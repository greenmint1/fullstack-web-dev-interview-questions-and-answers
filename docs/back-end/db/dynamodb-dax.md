# DynamoDB DAX Interview Questions and Answers

_Last updated: November 25, 2026_

This file has 450 interview questions and answers about Amazon DynamoDB Accelerator (DAX): 150 easy, 150 moderate and 150 advanced. The answers target DAX as it works in late 2026, with Node.js examples that use the DAX SDK for JavaScript v3 (`@amazon-dax-sdk/lib-dax`) next to the AWS SDK for JavaScript v3. The old `amazon-dax-client` package for SDK v2 is shown only where you will still see it in older projects.

## Table of Contents

- [Easy Questions (1-150)](#easy-questions-1-150)
- [Moderate Questions (151-300)](#moderate-questions-151-300)
- [Advanced Questions (301-450)](#advanced-questions-301-450)

### Easy Questions (1-150)

- [1: What is DynamoDB DAX?](#1-what-is-dynamodb-dax)
- [2: Why would you use DAX?](#2-why-would-you-use-dax)
- [3: Is DAX a separate database?](#3-is-dax-a-separate-database)
- [4: What does "API compatible with DynamoDB" mean for DAX?](#4-what-does-api-compatible-with-dynamodb-mean-for-dax)
- [5: What kind of latency can you expect from DAX?](#5-what-kind-of-latency-can-you-expect-from-dax)
- [6: What is a DAX cluster?](#6-what-is-a-dax-cluster)
- [7: What is a DAX node?](#7-what-is-a-dax-node)
- [8: What is the primary node in a DAX cluster?](#8-what-is-the-primary-node-in-a-dax-cluster)
- [9: What is a read replica in DAX?](#9-what-is-a-read-replica-in-dax)
- [10: How many nodes can a DAX cluster have?](#10-how-many-nodes-can-a-dax-cluster-have)
- [11: Why does AWS recommend at least three nodes for production?](#11-why-does-aws-recommend-at-least-three-nodes-for-production)
- [12: What is the item cache?](#12-what-is-the-item-cache)
- [13: What is the query cache?](#13-what-is-the-query-cache)
- [14: Are the item cache and query cache the same thing?](#14-are-the-item-cache-and-query-cache-the-same-thing)
- [15: What is the default TTL for items in DAX?](#15-what-is-the-default-ttl-for-items-in-dax)
- [16: What is TTL in DAX?](#16-what-is-ttl-in-dax)
- [17: What is a cache hit and a cache miss?](#17-what-is-a-cache-hit-and-a-cache-miss)
- [18: What does "read-through cache" mean for DAX?](#18-what-does-read-through-cache-mean-for-dax)
- [19: What does "write-through cache" mean for DAX?](#19-what-does-write-through-cache-mean-for-dax)
- [20: Which DynamoDB operations does DAX cache?](#20-which-dynamodb-operations-does-dax-cache)
- [21: Does DAX cache strongly consistent reads?](#21-does-dax-cache-strongly-consistent-reads)
- [22: What consistency model does DAX give for cached reads?](#22-what-consistency-model-does-dax-give-for-cached-reads)
- [23: Can you create a DynamoDB table through DAX?](#23-can-you-create-a-dynamodb-table-through-dax)
- [24: Does using DAX change the data stored in DynamoDB?](#24-does-using-dax-change-the-data-stored-in-dynamodb)
- [25: Where does a DAX cluster run?](#25-where-does-a-dax-cluster-run)
- [26: Can you connect to DAX from your laptop over the internet?](#26-can-you-connect-to-dax-from-your-laptop-over-the-internet)
- [27: What is the DAX cluster endpoint?](#27-what-is-the-dax-cluster-endpoint)
- [28: What is the difference between dax:// and daxs:// endpoints?](#28-what-is-the-difference-between-dax-and-daxs-endpoints)
- [29: Which ports does DAX use?](#29-which-ports-does-dax-use)
- [30: Which programming languages have DAX clients?](#30-which-programming-languages-have-dax-clients)
- [31: Which npm package do you use for DAX with AWS SDK v3?](#31-which-npm-package-do-you-use-for-dax-with-aws-sdk-v3)
- [32: What is the amazon-dax-client package?](#32-what-is-the-amazon-dax-client-package)
- [33: How do you create a DAX client in Node.js?](#33-how-do-you-create-a-dax-client-in-nodejs)
- [34: How do you read one item through DAX in Node.js?](#34-how-do-you-read-one-item-through-dax-in-nodejs)
- [35: How do you write an item through DAX in Node.js?](#35-how-do-you-write-an-item-through-dax-in-nodejs)
- [36: How do you run a Query through DAX in Node.js?](#36-how-do-you-run-a-query-through-dax-in-nodejs)
- [37: Do you need to change table design to use DAX?](#37-do-you-need-to-change-table-design-to-use-dax)
- [38: Does DAX work with global secondary indexes?](#38-does-dax-work-with-global-secondary-indexes)
- [39: Does DAX work with local secondary indexes?](#39-does-dax-work-with-local-secondary-indexes)
- [40: How does DAX help with hot keys?](#40-how-does-dax-help-with-hot-keys)
- [41: Does DAX reduce DynamoDB cost?](#41-does-dax-reduce-dynamodb-cost)
- [42: How is DAX priced?](#42-how-is-dax-priced)
- [43: What node types does DAX support?](#43-what-node-types-does-dax-support)
- [44: When should you use a T3 node type?](#44-when-should-you-use-a-t3-node-type)
- [45: Can you change the node type of an existing DAX cluster?](#45-can-you-change-the-node-type-of-an-existing-dax-cluster)
- [46: How do you add nodes to a DAX cluster?](#46-how-do-you-add-nodes-to-a-dax-cluster)
- [47: How do you remove nodes from a DAX cluster?](#47-how-do-you-remove-nodes-from-a-dax-cluster)
- [48: What is a subnet group in DAX?](#48-what-is-a-subnet-group-in-dax)
- [49: How do you create a DAX subnet group?](#49-how-do-you-create-a-dax-subnet-group)
- [50: What is a parameter group in DAX?](#50-what-is-a-parameter-group-in-dax)
- [51: How do you change the TTL of the DAX item cache?](#51-how-do-you-change-the-ttl-of-the-dax-item-cache)
- [52: What happens if you set the item cache TTL to 0?](#52-what-happens-if-you-set-the-item-cache-ttl-to-0)
- [53: What happens if you set the query cache TTL to 0?](#53-what-happens-if-you-set-the-query-cache-ttl-to-0)
- [54: What is LRU eviction in DAX?](#54-what-is-lru-eviction-in-dax)
- [55: What is negative caching in DAX?](#55-what-is-negative-caching-in-dax)
- [56: Does DAX support BatchGetItem?](#56-does-dax-support-batchgetitem)
- [57: Does DAX support BatchWriteItem?](#57-does-dax-support-batchwriteitem)
- [58: Does DAX support UpdateItem?](#58-does-dax-support-updateitem)
- [59: Does DAX support DeleteItem?](#59-does-dax-support-deleteitem)
- [60: Does DAX support transactions?](#60-does-dax-support-transactions)
- [61: What is a pass-through operation in DAX?](#61-what-is-a-pass-through-operation-in-dax)
- [62: Does DAX support conditional writes?](#62-does-dax-support-conditional-writes)
- [63: Does DAX support Scan?](#63-does-dax-support-scan)
- [64: Does DAX support pagination?](#64-does-dax-support-pagination)
- [65: What is the IAM service role for DAX?](#65-what-is-the-iam-service-role-for-dax)
- [66: What does the trust policy of the DAX service role look like?](#66-what-does-the-trust-policy-of-the-dax-service-role-look-like)
- [67: What IAM permissions does your app need to call DAX?](#67-what-iam-permissions-does-your-app-need-to-call-dax)
- [68: Can one DAX cluster cache more than one table?](#68-can-one-dax-cluster-cache-more-than-one-table)
- [69: Can DAX cache a table from another region?](#69-can-dax-cache-a-table-from-another-region)
- [70: Is DAX available in every AWS region?](#70-is-dax-available-in-every-aws-region)
- [71: How do you create a DAX cluster with the AWS CLI?](#71-how-do-you-create-a-dax-cluster-with-the-aws-cli)
- [72: How do you see details of a DAX cluster?](#72-how-do-you-see-details-of-a-dax-cluster)
- [73: How do you delete a DAX cluster?](#73-how-do-you-delete-a-dax-cluster)
- [74: Can you create a DAX cluster in the AWS console?](#74-can-you-create-a-dax-cluster-in-the-aws-console)
- [75: How long does it take to create a DAX cluster?](#75-how-long-does-it-take-to-create-a-dax-cluster)
- [76: What is the cluster status "available"?](#76-what-is-the-cluster-status-available)
- [77: What is encryption at rest in DAX?](#77-what-is-encryption-at-rest-in-dax)
- [78: Can you enable encryption at rest on an existing DAX cluster?](#78-can-you-enable-encryption-at-rest-on-an-existing-dax-cluster)
- [79: What is encryption in transit in DAX?](#79-what-is-encryption-in-transit-in-dax)
- [80: Can you enable encryption in transit on an existing cluster?](#80-can-you-enable-encryption-in-transit-on-an-existing-cluster)
- [81: Does DAX support customer managed KMS keys?](#81-does-dax-support-customer-managed-kms-keys)
- [82: What security group rules does DAX need?](#82-what-security-group-rules-does-dax-need)
- [83: What is a maintenance window in DAX?](#83-what-is-a-maintenance-window-in-dax)
- [84: How do you set the maintenance window?](#84-how-do-you-set-the-maintenance-window)
- [85: What is the SNS notification setting in DAX?](#85-what-is-the-sns-notification-setting-in-dax)
- [86: Does DAX replace a failed node automatically?](#86-does-dax-replace-a-failed-node-automatically)
- [87: What happens to the cache when a node restarts?](#87-what-happens-to-the-cache-when-a-node-restarts)
- [88: How do you reboot a DAX node?](#88-how-do-you-reboot-a-dax-node)
- [89: Can DAX be used with DynamoDB on-demand tables?](#89-can-dax-be-used-with-dynamodb-on-demand-tables)
- [90: Do you still need DynamoDB capacity when using DAX?](#90-do-you-still-need-dynamodb-capacity-when-using-dax)
- [91: What is a cold cache?](#91-what-is-a-cold-cache)
- [92: What is a warm cache?](#92-what-is-a-warm-cache)
- [93: What is the cache hit ratio?](#93-what-is-the-cache-hit-ratio)
- [94: Which CloudWatch namespace do DAX metrics use?](#94-which-cloudwatch-namespace-do-dax-metrics-use)
- [95: What are the main DAX CloudWatch metrics?](#95-what-are-the-main-dax-cloudwatch-metrics)
- [96: What does the ThrottledRequestCount metric show?](#96-what-does-the-throttledrequestcount-metric-show)
- [97: What does the EvictedSize metric show?](#97-what-does-the-evictedsize-metric-show)
- [98: What does CacheMemoryUtilization show?](#98-what-does-cachememoryutilization-show)
- [99: What is the difference between ErrorRequestCount and FaultRequestCount?](#99-what-is-the-difference-between-errorrequestcount-and-faultrequestcount)
- [100: Does DAX log API calls in CloudTrail?](#100-does-dax-log-api-calls-in-cloudtrail)
- [101: Can you use DAX from AWS Lambda?](#101-can-you-use-dax-from-aws-lambda)
- [102: Can you use DAX from ECS or EKS?](#102-can-you-use-dax-from-ecs-or-eks)
- [103: Can you use DAX from an EC2 instance?](#103-can-you-use-dax-from-an-ec2-instance)
- [104: Does DAX work with DynamoDB Local?](#104-does-dax-work-with-dynamodb-local)
- [105: How can you switch between DAX and DynamoDB in code?](#105-how-can-you-switch-between-dax-and-dynamodb-in-code)
- [106: What is the difference between DaxDocument and DynamoDBDocument?](#106-what-is-the-difference-between-daxdocument-and-dynamodbdocument)
- [107: Does DAX return data in the same format as DynamoDB?](#107-does-dax-return-data-in-the-same-format-as-dynamodb)
- [108: Can you tell from the response whether it was a cache hit?](#108-can-you-tell-from-the-response-whether-it-was-a-cache-hit)
- [109: Does DAX return ConsumedCapacity?](#109-does-dax-return-consumedcapacity)
- [110: What are good use cases for DAX?](#110-what-are-good-use-cases-for-dax)
- [111: When is DAX not a good fit?](#111-when-is-dax-not-a-good-fit)
- [112: Is DAX a good fit for write-heavy apps?](#112-is-dax-a-good-fit-for-write-heavy-apps)
- [113: What is the difference between DAX and ElastiCache?](#113-what-is-the-difference-between-dax-and-elasticache)
- [114: When would you choose ElastiCache over DAX?](#114-when-would-you-choose-elasticache-over-dax)
- [115: Is DAX the same as DynamoDB's internal cache?](#115-is-dax-the-same-as-dynamodbs-internal-cache)
- [116: Does DAX store data on disk?](#116-does-dax-store-data-on-disk)
- [117: Can DAX be used as a session store on its own?](#117-can-dax-be-used-as-a-session-store-on-its-own)
- [118: What is the working set in caching?](#118-what-is-the-working-set-in-caching)
- [119: Does every DAX node hold the same data?](#119-does-every-dax-node-hold-the-same-data)
- [120: How does the DAX client pick a node?](#120-how-does-the-dax-client-pick-a-node)
- [121: Why should you reuse the DAX client object?](#121-why-should-you-reuse-the-dax-client-object)
- [122: Do you need a load balancer in front of DAX?](#122-do-you-need-a-load-balancer-in-front-of-dax)
- [123: Can you use the normal AWS SDK DynamoDB client to talk to DAX?](#123-can-you-use-the-normal-aws-sdk-dynamodb-client-to-talk-to-dax)
- [124: Can you call DAX with curl or a REST client?](#124-can-you-call-dax-with-curl-or-a-rest-client)
- [125: What is a DAX node endpoint?](#125-what-is-a-dax-node-endpoint)
- [126: What happens if the DAX cluster is down?](#126-what-happens-if-the-dax-cluster-is-down)
- [127: Does DAX retry failed requests?](#127-does-dax-retry-failed-requests)
- [128: What happens when DynamoDB throttles a DAX request?](#128-what-happens-when-dynamodb-throttles-a-dax-request)
- [129: What happens when a DAX node is overloaded?](#129-what-happens-when-a-dax-node-is-overloaded)
- [130: What is the replication factor in DAX?](#130-what-is-the-replication-factor-in-dax)
- [131: Can you stop a DAX cluster to save money?](#131-can-you-stop-a-dax-cluster-to-save-money)
- [132: Can you tag a DAX cluster?](#132-can-you-tag-a-dax-cluster)
- [133: Can you create DAX with CloudFormation?](#133-can-you-create-dax-with-cloudformation)
- [134: Can you create DAX with the AWS CDK?](#134-can-you-create-dax-with-the-aws-cdk)
- [135: Can you create DAX with Terraform?](#135-can-you-create-dax-with-terraform)
- [136: Is DAX serverless?](#136-is-dax-serverless)
- [137: Does DAX scale automatically?](#137-does-dax-scale-automatically)
- [138: Can you scale DAX for more reads?](#138-can-you-scale-dax-for-more-reads)
- [139: Can you scale DAX for more memory?](#139-can-you-scale-dax-for-more-memory)
- [140: Does adding more nodes speed up writes?](#140-does-adding-more-nodes-speed-up-writes)
- [141: What is the max size of an item in DAX?](#141-what-is-the-max-size-of-an-item-in-dax)
- [142: Does DAX change DynamoDB limits?](#142-does-dax-change-dynamodb-limits)
- [143: What is DAX's effect on read cost for eventually consistent reads?](#143-what-is-daxs-effect-on-read-cost-for-eventually-consistent-reads)
- [144: What are the main parts you set up to use DAX?](#144-what-are-the-main-parts-you-set-up-to-use-dax)
- [145: Do you need to warm up DAX manually?](#145-do-you-need-to-warm-up-dax-manually)
- [146: Does DAX support PutItem with ReturnValues?](#146-does-dax-support-putitem-with-returnvalues)
- [147: Does DAX support ProjectionExpression?](#147-does-dax-support-projectionexpression)
- [148: Does DAX support filter expressions?](#148-does-dax-support-filter-expressions)
- [149: Does DAX work with DynamoDB Streams?](#149-does-dax-work-with-dynamodb-streams)
- [150: What is the most important thing to remember about DAX consistency?](#150-what-is-the-most-important-thing-to-remember-about-dax-consistency)

### Moderate Questions (151-300)

- [151: What permissions policy should the DAX service role have?](#151-what-permissions-policy-should-the-dax-service-role-have)
- [152: What does an app policy for DAX look like?](#152-what-does-an-app-policy-for-dax-look-like)
- [153: Why do DAX management actions use Resource "*"?](#153-why-do-dax-management-actions-use-resource-)
- [154: Why can DAX weaken table level IAM rules?](#154-why-can-dax-weaken-table-level-iam-rules)
- [155: How do you give a read-only app access through DAX?](#155-how-do-you-give-a-read-only-app-access-through-dax)
- [156: How do you connect to a TLS enabled DAX cluster in Node.js?](#156-how-do-you-connect-to-a-tls-enabled-dax-cluster-in-nodejs)
- [157: Where should you store the DAX endpoint for an app?](#157-where-should-you-store-the-dax-endpoint-for-an-app)
- [158: How do you fall back to DynamoDB when DAX is not reachable?](#158-how-do-you-fall-back-to-dynamodb-when-dax-is-not-reachable)
- [159: How do you handle a failed condition through DAX?](#159-how-do-you-handle-a-failed-condition-through-dax)
- [160: How do you retry throttled DAX requests?](#160-how-do-you-retry-throttled-dax-requests)
- [161: If you write an item through DAX and read it right away, do you get the new value?](#161-if-you-write-an-item-through-dax-and-read-it-right-away-do-you-get-the-new-value)
- [162: How do you get read-your-own-writes behavior with DAX?](#162-how-do-you-get-read-your-own-writes-behavior-with-dax)
- [163: Why can a Query return old data right after a write through DAX?](#163-why-can-a-query-return-old-data-right-after-a-write-through-dax)
- [164: How can you deal with stale query cache results?](#164-how-can-you-deal-with-stale-query-cache-results)
- [165: How do you pick TTL values for DAX?](#165-how-do-you-pick-ttl-values-for-dax)
- [166: Why would you set different TTLs for the item cache and the query cache?](#166-why-would-you-set-different-ttls-for-the-item-cache-and-the-query-cache)
- [167: How do you attach a parameter group to a cluster?](#167-how-do-you-attach-a-parameter-group-to-a-cluster)
- [168: Do TTL changes affect items that are already cached?](#168-do-ttl-changes-affect-items-that-are-already-cached)
- [169: How do you see the current parameter values?](#169-how-do-you-see-the-current-parameter-values)
- [170: What is write-around and when would you use it with DAX?](#170-what-is-write-around-and-when-would-you-use-it-with-dax)
- [171: What is cache pollution?](#171-what-is-cache-pollution)
- [172: Are writes through DAX slower than writes to DynamoDB?](#172-are-writes-through-dax-slower-than-writes-to-dynamodb)
- [173: How do you measure whether DAX actually helps your app?](#173-how-do-you-measure-whether-dax-actually-helps-your-app)
- [174: How do you create an alarm for a low cache hit rate?](#174-how-do-you-create-an-alarm-for-a-low-cache-hit-rate)
- [175: When should you add nodes based on CPU?](#175-when-should-you-add-nodes-based-on-cpu)
- [176: What can cause a low item cache hit rate?](#176-what-can-cause-a-low-item-cache-hit-rate)
- [177: How does the query cache key work, and why does it matter?](#177-how-does-the-query-cache-key-work-and-why-does-it-matter)
- [178: Why is it bad to put the current time in a DAX query?](#178-why-is-it-bad-to-put-the-current-time-in-a-dax-query)
- [179: How do you handle UnprocessedKeys from BatchGetItem through DAX?](#179-how-do-you-handle-unprocessedkeys-from-batchgetitem-through-dax)
- [180: How do you handle UnprocessedItems from BatchWriteItem through DAX?](#180-how-do-you-handle-unprocesseditems-from-batchwriteitem-through-dax)
- [181: How do you run a transaction through DAX?](#181-how-do-you-run-a-transaction-through-dax)
- [182: Should you read account balances through DAX?](#182-should-you-read-account-balances-through-dax)
- [183: How does DAX fit single-table design?](#183-how-does-dax-fit-single-table-design)
- [184: Are GSI query results through DAX more stale than normal?](#184-are-gsi-query-results-through-dax-more-stale-than-normal)
- [185: How does pagination interact with the query cache?](#185-how-does-pagination-interact-with-the-query-cache)
- [186: When is Scan through DAX a bad idea?](#186-when-is-scan-through-dax-a-bad-idea)
- [187: How does Lambda cold start affect DAX use?](#187-how-does-lambda-cold-start-affect-dax-use)
- [188: Does a Lambda in a VPC with DAX also need internet access?](#188-does-a-lambda-in-a-vpc-with-dax-also-need-internet-access)
- [189: How do you set up security groups for DAX with the CLI?](#189-how-do-you-set-up-security-groups-for-dax-with-the-cli)
- [190: Can an app in another VPC use a DAX cluster?](#190-can-an-app-in-another-vpc-use-a-dax-cluster)
- [191: How do you unit test code that uses DAX?](#191-how-do-you-unit-test-code-that-uses-dax)
- [192: How do you run integration tests against DAX?](#192-how-do-you-run-integration-tests-against-dax)
- [193: How do you move from amazon-dax-client (v2) to lib-dax (v3)?](#193-how-do-you-move-from-amazon-dax-client-v2-to-lib-dax-v3)
- [194: Why move from the v2 DAX client to the v3 one?](#194-why-move-from-the-v2-dax-client-to-the-v3-one)
- [195: Can you use DAX with TypeScript?](#195-can-you-use-dax-with-typescript)
- [196: How do you estimate the cost of DAX?](#196-how-do-you-estimate-the-cost-of-dax)
- [197: When can DAX cost more than it saves?](#197-when-can-dax-cost-more-than-it-saves)
- [198: How do you choose a DAX node type?](#198-how-do-you-choose-a-dax-node-type)
- [199: Why can load testing on T2 nodes mislead you?](#199-why-can-load-testing-on-t2-nodes-mislead-you)
- [200: What is the CPU credit issue with T3 nodes?](#200-what-is-the-cpu-credit-issue-with-t3-nodes)
- [201: How do you place DAX nodes in specific Availability Zones?](#201-how-do-you-place-dax-nodes-in-specific-availability-zones)
- [202: Does cross-AZ traffic matter for DAX?](#202-does-cross-az-traffic-matter-for-dax)
- [203: How should an app handle errors during DAX maintenance?](#203-how-should-an-app-handle-errors-during-dax-maintenance)
- [204: How do you see recent events for a DAX cluster?](#204-how-do-you-see-recent-events-for-a-dax-cluster)
- [205: How do you send DAX events to an SNS topic?](#205-how-do-you-send-dax-events-to-an-sns-topic)
- [206: How do you change a cluster's node type with no downtime?](#206-how-do-you-change-a-clusters-node-type-with-no-downtime)
- [207: How do you write a warm-up script for DAX?](#207-how-do-you-write-a-warm-up-script-for-dax)
- [208: What does the client see when the primary node fails?](#208-what-does-the-client-see-when-the-primary-node-fails)
- [209: Does DAX help with write throttling on hot partitions?](#209-does-dax-help-with-write-throttling-on-hot-partitions)
- [210: Can you lower provisioned read capacity after adding DAX?](#210-can-you-lower-provisioned-read-capacity-after-adding-dax)
- [211: Why is on-demand mode often paired with DAX?](#211-why-is-on-demand-mode-often-paired-with-dax)
- [212: What is the negative caching gotcha with DAX?](#212-what-is-the-negative-caching-gotcha-with-dax)
- [213: What happens if you delete an item directly in DynamoDB?](#213-what-happens-if-you-delete-an-item-directly-in-dynamodb)
- [214: Does DynamoDB TTL deletion update the DAX cache?](#214-does-dynamodb-ttl-deletion-update-the-dax-cache)
- [215: How does DAX work with DynamoDB global tables?](#215-how-does-dax-work-with-dynamodb-global-tables)
- [216: Can you invalidate a single item in DAX?](#216-can-you-invalidate-a-single-item-in-dax)
- [217: Can you flush the whole DAX cache?](#217-can-you-flush-the-whole-dax-cache)
- [218: What should you log when a DAX call fails?](#218-what-should-you-log-when-a-dax-call-fails)
- [219: What does the ClientConnections metric tell you?](#219-what-does-the-clientconnections-metric-tell-you)
- [220: How do you use DAX in an Express app?](#220-how-do-you-use-dax-in-an-express-app)
- [221: How does DAX fit a CQRS read model?](#221-how-does-dax-fit-a-cqrs-read-model)
- [222: Is DAX a good fit for a leaderboard?](#222-is-dax-a-good-fit-for-a-leaderboard)
- [223: What is the problem with reading counters through DAX?](#223-what-is-the-problem-with-reading-counters-through-dax)
- [224: How does optimistic locking work with DAX?](#224-how-does-optimistic-locking-work-with-dax)
- [225: Why is mixing DAX and direct DynamoDB writes risky?](#225-why-is-mixing-dax-and-direct-dynamodb-writes-risky)
- [226: Which reads should skip the cache?](#226-which-reads-should-skip-the-cache)
- [227: How do you choose between Query and GetItem when using DAX?](#227-how-do-you-choose-between-query-and-getitem-when-using-dax)
- [228: Why might BatchGetItem be better than Query for known IDs with DAX?](#228-why-might-batchgetitem-be-better-than-query-for-known-ids-with-dax)
- [229: How can you design access patterns to work well with DAX?](#229-how-can-you-design-access-patterns-to-work-well-with-dax)
- [230: How can you cache an expensive aggregate with DAX?](#230-how-can-you-cache-an-expensive-aggregate-with-dax)
- [231: What happens to the table when a cold DAX cluster gets full production traffic?](#231-what-happens-to-the-table-when-a-cold-dax-cluster-gets-full-production-traffic)
- [232: Should you use an in-process cache, DAX or both?](#232-should-you-use-an-in-process-cache-dax-or-both)
- [233: What is the downside of stacking an in-process cache on top of DAX?](#233-what-is-the-downside-of-stacking-an-in-process-cache-on-top-of-dax)
- [234: How does DAX compare to caching at the API layer, like CloudFront?](#234-how-does-dax-compare-to-caching-at-the-api-layer-like-cloudfront)
- [235: How do you handle time-sensitive data like prices with DAX?](#235-how-do-you-handle-time-sensitive-data-like-prices-with-dax)
- [236: Should microservices share one DAX cluster?](#236-should-microservices-share-one-dax-cluster)
- [237: Do Step Functions DynamoDB integrations go through DAX?](#237-do-step-functions-dynamodb-integrations-go-through-dax)
- [238: Do AppSync DynamoDB resolvers use DAX?](#238-do-appsync-dynamodb-resolvers-use-dax)
- [239: Can you share a parameter group across clusters?](#239-can-you-share-a-parameter-group-across-clusters)
- [240: How do you check which parameter group a cluster uses?](#240-how-do-you-check-which-parameter-group-a-cluster-uses)
- [241: Does a cluster need internet access or a NAT gateway?](#241-does-a-cluster-need-internet-access-or-a-nat-gateway)
- [242: How do you debug "connection timeout" errors to DAX?](#242-how-do-you-debug-connection-timeout-errors-to-dax)
- [243: What happens if you use dax:// on a TLS cluster?](#243-what-happens-if-you-use-dax-on-a-tls-cluster)
- [244: How do you change security groups on a running cluster?](#244-how-do-you-change-security-groups-on-a-running-cluster)
- [245: How do you set up a cheap DAX cluster for development?](#245-how-do-you-set-up-a-cheap-dax-cluster-for-development)
- [246: Why should DAX cluster names not contain sensitive information?](#246-why-should-dax-cluster-names-not-contain-sensitive-information)
- [247: Can DAX use IPv6?](#247-can-dax-use-ipv6)
- [248: Does item size affect DAX performance?](#248-does-item-size-affect-dax-performance)
- [249: Why should you avoid unbounded attribute names with DAX?](#249-why-should-you-avoid-unbounded-attribute-names-with-dax)
- [250: What is a noisy neighbor problem in a shared DAX cluster?](#250-what-is-a-noisy-neighbor-problem-in-a-shared-dax-cluster)
- [251: Should each environment have its own DAX cluster?](#251-should-each-environment-have-its-own-dax-cluster)
- [252: Where do you check DAX limits like nodes per cluster?](#252-where-do-you-check-dax-limits-like-nodes-per-cluster)
- [253: What should a DAX dashboard show?](#253-what-should-a-dax-dashboard-show)
- [254: Which CloudWatch alarms should you set for DAX?](#254-which-cloudwatch-alarms-should-you-set-for-dax)
- [255: How do you find the cause of high read latency with DAX?](#255-how-do-you-find-the-cause-of-high-read-latency-with-dax)
- [256: Why would a team see almost no cache hits after adding DAX?](#256-why-would-a-team-see-almost-no-cache-hits-after-adding-dax)
- [257: Why do cache misses jump after every deploy?](#257-why-do-cache-misses-jump-after-every-deploy)
- [258: Which changes force a new DAX cluster in CloudFormation?](#258-which-changes-force-a-new-dax-cluster-in-cloudformation)
- [259: How does a "top N" query behave in the query cache?](#259-how-does-a-top-n-query-behave-in-the-query-cache)
- [260: Should DAX nodes go in public or private subnets?](#260-should-dax-nodes-go-in-public-or-private-subnets)
- [261: How do you roll out DAX to an existing app safely?](#261-how-do-you-roll-out-dax-to-an-existing-app-safely)
- [262: How do you use a feature flag to turn DAX on and off?](#262-how-do-you-use-a-feature-flag-to-turn-dax-on-and-off)
- [263: Can you send only part of the traffic through DAX?](#263-can-you-send-only-part-of-the-traffic-through-dax)
- [264: Does TransactWriteItems idempotency work through DAX?](#264-does-transactwriteitems-idempotency-work-through-dax)
- [265: Is DAX good for a feature flags or config table?](#265-is-dax-good-for-a-feature-flags-or-config-table)
- [266: How would you use DAX for user profile reads?](#266-how-would-you-use-dax-for-user-profile-reads)
- [267: How would you set up DAX for a product catalog?](#267-how-would-you-set-up-dax-for-a-product-catalog)
- [268: Why is DAX popular in gaming backends?](#268-why-is-dax-popular-in-gaming-backends)
- [269: Why is DAX used in ad tech?](#269-why-is-dax-used-in-ad-tech)
- [270: How do you use DAX in a multi-region active-active setup?](#270-how-do-you-use-dax-in-a-multi-region-active-active-setup)
- [271: How do you see how much load DAX removes from the table?](#271-how-do-you-see-how-much-load-dax-removes-from-the-table)
- [272: Which metrics show request volume per operation?](#272-which-metrics-show-request-volume-per-operation)
- [273: How do you tell DAX throttling apart from DynamoDB throttling?](#273-how-do-you-tell-dax-throttling-apart-from-dynamodb-throttling)
- [274: What is FailedRequestCount in DAX?](#274-what-is-failedrequestcount-in-dax)
- [275: What do the network utilization metrics show?](#275-what-do-the-network-utilization-metrics-show)
- [276: What does the EstimatedDbSize metric show?](#276-what-does-the-estimateddbsize-metric-show)
- [277: What are ScanCacheHits and ScanCacheMisses?](#277-what-are-scancachehits-and-scancachemisses)
- [278: Do you need to back up a DAX cluster?](#278-do-you-need-to-back-up-a-dax-cluster)
- [279: What happens with DAX when you restore a DynamoDB table?](#279-what-happens-with-dax-when-you-restore-a-dynamodb-table)
- [280: What do you need to change when adding a new table to an existing DAX cluster?](#280-what-do-you-need-to-change-when-adding-a-new-table-to-an-existing-dax-cluster)
- [281: What happens if the DAX service role lacks permission on a table?](#281-what-happens-if-the-dax-service-role-lacks-permission-on-a-table)
- [282: What happens if the app's role lacks a dax: permission?](#282-what-happens-if-the-apps-role-lacks-a-dax-permission)
- [283: Does adding a GSI to a table affect DAX?](#283-does-adding-a-gsi-to-a-table-affect-dax)
- [284: How should you use DAX with Node.js cluster mode or several processes?](#284-how-should-you-use-dax-with-nodejs-cluster-mode-or-several-processes)
- [285: Can one DAX client handle many requests at the same time?](#285-can-one-dax-client-handle-many-requests-at-the-same-time)
- [286: How do you set up a Lambda with DAX using AWS SAM?](#286-how-do-you-set-up-a-lambda-with-dax-using-aws-sam)
- [287: How do you add a health check for DAX in your app?](#287-how-do-you-add-a-health-check-for-dax-in-your-app)
- [288: How do you track DAX cost per team?](#288-how-do-you-track-dax-cost-per-team)
- [289: Should batch jobs read through DAX?](#289-should-batch-jobs-read-through-dax)
- [290: What is the best way to run analytics on data behind DAX?](#290-what-is-the-best-way-to-run-analytics-on-data-behind-dax)
- [291: What happens step by step on a GetItem cache miss?](#291-what-happens-step-by-step-on-a-getitem-cache-miss)
- [292: What happens step by step on a PutItem through DAX?](#292-what-happens-step-by-step-on-a-putitem-through-dax)
- [293: Why should you avoid reading items you just scanned again through DAX?](#293-why-should-you-avoid-reading-items-you-just-scanned-again-through-dax)
- [294: What happens to query cache entries when an item in the result is deleted through DAX?](#294-what-happens-to-query-cache-entries-when-an-item-in-the-result-is-deleted-through-dax)
- [295: Can you use DAX with ExpressionAttributeNames for reserved words?](#295-can-you-use-dax-with-expressionattributenames-for-reserved-words)
- [296: Does DAX support all DynamoDB data types?](#296-does-dax-support-all-dynamodb-data-types)
- [297: How do you handle numbers bigger than JavaScript can hold with DAX?](#297-how-do-you-handle-numbers-bigger-than-javascript-can-hold-with-dax)
- [298: What would you check before turning on DAX for an existing table?](#298-what-would-you-check-before-turning-on-dax-for-an-existing-table)
- [299: How do you explain DAX to a non-technical stakeholder?](#299-how-do-you-explain-dax-to-a-non-technical-stakeholder)
- [300: What are the most common mistakes teams make with DAX?](#300-what-are-the-most-common-mistakes-teams-make-with-dax)

### Advanced Questions (301-450)

- [301: How does replication between the primary and read replicas work in DAX?](#301-how-does-replication-between-the-primary-and-read-replicas-work-in-dax)
- [302: Why are reads through DAX eventually consistent even if all writes go through DAX?](#302-why-are-reads-through-dax-eventually-consistent-even-if-all-writes-go-through-dax)
- [303: Why doesn't DAX update the query cache when an item changes?](#303-why-doesnt-dax-update-the-query-cache-when-an-item-changes)
- [304: Why can't DAX cache strongly consistent reads?](#304-why-cant-dax-cache-strongly-consistent-reads)
- [305: Why does DAX pass TransactGetItems straight to DynamoDB?](#305-why-does-dax-pass-transactgetitems-straight-to-dynamodb)
- [306: Why does DAX write to DynamoDB before updating its cache?](#306-why-does-dax-write-to-dynamodb-before-updating-its-cache)
- [307: Why is DAX write-through and not write-back?](#307-why-is-dax-write-through-and-not-write-back)
- [308: Describe a race where DAX keeps an older value even though every write succeeded.](#308-describe-a-race-where-dax-keeps-an-older-value-even-though-every-write-succeeded)
- [309: How can a stale DAX read cause a lost update?](#309-how-can-a-stale-dax-read-cause-a-lost-update)
- [310: Why is a conditional write safe even if your read came from a stale cache?](#310-why-is-a-conditional-write-safe-even-if-your-read-came-from-a-stale-cache)
- [311: What happens inside DAX when the primary node fails?](#311-what-happens-inside-dax-when-the-primary-node-fails)
- [312: A write through DAX times out during a failover. Did it succeed?](#312-a-write-through-dax-times-out-during-a-failover-did-it-succeed)
- [313: How does a three node, three AZ cluster behave when one AZ goes down?](#313-how-does-a-three-node-three-az-cluster-behave-when-one-az-goes-down)
- [314: Why doesn't adding nodes increase total DAX cache size?](#314-why-doesnt-adding-nodes-increase-total-dax-cache-size)
- [315: How is DAX's scaling model different from a sharded cache like ElastiCache cluster mode?](#315-how-is-daxs-scaling-model-different-from-a-sharded-cache-like-elasticache-cluster-mode)
- [316: Why does DAX handle hot keys well?](#316-why-does-dax-handle-hot-keys-well)
- [317: How do you calculate how many nodes you need for read throughput?](#317-how-do-you-calculate-how-many-nodes-you-need-for-read-throughput)
- [318: Walk through a sizing example for DAX.](#318-walk-through-a-sizing-example-for-dax)
- [319: How do you estimate memory needs for the item cache?](#319-how-do-you-estimate-memory-needs-for-the-item-cache)
- [320: Why should you keep spare capacity in a DAX cluster?](#320-why-should-you-keep-spare-capacity-in-a-dax-cluster)
- [321: What is a thundering herd problem with DAX?](#321-what-is-a-thundering-herd-problem-with-dax)
- [322: Why do all items in a DAX cluster share the same TTL, and what does it mean for design?](#322-why-do-all-items-in-a-dax-cluster-share-the-same-ttl-and-what-does-it-mean-for-design)
- [323: When would you run several DAX clusters for the same app?](#323-when-would-you-run-several-dax-clusters-for-the-same-app)
- [324: How can high-cardinality queries blow up the query cache?](#324-how-can-high-cardinality-queries-blow-up-the-query-cache)
- [325: How do LRU and TTL work together?](#325-how-do-lru-and-ttl-work-together)
- [326: Explain the attribute name metadata issue in more detail.](#326-explain-the-attribute-name-metadata-issue-in-more-detail)
- [327: How do item size and request rate affect node network limits?](#327-how-do-item-size-and-request-rate-affect-node-network-limits)
- [328: Why may p99 latency barely improve after adding DAX?](#328-why-may-p99-latency-barely-improve-after-adding-dax)
- [329: How do you calculate the expected average read latency with DAX?](#329-how-do-you-calculate-the-expected-average-read-latency-with-dax)
- [330: How can a busy Node.js event loop hide DAX speed?](#330-how-can-a-busy-nodejs-event-loop-hide-dax-speed)
- [331: How should you benchmark DAX correctly?](#331-how-should-you-benchmark-dax-correctly)
- [332: What security layers protect a DAX cluster?](#332-what-security-layers-protect-a-dax-cluster)
- [333: Do fine-grained IAM conditions like dynamodb:LeadingKeys work through DAX?](#333-do-fine-grained-iam-conditions-like-dynamodbleadingkeys-work-through-dax)
- [334: How do you isolate tenants in a multi-tenant SaaS app that uses DAX?](#334-how-do-you-isolate-tenants-in-a-multi-tenant-saas-app-that-uses-dax)
- [335: Your compliance team requires customer managed KMS keys. Can you use DAX?](#335-your-compliance-team-requires-customer-managed-kms-keys-can-you-use-dax)
- [336: Does TLS add much latency to DAX?](#336-does-tls-add-much-latency-to-dax)
- [337: How would you apply least privilege to a DAX setup?](#337-how-would-you-apply-least-privilege-to-a-dax-setup)
- [338: How do you audit who accessed data through DAX?](#338-how-do-you-audit-who-accessed-data-through-dax)
- [339: Why should dev and prod never share a DAX cluster?](#339-why-should-dev-and-prod-never-share-a-dax-cluster)
- [340: How do you plan disaster recovery for DAX?](#340-how-do-you-plan-disaster-recovery-for-dax)
- [341: How do you design cross-region DR with DAX?](#341-how-do-you-design-cross-region-dr-with-dax)
- [342: How do global tables' conflict rules interact with DAX?](#342-how-do-global-tables-conflict-rules-interact-with-dax)
- [343: When can write-through make cache use worse?](#343-when-can-write-through-make-cache-use-worse)
- [344: How would you decide which writes go through DAX?](#344-how-would-you-decide-which-writes-go-through-dax)
- [345: How should stream processors write to tables behind DAX?](#345-how-should-stream-processors-write-to-tables-behind-dax)
- [346: Why is "rewrite the item through DAX on every stream event" a bad idea?](#346-why-is-rewrite-the-item-through-dax-on-every-stream-event-a-bad-idea)
- [347: What is the worst-case staleness for an item read with GetItem through DAX?](#347-what-is-the-worst-case-staleness-for-an-item-read-with-getitem-through-dax)
- [348: What is the worst-case staleness for a Query through DAX on a GSI?](#348-what-is-the-worst-case-staleness-for-a-query-through-dax-on-a-gsi)
- [349: Is a BatchGetItem response through DAX a consistent snapshot?](#349-is-a-batchgetitem-response-through-dax-a-consistent-snapshot)
- [350: What happens with Select COUNT queries through DAX?](#350-what-happens-with-select-count-queries-through-dax)
- [351: How do you make write retries safe through DAX after a timeout?](#351-how-do-you-make-write-retries-safe-through-dax-after-a-timeout)
- [352: Why are increments risky to retry through DAX?](#352-why-are-increments-risky-to-retry-through-dax)
- [353: How would you add a circuit breaker for DAX in Node.js?](#353-how-would-you-add-a-circuit-breaker-for-dax-in-nodejs)
- [354: What is the risk of falling back to DynamoDB when DAX fails?](#354-what-is-the-risk-of-falling-back-to-dynamodb-when-dax-fails)
- [355: How would you design graceful degradation for a read-heavy API using DAX?](#355-how-would-you-design-graceful-degradation-for-a-read-heavy-api-using-dax)
- [356: How do you warm a new cluster before switching traffic to it?](#356-how-do-you-warm-a-new-cluster-before-switching-traffic-to-it)
- [357: Why can Lambda at high concurrency create too many DAX connections?](#357-why-can-lambda-at-high-concurrency-create-too-many-dax-connections)
- [358: How do idle Lambda environments affect DAX connections?](#358-how-do-idle-lambda-environments-affect-dax-connections)
- [359: When is DynamoDB alone fast enough so DAX isn't needed?](#359-when-is-dynamodb-alone-fast-enough-so-dax-isnt-needed)
- [360: How do you model DAX cost against DynamoDB read savings?](#360-how-do-you-model-dax-cost-against-dynamodb-read-savings)
- [361: How do you choose between R5 and R7i node types?](#361-how-do-you-choose-between-r5-and-r7i-node-types)
- [362: What should you do before reducing the number of nodes?](#362-what-should-you-do-before-reducing-the-number-of-nodes)
- [363: What happens right after you add a node?](#363-what-happens-right-after-you-add-a-node)
- [364: How can you automate DAX scaling since there's no auto scaling?](#364-how-can-you-automate-dax-scaling-since-theres-no-auto-scaling)
- [365: How do you scale DAX for predictable daily peaks?](#365-how-do-you-scale-dax-for-predictable-daily-peaks)
- [366: How do you test DAX failover?](#366-how-do-you-test-dax-failover)
- [367: Why might your tracing tool not show DAX calls?](#367-why-might-your-tracing-tool-not-show-dax-calls)
- [368: How do you add manual tracing around DAX calls with OpenTelemetry?](#368-how-do-you-add-manual-tracing-around-dax-calls-with-opentelemetry)
- [369: How can you get hit or miss info per request without CloudWatch?](#369-how-can-you-get-hit-or-miss-info-per-request-without-cloudwatch)
- [370: Users report seeing old data for a few minutes after editing a post. How do you debug it?](#370-users-report-seeing-old-data-for-a-few-minutes-after-editing-a-post-how-do-you-debug-it)
- [371: Deleted comments still appear in lists for a while. Why?](#371-deleted-comments-still-appear-in-lists-for-a-while-why)
- [372: New users get "not found" right after signup. What could cause it?](#372-new-users-get-not-found-right-after-signup-what-could-cause-it)
- [373: A product launch throttled the table even though DAX was in place. What went wrong?](#373-a-product-launch-throttled-the-table-even-though-dax-was-in-place-what-went-wrong)
- [374: Only the primary node shows high CPU. What does that tell you?](#374-only-the-primary-node-shows-high-cpu-what-does-that-tell-you)
- [375: Evictions jumped after a new feature shipped. What would you check?](#375-evictions-jumped-after-a-new-feature-shipped-what-would-you-check)
- [376: Latency spikes happen every Sunday morning. What's a likely reason?](#376-latency-spikes-happen-every-sunday-morning-whats-a-likely-reason)
- [377: A small app pays more for DAX than for DynamoDB. What do you do?](#377-a-small-app-pays-more-for-dax-than-for-dynamodb-what-do-you-do)
- [378: How would you migrate from an ElastiCache cache-aside setup to DAX?](#378-how-would-you-migrate-from-an-elasticache-cache-aside-setup-to-dax)
- [379: When would you move from DAX to ElastiCache?](#379-when-would-you-move-from-dax-to-elasticache)
- [380: One tenant's traffic is pushing other tenants' data out of DAX. What can you do?](#380-one-tenants-traffic-is-pushing-other-tenants-data-out-of-dax-what-can-you-do)
- [381: Your app needs low latency reads in three regions. How do you design it with DAX?](#381-your-app-needs-low-latency-reads-in-three-regions-how-do-you-design-it-with-dax)
- [382: Lambda functions time out when calling DAX. What would you check?](#382-lambda-functions-time-out-when-calling-dax-what-would-you-check)
- [383: Two requests from the same user show different values for the same item. Why?](#383-two-requests-from-the-same-user-show-different-values-for-the-same-item-why)
- [384: Can you make the DAX client always read from the same node?](#384-can-you-make-the-dax-client-always-read-from-the-same-node)
- [385: What is monotonic read consistency, and does DAX provide it?](#385-what-is-monotonic-read-consistency-and-does-dax-provide-it)
- [386: How can a version attribute help detect stale reads from DAX?](#386-how-can-a-version-attribute-help-detect-stale-reads-from-dax)
- [387: How do you avoid re-reading after an update when using DAX?](#387-how-do-you-avoid-re-reading-after-an-update-when-using-dax)
- [388: Why would you split an item into a read-hot part and a write-hot part?](#388-why-would-you-split-an-item-into-a-read-hot-part-and-a-write-hot-part)
- [389: Why can splitting large items improve DAX efficiency?](#389-why-can-splitting-large-items-improve-dax-efficiency)
- [390: How does denormalization interact with DAX?](#390-how-does-denormalization-interact-with-dax)
- [391: When is a precomputed result item better than relying on the query cache?](#391-when-is-a-precomputed-result-item-better-than-relying-on-the-query-cache)
- [392: When can the query cache be better than precomputed items?](#392-when-can-the-query-cache-be-better-than-precomputed-items)
- [393: How do you keep query parameters stable so requests share cache entries?](#393-how-do-you-keep-query-parameters-stable-so-requests-share-cache-entries)
- [394: Why are only the first pages of a list usually worth caching?](#394-why-are-only-the-first-pages-of-a-list-usually-worth-caching)
- [395: Should parallel scans go through DAX?](#395-should-parallel-scans-go-through-dax)
- [396: How do ConditionCheck items work in a transaction through DAX?](#396-how-do-conditioncheck-items-work-in-a-transaction-through-dax)
- [397: Does DAX lower the cost of transactions?](#397-does-dax-lower-the-cost-of-transactions)
- [398: How does DAX help with DynamoDB adaptive capacity limits?](#398-how-does-dax-help-with-dynamodb-adaptive-capacity-limits)
- [399: About how many reads reach DynamoDB for a very hot key behind DAX?](#399-about-how-many-reads-reach-dynamodb-for-a-very-hot-key-behind-dax)
- [400: Do DynamoDB response size limits still apply through DAX?](#400-do-dynamodb-response-size-limits-still-apply-through-dax)
- [401: Why does DAX use its own protocol instead of HTTPS like DynamoDB?](#401-why-does-dax-use-its-own-protocol-instead-of-https-like-dynamodb)
- [402: Why does DAX use client side discovery instead of a load balancer?](#402-why-does-dax-use-client-side-discovery-instead-of-a-load-balancer)
- [403: Why is DAX only reachable inside a VPC?](#403-why-is-dax-only-reachable-inside-a-vpc)
- [404: How does the client learn about cluster changes like new or replaced nodes?](#404-how-does-the-client-learn-about-cluster-changes-like-new-or-replaced-nodes)
- [405: How would you protect DAX from a sudden client side traffic spike?](#405-how-would-you-protect-dax-from-a-sudden-client-side-traffic-spike)
- [406: How do you handle very large query results through DAX without using too much memory in Node?](#406-how-do-you-handle-very-large-query-results-through-dax-without-using-too-much-memory-in-node)
- [407: How do you define SLOs for an app that uses DAX?](#407-how-do-you-define-slos-for-an-app-that-uses-dax)
- [408: What should a DAX outage runbook include?](#408-what-should-a-dax-outage-runbook-include)
- [409: Why should the DAX endpoint come from infrastructure code outputs?](#409-why-should-the-dax-endpoint-come-from-infrastructure-code-outputs)
- [410: When should you fix the table design instead of adding DAX?](#410-when-should-you-fix-the-table-design-instead-of-adding-dax)
- [411: Design the read path for a product page that gets 1 million reads per second.](#411-design-the-read-path-for-a-product-page-that-gets-1-million-reads-per-second)
- [412: Design a social feed with DAX. What would you cache?](#412-design-a-social-feed-with-dax-what-would-you-cache)
- [413: Would you use DAX or ElastiCache for a session store?](#413-would-you-use-dax-or-elasticache-for-a-session-store)
- [414: Design a "latest reading per device" API for IoT with DAX.](#414-design-a-latest-reading-per-device-api-for-iot-with-dax)
- [415: Would you build a rate limiter on DAX?](#415-would-you-build-a-rate-limiter-on-dax)
- [416: How would you handle inventory reservations if the catalog is behind DAX?](#416-how-would-you-handle-inventory-reservations-if-the-catalog-is-behind-dax)
- [417: Should you put DAX in front of every DynamoDB table by default?](#417-should-you-put-dax-in-front-of-every-dynamodb-table-by-default)
- [418: What questions would you ask before approving DAX in a design review?](#418-what-questions-would-you-ask-before-approving-dax-in-a-design-review)
- [419: How does DAX change the way you test an app?](#419-how-does-dax-change-the-way-you-test-an-app)
- [420: How would you simulate stale data in an integration test?](#420-how-would-you-simulate-stale-data-in-an-integration-test)
- [421: What is the trade-off between a long TTL and data freshness in numbers?](#421-what-is-the-trade-off-between-a-long-ttl-and-data-freshness-in-numbers)
- [422: Why do short TTLs hurt less for hot items than for warm items?](#422-why-do-short-ttls-hurt-less-for-hot-items-than-for-warm-items)
- [423: How do you choose TTL based on access frequency?](#423-how-do-you-choose-ttl-based-on-access-frequency)
- [424: How does DAX compare with RDS read replicas?](#424-how-does-dax-compare-with-rds-read-replicas)
- [425: Why does DAX not support DynamoDB's control plane, and what does it mean for your code?](#425-why-does-dax-not-support-dynamodbs-control-plane-and-what-does-it-mean-for-your-code)
- [426: How would you design an app to run with or without DAX?](#426-how-would-you-design-an-app-to-run-with-or-without-dax)
- [427: What happens if you change a parameter group while the cluster is busy?](#427-what-happens-if-you-change-a-parameter-group-while-the-cluster-is-busy)
- [428: Why is it hard to reason about "the cache state" in DAX?](#428-why-is-it-hard-to-reason-about-the-cache-state-in-dax)
- [429: What happens if two clients write the same item through DAX at nearly the same time?](#429-what-happens-if-two-clients-write-the-same-item-through-dax-at-nearly-the-same-time)
- [430: How does DAX treat items larger than what's useful to cache?](#430-how-does-dax-treat-items-larger-than-whats-useful-to-cache)
- [431: How do you decide between dax.t3 and an R node for a small production service?](#431-how-do-you-decide-between-daxt3-and-an-r-node-for-a-small-production-service)
- [432: What problems can a single-node DAX cluster cause in production?](#432-what-problems-can-a-single-node-dax-cluster-cause-in-production)
- [433: How can you tell if your cluster's working set fits in memory?](#433-how-can-you-tell-if-your-clusters-working-set-fits-in-memory)
- [434: What is the risk of using DAX for authorization data like roles and permissions?](#434-what-is-the-risk-of-using-dax-for-authorization-data-like-roles-and-permissions)
- [435: How do you explain the difference between DAX TTL and DynamoDB TTL in an interview?](#435-how-do-you-explain-the-difference-between-dax-ttl-and-dynamodb-ttl-in-an-interview)
- [436: Why might you still need ElastiCache even when using DAX?](#436-why-might-you-still-need-elasticache-even-when-using-dax)
- [437: How does using DAX affect DynamoDB contributor insights or table metrics?](#437-how-does-using-dax-affect-dynamodb-contributor-insights-or-table-metrics)
- [438: How would you handle a schema change, like renaming an attribute, with DAX?](#438-how-would-you-handle-a-schema-change-like-renaming-an-attribute-with-dax)
- [439: What's the effect of DAX on DynamoDB Streams consumers?](#439-whats-the-effect-of-dax-on-dynamodb-streams-consumers)
- [440: How would you secure DAX access from a container platform with many services?](#440-how-would-you-secure-dax-access-from-a-container-platform-with-many-services)
- [441: How does DAX's IAM model compare with direct DynamoDB access for least privilege?](#441-how-does-daxs-iam-model-compare-with-direct-dynamodb-access-for-least-privilege)
- [442: What changed in 2025 for DAX that is useful to know in interviews?](#442-what-changed-in-2025-for-dax-that-is-useful-to-know-in-interviews)
- [443: Why might an older Node project still use amazon-dax-client?](#443-why-might-an-older-node-project-still-use-amazon-dax-client)
- [444: What would you look for when reviewing code that uses DAX?](#444-what-would-you-look-for-when-reviewing-code-that-uses-dax)
- [445: How can a code change silently lower the DAX hit rate?](#445-how-can-a-code-change-silently-lower-the-dax-hit-rate)
- [446: How do you prove DAX is worth keeping after a year?](#446-how-do-you-prove-dax-is-worth-keeping-after-a-year)
- [447: What is the hardest part of running DAX well?](#447-what-is-the-hardest-part-of-running-dax-well)
- [448: If you could change one DAX default for most apps, what would it be?](#448-if-you-could-change-one-dax-default-for-most-apps-what-would-it-be)
- [449: How would you explain the main DAX trade-offs in one answer?](#449-how-would-you-explain-the-main-dax-trade-offs-in-one-answer)
- [450: When would you recommend against DAX in a system design interview?](#450-when-would-you-recommend-against-dax-in-a-system-design-interview)

---

# Easy Questions (1-150)

## 1: What is DynamoDB DAX?

DAX stands for DynamoDB Accelerator. It is a fully managed, in-memory cache that sits in front of DynamoDB tables. Your app sends reads and writes to DAX instead of DynamoDB, and DAX answers repeated reads from memory.

The main point is speed: DynamoDB reads usually take a few milliseconds, while a DAX cache hit usually takes microseconds.

## 2: Why would you use DAX?

You use DAX when an app reads the same items many times and needs very low read latency. Typical reasons are:

- Read latency in microseconds instead of milliseconds
- Fewer read capacity units used on the table, which can lower cost
- Protection against hot items that get read far more often than others

If your app is mostly writes, or every read must be strongly consistent, DAX gives little benefit.

## 3: Is DAX a separate database?

No. DAX is a cache, not a database. DynamoDB is still the source of truth. DAX keeps copies of items and query results in memory for a limited time. If a DAX cluster is deleted, no data is lost, because all writes go to DynamoDB.

## 4: What does "API compatible with DynamoDB" mean for DAX?

It means DAX accepts the same data plane calls as DynamoDB, such as GetItem, PutItem, Query and Scan, with the same request and response shapes. In most apps you only change how the client is created. The rest of the code that calls `get`, `put` or `query` stays the same.

## 5: What kind of latency can you expect from DAX?

For a cache hit, reads usually complete in microseconds (often a few hundred microseconds measured from the client). For a cache miss, DAX has to call DynamoDB, so latency is about the same as a normal DynamoDB read plus a small extra hop. Writes are not faster with DAX because they still go to DynamoDB first.

## 6: What is a DAX cluster?

A DAX cluster is a group of one or more nodes that together act as the cache. Your app connects to the cluster, not to a single node. One node is the primary and the rest are read replicas. The cluster runs inside your VPC.

## 7: What is a DAX node?

A node is one cache server inside a cluster. Each node has its own memory, CPU and network capacity, set by the node type you pick (for example `dax.r5.large`). Every node holds a full copy of the cached data, so any node can answer any read.

## 8: What is the primary node in a DAX cluster?

The primary node handles all writes. When a write comes in, the primary sends it to DynamoDB, updates its cache when the write succeeds, and then replicates the change to the read replicas. The primary can also serve reads, like any other node.

## 9: What is a read replica in DAX?

A read replica is a node that serves reads only. It receives cache updates from the primary node. Adding replicas gives the cluster more read throughput and better availability. If the primary fails, DAX promotes one of the replicas to be the new primary.

## 10: How many nodes can a DAX cluster have?

According to the DAX docs, a cluster can have up to 11 nodes: one primary and up to 10 read replicas. You can start with one node for testing. For production, AWS recommends at least three nodes spread across different Availability Zones.

## 11: Why does AWS recommend at least three nodes for production?

With three nodes in three Availability Zones, the cluster keeps working if one node or one whole Availability Zone fails. A one or two node cluster is not fault tolerant in the way AWS defines it, so it is meant for development and testing only.

## 12: What is the item cache?

The item cache stores the results of GetItem and BatchGetItem calls. Each entry is one item, keyed by the table and primary key. When you read an item by its key and it is already in the item cache, DAX returns it without calling DynamoDB.

## 13: What is the query cache?

The query cache stores the results of Query and Scan calls. Each entry is the full result set for one exact request (same table, key condition, filters, limits and other parameters). If the same request comes in again before the entry expires, DAX returns the saved result.

## 14: Are the item cache and query cache the same thing?

No. They are two separate caches inside DAX. An item read by GetItem goes to the item cache, and a result from Query or Scan goes to the query cache. A write updates the item cache but does not change anything in the query cache.

## 15: What is the default TTL for items in DAX?

The default time to live is 5 minutes for both the item cache and the query cache. After that time, the entry is treated as expired and the next read goes to DynamoDB again. You can change both values with a parameter group.

## 16: What is TTL in DAX?

TTL (time to live) is how long a cached entry stays valid. After the TTL passes, DAX does not return the entry anymore and fetches fresh data from DynamoDB on the next request. DAX TTL is not the same as DynamoDB's TTL feature, which deletes items from the table.

## 17: What is a cache hit and a cache miss?

A cache hit means DAX already has the requested data in memory and returns it right away. A cache miss means DAX does not have it (or it expired), so DAX reads from DynamoDB, returns the result to the client and stores it in the cache for the next time.

## 18: What does "read-through cache" mean for DAX?

It means the app never reads DynamoDB directly on a miss. The app asks DAX, and DAX itself fetches the data from DynamoDB when it is missing, stores it, and returns it. The app code does not need any "check cache, then check database" logic.

## 19: What does "write-through cache" mean for DAX?

When you write through DAX, DAX first writes the item to DynamoDB. Only if that write succeeds does it update the item in its cache. This keeps the item cache in step with the table for writes that go through DAX.

## 20: Which DynamoDB operations does DAX cache?

DAX caches eventually consistent reads from:

- GetItem and BatchGetItem (item cache)
- Query and Scan (query cache)

Writes like PutItem, UpdateItem, DeleteItem, BatchWriteItem and TransactWriteItems go through DAX to DynamoDB and update the item cache.

## 21: Does DAX cache strongly consistent reads?

No. If a request has `ConsistentRead: true`, DAX passes it straight to DynamoDB and returns DynamoDB's answer. The result is not saved in the cache. So strongly consistent reads get no speed benefit from DAX.

## 22: What consistency model does DAX give for cached reads?

DAX reads are eventually consistent. Cached data can be older than what is in the table, for example if someone wrote to DynamoDB without going through DAX, or if the change has not yet replicated to the node you hit.

## 23: Can you create a DynamoDB table through DAX?

No. DAX handles only data plane operations (reading and writing items). Control plane operations like CreateTable, UpdateTable, DeleteTable and DescribeTable must go to DynamoDB directly with the normal DynamoDB client.

## 24: Does using DAX change the data stored in DynamoDB?

No. DAX writes the same items to DynamoDB that you would write directly. The table looks the same whether it was written through DAX or not. DAX only adds a cache layer in front.

## 25: Where does a DAX cluster run?

A DAX cluster runs inside an Amazon VPC in your account. It is not reachable from the public internet. Your app must run in the same VPC (or a network connected to it), for example on EC2, ECS, EKS or Lambda with VPC access.

## 26: Can you connect to DAX from your laptop over the internet?

Not directly. DAX has no public endpoint. To test from a laptop you need network access into the VPC, for example a VPN, AWS Client VPN, or an SSH tunnel through a bastion host. Most people test with a small EC2 instance or a Lambda inside the VPC.

## 27: What is the DAX cluster endpoint?

The cluster endpoint is one DNS name for the whole cluster. The DAX client connects to it, finds all the nodes, and spreads requests across them. It looks like this:

```
dax://my-cluster.abc123.dax-clusters.us-east-1.amazonaws.com
```

You should give the cluster endpoint to your app instead of individual node addresses.

## 28: What is the difference between dax:// and daxs:// endpoints?

`dax://` is the plain, unencrypted endpoint and uses port 8111. `daxs://` is the TLS encrypted endpoint and uses port 9111. Which one you get depends on whether the cluster was created with encryption in transit turned on.

## 29: Which ports does DAX use?

DAX uses TCP port 8111 for unencrypted connections and TCP port 9111 for TLS connections. Your DAX security group must allow inbound traffic on the right port from the security group of your app.

## 30: Which programming languages have DAX clients?

AWS provides DAX clients for Java, Node.js (JavaScript), Python, Go and .NET. You cannot use the normal DynamoDB SDK client to talk to DAX. You need the DAX client for your language, because DAX uses its own wire protocol.

## 31: Which npm package do you use for DAX with AWS SDK v3?

You use `@amazon-dax-sdk/lib-dax`. It gives you `DaxDocument`, which works like `DynamoDBDocument` from `@aws-sdk/lib-dynamodb`. It depends on `@amazon-dax-sdk/client-dax` and needs Node.js 18 or later.

```bash
npm install @amazon-dax-sdk/lib-dax @aws-sdk/lib-dynamodb @aws-sdk/client-dynamodb
```

## 32: What is the amazon-dax-client package?

`amazon-dax-client` is the older DAX client for the AWS SDK for JavaScript v2. You still find it in older code. For new projects, use `@amazon-dax-sdk/lib-dax`, which was released in March 2025 for SDK v3.

## 33: How do you create a DAX client in Node.js?

```js
import { DaxDocument } from "@amazon-dax-sdk/lib-dax";

const dax = new DaxDocument({
  endpoints: [process.env.DAX_ENDPOINT],
  region: "us-east-1",
});
```

`endpoints` takes the cluster endpoint. Create the client once and reuse it, because it keeps open connections to the nodes.

## 34: How do you read one item through DAX in Node.js?

```js
const { Item } = await dax.get({
  TableName: "Users",
  Key: { userId: "u-123" },
});

console.log(Item);
```

This is the same call you would make with `DynamoDBDocument`. If the item is in the item cache, DAX returns it from memory.

## 35: How do you write an item through DAX in Node.js?

```js
await dax.put({
  TableName: "Users",
  Item: { userId: "u-123", name: "Ana", plan: "pro" },
});
```

DAX writes the item to DynamoDB first. If that works, it puts the new version in the item cache, so the next `get` for that key returns the new data.

## 36: How do you run a Query through DAX in Node.js?

```js
const { Items } = await dax.query({
  TableName: "Orders",
  KeyConditionExpression: "customerId = :c",
  ExpressionAttributeValues: { ":c": "c-42" },
});
```

The full result is saved in the query cache, keyed by these exact parameters. The same query in the next 5 minutes (default) comes from memory.

## 37: Do you need to change table design to use DAX?

No. DAX works with your existing tables, keys and indexes. You do not add attributes or change keys. You only create a cluster, give it access to the tables, and point the app's client at the cluster.

## 38: Does DAX work with global secondary indexes?

Yes. Queries and scans on a global secondary index can go through DAX and are cached in the query cache, just like queries on the base table. GetItem does not apply to indexes, so the item cache is only used for base table items.

## 39: Does DAX work with local secondary indexes?

Yes. A Query on a local secondary index through DAX is cached in the query cache. Keep in mind that a strongly consistent read on an LSI (which LSIs allow) is passed through and not cached.

## 40: How does DAX help with hot keys?

A hot key is an item that gets far more reads than others. Without a cache, all those reads hit one partition and can be throttled. With DAX, most of those reads are cache hits, so they never reach DynamoDB and the partition stays within its limits.

## 41: Does DAX reduce DynamoDB cost?

It can. Every cache hit is a read that DynamoDB does not have to serve, so you use fewer read capacity units or fewer on-demand read requests. But you pay for the DAX nodes per hour. DAX saves money only when the reads you remove cost more than the nodes.

## 42: How is DAX priced?

You pay per node per hour, based on the node type. There is no charge per request. T3 nodes run in unlimited mode, so you can also pay for extra CPU credits if a node runs above its baseline for long. Data transfer between Availability Zones inside the region can also add cost.

## 43: What node types does DAX support?

Current families in the docs include T3 and T2 (small burstable nodes, for test and light workloads), and R4, R5 and R7i (memory optimized nodes, for production). R7i nodes were added in April 2025. Sizes go from `small` and `medium` for T types up to `24xlarge` for R5 and R7i.

## 44: When should you use a T3 node type?

T3 nodes (`dax.t3.small`, `dax.t3.medium`) are cheap and fine for development, testing and small workloads with low, steady traffic. They are burstable and run in unlimited mode, so long periods of high CPU can create surplus credit charges. For production with real load, use an R family node.

## 45: Can you change the node type of an existing DAX cluster?

No. The node type is fixed when you create the cluster. To change it, create a new cluster with the new node type, point your app to it, and delete the old one. You can change the number of nodes on a running cluster, though.

## 46: How do you add nodes to a DAX cluster?

You increase the replication factor, which is the number of nodes in the cluster.

```bash
aws dax increase-replication-factor \
  --cluster-name my-cluster \
  --new-replication-factor 5
```

The new nodes start empty and fill up as they receive traffic and replicated writes.

## 47: How do you remove nodes from a DAX cluster?

```bash
aws dax decrease-replication-factor \
  --cluster-name my-cluster \
  --new-replication-factor 3
```

You can also name specific node IDs to remove with `--node-ids-to-remove`. Fewer nodes means less read capacity and less fault tolerance.

## 48: What is a subnet group in DAX?

A subnet group is a list of subnets in one VPC where DAX can place its nodes. You must give one when you create a cluster. To spread nodes across Availability Zones, the subnet group should include subnets in several zones.

## 49: How do you create a DAX subnet group?

```bash
aws dax create-subnet-group \
  --subnet-group-name my-dax-subnets \
  --subnet-ids subnet-aaa111 subnet-bbb222 subnet-ccc333
```

All subnets must be in the same VPC. Use private subnets, since DAX does not need internet access.

## 50: What is a parameter group in DAX?

A parameter group holds settings for a DAX cluster. The main ones are `record-ttl-millis` (TTL for the item cache) and `query-ttl-millis` (TTL for the query cache). If you don't pick one, the cluster uses the default group `default.dax1.0`, which you cannot edit.

## 51: How do you change the TTL of the DAX item cache?

Create a custom parameter group, set `record-ttl-millis`, and attach the group to the cluster.

```bash
aws dax create-parameter-group --parameter-group-name my-dax-params

aws dax update-parameter-group \
  --parameter-group-name my-dax-params \
  --parameter-name-values "ParameterName=record-ttl-millis,ParameterValue=600000"
```

`600000` milliseconds is 10 minutes. The new TTL applies to items cached after the change.

## 52: What happens if you set the item cache TTL to 0?

With `record-ttl-millis` set to 0, items in the item cache never expire on time. They are replaced only when a write goes through DAX or when LRU eviction removes them to free memory. This is risky if other systems write to the table directly, because the cache can stay stale for a long time.

## 53: What happens if you set the query cache TTL to 0?

With `query-ttl-millis` set to 0, DAX does not cache query and scan results at all. Queries and scans still go through DAX, but they are always sent to DynamoDB. The item cache keeps working as normal.

## 54: What is LRU eviction in DAX?

LRU means "least recently used". When a node runs low on memory, DAX removes the entries that have not been read for the longest time to make room. LRU is always on and you cannot turn it off. It can remove an entry before its TTL ends.

## 55: What is negative caching in DAX?

If you ask for an item that does not exist, DAX remembers that the item is missing. The next read for the same key returns "not found" from the cache without calling DynamoDB. The same applies to empty query results. The negative entry lasts until the TTL ends, LRU removes it, or a write for that key goes through DAX.

## 56: Does DAX support BatchGetItem?

Yes. BatchGetItem through DAX checks the item cache for each key. Keys that are cached are returned from memory, and only the missing ones are fetched from DynamoDB. The fetched items are then added to the item cache.

```js
const res = await dax.batchGet({
  RequestItems: {
    Users: { Keys: [{ userId: "u-1" }, { userId: "u-2" }] },
  },
});
```

## 57: Does DAX support BatchWriteItem?

Yes. BatchWriteItem goes through DAX to DynamoDB. For each put or delete that succeeds, DAX updates the item cache. Unprocessed items are returned to you the same way DynamoDB returns them, and you need to retry them.

## 58: Does DAX support UpdateItem?

Yes. UpdateItem is sent to DynamoDB, and if it succeeds DAX updates the cached copy of that item.

```js
await dax.update({
  TableName: "Users",
  Key: { userId: "u-123" },
  UpdateExpression: "SET plan = :p",
  ExpressionAttributeValues: { ":p": "free" },
});
```

## 59: Does DAX support DeleteItem?

Yes. DeleteItem goes to DynamoDB first. If the delete succeeds, DAX updates the item cache so a later GetItem for that key does not return the old item.

## 60: Does DAX support transactions?

Yes. TransactWriteItems goes through DAX to DynamoDB and updates the item cache when the transaction succeeds. TransactGetItems is passed straight to DynamoDB and is not served from the cache, because transactional reads must be up to date.

## 61: What is a pass-through operation in DAX?

A pass-through operation is one that DAX forwards to DynamoDB without using its cache. Examples are strongly consistent reads and TransactGetItems. You still call DAX, but you get DynamoDB latency and DynamoDB reads are consumed as normal.

## 62: Does DAX support conditional writes?

Yes. You can send PutItem, UpdateItem or DeleteItem with a `ConditionExpression`. DynamoDB checks the condition. If it fails, DynamoDB returns `ConditionalCheckFailedException`, the write does not happen, and DAX leaves the cache as it was.

## 63: Does DAX support Scan?

Yes. A Scan through DAX is cached in the query cache, keyed by the exact scan parameters. Scans read a lot of data, so caching a big scan result can use a lot of DAX memory. Use it only for small tables or repeated scans with a `Limit`.

## 64: Does DAX support pagination?

Yes. Query and Scan through DAX return `LastEvaluatedKey` just like DynamoDB. You pass it as `ExclusiveStartKey` to get the next page. Each page is a different request, so each page gets its own entry in the query cache.

## 65: What is the IAM service role for DAX?

DAX needs an IAM role to call DynamoDB for you. The role trusts the `dax.amazonaws.com` service and has permissions like `dynamodb:GetItem`, `dynamodb:PutItem`, `dynamodb:Query` and `dynamodb:DescribeTable` on the tables the cluster will cache. You pass the role ARN when creating the cluster.

## 66: What does the trust policy of the DAX service role look like?

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Principal": { "Service": "dax.amazonaws.com" },
      "Action": "sts:AssumeRole"
    }
  ]
}
```

This lets the DAX service assume the role. The permissions policy attached to the role decides which tables DAX can reach.

## 67: What IAM permissions does your app need to call DAX?

The app's role needs `dax:` actions on the cluster ARN, for example `dax:GetItem`, `dax:PutItem`, `dax:Query`, `dax:Scan`, `dax:BatchGetItem`. These are separate from `dynamodb:` actions. An app that only calls DAX does not need `dynamodb:GetItem` itself, because DAX makes the DynamoDB call with its own role.

## 68: Can one DAX cluster cache more than one table?

Yes. One cluster can cache many tables in the same region, up to 500 tables. The service role must allow access to each of them. All tables share the same memory on the nodes, so a busy table can push out items from another table.

## 69: Can DAX cache a table from another region?

No. A DAX cluster can only reach DynamoDB tables in its own region. If you have tables in several regions, you need a cluster in each region.

## 70: Is DAX available in every AWS region?

No. DAX is available in many regions but not all of them. Check the DynamoDB pricing page or the regional services list before you plan to use it in a specific region.

## 71: How do you create a DAX cluster with the AWS CLI?

```bash
aws dax create-cluster \
  --cluster-name my-cluster \
  --node-type dax.r5.large \
  --replication-factor 3 \
  --iam-role-arn arn:aws:iam::123456789012:role/DAXServiceRole \
  --subnet-group-name my-dax-subnets \
  --security-group-ids sg-0abc123 \
  --sse-specification Enabled=true \
  --cluster-endpoint-encryption-type TLS
```

This makes a three node cluster with encryption at rest and in transit.

## 72: How do you see details of a DAX cluster?

```bash
aws dax describe-clusters --cluster-names my-cluster
```

The output shows the status, node type, number of nodes, the cluster endpoint, node endpoints and their Availability Zones, the parameter group, and the encryption settings.

## 73: How do you delete a DAX cluster?

```bash
aws dax delete-cluster --cluster-name my-cluster
```

Deleting a cluster deletes all cached data, but nothing in DynamoDB. Before you delete it, switch the app back to the plain DynamoDB client or to another cluster, or requests will fail.

## 74: Can you create a DAX cluster in the AWS console?

Yes. In the DynamoDB console there is a DAX section with "Clusters", "Subnet groups" and "Parameter groups". The create wizard asks for the cluster name, node type, node count, subnet group, security groups, IAM role and encryption settings.

## 75: How long does it take to create a DAX cluster?

It usually takes several minutes, often around 10 minutes or more. The cluster status goes from `creating` to `available`. You cannot send requests until it is available.

## 76: What is the cluster status "available"?

`available` means the cluster is running and ready to serve requests. Other statuses you may see are `creating`, `modifying` (for example while nodes are added) and `deleting`.

## 77: What is encryption at rest in DAX?

Encryption at rest means DAX encrypts the data it stores on the node, including cached items, logs and config, with AES-256. It uses an AWS owned key through KMS. You can turn it on only when you create the cluster. It is not available on the old `dax.r3` node types.

## 78: Can you enable encryption at rest on an existing DAX cluster?

No. Encryption at rest must be chosen when the cluster is created and cannot be turned on or off later. To change it, create a new cluster with the setting you want and move the app to it.

## 79: What is encryption in transit in DAX?

It means traffic between your app and the DAX cluster uses TLS. You set it with `--cluster-endpoint-encryption-type TLS` when you create the cluster. The cluster then gives a `daxs://` endpoint on port 9111.

## 80: Can you enable encryption in transit on an existing cluster?

No. Like encryption at rest, it is set at creation time only. To switch, create a new cluster with TLS, update the app's endpoint, and delete the old cluster.

## 81: Does DAX support customer managed KMS keys?

No. DAX encryption at rest uses an AWS owned key managed by the service. You cannot pick your own customer managed key. If your rules require your own key, keep that in mind when choosing DAX.

## 82: What security group rules does DAX need?

The DAX security group needs an inbound rule that allows TCP 8111 (or 9111 for TLS) from your app's security group. Your app's security group needs outbound access to the same port. No other inbound access is needed.

## 83: What is a maintenance window in DAX?

A maintenance window is a weekly time slot, 60 minutes long by default, when AWS can apply updates to the cluster, such as software patches. Nodes may be replaced during maintenance, so apps can see short errors. You pick a time when traffic is low.

## 84: How do you set the maintenance window?

```bash
aws dax update-cluster \
  --cluster-name my-cluster \
  --preferred-maintenance-window "sun:05:00-sun:06:00"
```

The time is in UTC. If you don't set it, AWS picks one in a default block for the region.

## 85: What is the SNS notification setting in DAX?

You can link an SNS topic to a cluster. DAX then sends messages about events like node failures, node replacement and maintenance. This helps you get alerts without polling. You can also list recent events with `aws dax describe-events`.

## 86: Does DAX replace a failed node automatically?

Yes. DAX watches node health. If a node fails, DAX replaces it. If it was the primary, a read replica is promoted to primary first. The new node starts with an empty cache and fills up over time.

## 87: What happens to the cache when a node restarts?

The cache on that node is lost, because it lives in memory. After the restart the node starts empty and fills again from reads and replicated writes. This means more cache misses and more DynamoDB reads for a short time.

## 88: How do you reboot a DAX node?

```bash
aws dax reboot-node --cluster-name my-cluster --node-id my-cluster-a
```

Rebooting clears that node's cache. It is mostly used for testing failure handling.

## 89: Can DAX be used with DynamoDB on-demand tables?

Yes. DAX works with both on-demand and provisioned tables. With on-demand, each cache hit is one less paid read request. With provisioned, cache hits reduce the RCUs you need.

## 90: Do you still need DynamoDB capacity when using DAX?

Yes. Cache misses, writes, strongly consistent reads and pass-through operations all hit DynamoDB. If the cache is cold (for example after a restart), almost every read goes to the table. Plan table capacity for the worst case, not for a warm cache.

## 91: What is a cold cache?

A cold cache is a cache that is empty or almost empty, for example right after a cluster is created or a node is replaced. Most reads are misses, so latency and DynamoDB reads go up until the cache fills. This is often called "warming up".

## 92: What is a warm cache?

A warm cache already holds the data that the app reads most. Most reads are hits, latency is low and DynamoDB reads are low. The hit rate is a good way to tell how warm the cache is.

## 93: What is the cache hit ratio?

It is the share of reads served from the cache. For the item cache:

```
hit ratio = ItemCacheHits / (ItemCacheHits + ItemCacheMisses)
```

A high ratio (often 85 to 95 percent or more) means DAX is doing its job. A low ratio means many reads still go to DynamoDB.

## 94: Which CloudWatch namespace do DAX metrics use?

DAX metrics are in the `AWS/DAX` namespace. You can view them per cluster (`ClusterId`) or per node (`ClusterId` and `NodeId`).

## 95: What are the main DAX CloudWatch metrics?

- `ItemCacheHits`, `ItemCacheMisses`
- `QueryCacheHits`, `QueryCacheMisses`
- `CPUUtilization`
- `CacheMemoryUtilization`, `EvictedSize`
- `TotalRequestCount`, `ErrorRequestCount`, `FaultRequestCount`, `ThrottledRequestCount`
- `ClientConnections`

## 96: What does the ThrottledRequestCount metric show?

It counts requests that DAX itself throttled because a node was overloaded. It does not include throttling that DynamoDB returns to DAX. If this number grows, the cluster needs more nodes or bigger nodes.

## 97: What does the EvictedSize metric show?

It shows how much data was removed from the cache by LRU eviction to make room for new entries. If it is high, the working set does not fit in memory, and you may need a node type with more RAM.

## 98: What does CacheMemoryUtilization show?

It is the percent of the node's cache memory that is in use. When it is close to full, LRU eviction starts. High memory use with low evictions is normal and fine.

## 99: What is the difference between ErrorRequestCount and FaultRequestCount?

`ErrorRequestCount` counts requests that failed because of the user side, like bad parameters or throttling (similar to HTTP 4xx). `FaultRequestCount` counts requests that failed because of an internal DAX problem (similar to HTTP 5xx).

## 100: Does DAX log API calls in CloudTrail?

Yes, management API calls such as CreateCluster, UpdateCluster, DeleteCluster and UpdateParameterGroup are logged in CloudTrail. Don't count on CloudTrail as a log of every cached read. To see read and write volume, use the DAX CloudWatch metrics.

## 101: Can you use DAX from AWS Lambda?

Yes. The Lambda function must be attached to the same VPC as the DAX cluster, with subnets and a security group that can reach DAX on port 8111 or 9111. Create the DAX client outside the handler so it is reused across invocations.

```js
import { DaxDocument } from "@amazon-dax-sdk/lib-dax";

const dax = new DaxDocument({
  endpoints: [process.env.DAX_ENDPOINT],
  region: process.env.AWS_REGION,
});

export const handler = async (event) => {
  const { Item } = await dax.get({
    TableName: "Products",
    Key: { productId: event.productId },
  });
  return Item;
};
```

## 102: Can you use DAX from ECS or EKS?

Yes. Run the tasks or pods in subnets of the same VPC as the cluster, and allow their security group to reach the DAX port. Pass the cluster endpoint as an environment variable and create one DAX client per process.

## 103: Can you use DAX from an EC2 instance?

Yes, this is the most common setup. Launch the instance in the same VPC, allow its security group in the DAX security group's inbound rules, and give the instance role the needed `dax:` permissions.

## 104: Does DAX work with DynamoDB Local?

No. DynamoDB Local is a local copy of DynamoDB, and there is no local version of DAX. In local development you usually use the normal `DynamoDBDocument` client against DynamoDB Local and switch to `DaxDocument` only when a DAX endpoint is configured.

## 105: How can you switch between DAX and DynamoDB in code?

Because both clients have the same methods, you can pick one at startup:

```js
import { DaxDocument } from "@amazon-dax-sdk/lib-dax";
import { DynamoDBDocument } from "@aws-sdk/lib-dynamodb";
import { DynamoDBClient } from "@aws-sdk/client-dynamodb";

const region = "us-east-1";

export const db = process.env.DAX_ENDPOINT
  ? new DaxDocument({ endpoints: [process.env.DAX_ENDPOINT], region })
  : DynamoDBDocument.from(new DynamoDBClient({ region }));
```

The rest of the app uses `db.get`, `db.put` and so on without caring which one it is.

## 106: What is the difference between DaxDocument and DynamoDBDocument?

`DynamoDBDocument` talks to the DynamoDB HTTPS API. `DaxDocument` talks to a DAX cluster with the DAX protocol. They take the same request objects and return the same responses, with plain JavaScript values instead of DynamoDB's typed attribute format.

## 107: Does DAX return data in the same format as DynamoDB?

Yes. With the document client you get plain JavaScript objects, the same as from `DynamoDBDocument`. With the low level client you get the typed attribute format (`{ S: "..." }`, `{ N: "..." }`). The format does not depend on whether the data came from cache.

## 108: Can you tell from the response whether it was a cache hit?

Not from the normal response. The response looks the same for a hit and a miss. To see hit rates, use CloudWatch metrics like `ItemCacheHits` and `ItemCacheMisses`. You can also measure latency on the client side: hits are much faster.

## 109: Does DAX return ConsumedCapacity?

When a request reaches DynamoDB (a miss, a write or a pass-through), you can get consumed capacity like normal. A cache hit uses no DynamoDB capacity. Don't rely on consumed capacity numbers from DAX responses to judge table usage; use the table's CloudWatch metrics instead.

## 110: What are good use cases for DAX?

- Product catalogs and pages with many repeat reads
- Game leaderboards or player profiles read many times per second
- Session or config lookups by key
- Read-heavy APIs that need microsecond latency
- Tables with a few very hot items that cause throttling

## 111: When is DAX not a good fit?

- Write-heavy workloads, where most traffic is writes
- Apps that need strongly consistent reads for most calls
- Apps with very random reads where the same item is rarely read twice
- Apps that cannot run inside a VPC
- Languages or runtimes without a DAX client

## 112: Is DAX a good fit for write-heavy apps?

Usually not. Writes still go to DynamoDB, and DAX adds a small extra hop, so write latency gets slightly worse, not better. DAX only pays off when there are many reads per write.

## 113: What is the difference between DAX and ElastiCache?

DAX is made only for DynamoDB and is API compatible with it, so it caches reads with almost no code change. ElastiCache (Valkey, Redis OSS or Memcached) is a general cache. You can store anything there, use data structures like sorted sets, and cache data from any source, but your code must manage cache reads, writes and invalidation.

## 114: When would you choose ElastiCache over DAX?

Choose ElastiCache when you need to cache data from several sources, cache computed results (for example a rendered page or an aggregate), use data structures like lists or sorted sets, or control exactly when entries are removed. Choose DAX when you just want faster DynamoDB reads with little code change.

## 115: Is DAX the same as DynamoDB's internal cache?

No. DynamoDB has its own internal storage and caching that you don't see or control. DAX is a separate service that you create and pay for. It runs in your VPC and you control its size, nodes and TTL settings.

## 116: Does DAX store data on disk?

DAX keeps the cache in memory. Encryption at rest covers data the node keeps on its storage, like logs and swap. You should never treat DAX as durable storage. Anything only in DAX can be lost when a node restarts.

## 117: Can DAX be used as a session store on its own?

Not on its own. DAX is a cache over DynamoDB, so the session data still lives in a DynamoDB table. DAX can make session lookups faster, but the table is what keeps the sessions.

## 118: What is the working set in caching?

The working set is the data your app reads often within a short time. For DAX, the working set should fit in the memory of a node. If it doesn't, LRU keeps pushing out entries you will need again soon, and the hit rate drops.

## 119: Does every DAX node hold the same data?

Yes, in general. Writes are replicated from the primary to all replicas, and each node also fills its own cache from the reads it serves. Over time, nodes hold mostly the same hot data, though not always the exact same set at the same moment.

## 120: How does the DAX client pick a node?

The DAX client is cluster aware. It connects to the cluster endpoint, learns about all nodes, and spreads requests across them. It sends writes to the primary. If a node goes away, the client stops using it and moves traffic to the others.

## 121: Why should you reuse the DAX client object?

Creating a client opens connections and finds the cluster nodes, which takes time. If you create a new client for every request, you add that cost every time and may open too many connections. Create it once at startup and share it.

## 122: Do you need a load balancer in front of DAX?

No. The DAX client spreads requests across nodes by itself. Putting a normal load balancer in front would break the client's view of the cluster. Always connect with the cluster endpoint and the DAX client.

## 123: Can you use the normal AWS SDK DynamoDB client to talk to DAX?

No. The normal SDK client speaks the DynamoDB HTTPS API, and DAX uses its own protocol on port 8111 or 9111. You must use a DAX client library.

## 124: Can you call DAX with curl or a REST client?

No. DAX does not expose an HTTP API for data operations. Only DAX client libraries can send reads and writes. Management calls like `CreateCluster` use the normal AWS API and can be made with the AWS CLI.

## 125: What is a DAX node endpoint?

Each node has its own address, which you can see in `describe-clusters`. The client uses them internally. In your app config you should use the cluster endpoint, because nodes can be added, removed or replaced and their addresses change.

## 126: What happens if the DAX cluster is down?

Requests to DAX fail. DAX does not automatically fall back to DynamoDB. If you want the app to keep working, add your own fallback that catches DAX errors and retries the request on a normal DynamoDB client.

## 127: Does DAX retry failed requests?

The DAX client retries some failures, such as when a node is not reachable, by trying another node. Errors from DynamoDB itself, like a failed condition, are returned to you as normal. You should still handle errors in your own code.

## 128: What happens when DynamoDB throttles a DAX request?

If DynamoDB throttles a request that DAX sent on a cache miss or a write, DAX returns the throttling error to the client. DAX does not hide DynamoDB throttling. The table still needs enough capacity for misses and writes.

## 129: What happens when a DAX node is overloaded?

DAX can throttle requests itself if a node is overloaded, and the `ThrottledRequestCount` metric goes up. Your app gets throttling errors and should retry with backoff. The fix is to add nodes or use a larger node type.

## 130: What is the replication factor in DAX?

In DAX, the replication factor is the number of nodes in the cluster. A replication factor of 3 means one primary and two replicas. You change it with `increase-replication-factor` and `decrease-replication-factor`.

## 131: Can you stop a DAX cluster to save money?

No. There is no stop or pause option. A cluster is billed per node per hour while it exists. To stop paying, you delete it and create it again later. For dev environments, people often delete clusters at night with a script.

## 132: Can you tag a DAX cluster?

Yes. You can add tags when creating the cluster with `--tags` or later with `aws dax tag-resource`. Tags help with cost allocation and finding resources.

## 133: Can you create DAX with CloudFormation?

Yes. The resource types are `AWS::DAX::Cluster`, `AWS::DAX::SubnetGroup` and `AWS::DAX::ParameterGroup`.

```yaml
DaxCluster:
  Type: AWS::DAX::Cluster
  Properties:
    ClusterName: my-cluster
    NodeType: dax.r5.large
    ReplicationFactor: 3
    IAMRoleARN: !GetAtt DaxRole.Arn
    SubnetGroupName: !Ref DaxSubnetGroup
    SecurityGroupIds: [!Ref DaxSecurityGroup]
    SSESpecification:
      SSEEnabled: true
    ClusterEndpointEncryptionType: TLS
```

## 134: Can you create DAX with the AWS CDK?

Yes, through the low level `CfnCluster`, `CfnSubnetGroup` and `CfnParameterGroup` constructs in `aws-cdk-lib/aws-dax`. There are no higher level L2 constructs for DAX in the main CDK library, so you set the properties yourself.

## 135: Can you create DAX with Terraform?

Yes. The AWS provider has `aws_dax_cluster`, `aws_dax_subnet_group` and `aws_dax_parameter_group` resources. They map closely to the CLI options: cluster name, node type, replication factor, IAM role, subnet group, security groups and encryption settings.

## 136: Is DAX serverless?

No. DAX is managed, but you choose node types and node count, and you pay per node per hour even if there is no traffic. AWS handles patching, failure detection and node replacement for you.

## 137: Does DAX scale automatically?

No. DAX has no auto scaling for nodes. You change the number of nodes yourself, with the console, CLI or your own automation based on CloudWatch alarms. Changing node size means creating a new cluster.

## 138: Can you scale DAX for more reads?

Yes. Add read replicas. Each new node adds read capacity, because reads are spread across all nodes. This is called scaling out (horizontal scaling).

## 139: Can you scale DAX for more memory?

You need a bigger node type, which means a new cluster. Adding more nodes does not add cache space, because every node holds a full copy of the cache. This is scaling up (vertical scaling).

## 140: Does adding more nodes speed up writes?

No. All writes go through the primary node and then to DynamoDB. More replicas give more read capacity, but write capacity depends on the primary node and on the table.

## 141: What is the max size of an item in DAX?

DAX uses the same item size limit as DynamoDB, which is 400 KB per item. DAX does not let you store bigger items, because every item it caches comes from or goes to DynamoDB.

## 142: Does DAX change DynamoDB limits?

No. Table limits, item size, partition throughput and request size limits are all still DynamoDB's. DAX adds its own limits on top, such as node memory and the number of nodes per cluster.

## 143: What is DAX's effect on read cost for eventually consistent reads?

Each cache hit is a read that does not reach DynamoDB, so it uses no read capacity. For a table with a 90 percent hit rate, DynamoDB serves only about 10 percent of the eventually consistent reads.

## 144: What are the main parts you set up to use DAX?

1. An IAM service role that lets DAX access the tables
2. A subnet group in your VPC
3. A security group that allows the DAX port from your app
4. The DAX cluster (node type, count, encryption)
5. Optionally a parameter group for TTL settings
6. The DAX client in your app, pointed at the cluster endpoint

## 145: Do you need to warm up DAX manually?

You don't have to. DAX fills itself from normal reads. If you want low latency right after a deploy or restart, you can run a warm-up script that reads the most popular keys through DAX, so they are cached before real users arrive.

## 146: Does DAX support PutItem with ReturnValues?

Yes. You can pass `ReturnValues` (for example `ALL_OLD`) on PutItem, UpdateItem or DeleteItem through DAX. DynamoDB computes the return values and DAX passes them back to you.

## 147: Does DAX support ProjectionExpression?

Yes. You can send `ProjectionExpression` on GetItem, Query and Scan through DAX to get only some attributes, the same as with DynamoDB. The response contains only the attributes you asked for.

## 148: Does DAX support filter expressions?

Yes. Query and Scan through DAX accept `FilterExpression`. The filter is part of the request parameters, so a query with a different filter value gets a different query cache entry.

## 149: Does DAX work with DynamoDB Streams?

DynamoDB Streams are a feature of the table, not of DAX. Writes through DAX go to DynamoDB, so they appear in the table's stream like any other write. DAX does not read from streams, and stream events do not update the DAX cache.

## 150: What is the most important thing to remember about DAX consistency?

DAX gives eventually consistent reads, and the cache can be stale. Writes that go through DAX update the item cache, but writes that skip DAX, and any write's effect on cached query results, stay hidden until the cache entry expires. Design your app so that short stale reads are acceptable.

# Moderate Questions (151-300)

## 151: What permissions policy should the DAX service role have?

Give it only the DynamoDB actions DAX will run, on only the tables it should cache:

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "dynamodb:DescribeTable",
        "dynamodb:GetItem",
        "dynamodb:BatchGetItem",
        "dynamodb:Query",
        "dynamodb:Scan",
        "dynamodb:PutItem",
        "dynamodb:UpdateItem",
        "dynamodb:DeleteItem",
        "dynamodb:BatchWriteItem",
        "dynamodb:ConditionCheckItem"
      ],
      "Resource": [
        "arn:aws:dynamodb:us-east-1:123456789012:table/Users",
        "arn:aws:dynamodb:us-east-1:123456789012:table/Users/index/*"
      ]
    }
  ]
}
```

If the cluster is only for reads, leave out the write actions.

## 152: What does an app policy for DAX look like?

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "dax:GetItem",
        "dax:BatchGetItem",
        "dax:Query",
        "dax:PutItem",
        "dax:UpdateItem"
      ],
      "Resource": "arn:aws:dax:us-east-1:123456789012:cache/my-cluster"
    }
  ]
}
```

The resource is the cluster ARN, not the table ARN. This lets the app run only these actions against this cluster.

## 153: Why do DAX management actions use Resource "*"?

Management APIs like `dax:CreateCluster`, `dax:DescribeClusters` and `dax:CreateSubnetGroup` don't support resource level permissions in the same way, so AWS docs say to use `"Resource": "*"` for them. Keep these permissions for admin roles and CI pipelines, not for app roles.

## 154: Why can DAX weaken table level IAM rules?

DAX calls DynamoDB with its own service role, not with the caller's identity. Anyone who can call `dax:GetItem` on the cluster can read anything the service role can read, even if their own IAM policy denies `dynamodb:GetItem` on that table. If two groups of users need different table access, give them separate clusters with separate service roles.

## 155: How do you give a read-only app access through DAX?

Grant the app only read actions on the cluster: `dax:GetItem`, `dax:BatchGetItem`, `dax:Query` and `dax:Scan`. Do not grant `dax:PutItem` or other write actions. For stronger control, create a cluster whose service role has only DynamoDB read permissions, so even a wrong app policy cannot write through it.

## 156: How do you connect to a TLS enabled DAX cluster in Node.js?

Use the `daxs://` cluster endpoint. The client sets up TLS for you.

```js
import { DaxDocument } from "@amazon-dax-sdk/lib-dax";

const dax = new DaxDocument({
  endpoints: ["daxs://my-cluster.abc123.dax-clusters.us-east-1.amazonaws.com"],
  region: "us-east-1",
});
```

Make sure the security group allows port 9111, not 8111.

## 157: Where should you store the DAX endpoint for an app?

Keep it out of the code. Common places are an environment variable set by your deploy tool, AWS Systems Manager Parameter Store, or a CloudFormation output passed into the app. This lets each environment point to its own cluster, and makes it easy to switch clusters without a code change.

## 158: How do you fall back to DynamoDB when DAX is not reachable?

Wrap reads so that a DAX connection error retries the same request on a plain DynamoDB client:

```js
import { DaxDocument } from "@amazon-dax-sdk/lib-dax";
import { DynamoDBDocument } from "@aws-sdk/lib-dynamodb";
import { DynamoDBClient } from "@aws-sdk/client-dynamodb";

const region = "us-east-1";
const dax = new DaxDocument({ endpoints: [process.env.DAX_ENDPOINT], region });
const ddb = DynamoDBDocument.from(new DynamoDBClient({ region }));

export async function getItem(params) {
  try {
    return await dax.get(params);
  } catch (err) {
    if (
      err.name === "ConditionalCheckFailedException" ||
      err.name === "ValidationException"
    ) {
      throw err;
    }
    console.warn("DAX failed, using DynamoDB", err.name);
    return ddb.get(params);
  }
}
```

Only fall back on errors that point to DAX being down. Business errors should be thrown as usual, and the table must have enough capacity to take the full load.

## 159: How do you handle a failed condition through DAX?

The same way as with DynamoDB. The error name is `ConditionalCheckFailedException`.

```js
try {
  await dax.put({
    TableName: "Users",
    Item: { userId: "u-1", email: "a@example.com" },
    ConditionExpression: "attribute_not_exists(userId)",
  });
} catch (err) {
  if (err.name === "ConditionalCheckFailedException") {
    console.log("User already exists");
  } else {
    throw err;
  }
}
```

The cache is not changed when the condition fails.

## 160: How do you retry throttled DAX requests?

Retry with exponential backoff and jitter, and give up after a few tries:

```js
async function withRetry(fn, attempts = 5) {
  for (let i = 0; ; i++) {
    try {
      return await fn();
    } catch (err) {
      const throttled = /Throttl|ProvisionedThroughputExceeded/.test(
        err.name ?? "",
      );
      if (!throttled || i >= attempts - 1) throw err;
      const delay = Math.random() * 50 * 2 ** i;
      await new Promise((r) => setTimeout(r, delay));
    }
  }
}

await withRetry(() => dax.get({ TableName: "Users", Key: { userId: "u-1" } }));
```

Throttling can come from DAX (overloaded node) or from DynamoDB (on misses and writes).

## 161: If you write an item through DAX and read it right away, do you get the new value?

Usually yes for GetItem, because the write updates the item cache on the primary. But the read may go to a replica that has not received the update yet. Replication usually takes well under a second, so in rare cases you can read the old value for a short time.

## 162: How do you get read-your-own-writes behavior with DAX?

For the few reads that must see the latest write, set `ConsistentRead: true`. DAX passes the read to DynamoDB and you get the current value. Another option is to use the value you just wrote (for example from `ReturnValues: "ALL_NEW"` on UpdateItem) instead of reading it again.

## 163: Why can a Query return old data right after a write through DAX?

Writes update the item cache only. The query cache keeps the saved result of an earlier Query until its TTL ends. So if you put a new order and then query the customer's orders, the new order may be missing for up to the query TTL (5 minutes by default).

## 164: How can you deal with stale query cache results?

- Lower `query-ttl-millis` to a value your app can live with
- Use `ConsistentRead: true` on the few queries that must be fresh
- Read single items with GetItem when you know the key, since GetItem sees DAX writes
- Update the client side state with what you just wrote instead of querying again
- For data that changes often and must be fresh, skip DAX for those queries

## 165: How do you pick TTL values for DAX?

Ask how long the business can accept old data. A product description might be fine for 10 minutes, while a stock count might need a few seconds or no caching at all. A longer TTL gives a higher hit rate and lower cost, and a shorter TTL gives fresher data. Measure the hit rate after changing it.

## 166: Why would you set different TTLs for the item cache and the query cache?

They go stale in different ways. The item cache is updated by DAX writes, so it stays fresh if all writes go through DAX, and a longer TTL is fine. The query cache is never updated by writes, so it is often given a shorter TTL to limit how long lists stay out of date.

## 167: How do you attach a parameter group to a cluster?

```bash
aws dax update-cluster \
  --cluster-name my-cluster \
  --parameter-group-name my-dax-params
```

You can also set `--parameter-group-name` when you create the cluster. Several clusters can share one parameter group.

## 168: Do TTL changes affect items that are already cached?

No. A new TTL applies only to entries cached after the change. Entries already in the cache keep the TTL they had when they were stored. If you need the new TTL right away, you have to wait until the old entries expire.

## 169: How do you see the current parameter values?

```bash
aws dax describe-parameters --parameter-group-name my-dax-params
```

The output lists each parameter, its value, and whether it can be changed. You can also see this in the console under DAX parameter groups.

## 170: What is write-around and when would you use it with DAX?

Write-around means writing directly to DynamoDB and skipping DAX. It's useful for bulk loads, backfills and batch jobs that write many items nobody will read soon. If they went through DAX, they would fill the cache with cold data and push out hot items. The trade-off is that items already cached stay stale until their TTL ends.

## 171: What is cache pollution?

Cache pollution means the cache fills with entries that won't be read again, which pushes out entries that would have been read. With DAX, it often comes from big scans, bulk writes through DAX, or queries with many unique parameter combinations. You see it as high `EvictedSize` and a falling hit rate.

## 172: Are writes through DAX slower than writes to DynamoDB?

Slightly. DAX receives the write, sends it to DynamoDB, waits for success, updates the cache and replicates it. That's one extra network hop compared with writing to DynamoDB directly. For most apps the difference is small, but write latency never gets better with DAX.

## 173: How do you measure whether DAX actually helps your app?

Compare the same traffic with and without DAX. Track client side p50, p95 and p99 read latency, the DAX hit ratio, DynamoDB consumed read capacity and total cost. A load test in a staging environment works well. If the hit ratio is low, DAX may add cost without much gain.

## 174: How do you create an alarm for a low cache hit rate?

CloudWatch metric math can compute the ratio and alarm on it:

```bash
aws cloudwatch put-metric-alarm \
  --alarm-name dax-low-hit-rate \
  --comparison-operator LessThanThreshold \
  --threshold 0.8 \
  --evaluation-periods 3 \
  --metrics '[
    {"Id":"h","MetricStat":{"Metric":{"Namespace":"AWS/DAX","MetricName":"ItemCacheHits","Dimensions":[{"Name":"ClusterId","Value":"my-cluster"}]},"Period":300,"Stat":"Sum"},"ReturnData":false},
    {"Id":"m","MetricStat":{"Metric":{"Namespace":"AWS/DAX","MetricName":"ItemCacheMisses","Dimensions":[{"Name":"ClusterId","Value":"my-cluster"}]},"Period":300,"Stat":"Sum"},"ReturnData":false},
    {"Id":"ratio","Expression":"h/(h+m)","ReturnData":true}
  ]'
```

## 175: When should you add nodes based on CPU?

If `CPUUtilization` stays high on the nodes for long periods (many teams use around 70 percent as a warning), add replicas. High CPU leads to higher latency and DAX throttling. Look at per-node CPU too, because the primary does extra work for writes.

## 176: What can cause a low item cache hit rate?

- Reads are spread over many keys and few are repeated
- The TTL is too short
- The working set is bigger than node memory, so LRU evicts items
- Code sends `ConsistentRead: true`, so reads skip the cache
- Nodes restarted recently and the cache is still cold
- Many writes go around DAX, but that causes staleness rather than misses

## 177: How does the query cache key work, and why does it matter?

DAX uses the full set of request parameters as the key: table, index, key condition, expression values, filter, projection, limit, sort direction and start key. Any small difference makes a new entry. So two queries that return the same data but use different parameter text or values don't share a cache entry.

## 178: Why is it bad to put the current time in a DAX query?

If you query "events after now", the `now` value changes on every call, so each request has a new cache key and never hits the cache. Round the time to a bucket (for example the start of the current minute or hour) so many requests share the same parameters and the same cache entry.

```js
const bucket = Math.floor(Date.now() / 60000) * 60000;
await dax.query({
  TableName: "Events",
  KeyConditionExpression: "pk = :pk AND ts >= :t",
  ExpressionAttributeValues: { ":pk": "feed", ":t": bucket },
});
```

## 179: How do you handle UnprocessedKeys from BatchGetItem through DAX?

The same as with DynamoDB: loop until no keys are left, with a small backoff.

```js
let request = { Users: { Keys: keys } };
const items = [];

while (request && Object.keys(request).length) {
  const res = await dax.batchGet({ RequestItems: request });
  items.push(...(res.Responses?.Users ?? []));
  request = res.UnprocessedKeys;
  if (request && Object.keys(request).length) {
    await new Promise((r) => setTimeout(r, 100));
  }
}
```

## 180: How do you handle UnprocessedItems from BatchWriteItem through DAX?

```js
let request = {
  Orders: items.map((Item) => ({ PutRequest: { Item } })),
};

while (request && Object.keys(request).length) {
  const res = await dax.batchWrite({ RequestItems: request });
  request = res.UnprocessedItems;
  if (request && Object.keys(request).length) {
    await new Promise((r) => setTimeout(r, 200));
  }
}
```

A batch can hold up to 25 put or delete requests, the same as DynamoDB.

## 181: How do you run a transaction through DAX?

```js
await dax.transactWrite({
  TransactItems: [
    {
      Update: {
        TableName: "Accounts",
        Key: { accountId: "a-1" },
        UpdateExpression: "SET balance = balance - :amt",
        ConditionExpression: "balance >= :amt",
        ExpressionAttributeValues: { ":amt": 50 },
      },
    },
    {
      Update: {
        TableName: "Accounts",
        Key: { accountId: "a-2" },
        UpdateExpression: "SET balance = balance + :amt",
        ExpressionAttributeValues: { ":amt": 50 },
      },
    },
  ],
});
```

If the transaction succeeds, DAX updates both items in the item cache.

## 182: Should you read account balances through DAX?

For reads used to make decisions, like checking a balance before a payment, use `ConsistentRead: true` or TransactGetItems so you get the current value. For showing a balance on a dashboard where a few seconds of delay is fine, a cached read is OK. Never let a cached value be the only check before moving money; use a condition expression on the write.

## 183: How does DAX fit single-table design?

It works the same. DAX does not care how many entity types share one table. GetItem on `PK`/`SK` uses the item cache and Query on `PK` uses the query cache. Just keep in mind that a query for "all items in this partition" can be stale after writes to any item in that partition.

## 184: Are GSI query results through DAX more stale than normal?

They can be. A GSI is already eventually consistent with the base table, so a new write can take a short time to show up in the index. DAX then caches the query result for the query TTL. The total delay is the index lag plus up to one TTL.

## 185: How does pagination interact with the query cache?

Each page is a separate request with a different `ExclusiveStartKey`, so each page gets its own cache entry. Page one may be cached at a different time than page two. After writes, pages can be out of step, for example an item showing on two pages or on none for a short time.

## 186: When is Scan through DAX a bad idea?

When the table is large or the scan is rare. A big scan result takes a lot of node memory and pushes out hot items, and if the scan is not repeated within the TTL, caching it brings no benefit. Run large or parallel scans against DynamoDB directly, or export the table to S3 for analysis.

## 187: How does Lambda cold start affect DAX use?

On a cold start, Lambda creates the DAX client, which opens connections and finds the nodes. This adds time to the first request. VPC networking for Lambda is fast to set up now, but the client setup still costs time. Create the client at module level so warm invocations reuse it, and consider provisioned concurrency for latency sensitive functions.

## 188: Does a Lambda in a VPC with DAX also need internet access?

Not for DAX. DAX is inside the VPC. But if the same function also calls other AWS services (like SQS or Secrets Manager) or DynamoDB directly as a fallback, it needs a route to them, either through VPC endpoints or a NAT gateway. A gateway VPC endpoint for DynamoDB is free and a common choice.

## 189: How do you set up security groups for DAX with the CLI?

```bash
# security group for DAX
aws ec2 create-security-group --group-name dax-sg \
  --description "DAX cluster" --vpc-id vpc-0abc

# allow the app security group on the TLS port
aws ec2 authorize-security-group-ingress \
  --group-id sg-dax123 \
  --protocol tcp --port 9111 \
  --source-group sg-app456
```

Using a source security group instead of IP ranges keeps the rule correct when app instances change.

## 190: Can an app in another VPC use a DAX cluster?

Yes, if the networks are connected, for example with VPC peering or Transit Gateway, and routes and security groups allow traffic. The client talks to every node, not only the cluster endpoint, so every node's IP must be reachable. Cross-VPC paths add latency, so keeping the app in the same VPC is simpler.

## 191: How do you unit test code that uses DAX?

Don't call DAX in unit tests. Pass the client in as a dependency and replace it with a fake that has the same methods:

```js
export function makeUserRepo(db) {
  return {
    async getUser(userId) {
      const { Item } = await db.get({ TableName: "Users", Key: { userId } });
      return Item ?? null;
    },
  };
}

// test
const fakeDb = { get: async () => ({ Item: { userId: "u-1", name: "Ana" } }) };
const repo = makeUserRepo(fakeDb);
console.log(await repo.getUser("u-1"));
```

## 192: How do you run integration tests against DAX?

Run them from inside the VPC, for example in a CodeBuild project with VPC config, a container on ECS, or a Lambda. Use a test cluster (a single small node is often enough) and a test table. Most integration tests can also run against DynamoDB Local or a real table, since DAX has the same API.

## 193: How do you move from amazon-dax-client (v2) to lib-dax (v3)?

Old v2 code:

```js
const AWS = require("aws-sdk");
const AmazonDaxClient = require("amazon-dax-client");

const dax = new AmazonDaxClient({ endpoints: [endpoint], region: "us-east-1" });
const doc = new AWS.DynamoDB.DocumentClient({ service: dax });

const res = await doc
  .get({ TableName: "Users", Key: { userId: "u-1" } })
  .promise();
```

New v3 code:

```js
import { DaxDocument } from "@amazon-dax-sdk/lib-dax";

const doc = new DaxDocument({ endpoints: [endpoint], region: "us-east-1" });
const res = await doc.get({ TableName: "Users", Key: { userId: "u-1" } });
```

The request objects stay the same; the main changes are the import, the constructor and dropping `.promise()`.

## 194: Why move from the v2 DAX client to the v3 one?

AWS SDK for JavaScript v2 is in maintenance and has reached end of support, so new features and fixes go to v3. Keeping v2 just for DAX means your app carries two SDKs. The v3 DAX client fits with `@aws-sdk/lib-dynamodb`, uses promises directly and needs Node.js 18 or later.

## 195: Can you use DAX with TypeScript?

Yes. `@amazon-dax-sdk/lib-dax` works in TypeScript projects, and the input and output shapes match the AWS SDK v3 document client types. You can type your items yourself:

```ts
type User = { userId: string; name: string };

const { Item } = await dax.get({ TableName: "Users", Key: { userId: "u-1" } });
const user = Item as User | undefined;
```

## 196: How do you estimate the cost of DAX?

Multiply the hourly price of your node type by the node count and by about 730 hours per month. Then estimate how much DynamoDB read cost you save: reads per month times hit ratio times the price per read. If the savings plus the value of lower latency are bigger than the node cost, DAX makes sense on cost.

## 197: When can DAX cost more than it saves?

When read traffic is low, the hit rate is low, or most reads are strongly consistent. A three node production cluster runs all the time, even at night. For a small app with a few hundred reads per second, the nodes can easily cost more than the DynamoDB reads they replace.

## 198: How do you choose a DAX node type?

Look at three things:

- Memory: the working set must fit in one node's cache
- CPU: enough to handle your peak request rate
- Network: enough bandwidth for your item sizes and request rate

Start with a mid size R node, load test with real access patterns, and watch CPU, memory and evictions. Then adjust size and node count.

## 199: Why can load testing on T2 nodes mislead you?

T2 nodes use CPU credits. During a test they may run fast while they have credits, then slow down sharply when credits run out. The results don't show how the cluster behaves under steady load. Load test on the node type you plan to use in production.

## 200: What is the CPU credit issue with T3 nodes?

T3 DAX nodes run in unlimited mode. If a node uses more CPU than its baseline for a long time, it keeps running fast but you pay surplus credit charges. Watch `CPUCreditBalance` and `CPUSurplusCreditsCharged`. If surplus charges show up often, an R node may be cheaper.

## 201: How do you place DAX nodes in specific Availability Zones?

Pass `--availability-zones` when creating the cluster, one zone per node:

```bash
aws dax create-cluster \
  --cluster-name my-cluster \
  --node-type dax.r5.large \
  --replication-factor 3 \
  --availability-zones us-east-1a us-east-1b us-east-1c \
  --iam-role-arn arn:aws:iam::123456789012:role/DAXServiceRole \
  --subnet-group-name my-dax-subnets
```

If you leave it out, DAX spreads the nodes across zones from the subnet group.

## 202: Does cross-AZ traffic matter for DAX?

Yes, a little. When the client talks to a node in another Availability Zone, each request has a bit more network latency and can add data transfer cost. Spreading nodes across zones is still the right choice for availability. Just keep it in mind when you compare latency numbers.

## 203: How should an app handle errors during DAX maintenance?

During maintenance, nodes can be replaced one at a time, so some requests may fail or time out. The DAX client moves to other nodes, but your app should still retry with backoff and, for important reads, fall back to DynamoDB. Set the maintenance window to a low traffic time.

## 204: How do you see recent events for a DAX cluster?

```bash
aws dax describe-events \
  --source-name my-cluster \
  --source-type CLUSTER \
  --duration 1440
```

`--duration` is in minutes, so 1440 shows the last day. Events include node replacement, reboots and changes to settings.

## 205: How do you send DAX events to an SNS topic?

```bash
aws dax update-cluster \
  --cluster-name my-cluster \
  --notification-topic-arn arn:aws:sns:us-east-1:123456789012:dax-events \
  --notification-topic-status active
```

You can subscribe email, a chat webhook through Lambda, or a paging tool to that topic.

## 206: How do you change a cluster's node type with no downtime?

Use a blue/green switch:

1. Create a new cluster with the new node type and the same settings
2. Optionally warm it by reading hot keys through it
3. Change the app config to the new cluster endpoint and roll out
4. Watch metrics, then delete the old cluster

Because the cache is not the source of truth, nothing has to be copied.

## 207: How do you write a warm-up script for DAX?

Read the most popular keys through DAX after the cluster starts:

```js
import { DaxDocument } from "@amazon-dax-sdk/lib-dax";

const dax = new DaxDocument({
  endpoints: [process.env.DAX_ENDPOINT],
  region: "us-east-1",
});

async function warm(productIds) {
  for (let i = 0; i < productIds.length; i += 100) {
    const keys = productIds
      .slice(i, i + 100)
      .map((productId) => ({ productId }));
    await dax.batchGet({ RequestItems: { Products: { Keys: keys } } });
  }
}

await warm(await loadTopProductIds());
```

`loadTopProductIds` is your own function, for example reading a list from S3 or analytics. BatchGetItem takes up to 100 keys per call. Keep the rate low so the warm-up itself doesn't throttle the table.

## 208: What does the client see when the primary node fails?

Writes may fail for a short time until DAX promotes a replica to primary. Reads can keep going to the remaining nodes. The client finds out about the new primary and starts sending writes to it. Apps should retry failed writes with backoff during this short window.

## 209: Does DAX help with write throttling on hot partitions?

No. Every write still goes to DynamoDB, so a hot key for writes is still hot. DAX only removes read load. For write hot spots, fix the key design, for example with write sharding (adding a suffix to spread writes across partitions).

## 210: Can you lower provisioned read capacity after adding DAX?

You can, but carefully. If DAX restarts or the cache goes cold, most reads hit the table again, and a small capacity will throttle. Keep auto scaling on with a high enough maximum, or use on-demand mode, so the table can handle a cold cache.

## 211: Why is on-demand mode often paired with DAX?

On-demand handles traffic spikes without capacity planning. With DAX, table traffic is low most of the time but can jump when the cache is cold or after a failover. On-demand absorbs these jumps, and you only pay for the reads that actually reach the table.

## 212: What is the negative caching gotcha with DAX?

If an item is read before it exists, DAX caches "not found". If another system then creates the item directly in DynamoDB (not through DAX), reads through DAX keep returning "not found" until the TTL ends. Writing the item through DAX avoids this, because the write updates the cache.

## 213: What happens if you delete an item directly in DynamoDB?

DAX doesn't know about it. The deleted item stays in the item cache and is still returned until its TTL ends or LRU evicts it. Deletes should go through DAX if you want cached reads to stop returning the item.

## 214: Does DynamoDB TTL deletion update the DAX cache?

No. DynamoDB TTL deletes happen inside DynamoDB and don't go through DAX. A cached copy of an expired item can still be returned until the DAX TTL ends. If expiry must be exact, check the expiry attribute in your code and treat expired items as missing.

```js
const { Item } = await dax.get({ TableName: "Sessions", Key: { sessionId } });
const now = Math.floor(Date.now() / 1000);
const session = Item && Item.expiresAt > now ? Item : null;
```

## 215: How does DAX work with DynamoDB global tables?

A DAX cluster only sees writes made through it in its own region. Writes made in other regions and replicated into the local table bypass DAX, so the local cache can stay stale until TTL. If you use DAX with global tables, keep TTLs short and accept that reads can lag behind writes in other regions.

## 216: Can you invalidate a single item in DAX?

There is no invalidate API. The ways to refresh an item are: write it through DAX (put, update or delete), wait for its TTL, or let LRU evict it. You can't remove a single query cache entry; it only goes away on TTL or eviction.

## 217: Can you flush the whole DAX cache?

There is no flush command. Rebooting a node clears that node's cache, and rebooting all nodes one by one clears the cluster, but this causes errors and a cold cache. Creating a new cluster also gives an empty cache. Normally you should design around TTLs instead of flushing.

## 218: What should you log when a DAX call fails?

Log the error name and message, the operation (get, query, put), the table name, and whether the request was retried or fell back to DynamoDB. Don't log full items if they contain personal data. These logs, together with DAX CloudWatch metrics, help tell DAX problems apart from DynamoDB problems.

## 219: What does the ClientConnections metric tell you?

It shows the number of client connections to each node. A sudden jump often means the app creates a new DAX client per request instead of reusing one. Too many connections waste node resources and can slow the cluster down.

## 220: How do you use DAX in an Express app?

Create the client once when the module loads and use it in handlers:

```js
import express from "express";
import { DaxDocument } from "@amazon-dax-sdk/lib-dax";

const dax = new DaxDocument({
  endpoints: [process.env.DAX_ENDPOINT],
  region: "us-east-1",
});
const app = express();

app.get("/products/:id", async (req, res, next) => {
  try {
    const { Item } = await dax.get({
      TableName: "Products",
      Key: { productId: req.params.id },
    });
    if (!Item) return res.status(404).end();
    res.json(Item);
  } catch (err) {
    next(err);
  }
});

app.listen(3000);
```

## 221: How does DAX fit a CQRS read model?

In CQRS you keep a separate read model that is built from events or writes. If that read model is a DynamoDB table, DAX can cache it so read APIs are very fast. The read model is already eventually consistent, so a short DAX TTL usually fits well with what users expect.

## 222: Is DAX a good fit for a leaderboard?

It depends on how fresh the board must be. A leaderboard query on a GSI sorted by score gets cached in the query cache, so new scores won't show until the TTL ends. For a board that updates every few seconds, use a short query TTL. For real time ranks, a Valkey or Redis sorted set is usually a better tool.

## 223: What is the problem with reading counters through DAX?

If many clients increment a counter with `ADD`, every write goes through DynamoDB, and the item cache keeps the latest value only from writes that went through DAX. If some writers bypass DAX, the cached counter can be behind. For displays this is often fine; for decisions, read with `ConsistentRead: true`.

## 224: How does optimistic locking work with DAX?

You keep a `version` attribute and write with a condition that the version has not changed. If you read the item from a stale cache, the version may be old, and the conditional write fails. On failure, read again with `ConsistentRead: true` and retry.

```js
async function rename(userId, name) {
  let { Item } = await dax.get({ TableName: "Users", Key: { userId } });
  for (let i = 0; i < 3; i++) {
    try {
      return await dax.update({
        TableName: "Users",
        Key: { userId },
        UpdateExpression: "SET #n = :n, version = :next",
        ConditionExpression: "version = :v",
        ExpressionAttributeNames: { "#n": "name" },
        ExpressionAttributeValues: {
          ":n": name,
          ":v": Item.version,
          ":next": Item.version + 1,
        },
      });
    } catch (err) {
      if (err.name !== "ConditionalCheckFailedException") throw err;
      ({ Item } = await dax.get({
        TableName: "Users",
        Key: { userId },
        ConsistentRead: true,
      }));
    }
  }
  throw new Error("Too many conflicts");
}
```

## 225: Why is mixing DAX and direct DynamoDB writes risky?

Direct writes don't update the DAX cache. If service A writes through DAX and service B writes directly, reads through DAX can return values that are older than B's last write. Either send all writes for a table through DAX, or accept and document the staleness window (the TTL).

## 226: Which reads should skip the cache?

Reads where an old value can cause a wrong action:

- Checking stock or balance before a purchase
- Checking permissions right after they change
- Reading a value just before a conditional write that depends on it
- Reads after a write where the user must see the change

Use `ConsistentRead: true` for these, and keep the cache for display and read-heavy paths.

## 227: How do you choose between Query and GetItem when using DAX?

If you know the full primary key, use GetItem (or BatchGetItem). It uses the item cache, which is updated by writes through DAX, so it is fresher. Use Query when you really need a range or list. For lists, consider storing the keys and then reading items with BatchGetItem.

## 228: Why might BatchGetItem be better than Query for known IDs with DAX?

A Query result is cached as a whole and is not updated by writes. BatchGetItem reads each item from the item cache, which is updated by writes. If you already know the IDs, BatchGetItem gives fresher data and better reuse, because each item is shared across many requests instead of being stored inside many different query results.

## 229: How can you design access patterns to work well with DAX?

- Prefer key lookups (GetItem) for hot data
- Keep query parameters stable so requests share cache entries
- Store computed results as items, so they can be cached as one item
- Avoid huge result sets and big scans through DAX
- Keep hot data small so more of it fits in memory

## 230: How can you cache an expensive aggregate with DAX?

DAX can't compute anything. Instead, compute the aggregate yourself (for example with a stream processor or scheduled job), write it as an item like `{ pk: "STATS#2026-11-25" }`, and read that item through DAX. Readers then get a cheap cached GetItem instead of an expensive query.

## 231: What happens to the table when a cold DAX cluster gets full production traffic?

Almost every read misses, so the table gets nearly the full read load at once. With provisioned capacity that is set low, you get throttling and errors. To avoid this, warm the cache first, shift traffic gradually, or keep the table on on-demand or with enough capacity.

## 232: Should you use an in-process cache, DAX or both?

An in-process cache (like an LRU map in Node) is the fastest, but each process has its own copy and memory is small. DAX is shared by all processes and stays warm across deploys. Some apps use both: a tiny in-process cache with a short TTL for the very hottest keys, and DAX behind it.

## 233: What is the downside of stacking an in-process cache on top of DAX?

Staleness adds up. Data can be stale in the local cache for its TTL and in DAX for its TTL, so the worst case is the sum of both. You also lose the write-through freshness, because writes through DAX don't update other processes' local caches. Keep the local TTL very short.

## 234: How does DAX compare to caching at the API layer, like CloudFront?

CloudFront or API Gateway caching stores whole HTTP responses close to users. It can be much cheaper per request and also cuts compute cost. DAX caches only the database reads, so your app code still runs on every request. Use API caching for public, shared responses and DAX for per-user or dynamic data.

## 235: How do you handle time-sensitive data like prices with DAX?

Keep TTLs short for price data, or read prices with `ConsistentRead: true` at checkout. You can cache the product page data with a longer TTL and read only the price at the final step from DynamoDB. Price changes should go through DAX so the item cache is updated right away.

## 236: Should microservices share one DAX cluster?

They can, but there are trade-offs. Sharing saves money. Separate clusters give isolation: a busy service can't evict another service's data, and each cluster's service role can be limited to that service's tables. Since IAM is enforced at the cluster level, separate clusters are better when services need different access.

## 237: Do Step Functions DynamoDB integrations go through DAX?

No. Step Functions service integrations call the DynamoDB API directly. To use DAX in a workflow, call a Lambda function that uses the DAX client. Also keep in mind that direct writes from Step Functions bypass the DAX cache.

## 238: Do AppSync DynamoDB resolvers use DAX?

No. AppSync's DynamoDB data source talks to DynamoDB directly. If you want DAX, use a Lambda data source that runs inside the VPC and calls DAX. Writes made by AppSync directly to DynamoDB will not update the DAX cache.

## 239: Can you share a parameter group across clusters?

Yes. One parameter group can be attached to many clusters, which keeps TTL settings the same across environments. Be careful: changing the group changes every cluster that uses it.

## 240: How do you check which parameter group a cluster uses?

```bash
aws dax describe-clusters --cluster-names my-cluster \
  --query "Clusters[0].ParameterGroup"
```

The result shows the parameter group name and its apply status.

## 241: Does a cluster need internet access or a NAT gateway?

No. DAX nodes run in private subnets and reach DynamoDB through AWS. You don't have to add a NAT gateway for DAX itself. Your app may still need one, or VPC endpoints, for other AWS services.

## 242: How do you debug "connection timeout" errors to DAX?

Check these in order:

1. The app runs in the same VPC (or a connected one)
2. The DAX security group allows the right port (8111 or 9111) from the app's security group
3. You use the right scheme: `daxs://` for TLS clusters, `dax://` otherwise
4. Network ACLs on the subnets allow the traffic both ways
5. The cluster status is `available`

VPC Flow Logs can show whether packets are rejected.

## 243: What happens if you use dax:// on a TLS cluster?

The connection fails, because the cluster only accepts TLS connections on port 9111. Use the endpoint exactly as shown in `describe-clusters`, including its scheme, so you don't mix them up.

## 244: How do you change security groups on a running cluster?

```bash
aws dax update-cluster \
  --cluster-name my-cluster \
  --security-group-ids sg-new123 sg-other456
```

Make sure the new groups still allow the app's traffic before you remove old ones, or the app loses access.

## 245: How do you set up a cheap DAX cluster for development?

Use one `dax.t3.small` node, no read replicas, and the default parameter group. It's not fault tolerant, but it's fine for dev and testing. You can also delete it outside working hours with a scheduled script, because recreating it only costs a few minutes and an empty cache.

## 246: Why should DAX cluster names not contain sensitive information?

When encryption in transit is on, cluster names appear in public TLS certificate transparency logs. So a name like `acme-secret-merger-prod` could be seen by anyone. Use neutral names like `orders-cache-prod`.

## 247: Can DAX use IPv6?

Yes. When creating a cluster you can set `--network-type` to `ipv4`, `ipv6` or `dual_stack`. The subnets in the subnet group must support the chosen type. Use dual stack if some clients use IPv4 and some IPv6.

## 248: Does item size affect DAX performance?

Yes. Large items use more memory, so fewer fit in the cache, and they use more network bandwidth per read. A node may hit its network limit before CPU. If your items are large but you only need a few attributes often, consider storing a small summary item for hot reads.

## 249: Why should you avoid unbounded attribute names with DAX?

DAX keeps metadata about attribute names, and AWS docs say these names are kept even after items are evicted. If you use attribute names that keep changing, like timestamps or UUIDs as top level attribute names, this metadata can grow without limit and hurt the node. Use a fixed set of attribute names and put changing data in attribute values, not in names.

## 250: What is a noisy neighbor problem in a shared DAX cluster?

When several tables or services share one cluster, one of them can use most of the memory or CPU. For example, a big scan on one table can evict hot items of another table. If one workload hurts another, split them into separate clusters.

## 251: Should each environment have its own DAX cluster?

Yes. Dev, staging and production should use separate clusters, because they use separate tables and you don't want test traffic to evict production data. Dev clusters can be small single nodes, while production uses at least three R nodes.

## 252: Where do you check DAX limits like nodes per cluster?

Use the Service Quotas console (or `aws service-quotas list-service-quotas --service-code dax`) and the DAX quotas page in the DynamoDB developer guide. Some quotas, like the number of nodes per account in a region, can be raised with a request.

## 253: What should a DAX dashboard show?

- Item and query cache hit ratios
- `CPUUtilization` per node
- `CacheMemoryUtilization` and `EvictedSize`
- `TotalRequestCount` and per-operation counts
- `ErrorRequestCount`, `FaultRequestCount`, `ThrottledRequestCount`
- `ClientConnections`
- The table's consumed read and write capacity, to see how much load reaches DynamoDB

## 254: Which CloudWatch alarms should you set for DAX?

Common ones are: high `CPUUtilization` for several periods, any `FaultRequestCount`, rising `ThrottledRequestCount`, a low cache hit ratio, and high `EvictedSize`. Also alarm on the table's throttle metrics, since cache misses still go there. Send the alarms to the same SNS topic as DAX events.

## 255: How do you find the cause of high read latency with DAX?

First check the hit ratio. If it's low, latency is mostly DynamoDB latency. If the hit ratio is high, check node CPU, network use and throttling, and check whether the app creates too many clients. Also check client side issues like a busy Node event loop, which makes every request look slow.

## 256: Why would a team see almost no cache hits after adding DAX?

A common cause is that shared helper code sets `ConsistentRead: true` on every read, so all reads pass through. Other causes are reading mostly unique keys, a TTL of only a few seconds, or a query that includes a changing value (like a timestamp) in its parameters.

## 257: Why do cache misses jump after every deploy?

DAX itself keeps its cache across app deploys, so the cache should stay warm. If misses jump, check whether the deploy also changed query parameters (new projection, new filter, new limit), which creates new cache keys. Another cause is infrastructure code that replaces the cluster on deploy, for example a changed property that forces a new cluster.

## 258: Which changes force a new DAX cluster in CloudFormation?

Changing properties that DAX can't update in place, like node type, cluster name, subnet group, encryption at rest or endpoint encryption type, makes CloudFormation replace the cluster. The new cluster starts cold and has a new endpoint. Review change sets before deploying these.

## 259: How does a "top N" query behave in the query cache?

A query like "latest 10 posts" with `Limit: 10` and `ScanIndexForward: false` is cached as one entry. It's a great cache candidate because many users ask the same thing. But new posts won't show until the entry expires, so pick a query TTL that matches how fresh the feed must be.

## 260: Should DAX nodes go in public or private subnets?

Private subnets. DAX has no public endpoint and doesn't need internet access. Putting it in private subnets keeps the network simple and reduces exposure.

## 261: How do you roll out DAX to an existing app safely?

1. Create the cluster and IAM roles
2. Add the DAX client behind a config flag, keeping the DynamoDB client as the default
3. Turn DAX on for one service or a small share of instances
4. Watch hit ratio, latency, errors and table capacity
5. Increase traffic step by step
6. Keep the flag for a quick rollback

## 262: How do you use a feature flag to turn DAX on and off?

```js
const useDax = process.env.USE_DAX === "true" && process.env.DAX_ENDPOINT;

export const db = useDax
  ? new DaxDocument({ endpoints: [process.env.DAX_ENDPOINT], region })
  : DynamoDBDocument.from(new DynamoDBClient({ region }));
```

With a flag, you can turn DAX off during an incident by changing config and restarting, without a new build.

## 263: Can you send only part of the traffic through DAX?

Yes. Keep both clients and pick one per request, for example by a hash of the user ID:

```js
function pickClient(userId) {
  const bucket = [...userId].reduce((a, c) => a + c.charCodeAt(0), 0) % 100;
  return bucket < Number(process.env.DAX_PERCENT ?? 0) ? dax : ddb;
}
```

Using the user ID keeps each user on the same path, which avoids confusing differences between requests.

## 264: Does TransactWriteItems idempotency work through DAX?

Yes. You can pass `ClientRequestToken` in TransactWriteItems through DAX, and DynamoDB uses it to make retries of the same transaction safe within its idempotency window. DAX passes it along and updates the cache only when the transaction succeeds.

## 265: Is DAX good for a feature flags or config table?

Yes, it's a classic use. Config items are small, read on almost every request and rarely change. A GetItem through DAX is very fast and cheap. When you change a flag, write it through DAX so the item cache is updated, and keep in mind other nodes catch up within about a second.

## 266: How would you use DAX for user profile reads?

Profiles are read often (every page or API call) and written rarely. Read them with GetItem through DAX and write updates through DAX too. For the user's own "edit profile" page, show the values returned from the update call, so they see their change even if a replica is a moment behind.

## 267: How would you set up DAX for a product catalog?

Use GetItem through DAX for product pages and BatchGetItem for carts or lists of known IDs. Cache category listings in the query cache with a TTL of a few minutes. Write price and stock changes through DAX, and read stock with `ConsistentRead: true` at checkout. Size nodes so the most viewed products fit in memory.

## 268: Why is DAX popular in gaming backends?

Games often read player profiles, inventories and settings many times per second, while writes are less frequent. Microsecond reads keep the game responsive, and DAX removes hot key throttling during events when many players read the same data. Writes like scores still go to DynamoDB.

## 269: Why is DAX used in ad tech?

Ad bidding systems must answer in a few milliseconds and read things like campaign settings and user segments millions of times. Those reads repeat a lot, so the hit rate is high. DAX keeps read latency low and cuts the DynamoDB read cost for those huge volumes.

## 270: How do you use DAX in a multi-region active-active setup?

Run a DAX cluster in each region in front of that region's replica of a global table. Each app reads through its local DAX. Writes from the local app go through local DAX, but writes from other regions arrive by replication and bypass DAX, so set TTLs short enough for that delay.

## 271: How do you see how much load DAX removes from the table?

Compare DAX request counts with the table's `ConsumedReadCapacityUnits`. If the app sends 10,000 reads per second to DAX and the table only gets 1,000 RCUs worth of reads, DAX removes about 90 percent of the read load. Track this over time, especially after code changes.

## 272: Which metrics show request volume per operation?

DAX has per-operation metrics like `GetItemRequestCount`, `BatchGetItemRequestCount`, `QueryRequestCount`, `ScanRequestCount`, `PutItemRequestCount`, `UpdateItemRequestCount`, `DeleteItemRequestCount` and `TransactGetItemsCount`. They help you see which calls drive load.

## 273: How do you tell DAX throttling apart from DynamoDB throttling?

DAX throttling shows up in the `ThrottledRequestCount` metric of the cluster. DynamoDB throttling shows up in the table's throttle metrics, like `ReadThrottleEvents` and `WriteThrottleEvents`. If DAX throttles, add nodes. If the table throttles, raise table capacity or fix hot keys.

## 274: What is FailedRequestCount in DAX?

It counts requests that resulted in an error, covering both user errors and faults. Use `ErrorRequestCount` and `FaultRequestCount` to see which kind it was.

## 275: What do the network utilization metrics show?

`BaselineNetworkBytesInUtilization` and `BaselineNetworkBytesOutUtilization` show how close a node is to its baseline network limit. With large items or high request rates, nodes can hit network limits before CPU. If these are high, use a larger node type or reduce item sizes.

## 276: What does the EstimatedDbSize metric show?

It's an estimate of how much data is cached on the node. Compare it to the node's memory to see how much room is left, and watch it over time to see if the working set is growing.

## 277: What are ScanCacheHits and ScanCacheMisses?

They are like the query cache metrics but for Scan requests. They show whether repeated scans are being served from the cache. A very low hit rate for scans usually means caching them brings no benefit, and those scans should go directly to DynamoDB.

## 278: Do you need to back up a DAX cluster?

No. DAX holds only cached copies. The real data is in DynamoDB, which has its own backups and point-in-time recovery. If you lose a DAX cluster, you create a new one and it fills from the table.

## 279: What happens with DAX when you restore a DynamoDB table?

A restore creates a new table with a new name. DAX doesn't follow it automatically. You must give the service role access to the new table and point the app's requests at the new table name. Cached data for the old table just expires.

## 280: What do you need to change when adding a new table to an existing DAX cluster?

Only the service role's permissions: add the table ARN (and its index ARNs if you query indexes). There's no setting on the cluster that lists tables. Then the app can send requests for the new table through the same cluster.

## 281: What happens if the DAX service role lacks permission on a table?

When DAX tries to read or write that table in DynamoDB, it gets an access denied error and returns it to your app. Cached data is not involved because DAX could never fetch it. Fix the role's policy and retry.

## 282: What happens if the app's role lacks a dax: permission?

DAX rejects the request with an access denied error before it touches the cache or DynamoDB. For example, an app with `dax:GetItem` but without `dax:Query` can read items but not run queries through DAX.

## 283: Does adding a GSI to a table affect DAX?

The cluster itself doesn't need changes. To query the new index through DAX, the service role must allow `dynamodb:Query` on the index ARN (for example `table/Users/index/*`). After that, index queries are cached in the query cache.

## 284: How should you use DAX with Node.js cluster mode or several processes?

Each process needs its own DAX client, because a client can't be shared between processes. Create it once per process when it starts. Keep the number of processes per host reasonable, since each one opens its own connections to every node.

## 285: Can one DAX client handle many requests at the same time?

Yes. A single client object can handle many concurrent requests with `Promise.all`. You don't need a pool of clients.

```js
const ids = ["p-1", "p-2", "p-3"];
const results = await Promise.all(
  ids.map((productId) =>
    dax.get({ TableName: "Products", Key: { productId } }),
  ),
);
```

For many keys, BatchGetItem is usually more efficient than many separate gets.

## 286: How do you set up a Lambda with DAX using AWS SAM?

```yaml
Resources:
  GetProduct:
    Type: AWS::Serverless::Function
    Properties:
      Runtime: nodejs22.x
      Handler: index.handler
      VpcConfig:
        SubnetIds: [subnet-aaa111, subnet-bbb222]
        SecurityGroupIds: [sg-app456]
      Environment:
        Variables:
          DAX_ENDPOINT: !GetAtt DaxCluster.ClusterDiscoveryEndpointURL
      Policies:
        - Statement:
            - Effect: Allow
              Action: [dax:GetItem, dax:Query]
              Resource: !GetAtt DaxCluster.Arn
```

`ClusterDiscoveryEndpointURL` is the CloudFormation attribute that returns the cluster endpoint URL.

## 287: How do you add a health check for DAX in your app?

Do a cheap GetItem on a known small item, with a short timeout:

```js
export async function daxHealthy() {
  try {
    await Promise.race([
      dax.get({ TableName: "Config", Key: { pk: "health" } }),
      new Promise((_, reject) =>
        setTimeout(() => reject(new Error("timeout")), 500),
      ),
    ]);
    return true;
  } catch {
    return false;
  }
}
```

Don't let a failed DAX check mark the whole app unhealthy if you have a DynamoDB fallback.

## 288: How do you track DAX cost per team?

Add tags like `team` and `service` to each cluster and turn them on as cost allocation tags in the Billing console. Cost Explorer can then group DAX node-hour costs by team. Since DAX is billed per node, cost depends on cluster size, not on how many requests each team sends.

## 289: Should batch jobs read through DAX?

Usually not. A batch job that reads every item once doesn't benefit from caching, and it fills the cache with cold data, evicting items that real users need. Run batch reads directly against DynamoDB, ideally with on-demand or extra capacity, or use a table export to S3.

## 290: What is the best way to run analytics on data behind DAX?

Don't use DAX. Use DynamoDB export to S3 and query the export with Athena, or stream changes into another store. Analytics reads touch most of the data once, which is the opposite of what a cache is good at.

## 291: What happens step by step on a GetItem cache miss?

1. The client sends GetItem to a DAX node
2. The node checks its item cache and doesn't find the key
3. The node calls GetItem on DynamoDB (eventually consistent) with its service role
4. DynamoDB returns the item, or nothing
5. The node stores the item (or a negative entry) with the item TTL
6. The node returns the result to the client

## 292: What happens step by step on a PutItem through DAX?

1. The client sends PutItem to the primary node
2. The primary sends PutItem to DynamoDB
3. If DynamoDB fails (for example a condition fails), the error goes back and the cache is not changed
4. If it succeeds, the primary updates the item in its item cache
5. The primary returns success and replicates the change to the read replicas

## 293: Why should you avoid reading items you just scanned again through DAX?

A Scan result goes to the query cache, not the item cache. Reading those same items later with GetItem will miss the item cache the first time. Caches don't share entries, so plan which cache your hot reads will use.

## 294: What happens to query cache entries when an item in the result is deleted through DAX?

Nothing. The query cache entry still holds the deleted item until the entry's TTL ends. GetItem for that key will show it is gone, but the cached query will still list it. Apps that show lists after deletes should handle this, for example by removing the item from the UI after the delete call succeeds.

## 295: Can you use DAX with ExpressionAttributeNames for reserved words?

Yes. Expressions work the same as in DynamoDB, including `ExpressionAttributeNames` for reserved words like `name` or `status`. They're part of the request parameters, so they're also part of the query cache key.

## 296: Does DAX support all DynamoDB data types?

Yes. Strings, numbers, binary, booleans, null, lists, maps and sets are all supported, because DAX stores and returns items in DynamoDB's own format. The document client converts them to JavaScript values the same way `DynamoDBDocument` does.

## 297: How do you handle numbers bigger than JavaScript can hold with DAX?

DynamoDB numbers can have up to 38 digits, but a document client turns them into JavaScript `number`, which is only exact up to `Number.MAX_SAFE_INTEGER`. The DAX document client has the same issue as `DynamoDBDocument`. If you need exact large values, like IDs or money in small units, the simplest fix is to store them as strings.

## 298: What would you check before turning on DAX for an existing table?

- Read to write ratio (needs to be read-heavy)
- Share of strongly consistent reads (they won't benefit)
- Who writes to the table (anything that bypasses DAX causes staleness)
- How stale the data can be for each access pattern
- Whether all readers can run in the VPC with a DAX client
- Expected cost of the nodes vs savings and latency gains

## 299: How do you explain DAX to a non-technical stakeholder?

DAX is a fast memory layer in front of the database. It remembers recent answers, so repeated questions are answered almost instantly without asking the database again. The trade-off is that a remembered answer can be a few minutes old, so we only use it where that is acceptable.

## 300: What are the most common mistakes teams make with DAX?

- Creating a new DAX client per request
- Expecting writes to update cached queries
- Writing to the table from other tools and forgetting the cache
- Using one or two nodes in production
- Lowering table capacity too much and getting throttled on a cold cache
- Sending big scans or batch jobs through DAX
- Using DAX for data that must always be fresh

# Advanced Questions (301-450)

## 301: How does replication between the primary and read replicas work in DAX?

The primary applies each successful write to its own cache, then sends the change to the replicas through replication logs. Replicas apply the changes in order. AWS says this usually takes well under a second. Until a replica applies a change, reads from it can return the older value.

## 302: Why are reads through DAX eventually consistent even if all writes go through DAX?

Because of two delays. First, replicas get writes from the primary a little later, so a read that lands on a replica can be behind. Second, the query cache is never updated by writes. Even with perfect write discipline, DAX only promises eventual consistency.

## 303: Why doesn't DAX update the query cache when an item changes?

To do that, DAX would have to know every cached query whose result could include the changed item, including filters, ranges, indexes and limits. That's expensive and complex to track at high speed. DAX keeps it simple: query results live until TTL or eviction, and you choose the TTL that fits your freshness needs.

## 304: Why can't DAX cache strongly consistent reads?

A strongly consistent read must return every write that succeeded before it. A cache can't promise that, because DynamoDB may have been changed directly or the write may still be replicating between nodes. The only safe answer comes from DynamoDB itself, so DAX passes the read through.

## 305: Why does DAX pass TransactGetItems straight to DynamoDB?

TransactGetItems promises a consistent snapshot of several items at one point in time, checked against ongoing transactions. Cached copies might come from different moments, so DAX can't build that snapshot. It forwards the call to DynamoDB, which gives the real guarantee.

## 306: Why does DAX write to DynamoDB before updating its cache?

If DAX updated the cache first and the DynamoDB write then failed (for example a failed condition or throttling), the cache would hold data that never existed in the table. Writing to DynamoDB first and caching only on success keeps the cache from ever being ahead of the database for DAX writes.

## 307: Why is DAX write-through and not write-back?

A write-back cache confirms writes before saving them to the database and saves them later. It's faster, but data can be lost if a node fails, and it breaks DynamoDB's durability promise. DAX confirms a write only after DynamoDB has stored it, so DAX failures never lose data.

## 308: Describe a race where DAX keeps an older value even though every write succeeded.

Service A updates an item through DAX at time T1. Service B updates the same item directly in DynamoDB at T2. DynamoDB now has B's value, but DAX's item cache still holds A's value, because B's write never passed through DAX. Reads through DAX return A's value until the TTL ends, even though B's write was later.

## 309: How can a stale DAX read cause a lost update?

If code reads an item from DAX, changes a field in memory and writes the whole item back with PutItem, it may overwrite a newer version it never saw. That newer data is lost. Fix it by using UpdateItem with only the changed attributes, and a condition on a version attribute so stale writes fail instead of overwriting.

## 310: Why is a conditional write safe even if your read came from a stale cache?

The condition is evaluated by DynamoDB against the current item, not against the cache. If the cache was stale, the condition fails and nothing is written. So the stale read can cost you a retry, but it can't make the write wrong. This is why conditions are the right tool for correctness with DAX.

## 311: What happens inside DAX when the primary node fails?

DAX detects the failure and promotes one of the read replicas to primary. The client discovers the new layout and sends writes to the new primary. DAX then launches a replacement node, which joins as a replica with an empty cache. During the switch, some writes can fail and should be retried.

## 312: A write through DAX times out during a failover. Did it succeed?

You can't tell from the error. The write might have reached DynamoDB before the node failed, or it might not. Design writes to be safe to retry: use conditions (`attribute_not_exists` for creates, version checks for updates), idempotency keys, or `ClientRequestToken` for transactions. Then retrying is correct either way.

## 313: How does a three node, three AZ cluster behave when one AZ goes down?

The node in the failed zone becomes unreachable. If it was the primary, a replica in another zone is promoted. The client spreads reads over the two remaining nodes, so each gets more load, and read capacity drops by a third until DAX replaces the node. Size the cluster so two nodes can handle peak load.

## 314: Why doesn't adding nodes increase total DAX cache size?

Every node holds the full cache, not a slice of it. Adding a node adds a copy, which adds read throughput and fault tolerance but not memory. The cache size is limited by one node's memory. If the working set is bigger, you need a bigger node type.

## 315: How is DAX's scaling model different from a sharded cache like ElastiCache cluster mode?

ElastiCache cluster mode splits keys across shards, so total memory grows with each shard and each key lives on one shard. DAX copies the whole cache to every node, so memory is fixed by node size but any node can answer any read. DAX is simpler for reads and handles hot keys well; sharded caches handle much bigger datasets.

## 316: Why does DAX handle hot keys well?

Since every node can serve every key, reads for a hot key are spread across all nodes instead of hitting one shard. Adding replicas spreads them more. In a sharded cache, one very hot key can overload its shard, while in DAX the load is shared by the whole cluster.

## 317: How do you calculate how many nodes you need for read throughput?

Find the peak read rate one node handles at a safe CPU level in a load test. Then:

```
nodes = ceil(peak_reads_per_second / safe_reads_per_node) + 1
```

The extra node covers a node or AZ failure. Round up to at least three for production, and make sure the result fits the AZ spread you want.

## 318: Walk through a sizing example for DAX.

Say peak is 150,000 reads per second, the hit rate is 95 percent, and load tests show one `dax.r5.xlarge` node handles 50,000 reads per second at about 60 percent CPU. You need 3 nodes for the load plus 1 for failure, so 4 nodes. The table must still handle 7,500 reads per second from misses, plus more when the cache is cold.

## 319: How do you estimate memory needs for the item cache?

Estimate the number of hot items times their average size, plus overhead for metadata and keys. For example, 5 million hot items of 2 KB each is about 10 GB of raw data, so pick a node type with clearly more cache memory than that. Then load test and check `CacheMemoryUtilization` and `EvictedSize`.

## 320: Why should you keep spare capacity in a DAX cluster?

When a node fails or is replaced during maintenance, its traffic moves to the other nodes. If every node already runs hot, the rest can overload and start throttling. Also the replacement node starts cold, which increases table load for a while. Plan for one node missing at peak traffic.

## 321: What is a thundering herd problem with DAX?

When a very hot entry expires, many requests arrive at once and all miss. Each of them may go to DynamoDB for the same key at the same moment. Don't assume DAX merges these concurrent misses into one call. Make sure the table can handle short bursts on hot keys.

## 322: Why do all items in a DAX cluster share the same TTL, and what does it mean for design?

TTL is a cluster setting (through the parameter group), not per item or per table. Every item gets the same lifetime. If two tables have very different freshness needs, like product descriptions vs stock counts, one TTL won't suit both. You either compromise, read the fresh data with `ConsistentRead`, or use separate clusters.

## 323: When would you run several DAX clusters for the same app?

- Tables need different TTLs
- Tables need different IAM isolation (service roles)
- One workload's scans or bulk reads hurt another's hit rate
- Different teams need separate cost tracking or change control

The cost is more nodes and more to manage, so split only when there's a real need.

## 324: How can high-cardinality queries blow up the query cache?

If queries have many different parameter values (search terms, user IDs, time ranges), each one becomes a separate cache entry. Most are read once and never again. They take memory, push out useful entries and raise evictions. For such queries, set a short query TTL, cache them elsewhere, or skip DAX for them.

## 325: How do LRU and TTL work together?

TTL sets the longest time an entry can be served. LRU can remove it earlier if memory is needed. So an item read rarely may be evicted long before its TTL, while a hot item stays until the TTL ends. An entry is never served after its TTL, even if memory is free.

## 326: Explain the attribute name metadata issue in more detail.

DAX keeps a dictionary of attribute names it has seen so it can encode items efficiently. AWS docs say these names stay in memory even after the items are evicted. If your schema uses dynamic attribute names, like one attribute per day or per user ID, this dictionary keeps growing and can hurt the node over time. Keep attribute names to a fixed, small set.

## 327: How do item size and request rate affect node network limits?

Network bytes per second is roughly request rate times average response size. For example, 40,000 reads per second of 10 KB items is about 400 MB per second, which can reach a node's network limit before CPU. Watch the baseline network utilization metrics, project items to fewer attributes, or split large items.

## 328: Why may p99 latency barely improve after adding DAX?

Tail latency is driven by the slowest requests, and with DAX those are the cache misses, which still take DynamoDB time plus a hop. If even 2 percent of reads miss, p99 is still a DynamoDB read. p50 drops a lot, but p99 drops only if the hit rate is above 99 percent for that access pattern.

## 329: How do you calculate the expected average read latency with DAX?

```
avg = hit_ratio * hit_latency + (1 - hit_ratio) * miss_latency
```

With a 90 percent hit rate, 0.4 ms hits and 6 ms misses: `0.9 * 0.4 + 0.1 * 6 = 0.96 ms`. The misses add most of the average. Raising the hit rate from 90 to 98 percent cuts this to about 0.51 ms.

## 330: How can a busy Node.js event loop hide DAX speed?

DAX may answer in a few hundred microseconds, but if the event loop is busy with JSON parsing, heavy logging or CPU work, the promise callback waits in the queue. The measured latency then includes event loop delay. Measure event loop lag (for example with `perf_hooks.monitorEventLoopDelay`) next to DAX latency.

## 331: How should you benchmark DAX correctly?

- Run the load generator inside the same VPC and AZs as production
- Use realistic key distribution (hot and cold keys), not one key or fully random keys
- Warm the cache first, then measure steady state, and separately measure a cold start
- Use the production node type, not burstable nodes
- Record p50, p95, p99, hit ratio, node CPU and table capacity together

## 332: What security layers protect a DAX cluster?

- Network: VPC only, private subnets, security groups on 8111 or 9111
- Identity: IAM policies on `dax:` actions for callers, and a service role for DynamoDB access
- Encryption: at rest with AES-256, in transit with TLS
- Auditing: CloudTrail for management calls, CloudWatch for activity

All of these are set at cluster creation, and encryption can't be changed later.

## 333: Do fine-grained IAM conditions like dynamodb:LeadingKeys work through DAX?

Not in the way you might expect. Those conditions limit which partition keys a caller can access in DynamoDB. With DAX, DynamoDB sees the request as coming from the DAX service role, not from the caller. So a per-user `LeadingKeys` rule on the caller's DynamoDB policy is not applied to reads through DAX. If you need per-user row access, enforce it in your app or don't use DAX for that table.

## 334: How do you isolate tenants in a multi-tenant SaaS app that uses DAX?

DAX can't enforce tenant boundaries per caller. Options:

- Enforce tenant checks in the app (always include the tenant ID in keys and check it)
- Use separate clusters with separate service roles for high-security tenants
- Use separate tables per tenant group and give each cluster's role only those tables

Also watch for noisy tenants that evict others' data.

## 335: Your compliance team requires customer managed KMS keys. Can you use DAX?

Not for encryption at rest, because DAX only supports an AWS owned key. You'd need an exception from the compliance team, or you skip DAX and use DynamoDB directly (which supports customer managed keys), maybe with another cache that meets the rule. Bring this up early, because it can block the design.

## 336: Does TLS add much latency to DAX?

TLS adds the cost of encrypting each request and response, plus the handshake when connections open. Since the client keeps connections open, the handshake cost is paid rarely. The per-request cost is small but measurable at microsecond scale. Most teams accept it, and many security rules require it anyway.

## 337: How would you apply least privilege to a DAX setup?

- Service role: only the DynamoDB actions and tables (and indexes) the cluster needs; leave out writes for read-only clusters
- App roles: only the `dax:` actions they call, on the specific cluster ARN
- Admin roles: management actions, with `Resource: "*"` as required, kept separate from app roles
- Security groups: only app security groups as sources, only the one port in use

## 338: How do you audit who accessed data through DAX?

CloudTrail records management calls but is not a full log of reads through DAX. DynamoDB data events in CloudTrail, if enabled, show the DAX service role as the caller, not the end user. So for per-user audit trails, log access in your app with the user identity, and use VPC Flow Logs to see which hosts talk to DAX.

## 339: Why should dev and prod never share a DAX cluster?

A shared cluster means the service role must reach both dev and prod tables, so any dev app with `dax:` access could read prod data through it. Dev load could also evict prod data. Separate clusters, roles and ideally separate accounts keep them apart.

## 340: How do you plan disaster recovery for DAX?

DAX has no data to recover, so DR is about getting a cluster running and pointing apps to it. Keep the cluster defined in infrastructure as code, so you can recreate it in minutes. Make sure the app can run on DynamoDB alone (fallback) with enough table capacity while a new cluster starts and warms.

## 341: How do you design cross-region DR with DAX?

Use DynamoDB global tables for the data. In the DR region, either keep a running DAX cluster (costs money, but it's warm-ish from local traffic or a warm-up job) or create one during failover from your templates. Apps in the DR region must point to the local cluster endpoint. Plan table capacity for a cold cache right after failover.

## 342: How do global tables' conflict rules interact with DAX?

With multi-region global tables, conflicting writes in different regions are settled by last writer wins in DynamoDB. If the local DAX cached the local write, but a write from another region wins, the local table changes by replication and DAX doesn't see it. DAX keeps serving the losing value until TTL. Keep TTLs short, or avoid concurrent writes to the same item from several regions.

## 343: When can write-through make cache use worse?

If the app writes many items that are rarely read, each write through DAX puts that item into the item cache. These cold items take memory and push out hot items. For write-heavy, read-light tables, sending writes directly to DynamoDB (write-around) can give a better hit rate for the data that is actually read.

## 344: How would you decide which writes go through DAX?

Send writes through DAX when the item is likely to be read soon or is already hot, like profile updates, config changes and prices. Send writes directly to DynamoDB for bulk imports, logs, events and other data that won't be read through DAX soon. Document the rule so all teams follow it, since mixed writes cause staleness.

## 345: How should stream processors write to tables behind DAX?

If a Lambda processing a stream writes items that users read through DAX, those writes bypass DAX unless the Lambda also uses the DAX client. Put the processor in the VPC and write through DAX if fresh cached reads matter. Otherwise, accept staleness up to the TTL.

## 346: Why is "rewrite the item through DAX on every stream event" a bad idea?

It doubles writes and write cost, may trigger new stream events (a loop if not careful), and still leaves query cache entries stale. It also races with the original write. If freshness matters that much, make the original writer use DAX or don't cache that data.

## 347: What is the worst-case staleness for an item read with GetItem through DAX?

If the write went through DAX: about the replication delay, usually under a second. If the write bypassed DAX: up to the item TTL (`record-ttl-millis`) after the item was cached. If the item was never cached, the next read is a miss and returns fresh data.

## 348: What is the worst-case staleness for a Query through DAX on a GSI?

The GSI's own propagation delay, plus up to the query TTL (`query-ttl-millis`), plus any replication delay between nodes. Writes through DAX don't help, because the query cache isn't updated. So for a 5 minute query TTL, a list on a GSI can be just over 5 minutes old.

## 349: Is a BatchGetItem response through DAX a consistent snapshot?

No. Some items may come from cache (cached at different times) and others fresh from DynamoDB. The items in one response can reflect different moments. If you need a consistent snapshot of several items, use TransactGetItems, which passes through to DynamoDB.

## 350: What happens with Select COUNT queries through DAX?

A Query with `Select: "COUNT"` is cached like any other query result. The count can be stale for up to the query TTL. For counts that must be exact, either keep a counter item updated by writes, or run the count with `ConsistentRead: true` (base table or LSI only).

## 351: How do you make write retries safe through DAX after a timeout?

Make the write idempotent so running it twice has the same effect as once:

```js
await dax.put({
  TableName: "Payments",
  Item: { paymentId, orderId, amount, status: "CREATED" },
  ConditionExpression: "attribute_not_exists(paymentId)",
});
```

If the first attempt succeeded and you retry, the condition fails with `ConditionalCheckFailedException`, which you can treat as "already done" after checking the stored item. For updates, use a version check or set absolute values instead of increments.

## 352: Why are increments risky to retry through DAX?

`ADD count :one` is not idempotent. If a write timed out but actually succeeded, a retry adds one more time. To make it safe, store processed request IDs (for example with a condition on a set or a separate idempotency item) or use a transaction with `ClientRequestToken`.

## 353: How would you add a circuit breaker for DAX in Node.js?

Count recent DAX failures. When they pass a limit, stop calling DAX for a while and use DynamoDB directly, then try DAX again later:

```js
let failures = 0;
let openUntil = 0;

export async function read(params) {
  if (Date.now() < openUntil) return ddb.get(params);
  try {
    const res = await dax.get(params);
    failures = 0;
    return res;
  } catch (err) {
    if (err.name === "ConditionalCheckFailedException") throw err;
    if (++failures >= 5) openUntil = Date.now() + 30_000;
    return ddb.get(params);
  }
}
```

This stops every request from paying a timeout while DAX is down.

## 354: What is the risk of falling back to DynamoDB when DAX fails?

All reads that DAX used to absorb now hit the table at once. If the table's capacity was lowered because of DAX, it throttles and the outage spreads. Fallback only works if the table can take the full read load, for example on-demand mode or provisioned capacity with high enough limits.

## 355: How would you design graceful degradation for a read-heavy API using DAX?

- Normal: reads through DAX
- DAX failing: circuit breaker moves reads to DynamoDB
- Table throttling: serve a slightly older copy from a small in-process cache, or return partial results
- Load shedding: drop low priority requests (like recommendations) first

Test each step in staging so you know the app behaves well at each level.

## 356: How do you warm a new cluster before switching traffic to it?

Mirror real read traffic to the new cluster for a while (shadow reads), ignoring the results, or run a warm-up job that reads the top keys and top queries. Then switch the endpoint. Watch the new cluster's hit rate rise before moving all traffic. Make sure the shadow reads don't throttle the table.

## 357: Why can Lambda at high concurrency create too many DAX connections?

Each Lambda execution environment has its own DAX client, and each client opens connections to every node. With 2,000 concurrent environments and 5 nodes, that's a lot of connections. Watch `ClientConnections`, set reserved concurrency on the function, and consider a long running service (ECS) for very high, steady traffic.

## 358: How do idle Lambda environments affect DAX connections?

When a Lambda environment is frozen between invocations, its connections may be closed by the other side. On the next invocation the client may find stale connections and need to reconnect or retry. This can show up as rare errors or slow first requests. Handle them with retries and keep the client at module level.

## 359: When is DynamoDB alone fast enough so DAX isn't needed?

DynamoDB often answers in single-digit milliseconds. If your API's latency target is 50 or 100 ms and the database part is a small share of that, DAX won't change much for users. DAX matters when database time is a large share of a tight budget, or when you need to remove hot key throttling or lower read cost at very large scale.

## 360: How do you model DAX cost against DynamoDB read savings?

```
dax_monthly = node_price_per_hour * node_count * 730
saved_reads = monthly_eventually_consistent_reads * hit_ratio
ddb_savings = saved_reads * price_per_read
```

For on-demand, price per read depends on item size (4 KB units) and consistency. If `ddb_savings` is much lower than `dax_monthly`, DAX only makes sense if latency is a hard requirement.

## 361: How do you choose between R5 and R7i node types?

R7i is the newer generation (added in April 2025) and usually gives better price-performance than R5 at the same size. For new clusters, start with R7i if it's available in your region, and compare with a load test. Existing R5 clusters can move to R7i with a blue/green cluster switch.

## 362: What should you do before reducing the number of nodes?

Check that the remaining nodes can handle peak traffic with one node missing, and that CPU won't spike. Do it during low traffic. Removing nodes doesn't lose data, but it reduces read capacity and fault tolerance, and the primary should not be in the list you remove.

## 363: What happens right after you add a node?

The new node starts with an empty cache. The client starts sending it a share of reads, which mostly miss at first. Overall hit rate drops a little and table reads rise until the new node warms. Add nodes before peak traffic, not during it.

## 364: How can you automate DAX scaling since there's no auto scaling?

Use a CloudWatch alarm on CPU or throttles that triggers a Lambda (through SNS or EventBridge). The Lambda calls `IncreaseReplicationFactor` or `DecreaseReplicationFactor`:

```js
import {
  DAXClient,
  IncreaseReplicationFactorCommand,
} from "@aws-sdk/client-dax";

const dax = new DAXClient({});

export const handler = async () => {
  await dax.send(
    new IncreaseReplicationFactorCommand({
      ClusterName: "my-cluster",
      NewReplicationFactor: 5,
    }),
  );
};
```

Add limits and cooldowns so it doesn't scale in a loop.

## 365: How do you scale DAX for predictable daily peaks?

Use scheduled scaling: an EventBridge schedule runs a Lambda that adds nodes before the daily peak and removes them after. Add them early enough for new nodes to warm. This is often simpler and safer than reacting to alarms.

## 366: How do you test DAX failover?

In staging, run steady load, then reboot the primary node with `aws dax reboot-node`. Watch client errors, retries, latency and how long until writes work again. Also test losing a whole AZ by blocking traffic to one node with security groups or NACLs. Fix any part of the app that fails badly.

## 367: Why might your tracing tool not show DAX calls?

Auto-instrumentation for the AWS SDK hooks into SDK clients that make HTTP calls. The DAX client uses its own protocol, so tools that trace DynamoDB HTTP calls may not see DAX calls at all. Add manual spans around DAX calls so traces still show database time.

## 368: How do you add manual tracing around DAX calls with OpenTelemetry?

```js
import { trace, SpanStatusCode } from "@opentelemetry/api";

const tracer = trace.getTracer("dax");

export async function tracedGet(params) {
  return tracer.startActiveSpan("dax.get", async (span) => {
    span.setAttribute("db.system", "dynamodb");
    span.setAttribute("db.dynamodb.table_names", [params.TableName]);
    try {
      return await dax.get(params);
    } catch (err) {
      span.recordException(err);
      span.setStatus({ code: SpanStatusCode.ERROR });
      throw err;
    } finally {
      span.end();
    }
  });
}
```

## 369: How can you get hit or miss info per request without CloudWatch?

The response doesn't tell you. A practical trick is to record client side latency in a histogram: hits cluster well under a millisecond and misses at several milliseconds, so you can estimate the hit rate per route or per table from the latency distribution.

## 370: Users report seeing old data for a few minutes after editing a post. How do you debug it?

1. Check how the edit is written: through DAX or directly to DynamoDB
2. Check how the post is read: GetItem (item cache) or Query (query cache)
3. If it's read by Query, the query cache won't update until `query-ttl-millis`
4. If it's written directly, the item cache won't update either

Fixes: write through DAX, read the single post by key, lower the query TTL, or show the edited value from the write response.

## 371: Deleted comments still appear in lists for a while. Why?

The comment list is a Query, cached in the query cache. Deleting a comment through DAX updates the item cache but not the cached query result. The list shows the comment until the query TTL ends. Lower the query TTL for comments, filter out deleted IDs on the client, or use a soft delete flag checked against the item cache.

## 372: New users get "not found" right after signup. What could cause it?

A likely cause is negative caching. The app checks if the user exists (miss, so "not found" is cached), then a separate system, like a Cognito trigger or another service, creates the user directly in DynamoDB. Reads through DAX keep returning the cached "not found" until the TTL ends. Fix it by creating the user through DAX or reading with `ConsistentRead: true` right after signup.

## 373: A product launch throttled the table even though DAX was in place. What went wrong?

Possible causes:

- The cluster was new or recently restarted, so the cache was cold
- The product item was created right before launch, and early reads cached it, but stock reads used `ConsistentRead: true`
- Many unique query parameters missed the cache
- The table capacity was lowered too much because of DAX

Warm the cache before launch, keep table capacity ready for misses, and check how reads are sent.

## 374: Only the primary node shows high CPU. What does that tell you?

The primary handles all writes and replication. High CPU only there usually means a write-heavy load, like a bulk import running through DAX. Move bulk writes to go directly to DynamoDB, or reduce write rate. Adding replicas won't help, since they don't take writes.

## 375: Evictions jumped after a new feature shipped. What would you check?

Look for new scans or high-cardinality queries going through DAX, larger items being cached, or bulk writes through DAX. Compare per-operation request counts before and after. The fix is usually to route the new heavy pattern directly to DynamoDB or to use a bigger node type.

## 376: Latency spikes happen every Sunday morning. What's a likely reason?

The DAX maintenance window may be set to that time, and node replacements cause short errors and cold nodes. Check `describe-events` for maintenance events at those times. Move the window to a quieter time and make sure retries and fallback handle it.

## 377: A small app pays more for DAX than for DynamoDB. What do you do?

Compare the read savings and the latency gain to the node cost. If the app reads a few hundred items per second and users don't notice a few milliseconds, remove DAX and use DynamoDB directly. If latency matters, try a smaller node type for the cluster, but don't drop below what's needed for availability.

## 378: How would you migrate from an ElastiCache cache-aside setup to DAX?

1. Find all cache reads and writes in the code
2. Replace "check cache, then DynamoDB, then fill cache" with a DAX read
3. Replace "write DynamoDB, then delete cache key" with a DAX write
4. Keep ElastiCache for data DAX can't cache (computed results, data from other sources)
5. Roll out with a flag and compare hit rates and latency

## 379: When would you move from DAX to ElastiCache?

When you need things DAX can't do: caching computed or joined results, per-entry TTLs, explicit invalidation of keys, data structures like sorted sets, caching data from several databases, or a sharded cache bigger than one node's memory. You also move if you need customer managed keys or clients that can't use a DAX library.

## 380: One tenant's traffic is pushing other tenants' data out of DAX. What can you do?

Check which access patterns that tenant uses (scans, many unique queries). Rate limit that tenant, route its heavy reads directly to DynamoDB, or move it to its own table and cluster. Bigger nodes also help if the total working set no longer fits.

## 381: Your app needs low latency reads in three regions. How do you design it with DAX?

Use a global table replicated to the three regions. In each region, run a DAX cluster in the app's VPC and point the local app at it. Keep TTLs short because writes from other regions bypass local DAX. Route users to the closest region with DNS latency routing or Global Accelerator.

## 382: Lambda functions time out when calling DAX. What would you check?

- The Lambda is in the right VPC and subnets
- Its security group is allowed on the DAX port
- The endpoint scheme matches the cluster (`dax://` or `daxs://`)
- The client is created outside the handler
- The function timeout is long enough for the cold start client setup
- `ClientConnections` and node CPU are not maxed out

## 383: Two requests from the same user show different values for the same item. Why?

The two requests probably went to different nodes, and one of them hadn't applied the latest replicated write yet. DAX doesn't promise monotonic reads, so a later read can show an older value than an earlier read. Design the UI to tolerate this, or use `ConsistentRead: true` where it matters.

## 384: Can you make the DAX client always read from the same node?

Not in a supported way. The client chooses nodes and spreads load. Pinning to one node would remove load balancing and failover. Instead, design for eventual consistency and use strongly consistent reads where you need read-your-writes.

## 385: What is monotonic read consistency, and does DAX provide it?

Monotonic reads mean that once you've seen a value, you never see an older one later. DAX doesn't promise this, because successive reads can land on nodes at different replication points, and direct writes plus TTL can make values jump. If your logic needs it, track a version and ignore older versions in the app.

## 386: How can a version attribute help detect stale reads from DAX?

Store a `version` number that increases on every write. The client remembers the highest version it saw. If a later read returns a lower version, the client knows it's stale and can retry with `ConsistentRead: true` or keep its newer copy.

```js
if (Item.version < lastSeenVersion) {
  ({ Item } = await dax.get({
    TableName: "Docs",
    Key: { docId },
    ConsistentRead: true,
  }));
}
```

## 387: How do you avoid re-reading after an update when using DAX?

Ask DynamoDB to return the new item in the update response:

```js
const { Attributes } = await dax.update({
  TableName: "Users",
  Key: { userId },
  UpdateExpression: "SET displayName = :n",
  ExpressionAttributeValues: { ":n": name },
  ReturnValues: "ALL_NEW",
});
return Attributes;
```

The returned values come from DynamoDB after the write, so they are current, and you skip a read that could hit a stale node.

## 388: Why would you split an item into a read-hot part and a write-hot part?

If one item holds both rarely changed data (like a product description) and often changed data (like a view counter), every counter write replaces the cached item and can cause staleness on other nodes. Splitting them into two items lets the description stay cached and stable, while the counter is read with a short TTL or consistent read.

## 389: Why can splitting large items improve DAX efficiency?

If a 300 KB item is read only for its title and price, caching the whole item wastes memory and network. Storing a small summary item (title, price, image URL) for list and card views, and the big detail item separately, lets many more summaries fit in memory and makes hot reads cheaper.

## 390: How does denormalization interact with DAX?

Denormalized data is copied into several items to avoid extra reads. With DAX, those copies are cached separately, so when the source changes, some copies may be updated (through DAX writes) and others not yet. Readers can see mixed old and new values for a while. Keep denormalized fields that must match in the same item, or accept the short gap.

## 391: When is a precomputed result item better than relying on the query cache?

When many different readers need the same aggregated list and it must update on writes. A precomputed item (like "top 20 products in category X") written through DAX updates the item cache at once. A cached Query only refreshes after TTL. Precomputed items also cost one small GetItem instead of a larger query.

## 392: When can the query cache be better than precomputed items?

When the list is read often, changes slowly and has many variants (sort orders, categories, pages). Precomputing every variant is a lot of work and storage. The query cache gives you caching for any variant that is actually requested, without extra code, as long as some staleness is fine.

## 393: How do you keep query parameters stable so requests share cache entries?

Build query requests in one place with fixed placeholder names, fixed projection and fixed limits. Two queries with the same meaning but different placeholder names (`:pk` vs `:p`) or different projection order may be treated as different requests. Normalize values too, like lowercasing search terms and rounding time ranges.

## 394: Why are only the first pages of a list usually worth caching?

Most users look at page one, fewer at page two, and almost nobody at page ten. The first page gets a high hit rate, while deep pages are mostly misses that just take memory. Some teams send page one through DAX and deeper pages directly to DynamoDB.

## 395: Should parallel scans go through DAX?

Generally no. A parallel scan uses `Segment` and `TotalSegments` to read the whole table in parallel, usually once. Each segment result would be cached separately, using lots of memory with no reuse. Run parallel scans against DynamoDB directly with enough capacity, or use a table export.

## 396: How do ConditionCheck items work in a transaction through DAX?

A `ConditionCheck` in TransactWriteItems checks a condition on an item without changing it. DAX passes the transaction to DynamoDB, which checks everything at once. Since condition checks don't change items, nothing in the cache needs to change for them. The service role needs `dynamodb:ConditionCheckItem` for this to work.

## 397: Does DAX lower the cost of transactions?

No. Transactional writes still cost twice the normal write units in DynamoDB, and TransactGetItems is passed through, so it costs twice the normal read units too. DAX doesn't cache transactional reads, so it gives no savings there.

## 398: How does DAX help with DynamoDB adaptive capacity limits?

DynamoDB has per-partition limits (around 3,000 read units per second per partition) even with adaptive capacity. A very hot key can hit that limit. DAX serves most reads of that key from memory, so the partition sees only cache misses, which are a small fraction. This is one of the strongest reasons to use DAX.

## 399: About how many reads reach DynamoDB for a very hot key behind DAX?

In steady state, each node fetches the key once when its cached copy expires, so it's roughly the number of nodes per TTL period, plus bursts if many requests miss at the same moment. With 5 nodes and a 5 minute TTL, that's a handful of reads every 5 minutes, even if the key gets 100,000 reads per second.

## 400: Do DynamoDB response size limits still apply through DAX?

Yes. Query and Scan still return at most 1 MB of data per page, and BatchGetItem still returns at most 16 MB and 100 items per call. DAX doesn't change these limits, and caching a result doesn't make larger pages possible.

## 401: Why does DAX use its own protocol instead of HTTPS like DynamoDB?

The goal of DAX is microsecond reads. HTTP request parsing, headers and request signing on every call add overhead that matters at that scale. A compact binary protocol over long lived connections keeps each request small and fast. The cost is that you need a special client library.

## 402: Why does DAX use client side discovery instead of a load balancer?

A load balancer adds an extra network hop and its own latency to every request, which would eat into the microsecond gains. With client side discovery, the client knows every node, talks to them directly and sends writes straight to the primary. It also reacts to node failures without waiting for health checks on a load balancer.

## 403: Why is DAX only reachable inside a VPC?

DAX nodes are servers in your network with a custom protocol, and keeping them private reduces exposure. It also keeps latency low, since clients sit close to the nodes. Access control then has two layers: network rules (security groups) and IAM.

## 404: How does the client learn about cluster changes like new or replaced nodes?

The client connects to the cluster endpoint, gets the list of nodes, and keeps that list up to date over time. When nodes are added, removed or replaced, the client picks up the change and adjusts. That's why your config should hold only the cluster endpoint, not node addresses.

## 405: How would you protect DAX from a sudden client side traffic spike?

Limit concurrency in the app (for example with a semaphore around DAX calls), rate limit expensive patterns like scans, and use backoff on throttling. In Lambda, set reserved concurrency. Also keep CPU headroom on the cluster so short spikes don't cause throttling.

## 406: How do you handle very large query results through DAX without using too much memory in Node?

Read page by page and process each page before getting the next, instead of collecting everything into one array:

```js
async function* queryAll(params) {
  let ExclusiveStartKey;
  do {
    const res = await dax.query({ ...params, ExclusiveStartKey });
    yield* res.Items ?? [];
    ExclusiveStartKey = res.LastEvaluatedKey;
  } while (ExclusiveStartKey);
}

for await (const order of queryAll({
  TableName: "Orders",
  KeyConditionExpression: "customerId = :c",
  ExpressionAttributeValues: { ":c": "c-42" },
})) {
  console.log(order.orderId);
}
```

If the query is large and rare, send it to DynamoDB directly so it doesn't fill the cache.

## 407: How do you define SLOs for an app that uses DAX?

Set SLOs on what users see: API latency (p95, p99) and error rate. Then add internal indicators: DAX hit ratio, DAX error and throttle counts, and table throttles. Don't make "DAX available" the SLO itself, because a good fallback can keep the user SLO even when DAX is down.

## 408: What should a DAX outage runbook include?

- How to confirm the problem (metrics, `describe-clusters`, `describe-events`)
- How to switch the app to DynamoDB only (flag or config)
- How to raise table capacity or switch it to on-demand
- How to reboot or replace a node, or recreate the cluster from IaC
- How to switch back and watch the cache warm up
- Who to contact and how to open an AWS support case

## 409: Why should the DAX endpoint come from infrastructure code outputs?

If you replace the cluster (node type change, encryption change), the endpoint changes. When apps read the endpoint from a stack output or a parameter written by the stack, they pick up the new value on the next deploy. Hardcoded endpoints break silently when the cluster is replaced.

## 410: When should you fix the table design instead of adding DAX?

If throttling comes from a hot partition key for writes, a bad key choice, or scans used where queries would work, DAX only hides part of the problem. Fix the access patterns and keys first. Add DAX when reads are already well designed but you still need lower latency or less read load.

## 411: Design the read path for a product page that gets 1 million reads per second.

- CloudFront caches the public HTML and JSON where possible
- Behind it, the API reads product summary items with GetItem through a DAX cluster of R nodes, sized from load tests with one spare node
- Price and stock come from separate small items; stock is read with `ConsistentRead: true` only at checkout
- Writes to products go through DAX
- The table is on-demand or has high limits for cold cache and fallback
- Alarms on hit ratio, DAX CPU and table throttles

## 412: Design a social feed with DAX. What would you cache?

Cache user profiles and post items with GetItem through DAX, since they're read many times. Feed lists (Query on a feed partition) can use the query cache with a short TTL, maybe 10 to 30 seconds. New posts by the user themselves should be added to their own view from the write response, so they never wait for the TTL.

## 413: Would you use DAX or ElastiCache for a session store?

If sessions are already in DynamoDB and read on every request, DAX gives fast reads with no extra code. But sessions change often (last seen time, cart), and logouts must take effect quickly, so stale cache is risky. Many teams pick ElastiCache (Valkey or Redis OSS) for sessions because it supports explicit deletes and per-key TTL. If you use DAX, read sessions with `ConsistentRead` on security-sensitive checks.

## 414: Design a "latest reading per device" API for IoT with DAX.

Store the latest reading as one item per device (`pk = DEVICE#id`), overwritten on each update. Dashboards read it with GetItem through DAX. If devices write directly to DynamoDB (for example through IoT rules), DAX won't see the writes, so keep the item TTL short, like a few seconds, or read with `ConsistentRead` when the UI needs the exact last value.

## 415: Would you build a rate limiter on DAX?

No. A rate limiter needs exact, current counters updated many times per second. DAX doesn't help writes, and its reads can be stale, so limits would leak. Use atomic counters in DynamoDB directly with conditions, or a Valkey/Redis counter with `INCR` and expiry.

## 416: How would you handle inventory reservations if the catalog is behind DAX?

Use DAX for showing stock on product pages, where a slightly old number is fine. For reserving stock, do a conditional UpdateItem that decreases stock only if enough is left. DynamoDB checks the condition on the real value, so cached stock numbers can never cause overselling.

```js
await dax.update({
  TableName: "Inventory",
  Key: { sku },
  UpdateExpression: "SET available = available - :q",
  ConditionExpression: "available >= :q",
  ExpressionAttributeValues: { ":q": qty },
});
```

## 417: Should you put DAX in front of every DynamoDB table by default?

No. DAX adds cost, network setup, a special client and consistency rules every developer must understand. Use it for specific read-heavy tables where latency or read cost or hot keys are a real problem. Many tables do fine with DynamoDB alone.

## 418: What questions would you ask before approving DAX in a design review?

- What's the read to write ratio, and which reads repeat?
- What's the latency target, and how much of it is database time?
- Which reads must be strongly consistent?
- Who writes to the table, and do they all go through DAX?
- How stale can each access pattern be?
- What happens when DAX is down?
- What's the cost compared with the savings?

## 419: How does DAX change the way you test an app?

You need to test stale reads on purpose: write directly to DynamoDB, then read through DAX and check the app handles old data. Test negative caching, query cache staleness after writes, failover and fallback. Unit tests can fake the client, but these behaviors need integration tests against a real cluster.

## 420: How would you simulate stale data in an integration test?

```js
// 1. Read through DAX so the item is cached
await dax.get({ TableName: "Users", Key: { userId: "u-1" } });

// 2. Change it directly in DynamoDB, bypassing DAX
await ddb.update({
  TableName: "Users",
  Key: { userId: "u-1" },
  UpdateExpression: "SET plan = :p",
  ExpressionAttributeValues: { ":p": "enterprise" },
});

// 3. Read through DAX again: you get the old plan until the TTL ends
const { Item } = await dax.get({ TableName: "Users", Key: { userId: "u-1" } });
console.log(Item.plan); // old value
```

Then check that your app logic handles this case correctly.

## 421: What is the trade-off between a long TTL and data freshness in numbers?

With a 5 minute TTL and a hot item read 1,000 times per second per node, the table sees one read per node per 5 minutes for it, and data can be up to 5 minutes old (if written directly). With a 10 second TTL, the table sees 30 reads per node per 5 minutes, still tiny, and data is at most 10 seconds old. For hot items, short TTLs cost very little.

## 422: Why do short TTLs hurt less for hot items than for warm items?

A hot item is read so often that even with a short TTL it's almost always cached; only one read per TTL per node misses. A warm item, read once a minute, gets a miss on almost every read if the TTL is 30 seconds. So TTL mostly affects the hit rate of medium popularity data, not the hottest keys.

## 423: How do you choose TTL based on access frequency?

Look at the time between reads of typical items. If most items are read again within 2 minutes, a TTL above 2 minutes gives a good hit rate. If items are read once every 10 minutes, you need a TTL above 10 minutes to benefit, which may be too stale. In that case, DAX might not be worth it for those items.

## 424: How does DAX compare with RDS read replicas?

Both take read load off the main database. RDS read replicas are full database copies that run any SQL query, with replication lag. DAX is an in-memory cache for DynamoDB that only stores what was recently read and answers much faster. DAX entries also expire by TTL, while replicas follow the primary continuously.

## 425: Why does DAX not support DynamoDB's control plane, and what does it mean for your code?

DAX is a data cache, and table management has nothing to cache. So your code always needs a normal DynamoDB client for things like `DescribeTable`, `CreateTable`, backups, TTL settings and streams. Keep two clients in apps that do both, and don't route admin tasks through DAX.

## 426: How would you design an app to run with or without DAX?

Put all DynamoDB access behind a small data layer that receives a client (DAX or DynamoDB) at startup. Make all correctness-sensitive reads use `ConsistentRead: true` or conditional writes, so behavior is correct with either client. Then DAX becomes a performance option that can be turned off without code changes.

## 427: What happens if you change a parameter group while the cluster is busy?

New TTL values apply only to entries cached after the change, so the effect is gradual. Lowering the TTL slowly increases misses as old entries expire, and raising it slowly increases the hit rate. Watch table read capacity after lowering TTL, because misses can grow over the next TTL period.

## 428: Why is it hard to reason about "the cache state" in DAX?

Each node fills its own cache from the reads it serves, evicts with its own LRU, and receives writes through replication. So at any moment, nodes can hold different sets of items with different ages. Reason about worst-case staleness (TTL and replication delay) rather than an exact state.

## 429: What happens if two clients write the same item through DAX at nearly the same time?

Both writes go through the primary to DynamoDB. DynamoDB applies them in some order, and the last one applied wins in the table. The cache should end up with the result of the writes it processed, but don't depend on exact ordering between concurrent writers. Use conditions or versions if the order matters for your logic.

## 430: How does DAX treat items larger than what's useful to cache?

DAX caches what it reads, regardless of size, up to the DynamoDB 400 KB item limit. There's no setting to skip large items. If large items are rarely reused, read them directly from DynamoDB so they don't take cache memory.

## 431: How do you decide between dax.t3 and an R node for a small production service?

T3 nodes are cheap but burstable, with smaller memory and CPU. A small, steady service with low CPU may run fine on T3, but you risk surplus credit charges and less predictable latency. For production with a latency SLO, most teams pick the smallest R node, and use three of them for availability.

## 432: What problems can a single-node DAX cluster cause in production?

A single node has no failover. Maintenance, a node failure or an AZ outage takes the whole cache down, and all reads either fail or (with fallback) hit DynamoDB at once. When the node comes back, it's cold. That's acceptable for dev, but not for production.

## 433: How can you tell if your cluster's working set fits in memory?

If `CacheMemoryUtilization` is high but `EvictedSize` is low and the hit rate is stable, it fits. If evictions are steady and the hit rate drops when traffic grows, the working set is bigger than memory. A test: temporarily move to a bigger node type and see whether the hit rate goes up.

## 434: What is the risk of using DAX for authorization data like roles and permissions?

If permissions are revoked by a direct write to DynamoDB, or the check reads a cached query, a user may keep access until the TTL ends. For permission checks, either write changes through DAX and read by key, use a very short TTL, or read with `ConsistentRead: true` for sensitive actions.

## 435: How do you explain the difference between DAX TTL and DynamoDB TTL in an interview?

DAX TTL is how long a cached copy stays in the DAX cache. It's set per cluster in milliseconds and doesn't touch the table. DynamoDB TTL is a table feature that deletes items after a timestamp stored in an attribute, usually within a few days of expiry. They're unrelated, and DynamoDB TTL deletes don't update DAX.

## 436: Why might you still need ElastiCache even when using DAX?

DAX only caches DynamoDB reads. You may also need to cache API results from other services, rendered fragments, computed recommendations, or session data with per-key expiry. ElastiCache covers these. Using both is common in larger systems.

## 437: How does using DAX affect DynamoDB contributor insights or table metrics?

Table metrics like consumed read capacity and contributor insights only see requests that reach DynamoDB, so cache hits are invisible there. Hot keys served by DAX won't show up as hot in DynamoDB. To understand real access patterns, combine table metrics with DAX metrics and your own app logs.

## 438: How would you handle a schema change, like renaming an attribute, with DAX?

Cached items keep the old shape until they expire or are rewritten. During the change, your code must read both the old and new attribute names. Roll out code that handles both, migrate items (through DAX if you want the cache updated), wait at least one TTL, then remove support for the old name.

## 439: What's the effect of DAX on DynamoDB Streams consumers?

Writes through DAX reach DynamoDB normally, so they appear in streams like any other write. Consumers don't need to know DAX exists. But if consumers write back to the table directly, those writes bypass DAX and leave the cache stale.

## 440: How would you secure DAX access from a container platform with many services?

Give each service its own IAM role (for example ECS task roles or EKS pod identities) with only the `dax:` actions it needs on the specific cluster. Use a separate security group per service and allow only those groups in the DAX security group. If services need different table access, give them separate clusters.

## 441: How does DAX's IAM model compare with direct DynamoDB access for least privilege?

With direct access, each caller's IAM policy controls exactly which tables, actions and even keys it can touch. With DAX, the caller's policy controls which DAX actions on which cluster, and the cluster's service role controls the tables. So the real permission boundary is the cluster, which is coarser. Plan clusters around permission boundaries.

## 442: What changed in 2025 for DAX that is useful to know in interviews?

In March 2025, AWS released the DAX SDK for JavaScript v3 (`@amazon-dax-sdk/lib-dax`), so Node apps no longer need SDK v2 for DAX. In April 2025, R7i node types were added. The create-cluster API also supports a network type setting for IPv4, IPv6 or dual stack.

## 443: Why might an older Node project still use amazon-dax-client?

It was built before the v3 DAX client existed (March 2025), when the only option was SDK v2 with `amazon-dax-client`. Such projects often still use `aws-sdk` v2 for everything. Since SDK v2 reached end of support in 2025, moving to v3 and `@amazon-dax-sdk/lib-dax` should be on the roadmap.

## 444: What would you look for when reviewing code that uses DAX?

- The client is created once, not per request
- Strongly consistent reads are used only where needed
- No code assumes writes refresh cached queries
- Conditional writes protect important updates
- Bulk jobs and scans don't go through DAX
- There's error handling, retries and maybe a fallback
- Admin calls use a normal DynamoDB client

## 445: How can a code change silently lower the DAX hit rate?

Adding a new attribute to `ProjectionExpression`, changing a `Limit`, adding a filter, or including a request ID or timestamp in expression values creates new query cache keys. The old entries stop being used and the new ones start cold. Review query parameter changes for hot queries and watch hit rate after deploys.

## 446: How do you prove DAX is worth keeping after a year?

Look at hard numbers: DAX node cost, DynamoDB read cost saved (from hit counts), p50 and p99 latency with and without DAX (from a canary or test), and incidents prevented, like hot key throttling. If savings and latency gains are small, removing DAX simplifies the system.

## 447: What is the hardest part of running DAX well?

Not the setup, which is quick. The hard part is consistency discipline across teams: everyone must know that reads can be stale, that queries aren't refreshed by writes, and that direct writes bypass the cache. Most DAX incidents come from those assumptions, not from DAX failures.

## 448: If you could change one DAX default for most apps, what would it be?

Many apps would do better with a shorter query cache TTL than the default 5 minutes, because stale lists are the most common user-visible problem. The item cache can keep a longer TTL when writes go through DAX. Of course, the right value depends on the app's data and traffic.

## 449: How would you explain the main DAX trade-offs in one answer?

DAX gives microsecond reads and less DynamoDB read load for repeated, eventually consistent reads, with almost no code change. In exchange, you pay for nodes all the time, run inside a VPC with a special client, accept stale data up to the TTL, get no help for writes or strongly consistent reads, and lose per-caller table permissions.

## 450: When would you recommend against DAX in a system design interview?

When the system is write-heavy, needs strong consistency on most reads, has mostly unique reads, has low traffic where node cost outweighs savings, needs per-user table permissions, can't run its readers in a VPC, or needs features like explicit invalidation or customer managed keys. In those cases, DynamoDB alone or a general cache like ElastiCache is a better fit.
