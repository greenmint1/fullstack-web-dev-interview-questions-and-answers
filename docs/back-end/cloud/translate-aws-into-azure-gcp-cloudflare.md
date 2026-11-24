# Translate AWS into Azure, GCP and Cloudflare Interview Questions and Answers

_Last updated: November 24, 2026_

450 interview questions about translating AWS services, code and architecture into Microsoft Azure, Google Cloud (GCP) and Cloudflare, split into three levels: 150 easy, 150 moderate and 150 advanced. Every answer shows the same idea on each provider, in this order: AWS, Azure, GCP, Cloudflare. When a provider has no real equivalent for a service, it is left out of that answer (in comparison tables it is marked "n/a").

The answers target the state of the platforms in late 2026: AWS CLI v2 and AWS SDK for JavaScript v3, Azure CLI 2.x with the Azure Functions Node.js v4 programming model, the gcloud CLI with Cloud Run and Cloud Run functions, and Cloudflare Workers with Wrangler 4 and `wrangler.jsonc`. Code examples use TypeScript on Node.js 22+, Bash for CLI commands and HCL for Terraform. Cloudflare is not a full general-purpose cloud: it has no virtual machines, VPCs or managed Kubernetes, so it shows up mostly for serverless compute, storage, networking, security and edge features.

## Table of Contents

- [Easy Questions (1-150)](#easy-questions-1-150)
- [Moderate Questions (151-300)](#moderate-questions-151-300)
- [Advanced Questions (301-450)](#advanced-questions-301-450)

### Easy Questions (1-150)

- [1: What does it mean to translate an AWS architecture into Azure, GCP or Cloudflare?](#1-what-does-it-mean-to-translate-an-aws-architecture-into-azure-gcp-or-cloudflare)
- [2: How are AWS, Azure, GCP and Cloudflare different in nature?](#2-how-are-aws-azure-gcp-and-cloudflare-different-in-nature)
- [3: How does the AWS account structure map to the other providers?](#3-how-does-the-aws-account-structure-map-to-the-other-providers)
- [4: How do regions and availability zones compare?](#4-how-do-regions-and-availability-zones-compare)
- [5: What are the command-line tools for each provider?](#5-what-are-the-command-line-tools-for-each-provider)
- [6: How do you log in from the CLI?](#6-how-do-you-log-in-from-the-cli)
- [7: What is the equivalent of an IAM user?](#7-what-is-the-equivalent-of-an-iam-user)
- [8: What is the equivalent of an IAM role for code running in the cloud?](#8-what-is-the-equivalent-of-an-iam-role-for-code-running-in-the-cloud)
- [9: How do IAM policies compare to Azure RBAC and GCP IAM?](#9-how-do-iam-policies-compare-to-azure-rbac-and-gcp-iam)
- [10: What is the equivalent of the AWS root user?](#10-what-is-the-equivalent-of-the-aws-root-user)
- [11: How do you enforce MFA?](#11-how-do-you-enforce-mfa)
- [12: What is the equivalent of EC2?](#12-what-is-the-equivalent-of-ec2)
- [13: How do you create a virtual machine from the CLI?](#13-how-do-you-create-a-virtual-machine-from-the-cli)
- [14: How do instance type names compare?](#14-how-do-instance-type-names-compare)
- [15: What is the equivalent of an AMI?](#15-what-is-the-equivalent-of-an-ami)
- [16: What is the equivalent of EBS?](#16-what-is-the-equivalent-of-ebs)
- [17: What is the equivalent of a security group?](#17-what-is-the-equivalent-of-a-security-group)
- [18: How do you connect to a VM over SSH without opening port 22?](#18-how-do-you-connect-to-a-vm-over-ssh-without-opening-port-22)
- [19: What is the equivalent of Spot Instances?](#19-what-is-the-equivalent-of-spot-instances)
- [20: What is the equivalent of an Elastic IP?](#20-what-is-the-equivalent-of-an-elastic-ip)
- [21: What is the equivalent of EC2 user data?](#21-what-is-the-equivalent-of-ec2-user-data)
- [22: What is the equivalent of an Auto Scaling group?](#22-what-is-the-equivalent-of-an-auto-scaling-group)
- [23: What is the equivalent of AWS Lambda?](#23-what-is-the-equivalent-of-aws-lambda)
- [24: How do you write a simple HTTP function in each?](#24-how-do-you-write-a-simple-http-function-in-each)
- [25: How do you deploy a function from the CLI?](#25-how-do-you-deploy-a-function-from-the-cli)
- [26: What kinds of triggers can a function have?](#26-what-kinds-of-triggers-can-a-function-have)
- [27: How do function limits compare?](#27-how-do-function-limits-compare)
- [28: What are cold starts and how do they compare?](#28-what-are-cold-starts-and-how-do-they-compare)
- [29: How do you set environment variables for a function?](#29-how-do-you-set-environment-variables-for-a-function)
- [30: What is the equivalent of AWS Secrets Manager?](#30-what-is-the-equivalent-of-aws-secrets-manager)
- [31: What is the equivalent of SSM Parameter Store for plain configuration?](#31-what-is-the-equivalent-of-ssm-parameter-store-for-plain-configuration)
- [32: What is the equivalent of Amazon S3?](#32-what-is-the-equivalent-of-amazon-s3)
- [33: Why does Azure have storage accounts on top of containers?](#33-why-does-azure-have-storage-accounts-on-top-of-containers)
- [34: How do you upload and download a file from the CLI?](#34-how-do-you-upload-and-download-a-file-from-the-cli)
- [35: How do storage classes compare?](#35-how-do-storage-classes-compare)
- [36: What is the equivalent of an S3 presigned URL?](#36-what-is-the-equivalent-of-an-s3-presigned-url)
- [37: How do you host a static website?](#37-how-do-you-host-a-static-website)
- [38: What is the equivalent of S3 versioning?](#38-what-is-the-equivalent-of-s3-versioning)
- [39: What is the equivalent of S3 lifecycle rules?](#39-what-is-the-equivalent-of-s3-lifecycle-rules)
- [40: What is the equivalent of DynamoDB?](#40-what-is-the-equivalent-of-dynamodb)
- [41: What is the equivalent of Amazon RDS?](#41-what-is-the-equivalent-of-amazon-rds)
- [42: What is the equivalent of Aurora?](#42-what-is-the-equivalent-of-aurora)
- [43: What is the equivalent of ElastiCache?](#43-what-is-the-equivalent-of-elasticache)
- [44: What is the equivalent of Redshift?](#44-what-is-the-equivalent-of-redshift)
- [45: What is the equivalent of Athena?](#45-what-is-the-equivalent-of-athena)
- [46: What is the equivalent of SQS?](#46-what-is-the-equivalent-of-sqs)
- [47: What is the equivalent of SNS?](#47-what-is-the-equivalent-of-sns)
- [48: What is the equivalent of EventBridge?](#48-what-is-the-equivalent-of-eventbridge)
- [49: What is the equivalent of Kinesis?](#49-what-is-the-equivalent-of-kinesis)
- [50: What is the equivalent of Step Functions?](#50-what-is-the-equivalent-of-step-functions)
- [51: How do you run code on a schedule?](#51-how-do-you-run-code-on-a-schedule)
- [52: What is the equivalent of a VPC?](#52-what-is-the-equivalent-of-a-vpc)
- [53: How do subnets differ between AWS, Azure and GCP?](#53-how-do-subnets-differ-between-aws-azure-and-gcp)
- [54: What is the equivalent of a NAT gateway?](#54-what-is-the-equivalent-of-a-nat-gateway)
- [55: What is the equivalent of Route 53?](#55-what-is-the-equivalent-of-route-53)
- [56: How do you create a DNS record from the CLI?](#56-how-do-you-create-a-dns-record-from-the-cli)
- [57: What is the equivalent of CloudFront?](#57-what-is-the-equivalent-of-cloudfront)
- [58: What is the equivalent of an Application Load Balancer?](#58-what-is-the-equivalent-of-an-application-load-balancer)
- [59: What is the equivalent of a Network Load Balancer?](#59-what-is-the-equivalent-of-a-network-load-balancer)
- [60: What is the equivalent of API Gateway?](#60-what-is-the-equivalent-of-api-gateway)
- [61: What is the equivalent of AWS WAF?](#61-what-is-the-equivalent-of-aws-waf)
- [62: What is the equivalent of AWS Shield?](#62-what-is-the-equivalent-of-aws-shield)
- [63: What is the equivalent of AWS Certificate Manager?](#63-what-is-the-equivalent-of-aws-certificate-manager)
- [64: What is the equivalent of CloudWatch Logs?](#64-what-is-the-equivalent-of-cloudwatch-logs)
- [65: What is the equivalent of CloudWatch metrics and alarms?](#65-what-is-the-equivalent-of-cloudwatch-metrics-and-alarms)
- [66: What is the equivalent of AWS X-Ray?](#66-what-is-the-equivalent-of-aws-x-ray)
- [67: What is the equivalent of CloudTrail?](#67-what-is-the-equivalent-of-cloudtrail)
- [68: What is the equivalent of CloudFormation?](#68-what-is-the-equivalent-of-cloudformation)
- [69: How do you create a storage bucket with Terraform on each provider?](#69-how-do-you-create-a-storage-bucket-with-terraform-on-each-provider)
- [70: What is the equivalent of ECR?](#70-what-is-the-equivalent-of-ecr)
- [71: How do you push a container image?](#71-how-do-you-push-a-container-image)
- [72: What is the equivalent of ECS on Fargate?](#72-what-is-the-equivalent-of-ecs-on-fargate)
- [73: What is the equivalent of EKS?](#73-what-is-the-equivalent-of-eks)
- [74: How do you create a Kubernetes cluster from the CLI?](#74-how-do-you-create-a-kubernetes-cluster-from-the-cli)
- [75: What is the equivalent of Elastic Beanstalk or App Runner?](#75-what-is-the-equivalent-of-elastic-beanstalk-or-app-runner)
- [76: What is the equivalent of AWS Amplify Hosting?](#76-what-is-the-equivalent-of-aws-amplify-hosting)
- [77: What is the equivalent of Amazon Cognito?](#77-what-is-the-equivalent-of-amazon-cognito)
- [78: What is the equivalent of Amazon SES?](#78-what-is-the-equivalent-of-amazon-ses)
- [79: What is the equivalent of AWS KMS?](#79-what-is-the-equivalent-of-aws-kms)
- [80: What is the equivalent of Amazon Bedrock?](#80-what-is-the-equivalent-of-amazon-bedrock)
- [81: What is the equivalent of SageMaker?](#81-what-is-the-equivalent-of-sagemaker)
- [82: What are the equivalents of AWS AI services like Rekognition and Textract?](#82-what-are-the-equivalents-of-aws-ai-services-like-rekognition-and-textract)
- [83: What is the equivalent of OpenSearch Service?](#83-what-is-the-equivalent-of-opensearch-service)
- [84: What is the equivalent of a vector database on AWS?](#84-what-is-the-equivalent-of-a-vector-database-on-aws)
- [85: What is the equivalent of CodePipeline and CodeBuild?](#85-what-is-the-equivalent-of-codepipeline-and-codebuild)
- [86: What is the equivalent of CodeCommit?](#86-what-is-the-equivalent-of-codecommit)
- [87: What is the equivalent of Direct Connect?](#87-what-is-the-equivalent-of-direct-connect)
- [88: What is the equivalent of a site-to-site VPN?](#88-what-is-the-equivalent-of-a-site-to-site-vpn)
- [89: What is the equivalent of AWS PrivateLink?](#89-what-is-the-equivalent-of-aws-privatelink)
- [90: What is the equivalent of VPC peering?](#90-what-is-the-equivalent-of-vpc-peering)
- [91: What is the equivalent of Transit Gateway?](#91-what-is-the-equivalent-of-transit-gateway)
- [92: What is the equivalent of AWS Cost Explorer?](#92-what-is-the-equivalent-of-aws-cost-explorer)
- [93: How do you set up a budget alert?](#93-how-do-you-set-up-a-budget-alert)
- [94: How do tags compare?](#94-how-do-tags-compare)
- [95: How do the free tiers compare?](#95-how-do-the-free-tiers-compare)
- [96: How do pricing models for serverless compute differ?](#96-how-do-pricing-models-for-serverless-compute-differ)
- [97: How does the shared responsibility model compare?](#97-how-does-the-shared-responsibility-model-compare)
- [98: How do the well-architected frameworks compare?](#98-how-do-the-well-architected-frameworks-compare)
- [99: How do you install the JavaScript SDKs?](#99-how-do-you-install-the-javascript-sdks)
- [100: How do you read an object from storage in code?](#100-how-do-you-read-an-object-from-storage-in-code)
- [101: How does the default credential chain work in each SDK?](#101-how-does-the-default-credential-chain-work-in-each-sdk)
- [102: How do resource identifiers compare?](#102-how-do-resource-identifiers-compare)
- [103: How do service quotas compare?](#103-how-do-service-quotas-compare)
- [104: What is the equivalent of AWS Marketplace?](#104-what-is-the-equivalent-of-aws-marketplace)
- [105: How do you check provider health status?](#105-how-do-you-check-provider-health-status)
- [106: What is the equivalent of Trusted Advisor?](#106-what-is-the-equivalent-of-trusted-advisor)
- [107: What is the equivalent of AWS Config?](#107-what-is-the-equivalent-of-aws-config)
- [108: What is the equivalent of GuardDuty?](#108-what-is-the-equivalent-of-guardduty)
- [109: What is the equivalent of Amazon Inspector?](#109-what-is-the-equivalent-of-amazon-inspector)
- [110: What is the equivalent of Security Hub?](#110-what-is-the-equivalent-of-security-hub)
- [111: What is the equivalent of Service Control Policies?](#111-what-is-the-equivalent-of-service-control-policies)
- [112: What is the equivalent of AWS Control Tower?](#112-what-is-the-equivalent-of-aws-control-tower)
- [113: What is the equivalent of EFS?](#113-what-is-the-equivalent-of-efs)
- [114: What is the equivalent of FSx?](#114-what-is-the-equivalent-of-fsx)
- [115: What is the equivalent of AWS Backup?](#115-what-is-the-equivalent-of-aws-backup)
- [116: How do disk snapshots compare?](#116-how-do-disk-snapshots-compare)
- [117: How do you move large amounts of data into each cloud?](#117-how-do-you-move-large-amounts-of-data-into-each-cloud)
- [118: What is the equivalent of AWS Glue?](#118-what-is-the-equivalent-of-aws-glue)
- [119: What is the equivalent of EMR?](#119-what-is-the-equivalent-of-emr)
- [120: What is the equivalent of QuickSight?](#120-what-is-the-equivalent-of-quicksight)
- [121: What is the equivalent of Amazon MSK?](#121-what-is-the-equivalent-of-amazon-msk)
- [122: What is the equivalent of Amazon MQ?](#122-what-is-the-equivalent-of-amazon-mq)
- [123: What is the equivalent of AppSync?](#123-what-is-the-equivalent-of-appsync)
- [124: What is the equivalent of AWS IoT Core?](#124-what-is-the-equivalent-of-aws-iot-core)
- [125: What is the equivalent of AWS Outposts?](#125-what-is-the-equivalent-of-aws-outposts)
- [126: What is the equivalent of AWS Local Zones and Wavelength?](#126-what-is-the-equivalent-of-aws-local-zones-and-wavelength)
- [127: What is the equivalent of AWS Global Accelerator?](#127-what-is-the-equivalent-of-aws-global-accelerator)
- [128: How do you set up DNS failover?](#128-how-do-you-set-up-dns-failover)
- [129: What is the equivalent of Lambda function URLs?](#129-what-is-the-equivalent-of-lambda-function-urls)
- [130: What is the equivalent of Lambda@Edge and CloudFront Functions?](#130-what-is-the-equivalent-of-lambdaedge-and-cloudfront-functions)
- [131: How do you add a custom domain to a serverless app?](#131-how-do-you-add-a-custom-domain-to-a-serverless-app)
- [132: What is the equivalent of CloudWatch Synthetics?](#132-what-is-the-equivalent-of-cloudwatch-synthetics)
- [133: What is the equivalent of CloudWatch RUM?](#133-what-is-the-equivalent-of-cloudwatch-rum)
- [134: What is the equivalent of SNS mobile push?](#134-what-is-the-equivalent-of-sns-mobile-push)
- [135: What is the equivalent of Amazon Location Service?](#135-what-is-the-equivalent-of-amazon-location-service)
- [136: What is the equivalent of AWS media services for video?](#136-what-is-the-equivalent-of-aws-media-services-for-video)
- [137: What is the equivalent of API Gateway WebSocket APIs?](#137-what-is-the-equivalent-of-api-gateway-websocket-apis)
- [138: What is the equivalent of Amazon Chime SDK for real-time audio and video?](#138-what-is-the-equivalent-of-amazon-chime-sdk-for-real-time-audio-and-video)
- [139: What is the equivalent of a CAPTCHA or bot protection service?](#139-what-is-the-equivalent-of-a-captcha-or-bot-protection-service)
- [140: What is the equivalent of AWS Fault Injection Service?](#140-what-is-the-equivalent-of-aws-fault-injection-service)
- [141: What is the equivalent of a load testing service?](#141-what-is-the-equivalent-of-a-load-testing-service)
- [142: What are the pricing calculators?](#142-what-are-the-pricing-calculators)
- [143: What is the equivalent of AWS Systems Manager Patch Manager?](#143-what-is-the-equivalent-of-aws-systems-manager-patch-manager)
- [144: What is the equivalent of AWS Systems Manager Run Command?](#144-what-is-the-equivalent-of-aws-systems-manager-run-command)
- [145: What is the equivalent of Amazon WorkSpaces?](#145-what-is-the-equivalent-of-amazon-workspaces)
- [146: What is the equivalent of AWS Batch?](#146-what-is-the-equivalent-of-aws-batch)
- [147: What is the equivalent of Amazon Lightsail?](#147-what-is-the-equivalent-of-amazon-lightsail)
- [148: What is the equivalent of AWS Elastic Disaster Recovery?](#148-what-is-the-equivalent-of-aws-elastic-disaster-recovery)
- [149: What are the equivalent migration discovery tools?](#149-what-are-the-equivalent-migration-discovery-tools)
- [150: Can you give a quick cheat sheet of the most common translations?](#150-can-you-give-a-quick-cheat-sheet-of-the-most-common-translations)

### Moderate Questions (151-300)

- [151: How do you translate an IAM policy that grants read and write access to one bucket?](#151-how-do-you-translate-an-iam-policy-that-grants-read-and-write-access-to-one-bucket)
- [152: How do you create a custom role?](#152-how-do-you-create-a-custom-role)
- [153: How do you translate sts:AssumeRole?](#153-how-do-you-translate-stsassumerole)
- [154: How do you deploy from GitHub Actions without long-lived keys?](#154-how-do-you-deploy-from-github-actions-without-long-lived-keys)
- [155: How do you give a function its own identity?](#155-how-do-you-give-a-function-its-own-identity)
- [156: How do you build a small REST API with routes?](#156-how-do-you-build-a-small-rest-api-with-routes)
- [157: How do you read a JSON body and return JSON?](#157-how-do-you-read-a-json-body-and-return-json)
- [158: How do you run code when a file is uploaded to storage?](#158-how-do-you-run-code-when-a-file-is-uploaded-to-storage)
- [159: How do you consume messages from a queue?](#159-how-do-you-consume-messages-from-a-queue)
- [160: How do you send a message to a queue or topic?](#160-how-do-you-send-a-message-to-a-queue-or-topic)
- [161: How do you configure a dead-letter queue?](#161-how-do-you-configure-a-dead-letter-queue)
- [162: How do visibility timeout, lock duration and ack deadline compare?](#162-how-do-visibility-timeout-lock-duration-and-ack-deadline-compare)
- [163: How do you translate SQS FIFO queues?](#163-how-do-you-translate-sqs-fifo-queues)
- [164: How do you translate an SNS topic that fans out to several SQS queues?](#164-how-do-you-translate-an-sns-topic-that-fans-out-to-several-sqs-queues)
- [165: How do you write and read a record in the main NoSQL database?](#165-how-do-you-write-and-read-a-record-in-the-main-nosql-database)
- [166: How do you translate a DynamoDB query on partition key and sort key?](#166-how-do-you-translate-a-dynamodb-query-on-partition-key-and-sort-key)
- [167: How do you set a time-to-live on records?](#167-how-do-you-set-a-time-to-live-on-records)
- [168: How do you react to database changes?](#168-how-do-you-react-to-database-changes)
- [169: How do you create a managed SQL database from the CLI?](#169-how-do-you-create-a-managed-sql-database-from-the-cli)
- [170: How do you connect to Postgres efficiently from serverless code?](#170-how-do-you-connect-to-postgres-efficiently-from-serverless-code)
- [171: How do you use IAM authentication instead of a database password?](#171-how-do-you-use-iam-authentication-instead-of-a-database-password)
- [172: How do you read a secret at runtime?](#172-how-do-you-read-a-secret-at-runtime)
- [173: How do you inject secrets as environment variables without code?](#173-how-do-you-inject-secrets-as-environment-variables-without-code)
- [174: How do you generate an upload URL so the browser uploads straight to storage?](#174-how-do-you-generate-an-upload-url-so-the-browser-uploads-straight-to-storage)
- [175: How do you upload a large file in parts?](#175-how-do-you-upload-a-large-file-in-parts)
- [176: How do you configure CORS on a bucket?](#176-how-do-you-configure-cors-on-a-bucket)
- [177: How do you serve a private bucket through the CDN?](#177-how-do-you-serve-a-private-bucket-through-the-cdn)
- [178: How do you invalidate the CDN cache?](#178-how-do-you-invalidate-the-cdn-cache)
- [179: How do default caching rules differ between CDNs?](#179-how-do-default-caching-rules-differ-between-cdns)
- [180: How do you translate a CloudFront Function redirect into the other providers?](#180-how-do-you-translate-a-cloudfront-function-redirect-into-the-other-providers)
- [181: How do you serve a single-page app and its API from one deployment?](#181-how-do-you-serve-a-single-page-app-and-its-api-from-one-deployment)
- [182: How do you query logs for errors?](#182-how-do-you-query-logs-for-errors)
- [183: How do you write structured logs that each platform understands?](#183-how-do-you-write-structured-logs-that-each-platform-understands)
- [184: How do you create an alert when a function's errors go up?](#184-how-do-you-create-an-alert-when-a-functions-errors-go-up)
- [185: How do you add distributed tracing with OpenTelemetry?](#185-how-do-you-add-distributed-tracing-with-opentelemetry)
- [186: How do you do canary releases for serverless code?](#186-how-do-you-do-canary-releases-for-serverless-code)
- [187: How do Lambda versions and aliases map to the other platforms?](#187-how-do-lambda-versions-and-aliases-map-to-the-other-platforms)
- [188: How do you roll back a bad deployment?](#188-how-do-you-roll-back-a-bad-deployment)
- [189: How do you run and test functions locally?](#189-how-do-you-run-and-test-functions-locally)
- [190: How do you unit test a handler on each platform?](#190-how-do-you-unit-test-a-handler-on-each-platform)
- [191: How do you manage several environments (dev, staging, prod)?](#191-how-do-you-manage-several-environments-dev-staging-prod)
- [192: How are function dependencies packaged?](#192-how-are-function-dependencies-packaged)
- [193: What do you need to change for Node.js code to run on Workers?](#193-what-do-you-need-to-change-for-nodejs-code-to-run-on-workers)
- [194: How do you run an existing Express app on each platform?](#194-how-do-you-run-an-existing-express-app-on-each-platform)
- [195: How do you deploy a container web service on each platform?](#195-how-do-you-deploy-a-container-web-service-on-each-platform)
- [196: How does an ECS task definition translate?](#196-how-does-an-ecs-task-definition-translate)
- [197: How do autoscaling settings for containers compare?](#197-how-do-autoscaling-settings-for-containers-compare)
- [198: How do you run scheduled container jobs?](#198-how-do-you-run-scheduled-container-jobs)
- [199: How do Kubernetes pods get cloud credentials?](#199-how-do-kubernetes-pods-get-cloud-credentials)
- [200: How do Kubernetes ingress and load balancers translate?](#200-how-do-kubernetes-ingress-and-load-balancers-translate)
- [201: How do Kubernetes storage classes translate?](#201-how-do-kubernetes-storage-classes-translate)
- [202: How do you get cloud secrets into Kubernetes pods?](#202-how-do-you-get-cloud-secrets-into-kubernetes-pods)
- [203: How does Kubernetes node autoscaling compare?](#203-how-does-kubernetes-node-autoscaling-compare)
- [204: How do you configure a Terraform state backend on each provider?](#204-how-do-you-configure-a-terraform-state-backend-on-each-provider)
- [205: How do Terraform providers authenticate?](#205-how-do-terraform-providers-authenticate)
- [206: How do you translate a CloudFormation template into Bicep?](#206-how-do-you-translate-a-cloudformation-template-into-bicep)
- [207: How do you translate Lambda reserved concurrency?](#207-how-do-you-translate-lambda-reserved-concurrency)
- [208: How do you translate Lambda provisioned concurrency?](#208-how-do-you-translate-lambda-provisioned-concurrency)
- [209: How do you let a function reach private resources in a VPC?](#209-how-do-you-let-a-function-reach-private-resources-in-a-vpc)
- [210: How do you give serverless code a fixed outbound IP?](#210-how-do-you-give-serverless-code-a-fixed-outbound-ip)
- [211: How do you require client certificates (mTLS) on an API?](#211-how-do-you-require-client-certificates-mtls-on-an-api)
- [212: How do you validate JWTs at the gateway?](#212-how-do-you-validate-jwts-at-the-gateway)
- [213: How do you rate limit an API?](#213-how-do-you-rate-limit-an-api)
- [214: How do you make storage reachable only from a private network?](#214-how-do-you-make-storage-reachable-only-from-a-private-network)
- [215: How do VPC gateway endpoints compare with Azure service endpoints and Private Google Access?](#215-how-do-vpc-gateway-endpoints-compare-with-azure-service-endpoints-and-private-google-access)
- [216: How do you translate a security group that allows traffic from another security group?](#216-how-do-you-translate-a-security-group-that-allows-traffic-from-another-security-group)
- [217: How do you translate network ACLs?](#217-how-do-you-translate-network-acls)
- [218: How do you translate private hosted zones?](#218-how-do-you-translate-private-hosted-zones)
- [219: How do you resolve DNS between on-premises and the cloud?](#219-how-do-you-resolve-dns-between-on-premises-and-the-cloud)
- [220: How do you translate a bastion host setup?](#220-how-do-you-translate-a-bastion-host-setup)
- [221: How do load balancer health checks compare?](#221-how-do-load-balancer-health-checks-compare)
- [222: How do sticky sessions translate?](#222-how-do-sticky-sessions-translate)
- [223: How do you build a WebSocket chat room on each platform?](#223-how-do-you-build-a-websocket-chat-room-on-each-platform)
- [224: How do you stream a response (for example Server-Sent Events or LLM tokens)?](#224-how-do-you-stream-a-response-for-example-server-sent-events-or-llm-tokens)
- [225: How do you translate a Step Functions workflow into the other platforms?](#225-how-do-you-translate-a-step-functions-workflow-into-the-other-platforms)
- [226: How do you wait for a human approval inside a workflow?](#226-how-do-you-wait-for-a-human-approval-inside-a-workflow)
- [227: How do you add retries with backoff to workflow steps?](#227-how-do-you-add-retries-with-backoff-to-workflow-steps)
- [228: How do you translate an EventBridge rule?](#228-how-do-you-translate-an-eventbridge-rule)
- [229: How do you publish a custom event?](#229-how-do-you-publish-a-custom-event)
- [230: How do you translate EventBridge Pipes?](#230-how-do-you-translate-eventbridge-pipes)
- [231: How do you translate Kinesis producers and consumers?](#231-how-do-you-translate-kinesis-producers-and-consumers)
- [232: How do you load streaming data straight into the data warehouse?](#232-how-do-you-load-streaming-data-straight-into-the-data-warehouse)
- [233: How do you translate a Redshift COPY into the other warehouses?](#233-how-do-you-translate-a-redshift-copy-into-the-other-warehouses)
- [234: How do SQL dialects differ when translating Redshift queries?](#234-how-do-sql-dialects-differ-when-translating-redshift-queries)
- [235: How do you call an LLM on each platform?](#235-how-do-you-call-an-llm-on-each-platform)
- [236: How do you create embeddings and run a vector search?](#236-how-do-you-create-embeddings-and-run-a-vector-search)
- [237: How do you put a gateway in front of LLM calls for caching, logging and limits?](#237-how-do-you-put-a-gateway-in-front-of-llm-calls-for-caching-logging-and-limits)
- [238: How do you add content safety guardrails to LLM apps?](#238-how-do-you-add-content-safety-guardrails-to-llm-apps)
- [239: How do you run a RAG pipeline with mostly managed services?](#239-how-do-you-run-a-rag-pipeline-with-mostly-managed-services)
- [240: How do you host an AI agent?](#240-how-do-you-host-an-ai-agent)
- [241: How do you translate SES email sending code?](#241-how-do-you-translate-ses-email-sending-code)
- [242: How do you receive and process incoming email?](#242-how-do-you-receive-and-process-incoming-email)
- [243: How do you translate Cognito user sign-in for a web app?](#243-how-do-you-translate-cognito-user-sign-in-for-a-web-app)
- [244: How do you protect an internal admin app with SSO?](#244-how-do-you-protect-an-internal-admin-app-with-sso)
- [245: How do you translate KMS envelope encryption in code?](#245-how-do-you-translate-kms-envelope-encryption-in-code)
- [246: How do you encrypt storage with your own keys?](#246-how-do-you-encrypt-storage-with-your-own-keys)
- [247: How do you rotate secrets?](#247-how-do-you-rotate-secrets)
- [248: How do you add read replicas?](#248-how-do-you-add-read-replicas)
- [249: How do you make a managed database highly available?](#249-how-do-you-make-a-managed-database-highly-available)
- [250: How do you restore a database to a point in time?](#250-how-do-you-restore-a-database-to-a-point-in-time)
- [251: How do you migrate a database between clouds with minimal downtime?](#251-how-do-you-migrate-a-database-between-clouds-with-minimal-downtime)
- [252: How do you load existing data into D1?](#252-how-do-you-load-existing-data-into-d1)
- [253: How do NoSQL pricing models compare?](#253-how-do-nosql-pricing-models-compare)
- [254: How do you translate a DynamoDB partition key into Cosmos DB?](#254-how-do-you-translate-a-dynamodb-partition-key-into-cosmos-db)
- [255: How do secondary indexes translate?](#255-how-do-secondary-indexes-translate)
- [256: How do you translate conditional writes and optimistic locking?](#256-how-do-you-translate-conditional-writes-and-optimistic-locking)
- [257: How do you implement an atomic counter?](#257-how-do-you-implement-an-atomic-counter)
- [258: How do batch writes compare?](#258-how-do-batch-writes-compare)
- [259: How do you translate a cache-aside pattern with Redis?](#259-how-do-you-translate-a-cache-aside-pattern-with-redis)
- [260: How do you cache API responses at the edge?](#260-how-do-you-cache-api-responses-at-the-edge)
- [261: Where do you store user sessions on each platform?](#261-where-do-you-store-user-sessions-on-each-platform)
- [262: How much local disk does serverless code get?](#262-how-much-local-disk-does-serverless-code-get)
- [263: How do you mount shared storage into serverless containers?](#263-how-do-you-mount-shared-storage-into-serverless-containers)
- [264: How do you resize images on the fly?](#264-how-do-you-resize-images-on-the-fly)
- [265: How do you give users time-limited access to private CDN content?](#265-how-do-you-give-users-time-limited-access-to-private-cdn-content)
- [266: How do you block or allow traffic by country?](#266-how-do-you-block-or-allow-traffic-by-country)
- [267: How do you get the client's country or real IP in code?](#267-how-do-you-get-the-clients-country-or-real-ip-in-code)
- [268: How do you make sure the origin only accepts traffic from the CDN?](#268-how-do-you-make-sure-the-origin-only-accepts-traffic-from-the-cdn)
- [269: How do you deploy a static site from CI?](#269-how-do-you-deploy-a-static-site-from-ci)
- [270: How do you add security headers to every response?](#270-how-do-you-add-security-headers-to-every-response)
- [271: How do you translate feature flags from AWS AppConfig?](#271-how-do-you-translate-feature-flags-from-aws-appconfig)
- [272: How do services call each other privately?](#272-how-do-services-call-each-other-privately)
- [273: How do you call a private Cloud Run service from another service?](#273-how-do-you-call-a-private-cloud-run-service-from-another-service)
- [274: How do you make a service reachable only internally?](#274-how-do-you-make-a-service-reachable-only-internally)
- [275: What happened to AWS App Mesh, and what replaces a service mesh on each cloud?](#275-what-happened-to-aws-app-mesh-and-what-replaces-a-service-mesh-on-each-cloud)
- [276: How do the build config files compare?](#276-how-do-the-build-config-files-compare)
- [277: How do you preview infrastructure changes before applying them?](#277-how-do-you-preview-infrastructure-changes-before-applying-them)
- [278: How do you block public buckets across the organization?](#278-how-do-you-block-public-buckets-across-the-organization)
- [279: How do you restrict which regions can be used?](#279-how-do-you-restrict-which-regions-can-be-used)
- [280: How do you split cloud costs by team?](#280-how-do-you-split-cloud-costs-by-team)
- [281: How do commitment discounts compare?](#281-how-do-commitment-discounts-compare)
- [282: How do you handle spot VM interruptions in code?](#282-how-do-you-handle-spot-vm-interruptions-in-code)
- [283: How do you implement idempotency keys on each platform?](#283-how-do-you-implement-idempotency-keys-on-each-platform)
- [284: How do you send a message with a delay?](#284-how-do-you-send-a-message-with-a-delay)
- [285: How do you monitor queue backlog?](#285-how-do-you-monitor-queue-backlog)
- [286: How do you set log retention?](#286-how-do-you-set-log-retention)
- [287: How do you export logs to storage or a SIEM?](#287-how-do-you-export-logs-to-storage-or-a-siem)
- [288: How do you record custom business metrics?](#288-how-do-you-record-custom-business-metrics)
- [289: How do you turn log lines into metrics?](#289-how-do-you-turn-log-lines-into-metrics)
- [290: How do you host a Next.js app on each platform?](#290-how-do-you-host-a-nextjs-app-on-each-platform)
- [291: How do you schedule a job in a specific time zone?](#291-how-do-you-schedule-a-job-in-a-specific-time-zone)
- [292: How do readiness and liveness checks translate for containers?](#292-how-do-readiness-and-liveness-checks-translate-for-containers)
- [293: How do you shut down gracefully?](#293-how-do-you-shut-down-gracefully)
- [294: How do you run background work after sending the response?](#294-how-do-you-run-background-work-after-sending-the-response)
- [295: How do you translate API Gateway request validation?](#295-how-do-you-translate-api-gateway-request-validation)
- [296: How do you translate API keys and usage plans?](#296-how-do-you-translate-api-keys-and-usage-plans)
- [297: How do you expose an OpenAPI-defined API?](#297-how-do-you-expose-an-openapi-defined-api)
- [298: How do you translate a Lambda function that runs on a Kinesis or SQS batch with a batch window?](#298-how-do-you-translate-a-lambda-function-that-runs-on-a-kinesis-or-sqs-batch-with-a-batch-window)
- [299: How do you translate DynamoDB Accelerator (DAX)?](#299-how-do-you-translate-dynamodb-accelerator-dax)
- [300: How do you translate an image thumbnail pipeline end to end?](#300-how-do-you-translate-an-image-thumbnail-pipeline-end-to-end)

### Advanced Questions (301-450)

- [301: How do you plan a full migration from AWS to Azure or GCP?](#301-how-do-you-plan-a-full-migration-from-aws-to-azure-or-gcp)
- [302: How do you decide what moves to Cloudflare and what moves to Azure or GCP?](#302-how-do-you-decide-what-moves-to-cloudflare-and-what-moves-to-azure-or-gcp)
- [303: How do rehost, replatform and refactor apply when leaving AWS?](#303-how-do-rehost-replatform-and-refactor-apply-when-leaving-aws)
- [304: How do you find all AWS dependencies of an application before moving it?](#304-how-do-you-find-all-aws-dependencies-of-an-application-before-moving-it)
- [305: How do egress costs affect a migration?](#305-how-do-egress-costs-affect-a-migration)
- [306: What are the trade-offs of R2's zero egress pricing?](#306-what-are-the-trade-offs-of-r2s-zero-egress-pricing)
- [307: How do object storage consistency models compare?](#307-how-do-object-storage-consistency-models-compare)
- [308: How do consistency guarantees differ between Workers KV, D1 and Durable Objects?](#308-how-do-consistency-guarantees-differ-between-workers-kv-d1-and-durable-objects)
- [309: How do database consistency models compare across DynamoDB, Cosmos DB, Firestore and Spanner?](#309-how-do-database-consistency-models-compare-across-dynamodb-cosmos-db-firestore-and-spanner)
- [310: How do you translate DynamoDB global tables?](#310-how-do-you-translate-dynamodb-global-tables)
- [311: How do conflict resolution strategies differ in multi-region writes?](#311-how-do-conflict-resolution-strategies-differ-in-multi-region-writes)
- [312: How do you translate a DynamoDB single-table design?](#312-how-do-you-translate-a-dynamodb-single-table-design)
- [313: What causes hot partitions on each database and how do you avoid them?](#313-what-causes-hot-partitions-on-each-database-and-how-do-you-avoid-them)
- [314: What are Durable Objects, and what do they replace when coming from AWS?](#314-what-are-durable-objects-and-what-do-they-replace-when-coming-from-aws)
- [315: When should you not use Durable Objects?](#315-when-should-you-not-use-durable-objects)
- [316: How do you translate Aurora Global Database?](#316-how-do-you-translate-aurora-global-database)
- [317: How does distributed SQL compare across providers?](#317-how-does-distributed-sql-compare-across-providers)
- [318: How do multi-item transactions compare?](#318-how-do-multi-item-transactions-compare)
- [319: How does permission evaluation differ between AWS IAM, Azure RBAC and GCP IAM?](#319-how-does-permission-evaluation-differ-between-aws-iam-azure-rbac-and-gcp-iam)
- [320: How do you translate resource-based policies like S3 bucket policies?](#320-how-do-you-translate-resource-based-policies-like-s3-bucket-policies)
- [321: How do you translate attribute-based access control (ABAC)?](#321-how-do-you-translate-attribute-based-access-control-abac)
- [322: How do you translate permission boundaries?](#322-how-do-you-translate-permission-boundaries)
- [323: What tools help you reach least privilege on each cloud?](#323-what-tools-help-you-reach-least-privilege-on-each-cloud)
- [324: How do you set up break-glass access on each provider?](#324-how-do-you-set-up-break-glass-access-on-each-provider)
- [325: How do workloads on one cloud call another cloud without stored keys?](#325-how-do-workloads-on-one-cloud-call-another-cloud-without-stored-keys)
- [326: How do you solve the "secret zero" problem on each platform?](#326-how-do-you-solve-the-secret-zero-problem-on-each-platform)
- [327: How do zero trust access products compare?](#327-how-do-zero-trust-access-products-compare)
- [328: How do you control outbound traffic from workloads?](#328-how-do-you-control-outbound-traffic-from-workloads)
- [329: How do you translate a hub-and-spoke network?](#329-how-do-you-translate-a-hub-and-spoke-network)
- [330: How does GCP's global VPC change network design compared to AWS?](#330-how-does-gcps-global-vpc-change-network-design-compared-to-aws)
- [331: What are the equivalents of a data perimeter on each cloud?](#331-what-are-the-equivalents-of-a-data-perimeter-on-each-cloud)
- [332: How do you plan IP addresses for a multi-cloud setup?](#332-how-do-you-plan-ip-addresses-for-a-multi-cloud-setup)
- [333: How does DDoS protection differ architecturally?](#333-how-does-ddos-protection-differ-architecturally)
- [334: How does global load balancing differ between providers?](#334-how-does-global-load-balancing-differ-between-providers)
- [335: How do the execution models of Lambda, Azure Functions, Cloud Run and Workers differ under the hood?](#335-how-do-the-execution-models-of-lambda-azure-functions-cloud-run-and-workers-differ-under-the-hood)
- [336: What Workers limits shape how you design apps translated from Lambda?](#336-what-workers-limits-shape-how-you-design-apps-translated-from-lambda)
- [337: What is Smart Placement and when does it matter?](#337-what-is-smart-placement-and-when-does-it-matter)
- [338: How does the concurrency model affect database connections after a migration?](#338-how-does-the-concurrency-model-affect-database-connections-after-a-migration)
- [339: Can you walk through a pricing comparison for an I/O-bound API?](#339-can-you-walk-through-a-pricing-comparison-for-an-io-bound-api)
- [340: How do cold start mitigations compare in depth?](#340-how-do-cold-start-mitigations-compare-in-depth)
- [341: How do you port Lambda code that uses the AWS SDK heavily to Workers?](#341-how-do-you-port-lambda-code-that-uses-the-aws-sdk-heavily-to-workers)
- [342: How do you migrate observability without losing visibility during the move?](#342-how-do-you-migrate-observability-without-losing-visibility-during-the-move)
- [343: How do you keep logging costs under control on each cloud?](#343-how-do-you-keep-logging-costs-under-control-on-each-cloud)
- [344: Why does the CloudEvents format matter in a migration?](#344-why-does-the-cloudevents-format-matter-in-a-migration)
- [345: How do "exactly once" messaging guarantees compare?](#345-how-do-exactly-once-messaging-guarantees-compare)
- [346: How do ordering guarantees compare?](#346-how-do-ordering-guarantees-compare)
- [347: How do you translate the transactional outbox pattern?](#347-how-do-you-translate-the-transactional-outbox-pattern)
- [348: How do you translate a saga with compensation steps?](#348-how-do-you-translate-a-saga-with-compensation-steps)
- [349: How does Kubernetes portability hold up in practice between EKS, AKS and GKE?](#349-how-does-kubernetes-portability-hold-up-in-practice-between-eks-aks-and-gke)
- [350: How do managed Kubernetes control planes and upgrades differ?](#350-how-do-managed-kubernetes-control-planes-and-upgrades-differ)
- [351: How do object storage request rate limits compare?](#351-how-do-object-storage-request-rate-limits-compare)
- [352: What are the high-performance object storage options?](#352-what-are-the-high-performance-object-storage-options)
- [353: How do multipart upload limits compare?](#353-how-do-multipart-upload-limits-compare)
- [354: How do you translate S3 Object Lock for compliance storage?](#354-how-do-you-translate-s3-object-lock-for-compliance-storage)
- [355: How do you translate cross-region replication of objects?](#355-how-do-you-translate-cross-region-replication-of-objects)
- [356: How do you handle data residency on each provider?](#356-how-do-you-handle-data-residency-on-each-provider)
- [357: How do disaster recovery strategies translate?](#357-how-do-disaster-recovery-strategies-translate)
- [358: What RTO and RPO can you expect from managed database DR on each cloud?](#358-what-rto-and-rpo-can-you-expect-from-managed-database-dr-on-each-cloud)
- [359: How would you design an active-active web app on each cloud?](#359-how-would-you-design-an-active-active-web-app-on-each-cloud)
- [360: How do you translate a cell-based architecture?](#360-how-do-you-translate-a-cell-based-architecture)
- [361: How do you isolate tenants in a multi-tenant SaaS on each platform?](#361-how-do-you-isolate-tenants-in-a-multi-tenant-saas-on-each-platform)
- [362: What is Workers for Platforms and what does it replace?](#362-what-is-workers-for-platforms-and-what-does-it-replace)
- [363: How do landing zone designs translate?](#363-how-do-landing-zone-designs-translate)
- [364: How do you translate common SCPs into Azure Policy and GCP organization policies?](#364-how-do-you-translate-common-scps-into-azure-policy-and-gcp-organization-policies)
- [365: How do billing structures compare?](#365-how-do-billing-structures-compare)
- [366: How do you compare costs across clouds in one report?](#366-how-do-you-compare-costs-across-clouds-in-one-report)
- [367: How do you migrate DNS to a new provider with zero downtime?](#367-how-do-you-migrate-dns-to-a-new-provider-with-zero-downtime)
- [368: What is the difference between full and partial (CNAME) setup when moving to Cloudflare?](#368-what-is-the-difference-between-full-and-partial-cname-setup-when-moving-to-cloudflare)
- [369: How do you migrate a large S3 bucket with minimal downtime?](#369-how-do-you-migrate-a-large-s3-bucket-with-minimal-downtime)
- [370: How do you cut over a relational database between clouds?](#370-how-do-you-cut-over-a-relational-database-between-clouds)
- [371: How do you migrate DynamoDB data to Cosmos DB or Firestore?](#371-how-do-you-migrate-dynamodb-data-to-cosmos-db-or-firestore)
- [372: How do you migrate users out of Cognito?](#372-how-do-you-migrate-users-out-of-cognito)
- [373: How do you migrate KMS-encrypted data and secrets?](#373-how-do-you-migrate-kms-encrypted-data-and-secrets)
- [374: How do you translate a CloudFront distribution to Cloudflare?](#374-how-do-you-translate-a-cloudfront-distribution-to-cloudflare)
- [375: How would you migrate a Lambda + API Gateway + DynamoDB app to Cloudflare?](#375-how-would-you-migrate-a-lambda--api-gateway--dynamodb-app-to-cloudflare)
- [376: How would you migrate the same app to Azure?](#376-how-would-you-migrate-the-same-app-to-azure)
- [377: How would you migrate the same app to GCP?](#377-how-would-you-migrate-the-same-app-to-gcp)
- [378: How do you prove the translated system behaves the same?](#378-how-do-you-prove-the-translated-system-behaves-the-same)
- [379: How do you send shadow traffic during a migration?](#379-how-do-you-send-shadow-traffic-during-a-migration)
- [380: How does the strangler fig pattern work with Cloudflare in front?](#380-how-does-the-strangler-fig-pattern-work-with-cloudflare-in-front)
- [381: How do you connect clouds privately during a hybrid period?](#381-how-do-you-connect-clouds-privately-during-a-hybrid-period)
- [382: When does a multi-cloud abstraction layer help, and when does it hurt?](#382-when-does-a-multi-cloud-abstraction-layer-help-and-when-does-it-hurt)
- [383: How do you structure Terraform for several providers?](#383-how-do-you-structure-terraform-for-several-providers)
- [384: What are alternatives to Terraform for multi-cloud IaC?](#384-what-are-alternatives-to-terraform-for-multi-cloud-iac)
- [385: Which AWS services create the most lock-in, and how does that affect translation effort?](#385-which-aws-services-create-the-most-lock-in-and-how-does-that-affect-translation-effort)
- [386: How much lock-in does Cloudflare create?](#386-how-much-lock-in-does-cloudflare-create)
- [387: When should you not move a workload to Cloudflare?](#387-when-should-you-not-move-a-workload-to-cloudflare)
- [388: How do you translate centralized security logging?](#388-how-do-you-translate-centralized-security-logging)
- [389: How do you translate GuardDuty-based incident response?](#389-how-do-you-translate-guardduty-based-incident-response)
- [390: How do BYOK and hold-your-own-key options compare?](#390-how-do-byok-and-hold-your-own-key-options-compare)
- [391: How does confidential computing compare?](#391-how-does-confidential-computing-compare)
- [392: How do you secure the container supply chain on each cloud?](#392-how-do-you-secure-the-container-supply-chain-on-each-cloud)
- [393: How do you enforce Kubernetes policies across EKS, AKS and GKE?](#393-how-do-you-enforce-kubernetes-policies-across-eks-aks-and-gke)
- [394: Should you use HashiCorp Vault or each cloud's secret manager in a multi-cloud setup?](#394-should-you-use-hashicorp-vault-or-each-clouds-secret-manager-in-a-multi-cloud-setup)
- [395: How do you vend new accounts, subscriptions or projects safely at scale?](#395-how-do-you-vend-new-accounts-subscriptions-or-projects-safely-at-scale)
- [396: How do quotas affect a large migration?](#396-how-do-quotas-affect-a-large-migration)
- [397: How does the Azure resource group model change the way you organize resources compared to AWS?](#397-how-does-the-azure-resource-group-model-change-the-way-you-organize-resources-compared-to-aws)
- [398: How does the GCP project model change the way you organize resources?](#398-how-does-the-gcp-project-model-change-the-way-you-organize-resources)
- [399: How do you translate CloudWatch alarms and dashboards at scale?](#399-how-do-you-translate-cloudwatch-alarms-and-dashboards-at-scale)
- [400: How do you design SLOs that work across a hybrid migration?](#400-how-do-you-design-slos-that-work-across-a-hybrid-migration)
- [401: How would you build a real-time collaborative document editor on each platform?](#401-how-would-you-build-a-real-time-collaborative-document-editor-on-each-platform)
- [402: How would you handle inventory for a flash sale without overselling?](#402-how-would-you-handle-inventory-for-a-flash-sale-without-overselling)
- [403: How would you build a global rate limiter?](#403-how-would-you-build-a-global-rate-limiter)
- [404: How would you build a video platform on each provider?](#404-how-would-you-build-a-video-platform-on-each-provider)
- [405: How would you ingest high-volume telemetry from devices?](#405-how-would-you-ingest-high-volume-telemetry-from-devices)
- [406: How would you design a RAG chatbot on each platform?](#406-how-would-you-design-a-rag-chatbot-on-each-platform)
- [407: How would you design a SaaS app that keeps EU customer data in the EU?](#407-how-would-you-design-a-saas-app-that-keeps-eu-customer-data-in-the-eu)
- [408: How would you translate a nightly ETL pipeline?](#408-how-would-you-translate-a-nightly-etl-pipeline)
- [409: How would you build a reliable webhook receiver?](#409-how-would-you-build-a-reliable-webhook-receiver)
- [410: How would you build a file sharing app with large uploads?](#410-how-would-you-build-a-file-sharing-app-with-large-uploads)
- [411: How would you build a B2B API with per-customer limits and mTLS?](#411-how-would-you-build-a-b2b-api-with-per-customer-limits-and-mtls)
- [412: How would you migrate a cron-heavy monolith running on EC2?](#412-how-would-you-migrate-a-cron-heavy-monolith-running-on-ec2)
- [413: How do you translate event sourcing?](#413-how-do-you-translate-event-sourcing)
- [414: How do you translate CQRS read models?](#414-how-do-you-translate-cqrs-read-models)
- [415: How do you translate durable timers at scale?](#415-how-do-you-translate-durable-timers-at-scale)
- [416: How do you translate fan-out and fan-in?](#416-how-do-you-translate-fan-out-and-fan-in)
- [417: How do you process millions of objects in parallel?](#417-how-do-you-process-millions-of-objects-in-parallel)
- [418: How do you design backpressure across these platforms?](#418-how-do-you-design-backpressure-across-these-platforms)
- [419: How do you avoid retry storms after an outage?](#419-how-do-you-avoid-retry-storms-after-an-outage)
- [420: How do timeout limits along the request path compare?](#420-how-do-timeout-limits-along-the-request-path-compare)
- [421: How do request and response size limits compare?](#421-how-do-request-and-response-size-limits-compare)
- [422: How do you layer caching in a translated architecture?](#422-how-do-you-layer-caching-in-a-translated-architecture)
- [423: How do you protect the origin from cache stampedes?](#423-how-do-you-protect-the-origin-from-cache-stampedes)
- [424: How do you serve stale content when the origin is down?](#424-how-do-you-serve-stale-content-when-the-origin-is-down)
- [425: How do you support custom domains for SaaS customers?](#425-how-do-you-support-custom-domains-for-saas-customers)
- [426: How do TLS settings compare at the edge?](#426-how-do-tls-settings-compare-at-the-edge)
- [427: How do idle timeouts and long-lived connections differ?](#427-how-do-idle-timeouts-and-long-lived-connections-differ)
- [428: How does gRPC support compare?](#428-how-does-grpc-support-compare)
- [429: What happens to database connections after a failover, and how do you prepare?](#429-what-happens-to-database-connections-after-a-failover-and-how-do-you-prepare)
- [430: How do you run failover game days on each cloud?](#430-how-do-you-run-failover-game-days-on-each-cloud)
- [431: What cost traps catch teams after moving from AWS to Azure, GCP or Cloudflare?](#431-what-cost-traps-catch-teams-after-moving-from-aws-to-azure-gcp-or-cloudflare)
- [432: How do you estimate Durable Objects costs compared with DynamoDB?](#432-how-do-you-estimate-durable-objects-costs-compared-with-dynamodb)
- [433: How do you tune Cosmos DB after migrating from DynamoDB?](#433-how-do-you-tune-cosmos-db-after-migrating-from-dynamodb)
- [434: What Firestore limits bite teams coming from DynamoDB?](#434-what-firestore-limits-bite-teams-coming-from-dynamodb)
- [435: How do you design around D1's limits?](#435-how-do-you-design-around-d1s-limits)
- [436: How do you design around Workers KV limits?](#436-how-do-you-design-around-workers-kv-limits)
- [437: How do you debug and profile Workers in production compared to Lambda?](#437-how-do-you-debug-and-profile-workers-in-production-compared-to-lambda)
- [438: How do you debug cloud functions locally with real cloud resources?](#438-how-do-you-debug-cloud-functions-locally-with-real-cloud-resources)
- [439: How do you restructure a SAM or CDK project into a Cloudflare project?](#439-how-do-you-restructure-a-sam-or-cdk-project-into-a-cloudflare-project)
- [440: How do on-call and operations change after the move?](#440-how-do-on-call-and-operations-change-after-the-move)
- [441: How do you govern Cloudflare accounts and API tokens securely?](#441-how-do-you-govern-cloudflare-accounts-and-api-tokens-securely)
- [442: What questions should you ask before choosing the target cloud?](#442-what-questions-should-you-ask-before-choosing-the-target-cloud)
- [443: What are the most common mistakes when translating AWS to other clouds?](#443-what-are-the-most-common-mistakes-when-translating-aws-to-other-clouds)
- [444: How do you explain the core difference between translating to Azure or GCP and translating to Cloudflare?](#444-how-do-you-explain-the-core-difference-between-translating-to-azure-or-gcp-and-translating-to-cloudflare)
- [445: How do you translate IAM for a Cloudflare-based architecture that still calls AWS, Azure or GCP?](#445-how-do-you-translate-iam-for-a-cloudflare-based-architecture-that-still-calls-aws-azure-or-gcp)
- [446: How do you handle secrets for Workers that need to sign requests to other clouds?](#446-how-do-you-handle-secrets-for-workers-that-need-to-sign-requests-to-other-clouds)
- [447: How would you answer "Is multi-cloud worth it?" in an interview?](#447-how-would-you-answer-is-multi-cloud-worth-it-in-an-interview)
- [448: How do you keep a translated system from drifting back into provider-specific code everywhere?](#448-how-do-you-keep-a-translated-system-from-drifting-back-into-provider-specific-code-everywhere)
- [449: Can you summarize which AWS services have no equivalent on each provider?](#449-can-you-summarize-which-aws-services-have-no-equivalent-on-each-provider)
- [450: What principles make a good AWS translation?](#450-what-principles-make-a-good-aws-translation)

---

# Easy Questions (1-150)

## 1: What does it mean to translate an AWS architecture into Azure, GCP or Cloudflare?

It means rebuilding the same system with another provider's building blocks. You map each AWS service to its closest match, then adjust code, configuration, identity and networking to the way that provider works. Lambda becomes Azure Functions, Cloud Run functions or Workers, S3 becomes Blob Storage, Cloud Storage or R2, and so on.

A good translation keeps the behavior the same for users and changes only what is underneath. Most of the work is not renaming services. It is learning where each provider expects identity, network boundaries, configuration and data to live.

| AWS        | Azure                       | GCP                   | Cloudflare          |
| ---------- | --------------------------- | --------------------- | ------------------- |
| Lambda     | Azure Functions             | Cloud Run functions   | Workers             |
| S3         | Blob Storage                | Cloud Storage         | R2                  |
| DynamoDB   | Cosmos DB                   | Firestore             | D1 / KV             |
| SQS        | Service Bus / Queue Storage | Pub/Sub / Cloud Tasks | Queues              |
| IAM        | Entra ID + Azure RBAC       | Cloud IAM             | API tokens + Access |
| CloudFront | Front Door                  | Cloud CDN             | Cloudflare CDN      |

## 2: How are AWS, Azure, GCP and Cloudflare different in nature?

- **AWS** is the oldest and broadest public cloud. It has the most services, and each one is fairly independent with its own API and configuration style.
- **Azure** is Microsoft's cloud. It is tightly tied to Microsoft Entra ID (formerly Azure Active Directory), Windows Server, SQL Server and Microsoft 365, which makes it popular with enterprises already on Microsoft.
- **GCP** is Google's cloud. It is strong in data and analytics (BigQuery), Kubernetes (GKE was the first managed Kubernetes), AI and a global private network.
- **Cloudflare** started as a CDN and security network and grew into a developer platform. Code and data run on a global edge network in hundreds of cities, and you usually do not pick a region at all. It has no VMs, VPCs or managed Kubernetes.

So translating to Azure or GCP is mostly a one-to-one service mapping, while translating to Cloudflare usually means redesigning parts of the app around edge serverless.

## 3: How does the AWS account structure map to the other providers?

| AWS                      | Azure                                | GCP               | Cloudflare        |
| ------------------------ | ------------------------------------ | ----------------- | ----------------- |
| AWS Organizations (root) | Entra tenant + root management group | Organization      | n/a               |
| Organizational unit (OU) | Management group                     | Folder            | n/a               |
| AWS account              | Subscription                         | Project           | Account           |
| (no direct match)        | Resource group                       | (no direct match) | Zone (per domain) |
| Resource                 | Resource                             | Resource          | Resource          |

The AWS account is both the billing and the security boundary. In Azure, the subscription plays that role, and resource groups add one more layer inside it for grouping resources that share a lifecycle. In GCP, the project is the main boundary, and every resource belongs to exactly one project. In Cloudflare, an account holds Workers, R2 buckets and other resources, and each domain you add is a zone inside that account.

## 4: How do regions and availability zones compare?

- **AWS:** regions (for example `us-east-1`) each contain several availability zones (`us-east-1a`, `us-east-1b`). You pick a region for almost every resource.
- **Azure:** regions (for example `eastus`) and, in many regions, availability zones numbered 1, 2 and 3. Some services are zone-redundant with one setting. Azure also pairs regions for disaster recovery.
- **GCP:** regions (for example `us-central1`) contain zones (`us-central1-a`). Some resources are global (VPC networks, global load balancers), some regional, some zonal.
- **Cloudflare:** one global network. Workers run in the data center closest to the user. You do not choose regions, but you can use placement hints (Smart Placement, location hints for Durable Objects) and jurisdictions (for example `eu`) for data residency.

## 5: What are the command-line tools for each provider?

**AWS**

```bash
aws --version
aws s3 ls
```

**Azure**

```bash
az --version
az group list --output table
```

**GCP**

```bash
gcloud --version
gcloud projects list
```

**Cloudflare**

```bash
npx wrangler --version
npx wrangler whoami
```

`aws`, `az` and `gcloud` cover the whole platform. `wrangler` is focused on the developer platform (Workers, R2, D1, KV, Queues). DNS, WAF and other zone settings are managed through the dashboard, the REST API or Terraform.

## 6: How do you log in from the CLI?

**AWS**

```bash
aws configure sso      # one-time setup of an IAM Identity Center profile
aws sso login --profile dev
```

**Azure**

```bash
az login
az account set --subscription "My Subscription"
```

**GCP**

```bash
gcloud auth login
gcloud config set project my-project
gcloud auth application-default login   # credentials for SDKs on your machine
```

**Cloudflare**

```bash
npx wrangler login
```

For AWS, short-lived SSO credentials are the modern default. Long-lived access keys from `aws configure` still work but are a legacy habit. In GCP, `gcloud auth login` is for the CLI and `application-default login` is for code that uses client libraries.

## 7: What is the equivalent of an IAM user?

- **AWS:** IAM users, or better, users in IAM Identity Center (single sign-on).
- **Azure:** users in Microsoft Entra ID. Identity lives in the tenant, not in a subscription.
- **GCP:** Google accounts or Cloud Identity / Google Workspace users. GCP does not create users itself, it grants IAM roles to identities that exist elsewhere. Workforce Identity Federation lets you use an external IdP such as Okta or Entra ID.
- **Cloudflare:** account members invited by email, optionally with SSO through your IdP.

A common surprise when moving from AWS: there is no "create user" command in `gcloud`. You add an existing Google identity to a role binding.

## 8: What is the equivalent of an IAM role for code running in the cloud?

| AWS                                         | Azure                                      | GCP             | Cloudflare                       |
| ------------------------------------------- | ------------------------------------------ | --------------- | -------------------------------- |
| IAM role (execution role, instance profile) | Managed identity (system or user assigned) | Service account | Bindings (no credentials needed) |

On AWS, a Lambda function or EC2 instance assumes a role and gets temporary credentials. On Azure, you enable a managed identity on the resource and grant it Azure RBAC roles. On GCP, you attach a service account to the resource. On Cloudflare, a Worker gets access to R2, D1 or KV through bindings declared in `wrangler.jsonc`, so there are no credentials to manage at all. To call the Cloudflare API itself, you use an API token.

## 9: How do IAM policies compare to Azure RBAC and GCP IAM?

- **AWS:** JSON policies with `Effect`, `Action`, `Resource` and `Condition`. You attach them to users, roles or resources. Deny always wins.
- **Azure:** a role definition (a list of allowed `actions` and `dataActions`) plus a role assignment that binds a principal to that role at a scope (management group, subscription, resource group or resource). Permissions inherit downward.
- **GCP:** roles (lists of permissions such as `storage.objects.get`) bound to principals in an IAM policy on a resource, project, folder or organization. Bindings inherit downward. Deny policies exist but are separate.
- **Cloudflare:** API tokens with permission groups (for example "Workers Scripts: Edit") scoped to accounts or zones, plus member roles in the dashboard.

The big mental shift: AWS policies list resources inside the policy, while Azure and GCP attach the binding at a scope and let it flow down.

## 10: What is the equivalent of the AWS root user?

- **AWS:** the root user of each account, which you should lock away with MFA and not use day to day.
- **Azure:** the Global Administrator role in Entra ID, plus Owner on the root management group. A Global Administrator can elevate access to manage all subscriptions.
- **GCP:** Organization Administrator, and the Super Administrator of the Cloud Identity or Workspace account.
- **Cloudflare:** the Super Administrator member role on the account.

In all four, the rule is the same: keep very few people at this level, protect them with strong MFA, and do daily work with lower roles.

## 11: How do you enforce MFA?

- **AWS:** enable MFA for the root user and for IAM Identity Center users. AWS now requires MFA for root users.
- **Azure:** Conditional Access policies in Entra ID, or security defaults for smaller tenants. Azure also enforces MFA for sign-ins to the Azure portal and CLI.
- **GCP:** 2-Step Verification enforced in the Google Workspace or Cloud Identity admin console. Google Cloud is rolling out mandatory MFA for all users.
- **Cloudflare:** two-factor authentication on the account, which an admin can enforce for all members, or SSO with your IdP's MFA.

## 12: What is the equivalent of EC2?

- **AWS:** Amazon EC2.
- **Azure:** Azure Virtual Machines.
- **GCP:** Compute Engine.

Cloudflare has no virtual machines. If a workload truly needs a full VM, it stays on one of the other clouds, or you move it to Cloudflare Containers when it can run in a container.

## 13: How do you create a virtual machine from the CLI?

**AWS**

```bash
aws ec2 run-instances \
  --image-id ami-0abcdef1234567890 \
  --instance-type t3.micro \
  --key-name my-key \
  --subnet-id subnet-0123456789abcdef0
```

**Azure**

```bash
az vm create \
  --resource-group my-rg \
  --name my-vm \
  --image Ubuntu2404 \
  --size Standard_B2s \
  --generate-ssh-keys
```

**GCP**

```bash
gcloud compute instances create my-vm \
  --zone us-central1-a \
  --machine-type e2-small \
  --image-family ubuntu-2404-lts-amd64 \
  --image-project ubuntu-os-cloud
```

Azure needs a resource group first (`az group create`). GCP picks the default VPC network if you do not pass one.

## 14: How do instance type names compare?

| Purpose           | AWS            | Azure                        | GCP                          |
| ----------------- | -------------- | ---------------------------- | ---------------------------- |
| Burstable / small | `t3`, `t4g`    | B-series (`Standard_B2s`)    | `e2`, shared-core `e2-micro` |
| General purpose   | `m7i`, `m7g`   | D-series (`Standard_D4s_v5`) | `n2`, `n4`, `c4a`            |
| Compute optimized | `c7i`, `c7g`   | F-series                     | `c3`, `c4`, `h3`             |
| Memory optimized  | `r7i`, `x2idn` | E-series, M-series           | `m3`, `n2-highmem`           |
| GPU               | `p5`, `g6`     | NC, ND, NV series            | `a3`, `g2`                   |

ARM equivalents: AWS Graviton (`*g` types), Azure Cobalt (for example `Dpsv6`), Google Axion (`c4a`). Exact generations change often, so check the current list before sizing a migration.

## 15: What is the equivalent of an AMI?

- **AWS:** Amazon Machine Image (AMI).
- **Azure:** a VM image, stored as a managed image or, better, in an Azure Compute Gallery for versioning and sharing across regions.
- **GCP:** a Compute Engine image, grouped into image families so `--image-family` always picks the latest.

To build custom images on all three, teams often use HashiCorp Packer with a builder per cloud (`amazon-ebs`, `azure-arm`, `googlecompute`).

## 16: What is the equivalent of EBS?

- **AWS:** Elastic Block Store volumes (`gp3`, `io2`).
- **Azure:** Managed Disks (Standard HDD, Standard SSD, Premium SSD, Premium SSD v2, Ultra Disk).
- **GCP:** Persistent Disk (`pd-balanced`, `pd-ssd`) and the newer Hyperdisk (`hyperdisk-balanced`, `hyperdisk-extreme`).

One difference: on AWS and Azure, volume performance depends on the volume type and size settings. On GCP Persistent Disk, it also scales with disk size, while Hyperdisk lets you set IOPS and throughput directly like `gp3` or `io2`.

## 17: What is the equivalent of a security group?

- **AWS:** security groups (stateful, attached to network interfaces) and network ACLs (stateless, on subnets).
- **Azure:** network security groups (NSGs), stateful rules attached to subnets or network interfaces, plus application security groups to group VMs by role.
- **GCP:** VPC firewall rules and network firewall policies, applied to the whole VPC and targeted with network tags or service accounts.

AWS security groups only have allow rules. Azure NSGs and GCP firewall rules have both allow and deny rules with priorities, so rule order matters.

## 18: How do you connect to a VM over SSH without opening port 22?

- **AWS:** Systems Manager Session Manager (`aws ssm start-session --target i-0123...`) or EC2 Instance Connect Endpoint.
- **Azure:** Azure Bastion (`az network bastion ssh ...`) or Entra ID login for Linux VMs.
- **GCP:** Identity-Aware Proxy TCP forwarding: `gcloud compute ssh my-vm --tunnel-through-iap`, with OS Login for user management.
- **Cloudflare:** Cloudflare Tunnel (`cloudflared`) on the server, with Cloudflare Access in front of it, so users reach SSH through Cloudflare with SSO and no open inbound ports.

## 19: What is the equivalent of Spot Instances?

- **AWS:** EC2 Spot Instances, with a two-minute interruption notice.
- **Azure:** Azure Spot Virtual Machines, with a 30-second eviction notice through Scheduled Events.
- **GCP:** Spot VMs (the older name is preemptible VMs), with a 30-second preemption notice.

All three give large discounts in exchange for being stopped when the provider needs capacity back. Workloads must be stateless or able to checkpoint.

## 20: What is the equivalent of an Elastic IP?

- **AWS:** Elastic IP address.
- **Azure:** a static public IP address resource (`az network public-ip create --allocation-method Static`).
- **GCP:** a reserved static external IP address (`gcloud compute addresses create my-ip --region us-central1`).

On AWS, all public IPv4 addresses are now billed hourly. Azure and GCP also charge for public IPs, so reserve only what you need.

## 21: What is the equivalent of EC2 user data?

- **AWS:** user data, a script or cloud-init config run at first boot.
- **Azure:** custom data (cloud-init on Linux), passed with `az vm create --custom-data cloud-init.yaml`.
- **GCP:** a startup script in instance metadata, which runs on every boot: `--metadata-from-file startup-script=startup.sh`.

Note the difference: EC2 user data runs only on first boot by default, while a GCP startup script runs on every boot.

## 22: What is the equivalent of an Auto Scaling group?

- **AWS:** EC2 Auto Scaling groups with a launch template.
- **Azure:** Virtual Machine Scale Sets.
- **GCP:** managed instance groups (MIGs) with an instance template and an autoscaler.

All three can scale on CPU, custom metrics or a schedule, and replace unhealthy instances based on health checks.

## 23: What is the equivalent of AWS Lambda?

- **AWS:** AWS Lambda.
- **Azure:** Azure Functions (the Flex Consumption plan is the modern serverless option).
- **GCP:** Cloud Run functions (formerly Cloud Functions), which run on Cloud Run.
- **Cloudflare:** Cloudflare Workers.

Lambda, Azure Functions and Cloud Run functions run your code in containers or microVMs in one region. Workers run in V8 isolates on every Cloudflare location, start in milliseconds, and are billed by CPU time instead of wall-clock time.

## 24: How do you write a simple HTTP function in each?

**AWS**

```ts
import type { APIGatewayProxyHandlerV2 } from "aws-lambda";

export const handler: APIGatewayProxyHandlerV2 = async (event) => {
  const name = event.queryStringParameters?.name ?? "world";
  return { statusCode: 200, body: `Hello, ${name}!` };
};
```

**Azure**

```ts
import { app, HttpRequest, HttpResponseInit } from "@azure/functions";

app.http("hello", {
  methods: ["GET"],
  authLevel: "anonymous",
  handler: async (request: HttpRequest): Promise<HttpResponseInit> => {
    const name = request.query.get("name") ?? "world";
    return { body: `Hello, ${name}!` };
  },
});
```

**GCP**

```ts
import * as functions from "@google-cloud/functions-framework";

functions.http("hello", (req, res) => {
  const name = (req.query.name as string) ?? "world";
  res.send(`Hello, ${name}!`);
});
```

**Cloudflare**

```ts
export default {
  async fetch(request: Request): Promise<Response> {
    const name = new URL(request.url).searchParams.get("name") ?? "world";
    return new Response(`Hello, ${name}!`);
  },
} satisfies ExportedHandler;
```

GCP uses an Express-style `req`/`res`. Workers use the standard web `Request` and `Response`, the same API as `fetch` in the browser.

## 25: How do you deploy a function from the CLI?

**AWS**

```bash
zip function.zip index.mjs
aws lambda create-function \
  --function-name hello \
  --runtime nodejs22.x \
  --handler index.handler \
  --zip-file fileb://function.zip \
  --role arn:aws:iam::123456789012:role/hello-lambda-role
```

**Azure**

```bash
func azure functionapp publish my-func-app
```

**GCP**

```bash
gcloud functions deploy hello \
  --gen2 --runtime nodejs22 --region us-central1 \
  --source . --entry-point hello \
  --trigger-http --allow-unauthenticated
```

**Cloudflare**

```bash
npx wrangler deploy
```

Most teams use a framework instead of raw CLI calls: AWS SAM, CDK or Terraform on AWS, Bicep or Terraform on Azure, Terraform on GCP, and Wrangler (plus optional Terraform) on Cloudflare. The Azure function app itself must exist first (`az functionapp create`).

## 26: What kinds of triggers can a function have?

| Trigger          | AWS Lambda                | Azure Functions             | Cloud Run functions      | Workers                         |
| ---------------- | ------------------------- | --------------------------- | ------------------------ | ------------------------------- |
| HTTP             | Function URL, API Gateway | HTTP trigger                | HTTP trigger             | `fetch` handler                 |
| Schedule         | EventBridge Scheduler     | Timer trigger               | Cloud Scheduler          | Cron Triggers (`scheduled`)     |
| Queue            | SQS                       | Service Bus / Storage queue | Pub/Sub                  | Queues (`queue` handler)        |
| Object storage   | S3 events                 | Blob trigger / Event Grid   | Eventarc (Cloud Storage) | R2 event notifications          |
| Database changes | DynamoDB Streams          | Cosmos DB trigger           | Firestore triggers       | n/a                             |
| Email            | SES receipt rules         | n/a                         | n/a                      | Email Routing (`email` handler) |

Workers is the only one where the event type is a method on one exported object (`fetch`, `scheduled`, `queue`, `email`).

## 27: How do function limits compare?

| Limit        | AWS Lambda        | Azure Functions (Flex Consumption)                        | Cloud Run functions       | Workers (paid)                                                                        |
| ------------ | ----------------- | --------------------------------------------------------- | ------------------------- | ------------------------------------------------------------------------------------- |
| Max duration | 15 minutes        | Unbounded for non-HTTP (HTTP has a 230 s front-end limit) | 60 minutes (HTTP)         | No wall-clock limit while the client is connected; CPU time default 30 s, up to 5 min |
| Memory       | 128 MB to 10 GB   | 512 MB, 2 GB or 4 GB instances                            | up to 32 GiB              | 128 MB per isolate                                                                    |
| Billing      | Duration x memory | Execution time x memory                                   | CPU and memory per second | CPU time + requests                                                                   |

Limits change often, so always check the current docs before a migration. The key point is that Workers have little memory and limited CPU time per request, so heavy work belongs in Containers or another cloud.

## 28: What are cold starts and how do they compare?

A cold start is the delay when the platform has to start a new instance before handling a request.

- **AWS Lambda:** hundreds of milliseconds for Node.js, more with large packages or Java. Fixed with provisioned concurrency or SnapStart (Java, Python, .NET).
- **Azure Functions:** similar, and fixed on Flex Consumption with always-ready instances.
- **Cloud Run functions:** container start time. Fixed with minimum instances.
- **Cloudflare Workers:** isolates start in a few milliseconds, and Cloudflare often warms the Worker during the TLS handshake, so cold starts are rarely an issue.

## 29: How do you set environment variables for a function?

**AWS**

```bash
aws lambda update-function-configuration --function-name hello \
  --environment "Variables={STAGE=prod,LOG_LEVEL=info}"
```

**Azure**

```bash
az functionapp config appsettings set --name my-func-app --resource-group my-rg \
  --settings STAGE=prod LOG_LEVEL=info
```

**GCP**

```bash
gcloud functions deploy hello --update-env-vars STAGE=prod,LOG_LEVEL=info
```

**Cloudflare**

```jsonc
// wrangler.jsonc
{
  "vars": { "STAGE": "prod", "LOG_LEVEL": "info" },
}
```

In Workers, variables are read from the `env` argument (`env.STAGE`), not `process.env`. With the `nodejs_compat` flag, `process.env` can be populated too, but `env` is the normal way.

## 30: What is the equivalent of AWS Secrets Manager?

- **AWS:** Secrets Manager (and SecureString parameters in SSM Parameter Store).
- **Azure:** Azure Key Vault secrets.
- **GCP:** Secret Manager.
- **Cloudflare:** Worker secrets (`wrangler secret put`) and Secrets Store for secrets shared across Workers in an account.

**AWS**

```bash
aws secretsmanager create-secret --name db-password --secret-string 's3cr3t'
```

**Azure**

```bash
az keyvault secret set --vault-name my-vault --name db-password --value 's3cr3t'
```

**GCP**

```bash
printf 's3cr3t' | gcloud secrets create db-password --data-file=-
```

**Cloudflare**

```bash
npx wrangler secret put DB_PASSWORD
```

## 31: What is the equivalent of SSM Parameter Store for plain configuration?

- **AWS:** Systems Manager Parameter Store (and AWS AppConfig for feature flags and dynamic config).
- **Azure:** Azure App Configuration, which also has feature flags and can reference Key Vault secrets.
- **GCP:** Parameter Manager, which stores versioned configuration and can reference Secret Manager secrets.
- **Cloudflare:** `vars` in `wrangler.jsonc` for static config, or Workers KV for config you want to change without redeploying.

## 32: What is the equivalent of Amazon S3?

- **AWS:** Amazon S3.
- **Azure:** Azure Blob Storage, inside a storage account.
- **GCP:** Cloud Storage.
- **Cloudflare:** R2, which exposes an S3-compatible API and charges no egress fees.

| Concept        | AWS S3 | Azure Blob Storage           | Cloud Storage | R2          |
| -------------- | ------ | ---------------------------- | ------------- | ----------- |
| Top-level unit | Bucket | Storage account -> container | Bucket        | Bucket      |
| Item           | Object | Blob                         | Object        | Object      |
| Name scope     | Global | Account name is global       | Global        | Per account |

## 33: Why does Azure have storage accounts on top of containers?

In Azure, a storage account is the top-level resource. It sets the region, redundancy (LRS, ZRS, GRS), performance tier and networking rules, and it holds blob containers, file shares, queues and tables together. The account name must be globally unique and becomes part of the URL: `https://myaccount.blob.core.windows.net/mycontainer/file.txt`.

When translating an S3 bucket, you usually create one storage account per app or environment and one container per S3 bucket. Settings that were per-bucket on AWS (like replication) are often per-account on Azure.

## 34: How do you upload and download a file from the CLI?

**AWS**

```bash
aws s3 cp ./report.pdf s3://my-bucket/reports/report.pdf
aws s3 cp s3://my-bucket/reports/report.pdf ./report.pdf
```

**Azure**

```bash
az storage blob upload --account-name myaccount --container-name reports \
  --name report.pdf --file ./report.pdf --auth-mode login
az storage blob download --account-name myaccount --container-name reports \
  --name report.pdf --file ./report.pdf --auth-mode login
```

**GCP**

```bash
gcloud storage cp ./report.pdf gs://my-bucket/reports/report.pdf
gcloud storage cp gs://my-bucket/reports/report.pdf ./report.pdf
```

**Cloudflare**

```bash
npx wrangler r2 object put my-bucket/reports/report.pdf --file ./report.pdf --remote
npx wrangler r2 object get my-bucket/reports/report.pdf --file ./report.pdf --remote
```

`gcloud storage` replaces the older `gsutil`. For bulk copies, `azcopy` is the fast Azure tool, and for R2 you can point the AWS CLI or `rclone` at the R2 S3 endpoint.

## 35: How do storage classes compare?

| Access pattern        | AWS S3                          | Azure Blob                   | Cloud Storage | R2                |
| --------------------- | ------------------------------- | ---------------------------- | ------------- | ----------------- |
| Frequent              | Standard                        | Hot                          | Standard      | Standard          |
| Infrequent (~monthly) | Standard-IA, One Zone-IA        | Cool                         | Nearline      | Infrequent Access |
| Rare (~quarterly)     | Glacier Instant Retrieval       | Cold                         | Coldline      | n/a               |
| Archive (~yearly)     | Glacier Flexible / Deep Archive | Archive                      | Archive       | n/a               |
| Automatic             | Intelligent-Tiering             | Lifecycle rules / smart tier | Autoclass     | n/a               |

Retrieval rules differ: Azure Archive blobs must be rehydrated before reading (hours), while GCP Archive objects are readable right away with a higher retrieval fee. S3 Glacier Flexible Retrieval and Deep Archive also need a restore step.

## 36: What is the equivalent of an S3 presigned URL?

- **AWS:** presigned URL, signed with SigV4.
- **Azure:** shared access signature (SAS) token, best as a user delegation SAS signed with Entra ID credentials.
- **GCP:** signed URL, signed with a service account key or through the IAM `signBlob` API.
- **Cloudflare:** R2 presigned URL using the S3 API (the same AWS SDK code works against the R2 endpoint).

**GCP**

```bash
gcloud storage sign-url gs://my-bucket/report.pdf --duration=15m \
  --impersonate-service-account=signer@my-project.iam.gserviceaccount.com
```

## 37: How do you host a static website?

- **AWS:** S3 bucket + CloudFront (or AWS Amplify Hosting).
- **Azure:** Azure Static Web Apps, or the static website feature of a storage account behind Front Door.
- **GCP:** Firebase Hosting, or a Cloud Storage bucket behind an external Application Load Balancer with Cloud CDN.
- **Cloudflare:** Workers with static assets (or Cloudflare Pages). Assets are served from the edge for free, and you can add a Worker for dynamic routes.

**Cloudflare**

```jsonc
// wrangler.jsonc
{
  "name": "my-site",
  "compatibility_date": "2026-11-24",
  "assets": { "directory": "./dist" },
}
```

## 38: What is the equivalent of S3 versioning?

- **AWS:** S3 Versioning, enabled per bucket.
- **Azure:** blob versioning, enabled per storage account, plus soft delete for blobs and containers.
- **GCP:** Object Versioning on the bucket, plus soft delete, which is on by default with a 7-day retention.

R2 does not keep old object versions, so if you need history on Cloudflare, store versioned keys yourself (for example `reports/2026-11-24/report.pdf`).

## 39: What is the equivalent of S3 lifecycle rules?

- **AWS:** lifecycle configuration with transitions and expirations.
- **Azure:** lifecycle management policies on the storage account.
- **GCP:** Object Lifecycle Management rules on the bucket.
- **Cloudflare:** R2 object lifecycle rules (delete after N days, move to Infrequent Access, abort incomplete multipart uploads).

Lifecycle rules on R2 are set in the dashboard, through the S3-compatible `PutBucketLifecycleConfiguration` API, or with `wrangler r2 bucket lifecycle add`.

## 40: What is the equivalent of DynamoDB?

- **AWS:** DynamoDB, a key-value and document database.
- **Azure:** Azure Cosmos DB (the NoSQL API is the closest match), with partition keys and request units (RUs).
- **GCP:** Firestore for documents, or Bigtable for very large wide-column workloads.
- **Cloudflare:** no exact match. Use D1 (SQLite) for relational data, Workers KV for simple global key-value reads, or Durable Objects for strongly consistent per-entity state.

DynamoDB and Cosmos DB are the closest pair: both partition by key, both bill by throughput, both have on-demand and provisioned modes.

## 41: What is the equivalent of Amazon RDS?

| Engine     | AWS RDS            | Azure                                         | GCP                      | Cloudflare                   |
| ---------- | ------------------ | --------------------------------------------- | ------------------------ | ---------------------------- |
| PostgreSQL | RDS for PostgreSQL | Azure Database for PostgreSQL flexible server | Cloud SQL for PostgreSQL | Hyperdrive (connects to one) |
| MySQL      | RDS for MySQL      | Azure Database for MySQL flexible server      | Cloud SQL for MySQL      | Hyperdrive (connects to one) |
| SQL Server | RDS for SQL Server | Azure SQL Database / Managed Instance         | Cloud SQL for SQL Server | n/a                          |
| SQLite     | n/a                | n/a                                           | n/a                      | D1                           |

Cloudflare does not host Postgres or MySQL. Hyperdrive is a connection pooler and query cache that makes a database hosted elsewhere fast to reach from Workers. D1 is Cloudflare's own serverless SQLite database.

## 42: What is the equivalent of Aurora?

- **AWS:** Amazon Aurora (PostgreSQL and MySQL compatible), Aurora Serverless v2, and Aurora DSQL for distributed SQL.
- **Azure:** Azure SQL Database Hyperscale for SQL Server workloads and Azure Database for PostgreSQL flexible server for Postgres workloads.
- **GCP:** AlloyDB for PostgreSQL, and Spanner for globally distributed SQL.

AlloyDB is the closest match to Aurora PostgreSQL: separate compute and storage, fast read replicas and Postgres compatibility. Spanner is closer to Aurora DSQL.

## 43: What is the equivalent of ElastiCache?

- **AWS:** ElastiCache (Valkey, Redis OSS, Memcached) and MemoryDB.
- **Azure:** Azure Managed Redis. The older Azure Cache for Redis is being retired, so new work should not use it.
- **GCP:** Memorystore for Valkey, Memorystore for Redis Cluster, and Memorystore for Memcached.

Cloudflare has no managed Redis. For caching inside Workers, you use the Cache API, Workers KV, or Hyperdrive's query cache. To reach an existing Redis, you connect over TCP from a Worker or a Container.

## 44: What is the equivalent of Redshift?

- **AWS:** Amazon Redshift.
- **Azure:** Microsoft Fabric Data Warehouse (Azure Synapse Analytics dedicated SQL pools are the older option).
- **GCP:** BigQuery.

BigQuery is fully serverless and billed by bytes scanned or reserved slots, so there is no cluster to size. Redshift Serverless is the closest AWS model to it.

## 45: What is the equivalent of Athena?

- **AWS:** Amazon Athena, SQL over files in S3.
- **Azure:** Microsoft Fabric (SQL over OneLake files and shortcuts) or Synapse serverless SQL pools.
- **GCP:** BigQuery external tables and BigLake tables over Cloud Storage.
- **Cloudflare:** R2 SQL, a serverless query engine over Apache Iceberg tables in R2 Data Catalog.

## 46: What is the equivalent of SQS?

- **AWS:** Amazon SQS (standard and FIFO).
- **Azure:** Azure Service Bus queues for business messaging, or Azure Queue Storage for simple, cheap queues.
- **GCP:** Pub/Sub (with a pull subscription acting like a queue) or Cloud Tasks for HTTP task dispatch with rate limits.
- **Cloudflare:** Cloudflare Queues, with Workers as producers and consumers.

## 47: What is the equivalent of SNS?

- **AWS:** Amazon SNS topics with subscriptions.
- **Azure:** Service Bus topics and subscriptions, or Event Grid for lightweight event fan-out.
- **GCP:** Pub/Sub topics with multiple subscriptions.

Cloudflare has no topic service. To fan out on Cloudflare, a Worker sends the message to several Queues or calls other Workers through service bindings.

## 48: What is the equivalent of EventBridge?

- **AWS:** Amazon EventBridge (event buses, rules, Pipes and Scheduler).
- **Azure:** Event Grid (system topics for Azure events, custom topics and namespaces).
- **GCP:** Eventarc, which routes events from Google services, Pub/Sub and third parties to Cloud Run, Workflows and others.

Event Grid and Eventarc both use the CloudEvents format natively. EventBridge uses its own JSON envelope (`source`, `detail-type`, `detail`).

## 49: What is the equivalent of Kinesis?

- **AWS:** Kinesis Data Streams for streaming, Amazon Data Firehose for delivery to storage.
- **Azure:** Event Hubs (also speaks the Kafka protocol), with Stream Analytics for processing.
- **GCP:** Pub/Sub for ingestion, Dataflow for processing, and BigQuery subscriptions to write straight into BigQuery.
- **Cloudflare:** Pipelines, which ingests events over HTTP or from Workers and writes them to R2 as Iceberg tables.

## 50: What is the equivalent of Step Functions?

- **AWS:** AWS Step Functions (state machines in Amazon States Language). Lambda durable functions are a newer code-first option.
- **Azure:** Durable Functions (code-first orchestration) or Logic Apps (low-code workflows).
- **GCP:** Workflows (YAML or JSON steps).
- **Cloudflare:** Workflows, written as TypeScript code with `step.do()` and `step.sleep()`.

Step Functions and GCP Workflows are config-driven. Durable Functions, Lambda durable functions and Cloudflare Workflows are code-driven and replay your function to restore state.

## 51: How do you run code on a schedule?

**AWS**

```bash
aws scheduler create-schedule --name nightly \
  --schedule-expression "cron(0 2 * * ? *)" \
  --flexible-time-window Mode=OFF \
  --target '{"Arn":"arn:aws:lambda:us-east-1:123456789012:function:nightly","RoleArn":"arn:aws:iam::123456789012:role/scheduler-role"}'
```

**Azure**

```ts
import { app, Timer } from "@azure/functions";

app.timer("nightly", {
  schedule: "0 0 2 * * *", // NCRONTAB with seconds
  handler: async (timer: Timer) => {
    // work
  },
});
```

**GCP**

```bash
gcloud scheduler jobs create http nightly --location us-central1 \
  --schedule "0 2 * * *" --uri https://nightly-abc123-uc.a.run.app \
  --oidc-service-account-email scheduler@my-project.iam.gserviceaccount.com
```

**Cloudflare**

```jsonc
// wrangler.jsonc
{ "triggers": { "crons": ["0 2 * * *"] } }
```

Watch the cron formats: AWS has six fields with `?`, Azure has six fields starting with seconds, and GCP and Cloudflare use standard five-field cron.

## 52: What is the equivalent of a VPC?

- **AWS:** Amazon VPC, regional, with subnets in each availability zone.
- **Azure:** Azure Virtual Network (VNet), regional, with subnets that span all zones in the region.
- **GCP:** VPC network, which is global, with regional subnets.

Cloudflare has no customer VPC. Workers run on Cloudflare's network, and you reach private resources through Cloudflare Tunnel or Hyperdrive.

## 53: How do subnets differ between AWS, Azure and GCP?

- **AWS:** a subnet lives in one availability zone. "Public" or "private" depends on whether its route table points at an internet gateway.
- **Azure:** a subnet spans the whole region (all zones). VMs get outbound internet through a NAT gateway, load balancer or public IP. Default outbound access is being retired for new VNets, so explicit outbound is now the norm.
- **GCP:** a subnet is regional and spans all zones. The VPC itself is global, so subnets in different regions talk to each other without peering.

So an AWS design with three subnets per tier (one per zone) usually becomes one subnet per tier on Azure and GCP.

## 54: What is the equivalent of a NAT gateway?

- **AWS:** NAT gateway, one per availability zone for high availability.
- **Azure:** Azure NAT Gateway, attached to subnets.
- **GCP:** Cloud NAT, a software-defined service on a Cloud Router, with no single gateway VM.

There is no AWS-style internet gateway resource on Azure or GCP. Internet access is part of the network by default or through these NAT services.

## 55: What is the equivalent of Route 53?

- **AWS:** Route 53 (DNS, health checks, routing policies, domain registration).
- **Azure:** Azure DNS for hosting zones, and Traffic Manager for DNS-based routing.
- **GCP:** Cloud DNS, with routing policies (weighted, geolocation, failover).
- **Cloudflare:** Cloudflare DNS, one of the fastest authoritative DNS services, free on all plans, with Load Balancing for health-checked routing.

## 56: How do you create a DNS record from the CLI?

**AWS**

```bash
aws route53 change-resource-record-sets --hosted-zone-id Z123EXAMPLE \
  --change-batch '{"Changes":[{"Action":"UPSERT","ResourceRecordSet":{"Name":"api.example.com","Type":"A","TTL":300,"ResourceRecords":[{"Value":"203.0.113.10"}]}}]}'
```

**Azure**

```bash
az network dns record-set a add-record --resource-group my-rg \
  --zone-name example.com --record-set-name api --ipv4-address 203.0.113.10
```

**GCP**

```bash
gcloud dns record-sets create api.example.com. --zone=example-zone \
  --type=A --ttl=300 --rrdatas=203.0.113.10
```

**Cloudflare**

```bash
curl -X POST "https://api.cloudflare.com/client/v4/zones/$ZONE_ID/dns_records" \
  -H "Authorization: Bearer $CF_API_TOKEN" -H "Content-Type: application/json" \
  --data '{"type":"A","name":"api","content":"203.0.113.10","ttl":1,"proxied":true}'
```

On Cloudflare, `"proxied": true` sends traffic through the Cloudflare network (CDN, WAF, DDoS protection), and `ttl: 1` means automatic.

## 57: What is the equivalent of CloudFront?

- **AWS:** Amazon CloudFront.
- **Azure:** Azure Front Door (Standard or Premium). The classic Azure CDN options are being retired.
- **GCP:** Cloud CDN, enabled on an external Application Load Balancer backend, or Media CDN for video.
- **Cloudflare:** the Cloudflare CDN, on by default for every proxied DNS record.

On Cloudflare, you do not create a "distribution". You point DNS at Cloudflare, set records to proxied, and control caching with Cache Rules.

## 58: What is the equivalent of an Application Load Balancer?

- **AWS:** Application Load Balancer (ALB), regional, layer 7.
- **Azure:** Application Gateway (regional, layer 7, optional WAF) or Front Door (global).
- **GCP:** external Application Load Balancer, global by default, with URL maps.
- **Cloudflare:** Cloudflare Load Balancing, which balances across origins anywhere with health checks and steering policies.

GCP's global load balancer has one anycast IP for all regions, which on AWS needs Global Accelerator plus regional ALBs.

## 59: What is the equivalent of a Network Load Balancer?

- **AWS:** Network Load Balancer (NLB), layer 4.
- **Azure:** Azure Load Balancer (Standard SKU).
- **GCP:** external or internal passthrough Network Load Balancer, or the proxy Network Load Balancer.
- **Cloudflare:** Spectrum, which proxies TCP and UDP traffic through Cloudflare with DDoS protection.

## 60: What is the equivalent of API Gateway?

- **AWS:** Amazon API Gateway (REST, HTTP and WebSocket APIs).
- **Azure:** Azure API Management (APIM), including a Consumption tier for serverless use.
- **GCP:** API Gateway for simple serverless APIs, or Apigee for full API management.
- **Cloudflare:** usually a Worker in front of your services, plus API Shield for schema validation and mTLS, and rate limiting rules.

For a simple Lambda HTTP endpoint, a Lambda function URL replaces API Gateway, and on GCP and Azure the function's own HTTPS URL plays the same role.

## 61: What is the equivalent of AWS WAF?

- **AWS:** AWS WAF, attached to CloudFront, ALB or API Gateway.
- **Azure:** Azure Web Application Firewall on Front Door or Application Gateway.
- **GCP:** Google Cloud Armor security policies on external load balancers.
- **Cloudflare:** Cloudflare WAF with managed rulesets (Cloudflare Managed Ruleset, OWASP Core Ruleset) and custom rules written in the Rules language.

All four support managed rule sets, custom rules on headers and paths, geo blocking and rate limiting. Cloudflare applies them at the edge for every proxied hostname without a separate resource to attach.

## 62: What is the equivalent of AWS Shield?

- **AWS:** Shield Standard (free, automatic) and Shield Advanced (paid, with response team and cost protection).
- **Azure:** Azure DDoS Network Protection (paid, per VNet) or DDoS IP Protection (per public IP), on top of free basic protection.
- **GCP:** Cloud Armor, with Cloud Armor Enterprise for advanced DDoS protection and support.
- **Cloudflare:** unmetered DDoS protection included on every plan, at layers 3, 4 and 7.

## 63: What is the equivalent of AWS Certificate Manager?

- **AWS:** AWS Certificate Manager (ACM), free public certificates for AWS load balancers and CloudFront.
- **Azure:** managed certificates in Front Door, App Service and Container Apps, and Key Vault for certificates you bring.
- **GCP:** Certificate Manager and Google-managed SSL certificates on load balancers.
- **Cloudflare:** Universal SSL (free, automatic for proxied hostnames), Advanced Certificate Manager, and custom certificates.

On Cloudflare there are two TLS legs: browser to Cloudflare (edge certificate) and Cloudflare to your origin. Set SSL/TLS mode to Full (strict) so the origin certificate is validated too.

## 64: What is the equivalent of CloudWatch Logs?

- **AWS:** CloudWatch Logs, with log groups and Logs Insights queries.
- **Azure:** Azure Monitor Logs, stored in a Log Analytics workspace and queried with KQL.
- **GCP:** Cloud Logging, with log buckets, the Logs Explorer and the Logging query language.
- **Cloudflare:** Workers Logs (enable `observability` in `wrangler.jsonc`), `wrangler tail` for live logs, and Logpush to send logs to R2 or another tool.

**Cloudflare**

```jsonc
// wrangler.jsonc
{ "observability": { "enabled": true } }
```

## 65: What is the equivalent of CloudWatch metrics and alarms?

- **AWS:** CloudWatch metrics, dashboards and alarms, with SNS for notifications.
- **Azure:** Azure Monitor metrics, workbooks, alert rules and action groups.
- **GCP:** Cloud Monitoring metrics, dashboards, alerting policies and notification channels.
- **Cloudflare:** analytics dashboards per product, the GraphQL Analytics API, Workers Analytics Engine for custom metrics, and Notifications for alerts.

## 66: What is the equivalent of AWS X-Ray?

- **AWS:** AWS X-Ray, now usually used through OpenTelemetry (AWS Distro for OpenTelemetry or CloudWatch Application Signals).
- **Azure:** Application Insights, part of Azure Monitor, with the Azure Monitor OpenTelemetry Distro.
- **GCP:** Cloud Trace, which accepts OpenTelemetry data.
- **Cloudflare:** Workers tracing in Workers Observability, with automatic spans for bindings and `fetch` calls, and OpenTelemetry export to an external backend.

OpenTelemetry is the safest choice for a migration: instrument once and change only the exporter.

## 67: What is the equivalent of CloudTrail?

- **AWS:** AWS CloudTrail, which records API calls.
- **Azure:** the Azure Activity Log for control-plane operations, plus resource logs (diagnostic settings) for data-plane operations and Entra ID sign-in and audit logs.
- **GCP:** Cloud Audit Logs: Admin Activity (always on), Data Access (opt-in), System Event and Policy Denied logs.
- **Cloudflare:** Audit Logs for account and zone changes, available in the dashboard, API and Logpush.

## 68: What is the equivalent of CloudFormation?

- **AWS:** AWS CloudFormation (and CDK, which compiles to CloudFormation).
- **Azure:** Azure Resource Manager (ARM) templates, usually written in Bicep.
- **GCP:** Infrastructure Manager, which runs Terraform for you. Deployment Manager is deprecated.
- **Cloudflare:** no native template service. Use `wrangler.jsonc` for Workers and their bindings, and the Cloudflare Terraform provider for everything else.

Terraform (or OpenTofu) works on all four, which is why many teams move to it during a multi-cloud migration.

## 69: How do you create a storage bucket with Terraform on each provider?

**AWS**

```hcl
resource "aws_s3_bucket" "files" {
  bucket = "my-app-files-123"
}
```

**Azure**

```hcl
resource "azurerm_storage_account" "files" {
  name                     = "myappfiles123"
  resource_group_name      = azurerm_resource_group.main.name
  location                 = "eastus"
  account_tier             = "Standard"
  account_replication_type = "ZRS"
}

resource "azurerm_storage_container" "files" {
  name               = "files"
  storage_account_id = azurerm_storage_account.files.id
}
```

**GCP**

```hcl
resource "google_storage_bucket" "files" {
  name                        = "my-app-files-123"
  location                    = "US-CENTRAL1"
  uniform_bucket_level_access = true
}
```

**Cloudflare**

```hcl
resource "cloudflare_r2_bucket" "files" {
  account_id = var.cloudflare_account_id
  name       = "my-app-files"
}
```

## 70: What is the equivalent of ECR?

- **AWS:** Amazon Elastic Container Registry (ECR).
- **Azure:** Azure Container Registry (ACR).
- **GCP:** Artifact Registry. Container Registry (`gcr.io`) has been shut down, and `gcr.io` names are now served from Artifact Registry.
- **Cloudflare:** a built-in registry used by Cloudflare Containers (`wrangler containers push`), which can also pull public images from Docker Hub.

Artifact Registry also stores npm, Maven, Python and other packages, which on AWS is CodeArtifact.

## 71: How do you push a container image?

**AWS**

```bash
aws ecr get-login-password --region us-east-1 | docker login --username AWS \
  --password-stdin 123456789012.dkr.ecr.us-east-1.amazonaws.com
docker push 123456789012.dkr.ecr.us-east-1.amazonaws.com/api:1.0.0
```

**Azure**

```bash
az acr login --name myregistry
docker push myregistry.azurecr.io/api:1.0.0
```

**GCP**

```bash
gcloud auth configure-docker us-central1-docker.pkg.dev
docker push us-central1-docker.pkg.dev/my-project/my-repo/api:1.0.0
```

**Cloudflare**

```bash
npx wrangler containers push api:1.0.0
```

With Cloudflare Containers, `wrangler deploy` usually builds and pushes the image for you based on the `containers` section of `wrangler.jsonc`.

## 72: What is the equivalent of ECS on Fargate?

- **AWS:** Amazon ECS on Fargate (ECS Express Mode is a simpler way to run a web service).
- **Azure:** Azure Container Apps for services and jobs, or Azure Container Instances for single containers.
- **GCP:** Cloud Run services and Cloud Run jobs.
- **Cloudflare:** Cloudflare Containers, started and routed by a Worker and backed by a Durable Object per container instance.

Cloud Run and Container Apps are closer to "Fargate plus a load balancer plus autoscaling in one resource". You deploy an image and get an HTTPS URL.

## 73: What is the equivalent of EKS?

- **AWS:** Amazon EKS (and EKS Auto Mode for managed nodes).
- **Azure:** Azure Kubernetes Service (AKS), including AKS Automatic.
- **GCP:** Google Kubernetes Engine (GKE), Standard or Autopilot.

Cloudflare has no managed Kubernetes. A common pattern is to keep Kubernetes on one cloud and put Cloudflare in front for DNS, CDN, WAF and Tunnel.

## 74: How do you create a Kubernetes cluster from the CLI?

**AWS**

```bash
eksctl create cluster --name demo --region us-east-1 --enable-auto-mode
```

**Azure**

```bash
az aks create --resource-group my-rg --name demo --node-count 2 --generate-ssh-keys
az aks get-credentials --resource-group my-rg --name demo
```

**GCP**

```bash
gcloud container clusters create-auto demo --region us-central1
gcloud container clusters get-credentials demo --region us-central1
```

After this, `kubectl` works the same on all three. The differences are in IAM, networking, load balancers and storage classes.

## 75: What is the equivalent of Elastic Beanstalk or App Runner?

- **AWS:** Elastic Beanstalk, and App Runner (closed to new customers in 2026; AWS points to ECS Express Mode instead).
- **Azure:** Azure App Service (Web Apps), which runs code or containers with deployment slots and autoscale.
- **GCP:** Cloud Run (source deploy with `gcloud run deploy --source .`) or App Engine for older apps.
- **Cloudflare:** Workers, deployed with `wrangler deploy`, for apps that fit the Workers runtime.

## 76: What is the equivalent of AWS Amplify Hosting?

- **AWS:** AWS Amplify Hosting for front-end and SSR apps.
- **Azure:** Azure Static Web Apps (static sites with optional Functions APIs) or App Service for full SSR.
- **GCP:** Firebase App Hosting for Next.js and Angular SSR apps, or Firebase Hosting for static sites.
- **Cloudflare:** Workers with static assets, using framework adapters such as OpenNext for Next.js or the Cloudflare Vite plugin.

## 77: What is the equivalent of Amazon Cognito?

- **AWS:** Amazon Cognito user pools (customer sign-up and sign-in) and identity pools (AWS credentials for app users).
- **Azure:** Microsoft Entra External ID (the successor to Azure AD B2C for new customers).
- **GCP:** Identity Platform, which is Firebase Authentication with enterprise features.

Cloudflare has no customer identity service. Cloudflare Access protects internal apps for employees and partners, but for end-user sign-up you use an external provider (Auth0, Clerk, Cognito, Firebase) and verify its JWTs in a Worker.

## 78: What is the equivalent of Amazon SES?

- **AWS:** Amazon SES for sending and receiving email.
- **Azure:** Azure Communication Services Email.
- **Cloudflare:** Email Routing for receiving and forwarding, Email Workers to process incoming mail in code, and Email Service for sending (in beta).

GCP has no first-party email sending service. GCP projects usually use SendGrid, Mailgun or another provider.

## 79: What is the equivalent of AWS KMS?

- **AWS:** AWS Key Management Service (KMS), and CloudHSM for dedicated HSMs.
- **Azure:** Azure Key Vault keys (software or HSM-backed) and Azure Managed HSM.
- **GCP:** Cloud KMS, with Cloud HSM and Cloud External Key Manager.

Cloudflare has no general key management service for your app data. R2 and other storage are encrypted at rest by Cloudflare. For TLS private keys you want to keep on your own servers, Cloudflare offers Keyless SSL.

## 80: What is the equivalent of Amazon Bedrock?

- **AWS:** Amazon Bedrock (Claude, Llama, Mistral, Amazon Nova and others), with Bedrock AgentCore for agents.
- **Azure:** Microsoft Foundry (formerly Azure AI Foundry), whose Foundry Models include Azure OpenAI and many other models.
- **GCP:** Vertex AI (now part of the Gemini Enterprise Agent Platform) with Gemini and partner models such as Claude through Model Garden.
- **Cloudflare:** Workers AI for open models run on Cloudflare GPUs, and AI Gateway to proxy, cache and log calls to any provider.

## 81: What is the equivalent of SageMaker?

- **AWS:** Amazon SageMaker AI (training, notebooks, endpoints, pipelines).
- **Azure:** Azure Machine Learning.
- **GCP:** Vertex AI training, pipelines and prediction endpoints.

Cloudflare does not train models. Workers AI runs inference on a catalog of models, and you can bring LoRA adapters for some of them.

## 82: What are the equivalents of AWS AI services like Rekognition and Textract?

| Task                | AWS         | Azure                          | GCP                  | Cloudflare                    |
| ------------------- | ----------- | ------------------------------ | -------------------- | ----------------------------- |
| Image analysis      | Rekognition | Azure AI Vision                | Cloud Vision API     | Workers AI vision models      |
| Document extraction | Textract    | Azure AI Document Intelligence | Document AI          | n/a                           |
| Speech to text      | Transcribe  | Azure AI Speech                | Speech-to-Text       | Workers AI (Whisper)          |
| Text to speech      | Polly       | Azure AI Speech                | Text-to-Speech       | Workers AI TTS models         |
| Translation         | Translate   | Azure AI Translator            | Cloud Translation    | Workers AI translation models |
| Text analysis       | Comprehend  | Azure AI Language              | Natural Language API | n/a                           |

Many teams now replace these single-purpose APIs with a general LLM call, but the dedicated services are still cheaper and more predictable for high-volume jobs like OCR.

## 83: What is the equivalent of OpenSearch Service?

- **AWS:** Amazon OpenSearch Service (and OpenSearch Serverless).
- **Azure:** Azure AI Search for app search and vector search, or Elastic Cloud on Azure from the Marketplace.
- **GCP:** Vertex AI Search for managed search, or Elastic Cloud on GCP.
- **Cloudflare:** AI Search (formerly AutoRAG), which indexes data from R2 or a website for search and retrieval.

If you rely on raw OpenSearch APIs and plugins, the simplest translation is a managed Elastic or OpenSearch offering on the target cloud.

## 84: What is the equivalent of a vector database on AWS?

- **AWS:** S3 Vectors, OpenSearch vector search, Aurora PostgreSQL with pgvector.
- **Azure:** Azure AI Search vector indexes, Cosmos DB vector search, Azure Database for PostgreSQL with pgvector.
- **GCP:** Vertex AI Vector Search, AlloyDB or Cloud SQL with pgvector, Firestore vector search.
- **Cloudflare:** Vectorize, a vector database used through a Worker binding.

## 85: What is the equivalent of CodePipeline and CodeBuild?

- **AWS:** CodePipeline, CodeBuild and CodeDeploy.
- **Azure:** Azure Pipelines (part of Azure DevOps), or GitHub Actions.
- **GCP:** Cloud Build and Cloud Deploy.
- **Cloudflare:** Workers Builds, which builds and deploys a Worker on every Git push, with preview URLs for branches.

Many teams skip the provider's CI/CD and use GitHub Actions or GitLab CI for all four, with OIDC to log in to each cloud.

## 86: What is the equivalent of CodeCommit?

- **AWS:** AWS CodeCommit, which AWS reopened to new customers after a pause.
- **Azure:** Azure Repos in Azure DevOps.

GCP's Cloud Source Repositories is no longer offered to new customers, and Cloudflare has no Git hosting. Both connect to GitHub or GitLab instead.

## 87: What is the equivalent of Direct Connect?

- **AWS:** AWS Direct Connect.
- **Azure:** Azure ExpressRoute.
- **GCP:** Cloud Interconnect (Dedicated or Partner), and Cross-Cloud Interconnect to link directly to other clouds.
- **Cloudflare:** Cloudflare Network Interconnect (CNI), a private link between your network and Cloudflare.

## 88: What is the equivalent of a site-to-site VPN?

- **AWS:** AWS Site-to-Site VPN with a virtual private gateway or Transit Gateway.
- **Azure:** Azure VPN Gateway.
- **GCP:** Cloud VPN (HA VPN).
- **Cloudflare:** Magic WAN IPsec or GRE tunnels, or Cloudflare Tunnel and WARP connectors for app-level access without a classic VPN.

## 89: What is the equivalent of AWS PrivateLink?

- **AWS:** PrivateLink and interface VPC endpoints.
- **Azure:** Azure Private Link and private endpoints.
- **GCP:** Private Service Connect.
- **Cloudflare:** Cloudflare Tunnel exposes a private service to Cloudflare without a public IP, which serves a similar purpose for traffic coming from Cloudflare.

## 90: What is the equivalent of VPC peering?

- **AWS:** VPC peering (non-transitive).
- **Azure:** VNet peering, within a region or global.
- **GCP:** VPC Network Peering, or Shared VPC to use one network across projects.

Since a GCP VPC is already global, many AWS setups that need peering between regions need nothing extra on GCP.

## 91: What is the equivalent of Transit Gateway?

- **AWS:** AWS Transit Gateway, a hub that connects many VPCs and on-premises networks.
- **Azure:** Azure Virtual WAN, or a hub VNet with peering and Azure Firewall or an NVA.
- **GCP:** Network Connectivity Center, plus Shared VPC for many projects on one network.
- **Cloudflare:** Magic WAN, which connects offices, data centers and cloud networks through Cloudflare's network.

## 92: What is the equivalent of AWS Cost Explorer?

- **AWS:** Cost Explorer and the Cost and Usage Report (CUR 2.0 / Data Exports).
- **Azure:** Microsoft Cost Management (cost analysis, exports).
- **GCP:** Cloud Billing reports, and Cloud Billing export to BigQuery for detailed analysis.
- **Cloudflare:** the Billing section of the dashboard, with usage per product.

All three big clouds now support exports in the FinOps Open Cost and Usage Specification (FOCUS), which makes comparing bills across providers easier.

## 93: How do you set up a budget alert?

**AWS**

```bash
aws budgets create-budget --account-id 123456789012 \
  --budget '{"BudgetName":"monthly","BudgetLimit":{"Amount":"500","Unit":"USD"},"TimeUnit":"MONTHLY","BudgetType":"COST"}' \
  --notifications-with-subscribers '[{"Notification":{"NotificationType":"ACTUAL","ComparisonOperator":"GREATER_THAN","Threshold":80},"Subscribers":[{"SubscriptionType":"EMAIL","Address":"team@example.com"}]}]'
```

**Azure**

```bash
az consumption budget create --budget-name monthly --amount 500 \
  --category cost --time-grain monthly \
  --start-date 2026-12-01 --end-date 2027-12-01
```

**GCP**

```bash
gcloud billing budgets create --billing-account=0X0X0X-0X0X0X-0X0X0X \
  --display-name=monthly --budget-amount=500USD \
  --threshold-rule=percent=0.8
```

Cloudflare has usage-based billing notifications that you set up in the dashboard under Notifications. A budget alert never stops spending by itself on any provider; you need automation for that.

## 94: How do tags compare?

- **AWS:** tags (key-value pairs) on almost every resource, used for cost allocation, ABAC and automation.
- **Azure:** tags on resources, resource groups and subscriptions. Tags are not inherited by default, but Azure Policy can enforce or copy them.
- **GCP:** labels (key-value pairs for billing and filtering) and a separate tags resource (organization-level tags used in IAM conditions and firewall policies).

Cloudflare has no general tagging of resources, so cost and ownership are usually tracked by account, Worker name or naming conventions.

## 95: How do the free tiers compare?

- **AWS:** a free plan with credits for new accounts, plus always-free limits on some services (for example Lambda's monthly free requests and compute).
- **Azure:** a free account with credit for the first 30 days, 12 months of selected free services, and always-free amounts (for example Azure Functions grants).
- **GCP:** a free trial with credit for new customers, plus an always-free tier (for example an `e2-micro` VM in some US regions and Cloud Run free requests).
- **Cloudflare:** a large always-free tier: free CDN, DNS and DDoS protection, 100,000 Worker requests per day, and free tiers for R2, D1 and KV.

Always check the current numbers. Free tier details change often.

## 96: How do pricing models for serverless compute differ?

- **AWS Lambda:** requests plus GB-seconds (memory times wall-clock duration).
- **Azure Functions Flex Consumption:** executions plus GB-seconds, and a lower rate for always-ready instances.
- **Cloud Run functions:** vCPU-seconds and GiB-seconds while handling requests (request-based billing) or for the whole instance lifetime (instance-based billing), plus requests.
- **Cloudflare Workers:** requests plus CPU milliseconds. Time spent waiting on `fetch` or a database does not count.

That last point makes Workers cheap for I/O-heavy APIs that spend most of their time waiting on other services.

## 97: How does the shared responsibility model compare?

All four use the same idea: the provider secures the infrastructure ("security of the cloud") and you secure what you put on it ("security in the cloud"). The split moves with the service type:

- VMs (EC2, Azure VMs, Compute Engine): you patch the OS, configure firewalls and manage access.
- Containers on serverless (Fargate, Container Apps, Cloud Run, Cloudflare Containers): you own the image and its dependencies.
- Functions (Lambda, Azure Functions, Cloud Run functions, Workers): you own the code, its dependencies, secrets and IAM.

In every case, identity, access settings and data classification stay your job.

## 98: How do the well-architected frameworks compare?

- **AWS:** AWS Well-Architected Framework with six pillars (operational excellence, security, reliability, performance efficiency, cost optimization, sustainability) and the Well-Architected Tool.
- **Azure:** Azure Well-Architected Framework with five pillars (reliability, security, cost optimization, operational excellence, performance efficiency) and Azure Advisor recommendations.
- **GCP:** Google Cloud Well-Architected Framework (formerly the Architecture Framework), with pillars for operational excellence, security, reliability, cost optimization, performance and sustainability.

The pillars are almost the same, so an AWS design review translates well into Azure or GCP review language.

## 99: How do you install the JavaScript SDKs?

**AWS**

```bash
npm install @aws-sdk/client-s3 @aws-sdk/client-dynamodb
```

**Azure**

```bash
npm install @azure/identity @azure/storage-blob @azure/cosmos
```

**GCP**

```bash
npm install @google-cloud/storage @google-cloud/firestore
```

**Cloudflare**

```bash
npm install -D wrangler @cloudflare/workers-types
```

AWS SDK v3, Azure and GCP all use one package per service. On Cloudflare, Workers talk to R2, D1 and KV through bindings, so there is no client library to install. You only need Wrangler and types (or the types generated by `wrangler types`).

## 100: How do you read an object from storage in code?

**AWS**

```ts
import { S3Client, GetObjectCommand } from "@aws-sdk/client-s3";

const s3 = new S3Client({});
const res = await s3.send(
  new GetObjectCommand({ Bucket: "my-bucket", Key: "a.txt" }),
);
const text = await res.Body?.transformToString();
```

**Azure**

```ts
import { DefaultAzureCredential } from "@azure/identity";
import { BlobServiceClient } from "@azure/storage-blob";

const service = new BlobServiceClient(
  "https://myaccount.blob.core.windows.net",
  new DefaultAzureCredential(),
);
const blob = service.getContainerClient("files").getBlobClient("a.txt");
const text = (await blob.downloadToBuffer()).toString("utf8");
```

**GCP**

```ts
import { Storage } from "@google-cloud/storage";

const storage = new Storage();
const [buf] = await storage.bucket("my-bucket").file("a.txt").download();
const text = buf.toString("utf8");
```

**Cloudflare**

```ts
export default {
  async fetch(_req: Request, env: { FILES: R2Bucket }): Promise<Response> {
    const obj = await env.FILES.get("a.txt");
    if (!obj) return new Response("Not found", { status: 404 });
    return new Response(await obj.text());
  },
};
```

## 101: How does the default credential chain work in each SDK?

- **AWS:** the SDK checks environment variables, then the shared config and SSO profiles, then container or instance metadata (the IAM role). You write `new S3Client({})`.
- **Azure:** `DefaultAzureCredential` tries environment variables, workload identity, managed identity, then developer logins (Azure CLI, Azure Developer CLI, VS Code).
- **GCP:** Application Default Credentials (ADC) checks `GOOGLE_APPLICATION_CREDENTIALS`, then the gcloud ADC file, then the metadata server (the attached service account).
- **Cloudflare:** no chain is needed inside a Worker, because bindings are injected as `env`. Outside Workers, you pass an API token.

In production, `DefaultAzureCredential` is often replaced with `ManagedIdentityCredential` to avoid slow fallbacks and surprises.

## 102: How do resource identifiers compare?

- **AWS:** ARNs, for example `arn:aws:s3:::my-bucket` or `arn:aws:lambda:us-east-1:123456789012:function:hello`.
- **Azure:** resource IDs, for example `/subscriptions/<sub-id>/resourceGroups/my-rg/providers/Microsoft.Storage/storageAccounts/myaccount`.
- **GCP:** resource names, for example `projects/my-project/locations/us-central1/functions/hello`, and full names like `//storage.googleapis.com/projects/_/buckets/my-bucket` in IAM and Asset Inventory.
- **Cloudflare:** account IDs, zone IDs and resource names or IDs, for example a Worker named `api` in account `abc123`.

## 103: How do service quotas compare?

- **AWS:** Service Quotas console and API, with per-account, per-region limits (for example Lambda concurrent executions).
- **Azure:** quotas per subscription and region (for example vCPUs per VM family), raised in the portal with a support request or the Quotas API.
- **GCP:** Cloud Quotas per project and region, viewed and adjusted in the console or with `gcloud`.
- **Cloudflare:** plan-based limits per account (Workers, D1, R2, Queues), documented per product, with higher limits on request.

A migration often fails on day one because nobody raised quotas on the new account, subscription or project.

## 104: What is the equivalent of AWS Marketplace?

- **AWS:** AWS Marketplace.
- **Azure:** Azure Marketplace (and Microsoft commercial marketplace).
- **GCP:** Google Cloud Marketplace.

Cloudflare has no marketplace for third-party software, but it has integrations and partner apps for some products.

## 105: How do you check provider health status?

- **AWS:** AWS Health Dashboard, with personalized events for your account.
- **Azure:** Azure Status page and Azure Service Health (personalized, with alerts).
- **GCP:** Google Cloud Service Health, with personalized incidents for your projects.
- **Cloudflare:** the Cloudflare Status page and Notifications for incidents.

## 106: What is the equivalent of Trusted Advisor?

- **AWS:** Trusted Advisor and Compute Optimizer.
- **Azure:** Azure Advisor.
- **GCP:** Recommender (Active Assist), for example idle VM and rightsizing recommendations.

Cloudflare has no general advisor, but the dashboard shows security and performance suggestions per zone (Security Center, Speed recommendations).

## 107: What is the equivalent of AWS Config?

- **AWS:** AWS Config (resource inventory, configuration history, compliance rules).
- **Azure:** Azure Resource Graph for inventory, Azure Policy for compliance, and change analysis for history.
- **GCP:** Cloud Asset Inventory for inventory and history, plus Organization Policy and Security Command Center for compliance.

## 108: What is the equivalent of GuardDuty?

- **AWS:** Amazon GuardDuty.
- **Azure:** Microsoft Defender for Cloud (threat protection plans), with Microsoft Sentinel as the SIEM.
- **GCP:** Security Command Center threat detection (Event Threat Detection, Container Threat Detection), with Google Security Operations as the SIEM.
- **Cloudflare:** Security Center and security analytics for the traffic that goes through Cloudflare.

## 109: What is the equivalent of Amazon Inspector?

- **AWS:** Amazon Inspector (VM, container image and Lambda vulnerability scanning).
- **Azure:** Defender for Cloud vulnerability assessment (servers and container registries).
- **GCP:** Artifact Analysis (container scanning) and VM Manager vulnerability reports.

## 110: What is the equivalent of Security Hub?

- **AWS:** AWS Security Hub, which collects findings and checks against standards.
- **Azure:** Microsoft Defender for Cloud (secure score, regulatory compliance dashboard).
- **GCP:** Security Command Center.
- **Cloudflare:** Security Center, which scans your Cloudflare setup for insecure settings.

## 111: What is the equivalent of Service Control Policies?

- **AWS:** SCPs and resource control policies (RCPs) in AWS Organizations, which set the maximum permissions for accounts.
- **Azure:** Azure Policy assignments (with `deny` effects) at management group or subscription scope.
- **GCP:** Organization Policy constraints (for example "restrict resource locations") and IAM deny policies.

SCPs limit IAM actions. Azure Policy and GCP organization policies mostly limit resource configurations, such as which regions or SKUs are allowed. To block actions in GCP, use IAM deny policies.

## 112: What is the equivalent of AWS Control Tower?

- **AWS:** AWS Control Tower for setting up a multi-account landing zone.
- **Azure:** Azure landing zones (the Cloud Adoption Framework reference implementations).
- **GCP:** the Google Cloud setup checklist and the enterprise foundations blueprint (Terraform).

## 113: What is the equivalent of EFS?

- **AWS:** Amazon EFS (NFS).
- **Azure:** Azure Files (SMB and NFS), or Azure NetApp Files for high performance.
- **GCP:** Filestore (NFS), or Google Cloud NetApp Volumes.

Cloudflare has no shared file system. R2 is object storage, and Workers have no persistent disk.

## 114: What is the equivalent of FSx?

- **AWS:** FSx for Windows File Server, NetApp ONTAP, Lustre and OpenZFS.
- **Azure:** Azure Files, Azure NetApp Files and Azure Managed Lustre.
- **GCP:** Google Cloud NetApp Volumes, Managed Lustre and Filestore.

## 115: What is the equivalent of AWS Backup?

- **AWS:** AWS Backup.
- **Azure:** Azure Backup with Recovery Services vaults and Backup vaults.
- **GCP:** Backup and DR Service.

Cloudflare has no backup service. D1 has Time Travel for point-in-time restore within a retention window, and for R2 you copy important data to another bucket or cloud yourself.

## 116: How do disk snapshots compare?

**AWS**

```bash
aws ec2 create-snapshot --volume-id vol-0123456789abcdef0 --description nightly
```

**Azure**

```bash
az snapshot create --resource-group my-rg --name data-snap \
  --source /subscriptions/<sub-id>/resourceGroups/my-rg/providers/Microsoft.Compute/disks/data-disk
```

**GCP**

```bash
gcloud compute snapshots create data-snap --source-disk data-disk \
  --source-disk-zone us-central1-a
```

All three snapshots are incremental, and on all three you can schedule them (Data Lifecycle Manager or AWS Backup, Azure Backup, GCP snapshot schedules).

## 117: How do you move large amounts of data into each cloud?

| Need                   | AWS           | Azure                       | GCP                      | Cloudflare    |
| ---------------------- | ------------- | --------------------------- | ------------------------ | ------------- |
| Online transfer        | DataSync      | AzCopy, Azure Storage Mover | Storage Transfer Service | Super Slurper |
| Incremental, on demand | n/a           | n/a                         | n/a                      | Sippy         |
| Offline device         | Snowball Edge | Azure Data Box              | Transfer Appliance       | n/a           |

Super Slurper copies a whole bucket from S3, GCS or Azure into R2. Sippy copies objects lazily: when R2 misses an object, it fetches it from the old bucket and stores it, so egress happens only once per object.

## 118: What is the equivalent of AWS Glue?

- **AWS:** AWS Glue (ETL jobs, crawlers, Data Catalog).
- **Azure:** Azure Data Factory or Data Factory in Microsoft Fabric, with Microsoft Purview for cataloging.
- **GCP:** Dataflow (Apache Beam), Cloud Data Fusion, Dataproc, and Dataplex Universal Catalog.
- **Cloudflare:** R2 Data Catalog, a managed Apache Iceberg catalog on R2, for the catalog part only.

## 119: What is the equivalent of EMR?

- **AWS:** Amazon EMR (Spark, Hive, Presto).
- **Azure:** Azure Databricks, or Spark in Microsoft Fabric. HDInsight is the older option.
- **GCP:** Dataproc and Google Cloud Serverless for Apache Spark.

## 120: What is the equivalent of QuickSight?

- **AWS:** Amazon Quick Sight (QuickSight), now part of Amazon Quick Suite.
- **Azure:** Power BI.
- **GCP:** Looker and Looker Studio.

## 121: What is the equivalent of Amazon MSK?

- **AWS:** Amazon Managed Streaming for Apache Kafka (MSK).
- **Azure:** Event Hubs with its Kafka endpoint, or Confluent Cloud on Azure.
- **GCP:** Google Cloud Managed Service for Apache Kafka.

Event Hubs speaks the Kafka protocol but is not a full Kafka cluster. Features like Kafka Streams state stores or some admin APIs may behave differently.

## 122: What is the equivalent of Amazon MQ?

- **AWS:** Amazon MQ (ActiveMQ and RabbitMQ).
- **Azure:** Azure Service Bus, which supports AMQP 1.0 and JMS 2.0 on the Premium tier.

GCP and Cloudflare have no managed ActiveMQ or RabbitMQ. On GCP, teams use Pub/Sub or run RabbitMQ on GKE or from the Marketplace.

## 123: What is the equivalent of AppSync?

- **AWS:** AWS AppSync (managed GraphQL and real-time APIs).
- **Azure:** Azure API Management GraphQL APIs (pass-through or synthetic GraphQL with resolvers).
- **GCP:** Firebase Data Connect, which generates a GraphQL API over Cloud SQL for PostgreSQL.

On Cloudflare, you run a GraphQL server (for example GraphQL Yoga) inside a Worker.

## 124: What is the equivalent of AWS IoT Core?

- **AWS:** AWS IoT Core.
- **Azure:** Azure IoT Hub, and Event Grid MQTT broker.

Google retired Cloud IoT Core in 2023, so on GCP you use a partner MQTT platform or run a broker yourself and send data to Pub/Sub. Cloudflare has no IoT service.

## 125: What is the equivalent of AWS Outposts?

- **AWS:** AWS Outposts (AWS racks or servers in your data center).
- **Azure:** Azure Local (formerly Azure Stack HCI), managed through Azure Arc.
- **GCP:** Google Distributed Cloud (connected and air-gapped).

## 126: What is the equivalent of AWS Local Zones and Wavelength?

- **AWS:** Local Zones (small regions near big cities) and Wavelength (inside 5G networks).
- **Azure:** Azure Extended Zones and Azure Operator Nexus.
- **Cloudflare:** every Cloudflare location acts like an edge zone. Workers run in hundreds of cities by default, so there is nothing to enable.

## 127: What is the equivalent of AWS Global Accelerator?

- **AWS:** AWS Global Accelerator (anycast IPs routed over the AWS backbone to regional endpoints).
- **Azure:** Azure Front Door for HTTP, and the cross-region (global) Load Balancer for layer 4.
- **GCP:** the global external Application Load Balancer and proxy Network Load Balancer with Premium Tier networking, which use one anycast IP.
- **Cloudflare:** all proxied traffic already enters on anycast IPs, and Argo Smart Routing picks the fastest path across Cloudflare's network.

## 128: How do you set up DNS failover?

- **AWS:** Route 53 health checks with a failover routing policy.
- **Azure:** Traffic Manager with priority routing, or Front Door origin groups with health probes.
- **GCP:** Cloud DNS failover routing policies with health checks (for internal load balancers) or a global load balancer with backend health.
- **Cloudflare:** Load Balancing with health monitors and a fallback pool.

## 129: What is the equivalent of Lambda function URLs?

- **AWS:** Lambda function URLs, a built-in HTTPS endpoint for a function.
- **Azure:** every HTTP-triggered function has an HTTPS URL on `<app>.azurewebsites.net` (with function keys or Entra auth).
- **GCP:** every Cloud Run function has an HTTPS URL, public with `--allow-unauthenticated` or protected by IAM.
- **Cloudflare:** every Worker can get a `*.workers.dev` URL, or you attach routes or a custom domain.

## 130: What is the equivalent of Lambda@Edge and CloudFront Functions?

- **AWS:** CloudFront Functions (lightweight JavaScript at edge locations) and Lambda@Edge (full Lambda at regional edge caches).
- **Azure:** Front Door Rules Engine for header and URL rewrites, with no custom code at the edge.
- **GCP:** Service Extensions plugins on load balancers and Media CDN (WebAssembly).
- **Cloudflare:** Workers, which are full edge compute by design, plus Transform Rules and Snippets for small changes.

## 131: How do you add a custom domain to a serverless app?

**AWS**

```bash
aws apigatewayv2 create-domain-name --domain-name api.example.com \
  --domain-name-configurations CertificateArn=arn:aws:acm:us-east-1:123456789012:certificate/abc
```

**Azure**

```bash
az functionapp config hostname add --webapp-name my-func-app \
  --resource-group my-rg --hostname api.example.com
```

**GCP**

```bash
gcloud beta run domain-mappings create --service hello \
  --domain api.example.com --region us-central1
```

**Cloudflare**

```jsonc
// wrangler.jsonc
{ "routes": [{ "pattern": "api.example.com", "custom_domain": true }] }
```

Cloud Run domain mappings are limited to some regions, so the production setup is usually a global load balancer with a serverless network endpoint group. On Cloudflare, the custom domain creates the DNS record and certificate for you.

## 132: What is the equivalent of CloudWatch Synthetics?

- **AWS:** CloudWatch Synthetics canaries and Route 53 health checks.
- **Azure:** Application Insights availability tests (standard tests).
- **GCP:** Cloud Monitoring uptime checks and synthetic monitors.
- **Cloudflare:** Health Checks (and Load Balancing monitors) that probe your origins from Cloudflare locations.

## 133: What is the equivalent of CloudWatch RUM?

- **AWS:** CloudWatch RUM.
- **Azure:** the Application Insights JavaScript SDK for browser telemetry.
- **Cloudflare:** Web Analytics, a free privacy-friendly analytics script with Core Web Vitals, or automatic setup on proxied sites.

GCP has no first-party browser RUM. Firebase Performance Monitoring covers web and mobile apps built with Firebase.

## 134: What is the equivalent of SNS mobile push?

- **AWS:** Amazon SNS mobile push and AWS End User Messaging.
- **Azure:** Azure Notification Hubs.
- **GCP:** Firebase Cloud Messaging (FCM).

## 135: What is the equivalent of Amazon Location Service?

- **AWS:** Amazon Location Service.
- **Azure:** Azure Maps.
- **GCP:** Google Maps Platform.

## 136: What is the equivalent of AWS media services for video?

- **AWS:** AWS Elemental MediaConvert (transcoding), Amazon IVS (live streaming) and CloudFront for delivery.
- **GCP:** Transcoder API, Live Stream API and Media CDN.
- **Cloudflare:** Cloudflare Stream, which stores, encodes and delivers video, live and on demand, through one API.

Azure Media Services was retired in 2024, so on Azure you use a partner solution or build with Azure Container Apps and Front Door.

## 137: What is the equivalent of API Gateway WebSocket APIs?

- **AWS:** API Gateway WebSocket APIs, with Lambda handling connect, message and disconnect.
- **Azure:** Azure Web PubSub, or SignalR Service.
- **GCP:** Cloud Run, which supports WebSockets directly on a service.
- **Cloudflare:** Durable Objects with the WebSocket Hibernation API, where one object holds the connections for a room or user.

## 138: What is the equivalent of Amazon Chime SDK for real-time audio and video?

- **AWS:** Amazon Chime SDK and Amazon IVS real-time streaming.
- **Azure:** Azure Communication Services (calling, chat, SMS).
- **Cloudflare:** Cloudflare Realtime (formerly Calls), a WebRTC SFU and TURN service on Cloudflare's network.

## 139: What is the equivalent of a CAPTCHA or bot protection service?

- **AWS:** AWS WAF CAPTCHA and challenge actions, and AWS WAF Bot Control.
- **GCP:** reCAPTCHA (in Google Cloud), integrated with Cloud Armor.
- **Cloudflare:** Turnstile, a free CAPTCHA alternative that usually needs no puzzle, plus Bot Management for traffic.

Azure has no first-party CAPTCHA. Azure WAF has bot protection rules, and apps usually add reCAPTCHA or Turnstile.

## 140: What is the equivalent of AWS Fault Injection Service?

- **AWS:** AWS Fault Injection Service (FIS).
- **Azure:** Azure Chaos Studio.

GCP has no first-party chaos service. Teams use open-source tools like Chaos Mesh on GKE.

## 141: What is the equivalent of a load testing service?

- **AWS:** Distributed Load Testing on AWS (a solution you deploy).
- **Azure:** Azure Load Testing (managed, runs JMeter and Locust scripts).

GCP and Cloudflare have no managed load testing service. Use k6, Locust or JMeter yourself, and on Cloudflare ask before load testing a production zone so it is not treated as an attack.

## 142: What are the pricing calculators?

- **AWS:** AWS Pricing Calculator.
- **Azure:** Azure pricing calculator and the TCO calculator.
- **GCP:** Google Cloud Pricing Calculator.
- **Cloudflare:** published per-product pricing pages (Workers, R2, D1 and so on). There is no full calculator, but most products have simple usage-based prices.

## 143: What is the equivalent of AWS Systems Manager Patch Manager?

- **AWS:** Systems Manager Patch Manager.
- **Azure:** Azure Update Manager.
- **GCP:** VM Manager OS patch management.

## 144: What is the equivalent of AWS Systems Manager Run Command?

- **AWS:** Systems Manager Run Command.
- **Azure:** Run Command on VMs (`az vm run-command invoke`).
- **GCP:** no exact match. You use OS Config policies, startup scripts or `gcloud compute ssh --command`.

**Azure**

```bash
az vm run-command invoke --resource-group my-rg --name my-vm \
  --command-id RunShellScript --scripts "systemctl restart nginx"
```

## 145: What is the equivalent of Amazon WorkSpaces?

- **AWS:** Amazon WorkSpaces.
- **Azure:** Azure Virtual Desktop and Windows 365.

GCP has no first-party virtual desktop service. Cloudflare offers Browser Isolation, which runs a remote browser for users but not a full desktop.

## 146: What is the equivalent of AWS Batch?

- **AWS:** AWS Batch.
- **Azure:** Azure Batch, or Container Apps jobs for container workloads.
- **GCP:** Batch, or Cloud Run jobs for container tasks.

Cloudflare has no batch compute service. Long jobs can run as Workflows (many small steps) or in Containers.

## 147: What is the equivalent of Amazon Lightsail?

- **AWS:** Amazon Lightsail (simple VPS with fixed monthly price).
- **Azure:** no direct match. The closest is App Service on a basic plan or a B-series VM.
- **GCP:** no direct match. The closest is an `e2` VM or Cloud Run.

Cloudflare has no VPS, but for simple websites Workers with static assets often replace a small Lightsail server.

## 148: What is the equivalent of AWS Elastic Disaster Recovery?

- **AWS:** AWS Elastic Disaster Recovery.
- **Azure:** Azure Site Recovery.
- **GCP:** Backup and DR Service, plus Migrate to Virtual Machines for replication into Compute Engine.

## 149: What are the equivalent migration discovery tools?

- **AWS:** AWS Application Discovery Service and AWS Transform for assessments and code changes.
- **Azure:** Azure Migrate (discovery, assessment, migration).
- **GCP:** Migration Center (discovery, TCO reports) and Migrate to Virtual Machines.

When you move from AWS to Azure or GCP, the target cloud's tool is usually the one that can read your AWS environment. Azure Migrate and Migration Center can both discover AWS resources.

## 150: Can you give a quick cheat sheet of the most common translations?

| AWS             | Azure                                  | GCP                        | Cloudflare                  |
| --------------- | -------------------------------------- | -------------------------- | --------------------------- |
| EC2             | Virtual Machines                       | Compute Engine             | n/a                         |
| Lambda          | Azure Functions                        | Cloud Run functions        | Workers                     |
| ECS / Fargate   | Container Apps                         | Cloud Run                  | Containers                  |
| EKS             | AKS                                    | GKE                        | n/a                         |
| S3              | Blob Storage                           | Cloud Storage              | R2                          |
| DynamoDB        | Cosmos DB                              | Firestore / Bigtable       | D1 / KV / Durable Objects   |
| RDS / Aurora    | Azure SQL / PostgreSQL flexible server | Cloud SQL / AlloyDB        | Hyperdrive (to external DB) |
| ElastiCache     | Azure Managed Redis                    | Memorystore                | n/a                         |
| SQS             | Service Bus / Queue Storage            | Pub/Sub / Cloud Tasks      | Queues                      |
| SNS             | Service Bus topics / Event Grid        | Pub/Sub                    | n/a                         |
| EventBridge     | Event Grid                             | Eventarc                   | n/a                         |
| Step Functions  | Durable Functions / Logic Apps         | Workflows                  | Workflows                   |
| VPC             | Virtual Network                        | VPC network                | n/a                         |
| Route 53        | Azure DNS                              | Cloud DNS                  | DNS                         |
| CloudFront      | Front Door                             | Cloud CDN                  | CDN                         |
| WAF / Shield    | WAF / DDoS Protection                  | Cloud Armor                | WAF / DDoS                  |
| IAM             | Entra ID + RBAC                        | Cloud IAM                  | API tokens / Access         |
| Secrets Manager | Key Vault                              | Secret Manager             | Secrets / Secrets Store     |
| CloudWatch      | Azure Monitor                          | Cloud Logging / Monitoring | Workers Observability       |
| CloudFormation  | ARM / Bicep                            | Infrastructure Manager     | Wrangler / Terraform        |
| Bedrock         | Microsoft Foundry                      | Vertex AI                  | Workers AI                  |

# Moderate Questions (151-300)

## 151: How do you translate an IAM policy that grants read and write access to one bucket?

**AWS**

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": ["s3:GetObject", "s3:PutObject"],
      "Resource": "arn:aws:s3:::my-bucket/*"
    }
  ]
}
```

**Azure**

```bash
az role assignment create \
  --assignee <principal-id> \
  --role "Storage Blob Data Contributor" \
  --scope /subscriptions/<sub-id>/resourceGroups/my-rg/providers/Microsoft.Storage/storageAccounts/myaccount/blobServices/default/containers/files
```

**GCP**

```bash
gcloud storage buckets add-iam-policy-binding gs://my-bucket \
  --member=serviceAccount:api@my-project.iam.gserviceaccount.com \
  --role=roles/storage.objectUser
```

**Cloudflare**

```jsonc
// wrangler.jsonc: the Worker gets full access to this one bucket
{ "r2_buckets": [{ "binding": "FILES", "bucket_name": "my-bucket" }] }
```

On Azure and GCP you usually pick a built-in role and narrow it by scope, instead of listing actions. Azure data access (reading blobs) needs a data-plane role like "Storage Blob Data Contributor". Being "Owner" of the storage account is not enough.

## 152: How do you create a custom role?

**AWS**

```bash
aws iam create-policy --policy-name ReportsReader --policy-document file://policy.json
```

**Azure**

```json
{
  "Name": "Reports Reader",
  "Actions": [],
  "DataActions": [
    "Microsoft.Storage/storageAccounts/blobServices/containers/blobs/read"
  ],
  "AssignableScopes": ["/subscriptions/<sub-id>"]
}
```

```bash
az role definition create --role-definition @reports-reader.json
```

**GCP**

```bash
gcloud iam roles create reportsReader --project=my-project \
  --title="Reports Reader" \
  --permissions=storage.objects.get,storage.objects.list
```

In AWS, a policy is attached directly. In Azure and GCP, the custom role is only a list of permissions and still needs a role assignment or binding at some scope.

## 153: How do you translate sts:AssumeRole?

- **AWS:** a role with a trust policy, assumed with `sts:AssumeRole` to get temporary credentials, often across accounts.
- **Azure:** no role switching. You grant the same identity roles in another subscription, use Azure Lighthouse for cross-tenant management, or use a multi-tenant app registration.
- **GCP:** service account impersonation. The caller needs `roles/iam.serviceAccountTokenCreator` on the target service account.

**AWS**

```bash
aws sts assume-role --role-arn arn:aws:iam::222222222222:role/deployer --role-session-name ci
```

**GCP**

```bash
gcloud storage ls gs://prod-bucket \
  --impersonate-service-account=deployer@prod-project.iam.gserviceaccount.com
```

```ts
import { GoogleAuth, Impersonated } from "google-auth-library";

const source = await new GoogleAuth().getClient();
const client = new Impersonated({
  sourceClient: source,
  targetPrincipal: "deployer@prod-project.iam.gserviceaccount.com",
  targetScopes: ["https://www.googleapis.com/auth/cloud-platform"],
  lifetime: 3600,
});
```

## 154: How do you deploy from GitHub Actions without long-lived keys?

**AWS**

```yaml
permissions: { id-token: write, contents: read }
steps:
  - uses: aws-actions/configure-aws-credentials@v4
    with:
      role-to-assume: arn:aws:iam::123456789012:role/github-deploy
      aws-region: us-east-1
```

**Azure**

```yaml
permissions: { id-token: write, contents: read }
steps:
  - uses: azure/login@v2
    with:
      client-id: ${{ vars.AZURE_CLIENT_ID }}
      tenant-id: ${{ vars.AZURE_TENANT_ID }}
      subscription-id: ${{ vars.AZURE_SUBSCRIPTION_ID }}
```

**GCP**

```yaml
permissions: { id-token: write, contents: read }
steps:
  - uses: google-github-actions/auth@v2
    with:
      workload_identity_provider: projects/123456/locations/global/workloadIdentityPools/github/providers/my-repo
      service_account: deploy@my-project.iam.gserviceaccount.com
```

**Cloudflare**

```yaml
steps:
  - uses: cloudflare/wrangler-action@v3
    with:
      apiToken: ${{ secrets.CLOUDFLARE_API_TOKEN }}
      accountId: ${{ vars.CLOUDFLARE_ACCOUNT_ID }}
```

AWS, Azure (federated credentials on an app registration or user-assigned managed identity) and GCP (Workload Identity Federation) all trust GitHub's OIDC token. Cloudflare does not accept OIDC for deploys, so you use a narrowly scoped API token stored as a secret.

## 155: How do you give a function its own identity?

**AWS**

```bash
aws lambda update-function-configuration --function-name api \
  --role arn:aws:iam::123456789012:role/api-lambda-role
```

**Azure**

```bash
az functionapp identity assign --name my-func-app --resource-group my-rg
# then grant roles to the returned principalId
```

**GCP**

```bash
gcloud functions deploy api --gen2 --region us-central1 \
  --service-account api@my-project.iam.gserviceaccount.com
```

**Cloudflare**

```jsonc
// wrangler.jsonc: access is granted by declaring bindings
{
  "d1_databases": [
    { "binding": "DB", "database_name": "app", "database_id": "<id>" },
  ],
  "kv_namespaces": [{ "binding": "CACHE", "id": "<id>" }],
}
```

Avoid the default service accounts on GCP (the Compute Engine default account often has the broad Editor role). Create one service account per function with only the roles it needs.

## 156: How do you build a small REST API with routes?

**AWS**

```ts
import type { APIGatewayProxyHandlerV2 } from "aws-lambda";

// API Gateway HTTP API routes: "GET /users/{id}" -> this function
export const handler: APIGatewayProxyHandlerV2 = async (event) => {
  const id = event.pathParameters?.id;
  return { statusCode: 200, body: JSON.stringify({ id }) };
};
```

**Azure**

```ts
import { app } from "@azure/functions";

app.http("getUser", {
  methods: ["GET"],
  route: "users/{id}",
  authLevel: "anonymous",
  handler: async (request) => ({ jsonBody: { id: request.params.id } }),
});
```

**GCP**

```ts
import * as functions from "@google-cloud/functions-framework";
import express from "express";

const app = express();
app.get("/users/:id", (req, res) => res.json({ id: req.params.id }));

functions.http("api", app);
```

**Cloudflare**

```ts
import { Hono } from "hono";

const app = new Hono();
app.get("/users/:id", (c) => c.json({ id: c.req.param("id") }));

export default app;
```

Hono runs on all four platforms, so it is a popular choice when a team wants one routing layer that moves between clouds.

## 157: How do you read a JSON body and return JSON?

**AWS**

```ts
export const handler: APIGatewayProxyHandlerV2 = async (event) => {
  const raw = event.isBase64Encoded
    ? Buffer.from(event.body ?? "", "base64").toString()
    : (event.body ?? "{}");
  const input = JSON.parse(raw);
  return {
    statusCode: 201,
    headers: { "content-type": "application/json" },
    body: JSON.stringify({ received: input }),
  };
};
```

**Azure**

```ts
app.http("create", {
  methods: ["POST"],
  handler: async (request) => {
    const input = await request.json();
    return { status: 201, jsonBody: { received: input } };
  },
});
```

**GCP**

```ts
functions.http("create", (req, res) => {
  // JSON bodies are parsed automatically when content-type is application/json
  res.status(201).json({ received: req.body });
});
```

**Cloudflare**

```ts
export default {
  async fetch(request: Request): Promise<Response> {
    const input = await request.json();
    return Response.json({ received: input }, { status: 201 });
  },
};
```

## 158: How do you run code when a file is uploaded to storage?

**AWS**

```ts
import type { S3Handler } from "aws-lambda";

export const handler: S3Handler = async (event) => {
  for (const record of event.Records) {
    console.log(
      record.s3.bucket.name,
      decodeURIComponent(record.s3.object.key),
    );
  }
};
```

**Azure**

```ts
import { app, InvocationContext } from "@azure/functions";

app.storageBlob("onUpload", {
  path: "uploads/{name}",
  connection: "AzureWebJobsStorage",
  source: "EventGrid",
  handler: async (blob: unknown, context: InvocationContext) => {
    context.log("New blob:", context.triggerMetadata?.name);
  },
});
```

**GCP**

```ts
import * as functions from "@google-cloud/functions-framework";

functions.cloudEvent<{ bucket: string; name: string }>("onUpload", (event) => {
  console.log(event.data?.bucket, event.data?.name);
});
```

```bash
gcloud functions deploy onUpload --gen2 --runtime nodejs22 --region us-central1 \
  --source . --entry-point onUpload --trigger-bucket my-bucket
```

**Cloudflare**

```bash
npx wrangler r2 bucket notification create uploads \
  --event-type object-create --queue upload-events
```

```ts
export default {
  async queue(
    batch: MessageBatch<{ action: string; object: { key: string } }>,
  ) {
    for (const msg of batch.messages) {
      console.log(msg.body.action, msg.body.object.key);
      msg.ack();
    }
  },
};
```

On Azure, the Event Grid source is the recommended option for blob triggers because polling is slow on Flex Consumption. On Cloudflare, R2 sends events to a Queue, and a Worker consumes the Queue.

## 159: How do you consume messages from a queue?

**AWS**

```ts
import type { SQSHandler } from "aws-lambda";

export const handler: SQSHandler = async (event) => {
  const batchItemFailures: { itemIdentifier: string }[] = [];
  for (const record of event.Records) {
    try {
      await processOrder(JSON.parse(record.body));
    } catch {
      batchItemFailures.push({ itemIdentifier: record.messageId });
    }
  }
  return { batchItemFailures };
};
```

**Azure**

```ts
app.serviceBusQueue("orders", {
  connection: "ServiceBusConnection",
  queueName: "orders",
  handler: async (message: unknown, context) => {
    await processOrder(message);
  },
});
```

**GCP**

```ts
functions.cloudEvent<{ message: { data: string } }>("orders", async (event) => {
  const order = JSON.parse(
    Buffer.from(event.data!.message.data, "base64").toString(),
  );
  await processOrder(order);
});
```

**Cloudflare**

```ts
export default {
  async queue(batch: MessageBatch<Order>, env: Env) {
    for (const msg of batch.messages) {
      try {
        await processOrder(msg.body);
        msg.ack();
      } catch {
        msg.retry({ delaySeconds: 30 });
      }
    }
  },
};
```

Lambda partial batch responses need `ReportBatchItemFailures` turned on in the event source mapping. On Azure, throwing an error abandons the message so it is retried. On GCP, throwing makes Pub/Sub redeliver. On Cloudflare, you ack or retry each message.

## 160: How do you send a message to a queue or topic?

**AWS**

```ts
import { SQSClient, SendMessageCommand } from "@aws-sdk/client-sqs";

await new SQSClient({}).send(
  new SendMessageCommand({
    QueueUrl: process.env.QUEUE_URL,
    MessageBody: JSON.stringify(order),
  }),
);
```

**Azure**

```ts
import { ServiceBusClient } from "@azure/service-bus";
import { DefaultAzureCredential } from "@azure/identity";

const client = new ServiceBusClient(
  "my-ns.servicebus.windows.net",
  new DefaultAzureCredential(),
);
const sender = client.createSender("orders");
await sender.sendMessages({ body: order });
await sender.close();
```

**GCP**

```ts
import { PubSub } from "@google-cloud/pubsub";

await new PubSub().topic("orders").publishMessage({ json: order });
```

**Cloudflare**

```ts
await env.ORDERS.send(order); // producer binding from wrangler.jsonc
```

## 161: How do you configure a dead-letter queue?

**AWS**

```bash
aws sqs set-queue-attributes --queue-url $QUEUE_URL --attributes \
  '{"RedrivePolicy":"{\"deadLetterTargetArn\":\"arn:aws:sqs:us-east-1:123456789012:orders-dlq\",\"maxReceiveCount\":\"5\"}"}'
```

**Azure**

```bash
az servicebus queue create --resource-group my-rg --namespace-name my-ns \
  --name orders --max-delivery-count 5
# dead letters go to the built-in subqueue orders/$DeadLetterQueue
```

**GCP**

```bash
gcloud pubsub subscriptions update orders-sub \
  --dead-letter-topic=orders-dlq --max-delivery-attempts=5
```

**Cloudflare**

```jsonc
{
  "queues": {
    "consumers": [
      {
        "queue": "orders",
        "max_retries": 5,
        "dead_letter_queue": "orders-dlq",
      },
    ],
  },
}
```

Every Service Bus queue already has a dead-letter subqueue, so there is nothing extra to create. On GCP, the Pub/Sub service agent needs publisher rights on the dead-letter topic and subscriber rights on the source subscription.

## 162: How do visibility timeout, lock duration and ack deadline compare?

| Concept                        | AWS SQS                         | Azure Service Bus                      | GCP Pub/Sub                              | Cloudflare Queues                          |
| ------------------------------ | ------------------------------- | -------------------------------------- | ---------------------------------------- | ------------------------------------------ |
| Time a consumer owns a message | Visibility timeout (up to 12 h) | Lock duration (up to 5 min, renewable) | Ack deadline (10 s to 600 s, extendable) | Until the consumer invocation ends         |
| Retry delay                    | Visibility timeout              | Abandon or schedule                    | Retry policy (exponential backoff)       | `retry({ delaySeconds })` or `retry_delay` |
| Max message size               | 1 MiB                           | 256 KB Standard, up to 100 MB Premium  | 10 MB                                    | 128 KB                                     |

When the processing time can exceed the lock, all four will deliver the message again. Make consumers idempotent and extend the lock or deadline for long work.

## 163: How do you translate SQS FIFO queues?

- **AWS:** FIFO queue with `MessageGroupId` for ordering and `MessageDeduplicationId` (or content-based deduplication) for a 5-minute dedup window.
- **Azure:** Service Bus sessions (`sessionId`) for ordered processing per key, and duplicate detection on the queue.
- **GCP:** Pub/Sub ordering keys with message ordering enabled on the subscription, and exactly-once delivery as a separate option.

**GCP**

```ts
const topic = new PubSub().topic("orders", { messageOrdering: true });
await topic.publishMessage({ json: order, orderingKey: order.customerId });
```

Cloudflare Queues do not guarantee ordering, so you leave it out or put ordered work behind a Durable Object per key.

## 164: How do you translate an SNS topic that fans out to several SQS queues?

- **AWS:** one SNS topic with several SQS subscriptions, optionally with filter policies.
- **Azure:** one Service Bus topic with several subscriptions, each with SQL or correlation filters.
- **GCP:** one Pub/Sub topic with several subscriptions, each with an optional filter expression.
- **Cloudflare:** no topic. The producer Worker sends to each Queue itself.

**GCP**

```bash
gcloud pubsub topics create orders
gcloud pubsub subscriptions create billing-sub --topic=orders
gcloud pubsub subscriptions create shipping-sub --topic=orders \
  --message-filter='attributes.country = "US"'
```

**Cloudflare**

```ts
await Promise.all([env.BILLING.send(order), env.SHIPPING.send(order)]);
```

On GCP and Azure, the topic and its queue-like subscriptions are one service, so you do not need the SNS-plus-SQS pair.

## 165: How do you write and read a record in the main NoSQL database?

**AWS**

```ts
import { DynamoDBClient } from "@aws-sdk/client-dynamodb";
import {
  DynamoDBDocumentClient,
  PutCommand,
  GetCommand,
} from "@aws-sdk/lib-dynamodb";

const db = DynamoDBDocumentClient.from(new DynamoDBClient({}));
await db.send(
  new PutCommand({ TableName: "users", Item: { id: "u1", name: "Ana" } }),
);
const { Item } = await db.send(
  new GetCommand({ TableName: "users", Key: { id: "u1" } }),
);
```

**Azure**

```ts
import { CosmosClient } from "@azure/cosmos";
import { DefaultAzureCredential } from "@azure/identity";

const users = new CosmosClient({
  endpoint: "https://my-account.documents.azure.com",
  aadCredentials: new DefaultAzureCredential(),
})
  .database("app")
  .container("users"); // partition key: /id

await users.items.upsert({ id: "u1", name: "Ana" });
const { resource } = await users.item("u1", "u1").read();
```

**GCP**

```ts
import { Firestore } from "@google-cloud/firestore";

const db = new Firestore();
await db.collection("users").doc("u1").set({ name: "Ana" });
const snap = await db.collection("users").doc("u1").get();
const user = snap.data();
```

**Cloudflare**

```ts
await env.DB.prepare("INSERT OR REPLACE INTO users (id, name) VALUES (?, ?)")
  .bind("u1", "Ana")
  .run();
const user = await env.DB.prepare("SELECT * FROM users WHERE id = ?")
  .bind("u1")
  .first();
```

Cosmos DB reads by id need the partition key value too. Cloudflare D1 is SQL, so you define a table with a migration first.

## 166: How do you translate a DynamoDB query on partition key and sort key?

**AWS**

```ts
import { QueryCommand } from "@aws-sdk/lib-dynamodb";

const { Items } = await db.send(
  new QueryCommand({
    TableName: "orders",
    KeyConditionExpression: "customerId = :c AND createdAt > :d",
    ExpressionAttributeValues: { ":c": "c1", ":d": "2026-01-01" },
    ScanIndexForward: false,
    Limit: 20,
  }),
);
```

**Azure**

```ts
const { resources } = await orders.items
  .query(
    {
      query:
        "SELECT TOP 20 * FROM o WHERE o.customerId = @c AND o.createdAt > @d ORDER BY o.createdAt DESC",
      parameters: [
        { name: "@c", value: "c1" },
        { name: "@d", value: "2026-01-01" },
      ],
    },
    { partitionKey: "c1" },
  )
  .fetchAll();
```

**GCP**

```ts
const snap = await db
  .collection("orders")
  .where("customerId", "==", "c1")
  .where("createdAt", ">", "2026-01-01")
  .orderBy("createdAt", "desc")
  .limit(20)
  .get();
```

**Cloudflare**

```ts
const { results } = await env.DB.prepare(
  "SELECT * FROM orders WHERE customer_id = ? AND created_at > ? ORDER BY created_at DESC LIMIT 20",
)
  .bind("c1", "2026-01-01")
  .all();
```

Cosmos DB queries are cheapest when they target one partition key. Firestore may ask you to create a composite index for this query. D1 needs an index on `(customer_id, created_at)`.

## 167: How do you set a time-to-live on records?

- **AWS:** DynamoDB TTL on a numeric attribute that holds a Unix timestamp in seconds. Deletion happens in the background, usually within a few days.
- **Azure:** Cosmos DB `defaultTtl` on the container and an optional `ttl` field (seconds) per item.
- **GCP:** Firestore TTL policies on a timestamp field, deleted usually within 24 hours after expiry.
- **Cloudflare:** Workers KV `expirationTtl` (minimum 60 seconds) on `put`.

**Cloudflare**

```ts
await env.SESSIONS.put(sessionId, JSON.stringify(session), {
  expirationTtl: 3600,
});
```

On every platform except KV, expired items can still be read until they are deleted, so filter by expiry in your queries if it matters.

## 168: How do you react to database changes?

- **AWS:** DynamoDB Streams with a Lambda trigger.
- **Azure:** the Cosmos DB change feed with an Azure Functions Cosmos DB trigger.
- **GCP:** Firestore triggers through Eventarc (for example `google.cloud.firestore.document.v1.written`).

**Azure**

```ts
app.cosmosDB("onUserChange", {
  connection: "CosmosConnection",
  databaseName: "app",
  containerName: "users",
  leaseContainerName: "leases",
  createLeaseContainerIfNotExists: true,
  handler: async (documents: unknown[], context) => {
    context.log(`Changed: ${documents.length}`);
  },
});
```

Cloudflare D1 has no change stream. Publish an event to a Queue in the same code that writes to the database, or use a Durable Object that owns both the write and the notification.

## 169: How do you create a managed SQL database from the CLI?

**AWS**

```bash
aws rds create-db-instance --db-instance-identifier app-db \
  --engine postgres --db-instance-class db.t4g.micro \
  --allocated-storage 20 --master-username app --manage-master-user-password
```

**Azure**

```bash
az postgres flexible-server create --resource-group my-rg --name app-db \
  --tier Burstable --sku-name Standard_B1ms --storage-size 32 \
  --admin-user app --admin-password "$DB_PASSWORD"
```

**GCP**

```bash
gcloud sql instances create app-db --database-version=POSTGRES_17 \
  --tier=db-custom-1-3840 --region=us-central1
```

**Cloudflare**

```bash
npx wrangler d1 create app-db
npx wrangler d1 migrations create app-db init
npx wrangler d1 migrations apply app-db --remote
```

`--manage-master-user-password` stores the password in Secrets Manager for you. D1 is not Postgres: it is SQLite, so migrating from RDS to D1 means checking SQL dialect and data size limits (10 GB per database).

## 170: How do you connect to Postgres efficiently from serverless code?

- **AWS:** RDS Proxy pools connections between Lambda and RDS or Aurora.
- **Azure:** Azure Database for PostgreSQL flexible server has built-in PgBouncer you turn on as a server setting (port 6432).
- **GCP:** the Cloud SQL Node.js Connector or Cloud SQL Auth Proxy for secure connections, plus managed connection pooling on some editions. Keep the pool small and outside the handler.
- **Cloudflare:** Hyperdrive, which keeps pooled connections close to your database and can cache read queries.

**Cloudflare**

```ts
import { Client } from "pg";

export default {
  async fetch(_req: Request, env: { HYPERDRIVE: Hyperdrive }) {
    const client = new Client({
      connectionString: env.HYPERDRIVE.connectionString,
    });
    await client.connect();
    const { rows } = await client.query("SELECT id, name FROM users LIMIT 10");
    return Response.json(rows);
  },
};
```

On all platforms, create clients outside the handler when the runtime reuses instances (Lambda, Azure Functions, Cloud Run). In Workers with Hyperdrive, connecting per request is fine because Hyperdrive does the pooling.

## 171: How do you use IAM authentication instead of a database password?

**AWS**

```ts
import { Signer } from "@aws-sdk/rds-signer";

const token = await new Signer({
  hostname: "app-db.abc.us-east-1.rds.amazonaws.com",
  port: 5432,
  username: "app_iam",
}).getAuthToken();
// use token as the password
```

**Azure**

```ts
import { DefaultAzureCredential } from "@azure/identity";

const { token } = await new DefaultAzureCredential().getToken(
  "https://ossrdbms-aad.database.windows.net/.default",
);
// use token as the password for the Entra-enabled Postgres role
```

**GCP**

```ts
import {
  Connector,
  AuthTypes,
  IpAddressTypes,
} from "@google-cloud/cloud-sql-connector";
import pg from "pg";

const connector = new Connector();
const opts = await connector.getOptions({
  instanceConnectionName: "my-project:us-central1:app-db",
  authType: AuthTypes.IAM,
  ipType: IpAddressTypes.PRIVATE,
});
const pool = new pg.Pool({
  ...opts,
  user: "api@my-project.iam",
  database: "app",
});
```

Tokens are short-lived (15 minutes on AWS, about an hour on Azure), so refresh them when you create new connections.

## 172: How do you read a secret at runtime?

**AWS**

```ts
import {
  SecretsManagerClient,
  GetSecretValueCommand,
} from "@aws-sdk/client-secrets-manager";

const { SecretString } = await new SecretsManagerClient({}).send(
  new GetSecretValueCommand({ SecretId: "db-password" }),
);
```

**Azure**

```ts
import { SecretClient } from "@azure/keyvault-secrets";
import { DefaultAzureCredential } from "@azure/identity";

const client = new SecretClient(
  "https://my-vault.vault.azure.net",
  new DefaultAzureCredential(),
);
const { value } = await client.getSecret("db-password");
```

**GCP**

```ts
import { SecretManagerServiceClient } from "@google-cloud/secret-manager";

const [version] = await new SecretManagerServiceClient().accessSecretVersion({
  name: "projects/my-project/secrets/db-password/versions/latest",
});
const value = version.payload?.data?.toString();
```

**Cloudflare**

```ts
// Worker secret set with `wrangler secret put DB_PASSWORD`
const value = env.DB_PASSWORD;
// Secrets Store binding
const shared = await env.STRIPE_KEY.get();
```

Cache the secret in memory outside the handler so you do not call the secret service on every request.

## 173: How do you inject secrets as environment variables without code?

- **AWS:** Lambda has no native secret env vars. Use the AWS Parameters and Secrets Lambda Extension, or ECS task definitions with `secrets` that reference Secrets Manager.
- **Azure:** Key Vault references in app settings: `@Microsoft.KeyVault(SecretUri=https://my-vault.vault.azure.net/secrets/db-password/)`.
- **GCP:** `--set-secrets` on Cloud Run and Cloud Run functions.
- **Cloudflare:** Worker secrets are always exposed on `env`, never in plain text in the dashboard.

**GCP**

```bash
gcloud run deploy api --image us-central1-docker.pkg.dev/my-project/repo/api:1 \
  --set-secrets DB_PASSWORD=db-password:latest
```

**Azure**

```bash
az functionapp config appsettings set --name my-func-app --resource-group my-rg \
  --settings "DB_PASSWORD=@Microsoft.KeyVault(SecretUri=https://my-vault.vault.azure.net/secrets/db-password/)"
```

The app's managed identity needs the "Key Vault Secrets User" role for the reference to work.

## 174: How do you generate an upload URL so the browser uploads straight to storage?

**AWS**

```ts
import { S3Client, PutObjectCommand } from "@aws-sdk/client-s3";
import { getSignedUrl } from "@aws-sdk/s3-request-presigner";

const url = await getSignedUrl(
  new S3Client({}),
  new PutObjectCommand({
    Bucket: "uploads",
    Key: "a.png",
    ContentType: "image/png",
  }),
  { expiresIn: 600 },
);
```

**Azure**

```ts
import {
  BlobServiceClient,
  BlobSASPermissions,
  generateBlobSASQueryParameters,
} from "@azure/storage-blob";
import { DefaultAzureCredential } from "@azure/identity";

const service = new BlobServiceClient(
  "https://myaccount.blob.core.windows.net",
  new DefaultAzureCredential(),
);
const startsOn = new Date();
const expiresOn = new Date(Date.now() + 10 * 60 * 1000);
const key = await service.getUserDelegationKey(startsOn, expiresOn);
const sas = generateBlobSASQueryParameters(
  {
    containerName: "uploads",
    blobName: "a.png",
    permissions: BlobSASPermissions.parse("cw"),
    startsOn,
    expiresOn,
  },
  key,
  "myaccount",
).toString();
const url = `https://myaccount.blob.core.windows.net/uploads/a.png?${sas}`;
```

**GCP**

```ts
const [url] = await new Storage()
  .bucket("uploads")
  .file("a.png")
  .getSignedUrl({
    version: "v4",
    action: "write",
    expires: Date.now() + 10 * 60 * 1000,
    contentType: "image/png",
  });
```

**Cloudflare**

```ts
import { S3Client, PutObjectCommand } from "@aws-sdk/client-s3";
import { getSignedUrl } from "@aws-sdk/s3-request-presigner";

const r2 = new S3Client({
  region: "auto",
  endpoint: `https://${ACCOUNT_ID}.r2.cloudflarestorage.com`,
  credentials: {
    accessKeyId: R2_ACCESS_KEY_ID,
    secretAccessKey: R2_SECRET_ACCESS_KEY,
  },
});
const url = await getSignedUrl(
  r2,
  new PutObjectCommand({ Bucket: "uploads", Key: "a.png" }),
  { expiresIn: 600 },
);
```

The browser must send a `PUT` with the same content type, and Azure also needs the `x-ms-blob-type: BlockBlob` header. Each bucket needs a CORS rule that allows the browser origin.

## 175: How do you upload a large file in parts?

**AWS**

```ts
import { Upload } from "@aws-sdk/lib-storage";

await new Upload({
  client: new S3Client({}),
  params: {
    Bucket: "backups",
    Key: "db.dump",
    Body: fs.createReadStream("db.dump"),
  },
  partSize: 16 * 1024 * 1024,
}).done();
```

**Azure**

```ts
const blob = service
  .getContainerClient("backups")
  .getBlockBlobClient("db.dump");
await blob.uploadFile("db.dump", {
  blockSize: 16 * 1024 * 1024,
  concurrency: 4,
});
```

**GCP**

```ts
await new Storage().bucket("backups").upload("db.dump", { resumable: true });
```

**Cloudflare**

```ts
const upload = await env.BACKUPS.createMultipartUpload("db.dump");
const part1 = await upload.uploadPart(1, chunk1);
const part2 = await upload.uploadPart(2, chunk2);
await upload.complete([part1, part2]);
```

S3 and R2 use multipart uploads (parts of at least 5 MiB except the last). Azure uses blocks committed with a block list. GCS uses resumable uploads or object composition.

## 176: How do you configure CORS on a bucket?

**AWS**

```bash
aws s3api put-bucket-cors --bucket uploads --cors-configuration '{
  "CORSRules": [{ "AllowedOrigins": ["https://app.example.com"], "AllowedMethods": ["GET","PUT"], "AllowedHeaders": ["*"], "MaxAgeSeconds": 3600 }]
}'
```

**Azure**

```bash
az storage cors add --account-name myaccount --services b \
  --methods GET PUT --origins https://app.example.com \
  --allowed-headers '*' --exposed-headers '*' --max-age 3600
```

**GCP**

```bash
cat > cors.json <<'JSON'
[{ "origin": ["https://app.example.com"], "method": ["GET","PUT"], "responseHeader": ["Content-Type"], "maxAgeSeconds": 3600 }]
JSON
gcloud storage buckets update gs://uploads --cors-file=cors.json
```

**Cloudflare**

```bash
npx wrangler r2 bucket cors set uploads --file cors.json
```

R2's CORS file uses the S3-style rule format (`AllowedOrigins`, `AllowedMethods`) wrapped in a `rules` array. Azure CORS is set per storage account and service, not per container.

## 177: How do you serve a private bucket through the CDN?

- **AWS:** CloudFront with Origin Access Control (OAC) and a bucket policy that allows only that distribution.
- **Azure:** Front Door Premium with a Private Link origin to the storage account, so the account can block public access.
- **GCP:** a backend bucket with Cloud CDN, where the Cloud CDN service account gets read access to the private bucket, or signed URLs and cookies for user-level access.
- **Cloudflare:** a Worker with an R2 binding in front of a private bucket, or an R2 custom domain (public) with WAF and cache rules.

**Cloudflare**

```ts
export default {
  async fetch(request: Request, env: { FILES: R2Bucket }) {
    const key = new URL(request.url).pathname.slice(1);
    const obj = await env.FILES.get(key);
    if (!obj) return new Response("Not found", { status: 404 });
    const headers = new Headers();
    obj.writeHttpMetadata(headers);
    headers.set("etag", obj.httpEtag);
    return new Response(obj.body, { headers });
  },
};
```

## 178: How do you invalidate the CDN cache?

**AWS**

```bash
aws cloudfront create-invalidation --distribution-id E123EXAMPLE --paths "/*"
```

**Azure**

```bash
az afd endpoint purge --resource-group my-rg --profile-name my-fd \
  --endpoint-name my-endpoint --content-paths "/*"
```

**GCP**

```bash
gcloud compute url-maps invalidate-cdn-cache my-url-map --path "/*" --async
```

**Cloudflare**

```bash
curl -X POST "https://api.cloudflare.com/client/v4/zones/$ZONE_ID/purge_cache" \
  -H "Authorization: Bearer $CF_API_TOKEN" -H "Content-Type: application/json" \
  --data '{"files":["https://example.com/app.js"]}'
```

Cloudflare purges usually complete in seconds worldwide. Use versioned file names (`app.3f2a.js`) on every provider so you rarely need to purge at all.

## 179: How do default caching rules differ between CDNs?

- **AWS CloudFront:** caches based on the cache policy you attach (for example `CachingOptimized`), and respects origin `Cache-Control` within the policy's min and max TTLs.
- **Azure Front Door:** caching is off until you enable it on a route, with query string behavior (ignore, use, include or exclude specific ones) and optional compression.
- **GCP Cloud CDN:** cache modes `CACHE_ALL_STATIC` (default), `USE_ORIGIN_HEADERS` and `FORCE_CACHE_ALL`.
- **Cloudflare:** caches only files with static extensions (images, CSS, JS) by default, not HTML or JSON. Use Cache Rules to cache more, and respect or override origin headers.

A common migration bug: HTML was cached on CloudFront and suddenly is not on Cloudflare (or the reverse), so check cache hit rates right after the switch.

## 180: How do you translate a CloudFront Function redirect into the other providers?

**AWS**

```js
function handler(event) {
  var request = event.request;
  if (request.uri === "/old") {
    return {
      statusCode: 301,
      statusDescription: "Moved",
      headers: { location: { value: "/new" } },
    };
  }
  return request;
}
```

**Azure**

```bash
az afd rule create --resource-group my-rg --profile-name my-fd --rule-set-name redirects \
  --rule-name old-to-new --order 1 --match-variable UrlPath --operator Equal \
  --match-values /old --action-name UrlRedirect --redirect-type Moved \
  --custom-path /new
```

**GCP**

```yaml
# URL map pathMatcher snippet
pathRules:
  - paths: ["/old"]
    urlRedirect:
      pathRedirect: /new
      redirectResponseCode: MOVED_PERMANENTLY_DEFAULT
```

**Cloudflare**

```ts
export default {
  async fetch(request: Request) {
    const url = new URL(request.url);
    if (url.pathname === "/old")
      return Response.redirect(new URL("/new", url), 301);
    return fetch(request);
  },
};
```

For many fixed redirects, Cloudflare Bulk Redirects or Single Redirect rules are cheaper and simpler than a Worker.

## 181: How do you serve a single-page app and its API from one deployment?

- **AWS:** S3 + CloudFront for the SPA, and a second CloudFront behavior (`/api/*`) pointing to API Gateway or a Lambda function URL. Set the error response for 404 to `/index.html` for client-side routing.
- **Azure:** Azure Static Web Apps with an `api` folder of Azure Functions, or a linked Functions app, and `navigationFallback` in `staticwebapp.config.json`.
- **GCP:** Firebase Hosting with rewrites to Cloud Run (`"rewrites": [{ "source": "/api/**", "run": { "serviceId": "api" } }]`).
- **Cloudflare:** one Worker with static assets and SPA fallback.

**Cloudflare**

```jsonc
{
  "name": "app",
  "main": "src/worker.ts",
  "compatibility_date": "2026-11-24",
  "assets": {
    "directory": "./dist",
    "not_found_handling": "single-page-application",
    "run_worker_first": ["/api/*"],
  },
}
```

## 182: How do you query logs for errors?

**AWS**

```text
fields @timestamp, @message
| filter @message like /ERROR/
| sort @timestamp desc
| limit 20
```

**Azure**

```kusto
AppTraces
| where SeverityLevel >= 3
| order by TimeGenerated desc
| take 20
```

**GCP**

```text
resource.type="cloud_run_revision"
resource.labels.service_name="api"
severity>=ERROR
```

**Cloudflare**

```bash
npx wrangler tail api --status error
```

For history on Cloudflare, use the Workers Logs query builder in the dashboard or Logpush to R2 or your log platform. KQL on Azure is the most powerful of these query languages, and it is also used by Microsoft Sentinel.

## 183: How do you write structured logs that each platform understands?

- **AWS:** set the Lambda log format to JSON, and log objects. CloudWatch Logs Insights discovers JSON fields automatically.
- **Azure:** use `context.log`, `context.warn` and `context.error` (they map to severity levels in Application Insights), or the OpenTelemetry distro for custom properties.
- **GCP:** print one JSON object per line with a `severity` field and a `message` field. Cloud Logging turns it into a structured entry.
- **Cloudflare:** `console.log` an object. Workers Logs indexes the fields so you can filter on them.

**GCP**

```ts
console.log(
  JSON.stringify({
    severity: "ERROR",
    message: "payment failed",
    orderId: "o1",
  }),
);
```

**Cloudflare**

```ts
console.log({ level: "error", message: "payment failed", orderId: "o1" });
```

## 184: How do you create an alert when a function's errors go up?

**AWS**

```bash
aws cloudwatch put-metric-alarm --alarm-name api-errors \
  --namespace AWS/Lambda --metric-name Errors \
  --dimensions Name=FunctionName,Value=api \
  --statistic Sum --period 300 --evaluation-periods 1 \
  --threshold 5 --comparison-operator GreaterThanThreshold \
  --alarm-actions arn:aws:sns:us-east-1:123456789012:oncall
```

**Azure**

```bash
az monitor metrics alert create --name api-errors --resource-group my-rg \
  --scopes "$FUNCTION_APP_ID" --condition "total Http5xx > 5" \
  --window-size 5m --evaluation-frequency 1m --action "$ACTION_GROUP_ID"
```

**GCP**

```hcl
resource "google_monitoring_alert_policy" "api_errors" {
  display_name = "api errors"
  combiner     = "OR"
  conditions {
    display_name = "5xx > 5"
    condition_threshold {
      filter          = "resource.type = \"cloud_run_revision\" AND metric.type = \"run.googleapis.com/request_count\" AND metric.labels.response_code_class = \"5xx\""
      comparison      = "COMPARISON_GT"
      threshold_value = 5
      duration        = "300s"
      aggregations {
        alignment_period   = "300s"
        per_series_aligner = "ALIGN_SUM"
      }
    }
  }
  notification_channels = [google_monitoring_notification_channel.oncall.id]
}
```

On Cloudflare, you set up Notifications in the dashboard (for example Workers error rate alerts, origin health alerts), or send Workers Logs to your own alerting system.

## 185: How do you add distributed tracing with OpenTelemetry?

- **AWS:** the AWS Distro for OpenTelemetry Lambda layer or the CloudWatch Application Signals setup, exporting to X-Ray or CloudWatch.
- **Azure:** `@azure/monitor-opentelemetry` with `useAzureMonitor()` at startup and the Application Insights connection string.
- **GCP:** the standard OpenTelemetry Node SDK with an OTLP exporter to the Telemetry API, or the Google Cloud trace exporter.
- **Cloudflare:** turn on tracing in `observability` and, if you want, export traces with OTLP to an external destination configured in the dashboard.

**Azure**

```ts
import { useAzureMonitor } from "@azure/monitor-opentelemetry";

useAzureMonitor({
  azureMonitorExporterOptions: {
    connectionString: process.env.APPLICATIONINSIGHTS_CONNECTION_STRING,
  },
});
```

**Cloudflare**

```jsonc
{
  "observability": {
    "enabled": true,
    "traces": { "enabled": true },
  },
}
```

## 186: How do you do canary releases for serverless code?

**AWS**

```bash
aws lambda publish-version --function-name api            # returns version 8
aws lambda update-alias --function-name api --name live \
  --function-version 7 --routing-config '{"AdditionalVersionWeights":{"8":0.1}}'
```

**Azure**

```bash
# App Service / Functions Premium: route 10% to the staging slot
az webapp traffic-routing set --resource-group my-rg --name my-app \
  --distribution staging=10
```

**GCP**

```bash
gcloud run deploy api --image "$IMAGE" --no-traffic --tag canary --region us-central1
gcloud run services update-traffic api --to-tags canary=10 --region us-central1
```

**Cloudflare**

```bash
npx wrangler versions upload
npx wrangler versions deploy <old-version-id>@90% <new-version-id>@10%
```

Flex Consumption Function apps do not support deployment slots, so on Azure, canaries for serverless code often run on Container Apps revisions with traffic weights instead.

## 187: How do Lambda versions and aliases map to the other platforms?

| AWS Lambda          | Azure                                           | GCP Cloud Run              | Cloudflare Workers                      |
| ------------------- | ----------------------------------------------- | -------------------------- | --------------------------------------- |
| Version (immutable) | Container Apps revision / deployment            | Revision (immutable)       | Version                                 |
| Alias (`live`)      | Deployment slot (App Service) or revision label | Revision tag (URL per tag) | Deployment (which versions get traffic) |
| `$LATEST`           | Production slot                                 | Latest ready revision      | Current deployment                      |

Cloud Run tags give each revision its own URL (`https://canary---api-abc.a.run.app`), which is handy for testing before sending traffic. Workers versions can be previewed through version preview URLs.

## 188: How do you roll back a bad deployment?

**AWS**

```bash
aws lambda update-alias --function-name api --name live --function-version 7
```

**Azure**

```bash
az webapp deployment slot swap --resource-group my-rg --name my-app --slot staging
# swapping again puts the previous code back in production
```

**GCP**

```bash
gcloud run services update-traffic api --to-revisions api-00041-xyz=100 --region us-central1
```

**Cloudflare**

```bash
npx wrangler rollback
```

Rollbacks only restore code. Database migrations and data changes do not roll back, so design schema changes to be backward compatible (expand, then contract).

## 189: How do you run and test functions locally?

- **AWS:** AWS SAM CLI (`sam local invoke`, `sam local start-api`), or LocalStack to emulate AWS services.
- **Azure:** Azure Functions Core Tools (`func start`), Azurite for Storage, and the Cosmos DB and Service Bus emulators.
- **GCP:** the Functions Framework (`npx @google-cloud/functions-framework --target=hello`), plus emulators for Firestore, Pub/Sub, Bigtable and Spanner in `gcloud emulators` or the Firebase Emulator Suite.
- **Cloudflare:** `wrangler dev`, which runs the real `workerd` runtime locally with local versions of KV, R2, D1, Durable Objects and Queues.

Cloudflare's local mode is closest to production, because it is the same open-source runtime that runs on the edge.

## 190: How do you unit test a handler on each platform?

**AWS**

```ts
import { handler } from "./index";

test("returns greeting", async () => {
  const res = await handler(
    { queryStringParameters: { name: "Ana" } } as any,
    {} as any,
    () => {},
  );
  expect(res).toMatchObject({ statusCode: 200, body: "Hello, Ana!" });
});
```

**Azure**

```ts
import { HttpRequest, InvocationContext } from "@azure/functions";
import { hello } from "./hello";

test("returns greeting", async () => {
  const req = new HttpRequest({
    method: "GET",
    url: "http://localhost/api/hello?name=Ana",
  });
  const res = await hello(req, new InvocationContext());
  expect(res.body).toBe("Hello, Ana!");
});
```

**GCP**

```ts
import { getTestServer } from "@google-cloud/functions-framework/testing";
import request from "supertest";
import "./index";

test("returns greeting", async () => {
  const res = await request(getTestServer("hello")).get("/?name=Ana");
  expect(res.text).toBe("Hello, Ana!");
});
```

**Cloudflare**

```ts
import { SELF } from "cloudflare:test";

test("returns greeting", async () => {
  const res = await SELF.fetch("https://example.com/?name=Ana");
  expect(await res.text()).toBe("Hello, Ana!");
});
```

The Cloudflare test uses `@cloudflare/vitest-pool-workers`, which runs tests inside the Workers runtime with real bindings. For the Azure test, export the handler function separately from `app.http` so you can call it directly.

## 191: How do you manage several environments (dev, staging, prod)?

- **AWS:** one account per environment in AWS Organizations, with separate stacks or Terraform workspaces.
- **Azure:** one subscription per environment (or resource groups for small teams), with parameter files per environment.
- **GCP:** one project per environment, often under folders like `nonprod` and `prod`.
- **Cloudflare:** Wrangler environments in one file, deployed as separate Workers, often in separate accounts for production.

**Cloudflare**

```jsonc
{
  "name": "api",
  "main": "src/index.ts",
  "compatibility_date": "2026-11-24",
  "vars": { "STAGE": "dev" },
  "env": {
    "staging": { "vars": { "STAGE": "staging" } },
    "production": {
      "vars": { "STAGE": "prod" },
      "routes": [{ "pattern": "api.example.com", "custom_domain": true }],
    },
  },
}
```

```bash
npx wrangler deploy --env production
```

Bindings and vars are not inherited by named environments in Wrangler, so you repeat them in each `env` block.

## 192: How are function dependencies packaged?

- **AWS:** you upload a zip (or container image) with your bundled code. Teams bundle with esbuild and use Lambda layers for shared dependencies.
- **Azure:** `func azure functionapp publish` uploads the project, and a remote build runs `npm install` on Linux. You can also deploy a pre-built zip.
- **GCP:** you upload source, and Cloud Build runs Google Cloud's buildpacks (`npm install`, `npm run build` via `gcp-build`) to create an image.
- **Cloudflare:** Wrangler bundles your code and dependencies with esbuild into one script before upload. Native Node add-ons do not work.

Lambda layers have no direct equivalent elsewhere. On other platforms you either bundle shared code into each function or publish a private npm package.

## 193: What do you need to change for Node.js code to run on Workers?

- Add `"compatibility_flags": ["nodejs_compat"]` to `wrangler.jsonc`. This turns on many Node built-ins such as `node:buffer`, `node:crypto`, `node:stream`, `node:events` and parts of `node:fs` (an in-memory file system) and `node:net`.
- Replace `process.env` reads with `env` bindings, or rely on `nodejs_compat` populating `process.env` from vars and secrets.
- Replace long-lived module-level state (in-memory caches, open sockets reused across requests) with KV, Durable Objects or Hyperdrive.
- Replace native add-ons (`sharp`, `bcrypt` native builds) with WebAssembly or pure-JS versions, or Cloudflare Images for image work.
- Keep CPU work small. Heavy tasks go to Containers or another cloud.

## 194: How do you run an existing Express app on each platform?

- **AWS:** wrap it with `@codegenie/serverless-express` for Lambda, or run it unchanged in a container with the AWS Lambda Web Adapter, ECS or Elastic Beanstalk.
- **Azure:** run it unchanged on App Service or Container Apps. Azure Functions is not a good fit for a whole Express app.
- **GCP:** run it unchanged on Cloud Run (`gcloud run deploy --source .`), or pass the Express app to `functions.http`.
- **Cloudflare:** run it with `nodejs_compat` and the Workers `node:http` support, or move routes to Hono, which is the more common path.

**GCP**

```bash
gcloud run deploy api --source . --region us-central1 --allow-unauthenticated
```

Cloud Run is the easiest target: anything that listens on `$PORT` in a container just works.

## 195: How do you deploy a container web service on each platform?

**AWS**

```bash
aws ecs create-service --cluster main --service-name api \
  --task-definition api:1 --desired-count 2 --launch-type FARGATE \
  --network-configuration "awsvpcConfiguration={subnets=[subnet-a,subnet-b],securityGroups=[sg-1]}" \
  --load-balancers targetGroupArn=$TG_ARN,containerName=api,containerPort=8080
```

**Azure**

```bash
az containerapp create --name api --resource-group my-rg \
  --environment my-env --image myregistry.azurecr.io/api:1.0.0 \
  --target-port 8080 --ingress external --min-replicas 0 --max-replicas 10
```

**GCP**

```bash
gcloud run deploy api --image us-central1-docker.pkg.dev/my-project/repo/api:1.0.0 \
  --port 8080 --region us-central1 --min-instances 0 --max-instances 10
```

**Cloudflare**

```ts
import { Container, getContainer } from "@cloudflare/containers";

export class Api extends Container {
  defaultPort = 8080;
  sleepAfter = "5m";
}

export default {
  async fetch(request: Request, env: { API: DurableObjectNamespace<Api> }) {
    return getContainer(env.API).fetch(request);
  },
};
```

```jsonc
{
  "containers": [
    { "class_name": "Api", "image": "./Dockerfile", "max_instances": 10 },
  ],
  "durable_objects": { "bindings": [{ "name": "API", "class_name": "Api" }] },
  "migrations": [{ "tag": "v1", "new_sqlite_classes": ["Api"] }],
}
```

ECS needs a cluster, task definition, target group and load balancer. Container Apps and Cloud Run give you autoscaling and an HTTPS URL in one command. On Cloudflare, a Worker decides which container instance handles each request.

## 196: How does an ECS task definition translate?

**AWS**

```json
{
  "family": "api",
  "cpu": "512",
  "memory": "1024",
  "networkMode": "awsvpc",
  "requiresCompatibilities": ["FARGATE"],
  "containerDefinitions": [
    {
      "name": "api",
      "image": "123456789012.dkr.ecr.us-east-1.amazonaws.com/api:1.0.0",
      "portMappings": [{ "containerPort": 8080 }],
      "environment": [{ "name": "STAGE", "value": "prod" }],
      "secrets": [
        {
          "name": "DB_PASSWORD",
          "valueFrom": "arn:aws:secretsmanager:us-east-1:123456789012:secret:db-password"
        }
      ]
    }
  ]
}
```

**Azure**

```yaml
properties:
  template:
    containers:
      - name: api
        image: myregistry.azurecr.io/api:1.0.0
        resources: { cpu: 0.5, memory: 1Gi }
        env:
          - name: STAGE
            value: prod
          - name: DB_PASSWORD
            secretRef: db-password
  configuration:
    ingress: { external: true, targetPort: 8080 }
    secrets:
      - name: db-password
        keyVaultUrl: https://my-vault.vault.azure.net/secrets/db-password
        identity: system
```

**GCP**

```yaml
apiVersion: serving.knative.dev/v1
kind: Service
metadata:
  name: api
spec:
  template:
    spec:
      containers:
        - image: us-central1-docker.pkg.dev/my-project/repo/api:1.0.0
          ports: [{ containerPort: 8080 }]
          resources: { limits: { cpu: "1", memory: 1Gi } }
          env:
            - name: STAGE
              value: prod
            - name: DB_PASSWORD
              valueFrom:
                secretKeyRef: { name: db-password, key: latest }
```

Cloud Run uses the Knative service format, so you apply it with `gcloud run services replace service.yaml`. On Cloudflare, you set the instance type in the `containers` section of `wrangler.jsonc` and pass env vars from the Worker through the `Container` class (`envVars`).

## 197: How do autoscaling settings for containers compare?

| Setting               | ECS (Fargate)                                           | Container Apps                                       | Cloud Run                             | Cloudflare Containers               |
| --------------------- | ------------------------------------------------------- | ---------------------------------------------------- | ------------------------------------- | ----------------------------------- |
| Min / max             | Service Auto Scaling min / max tasks                    | `--min-replicas` / `--max-replicas`                  | `--min-instances` / `--max-instances` | `max_instances`; started on demand  |
| Scale signal          | CPU, memory, ALB request count                          | HTTP concurrency, KEDA scalers (queues, CPU, custom) | Request concurrency, CPU              | Requests routed by the Worker       |
| Scale to zero         | No (min 0 tasks possible, but no auto start on request) | Yes                                                  | Yes                                   | Yes (`sleepAfter`)                  |
| Requests per instance | Unlimited (your app decides)                            | Concurrency rule                                     | `--concurrency` (default 80)          | One container per Durable Object id |

Container Apps uses KEDA under the hood, so it can scale on Service Bus queue length or Kafka lag directly. That makes it a good home for workers translated from ECS services that poll SQS.

## 198: How do you run scheduled container jobs?

**AWS**

```bash
aws scheduler create-schedule --name nightly-report \
  --schedule-expression "cron(0 3 * * ? *)" --flexible-time-window Mode=OFF \
  --target '{"Arn":"arn:aws:ecs:us-east-1:123456789012:cluster/main","RoleArn":"arn:aws:iam::123456789012:role/scheduler","EcsParameters":{"TaskDefinitionArn":"arn:aws:ecs:us-east-1:123456789012:task-definition/report:3","LaunchType":"FARGATE","NetworkConfiguration":{"awsvpcConfiguration":{"Subnets":["subnet-a"]}}}}'
```

**Azure**

```bash
az containerapp job create --name nightly-report --resource-group my-rg \
  --environment my-env --trigger-type Schedule --cron-expression "0 3 * * *" \
  --image myregistry.azurecr.io/report:1.0.0 --replica-timeout 1800
```

**GCP**

```bash
gcloud run jobs create nightly-report --image "$IMAGE" --region us-central1 --task-timeout 30m
gcloud scheduler jobs create http nightly-report-trigger --location us-central1 \
  --schedule "0 3 * * *" --http-method POST \
  --uri "https://run.googleapis.com/v2/projects/my-project/locations/us-central1/jobs/nightly-report:run" \
  --oauth-service-account-email scheduler@my-project.iam.gserviceaccount.com
```

**Cloudflare**

```ts
export default {
  async scheduled(
    controller: ScheduledController,
    env: Env,
    ctx: ExecutionContext,
  ) {
    ctx.waitUntil(
      env.REPORT_WORKFLOW.create({
        params: { date: new Date().toISOString() },
      }),
    );
  },
};
```

On Cloudflare, a Cron Trigger usually starts a Workflow, which splits the job into durable steps instead of one long-running process.

## 199: How do Kubernetes pods get cloud credentials?

- **AWS:** EKS Pod Identity (newer) or IAM Roles for Service Accounts (IRSA). A Kubernetes service account maps to an IAM role.
- **Azure:** Microsoft Entra Workload ID on AKS. A Kubernetes service account federates with a user-assigned managed identity.
- **GCP:** Workload Identity Federation for GKE. You can grant IAM roles directly to a Kubernetes service account principal, or link it to a Google service account.

**Azure**

```yaml
apiVersion: v1
kind: ServiceAccount
metadata:
  name: api
  annotations:
    azure.workload.identity/client-id: <managed-identity-client-id>
---
# pod template labels
metadata:
  labels:
    azure.workload.identity/use: "true"
```

**GCP**

```bash
gcloud storage buckets add-iam-policy-binding gs://my-bucket \
  --role=roles/storage.objectViewer \
  --member="principal://iam.googleapis.com/projects/123456/locations/global/workloadIdentityPools/my-project.svc.id.goog/subject/ns/default/sa/api"
```

In all three, the SDK default credential chain picks up the identity automatically, so application code does not change.

## 200: How do Kubernetes ingress and load balancers translate?

- **AWS:** AWS Load Balancer Controller creates an ALB for `Ingress` and an NLB for `Service type: LoadBalancer`. EKS Auto Mode includes it.
- **Azure:** the application routing add-on (managed NGINX) or Application Gateway for Containers, which supports the Gateway API. `Service type: LoadBalancer` creates an Azure Load Balancer rule.
- **GCP:** GKE Gateway controller (Gateway API) or GKE Ingress, both creating Google Cloud load balancers. `Service type: LoadBalancer` creates a passthrough Network Load Balancer.

The Kubernetes Gateway API is the most portable choice, since all three providers support it with their own `GatewayClass`.

## 201: How do Kubernetes storage classes translate?

| Need                 | EKS                   | AKS                                   | GKE                            |
| -------------------- | --------------------- | ------------------------------------- | ------------------------------ |
| Block disk, one node | `gp3` (EBS CSI)       | `managed-csi` / `managed-csi-premium` | `standard-rwo` / `premium-rwo` |
| Shared file system   | EFS CSI               | `azurefile-csi`                       | Filestore CSI                  |
| Object storage mount | Mountpoint for S3 CSI | BlobFuse CSI                          | Cloud Storage FUSE CSI         |

Block disks on all three are zonal, so a pod with a `ReadWriteOnce` volume cannot move to a node in another zone. Use zone-redundant options (Azure ZRS disks, GKE regional persistent disks) when you need that.

## 202: How do you get cloud secrets into Kubernetes pods?

- **AWS:** Secrets Store CSI Driver with the AWS provider, or External Secrets Operator syncing from Secrets Manager.
- **Azure:** the Azure Key Vault provider for Secrets Store CSI Driver (an AKS add-on).
- **GCP:** Secret Manager add-on for GKE (Secrets Store CSI based), or External Secrets Operator.

External Secrets Operator supports all three backends with the same `ExternalSecret` resource, which makes a multi-cloud move easier.

## 203: How does Kubernetes node autoscaling compare?

- **AWS:** Karpenter (or EKS Auto Mode, which runs Karpenter for you), or Cluster Autoscaler with managed node groups.
- **Azure:** Cluster Autoscaler on node pools, or node auto-provisioning (based on Karpenter). AKS Automatic sets this up for you.
- **GCP:** Cluster Autoscaler with node auto-provisioning on GKE Standard, or Autopilot, where you never manage nodes and pay per pod resource request.

GKE Autopilot is closest to "Fargate for all pods". EKS Auto Mode and AKS Automatic are the closest matches on the other two.

## 204: How do you configure a Terraform state backend on each provider?

**AWS**

```hcl
terraform {
  backend "s3" {
    bucket       = "my-tf-state"
    key          = "app/terraform.tfstate"
    region       = "us-east-1"
    use_lockfile = true
  }
}
```

**Azure**

```hcl
terraform {
  backend "azurerm" {
    resource_group_name  = "tfstate-rg"
    storage_account_name = "mytfstate123"
    container_name       = "tfstate"
    key                  = "app.terraform.tfstate"
    use_azuread_auth     = true
  }
}
```

**GCP**

```hcl
terraform {
  backend "gcs" {
    bucket = "my-tf-state"
    prefix = "app"
  }
}
```

**Cloudflare**

```hcl
terraform {
  backend "s3" {
    bucket                      = "tf-state"
    key                         = "app/terraform.tfstate"
    region                      = "auto"
    endpoints                   = { s3 = "https://<account-id>.r2.cloudflarestorage.com" }
    skip_credentials_validation = true
    skip_region_validation      = true
    skip_requesting_account_id  = true
    skip_metadata_api_check     = true
    skip_s3_checksum            = true
    use_path_style              = true
  }
}
```

The S3 backend's `use_lockfile` replaces the older DynamoDB lock table. Azure Blob and GCS lock state natively. R2 works through the S3 backend with the S3 compatibility flags.

## 205: How do Terraform providers authenticate?

- **AWS:** the standard AWS credential chain (`AWS_PROFILE`, SSO, OIDC role in CI).
- **Azure:** `azurerm` uses Azure CLI login locally, and OIDC (`ARM_USE_OIDC=true`, `ARM_CLIENT_ID`, `ARM_TENANT_ID`, `ARM_SUBSCRIPTION_ID`) or managed identity in CI. It also needs `features {}` in the provider block.
- **GCP:** Application Default Credentials, often with `impersonate_service_account` in the provider block.
- **Cloudflare:** an API token in `CLOUDFLARE_API_TOKEN`.

**Azure**

```hcl
provider "azurerm" {
  features {}
  subscription_id = var.subscription_id
}
```

**GCP**

```hcl
provider "google" {
  project                     = "my-project"
  region                      = "us-central1"
  impersonate_service_account = "terraform@my-project.iam.gserviceaccount.com"
}
```

## 206: How do you translate a CloudFormation template into Bicep?

**AWS**

```yaml
Resources:
  FilesBucket:
    Type: AWS::S3::Bucket
    Properties:
      BucketName: my-app-files-123
      VersioningConfiguration:
        Status: Enabled
Outputs:
  BucketName:
    Value: !Ref FilesBucket
```

**Azure**

```bicep
param location string = resourceGroup().location

resource files 'Microsoft.Storage/storageAccounts@2023-05-01' = {
  name: 'myappfiles123'
  location: location
  sku: { name: 'Standard_ZRS' }
  kind: 'StorageV2'
  properties: { allowBlobPublicAccess: false }
}

resource blobService 'Microsoft.Storage/storageAccounts/blobServices@2023-05-01' = {
  parent: files
  name: 'default'
  properties: { isVersioningEnabled: true }
}

output accountName string = files.name
```

```bash
az deployment group create --resource-group my-rg --template-file main.bicep
```

The structure maps well: `Parameters` become `param`, `Resources` become `resource`, `Outputs` become `output`, and `!Ref`/`!GetAtt` become plain property access. CloudFormation stacks map to deployment stacks (`az stack group create`) when you want Azure to track and delete the resources together.

## 207: How do you translate Lambda reserved concurrency?

- **AWS:** reserved concurrency caps how many instances a function can use (`aws lambda put-function-concurrency --reserved-concurrent-executions 20`).
- **Azure:** on Flex Consumption, set the maximum instance count (`az functionapp scale config set --maximum-instance-count 20`) and per-instance HTTP concurrency.
- **GCP:** `--max-instances 20` on the function or Cloud Run service, plus `--concurrency` for requests per instance.

Workers have no instance cap you control. To protect a fragile backend from a Worker, use a Queue with `max_concurrency` on the consumer, rate limiting, or a Durable Object that serializes access.

## 208: How do you translate Lambda provisioned concurrency?

- **AWS:** provisioned concurrency keeps N instances warm (`aws lambda put-provisioned-concurrency-config`).
- **Azure:** always-ready instances on Flex Consumption, or a Premium plan with pre-warmed instances.
- **GCP:** `--min-instances` on Cloud Run functions or Cloud Run.

**GCP**

```bash
gcloud run services update api --min-instances 2 --region us-central1
```

Workers do not need this because isolates start in milliseconds.

## 209: How do you let a function reach private resources in a VPC?

- **AWS:** attach the Lambda function to VPC subnets and security groups.
- **Azure:** VNet integration on the Function app (Flex Consumption and Premium support it), with a dedicated delegated subnet.
- **GCP:** Direct VPC egress (`--network`, `--subnet`) on Cloud Run and Cloud Run functions, or the older Serverless VPC Access connector.
- **Cloudflare:** run `cloudflared` (Cloudflare Tunnel) inside the private network, and reach it from Workers. For databases, Hyperdrive can connect through a Tunnel.

**GCP**

```bash
gcloud run deploy api --image "$IMAGE" --region us-central1 \
  --network default --subnet default --vpc-egress private-ranges-only
```

## 210: How do you give serverless code a fixed outbound IP?

- **AWS:** put the Lambda function in private subnets with a NAT gateway that has an Elastic IP.
- **Azure:** VNet integration plus a NAT Gateway with a static public IP on the integration subnet, with all traffic routed through the VNet.
- **GCP:** Direct VPC egress with `--vpc-egress all-traffic` and Cloud NAT using a reserved static IP.

Workers do not have fixed outbound IPs. If a partner needs an IP allowlist, put a small proxy with a static IP on another cloud, or use authentication that does not depend on IPs (mTLS with the Workers `mtls_certificates` binding, signed requests, or Cloudflare Tunnel).

## 211: How do you require client certificates (mTLS) on an API?

- **AWS:** API Gateway custom domain with mutual TLS and a truststore in S3, or ALB mTLS with a trust store.
- **Azure:** API Management client certificate validation in policies, or Application Gateway mutual authentication.
- **GCP:** external Application Load Balancer mTLS with a `TrustConfig` in Certificate Manager and a server TLS policy.
- **Cloudflare:** API Shield mTLS, with Cloudflare-issued client certificates and a WAF rule that blocks requests without a valid certificate.

**Cloudflare**

```text
(http.host eq "api.example.com" and not cf.tls_client_auth.cert_verified)
```

That expression in a WAF custom rule with the Block action enforces mTLS at the edge.

## 212: How do you validate JWTs at the gateway?

**AWS**

```bash
aws apigatewayv2 create-authorizer --api-id abc123 --authorizer-type JWT \
  --name auth0 --identity-source '$request.header.Authorization' \
  --jwt-configuration Audience=https://api.example.com,Issuer=https://example.auth0.com/
```

**Azure**

```xml
<validate-jwt header-name="Authorization" failed-validation-httpcode="401">
  <openid-config url="https://example.auth0.com/.well-known/openid-configuration" />
  <audiences><audience>https://api.example.com</audience></audiences>
</validate-jwt>
```

**GCP**

```yaml
# API Gateway OpenAPI 2.0 spec
securityDefinitions:
  auth0:
    authorizationUrl: ""
    flow: implicit
    type: oauth2
    x-google-issuer: https://example.auth0.com/
    x-google-jwks_uri: https://example.auth0.com/.well-known/jwks.json
    x-google-audiences: https://api.example.com
```

**Cloudflare**

```ts
import { createRemoteJWKSet, jwtVerify } from "jose";

const JWKS = createRemoteJWKSet(
  new URL("https://example.auth0.com/.well-known/jwks.json"),
);

export default {
  async fetch(request: Request) {
    const token = request.headers.get("authorization")?.replace(/^Bearer /, "");
    if (!token) return new Response("Unauthorized", { status: 401 });
    try {
      await jwtVerify(token, JWKS, {
        issuer: "https://example.auth0.com/",
        audience: "https://api.example.com",
      });
    } catch {
      return new Response("Unauthorized", { status: 401 });
    }
    return fetch(request);
  },
};
```

Cloudflare API Shield also has JWT validation rules that check tokens without code.

## 213: How do you rate limit an API?

- **AWS:** API Gateway throttling and usage plans with API keys, or AWS WAF rate-based rules.
- **Azure:** API Management `rate-limit-by-key` and `quota-by-key` policies, or WAF rate limit rules.
- **GCP:** Cloud Armor rate limiting rules (throttle or rate-based ban), or Apigee SpikeArrest and Quota policies.
- **Cloudflare:** rate limiting rules in the WAF, or the Workers Rate Limiting binding for limits inside code.

**Azure**

```xml
<rate-limit-by-key calls="100" renewal-period="60"
  counter-key="@(context.Request.IpAddress)" />
```

**Cloudflare**

```ts
// wrangler.jsonc: "ratelimits": [{ "name": "LIMITER", "namespace_id": "1001", "simple": { "limit": 100, "period": 60 } }]
const { success } = await env.LIMITER.limit({ key: userId });
if (!success) return new Response("Too many requests", { status: 429 });
```

## 214: How do you make storage reachable only from a private network?

- **AWS:** S3 gateway or interface VPC endpoint, and a bucket policy with `aws:SourceVpce`.
- **Azure:** a private endpoint for the storage account (blob sub-resource), a private DNS zone `privatelink.blob.core.windows.net`, and public network access disabled.
- **GCP:** Private Google Access on the subnet (or a Private Service Connect endpoint for Google APIs), plus VPC Service Controls to stop data leaving a perimeter.

**Azure**

```bash
az network private-endpoint create --resource-group my-rg --name files-pe \
  --vnet-name app-vnet --subnet endpoints \
  --private-connection-resource-id "$STORAGE_ID" --group-id blob \
  --connection-name files-pe-conn
az storage account update --name myaccount --resource-group my-rg \
  --public-network-access Disabled
```

On Cloudflare, R2 buckets are private unless you add a public domain, and access goes only through bindings or S3 API credentials.

## 215: How do VPC gateway endpoints compare with Azure service endpoints and Private Google Access?

- **AWS gateway endpoints** (S3, DynamoDB): free, added to route tables, and traffic stays on AWS. Interface endpoints (PrivateLink) cost per hour and per GB.
- **Azure service endpoints:** free, enabled per subnet, and the storage account firewall can allow that subnet. The service still has a public IP. Private endpoints are the PrivateLink equivalent, with a private IP in your VNet.
- **GCP Private Google Access:** free, enabled per subnet, and lets VMs without external IPs reach Google APIs. Private Service Connect gives Google APIs a private IP.

So "S3 gateway endpoint" usually translates to "service endpoint" on Azure and "Private Google Access" on GCP, while "interface endpoint" translates to "private endpoint" or "Private Service Connect".

## 216: How do you translate a security group that allows traffic from another security group?

**AWS**

```bash
aws ec2 authorize-security-group-ingress --group-id sg-db \
  --protocol tcp --port 5432 --source-group sg-app
```

**Azure**

```bash
az network nsg rule create --resource-group my-rg --nsg-name db-nsg \
  --name allow-app --priority 100 --direction Inbound --access Allow \
  --protocol Tcp --destination-port-ranges 5432 \
  --source-asgs app-asg --destination-asgs db-asg
```

**GCP**

```bash
gcloud compute firewall-rules create allow-app-to-db --network app-vpc \
  --direction INGRESS --allow tcp:5432 \
  --source-service-accounts app@my-project.iam.gserviceaccount.com \
  --target-service-accounts db@my-project.iam.gserviceaccount.com
```

Azure uses application security groups (ASGs) as the "group of VMs" label. GCP uses service accounts or network tags. Service accounts are safer than tags because only people with IAM rights can attach them.

## 217: How do you translate network ACLs?

- **AWS:** network ACLs, stateless, numbered rules, attached to subnets.
- **Azure:** an NSG attached to a subnet (stateful) is the usual replacement. Azure has no stateless subnet ACL.
- **GCP:** hierarchical firewall policies at the organization or folder level, and network firewall policies at the VPC level. Both are stateful.

Since NSGs and GCP firewall rules are stateful, you drop the return-traffic rules (ephemeral port ranges) that NACLs need.

## 218: How do you translate private hosted zones?

- **AWS:** Route 53 private hosted zones associated with VPCs.
- **Azure:** Azure Private DNS zones linked to VNets.
- **GCP:** Cloud DNS private zones visible to selected VPC networks.

**Azure**

```bash
az network private-dns zone create --resource-group my-rg --name internal.example.com
az network private-dns link vnet create --resource-group my-rg \
  --zone-name internal.example.com --name app-link \
  --virtual-network app-vnet --registration-enabled false
```

**GCP**

```bash
gcloud dns managed-zones create internal --dns-name internal.example.com. \
  --visibility private --networks app-vpc --description "internal zone"
```

## 219: How do you resolve DNS between on-premises and the cloud?

- **AWS:** Route 53 Resolver inbound and outbound endpoints with forwarding rules.
- **Azure:** Azure DNS Private Resolver with inbound and outbound endpoints and DNS forwarding rulesets.
- **GCP:** Cloud DNS forwarding zones (outbound) and inbound server policies.
- **Cloudflare:** for users and devices on Cloudflare One, Gateway resolver policies forward internal domains to your private DNS servers.

## 220: How do you translate a bastion host setup?

- **AWS:** replace bastion VMs with Session Manager or EC2 Instance Connect Endpoint.
- **Azure:** Azure Bastion in an `AzureBastionSubnet` of the VNet (Standard SKU for native client and tunneling).
- **GCP:** IAP TCP forwarding with a firewall rule that allows only `35.235.240.0/20` (the IAP range).
- **Cloudflare:** Cloudflare Access for Infrastructure, with `cloudflared` or the WARP client in front of SSH and RDP targets.

**GCP**

```bash
gcloud compute firewall-rules create allow-iap-ssh --network app-vpc \
  --allow tcp:22 --source-ranges 35.235.240.0/20
gcloud compute ssh my-vm --zone us-central1-a --tunnel-through-iap
```

## 221: How do load balancer health checks compare?

- **AWS ALB:** target group health checks with path, interval, healthy and unhealthy thresholds.
- **Azure Application Gateway / Front Door:** health probes per backend setting or origin group, with path and interval.
- **GCP:** a health check resource attached to the backend service (HTTP, HTTPS, HTTP/2, TCP, gRPC).
- **Cloudflare Load Balancing:** monitors attached to pools, checked from several Cloudflare regions.

**GCP**

```bash
gcloud compute health-checks create http api-hc --port 8080 --request-path /healthz \
  --check-interval 10s --healthy-threshold 2 --unhealthy-threshold 3
```

In GCP, health check traffic comes from fixed Google ranges (`35.191.0.0/16`, `130.211.0.0/22`), so your firewall must allow them, or the backends will look unhealthy.

## 222: How do sticky sessions translate?

- **AWS ALB:** target group stickiness (duration-based cookie or application cookie).
- **Azure:** Application Gateway cookie-based affinity, Front Door session affinity, or Container Apps session affinity.
- **GCP:** backend service session affinity (generated cookie, header field, HTTP cookie, client IP).
- **Cloudflare:** Load Balancing session affinity by cookie, header or IP, or a Durable Object that routes all requests for one key to one place.

Sticky sessions are often a sign of in-memory session state. During a migration, moving sessions to Redis, Cosmos DB, Firestore or KV usually removes the need.

## 223: How do you build a WebSocket chat room on each platform?

- **AWS:** API Gateway WebSocket API with `$connect`, `$disconnect` and `sendMessage` routes. Connection IDs are stored in DynamoDB, and you broadcast with `PostToConnectionCommand`.
- **Azure:** Azure Web PubSub with groups (`sendToGroup`), and a Function for events.
- **GCP:** a Cloud Run service that handles WebSockets directly, with Memorystore or Pub/Sub to broadcast across instances.
- **Cloudflare:** one Durable Object per room that accepts WebSockets and broadcasts.

**Cloudflare**

```ts
import { DurableObject } from "cloudflare:workers";

export class ChatRoom extends DurableObject {
  async fetch(request: Request) {
    const pair = new WebSocketPair();
    this.ctx.acceptWebSocket(pair[1]);
    return new Response(null, { status: 101, webSocket: pair[0] });
  }

  async webSocketMessage(_ws: WebSocket, message: string | ArrayBuffer) {
    for (const socket of this.ctx.getWebSockets()) socket.send(message);
  }
}

export default {
  async fetch(
    request: Request,
    env: { ROOMS: DurableObjectNamespace<ChatRoom> },
  ) {
    const room = new URL(request.url).searchParams.get("room") ?? "lobby";
    return env.ROOMS.get(env.ROOMS.idFromName(room)).fetch(request);
  },
};
```

The Durable Object version needs no database for connection IDs, because all sockets for a room live in one object. The Hibernation API (`acceptWebSocket`) lets the object sleep between messages, so idle connections cost little.

## 224: How do you stream a response (for example Server-Sent Events or LLM tokens)?

**AWS**

```ts
export const handler = awslambda.streamifyResponse(
  async (event, responseStream) => {
    responseStream.setContentType("text/event-stream");
    for (const word of ["Hello", "from", "Lambda"]) {
      responseStream.write(`data: ${word}\n\n`);
    }
    responseStream.end();
  },
);
```

**Azure**

```ts
import { app } from "@azure/functions";
import { Readable } from "node:stream";

app.setup({ enableHttpStream: true });

app.http("stream", {
  methods: ["GET"],
  handler: async () => ({
    headers: { "content-type": "text/event-stream" },
    body: Readable.from([
      "data: Hello\n\n",
      "data: from\n\n",
      "data: Azure\n\n",
    ]),
  }),
});
```

**GCP**

```ts
functions.http("stream", (req, res) => {
  res.setHeader("content-type", "text/event-stream");
  for (const word of ["Hello", "from", "GCP"]) res.write(`data: ${word}\n\n`);
  res.end();
});
```

**Cloudflare**

```ts
export default {
  async fetch() {
    const { readable, writable } = new TransformStream();
    const writer = writable.getWriter();
    const enc = new TextEncoder();
    (async () => {
      for (const word of ["Hello", "from", "Workers"])
        await writer.write(enc.encode(`data: ${word}\n\n`));
      await writer.close();
    })();
    return new Response(readable, {
      headers: { "content-type": "text/event-stream" },
    });
  },
};
```

Lambda response streaming works with function URLs (and API Gateway REST APIs with streaming enabled). The global `awslambda` object only exists inside the Lambda Node.js runtime.

## 225: How do you translate a Step Functions workflow into the other platforms?

**AWS**

```json
{
  "StartAt": "Charge",
  "States": {
    "Charge": {
      "Type": "Task",
      "Resource": "arn:aws:lambda:us-east-1:123456789012:function:charge",
      "Next": "Ship"
    },
    "Ship": {
      "Type": "Task",
      "Resource": "arn:aws:lambda:us-east-1:123456789012:function:ship",
      "End": true
    }
  }
}
```

**Azure**

```ts
import * as df from "durable-functions";

df.app.orchestration("orderFlow", function* (context) {
  const order = context.df.getInput();
  const payment = yield context.df.callActivity("charge", order);
  yield context.df.callActivity("ship", { order, payment });
});
```

**GCP**

```yaml
main:
  params: [order]
  steps:
    - charge:
        call: http.post
        args:
          url: https://charge-abc123-uc.a.run.app
          body: ${order}
          auth: { type: OIDC }
        result: payment
    - ship:
        call: http.post
        args:
          url: https://ship-abc123-uc.a.run.app
          body: { order: ${order}, payment: ${payment.body} }
          auth: { type: OIDC }
```

**Cloudflare**

```ts
import {
  WorkflowEntrypoint,
  WorkflowStep,
  WorkflowEvent,
} from "cloudflare:workers";

export class OrderFlow extends WorkflowEntrypoint<Env, Order> {
  async run(event: WorkflowEvent<Order>, step: WorkflowStep) {
    const payment = await step.do("charge", () => charge(event.payload));
    await step.do("ship", () => ship(event.payload, payment));
  }
}
```

Durable Functions and Cloudflare Workflows replay the code, so each step must be deterministic outside `callActivity` or `step.do`. Do not call `Date.now()` or `Math.random()` directly in the orchestrator body.

## 226: How do you wait for a human approval inside a workflow?

- **AWS:** Step Functions `.waitForTaskToken`. A task sends the token by email, and the approver's request calls `SendTaskSuccess`.
- **Azure:** Durable Functions `context.df.waitForExternalEvent("Approval")`, raised with `client.raiseEvent(instanceId, "Approval", data)`.
- **GCP:** Workflows callbacks: `events.create_callback_endpoint` creates a URL, and `events.await_callback` waits for a request to it.
- **Cloudflare:** Workflows `step.waitForEvent("approval", { type: "approval", timeout: "7 days" })`, resumed with `instance.sendEvent()`.

**Cloudflare**

```ts
const approval = await step.waitForEvent<{ approved: boolean }>(
  "wait for manager",
  {
    type: "approval",
    timeout: "7 days",
  },
);
if (!approval.payload.approved) return;
```

All four let the workflow sleep for days without paying for compute while it waits.

## 227: How do you add retries with backoff to workflow steps?

**AWS**

```json
"Charge": {
  "Type": "Task",
  "Resource": "arn:aws:lambda:us-east-1:123456789012:function:charge",
  "Retry": [{ "ErrorEquals": ["States.ALL"], "IntervalSeconds": 2, "MaxAttempts": 5, "BackoffRate": 2 }],
  "Next": "Ship"
}
```

**Azure**

```ts
const retry = new df.RetryOptions(2000, 5); // first retry after 2 s, max 5 attempts
retry.backoffCoefficient = 2;
const payment = yield context.df.callActivityWithRetry("charge", retry, order);
```

**GCP**

```yaml
- charge:
    try:
      call: http.post
      args: { url: https://charge-abc123-uc.a.run.app, body: ${order}, auth: { type: OIDC } }
      result: payment
    retry:
      predicate: ${http.default_retry_predicate}
      max_retries: 5
      backoff: { initial_delay: 2, max_delay: 60, multiplier: 2 }
```

**Cloudflare**

```ts
const payment = await step.do(
  "charge",
  {
    retries: { limit: 5, delay: "2 seconds", backoff: "exponential" },
    timeout: "1 minute",
  },
  () => charge(event.payload),
);
```

## 228: How do you translate an EventBridge rule?

**AWS**

```json
{
  "source": ["myapp.orders"],
  "detail-type": ["OrderPlaced"],
  "detail": { "total": [{ "numeric": [">", 100] }] }
}
```

**Azure**

```bash
az eventgrid event-subscription create --name big-orders \
  --source-resource-id "$TOPIC_ID" \
  --endpoint "$FUNCTION_ID" --endpoint-type azurefunction \
  --included-event-types OrderPlaced \
  --advanced-filter data.total NumberGreaterThan 100
```

**GCP**

```bash
gcloud eventarc triggers create big-orders --location us-central1 \
  --destination-run-service big-orders --destination-run-region us-central1 \
  --event-filters type=google.cloud.pubsub.topic.v1.messagePublished \
  --transport-topic projects/my-project/topics/orders \
  --service-account eventarc@my-project.iam.gserviceaccount.com
```

Eventarc filters on event attributes, not on the message body. For body-based filtering like `total > 100`, add a Pub/Sub subscription filter on message attributes, or filter in the handler. Cloudflare has no event bus, so the producer decides where to send each event.

## 229: How do you publish a custom event?

**AWS**

```ts
import {
  EventBridgeClient,
  PutEventsCommand,
} from "@aws-sdk/client-eventbridge";

await new EventBridgeClient({}).send(
  new PutEventsCommand({
    Entries: [
      {
        Source: "myapp.orders",
        DetailType: "OrderPlaced",
        Detail: JSON.stringify(order),
        EventBusName: "app",
      },
    ],
  }),
);
```

**Azure**

```ts
import { EventGridPublisherClient } from "@azure/eventgrid";
import { DefaultAzureCredential } from "@azure/identity";

const client = new EventGridPublisherClient(
  "https://my-topic.eastus-1.eventgrid.azure.net/api/events",
  "CloudEvent",
  new DefaultAzureCredential(),
);
await client.send([
  { type: "OrderPlaced", source: "/myapp/orders", data: order },
]);
```

**GCP**

```ts
await new PubSub().topic("orders").publishMessage({
  json: order,
  attributes: { type: "OrderPlaced" },
});
```

**Cloudflare**

```ts
await env.ORDER_EVENTS.send({ type: "OrderPlaced", data: order });
```

## 230: How do you translate EventBridge Pipes?

- **AWS:** EventBridge Pipes connects a source (SQS, Kinesis, DynamoDB Streams) to a target with optional filtering and enrichment.
- **Azure:** no single service. Event Grid subscriptions, Azure Functions triggers, or Logic Apps do the same job.
- **GCP:** Eventarc Advanced pipelines (bus, enrollments and pipelines with transformations), or a Pub/Sub subscription with a push endpoint and single message transforms.
- **Cloudflare:** a Queue consumer Worker that filters, enriches and forwards.

## 231: How do you translate Kinesis producers and consumers?

**AWS**

```ts
import { KinesisClient, PutRecordCommand } from "@aws-sdk/client-kinesis";

await new KinesisClient({}).send(
  new PutRecordCommand({
    StreamName: "clicks",
    PartitionKey: event.userId,
    Data: new TextEncoder().encode(JSON.stringify(event)),
  }),
);
```

**Azure**

```ts
import { EventHubProducerClient } from "@azure/event-hubs";
import { DefaultAzureCredential } from "@azure/identity";

const producer = new EventHubProducerClient(
  "my-ns.servicebus.windows.net",
  "clicks",
  new DefaultAzureCredential(),
);
await producer.sendBatch([{ body: event }], { partitionKey: event.userId });
```

**GCP**

```ts
await new PubSub()
  .topic("clicks")
  .publishMessage({ json: event, orderingKey: event.userId });
```

**Cloudflare**

```ts
// Pipelines binding writes events to R2 as Iceberg
await env.CLICKS_PIPELINE.send([event]);
```

Kinesis shards and Event Hubs partitions are fixed or manually scaled units of throughput. Pub/Sub scales automatically and has no partitions to manage.

## 232: How do you load streaming data straight into the data warehouse?

- **AWS:** Amazon Data Firehose delivering to Redshift, S3 or Apache Iceberg tables.
- **Azure:** Event Hubs Capture to Data Lake Storage, or Eventstream in Microsoft Fabric.
- **GCP:** a Pub/Sub BigQuery subscription, which writes each message into a BigQuery table with no code.
- **Cloudflare:** Pipelines writing to R2 Data Catalog Iceberg tables, queried with R2 SQL or any Iceberg engine.

**GCP**

```bash
gcloud pubsub subscriptions create clicks-to-bq --topic clicks \
  --bigquery-table my-project:analytics.clicks --use-topic-schema
```

## 233: How do you translate a Redshift COPY into the other warehouses?

**AWS**

```sql
COPY analytics.sales
FROM 's3://my-bucket/sales/'
IAM_ROLE 'arn:aws:iam::123456789012:role/redshift-load'
FORMAT AS PARQUET;
```

**Azure**

```sql
COPY INTO analytics.sales
FROM 'https://myaccount.blob.core.windows.net/data/sales/*.parquet'
WITH (FILE_TYPE = 'PARQUET');
```

**GCP**

```bash
bq load --source_format=PARQUET analytics.sales "gs://my-bucket/sales/*.parquet"
```

The Azure example works in Fabric Data Warehouse and Synapse dedicated SQL pools. In BigQuery you can also skip loading and query the files with an external or BigLake table.

## 234: How do SQL dialects differ when translating Redshift queries?

- **Redshift** is based on PostgreSQL 8 syntax: `DATEADD`, `GETDATE()`, `DISTKEY`/`SORTKEY` in table definitions.
- **Fabric and Synapse** use T-SQL: `DATEADD(day, 7, col)`, `GETDATE()`, `TOP 10` instead of `LIMIT`.
- **BigQuery** uses GoogleSQL: `DATE_ADD(col, INTERVAL 7 DAY)`, `CURRENT_TIMESTAMP()`, backtick-quoted `project.dataset.table`, and partitioning and clustering instead of distribution keys.

| Task       | Redshift             | Fabric / Synapse     | BigQuery                      |
| ---------- | -------------------- | -------------------- | ----------------------------- |
| Add days   | `DATEADD(day, 7, d)` | `DATEADD(day, 7, d)` | `DATE_ADD(d, INTERVAL 7 DAY)` |
| Limit rows | `LIMIT 10`           | `TOP 10`             | `LIMIT 10`                    |
| Now        | `GETDATE()`          | `GETDATE()`          | `CURRENT_TIMESTAMP()`         |

BigQuery Migration Service and Azure's migration tools can translate SQL automatically, but review the output, especially window functions and date math.

## 235: How do you call an LLM on each platform?

**AWS**

```ts
import {
  BedrockRuntimeClient,
  ConverseCommand,
} from "@aws-sdk/client-bedrock-runtime";

const res = await new BedrockRuntimeClient({}).send(
  new ConverseCommand({
    modelId: process.env.BEDROCK_MODEL_ID, // an Anthropic Claude model or inference profile ID
    messages: [{ role: "user", content: [{ text: "Summarize this ticket" }] }],
  }),
);
const text = res.output?.message?.content?.[0]?.text;
```

**Azure**

```ts
import { AzureOpenAI } from "openai";
import {
  DefaultAzureCredential,
  getBearerTokenProvider,
} from "@azure/identity";

const client = new AzureOpenAI({
  endpoint: "https://my-foundry.openai.azure.com",
  azureADTokenProvider: getBearerTokenProvider(
    new DefaultAzureCredential(),
    "https://cognitiveservices.azure.com/.default",
  ),
  apiVersion: "2024-10-21",
  deployment: "gpt-4o",
});
const res = await client.chat.completions.create({
  model: "gpt-4o",
  messages: [{ role: "user", content: "Summarize this ticket" }],
});
```

**GCP**

```ts
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({
  vertexai: true,
  project: "my-project",
  location: "us-central1",
});
const res = await ai.models.generateContent({
  model: "gemini-2.5-flash",
  contents: "Summarize this ticket",
});
const text = res.text;
```

**Cloudflare**

```ts
const res = await env.AI.run("@cf/meta/llama-3.3-70b-instruct-fp8-fast", {
  messages: [{ role: "user", content: "Summarize this ticket" }],
});
```

Model IDs and API versions change often, so read them from config, not code. Bedrock model IDs that start with `us.` or `global.` are cross-region inference profiles.

## 236: How do you create embeddings and run a vector search?

**AWS**

```ts
import {
  S3VectorsClient,
  QueryVectorsCommand,
} from "@aws-sdk/client-s3vectors";

const res = await new S3VectorsClient({}).send(
  new QueryVectorsCommand({
    vectorBucketName: "docs-vectors",
    indexName: "docs",
    queryVector: { float32: embedding },
    topK: 5,
    returnMetadata: true,
  }),
);
```

**Azure**

```ts
import { SearchClient } from "@azure/search-documents";

const results = await searchClient.search("*", {
  vectorSearchOptions: {
    queries: [
      {
        kind: "vector",
        vector: embedding,
        fields: ["contentVector"],
        kNearestNeighborsCount: 5,
      },
    ],
  },
});
```

**GCP**

```sql
-- AlloyDB or Cloud SQL for PostgreSQL with pgvector
SELECT id, content FROM docs ORDER BY embedding <=> $1 LIMIT 5;
```

**Cloudflare**

```ts
const { data } = await env.AI.run("@cf/baai/bge-base-en-v1.5", {
  text: [question],
});
const matches = await env.VECTORIZE.query(data[0], {
  topK: 5,
  returnMetadata: "all",
});
```

The embedding model sets the vector size (for example 768 or 1,536 dimensions), so you must re-embed all documents if you switch models during a migration. Embeddings from different models are not compatible.

## 237: How do you put a gateway in front of LLM calls for caching, logging and limits?

- **AWS:** no dedicated gateway. Teams use Bedrock's invocation logging, Bedrock Guardrails, and API Gateway or a proxy for limits.
- **Azure:** API Management AI gateway policies (`llm-token-limit`, `llm-emit-token-metric`, semantic caching) in front of Foundry or Azure OpenAI.
- **GCP:** Apigee AI policies in front of Vertex AI.
- **Cloudflare:** AI Gateway, which sits in front of Workers AI, OpenAI, Anthropic, Bedrock, Vertex and others, with caching, rate limits, retries, fallbacks and logs.

**Cloudflare**

```ts
import OpenAI from "openai";

const client = new OpenAI({
  apiKey: env.OPENAI_API_KEY,
  baseURL: `https://gateway.ai.cloudflare.com/v1/${env.ACCOUNT_ID}/my-gateway/openai`,
});
```

## 238: How do you add content safety guardrails to LLM apps?

- **AWS:** Amazon Bedrock Guardrails (content filters, denied topics, PII redaction, contextual grounding checks).
- **Azure:** Azure AI Content Safety and Foundry content filters, including Prompt Shields for prompt injection.
- **GCP:** Model Armor for prompt and response screening, and safety settings on Gemini calls.
- **Cloudflare:** Firewall for AI (detects prompt injection and PII in requests to AI apps behind Cloudflare), and AI Gateway guardrails using Llama Guard on Workers AI.

## 239: How do you run a RAG pipeline with mostly managed services?

- **AWS:** Bedrock Knowledge Bases, with S3 as the source and S3 Vectors or OpenSearch Serverless as the store.
- **Azure:** Azure AI Search with integrated vectorization (indexers that chunk and embed), plus Foundry Agent Service or "On your data".
- **GCP:** Vertex AI RAG Engine or Vertex AI Search, with Cloud Storage as the source.
- **Cloudflare:** AI Search (formerly AutoRAG), which indexes an R2 bucket or website into Vectorize and answers with Workers AI.

**Cloudflare**

```ts
const answer = await env.AI.autorag("docs-search").aiSearch({
  query: "How do refunds work?",
});
```

Managed RAG is fast to set up, but chunking, metadata filters and ranking are harder to tune than a pipeline you build yourself.

## 240: How do you host an AI agent?

- **AWS:** Bedrock AgentCore (Runtime, Memory, Gateway, Identity) for any framework, or Bedrock Agents.
- **Azure:** Foundry Agent Service.
- **GCP:** Vertex AI Agent Engine (now called Agent Runtime in the Gemini Enterprise Agent Platform), often with Google's Agent Development Kit (ADK).
- **Cloudflare:** the Agents SDK, where each agent is a Durable Object with its own state, SQL storage, scheduling and WebSockets.

**Cloudflare**

```ts
import { Agent, routeAgentRequest } from "agents";

export class SupportAgent extends Agent<Env, { tickets: number }> {
  initialState = { tickets: 0 };
  async onRequest(_request: Request) {
    this.setState({ tickets: this.state.tickets + 1 });
    return Response.json(this.state);
  }
}

export default {
  async fetch(request: Request, env: Env) {
    return (
      (await routeAgentRequest(request, env)) ??
      new Response("Not found", { status: 404 })
    );
  },
};
```

## 241: How do you translate SES email sending code?

**AWS**

```ts
import { SESv2Client, SendEmailCommand } from "@aws-sdk/client-sesv2";

await new SESv2Client({}).send(
  new SendEmailCommand({
    FromEmailAddress: "no-reply@example.com",
    Destination: { ToAddresses: ["ana@example.com"] },
    Content: {
      Simple: {
        Subject: { Data: "Welcome" },
        Body: { Text: { Data: "Hi Ana" } },
      },
    },
  }),
);
```

**Azure**

```ts
import { EmailClient } from "@azure/communication-email";
import { DefaultAzureCredential } from "@azure/identity";

const client = new EmailClient(
  "https://my-acs.communication.azure.com",
  new DefaultAzureCredential(),
);
const poller = await client.beginSend({
  senderAddress: "no-reply@example.com",
  recipients: { to: [{ address: "ana@example.com" }] },
  content: { subject: "Welcome", plainText: "Hi Ana" },
});
await poller.pollUntilDone();
```

**Cloudflare**

```ts
// send_email binding; Email Service sending is in beta
await env.EMAIL.send({
  from: "no-reply@example.com",
  to: "ana@example.com",
  subject: "Welcome",
  text: "Hi Ana",
});
```

For all providers, set up SPF, DKIM and DMARC for the sending domain before you switch, or mail will land in spam. Cloudflare's sending API is new, so check its current shape and limits before relying on it.

## 242: How do you receive and process incoming email?

- **AWS:** SES receipt rules that store mail in S3 or invoke Lambda.
- **Cloudflare:** Email Routing with an Email Worker.

**Cloudflare**

```ts
export default {
  async email(message: ForwardableEmailMessage, env: Env) {
    if (message.to.startsWith("support@")) {
      await env.TICKETS.send({
        from: message.from,
        subject: message.headers.get("subject"),
      });
      await message.forward("team@example.com");
    } else {
      message.setReject("Unknown address");
    }
  },
};
```

Azure Communication Services and GCP have no inbound email processing, so teams use a provider like SendGrid Inbound Parse or Mailgun routes with a webhook to a function.

## 243: How do you translate Cognito user sign-in for a web app?

- **AWS:** a Cognito user pool with the managed login pages, app client and hosted domain. The app uses OIDC with PKCE and gets ID and access tokens.
- **Azure:** an Entra External ID tenant with user flows, an app registration and MSAL (`@azure/msal-browser`) in the front end.
- **GCP:** Identity Platform with the Firebase Auth SDK (`signInWithPopup`, `signInWithEmailAndPassword`), and ID tokens verified with the Firebase Admin SDK on the server.

All three issue standard JWTs, so backend token checks translate to a new issuer, audience and JWKS URL. Users' passwords usually cannot be exported from Cognito, so plan a lazy migration (verify against Cognito at first login, then create the user in the new system) or force a reset.

## 244: How do you protect an internal admin app with SSO?

- **AWS:** ALB authentication with an OIDC IdP or Cognito, or AWS Verified Access.
- **Azure:** App Service authentication ("Easy Auth") with Entra ID, or Entra application proxy.
- **GCP:** Identity-Aware Proxy (IAP) on the load balancer or directly on Cloud Run.
- **Cloudflare:** Cloudflare Access in front of the hostname, with policies by email, group or device posture.

**GCP**

```bash
gcloud beta run services update admin --region us-central1 --iap
gcloud beta iap web add-iam-policy-binding --resource-type=cloud-run \
  --service=admin --region=us-central1 \
  --member=group:admins@example.com --role=roles/iap.httpsResourceAccessor
```

Behind Cloudflare Access, your app should still verify the `Cf-Access-Jwt-Assertion` header against your team's JWKS, so requests that bypass Cloudflare are rejected.

## 245: How do you translate KMS envelope encryption in code?

**AWS**

```ts
import { KMSClient, GenerateDataKeyCommand } from "@aws-sdk/client-kms";

const { Plaintext, CiphertextBlob } = await new KMSClient({}).send(
  new GenerateDataKeyCommand({ KeyId: "alias/app", KeySpec: "AES_256" }),
);
// encrypt data locally with Plaintext (AES-GCM), store CiphertextBlob next to it
```

**Azure**

```ts
import { CryptographyClient } from "@azure/keyvault-keys";
import { DefaultAzureCredential } from "@azure/identity";
import { randomBytes } from "node:crypto";

const dataKey = randomBytes(32);
const crypto = new CryptographyClient(
  "https://my-vault.vault.azure.net/keys/app",
  new DefaultAzureCredential(),
);
const { result: wrappedKey } = await crypto.wrapKey("RSA-OAEP-256", dataKey);
```

**GCP**

```ts
import { KeyManagementServiceClient } from "@google-cloud/kms";
import { randomBytes } from "node:crypto";

const dataKey = randomBytes(32);
const [res] = await new KeyManagementServiceClient().encrypt({
  name: "projects/my-project/locations/global/keyRings/app/cryptoKeys/data",
  plaintext: dataKey,
});
const wrappedKey = res.ciphertext;
```

AWS KMS generates the data key for you. On Azure and GCP you create the random key yourself and ask the KMS to wrap it. The Tink library on GCP and the Azure SDKs' client-side encryption features can do this pattern for you.

## 246: How do you encrypt storage with your own keys?

**AWS**

```bash
aws s3api put-bucket-encryption --bucket my-bucket --server-side-encryption-configuration \
  '{"Rules":[{"ApplyServerSideEncryptionByDefault":{"SSEAlgorithm":"aws:kms","KMSMasterKeyID":"alias/app"},"BucketKeyEnabled":true}]}'
```

**Azure**

```bash
az storage account update --name myaccount --resource-group my-rg \
  --encryption-key-source Microsoft.Keyvault \
  --encryption-key-vault https://my-vault.vault.azure.net \
  --encryption-key-name storage-key \
  --identity-type UserAssigned --user-identity-id "$IDENTITY_ID" \
  --key-vault-user-identity-id "$IDENTITY_ID"
```

**GCP**

```bash
gcloud storage buckets update gs://my-bucket \
  --default-encryption-key=projects/my-project/locations/us-central1/keyRings/app/cryptoKeys/storage
```

All three encrypt by default with provider-managed keys. Customer-managed keys add control (you can disable the key to cut off access) and audit logs. R2 always encrypts at rest with Cloudflare-managed keys, and has no customer-managed key option.

## 247: How do you rotate secrets?

- **AWS:** Secrets Manager rotation with a Lambda rotation function (managed rotation for RDS and some other services).
- **Azure:** Key Vault automatic rotation policies for keys. For secrets, use the `SecretNearExpiry` Event Grid event to trigger a Function that creates a new version.
- **GCP:** Secret Manager rotation schedules, which publish to a Pub/Sub topic so your function can create a new version.
- **Cloudflare:** no built-in rotation. Run a scheduled Worker or CI job that creates the new credential and updates the secret with the API or `wrangler secret put`.

Whatever the provider, read the "latest" version at runtime and cache it briefly, so a rotation does not need a redeploy.

## 248: How do you add read replicas?

**AWS**

```bash
aws rds create-db-instance-read-replica --db-instance-identifier app-db-replica \
  --source-db-instance-identifier app-db
```

**Azure**

```bash
az postgres flexible-server replica create --replica-name app-db-replica \
  --resource-group my-rg --source-server app-db
```

**GCP**

```bash
gcloud sql instances create app-db-replica --master-instance-name=app-db --region=us-central1
```

**Cloudflare**

```ts
// D1 read replication: a session keeps reads consistent with this user's earlier writes
const session = env.DB.withSession(
  request.headers.get("x-d1-bookmark") ?? "first-unconstrained",
);
const user = await session
  .prepare("SELECT * FROM users WHERE id = ?")
  .bind(id)
  .first();
const response = Response.json(user);
response.headers.set("x-d1-bookmark", session.getBookmark() ?? "");
```

D1 replicas are created and placed by Cloudflare when you turn on read replication. The Sessions API with bookmarks gives "read your own writes" consistency.

## 249: How do you make a managed database highly available?

- **AWS:** RDS Multi-AZ (a standby in another zone, or Multi-AZ DB clusters with two readable standbys), or Aurora replicas across zones.
- **Azure:** zone-redundant high availability on flexible server (`--high-availability ZoneRedundant`), or zone redundancy on Azure SQL Database.
- **GCP:** Cloud SQL high availability (`--availability-type=REGIONAL`), with a standby in another zone.
- **Cloudflare:** D1 is managed by Cloudflare and stored durably, so there is no HA setting to configure.

Failover time is usually 1 to 2 minutes on all three big clouds. Your app must retry connections, because the DNS name moves to the new primary.

## 250: How do you restore a database to a point in time?

**AWS**

```bash
aws rds restore-db-instance-to-point-in-time --source-db-instance-identifier app-db \
  --target-db-instance-identifier app-db-restored --restore-time 2026-11-24T09:30:00Z
```

**Azure**

```bash
az postgres flexible-server restore --resource-group my-rg --name app-db-restored \
  --source-server app-db --restore-time "2026-11-24T09:30:00Z"
```

**GCP**

```bash
gcloud sql instances clone app-db app-db-restored --point-in-time 2026-11-24T09:30:00Z
```

**Cloudflare**

```bash
npx wrangler d1 time-travel restore app-db --timestamp 2026-11-24T09:30:00Z
```

The three big clouds restore into a new instance, so you then switch the app's connection string. D1 Time Travel restores the database in place (and gives you a bookmark to undo the restore).

## 251: How do you migrate a database between clouds with minimal downtime?

- **AWS:** AWS Database Migration Service (full load plus change data capture).
- **Azure:** Azure Database Migration Service, and the migration service in Azure Database for PostgreSQL for online migrations.
- **GCP:** Database Migration Service, which supports continuous migration from PostgreSQL and MySQL (including RDS and Aurora) into Cloud SQL and AlloyDB.

Cloudflare has no migration service for D1. You export data, convert it to SQLite SQL, and import with `wrangler d1 execute --file`. For a live cut-over, keep the old database as the source of truth until you switch writes.

## 252: How do you load existing data into D1?

```bash
npx wrangler d1 execute app-db --remote --file=./schema.sql
npx wrangler d1 execute app-db --remote --file=./data.sql
npx wrangler d1 export app-db --remote --output=./backup.sql
```

From Postgres or MySQL, you export data as plain `INSERT` statements and fix dialect differences: SQLite has no `SERIAL` (use `INTEGER PRIMARY KEY`), no native boolean or date types (use integers and ISO strings), and different JSON functions. Large imports should be split into files so a single statement stays under D1's limits.

## 253: How do NoSQL pricing models compare?

| Provider      | Capacity model                                                                      |
| ------------- | ----------------------------------------------------------------------------------- |
| DynamoDB      | On-demand (per read and write request unit) or provisioned RCU/WCU with autoscaling |
| Cosmos DB     | Request units (RU/s): provisioned, autoscale or serverless                          |
| Firestore     | Per document read, write and delete, plus storage                                   |
| Cloudflare D1 | Rows read and rows written, plus storage                                            |
| Workers KV    | Reads, writes, deletes, lists and storage                                           |

A query that scans many items is cheap to write on all of them, but expensive to run. In D1, a missing index turns into many rows read. In Firestore, every returned document is a read. In Cosmos DB, cross-partition queries cost more RUs.

## 254: How do you translate a DynamoDB partition key into Cosmos DB?

- DynamoDB's partition key becomes the Cosmos DB container's partition key path (for example `/customerId`). Cosmos DB also supports hierarchical partition keys (up to three levels, like `/tenantId`, `/userId`, `/sessionId`).
- DynamoDB's sort key has no direct match. Store it as a normal property and query with `ORDER BY` inside the partition. The `id` must be unique within a partition.
- A single-table DynamoDB design (many entity types in one table) can stay as one Cosmos container with a `type` field, which is a common Cosmos pattern too.

```ts
await orders.items.create({
  id: "o-1001",
  customerId: "c1", // partition key
  type: "order",
  createdAt: "2026-11-24T10:00:00Z",
  total: 120,
});
```

Each logical partition in Cosmos DB is limited to 20 GB, so a partition key with few values (like `country`) is a bad choice there too.

## 255: How do secondary indexes translate?

- **DynamoDB:** global secondary indexes (GSIs) and local secondary indexes (LSIs) that you define explicitly.
- **Cosmos DB:** every property is indexed by default. You tune the indexing policy (exclude paths, add composite indexes for `ORDER BY` on several fields).
- **Firestore:** single-field indexes are automatic. Queries with several filters or sorts need composite indexes, defined in `firestore.indexes.json` or created from the error link.
- **D1:** regular SQL `CREATE INDEX`.

```sql
-- D1
CREATE INDEX idx_orders_customer_created ON orders (customer_id, created_at);
```

## 256: How do you translate conditional writes and optimistic locking?

**AWS**

```ts
await db.send(
  new UpdateCommand({
    TableName: "accounts",
    Key: { id: "a1" },
    UpdateExpression: "SET balance = :b, version = :next",
    ConditionExpression: "version = :v",
    ExpressionAttributeValues: { ":b": 50, ":v": 3, ":next": 4 },
  }),
);
```

**Azure**

```ts
const { resource, etag } = await accounts.item("a1", "a1").read();
await accounts
  .item("a1", "a1")
  .replace(
    { ...resource, balance: 50 },
    { accessCondition: { type: "IfMatch", condition: etag! } },
  );
```

**GCP**

```ts
await db.runTransaction(async (tx) => {
  const ref = db.collection("accounts").doc("a1");
  const snap = await tx.get(ref);
  tx.update(ref, { balance: (snap.get("balance") as number) - 10 });
});
```

**Cloudflare**

```ts
const { meta } = await env.DB.prepare(
  "UPDATE accounts SET balance = ?, version = version + 1 WHERE id = ? AND version = ?",
)
  .bind(50, "a1", 3)
  .run();
if (meta.changes === 0) throw new Error("Conflict, retry");
```

A failed condition throws `ConditionalCheckFailedException` on DynamoDB and a 412 error on Cosmos DB. Firestore transactions retry automatically on contention.

## 257: How do you implement an atomic counter?

**AWS**

```ts
await db.send(
  new UpdateCommand({
    TableName: "stats",
    Key: { id: "views" },
    UpdateExpression: "ADD #c :one",
    ExpressionAttributeNames: { "#c": "count" },
    ExpressionAttributeValues: { ":one": 1 },
  }),
);
```

**Azure**

```ts
await stats
  .item("views", "views")
  .patch([{ op: "incr", path: "/count", value: 1 }]);
```

**GCP**

```ts
import { FieldValue } from "@google-cloud/firestore";

await db
  .collection("stats")
  .doc("views")
  .update({ count: FieldValue.increment(1) });
```

**Cloudflare**

```ts
import { DurableObject } from "cloudflare:workers";

export class Counter extends DurableObject {
  async increment() {
    const next = ((await this.ctx.storage.get<number>("count")) ?? 0) + 1;
    await this.ctx.storage.put("count", next);
    return next;
  }
}
```

Workers KV is not safe for counters, because it is eventually consistent and has no atomic increment. A Durable Object handles one request at a time per id, so its increment is safe. A D1 `UPDATE ... SET count = count + 1` also works.

## 258: How do batch writes compare?

| Service   | Batch API                               | Limit                                                  | Atomic?                       |
| --------- | --------------------------------------- | ------------------------------------------------------ | ----------------------------- |
| DynamoDB  | `BatchWriteItem` / `TransactWriteItems` | 25 items / 100 items                                   | Batch no, transaction yes     |
| Cosmos DB | Bulk operations / transactional batch   | Transactional batch: 100 operations, one partition key | Batch yes                     |
| Firestore | `WriteBatch` / transactions             | 500 writes                                             | Yes                           |
| D1        | `env.DB.batch([...])`                   | Statement and size limits                              | Yes (runs as one transaction) |

**Cloudflare**

```ts
await env.DB.batch([
  env.DB.prepare("INSERT INTO orders (id, total) VALUES (?, ?)").bind(
    "o1",
    120,
  ),
  env.DB.prepare(
    "UPDATE customers SET order_count = order_count + 1 WHERE id = ?",
  ).bind("c1"),
]);
```

## 259: How do you translate a cache-aside pattern with Redis?

**AWS**

```ts
import { createClient } from "redis";

const redis = createClient({ url: `rediss://${process.env.CACHE_HOST}:6379` });
await redis.connect();

async function getUser(id: string) {
  const hit = await redis.get(`user:${id}`);
  if (hit) return JSON.parse(hit);
  const user = await loadUserFromDb(id);
  await redis.set(`user:${id}`, JSON.stringify(user), { EX: 300 });
  return user;
}
```

**Azure**

The same code works with Azure Managed Redis on port 10000, using the access key or, better, Entra ID authentication with the `@redis/entraid` credentials provider.

**GCP**

The same code works with Memorystore for Valkey or Redis. Memorystore is reached over a private IP in your VPC, so serverless code needs Direct VPC egress.

**Cloudflare**

```ts
async function getUser(id: string, env: Env) {
  const hit = await env.CACHE.get<User>(`user:${id}`, "json");
  if (hit) return hit;
  const user = await loadUserFromDb(id, env);
  await env.CACHE.put(`user:${id}`, JSON.stringify(user), {
    expirationTtl: 300,
  });
  return user;
}
```

KV is a good cache for data read far more than written. Writes to the same key are limited to about one per second, and a new value can take up to about a minute to show everywhere.

## 260: How do you cache API responses at the edge?

- **AWS:** a CloudFront cache behavior for `/api/*` with a cache policy keyed on the headers and query strings that matter.
- **Azure:** Front Door caching on the API route with query string caching behavior.
- **GCP:** Cloud CDN with `USE_ORIGIN_HEADERS` and `Cache-Control: public, max-age=60` from the backend.
- **Cloudflare:** a Cache Rule for the API path, or the Cache API inside a Worker.

**Cloudflare**

```ts
export default {
  async fetch(request: Request, env: Env, ctx: ExecutionContext) {
    const cache = caches.default;
    const cached = await cache.match(request);
    if (cached) return cached;
    const response = Response.json(await loadProducts(env), {
      headers: { "cache-control": "public, max-age=60" },
    });
    ctx.waitUntil(cache.put(request, response.clone()));
    return response;
  },
};
```

The Workers Cache API stores data in the local Cloudflare data center only, not globally. Never cache responses that depend on the user's cookies or `Authorization` header unless they are part of the cache key.

## 261: Where do you store user sessions on each platform?

- **AWS:** DynamoDB with TTL, or ElastiCache.
- **Azure:** Azure Managed Redis or Cosmos DB with TTL.
- **GCP:** Memorystore or Firestore with a TTL policy.
- **Cloudflare:** Workers KV for read-heavy sessions, or a Durable Object per session when you need strong consistency.

Stateless JWT sessions avoid the store entirely, but then you need a short expiry and a way to revoke tokens, which brings a small store back.

## 262: How much local disk does serverless code get?

- **AWS Lambda:** `/tmp`, configurable from 512 MB to 10 GB, kept between warm invocations of the same instance.
- **Azure Functions:** a local temp folder on the instance. Size depends on the plan, and it is not shared or persistent.
- **Cloud Run functions:** an in-memory file system, so files you write count against the memory limit. You can mount Cloud Storage or Filestore volumes.
- **Cloudflare Workers:** no real disk. With `nodejs_compat`, `node:fs` offers a small in-memory `/tmp` that lasts only for the request. Use R2 for files.

## 263: How do you mount shared storage into serverless containers?

- **AWS:** EFS access points mounted into Lambda or ECS tasks.
- **Azure:** Azure Files shares mounted as volumes in Container Apps or App Service.
- **GCP:** Cloud Storage FUSE volumes or NFS (Filestore) volumes in Cloud Run services and jobs.

**GCP**

```bash
gcloud run deploy api --image "$IMAGE" --region us-central1 \
  --add-volume name=files,type=cloud-storage,bucket=my-bucket \
  --add-volume-mount volume=files,mount-path=/mnt/files
```

Cloudflare has no volume mounts. Containers have local disk that is lost when the instance stops, so persistent data goes to R2, D1 or Durable Object storage.

## 264: How do you resize images on the fly?

- **AWS:** the Dynamic Image Transformation for Amazon CloudFront solution (Lambda + Sharp behind CloudFront), or your own Lambda.
- **Azure:** a Function or Container App using Sharp behind Front Door.
- **GCP:** a Cloud Run service using Sharp behind Cloud CDN.
- **Cloudflare:** Cloudflare Images transformations, by URL or from a Worker.

**Cloudflare**

```html
<img src="/cdn-cgi/image/width=400,format=auto,quality=80/uploads/photo.jpg" />
```

```ts
return fetch(imageUrl, {
  cf: { image: { width: 400, format: "avif", fit: "cover" } },
});
```

On the three big clouds you build and run the resize service yourself, and the CDN caches each size. On Cloudflare, it is a built-in feature billed per unique transformation.

## 265: How do you give users time-limited access to private CDN content?

- **AWS:** CloudFront signed URLs or signed cookies with a key group.
- **GCP:** Cloud CDN signed URLs and signed cookies with a signing key on the backend.
- **Cloudflare:** a Worker that checks an HMAC token in the URL or cookie before serving from R2, or Cloudflare Access for logged-in users.

Azure Front Door has no token authentication feature, so the usual pattern is SAS URLs straight to Blob Storage, or a check in the origin app.

## 266: How do you block or allow traffic by country?

- **AWS:** CloudFront geographic restrictions, or an AWS WAF geo match rule.
- **Azure:** a Front Door WAF custom rule with `GeoMatch` on `RemoteAddr`.
- **GCP:** a Cloud Armor rule with `origin.region_code == 'XX'`.
- **Cloudflare:** a WAF custom rule with `ip.src.country`.

**GCP**

```bash
gcloud compute security-policies rules create 1000 --security-policy edge-policy \
  --expression "origin.region_code == 'RU'" --action deny-403
```

**Cloudflare**

```text
(ip.src.country in {"RU" "KP"})
```

## 267: How do you get the client's country or real IP in code?

- **AWS:** CloudFront adds `CloudFront-Viewer-Country` (when configured in the origin request policy) and `X-Forwarded-For`. Lambda function URLs give `event.requestContext.http.sourceIp`.
- **Azure:** Front Door sends `X-Azure-ClientIP`, `X-Forwarded-For` and, with a rule set, custom headers. Geo needs a lookup or a rules engine variable.
- **GCP:** the load balancer can add custom request headers such as `X-Client-Region: {client_region}` and sends `X-Forwarded-For`.
- **Cloudflare:** `CF-Connecting-IP` and `CF-IPCountry` headers, and in Workers `request.cf.country`, `request.cf.city` and more.

**Cloudflare**

```ts
const country = request.cf?.country ?? "unknown";
const ip = request.headers.get("cf-connecting-ip");
```

## 268: How do you make sure the origin only accepts traffic from the CDN?

- **AWS:** allow the CloudFront managed prefix list in the ALB security group, and check a secret custom header. For S3, use Origin Access Control. Newer setups use CloudFront VPC origins for private ALBs.
- **Azure:** allow the `AzureFrontDoor.Backend` service tag and check the `X-Azure-FDID` header equals your Front Door ID, or use Private Link origins.
- **GCP:** keep backends internal (no external IP) behind the load balancer, and allow only the Google front-end ranges in firewall rules.
- **Cloudflare:** use Cloudflare Tunnel so the origin has no open inbound ports, or Authenticated Origin Pulls (mTLS from Cloudflare to the origin).

## 269: How do you deploy a static site from CI?

**AWS**

```bash
aws s3 sync ./dist s3://my-site --delete
aws cloudfront create-invalidation --distribution-id E123EXAMPLE --paths "/index.html"
```

**Azure**

```bash
npx @azure/static-web-apps-cli deploy ./dist --deployment-token "$SWA_TOKEN" --env production
```

**GCP**

```bash
npx firebase-tools deploy --only hosting --project my-project
```

**Cloudflare**

```bash
npx wrangler deploy
```

## 270: How do you add security headers to every response?

- **AWS:** a CloudFront response headers policy (managed `SecurityHeadersPolicy` or custom).
- **Azure:** a Front Door rule set with "Modify response header" actions.
- **GCP:** custom response headers on the backend service or backend bucket (`--custom-response-header`).
- **Cloudflare:** Response Header Transform Rules, managed transforms ("Add security headers"), or a Worker.

**GCP**

```bash
gcloud compute backend-buckets update site-bucket \
  --custom-response-header="Strict-Transport-Security: max-age=31536000; includeSubDomains" \
  --custom-response-header="X-Content-Type-Options: nosniff"
```

## 271: How do you translate feature flags from AWS AppConfig?

- **AWS:** AppConfig feature flags with the AppConfig Agent Lambda extension for cached reads.
- **Azure:** App Configuration feature flags with `@microsoft/feature-management` and the App Configuration provider.
- **GCP:** Firebase Remote Config (server-side templates for backends), or a third-party flag service.
- **Cloudflare:** flags stored in Workers KV and read per request, or a third-party service through its OpenFeature provider.

OpenFeature is a vendor-neutral standard API with providers for many flag services, which makes flag code portable across clouds.

## 272: How do services call each other privately?

- **AWS:** Lambda `Invoke` with IAM, or private API Gateway, or ECS Service Connect.
- **Azure:** Container Apps internal ingress (apps in the same environment call `http://<app-name>`), or Functions with Entra authentication.
- **GCP:** Cloud Run service-to-service calls with Google-signed ID tokens and `roles/run.invoker`.
- **Cloudflare:** service bindings, which call another Worker directly with no network hop or public URL, including typed RPC methods.

**Cloudflare**

```ts
// users-service
import { WorkerEntrypoint } from "cloudflare:workers";

export default class Users extends WorkerEntrypoint<Env> {
  async getUser(id: string) {
    return this.env.DB.prepare("SELECT * FROM users WHERE id = ?")
      .bind(id)
      .first();
  }
}

// api worker, with "services": [{ "binding": "USERS", "service": "users-service" }]
const user = await env.USERS.getUser("u1");
```

## 273: How do you call a private Cloud Run service from another service?

```ts
import { GoogleAuth } from "google-auth-library";

const target = "https://orders-abc123-uc.a.run.app";
const client = await new GoogleAuth().getIdTokenClient(target);
const res = await client.request({ url: `${target}/orders/o1` });
```

The calling service's service account needs `roles/run.invoker` on the target. The AWS equivalent is signing requests with SigV4 for an IAM-authorized Lambda function URL or API Gateway route. On Azure, the caller requests an Entra token for the target app's application ID URI with its managed identity and sends it as a bearer token.

## 274: How do you make a service reachable only internally?

- **AWS:** a private API Gateway endpoint, an internal ALB, or a Lambda function URL with `AWS_IAM` auth.
- **Azure:** Container Apps with internal ingress, or a Function app with private endpoints and public access disabled.
- **GCP:** Cloud Run `--ingress internal` (or `internal-and-cloud-load-balancing`), plus IAM `--no-allow-unauthenticated`.
- **Cloudflare:** a Worker with `"workers_dev": false` and no routes, called only through service bindings.

**GCP**

```bash
gcloud run services update orders --region us-central1 --ingress internal
```

## 275: What happened to AWS App Mesh, and what replaces a service mesh on each cloud?

AWS App Mesh reached end of support in September 2026. AWS recommends ECS Service Connect for ECS and VPC Lattice or Istio for EKS.

- **AWS:** ECS Service Connect, Amazon VPC Lattice, or Istio on EKS.
- **Azure:** the Istio-based service mesh add-on for AKS.
- **GCP:** Cloud Service Mesh (managed Istio) for GKE and Cloud Run.

Since Istio exists on all three, it is the most portable mesh choice for Kubernetes workloads.

## 276: How do the build config files compare?

**AWS**

```yaml
# buildspec.yml (CodeBuild)
version: 0.2
phases:
  install: { runtime-versions: { nodejs: 22 } }
  build:
    commands:
      - npm ci
      - npm test
      - npm run build
artifacts:
  files: ["dist/**/*"]
```

**Azure**

```yaml
# azure-pipelines.yml
trigger: [main]
pool: { vmImage: ubuntu-latest }
steps:
  - task: NodeTool@0
    inputs: { versionSpec: "22.x" }
  - script: npm ci && npm test && npm run build
```

**GCP**

```yaml
# cloudbuild.yaml
steps:
  - name: node:22
    entrypoint: bash
    args: ["-c", "npm ci && npm test && npm run build"]
  - name: gcr.io/cloud-builders/docker
    args:
      [
        "build",
        "-t",
        "us-central1-docker.pkg.dev/$PROJECT_ID/repo/api:$SHORT_SHA",
        ".",
      ]
images: ["us-central1-docker.pkg.dev/$PROJECT_ID/repo/api:$SHORT_SHA"]
```

Cloudflare Workers Builds has no build file. You set the build command (for example `npm run build`) and deploy command (`npx wrangler deploy`) in the dashboard, and it runs on every push.

## 277: How do you preview infrastructure changes before applying them?

- **AWS:** CloudFormation change sets, or `cdk diff`.
- **Azure:** `az deployment group what-if --template-file main.bicep`.
- **GCP:** Infrastructure Manager previews (`gcloud infra-manager previews create`), or `terraform plan`.
- **Cloudflare:** `wrangler deploy --dry-run` for Workers, or `terraform plan` for zone settings.

Running `terraform plan` in pull requests works on every provider, which is one reason teams standardize on Terraform during a migration.

## 278: How do you block public buckets across the organization?

- **AWS:** S3 Block Public Access at the account level, enforced with an SCP so nobody can turn it off.
- **Azure:** Azure Policy "Storage account public access should be disallowed" with a `deny` effect at the management group.
- **GCP:** the organization policy constraint `storage.publicAccessPrevention`.
- **Cloudflare:** R2 buckets are private by default. Public access needs an explicit custom domain or the `r2.dev` URL, which you can restrict with member roles.

**GCP**

```bash
gcloud resource-manager org-policies enable-enforce \
  constraints/storage.publicAccessPrevention --organization=123456789
```

## 279: How do you restrict which regions can be used?

- **AWS:** an SCP that denies actions when `aws:RequestedRegion` is not in an allowed list (with exceptions for global services).
- **Azure:** the built-in Azure Policy "Allowed locations".
- **GCP:** the organization policy `gcp.resourceLocations`, using value groups like `in:eu-locations`.
- **Cloudflare:** jurisdictions for R2 and Durable Objects (for example `eu`), and the Data Localization Suite for keeping traffic processing in a region.

## 280: How do you split cloud costs by team?

- **AWS:** cost allocation tags activated in Billing, plus Cost Categories.
- **Azure:** tags on resources or resource groups, cost allocation rules, and separate subscriptions per team.
- **GCP:** labels on resources, separate projects per team, and the BigQuery billing export to group by label or project.
- **Cloudflare:** separate accounts per team or product, because usage is billed per account.

## 281: How do commitment discounts compare?

- **AWS:** Savings Plans (Compute, EC2 Instance, SageMaker) and Reserved Instances for RDS, ElastiCache, OpenSearch and Redshift.
- **Azure:** Azure savings plan for compute and Azure Reservations (VMs, SQL, Cosmos DB, storage).
- **GCP:** committed use discounts (resource-based and spend-based), plus automatic sustained use discounts on some VM types.
- **Cloudflare:** monthly plans (Free, Pro, Business, Enterprise) and Workers Paid. Large customers sign Enterprise contracts with committed usage.

GCP's sustained use discounts apply automatically without any commitment, which has no direct match on AWS.

## 282: How do you handle spot VM interruptions in code?

**AWS**

```bash
TOKEN=$(curl -s -X PUT http://169.254.169.254/latest/api/token -H "X-aws-ec2-metadata-token-ttl-seconds: 60")
curl -s -H "X-aws-ec2-metadata-token: $TOKEN" http://169.254.169.254/latest/meta-data/spot/instance-action
```

**Azure**

```bash
curl -s -H "Metadata: true" "http://169.254.169.254/metadata/scheduledevents?api-version=2020-07-01"
```

**GCP**

```bash
curl -s -H "Metadata-Flavor: Google" \
  "http://metadata.google.internal/computeMetadata/v1/instance/preempted?wait_for_change=true"
```

Poll (or wait on) these endpoints, then drain work and checkpoint. The notice is about two minutes on AWS and about 30 seconds on Azure and GCP, so the drain must be fast.

## 283: How do you implement idempotency keys on each platform?

- **AWS:** Powertools for AWS Lambda's idempotency utility with a DynamoDB table, or a conditional `PutItem` with `attribute_not_exists(pk)`.
- **Azure:** `items.create()` in Cosmos DB with the idempotency key as `id`, which fails with 409 if it exists.
- **GCP:** Firestore `doc(key).create()`, which fails if the document already exists.
- **Cloudflare:** a D1 table with a unique key, or a Durable Object per key that stores the first result.

**GCP**

```ts
try {
  await db
    .collection("idempotency")
    .doc(key)
    .create({ status: "processing", at: Date.now() });
} catch (err: any) {
  if (err.code === 6) return getStoredResult(key); // ALREADY_EXISTS
  throw err;
}
```

**Cloudflare**

```ts
const { meta } = await env.DB.prepare(
  "INSERT OR IGNORE INTO idempotency (key, created_at) VALUES (?, ?)",
)
  .bind(key, Date.now())
  .run();
if (meta.changes === 0) return getStoredResult(key, env);
```

## 284: How do you send a message with a delay?

**AWS**

```ts
await sqs.send(
  new SendMessageCommand({ QueueUrl, MessageBody: body, DelaySeconds: 300 }),
);
```

**Azure**

```ts
await sender.scheduleMessages({ body }, new Date(Date.now() + 5 * 60 * 1000));
```

**GCP**

```ts
import { CloudTasksClient } from "@google-cloud/tasks";

const tasks = new CloudTasksClient();
await tasks.createTask({
  parent: tasks.queuePath("my-project", "us-central1", "emails"),
  task: {
    scheduleTime: { seconds: Math.floor(Date.now() / 1000) + 300 },
    httpRequest: {
      httpMethod: "POST",
      url: "https://send-email-abc123-uc.a.run.app",
      body: Buffer.from(body).toString("base64"),
      oidcToken: {
        serviceAccountEmail: "tasks@my-project.iam.gserviceaccount.com",
      },
    },
  },
});
```

**Cloudflare**

```ts
await env.EMAILS.send(body, { delaySeconds: 300 });
```

SQS delays are limited to 15 minutes. Service Bus scheduled messages and Cloud Tasks can go much further out. Cloudflare Queues allow delays of up to 12 hours. For longer waits on Cloudflare, use a Workflow with `step.sleep` or a Durable Object alarm.

## 285: How do you monitor queue backlog?

| Provider          | Metric                                                                             |
| ----------------- | ---------------------------------------------------------------------------------- |
| SQS               | `ApproximateNumberOfMessagesVisible`, `ApproximateAgeOfOldestMessage`              |
| Service Bus       | `ActiveMessages`, `DeadletteredMessages`                                           |
| Pub/Sub           | `subscription/num_undelivered_messages`, `subscription/oldest_unacked_message_age` |
| Cloudflare Queues | Backlog messages and bytes in the dashboard and GraphQL Analytics API              |

Alert on the age of the oldest message, not only on the count. A small backlog that never moves means a stuck consumer.

## 286: How do you set log retention?

**AWS**

```bash
aws logs put-retention-policy --log-group-name /aws/lambda/api --retention-in-days 30
```

**Azure**

```bash
az monitor log-analytics workspace update --resource-group my-rg \
  --workspace-name app-logs --retention-time 30
```

**GCP**

```bash
gcloud logging buckets update _Default --location=global --retention-days=30
```

CloudWatch log groups keep logs forever by default, which is a common source of slowly growing bills. Workers Logs keeps logs for a fixed number of days based on your plan, so use Logpush for longer retention.

## 287: How do you export logs to storage or a SIEM?

- **AWS:** CloudWatch Logs subscription filters to Amazon Data Firehose, Lambda or Kinesis, or log group exports to S3.
- **Azure:** diagnostic settings that send logs to a storage account, Event Hubs or Log Analytics, and Microsoft Sentinel on top.
- **GCP:** log sinks to Cloud Storage, BigQuery, Pub/Sub or another project's log bucket.
- **Cloudflare:** Logpush jobs to R2, S3, Azure Blob, GCS, Datadog, Splunk and other destinations.

**GCP**

```bash
gcloud logging sinks create errors-to-bq \
  bigquery.googleapis.com/projects/my-project/datasets/logs \
  --log-filter='severity>=ERROR'
```

## 288: How do you record custom business metrics?

**AWS**

```ts
// Embedded Metric Format: CloudWatch extracts the metric from the log line
console.log(
  JSON.stringify({
    _aws: {
      Timestamp: Date.now(),
      CloudWatchMetrics: [
        {
          Namespace: "Shop",
          Dimensions: [["Country"]],
          Metrics: [{ Name: "Orders", Unit: "Count" }],
        },
      ],
    },
    Country: "US",
    Orders: 1,
  }),
);
```

**Azure**

```ts
import { metrics } from "@opentelemetry/api";

const orders = metrics.getMeter("shop").createCounter("orders");
orders.add(1, { country: "US" }); // exported by the Azure Monitor OpenTelemetry Distro
```

**GCP**

```ts
import { metrics } from "@opentelemetry/api";

metrics.getMeter("shop").createCounter("orders").add(1, { country: "US" });
// exported with the OTLP exporter to Cloud Monitoring
```

**Cloudflare**

```ts
env.SHOP_METRICS.writeDataPoint({
  blobs: ["US"],
  doubles: [1],
  indexes: ["orders"],
});
```

Workers Analytics Engine stores data points that you query with SQL through its API, or visualize in Grafana.

## 289: How do you turn log lines into metrics?

- **AWS:** CloudWatch Logs metric filters.
- **Azure:** log search alert rules on a KQL query, or summarizing logs in workbooks.
- **GCP:** log-based metrics (counter or distribution).

**GCP**

```bash
gcloud logging metrics create payment_failures \
  --description="Failed payments" \
  --log-filter='resource.type="cloud_run_revision" AND jsonPayload.message="payment failed"'
```

On Cloudflare, write a data point to Analytics Engine where the event happens, instead of deriving metrics from logs.

## 290: How do you host a Next.js app on each platform?

- **AWS:** AWS Amplify Hosting (native support for SSR), or OpenNext with Lambda and CloudFront.
- **Azure:** App Service or Container Apps running `next start` in a container. Static Web Apps has hybrid Next.js support in preview.
- **GCP:** Firebase App Hosting, or Cloud Run with a standalone output build.
- **Cloudflare:** the OpenNext Cloudflare adapter (`@opennextjs/cloudflare`), which builds the app into a Worker with static assets.

**GCP**

```bash
# next.config.js: output: "standalone"
gcloud run deploy web --source . --region us-central1 --allow-unauthenticated
```

**Cloudflare**

```bash
npm install -D @opennextjs/cloudflare
npx opennextjs-cloudflare build
npx opennextjs-cloudflare deploy
```

## 291: How do you schedule a job in a specific time zone?

- **AWS:** EventBridge Scheduler supports `--schedule-expression-timezone "Europe/Berlin"`.
- **Azure:** timer triggers use UTC by default. Set the `WEBSITE_TIME_ZONE` app setting on supported plans, or write the schedule in UTC.
- **GCP:** Cloud Scheduler supports `--time-zone="Europe/Berlin"`.
- **Cloudflare:** Cron Triggers always run in UTC, so convert the schedule yourself.

Time zones with daylight saving time move by an hour twice a year in UTC terms. If the job must run at 9:00 local time all year, use a scheduler with time zone support, or schedule hourly and check the local time in code.

## 292: How do readiness and liveness checks translate for containers?

- **AWS ECS:** container `healthCheck` in the task definition, plus target group health checks on the ALB.
- **Azure Container Apps:** `liveness`, `readiness` and `startup` probes on the container (HTTP or TCP).
- **GCP Cloud Run:** startup and liveness probes (HTTP, TCP or gRPC). There is no readiness probe; Cloud Run only sends traffic after the startup probe passes.
- **Cloudflare Containers:** the Worker's `Container` class waits for the port to be ready, and you add your own health check route if needed.

## 293: How do you shut down gracefully?

- **AWS ECS:** the task gets `SIGTERM`, then `SIGKILL` after `stopTimeout` (default 30 seconds).
- **Azure Container Apps:** `SIGTERM`, then kill after `terminationGracePeriodSeconds` (default 30 seconds).
- **GCP Cloud Run:** `SIGTERM`, then `SIGKILL` 10 seconds later.
- **Cloudflare Workers:** no process to stop. Use `ctx.waitUntil()` to finish background work (like logging or cache writes) after the response is sent.

```ts
process.on("SIGTERM", async () => {
  await server.close();
  await db.end();
  process.exit(0);
});
```

## 294: How do you run background work after sending the response?

- **AWS Lambda:** the instance is frozen after the handler returns, so background promises may never finish. Finish before returning, use response streaming, or send the work to SQS.
- **Azure Functions:** same idea. Await the work, or put it on a queue.
- **Cloud Run:** with request-based billing, CPU is throttled after the response. Use instance-based billing (`--no-cpu-throttling`) if you do background work, or Cloud Tasks.
- **Cloudflare Workers:** `ctx.waitUntil(promise)` keeps the Worker alive after the response is sent, up to a time limit.

**Cloudflare**

```ts
export default {
  async fetch(request: Request, env: Env, ctx: ExecutionContext) {
    ctx.waitUntil(env.ANALYTICS.send({ path: new URL(request.url).pathname }));
    return new Response("ok");
  },
};
```

## 295: How do you translate API Gateway request validation?

- **AWS:** API Gateway REST API request validators with JSON Schema models.
- **Azure:** API Management `validate-content` policy against the API's schema.
- **GCP:** Apigee OASValidation policy (API Gateway does not validate bodies).
- **Cloudflare:** API Shield schema validation (upload an OpenAPI schema), or Zod validation in the Worker.

**Cloudflare**

```ts
import { z } from "zod";

const Order = z.object({
  productId: z.string(),
  quantity: z.number().int().positive(),
});

const parsed = Order.safeParse(await request.json());
if (!parsed.success)
  return Response.json(parsed.error.flatten(), { status: 400 });
```

## 296: How do you translate API keys and usage plans?

- **AWS:** API Gateway API keys attached to usage plans with throttling and quotas.
- **Azure:** API Management subscriptions (subscription keys) attached to products with rate limit and quota policies.
- **GCP:** API keys restricted to an API in API Gateway, or Apigee API products and developer apps.
- **Cloudflare:** no built-in API key product. Store hashed keys in KV or D1, check them in a Worker, and use the Rate Limiting binding with the key as the limit key.

## 297: How do you expose an OpenAPI-defined API?

**AWS**

```bash
aws apigatewayv2 import-api --body file://openapi.yaml
```

**Azure**

```bash
az apim api import --resource-group my-rg --service-name my-apim \
  --path orders --specification-format OpenApi --specification-path openapi.yaml
```

**GCP**

```bash
gcloud api-gateway api-configs create orders-v1 --api=orders \
  --openapi-spec=openapi.yaml --backend-auth-service-account=gw@my-project.iam.gserviceaccount.com
gcloud api-gateway gateways create orders-gw --api=orders --api-config=orders-v1 --location=us-central1
```

On Cloudflare, you upload the OpenAPI file to API Shield for schema validation and endpoint discovery, and implement routes in a Worker (libraries like `chanfana` generate OpenAPI docs from Hono routes).

## 298: How do you translate a Lambda function that runs on a Kinesis or SQS batch with a batch window?

- **AWS:** event source mapping with `BatchSize` and `MaximumBatchingWindowInSeconds`.
- **Azure:** Event Hubs trigger with `cardinality: "many"` and `maxEventBatchSize`, or Service Bus trigger with `isSessionsEnabled` and batch settings in `host.json`.
- **GCP:** Pub/Sub push subscriptions deliver one message per request. For batches, use a pull subscriber on Cloud Run with flow control, or BigQuery subscriptions.
- **Cloudflare:** Queues consumer settings `max_batch_size` and `max_batch_timeout`.

**Cloudflare**

```jsonc
{
  "queues": {
    "consumers": [
      { "queue": "clicks", "max_batch_size": 100, "max_batch_timeout": 5 },
    ],
  },
}
```

## 299: How do you translate DynamoDB Accelerator (DAX)?

- **AWS:** DAX, an in-memory write-through cache for DynamoDB with the same API.
- **Azure:** the Cosmos DB integrated cache, used through a dedicated gateway.
- **GCP:** no built-in Firestore cache. Firestore client SDKs cache locally, and servers use Memorystore with cache-aside.
- **Cloudflare:** D1 read replicas, KV in front of D1, or Hyperdrive's query cache for external databases.

## 300: How do you translate an image thumbnail pipeline end to end?

| Step         | AWS              | Azure                  | GCP                            | Cloudflare                              |
| ------------ | ---------------- | ---------------------- | ------------------------------ | --------------------------------------- |
| Upload URL   | S3 presigned URL | User delegation SAS    | Signed URL (v4)                | R2 presigned URL                        |
| Storage      | S3 bucket        | Blob container         | Cloud Storage bucket           | R2 bucket                               |
| Upload event | S3 event -> SQS  | Event Grid -> Function | Eventarc -> Cloud Run function | R2 event notification -> Queue          |
| Resize       | Lambda + Sharp   | Function + Sharp       | Cloud Run function + Sharp     | Images transformations (no resize code) |
| Metadata     | DynamoDB         | Cosmos DB              | Firestore                      | D1                                      |
| Delivery     | CloudFront       | Front Door             | Cloud CDN                      | R2 custom domain + cache                |

Good things to mention in an interview: put a queue between the upload event and the resizer so failures retry, write thumbnails to a different prefix or bucket so the resizer does not trigger itself, and make the resize idempotent so duplicate events do no harm.

# Advanced Questions (301-450)

## 301: How do you plan a full migration from AWS to Azure or GCP?

1. **Discover:** export an inventory of every account, region and resource (AWS Config, Resource Explorer, the Cost and Usage Report). Azure Migrate and Google Migration Center can also scan AWS.
2. **Map:** for each service, pick the target equivalent and note the gaps (features, limits, pricing model).
3. **Build the foundation first:** landing zone (management groups or folders), identity (Entra ID or Cloud Identity), networking, logging, policies and CI/CD access.
4. **Pick waves:** start with stateless, low-risk apps, then data stores, then core systems.
5. **Move data:** bulk copy, then continuous replication (DMS, Storage Transfer Service, AzCopy sync), then a short cut-over window.
6. **Cut over with DNS:** lower TTLs days before, switch, and keep AWS ready to switch back.
7. **Decommission:** remove AWS resources only after a stable period, and keep backups.

The most common failure is starting with apps before the landing zone, identity and networking are ready on the target.

## 302: How do you decide what moves to Cloudflare and what moves to Azure or GCP?

Cloudflare is a good fit for:

- HTTP APIs and web apps that are mostly I/O (calling databases and other APIs), with short CPU time per request.
- Static sites, SSR front ends, edge logic, auth checks, redirects and A/B tests.
- Object storage with heavy egress (R2).
- Real-time coordination (Durable Objects), queues, cron jobs and durable workflows.
- DNS, CDN, WAF, DDoS protection and zero trust access, in front of any cloud.

Azure or GCP is the better fit for:

- VMs, Kubernetes, Windows workloads and anything with long-running processes.
- Large relational databases (Postgres, SQL Server) and data warehouses.
- Heavy CPU or memory work, ML training, and large batch jobs.
- Workloads that need VPC-level networking and private connectivity to on-premises.

Many real migrations use both: Cloudflare at the edge, and Azure or GCP for databases and heavy compute, with Hyperdrive or Tunnel between them.

## 303: How do rehost, replatform and refactor apply when leaving AWS?

- **Rehost (lift and shift):** EC2 VMs become Azure VMs or Compute Engine VMs with the same OS and app. Fast, but you keep the operational work. Tools: Azure Migrate, Migrate to Virtual Machines.
- **Replatform:** small changes for managed services. A container on ECS moves to Container Apps or Cloud Run. RDS Postgres moves to Azure Database for PostgreSQL or Cloud SQL. Code changes are minimal.
- **Refactor:** redesign for the target. Lambda + API Gateway + DynamoDB becomes Workers + D1 + Durable Objects, or Cosmos DB with change feed on Azure. Highest effort, highest long-term payoff.

A good migration plan labels each workload with one of these, instead of applying one approach to everything.

## 304: How do you find all AWS dependencies of an application before moving it?

- Read the IaC (CloudFormation, CDK, Terraform) and list every resource type.
- Search code for SDK clients (`@aws-sdk/client-*` imports) and ARNs or AWS hostnames in config.
- Check IAM role policies attached to the app. Every allowed action is a likely dependency.
- Look at CloudTrail and VPC Flow Logs for calls the code makes that are not in IaC (for example a hard-coded bucket in another account).
- Check DNS: CNAMEs to `*.amazonaws.com`, `*.cloudfront.net` and `*.elb.amazonaws.com`.
- Check hidden coupling: Cognito user pools, SES identities, KMS-encrypted data, and S3 presigned URLs embedded in other systems.

KMS-encrypted data is easy to miss. You must decrypt it on AWS before moving, because AWS KMS keys cannot be exported.

## 305: How do egress costs affect a migration?

Data leaving AWS to the internet is billed per GB, and moving hundreds of terabytes can cost a lot. Ways to reduce it:

- AWS waives data transfer out fees for customers fully leaving AWS (you request it through support, with conditions). Azure and GCP have similar programs for leaving their clouds.
- Use Cloudflare R2 Sippy to copy objects lazily, so only data that is actually read gets transferred.
- Compress data and move only what you need (drop old logs, expired backups).
- For very large volumes, use offline devices (AWS Snowball export to then load elsewhere) or a private interconnect through a colocation partner.

After the migration, check the new egress model: R2 has no egress fees, Azure and GCP charge for internet egress, and cross-region traffic is billed on all three big clouds.

## 306: What are the trade-offs of R2's zero egress pricing?

- **No egress fees:** reading data out to the internet or another cloud costs nothing beyond operation fees. That is why R2 is popular for public assets, model weights, datasets and backups served to many clients.
- **Operation fees still apply:** Class A operations (writes, lists) and Class B operations (reads) are billed per million. A workload with billions of tiny reads can still cost real money.
- **Fewer features:** no object versioning, fewer storage classes, no object-level ACLs, and a subset of the S3 API.
- **Location:** buckets live in a region (chosen by location hint or automatically), and the data is served through Cloudflare's cache, which helps hot objects but not cold random reads far from the bucket.

So R2 wins when egress dominates the bill, and S3, Blob or GCS still win when you need advanced storage features or tight integration with that cloud's compute.

## 307: How do object storage consistency models compare?

- **S3:** strong read-after-write consistency for all operations, including overwrites, deletes and list.
- **Azure Blob Storage:** strong consistency within the primary region. Geo-replicated secondaries (RA-GRS) are eventually consistent.
- **Cloud Storage:** strong consistency for object reads, writes, deletes and listing. Cached public objects may be stale until the cache expires.
- **R2:** strong consistency for reads and writes in the bucket. Data cached by the Cloudflare CDN in front of a custom domain follows normal cache rules.

So the old "S3 is eventually consistent" design workarounds are no longer needed on any of them. The CDN layer is where stale reads come from.

## 308: How do consistency guarantees differ between Workers KV, D1 and Durable Objects?

- **Workers KV:** eventually consistent. Writes appear in other locations usually within about 60 seconds. Best for read-heavy config, flags and caches.
- **D1:** one primary database with strong consistency for writes. With read replication on, reads from replicas can lag, and the Sessions API keeps a user's reads at least as new as their writes.
- **Durable Objects:** strongly consistent per object. Each object runs in one place and handles requests one at a time (input and output gates), so its storage behaves like a single-threaded program with transactions.

A typical translation from DynamoDB: strongly consistent per-entity state goes to Durable Objects, relational queries go to D1, and globally cached reads go to KV.

## 309: How do database consistency models compare across DynamoDB, Cosmos DB, Firestore and Spanner?

| Database  | Options                                                                                                                                        |
| --------- | ---------------------------------------------------------------------------------------------------------------------------------------------- |
| DynamoDB  | Eventually consistent reads (default) or strongly consistent reads per request; global tables with eventual or multi-region strong consistency |
| Cosmos DB | Five levels per account (can be relaxed per request): strong, bounded staleness, session (default), consistent prefix, eventual                |
| Firestore | Strong consistency for reads and queries                                                                                                       |
| Spanner   | External consistency (strict serializability), even across regions                                                                             |

Cosmos DB session consistency is the closest match to normal DynamoDB usage. It gives "read your own writes" within a client session at lower cost than strong.

## 310: How do you translate DynamoDB global tables?

- **AWS:** global tables replicate a table across regions with active-active writes, using eventual consistency and last-writer-wins, or multi-region strong consistency for some region sets.
- **Azure:** Cosmos DB with multiple write regions, conflict resolution policies (last writer wins on `_ts` or a custom path, or a custom stored procedure).
- **GCP:** Spanner multi-region instances (strongly consistent writes with a leader region), or Firestore multi-region locations (one database replicated across regions in one geography).
- **Cloudflare:** no multi-writer database. Durable Objects put each entity in one location close to where it is first used, and D1 read replicas spread reads globally.

The key interview point: active-active writes need a conflict strategy. Spanner avoids conflicts by being strongly consistent, at the cost of higher write latency across regions.

## 311: How do conflict resolution strategies differ in multi-region writes?

- **DynamoDB global tables:** last writer wins by timestamp, chosen by the service. Use conditional writes and single-region "home" ownership for items that must not conflict.
- **Cosmos DB:** last writer wins on a configurable numeric path, or a custom merge stored procedure, or manual resolution through the conflicts feed.
- **Spanner:** no conflicts. Transactions are serialized globally with TrueTime.
- **Durable Objects:** no conflicts. Each object has one location and one writer.

When you migrate from a multi-writer system to a single-writer one, latency for far-away writers goes up. When you migrate the other way, you must add conflict handling that the old system did for you.

## 312: How do you translate a DynamoDB single-table design?

1. List the access patterns from the DynamoDB design (for example "get orders for a customer, newest first").
2. On **Cosmos DB**, a single container with a `type` field and a partition key like `/customerId` keeps most patterns. Use hierarchical partition keys when one key gets too big.
3. On **Firestore**, model entities as collections and subcollections (`customers/{id}/orders/{orderId}`), and use collection group queries for cross-customer lookups.
4. On **D1**, go back to normal relational tables with foreign keys and indexes. Single-table design is a workaround for missing joins, and SQLite has joins.
5. On **Durable Objects**, one object per aggregate (for example per customer) with its own SQLite storage holding that customer's orders.

Do not copy the composite `PK`/`SK` string keys (`CUSTOMER#123`) into a relational database. They make queries and indexes harder there.

## 313: What causes hot partitions on each database and how do you avoid them?

- **DynamoDB:** each partition handles up to 3,000 RCU and 1,000 WCU. Adaptive capacity helps, but one very hot key is still throttled. Fix with write sharding (`key#0..N`).
- **Cosmos DB:** each physical partition handles up to 10,000 RU/s, and one logical partition key value lives on one physical partition. Fix with a higher-cardinality key or hierarchical keys.
- **Firestore:** sequential document IDs or timestamps in indexed fields create hotspots. Follow the "500/50/5" ramp-up rule for new traffic and use random IDs.
- **Durable Objects:** one object processes requests one at a time, so a single object handles roughly hundreds to about a thousand simple requests per second. Fix by sharding state across many objects.
- **D1:** one database has one primary for writes, so very write-heavy apps split data across several databases (for example per tenant).

## 314: What are Durable Objects, and what do they replace when coming from AWS?

A Durable Object is a class instance with a unique id that Cloudflare runs in exactly one place at a time, with its own private, strongly consistent storage (SQLite-backed). All requests for that id reach the same instance. It is the actor model as a managed service.

On AWS, the same job usually needs several services: Lambda for logic, DynamoDB with conditional writes for consistency, API Gateway WebSockets and a connection table for real-time, and EventBridge Scheduler or Step Functions for timers. A Durable Object does all of these in one class (storage, WebSockets, alarms).

The closest Azure match is Durable Entities in Durable Functions, or Microsoft Orleans grains on Container Apps. GCP has no managed actor service.

## 315: When should you not use Durable Objects?

- When you need queries across many entities, like "all orders over $100 this week". Each object's storage is private, so you would need to fan out. Use D1 or an external database.
- When one entity gets very high write traffic that cannot be split.
- When the data must be readable from many regions with low latency. An object lives in one location.
- When the team needs SQL analytics or BI tools to read the data directly.

A common design: Durable Objects for live coordination (rooms, counters, rate limits, sessions), and D1 or Postgres as the system of record for reporting.

## 316: How do you translate Aurora Global Database?

- **AWS:** Aurora Global Database, one primary region with up to several read-only secondary regions, typical lag under a second, and managed failover.
- **Azure:** Azure SQL active geo-replication or failover groups, and cross-region read replicas for Azure Database for PostgreSQL flexible server (with promote for failover).
- **GCP:** AlloyDB cross-region replication (secondary clusters), or Cloud SQL cross-region read replicas with promotion. Spanner for true multi-region writes.

Failover groups in Azure SQL give a stable listener endpoint that moves to the new primary, which is the closest match to Aurora's global writer endpoint.

## 317: How does distributed SQL compare across providers?

- **AWS Aurora DSQL:** serverless, PostgreSQL-compatible, active-active across regions, optimistic concurrency (transactions may need retry), with some Postgres features missing (for example foreign keys and some extensions).
- **GCP Spanner:** the oldest and most mature. GoogleSQL or a PostgreSQL interface, strong external consistency, interleaved tables, and multi-region configs.
- **Azure:** no direct match for multi-region active-active SQL. Cosmos DB covers multi-region writes for NoSQL, and Azure SQL Hyperscale covers large single-region SQL with read replicas.
- **Cloudflare:** D1 with read replication is single-primary, so it is not distributed SQL for writes.

Both DSQL and Spanner push you to design for retries and avoid hot rows, which is a bigger change than the SQL dialect.

## 318: How do multi-item transactions compare?

- **DynamoDB:** `TransactWriteItems` with up to 100 items across tables in one region, at double the write cost.
- **Cosmos DB:** transactional batch or stored procedures, only within one logical partition key.
- **Firestore:** transactions across any documents in the database (up to 500 writes), with optimistic concurrency on the server SDKs.
- **D1:** SQL transactions through `batch()`, within one database.
- **Durable Objects:** `ctx.storage.transaction()` or the SQL API, within one object.

The Cosmos DB rule is the biggest surprise when coming from DynamoDB: a transaction cannot span partition keys, so the data model must put things that change together in one partition.

## 319: How does permission evaluation differ between AWS IAM, Azure RBAC and GCP IAM?

- **AWS:** default deny. A request is allowed if an identity or resource policy allows it and nothing denies it. SCPs, RCPs, permission boundaries and session policies can only reduce permissions. Explicit deny always wins.
- **Azure:** RBAC is additive: the union of all role assignments at the scope and above. Deny assignments exist but are created only by Azure itself (for example by deployment stacks and managed apps), not written by you directly. Azure Policy blocks configurations, not identities.
- **GCP:** allow policies inherit down from organization to folder to project to resource and are additive. IAM deny policies are evaluated first and override allows. Principal access boundary policies limit which resources a principal can access.

So an AWS design that depends on explicit deny statements maps to GCP deny policies, but on Azure it usually becomes "don't grant it" plus Azure Policy guardrails.

## 320: How do you translate resource-based policies like S3 bucket policies?

- **AWS:** resource policies (bucket policies, KMS key policies, SQS queue policies) grant access to principals in other accounts and add conditions like `aws:SourceVpce`.
- **Azure:** no resource policies. Access is granted with role assignments scoped to the resource. Cross-tenant access uses guest users, multi-tenant apps or Lighthouse. Network conditions are firewall settings on the resource.
- **GCP:** IAM policies can be set directly on resources (bucket, topic, secret), so a bucket IAM policy is the natural match. Network conditions come from VPC Service Controls.

Pay special attention to KMS key policies: on AWS, a key policy can block even account admins, while Azure Key Vault and Cloud KMS rely on normal RBAC at the vault or key level.

## 321: How do you translate attribute-based access control (ABAC)?

**AWS**

```json
{
  "Effect": "Allow",
  "Action": "s3:GetObject",
  "Resource": "arn:aws:s3:::docs/*",
  "Condition": {
    "StringEquals": { "s3:ExistingObjectTag/team": "${aws:PrincipalTag/team}" }
  }
}
```

**Azure**

```text
(
 !(ActionMatches{'Microsoft.Storage/storageAccounts/blobServices/containers/blobs/read'})
 OR
 @Resource[Microsoft.Storage/storageAccounts/blobServices/containers/blobs/tags:team<$key_case_sensitive$>]
   StringEquals @Principal[Microsoft.Directory/CustomSecurityAttributes/Id:Engineering_team]
)
```

**GCP**

```bash
gcloud projects add-iam-policy-binding my-project \
  --member=group:team-a@example.com --role=roles/storage.objectViewer \
  --condition='expression=resource.name.startsWith("projects/_/buckets/docs/objects/team-a/"),title=team-a-only'
```

Azure ABAC conditions on role assignments work for blob storage and a few other services, using blob index tags and Entra custom security attributes. GCP IAM conditions use CEL on resource names, dates and tags.

## 322: How do you translate permission boundaries?

- **AWS:** a permission boundary on a role caps what any policy attached to it can grant. It is often used so developers can create roles but not escalate.
- **Azure:** no direct match. Use role assignment conditions that restrict which roles a user can assign (delegated role assignment management), plus Privileged Identity Management for just-in-time elevation.
- **GCP:** IAM deny policies and principal access boundary policies, plus organization policy constraints on who can grant roles to which domains (`iam.allowedPolicyMemberDomains`).

## 323: What tools help you reach least privilege on each cloud?

- **AWS:** IAM Access Analyzer (unused access findings, policy generation from CloudTrail activity), and last-accessed information.
- **Azure:** Entra access reviews, Privileged Identity Management (just-in-time roles), and Defender for Cloud recommendations about over-permissioned identities.
- **GCP:** IAM Recommender (role recommendations based on 90 days of usage) and Policy Analyzer.

After a migration, start with broader roles for a short period, then use these tools to shrink them based on real usage. Guessing exact permissions up front usually breaks things.

## 324: How do you set up break-glass access on each provider?

- **AWS:** a few IAM users or root credentials with hardware MFA, stored in a safe, used only when IAM Identity Center is down, and monitored with alerts on every use.
- **Azure:** two cloud-only Global Administrator accounts, excluded from Conditional Access policies that could lock them out, using FIDO2 keys, with sign-in alerts.
- **GCP:** a super admin account in Cloud Identity with security keys, not federated to the main IdP, with alerts.
- **Cloudflare:** a Super Administrator account that does not depend on SSO (or an SSO bypass for one account), with hardware 2FA.

The common rule: break-glass accounts must not depend on the same IdP, network or MFA system whose failure you are planning for.

## 325: How do workloads on one cloud call another cloud without stored keys?

- **AWS workload to GCP:** GCP Workload Identity Federation with an AWS provider. The workload signs a `GetCallerIdentity` request with its IAM role, and GCP exchanges it for a short-lived token.
- **Azure workload to AWS:** the managed identity gets an Entra token and calls `AssumeRoleWithWebIdentity` on an IAM role that trusts the Entra issuer (an IAM OIDC identity provider).
- **GCP workload to Azure:** a federated identity credential on an Entra app registration or user-assigned managed identity that trusts Google's OIDC tokens for that service account.
- **Any cloud to Cloudflare:** Cloudflare does not accept federated tokens for API access, so you store a narrowly scoped API token in the source cloud's secret store.

**GCP**

```bash
gcloud iam workload-identity-pools providers create-aws aws-prod \
  --location=global --workload-identity-pool=multicloud --account-id=123456789012
```

## 326: How do you solve the "secret zero" problem on each platform?

"Secret zero" is the first credential an app needs to fetch all other secrets. Each platform removes it by giving the workload an identity from the platform itself:

- **AWS:** the IAM role attached to Lambda, ECS tasks or EC2 instances.
- **Azure:** managed identity on the resource.
- **GCP:** the attached service account, through the metadata server.
- **Cloudflare:** bindings and secrets injected into `env` by the platform at deploy time.

The anti-pattern to avoid in a migration is copying an AWS access key into the new cloud's environment variables "just for now". Use federation (question 325) instead.

## 327: How do zero trust access products compare?

| Need                         | AWS                             | Azure                            | GCP                                              | Cloudflare                      |
| ---------------------------- | ------------------------------- | -------------------------------- | ------------------------------------------------ | ------------------------------- |
| Private web apps without VPN | Verified Access                 | Entra Private Access / app proxy | IAP                                              | Access                          |
| Device posture checks        | Verified Access trust providers | Conditional Access with Intune   | Context-Aware Access (Chrome Enterprise Premium) | Access device posture with WARP |
| Secure web gateway           | n/a                             | Entra Internet Access            | Secure Web Proxy (for workloads)                 | Gateway                         |

Cloudflare's offering (Cloudflare One) is not tied to one cloud, which is why many multi-cloud companies use it to give employees one access layer for apps on AWS, Azure and GCP.

## 328: How do you control outbound traffic from workloads?

- **AWS:** NAT gateway plus AWS Network Firewall (domain allowlists, Suricata rules), or Route 53 Resolver DNS Firewall.
- **Azure:** Azure Firewall with application rules (FQDN tags) on a hub VNet, and user-defined routes that force traffic through it.
- **GCP:** Cloud NGFW with FQDN objects in firewall policies, or Secure Web Proxy for HTTP(S) egress.
- **Cloudflare:** Cloudflare Gateway for user and device traffic. Workers outbound requests are not filtered by a firewall you control.

## 329: How do you translate a hub-and-spoke network?

- **AWS:** Transit Gateway as the hub, with VPC attachments per spoke, and a shared inspection VPC.
- **Azure:** a hub VNet with Azure Firewall and VPN or ExpressRoute gateways, peered to spoke VNets with `useRemoteGateways`, or Azure Virtual WAN managing hubs for you.
- **GCP:** Shared VPC (one host project, many service projects) often replaces hub and spoke entirely. For separate VPCs, Network Connectivity Center VPC spokes, or VPC peering with a hub VPC.

In GCP, a single Shared VPC with subnets per team is often simpler than recreating AWS's many-VPC design.

## 330: How does GCP's global VPC change network design compared to AWS?

- One VPC spans all regions, and subnets in different regions route to each other by default. On AWS, you need peering or Transit Gateway between regional VPCs.
- Firewall rules apply to the whole VPC, so you scope them with tags or service accounts, not by subnet.
- Routes are global by default (dynamic routing mode can be regional or global for Cloud Router).
- A single internal load balancer can be reached from other regions with global access enabled.

The risk: a firewall rule meant for one region now affects all regions. Use network firewall policies and clear naming to avoid surprises.

## 331: What are the equivalents of a data perimeter on each cloud?

- **AWS:** a data perimeter built from SCPs, resource control policies and VPC endpoint policies with conditions like `aws:PrincipalOrgID`, `aws:ResourceOrgID` and `aws:SourceVpce`.
- **Azure:** private endpoints with public access disabled, Azure Policy, and Network Security Perimeter for PaaS services.
- **GCP:** VPC Service Controls, which put projects and services inside a perimeter and block data copies to outside projects even with valid credentials.

VPC Service Controls is the most complete built-in option. On AWS the same effect takes several policy types working together.

## 332: How do you plan IP addresses for a multi-cloud setup?

- Reserve a non-overlapping block per cloud and region (for example `10.0.0.0/12` for AWS, `10.16.0.0/12` for Azure, `10.32.0.0/12` for GCP).
- Azure reserves 5 IPs per subnet, AWS reserves 5, GCP reserves 4, so tiny subnets lose a big share.
- Kubernetes needs large ranges: AKS with Azure CNI Overlay and GKE VPC-native clusters use pod ranges, and EKS VPC CNI uses VPC IPs for pods by default.
- Azure and GCP subnets can be expanded later more easily than AWS subnets, which cannot be resized.

Overlapping ranges block peering and VPN routing, and fixing them later means re-IPing workloads, so plan before the first VNet or VPC.

## 333: How does DDoS protection differ architecturally?

- **AWS:** Shield Standard protects all customers at layers 3 and 4. Shield Advanced adds layer 7 response, cost protection and a response team. Protection is strongest on CloudFront, Route 53 and Global Accelerator edges.
- **Azure:** basic infrastructure protection for all, plus DDoS Network Protection with adaptive tuning per public IP. Layer 7 comes from WAF on Front Door or Application Gateway.
- **GCP:** Google front ends absorb volumetric attacks for global load balancers. Cloud Armor adds layer 7 rules and Adaptive Protection (ML-based attack detection).
- **Cloudflare:** all proxied traffic enters through anycast across the whole network, so attacks spread across all data centers. Mitigation for layers 3 to 7 is automatic and unmetered.

The shared design rule: hide origins behind the edge, and make sure attackers cannot reach the origin IP directly.

## 334: How does global load balancing differ between providers?

- **AWS:** most load balancers are regional. Global routing uses Route 53 (DNS) or Global Accelerator (anycast IPs to regional endpoints) or CloudFront in front.
- **Azure:** Front Door is a global layer 7 entry with anycast. Traffic Manager is DNS-based. The cross-region Load Balancer is global layer 4.
- **GCP:** the global external Application Load Balancer uses one anycast IP served from Google's edge, routing to the closest healthy backend in any region.
- **Cloudflare:** every proxied hostname is already anycast. Cloudflare Load Balancing adds health checks and steering (geo, latency, weighted) across origins in any cloud.

DNS-based failover depends on TTLs and client caching, while anycast failover is near instant, which matters for strict RTO targets.

## 335: How do the execution models of Lambda, Azure Functions, Cloud Run and Workers differ under the hood?

- **Lambda:** each execution environment is a Firecracker microVM running your runtime. One environment handles one request at a time.
- **Azure Functions (Flex Consumption):** your code runs in a Functions host process on managed Linux instances. One instance handles many concurrent requests, set by per-instance concurrency.
- **Cloud Run:** your container runs in a gVisor sandbox (first generation) or a microVM (second generation). One instance handles up to the configured concurrency (default 80).
- **Workers:** your script runs in a V8 isolate inside a shared process. Thousands of isolates share one process, and each isolate handles many requests.

These differences explain cold starts, pricing models, how many database connections you open, and what code can run (Workers cannot run arbitrary native binaries).

## 336: What Workers limits shape how you design apps translated from Lambda?

- **CPU time:** 30 seconds by default per request on the paid plan, configurable up to 5 minutes. Wall-clock time waiting on I/O does not count.
- **Memory:** 128 MB per isolate, shared by concurrent requests in that isolate.
- **Subrequests:** a limit on `fetch` and binding calls per request (much higher on paid plans).
- **Bundle size:** a compressed size limit on the Worker script, so huge dependencies (full AWS SDK, heavy ML libraries) are a problem.
- **No native modules or real file system.**

Design changes: stream large payloads instead of buffering, split long work into Workflows steps or Queue messages, and move CPU-heavy or memory-heavy code to Containers.

## 337: What is Smart Placement and when does it matter?

By default, a Worker runs in the Cloudflare location closest to the user. If the Worker then makes several round trips to a database in one region (for example Postgres in `us-east-1`), each trip crosses the world.

Smart Placement watches the Worker's subrequests and, if it is faster, runs the Worker near the backend instead of near the user. You turn it on with:

```jsonc
{ "placement": { "mode": "smart" } }
```

This matters a lot in hybrid migrations where Workers call databases still on AWS, Azure or GCP. Combined with Hyperdrive, it keeps the edge benefits without paying cross-continent latency for every query.

## 338: How does the concurrency model affect database connections after a migration?

- **Lambda:** one request per environment, so 1,000 concurrent requests can mean 1,000 database connections. RDS Proxy is the usual fix.
- **Azure Functions and Cloud Run:** many requests per instance share one connection pool, so a small pool per instance (for example 5 to 10) and a cap on instances keeps the total connection count under control.
- **Workers:** you cannot keep a pool across requests in the usual way, so you use Hyperdrive (which keeps the pool near the database) or HTTP-based database drivers.

When moving from Lambda to Cloud Run, teams often over-provision pools and run out of database connections, because they kept the "one connection per instance" mindset with 80 requests per instance.

## 339: Can you walk through a pricing comparison for an I/O-bound API?

Assume 50 million requests per month, each taking 200 ms of wall-clock time but only 5 ms of CPU, using 256 MB on Lambda.

- **Lambda:** billed for 200 ms x 256 MB on every request, plus request fees. Most of the compute cost is time spent waiting on the database.
- **Azure Functions Flex Consumption:** similar GB-second model on instance memory, but concurrent requests share an instance, so waiting time is shared too.
- **Cloud Run with request-based billing:** billed for instance time while requests are active, shared by up to 80 concurrent requests per instance, which makes I/O wait much cheaper than on Lambda.
- **Workers:** billed for 5 ms CPU per request plus request fees, and waiting is free.

The point to make in an interview: for I/O-heavy APIs, models that charge for CPU (Workers) or share instances across concurrent requests (Cloud Run, Flex Consumption) are usually cheaper than per-request wall-clock billing. For CPU-heavy work, the difference shrinks or reverses.

## 340: How do cold start mitigations compare in depth?

- **Lambda:** provisioned concurrency (paid warm environments), SnapStart (snapshot of an initialized environment for Java, Python and .NET), smaller bundles and lazy imports.
- **Azure Functions:** always-ready instances on Flex Consumption, pre-warmed instances on Premium, and keeping the package small.
- **Cloud Run:** min instances, startup CPU boost (`--cpu-boost`), smaller images, and lazy initialization.
- **Workers:** effectively not needed. Keep global scope work small, because it runs on every new isolate.

On all platforms, the cheapest fix is doing less at startup: create clients lazily, avoid loading large config files, and trim dependencies.

## 341: How do you port Lambda code that uses the AWS SDK heavily to Workers?

Options, from least to most change:

1. **Keep calling AWS from the Worker.** The modular AWS SDK v3 clients work in Workers with `nodejs_compat`, or you use `aws4fetch` (a tiny SigV4 signer built on `fetch`). Store AWS keys as secrets, scoped to the minimum.
2. **Replace AWS services with Cloudflare bindings** one by one: S3 to R2, SQS to Queues, DynamoDB to D1 or Durable Objects, Secrets Manager to secrets.
3. **Hide storage behind interfaces** in your code (`FileStore`, `Queue`, `UserRepository`) so the handler logic does not change while the implementation moves.

**Cloudflare**

```ts
import { AwsClient } from "aws4fetch";

const aws = new AwsClient({
  accessKeyId: env.AWS_KEY_ID,
  secretAccessKey: env.AWS_SECRET,
  region: "us-east-1",
});
const res = await aws.fetch(
  "https://sqs.us-east-1.amazonaws.com/123456789012/orders",
  {
    method: "POST",
    headers: {
      "content-type": "application/x-amz-json-1.0",
      "x-amz-target": "AmazonSQS.SendMessage",
    },
    body: JSON.stringify({
      QueueUrl: "https://sqs.us-east-1.amazonaws.com/123456789012/orders",
      MessageBody: "hi",
    }),
  },
);
```

## 342: How do you migrate observability without losing visibility during the move?

1. Instrument apps with OpenTelemetry (traces, metrics, logs) before migrating, while still exporting to CloudWatch and X-Ray.
2. Run an OpenTelemetry Collector that can send to both the old and new backends (Azure Monitor, Cloud Observability, or a vendor like Grafana or Datadog).
3. Recreate dashboards and alerts on the target before moving traffic, and compare them side by side during the overlap.
4. Keep consistent service names and attributes (`service.name`, `deployment.environment`) so traces connect across clouds during hybrid periods.
5. For Cloudflare Workers, use Workers Observability plus OTLP export to the same backend.

A neutral backend (Grafana, Datadog, Honeycomb, New Relic) often makes multi-cloud setups easier than each cloud's own tools.

## 343: How do you keep logging costs under control on each cloud?

- **AWS:** set retention on every log group, use the Infrequent Access log class, filter noisy logs at the source, and use subscription filters only for what you need.
- **Azure:** use Basic or Auxiliary log tables for verbose logs, daily caps on workspaces, data collection rules to drop fields, and sampling in Application Insights.
- **GCP:** exclusion filters on the `_Default` sink, shorter retention on noisy buckets, and log sampling for high-volume request logs.
- **Cloudflare:** Workers Logs has sampling (`head_sampling_rate`), and Logpush lets you push only selected fields and filtered events.

**Cloudflare**

```jsonc
{ "observability": { "enabled": true, "head_sampling_rate": 0.1 } }
```

## 344: Why does the CloudEvents format matter in a migration?

CloudEvents is a CNCF spec for event metadata (`id`, `source`, `type`, `time`, `subject`, `data`). Azure Event Grid and GCP Eventarc use it natively, and EventBridge does not (it uses `source`, `detail-type`, `detail`).

If your AWS events follow a custom shape, add a translation layer once (for example a small function that maps EventBridge events to CloudEvents), and make consumers depend on CloudEvents fields. Then events can move between Event Grid, Eventarc, Kafka or Cloudflare Queues without changing consumers.

```json
{
  "specversion": "1.0",
  "id": "9f1c2e",
  "source": "/myapp/orders",
  "type": "com.example.order.placed",
  "time": "2026-11-24T10:00:00Z",
  "datacontenttype": "application/json",
  "data": { "orderId": "o1", "total": 120 }
}
```

## 345: How do "exactly once" messaging guarantees compare?

- **SQS standard:** at least once. **SQS FIFO:** exactly-once processing within a 5-minute deduplication window, by message deduplication ID.
- **Service Bus:** at least once with peek-lock. Duplicate detection drops repeated message IDs within a time window. Transactions can tie receive and send together.
- **Pub/Sub:** at least once by default. Exactly-once delivery (per subscription, regional) guarantees no redelivery after a successful ack.
- **Cloudflare Queues:** at least once.

In every case, "exactly once" ends at the broker. Your handler's side effects (database writes, emails) still need idempotency, because a crash between doing the work and acking causes redelivery.

## 346: How do ordering guarantees compare?

- **SQS FIFO:** strict order per message group ID.
- **Service Bus:** strict order per session.
- **Pub/Sub:** order per ordering key when message ordering is on. A failed message blocks later messages with the same key until it succeeds or is dead-lettered.
- **Kinesis, Event Hubs, Kafka:** order per shard or partition.
- **Cloudflare Queues:** no ordering guarantee. Use a Durable Object per key to serialize processing.

Ordering limits parallelism to the number of keys. Choose keys (customer, account) that keep related events in order while still giving enough parallel streams.

## 347: How do you translate the transactional outbox pattern?

The outbox pattern writes the business change and an "event to publish" in the same database transaction, then a relay publishes the event. Translations:

- **AWS:** DynamoDB `TransactWriteItems` (item + outbox item), with DynamoDB Streams and Lambda as the relay. Or RDS with an outbox table and a poller or Debezium.
- **Azure:** Cosmos DB transactional batch in one partition, with the change feed as the relay.
- **GCP:** Firestore transaction, with Firestore triggers through Eventarc as the relay. Or Spanner with change streams.
- **Cloudflare:** a Durable Object writes state and an outbox row to its SQLite storage in one transaction, then an alarm sends pending rows to a Queue and deletes them when sent.

Change-feed-based relays (DynamoDB Streams, Cosmos change feed, Firestore triggers) often make the separate outbox table unnecessary: the state change itself becomes the event.

## 348: How do you translate a saga with compensation steps?

- **AWS:** Step Functions with `Catch` blocks that call compensating Lambdas in reverse order.
- **Azure:** Durable Functions orchestrator with `try/catch` around activities, calling compensations in `catch`.
- **GCP:** Workflows with `try/except` blocks and compensation calls.
- **Cloudflare:** Workflows with `try/catch` around `step.do` calls, where compensations are also `step.do` calls so they are durable.

**Cloudflare**

```ts
async run(event: WorkflowEvent<Booking>, step: WorkflowStep) {
  const flight = await step.do("book flight", () => bookFlight(event.payload));
  try {
    await step.do("book hotel", () => bookHotel(event.payload));
  } catch (err) {
    await step.do("cancel flight", () => cancelFlight(flight.id));
    throw err;
  }
}
```

Compensations must be idempotent too, because the engine may retry them.

## 349: How does Kubernetes portability hold up in practice between EKS, AKS and GKE?

Portable with little change: Deployments, Services, ConfigMaps, Helm charts, HPA, most operators, and the Gateway API.

Needs translation:

- Identity: IRSA or Pod Identity annotations become Workload ID or Workload Identity annotations.
- Load balancer annotations (`service.beta.kubernetes.io/aws-load-balancer-*`) become Azure or GCP annotations.
- Storage classes and CSI drivers.
- Node autoscaling (Karpenter configs, node pools).
- Logging and monitoring agents (Container Insights, Azure Monitor for containers, GKE's built-in logging).
- Network policies (Calico, Cilium, AKS network policy, GKE Dataplane V2).

Keeping cloud-specific settings in Helm values or Kustomize overlays per cloud is the usual way to keep one set of manifests.

## 350: How do managed Kubernetes control planes and upgrades differ?

- **EKS:** you pay per cluster hour. Upgrades are manual (control plane, then nodes and add-ons), with extended support at extra cost for older versions.
- **AKS:** free tier control plane (no SLA) or Standard tier with SLA. Auto-upgrade channels and planned maintenance windows.
- **GKE:** release channels (Rapid, Regular, Stable, Extended) with automatic control plane and node upgrades and maintenance windows. Autopilot manages everything.

GKE upgrades itself by default, which surprises teams coming from EKS, where nothing upgrades unless you do it. Set maintenance windows and exclusions before migrating production workloads.

## 351: How do object storage request rate limits compare?

- **S3:** at least 3,500 writes and 5,500 reads per second per prefix, and it scales by spreading keys over more prefixes. Sudden spikes can return `503 Slow Down` while S3 scales.
- **Azure Blob Storage:** limits per storage account (requests per second and ingress or egress bandwidth), and per blob. Very high scale needs several accounts or premium block blob accounts.
- **Cloud Storage:** about 1,000 writes and 5,000 reads per second per bucket to start, and it autoscales over time. Ramp traffic gradually, and avoid sequential key names that hit one key range.
- **R2:** high limits per bucket, with a lower limit on writes to the same object key (about one per second for concurrent writes to one key).

The shared lesson: avoid sequential prefixes (timestamps at the start of keys) and ramp large jobs gradually.

## 352: What are the high-performance object storage options?

- **AWS:** S3 Express One Zone, directory buckets in one zone with single-digit millisecond latency.
- **Azure:** premium block blob storage accounts on SSDs.
- **GCP:** Rapid Storage (zonal buckets) for low-latency, high-throughput access in one zone, and Anywhere Cache for caching data near compute.

Cloudflare has no special performance tier, but frequently read objects are served from Cloudflare's cache. For ML training data, all three big clouds also offer Lustre file systems, which often beat object storage.

## 353: How do multipart upload limits compare?

| Limit           | S3                 | Azure block blob          | Cloud Storage                                                  | R2                                               |
| --------------- | ------------------ | ------------------------- | -------------------------------------------------------------- | ------------------------------------------------ |
| Parts / blocks  | Up to 10,000 parts | Up to 50,000 blocks       | Up to 32 objects per compose (repeatable), or resumable upload | Up to 10,000 parts                               |
| Part size       | 5 MiB to 5 GiB     | Up to 4,000 MiB per block | Any size chunks (multiples of 256 KiB)                         | 5 MiB to 5 GiB (all but last part the same size) |
| Max object size | Several TB         | About 190 TiB             | 5 TiB                                                          | About 5 TiB                                      |

S3 and R2 use the same multipart API, so S3 multipart code works on R2 with only the endpoint changed. Azure uses `Put Block` and `Put Block List`. GCS prefers resumable uploads, and its XML API also supports S3-style multipart uploads.

## 354: How do you translate S3 Object Lock for compliance storage?

- **AWS:** S3 Object Lock in governance or compliance mode, with retention periods and legal holds (WORM).
- **Azure:** immutable storage for Blob Storage: time-based retention policies and legal holds at container or version level, which can be locked.
- **GCP:** Bucket Lock (a locked retention policy on a bucket) and object retention configurations per object, plus event-based holds.
- **Cloudflare:** R2 bucket locks, with retention rules by prefix (a number of days, a date, or indefinite).

Locked compliance policies on all four cannot be shortened or removed, even by admins, so test with short periods first.

## 355: How do you translate cross-region replication of objects?

- **AWS:** S3 Cross-Region Replication (CRR) per bucket with rules and an IAM role, plus Replication Time Control for an SLA.
- **Azure:** geo-redundant storage (GRS or GZRS) at the account level, replicating to the paired region automatically. Object replication between accounts gives rule-based control like CRR.
- **GCP:** dual-region or multi-region buckets that replicate automatically, with turbo replication for a 15-minute RPO in dual-region buckets.
- **Cloudflare:** no customer-managed replication. R2 stores data durably in its region. For a second copy, copy objects to another bucket or provider yourself.

GCS dual-region buckets and Azure GRS need no replication rules, which removes a whole class of AWS config.

## 356: How do you handle data residency on each provider?

- **AWS:** pick regions, enforce with SCPs on `aws:RequestedRegion`, and watch global services (IAM, CloudFront, Route 53) that are not region-bound. AWS European Sovereign Cloud is a separate EU-only partition.
- **Azure:** pick regions, use the "Allowed locations" policy, and the EU Data Boundary for Microsoft services. Sovereign clouds exist for some countries.
- **GCP:** the `gcp.resourceLocations` org policy, Assured Workloads for regulated regimes, and sovereign cloud offerings with local partners.
- **Cloudflare:** the Data Localization Suite (Regional Services to inspect traffic only in a region, Customer Metadata Boundary for logs), and jurisdiction-restricted R2 buckets and Durable Objects (for example `eu`).

**Cloudflare**

```bash
npx wrangler r2 bucket create eu-files --jurisdiction eu
```

## 357: How do disaster recovery strategies translate?

| Strategy           | AWS                                                | Azure                                          | GCP                                         |
| ------------------ | -------------------------------------------------- | ---------------------------------------------- | ------------------------------------------- |
| Backup and restore | AWS Backup cross-region copies                     | Azure Backup cross-region restore              | Backup and DR Service, cross-region backups |
| Pilot light        | Aurora Global DB + stopped infra in IaC            | Geo-replicated DB + IaC ready                  | Cross-region replica + IaC ready            |
| Warm standby       | Scaled-down stack in 2nd region, Route 53 failover | Scaled-down stack, Front Door priority routing | Scaled-down stack, global LB                |
| Active-active      | DynamoDB global tables, Route 53 latency routing   | Cosmos DB multi-write, Front Door              | Spanner multi-region, global LB             |

For Cloudflare, the edge layer is already multi-location, so DR planning focuses on the data stores (D1 backups via Time Travel and exports, R2 copies elsewhere) and on origin failover with Load Balancing.

## 358: What RTO and RPO can you expect from managed database DR on each cloud?

- **Aurora Global Database:** RPO typically around a second, RTO about a minute with managed failover.
- **Azure SQL failover groups:** RPO of seconds (asynchronous geo-replication), RTO of about an hour as the documented target for customer-managed failover, often much faster in practice.
- **Cloud SQL cross-region replica:** RPO depends on replication lag, RTO of minutes with promotion, or using cross-region disaster recovery with a designated replica.
- **Spanner multi-region:** RPO zero, with automatic failover inside the instance configuration.
- **Cosmos DB multi-region:** RPO depends on consistency level (zero with strong across regions), and RTO is automatic with service-managed failover.

Always confirm the current SLA pages, and test failover. Documented numbers are targets, not guarantees for your app.

## 359: How would you design an active-active web app on each cloud?

- **AWS:** CloudFront and Route 53 latency routing to API Gateway and Lambda in two regions, DynamoDB global tables, S3 replication.
- **Azure:** Front Door to Container Apps or Functions in two regions, Cosmos DB with multi-region writes, GZRS storage or object replication.
- **GCP:** global external Application Load Balancer to Cloud Run in two regions (serverless NEGs), Spanner or Firestore multi-region, dual-region buckets.
- **Cloudflare:** Workers everywhere, Durable Objects for per-entity consistency, D1 read replication, and R2. The compute is active-active by default.

The hard part on all of them is the same: writes. Decide which data can be eventually consistent and which must have one owner region.

## 360: How do you translate a cell-based architecture?

A cell is a complete, independent copy of the stack serving a slice of customers, with a thin routing layer in front.

- **AWS:** one account per cell, a router (Lambda or CloudFront Functions with a cell-mapping table), and separate DynamoDB tables per cell.
- **Azure:** one subscription or resource group per cell (deployment stamps), with Front Door routing by tenant.
- **GCP:** one project per cell, with a global load balancer and URL maps or a routing service.
- **Cloudflare:** a router Worker that maps tenants to cells (stored in KV), and per-cell origins or per-tenant D1 databases and Durable Objects.

Cells limit the blast radius of a bad deploy or noisy tenant to one cell, and they also work around per-account and per-project quotas.

## 361: How do you isolate tenants in a multi-tenant SaaS on each platform?

| Isolation level  | AWS                                                  | Azure                                       | GCP                                                 | Cloudflare                                        |
| ---------------- | ---------------------------------------------------- | ------------------------------------------- | --------------------------------------------------- | ------------------------------------------------- |
| Strongest (silo) | Account per tenant                                   | Subscription per tenant                     | Project per tenant                                  | Account per tenant                                |
| Middle (bridge)  | Table or schema per tenant                           | Container or database per tenant            | Database per tenant                                 | D1 database per tenant, Durable Object per tenant |
| Shared (pool)    | Shared table, `tenantId` key, ABAC with session tags | Shared container, partition key `/tenantId` | Shared collection, security rules or IAM conditions | Shared D1 with `tenant_id` column                 |
| Tenant code      | n/a                                                  | n/a                                         | n/a                                                 | Workers for Platforms                             |

Cloudflare makes the "database per tenant" model cheap, because D1 databases and Durable Objects have no per-instance fixed cost.

## 362: What is Workers for Platforms and what does it replace?

Workers for Platforms lets a SaaS run untrusted code from its customers as Workers in a dispatch namespace. A dispatch Worker receives each request, decides which customer script handles it, and can apply limits (CPU, subrequests) and add custom bindings.

On AWS, the closest approach is creating a Lambda function per customer in a separate account, with heavy orchestration. Azure and GCP have no direct equivalent.

```ts
export default {
  async fetch(request: Request, env: { DISPATCHER: DispatchNamespace }) {
    const tenant = new URL(request.url).hostname.split(".")[0];
    const worker = env.DISPATCHER.get(tenant, {}, { limits: { cpuMs: 50 } });
    return worker.fetch(request);
  },
};
```

## 363: How do landing zone designs translate?

| Layer            | AWS (Control Tower)                               | Azure (landing zones)                                              | GCP (enterprise foundations)                   |
| ---------------- | ------------------------------------------------- | ------------------------------------------------------------------ | ---------------------------------------------- |
| Hierarchy        | OUs: Security, Infrastructure, Workloads, Sandbox | Management groups: Platform, Landing zones (Corp, Online), Sandbox | Folders: bootstrap, common, prod, nonprod, dev |
| Central logging  | Log Archive account                               | Management subscription with Log Analytics                         | Logging project with aggregated sinks          |
| Security tooling | Audit account (Security Hub, GuardDuty)           | Defender for Cloud, Sentinel in management                         | Security Command Center at org level           |
| Networking       | Network account, Transit Gateway                  | Connectivity subscription, hub VNet or Virtual WAN                 | Shared VPC host projects                       |
| Guardrails       | SCPs, Config rules                                | Azure Policy initiatives                                           | Organization policies                          |
| Account vending  | Account Factory                                   | Subscription vending (Bicep or Terraform modules)                  | Project factory (Terraform)                    |

The shapes are almost identical, so an AWS landing zone design document translates well section by section.

## 364: How do you translate common SCPs into Azure Policy and GCP organization policies?

| Guardrail             | AWS SCP                                      | Azure Policy                                            | GCP org policy                         |
| --------------------- | -------------------------------------------- | ------------------------------------------------------- | -------------------------------------- |
| Allowed regions       | Deny if `aws:RequestedRegion` not in list    | Allowed locations                                       | `gcp.resourceLocations`                |
| No public storage     | Deny `s3:PutBucketPublicAccessBlock` changes | Deny storage accounts with public access                | `storage.publicAccessPrevention`       |
| No long-lived keys    | Deny `iam:CreateAccessKey`                   | Entra app management policies that block client secrets | `iam.disableServiceAccountKeyCreation` |
| Require encryption    | Deny unencrypted `PutObject`                 | Require CMK on storage                                  | `gcp.restrictNonCmekServices`          |
| Block leaving the org | Deny `organizations:LeaveOrganization`       | n/a                                                     | n/a                                    |

## 365: How do billing structures compare?

- **AWS:** the management account of AWS Organizations pays for all member accounts (consolidated billing).
- **Azure:** billing accounts under an Enterprise Agreement or Microsoft Customer Agreement, with billing profiles and invoice sections, linked to subscriptions.
- **GCP:** Cloud Billing accounts that projects link to. One billing account can pay for projects across organizations.
- **Cloudflare:** billing per account, with subscriptions for plans and add-ons per zone or account.

In GCP, unlinking a project from its billing account stops its resources, which is used as a hard spending cap pattern (with a budget alert that calls a function to unlink billing).

## 366: How do you compare costs across clouds in one report?

- Export billing data from each provider in FOCUS format (AWS Data Exports, Azure Cost Management exports, GCP's FOCUS view on the BigQuery billing export).
- Load them into one warehouse and normalize service categories, regions and tags or labels.
- Track unit costs (cost per request, per tenant, per GB served) rather than raw totals, so the comparison survives traffic changes.
- Add Cloudflare usage from its billing and analytics APIs, mapped into the same categories by hand, since it has no FOCUS export.

## 367: How do you migrate DNS to a new provider with zero downtime?

1. Lower TTLs on records you will change (for example to 300 seconds) at least one old-TTL period before the move.
2. Copy all records to the new provider. Export from Route 53 and import a zone file (Azure DNS, Cloud DNS and Cloudflare all accept BIND zone files).
3. Check the new name servers answer correctly (`dig @new-ns example.com`).
4. If DNSSEC is on, turn it off at the registrar first or do a multi-signer migration, or resolvers will reject answers.
5. Change the name servers at the registrar. Both providers serve correct answers during the NS TTL (often 48 hours), so users see no downtime.
6. Keep the old zone for a week before deleting it.

**Cloudflare**

```bash
aws route53 list-resource-record-sets --hosted-zone-id Z123EXAMPLE > records.json
# convert to a BIND file, then import in the Cloudflare dashboard (DNS > Records > Import)
```

## 368: What is the difference between full and partial (CNAME) setup when moving to Cloudflare?

- **Full setup:** Cloudflare becomes the authoritative DNS provider for the domain. You change name servers at the registrar. All Cloudflare features are available.
- **Partial (CNAME) setup:** DNS stays at Route 53 (or another provider), and you CNAME specific hostnames to Cloudflare. Available on Business and Enterprise plans.

During a gradual migration away from Route 53, partial setup lets you put Cloudflare's CDN and WAF in front of a few hostnames first, without moving the whole zone.

## 369: How do you migrate a large S3 bucket with minimal downtime?

- **To Azure:** Azure Storage Mover or `azcopy copy 'https://bucket.s3.amazonaws.com' 'https://account.blob.core.windows.net/container' --recursive`, then `azcopy sync` for changes, then cut over.
- **To GCP:** Storage Transfer Service with an S3 source, scheduled to run repeatedly until cut-over. It can use AWS role federation instead of keys.
- **To R2:** Super Slurper for the bulk copy and Sippy for lazy copy on read. Together they let you switch reads to R2 right away.

**GCP**

```bash
gcloud transfer jobs create s3://my-bucket gs://my-bucket \
  --source-creds-file=aws-creds.json --schedule-repeats-every=1h
```

Plan for metadata differences: S3 user metadata, tags, ACLs and storage classes do not all carry over, and object ETags will differ for multipart uploads.

## 370: How do you cut over a relational database between clouds?

1. Set up continuous replication (Database Migration Service on the target, or logical replication from RDS Postgres).
2. Wait until the replica is in sync, and validate row counts and checksums on key tables.
3. Put the app in read-only or maintenance mode for a short window.
4. Wait for replication lag to reach zero, then stop replication and promote the target.
5. Update the connection string (ideally a DNS name you control, so the change is one record).
6. Re-enable writes and watch errors closely.
7. Keep reverse replication or the old database ready for rollback for a set period.

Sequences and identity columns are a common bug: after promotion, make sure sequence values on the target are ahead of the highest copied ID.

## 371: How do you migrate DynamoDB data to Cosmos DB or Firestore?

1. Export the table to S3 with point-in-time export (DynamoDB JSON or Ion format), which does not use table capacity.
2. **Cosmos DB:** use Azure Data Factory or a custom job (Spark, a Container Apps job) to read the export, transform items (add `id` and the partition key field, convert DynamoDB types), and bulk insert.
3. **Firestore:** use a Dataflow job or a script with batched writes, mapping items to documents and collections.
4. For the gap between export and cut-over, replay changes from DynamoDB Streams with a Lambda that writes to the target.

DynamoDB's typed JSON (`{"S": "Ana"}`, `{"N": "42"}`) must be unmarshalled first (`unmarshall` from `@aws-sdk/util-dynamodb`).

## 372: How do you migrate users out of Cognito?

Cognito does not export password hashes, so there are two strategies:

- **Lazy migration:** the new identity system (Entra External ID custom authentication extensions, Identity Platform blocking functions, Auth0, or your own Worker-based login) receives the login, checks the password against Cognito with `InitiateAuth`, and on success creates the user with that password in the new system.
- **Bulk import plus reset:** export user attributes (with `ListUsers`), import them into the new system, and require a password reset or passwordless login.

Lazy migration keeps users happy but needs Cognito running until most active users have logged in. MFA secrets cannot be exported either, so users must enroll MFA again.

## 373: How do you migrate KMS-encrypted data and secrets?

- AWS KMS keys (customer-managed, AWS-generated material) cannot be exported. Decrypt data on AWS and re-encrypt on the target with Key Vault or Cloud KMS keys.
- If you used imported key material (BYOK), you kept a copy of the key and can import it into Azure Managed HSM or Cloud KMS, but re-wrapping data keys is still cleaner.
- Secrets Manager values are exported by reading each secret and writing it into Key Vault, Secret Manager or Cloudflare secrets. Rotate them right after the move, because they passed through the migration tooling.
- Encrypted EBS snapshots and RDS backups cannot be read outside AWS. Export data logically instead.

## 374: How do you translate a CloudFront distribution to Cloudflare?

| CloudFront concept                   | Cloudflare equivalent                                                  |
| ------------------------------------ | ---------------------------------------------------------------------- |
| Distribution + alternate domain      | Proxied DNS record in a zone                                           |
| Origin and origin groups             | DNS record target, or Load Balancing pools                             |
| Cache behaviors by path              | Cache Rules, Origin Rules, Configuration Rules                         |
| Cache policy / origin request policy | Cache Rules (cache key, TTL), Transform Rules                          |
| CloudFront Functions / Lambda@Edge   | Workers, Snippets, Transform and Redirect Rules                        |
| Origin Access Control                | Cloudflare Tunnel or Authenticated Origin Pulls; Workers + R2 bindings |
| Signed URLs / cookies                | Worker token check, or WAF token authentication                        |
| Geo restriction                      | WAF custom rule on `ip.src.country`                                    |
| AWS WAF web ACL                      | Cloudflare WAF managed and custom rules                                |
| Real-time logs                       | Logpush (and Instant Logs)                                             |

A practical tip: CloudFront forwards very little by default, while Cloudflare forwards most headers, cookies and query strings to the origin. Check cache keys so you do not accidentally lower your hit rate or serve personalized content from cache.

## 375: How would you migrate a Lambda + API Gateway + DynamoDB app to Cloudflare?

1. **Routing:** API Gateway routes become a Hono router in one Worker (or several Workers joined by service bindings).
2. **Handlers:** Lambda handlers become route handlers. Replace `event` and return objects with `Request` and `Response`.
3. **Data:** pick per table. Relational access patterns go to D1, per-entity state with strong consistency goes to Durable Objects, and config or cache goes to KV.
4. **Async work:** SQS becomes Queues, Step Functions becomes Workflows, EventBridge Scheduler becomes Cron Triggers.
5. **Auth:** Cognito stays at first (verify its JWTs in the Worker with `jose`), and moves later if needed.
6. **Migration path:** put Cloudflare in front of API Gateway first, then move routes one by one to Workers (strangler fig), while the Worker still calls DynamoDB through `aws4fetch` until the data moves.
7. **Test:** run the same contract tests against both versions.

The usual blockers are large dependencies, CPU-heavy endpoints and code that relies on Node APIs missing from Workers. Those endpoints can stay on Lambda or move to Containers.

## 376: How would you migrate the same app to Azure?

- **API Gateway** becomes API Management (Consumption or Standard v2) or just HTTP-triggered Functions with routes.
- **Lambda** becomes Azure Functions on Flex Consumption (Node.js v4 programming model).
- **DynamoDB** becomes Cosmos DB for NoSQL with a partition key matching the DynamoDB partition key, and the change feed replacing Streams.
- **SQS / SNS** become Service Bus queues and topics.
- **Cognito** becomes Entra External ID.
- **IAM roles** become managed identities with RBAC data-plane roles (Cosmos DB Built-in Data Contributor, Service Bus Data Sender).
- **CloudWatch** becomes Application Insights and Log Analytics.
- **CloudFormation or SAM** becomes Bicep or Terraform, deployed with GitHub Actions using OIDC.

Cosmos DB data-plane RBAC roles are assigned with `az cosmosdb sql role assignment create`, not the normal `az role assignment create`, which trips up many teams.

## 377: How would you migrate the same app to GCP?

- **API Gateway + Lambda** become Cloud Run (one service with an Express or Hono router), or Cloud Run functions per endpoint, with API Gateway or a load balancer in front if needed.
- **DynamoDB** becomes Firestore (Native mode), or Bigtable for very high throughput key-value workloads.
- **SQS / SNS** become Pub/Sub topics and subscriptions, and Cloud Tasks for rate-limited HTTP dispatch.
- **Step Functions** becomes Workflows.
- **Cognito** becomes Identity Platform.
- **IAM roles** become one service account per service with narrow roles.
- **CloudWatch** becomes Cloud Logging and Cloud Monitoring, with structured JSON logs.

Moving several Lambdas into one Cloud Run service is common, because Cloud Run handles many routes and concurrent requests per instance, which lowers cost and cold starts.

## 378: How do you prove the translated system behaves the same?

- **Contract tests:** run the same API test suite (status codes, bodies, headers, error shapes) against old and new endpoints.
- **Shadow traffic:** mirror a copy of real requests to the new system and compare responses, without returning them to users.
- **Data checks:** compare row counts, checksums and sample records between old and new stores.
- **Replay:** replay recorded event streams (from S3 exports or logs) into the new pipeline and compare outputs.
- **Performance tests:** check latency percentiles and throughput, especially for cold starts and database connections.
- **Gradual traffic:** weighted routing (Route 53, Front Door, Cloudflare Load Balancing) from 1% up, with automatic rollback on error rates.

## 379: How do you send shadow traffic during a migration?

- **AWS side:** an API Gateway or ALB cannot mirror traffic by itself. Use a proxy (Envoy) or VPC Traffic Mirroring for raw packets.
- **Cloudflare in front:** a Worker can send a copy of each request to the new backend with `ctx.waitUntil`, while returning the old backend's response.

```ts
export default {
  async fetch(request: Request, env: Env, ctx: ExecutionContext) {
    const shadow = request.clone();
    ctx.waitUntil(
      fetch(
        new URL(new URL(request.url).pathname, env.NEW_ORIGIN),
        shadow,
      ).then(async (res) => {
        if (res.status >= 500)
          console.log({
            shadowError: res.status,
            path: new URL(request.url).pathname,
          });
      }),
    );
    return fetch(request); // old origin stays the source of truth
  },
};
```

Only shadow read-only requests, or make sure the new system writes to an isolated store. Shadowing `POST /payments` to a live payment provider would charge customers twice.

## 380: How does the strangler fig pattern work with Cloudflare in front?

1. Point DNS at Cloudflare and proxy all traffic to the existing AWS origin. Nothing changes for users.
2. Add a Worker on the hostname that routes by path: migrated routes go to the new backend (Workers, Azure or GCP), everything else goes to AWS.
3. Move routes one by one, with a feature flag in KV to switch each route back quickly.
4. When no routes go to AWS, remove the old origin.

The same pattern works with Azure Front Door rules or a GCP global load balancer URL map, but Cloudflare makes it easy because the edge sits in front of any origin.

## 381: How do you connect clouds privately during a hybrid period?

- **AWS to Azure:** Site-to-Site VPN between a virtual private gateway and Azure VPN Gateway, or Direct Connect and ExpressRoute meeting at a colocation partner (for example through Equinix or Megaport).
- **AWS or Azure to GCP:** HA VPN, or Cross-Cloud Interconnect, which gives a dedicated physical link from GCP to AWS, Azure or Oracle.
- **Through Cloudflare:** Magic WAN or Magic Cloud Networking to connect VPCs from several clouds over Cloudflare's network, or Cloudflare Tunnel for app-level connections.

Budget for the egress on both sides during the hybrid period. Chatty services split across clouds can cost more than expected.

## 382: When does a multi-cloud abstraction layer help, and when does it hurt?

Helps:

- Thin interfaces around storage, queues and secrets in application code, so a migration changes one adapter.
- Kubernetes, Terraform, OpenTelemetry and Postgres as common ground.
- Standard protocols (S3 API, OIDC, CloudEvents) instead of proprietary ones.

Hurts:

- A "lowest common denominator" platform that hides each cloud's best features (Spanner consistency, DynamoDB streams, Durable Objects) and still leaks differences.
- Big internal frameworks that a small team must maintain forever.
- Abstracting IAM and networking, which differ too much to hide safely.

A good rule: abstract at the application boundary (your own interfaces), not at the infrastructure layer.

## 383: How do you structure Terraform for several providers?

- One root module per environment and provider (`aws/prod`, `azure/prod`, `cloudflare/prod`), so a failure or plan in one does not block others.
- Shared modules per capability (`static-site`, `queue-worker`) with a provider-specific implementation each, and similar input variables.
- Remote state per root module, in the provider where it runs (S3, Azure Blob, GCS, or R2).
- Data passed between roots through outputs read with `terraform_remote_state` or a parameter store.
- OIDC authentication for each provider in CI.

Avoid one giant module with all four providers. It makes plans slow and failures hard to isolate.

## 384: What are alternatives to Terraform for multi-cloud IaC?

- **OpenTofu:** an open-source fork of Terraform with the same language and providers.
- **Pulumi:** IaC in TypeScript, Python, Go or C#, with providers for AWS, Azure, GCP and Cloudflare.
- **Crossplane:** manages cloud resources as Kubernetes custom resources, useful when your platform team already runs everything through Kubernetes.
- **Cloud-native tools:** CloudFormation and CDK (AWS), Bicep (Azure), Infrastructure Manager (Terraform on GCP), Wrangler (Cloudflare Workers).

For teams coming from AWS CDK, Pulumi feels the most familiar, because it is also general-purpose code.

## 385: Which AWS services create the most lock-in, and how does that affect translation effort?

High effort to translate:

- DynamoDB (data model, streams, transactions), Step Functions (ASL), EventBridge rules, Cognito (password hashes), AppSync, Kinesis, and IAM-heavy designs.
- KMS-encrypted data and anything depending on AWS-specific networking (PrivateLink, Transit Gateway).

Medium effort:

- Lambda (handler signatures, triggers), SQS and SNS, API Gateway, CloudWatch dashboards and alarms.

Low effort:

- RDS and Aurora (Postgres or MySQL), EKS workloads, containers on ECS, S3 data (S3 API is widely supported), and anything already on Terraform and OpenTelemetry.

Use this ranking to estimate a migration and to decide where to add abstraction early.

## 386: How much lock-in does Cloudflare create?

- **Workers runtime:** open source (`workerd`), and code uses standard web APIs (`fetch`, `Request`, `Response`, Web Crypto), which run on Deno, Bun, Node and other edge runtimes.
- **R2:** S3-compatible API, so moving data out is easy and free of egress fees.
- **D1:** SQLite, so the data exports as standard SQL.
- **High lock-in:** Durable Objects, Workflows, Queues and bindings-based design. There is no equivalent elsewhere, so translating them out means redesigning with databases, queues and workflow engines.

The same trade-off as any cloud: the most unique features give the most value and the most lock-in.

## 387: When should you not move a workload to Cloudflare?

- Long CPU-heavy jobs (video encoding, large data processing) that exceed Workers CPU limits. Containers help, but big batch work fits Azure Batch, Cloud Run jobs or AWS Batch better.
- Apps tightly bound to a relational database that must stay in one region, with many round trips per request, unless you use Hyperdrive and Smart Placement.
- Workloads that need VMs, GPUs you control, Windows, or Kubernetes.
- Teams that need deep VPC networking, private subnets and on-premises connectivity for every service.
- Very large single databases (D1 has a per-database size limit of 10 GB).

## 388: How do you translate centralized security logging?

- **AWS:** an organization CloudTrail into a Log Archive account, GuardDuty and Security Hub with a delegated admin, and Amazon Security Lake (OCSF format).
- **Azure:** diagnostic settings (enforced by Azure Policy) sending logs to a central Log Analytics workspace, with Microsoft Sentinel as SIEM and Defender for Cloud alerts.
- **GCP:** organization-level aggregated log sinks into a central logging project or BigQuery, Security Command Center, and Google Security Operations (Chronicle) as SIEM.
- **Cloudflare:** Logpush for HTTP, firewall, Workers trace and audit logs into the same SIEM, plus Cloudflare's own security analytics.

Normalize to one schema (OCSF or ECS) if you run several clouds, so detections work across all of them.

## 389: How do you translate GuardDuty-based incident response?

1. **Detection:** GuardDuty findings become Defender for Cloud alerts (Azure) or Security Command Center findings (GCP).
2. **Routing:** EventBridge rules on findings become Logic Apps or Sentinel automation rules (Azure), or SCC notifications to Pub/Sub (GCP).
3. **Containment:** a Lambda that isolates an instance (swap security group) becomes a playbook that applies an "isolate" NSG (Azure) or a firewall rule with a quarantine tag (GCP).
4. **Credentials:** revoking IAM role sessions becomes disabling the managed identity's access or the service account (`gcloud iam service-accounts disable`).
5. **Forensics:** EBS snapshots become managed disk snapshots or persistent disk snapshots, copied to a forensics subscription or project.

## 390: How do BYOK and hold-your-own-key options compare?

- **AWS:** imported key material in KMS (BYOK), CloudHSM-backed custom key stores, and External Key Store (XKS) where keys stay in your own HSM outside AWS.
- **Azure:** BYOK into Key Vault Premium or Managed HSM, and Managed HSM for single-tenant FIPS 140-3 Level 3 keys.
- **GCP:** imported keys in Cloud KMS, Cloud HSM, and Cloud External Key Manager (EKM), where the key stays with a partner key manager.
- **Cloudflare:** Keyless SSL (TLS private keys stay on your servers) and Geo Key Manager (choose where keys are stored).

XKS and Cloud EKM are the closest pair: the provider never holds the key, and you can cut off access by disabling your key manager.

## 391: How does confidential computing compare?

- **AWS:** Nitro Enclaves (isolated environments attached to EC2 instances), and AMD SEV-SNP on some instance types.
- **Azure:** confidential VMs (AMD SEV-SNP, Intel TDX), confidential containers on AKS and Container Instances, and Azure Attestation.
- **GCP:** Confidential VMs (AMD SEV, SEV-SNP, Intel TDX), Confidential GKE nodes, and Confidential Space for multi-party data sharing.

Cloudflare has no confidential computing offering for customer code. Nitro Enclaves code needs real rework on other clouds, since their model is VM-level, not enclave-level.

## 392: How do you secure the container supply chain on each cloud?

- **AWS:** ECR image scanning (Inspector), signing with AWS Signer and Notation, and admission checks on EKS with Kyverno or Gatekeeper.
- **Azure:** ACR with Defender for Containers scanning, Notation signing with Key Vault, and Azure Policy for AKS (Gatekeeper) to enforce signed images.
- **GCP:** Artifact Analysis scanning, Binary Authorization to allow only attested images on GKE and Cloud Run, and SLSA provenance from Cloud Build.
- **Cloudflare:** Containers images come from your build. Sign and scan in CI before `wrangler deploy`.

Binary Authorization is a strong built-in deploy gate that has no exact AWS equivalent, so AWS teams moving to GCP often adopt it.

## 393: How do you enforce Kubernetes policies across EKS, AKS and GKE?

- **AKS:** Azure Policy for Kubernetes (Gatekeeper-based) with built-in initiatives.
- **GKE:** Policy Controller (Gatekeeper-based) with policy bundles such as CIS and Pod Security Standards.
- **EKS:** install Kyverno or OPA Gatekeeper yourself.
- **All three:** Kubernetes Pod Security Admission and ValidatingAdmissionPolicy (CEL), built into Kubernetes.

Write policies once as Gatekeeper constraints, Kyverno policies or ValidatingAdmissionPolicy, and they run on all three.

## 394: Should you use HashiCorp Vault or each cloud's secret manager in a multi-cloud setup?

- **Native secret managers** (Secrets Manager, Key Vault, Secret Manager, Cloudflare secrets): no servers to run, native identity, cheap. But each has its own API and access model.
- **Vault (or a managed Vault):** one API and policy model across clouds, dynamic secrets (short-lived database credentials), and PKI. But it is another critical system to run and secure.

A common middle ground: keep native secret managers, and use External Secrets Operator (for Kubernetes) or a small internal library to read secrets through one interface. Use Vault only if you need dynamic secrets or one policy model badly enough to run it.

## 395: How do you vend new accounts, subscriptions or projects safely at scale?

- **AWS:** Control Tower Account Factory or Account Factory for Terraform (AFT), applying baselines (CloudTrail, Config, SSO assignments) automatically.
- **Azure:** subscription vending with the Azure landing zone Bicep or Terraform modules, placing new subscriptions under the right management group with policies and networking.
- **GCP:** the project factory Terraform module, with folders, billing, shared VPC attachment and default APIs.
- **Cloudflare:** new accounts set up by an admin (multi-account management is an Enterprise feature), with Terraform to apply standard settings.

The vending pipeline is where guardrails and naming stay consistent, so build it before teams start migrating.

## 396: How do quotas affect a large migration?

- New AWS accounts, Azure subscriptions and GCP projects start with low default quotas (vCPUs, IPs, Lambda concurrency, Cloud Run instances).
- Quota increases can take days, and some need a support plan or a sales conversation.
- Some quotas are per region, so a multi-region design needs requests in every region.
- Cloudflare limits (Workers subrequests, D1 database count and size, Queues throughput) are documented per plan, and some can be raised by request.

List expected quotas in the migration plan and request them weeks before load tests.

## 397: How does the Azure resource group model change the way you organize resources compared to AWS?

- Every Azure resource must be in a resource group, which is a lifecycle and access boundary inside a subscription.
- You can assign RBAC and policies at the resource group level, which on AWS needs tag-based conditions.
- Deleting a resource group deletes everything inside it, which is great for temporary environments and dangerous in production (use resource locks).
- A resource group has a location for its metadata, but its resources can be in other regions.

A common pattern: one resource group per app per environment (`rg-orders-prod`), and shared infrastructure (networking, monitoring) in its own groups.

## 398: How does the GCP project model change the way you organize resources?

- The project is the main unit for APIs, billing, quotas and IAM. Every service API must be enabled per project (`gcloud services enable run.googleapis.com`).
- Projects are cheap to create, so GCP designs use many small projects (per app and environment) more freely than AWS uses accounts.
- Project IDs are globally unique and permanent, so naming conventions matter.
- Shared VPC links networking across projects, so isolation by project does not mean separate networks.

Forgetting to enable APIs is the most common first error when running Terraform translated from AWS.

## 399: How do you translate CloudWatch alarms and dashboards at scale?

- Export alarm definitions (from IaC or `describe-alarms`) and map each metric to its target equivalent. Many have no one-to-one match (Lambda `Throttles` has no equivalent on Workers).
- Prefer alerting on user-facing SLOs (error rate, latency percentiles) instead of copying every infrastructure alarm.
- Define alerts in code: Terraform `azurerm_monitor_metric_alert`, `google_monitoring_alert_policy`, or Cloudflare notification policies through Terraform.
- Rebuild dashboards in Azure Workbooks, Cloud Monitoring dashboards, or a shared Grafana that reads all providers.

Cloud Monitoring supports SLO objects with burn-rate alerts natively, and the migration is a good moment to move to SLO-based alerting on every provider.

## 400: How do you design SLOs that work across a hybrid migration?

- Measure at the edge, where users enter (Cloudflare, Front Door, global load balancer), so the SLO does not change when the backend moves.
- Use the same definitions on both sides: "99.9% of `GET /orders` requests return 2xx or 4xx in under 300 ms over 28 days".
- Track error budget burn during each migration wave, and pause waves when the budget runs low.
- Tag telemetry with the backend (`backend=aws` or `backend=gcp`) to compare old and new during weighted routing.

## 401: How would you build a real-time collaborative document editor on each platform?

- **AWS:** API Gateway WebSockets, Lambda for messages, DynamoDB for document state and connection IDs, and ElastiCache pub/sub or DynamoDB Streams to fan out. Ordering and conflicts are handled in your code (often with CRDTs like Yjs).
- **Azure:** Web PubSub (with the Yjs integration or groups per document), Functions for persistence, and Cosmos DB for snapshots.
- **GCP:** Cloud Run with WebSockets, session affinity, and Memorystore pub/sub between instances, plus Firestore for snapshots.
- **Cloudflare:** one Durable Object per document that holds connections, applies updates in order, and saves snapshots to its SQLite storage, with periodic copies to R2.

The Cloudflare version needs the fewest moving parts because one object owns the document. The others must coordinate across many stateless instances.

## 402: How would you handle inventory for a flash sale without overselling?

- **AWS:** DynamoDB conditional update `SET stock = stock - :q` with `ConditionExpression: stock >= :q`. Use SQS to queue orders if traffic exceeds the table's capacity.
- **Azure:** Cosmos DB patch with a filter predicate (`FROM c WHERE c.stock >= 1`) and `incr` by -1, or optimistic concurrency with ETags.
- **GCP:** a Firestore transaction (watch out for contention on one document), or Spanner for very high write rates on hot rows.
- **Cloudflare:** a Durable Object per product that decrements stock in memory and storage. Since it processes requests one at a time, overselling cannot happen.

**Cloudflare**

```ts
export class Inventory extends DurableObject {
  async reserve(qty: number): Promise<boolean> {
    const stock = (await this.ctx.storage.get<number>("stock")) ?? 0;
    if (stock < qty) return false;
    await this.ctx.storage.put("stock", stock - qty);
    return true;
  }
}
```

For extreme spikes on one product, shard stock across several objects or partition keys (for example 10 buckets of 100 items) and try another bucket when one is empty.

## 403: How would you build a global rate limiter?

- **AWS:** WAF rate-based rules for simple per-IP limits, or ElastiCache with a sliding window in Lambda for per-user limits (regional, not global).
- **Azure:** API Management `rate-limit-by-key` (per gateway instance in multi-region deployments), or Azure Managed Redis.
- **GCP:** Cloud Armor rate limiting at the edge, or Memorystore with a token bucket.
- **Cloudflare:** WAF rate limiting rules for edge limits, the Workers Rate Limiting binding (counts per location, fast and approximate), or a Durable Object per key for exact global counts.

Exact global limits need one place to count, which adds latency. Most systems accept approximate per-location limits for abuse protection and use exact counting only for billing or quotas.

## 404: How would you build a video platform on each provider?

- **AWS:** S3 uploads, MediaConvert for HLS and DASH renditions, IVS for live, CloudFront for delivery with signed URLs, and DynamoDB for metadata.
- **Azure:** Blob Storage uploads, a transcoding pipeline you run (FFmpeg on Container Apps jobs or Batch) or a partner service, Front Door delivery. Azure Media Services is retired.
- **GCP:** Cloud Storage, Transcoder API, Live Stream API, Media CDN, and Firestore for metadata.
- **Cloudflare:** Stream handles upload, encoding, storage, live and playback in one product, with signed tokens and a player. R2 + Workers if you want to manage files yourself.

Egress is usually the biggest cost in video, which is why Cloudflare Stream and R2 are popular for delivery even when processing stays on another cloud.

## 405: How would you ingest high-volume telemetry from devices?

- **AWS:** IoT Core (MQTT) or API Gateway, Kinesis Data Streams, Firehose to S3 and Timestream or Redshift.
- **Azure:** IoT Hub or Event Grid MQTT broker, Event Hubs, Stream Analytics, and Azure Data Explorer or Fabric Real-Time Intelligence.
- **GCP:** devices send through a partner MQTT broker or HTTPS to Cloud Run, then Pub/Sub, Dataflow and BigQuery.
- **Cloudflare:** HTTPS ingest to a Worker or straight to Pipelines, which batches events into Iceberg tables on R2.

Batch on the device side when you can. Per-message costs (requests, messages, operations) dominate at high volume on every provider.

## 406: How would you design a RAG chatbot on each platform?

| Layer          | AWS                               | Azure                    | GCP                         | Cloudflare                               |
| -------------- | --------------------------------- | ------------------------ | --------------------------- | ---------------------------------------- |
| Documents      | S3                                | Blob Storage             | Cloud Storage               | R2                                       |
| Ingest / chunk | Lambda or Bedrock Knowledge Bases | AI Search indexers       | RAG Engine or Cloud Run job | AI Search or Workflows                   |
| Embeddings     | Bedrock embedding models          | Foundry embedding models | Vertex AI embedding models  | Workers AI embedding models              |
| Vector store   | S3 Vectors / OpenSearch           | AI Search                | Vector Search / AlloyDB     | Vectorize                                |
| LLM            | Bedrock                           | Foundry (Azure OpenAI)   | Gemini on Vertex AI         | Workers AI or AI Gateway to any provider |
| Chat state     | DynamoDB                          | Cosmos DB                | Firestore                   | Durable Objects (Agents SDK)             |
| Guardrails     | Bedrock Guardrails                | AI Content Safety        | Model Armor                 | AI Gateway guardrails, Firewall for AI   |

The important design points are the same everywhere: chunking strategy, metadata filters for access control (users must only retrieve documents they can see), evaluation datasets, and caching repeated questions.

## 407: How would you design a SaaS app that keeps EU customer data in the EU?

- **AWS:** separate EU deployment in `eu-*` regions (or the AWS European Sovereign Cloud), SCP region restrictions, and a global routing layer that sends EU tenants to the EU stack.
- **Azure:** EU regions, Azure Policy allowed locations, EU Data Boundary, and Front Door routing by tenant.
- **GCP:** EU regions with `gcp.resourceLocations` set to `in:eu-locations`, Assured Workloads for EU regions and support, and a global load balancer routing by host.
- **Cloudflare:** jurisdiction `eu` on R2 buckets and Durable Objects, Regional Services so EU traffic is decrypted only in EU data centers, and Customer Metadata Boundary for logs.

Watch for hidden data flows: logs, backups, support tickets, AI model calls and analytics often leave the region by default.

## 408: How would you translate a nightly ETL pipeline?

- **AWS:** EventBridge Scheduler triggers Step Functions, which runs Glue jobs reading S3 and loading Redshift.
- **Azure:** a Data Factory pipeline with a schedule trigger, running data flows or Databricks or Fabric notebooks, loading Fabric Warehouse.
- **GCP:** Cloud Composer (managed Airflow) or Workflows with Cloud Scheduler, running Dataflow or BigQuery SQL (often ELT: load first, transform in BigQuery with Dataform).
- **Cloudflare:** small pipelines only: a Cron Trigger starts a Workflow that reads from APIs, writes to R2 and loads Iceberg tables. Heavy transforms belong elsewhere.

When moving to BigQuery, many Glue Spark jobs become simple SQL transformations, which is a big simplification.

## 409: How would you build a reliable webhook receiver?

The rule on every platform: accept fast, store, then process asynchronously.

- **AWS:** API Gateway or a Lambda function URL that verifies the signature and sends to SQS, then a consumer Lambda processes with a DLQ.
- **Azure:** an HTTP-triggered Function that verifies and sends to Service Bus, then a Service Bus-triggered Function.
- **GCP:** a Cloud Run function that verifies and publishes to Pub/Sub (or creates a Cloud Task), then a subscriber with a dead-letter topic.
- **Cloudflare:** a Worker that verifies the signature and sends to a Queue, then a consumer Worker with `max_retries` and a dead-letter queue.

**Cloudflare**

```ts
export default {
  async fetch(request: Request, env: Env) {
    const body = await request.text();
    if (
      !(await verifySignature(
        body,
        request.headers.get("x-signature"),
        env.WEBHOOK_SECRET,
      ))
    ) {
      return new Response("Bad signature", { status: 401 });
    }
    await env.WEBHOOKS.send({ body, receivedAt: Date.now() });
    return new Response("ok", { status: 202 });
  },
};
```

Store the provider's event ID and skip duplicates, because webhook senders retry.

## 410: How would you build a file sharing app with large uploads?

- Uploads go straight from the browser to storage with presigned multipart uploads (S3, R2), SAS with block uploads (Azure), or resumable upload sessions (GCS). The API never proxies the bytes.
- Metadata (owner, name, size, status) lives in DynamoDB, Cosmos DB, Firestore or D1.
- Upload completion triggers processing through storage events (S3 events, Event Grid, Eventarc, R2 notifications to Queues).
- Downloads use short-lived signed URLs or a Worker that checks permissions and streams from R2.
- For heavy egress, R2 removes most of the delivery cost.

Set lifecycle rules to abort incomplete multipart uploads, or failed uploads will keep costing storage on S3, R2 and GCS.

## 411: How would you build a B2B API with per-customer limits and mTLS?

- **AWS:** API Gateway with a custom domain and mutual TLS, usage plans with API keys per customer, and a Lambda authorizer mapping certificates to customers.
- **Azure:** API Management with client certificate validation, products and subscriptions per customer, and `rate-limit-by-key` on the subscription ID.
- **GCP:** Apigee with mTLS on the load balancer, API products and developer apps per customer, and Quota policies.
- **Cloudflare:** API Shield mTLS with client certificates per customer, a Worker that maps the certificate fingerprint (`request.cf.tlsClientAuth.certFingerprintSHA256`) to a customer, and the Rate Limiting binding keyed by customer.

## 412: How would you migrate a cron-heavy monolith running on EC2?

1. **List jobs:** read the crontab and scheduler config. Note duration, CPU, memory and dependencies for each.
2. **Short, light jobs:** move to timer-triggered Functions (Azure), Cloud Scheduler + Cloud Run functions (GCP), or Cron Triggers (Cloudflare).
3. **Long or heavy jobs:** move to Container Apps jobs, Cloud Run jobs (up to 24 hours per task), or Azure Batch / GCP Batch.
4. **Multi-step jobs:** use Durable Functions, GCP Workflows or Cloudflare Workflows so a failed step retries without rerunning everything.
5. **Overlap protection:** cron on one VM never ran twice at once by accident. In the cloud, add locks (a lease in Blob Storage, a Firestore document, or a Durable Object) or use schedulers that prevent overlap.
6. **Monitoring:** alert when a job does not run, not only when it fails.

## 413: How do you translate event sourcing?

- **AWS:** an events table in DynamoDB (aggregate ID as partition key, version as sort key, conditional writes to prevent version conflicts), with DynamoDB Streams to build read models.
- **Azure:** Cosmos DB container with aggregate ID as partition key, transactional batch for appending, and the change feed to build projections.
- **GCP:** Firestore subcollections per aggregate with transactions, or Spanner tables with change streams for high scale.
- **Cloudflare:** a Durable Object per aggregate that appends events to its SQLite storage and pushes them to a Queue for projections into D1.

The Durable Object version is natural for event sourcing, because the object is the single writer for its aggregate and never has version conflicts.

## 414: How do you translate CQRS read models?

- **AWS:** DynamoDB Streams or EventBridge feeding Lambda functions that update read stores (OpenSearch, another DynamoDB table, Aurora).
- **Azure:** Cosmos DB change feed processors (Functions) updating AI Search, another container with a different partition key, or SQL.
- **GCP:** Pub/Sub or Firestore triggers updating BigQuery, another Firestore collection or a Postgres replica.
- **Cloudflare:** Queues consumers updating D1 tables, KV entries for global cached reads, or Vectorize indexes.

All read models are eventually consistent. The UI should handle "your change will appear in a moment", or read from the write model right after a user's own change.

## 415: How do you translate durable timers at scale?

- **AWS:** EventBridge Scheduler one-time schedules (millions per account), or Step Functions `Wait` states.
- **Azure:** Durable Functions timers (`context.df.createTimer`), or Service Bus scheduled messages.
- **GCP:** Cloud Tasks with `scheduleTime` (up to 30 days ahead), or Workflows `sys.sleep`.
- **Cloudflare:** Durable Object alarms (one alarm per object, rescheduled as needed), or Workflows `step.sleep` and `step.sleepUntil`.

**Cloudflare**

```ts
export class Subscription extends DurableObject {
  async start(trialDays: number) {
    await this.ctx.storage.setAlarm(
      Date.now() + trialDays * 24 * 60 * 60 * 1000,
    );
  }
  async alarm() {
    await this.env.BILLING.send({
      id: this.ctx.id.toString(),
      event: "trial_ended",
    });
  }
}
```

## 416: How do you translate fan-out and fan-in?

**AWS**

```json
"ProcessAll": {
  "Type": "Map",
  "ItemsPath": "$.files",
  "MaxConcurrency": 20,
  "ItemProcessor": {
    "StartAt": "Process",
    "States": { "Process": { "Type": "Task", "Resource": "arn:aws:lambda:us-east-1:123456789012:function:process", "End": true } }
  },
  "End": true
}
```

**Azure**

```ts
df.app.orchestration("processAll", function* (context) {
  const files: string[] = context.df.getInput();
  const tasks = files.map((f) => context.df.callActivity("process", f));
  const results = yield context.df.Task.all(tasks);
  return results;
});
```

**GCP**

```yaml
- processAll:
    parallel:
      concurrency_limit: 20
      for:
        value: file
        in: ${files}
        steps:
          - process:
              call: http.post
              args: { url: https://process-abc123-uc.a.run.app, body: { file: ${file} }, auth: { type: OIDC } }
```

**Cloudflare**

```ts
const results = await Promise.all(
  event.payload.files.map((file) =>
    step.do(`process ${file}`, () => processFile(file)),
  ),
);
```

For very large fan-outs (millions of items), use Step Functions Distributed Map, Cloud Run jobs with many tasks, Azure Batch, or a Queue with many consumers, instead of one workflow holding all results.

## 417: How do you process millions of objects in parallel?

- **AWS:** Step Functions Distributed Map over an S3 prefix or inventory, or S3 Batch Operations for simple per-object actions.
- **Azure:** Azure Batch, or a Container Apps job with parallelism reading a work list from Service Bus.
- **GCP:** Cloud Run jobs with `--tasks 1000`. Each task reads `CLOUD_RUN_TASK_INDEX` and `CLOUD_RUN_TASK_COUNT` to pick its share.
- **Cloudflare:** list objects in a Worker or Workflow, send keys to a Queue in batches, and let consumers scale out automatically.

**GCP**

```ts
const index = Number(process.env.CLOUD_RUN_TASK_INDEX);
const count = Number(process.env.CLOUD_RUN_TASK_COUNT);
const mine = allKeys.filter((_, i) => i % count === index);
```

## 418: How do you design backpressure across these platforms?

- Put a queue between fast producers and slow consumers (SQS, Service Bus, Pub/Sub, Queues).
- Cap consumer concurrency to protect the database: Lambda event source mapping maximum concurrency, Functions `maxConcurrentCalls` in `host.json`, Pub/Sub flow control or Cloud Run max instances, Queues `max_concurrency`.
- Return `429` with `Retry-After` from APIs instead of letting requests pile up.
- Watch queue age, and scale or shed load before it grows without limit.

Serverless platforms scale up fast, which is great until the database behind them does not. Concurrency caps are the main backpressure tool.

## 419: How do you avoid retry storms after an outage?

- Use exponential backoff with jitter in every client (AWS SDK v3, Azure SDKs and Google client libraries do this by default, but your own `fetch` code does not).
- Limit retries at each layer. Three layers each retrying three times means 27 calls per request.
- Use circuit breakers in service-to-service calls, so a failing dependency gets time to recover.
- Make queue consumers back off: SQS visibility timeouts, Service Bus abandon with delay, Pub/Sub retry policy with min and max backoff, Queues `retry({ delaySeconds })`.
- After failover, ramp traffic back gradually with weighted routing.

## 420: How do timeout limits along the request path compare?

| Hop                         | Default or maximum timeout                                              |
| --------------------------- | ----------------------------------------------------------------------- |
| API Gateway (REST)          | 29 seconds by default (can be raised by request for regional APIs)      |
| API Gateway (HTTP API)      | 30 seconds maximum                                                      |
| Lambda                      | Up to 15 minutes                                                        |
| Azure Front Door            | Origin response timeout 60 seconds by default (configurable)            |
| Azure Functions HTTP        | About 230 seconds through the front end, regardless of function timeout |
| GCP external Application LB | Backend service timeout 30 seconds by default (configurable)            |
| Cloud Run                   | Request timeout up to 60 minutes                                        |
| Cloudflare proxy            | 100 seconds to the origin before a 524 error (higher on Enterprise)     |

Align timeouts so the outer layer waits slightly longer than the inner one. For work that takes longer than the shortest hop, switch to async: return `202` with a job ID and let the client poll or receive a webhook.

## 421: How do request and response size limits compare?

- **Lambda:** 6 MB request and response for synchronous invocations (response streaming allows larger responses), and 10 MB through API Gateway.
- **Azure Functions:** request size limits depend on the plan and host settings. Large files should go straight to Blob Storage.
- **Cloud Run:** 32 MiB request size over HTTP/1, with no limit for HTTP/2 streaming.
- **Cloudflare:** request body limit of 100 MB on Free and Pro, 200 MB on Business and 500 MB by default on Enterprise.

The design rule on every platform: do not send large files through your API. Use presigned or signed upload URLs.

## 422: How do you layer caching in a translated architecture?

1. **Browser cache:** `Cache-Control` and `ETag` headers, the same on every provider.
2. **CDN:** CloudFront, Front Door, Cloud CDN or Cloudflare, for static assets and cacheable API responses.
3. **Edge data:** Cloudflare KV or the Cache API for data needed in Workers. No direct equivalent on AWS except CloudFront KeyValueStore for small lookups in CloudFront Functions.
4. **Regional cache:** ElastiCache, Azure Managed Redis, Memorystore.
5. **Database caches:** DAX, Cosmos DB integrated cache, Hyperdrive query caching.

Each layer needs a clear invalidation rule. Most cache bugs after a migration come from the CDN layer, because default caching rules differ between providers.

## 423: How do you protect the origin from cache stampedes?

- **AWS:** CloudFront Origin Shield (an extra caching layer in one region) and request collapsing for identical requests.
- **Azure:** Front Door caching collapses concurrent requests for the same content at each edge.
- **GCP:** Cloud CDN request coalescing.
- **Cloudflare:** Tiered Cache (upper-tier data centers fetch from the origin for the others) and concurrent request collapsing, plus `stale-while-revalidate` support.

In application caches (Redis, KV), use a lock or "single flight" per key so only one request recomputes a missing value.

## 424: How do you serve stale content when the origin is down?

- **AWS:** CloudFront serves stale objects when the origin errors if `Cache-Control: stale-if-error` is set, and custom error responses can serve a static fallback from S3.
- **Azure:** Front Door does not serve stale on error, so use origin groups with a backup origin (for example a static site in Blob Storage).
- **GCP:** Cloud CDN serves stale content on origin errors up to `serveWhileStale` (and supports `stale-while-revalidate`).
- **Cloudflare:** Always Online and `stale-if-error`, or a Worker that falls back to a copy in KV or R2 when the origin fails.

## 425: How do you support custom domains for SaaS customers?

- **AWS:** CloudFront SaaS Manager (multi-tenant distributions with per-tenant domains and certificates), or ACM certificates per domain on a distribution.
- **Azure:** Front Door custom domains with managed certificates, added per customer through the API.
- **GCP:** Certificate Manager with DNS or load balancer authorization, and certificate maps on the load balancer.
- **Cloudflare:** Cloudflare for SaaS (custom hostnames), where customers CNAME to your zone and Cloudflare issues and renews certificates for them.

**Cloudflare**

```bash
curl -X POST "https://api.cloudflare.com/client/v4/zones/$ZONE_ID/custom_hostnames" \
  -H "Authorization: Bearer $CF_API_TOKEN" -H "Content-Type: application/json" \
  --data '{"hostname":"app.customer.com","ssl":{"method":"http","type":"dv"}}'
```

## 426: How do TLS settings compare at the edge?

- **Minimum TLS version:** CloudFront security policies (for example `TLSv1.2_2021`), Front Door minimum TLS version per domain, GCP SSL policies (`MODERN`, `RESTRICTED` or custom), Cloudflare Minimum TLS Version per zone.
- **HSTS:** response headers on CloudFront, Front Door rules or GCP custom headers, and a built-in HSTS setting on Cloudflare.
- **Post-quantum key agreement:** Cloudflare enables hybrid post-quantum key exchange by default for browsers that support it. The big clouds are adding support at their edges too, so check current docs per service.
- **Origin TLS:** CloudFront origin protocol policy, Front Door origin certificate checks, GCP backend protocol HTTPS, Cloudflare SSL mode Full (strict).

## 427: How do idle timeouts and long-lived connections differ?

- **AWS ALB:** idle timeout 60 seconds by default (up to 4,000). API Gateway WebSockets: 10-minute idle timeout and 2-hour maximum connection.
- **Azure:** Application Gateway and Front Door support WebSockets. Web PubSub manages long-lived connections for you.
- **GCP:** WebSocket connections on Cloud Run are limited by the request timeout (up to 60 minutes), so clients must reconnect.
- **Cloudflare:** WebSockets through the proxy have no fixed maximum duration but can be closed during network or Worker deploys, and Durable Objects with hibernation keep idle connections cheap.

Clients must reconnect automatically on every platform. Design for it rather than tuning timeouts.

## 428: How does gRPC support compare?

- **AWS:** ALB supports gRPC to targets, and ECS or EKS services run gRPC servers. API Gateway does not support gRPC.
- **Azure:** Container Apps and AKS support gRPC (HTTP/2 end to end). Application Gateway for Containers supports gRPC.
- **GCP:** Cloud Run supports gRPC (including streaming with HTTP/2), and the Application Load Balancer supports gRPC backends.
- **Cloudflare:** the proxy can pass gRPC to your origin (turn on gRPC in network settings). Workers can call gRPC-web or Connect-style APIs but cannot run a native gRPC server.

## 429: What happens to database connections after a failover, and how do you prepare?

- All clients lose connections at once and reconnect together, which can overload the new primary.
- DNS caches may still point at the old primary for the TTL, so clients connect to a read-only or dead host.

Preparation on every cloud:

- Use the provider's stable endpoint (Aurora cluster endpoint, Azure SQL failover group listener, Cloud SQL instance connection name through the connector, Hyperdrive in front of any of them).
- Set low DNS TTLs in clients and connection pools (some runtimes cache DNS forever by default).
- Reconnect with jittered backoff.
- Use a pooler (RDS Proxy, PgBouncer, Hyperdrive) that hides the reconnect storm from the database.

## 430: How do you run failover game days on each cloud?

- **AWS:** AWS Fault Injection Service experiments (stop instances, inject API errors, simulate AZ power interruption), plus ARC zonal shift to move traffic away from a zone.
- **Azure:** Azure Chaos Studio experiments (VM shutdown, NSG rules, AKS chaos via Chaos Mesh), and manual failover of failover groups and Cosmos DB regions.
- **GCP:** no managed chaos service. Use Chaos Mesh or Litmus on GKE, gcloud commands to fail over Cloud SQL and stop instances, and load balancer backend changes.
- **Cloudflare:** disable a Load Balancing pool or origin and watch failover, and test Worker fallbacks by blocking origins.

Run game days in production-like environments on a schedule, and fix runbooks based on what actually happens.

## 431: What cost traps catch teams after moving from AWS to Azure, GCP or Cloudflare?

- **Azure:** Log Analytics ingestion from verbose diagnostic settings, Premium SKUs chosen "to be safe" (Premium Functions plans, Premium Service Bus), NAT Gateway and Private Endpoint hourly charges per endpoint, and forgotten public IPs.
- **GCP:** Cloud Logging ingestion over the free allotment, inter-zone and inter-region traffic, Cloud NAT data processing, min instances left on in non-production, and BigQuery on-demand scans with `SELECT *`.
- **Cloudflare:** R2 Class A operations from chatty writes, Durable Objects duration when objects never sleep (use hibernation and short alarms), Workers Logs volume, and Queues operations per message.

Set budgets with alerts on day one of each new account, subscription or project.

## 432: How do you estimate Durable Objects costs compared with DynamoDB?

- **DynamoDB:** you pay per read and write request (on-demand) plus storage. A counter incremented 1 million times costs 1 million write requests.
- **Durable Objects:** you pay per request to the object, plus duration (GB-seconds while the object is active in memory), plus storage reads and writes (rows for SQLite-backed objects).

So a Durable Object that receives bursts and then sleeps is cheap, while one kept awake by a steady stream of requests or open WebSockets without hibernation pays duration all the time. Batching writes inside the object (for example flushing every second) can cut storage write costs a lot, which DynamoDB cannot do because every item update is its own request.

## 433: How do you tune Cosmos DB after migrating from DynamoDB?

- Measure RU charge per operation (the `x-ms-request-charge` header, or `requestCharge` in the SDK) for your top queries.
- Exclude paths you never query from the indexing policy. Indexing every field (the default) makes writes more expensive.
- Add composite indexes for queries with `ORDER BY` on several fields.
- Use point reads (`item(id, pk).read()`) instead of queries when you know the id and partition key. A 1 KB point read costs 1 RU.
- Choose session consistency unless you need stronger.
- Use autoscale throughput for spiky loads, or serverless for small, bursty apps.

## 434: What Firestore limits bite teams coming from DynamoDB?

- Maximum document size of 1 MiB (DynamoDB items are limited to 400 KB, so this rarely hurts).
- A sustained write rate to a single document of about one write per second. Counters need sharding (distributed counters).
- Index fan-out: every indexed field creates index entries, and documents with large arrays or maps can hit index entry limits.
- Queries need indexes for every combination of filters and sorts, created ahead of time.
- Transactions and batched writes are limited to 500 operations.

The one-write-per-second rule is the biggest surprise. Hot DynamoDB items with frequent updates need a different design on Firestore.

## 435: How do you design around D1's limits?

- Each database has a maximum size (10 GB on the paid plan), and an account can have many databases.
- Writes go to one primary, so very write-heavy workloads should be split across several databases.
- Queries have a time limit, so large scans and heavy reports belong in another system (R2 Data Catalog with R2 SQL, or an external warehouse).

The common pattern is one D1 database per tenant, per user or per shard key, with the Worker choosing the database binding or using the D1 REST API for dynamic databases. This "many small databases" design is the opposite of the AWS habit of one big RDS instance.

## 436: How do you design around Workers KV limits?

- Eventual consistency: writes take up to about a minute to appear everywhere. Do not use KV for data that must be read right after writing elsewhere.
- About one write per second per key. High-write keys need Durable Objects.
- Values up to 25 MiB, and metadata up to 1 KB.
- List operations are paged and slower than gets, so avoid listing on hot paths.
- Reads are fast in locations where the key is cached, and slower the first time a key is read in a location.

KV is ideal for config, feature flags, routing tables and cached API responses. It is a poor match for counters, carts or anything transactional.

## 437: How do you debug and profile Workers in production compared to Lambda?

- **Lambda:** CloudWatch Logs, X-Ray traces, Lambda Insights for memory and CPU, and CloudWatch Application Signals.
- **Workers:** Workers Logs with request details and CPU time per invocation, traces with automatic spans for bindings, `wrangler tail` for live logs, and the Chrome DevTools profiler through `wrangler dev` for local CPU profiling.

When a translated endpoint hits CPU limits on Workers, profile locally with DevTools, look for large JSON parsing, crypto in JavaScript instead of Web Crypto, and regex-heavy code.

## 438: How do you debug cloud functions locally with real cloud resources?

- **AWS:** `sam local invoke` or `sam local start-api` with your AWS profile, so the local code calls real DynamoDB or S3. LocalStack for fully local tests.
- **Azure:** `func start` with `local.settings.json` pointing to real resources, using your `az login` identity through `DefaultAzureCredential`.
- **GCP:** the Functions Framework with Application Default Credentials from `gcloud auth application-default login`.
- **Cloudflare:** `wrangler dev` uses local simulations by default. Set `"remote": true` on a binding to use the real KV, R2, D1 or Queue while the code runs locally, or run `wrangler dev --remote`.

## 439: How do you restructure a SAM or CDK project into a Cloudflare project?

**AWS**

```text
template.yaml        # functions, API, tables, queues
src/
  handlers/getUser.ts
  handlers/createOrder.ts
  handlers/processOrder.ts
```

**Cloudflare**

```text
wrangler.jsonc       # bindings: D1, KV, Queues, Workflows, Durable Objects
migrations/0001_init.sql
src/
  index.ts           # Hono app + queue() + scheduled() handlers
  routes/users.ts
  routes/orders.ts
  queues/processOrder.ts
  durable/Cart.ts
```

One Worker often replaces many Lambda functions, because a Worker exports several handlers (`fetch`, `queue`, `scheduled`) and routes requests internally. Split into separate Workers with service bindings only when teams, deploy cadence or limits require it.

## 440: How do on-call and operations change after the move?

- Runbooks must be rewritten: different consoles, CLI commands, metric names and failure modes.
- Alert routing changes (SNS to PagerDuty becomes Azure Monitor action groups, Cloud Monitoring notification channels, or Cloudflare Notifications webhooks).
- Support plans differ, so know how to open a severity-1 case with the new provider before you need it.
- Status pages and incident histories are different, so subscribe to the new provider's status feeds.
- Practice: run a small game day per critical system after migration, with the new runbooks.

## 441: How do you govern Cloudflare accounts and API tokens securely?

- Use SSO with your IdP and enforce 2FA for all members.
- Give members scoped roles (for example per zone or product) instead of Super Administrator.
- Use API tokens, not the legacy Global API Key, and scope each token to specific permissions, accounts or zones, IP ranges and an expiry.
- Store tokens in your CI secret store, and use separate tokens per pipeline.
- Watch Audit Logs (and push them with Logpush to your SIEM).
- Manage zone settings with Terraform so changes are reviewed.

## 442: What questions should you ask before choosing the target cloud?

- Where does the team's experience lie, and what does the company already use (Microsoft 365 and Entra ID point to Azure, BigQuery-heavy analytics point to GCP)?
- Which services does the app depend on most, and how good is each target's equivalent?
- What are the data residency, compliance and certification needs?
- What is the egress pattern? Heavy public egress favors Cloudflare R2 and the CDN.
- Are there credits, commitments or enterprise agreements that change the price?
- What is the latency target for global users? Edge platforms help a lot here.
- How much refactoring can the business afford, and in what time frame?

## 443: What are the most common mistakes when translating AWS to other clouds?

- Copying the AWS account and VPC layout one-to-one instead of using each cloud's model (resource groups, Shared VPC, global VPC).
- Treating Azure RBAC and GCP IAM like AWS policy JSON, and ending up with too-broad roles.
- Assuming the same limits and defaults (timeouts, cache rules, queue lock durations, function memory).
- Forgetting data-plane roles on Azure (being Owner does not let you read blobs or Cosmos DB data).
- Moving DynamoDB designs straight into relational databases or Firestore without redesigning access patterns.
- Porting Lambda code to Workers without checking CPU, memory and Node API use.
- Ignoring egress and logging costs on the target.
- Cutting over DNS without lowering TTLs or handling DNSSEC.

## 444: How do you explain the core difference between translating to Azure or GCP and translating to Cloudflare?

Translating to Azure or GCP is mostly **service mapping**: almost every AWS building block (VMs, VPCs, managed databases, queues, functions, Kubernetes) has a close equivalent, and the architecture can stay similar.

Translating to Cloudflare is mostly **re-architecture**: there are no regions to choose, no VPCs, no VMs and no managed Postgres. Compute runs on every location, state lives in Durable Objects, D1, KV and R2, and bindings replace IAM and network plumbing. In return, you get global low latency, no cold starts, no egress fees on R2, and much less infrastructure to manage.

That is why many companies use Cloudflare together with a hyperscaler instead of as a full replacement.

## 445: How do you translate IAM for a Cloudflare-based architecture that still calls AWS, Azure or GCP?

- Store narrowly scoped credentials for the other cloud as Worker secrets: an IAM user access key with a minimal policy (AWS), a service principal with a client secret or certificate (Azure), or a service account key (GCP). There is no workload identity federation from Workers yet, so these are long-lived.
- Reduce the risk: restrict by IP where possible (Workers have no fixed IPs, so this rarely works), rotate keys on a schedule, and limit each credential to one resource.
- Better: put a small API on the other cloud that accepts calls only from Cloudflare (mTLS with the Workers `mtls_certificates` binding, or Cloudflare Access service tokens through a Tunnel), and let that API use native identity to reach cloud services.

## 446: How do you handle secrets for Workers that need to sign requests to other clouds?

- **AWS:** use `aws4fetch` with an access key from Worker secrets.
- **Azure:** request an Entra token with the client credentials flow (`fetch` to `https://login.microsoftonline.com/<tenant>/oauth2/v2.0/token`), and cache it in memory or KV until it expires.
- **GCP:** sign a JWT with the service account private key using Web Crypto, and exchange it for an access token at `https://oauth2.googleapis.com/token`, then cache it.

**Cloudflare**

```ts
async function getAzureToken(env: Env): Promise<string> {
  const cached = (await env.TOKENS.get("azure", "json")) as {
    token: string;
    exp: number;
  } | null;
  if (cached && cached.exp > Date.now() + 60_000) return cached.token;
  const res = await fetch(
    `https://login.microsoftonline.com/${env.AZURE_TENANT_ID}/oauth2/v2.0/token`,
    {
      method: "POST",
      body: new URLSearchParams({
        grant_type: "client_credentials",
        client_id: env.AZURE_CLIENT_ID,
        client_secret: env.AZURE_CLIENT_SECRET,
        scope: "https://storage.azure.com/.default",
      }),
    },
  );
  const { access_token, expires_in } = (await res.json()) as {
    access_token: string;
    expires_in: number;
  };
  await env.TOKENS.put(
    "azure",
    JSON.stringify({
      token: access_token,
      exp: Date.now() + expires_in * 1000,
    }),
    {
      expirationTtl: Math.max(60, expires_in - 120),
    },
  );
  return access_token;
}
```

Caching tokens in KV shares them across locations, but KV is eventually consistent, so the code must also handle getting a fresh token when the cached one is missing.

## 447: How would you answer "Is multi-cloud worth it?" in an interview?

Multi-cloud is worth it when there is a clear reason:

- Best-of-breed services (BigQuery for analytics, Cloudflare for edge, Azure for Microsoft-centric identity).
- Regulatory or customer demands for a specific provider or region.
- A better negotiating position on large spend.
- An acquisition that brought another cloud.

It is not worth it as a vague resilience strategy for most teams: running the same app actively on two clouds doubles operational work, skills and testing, and provider-wide outages are rare compared to your own deploy mistakes. A common, practical form is "one main cloud plus Cloudflare at the edge", which gets real benefits without duplicating everything.

## 448: How do you keep a translated system from drifting back into provider-specific code everywhere?

- Keep cloud SDK calls inside adapter modules (`storage/r2.ts`, `storage/s3.ts`) with one interface, and test the interface.
- Use standard formats: OpenTelemetry for telemetry, CloudEvents for events, OIDC and JWT for auth, SQL for relational data.
- Document which services are intentionally provider-specific (for example Durable Objects or Spanner) and why.
- Review new dependencies on proprietary services in architecture reviews, so lock-in is a decision, not an accident.

## 449: Can you summarize which AWS services have no equivalent on each provider?

| AWS service             | Missing on Azure                  | Missing on GCP         | Missing on Cloudflare                                   |
| ----------------------- | --------------------------------- | ---------------------- | ------------------------------------------------------- |
| EC2, VPC, EKS           | No                                | No                     | Yes (no VMs, VPCs or Kubernetes)                        |
| RDS / Aurora            | No                                | No                     | Yes (D1 is SQLite; Hyperdrive connects to external DBs) |
| SES (sending)           | No (Communication Services Email) | Yes (use a partner)    | Partly (Email Service in beta)                          |
| IoT Core                | No                                | Yes (retired)          | Yes                                                     |
| Cognito                 | No (Entra External ID)            | No (Identity Platform) | Yes (Access is for internal apps)                       |
| SNS / EventBridge       | No                                | No                     | Yes (no topics or event bus)                            |
| KMS                     | No                                | No                     | Yes (no general KMS for app data)                       |
| SageMaker               | No                                | No                     | Yes (inference only via Workers AI)                     |
| Media services          | Yes (Media Services retired)      | No                     | No (Stream)                                             |
| Fault Injection Service | No (Chaos Studio)                 | Yes                    | Yes                                                     |

The answer to "what if there is no equivalent?" is always one of: use a partner or open-source service, keep that piece on the original cloud, or redesign so the feature is not needed.

## 450: What principles make a good AWS translation?

1. **Translate behavior, not resources.** Start from what users and other systems need, then pick the target's best way to provide it.
2. **Use each platform's native model** (resource groups and RBAC on Azure, projects and service accounts on GCP, bindings and Durable Objects on Cloudflare) instead of copying AWS patterns.
3. **Build the foundation first:** identity, networking, logging, policies and CI/CD.
4. **Move data carefully:** continuous replication, validation and a tested rollback.
5. **Measure at the edge:** SLOs, shadow traffic and weighted routing make the cut-over safe.
6. **Watch the new cost model** from day one.
7. **Prefer open standards** (Postgres, Kubernetes, OpenTelemetry, OIDC, S3 API, CloudEvents) where they do not cost you important features.
8. **Write it down:** a service mapping table, the known gaps and the decisions made for each one, so the next team understands why the system looks the way it does.
