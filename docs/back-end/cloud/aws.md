# AWS Certified Developer - Associate Interview Questions and Answers

_Last updated: October 24, 2026_

Interview questions and answers based on the AWS Certified Developer - Associate (DVA-C02) exam guide. The questions are grouped by the four exam domains, with 50 questions in each:

| Domain                           | Weight in exam | Questions |
| -------------------------------- | -------------- | --------- |
| Development with AWS Services    | 32%            | 1 - 50    |
| Security                         | 26%            | 51 - 100  |
| Deployment                       | 24%            | 101 - 150 |
| Troubleshooting and Optimization | 18%            | 151 - 200 |

Code examples use the AWS SDK for JavaScript v3, boto3 (Python), the AWS CLI v2, SAM and CloudFormation. Account IDs, ARNs and names in the examples are placeholders.

## Table of Contents

- [Domain 1: Development with AWS Services](#domain-1-development-with-aws-services)
  - [1: What is AWS Lambda and when would you use it?](#1-what-is-aws-lambda-and-when-would-you-use-it)
  - [2: What are the three ways Lambda can be invoked?](#2-what-are-the-three-ways-lambda-can-be-invoked)
  - [3: What does a Lambda handler look like in Python and Node.js?](#3-what-does-a-lambda-handler-look-like-in-python-and-nodejs)
  - [4: Why should you create SDK clients and database connections outside the handler?](#4-why-should-you-create-sdk-clients-and-database-connections-outside-the-handler)
  - [5: What are the main Lambda limits a developer should know?](#5-what-are-the-main-lambda-limits-a-developer-should-know)
  - [6: What are Lambda layers?](#6-what-are-lambda-layers)
  - [7: How do you pass configuration to a Lambda function?](#7-how-do-you-pass-configuration-to-a-lambda-function)
  - [8: What is the Lambda execution environment lifecycle?](#8-what-is-the-lambda-execution-environment-lifecycle)
  - [9: What is the difference between Lambda destinations and a dead-letter queue?](#9-what-is-the-difference-between-lambda-destinations-and-a-dead-letter-queue)
  - [10: How does Lambda retry asynchronous invocations?](#10-how-does-lambda-retry-asynchronous-invocations)
  - [11: How do you process SQS messages with Lambda and handle partial failures?](#11-how-do-you-process-sqs-messages-with-lambda-and-handle-partial-failures)
  - [12: What is a Lambda function URL?](#12-what-is-a-lambda-function-url)
  - [13: How do you deploy a Lambda function as a container image?](#13-how-do-you-deploy-a-lambda-function-as-a-container-image)
  - [14: What are the differences between REST APIs, HTTP APIs and WebSocket APIs in API Gateway?](#14-what-are-the-differences-between-rest-apis-http-apis-and-websocket-apis-in-api-gateway)
  - [15: What is the difference between proxy and non-proxy integrations?](#15-what-is-the-difference-between-proxy-and-non-proxy-integrations)
  - [16: What are mapping templates in API Gateway?](#16-what-are-mapping-templates-in-api-gateway)
  - [17: What are API Gateway stages and stage variables?](#17-what-are-api-gateway-stages-and-stage-variables)
  - [18: What are usage plans and API keys?](#18-what-are-usage-plans-and-api-keys)
  - [19: How do you enable CORS for an API?](#19-how-do-you-enable-cors-for-an-api)
  - [20: What is Amazon DynamoDB and what kinds of primary keys does it support?](#20-what-is-amazon-dynamodb-and-what-kinds-of-primary-keys-does-it-support)
  - [21: How do you choose a good partition key?](#21-how-do-you-choose-a-good-partition-key)
  - [22: What is the difference between Query and Scan?](#22-what-is-the-difference-between-query-and-scan)
  - [23: What is the difference between an LSI and a GSI?](#23-what-is-the-difference-between-an-lsi-and-a-gsi)
  - [24: How do you calculate RCUs and WCUs?](#24-how-do-you-calculate-rcus-and-wcus)
  - [25: What is the difference between on-demand and provisioned capacity?](#25-what-is-the-difference-between-on-demand-and-provisioned-capacity)
  - [26: How do conditional writes and optimistic locking work in DynamoDB?](#26-how-do-conditional-writes-and-optimistic-locking-work-in-dynamodb)
  - [27: How do DynamoDB transactions work?](#27-how-do-dynamodb-transactions-work)
  - [28: What are DynamoDB Streams?](#28-what-are-dynamodb-streams)
  - [29: What is DynamoDB TTL?](#29-what-is-dynamodb-ttl)
  - [30: What is DAX and how is it different from ElastiCache?](#30-what-is-dax-and-how-is-it-different-from-elasticache)
  - [31: How do batch operations work in DynamoDB?](#31-how-do-batch-operations-work-in-dynamodb)
  - [32: How does pagination work in DynamoDB?](#32-how-does-pagination-work-in-dynamodb)
  - [33: What are the main S3 storage classes?](#33-what-are-the-main-s3-storage-classes)
  - [34: How do you upload large files to S3?](#34-how-do-you-upload-large-files-to-s3)
  - [35: How can you react to new objects in S3?](#35-how-can-you-react-to-new-objects-in-s3)
  - [36: What are S3 versioning and lifecycle rules?](#36-what-are-s3-versioning-and-lifecycle-rules)
  - [37: What is the difference between SQS Standard and FIFO queues?](#37-what-is-the-difference-between-sqs-standard-and-fifo-queues)
  - [38: What are the key SQS settings and how do you send and receive messages?](#38-what-are-the-key-sqs-settings-and-how-do-you-send-and-receive-messages)
  - [39: How do dead-letter queues work in SQS?](#39-how-do-dead-letter-queues-work-in-sqs)
  - [40: What is SNS and what is the fan-out pattern?](#40-what-is-sns-and-what-is-the-fan-out-pattern)
  - [41: What is Amazon EventBridge?](#41-what-is-amazon-eventbridge)
  - [42: What is Kinesis Data Streams and how is it different from SQS?](#42-what-is-kinesis-data-streams-and-how-is-it-different-from-sqs)
  - [43: What is Amazon Data Firehose?](#43-what-is-amazon-data-firehose)
  - [44: What is AWS Step Functions?](#44-what-is-aws-step-functions)
  - [45: What caching strategies do you use with ElastiCache?](#45-what-caching-strategies-do-you-use-with-elasticache)
  - [46: What is AWS AppSync?](#46-what-is-aws-appsync)
  - [47: What are paginators and waiters in the AWS SDKs?](#47-what-are-paginators-and-waiters-in-the-aws-sdks)
  - [48: What does idempotency mean and how do you make a Lambda function idempotent?](#48-what-does-idempotency-mean-and-how-do-you-make-a-lambda-function-idempotent)
  - [49: Which SDK versions should you use today?](#49-which-sdk-versions-should-you-use-today)
  - [50: How do you choose between SQS, SNS, EventBridge and Kinesis?](#50-how-do-you-choose-between-sqs-sns-eventbridge-and-kinesis)
- [Domain 2: Security](#domain-2-security)
  - [51: What is the difference between IAM users, groups, roles and policies?](#51-what-is-the-difference-between-iam-users-groups-roles-and-policies)
  - [52: What does an IAM policy look like?](#52-what-does-an-iam-policy-look-like)
  - [53: What is the difference between identity-based and resource-based policies?](#53-what-is-the-difference-between-identity-based-and-resource-based-policies)
  - [54: How does AWS evaluate policies?](#54-how-does-aws-evaluate-policies)
  - [55: How does assuming an IAM role work?](#55-how-does-assuming-an-iam-role-work)
  - [56: How do you give an application in account A access to resources in account B?](#56-how-do-you-give-an-application-in-account-a-access-to-resources-in-account-b)
  - [57: How does the AWS SDK find credentials?](#57-how-does-the-aws-sdk-find-credentials)
  - [58: How does an EC2 instance get AWS credentials, and what is IMDSv2?](#58-how-does-an-ec2-instance-get-aws-credentials-and-what-is-imdsv2)
  - [59: What is the difference between an ECS task role and a task execution role?](#59-what-is-the-difference-between-an-ecs-task-role-and-a-task-execution-role)
  - [60: What is the difference between a Lambda execution role and a Lambda resource-based policy?](#60-what-is-the-difference-between-a-lambda-execution-role-and-a-lambda-resource-based-policy)
  - [61: What is a permissions boundary?](#61-what-is-a-permissions-boundary)
  - [62: How do you apply least privilege in practice?](#62-how-do-you-apply-least-privilege-in-practice)
  - [63: What are IAM condition keys and policy variables? Give examples.](#63-what-are-iam-condition-keys-and-policy-variables-give-examples)
  - [64: What is the difference between Cognito user pools and identity pools?](#64-what-is-the-difference-between-cognito-user-pools-and-identity-pools)
  - [65: What tokens does a Cognito user pool return, and how do you validate them?](#65-what-tokens-does-a-cognito-user-pool-return-and-how-do-you-validate-them)
  - [66: How do users sign in with Cognito using OAuth 2.0?](#66-how-do-users-sign-in-with-cognito-using-oauth-20)
  - [67: What authorization options does API Gateway support?](#67-what-authorization-options-does-api-gateway-support)
  - [68: How does a Lambda authorizer work?](#68-how-does-a-lambda-authorizer-work)
  - [69: How do you protect an HTTP API with a Cognito JWT authorizer?](#69-how-do-you-protect-an-http-api-with-a-cognito-jwt-authorizer)
  - [70: How do clients call an API protected with IAM authorization?](#70-how-do-clients-call-an-api-protected-with-iam-authorization)
  - [71: What is AWS KMS and what types of keys are there?](#71-what-is-aws-kms-and-what-types-of-keys-are-there)
  - [72: What is envelope encryption?](#72-what-is-envelope-encryption)
  - [73: What KMS limits and errors should you know as a developer?](#73-what-kms-limits-and-errors-should-you-know-as-a-developer)
  - [74: What are KMS key policies and grants?](#74-what-are-kms-key-policies-and-grants)
  - [75: How does KMS key rotation work?](#75-how-does-kms-key-rotation-work)
  - [76: What encryption options exist for S3 objects?](#76-what-encryption-options-exist-for-s3-objects)
  - [77: How do you force encryption and HTTPS for an S3 bucket?](#77-how-do-you-force-encryption-and-https-for-an-s3-bucket)
  - [78: What is an S3 presigned URL and how do you create one?](#78-what-is-an-s3-presigned-url-and-how-do-you-create-one)
  - [79: What are S3 Block Public Access and Object Ownership?](#79-what-are-s3-block-public-access-and-object-ownership)
  - [80: How do you configure CORS on an S3 bucket?](#80-how-do-you-configure-cors-on-an-s3-bucket)
  - [81: What is the difference between Secrets Manager and SSM Parameter Store?](#81-what-is-the-difference-between-secrets-manager-and-ssm-parameter-store)
  - [82: How do you read a secret from Secrets Manager in code?](#82-how-do-you-read-a-secret-from-secrets-manager-in-code)
  - [83: How does secret rotation work in Secrets Manager?](#83-how-does-secret-rotation-work-in-secrets-manager)
  - [84: How do you use Parameter Store hierarchies?](#84-how-do-you-use-parameter-store-hierarchies)
  - [85: How are Lambda environment variables encrypted?](#85-how-are-lambda-environment-variables-encrypted)
  - [86: How do you handle encryption in transit?](#86-how-do-you-handle-encryption-in-transit)
  - [87: How do you let a Lambda function access resources in a private VPC?](#87-how-do-you-let-a-lambda-function-access-resources-in-a-private-vpc)
  - [88: What is the difference between gateway and interface VPC endpoints?](#88-what-is-the-difference-between-gateway-and-interface-vpc-endpoints)
  - [89: What is the difference between security groups and network ACLs?](#89-what-is-the-difference-between-security-groups-and-network-acls)
  - [90: How can you restrict users to only their own items in DynamoDB?](#90-how-can-you-restrict-users-to-only-their-own-items-in-dynamodb)
  - [91: How do you let GitHub Actions (or any CI system) deploy to AWS without access keys?](#91-how-do-you-let-github-actions-or-any-ci-system-deploy-to-aws-without-access-keys)
  - [92: How do developers get CLI credentials with IAM Identity Center?](#92-how-do-developers-get-cli-credentials-with-iam-identity-center)
  - [93: What are STS temporary credentials and how do MFA-protected API calls work?](#93-what-are-sts-temporary-credentials-and-how-do-mfa-protected-api-calls-work)
  - [94: How do you audit who did what in an AWS account?](#94-how-do-you-audit-who-did-what-in-an-aws-account)
  - [95: How do you keep sensitive data out of logs?](#95-how-do-you-keep-sensitive-data-out-of-logs)
  - [96: How do you protect a public API from abuse?](#96-how-do-you-protect-a-public-api-from-abuse)
  - [97: How do you serve private S3 content through CloudFront?](#97-how-do-you-serve-private-s3-content-through-cloudfront)
  - [98: What is the difference between CloudFront signed URLs, signed cookies and S3 presigned URLs?](#98-what-is-the-difference-between-cloudfront-signed-urls-signed-cookies-and-s3-presigned-urls)
  - [99: How is data encrypted at rest in common serverless services?](#99-how-is-data-encrypted-at-rest-in-common-serverless-services)
  - [100: An access key was committed to a public Git repository. What do you do?](#100-an-access-key-was-committed-to-a-public-git-repository-what-do-you-do)
- [Domain 3: Deployment](#domain-3-deployment)
  - [101: What is AWS SAM?](#101-what-is-aws-sam)
  - [102: What are the main SAM CLI commands?](#102-what-are-the-main-sam-cli-commands)
  - [103: What are SAM policy templates and Globals?](#103-what-are-sam-policy-templates-and-globals)
  - [104: What are the sections of a CloudFormation template?](#104-what-are-the-sections-of-a-cloudformation-template)
  - [105: What are the most used CloudFormation intrinsic functions?](#105-what-are-the-most-used-cloudformation-intrinsic-functions)
  - [106: How do Parameters, Mappings and Conditions work together?](#106-how-do-parameters-mappings-and-conditions-work-together)
  - [107: How do you share values between stacks?](#107-how-do-you-share-values-between-stacks)
  - [108: What are change sets and drift detection?](#108-what-are-change-sets-and-drift-detection)
  - [109: What are DeletionPolicy and UpdateReplacePolicy?](#109-what-are-deletionpolicy-and-updatereplacepolicy)
  - [110: What happens when a CloudFormation deployment fails?](#110-what-happens-when-a-cloudformation-deployment-fails)
  - [111: What is a CloudFormation custom resource?](#111-what-is-a-cloudformation-custom-resource)
  - [112: What are CloudFormation StackSets?](#112-what-are-cloudformation-stacksets)
  - [113: What is the AWS CDK?](#113-what-is-the-aws-cdk)
  - [114: What are the main CDK CLI commands?](#114-what-are-the-main-cdk-cli-commands)
  - [115: What are Lambda versions and aliases?](#115-what-are-lambda-versions-and-aliases)
  - [116: How do you shift traffic gradually between Lambda versions?](#116-how-do-you-shift-traffic-gradually-between-lambda-versions)
  - [117: What deployment configurations does CodeDeploy have for Lambda?](#117-what-deployment-configurations-does-codedeploy-have-for-lambda)
  - [118: How does CodeDeploy work with EC2 and on-premises servers?](#118-how-does-codedeploy-work-with-ec2-and-on-premises-servers)
  - [119: How do you do blue/green deployments for ECS?](#119-how-do-you-do-bluegreen-deployments-for-ecs)
  - [120: What deployment strategies should you know?](#120-what-deployment-strategies-should-you-know)
  - [121: What is AWS Elastic Beanstalk?](#121-what-is-aws-elastic-beanstalk)
  - [122: What deployment policies does Elastic Beanstalk support?](#122-what-deployment-policies-does-elastic-beanstalk-support)
  - [123: How do you customize an Elastic Beanstalk environment?](#123-how-do-you-customize-an-elastic-beanstalk-environment)
  - [124: What is an Elastic Beanstalk worker environment?](#124-what-is-an-elastic-beanstalk-worker-environment)
  - [125: What is AWS CodeBuild and what does a buildspec look like?](#125-what-is-aws-codebuild-and-what-does-a-buildspec-look-like)
  - [126: How do you speed up and secure CodeBuild builds?](#126-how-do-you-speed-up-and-secure-codebuild-builds)
  - [127: What is AWS CodePipeline?](#127-what-is-aws-codepipeline)
  - [128: How do you connect a pipeline to GitHub, GitLab or Bitbucket?](#128-how-do-you-connect-a-pipeline-to-github-gitlab-or-bitbucket)
  - [129: What is AWS CodeArtifact?](#129-what-is-aws-codeartifact)
  - [130: How do you push images to Amazon ECR?](#130-how-do-you-push-images-to-amazon-ecr)
  - [131: What are the main Amazon ECS concepts?](#131-what-are-the-main-amazon-ecs-concepts)
  - [132: When would you choose containers on ECS/Fargate over Lambda?](#132-when-would-you-choose-containers-on-ecsfargate-over-lambda)
  - [133: How do API Gateway deployments and canary releases work?](#133-how-do-api-gateway-deployments-and-canary-releases-work)
  - [134: How do you manage dev, test and prod environments?](#134-how-do-you-manage-dev-test-and-prod-environments)
  - [135: What is AWS AppConfig and how do you use feature flags?](#135-what-is-aws-appconfig-and-how-do-you-use-feature-flags)
  - [136: What is AWS Amplify?](#136-what-is-aws-amplify)
  - [137: How do you package Lambda functions with dependencies?](#137-how-do-you-package-lambda-functions-with-dependencies)
  - [138: How do you test serverless applications?](#138-how-do-you-test-serverless-applications)
  - [139: How do you add tests and approvals to a pipeline?](#139-how-do-you-add-tests-and-approvals-to-a-pipeline)
  - [140: How do you roll back a failed deployment automatically?](#140-how-do-you-roll-back-a-failed-deployment-automatically)
  - [141: What is CloudFormation Git sync?](#141-what-is-cloudformation-git-sync)
  - [142: How do you bootstrap software on EC2 with CloudFormation?](#142-how-do-you-bootstrap-software-on-ec2-with-cloudformation)
  - [143: What are CloudFormation dynamic references?](#143-what-are-cloudformation-dynamic-references)
  - [144: How do you deploy across multiple accounts with CodePipeline?](#144-how-do-you-deploy-across-multiple-accounts-with-codepipeline)
  - [145: How do you deploy a static website on S3 and CloudFront?](#145-how-do-you-deploy-a-static-website-on-s3-and-cloudfront)
  - [146: What do aws cloudformation package and sam package do?](#146-what-do-aws-cloudformation-package-and-sam-package-do)
  - [147: How do you protect production stacks from accidental changes?](#147-how-do-you-protect-production-stacks-from-accidental-changes)
  - [148: How do you deal with Lambda runtime deprecations and updates?](#148-how-do-you-deal-with-lambda-runtime-deprecations-and-updates)
  - [149: What gets frozen when you publish a Lambda version?](#149-what-gets-frozen-when-you-publish-a-lambda-version)
  - [150: Describe a CI/CD flow for a serverless application.](#150-describe-a-cicd-flow-for-a-serverless-application)
- [Domain 4: Troubleshooting and Optimization](#domain-4-troubleshooting-and-optimization)
  - [151: What are the main parts of Amazon CloudWatch?](#151-what-are-the-main-parts-of-amazon-cloudwatch)
  - [152: How do you publish a custom metric?](#152-how-do-you-publish-a-custom-metric)
  - [153: What is the CloudWatch Embedded Metric Format (EMF)?](#153-what-is-the-cloudwatch-embedded-metric-format-emf)
  - [154: How do you search logs with CloudWatch Logs Insights?](#154-how-do-you-search-logs-with-cloudwatch-logs-insights)
  - [155: What is a metric filter?](#155-what-is-a-metric-filter)
  - [156: How do CloudWatch alarms work?](#156-how-do-cloudwatch-alarms-work)
  - [157: How should you log from Lambda?](#157-how-should-you-log-from-lambda)
  - [158: What is AWS X-Ray and what are its main concepts?](#158-what-is-aws-x-ray-and-what-are-its-main-concepts)
  - [159: What is the difference between annotations and metadata in X-Ray?](#159-what-is-the-difference-between-annotations-and-metadata-in-x-ray)
  - [160: How do you enable tracing in Lambda, API Gateway and containers?](#160-how-do-you-enable-tracing-in-lambda-api-gateway-and-containers)
  - [161: When do you use CloudWatch, X-Ray and CloudTrail?](#161-when-do-you-use-cloudwatch-x-ray-and-cloudtrail)
  - [162: What is CloudWatch Application Signals?](#162-what-is-cloudwatch-application-signals)
  - [163: What causes Lambda cold starts and how can you reduce them?](#163-what-causes-lambda-cold-starts-and-how-can-you-reduce-them)
  - [164: What is the difference between reserved concurrency and provisioned concurrency?](#164-what-is-the-difference-between-reserved-concurrency-and-provisioned-concurrency)
  - [165: What is Lambda SnapStart?](#165-what-is-lambda-snapstart)
  - [166: How do you choose the right memory size for a Lambda function?](#166-how-do-you-choose-the-right-memory-size-for-a-lambda-function)
  - [167: A Lambda function returns TooManyRequestsException (429). What is happening?](#167-a-lambda-function-returns-toomanyrequestsexception-429-what-is-happening)
  - [168: A Lambda function times out. How do you troubleshoot it?](#168-a-lambda-function-times-out-how-do-you-troubleshoot-it)
  - [169: How do you read a Lambda REPORT log line?](#169-how-do-you-read-a-lambda-report-log-line)
  - [170: A Lambda function in a VPC cannot reach S3 or an external API. Why?](#170-a-lambda-function-in-a-vpc-cannot-reach-s3-or-an-external-api-why)
  - [171: What is Lambda Insights?](#171-what-is-lambda-insights)
  - [172: Messages in an SQS queue processed by Lambda are processed more than once. Why?](#172-messages-in-an-sqs-queue-processed-by-lambda-are-processed-more-than-once-why)
  - [173: A Lambda function reading from Kinesis or DynamoDB Streams is falling behind. How do you fix it?](#173-a-lambda-function-reading-from-kinesis-or-dynamodb-streams-is-falling-behind-how-do-you-fix-it)
  - [174: What is exponential backoff with jitter and how do SDK retries work?](#174-what-is-exponential-backoff-with-jitter-and-how-do-sdk-retries-work)
  - [175: DynamoDB returns ProvisionedThroughputExceededException. What do you do?](#175-dynamodb-returns-provisionedthroughputexceededexception-what-do-you-do)
  - [176: How do you make DynamoDB reads faster and cheaper?](#176-how-do-you-make-dynamodb-reads-faster-and-cheaper)
  - [177: When is DAX not a good fit?](#177-when-is-dax-not-a-good-fit)
  - [178: What do common API Gateway error codes mean?](#178-what-do-common-api-gateway-error-codes-mean)
  - [179: What is the API Gateway integration timeout and can it be changed?](#179-what-is-the-api-gateway-integration-timeout-and-can-it-be-changed)
  - [180: How does API Gateway caching work?](#180-how-does-api-gateway-caching-work)
  - [181: How does throttling work in API Gateway?](#181-how-does-throttling-work-in-api-gateway)
  - [182: How do you make CloudFront caching work well?](#182-how-do-you-make-cloudfront-caching-work-well)
  - [183: How do you improve S3 performance?](#183-how-do-you-improve-s3-performance)
  - [184: Your code gets AccessDenied from S3. What do you check?](#184-your-code-gets-accessdenied-from-s3-what-do-you-check)
  - [185: How can you read only part of the data in a large S3 object?](#185-how-can-you-read-only-part-of-the-data-in-a-large-s3-object)
  - [186: An ElastiCache cache is not helping performance. What do you look at?](#186-an-elasticache-cache-is-not-helping-performance-what-do-you-look-at)
  - [187: How do you troubleshoot an SQS-based system where messages pile up?](#187-how-do-you-troubleshoot-an-sqs-based-system-where-messages-pile-up)
  - [188: How do you debug a failed Step Functions execution?](#188-how-do-you-debug-a-failed-step-functions-execution)
  - [189: A CloudFormation stack update fails. How do you find the cause?](#189-a-cloudformation-stack-update-fails-how-do-you-find-the-cause)
  - [190: A CodeDeploy deployment to EC2 fails. What do you check?](#190-a-codedeploy-deployment-to-ec2-fails-what-do-you-check)
  - [191: A CodeBuild build fails. How do you troubleshoot?](#191-a-codebuild-build-fails-how-do-you-troubleshoot)
  - [192: An ECS task keeps stopping or never starts. How do you troubleshoot?](#192-an-ecs-task-keeps-stopping-or-never-starts-how-do-you-troubleshoot)
  - [193: An Application Load Balancer returns 5xx errors. How do you tell where they come from?](#193-an-application-load-balancer-returns-5xx-errors-how-do-you-tell-where-they-come-from)
  - [194: How do you follow a single request across many services?](#194-how-do-you-follow-a-single-request-across-many-services)
  - [195: Lambda functions exhaust the database connection limit. How do you fix it?](#195-lambda-functions-exhaust-the-database-connection-limit-how-do-you-fix-it)
  - [196: How can a developer lower the cost of a serverless application?](#196-how-can-a-developer-lower-the-cost-of-a-serverless-application)
  - [197: What are CloudWatch Synthetics canaries?](#197-what-are-cloudwatch-synthetics-canaries)
  - [198: What is Lambda recursive loop detection?](#198-what-is-lambda-recursive-loop-detection)
  - [199: How do you debug Lambda functions locally and in the cloud?](#199-how-do-you-debug-lambda-functions-locally-and-in-the-cloud)
  - [200: What are good practices for using the AWS SDKs efficiently?](#200-what-are-good-practices-for-using-the-aws-sdks-efficiently)

---

# Domain 1: Development with AWS Services

## 1: What is AWS Lambda and when would you use it?

Lambda is a compute service that runs your code in response to events without you managing servers. You upload code (a zip file or a container image), pick a runtime, and AWS runs it when something triggers it: an HTTP request through API Gateway, a new object in S3, a message in SQS, a schedule, and so on.

Use it when:

- The work is event-driven and short (up to 15 minutes per invocation).
- Traffic is spiky or unpredictable, so paying per request and per millisecond is cheaper than running servers all day.
- You want AWS to handle scaling, patching and availability.

It is a poor fit for long-running processes, workloads that need a persistent local state, or jobs that need special hardware like GPUs. For those, look at ECS, Fargate, EC2 or AWS Batch.

## 2: What are the three ways Lambda can be invoked?

1. **Synchronous**: the caller waits for the result. Examples: API Gateway, function URLs, `aws lambda invoke` with the default `RequestResponse` type, Cognito triggers. If the function fails, the caller gets the error and decides whether to retry.
2. **Asynchronous**: the caller hands the event to Lambda and gets a `202` right away. Lambda puts the event in an internal queue and processes it. Examples: S3 notifications, SNS, EventBridge. Lambda retries failed async invocations (up to 2 times by default) and can send failures to a dead-letter queue or an on-failure destination.
3. **Event source mapping (polling)**: Lambda itself polls a source and invokes your function with batches of records. Examples: SQS, Kinesis Data Streams, DynamoDB Streams, Amazon MSK, self-managed Kafka, Amazon MQ, DocumentDB. Retry behavior depends on the source.

```bash
# Synchronous
aws lambda invoke --function-name orders-api \
  --cli-binary-format raw-in-base64-out \
  --payload '{"orderId":"o-1"}' response.json

# Asynchronous
aws lambda invoke --function-name orders-api \
  --invocation-type Event \
  --cli-binary-format raw-in-base64-out \
  --payload '{"orderId":"o-1"}' response.json
```

## 3: What does a Lambda handler look like in Python and Node.js?

The handler is the function Lambda calls for each event. It gets the event and a context object.

Python:

```python
import json

def lambda_handler(event, context):
    print(f"Request ID: {context.aws_request_id}")
    print(f"Time left (ms): {context.get_remaining_time_in_millis()}")

    body = json.loads(event.get("body") or "{}")
    return {
        "statusCode": 200,
        "headers": {"Content-Type": "application/json"},
        "body": json.dumps({"received": body}),
    }
```

Node.js 22 (ES modules, file named `index.mjs`, handler `index.handler`):

```javascript
export const handler = async (event, context) => {
  console.log("Request ID:", context.awsRequestId);

  const body = JSON.parse(event.body ?? "{}");
  return {
    statusCode: 200,
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ received: body }),
  };
};
```

In Node.js, use `async` handlers. Callback-based handlers are not supported starting with the Node.js 24 runtime, so new code should not use them.

## 4: Why should you create SDK clients and database connections outside the handler?

Code outside the handler runs once per execution environment, during the init phase. Lambda reuses the same environment for later invocations (warm starts), so anything you create there is reused too.

```python
import os
import boto3

# Runs once per execution environment
dynamodb = boto3.resource("dynamodb")
table = dynamodb.Table(os.environ["TABLE_NAME"])

def lambda_handler(event, context):
    # Runs on every invocation
    return table.get_item(Key={"pk": event["id"]}).get("Item")
```

This saves time on every warm invocation, because creating clients, loading config and opening TCP/TLS connections is slow. Do not store request-specific data (like the current user) in global variables, because the next request in the same environment will see it.

## 5: What are the main Lambda limits a developer should know?

| Setting                                    | Limit                                                            |
| ------------------------------------------ | ---------------------------------------------------------------- |
| Memory                                     | 128 MB to 10,240 MB (CPU scales with memory)                     |
| Timeout                                    | Up to 900 seconds (15 minutes)                                   |
| `/tmp` ephemeral storage                   | 512 MB to 10,240 MB                                              |
| Synchronous payload (request and response) | 6 MB each                                                        |
| Asynchronous payload                       | 1 MB (raised from 256 KB in late 2025)                           |
| Zip package                                | 50 MB zipped for direct upload, 250 MB unzipped including layers |
| Container image                            | 10 GB                                                            |
| Layers per function                        | 5                                                                |
| Environment variables                      | 4 KB total                                                       |
| Concurrent executions                      | 1,000 per Region by default (soft limit, can be raised)          |

When a payload is too large, the usual fix is to put the data in S3 and pass a reference (bucket and key) in the event.

## 6: What are Lambda layers?

A layer is a zip archive with libraries, custom runtimes or other files that you can attach to many functions. Lambda extracts layer content into `/opt`. For Python, files under `python/` in the layer end up on the import path; for Node.js, files under `nodejs/node_modules`.

```bash
mkdir -p layer/python
pip install requests -t layer/python
cd layer && zip -r ../requests-layer.zip . && cd ..

aws lambda publish-layer-version \
  --layer-name requests \
  --zip-file fileb://requests-layer.zip \
  --compatible-runtimes python3.13 \
  --compatible-architectures arm64

aws lambda update-function-configuration \
  --function-name orders-api \
  --layers arn:aws:lambda:us-east-1:111122223333:layer:requests:1
```

Notes:

- Layer versions are immutable. A new upload creates a new version number.
- Max 5 layers per function, and the total unzipped size still counts toward the 250 MB limit.
- Container image functions do not use layers. You copy the files into the image instead.

## 7: How do you pass configuration to a Lambda function?

Common options:

- **Environment variables** for simple, non-secret settings such as table names or log level.
- **SSM Parameter Store** for shared config and **Secrets Manager** for secrets such as database passwords or API keys.
- **AWS AppConfig** for config that changes at runtime, like feature flags.

```python
import os

TABLE_NAME = os.environ["TABLE_NAME"]
LOG_LEVEL = os.environ.get("LOG_LEVEL", "INFO")
```

For parameters and secrets, the **AWS Parameters and Secrets Lambda Extension** gives you a local HTTP cache, so you do not call the API on every invocation:

```python
import os
import json
import urllib.request

def get_secret(secret_id):
    url = f"http://localhost:2773/secretsmanager/get?secretId={secret_id}"
    req = urllib.request.Request(url)
    req.add_header("X-Aws-Parameters-Secrets-Token", os.environ["AWS_SESSION_TOKEN"])
    with urllib.request.urlopen(req) as resp:
        return json.loads(json.loads(resp.read())["SecretString"])
```

## 8: What is the Lambda execution environment lifecycle?

Each execution environment goes through three phases:

1. **Init**: Lambda downloads your code, starts the runtime and extensions, and runs code outside the handler. This is the "cold start". It is limited to 10 seconds for on-demand functions before Lambda retries init on the first invoke.
2. **Invoke**: Lambda calls your handler. After it returns, the environment is frozen and may be reused for the next event.
3. **Shutdown**: when Lambda decides to retire the environment, extensions get a shutdown event and then the environment is removed.

One environment handles one request at a time. If 50 requests arrive at once, Lambda creates up to 50 environments. Since August 2025, the init phase is billed for on-demand functions too, so heavy init code costs money as well as latency.

## 9: What is the difference between Lambda destinations and a dead-letter queue?

Both handle asynchronous invocations (and destinations also work with some event source mappings) that failed after all retries.

|            | Dead-letter queue       | Destinations                                                         |
| ---------- | ----------------------- | -------------------------------------------------------------------- |
| Targets    | SQS or SNS              | SQS, SNS, Lambda, EventBridge, and S3 (for failures)                 |
| On success | Not supported           | Supported                                                            |
| Data sent  | Only the original event | Event plus details: error message, stack trace, request ID, response |

Destinations are the newer and more useful option. AWS recommends them over DLQs for new code.

```bash
aws lambda put-function-event-invoke-config \
  --function-name process-order \
  --maximum-retry-attempts 1 \
  --maximum-event-age-in-seconds 3600 \
  --destination-config '{
    "OnSuccess": {"Destination": "arn:aws:sqs:us-east-1:111122223333:orders-done"},
    "OnFailure": {"Destination": "arn:aws:sqs:us-east-1:111122223333:orders-failed"}
  }'
```

## 10: How does Lambda retry asynchronous invocations?

- Default is 2 retries (3 attempts total). You can set it from 0 to 2.
- Lambda waits about 1 minute before the first retry and about 2 minutes before the second.
- Events are kept in the internal queue for up to 6 hours by default. You can lower this with "maximum event age" (60 seconds to 6 hours).
- If the function is throttled or the service returns a system error, Lambda keeps retrying with backoff until the maximum event age is reached.
- After all attempts fail, the event goes to the on-failure destination or DLQ if one is configured, otherwise it is dropped.

Because an event may be delivered more than once, async handlers should be idempotent.

## 11: How do you process SQS messages with Lambda and handle partial failures?

Create an event source mapping. Lambda polls the queue and calls your function with a batch (up to 10 messages for FIFO, up to 10,000 for standard queues with a batching window). If the function throws, the whole batch goes back to the queue. To retry only the failed messages, turn on `ReportBatchItemFailures` and return the IDs of the failed messages.

```python
import json

def lambda_handler(event, context):
    failures = []
    for record in event["Records"]:
        try:
            order = json.loads(record["body"])
            process_order(order)
        except Exception as exc:
            print(f"Failed {record['messageId']}: {exc}")
            failures.append({"itemIdentifier": record["messageId"]})

    return {"batchItemFailures": failures}
```

SAM config:

```yaml
Events:
  OrdersQueue:
    Type: SQS
    Properties:
      Queue: !GetAtt OrdersQueue.Arn
      BatchSize: 10
      FunctionResponseTypes:
        - ReportBatchItemFailures
```

Successful messages are deleted by Lambda. Failed ones become visible again after the visibility timeout and are moved to the DLQ after `maxReceiveCount` attempts.

## 12: What is a Lambda function URL?

A function URL is a dedicated HTTPS endpoint for a single function, in the form `https://<url-id>.lambda-url.<region>.on.aws`. It is a quick way to expose a function over HTTP without API Gateway.

- Auth type `AWS_IAM` requires SigV4 signed requests. Auth type `NONE` is public, but you still need a resource-based policy that allows `lambda:InvokeFunctionUrl`.
- Supports CORS settings.
- Supports response streaming (`InvokeMode: RESPONSE_STREAM`), which API Gateway does not do the same way.
- No usage plans, API keys, request validation, caching, or custom authorizers. If you need those, use API Gateway.

```bash
aws lambda create-function-url-config \
  --function-name report-generator \
  --auth-type AWS_IAM \
  --invoke-mode BUFFERED
```

## 13: How do you deploy a Lambda function as a container image?

Build an image based on an AWS Lambda base image (or any image that includes the Lambda Runtime Interface Client), push it to Amazon ECR, and create the function from the image.

```dockerfile
FROM public.ecr.aws/lambda/python:3.13

COPY requirements.txt ${LAMBDA_TASK_ROOT}
RUN pip install -r requirements.txt

COPY app.py ${LAMBDA_TASK_ROOT}

CMD ["app.lambda_handler"]
```

```bash
docker build --platform linux/arm64 -t image-resizer .
docker tag image-resizer:latest 111122223333.dkr.ecr.us-east-1.amazonaws.com/image-resizer:1.0.0
docker push 111122223333.dkr.ecr.us-east-1.amazonaws.com/image-resizer:1.0.0

aws lambda create-function \
  --function-name image-resizer \
  --package-type Image \
  --code ImageUri=111122223333.dkr.ecr.us-east-1.amazonaws.com/image-resizer:1.0.0 \
  --architectures arm64 \
  --role arn:aws:iam::111122223333:role/image-resizer-role
```

Use images when dependencies are larger than 250 MB, or when your team already builds and scans everything as containers. The image must be in ECR in the same account or a cross-account repo with the right permissions.

## 14: What are the differences between REST APIs, HTTP APIs and WebSocket APIs in API Gateway?

|                                       | REST API                                  | HTTP API                                          | WebSocket API                      |
| ------------------------------------- | ----------------------------------------- | ------------------------------------------------- | ---------------------------------- |
| Use case                              | Full-featured APIs                        | Simple, cheaper APIs for Lambda and HTTP backends | Two-way, real-time communication   |
| Cost                                  | Higher                                    | Lower                                             | Per message and connection minutes |
| Auth                                  | IAM, Cognito, Lambda authorizer, API keys | IAM, JWT (Cognito or any OIDC), Lambda authorizer | IAM, Lambda authorizer             |
| Usage plans and API keys              | Yes                                       | No                                                | No                                 |
| Request validation, mapping templates | Yes                                       | No (only parameter mapping)                       | Yes                                |
| Caching                               | Yes                                       | No                                                | No                                 |
| AWS WAF                               | Yes                                       | No                                                | No                                 |
| Private endpoints                     | Yes                                       | No                                                | No                                 |

A common rule: start with HTTP API for Lambda backends, switch to REST API if you need caching, WAF, usage plans, request validation, or private APIs.

## 15: What is the difference between proxy and non-proxy integrations?

- **Lambda proxy integration**: API Gateway sends the whole request (method, path, headers, query string, body) to Lambda as one event, and the function must return a response in a fixed format. It is simple and the most common choice.
- **Non-proxy (custom) integration**: you control the request and response with mapping templates. API Gateway can transform the data before it reaches the backend and after it comes back.

The Lambda proxy response must look like this, otherwise API Gateway returns `502 Bad Gateway`:

```javascript
export const handler = async (event) => {
  const id = event.pathParameters?.id;
  return {
    statusCode: 200,
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ id }), // body must be a string
    isBase64Encoded: false,
  };
};
```

## 16: What are mapping templates in API Gateway?

Mapping templates are written in Velocity Template Language (VTL) and used in REST API non-proxy integrations to change the request or response body. You can rename fields, add values, or call AWS services directly without a Lambda function.

Example: send a POST body straight to SQS without Lambda (integration request template for `application/json`):

```velocity
Action=SendMessage&MessageBody=$util.urlEncode($input.body)
```

Example: reshape the request for a Lambda backend:

```velocity
{
  "customerId": "$input.params('customerId')",
  "order": $input.json('$'),
  "sourceIp": "$context.identity.sourceIp"
}
```

Direct service integrations like this can save money and latency for simple tasks.

## 17: What are API Gateway stages and stage variables?

A **stage** is a named snapshot of a deployment, like `dev`, `test` or `prod`. Each stage has its own URL, settings (throttling, caching, logging) and can point to different backends.

**Stage variables** are key-value pairs attached to a stage. You can use them in integration URIs, for example to call a different Lambda alias per stage:

```
arn:aws:lambda:us-east-1:111122223333:function:orders-api:${stageVariables.lambdaAlias}
```

Set `lambdaAlias=dev` on the dev stage and `lambdaAlias=prod` on the prod stage. You also need to give API Gateway permission to invoke each alias.

## 18: What are usage plans and API keys?

Usage plans (REST APIs only) let you set throttling and quotas for clients. An API key identifies a client and is linked to one or more usage plans.

- Throttling: steady rate (requests per second) and burst.
- Quota: total requests per day, week or month.

The client sends the key in the `x-api-key` header. API keys are for metering and limiting, not for security. Use IAM, Cognito or a Lambda authorizer for authentication.

```bash
aws apigateway create-usage-plan \
  --name partner-basic \
  --throttle burstLimit=20,rateLimit=10 \
  --quota limit=10000,period=MONTH \
  --api-stages apiId=a1b2c3d4e5,stage=prod
```

## 19: How do you enable CORS for an API?

Browsers block cross-origin calls unless the server returns the right CORS headers. With API Gateway:

- **HTTP API**: configure CORS on the API (allowed origins, methods, headers). API Gateway answers the `OPTIONS` preflight for you.
- **REST API**: enable CORS on the resource, which creates an `OPTIONS` method with a mock integration. With **Lambda proxy integration**, your function must also return the CORS headers on the real responses.

```python
def lambda_handler(event, context):
    return {
        "statusCode": 200,
        "headers": {
            "Access-Control-Allow-Origin": "https://app.example.com",
            "Access-Control-Allow-Headers": "Content-Type,Authorization",
            "Access-Control-Allow-Methods": "GET,POST,OPTIONS",
        },
        "body": '{"ok": true}',
    }
```

Remember to redeploy the REST API stage after changing CORS settings.

## 20: What is Amazon DynamoDB and what kinds of primary keys does it support?

DynamoDB is a fully managed NoSQL key-value and document database with single-digit millisecond latency at any scale. Tables have no fixed schema except for the primary key.

Two types of primary key:

- **Partition key only (simple key)**: each item is identified by one attribute, for example `userId`. Must be unique.
- **Partition key + sort key (composite key)**: items with the same partition key are stored together and sorted by the sort key, for example `customerId` + `orderDate`. The combination must be unique.

The partition key value is hashed to decide which physical partition stores the item. Max item size is 400 KB.

## 21: How do you choose a good partition key?

Pick a key with many distinct values that are accessed fairly evenly, so traffic spreads across partitions.

- Good: `userId`, `orderId`, `deviceId`.
- Bad: `status` (few values like `ACTIVE`/`INACTIVE`), `date` for a write-heavy table (all writes for today hit one partition).

If one value is very hot, you can add a suffix (write sharding), for example `2026-10-23#7` where the suffix is a random number from 0 to 9, and then query all suffixes when reading.

Also design the key around your access patterns. In DynamoDB you model the queries first, then the table.

## 22: What is the difference between Query and Scan?

- **Query** finds items by partition key (and optionally a sort key condition). It reads only the matching items, so it is fast and cheap.
- **Scan** reads every item in the table or index and then filters. It is slow and expensive on large tables.

`FilterExpression` is applied after the read, so you still pay for all the items that were read.

```python
import boto3
from boto3.dynamodb.conditions import Key, Attr

table = boto3.resource("dynamodb").Table("Orders")

resp = table.query(
    KeyConditionExpression=Key("customerId").eq("c-123")
    & Key("orderDate").begins_with("2026-10"),
    FilterExpression=Attr("status").eq("SHIPPED"),
    ProjectionExpression="orderId, orderDate, total",
    ScanIndexForward=False,  # newest first
    Limit=20,
)
items = resp["Items"]
```

Note: the boto3 `resource` interface still works but AWS does not add new features to it. Using the `client` interface is also fine and is the only option for new APIs.

## 23: What is the difference between an LSI and a GSI?

|                | Local secondary index (LSI)                | Global secondary index (GSI) |
| -------------- | ------------------------------------------ | ---------------------------- |
| Partition key  | Same as the table                          | Any attribute                |
| Sort key       | Different from the table                   | Any attribute (optional)     |
| When to create | Only at table creation                     | Any time                     |
| Capacity       | Shares the table's capacity                | Has its own capacity         |
| Consistency    | Eventual or strong                         | Eventual only                |
| Limits         | 5 per table, 10 GB per partition key value | 20 per table by default      |

Example: an `Orders` table keyed by `customerId` + `orderDate`. A GSI on `status` + `orderDate` lets you query "all pending orders by date" across customers.

If writes to a GSI are throttled, writes to the main table are throttled too, so give GSIs enough capacity.

## 24: How do you calculate RCUs and WCUs?

- **1 RCU** = one strongly consistent read per second of an item up to 4 KB, or two eventually consistent reads per second. Transactional reads cost 2 RCUs per 4 KB.
- **1 WCU** = one write per second of an item up to 1 KB. Transactional writes cost 2 WCUs per 1 KB.

Always round the item size up to the next 4 KB (reads) or 1 KB (writes).

Examples:

- 10 strongly consistent reads/second of 6 KB items: 6 KB rounds to 8 KB = 2 units. 10 x 2 = **20 RCUs**.
- Same reads, eventually consistent: **10 RCUs**.
- 5 writes/second of 2.5 KB items: rounds to 3 KB = 3 units. 5 x 3 = **15 WCUs**.

## 25: What is the difference between on-demand and provisioned capacity?

- **On-demand**: you pay per request. No capacity planning. Good for new apps, unpredictable traffic, or tables that are idle most of the time. Since late 2024 on-demand is much cheaper than before, so it is the default choice for many workloads. You can set a maximum throughput to cap cost.
- **Provisioned**: you set RCUs and WCUs (optionally with auto scaling). Cheaper for steady, predictable traffic, and you can buy reserved capacity. Requests above the provisioned rate get throttled.

You can switch a table between modes (with some limits on how often).

## 26: How do conditional writes and optimistic locking work in DynamoDB?

A conditional write only succeeds if a condition on the existing item is true. If not, DynamoDB returns `ConditionalCheckFailedException` and nothing changes.

Optimistic locking uses a version number: read the item, then update only if the version is still the same.

```python
import boto3
from botocore.exceptions import ClientError

table = boto3.resource("dynamodb").Table("Products")

def update_price(product_id, new_price, expected_version):
    try:
        table.update_item(
            Key={"productId": product_id},
            UpdateExpression="SET price = :p, version = version + :one",
            ConditionExpression="version = :expected",
            ExpressionAttributeValues={
                ":p": new_price,
                ":one": 1,
                ":expected": expected_version,
            },
        )
    except ClientError as e:
        if e.response["Error"]["Code"] == "ConditionalCheckFailedException":
            raise RuntimeError("Item was changed by someone else, reload and retry")
        raise
```

Another common use: `ConditionExpression="attribute_not_exists(pk)"` to avoid overwriting an existing item on `PutItem`.

## 27: How do DynamoDB transactions work?

`TransactWriteItems` and `TransactGetItems` let you group up to 100 actions across one or more tables in the same account and Region. Either all succeed or none do.

```javascript
import { DynamoDBClient } from "@aws-sdk/client-dynamodb";
import {
  DynamoDBDocumentClient,
  TransactWriteCommand,
} from "@aws-sdk/lib-dynamodb";

const ddb = DynamoDBDocumentClient.from(new DynamoDBClient({}));

await ddb.send(
  new TransactWriteCommand({
    TransactItems: [
      {
        Update: {
          TableName: "Accounts",
          Key: { accountId: "A" },
          UpdateExpression: "SET balance = balance - :amt",
          ConditionExpression: "balance >= :amt",
          ExpressionAttributeValues: { ":amt": 100 },
        },
      },
      {
        Update: {
          TableName: "Accounts",
          Key: { accountId: "B" },
          UpdateExpression: "SET balance = balance + :amt",
          ExpressionAttributeValues: { ":amt": 100 },
        },
      },
    ],
    ClientRequestToken: "transfer-7f3a2c", // makes the call idempotent for 10 minutes
  }),
);
```

Transactions cost twice the normal capacity. If any condition fails, you get `TransactionCanceledException` with the reason for each item.

## 28: What are DynamoDB Streams?

A stream is an ordered log of item changes (insert, modify, remove) in a table, kept for 24 hours. You choose what each record contains: `KEYS_ONLY`, `NEW_IMAGE`, `OLD_IMAGE` or `NEW_AND_OLD_IMAGES`.

Common uses: trigger Lambda when data changes, replicate to another store, send notifications, or build audit logs.

```python
def lambda_handler(event, context):
    for record in event["Records"]:
        if record["eventName"] == "INSERT":
            new_item = record["dynamodb"]["NewImage"]
            send_welcome_email(new_item["email"]["S"])
```

Records for the same item are delivered in order. Lambda processes each shard in order and retries a failed batch until it succeeds or expires, so handle errors carefully (see the troubleshooting section). There is also the option to stream changes to Kinesis Data Streams instead, which gives longer retention and more consumers.

## 29: What is DynamoDB TTL?

Time to Live lets DynamoDB delete items automatically after a timestamp. You pick an attribute that holds the expiry time as a Unix epoch in **seconds**.

```python
import time

table.put_item(Item={
    "sessionId": "s-123",
    "userId": "u-1",
    "expiresAt": int(time.time()) + 3600,  # 1 hour
})
```

```bash
aws dynamodb update-time-to-live \
  --table-name Sessions \
  --time-to-live-specification "Enabled=true, AttributeName=expiresAt"
```

Deletes are free (no WCUs) but not instant. They usually happen within a few days of expiry, so filter out expired items in your queries if that matters. TTL deletes appear in DynamoDB Streams, which is useful for archiving.

## 30: What is DAX and how is it different from ElastiCache?

**DynamoDB Accelerator (DAX)** is an in-memory cache built for DynamoDB. It is API-compatible, so you swap the DynamoDB client for the DAX client and most code stays the same. Reads from cache return in microseconds.

- DAX caches `GetItem`/`BatchGetItem` results (item cache) and `Query`/`Scan` results (query cache).
- It is write-through for writes that go through DAX.
- It only gives eventually consistent reads. Strongly consistent reads go to DynamoDB.

**ElastiCache** (Valkey, Redis OSS or Memcached) is a general cache. You decide what to store and write the caching logic yourself. Use it when you cache data from many sources, store computed results, sessions, or leaderboards.

## 31: How do batch operations work in DynamoDB?

- `BatchGetItem`: up to 100 items or 16 MB per call.
- `BatchWriteItem`: up to 25 put or delete requests, up to 16 MB per call. No updates and no conditions.

Batch calls are not atomic. Some items can fail because of throttling, and they come back in `UnprocessedKeys` or `UnprocessedItems`. You must retry those with backoff.

```python
import time
import boto3

client = boto3.client("dynamodb")

def batch_write(requests):
    request_items = {"Orders": requests}
    delay = 0.1
    while request_items:
        resp = client.batch_write_item(RequestItems=request_items)
        request_items = resp.get("UnprocessedItems", {})
        if request_items:
            time.sleep(delay)
            delay = min(delay * 2, 5)
```

The boto3 `table.batch_writer()` helper handles batching and retries of unprocessed items for you.

## 32: How does pagination work in DynamoDB?

`Query` and `Scan` return at most 1 MB of data per call. If there is more, the response includes `LastEvaluatedKey`. You pass it as `ExclusiveStartKey` in the next call. When `LastEvaluatedKey` is missing, you are done.

The easiest way is to use SDK paginators:

```python
import boto3

client = boto3.client("dynamodb")
paginator = client.get_paginator("query")

for page in paginator.paginate(
    TableName="Orders",
    KeyConditionExpression="customerId = :c",
    ExpressionAttributeValues={":c": {"S": "c-123"}},
):
    for item in page["Items"]:
        print(item["orderId"]["S"])
```

For APIs that return pages to a browser, return `LastEvaluatedKey` (encoded, for example as base64) as a "next token" to the client.

## 33: What are the main S3 storage classes?

| Class                         | Use case                                                                       |
| ----------------------------- | ------------------------------------------------------------------------------ |
| S3 Standard                   | Frequently accessed data                                                       |
| S3 Intelligent-Tiering        | Unknown or changing access patterns, moves objects between tiers automatically |
| S3 Standard-IA                | Infrequent access, but needs fast retrieval                                    |
| S3 One Zone-IA                | Infrequent access, can be recreated, stored in one AZ                          |
| S3 Express One Zone           | Very low latency, single AZ, uses directory buckets                            |
| S3 Glacier Instant Retrieval  | Archive data that still needs millisecond access                               |
| S3 Glacier Flexible Retrieval | Archive, retrieval in minutes to hours                                         |
| S3 Glacier Deep Archive       | Long-term archive, retrieval in hours, cheapest                                |

Since December 2020, S3 gives strong read-after-write consistency for all PUT and DELETE operations, so a read right after a write always returns the latest data.

## 34: How do you upload large files to S3?

A single `PutObject` can upload up to 5 GB, but AWS recommends **multipart upload** for anything over about 100 MB. The file is split into parts (5 MiB to 5 GiB each, up to 10,000 parts) that upload in parallel and can be retried one by one.

The SDKs have high-level helpers that do this for you.

JavaScript SDK v3:

```javascript
import { S3Client } from "@aws-sdk/client-s3";
import { Upload } from "@aws-sdk/lib-storage";
import { createReadStream } from "node:fs";

const upload = new Upload({
  client: new S3Client({}),
  params: {
    Bucket: "my-backups",
    Key: "db/2026-10-23.dump",
    Body: createReadStream("./db.dump"),
  },
  partSize: 10 * 1024 * 1024, // 10 MB
  queueSize: 4, // parallel parts
});

upload.on("httpUploadProgress", (p) => console.log(p.loaded, "/", p.total));
await upload.done();
```

Python:

```python
import boto3
from boto3.s3.transfer import TransferConfig

config = TransferConfig(multipart_threshold=100 * 1024 * 1024, max_concurrency=8)
boto3.client("s3").upload_file("db.dump", "my-backups", "db/2026-10-23.dump", Config=config)
```

Add a lifecycle rule to abort incomplete multipart uploads, otherwise unfinished parts keep costing money.

## 35: How can you react to new objects in S3?

Two options:

1. **S3 event notifications**: send events like `s3:ObjectCreated:*` to Lambda, SQS or SNS. Simple, but limited filtering (prefix and suffix only).
2. **Amazon EventBridge**: turn on EventBridge for the bucket, and all events go to the default event bus. You get advanced filtering (object size, metadata, key patterns), many more targets, archive and replay.

```python
from urllib.parse import unquote_plus

def lambda_handler(event, context):
    for record in event["Records"]:
        bucket = record["s3"]["bucket"]["name"]
        key = unquote_plus(record["s3"]["object"]["key"])  # keys are URL-encoded
        print(f"New object: s3://{bucket}/{key}")
```

Be careful not to write output into the same bucket and prefix that triggers the function, or you get an infinite loop.

## 36: What are S3 versioning and lifecycle rules?

**Versioning** keeps every version of an object. A delete adds a "delete marker" instead of removing data, so you can restore old versions. Once enabled, versioning can only be suspended, not turned off.

**Lifecycle rules** move or delete objects automatically:

```json
{
  "Rules": [
    {
      "ID": "logs-retention",
      "Filter": { "Prefix": "logs/" },
      "Status": "Enabled",
      "Transitions": [
        { "Days": 30, "StorageClass": "STANDARD_IA" },
        { "Days": 90, "StorageClass": "GLACIER" }
      ],
      "Expiration": { "Days": 365 },
      "NoncurrentVersionExpiration": { "NoncurrentDays": 30 },
      "AbortIncompleteMultipartUpload": { "DaysAfterInitiation": 7 }
    }
  ]
}
```

```bash
aws s3api put-bucket-lifecycle-configuration \
  --bucket my-app-logs \
  --lifecycle-configuration file://lifecycle.json
```

## 37: What is the difference between SQS Standard and FIFO queues?

|            | Standard                            | FIFO                                                                                                     |
| ---------- | ----------------------------------- | -------------------------------------------------------------------------------------------------------- |
| Throughput | Nearly unlimited                    | 300 messages/s per API action without batching, 3,000 with batching, much more with high throughput mode |
| Delivery   | At least once (duplicates possible) | Exactly-once processing within a 5-minute deduplication window                                           |
| Order      | Best effort                         | Strict order within a message group                                                                      |
| Name       | Any                                 | Must end with `.fifo`                                                                                    |

FIFO queues need a `MessageGroupId`. Messages in the same group are processed in order, one at a time. Different groups can be processed in parallel, so use something like `customerId` as the group ID to get both order and parallelism.

```python
sqs.send_message(
    QueueUrl=fifo_url,
    MessageBody=json.dumps(event),
    MessageGroupId=f"customer-{customer_id}",
    MessageDeduplicationId=event["eventId"],  # or enable content-based deduplication
)
```

## 38: What are the key SQS settings and how do you send and receive messages?

- **Visibility timeout** (default 30 seconds, max 12 hours): after a consumer receives a message, it is hidden from others for this time. If not deleted in time, it becomes visible again.
- **Long polling** (`WaitTimeSeconds` up to 20): the call waits for messages instead of returning empty right away. Cheaper and fewer empty responses.
- **Delay queues** (`DelaySeconds` up to 15 minutes): hide new messages for a while.
- **Retention**: 1 minute to 14 days, default 4 days.
- **Max message size**: 1 MiB (raised from 256 KiB in 2025). For bigger payloads, store data in S3 and send a pointer, for example with the Extended Client Library.

```python
import json
import boto3

sqs = boto3.client("sqs")
url = sqs.get_queue_url(QueueName="orders")["QueueUrl"]

sqs.send_message(QueueUrl=url, MessageBody=json.dumps({"orderId": "o-1"}))

resp = sqs.receive_message(
    QueueUrl=url,
    MaxNumberOfMessages=10,
    WaitTimeSeconds=20,
    VisibilityTimeout=60,
)
for msg in resp.get("Messages", []):
    process(json.loads(msg["Body"]))
    sqs.delete_message(QueueUrl=url, ReceiptHandle=msg["ReceiptHandle"])
```

If processing takes longer than expected, call `ChangeMessageVisibility` to extend the timeout.

## 39: How do dead-letter queues work in SQS?

A DLQ is a normal queue that receives messages that failed too many times. You set a redrive policy on the source queue with `maxReceiveCount`. When a message is received that many times without being deleted, SQS moves it to the DLQ.

```bash
aws sqs set-queue-attributes \
  --queue-url https://sqs.us-east-1.amazonaws.com/111122223333/orders \
  --attributes '{
    "RedrivePolicy": "{\"deadLetterTargetArn\":\"arn:aws:sqs:us-east-1:111122223333:orders-dlq\",\"maxReceiveCount\":\"5\"}"
  }'
```

Rules:

- The DLQ must be the same type (a FIFO queue needs a FIFO DLQ) and in the same account and Region.
- Set the DLQ retention longer than the source queue's, because the original enqueue timestamp is kept for standard queues.
- After you fix the bug, use **DLQ redrive** (console or `StartMessageMoveTask` API) to send messages back to the source queue.
- Put an alarm on `ApproximateNumberOfMessagesVisible` of the DLQ.

## 40: What is SNS and what is the fan-out pattern?

Amazon SNS is a pub/sub service. Publishers send a message to a topic, and SNS pushes it to all subscribers: SQS, Lambda, HTTP/S endpoints, email, SMS, mobile push, or Firehose.

**Fan-out** means one SNS topic sends to several SQS queues, so different services each get their own copy and process it at their own pace.

```
           +--> SQS: billing-queue   --> billing service
Order  --> SNS topic --> SQS: shipping-queue --> shipping service
           +--> SQS: analytics-queue --> analytics
```

**Subscription filter policies** let a subscriber get only the messages it cares about:

```json
{
  "eventType": ["order_placed"],
  "amount": [{ "numeric": [">=", 100] }]
}
```

By default filters apply to message attributes. Set `FilterPolicyScope` to `MessageBody` to filter on the JSON body. SNS FIFO topics exist for ordered fan-out to SQS FIFO queues.

## 41: What is Amazon EventBridge?

EventBridge is a serverless event bus. Services and apps send events to a bus, and **rules** match events by pattern and route them to targets (Lambda, SQS, Step Functions, API destinations, other buses, and more).

Features: AWS service events on the default bus, custom buses, SaaS partner events, schema registry, archive and replay, EventBridge Pipes (point-to-point source to target with filtering and enrichment) and **EventBridge Scheduler** (cron and one-time schedules, the recommended replacement for scheduled rules).

Sending an event:

```python
import json
import boto3

events = boto3.client("events")
events.put_events(Entries=[{
    "EventBusName": "orders-bus",
    "Source": "com.example.orders",
    "DetailType": "OrderPlaced",
    "Detail": json.dumps({"orderId": "o-1", "total": 250, "country": "DE"}),
}])
```

Rule pattern that matches large orders from Germany:

```json
{
  "source": ["com.example.orders"],
  "detail-type": ["OrderPlaced"],
  "detail": {
    "country": ["DE"],
    "total": [{ "numeric": [">", 100] }]
  }
}
```

`PutEvents` can partly fail. Always check `FailedEntryCount` in the response.

## 42: What is Kinesis Data Streams and how is it different from SQS?

Kinesis Data Streams is for real-time streaming of large amounts of ordered data, like clickstreams, logs or IoT data.

|           | Kinesis Data Streams                                            | SQS                                                     |
| --------- | --------------------------------------------------------------- | ------------------------------------------------------- |
| Consumers | Many consumers read the same data                               | Each message is processed by one consumer, then deleted |
| Order     | Per shard (by partition key)                                    | Only in FIFO queues                                     |
| Replay    | Yes, data stays for the retention period (24 hours to 365 days) | No, deleted after processing                            |
| Scaling   | Shards (provisioned) or on-demand mode                          | Automatic                                               |

Each shard supports 1 MB/s or 1,000 records/s of writes, and 2 MB/s of reads shared by all standard consumers. **Enhanced fan-out** gives each registered consumer its own 2 MB/s per shard.

```python
import json
import boto3

kinesis = boto3.client("kinesis")
kinesis.put_record(
    StreamName="clickstream",
    Data=json.dumps({"userId": "u-1", "page": "/cart"}).encode(),
    PartitionKey="u-1",  # same key goes to the same shard, so order is kept per user
)
```

## 43: What is Amazon Data Firehose?

Amazon Data Firehose (formerly Kinesis Data Firehose) loads streaming data into destinations like S3, Redshift, OpenSearch, Splunk, Snowflake, Apache Iceberg tables, and HTTP endpoints. It is fully managed and scales automatically.

- It buffers data by size or time before delivery, so it is near real-time, not real-time.
- It can transform records with a Lambda function, convert JSON to Parquet or ORC, and compress data.
- Sources can be direct `PutRecord` calls, Kinesis Data Streams, MSK, CloudWatch Logs, and more.

Use Kinesis Data Streams when you need custom consumers and replay. Use Firehose when you just need to deliver data to storage or analytics with no code.

## 44: What is AWS Step Functions?

Step Functions orchestrates multiple steps (Lambda functions, AWS service calls, human approval, waits) as a state machine defined in Amazon States Language (JSON). It handles retries, error handling, parallel branches and state between steps.

|                     | Standard                           | Express                                      |
| ------------------- | ---------------------------------- | -------------------------------------------- |
| Max duration        | 1 year                             | 5 minutes                                    |
| Execution semantics | Exactly once                       | At least once (async) or at most once (sync) |
| Pricing             | Per state transition               | Per execution, duration and memory           |
| Use case            | Long, auditable business workflows | High-volume, short event processing          |

```json
{
  "Comment": "Process an order",
  "StartAt": "ChargeCard",
  "States": {
    "ChargeCard": {
      "Type": "Task",
      "Resource": "arn:aws:states:::lambda:invoke",
      "Arguments": {
        "FunctionName": "charge-card",
        "Payload": "{% $states.input %}"
      },
      "Retry": [
        {
          "ErrorEquals": ["States.TaskFailed"],
          "IntervalSeconds": 2,
          "MaxAttempts": 3,
          "BackoffRate": 2,
          "JitterStrategy": "FULL"
        }
      ],
      "Output": "{% $states.result.Payload %}",
      "Catch": [
        {
          "ErrorEquals": ["States.ALL"],
          "Next": "NotifyFailure"
        }
      ],
      "Next": "ShipOrder"
    },
    "ShipOrder": {
      "Type": "Task",
      "Resource": "arn:aws:states:::sqs:sendMessage",
      "Arguments": {
        "QueueUrl": "https://sqs.us-east-1.amazonaws.com/111122223333/shipping",
        "MessageBody": "{% $string($states.input) %}"
      },
      "End": true
    },
    "NotifyFailure": {
      "Type": "Fail",
      "Error": "OrderFailed"
    }
  },
  "QueryLanguage": "JSONata"
}
```

This example uses JSONata (added in late 2024). Older state machines use JSONPath with `Parameters`, `InputPath`, `ResultPath` and `OutputPath`. Both are supported. For workflows that live inside a single Lambda function, Lambda durable functions (announced at re:Invent 2025) are another option.

## 45: What caching strategies do you use with ElastiCache?

**Lazy loading (cache-aside)**: read from cache, on a miss read from the database and put it in the cache.

- Pros: only requested data is cached, cache failure is not fatal.
- Cons: a miss costs three trips, and data can be stale.

**Write-through**: update the cache every time you write to the database.

- Pros: cache is always fresh.
- Cons: every write is slower, and you cache data that may never be read.

Most apps combine both and add a **TTL** so stale data expires.

```python
import json
import os
import redis  # works with Valkey and Redis OSS

cache = redis.Redis(host=os.environ["CACHE_HOST"], port=6379, ssl=True)

def get_product(product_id):
    key = f"product:{product_id}"
    cached = cache.get(key)
    if cached:
        return json.loads(cached)

    product = db_get_product(product_id)            # cache miss
    cache.setex(key, 300, json.dumps(product))      # TTL 5 minutes
    return product

def update_product(product):
    db_save_product(product)
    cache.setex(f"product:{product['id']}", 300, json.dumps(product))  # write-through
```

ElastiCache now supports Valkey (an open source fork of Redis), Redis OSS and Memcached, in both node-based clusters and ElastiCache Serverless.

## 46: What is AWS AppSync?

AppSync is a managed GraphQL service (it also has AppSync Events for pub/sub over WebSockets). Clients send GraphQL queries, mutations and subscriptions. Resolvers connect fields to data sources such as DynamoDB, Lambda, RDS, OpenSearch, HTTP endpoints, or EventBridge.

Resolvers are written in JavaScript (`APPSYNC_JS` runtime), which replaced VTL as the recommended option:

```javascript
import { util } from "@aws-appsync/utils";

export function request(ctx) {
  return {
    operation: "GetItem",
    key: util.dynamodb.toMapValues({ id: ctx.args.id }),
  };
}

export function response(ctx) {
  return ctx.result;
}
```

Use AppSync when clients need flexible queries (fetch exactly the fields they need from many sources in one call) or real-time updates through subscriptions. Auth options include API key, IAM, Cognito user pools, OIDC and Lambda.

## 47: What are paginators and waiters in the AWS SDKs?

- **Paginators** loop through all pages of a list API for you (handling `NextToken`, `Marker`, `LastEvaluatedKey`, and so on).
- **Waiters** poll an API until a resource reaches a state, like "table exists" or "instance running".

JavaScript SDK v3:

```javascript
import {
  DynamoDBClient,
  CreateTableCommand,
  waitUntilTableExists,
} from "@aws-sdk/client-dynamodb";
import { S3Client, paginateListObjectsV2 } from "@aws-sdk/client-s3";

const ddb = new DynamoDBClient({});
await ddb.send(new CreateTableCommand({ /* ... */ TableName: "Orders" }));
await waitUntilTableExists(
  { client: ddb, maxWaitTime: 120 },
  { TableName: "Orders" },
);

const s3 = new S3Client({});
for await (const page of paginateListObjectsV2(
  { client: s3 },
  { Bucket: "my-bucket" },
)) {
  for (const obj of page.Contents ?? []) console.log(obj.Key);
}
```

Python:

```python
s3 = boto3.client("s3")
s3.create_bucket(Bucket="my-new-bucket")
s3.get_waiter("bucket_exists").wait(Bucket="my-new-bucket")

for page in s3.get_paginator("list_objects_v2").paginate(Bucket="my-bucket"):
    for obj in page.get("Contents", []):
        print(obj["Key"])
```

## 48: What does idempotency mean and how do you make a Lambda function idempotent?

An operation is idempotent when running it several times gives the same result as running it once. It matters because SQS, SNS, EventBridge, async Lambda and client retries can all deliver the same event more than once. Without idempotency, a customer might be charged twice.

Common approach: store a unique key for each request (for example an order ID or an `Idempotency-Key` header) with a conditional write. If the key already exists, return the saved result instead of doing the work again.

Powertools for AWS Lambda has a ready-made utility:

```python
from aws_lambda_powertools.utilities.idempotency import (
    DynamoDBPersistenceLayer,
    IdempotencyConfig,
    idempotent,
)

persistence = DynamoDBPersistenceLayer(table_name="IdempotencyTable")
config = IdempotencyConfig(event_key_jmespath="body.orderId", expires_after_seconds=3600)

@idempotent(persistence_store=persistence, config=config)
def lambda_handler(event, context):
    charge_customer(event)
    return {"statusCode": 200, "body": "charged"}
```

Many AWS APIs also take a client token (`ClientRequestToken`, `ClientToken`) for the same reason.

## 49: Which SDK versions should you use today?

- **JavaScript**: SDK v3 (`@aws-sdk/client-*`). It is modular, so you import only the clients you need, which makes Lambda bundles smaller. SDK v2 reached end of support in September 2025. The Node.js Lambda runtimes include SDK v3, not v2.
- **Python**: boto3 (current versions follow the supported Python versions; old Python releases get dropped over time).
- **Java**: SDK for Java 2.x. Version 1.x reached end of support at the end of 2025.
- **CLI**: AWS CLI v2.

SDK v3 uses a "client + command" style:

```javascript
import { S3Client, GetObjectCommand } from "@aws-sdk/client-s3";

const s3 = new S3Client({ region: "us-east-1" });
const resp = await s3.send(
  new GetObjectCommand({ Bucket: "my-bucket", Key: "a.json" }),
);
const text = await resp.Body.transformToString();
```

In Lambda, it is a good idea to bundle your own SDK version with your code (for example with esbuild) so that a runtime update does not change the SDK version under you.

## 50: How do you choose between SQS, SNS, EventBridge and Kinesis?

| Need                                                                              | Service                           |
| --------------------------------------------------------------------------------- | --------------------------------- |
| Decouple a producer from one consumer, buffer work, retry later                   | **SQS**                           |
| Push the same message to many subscribers quickly, including SMS, email, mobile   | **SNS** (often SNS + SQS fan-out) |
| Route events by content to many targets, integrate AWS and SaaS events, schedules | **EventBridge**                   |
| High-volume ordered stream, many consumers, replay of past data                   | **Kinesis Data Streams**          |
| Load streaming data into S3, Redshift, OpenSearch with no code                    | **Data Firehose**                 |
| Multi-step workflow with state, retries and branches                              | **Step Functions**                |

A typical event-driven setup: services publish domain events to EventBridge, rules route them to SQS queues owned by each consumer service, and each consumer uses Lambda with partial batch responses and a DLQ.

---

# Domain 2: Security

## 51: What is the difference between IAM users, groups, roles and policies?

- **User**: a long-term identity for one person or application, with a password and/or access keys.
- **Group**: a collection of users. Policies attached to the group apply to every user in it. Groups cannot be nested and cannot be used as a principal.
- **Role**: an identity with no long-term credentials. Someone or something (a user, an AWS service, another account, a federated user) assumes it and gets temporary credentials.
- **Policy**: a JSON document that allows or denies actions on resources.

Best practice today: people sign in through IAM Identity Center (or another identity provider) and use roles, and workloads use roles too. Avoid IAM users with long-term access keys where you can.

## 52: What does an IAM policy look like?

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "ReadWriteOrdersTable",
      "Effect": "Allow",
      "Action": [
        "dynamodb:GetItem",
        "dynamodb:PutItem",
        "dynamodb:UpdateItem",
        "dynamodb:Query"
      ],
      "Resource": [
        "arn:aws:dynamodb:us-east-1:111122223333:table/Orders",
        "arn:aws:dynamodb:us-east-1:111122223333:table/Orders/index/*"
      ]
    },
    {
      "Sid": "DenyOutsideRegion",
      "Effect": "Deny",
      "Action": "*",
      "Resource": "*",
      "Condition": {
        "StringNotEquals": { "aws:RequestedRegion": "us-east-1" }
      }
    }
  ]
}
```

Main elements:

- `Version`: always use `2012-10-17` (needed for policy variables).
- `Effect`: `Allow` or `Deny`.
- `Action`: API actions, like `s3:GetObject`. Wildcards are allowed.
- `Resource`: ARNs the statement applies to.
- `Condition`: optional rules (IP, tags, time, MFA, and so on).
- `Principal`: only in resource-based policies and trust policies.

## 53: What is the difference between identity-based and resource-based policies?

- **Identity-based policies** are attached to a user, group or role and say what that identity can do.
- **Resource-based policies** are attached to a resource (S3 bucket, SQS queue, SNS topic, Lambda function, KMS key, Secrets Manager secret, API Gateway API) and say who can access it. They include a `Principal`.

Example S3 bucket policy that lets another account read objects:

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Principal": { "AWS": "arn:aws:iam::444455556666:role/reporting" },
      "Action": "s3:GetObject",
      "Resource": "arn:aws:s3:::shared-reports/*"
    }
  ]
}
```

Within one account, an allow in either the identity policy or the resource policy is enough. For cross-account access, normally both sides must allow it (the resource policy in the owner account and the identity policy in the caller's account).

## 54: How does AWS evaluate policies?

In short:

1. By default everything is denied (implicit deny).
2. If any applicable policy has an explicit `Deny`, the request is denied. An explicit deny always wins.
3. Organization SCPs and RCPs, permission boundaries and session policies must all allow the action. They limit permissions but never grant them.
4. Otherwise, if an identity-based or resource-based policy allows the action, it is allowed.

A common interview trick: a user has `s3:*` in their policy, but the bucket policy has a `Deny` for their role. The result is denied.

## 55: How does assuming an IAM role work?

A role has two policies:

- **Trust policy**: who can assume the role.
- **Permissions policy**: what the role can do.

The caller calls `sts:AssumeRole` and gets temporary credentials (access key, secret key, session token) that expire after a set time (15 minutes to 12 hours, depending on the role's max session duration).

Trust policy example:

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Principal": { "AWS": "arn:aws:iam::111122223333:role/ci-runner" },
      "Action": "sts:AssumeRole"
    }
  ]
}
```

Assume the role in Python:

```python
import boto3

sts = boto3.client("sts")
creds = sts.assume_role(
    RoleArn="arn:aws:iam::222222222222:role/deploy",
    RoleSessionName="ci-deploy-1234",
    DurationSeconds=3600,
)["Credentials"]

s3 = boto3.client(
    "s3",
    aws_access_key_id=creds["AccessKeyId"],
    aws_secret_access_key=creds["SecretAccessKey"],
    aws_session_token=creds["SessionToken"],
)
```

With the CLI you can do the same with a profile:

```ini
# ~/.aws/config
[profile prod-deploy]
role_arn = arn:aws:iam::222222222222:role/deploy
source_profile = default
```

## 56: How do you give an application in account A access to resources in account B?

Two common ways:

1. **Cross-account role**: create a role in account B that trusts account A (or a specific role in A). The app in A calls `sts:AssumeRole` and uses the temporary credentials. The role in A also needs permission to call `sts:AssumeRole` on that role ARN.
2. **Resource-based policy**: if the service supports it (S3, SQS, SNS, KMS, Lambda, Secrets Manager), add a statement in account B that allows the principal from account A. The app keeps its own identity.

When a third party assumes a role in your account, use an **external ID** in the trust policy to avoid the "confused deputy" problem:

```json
"Condition": { "StringEquals": { "sts:ExternalId": "a8f3-unique-value" } }
```

## 57: How does the AWS SDK find credentials?

The SDKs and CLI use a **default credential provider chain**. Roughly in this order:

1. Credentials passed in code (avoid this).
2. Environment variables: `AWS_ACCESS_KEY_ID`, `AWS_SECRET_ACCESS_KEY`, `AWS_SESSION_TOKEN`.
3. Web identity token (`AWS_WEB_IDENTITY_TOKEN_FILE` + `AWS_ROLE_ARN`), used by EKS and CI systems.
4. Shared config and credentials files (`~/.aws/config`, `~/.aws/credentials`), including SSO and `role_arn` profiles. The profile comes from `AWS_PROFILE`.
5. Container credentials (ECS task role, EKS Pod Identity).
6. EC2 instance profile through the instance metadata service.

The exact order differs slightly by SDK, but the idea is the same. In Lambda, the execution role credentials are put in environment variables for you.

The key point: never hardcode access keys in code or commit them to Git. Create the client with no credentials and let the chain find them.

```python
s3 = boto3.client("s3")  # credentials come from the environment
```

## 58: How does an EC2 instance get AWS credentials, and what is IMDSv2?

You attach an **instance profile** (a container for an IAM role) to the instance. The SDK gets temporary credentials for that role from the Instance Metadata Service (IMDS) at `169.254.169.254`, and they rotate automatically.

**IMDSv2** requires a session token obtained by a `PUT` request first. This blocks many SSRF attacks that could steal credentials through IMDSv1's simple `GET`. New instance types and AMIs (such as Amazon Linux 2023) default to IMDSv2 only, and you should enforce it everywhere.

```bash
TOKEN=$(curl -s -X PUT "http://169.254.169.254/latest/api/token" \
  -H "X-aws-ec2-metadata-token-ttl-seconds: 21600")

curl -s -H "X-aws-ec2-metadata-token: $TOKEN" \
  http://169.254.169.254/latest/meta-data/iam/security-credentials/
```

```bash
aws ec2 modify-instance-metadata-options \
  --instance-id i-0abc123 \
  --http-tokens required
```

## 59: What is the difference between an ECS task role and a task execution role?

- **Task execution role**: used by the ECS agent (or Fargate) to start the task. It pulls the image from ECR, writes logs to CloudWatch Logs, and reads secrets from Secrets Manager or Parameter Store that are injected into the container.
- **Task role**: used by your application code inside the container to call AWS services (S3, DynamoDB, SQS, and so on).

```json
{
  "family": "orders-api",
  "taskRoleArn": "arn:aws:iam::111122223333:role/orders-api-task",
  "executionRoleArn": "arn:aws:iam::111122223333:role/ecsTaskExecutionRole",
  "containerDefinitions": [
    {
      "name": "app",
      "image": "111122223333.dkr.ecr.us-east-1.amazonaws.com/orders-api:1.4.2",
      "secrets": [
        {
          "name": "DB_PASSWORD",
          "valueFrom": "arn:aws:secretsmanager:us-east-1:111122223333:secret:prod/orders/db-AbCdEf"
        }
      ]
    }
  ]
}
```

If the app gets `AccessDenied` calling DynamoDB, check the task role. If the task fails to start because it cannot pull the image or read a secret, check the execution role.

## 60: What is the difference between a Lambda execution role and a Lambda resource-based policy?

- **Execution role**: what the function can do. For example, read from DynamoDB and write logs. Every function needs one, at least with `AWSLambdaBasicExecutionRole` for logs.
- **Resource-based policy**: who can invoke the function. For example, allow S3, SNS, EventBridge or API Gateway to call it, or allow another account.

```bash
aws lambda add-permission \
  --function-name process-upload \
  --statement-id s3-invoke \
  --action lambda:InvokeFunction \
  --principal s3.amazonaws.com \
  --source-arn arn:aws:s3:::my-upload-bucket \
  --source-account 111122223333
```

Note the difference with event source mappings (SQS, Kinesis, DynamoDB Streams): there Lambda polls the source, so the **execution role** needs permission to read from the queue or stream, and no resource-based policy is needed.

## 61: What is a permissions boundary?

A permissions boundary is a managed policy that sets the maximum permissions an IAM user or role can have. The effective permissions are the intersection of the identity policy and the boundary.

Typical use: you let developers create roles for their Lambda functions, but require that every role they create has a boundary attached, so they cannot create a role more powerful than allowed.

```json
{
  "Effect": "Allow",
  "Action": ["iam:CreateRole", "iam:AttachRolePolicy"],
  "Resource": "arn:aws:iam::111122223333:role/app-*",
  "Condition": {
    "StringEquals": {
      "iam:PermissionsBoundary": "arn:aws:iam::111122223333:policy/DevBoundary"
    }
  }
}
```

## 62: How do you apply least privilege in practice?

- Start with only the actions and resources the code needs. Avoid `"Action": "*"` and `"Resource": "*"`.
- Use one role per function or service, not one shared role.
- Use conditions (source ARN, VPC, tags, encryption) to narrow access further.
- Use **IAM Access Analyzer**: it can generate a policy from CloudTrail activity, validate policies, find resources shared outside your account, and find unused roles, keys and permissions.
- Check "last accessed" information in IAM to remove permissions nobody uses.
- With SAM, use policy templates like `DynamoDBReadPolicy` instead of full access. With CDK, use grant methods like `table.grantReadData(fn)`.

## 63: What are IAM condition keys and policy variables? Give examples.

Condition keys let you allow or deny based on request context.

Deny S3 access that does not use HTTPS:

```json
{
  "Effect": "Deny",
  "Principal": "*",
  "Action": "s3:*",
  "Resource": ["arn:aws:s3:::my-bucket", "arn:aws:s3:::my-bucket/*"],
  "Condition": { "Bool": { "aws:SecureTransport": "false" } }
}
```

Allow access only to resources with the same team tag as the caller (attribute-based access control):

```json
{
  "Effect": "Allow",
  "Action": ["ec2:StartInstances", "ec2:StopInstances"],
  "Resource": "*",
  "Condition": {
    "StringEquals": { "aws:ResourceTag/team": "${aws:PrincipalTag/team}" }
  }
}
```

Policy variables let one policy work for many users. Each user can only use their own folder:

```json
{
  "Effect": "Allow",
  "Action": ["s3:GetObject", "s3:PutObject"],
  "Resource": "arn:aws:s3:::user-files/home/${aws:username}/*"
}
```

Other useful keys: `aws:SourceIp`, `aws:SourceVpce`, `aws:MultiFactorAuthPresent`, `aws:PrincipalOrgID`, `aws:SourceArn`, `aws:SourceAccount`.

## 64: What is the difference between Cognito user pools and identity pools?

- **User pool**: a user directory for sign-up and sign-in. It handles passwords, MFA, email/phone verification, social and SAML/OIDC login, and returns JWT tokens (ID, access, refresh). Use it to authenticate users of your app.
- **Identity pool** (federated identities): exchanges a token (from a user pool, Google, Apple, SAML, and so on) or guest access for **temporary AWS credentials** for an IAM role. Use it when the client (mobile or browser) needs to call AWS services directly, like uploading to S3.

Common setup: users sign in to a user pool, the app sends the token to API Gateway for API calls, and uses an identity pool when it needs direct AWS access.

## 65: What tokens does a Cognito user pool return, and how do you validate them?

- **ID token**: claims about the user (email, name, groups). Used by the app to know who the user is.
- **Access token**: has scopes and groups. Used to authorize API calls.
- **Refresh token**: gets new ID and access tokens. Default valid for 30 days.

ID and access tokens are JWTs, valid for 1 hour by default (configurable). To validate one yourself: check the signature with the user pool's JWKS (`https://cognito-idp.<region>.amazonaws.com/<userPoolId>/.well-known/jwks.json`), check `exp`, check `iss`, check `token_use`, and check `aud` (ID token) or `client_id` (access token).

The `aws-jwt-verify` library does all of this:

```javascript
import { CognitoJwtVerifier } from "aws-jwt-verify";

const verifier = CognitoJwtVerifier.create({
  userPoolId: "us-east-1_AbC123xyz",
  tokenUse: "access",
  clientId: "4k2ex5rn1dk2f1example",
});

export async function getUser(authHeader) {
  const token = authHeader?.replace(/^Bearer /, "");
  try {
    const payload = await verifier.verify(token);
    return { sub: payload.sub, groups: payload["cognito:groups"] ?? [] };
  } catch {
    return null; // invalid or expired
  }
}
```

## 66: How do users sign in with Cognito using OAuth 2.0?

Cognito user pools provide **managed login** (the newer version of the hosted UI) with OAuth 2.0 and OpenID Connect endpoints. For web and mobile apps, use the **authorization code grant with PKCE**:

1. The app redirects the user to `https://<domain>/oauth2/authorize?response_type=code&client_id=...&redirect_uri=...&scope=openid+email&code_challenge=...&code_challenge_method=S256`.
2. The user signs in (password, passkey, social login, or SAML/OIDC).
3. Cognito redirects back to the app with a `code`.
4. The app calls `/oauth2/token` with the code and the PKCE `code_verifier` and gets tokens.

Do not use the implicit grant for new apps. For machine-to-machine calls, use the **client credentials** grant with an app client that has a secret and custom scopes from a resource server.

Libraries like AWS Amplify handle this flow for you.

## 67: What authorization options does API Gateway support?

| Option                       | REST API               | HTTP API           | Notes                                                                   |
| ---------------------------- | ---------------------- | ------------------ | ----------------------------------------------------------------------- |
| IAM (SigV4)                  | Yes                    | Yes                | Good for AWS services, other accounts, and clients with AWS credentials |
| Cognito user pool authorizer | Yes                    | Via JWT authorizer | Validates the Cognito token, no code                                    |
| JWT authorizer               | No                     | Yes                | Any OIDC/OAuth 2.0 provider                                             |
| Lambda authorizer            | Yes                    | Yes                | Custom logic, any token format                                          |
| API keys                     | Yes (with usage plans) | No                 | For metering, not real auth                                             |
| Resource policy              | Yes                    | No                 | Allow/deny by account, IP, VPC endpoint                                 |

Mutual TLS is also supported with a custom domain name.

## 68: How does a Lambda authorizer work?

API Gateway calls your function before the real integration. The function checks the token or request and returns an IAM policy (REST API) or a simple yes/no (HTTP API with simple responses). API Gateway can cache the result for a TTL (default 300 seconds, max 3600).

Two types for REST APIs:

- **TOKEN**: gets one header value (like `Authorization`).
- **REQUEST**: gets headers, query string, path and context. Required for caching on several values.

REST API, TOKEN authorizer:

```javascript
export const handler = async (event) => {
  const token = event.authorizationToken;
  const user = await validateToken(token); // your own check

  return {
    principalId: user ? user.id : "anonymous",
    policyDocument: {
      Version: "2012-10-17",
      Statement: [
        {
          Action: "execute-api:Invoke",
          Effect: user ? "Allow" : "Deny",
          Resource: event.methodArn,
        },
      ],
    },
    context: user ? { userId: user.id, plan: user.plan } : {},
  };
};
```

HTTP API with simple responses:

```javascript
export const handler = async (event) => {
  const ok = await validateToken(event.headers.authorization);
  return { isAuthorized: ok, context: { source: "custom-auth" } };
};
```

Be careful with caching: if you return a policy for `event.methodArn` only and caching is on, the same cached policy may be used for other methods and get denied. Return a wider resource (for example `arn:...:api-id/stage/*`) if needed.

## 69: How do you protect an HTTP API with a Cognito JWT authorizer?

In SAM:

```yaml
OrdersApi:
  Type: AWS::Serverless::HttpApi
  Properties:
    Auth:
      DefaultAuthorizer: CognitoJwt
      Authorizers:
        CognitoJwt:
          IdentitySource: $request.header.Authorization
          JwtConfiguration:
            issuer: !Sub https://cognito-idp.${AWS::Region}.amazonaws.com/${UserPool}
            audience:
              - !Ref UserPoolClient
```

API Gateway checks the signature, expiry, issuer and audience. Your Lambda gets the claims in the event:

```python
def lambda_handler(event, context):
    claims = event["requestContext"]["authorizer"]["jwt"]["claims"]
    user_id = claims["sub"]
    ...
```

You can also require OAuth scopes per route with `AuthorizationScopes`.

## 70: How do clients call an API protected with IAM authorization?

The request must be signed with **Signature Version 4** using AWS credentials, and the caller's IAM policy must allow `execute-api:Invoke` on the API ARN.

```json
{
  "Effect": "Allow",
  "Action": "execute-api:Invoke",
  "Resource": "arn:aws:execute-api:us-east-1:111122223333:a1b2c3d4e5/prod/GET/orders/*"
}
```

Signing a request in Node.js with SDK v3 components:

```javascript
import { SignatureV4 } from "@smithy/signature-v4";
import { HttpRequest } from "@smithy/protocol-http";
import { Sha256 } from "@aws-crypto/sha256-js";
import { defaultProvider } from "@aws-sdk/credential-provider-node";

const signer = new SignatureV4({
  credentials: defaultProvider(),
  region: "us-east-1",
  service: "execute-api",
  sha256: Sha256,
});

const request = new HttpRequest({
  method: "GET",
  protocol: "https:",
  hostname: "a1b2c3d4e5.execute-api.us-east-1.amazonaws.com",
  path: "/prod/orders/o-1",
  headers: { host: "a1b2c3d4e5.execute-api.us-east-1.amazonaws.com" },
});

const signed = await signer.sign(request);
const resp = await fetch(`https://${signed.hostname}${signed.path}`, {
  headers: signed.headers,
});
```

With the CLI, `awscurl` or Postman's AWS Signature auth type are handy for testing.

## 71: What is AWS KMS and what types of keys are there?

AWS Key Management Service creates and controls encryption keys. Key material never leaves KMS unencrypted (it is protected by FIPS-validated HSMs).

By owner:

- **AWS owned keys**: used by services internally, you do not see them. Free.
- **AWS managed keys**: created by a service in your account (`aws/s3`, `aws/lambda`), you cannot change their policy. Rotated every year.
- **Customer managed keys**: you create and control them: key policy, rotation, grants, enable/disable, deletion. Needed for cross-account use and fine-grained control.

By type:

- **Symmetric** (AES-256): the default, used for most encryption. Used with `Encrypt`, `Decrypt`, `GenerateDataKey`.
- **Asymmetric** (RSA, ECC): for public-key encryption or signing and verifying outside AWS.
- **HMAC**: to generate and verify message authentication codes.

There are also multi-Region keys (same key material in several Regions) and keys with imported material or in a custom key store (CloudHSM or external).

## 72: What is envelope encryption?

KMS `Encrypt` only takes up to 4 KB of data. For larger data you use envelope encryption:

1. Call `GenerateDataKey`. KMS returns a data key in plaintext and the same key encrypted under your KMS key.
2. Encrypt your data locally with the plaintext data key, then delete it from memory.
3. Store the encrypted data together with the encrypted data key.
4. To decrypt: call `Decrypt` on the encrypted data key, then decrypt the data locally.

```python
import os
import boto3
from cryptography.hazmat.primitives.ciphers.aead import AESGCM

kms = boto3.client("kms")

def encrypt(data: bytes):
    dk = kms.generate_data_key(KeyId="alias/app-data", KeySpec="AES_256")
    nonce = os.urandom(12)
    ciphertext = AESGCM(dk["Plaintext"]).encrypt(nonce, data, None)
    return {"ciphertext": ciphertext, "nonce": nonce, "encrypted_key": dk["CiphertextBlob"]}

def decrypt(blob):
    key = kms.decrypt(CiphertextBlob=blob["encrypted_key"])["Plaintext"]
    return AESGCM(key).decrypt(blob["nonce"], blob["ciphertext"], None)
```

Benefits: large data never goes over the network to KMS, and you make fewer KMS calls. In real projects use the **AWS Encryption SDK**, which does this for you with a safe message format. AWS services like S3 and DynamoDB use envelope encryption internally.

## 73: What KMS limits and errors should you know as a developer?

- `Encrypt` accepts at most **4 KB** of plaintext.
- Each account has **request quotas** per second for cryptographic operations (shared across operations, thousands per second depending on the Region and key type). Above that you get `ThrottlingException`.
- SSE-KMS on S3 calls KMS for each object upload and download, so a busy bucket can hit the KMS quota.

How to avoid throttling:

- Use **S3 Bucket Keys** to reduce KMS calls from S3 by up to 99%.
- Cache data keys (the AWS Encryption SDK has a caching feature).
- Use exponential backoff and retries (the SDK does this by default).
- Request a quota increase if needed.

Other common errors: `AccessDeniedException` (the key policy or IAM policy does not allow the action), `DisabledException`, and `KMSInvalidStateException` (key pending deletion).

## 74: What are KMS key policies and grants?

Every KMS key has a **key policy**, which is the main way to control access. Unlike most services, IAM policies alone are not enough: the key policy must allow the account (usually through the root principal statement below) before IAM policies can grant access.

```json
{
  "Sid": "EnableIAMPolicies",
  "Effect": "Allow",
  "Principal": { "AWS": "arn:aws:iam::111122223333:root" },
  "Action": "kms:*",
  "Resource": "*"
}
```

```json
{
  "Sid": "AllowAppToUseKey",
  "Effect": "Allow",
  "Principal": { "AWS": "arn:aws:iam::111122223333:role/orders-api" },
  "Action": ["kms:Encrypt", "kms:Decrypt", "kms:GenerateDataKey"],
  "Resource": "*",
  "Condition": {
    "StringEquals": { "kms:ViaService": "s3.us-east-1.amazonaws.com" }
  }
}
```

**Grants** give temporary, programmatic permission to use a key, often used by AWS services (for example EBS or RDS) on your behalf. You create them with `CreateGrant` and remove them with `RetireGrant` or `RevokeGrant`.

## 75: How does KMS key rotation work?

- **Automatic rotation** for symmetric customer managed keys: off by default. When on, KMS creates new key material on a schedule you choose, from 90 to 2,560 days (default 365).
- **On-demand rotation**: you can rotate right away with `RotateKeyOnDemand`.
- **AWS managed keys** rotate every year automatically.
- The key ID, ARN and alias stay the same. Old key material is kept so old data can still be decrypted. You do not need to re-encrypt data.
- Asymmetric, HMAC and imported keys do not support automatic rotation. Rotate them manually by creating a new key and moving the alias.

```bash
aws kms enable-key-rotation --key-id 1234abcd-12ab-34cd-56ef-1234567890ab --rotation-period-in-days 180
```

## 76: What encryption options exist for S3 objects?

Server-side:

- **SSE-S3**: S3 manages the keys (AES-256). Since January 2023 this is applied to all new objects by default.
- **SSE-KMS**: uses a KMS key. You get access control through the key policy and audit logs in CloudTrail. Header: `x-amz-server-side-encryption: aws:kms`.
- **DSSE-KMS**: dual-layer encryption with KMS, for strict compliance requirements.
- **SSE-C**: you provide the key in every request. S3 does not store it. HTTPS is required. AWS has announced that SSE-C is disabled by default on new buckets, so prefer SSE-KMS for new work.

Client-side: you encrypt before upload (for example with the Amazon S3 Encryption Client or the AWS Encryption SDK). S3 never sees the plaintext.

```python
s3.put_object(
    Bucket="customer-docs",
    Key="contracts/c-1.pdf",
    Body=data,
    ServerSideEncryption="aws:kms",
    SSEKMSKeyId="alias/customer-docs",
    BucketKeyEnabled=True,
)
```

## 77: How do you force encryption and HTTPS for an S3 bucket?

1. Set **default encryption** on the bucket (for example SSE-KMS with a customer managed key and Bucket Key enabled). Objects uploaded without headers are encrypted with it.
2. To require a specific key, add a bucket policy that denies `PutObject` with a different key.
3. Deny any request not using TLS.

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "DenyInsecureTransport",
      "Effect": "Deny",
      "Principal": "*",
      "Action": "s3:*",
      "Resource": [
        "arn:aws:s3:::customer-docs",
        "arn:aws:s3:::customer-docs/*"
      ],
      "Condition": { "Bool": { "aws:SecureTransport": "false" } }
    },
    {
      "Sid": "DenyWrongKmsKey",
      "Effect": "Deny",
      "Principal": "*",
      "Action": "s3:PutObject",
      "Resource": "arn:aws:s3:::customer-docs/*",
      "Condition": {
        "StringNotEqualsIfExists": {
          "s3:x-amz-server-side-encryption-aws-kms-key-id": "arn:aws:kms:us-east-1:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab"
        }
      }
    }
  ]
}
```

## 78: What is an S3 presigned URL and how do you create one?

A presigned URL gives temporary access to a specific object operation (GET or PUT) to anyone who has the URL, without AWS credentials. It is signed with the credentials of whoever created it, and works only if that identity has the permission.

Common use: let a browser upload a file directly to S3 instead of sending it through your API.

```javascript
import {
  S3Client,
  PutObjectCommand,
  GetObjectCommand,
} from "@aws-sdk/client-s3";
import { getSignedUrl } from "@aws-sdk/s3-request-presigner";

const s3 = new S3Client({});

export const handler = async (event) => {
  const key = `uploads/${crypto.randomUUID()}.png`;

  const uploadUrl = await getSignedUrl(
    s3,
    new PutObjectCommand({
      Bucket: "user-uploads",
      Key: key,
      ContentType: "image/png",
    }),
    { expiresIn: 300 }, // seconds
  );

  return { statusCode: 200, body: JSON.stringify({ uploadUrl, key }) };
};
```

```python
url = boto3.client("s3").generate_presigned_url(
    "get_object",
    Params={"Bucket": "user-uploads", "Key": "uploads/abc.png"},
    ExpiresIn=600,
)
```

Max expiry is 7 days with long-term credentials. If the URL is signed with temporary credentials (like a Lambda role), it stops working when those credentials expire, even if `expiresIn` is longer.

## 79: What are S3 Block Public Access and Object Ownership?

- **Block Public Access**: account-level and bucket-level settings that override any policy or ACL that would make data public. Since April 2023 it is on by default for new buckets. Keep it on unless the bucket really must be public (and even for websites, use CloudFront with OAC instead).
- **Object Ownership**: with "Bucket owner enforced" (default for new buckets since April 2023), ACLs are disabled and the bucket owner owns every object. Access is controlled only by policies. AWS recommends keeping ACLs disabled.

If an old app sends `x-amz-acl` headers to a bucket with ACLs disabled, uploads fail with `AccessControlListNotSupported` unless the ACL is `bucket-owner-full-control`.

## 80: How do you configure CORS on an S3 bucket?

If a web page on `https://app.example.com` loads files from or uploads to S3 directly (for example with a presigned URL), the bucket needs a CORS configuration:

```json
[
  {
    "AllowedOrigins": ["https://app.example.com"],
    "AllowedMethods": ["GET", "PUT"],
    "AllowedHeaders": ["*"],
    "ExposeHeaders": ["ETag"],
    "MaxAgeSeconds": 3000
  }
]
```

```bash
aws s3api put-bucket-cors --bucket user-uploads --cors-configuration file://cors.json
```

CORS does not grant permission. It only tells the browser which cross-origin requests are allowed. You still need a presigned URL or a policy that allows the request.

## 81: What is the difference between Secrets Manager and SSM Parameter Store?

|                      | Secrets Manager                                                                             | Parameter Store                                |
| -------------------- | ------------------------------------------------------------------------------------------- | ---------------------------------------------- |
| Purpose              | Secrets (DB passwords, API keys)                                                            | Config values and secrets                      |
| Automatic rotation   | Built in, with Lambda rotation functions and managed rotation for RDS, Redshift, DocumentDB | No built-in rotation                           |
| Encryption           | Always encrypted with KMS                                                                   | `SecureString` uses KMS, `String` is plaintext |
| Cross-account access | Yes, with resource policy                                                                   | Advanced parameters can be shared with AWS RAM |
| Size                 | 64 KB                                                                                       | 4 KB standard, 8 KB advanced                   |
| Cost                 | Per secret per month plus API calls                                                         | Standard parameters are free                   |

Rule of thumb: use Secrets Manager for credentials that should rotate, and Parameter Store for configuration and simple secrets. You can read Secrets Manager secrets through the Parameter Store API too, with the `/aws/reference/secretsmanager/` prefix.

## 82: How do you read a secret from Secrets Manager in code?

```python
import json
import boto3

sm = boto3.client("secretsmanager")

def get_db_credentials():
    resp = sm.get_secret_value(SecretId="prod/orders/db")
    return json.loads(resp["SecretString"])

creds = get_db_credentials()
# creds["username"], creds["password"], creds["host"]
```

```javascript
import {
  SecretsManagerClient,
  GetSecretValueCommand,
} from "@aws-sdk/client-secrets-manager";

const sm = new SecretsManagerClient({});
const { SecretString } = await sm.send(
  new GetSecretValueCommand({ SecretId: "prod/orders/db" }),
);
const creds = JSON.parse(SecretString);
```

Do not call the API on every request. Cache the value (for example with the `aws-secretsmanager-caching` library or the Parameters and Secrets Lambda Extension) and refresh it on a timer or when authentication fails. The role needs `secretsmanager:GetSecretValue` and `kms:Decrypt` if a customer managed key is used.

## 83: How does secret rotation work in Secrets Manager?

Secrets Manager rotates a secret on a schedule (for example every 30 days, or with a cron expression) by running a rotation Lambda function in four steps:

1. `createSecret`: create a new version with a new password, labeled `AWSPENDING`.
2. `setSecret`: change the password in the database.
3. `testSecret`: log in with the new password.
4. `finishSecret`: move the `AWSCURRENT` label to the new version. The old one becomes `AWSPREVIOUS`.

For RDS, Aurora, Redshift and DocumentDB, AWS provides ready-made rotation functions. For RDS you can also let RDS manage the master password in Secrets Manager (`ManageMasterUserPassword`), which rotates it without any Lambda.

Strategies: **single user** (change the password of one user, with a short window where connections can fail) or **alternating users** (two users, switch between them, no downtime).

Apps must not cache secrets forever. They should re-read the secret when a login fails.

## 84: How do you use Parameter Store hierarchies?

Name parameters like a path, so you can read all values for an app and environment at once and control access by path in IAM.

```bash
aws ssm put-parameter --name /orders/prod/table-name --type String --value Orders-prod
aws ssm put-parameter --name /orders/prod/api-key --type SecureString --value 's3cr3t' --key-id alias/orders
```

```python
import boto3

ssm = boto3.client("ssm")
params = {}
paginator = ssm.get_paginator("get_parameters_by_path")
for page in paginator.paginate(Path="/orders/prod/", Recursive=True, WithDecryption=True):
    for p in page["Parameters"]:
        params[p["Name"].split("/")[-1]] = p["Value"]
```

IAM policy for one environment only:

```json
{
  "Effect": "Allow",
  "Action": ["ssm:GetParametersByPath", "ssm:GetParameter"],
  "Resource": "arn:aws:ssm:us-east-1:111122223333:parameter/orders/prod/*"
}
```

Parameters can also be referenced in CloudFormation (`{{resolve:ssm:/orders/prod/table-name}}`).

## 85: How are Lambda environment variables encrypted?

Lambda always encrypts environment variables at rest with KMS, using an AWS managed key (`aws/lambda`) by default. You can pick a customer managed key for more control.

Anyone with `lambda:GetFunctionConfiguration` can still see the values in plaintext. So for real secrets:

- Option 1 (recommended): store them in Secrets Manager or Parameter Store and read them at runtime.
- Option 2: use encryption helpers so the value is encrypted in transit and in the console, and decrypt it in code with `kms:Decrypt`.

```python
import os
import base64
import boto3

ENCRYPTED = os.environ["API_KEY"]
API_KEY = boto3.client("kms").decrypt(
    CiphertextBlob=base64.b64decode(ENCRYPTED),
    EncryptionContext={"LambdaFunctionName": os.environ["AWS_LAMBDA_FUNCTION_NAME"]},
)["Plaintext"].decode()
```

## 86: How do you handle encryption in transit?

- AWS service endpoints use HTTPS (TLS 1.2 or higher). The SDKs use TLS by default.
- Use **AWS Certificate Manager (ACM)** for free public TLS certificates on ALB, CloudFront, API Gateway custom domains and more. ACM renews them automatically.
- Certificates for **CloudFront** must be in **us-east-1**. For regional services like ALB or a regional API Gateway, the certificate must be in the same Region.
- Enforce TLS with policies (`aws:SecureTransport`) and with TLS settings on CloudFront, API Gateway and load balancers.
- Turn on TLS for ElastiCache (in-transit encryption) and RDS (`rds.force_ssl`).

## 87: How do you let a Lambda function access resources in a private VPC?

Configure the function with VPC subnets and security groups. Lambda creates elastic network interfaces (Hyperplane ENIs) in those subnets. This is needed to reach RDS, ElastiCache, or internal services in private subnets.

```yaml
OrdersFunction:
  Type: AWS::Serverless::Function
  Properties:
    VpcConfig:
      SubnetIds: [subnet-0aaa, subnet-0bbb]
      SecurityGroupIds: [sg-0lambda]
```

Things to know:

- The execution role needs ENI permissions (`AWSLambdaVPCAccessExecutionRole`).
- A function in a VPC has **no internet access** by default, even in a public subnet. To call the internet or public AWS endpoints, use a NAT gateway in a public subnet, or use **VPC endpoints** for AWS services.
- The database security group must allow inbound traffic from the Lambda security group.
- Use more than one subnet in different AZs for availability.

## 88: What is the difference between gateway and interface VPC endpoints?

VPC endpoints let resources in a VPC reach AWS services privately, without an internet gateway or NAT.

- **Gateway endpoints**: only for **S3 and DynamoDB**. You add them to route tables. Free.
- **Interface endpoints (AWS PrivateLink)**: an ENI with a private IP in your subnet, for most AWS services (SQS, SNS, Secrets Manager, KMS, STS, ECR, CloudWatch, and more). Charged per hour and per GB. S3 also supports interface endpoints.

You can attach **endpoint policies** to restrict what can be done through the endpoint, and use conditions like `aws:SourceVpce` in bucket policies to allow access only from your VPC.

```json
{
  "Effect": "Deny",
  "Principal": "*",
  "Action": "s3:*",
  "Resource": ["arn:aws:s3:::internal-data", "arn:aws:s3:::internal-data/*"],
  "Condition": { "StringNotEquals": { "aws:SourceVpce": "vpce-0abc123" } }
}
```

## 89: What is the difference between security groups and network ACLs?

|       | Security group                                  | Network ACL                                |
| ----- | ----------------------------------------------- | ------------------------------------------ |
| Level | ENI / instance                                  | Subnet                                     |
| State | Stateful (return traffic allowed automatically) | Stateless (you must allow return traffic)  |
| Rules | Allow only                                      | Allow and deny                             |
| Order | All rules evaluated                             | Evaluated by rule number, first match wins |

Developers mostly work with security groups. A good practice is to reference other security groups instead of IP ranges, for example "allow port 5432 from the Lambda security group".

## 90: How can you restrict users to only their own items in DynamoDB?

Use **fine-grained access control** with the `dynamodb:LeadingKeys` condition. With Cognito identity pools, the user's identity ID is available as a policy variable.

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "dynamodb:GetItem",
        "dynamodb:PutItem",
        "dynamodb:Query",
        "dynamodb:UpdateItem"
      ],
      "Resource": "arn:aws:dynamodb:us-east-1:111122223333:table/UserNotes",
      "Condition": {
        "ForAllValues:StringEquals": {
          "dynamodb:LeadingKeys": ["${cognito-identity.amazonaws.com:sub}"]
        }
      }
    }
  ]
}
```

The table's partition key must hold the identity ID. You can also limit which attributes a user can read or write with `dynamodb:Attributes` and `dynamodb:Select`.

## 91: How do you let GitHub Actions (or any CI system) deploy to AWS without access keys?

Use **OIDC federation**. GitHub issues a short-lived token, AWS STS exchanges it for temporary credentials with `AssumeRoleWithWebIdentity`.

1. Create an IAM OIDC identity provider for `https://token.actions.githubusercontent.com` with audience `sts.amazonaws.com`.
2. Create a role with a trust policy that only allows your repository and branch:

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Principal": {
        "Federated": "arn:aws:iam::111122223333:oidc-provider/token.actions.githubusercontent.com"
      },
      "Action": "sts:AssumeRoleWithWebIdentity",
      "Condition": {
        "StringEquals": {
          "token.actions.githubusercontent.com:aud": "sts.amazonaws.com",
          "token.actions.githubusercontent.com:sub": "repo:my-org/orders-service:ref:refs/heads/main"
        }
      }
    }
  ]
}
```

3. Use it in the workflow:

```yaml
permissions:
  id-token: write
  contents: read

jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: aws-actions/configure-aws-credentials@v4
        with:
          role-to-assume: arn:aws:iam::111122223333:role/github-deploy
          aws-region: us-east-1
      - run: sam deploy --no-confirm-changeset
```

No long-term keys are stored in GitHub, and the credentials expire after the job.

## 92: How do developers get CLI credentials with IAM Identity Center?

IAM Identity Center (successor to AWS SSO) gives people one sign-in for many accounts and permission sets. For the CLI:

```bash
aws configure sso
# SSO session name: my-company
# SSO start URL: https://my-company.awsapps.com/start
# SSO region: us-east-1
# then pick the account and role

aws sso login --profile dev
aws s3 ls --profile dev
```

The CLI and SDKs read the cached token and get short-term role credentials automatically. They refresh when needed, and you run `aws sso login` again when the session expires. This replaces sharing long-term access keys among developers.

## 93: What are STS temporary credentials and how do MFA-protected API calls work?

STS (Security Token Service) returns temporary credentials: an access key ID, secret key and session token with an expiry time. Main APIs:

- `AssumeRole`: assume a role in the same or another account.
- `AssumeRoleWithWebIdentity`: exchange an OIDC token (Cognito, GitHub, EKS).
- `AssumeRoleWithSAML`: exchange a SAML assertion.
- `GetSessionToken`: get temporary credentials for an IAM user, often with MFA.
- `GetCallerIdentity`: returns who you are. Useful for debugging and does not need any permission.

To require MFA for sensitive actions, use a condition:

```json
{
  "Effect": "Deny",
  "Action": ["ec2:TerminateInstances", "s3:DeleteBucket"],
  "Resource": "*",
  "Condition": { "BoolIfExists": { "aws:MultiFactorAuthPresent": "false" } }
}
```

```bash
aws sts get-session-token --serial-number arn:aws:iam::111122223333:mfa/alice --token-code 123456
aws sts get-caller-identity
```

## 94: How do you audit who did what in an AWS account?

**AWS CloudTrail** records API calls made in the account: who called, from where, when, which parameters, and whether it succeeded.

- **Event history**: the last 90 days of management events, free, in the console.
- **Trails**: send events to S3 (and optionally CloudWatch Logs) for long-term storage. Can be multi-Region and organization-wide.
- **Data events**: object-level S3 operations, Lambda invocations, DynamoDB item operations. Off by default because of volume and cost.
- **CloudTrail Lake**: store events and query them with SQL.

Example: find who deleted a table.

```bash
aws cloudtrail lookup-events \
  --lookup-attributes AttributeKey=EventName,AttributeValue=DeleteTable \
  --max-results 5
```

## 95: How do you keep sensitive data out of logs?

- Do not log full request bodies, tokens, passwords or card numbers. Log IDs instead.
- Use structured logging so you control exactly which fields are written.
- Use **CloudWatch Logs data protection policies** to detect and mask sensitive data (emails, credit card numbers, AWS secret keys, and many more types) in log groups. Masked values can only be seen by users with the `logs:Unmask` permission.
- Set log retention and encrypt log groups with a KMS key if needed.
- Use **Amazon Macie** to find sensitive data stored in S3.

```bash
aws logs put-data-protection-policy \
  --log-group-identifier /aws/lambda/orders-api \
  --policy-document file://data-protection.json
```

## 96: How do you protect a public API from abuse?

- **AWS WAF** on CloudFront, API Gateway REST APIs, ALB, AppSync or Cognito user pools: managed rule groups (SQL injection, common exploits, known bad IPs), rate-based rules, geo blocking, bot control.
- **Throttling** in API Gateway at stage, method and usage plan level.
- **Authentication** on every route that is not meant to be public.
- **Request validation** in API Gateway REST APIs (JSON schema models) to reject bad input early.
- **AWS Shield Standard** is on for everyone and protects against common DDoS attacks. Shield Advanced adds more protection and support.
- Put **CloudFront** in front for caching and to absorb traffic at the edge.

## 97: How do you serve private S3 content through CloudFront?

Use **Origin Access Control (OAC)**, which replaced the older Origin Access Identity (OAI). The bucket stays private and only CloudFront can read it. OAC also works with SSE-KMS encrypted objects.

Bucket policy:

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "AllowCloudFrontOAC",
      "Effect": "Allow",
      "Principal": { "Service": "cloudfront.amazonaws.com" },
      "Action": "s3:GetObject",
      "Resource": "arn:aws:s3:::my-site-content/*",
      "Condition": {
        "StringEquals": {
          "AWS:SourceArn": "arn:aws:cloudfront::111122223333:distribution/E1ABCDEF2GHIJ"
        }
      }
    }
  ]
}
```

If objects use SSE-KMS, the KMS key policy must also allow `kms:Decrypt` for the CloudFront service principal with the same source ARN condition.

## 98: What is the difference between CloudFront signed URLs, signed cookies and S3 presigned URLs?

- **S3 presigned URL**: signed with IAM credentials, gives access to one S3 object directly. Good for uploads and short-lived downloads.
- **CloudFront signed URL**: signed with a key in a CloudFront **key group**, gives access to one file through CloudFront. Supports custom policies (IP range, start and end time).
- **CloudFront signed cookies**: same idea, but one cookie gives access to many files, like all the segments of a video or a whole members area.

Use CloudFront signing when content is served through CloudFront (caching, global edge). Use S3 presigned URLs when the client talks to S3 directly.

## 99: How is data encrypted at rest in common serverless services?

| Service              | Default                                   | Options                                 |
| -------------------- | ----------------------------------------- | --------------------------------------- |
| S3                   | SSE-S3                                    | SSE-KMS, DSSE-KMS, client-side          |
| DynamoDB             | AWS owned key                             | AWS managed key or customer managed key |
| SQS                  | SSE-SQS (SQS managed keys) for new queues | SSE-KMS                                 |
| SNS                  | Not encrypted by default                  | SSE with KMS                            |
| Lambda env vars      | `aws/lambda` key                          | Customer managed key                    |
| CloudWatch Logs      | Encrypted by the service                  | Customer managed KMS key per log group  |
| Kinesis Data Streams | Not encrypted by default                  | SSE with KMS                            |
| Secrets Manager      | `aws/secretsmanager`                      | Customer managed key                    |

When you use a customer managed key, remember that producers and consumers need `kms:GenerateDataKey` and/or `kms:Decrypt` on that key. For example, an SNS topic sending to an encrypted SQS queue needs the queue's KMS key policy to allow the SNS service principal.

## 100: An access key was committed to a public Git repository. What do you do?

1. **Deactivate the key right away** (or delete it) in IAM. Do not wait. Bots scan GitHub for keys within minutes.
2. Check **CloudTrail** for actions done with that key (`userIdentity.accessKeyId`) and look for new users, roles, keys, EC2 instances, Lambda functions, or changes to policies.
3. Remove anything the attacker created and rotate any other secrets that may be exposed.
4. Remove the key from Git history (rewriting history is not enough on its own, because the key is already public, which is why step 1 comes first).
5. Check billing and contact AWS Support if needed. AWS may also contact you and attach the `AWSCompromisedKeyQuarantine` policy to the user.
6. Prevent it next time: use roles and short-term credentials (IAM Identity Center, OIDC for CI), git hooks or secret scanning (for example git-secrets or GitHub secret scanning), and a secret scan step in the pipeline.

---

# Domain 3: Deployment

## 101: What is AWS SAM?

The AWS Serverless Application Model (SAM) is an extension of CloudFormation for serverless apps. A SAM template has `Transform: AWS::Serverless-2016-10-31`, and short resource types like `AWS::Serverless::Function`, `AWS::Serverless::Api`, `AWS::Serverless::HttpApi`, `AWS::Serverless::SimpleTable`, `AWS::Serverless::StateMachine` and `AWS::Serverless::LayerVersion`. During deployment, CloudFormation expands them into normal resources (function, role, permissions, API, event source mappings, and so on).

```yaml
AWSTemplateFormatVersion: "2010-09-09"
Transform: AWS::Serverless-2016-10-31
Description: Orders service

Globals:
  Function:
    Runtime: python3.13
    Architectures: [arm64]
    MemorySize: 256
    Timeout: 10
    Environment:
      Variables:
        TABLE_NAME: !Ref OrdersTable

Resources:
  CreateOrderFunction:
    Type: AWS::Serverless::Function
    Properties:
      CodeUri: src/
      Handler: app.create_order
      Policies:
        - DynamoDBCrudPolicy:
            TableName: !Ref OrdersTable
      Events:
        CreateOrder:
          Type: HttpApi
          Properties:
            Path: /orders
            Method: post

  OrdersTable:
    Type: AWS::DynamoDB::Table
    Properties:
      BillingMode: PAY_PER_REQUEST
      AttributeDefinitions:
        - AttributeName: orderId
          AttributeType: S
      KeySchema:
        - AttributeName: orderId
          KeyType: HASH

Outputs:
  ApiUrl:
    Value: !Sub "https://${ServerlessHttpApi}.execute-api.${AWS::Region}.amazonaws.com"
```

## 102: What are the main SAM CLI commands?

```bash
sam init                         # start a new project from a template
sam build                        # install dependencies and prepare artifacts in .aws-sam/
sam build --use-container        # build inside a Lambda-like container (native dependencies)
sam validate --lint              # check the template

sam local invoke CreateOrderFunction -e events/create.json   # run one function locally in Docker
sam local start-api              # run API Gateway + functions locally
sam local generate-event s3 put  # create a sample event

sam deploy --guided              # first deploy, saves answers to samconfig.toml
sam deploy                       # later deploys
sam sync --watch --stack-name orders-dev   # fast sync of code changes to a dev stack

sam logs -n CreateOrderFunction --stack-name orders-dev --tail
sam remote invoke CreateOrderFunction --stack-name orders-dev --event '{"id":"1"}'
sam delete --stack-name orders-dev
```

`sam sync` skips CloudFormation for code-only changes and updates the function directly, which is much faster. Use it only for development stacks, never production.

## 103: What are SAM policy templates and Globals?

**Policy templates** are predefined, scoped IAM policies you can add to a function with one line. They help with least privilege.

```yaml
Policies:
  - DynamoDBReadPolicy:
      TableName: !Ref OrdersTable
  - SQSSendMessagePolicy:
      QueueName: !GetAtt ShippingQueue.QueueName
  - S3ReadPolicy:
      BucketName: !Ref UploadsBucket
  - SSMParameterReadPolicy:
      ParameterName: orders/prod/*
  - Statement: # you can also add plain statements
      - Effect: Allow
        Action: events:PutEvents
        Resource: !GetAtt OrdersBus.Arn
```

**Globals** set common properties for all functions, APIs or tables in the template (runtime, memory, timeout, environment variables, tracing, layers). A value set on a resource overrides the global one.

SAM **connectors** (`AWS::Serverless::Connector` or the `Connectors` property) are another way to give permissions: you say "this function writes to this table" and SAM builds the policy.

## 104: What are the sections of a CloudFormation template?

```yaml
AWSTemplateFormatVersion: "2010-09-09" # optional
Description: My stack # optional
Metadata: {} # optional, extra info (for example console parameter grouping)
Parameters: {} # input values at deploy time
Rules: {} # validate parameter combinations
Mappings: {} # static lookup tables
Conditions: {} # create resources only if a condition is true
Transform: [] # macros, for example AWS::Serverless-2016-10-31
Resources: {} # the only required section
Outputs: {} # values to show or export
```

Templates can be JSON or YAML. `Resources` is the only required section.

## 105: What are the most used CloudFormation intrinsic functions?

| Function                   | Example                                       | Result                                                            |
| -------------------------- | --------------------------------------------- | ----------------------------------------------------------------- |
| `Ref`                      | `!Ref OrdersTable`                            | Resource's main ID (table name, bucket name) or a parameter value |
| `Fn::GetAtt`               | `!GetAtt OrdersTable.Arn`                     | An attribute of a resource                                        |
| `Fn::Sub`                  | `!Sub "arn:aws:s3:::${Bucket}/*"`             | String with variables replaced                                    |
| `Fn::Join`                 | `!Join [",", [a, b, c]]`                      | `a,b,c`                                                           |
| `Fn::Select` / `Fn::Split` | `!Select [0, !GetAZs ""]`                     | Pick from a list                                                  |
| `Fn::ImportValue`          | `!ImportValue network-VpcId`                  | Value exported by another stack                                   |
| `Fn::FindInMap`            | `!FindInMap [EnvMap, !Ref Env, InstanceType]` | Value from Mappings                                               |
| `Fn::If`                   | `!If [IsProd, 3, 1]`                          | Value based on a condition                                        |
| `Fn::Base64`               | `!Base64 "#!/bin/bash ..."`                   | Base64 string, used in EC2 UserData                               |
| `Fn::GetAZs`               | `!GetAZs ""`                                  | AZs in the current Region                                         |

Pseudo parameters like `AWS::Region`, `AWS::AccountId`, `AWS::StackName` and `AWS::Partition` are available everywhere.

## 106: How do Parameters, Mappings and Conditions work together?

```yaml
Parameters:
  Env:
    Type: String
    AllowedValues: [dev, prod]
    Default: dev
  LatestAmiId:
    Type: AWS::SSM::Parameter::Value<AWS::EC2::Image::Id>
    Default: /aws/service/ami-amazon-linux-latest/al2023-ami-kernel-default-x86_64

Mappings:
  EnvConfig:
    dev:
      MemorySize: 256
    prod:
      MemorySize: 1024

Conditions:
  IsProd: !Equals [!Ref Env, prod]

Resources:
  Function:
    Type: AWS::Serverless::Function
    Properties:
      MemorySize: !FindInMap [EnvConfig, !Ref Env, MemorySize]
      # ...

  ErrorsAlarm:
    Type: AWS::CloudWatch::Alarm
    Condition: IsProd # only created in prod
    Properties:
      # ...
```

The `AWS::SSM::Parameter::Value<...>` parameter type reads the latest value from Parameter Store at deploy time. It is a common way to always use the latest Amazon Linux 2023 AMI.

## 107: How do you share values between stacks?

Two ways:

1. **Exports and `Fn::ImportValue`** (cross-stack references): stack A exports a value, stack B imports it.

```yaml
# network stack
Outputs:
  VpcId:
    Value: !Ref Vpc
    Export:
      Name: !Sub "${AWS::StackName}-VpcId"
```

```yaml
# app stack
VpcId: !ImportValue network-VpcId
```

Export names must be unique per Region, and you cannot delete or change an export while another stack imports it.

2. **Nested stacks** (`AWS::CloudFormation::Stack`): a parent stack creates child stacks from other templates and passes parameters. Good for reusing a component (for example, a standard ALB setup) and for staying under the 500 resource limit per stack.

Use exports when stacks have separate lifecycles and owners (network team vs app team). Use nested stacks when the parts are deployed together. Parameter Store is a third option that avoids the strong coupling of exports.

## 108: What are change sets and drift detection?

- **Change set**: a preview of what an update will do before you run it: which resources will be added, modified or **replaced**. Replacement matters, because it can delete data (for example, renaming a DynamoDB table replaces it). `sam deploy` creates a change set and asks you to confirm by default.

```bash
aws cloudformation create-change-set --stack-name orders --change-set-name v2 \
  --template-body file://template.yaml --capabilities CAPABILITY_IAM
aws cloudformation describe-change-set --stack-name orders --change-set-name v2
aws cloudformation execute-change-set --stack-name orders --change-set-name v2
```

- **Drift detection**: compares the real resources with the template and shows changes made outside CloudFormation (for example, someone edited a security group in the console).

```bash
aws cloudformation detect-stack-drift --stack-name orders
```

## 109: What are DeletionPolicy and UpdateReplacePolicy?

They control what happens to the real resource when CloudFormation deletes or replaces it.

- `Delete`: delete the resource (default for most resources).
- `Retain`: keep the resource, just remove it from the stack.
- `Snapshot`: take a snapshot before deleting (RDS, EBS, ElastiCache, Redshift, Neptune, DocumentDB).
- `RetainExceptOnCreate`: keep it, unless the stack is rolling back from a failed create.

```yaml
OrdersTable:
  Type: AWS::DynamoDB::Table
  DeletionPolicy: Retain
  UpdateReplacePolicy: Retain
  Properties:
    # ...
```

Always set these on stateful resources (tables, buckets, databases) in production. Note: CloudFormation cannot delete a non-empty S3 bucket, so the delete fails unless you empty it first.

## 110: What happens when a CloudFormation deployment fails?

- **Create fails**: by default the stack rolls back and deletes created resources (`ROLLBACK_COMPLETE`). A stack in that state can only be deleted, not updated. You can use `--disable-rollback` (or `--on-failure DO_NOTHING`) during development to keep the failed resources for debugging.
- **Update fails**: CloudFormation rolls back to the last working state (`UPDATE_ROLLBACK_COMPLETE`).
- **Rollback fails**: the stack ends in `UPDATE_ROLLBACK_FAILED`, usually because a resource was changed or deleted outside CloudFormation. Fix the cause, then run `continue-update-rollback`, optionally skipping the broken resources.

```bash
aws cloudformation continue-update-rollback --stack-name orders \
  --resources-to-skip MyBrokenResource
```

You can also add **rollback triggers**: CloudWatch alarms that CloudFormation watches during and after an update. If an alarm goes off, it rolls back.

## 111: What is a CloudFormation custom resource?

A custom resource lets CloudFormation run your own logic during create, update and delete, for things CloudFormation does not support, or for tasks like seeding a database or emptying a bucket before deletion. CloudFormation calls a Lambda function (or SNS topic) and waits for the function to send a response to a presigned S3 URL.

```yaml
SeedData:
  Type: Custom::SeedData
  Properties:
    ServiceToken: !GetAtt SeedFunction.Arn
    ServiceTimeout: 300
    TableName: !Ref OrdersTable
```

```python
import cfnresponse  # available when the function code is inline (ZipFile)

def handler(event, context):
    try:
        if event["RequestType"] == "Create":
            seed(event["ResourceProperties"]["TableName"])
        cfnresponse.send(event, context, cfnresponse.SUCCESS, {"Message": "done"})
    except Exception as e:
        cfnresponse.send(event, context, cfnresponse.FAILED, {"Error": str(e)})
```

If the function never responds (for example an unhandled exception), the stack waits until the timeout. `ServiceTimeout` lets you lower that from the default of one hour. The CDK has a Provider framework that handles the response part for you.

## 112: What are CloudFormation StackSets?

StackSets deploy the same template to many accounts and/or Regions with one operation. Typical uses: baseline IAM roles, Config rules, logging, or guardrails across an AWS Organization.

- With **service-managed permissions**, StackSets integrate with AWS Organizations and can deploy automatically to new accounts in an OU.
- With **self-managed permissions**, you create the admin and execution roles yourself.
- You control rollout with max concurrent accounts and failure tolerance.

## 113: What is the AWS CDK?

The AWS Cloud Development Kit lets you define infrastructure in TypeScript, Python, Java, C#, or Go. The CDK app synthesizes a CloudFormation template, and CloudFormation deploys it.

Constructs come in three levels:

- **L1** (`CfnBucket`): one-to-one with CloudFormation resources.
- **L2** (`Bucket`): higher-level with good defaults and helper methods like `grantRead`.
- **L3** (patterns): several resources together, like `ApplicationLoadBalancedFargateService`.

```typescript
import * as cdk from "aws-cdk-lib";
import { Construct } from "constructs";
import * as dynamodb from "aws-cdk-lib/aws-dynamodb";
import * as lambda from "aws-cdk-lib/aws-lambda";
import * as apigw from "aws-cdk-lib/aws-apigateway";

export class OrdersStack extends cdk.Stack {
  constructor(scope: Construct, id: string, props?: cdk.StackProps) {
    super(scope, id, props);

    const table = new dynamodb.TableV2(this, "Orders", {
      partitionKey: { name: "orderId", type: dynamodb.AttributeType.STRING },
      removalPolicy: cdk.RemovalPolicy.RETAIN,
    });

    const fn = new lambda.Function(this, "CreateOrder", {
      runtime: lambda.Runtime.NODEJS_22_X,
      architecture: lambda.Architecture.ARM_64,
      handler: "index.handler",
      code: lambda.Code.fromAsset("lambda"),
      environment: { TABLE_NAME: table.tableName },
    });

    table.grantReadWriteData(fn); // creates a least-privilege IAM policy

    new apigw.LambdaRestApi(this, "OrdersApi", { handler: fn });
  }
}
```

CDK v1 reached end of support in 2023. Use CDK v2, where everything is in the single `aws-cdk-lib` package.

## 114: What are the main CDK CLI commands?

```bash
cdk init app --language typescript
cdk bootstrap aws://111122223333/us-east-1   # one time per account/Region
cdk synth                                    # produce the CloudFormation template in cdk.out/
cdk diff                                     # compare with what is deployed
cdk deploy OrdersStack
cdk deploy --hotswap                         # quick code updates for dev, skips CloudFormation where possible
cdk watch                                    # deploy on file change (dev only)
cdk destroy OrdersStack
```

**Bootstrapping** creates the `CDKToolkit` stack with an S3 bucket and ECR repository for assets and IAM roles that the CLI uses to deploy. You must bootstrap every account and Region you deploy to. `cdk.context.json` caches lookups (like VPC IDs or AMIs) so synth is repeatable. Commit it to Git.

## 115: What are Lambda versions and aliases?

- **`$LATEST`**: the editable, unpublished version of the function.
- **Version**: an immutable snapshot of code and configuration, with a number (1, 2, 3...). Its ARN ends with `:3`.
- **Alias**: a named pointer to a version, like `prod` or `live`. You can move it to another version without changing callers.

```bash
aws lambda publish-version --function-name orders-api --description "release 1.4.2"
aws lambda create-alias --function-name orders-api --name prod --function-version 7
aws lambda update-alias --function-name orders-api --name prod --function-version 8
```

Point API Gateway, event sources and other callers at the alias ARN (`...:function:orders-api:prod`), not `$LATEST`. Then a release is just moving the alias, and a rollback is moving it back.

## 116: How do you shift traffic gradually between Lambda versions?

An alias can split traffic between two versions with weights:

```bash
# 90% to version 7, 10% to version 8
aws lambda update-alias --function-name orders-api --name prod \
  --function-version 7 \
  --routing-config '{"AdditionalVersionWeights": {"8": 0.1}}'
```

In practice, let **CodeDeploy** do it. With SAM:

```yaml
CreateOrderFunction:
  Type: AWS::Serverless::Function
  Properties:
    AutoPublishAlias: live
    DeploymentPreference:
      Type: Canary10Percent5Minutes
      Alarms:
        - !Ref CreateOrderErrorsAlarm
      Hooks:
        PreTraffic: !Ref PreTrafficCheckFunction
```

`AutoPublishAlias` publishes a new version on every code change and updates the alias. `DeploymentPreference` creates a CodeDeploy application and deployment group that shifts traffic and rolls back automatically if an alarm fires or the hook fails.

## 117: What deployment configurations does CodeDeploy have for Lambda?

- **Canary**: shift a small percent first, then the rest after a wait. `LambdaCanary10Percent5Minutes`, `LambdaCanary10Percent10Minutes`, `LambdaCanary10Percent15Minutes`, `LambdaCanary10Percent30Minutes`.
- **Linear**: shift equal steps over time. `LambdaLinear10PercentEvery1Minute`, `LambdaLinear10PercentEvery2Minutes`, `LambdaLinear10PercentEvery3Minutes`, `LambdaLinear10PercentEvery10Minutes`.
- **All at once**: `LambdaAllAtOnce`.

(In CodeDeploy they have the `CodeDeployDefault.` prefix. SAM accepts the short names.)

Hooks:

- `BeforeAllowTraffic`: run a test Lambda against the new version before any traffic moves.
- `AfterAllowTraffic`: run checks after all traffic has moved.

A hook function must report its result back:

```python
import boto3

codedeploy = boto3.client("codedeploy")

def handler(event, context):
    status = "Succeeded" if run_smoke_tests() else "Failed"
    codedeploy.put_lifecycle_event_hook_execution_status(
        deploymentId=event["DeploymentId"],
        lifecycleEventHookExecutionId=event["LifecycleEventHookExecutionId"],
        status=status,
    )
```

## 118: How does CodeDeploy work with EC2 and on-premises servers?

The **CodeDeploy agent** runs on each instance. You define a deployment group (by tags or Auto Scaling group), and CodeDeploy pulls a revision (from S3 or GitHub) and runs the steps in `appspec.yml` in the root of the bundle.

```yaml
version: 0.0
os: linux
files:
  - source: /
    destination: /var/www/orders
hooks:
  ApplicationStop:
    - location: scripts/stop.sh
      timeout: 60
  BeforeInstall:
    - location: scripts/install_deps.sh
  AfterInstall:
    - location: scripts/configure.sh
  ApplicationStart:
    - location: scripts/start.sh
  ValidateService:
    - location: scripts/health_check.sh
      timeout: 120
```

Order of events for an in-place deployment: `ApplicationStop` → `DownloadBundle` → `BeforeInstall` → `Install` → `AfterInstall` → `ApplicationStart` → `ValidateService`. With a load balancer, there are also `BeforeBlockTraffic`, `BlockTraffic`, `AfterBlockTraffic`, `BeforeAllowTraffic`, `AllowTraffic`, `AfterAllowTraffic`.

Deployment configs for EC2: `CodeDeployDefault.AllAtOnce`, `HalfAtATime`, `OneAtATime`, or a custom minimum healthy hosts value. You can do **in-place** or **blue/green** (new instances, then switch the load balancer).

Note: `ApplicationStop` runs the script from the **previous** revision, so a broken stop script in the old revision can fail the new deployment.

## 119: How do you do blue/green deployments for ECS?

Options:

1. **ECS built-in blue/green** (added in 2025): set the service deployment strategy to blue/green. ECS starts the new task set, shifts traffic through the ALB/NLB or Service Connect, supports bake time and lifecycle hooks (Lambda), and rolls back automatically. No CodeDeploy needed. Linear and canary strategies were added later as well.
2. **CodeDeploy blue/green**: the older way. The deployment group uses two target groups and a production listener (plus an optional test listener). The `appspec.yaml` for ECS:

```yaml
version: 0.0
Resources:
  - TargetService:
      Type: AWS::ECS::Service
      Properties:
        TaskDefinition: "arn:aws:ecs:us-east-1:111122223333:task-definition/orders-api:12"
        LoadBalancerInfo:
          ContainerName: "app"
          ContainerPort: 8080
Hooks:
  - AfterAllowTestTraffic: "arn:aws:lambda:us-east-1:111122223333:function:orders-smoke-test"
```

Traffic options: `CodeDeployDefault.ECSAllAtOnce`, `ECSCanary10Percent5Minutes`, `ECSLinear10PercentEvery1Minutes`, and others.

The default ECS rolling update (with `minimumHealthyPercent` and `maximumPercent`) plus the **deployment circuit breaker** with rollback is enough for many services.

## 120: What deployment strategies should you know?

| Strategy                 | How it works                                    | Downtime              | Rollback             | Cost                 |
| ------------------------ | ----------------------------------------------- | --------------------- | -------------------- | -------------------- |
| All at once (in-place)   | Update everything at the same time              | Yes                   | Redeploy old version | Lowest               |
| Rolling                  | Update in batches                               | No, but less capacity | Redeploy             | Low                  |
| Rolling with extra batch | Add new instances first, then roll              | No                    | Redeploy             | A bit more           |
| Immutable                | New instances in a new group, swap when healthy | No                    | Terminate new group  | Double during deploy |
| Blue/green               | Full new environment, switch traffic            | No                    | Switch back          | Double during deploy |
| Canary                   | Small percent first, then the rest              | No                    | Shift back           | Low                  |
| Linear                   | Equal steps over time                           | No                    | Shift back           | Low                  |

During rolling and canary deployments, two versions run at the same time, so the new code must be backward compatible with the old one (database schema, message formats, APIs).

## 121: What is AWS Elastic Beanstalk?

Elastic Beanstalk is a PaaS: you upload your code, and it creates and manages EC2 instances, an Auto Scaling group, a load balancer, monitoring and logs. You still have full access to the underlying resources.

- **Application**: a container for environments and versions.
- **Application version**: a specific code bundle in S3.
- **Environment**: a running copy of a version (for example `orders-prod`).
- **Environment tiers**: **web server** (behind a load balancer) or **worker** (reads from SQS).
- Platforms: Node.js, Python, Java (Corretto, Tomcat), .NET, PHP, Ruby, Go, Docker, on Amazon Linux 2023.

```bash
eb init orders --platform node.js --region us-east-1
eb create orders-prod
eb deploy
eb logs
eb setenv DB_HOST=orders.cluster-xyz.us-east-1.rds.amazonaws.com
```

## 122: What deployment policies does Elastic Beanstalk support?

- **All at once**: deploy to all instances at once. Fast, but downtime. Good for dev.
- **Rolling**: deploy in batches. Capacity drops while a batch is updating.
- **Rolling with additional batch**: launches a new batch first, so full capacity stays.
- **Immutable**: launches a full set of new instances in a temporary Auto Scaling group, moves them in when healthy, then terminates the old ones. Safest, rollback is quick.
- **Traffic splitting**: canary testing. Sends a percent of traffic to new instances for a set time, then completes or rolls back.

**Blue/green** is not a policy. You clone the environment, deploy to the clone, test it, then use **Swap environment URLs** (a CNAME swap). Beware of DNS caching during the switch, and keep the database outside the environment (an RDS instance created inside an EB environment is deleted with it).

## 123: How do you customize an Elastic Beanstalk environment?

- **`.ebextensions/*.config`** (YAML or JSON): option settings, packages, files, commands, and extra CloudFormation resources.

```yaml
# .ebextensions/01-options.config
option_settings:
  aws:elasticbeanstalk:application:environment:
    NODE_ENV: production
  aws:autoscaling:asg:
    MinSize: 2
    MaxSize: 6
  aws:elasticbeanstalk:command:
    DeploymentPolicy: Immutable
```

- **`.platform/`** (Amazon Linux 2 and 2023 platforms): platform hooks and proxy config.
  - `.platform/hooks/prebuild/`, `predeploy/`, `postdeploy/`: shell scripts run during deployment.
  - `.platform/nginx/conf.d/*.conf`: extra nginx config.
- **`Procfile`**: how to start your app, for example `web: node server.js`.
- **`env.yaml`**: environment settings for `eb create`.

Settings precedence (highest first): settings applied directly to the environment (console, CLI, API), saved configurations, `.ebextensions`, then defaults.

## 124: What is an Elastic Beanstalk worker environment?

A worker environment runs background jobs. Elastic Beanstalk installs a daemon on each instance that reads messages from an SQS queue and POSTs each one to your app at `http://localhost/` (or a path you choose). If your app returns `200`, the daemon deletes the message. Otherwise it is retried, and can go to a DLQ.

For scheduled jobs, add a `cron.yaml` file:

```yaml
version: 1
cron:
  - name: "nightly-report"
    url: "/tasks/nightly-report"
    schedule: "0 2 * * *"
```

A common pattern: the web tier puts long tasks (like video processing) in SQS, and the worker tier processes them.

## 125: What is AWS CodeBuild and what does a buildspec look like?

CodeBuild is a managed build service. It runs your build commands in a fresh container and you pay per build minute. The steps are in `buildspec.yml` at the repo root.

```yaml
version: 0.2

env:
  variables:
    NODE_ENV: production
  parameter-store:
    API_BASE_URL: /orders/prod/api-base-url
  secrets-manager:
    NPM_TOKEN: prod/ci/npm:token
  exported-variables:
    - IMAGE_TAG

phases:
  install:
    runtime-versions:
      nodejs: 22
    commands:
      - npm ci
  pre_build:
    commands:
      - npm run lint
      - npm test
      - export IMAGE_TAG=$(echo $CODEBUILD_RESOLVED_SOURCE_VERSION | cut -c1-7)
  build:
    commands:
      - npm run build
      - sam build
  post_build:
    commands:
      - sam package --s3-bucket $ARTIFACT_BUCKET --output-template-file packaged.yaml

reports:
  unit-tests:
    files: ["reports/junit.xml"]
    file-format: JUNITXML

artifacts:
  files:
    - packaged.yaml

cache:
  paths:
    - "node_modules/**/*"
```

Phases run in order: `install`, `pre_build`, `build`, `post_build`. If a command fails in `build`, `post_build` still runs (useful for cleanup), unless you set `on-failure: ABORT`.

## 126: How do you speed up and secure CodeBuild builds?

Speed:

- **Caching**: S3 cache (shared across hosts) or local cache (Docker layer, source, custom) on the build host.
- Pick a bigger compute type, or ARM (Graviton) images when they work for you.
- **Reserved capacity fleets** to avoid the time to provision a new build host.
- Use **batch builds** to run builds in parallel.

Security:

- Get secrets from Secrets Manager or Parameter Store in the `env` section. Never put them in plaintext variables.
- Give the CodeBuild service role only what the build needs.
- Run the build in a VPC if it needs private resources (it then needs a NAT or VPC endpoints for internet and AWS APIs).

You can test a buildspec locally with the CodeBuild local agent (`codebuild_build.sh`) before pushing.

## 127: What is AWS CodePipeline?

CodePipeline is a continuous delivery service. A pipeline has **stages** (Source, Build, Test, Deploy, Approval). Each stage has **actions** that run in sequence or in parallel. Actions pass **artifacts** to each other through an S3 artifact bucket.

Supported action providers include: CodeConnections (GitHub, GitLab, Bitbucket), CodeCommit, S3, ECR (source); CodeBuild, Jenkins (build and test); CloudFormation, CodeDeploy, ECS, Elastic Beanstalk, S3, Lambda (deploy); manual approval; invoking a Lambda function.

**V2 pipelines** (the default type now) add:

- Triggers with filters on branches, tags and file paths, plus pull request events.
- Pipeline-level variables you can set when you start a run.
- Execution modes: `SUPERSEDED` (default), `QUEUED`, `PARALLEL`.
- Stage-level rollback and conditions (for example, roll back if an alarm fires).
- Built-in actions like the "Commands" action to run shell commands without a separate CodeBuild project.

## 128: How do you connect a pipeline to GitHub, GitLab or Bitbucket?

Use **AWS CodeConnections** (renamed from CodeStar Connections in 2024). You create a connection, finish the OAuth handshake in the console once, and reference the connection ARN in the pipeline source action.

```yaml
- Name: Source
  Actions:
    - Name: GitHub
      ActionTypeId:
        Category: Source
        Owner: AWS
        Provider: CodeStarSourceConnection
        Version: "1"
      Configuration:
        ConnectionArn: arn:aws:codeconnections:us-east-1:111122223333:connection/abc-123
        FullRepositoryId: my-org/orders-service
        BranchName: main
        OutputArtifactFormat: CODE_ZIP
      OutputArtifacts:
        - Name: SourceOutput
```

The provider name in the action is still `CodeStarSourceConnection`. Note also that AWS CodeCommit was closed to new customers in 2024, then returned to full availability in late 2025, so you may see either Git hosting choice in real projects.

## 129: What is AWS CodeArtifact?

CodeArtifact is a managed package repository for npm, PyPI, Maven, Gradle, NuGet, Swift, Ruby gems, Cargo and generic packages. It can proxy public repositories (npmjs, PyPI, Maven Central) through upstream connections, so you keep a cached copy and control what is used.

```bash
aws codeartifact login --tool npm --domain my-company --repository shared --domain-owner 111122223333
npm install
npm publish   # publish a private package
```

```bash
aws codeartifact login --tool pip --domain my-company --repository shared
pip install internal-utils
```

The login token is valid for up to 12 hours. In CodeBuild, run the login command in the `install` phase.

## 130: How do you push images to Amazon ECR?

```bash
ACCOUNT=111122223333
REGION=us-east-1
REPO=orders-api

aws ecr create-repository --repository-name $REPO \
  --image-scanning-configuration scanOnPush=true \
  --image-tag-mutability IMMUTABLE

aws ecr get-login-password --region $REGION | \
  docker login --username AWS --password-stdin $ACCOUNT.dkr.ecr.$REGION.amazonaws.com

docker build -t $REPO:1.4.2 .
docker tag $REPO:1.4.2 $ACCOUNT.dkr.ecr.$REGION.amazonaws.com/$REPO:1.4.2
docker push $ACCOUNT.dkr.ecr.$REGION.amazonaws.com/$REPO:1.4.2
```

Good practices:

- Use unique tags (version or Git commit SHA) and **immutable tags**, not `latest`.
- Turn on **image scanning** (basic or enhanced with Amazon Inspector).
- Add **lifecycle policies** to delete old or untagged images.
- Use **pull through cache** rules for public images (Docker Hub, ECR Public), so builds do not depend on external rate limits.

## 131: What are the main Amazon ECS concepts?

- **Cluster**: a logical group of capacity.
- **Task definition**: a JSON blueprint for one or more containers: image, CPU, memory, ports, environment, secrets, IAM roles, logging. Each change creates a new revision.
- **Task**: a running copy of a task definition.
- **Service**: keeps a desired number of tasks running, replaces failed ones, and registers them with a load balancer.
- **Launch type / capacity provider**: **Fargate** (serverless, no instances to manage), **EC2** (you manage the instances), or **ECS Managed Instances** (AWS manages EC2 instances for you).

```json
{
  "family": "orders-api",
  "networkMode": "awsvpc",
  "requiresCompatibilities": ["FARGATE"],
  "cpu": "512",
  "memory": "1024",
  "runtimePlatform": {
    "cpuArchitecture": "ARM64",
    "operatingSystemFamily": "LINUX"
  },
  "executionRoleArn": "arn:aws:iam::111122223333:role/ecsTaskExecutionRole",
  "taskRoleArn": "arn:aws:iam::111122223333:role/orders-api-task",
  "containerDefinitions": [
    {
      "name": "app",
      "image": "111122223333.dkr.ecr.us-east-1.amazonaws.com/orders-api:1.4.2",
      "portMappings": [{ "containerPort": 8080 }],
      "logConfiguration": {
        "logDriver": "awslogs",
        "options": {
          "awslogs-group": "/ecs/orders-api",
          "awslogs-region": "us-east-1",
          "awslogs-stream-prefix": "app"
        }
      },
      "healthCheck": {
        "command": [
          "CMD-SHELL",
          "curl -f http://localhost:8080/health || exit 1"
        ],
        "interval": 30,
        "retries": 3
      }
    }
  ]
}
```

## 132: When would you choose containers on ECS/Fargate over Lambda?

Choose containers when:

- Work runs longer than 15 minutes, or the service runs all the time.
- You need more than 10 GB of memory, or specific CPU, or GPU (with EC2).
- You have an existing app (Spring Boot, Django, .NET) that you do not want to rewrite into functions.
- Traffic is steady and high, where always-on tasks can be cheaper than per-request pricing.
- You need long-lived connections, like WebSockets handled directly, or a background process that keeps state in memory.

Choose Lambda when traffic is spiky or low, work is event-driven and short, and you want zero server management and scale to zero.

## 133: How do API Gateway deployments and canary releases work?

For REST APIs, changes to resources and methods do nothing until you **create a deployment** and associate it with a stage. HTTP APIs can use **auto-deploy** on a stage.

```bash
aws apigateway create-deployment --rest-api-id a1b2c3d4e5 --stage-name prod --description "v1.5"
```

**Canary release** on a REST API stage: send a percent of traffic to a new deployment while the rest uses the current one. Canary requests can use their own stage variables (for example pointing to a new Lambda alias) and are logged separately. When happy, promote the canary.

```bash
aws apigateway create-deployment --rest-api-id a1b2c3d4e5 --stage-name prod \
  --canary-settings '{"percentTraffic": 10, "useStageCache": false}'
```

## 134: How do you manage dev, test and prod environments?

Common practices:

- Use **separate AWS accounts** per environment (managed with AWS Organizations and Control Tower). This isolates permissions, limits and costs.
- Use **the same template** for every environment, with parameters for the differences (instance sizes, domain names, log levels).
- Keep config in **Parameter Store** or **AppConfig** under paths like `/orders/prod/...`, and secrets in **Secrets Manager**.
- Use a **pipeline** to promote the same build artifact from dev to test to prod, instead of building again for each environment.
- Use `samconfig.toml` environments or CDK stages:

```toml
# samconfig.toml
version = 0.1

[dev.deploy.parameters]
stack_name = "orders-dev"
parameter_overrides = "Env=dev"
capabilities = "CAPABILITY_IAM"
resolve_s3 = true

[prod.deploy.parameters]
stack_name = "orders-prod"
parameter_overrides = "Env=prod"
capabilities = "CAPABILITY_IAM"
resolve_s3 = true
```

```bash
sam deploy --config-env prod
```

## 135: What is AWS AppConfig and how do you use feature flags?

AWS AppConfig (part of Systems Manager) manages application configuration and feature flags that can change without a redeploy. It supports validators (JSON Schema or Lambda), gradual **deployment strategies** (for example 20% every 2 minutes), and automatic rollback if a CloudWatch alarm fires.

Feature flag profile example:

```json
{
  "flags": { "new_checkout": { "name": "New checkout" } },
  "values": { "new_checkout": { "enabled": true } },
  "version": "1"
}
```

In Lambda, the **AppConfig Agent Lambda extension** caches the config locally and polls for updates:

```python
import json
import urllib.request

URL = "http://localhost:2772/applications/orders/environments/prod/configurations/feature-flags"

def lambda_handler(event, context):
    with urllib.request.urlopen(URL) as resp:
        flags = json.loads(resp.read())
    if flags["new_checkout"]["enabled"]:
        return new_checkout(event)
    return old_checkout(event)
```

On containers and EC2, use the AppConfig Agent or the `StartConfigurationSession` and `GetLatestConfiguration` APIs.

## 136: What is AWS Amplify?

Amplify is a set of tools for building and hosting web and mobile apps.

- **Amplify Hosting**: CI/CD and hosting for static sites and SSR frameworks (Next.js, Nuxt, and others). Connect a Git repo, and each push builds and deploys. Each branch can get its own environment, with preview URLs for pull requests.
- **Amplify Gen 2**: define the backend in TypeScript (auth with Cognito, data with AppSync and DynamoDB, storage with S3, functions with Lambda). It is built on the CDK, and each developer can get a personal cloud sandbox (`npx ampx sandbox`).
- **Amplify libraries**: client libraries for auth, API calls, storage, and UI components.

```typescript
// amplify/data/resource.ts (Gen 2)
import { a, defineData, type ClientSchema } from "@aws-amplify/backend";

const schema = a.schema({
  Todo: a
    .model({ content: a.string(), done: a.boolean() })
    .authorization((allow) => [allow.owner()]),
});

export type Schema = ClientSchema<typeof schema>;
export const data = defineData({ schema });
```

## 137: How do you package Lambda functions with dependencies?

- **Python**: install dependencies into the package folder and zip it. For packages with native code (like `numpy`, `cryptography`), install wheels for the Lambda platform, or build with `sam build --use-container`.

```bash
pip install -r requirements.txt -t package/ \
  --platform manylinux2014_aarch64 --only-binary=:all: --python-version 3.13
cp app.py package/
cd package && zip -r ../function.zip . && cd ..
aws lambda update-function-code --function-name orders-api --zip-file fileb://function.zip
```

- **Node.js**: bundle and tree-shake with esbuild (SAM supports `BuildMethod: esbuild` in `Metadata`), so the package is small and cold starts are faster.

```yaml
CreateOrderFunction:
  Type: AWS::Serverless::Function
  Properties:
    Runtime: nodejs22.x
    Handler: app.handler
  Metadata:
    BuildMethod: esbuild
    BuildProperties:
      Minify: true
      Target: es2022
      EntryPoints:
        - app.ts
```

- Packages over 50 MB zipped must be uploaded to S3 first. Over 250 MB unzipped, use a container image.
- Match the architecture: `arm64` (Graviton, usually cheaper and faster) or `x86_64`.

## 138: How do you test serverless applications?

- **Unit tests**: test business logic without AWS. Mock SDK calls.

```javascript
import { mockClient } from "aws-sdk-client-mock";
import { DynamoDBDocumentClient, GetCommand } from "@aws-sdk/lib-dynamodb";
import { handler } from "../src/get-order.mjs";

const ddbMock = mockClient(DynamoDBDocumentClient);

test("returns 404 when order is missing", async () => {
  ddbMock.on(GetCommand).resolves({});
  const res = await handler({ pathParameters: { id: "o-404" } });
  expect(res.statusCode).toBe(404);
});
```

```python
import boto3
from moto import mock_aws

@mock_aws
def test_save_order():
    boto3.client("dynamodb", region_name="us-east-1").create_table(
        TableName="Orders",
        KeySchema=[{"AttributeName": "orderId", "KeyType": "HASH"}],
        AttributeDefinitions=[{"AttributeName": "orderId", "AttributeType": "S"}],
        BillingMode="PAY_PER_REQUEST",
    )
    save_order({"orderId": "o-1"})
    ...
```

- **Local runs**: `sam local invoke` and `sam local start-api` for a quick check. They do not emulate IAM or other services fully.
- **Integration tests in the cloud**: deploy to a dev or ephemeral stack (`sam sync`, `cdk deploy`) and run tests against real services. AWS recommends this because mocks hide permission and configuration problems.
- **API Gateway mock integrations**: return fixed responses so frontend teams can work before the backend is ready.
- **Lambda test events** in the console, including shareable test events stored in the EventBridge schema registry.

## 139: How do you add tests and approvals to a pipeline?

A typical pipeline:

1. **Source**: pull from Git.
2. **Build**: CodeBuild runs unit tests, lint, security scans, and builds artifacts.
3. **Deploy to test**: CloudFormation or SAM deploy.
4. **Integration tests**: CodeBuild runs tests against the test environment. Fail the pipeline if they fail.
5. **Manual approval**: someone reviews before production. Can send an SNS notification with a link.
6. **Deploy to prod**: with a canary or linear strategy and alarms.

```yaml
- Name: Approve
  Actions:
    - Name: ManualApproval
      ActionTypeId:
        Category: Approval
        Owner: AWS
        Provider: Manual
        Version: "1"
      Configuration:
        NotificationArn: !Ref ApprovalTopic
        CustomData: "Check the test report before approving."
```

## 140: How do you roll back a failed deployment automatically?

- **CodeDeploy**: enable automatic rollback on deployment failure and on CloudWatch alarm. If the error rate alarm fires during a canary, traffic goes back to the old version.
- **SAM DeploymentPreference**: same thing, with `Alarms` and hooks.
- **CloudFormation**: rolls back failed updates. Add rollback triggers with alarms.
- **ECS**: deployment circuit breaker with `rollback: true`, or the alarms setting on the service deployment configuration. Blue/green rolls back on alarm or hook failure.
- **Elastic Beanstalk**: immutable and traffic splitting deployments roll back if health checks fail.
- **CodePipeline V2**: stage-level rollback, triggered on failure or by a condition.

```json
"deploymentConfiguration": {
  "deploymentCircuitBreaker": { "enable": true, "rollback": true },
  "alarms": { "alarmNames": ["orders-api-5xx"], "enable": true, "rollback": true }
}
```

Good alarms to use: 5xx error rate, Lambda `Errors`, latency p99, and business metrics like failed payments.

## 141: What is CloudFormation Git sync?

Git sync links a CloudFormation stack to a Git repository (GitHub, GitLab, Bitbucket, through CodeConnections). You keep the template and a deployment file in the repo, and when you push to the tracked branch, CloudFormation updates the stack. It can also comment on pull requests with the planned changes.

```yaml
# deployment-file.yaml
template-file-path: ./template.yaml
parameters:
  Env: prod
tags:
  team: orders
```

It is a simple GitOps option for infrastructure when you do not need a full pipeline with tests and approvals.

## 142: How do you bootstrap software on EC2 with CloudFormation?

- **UserData**: a script that runs on the first boot.
- **cfn-init**: reads `AWS::CloudFormation::Init` metadata and installs packages, writes files, and starts services in a declarative way.
- **cfn-signal**: tells CloudFormation whether setup succeeded. Use it with a **CreationPolicy** so the stack waits for the signal.
- **cfn-hup**: watches for metadata changes and re-runs `cfn-init` on updates.

```yaml
WebServer:
  Type: AWS::EC2::Instance
  CreationPolicy:
    ResourceSignal:
      Timeout: PT10M
  Metadata:
    AWS::CloudFormation::Init:
      config:
        packages:
          dnf:
            nginx: []
        services:
          systemd:
            nginx:
              enabled: true
              ensureRunning: true
  Properties:
    ImageId: !Ref LatestAmiId
    InstanceType: t4g.small
    UserData:
      Fn::Base64: !Sub |
        #!/bin/bash
        /opt/aws/bin/cfn-init -v --stack ${AWS::StackName} --resource WebServer --region ${AWS::Region}
        /opt/aws/bin/cfn-signal -e $? --stack ${AWS::StackName} --resource WebServer --region ${AWS::Region}
```

If no signal arrives before the timeout, the resource fails and the stack rolls back.

## 143: What are CloudFormation dynamic references?

Dynamic references read values from Parameter Store or Secrets Manager at deploy time, so secrets are not written in the template or passed as parameters.

```yaml
Database:
  Type: AWS::RDS::DBInstance
  Properties:
    MasterUsername: "{{resolve:secretsmanager:prod/orders/db:SecretString:username}}"
    MasterUserPassword: "{{resolve:secretsmanager:prod/orders/db:SecretString:password}}"

Function:
  Type: AWS::Lambda::Function
  Properties:
    Environment:
      Variables:
        TABLE_NAME: "{{resolve:ssm:/orders/prod/table-name}}"
```

Supported forms: `ssm` (String/StringList), `ssm-secure` (SecureString, only for some resource properties), and `secretsmanager`. For RDS, an even better option is `ManageMasterUserPassword: true`, so RDS creates and rotates the secret itself.

## 144: How do you deploy across multiple accounts with CodePipeline?

Usual setup: a **tools account** holds the pipeline, and it deploys into dev, test and prod accounts.

1. In each target account, create a role that the pipeline can assume (trust the tools account), plus a CloudFormation execution role.
2. Use a **customer managed KMS key** for the artifact bucket, and let the target account roles use it. The default `aws/s3` key cannot be shared across accounts.
3. Add a bucket policy on the artifact bucket that allows the target account roles to read.
4. In the deploy action, set `RoleArn` to the cross-account role.

```yaml
- Name: DeployProd
  RoleArn: arn:aws:iam::333333333333:role/pipeline-cross-account
  ActionTypeId:
    Category: Deploy
    Owner: AWS
    Provider: CloudFormation
    Version: "1"
  Configuration:
    ActionMode: CREATE_UPDATE
    StackName: orders-prod
    TemplatePath: BuildOutput::packaged.yaml
    RoleArn: arn:aws:iam::333333333333:role/cfn-exec
    Capabilities: CAPABILITY_IAM,CAPABILITY_AUTO_EXPAND
```

CDK Pipelines does most of this for you if you use the CDK.

## 145: How do you deploy a static website on S3 and CloudFront?

1. Create a private S3 bucket (Block Public Access on).
2. Create a CloudFront distribution with the bucket as origin, using **Origin Access Control**.
3. Add an ACM certificate (in us-east-1) and an alternate domain name, plus a Route 53 alias record.
4. Upload files and invalidate the cache.

```bash
npm run build
aws s3 sync ./dist s3://my-site-content --delete \
  --cache-control "public,max-age=31536000,immutable" --exclude "index.html"
aws s3 cp ./dist/index.html s3://my-site-content/index.html \
  --cache-control "no-cache"
aws cloudfront create-invalidation --distribution-id E1ABCDEF2GHIJ --paths "/index.html"
```

Using content hashes in file names (like `app.3f9a1c.js`) means you only need to invalidate `index.html`. For single page apps, add a custom error response or a CloudFront Function so unknown paths return `index.html`. Amplify Hosting is a simpler alternative that does all of this for you.

## 146: What do `aws cloudformation package` and `sam package` do?

Templates often point to local code, like `CodeUri: src/`. CloudFormation cannot read your local disk, so `package`:

1. Zips local code and files.
2. Uploads them to S3 (or ECR for images).
3. Writes a new template where local paths are replaced with S3 URIs.

```bash
aws cloudformation package --template-file template.yaml \
  --s3-bucket my-artifacts --output-template-file packaged.yaml

aws cloudformation deploy --template-file packaged.yaml \
  --stack-name orders --capabilities CAPABILITY_IAM CAPABILITY_AUTO_EXPAND
```

`sam deploy` packages automatically. `CAPABILITY_IAM` (or `CAPABILITY_NAMED_IAM` for named IAM resources) is required when the template creates IAM resources, and `CAPABILITY_AUTO_EXPAND` when it uses macros or nested apps.

## 147: How do you protect production stacks from accidental changes?

- **Termination protection**: the stack cannot be deleted until it is turned off.

```bash
aws cloudformation update-termination-protection --enable-termination-protection --stack-name orders-prod
```

- **Stack policy**: a JSON document that blocks updates to certain resources. Once set, all resources are protected unless allowed.

```json
{
  "Statement": [
    {
      "Effect": "Allow",
      "Action": "Update:*",
      "Principal": "*",
      "Resource": "*"
    },
    {
      "Effect": "Deny",
      "Action": ["Update:Replace", "Update:Delete"],
      "Principal": "*",
      "Resource": "LogicalResourceId/OrdersTable"
    }
  ]
}
```

- `DeletionPolicy: Retain` and `UpdateReplacePolicy: Retain` on stateful resources.
- Deletion protection on the resources themselves (DynamoDB `DeletionProtectionEnabled`, RDS `DeletionProtection`).
- Deploy only through a pipeline, and limit who can change production in IAM.
- Review change sets for `Replacement: True` before you execute them.

## 148: How do you deal with Lambda runtime deprecations and updates?

AWS deprecates runtimes when the language version reaches end of life (for example Node.js 18 and Python 3.9 in 2025). After deprecation, you stop getting security patches and later cannot create or update functions with that runtime.

What to do:

- Keep a list of runtimes in use (AWS Health and Trusted Advisor send notices, and you can list functions by runtime).
- Upgrade to the newer runtime (for example `nodejs22.x`, `python3.13`, `java21`), run tests, and redeploy.
- Use **runtime management controls**: `Auto` (default, AWS applies patch updates), `FunctionUpdate` (updates when you deploy), or `Manual` (pin a runtime version, mostly for rollback if a patch breaks you).

```bash
aws lambda list-functions --query "Functions[?Runtime=='python3.9'].FunctionName"
```

For OS-only runtimes, use `provided.al2023` instead of `provided.al2`.

## 149: What gets frozen when you publish a Lambda version?

A published version is immutable. It includes:

- The function code (or image digest).
- Runtime and handler.
- Environment variables.
- Memory, timeout, ephemeral storage, architecture.
- Layers, VPC config, and most other settings.

So if you change an environment variable on `$LATEST`, existing versions still use the old value. You need to publish a new version and move the alias.

Settings that are not part of the version: aliases, reserved concurrency (set on the function), triggers that point to an alias, and resource-based policies (set per version or alias). Provisioned concurrency is set on a version or alias, not on `$LATEST`.

## 150: Describe a CI/CD flow for a serverless application.

An example for a SAM-based service:

1. A developer opens a pull request. A CodeBuild job (or GitHub Actions) runs lint, unit tests and `sam validate --lint`.
2. After merge to `main`, CodePipeline (V2, triggered by the branch) starts.
3. **Build stage**: CodeBuild runs `sam build` and `sam package`, and stores `packaged.yaml` as the artifact.
4. **Deploy to dev/test**: a CloudFormation action creates a change set and executes it in the test account.
5. **Test stage**: CodeBuild runs integration tests against the test API.
6. **Approval**: manual approval (optional).
7. **Deploy to prod**: CloudFormation deploy in the prod account. Inside the template, `AutoPublishAlias` and `DeploymentPreference: Canary10Percent5Minutes` make CodeDeploy shift traffic and watch alarms.
8. If alarms fire, CodeDeploy rolls back traffic to the previous version automatically.

The same artifact is promoted through every environment. Only parameters change.

---

# Domain 4: Troubleshooting and Optimization

## 151: What are the main parts of Amazon CloudWatch?

- **Metrics**: time series data. AWS services publish metrics automatically (Lambda `Invocations`, `Errors`, `Duration`, `Throttles`; SQS `ApproximateAgeOfOldestMessage`; and so on). You can publish your own.
- **Logs**: log groups and log streams. Lambda, ECS, API Gateway and others send logs here.
- **Logs Insights**: a query language for searching and aggregating logs.
- **Alarms**: watch a metric (or a metric math expression) and act when it crosses a threshold: SNS notifications, Auto Scaling, EC2 actions, Systems Manager actions.
- **Dashboards**: charts for metrics and log queries.
- **Other features**: Application Signals (APM), Synthetics (canaries), RUM (real user monitoring), Container Insights, Lambda Insights, anomaly detection, and Contributor Insights.

## 152: How do you publish a custom metric?

Use `PutMetricData`. Each metric has a namespace, name, dimensions, value and unit. Standard resolution is 1 minute. High resolution (`StorageResolution: 1`) keeps data per second, useful for alarms that react within 10 or 30 seconds.

```python
import boto3

cloudwatch = boto3.client("cloudwatch")

cloudwatch.put_metric_data(
    Namespace="OrdersService",
    MetricData=[{
        "MetricName": "OrdersPlaced",
        "Dimensions": [
            {"Name": "Environment", "Value": "prod"},
            {"Name": "Channel", "Value": "mobile"},
        ],
        "Value": 1,
        "Unit": "Count",
        "StorageResolution": 60,
    }],
)
```

Each unique combination of dimensions is a separate metric (and costs money), so do not use high-cardinality values like user ID as a dimension. Calling `PutMetricData` from Lambda on every request adds latency. The Embedded Metric Format is usually a better choice there.

## 153: What is the CloudWatch Embedded Metric Format (EMF)?

EMF lets you create metrics by writing a JSON log line in a special format. CloudWatch extracts the metrics from the logs asynchronously. There is no API call in your code path, so it is fast and cannot be throttled, and you also keep the high-cardinality details in the log for searching.

```json
{
  "_aws": {
    "Timestamp": 1761217200000,
    "CloudWatchMetrics": [
      {
        "Namespace": "OrdersService",
        "Dimensions": [["Environment"]],
        "Metrics": [{ "Name": "ProcessingTime", "Unit": "Milliseconds" }]
      }
    ]
  },
  "Environment": "prod",
  "ProcessingTime": 182,
  "orderId": "o-991",
  "customerId": "c-123"
}
```

With Powertools for AWS Lambda (Python):

```python
from aws_lambda_powertools import Metrics
from aws_lambda_powertools.metrics import MetricUnit

metrics = Metrics(namespace="OrdersService", service="orders")

@metrics.log_metrics
def lambda_handler(event, context):
    metrics.add_dimension(name="Environment", value="prod")
    metrics.add_metric(name="OrdersPlaced", unit=MetricUnit.Count, value=1)
    metrics.add_metadata(key="orderId", value=event["orderId"])
```

## 154: How do you search logs with CloudWatch Logs Insights?

Logs Insights has its own query language (and also supports OpenSearch PPL and SQL). It auto-discovers fields in JSON logs and Lambda logs.

Last 50 errors:

```
fields @timestamp, @requestId, @message
| filter @message like /ERROR/
| sort @timestamp desc
| limit 50
```

Lambda duration and memory per 5 minutes:

```
filter @type = "REPORT"
| stats avg(@duration) as avgMs,
        pct(@duration, 99) as p99Ms,
        max(@maxMemoryUsed / 1000 / 1000) as maxMemMB
  by bin(5m)
```

Count cold starts:

```
filter @type = "REPORT" and ispresent(@initDuration)
| stats count() as coldStarts, avg(@initDuration) as avgInitMs by bin(1h)
```

Top error types from JSON logs:

```
filter level = "ERROR"
| stats count() as errors by errorType
| sort errors desc
```

You can save queries, add results to dashboards, and query many log groups at once.

## 155: What is a metric filter?

A metric filter turns matching log events into a CloudWatch metric, so you can alarm on things that only appear in logs.

```bash
aws logs put-metric-filter \
  --log-group-name /aws/lambda/payments \
  --filter-name PaymentDeclined \
  --filter-pattern '{ $.event = "payment_declined" }' \
  --metric-transformations \
      metricName=PaymentDeclined,metricNamespace=Payments,metricValue=1,defaultValue=0
```

Filters only apply to new log events, not past ones. For past data, use Logs Insights. Another related feature is **subscription filters**, which stream log events to Lambda, Kinesis, Firehose or OpenSearch in real time.

## 156: How do CloudWatch alarms work?

An alarm watches one metric or a metric math expression over a period, and has three states: `OK`, `ALARM`, and `INSUFFICIENT_DATA`.

Important settings:

- **Period** and **evaluation periods**, plus **datapoints to alarm** (for example 3 out of 5 periods, to avoid noise).
- **Missing data treatment**: `missing`, `notBreaching`, `breaching`, or `ignore`. For error metrics that only report when there are errors, `notBreaching` is usually right.
- **Actions**: SNS, Auto Scaling, EC2, Systems Manager OpsItems or incidents, Lambda (direct alarm actions).

```bash
aws cloudwatch put-metric-alarm \
  --alarm-name orders-api-errors \
  --namespace AWS/Lambda --metric-name Errors \
  --dimensions Name=FunctionName,Value=orders-api \
  --statistic Sum --period 60 \
  --evaluation-periods 5 --datapoints-to-alarm 3 \
  --threshold 5 --comparison-operator GreaterThanOrEqualToThreshold \
  --treat-missing-data notBreaching \
  --alarm-actions arn:aws:sns:us-east-1:111122223333:oncall
```

**Composite alarms** combine other alarms with AND/OR/NOT, to reduce alert noise (for example, only page when both the error rate and latency are bad).

## 157: How should you log from Lambda?

- Use **structured JSON logs** with a level, a message, and context fields (request ID, order ID, user ID).
- Turn on Lambda **advanced logging controls**: JSON log format, application log level and system log level filters, and a custom log group name. With JSON format, Lambda adds `requestId` and timestamps for you.
- Set **log retention** on the log group (the default is to keep logs forever).
- Do not log secrets or full personal data.

```yaml
CreateOrderFunction:
  Type: AWS::Serverless::Function
  Properties:
    LoggingConfig:
      LogFormat: JSON
      ApplicationLogLevel: INFO
      SystemLogLevel: WARN
      LogGroup: /orders/prod/create-order
```

With Powertools:

```python
from aws_lambda_powertools import Logger

logger = Logger(service="orders")

@logger.inject_lambda_context(log_event=False, correlation_id_path="requestContext.requestId")
def lambda_handler(event, context):
    logger.append_keys(order_id=event.get("orderId"))
    logger.info("Creating order")
```

## 158: What is AWS X-Ray and what are its main concepts?

X-Ray is a distributed tracing service. It shows how a request travels through your services, where time is spent, and where errors happen.

- **Trace**: the whole path of one request, identified by a trace ID (passed in the `X-Amzn-Trace-Id` header).
- **Segment**: the work done by one service (for example, your Lambda function).
- **Subsegment**: a smaller part inside a segment, like a DynamoDB call, an HTTP call, or a block of your code.
- **Service map / trace map**: a graph of services with latency and error rates.
- **Annotations**: indexed key-value pairs you can filter on.
- **Metadata**: non-indexed data for extra details.
- **Sampling**: X-Ray does not record every request. The default rule records the first request each second and 5% of the rest.

X-Ray data is viewed in the CloudWatch console (traces, trace map, Application Signals).

## 159: What is the difference between annotations and metadata in X-Ray?

|                           | Annotations                               | Metadata                                    |
| ------------------------- | ----------------------------------------- | ------------------------------------------- |
| Indexed                   | Yes                                       | No                                          |
| Can filter traces by them | Yes (`annotation.customer_tier = "gold"`) | No                                          |
| Value types               | String, number, boolean                   | Any object                                  |
| Limit                     | 50 per trace                              | No small limit (counts toward segment size) |

Use annotations for things you will search on (customer tier, order type, error code). Use metadata for debug data (full request, response).

```python
from aws_lambda_powertools import Tracer

tracer = Tracer(service="orders")

@tracer.capture_method
def charge_card(order):
    tracer.put_annotation(key="customer_tier", value=order["tier"])
    tracer.put_metadata(key="order", value=order)
    ...

@tracer.capture_lambda_handler
def lambda_handler(event, context):
    return charge_card(event)
```

Filter expression in the console:

```
annotation.customer_tier = "gold" AND responsetime > 2
```

## 160: How do you enable tracing in Lambda, API Gateway and containers?

- **Lambda**: turn on active tracing (`Tracing: Active`). The execution role needs `xray:PutTraceSegments` and `xray:PutTelemetryRecords` (`AWSXRayDaemonWriteAccess`).
- **API Gateway**: enable X-Ray tracing on the REST API stage.
- **ECS/EKS/EC2**: run the X-Ray daemon or the CloudWatch agent / ADOT collector as a sidecar, and instrument your code.
- **SQS, SNS, Step Functions, EventBridge**: pass the trace header along, so traces continue across services.

```yaml
Globals:
  Function:
    Tracing: Active
  Api:
    TracingEnabled: true
```

For code instrumentation, AWS now recommends **OpenTelemetry** through the **AWS Distro for OpenTelemetry (ADOT)** or the CloudWatch agent, instead of the X-Ray SDKs. AWS announced that the X-Ray SDKs and daemon are moving to maintenance mode. Powertools Tracer still works and is widely used in Lambda.

## 161: When do you use CloudWatch, X-Ray and CloudTrail?

- **CloudWatch**: "How is my system doing?" Metrics, logs, alarms, dashboards.
- **X-Ray / Application Signals**: "Why is this request slow, and which service failed?" Distributed tracing and service maps.
- **CloudTrail**: "Who changed what in my account, and when?" API call auditing.

Example: users report errors. A CloudWatch alarm shows a 5xx spike. X-Ray traces show the errors come from DynamoDB throttling inside the payments function. CloudTrail shows someone changed the table's provisioned capacity an hour ago.

## 162: What is CloudWatch Application Signals?

Application Signals is the APM feature in CloudWatch. With OpenTelemetry-based auto-instrumentation (for Java, Python, Node.js, .NET on EKS, ECS, EC2 and Lambda), it collects standard metrics (calls, latency, errors, faults) per service and per operation, builds a service map, links metrics to traces and logs, and lets you define **SLOs** (service level objectives) such as "99.9% of requests under 300 ms".

It saves you from building dashboards by hand and makes it easy to go from "the SLO is breached" to the exact slow traces.

## 163: What causes Lambda cold starts and how can you reduce them?

A cold start happens when Lambda has to create a new execution environment: download code, start the runtime, run init code. It happens on the first request, when scaling up, and after the environment is recycled.

Ways to reduce it:

- Keep the package small: bundle and tree-shake (esbuild), remove unused dependencies, import only the SDK clients you need.
- Do less work at init: lazy-load things that are rarely used.
- Pick a faster runtime when possible (Node.js, Python, Go start faster than Java or .NET without tuning).
- Use more memory, since CPU scales with memory and init gets faster.
- Use **SnapStart** for Java, Python and .NET.
- Use **provisioned concurrency** for latency-critical endpoints.
- For Java, use tiered compilation settings (`JAVA_TOOL_OPTIONS=-XX:+TieredCompilation -XX:TieredStopAtLevel=1`) or native images.

Remember that init time is now billed for on-demand functions, so reducing init also saves money.

## 164: What is the difference between reserved concurrency and provisioned concurrency?

- **Reserved concurrency**: sets aside part of the account's concurrency for one function, and also **caps** that function at that number. No extra cost. Use it to protect a downstream system (for example a database that allows only 50 connections) or to make sure a critical function always has capacity. Setting it to 0 stops all invocations, which is a quick "off switch".
- **Provisioned concurrency**: keeps a number of environments **initialized and warm**, so requests do not get cold starts. Costs money while it is configured. Set it on an alias or version, and you can scale it on a schedule or with Application Auto Scaling.

```bash
aws lambda put-function-concurrency --function-name payments --reserved-concurrent-executions 50

aws lambda put-provisioned-concurrency-config --function-name checkout \
  --qualifier live --provisioned-concurrent-executions 20
```

Lambda also has a scaling rate limit: each function can add up to 1,000 concurrent executions every 10 seconds.

## 165: What is Lambda SnapStart?

SnapStart reduces cold starts by taking a snapshot of the initialized execution environment (memory and disk) when you publish a version. New environments are resumed from the cached snapshot instead of running init again.

- Supported for Java 11 and later, Python 3.12 and later, and .NET 8 and later.
- Works on published versions and aliases, not `$LATEST`.
- Not compatible with provisioned concurrency, EFS, or ephemeral storage above 512 MB.
- Anything unique created during init (random seeds, unique IDs, temporary credentials, network connections) is shared by all environments restored from the snapshot. Use runtime hooks to refresh them.

```python
from snapshot_restore_py import register_after_restore

@register_after_restore
def reconnect():
    global db
    db = open_db_connection()
```

```yaml
JavaFunction:
  Type: AWS::Serverless::Function
  Properties:
    Runtime: java21
    AutoPublishAlias: live
    SnapStart:
      ApplyOn: PublishedVersions
```

## 166: How do you choose the right memory size for a Lambda function?

Lambda gives CPU in proportion to memory (a full vCPU at 1,769 MB, up to 6 vCPUs at 10,240 MB). More memory costs more per millisecond, but the function may finish much faster, so the total cost can go down.

Approach:

1. Look at `Max Memory Used` in the `REPORT` log lines. Keep a safety margin.
2. Run **AWS Lambda Power Tuning** (an open source Step Functions tool) to test different memory sizes and see the cost and speed of each.
3. Check **AWS Compute Optimizer**, which recommends memory sizes based on real usage.
4. Try **arm64 (Graviton)**, which is about 20% cheaper per GB-second and often faster.

CPU-heavy work (image processing, compression) benefits a lot from more memory. I/O-bound work (waiting on APIs) usually does not.

## 167: A Lambda function returns `TooManyRequestsException` (429). What is happening?

The function is **throttled**: it hit a concurrency limit. Possible causes:

- The account's Regional concurrency limit (1,000 by default) is used up by all functions together.
- The function's **reserved concurrency** is too low.
- The scaling rate limit was hit during a sudden burst.
- Provisioned concurrency is fully used and the alias has spillover limits.

How the caller is affected:

- **Synchronous**: the caller gets the 429 and must retry (API Gateway returns it to the client).
- **Asynchronous**: Lambda retries for up to 6 hours, then sends to the DLQ/destination.
- **SQS event source**: messages go back to the queue and are retried, and may end up in the DLQ.

Fixes: check the `Throttles` and `ConcurrentExecutions` metrics, raise reserved concurrency or request a higher account limit, smooth traffic with SQS, set maximum concurrency on SQS event sources, or reduce duration (lower duration means less concurrency for the same traffic, because concurrency = requests per second x average duration in seconds).

## 168: A Lambda function times out. How do you troubleshoot it?

The log shows `Task timed out after X seconds`. Steps:

1. Check where time goes with X-Ray or timing logs. Usually it is a slow downstream call.
2. **Lambda in a VPC calling the internet or an AWS API** without a NAT gateway or VPC endpoint hangs until timeout. This is a very common cause.
3. **Database connections**: too many connections, or waiting on a lock. Use RDS Proxy.
4. **SDK timeouts**: set connect and read timeouts on SDK and HTTP clients lower than the function timeout, so you get a clear error instead of a silent timeout.
5. **Event loop not empty (Node.js)**: an unawaited promise or open handle. Make sure every promise is awaited.
6. Raise the memory (more CPU) if the work is CPU-bound, or raise the timeout if the work really takes longer.

```python
from botocore.config import Config
import boto3

s3 = boto3.client("s3", config=Config(connect_timeout=2, read_timeout=5, retries={"max_attempts": 3}))
```

Also remember that API Gateway has its own timeout (29 seconds by default for REST APIs, 30 seconds for HTTP APIs), so a function with a 60 second timeout behind API Gateway still fails at the API.

## 169: How do you read a Lambda `REPORT` log line?

```
REPORT RequestId: 3f1a... Duration: 1834.52 ms Billed Duration: 2269 ms Memory Size: 512 MB Max Memory Used: 498 MB Init Duration: 434.21 ms
```

- **Duration**: time spent in the handler.
- **Billed Duration**: what you pay for (now includes init for on-demand functions, rounded up to 1 ms).
- **Memory Size / Max Memory Used**: here the function used 498 of 512 MB. That is very close to the limit, and an out-of-memory error is likely soon. Raise the memory.
- **Init Duration**: present only on cold starts.

If you see `Runtime exited with error: signal: killed` or `Runtime.OutOfMemory`, the function ran out of memory. If you see `Status: timeout`, it hit the timeout.

## 170: A Lambda function in a VPC cannot reach S3 or an external API. Why?

Lambda functions attached to a VPC only have private IPs. Even in a public subnet they do not get a public IP, so they cannot use the internet gateway.

Fixes:

- **For AWS services**: add VPC endpoints. A gateway endpoint for S3 and DynamoDB (free), interface endpoints for others (SQS, Secrets Manager, KMS, STS, and so on). Make sure endpoint security groups allow HTTPS from the Lambda security group, and private DNS is enabled.
- **For the internet**: put the function in private subnets whose route table sends `0.0.0.0/0` to a **NAT gateway** in a public subnet.
- Check that the Lambda security group allows outbound traffic, and that network ACLs allow return traffic.
- If the function does not need private resources, do not attach it to a VPC at all.

## 171: What is Lambda Insights?

Lambda Insights is a CloudWatch feature, added as a Lambda extension (layer), that collects system-level metrics per function: CPU time, memory used, network, disk, and cold starts. It shows them in a ready-made dashboard and helps find memory leaks or CPU bottlenecks that the standard metrics do not show.

```yaml
Layers:
  - !Sub arn:aws:lambda:${AWS::Region}:580247275435:layer:LambdaInsightsExtension-Arm64:<version>
Policies:
  - CloudWatchLambdaInsightsExecutionRolePolicy
```

(Look up the current layer version for your Region and architecture in the docs.) It has a cost per function and per log volume, so turn it on where you need it.

## 172: Messages in an SQS queue processed by Lambda are processed more than once. Why?

Common causes:

1. **Visibility timeout too short**: if the function runs longer than the visibility timeout, the message becomes visible again and another invocation picks it up. AWS recommends setting the queue's visibility timeout to **at least 6 times the function timeout** (plus the batching window).
2. **Whole batch fails**: one bad message makes the function throw, so all messages in the batch return to the queue, including the ones already processed. Use `ReportBatchItemFailures`.
3. **Standard queues are at-least-once**: duplicates can happen even when everything is correct. Make processing idempotent.
4. **Function errors or timeouts** after side effects already happened (for example after charging a card).

Related settings:

- Set a DLQ with a reasonable `maxReceiveCount` (5 or more) so poison messages do not loop forever.
- Use **maximum concurrency** on the event source mapping to limit how many functions process the queue, instead of reserved concurrency (which causes throttling and extra retries).

```bash
aws lambda update-event-source-mapping --uuid 1a2b3c... \
  --scaling-config MaximumConcurrency=20 \
  --function-response-types ReportBatchItemFailures
```

## 173: A Lambda function reading from Kinesis or DynamoDB Streams is falling behind. How do you fix it?

Signs: the `IteratorAge` metric keeps growing.

Causes and fixes:

- **Poison record**: by default, Lambda retries a failed batch until it succeeds or the data expires, and the shard is blocked meanwhile. Fix with:
  - `BisectBatchOnFunctionError`: split the batch in half to find the bad record.
  - `MaximumRetryAttempts` and `MaximumRecordAgeInSeconds`: stop retrying after a limit.
  - **On-failure destination** (SQS, SNS, S3) to keep details of skipped records.
  - `ReportBatchItemFailures` to checkpoint at the failed record.
- **Not enough parallelism**: raise `ParallelizationFactor` (up to 10 concurrent batches per shard, order is still kept per partition key), or add shards.
- **Slow function**: optimize code, raise memory, increase `BatchSize`.
- **Many consumers sharing read throughput**: use enhanced fan-out for Kinesis.

```bash
aws lambda update-event-source-mapping --uuid 4d5e6f... \
  --bisect-batch-on-function-error \
  --maximum-retry-attempts 3 \
  --maximum-record-age-in-seconds 3600 \
  --parallelization-factor 4 \
  --destination-config '{"OnFailure":{"Destination":"arn:aws:sqs:us-east-1:111122223333:stream-failures"}}'
```

## 174: What is exponential backoff with jitter and how do SDK retries work?

When a call fails with a throttling or temporary error (429, 500, 503, `ThrottlingException`, `ProvisionedThroughputExceededException`), retrying right away makes things worse. **Exponential backoff** waits longer after each failure (100 ms, 200 ms, 400 ms...). **Jitter** adds randomness so many clients do not retry at the same moment.

The AWS SDKs already do this. You can tune it:

```python
import boto3
from botocore.config import Config

config = Config(retries={"max_attempts": 6, "mode": "adaptive"})
dynamodb = boto3.client("dynamodb", config=config)
```

```javascript
import { DynamoDBClient } from "@aws-sdk/client-dynamodb";

const client = new DynamoDBClient({ maxAttempts: 6, retryMode: "adaptive" });
```

Retry modes:

- `legacy`: old behavior (boto3 default for a long time).
- `standard`: consistent retry rules across SDKs, 3 attempts by default, with a retry quota.
- `adaptive`: standard plus client-side rate limiting when throttled. Good for batch jobs.

For your own code (for example calling a third-party API):

```python
import random
import time

def call_with_backoff(fn, max_attempts=5, base=0.1, cap=5.0):
    for attempt in range(max_attempts):
        try:
            return fn()
        except TemporaryError:
            if attempt == max_attempts - 1:
                raise
            time.sleep(random.uniform(0, min(cap, base * 2 ** attempt)))  # full jitter
```

Only retry errors that can succeed later. Do not retry `400 ValidationException` or `403 AccessDenied`.

## 175: DynamoDB returns `ProvisionedThroughputExceededException`. What do you do?

The table or an index is getting more reads or writes than its capacity, or one partition is too hot.

Check:

- `ReadThrottleEvents`, `WriteThrottleEvents`, `ConsumedReadCapacityUnits`, `ConsumedWriteCapacityUnits` for the table **and every GSI**. A throttled GSI throttles writes to the base table.
- **CloudWatch Contributor Insights for DynamoDB** to find the most accessed (hot) keys.

Fixes:

- Use **auto scaling** or switch to **on-demand** mode.
- Fix hot keys: better partition key design or write sharding.
- Cache hot reads with DAX or ElastiCache.
- Use eventually consistent reads (half the cost of strongly consistent).
- Make sure the SDK retries with backoff (it does by default).
- Spread batch jobs over time instead of running them in a burst.

DynamoDB has adaptive capacity, which moves capacity to hot partitions automatically, but a single partition still has a hard limit of 3,000 RCUs and 1,000 WCUs per second.

## 176: How do you make DynamoDB reads faster and cheaper?

- Use `Query` or `GetItem` instead of `Scan`.
- Use `ProjectionExpression` to return only needed attributes (smaller responses, although capacity is calculated on the full item).
- Keep items small. Store large blobs in S3 and keep a pointer.
- Use **sparse indexes**: a GSI only includes items that have the index key, so you can index only "open orders" for example.
- Use `BatchGetItem` to fetch many items in one call.
- Use eventually consistent reads where possible.
- For big scans (exports or analytics), use **parallel scan** with `Segment` and `TotalSegments`, or better, **Export to S3** and query with Athena, which uses no table capacity.

```python
def scan_segment(segment, total):
    resp = table.scan(Segment=segment, TotalSegments=total, ProjectionExpression="pk, status")
    ...

# run scan_segment(0, 4), scan_segment(1, 4), ... in parallel threads
```

## 177: When is DAX not a good fit?

- When the app needs **strongly consistent reads** (DAX passes them through to DynamoDB with no caching benefit).
- When the workload is **write-heavy** and reads are rare.
- When reads are spread evenly over a huge key space, so the cache hit rate is low.
- When the client is not in a VPC (DAX runs in a VPC).
- When you need to cache data from other sources too (use ElastiCache).

Also note that DAX's item cache and query cache are separate. An update through DAX refreshes the item cache, but cached query results can stay stale until their TTL expires.

## 178: What do common API Gateway error codes mean?

| Code                      | Usual cause                                                                                                                                                                                        |
| ------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 400 Bad Request           | Request validation failed, bad JSON                                                                                                                                                                |
| 401 Unauthorized          | Missing or invalid token for a Cognito or Lambda authorizer                                                                                                                                        |
| 403 Forbidden             | IAM denied, authorizer returned Deny, WAF blocked it, resource policy denied it, or **"Missing Authentication Token"**, which usually means the path or method does not exist (wrong URL or stage) |
| 404 Not Found             | No matching route (HTTP API)                                                                                                                                                                       |
| 413                       | Payload over the 10 MB API Gateway limit                                                                                                                                                           |
| 429 Too Many Requests     | Throttled by stage, method, usage plan or account limits                                                                                                                                           |
| 500 Internal Server Error | Bad integration config, mapping template errors, or missing permission for API Gateway to invoke Lambda                                                                                            |
| 502 Bad Gateway           | Lambda returned an invalid proxy response (for example `body` not a string), or the function crashed                                                                                               |
| 503 Service Unavailable   | Backend unavailable                                                                                                                                                                                |
| 504 Gateway Timeout       | Integration took longer than the integration timeout                                                                                                                                               |

Turn on **execution logging** and **access logging** for the stage to see the details. The `IntegrationLatency` and `Latency` metrics help separate backend time from API Gateway overhead.

## 179: What is the API Gateway integration timeout and can it be changed?

- **REST APIs**: the default and maximum used to be 29 seconds. Since June 2024, you can raise the timeout above 29 seconds for **Regional and private** REST APIs (edge-optimized stay at 29 seconds). Raising it may require lowering your account-level throttle quota.
- **HTTP APIs**: up to 30 seconds.
- **WebSocket APIs**: 29 seconds per integration call.

For work that takes longer, do not keep the client waiting. Use an async pattern: accept the request, return `202 Accepted` with a job ID, process in the background (SQS, Step Functions), and let the client poll a status endpoint or get notified through WebSockets. For large responses, consider Lambda response streaming through a function URL.

## 180: How does API Gateway caching work?

REST API stages can have a cache (0.5 GB to 237 GB). Responses are cached by method and by the cache keys you choose (path, query string parameters, headers). Default TTL is 300 seconds, max 3,600, and 0 disables it.

- Enable it per stage and override per method.
- Only `GET` methods are cached by default.
- Clients can bypass the cache with `Cache-Control: max-age=0`, but only if they are allowed `execute-api:InvalidateCache`. Turn on "Require authorization" so anonymous users cannot flush your cache.
- Encrypt cache data if it is sensitive.
- Watch `CacheHitCount` and `CacheMissCount`.

HTTP APIs have no built-in cache. Put CloudFront in front of them if you need caching.

## 181: How does throttling work in API Gateway?

Limits are applied in this order (the most specific one that applies wins, but you can never exceed the account limit):

1. **Account level per Region**: 10,000 requests per second with a burst of 5,000 (soft limits).
2. **Stage and method level**: you can set lower limits per stage or per method.
3. **Usage plan / API key level** (REST APIs): per client limits and quotas.

Throttling uses a token bucket: the rate is how fast tokens refill and the burst is the bucket size. When there are no tokens, clients get `429 Too Many Requests` and should retry with backoff.

Throttling also protects your backend. For example, if Lambda reserved concurrency is 100 and average duration is 0.5 s, the function can handle about 200 requests per second, so a stage limit of 200 rps avoids Lambda throttles.

## 182: How do you make CloudFront caching work well?

- Use **cache policies** to choose the cache key (which headers, cookies and query strings) and TTLs. Fewer values in the key means more cache hits.
- Use **origin request policies** to send extra values to the origin without adding them to the cache key.
- Set `Cache-Control` headers at the origin (for example `max-age=31536000, immutable` for versioned assets, `no-cache` for HTML).
- Use **versioned file names** instead of invalidations where possible. Invalidations are fine for a few paths, and the first 1,000 paths per month are free.
- Watch `CacheHitRate` in CloudFront metrics and the cache statistics reports.
- Turn on **Origin Shield** to reduce load on the origin from many edge locations.
- Use compression (gzip and Brotli).

## 183: How do you improve S3 performance?

- S3 supports at least **3,500 PUT/COPY/POST/DELETE** and **5,500 GET/HEAD** requests per second **per partitioned prefix**. Spread keys across prefixes to scale further (for example `logs/2026/10/23/...` or a hash prefix). S3 scales prefixes automatically over time, so you may see short `503 Slow Down` errors during sudden spikes. Retry with backoff.
- **Multipart upload** for large objects (parallel parts, retry only failed parts).
- **Byte-range fetches** to download parts of an object in parallel, or only the part you need.
- **S3 Transfer Acceleration** for uploads from far away clients (uses CloudFront edge locations).
- **CloudFront** in front of S3 for frequently read content.
- **S3 Express One Zone** for very low latency and high request rates in a single AZ.
- With SSE-KMS, use **Bucket Keys** to avoid hitting KMS limits.

```python
s3.get_object(Bucket="big-data", Key="huge.csv", Range="bytes=0-1048575")  # first 1 MB
```

## 184: Your code gets `AccessDenied` from S3. What do you check?

1. **Identity policy**: does the role allow the action on the right ARN? `s3:ListBucket` needs the bucket ARN (`arn:aws:s3:::bucket`), while `s3:GetObject` needs the object ARN (`arn:aws:s3:::bucket/*`).
2. **Bucket policy**: is there an explicit `Deny` (for example a VPC endpoint condition, TLS condition, or an encryption requirement)?
3. **KMS**: if the object uses SSE-KMS, the role needs `kms:Decrypt` (for reads) or `kms:GenerateDataKey` (for writes) on the key, and the key policy must allow it.
4. **Cross-account**: both the bucket policy and the caller's IAM policy must allow it. With ACLs disabled, the bucket owner owns all objects.
5. **Block Public Access**: blocks public policies.
6. **Organization SCPs or RCPs**, permission boundaries, or session policies.
7. **VPC endpoint policy** if the request goes through an endpoint.
8. For a missing object, S3 returns `403` instead of `404` if you do not have `s3:ListBucket`.

Tools: the error message often says which policy type denied the request, CloudTrail shows the denied call, and **IAM Policy Simulator** or Access Analyzer can help.

## 185: How can you read only part of the data in a large S3 object?

- **Byte-range GET** (`Range` header): get specific bytes, useful for fixed-size records or file formats with an index (Parquet footers, ZIP directories).
- **Amazon Athena**: run SQL over files in S3 (CSV, JSON, Parquet), paying per data scanned. Use columnar formats and partitions to scan less.

Note: **S3 Select** is no longer available to new customers (since July 2024). AWS suggests Athena or client-side filtering instead. If an interviewer asks about it, mention it as legacy.

## 186: An ElastiCache cache is not helping performance. What do you look at?

- **Cache hit rate** (`CacheHitRate`, or `CacheHits` and `CacheMisses`): low hit rate means the wrong data is cached, keys are too specific, or TTLs are too short.
- **Evictions**: the cache is full and items are removed early. Scale up, add shards, or reduce what you cache. Check `DatabaseMemoryUsagePercentage`.
- **CPU**: `EngineCPUUtilization` high means the engine thread is busy, often from expensive commands like `KEYS *` or large sorted set operations.
- **Connections**: `CurrConnections` and `NewConnections`. Lambda functions should reuse connections created at init.
- **Network**: large values use a lot of bandwidth. Compress or split them.
- **Stale data**: add TTLs and invalidate or update keys on writes.
- **Hot keys**: one key used by everyone can overload one shard. Use read replicas or local caching for it.

ElastiCache Serverless removes most capacity planning, if that fits the workload.

## 187: How do you troubleshoot an SQS-based system where messages pile up?

Metrics to check:

- `ApproximateNumberOfMessagesVisible`: backlog size.
- `ApproximateAgeOfOldestMessage`: how far behind consumers are.
- `ApproximateNumberOfMessagesNotVisible`: messages in flight.
- `NumberOfMessagesSent` vs `NumberOfMessagesDeleted`: producer vs consumer rate.
- DLQ `ApproximateNumberOfMessagesVisible`: failing messages.

Causes and fixes:

- Consumers too slow or too few: add consumers, raise Lambda maximum concurrency, increase batch size, optimize processing.
- Consumers failing and messages returning to the queue: check logs and the DLQ.
- Lambda throttled: check `Throttles` and concurrency settings.
- FIFO queue with few message groups: only one message per group is processed at a time, so use more distinct group IDs.
- Empty receives costing money: use long polling.

## 188: How do you debug a failed Step Functions execution?

- Open the execution in the console. The **graph view** and **event history** show each state's input, output, errors and retries.
- Check the error and cause in the `TaskFailed` or `ExecutionFailed` event.
- Use the **TestState API** to test a single state (with its input and IAM role) without running the whole state machine.
- Use **redrive** to restart a failed Standard workflow from the failed step, instead of starting over.
- Turn on CloudWatch Logs for the state machine (required to see Express workflow details) and X-Ray tracing.
- Add `Retry` with backoff for temporary errors (`Lambda.ServiceException`, `Lambda.TooManyRequestsException`) and `Catch` to handle failures cleanly.

```bash
aws stepfunctions redrive-execution \
  --execution-arn arn:aws:states:us-east-1:111122223333:execution:order-flow:abc123
```

## 189: A CloudFormation stack update fails. How do you find the cause?

1. Look at the **Events** tab (or `describe-stack-events`). Find the **first** `CREATE_FAILED` or `UPDATE_FAILED` event. Later failures are usually just side effects of the rollback.
2. Common causes:
   - Missing IAM permission for the deploying role (or missing `CAPABILITY_IAM`).
   - A resource name already exists (names must be unique, for example S3 buckets).
   - Service quota reached (for example VPCs, EIPs).
   - Invalid property values, or a property that requires replacement on a resource with a fixed name.
   - Custom resource did not respond.
   - Drift: someone changed or deleted a resource manually.
3. Use change sets before updating, and turn on the **"Detect root cause"** feature in the console for failed operations.
4. For `UPDATE_ROLLBACK_FAILED`, fix the resource, then `continue-update-rollback`.

```bash
aws cloudformation describe-stack-events --stack-name orders \
  --query "StackEvents[?contains(ResourceStatus, 'FAILED')].[LogicalResourceId,ResourceStatusReason]" \
  --output table
```

## 190: A CodeDeploy deployment to EC2 fails. What do you check?

- The **deployment events** in the console show which lifecycle hook failed on which instance.
- The **CodeDeploy agent log** on the instance: `/var/log/aws/codedeploy-agent/codedeploy-agent.log`, and the script output in `/opt/codedeploy-agent/deployment-root/<group-id>/<deployment-id>/logs/scripts.log`.
- Is the agent installed and running? (`sudo systemctl status codedeploy-agent`)
- Does the **instance profile** allow reading the revision from S3?
- Does the **CodeDeploy service role** have the right permissions?
- Script problems: missing execute permission, wrong path, script timeout too short, a script that returns non-zero.
- `ApplicationStop` failing because the old revision's script is broken. You can redeploy with "ignore ApplicationStop failures".
- Health checks failing in `ValidateService` or in the load balancer.

## 191: A CodeBuild build fails. How do you troubleshoot?

- Read the **build logs** (CloudWatch Logs or S3), and check which phase failed.
- `COMMAND_EXECUTION_ERROR`: a command returned non-zero. Run it locally in the same image to reproduce, or use the CodeBuild local agent.
- `Access denied` errors: the CodeBuild service role is missing permissions (S3 artifacts, ECR push, Secrets Manager, KMS).
- Cannot reach the internet or AWS APIs: the build runs in a VPC without NAT or endpoints.
- Docker builds fail: the project needs **privileged mode** to run Docker.
- Out of memory or disk: use a larger compute type.
- Timeouts: raise the build timeout or add caching.
- **Session Manager** debugging: add `codebuild-breakpoint` in the buildspec to pause the build and connect to the container.

## 192: An ECS task keeps stopping or never starts. How do you troubleshoot?

- Check the task's **stopped reason** in the console or with `describe-tasks`:

```bash
aws ecs describe-tasks --cluster prod --tasks <task-id> \
  --query "tasks[0].{reason:stoppedReason, containers:containers[].{name:name, exit:exitCode, reason:reason}}"
```

- `CannotPullContainerError`: wrong image name or tag, the execution role cannot read ECR, or no network path to ECR (private subnet without NAT or ECR/S3 endpoints).
- `ResourceInitializationError`: often secrets cannot be read (execution role or KMS permissions) or there is no network path to Secrets Manager.
- Exit code `137`: the container was killed, often out of memory. Raise the memory limit.
- Exit code `1` or other: application error. Check the container logs in CloudWatch Logs.
- Tasks stopped by ELB health checks: the health check path is wrong, the app starts too slowly (set `healthCheckGracePeriodSeconds`), or the security group blocks the load balancer.
- Use **ECS Exec** to open a shell in a running container for debugging.

## 193: An Application Load Balancer returns 5xx errors. How do you tell where they come from?

- `HTTPCode_ELB_5XX_Count`: generated by the load balancer itself.
  - **502 Bad Gateway**: the target closed the connection or sent an invalid response, or a Lambda target returned a bad response.
  - **503 Service Unavailable**: no healthy targets registered.
  - **504 Gateway Timeout**: the target did not respond within the idle timeout (default 60 seconds).
- `HTTPCode_Target_5XX_Count`: returned by your application. Look at the app logs.
- `UnHealthyHostCount` and target group health check details show why targets are unhealthy.
- ALB **access logs** (to S3) and **connection logs** show the details for each request.

One common cause of random 502s: the app's keep-alive timeout is shorter than the ALB idle timeout. Make the app's keep-alive timeout longer than the ALB's.

## 194: How do you follow a single request across many services?

- Generate or accept a **correlation ID** at the entry point (API Gateway request ID, or a `X-Correlation-Id` header) and pass it to every downstream call, message attribute and log line.
- Use **distributed tracing** (X-Ray or OpenTelemetry). The trace ID is passed automatically through supported services (API Gateway, Lambda, SQS, SNS, EventBridge, Step Functions) and SDK calls.
- Use **structured logs** with the same field names in every service, so one Logs Insights query across several log groups finds everything for one ID.

```
fields @timestamp, @log, level, message
| filter correlation_id = "c0ffee-1234"
| sort @timestamp asc
```

## 195: Lambda functions exhaust the database connection limit. How do you fix it?

Each Lambda execution environment opens its own connection, so 500 concurrent invocations can mean 500 connections, more than a small RDS instance allows.

Fixes:

- Use **RDS Proxy**. It pools and shares connections, handles failover faster, and supports IAM authentication and Secrets Manager.
- Open the connection outside the handler and reuse it.
- Limit the function's concurrency (reserved concurrency or SQS maximum concurrency) to what the database can handle.
- For Aurora, consider the **RDS Data API** (HTTP-based, no connection management), or **Aurora DSQL** or DynamoDB for serverless-friendly data stores.

```python
import os
import boto3
import pymysql

def connect():
    token = boto3.client("rds").generate_db_auth_token(
        DBHostname=os.environ["PROXY_ENDPOINT"], Port=3306, DBUsername="app_user"
    )
    return pymysql.connect(
        host=os.environ["PROXY_ENDPOINT"], user="app_user", password=token,
        database="orders", ssl={"ca": "/opt/rds-ca.pem"},  # CA bundle shipped in a layer
    )

conn = connect()  # reused across invocations

def lambda_handler(event, context):
    with conn.cursor() as cur:
        cur.execute("SELECT status FROM orders WHERE id = %s", (event["id"],))
        return cur.fetchone()
```

## 196: How can a developer lower the cost of a serverless application?

- **Lambda**: right-size memory, use arm64, cut init time (it is billed now), avoid waiting on other services inside a function (use Step Functions or async patterns instead), and filter events at the event source mapping so you do not pay to invoke a function that ignores the event.
- **API Gateway**: use HTTP APIs when you do not need REST API features. Cache where possible.
- **DynamoDB**: pick on-demand vs provisioned based on traffic, use TTL to delete old data for free, avoid scans, and use the Standard-IA table class for rarely accessed tables.
- **S3**: lifecycle rules, Intelligent-Tiering, and abort incomplete multipart uploads.
- **CloudWatch Logs**: set retention, lower log levels in production, and use the Infrequent Access log class for logs you rarely query.
- **Step Functions**: Express workflows for high-volume short jobs.
- **Data transfer**: VPC endpoints instead of NAT gateway for AWS service traffic.
- Tag resources and check **Cost Explorer** and budgets.

Event filtering example (only invoke for new orders):

```yaml
Events:
  Stream:
    Type: DynamoDB
    Properties:
      Stream: !GetAtt OrdersTable.StreamArn
      StartingPosition: LATEST
      FilterCriteria:
        Filters:
          - Pattern: '{"eventName": ["INSERT"]}'
```

## 197: What are CloudWatch Synthetics canaries?

Canaries are scripts (Node.js with Puppeteer or Playwright, or Python with Selenium) that run on a schedule and check your endpoints and user flows from the outside, like a real user: load a page, log in, call an API. They record availability, latency, screenshots and HAR files, and you can set alarms on them.

Use them to find problems before customers do, for example a broken login page at 3 AM when there is no real traffic. A simple API check:

```javascript
const synthetics = require("Synthetics");

const apiCanary = async () => {
  await synthetics.executeHttpStep("Get health", {
    hostname: "api.example.com",
    method: "GET",
    path: "/health",
    protocol: "https:",
  });
};

exports.handler = async () => apiCanary();
```

## 198: What is Lambda recursive loop detection?

Lambda detects some infinite loops, for example a function that writes to an SQS queue that triggers the same function, or a function writing to the S3 bucket that triggers it. After about 16 invocations in the same chain, Lambda stops the loop and sends the event to a DLQ or on-failure destination if configured. It currently covers SQS, SNS, S3 and Lambda (direct invocation via the SDK).

It is on by default. You can turn it off per function (`RecursiveLoop: Allow`) if the recursion is intended, but it is better to fix the design: write output to a different bucket or prefix, use a different queue, or add a guard field in the message.

```bash
aws lambda put-function-recursion-config --function-name image-resizer --recursive-loop Terminate
```

## 199: How do you debug Lambda functions locally and in the cloud?

Locally:

- **Unit tests** with mocked SDK clients for most logic.
- `sam local invoke` and `sam local start-api` run the function in a Lambda-like Docker container. Add `-d 5858` (or another port) to attach a debugger from VS Code or IntelliJ.
- The **AWS Toolkit** for VS Code and JetBrains can run and debug functions locally and remotely.

In the cloud:

- `sam logs --tail` or `aws logs tail /aws/lambda/<name> --follow` to watch logs live.
- `sam remote invoke` to send a test event to the deployed function.
- **Lambda console test events** for quick checks.
- **X-Ray / Application Signals** traces to find slow or failing calls.
- Temporarily raise the log level to `DEBUG` using advanced logging controls, without changing code.

```bash
sam local invoke CreateOrderFunction -e events/create.json -d 5858
aws logs tail /aws/lambda/orders-api --follow --since 10m
```

## 200: What are good practices for using the AWS SDKs efficiently?

- **Create clients once** and reuse them (outside the Lambda handler).
- **Keep connections alive**. SDK for JavaScript v3 reuses connections by default. In other languages, check HTTP client settings.
- **Use batch APIs**: `SendMessageBatch`, `DeleteMessageBatch`, `BatchWriteItem`, `PutRecords`, `PutEvents` with several entries.
- **Use paginators** instead of writing your own loops, and stop early when you have what you need.
- **Set timeouts and retry settings** that match your function timeout.
- **Run independent calls in parallel** (`Promise.all` in Node.js, threads or asyncio in Python).
- **Import only the clients you need** (modular SDK v3) to keep bundles small.
- **Cache** results that rarely change (config, secrets, lookup tables).
- **Handle errors by type**: retry throttling and 5xx, fail fast on 4xx.

```javascript
import { SQSClient, SendMessageBatchCommand } from "@aws-sdk/client-sqs";

const sqs = new SQSClient({ maxAttempts: 5 });

export async function sendAll(queueUrl, messages) {
  const chunks = [];
  for (let i = 0; i < messages.length; i += 10)
    chunks.push(messages.slice(i, i + 10));

  const results = await Promise.all(
    chunks.map((chunk) =>
      sqs.send(
        new SendMessageBatchCommand({
          QueueUrl: queueUrl,
          Entries: chunk.map((m, idx) => ({
            Id: String(idx),
            MessageBody: JSON.stringify(m),
          })),
        }),
      ),
    ),
  );

  const failed = results.flatMap((r) => r.Failed ?? []);
  if (failed.length)
    throw new Error(`${failed.length} messages failed to send`);
}
```
