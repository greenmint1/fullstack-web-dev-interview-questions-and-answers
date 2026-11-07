# Google Cloud (GCP) Interview Questions and Answers

_Last updated: October 29, 2026_

450 Google Cloud interview questions with answers, split into three levels: 150 easy, 150 moderate and 150 advanced.

The answers reflect Google Cloud as of late 2026: Cloud Run (services, jobs, functions and worker pools), GKE Autopilot, Artifact Registry, Workload Identity Federation, Cloud SQL Enterprise Plus, Firestore, BigQuery editions and Gemini Enterprise Agent Platform (formerly Vertex AI). Code examples use the gcloud CLI, Terraform and the Node.js client libraries (`@google-cloud/storage`, `@google-cloud/pubsub` and so on). Older services such as Container Registry, Deployment Manager and Cloud Functions 1st gen are mentioned where you will still meet them in real projects.

## Table of Contents

- [Easy Questions (1-150)](#easy-questions-1-150)
- [Moderate Questions (151-300)](#moderate-questions-151-300)
- [Advanced Questions (301-450)](#advanced-questions-301-450)

### Easy Questions (1-150)

- [1: What is Google Cloud?](#1-what-is-google-cloud)
- [2: What is the difference between Google Cloud, GCP and Google Workspace?](#2-what-is-the-difference-between-google-cloud-gcp-and-google-workspace)
- [3: What are regions and zones?](#3-what-are-regions-and-zones)
- [4: What are multi-region and dual-region locations?](#4-what-are-multi-region-and-dual-region-locations)
- [5: What is the Google Cloud resource hierarchy?](#5-what-is-the-google-cloud-resource-hierarchy)
- [6: What is a project in Google Cloud?](#6-what-is-a-project-in-google-cloud)
- [7: What are folders used for?](#7-what-are-folders-used-for)
- [8: What is the organization resource?](#8-what-is-the-organization-resource)
- [9: What is a billing account?](#9-what-is-a-billing-account)
- [10: How do budgets and budget alerts work?](#10-how-do-budgets-and-budget-alerts-work)
- [11: What are labels?](#11-what-are-labels)
- [12: What is the difference between labels, tags and network tags?](#12-what-is-the-difference-between-labels-tags-and-network-tags)
- [13: What is the Google Cloud console?](#13-what-is-the-google-cloud-console)
- [14: What is the gcloud CLI?](#14-what-is-the-gcloud-cli)
- [15: What are gcloud configurations?](#15-what-are-gcloud-configurations)
- [16: What is Cloud Shell?](#16-what-is-cloud-shell)
- [17: Why do you need to enable APIs in a project?](#17-why-do-you-need-to-enable-apis-in-a-project)
- [18: What are quotas?](#18-what-are-quotas)
- [19: What service models does Google Cloud offer?](#19-what-service-models-does-google-cloud-offer)
- [20: What is the Google Cloud free tier?](#20-what-is-the-google-cloud-free-tier)
- [21: How does Google Cloud pricing generally work?](#21-how-does-google-cloud-pricing-generally-work)
- [22: What is IAM in Google Cloud?](#22-what-is-iam-in-google-cloud)
- [23: What types of principals exist in Google Cloud IAM?](#23-what-types-of-principals-exist-in-google-cloud-iam)
- [24: What are the types of IAM roles?](#24-what-are-the-types-of-iam-roles)
- [25: Why should you avoid basic roles?](#25-why-should-you-avoid-basic-roles)
- [26: What is an IAM allow policy?](#26-what-is-an-iam-allow-policy)
- [27: What is a service account?](#27-what-is-a-service-account)
- [28: Why should you avoid service account keys?](#28-why-should-you-avoid-service-account-keys)
- [29: What are default service accounts?](#29-what-are-default-service-accounts)
- [30: What are Application Default Credentials (ADC)?](#30-what-are-application-default-credentials-adc)
- [31: What is the difference between gcloud auth login and gcloud auth application-default login?](#31-what-is-the-difference-between-gcloud-auth-login-and-gcloud-auth-application-default-login)
- [32: Why grant roles to groups instead of individual users?](#32-why-grant-roles-to-groups-instead-of-individual-users)
- [33: What compute options does Google Cloud offer?](#33-what-compute-options-does-google-cloud-offer)
- [34: What is Compute Engine?](#34-what-is-compute-engine)
- [35: What machine families are there in Compute Engine?](#35-what-machine-families-are-there-in-compute-engine)
- [36: What are Spot VMs?](#36-what-are-spot-vms)
- [37: What disk options does Compute Engine have?](#37-what-disk-options-does-compute-engine-have)
- [38: What is the difference between images and snapshots?](#38-what-is-the-difference-between-images-and-snapshots)
- [39: What are startup scripts and metadata?](#39-what-are-startup-scripts-and-metadata)
- [40: How do you SSH into a Compute Engine VM?](#40-how-do-you-ssh-into-a-compute-engine-vm)
- [41: What are sustained use discounts and committed use discounts?](#41-what-are-sustained-use-discounts-and-committed-use-discounts)
- [42: What are instance templates and managed instance groups?](#42-what-are-instance-templates-and-managed-instance-groups)
- [43: What is App Engine and what is the difference between standard and flexible?](#43-what-is-app-engine-and-what-is-the-difference-between-standard-and-flexible)
- [44: What is Cloud Run?](#44-what-is-cloud-run)
- [45: How do you deploy an app to Cloud Run?](#45-how-do-you-deploy-an-app-to-cloud-run)
- [46: What is the difference between a Cloud Run service and a Cloud Run job?](#46-what-is-the-difference-between-a-cloud-run-service-and-a-cloud-run-job)
- [47: What are Cloud Run functions?](#47-what-are-cloud-run-functions)
- [48: What triggers can start a Cloud Run function?](#48-what-triggers-can-start-a-cloud-run-function)
- [49: How do you write and deploy an HTTP function in Node.js?](#49-how-do-you-write-and-deploy-an-http-function-in-nodejs)
- [50: What is the Functions Framework?](#50-what-is-the-functions-framework)
- [51: What is GKE?](#51-what-is-gke)
- [52: What is the difference between GKE Autopilot and GKE Standard?](#52-what-is-the-difference-between-gke-autopilot-and-gke-standard)
- [53: What is Artifact Registry?](#53-what-is-artifact-registry)
- [54: What happened to Container Registry?](#54-what-happened-to-container-registry)
- [55: What is Cloud Build?](#55-what-is-cloud-build)
- [56: What does a basic cloudbuild.yaml look like?](#56-what-does-a-basic-cloudbuildyaml-look-like)
- [57: What is Cloud Storage?](#57-what-is-cloud-storage)
- [58: What are buckets and objects in Cloud Storage?](#58-what-are-buckets-and-objects-in-cloud-storage)
- [59: What storage classes does Cloud Storage have?](#59-what-storage-classes-does-cloud-storage-have)
- [60: What location types can a Cloud Storage bucket have?](#60-what-location-types-can-a-cloud-storage-bucket-have)
- [61: How do you copy files to and from Cloud Storage from the command line?](#61-how-do-you-copy-files-to-and-from-cloud-storage-from-the-command-line)
- [62: What is object versioning in Cloud Storage?](#62-what-is-object-versioning-in-cloud-storage)
- [63: What are lifecycle rules in Cloud Storage?](#63-what-are-lifecycle-rules-in-cloud-storage)
- [64: What is uniform bucket-level access?](#64-what-is-uniform-bucket-level-access)
- [65: What is public access prevention?](#65-what-is-public-access-prevention)
- [66: What is a signed URL?](#66-what-is-a-signed-url)
- [67: How do you host a static website on Cloud Storage?](#67-how-do-you-host-a-static-website-on-cloud-storage)
- [68: What is soft delete in Cloud Storage?](#68-what-is-soft-delete-in-cloud-storage)
- [69: What database options does Google Cloud offer?](#69-what-database-options-does-google-cloud-offer)
- [70: What is Cloud SQL?](#70-what-is-cloud-sql)
- [71: How do you connect to Cloud SQL from an application?](#71-how-do-you-connect-to-cloud-sql-from-an-application)
- [72: How do backups work in Cloud SQL?](#72-how-do-backups-work-in-cloud-sql)
- [73: What does high availability mean in Cloud SQL?](#73-what-does-high-availability-mean-in-cloud-sql)
- [74: What are Cloud SQL read replicas?](#74-what-are-cloud-sql-read-replicas)
- [75: What is Firestore?](#75-what-is-firestore)
- [76: What is the difference between Firestore Native mode and Datastore mode?](#76-what-is-the-difference-between-firestore-native-mode-and-datastore-mode)
- [77: What is the Firestore data model?](#77-what-is-the-firestore-data-model)
- [78: How do you read and write Firestore data from Node.js?](#78-how-do-you-read-and-write-firestore-data-from-nodejs)
- [79: What is Bigtable?](#79-what-is-bigtable)
- [80: What is Spanner?](#80-what-is-spanner)
- [81: What is AlloyDB?](#81-what-is-alloydb)
- [82: What is Memorystore?](#82-what-is-memorystore)
- [83: What is BigQuery?](#83-what-is-bigquery)
- [84: How is data organized in BigQuery?](#84-how-is-data-organized-in-bigquery)
- [85: How do you run a BigQuery query from Node.js?](#85-how-do-you-run-a-bigquery-query-from-nodejs)
- [86: What is Pub/Sub?](#86-what-is-pubsub)
- [87: What is the difference between a topic and a subscription?](#87-what-is-the-difference-between-a-topic-and-a-subscription)
- [88: What is the difference between push and pull subscriptions?](#88-what-is-the-difference-between-push-and-pull-subscriptions)
- [89: How do you publish and receive Pub/Sub messages in Node.js?](#89-how-do-you-publish-and-receive-pubsub-messages-in-nodejs)
- [90: What is the acknowledgement deadline in Pub/Sub?](#90-what-is-the-acknowledgement-deadline-in-pubsub)
- [91: What is Cloud Tasks?](#91-what-is-cloud-tasks)
- [92: What is Cloud Scheduler?](#92-what-is-cloud-scheduler)
- [93: What is Eventarc?](#93-what-is-eventarc)
- [94: What is Workflows?](#94-what-is-workflows)
- [95: What is a VPC network in Google Cloud?](#95-what-is-a-vpc-network-in-google-cloud)
- [96: What are subnets in Google Cloud?](#96-what-are-subnets-in-google-cloud)
- [97: What is the difference between auto mode and custom mode VPCs?](#97-what-is-the-difference-between-auto-mode-and-custom-mode-vpcs)
- [98: How do firewall rules work in a Google Cloud VPC?](#98-how-do-firewall-rules-work-in-a-google-cloud-vpc)
- [99: What is the difference between internal and external IP addresses?](#99-what-is-the-difference-between-internal-and-external-ip-addresses)
- [100: What is Cloud NAT?](#100-what-is-cloud-nat)
- [101: What is Private Google Access?](#101-what-is-private-google-access)
- [102: What load balancers does Google Cloud offer?](#102-what-load-balancers-does-google-cloud-offer)
- [103: What is Cloud CDN?](#103-what-is-cloud-cdn)
- [104: What is Cloud DNS?](#104-what-is-cloud-dns)
- [105: What is Cloud Armor?](#105-what-is-cloud-armor)
- [106: What is Identity-Aware Proxy (IAP)?](#106-what-is-identity-aware-proxy-iap)
- [107: What is Secret Manager?](#107-what-is-secret-manager)
- [108: What is Cloud KMS?](#108-what-is-cloud-kms)
- [109: Is data encrypted at rest in Google Cloud by default?](#109-is-data-encrypted-at-rest-in-google-cloud-by-default)
- [110: What is Cloud Logging?](#110-what-is-cloud-logging)
- [111: How do you search logs in Logs Explorer?](#111-how-do-you-search-logs-in-logs-explorer)
- [112: What is Cloud Monitoring?](#112-what-is-cloud-monitoring)
- [113: What are uptime checks?](#113-what-are-uptime-checks)
- [114: What is an alerting policy in Cloud Monitoring?](#114-what-is-an-alerting-policy-in-cloud-monitoring)
- [115: What is Cloud Trace?](#115-what-is-cloud-trace)
- [116: What is Error Reporting?](#116-what-is-error-reporting)
- [117: What are Cloud Audit Logs?](#117-what-are-cloud-audit-logs)
- [118: What is Google Cloud Observability?](#118-what-is-google-cloud-observability)
- [119: How do you use Terraform with Google Cloud?](#119-how-do-you-use-terraform-with-google-cloud)
- [120: What are Infrastructure Manager and Deployment Manager?](#120-what-are-infrastructure-manager-and-deployment-manager)
- [121: What is Cloud Deploy?](#121-what-is-cloud-deploy)
- [122: What is the relationship between Firebase and Google Cloud?](#122-what-is-the-relationship-between-firebase-and-google-cloud)
- [123: What are Firebase Hosting and Firebase App Hosting?](#123-what-are-firebase-hosting-and-firebase-app-hosting)
- [124: What is the difference between API Gateway, Apigee and Cloud Endpoints?](#124-what-is-the-difference-between-api-gateway-apigee-and-cloud-endpoints)
- [125: What is Google Cloud Marketplace?](#125-what-is-google-cloud-marketplace)
- [126: What client libraries does Google Cloud offer?](#126-what-client-libraries-does-google-cloud-offer)
- [127: How do you test against Google Cloud services locally?](#127-how-do-you-test-against-google-cloud-services-locally)
- [128: What is an SLA in Google Cloud?](#128-what-is-an-sla-in-google-cloud)
- [129: What is the shared responsibility model?](#129-what-is-the-shared-responsibility-model)
- [130: What is Cloud Asset Inventory?](#130-what-is-cloud-asset-inventory)
- [131: What is Active Assist and the Recommender?](#131-what-is-active-assist-and-the-recommender)
- [132: What is Security Command Center?](#132-what-is-security-command-center)
- [133: What are organization policies?](#133-what-are-organization-policies)
- [134: What is Dataflow?](#134-what-is-dataflow)
- [135: What is Dataproc?](#135-what-is-dataproc)
- [136: What is Cloud Composer?](#136-what-is-cloud-composer)
- [137: What is Gemini Enterprise Agent Platform (formerly Vertex AI)?](#137-what-is-gemini-enterprise-agent-platform-formerly-vertex-ai)
- [138: What is the difference between calling Gemini through Google AI Studio and through Google Cloud?](#138-what-is-the-difference-between-calling-gemini-through-google-ai-studio-and-through-google-cloud)
- [139: What are Gemini Code Assist and Gemini Cloud Assist?](#139-what-are-gemini-code-assist-and-gemini-cloud-assist)
- [140: How do you use a custom domain with Cloud Run?](#140-how-do-you-use-a-custom-domain-with-cloud-run)
- [141: How do you set environment variables on a Cloud Run service?](#141-how-do-you-set-environment-variables-on-a-cloud-run-service)
- [142: What is the PORT environment variable in Cloud Run?](#142-what-is-the-port-environment-variable-in-cloud-run)
- [143: What does "scale to zero" mean in Cloud Run?](#143-what-does-scale-to-zero-mean-in-cloud-run)
- [144: How do you get TLS certificates for your domains on Google Cloud?](#144-how-do-you-get-tls-certificates-for-your-domains-on-google-cloud)
- [145: How do common Google Cloud services map to AWS?](#145-how-do-common-google-cloud-services-map-to-aws)
- [146: What are the Premium and Standard network tiers?](#146-what-are-the-premium-and-standard-network-tiers)
- [147: How can you connect an on-premises network to Google Cloud?](#147-how-can-you-connect-an-on-premises-network-to-google-cloud)
- [148: How do you move large amounts of data into Google Cloud?](#148-how-do-you-move-large-amounts-of-data-into-google-cloud)
- [149: How is Cloud Run billed?](#149-how-is-cloud-run-billed)
- [150: How do you shut down a project and what happens?](#150-how-do-you-shut-down-a-project-and-what-happens)

### Moderate Questions (151-300)

- [151: How would you set up projects and folders for a company with dev, staging and prod?](#151-how-would-you-set-up-projects-and-folders-for-a-company-with-dev-staging-and-prod)
- [152: How does IAM policy inheritance work?](#152-how-does-iam-policy-inheritance-work)
- [153: When should you create a custom IAM role?](#153-when-should-you-create-a-custom-iam-role)
- [154: What are IAM Conditions?](#154-what-are-iam-conditions)
- [155: Should you grant roles at the project level or on individual resources?](#155-should-you-grant-roles-at-the-project-level-or-on-individual-resources)
- [156: What is service account impersonation?](#156-what-is-service-account-impersonation)
- [157: How do short-lived service account credentials work?](#157-how-do-short-lived-service-account-credentials-work)
- [158: How do you give a Cloud Run service access to other Google Cloud resources?](#158-how-do-you-give-a-cloud-run-service-access-to-other-google-cloud-resources)
- [159: How do you let GitHub Actions deploy to Google Cloud without a key?](#159-how-do-you-let-github-actions-deploy-to-google-cloud-without-a-key)
- [160: How does Workload Identity Federation for GKE work?](#160-how-does-workload-identity-federation-for-gke-work)
- [161: What does the Service Account User role do and why does it matter?](#161-what-does-the-service-account-user-role-do-and-why-does-it-matter)
- [162: How do you troubleshoot a "Permission denied" error?](#162-how-do-you-troubleshoot-a-permission-denied-error)
- [163: Which organization policies would you set in a new organization?](#163-which-organization-policies-would-you-set-in-a-new-organization)
- [164: What is concurrency in Cloud Run and how do you choose it?](#164-what-is-concurrency-in-cloud-run-and-how-do-you-choose-it)
- [165: How do min and max instances work in Cloud Run?](#165-how-do-min-and-max-instances-work-in-cloud-run)
- [166: What is the difference between request-based and instance-based billing in Cloud Run?](#166-what-is-the-difference-between-request-based-and-instance-based-billing-in-cloud-run)
- [167: What causes cold starts on Cloud Run and how do you reduce them?](#167-what-causes-cold-starts-on-cloud-run-and-how-do-you-reduce-them)
- [168: What is startup CPU boost?](#168-what-is-startup-cpu-boost)
- [169: How do revisions and traffic splitting work in Cloud Run?](#169-how-do-revisions-and-traffic-splitting-work-in-cloud-run)
- [170: What are revision tags in Cloud Run?](#170-what-are-revision-tags-in-cloud-run)
- [171: How does one Cloud Run service call another private Cloud Run service?](#171-how-does-one-cloud-run-service-call-another-private-cloud-run-service)
- [172: What do the Cloud Run ingress settings do?](#172-what-do-the-cloud-run-ingress-settings-do)
- [173: How do you use Secret Manager secrets in Cloud Run?](#173-how-do-you-use-secret-manager-secrets-in-cloud-run)
- [174: How do you mount a Cloud Storage bucket in Cloud Run?](#174-how-do-you-mount-a-cloud-storage-bucket-in-cloud-run)
- [175: What are sidecars in Cloud Run?](#175-what-are-sidecars-in-cloud-run)
- [176: What health checks does Cloud Run support?](#176-what-health-checks-does-cloud-run-support)
- [177: What is the maximum request timeout on Cloud Run and how do you handle long-running work?](#177-what-is-the-maximum-request-timeout-on-cloud-run-and-how-do-you-handle-long-running-work)
- [178: How do Cloud Run jobs run tasks in parallel?](#178-how-do-cloud-run-jobs-run-tasks-in-parallel)
- [179: How does Cloud Run connect to resources in a VPC?](#179-how-does-cloud-run-connect-to-resources-in-a-vpc)
- [180: How do you connect Cloud Run to Cloud SQL securely?](#180-how-do-you-connect-cloud-run-to-cloud-sql-securely)
- [181: How do you put a load balancer in front of Cloud Run?](#181-how-do-you-put-a-load-balancer-in-front-of-cloud-run)
- [182: How should a Cloud Run container handle shutdown?](#182-how-should-a-cloud-run-container-handle-shutdown)
- [183: How do you write a function that runs when a file is uploaded to Cloud Storage?](#183-how-do-you-write-a-function-that-runs-when-a-file-is-uploaded-to-cloud-storage)
- [184: How do you process Pub/Sub messages with a Cloud Run function?](#184-how-do-you-process-pubsub-messages-with-a-cloud-run-function)
- [185: What are the differences between Cloud Functions 1st gen and Cloud Run functions?](#185-what-are-the-differences-between-cloud-functions-1st-gen-and-cloud-run-functions)
- [186: How do retries work for event-driven functions?](#186-how-do-retries-work-for-event-driven-functions)
- [187: What is a VPC-native GKE cluster?](#187-what-is-a-vpc-native-gke-cluster)
- [188: What is the difference between zonal and regional GKE clusters?](#188-what-is-the-difference-between-zonal-and-regional-gke-clusters)
- [189: What are node pools in GKE Standard?](#189-what-are-node-pools-in-gke-standard)
- [190: How do GKE release channels and upgrades work?](#190-how-do-gke-release-channels-and-upgrades-work)
- [191: How do you expose an app running on GKE?](#191-how-do-you-expose-an-app-running-on-gke)
- [192: How does autoscaling work in GKE?](#192-how-does-autoscaling-work-in-gke)
- [193: What is a private GKE cluster?](#193-what-is-a-private-gke-cluster)
- [194: How does GKE pull images from Artifact Registry?](#194-how-does-gke-pull-images-from-artifact-registry)
- [195: What is Config Connector?](#195-what-is-config-connector)
- [196: How does autoscaling work for a managed instance group?](#196-how-does-autoscaling-work-for-a-managed-instance-group)
- [197: What are autohealing and rolling updates in MIGs?](#197-what-are-autohealing-and-rolling-updates-in-migs)
- [198: How do you choose between Cloud Run, GKE, Compute Engine and Cloud Run functions?](#198-how-do-you-choose-between-cloud-run-gke-compute-engine-and-cloud-run-functions)
- [199: How do Cloud Build triggers work?](#199-how-do-cloud-build-triggers-work)
- [200: What are Cloud Build private pools?](#200-what-are-cloud-build-private-pools)
- [201: What is the difference between building with a Dockerfile and with buildpacks?](#201-what-is-the-difference-between-building-with-a-dockerfile-and-with-buildpacks)
- [202: How do you set up a delivery pipeline with Cloud Deploy?](#202-how-do-you-set-up-a-delivery-pipeline-with-cloud-deploy)
- [203: How do you do a canary deployment with Cloud Deploy?](#203-how-do-you-do-a-canary-deployment-with-cloud-deploy)
- [204: What are remote and virtual repositories in Artifact Registry?](#204-what-are-remote-and-virtual-repositories-in-artifact-registry)
- [205: How does vulnerability scanning work in Artifact Registry?](#205-how-does-vulnerability-scanning-work-in-artifact-registry)
- [206: How do you store Terraform state on Google Cloud?](#206-how-do-you-store-terraform-state-on-google-cloud)
- [207: What is the difference between the google and google-beta Terraform providers?](#207-what-is-the-difference-between-the-google-and-google-beta-terraform-providers)
- [208: How should Terraform authenticate to Google Cloud?](#208-how-should-terraform-authenticate-to-google-cloud)
- [209: How do you let a browser upload a file directly to Cloud Storage?](#209-how-do-you-let-a-browser-upload-a-file-directly-to-cloud-storage)
- [210: What are resumable uploads in Cloud Storage?](#210-what-are-resumable-uploads-in-cloud-storage)
- [211: How do you configure CORS on a Cloud Storage bucket?](#211-how-do-you-configure-cors-on-a-cloud-storage-bucket)
- [212: What consistency does Cloud Storage provide?](#212-what-consistency-does-cloud-storage-provide)
- [213: How do you get notified when objects change in Cloud Storage?](#213-how-do-you-get-notified-when-objects-change-in-cloud-storage)
- [214: What is Autoclass in Cloud Storage?](#214-what-is-autoclass-in-cloud-storage)
- [215: What are retention policies, object holds and Bucket Lock?](#215-what-are-retention-policies-object-holds-and-bucket-lock)
- [216: How do you get good performance from Cloud Storage at high request rates?](#216-how-do-you-get-good-performance-from-cloud-storage-at-high-request-rates)
- [217: What costs are there besides storage in Cloud Storage?](#217-what-costs-are-there-besides-storage-in-cloud-storage)
- [218: What is the difference between Cloud SQL Enterprise and Enterprise Plus editions?](#218-what-is-the-difference-between-cloud-sql-enterprise-and-enterprise-plus-editions)
- [219: Should Cloud SQL use a public IP or a private IP?](#219-should-cloud-sql-use-a-public-ip-or-a-private-ip)
- [220: What is IAM database authentication in Cloud SQL?](#220-what-is-iam-database-authentication-in-cloud-sql)
- [221: How do you handle database connections from serverless apps to Cloud SQL?](#221-how-do-you-handle-database-connections-from-serverless-apps-to-cloud-sql)
- [222: How do Cloud SQL maintenance windows work?](#222-how-do-cloud-sql-maintenance-windows-work)
- [223: How do you recover from an accidental data deletion in Cloud SQL?](#223-how-do-you-recover-from-an-accidental-data-deletion-in-cloud-sql)
- [224: How do you migrate an existing database to Cloud SQL?](#224-how-do-you-migrate-an-existing-database-to-cloud-sql)
- [225: How do indexes work in Firestore?](#225-how-do-indexes-work-in-firestore)
- [226: What is the difference between transactions and batched writes in Firestore?](#226-what-is-the-difference-between-transactions-and-batched-writes-in-firestore)
- [227: What are Firestore Security Rules?](#227-what-are-firestore-security-rules)
- [228: How do real-time listeners work in Firestore?](#228-how-do-real-time-listeners-work-in-firestore)
- [229: What limits should you know when designing for Firestore?](#229-what-limits-should-you-know-when-designing-for-firestore)
- [230: How do you paginate results in Firestore?](#230-how-do-you-paginate-results-in-firestore)
- [231: What are TTL policies in Firestore?](#231-what-are-ttl-policies-in-firestore)
- [232: What is Firestore with MongoDB compatibility?](#232-what-is-firestore-with-mongodb-compatibility)
- [233: Which Memorystore option should you pick?](#233-which-memorystore-option-should-you-pick)
- [234: How do you use Memorystore as a cache from Cloud Run?](#234-how-do-you-use-memorystore-as-a-cache-from-cloud-run)
- [235: What is table partitioning in BigQuery?](#235-what-is-table-partitioning-in-bigquery)
- [236: What is clustering in BigQuery?](#236-what-is-clustering-in-bigquery)
- [237: How does BigQuery pricing work?](#237-how-does-bigquery-pricing-work)
- [238: How do you reduce BigQuery query costs?](#238-how-do-you-reduce-bigquery-query-costs)
- [239: How do you stream data into BigQuery?](#239-how-do-you-stream-data-into-bigquery)
- [240: How do you prevent SQL injection when querying BigQuery from an app?](#240-how-do-you-prevent-sql-injection-when-querying-bigquery-from-an-app)
- [241: What are external tables and BigLake tables in BigQuery?](#241-what-are-external-tables-and-biglake-tables-in-bigquery)
- [242: What are scheduled queries and materialized views in BigQuery?](#242-what-are-scheduled-queries-and-materialized-views-in-bigquery)
- [243: How do you control access to specific rows and columns in BigQuery?](#243-how-do-you-control-access-to-specific-rows-and-columns-in-bigquery)
- [244: What is a dead-letter topic in Pub/Sub?](#244-what-is-a-dead-letter-topic-in-pubsub)
- [245: How does the retry policy work on a Pub/Sub subscription?](#245-how-does-the-retry-policy-work-on-a-pubsub-subscription)
- [246: How do ordering keys work in Pub/Sub?](#246-how-do-ordering-keys-work-in-pubsub)
- [247: What is exactly-once delivery in Pub/Sub?](#247-what-is-exactly-once-delivery-in-pubsub)
- [248: How do you filter messages on a Pub/Sub subscription?](#248-how-do-you-filter-messages-on-a-pubsub-subscription)
- [249: What are BigQuery and Cloud Storage subscriptions in Pub/Sub?](#249-what-are-bigquery-and-cloud-storage-subscriptions-in-pubsub)
- [250: What are Pub/Sub schemas?](#250-what-are-pubsub-schemas)
- [251: How do you secure a push subscription to Cloud Run?](#251-how-do-you-secure-a-push-subscription-to-cloud-run)
- [252: What is flow control in a Pub/Sub subscriber?](#252-what-is-flow-control-in-a-pubsub-subscriber)
- [253: How do message retention and seek work in Pub/Sub?](#253-how-do-message-retention-and-seek-work-in-pubsub)
- [254: When would you use Cloud Tasks instead of Pub/Sub?](#254-when-would-you-use-cloud-tasks-instead-of-pubsub)
- [255: How do you create a Cloud Task that calls a private Cloud Run service?](#255-how-do-you-create-a-cloud-task-that-calls-a-private-cloud-run-service)
- [256: How do you trigger code from any Google Cloud API call using Eventarc?](#256-how-do-you-trigger-code-from-any-google-cloud-api-call-using-eventarc)
- [257: What does a simple Workflows definition look like?](#257-what-does-a-simple-workflows-definition-look-like)
- [258: How do you run a Cloud Run job on a schedule?](#258-how-do-you-run-a-cloud-run-job-on-a-schedule)
- [259: What is Shared VPC?](#259-what-is-shared-vpc)
- [260: What is VPC Network Peering and what are its limits?](#260-what-is-vpc-network-peering-and-what-are-its-limits)
- [261: What is Private Service Connect?](#261-what-is-private-service-connect)
- [262: What is private services access?](#262-what-is-private-services-access)
- [263: What are hierarchical and network firewall policies?](#263-what-are-hierarchical-and-network-firewall-policies)
- [264: How do you pick a Google Cloud load balancer?](#264-how-do-you-pick-a-google-cloud-load-balancer)
- [265: What are the components of a global external Application Load Balancer?](#265-what-are-the-components-of-a-global-external-application-load-balancer)
- [266: How do you get Google-managed certificates on a load balancer?](#266-how-do-you-get-google-managed-certificates-on-a-load-balancer)
- [267: How do you control caching in Cloud CDN?](#267-how-do-you-control-caching-in-cloud-cdn)
- [268: How do you write Cloud Armor rules?](#268-how-do-you-write-cloud-armor-rules)
- [269: How do you rate limit clients with Cloud Armor?](#269-how-do-you-rate-limit-clients-with-cloud-armor)
- [270: How do you use IAP to protect a Cloud Run app or reach a VM?](#270-how-do-you-use-iap-to-protect-a-cloud-run-app-or-reach-a-vm)
- [271: How do you configure Cloud NAT and avoid port exhaustion?](#271-how-do-you-configure-cloud-nat-and-avoid-port-exhaustion)
- [272: How do private DNS zones and DNS forwarding work in Cloud DNS?](#272-how-do-private-dns-zones-and-dns-forwarding-work-in-cloud-dns)
- [273: How does HA VPN work?](#273-how-does-ha-vpn-work)
- [274: How do you rotate secrets in Secret Manager?](#274-how-do-you-rotate-secrets-in-secret-manager)
- [275: How do you read a secret from Secret Manager in Node.js?](#275-how-do-you-read-a-secret-from-secret-manager-in-nodejs)
- [276: What are customer-managed encryption keys (CMEK)?](#276-what-are-customer-managed-encryption-keys-cmek)
- [277: How do you write structured logs from Cloud Run?](#277-how-do-you-write-structured-logs-from-cloud-run)
- [278: What are log-based metrics?](#278-what-are-log-based-metrics)
- [279: What are log sinks and how do you route logs?](#279-what-are-log-sinks-and-how-do-you-route-logs)
- [280: How do you control Cloud Logging costs?](#280-how-do-you-control-cloud-logging-costs)
- [281: What is Log Analytics?](#281-what-is-log-analytics)
- [282: How do you send custom metrics to Cloud Monitoring?](#282-how-do-you-send-custom-metrics-to-cloud-monitoring)
- [283: How does trace context propagate between services on Google Cloud?](#283-how-does-trace-context-propagate-between-services-on-google-cloud)
- [284: How do you define an SLO in Cloud Monitoring?](#284-how-do-you-define-an-slo-in-cloud-monitoring)
- [285: What is Google Cloud Managed Service for Prometheus?](#285-what-is-google-cloud-managed-service-for-prometheus)
- [286: A Cloud Run service is returning 500 and 503 errors. How do you debug it?](#286-a-cloud-run-service-is-returning-500-and-503-errors-how-do-you-debug-it)
- [287: What is Cloud Profiler?](#287-what-is-cloud-profiler)
- [288: How can you automatically stop spending when a budget is exceeded?](#288-how-can-you-automatically-stop-spending-when-a-budget-is-exceeded)
- [289: Why export billing data to BigQuery?](#289-why-export-billing-data-to-bigquery)
- [290: How do you allocate cloud costs to teams?](#290-how-do-you-allocate-cloud-costs-to-teams)
- [291: What is the difference between resource-based and spend-based committed use discounts?](#291-what-is-the-difference-between-resource-based-and-spend-based-committed-use-discounts)
- [292: How do you rightsize Compute Engine and GKE resources?](#292-how-do-you-rightsize-compute-engine-and-gke-resources)
- [293: How should an app handle quota errors (429 or RESOURCE_EXHAUSTED)?](#293-how-should-an-app-handle-quota-errors-429-or-resource_exhausted)
- [294: How do retries work in the Google Cloud client libraries?](#294-how-do-retries-work-in-the-google-cloud-client-libraries)
- [295: How do you manage configuration across dev, staging and prod?](#295-how-do-you-manage-configuration-across-dev-staging-and-prod)
- [296: How do you develop locally against Google Cloud services?](#296-how-do-you-develop-locally-against-google-cloud-services)
- [297: How do you call Gemini models from a Node.js backend on Google Cloud?](#297-how-do-you-call-gemini-models-from-a-nodejs-backend-on-google-cloud)
- [298: When would you choose Dataflow over Dataproc?](#298-when-would-you-choose-dataflow-over-dataproc)
- [299: What is Datastream?](#299-what-is-datastream)
- [300: How do you add user authentication to an app on Google Cloud?](#300-how-do-you-add-user-authentication-to-an-app-on-google-cloud)

### Advanced Questions (301-450)

- [301: How would you design a highly available web app on Google Cloud?](#301-how-would-you-design-a-highly-available-web-app-on-google-cloud)
- [302: How do you run a Cloud Run service in multiple regions?](#302-how-do-you-run-a-cloud-run-service-in-multiple-regions)
- [303: What disaster recovery strategies can you use on Google Cloud?](#303-what-disaster-recovery-strategies-can-you-use-on-google-cloud)
- [304: How does Spanner provide strong consistency across regions?](#304-how-does-spanner-provide-strong-consistency-across-regions)
- [305: How do you avoid hotspots in Spanner?](#305-how-do-you-avoid-hotspots-in-spanner)
- [306: What are interleaved tables in Spanner?](#306-what-are-interleaved-tables-in-spanner)
- [307: How do you choose between Cloud SQL, AlloyDB and Spanner?](#307-how-do-you-choose-between-cloud-sql-alloydb-and-spanner)
- [308: What makes AlloyDB faster than standard PostgreSQL?](#308-what-makes-alloydb-faster-than-standard-postgresql)
- [309: How do you design a row key for Bigtable?](#309-how-do-you-design-a-row-key-for-bigtable)
- [310: How do you detect and fix hotspots in Bigtable?](#310-how-do-you-detect-and-fix-hotspots-in-bigtable)
- [311: How do you avoid hotspots in Firestore?](#311-how-do-you-avoid-hotspots-in-firestore)
- [312: How do you implement a high-traffic counter in Firestore?](#312-how-do-you-implement-a-high-traffic-counter-in-firestore)
- [313: How does BigQuery work internally?](#313-how-does-bigquery-work-internally)
- [314: How do you optimize a slow BigQuery query?](#314-how-do-you-optimize-a-slow-bigquery-query)
- [315: How do BigQuery reservations and slot autoscaling work?](#315-how-do-bigquery-reservations-and-slot-autoscaling-work)
- [316: What are the limits of DML in BigQuery and how do you do upserts?](#316-what-are-the-limits-of-dml-in-bigquery-and-how-do-you-do-upserts)
- [317: How can you stream change data (CDC) into BigQuery with upserts?](#317-how-can-you-stream-change-data-cdc-into-bigquery-with-upserts)
- [318: How do you handle data residency and cross-region needs in BigQuery?](#318-how-do-you-handle-data-residency-and-cross-region-needs-in-bigquery)
- [319: What delivery guarantees does Pub/Sub give end to end?](#319-what-delivery-guarantees-does-pubsub-give-end-to-end)
- [320: How do you build an effectively exactly-once processing pipeline on Google Cloud?](#320-how-do-you-build-an-effectively-exactly-once-processing-pipeline-on-google-cloud)
- [321: What are the trade-offs of using ordering keys in Pub/Sub at scale?](#321-what-are-the-trade-offs-of-using-ordering-keys-in-pubsub-at-scale)
- [322: How do you scale Pub/Sub consumers and handle backpressure?](#322-how-do-you-scale-pubsub-consumers-and-handle-backpressure)
- [323: How do you reliably publish events after a database write?](#323-how-do-you-reliably-publish-events-after-a-database-write)
- [324: How would you implement a saga for a multi-service transaction?](#324-how-would-you-implement-a-saga-for-a-multi-service-transaction)
- [325: How do you design idempotent APIs on Google Cloud?](#325-how-do-you-design-idempotent-apis-on-google-cloud)
- [326: What are VPC Service Controls?](#326-what-are-vpc-service-controls)
- [327: How do you roll out VPC Service Controls without breaking things?](#327-how-do-you-roll-out-vpc-service-controls-without-breaking-things)
- [328: What is Access Context Manager?](#328-what-is-access-context-manager)
- [329: How do you apply least privilege at scale in a large organization?](#329-how-do-you-apply-least-privilege-at-scale-in-a-large-organization)
- [330: What are IAM deny policies?](#330-what-are-iam-deny-policies)
- [331: What are principal access boundary policies?](#331-what-are-principal-access-boundary-policies)
- [332: Why are service account keys such a big risk, and how do you remove them?](#332-why-are-service-account-keys-such-a-big-risk-and-how-do-you-remove-them)
- [333: How do you secure Workload Identity Federation configuration?](#333-how-do-you-secure-workload-identity-federation-configuration)
- [334: How does using a service account across projects work?](#334-how-does-using-a-service-account-across-projects-work)
- [335: What are common privilege escalation paths in Google Cloud IAM?](#335-what-are-common-privilege-escalation-paths-in-google-cloud-iam)
- [336: How do you secure a Cloud Run service end to end?](#336-how-do-you-secure-a-cloud-run-service-end-to-end)
- [337: What is Binary Authorization?](#337-what-is-binary-authorization)
- [338: How do you secure the software supply chain on Google Cloud?](#338-how-do-you-secure-the-software-supply-chain-on-google-cloud)
- [339: How do you use secrets safely in Cloud Build?](#339-how-do-you-use-secrets-safely-in-cloud-build)
- [340: How does key management work in Cloud KMS in more detail?](#340-how-does-key-management-work-in-cloud-kms-in-more-detail)
- [341: What are Cloud HSM and Cloud External Key Manager?](#341-what-are-cloud-hsm-and-cloud-external-key-manager)
- [342: How do you do envelope encryption with Cloud KMS?](#342-how-do-you-do-envelope-encryption-with-cloud-kms)
- [343: What is Confidential Computing on Google Cloud?](#343-what-is-confidential-computing-on-google-cloud)
- [344: What is Shielded VM?](#344-what-is-shielded-vm)
- [345: What is Sensitive Data Protection?](#345-what-is-sensitive-data-protection)
- [346: What does Security Command Center provide at higher tiers?](#346-what-does-security-command-center-provide-at-higher-tiers)
- [347: Should you enable Data Access audit logs everywhere?](#347-should-you-enable-data-access-audit-logs-everywhere)
- [348: A service account key was leaked publicly. What do you do?](#348-a-service-account-key-was-leaked-publicly-what-do-you-do)
- [349: How do you restrict where resources can be created?](#349-how-do-you-restrict-where-resources-can-be-created)
- [350: What are Assured Workloads?](#350-what-are-assured-workloads)
- [351: How does Cloud Run run containers under the hood?](#351-how-does-cloud-run-run-containers-under-the-hood)
- [352: When should you choose the second generation execution environment in Cloud Run?](#352-when-should-you-choose-the-second-generation-execution-environment-in-cloud-run)
- [353: How does Cloud Run decide how many instances to run?](#353-how-does-cloud-run-decide-how-many-instances-to-run)
- [354: What are Cloud Run worker pools?](#354-what-are-cloud-run-worker-pools)
- [355: How do GPUs work on Cloud Run?](#355-how-do-gpus-work-on-cloud-run)
- [356: How do you stop Cloud Run from overwhelming a database?](#356-how-do-you-stop-cloud-run-from-overwhelming-a-database)
- [357: Can Cloud Run handle WebSockets, streaming and gRPC?](#357-can-cloud-run-handle-websockets-streaming-and-grpc)
- [358: How does session affinity work in Cloud Run and what are its limits?](#358-how-does-session-affinity-work-in-cloud-run-and-what-are-its-limits)
- [359: How do you give a Cloud Run service a static outbound IP?](#359-how-do-you-give-a-cloud-run-service-a-static-outbound-ip)
- [360: How does container startup order work in a multi-container Cloud Run service?](#360-how-does-container-startup-order-work-in-a-multi-container-cloud-run-service)
- [361: How do you reduce Cloud Run costs?](#361-how-do-you-reduce-cloud-run-costs)
- [362: What is the difference between allowing unauthenticated access and disabling the invoker IAM check?](#362-what-is-the-difference-between-allowing-unauthenticated-access-and-disabling-the-invoker-iam-check)
- [363: How does GKE Autopilot pricing and scheduling work?](#363-how-does-gke-autopilot-pricing-and-scheduling-work)
- [364: How does the GKE metadata server work with Workload Identity Federation?](#364-how-does-the-gke-metadata-server-work-with-workload-identity-federation)
- [365: How do you control pod-to-pod traffic in GKE?](#365-how-do-you-control-pod-to-pod-traffic-in-gke)
- [366: How do you run applications across multiple GKE clusters?](#366-how-do-you-run-applications-across-multiple-gke-clusters)
- [367: How do you upgrade GKE nodes safely?](#367-how-do-you-upgrade-gke-nodes-safely)
- [368: What role do PodDisruptionBudgets play in GKE?](#368-what-role-do-poddisruptionbudgets-play-in-gke)
- [369: How do you use Spot VMs safely in GKE?](#369-how-do-you-use-spot-vms-safely-in-gke)
- [370: How do you optimize GKE costs?](#370-how-do-you-optimize-gke-costs)
- [371: What causes IP address exhaustion in GKE and how do you fix it?](#371-what-causes-ip-address-exhaustion-in-gke-and-how-do-you-fix-it)
- [372: How do you attach Cloud Armor, IAP and other settings to services exposed with the GKE Gateway API?](#372-how-do-you-attach-cloud-armor-iap-and-other-settings-to-services-exposed-with-the-gke-gateway-api)
- [373: What is Cloud Service Mesh?](#373-what-is-cloud-service-mesh)
- [374: What is live migration in Compute Engine?](#374-what-is-live-migration-in-compute-engine)
- [375: How do regional managed instance groups spread VMs and handle capacity shortages?](#375-how-do-regional-managed-instance-groups-spread-vms-and-handle-capacity-shortages)
- [376: What are stateful managed instance groups?](#376-what-are-stateful-managed-instance-groups)
- [377: What are sole-tenant nodes and placement policies?](#377-what-are-sole-tenant-nodes-and-placement-policies)
- [378: How does Google's global load balancer work internally?](#378-how-does-googles-global-load-balancer-work-internally)
- [379: Why does the Premium Tier network matter for performance?](#379-why-does-the-premium-tier-network-matter-for-performance)
- [380: When would you choose a regional load balancer over a global one?](#380-when-would-you-choose-a-regional-load-balancer-over-a-global-one)
- [381: How do you design hybrid connectivity between on-prem and Google Cloud?](#381-how-do-you-design-hybrid-connectivity-between-on-prem-and-google-cloud)
- [382: What is Network Connectivity Center?](#382-what-is-network-connectivity-center)
- [383: How do you set up DNS for a hybrid environment?](#383-how-do-you-set-up-dns-for-a-hybrid-environment)
- [384: How do you reduce network egress costs on Google Cloud?](#384-how-do-you-reduce-network-egress-costs-on-google-cloud)
- [385: How do you publish an internal service to other teams with Private Service Connect?](#385-how-do-you-publish-an-internal-service-to-other-teams-with-private-service-connect)
- [386: How do you connect serverless services to a private database securely?](#386-how-do-you-connect-serverless-services-to-a-private-database-securely)
- [387: How would you implement rate limiting across a distributed API on Google Cloud?](#387-how-would-you-implement-rate-limiting-across-a-distributed-api-on-google-cloud)
- [388: When would you use Apigee and what does it give you?](#388-when-would-you-use-apigee-and-what-does-it-give-you)
- [389: How would you design a multi-tenant SaaS on Google Cloud?](#389-how-would-you-design-a-multi-tenant-saas-on-google-cloud)
- [390: What is a landing zone and how do you build one on Google Cloud?](#390-what-is-a-landing-zone-and-how-do-you-build-one-on-google-cloud)
- [391: How do you structure Terraform for a large Google Cloud setup?](#391-how-do-you-structure-terraform-for-a-large-google-cloud-setup)
- [392: How do you enforce policies on Terraform changes before they are applied?](#392-how-do-you-enforce-policies-on-terraform-changes-before-they-are-applied)
- [393: Which organization-wide guardrails are the most important?](#393-which-organization-wide-guardrails-are-the-most-important)
- [394: How would you migrate an app from AWS to Google Cloud?](#394-how-would-you-migrate-an-app-from-aws-to-google-cloud)
- [395: How do you migrate a production database with near-zero downtime?](#395-how-do-you-migrate-a-production-database-with-near-zero-downtime)
- [396: How does Cloud SQL high availability work internally, and what happens during failover?](#396-how-does-cloud-sql-high-availability-work-internally-and-what-happens-during-failover)
- [397: How do you design cross-region disaster recovery for Cloud SQL?](#397-how-do-you-design-cross-region-disaster-recovery-for-cloud-sql)
- [398: How do you tune Cloud SQL for PostgreSQL performance?](#398-how-do-you-tune-cloud-sql-for-postgresql-performance)
- [399: How do you manage database connections for thousands of serverless instances?](#399-how-do-you-manage-database-connections-for-thousands-of-serverless-instances)
- [400: How do Memorystore failover and client behavior affect app reliability?](#400-how-do-memorystore-failover-and-client-behavior-affect-app-reliability)
- [401: What is a cache stampede and how do you prevent it?](#401-what-is-a-cache-stampede-and-how-do-you-prevent-it)
- [402: How would you design uploading and processing of very large files?](#402-how-would-you-design-uploading-and-processing-of-very-large-files)
- [403: Can object naming affect Cloud Storage performance?](#403-can-object-naming-affect-cloud-storage-performance)
- [404: Why might users still see old content after you update a file in Cloud Storage?](#404-why-might-users-still-see-old-content-after-you-update-a-file-in-cloud-storage)
- [405: How would you design a data lake and warehouse on Google Cloud?](#405-how-would-you-design-a-data-lake-and-warehouse-on-google-cloud)
- [406: How do windows and watermarks work in Dataflow streaming pipelines?](#406-how-do-windows-and-watermarks-work-in-dataflow-streaming-pipelines)
- [407: What makes Dataflow scale and process exactly once?](#407-what-makes-dataflow-scale-and-process-exactly-once)
- [408: When can you skip Dataflow and send Pub/Sub data straight to BigQuery?](#408-when-can-you-skip-dataflow-and-send-pubsub-data-straight-to-bigquery)
- [409: What would a complete observability setup for a Google Cloud app look like?](#409-what-would-a-complete-observability-setup-for-a-google-cloud-app-look-like)
- [410: How do you control logging costs at large scale?](#410-how-do-you-control-logging-costs-at-large-scale)
- [411: How do you centralize logs from all projects in an organization?](#411-how-do-you-centralize-logs-from-all-projects-in-an-organization)
- [412: How do you avoid alert fatigue in Cloud Monitoring?](#412-how-do-you-avoid-alert-fatigue-in-cloud-monitoring)
- [413: Users report the API is slow. How do you find the cause?](#413-users-report-the-api-is-slow-how-do-you-find-the-cause)
- [414: A Cloud Run service suddenly returns HTTP 429 errors. What could be wrong?](#414-a-cloud-run-service-suddenly-returns-http-429-errors-what-could-be-wrong)
- [415: The backlog on a Pub/Sub subscription keeps growing. How do you investigate?](#415-the-backlog-on-a-pubsub-subscription-keeps-growing-how-do-you-investigate)
- [416: GKE pods are stuck in Pending or keep getting OOMKilled. How do you troubleshoot?](#416-gke-pods-are-stuck-in-pending-or-keep-getting-oomkilled-how-do-you-troubleshoot)
- [417: Cloud SQL CPU is at 100% after a release. What do you do?](#417-cloud-sql-cpu-is-at-100-after-a-release-what-do-you-do)
- [418: Your Google Cloud bill doubled overnight. How do you find out why?](#418-your-google-cloud-bill-doubled-overnight-how-do-you-find-out-why)
- [419: How do you prepare Google Cloud for a big launch or traffic event?](#419-how-do-you-prepare-google-cloud-for-a-big-launch-or-traffic-event)
- [420: How do you load test an app running on Google Cloud?](#420-how-do-you-load-test-an-app-running-on-google-cloud)
- [421: How do you design an app to survive a zone outage?](#421-how-do-you-design-an-app-to-survive-a-zone-outage)
- [422: How do you prevent retry storms between services?](#422-how-do-you-prevent-retry-storms-between-services)
- [423: How do you reduce API latency for users around the world?](#423-how-do-you-reduce-api-latency-for-users-around-the-world)
- [424: What are your options for data consistency across regions?](#424-what-are-your-options-for-data-consistency-across-regions)
- [425: What FinOps practices would you set up for a Google Cloud organization?](#425-what-finops-practices-would-you-set-up-for-a-google-cloud-organization)
- [426: How do you decide how much to commit with CUDs?](#426-how-do-you-decide-how-much-to-commit-with-cuds)
- [427: How do you choose a Google Cloud region for an app?](#427-how-do-you-choose-a-google-cloud-region-for-an-app)
- [428: How does Google Cloud help with sustainability?](#428-how-does-google-cloud-help-with-sustainability)
- [429: How would you build a RAG (retrieval-augmented generation) app on Google Cloud?](#429-how-would-you-build-a-rag-retrieval-augmented-generation-app-on-google-cloud)
- [430: How do you secure a generative AI application on Google Cloud?](#430-how-do-you-secure-a-generative-ai-application-on-google-cloud)
- [431: How do you choose where to serve an ML model on Google Cloud?](#431-how-do-you-choose-where-to-serve-an-ml-model-on-google-cloud)
- [432: What can you do with AI and ML directly in BigQuery?](#432-what-can-you-do-with-ai-and-ml-directly-in-bigquery)
- [433: How do you choose between Cloud Run jobs, Batch and Dataflow for batch processing?](#433-how-do-you-choose-between-cloud-run-jobs-batch-and-dataflow-for-batch-processing)
- [434: How do you orchestrate dependent jobs and services?](#434-how-do-you-orchestrate-dependent-jobs-and-services)
- [435: How would you design a system that receives webhooks at high volume?](#435-how-would-you-design-a-system-that-receives-webhooks-at-high-volume)
- [436: How would you build a real-time chat or live-update feature on Google Cloud?](#436-how-would-you-build-a-real-time-chat-or-live-update-feature-on-google-cloud)
- [437: How do you design a file processing pipeline that is easy to operate?](#437-how-do-you-design-a-file-processing-pipeline-that-is-easy-to-operate)
- [438: When should tenants or teams get separate projects instead of sharing one?](#438-when-should-tenants-or-teams-get-separate-projects-instead-of-sharing-one)
- [439: How do you do a blue-green deployment of a whole stack, not just one service?](#439-how-do-you-do-a-blue-green-deployment-of-a-whole-stack-not-just-one-service)
- [440: How do you run database schema migrations in a CI/CD pipeline on Google Cloud?](#440-how-do-you-run-database-schema-migrations-in-a-cicd-pipeline-on-google-cloud)
- [441: How do you manage application configuration and feature flags across many services?](#441-how-do-you-manage-application-configuration-and-feature-flags-across-many-services)
- [442: How do you test infrastructure code for Google Cloud?](#442-how-do-you-test-infrastructure-code-for-google-cloud)
- [443: At what point does GKE become cheaper than Cloud Run?](#443-at-what-point-does-gke-become-cheaper-than-cloud-run)
- [444: How do you use error budgets to decide on releases?](#444-how-do-you-use-error-budgets-to-decide-on-releases)
- [445: What is a sound backup strategy across Google Cloud services?](#445-what-is-a-sound-backup-strategy-across-google-cloud-services)
- [446: How do you protect backups against ransomware or a malicious admin?](#446-how-do-you-protect-backups-against-ransomware-or-a-malicious-admin)
- [447: How do you handle data deletion requests (like GDPR) in a Google Cloud system?](#447-how-do-you-handle-data-deletion-requests-like-gdpr-in-a-google-cloud-system)
- [448: How do you keep a large Google Cloud organization clean over time?](#448-how-do-you-keep-a-large-google-cloud-organization-clean-over-time)
- [449: What are common anti-patterns on Google Cloud?](#449-what-are-common-anti-patterns-on-google-cloud)
- [450: Design an e-commerce backend on Google Cloud.](#450-design-an-e-commerce-backend-on-google-cloud)

---

# Easy Questions (1-150)

## 1: What is Google Cloud?

Google Cloud (often called GCP, Google Cloud Platform) is Google's public cloud. It gives you computing, storage, databases, networking, data analytics, AI and developer tools that you rent and pay for by usage instead of buying your own hardware.

It runs on the same global network and data centers that Google uses for Search, YouTube and Gmail. You manage it through the web console, the `gcloud` command line tool, client libraries and REST/gRPC APIs.

## 2: What is the difference between Google Cloud, GCP and Google Workspace?

- **Google Cloud** is the company's full cloud business. It includes the infrastructure platform and Google Workspace.
- **GCP (Google Cloud Platform)** is the older name people still use for the infrastructure part: Compute Engine, Cloud Run, Cloud Storage, BigQuery and so on.
- **Google Workspace** is the office suite: Gmail, Docs, Drive, Meet. It is a SaaS product, not something you build on.

In interviews "GCP" and "Google Cloud" usually mean the same thing.

## 3: What are regions and zones?

A **region** is a geographic area, for example `europe-west1` (Belgium) or `us-central1` (Iowa). A **zone** is an isolated location inside a region, for example `europe-west1-b`. Most regions have three or more zones.

Zones have separate power, cooling and networking, so a failure in one zone usually does not affect the others. To survive a zone failure you run your app in more than one zone. To survive a region failure you run in more than one region.

Resources are zonal (a VM, a zonal disk), regional (a Cloud Run service, a regional MIG, a Cloud SQL HA instance) or global (a VPC network, a global load balancer, an image).

## 4: What are multi-region and dual-region locations?

Some services, mainly Cloud Storage, BigQuery, Firestore and Spanner, let you store data in more than one region at once:

- **Multi-region**: a large area like `US`, `EU` or `ASIA`. Google picks the regions inside it.
- **Dual-region**: two specific regions you choose, like `europe-west1` and `europe-west4` (or predefined pairs such as `EUR4`).

You get higher availability and the data survives a full region outage. The trade-off is higher price, and for some services slightly higher write latency.

## 5: What is the Google Cloud resource hierarchy?

Resources are organized in a tree:

```text
Organization (example.com)
├── Folder (Production)
│   ├── Project (shop-prod)
│   │   ├── Cloud Run service
│   │   └── Cloud SQL instance
│   └── Project (data-prod)
└── Folder (Development)
    └── Project (shop-dev)
```

IAM policies and organization policies set on a higher level are inherited by everything below it. So a role granted on a folder applies to all projects in that folder.

## 6: What is a project in Google Cloud?

A project is the basic container for resources. Every VM, bucket, database or Cloud Run service belongs to exactly one project. Billing, enabled APIs, quotas and IAM permissions are all managed per project.

A project has three identifiers:

- **Project name**: a display name you can change.
- **Project ID**: a globally unique ID you choose at creation (`shop-prod-4821`). It cannot be changed.
- **Project number**: a number Google assigns. It shows up in service account emails and some URLs.

## 7: What are folders used for?

Folders group projects (and other folders) under an organization. Teams usually create folders per environment (prod, non-prod), per department or per business unit.

The main reason to use folders is to apply IAM roles and organization policies once to a group of projects instead of to each project separately. For example you can give the security team viewer access on the `Production` folder and it applies to every prod project.

## 8: What is the organization resource?

The organization is the root node of the hierarchy. It is created automatically when a company uses Google Workspace or Cloud Identity with its domain and creates its first project.

It lets the company own all projects centrally. Without it, projects belong to the individual users who created them, and when that person leaves you can lose control of the project. Org admins can set org-wide IAM and organization policies.

## 9: What is a billing account?

A billing account pays for the resources in one or more projects. It holds the payment method (card or invoice) and receives the charges.

A project must be linked to a billing account to use paid services. One billing account can pay for many projects, and you can move a project to a different billing account. Billing permissions (for example Billing Account Administrator) are separate from project permissions.

## 10: How do budgets and budget alerts work?

You create a budget on a billing account with an amount (for example $500 per month) and thresholds (50%, 90%, 100%). When actual or forecasted spend crosses a threshold, Google sends an email to billing admins and can publish a message to a Pub/Sub topic.

A budget does **not** stop spending by itself. It only notifies. To actually cap costs you have to react to the Pub/Sub message, for example with a function that disables billing on the project (see question 288).

## 11: What are labels?

Labels are key-value pairs you attach to resources, such as `env=prod`, `team=payments` or `app=checkout`.

They are mainly used to filter resources and to split costs in billing reports and the BigQuery billing export. Keys and values must be lowercase and can contain letters, numbers, underscores and dashes.

```bash
gcloud compute instances add-labels my-vm --zone=europe-west1-b --labels=env=prod,team=payments
```

## 12: What is the difference between labels, tags and network tags?

- **Labels**: key-value metadata for organizing resources and costs. They do not affect access.
- **Tags** (resource manager tags): key-value pairs defined centrally at org or project level. You can use them in IAM conditions and organization policies, and they are inherited down the hierarchy. For example "allow this role only on resources tagged `env=dev`".
- **Network tags**: plain strings on Compute Engine VMs, like `web-server`, used to target firewall rules and routes.

## 13: What is the Google Cloud console?

The console (`console.cloud.google.com`) is the web UI for Google Cloud. You can create and manage resources, view logs and metrics, see billing, manage IAM and open Cloud Shell.

It is good for exploring and one-off tasks. For anything you repeat or want to review, it is better to use `gcloud` scripts or infrastructure as code like Terraform.

## 14: What is the gcloud CLI?

`gcloud` is the main command line tool for Google Cloud. It is part of the Google Cloud CLI, which also includes `bq` for BigQuery and the older `gsutil` for Cloud Storage.

```bash
gcloud auth login
gcloud config set project my-project
gcloud run services list --region=europe-west1
gcloud compute instances create my-vm --zone=europe-west1-b --machine-type=e2-small
```

Commands follow the pattern `gcloud <group> <resource> <action>`. Some features first appear under `gcloud beta` or `gcloud alpha`.

## 15: What are gcloud configurations?

A configuration is a named set of gcloud properties such as account, project, region and zone. They help when you switch between projects or accounts often.

```bash
gcloud config configurations create prod
gcloud config set project shop-prod
gcloud config set run/region europe-west1

gcloud config configurations activate dev
gcloud config list
```

You can also override per command with `--project` or the `CLOUDSDK_CORE_PROJECT` environment variable.

## 16: What is Cloud Shell?

Cloud Shell is a free, browser-based terminal opened from the console. It gives you a small Linux VM with `gcloud`, `kubectl`, Terraform, Docker, git, Node.js, Python and other tools already installed, and you are already authenticated as your user.

It has 5 GB of persistent home directory storage and a built-in code editor. It is handy for quick tasks, but sessions time out after inactivity, so it is not a place to run long jobs.

## 17: Why do you need to enable APIs in a project?

Each Google Cloud service is exposed as an API (for example `run.googleapis.com`, `sqladmin.googleapis.com`). Most APIs are disabled in a new project, and you must enable them before you can use the service.

```bash
gcloud services enable run.googleapis.com artifactregistry.googleapis.com cloudbuild.googleapis.com
gcloud services list --enabled
```

If you forget, you get an error like `PERMISSION_DENIED: ... API has not been used in project ... or it is disabled`.

## 18: What are quotas?

Quotas limit how much of a resource a project can use, for example the number of vCPUs per region, API requests per minute or the number of Cloud Run instances. They protect you from runaway costs and protect Google from overload.

You can view quotas in the console under IAM & Admin > Quotas and request increases for most of them. When you hit a quota, API calls fail with `RESOURCE_EXHAUSTED` or HTTP 429. Some limits are fixed system limits that cannot be raised.

## 19: What service models does Google Cloud offer?

- **IaaS**: you manage the OS and above. Example: Compute Engine VMs.
- **Containers / CaaS**: you manage containers, Google manages the cluster to different degrees. Examples: GKE Standard, GKE Autopilot.
- **Serverless / PaaS**: you give code or a container and Google runs and scales it. Examples: Cloud Run, Cloud Run functions, App Engine.
- **Managed services**: databases and tools you just use. Examples: Cloud SQL, Firestore, BigQuery, Pub/Sub.
- **SaaS**: finished apps like Google Workspace.

The more managed the service, the less you operate but the less control you have.

## 20: What is the Google Cloud free tier?

There are two parts:

- **Free trial**: new customers get $300 in credits to use within 90 days.
- **Free tier (Always Free)**: monthly free usage that does not expire, for example an `e2-micro` VM in some US regions, 5 GB of Cloud Storage in some US regions, 2 million Cloud Run requests, 1 TiB of BigQuery queries and 10 GiB of BigQuery storage, and Firestore daily free reads and writes.

Limits change over time, so always check the current free tier page.

## 21: How does Google Cloud pricing generally work?

You pay for what you use. Most compute is billed per second (Compute Engine has a one-minute minimum). Storage is billed per GB per month, and network egress is billed per GB leaving a region or going to the internet. Ingress is usually free.

Discounts come from sustained use discounts (automatic for some VM types), committed use discounts (1 or 3 year commitments) and Spot VMs. You can estimate costs with the Google Cloud Pricing Calculator.

## 22: What is IAM in Google Cloud?

Identity and Access Management controls **who** can do **what** on **which resource**.

- **Who**: a principal, like a user, group or service account.
- **What**: a role, which is a set of permissions like `storage.objects.get`.
- **Which resource**: the organization, folder, project or a single resource like a bucket.

You grant roles to principals on a resource through an allow policy. Permissions are not granted directly, only through roles.

## 23: What types of principals exist in Google Cloud IAM?

- Google accounts (`user:alice@example.com`)
- Service accounts (`serviceAccount:api@my-project.iam.gserviceaccount.com`)
- Google groups (`group:devs@example.com`)
- Google Workspace or Cloud Identity domains (`domain:example.com`)
- `allUsers` (anyone on the internet) and `allAuthenticatedUsers` (any signed-in Google account)
- Workforce and workload identity pool identities (external users and workloads federated in, for example from GitHub, AWS or Okta)

Be careful with `allUsers` and `allAuthenticatedUsers`. They make a resource public.

## 24: What are the types of IAM roles?

- **Basic roles**: Owner, Editor and Viewer. They apply to almost every service in a project.
- **Predefined roles**: created and maintained by Google per service, like `roles/run.invoker`, `roles/storage.objectViewer` or `roles/cloudsql.client`.
- **Custom roles**: roles you define with an exact list of permissions, at project or organization level.

Use predefined roles first, and custom roles when no predefined role is narrow enough.

## 25: Why should you avoid basic roles?

Basic roles are very broad. Editor can create and delete almost anything in the project, including VMs, databases and buckets, and Owner can also change IAM. Giving a developer or a service Editor breaks the principle of least privilege.

They are fine for a personal sandbox project. In shared or production projects, use predefined roles that cover only what is needed, for example `roles/run.developer` and `roles/logging.viewer`.

## 26: What is an IAM allow policy?

An allow policy (often just "IAM policy") is attached to a resource and lists role bindings. Each binding maps a role to a list of principals, optionally with a condition.

```json
{
  "bindings": [
    {
      "role": "roles/storage.objectViewer",
      "members": [
        "group:analysts@example.com",
        "serviceAccount:etl@my-project.iam.gserviceaccount.com"
      ]
    }
  ],
  "etag": "BwX...",
  "version": 3
}
```

```bash
gcloud projects add-iam-policy-binding my-project \
  --member="group:analysts@example.com" --role="roles/bigquery.dataViewer"
```

The `etag` prevents two people from overwriting each other's changes.

## 27: What is a service account?

A service account is an identity for an application or workload, not a person. Its email looks like `name@PROJECT_ID.iam.gserviceaccount.com`.

You attach a service account to a VM, a Cloud Run service, a function or a GKE workload, and the code running there gets credentials for that account automatically. You then grant roles to the service account, the same way as for users. A service account is also a resource itself, so you control who can use or impersonate it.

## 28: Why should you avoid service account keys?

A service account key is a long-lived JSON file with a private key. Anyone who gets the file can act as the service account until the key is deleted. Keys get committed to Git, copied to laptops and leaked in logs.

Better options:

- Attach the service account to the resource (Cloud Run, GKE, VM) and let it get short-lived tokens from the metadata server.
- Use Workload Identity Federation for workloads outside Google Cloud (GitHub Actions, AWS, on-prem).
- Use impersonation for local development.

New organizations have key creation disabled by default through an organization policy.

## 29: What are default service accounts?

Some services create a service account automatically when you enable them, for example the Compute Engine default service account (`PROJECT_NUMBER-compute@developer.gserviceaccount.com`). VMs, Cloud Run and functions use it if you do not pick another one.

In older projects this account was given the Editor role automatically, which is far too much. Best practice is to create a dedicated service account per app with only the roles it needs. New organizations block the automatic Editor grant with an organization policy.

## 30: What are Application Default Credentials (ADC)?

ADC is the way Google client libraries find credentials automatically, so you do not have to pass them in code. The libraries check, in order:

1. The `GOOGLE_APPLICATION_CREDENTIALS` environment variable (path to a credential file).
2. Credentials created by `gcloud auth application-default login` on your machine.
3. The attached service account from the metadata server when running on Google Cloud.

```js
import { Storage } from "@google-cloud/storage";

// No keys in code: works locally and on Cloud Run
const storage = new Storage();
const [buckets] = await storage.getBuckets();
```

## 31: What is the difference between gcloud auth login and gcloud auth application-default login?

- `gcloud auth login` gives credentials to the **gcloud CLI itself**, so commands like `gcloud run deploy` work.
- `gcloud auth application-default login` creates a local ADC file used by **your code and client libraries** (and by tools like Terraform).

They are separate. A common mistake is running only `gcloud auth login` and then wondering why a Node.js app says it cannot find default credentials.

## 32: Why grant roles to groups instead of individual users?

When roles are granted to groups (`group:backend-devs@example.com`), you manage access by adding or removing people from the group. You do not have to edit IAM policies on many projects when someone joins or leaves.

It also makes policies shorter and easier to audit, and you stay further from the limit on bindings per policy. Service accounts can be group members too, but usually you grant them roles directly.

## 33: What compute options does Google Cloud offer?

- **Compute Engine**: virtual machines with full control.
- **GKE**: managed Kubernetes, in Standard or Autopilot mode.
- **Cloud Run**: serverless containers (services, jobs, worker pools) and functions.
- **App Engine**: older PaaS for web apps.
- **Batch**: managed batch jobs on VMs.
- **Bare Metal Solution and VMware Engine**: for special lift-and-shift cases.

For most new web backends, Cloud Run is the default choice. GKE fits complex platforms, and Compute Engine fits workloads that need full OS control.

## 34: What is Compute Engine?

Compute Engine is Google Cloud's IaaS service for virtual machines. You choose the machine type, image (Debian, Ubuntu, Windows and so on), disks, network and zone, and you manage the OS and software yourself.

```bash
gcloud compute instances create web-1 \
  --zone=europe-west1-b \
  --machine-type=e2-medium \
  --image-family=debian-12 --image-project=debian-cloud \
  --tags=http-server
```

VMs can be resized, stopped and started. You pay for vCPUs and memory while the VM is running, and for disks all the time.

## 35: What machine families are there in Compute Engine?

- **General purpose**: E2 (cheap, shared-core options like `e2-micro`), N2, N2D, N4, C3, C4 and Arm-based C4A and T2A. Good for web servers and most apps.
- **Compute optimized**: C2, C2D, H3. High per-core performance.
- **Memory optimized**: M1, M2, M3. Very large memory for SAP HANA and in-memory databases.
- **Storage optimized**: Z3. Lots of local SSD.
- **Accelerator optimized**: A2, A3, A4, G2 with NVIDIA GPUs.

You can also create custom machine types with a specific number of vCPUs and amount of memory on several families.

## 36: What are Spot VMs?

Spot VMs use spare Compute Engine capacity at a large discount (often 60-91% off). Google can stop them at any time with a 30-second notice when it needs the capacity back.

They are good for fault-tolerant work: batch jobs, CI runners, rendering, stateless workers. They are a bad fit for databases or anything that cannot handle sudden shutdown. Preemptible VMs are the older version of Spot VMs, with a hard 24-hour runtime limit.

```bash
gcloud compute instances create batch-1 --zone=us-central1-a --provisioning-model=SPOT --instance-termination-action=DELETE
```

## 37: What disk options does Compute Engine have?

- **Persistent Disk** (pd-standard, pd-balanced, pd-ssd): network block storage, zonal or regional (replicated across two zones).
- **Hyperdisk** (Balanced, Throughput, Extreme, ML): newer block storage where you set IOPS and throughput separately from size. Newer machine series such as C4 and N4 use Hyperdisk.
- **Local SSD**: physically attached to the host, very fast, but data is lost when the VM stops or the host fails.

Disks are separate from the VM, so a persistent disk survives a VM delete if auto-delete is off.

## 38: What is the difference between images and snapshots?

- An **image** is a boot disk template used to create new VMs. Google provides public images (Debian, Ubuntu, Windows), and you can make custom images with your software already installed. Image families point to the latest image in a series.
- A **snapshot** is a point-in-time backup of a disk. Snapshots are incremental and can be scheduled with snapshot schedules.

Use images to create many identical VMs, and snapshots to back up and restore data.

## 39: What are startup scripts and metadata?

Every VM has a metadata server at `http://metadata.google.internal` that returns information like the project ID, zone, service account tokens and custom key-value metadata.

A startup script is a special metadata key (`startup-script`) that runs every time the VM boots:

```bash
gcloud compute instances create web-1 --zone=europe-west1-b \
  --metadata=startup-script='#! /bin/bash
apt-get update && apt-get install -y nginx'
```

Startup scripts are fine for simple setup. For larger setups, bake a custom image or use containers.

## 40: How do you SSH into a Compute Engine VM?

The simplest way is `gcloud compute ssh my-vm --zone=europe-west1-b`, or the SSH button in the console. gcloud creates a key and pushes it to the VM.

The recommended setup is **OS Login**, which ties SSH access to IAM roles (`roles/compute.osLogin` or `roles/compute.osAdminLogin`) instead of keys in metadata. For VMs without a public IP, use IAP TCP forwarding (`gcloud compute ssh my-vm --tunnel-through-iap`) so you do not need to open port 22 to the internet.

## 41: What are sustained use discounts and committed use discounts?

- **Sustained use discounts (SUDs)**: applied automatically when certain VM types (like N1 and N2) run a large part of the month. No commitment needed. They do not apply to E2 or some newer series.
- **Committed use discounts (CUDs)**: you commit to a resource amount (resource-based) or a dollar spend per hour (spend-based, also called flexible CUDs) for 1 or 3 years in exchange for a bigger discount. Spend-based CUDs also exist for Cloud Run, Cloud SQL, GKE and others.

CUDs are billed whether you use the resources or not, so commit only to your steady baseline.

## 42: What are instance templates and managed instance groups?

An **instance template** defines a VM's configuration: machine type, image, disks, network, metadata and service account.

A **managed instance group (MIG)** creates and manages identical VMs from a template. It gives you:

- Autoscaling based on CPU, load balancer usage or custom metrics
- Autohealing with health checks
- Rolling updates to a new template
- Zonal or regional (spread across zones) placement

MIGs are the usual way to run stateless VM-based apps behind a load balancer.

## 43: What is App Engine and what is the difference between standard and flexible?

App Engine is Google's original PaaS. You deploy code with an `app.yaml` file and Google runs and scales it.

- **Standard environment**: runs in a sandbox with specific language runtimes, starts fast and can scale to zero.
- **Flexible environment**: runs your app in Docker containers on Compute Engine VMs. It cannot scale to zero and is slower to deploy.

App Engine still works and many older apps use it, but for new projects Google recommends Cloud Run, which gives you more control and runs any container.

## 44: What is Cloud Run?

Cloud Run is a fully managed serverless platform for running containers. You give it a container image (or source code), and it handles servers, HTTPS, scaling and load balancing.

Key points:

- Any language or binary that can run in a Linux container
- Scales automatically, including down to zero
- Billed per use (CPU, memory, requests), with a free tier
- Each service gets an HTTPS URL like `https://api-123456789.europe-west1.run.app`
- Built-in IAM authentication, revisions and traffic splitting

It has several resource types: services (HTTP), jobs (run to completion), worker pools (always-on background work) and functions.

## 45: How do you deploy an app to Cloud Run?

From a container image:

```bash
gcloud run deploy api \
  --image=europe-west1-docker.pkg.dev/my-project/apps/api:1.4.0 \
  --region=europe-west1 \
  --service-account=api-sa@my-project.iam.gserviceaccount.com \
  --no-allow-unauthenticated
```

Or directly from source code. Cloud Build builds the image with your Dockerfile, or with Google Cloud buildpacks if there is no Dockerfile, and stores it in Artifact Registry:

```bash
gcloud run deploy api --source=. --region=europe-west1
```

Each deploy creates a new immutable revision.

## 46: What is the difference between a Cloud Run service and a Cloud Run job?

- A **service** listens for HTTP requests (or gRPC, WebSockets) on a port and scales with incoming traffic. Use it for APIs, websites and webhooks.
- A **job** runs a container to completion and then stops. It does not serve requests. Use it for batch work, migrations, scheduled reports and data processing. A job can run many tasks in parallel.

```bash
gcloud run jobs deploy nightly-report --image=REGION-docker.pkg.dev/my-project/apps/report:latest --region=europe-west1
gcloud run jobs execute nightly-report --region=europe-west1
```

## 47: What are Cloud Run functions?

Cloud Run functions is the current name of Cloud Functions. You write a single function, Google builds it into a container and runs it on Cloud Run. It was renamed in 2024 when Cloud Functions 2nd gen was merged into Cloud Run.

Functions are good for small pieces of glue code: handle an HTTP webhook, react to a file upload in Cloud Storage or process a Pub/Sub message. Supported runtimes include Node.js, Python, Go, Java, .NET, Ruby and PHP.

The older "Cloud Functions (1st gen)" still exists for existing functions, but new functions should use the Cloud Run based version.

## 48: What triggers can start a Cloud Run function?

- **HTTP triggers**: the function has a URL and runs on each HTTP request.
- **Event triggers**: the function runs when an event happens. Events come through Eventarc and include Pub/Sub messages, Cloud Storage object changes, Firestore document changes, Cloud Audit Log entries (almost any Google API call) and events from other sources.

Event-driven functions receive the event in CloudEvents format.

## 49: How do you write and deploy an HTTP function in Node.js?

```js
// index.js
import functions from "@google-cloud/functions-framework";

functions.http("hello", (req, res) => {
  const name = req.query.name ?? "world";
  res.send(`Hello, ${name}!`);
});
```

```json
{
  "type": "module",
  "dependencies": { "@google-cloud/functions-framework": "^4.0.0" }
}
```

```bash
gcloud functions deploy hello \
  --gen2 --runtime=nodejs22 --region=europe-west1 \
  --source=. --entry-point=hello --trigger-http
```

You can also deploy the same code with `gcloud run deploy hello --source=. --function=hello`.

## 50: What is the Functions Framework?

The Functions Framework is an open source library from Google that wraps your function in a small HTTP server. It is what Cloud Run functions uses under the hood, and you can run it locally to test:

```bash
npx @google-cloud/functions-framework --target=hello
curl http://localhost:8080?name=Ana
```

Because it is just a normal server, you can also put the same function into a container and run it anywhere, which reduces vendor lock-in.

## 51: What is GKE?

Google Kubernetes Engine (GKE) is Google's managed Kubernetes service. Google runs and upgrades the Kubernetes control plane, and you deploy workloads with normal Kubernetes manifests and `kubectl`.

GKE adds integrations with Google Cloud: load balancers for Services and Gateways, Persistent Disk volumes, Workload Identity Federation for IAM, Cloud Logging and Monitoring, autoscaling, and automatic upgrades through release channels.

## 52: What is the difference between GKE Autopilot and GKE Standard?

- **Autopilot**: Google manages the nodes. You just deploy pods and pay for the CPU, memory and storage that the pods request. Security best practices are enforced, and you cannot SSH into nodes. It is the recommended default mode.
- **Standard**: you create and manage node pools, choose machine types and pay for whole nodes whether they are full or not. You get more control, for example over node configuration and privileged workloads.

```bash
gcloud container clusters create-auto my-cluster --region=europe-west1
```

## 53: What is Artifact Registry?

Artifact Registry is Google Cloud's service for storing build artifacts: Docker and OCI images, npm, Maven, Python, Go, Apt and Yum packages, and more. Repositories are regional or multi-regional, and access is controlled by IAM.

```bash
gcloud artifacts repositories create apps --repository-format=docker --location=europe-west1
gcloud auth configure-docker europe-west1-docker.pkg.dev
docker push europe-west1-docker.pkg.dev/my-project/apps/api:1.0.0
```

Image URLs follow the format `LOCATION-docker.pkg.dev/PROJECT/REPOSITORY/IMAGE:TAG`.

## 54: What happened to Container Registry?

Container Registry (`gcr.io`) was the older image registry. It was deprecated and shut down in 2025, and Artifact Registry replaces it.

You will still see `gcr.io/...` image names in old docs, pipelines and manifests. Google provides `gcr.io` repositories hosted in Artifact Registry so these names can keep working, but new projects should use `*-docker.pkg.dev` repositories directly.

## 55: What is Cloud Build?

Cloud Build is a managed CI/CD service that runs builds as a series of steps. Each step is a container. It can build Docker images, run tests, push to Artifact Registry and deploy to Cloud Run, GKE and other targets.

Builds can be started manually with `gcloud builds submit`, or automatically by triggers on GitHub, GitLab or Bitbucket pushes and pull requests. You pay per build minute, with a free monthly amount.

## 56: What does a basic cloudbuild.yaml look like?

```yaml
steps:
  - name: "node:22"
    entrypoint: npm
    args: ["ci"]
  - name: "node:22"
    entrypoint: npm
    args: ["test"]
  - name: "gcr.io/cloud-builders/docker"
    args:
      [
        "build",
        "-t",
        "europe-west1-docker.pkg.dev/$PROJECT_ID/apps/api:$SHORT_SHA",
        ".",
      ]
  - name: "gcr.io/cloud-builders/docker"
    args:
      ["push", "europe-west1-docker.pkg.dev/$PROJECT_ID/apps/api:$SHORT_SHA"]
  - name: "gcr.io/google.com/cloudsdktool/cloud-sdk"
    entrypoint: gcloud
    args:
      [
        "run",
        "deploy",
        "api",
        "--image=europe-west1-docker.pkg.dev/$PROJECT_ID/apps/api:$SHORT_SHA",
        "--region=europe-west1",
      ]
images:
  - "europe-west1-docker.pkg.dev/$PROJECT_ID/apps/api:$SHORT_SHA"
```

`$PROJECT_ID` and `$SHORT_SHA` are built-in substitutions. All steps share the `/workspace` directory.

## 57: What is Cloud Storage?

Cloud Storage is Google's object storage, similar to Amazon S3. You store files (objects) of any type in buckets. A single object can be up to 5 TiB.

It is used for user uploads, static website files, backups, data lake files, logs and build artifacts. It has 11 nines (99.999999999%) of annual durability and you access it through the console, `gcloud storage`, client libraries or the JSON/XML APIs.

## 58: What are buckets and objects in Cloud Storage?

A **bucket** is a container for objects. Bucket names are globally unique across all of Google Cloud. A bucket has a location, a default storage class and settings like versioning and access control.

An **object** is a file plus metadata (content type, cache control, custom metadata). The namespace is flat: `images/2026/cat.png` is one object name, and the "folders" in the console are just name prefixes. Hierarchical namespace buckets are an option if you need real folders with fast renames.

## 59: What storage classes does Cloud Storage have?

| Class    | Use case                       | Minimum storage duration |
| -------- | ------------------------------ | ------------------------ |
| Standard | Frequently accessed data       | None                     |
| Nearline | Accessed about once a month    | 30 days                  |
| Coldline | Accessed about once a quarter  | 90 days                  |
| Archive  | Accessed less than once a year | 365 days                 |

Colder classes have cheaper storage but higher retrieval and operation costs, plus an early deletion fee if you delete before the minimum duration. All classes have the same low latency (millisecond access), unlike some archive services on other clouds.

## 60: What location types can a Cloud Storage bucket have?

- **Region**: one region, like `europe-west1`. Lowest cost, and best when compute is in the same region.
- **Dual-region**: two regions. Data is replicated, and you can turn on turbo replication for a 15-minute RPO.
- **Multi-region**: a large area like `US` or `EU`. Highest availability, good for serving content to users across a continent.

The location cannot be changed after the bucket is created. To move data you create a new bucket and copy objects.

## 61: How do you copy files to and from Cloud Storage from the command line?

Use `gcloud storage`, which replaces the older `gsutil` tool:

```bash
gcloud storage buckets create gs://my-app-uploads --location=europe-west1 --uniform-bucket-level-access
gcloud storage cp ./report.pdf gs://my-app-uploads/reports/
gcloud storage cp -r ./dist gs://my-site-bucket
gcloud storage ls gs://my-app-uploads/reports/
gcloud storage rsync ./dist gs://my-site-bucket --recursive --delete-unmatched-destination-objects
```

`gsutil` still works and you will see it in older scripts, but `gcloud storage` is faster and is the recommended tool.

## 62: What is object versioning in Cloud Storage?

When versioning is on, overwriting or deleting an object does not remove the old data. The previous version becomes a noncurrent version with its own generation number, and you can restore it.

```bash
gcloud storage buckets update gs://my-bucket --versioning
gcloud storage ls --all-versions gs://my-bucket/config.json
```

Noncurrent versions are billed like normal objects, so combine versioning with lifecycle rules that delete old versions after some time.

## 63: What are lifecycle rules in Cloud Storage?

Lifecycle rules automatically delete objects or change their storage class based on conditions like age, storage class, number of newer versions or name prefix.

```json
{
  "rule": [
    {
      "action": { "type": "SetStorageClass", "storageClass": "COLDLINE" },
      "condition": { "age": 90 }
    },
    { "action": { "type": "Delete" }, "condition": { "age": 365 } },
    {
      "action": { "type": "Delete" },
      "condition": { "isLive": false, "numNewerVersions": 3 }
    }
  ]
}
```

```bash
gcloud storage buckets update gs://my-bucket --lifecycle-file=lifecycle.json
```

## 64: What is uniform bucket-level access?

Cloud Storage has two access control systems: IAM (bucket-level) and ACLs (per object). **Uniform bucket-level access** turns off ACLs, so only IAM decides who can access objects.

This is the recommended setting. It is simpler to reason about, works with IAM Conditions and organization policies, and avoids surprises like a single object being made public by an ACL. Fine-grained ACLs are a legacy option, kept mainly for compatibility with S3-style tools.

## 65: What is public access prevention?

Public access prevention is a bucket setting (also enforceable with an organization policy) that blocks granting access to `allUsers` and `allAuthenticatedUsers`. Even if someone tries to make the bucket or an object public, it does not work.

Turn it on for every bucket that should never be public, which is most of them. For buckets that really serve public content, like a static website, you leave it off on purpose and usually put Cloud CDN in front.

## 66: What is a signed URL?

A signed URL gives time-limited access to one object to anyone who has the URL, without a Google account. It is used to let users download a private file or upload a file directly to a bucket from the browser.

```js
import { Storage } from "@google-cloud/storage";

const storage = new Storage();
const [url] = await storage
  .bucket("my-app-uploads")
  .file("invoices/inv-1001.pdf")
  .getSignedUrl({
    version: "v4",
    action: "read",
    expires: Date.now() + 15 * 60 * 1000,
  });
```

V4 signed URLs can be valid for at most 7 days.

## 67: How do you host a static website on Cloud Storage?

1. Create a bucket and upload your files (`index.html`, JS, CSS).
2. Grant `roles/storage.objectViewer` to `allUsers` on the bucket.
3. Set the main page and error page: `gcloud storage buckets update gs://my-site --web-main-page-suffix=index.html --web-error-page=404.html`.
4. For a custom domain with HTTPS, put a global external Application Load Balancer with a backend bucket in front, and turn on Cloud CDN.

For single-page apps that need rewrites, Firebase Hosting is often easier.

## 68: What is soft delete in Cloud Storage?

Soft delete keeps deleted and overwritten objects for a retention period (7 days by default, configurable from 7 to 90 days, or turned off). During that time you can restore them, even if versioning is off.

```bash
gcloud storage ls --soft-deleted gs://my-bucket
gcloud storage restore gs://my-bucket/important.csv#1712345678901234
```

Soft-deleted data is billed, so buckets with a lot of short-lived temporary files can cost more. For those you can lower or disable the retention.

## 69: What database options does Google Cloud offer?

- **Cloud SQL**: managed MySQL, PostgreSQL and SQL Server.
- **AlloyDB for PostgreSQL**: high-performance PostgreSQL-compatible database.
- **Spanner**: globally distributed, strongly consistent relational database.
- **Firestore**: serverless NoSQL document database.
- **Bigtable**: wide-column NoSQL for very large, low-latency workloads.
- **Memorystore**: managed Redis, Valkey and Memcached.
- **BigQuery**: data warehouse for analytics (not for transactions).

Pick based on data model, scale, consistency needs and cost.

## 70: What is Cloud SQL?

Cloud SQL is a managed relational database service for MySQL, PostgreSQL and SQL Server. Google handles the VM, OS patches, backups, replication, failover and storage growth. You still own the schema, queries and tuning.

It comes in two editions, Enterprise and Enterprise Plus. It supports high availability, read replicas, point-in-time recovery, private IP and IAM database authentication. It is the usual default for a relational database behind a web app.

## 71: How do you connect to Cloud SQL from an application?

Options:

- **Cloud Run built-in connection**: add the instance with `--add-cloudsql-instances=PROJECT:REGION:INSTANCE` and connect through a Unix socket at `/cloudsql/PROJECT:REGION:INSTANCE`.
- **Cloud SQL language connectors** (Node.js, Python, Java, Go): libraries that handle TLS and IAM authorization in your code.
- **Cloud SQL Auth Proxy**: a small binary or sidecar that opens a local port and forwards to the instance with IAM-based auth and TLS.
- **Private IP**: connect directly over the VPC (for example with Direct VPC egress from Cloud Run).

```bash
./cloud-sql-proxy my-project:europe-west1:main-db --port 5432
psql "host=127.0.0.1 port=5432 user=app dbname=shop"
```

## 72: How do backups work in Cloud SQL?

Cloud SQL takes automated daily backups during a backup window you choose, and keeps them for a configurable number of days. You can also take on-demand backups before risky changes.

With point-in-time recovery turned on, Cloud SQL also keeps transaction logs, so you can restore to any moment in the retention window (for example to just before a bad `DELETE`). Restores create a new instance or overwrite an existing one. Enterprise Plus can keep backups longer and supports backups that survive instance deletion.

## 73: What does high availability mean in Cloud SQL?

An HA (regional) Cloud SQL instance has a primary in one zone and a standby in another zone of the same region. Data is written synchronously to regional persistent disk, so the standby has the same data.

If the primary zone fails, Cloud SQL fails over to the standby automatically, usually within a minute, and the instance keeps the same IP. The standby does not serve read traffic. For reads you use read replicas.

## 74: What are Cloud SQL read replicas?

A read replica is a read-only copy of the primary that is updated with asynchronous replication. You send read-heavy queries (reports, search pages) to replicas to take load off the primary.

Replicas can be in the same region or another region (cross-region replicas, useful for disaster recovery and local reads). Because replication is asynchronous, replicas can lag behind, so reads right after a write may not see the new data.

## 75: What is Firestore?

Firestore is a serverless NoSQL document database. It scales automatically, has no servers or instances to manage, and you pay per document read, write and delete plus storage.

It supports real-time listeners, offline support in mobile and web SDKs, ACID transactions, strong consistency and multi-region replication. It is popular for mobile and web apps, especially with Firebase, and for backend apps that need a simple, scalable document store.

## 76: What is the difference between Firestore Native mode and Datastore mode?

- **Native mode**: the full Firestore with collections and documents, real-time listeners, mobile and web SDKs and Security Rules.
- **Datastore mode**: uses the Firestore storage engine but keeps the older Cloud Datastore API (entities, kinds, ancestors). No real-time updates or mobile SDKs. Meant for server apps that already use the Datastore API.

The mode is chosen per database. New apps usually use Native mode. A project can have several Firestore databases, each with its own mode.

## 77: What is the Firestore data model?

Data is stored in **documents**, which are sets of fields (strings, numbers, maps, arrays, timestamps, references and so on). Documents live in **collections**. A document can have **subcollections**, which lets you nest data:

```text
users/{userId}
  name: "Ana"
  plan: "pro"
  orders/{orderId}
    total: 49.99
    createdAt: 2026-10-01T10:00:00Z
```

A document can be at most 1 MiB. Collections are created automatically when you add the first document. Firestore has no joins, so you design data around your queries.

## 78: How do you read and write Firestore data from Node.js?

```js
import { Firestore, FieldValue } from "@google-cloud/firestore";

const db = new Firestore();

await db
  .collection("users")
  .doc("u123")
  .set({ name: "Ana", plan: "pro", createdAt: FieldValue.serverTimestamp() });

const snap = await db.collection("users").doc("u123").get();
console.log(snap.exists ? snap.data() : "not found");

const proUsers = await db
  .collection("users")
  .where("plan", "==", "pro")
  .orderBy("createdAt", "desc")
  .limit(20)
  .get();
proUsers.forEach((doc) => console.log(doc.id, doc.data()));
```

In Firebase projects you often use `firebase-admin` instead, which wraps the same client.

## 79: What is Bigtable?

Bigtable is a wide-column NoSQL database for very large amounts of data (terabytes to petabytes) with single-digit millisecond latency. It is the same technology behind Google Search and Maps, and it is compatible with the HBase API.

It fits time series, IoT, ad tech, financial data and ML feature stores. Data is sorted by a single row key, so good row key design is the most important part. It is not a good choice for small datasets or for queries that need joins or secondary indexes.

## 80: What is Spanner?

Spanner is a fully managed relational database that scales horizontally across regions while keeping strong consistency and ACID transactions. It supports GoogleSQL and a PostgreSQL dialect.

You size it in nodes or processing units (1,000 processing units equal 1 node), and multi-region configurations have a 99.999% availability SLA. It is used for global apps with large write volume, like payments, gaming and inventory, where a single Cloud SQL instance is not enough.

## 81: What is AlloyDB?

AlloyDB for PostgreSQL is a managed, PostgreSQL-compatible database built by Google for high performance. It separates compute and storage, has a columnar engine for fast analytical queries on the same data, and supports read pool instances for scaling reads.

It is a step up from Cloud SQL for PostgreSQL when you need more throughput, faster analytics or vector search with good performance (AlloyDB AI). AlloyDB Omni is a downloadable version you can run anywhere.

## 82: What is Memorystore?

Memorystore is a managed in-memory data store service. It offers:

- **Memorystore for Valkey** (Valkey is the open source fork of Redis)
- **Memorystore for Redis Cluster**
- **Memorystore for Redis** (non-cluster instances)
- **Memorystore for Memcached**

It is used for caching, sessions, rate limiting, leaderboards and queues. Instances are reached over private IP in your VPC, so clients must be in or connected to that network.

## 83: What is BigQuery?

BigQuery is Google's serverless data warehouse. You load or stream data into tables and query it with SQL, and it can scan terabytes in seconds. There are no servers or indexes to manage.

Storage and compute are separate. You pay for storage, and for compute either per TiB scanned (on-demand) or by reserving slots (editions). It also has built-in ML (BigQuery ML), geospatial functions, vector search, BI Engine and connections to external data in Cloud Storage and other clouds.

## 84: How is data organized in BigQuery?

```text
project
└── dataset (has a location, like EU or europe-west1)
    ├── table
    ├── view
    ├── materialized view
    └── routine (function or stored procedure)
```

You refer to a table as `project.dataset.table`. Access is controlled with IAM at the project, dataset, table or even row and column level. The dataset location decides where data is stored, and you cannot join tables from datasets in different locations in one query.

## 85: How do you run a BigQuery query from Node.js?

```js
import { BigQuery } from "@google-cloud/bigquery";

const bigquery = new BigQuery();

const [rows] = await bigquery.query({
  query: `
    SELECT country, COUNT(*) AS orders
    FROM \`my-project.shop.orders\`
    WHERE created_at >= @since
    GROUP BY country
    ORDER BY orders DESC`,
  params: { since: "2026-01-01" },
  location: "EU",
});

rows.forEach((r) => console.log(r.country, r.orders));
```

Always use query parameters (`@since`) instead of string concatenation, to avoid SQL injection.

## 86: What is Pub/Sub?

Pub/Sub is a fully managed, global messaging service. Publishers send messages to a **topic**, and every **subscription** on that topic gets a copy of each message. Subscribers then receive messages from their subscription.

It decouples services, absorbs traffic spikes and enables event-driven designs. It scales automatically to millions of messages per second, keeps unacknowledged messages for up to 7 days by default, and delivers at least once by default.

## 87: What is the difference between a topic and a subscription?

- A **topic** is a named channel that publishers send messages to. It does not keep messages by itself (unless you turn on topic retention).
- A **subscription** is attached to one topic and represents one consumer group. Each message is delivered to every subscription, but within one subscription each message goes to only one of the subscribers.

So to fan out an event to three services you create three subscriptions. To spread work across many workers you use one subscription with many subscribers.

## 88: What is the difference between push and pull subscriptions?

- **Pull**: your subscriber connects to Pub/Sub and pulls messages, usually with the streaming pull API in the client libraries. Good for workers on GKE or VMs and high throughput.
- **Push**: Pub/Sub sends each message as an HTTP POST to an HTTPS endpoint you set, like a Cloud Run service. A 2xx response acknowledges the message.

There are also export subscriptions that write messages directly to BigQuery or Cloud Storage without any code.

## 89: How do you publish and receive Pub/Sub messages in Node.js?

```js
import { PubSub } from "@google-cloud/pubsub";

const pubsub = new PubSub();

// Publish
const messageId = await pubsub.topic("orders").publishMessage({
  json: { orderId: "o-1001", total: 49.99 },
  attributes: { type: "order.created" },
});

// Subscribe (streaming pull)
const subscription = pubsub.subscription("orders-email");
subscription.on("message", (message) => {
  const order = JSON.parse(message.data.toString());
  console.log("Got order", order.orderId);
  message.ack();
});
subscription.on("error", (err) => console.error(err));
```

## 90: What is the acknowledgement deadline in Pub/Sub?

After Pub/Sub delivers a message, the subscriber has a time window (the ack deadline) to acknowledge it. The default is 10 seconds and the maximum is 600 seconds. If the message is not acked in time, Pub/Sub delivers it again.

The client libraries extend the deadline automatically while your code is still processing (lease management). If processing fails, call `message.nack()` to make Pub/Sub redeliver it right away.

## 91: What is Cloud Tasks?

Cloud Tasks is a managed queue for running work asynchronously by sending HTTP requests to a target, such as a Cloud Run service or any HTTPS endpoint. You add a task to a queue, and Cloud Tasks delivers it, with retries, rate limits and optional scheduling for a later time.

It is good for background jobs triggered by user actions, like sending an email after sign-up, where you want to control how fast the target is called.

## 92: What is Cloud Scheduler?

Cloud Scheduler is a managed cron service. You define a schedule with cron syntax and a target: an HTTP endpoint, a Pub/Sub topic or an App Engine route.

```bash
gcloud scheduler jobs create http nightly-cleanup \
  --location=europe-west1 \
  --schedule="0 3 * * *" --time-zone="Europe/Berlin" \
  --uri="https://cleanup-123456789.europe-west1.run.app/run" \
  --http-method=POST \
  --oidc-service-account-email=scheduler@my-project.iam.gserviceaccount.com
```

The OIDC token lets it call a private Cloud Run service.

## 93: What is Eventarc?

Eventarc is Google Cloud's eventing service. It routes events from sources such as Cloud Storage, Pub/Sub, Firestore, Cloud Audit Logs and third parties to targets like Cloud Run services, Cloud Run functions, Workflows and GKE services.

Events use the CloudEvents format. Eventarc Standard handles triggers from Google sources, and Eventarc Advanced adds a message bus with filtering, transformation and routing for more complex setups. When you create an event-triggered Cloud Run function, an Eventarc trigger is created for you.

## 94: What is Workflows?

Workflows is a serverless orchestration service. You write a workflow in YAML or JSON as a series of steps that call HTTP endpoints, Google Cloud APIs, Cloud Run services and functions, with variables, conditions, loops, retries and error handling.

It fits multi-step business processes, like "charge the card, reserve stock, send confirmation", and long-running processes that need to wait for callbacks. You pay per step executed.

## 95: What is a VPC network in Google Cloud?

A Virtual Private Cloud (VPC) is a private network for your resources. In Google Cloud a VPC is **global**: one network can have subnets in many regions, and VMs in different regions can talk to each other over private IPs without extra setup.

The VPC contains subnets, routes and firewall rules. Resources like VMs, GKE nodes, internal load balancers and Memorystore instances get IP addresses from it.

## 96: What are subnets in Google Cloud?

A subnet is an IP range (for example `10.10.0.0/20`) in one region inside a VPC. Subnets are regional, so they cover all zones in that region.

You can expand a subnet's range later without downtime, but you cannot shrink it. Subnets can have secondary ranges, used by GKE for pod and service IPs. Ranges in the same VPC, and in connected VPCs, must not overlap.

## 97: What is the difference between auto mode and custom mode VPCs?

- **Auto mode**: Google creates one subnet in every region automatically, with fixed ranges from `10.128.0.0/9`. The `default` network in a new project is auto mode.
- **Custom mode**: you create subnets yourself in the regions you need, with ranges you choose.

Use custom mode for production. Auto mode ranges often overlap with other networks, which breaks peering and VPN later, and you get subnets in regions you never use.

## 98: How do firewall rules work in a Google Cloud VPC?

VPC firewall rules allow or deny traffic to and from VMs. Each rule has a direction (ingress or egress), a priority (lower number wins), an action (allow or deny), protocols and ports, a source or destination, and targets (all instances, network tags or service accounts).

```bash
gcloud compute firewall-rules create allow-http \
  --network=main --direction=INGRESS --action=ALLOW \
  --rules=tcp:80,tcp:443 --source-ranges=0.0.0.0/0 --target-tags=http-server
```

Firewalls are stateful. Every VPC has implied rules: deny all ingress, allow all egress. Newer setups often use network firewall policies, which can be shared and managed centrally.

## 99: What is the difference between internal and external IP addresses?

- An **internal IP** comes from a subnet range and is reachable only inside the VPC and connected networks.
- An **external IP** is a public address reachable from the internet. It can be **ephemeral** (changes when the VM stops) or **static** (reserved, stays the same until you release it).

Best practice is to give VMs only internal IPs and expose services through a load balancer. For outbound internet access without external IPs, use Cloud NAT.

## 100: What is Cloud NAT?

Cloud NAT lets VMs, GKE nodes and Cloud Run (through Direct VPC egress or a connector) with no external IP reach the internet for outbound connections, such as downloading packages or calling third-party APIs. Inbound connections from the internet are not allowed.

It is a managed, software-defined service attached to a Cloud Router in a region. There is no NAT VM to manage. You can use auto-allocated IPs or reserve static IPs, which is useful when a partner needs to allowlist your outbound IP.

## 101: What is Private Google Access?

Private Google Access is a subnet setting that lets VMs without external IPs reach Google APIs and services (Cloud Storage, BigQuery, Pub/Sub and so on) using their internal IPs.

```bash
gcloud compute networks subnets update app-subnet --region=europe-west1 --enable-private-ip-google-access
```

Without it, a VM with no public IP and no Cloud NAT cannot call Google APIs.

## 102: What load balancers does Google Cloud offer?

- **Application Load Balancers** (Layer 7, HTTP/HTTPS): global external, regional external, regional internal and cross-region internal. They do URL routing, TLS termination, Cloud CDN and Cloud Armor.
- **Network Load Balancers** (Layer 4): proxy (TCP/SSL with TLS offload) and passthrough (TCP/UDP that keeps the client IP), external or internal.

The global external Application Load Balancer gives you one anycast IP for users worldwide and routes them to the nearest healthy backend. Backends can be MIGs, GKE, Cloud Run, Cloud Storage buckets or external endpoints.

## 103: What is Cloud CDN?

Cloud CDN caches content at Google's edge locations close to users. It works together with the global external Application Load Balancer, with Cloud Storage buckets, MIGs, GKE, Cloud Run or external origins as backends.

You turn it on per backend service or backend bucket. It respects `Cache-Control` headers, supports signed URLs and cookies for private content, and lets you invalidate cached paths after a deploy. Media CDN is a separate product for very large video and download workloads.

## 104: What is Cloud DNS?

Cloud DNS is a managed, highly available DNS service. You create **public zones** for domains on the internet and **private zones** visible only to chosen VPC networks (for example `db.internal.example.com`).

```bash
gcloud dns managed-zones create example-com --dns-name="example.com." --description="Public zone"
gcloud dns record-sets create api.example.com. --zone=example-com --type=A --ttl=300 --rrdatas=34.120.10.20
```

It supports DNSSEC, forwarding zones, peering zones and routing policies like weighted and geolocation routing.

## 105: What is Cloud Armor?

Cloud Armor is Google's web application firewall and DDoS protection. You attach security policies to backend services of external load balancers.

Policies can:

- Allow or deny traffic by IP range, country or request attributes
- Block common attacks with preconfigured WAF rules (SQL injection, XSS and other OWASP Top 10 attacks)
- Rate limit or temporarily ban abusive clients
- Do bot management with reCAPTCHA

Cloud Armor Enterprise adds adaptive protection, threat intelligence and DDoS response support.

## 106: What is Identity-Aware Proxy (IAP)?

IAP puts Google sign-in and IAM in front of your app. A user must log in with a Google identity and have the `IAP-secured Web App User` role before their request reaches your backend. It is a simple way to protect internal tools without a VPN.

It works with backends behind an Application Load Balancer, App Engine and Cloud Run. IAP TCP forwarding also lets admins SSH or RDP to VMs that have no public IP.

## 107: What is Secret Manager?

Secret Manager stores API keys, passwords, certificates and other secrets. Secrets are versioned, encrypted, controlled with IAM and every access is written to audit logs.

```bash
echo -n "s3cr3t" | gcloud secrets create db-password --data-file=-
gcloud secrets add-iam-policy-binding db-password \
  --member="serviceAccount:api-sa@my-project.iam.gserviceaccount.com" \
  --role="roles/secretmanager.secretAccessor"
```

Cloud Run, GKE and Cloud Build can read secrets directly, so they never have to sit in code or plain environment variable config.

## 108: What is Cloud KMS?

Cloud Key Management Service lets you create and manage encryption keys. You can use them to encrypt and decrypt data in your app, to sign data, or as customer-managed encryption keys (CMEK) for services like Cloud Storage, BigQuery and Cloud SQL.

Keys live in key rings in a location. They can be software keys, HSM-backed keys (Cloud HSM) or keys held in an external key manager (Cloud EKM). Access to keys is controlled with IAM, separately from access to the data.

## 109: Is data encrypted at rest in Google Cloud by default?

Yes. All customer data stored in Google Cloud is encrypted at rest by default with AES-256, using keys Google manages. You do not need to do anything.

If you need more control, for compliance or to be able to revoke access, you can use customer-managed encryption keys (CMEK) in Cloud KMS. Data in transit between Google data centers and from users to Google front ends is also encrypted.

## 110: What is Cloud Logging?

Cloud Logging collects, stores and lets you search logs from Google Cloud services and your apps. Logs from Cloud Run, GKE, Cloud Run functions and App Engine are collected automatically from stdout and stderr. VMs need the Ops Agent.

You can search logs in Logs Explorer, create log-based metrics and alerts, route logs to BigQuery, Cloud Storage or Pub/Sub with sinks, and run SQL on them with Log Analytics.

## 111: How do you search logs in Logs Explorer?

You use the Logging query language:

```text
resource.type="cloud_run_revision"
resource.labels.service_name="api"
severity>=ERROR
timestamp>="2026-10-28T00:00:00Z"
jsonPayload.userId="u123"
```

Lines are combined with AND. You can use `OR`, `NOT`, `:` for "contains" and `=~` for regex. The same query works on the command line:

```bash
gcloud logging read 'resource.type="cloud_run_revision" AND severity>=ERROR' --limit=20 --freshness=1h
```

## 112: What is Cloud Monitoring?

Cloud Monitoring collects metrics from Google Cloud services, VMs (through the Ops Agent), GKE, Prometheus and your own apps. You can build dashboards, create alerting policies, set up uptime checks and define SLOs.

Many metrics are available with no setup, like Cloud Run request count and latency, Cloud SQL CPU, or Pub/Sub backlog size. Cloud Monitoring and Cloud Logging together are part of Google Cloud Observability (formerly Stackdriver).

## 113: What are uptime checks?

Uptime checks call your HTTP, HTTPS or TCP endpoint from several locations around the world at a regular interval (for example every minute) and check that it responds, optionally with expected content.

You connect an alerting policy to the check so you get notified when the endpoint is down from multiple locations. They can also check private endpoints inside a VPC.

## 114: What is an alerting policy in Cloud Monitoring?

An alerting policy watches a metric or log condition and creates an incident when it is met, for example "Cloud Run 5xx error rate above 5% for 5 minutes" or "Cloud SQL CPU above 90%".

It sends notifications to channels such as email, SMS, Slack, PagerDuty, webhooks or Pub/Sub. Policies can be created in the console, with `gcloud`, the API or Terraform. You can also use PromQL to write conditions.

## 115: What is Cloud Trace?

Cloud Trace is a distributed tracing system. It shows how long each part of a request took as it moved through your services, for example load balancer → Cloud Run API → Firestore → another service.

You send traces with OpenTelemetry, and Cloud Run and the load balancer can add their own spans. It helps find slow calls and bottlenecks that are hard to spot from logs alone.

## 116: What is Error Reporting?

Error Reporting groups exceptions and errors from your apps, shows how often they happen and when they first appeared, and can notify you about new errors.

It reads errors from Cloud Logging automatically. For Cloud Run, GKE and functions, logging a stack trace to stderr or as a structured log with `severity: "ERROR"` and the stack in the message is enough for it to pick it up.

## 117: What are Cloud Audit Logs?

Audit logs record who did what, where and when in your Google Cloud resources:

- **Admin Activity**: changes to configuration or metadata (create a VM, change IAM). Always on and free.
- **Data Access**: reads of configuration and reads or writes of user data. Off by default for most services (BigQuery is an exception) because they can be very large.
- **System Event**: actions done by Google systems, like live migration.
- **Policy Denied**: requests denied by a security policy like VPC Service Controls.

## 118: What is Google Cloud Observability?

Google Cloud Observability is the umbrella name for the monitoring tools: Cloud Logging, Cloud Monitoring, Cloud Trace, Cloud Profiler and Error Reporting, plus Managed Service for Prometheus. It used to be called Stackdriver, and later Google Cloud's operations suite.

Interviewers might use any of these names. They all refer to the same set of tools.

## 119: How do you use Terraform with Google Cloud?

Terraform uses the `google` (and `google-beta`) provider to create resources:

```hcl
provider "google" {
  project = "my-project"
  region  = "europe-west1"
}

resource "google_storage_bucket" "uploads" {
  name                        = "my-project-uploads"
  location                    = "EUROPE-WEST1"
  uniform_bucket_level_access = true
  public_access_prevention    = "enforced"
}
```

```bash
terraform init
terraform plan
terraform apply
```

Terraform is the most common infrastructure as code tool on Google Cloud.

## 120: What are Infrastructure Manager and Deployment Manager?

**Deployment Manager** was Google's original infrastructure as code tool, using YAML with Jinja or Python templates. It reached end of support on March 31, 2026. Resources it created keep working, but the service and `gcloud deployment-manager` commands can no longer be used to manage them.

**Infrastructure Manager** (Infra Manager) is the replacement. It is a managed service that runs Terraform for you: it stores state, runs `plan` and `apply` in Cloud Build and keeps a history of deployments.

## 121: What is Cloud Deploy?

Cloud Deploy is a managed continuous delivery service for Cloud Run and GKE (and other targets through custom targets). You define a delivery pipeline with ordered targets like `dev → staging → prod`, then create a release, and promote it from one target to the next.

It supports approvals, canary and blue-green style rollouts, automatic rollbacks, deploy verification and a full history of what was deployed where. It uses Skaffold to render and deploy manifests.

## 122: What is the relationship between Firebase and Google Cloud?

Firebase is Google's app development platform for mobile and web. Every Firebase project is also a Google Cloud project, so they share resources, billing and IAM.

Some Firebase services are Google Cloud services with extra SDKs, like Firestore and Cloud Storage for Firebase. Others are Firebase-specific, like Firebase Authentication, Hosting, App Hosting, Crashlytics and Remote Config. You can use both consoles on the same project.

## 123: What are Firebase Hosting and Firebase App Hosting?

- **Firebase Hosting** serves static files and single-page apps from a global CDN with free SSL and custom domains. It can also rewrite requests to Cloud Run or functions.
- **Firebase App Hosting** is for full-stack web frameworks with server-side rendering, like Next.js and Angular. You connect a GitHub repo, and it builds and runs the app on Cloud Run with a CDN in front.

```bash
firebase init hosting
firebase deploy --only hosting
```

## 124: What is the difference between API Gateway, Apigee and Cloud Endpoints?

- **API Gateway**: a simple, fully managed gateway for serverless backends (Cloud Run, functions). You describe the API with an OpenAPI spec and get API keys, JWT authentication and basic quotas.
- **Apigee**: a full API management platform with developer portals, monetization, analytics, advanced traffic policies and security. Used for large, external API programs.
- **Cloud Endpoints**: an older option based on the Extensible Service Proxy (ESP). Still works, but most new projects choose API Gateway or Apigee.

## 125: What is Google Cloud Marketplace?

Cloud Marketplace is a catalog of ready-made software from Google and third parties that you can deploy into your project: databases, monitoring tools, security products, VM images and Kubernetes apps.

Billing for many products goes through your Google Cloud billing account, which helps when a company already has a cloud budget or a committed spend agreement with Google.

## 126: What client libraries does Google Cloud offer?

Google provides idiomatic client libraries for Node.js, Python, Java, Go, C#, Ruby, PHP and C++. In Node.js each service is a separate package:

```bash
npm install @google-cloud/storage @google-cloud/pubsub @google-cloud/firestore @google-cloud/secret-manager
```

They handle authentication with ADC, retries with backoff for common errors, pagination and gRPC or REST transport. Prefer them over calling REST APIs by hand.

## 127: How do you test against Google Cloud services locally?

Some services have local emulators:

```bash
gcloud emulators firestore start --host-port=localhost:8080
gcloud beta emulators pubsub start --project=demo-project
```

Point the client library at the emulator with environment variables like `FIRESTORE_EMULATOR_HOST=localhost:8080` and `PUBSUB_EMULATOR_HOST=localhost:8085`. The Firebase Local Emulator Suite also runs Firestore, Auth, Storage, Pub/Sub and functions emulators together.

For services without emulators, use a separate dev project.

## 128: What is an SLA in Google Cloud?

A Service Level Agreement is Google's promise about a service's monthly uptime, for example 99.95% for a Cloud SQL HA instance or 99.999% for multi-region Spanner. If Google misses it, you can get service credits.

SLAs often depend on how you set things up. A single-zone VM has a lower SLA than a regional MIG, and Cloud SQL without HA has no availability SLA at all. Your own app's availability is limited by every service it depends on.

## 129: What is the shared responsibility model?

Google and the customer split security duties.

- **Google** is responsible for the physical data centers, hardware, network infrastructure and the managed parts of each service.
- **The customer** is responsible for their data, identities and IAM, app code, configuration (like public buckets or open firewalls) and, for IaaS, the guest OS.

The more managed the service, the more Google handles. A misconfigured IAM policy is always the customer's problem. Google also describes this as "shared fate", meaning it gives secure defaults and blueprints to help customers.

## 130: What is Cloud Asset Inventory?

Cloud Asset Inventory keeps a list of all resources and IAM policies in your organization, folders and projects, with history.

You can search for things like "all buckets with public access", "who has Owner on this folder" or "all VMs with external IPs", export the inventory to BigQuery or Cloud Storage, and get real-time change notifications through Pub/Sub.

```bash
gcloud asset search-all-resources --scope=organizations/123456789 --asset-types=storage.googleapis.com/Bucket
```

## 131: What is Active Assist and the Recommender?

Active Assist is a set of tools that analyze your usage and give recommendations through the Recommender API and the console. Examples:

- Resize or stop idle VMs
- Delete unattached disks and unused IP addresses
- Remove unused IAM permissions (IAM recommender)
- Buy committed use discounts
- Clean up idle projects

They are a quick way to cut costs and tighten security.

## 132: What is Security Command Center?

Security Command Center (SCC) is Google Cloud's central security and risk dashboard. It finds misconfigurations (public buckets, open firewall rules, keys in use), vulnerabilities, threats (crypto mining, suspicious IAM changes, malware) and compliance gaps.

It comes in Standard (basic, free), Premium and Enterprise tiers. Findings can be exported to SIEM tools or Pub/Sub for automatic responses.

## 133: What are organization policies?

Organization policies set guardrails on what can be configured in an organization, folder or project, no matter what IAM roles people have. Examples:

- `constraints/gcp.resourceLocations`: only allow resources in EU regions
- `constraints/iam.disableServiceAccountKeyCreation`: block service account keys
- `constraints/compute.vmExternalIpAccess`: block external IPs on VMs
- `constraints/storage.publicAccessPrevention`: block public buckets

IAM decides **who** can act. Organization policies decide **what** configurations are allowed at all.

## 134: What is Dataflow?

Dataflow is a managed service for running Apache Beam pipelines, for both batch and streaming data processing. It handles workers, autoscaling and fault tolerance.

A typical example is reading events from Pub/Sub, cleaning and aggregating them in time windows, and writing the results to BigQuery. You write pipelines in Java, Python or Go, or start from Google-provided templates without coding.

## 135: What is Dataproc?

Dataproc is a managed service for Apache Spark, Hadoop, Flink and related tools. You can create clusters in about 90 seconds and delete them when the job is done, or run Spark jobs with Dataproc Serverless without managing clusters at all.

It is the easiest way to move existing Spark or Hadoop jobs to Google Cloud. For new pipelines, teams often compare it with Dataflow and BigQuery.

## 136: What is Cloud Composer?

Cloud Composer is a managed Apache Airflow service. You write workflows (DAGs) in Python to schedule and orchestrate data pipelines: run a BigQuery query, start a Dataflow job, wait for a file in Cloud Storage and so on.

It is used for complex data pipelines with many dependencies. For simpler orchestration of APIs and services, Workflows is lighter and cheaper.

## 137: What is Gemini Enterprise Agent Platform (formerly Vertex AI)?

Vertex AI was Google Cloud's machine learning and generative AI platform. In April 2026 it was renamed and expanded as Gemini Enterprise Agent Platform. Many parts were renamed too, for example Vertex AI Studio became Agent Studio and Agent Engine became Agent Runtime. Old links redirect, and many docs and code samples still say Vertex AI.

It gives you access to Gemini and other models through Model Garden, tools for building and running agents, model training and tuning, vector search, evaluation and model serving endpoints. API usage is billed to your Google Cloud project.

## 138: What is the difference between calling Gemini through Google AI Studio and through Google Cloud?

- **Google AI Studio / Gemini Developer API**: you sign up with an API key and start fast. Good for prototypes and small apps.
- **Gemini on Google Cloud (Agent Platform)**: authentication with IAM and service accounts, data residency controls, VPC Service Controls, enterprise SLAs, quotas per project and billing through your cloud account.

The Google Gen AI SDK (`@google/genai` for JavaScript) supports both. You switch by configuration, not by rewriting code.

## 139: What are Gemini Code Assist and Gemini Cloud Assist?

- **Gemini Code Assist**: an AI coding assistant for IDEs (VS Code, JetBrains) and the terminal. It completes code, explains code and generates tests.
- **Gemini Cloud Assist**: an assistant inside the Google Cloud console. It helps you design architectures, troubleshoot issues, understand logs and costs, and write `gcloud` commands.

Both are paid add-ons for business use, with some free individual options.

## 140: How do you use a custom domain with Cloud Run?

Options:

1. **Global external Application Load Balancer** with a serverless NEG pointing to the service, plus a Google-managed certificate. This is the recommended production setup, and it also gives you Cloud CDN, Cloud Armor and multi-region routing.
2. **Firebase Hosting** with a rewrite to the Cloud Run service. Simple and includes a CDN.
3. **Cloud Run domain mappings**. Built in, but in preview, available only in some regions and with limitations.

## 141: How do you set environment variables on a Cloud Run service?

```bash
gcloud run deploy api --image=IMAGE --region=europe-west1 \
  --set-env-vars=NODE_ENV=production,LOG_LEVEL=info

gcloud run services update api --region=europe-west1 --update-env-vars=LOG_LEVEL=debug
```

Changing env vars creates a new revision. For secrets, do not use plain env vars. Reference Secret Manager instead with `--set-secrets=DB_PASSWORD=db-password:latest`.

## 142: What is the PORT environment variable in Cloud Run?

Cloud Run sends requests to your container on one port and sets the `PORT` environment variable to that port, `8080` by default. Your server must listen on `0.0.0.0` and the port from `PORT`:

```js
import express from "express";

const app = express();
app.get("/", (req, res) => res.send("ok"));

const port = Number(process.env.PORT) || 8080;
app.listen(port, "0.0.0.0", () => console.log(`Listening on ${port}`));
```

You can change the port with `--port`. A common startup error is a server listening on `localhost` or a hard-coded port, which makes the deploy fail with "container failed to start and listen on the port".

## 143: What does "scale to zero" mean in Cloud Run?

When a service has no traffic for a while, Cloud Run removes all its instances, and you pay nothing for compute with request-based billing. When a new request arrives, Cloud Run starts an instance, which adds startup latency (a cold start).

If you cannot accept cold starts, set a minimum number of instances (`--min-instances=1`). You then pay for idle instances, at a lower idle rate.

## 144: How do you get TLS certificates for your domains on Google Cloud?

- **Google-managed certificates**: Google issues and renews certificates for your domains automatically. Used with load balancers, through classic SSL certificate resources or Certificate Manager.
- **Certificate Manager**: a central service for managing many certificates, including wildcard certificates with DNS authorization and certificate maps for large numbers of domains.
- **Self-managed certificates**: you upload your own certificate and key.

Cloud Run `*.run.app` URLs and Firebase Hosting get HTTPS automatically.

## 145: How do common Google Cloud services map to AWS?

| Google Cloud               | AWS                      |
| -------------------------- | ------------------------ |
| Compute Engine             | EC2                      |
| Cloud Run                  | App Runner / ECS Fargate |
| Cloud Run functions        | Lambda                   |
| GKE                        | EKS                      |
| Cloud Storage              | S3                       |
| Cloud SQL                  | RDS                      |
| Firestore                  | DynamoDB (roughly)       |
| BigQuery                   | Redshift / Athena        |
| Pub/Sub                    | SNS + SQS                |
| Cloud Tasks                | SQS                      |
| Secret Manager             | Secrets Manager          |
| Cloud Logging / Monitoring | CloudWatch               |

One big difference: a Google Cloud VPC is global, while an AWS VPC is regional.

## 146: What are the Premium and Standard network tiers?

- **Premium Tier** (default): traffic enters and leaves Google's private global network at the edge location closest to the user, then travels on Google's backbone. Better performance and needed for global load balancers.
- **Standard Tier**: traffic travels over the public internet and enters Google's network close to the region where your resource runs. Cheaper egress, but higher latency and only regional load balancers.

Standard tier can make sense for cost-sensitive apps whose users are close to one region.

## 147: How can you connect an on-premises network to Google Cloud?

- **Cloud VPN (HA VPN)**: IPsec tunnels over the internet. Quick to set up, up to about 3 Gbps per tunnel, and a 99.99% SLA with the right setup.
- **Dedicated Interconnect**: a physical connection from your data center to Google at a colocation facility, 10 or 100 Gbps per link.
- **Partner Interconnect**: a connection through a service provider, from 50 Mbps up.
- **Cross-Cloud Interconnect**: a dedicated link between Google Cloud and another cloud.

All use Cloud Router with BGP to exchange routes.

## 148: How do you move large amounts of data into Google Cloud?

- `gcloud storage cp` or `rsync` for small to medium amounts over the network.
- **Storage Transfer Service**: managed transfers from other clouds (S3, Azure Blob), HTTP sources, on-prem file systems or between buckets, with scheduling.
- **Transfer Appliance**: a physical device Google ships to you for hundreds of terabytes or more when the network is too slow.
- **BigQuery Data Transfer Service**: scheduled loads into BigQuery from SaaS apps, other warehouses and Cloud Storage.
- **Database Migration Service**: for moving databases into Cloud SQL or AlloyDB.

## 149: How is Cloud Run billed?

It depends on the billing mode:

- **Request-based billing** (default): you pay for CPU and memory only while an instance is handling requests (plus startup and shutdown), plus a small fee per million requests.
- **Instance-based billing**: you pay for the whole lifetime of each instance, even between requests, but at a lower rate and with no per-request fee. Needed for background work outside requests.

Minimum instances are billed at an idle rate. There is a monthly free tier, and committed use discounts can lower the price for steady usage.

## 150: How do you shut down a project and what happens?

```bash
gcloud projects delete my-old-project
```

Shutting down a project stops billing and all resources in it, and the project is marked for deletion. For about 30 days you can restore it with `gcloud projects undelete`. After that, the project and all its data are deleted permanently and the project ID can never be used again.

Before deleting, check for shared resources other projects depend on, like Shared VPC host networks, service accounts used elsewhere, or DNS zones.

# Moderate Questions (151-300)

## 151: How would you set up projects and folders for a company with dev, staging and prod?

A common layout:

```text
Organization
├── Folder: shared        (networking host project, logging, CI/CD, artifact registry)
├── Folder: production    (one project per app or team: shop-prod, payments-prod)
├── Folder: non-production
│   ├── shop-staging
│   └── shop-dev
└── Folder: sandbox       (personal experiments, with budgets and auto-cleanup)
```

Use a separate project per environment and per app. Projects are the strongest isolation boundary for IAM, quotas and billing, so a mistake in dev cannot touch prod. Put strict organization policies and limited IAM on the production folder. Create projects with Terraform so they all get the same baseline (APIs, labels, budgets, log sinks).

## 152: How does IAM policy inheritance work?

The effective policy on a resource is the **union** of the allow policies set on it and on all its ancestors (project, folders, organization). If a group has Viewer on a folder, it has Viewer on every project and resource below.

You cannot remove an inherited permission with an allow policy lower in the tree. Allow policies only add. To block permissions you need IAM deny policies or principal access boundary policies (see questions 330-331). This is why you grant broad roles high in the tree only with great care.

## 153: When should you create a custom IAM role?

Create a custom role when the predefined roles give more permissions than needed. For example, a support tool that only needs to read Cloud Run service configs and logs, without seeing secrets.

```bash
gcloud iam roles create runConfigReader --project=my-project \
  --title="Cloud Run config reader" \
  --permissions=run.services.get,run.services.list,run.revisions.get,run.revisions.list \
  --stage=GA
```

Downsides: you must maintain custom roles yourself when Google adds new permissions, and some permissions cannot be used in custom roles. Do not make many near-identical custom roles. Prefer predefined roles when they fit.

## 154: What are IAM Conditions?

IAM Conditions add a CEL expression to a role binding, so the role applies only when the condition is true. Common uses are temporary access and limiting access to resources by name or tag.

```bash
gcloud projects add-iam-policy-binding my-project \
  --member="user:contractor@example.com" \
  --role="roles/storage.objectViewer" \
  --condition='expression=request.time < timestamp("2026-12-31T00:00:00Z") && resource.name.startsWith("projects/_/buckets/shared-reports"),title=temp-reports-access'
```

Not every service supports every condition attribute. Basic roles cannot be used with conditions, and policies with conditions need policy version 3.

## 155: Should you grant roles at the project level or on individual resources?

Prefer the smallest scope that works. If a service only needs to read one bucket, grant `roles/storage.objectViewer` on that bucket, not on the project. If a Cloud Run service calls only one other service, grant `roles/run.invoker` on that service.

Project-level grants are simpler but give access to every current and future resource of that type in the project. They are fine when the project itself is small and dedicated to one app. Resource-level grants are harder to see in one place, so use Cloud Asset Inventory or Policy Analyzer to review them.

## 156: What is service account impersonation?

Impersonation lets a user or another service account get short-lived credentials for a service account without a key. The caller needs `roles/iam.serviceAccountTokenCreator` on the target service account.

```bash
gcloud storage ls gs://prod-bucket --impersonate-service-account=deployer@my-project.iam.gserviceaccount.com
gcloud config set auth/impersonate_service_account deployer@my-project.iam.gserviceaccount.com
gcloud auth application-default login --impersonate-service-account=deployer@my-project.iam.gserviceaccount.com
```

Developers keep minimal personal permissions and impersonate a service account only when needed, and every impersonation is audit logged with the real caller's identity.

## 157: How do short-lived service account credentials work?

The IAM Service Account Credentials API can create, for a service account:

- **OAuth 2.0 access tokens** (default 1 hour) for calling Google APIs
- **OpenID Connect ID tokens** for calling services that check identity, like private Cloud Run services
- **Signed JWTs and signed blobs**, for example to create signed URLs without a key file

The caller needs the Token Creator role on the target account. Client libraries use this API automatically when you configure impersonation. Tokens expire on their own, so a leak is much less damaging than a leaked key.

## 158: How do you give a Cloud Run service access to other Google Cloud resources?

1. Create a dedicated service account for the service.
2. Grant it only the roles it needs on the right resources.
3. Deploy the service with that account.

```bash
gcloud iam service-accounts create orders-api
gcloud storage buckets add-iam-policy-binding gs://invoices \
  --member="serviceAccount:orders-api@my-project.iam.gserviceaccount.com" --role="roles/storage.objectCreator"
gcloud run deploy orders-api --image=IMAGE --region=europe-west1 \
  --service-account=orders-api@my-project.iam.gserviceaccount.com
```

The code uses ADC and gets tokens from the metadata server. No keys involved. The person deploying needs `roles/iam.serviceAccountUser` on that service account.

## 159: How do you let GitHub Actions deploy to Google Cloud without a key?

Use Workload Identity Federation. GitHub issues an OIDC token for each workflow run, and Google exchanges it for short-lived Google credentials.

```bash
gcloud iam workload-identity-pools create github --location=global
gcloud iam workload-identity-pools providers create-oidc github-provider \
  --location=global --workload-identity-pool=github \
  --issuer-uri="https://token.actions.githubusercontent.com" \
  --attribute-mapping="google.subject=assertion.sub,attribute.repository=assertion.repository" \
  --attribute-condition="assertion.repository_owner=='my-org'"

gcloud iam service-accounts add-iam-policy-binding deployer@my-project.iam.gserviceaccount.com \
  --role=roles/iam.workloadIdentityUser \
  --member="principalSet://iam.googleapis.com/projects/PROJECT_NUMBER/locations/global/workloadIdentityPools/github/attribute.repository/my-org/shop"
```

```yaml
permissions:
  id-token: write
  contents: read
steps:
  - uses: actions/checkout@v4
  - uses: google-github-actions/auth@v2
    with:
      workload_identity_provider: projects/PROJECT_NUMBER/locations/global/workloadIdentityPools/github/providers/github-provider
      service_account: deployer@my-project.iam.gserviceaccount.com
  - uses: google-github-actions/setup-gcloud@v2
  - run: gcloud run deploy api --image=IMAGE --region=europe-west1
```

You can also grant roles directly to the federated principal and skip the service account for services that support it.

## 160: How does Workload Identity Federation for GKE work?

It lets pods use IAM without keys. Each Kubernetes service account (KSA) gets an IAM identity, and the GKE metadata server on each node gives pods short-lived tokens for it.

The current approach is to grant IAM roles directly to the KSA principal:

```bash
gcloud storage buckets add-iam-policy-binding gs://reports \
  --role=roles/storage.objectViewer \
  --member="principal://iam.googleapis.com/projects/PROJECT_NUMBER/locations/global/workloadIdentityPools/my-project.svc.id.goog/subject/ns/billing/sa/reporter"
```

The older approach, still common, is to link the KSA to an IAM service account with the `iam.gke.io/gcp-service-account` annotation and give the KSA `roles/iam.workloadIdentityUser` on it. Autopilot has Workload Identity Federation turned on by default. On Standard you enable it on the cluster and node pools.

## 161: What does the Service Account User role do and why does it matter?

`roles/iam.serviceAccountUser` lets a principal **attach** a service account to a resource, using the `iam.serviceAccounts.actAs` permission. You need it to deploy a Cloud Run service, a VM or a function that runs as that service account.

This matters because attaching a powerful service account is a way to get its power. If a developer can deploy code that runs as an admin service account, they effectively are admin. Grant Service Account User on specific service accounts, not on the whole project.

## 162: How do you troubleshoot a "Permission denied" error?

1. Read the full error. It usually names the missing permission, like `run.services.update`, and the resource.
2. Check which identity actually made the call: your user, an impersonated account, or the service account attached to the workload.
3. Use **Policy Troubleshooter** in the console, or `gcloud policy-intelligence troubleshoot-policy iam`, to see why the principal does or does not have the permission. It also explains deny policies and conditions.
4. Check for organization policies, VPC Service Controls (the error mentions `VPC_SERVICE_CONTROLS`) and whether the API is enabled.
5. Remember IAM changes can take a few minutes to take effect.

## 163: Which organization policies would you set in a new organization?

A typical baseline:

- `iam.disableServiceAccountKeyCreation`: no service account keys
- `iam.automaticIamGrantsForDefaultServiceAccounts`: no Editor role for default service accounts
- `iam.allowedPolicyMemberDomains`: only identities from your domain can get IAM roles
- `storage.publicAccessPrevention` and `storage.uniformBucketLevelAccess`
- `compute.vmExternalIpAccess`: no external IPs on VMs (with exceptions)
- `compute.requireOsLogin` and `compute.skipDefaultNetworkCreation`
- `gcp.resourceLocations`: only allowed regions
- `sql.restrictPublicIp`

Use dry-run mode first to see what would be blocked before you enforce a policy.

## 164: What is concurrency in Cloud Run and how do you choose it?

Concurrency is the maximum number of requests one instance handles at the same time. The default is 80 and the maximum is 1000. When all instances are at their concurrency limit, Cloud Run starts more.

- I/O-bound apps (Node.js APIs that mostly wait on databases) can handle high concurrency, which means fewer instances and lower cost.
- CPU-heavy work or code that is not thread-safe needs low concurrency, sometimes 1.

```bash
gcloud run services update api --region=europe-west1 --concurrency=200 --cpu=2 --memory=1Gi
```

Load test to find a value where latency stays acceptable.

## 165: How do min and max instances work in Cloud Run?

- **Min instances** keeps a number of instances warm all the time to avoid cold starts. Idle instances are billed at a lower rate.
- **Max instances** caps how many instances can run. It protects downstream systems like a database with a connection limit, and it caps cost.

```bash
gcloud run services update api --region=europe-west1 --min-instances=2 --max-instances=50
```

When max instances is reached and all are busy, requests wait in a queue for a short time and can then fail with HTTP 429. You can also set min and max at the service level so they apply across all revisions.

## 166: What is the difference between request-based and instance-based billing in Cloud Run?

- **Request-based billing** (CPU only allocated during requests): CPU is throttled when no request is being handled. Cheapest for normal request/response APIs, but background work after sending the response may freeze.
- **Instance-based billing** (CPU always allocated): CPU is available for the whole instance lifetime. Use it for background tasks, in-process queues, WebSockets with server pushes or OpenTelemetry exporters that flush in the background.

```bash
gcloud run services update api --region=europe-west1 --no-cpu-throttling
```

A common bug is starting async work after `res.send()` with request-based billing. That work runs very slowly or not at all.

## 167: What causes cold starts on Cloud Run and how do you reduce them?

A cold start happens when a request needs a new instance. Cloud Run must pull the image, start the container and wait until your app listens on the port.

Ways to reduce them:

- Set `--min-instances` for latency-sensitive services
- Turn on startup CPU boost
- Use small base images and fewer dependencies
- Do less work at startup, and lazy-load rarely used modules
- Raise concurrency so fewer new instances are needed
- For Node.js, bundle the code and avoid heavy synchronous work at import time

## 168: What is startup CPU boost?

Startup CPU boost gives an instance extra CPU while it is starting up, so the app initializes faster. Cloud Run removes the extra CPU after startup.

```bash
gcloud run services update api --region=europe-west1 --cpu-boost
```

It helps most for runtimes with slow startup, like Java and Spring Boot or large Node.js apps. You pay for the extra CPU only during startup.

## 169: How do revisions and traffic splitting work in Cloud Run?

Each deploy or config change creates a new immutable **revision**. By default the newest revision gets 100% of traffic. You can instead split traffic between revisions to do a canary release:

```bash
gcloud run deploy api --image=IMAGE:v2 --region=europe-west1 --no-traffic
gcloud run services update-traffic api --region=europe-west1 --to-revisions=api-00042-abc=10
gcloud run services update-traffic api --region=europe-west1 --to-latest
```

To roll back, send 100% of traffic back to the previous revision. Old revisions stay available until you delete them, so rollbacks are instant.

## 170: What are revision tags in Cloud Run?

A tag gives a revision its own URL, like `https://green---api-123456789.europe-west1.run.app`, without sending it any normal traffic. You use it to test a new version in production before switching users to it.

```bash
gcloud run deploy api --image=IMAGE:v2 --region=europe-west1 --no-traffic --tag=green
# test https://green---api-...run.app
gcloud run services update-traffic api --region=europe-west1 --to-tags=green=100
```

This is a simple blue-green deployment on Cloud Run.

## 171: How does one Cloud Run service call another private Cloud Run service?

1. Deploy the target with `--no-allow-unauthenticated`.
2. Grant the caller's service account `roles/run.invoker` on the target.
3. In the caller, get an ID token with the target URL as the audience and send it in the `Authorization` header.

```js
import { GoogleAuth } from "google-auth-library";

const auth = new GoogleAuth();
const targetUrl = "https://billing-123456789.europe-west1.run.app";

const client = await auth.getIdTokenClient(targetUrl);
const res = await client.request({
  url: `${targetUrl}/invoices`,
  method: "POST",
  data: { orderId: "o-1" },
});
console.log(res.data);
```

Cloud Run checks the token and the IAM role before the request reaches your code.

## 172: What do the Cloud Run ingress settings do?

Ingress controls which network paths can reach the service:

- `all`: anyone on the internet can reach the URL (IAM still applies if the service is private).
- `internal`: only requests from VPC networks in the same project or Shared VPC, internal load balancers, and some Google services like Pub/Sub, Eventarc, Cloud Scheduler and Workflows.
- `internal-and-cloud-load-balancing`: internal traffic plus traffic through an external Application Load Balancer.

Use `internal-and-cloud-load-balancing` when you put Cloud Armor and a load balancer in front, so nobody can bypass them through the `run.app` URL.

## 173: How do you use Secret Manager secrets in Cloud Run?

You can expose a secret as an environment variable or mount it as a file:

```bash
gcloud run deploy api --image=IMAGE --region=europe-west1 \
  --set-secrets=DB_PASSWORD=db-password:latest,/secrets/firebase.json=firebase-config:3
```

The service account needs `roles/secretmanager.secretAccessor`. Env var secrets are read when the instance starts, so a new secret version is picked up only by new instances. Mounted files with `latest` are read on access, so they pick up new versions without a redeploy. Pin a specific version in production if you want controlled rollouts.

## 174: How do you mount a Cloud Storage bucket in Cloud Run?

Cloud Run supports volume mounts, including Cloud Storage FUSE:

```bash
gcloud run deploy api --image=IMAGE --region=europe-west1 \
  --add-volume=name=assets,type=cloud-storage,bucket=my-assets-bucket,readonly=true \
  --add-volume-mount=volume=assets,mount-path=/mnt/assets
```

Your code reads files from `/mnt/assets` like a normal folder. It is handy for config, ML models or static assets. It is not a real POSIX file system: there is no file locking, concurrent writes to the same file are unsafe, and performance is lower than local disk. Other volume types include in-memory volumes and NFS (Filestore).

## 175: What are sidecars in Cloud Run?

A Cloud Run service can run several containers in one instance. One is the ingress container that receives requests. The others are sidecars that share the network (localhost) and can share in-memory volumes.

Typical sidecars:

- An OpenTelemetry Collector or Prometheus sidecar for metrics
- A reverse proxy like Nginx or Envoy in front of the app
- The Cloud SQL Auth Proxy

You can set container start order with dependencies, so the app starts only after the sidecar is healthy.

## 176: What health checks does Cloud Run support?

- **Startup probe**: tells Cloud Run when the container has finished starting. By default it is a TCP check on the port. You can use an HTTP or gRPC check to wait for things like cache warm-up.
- **Liveness probe**: checks regularly that the container is still healthy. If it fails, Cloud Run restarts the instance.

```yaml
startupProbe:
  httpGet:
    path: /healthz/startup
  periodSeconds: 2
  failureThreshold: 30
livenessProbe:
  httpGet:
    path: /healthz/live
  periodSeconds: 10
```

This goes in the container spec of the service YAML, applied with `gcloud run services replace service.yaml`.

## 177: What is the maximum request timeout on Cloud Run and how do you handle long-running work?

The default request timeout is 5 minutes, and you can raise it up to 60 minutes with `--timeout=3600`. But keeping an HTTP request open for a long time is fragile: clients, proxies and load balancers may cut it, and retries can run the work twice.

Better patterns for long work:

- Return `202 Accepted` right away and process in a Cloud Run job, a Cloud Tasks task or a Pub/Sub consumer
- Store the job status in Firestore or a database, and let the client poll or listen for updates
- Split big work into smaller chunks

## 178: How do Cloud Run jobs run tasks in parallel?

A job execution runs a number of tasks (`--tasks`). Each task is a container instance that gets `CLOUD_RUN_TASK_INDEX` (0-based) and `CLOUD_RUN_TASK_COUNT` environment variables, which you use to split the work. `--parallelism` limits how many tasks run at once.

```bash
gcloud run jobs deploy resize-images --image=IMAGE --region=europe-west1 \
  --tasks=50 --parallelism=10 --max-retries=3 --task-timeout=30m
```

```js
const index = Number(process.env.CLOUD_RUN_TASK_INDEX ?? 0);
const count = Number(process.env.CLOUD_RUN_TASK_COUNT ?? 1);
const myFiles = allFiles.filter((_, i) => i % count === index);
```

Each failed task is retried separately, up to `--max-retries`.

## 179: How does Cloud Run connect to resources in a VPC?

Cloud Run runs outside your VPC by default. To reach private IPs (Memorystore, Cloud SQL private IP, internal services on VMs), there are two options:

- **Direct VPC egress** (recommended): Cloud Run instances get IPs directly from a subnet. No extra VMs to pay for, lower latency and higher throughput.
- **Serverless VPC Access connector** (older): a group of small managed VMs that forward traffic. Adds cost and is a throughput bottleneck, but uses fewer subnet IPs.

```bash
gcloud run deploy api --image=IMAGE --region=europe-west1 \
  --network=main --subnet=run-egress --vpc-egress=private-ranges-only
```

With `--vpc-egress=all-traffic`, internet traffic also goes through the VPC, which you use with Cloud NAT to get a static outbound IP.

## 180: How do you connect Cloud Run to Cloud SQL securely?

Common setup with the Node.js connector and IAM database auth:

```js
import {
  Connector,
  IpAddressTypes,
  AuthTypes,
} from "@google-cloud/cloud-sql-connector";
import pg from "pg";

const connector = new Connector();
const clientOpts = await connector.getOptions({
  instanceConnectionName: process.env.INSTANCE_CONNECTION_NAME, // my-project:europe-west1:main-db
  ipType: IpAddressTypes.PRIVATE,
  authType: AuthTypes.IAM,
});

const pool = new pg.Pool({
  ...clientOpts,
  user: "orders-api@my-project.iam", // IAM user for the service account
  database: "shop",
  max: 5,
});
```

The service account needs `roles/cloudsql.client` and `roles/cloudsql.instanceUser`. With private IP, the service also needs Direct VPC egress. Keep the pool small and remember that the total is pool size × max instances.

## 181: How do you put a load balancer in front of Cloud Run?

You use a serverless network endpoint group (NEG) as the backend of a global external Application Load Balancer:

```bash
gcloud compute network-endpoint-groups create api-neg --region=europe-west1 \
  --network-endpoint-type=serverless --cloud-run-service=api
gcloud compute backend-services create api-backend --global --load-balancing-scheme=EXTERNAL_MANAGED
gcloud compute backend-services add-backend api-backend --global \
  --network-endpoint-group=api-neg --network-endpoint-group-region=europe-west1
```

Then you add a URL map, a target HTTPS proxy with a managed certificate and a forwarding rule. This gives you a custom domain, a static IP, Cloud Armor, Cloud CDN, IAP and the ability to route to services in several regions.

## 182: How should a Cloud Run container handle shutdown?

When Cloud Run stops an instance (scale-in, new revision, maintenance), it sends `SIGTERM` and then waits 10 seconds before `SIGKILL`. Use that time to finish in-flight work, flush logs and traces, and close database connections.

```js
const server = app.listen(port);

process.on("SIGTERM", async () => {
  console.log("SIGTERM received, shutting down");
  server.close();
  await pool.end();
  process.exit(0);
});
```

Do not rely on this for long work. Ten seconds is short, and the process may not get CPU time with request-based billing outside of requests.

## 183: How do you write a function that runs when a file is uploaded to Cloud Storage?

```js
import functions from "@google-cloud/functions-framework";
import { Storage } from "@google-cloud/storage";

const storage = new Storage();

functions.cloudEvent("onUpload", async (cloudEvent) => {
  const { bucket, name, contentType } = cloudEvent.data;
  if (!contentType?.startsWith("image/")) return;
  console.log(`New image gs://${bucket}/${name}`);
  const [metadata] = await storage.bucket(bucket).file(name).getMetadata();
  console.log("Size:", metadata.size);
});
```

```bash
gcloud functions deploy onUpload --gen2 --runtime=nodejs22 --region=europe-west1 \
  --source=. --entry-point=onUpload \
  --trigger-event-filters="type=google.cloud.storage.object.v1.finalized" \
  --trigger-event-filters="bucket=my-uploads"
```

Be careful if the function writes back to the same bucket. It can trigger itself in a loop.

## 184: How do you process Pub/Sub messages with a Cloud Run function?

```js
import functions from "@google-cloud/functions-framework";

functions.cloudEvent("handleOrder", async (cloudEvent) => {
  const message = cloudEvent.data.message;
  const order = JSON.parse(Buffer.from(message.data, "base64").toString());
  console.log("Order", order.orderId, "attributes", message.attributes);
  await saveOrder(order);
});
```

```bash
gcloud functions deploy handleOrder --gen2 --runtime=nodejs22 --region=europe-west1 \
  --source=. --entry-point=handleOrder --trigger-topic=orders
```

The message data is base64-encoded. If the function throws (and retries are enabled), the message is redelivered, so make the handler idempotent.

## 185: What are the differences between Cloud Functions 1st gen and Cloud Run functions?

| Feature           | 1st gen                   | Cloud Run functions (formerly 2nd gen) |
| ----------------- | ------------------------- | -------------------------------------- |
| Runs on           | Legacy functions platform | Cloud Run                              |
| Concurrency       | 1 request per instance    | Up to 1000 per instance                |
| HTTP timeout      | 9 minutes                 | Up to 60 minutes                       |
| Max size          | 8 GB memory               | Up to 32 GiB memory, 8 vCPU            |
| Event sources     | Limited set               | Eventarc (many sources)                |
| Traffic splitting | No                        | Yes (through Cloud Run revisions)      |

Event-driven functions are still limited to 9 minutes in both. New functions should not use 1st gen.

## 186: How do retries work for event-driven functions?

By default event-driven functions are **not** retried. If the function fails, the event is dropped. With the `--retry` flag, failed events are retried with exponential backoff for up to 24 hours (for Pub/Sub, until message retention ends).

When retries are on:

- Make the handler idempotent, for example by storing processed event IDs (`cloudEvent.id`) in Firestore.
- Do not throw for errors that will never succeed, like bad input. Log them and return, or the event retries for a day.
- Use a dead-letter topic on the Pub/Sub subscription for messages that keep failing.

## 187: What is a VPC-native GKE cluster?

In a VPC-native cluster, pods and services get IP addresses from secondary ranges of the subnet (alias IPs). Pod IPs are real VPC addresses, so they are routable within the VPC and connected networks without extra routes.

It is required for many features, like Private Service Connect, container-native load balancing with NEGs (traffic goes straight to pods, not through node ports) and network policies. All new clusters are VPC-native by default. You must plan pod ranges carefully, because running out of pod IPs limits how many nodes you can add.

## 188: What is the difference between zonal and regional GKE clusters?

- **Zonal cluster**: one control plane replica in one zone. During control plane upgrades or a zone outage you cannot change the cluster (workloads keep running if nodes are fine).
- **Regional cluster**: control plane replicas in three zones, and nodes spread across zones by default. Upgrades do not take the control plane down, and the cluster survives a zone failure.

Use regional clusters for production. Autopilot clusters are always regional. Remember that in Standard regional clusters, `--num-nodes` is per zone, so `--num-nodes=2` gives 6 nodes.

## 189: What are node pools in GKE Standard?

A node pool is a group of nodes with the same configuration: machine type, disk, labels, taints, Spot or on-demand, GPU and so on. A cluster can have many node pools.

Uses:

- A general pool for normal workloads and a high-memory pool for caches
- A Spot pool for batch jobs with a taint so only tolerant pods land there
- A GPU pool for ML inference

```bash
gcloud container node-pools create spot-pool --cluster=main --region=europe-west1 \
  --machine-type=e2-standard-4 --spot --num-nodes=1 \
  --enable-autoscaling --min-nodes=0 --max-nodes=10 \
  --node-taints=workload=batch:NoSchedule
```

## 190: How do GKE release channels and upgrades work?

When you enroll a cluster in a release channel (Rapid, Regular, Stable or Extended), GKE upgrades the control plane and nodes automatically to versions tested for that channel. Regular is the default.

You control timing with:

- **Maintenance windows**: when upgrades may happen
- **Maintenance exclusions**: periods when they must not, like Black Friday
- **Surge upgrades or blue-green node pool upgrades**: how nodes are replaced

Watch deprecation insights before minor upgrades, because removed Kubernetes APIs can break your manifests.

## 191: How do you expose an app running on GKE?

- **Service type ClusterIP**: internal only, inside the cluster.
- **Service type LoadBalancer**: creates a passthrough Network Load Balancer (external, or internal with an annotation).
- **Ingress**: creates an Application Load Balancer for HTTP(S) routing.
- **Gateway API** (recommended for new setups): GKE Gateway controller creates load balancers from `Gateway` and `HTTPRoute` resources. It supports multi-cluster gateways, traffic splitting and cleaner role separation than Ingress.

```yaml
apiVersion: gateway.networking.k8s.io/v1
kind: HTTPRoute
metadata:
  name: api
spec:
  parentRefs:
    - name: external-gateway
  hostnames: ["api.example.com"]
  rules:
    - backendRefs:
        - name: api
          port: 8080
```

## 192: How does autoscaling work in GKE?

- **Horizontal Pod Autoscaler (HPA)**: changes the number of pod replicas based on CPU, memory or custom and external metrics (for example Pub/Sub backlog).
- **Vertical Pod Autoscaler (VPA)**: recommends or sets pod CPU and memory requests.
- **Cluster autoscaler**: adds nodes when pods cannot be scheduled and removes underused nodes (Standard).
- **Node auto-provisioning**: creates new node pools with the right machine type automatically (Standard).

In Autopilot, node scaling is handled for you. You only configure HPA and VPA for your pods.

## 193: What is a private GKE cluster?

In a private cluster, nodes have only internal IPs, so they cannot be reached from the internet. The control plane can have a public endpoint limited by authorized networks, or only a private endpoint.

Nodes need Cloud NAT to pull images from public registries, and Private Google Access to reach Google APIs and Artifact Registry. Newer GKE versions use a DNS-based control plane endpoint protected by IAM, which makes it easier to reach the API server of a private cluster without VPNs or bastion hosts.

## 194: How does GKE pull images from Artifact Registry?

Nodes use the node's service account to pull images. It needs `roles/artifactregistry.reader` on the repository (or project). If the cluster and the repository are in the same project and the node service account has the default permissions, it usually just works.

Common problems:

- A custom node service account without the reader role → `ImagePullBackOff` with a 403
- A private cluster without Private Google Access → timeouts
- A wrong image path, for example still using `gcr.io` names

Keep the repository in the same region as the cluster for faster pulls and no cross-region egress. GKE image streaming can also start large images faster.

## 195: What is Config Connector?

Config Connector is a Kubernetes add-on that lets you manage Google Cloud resources (buckets, Pub/Sub topics, Cloud SQL instances, IAM) as Kubernetes custom resources:

```yaml
apiVersion: storage.cnrm.cloud.google.com/v1beta1
kind: StorageBucket
metadata:
  name: my-project-reports
spec:
  location: EU
  uniformBucketLevelAccess: true
```

It constantly reconciles the real resource with the YAML, like other Kubernetes controllers. Teams that already use GitOps with Kubernetes (Argo CD, Config Sync) use it instead of Terraform. Config Controller is a hosted version.

## 196: How does autoscaling work for a managed instance group?

You attach an autoscaler to a MIG with a target, such as 60% average CPU, a load balancer serving capacity, a Cloud Monitoring metric or a schedule.

```bash
gcloud compute instance-groups managed set-autoscaling web-mig --region=europe-west1 \
  --min-num-replicas=2 --max-num-replicas=20 \
  --target-cpu-utilization=0.6 --cool-down-period=90
```

Set the initialization period (cool-down) to how long a VM takes to boot and become ready, so the autoscaler does not overreact. Predictive autoscaling can scale out ahead of daily traffic patterns, and scale-in controls limit how fast VMs are removed.

## 197: What are autohealing and rolling updates in MIGs?

**Autohealing** uses a health check to find VMs whose app is not responding, and recreates them. The health check should test the app, not just whether the VM is on.

**Rolling updates** replace VMs with a new instance template gradually:

```bash
gcloud compute instance-groups managed rolling-action start-update web-mig --region=europe-west1 \
  --version=template=web-template-v2 --max-surge=3 --max-unavailable=0
```

`max-surge` adds new VMs before removing old ones, and `max-unavailable=0` keeps full capacity during the update. You can also do a canary by giving a second template a target size, like 10%.

## 198: How do you choose between Cloud Run, GKE, Compute Engine and Cloud Run functions?

- **Cloud Run functions**: small event handlers and webhooks, one function per job.
- **Cloud Run**: most stateless HTTP services and jobs. No cluster to run, scales to zero and has the least operations work.
- **GKE**: many services with complex needs: service mesh, custom controllers, stateful sets, special networking, GPUs at scale, or teams already invested in Kubernetes.
- **Compute Engine**: software that needs full OS control, licensed software tied to machines, legacy apps, or very specific hardware.

A good default for a web team is "Cloud Run unless there is a clear reason not to".

## 199: How do Cloud Build triggers work?

A trigger starts a build automatically on an event, usually a push to a branch, a new tag or a pull request in a connected repository (GitHub, GitLab, Bitbucket). It can also run manually, from a Pub/Sub message or a webhook.

```bash
gcloud builds triggers create github --name=api-main --region=europe-west1 \
  --repository=projects/my-project/locations/europe-west1/connections/github/repositories/shop \
  --branch-pattern="^main$" --build-config=cloudbuild.yaml \
  --included-files="services/api/**" \
  --service-account=projects/my-project/serviceAccounts/builder@my-project.iam.gserviceaccount.com
```

`--included-files` lets a monorepo build only the services that changed. Always set a dedicated build service account with minimal roles.

## 200: What are Cloud Build private pools?

By default builds run in a Google-managed default pool on the public internet. A **private pool** is a set of build workers dedicated to you that can be peered with your VPC.

Use private pools when builds need to reach private resources (a private GKE cluster, an internal package registry, a database for integration tests), when you need specific machine types, or when you need a static egress IP or VPC Service Controls support.

## 201: What is the difference between building with a Dockerfile and with buildpacks?

- **Dockerfile**: you control every layer: base image, build steps, users, multi-stage builds. More control, but you maintain it.
- **Google Cloud buildpacks**: detect your language (`package.json`, `requirements.txt`, `go.mod`) and build a production image automatically, with secure base images that Google updates. `gcloud run deploy --source .` uses them when there is no Dockerfile.

A good Node.js Dockerfile:

```dockerfile
FROM node:22-slim AS build
WORKDIR /app
COPY package*.json ./
RUN npm ci
COPY . .
RUN npm run build && npm prune --omit=dev

FROM node:22-slim
WORKDIR /app
ENV NODE_ENV=production
COPY --from=build /app/node_modules ./node_modules
COPY --from=build /app/dist ./dist
USER node
CMD ["node", "dist/server.js"]
```

## 202: How do you set up a delivery pipeline with Cloud Deploy?

```yaml
# clouddeploy.yaml
apiVersion: deploy.cloud.google.com/v1
kind: DeliveryPipeline
metadata:
  name: api
serialPipeline:
  stages:
    - targetId: staging
    - targetId: prod
---
apiVersion: deploy.cloud.google.com/v1
kind: Target
metadata:
  name: prod
requireApproval: true
run:
  location: projects/shop-prod/locations/europe-west1
```

```bash
gcloud deploy apply --file=clouddeploy.yaml --region=europe-west1
gcloud deploy releases create rel-1-4-0 --delivery-pipeline=api --region=europe-west1 \
  --images=api=europe-west1-docker.pkg.dev/my-project/apps/api:1.4.0
gcloud deploy releases promote --release=rel-1-4-0 --delivery-pipeline=api --region=europe-west1
```

The release renders manifests once, so the exact same artifact is promoted from staging to prod.

## 203: How do you do a canary deployment with Cloud Deploy?

Add a canary strategy to the stage:

```yaml
serialPipeline:
  stages:
    - targetId: prod
      strategy:
        canary:
          runtimeConfig:
            cloudRun:
              automaticTrafficControl: true
          canaryDeployment:
            percentages: [10, 50]
            verify: true
```

Cloud Deploy first sends 10% of traffic to the new revision, runs verification if set, waits for you (or an automation) to advance, then goes to 50%, then 100%. If something goes wrong you roll back to the previous release. For GKE it works with Gateway API or Service-based traffic splitting.

## 204: What are remote and virtual repositories in Artifact Registry?

- **Standard repository**: you push your own artifacts.
- **Remote repository**: a caching proxy for an upstream like Docker Hub, npmjs or PyPI. Builds pull through it, so you avoid Docker Hub rate limits and keep working if the upstream is down.
- **Virtual repository**: one endpoint that combines several standard and remote repositories with a priority order.

A common setup is a virtual npm repo that checks your private packages first and then a remote npmjs cache. This also helps against dependency confusion attacks.

## 205: How does vulnerability scanning work in Artifact Registry?

When you enable the Container Scanning API, Artifact Registry scans images when they are pushed and keeps checking them for new vulnerabilities for a period after that. It finds known CVEs in OS packages and language packages (Node.js, Python, Java, Go).

```bash
gcloud artifacts docker images list europe-west1-docker.pkg.dev/my-project/apps --show-occurrences
gcloud artifacts docker images describe europe-west1-docker.pkg.dev/my-project/apps/api:1.4.0 --show-package-vulnerability
```

You can also scan on demand in CI with `gcloud artifacts docker images scan`, and fail the build or block deploys with Binary Authorization when critical issues are found.

## 206: How do you store Terraform state on Google Cloud?

Use a Cloud Storage bucket as the backend:

```hcl
terraform {
  backend "gcs" {
    bucket = "acme-terraform-state"
    prefix = "shop/prod"
  }
}
```

The GCS backend supports state locking, so two people cannot apply at once. Turn on object versioning so you can recover an old state file, restrict IAM on the bucket (state can contain secrets), and use a separate prefix or bucket per environment.

## 207: What is the difference between the google and google-beta Terraform providers?

- `google` supports GA features of Google Cloud services.
- `google-beta` also supports beta features and fields.

You use `google-beta` only for resources that need it, by setting `provider = google-beta` on those resources. Both should be on the same version. Beta features can change, so keep their use small in production code.

## 208: How should Terraform authenticate to Google Cloud?

- **Locally**: run `gcloud auth application-default login`, ideally with impersonation of a deployer service account, so your personal account does not need broad roles.
- **In CI**: use Workload Identity Federation (GitHub Actions, GitLab, others) or run in Cloud Build with a build service account.
- **Never** commit key files or put them in CI variables if you can avoid it.

```hcl
provider "google" {
  project                     = "shop-prod"
  region                      = "europe-west1"
  impersonate_service_account = "terraform@shop-admin.iam.gserviceaccount.com"
}
```

## 209: How do you let a browser upload a file directly to Cloud Storage?

Your backend creates a V4 signed URL for a `PUT` and returns it. The browser uploads straight to Cloud Storage, so large files never pass through your server.

```js
// Backend (Cloud Run)
const [uploadUrl] = await storage
  .bucket("my-app-uploads")
  .file(`users/${userId}/${crypto.randomUUID()}.jpg`)
  .getSignedUrl({
    version: "v4",
    action: "write",
    expires: Date.now() + 10 * 60 * 1000,
    contentType: "image/jpeg",
  });
```

```js
// Browser
await fetch(uploadUrl, {
  method: "PUT",
  headers: { "Content-Type": "image/jpeg" },
  body: file,
});
```

On Cloud Run there is no key file, so the library signs through the IAM `signBlob` API. The service account needs `roles/iam.serviceAccountTokenCreator` on itself. You also need a CORS config on the bucket.

## 210: What are resumable uploads in Cloud Storage?

A resumable upload starts a session, and the file is sent in chunks. If the connection drops, you continue from the last confirmed byte instead of starting again. It is recommended for files larger than about 8 MB or for unreliable networks like mobile.

The Node.js library uses resumable uploads by default for `file.save()` and `createWriteStream()`. For browser uploads, the backend can create the session URL with `file.createResumableUpload()` and send it to the client.

## 211: How do you configure CORS on a Cloud Storage bucket?

```json
[
  {
    "origin": ["https://app.example.com"],
    "method": ["GET", "PUT"],
    "responseHeader": ["Content-Type"],
    "maxAgeSeconds": 3600
  }
]
```

```bash
gcloud storage buckets update gs://my-app-uploads --cors-file=cors.json
```

CORS is needed when JavaScript in the browser calls Cloud Storage directly, for example uploads with signed URLs. Use your real origins instead of `*`.

## 212: What consistency does Cloud Storage provide?

Cloud Storage is strongly consistent for object operations: after a successful write, overwrite or delete, any following read or list returns the latest data, worldwide. This includes listing objects in a bucket.

One catch is caching. Publicly readable objects can be cached by Google's edge caches and browsers according to `Cache-Control` (default `public, max-age=3600`), so users may see an old version after an overwrite. Set `Cache-Control: no-cache` or use versioned file names for files that change.

## 213: How do you get notified when objects change in Cloud Storage?

Two main options:

- **Eventarc / Cloud Run function triggers** on events like `google.cloud.storage.object.v1.finalized` (created or overwritten) and `deleted`.
- **Pub/Sub notifications** configured on the bucket:

```bash
gcloud storage buckets notifications create gs://my-uploads --topic=uploads --event-types=OBJECT_FINALIZE
```

Delivery is at least once, so handlers must cope with duplicates. Filter by prefix (`--object-prefix`) to avoid triggering on files your own code writes.

## 214: What is Autoclass in Cloud Storage?

Autoclass moves each object automatically between storage classes based on access: objects start in Standard, move to Nearline after 30 days without access, then Coldline and optionally Archive. If an object is read, it moves back to Standard.

There are no early deletion or retrieval fees for Autoclass transitions, only a small management fee per object. It is useful when you cannot predict how data will be accessed. If access patterns are known, lifecycle rules can be cheaper.

## 215: What are retention policies, object holds and Bucket Lock?

- **Retention policy**: objects cannot be deleted or overwritten until they reach a minimum age (for example 7 years for financial records).
- **Bucket Lock**: locking the retention policy makes it permanent. Nobody, including project owners, can shorten or remove it. Used for WORM compliance (SEC, FINRA).
- **Object holds**: event-based or temporary holds that prevent deletion of individual objects, for example during a legal case.
- **Object Retention Lock**: retention settings per object instead of per bucket.

Be careful, a locked bucket cannot be deleted until all objects expire.

## 216: How do you get good performance from Cloud Storage at high request rates?

- Cloud Storage starts a bucket with a limited request rate per key range (about 1,000 writes and 5,000 reads per second) and scales up automatically as load grows. Ramp up traffic gradually instead of jumping straight to huge rates.
- Avoid sequential name prefixes like timestamps (`2026-10-29-10-00-01.log`) at very high rates. They put all writes on one key range. Add a hash prefix if needed.
- Use parallel composite uploads and sliced downloads for very large files (`gcloud storage` does this automatically).
- Keep compute in the same region as the bucket.
- Reuse client objects and connections.

## 217: What costs are there besides storage in Cloud Storage?

- **Operations**: Class A (writes, lists) and Class B (reads) are charged per 10,000 operations, higher for colder classes.
- **Retrieval fees** for Nearline, Coldline and Archive.
- **Early deletion fees** if you delete before the minimum storage duration.
- **Network egress** to the internet or other regions. Data transfer to Google services in the same region is often free.
- **Replication** for dual-region and multi-region buckets.
- **Soft delete and noncurrent versions** stored.

A bucket with millions of tiny files can cost more in operations than in storage.

## 218: What is the difference between Cloud SQL Enterprise and Enterprise Plus editions?

- **Enterprise**: the standard edition. 99.95% SLA for HA instances, good for most apps.
- **Enterprise Plus**: for demanding workloads. 99.99% SLA, faster machine types, a data cache on local SSD for faster reads, near-zero downtime maintenance (under a second in many cases), longer point-in-time recovery retention and other advanced features.

Enterprise Plus costs more. You can upgrade an existing MySQL or PostgreSQL instance from Enterprise to Enterprise Plus with a short downtime.

## 219: Should Cloud SQL use a public IP or a private IP?

**Private IP** is recommended. The instance gets an address in your VPC (through private services access or Private Service Connect), so traffic never goes over the internet and there is nothing to attack from outside.

**Public IP** works if you use the Cloud SQL Auth Proxy or connectors with no authorized networks, because they authenticate with IAM and use TLS. Never open authorized networks to `0.0.0.0/0`. You can enforce private IP with the `sql.restrictPublicIp` organization policy.

## 220: What is IAM database authentication in Cloud SQL?

It lets users and service accounts log into PostgreSQL or MySQL with their IAM identity instead of a database password. The client uses a short-lived OAuth token as the password, and Cloud SQL checks it.

```bash
gcloud sql users create orders-api@my-project.iam --instance=main-db --type=cloud_iam_service_account
```

Then grant normal database privileges to that user with `GRANT`. Benefits: no passwords to store or rotate, and access is removed when the IAM identity is removed. The connectors and the Auth Proxy with `--auto-iam-authn` handle the token automatically.

## 221: How do you handle database connections from serverless apps to Cloud SQL?

Each Cloud Run instance opens its own connection pool, so the total number of connections is pool size × number of instances. With autoscaling this can easily go over the database's `max_connections`.

Ways to control it:

- Keep pools small (2-10) and reuse them across requests (create the pool once, outside the handler)
- Set `--max-instances` to match what the database can handle
- Use Cloud SQL managed connection pooling (Enterprise Plus) or PgBouncer in front of PostgreSQL
- Set connection timeouts and close idle connections

## 222: How do Cloud SQL maintenance windows work?

Google needs to apply updates (OS, database minor versions) to instances. You choose a maintenance window (day and hour) and an order (earlier or later in the rollout). You can also set deny periods of up to 90 days when no maintenance happens, for example during a big sales event.

Maintenance causes a short downtime: usually under a minute for Enterprise, and under a second for Enterprise Plus in most cases. Apps should retry failed connections so they recover automatically. You can also trigger maintenance yourself early.

## 223: How do you recover from an accidental data deletion in Cloud SQL?

If point-in-time recovery is on, you clone the instance to a time just before the mistake:

```bash
gcloud sql instances clone main-db main-db-recovered \
  --point-in-time="2026-10-28T14:29:00Z"
```

Then you copy the lost rows from the clone back to the main instance (or switch the app to the clone if needed). Cloning does not touch the original instance, so it is safe to try several timestamps. Without PITR, you can only restore the last backup, which loses everything after it.

## 224: How do you migrate an existing database to Cloud SQL?

Use **Database Migration Service (DMS)**. It sets up continuous replication from a source (on-prem MySQL or PostgreSQL, Amazon RDS, another Cloud SQL) to a new Cloud SQL or AlloyDB instance:

1. Create a connection profile for the source.
2. Create a migration job. DMS does an initial full dump and then keeps replicating changes (CDC).
3. Test the app against the destination.
4. Stop writes on the source, wait for replication to catch up, and switch the app over (promote).

Downtime is only the final switch. For heterogeneous migrations (like Oracle to PostgreSQL), DMS also helps convert schemas.

## 225: How do indexes work in Firestore?

Firestore creates **single-field indexes** automatically for every field, so simple queries like `where("plan", "==", "pro")` work out of the box.

Queries that combine several fields, like an equality filter plus `orderBy` on a different field, need a **composite index**. If one is missing, the query fails with an error that includes a link to create it. You can also define indexes in `firestore.indexes.json` and deploy them with the Firebase CLI or Terraform.

You can add single-field index exemptions for large fields you never query, like long text, to save storage and write costs.

## 226: What is the difference between transactions and batched writes in Firestore?

- **Transaction**: reads and then writes based on what was read. If any read document changes before commit, the transaction retries. Server SDKs use pessimistic locks.
- **Batched write**: a group of writes (set, update, delete) with no reads, all applied atomically.

```js
await db.runTransaction(async (tx) => {
  const ref = db.collection("products").doc("p1");
  const snap = await tx.get(ref);
  const stock = snap.get("stock");
  if (stock < 1) throw new Error("Out of stock");
  tx.update(ref, { stock: stock - 1 });
  tx.create(db.collection("orders").doc(), {
    productId: "p1",
    createdAt: FieldValue.serverTimestamp(),
  });
});
```

In a transaction, all reads must happen before writes.

## 227: What are Firestore Security Rules?

Security Rules control access when clients (web and mobile apps) call Firestore directly with the Firebase SDK. They are not used for server SDKs, which use IAM and bypass rules.

```text
rules_version = '2';
service cloud.firestore {
  match /databases/{database}/documents {
    match /users/{userId} {
      allow read, update: if request.auth != null && request.auth.uid == userId;
    }
    match /posts/{postId} {
      allow read: if true;
      allow create: if request.auth != null && request.resource.data.authorId == request.auth.uid;
    }
  }
}
```

Rules are not filters. A query must only ask for documents the user is allowed to read, or the whole query fails. Test rules with the emulator.

## 228: How do real-time listeners work in Firestore?

A listener subscribes to a document or a query and gets the initial result followed by updates whenever matching data changes:

```js
const unsubscribe = db
  .collection("orders")
  .where("status", "==", "pending")
  .onSnapshot((snapshot) => {
    snapshot
      .docChanges()
      .forEach((change) => console.log(change.type, change.doc.id));
  });
```

Each changed document counts as a read. Listeners are mostly used in web and mobile clients for live UIs. On a backend, prefer Eventarc triggers or Pub/Sub, because a long-lived listener in a scale-to-zero service does not work well.

## 229: What limits should you know when designing for Firestore?

- Maximum document size: 1 MiB
- Sustained writes to a single document: about 1 per second recommended. Higher rates cause contention.
- New collections with sequential keys or indexed timestamp fields: write rate is limited until Firestore splits the range, so ramp up traffic gradually (the "500/50/5" rule).
- Each composite and single-field index adds write cost.
- Queries cannot do joins, and some inequality and `OR` combinations need composite indexes.
- Maximum depth of subcollections: 100.

Design documents around your read patterns, and avoid hot documents like a global counter.

## 230: How do you paginate results in Firestore?

Use query cursors, not offsets. Offsets still read (and bill for) the skipped documents.

```js
const pageSize = 20;
let query = db.collection("posts").orderBy("createdAt", "desc").limit(pageSize);

const first = await query.get();
const last = first.docs.at(-1);

const next = await db
  .collection("posts")
  .orderBy("createdAt", "desc")
  .startAfter(last)
  .limit(pageSize)
  .get();
```

For an API, return the last document's ID or sort values as an opaque cursor, and use `startAfter` with those values on the next call.

## 231: What are TTL policies in Firestore?

A TTL policy deletes documents automatically after a timestamp field's time has passed. You pick a field, for example `expireAt`, and Firestore deletes documents whose `expireAt` is in the past.

```bash
gcloud firestore fields ttls update expireAt --collection-group=sessions --enable-ttl
```

Deletion is not instant. It usually happens within 24 hours after expiry, so your queries should still filter out expired documents. TTL deletes are billed like normal deletes. It is great for sessions, temporary tokens and logs.

## 232: What is Firestore with MongoDB compatibility?

It is a Firestore option (in the Enterprise edition) that accepts the MongoDB wire protocol, so you can use existing MongoDB drivers, tools and much of your MongoDB code with a serverless Google Cloud database.

```js
import { MongoClient } from "mongodb";

const client = new MongoClient(process.env.FIRESTORE_MONGODB_URI);
const orders = client.db("shop").collection("orders");
await orders.insertOne({ userId: "u1", total: 49.99 });
```

It does not support every MongoDB feature, so check the compatibility list before migrating. It is useful for teams moving from self-hosted MongoDB or Atlas who want a fully managed, scale-to-zero option.

## 233: Which Memorystore option should you pick?

- **Memorystore for Valkey**: open source, Redis-compatible, cluster mode, the default choice for new projects that want to avoid the Redis license change.
- **Memorystore for Redis Cluster**: sharded Redis with zero-downtime scaling and high throughput.
- **Memorystore for Redis** (instances): simpler single-shard Redis, Basic (no replica) or Standard (with failover). Many existing apps use it.
- **Memorystore for Memcached**: plain caching with no persistence or replication.

Cluster options need clients that support cluster mode. Use Standard tier or cluster replicas in production for failover.

## 234: How do you use Memorystore as a cache from Cloud Run?

Cloud Run needs network access to the instance's private IP, usually with Direct VPC egress:

```bash
gcloud run deploy api --image=IMAGE --region=europe-west1 \
  --network=main --subnet=run-egress --vpc-egress=private-ranges-only \
  --set-env-vars=REDIS_HOST=10.20.0.3
```

```js
import { createClient } from "redis";

const redis = createClient({ url: `redis://${process.env.REDIS_HOST}:6379` });
await redis.connect();

async function getProduct(id) {
  const cached = await redis.get(`product:${id}`);
  if (cached) return JSON.parse(cached);
  const product = await db.getProduct(id);
  await redis.set(`product:${id}`, JSON.stringify(product), { EX: 300 });
  return product;
}
```

Create the client once per instance. Turn on AUTH and in-transit encryption for production.

## 235: What is table partitioning in BigQuery?

Partitioning splits a table into segments, usually by date (a `DATE` or `TIMESTAMP` column, or ingestion time) or by an integer range. Queries that filter on the partition column only scan the matching partitions, which lowers cost and speeds things up.

```sql
CREATE TABLE shop.events (
  event_time TIMESTAMP,
  user_id STRING,
  event_name STRING
)
PARTITION BY DATE(event_time)
OPTIONS (partition_expiration_days = 400, require_partition_filter = TRUE);
```

`require_partition_filter` forces users to filter by date, so nobody scans the full table by accident.

## 236: What is clustering in BigQuery?

Clustering sorts data inside a table (or inside each partition) by up to four columns. When a query filters or aggregates on those columns, BigQuery can skip blocks that do not match.

```sql
CREATE TABLE shop.events
PARTITION BY DATE(event_time)
CLUSTER BY user_id, event_name
AS SELECT * FROM shop.events_raw;
```

Partition by time, and cluster by columns you often filter on with high cardinality, like `user_id` or `customer_id`. BigQuery reclusters automatically in the background for free. With clustering, the cost estimate before running may be higher than the real cost.

## 237: How does BigQuery pricing work?

**Storage**: per GiB per month. Data not modified for 90 days becomes long-term storage at about half price. You can choose logical or physical (compressed) storage billing per dataset.

**Compute**, two models:

- **On-demand**: pay per TiB of data scanned by queries ($6.25 per TiB in US multi-region, first 1 TiB per month free).
- **Capacity (editions)**: Standard, Enterprise or Enterprise Plus. You pay for slots (units of compute) per hour, with autoscaling and optional commitments.

Streaming inserts and Storage Write API usage are charged separately. Batch loading from Cloud Storage is free.

## 238: How do you reduce BigQuery query costs?

- Select only the columns you need. Avoid `SELECT *`. BigQuery is columnar and bills by columns scanned.
- Partition tables and filter on the partition column. Cluster on common filter columns.
- `LIMIT` does **not** reduce scanned data on normal tables.
- Use the dry run or the query validator to see bytes scanned before running.
- Set `maximum_bytes_billed` on queries and custom quotas per user or project.
- Use materialized views or summary tables for dashboards that run the same aggregation often.
- Consider editions with slot reservations when on-demand spend is high and steady.

## 239: How do you stream data into BigQuery?

The recommended way is the **Storage Write API**. It has higher throughput and lower cost than the legacy `insertAll` streaming API, and supports exactly-once delivery with committed streams.

Other options:

- **Pub/Sub BigQuery subscription**: writes messages from a topic straight into a table, with no code.
- **Dataflow**: when you need transformations before writing.
- Legacy `tabledata.insertAll` (`table.insert()` in Node.js): still works and is simple, but costs more.

```js
await bigquery
  .dataset("shop")
  .table("events")
  .insert([
    { event_time: new Date().toISOString(), user_id: "u1", event_name: "view" },
  ]);
```

## 240: How do you prevent SQL injection when querying BigQuery from an app?

Use query parameters, never string building:

```js
const [rows] = await bigquery.query({
  query: `SELECT order_id, total FROM \`shop.orders\` WHERE user_id = @userId AND status IN UNNEST(@statuses)`,
  params: { userId: req.user.id, statuses: ["paid", "shipped"] },
});
```

Parameters can be scalars, arrays and structs. You cannot use parameters for table or column names. For those, check values against an allowlist in code before inserting them into the SQL.

## 241: What are external tables and BigLake tables in BigQuery?

- **External tables** let you query data that lives outside BigQuery storage, like CSV, JSON, Parquet or Avro files in Cloud Storage, or Google Sheets, without loading it.
- **BigLake tables** are an improved kind of external table. Access goes through a connection with its own service account, so users do not need access to the bucket. They support fine-grained security (row and column level), metadata caching for speed and open formats like Apache Iceberg.

External queries are slower than native tables. They fit data lakes where many engines (Spark, BigQuery) share the same files.

## 242: What are scheduled queries and materialized views in BigQuery?

- **Scheduled queries** run a SQL statement on a schedule (for example every hour) and write the result to a table. They use the BigQuery Data Transfer Service. Good for building daily summary tables.
- **Materialized views** store the precomputed result of a query and are refreshed automatically and incrementally when the base table changes. BigQuery can even rewrite queries on the base table to use the materialized view.

```sql
CREATE MATERIALIZED VIEW shop.daily_sales AS
SELECT DATE(created_at) AS day, SUM(total) AS revenue, COUNT(*) AS orders
FROM shop.orders
GROUP BY day;
```

## 243: How do you control access to specific rows and columns in BigQuery?

- **Authorized views**: a view in one dataset can read a table in another dataset that users cannot access directly. Users only see what the view returns.
- **Row-level security**: row access policies filter rows by user or group.
- **Column-level security**: policy tags from Data Catalog (Dataplex) restrict access to sensitive columns like email or salary.
- **Dynamic data masking**: users see masked values (for example a hash) instead of the real value.

```sql
CREATE ROW ACCESS POLICY eu_only ON shop.orders
GRANT TO ("group:eu-analysts@example.com")
FILTER USING (region = "EU");
```

## 244: What is a dead-letter topic in Pub/Sub?

A dead-letter topic receives messages that a subscription failed to deliver after a maximum number of attempts (between 5 and 100). Without it, a "poison" message that always fails keeps being redelivered until it expires.

```bash
gcloud pubsub subscriptions update orders-worker \
  --dead-letter-topic=orders-dead-letter --max-delivery-attempts=10
```

The Pub/Sub service agent needs publisher rights on the dead-letter topic and subscriber rights on the source subscription. Add a subscription on the dead-letter topic too, otherwise those messages are lost. Then alert on its size and inspect or replay the messages.

## 245: How does the retry policy work on a Pub/Sub subscription?

By default, Pub/Sub redelivers a nacked or expired message right away. This can hammer a struggling backend. You can set an exponential backoff retry policy instead:

```bash
gcloud pubsub subscriptions update orders-worker --min-retry-delay=10s --max-retry-delay=600s
```

The delay grows between attempts for the same message, from the minimum up to the maximum. It is a good default together with a dead-letter topic.

## 246: How do ordering keys work in Pub/Sub?

If you publish messages with the same ordering key, and the subscription has message ordering enabled, subscribers receive those messages in the order they were published (within one region).

```js
const topic = pubsub.topic("account-events", { messageOrdering: true });
await topic.publishMessage({
  json: { type: "deposit", amount: 100 },
  orderingKey: "account-42",
});
```

```bash
gcloud pubsub subscriptions create account-events-sub --topic=account-events --enable-message-ordering
```

Ordering is per key, not global, so use keys like a user or account ID. If a publish with a key fails, later publishes with that key are paused until you call `topic.resumePublishing(key)`. Ordering lowers throughput per key.

## 247: What is exactly-once delivery in Pub/Sub?

With exactly-once delivery enabled on a pull subscription, Pub/Sub guarantees that a message is not redelivered after it has been acknowledged successfully, and that it is not redelivered while its ack deadline is still valid.

```bash
gcloud pubsub subscriptions create payments-sub --topic=payments --enable-exactly-once-delivery
```

Your code must check the ack result. In Node.js, use `await message.ackWithResponse()` and handle failures. It works only for pull subscriptions within one region, and it adds latency. Duplicate publishes from the publisher side are still possible, so idempotent processing is still a good idea.

## 248: How do you filter messages on a Pub/Sub subscription?

A filter on message attributes means the subscription only receives matching messages. Others are acknowledged automatically and never delivered.

```bash
gcloud pubsub subscriptions create eu-orders --topic=orders \
  --message-filter='attributes.region = "eu" AND attributes.type = "order.created"'
```

Filters work only on attributes, not on the message body, so publishers must set useful attributes. The filter cannot be changed after creation. You still pay for the filtered-out messages.

## 249: What are BigQuery and Cloud Storage subscriptions in Pub/Sub?

They are export subscriptions that write messages directly to a destination without any subscriber code:

- **BigQuery subscription**: writes each message as a row to a table. It can use the topic schema or table schema to map fields.
- **Cloud Storage subscription**: batches messages into files (text or Avro) in a bucket, based on time or size.

```bash
gcloud pubsub subscriptions create events-to-bq --topic=events \
  --bigquery-table=my-project:analytics.events --use-table-schema
```

They replace a lot of simple Dataflow jobs that only moved data from Pub/Sub to storage.

## 250: What are Pub/Sub schemas?

A schema (Avro or Protocol Buffers) attached to a topic defines the format of messages. Pub/Sub rejects published messages that do not match it, so bad data never reaches subscribers.

```bash
gcloud pubsub schemas create order-schema --type=avro --definition-file=order.avsc
gcloud pubsub topics create orders --schema=order-schema --message-encoding=json
```

Schemas can have revisions, and a topic can accept a range of revisions so you can evolve the format without breaking consumers.

## 251: How do you secure a push subscription to Cloud Run?

1. Keep the Cloud Run service private (`--no-allow-unauthenticated`).
2. Create a service account for push and give it `roles/run.invoker` on the service.
3. Configure the subscription to send an OIDC token:

```bash
gcloud pubsub subscriptions create orders-push --topic=orders \
  --push-endpoint=https://worker-123456789.europe-west1.run.app/pubsub \
  --push-auth-service-account=pubsub-push@my-project.iam.gserviceaccount.com
```

Cloud Run validates the token before your code runs. If you push to an endpoint outside Cloud Run, verify the JWT yourself (audience, issuer, email). You can also set ingress to `internal`, since Pub/Sub counts as internal traffic.

## 252: What is flow control in a Pub/Sub subscriber?

Flow control limits how many messages (or bytes) the client holds unacknowledged at once. Without it, a fast stream can load more messages than your process can handle and run out of memory or time out.

```js
const subscription = pubsub.subscription("orders-worker", {
  flowControl: { maxMessages: 50, allowExcessMessages: false },
  ackDeadline: 60,
});
```

Set it based on how many messages one instance can process at the same time. For GKE workers, scale pods on the subscription backlog metric.

## 253: How do message retention and seek work in Pub/Sub?

- **Subscription retention**: unacked messages are kept for 7 days by default (10 minutes to 7 days). You can also retain acked messages.
- **Topic retention**: the topic keeps all messages for up to 31 days, even before a subscription exists.
- **Seek**: moves a subscription back to a timestamp or a snapshot, so messages after that point are redelivered.

```bash
gcloud pubsub snapshots create before-deploy --subscription=orders-worker
gcloud pubsub subscriptions seek orders-worker --snapshot=before-deploy
```

Take a snapshot before deploying a new consumer. If the new code corrupts data, seek back and reprocess.

## 254: When would you use Cloud Tasks instead of Pub/Sub?

| Need                                    | Cloud Tasks | Pub/Sub |
| --------------------------------------- | ----------- | ------- |
| Explicit control of call rate to target | Yes         | Limited |
| Schedule a task for a specific time     | Yes         | No      |
| Deduplicate by task name                | Yes         | No      |
| Fan-out to many subscribers             | No          | Yes     |
| Very high throughput streaming          | No          | Yes     |
| Producer knows the consumer             | Yes         | No      |

Use Cloud Tasks when the producer wants a specific service to do a job, at a controlled rate. Use Pub/Sub when a producer announces an event and does not care who listens.

## 255: How do you create a Cloud Task that calls a private Cloud Run service?

```js
import { CloudTasksClient } from "@google-cloud/tasks";

const client = new CloudTasksClient();
const parent = client.queuePath("my-project", "europe-west1", "emails");

await client.createTask({
  parent,
  task: {
    httpRequest: {
      httpMethod: "POST",
      url: "https://mailer-123456789.europe-west1.run.app/send",
      headers: { "Content-Type": "application/json" },
      body: Buffer.from(
        JSON.stringify({ to: "ana@example.com", template: "welcome" }),
      ).toString("base64"),
      oidcToken: {
        serviceAccountEmail: "tasks-invoker@my-project.iam.gserviceaccount.com",
      },
    },
    scheduleTime: { seconds: Math.floor(Date.now() / 1000) + 60 },
  },
});
```

Configure rate limits and retries on the queue:

```bash
gcloud tasks queues update emails --location=europe-west1 --max-dispatches-per-second=20 --max-concurrent-dispatches=10 --max-attempts=5
```

## 256: How do you trigger code from any Google Cloud API call using Eventarc?

Eventarc can trigger on Cloud Audit Log entries, which covers almost every Google Cloud API. For example, run a Cloud Run service whenever someone creates a bucket:

```bash
gcloud eventarc triggers create on-bucket-create --location=global \
  --destination-run-service=bucket-auditor --destination-run-region=europe-west1 \
  --event-filters="type=google.cloud.audit.log.v1.written" \
  --event-filters="serviceName=storage.googleapis.com" \
  --event-filters="methodName=storage.buckets.create" \
  --service-account=eventarc-trigger@my-project.iam.gserviceaccount.com
```

The relevant audit log type must be enabled (Data Access logs for read events). Audit log events arrive with some delay, so do not use them for latency-critical paths. Prefer direct events (Cloud Storage, Pub/Sub) when they exist.

## 257: What does a simple Workflows definition look like?

```yaml
main:
  params: [input]
  steps:
    - createOrder:
        call: http.post
        args:
          url: https://orders-123456789.europe-west1.run.app/orders
          auth:
            type: OIDC
          body: ${input}
        result: order
    - chargeCard:
        try:
          call: http.post
          args:
            url: https://payments-123456789.europe-west1.run.app/charge
            auth:
              type: OIDC
            body:
              orderId: ${order.body.id}
        retry: ${http.default_retry}
        result: payment
    - done:
        return: ${payment.body}
```

```bash
gcloud workflows deploy checkout --source=checkout.yaml --location=europe-west1 --service-account=workflows@my-project.iam.gserviceaccount.com
gcloud workflows run checkout --location=europe-west1 --data='{"userId":"u1","items":["p1"]}'
```

## 258: How do you run a Cloud Run job on a schedule?

Use Cloud Scheduler to call the Cloud Run Admin API's `run` method for the job:

```bash
gcloud scheduler jobs create http nightly-report \
  --location=europe-west1 --schedule="0 2 * * *" --time-zone="UTC" \
  --uri="https://run.googleapis.com/v2/projects/my-project/locations/europe-west1/jobs/report:run" \
  --http-method=POST \
  --oauth-service-account-email=scheduler@my-project.iam.gserviceaccount.com
```

Note it uses an OAuth token (for Google APIs), not an OIDC token. The scheduler service account needs a role that can run the job, like `roles/run.invoker` on the job. The console can set this up for you from the job's Triggers tab.

## 259: What is Shared VPC?

Shared VPC lets one **host project** own a VPC network and share its subnets with **service projects**. Resources in service projects (VMs, GKE, Cloud Run with Direct VPC egress) use IPs from the shared subnets.

This lets a central network team control subnets, firewalls, routes, VPN and Interconnect, while app teams manage their own resources and IAM in their own projects. You grant `roles/compute.networkUser` on specific subnets to service project principals. It is the usual setup in enterprise landing zones.

## 260: What is VPC Network Peering and what are its limits?

VPC peering connects two VPC networks (in the same or different projects or organizations) so they can talk over internal IPs, with Google's network and no gateways.

Limits:

- IP ranges must not overlap.
- Peering is **not transitive**. If A peers with B and B peers with C, A cannot reach C through B.
- There are limits on the number of peerings and routes.
- Each side manages its own firewall rules.

For hub-and-spoke designs with many networks, Network Connectivity Center or Private Service Connect often fit better.

## 261: What is Private Service Connect?

Private Service Connect (PSC) lets you reach a service through a private IP endpoint in your own VPC, without peering and without overlapping range issues.

Uses:

- Reach Google APIs on a private IP you choose
- Reach managed services (Cloud SQL, AlloyDB, Memorystore, Apigee) privately
- Consume a service published by another team or a SaaS vendor (service attachments)
- Publish your own internal service to other VPCs

Because only the endpoint IP is shared, the networks stay isolated, which makes it more secure and easier to scale than peering.

## 262: What is private services access?

Private services access is an older way to connect a VPC to Google-managed services like Cloud SQL, Memorystore for Redis and Filestore over private IPs. You reserve an IP range in your VPC, and Google creates a VPC peering to a Google-owned service producer network that uses that range.

```bash
gcloud compute addresses create google-managed-services --global --purpose=VPC_PEERING --prefix-length=16 --network=main
gcloud services vpc-peerings connect --service=servicenetworking.googleapis.com --ranges=google-managed-services --network=main
```

Since it is peering, it is not transitive, which causes trouble reaching those services from on-prem or other peered VPCs. Many services now also support Private Service Connect, which avoids this.

## 263: What are hierarchical and network firewall policies?

- **Hierarchical firewall policies** are attached to the organization or folders and apply to all VPCs below. Security teams use them for org-wide rules, like "always allow IAP ranges for SSH" or "block known bad IPs". A rule can `goto_next` to let lower levels decide.
- **Global and regional network firewall policies** apply to a VPC, like VPC firewall rules, but can be shared, can use secure tags (IAM-controlled) instead of network tags, and support features like FQDN and geolocation objects and threat intelligence.

Rules are evaluated from organization down to folders, then the network policy and VPC rules.

## 264: How do you pick a Google Cloud load balancer?

1. **HTTP/HTTPS traffic?** Use an Application Load Balancer. Otherwise use a Network Load Balancer.
2. **Clients on the internet or internal?** External or internal.
3. **Users worldwide or backends in multiple regions?** Global. Data must stay in one region or Standard Tier? Regional.
4. **For Layer 4: need to keep the client IP and support UDP?** Passthrough. Need TLS offload or global reach? Proxy.

Typical answers: a public web app → global external Application LB. Service-to-service in a VPC → regional internal Application LB. A game server with UDP → external passthrough Network LB.

## 265: What are the components of a global external Application Load Balancer?

```text
Client → Forwarding rule (IP:443) → Target HTTPS proxy (+ SSL certificates)
       → URL map (host and path rules) → Backend service (+ Cloud Armor, CDN, IAP, health check)
       → Backends: instance groups, NEGs (zonal, serverless, internet) or backend buckets
```

- **Forwarding rule**: the public IP and port.
- **Target proxy**: terminates HTTP/HTTPS and holds the certificates.
- **URL map**: routes by host and path, and can do redirects, rewrites and traffic splitting.
- **Backend service**: groups backends, sets the balancing mode, timeouts and health checks, and is where you attach Cloud Armor, Cloud CDN and IAP.

## 266: How do you get Google-managed certificates on a load balancer?

The simple way:

```bash
gcloud compute ssl-certificates create api-cert --domains=api.example.com --global
```

Attach it to the target HTTPS proxy and point the domain's DNS A record to the load balancer IP. Provisioning finishes after DNS points to the LB, which can take up to an hour.

With **Certificate Manager** you can use DNS authorization, which lets you issue the certificate before switching DNS (zero-downtime migrations) and supports wildcard certificates:

```bash
gcloud certificate-manager dns-authorizations create example-auth --domain=example.com
gcloud certificate-manager certificates create wildcard-cert --domains="*.example.com,example.com" --dns-authorizations=example-auth
```

## 267: How do you control caching in Cloud CDN?

Cloud CDN has cache modes:

- `USE_ORIGIN_HEADERS`: cache only responses with valid caching headers.
- `CACHE_ALL_STATIC` (default): cache static content (images, CSS, JS) and anything with cache headers.
- `FORCE_CACHE_ALL`: cache everything, ignoring private headers. Dangerous for user-specific responses.

You can also set default, max and client TTLs, customize cache keys (for example ignore some query parameters), use negative caching for 404s, and serve stale content while revalidating. After a deploy, invalidate paths:

```bash
gcloud compute url-maps invalidate-cdn-cache web-lb --path="/index.html" --async
```

Versioned asset names (`app.3f9a1c.js`) are better than frequent invalidations.

## 268: How do you write Cloud Armor rules?

```bash
gcloud compute security-policies create api-policy

# Block a country
gcloud compute security-policies rules create 1000 --security-policy=api-policy \
  --expression="origin.region_code == 'XX'" --action=deny-403

# OWASP SQL injection and XSS protection
gcloud compute security-policies rules create 2000 --security-policy=api-policy \
  --expression="evaluatePreconfiguredWaf('sqli-v33-stable', {'sensitivity': 1}) || evaluatePreconfiguredWaf('xss-v33-stable', {'sensitivity': 1})" \
  --action=deny-403

gcloud compute backend-services update api-backend --global --security-policy=api-policy
```

Rules run in priority order (lowest first) and the first match wins. Start new WAF rules in preview mode (`--preview`) and check logs for false positives before enforcing.

## 269: How do you rate limit clients with Cloud Armor?

```bash
gcloud compute security-policies rules create 3000 --security-policy=api-policy \
  --expression="request.path.matches('/login')" \
  --action=rate-based-ban \
  --rate-limit-threshold-count=20 --rate-limit-threshold-interval-sec=60 \
  --ban-duration-sec=600 \
  --conform-action=allow --exceed-action=deny-429 \
  --enforce-on-key=IP
```

- `throttle` limits a client to a rate and rejects the extra requests.
- `rate-based-ban` bans a client for some time after it goes over the limit.

You can key the limit by IP, by an HTTP header (like an API key), by cookie, by path and more. Rate limiting at the edge protects your backends from login brute force and scraping.

## 270: How do you use IAP to protect a Cloud Run app or reach a VM?

**Cloud Run**: you can enable IAP directly on the service, or put the service behind an external Application Load Balancer and enable IAP on the backend service. Then grant `roles/iap.httpsResourceAccessor` to the users or groups who should get in. Your app can read the user's identity from the `x-goog-iap-jwt-assertion` header and should verify that JWT.

**VMs with no public IP**: allow ingress from IAP's range `35.235.240.0/20` on port 22, grant `roles/iap.tunnelResourceAccessor`, then:

```bash
gcloud compute ssh db-admin-vm --zone=europe-west1-b --tunnel-through-iap
gcloud compute start-iap-tunnel db-admin-vm 5432 --local-host-port=localhost:5432 --zone=europe-west1-b
```

## 271: How do you configure Cloud NAT and avoid port exhaustion?

```bash
gcloud compute routers create nat-router --network=main --region=europe-west1
gcloud compute routers nats create nat-config --router=nat-router --region=europe-west1 \
  --nat-all-subnet-ip-ranges --auto-allocate-nat-external-ips \
  --enable-dynamic-port-allocation --min-ports-per-vm=64 --max-ports-per-vm=4096
```

Each NAT IP has about 64,000 ports, shared between VMs. If a VM (or a busy Cloud Run service) opens many connections to the same destination, it can run out of ports and connections fail, shown as dropped packets in NAT logs and metrics.

Fixes: enable dynamic port allocation, add more NAT IPs, reuse HTTP connections (keep-alive) instead of opening new ones, and lower TCP timeouts where safe.

## 272: How do private DNS zones and DNS forwarding work in Cloud DNS?

- **Private zone**: DNS records visible only to selected VPC networks, like `db.internal.example.com → 10.20.0.5`.
- **Forwarding zone**: sends queries for a domain (like `corp.example.com`) to on-prem DNS servers.
- **Inbound server policy**: lets on-prem DNS servers resolve your private zones in Google Cloud.
- **Peering zone**: lets one VPC use the DNS setup of another VPC, useful with Shared VPC and hub-and-spoke designs.

Together these give hybrid DNS where cloud and on-prem resolve each other's names.

## 273: How does HA VPN work?

HA VPN uses a VPN gateway with two interfaces, each with its own public IP. You create two tunnels (one per interface) to your on-prem VPN device, or to two devices. With this setup Google gives a 99.99% SLA.

Routes are exchanged dynamically with BGP through Cloud Router, so when a tunnel goes down traffic moves to the other one automatically. Each tunnel supports about 3 Gbps. You add more tunnels for more bandwidth. HA VPN can also connect to AWS or Azure VPN gateways.

## 274: How do you rotate secrets in Secret Manager?

Secrets have versions. Rotation means adding a new version and then disabling or destroying the old one:

```bash
echo -n "new-password" | gcloud secrets versions add db-password --data-file=-
gcloud secrets versions disable 3 --secret=db-password
```

You can set a rotation schedule on a secret, which publishes a message to a Pub/Sub topic at each rotation time. A function or job then creates the new credential in the target system and adds the new version. Apps should read `latest` (or reload on a schedule) and handle both old and new credentials working for a short overlap period.

## 275: How do you read a secret from Secret Manager in Node.js?

```js
import { SecretManagerServiceClient } from "@google-cloud/secret-manager";

const client = new SecretManagerServiceClient();

async function getSecret(name) {
  const [version] = await client.accessSecretVersion({
    name: `projects/my-project/secrets/${name}/versions/latest`,
  });
  return version.payload.data.toString("utf8");
}

const stripeKey = await getSecret("stripe-api-key");
```

Read secrets once at startup or cache them for a few minutes. Calling the API on every request adds latency and cost and can hit quotas. On Cloud Run it is often simpler to use `--set-secrets` and read an env var or file.

## 276: What are customer-managed encryption keys (CMEK)?

With CMEK, a service like Cloud Storage, BigQuery, Cloud SQL, Pub/Sub or Persistent Disk encrypts your data with a key you own in Cloud KMS instead of a Google-managed key.

```bash
gcloud storage buckets update gs://finance-data \
  --default-encryption-key=projects/sec/locations/europe-west1/keyRings/data/cryptoKeys/finance
```

You control rotation, can see key usage in audit logs, and can disable the key to make the data unreadable. The service's service agent needs `roles/cloudkms.cryptoKeyEncrypterDecrypter` on the key. If the key is disabled or destroyed by mistake, the data becomes unusable, so protect keys carefully.

## 277: How do you write structured logs from Cloud Run?

Write one JSON object per line to stdout. Cloud Logging reads special fields like `severity`, `message`, `httpRequest` and `logging.googleapis.com/trace`:

```js
function log(severity, message, extra = {}) {
  console.log(JSON.stringify({ severity, message, ...extra }));
}

app.use((req, res, next) => {
  const traceHeader = req.header("X-Cloud-Trace-Context");
  const [traceId] = traceHeader?.split("/") ?? [];
  req.log = (sev, msg, extra) =>
    log(sev, msg, {
      ...extra,
      "logging.googleapis.com/trace": `projects/${process.env.PROJECT_ID}/traces/${traceId}`,
    });
  next();
});

req.log("ERROR", "Payment failed", { orderId: "o-1", provider: "stripe" });
```

Linking logs to the trace makes the Logs Explorer group all logs of one request together. Libraries like Pino or Winston with the Google Cloud formatter can do this for you.

## 278: What are log-based metrics?

A log-based metric turns matching log entries into a Cloud Monitoring metric, so you can chart and alert on it.

- **Counter metrics** count entries that match a filter, like "payment failed" logs.
- **Distribution metrics** extract a number from logs, like a latency field, and build a histogram.

```bash
gcloud logging metrics create payment_failures \
  --description="Failed payments" \
  --log-filter='resource.type="cloud_run_revision" AND jsonPayload.message="Payment failed"'
```

Then create an alerting policy on `logging.googleapis.com/user/payment_failures`. For high-volume numbers, sending real metrics with OpenTelemetry is cheaper and more accurate.

## 279: What are log sinks and how do you route logs?

All logs pass through the Log Router. Sinks decide where each log entry goes:

- `_Required` sink: audit and some system logs to the `_Required` bucket (cannot be changed).
- `_Default` sink: everything else to the `_Default` bucket.
- Custom sinks: send matching logs to another log bucket, BigQuery, Cloud Storage, Pub/Sub or another project.

```bash
gcloud logging sinks create audit-to-bq \
  bigquery.googleapis.com/projects/sec-logging/datasets/audit_logs \
  --log-filter='logName:"cloudaudit.googleapis.com"'
```

The sink has a writer identity (service account) that you must grant write access on the destination.

## 280: How do you control Cloud Logging costs?

You pay for log volume ingested into log buckets (after a free amount per project) and for retention longer than 30 days.

Ways to cut costs:

- Add **exclusion filters** to the `_Default` sink for noisy logs (health checks, debug logs, successful load balancer requests).
- Lower log levels in production.
- Sample high-volume request logs.
- Route long-term logs to Cloud Storage instead of keeping them in log buckets for years.
- Avoid huge log entries (full request bodies).

Excluded logs are dropped. Make sure you do not exclude logs you need for audits or debugging.

## 281: What is Log Analytics?

Log Analytics lets you query logs with SQL in a log bucket that has been upgraded to use it. Under the hood it uses BigQuery, and you can link the bucket to a BigQuery dataset to join logs with other data.

```sql
SELECT
  JSON_VALUE(json_payload.orderId) AS order_id,
  COUNT(*) AS errors
FROM `my-project.global._Default._AllLogs`
WHERE severity = 'ERROR'
  AND timestamp > TIMESTAMP_SUB(CURRENT_TIMESTAMP(), INTERVAL 1 DAY)
GROUP BY order_id
ORDER BY errors DESC
LIMIT 20;
```

It is much better than Logs Explorer for aggregations, like "top 10 error messages per service this week".

## 282: How do you send custom metrics to Cloud Monitoring?

The recommended way is OpenTelemetry. You instrument your app with the OpenTelemetry SDK and export metrics either to an OpenTelemetry Collector (a sidecar on Cloud Run or a deployment on GKE) or directly with Google's exporters.

```js
import { metrics } from "@opentelemetry/api";

const meter = metrics.getMeter("checkout");
const ordersCounter = meter.createCounter("orders_created", {
  description: "Orders created",
});

ordersCounter.add(1, { payment_method: "card", country: "DE" });
```

Keep label values low-cardinality. Do not use user IDs or order IDs as labels, because each unique combination is a separate time series and costs money.

## 283: How does trace context propagate between services on Google Cloud?

Google Cloud load balancers and Cloud Run add a trace header to incoming requests. Newer setups use the W3C `traceparent` header, and the older `X-Cloud-Trace-Context` header is still sent.

When your service calls another service, it must forward the context so both spans end up in the same trace. OpenTelemetry auto-instrumentation for Node.js (HTTP, Express, gRPC, database clients) does this automatically. For Pub/Sub, the context is passed in message attributes, and the client library can do this when OpenTelemetry tracing is enabled.

## 284: How do you define an SLO in Cloud Monitoring?

You create a service (Cloud Run, GKE and others are detected automatically, or you define a custom one), then add an SLO:

- **SLI**: what you measure, like "fraction of requests with status < 500" or "fraction of requests faster than 300 ms".
- **Goal**: like 99.9%.
- **Window**: rolling (28 days) or calendar (monthly).

Cloud Monitoring then shows the error budget left and lets you alert on **burn rate**, meaning how fast the error budget is being used up, which is a better signal than raw error rate alerts.

## 285: What is Google Cloud Managed Service for Prometheus?

It is a managed, global Prometheus-compatible metrics backend built on Monarch, the same system behind Cloud Monitoring. You keep using Prometheus exporters, PromQL and Grafana, but you do not run Prometheus servers or worry about storage and scaling.

On GKE, managed collection is turned on by default for new clusters. You define `PodMonitoring` resources to tell it what to scrape. Metrics are kept for 24 months, and you pay per sample ingested.

## 286: A Cloud Run service is returning 500 and 503 errors. How do you debug it?

1. **Logs**: filter Logs Explorer by the service and `severity>=ERROR`. Look for stack traces and messages from Cloud Run itself, like "The request failed because the instance could not start" or "Memory limit exceeded".
2. **Metrics**: check request count by response code, latency, instance count, CPU and memory. Memory near the limit means OOM kills.
3. **503 causes**: the container crashed or failed startup probes, max instances reached with no room in the queue, or request timeout.
4. **Recent changes**: compare with the previous revision, and roll back traffic if the new one is broken.
5. **Dependencies**: check database connections (pool exhausted), VPC egress, NAT ports and downstream service errors.

## 287: What is Cloud Profiler?

Cloud Profiler continuously collects CPU and heap profiles from your running apps with low overhead, and shows flame graphs in the console. It supports Node.js, Java, Go and Python.

```js
import profiler from "@google-cloud/profiler";

await profiler.start({
  serviceContext: { service: "api", version: process.env.K_REVISION },
});
```

It helps answer "which functions use the most CPU in production" or "where does memory grow", without reproducing the load locally. On Cloud Run, enable instance-based billing so the profiler agent gets CPU between requests.

## 288: How can you automatically stop spending when a budget is exceeded?

Budgets only send notifications. To act on them:

1. Configure the budget to publish to a Pub/Sub topic.
2. Write a Cloud Run function subscribed to the topic.
3. When `costAmount` is above `budgetAmount`, the function disables billing on the project by calling the Cloud Billing API, or scales down specific resources.

```js
import functions from "@google-cloud/functions-framework";
import { CloudBillingClient } from "@google-cloud/billing";

const billing = new CloudBillingClient();

functions.cloudEvent("capSpend", async (event) => {
  const data = JSON.parse(
    Buffer.from(event.data.message.data, "base64").toString(),
  );
  if (data.costAmount <= data.budgetAmount) return;
  await billing.updateProjectBillingInfo({
    name: "projects/sandbox-123",
    projectBillingInfo: { billingAccountName: "" },
  });
});
```

Disabling billing stops all paid services and can delete some resources. Use this for sandboxes, not production. Budget data is also delayed by hours.

## 289: Why export billing data to BigQuery?

The Cloud Billing export sends detailed cost data (standard usage cost, detailed usage cost per resource, and pricing data) to a BigQuery dataset regularly through the day. With it you can:

- Break down cost by project, service, SKU, label and even individual resources
- Build dashboards in Looker Studio
- Find cost spikes and their cause
- Allocate costs to teams using labels

```sql
SELECT labels.value AS team, ROUND(SUM(cost), 2) AS cost
FROM `billing.gcp_billing_export_v1_XXXXXX`, UNNEST(labels) AS labels
WHERE labels.key = 'team' AND invoice.month = '202610'
GROUP BY team ORDER BY cost DESC;
```

Turn it on early, because it only includes data from when it was enabled.

## 290: How do you allocate cloud costs to teams?

- Use **separate projects** per team or app where possible. Project is the clearest cost boundary.
- Apply **labels** like `team`, `app`, `env` and `cost-center` to every resource, and enforce them in Terraform modules or with policy checks.
- For shared resources like GKE clusters, enable **GKE cost allocation** to split costs by namespace and label.
- Export billing to BigQuery and build reports per label.
- Set **budgets** per project or label with alerts to the owning team.

## 291: What is the difference between resource-based and spend-based committed use discounts?

- **Resource-based CUDs**: commit to a specific amount of vCPUs, memory, GPUs or local SSD in a region for 1 or 3 years. Good discounts, but tied to a machine family and region.
- **Spend-based (flexible) CUDs**: commit to spend a dollar amount per hour on a set of services (Compute Engine across many machine series, Cloud Run, GKE Autopilot, Cloud SQL and others). Smaller discount, but much more flexible.

Combine them: cover a stable core with resource-based CUDs and a broader baseline with flexible CUDs. The CUD recommender suggests amounts based on your history.

## 292: How do you rightsize Compute Engine and GKE resources?

- Use the **machine type recommender** for VMs. It suggests smaller machines for underused VMs, based on Cloud Monitoring data.
- Install the **Ops Agent** so memory metrics are available for better recommendations.
- In GKE, use **VPA recommendations** and the GKE cost optimization views to fix pod requests that are much higher than usage.
- Use custom machine types to match the real ratio of CPU and memory.
- Re-check after traffic changes. Rightsizing is a regular task, not one-time.

## 293: How should an app handle quota errors (429 or RESOURCE_EXHAUSTED)?

- Retry with **exponential backoff and jitter**. Client libraries already do this for many methods.
- Do not retry immediately in a tight loop. That makes it worse.
- Batch requests where the API supports it.
- Cache results that do not change often.
- Spread load over time with Cloud Tasks or a queue.
- If the limit is too low for normal usage, request a quota increase, and add alerting on quota usage metrics so you know before you hit it.

## 294: How do retries work in the Google Cloud client libraries?

Most Node.js client libraries (built on google-gax) retry idempotent calls automatically on transient errors like `UNAVAILABLE` and `DEADLINE_EXCEEDED`, with exponential backoff. Each method has a default timeout and retry settings.

You can change them per call:

```js
// Give this call more time and fewer retries than the default
const [topics] = await pubsub.getTopics({
  gaxOpts: { timeout: 30_000, maxRetries: 3 },
});
```

Be careful with non-idempotent operations, like creating resources with server-generated IDs. A retry after a lost response can create a duplicate.

## 295: How do you manage configuration across dev, staging and prod?

- One project per environment, created from the same Terraform modules with different variables.
- Non-secret config as environment variables set at deploy time (Cloud Run, GKE ConfigMaps).
- Secrets in Secret Manager in each environment's project, with the same secret names.
- The same container image promoted through environments (with Cloud Deploy or your CI), never rebuilt per environment.
- Feature flags (Firebase Remote Config or a third-party tool) for behavior changes that should not need a deploy.

## 296: How do you develop locally against Google Cloud services?

- Run `gcloud auth application-default login` so client libraries can call real services as you, ideally impersonating a dev service account.
- Use emulators for Firestore, Pub/Sub, Datastore, Bigtable and Spanner, or the Firebase Emulator Suite.
- Use a personal or shared **dev project**, not prod.
- Run containers locally with `docker run -e GOOGLE_CLOUD_PROJECT=... -v ~/.config/gcloud:/root/.config/gcloud` to reuse your ADC.
- For Cloud SQL, use the Cloud SQL Auth Proxy to reach a dev instance.

## 297: How do you call Gemini models from a Node.js backend on Google Cloud?

Use the Google Gen AI SDK with the Agent Platform (Vertex AI) backend, so authentication goes through ADC and IAM:

```js
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({
  vertexai: true,
  project: process.env.GOOGLE_CLOUD_PROJECT,
  location: "global",
});

const response = await ai.models.generateContent({
  model: process.env.GEMINI_MODEL, // check the docs for current model names
  contents: "Summarize this support ticket in two sentences: ...",
});

console.log(response.text);
```

The service account needs `roles/aiplatform.user`. Model names change often, so keep the model in config, not in code.

## 298: When would you choose Dataflow over Dataproc?

- **Dataflow**: new pipelines, especially streaming. Serverless, autoscaling, exactly-once processing with Apache Beam. No clusters to tune.
- **Dataproc**: existing Spark, Hadoop or Hive code, teams with Spark skills, or tools from that ecosystem (notebooks, Spark ML). Dataproc Serverless removes most of the cluster work.

If the pipeline is mainly SQL transformations on data already in BigQuery, consider doing it inside BigQuery (scheduled queries, Dataform) instead of either.

## 299: What is Datastream?

Datastream is a serverless change data capture (CDC) service. It reads changes from the transaction logs of MySQL, PostgreSQL, Oracle, SQL Server and other sources, and streams them to BigQuery, Cloud Storage or other destinations with low latency.

A common use is keeping an up-to-date copy of an operational database in BigQuery for analytics, without heavy nightly exports and without loading the production database with queries.

## 300: How do you add user authentication to an app on Google Cloud?

Common choices:

- **Firebase Authentication**: easy SDKs for email/password, phone and social logins (Google, Apple, GitHub). Good for web and mobile apps.
- **Identity Platform**: the Google Cloud version of Firebase Auth with enterprise features like SAML and OIDC providers, multi-tenancy, blocking functions and an SLA.
- **IAP**: for internal apps used by employees with Google identities.

On the backend you verify the ID token:

```js
import { initializeApp } from "firebase-admin/app";
import { getAuth } from "firebase-admin/auth";

initializeApp();

app.use(async (req, res, next) => {
  const token = req.header("Authorization")?.replace("Bearer ", "");
  try {
    req.user = await getAuth().verifyIdToken(token);
    next();
  } catch {
    res.status(401).send("Unauthorized");
  }
});
```

# Advanced Questions (301-450)

## 301: How would you design a highly available web app on Google Cloud?

A typical design for a stateless API plus database:

- **Edge**: global external Application Load Balancer with Cloud Armor and Cloud CDN, one anycast IP.
- **Compute**: Cloud Run services (regional, already spread across zones) or a regional GKE cluster. Optionally the same service in two regions behind the same load balancer.
- **Database**: Cloud SQL Enterprise Plus with HA (zonal failover) plus a cross-region replica for DR, or Spanner if you need multi-region writes.
- **Cache and sessions**: Memorystore with replicas, or keep the app stateless and put sessions in a signed cookie or Firestore.
- **Async work**: Pub/Sub and Cloud Tasks so spikes and slow dependencies do not hurt the user path.
- **Operations**: SLOs with burn-rate alerts, health checks, automated rollbacks and tested backups.

The key idea is to remove single points of failure at each layer and to decide where you accept zonal vs regional risk.

## 302: How do you run a Cloud Run service in multiple regions?

1. Deploy the same image to two or more regions (the same service name in each).
2. Create a serverless NEG in each region pointing to that region's service.
3. Add all NEGs to one backend service of a global external Application Load Balancer.

```bash
for region in europe-west1 us-central1; do
  gcloud run deploy api --image=IMAGE --region=$region --ingress=internal-and-cloud-load-balancing
  gcloud compute network-endpoint-groups create api-neg-$region --region=$region \
    --network-endpoint-type=serverless --cloud-run-service=api
  gcloud compute backend-services add-backend api-backend --global \
    --network-endpoint-group=api-neg-$region --network-endpoint-group-region=$region
done
```

The load balancer sends users to the closest region. Add outlier detection or health checks so it moves traffic away from a failing region. The hard part is the data layer: each region needs access to data with acceptable latency and consistency, so pair this with Spanner, Firestore multi-region, or a primary database with clear failover rules.

## 303: What disaster recovery strategies can you use on Google Cloud?

They range from cheap and slow to expensive and fast:

| Pattern        | Description                                                                 | RTO / RPO       |
| -------------- | --------------------------------------------------------------------------- | --------------- |
| Backup/restore | Backups to another region, rebuild everything with Terraform after disaster | Hours / hours   |
| Pilot light    | Data replicated to DR region, minimal compute kept off or at zero           | Tens of minutes |
| Warm standby   | Scaled-down full stack running in DR region, scale up on failover           | Minutes         |
| Active-active  | Full stack in two or more regions serving traffic all the time              | Near zero       |

On Google Cloud, serverless services make warm standby cheap: Cloud Run in the DR region scales to zero until needed. Data replication options include cross-region Cloud SQL replicas, dual-region buckets, multi-region Firestore and Spanner. Whatever you choose, practice failovers regularly.

## 304: How does Spanner provide strong consistency across regions?

Spanner splits data into **splits** (ranges of keys). Each split is replicated with **Paxos** across zones or regions. A write is committed when a majority of voting replicas agree.

Spanner uses **TrueTime**, an API backed by GPS receivers and atomic clocks in every data center. It returns the current time with a small, known uncertainty. When committing, Spanner waits out that uncertainty ("commit wait") before making the write visible. This guarantees that if transaction T1 commits before T2 starts, T1 has a lower timestamp. That property is called external consistency, which is stronger than serializability.

Because of this, reads at a timestamp can be served by any replica that is caught up, without locks.

## 305: How do you avoid hotspots in Spanner?

Spanner stores rows ordered by primary key and splits key ranges across servers. If keys increase monotonically (auto-increment IDs, timestamps first), all new writes go to the last split, which becomes a hotspot.

Fixes:

- Use **UUID v4** keys or bit-reversed sequences (`GENERATE_UUID()` or `bit_reversed_positive` sequences).
- If you need time ordering, put a high-cardinality column first, like `(UserId, CreatedAt)`.
- Add a shard prefix (`ShardId = hash(key) % N`) for very high write rates.
- Avoid indexes whose leading column is a timestamp, because indexes are tables too and can hotspot.

Key Visualizer in the console shows hot key ranges.

## 306: What are interleaved tables in Spanner?

Interleaving stores child rows physically next to their parent row. For example, `Orders` interleaved in `Customers` keeps a customer's orders in the same split as the customer.

```sql
CREATE TABLE Customers (
  CustomerId STRING(36) NOT NULL,
  Name STRING(MAX)
) PRIMARY KEY (CustomerId);

CREATE TABLE Orders (
  CustomerId STRING(36) NOT NULL,
  OrderId STRING(36) NOT NULL,
  Total NUMERIC
) PRIMARY KEY (CustomerId, OrderId),
  INTERLEAVE IN PARENT Customers ON DELETE CASCADE;
```

Joins and transactions that touch one customer and their orders stay local to one split, which makes them fast. The child's primary key must start with the parent's key. Do not interleave if a parent can get a huge number of children, because a single split has size and throughput limits.

## 307: How do you choose between Cloud SQL, AlloyDB and Spanner?

- **Cloud SQL**: standard MySQL, PostgreSQL or SQL Server. Vertical scaling plus read replicas. Fits most apps up to a few TB and moderate write volume. Cheapest and most familiar.
- **AlloyDB**: PostgreSQL-compatible with much higher throughput, fast analytics through the columnar engine, and fast failover. Fits busy PostgreSQL apps that outgrow Cloud SQL or need HTAP and vector search.
- **Spanner**: horizontal scale for reads and writes, multi-region with 99.999% SLA and strong consistency. Fits global apps or very high write rates. Requires schema design for distribution (keys, interleaving) and has some SQL differences.

Start with Cloud SQL unless you know you need more, and design so you can move later.

## 308: What makes AlloyDB faster than standard PostgreSQL?

- **Separated storage**: a distributed, log-based storage layer. The database writes only the WAL, and storage builds pages from it. Less I/O on the primary and fast replicas that share storage.
- **Columnar engine**: keeps frequently scanned columns in memory in columnar format, automatically chosen, so analytical queries can be many times faster without a separate warehouse.
- **Intelligent caching** across memory and local SSD tiers.
- **Read pools**: many read replicas behind one endpoint with low lag.
- **Fast failover**: usually under a minute.

Google says it is several times faster than standard PostgreSQL for transactional workloads. For interviews, the key point is the storage/compute separation.

## 309: How do you design a row key for Bigtable?

The row key is the only index, and rows are sorted by it. A good key:

- Matches your most common query, so it can be read as a single row or a short range scan.
- Spreads writes across the key space to avoid hotspots.
- Puts the most general part first, like `device#region#timestamp`.

Example for IoT readings, queried per device over time:

```text
sensor-4821#20261029T101500
sensor-4821#20261029T101600
```

Avoid keys that start with a timestamp or sequential ID. If you need the newest rows first, use a reversed timestamp (`Long.MAX_VALUE - ts`). Keep keys short, since they are stored with every cell.

## 310: How do you detect and fix hotspots in Bigtable?

**Detect**: use Key Visualizer, which shows a heat map of read and write activity across the key space over time. Bright horizontal lines mean a hot key or range. Also watch CPU per node. Bigtable recommends keeping it under about 70% for latency-sensitive apps.

**Fix**:

- Change the row key design to spread writes (field promotion, salting with a hash prefix).
- Split very wide rows (rows with too many cells).
- Add nodes or enable autoscaling, but this does not help if one key is hot.
- Use app profiles to separate batch and serving traffic, possibly to different clusters.

## 311: How do you avoid hotspots in Firestore?

Firestore splits data into key ranges that move between servers. Hotspots come from:

- **Sequential document IDs** like timestamps or counters. Use auto-generated IDs (`collection.add()` or `doc()` with no ID).
- **Indexed fields with sequential values** like `createdAt` at very high write rates. If you never query on it, exempt the field from indexing.
- **A single document updated very often** (counter, "last updated" doc). Use distributed counters or batch the updates.

Follow the **500/50/5** rule for new collections: start at up to 500 operations per second and increase by at most 50% every 5 minutes, so Firestore has time to split.

## 312: How do you implement a high-traffic counter in Firestore?

A single document should not be updated more than about once per second. For a busy counter (likes, views), use a **distributed counter**: N shard documents, each request increments a random shard, and the total is the sum.

```js
const NUM_SHARDS = 10;

async function incrementLikes(postId) {
  const shardId = Math.floor(Math.random() * NUM_SHARDS).toString();
  await db
    .doc(`posts/${postId}/likeShards/${shardId}`)
    .set({ count: FieldValue.increment(1) }, { merge: true });
}

async function getLikes(postId) {
  const shards = await db.collection(`posts/${postId}/likeShards`).get();
  return shards.docs.reduce((sum, d) => sum + (d.get("count") ?? 0), 0);
}
```

Alternatives: use a `sum()` aggregation query over the shards, or count in Memorystore and write the total to Firestore periodically.

## 313: How does BigQuery work internally?

- **Colossus**: Google's distributed file system stores table data in a columnar format called Capacitor.
- **Dremel**: the query engine. A query becomes a tree of stages, and each stage runs on many **slots** (units of CPU, memory and network) in parallel.
- **Shuffle**: intermediate results between stages go through a distributed in-memory shuffle layer, which lets BigQuery handle large joins and aggregations.
- **Jupiter network**: Google's data center network gives huge bandwidth between storage and compute, which makes storage/compute separation practical.

Because storage and compute are separate, you can scale them independently and many queries can read the same data at once.

## 314: How do you optimize a slow BigQuery query?

1. Open the **execution graph** in the console. Look for stages with high wait, slot time, or large output.
2. Reduce data read: select fewer columns, filter on partition and cluster columns early.
3. Check joins: filter both sides before joining, and watch for joins that explode the number of rows. Put the larger table first in older-style guidance, though the optimizer often handles order now.
4. Avoid data skew. One key with a huge number of rows makes one worker do most of the work. Handle skewed keys separately.
5. Replace repeated work with materialized views or intermediate tables.
6. Avoid `ORDER BY` on huge results without `LIMIT`, and JavaScript UDFs when SQL can do it.
7. Use `APPROX_COUNT_DISTINCT` and other approximate functions when exact values are not needed.

## 315: How do BigQuery reservations and slot autoscaling work?

With editions you create a **reservation** in a region with:

- A **baseline**: slots always allocated and billed.
- A **max** (autoscaling): BigQuery adds slots in steps up to this amount when queries need them, and you pay per second for what was used.

Projects are **assigned** to reservations, so their queries use those slots. Idle slots from one reservation can be shared with others. You can buy **commitments** (1 or 3 years) for discounted baseline slots.

A common setup: one reservation for production ETL with a higher baseline, another for ad-hoc analyst queries with a low baseline and a capped max, so analysts cannot slow down production pipelines.

## 316: What are the limits of DML in BigQuery and how do you do upserts?

BigQuery is built for analytics, not row-by-row OLTP. DML (`INSERT`, `UPDATE`, `DELETE`, `MERGE`) works, but each statement rewrites storage blocks, so many tiny statements are slow and can hit concurrency limits (mutating DML on a table is queued).

Do changes in batches. For upserts, load changes into a staging table and run one `MERGE`:

```sql
MERGE shop.customers AS t
USING shop.customers_staging AS s
ON t.customer_id = s.customer_id
WHEN MATCHED THEN
  UPDATE SET email = s.email, updated_at = s.updated_at
WHEN NOT MATCHED THEN
  INSERT (customer_id, email, updated_at) VALUES (s.customer_id, s.email, s.updated_at);
```

Filter the target by partition in the `ON` clause when possible, so the `MERGE` does not scan the whole table.

## 317: How can you stream change data (CDC) into BigQuery with upserts?

The Storage Write API supports **CDC upserts** on tables with a primary key. Each row includes a `_CHANGE_TYPE` pseudo-column (`UPSERT` or `DELETE`), and BigQuery applies the changes in the background.

You set `max_staleness` on the table to control how fresh query results must be. A lower value means fresher data but more compute cost at query time.

Datastream uses this method when replicating from databases into BigQuery, so you get a near real-time copy without writing `MERGE` jobs yourself.

## 318: How do you handle data residency and cross-region needs in BigQuery?

- A dataset's location is fixed at creation. Queries run in the location of the data, and one query cannot join datasets from different locations.
- To combine data, copy datasets with **cross-region dataset replication** or the Data Transfer Service, or use **BigQuery Omni** to query data stored in AWS or Azure in place.
- To enforce residency, use the `gcp.resourceLocations` organization policy and, for regulated workloads, Assured Workloads.
- For DR, BigQuery **managed disaster recovery** (with Enterprise Plus) can fail over compute and storage to a secondary region.

Pick locations early. Moving large datasets later costs time and egress.

## 319: What delivery guarantees does Pub/Sub give end to end?

- **Publishing**: a successful publish means the message is stored durably in multiple zones. If the publish response is lost, the client may retry and create a **duplicate** with a new message ID.
- **Delivery**: at-least-once by default. Duplicates can happen after ack deadline expiry, nacks or failures.
- **Exactly-once delivery** (pull, single region): prevents redelivery after a successful ack, but does not remove publisher-side duplicates.
- **Ordering**: only with ordering keys and an ordered subscription. Otherwise messages can arrive in any order.

So a correct consumer must be **idempotent** and must not assume ordering unless configured. Use a business ID in the message (like `orderId`) for deduplication, not the Pub/Sub message ID.

## 320: How do you build an effectively exactly-once processing pipeline on Google Cloud?

You cannot rely on the transport alone. Combine:

1. **Idempotency keys**: each event carries a stable ID from the producer (`orderId`, `eventId`).
2. **Atomic dedup + effect**: in one database transaction, check whether the ID was processed, apply the change, and record the ID.

```js
await db.runTransaction(async (tx) => {
  const marker = db.collection("processedEvents").doc(event.id);
  if ((await tx.get(marker)).exists) return; // already done
  tx.update(db.doc(`accounts/${event.accountId}`), {
    balance: FieldValue.increment(event.amount),
  });
  tx.create(marker, {
    processedAt: FieldValue.serverTimestamp(),
    expireAt: inThirtyDays(),
  });
});
```

3. Acknowledge the message only after the transaction commits.
4. Use a TTL on the dedup records.

For streaming analytics, Dataflow provides exactly-once processing within the pipeline, and BigQuery's Storage Write API committed streams give exactly-once writes.

## 321: What are the trade-offs of using ordering keys in Pub/Sub at scale?

- Messages with the same key are delivered one batch at a time to one subscriber, so **throughput per key** is limited (about 1 MB/s per ordering key for publishing).
- A slow or failing message **blocks** all later messages for that key until it is acked or sent to a dead-letter topic.
- Publishing errors pause the key until you resume it in the client.
- Hot keys (one tenant with most of the traffic) create uneven load.

Use keys that are fine-grained (per account, per order) rather than coarse (per tenant or global). Often a better design is to make consumers handle out-of-order events, for example with version numbers and "ignore older version" logic.

## 322: How do you scale Pub/Sub consumers and handle backpressure?

- **Monitor** `subscription/num_undelivered_messages` and `oldest_unacked_message_age`. Age is the best signal of falling behind.
- **Scale out** subscribers on backlog: HPA with external metrics on GKE, or push subscriptions to Cloud Run, which scales by concurrent requests.
- **Protect downstream** systems with flow control, Cloud Run `max-instances`, or by putting Cloud Tasks with a rate limit between Pub/Sub and a fragile API.
- **Handle failures**: exponential retry policy and a dead-letter topic, so bad messages do not loop forever.

With push to Cloud Run, Pub/Sub also slows down delivery automatically when your endpoint returns errors or responds slowly (push backoff).

## 323: How do you reliably publish events after a database write?

The problem: you save an order to the database and then publish `order.created` to Pub/Sub. If the process crashes between the two, the event is lost. If you publish first and the write fails, you have a false event.

The **transactional outbox** pattern solves it:

1. In the same database transaction, write the order and an `outbox` row with the event.
2. A separate relay reads unsent outbox rows, publishes them to Pub/Sub, and marks them sent.
3. Consumers are idempotent, since the relay can publish an event twice.

On Google Cloud, the relay can be a Cloud Run job on a schedule, a Firestore trigger on the outbox collection, or Datastream/CDC reading the outbox table and feeding Pub/Sub.

## 324: How would you implement a saga for a multi-service transaction?

There is no distributed transaction across Cloud Run services, Firestore and payment providers, so you use a saga: a sequence of local steps, each with a **compensating action** if a later step fails.

With **Workflows** as the orchestrator:

```yaml
main:
  params: [order]
  steps:
    - reserveStock:
        call: http.post
        args: { url: https://inventory.../reserve, auth: { type: OIDC }, body: ${order} }
    - charge:
        try:
          call: http.post
          args: { url: https://payments.../charge, auth: { type: OIDC }, body: ${order} }
        except:
          as: e
          steps:
            - releaseStock:
                call: http.post
                args: { url: https://inventory.../release, auth: { type: OIDC }, body: ${order} }
            - fail:
                raise: ${e}
    - confirm:
        call: http.post
        args: { url: https://orders.../confirm, auth: { type: OIDC }, body: ${order} }
```

Every step and compensation must be idempotent, because Workflows retries. The alternative is choreography with Pub/Sub events, which avoids a central orchestrator but is harder to follow.

## 325: How do you design idempotent APIs on Google Cloud?

- Clients send an `Idempotency-Key` header for unsafe operations (`POST /payments`).
- The server stores the key with the request hash and the response, in Firestore, Cloud SQL or Memorystore, with a TTL.
- On a repeated key: return the saved response. If the same key comes with a different body, return an error.
- Do the "save key" and "do the work" in one transaction where possible, or use a state field (`processing`, `done`) to handle concurrent retries.

This matters a lot on Google Cloud because many parts retry for you: client libraries, Pub/Sub, Cloud Tasks, Eventarc, Workflows and load balancers.

## 326: What are VPC Service Controls?

VPC Service Controls create a **service perimeter** around projects and Google APIs (Cloud Storage, BigQuery, Secret Manager and others). Requests to protected services from outside the perimeter are blocked, even if the caller has valid IAM credentials.

This protects against **data exfiltration**: a stolen service account token, an insider copying a BigQuery table to a personal project, or a misconfigured bucket cannot move data outside the perimeter.

IAM answers "who can access". VPC Service Controls add "from where and to where". They are common in regulated environments like finance and healthcare.

## 327: How do you roll out VPC Service Controls without breaking things?

1. **Map data flows** first: which services, projects, CI systems, partners and users access the protected APIs.
2. Create the perimeter in **dry-run mode**. Violations are logged but not blocked.
3. Analyze the dry-run logs (`Policy Denied` audit logs, the VPC SC troubleshooter) and add **ingress and egress rules** for legitimate flows, like your CI's service account or a partner's project.
4. Use **access levels** (from Access Context Manager) to allow trusted IP ranges or devices.
5. Enforce, and keep dry-run for future changes.

Common breakages: Cloud Build or third-party SaaS calling APIs, cross-project log sinks and BigQuery queries across projects in and out of the perimeter.

## 328: What is Access Context Manager?

Access Context Manager defines **access levels**: conditions about the request context, such as source IP ranges, device policy (encrypted, managed, OS version), user identity or geographic region.

Access levels are used by:

- VPC Service Controls (allow access into a perimeter only from corporate IPs)
- IAP and Chrome Enterprise Premium (context-aware access to internal apps)
- IAM Conditions

This is the base of Google's zero-trust model (BeyondCorp): access depends on who you are and the state of your device, not on being inside the office network.

## 329: How do you apply least privilege at scale in a large organization?

- Grant roles to **groups**, never individuals, and manage groups through your identity provider.
- Use **predefined roles** on specific resources, not basic roles on projects.
- Use the **IAM recommender** to find and remove permissions that have not been used in 90 days.
- Use **just-in-time access** (Privileged Access Manager) for admin roles: users request elevation for a limited time with approval.
- Use **deny policies** and **principal access boundaries** for hard limits.
- Run regular reviews with Policy Analyzer and Cloud Asset Inventory exports.
- Define IAM in Terraform so changes go through code review.

## 330: What are IAM deny policies?

Deny policies explicitly block permissions for principals, regardless of any allow policies. They are attached to an organization, folder or project and are evaluated **before** allow policies.

```json
{
  "rules": [
    {
      "denyRule": {
        "deniedPrincipals": ["principalSet://goog/public:all"],
        "exceptionPrincipals": [
          "principalSet://goog/group/security-admins@example.com"
        ],
        "deniedPermissions": [
          "iam.googleapis.com/roles.delete",
          "iam.googleapis.com/roles.update"
        ]
      }
    }
  ]
}
```

Use them for guardrails like "nobody except the security team can delete custom roles or change service account keys", even if someone has Owner. Not every permission supports deny yet, so check the supported list.

## 331: What are principal access boundary policies?

A principal access boundary (PAB) policy limits **which resources** a principal is allowed to access at all, no matter what roles they get. For example, all users in your workforce pool can access resources only in your organization.

This blocks a class of attacks where someone with a valid identity is granted access to resources in another organization and uses it to move data out. Allow policies say what you can do, deny policies block specific permissions, and PAB policies set the outer boundary of where a principal can act.

## 332: Why are service account keys such a big risk, and how do you remove them?

Keys are long-lived bearer credentials. They do not expire by default, they can be used from anywhere, and they are often found in Git repos, Docker images, CI variables and laptops. Many real Google Cloud breaches started with a leaked key.

Plan to remove them:

1. Find all keys with Cloud Asset Inventory and check usage with **key usage insights** (Activity Analyzer).
2. Replace each use: attached service accounts on Google Cloud, Workload Identity Federation for external CI and other clouds, impersonation for humans.
3. Disable unused keys first, watch for errors, then delete.
4. Enforce `iam.disableServiceAccountKeyCreation` and `iam.disableServiceAccountKeyUpload` org-wide, with documented exceptions only.
5. Set key expiry (`iam.serviceAccountKeyExpiryHours`) where keys must stay.

## 333: How do you secure Workload Identity Federation configuration?

The main risk is a provider that trusts too much. For example, a GitHub OIDC provider without an attribute condition trusts **every** GitHub repository in the world.

Best practices:

- Always set an **attribute condition** that limits the issuer's tokens to your org, repo, branch or environment (`assertion.repository_owner == 'my-org'`).
- Grant access to narrow principal sets (one repo, or one repo + branch `ref`), not the whole pool.
- Use separate pools per environment or trust domain.
- For GitHub, use repository IDs (`repository_id`, `repository_owner_id`) instead of names, since names can be reused after renaming or deletion.
- Monitor the token exchange in audit logs (`sts.googleapis.com`).

## 334: How does using a service account across projects work?

A service account belongs to one project but can be granted roles in any project. Two different cases:

- **Accessing resources in another project**: just grant the service account a role on that project or resource. Simple.
- **Attaching a service account from project A to a resource in project B** (for example a Cloud Run service in B running as `sa@A`): requires that the `iam.disableCrossProjectServiceAccountUsage` org policy is not enforced in A, and that the deployer has Service Account User on it. B's service agents also need Token Creator on it.

Centralizing service accounts in one project can simplify management, but it also concentrates risk. Many teams keep service accounts in the same project as the workload.

## 335: What are common privilege escalation paths in Google Cloud IAM?

- `iam.serviceAccounts.actAs` (Service Account User) on a powerful account plus permission to deploy compute (Cloud Run, functions, VMs, Cloud Build) → run code as that account.
- `iam.serviceAccountKeys.create` → make a key for a powerful account.
- `iam.serviceAccounts.getAccessToken` (Token Creator) → mint tokens directly.
- `resourcemanager.projects.setIamPolicy` → grant yourself anything.
- `compute.instances.setMetadata` → add SSH keys or a startup script to a VM running as a powerful account.
- Write access to a Cloud Build trigger's repo or config → run builds as the build service account.
- `iam.roles.update` on a custom role you already have.

Audit who holds these permissions, especially on projects with highly privileged service accounts.

## 336: How do you secure a Cloud Run service end to end?

- **Identity**: dedicated service account with minimal roles. No default compute service account.
- **Access**: `--no-allow-unauthenticated` unless it is a public API. Use `roles/run.invoker` for callers, IAP for internal users.
- **Network**: ingress `internal` or `internal-and-cloud-load-balancing`. Cloud Armor on the load balancer. Egress through the VPC with firewall policies if needed.
- **Secrets**: Secret Manager, pinned versions, no secrets in images or env config.
- **Supply chain**: images from Artifact Registry with vulnerability scanning, Binary Authorization to allow only signed images.
- **Data**: CMEK if required, VPC Service Controls around the project.
- **Detection**: audit logs, Security Command Center findings, alerts on IAM changes.

## 337: What is Binary Authorization?

Binary Authorization is a deploy-time policy check for GKE and Cloud Run. It allows only container images that meet your policy, for example images signed by trusted **attestors** (your CI after tests and scans passed), or images from approved registries.

```bash
gcloud run deploy api --image=IMAGE@sha256:... --region=europe-west1 --binary-authorization=default
```

You can start in **dry-run** (audit) mode to see what would be blocked. Combined with Cloud Build provenance and vulnerability scanning, it prevents someone from deploying an untested image straight to production, even if they have deploy permissions. Always deploy by digest, not tag.

## 338: How do you secure the software supply chain on Google Cloud?

- **Source**: protected branches, required reviews, signed commits.
- **Build**: Cloud Build generates **SLSA build provenance** for images, describing what was built from which source by which builder. Use private pools and least-privilege build service accounts.
- **Dependencies**: Artifact Registry remote and virtual repositories to control where packages come from, and Assured Open Source Software for vetted packages.
- **Artifacts**: vulnerability scanning, immutable tags, deploy by digest.
- **Deploy**: Binary Authorization checks provenance and attestations. Cloud Deploy for controlled promotion.
- **Runtime**: GKE security posture dashboard and Security Command Center for runtime threats.

## 339: How do you use secrets safely in Cloud Build?

Use `availableSecrets` with Secret Manager instead of plain substitutions:

```yaml
steps:
  - name: "node:22"
    entrypoint: bash
    args:
      [
        "-c",
        "npm config set //npm.pkg.github.com/:_authToken $$NPM_TOKEN && npm ci",
      ]
    secretEnv: ["NPM_TOKEN"]
availableSecrets:
  secretManager:
    - versionName: projects/$PROJECT_ID/secrets/npm-token/versions/latest
      env: "NPM_TOKEN"
```

Note the `$$` so Cloud Build does not treat it as a substitution. The build service account needs Secret Accessor on that secret only. Do not `echo` secrets, do not write them into image layers (use Docker build secrets or multi-stage builds), and do not pass them as `--build-arg`, which ends up in image history.

## 340: How does key management work in Cloud KMS in more detail?

- **Key ring**: a grouping of keys in a location. Cannot be deleted.
- **Key**: has a purpose (symmetric encrypt/decrypt, asymmetric sign, asymmetric decrypt, MAC) and a protection level (software, HSM, external).
- **Key versions**: the actual key material. Rotation creates a new primary version. Old versions still decrypt old data.
- **Rotation**: automatic for symmetric keys on a schedule. Data is not re-encrypted automatically; services use the new version for new writes.
- **Destruction**: versions are scheduled for destruction with a waiting period (default 30 days), so mistakes can be undone.
- **Separation of duties**: keep keys in a separate project managed by a security team, and grant `cryptoKeyEncrypterDecrypter` only to the service agents that need it.

## 341: What are Cloud HSM and Cloud External Key Manager?

- **Cloud HSM**: keys are created and used inside FIPS 140-2 Level 3 certified hardware security modules managed by Google. You use them through the same KMS API by choosing protection level `HSM`. Needed for some compliance rules.
- **Cloud EKM**: the key stays in a key manager **outside** Google, run by a partner (like Thales or Fortanix) or by you. Google calls it for every encrypt/decrypt operation. You can refuse requests and give reasons (Key Access Justifications).

EKM gives the most control, since Google cannot decrypt the data without your external key, but it adds latency and makes the external system part of your availability.

## 342: How do you do envelope encryption with Cloud KMS?

You encrypt large data locally with a random **data encryption key (DEK)**, then encrypt the DEK with a **key encryption key (KEK)** in KMS. You store the encrypted data and the wrapped DEK together.

```js
import crypto from "node:crypto";
import { KeyManagementServiceClient } from "@google-cloud/kms";

const kms = new KeyManagementServiceClient();
const keyName = kms.cryptoKeyPath(
  "sec-project",
  "europe-west1",
  "app-keys",
  "documents",
);

async function encrypt(plaintext) {
  const dek = crypto.randomBytes(32);
  const iv = crypto.randomBytes(12);
  const cipher = crypto.createCipheriv("aes-256-gcm", dek, iv);
  const data = Buffer.concat([cipher.update(plaintext), cipher.final()]);
  const [{ ciphertext: wrappedDek }] = await kms.encrypt({
    name: keyName,
    plaintext: dek,
  });
  return { data, iv, tag: cipher.getAuthTag(), wrappedDek };
}
```

KMS calls only handle 32 bytes, not the whole file, so this is fast and cheap. KMS has a 64 KiB limit on direct encryption, so large data always needs this pattern. Libraries like Tink do this for you.

## 343: What is Confidential Computing on Google Cloud?

Confidential Computing protects data **in use** by encrypting VM memory with hardware support (AMD SEV, SEV-SNP or Intel TDX). Even Google's hypervisor and operators cannot read the memory.

Available as:

- **Confidential VMs** on Compute Engine
- **Confidential GKE Nodes**
- **Confidential Space** for multi-party computation, where several companies combine sensitive data without seeing each other's raw data
- Confidential options for Dataproc and some GPUs

Usually you turn it on with a flag and no code changes, with a small performance cost. It completes encryption at rest and in transit.

## 344: What is Shielded VM?

Shielded VM protects Compute Engine VMs against boot-level malware and rootkits:

- **Secure Boot**: only boot components signed by trusted keys can run.
- **vTPM**: a virtual Trusted Platform Module for measured boot and key protection.
- **Integrity monitoring**: compares boot measurements to a known good baseline and reports changes in Cloud Monitoring and logs.

Most Google public images support Shielded VM, and you can require it with the `compute.requireShieldedVm` organization policy. GKE nodes use Shielded VMs by default.

## 345: What is Sensitive Data Protection?

Sensitive Data Protection (formerly Cloud DLP) finds, classifies and protects sensitive data like credit card numbers, emails, phone numbers and national IDs.

- **Discovery**: scans BigQuery, Cloud SQL and Cloud Storage across the organization and creates data profiles showing where sensitive data is.
- **Inspection**: checks text, images or storage for sensitive data with built-in and custom detectors.
- **De-identification**: masks, redacts, tokenizes or format-preserving encrypts values, for example before logging or before giving data to analysts.

It is often used to clean logs, chat transcripts and prompts sent to AI models.

## 346: What does Security Command Center provide at higher tiers?

- **Security Health Analytics**: misconfiguration checks (public buckets, open firewalls, MFA, logging gaps) mapped to CIS, PCI DSS and other standards.
- **Event Threat Detection**: finds threats in logs, such as crypto mining, anomalous IAM grants, leaked credentials and data exfiltration.
- **Container Threat Detection**: runtime threats in GKE, like reverse shells and unexpected binaries.
- **Vulnerability findings**: from Web Security Scanner and VM vulnerability scanning.
- **Attack path simulation**: shows how an attacker could reach valuable resources and which findings matter most.
- **Enterprise tier**: adds multi-cloud coverage and SIEM/SOAR features from Google Security Operations.

## 347: Should you enable Data Access audit logs everywhere?

Data Access logs record reads of data and configuration, like every `storage.objects.get` or every Firestore read. They are valuable for security investigations and compliance, but they can be **very large and expensive**.

A balanced approach:

- Enable them for services with sensitive data (Secret Manager, Cloud KMS, BigQuery, Cloud SQL Admin, specific buckets).
- Use **exempted principals** to skip high-volume service accounts whose behavior is known.
- Route them to a central logging project with appropriate retention, possibly to Cloud Storage for cheaper long-term storage.
- Review costs after enabling.

Set the configuration at the organization or folder level so it is consistent.

## 348: A service account key was leaked publicly. What do you do?

1. **Disable the key** immediately (`gcloud iam service-accounts keys disable`), then delete it after confirming nothing legitimate breaks. Do not wait.
2. **Investigate** with audit logs: filter on `protoPayload.authenticationInfo.serviceAccountKeyName` to see what the key was used for, from which IPs, and when.
3. **Check for persistence**: new keys, new service accounts, IAM grants, VMs (crypto miners), Cloud Run services, functions, or changes to org policies made by the attacker.
4. **Contain**: remove attacker-created resources, rotate any secrets the account could read, and check billing for spikes.
5. **Fix the cause**: remove the need for keys (Workload Identity Federation), enable secret scanning in the repo, enforce the no-keys org policy.

Google may also detect public leaks and notify you or disable the key automatically.

## 349: How do you restrict where resources can be created?

Use the resource locations organization policy:

```yaml
name: organizations/123456789/policies/gcp.resourceLocations
spec:
  rules:
    - values:
        allowedValues:
          - in:eu-locations
```

```bash
gcloud org-policies set-policy locations-policy.yaml
```

`in:eu-locations` is a value group that includes EU regions and the EU multi-region. It applies to resources that store data. Some global services (like IAM, or global load balancers) are not limited by it, so for strict residency you also need Assured Workloads, careful service choices and contracts.

## 350: What are Assured Workloads?

Assured Workloads creates folders with controls for a compliance program, like FedRAMP, IL4, CJIS, HIPAA, or EU Data Boundary and sovereign controls.

It automatically applies organization policies that limit regions and services to those that meet the program, can restrict Google support personnel by location and citizenship, and can require CMEK. It also monitors for violations. It is used by public sector and regulated companies that must prove where data is stored and who can access it.

## 351: How does Cloud Run run containers under the hood?

Cloud Run is built on Google's Borg infrastructure. Each instance runs in a sandbox:

- **First generation execution environment**: uses **gVisor**, a user-space kernel that intercepts system calls. Fast startup and strong isolation, but some system calls and file system behaviors are not fully supported.
- **Second generation execution environment**: uses a lightweight **microVM**. Full Linux compatibility (all system calls, namespaces, cgroups, NFS and Cloud Storage FUSE mounts), faster CPU and network performance under sustained load, but slightly slower cold starts.

Cloud Run exposes a Knative-compatible API (`serving.knative.dev/v1`) as well as its own v2 API, so YAML exported from Cloud Run looks like Knative.

## 352: When should you choose the second generation execution environment in Cloud Run?

Choose gen2 when you need:

- Network file systems (NFS, Cloud Storage FUSE volume mounts)
- Full Linux compatibility, for example software that uses unusual system calls or tools like `strace`
- Better CPU and network performance for sustained work
- Bigger memory or CPU configurations, or GPUs

Choose gen1 when cold start speed matters most and your app runs fine in it. Cloud Run jobs and services with certain features use gen2 automatically. If you do not set it, Cloud Run picks a default based on the features used.

```bash
gcloud run services update api --region=europe-west1 --execution-environment=gen2
```

## 353: How does Cloud Run decide how many instances to run?

Cloud Run's autoscaler looks mainly at:

- **Request concurrency**: how many requests are in flight compared to the concurrency setting. It tries to keep instances at about 60% of max concurrency.
- **CPU utilization**: it targets about 60% CPU over a one-minute window.
- **Limits**: min and max instances.

It scales out quickly when load rises. When load drops, it keeps idle instances for a while (up to about 15 minutes) before shutting them down, which helps with short gaps in traffic. You can also choose manual scaling to set a fixed number of instances, for example for services that scale based on an external signal.

## 354: What are Cloud Run worker pools?

Worker pools are a Cloud Run resource type for **non-request** workloads: always-on background processes that pull work, like Pub/Sub pull consumers, Kafka consumers or queue workers.

Unlike services, worker pools have no public endpoint, no request-based autoscaling and no load balancing. You set the number of instances (manually, or with an external autoscaler based on queue backlog). They are cheaper than running a service with instance-based billing just to keep a worker alive.

```bash
gcloud run worker-pools deploy kafka-consumer --image=IMAGE --region=europe-west1 --instances=3
```

Check the current launch stage and flags in the docs, since this resource type is newer than services and jobs.

## 355: How do GPUs work on Cloud Run?

Cloud Run services, jobs and worker pools can attach an NVIDIA GPU (L4, and newer types in some regions) per instance. You still get scale to zero and pay per second, which makes it a cheap way to serve open models (Gemma, Llama) for low or spiky traffic.

```bash
gcloud run deploy llm --image=IMAGE --region=europe-west4 \
  --gpu=1 --gpu-type=nvidia-l4 --cpu=8 --memory=32Gi \
  --no-cpu-throttling --max-instances=3 --concurrency=4
```

Things to know: GPU services require instance-based billing, need minimum CPU and memory, have quotas per region, and cold starts include loading the model, so put the model in the image or load from Cloud Storage FUSE and consider min instances. For large steady traffic, GKE with GPU node pools may be cheaper.

## 356: How do you stop Cloud Run from overwhelming a database?

When traffic spikes, Cloud Run can scale to hundreds of instances, each with a connection pool. A Cloud SQL instance may allow only a few hundred connections.

Controls:

- `max-instances × pool size` must stay under the database's connection limit (minus admin connections).
- Use a **connection pooler**: Cloud SQL managed connection pooling, PgBouncer on a VM or GKE, or AlloyDB's managed pooling.
- **Shed load early**: return 429 or 503 quickly when the pool is exhausted instead of waiting until timeout.
- **Cache reads** in Memorystore.
- **Move writes** that can wait to a queue (Pub/Sub, Cloud Tasks) with controlled consumers.

## 357: Can Cloud Run handle WebSockets, streaming and gRPC?

Yes:

- **WebSockets**: supported, but each connection counts as a request for its whole lifetime, limited by the request timeout (max 60 minutes). Clients must reconnect. Instances do not share state, so use Memorystore or Pub/Sub to broadcast between instances.
- **Server-sent events and response streaming**: supported (HTTP/1.1 chunked or HTTP/2).
- **gRPC**: supported, including streaming, if you enable end-to-end HTTP/2 (`--use-http2`). Your server must then speak h2c (HTTP/2 without TLS).

For long-lived connections, consider instance-based billing, since the instance is "in a request" the whole time anyway.

## 358: How does session affinity work in Cloud Run and what are its limits?

With session affinity enabled, Cloud Run uses a cookie to send requests from the same client to the same instance when possible.

It is **best effort**: if the instance is shut down, scaled in, at max concurrency or a new revision is deployed, the client goes to another instance. So you must never store important state only in instance memory. Use it as an optimization (for example to reuse a local cache or keep WebSocket reconnects on the same instance), with real state in Memorystore, Firestore or a database.

## 359: How do you give a Cloud Run service a static outbound IP?

Some partners need to allowlist your IP. Cloud Run's default egress uses shared Google IPs, so:

1. Connect the service to a VPC with Direct VPC egress (or a connector).
2. Set `--vpc-egress=all-traffic` so internet-bound traffic also goes through the VPC.
3. Create a Cloud Router and Cloud NAT on that subnet's region with a **reserved static IP**.

```bash
gcloud compute addresses create run-egress-ip --region=europe-west1
gcloud compute routers nats create run-nat --router=nat-router --region=europe-west1 \
  --nat-custom-subnet-ip-ranges=run-egress --nat-external-ip-pool=run-egress-ip
gcloud run services update api --region=europe-west1 --network=main --subnet=run-egress --vpc-egress=all-traffic
```

Watch NAT port usage for busy services.

## 360: How does container startup order work in a multi-container Cloud Run service?

By default all containers start at the same time. You can declare dependencies so a container starts only after another container's startup probe passes:

```yaml
spec:
  template:
    metadata:
      annotations:
        run.googleapis.com/container-dependencies: '{"app":["otel-collector"]}'
    spec:
      containers:
        - name: app
          image: IMAGE
          ports:
            - containerPort: 8080
        - name: otel-collector
          image: otel/opentelemetry-collector-contrib:0.110.0
          startupProbe:
            tcpSocket:
              port: 4317
```

Only the container with `ports` gets ingress traffic. The instance is ready when all containers are started. All containers share CPU and memory limits set per container, and if one container exits, the instance is restarted.

## 361: How do you reduce Cloud Run costs?

- Use **request-based billing** for normal APIs, and instance-based only where needed.
- **Raise concurrency** so each instance serves more requests (especially Node.js and Go I/O-bound apps).
- **Right-size CPU and memory**. Check utilization metrics. Many services run fine with 1 vCPU and 512 MiB.
- Keep **min instances** at 0 for non-critical services, or 1 only where cold starts matter.
- Make responses faster: billed time is request time.
- Cache with Cloud CDN for cacheable responses.
- Buy **Cloud Run committed use discounts** for steady spend.
- Use jobs instead of always-on services for batch work, and worker pools instead of services with CPU always on for background consumers.

## 362: What is the difference between allowing unauthenticated access and disabling the invoker IAM check?

- `--allow-unauthenticated` grants `roles/run.invoker` to `allUsers`. This requires that the org allows `allUsers` in IAM policies, which many organizations block with the domain restricted sharing policy.
- `--no-invoker-iam-check` turns off the IAM invoker check for the service entirely. The service is public without adding `allUsers` to its policy, so it works in orgs that block `allUsers`.

Either way the service is public, and your code must handle authentication itself (for example Firebase Auth tokens). Use ingress settings and Cloud Armor to limit who can reach it.

## 363: How does GKE Autopilot pricing and scheduling work?

Autopilot bills **per pod** for the CPU, memory and ephemeral storage the pod **requests**, with a minimum per pod and rounding. Nodes are invisible to you.

Things to know:

- If you do not set requests, Autopilot applies defaults, which may be bigger than you need.
- Requests should match real usage. Overrequesting costs money, underrequesting gets you throttled or OOM-killed.
- You can choose **compute classes** (like `Balanced`, `Scale-Out`, `Performance`, Spot or specific machine families) per workload with a node selector.
- Some things are restricted: privileged containers, most host access, and some DaemonSets unless allowlisted partner workloads.

Autopilot removes node management and bin-packing waste, which often makes it cheaper than Standard for teams that would otherwise overprovision nodes.

## 364: How does the GKE metadata server work with Workload Identity Federation?

With Workload Identity Federation for GKE enabled, each node runs a **GKE metadata server** as a DaemonSet. Pod calls to `169.254.169.254` (the normal metadata address) are intercepted by it instead of reaching the Compute Engine metadata server.

When a client library asks for a token, the GKE metadata server sees which pod and Kubernetes service account made the request, exchanges the KSA's identity for a federated token (and impersonates a linked IAM service account if configured), and returns a short-lived token.

This means pods **cannot** see the node's service account, which is a big security improvement. It also means apps starting very quickly might call the metadata server before it is ready, so client libraries retry.

## 365: How do you control pod-to-pod traffic in GKE?

Use **Kubernetes NetworkPolicies**, enforced by **GKE Dataplane V2** (based on eBPF and Cilium), which is the default for Autopilot and new clusters.

```yaml
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
  name: api-allow-from-frontend
  namespace: shop
spec:
  podSelector:
    matchLabels:
      app: api
  policyTypes: ["Ingress"]
  ingress:
    - from:
        - podSelector:
            matchLabels:
              app: frontend
      ports:
        - port: 8080
```

Start with a default-deny policy per namespace and add allow rules. Dataplane V2 also provides network policy logging, so you can see allowed and denied connections. For Layer 7 rules and mTLS, add a service mesh.

## 366: How do you run applications across multiple GKE clusters?

- **Fleets**: group clusters (in one or more projects and regions) for shared management features.
- **Multi-cluster Gateway**: one global external load balancer that routes to services in several clusters, with health-based failover and traffic splitting between clusters.
- **Multi-cluster Services (MCS)**: services exported from one cluster can be discovered in others (`service.clusterset.local`).
- **Config Sync**: GitOps sync of the same config to all fleet clusters.
- **Cloud Service Mesh**: mTLS and traffic management across clusters.

Use multi-cluster for regional redundancy, data residency per region, or limiting the blast radius of upgrades.

## 367: How do you upgrade GKE nodes safely?

**Surge upgrades** (default): GKE adds new nodes (`max-surge`) and drains old ones (`max-unavailable`) a few at a time. Fast and cheap, but if the new version has a problem, rollback is slow.

**Blue-green upgrades**: GKE creates a full set of new nodes, moves pods over in batches with soak time, and keeps the old nodes until you confirm. Rolling back is quick, but you temporarily need double capacity and quota.

In both cases:

- Set **PodDisruptionBudgets** so drains do not take down too many replicas at once.
- Make apps handle `SIGTERM` and set `terminationGracePeriodSeconds`.
- Test upgrades in staging clusters on a faster release channel first.

## 368: What role do PodDisruptionBudgets play in GKE?

A PDB limits how many pods of an app can be voluntarily disrupted at once, for example during node drains for upgrades, autoscaler scale-down or maintenance.

```yaml
apiVersion: policy/v1
kind: PodDisruptionBudget
metadata:
  name: api-pdb
spec:
  minAvailable: 2
  selector:
    matchLabels:
      app: api
```

Without PDBs, an upgrade can drain all replicas of a service at once. But a too-strict PDB (like `maxUnavailable: 0` or `minAvailable` equal to replicas) blocks drains. GKE respects PDBs for up to about an hour during upgrades and then may evict anyway.

## 369: How do you use Spot VMs safely in GKE?

- Create a Spot node pool (Standard) or use the Spot compute class (`cloud.google.com/gke-spot: "true"` node selector in Autopilot).
- Run only **fault-tolerant** workloads there: stateless replicas, batch jobs, CI runners.
- Keep an on-demand node pool for critical pods and use **taints and tolerations** or node affinity so they do not land on Spot nodes.
- Handle the short termination notice: GKE gives pods a limited graceful shutdown period on Spot preemption, so keep `terminationGracePeriodSeconds` short and save progress often.
- Spread replicas across zones and machine types to reduce the chance that all Spot capacity disappears at once.

## 370: How do you optimize GKE costs?

- Use **Autopilot** if you do not need node-level control.
- **Right-size requests** with VPA recommendations and the GKE cost insights.
- Enable **cluster autoscaler** with the `optimize-utilization` profile, and **HPA** to scale replicas with load.
- Use **Spot** for fault-tolerant workloads.
- Use **committed use discounts** for steady baseline nodes.
- Scale down non-prod clusters at night and on weekends.
- Enable **GKE cost allocation** to see costs per namespace and team, which makes owners care.
- Remove unused load balancers, persistent volumes and idle node pools.

## 371: What causes IP address exhaustion in GKE and how do you fix it?

In VPC-native clusters, each node reserves a block of pod IPs from the pod secondary range (by default a `/24`, 256 IPs, for up to 110 pods). A `/20` pod range only supports 16 nodes at that setting. When the range is used up, the cluster cannot add nodes even if pods are pending.

Fixes:

- Lower **max pods per node** (for example 32 → smaller per-node block) so more nodes fit.
- **Add additional pod ranges** to the cluster (discontiguous multi-pod CIDR), which works on existing clusters.
- Use **Class E** or other non-RFC1918 ranges for pods where your network allows it.
- Plan ranges generously at cluster creation, and keep pod ranges out of the shared corporate range plan when possible.

## 372: How do you attach Cloud Armor, IAP and other settings to services exposed with the GKE Gateway API?

GKE uses **policy resources** attached to Kubernetes Services:

```yaml
apiVersion: networking.gke.io/v1
kind: GCPBackendPolicy
metadata:
  name: api-backend-policy
  namespace: shop
spec:
  default:
    securityPolicy: api-armor-policy
    timeoutSec: 30
    logging:
      enabled: true
      sampleRate: 500000
  targetRef:
    group: ""
    kind: Service
    name: api
---
apiVersion: networking.gke.io/v1
kind: HealthCheckPolicy
metadata:
  name: api-health
  namespace: shop
spec:
  default:
    config:
      type: HTTP
      httpHealthCheck:
        requestPath: /healthz
  targetRef:
    group: ""
    kind: Service
    name: api
```

`GCPBackendPolicy` can also enable IAP, connection draining and session affinity. `GCPGatewayPolicy` controls Gateway-level settings like SSL policies. This replaces the `BackendConfig` and `FrontendConfig` resources used with Ingress.

## 373: What is Cloud Service Mesh?

Cloud Service Mesh is Google's managed service mesh, based on Istio APIs (and in some modes on Traffic Director). It works with GKE and VMs, and has a managed control plane.

It gives you:

- **mTLS** between services automatically, with workload identities
- **Authorization policies** (service A may call service B on `/payments` only)
- **Traffic management**: retries, timeouts, circuit breaking, traffic splitting, fault injection
- **Observability**: golden signals per service and a service topology view

A mesh adds complexity and some latency. It is worth it when you have many services with strict security needs, not for a few services that Cloud Run IAM already covers well.

## 374: What is live migration in Compute Engine?

When Google needs to do host maintenance (hardware repair, software updates, security patches), Compute Engine moves running VMs to another host **without rebooting them**. Memory is copied while the VM runs, then the VM is paused for a very short time and resumed on the new host.

Your app keeps running, and open connections usually survive. Some VMs cannot live migrate: those with certain GPUs, some Confidential VMs, and Spot VMs. Those are stopped or terminated instead, with advance notice through the metadata server (`maintenance-event`), so your app can prepare.

## 375: How do regional managed instance groups spread VMs and handle capacity shortages?

A regional MIG spreads VMs across zones in a region. Distribution shapes:

- **EVEN**: same number of VMs per zone.
- **BALANCED**: tries to balance but can place more in zones with capacity.
- **ANY**: places VMs wherever capacity is available, good for batch.
- **ANY_SINGLE_ZONE**: all VMs in one zone, good when VMs talk to each other a lot.

**Instance flexibility** lets one MIG use several machine types. If one type is out of stock in a zone, it creates another type from your list. This is very useful for Spot and GPU workloads, where capacity is limited. Combine with **resize requests** to get VMs when capacity becomes available.

## 376: What are stateful managed instance groups?

A stateful MIG keeps specific state for each VM across recreation, autohealing and updates:

- **Persistent disks** stay attached to the same instance name
- **Instance names** stay the same
- **Internal and external IPs** can be preserved
- **Metadata** per instance

It lets you run stateful apps like databases, Kafka or Elasticsearch on MIGs and still get autohealing and rolling updates. Autoscaling is not supported for stateful MIGs, because removing a VM would remove its state.

## 377: What are sole-tenant nodes and placement policies?

- **Sole-tenant nodes**: physical servers dedicated to your project. Your VMs do not share hardware with other customers. Used for compliance, and for bring-your-own-license software licensed per physical core or socket (like some Windows Server and SQL Server licenses).
- **Placement policies**:
  - **Spread placement**: puts VMs on different hardware to reduce correlated failures.
  - **Compact placement**: puts VMs physically close for very low network latency, used for HPC and tightly coupled workloads.

## 378: How does Google's global load balancer work internally?

- **Anycast IP**: the same IP is announced from many Google edge locations worldwide. Users connect to the nearest one through BGP.
- **Google Front Ends (GFEs)** or **Envoy-based proxies** at the edge terminate TCP and TLS close to the user, which reduces handshake latency.
- Traffic travels on **Google's private backbone** to the selected backend region, chosen by health, capacity and proximity.
- **Maglev** is Google's distributed software load balancer for packet-level (Layer 4) balancing using consistent hashing.
- **Andromeda** is the software-defined networking stack that virtualizes the VPC network and delivers traffic to VMs.

There are no load balancer instances to pre-warm. It scales to millions of requests per second without warm-up.

## 379: Why does the Premium Tier network matter for performance?

With Premium Tier, user traffic enters Google's network at the closest of more than 100 edge points of presence and then travels on Google's private fiber. With Standard Tier, traffic travels over the public internet to the region.

Benefits of Premium Tier:

- Lower and more stable latency, especially for users far from the region
- TLS terminated at the edge with the global load balancer
- One global anycast IP for multi-region backends
- Better protection against network-level DDoS at the edge

The cost is higher egress pricing. For global consumer apps, Premium is almost always the right choice.

## 380: When would you choose a regional load balancer over a global one?

- **Data residency or sovereignty**: a regional load balancer terminates TLS only in that region, while a global one can terminate TLS at any edge location worldwide.
- **Standard Tier networking** to save egress costs.
- **Isolation**: a regional failure domain, with no shared global configuration.
- **Features**: some features exist only on one kind, and internal load balancers are mostly regional (with a cross-region internal option).

For most public apps, global is better. For strict EU-only processing, regional external Application Load Balancers with backends in the EU are a common answer.

## 381: How do you design hybrid connectivity between on-prem and Google Cloud?

1. **Bandwidth and SLA**: under a few Gbps and OK with internet paths → HA VPN. Higher bandwidth, lower latency and steady throughput → Dedicated or Partner Interconnect.
2. **Redundancy**: for a 99.99% SLA, use two Interconnect connections in two metro areas (four connections in total) or HA VPN with two tunnels, and two Cloud Routers.
3. **Routing**: BGP with Cloud Router. Choose **global dynamic routing** so all regions learn on-prem routes. Use custom route advertisements to announce the right ranges.
4. **IP planning**: no overlap between on-prem and cloud ranges.
5. **DNS**: forwarding zones and inbound server policies for hybrid DNS.
6. **Security**: HA VPN over Interconnect or MACsec if encryption on the link is required.

## 382: What is Network Connectivity Center?

Network Connectivity Center (NCC) is a hub-and-spoke model for connecting many networks. The hub is a global resource, and spokes can be:

- VPC networks (VPC spokes)
- HA VPN tunnels, Interconnect attachments and router appliances (hybrid spokes)

It solves the non-transitive peering problem: VPC spokes on the same hub can talk to each other, and hybrid spokes give site-to-site connectivity using Google's backbone. It is easier to manage than a full mesh of peerings when you have many VPCs, for example one VPC per business unit.

## 383: How do you set up DNS for a hybrid environment?

- **Cloud to on-prem**: create a **forwarding zone** in Cloud DNS for `corp.example.com` that forwards to on-prem DNS servers through VPN or Interconnect.
- **On-prem to cloud**: create an **inbound server policy** on the VPC. It gives entry-point IPs in each region. Configure on-prem DNS to forward cloud zones (like `gcp.example.com` or `googleapis.com` for Private Google Access) to those IPs.
- **Many VPCs**: put the forwarding and private zones in a hub VPC and use **DNS peering** from spoke VPCs.
- **Private API access**: create a private zone for `googleapis.com` pointing to `private.googleapis.com` or a PSC endpoint, so on-prem traffic to Google APIs stays private.

## 384: How do you reduce network egress costs on Google Cloud?

- Keep compute and data **in the same region**. Cross-region and cross-zone traffic is billed.
- Use **Cloud CDN** for cacheable content. CDN egress is cheaper than direct egress and reduces origin traffic.
- **Compress** responses (gzip, Brotli) and use efficient formats.
- Use **Private Google Access** and internal IPs instead of public endpoints.
- Avoid chatty cross-region service calls. Batch or replicate data locally.
- Consider **Standard Tier** for traffic where latency is less important.
- For hybrid, **Interconnect** egress is cheaper per GB than internet egress.
- Use the billing export to find which SKU and project drive egress.

## 385: How do you publish an internal service to other teams with Private Service Connect?

1. Put your service behind an **internal load balancer** (for example a regional internal Application LB or passthrough NLB) in your producer VPC.
2. Create a **PSC subnet** used for NAT of consumer traffic.
3. Create a **service attachment** pointing to the load balancer's forwarding rule, with an accept list of consumer projects:

```bash
gcloud compute service-attachments create orders-svc --region=europe-west1 \
  --producer-forwarding-rule=orders-ilb-fr --connection-preference=ACCEPT_MANUAL \
  --consumer-accept-list=team-b-project=10 --nat-subnets=psc-nat-subnet
```

4. Consumers create an **endpoint** in their own VPC pointing to the service attachment and get a private IP.

IP ranges can overlap between producer and consumer, and consumers cannot reach anything except the published service.

## 386: How do you connect serverless services to a private database securely?

A typical pattern:

- Cloud SQL or AlloyDB with **private IP only** (PSC or private services access).
- Cloud Run with **Direct VPC egress** to a dedicated subnet and `--vpc-egress=private-ranges-only`.
- **Firewall rules** that allow only that subnet (or network tags on the Cloud Run revision) to reach the database port.
- **IAM database authentication** with the service's service account, so no passwords.
- Connectors or the Auth Proxy for TLS and IAM authorization.
- Connection pool limits matched to Cloud Run max instances.

This gives no public exposure, no shared passwords, and access tied to the workload identity.

## 387: How would you implement rate limiting across a distributed API on Google Cloud?

Options by layer:

- **Edge**: Cloud Armor rate limiting by IP, header or API key. Cheap and stops abuse before it reaches your code.
- **API management**: Apigee or API Gateway quotas per consumer key.
- **Application**: a shared counter in **Memorystore** with a sliding window or token bucket, keyed by user or tenant. All instances share the same counters.

```js
async function allow(userId, limit = 100, windowSec = 60) {
  const key = `rl:${userId}:${Math.floor(Date.now() / 1000 / windowSec)}`;
  const count = await redis.incr(key);
  if (count === 1) await redis.expire(key, windowSec);
  return count <= limit;
}
```

- **Downstream protection**: Cloud Tasks queues with `max-dispatches-per-second` to call third-party APIs at a fixed rate.

## 388: When would you use Apigee and what does it give you?

Use Apigee when APIs are a product: many external consumers, partners, different plans, and the need for strong governance.

It provides:

- A proxy layer with policies: authentication (OAuth, API keys, JWT), quotas, spike arrest, transformations, caching
- **Developer portal** for onboarding and API key management
- **Analytics** on usage, latency and errors per developer and app
- **Monetization** with rate plans
- **Advanced API Security** to detect abuse and misconfigured APIs
- Hybrid deployment (Apigee hybrid) to run the runtime in your own Kubernetes

For internal service-to-service APIs it is usually too much; Cloud Run IAM, a load balancer, or a mesh is enough.

## 389: How would you design a multi-tenant SaaS on Google Cloud?

Choose an isolation model per tenant tier:

- **Pooled**: all tenants share services and databases, with `tenant_id` on every row. Cheapest. Enforce isolation with row-level security in PostgreSQL, tenant-aware Firestore rules, or BigQuery row access policies.
- **Siloed**: each tenant gets its own project (or database), created by automation. Strongest isolation, easy cost tracking per tenant, but more to manage.
- **Bridge**: shared compute, separate databases or schemas per tenant.

Other points: tenant identity with Identity Platform multi-tenancy, per-tenant rate limits and quotas, per-tenant CMEK if customers require it, noisy-neighbor protection (separate queues or Pub/Sub ordering keys per tenant), and labels or projects for cost per tenant.

## 390: What is a landing zone and how do you build one on Google Cloud?

A landing zone is the base setup of an organization before apps move in: resource hierarchy, identity, networking, security guardrails, logging and billing.

Typical parts:

- Folder structure per environment and business unit
- Groups and IAM model, with break-glass accounts
- Organization policies baseline
- Shared VPC host projects with hub-and-spoke or NCC, hybrid connectivity, Cloud DNS
- Centralized logging (aggregated sinks) and monitoring
- Security Command Center, VPC Service Controls for sensitive data
- Project factory: automation that creates projects with labels, budgets and baseline config

Google provides the **Enterprise Foundations Blueprint** and **Cloud Foundation Fabric** (Terraform), and the console has a setup checklist that generates Terraform for you.

## 391: How do you structure Terraform for a large Google Cloud setup?

- **Layers** with separate state: org/foundation (folders, org policies, IAM), networking, shared services, and per-app or per-environment stacks. Changes in an app should not plan the whole org.
- **Reusable modules** (your own or Google's terraform-google-modules / Cloud Foundation Fabric) for projects, networks, Cloud Run services and so on.
- **One state per environment** in a GCS backend with versioning, with access limited to the CI service account.
- **CI/CD**: `terraform plan` on pull requests posted as a comment, `apply` after merge, using Workload Identity Federation and impersonation of per-layer service accounts.
- **Policy checks** before apply (see the next question).
- **Pin provider and module versions**, and upgrade them on purpose.

## 392: How do you enforce policies on Terraform changes before they are applied?

- **Policy as code** on the plan: use `gcloud beta terraform vet` (Policy Library with constraint templates), OPA/Conftest, or Sentinel in Terraform Cloud. For example "no public buckets", "all resources have labels", "only allowed regions".
- **Organization policies and custom org policy constraints** as the final enforcement layer in Google Cloud. Even if a check is skipped, the API refuses the change.
- **Drift detection**: run scheduled `terraform plan` to find changes made outside Terraform, and alert on them. Cloud Asset Inventory feeds can also notify on changes to important resources.
- **Restrict console write access** in production so Terraform is the only path for changes.

## 393: Which organization-wide guardrails are the most important?

In order of impact for most companies:

1. **No service account keys** and no default Editor grants.
2. **Domain restricted sharing**: only your identities can get IAM roles (blocks `allUsers` and outside accounts).
3. **Public access prevention** for Cloud Storage and restrict public IPs on Cloud SQL and VMs.
4. **Resource locations** for data residency.
5. **Centralized, immutable audit logging** with an aggregated sink to a locked bucket in a security project.
6. **Budgets and alerts** on every project.
7. **Security Command Center** enabled org-wide.
8. **VPC Service Controls** around sensitive data projects.

## 394: How would you migrate an app from AWS to Google Cloud?

1. **Assess**: inventory services and dependencies, data volumes, latency needs and licensing. Map services (EC2 → Compute Engine, ECS/Fargate → Cloud Run or GKE, RDS → Cloud SQL, S3 → Cloud Storage, SQS/SNS → Pub/Sub or Cloud Tasks, Lambda → Cloud Run functions, IAM roles → service accounts).
2. **Foundation**: landing zone, networking, Cross-Cloud Interconnect or HA VPN to AWS during the migration.
3. **Data**: Storage Transfer Service for S3, Database Migration Service for RDS with continuous replication, BigQuery Data Transfer Service for Redshift.
4. **Workloads**: containerize where possible and deploy to Cloud Run or GKE. Migrate to Virtual Machines for VMs that must move as they are.
5. **Cutover** per service with DNS weighting, keep rollback paths, then decommission AWS resources.

Watch out for differences: global VPCs, IAM model (no assume-role, but impersonation), and quotas that may need increases in advance.

## 395: How do you migrate a production database with near-zero downtime?

1. **Set up continuous replication** to the target (Database Migration Service, native replication, or Datastream). Initial copy, then ongoing CDC.
2. **Validate**: compare row counts and checksums, run the app's read paths against the target.
3. **Lower DNS/connection TTLs** and prepare config so the app can switch with one change.
4. **Cutover window**: put the app in read-only mode or stop writes briefly, wait until replication lag is zero, promote the target, switch the app to the target.
5. **Keep reverse replication** or a fallback plan for a period, in case of problems.

If the schema also changes, use the **expand and contract** pattern: make the schema compatible with both old and new code, migrate, then remove old columns later.

## 396: How does Cloud SQL high availability work internally, and what happens during failover?

The primary and standby are in different zones. Data is on **regional persistent disk**, which synchronously replicates every write to both zones. The standby is not running queries.

On failure (detected through heartbeats), Cloud SQL:

1. Fences the old primary so it cannot write.
2. Attaches the regional disk to the standby and starts the database there, which does crash recovery.
3. Moves the instance's IP to the new primary.

Clients see dropped connections for about a minute, then can reconnect to the same IP. Enterprise Plus reduces downtime further. Apps must have connection retry logic. HA does not protect against bad queries or data deletion; that is what backups and PITR are for.

## 397: How do you design cross-region disaster recovery for Cloud SQL?

- Create a **cross-region read replica** in the DR region. It receives async replication, so RPO is the replication lag (usually seconds).
- On disaster, **promote** the replica to a standalone primary and point apps to it. With Enterprise Plus, use **advanced disaster recovery**: designate the replica as a DR replica and use **switchover** (planned, no data loss) or **replica failover** (unplanned), which keeps the replication setup and the write endpoint easier to manage.
- Keep **backups in another region** too, in case of logical corruption that replicates.
- Automate the runbook with Terraform or scripts and test it regularly.
- Make sure the app, secrets, and network in the DR region are ready.

## 398: How do you tune Cloud SQL for PostgreSQL performance?

- **Query Insights**: find the slowest queries, wait events and which app (with tags like `sqlcommenter`) sends them.
- **Indexes**: check `EXPLAIN (ANALYZE, BUFFERS)` for sequential scans on large tables. Use the index advisor recommendations.
- **Memory**: choose a machine with enough RAM for the working set. Enterprise Plus data cache helps read-heavy workloads.
- **Flags**: tune `work_mem`, `max_connections`, `autovacuum` settings through database flags.
- **Connections**: pool connections. Too many connections waste memory.
- **Storage**: IOPS scale with disk size on SSD, so a larger disk can be faster. Enable automatic storage increase.
- **Reads**: move them to read replicas or a cache.
- **Vacuum**: watch for table bloat and long-running transactions that block vacuum.

## 399: How do you manage database connections for thousands of serverless instances?

- Put a **connection pooler** between the app and the database: Cloud SQL managed connection pooling, AlloyDB managed pooling, or PgBouncer in transaction mode on GKE or a MIG.
- Keep **app-side pools small** and set short idle timeouts.
- **Limit concurrency** at the source: Cloud Run max instances, Pub/Sub flow control, Cloud Tasks rate limits.
- Use **Spanner or Firestore** for workloads that really need massive concurrency, because they do not have a connection-per-client model.
- Use **read replicas** behind a pooler for read scaling.

Transaction-mode pooling breaks session features (prepared statements in some drivers, `SET`, advisory locks), so test the driver settings.

## 400: How do Memorystore failover and client behavior affect app reliability?

With Standard tier Redis or Valkey/Redis Cluster with replicas, a primary failure triggers automatic failover to a replica, usually within seconds. During that time:

- Writes fail and connections drop.
- Recent writes that were not yet replicated can be **lost** (replication is async).
- Cluster mode clients must refresh their slot map (they get `MOVED` errors).

So:

- Use clients with **automatic reconnect** and retry with backoff.
- Treat the cache as **losable**. The source of truth stays in the database.
- For cluster mode, use a cluster-aware client and connect through the discovery endpoint.
- Do not use Memorystore as the only store for important data like payments or orders.

## 401: What is a cache stampede and how do you prevent it?

A cache stampede happens when a popular cache key expires and many requests miss at the same time. They all hit the database together to rebuild the same value, which can overload it.

Prevention:

- **Locking**: only one request rebuilds the value (for example `SET key:lock NX EX 10` in Redis). Others wait briefly or serve stale data.
- **Stale-while-revalidate**: keep serving the old value while one worker refreshes it in the background.
- **Jittered TTLs**: add randomness so keys do not expire at the same moment.
- **Early refresh**: refresh hot keys before expiry, with probability increasing as expiry approaches.
- **Request coalescing** in each instance: share one in-flight promise per key.

## 402: How would you design uploading and processing of very large files?

1. The client asks the backend for an upload URL. The backend checks permissions and creates a **resumable upload session** or V4 signed URL.
2. The client uploads directly to a **staging bucket**, resuming on failures.
3. An **Eventarc trigger** on object finalize starts processing: a Cloud Run service for small work, or a **Cloud Run job / Batch / Dataflow** for heavy work, often through Pub/Sub for buffering.
4. Processing writes results to a separate bucket (to avoid trigger loops) and updates status in Firestore.
5. The client sees progress through Firestore listeners or polling.
6. **Lifecycle rules** clean up the staging bucket.

For very large files, use parallel composite uploads or chunked processing (`Range` reads) so several workers can process parts at the same time.

## 403: Can object naming affect Cloud Storage performance?

Yes, at very high request rates. Cloud Storage splits the object namespace into key ranges by name. Names that are sequential, like `logs/2026-10-29T10:00:01.json`, `logs/2026-10-29T10:00:02.json`, send all new writes to the same range.

Cloud Storage auto-scales by splitting ranges, but this takes time. When you suddenly go to thousands of writes per second with sequential names, you can get 429 or 503 errors.

Fixes: add a short hash prefix (`a3f9/logs/2026-...`), ramp up gradually (doubling the request rate no faster than every 20 minutes), and retry 429/503 with exponential backoff.

## 404: Why might users still see old content after you update a file in Cloud Storage?

Cloud Storage itself is strongly consistent, but **caches** are not:

- Publicly readable objects get `Cache-Control: public, max-age=3600` by default, so browsers and Google's edge caches can keep the old version for up to an hour.
- Cloud CDN in front of a bucket caches based on headers and its own TTL settings.

Fixes:

- Use **content-hashed file names** (`app.3f9a1c.js`) and set a long `max-age` for them, with `index.html` set to `no-cache`.
- Set `Cache-Control` metadata explicitly on upload.
- **Invalidate** Cloud CDN paths after deploys if you must reuse names.

## 405: How would you design a data lake and warehouse on Google Cloud?

A common lakehouse design:

- **Ingestion**: Pub/Sub for events, Datastream for database CDC, Storage Transfer Service and BigQuery Data Transfer Service for batch sources.
- **Storage**: raw files in Cloud Storage in open formats (Parquet, Iceberg), organized in zones like `raw`, `cleaned` and `curated`. Native BigQuery tables for hot, curated data.
- **Table layer**: **BigLake** tables (including BigLake Iceberg tables) so BigQuery, Spark and other engines share the same data with consistent security.
- **Processing**: SQL in BigQuery with **Dataform** for transformations, Dataflow for streaming, Dataproc Serverless for Spark.
- **Governance**: **Dataplex** for catalog, lineage, data quality and policy tags.
- **Consumption**: Looker, Looker Studio, BigQuery ML and AI agents over the curated layer.

## 406: How do windows and watermarks work in Dataflow streaming pipelines?

Streaming data is grouped into **windows** by event time:

- **Fixed windows**: non-overlapping, like every 1 minute.
- **Sliding windows**: overlapping, like 5-minute windows every minute.
- **Session windows**: grouped by activity with gaps, per key.

Events can arrive late. The **watermark** is Dataflow's estimate of how far event time has progressed, meaning "we think all events before time T have arrived". When the watermark passes the end of a window, the window's result is emitted.

**Triggers** control when results are emitted (early, on time, late), and **allowed lateness** controls how long late data still updates a window. With Pub/Sub as the source, Dataflow uses publish time or a timestamp attribute for event time.

## 407: What makes Dataflow scale and process exactly once?

- **Autoscaling**: horizontal autoscaling adds and removes workers based on backlog and CPU. Vertical autoscaling (with Dataflow Prime) changes worker memory.
- **Streaming Engine**: moves state and shuffle from worker VMs to a Google backend, so workers are lighter and scaling is faster.
- **Dynamic work rebalancing**: splits slow work items in batch pipelines to deal with stragglers.
- **Exactly-once processing**: Dataflow checkpoints state and deduplicates records internally, so each record affects the result once. Sinks must also be idempotent or transactional for end-to-end exactly-once. There is also an **at-least-once streaming mode**, cheaper and lower latency, for pipelines that can handle duplicates.

## 408: When can you skip Dataflow and send Pub/Sub data straight to BigQuery?

Use a **BigQuery subscription** when:

- Messages map directly to table columns (with a topic schema or JSON matching the table schema)
- You need no joins, aggregations or complex transformations before storage
- At-least-once delivery is OK, or you deduplicate later in SQL

Single message transforms (SMTs) can do light per-message changes, like renaming fields or masking values, without Dataflow.

Use **Dataflow** when you need windowed aggregation, enrichment with other data, complex parsing, exactly-once into BigQuery, or writing to several sinks. Many teams start with BigQuery subscriptions and transform inside BigQuery with SQL afterwards (ELT), which is simpler and cheaper.

## 409: What would a complete observability setup for a Google Cloud app look like?

- **Logs**: structured JSON logs with severity, request ID and trace ID, routed by sinks: app logs to log buckets with 30-90 days retention, audit logs to a central security project, long-term archives to Cloud Storage.
- **Metrics**: built-in service metrics plus OpenTelemetry custom metrics for business events (orders, payments). Managed Prometheus on GKE.
- **Traces**: OpenTelemetry auto-instrumentation, trace context propagated through HTTP and Pub/Sub, sampling tuned for cost.
- **Errors and profiles**: Error Reporting and Cloud Profiler.
- **SLOs**: per user-facing journey, with multi-window burn-rate alerts to on-call.
- **Dashboards**: golden signals (latency, traffic, errors, saturation) per service.
- **Runbooks**: linked from each alert.

## 410: How do you control logging costs at large scale?

- **Measure first**: use the log volume metrics (`logging.googleapis.com/billing/bytes_ingested`) per resource and log name to find the biggest sources.
- **Exclude** noisy logs at the sink: health checks, load balancer logs for successful requests, verbose debug logs, Kubernetes system noise.
- **Sample** high-volume logs (for example keep 10% of 2xx request logs) with exclusion filters using `sample()`.
- **Lower verbosity** in libraries and the app in production.
- **Route** long-term data to Cloud Storage (cheap) instead of keeping it in log buckets.
- **Use metrics** instead of logs for counting things.
- Set **budgets** with alerts on the logging SKUs.

## 411: How do you centralize logs from all projects in an organization?

Create an **aggregated sink** at the organization or folder level with `--include-children`:

```bash
gcloud logging sinks create org-audit-sink \
  logging.googleapis.com/projects/central-logging/locations/europe-west1/buckets/audit \
  --organization=123456789 --include-children \
  --log-filter='logName:"cloudaudit.googleapis.com"'
```

Then grant the sink's writer identity `roles/logging.bucketWriter` on the destination bucket.

Best practices: put the destination in a dedicated security project with limited access, **lock the retention** on the log bucket so logs cannot be deleted, enable Log Analytics for SQL queries, and optionally also export to BigQuery or a SIEM. You can use **intercepting** sinks to stop logs from also going to child projects if you want them stored only centrally.

## 412: How do you avoid alert fatigue in Cloud Monitoring?

- **Alert on symptoms**, not causes. Alert when users are affected (SLO burn rate, error rate, latency) rather than on every high CPU.
- Use **multi-window, multi-burn-rate** alerts: a fast burn over 1 hour (page now) and a slow burn over 6 hours or more (ticket).
- Set **durations** and use rolling windows so one spike does not page anyone.
- Route by **severity**: pages only for urgent, user-impacting issues, everything else to a ticket or chat channel.
- Attach **documentation** with a runbook to each alert.
- **Review alerts** regularly and remove or tune the ones nobody acts on.

## 413: Users report the API is slow. How do you find the cause?

1. **Confirm and scope**: check latency percentiles (p50, p95, p99) by service, revision, region and endpoint. Is it everyone or some users? Did it start at a deploy?
2. **Traces**: open slow traces in Cloud Trace to see which span takes the time: the service itself, a database query, or a downstream call.
3. **Saturation**: check CPU, memory, instance count at max, connection pool waits, Cloud SQL CPU and locks, Memorystore latency.
4. **Cold starts**: check if slow requests line up with new instances starting (Cloud Run startup latency metric).
5. **Dependencies**: third-party API latency, NAT port exhaustion, DNS issues.
6. **Profiles**: Cloud Profiler for CPU hot spots in the code.
7. **Fix and verify** with the same metrics, and add an SLO alert so you notice before users do next time.

## 414: A Cloud Run service suddenly returns HTTP 429 errors. What could be wrong?

429 from Cloud Run usually means there is **no instance available** to take the request:

- **Max instances reached** and all instances are at max concurrency. Check the instance count metric.
- **Quota limits** in the region (total instances or CPU across services).
- **Sudden traffic spike** faster than scale-out, especially with slow cold starts.
- Concurrency set very low (like 1) with slow requests.

Fixes: raise max instances (if the backend can handle it), raise concurrency if the app supports it, add min instances for baseline capacity, speed up startup, request a quota increase, and make clients retry 429 with backoff. Also check whether the 429 comes from your own code or a downstream API, by looking at the logs.

## 415: The backlog on a Pub/Sub subscription keeps growing. How do you investigate?

1. **Metrics**: `num_undelivered_messages`, `oldest_unacked_message_age`, ack and nack rates, and for push subscriptions the push request latency and response codes.
2. **Is anyone consuming?** Subscribers crashed, a deploy broke them, or a push endpoint returns errors (404, 401 after an IAM change, 500).
3. **Are messages failing and looping?** A poison message being nacked again and again. Look for repeated message IDs in logs, and set up a dead-letter topic.
4. **Too slow?** Processing time per message increased (slow database), or flow control limits too low for the traffic.
5. **Too few consumers?** Scale out subscribers, raise Cloud Run max instances for push.
6. **Ordering keys** with one stuck key block all later messages for that key.

Keep in mind that messages older than the retention period (7 days by default) are dropped.

## 416: GKE pods are stuck in Pending or keep getting OOMKilled. How do you troubleshoot?

**Pending**:

- `kubectl describe pod` shows the reason: `Insufficient cpu/memory`, node selector or affinity mismatch, taints, PVC not bound, or quota exceeded.
- Check if the cluster autoscaler can scale (max nodes reached, regional quota for CPUs, no IPs left in the pod range, or Spot capacity unavailable).
- In Autopilot, check that requests and compute class are valid.

**OOMKilled**:

- The container used more memory than its limit. Check `kubectl describe pod` for `Last State: Terminated, Reason: OOMKilled`, and memory usage metrics.
- Raise the memory limit, fix leaks, or tune the runtime (for Node.js, `--max-old-space-size` lower than the container limit).
- Make sure requests are realistic so pods are not placed on nodes without enough memory.

## 417: Cloud SQL CPU is at 100% after a release. What do you do?

1. **Mitigate**: if the release clearly caused it, roll back the app. If the database is unhealthy, consider scaling up the machine temporarily (this restarts the instance, short downtime).
2. **Find the queries**: Query Insights shows top queries by load. Look for new queries or changed query plans. `pg_stat_statements` gives the same in PostgreSQL.
3. **Common causes**: a missing index for a new query, an N+1 pattern from an ORM, a query in a loop, a full table scan from a removed `WHERE`, too many connections, or a lock storm from a migration.
4. **Fix**: add the index (`CREATE INDEX CONCURRENTLY` in PostgreSQL), fix the code, add caching or move reads to replicas.
5. **Prevent**: run `EXPLAIN` on new queries in code review, load test before releases, and alert on database CPU and query latency.

## 418: Your Google Cloud bill doubled overnight. How do you find out why?

1. **Billing reports** in the console: group by project, then service, then SKU, and compare days to see what changed.
2. **Billing export in BigQuery**: drill down to resource names and labels with SQL.
3. **Common causes**: an autoscaling loop (service calling itself, function triggering itself on the same bucket), a forgotten load test, BigQuery queries scanning full tables (often from a dashboard refresh), logging volume spike, network egress from a misconfigured CDN or a public bucket being hotlinked, a compromised account running crypto miners (check for new VMs and GPUs in unusual regions).
4. **Stop the bleeding**: scale down or disable the cause, set max instances, quotas or BigQuery custom quotas.
5. **Prevent**: budgets with alerts per project, anomaly detection on cost, and limits on BigQuery bytes billed.

## 419: How do you prepare Google Cloud for a big launch or traffic event?

- **Capacity and quotas**: estimate peak load, then check and request increases for quotas (Cloud Run instances, CPUs per region, API rate limits, Cloud SQL connections) weeks in advance.
- **Reservations**: reserve Compute Engine or GPU capacity if you need specific machine types.
- **Load test** the full stack to 1.5-2x expected peak.
- **Pre-scale**: set min instances, increase database size, warm caches.
- **Freeze**: GKE maintenance exclusions, Cloud SQL deny maintenance periods, a code freeze.
- **Protection**: Cloud Armor rate limits and bot rules, CDN caching for static and cacheable API responses.
- **Runbooks and on-call** ready, with dashboards for the launch.
- Optionally use Google Cloud **Event Management** support for large events.

## 420: How do you load test an app running on Google Cloud?

- Use tools like **k6**, **Locust** or **JMeter**, running on Cloud Run jobs, GKE or Compute Engine so you can generate enough load (and are close to the region if you want to measure the service, not the internet).
- Test against a **staging environment** that matches production size, or production in a careful, announced window.
- Ramp up gradually, and watch Cloud Monitoring: latency percentiles, errors, instance counts, database CPU, connection counts, Pub/Sub backlogs.
- Check **quotas** before testing, and make sure Cloud Armor will not block your load generators.
- Tell your team (and if needed Google support for very large tests) so alerts are not mistaken for an attack.
- Watch costs: autoscaling under a load test is real spend.

## 421: How do you design an app to survive a zone outage?

- Use **regional** services wherever possible: Cloud Run, regional GKE clusters, regional MIGs, Cloud SQL HA, regional persistent disks, Memorystore with replicas, Firestore and Cloud Storage.
- Spread replicas across zones with **topology spread constraints** or pod anti-affinity in GKE.
- Keep **enough spare capacity** so the remaining zones can handle full traffic (N+1 thinking: with 3 zones, each zone should handle 50% of traffic).
- Avoid zonal dependencies hidden in the design: a single VM running a cron job, a zonal file server, a zonal internal load balancer backend.
- Test it: drain a zone in staging (for example cordon GKE nodes in one zone) and see what breaks.

## 422: How do you prevent retry storms between services?

When a dependency is slow, every caller retries, which multiplies load and makes the outage worse.

Protections:

- **Exponential backoff with jitter** on all retries.
- **Retry budgets**: limit retries to a small percentage of total requests.
- Retry only at **one layer** of the call stack, not at every layer.
- **Timeouts** shorter than the caller's own timeout, so work is not wasted.
- **Circuit breakers**: stop calling a failing dependency for a while (in code, or with Cloud Service Mesh outlier detection).
- **Load shedding**: return 503 quickly when overloaded.
- **Queues** between services (Pub/Sub, Cloud Tasks with rate limits) for work that does not need a synchronous answer.

## 423: How do you reduce API latency for users around the world?

- **Global external Application Load Balancer** with Premium Tier: TLS ends at the nearest edge, and traffic uses Google's backbone.
- **Cloud CDN** for cacheable responses, including API responses with proper `Cache-Control` and cache keys.
- **Multi-region backends** (Cloud Run in several regions) so compute is close to users.
- **Data close to users**: Firestore or Spanner multi-region configurations, read replicas in other regions, or region-specific data partitioning.
- **Fewer round trips**: batch API calls, use HTTP/2 or HTTP/3, compress responses.
- **Edge logic**: redirects and header changes in the load balancer instead of in the app.

## 424: What are your options for data consistency across regions?

- **Strong consistency everywhere**: Spanner multi-region or Firestore multi-region. Writes are slower (they need a quorum across regions), but reads see the latest data.
- **Single primary**: one write region (Cloud SQL primary) with read replicas elsewhere. Simple, but reads in other regions can be stale, and writes from far away are slow.
- **Partitioned by region**: each user's data lives in their home region. Good for residency and latency, but cross-region queries are harder.
- **Eventual consistency**: replicate with events (Pub/Sub, Datastream) and accept short delays.

The right choice depends on the business: a bank balance needs strong consistency, a product catalog can be eventually consistent.

## 425: What FinOps practices would you set up for a Google Cloud organization?

- **Visibility**: billing export to BigQuery, Looker Studio dashboards per team, mandatory labels, GKE cost allocation.
- **Accountability**: each project has an owning team and a budget with alerts to that team.
- **Optimization**: monthly review of Recommender findings (idle resources, rightsizing), storage lifecycle policies, log volume, BigQuery query costs.
- **Rate optimization**: committed use discounts for the stable baseline, reviewed quarterly.
- **Guardrails**: quotas, BigQuery custom quotas, max instances, org policies against expensive regions or machine types where needed.
- **Unit economics**: track cost per order, per user or per request, not just total spend.

## 426: How do you decide how much to commit with CUDs?

1. Look at at least 3-6 months of usage from billing export or the CUD recommender.
2. Find the **steady baseline**: the usage level that is almost always present, for example the minimum hourly usage over the period.
3. Commit to that baseline, not to peaks. Unused commitment is still paid for.
4. Prefer **flexible (spend-based) CUDs** if machine types or services may change, and **resource-based** CUDs for very stable fleets.
5. Stagger commitments (buy some each quarter) so they do not all expire at once and you can adjust as usage changes.
6. Check the CUD analysis report regularly for utilization.

## 427: How do you choose a Google Cloud region for an app?

Consider:

- **Latency**: close to most users and to other systems the app talks to.
- **Data residency and compliance**: legal requirements for where data is stored.
- **Service availability**: not every service, machine type or GPU is in every region.
- **Price**: prices differ between regions. Some US regions are cheaper than Europe or Asia.
- **Carbon**: some regions have a higher share of carbon-free energy (marked "Low CO2" in the console).
- **DR pairing**: a second region far enough away for disaster recovery but close enough for replication latency.
- **Capacity**: popular regions can be short of some resources like GPUs.

## 428: How does Google Cloud help with sustainability?

- Google publishes the **carbon-free energy percentage** (CFE%) per region and marks low-carbon regions in the console.
- **Carbon Footprint** reports show the emissions of your usage per project, service and region, and can be exported to BigQuery.
- The **Active Assist** recommender includes sustainability impact, for example from removing idle VMs.

To reduce footprint: choose low-carbon regions when latency and compliance allow, remove idle resources, rightsize, use serverless that scales to zero, and run batch jobs in low-carbon regions or times.

## 429: How would you build a RAG (retrieval-augmented generation) app on Google Cloud?

1. **Ingest**: documents in Cloud Storage. A Cloud Run job or Eventarc-triggered service splits them into chunks.
2. **Embed**: create embeddings with an embedding model on Agent Platform (formerly Vertex AI).
3. **Store vectors**: AlloyDB or Cloud SQL for PostgreSQL with `pgvector` (good when you already use PostgreSQL), BigQuery vector search for analytics-scale data, Firestore vector search, or Agent Platform Vector Search for very large, low-latency workloads.
4. **Query**: on a user question, embed it, find similar chunks, and send them with the question to a Gemini model.
5. **Serve**: a Cloud Run API with streaming responses.
6. **Guardrails**: access control on which documents a user may retrieve, Model Armor for prompt injection and sensitive data, logging and evaluation of answers.

Managed options like **Agent Platform RAG Engine** or Google's managed enterprise search products can replace much of the custom pipeline.

## 430: How do you secure a generative AI application on Google Cloud?

- **IAM**: the app's service account gets only `aiplatform.user` (or narrower), no broad roles.
- **Data protection**: VPC Service Controls around the AI APIs and data, CMEK where needed, data residency with regional endpoints.
- **Prompt and response screening**: **Model Armor** checks for prompt injection, jailbreaks, sensitive data and harmful content, and can be applied to model calls.
- **Retrieval security**: filter retrieved documents by the user's permissions before they reach the model.
- **Tool use**: agents calling tools should use least-privilege identities and require confirmation for risky actions.
- **Sensitive Data Protection** to mask PII in prompts and logs.
- **Monitoring**: log prompts and outputs carefully (respecting privacy), track costs and abuse, and set quotas per user.

## 431: How do you choose where to serve an ML model on Google Cloud?

- **Agent Platform managed endpoints** (formerly Vertex AI Prediction): managed autoscaling, model monitoring, A/B traffic splitting. Easiest for models trained on the platform or from Model Garden.
- **Gemini and partner models through API**: no serving at all, pay per token. Best when a hosted model is good enough.
- **Cloud Run with GPUs**: your own container (vLLM, Ollama, TGI) with scale to zero. Good for open models with spiky traffic.
- **GKE with GPUs or TPUs**: most control and best cost at high steady load, with features like GKE Inference Gateway for model-aware load balancing.

The choice depends on traffic pattern, latency needs, model size and how much operations work the team can take on.

## 432: What can you do with AI and ML directly in BigQuery?

- **BigQuery ML**: train and run models with SQL (linear and logistic regression, k-means, time series with ARIMA_PLUS, boosted trees, matrix factorization).
- **Remote models**: call Gemini and other Agent Platform models from SQL with `ML.GENERATE_TEXT` or AI functions, for example to classify or summarize text in a table.
- **Embeddings and vector search**: `ML.GENERATE_EMBEDDING` and the `VECTOR_SEARCH` function with vector indexes.
- **Forecasting**: `AI.FORECAST` with the TimesFM model.

```sql
SELECT *
FROM ML.FORECAST(MODEL shop.sales_forecast, STRUCT(30 AS horizon));
```

It keeps data in place, which avoids moving data to another system and keeps governance simple.

## 433: How do you choose between Cloud Run jobs, Batch and Dataflow for batch processing?

- **Cloud Run jobs**: containerized tasks, up to thousands of tasks per execution, simple to set up, good for app-level batch work (sending reports, resizing images, data exports). Task runtime is limited (hours, not days).
- **Batch**: runs jobs on Compute Engine VMs with full control: large machines, GPUs, Spot VMs, MPI, long runtimes. Good for HPC, scientific and rendering workloads.
- **Dataflow**: data-parallel pipelines with Apache Beam. Good for transforming large datasets with joins, aggregations and many sources and sinks.

Also consider BigQuery SQL for data that is already in BigQuery. It often beats all three for simplicity.

## 434: How do you orchestrate dependent jobs and services?

- **Workflows**: lightweight, serverless orchestration of APIs, Cloud Run jobs and services, with retries, conditions and callbacks. Good for app processes and simple pipelines.
- **Cloud Composer (Airflow)**: data pipelines with many tasks, dependencies, backfills, and Airflow's large operator library.
- **Cloud Scheduler**: only time-based triggers. Combine with Workflows for dependencies.
- **Eventarc + Pub/Sub**: event-driven choreography without a central orchestrator.

Rule of thumb: Workflows for service orchestration and simple pipelines, Composer for complex data engineering DAGs.

## 435: How would you design a system that receives webhooks at high volume?

- **Ingress**: a small Cloud Run service behind a load balancer with Cloud Armor. It only verifies the signature (HMAC from the provider), does basic validation, and publishes the payload to **Pub/Sub**, then returns 200 quickly.
- **Durability**: once in Pub/Sub, the webhook is safe even if downstream systems are down.
- **Processing**: subscribers (Cloud Run with push, or workers) process events with idempotency by the provider's event ID.
- **Ordering**: use ordering keys per resource if the provider sends events that must be applied in order, or use version numbers.
- **Failures**: retry policy and dead-letter topic, with a replay tool.
- **Monitoring**: alerts on signature failures (possible attack or key rotation), backlog age and dead-letter count.

## 436: How would you build a real-time chat or live-update feature on Google Cloud?

Options:

- **Firestore real-time listeners**: clients subscribe directly to documents or queries. Easiest, scales automatically, works offline. Security Rules control who sees what. Cost is per document read.
- **Firebase Realtime Database**: lower latency for very frequent small updates, like presence.
- **Custom WebSocket service** on Cloud Run or GKE: instances connected through **Memorystore pub/sub** or **Pub/Sub** to broadcast messages to users connected to other instances. More control but you manage connection limits, timeouts and reconnects.

For most apps, Firestore listeners are the fastest path. For high-frequency data (multiplayer games, collaborative editing at scale), a custom service on GKE is common.

## 437: How do you design a file processing pipeline that is easy to operate?

```text
Upload bucket ──(finalize event)──▶ Pub/Sub topic ──▶ Cloud Run worker ──▶ Output bucket
                                          │                   │
                                          ▼                   ▼
                                  Dead-letter topic     Firestore (job status)
```

Design points:

- Events go to Pub/Sub, which gives buffering, retries and a dead-letter topic.
- Workers are idempotent: processing the same file twice gives the same result (output name based on input name + generation).
- Output goes to a different bucket so processing does not trigger itself.
- Status per file is stored for the UI and support.
- Max instances on workers protect downstream systems.
- Metrics: files processed, failures, processing time and backlog age.
- A replay tool: re-publish events for a prefix or time range.

## 438: When should tenants or teams get separate projects instead of sharing one?

Separate projects when you need:

- **Strong isolation**: IAM, quotas and API limits are per project, so one tenant cannot hit another's limits or see their resources.
- **Clear cost tracking** per tenant or team.
- **Different compliance requirements** (CMEK keys, regions, VPC Service Controls perimeters).
- **Independent lifecycle**: delete a tenant by deleting a project.

Shared project when:

- You have many small tenants (thousands), where project limits and management overhead are too high.
- Resources are naturally shared (one Cloud Run service, one database with tenant IDs).

Many SaaS companies mix both: pooled projects for small tenants and dedicated projects for large enterprise customers.

## 439: How do you do a blue-green deployment of a whole stack, not just one service?

1. Deploy the **green** stack next to blue: new revisions of all services (Cloud Run tags with `--no-traffic`, or a separate GKE namespace or cluster), using the same or a compatible database schema.
2. **Test green** using tagged URLs or a separate hostname.
3. **Switch traffic** at one point: load balancer URL map or weighted backend services, Gateway API `HTTPRoute` weights, or Cloud Run traffic split for each service.
4. **Watch** SLOs and errors. Roll back by switching back.
5. **Retire blue** after a safe period.

The hard part is the database. Use backward-compatible schema changes (expand and contract), so blue and green can both run against the same database during the switch.

## 440: How do you run database schema migrations in a CI/CD pipeline on Google Cloud?

- Package migrations with the app (Prisma, Flyway, Liquibase, Knex) and run them as a separate step: a **Cloud Run job** that connects with IAM auth, or a Cloud Build step through a private pool.
- Run migrations **before** deploying new code, and make them **backward compatible** with the currently running version.
- For destructive changes, use **expand and contract**: add the new column, deploy code that writes both, backfill, switch reads, then remove the old column in a later release.
- Take an **on-demand backup** or rely on PITR before risky migrations.
- Use lock timeouts so a migration does not block production queries for a long time.
- Make Cloud Deploy run the migration job as a **predeploy hook** so migrations and deploys happen in the right order per environment.

## 441: How do you manage application configuration and feature flags across many services?

- **Static config** per environment: environment variables set by Terraform or Cloud Deploy, with values stored in Git.
- **Secrets**: Secret Manager, with the same names in each environment project.
- **Dynamic config and flags**: **Firebase Remote Config** (now usable on servers too) or a third-party flag service, so you can change behavior without a deploy, do gradual rollouts and kill switches.
- **Shared config across services**: a config file in Cloud Storage or Firestore that services read and cache, if you need something simple.

Keep flags short-lived and clean them up, or the codebase fills with dead branches.

## 442: How do you test infrastructure code for Google Cloud?

- **Static checks**: `terraform fmt`, `terraform validate`, `tflint` with the Google ruleset, and security scanners like Checkov or Trivy.
- **Policy checks**: `gcloud beta terraform vet` or OPA on the plan output.
- **Unit-style tests**: `terraform test` with mocked providers for module logic.
- **Integration tests**: `terraform test` or Terratest that apply modules in a disposable test project, check the real resources (for example call the Cloud Run URL), then destroy them.
- **Ephemeral environments** per pull request for bigger changes, created by a project factory and cleaned up automatically.

## 443: At what point does GKE become cheaper than Cloud Run?

There is no fixed number, but the trade-off is:

- **Cloud Run** costs more per unit of CPU and memory, but bills only for what you use (with request-based billing) and has almost no operations cost. It wins for spiky traffic, many small services and services that are idle often.
- **GKE** (especially Standard with good bin-packing, CUDs and Spot) has a lower price per unit, but you pay for idle capacity and for the people who run it. It wins for large, steady, high-utilization workloads.

Cloud Run with instance-based billing and committed use discounts narrows the gap. Do the math with real utilization, and include team time. Many companies run most services on Cloud Run and only the heavy, steady ones on GKE.

## 444: How do you use error budgets to decide on releases?

An error budget is `1 - SLO`. For a 99.9% availability SLO over 28 days, the budget is about 40 minutes of failure.

- If plenty of budget is left, teams can ship faster and take more risk (bigger changes, experiments).
- If the budget is nearly used up, the policy says to slow down: freeze risky releases and focus on reliability work until the budget recovers.

Cloud Monitoring SLOs show remaining budget and burn rate. You can automate checks: Cloud Deploy can require approval or block promotions when the SLO burn rate is high, and canary analysis can compare the new revision's error rate to the old one.

## 445: What is a sound backup strategy across Google Cloud services?

- **Cloud SQL / AlloyDB**: automated backups + PITR, backups in a second region, and periodic exports to Cloud Storage for long-term retention.
- **Firestore**: scheduled backups and PITR (up to 7 days), managed exports to Cloud Storage for long retention.
- **Spanner**: backups and PITR, copied to another region.
- **Cloud Storage**: object versioning, soft delete, and copies to a bucket in another region or project.
- **Compute Engine and GKE**: snapshot schedules, Backup for GKE for workloads and volumes.
- **Central management**: **Backup and DR Service** with backup vaults for supported services.

Keep backups in a **separate project** with restricted access, so a compromised app project cannot delete them, and **test restores** regularly.

## 446: How do you protect backups against ransomware or a malicious admin?

- **Backup vaults** in Backup and DR Service with **enforced retention**: backups cannot be deleted before the retention period ends, even by admins.
- **Bucket Lock** or Object Retention Lock on Cloud Storage backup buckets.
- Keep backups in a **separate project or organization** with different admins (separation of duties).
- Use **deny policies** to block deletion permissions on backup resources for everyone except a break-glass group.
- **Monitor** for mass deletes and changes to retention settings with audit log alerts.
- Test restores to make sure backups are complete and usable.

## 447: How do you handle data deletion requests (like GDPR) in a Google Cloud system?

- **Know where data is**: Sensitive Data Protection discovery and a data catalog (Dataplex) to map where personal data lives: Cloud SQL, Firestore, BigQuery, Cloud Storage, logs, backups.
- **Design for deletion**: key personal data by user ID, avoid copying PII to many places, and pseudonymize analytics data.
- **Deletion workflow**: a Workflows or Pub/Sub-driven process that deletes or anonymizes the user's data in each system and records completion.
- **BigQuery**: `DELETE` with partition filters, or keep PII in a separate table that is easy to purge.
- **Logs and backups**: short retention for logs containing PII, and document how deleted data ages out of backups.
- **Crypto-shredding**: encrypt each user's data with a per-user key and delete the key to make the data unreadable everywhere.

## 448: How do you keep a large Google Cloud organization clean over time?

- **Project lifecycle**: every project has an owner label and an expiry for sandboxes. Unattended project recommendations flag unused projects.
- **Recommender** reviews: idle VMs, disks, IPs, over-privileged IAM.
- **Asset Inventory** exports to BigQuery for regular reports: public resources, external IPs, old service account keys, resources without labels.
- **Automation**: delete sandbox resources on a schedule, budgets with automatic actions for sandboxes.
- **Policy**: org policies prevent the worst misconfigurations so cleanup does not keep growing.
- **Ownership reviews**: quarterly checks that groups, folders and billing accounts still match the company structure.

## 449: What are common anti-patterns on Google Cloud?

- Using the **default service account** with Editor for everything.
- **Service account keys** in code, CI variables or laptops.
- Everything in **one project** for all environments.
- **Auto mode VPC** in production, with overlapping ranges later.
- **Public buckets or databases** "temporarily".
- Cloud Run services that do **background work with request-based billing**.
- **No max instances**, so a spike overloads the database.
- `SELECT *` in BigQuery dashboards over unpartitioned tables.
- **No budgets or alerts**, so cost surprises arrive with the invoice.
- **ClickOps** in production with no infrastructure as code.
- Treating a **cache or Pub/Sub** as the source of truth.

## 450: Design an e-commerce backend on Google Cloud.

**Frontend and edge**: Next.js on Firebase App Hosting or Cloud Run, global external Application Load Balancer with Cloud CDN for product images and pages, Cloud Armor with WAF rules, rate limiting on login and checkout, and bot protection.

**Services** (Cloud Run, each with its own service account):

- **Catalog**: reads from Cloud SQL or AlloyDB, cached in Memorystore. Search with a Google managed search product or a search engine like Elasticsearch on GKE.
- **Cart**: Firestore or Memorystore, keyed by user or session.
- **Orders**: Cloud SQL (Enterprise Plus, HA, cross-region replica) as the source of truth, with the transactional outbox pattern to publish `order.created` to Pub/Sub.
- **Payments**: calls the payment provider with idempotency keys. Webhooks come in through a small ingress service into Pub/Sub.
- **Inventory**: reserves stock in a transaction. Checkout is a saga in Workflows with compensations.
- **Notifications**: Pub/Sub subscriber sending emails through Cloud Tasks with rate limits.

**Data and analytics**: Datastream from Cloud SQL to BigQuery, Pub/Sub BigQuery subscription for clickstream events, BigQuery ML for recommendations and forecasting.

**Identity**: Identity Platform for customers, IAP for the admin panel.

**Operations**: Terraform, Cloud Build and Cloud Deploy with canary releases, SLOs on checkout success and latency, backups in a separate project, and load tests before sales events.
