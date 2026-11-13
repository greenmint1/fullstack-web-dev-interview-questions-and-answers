# AWS Security Interview Questions and Answers

_Last updated: November 13, 2026_

450 interview questions and answers about security on AWS: 150 easy, 150 moderate and 150 advanced. They cover IAM, accounts and organizations, encryption, network security, the security services (GuardDuty, Security Hub, Config and others), incident response and secure CI/CD. The answers match AWS features and service names as of late 2026, including Security Hub CSPM, resource control policies, EKS Pod Identity and centralized root access.

## Table of Contents

- [Easy Questions (1-150)](#easy-questions-1-150)
- [Moderate Questions (151-300)](#moderate-questions-151-300)
- [Advanced Questions (301-450)](#advanced-questions-301-450)

### Easy Questions (1-150)

- [1: What is the AWS shared responsibility model?](#1-what-is-the-aws-shared-responsibility-model)
- [2: How does your share of the work change between EC2, RDS and Lambda?](#2-how-does-your-share-of-the-work-change-between-ec2-rds-and-lambda)
- [3: What is the root user in an AWS account?](#3-what-is-the-root-user-in-an-aws-account)
- [4: How do you protect the root user?](#4-how-do-you-protect-the-root-user)
- [5: Which tasks still need the root user?](#5-which-tasks-still-need-the-root-user)
- [6: What MFA types does AWS support?](#6-what-mfa-types-does-aws-support)
- [7: What is AWS IAM?](#7-what-is-aws-iam)
- [8: What is an IAM user?](#8-what-is-an-iam-user)
- [9: What is an IAM group?](#9-what-is-an-iam-group)
- [10: What is an IAM role?](#10-what-is-an-iam-role)
- [11: What is the difference between an IAM user and an IAM role?](#11-what-is-the-difference-between-an-iam-user-and-an-iam-role)
- [12: What does an IAM policy look like?](#12-what-does-an-iam-policy-look-like)
- [13: What are the main elements of a policy statement?](#13-what-are-the-main-elements-of-a-policy-statement)
- [14: What is the difference between AWS managed, customer managed and inline policies?](#14-what-is-the-difference-between-aws-managed-customer-managed-and-inline-policies)
- [15: What is an ARN?](#15-what-is-an-arn)
- [16: What is the difference between identity-based and resource-based policies?](#16-what-is-the-difference-between-identity-based-and-resource-based-policies)
- [17: What does least privilege mean on AWS?](#17-what-does-least-privilege-mean-on-aws)
- [18: What is an implicit deny?](#18-what-is-an-implicit-deny)
- [19: What is an explicit deny?](#19-what-is-an-explicit-deny)
- [20: What are access keys and why are long-lived ones risky?](#20-what-are-access-keys-and-why-are-long-lived-ones-risky)
- [21: How do you rotate an IAM user's access key without downtime?](#21-how-do-you-rotate-an-iam-users-access-key-without-downtime)
- [22: What is an IAM password policy?](#22-what-is-an-iam-password-policy)
- [23: What is AWS STS?](#23-what-is-aws-sts)
- [24: What do temporary credentials consist of?](#24-what-do-temporary-credentials-consist-of)
- [25: What does AssumeRole do?](#25-what-does-assumerole-do)
- [26: What is a role trust policy?](#26-what-is-a-role-trust-policy)
- [27: What is an EC2 instance profile?](#27-what-is-an-ec2-instance-profile)
- [28: Why should you not put access keys on an EC2 instance?](#28-why-should-you-not-put-access-keys-on-an-ec2-instance)
- [29: What is a service-linked role?](#29-what-is-a-service-linked-role)
- [30: What is IAM Access Analyzer?](#30-what-is-iam-access-analyzer)
- [31: What is the IAM credential report?](#31-what-is-the-iam-credential-report)
- [32: What is IAM Identity Center?](#32-what-is-iam-identity-center)
- [33: What is identity federation?](#33-what-is-identity-federation)
- [34: What is AWS Organizations?](#34-what-is-aws-organizations)
- [35: What is a service control policy (SCP)?](#35-what-is-a-service-control-policy-scp)
- [36: What is AWS Control Tower?](#36-what-is-aws-control-tower)
- [37: Why do companies use multiple AWS accounts?](#37-why-do-companies-use-multiple-aws-accounts)
- [38: What is Amazon Cognito?](#38-what-is-amazon-cognito)
- [39: What is the difference between a Cognito user pool and an identity pool?](#39-what-is-the-difference-between-a-cognito-user-pool-and-an-identity-pool)
- [40: What tokens does a Cognito user pool issue?](#40-what-tokens-does-a-cognito-user-pool-issue)
- [41: What is AWS Secrets Manager?](#41-what-is-aws-secrets-manager)
- [42: What is SSM Parameter Store and what is a SecureString?](#42-what-is-ssm-parameter-store-and-what-is-a-securestring)
- [43: What is AWS KMS?](#43-what-is-aws-kms)
- [44: What is the difference between customer managed, AWS managed and AWS owned KMS keys?](#44-what-is-the-difference-between-customer-managed-aws-managed-and-aws-owned-kms-keys)
- [45: What does encryption at rest mean?](#45-what-does-encryption-at-rest-mean)
- [46: What does encryption in transit mean?](#46-what-does-encryption-in-transit-mean)
- [47: What is AWS Certificate Manager (ACM)?](#47-what-is-aws-certificate-manager-acm)
- [48: What is AWS CloudHSM?](#48-what-is-aws-cloudhsm)
- [49: What is S3 Block Public Access?](#49-what-is-s3-block-public-access)
- [50: What is an S3 bucket policy?](#50-what-is-an-s3-bucket-policy)
- [51: What is an S3 presigned URL?](#51-what-is-an-s3-presigned-url)
- [52: What server-side encryption options does S3 support?](#52-what-server-side-encryption-options-does-s3-support)
- [53: What is S3 versioning and why does it matter for security?](#53-what-is-s3-versioning-and-why-does-it-matter-for-security)
- [54: What is S3 Object Lock?](#54-what-is-s3-object-lock)
- [55: What are S3 ACLs and Object Ownership?](#55-what-are-s3-acls-and-object-ownership)
- [56: What is a VPC?](#56-what-is-a-vpc)
- [57: What is the difference between a public and a private subnet?](#57-what-is-the-difference-between-a-public-and-a-private-subnet)
- [58: What is a security group?](#58-what-is-a-security-group)
- [59: What is a network ACL?](#59-what-is-a-network-acl)
- [60: How do security groups and NACLs differ?](#60-how-do-security-groups-and-nacls-differ)
- [61: What is a NAT gateway?](#61-what-is-a-nat-gateway)
- [62: What is a VPC endpoint?](#62-what-is-a-vpc-endpoint)
- [63: What is AWS PrivateLink?](#63-what-is-aws-privatelink)
- [64: What are VPC Flow Logs?](#64-what-are-vpc-flow-logs)
- [65: What is a bastion host and why do many teams stop using one?](#65-what-is-a-bastion-host-and-why-do-many-teams-stop-using-one)
- [66: What is Systems Manager Session Manager?](#66-what-is-systems-manager-session-manager)
- [67: What is Systems Manager Patch Manager?](#67-what-is-systems-manager-patch-manager)
- [68: What is AWS WAF?](#68-what-is-aws-waf)
- [69: What are AWS WAF managed rule groups?](#69-what-are-aws-waf-managed-rule-groups)
- [70: What is a rate-based rule in AWS WAF?](#70-what-is-a-rate-based-rule-in-aws-waf)
- [71: What is AWS Shield Standard?](#71-what-is-aws-shield-standard)
- [72: What is AWS Shield Advanced?](#72-what-is-aws-shield-advanced)
- [73: How does AWS help you handle DDoS attacks?](#73-how-does-aws-help-you-handle-ddos-attacks)
- [74: What basic security settings should a CloudFront distribution have?](#74-what-basic-security-settings-should-a-cloudfront-distribution-have)
- [75: What is CloudFront Origin Access Control (OAC)?](#75-what-is-cloudfront-origin-access-control-oac)
- [76: What is the difference between CloudFront signed URLs and signed cookies?](#76-what-is-the-difference-between-cloudfront-signed-urls-and-signed-cookies)
- [77: What authorization options does API Gateway have?](#77-what-authorization-options-does-api-gateway-have)
- [78: What is a Lambda execution role?](#78-what-is-a-lambda-execution-role)
- [79: What is a Lambda resource-based policy?](#79-what-is-a-lambda-resource-based-policy)
- [80: How are Lambda environment variables protected?](#80-how-are-lambda-environment-variables-protected)
- [81: What auth types can a Lambda function URL use?](#81-what-auth-types-can-a-lambda-function-url-use)
- [82: What does ECR image scanning do?](#82-what-does-ecr-image-scanning-do)
- [83: What is the difference between an ECS task role and a task execution role?](#83-what-is-the-difference-between-an-ecs-task-role-and-a-task-execution-role)
- [84: How does Fargate isolate workloads?](#84-how-does-fargate-isolate-workloads)
- [85: How do you encrypt an RDS database?](#85-how-do-you-encrypt-an-rds-database)
- [86: How do you keep an RDS database off the internet?](#86-how-do-you-keep-an-rds-database-off-the-internet)
- [87: How is DynamoDB data encrypted?](#87-how-is-dynamodb-data-encrypted)
- [88: What is IAM database authentication?](#88-what-is-iam-database-authentication)
- [89: What is AWS CloudTrail?](#89-what-is-aws-cloudtrail)
- [90: What is the difference between CloudTrail management events and data events?](#90-what-is-the-difference-between-cloudtrail-management-events-and-data-events)
- [91: What is CloudTrail event history and why is it not enough?](#91-what-is-cloudtrail-event-history-and-why-is-it-not-enough)
- [92: What is CloudWatch Logs used for in security?](#92-what-is-cloudwatch-logs-used-for-in-security)
- [93: How do you get alerted when someone signs in as root?](#93-how-do-you-get-alerted-when-someone-signs-in-as-root)
- [94: What is AWS Config?](#94-what-is-aws-config)
- [95: What is the difference between managed and custom Config rules?](#95-what-is-the-difference-between-managed-and-custom-config-rules)
- [96: What is Amazon GuardDuty?](#96-what-is-amazon-guardduty)
- [97: What is AWS Security Hub?](#97-what-is-aws-security-hub)
- [98: What is Amazon Inspector?](#98-what-is-amazon-inspector)
- [99: What is Amazon Macie?](#99-what-is-amazon-macie)
- [100: What is Amazon Detective?](#100-what-is-amazon-detective)
- [101: What is Amazon Security Lake?](#101-what-is-amazon-security-lake)
- [102: How is EventBridge used for security?](#102-how-is-eventbridge-used-for-security)
- [103: What security checks does AWS Trusted Advisor do?](#103-what-security-checks-does-aws-trusted-advisor-do)
- [104: What is AWS Artifact?](#104-what-is-aws-artifact)
- [105: What is AWS Audit Manager?](#105-what-is-aws-audit-manager)
- [106: Does using AWS make your app HIPAA or PCI compliant?](#106-does-using-aws-make-your-app-hipaa-or-pci-compliant)
- [107: What is AWS Backup?](#107-what-is-aws-backup)
- [108: What is AWS Backup Vault Lock?](#108-what-is-aws-backup-vault-lock)
- [109: What is attribute-based access control (ABAC) on AWS?](#109-what-is-attribute-based-access-control-abac-on-aws)
- [110: What is a permissions boundary?](#110-what-is-a-permissions-boundary)
- [111: What is a session policy?](#111-what-is-a-session-policy)
- [112: What is the Security Pillar of the AWS Well-Architected Framework?](#112-what-is-the-security-pillar-of-the-aws-well-architected-framework)
- [113: What are the design principles of the Security Pillar?](#113-what-are-the-design-principles-of-the-security-pillar)
- [114: What is AWS Network Firewall?](#114-what-is-aws-network-firewall)
- [115: What is Route 53 Resolver DNS Firewall?](#115-what-is-route-53-resolver-dns-firewall)
- [116: What is the EC2 instance metadata service and what is IMDSv2?](#116-what-is-the-ec2-instance-metadata-service-and-what-is-imdsv2)
- [117: What is a data perimeter?](#117-what-is-a-data-perimeter)
- [118: What are the two basic ways to give another account access to your resources?](#118-what-are-the-two-basic-ways-to-give-another-account-access-to-your-resources)
- [119: How do pods in EKS get AWS permissions?](#119-how-do-pods-in-eks-get-aws-permissions)
- [120: What is AWS Firewall Manager?](#120-what-is-aws-firewall-manager)
- [121: What is the IAM policy simulator?](#121-what-is-the-iam-policy-simulator)
- [122: How do you check which identity your CLI is using?](#122-how-do-you-check-which-identity-your-cli-is-using)
- [123: Where should you never store AWS secrets?](#123-where-should-you-never-store-aws-secrets)
- [124: What happens when AWS finds your access key on public GitHub?](#124-what-happens-when-aws-finds-your-access-key-on-public-github)
- [125: What does defense in depth mean on AWS?](#125-what-does-defense-in-depth-mean-on-aws)
- [126: Why reference security groups instead of IP addresses?](#126-why-reference-security-groups-instead-of-ip-addresses)
- [127: What is AWS Private Certificate Authority?](#127-what-is-aws-private-certificate-authority)
- [128: How do you force clients to use TLS when calling AWS services?](#128-how-do-you-force-clients-to-use-tls-when-calling-aws-services)
- [129: How do you make sure S3 objects are always encrypted with your KMS key?](#129-how-do-you-make-sure-s3-objects-are-always-encrypted-with-your-kms-key)
- [130: What is CloudTrail log file integrity validation?](#130-what-is-cloudtrail-log-file-integrity-validation)
- [131: What is an organization trail?](#131-what-is-an-organization-trail)
- [132: What does AWS Systems Manager offer for security?](#132-what-does-aws-systems-manager-offer-for-security)
- [133: What is the difference between GuardDuty, Inspector and Macie?](#133-what-is-the-difference-between-guardduty-inspector-and-macie)
- [134: What should every new AWS account have turned on?](#134-what-should-every-new-aws-account-have-turned-on)
- [135: What is AWS Security Incident Response?](#135-what-is-aws-security-incident-response)
- [136: How does infrastructure as code help security?](#136-how-does-infrastructure-as-code-help-security)
- [137: What tools scan IaC for security problems?](#137-what-tools-scan-iac-for-security-problems)
- [138: How does GitHub Actions authenticate to AWS without access keys?](#138-how-does-github-actions-authenticate-to-aws-without-access-keys)
- [139: Why is OIDC better than storing access keys in CI secrets?](#139-why-is-oidc-better-than-storing-access-keys-in-ci-secrets)
- [140: What is a deploy role?](#140-what-is-a-deploy-role)
- [141: What are common S3 security mistakes?](#141-what-are-common-s3-security-mistakes)
- [142: What are common IAM mistakes?](#142-what-are-common-iam-mistakes)
- [143: Do you need permission from AWS to run a penetration test?](#143-do-you-need-permission-from-aws-to-run-a-penetration-test)
- [144: What is the difference between CloudTrail and CloudWatch?](#144-what-is-the-difference-between-cloudtrail-and-cloudwatch)
- [145: What is a KMS key policy?](#145-what-is-a-kms-key-policy)
- [146: How does KMS key rotation work?](#146-how-does-kms-key-rotation-work)
- [147: How does Secrets Manager rotation work?](#147-how-does-secrets-manager-rotation-work)
- [148: How can you add MFA to a Cognito user pool?](#148-how-can-you-add-mfa-to-a-cognito-user-pool)
- [149: What are AWS managed job function policies?](#149-what-are-aws-managed-job-function-policies)
- [150: What is a break-glass account?](#150-what-is-a-break-glass-account)

### Moderate Questions (151-300)

- [151: How does IAM decide whether to allow a request in a single account?](#151-how-does-iam-decide-whether-to-allow-a-request-in-a-single-account)
- [152: How is policy evaluation different for cross-account requests?](#152-how-is-policy-evaluation-different-for-cross-account-requests)
- [153: How do SCPs combine with IAM policies?](#153-how-do-scps-combine-with-iam-policies)
- [154: What are resource control policies (RCPs)?](#154-what-are-resource-control-policies-rcps)
- [155: What is the difference between an allow-list and a deny-list SCP strategy?](#155-what-is-the-difference-between-an-allow-list-and-a-deny-list-scp-strategy)
- [156: How do you write an SCP that limits which regions can be used?](#156-how-do-you-write-an-scp-that-limits-which-regions-can-be-used)
- [157: How do you use a permissions boundary to let developers create roles safely?](#157-how-do-you-use-a-permissions-boundary-to-let-developers-create-roles-safely)
- [158: What is iam:PassRole and why is it dangerous?](#158-what-is-iampassrole-and-why-is-it-dangerous)
- [159: Which condition operators should you know?](#159-which-condition-operators-should-you-know)
- [160: What are policy variables?](#160-what-are-policy-variables)
- [161: What are the risks of NotAction and NotResource?](#161-what-are-the-risks-of-notaction-and-notresource)
- [162: How do you require MFA for sensitive actions?](#162-how-do-you-require-mfa-for-sensitive-actions)
- [163: How do you set up a role that a third-party SaaS vendor can assume?](#163-how-do-you-set-up-a-role-that-a-third-party-saas-vendor-can-assume)
- [164: What is the confused deputy problem?](#164-what-is-the-confused-deputy-problem)
- [165: How do you prevent the confused deputy problem with AWS service principals?](#165-how-do-you-prevent-the-confused-deputy-problem-with-aws-service-principals)
- [166: What is role chaining and what limits it?](#166-what-is-role-chaining-and-what-limits-it)
- [167: How long can a role session last?](#167-how-long-can-a-role-session-last)
- [168: What are session tags?](#168-what-are-session-tags)
- [169: What is sts:SourceIdentity?](#169-what-is-stssourceidentity)
- [170: How does AssumeRoleWithWebIdentity work?](#170-how-does-assumerolewithwebidentity-work)
- [171: How does SAML federation to AWS work?](#171-how-does-saml-federation-to-aws-work)
- [172: What are permission sets in IAM Identity Center?](#172-what-are-permission-sets-in-iam-identity-center)
- [173: How do you connect IAM Identity Center to an external identity provider?](#173-how-do-you-connect-iam-identity-center-to-an-external-identity-provider)
- [174: How do you use attributes from your IdP for access control in Identity Center?](#174-how-do-you-use-attributes-from-your-idp-for-access-control-in-identity-center)
- [175: How do you use IAM Access Analyzer to move toward least privilege?](#175-how-do-you-use-iam-access-analyzer-to-move-toward-least-privilege)
- [176: How can you check IAM policies in a CI pipeline?](#176-how-can-you-check-iam-policies-in-a-ci-pipeline)
- [177: How do you use "last accessed" information?](#177-how-do-you-use-last-accessed-information)
- [178: What kinds of controls does Control Tower have?](#178-what-kinds-of-controls-does-control-tower-have)
- [179: What OU structure does AWS recommend for a landing zone?](#179-what-ou-structure-does-aws-recommend-for-a-landing-zone)
- [180: What is a delegated administrator and why use one?](#180-what-is-a-delegated-administrator-and-why-use-one)
- [181: What is Account Factory for Terraform (AFT)?](#181-what-is-account-factory-for-terraform-aft)
- [182: How should a backend validate a Cognito access token?](#182-how-should-a-backend-validate-a-cognito-access-token)
- [183: How do Cognito identity pools choose an IAM role?](#183-how-do-cognito-identity-pools-choose-an-iam-role)
- [184: How can Cognito Lambda triggers improve security?](#184-how-can-cognito-lambda-triggers-improve-security)
- [185: Should a browser app use a Cognito app client secret?](#185-should-a-browser-app-use-a-cognito-app-client-secret)
- [186: Where should a web app store tokens from Cognito?](#186-where-should-a-web-app-store-tokens-from-cognito)
- [187: How do you enforce IMDSv2 across your accounts?](#187-how-do-you-enforce-imdsv2-across-your-accounts)
- [188: Why does the IMDS hop limit matter for containers?](#188-why-does-the-imds-hop-limit-matter-for-containers)
- [189: How do you set up IRSA for an EKS pod?](#189-how-do-you-set-up-irsa-for-an-eks-pod)
- [190: What are the advantages of EKS Pod Identity over IRSA?](#190-what-are-the-advantages-of-eks-pod-identity-over-irsa)
- [191: How do you stop ECS tasks on EC2 from using the instance role?](#191-how-do-you-stop-ecs-tasks-on-ec2-from-using-the-instance-role)
- [192: When do you choose Secrets Manager versus Parameter Store?](#192-when-do-you-choose-secrets-manager-versus-parameter-store)
- [193: How do you inject secrets into an ECS task?](#193-how-do-you-inject-secrets-into-an-ecs-task)
- [194: How should a Lambda function read secrets efficiently?](#194-how-should-a-lambda-function-read-secrets-efficiently)
- [195: How do you share a Secrets Manager secret with another account?](#195-how-do-you-share-a-secrets-manager-secret-with-another-account)
- [196: What is envelope encryption?](#196-what-is-envelope-encryption)
- [197: When do you use GenerateDataKey instead of Encrypt?](#197-when-do-you-use-generatedatakey-instead-of-encrypt)
- [198: What are KMS grants?](#198-what-are-kms-grants)
- [199: What is a KMS encryption context?](#199-what-is-a-kms-encryption-context)
- [200: What does a well-structured KMS key policy look like?](#200-what-does-a-well-structured-kms-key-policy-look-like)
- [201: What does the kms:ViaService condition do?](#201-what-does-the-kmsviaservice-condition-do)
- [202: What are KMS multi-Region keys?](#202-what-are-kms-multi-region-keys)
- [203: What happens when you delete a KMS key?](#203-what-happens-when-you-delete-a-kms-key)
- [204: What key types does KMS support besides symmetric keys?](#204-what-key-types-does-kms-support-besides-symmetric-keys)
- [205: What is an S3 Bucket Key?](#205-what-is-an-s3-bucket-key)
- [206: How do KMS, CloudHSM, custom key stores and external key stores compare?](#206-how-do-kms-cloudhsm-custom-key-stores-and-external-key-stores-compare)
- [207: What should you know about ACM certificates for CloudFront?](#207-what-should-you-know-about-acm-certificates-for-cloudfront)
- [208: Where should TLS be terminated in a typical AWS web app?](#208-where-should-tls-be-terminated-in-a-typical-aws-web-app)
- [209: How do you make sure all EBS volumes are encrypted?](#209-how-do-you-make-sure-all-ebs-volumes-are-encrypted)
- [210: How do you share an encrypted EBS snapshot or AMI with another account?](#210-how-do-you-share-an-encrypted-ebs-snapshot-or-ami-with-another-account)
- [211: What are S3 Access Points and why do they help security?](#211-what-are-s3-access-points-and-why-do-they-help-security)
- [212: How do you give another account access to an S3 bucket?](#212-how-do-you-give-another-account-access-to-an-s3-bucket)
- [213: What are the security pitfalls of presigned URLs?](#213-what-are-the-security-pitfalls-of-presigned-urls)
- [214: What is the difference between S3 server access logs and CloudTrail data events?](#214-what-is-the-difference-between-s3-server-access-logs-and-cloudtrail-data-events)
- [215: How can S3 replication protect against data loss or attack?](#215-how-can-s3-replication-protect-against-data-loss-or-attack)
- [216: What is MFA Delete in S3 and what are its limits?](#216-what-is-mfa-delete-in-s3-and-what-are-its-limits)
- [217: How would you design security groups for a three-tier web app?](#217-how-would-you-design-security-groups-for-a-three-tier-web-app)
- [218: Why do NACLs need ephemeral port rules?](#218-why-do-nacls-need-ephemeral-port-rules)
- [219: What is a VPC endpoint policy and how do you use it for S3?](#219-what-is-a-vpc-endpoint-policy-and-how-do-you-use-it-for-s3)
- [220: What does private DNS on an interface endpoint do?](#220-what-does-private-dns-on-an-interface-endpoint-do)
- [221: What is the difference between aws:SourceVpce, aws:SourceVpc and aws:SourceIp?](#221-what-is-the-difference-between-awssourcevpce-awssourcevpc-and-awssourceip)
- [222: How can you control outbound internet traffic from a VPC?](#222-how-can-you-control-outbound-internet-traffic-from-a-vpc)
- [223: How do you analyze VPC Flow Logs?](#223-how-do-you-analyze-vpc-flow-logs)
- [224: What is VPC Traffic Mirroring?](#224-what-is-vpc-traffic-mirroring)
- [225: How do VPC peering and Transit Gateway differ from a security point of view?](#225-how-do-vpc-peering-and-transit-gateway-differ-from-a-security-point-of-view)
- [226: How are rules evaluated in an AWS WAF web ACL?](#226-how-are-rules-evaluated-in-an-aws-waf-web-acl)
- [227: What does AWS WAF Bot Control do?](#227-what-does-aws-waf-bot-control-do)
- [228: How do WAF labels and logging help?](#228-how-do-waf-labels-and-logging-help)
- [229: What is the difference between the CAPTCHA and Challenge actions in WAF?](#229-what-is-the-difference-between-the-captcha-and-challenge-actions-in-waf)
- [230: What are WAF Account Takeover Prevention and Account Creation Fraud Prevention?](#230-what-are-waf-account-takeover-prevention-and-account-creation-fraud-prevention)
- [231: What does the Shield Response Team do?](#231-what-does-the-shield-response-team-do)
- [232: How do you stop people from bypassing CloudFront and hitting your ALB directly?](#232-how-do-you-stop-people-from-bypassing-cloudfront-and-hitting-your-alb-directly)
- [233: What is CloudFront field-level encryption?](#233-what-is-cloudfront-field-level-encryption)
- [234: How do you restrict content by country in CloudFront?](#234-how-do-you-restrict-content-by-country-in-cloudfront)
- [235: Which security headers should you add with a CloudFront response headers policy?](#235-which-security-headers-should-you-add-with-a-cloudfront-response-headers-policy)
- [236: What is the difference between TOKEN and REQUEST Lambda authorizers?](#236-what-is-the-difference-between-token-and-request-lambda-authorizers)
- [237: How do you make an API Gateway REST API private?](#237-how-do-you-make-an-api-gateway-rest-api-private)
- [238: How does API Gateway throttling protect your backend?](#238-how-does-api-gateway-throttling-protect-your-backend)
- [239: How does mutual TLS work in API Gateway?](#239-how-does-mutual-tls-work-in-api-gateway)
- [240: How does a client call an API Gateway API protected with IAM auth?](#240-how-does-a-client-call-an-api-gateway-api-protected-with-iam-auth)
- [241: When should a Lambda function run inside a VPC?](#241-when-should-a-lambda-function-run-inside-a-vpc)
- [242: What is Lambda code signing?](#242-what-is-lambda-code-signing)
- [243: What are the security risks of Lambda layers?](#243-what-are-the-security-risks-of-lambda-layers)
- [244: How do you put CloudFront in front of a Lambda function URL securely?](#244-how-do-you-put-cloudfront-in-front-of-a-lambda-function-url-securely)
- [245: What container settings make ECS tasks more secure?](#245-what-container-settings-make-ecs-tasks-more-secure)
- [246: How does access control work in EKS?](#246-how-does-access-control-work-in-eks)
- [247: How should the EKS API server endpoint be exposed?](#247-how-should-the-eks-api-server-endpoint-be-exposed)
- [248: How do you secure Amazon ECR repositories?](#248-how-do-you-secure-amazon-ecr-repositories)
- [249: How can you sign and verify container images on AWS?](#249-how-can-you-sign-and-verify-container-images-on-aws)
- [250: What does GuardDuty Runtime Monitoring add?](#250-what-does-guardduty-runtime-monitoring-add)
- [251: How do you force TLS connections to RDS?](#251-how-do-you-force-tls-connections-to-rds)
- [252: How can RDS manage the master password for you?](#252-how-can-rds-manage-the-master-password-for-you)
- [253: How do you limit users to their own items in DynamoDB?](#253-how-do-you-limit-users-to-their-own-items-in-dynamodb)
- [254: Does DynamoDB support resource-based policies?](#254-does-dynamodb-support-resource-based-policies)
- [255: What are Aurora Database Activity Streams?](#255-what-are-aurora-database-activity-streams)
- [256: How do you set up a central CloudTrail organization trail properly?](#256-how-do-you-set-up-a-central-cloudtrail-organization-trail-properly)
- [257: What is CloudTrail Lake?](#257-what-is-cloudtrail-lake)
- [258: What are CloudTrail Insights?](#258-what-are-cloudtrail-insights)
- [259: How do you investigate a suspicious role with CloudTrail and Athena?](#259-how-do-you-investigate-a-suspicious-role-with-cloudtrail-and-athena)
- [260: What is CloudWatch Logs data protection?](#260-what-is-cloudwatch-logs-data-protection)
- [261: How do you alarm on many failed API calls?](#261-how-do-you-alarm-on-many-failed-api-calls)
- [262: What is an AWS Config conformance pack?](#262-what-is-an-aws-config-conformance-pack)
- [263: What is a Config aggregator?](#263-what-is-a-config-aggregator)
- [264: How do you automatically fix non-compliant resources with Config?](#264-how-do-you-automatically-fix-non-compliant-resources-with-config)
- [265: What are some common GuardDuty finding types?](#265-what-are-some-common-guardduty-finding-types)
- [266: How do you reduce GuardDuty noise?](#266-how-do-you-reduce-guardduty-noise)
- [267: What does GuardDuty Malware Protection cover?](#267-what-does-guardduty-malware-protection-cover)
- [268: What is GuardDuty Extended Threat Detection?](#268-what-is-guardduty-extended-threat-detection)
- [269: What standards does Security Hub CSPM check against?](#269-what-standards-does-security-hub-cspm-check-against)
- [270: What are Security Hub automation rules?](#270-what-are-security-hub-automation-rules)
- [271: How can Inspector be used in a CI/CD pipeline?](#271-how-can-inspector-be-used-in-a-cicd-pipeline)
- [272: How do you make Macie more useful?](#272-how-do-you-make-macie-more-useful)
- [273: How do you use Detective during an investigation?](#273-how-do-you-use-detective-during-an-investigation)
- [274: How do other tools consume data from Security Lake?](#274-how-do-other-tools-consume-data-from-security-lake)
- [275: How would you automatically close SSH open to the internet?](#275-how-would-you-automatically-close-ssh-open-to-the-internet)
- [276: What do you do when an access key is leaked?](#276-what-do-you-do-when-an-access-key-is-leaked)
- [277: How do you isolate a compromised EC2 instance?](#277-how-do-you-isolate-a-compromised-ec2-instance)
- [278: How do you secure and audit Session Manager?](#278-how-do-you-secure-and-audit-session-manager)
- [279: Why is Run Command safer than SSH for fleet changes?](#279-why-is-run-command-safer-than-ssh-for-fleet-changes)
- [280: How would you allow only certain outbound domains with Network Firewall?](#280-how-would-you-allow-only-certain-outbound-domains-with-network-firewall)
- [281: What are some important DNS Firewall settings?](#281-what-are-some-important-dns-firewall-settings)
- [282: How do you use aws:PrincipalOrgID in a resource policy?](#282-how-do-you-use-awsprincipalorgid-in-a-resource-policy)
- [283: What is aws:ResourceOrgID used for?](#283-what-is-awsresourceorgid-used-for)
- [284: Show an example of an ABAC policy.](#284-show-an-example-of-an-abac-policy)
- [285: How do you enforce tags on new resources?](#285-how-do-you-enforce-tags-on-new-resources)
- [286: How does a central security account access all member accounts?](#286-how-does-a-central-security-account-access-all-member-accounts)
- [287: What should you watch for when sharing resources with AWS RAM?](#287-what-should-you-watch-for-when-sharing-resources-with-aws-ram)
- [288: How do you protect backups from an attacker with admin access to production?](#288-how-do-you-protect-backups-from-an-attacker-with-admin-access-to-production)
- [289: What are backup policies in AWS Organizations?](#289-what-are-backup-policies-in-aws-organizations)
- [290: How can you reduce PCI DSS scope on AWS?](#290-how-can-you-reduce-pci-dss-scope-on-aws)
- [291: How would you collect evidence for a SOC 2 audit on AWS?](#291-how-would-you-collect-evidence-for-a-soc-2-audit-on-aws)
- [292: How do CloudFormation StackSets help with security guardrails?](#292-how-do-cloudformation-stacksets-help-with-security-guardrails)
- [293: What are CloudFormation Hooks?](#293-what-are-cloudformation-hooks)
- [294: How do you secure Terraform state on AWS?](#294-how-do-you-secure-terraform-state-on-aws)
- [295: How do you lock a GitHub Actions OIDC role to one repo and branch?](#295-how-do-you-lock-a-github-actions-oidc-role-to-one-repo-and-branch)
- [296: How do you keep a CDK or CloudFormation deploy role least privilege?](#296-how-do-you-keep-a-cdk-or-cloudformation-deploy-role-least-privilege)
- [297: How do you protect AWS credentials from pull requests opened from forks?](#297-how-do-you-protect-aws-credentials-from-pull-requests-opened-from-forks)
- [298: How do you run a Well-Architected security review?](#298-how-do-you-run-a-well-architected-security-review)
- [299: Why is a security group open to 0.0.0.0/0 on port 22 or 3389 so dangerous?](#299-why-is-a-security-group-open-to-00000-on-port-22-or-3389-so-dangerous)
- [300: What happened in the Capital One breach and what are the lessons?](#300-what-happened-in-the-capital-one-breach-and-what-are-the-lessons)

### Advanced Questions (301-450)

- [301: When can a resource-based policy allow access even if the identity policy does not?](#301-when-can-a-resource-based-policy-allow-access-even-if-the-identity-policy-does-not)
- [302: Why might a trust policy suddenly stop working after a role is recreated?](#302-why-might-a-trust-policy-suddenly-stop-working-after-a-role-is-recreated)
- [303: What are common IAM privilege escalation paths?](#303-what-are-common-iam-privilege-escalation-paths)
- [304: How do you find privilege escalation risks in an account?](#304-how-do-you-find-privilege-escalation-risks-in-an-account)
- [305: How do you revoke credentials for a role session that has already been issued?](#305-how-do-you-revoke-credentials-for-a-role-session-that-has-already-been-issued)
- [306: How can you stop stolen EC2 role credentials from being used outside the instance?](#306-how-can-you-stop-stolen-ec2-role-credentials-from-being-used-outside-the-instance)
- [307: How do you design a data perimeter?](#307-how-do-you-design-a-data-perimeter)
- [308: How do you avoid breaking AWS services when adding network conditions to policies?](#308-how-do-you-avoid-breaking-aws-services-when-adding-network-conditions-to-policies)
- [309: What is aws:CalledVia?](#309-what-is-awscalledvia)
- [310: How do you prevent your roles from assuming roles in accounts outside your organization?](#310-how-do-you-prevent-your-roles-from-assuming-roles-in-accounts-outside-your-organization)
- [311: How do RCPs help with the confused deputy problem at scale?](#311-how-do-rcps-help-with-the-confused-deputy-problem-at-scale)
- [312: How do you protect security tooling in member accounts from local admins?](#312-how-do-you-protect-security-tooling-in-member-accounts-from-local-admins)
- [313: What limits do SCPs have and how do you work around them?](#313-what-limits-do-scps-have-and-how-do-you-work-around-them)
- [314: How do you safely roll out a new SCP?](#314-how-do-you-safely-roll-out-a-new-scp)
- [315: How would you design identity and access for a company with 200 AWS accounts?](#315-how-would-you-design-identity-and-access-for-a-company-with-200-aws-accounts)
- [316: How do you design break-glass access when you rely on IAM Identity Center?](#316-how-do-you-design-break-glass-access-when-you-rely-on-iam-identity-center)
- [317: How does centralized root access work in AWS Organizations?](#317-how-does-centralized-root-access-work-in-aws-organizations)
- [318: How do you secure the Organizations management account?](#318-how-do-you-secure-the-organizations-management-account)
- [319: How would you design Cognito for a multi-tenant SaaS app?](#319-how-would-you-design-cognito-for-a-multi-tenant-saas-app)
- [320: How do you handle token revocation with Cognito?](#320-how-do-you-handle-token-revocation-with-cognito)
- [321: What are common JWT validation mistakes?](#321-what-are-common-jwt-validation-mistakes)
- [322: How do you give each mobile user access to only their own S3 folder?](#322-how-do-you-give-each-mobile-user-access-to-only-their-own-s3-folder)
- [323: How do you do fine-grained authorization in a multi-tenant API on AWS?](#323-how-do-you-do-fine-grained-authorization-in-a-multi-tenant-api-on-aws)
- [324: Why does IMDSv2 stop most SSRF attacks?](#324-why-does-imdsv2-stop-most-ssrf-attacks)
- [325: How do the threat models of the node role, IRSA and Pod Identity differ on EKS?](#325-how-do-the-threat-models-of-the-node-role-irsa-and-pod-identity-differ-on-eks)
- [326: How would you harden an EKS cluster?](#326-how-would-you-harden-an-eks-cluster)
- [327: How are Kubernetes secrets protected in EKS?](#327-how-are-kubernetes-secrets-protected-in-eks)
- [328: How do you limit pod-to-pod network traffic in EKS?](#328-how-do-you-limit-pod-to-pod-network-traffic-in-eks)
- [329: What is the impact of a container breakout on an EKS EC2 node?](#329-what-is-the-impact-of-a-container-breakout-on-an-eks-ec2-node)
- [330: How does compute isolation differ between Lambda, Fargate and EC2-based containers?](#330-how-does-compute-isolation-differ-between-lambda-fargate-and-ec2-based-containers)
- [331: How do you design KMS keys for a large organization?](#331-how-do-you-design-kms-keys-for-a-large-organization)
- [332: What is needed for a role in account B to use a KMS key in account A?](#332-what-is-needed-for-a-role-in-account-b-to-use-a-kms-key-in-account-a)
- [333: How do you handle KMS request limits in high-volume apps?](#333-how-do-you-handle-kms-request-limits-in-high-volume-apps)
- [334: What is crypto-shredding and how can KMS support it?](#334-what-is-crypto-shredding-and-how-can-kms-support-it)
- [335: What are the trade-offs of importing your own key material into KMS?](#335-what-are-the-trade-offs-of-importing-your-own-key-material-into-kms)
- [336: How do you avoid locking yourself out of a KMS key?](#336-how-do-you-avoid-locking-yourself-out-of-a-kms-key)
- [337: How did attackers use SSE-C to hold S3 data for ransom, and how do you defend against it?](#337-how-did-attackers-use-sse-c-to-hold-s3-data-for-ransom-and-how-do-you-defend-against-it)
- [338: How would you design S3 for ransomware resilience?](#338-how-would-you-design-s3-for-ransomware-resilience)
- [339: What should you watch out for with Object Lock compliance mode?](#339-what-should-you-watch-out-for-with-object-lock-compliance-mode)
- [340: How would you design a secure file upload pipeline on AWS?](#340-how-would-you-design-a-secure-file-upload-pipeline-on-aws)
- [341: In which ways can S3 data be exposed even with Block Public Access on?](#341-in-which-ways-can-s3-data-be-exposed-even-with-block-public-access-on)
- [342: What is the risk of predictable S3 bucket names, and how do you defend against it?](#342-what-is-the-risk-of-predictable-s3-bucket-names-and-how-do-you-defend-against-it)
- [343: What is subdomain takeover on AWS?](#343-what-is-subdomain-takeover-on-aws)
- [344: How would you design the network for a workload handling card data?](#344-how-would-you-design-the-network-for-a-workload-handling-card-data)
- [345: How do you build centralized egress inspection with Transit Gateway?](#345-how-do-you-build-centralized-egress-inspection-with-transit-gateway)
- [346: What are the trade-offs of centralizing interface VPC endpoints?](#346-what-are-the-trade-offs-of-centralizing-interface-vpc-endpoints)
- [347: How do you secure a PrivateLink endpoint service you offer to customers?](#347-how-do-you-secure-a-privatelink-endpoint-service-you-offer-to-customers)
- [348: What is Gateway Load Balancer used for?](#348-what-is-gateway-load-balancer-used-for)
- [349: What is AWS Verified Access and when would you use it?](#349-what-is-aws-verified-access-and-when-would-you-use-it)
- [350: How can attackers exfiltrate data through DNS, and how do you detect it?](#350-how-can-attackers-exfiltrate-data-through-dns-and-how-do-you-detect-it)
- [351: How would you design a DDoS-resilient architecture on AWS?](#351-how-would-you-design-a-ddos-resilient-architecture-on-aws)
- [352: What are the request body inspection limits in AWS WAF and why do they matter?](#352-what-are-the-request-body-inspection-limits-in-aws-waf-and-why-do-they-matter)
- [353: How do you tune AWS WAF for a JSON API?](#353-how-do-you-tune-aws-waf-for-a-json-api)
- [354: What does Shield Advanced automatic application layer DDoS mitigation do?](#354-what-does-shield-advanced-automatic-application-layer-ddos-mitigation-do)
- [355: How do you rotate keys for CloudFront signed URLs?](#355-how-do-you-rotate-keys-for-cloudfront-signed-urls)
- [356: How do you use OAC with an S3 bucket encrypted with SSE-KMS?](#356-how-do-you-use-oac-with-an-s3-bucket-encrypted-with-sse-kms)
- [357: What is a security risk with Lambda authorizer caching?](#357-what-is-a-security-risk-with-lambda-authorizer-caching)
- [358: How do you secure incoming webhooks on AWS?](#358-how-do-you-secure-incoming-webhooks-on-aws)
- [359: What is the threat model for a Lambda-based app?](#359-what-is-the-threat-model-for-a-lambda-based-app)
- [360: How can an attacker steal Lambda credentials, and what can you do about it?](#360-how-can-an-attacker-steal-lambda-credentials-and-what-can-you-do-about-it)
- [361: What is "denial of wallet" and how do you defend serverless apps against it?](#361-what-is-denial-of-wallet-and-how-do-you-defend-serverless-apps-against-it)
- [362: How do you secure ECS Exec?](#362-how-do-you-secure-ecs-exec)
- [363: What is dependency confusion and how does CodeArtifact help?](#363-what-is-dependency-confusion-and-how-does-codeartifact-help)
- [364: How would an attacker abuse a CI/CD pipeline to reach AWS?](#364-how-would-an-attacker-abuse-a-cicd-pipeline-to-reach-aws)
- [365: What mistakes are common in GitHub Actions OIDC trust policies?](#365-what-mistakes-are-common-in-github-actions-oidc-trust-policies)
- [366: How would you set up cross-account deployments from a central CI/CD account?](#366-how-would-you-set-up-cross-account-deployments-from-a-central-cicd-account)
- [367: How do you stop people from changing production resources outside the pipeline?](#367-how-do-you-stop-people-from-changing-production-resources-outside-the-pipeline)
- [368: What is the difference between scanning IaC templates and scanning a Terraform plan?](#368-what-is-the-difference-between-scanning-iac-templates-and-scanning-a-terraform-plan)
- [369: How do you keep secrets out of CloudFormation templates?](#369-how-do-you-keep-secrets-out-of-cloudformation-templates)
- [370: What are the single-user and alternating-users rotation strategies?](#370-what-are-the-single-user-and-alternating-users-rotation-strategies)
- [371: How can secret rotation fail, and how do you monitor it?](#371-how-can-secret-rotation-fail-and-how-do-you-monitor-it)
- [372: How can you avoid static secrets entirely on AWS?](#372-how-can-you-avoid-static-secrets-entirely-on-aws)
- [373: When is IAM database authentication not a good fit?](#373-when-is-iam-database-authentication-not-a-good-fit)
- [374: How have public RDS snapshots led to data leaks, and how do you prevent it?](#374-how-have-public-rds-snapshots-led-to-data-leaks-and-how-do-you-prevent-it)
- [375: How do you block public EBS snapshots and AMIs?](#375-how-do-you-block-public-ebs-snapshots-and-amis)
- [376: What are Organizations declarative policies?](#376-what-are-organizations-declarative-policies)
- [377: How do you protect DynamoDB tables from deletion and data loss?](#377-how-do-you-protect-dynamodb-tables-from-deletion-and-data-loss)
- [378: How does encryption work for cross-region RDS and Aurora replicas?](#378-how-does-encryption-work-for-cross-region-rds-and-aurora-replicas)
- [379: How do attackers try to avoid CloudTrail, and how do you detect it?](#379-how-do-attackers-try-to-avoid-cloudtrail-and-how-do-you-detect-it)
- [380: What activity does CloudTrail not capture by default?](#380-what-activity-does-cloudtrail-not-capture-by-default)
- [381: How would you design logging for a large AWS organization?](#381-how-would-you-design-logging-for-a-large-aws-organization)
- [382: How do you test that your detections actually work?](#382-how-do-you-test-that-your-detections-actually-work)
- [383: What should an AWS incident response plan include?](#383-what-should-an-aws-incident-response-plan-include)
- [384: How do you do forensics on a compromised EC2 instance?](#384-how-do-you-do-forensics-on-a-compromised-ec2-instance)
- [385: How do you respond when an IAM role (not a user) is compromised?](#385-how-do-you-respond-when-an-iam-role-not-a-user-is-compromised)
- [386: How do you respond to a compromised Lambda function?](#386-how-do-you-respond-to-a-compromised-lambda-function)
- [387: How do you respond to a compromised pod in EKS?](#387-how-do-you-respond-to-a-compromised-pod-in-eks)
- [388: What do you do if the root user of an account is compromised?](#388-what-do-you-do-if-the-root-user-of-an-account-is-compromised)
- [389: What do you do when an S3 bucket was found publicly exposed?](#389-what-do-you-do-when-an-s3-bucket-was-found-publicly-exposed)
- [390: What are the signs of a crypto-mining compromise and how do you respond?](#390-what-are-the-signs-of-a-crypto-mining-compromise-and-how-do-you-respond)
- [391: What persistence techniques do attackers use in AWS accounts?](#391-what-persistence-techniques-do-attackers-use-in-aws-accounts)
- [392: How would you build an automated security response pipeline?](#392-how-would-you-build-an-automated-security-response-pipeline)
- [393: What are the risks of automatic remediation?](#393-what-are-the-risks-of-automatic-remediation)
- [394: How should GuardDuty be set up across an organization?](#394-how-should-guardduty-be-set-up-across-an-organization)
- [395: How do you manage findings across regions and accounts in Security Hub CSPM?](#395-how-do-you-manage-findings-across-regions-and-accounts-in-security-hub-cspm)
- [396: How does Inspector scan EC2 instances?](#396-how-does-inspector-scan-ec2-instances)
- [397: How do you control Macie costs at scale?](#397-how-do-you-control-macie-costs-at-scale)
- [398: Should you build a SIEM on Security Lake or buy one?](#398-should-you-build-a-siem-on-security-lake-or-buy-one)
- [399: How do you keep AWS Config costs reasonable?](#399-how-do-you-keep-aws-config-costs-reasonable)
- [400: How do preventive, detective, proactive and responsive controls fit together?](#400-how-do-preventive-detective-proactive-and-responsive-controls-fit-together)
- [401: Should you patch servers in place or replace them?](#401-should-you-patch-servers-in-place-or-replace-them)
- [402: When would you pick EC2 Instance Connect Endpoint over Session Manager?](#402-when-would-you-pick-ec2-instance-connect-endpoint-over-session-manager)
- [403: What are the trade-offs of TLS inspection in Network Firewall?](#403-what-are-the-trade-offs-of-tls-inspection-in-network-firewall)
- [404: How can DNS-over-HTTPS get around your DNS controls, and how do you handle it?](#404-how-can-dns-over-https-get-around-your-dns-controls-and-how-do-you-handle-it)
- [405: What are the common pitfalls of ABAC on AWS?](#405-what-are-the-common-pitfalls-of-abac-on-aws)
- [406: How do you scale ABAC with IAM Identity Center?](#406-how-do-you-scale-abac-with-iam-identity-center)
- [407: How do you use tags in an SCP to protect certain resources?](#407-how-do-you-use-tags-in-an-scp-to-protect-certain-resources)
- [408: When should you use a resource-based policy instead of role assumption for cross-account access?](#408-when-should-you-use-a-resource-based-policy-instead-of-role-assumption-for-cross-account-access)
- [409: A role in account B gets AccessDenied reading an SSE-KMS object in account A's bucket. How do you troubleshoot?](#409-a-role-in-account-b-gets-accessdenied-reading-an-sse-kms-object-in-account-as-bucket-how-do-you-troubleshoot)
- [410: How do you read an AccessDenied error message on AWS?](#410-how-do-you-read-an-accessdenied-error-message-on-aws)
- [411: How do you apply the 3-2-1 backup rule on AWS for ransomware?](#411-how-do-you-apply-the-3-2-1-backup-rule-on-aws-for-ransomware)
- [412: What happens to IAM and IAM Identity Center if a region fails?](#412-what-happens-to-iam-and-iam-identity-center-if-a-region-fails)
- [413: Why should you use STS regional endpoints?](#413-why-should-you-use-sts-regional-endpoints)
- [414: What do you need to run a HIPAA workload on AWS?](#414-what-do-you-need-to-run-a-hipaa-workload-on-aws)
- [415: How do you meet data residency requirements on AWS?](#415-how-do-you-meet-data-residency-requirements-on-aws)
- [416: What does "compliance as code" mean on AWS?](#416-what-does-compliance-as-code-mean-on-aws)
- [417: Which IAM limits affect how you design policies?](#417-which-iam-limits-affect-how-you-design-policies)
- [418: When do you use a permissions boundary, an SCP or a session policy?](#418-when-do-you-use-a-permissions-boundary-an-scp-or-a-session-policy)
- [419: How would you build a self-service AWS platform for dev teams with guardrails?](#419-how-would-you-build-a-self-service-aws-platform-for-dev-teams-with-guardrails)
- [420: What are the tenant isolation models for SaaS on AWS?](#420-what-are-the-tenant-isolation-models-for-saas-on-aws)
- [421: What is the token vending machine pattern?](#421-what-is-the-token-vending-machine-pattern)
- [422: How would you secure a serverless app made of API Gateway, Lambda and DynamoDB?](#422-how-would-you-secure-a-serverless-app-made-of-api-gateway-lambda-and-dynamodb)
- [423: How would you secure a public static website with a backend API?](#423-how-would-you-secure-a-public-static-website-with-a-backend-api)
- [424: What does zero trust mean on AWS in practice?](#424-what-does-zero-trust-mean-on-aws-in-practice)
- [425: What is wrong with a trust policy that allows "AWS": "*" and how is it exploited?](#425-what-is-wrong-with-a-trust-policy-that-allows-aws--and-how-is-it-exploited)
- [426: Why are open SNS topic and SQS queue policies dangerous?](#426-why-are-open-sns-topic-and-sqs-queue-policies-dangerous)
- [427: How can a misconfigured Cognito user pool lead to privilege escalation?](#427-how-can-a-misconfigured-cognito-user-pool-lead-to-privilege-escalation)
- [428: What API security mistakes do you often see in AWS reviews?](#428-what-api-security-mistakes-do-you-often-see-in-aws-reviews)
- [429: Walk through a typical "leaked key on GitHub" breach.](#429-walk-through-a-typical-leaked-key-on-github-breach)
- [430: What did the CircleCI breach in early 2023 teach about CI/CD and AWS?](#430-what-did-the-circleci-breach-in-early-2023-teach-about-cicd-and-aws)
- [431: How have exposed .env files led to AWS account compromises?](#431-how-have-exposed-env-files-led-to-aws-account-compromises)
- [432: How could an SSRF bug in an EKS pod lead to an AWS account compromise?](#432-how-could-an-ssrf-bug-in-an-eks-pod-lead-to-an-aws-account-compromise)
- [433: How can attackers abuse AWS credentials cached on developer laptops?](#433-how-can-attackers-abuse-aws-credentials-cached-on-developer-laptops)
- [434: Which open-source tools are used to test AWS security?](#434-which-open-source-tools-are-used-to-test-aws-security)
- [435: How does Prowler compare with Security Hub CSPM?](#435-how-does-prowler-compare-with-security-hub-cspm)
- [436: You join a company with a weak AWS setup. What do you fix first?](#436-you-join-a-company-with-a-weak-aws-setup-what-do-you-fix-first)
- [437: How do you measure an AWS security program?](#437-how-do-you-measure-an-aws-security-program)
- [438: How do you secure apps built with Amazon Bedrock?](#438-how-do-you-secure-apps-built-with-amazon-bedrock)
- [439: What can an attacker do with the Organizations management account, and how do you limit the risk?](#439-what-can-an-attacker-do-with-the-organizations-management-account-and-how-do-you-limit-the-risk)
- [440: Why is NotPrincipal with Deny risky?](#440-why-is-notprincipal-with-deny-risky)
- [441: A decrypt call fails even though the key policy and IAM policy allow it. What could it be?](#441-a-decrypt-call-fails-even-though-the-key-policy-and-iam-policy-allow-it-what-could-it-be)
- [442: How can you lock yourself out of an S3 bucket, and how do you recover?](#442-how-can-you-lock-yourself-out-of-an-s3-bucket-and-how-do-you-recover)
- [443: Why use aws:PrincipalArn instead of aws:userid or a role ARN in Principal for exceptions?](#443-why-use-awsprincipalarn-instead-of-awsuserid-or-a-role-arn-in-principal-for-exceptions)
- [444: What problems does IAM eventual consistency cause in automation?](#444-what-problems-does-iam-eventual-consistency-cause-in-automation)
- [445: How do you give temporary elevated access on AWS?](#445-how-do-you-give-temporary-elevated-access-on-aws)
- [446: Can an SCP stop your account from sharing data with outside principals?](#446-can-an-scp-stop-your-account-from-sharing-data-with-outside-principals)
- [447: How would you detect and respond to a compromised identity provider?](#447-how-would-you-detect-and-respond-to-a-compromised-identity-provider)
- [448: What do you look for when reviewing a pull request that changes IAM?](#448-what-do-you-look-for-when-reviewing-a-pull-request-that-changes-iam)
- [449: What is the shared responsibility model for managed AI and serverless services?](#449-what-is-the-shared-responsibility-model-for-managed-ai-and-serverless-services)
- [450: How would you design security for a brand-new AWS organization from scratch?](#450-how-would-you-design-security-for-a-brand-new-aws-organization-from-scratch)

---

# Easy Questions (1-150)

## 1: What is the AWS shared responsibility model?

It splits security work between AWS and you. AWS is responsible for security "of" the cloud: data centers, hardware, the network, and the software that runs the services. You are responsible for security "in" the cloud: your data, who has access, how you configure services, your operating systems and your application code.

Most breaches on AWS happen on the customer side of that line, for example a public S3 bucket or a leaked access key, not because AWS itself was hacked.

## 2: How does your share of the work change between EC2, RDS and Lambda?

The more managed the service, the less you have to do.

- EC2: you patch the OS, configure the firewall (security groups), install software, manage disk encryption and everything above that.
- RDS: AWS patches the OS and database engine, but you choose network access, encryption, database users, parameter settings and backups.
- Lambda: AWS runs the OS and runtime. You handle your code, its dependencies, the execution role and any secrets it uses.

In all three cases, data and access control stay your job.

## 3: What is the root user in an AWS account?

The root user is the identity created with the account. It signs in with the email address and password used at sign-up and has full access to everything in the account. IAM policies cannot limit it inside its own account (SCPs from AWS Organizations can, for member accounts). Because it can do anything, including closing the account, it should almost never be used.

## 4: How do you protect the root user?

- Turn on MFA, preferably a FIDO2 security key or passkey. AWS now requires MFA for root users in most account types.
- Do not create access keys for root. Delete them if they exist.
- Use a strong, unique password stored in a password manager or safe.
- Use a group email address for the account, not a personal inbox.
- Do daily work with IAM Identity Center users or roles instead.
- In AWS Organizations, turn on centralized root access so member accounts have no root credentials at all.
- Alert on any root sign-in through CloudTrail and EventBridge.

## 5: Which tasks still need the root user?

A small set of account-level tasks, for example:

- Changing the account name, email address or root password
- Closing the account
- Restoring IAM permissions when the only administrator locked themselves out
- Changing or cancelling an AWS Support plan
- Registering as a seller in the Reserved Instance Marketplace
- Unlocking an S3 bucket policy that denies everyone, or an SQS queue policy that does the same

With centralized root access in Organizations, some of these (like deleting a bad bucket policy) can be done from the management account with a short root session instead of signing in as root.

## 6: What MFA types does AWS support?

- Passkeys and FIDO2 security keys (like YubiKey)
- Virtual authenticator apps (TOTP apps like Google Authenticator or 1Password)
- Hardware TOTP tokens

FIDO2 keys and passkeys are phishing-resistant because the key checks the website origin. TOTP codes can be phished by a fake login page. You can register up to eight MFA devices per root user or IAM user.

## 7: What is AWS IAM?

IAM (Identity and Access Management) controls who can do what in your AWS account. It has identities (users, groups, roles) and policies that describe allowed and denied actions. Every AWS API call is checked against IAM before it runs. IAM is a global service and has no extra cost.

## 8: What is an IAM user?

An IAM user is a long-term identity in one account. It can have a password for the console and up to two access keys for the API. Each user has its own permissions through policies.

Today AWS recommends avoiding IAM users for people. Use IAM Identity Center or federation instead, and roles for workloads. IAM users still show up for things like legacy tools that cannot use roles, or a break-glass account.

## 9: What is an IAM group?

A group is a collection of IAM users. You attach policies to the group and every user in it gets those permissions. This is easier than attaching policies to each user. Groups cannot be nested, cannot be used as a principal in a resource policy, and cannot sign in. They only hold users.

## 10: What is an IAM role?

A role is an identity with permissions but no long-term credentials. Something has to "assume" it, and then it gets temporary credentials from STS. A role can be assumed by a user, an AWS service (EC2, Lambda), a user from another account, or an external identity through federation. Each role has a trust policy that says who can assume it, and permission policies that say what it can do.

## 11: What is the difference between an IAM user and an IAM role?

|             | IAM user                           | IAM role                                 |
| ----------- | ---------------------------------- | ---------------------------------------- |
| Credentials | Long-term password and access keys | Temporary, from STS                      |
| Who uses it | One specific person or app         | Anyone allowed by the trust policy       |
| Expiry      | Keys never expire unless rotated   | Sessions expire (15 min to 12 h)         |
| Typical use | Legacy tools, break-glass          | Services, cross-account, federated users |

Roles are safer because there is nothing long-lived to leak.

## 12: What does an IAM policy look like?

It is a JSON document with a version and one or more statements.

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "ReadReports",
      "Effect": "Allow",
      "Action": ["s3:GetObject"],
      "Resource": "arn:aws:s3:::company-reports/*"
    }
  ]
}
```

Always use `"Version": "2012-10-17"`. The older `2008-10-17` version does not support policy variables like `${aws:username}`.

## 13: What are the main elements of a policy statement?

- `Effect`: `Allow` or `Deny`
- `Action` (or `NotAction`): the API actions, like `s3:GetObject`
- `Resource` (or `NotResource`): the ARNs the statement applies to
- `Condition`: optional extra checks, like source IP, MFA, tags or VPC endpoint
- `Principal` (or `NotPrincipal`): who the statement applies to. Only used in resource-based policies and trust policies.
- `Sid`: an optional label

## 14: What is the difference between AWS managed, customer managed and inline policies?

- AWS managed policies are written and updated by AWS, like `ReadOnlyAccess`. They are easy to use but often too broad, and AWS can change them.
- Customer managed policies are standalone policies you write. You can attach them to many identities, and they keep version history.
- Inline policies are embedded directly in one user, group or role and are deleted with it.

Customer managed policies are usually the best default. Use inline policies only when the permission should never be reused.

## 15: What is an ARN?

An Amazon Resource Name uniquely identifies a resource. The format is:

```text
arn:partition:service:region:account-id:resource
```

Examples:

```text
arn:aws:iam::123456789012:role/deploy-role
arn:aws:s3:::my-bucket/reports/*
arn:aws:lambda:eu-west-1:123456789012:function:orders
```

Some services leave the region or account empty. IAM is global, so its ARNs have no region. S3 bucket ARNs have neither region nor account.

## 16: What is the difference between identity-based and resource-based policies?

Identity-based policies are attached to a user, group or role and say what that identity can do. Resource-based policies are attached to a resource, like an S3 bucket, SQS queue, KMS key or Lambda function, and say who can access that resource. Resource-based policies have a `Principal` element. They are the main way to give another account access without making it assume a role.

## 17: What does least privilege mean on AWS?

Give each identity only the permissions it needs for its job, on only the resources it needs, and nothing more. In practice: start with a small set of actions, scope `Resource` to specific ARNs, add conditions, and remove unused permissions over time using IAM Access Analyzer and last-accessed data. Avoid `"Action": "*"` and `"Resource": "*"` unless there really is no narrower option.

## 18: What is an implicit deny?

By default, every request is denied. If no policy allows an action, the request fails. This is called an implicit deny. You do not need to write anything to get it. It is why a new IAM user with no policies cannot do anything.

## 19: What is an explicit deny?

An explicit deny is a statement with `"Effect": "Deny"` that matches the request. It always wins, no matter how many allows exist in other policies. Explicit denies are useful for guardrails, for example blocking everyone from deleting CloudTrail trails, or denying all actions outside approved regions.

## 20: What are access keys and why are long-lived ones risky?

Access keys are an access key ID (starting with `AKIA`) and a secret access key. They sign API calls from the CLI and SDKs. They never expire on their own, so if one leaks in a Git repo, log file or laptop backup, an attacker can use it until someone notices and disables it. Prefer roles and temporary credentials (keys starting with `ASIA`) wherever possible.

## 21: How do you rotate an IAM user's access key without downtime?

Each user can have two access keys, which makes rotation possible:

1. Create a second key.
2. Update the application to use the new key.
3. Check "last used" on the old key to confirm nothing still uses it.
4. Deactivate the old key and wait a bit.
5. Delete the old key.

```bash
aws iam create-access-key --user-name legacy-app
aws iam update-access-key --user-name legacy-app --access-key-id AKIAOLDKEY --status Inactive
aws iam delete-access-key --user-name legacy-app --access-key-id AKIAOLDKEY
```

## 22: What is an IAM password policy?

It sets rules for IAM user console passwords in the account: minimum length, required character types, maximum age, preventing reuse, and whether users can change their own password. It does not apply to the root user or to IAM Identity Center users (Identity Center has its own settings). A typical setting is a minimum length of 14 or more characters with MFA required.

## 23: What is AWS STS?

The Security Token Service issues temporary credentials. You call it to assume a role (`AssumeRole`), to exchange a web identity token for AWS credentials (`AssumeRoleWithWebIdentity`), to exchange a SAML assertion (`AssumeRoleWithSAML`), or to get a session token with MFA (`GetSessionToken`). The credentials it returns expire automatically.

## 24: What do temporary credentials consist of?

Three values plus an expiry time:

- `AccessKeyId` (starts with `ASIA`)
- `SecretAccessKey`
- `SessionToken`
- `Expiration`

All three values must be sent with each request. SDKs pick them up automatically from environment variables, the credentials file, or the instance metadata service.

## 25: What does AssumeRole do?

`sts:AssumeRole` lets a principal take on a role and get temporary credentials for it. The caller needs permission to call `sts:AssumeRole` on that role, and the role's trust policy must allow the caller.

```bash
aws sts assume-role \
  --role-arn arn:aws:iam::222222222222:role/ReadOnlyAudit \
  --role-session-name alice-audit
```

The returned credentials have the role's permissions, not the caller's.

## 26: What is a role trust policy?

It is a resource-based policy attached to a role that says who may assume it.

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Principal": { "Service": "lambda.amazonaws.com" },
      "Action": "sts:AssumeRole"
    }
  ]
}
```

This one lets the Lambda service assume the role. For cross-account access, the principal would be another account or role ARN.

## 27: What is an EC2 instance profile?

An instance profile is a container that holds one IAM role and attaches it to an EC2 instance. Code on the instance gets temporary credentials for that role from the instance metadata service, and the SDK rotates them automatically. When you pick a role in the EC2 console, it creates the instance profile for you.

## 28: Why should you not put access keys on an EC2 instance?

Keys on disk are long-lived, easy to copy, often end up in AMIs, backups and logs, and must be rotated by hand. An instance profile gives the same access with temporary credentials that rotate automatically and cannot be reused after they expire. If the instance is compromised, the damage is limited to the role's permissions and the remaining session time.

## 29: What is a service-linked role?

It is a role that is predefined by an AWS service and linked to it, for example `AWSServiceRoleForAutoScaling`. The service creates or asks you to create it, and the permissions are set by AWS. You cannot change its permissions, and you usually cannot delete it while the service still uses it. It lets services act on your behalf without you writing the policy.

## 30: What is IAM Access Analyzer?

Access Analyzer helps you find and reduce access. It has several features:

- External access findings: resources (S3 buckets, KMS keys, roles, queues and more) shared outside your account or organization
- Internal access findings: which principals in your organization can reach critical resources
- Unused access findings: unused roles, access keys, passwords and permissions
- Policy validation: checks policies for errors and bad practices
- Policy generation: builds a least-privilege policy from CloudTrail activity
- Custom policy checks: verify a policy does not grant certain access before you deploy it

## 31: What is the IAM credential report?

It is a CSV file listing every IAM user in the account and the status of their credentials: whether they have a password, when it was last used, whether MFA is on, and when each access key was created and last used. Auditors use it to find old keys and users without MFA.

```bash
aws iam generate-credential-report
aws iam get-credential-report --query Content --output text | base64 --decode
```

## 32: What is IAM Identity Center?

IAM Identity Center (formerly AWS SSO) is the recommended way to give people access to AWS accounts. Users sign in once through a portal and pick an account and permission set. Identity Center creates roles in each account and hands out short-lived credentials. It can use its own user directory, Active Directory, or an external identity provider like Okta, Microsoft Entra ID or Google Workspace.

## 33: What is identity federation?

Federation means letting users from another identity system use AWS without creating IAM users for them. The external identity provider (IdP) authenticates the user, then AWS trusts that result and issues temporary credentials. The common standards are SAML 2.0 (for workforce logins) and OpenID Connect (for web, mobile and CI systems like GitHub Actions).

## 34: What is AWS Organizations?

Organizations lets you manage many AWS accounts together. It gives you:

- One management account and many member accounts
- Organizational units (OUs) to group accounts
- Consolidated billing
- Policies that apply to many accounts at once: SCPs, RCPs, tag policies, backup policies and others
- Trusted access, so services like CloudTrail, GuardDuty and Security Hub can be turned on organization-wide

## 35: What is a service control policy (SCP)?

An SCP is an Organizations policy that sets the maximum permissions for IAM users and roles in member accounts. It does not grant anything by itself. Even if a role has `AdministratorAccess`, it cannot do what the SCP blocks. SCPs do not affect the management account or service-linked roles.

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "DenyLeavingOrg",
      "Effect": "Deny",
      "Action": "organizations:LeaveOrganization",
      "Resource": "*"
    }
  ]
}
```

## 36: What is AWS Control Tower?

Control Tower sets up and manages a multi-account environment (a landing zone) using AWS best practices. It creates a management account setup, a Log Archive account and an Audit account, sets up IAM Identity Center, organization-wide CloudTrail and Config, and applies controls (guardrails). It also gives you Account Factory to create new accounts with the same baseline.

## 37: Why do companies use multiple AWS accounts?

An account is the strongest isolation boundary on AWS. Separate accounts:

- Limit the blast radius if one account is compromised
- Separate production from development and testing
- Make billing and quotas per team or workload clear
- Let you apply different SCPs per environment
- Keep logs and security tools in accounts that app teams cannot change

## 38: What is Amazon Cognito?

Cognito adds sign-up, sign-in and access control to web and mobile apps. User pools are a user directory and OIDC identity provider that issue JWTs. Identity pools exchange tokens (from a user pool, Google, Apple, SAML and so on) for temporary AWS credentials, so a client can call AWS services directly with limited permissions.

## 39: What is the difference between a Cognito user pool and an identity pool?

- A user pool handles authentication. It stores users, handles passwords, MFA and social login, and returns ID, access and refresh tokens.
- An identity pool handles authorization to AWS. It takes a token and returns temporary AWS credentials for an IAM role.

You can use a user pool alone (your API checks the JWT), or both together when the browser or app needs to call S3 or DynamoDB directly.

## 40: What tokens does a Cognito user pool issue?

- ID token: a JWT with user attributes like email and name. Used by your app to know who the user is.
- Access token: a JWT with scopes and groups. Sent to your APIs to authorize calls.
- Refresh token: used to get new ID and access tokens without signing in again.

ID and access tokens default to one hour. Refresh tokens default to 30 days and can be set from 1 hour up to 10 years.

## 41: What is AWS Secrets Manager?

Secrets Manager stores secrets like database passwords and API keys, encrypted with KMS. Apps fetch them at runtime with an API call instead of keeping them in code or config files. It supports automatic rotation with Lambda functions, managed rotation for some services such as RDS, versioning, cross-region replication and resource policies for cross-account access.

## 42: What is SSM Parameter Store and what is a SecureString?

Parameter Store, part of Systems Manager, stores configuration values in a hierarchy like `/prod/orders/db_host`. Parameter types are `String`, `StringList` and `SecureString`. A `SecureString` is encrypted with KMS and decrypted only when you ask for it with `--with-decryption` and have `kms:Decrypt` permission.

```bash
aws ssm put-parameter --name /prod/orders/api_key --type SecureString --value 'abc123'
aws ssm get-parameter --name /prod/orders/api_key --with-decryption
```

## 43: What is AWS KMS?

Key Management Service creates and controls encryption keys. Key material stays inside FIPS 140-3 validated hardware security modules and never leaves KMS in plain text. Other services (S3, EBS, RDS, Secrets Manager and many more) use KMS keys to encrypt your data. Every use of a key is logged in CloudTrail, and access is controlled by key policies, IAM policies and grants.

## 44: What is the difference between customer managed, AWS managed and AWS owned KMS keys?

- Customer managed keys: you create them, write the key policy, control rotation and can disable or delete them. They cost a monthly fee.
- AWS managed keys: created in your account by a service (alias like `aws/s3`). You can see them and their usage, but cannot change the policy or share them cross-account.
- AWS owned keys: belong to AWS and are shared across many accounts. You cannot see or audit them. Used by default in services like DynamoDB.

Use customer managed keys when you need control over who can decrypt, cross-account access or a custom rotation and deletion process.

## 45: What does encryption at rest mean?

Data is encrypted while stored on disk, so someone with access to the raw storage cannot read it. On AWS this covers EBS volumes, S3 objects, RDS and Aurora storage, DynamoDB tables, snapshots and backups. Most services use KMS keys for this. Many now encrypt by default, for example all new S3 objects get at least SSE-S3.

## 46: What does encryption in transit mean?

Data is encrypted while moving over a network, usually with TLS. Clients talk to AWS APIs over HTTPS, and you should also use TLS between your users and your load balancers, CloudFront and APIs, and between your app and its database. Some EC2 instance types also encrypt traffic between instances automatically at the hardware level.

## 47: What is AWS Certificate Manager (ACM)?

ACM issues and manages TLS certificates. Public certificates are free when used with integrated services like Elastic Load Balancing, CloudFront and API Gateway, and ACM renews them automatically. You prove you own the domain with DNS or email validation. ACM can also import third-party certificates, and AWS Private CA can issue private certificates for internal services.

## 48: What is AWS CloudHSM?

CloudHSM gives you dedicated hardware security modules in your VPC. You fully control the keys and users. AWS cannot access your key material. It is used when compliance requires single-tenant HSMs, for custom crypto workloads like SSL offload or document signing, or as a custom key store behind KMS. It costs much more than KMS and you manage clustering and backups yourself.

## 49: What is S3 Block Public Access?

It is a set of four settings that override anything that would make S3 data public:

- `BlockPublicAcls` and `IgnorePublicAcls` for ACLs
- `BlockPublicPolicy` and `RestrictPublicBuckets` for bucket policies

It can be set at the account level and per bucket. New buckets have all four turned on by default. Turn it on at the account level unless you have a specific public bucket, and even then prefer CloudFront in front of a private bucket.

## 50: What is an S3 bucket policy?

It is a resource-based policy on a bucket that controls who can access the bucket and its objects. It is used for cross-account access, forcing TLS, forcing encryption headers, allowing CloudFront through OAC, or limiting access to a VPC endpoint.

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "DenyInsecureTransport",
      "Effect": "Deny",
      "Principal": "*",
      "Action": "s3:*",
      "Resource": ["arn:aws:s3:::my-bucket", "arn:aws:s3:::my-bucket/*"],
      "Condition": { "Bool": { "aws:SecureTransport": "false" } }
    }
  ]
}
```

## 51: What is an S3 presigned URL?

A presigned URL gives temporary access to one S3 object without making it public. It is signed with the credentials of whoever created it, so it can only do what that identity can do. It expires after a set time (up to 7 days with SigV4, and earlier if the signing credentials expire first).

```bash
aws s3 presign s3://invoices/2026/inv-1001.pdf --expires-in 300
```

A common use is letting a browser upload or download a file directly to S3 after your backend checks the user's permissions.

## 52: What server-side encryption options does S3 support?

- SSE-S3: S3 manages the keys. This is the default for all new objects.
- SSE-KMS: uses a KMS key, so you get key policies, CloudTrail logs of key use, and the ability to revoke access by changing the key policy.
- DSSE-KMS: two layers of encryption with KMS, for rules that ask for dual-layer encryption.
- SSE-C: you send your own key with each request. S3 does not store the key. Since April 2026 it is disabled by default on new general purpose buckets.

There is also client-side encryption, where you encrypt before uploading.

## 53: What is S3 versioning and why does it matter for security?

Versioning keeps every version of every object. If something is overwritten or deleted, by mistake or by an attacker, you can restore an older version. A delete just adds a delete marker. Combined with MFA Delete or Object Lock, it protects against ransomware that tries to encrypt or wipe your data. Lifecycle rules can expire old versions to control cost.

## 54: What is S3 Object Lock?

Object Lock stores objects in a write-once-read-many (WORM) way. It needs versioning. It has two retention modes:

- Governance mode: most users cannot delete or change the object version before the retention date, but users with `s3:BypassGovernanceRetention` can.
- Compliance mode: nobody can delete the version or shorten retention until it ends, not even the root user.

There is also a legal hold, which blocks deletion with no end date until it is removed.

## 55: What are S3 ACLs and Object Ownership?

ACLs are the old access control system for buckets and objects. Object Ownership controls who owns uploaded objects and whether ACLs are used. The setting "Bucket owner enforced" disables ACLs completely so that only policies control access, and the bucket owner owns every object. Since April 2023 this is the default for new buckets. Keep ACLs disabled unless an old integration really needs them.

## 56: What is a VPC?

A Virtual Private Cloud is your own isolated network in an AWS region. You choose its IP range, split it into subnets across availability zones, and control routing, internet access and firewalls. Resources like EC2, RDS and Lambda (when attached to a VPC) live inside it.

## 57: What is the difference between a public and a private subnet?

A public subnet has a route to an internet gateway (`0.0.0.0/0 -> igw-...`), so instances with a public IP can be reached from the internet. A private subnet has no such route. Instances there can reach the internet only through a NAT gateway (outbound only), or not at all. Databases and app servers usually go in private subnets, and only load balancers sit in public ones.

## 58: What is a security group?

A security group is a stateful virtual firewall attached to a network interface (EC2, RDS, Lambda in a VPC, load balancers and so on). It only has allow rules. Because it is stateful, return traffic for an allowed connection is allowed automatically. By default it blocks all inbound traffic and allows all outbound traffic.

## 59: What is a network ACL?

A network ACL is a stateless firewall at the subnet level. It has numbered allow and deny rules, checked in order from the lowest number, and the first match wins. Because it is stateless, you must allow return traffic on ephemeral ports (1024-65535) yourself. The default NACL allows everything. Custom NACLs deny everything until you add rules.

## 60: How do security groups and NACLs differ?

|               | Security group        | Network ACL                           |
| ------------- | --------------------- | ------------------------------------- |
| Level         | Network interface     | Subnet                                |
| State         | Stateful              | Stateless                             |
| Rules         | Allow only            | Allow and deny                        |
| Order         | All rules checked     | Lowest number first, first match wins |
| Can reference | Other security groups | Only CIDR ranges                      |

Security groups do most of the work. NACLs are used for broad subnet-level blocks, like blocking a bad IP range.

## 61: What is a NAT gateway?

A NAT gateway sits in a public subnet and lets instances in private subnets start outbound connections to the internet (for updates or third-party APIs) while blocking unsolicited inbound connections. It is managed by AWS and scales on its own. It does not filter traffic by domain, so if you need egress filtering, add Network Firewall or a proxy.

## 62: What is a VPC endpoint?

A VPC endpoint lets resources in your VPC reach AWS services without going over the internet.

- Gateway endpoints: only for S3 and DynamoDB. Added as a route in the route table and free.
- Interface endpoints: an ENI with a private IP in your subnet, powered by PrivateLink. Available for most AWS services and billed per hour and per GB.

Endpoints keep traffic private and let you use endpoint policies and the `aws:SourceVpce` condition to lock things down.

## 63: What is AWS PrivateLink?

PrivateLink lets you expose a service from one VPC to many other VPCs or accounts privately, without VPC peering, internet gateways or overlapping IP worries. The provider puts the service behind a Network Load Balancer and creates an endpoint service. Consumers create an interface endpoint. Traffic only flows one way, from consumer to provider, which keeps the exposure small.

## 64: What are VPC Flow Logs?

Flow Logs record IP traffic metadata for a VPC, subnet or network interface: source and destination IP, ports, protocol, bytes, and whether it was `ACCEPT` or `REJECT`. They do not capture packet contents. Logs go to CloudWatch Logs, S3 or Amazon Data Firehose. They help with investigating suspicious connections and debugging security group rules, and GuardDuty analyzes flow log data on its own.

## 65: What is a bastion host and why do many teams stop using one?

A bastion (jump box) is a server in a public subnet that admins SSH into before reaching private servers. It needs an open inbound port, SSH key management, patching, and it is a prime target for attackers. Systems Manager Session Manager and EC2 Instance Connect Endpoint give shell access without opening inbound ports or managing long-lived keys, so most teams replace bastions with those.

## 66: What is Systems Manager Session Manager?

Session Manager gives you a browser or CLI shell on EC2 instances and on-premises servers through the SSM Agent. The agent connects outbound to Systems Manager, so you need no inbound ports, no bastion and no SSH keys. Access is controlled with IAM, and sessions can be logged to S3 or CloudWatch Logs.

```bash
aws ssm start-session --target i-0abc123def4567890
```

It can also forward ports, for example to reach a private database from your laptop.

## 67: What is Systems Manager Patch Manager?

Patch Manager scans and installs OS and some application patches on managed nodes. You define patch baselines (which patches to approve and when) and run patching on a schedule using maintenance windows or a patch policy in Quick Setup. It reports compliance, so you can see which instances are missing critical security patches.

## 68: What is AWS WAF?

AWS WAF is a web application firewall. You attach a web ACL to CloudFront, an Application Load Balancer, API Gateway REST APIs, AppSync, Cognito user pools, App Runner or Verified Access. Rules inspect HTTP requests and can allow, block, count, or send a CAPTCHA or challenge. It protects against things like SQL injection, cross-site scripting, bad bots and request floods.

## 69: What are AWS WAF managed rule groups?

They are ready-made rule sets maintained by AWS or by Marketplace sellers. Common AWS ones:

- `AWSManagedRulesCommonRuleSet` (core rule set, OWASP-style protections)
- `AWSManagedRulesKnownBadInputsRuleSet`
- `AWSManagedRulesSQLiRuleSet`
- `AWSManagedRulesAmazonIpReputationList`
- `AWSManagedRulesBotControlRuleSet`
- `AWSManagedRulesATPRuleSet` (account takeover prevention)

Start new rule groups in count mode, check for false positives, then switch to block.

## 70: What is a rate-based rule in AWS WAF?

A rate-based rule counts requests per key (by default per IP) over a time window and acts when the count goes over a limit. You can pick an evaluation window of 1, 2, 5 or 10 minutes, and aggregate by things like a header, cookie, query argument or forwarded IP. It helps against brute-force logins, scraping and simple HTTP floods.

## 71: What is AWS Shield Standard?

Shield Standard is free and on by default for every AWS customer. It protects against common network and transport layer DDoS attacks, like SYN floods and UDP reflection attacks, on AWS edge and regional services. You do not have to set anything up. It works best for resources behind CloudFront, Route 53 and Global Accelerator.

## 72: What is AWS Shield Advanced?

Shield Advanced is a paid subscription for extra DDoS protection on CloudFront, Route 53, Global Accelerator, load balancers and Elastic IPs. It adds:

- Detection tuned to your traffic and automatic application layer mitigation with WAF
- Access to the Shield Response Team (SRT) during attacks
- Cost protection for scaling charges caused by a DDoS
- Health-based detection using Route 53 health checks
- WAF and Firewall Manager at no extra cost for protected resources

## 73: How does AWS help you handle DDoS attacks?

Mostly through architecture. Put CloudFront and Route 53 in front, since they run on a large global edge network that absorbs a lot of traffic. Add WAF with rate-based rules for application layer floods. Use Auto Scaling and load balancers so the app can take spikes. Keep origins private so attackers cannot go around the edge. Shield Standard is always on, and Shield Advanced adds response support and cost protection.

## 74: What basic security settings should a CloudFront distribution have?

- Viewer protocol policy set to "Redirect HTTP to HTTPS" or "HTTPS only"
- A modern TLS security policy (TLSv1.2_2021 or newer) with an ACM certificate
- Origin Access Control so the S3 origin is private
- A custom origin reachable only from CloudFront (managed prefix list or a secret header)
- A WAF web ACL attached
- A response headers policy that adds security headers like HSTS and X-Content-Type-Options
- Standard logging turned on

## 75: What is CloudFront Origin Access Control (OAC)?

OAC lets CloudFront sign its requests to an S3 origin with SigV4, so the bucket can stay fully private and only allow the CloudFront distribution. It replaces the older Origin Access Identity (OAI). OAC supports SSE-KMS encrypted objects, all regions, and PUT/POST requests.

```json
{
  "Effect": "Allow",
  "Principal": { "Service": "cloudfront.amazonaws.com" },
  "Action": "s3:GetObject",
  "Resource": "arn:aws:s3:::site-assets/*",
  "Condition": {
    "StringEquals": {
      "AWS:SourceArn": "arn:aws:cloudfront::111122223333:distribution/E1ABCDEF2GHIJ"
    }
  }
}
```

## 76: What is the difference between CloudFront signed URLs and signed cookies?

Both limit access to private content served through CloudFront. A signed URL grants access to one file, good for a single download link. Signed cookies grant access to many files at once without changing their URLs, good for a whole paid video library or an HLS stream with many segments. Both are signed with a private key whose public key is in a CloudFront key group.

## 77: What authorization options does API Gateway have?

- IAM authorization (SigV4-signed requests)
- Cognito user pool authorizers (REST APIs)
- JWT authorizers (HTTP APIs), for any OIDC provider
- Lambda authorizers (custom code checking a token or request parameters)
- API keys with usage plans (for metering and throttling, not real authentication)
- Resource policies (REST APIs) to limit by account, IP or VPC endpoint
- Mutual TLS on custom domains

## 78: What is a Lambda execution role?

It is the IAM role a Lambda function assumes when it runs. The function's code gets temporary credentials for this role through environment variables. It needs at least permission to write logs to CloudWatch Logs (`AWSLambdaBasicExecutionRole`), plus whatever the code calls, like DynamoDB or S3. Give each function its own role so a bug in one function cannot reach another function's data.

## 79: What is a Lambda resource-based policy?

It controls who can invoke the function (or manage it), for example allowing S3, SNS, API Gateway or another account to call it.

```bash
aws lambda add-permission \
  --function-name thumbnail \
  --statement-id s3-invoke \
  --action lambda:InvokeFunction \
  --principal s3.amazonaws.com \
  --source-arn arn:aws:s3:::uploads-bucket \
  --source-account 111122223333
```

Always add `--source-arn` and `--source-account` for service principals, so some other account's bucket cannot invoke your function.

## 80: How are Lambda environment variables protected?

Lambda encrypts environment variables at rest with an AWS managed KMS key by default. You can use a customer managed key instead. Anyone with `lambda:GetFunctionConfiguration` can still read the values, so environment variables are not a good place for real secrets. Store secrets in Secrets Manager or Parameter Store and fetch them at runtime, for example with the Parameters and Secrets Lambda extension.

## 81: What auth types can a Lambda function URL use?

- `AWS_IAM`: callers must sign requests with SigV4 and have `lambda:InvokeFunctionUrl` permission.
- `NONE`: anyone on the internet can call it. Your code must do its own auth.

Function URLs have no WAF and no built-in throttling per client. For public APIs, either put CloudFront with OAC in front of an `AWS_IAM` function URL, or use API Gateway.

## 82: What does ECR image scanning do?

It checks container images for known vulnerabilities (CVEs).

- Basic scanning: free, scans OS packages on push or manually.
- Enhanced scanning: uses Amazon Inspector, scans OS and programming language packages, and keeps rescanning images when new CVEs are published.

Findings show severity and fixed versions, and enhanced scanning findings flow into Security Hub and EventBridge.

## 83: What is the difference between an ECS task role and a task execution role?

- The task execution role is used by the ECS agent and Fargate to start the task: pull the image from ECR, send logs to CloudWatch, and fetch secrets referenced in the task definition.
- The task role is used by your application code inside the container to call AWS services like S3 or SQS.

Keep them separate so the app does not get the agent's permissions and the agent does not get the app's.

## 84: How does Fargate isolate workloads?

Each Fargate task (or EKS pod on Fargate) runs in its own micro VM with its own kernel, CPU, memory and network interface. Tasks do not share a kernel with other customers' tasks or with your other tasks. You also cannot run privileged containers or access the host, which removes a whole class of container escape attacks.

## 85: How do you encrypt an RDS database?

Select encryption when you create the instance or cluster and pick a KMS key. This encrypts storage, automated backups, snapshots and read replicas. You cannot turn on encryption for an existing unencrypted instance directly. Instead, take a snapshot, copy it with encryption on, and restore from the encrypted copy.

## 86: How do you keep an RDS database off the internet?

- Put it in private subnets with a DB subnet group that has no internet route
- Set "Publicly accessible" to No
- Allow inbound only from the app's security group on the database port
- Connect with TLS and use IAM database authentication or Secrets Manager for credentials
- For admin access, use Session Manager port forwarding or a VPN instead of opening the database

## 87: How is DynamoDB data encrypted?

All DynamoDB tables are encrypted at rest and you cannot turn it off. You choose between an AWS owned key (default, free), an AWS managed key (`aws/dynamodb`) or a customer managed key. Data in transit is protected with HTTPS. For very sensitive fields, you can also encrypt on the client with the AWS Database Encryption SDK.

## 88: What is IAM database authentication?

It lets you connect to RDS or Aurora MySQL and PostgreSQL with a short-lived token instead of a password. The token is valid for 15 minutes and is generated with your IAM credentials.

```bash
aws rds generate-db-auth-token \
  --hostname orders.abc123.eu-west-1.rds.amazonaws.com \
  --port 5432 --username app_user --region eu-west-1
```

The IAM identity needs `rds-db:connect` on the database user's ARN, and the connection must use TLS.

## 89: What is AWS CloudTrail?

CloudTrail records API calls in your account: who called what, when, from where, and whether it worked. It covers the console, CLI, SDKs and AWS services acting for you. It is the main source for audits and incident investigations.

## 90: What is the difference between CloudTrail management events and data events?

- Management events are control plane actions like `CreateUser`, `RunInstances` or `PutBucketPolicy`. They are logged by default.
- Data events are high-volume data plane actions like S3 `GetObject`/`PutObject`, Lambda `Invoke` or DynamoDB item reads. They are off by default and cost extra.

Turn on data events at least for sensitive S3 buckets, so you can see who read or deleted objects.

## 91: What is CloudTrail event history and why is it not enough?

Event history shows the last 90 days of management events in a region for free, without any setup. It does not include data events, cannot be kept longer than 90 days and is not stored somewhere you control. For real auditing, create a trail (ideally an organization trail) that delivers logs to an S3 bucket in a separate log archive account, or use CloudTrail Lake.

## 92: What is CloudWatch Logs used for in security?

It collects logs from Lambda, ECS, EC2 (through the CloudWatch agent), API Gateway, VPC Flow Logs, CloudTrail and more. You can search them with Logs Insights, create metric filters that turn log patterns into metrics, set alarms, and send data to other tools through subscription filters. Log groups can be encrypted with KMS and have a retention period.

## 93: How do you get alerted when someone signs in as root?

Create an EventBridge rule that matches root console sign-ins from CloudTrail and sends them to SNS, Slack or your incident tool.

```json
{
  "detail-type": ["AWS Console Sign In via CloudTrail"],
  "detail": {
    "userIdentity": { "type": ["Root"] }
  }
}
```

The older way, a CloudWatch Logs metric filter plus alarm on the CloudTrail log group, still works and is what the CIS benchmark describes.

## 94: What is AWS Config?

Config records the configuration of your resources over time and checks them against rules. You can see what a security group looked like last Tuesday and who changed it (linked to CloudTrail). Config rules mark resources as compliant or non-compliant, for example "S3 buckets must block public access" or "EBS volumes must be encrypted".

## 95: What is the difference between managed and custom Config rules?

Managed rules are predefined by AWS, like `s3-bucket-public-read-prohibited` or `iam-user-mfa-enabled`. You just turn them on and set parameters. Custom rules are your own logic, written as a Lambda function or in Guard (the CloudFormation Guard policy language), for checks AWS does not provide.

## 96: What is Amazon GuardDuty?

GuardDuty is a threat detection service. It analyzes CloudTrail events, VPC Flow Logs and DNS logs, and with optional protection plans also S3 data events, EKS audit logs, runtime activity, RDS logins, Lambda network activity and malware in EBS volumes or S3 uploads. It produces findings like "EC2 instance talking to a known crypto mining pool" or "API calls from a Tor exit node". It uses threat intel and machine learning, and you do not manage any agents for the base features.

## 97: What is AWS Security Hub?

Since December 2025 there are two related services:

- Security Hub (the new version) pulls together findings from GuardDuty, Inspector, Macie, Security Hub CSPM and others, correlates them, and shows prioritized risks and exposure.
- Security Hub CSPM (the original Security Hub, renamed) runs automated checks against standards like the AWS Foundational Security Best Practices and CIS AWS Foundations Benchmark and gives a security score.

Both are usually turned on organization-wide from a delegated administrator account.

## 98: What is Amazon Inspector?

Inspector scans for software vulnerabilities and unintended network exposure. It covers EC2 instances (through the SSM agent or agentless snapshots), ECR container images and Lambda functions (packages and, optionally, code). It rescans when new CVEs come out and gives a risk score that takes into account things like network reachability.

## 99: What is Amazon Macie?

Macie finds sensitive data in S3, like credit card numbers, passport numbers, API keys and personal data. It also checks bucket security, flagging buckets that are public, unencrypted or shared with other accounts. You can run sampled automated discovery across all buckets or full discovery jobs on chosen buckets.

## 100: What is Amazon Detective?

Detective helps you investigate security findings. It automatically builds a graph from CloudTrail, VPC Flow Logs, GuardDuty findings and EKS audit logs, then shows how a role, IP address or instance behaved over time. When GuardDuty says a role did something odd, Detective helps you answer "is that normal for this role, and what else did it touch?"

## 101: What is Amazon Security Lake?

Security Lake collects security logs from AWS sources (CloudTrail, VPC Flow Logs, Route 53 resolver logs, Security Hub findings, EKS audit logs, WAF logs) and third-party tools into an S3-based data lake in your account. It converts them to the Open Cybersecurity Schema Framework (OCSF) format in Apache Parquet. SIEM tools and analytics services like Athena can then query one consistent format.

## 102: How is EventBridge used for security?

EventBridge receives events from AWS services, including CloudTrail API calls, GuardDuty findings, Security Hub findings and Config compliance changes. You write rules that match events and send them to targets like SNS, Lambda, Step Functions or Systems Manager Automation. This is how teams build alerts and automatic fixes, for example closing a security group that was opened to the world.

## 103: What security checks does AWS Trusted Advisor do?

Trusted Advisor checks your account against best practices. Security checks include open security group ports, root account MFA, S3 bucket permissions, IAM use, exposed access keys and CloudTrail logging. Basic and Developer support plans get a few core checks. Business support and higher get the full set. Many of these checks now come from Security Hub CSPM.

## 104: What is AWS Artifact?

Artifact is a self-service portal for AWS compliance reports and agreements. You can download AWS's SOC 1/2/3 reports, PCI DSS attestation, ISO certificates and others, and accept agreements like the HIPAA Business Associate Addendum (BAA). These reports cover AWS's side of the shared responsibility model. Your own audit still has to cover your side.

## 105: What is AWS Audit Manager?

Audit Manager helps you collect evidence for audits. You pick a framework (like SOC 2, PCI DSS, HIPAA or CIS), and it continuously gathers evidence from Config, Security Hub CSPM, CloudTrail and API calls and maps it to controls. Auditors can then review assessment reports instead of you collecting screenshots by hand.

## 106: Does using AWS make your app HIPAA or PCI compliant?

No. AWS is certified for many programs and lists which services are "in scope". Using in-scope services is required, but you still have to configure them correctly and run your own controls: encryption, access control, logging, backups, policies and processes. For HIPAA you also need to accept the BAA in Artifact. Compliance is shared, just like security.

## 107: What is AWS Backup?

AWS Backup is a central service to back up EBS, EC2, RDS, Aurora, DynamoDB, EFS, FSx, S3 and more. You define backup plans (schedule, retention, lifecycle, cross-region and cross-account copies) and assign resources by tag. Backups are stored in backup vaults, each encrypted with a KMS key and protected by a vault access policy.

## 108: What is AWS Backup Vault Lock?

Vault Lock stops anyone from deleting backups early or changing retention settings. In governance mode, users with enough IAM permissions can still remove the lock. In compliance mode, after a short grace period, nobody can change or delete it, including the root user and AWS. It is a key protection against ransomware and against insiders who want to destroy backups before an attack.

## 109: What is attribute-based access control (ABAC) on AWS?

ABAC grants access based on tags (attributes) instead of listing each resource. For example, a developer with the tag `project=apollo` can manage any resource also tagged `project=apollo`. New resources work without editing policies as long as they are tagged correctly. It uses condition keys like `aws:PrincipalTag`, `aws:ResourceTag` and `aws:RequestTag`.

## 110: What is a permissions boundary?

A permissions boundary is a managed policy you attach to a user or role to set the maximum permissions it can ever have. The effective permissions are the overlap between the identity's policies and the boundary. Boundaries are mostly used to let developers create their own roles safely: they can create roles, but only if those roles carry the same boundary.

## 111: What is a session policy?

A session policy is a policy you pass when you assume a role or create a federated session. It limits the session to the overlap of the role's permissions and the session policy. It never adds permissions. It is useful when one role serves many callers and you want to narrow each session, for example limiting it to one S3 prefix.

```bash
aws sts assume-role --role-arn arn:aws:iam::111122223333:role/DataAccess \
  --role-session-name job-42 \
  --policy file://only-job-42-prefix.json
```

## 112: What is the Security Pillar of the AWS Well-Architected Framework?

It is one of six pillars of the Well-Architected Framework. It describes how to protect data, systems and assets. It is split into areas: security foundations, identity and access management, detection, infrastructure protection, data protection, incident response and application security. The Well-Architected Tool lets you review a workload against these questions.

## 113: What are the design principles of the Security Pillar?

- Implement a strong identity foundation (least privilege, central identity, no long-term credentials)
- Maintain traceability (logs and alerts)
- Apply security at all layers
- Automate security best practices
- Protect data in transit and at rest
- Keep people away from data
- Prepare for security events

## 114: What is AWS Network Firewall?

Network Firewall is a managed, stateful network firewall and intrusion prevention service for VPCs. You route traffic through firewall endpoints in dedicated subnets. It supports stateless rules, stateful rules, Suricata-compatible IPS rules, and domain lists to allow or block outbound traffic by hostname (using SNI and the HTTP Host header). It is often placed in a central inspection VPC behind a Transit Gateway.

## 115: What is Route 53 Resolver DNS Firewall?

DNS Firewall filters DNS queries made from your VPCs through the Route 53 Resolver. You create rules with domain lists (your own or AWS managed lists of malware and botnet domains) and actions to allow, block or alert. It helps stop malware from calling home and stops data being leaked through DNS lookups to attacker domains.

## 116: What is the EC2 instance metadata service and what is IMDSv2?

IMDS is a local endpoint at `169.254.169.254` that gives an instance information about itself, including temporary credentials for its role. IMDSv1 answers simple GET requests, which SSRF bugs can abuse. IMDSv2 requires a session token obtained with a PUT request first, and the token response has a hop limit, which blocks most SSRF attacks.

```bash
TOKEN=$(curl -s -X PUT "http://169.254.169.254/latest/api/token" \
  -H "X-aws-ec2-metadata-token-ttl-seconds: 21600")
curl -s -H "X-aws-ec2-metadata-token: $TOKEN" \
  http://169.254.169.254/latest/meta-data/iam/security-credentials/
```

## 117: What is a data perimeter?

A data perimeter is a set of preventive guardrails that make sure only trusted identities can access trusted resources from expected networks. It is built with SCPs, RCPs, resource policies and VPC endpoint policies using conditions like `aws:PrincipalOrgID`, `aws:ResourceOrgID` and `aws:SourceVpce`. Even if a credential leaks, it cannot be used to copy data out to an attacker's account or from an unknown network.

## 118: What are the two basic ways to give another account access to your resources?

1. Role assumption: create a role in your account that trusts the other account. Their users assume it and act in your account.
2. Resource-based policy: add the other account as a principal in the resource's policy (S3 bucket, KMS key, SQS queue and so on). Their users access the resource directly while keeping their own identity.

In both cases, the other account must also grant its own users permission in an identity-based policy.

## 119: How do pods in EKS get AWS permissions?

There are two current options:

- EKS Pod Identity: you install the Pod Identity Agent add-on and create a pod identity association between a Kubernetes service account and an IAM role. It is the simpler, newer option.
- IAM Roles for Service Accounts (IRSA): uses the cluster's OIDC provider and `AssumeRoleWithWebIdentity`, with the role ARN annotated on the service account.

Both give each pod its own role, so you do not have to give the node role broad permissions.

## 120: What is AWS Firewall Manager?

Firewall Manager centrally manages firewall rules across all accounts in an organization. It can deploy and enforce WAF web ACLs, Shield Advanced protections, security group policies, Network Firewall and DNS Firewall rules. When a new account or resource appears, the policy is applied automatically. It requires AWS Organizations and AWS Config.

## 121: What is the IAM policy simulator?

It is a tool to test whether a user, group or role is allowed to call certain actions on certain resources, given their attached policies. It also lets you test a draft policy before attaching it. The CLI version is `aws iam simulate-principal-policy`. It helps debug "Access Denied" errors without trial and error in production.

## 122: How do you check which identity your CLI is using?

```bash
aws sts get-caller-identity
```

It returns the account ID, the user or role ARN and the user ID. This call needs no permissions and cannot be denied by IAM policies. It is the first thing to run when you get an unexpected "Access Denied" or worry you are in the wrong account.

## 123: Where should you never store AWS secrets?

- In source code or Git history
- In Docker images or AMIs
- In plain text environment variables in task definitions or CloudFormation templates
- In public S3 buckets, wikis or chat tools
- In frontend JavaScript or mobile app bundles

Store them in Secrets Manager or Parameter Store, and better yet, avoid static secrets for AWS access entirely by using roles.

## 124: What happens when AWS finds your access key on public GitHub?

AWS scans public code repositories for exposed keys. When it finds one, it attaches the `AWSCompromisedKeyQuarantineV3` managed policy to the IAM user, which denies many risky actions, opens a support case and emails the account contact. The key still works for other actions and is not deleted. You must still deactivate it, rotate it and check CloudTrail for what the attacker did.

## 125: What does defense in depth mean on AWS?

It means using several layers of controls, so if one fails another still stops the attack. For a web app this could be: WAF at the edge, private subnets, tight security groups, IAM roles with least privilege, encryption with KMS key policies, SCPs at the organization level, and GuardDuty to detect what gets through. No single misconfiguration should expose your data.

## 126: Why reference security groups instead of IP addresses?

A security group rule can allow traffic from another security group, for example "allow port 5432 from the app-servers security group". Any instance in that group is allowed, even when IPs change because of scaling or redeploys. This is cleaner and tighter than allowing the whole subnet CIDR. It works within the same VPC and across peered VPCs in the same region.

## 127: What is AWS Private Certificate Authority?

AWS Private CA is a managed private certificate authority. It issues certificates for internal services, mutual TLS between microservices, IoT devices or VPN clients. You do not have to run your own CA servers, and keys are protected by HSMs. ACM can issue and renew private certificates from it for use with load balancers. There is a short-lived certificate mode with lower cost for certificates valid up to 7 days.

## 128: How do you force clients to use TLS when calling AWS services?

Add a deny statement with the `aws:SecureTransport` condition to the resource policy, so any HTTP request fails. This works on S3 buckets, SQS queues, SNS topics and other resources with resource policies. You can also require a minimum TLS version for S3 with the `s3:TlsVersion` condition key. Most AWS service endpoints already require TLS 1.2 or higher.

## 129: How do you make sure S3 objects are always encrypted with your KMS key?

Set default bucket encryption to SSE-KMS with your key and turn on S3 Bucket Keys to reduce KMS costs. Then, if needed, add a bucket policy that denies uploads using a different key:

```json
{
  "Sid": "DenyWrongKey",
  "Effect": "Deny",
  "Principal": "*",
  "Action": "s3:PutObject",
  "Resource": "arn:aws:s3:::finance-data/*",
  "Condition": {
    "StringNotEqualsIfExists": {
      "s3:x-amz-server-side-encryption-aws-kms-key-id": "arn:aws:kms:eu-west-1:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab"
    }
  }
}
```

## 130: What is CloudTrail log file integrity validation?

When turned on, CloudTrail creates a digest file every hour with SHA-256 hashes of the log files delivered in that hour, signed with SHA-256 and RSA. Later you can prove the logs were not changed or deleted:

```bash
aws cloudtrail validate-logs \
  --trail-arn arn:aws:cloudtrail:eu-west-1:111122223333:trail/org-trail \
  --start-time 2026-11-01T00:00:00Z
```

This is important for audits and forensics.

## 131: What is an organization trail?

An organization trail is a CloudTrail trail created in the management account (or a delegated admin account) that logs events for every account in the organization. Member accounts can see it but cannot change or delete it. Logs usually go to an S3 bucket in a dedicated log archive account. New accounts are covered automatically.

## 132: What does AWS Systems Manager offer for security?

- Session Manager: shell access without SSH or open ports
- Patch Manager: OS patching and compliance
- Parameter Store: config values and secrets
- Run Command: run scripts on many instances without SSH
- Automation: runbooks for remediation and incident response
- Inventory: what software is installed where
- State Manager: keep instances in a known configuration

## 133: What is the difference between GuardDuty, Inspector and Macie?

- GuardDuty finds threats: suspicious activity and attacks happening now.
- Inspector finds vulnerabilities: weak spots in software and network exposure that could be attacked.
- Macie finds sensitive data in S3 and risky bucket settings.

They complement each other and all send findings to Security Hub.

## 134: What should every new AWS account have turned on?

A basic security baseline:

- Root MFA, no root access keys
- IAM Identity Center for people, roles for workloads
- An organization CloudTrail trail with log file validation
- AWS Config recording
- GuardDuty and Security Hub CSPM (organization-wide)
- IAM Access Analyzer
- S3 Block Public Access at the account level
- EBS encryption by default
- IMDSv2 as the default for new instances
- Budget and billing alerts, which often catch crypto mining first

## 135: What is AWS Security Incident Response?

It is a service (launched in December 2024) that helps you prepare for, respond to and recover from security incidents. It triages findings from GuardDuty and Security Hub, gives you a case management workflow, and gives access to the AWS Customer Incident Response Team (CIRT) around the clock. It is a paid service, organized at the organization level.

## 136: How does infrastructure as code help security?

With CloudFormation, CDK or Terraform, every resource is defined in code that goes through code review and version control. You can scan templates for mistakes before deployment, rebuild environments the same way every time, detect drift from the approved state, and see who changed what in Git. Manual console changes are harder to review and easy to forget.

## 137: What tools scan IaC for security problems?

- Checkov (Terraform, CloudFormation, CDK output, Kubernetes)
- Trivy (includes the checks from the former tfsec project)
- cfn-nag and cfn-lint for CloudFormation
- CloudFormation Guard for policy-as-code rules
- cdk-nag for CDK apps
- KICS
- Open Policy Agent (OPA) or Conftest for custom rules

Run them in CI on every pull request so problems are caught before they reach AWS.

## 138: How does GitHub Actions authenticate to AWS without access keys?

GitHub issues a short-lived OIDC token for each workflow run. You register GitHub's OIDC provider (`token.actions.githubusercontent.com`) in IAM and create a role that trusts it, limited to your repository and branch. The workflow asks for the token and calls `AssumeRoleWithWebIdentity` through the `aws-actions/configure-aws-credentials` action.

```yaml
permissions:
  id-token: write
  contents: read

steps:
  - uses: aws-actions/configure-aws-credentials@v4
    with:
      role-to-assume: arn:aws:iam::111122223333:role/gh-deploy
      aws-region: eu-west-1
```

## 139: Why is OIDC better than storing access keys in CI secrets?

There are no long-lived keys to leak, rotate or forget. Each job gets credentials that last about an hour. The role's trust policy can limit which repository, branch or environment may use it, so a fork or another repo cannot. And CloudTrail shows the role session name, which can be tied back to the workflow run.

## 140: What is a deploy role?

A deploy role is the IAM role that a CI/CD pipeline assumes to deploy infrastructure or code. It should have only the permissions the deployment needs, be trusted only by the pipeline's identity (OIDC subject or CodePipeline), exist separately per environment and account, and be blocked by SCPs from things like turning off CloudTrail. It is a high-value target, so treat it like an admin credential.

## 141: What are common S3 security mistakes?

- Turning off Block Public Access to "fix" an access problem
- Using `"Principal": "*"` without conditions in a bucket policy
- Leaving ACLs enabled and granting access to "Authenticated Users" (any AWS account)
- No versioning or Object Lock on important data
- Not logging data events for sensitive buckets
- Generating presigned URLs that last days instead of minutes
- Storing backups or logs in the same account as production

## 142: What are common IAM mistakes?

- Using the root user for daily work
- Creating IAM users with access keys for everyone, then never rotating them
- `"Action": "*"` and `"Resource": "*"` everywhere
- Giving `iam:PassRole` on `*`
- Trust policies that trust a whole account or `"AWS": "*"` without conditions
- Sharing one role between many unrelated workloads
- Not removing permissions and users when people leave

## 143: Do you need permission from AWS to run a penetration test?

For a list of common services (EC2, RDS, Aurora, CloudFront, API Gateway, Lambda, Lightsail, Elastic Beanstalk and others), you can pen test your own resources without asking first. Some activities are not allowed, like DNS zone walking against Route 53 hosted zones, DoS or flood testing, and attacking AWS infrastructure itself. DDoS simulation tests must follow a separate policy and use an approved partner.

## 144: What is the difference between CloudTrail and CloudWatch?

CloudTrail records API activity: who did what to which resource. CloudWatch collects metrics and logs from your resources and applications and lets you set alarms. In security you use both: CloudTrail tells you that someone changed a security group, while CloudWatch can raise an alarm when a log pattern or metric (like failed logins) crosses a limit.

## 145: What is a KMS key policy?

Every KMS key has a key policy, which is its resource-based policy. Unlike most resources, IAM policies alone cannot grant access to a KMS key. The key policy must allow it, either directly or by allowing the account root principal, which then lets IAM policies grant access. If the key policy loses all admin access, you need AWS Support to recover it.

## 146: How does KMS key rotation work?

For symmetric customer managed keys you can turn on automatic rotation, with a period from 90 days to 7 years (365 days by default). You can also rotate on demand. KMS creates new key material but keeps old material, so data encrypted earlier can still be decrypted. The key ID and ARN stay the same, so apps do not change. AWS managed keys rotate every year automatically.

## 147: How does Secrets Manager rotation work?

Rotation uses a Lambda function (or managed rotation for some services) that runs on a schedule you set, as often as every 4 hours. It follows four steps: create a new secret version, set it in the database or service, test it, then mark it as current. Apps that always fetch the current version from Secrets Manager pick up the new value without a redeploy.

## 148: How can you add MFA to a Cognito user pool?

You set MFA to off, optional or required, and choose methods: SMS text messages, TOTP authenticator apps, or email codes (email requires the Essentials or Plus feature plan). The Essentials and Plus plans also support passkeys (WebAuthn) for passwordless sign-in. Threat protection (formerly advanced security features) can require MFA only when a sign-in looks risky.

## 149: What are AWS managed job function policies?

They are AWS managed policies built around common job roles, such as `AdministratorAccess`, `PowerUserAccess`, `ReadOnlyAccess`, `ViewOnlyAccess`, `SecurityAudit`, `DatabaseAdministrator` and `NetworkAdministrator`. They are a quick start but usually broader than needed. Note that `ReadOnlyAccess` lets you read data such as S3 objects and DynamoDB items, while `ViewOnlyAccess` only lists and describes resources.

## 150: What is a break-glass account?

It is an emergency access path used only when normal access fails, for example if your identity provider is down or IAM Identity Center is misconfigured. It is usually an IAM user or role with admin rights, protected by strong MFA, with credentials stored in a safe place and split between people. Any use should trigger alerts and be reviewed afterward.

# Moderate Questions (151-300)

## 151: How does IAM decide whether to allow a request in a single account?

Roughly in this order:

1. If any applicable policy has an explicit `Deny` that matches, the request is denied.
2. If an SCP or RCP in the organization does not allow it, it is denied.
3. If a resource-based policy allows it, it is usually allowed (with some exceptions, like when a permissions boundary or session policy applies to a role session).
4. If a permissions boundary exists and does not allow it, it is denied.
5. If a session policy exists and does not allow it, it is denied.
6. If an identity-based policy allows it, it is allowed.
7. Otherwise it is implicitly denied.

The short version: deny beats allow, and something has to allow it.

## 152: How is policy evaluation different for cross-account requests?

For a request from account A to a resource in account B, both sides must allow it. Account A's identity-based policy must allow the action, and account B's resource-based policy (or the trust policy of a role in B) must allow the principal from A. An allow on only one side is not enough. SCPs of account A and RCPs of account B also apply.

## 153: How do SCPs combine with IAM policies?

SCPs filter. The effective permission is the overlap between what the SCPs allow and what the IAM policies allow. SCPs are applied at the root, each OU and each account. A request must be allowed at every level from the root down to the account. That is why the default `FullAWSAccess` SCP is attached everywhere: if you remove it and attach nothing else, nothing is allowed. An explicit deny in any SCP at any level blocks the action.

## 154: What are resource control policies (RCPs)?

RCPs, added to Organizations in November 2024, are like SCPs but for resources. An SCP limits what your principals can do. An RCP limits what anyone, including principals outside your organization, can do to your resources. They work for services like S3, STS, KMS, SQS, Secrets Manager, DynamoDB and others. A common use is denying access to your S3 buckets from any principal outside your organization, even if someone writes a bad bucket policy.

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "EnforceOrgIdentities",
      "Effect": "Deny",
      "Principal": "*",
      "Action": [
        "s3:*",
        "sqs:*",
        "kms:*",
        "secretsmanager:*",
        "sts:AssumeRole"
      ],
      "Resource": "*",
      "Condition": {
        "StringNotEqualsIfExists": { "aws:PrincipalOrgID": "o-a1b2c3d4e5" },
        "BoolIfExists": { "aws:PrincipalIsAWSService": "false" }
      }
    }
  ]
}
```

## 155: What is the difference between an allow-list and a deny-list SCP strategy?

- Deny list: keep `FullAWSAccess` and add SCPs that deny specific things (leave the organization, disable CloudTrail, use unapproved regions). Easy to maintain and the common choice.
- Allow list: remove `FullAWSAccess` and attach SCPs that allow only approved services. Tighter, but every new service needs an SCP change.

Many teams use deny lists for most OUs and allow lists for highly sensitive accounts.

## 156: How do you write an SCP that limits which regions can be used?

Deny everything outside the approved regions, but exclude global services with `NotAction`, since their API calls go to `us-east-1`.

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "DenyOtherRegions",
      "Effect": "Deny",
      "NotAction": [
        "iam:*",
        "organizations:*",
        "route53:*",
        "cloudfront:*",
        "sts:*",
        "support:*",
        "budgets:*",
        "waf:*",
        "globalaccelerator:*"
      ],
      "Resource": "*",
      "Condition": {
        "StringNotEquals": {
          "aws:RequestedRegion": ["eu-west-1", "eu-central-1"]
        },
        "ArnNotLike": {
          "aws:PrincipalARN": "arn:aws:iam::*:role/OrgBreakGlass"
        }
      }
    }
  ]
}
```

Control Tower also offers a region deny control that does the same.

## 157: How do you use a permissions boundary to let developers create roles safely?

Give developers `iam:CreateRole` and `iam:PutRolePolicy` only if the new role has a specific boundary attached, and block them from changing or removing the boundary.

```json
{
  "Effect": "Allow",
  "Action": ["iam:CreateRole", "iam:AttachRolePolicy", "iam:PutRolePolicy"],
  "Resource": "arn:aws:iam::111122223333:role/app/*",
  "Condition": {
    "StringEquals": {
      "iam:PermissionsBoundary": "arn:aws:iam::111122223333:policy/DevBoundary"
    }
  }
}
```

Add a separate deny on `iam:DeleteRolePermissionsBoundary` and on changing the `DevBoundary` policy itself. Now any role they create can never have more than the boundary allows.

## 158: What is iam:PassRole and why is it dangerous?

When you launch an EC2 instance, create a Lambda function or start an ECS task with a role, you "pass" that role to the service. This needs `iam:PassRole` on the role. If a user can pass any role (`Resource: *`), they can launch a function with an admin role and run code as admin, which is privilege escalation. Always limit `iam:PassRole` to specific role ARNs and add the `iam:PassedToService` condition.

```json
{
  "Effect": "Allow",
  "Action": "iam:PassRole",
  "Resource": "arn:aws:iam::111122223333:role/lambda/orders-*",
  "Condition": {
    "StringEquals": { "iam:PassedToService": "lambda.amazonaws.com" }
  }
}
```

## 159: Which condition operators should you know?

- `StringEquals`, `StringNotEquals`, `StringLike` (with `*` and `?`)
- `ArnEquals`, `ArnLike`
- `Bool` (for `aws:SecureTransport`, `aws:MultiFactorAuthPresent`)
- `IpAddress`, `NotIpAddress`
- `NumericLessThan` and friends, `DateGreaterThan` and friends
- `Null` (checks whether a key exists)
- `...IfExists` versions, which match when the key is missing
- `ForAnyValue:` and `ForAllValues:` for multi-valued keys like `aws:TagKeys`

Multiple conditions in one block are ANDed. Multiple values for one key are ORed.

## 160: What are policy variables?

Policy variables are placeholders replaced with request values at evaluation time, which lets one policy serve many users.

```json
{
  "Effect": "Allow",
  "Action": ["s3:GetObject", "s3:PutObject"],
  "Resource": "arn:aws:s3:::home-dirs/${aws:username}/*"
}
```

Other useful ones are `${aws:PrincipalTag/team}`, `${aws:userid}` and `${aws:PrincipalAccount}`. They only work in policies with version `2012-10-17`.

## 161: What are the risks of NotAction and NotResource?

`"Effect": "Allow"` with `NotAction` allows everything except the listed actions, including any new services AWS launches later. That is almost always too broad. `NotAction` is safe and useful with `Deny`, for example "deny everything except IAM when MFA is missing". `NotResource` has the same problem. Read these statements carefully in reviews.

## 162: How do you require MFA for sensitive actions?

Use the `aws:MultiFactorAuthPresent` or `aws:MultiFactorAuthAge` condition keys.

```json
{
  "Sid": "DenyStopWithoutMFA",
  "Effect": "Deny",
  "Action": ["ec2:StopInstances", "ec2:TerminateInstances"],
  "Resource": "*",
  "Condition": { "BoolIfExists": { "aws:MultiFactorAuthPresent": "false" } }
}
```

Use `BoolIfExists`, because long-term access key requests do not include the key at all, and plain `Bool` would not match them. For IAM Identity Center users, MFA is enforced at sign-in instead.

## 163: How do you set up a role that a third-party SaaS vendor can assume?

Create a role in your account that trusts the vendor's AWS account, and require an ExternalId that the vendor gives you, unique to your tenant.

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Principal": { "AWS": "arn:aws:iam::999988887777:root" },
      "Action": "sts:AssumeRole",
      "Condition": { "StringEquals": { "sts:ExternalId": "tenant-5f2a9c" } }
    }
  ]
}
```

Attach only the permissions the vendor needs, for example read-only access for a monitoring tool.

## 164: What is the confused deputy problem?

A confused deputy is a service with permissions that is tricked into using them for the wrong customer. Say a SaaS vendor assumes roles in many customer accounts. If an attacker signs up as a customer and enters your role ARN, the vendor would assume your role on the attacker's behalf. ExternalId fixes this: the vendor generates a unique ID per customer and always sends it, so the attacker cannot get the vendor to send your ID.

## 165: How do you prevent the confused deputy problem with AWS service principals?

When a resource policy or trust policy allows a service principal (like `sns.amazonaws.com` or `cloudtrail.amazonaws.com`), add `aws:SourceArn` or `aws:SourceAccount` conditions. Without them, the service could be used on behalf of a different account to access your resource.

```json
{
  "Effect": "Allow",
  "Principal": { "Service": "cloudtrail.amazonaws.com" },
  "Action": "s3:PutObject",
  "Resource": "arn:aws:s3:::org-trail-logs/AWSLogs/*",
  "Condition": {
    "StringEquals": {
      "aws:SourceArn": "arn:aws:cloudtrail:eu-west-1:111122223333:trail/org-trail"
    }
  }
}
```

## 166: What is role chaining and what limits it?

Role chaining is using a role's credentials to assume another role. For example, a developer assumes a role in a tools account, then from there assumes a role in production. The session duration of a chained role is limited to one hour, no matter what the role's maximum session duration is. Transitive session tags and source identity can carry through the chain so you can still trace who started it.

## 167: How long can a role session last?

Each role has a `MaxSessionDuration` from 1 hour (default) to 12 hours. The caller can ask for any `DurationSeconds` from 15 minutes up to that maximum. Role chaining is capped at 1 hour. Shorter sessions limit the damage of stolen credentials, so keep long sessions for cases like long-running batch jobs only.

## 168: What are session tags?

Session tags are key-value pairs passed when assuming a role, through `AssumeRole`, SAML attributes or OIDC claims. They become principal tags for that session, available as `aws:PrincipalTag/...` in policies. They let one role behave differently for each user, which is the base of ABAC with federation. Marking tags as transitive keeps them in role chains.

## 169: What is sts:SourceIdentity?

Source identity is a value set when a role is first assumed, typically the person's username from the IdP. Once set, it cannot be changed for the rest of the session or any chained sessions, and it appears in CloudTrail for every action. This answers "which human did this" even after several role hops. You can require it in trust policies with the `sts:SourceIdentity` condition key.

## 170: How does AssumeRoleWithWebIdentity work?

1. The workload gets an OIDC token (JWT) from an identity provider, like GitHub Actions, an EKS cluster, or Google.
2. It calls STS `AssumeRoleWithWebIdentity` with the token and the role ARN. The call does not need AWS credentials.
3. STS validates the token signature against the IdP's public keys and checks the role trust policy conditions (`aud`, `sub` and so on).
4. STS returns temporary credentials.

You must create an IAM OIDC identity provider for the issuer first. For mobile apps, Cognito identity pools are usually used instead of calling this directly.

## 171: How does SAML federation to AWS work?

1. The user signs in to the corporate IdP (Entra ID, Okta, ADFS).
2. The IdP sends a signed SAML assertion to the AWS sign-in endpoint. The assertion lists the roles the user may use.
3. AWS calls `AssumeRoleWithSAML` and checks the assertion against the SAML provider created in IAM and the role's trust policy.
4. The user gets a console session or CLI credentials for the chosen role.

With IAM Identity Center, Identity Center is the SAML service provider and you manage this setup once for all accounts.

## 172: What are permission sets in IAM Identity Center?

A permission set is a template of policies (AWS managed, customer managed, inline, and an optional permissions boundary) plus a session duration. When you assign a user or group to an account with a permission set, Identity Center creates an IAM role called `AWSReservedSSO_<name>_<id>` in that account. Changing the permission set updates the role in every account where it is assigned.

## 173: How do you connect IAM Identity Center to an external identity provider?

Set the identity source to an external IdP. Then:

1. Exchange SAML metadata between the IdP and Identity Center so users sign in through the IdP.
2. Turn on SCIM automatic provisioning, so users and groups are created, updated and removed in Identity Center when they change in the IdP.
3. Assign IdP groups to accounts with permission sets.

With SCIM, when someone leaves and is disabled in the IdP, they lose AWS access automatically.

## 174: How do you use attributes from your IdP for access control in Identity Center?

Turn on "Attributes for access control" in Identity Center and map attributes like `department` or `costCenter` from the IdP. They become session tags on the role session. Permission set policies can then compare `aws:PrincipalTag/costCenter` with `aws:ResourceTag/costCenter`, so one permission set covers every team without writing a policy per team.

## 175: How do you use IAM Access Analyzer to move toward least privilege?

1. Create an unused access analyzer for the organization and review findings for roles, keys and permissions not used for 90 days or more.
2. For a role that is too broad, use policy generation: Access Analyzer reads CloudTrail and writes a policy with the actions actually used.
3. Review the generated policy, add resource ARNs and conditions, and replace the broad policy.
4. Keep external access analyzers on to catch new public or cross-account sharing.

## 176: How can you check IAM policies in a CI pipeline?

Access Analyzer has APIs for custom policy checks that you can call from CI:

- `ValidatePolicy`: syntax errors and best practice warnings
- `CheckNoNewAccess`: does the new policy grant more than the old one?
- `CheckAccessNotGranted`: does it grant any of these sensitive actions or resources?
- `CheckNoPublicAccess`: does this resource policy make the resource public?

```bash
aws accessanalyzer check-access-not-granted \
  --policy-document file://policy.json \
  --access '[{"actions":["iam:CreateUser","s3:DeleteBucket"]}]' \
  --policy-type IDENTITY_POLICY
```

The IAM Policy Validator for CloudFormation and Terraform wraps these for IaC.

## 177: How do you use "last accessed" information?

IAM shows when each service (and for some services, each action) was last used by a user, role, group or policy, and Organizations shows the same per OU or account. If a role has `s3:*`, `dynamodb:*` and `sqs:*` but only used S3 in the last 90 days, you can remove DynamoDB and SQS. You can see it in the console under "Last Accessed" or with `aws iam generate-service-last-accessed-details`.

## 178: What kinds of controls does Control Tower have?

- Preventive controls: block actions, built with SCPs and RCPs (for example "disallow deleting the log archive").
- Detective controls: find non-compliant resources after the fact, built with Config rules.
- Proactive controls: check resources before CloudFormation creates them, built with CloudFormation Hooks.

Each control is also labeled mandatory, strongly recommended or elective.

## 179: What OU structure does AWS recommend for a landing zone?

A common layout from the AWS multi-account guidance:

- Security OU: Log Archive and Security Tooling (Audit) accounts
- Infrastructure OU: networking, shared services
- Workloads OU: split into Prod and Non-Prod (or SDLC)
- Sandbox OU: experiments with tight spending limits, no connection to production
- Policy Staging OU: test SCP changes before rolling them out
- Suspended OU: closed or compromised accounts with a deny-all SCP

Apply SCPs per OU, so production gets stricter rules than sandbox.

## 180: What is a delegated administrator and why use one?

Many security services (GuardDuty, Security Hub, Inspector, Macie, Detective, Config, Access Analyzer, IAM Identity Center and others) let you register a member account as the delegated administrator for the organization. Then you manage the service from that account instead of the management account. This keeps day-to-day security work out of the management account, which should have almost no workloads and very few users.

## 181: What is Account Factory for Terraform (AFT)?

AFT is a Control Tower add-on that creates and customizes accounts through a Terraform GitOps pipeline. You add an account request file to a Git repo, and AFT creates the account through Control Tower and applies global and account-specific Terraform customizations, such as baseline roles, VPC setup and security settings. It keeps account creation consistent and reviewed.

## 182: How should a backend validate a Cognito access token?

Check that:

- The signature is valid using the user pool's JWKS (`https://cognito-idp.<region>.amazonaws.com/<poolId>/.well-known/jwks.json`)
- `iss` matches your user pool
- `token_use` is `access` (or `id` if you expect an ID token)
- `client_id` (access token) or `aud` (ID token) matches your app client
- `exp` is in the future
- Scopes or groups match what the endpoint needs

The `aws-jwt-verify` library does this for Node.js:

```ts
import { CognitoJwtVerifier } from "aws-jwt-verify";

const verifier = CognitoJwtVerifier.create({
  userPoolId: "eu-west-1_AbCdEf123",
  tokenUse: "access",
  clientId: "4abc5defgh6ijkl7mnop8qrst",
});

const payload = await verifier.verify(token); // throws if invalid
```

## 183: How do Cognito identity pools choose an IAM role?

An identity pool has an authenticated role and, optionally, an unauthenticated (guest) role. You can also use role-based access control: choose a role from the token's `cognito:preferred_role` claim (from user pool groups) or map claims to roles with rules. The role trust policy should check `cognito-identity.amazonaws.com:aud` (the pool ID) and `amr` (authenticated or unauthenticated). Keep the guest role very small or turn guest access off.

## 184: How can Cognito Lambda triggers improve security?

- Pre sign-up: block disposable email domains or auto-confirm only trusted domains
- Pre authentication: block sign-in for users flagged in your own system
- Pre token generation: add or remove claims and scopes, for example tenant ID
- Define/create/verify auth challenge: build custom flows like extra verification steps
- Custom email and SMS senders: control message content and delivery

Keep triggers fast, because they run on every sign-in.

## 185: Should a browser app use a Cognito app client secret?

No. A client secret in a single-page app or mobile app is visible to anyone, so it is not a secret. Public clients should use the authorization code flow with PKCE and no client secret. Use client secrets only for confidential clients, like a server-side web app or machine-to-machine calls with the client credentials flow.

## 186: Where should a web app store tokens from Cognito?

Avoid `localStorage` for long-lived tokens, because any XSS can read it. Safer options:

- A backend-for-frontend that keeps tokens on the server and gives the browser an `HttpOnly`, `Secure`, `SameSite` session cookie
- Keep access tokens in memory only, with short lifetimes, and refresh through an `HttpOnly` cookie

Also enable refresh token rotation or revocation and keep access token lifetimes short.

## 187: How do you enforce IMDSv2 across your accounts?

- Set the account-level default so new instances use IMDSv2 (`aws ec2 modify-instance-metadata-defaults --http-tokens required`)
- Set `HttpTokens: required` in launch templates and AMIs (AMIs can be flagged with `ImdsSupport: v2.0`)
- Use an SCP that denies `ec2:RunInstances` unless `ec2:MetadataHttpTokens` is `required`
- Use an SCP condition on `ec2:RoleDelivery` (`NumericLessThan 2.0`) to deny API calls made with credentials taken from IMDSv1
- Monitor the `MetadataNoToken` CloudWatch metric to find apps still using IMDSv1

## 188: Why does the IMDS hop limit matter for containers?

The hop limit (`HttpPutResponseHopLimit`) is the IP TTL on IMDSv2 token responses. With a limit of 1, the token response cannot cross the extra network hop into a container on the instance, so containers cannot get the node role's credentials. That is usually what you want, because pods should use their own roles. Set it to 2 only if containers truly need IMDS. Many EKS node AMIs default to 2, so check it.

## 189: How do you set up IRSA for an EKS pod?

1. Create an IAM OIDC provider for the cluster's OIDC issuer URL.
2. Create a role with a trust policy that allows only that service account:

```json
{
  "Effect": "Allow",
  "Principal": {
    "Federated": "arn:aws:iam::111122223333:oidc-provider/oidc.eks.eu-west-1.amazonaws.com/id/EXAMPLED539D4633E53DE1B71EXAMPLE"
  },
  "Action": "sts:AssumeRoleWithWebIdentity",
  "Condition": {
    "StringEquals": {
      "oidc.eks.eu-west-1.amazonaws.com/id/EXAMPLED539D4633E53DE1B71EXAMPLE:sub": "system:serviceaccount:orders:orders-api",
      "oidc.eks.eu-west-1.amazonaws.com/id/EXAMPLED539D4633E53DE1B71EXAMPLE:aud": "sts.amazonaws.com"
    }
  }
}
```

3. Annotate the service account with `eks.amazonaws.com/role-arn`.

The SDK in the pod reads the projected token and calls `AssumeRoleWithWebIdentity`.

## 190: What are the advantages of EKS Pod Identity over IRSA?

- No OIDC provider per cluster and no cluster-specific trust policy. The trust policy just trusts `pods.eks.amazonaws.com`.
- The same role can be reused across clusters without editing the trust policy.
- Associations are managed through the EKS API, not service account annotations.
- Session tags (cluster name, namespace, service account) are added automatically, which helps ABAC.

```bash
aws eks create-pod-identity-association --cluster-name prod \
  --namespace orders --service-account orders-api \
  --role-arn arn:aws:iam::111122223333:role/orders-api
```

IRSA is still needed where Pod Identity is not supported, such as pods running on Fargate and Kubernetes clusters that are not EKS on AWS (for example self-managed clusters).

## 191: How do you stop ECS tasks on EC2 from using the instance role?

With the `awsvpc` network mode, set `ECS_AWSVPC_BLOCK_IMDS=true` in the ECS agent config. With `bridge` mode, add an iptables rule that blocks traffic from the docker bridge to `169.254.169.254`. Set the IMDS hop limit to 1 too. Each task should get its own permissions from its task role, which ECS provides through a separate credentials endpoint.

## 192: When do you choose Secrets Manager versus Parameter Store?

|               | Secrets Manager                     | Parameter Store                                |
| ------------- | ----------------------------------- | ---------------------------------------------- |
| Rotation      | Built in                            | Do it yourself                                 |
| Cost          | Per secret per month plus API calls | Standard parameters are free                   |
| Cross-account | Resource policies                   | Advanced parameters can be shared with AWS RAM |
| Replication   | Cross-region replication            | None                                           |
| Size          | 64 KB                               | 4 KB standard, 8 KB advanced                   |

Use Secrets Manager for credentials that need rotation or cross-account sharing, like database passwords. Use Parameter Store `SecureString` for simple config and low-risk secrets.

## 193: How do you inject secrets into an ECS task?

Reference them in the container definition's `secrets` field. ECS fetches them at task start using the task execution role and sets them as environment variables.

```json
"secrets": [
  {
    "name": "DB_PASSWORD",
    "valueFrom": "arn:aws:secretsmanager:eu-west-1:111122223333:secret:prod/orders/db-AbCdEf:password::"
  },
  {
    "name": "API_KEY",
    "valueFrom": "arn:aws:ssm:eu-west-1:111122223333:parameter/prod/orders/api_key"
  }
]
```

The execution role needs `secretsmanager:GetSecretValue` or `ssm:GetParameters`, plus `kms:Decrypt` if a customer managed key is used. The value does not change until the task restarts, so plan for rotation.

## 194: How should a Lambda function read secrets efficiently?

Fetch the secret outside the handler or cache it with a short TTL, so you do not call Secrets Manager on every invocation. Options:

- The AWS Parameters and Secrets Lambda Extension, which caches values and serves them on a localhost port
- Powertools for AWS Lambda parameters utility with caching
- Your own in-memory cache with expiry

Caching cuts latency and cost, but keep the TTL short enough to pick up rotated secrets.

## 195: How do you share a Secrets Manager secret with another account?

1. Encrypt the secret with a customer managed KMS key (you cannot share the default `aws/secretsmanager` key).
2. Add a resource policy to the secret allowing the other account's role `secretsmanager:GetSecretValue`.
3. Add the role to the KMS key policy for `kms:Decrypt`, ideally with `kms:ViaService` set to Secrets Manager.
4. In the other account, give the role IAM permissions for both the secret ARN and the key.

## 196: What is envelope encryption?

You encrypt data with a data key, and then encrypt the data key with a KMS key. You store the encrypted data and the encrypted data key together. To decrypt, you ask KMS to decrypt the data key, then decrypt the data locally. This is fast, because large data never goes to KMS (which has a 4 KB limit per `Encrypt` call), and safe, because the plaintext data key is only in memory for a short time. S3, EBS and most AWS services use this pattern.

## 197: When do you use GenerateDataKey instead of Encrypt?

`Encrypt` sends up to 4 KB of plaintext to KMS and gets ciphertext back, fine for small secrets. `GenerateDataKey` returns a fresh data key in plaintext and encrypted form, for envelope encryption of larger data. `GenerateDataKeyWithoutPlaintext` returns only the encrypted copy, useful when one component prepares keys and another uses them later. In app code, the AWS Encryption SDK handles all this for you.

## 198: What are KMS grants?

A grant gives a principal permission to use a KMS key for specific operations, without changing the key policy. AWS services use grants a lot. For example, when EBS attaches an encrypted volume, it creates a grant so EC2 can decrypt it. Grants can be limited by encryption context and retired when no longer needed. They take effect quickly and are good for temporary, programmatic access.

```bash
aws kms create-grant --key-id 1234abcd-12ab-34cd-56ef-1234567890ab \
  --grantee-principal arn:aws:iam::111122223333:role/batch-job \
  --operations Decrypt
```

## 199: What is a KMS encryption context?

It is a set of non-secret key-value pairs you pass when encrypting. The same context must be passed to decrypt, or it fails. It is logged in CloudTrail, which makes logs more useful, and you can use it in key policy conditions (`kms:EncryptionContext:tenant`) to make sure one tenant's role can only decrypt that tenant's data.

```bash
aws kms encrypt --key-id alias/app-data \
  --plaintext fileb://note.txt \
  --encryption-context tenant=acme,purpose=notes
```

## 200: What does a well-structured KMS key policy look like?

It separates key administrators from key users and keeps the account root statement so IAM can be used and the key cannot be orphaned.

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "EnableIAMPolicies",
      "Effect": "Allow",
      "Principal": { "AWS": "arn:aws:iam::111122223333:root" },
      "Action": "kms:*",
      "Resource": "*"
    },
    {
      "Sid": "KeyAdmins",
      "Effect": "Allow",
      "Principal": { "AWS": "arn:aws:iam::111122223333:role/KmsAdmin" },
      "Action": [
        "kms:Describe*",
        "kms:Enable*",
        "kms:Disable*",
        "kms:Put*",
        "kms:Update*",
        "kms:TagResource",
        "kms:UntagResource",
        "kms:ScheduleKeyDeletion",
        "kms:CancelKeyDeletion"
      ],
      "Resource": "*"
    },
    {
      "Sid": "KeyUsers",
      "Effect": "Allow",
      "Principal": { "AWS": "arn:aws:iam::111122223333:role/orders-api" },
      "Action": [
        "kms:Encrypt",
        "kms:Decrypt",
        "kms:GenerateDataKey*",
        "kms:DescribeKey"
      ],
      "Resource": "*"
    }
  ]
}
```

`"Resource": "*"` in a key policy means "this key".

## 201: What does the kms:ViaService condition do?

It allows a KMS key to be used only when the request comes through a specific AWS service. For example, a role can decrypt with the key only through S3 in one region, not by calling KMS directly.

```json
{
  "Effect": "Allow",
  "Principal": { "AWS": "arn:aws:iam::111122223333:role/reports-reader" },
  "Action": "kms:Decrypt",
  "Resource": "*",
  "Condition": {
    "StringEquals": { "kms:ViaService": "s3.eu-west-1.amazonaws.com" }
  }
}
```

This means that even if the role's credentials leak, the attacker cannot decrypt arbitrary ciphertext with the key.

## 202: What are KMS multi-Region keys?

They are a set of related keys in different regions with the same key ID and key material. Data encrypted in one region can be decrypted in another without calling the first region. They are useful for disaster recovery, global DynamoDB tables and client-side encryption across regions. Each replica has its own key policy. Do not use them by default: single-region keys keep data from being decrypted in places you did not plan for.

## 203: What happens when you delete a KMS key?

You cannot delete a key immediately. You schedule deletion with a waiting period of 7 to 30 days (30 by default). During that time the key is unusable, and you can cancel. After deletion, all data encrypted with it is lost forever. Before deleting, disable the key and watch CloudTrail and CloudWatch for failed calls, which show what still depends on it. An attacker scheduling deletion of your keys is a ransomware tactic, so alert on `ScheduleKeyDeletion`.

## 204: What key types does KMS support besides symmetric keys?

- Asymmetric RSA keys for encryption or signing
- Asymmetric ECC keys (NIST curves, secp256k1) for signing
- SM2 keys in China regions
- ML-DSA keys for post-quantum signing
- HMAC keys for generating and verifying message authentication codes

Asymmetric keys let you share the public key outside AWS, for example to verify signed JWTs or documents, while the private key never leaves KMS.

## 205: What is an S3 Bucket Key?

With SSE-KMS, every object normally needs a call to KMS, which costs money and can hit KMS request limits. An S3 Bucket Key is a short-lived bucket-level key derived from your KMS key, used to create data keys for objects. It cuts KMS calls by up to 99%. One side effect: CloudTrail KMS events show the bucket ARN instead of the object ARN as encryption context.

## 206: How do KMS, CloudHSM, custom key stores and external key stores compare?

- KMS (standard): multi-tenant HSMs run by AWS. Easy, cheap, integrated with almost every service.
- CloudHSM: single-tenant HSMs you control, with standard APIs like PKCS #11 and JCE. You manage the cluster.
- KMS custom key store (CloudHSM): KMS keys whose material lives in your CloudHSM cluster. You get KMS integration with single-tenant HSMs.
- KMS external key store (XKS): KMS keys backed by an HSM outside AWS, for rules that require keys to stay on premises. Your HSM's availability and latency now affect every encrypt and decrypt.

Pick standard KMS unless a regulation clearly requires something else.

## 207: What should you know about ACM certificates for CloudFront?

The certificate must be in `us-east-1`, no matter where your origin is. Use DNS validation with Route 53 so renewal is fully automatic. Email validation needs someone to click a link each time. ACM certificates attached to CloudFront or a load balancer cannot be exported. Since 2025, ACM can also issue exportable public certificates for a fee, for use on servers outside integrated services.

## 208: Where should TLS be terminated in a typical AWS web app?

Often at the load balancer or CloudFront, with an ACM certificate. For sensitive data or compliance (like PCI), you also encrypt from the load balancer to the targets, using HTTPS target groups with certificates on the instances or containers. Pick a strong ALB security policy (TLS 1.2 or 1.3 only, for example `ELBSecurityPolicy-TLS13-1-2-2021-06`). With a Network Load Balancer you can pass TLS through to targets if they must see the client handshake, such as for mutual TLS.

## 209: How do you make sure all EBS volumes are encrypted?

Turn on "EBS encryption by default" in each region of each account, with your KMS key if needed. Every new volume and snapshot copy is then encrypted, even if the person launching forgets. Back it up with an SCP that denies `ec2:CreateVolume` when `ec2:Encrypted` is false, and the Config rule `encrypted-volumes`.

```bash
aws ec2 enable-ebs-encryption-by-default --region eu-west-1
```

## 210: How do you share an encrypted EBS snapshot or AMI with another account?

You cannot share snapshots encrypted with the AWS managed key `aws/ebs`. Use a customer managed key, add the target account to the key policy (at least `kms:Decrypt`, `kms:DescribeKey`, `kms:CreateGrant`, `kms:ReEncrypt*`), then share the snapshot or AMI. The target account should copy it and re-encrypt with its own key, so it does not keep depending on your key.

## 211: What are S3 Access Points and why do they help security?

An access point is a named network endpoint for a bucket with its own policy. Instead of one huge bucket policy for many teams, each team or app gets its own access point with a focused policy. An access point can be limited to a VPC, so it cannot be reached from the internet at all. The bucket policy can then delegate access control to access points owned by the account.

```bash
aws s3control create-access-point --account-id 111122223333 \
  --name analytics-vpc-only --bucket data-lake \
  --vpc-configuration VpcId=vpc-0abc1234
```

## 212: How do you give another account access to an S3 bucket?

1. Add a bucket policy that allows the other account's role specific actions on specific prefixes.
2. In the other account, give the role an IAM policy with the same actions on the bucket.
3. If objects use SSE-KMS with a customer managed key, add the role to the key policy too.
4. Keep Object Ownership on "Bucket owner enforced" so objects written by the other account belong to you.

For many consumers, use access points or a role in your account they can assume, instead of one large bucket policy.

## 213: What are the security pitfalls of presigned URLs?

- Anyone who has the URL can use it until it expires, so treat it like a password.
- The URL works with the signer's permissions, so sign with a narrowly scoped role.
- If the signing credentials are temporary, the URL stops working when they expire, which can be shorter than you expected.
- For uploads, a presigned PUT does not limit file size. Use a presigned POST with a policy (`content-length-range`, content type) for that.
- URLs end up in logs, browser history and referrer headers, so keep expiry short.

You can also block presigned URL use beyond a certain age with the `s3:signatureAge` condition.

## 214: What is the difference between S3 server access logs and CloudTrail data events?

Server access logs are free (you pay storage), delivered on a best-effort basis, and include details like referrer and object size. CloudTrail data events cost money per event but are delivered reliably within minutes, include full IAM identity details, integrate with CloudTrail Lake, EventBridge and GuardDuty, and can be centralized with organization trails. For security investigations, CloudTrail data events are usually the better choice.

## 215: How can S3 replication protect against data loss or attack?

Replicate important buckets to another account (and often another region) that production admins cannot touch. Turn on "change object ownership to destination bucket owner" so the copies belong to the backup account. Add Object Lock on the destination. Delete markers are not replicated by default, so a mass delete in production does not wipe the copy. Even if production is fully compromised, the copy survives.

## 216: What is MFA Delete in S3 and what are its limits?

MFA Delete requires an MFA code to permanently delete an object version or to change the bucket's versioning state. Only the root user can turn it on, and only through the CLI or API, not the console. It also does not work with lifecycle rules that expire versions. Because of these limits, many teams use Object Lock or replication to a separate account instead.

## 217: How would you design security groups for a three-tier web app?

- ALB security group: inbound 443 from `0.0.0.0/0` (or from the CloudFront managed prefix list).
- App security group: inbound app port only from the ALB security group.
- Database security group: inbound 5432 only from the app security group.
- No SSH or RDP rules anywhere. Use Session Manager.
- Outbound rules narrowed where you can, for example the app can only reach the database and the VPC endpoints.

Referencing groups instead of CIDRs means scaling and redeploys need no rule changes.

## 218: Why do NACLs need ephemeral port rules?

NACLs are stateless, so a response is treated like new traffic. If a web server receives a request on port 443, its reply goes back to the client's random source port (1024-65535). The outbound NACL rules must allow that range, or replies are dropped. In the same way, when an instance in the subnet calls out, inbound rules must allow the reply ports. Forgetting this is a common cause of mysterious timeouts.

## 219: What is a VPC endpoint policy and how do you use it for S3?

An endpoint policy limits what can be done through that endpoint. For an S3 gateway endpoint, you can allow access only to your organization's buckets, so a compromised instance cannot upload data to an attacker's bucket.

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Principal": "*",
      "Action": "s3:*",
      "Resource": "*",
      "Condition": { "StringEquals": { "aws:ResourceOrgID": "o-a1b2c3d4e5" } }
    }
  ]
}
```

Remember that some AWS-owned buckets (like those for Amazon Linux repos or ECR image layers) may need an extra exception.

## 220: What does private DNS on an interface endpoint do?

With private DNS on, the normal public service name (for example `secretsmanager.eu-west-1.amazonaws.com`) resolves to the endpoint's private IPs inside the VPC. Apps and SDKs use the endpoint without any code changes. Without it, you must call the endpoint-specific DNS name. In multi-VPC setups, teams often centralize endpoints in a shared VPC and share private hosted zones with other VPCs.

## 221: What is the difference between aws:SourceVpce, aws:SourceVpc and aws:SourceIp?

- `aws:SourceVpce`: the request came through a specific VPC endpoint
- `aws:SourceVpc`: the request came through any endpoint in a specific VPC
- `aws:SourceIp`: the public IP of the caller. It is not present for requests through a VPC endpoint (those have `aws:VpcSourceIp` instead)

A common mistake is restricting a bucket by `aws:SourceIp` with private IP ranges. That never matches, because requests through a VPC endpoint do not carry the public `aws:SourceIp` value.

## 222: How can you control outbound internet traffic from a VPC?

- No route to the internet at all, with VPC endpoints for AWS services
- NAT gateway plus Network Firewall with a domain allow list
- An explicit forward proxy (like Squid) on EC2
- Route 53 Resolver DNS Firewall to block lookups of bad or unapproved domains
- Tight outbound security group rules

Egress control matters because attackers need to send data out and talk to command-and-control servers.

## 223: How do you analyze VPC Flow Logs?

Send them to S3 in Parquet format, with a custom format that includes useful fields like `vpc-id`, `subnet-id`, `instance-id`, `pkt-srcaddr`, `flow-direction` and `tcp-flags`. Query them with Athena:

```sql
SELECT srcaddr, dstaddr, dstport, SUM(bytes) AS total_bytes
FROM vpc_flow_logs
WHERE action = 'ACCEPT' AND flow_direction = 'egress'
  AND day = '2026/11/12'
GROUP BY srcaddr, dstaddr, dstport
ORDER BY total_bytes DESC
LIMIT 20;
```

This finds large outbound transfers, which may be data exfiltration. CloudWatch Logs Insights works for smaller volumes.

## 224: What is VPC Traffic Mirroring?

Traffic Mirroring copies the actual packets from an ENI to a target, like an intrusion detection appliance or a Network Load Balancer in front of one. Flow Logs only give metadata. Mirroring gives full packet contents for deep inspection or forensics. It is not supported on all instance types, and mirroring a lot of traffic can be expensive.

## 225: How do VPC peering and Transit Gateway differ from a security point of view?

Peering is a direct link between two VPCs and is not transitive, so each pair needs its own peering. It is simple, but routing and security groups have to be managed per pair. Transit Gateway is a hub with route tables, so you can segment networks (prod cannot reach dev) and send traffic through a central inspection VPC with Network Firewall. For more than a few VPCs, Transit Gateway or Cloud WAN make segmentation easier to manage.

## 226: How are rules evaluated in an AWS WAF web ACL?

Rules and rule groups run in priority order, lowest number first. A terminating action (Allow, Block, or CAPTCHA/Challenge when the token is missing) stops evaluation. Count is non-terminating and just adds labels and metrics. If nothing terminates, the web ACL's default action applies. Scope-down statements limit a rule to certain requests, for example only applying Bot Control to `/login` paths to save cost.

## 227: What does AWS WAF Bot Control do?

Bot Control is a managed rule group with two levels:

- Common: detects self-identifying bots (search engines, scrapers, monitoring tools) and labels them by category so you can allow good bots and block others.
- Targeted: adds browser fingerprinting, behavior analysis and machine learning to catch bots that pretend to be real browsers. It can use challenges and the WAF client SDK tokens.

Targeted costs more, so use scope-down statements to apply it only where bots hurt you, like checkout or login.

## 228: How do WAF labels and logging help?

Rules add labels to requests they match, like `awswaf:managed:aws:bot-control:bot:category:search_engine`. Later rules can match on these labels, which lets you build logic like "block bots unless they are verified search engines". WAF logs (to CloudWatch Logs, S3 or Data Firehose) show each request, which rules matched and the action taken. Redact sensitive fields like `Authorization` headers in the logging config.

## 229: What is the difference between the CAPTCHA and Challenge actions in WAF?

CAPTCHA shows a puzzle the user must solve. Challenge runs a silent JavaScript check in the browser to prove it is a real browser, with no user interaction. Both set a token cookie that is valid for a set immunity time. Use Challenge for most cases to block simple scripts without bothering users. Use CAPTCHA for higher-risk actions. Neither works well on API calls from non-browser clients, so use them on web pages and use the WAF mobile SDK for apps.

## 230: What are WAF Account Takeover Prevention and Account Creation Fraud Prevention?

ATP watches login requests. It checks credentials against a database of stolen credentials and looks for patterns of credential stuffing, then blocks or challenges suspicious attempts. ACFP does the same for sign-up pages, catching fake account creation using known fraud signals. Both are paid managed rule groups configured with your login or registration paths and field names.

## 231: What does the Shield Response Team do?

With Shield Advanced and Business or Enterprise support, you can contact the SRT during a DDoS attack. They help analyze the attack and write WAF rules to mitigate it. With proactive engagement, the SRT contacts you when health checks for a protected resource fail during a detected event. You grant them a role (`AWSSRTSupportAccess`) so they can view and update your WAF and Shield config.

## 232: How do you stop people from bypassing CloudFront and hitting your ALB directly?

Options:

- Use CloudFront VPC origins, which let you keep the ALB in a private subnet so it is not reachable from the internet at all.
- Allow inbound to the ALB security group only from the AWS managed prefix list `com.amazonaws.global.cloudfront.origin-facing`.
- Add a secret custom header in CloudFront and have the ALB listener rule (or WAF on the ALB) reject requests without it. Rotate the value.

The prefix list alone is not enough, because another customer's CloudFront distribution also comes from those IPs.

## 233: What is CloudFront field-level encryption?

It encrypts specific form fields (like a credit card number) at the edge with a public key you provide. The value stays encrypted through your whole stack, and only the service holding the private key, for example the payment service, can decrypt it. It works for POST requests with form data. It reduces how many systems can see sensitive data, which can shrink PCI scope.

## 234: How do you restrict content by country in CloudFront?

Use geographic restrictions on the distribution with an allow list or block list of countries. For finer control, like different rules per path or combining with IP reputation, use a WAF geo match rule instead. Both rely on IP geolocation, which VPNs and proxies can get around, so do not treat it as strong security.

## 235: Which security headers should you add with a CloudFront response headers policy?

- `Strict-Transport-Security` (HSTS) with a long max-age and `includeSubDomains`
- `Content-Security-Policy` suited to your site
- `X-Content-Type-Options: nosniff`
- `X-Frame-Options: DENY` or a CSP `frame-ancestors` rule
- `Referrer-Policy: strict-origin-when-cross-origin`

AWS provides a managed `SecurityHeadersPolicy` as a starting point, and you can create a custom policy with your own CSP.

## 236: What is the difference between TOKEN and REQUEST Lambda authorizers?

- TOKEN authorizers (REST APIs only) receive a single header value, such as a bearer token.
- REQUEST authorizers receive headers, query strings, path, stage variables and context, so they can make decisions on several inputs.

Both return an IAM policy (or a simple true/false response for HTTP APIs) and can be cached by an identity source for up to an hour. Be careful with caching: a cached policy must cover all resources the token might call, or later calls to other routes will be wrongly denied or allowed.

## 237: How do you make an API Gateway REST API private?

Choose the private endpoint type, create an `execute-api` interface endpoint in your VPC, and add a resource policy that only allows that endpoint.

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Principal": "*",
      "Action": "execute-api:Invoke",
      "Resource": "execute-api:/*"
    },
    {
      "Effect": "Deny",
      "Principal": "*",
      "Action": "execute-api:Invoke",
      "Resource": "execute-api:/*",
      "Condition": {
        "StringNotEquals": { "aws:SourceVpce": "vpce-0a1b2c3d4e5f67890" }
      }
    }
  ]
}
```

Private APIs can't be reached from the internet at all.

## 238: How does API Gateway throttling protect your backend?

There is an account-level limit per region (10,000 requests per second steady state with bursts, by default) and you can set lower limits per stage and per method. With usage plans and API keys, you can set per-client rate limits and quotas. Throttled requests get HTTP 429. This prevents one noisy client or a simple flood from overloading your Lambda functions or database. Use WAF rate-based rules for per-IP limits.

## 239: How does mutual TLS work in API Gateway?

You turn on mTLS for a custom domain and upload a truststore (a PEM bundle of CA certificates) to S3. Clients must present a certificate signed by one of those CAs during the TLS handshake. API Gateway rejects connections with no valid certificate before your code runs. Disable the default `execute-api` endpoint so clients cannot skip the custom domain. You can pass the client certificate details to a Lambda authorizer for extra checks, like revocation.

## 240: How does a client call an API Gateway API protected with IAM auth?

The client signs each request with SigV4 using AWS credentials, for example from a Cognito identity pool, an IAM role or a federated session. API Gateway checks the signature and that the caller has `execute-api:Invoke` on the method ARN.

```ts
import { SignatureV4 } from "@smithy/signature-v4";
import { Sha256 } from "@aws-crypto/sha256-js";
import { fromNodeProviderChain } from "@aws-sdk/credential-providers";

const signer = new SignatureV4({
  credentials: fromNodeProviderChain(),
  region: "eu-west-1",
  service: "execute-api",
  sha256: Sha256,
});

const signed = await signer.sign({
  method: "GET",
  protocol: "https:",
  hostname: "abc123.execute-api.eu-west-1.amazonaws.com",
  path: "/prod/orders",
  headers: { host: "abc123.execute-api.eu-west-1.amazonaws.com" },
});

const res = await fetch(`https://${signed.hostname}${signed.path}`, {
  method: signed.method,
  headers: signed.headers,
});
```

It is a good fit for service-to-service calls inside AWS.

## 241: When should a Lambda function run inside a VPC?

When it needs to reach private resources like RDS, ElastiCache or internal services. A VPC function gets ENIs in your subnets and is controlled by security groups. It has no internet access unless the subnets route through a NAT gateway, and it reaches AWS services through VPC endpoints. Do not put functions in a VPC just because "it feels safer" if they only call public AWS APIs. It adds complexity without much benefit, though it does let you apply egress controls.

## 242: What is Lambda code signing?

Code signing makes sure only trusted, unmodified code is deployed to a function. You create a signing profile in AWS Signer, sign your deployment packages in CI, and attach a code signing configuration to the function with the allowed signing profiles. With the policy set to `Enforce`, Lambda rejects deployments that are unsigned, signed by an unknown profile, changed after signing or expired. It applies to zip packages, not container images.

## 243: What are the security risks of Lambda layers?

A layer adds code to your function, often shared libraries. If you use a public layer from someone else's account, you run their code with your function's permissions. They could also delete it, breaking new deployments. Prefer building layers yourself, pin layer versions, scan them like any dependency, and limit `lambda:GetLayerVersion` access to layers you share.

## 244: How do you put CloudFront in front of a Lambda function URL securely?

Set the function URL auth type to `AWS_IAM`, create an Origin Access Control for Lambda in CloudFront, and add a resource policy that lets CloudFront invoke the URL.

```bash
aws lambda add-permission --function-name web-api \
  --statement-id cloudfront-oac \
  --action lambda:InvokeFunctionUrl \
  --principal cloudfront.amazonaws.com \
  --source-arn arn:aws:cloudfront::111122223333:distribution/E1ABCDEF2GHIJ
```

Now the URL cannot be called directly, and you can add WAF, caching and a custom domain on CloudFront. For POST and PUT, the client must send an `x-amz-content-sha256` header with the body hash.

## 245: What container settings make ECS tasks more secure?

- `readonlyRootFilesystem: true`
- Run as a non-root `user`
- No `privileged: true`, and drop Linux capabilities you do not need
- Secrets through the `secrets` field, not plain `environment`
- One task role per service with least privilege
- `awsvpc` network mode so each task gets its own security group
- Image scanning and pinned image digests instead of `latest`
- Enable GuardDuty Runtime Monitoring

## 246: How does access control work in EKS?

Two layers:

- AWS IAM authenticates the user or role to the cluster. Access entries (the newer, recommended way) map IAM principals to Kubernetes permissions through the EKS API. The old `aws-auth` ConfigMap is legacy.
- Kubernetes RBAC decides what they can do inside the cluster with Roles, ClusterRoles and bindings. Access entries can also attach EKS access policies like `AmazonEKSClusterAdminPolicy` or `AmazonEKSViewPolicy`.

```bash
aws eks create-access-entry --cluster-name prod \
  --principal-arn arn:aws:iam::111122223333:role/dev-team
aws eks associate-access-policy --cluster-name prod \
  --principal-arn arn:aws:iam::111122223333:role/dev-team \
  --policy-arn arn:aws:eks::aws:cluster-access-policy/AmazonEKSViewPolicy \
  --access-scope type=namespace,namespaces=orders
```

## 247: How should the EKS API server endpoint be exposed?

By default it is public, protected only by IAM authentication. Better options:

- Private endpoint only, reachable from your VPC or through VPN or Direct Connect
- Public and private, with the public endpoint limited to specific CIDR ranges

Nodes always use the private endpoint when it is turned on. A private-only endpoint means CI runners and admins need network access to the VPC.

## 248: How do you secure Amazon ECR repositories?

- Repository policies that allow pulls only from your accounts or organization
- Tag immutability so a tag like `v1.4.2` cannot be overwritten with another image
- Enhanced scanning with Inspector
- KMS encryption with a customer managed key if needed
- Lifecycle policies to delete old, unpatched images
- Pull-through cache rules for public images, so you control and scan what comes in from Docker Hub or other registries

## 249: How can you sign and verify container images on AWS?

AWS Signer supports container image signing with the Notation CLI. You create a signing profile, sign images in CI after pushing to ECR, and the signatures are stored in ECR next to the image. At deploy time you verify them, for example with Kyverno or Ratify admission controllers in EKS. This makes sure only images built by your pipeline can run.

```bash
notation sign 111122223333.dkr.ecr.eu-west-1.amazonaws.com/orders@sha256:4f1c... \
  --plugin com.amazonaws.signer.notation.plugin \
  --id arn:aws:signer:eu-west-1:111122223333:/signing-profiles/prod_images
```

## 250: What does GuardDuty Runtime Monitoring add?

It uses a lightweight security agent on EKS nodes, ECS (including Fargate) and EC2 to watch OS-level events: process starts, file access, network connections and privilege changes. It finds things the log-based detections cannot, like a reverse shell inside a container, crypto mining processes or a container escape attempt. GuardDuty can manage the agent for you as an EKS add-on or through SSM.

## 251: How do you force TLS connections to RDS?

Set it in the DB parameter group:

- PostgreSQL: `rds.force_ssl = 1` (the default is already 1 from PostgreSQL 15 on RDS)
- MySQL and MariaDB: `require_secure_transport = ON`
- SQL Server: `rds.force_ssl = 1`

Clients should also verify the server certificate using the RDS CA bundle (`sslmode=verify-full` for PostgreSQL). Without verification, encryption alone does not stop a man-in-the-middle.

## 252: How can RDS manage the master password for you?

Set `ManageMasterUserPassword` when creating or modifying the instance or cluster. RDS creates a secret in Secrets Manager, stores the master password there and rotates it (every 7 days by default). Nobody has to see or type the password, and apps read it from Secrets Manager. You can choose a customer managed KMS key for the secret.

```bash
aws rds modify-db-instance --db-instance-identifier orders-db \
  --manage-master-user-password --apply-immediately
```

## 253: How do you limit users to their own items in DynamoDB?

Use the `dynamodb:LeadingKeys` condition so a user can only touch items whose partition key equals their identity, for example the Cognito identity ID.

```json
{
  "Effect": "Allow",
  "Action": [
    "dynamodb:GetItem",
    "dynamodb:Query",
    "dynamodb:PutItem",
    "dynamodb:UpdateItem"
  ],
  "Resource": "arn:aws:dynamodb:eu-west-1:111122223333:table/UserNotes",
  "Condition": {
    "ForAllValues:StringEquals": {
      "dynamodb:LeadingKeys": ["${cognito-identity.amazonaws.com:sub}"]
    }
  }
}
```

You can also limit which attributes can be read or written with `dynamodb:Attributes`.

## 254: Does DynamoDB support resource-based policies?

Yes, since 2024. You can attach resource-based policies to tables, indexes and streams. This allows cross-account access without role assumption, and lets you add guardrails directly on the table, such as denying deletes or limiting access to a VPC endpoint. Access Analyzer also checks these policies for external access.

## 255: What are Aurora Database Activity Streams?

They push a near real-time stream of database activity (logins, queries, schema changes) from Aurora PostgreSQL, Aurora MySQL and some RDS engines to Kinesis Data Streams, encrypted with your KMS key. The database admins cannot turn it off or change it from inside the database, which separates duties between DBAs and the security team. Partner tools or your own consumers analyze the stream for suspicious queries.

## 256: How do you set up a central CloudTrail organization trail properly?

- Create a multi-region organization trail from the management account or delegated admin
- Deliver to an S3 bucket in the Log Archive account with a bucket policy that only allows CloudTrail writes for your trail ARN
- Encrypt with a customer managed KMS key whose policy lets CloudTrail encrypt and only the security team decrypt
- Turn on log file validation
- Send a copy to CloudWatch Logs for alerts
- Use Object Lock or a deny-delete bucket policy on the log bucket
- Add an SCP denying `cloudtrail:StopLogging`, `DeleteTrail` and `UpdateTrail` for everyone except an admin role

## 257: What is CloudTrail Lake?

CloudTrail Lake is a managed store for events where you can run SQL queries directly, without setting up Athena or a SIEM. It can collect CloudTrail events, Config items, Audit Manager evidence and events from outside AWS. You choose retention per event data store (up to 10 years). It is useful for investigations, like "show everything this access key did in the last 30 days".

```sql
SELECT eventTime, eventName, sourceIPAddress, awsRegion
FROM <event-data-store-id>
WHERE userIdentity.accessKeyId = 'AKIAEXAMPLE123'
ORDER BY eventTime DESC
```

## 258: What are CloudTrail Insights?

Insights learns the normal rate of write management API calls (and error rates) in your account and logs an Insights event when activity is unusual, for example a sudden burst of `RunInstances` or `DeleteBucket` calls, or a spike in `AccessDenied` errors. This can catch crypto mining, scripts gone wrong, or an attacker trying permissions. It costs extra per event analyzed.

## 259: How do you investigate a suspicious role with CloudTrail and Athena?

Create an Athena table over the CloudTrail bucket (CloudTrail can create it for you from the console), then query by the role or session:

```sql
SELECT eventtime, eventsource, eventname, sourceipaddress, useragent, errorcode
FROM cloudtrail_logs
WHERE useridentity.arn LIKE 'arn:aws:sts::111122223333:assumed-role/orders-api/%'
  AND eventtime > '2026-11-10T00:00:00Z'
ORDER BY eventtime;
```

Look for unexpected regions, IPs that are not AWS or your office, user agents that do not match your SDK, and recon calls like `ListBuckets`, `GetCallerIdentity` or `ListAttachedRolePolicies`.

## 260: What is CloudWatch Logs data protection?

You attach a data protection policy to a log group that detects sensitive data like emails, credit card numbers, AWS secret keys or custom patterns. Matching values are masked when anyone views the logs, unless they have the `logs:Unmask` permission. It also reports how often sensitive data appeared, which tells developers which code is logging things it should not.

## 261: How do you alarm on many failed API calls?

Create a metric filter on the CloudTrail log group in CloudWatch Logs, then an alarm on it.

```bash
aws logs put-metric-filter --log-group-name org-trail \
  --filter-name UnauthorizedAPICalls \
  --filter-pattern '{ ($.errorCode = "*UnauthorizedOperation") || ($.errorCode = "AccessDenied*") }' \
  --metric-transformations metricName=UnauthorizedAPICalls,metricNamespace=CISBenchmark,metricValue=1

aws cloudwatch put-metric-alarm --alarm-name UnauthorizedAPICalls \
  --namespace CISBenchmark --metric-name UnauthorizedAPICalls \
  --statistic Sum --period 300 --evaluation-periods 1 --threshold 20 \
  --comparison-operator GreaterThanOrEqualToThreshold \
  --alarm-actions arn:aws:sns:eu-west-1:111122223333:security-alerts
```

Set the threshold to fit your normal noise, or you will ignore it after a week.

## 262: What is an AWS Config conformance pack?

A conformance pack is a collection of Config rules and remediation actions deployed together as one unit, written in YAML. AWS provides sample packs for frameworks like CIS, NIST 800-53, PCI DSS, HIPAA and operational best practices for many services. You can deploy them to a whole organization and see a compliance score per pack.

```bash
aws configservice put-organization-conformance-pack \
  --organization-conformance-pack-name s3-best-practices \
  --template-s3-uri s3://my-config-packs/Operational-Best-Practices-for-Amazon-S3.yaml
```

## 263: What is a Config aggregator?

An aggregator collects Config data and compliance results from many accounts and regions into one view, usually in the security tooling account. It lets you ask "which EBS volumes in the whole organization are unencrypted" with advanced queries in SQL-like syntax.

```sql
SELECT accountId, awsRegion, resourceId
WHERE resourceType = 'AWS::EC2::Volume'
  AND configuration.encrypted = false
```

## 264: How do you automatically fix non-compliant resources with Config?

Attach a remediation action to a Config rule. Remediation runs a Systems Manager Automation runbook, either manually or automatically with retries. For example, the rule `s3-bucket-public-read-prohibited` can trigger `AWS-DisableS3BucketPublicReadWrite`. The runbook needs an IAM role with only the permissions to make that fix. Test automatic remediation carefully, because a wrong rule can break production at scale.

## 265: What are some common GuardDuty finding types?

- `UnauthorizedAccess:IAMUser/InstanceCredentialExfiltration.OutsideAWS`: instance role credentials used from outside AWS
- `CryptoCurrency:EC2/BitcoinTool.B!DNS`: instance querying mining pool domains
- `Recon:IAMUser/MaliciousIPCaller`: API calls from known bad IPs
- `Policy:IAMUser/RootCredentialUsage`: root user activity
- `Backdoor:EC2/C&CActivity.B`: instance talking to a command-and-control server
- `Exfiltration:S3/AnomalousBehavior`: unusual S3 data access
- `PrivilegeEscalation:Kubernetes/PrivilegedContainer`

Severity is low, medium, high or critical. Treat high and critical as incidents.

## 266: How do you reduce GuardDuty noise?

- Suppression rules: auto-archive findings that match filters you know are expected, like a vulnerability scanner's IP.
- Trusted IP lists: IPs that should not generate findings (like your office).
- Threat lists: your own lists of known bad IPs and domains to add detections.
- Tune by fixing root causes, not just suppressing. If an instance keeps triggering a port scan finding, maybe it should not be public.

Keep suppression narrow, because attackers may use the same patterns.

## 267: What does GuardDuty Malware Protection cover?

- Malware Protection for EC2: when a finding suggests malware, GuardDuty scans the EBS volumes of the instance (or container workloads) by taking snapshots, without an agent. You can also run on-demand scans.
- Malware Protection for S3: scans new objects uploaded to chosen buckets and can tag them with the result, so downstream code only processes clean files. This works even without the rest of GuardDuty turned on.

The second one is useful for any app that accepts file uploads from users.

## 268: What is GuardDuty Extended Threat Detection?

It correlates many signals over time (API calls, runtime events, findings) into attack sequence findings that describe a whole multi-step attack, like credential theft followed by privilege escalation and data exfiltration, mapped to MITRE ATT&CK tactics. These come with critical severity and a summary of the affected resources. It is on by default for accounts with GuardDuty and expands with protection plans like EKS and S3.

## 269: What standards does Security Hub CSPM check against?

- AWS Foundational Security Best Practices (FSBP)
- CIS AWS Foundations Benchmark (several versions)
- PCI DSS
- NIST SP 800-53 Rev. 5
- NIST SP 800-171
- AWS Resource Tagging Standard

Use central configuration from the delegated admin account to choose which standards and controls are on for which OUs and accounts, instead of configuring each account.

## 270: What are Security Hub automation rules?

Automation rules update findings automatically as they arrive, based on criteria you define. For example: raise severity for anything in production accounts, suppress a control in sandbox accounts, add a note, or set the workflow status. They run before findings go to EventBridge, so downstream alerts see the updated values. This keeps the console useful as findings grow.

## 271: How can Inspector be used in a CI/CD pipeline?

Inspector has a CI/CD integration that scans container images and other artifacts before they are pushed. The `inspector-sbomgen` tool creates a software bill of materials, and the `inspector-scan` API (`ScanSbom`) returns vulnerabilities. Plugins exist for Jenkins and TeamCity, and you can call it from GitHub Actions or CodeBuild. The build fails if critical vulnerabilities are found, so vulnerable images never reach ECR.

## 272: How do you make Macie more useful?

- Turn on automated sensitive data discovery for an organization-wide view at low cost
- Add custom data identifiers (regex plus keywords) for your own data, like internal customer IDs
- Use allow lists to ignore known test data or public values
- Run targeted discovery jobs on high-risk buckets
- Send findings to Security Hub and EventBridge so they create tickets

Macie only covers S3, so other data stores need other tools.

## 273: How do you use Detective during an investigation?

Start from a GuardDuty finding or an entity like a role, IP or EC2 instance. Detective shows its activity timeline, baseline behavior, API call volume, new geolocations, related findings and resources it touched. Finding groups bundle related findings into one story. It answers scoping questions quickly: when did this start, which other resources are involved, and is this activity new for this entity.

## 274: How do other tools consume data from Security Lake?

Through subscribers. A data access subscriber reads the Parquet files directly from S3 (for example a SIEM or Athena in another account). A query access subscriber uses Lake Formation to query the tables with Athena without copying data. Subscribers get only the sources and regions you allow. Because data is in OCSF, the same queries work for AWS and third-party sources.

## 275: How would you automatically close SSH open to the internet?

1. EventBridge rule on CloudTrail `AuthorizeSecurityGroupIngress` events (or the Config rule `restricted-ssh`).
2. Target a Lambda function or SSM Automation runbook.
3. The function checks whether the rule opens port 22 to `0.0.0.0/0` or `::/0`, and if so revokes it and notifies the team.

```python
import boto3

ec2 = boto3.client("ec2")

def handler(event, context):
    detail = event["detail"]
    group_id = detail["requestParameters"]["groupId"]
    for perm in detail["requestParameters"]["ipPermissions"]["items"]:
        if perm.get("fromPort") == 22:
            for ip_range in perm.get("ipRanges", {}).get("items", []):
                if ip_range.get("cidrIp") == "0.0.0.0/0":
                    ec2.revoke_security_group_ingress(
                        GroupId=group_id,
                        IpPermissions=[{
                            "IpProtocol": perm["ipProtocol"],
                            "FromPort": 22,
                            "ToPort": perm["toPort"],
                            "IpRanges": [{"CidrIp": "0.0.0.0/0"}],
                        }],
                    )
```

Better still, prevent it in the first place with Firewall Manager or IaC checks.

## 276: What do you do when an access key is leaked?

1. Deactivate the key right away (do not delete it yet, you may need it for tracing).
2. If it belonged to a user, also revoke their active sessions, reset the password and check MFA.
3. Search CloudTrail for everything that key did since it was created: new users, keys, roles, instances, Lambda functions, changes in other regions.
4. Remove anything the attacker created, especially new IAM users, access keys and roles with trust to outside accounts.
5. Check billing for unexpected resources, like GPU instances in other regions.
6. Replace the key with a role-based method and find out how it leaked.

## 277: How do you isolate a compromised EC2 instance?

1. Do not terminate it. You will lose memory and disk evidence.
2. Change its security group to an "isolation" group with no inbound or outbound rules. Note that existing tracked connections may continue, so also use a NACL deny if needed.
3. Detach it from Auto Scaling groups and load balancers.
4. Turn on termination protection and tag it as under investigation.
5. Take EBS snapshots and capture memory if you can.
6. Revoke the instance role's active sessions by adding a deny policy with an `aws:TokenIssueTime` condition.

Do the analysis in a separate forensics account, using copies of the snapshots.

## 278: How do you secure and audit Session Manager?

- Encrypt session data with a KMS key in the Session Manager preferences
- Log session output to S3 and CloudWatch Logs
- Turn on `idleSessionTimeout` and `maxSessionDuration`
- Run sessions as a specific OS user instead of the default `ssm-user`
- Limit `ssm:StartSession` to tagged instances and specific documents

```json
{
  "Effect": "Allow",
  "Action": "ssm:StartSession",
  "Resource": "arn:aws:ec2:*:111122223333:instance/*",
  "Condition": {
    "StringEquals": { "ssm:resourceTag/team": "${aws:PrincipalTag/team}" }
  }
}
```

## 279: Why is Run Command safer than SSH for fleet changes?

Run Command needs no open ports or SSH keys, is authorized per document and per instance through IAM, logs who ran what in CloudTrail, and can save output to S3. You can limit which documents people may run, so someone can restart a service without getting a full shell. With SSH, you only know someone connected, not what they typed, unless you add extra tooling.

## 280: How would you allow only certain outbound domains with Network Firewall?

Create a stateful domain list rule group with an allow list and set the stateful default action to drop everything else.

```bash
aws network-firewall create-rule-group --rule-group-name egress-allow \
  --type STATEFUL --capacity 100 \
  --rule-group '{
    "RulesSource": {
      "RulesSourceList": {
        "Targets": [".github.com", "api.stripe.com", ".amazonaws.com"],
        "TargetTypes": ["TLS_SNI", "HTTP_HOST"],
        "GeneratedRulesType": "ALLOWLIST"
      }
    }
  }'
```

Route traffic from private subnets through the firewall endpoint before the NAT gateway. Domain filtering relies on SNI, so it can be fooled by clients that fake SNI. For stronger control, Network Firewall can also do TLS inspection.

## 281: What are some important DNS Firewall settings?

- AWS managed domain lists (malware, botnet command and control, aggregate threat list, and Amazon GuardDuty threat list) that update on their own
- Your own allow and block lists
- Actions: ALLOW, BLOCK (with NODATA, NXDOMAIN or a custom response) and ALERT
- Fail-open vs fail-closed for when DNS Firewall cannot evaluate a query: fail-closed favors security, fail-open favors availability
- Rule groups can be shared with Firewall Manager or AWS RAM across accounts

Start with ALERT, check logs, then switch to BLOCK.

## 282: How do you use aws:PrincipalOrgID in a resource policy?

It lets you allow every principal in your organization without listing account IDs, and new accounts are included automatically.

```json
{
  "Sid": "AllowOrgRead",
  "Effect": "Allow",
  "Principal": "*",
  "Action": "s3:GetObject",
  "Resource": "arn:aws:s3:::shared-artifacts/*",
  "Condition": { "StringEquals": { "aws:PrincipalOrgID": "o-a1b2c3d4e5" } }
}
```

You can use `aws:PrincipalOrgPaths` to narrow it down to one OU.

## 283: What is aws:ResourceOrgID used for?

It is the organization ID of the account that owns the resource being accessed. In an SCP or VPC endpoint policy, you can deny access to resources that are not in your organization. This stops a compromised identity from copying data to an attacker-owned S3 bucket or queue. Some AWS-owned resources, like public buckets that AWS services use, need exceptions.

## 284: Show an example of an ABAC policy.

This lets engineers start and stop only EC2 instances whose `project` tag matches their own `project` principal tag:

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "ec2:StartInstances",
        "ec2:StopInstances",
        "ec2:RebootInstances"
      ],
      "Resource": "arn:aws:ec2:*:111122223333:instance/*",
      "Condition": {
        "StringEquals": {
          "aws:ResourceTag/project": "${aws:PrincipalTag/project}"
        }
      }
    },
    {
      "Effect": "Allow",
      "Action": "ec2:DescribeInstances",
      "Resource": "*"
    }
  ]
}
```

For this to be safe, people must not be able to change the `project` tag on resources or on their own identity.

## 285: How do you enforce tags on new resources?

- In IAM policies or SCPs, deny create actions when required tags are missing, using `aws:RequestTag/<key>` with a `Null` condition
- Deny tag changes on protected keys with `aws:TagKeys`
- Use tag policies in Organizations to standardize keys and values (and enforce values for some resource types)
- Use the Config rule `required-tags` to find untagged resources

```json
{
  "Sid": "RequireProjectTag",
  "Effect": "Deny",
  "Action": "ec2:RunInstances",
  "Resource": "arn:aws:ec2:*:*:instance/*",
  "Condition": { "Null": { "aws:RequestTag/project": "true" } }
}
```

## 286: How does a central security account access all member accounts?

Deploy the same role (for example `SecurityAudit-ReadOnly`) into every account using CloudFormation StackSets with service-managed permissions, so new accounts get it automatically. The role trusts only a role in the security tooling account. Security tools assume it to scan or investigate. Use SCPs to stop member account admins from changing or deleting this role.

## 287: What should you watch for when sharing resources with AWS RAM?

AWS Resource Access Manager shares resources like subnets, Transit Gateways, Route 53 Resolver rules and License Manager configurations with other accounts. Turn on sharing with AWS Organizations and disallow sharing with external accounts unless needed. Shared subnets let other accounts put resources in your VPC, but they cannot change your route tables or NACLs. Review shares regularly, since a wrong share can expose network paths.

## 288: How do you protect backups from an attacker with admin access to production?

- Copy backups to a separate backup account in a different OU with its own strict SCPs
- Use a logically air-gapped vault, which is locked in compliance mode, encrypted with an AWS owned key by default, and can be shared to a recovery account through RAM
- Use Backup Vault Lock in compliance mode
- Use different KMS keys per account, so a compromised production key policy does not affect backups
- Test restores regularly, because backups you cannot restore do not count

## 289: What are backup policies in AWS Organizations?

Backup policies let you define AWS Backup plans at the organization, OU or account level. They are merged down the tree, and member accounts cannot weaken them. A policy can say "every resource tagged `backup=daily` gets a daily backup kept for 35 days, copied to the backup account". This makes sure new accounts follow the same backup rules without anyone setting them up by hand.

## 290: How can you reduce PCI DSS scope on AWS?

Keep cardholder data in as few places as possible. Use a payment provider's hosted fields or tokens so your servers never see card numbers. If you must handle them, put the cardholder data environment in dedicated accounts, separate it with network controls, use field-level encryption at the edge and tokenize early. Everything that can reach the CDE is in scope, so fewer connections mean a smaller and cheaper audit.

## 291: How would you collect evidence for a SOC 2 audit on AWS?

Use Audit Manager with the SOC 2 framework to gather evidence automatically from Config, Security Hub CSPM, CloudTrail and API calls. Download AWS's SOC 2 report from Artifact for the AWS side. Show access reviews from IAM Identity Center, change management from Git and CI logs, and incident response runbooks. Auditors want proof that controls run continuously, not screenshots from the day before the audit.

## 292: How do CloudFormation StackSets help with security guardrails?

StackSets deploy the same template to many accounts and regions at once. With service-managed permissions and auto-deployment, every new account in an OU gets the stack automatically. Teams use them to roll out baseline IAM roles, Config rules, EventBridge forwarding rules, GuardDuty settings and log subscriptions. Pair them with SCPs that stop member accounts from deleting those stacks or their resources.

## 293: What are CloudFormation Hooks?

Hooks run checks before CloudFormation (and Cloud Control API) creates, updates or deletes resources, stacks or change sets. A hook can fail the operation or only warn. You can write them with Guard rules or Lambda functions, or turn on managed proactive controls from Control Tower. For example, a hook can block any S3 bucket without encryption or any security group with SSH open to the world before it exists.

## 294: How do you secure Terraform state on AWS?

State files can contain secrets and full resource details, so:

- Use the S3 backend with encryption (SSE-KMS), versioning and Block Public Access
- Use S3 native state locking (`use_lockfile = true`), which replaces the older DynamoDB lock table
- Limit bucket access to the CI deploy role and a few admins
- Keep state per environment, in the matching account
- Mark sensitive outputs and avoid putting secrets in variables at all where possible

```hcl
terraform {
  backend "s3" {
    bucket       = "acme-tfstate-prod"
    key          = "orders/terraform.tfstate"
    region       = "eu-west-1"
    encrypt      = true
    kms_key_id   = "alias/tfstate"
    use_lockfile = true
  }
}
```

## 295: How do you lock a GitHub Actions OIDC role to one repo and branch?

Check the `aud` and `sub` claims in the trust policy.

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
          "token.actions.githubusercontent.com:sub": "repo:acme/orders-service:ref:refs/heads/main"
        }
      }
    }
  ]
}
```

For deployments through GitHub environments, use `repo:acme/orders-service:environment:production`, so environment protection rules (required reviewers) also apply.

## 296: How do you keep a CDK or CloudFormation deploy role least privilege?

CDK bootstrap creates several roles: a deploy role that the pipeline assumes, and a CloudFormation execution role that CloudFormation uses to create resources. By default the execution role has `AdministratorAccess`. Tighten it by bootstrapping with `--cloudformation-execution-policies` set to a custom policy, and add a permissions boundary to roles the app creates with a custom bootstrap template. Keep the pipeline role able only to start deployments, not to change resources directly.

## 297: How do you protect AWS credentials from pull requests opened from forks?

- Workflows triggered by `pull_request` from forks do not get secrets or OIDC tokens with write access by default. Keep it that way.
- Avoid `pull_request_target` with a checkout of the fork's code, because it runs untrusted code with your secrets.
- Only allow deploy roles for `main` or protected environments in the trust policy `sub` condition.
- Give PR builds a read-only role, if any.
- Pin third-party actions to a full commit SHA to avoid tampered tags.

## 298: How do you run a Well-Architected security review?

Pick a workload and use the Well-Architected Tool in the console. Answer the Security Pillar questions with the team that owns the workload. The tool flags high-risk and medium-risk issues and links to guidance. Turn the high-risk issues into backlog items with owners, then review again after some months to track progress. Custom lenses let you add your own company standards.

## 299: Why is a security group open to 0.0.0.0/0 on port 22 or 3389 so dangerous?

Internet scanners find open SSH and RDP within minutes of an instance starting. Attackers then try leaked keys, weak passwords and known exploits. Even with strong auth, any future vulnerability in the service is directly exposed. Use Session Manager or EC2 Instance Connect Endpoint instead, and detect and block these rules with Config, Security Hub CSPM and Firewall Manager.

## 300: What happened in the Capital One breach and what are the lessons?

In 2019 an attacker used a server-side request forgery (SSRF) bug in a misconfigured web application firewall running on EC2. The SSRF reached IMDSv1 and got the instance role's credentials. That role could list and read many S3 buckets, so the attacker copied data on about 100 million people.

Lessons:

- Use IMDSv2, which blocks this kind of SSRF
- Keep instance roles narrow, especially for internet-facing hosts
- Alert when instance credentials are used outside AWS (GuardDuty does this now)
- Use data perimeter controls, like VPC endpoint conditions on sensitive buckets

# Advanced Questions (301-450)

## 301: When can a resource-based policy allow access even if the identity policy does not?

Within the same account, if a resource-based policy names the principal directly, the request can be allowed even without an identity-based allow. The details depend on what was named:

- If the policy names an IAM user ARN, or a role session ARN, the allow works even when a permissions boundary or session policy would not allow it.
- If the policy names a role ARN (not the session), the role session's permissions boundary and session policy still limit the request.
- An explicit deny anywhere, and SCPs and RCPs, still apply.
- For KMS keys and role trust policies, the resource policy is required in all cases.

Cross-account, both sides always need to allow.

## 302: Why might a trust policy suddenly stop working after a role is recreated?

When you put a role ARN in a trust policy or resource policy, IAM stores the role's unique ID (like `AROAEXAMPLEID`), not the name. If the role is deleted and recreated with the same name, it gets a new ID, and the old policy shows a strange ID instead of an ARN. It no longer matches. This is a security feature: someone cannot delete and recreate a role to inherit its old access. Fix it by updating the policy to point to the new role.

## 303: What are common IAM privilege escalation paths?

If a principal has any of these, it can often become admin:

- `iam:CreatePolicyVersion` or `iam:SetDefaultPolicyVersion` on its own policy
- `iam:AttachUserPolicy`, `AttachRolePolicy`, `PutUserPolicy`, `PutRolePolicy` on itself or a role it can assume
- `iam:CreateAccessKey` or `iam:CreateLoginProfile` / `UpdateLoginProfile` on another user
- `iam:UpdateAssumeRolePolicy` on a powerful role
- `iam:PassRole` plus `lambda:CreateFunction`, `ec2:RunInstances`, `cloudformation:CreateStack`, `glue:CreateDevEndpoint` and similar
- `lambda:UpdateFunctionCode` on a function with a powerful role
- `ssm:SendCommand` or `ssm:StartSession` on an instance with a powerful role

Review policies for these combinations, not just for `*`.

## 304: How do you find privilege escalation risks in an account?

- IAM Access Analyzer policy checks and unused access findings
- Open-source tools: PMapper (builds a graph of who can become whom), Cloudsplaining (flags risky actions in policies), Prowler and CloudFox
- Custom policy checks in CI with `CheckAccessNotGranted` for actions like `iam:PassRole` on `*`
- Regular reviews of who can modify IAM, Lambda code and SSM documents

Escalation paths often come from combining two "harmless" permissions, so a graph view helps.

## 305: How do you revoke credentials for a role session that has already been issued?

Temporary credentials cannot be cancelled directly. Instead, attach a deny policy to the role that blocks any session issued before now:

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Deny",
      "Action": "*",
      "Resource": "*",
      "Condition": {
        "DateLessThan": { "aws:TokenIssueTime": "2026-11-13T09:30:00Z" }
      }
    }
  ]
}
```

The console's "Revoke active sessions" button adds exactly this as `AWSRevokeOlderSessions`. New sessions still work, so first fix whatever let the attacker get credentials, or they will just get new ones.

## 306: How can you stop stolen EC2 role credentials from being used outside the instance?

Use the condition keys AWS adds to credentials delivered through IMDS:

- `aws:ec2InstanceSourceVpc`: the VPC ID of the instance
- `aws:ec2InstanceSourcePrivateIPv4`: the private IP of the instance

Compare them with the actual request's network values in an SCP or RCP:

```json
{
  "Sid": "DenyStolenInstanceCreds",
  "Effect": "Deny",
  "Action": "*",
  "Resource": "*",
  "Condition": {
    "StringNotEquals": { "aws:ec2InstanceSourceVpc": "${aws:SourceVpc}" },
    "Null": { "ec2:SourceInstanceARN": "false" },
    "BoolIfExists": { "aws:ViaAWSService": "false" }
  }
}
```

Requests from the instance through a VPC endpoint have a matching VPC. Requests from an attacker's laptop do not. This needs VPC endpoints for the services involved, since `aws:SourceVpc` is only set on requests through endpoints, so roll it out carefully.

## 307: How do you design a data perimeter?

Think of three perimeters and apply each to identities, resources and networks:

| Goal                                        | Control                       | Key condition                                                          |
| ------------------------------------------- | ----------------------------- | ---------------------------------------------------------------------- |
| Only trusted identities access my resources | RCPs, resource policies       | `aws:PrincipalOrgID`, `aws:PrincipalIsAWSService`                      |
| My identities only access trusted resources | SCPs, VPC endpoint policies   | `aws:ResourceOrgID`                                                    |
| Access only from expected networks          | SCPs, RCPs, resource policies | `aws:SourceVpc`, `aws:SourceVpce`, `aws:SourceIp`, `aws:ViaAWSService` |

Roll out in stages: start with logging what would be denied (using CloudTrail queries), add exceptions for AWS services and partners, and only then enforce. AWS publishes example policies in the `data-perimeter-policy-examples` GitHub repo.

## 308: How do you avoid breaking AWS services when adding network conditions to policies?

Many AWS services call other services for you from AWS networks, not from your VPC. For example, CloudFormation creates resources, Athena reads S3, or KMS is called by S3 when you upload an object. These requests do not match your `aws:SourceVpc` or `aws:SourceIp`. Exclude them with:

- `aws:ViaAWSService` (true when a service makes a call using your credentials)
- `aws:PrincipalIsAWSService` (true when a service principal itself makes the call)
- `aws:CalledVia` / `aws:CalledViaFirst` for specific services

Always use `BoolIfExists` on these keys so requests without them are handled as you intend.

## 309: What is aws:CalledVia?

It lists the services that made a request on behalf of the principal, in order. For example, if a user runs an Athena query that reads S3, the S3 request has `aws:CalledVia` = `athena.amazonaws.com`. You can use it to allow S3 access only through Athena, or to allow `kms:Decrypt` only when CloudFormation is calling. Only some services set it, so check the documentation before relying on it.

## 310: How do you prevent your roles from assuming roles in accounts outside your organization?

Use an SCP that denies `sts:AssumeRole` (and the `WithSAML`/`WithWebIdentity` variants as needed) when the target role is not in your organization:

```json
{
  "Sid": "DenyAssumeOutsideOrg",
  "Effect": "Deny",
  "Action": "sts:AssumeRole",
  "Resource": "*",
  "Condition": {
    "StringNotEquals": { "aws:ResourceOrgID": "o-a1b2c3d4e5" },
    "ArnNotLike": {
      "aws:PrincipalArn": "arn:aws:iam::*:role/ThirdPartyIntegration"
    }
  }
}
```

This stops attackers from pivoting into their own accounts with credentials from yours. Add exceptions for approved vendors.

## 311: How do RCPs help with the confused deputy problem at scale?

Instead of adding `aws:SourceArn` and `aws:SourceAccount` conditions to every bucket, queue and key policy, you can write one RCP that denies requests from AWS service principals unless they act on behalf of your organization:

```json
{
  "Sid": "EnforceConfusedDeputyProtection",
  "Effect": "Deny",
  "Principal": "*",
  "Action": ["s3:*", "sqs:*", "kms:*", "secretsmanager:*", "sts:*"],
  "Resource": "*",
  "Condition": {
    "StringNotEqualsIfExists": { "aws:SourceOrgID": "o-a1b2c3d4e5" },
    "Null": { "aws:SourceAccount": "false" },
    "Bool": { "aws:PrincipalIsAWSService": "true" }
  }
}
```

New resources are covered automatically, and teams cannot forget it.

## 312: How do you protect security tooling in member accounts from local admins?

Use an SCP that denies changes to security resources unless the caller is the security team's role:

```json
{
  "Sid": "ProtectSecurityBaseline",
  "Effect": "Deny",
  "Action": [
    "cloudtrail:StopLogging",
    "cloudtrail:DeleteTrail",
    "cloudtrail:UpdateTrail",
    "cloudtrail:PutEventSelectors",
    "guardduty:DeleteDetector",
    "guardduty:DisassociateFromAdministratorAccount",
    "guardduty:UpdateDetector",
    "config:StopConfigurationRecorder",
    "config:DeleteConfigurationRecorder",
    "config:DeleteDeliveryChannel",
    "securityhub:DisableSecurityHub",
    "access-analyzer:DeleteAnalyzer",
    "iam:DeleteRole",
    "iam:UpdateAssumeRolePolicy",
    "iam:DetachRolePolicy",
    "iam:PutRolePolicy"
  ],
  "Resource": "*",
  "Condition": {
    "ArnNotLike": { "aws:PrincipalArn": "arn:aws:iam::*:role/SecurityAdmin" }
  }
}
```

In practice the IAM actions are scoped to the baseline role ARNs, not `*`, so teams can still manage their own roles.

## 313: What limits do SCPs have and how do you work around them?

- Up to 5 SCPs attached per root, OU or account
- Each SCP is limited to 5,120 characters
- They do not apply to the management account or service-linked roles

To stay within limits: remove whitespace (the console counts it), group actions with wildcards like `cloudtrail:Delete*` carefully, move some controls to RCPs or permissions boundaries, and spread controls across levels of the OU tree. Keep SCPs in Git and deploy them through a pipeline so changes are reviewed.

## 314: How do you safely roll out a new SCP?

1. Write it and test it with the IAM policy simulator, which can include SCPs for member accounts.
2. Search CloudTrail (CloudTrail Lake or Athena) for calls that would have been denied in the last 90 days.
3. Attach it to a Policy Staging OU with a test account, and run real workloads there.
4. Roll it out to sandbox and dev OUs, watch for `AccessDenied` errors that mention a service control policy.
5. Then roll it out to production.

A bad SCP at the root can block every account at once, including incident responders.

## 315: How would you design identity and access for a company with 200 AWS accounts?

- One identity source (the corporate IdP) connected to IAM Identity Center with SCIM
- A small set of permission sets (ReadOnly, Developer, Operator, Admin, SecurityAudit, BreakGlass), with permissions boundaries for Developer
- Group-based assignments by OU, managed in Terraform or CloudFormation, not clicked in the console
- ABAC with IdP attributes to avoid a permission set per team
- No IAM users except tightly controlled break-glass
- Workload roles created by pipelines, with boundaries
- Central security roles deployed with StackSets and protected by SCPs
- Regular access reviews using Access Analyzer and last-accessed data

## 316: How do you design break-glass access when you rely on IAM Identity Center?

Identity Center depends on your IdP and on its home region. If either fails, nobody can sign in. So:

- Keep a couple of IAM users with admin roles in the management account and key accounts, or plan to use centralized root sessions
- Protect them with FIDO2 MFA, keep the credentials in a physical safe split between people
- Alert on every use through EventBridge and page the security team
- Test the procedure a few times a year
- Exclude break-glass principals from SCPs that could otherwise lock you out (like region restrictions)

## 317: How does centralized root access work in AWS Organizations?

After you enable it, you can remove root credentials (password, keys, MFA) from member accounts, and new accounts are created without them. When a root-only task is needed, a principal in the management account or delegated admin calls `sts:AssumeRoot` with a task policy that limits the session to one job, such as deleting a broken S3 bucket policy or unlocking an SQS queue policy. The session is short and fully logged.

```bash
aws sts assume-root \
  --target-principal 222233334444 \
  --task-policy-arn arn=arn:aws:iam::aws:policy/root-task/S3UnlockBucketPolicy \
  --duration-seconds 900
```

This removes hundreds of root passwords and MFA devices you would otherwise have to protect.

## 318: How do you secure the Organizations management account?

- Run no workloads in it
- Very few people have access, with phishing-resistant MFA
- Delegate security services, Identity Center admin, StackSets and Config to other accounts
- Avoid permission sets that grant admin there by default
- Watch it closely, since SCPs do not apply to it
- Remember it can do `sts:AssumeRoot`, create accounts, change SCPs and leave nothing behind in member accounts. A compromise here means the whole organization is compromised.

## 319: How would you design Cognito for a multi-tenant SaaS app?

Options:

- One user pool with a `custom:tenant_id` attribute (read-only for users), added to tokens with a pre token generation trigger. Simple and scales to many tenants.
- One app client per tenant inside one pool, useful when tenants need different settings.
- One user pool per tenant, needed when tenants have their own federation, password policies or strict isolation, but harder to manage at scale.

Whatever you choose, the backend must take the tenant ID from the verified token, never from a request parameter, and enforce it on every data access.

## 320: How do you handle token revocation with Cognito?

JWT access tokens are valid until they expire, and APIs that only check the signature cannot know a user was signed out. Mitigations:

- Short access token lifetimes (5 to 15 minutes)
- Refresh token revocation (`RevokeToken`) and refresh token rotation, so a stolen refresh token stops working
- `GlobalSignOut` or `AdminUserGlobalSignOut`, which invalidates refresh tokens. Cognito also rejects revoked access tokens on its own APIs, but your API will still accept them unless you check.
- For high-risk actions, check with Cognito (for example `GetUser`) or keep your own deny list of revoked token IDs (`jti`) until they expire.

## 321: What are common JWT validation mistakes?

- Not checking the signature, or accepting `alg: none`
- Fetching keys from a URL in the token (`jku`) instead of a fixed JWKS URL
- Accepting ID tokens where access tokens are expected, or the other way round
- Not checking `iss`, `aud`/`client_id` or `exp`
- Reading claims like `email` that the user can change, and treating them as verified
- Using a user-writable custom attribute for authorization
- Not caching the JWKS, then failing open when the fetch fails

Use a maintained library like `aws-jwt-verify` instead of writing it yourself.

## 322: How do you give each mobile user access to only their own S3 folder?

Use a Cognito identity pool so users get temporary credentials, and a role policy with the identity ID as a variable:

```json
{
  "Effect": "Allow",
  "Action": ["s3:GetObject", "s3:PutObject", "s3:DeleteObject"],
  "Resource": "arn:aws:s3:::user-uploads/private/${cognito-identity.amazonaws.com:sub}/*"
}
```

Risks to manage: users can call any allowed API directly, not just through your app, so keep the policy narrow. Users can upload anything, so scan uploads and limit size. And the guest role must not have this access.

## 323: How do you do fine-grained authorization in a multi-tenant API on AWS?

Authentication (who you are) is handled by Cognito or another IdP. Authorization (what you can do) needs more than token scopes. Options:

- A Lambda authorizer that checks the token and returns a policy with tenant context
- Amazon Verified Permissions, which stores policies in the Cedar language and answers "is this principal allowed to do this action on this resource?" with `IsAuthorized` calls
- Authorization checks in the service code itself, using the verified tenant and role

Keep authorization logic in one place, test it, and log every decision for audits.

## 324: Why does IMDSv2 stop most SSRF attacks?

Typical SSRF lets an attacker make the server send a GET request to a URL. IMDSv2 needs:

1. A PUT request to get a token, which most SSRF bugs cannot send.
2. A custom header (`X-aws-ec2-metadata-token`) on every request, which SSRF usually cannot set.
3. IMDSv2 rejects token requests that contain an `X-Forwarded-For` header, which blocks many open proxies and WAFs that forward requests.
4. The hop limit stops the token response from leaving the instance through a proxy or container.

A full remote code execution still gets credentials, so least privilege on the role still matters.

## 325: How do the threat models of the node role, IRSA and Pod Identity differ on EKS?

- Node role: shared by every pod on the node. If any pod is compromised and can reach IMDS, it gets the node's permissions, which include pulling images and managing ENIs.
- IRSA and Pod Identity: each service account gets its own role, so a compromised pod only gets its own permissions.

Block pods from IMDS (hop limit 1 and network policies), keep the node role minimal, and use one role per service account. If the attacker breaks out to the node, they can read other pods' tokens on that node, so isolate sensitive workloads on separate node groups or Fargate.

## 326: How would you harden an EKS cluster?

- Private API endpoint or public with CIDR limits
- Access entries with least privilege, no shared admin role
- Envelope encryption of Kubernetes secrets with KMS (on by default for new clusters), or use Secrets Manager through the Secrets Store CSI driver
- Pod Security Standards (`restricted` profile) through Pod Security Admission
- Network policies to limit pod-to-pod traffic
- Pod Identity per workload, IMDS blocked from pods
- Control plane audit logs to CloudWatch, plus GuardDuty EKS Protection and Runtime Monitoring
- Admission controls (Kyverno or OPA Gatekeeper) to block privileged pods and unsigned images
- Managed node groups or Bottlerocket nodes kept up to date, or EKS Auto Mode

## 327: How are Kubernetes secrets protected in EKS?

etcd volumes are encrypted at rest by AWS. On top of that, EKS supports envelope encryption with a KMS key: each secret is encrypted with a data key, which is encrypted by your KMS key. New clusters on recent Kubernetes versions get envelope encryption by default with an AWS owned key, and you can use your own customer managed key. Remember that anyone with `get secrets` RBAC permission can still read them, so RBAC is the more important control.

## 328: How do you limit pod-to-pod network traffic in EKS?

- Kubernetes NetworkPolicy, enforced natively by the Amazon VPC CNI (turn on its network policy support) or by Calico or Cilium
- Security groups for pods, which give specific pods their own ENI security group so you can control access to RDS and other AWS resources by pod
- Start with a default deny policy per namespace and allow only the needed flows

```yaml
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
  name: default-deny
  namespace: orders
spec:
  podSelector: {}
  policyTypes: ["Ingress", "Egress"]
```

## 329: What is the impact of a container breakout on an EKS EC2 node?

The attacker gets the node: they can read service account tokens and secrets of every pod on that node, use the node role through IMDS, see the containers' file systems and maybe reach the kubelet API. Mitigations: do not run privileged pods, use `restricted` Pod Security Standards, use Bottlerocket or a minimal OS with SELinux, keep nodes patched, keep the node role small, separate sensitive workloads onto their own nodes or Fargate, and detect suspicious activity with GuardDuty Runtime Monitoring.

## 330: How does compute isolation differ between Lambda, Fargate and EC2-based containers?

Lambda and Fargate run each function environment or task in its own Firecracker micro VM, with a dedicated kernel, so a kernel exploit does not reach other tenants. Containers on EC2 share the host kernel with other containers on that instance. For multi-tenant SaaS running untrusted or customer code, Lambda or Fargate give stronger isolation by default. On EC2, you would need separate instances per tenant or extra sandboxing like gVisor.

## 331: How do you design KMS keys for a large organization?

Common patterns:

- Keys per account and per data classification (for example `prod-orders-pii`), owned by the workload account. This limits blast radius and keeps teams in control.
- A few central keys in a security account for shared things like the CloudTrail log bucket or backups.
- Consistent aliases and tags, with key policies generated from templates.
- `kms:ViaService` and encryption context conditions to narrow how keys are used.
- An SCP that limits `kms:PutKeyPolicy` and `kms:ScheduleKeyDeletion` to key admin roles.

Avoid one giant key for everything, because then the key policy becomes the most powerful policy in the company.

## 332: What is needed for a role in account B to use a KMS key in account A?

1. Account A's key policy must allow account B (or the specific role) the needed actions.
2. Account B's IAM policy for the role must allow those actions on the key ARN (with the full ARN, not an alias).
3. If the key is used through a service, that service must support cross-account keys. AWS managed keys can never be used cross-account.
4. Watch for conditions like `kms:ViaService` or `kms:CallerAccount` that may block it.

If either policy is missing, you get `AccessDeniedException` from KMS, which often surfaces as a confusing S3 or EBS error.

## 333: How do you handle KMS request limits in high-volume apps?

KMS has per-account, per-region request quotas (for example, several thousand to tens of thousands of cryptographic requests per second depending on region and operation). To stay under them:

- Use envelope encryption, so you call KMS per data key, not per record
- Use S3 Bucket Keys for SSE-KMS
- In the AWS Encryption SDK, use the AWS KMS hierarchical keyring, which caches branch keys locally and reduces KMS calls
- Request a quota increase for known peaks

Watch for `ThrottlingException` in CloudWatch metrics and app logs.

## 334: What is crypto-shredding and how can KMS support it?

Crypto-shredding means deleting data by destroying the key that encrypts it, instead of finding and deleting every copy (including backups). With KMS, you could use a key per customer or a data key per customer stored in a table encrypted under a KMS key. When the customer asks to be deleted, delete their data key (or schedule deletion of their KMS key). All their ciphertext, even in old backups, becomes unreadable. It helps with GDPR deletion but needs careful design so you do not destroy keys by accident.

## 335: What are the trade-offs of importing your own key material into KMS?

Imported material (BYOK) lets you keep a copy outside AWS and prove where the key came from. But:

- You are responsible for keeping a backup. If KMS deletes it (for example after an expiration date you set), only your copy can restore it.
- Automatic rotation is not supported for imported material in the same way, so you plan rotation yourself (KMS now supports on-demand rotation for imported keys, but you still supply the new material).
- The import process adds operational steps and risk.

It rarely adds real security over AWS-generated keys. Use it when a regulation or policy requires key material generated by you.

## 336: How do you avoid locking yourself out of a KMS key?

KMS has a lockout safety check: `PutKeyPolicy` fails if the new policy would stop the caller from changing the policy later, unless you set `BypassPolicyLockoutSafetyCheck`, which you should almost never do. Keep the account root statement (`arn:aws:iam::<account>:root` with `kms:*`) so IAM admins can always recover access. If a key does become unmanageable, only AWS Support can help, and only in some cases.

## 337: How did attackers use SSE-C to hold S3 data for ransom, and how do you defend against it?

In early 2025, a group used leaked AWS keys with S3 write access to rewrite objects using SSE-C with a key only they knew. AWS stores only an HMAC of the key, so neither AWS nor the owner could decrypt. They then set lifecycle rules to delete the data within days and left a ransom note.

Defenses:

- No long-lived keys, and least privilege on `s3:PutObject` and `s3:PutLifecycleConfiguration`
- Block SSE-C where you do not use it, by bucket setting (now the default for new buckets) or with a policy denying requests that include `s3:x-amz-server-side-encryption-customer-algorithm`
- Versioning plus Object Lock or replication to a separate account
- GuardDuty S3 protection and alerts on unusual lifecycle and encryption changes

## 338: How would you design S3 for ransomware resilience?

- Versioning on all important buckets
- Object Lock (compliance mode for critical data) or AWS Backup for S3 with Vault Lock
- Replication to a separate account in another OU, with ownership overridden and Object Lock on the target
- Deny `s3:PutLifecycleConfiguration`, `s3:PutBucketVersioning` and `s3:DeleteObjectVersion` to everyone but a small admin role
- Block SSE-C, restrict which KMS keys can be used
- RCPs to stop access from outside the organization
- GuardDuty S3 Protection and CloudTrail data events, with alerts on mass deletes or rewrites
- Regular restore tests

## 339: What should you watch out for with Object Lock compliance mode?

Nobody, including root and AWS Support, can delete a locked version until retention ends. If someone sets a 10-year retention on terabytes of data by mistake, you pay for it for 10 years, and you cannot close the account normally while it holds locked data. Use governance mode for testing and most cases, and compliance mode only for data you are sure about. Restrict `s3:PutObjectRetention` and `s3:PutBucketObjectLockConfiguration` so attackers cannot use it to cause cost damage.

## 340: How would you design a secure file upload pipeline on AWS?

1. The backend checks the user and returns a presigned POST with a short expiry, a fixed key prefix, size limit and content type.
2. Files land in a quarantine bucket with no public access.
3. GuardDuty Malware Protection for S3 (or your own scanner) scans each new object and tags it.
4. An EventBridge rule moves clean files to the main bucket and deletes or isolates infected ones.
5. Downstream code only reads from the main bucket, and never trusts the file name or extension from the client.
6. Serve files through CloudFront with signed URLs or an authorized API, with `Content-Disposition: attachment` for user content.

## 341: In which ways can S3 data be exposed even with Block Public Access on?

Block Public Access only blocks "public" access, meaning anyone on the internet. Data can still leak through:

- Bucket policies or access points shared with other accounts (that is not considered public)
- A CloudFront distribution that serves the whole bucket without auth
- Long-lived presigned URLs
- Over-broad IAM roles in your own accounts, including roles assumable by vendors
- Replication to a bucket you do not control
- Copies in logs, analytics or backups with weaker settings

Use Access Analyzer external access findings, Macie and RCPs to cover these.

## 342: What is the risk of predictable S3 bucket names, and how do you defend against it?

S3 bucket names are global. If your code or a service writes to a bucket name it expects to exist (like `myapp-assets-<region>`) and that bucket does not exist yet, or was deleted, an attacker can create it and receive your data or serve you malicious files. Research in 2024 showed some AWS services and open-source tools had this problem. Defenses:

- Pass `ExpectedBucketOwner` (the `x-amz-expected-bucket-owner` header) in S3 calls so they fail if another account owns the bucket
- Use `aws:ResourceOrgID` or `aws:ResourceAccount` in SCPs or endpoint policies
- Add random suffixes or the account ID to bucket names
- Do not delete buckets that code or DNS still points to

## 343: What is subdomain takeover on AWS?

A DNS record points to an AWS resource that no longer exists, like a deleted S3 website bucket, a CloudFront distribution, an Elastic Beanstalk environment or a released Elastic IP. An attacker creates a resource with the same name or grabs the IP, and now serves content on your subdomain. They can steal cookies or run phishing. Prevent it by deleting DNS records before or with the resource, using alias records where possible, and scanning your Route 53 zones for dangling records.

## 344: How would you design the network for a workload handling card data?

- Dedicated accounts for the cardholder data environment (CDE)
- A VPC with private subnets only for app and database tiers. Public ingress only through CloudFront and WAF to an ALB, or through a VPC origin
- Egress through a central inspection VPC with Network Firewall and a domain allow list
- VPC endpoints with policies for all AWS services used
- Security groups between tiers, NACLs to block everything else
- No peering to non-CDE VPCs. If connectivity is needed, use Transit Gateway route tables that only allow specific flows, or PrivateLink
- Flow Logs, DNS query logs and Network Firewall logs sent to the log archive account
- TLS everywhere, including inside the VPC

## 345: How do you build centralized egress inspection with Transit Gateway?

Spoke VPCs send `0.0.0.0/0` to the Transit Gateway. The TGW routes it to an inspection VPC, where traffic goes through Network Firewall endpoints, then to a NAT gateway and internet gateway in an egress VPC (or the same VPC). Turn on appliance mode on the inspection VPC attachment, so both directions of a flow go through the same AZ's firewall endpoint, because stateful inspection needs symmetric traffic. Use separate TGW route tables so spokes cannot talk to each other unless allowed.

## 346: What are the trade-offs of centralizing interface VPC endpoints?

Centralizing endpoints in a shared services VPC, with Route 53 private hosted zones shared to spoke VPCs, cuts cost (fewer endpoints per VPC) and gives one place to manage endpoint policies. But:

- Traffic crosses the Transit Gateway, which adds data processing cost and latency
- `aws:SourceVpce` conditions become broader, because many VPCs share one endpoint
- Endpoint policies apply to everyone using it, so per-workload restrictions are harder

Many companies centralize common endpoints and keep sensitive ones local to the workload VPC.

## 347: How do you secure a PrivateLink endpoint service you offer to customers?

- Require acceptance for each connection request, or allow-list principals (account or role ARNs) that may create endpoints
- Never allow `*` as a principal
- Put the service behind an NLB with security groups, and check the source VPC endpoint ID from the Proxy Protocol v2 header to map connections to customers
- Still authenticate requests at the application level. Private connectivity is not authentication.
- Use TLS on the NLB listener or end-to-end
- Monitor connections and reject or delete endpoints of customers who leave

## 348: What is Gateway Load Balancer used for?

Gateway Load Balancer (GWLB) lets you insert third-party virtual appliances, like next-generation firewalls or IDS, into the traffic path transparently. Traffic is sent to the appliances using GENEVE encapsulation, and GWLB endpoints in your VPCs are used as route targets. It scales and health-checks the appliances. Teams use it when they need a specific vendor firewall instead of AWS Network Firewall.

## 349: What is AWS Verified Access and when would you use it?

Verified Access gives users access to internal web apps (and, since 2025, non-HTTP resources like databases and SSH servers) without a VPN. Each request is checked against policies written in Cedar that use identity data from IAM Identity Center or an OIDC provider and device posture from tools like CrowdStrike or Jamf. It is a zero trust approach: every request is verified, not just the network connection. It fits when you want to retire a VPN for internal tools.

## 350: How can attackers exfiltrate data through DNS, and how do you detect it?

Malware encodes data in DNS queries to a domain the attacker controls, like `c2VjcmV0.attacker.com`. Even with no internet route, the VPC resolver forwards these queries. Detection and prevention:

- GuardDuty detects DNS exfiltration patterns in the resolver logs it analyzes
- Route 53 Resolver query logging plus your own analysis (long or high-entropy subdomains, high query volume to one domain)
- DNS Firewall with managed threat lists, and in strict environments an allow list of domains with everything else blocked
- DNS Firewall Advanced, which detects DNS tunneling and domain generation algorithm (DGA) patterns

## 351: How would you design a DDoS-resilient architecture on AWS?

- Put everything public behind CloudFront (and Route 53 for DNS), so attacks hit the large edge network first
- Keep origins private: VPC origins or ALBs locked to CloudFront
- Use WAF with rate-based rules, managed rule groups and Bot Control
- Cache as much as you can, so floods of the same request never reach the origin
- Auto Scaling and serverless back ends that can absorb spikes, with limits so cost does not explode
- Shield Advanced for critical apps, with health checks and proactive engagement
- Have a runbook: who to call, which rules to switch from count to block, and how to put up a static fallback page

## 352: What are the request body inspection limits in AWS WAF and why do they matter?

WAF only inspects the first part of a request body: 8 KB for ALB and AppSync, and 16 KB by default for CloudFront, API Gateway, Cognito, App Runner and Verified Access (you can raise it to 64 KB at extra cost). An attacker can put padding before the payload to push it past the inspected part. Set the oversize handling in each rule to `MATCH` or add a rule that blocks bodies over the limit for paths that do not expect large bodies. The `SizeRestrictions_BODY` rule in the core rule set also blocks large bodies, which is why upload endpoints often need an exception.

## 353: How do you tune AWS WAF for a JSON API?

- Use JSON body parsing in rule statements so WAF inspects values, not raw text, and set how invalid JSON is handled
- Exclude or scope down rules that cause false positives on known fields
- Add rate-based rules keyed on API key headers, JWT claims or IP
- Use JA3 or JA4 TLS fingerprints (available for CloudFront) to spot automated clients that rotate IPs
- Start in count mode, analyze logs with Athena or CloudWatch Logs Insights, then block
- Remember that WAF does not replace input validation in the app

## 354: What does Shield Advanced automatic application layer DDoS mitigation do?

When turned on for a CloudFront distribution or ALB with a WAF web ACL, Shield Advanced learns the normal traffic baseline. During an attack it creates, tests and deploys WAF rules in a rule group it manages, matching the attack's signature, either in count or block mode. When the attack ends, it removes them. This handles HTTP floods faster than a person writing rules at 3 a.m., but you should still review what it creates.

## 355: How do you rotate keys for CloudFront signed URLs?

Use trusted key groups (not the legacy root-account CloudFront key pairs). A key group can hold up to five public keys. To rotate:

1. Create a new key pair and upload the public key to CloudFront.
2. Add it to the key group, so both old and new keys are valid.
3. Switch your signing service to the new private key, stored in Secrets Manager.
4. Wait until all URLs signed with the old key have expired.
5. Remove the old key from the group.

## 356: How do you use OAC with an S3 bucket encrypted with SSE-KMS?

Besides the bucket policy allowing `cloudfront.amazonaws.com` with `AWS:SourceArn`, the KMS key policy must allow CloudFront to decrypt:

```json
{
  "Sid": "AllowCloudFrontDecrypt",
  "Effect": "Allow",
  "Principal": { "Service": "cloudfront.amazonaws.com" },
  "Action": "kms:Decrypt",
  "Resource": "*",
  "Condition": {
    "StringEquals": {
      "AWS:SourceArn": "arn:aws:cloudfront::111122223333:distribution/E1ABCDEF2GHIJ"
    }
  }
}
```

OAI never supported this, which is one reason OAC replaced it. If you also upload through CloudFront, add `kms:Encrypt` and `kms:GenerateDataKey*`.

## 357: What is a security risk with Lambda authorizer caching?

The authorizer result is cached per identity source (for example the token) for the TTL. If the returned policy only allows the specific method ARN that was called (`event.methodArn`), the next call with the same token to a different route uses the cached policy and is denied. To avoid that, people often return a wildcard like `arn:aws:execute-api:region:account:api-id/stage/*/*`, which then allows every route for that token for the cache time. The safe approach: return a policy listing all routes the user is allowed to call, include everything that affects the decision in the identity source, or turn caching off for authorizers that depend on the path.

## 358: How do you secure incoming webhooks on AWS?

- Verify the sender's signature (for example Stripe's or GitHub's HMAC header) with a secret from Secrets Manager, using a constant-time comparison
- Check timestamps to block replays
- Restrict source IPs with WAF if the provider publishes ranges, but do not rely on this alone
- Return quickly and process asynchronously through SQS, so slow processing does not cause retries or timeouts
- Make processing idempotent, since providers retry
- Rate-limit with WAF or API Gateway throttling

## 359: What is the threat model for a Lambda-based app?

- Event injection: untrusted data comes from many sources (API Gateway, S3 object keys, SQS messages, DynamoDB streams). Validate all of it.
- Over-privileged execution roles: one bug becomes full data access.
- Vulnerable dependencies and layers.
- Secrets in environment variables, readable by anyone with `GetFunctionConfiguration`.
- Denial of wallet: an attacker triggers huge numbers of invocations. Use throttling, WAF and reserved concurrency.
- Missing auth on function URLs or API routes.
- Logging sensitive data to CloudWatch.

## 360: How can an attacker steal Lambda credentials, and what can you do about it?

Lambda credentials are in environment variables (`AWS_ACCESS_KEY_ID`, `AWS_SECRET_ACCESS_KEY`, `AWS_SESSION_TOKEN`). Bugs like path traversal reading `/proc/self/environ`, command injection, or code that returns or logs `process.env` can leak them. With those, the attacker uses the function's role from anywhere. Mitigations: narrow execution roles, never log the environment, add network-based conditions (VPC endpoints plus `aws:SourceVpc` checks) for sensitive actions, and watch GuardDuty for Lambda credentials used from unusual places.

## 361: What is "denial of wallet" and how do you defend serverless apps against it?

It is an attack that tries to make you pay, not to take you down. Serverless scales automatically, so a flood of requests to a public function URL or API turns into a large bill. Defenses:

- WAF with rate-based rules in front of everything public
- API Gateway throttling and usage plans
- Reserved concurrency limits on functions
- Avoid public `NONE` auth function URLs
- AWS Budgets alerts and cost anomaly detection
- Shield Advanced cost protection for supported resources

## 362: How do you secure ECS Exec?

ECS Exec gives a shell in running containers through Session Manager. Control it with:

- IAM: limit `ecs:ExecuteCommand` by cluster, task and the `ecs:container-name` condition, and only for on-call roles
- Turn on logging of commands and output to S3 or CloudWatch Logs, and KMS encryption of the session
- Only enable it (`enableExecuteCommand`) on services that need it
- Alert on `ExecuteCommand` events in CloudTrail for production clusters

## 363: What is dependency confusion and how does CodeArtifact help?

Dependency confusion is when an attacker publishes a public package with the same name as your internal package and a higher version, and your build pulls the public one. CodeArtifact has package origin controls: for each package you can block upstream (public) versions or block direct publishing, so internal package names can only come from your repository. Combine this with lock files and scoped package names like `@acme/utils`.

## 364: How would an attacker abuse a CI/CD pipeline to reach AWS?

- Poisoned pipeline execution: changing the build script in a pull request so it runs attacker code with the pipeline's credentials
- Stealing long-lived AWS keys stored as CI secrets
- Compromising a third-party action or plugin
- Using an OIDC trust policy that is too broad (any repo in the org, any branch)
- Pushing a malicious image that the deploy role ships to production

Defenses: OIDC with tight `sub` conditions, separate build and deploy jobs, environment protection rules, pinned actions, least-privilege deploy roles, SCPs that limit what deploy roles can do, and signed artifacts verified at deploy.

## 365: What mistakes are common in GitHub Actions OIDC trust policies?

- No `sub` condition, or `StringLike` with `repo:acme/*`, which lets any repo in the org deploy
- Missing the `aud` check
- Trusting `pull_request` contexts for a deploy role
- One role for all environments, so a dev branch can deploy to production
- Not knowing that repo and org renames can let a new repo with the old name match the condition

GitHub lets you customize the `sub` claim to include immutable IDs like `repository_owner_id` and `repository_id`, which avoids the rename problem. Review these trust policies the same way you review admin permissions.

## 366: How would you set up cross-account deployments from a central CI/CD account?

- A tools or CI account runs pipelines (CodePipeline or GitHub Actions with OIDC into the tools account)
- Each target account (dev, staging, prod) has a deploy role that trusts only the pipeline role in the tools account, with `sts:ExternalId` or `aws:PrincipalArn` conditions
- Artifacts are stored in an S3 bucket encrypted with a KMS key shared with the target accounts
- Production deploys need a manual approval step or a protected environment
- Deploy roles in production have permissions boundaries, and SCPs stop them from touching security resources
- All role assumptions show the pipeline execution ID in the session name for tracing

## 367: How do you stop people from changing production resources outside the pipeline?

- Give humans read-only access in production by default, with a time-limited elevated permission set for emergencies
- An SCP that denies write actions in production unless the principal is the deploy role or break-glass role
- Config rules and drift detection (CloudFormation drift detection or `terraform plan` on a schedule) to find manual changes
- EventBridge alerts on write API calls by human sessions in production accounts

## 368: What is the difference between scanning IaC templates and scanning a Terraform plan?

Template scanning checks the source code. It is fast and runs early, but it can miss values that are only known after variables, modules and data sources are resolved. Plan scanning (for example `terraform show -json plan.out` fed into Checkov or OPA) checks exactly what will be created, with all values resolved. Do both: template scanning in the IDE and on pull requests, plan scanning as a gate before apply. CloudFormation Hooks give a similar last-step check on the AWS side.

## 369: How do you keep secrets out of CloudFormation templates?

Use dynamic references so CloudFormation fetches the value at deploy time and it never appears in the template or console:

```yaml
Resources:
  OrdersDb:
    Type: AWS::RDS::DBInstance
    Properties:
      Engine: postgres
      DBInstanceClass: db.t4g.medium
      AllocatedStorage: "20"
      MasterUsername: "{{resolve:secretsmanager:prod/orders/db:SecretString:username}}"
      MasterUserPassword: "{{resolve:secretsmanager:prod/orders/db:SecretString:password}}"
```

Even better, use `ManageMasterUserPassword: true` so no secret is needed at all. Mark parameters with `NoEcho: true` if you must pass secrets as parameters, but note they can still leak through outputs or metadata.

## 370: What are the single-user and alternating-users rotation strategies?

- Single user: the rotation function changes the password of one database user. Simple, but there is a short moment where clients with the old password fail until they refresh.
- Alternating users: two database users exist. Rotation updates the password of the user that is not current, then makes it current. Clients using the old credentials keep working until the next rotation. It needs a separate admin secret to create and update the users.

For high-traffic apps, alternating users avoid connection errors during rotation.

## 371: How can secret rotation fail, and how do you monitor it?

- The rotation Lambda cannot reach the database (wrong subnet, security group, or missing VPC endpoint for Secrets Manager)
- Missing permissions on the secret or KMS key
- The database rejects the change (password rules, user locked)
- Apps cache the secret forever and break after rotation

Monitor `RotationFailed` events through EventBridge, check the rotation function's logs, and test rotation in non-production first. Secrets Manager labels versions (`AWSCURRENT`, `AWSPENDING`, `AWSPREVIOUS`), so you can roll back by moving the label.

## 372: How can you avoid static secrets entirely on AWS?

- Workloads use IAM roles (instance profiles, task roles, Lambda roles, Pod Identity)
- CI uses OIDC federation
- Humans use Identity Center
- Databases use IAM authentication or RDS-managed passwords
- Service-to-service calls use SigV4 with IAM auth, or mTLS with short-lived certificates from Private CA
- Third-party APIs that need API keys are the main exception, and those go into Secrets Manager with rotation where possible

Fewer static secrets means fewer things to leak and rotate.

## 373: When is IAM database authentication not a good fit?

- High connection rates: generating tokens and the IAM auth check add overhead, and AWS recommends it for fewer than about 200 new connections per second
- Apps or tools that cannot generate tokens or require a fixed password
- Engines that do not support it, like Oracle (SQL Server and Oracle have other options like Kerberos)

Connection pooling with RDS Proxy helps: apps connect to the proxy with IAM auth, and the proxy holds pooled connections using a Secrets Manager secret.

## 374: How have public RDS snapshots led to data leaks, and how do you prevent it?

Teams share RDS snapshots to "public" by mistake, often while trying to share with one account. Anyone can then restore them and read the full database. Researchers have repeatedly found real public snapshots with personal data. Prevent it:

- Encrypt snapshots with a customer managed KMS key, which blocks public sharing
- An SCP that denies `rds:ModifyDBSnapshotAttribute` and `rds:ModifyDBClusterSnapshotAttribute` with `rds:AddAttribute/restore` set to `all`
- Security Hub CSPM control RDS.1 and Config rule `rds-snapshots-public-prohibited`

## 375: How do you block public EBS snapshots and AMIs?

Turn on block public access for EBS snapshots (`block-all-sharing` or `block-new-sharing`) and for AMIs, per region, or enforce them across the organization with declarative policies.

```bash
aws ec2 enable-snapshot-block-public-access --state block-all-sharing --region eu-west-1
aws ec2 enable-image-block-public-access --image-block-public-access-state block-new-sharing --region eu-west-1
```

Public snapshots and AMIs have exposed source code, credentials in config files and private keys. Scan AMIs for secrets before sharing them even privately.

## 376: What are Organizations declarative policies?

Declarative policies, added in late 2024, set a desired configuration for a service across accounts, and the service itself enforces it, even for new APIs and features. Unlike SCPs, they act on the service configuration, not on IAM permissions. Current uses include blocking public sharing of AMIs and snapshots, requiring IMDSv2 defaults, blocking VPC internet gateway access, and restricting which AMIs can be launched (allowed AMIs). You can also show a custom error message to users who hit them.

## 377: How do you protect DynamoDB tables from deletion and data loss?

- Turn on deletion protection on important tables
- Point-in-time recovery (PITR), with a recovery period you choose up to 35 days
- AWS Backup with Vault Lock and cross-account copies
- A resource policy or SCP that denies `dynamodb:DeleteTable` and `dynamodb:UpdateContinuousBackups` except for an admin role
- Least-privilege item-level access for apps, so a bug cannot run a mass `DeleteItem`

## 378: How does encryption work for cross-region RDS and Aurora replicas?

KMS keys are regional (unless multi-Region), so a cross-region read replica or snapshot copy needs a key in the destination region. You specify it when creating the replica or copying the snapshot. You cannot change the KMS key of an existing encrypted database in place: you copy a snapshot with the new key and restore. Plan keys per region early, especially for disaster recovery setups.

## 379: How do attackers try to avoid CloudTrail, and how do you detect it?

- `StopLogging`, `DeleteTrail` or `UpdateTrail` on trails
- `PutEventSelectors` to exclude events they want to hide
- Deleting or changing the S3 bucket, its policy, or the KMS key used for logs
- Working in regions they hope are not monitored
- Using APIs that are not logged or are only logged as data events

Defenses: organization trails that member accounts cannot change, SCPs denying trail changes, multi-region trails, logs in a separate locked account, GuardDuty findings like `Stealth:IAMUser/CloudTrailLoggingDisabled`, and alerts on any trail or event selector change.

## 380: What activity does CloudTrail not capture by default?

- Data events (S3 object access, Lambda invokes, DynamoDB item operations and many others) unless you turn them on
- Network activity (use VPC Flow Logs) and DNS queries (Resolver query logs)
- Activity inside the OS or the database (use OS logs, database audit logs)
- Application-level actions in your own code
- Some read-only or very high volume API calls that services exclude

Also, network activity events for VPC endpoints are a separate opt-in category, which show API calls through your endpoints, including denied calls from other accounts.

## 381: How would you design logging for a large AWS organization?

- Log Archive account holding CloudTrail, Config, VPC Flow Logs, DNS logs, WAF, ALB and CloudFront logs in locked S3 buckets with Object Lock or strict deny-delete policies
- Lifecycle rules: hot for 90 days, cheaper storage classes for one to seven years based on compliance
- Security Lake or a SIEM for search and correlation, fed from those buckets
- CloudWatch Logs only for what you alert on in near real time, with retention set
- Central KMS keys with decrypt limited to the security team
- Monitoring of the pipeline itself, so you notice when a log source stops

## 382: How do you test that your detections actually work?

Run safe attack simulations in a test account and check that alerts fire. Tools like Stratus Red Team (from Datadog) run single attack techniques mapped to MITRE ATT&CK, such as stopping CloudTrail, creating a backdoor IAM user or exfiltrating an EBS snapshot. GuardDuty also offers sample findings and a tester script. Track for each technique: was it detected, how fast, and did the right person get paged? Repeat after every change to the detection pipeline.

## 383: What should an AWS incident response plan include?

- Contacts and roles: who leads, who talks to legal and customers, how to reach AWS Support and the CIRT
- Pre-created IR roles in every account (read-only investigator, containment role), deployed by StackSets
- A forensics account with tools and permissions to copy snapshots
- Runbooks for common cases: leaked key, compromised instance, compromised role, public bucket, root account compromise, ransomware
- Pre-tested automation for containment
- Log sources and how to query them
- Regular game days to practice

## 384: How do you do forensics on a compromised EC2 instance?

1. Isolate with a forensic security group, keep it running.
2. Capture memory if possible (tools like LiME or AVML), through SSM or the console.
3. Take EBS snapshots of all volumes, tag them with case details, and share or copy them to the forensics account (re-encrypting with the forensics KMS key).
4. In the forensics account, create volumes from the snapshots and attach them read-only to an analysis instance with no internet access.
5. Collect instance metadata, CloudTrail events, VPC Flow Logs and GuardDuty findings for the instance.
6. Keep a chain of custody record: who did what, when, and hashes of the evidence.

## 385: How do you respond when an IAM role (not a user) is compromised?

1. Find out how the credentials were stolen (instance, Lambda, CI, a federated user) and close that path first.
2. Revoke existing sessions with the `aws:TokenIssueTime` deny policy.
3. If the role can be assumed by others, check and tighten the trust policy.
4. Review CloudTrail for everything the role sessions did, using the session name and source IP.
5. Remove any persistence created: new roles, users, keys, Lambda functions, EventBridge rules.
6. Reduce the role's permissions to what is needed.

## 386: How do you respond to a compromised Lambda function?

- Set reserved concurrency to 0 to stop it from running (this throttles all invocations)
- Revoke the execution role's sessions and check what it did in CloudTrail
- Download and save the current code and configuration for analysis (`get-function` gives a download link)
- Check for changed code, new layers, new environment variables or event source mappings, and who made those changes
- Look for the root cause, such as an injection bug or a compromised deploy pipeline
- Redeploy a clean, reviewed version with a narrower role

## 387: How do you respond to a compromised pod in EKS?

- Label it and apply a network policy that blocks all ingress and egress for it
- Cordon the node so no new pods are scheduled there
- Do not delete the pod right away. Capture its logs, a description, and if possible a memory and filesystem snapshot of the container
- Revoke its IAM role sessions (Pod Identity or IRSA) and rotate any secrets it could read
- Check GuardDuty Runtime Monitoring and EKS audit logs for what it did, including Kubernetes API calls with its service account
- Decide whether the node is also compromised. If yes, isolate and snapshot the node too.

## 388: What do you do if the root user of an account is compromised?

1. Try to sign in and reset the password and MFA. If you cannot, contact AWS Support right away.
2. Revoke and delete any root access keys.
3. Check the account's contact email and phone, and alternate contacts, since attackers change them.
4. Look for new IAM users, roles, identity providers, access keys and changes to billing.
5. For member accounts, remove root credentials using centralized root access, and use SCPs to block the account while you investigate (for example move it to a quarantine OU).
6. Find out how it happened, often a reused password or a compromised email account.

## 389: What do you do when an S3 bucket was found publicly exposed?

1. Make it private immediately: turn on Block Public Access, fix the bucket policy and ACLs.
2. Check what was in it with Macie or a quick inventory, and how sensitive it is.
3. Check access logs or CloudTrail data events (if they were on) to see who downloaded what. If logging was off, assume everything was accessed.
4. Check for writes too: did someone upload malware or change files served to users?
5. Involve legal and privacy teams about notification obligations.
6. Find why it happened and add preventive controls (account-level BPA, SCP, RCP, IaC checks).

## 390: What are the signs of a crypto-mining compromise and how do you respond?

Signs: sudden high EC2 or GPU usage, instances in regions you never use, GuardDuty `CryptoCurrency` findings, `RunInstances` calls from unknown IPs, service quota increase requests, or a billing alert. Response: find which credential launched the resources, disable it and revoke sessions, terminate the miners after snapshotting one for evidence, check every region for other resources (Lambda, ECS, SageMaker, Batch), remove persistence, and contact AWS Support about billing. Region-deny SCPs and budget alerts limit future damage.

## 391: What persistence techniques do attackers use in AWS accounts?

- New IAM users or extra access keys on existing users
- Changing role trust policies to trust their own account
- Adding an IAM identity provider (SAML or OIDC) they control
- Lambda functions triggered by EventBridge to recreate access if it gets removed
- Changes to IAM Identity Center users or permission sets
- EC2 user data or SSM documents that run their code
- Sharing AMIs, snapshots or KMS keys with their own account
- Resource policies (S3, SQS, Secrets Manager) granting their account access

Clean-up must check all of these, not just the first leaked key. Access Analyzer external access findings help find the cross-account ones.

## 392: How would you build an automated security response pipeline?

1. Security Hub (or EventBridge directly) receives findings from GuardDuty, Inspector, Macie and Security Hub CSPM.
2. EventBridge rules route findings by type and severity.
3. Step Functions workflows run the response: gather context, ask for approval in Slack if needed, then act through Lambda or SSM Automation (isolate instance, revoke sessions, block IP in WAF).
4. Every action is logged and the finding is updated with a note.
5. Tickets are created for follow-up.

Start with low-risk actions (notify, enrich, snapshot) and automate destructive ones only after they are well tested.

## 393: What are the risks of automatic remediation?

- A wrong rule can break production at scale, for example removing a security group rule a service needs
- Attackers can trigger remediation on purpose to cause outages
- Fights with IaC: the pipeline puts the change back, remediation removes it again
- The remediation role is powerful and becomes a target
- Teams stop fixing root causes because "automation handles it"

Guardrails: allow exceptions by tag, run in notify-only mode first, limit blast radius per run, require approval for destructive actions, and alert on every automatic change.

## 394: How should GuardDuty be set up across an organization?

- Delegate admin to the security tooling account
- Turn on auto-enable for all accounts (existing and new) and all regions, including regions you do not use, since attackers like those
- Enable protection plans based on risk: S3, EKS, Runtime Monitoring, Malware Protection, RDS, Lambda
- Export findings to an S3 bucket in the log archive account for long-term storage
- Send high-severity findings through EventBridge to the on-call tool
- Keep suppression rules few and reviewed

## 395: How do you manage findings across regions and accounts in Security Hub CSPM?

Use cross-region aggregation to link all regions to one home region, and the delegated admin account to see all member accounts. Central configuration policies decide which standards and controls apply per OU. Disable controls that do not apply (for example global resource checks in every region except one). Integrate with Jira or ServiceNow through the built-in integrations, and use automation rules to route findings to the right team by account or tag.

## 396: How does Inspector scan EC2 instances?

Two modes:

- Agent-based: uses the SSM Agent to collect software inventory. The instance must be an SSM managed instance.
- Agentless: Inspector takes EBS snapshots, scans them and deletes the snapshots. Useful for instances without SSM.

The hybrid scan mode uses agent-based where possible and agentless for the rest. Inspector also creates network reachability findings, showing ports that can be reached from the internet through the path of internet gateways, load balancers and security groups.

## 397: How do you control Macie costs at scale?

Macie charges per bucket monitored and per GB of data scanned. To control cost:

- Use automated sensitive data discovery, which samples objects instead of scanning everything
- Exclude buckets with known non-sensitive data (logs, build artifacts) from discovery
- Run full discovery jobs only on high-risk buckets, and use incremental scanning (only new objects since the last run)
- Skip file types that do not hold sensitive data, like images or compiled binaries
- Watch the usage page in the Macie console

## 398: Should you build a SIEM on Security Lake or buy one?

Security Lake gives you normalized data (OCSF) in your own S3 at storage prices, and you can query with Athena or OpenSearch. But it is not a full SIEM: correlation rules, case management and dashboards are up to you or a partner tool. A commercial SIEM gives detection content and workflows out of the box but can be expensive at cloud log volumes. Many teams keep all raw data in Security Lake and send a filtered subset to the SIEM.

## 399: How do you keep AWS Config costs reasonable?

Config charges per configuration item recorded and per rule evaluation. Busy resources like ENIs, security groups in large ECS clusters, or ephemeral instances can create many items. Options:

- Use periodic recording (daily) for noisy resource types and continuous recording for important ones
- Exclude resource types you do not need
- Record global resources (IAM) in only one region
- Remove duplicate rules that Security Hub CSPM already runs
- Use conformance packs carefully, since each rule in each account and region costs money

## 400: How do preventive, detective, proactive and responsive controls fit together?

- Preventive: stop the bad action from happening (SCPs, RCPs, permission boundaries, declarative policies, Block Public Access)
- Proactive: stop bad resources before deployment (IaC scanning, CloudFormation Hooks)
- Detective: notice when something wrong exists or happens (Config, Security Hub CSPM, GuardDuty, CloudTrail alerts)
- Responsive: fix it (EventBridge plus automation, incident runbooks)

Preventive controls are strongest but can block work if too strict. Use them for things that must never happen. Use detective and responsive controls for things that need judgment.

## 401: Should you patch servers in place or replace them?

In-place patching with Patch Manager works for long-lived servers, but servers slowly drift from each other and from what you tested. Immutable infrastructure builds a new patched AMI or container image (with EC2 Image Builder or CI), tests it, and replaces instances through a rolling or blue/green deploy. Replacement is easier to audit and roll back, and it also removes anything an attacker may have left on the old host. Most teams use immutable images for app servers and Patch Manager for the few servers that cannot be replaced easily.

## 402: When would you pick EC2 Instance Connect Endpoint over Session Manager?

Session Manager needs the SSM Agent and a path to Systems Manager (internet or VPC endpoints), and it works on instances without any inbound rules. EC2 Instance Connect Endpoint lets you open SSH or RDP to private instances without public IPs or a bastion, and without an agent, which helps for appliances or OSes where you cannot install SSM. Its access is controlled with IAM (`ec2-instance-connect:OpenTunnel`) and logged in CloudTrail, but the session contents are not recorded the way Session Manager can record them. For most fleets, Session Manager is the default.

## 403: What are the trade-offs of TLS inspection in Network Firewall?

With TLS inspection, the firewall decrypts traffic, inspects it with Suricata rules and re-encrypts it, using certificates from ACM. That catches threats hidden in HTTPS and allows rules on full URLs. Downsides: you must install your CA on every client for egress inspection, certificate pinning in some apps breaks, it adds latency and cost, and the firewall now sees sensitive data, which has privacy and compliance impact. Many teams inspect only some destinations and use SNI-based domain filtering for the rest.

## 404: How can DNS-over-HTTPS get around your DNS controls, and how do you handle it?

Apps or malware can send DNS queries over HTTPS to public resolvers like `1.1.1.1` or `8.8.8.8`, which skips the Route 53 Resolver and therefore DNS Firewall and query logs. To handle it, block outbound traffic to known DoH resolver IPs and domains in Network Firewall or security groups, restrict egress to an allow list of domains, and watch Flow Logs for port 443 traffic to public resolvers. Without egress control, DNS controls alone are easy to bypass.

## 405: What are the common pitfalls of ABAC on AWS?

- People who can change tags can change their access. Lock down `ec2:CreateTags`, `iam:TagRole`, `iam:TagUser` and similar with conditions on `aws:TagKeys`.
- Resources must get the right tag at creation. Use `aws:RequestTag` conditions on create actions, and tag-on-create.
- Not every action supports `aws:ResourceTag`. List and some create actions do not, so you need other statements for them.
- Tag values are case-sensitive, so `Prod` and `prod` are different.
- Debugging is harder, because the policy text alone does not tell you who can access what.

## 406: How do you scale ABAC with IAM Identity Center?

Map IdP attributes (like `team` or `costCenter`) to session tags with "attributes for access control". Write a small number of permission sets whose policies compare `aws:PrincipalTag/team` with `aws:ResourceTag/team`. Use SCPs or permissions boundaries to stop people from changing tags on resources and to require the `team` tag on create. When a new team appears in the IdP, it gets access to its own resources with no new permission sets. Keep audit simple by logging tag changes and running Config checks for untagged resources.

## 407: How do you use tags in an SCP to protect certain resources?

Tag resources managed by the platform or security team (for example `owner=platform`) and deny changes to them for everyone else.

```json
{
  "Sid": "ProtectPlatformResources",
  "Effect": "Deny",
  "Action": [
    "ec2:DeleteVpc",
    "ec2:DeleteSubnet",
    "ec2:ModifyVpcAttribute",
    "ec2:DeleteRoute",
    "ec2:CreateRoute",
    "ec2:DeleteTags",
    "ec2:CreateTags"
  ],
  "Resource": "*",
  "Condition": {
    "StringEquals": { "aws:ResourceTag/owner": "platform" },
    "ArnNotLike": { "aws:PrincipalArn": "arn:aws:iam::*:role/PlatformAdmin" }
  }
}
```

Including the tag actions matters: otherwise someone removes the tag first and then deletes the resource.

## 408: When should you use a resource-based policy instead of role assumption for cross-account access?

Resource-based policies:

- The caller keeps its own identity and permissions, which is handy when it needs to read from your bucket and write to its own at the same time
- CloudTrail shows the real caller from the other account
- Only works for services with resource policies

Role assumption:

- Works for any service
- You control the full permission set in your account
- The caller loses its own permissions while using the role

For KMS, S3, SQS, SNS and Secrets Manager, resource policies are common. For broad access, like a security scanner, roles are better.

## 409: A role in account B gets AccessDenied reading an SSE-KMS object in account A's bucket. How do you troubleshoot?

Check each layer in turn:

1. Role's IAM policy in B: allows `s3:GetObject` on the bucket ARN and `kms:Decrypt` on the full key ARN.
2. Bucket policy in A: allows the role (or account B) to get objects.
3. Key policy in A: allows the role or account B to `kms:Decrypt`.
4. Object ownership: if the bucket uses ACLs and another account wrote the object, A may not own it.
5. SCPs in B, RCPs in A, VPC endpoint policies on B's side, and permissions boundaries on the role.
6. Was the object encrypted with the AWS managed `aws/s3` key? That key cannot be used cross-account at all.

The error message often says which policy type denied the request, which narrows the search.

## 410: How do you read an AccessDenied error message on AWS?

Many services now include the reason in the message, for example:

```text
User: arn:aws:sts::111122223333:assumed-role/dev/alice is not authorized to perform:
s3:PutBucketPolicy on resource: arn:aws:s3:::logs with an explicit deny in a service control policy
```

The message tells you the principal, the action, the resource and the policy type (identity-based, resource-based, SCP, RCP, permissions boundary, session policy, VPC endpoint policy) and whether it was an explicit or implicit deny. For encoded EC2 errors, decode the message with `aws sts decode-authorization-message`, which needs the `sts:DecodeAuthorizationMessage` permission.

## 411: How do you apply the 3-2-1 backup rule on AWS for ransomware?

Three copies, on two different storage types or services, with one copy isolated:

- The production data itself
- AWS Backup in the same account and region for fast restores
- A copy in a separate backup account (and often another region) in a logically air-gapped vault or a vault with Vault Lock in compliance mode

The isolated copy must survive an attacker with admin rights in production, which means separate credentials, separate KMS keys and SCPs. Use AWS Backup restore testing to restore on a schedule and check the data works, because a backup you never restored is a guess.

## 412: What happens to IAM and IAM Identity Center if a region fails?

IAM's control plane (creating users, changing policies) runs in `us-east-1`, but authentication and authorization are served in every region, so existing roles keep working if `us-east-1` has problems. STS is available as regional endpoints. IAM Identity Center runs in one home region, and if that region is down, users cannot sign in through it, although existing sessions continue until they expire. Plan break-glass IAM access that does not depend on it.

## 413: Why should you use STS regional endpoints?

The global endpoint `sts.amazonaws.com` runs in `us-east-1` (though AWS now serves most global endpoint requests in the caller's region). Regional endpoints like `sts.eu-west-1.amazonaws.com` reduce latency, keep working if another region has problems, and let you use a VPC interface endpoint for STS. Tokens from regional endpoints work in all regions, including opt-in regions. Current SDKs and the CLI default to regional endpoints. Older configs may still set `sts_regional_endpoints = legacy`.

## 414: What do you need to run a HIPAA workload on AWS?

- Accept the Business Associate Addendum (BAA) in AWS Artifact for the accounts that hold PHI
- Store and process PHI only in HIPAA eligible services
- Encrypt PHI at rest and in transit
- Enable logging of access to PHI (CloudTrail, data events, database audit logs) and keep logs long enough
- Least-privilege access with MFA and regular access reviews
- Backups and a tested recovery plan
- Use the HIPAA Security Rule conformance pack and Audit Manager framework to track controls

AWS being eligible does not make your setup compliant. Your own policies and risk assessments are still required.

## 415: How do you meet data residency requirements on AWS?

- SCPs that deny actions outside approved regions, with exceptions only for global services
- Disable opt-in regions you do not use
- Single-region KMS keys, so data cannot be decrypted elsewhere
- Disable or restrict cross-region replication, backup copies and multi-Region keys unless approved
- Check where global services (CloudFront logs, IAM, Route 53) and support cases store data
- For strict sovereignty needs, look at KMS external key stores or AWS sovereign cloud offerings

Document data flows, because auditors will ask where backups and logs go.

## 416: What does "compliance as code" mean on AWS?

Compliance rules are written as code and run automatically instead of being checked by hand once a year. Examples: SCPs and RCPs for things that must never happen, CloudFormation Guard or OPA rules in CI, CloudFormation Hooks at deploy time, Config rules and conformance packs for continuous checks, and Audit Manager collecting the evidence. All of it lives in Git with reviews, so you can show an auditor when each control was added and that it has been running since.

## 417: Which IAM limits affect how you design policies?

- Managed policy size: 6,144 characters (whitespace not counted)
- Inline policies: 2,048 characters per user, 10,240 per role, 5,120 per group (total for all inline policies on that identity)
- Managed policies attached per role or user: 10 by default, up to 20 with a quota increase
- Role trust policy size: 2,048 by default, up to 4,096
- Session policy: 2,048 characters packed
- SCP: 5,120 characters, 5 per target

When you hit these, it is usually a sign to use wildcards carefully, split roles by job, or move to ABAC instead of listing many ARNs.

## 418: When do you use a permissions boundary, an SCP or a session policy?

- SCP: organization-wide or OU-wide rules that apply to every principal in the accounts, like "no one can disable CloudTrail". Managed by the central team.
- Permissions boundary: limits a specific user or role, mostly to safely delegate IAM role creation to developers or pipelines inside an account.
- Session policy: narrows one session at runtime, like a token vending machine giving each tenant access to only their prefix.

All three only limit permissions. None of them grant anything on their own.

## 419: How would you build a self-service AWS platform for dev teams with guardrails?

- Account vending through Control Tower Account Factory or AFT, with a baseline per account
- SCPs and RCPs per OU for hard rules
- Developers get a permission set with a permissions boundary that lets them create roles for their apps
- Templates or CDK constructs with secure defaults (encrypted buckets, private subnets, logging on)
- IaC scanning and CloudFormation Hooks for proactive checks
- Security Hub CSPM and Config for detection, with findings routed to the owning team
- Clear docs on how to request exceptions

The goal is that the secure path is also the easy path.

## 420: What are the tenant isolation models for SaaS on AWS?

- Silo: each tenant has its own resources, often its own account. Strongest isolation, highest cost and operations work.
- Pool: tenants share resources (tables, buckets, compute) and isolation comes from code and IAM policies with tenant context.
- Bridge: a mix, such as shared compute with a database per tenant, or premium tenants in silos.

In the pool model, enforce isolation with IAM where you can (dynamic session policies, `dynamodb:LeadingKeys`, S3 prefixes, KMS encryption context per tenant), not only with `WHERE tenant_id = ?` in code.

## 421: What is the token vending machine pattern?

A component that gives each request credentials scoped to one tenant. It assumes a shared role with a session policy (or session tags) built for the current tenant, then hands the temporary credentials to the code handling that request.

```python
import json
import boto3

sts = boto3.client("sts")

def credentials_for_tenant(tenant_id: str) -> dict:
    policy = {
        "Version": "2012-10-17",
        "Statement": [{
            "Effect": "Allow",
            "Action": ["dynamodb:GetItem", "dynamodb:Query", "dynamodb:PutItem"],
            "Resource": "arn:aws:dynamodb:eu-west-1:111122223333:table/Orders",
            "Condition": {
                "ForAllValues:StringEquals": {"dynamodb:LeadingKeys": [tenant_id]}
            },
        }],
    }
    resp = sts.assume_role(
        RoleArn="arn:aws:iam::111122223333:role/TenantDataAccess",
        RoleSessionName=f"tenant-{tenant_id}",
        Policy=json.dumps(policy),
        DurationSeconds=900,
    )
    return resp["Credentials"]
```

Even if code forgets a tenant filter, AWS blocks access to other tenants' items. The `tenant_id` must come from the verified token, not the request.

## 422: How would you secure a serverless app made of API Gateway, Lambda and DynamoDB?

- CloudFront and WAF in front of the API, with rate limits
- Cognito or another OIDC provider with a JWT or Cognito authorizer on every route
- Request validation in API Gateway and input validation in code
- One execution role per function with only the table actions it uses, ideally with `dynamodb:LeadingKeys`
- Secrets in Secrets Manager with caching
- Customer managed KMS key for DynamoDB if you need control over decryption, PITR and deletion protection on
- Reserved concurrency and throttling to limit cost attacks
- Structured logs without sensitive data, X-Ray tracing, alarms on 4xx/5xx spikes
- Code signing, dependency scanning and Inspector Lambda scanning in CI

## 423: How would you secure a public static website with a backend API?

- S3 bucket fully private, served by CloudFront with OAC
- ACM certificate, HTTPS only, TLS 1.2+, HSTS and a strict CSP via response headers policy
- WAF on the distribution with managed rules and rate limits
- The API on a separate path or domain, behind the same CloudFront, with its own auth
- CORS on the API limited to your site origin
- Deploy the site from CI with OIDC and a role that can only write to that bucket and create invalidations
- Logging for CloudFront and WAF, and alerts on unusual traffic

## 424: What does zero trust mean on AWS in practice?

Do not trust a request just because it comes from inside your network. Authenticate and authorize every call, based on identity and context. On AWS that means:

- Every AWS API call is already signed and authorized by IAM, which is the base
- Service-to-service calls use IAM auth (SigV4), mTLS or VPC Lattice with auth policies, not "anything in the VPC is fine"
- Internal apps use Verified Access instead of a VPN
- Short-lived credentials everywhere
- Network controls still exist, but as an extra layer, not the main one

## 425: What is wrong with a trust policy that allows "AWS": "*" and how is it exploited?

```json
{
  "Effect": "Allow",
  "Principal": { "AWS": "*" },
  "Action": "sts:AssumeRole"
}
```

Any AWS principal in any account can assume this role. Attackers scan for such roles by guessing common names (like `deploy`, `ci-role`, `OrganizationAccountAccessRole` variants) in known account IDs. If the trust policy has no conditions such as `aws:PrincipalOrgID` or `sts:ExternalId`, they get in. Access Analyzer reports these as external access findings, and an RCP on `sts:AssumeRole` with `aws:PrincipalOrgID` blocks it organization-wide.

## 426: Why are open SNS topic and SQS queue policies dangerous?

A queue policy with `"Principal": "*"` and `sqs:SendMessage` (without a `aws:SourceArn` condition) lets anyone push messages into your processing pipeline, which can trigger expensive work or inject bad data. With `sqs:ReceiveMessage`, anyone can read your messages. An open SNS topic lets anyone subscribe their own endpoint and receive every message, or publish fake notifications. Always restrict principals to your accounts, your organization or specific source ARNs.

## 427: How can a misconfigured Cognito user pool lead to privilege escalation?

If an app stores roles or tenant IDs in custom attributes (like `custom:role` or `custom:tenant_id`) and the app client allows users to write those attributes, a user can call `UpdateUserAttributes` with their own access token and set `custom:role=admin`. Your backend then trusts the claim in the next token. Fix it by making such attributes read-only for the app client (remove them from writable attributes), setting them only from the backend with admin APIs, and preferring Cognito groups for roles.

## 428: What API security mistakes do you often see in AWS reviews?

- API Gateway routes with no authorizer, often added later for "testing"
- The default `execute-api` endpoint left on when a custom domain with mTLS or WAF is used, so clients can skip the controls
- Old stages (`dev`, `test`) still deployed and public
- Function URLs with auth type `NONE`
- Lambda authorizers that fail open on errors
- CORS set to `*` with credentials
- Detailed error messages and stack traces returned to clients

## 429: Walk through a typical "leaked key on GitHub" breach.

1. A developer commits an `.env` file or test script with an IAM user's access key to a public repo.
2. Automated scanners run by attackers find it within minutes, often before AWS's own scan does anything.
3. The attacker calls `GetCallerIdentity`, lists permissions, then launches large GPU instances in many regions for crypto mining, or copies S3 data.
4. They may create a new IAM user or keys for persistence.
5. The owner notices days later through a large bill or AWS's quarantine email.

Lessons: no IAM user keys for development, pre-commit secret scanning (git-secrets, gitleaks) and GitHub push protection, region-deny SCPs, budget alerts and GuardDuty.

## 430: What did the CircleCI breach in early 2023 teach about CI/CD and AWS?

Attackers stole a CircleCI engineer's session token through malware on their laptop, got into CircleCI's systems and accessed customer secrets, including AWS access keys stored as environment variables. CircleCI told all customers to rotate every secret. Teams that used OIDC federation to AWS had no AWS keys to rotate, while teams with stored keys had a long and painful rotation. The lesson: a CI provider is a third party holding your secrets, so avoid storing long-lived AWS credentials there.

## 431: How have exposed .env files led to AWS account compromises?

In a widely reported 2024 extortion campaign, attackers scanned millions of domains for publicly reachable `.env` files on misconfigured web servers. Many contained AWS access keys. With those keys they enumerated IAM, created new roles for persistence, found S3 buckets, copied the data out, deleted it and left ransom notes. Defenses: never keep secrets in files served by web servers, block dotfiles at the web server or CloudFront level, use roles instead of keys, and restrict S3 deletes with versioning and Object Lock.

## 432: How could an SSRF bug in an EKS pod lead to an AWS account compromise?

The app in a pod has an SSRF bug. If pods can reach IMDS (hop limit 2 and no network policy blocking it), the attacker fetches the node role's credentials, which often include broad EC2 and ECR permissions. From there they might read images, describe the network, or with a badly scoped node role, do much more. Mitigations: block pods from IMDS, use Pod Identity or IRSA for app permissions, keep the node role minimal, validate outbound URLs in the app, and watch GuardDuty for instance credentials used outside the instance.

## 433: How can attackers abuse AWS credentials cached on developer laptops?

The CLI caches SSO tokens in `~/.aws/sso/cache` and role credentials in `~/.aws/cli/cache`, and some people still keep IAM user keys in `~/.aws/credentials`. Malware like info-stealers copies these files and uses them until they expire. Mitigations: no long-lived keys on laptops, short Identity Center session lengths for privileged permission sets, device posture checks at the IdP, endpoint protection, re-authentication with MFA for elevated access, and alerts on sessions used from new IPs or countries.

## 434: Which open-source tools are used to test AWS security?

- Prowler: security posture checks against CIS, FSBP, HIPAA and other frameworks
- ScoutSuite: multi-cloud configuration review
- CloudFox: finds attack paths and exploitable access from a given set of credentials
- Pacu: an AWS exploitation framework for authorized pen tests
- PMapper: IAM privilege escalation graph
- Stratus Red Team: runs individual attack techniques to test detections
- Steampipe and Powerpipe: query AWS with SQL and run compliance benchmarks

Only use offensive tools on accounts you own or are authorized to test, and within AWS's pen testing policy.

## 435: How does Prowler compare with Security Hub CSPM?

Security Hub CSPM is a managed AWS service: always on, continuous, integrated with Config and EventBridge, and billed per check. Prowler is open source and runs on demand or on a schedule. It has many checks beyond AWS's standards, supports other clouds, and is easy to run in CI or for a one-time audit. Many teams use Security Hub CSPM for continuous posture management and run Prowler for deeper audits or extra frameworks. Prowler can also send its findings to Security Hub.

## 436: You join a company with a weak AWS setup. What do you fix first?

First weeks:

- Root MFA everywhere, remove root keys
- Turn on CloudTrail organization trail, GuardDuty and Security Hub CSPM in all accounts and regions
- Account-level S3 Block Public Access
- Find and rotate or remove old IAM user access keys, and check for leaked ones
- Review security groups open to the internet

Next months:

- Move people to IAM Identity Center with the corporate IdP
- Move CI to OIDC
- Set up a Log Archive account and basic SCPs
- Fix critical findings, start Access Analyzer reviews

Later: data perimeter, ABAC, automated remediation and full landing zone work. Fix the things attackers use most often first.

## 437: How do you measure an AWS security program?

Useful metrics:

- Percentage of accounts with the security baseline (CloudTrail, GuardDuty, Config, Security Hub CSPM)
- Number of IAM users and active long-lived access keys, trending to zero
- Critical and high findings open, and mean time to fix them
- Mean time to detect and respond in incidents and game days
- Security Hub CSPM score per account and OU
- Percentage of workloads deployed only through pipelines
- Critical vulnerabilities in running images past their fix deadline

Pick a few, report them regularly, and tie them to owners.

## 438: How do you secure apps built with Amazon Bedrock?

- Use IAM to limit which roles can invoke which models (`bedrock:InvokeModel` on specific model ARNs), and use SCPs to block unapproved models
- Use VPC interface endpoints for Bedrock so traffic stays private
- Bedrock does not use your prompts or outputs to train base models and does not share them with model providers. Encrypt custom models and knowledge bases with your KMS keys.
- Use Bedrock Guardrails to filter harmful content, block denied topics, redact PII and detect prompt attacks
- Treat model output as untrusted input. Agents and tools that call APIs need least-privilege roles, and dangerous actions need confirmation.
- Turn on model invocation logging to S3 or CloudWatch, and protect those logs because they contain prompts

## 439: What can an attacker do with the Organizations management account, and how do you limit the risk?

From the management account they can change or detach SCPs and RCPs, create accounts, use `sts:AssumeRoot` or `OrganizationAccountAccessRole` to get into member accounts, change Identity Center assignments and remove accounts from the organization. In practice it is full control over everything. Limit the risk by keeping almost nobody there, using phishing-resistant MFA, delegating services to other accounts, removing or restricting `OrganizationAccountAccessRole` in member accounts, alerting on every sign-in and Organizations change, and keeping logs in a Log Archive account it does not control day to day.

## 440: Why is NotPrincipal with Deny risky?

`"Effect": "Deny"` with `NotPrincipal` denies everyone except the listed principals. It is easy to get wrong:

- For a role, you must list both the role ARN and the assumed-role session ARN, or the role's sessions are denied
- You often need to list the account root too
- Mistakes can lock everyone, including admins, out of a bucket

AWS recommends using `"Principal": "*"` with a condition on `aws:PrincipalArn` instead:

```json
{
  "Effect": "Deny",
  "Principal": "*",
  "Action": "s3:*",
  "Resource": ["arn:aws:s3:::payroll", "arn:aws:s3:::payroll/*"],
  "Condition": {
    "ArnNotEquals": {
      "aws:PrincipalArn": "arn:aws:iam::111122223333:role/PayrollApp"
    }
  }
}
```

## 441: A decrypt call fails even though the key policy and IAM policy allow it. What could it be?

- The encryption context passed on decrypt does not match the one used on encrypt
- A key policy or grant condition requires a specific encryption context or `kms:ViaService` that the call does not meet
- The key is disabled, pending deletion, or the ciphertext was made with a different key (common after a restore or copy)
- The request comes through a VPC endpoint whose endpoint policy does not allow KMS
- An SCP or RCP denies it
- The caller is in a different region and the key is single-region

KMS returns `InvalidCiphertextException` for context or key mismatches, which looks like data corruption but usually is not.

## 442: How can you lock yourself out of an S3 bucket, and how do you recover?

A bucket policy with `"Effect": "Deny"`, `"Principal": "*"` and `"Action": "s3:*"` and a condition that nobody meets (like the wrong VPC endpoint ID) denies everyone in the account, including admins. Only the root user can then delete the bucket policy. With centralized root access in Organizations, you can use `sts:AssumeRoot` with the `S3UnlockBucketPolicy` task policy from the management account instead of signing in as root. Always exclude a break-glass role in deny statements and test bucket policies in a non-production bucket first.

## 443: Why use aws:PrincipalArn instead of aws:userid or a role ARN in Principal for exceptions?

When you put a role ARN in `Principal`, IAM converts it to the role's unique ID. If the role is deleted and recreated, the policy breaks. When you use `aws:PrincipalArn` in a condition, it matches by ARN, so a recreated role still matches, which is convenient but also means anyone who can create a role with that name gets the exception. For exceptions in SCPs and deny statements, `aws:PrincipalArn` is the standard choice, and you protect it by denying creation of roles with those names except by the platform team.

## 444: What problems does IAM eventual consistency cause in automation?

IAM changes are replicated globally and can take a few seconds to apply everywhere. If a script creates a role and immediately passes it to Lambda or tries to assume it, the call can fail with "role cannot be assumed" or `AccessDenied`. Also, when you remove a permission, it may still work for a short time. Build in retries with backoff, avoid creating IAM resources in the same hot path as using them, and do not rely on instant revocation during incident response.

## 445: How do you give temporary elevated access on AWS?

Instead of giving people standing admin access, let them request it for a short time with approval. Options:

- IAM Identity Center with a just-in-time access tool, like the AWS open-source TEAM solution (Temporary Elevated Access Management) or commercial tools
- An approval workflow that adds the user to an IdP group for a few hours, synced through SCIM
- A pipeline that assumes the elevated role on the user's behalf for specific tasks

Every elevation should record the reason, the approver and the session activity in CloudTrail.

## 446: Can an SCP stop your account from sharing data with outside principals?

Not fully. SCPs limit what principals in your accounts can do, so they can block `s3:PutBucketPolicy` calls, but once a bucket policy grants access to an external account, the external principal's requests are not checked against your SCPs. RCPs fill this gap, because they apply to requests made to your resources by anyone. A strong setup uses SCPs to stop people from creating bad shares, RCPs to block external access even if a share exists, and Access Analyzer to find what was shared.

## 447: How would you detect and respond to a compromised identity provider?

If your IdP (Okta, Entra ID) is compromised, an attacker can sign in as anyone or add themselves to admin groups, and SCIM will sync that to IAM Identity Center. Detection: alert on new admin group memberships, new permission set assignments, sign-ins from unusual locations, and `CreateSAMLProvider` or `UpdateSAMLProvider` events. Response: switch to break-glass IAM access, disable the external IdP connection or affected users in Identity Center, revoke sessions with the `aws:TokenIssueTime` deny, and review all IAM and Identity Center changes since the compromise started.

## 448: What do you look for when reviewing a pull request that changes IAM?

- New wildcards in `Action` or `Resource`, especially `iam:*`, `sts:AssumeRole` on `*`, `iam:PassRole` on `*`
- New trust relationships, especially to other accounts, `"AWS": "*"` or OIDC providers without `sub` conditions
- Removed conditions like `aws:SourceArn`, `aws:PrincipalOrgID`, MFA or ExternalId
- Resource policies that become public or cross-account
- Permissions boundaries removed or weakened
- Privilege escalation combinations (PassRole plus create compute)
- Whether the change matches the stated purpose, or adds "just in case" permissions

Automate most of this with Access Analyzer checks in CI, and keep human review for trust and resource policies.

## 449: What is the shared responsibility model for managed AI and serverless services?

The line moves further toward AWS, but the customer side never disappears. For Lambda or Bedrock, AWS secures the infrastructure, runtime and model hosting. You still own IAM permissions, data you send in, how outputs are used, secrets, logging, input validation and the application logic around it. For AI specifically, you also own prompt injection defenses, guardrail configuration and deciding which actions an agent may take. Many serverless incidents are not runtime bugs but over-broad roles and missing auth.

## 450: How would you design security for a brand-new AWS organization from scratch?

1. Set up Organizations with Control Tower: Security OU (Log Archive, Audit), Infrastructure, Workloads (Prod, Non-Prod), Sandbox, Suspended, Policy Staging.
2. Turn on centralized root access, so member accounts have no root credentials.
3. Connect IAM Identity Center to the corporate IdP with SCIM, create a small set of permission sets, and plan break-glass access.
4. Organization trail, Config, GuardDuty, Security Hub and Security Hub CSPM, Inspector, Macie and Access Analyzer, all delegated to the Audit account.
5. SCPs for basics: region restriction, protect security tooling, deny leaving the organization, deny root actions. RCPs and declarative policies for the data perimeter, IMDSv2 and public sharing blocks.
6. Networking with private subnets, VPC endpoints, central egress inspection and DNS Firewall.
7. KMS keys per account and data class, encryption by default for EBS and S3.
8. CI/CD with OIDC, least-privilege deploy roles, IaC scanning and CloudFormation Hooks.
9. AWS Backup with backup policies, a separate backup account and Vault Lock.
10. EventBridge-based alerting, incident response runbooks, IR roles and a forensics account, and regular game days.

Then review it against the Well-Architected Security Pillar and keep improving.
