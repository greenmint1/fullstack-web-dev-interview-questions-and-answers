# Microsoft Azure Interview Questions and Answers

_Last updated: October 29, 2026_

450 Microsoft Azure interview questions with answers, split into three levels: 150 easy, 150 moderate and 150 advanced.

The answers reflect Azure as of late 2026: Microsoft Entra ID (formerly Azure AD), Bicep, the Azure Developer CLI, Azure Functions with the Flex Consumption plan and the Node.js v4 programming model, Azure Container Apps, AKS and Microsoft Foundry (formerly Azure AI Foundry). Code examples use the Azure CLI, Bicep and the current Azure SDK for JavaScript (`@azure/identity`, `@azure/storage-blob` and so on). Older services and names are mentioned where you will still meet them in real projects.

## Table of Contents

- [Easy Questions (1-150)](#easy-questions-1-150)
- [Moderate Questions (151-300)](#moderate-questions-151-300)
- [Advanced Questions (301-450)](#advanced-questions-301-450)

### Easy Questions (1-150)

- [1: What is Microsoft Azure?](#1-what-is-microsoft-azure)
- [2: What are IaaS, PaaS and SaaS? Give an Azure example of each.](#2-what-are-iaas-paas-and-saas-give-an-azure-example-of-each)
- [3: What is the shared responsibility model?](#3-what-is-the-shared-responsibility-model)
- [4: What is an Azure region?](#4-what-is-an-azure-region)
- [5: What are availability zones?](#5-what-are-availability-zones)
- [6: What are region pairs?](#6-what-are-region-pairs)
- [7: What is an Azure geography?](#7-what-is-an-azure-geography)
- [8: What is the hierarchy of Azure resources from top to bottom?](#8-what-is-the-hierarchy-of-azure-resources-from-top-to-bottom)
- [9: What is an Azure subscription?](#9-what-is-an-azure-subscription)
- [10: What is a resource group?](#10-what-is-a-resource-group)
- [11: Can resources in one resource group be in different regions?](#11-can-resources-in-one-resource-group-be-in-different-regions)
- [12: What is a management group?](#12-what-is-a-management-group)
- [13: What is Azure Resource Manager (ARM)?](#13-what-is-azure-resource-manager-arm)
- [14: What is a resource provider?](#14-what-is-a-resource-provider)
- [15: What is the Azure portal?](#15-what-is-the-azure-portal)
- [16: What is the Azure CLI?](#16-what-is-the-azure-cli)
- [17: What is Azure PowerShell?](#17-what-is-azure-powershell)
- [18: What is Azure Cloud Shell?](#18-what-is-azure-cloud-shell)
- [19: What is Microsoft Entra ID?](#19-what-is-microsoft-entra-id)
- [20: What is a tenant?](#20-what-is-a-tenant)
- [21: Is Entra ID the same as on-premises Active Directory?](#21-is-entra-id-the-same-as-on-premises-active-directory)
- [22: What is Azure role-based access control (RBAC)?](#22-what-is-azure-role-based-access-control-rbac)
- [23: What are the most common built-in Azure roles?](#23-what-are-the-most-common-built-in-azure-roles)
- [24: What is the difference between Azure RBAC roles and Entra ID roles?](#24-what-is-the-difference-between-azure-rbac-roles-and-entra-id-roles)
- [25: What is a service principal?](#25-what-is-a-service-principal)
- [26: What is a managed identity?](#26-what-is-a-managed-identity)
- [27: What are the two types of managed identities?](#27-what-are-the-two-types-of-managed-identities)
- [28: What is an Azure Virtual Machine?](#28-what-is-an-azure-virtual-machine)
- [29: How are Azure VM sizes named?](#29-how-are-azure-vm-sizes-named)
- [30: What disks does an Azure VM have?](#30-what-disks-does-an-azure-vm-have)
- [31: What are the managed disk types?](#31-what-are-the-managed-disk-types)
- [32: What is the difference between stopping and deallocating a VM?](#32-what-is-the-difference-between-stopping-and-deallocating-a-vm)
- [33: What is an availability set?](#33-what-is-an-availability-set)
- [34: What is a Virtual Machine Scale Set?](#34-what-is-a-virtual-machine-scale-set)
- [35: What is Azure App Service?](#35-what-is-azure-app-service)
- [36: What is an App Service plan?](#36-what-is-an-app-service-plan)
- [37: What is the difference between scaling up and scaling out?](#37-what-is-the-difference-between-scaling-up-and-scaling-out)
- [38: What is Azure Functions?](#38-what-is-azure-functions)
- [39: What are triggers and bindings in Azure Functions?](#39-what-are-triggers-and-bindings-in-azure-functions)
- [40: What does a basic HTTP-triggered function look like in Node.js?](#40-what-does-a-basic-http-triggered-function-look-like-in-nodejs)
- [41: What are the Azure Functions hosting plans?](#41-what-are-the-azure-functions-hosting-plans)
- [42: What is a cold start?](#42-what-is-a-cold-start)
- [43: What is a timer trigger?](#43-what-is-a-timer-trigger)
- [44: What is Azure Container Instances (ACI)?](#44-what-is-azure-container-instances-aci)
- [45: What is Azure Container Apps?](#45-what-is-azure-container-apps)
- [46: What is Azure Kubernetes Service (AKS)?](#46-what-is-azure-kubernetes-service-aks)
- [47: What is Azure Container Registry (ACR)?](#47-what-is-azure-container-registry-acr)
- [48: What is an Azure Storage account?](#48-what-is-an-azure-storage-account)
- [49: What is Azure Blob Storage?](#49-what-is-azure-blob-storage)
- [50: What are the blob access tiers?](#50-what-are-the-blob-access-tiers)
- [51: What redundancy options does Azure Storage offer?](#51-what-redundancy-options-does-azure-storage-offer)
- [52: What is Azure Queue Storage?](#52-what-is-azure-queue-storage)
- [53: What is Azure Table Storage?](#53-what-is-azure-table-storage)
- [54: What is Azure Files?](#54-what-is-azure-files)
- [55: What is Azure Data Lake Storage Gen2?](#55-what-is-azure-data-lake-storage-gen2)
- [56: What is Azure SQL Database?](#56-what-is-azure-sql-database)
- [57: What are the Azure SQL deployment options?](#57-what-are-the-azure-sql-deployment-options)
- [58: What is Azure Cosmos DB?](#58-what-is-azure-cosmos-db)
- [59: What is a request unit (RU) in Cosmos DB?](#59-what-is-a-request-unit-ru-in-cosmos-db)
- [60: What managed open-source databases does Azure offer?](#60-what-managed-open-source-databases-does-azure-offer)
- [61: What is Azure Cache for Redis?](#61-what-is-azure-cache-for-redis)
- [62: What is an Azure Virtual Network (VNet)?](#62-what-is-an-azure-virtual-network-vnet)
- [63: What is a subnet?](#63-what-is-a-subnet)
- [64: What is a Network Security Group (NSG)?](#64-what-is-a-network-security-group-nsg)
- [65: What is a public IP address in Azure?](#65-what-is-a-public-ip-address-in-azure)
- [66: What is Azure DNS?](#66-what-is-azure-dns)
- [67: What is Azure Load Balancer?](#67-what-is-azure-load-balancer)
- [68: What is Azure Application Gateway?](#68-what-is-azure-application-gateway)
- [69: What is Azure Front Door?](#69-what-is-azure-front-door)
- [70: What is Azure Traffic Manager?](#70-what-is-azure-traffic-manager)
- [71: What is the difference between Load Balancer, Application Gateway, Front Door and Traffic Manager?](#71-what-is-the-difference-between-load-balancer-application-gateway-front-door-and-traffic-manager)
- [72: What is VNet peering?](#72-what-is-vnet-peering)
- [73: What is a VPN Gateway?](#73-what-is-a-vpn-gateway)
- [74: What is ExpressRoute?](#74-what-is-expressroute)
- [75: What is Azure Bastion?](#75-what-is-azure-bastion)
- [76: What is Azure Key Vault?](#76-what-is-azure-key-vault)
- [77: How do you read a secret from Key Vault in Node.js?](#77-how-do-you-read-a-secret-from-key-vault-in-nodejs)
- [78: What is Azure Monitor?](#78-what-is-azure-monitor)
- [79: What is the difference between metrics and logs in Azure Monitor?](#79-what-is-the-difference-between-metrics-and-logs-in-azure-monitor)
- [80: What is Application Insights?](#80-what-is-application-insights)
- [81: What is a Log Analytics workspace?](#81-what-is-a-log-analytics-workspace)
- [82: What is KQL?](#82-what-is-kql)
- [83: What are Azure Monitor alerts?](#83-what-are-azure-monitor-alerts)
- [84: What is Azure Service Bus?](#84-what-is-azure-service-bus)
- [85: What is Azure Event Grid?](#85-what-is-azure-event-grid)
- [86: What is Azure Event Hubs?](#86-what-is-azure-event-hubs)
- [87: When do you use Service Bus, Event Grid or Event Hubs?](#87-when-do-you-use-service-bus-event-grid-or-event-hubs)
- [88: What is Azure Logic Apps?](#88-what-is-azure-logic-apps)
- [89: What is Azure API Management (APIM)?](#89-what-is-azure-api-management-apim)
- [90: What is Azure Static Web Apps?](#90-what-is-azure-static-web-apps)
- [91: What is an ARM template?](#91-what-is-an-arm-template)
- [92: What is Bicep?](#92-what-is-bicep)
- [93: How do you deploy a Bicep file?](#93-how-do-you-deploy-a-bicep-file)
- [94: What is infrastructure as code (IaC) and why use it?](#94-what-is-infrastructure-as-code-iac-and-why-use-it)
- [95: What are tags in Azure?](#95-what-are-tags-in-azure)
- [96: What are resource locks?](#96-what-are-resource-locks)
- [97: What is Azure Policy?](#97-what-is-azure-policy)
- [98: What is the difference between Azure Policy and RBAC?](#98-what-is-the-difference-between-azure-policy-and-rbac)
- [99: What is the Azure pricing calculator?](#99-what-is-the-azure-pricing-calculator)
- [100: What is Microsoft Cost Management?](#100-what-is-microsoft-cost-management)
- [101: What is an Azure budget?](#101-what-is-an-azure-budget)
- [102: What are Azure Reservations?](#102-what-are-azure-reservations)
- [103: What is an Azure savings plan for compute?](#103-what-is-an-azure-savings-plan-for-compute)
- [104: What are Spot VMs?](#104-what-are-spot-vms)
- [105: What is Azure Advisor?](#105-what-is-azure-advisor)
- [106: What is Azure Service Health?](#106-what-is-azure-service-health)
- [107: What is an SLA in Azure?](#107-what-is-an-sla-in-azure)
- [108: How do you calculate the composite SLA of an app that uses several services?](#108-how-do-you-calculate-the-composite-sla-of-an-app-that-uses-several-services)
- [109: What is Azure Marketplace?](#109-what-is-azure-marketplace)
- [110: What is Azure DevOps?](#110-what-is-azure-devops)
- [111: How do you deploy to Azure from GitHub Actions?](#111-how-do-you-deploy-to-azure-from-github-actions)
- [112: What is the Azure Developer CLI (azd)?](#112-what-is-the-azure-developer-cli-azd)
- [113: What is Microsoft Foundry?](#113-what-is-microsoft-foundry)
- [114: What is Azure OpenAI?](#114-what-is-azure-openai)
- [115: What are Azure AI services?](#115-what-are-azure-ai-services)
- [116: What is Azure AI Search?](#116-what-is-azure-ai-search)
- [117: What is Microsoft Defender for Cloud?](#117-what-is-microsoft-defender-for-cloud)
- [118: What is Microsoft Sentinel?](#118-what-is-microsoft-sentinel)
- [119: What is Azure Arc?](#119-what-is-azure-arc)
- [120: What is Azure Backup?](#120-what-is-azure-backup)
- [121: What is Azure Site Recovery?](#121-what-is-azure-site-recovery)
- [122: What is Azure Migrate?](#122-what-is-azure-migrate)
- [123: What is multi-factor authentication in Entra ID?](#123-what-is-multi-factor-authentication-in-entra-id)
- [124: What is Conditional Access?](#124-what-is-conditional-access)
- [125: What is Microsoft Entra External ID?](#125-what-is-microsoft-entra-external-id)
- [126: What is an app registration?](#126-what-is-an-app-registration)
- [127: What is a shared access signature (SAS)?](#127-what-is-a-shared-access-signature-sas)
- [128: What are storage account access keys and why should you avoid them?](#128-what-are-storage-account-access-keys-and-why-should-you-avoid-them)
- [129: What are deployment slots in App Service?](#129-what-are-deployment-slots-in-app-service)
- [130: What are app settings in App Service?](#130-what-are-app-settings-in-app-service)
- [131: How do you add a custom domain and TLS to an App Service app?](#131-how-do-you-add-a-custom-domain-and-tls-to-an-app-service-app)
- [132: What is autoscale in Azure?](#132-what-is-autoscale-in-azure)
- [133: What is Durable Functions?](#133-what-is-durable-functions)
- [134: What is Azure SignalR Service?](#134-what-is-azure-signalr-service)
- [135: What is Azure Notification Hubs?](#135-what-is-azure-notification-hubs)
- [136: What is Azure Communication Services?](#136-what-is-azure-communication-services)
- [137: What is Azure Data Factory?](#137-what-is-azure-data-factory)
- [138: What is Microsoft Fabric?](#138-what-is-microsoft-fabric)
- [139: What is Azure Databricks?](#139-what-is-azure-databricks)
- [140: What is Azure Batch?](#140-what-is-azure-batch)
- [141: What is Azure Service Fabric?](#141-what-is-azure-service-fabric)
- [142: What is Azure Virtual Desktop?](#142-what-is-azure-virtual-desktop)
- [143: What are Azure quotas and limits?](#143-what-are-azure-quotas-and-limits)
- [144: What is the Azure activity log?](#144-what-is-the-azure-activity-log)
- [145: What are diagnostic settings?](#145-what-are-diagnostic-settings)
- [146: How do you log in to the Azure CLI in different situations?](#146-how-do-you-log-in-to-the-azure-cli-in-different-situations)
- [147: What output formats does the Azure CLI support?](#147-what-output-formats-does-the-azure-cli-support)
- [148: What is a resource ID?](#148-what-is-a-resource-id)
- [149: What is Azure App Configuration?](#149-what-is-azure-app-configuration)
- [150: What is the Microsoft Cloud Adoption Framework?](#150-what-is-the-microsoft-cloud-adoption-framework)

### Moderate Questions (151-300)

- [151: How does DefaultAzureCredential work?](#151-how-does-defaultazurecredential-work)
- [152: Why might you not want DefaultAzureCredential in production?](#152-why-might-you-not-want-defaultazurecredential-in-production)
- [153: When do you choose a user-assigned managed identity over a system-assigned one?](#153-when-do-you-choose-a-user-assigned-managed-identity-over-a-system-assigned-one)
- [154: How do you give an App Service app access to a storage account without keys?](#154-how-do-you-give-an-app-service-app-access-to-a-storage-account-without-keys)
- [155: What is the difference between the control plane and the data plane in Azure?](#155-what-is-the-difference-between-the-control-plane-and-the-data-plane-in-azure)
- [156: What are Key Vault references in App Service and Functions?](#156-what-are-key-vault-references-in-app-service-and-functions)
- [157: What is the difference between Key Vault access policies and Azure RBAC for Key Vault?](#157-what-is-the-difference-between-key-vault-access-policies-and-azure-rbac-for-key-vault)
- [158: What are soft delete and purge protection in Key Vault?](#158-what-are-soft-delete-and-purge-protection-in-key-vault)
- [159: How do deployment slot swaps work in App Service?](#159-how-do-deployment-slot-swaps-work-in-app-service)
- [160: What are slot settings (sticky settings)?](#160-what-are-slot-settings-sticky-settings)
- [161: What is swap with preview?](#161-what-is-swap-with-preview)
- [162: What deployment methods does App Service support?](#162-what-deployment-methods-does-app-service-support)
- [163: What is the benefit of running from a package in App Service?](#163-what-is-the-benefit-of-running-from-a-package-in-app-service)
- [164: How do you see logs from an App Service app?](#164-how-do-you-see-logs-from-an-app-service-app)
- [165: What does the App Service health check feature do?](#165-what-does-the-app-service-health-check-feature-do)
- [166: What does Always On do in App Service?](#166-what-does-always-on-do-in-app-service)
- [167: What is VNet integration for App Service?](#167-what-is-vnet-integration-for-app-service)
- [168: What is the difference between service endpoints and private endpoints?](#168-what-is-the-difference-between-service-endpoints-and-private-endpoints)
- [169: Why do private endpoints need private DNS zones?](#169-why-do-private-endpoints-need-private-dns-zones)
- [170: How are NSG rules evaluated?](#170-how-are-nsg-rules-evaluated)
- [171: What are service tags?](#171-what-are-service-tags)
- [172: What are application security groups (ASGs)?](#172-what-are-application-security-groups-asgs)
- [173: What are user-defined routes (UDRs)?](#173-what-are-user-defined-routes-udrs)
- [174: What is a NAT gateway and why use one?](#174-what-is-a-nat-gateway-and-why-use-one)
- [175: What changed with default outbound access for VMs?](#175-what-changed-with-default-outbound-access-for-vms)
- [176: What is a hub-and-spoke network topology?](#176-what-is-a-hub-and-spoke-network-topology)
- [177: How do you write a Bicep module and use it?](#177-how-do-you-write-a-bicep-module-and-use-it)
- [178: What is a .bicepparam file?](#178-what-is-a-bicepparam-file)
- [179: What does the what-if operation do?](#179-what-does-the-what-if-operation-do)
- [180: What is the difference between incremental and complete deployment modes?](#180-what-is-the-difference-between-incremental-and-complete-deployment-modes)
- [181: What are deployment stacks?](#181-what-are-deployment-stacks)
- [182: How do you use existing resources in Bicep?](#182-how-do-you-use-existing-resources-in-bicep)
- [183: How do you create a role assignment in Bicep?](#183-how-do-you-create-a-role-assignment-in-bicep)
- [184: How does Terraform work with Azure?](#184-how-does-terraform-work-with-azure)
- [185: Bicep or Terraform: how do you choose?](#185-bicep-or-terraform-how-do-you-choose)
- [186: How do you set up OIDC (workload identity federation) for GitHub Actions?](#186-how-do-you-set-up-oidc-workload-identity-federation-for-github-actions)
- [187: How do you build and push images to ACR in CI?](#187-how-do-you-build-and-push-images-to-acr-in-ci)
- [188: How does AKS pull images from ACR?](#188-how-does-aks-pull-images-from-acr)
- [189: What are revisions in Azure Container Apps?](#189-what-are-revisions-in-azure-container-apps)
- [190: How do you split traffic between revisions in Container Apps?](#190-how-do-you-split-traffic-between-revisions-in-container-apps)
- [191: How does scaling work in Azure Container Apps?](#191-how-does-scaling-work-in-azure-container-apps)
- [192: What is the difference between a container app and a Container Apps job?](#192-what-is-the-difference-between-a-container-app-and-a-container-apps-job)
- [193: What is Dapr and how is it used in Container Apps?](#193-what-is-dapr-and-how-is-it-used-in-container-apps)
- [194: What is a Container Apps environment?](#194-what-is-a-container-apps-environment)
- [195: How do output bindings work in Azure Functions with Node.js v4?](#195-how-do-output-bindings-work-in-azure-functions-with-nodejs-v4)
- [196: How does a Service Bus trigger work in Azure Functions?](#196-how-does-a-service-bus-trigger-work-in-azure-functions)
- [197: How do you connect a function trigger to a service with a managed identity instead of a connection string?](#197-how-do-you-connect-a-function-trigger-to-a-service-with-a-managed-identity-instead-of-a-connection-string)
- [198: What is the Flex Consumption plan and how is it different from the old Consumption plan?](#198-what-is-the-flex-consumption-plan-and-how-is-it-different-from-the-old-consumption-plan)
- [199: What is host.json in Azure Functions?](#199-what-is-hostjson-in-azure-functions)
- [200: How do you run Azure Functions locally?](#200-how-do-you-run-azure-functions-locally)
- [201: What are the main Durable Functions patterns?](#201-what-are-the-main-durable-functions-patterns)
- [202: Show a fan-out/fan-in orchestration in Node.js.](#202-show-a-fan-outfan-in-orchestration-in-nodejs)
- [203: What is the difference between Service Bus queues and topics?](#203-what-is-the-difference-between-service-bus-queues-and-topics)
- [204: What are peek-lock and receive-and-delete in Service Bus?](#204-what-are-peek-lock-and-receive-and-delete-in-service-bus)
- [205: What is the dead-letter queue in Service Bus?](#205-what-is-the-dead-letter-queue-in-service-bus)
- [206: How do you send and receive Service Bus messages in Node.js?](#206-how-do-you-send-and-receive-service-bus-messages-in-nodejs)
- [207: What are Service Bus sessions?](#207-what-are-service-bus-sessions)
- [208: What is duplicate detection in Service Bus?](#208-what-is-duplicate-detection-in-service-bus)
- [209: How do you schedule a message in Service Bus?](#209-how-do-you-schedule-a-message-in-service-bus)
- [210: What is the difference between Service Bus Standard and Premium tiers?](#210-what-is-the-difference-between-service-bus-standard-and-premium-tiers)
- [211: How does Event Grid deliver events and handle failures?](#211-how-does-event-grid-deliver-events-and-handle-failures)
- [212: What are Event Grid system topics, custom topics and namespaces?](#212-what-are-event-grid-system-topics-custom-topics-and-namespaces)
- [213: How do you filter Event Grid events?](#213-how-do-you-filter-event-grid-events)
- [214: What is the CloudEvents schema and why use it?](#214-what-is-the-cloudevents-schema-and-why-use-it)
- [215: What are partitions and consumer groups in Event Hubs?](#215-what-are-partitions-and-consumer-groups-in-event-hubs)
- [216: What is checkpointing in Event Hubs?](#216-what-is-checkpointing-in-event-hubs)
- [217: Can you use Kafka clients with Event Hubs?](#217-can-you-use-kafka-clients-with-event-hubs)
- [218: What is Event Hubs Capture?](#218-what-is-event-hubs-capture)
- [219: What types of SAS tokens exist and which is the safest?](#219-what-types-of-sas-tokens-exist-and-which-is-the-safest)
- [220: How do you create a user delegation SAS in Node.js so a browser can upload a file directly?](#220-how-do-you-create-a-user-delegation-sas-in-nodejs-so-a-browser-can-upload-a-file-directly)
- [221: What is blob lifecycle management?](#221-what-is-blob-lifecycle-management)
- [222: What data protection features does Blob Storage have?](#222-what-data-protection-features-does-blob-storage-have)
- [223: How do you host a static website in Azure Storage?](#223-how-do-you-host-a-static-website-in-azure-storage)
- [224: How do you configure CORS for Blob Storage?](#224-how-do-you-configure-cors-for-blob-storage)
- [225: What is AzCopy?](#225-what-is-azcopy)
- [226: How do you upload a large file to Blob Storage efficiently from Node.js?](#226-how-do-you-upload-a-large-file-to-blob-storage-efficiently-from-nodejs)
- [227: How do you choose a partition key in Cosmos DB?](#227-how-do-you-choose-a-partition-key-in-cosmos-db)
- [228: What are the Cosmos DB consistency levels?](#228-what-are-the-cosmos-db-consistency-levels)
- [229: What are the Cosmos DB throughput options?](#229-what-are-the-cosmos-db-throughput-options)
- [230: How do you query Cosmos DB from Node.js?](#230-how-do-you-query-cosmos-db-from-nodejs)
- [231: What is the Cosmos DB change feed?](#231-what-is-the-cosmos-db-change-feed)
- [232: What is TTL in Cosmos DB?](#232-what-is-ttl-in-cosmos-db)
- [233: How does indexing work in Cosmos DB?](#233-how-does-indexing-work-in-cosmos-db)
- [234: What is the difference between the DTU and vCore models in Azure SQL Database?](#234-what-is-the-difference-between-the-dtu-and-vcore-models-in-azure-sql-database)
- [235: What is serverless compute in Azure SQL Database?](#235-what-is-serverless-compute-in-azure-sql-database)
- [236: What is an elastic pool?](#236-what-is-an-elastic-pool)
- [237: How do you connect a Node.js app to Azure SQL with Entra ID instead of a password?](#237-how-do-you-connect-a-nodejs-app-to-azure-sql-with-entra-id-instead-of-a-password)
- [238: What is the difference between active geo-replication and failover groups in Azure SQL?](#238-what-is-the-difference-between-active-geo-replication-and-failover-groups-in-azure-sql)
- [239: How does point-in-time restore work in Azure SQL?](#239-how-does-point-in-time-restore-work-in-azure-sql)
- [240: What caching patterns do you use with Azure Cache for Redis?](#240-what-caching-patterns-do-you-use-with-azure-cache-for-redis)
- [241: How do you add Application Insights to a Node.js app today?](#241-how-do-you-add-application-insights-to-a-nodejs-app-today)
- [242: Write a KQL query that shows the slowest API endpoints.](#242-write-a-kql-query-that-shows-the-slowest-api-endpoints)
- [243: How do you find failed dependencies for a specific request in Application Insights?](#243-how-do-you-find-failed-dependencies-for-a-specific-request-in-application-insights)
- [244: What are action groups?](#244-what-are-action-groups)
- [245: What are Azure Monitor workbooks?](#245-what-are-azure-monitor-workbooks)
- [246: What are some common APIM policies?](#246-what-are-some-common-apim-policies)
- [247: What are products and subscriptions in APIM?](#247-what-are-products-and-subscriptions-in-apim)
- [248: What are the APIM tiers?](#248-what-are-the-apim-tiers)
- [249: How do routing rules and the rules engine work in Azure Front Door?](#249-how-do-routing-rules-and-the-rules-engine-work-in-azure-front-door)
- [250: How do you make sure only Front Door can reach your App Service origin?](#250-how-do-you-make-sure-only-front-door-can-reach-your-app-service-origin)
- [251: What WAF features do Front Door and Application Gateway offer?](#251-what-waf-features-do-front-door-and-application-gateway-offer)
- [252: How do you register an API and a client app in Entra ID so the client can call the API?](#252-how-do-you-register-an-api-and-a-client-app-in-entra-id-so-the-client-can-call-the-api)
- [253: What is the difference between delegated permissions (scopes) and application permissions (app roles)?](#253-what-is-the-difference-between-delegated-permissions-scopes-and-application-permissions-app-roles)
- [254: Which OAuth 2.0 flow should each type of app use with Entra ID?](#254-which-oauth-20-flow-should-each-type-of-app-use-with-entra-id)
- [255: How do you validate Entra ID tokens in a Node.js API?](#255-how-do-you-validate-entra-id-tokens-in-a-nodejs-api)
- [256: What is MSAL?](#256-what-is-msal)
- [257: How do you create a custom RBAC role?](#257-how-do-you-create-a-custom-rbac-role)
- [258: What is Privileged Identity Management (PIM)?](#258-what-is-privileged-identity-management-pim)
- [259: What are the Azure Policy effects?](#259-what-are-the-azure-policy-effects)
- [260: Write a simple Azure Policy that only allows certain regions.](#260-write-a-simple-azure-policy-that-only-allows-certain-regions)
- [261: What is a policy initiative?](#261-what-is-a-policy-initiative)
- [262: How does remediation work for DeployIfNotExists and Modify policies?](#262-how-does-remediation-work-for-deployifnotexists-and-modify-policies)
- [263: What is an Azure landing zone?](#263-what-is-an-azure-landing-zone)
- [264: How do you enforce tags across an organization?](#264-how-do-you-enforce-tags-across-an-organization)
- [265: What are common ways to reduce Azure costs?](#265-what-are-common-ways-to-reduce-azure-costs)
- [266: How do autoscale rules work for an App Service plan?](#266-how-do-autoscale-rules-work-for-an-app-service-plan)
- [267: What is the difference between Uniform and Flexible orchestration in VM scale sets?](#267-what-is-the-difference-between-uniform-and-flexible-orchestration-in-vm-scale-sets)
- [268: How do you run setup scripts when a VM starts?](#268-how-do-you-run-setup-scripts-when-a-vm-starts)
- [269: How do you mount an Azure file share in App Service or Container Apps?](#269-how-do-you-mount-an-azure-file-share-in-app-service-or-container-apps)
- [270: How do APIs work in Azure Static Web Apps?](#270-how-do-apis-work-in-azure-static-web-apps)
- [271: What is the difference between Logic Apps Consumption and Standard?](#271-what-is-the-difference-between-logic-apps-consumption-and-standard)
- [272: How do retries work for Azure Functions triggers?](#272-how-do-retries-work-for-azure-functions-triggers)
- [273: How do you troubleshoot an App Service app that won't start?](#273-how-do-you-troubleshoot-an-app-service-app-that-wont-start)
- [274: What is Azure Resource Graph?](#274-what-is-azure-resource-graph)
- [275: How do you use JMESPath queries with the Azure CLI?](#275-how-do-you-use-jmespath-queries-with-the-azure-cli)
- [276: What does az rest do?](#276-what-does-az-rest-do)
- [277: What should you check before moving resources to another resource group or subscription?](#277-what-should-you-check-before-moving-resources-to-another-resource-group-or-subscription)
- [278: What is a good naming convention for Azure resources?](#278-what-is-a-good-naming-convention-for-azure-resources)
- [279: How do you add sign-in to an App Service app without writing auth code?](#279-how-do-you-add-sign-in-to-an-app-service-app-without-writing-auth-code)
- [280: How do you call Microsoft Graph from an app using a managed identity?](#280-how-do-you-call-microsoft-graph-from-an-app-using-a-managed-identity)
- [281: How does App Configuration handle feature flags?](#281-how-does-app-configuration-handle-feature-flags)
- [282: What is the difference between Azure Functions and Azure Container Apps for background processing?](#282-what-is-the-difference-between-azure-functions-and-azure-container-apps-for-background-processing)
- [283: What is the difference between App Service, Container Apps and AKS for hosting a web API?](#283-what-is-the-difference-between-app-service-container-apps-and-aks-for-hosting-a-web-api)
- [284: How do you set up a CI/CD pipeline for a Node.js app on App Service with GitHub Actions?](#284-how-do-you-set-up-a-cicd-pipeline-for-a-nodejs-app-on-app-service-with-github-actions)
- [285: What are access restrictions in App Service?](#285-what-are-access-restrictions-in-app-service)
- [286: What does an Azure SQL firewall do?](#286-what-does-an-azure-sql-firewall-do)
- [287: How do you scale an Azure SQL database without downtime?](#287-how-do-you-scale-an-azure-sql-database-without-downtime)
- [288: What are transient errors and how do you handle them in Azure?](#288-what-are-transient-errors-and-how-do-you-handle-them-in-azure)
- [289: How do you protect a VM from being exposed to the internet?](#289-how-do-you-protect-a-vm-from-being-exposed-to-the-internet)
- [290: What is Azure Update Manager?](#290-what-is-azure-update-manager)
- [291: What is the difference between Azure Monitor Agent and the older agents?](#291-what-is-the-difference-between-azure-monitor-agent-and-the-older-agents)
- [292: What are data collection rules?](#292-what-are-data-collection-rules)
- [293: How do you send custom logs from an app to Log Analytics?](#293-how-do-you-send-custom-logs-from-an-app-to-log-analytics)
- [294: How do you handle secrets in Container Apps?](#294-how-do-you-handle-secrets-in-container-apps)
- [295: How does the Cosmos DB Functions trigger work?](#295-how-does-the-cosmos-db-functions-trigger-work)
- [296: How do you protect against accidental deletion of a production resource group?](#296-how-do-you-protect-against-accidental-deletion-of-a-production-resource-group)
- [297: What is Azure Chaos Studio?](#297-what-is-azure-chaos-studio)
- [298: What is Azure Load Testing?](#298-what-is-azure-load-testing)
- [299: How do you set up a custom domain with HTTPS on Azure Front Door?](#299-how-do-you-set-up-a-custom-domain-with-https-on-azure-front-door)
- [300: How would you organize subscriptions for a mid-sized company?](#300-how-would-you-organize-subscriptions-for-a-mid-sized-company)

### Advanced Questions (301-450)

- [301: What are the five pillars of the Azure Well-Architected Framework?](#301-what-are-the-five-pillars-of-the-azure-well-architected-framework)
- [302: What are RTO and RPO, and how do they affect your Azure design?](#302-what-are-rto-and-rpo-and-how-do-they-affect-your-azure-design)
- [303: Compare the main disaster recovery strategies on Azure.](#303-compare-the-main-disaster-recovery-strategies-on-azure)
- [304: How do you design an active-active multi-region web app on Azure?](#304-how-do-you-design-an-active-active-multi-region-web-app-on-azure)
- [305: How does conflict resolution work with Cosmos DB multi-region writes?](#305-how-does-conflict-resolution-work-with-cosmos-db-multi-region-writes)
- [306: What happens to your app during an Azure SQL failover group failover?](#306-what-happens-to-your-app-during-an-azure-sql-failover-group-failover)
- [307: Why can Traffic Manager failover be slower than expected?](#307-why-can-traffic-manager-failover-be-slower-than-expected)
- [308: How do you design for availability zones inside one region?](#308-how-do-you-design-for-availability-zones-inside-one-region)
- [309: What does zone-redundant mean for App Service, and what do you need to turn it on?](#309-what-does-zone-redundant-mean-for-app-service-and-what-do-you-need-to-turn-it-on)
- [310: How do you do a zero-downtime database schema change while deploying a new app version?](#310-how-do-you-do-a-zero-downtime-database-schema-change-while-deploying-a-new-app-version)
- [311: How do you do a canary release with Azure Front Door or Container Apps?](#311-how-do-you-do-a-canary-release-with-azure-front-door-or-container-apps)
- [312: What are the networking options for AKS?](#312-what-are-the-networking-options-for-aks)
- [313: What is AKS workload identity?](#313-what-is-aks-workload-identity)
- [314: What is the difference between system and user node pools in AKS?](#314-what-is-the-difference-between-system-and-user-node-pools-in-aks)
- [315: How do the cluster autoscaler and HPA work together in AKS?](#315-how-do-the-cluster-autoscaler-and-hpa-work-together-in-aks)
- [316: How do you upgrade an AKS cluster safely?](#316-how-do-you-upgrade-an-aks-cluster-safely)
- [317: What is AKS Automatic?](#317-what-is-aks-automatic)
- [318: How do you make an AKS cluster private?](#318-how-do-you-make-an-aks-cluster-private)
- [319: How do you use Key Vault secrets in AKS pods?](#319-how-do-you-use-key-vault-secrets-in-aks-pods)
- [320: What ingress options exist for AKS?](#320-what-ingress-options-exist-for-aks)
- [321: How do you integrate AKS with Entra ID for user access?](#321-how-do-you-integrate-aks-with-entra-id-for-user-access)
- [322: What is the zero trust model and how do you apply it in Azure?](#322-what-is-the-zero-trust-model-and-how-do-you-apply-it-in-azure)
- [323: How do you prevent data exfiltration from Azure PaaS services?](#323-how-do-you-prevent-data-exfiltration-from-azure-paas-services)
- [324: What are customer-managed keys (CMK) and when do you need them?](#324-what-are-customer-managed-keys-cmk-and-when-do-you-need-them)
- [325: What is Azure Key Vault Managed HSM?](#325-what-is-azure-key-vault-managed-hsm)
- [326: How does encryption in transit work in Azure?](#326-how-does-encryption-in-transit-work-in-azure)
- [327: What is Azure confidential computing?](#327-what-is-azure-confidential-computing)
- [328: How do you rotate secrets that can't be replaced by managed identities?](#328-how-do-you-rotate-secrets-that-cant-be-replaced-by-managed-identities)
- [329: What are the risks of Entra app client secrets and what are the alternatives?](#329-what-are-the-risks-of-entra-app-client-secrets-and-what-are-the-alternatives)
- [330: How do you limit what a compromised managed identity can do?](#330-how-do-you-limit-what-a-compromised-managed-identity-can-do)
- [331: How does Defender for Cloud's secure score work?](#331-how-does-defender-for-clouds-secure-score-work)
- [332: What is Defender CSPM's attack path analysis?](#332-what-is-defender-cspms-attack-path-analysis)
- [333: How do you secure a Cosmos DB account?](#333-how-do-you-secure-a-cosmos-db-account)
- [334: Why should you create SDK clients like CosmosClient or BlobServiceClient only once?](#334-why-should-you-create-sdk-clients-like-cosmosclient-or-blobserviceclient-only-once)
- [335: What is SNAT port exhaustion and how do you fix it in App Service?](#335-what-is-snat-port-exhaustion-and-how-do-you-fix-it-in-app-service)
- [336: How do you detect and fix a hot partition in Cosmos DB?](#336-how-do-you-detect-and-fix-a-hot-partition-in-cosmos-db)
- [337: Why are cross-partition queries expensive in Cosmos DB, and how do you avoid them?](#337-why-are-cross-partition-queries-expensive-in-cosmos-db-and-how-do-you-avoid-them)
- [338: How do you do bulk inserts into Cosmos DB efficiently?](#338-how-do-you-do-bulk-inserts-into-cosmos-db-efficiently)
- [339: What is Azure SQL Hyperscale and when do you use it?](#339-what-is-azure-sql-hyperscale-and-when-do-you-use-it)
- [340: How do you find and fix slow queries in Azure SQL?](#340-how-do-you-find-and-fix-slow-queries-in-azure-sql)
- [341: What is read scale-out in Azure SQL?](#341-what-is-read-scale-out-in-azure-sql)
- [342: How do you avoid large keys and other common problems with Redis on Azure?](#342-how-do-you-avoid-large-keys-and-other-common-problems-with-redis-on-azure)
- [343: How do you size Event Hubs throughput?](#343-how-do-you-size-event-hubs-throughput)
- [344: How do you keep message order while scaling consumers?](#344-how-do-you-keep-message-order-while-scaling-consumers)
- [345: What is the outbox pattern and how do you implement it on Azure?](#345-what-is-the-outbox-pattern-and-how-do-you-implement-it-on-azure)
- [346: How do you make message consumers idempotent?](#346-how-do-you-make-message-consumers-idempotent)
- [347: How do you handle poison messages?](#347-how-do-you-handle-poison-messages)
- [348: How does Durable Functions replay work, and why must orchestrators be deterministic?](#348-how-does-durable-functions-replay-work-and-why-must-orchestrators-be-deterministic)
- [349: What storage providers can Durable Functions use?](#349-what-storage-providers-can-durable-functions-use)
- [350: How does the Azure Functions scale controller decide how many instances to run?](#350-how-does-the-azure-functions-scale-controller-decide-how-many-instances-to-run)
- [351: What are ARM throttling limits and how do you deal with them?](#351-what-are-arm-throttling-limits-and-how-do-you-deal-with-them)
- [352: How do you handle 429 responses from Azure services in your app?](#352-how-do-you-handle-429-responses-from-azure-services-in-your-app)
- [353: How do you design a multi-tenant SaaS application on Azure?](#353-how-do-you-design-a-multi-tenant-saas-application-on-azure)
- [354: What is the deployment stamps pattern?](#354-what-is-the-deployment-stamps-pattern)
- [355: How do you choose between Azure Firewall, NSGs and NVAs?](#355-how-do-you-choose-between-azure-firewall-nsgs-and-nvas)
- [356: What is Azure Virtual WAN and when would you choose it over a hand-built hub-and-spoke?](#356-what-is-azure-virtual-wan-and-when-would-you-choose-it-over-a-hand-built-hub-and-spoke)
- [357: How do you set up DNS for private endpoints in a hybrid network?](#357-how-do-you-set-up-dns-for-private-endpoints-in-a-hybrid-network)
- [358: What is forced tunneling and what problems can it cause?](#358-what-is-forced-tunneling-and-what-problems-can-it-cause)
- [359: What is asymmetric routing and how does it break things in Azure?](#359-what-is-asymmetric-routing-and-how-does-it-break-things-in-azure)
- [360: What is Azure Private Link Service?](#360-what-is-azure-private-link-service)
- [361: How do you make a whole PaaS solution private (no public endpoints)?](#361-how-do-you-make-a-whole-paas-solution-private-no-public-endpoints)
- [362: How do Azure Front Door caching and origin shielding work?](#362-how-do-azure-front-door-caching-and-origin-shielding-work)
- [363: How do you protect an API against DDoS attacks on Azure?](#363-how-do-you-protect-an-api-against-ddos-attacks-on-azure)
- [364: How does distributed tracing work across Azure services?](#364-how-does-distributed-tracing-work-across-azure-services)
- [365: How do you control Application Insights and Log Analytics costs?](#365-how-do-you-control-application-insights-and-log-analytics-costs)
- [366: What is the difference between Analytics, Basic and Auxiliary logs in Log Analytics?](#366-what-is-the-difference-between-analytics-basic-and-auxiliary-logs-in-log-analytics)
- [367: How do you define and monitor SLOs for an Azure app?](#367-how-do-you-define-and-monitor-slos-for-an-azure-app)
- [368: What is Azure Managed Grafana and Azure Monitor managed service for Prometheus?](#368-what-is-azure-managed-grafana-and-azure-monitor-managed-service-for-prometheus)
- [369: How would you troubleshoot intermittent 502 errors from Application Gateway?](#369-how-would-you-troubleshoot-intermittent-502-errors-from-application-gateway)
- [370: How would you troubleshoot high latency in a Node.js API on App Service?](#370-how-would-you-troubleshoot-high-latency-in-a-nodejs-api-on-app-service)
- [371: What is Azure App Service Environment (ASE)?](#371-what-is-azure-app-service-environment-ase)
- [372: When would you choose Azure SQL Managed Instance over Azure SQL Database?](#372-when-would-you-choose-azure-sql-managed-instance-over-azure-sql-database)
- [373: How do you migrate an on-premises Node.js + PostgreSQL app to Azure?](#373-how-do-you-migrate-an-on-premises-nodejs--postgresql-app-to-azure)
- [374: What are the main features of Azure Database for PostgreSQL Flexible Server you should know?](#374-what-are-the-main-features-of-azure-database-for-postgresql-flexible-server-you-should-know)
- [375: How do you implement retrieval-augmented generation (RAG) on Azure?](#375-how-do-you-implement-retrieval-augmented-generation-rag-on-azure)
- [376: How do you call an Azure OpenAI deployment from Node.js with Entra ID auth?](#376-how-do-you-call-an-azure-openai-deployment-from-nodejs-with-entra-id-auth)
- [377: How do you handle quotas and scaling for Azure OpenAI in production?](#377-how-do-you-handle-quotas-and-scaling-for-azure-openai-in-production)
- [378: What is the "AI gateway" in Azure API Management?](#378-what-is-the-ai-gateway-in-azure-api-management)
- [379: How do you secure a public storage-backed file download feature for authenticated users only?](#379-how-do-you-secure-a-public-storage-backed-file-download-feature-for-authenticated-users-only)
- [380: Design a file upload and processing pipeline on Azure.](#380-design-a-file-upload-and-processing-pipeline-on-azure)
- [381: Design a URL shortener on Azure that can handle high read traffic.](#381-design-a-url-shortener-on-azure-that-can-handle-high-read-traffic)
- [382: How would you design an order processing system with Azure messaging?](#382-how-would-you-design-an-order-processing-system-with-azure-messaging)
- [383: How do you implement the saga pattern with Durable Functions?](#383-how-do-you-implement-the-saga-pattern-with-durable-functions)
- [384: What are the limits and gotchas of Azure Functions HTTP triggers?](#384-what-are-the-limits-and-gotchas-of-azure-functions-http-triggers)
- [385: How do you protect downstream systems from Azure Functions scaling too fast?](#385-how-do-you-protect-downstream-systems-from-azure-functions-scaling-too-fast)
- [386: How do you share code and configuration between many Function apps or microservices without coupling them?](#386-how-do-you-share-code-and-configuration-between-many-function-apps-or-microservices-without-coupling-them)
- [387: How does Azure handle platform maintenance on VMs, and how do you reduce its impact?](#387-how-does-azure-handle-platform-maintenance-on-vms-and-how-do-you-reduce-its-impact)
- [388: What is the Azure Instance Metadata Service (IMDS)?](#388-what-is-the-azure-instance-metadata-service-imds)
- [389: How do you protect against SSRF attacks that target managed identity tokens?](#389-how-do-you-protect-against-ssrf-attacks-that-target-managed-identity-tokens)
- [390: How do you handle long-running operations (LROs) in the Azure SDKs?](#390-how-do-you-handle-long-running-operations-lros-in-the-azure-sdks)
- [391: What are ETags and how do you use them for optimistic concurrency in Azure?](#391-what-are-etags-and-how-do-you-use-them-for-optimistic-concurrency-in-azure)
- [392: How do you implement a distributed lock on Azure?](#392-how-do-you-implement-a-distributed-lock-on-azure)
- [393: What are the main egress (data transfer) cost traps in Azure?](#393-what-are-the-main-egress-data-transfer-cost-traps-in-azure)
- [394: How do you implement FinOps practices in Azure?](#394-how-do-you-implement-finops-practices-in-azure)
- [395: How do you decide between reservations and savings plans?](#395-how-do-you-decide-between-reservations-and-savings-plans)
- [396: What is subscription vending?](#396-what-is-subscription-vending)
- [397: How do you manage policy as code?](#397-how-do-you-manage-policy-as-code)
- [398: What is the difference between Azure Policy and Azure Blueprints?](#398-what-is-the-difference-between-azure-policy-and-azure-blueprints)
- [399: What are template specs?](#399-what-are-template-specs)
- [400: How does Azure Resource Manager handle dependencies and parallelism in a Bicep deployment?](#400-how-does-azure-resource-manager-handle-dependencies-and-parallelism-in-a-bicep-deployment)
- [401: How do you test Bicep and other infrastructure code?](#401-how-do-you-test-bicep-and-other-infrastructure-code)
- [402: How do you handle configuration drift between your IaC and what's actually in Azure?](#402-how-do-you-handle-configuration-drift-between-your-iac-and-whats-actually-in-azure)
- [403: What is the blast radius concept and how do you limit it in Azure?](#403-what-is-the-blast-radius-concept-and-how-do-you-limit-it-in-azure)
- [404: How would you roll out a change safely across many regions?](#404-how-would-you-roll-out-a-change-safely-across-many-regions)
- [405: What is the Retry pattern vs the Circuit Breaker pattern, and how do they work together?](#405-what-is-the-retry-pattern-vs-the-circuit-breaker-pattern-and-how-do-they-work-together)
- [406: What is the Queue-Based Load Leveling pattern and when do you use it on Azure?](#406-what-is-the-queue-based-load-leveling-pattern-and-when-do-you-use-it-on-azure)
- [407: What is the Claim-Check pattern?](#407-what-is-the-claim-check-pattern)
- [408: What is the Competing Consumers pattern?](#408-what-is-the-competing-consumers-pattern)
- [409: What is the Valet Key pattern?](#409-what-is-the-valet-key-pattern)
- [410: What is the Strangler Fig pattern and how do you apply it when moving to Azure?](#410-what-is-the-strangler-fig-pattern-and-how-do-you-apply-it-when-moving-to-azure)
- [411: What is the Backends for Frontends (BFF) pattern and how would you host it on Azure?](#411-what-is-the-backends-for-frontends-bff-pattern-and-how-would-you-host-it-on-azure)
- [412: How do you secure a single-page app that calls APIs with Entra ID?](#412-how-do-you-secure-a-single-page-app-that-calls-apis-with-entra-id)
- [413: What are Continuous Access Evaluation (CAE) and token lifetimes in Entra ID?](#413-what-are-continuous-access-evaluation-cae-and-token-lifetimes-in-entra-id)
- [414: How does Conditional Access apply to workload identities?](#414-how-does-conditional-access-apply-to-workload-identities)
- [415: What is a cross-tenant scenario in Azure and how do you handle access?](#415-what-is-a-cross-tenant-scenario-in-azure-and-how-do-you-handle-access)
- [416: What is Azure Lighthouse?](#416-what-is-azure-lighthouse)
- [417: How would you design a secure CI/CD pipeline for production Azure deployments?](#417-how-would-you-design-a-secure-cicd-pipeline-for-production-azure-deployments)
- [418: How do you sign and verify container images on Azure?](#418-how-do-you-sign-and-verify-container-images-on-azure)
- [419: What does Defender for Containers do?](#419-what-does-defender-for-containers-do)
- [420: How do you enforce Kubernetes security rules in AKS with Azure Policy?](#420-how-do-you-enforce-kubernetes-security-rules-in-aks-with-azure-policy)
- [421: How do you handle stateful workloads on AKS?](#421-how-do-you-handle-stateful-workloads-on-aks)
- [422: What is the Istio-based service mesh add-on for AKS, and when do you need a service mesh?](#422-what-is-the-istio-based-service-mesh-add-on-for-aks-and-when-do-you-need-a-service-mesh)
- [423: How do you reduce cold start and image pull time in Container Apps and AKS?](#423-how-do-you-reduce-cold-start-and-image-pull-time-in-container-apps-and-aks)
- [424: How do probes work in Azure Container Apps, and what happens if they're misconfigured?](#424-how-do-probes-work-in-azure-container-apps-and-what-happens-if-theyre-misconfigured)
- [425: How do you design Cosmos DB data models differently from SQL?](#425-how-do-you-design-cosmos-db-data-models-differently-from-sql)
- [426: How does Cosmos DB guarantee availability in a single region and across regions?](#426-how-does-cosmos-db-guarantee-availability-in-a-single-region-and-across-regions)
- [427: What are hierarchical partition keys in Cosmos DB?](#427-what-are-hierarchical-partition-keys-in-cosmos-db)
- [428: How do you do vector search in Cosmos DB?](#428-how-do-you-do-vector-search-in-cosmos-db)
- [429: How do you choose the right database on Azure for a new service?](#429-how-do-you-choose-the-right-database-on-azure-for-a-new-service)
- [430: How do you migrate a large production database to Azure with minimal downtime?](#430-how-do-you-migrate-a-large-production-database-to-azure-with-minimal-downtime)
- [431: How do you make Azure Key Vault highly available and avoid it becoming a bottleneck?](#431-how-do-you-make-azure-key-vault-highly-available-and-avoid-it-becoming-a-bottleneck)
- [432: What is the difference between Azure Storage account failover and the old geo-redundancy behavior?](#432-what-is-the-difference-between-azure-storage-account-failover-and-the-old-geo-redundancy-behavior)
- [433: How do you protect backups from ransomware in Azure?](#433-how-do-you-protect-backups-from-ransomware-in-azure)
- [434: What's the difference between high availability and disaster recovery?](#434-whats-the-difference-between-high-availability-and-disaster-recovery)
- [435: How do you test that your disaster recovery plan actually works?](#435-how-do-you-test-that-your-disaster-recovery-plan-actually-works)
- [436: How would you design logging and monitoring for 50 microservices across several subscriptions?](#436-how-would-you-design-logging-and-monitoring-for-50-microservices-across-several-subscriptions)
- [437: How do you correlate logs from an Azure Function triggered by Service Bus with the HTTP request that started it?](#437-how-do-you-correlate-logs-from-an-azure-function-triggered-by-service-bus-with-the-http-request-that-started-it)
- [438: What happens when an Azure region has an outage and what can you do in advance?](#438-what-happens-when-an-azure-region-has-an-outage-and-what-can-you-do-in-advance)
- [439: What are on-demand capacity reservations?](#439-what-are-on-demand-capacity-reservations)
- [440: How do you handle the "AllocationFailed" or "SkuNotAvailable" errors?](#440-how-do-you-handle-the-allocationfailed-or-skunotavailable-errors)
- [441: How do you make Azure Functions or App Service handle a sudden 10x traffic spike?](#441-how-do-you-make-azure-functions-or-app-service-handle-a-sudden-10x-traffic-spike)
- [442: Scenario: your Cosmos DB bill suddenly doubled. How do you investigate?](#442-scenario-your-cosmos-db-bill-suddenly-doubled-how-do-you-investigate)
- [443: Scenario: an App Service app slows down every day around the same time. What do you check?](#443-scenario-an-app-service-app-slows-down-every-day-around-the-same-time-what-do-you-check)
- [444: Scenario: a developer accidentally committed a storage account key to a public GitHub repo. What do you do?](#444-scenario-a-developer-accidentally-committed-a-storage-account-key-to-a-public-github-repo-what-do-you-do)
- [445: Scenario: a Service Bus queue keeps growing and consumers can't keep up. What do you do?](#445-scenario-a-service-bus-queue-keeps-growing-and-consumers-cant-keep-up-what-do-you-do)
- [446: Scenario: after enabling private endpoints on a storage account, your Function app can't start. Why?](#446-scenario-after-enabling-private-endpoints-on-a-storage-account-your-function-app-cant-start-why)
- [447: Scenario: your team wants to move from App Service to AKS "because everyone uses Kubernetes". How do you respond?](#447-scenario-your-team-wants-to-move-from-app-service-to-aks-because-everyone-uses-kubernetes-how-do-you-respond)
- [448: Scenario: you need to run a nightly job that takes 3 hours. Which Azure service would you use?](#448-scenario-you-need-to-run-a-nightly-job-that-takes-3-hours-which-azure-service-would-you-use)
- [449: Scenario: management wants to cut the Azure bill by 30% without hurting reliability. Where do you start?](#449-scenario-management-wants-to-cut-the-azure-bill-by-30-without-hurting-reliability-where-do-you-start)
- [450: Scenario: design the Azure architecture for a new e-commerce platform expected to grow fast.](#450-scenario-design-the-azure-architecture-for-a-new-e-commerce-platform-expected-to-grow-fast)

---

# Easy Questions (1-150)

## 1: What is Microsoft Azure?

Azure is Microsoft's public cloud platform. It gives you on-demand access to compute, storage, networking, databases, messaging, AI and many other services that run in Microsoft's data centers around the world. You pay for what you use instead of buying and running your own hardware.

## 2: What are IaaS, PaaS and SaaS? Give an Azure example of each.

- **IaaS (Infrastructure as a Service):** you rent virtual machines, disks and networks, and you manage the OS and everything above it. Example: Azure Virtual Machines.
- **PaaS (Platform as a Service):** Azure manages the OS and runtime, you deploy your code or data. Example: Azure App Service, Azure SQL Database.
- **SaaS (Software as a Service):** a finished product you just use. Example: Microsoft 365.

The higher you go, the less you manage and the less control you have.

## 3: What is the shared responsibility model?

It describes which security and operations tasks belong to Microsoft and which belong to you. Microsoft always handles the physical data centers, hardware and host network. With IaaS you are responsible for the OS, patches, apps and data. With PaaS Microsoft also handles the OS and runtime. In every model you are still responsible for your data, identities, access and how you configure the service.

## 4: What is an Azure region?

A region is a geographic area with one or more data centers connected by a low-latency network, for example `westeurope` or `eastus2`. You choose a region when you create most resources. The choice affects latency to users, price, which services are available, and data residency rules.

## 5: What are availability zones?

Availability zones are physically separate locations inside one region. Each zone has its own power, cooling and networking. If you spread resources across zones (for example zone-redundant storage or VMs in zones 1, 2 and 3), your app survives the failure of a whole data center. Not every region has zones.

## 6: What are region pairs?

Most Azure regions are paired with another region in the same geography, for example North Europe and West Europe. Microsoft rolls out platform updates to one region of a pair at a time, and some services (like geo-redundant storage) replicate to the paired region by default. Newer regions are often built without a pair and rely on availability zones instead.

## 7: What is an Azure geography?

A geography is a group of regions that share data residency and compliance rules, usually a country or a market such as "Europe", "United States" or "Germany". It matters when your company has legal rules about where data can be stored.

## 8: What is the hierarchy of Azure resources from top to bottom?

1. **Entra ID tenant** (the identity directory of the organization)
2. **Management groups** (optional, group subscriptions)
3. **Subscriptions** (billing and access boundary)
4. **Resource groups** (logical containers)
5. **Resources** (VMs, storage accounts, databases and so on)

Access rules and policies set at a higher level are inherited by everything below.

## 9: What is an Azure subscription?

A subscription is a billing unit and an access boundary. Every resource belongs to exactly one subscription, and the costs of those resources go on that subscription's bill. Companies often have separate subscriptions for production, development and different teams. Subscriptions also have quotas, such as how many vCPUs you can use per region.

## 10: What is a resource group?

A resource group is a container that holds related resources for one solution, for example the web app, database and storage account of one project. A resource can be in only one resource group. When you delete the resource group, every resource inside it is deleted too, which makes cleanup easy.

```bash
az group create --name rg-shop-dev --location westeurope
```

## 11: Can resources in one resource group be in different regions?

Yes. The resource group has a location, but that location only stores the group's metadata. The resources inside can be in any region. In practice teams often keep them in the same region to make things easier to reason about.

## 12: What is a management group?

A management group is a container above subscriptions. You use it to apply Azure Policy and role assignments to many subscriptions at once. For example, you can have a "Production" management group that blocks certain VM sizes for every subscription inside it. Management groups can be nested up to six levels deep under the root.

## 13: What is Azure Resource Manager (ARM)?

ARM is the deployment and management layer of Azure. Every request to create, change or delete a resource, whether from the portal, CLI, PowerShell, SDK or Bicep, goes through the ARM API. ARM checks authentication and authorization, applies policies and then sends the request to the right resource provider.

## 14: What is a resource provider?

A resource provider is the service that supplies a type of resource, for example `Microsoft.Compute` for VMs or `Microsoft.Storage` for storage accounts. A subscription must have a provider registered before you can create its resources. Many are registered automatically, but sometimes you need to do it by hand.

```bash
az provider register --namespace Microsoft.App
```

## 15: What is the Azure portal?

The Azure portal (portal.azure.com) is the web UI for managing Azure. You can create resources, look at metrics and logs, change settings and see costs. It is great for learning and checking things, but production environments should be created with code (Bicep, Terraform) so they can be repeated.

## 16: What is the Azure CLI?

The Azure CLI (`az`) is a cross-platform command-line tool for managing Azure. Commands follow a `az <group> <subgroup> <action>` pattern.

```bash
az login
az account set --subscription "My Subscription"
az vm list --output table
```

## 17: What is Azure PowerShell?

Azure PowerShell is a set of PowerShell modules (the `Az` module) for managing Azure. It does the same things as the Azure CLI, but with PowerShell cmdlets like `New-AzResourceGroup`. Teams with a Windows or PowerShell background often prefer it, while the CLI is more common in Linux and Bash scripts.

## 18: What is Azure Cloud Shell?

Cloud Shell is a browser-based shell that you open from the portal. It comes with the Azure CLI, Azure PowerShell, Terraform, kubectl, git and other tools already installed and logged in as you. You can attach a storage account to keep your files between sessions.

## 19: What is Microsoft Entra ID?

Microsoft Entra ID (formerly Azure Active Directory) is Microsoft's cloud identity service. It stores users, groups and applications, handles sign-in, multi-factor authentication and single sign-on, and issues tokens (OAuth 2.0 and OpenID Connect). Every Azure subscription trusts exactly one Entra ID tenant.

## 20: What is a tenant?

A tenant is a dedicated instance of Entra ID for an organization. It has its own users, groups and app registrations and usually a domain like `contoso.onmicrosoft.com`. One tenant can have many subscriptions, but each subscription belongs to one tenant.

## 21: Is Entra ID the same as on-premises Active Directory?

No. On-premises Active Directory Domain Services uses Kerberos, NTLM, LDAP and Group Policy and is designed for computers on a corporate network. Entra ID is a cloud identity service that uses web protocols like OAuth 2.0, OpenID Connect and SAML. You can sync on-premises AD users to Entra ID with Entra Connect so people use one identity for both.

## 22: What is Azure role-based access control (RBAC)?

Azure RBAC controls who can do what on Azure resources. A **role assignment** has three parts: a **security principal** (user, group, service principal or managed identity), a **role definition** (a set of allowed actions), and a **scope** (management group, subscription, resource group or single resource).

```bash
az role assignment create \
  --assignee user@contoso.com \
  --role "Reader" \
  --scope /subscriptions/<sub-id>/resourceGroups/rg-shop-dev
```

## 23: What are the most common built-in Azure roles?

- **Owner:** full access, including managing role assignments.
- **Contributor:** can create and manage all resources, but cannot assign roles.
- **Reader:** can view everything, cannot change anything.
- **User Access Administrator:** can manage role assignments only.

There are also many service-specific roles like "Storage Blob Data Reader" or "Key Vault Secrets User".

## 24: What is the difference between Azure RBAC roles and Entra ID roles?

Azure RBAC roles control access to Azure resources (VMs, storage, and so on) at management group, subscription, resource group or resource scope. Entra ID roles control access to the directory itself, for example creating users, resetting passwords or managing app registrations. A Global Administrator in Entra ID does not automatically have access to subscriptions, although they can elevate themselves to get it.

## 25: What is a service principal?

A service principal is an identity for an application inside an Entra ID tenant. When an app, script or CI pipeline needs to call Azure, it signs in as a service principal and gets RBAC permissions like a user would. Service principals are created from app registrations, or automatically for managed identities.

## 26: What is a managed identity?

A managed identity is an identity in Entra ID that Azure creates and manages for a resource, for example an App Service or a VM. Your code uses it to get tokens for other Azure services, so you do not need to store passwords or keys. Azure rotates the credentials for you.

## 27: What are the two types of managed identities?

- **System-assigned:** created as part of one resource and deleted together with it. One resource, one identity.
- **User-assigned:** a standalone Azure resource that you create once and attach to one or more resources. It lives on after those resources are deleted.

## 28: What is an Azure Virtual Machine?

An Azure VM is a virtual server running Windows or Linux in Azure. You pick the size (CPU, memory), the image (for example Ubuntu 24.04), disks and network. You are responsible for the OS, patches and software. VMs are the IaaS option, used when you need full control or run software that cannot move to PaaS.

```bash
az vm create \
  --resource-group rg-demo \
  --name vm-web-01 \
  --image Ubuntu2404 \
  --size Standard_B2s \
  --admin-username azureuser \
  --generate-ssh-keys
```

## 29: How are Azure VM sizes named?

VM sizes are grouped into families by purpose: **B** (burstable), **D** (general purpose), **E** (memory optimized), **F** (compute optimized), **L** (storage optimized), **N** (GPU), **M** (very large memory). A name like `Standard_D4s_v5` means: D family, 4 vCPUs, `s` supports premium storage, version 5. Other letters include `a` (AMD), `p` (ARM-based) and `d` (local temp disk).

## 30: What disks does an Azure VM have?

- **OS disk:** holds the operating system.
- **Data disks:** extra disks you attach for application data.
- **Temporary disk:** local storage on the host, fast but the data can be lost when the VM is moved or deallocated. Use it only for things like swap or scratch files.

OS and data disks are managed disks stored in Azure Storage.

## 31: What are the managed disk types?

- **Standard HDD:** cheapest, for backups and rarely used data.
- **Standard SSD:** for light production and dev/test workloads.
- **Premium SSD:** for production workloads that need low latency.
- **Premium SSD v2:** you set size, IOPS and throughput separately.
- **Ultra Disk:** highest performance, for heavy databases like SAP HANA.

## 32: What is the difference between stopping and deallocating a VM?

If you shut down the VM from inside the OS, it is "stopped" but still allocated on the host, so you keep paying for compute. If you stop it from the portal or with `az vm deallocate`, it is "stopped (deallocated)", the compute is released and you only pay for disks and any static public IP.

```bash
az vm deallocate --resource-group rg-demo --name vm-web-01
```

## 33: What is an availability set?

An availability set spreads VMs across **fault domains** (separate racks with their own power and network switch) and **update domains** (groups that are rebooted at different times during maintenance). It protects against hardware failure and planned maintenance inside one data center. Availability zones give stronger protection and are preferred where available.

## 34: What is a Virtual Machine Scale Set?

A Virtual Machine Scale Set (VMSS) lets you run a group of identical VMs that can scale out and in automatically based on rules like CPU usage or a schedule. Scale sets can spread instances across availability zones and work with load balancers. They are used for large stateless workloads and are also what AKS uses for its node pools.

## 35: What is Azure App Service?

App Service is a PaaS for hosting web apps, REST APIs and mobile back ends. You can run code in .NET, Node.js, Python, Java or PHP, or bring your own container, on Windows or Linux. Azure handles the OS, patching, load balancing and scaling, and gives you features like deployment slots, custom domains, TLS certificates and built-in authentication.

## 36: What is an App Service plan?

An App Service plan is the set of compute resources (VMs) that your web apps run on. The plan defines the region, OS, number of instances and the pricing tier (Free, Basic, Standard, Premium, Isolated). Several apps can share one plan, and they all share its CPU and memory. You pay for the plan, not per app.

```bash
az appservice plan create -g rg-demo -n plan-web --sku P0V3 --is-linux
az webapp create -g rg-demo -p plan-web -n my-shop-api --runtime "NODE:22-lts"
```

## 37: What is the difference between scaling up and scaling out?

- **Scale up (vertical):** move to a bigger instance, more CPU and memory per machine. For App Service this means changing the pricing tier.
- **Scale out (horizontal):** add more instances of the same size behind a load balancer.

Scaling out is usually better for web apps because it also adds redundancy, but the app must be stateless.

## 38: What is Azure Functions?

Azure Functions is a serverless compute service. You write small pieces of code (functions) that run in response to events, like an HTTP request, a new message in a queue, a file uploaded to Blob Storage or a timer. Azure handles the servers and scales the number of instances based on load. On the consumption-based plans you pay only for execution.

## 39: What are triggers and bindings in Azure Functions?

- A **trigger** is what starts a function. Each function has exactly one trigger, such as HTTP, timer, Service Bus or Blob.
- **Bindings** connect the function to other services without writing client code. Input bindings read data, output bindings write data, for example writing a message to a queue by returning a value.

## 40: What does a basic HTTP-triggered function look like in Node.js?

With the Node.js v4 programming model you register functions in code:

```js
const { app } = require("@azure/functions");

app.http("hello", {
  methods: ["GET"],
  authLevel: "anonymous",
  handler: async (request, context) => {
    const name = request.query.get("name") || "world";
    context.log(`Request for ${name}`);
    return { body: `Hello, ${name}!` };
  },
});
```

The older v3 model used a `function.json` file per function. It is still around in older projects, but new code should use v4.

## 41: What are the Azure Functions hosting plans?

- **Flex Consumption:** the recommended serverless plan. Pay per use, scales to zero, fast scaling, VNet integration and optional "always ready" instances.
- **Consumption:** the original serverless plan. The Linux version is legacy and retires in September 2028.
- **Premium (Elastic Premium):** pre-warmed instances with no cold start, VNet support, longer run times.
- **Dedicated (App Service plan):** runs on an App Service plan you already pay for.
- **Container Apps:** run functions as containers inside Azure Container Apps.

## 42: What is a cold start?

A cold start is the extra delay when a serverless platform has to create a new instance to handle a request, for example after the app has scaled to zero. It includes starting the host, loading your code and running initialization. Ways to reduce it: Flex Consumption "always ready" instances, the Premium plan, smaller deployment packages and lighter startup code.

## 43: What is a timer trigger?

A timer trigger runs a function on a schedule written as a six-field NCRONTAB expression (seconds included).

```js
const { app } = require("@azure/functions");

app.timer("nightlyCleanup", {
  schedule: "0 0 2 * * *", // every day at 02:00 UTC
  handler: async (timer, context) => {
    context.log("Running cleanup");
  },
});
```

## 44: What is Azure Container Instances (ACI)?

ACI runs containers directly without managing VMs or an orchestrator. You give it an image, CPU and memory, and it starts in seconds. You pay per second. It is good for simple tasks, batch jobs, build agents and quick tests, but it does not have built-in autoscaling, load balancing or rolling updates.

## 45: What is Azure Container Apps?

Azure Container Apps is a serverless platform for running containerized apps and microservices. It is built on Kubernetes, KEDA, Envoy and Dapr, but you don't manage the cluster. It supports HTTP ingress, scale to zero, scaling on events (queue length, HTTP traffic), revisions with traffic splitting, and background jobs.

## 46: What is Azure Kubernetes Service (AKS)?

AKS is Azure's managed Kubernetes service. Azure runs and manages the Kubernetes control plane for you, and you manage the worker nodes (node pools) and your workloads. It is the choice when you need the full Kubernetes API and ecosystem, such as Helm charts, operators, custom controllers and fine-grained networking.

## 47: What is Azure Container Registry (ACR)?

ACR is a private registry for Docker images, Helm charts and other OCI artifacts. AKS, Container Apps, App Service and ACI can pull images from it, usually using a managed identity. Premium tier adds geo-replication, private endpoints and content trust.

```bash
az acr create -g rg-demo -n myregistry123 --sku Basic
az acr build --registry myregistry123 --image api:v1 .
```

## 48: What is an Azure Storage account?

A storage account is a resource that gives you a unique namespace for storing data. One account can hold four types of data services: **Blob** (objects/files), **Queue** (simple messages), **Table** (NoSQL key-value) and **Files** (SMB/NFS file shares). Its endpoints look like `https://<account>.blob.core.windows.net`.

## 49: What is Azure Blob Storage?

Blob Storage stores unstructured data like images, videos, backups, logs and static files. Data is organized as **storage account → container → blob**. There are three blob types: **block blobs** (most files), **append blobs** (logs that are only appended to) and **page blobs** (random read/write, used for VM disks).

## 50: What are the blob access tiers?

- **Hot:** frequently accessed data, highest storage cost, lowest access cost.
- **Cool:** infrequently accessed, kept at least 30 days.
- **Cold:** rarely accessed, kept at least 90 days.
- **Archive:** offline, cheapest storage, kept at least 180 days. Reading it requires "rehydration", which can take hours.

Deleting or moving data before the minimum period costs an early deletion fee.

## 51: What redundancy options does Azure Storage offer?

- **LRS (locally redundant):** 3 copies in one data center.
- **ZRS (zone-redundant):** 3 copies across 3 availability zones in one region.
- **GRS (geo-redundant):** LRS in the primary region plus an async copy (LRS) in the paired secondary region.
- **GZRS (geo-zone-redundant):** ZRS in the primary plus LRS in the secondary.
- **RA-GRS / RA-GZRS:** same as GRS/GZRS, but you can also read from the secondary.

## 52: What is Azure Queue Storage?

Queue Storage is a simple message queue inside a storage account. A message can be up to 64 KB, and a queue can hold millions of messages. It is cheap and easy, good for basic background work. For ordering, sessions, topics, transactions or bigger messages, use Azure Service Bus instead.

## 53: What is Azure Table Storage?

Table Storage is a NoSQL key-value store for structured data without a fixed schema. Each entity has a **PartitionKey** and a **RowKey** that together form its unique key. It is cheap and fast for simple lookups but has limited querying. Azure Cosmos DB for Table offers the same API with more features.

## 54: What is Azure Files?

Azure Files gives you fully managed file shares that you can mount over SMB or NFS from Windows, Linux, macOS, VMs, containers and App Service. It is often used to replace on-premises file servers, for shared configuration, or for "lift and shift" apps that expect a normal file system.

## 55: What is Azure Data Lake Storage Gen2?

Data Lake Storage Gen2 is Blob Storage with a **hierarchical namespace** turned on. It adds real directories, atomic folder rename and POSIX-style access control lists. It is the standard storage for big data and analytics tools like Databricks, Synapse and Microsoft Fabric.

## 56: What is Azure SQL Database?

Azure SQL Database is a fully managed relational database based on the latest SQL Server engine. Microsoft handles patching, backups, high availability and upgrades. You connect to it like a normal SQL Server using T-SQL, and you choose a purchasing model (DTU or vCore) and tier based on performance needs.

## 57: What are the Azure SQL deployment options?

- **Azure SQL Database:** a single managed database or an elastic pool. Best for new cloud apps.
- **Azure SQL Managed Instance:** almost full SQL Server compatibility (SQL Agent, cross-database queries, CLR), good for migrating existing apps.
- **SQL Server on Azure VMs:** full control of SQL Server and the OS, IaaS.

## 58: What is Azure Cosmos DB?

Cosmos DB is a fully managed, globally distributed NoSQL database. It offers single-digit millisecond reads and writes, automatic indexing, multi-region replication and several APIs: NoSQL (the native one), MongoDB, Apache Cassandra, Apache Gremlin and Table. There is also Azure Cosmos DB for PostgreSQL for distributed relational data.

## 59: What is a request unit (RU) in Cosmos DB?

A request unit is the currency for throughput in Cosmos DB. Every operation costs RUs based on CPU, memory and IO. Reading a 1 KB item by its ID and partition key costs about 1 RU. Writes, queries and bigger items cost more. You either provision RU/s, use autoscale, or use serverless where you pay per RU consumed.

## 60: What managed open-source databases does Azure offer?

- **Azure Database for PostgreSQL – Flexible Server**
- **Azure Database for MySQL – Flexible Server**
- **Azure Managed Redis** and **Azure Cache for Redis** for caching
- **Azure Cosmos DB for MongoDB** (MongoDB-compatible API)

The older "Single Server" options for PostgreSQL and MySQL are retired, so Flexible Server is the one to use.

## 61: What is Azure Cache for Redis?

It is a managed Redis cache used to speed up apps by keeping frequently used data in memory, store sessions, implement rate limiting or act as a simple message broker. Microsoft has also released **Azure Managed Redis**, based on Redis Enterprise, as the newer recommended option, and is moving customers there over time.

## 62: What is an Azure Virtual Network (VNet)?

A VNet is your private network in Azure. Resources inside it, such as VMs, can talk to each other with private IP addresses. You define an address space (for example `10.0.0.0/16`), split it into subnets, and control traffic with NSGs and route tables. A VNet lives in one region and one subscription.

```bash
az network vnet create -g rg-demo -n vnet-app \
  --address-prefix 10.0.0.0/16 \
  --subnet-name snet-web --subnet-prefix 10.0.1.0/24
```

## 63: What is a subnet?

A subnet is a range of IP addresses inside a VNet. You put resources with similar roles or security needs into the same subnet, like `snet-web`, `snet-app` and `snet-db`. Azure reserves 5 IP addresses in every subnet (the first four and the last one), so a `/24` gives you 251 usable addresses.

## 64: What is a Network Security Group (NSG)?

An NSG is a set of allow/deny rules that filter network traffic by source, destination, port and protocol. You attach it to a subnet or a network interface. Rules have a priority number from 100 to 4096; lower numbers are checked first and the first match wins. NSGs come with default rules, for example allowing traffic inside the VNet and denying all other inbound traffic.

## 65: What is a public IP address in Azure?

A public IP address is a resource you attach to a VM, load balancer, gateway or firewall so it can be reached from the internet. It can be static or dynamic. Use the **Standard** SKU, which is secure by default (closed until an NSG allows traffic) and supports availability zones. The Basic SKU was retired in September 2025.

## 66: What is Azure DNS?

Azure DNS hosts DNS zones on Microsoft's global name servers, so you can manage records like A, CNAME, MX and TXT with the same tools you use for other Azure resources. **Azure Private DNS** zones resolve names only inside linked VNets, which is used for private endpoints and internal services.

## 67: What is Azure Load Balancer?

Azure Load Balancer works at layer 4 (TCP/UDP). It spreads incoming traffic across healthy backend VMs or scale set instances using health probes. It can be public (internet-facing) or internal (private IP only). It is very fast and doesn't look at HTTP content, so it can't route by URL.

## 68: What is Azure Application Gateway?

Application Gateway is a regional layer 7 (HTTP/HTTPS) load balancer. It can route by URL path or host name, end TLS, rewrite headers, keep session affinity with cookies and include a **Web Application Firewall (WAF)** to block common attacks like SQL injection and XSS.

## 69: What is Azure Front Door?

Azure Front Door is a global layer 7 entry point that runs on Microsoft's edge network. It gives you a CDN, global HTTP load balancing across regions, TLS termination, caching, routing rules and WAF. It sends users to the closest healthy backend. It is the recommended replacement for the classic Azure CDN offerings.

## 70: What is Azure Traffic Manager?

Traffic Manager is a DNS-based traffic router. It answers DNS queries with the endpoint that best matches the routing method you choose: priority (failover), weighted, performance (lowest latency), geographic, multivalue or subnet. Because it only works at the DNS level, it doesn't see the actual traffic and failover speed depends on DNS TTL.

## 71: What is the difference between Load Balancer, Application Gateway, Front Door and Traffic Manager?

| Service             | Layer       | Scope    | Typical use                               |
| ------------------- | ----------- | -------- | ----------------------------------------- |
| Load Balancer       | 4 (TCP/UDP) | Regional | Non-HTTP traffic, internal load balancing |
| Application Gateway | 7 (HTTP)    | Regional | Web apps in one region, path routing, WAF |
| Front Door          | 7 (HTTP)    | Global   | Multi-region web apps, CDN, global WAF    |
| Traffic Manager     | DNS         | Global   | DNS failover, also for non-HTTP endpoints |

## 72: What is VNet peering?

VNet peering connects two VNets so their resources can talk with private IPs over Microsoft's backbone, as if they were on one network. Peering can be in the same region or across regions (global peering) and even across subscriptions and tenants. Address spaces must not overlap, and peering is not transitive by default.

## 73: What is a VPN Gateway?

A VPN Gateway sends encrypted traffic between an Azure VNet and another network over the public internet. It supports **site-to-site** (your office to Azure), **point-to-site** (single computers to Azure) and **VNet-to-VNet** connections. It is placed in a special subnet named `GatewaySubnet`.

## 74: What is ExpressRoute?

ExpressRoute is a private, dedicated connection between your on-premises network and Azure through a connectivity provider. Traffic does not go over the public internet, so you get more reliable speeds, lower latency and higher bandwidth than a VPN. It costs more and takes longer to set up.

## 75: What is Azure Bastion?

Azure Bastion lets you connect to VMs over RDP or SSH directly from the Azure portal or the native client, using TLS. The VMs don't need public IP addresses and you don't open ports 22 or 3389 to the internet. Bastion sits in a subnet named `AzureBastionSubnet`.

## 76: What is Azure Key Vault?

Key Vault is a service for storing and managing secrets (passwords, connection strings), cryptographic keys and TLS certificates. Apps read secrets at runtime using their managed identity instead of keeping them in code or config files. Access is controlled with Azure RBAC, and all access can be logged.

## 77: How do you read a secret from Key Vault in Node.js?

```js
const { DefaultAzureCredential } = require("@azure/identity");
const { SecretClient } = require("@azure/keyvault-secrets");

const client = new SecretClient(
  "https://my-vault.vault.azure.net",
  new DefaultAzureCredential(),
);

const secret = await client.getSecret("DbPassword");
console.log(secret.value);
```

The identity running the code needs the "Key Vault Secrets User" role on the vault.

## 78: What is Azure Monitor?

Azure Monitor is the main service for collecting and analyzing metrics, logs and traces from Azure resources, apps, VMs and on-premises machines. It includes Application Insights, Log Analytics, metrics explorer, alerts, workbooks and dashboards. Almost every Azure resource sends platform metrics to it automatically.

## 79: What is the difference between metrics and logs in Azure Monitor?

- **Metrics** are numbers collected at regular intervals, like CPU percentage or request count. They are lightweight, near real-time and good for alerts and charts.
- **Logs** are records with many fields, like a request log or an exception with a stack trace. They are stored in a Log Analytics workspace and queried with KQL, which makes them good for detailed troubleshooting.

## 80: What is Application Insights?

Application Insights is the application performance monitoring (APM) part of Azure Monitor. It collects requests, dependencies (calls to databases and APIs), exceptions, traces, page views and custom events from your app. It shows response times, failure rates and an application map of how your services call each other. New apps should use the Azure Monitor OpenTelemetry distro to send this data.

## 81: What is a Log Analytics workspace?

A Log Analytics workspace is where Azure Monitor stores log data. Resources send logs there through diagnostic settings, and Application Insights stores its data there too. You query the data with KQL, set retention, and control who can read it. Pricing depends mostly on how many GB you ingest.

## 82: What is KQL?

KQL (Kusto Query Language) is the read-only query language used in Log Analytics, Application Insights, Azure Data Explorer and Microsoft Sentinel. You start with a table and pipe the data through operators.

```kusto
AppRequests
| where TimeGenerated > ago(1h)
| where Success == false
| summarize count() by Name
| order by count_ desc
```

## 83: What are Azure Monitor alerts?

Alerts notify you or run an action when a condition is met. Types include **metric alerts** (for example CPU over 80% for 5 minutes), **log search alerts** (a KQL query returns results), **activity log alerts** (someone deleted a resource) and **service health alerts**. Alerts use **action groups** to send email, SMS, push notifications or call webhooks, Logic Apps and Functions.

## 84: What is Azure Service Bus?

Service Bus is an enterprise message broker. It offers **queues** (one sender, one receiver per message) and **topics with subscriptions** (publish/subscribe). It supports dead-letter queues, sessions for ordered processing, scheduled messages, duplicate detection and transactions. It is used to decouple services and handle work reliably.

## 85: What is Azure Event Grid?

Event Grid is an event routing service. Sources like Blob Storage, resource groups or your own apps publish events ("a blob was created"), and Event Grid pushes them to subscribers such as Functions, webhooks, Service Bus or Event Hubs. It supports filtering, retries and the CloudEvents schema. It is for reacting to things that happened, not for sending commands.

## 86: What is Azure Event Hubs?

Event Hubs is a big data streaming platform that can take in millions of events per second, such as telemetry, logs and clickstreams. Data is split into **partitions** and kept for a retention period, so many consumers can read the same stream at their own pace. It also has an Apache Kafka compatible endpoint.

## 87: When do you use Service Bus, Event Grid or Event Hubs?

- **Service Bus:** high-value business messages and commands, like "process this order", where each message must be handled reliably.
- **Event Grid:** lightweight notifications that something happened, like "a file was uploaded", delivered by push.
- **Event Hubs:** a large stream of events or telemetry for analytics, read by many consumers.

## 88: What is Azure Logic Apps?

Logic Apps is a low-code service for building automated workflows with a visual designer. A workflow starts from a trigger (like a new email, an HTTP call or a schedule) and runs actions using hundreds of built-in connectors for Office 365, Salesforce, SQL, SAP and more. It is often used for integrations between systems.

## 89: What is Azure API Management (APIM)?

API Management is a gateway that sits in front of your back-end APIs. It handles authentication, rate limiting, caching, request/response transformation, versioning and analytics through **policies**. It also has a developer portal where API consumers can read docs and get subscription keys.

## 90: What is Azure Static Web Apps?

Static Web Apps hosts static front ends (React, Angular, Vue, Next.js static export and so on) from a global network, with optional serverless APIs built on Azure Functions. It connects to GitHub or Azure DevOps and creates a CI/CD workflow, and every pull request gets its own preview environment. It also has built-in authentication.

## 91: What is an ARM template?

An ARM template is a JSON file that describes the Azure resources you want to deploy. It is declarative: you describe the end state and ARM works out how to create it. ARM templates are still supported, but writing them by hand is verbose, so most teams now write Bicep, which compiles to ARM JSON.

## 92: What is Bicep?

Bicep is Microsoft's language for infrastructure as code on Azure. It is shorter and easier to read than ARM JSON, has type checking and IntelliSense, and compiles down to an ARM template. It supports every Azure resource type and API version on the day it is released.

```bicep
param location string = resourceGroup().location

resource storage 'Microsoft.Storage/storageAccounts@2023-05-01' = {
  name: 'stshop${uniqueString(resourceGroup().id)}'
  location: location
  sku: { name: 'Standard_LRS' }
  kind: 'StorageV2'
}
```

## 93: How do you deploy a Bicep file?

```bash
az deployment group create \
  --resource-group rg-shop-dev \
  --template-file main.bicep \
  --parameters environment=dev
```

There are also `az deployment sub create`, `az deployment mg create` and `az deployment tenant create` for deployments at subscription, management group and tenant scope.

## 94: What is infrastructure as code (IaC) and why use it?

IaC means you define your infrastructure in files that are stored in git, instead of clicking through the portal. Benefits: environments are repeatable and consistent, changes are reviewed in pull requests, you have history and can roll back, and you can rebuild an environment quickly. On Azure the common tools are Bicep, Terraform, Pulumi and ARM templates.

## 95: What are tags in Azure?

Tags are name/value pairs that you attach to resources, resource groups and subscriptions, like `environment=prod` or `costCenter=1234`. They help with cost reports, automation and finding resources. Tags are not inherited by child resources automatically, but you can use Azure Policy to add or copy them.

```bash
az group update -n rg-shop-dev --tags environment=dev owner=team-shop
```

## 96: What are resource locks?

Resource locks prevent accidental changes. **CanNotDelete** allows changes but blocks deletion. **ReadOnly** blocks both changes and deletion. Locks apply to everyone, including Owners, and are inherited by child resources. You must remove the lock before you can do the blocked operation.

```bash
az lock create --name no-delete --lock-type CanNotDelete --resource-group rg-shop-prod
```

## 97: What is Azure Policy?

Azure Policy enforces rules on your resources, for example "only these regions are allowed", "storage accounts must not allow public access" or "every resource must have a costCenter tag". Policies are assigned at a scope and check resources when they are created or updated, and they also report on existing resources that don't comply.

## 98: What is the difference between Azure Policy and RBAC?

RBAC controls **who** can perform actions (for example, Alice can create VMs). Azure Policy controls **what** the resources can look like no matter who creates them (for example, VMs must be in West Europe and use approved sizes). You usually need both.

## 99: What is the Azure pricing calculator?

The pricing calculator is a website where you choose services, regions, sizes and expected usage to estimate monthly costs before you build anything. It helps compare options, for example Premium vs Standard App Service plans, or reserved vs pay-as-you-go VMs.

## 100: What is Microsoft Cost Management?

Cost Management shows what you are spending in Azure. You can break costs down by subscription, resource group, service or tag, see forecasts, set budgets with alerts, and export cost data to storage for reporting. It also shows recommendations from Azure Advisor for saving money.

## 101: What is an Azure budget?

A budget is a spending limit you set in Cost Management for a scope like a subscription or resource group. When actual or forecasted cost reaches a threshold (for example 80% or 100%), Azure sends emails or triggers an action group. A budget does not stop resources by itself; you have to automate that if you want it.

## 102: What are Azure Reservations?

A reservation is a 1-year or 3-year commitment to a specific resource type, like a VM size in a region or Azure SQL vCores. In return you get a big discount, up to about 72% compared to pay-as-you-go. They make sense for workloads that run all the time and won't change much.

## 103: What is an Azure savings plan for compute?

A savings plan is a commitment to spend a fixed amount per hour on compute for 1 or 3 years. The discount applies automatically across VMs, App Service, Functions Premium, Container Apps and other compute in any region. It is more flexible than reservations but the discount is usually a bit smaller.

## 104: What are Spot VMs?

Spot VMs use Azure's spare capacity at a large discount. Azure can evict them with 30 seconds notice when it needs the capacity back or when the price goes above your maximum. They are good for batch jobs, CI agents, rendering and other work that can be stopped and restarted, not for production web servers.

## 105: What is Azure Advisor?

Azure Advisor is a free service that looks at your resources and gives recommendations in five areas: reliability, security, performance, cost and operational excellence. Examples: "this VM is underused, resize it", "enable soft delete on this storage account" or "buy a reservation for these VMs".

## 106: What is Azure Service Health?

Service Health tells you about Azure problems that affect **your** resources: service issues (outages), planned maintenance, health advisories and security advisories. You can create service health alerts so your team gets notified. **Resource Health** shows the health of a single resource, for example if a VM is unavailable because of a platform problem.

## 107: What is an SLA in Azure?

A Service Level Agreement is Microsoft's promise for the uptime of a service, for example 99.95% or 99.99%, and the service credit you get if it is not met. The SLA often depends on configuration. For example, a single VM with Premium SSD has a lower SLA than VMs spread across availability zones.

## 108: How do you calculate the composite SLA of an app that uses several services?

If the app needs all services to work, multiply their SLAs. For example, App Service (99.95%) and Azure SQL (99.99%) give `0.9995 × 0.9999 ≈ 0.9994`, or about 99.94%. The combined SLA is always lower than the weakest part. Adding redundancy, like a second region, raises it.

## 109: What is Azure Marketplace?

Azure Marketplace is an online store with thousands of ready-made products from Microsoft and partners: VM images, SaaS apps, firewalls, databases and solution templates. You can deploy them into your subscription and often pay for them through your Azure bill.

## 110: What is Azure DevOps?

Azure DevOps is a set of developer services: **Boards** (work tracking), **Repos** (git), **Pipelines** (CI/CD), **Test Plans** and **Artifacts** (package feeds). It is often used with Azure, but works with any cloud. Many teams now use GitHub with GitHub Actions instead, which Microsoft also owns.

## 111: How do you deploy to Azure from GitHub Actions?

Use the `azure/login` action to sign in, then run CLI commands or a deploy action. The recommended login is OpenID Connect (OIDC) with a federated credential, so no secret is stored in GitHub.

```yaml
permissions:
  id-token: write
  contents: read

steps:
  - uses: actions/checkout@v4
  - uses: azure/login@v2
    with:
      client-id: ${{ secrets.AZURE_CLIENT_ID }}
      tenant-id: ${{ secrets.AZURE_TENANT_ID }}
      subscription-id: ${{ secrets.AZURE_SUBSCRIPTION_ID }}
  - run: az webapp deploy -g rg-shop -n my-shop-api --src-path app.zip
```

## 112: What is the Azure Developer CLI (azd)?

`azd` is a developer tool that takes a project from code to running in Azure with a few commands. A project has an `azure.yaml` file and infrastructure in Bicep or Terraform. `azd up` provisions resources and deploys code, `azd deploy` only deploys code, and `azd down` deletes everything. There are many ready-made templates.

```bash
azd init --template todo-nodejs-mongo
azd up
```

## 113: What is Microsoft Foundry?

Microsoft Foundry (formerly Azure AI Foundry, and before that Azure AI Studio) is Azure's platform for building generative AI apps and agents. It gives you access to models from OpenAI, Microsoft, Meta, Mistral, Anthropic and others, plus tools for prompt testing, evaluation, content safety, agents and deployment.

## 114: What is Azure OpenAI?

Azure OpenAI gives you access to OpenAI models (GPT, embeddings, image and audio models) running in Azure. You get the same models as OpenAI, but with Azure features: Entra ID authentication, private networking, regional data processing, content filtering and enterprise compliance. It is now part of Microsoft Foundry.

## 115: What are Azure AI services?

Azure AI services (formerly Cognitive Services) are prebuilt AI APIs you can call without training your own models. Examples: **Azure AI Vision** (image analysis, OCR), **Azure AI Speech** (speech-to-text, text-to-speech), **Azure AI Language** (sentiment, entity extraction), **Azure AI Translator**, **Azure AI Document Intelligence** (extract data from forms and invoices) and **Azure AI Search**.

## 116: What is Azure AI Search?

Azure AI Search (formerly Azure Cognitive Search) is a managed search service. It indexes your content and supports full-text search, filters, facets, vector search and hybrid search. It is commonly used as the retrieval part of RAG (retrieval-augmented generation) apps with large language models.

## 117: What is Microsoft Defender for Cloud?

Defender for Cloud is a security tool for Azure, other clouds and on-premises. It gives you a **secure score** with recommendations based on security benchmarks (posture management), and paid **Defender plans** that detect threats in servers, storage, databases, containers, Key Vault and more.

## 118: What is Microsoft Sentinel?

Sentinel is a cloud-native SIEM (security information and event management) and SOAR tool. It collects security data from Azure, Microsoft 365, other clouds, firewalls and more into a Log Analytics workspace, detects threats with analytics rules, and can run automated responses with playbooks built on Logic Apps.

## 119: What is Azure Arc?

Azure Arc lets you manage servers, Kubernetes clusters and databases that run outside Azure (on-premises or in other clouds) as if they were Azure resources. You can apply Azure Policy, RBAC, tags, Defender and Azure Monitor to them from the same place.

## 120: What is Azure Backup?

Azure Backup is a managed service for backing up VMs, SQL Server and SAP HANA in VMs, Azure Files, blobs, disks, PostgreSQL and on-premises machines. Backups are stored in a **Recovery Services vault** or **Backup vault**, with retention policies, soft delete and optional immutability to protect against ransomware.

## 121: What is Azure Site Recovery?

Site Recovery is a disaster recovery service. It continuously replicates VMs (Azure, VMware, Hyper-V or physical servers) to another Azure region, and lets you fail over when the primary site goes down and fail back later. You can run test failovers without touching production.

## 122: What is Azure Migrate?

Azure Migrate is a hub for planning and doing migrations to Azure. It can discover on-premises servers, databases and web apps, check if they are ready for Azure, estimate costs and right-size, then migrate VMs, databases and web apps with the right tools.

## 123: What is multi-factor authentication in Entra ID?

MFA requires a second proof of identity besides a password, such as the Microsoft Authenticator app, a FIDO2 security key, Windows Hello or a phone call. It blocks most account takeover attacks. In Entra ID it is usually required through Conditional Access policies or security defaults, and Azure now requires MFA for signing in to the portal and CLI.

## 124: What is Conditional Access?

Conditional Access is the Entra ID policy engine that decides if a sign-in is allowed, based on signals like who the user is, their location, device state, the app and the sign-in risk. Example policy: "require MFA for all admins" or "block access from outside these countries". It requires an Entra ID P1 or higher license.

## 125: What is Microsoft Entra External ID?

Entra External ID is the identity service for customer-facing apps (CIAM) and for partners. Users can sign up with email, social accounts like Google or Facebook, or their own company account. It is the successor of Azure AD B2C for new customers, though existing B2C tenants are still supported.

## 126: What is an app registration?

An app registration tells Entra ID about your application so it can sign users in or call APIs. It gives the app a **client ID**, redirect URIs, credentials (secret, certificate or federated credential), API permissions and exposed scopes. When you register an app, Entra ID also creates a service principal for it in your tenant.

## 127: What is a shared access signature (SAS)?

A SAS is a URL token that grants limited access to Azure Storage resources: which resource, which permissions (read, write, delete), and for how long. You give it to a client so it can upload or download a blob directly without having the account key.

```
https://myaccount.blob.core.windows.net/photos/cat.jpg?sv=2022-11-02&se=2026-11-01T10:00Z&sr=b&sp=r&sig=...
```

## 128: What are storage account access keys and why should you avoid them?

Each storage account has two access keys that give full access to all data in the account. If one leaks, the attacker can do anything. It is better to use Entra ID with RBAC roles and managed identities, and you can turn off shared key access on the account completely with `allowSharedKeyAccess: false`.

## 129: What are deployment slots in App Service?

Deployment slots are live copies of your app with their own host names, like `my-app-staging.azurewebsites.net`. You deploy a new version to the staging slot, test it and warm it up, then **swap** it with production. The swap is fast and has no downtime, and you can swap back if something goes wrong. Slots need the Standard tier or higher.

## 130: What are app settings in App Service?

App settings are key/value pairs that App Service passes to your app as environment variables. They are used for configuration like `NODE_ENV` or feature flags. Connection strings have their own section. Values are encrypted at rest, and you can reference Key Vault secrets instead of putting the secret value there.

```js
const apiUrl = process.env.PAYMENT_API_URL;
```

## 131: How do you add a custom domain and TLS to an App Service app?

1. Add a DNS record: a CNAME pointing to `<app>.azurewebsites.net` (or an A record plus a TXT record for verification).
2. Add the custom domain to the app in the portal or CLI.
3. Add a certificate: use the free **App Service managed certificate**, import one from Key Vault, or upload your own.
4. Bind the certificate to the domain with SNI SSL and turn on "HTTPS Only".

## 132: What is autoscale in Azure?

Autoscale automatically changes the number of instances based on rules. **Metric rules** scale out when, for example, average CPU is over 70% for 10 minutes. **Schedule rules** set a fixed count at certain times, like more instances during business hours. It works for VM scale sets, App Service plans and some other services. App Service also has **automatic scaling**, where the platform decides based on HTTP traffic.

## 133: What is Durable Functions?

Durable Functions is an extension of Azure Functions for writing stateful workflows in code. An **orchestrator function** calls **activity functions** and the framework saves progress, so a workflow can run for minutes or months, wait for events and survive restarts. Common patterns are function chaining, fan-out/fan-in, async HTTP APIs, human approval and monitoring.

## 134: What is Azure SignalR Service?

Azure SignalR Service is a managed service for adding real-time features like chat, live dashboards and notifications using ASP.NET Core SignalR. It handles the WebSocket connections at scale so your app servers don't have to. For other languages and raw WebSockets, **Azure Web PubSub** is the related service.

## 135: What is Azure Notification Hubs?

Notification Hubs is a push notification engine that sends notifications to mobile apps on iOS, Android, Windows and others through the platform push services (APNs, FCM). You can send to millions of devices at once and target users by tags.

## 136: What is Azure Communication Services?

Azure Communication Services gives you APIs for adding voice and video calling, chat, SMS, email and phone numbers to your apps. It's the same platform that powers Microsoft Teams, and it can also talk to Teams meetings.

## 137: What is Azure Data Factory?

Data Factory is a managed ETL and data integration service. You build pipelines that copy data from more than 90 sources (databases, files, SaaS apps) and transform it with data flows or by calling other services. Pipelines can run on a schedule or on events. The same engine is also part of Microsoft Fabric.

## 138: What is Microsoft Fabric?

Microsoft Fabric is an all-in-one analytics SaaS platform that combines data engineering, data warehousing, data science, real-time analytics and Power BI. All data is stored in **OneLake** in an open Delta Parquet format. Many new analytics projects use Fabric instead of building separate Synapse, Data Factory and Power BI setups.

## 139: What is Azure Databricks?

Azure Databricks is an Apache Spark-based analytics platform, built together by Databricks and Microsoft. It is used for big data processing, data engineering, machine learning and lakehouse architectures with Delta Lake, and it reads data from Data Lake Storage Gen2.

## 140: What is Azure Batch?

Azure Batch runs large-scale parallel and high-performance computing jobs. You define a pool of VMs, submit jobs made of many tasks, and Batch schedules them across the pool and scales it. It is used for rendering, simulations, financial modeling and media processing.

## 141: What is Azure Service Fabric?

Service Fabric is a distributed systems platform for running microservices and containers, including stateful services. Microsoft uses it internally for services like Azure SQL and Cosmos DB. For new projects most teams choose AKS or Container Apps, but you will still see Service Fabric in older enterprise systems.

## 142: What is Azure Virtual Desktop?

Azure Virtual Desktop is a service for running Windows desktops and apps in Azure and accessing them from any device. It supports Windows multi-session, so several users can share one VM. It's used for remote work, contractors and secure access to company apps.

## 143: What are Azure quotas and limits?

Each subscription has limits, like the number of vCPUs per VM family per region, the number of storage accounts, or public IPs. Some are hard limits, others (quotas) can be raised with a support request or from the Quotas page. If you hit a quota, deployments fail with errors like `QuotaExceeded`.

```bash
az vm list-usage --location westeurope --output table
```

## 144: What is the Azure activity log?

The activity log records control-plane events in a subscription: who created, changed or deleted which resource, and when. It also includes service health events and policy evaluations. It's kept for 90 days; to keep it longer or query it with KQL, send it to a Log Analytics workspace using a diagnostic setting.

## 145: What are diagnostic settings?

Diagnostic settings tell a resource where to send its resource logs and metrics: a Log Analytics workspace, a storage account, an event hub or a partner solution. Resource logs (like Key Vault access logs or App Service HTTP logs) are not collected until you create a diagnostic setting.

## 146: How do you log in to the Azure CLI in different situations?

```bash
az login                                  # interactive, opens a browser
az login --use-device-code                # when there's no browser
az login --identity                       # inside an Azure VM/container with a managed identity
az login --service-principal -u <appId> -p <secret> --tenant <tenantId>
```

In CI pipelines the recommended way is a federated credential (OIDC), handled by actions like `azure/login`.

## 147: What output formats does the Azure CLI support?

The `--output` (`-o`) flag supports `json` (default), `jsonc`, `table`, `tsv`, `yaml`, `yamlc` and `none`. `tsv` is useful in scripts because it gives plain values without quotes. You can filter results with `--query`, which uses JMESPath.

```bash
az webapp list --query "[].{name:name, state:state}" -o table
```

## 148: What is a resource ID?

A resource ID is the full unique path of a resource in Azure:

```
/subscriptions/<subscription-id>/resourceGroups/<rg>/providers/Microsoft.Web/sites/my-shop-api
```

You use it in role assignments, Bicep references, CLI commands with `--ids`, and the REST API. It includes the subscription, resource group, provider namespace, type and name.

## 149: What is Azure App Configuration?

App Configuration is a service for storing app settings and **feature flags** in one central place, separate from your code. Many apps and environments can read from it. It supports labels (for example per environment), versioning, Key Vault references and dynamic refresh, so you can change settings without redeploying.

## 150: What is the Microsoft Cloud Adoption Framework?

The Cloud Adoption Framework (CAF) is Microsoft's guidance for moving to and running in Azure. It covers strategy, planning, getting ready (landing zones), migrating, innovating, governance, security and management. It also has naming and tagging recommendations, like prefixes `rg-`, `vm-`, `st` and `kv-`.

# Moderate Questions (151-300)

## 151: How does DefaultAzureCredential work?

`DefaultAzureCredential` from `@azure/identity` tries a list of credential types in order and uses the first one that works. In the JavaScript SDK the order is: environment variables, workload identity, managed identity, then developer tools like Visual Studio Code, Azure CLI, Azure PowerShell and Azure Developer CLI. That means the same code works on your laptop (using your `az login`) and in Azure (using the managed identity).

```js
const { DefaultAzureCredential } = require("@azure/identity");
const { BlobServiceClient } = require("@azure/storage-blob");

const client = new BlobServiceClient(
  "https://stshop.blob.core.windows.net",
  new DefaultAzureCredential(),
);
```

## 152: Why might you not want DefaultAzureCredential in production?

Because it tries several credentials, startup can be slower, it can pick an unexpected identity, and failures are harder to debug. In production many teams use a specific credential like `ManagedIdentityCredential` (with the client ID of a user-assigned identity), or set the `AZURE_TOKEN_CREDENTIALS` environment variable to limit which credentials `DefaultAzureCredential` tries.

```js
const { ManagedIdentityCredential } = require("@azure/identity");
const credential = new ManagedIdentityCredential({
  clientId: process.env.AZURE_CLIENT_ID,
});
```

## 153: When do you choose a user-assigned managed identity over a system-assigned one?

Choose user-assigned when:

- several resources need the same permissions (for example 10 Function apps reading the same Key Vault),
- you want to set up role assignments **before** the resource exists, for example in IaC,
- resources are recreated often and you don't want to redo role assignments,
- you hit limits on how many role assignments you can create.

System-assigned is simpler when one resource needs its own identity and the identity should be removed with it.

## 154: How do you give an App Service app access to a storage account without keys?

1. Turn on a managed identity for the app.
2. Give that identity a data-plane role on the storage account, like "Storage Blob Data Contributor".
3. In code, use `DefaultAzureCredential` or `ManagedIdentityCredential` instead of a connection string.

```bash
az webapp identity assign -g rg-shop -n my-shop-api
principalId=$(az webapp identity show -g rg-shop -n my-shop-api --query principalId -o tsv)
az role assignment create --assignee $principalId \
  --role "Storage Blob Data Contributor" \
  --scope $(az storage account show -n stshop -g rg-shop --query id -o tsv)
```

## 155: What is the difference between the control plane and the data plane in Azure?

The **control plane** is used to manage resources and goes through ARM (`management.azure.com`), for example creating a storage account or changing its settings. The **data plane** is used to work with the data inside the resource, for example reading a blob or a Key Vault secret, and goes to the service endpoint directly. They have separate roles: "Contributor" on a storage account does not let you read blobs through Entra ID; you need "Storage Blob Data Reader" for that.

## 156: What are Key Vault references in App Service and Functions?

A Key Vault reference lets an app setting point to a secret in Key Vault instead of holding the value. The platform reads the secret using the app's managed identity and gives it to your code as a normal environment variable.

```
@Microsoft.KeyVault(SecretUri=https://kv-shop.vault.azure.net/secrets/DbPassword/)
```

If you leave out the version, the app picks up new versions automatically within about 24 hours, or right away after a restart or config change.

## 157: What is the difference between Key Vault access policies and Azure RBAC for Key Vault?

Access policies are the older model, set on each vault, that give permissions like "get secrets" to a principal. **Azure RBAC** is the recommended model: you use roles like "Key Vault Secrets User" or "Key Vault Administrator", assigned at any scope and managed like other Azure access, with support for PIM and audit. New vaults use RBAC by default.

## 158: What are soft delete and purge protection in Key Vault?

**Soft delete** keeps deleted vaults and secrets for a retention period (7 to 90 days) so you can recover them. It is always on for new vaults. **Purge protection** stops anyone, even an admin, from permanently deleting (purging) items during that retention period. Turn on purge protection for production vaults, especially when you use customer-managed keys.

## 159: How do deployment slot swaps work in App Service?

When you swap staging into production, App Service:

1. Applies the production slot's settings (the sticky ones) to the staging instances.
2. Warms up the staging instances by sending requests to the root or the path you set with `applicationInitialization`.
3. When the instances are ready, switches the routing so production traffic goes to them.

Because the switch happens only after warm-up, users don't see downtime. If problems appear, swap again to roll back.

## 160: What are slot settings (sticky settings)?

A slot setting stays with the slot and does not move during a swap. Use it for values that must differ per environment, like the production database connection string or a feature flag that should only be on in staging. Settings without this flag move with the app to the other slot.

```bash
az webapp config appsettings set -g rg-shop -n my-shop-api --slot staging \
  --slot-settings DB_NAME=shop_staging
```

## 161: What is swap with preview?

Swap with preview (multi-phase swap) does the first step of the swap, applying production settings to the staging slot, and then stops. You can test the staging slot with production settings before you finish the swap. If something is wrong, you cancel the swap and production is never touched.

## 162: What deployment methods does App Service support?

- **Zip deploy / `az webapp deploy`:** upload a package.
- **Run from package:** mount a zip file as read-only `wwwroot` (`WEBSITE_RUN_FROM_PACKAGE=1`).
- **Containers:** pull an image from ACR or another registry.
- **GitHub Actions / Azure Pipelines:** CI/CD.
- **Local git and FTP/S:** older options; FTP should be turned off.

```bash
az webapp deploy -g rg-shop -n my-shop-api --src-path ./dist/app.zip --type zip
```

## 163: What is the benefit of running from a package in App Service?

With `WEBSITE_RUN_FROM_PACKAGE`, the zip file is mounted as the read-only app folder instead of being extracted. Deployments are atomic (all files change at once), cold starts can be faster, rollback is easy, and you avoid file locking problems during deployment. The downside is that the app can't write to its own folder.

## 164: How do you see logs from an App Service app?

- Turn on **App Service logs** (application logging, web server logging) and stream them with `az webapp log tail`.
- Send logs to Log Analytics with diagnostic settings (`AppServiceConsoleLogs`, `AppServiceHTTPLogs`).
- Use Application Insights for requests, exceptions and traces.
- Use the **Kudu** site (`https://<app>.scm.azurewebsites.net`) or SSH to look at files and processes.

```bash
az webapp log tail -g rg-shop -n my-shop-api
```

## 165: What does the App Service health check feature do?

You set a path, like `/health`, and App Service pings it on every instance. If an instance keeps failing (by default after 10 failed pings), it is taken out of the load balancer, and if it stays unhealthy it gets replaced. It only works well when you run two or more instances. The health endpoint should check important dependencies but stay fast.

## 166: What does Always On do in App Service?

Without Always On, an app is unloaded after about 20 minutes with no traffic, so the next request has a slow start. Always On keeps the app loaded by sending regular requests. You need it for continuous WebJobs and for timer-triggered functions on an App Service plan. It is not available on the Free tier.

## 167: What is VNet integration for App Service?

VNet integration lets your app make **outbound** calls into a virtual network, for example to reach a database behind a private endpoint or a VM with a private IP. It uses a dedicated subnet delegated to `Microsoft.Web/serverFarms`. It does not make the app private for incoming traffic; for that you use a private endpoint or access restrictions.

## 168: What is the difference between service endpoints and private endpoints?

- **Service endpoints** extend your VNet identity to a PaaS service. Traffic goes over the Azure backbone and the service can allow only your subnet, but the service still has a public IP address.
- **Private endpoints** give the PaaS resource a private IP address inside your VNet. You can turn off public access completely, and you can reach it from peered VNets and on-premises.

Private endpoints are more secure and more flexible, but cost more and need private DNS setup.

## 169: Why do private endpoints need private DNS zones?

Clients still connect using the normal host name like `stshop.blob.core.windows.net`. Azure resolves that through a CNAME to `stshop.privatelink.blob.core.windows.net`. A private DNS zone named `privatelink.blob.core.windows.net` linked to your VNet returns the private IP. Without it, the name resolves to the public IP and the connection fails if public access is off.

## 170: How are NSG rules evaluated?

Rules are processed by priority, lowest number first, and processing stops at the first match. Inbound traffic is checked first against the subnet NSG and then the NIC NSG; outbound in the reverse order. Traffic must be allowed by both. Default rules (priority 65000 and up) allow VNet and load balancer traffic and deny everything else inbound.

```bash
az network nsg rule create -g rg-demo --nsg-name nsg-web -n allow-https \
  --priority 100 --direction Inbound --access Allow --protocol Tcp \
  --destination-port-ranges 443 --source-address-prefixes Internet
```

## 171: What are service tags?

Service tags are names for groups of IP address ranges of Azure services, like `Storage`, `AzureCloud`, `AzureFrontDoor.Backend`, `Sql.WestEurope` or `AzureMonitor`. Microsoft keeps the IP lists updated. You use them in NSG and firewall rules instead of maintaining IP lists by hand.

## 172: What are application security groups (ASGs)?

ASGs let you group VMs by role, like `asg-web` and `asg-db`, and use those groups in NSG rules instead of IP addresses. For example: "allow `asg-web` to talk to `asg-db` on port 5432". When you add a new VM, you only attach its NIC to the right ASG.

## 173: What are user-defined routes (UDRs)?

Azure has system routes that send traffic within the VNet, to peered VNets and to the internet. A **route table** with user-defined routes overrides them. A common case is sending all outbound traffic (`0.0.0.0/0`) through Azure Firewall or a network virtual appliance for inspection. You attach a route table to a subnet.

## 174: What is a NAT gateway and why use one?

A NAT gateway gives a subnet a fixed set of public IPs for outbound internet traffic. It scales to many connections, avoids SNAT port exhaustion and gives you static outbound IPs that partners can allowlist. Since new VNets now create private subnets by default (no implicit outbound access), NAT gateway is the usual way to give them internet egress.

## 175: What changed with default outbound access for VMs?

In the past, a VM without a public IP or load balancer still got internet access through a hidden Microsoft IP. Microsoft is retiring this: newly created VNets (with newer API versions) now have private subnets by default. VMs in them need an explicit outbound method: NAT gateway, a public IP, load balancer outbound rules or a firewall. Existing VNets keep the old behavior.

## 176: What is a hub-and-spoke network topology?

A **hub** VNet holds shared services like Azure Firewall, VPN or ExpressRoute gateways, Bastion and DNS. **Spoke** VNets hold workloads and are peered to the hub. Spokes usually reach each other and on-premises through the hub, which gives you one place to inspect and control traffic. Azure Virtual WAN is a managed version of this design.

## 177: How do you write a Bicep module and use it?

A module is just another Bicep file that you call from a parent file.

```bicep
// modules/storage.bicep
param name string
param location string

resource sa 'Microsoft.Storage/storageAccounts@2023-05-01' = {
  name: name
  location: location
  sku: { name: 'Standard_ZRS' }
  kind: 'StorageV2'
  properties: { minimumTlsVersion: 'TLS1_2', allowBlobPublicAccess: false }
}

output id string = sa.id
```

```bicep
// main.bicep
module storage 'modules/storage.bicep' = {
  name: 'storage'
  params: { name: 'stshopdev01', location: resourceGroup().location }
}

output storageId string = storage.outputs.id
```

## 178: What is a .bicepparam file?

A `.bicepparam` file holds parameter values for a Bicep file, written in Bicep syntax with type checking. It replaces JSON parameter files. You can also read values from Key Vault with `getSecret()`.

```bicep
using './main.bicep'

param environment = 'prod'
param location = 'westeurope'
param skuName = 'P1v3'
```

```bash
az deployment group create -g rg-shop-prod --parameters main.prod.bicepparam
```

## 179: What does the what-if operation do?

`what-if` shows the changes a deployment would make, like resources that would be created, modified or deleted, without actually deploying. It works like `terraform plan` and is a good step to run in pull requests.

```bash
az deployment group what-if -g rg-shop-prod --template-file main.bicep --parameters main.prod.bicepparam
```

## 180: What is the difference between incremental and complete deployment modes?

- **Incremental (default):** resources in the template are created or updated; resources in the resource group that are not in the template are left alone.
- **Complete:** resources in the resource group that are not in the template are **deleted**.

Complete mode is risky. For managing the full lifecycle of a set of resources, deployment stacks are now the recommended option.

## 181: What are deployment stacks?

A deployment stack is a Bicep/ARM deployment that Azure tracks as one unit of managed resources. When you update the stack and a resource is no longer in the template, the stack can delete it or detach it (you choose with `--action-on-unmanage`). Stacks can also add **deny settings** so nobody can change or delete the managed resources outside the stack.

```bash
az stack group create --name shop-stack -g rg-shop \
  --template-file main.bicep \
  --action-on-unmanage deleteResources \
  --deny-settings-mode denyDelete
```

## 182: How do you use existing resources in Bicep?

Use the `existing` keyword to reference a resource you don't deploy in this file, so you can read its properties or use it as a scope.

```bicep
resource kv 'Microsoft.KeyVault/vaults@2023-07-01' existing = {
  name: 'kv-shop-prod'
}

output vaultUri string = kv.properties.vaultUri
```

## 183: How do you create a role assignment in Bicep?

Role assignment names must be GUIDs, so use `guid()` with stable inputs to keep it the same across deployments.

```bicep
param principalId string

resource sa 'Microsoft.Storage/storageAccounts@2023-05-01' existing = {
  name: 'stshopprod'
}

var blobDataContributor = 'ba92f5b4-2d11-453d-a403-e96b0029c9fe'

resource ra 'Microsoft.Authorization/roleAssignments@2022-04-01' = {
  name: guid(sa.id, principalId, blobDataContributor)
  scope: sa
  properties: {
    principalId: principalId
    principalType: 'ServicePrincipal'
    roleDefinitionId: subscriptionResourceId('Microsoft.Authorization/roleDefinitions', blobDataContributor)
  }
}
```

## 184: How does Terraform work with Azure?

Terraform uses the `azurerm` provider for ARM resources, `azuread` for Entra ID objects and `azapi` for any ARM API (including preview features). State is usually stored in a Blob Storage container, with blob leases used for locking.

```hcl
terraform {
  backend "azurerm" {
    resource_group_name  = "rg-tfstate"
    storage_account_name = "sttfstate001"
    container_name       = "tfstate"
    key                  = "shop/prod.tfstate"
    use_azuread_auth     = true
  }
}

provider "azurerm" {
  features {}
}
```

## 185: Bicep or Terraform: how do you choose?

- **Bicep:** Azure only, no state file to manage (Azure is the state), new resource types supported on day one, free, simple for Azure-focused teams.
- **Terraform:** works with many clouds and SaaS (GitHub, Datadog, Cloudflare), big community, has a plan/state model, but you must manage and protect state.

If the company is only on Azure, Bicep is often simpler. If it uses many providers, Terraform gives one tool for everything.

## 186: How do you set up OIDC (workload identity federation) for GitHub Actions?

1. Create an app registration (or a user-assigned managed identity).
2. Add a **federated credential** that trusts GitHub's token issuer for your repo and branch/environment.
3. Assign it RBAC roles on the target scope.
4. In the workflow, give the job `id-token: write` and use `azure/login` with client ID, tenant ID and subscription ID.

```bash
az ad app federated-credential create --id <appObjectId> --parameters '{
  "name": "github-main",
  "issuer": "https://token.actions.githubusercontent.com",
  "subject": "repo:my-org/shop:ref:refs/heads/main",
  "audiences": ["api://AzureADTokenExchange"]
}'
```

No client secret is stored, and the GitHub token is valid only for a short time.

## 187: How do you build and push images to ACR in CI?

You can use `az acr build`, which builds the image in Azure (no Docker needed on the agent), or log in and use Docker.

```bash
az acr login --name myregistry123
docker build -t myregistry123.azurecr.io/shop-api:${GITHUB_SHA} .
docker push myregistry123.azurecr.io/shop-api:${GITHUB_SHA}
```

Tag images with the commit SHA, not just `latest`, so you know exactly what is deployed and can roll back.

## 188: How does AKS pull images from ACR?

The simplest way is to attach the registry to the cluster. This gives the kubelet managed identity the `AcrPull` role on the registry.

```bash
az aks update -g rg-aks -n aks-shop --attach-acr myregistry123
```

You don't need image pull secrets. Container Apps and App Service work the same way with a managed identity that has `AcrPull`.

## 189: What are revisions in Azure Container Apps?

A revision is an immutable snapshot of a container app's version. A new revision is created when you change revision-scope settings like the image, env vars or scale rules. In **single revision mode** the new revision replaces the old one. In **multiple revision mode** you can run several at once and split traffic between them.

## 190: How do you split traffic between revisions in Container Apps?

```bash
az containerapp revision set-mode -g rg-shop -n shop-api --mode multiple

az containerapp ingress traffic set -g rg-shop -n shop-api \
  --revision-weight shop-api--v1=80 shop-api--v2=20
```

This is used for blue-green and canary releases. You can also give revisions labels, which get their own URL for testing before sending real traffic.

## 191: How does scaling work in Azure Container Apps?

Container Apps uses KEDA. You set min and max replicas and one or more scale rules: HTTP (concurrent requests), TCP, CPU/memory, or event-based rules like Service Bus queue length, Event Hubs, Kafka, Redis and many more KEDA scalers. With `minReplicas: 0` the app scales to zero and you pay nothing for compute when idle.

```bash
az containerapp update -g rg-shop -n order-worker \
  --min-replicas 0 --max-replicas 20 \
  --scale-rule-name sb-queue --scale-rule-type azure-servicebus \
  --scale-rule-metadata queueName=orders namespace=sb-shop messageCount=10 \
  --scale-rule-identity system
```

## 192: What is the difference between a container app and a Container Apps job?

A **container app** runs all the time (or scales to zero) and usually serves HTTP or processes events continuously. A **job** runs a container until it finishes and then stops. Jobs can be triggered manually, on a schedule (cron), or by events like messages in a queue. Use jobs for batch processing, migrations and scheduled tasks.

## 193: What is Dapr and how is it used in Container Apps?

Dapr (Distributed Application Runtime) is a sidecar that gives microservices building blocks through simple HTTP/gRPC APIs: service invocation, state management, pub/sub, bindings, secrets and actors. In Container Apps you turn it on per app, and you configure components (like a Service Bus pub/sub or Cosmos DB state store) at the environment level. Your code stays the same if you change the underlying service.

## 194: What is a Container Apps environment?

An environment is the secure boundary around a group of container apps and jobs. Apps in the same environment share a virtual network, Log Analytics workspace and Dapr setup, and can call each other by name. You can choose a **Consumption** profile (serverless) or **Dedicated** workload profiles (reserved hardware, including GPU).

## 195: How do output bindings work in Azure Functions with Node.js v4?

You define the binding with the `output` helpers and set its value with `context.extraOutputs` or by returning it.

```js
const { app, output } = require("@azure/functions");

const queueOutput = output.storageQueue({
  queueName: "orders",
  connection: "AzureWebJobsStorage",
});

app.http("createOrder", {
  methods: ["POST"],
  extraOutputs: [queueOutput],
  handler: async (request, context) => {
    const order = await request.json();
    context.extraOutputs.set(queueOutput, order);
    return { status: 202, jsonBody: { accepted: true } };
  },
});
```

## 196: How does a Service Bus trigger work in Azure Functions?

The Functions host receives messages for you in peek-lock mode. If the function finishes without error, the message is completed. If it throws, the message is abandoned and retried until it hits the max delivery count, then it goes to the dead-letter queue.

```js
const { app } = require("@azure/functions");

app.serviceBusQueue("processOrder", {
  connection: "ServiceBusConnection",
  queueName: "orders",
  handler: async (message, context) => {
    context.log("Order", message.orderId);
    context.log("Delivery count", context.triggerMetadata.deliveryCount);
  },
});
```

## 197: How do you connect a function trigger to a service with a managed identity instead of a connection string?

Use identity-based connections. Instead of a connection string setting, you set app settings with the same prefix and a `__fullyQualifiedNamespace` or `__serviceUri` suffix. The Functions host then uses the app's managed identity.

```
ServiceBusConnection__fullyQualifiedNamespace = sb-shop.servicebus.windows.net
AzureWebJobsStorage__accountName = stshopfunc
```

The identity also needs the right data roles, like "Azure Service Bus Data Receiver".

## 198: What is the Flex Consumption plan and how is it different from the old Consumption plan?

Flex Consumption is the newer serverless plan for Azure Functions on Linux. Compared to the Consumption plan it adds VNet integration, faster scaling, per-function scaling, a choice of instance memory sizes, configurable concurrency and optional **always ready** instances to cut cold starts. Deployment packages live in a blob container. Linux Consumption is retiring (no new features, ends September 30, 2028), so new Linux apps should use Flex Consumption.

```bash
az functionapp create -g rg-shop -n func-shop \
  --storage-account stshopfunc \
  --flex-consumption-location westeurope \
  --runtime node --runtime-version 22
```

## 199: What is host.json in Azure Functions?

`host.json` holds settings for the whole function app: logging levels and sampling, extension settings (like Service Bus `maxConcurrentCalls`, queue batch size), function timeout and retries. It applies to every function in the app.

```json
{
  "version": "2.0",
  "logging": {
    "applicationInsights": {
      "samplingSettings": { "isEnabled": true, "excludedTypes": "Request" }
    }
  },
  "extensions": {
    "serviceBus": { "maxConcurrentCalls": 16 }
  }
}
```

## 200: How do you run Azure Functions locally?

Install Azure Functions Core Tools and run `func start`. Local settings go in `local.settings.json` (which should not be committed). For storage you can use the **Azurite** emulator.

```bash
npm install -g azure-functions-core-tools@4
func init my-funcs --javascript
func new --name hello --template "HTTP trigger"
func start
```

## 201: What are the main Durable Functions patterns?

- **Function chaining:** call activities one after another, passing output to the next.
- **Fan-out/fan-in:** start many activities in parallel and wait for all of them.
- **Async HTTP API:** start a long job and give the caller a status URL to poll.
- **Monitor:** a loop that checks something on a schedule until a condition is met.
- **Human interaction:** wait for an external event, like an approval, with a timeout.
- **Aggregator (entities):** durable entities that hold small pieces of state.

## 202: Show a fan-out/fan-in orchestration in Node.js.

```js
const df = require("durable-functions");

df.app.orchestration("resizeAll", function* (context) {
  const images = yield context.df.callActivity("listImages");
  const tasks = images.map((img) => context.df.callActivity("resize", img));
  const results = yield context.df.Task.all(tasks);
  return results.length;
});

df.app.activity("listImages", { handler: async () => ["a.jpg", "b.jpg"] });
df.app.activity("resize", { handler: async (img) => `${img} done` });
```

The orchestrator uses a generator function and `yield` so the framework can save progress and replay it.

## 203: What is the difference between Service Bus queues and topics?

A **queue** delivers each message to one receiver; several receivers compete for messages (competing consumers). A **topic** delivers a copy of each message to every **subscription**, and each subscription works like its own queue. Subscriptions can have filters (SQL or correlation filters) so they only get the messages they care about.

## 204: What are peek-lock and receive-and-delete in Service Bus?

- **Peek-lock (default):** the receiver gets the message and it is locked for a period (lock duration). The receiver must complete it after processing. If it doesn't, the lock expires and the message becomes available again. This gives at-least-once delivery.
- **Receive-and-delete:** the message is removed as soon as it is received. Faster, but if the receiver crashes the message is lost (at-most-once).

## 205: What is the dead-letter queue in Service Bus?

Every queue and topic subscription has a dead-letter sub-queue. Messages go there when they exceed the max delivery count, expire (if dead-lettering on expiry is on), fail filter evaluation, or when your code dead-letters them on purpose. Dead-lettered messages stay until you read them, so you should monitor and process this queue.

```js
await receiver.deadLetterMessage(message, {
  deadLetterReason: "InvalidPayload",
  deadLetterErrorDescription: "Missing customerId",
});
```

## 206: How do you send and receive Service Bus messages in Node.js?

```js
const { ServiceBusClient } = require("@azure/service-bus");
const { DefaultAzureCredential } = require("@azure/identity");

const client = new ServiceBusClient(
  "sb-shop.servicebus.windows.net",
  new DefaultAzureCredential(),
);

const sender = client.createSender("orders");
await sender.sendMessages({ body: { orderId: 42 }, messageId: "order-42" });

const receiver = client.createReceiver("orders");
receiver.subscribe({
  processMessage: async (msg) => {
    console.log(msg.body);
    // completed automatically when this resolves (autoCompleteMessages defaults to true)
  },
  processError: async (err) => console.error(err.error),
});
```

## 207: What are Service Bus sessions?

Sessions group related messages by `sessionId`, for example all messages for one order. One receiver locks a session and gets its messages in FIFO order, while other receivers handle other sessions in parallel. Use sessions when you need ordered processing per entity. The queue or subscription must be created with sessions enabled.

## 208: What is duplicate detection in Service Bus?

When duplicate detection is on, Service Bus remembers the `messageId` of messages for a time window (up to 7 days). If a sender retries and sends a message with the same `messageId`, Service Bus drops the copy. It protects against duplicates caused by sender retries, but your receivers should still be idempotent.

## 209: How do you schedule a message in Service Bus?

You can set `scheduledEnqueueTimeUtc` on the message or call `scheduleMessages`. The message is stored but not visible to receivers until that time. You can cancel it with the returned sequence number.

```js
const at = new Date(Date.now() + 30 * 60 * 1000);
const [seq] = await sender.scheduleMessages({ body: { remind: "user-7" } }, at);
// later: await sender.cancelScheduledMessages(seq);
```

## 210: What is the difference between Service Bus Standard and Premium tiers?

- **Standard:** shared resources, pay per operation, message size up to 256 KB, variable throughput.
- **Premium:** dedicated resources (messaging units), predictable performance, messages up to 100 MB, VNet integration and private endpoints, availability zones, geo-replication, and customer-managed keys.

Production systems with steady load or strict network rules usually need Premium.

## 211: How does Event Grid deliver events and handle failures?

Event Grid pushes events to the subscriber and expects a success response. If delivery fails, it retries with exponential backoff for up to 24 hours (or the max attempts you set, up to 30). After that it can send the event to a **dead-letter** blob container if you configured one. Delivery is at-least-once, so handlers must be idempotent.

## 212: What are Event Grid system topics, custom topics and namespaces?

- **System topics:** events from Azure services, like Blob Storage, resource groups or Key Vault.
- **Custom topics:** your own apps publish events over HTTP.
- **Event Grid namespaces:** a newer resource that supports pull delivery (consumers fetch events), MQTT for IoT devices, and push delivery to Event Hubs and webhooks.

## 213: How do you filter Event Grid events?

On an event subscription you can filter by **event type** (like `Microsoft.Storage.BlobCreated`), by **subject** prefix/suffix (like `/blobServices/default/containers/uploads/` and `.jpg`), and with **advanced filters** on fields in the event data (like `data.contentLength > 1000`).

```bash
az eventgrid event-subscription create --name images-to-func \
  --source-resource-id $(az storage account show -n stshop -g rg-shop --query id -o tsv) \
  --endpoint-type azurefunction --endpoint <function-resource-id> \
  --included-event-types Microsoft.Storage.BlobCreated \
  --subject-ends-with .jpg
```

## 214: What is the CloudEvents schema and why use it?

CloudEvents is an open CNCF standard for describing event data with common fields like `id`, `source`, `type`, `time` and `data`. Event Grid supports both its own schema and CloudEvents 1.0. Using CloudEvents makes events portable between clouds and tools.

## 215: What are partitions and consumer groups in Event Hubs?

- **Partitions** are ordered logs inside an event hub. Events with the same partition key go to the same partition, so their order is kept. More partitions allow more parallel consumers.
- **Consumer groups** are separate views of the whole event hub. Each consumer group reads the stream independently with its own position, for example one group for real-time alerts and one for archiving.

## 216: What is checkpointing in Event Hubs?

Consumers save their position (offset) in each partition to a store, usually Blob Storage. This is checkpointing. If a consumer restarts or a partition moves to another instance, it continues from the last checkpoint. Events after the last checkpoint can be processed again, so processing must be idempotent.

```js
const { EventHubConsumerClient } = require("@azure/event-hubs");
const { ContainerClient } = require("@azure/storage-blob");
const {
  BlobCheckpointStore,
} = require("@azure/eventhubs-checkpointstore-blob");
const { DefaultAzureCredential } = require("@azure/identity");

const credential = new DefaultAzureCredential();
const container = new ContainerClient(
  "https://stshop.blob.core.windows.net/checkpoints",
  credential,
);
const consumer = new EventHubConsumerClient(
  "$Default",
  "eh-shop.servicebus.windows.net",
  "telemetry",
  credential,
  new BlobCheckpointStore(container),
);

consumer.subscribe({
  processEvents: async (events, context) => {
    if (events.length === 0) return;
    // handle events...
    await context.updateCheckpoint(events[events.length - 1]);
  },
  processError: async (err) => console.error(err),
});
```

## 217: Can you use Kafka clients with Event Hubs?

Yes. Event Hubs (Standard tier and above) has a Kafka-compatible endpoint on port 9093. Existing Kafka producers and consumers can connect by changing the bootstrap server and authentication (SASL with a connection string, or OAuth with Entra ID). An event hubs namespace maps to a Kafka cluster and an event hub maps to a topic. Some Kafka features, like Kafka Streams on lower tiers, are limited.

## 218: What is Event Hubs Capture?

Capture automatically saves the data from an event hub to Blob Storage or Data Lake Storage in Avro or Parquet format, based on a time or size window. You get a raw archive of all events for batch analytics without writing any consumer code.

## 219: What types of SAS tokens exist and which is the safest?

- **Account SAS:** signed with the account key, can cover several services.
- **Service SAS:** signed with the account key, for one service (blob, queue, table or files).
- **User delegation SAS:** signed with Entra ID credentials through a user delegation key. Blob and Data Lake only.

User delegation SAS is the safest, because it doesn't use the account key, it can be revoked by revoking the delegation keys, and it is tied to an identity for auditing.

## 220: How do you create a user delegation SAS in Node.js so a browser can upload a file directly?

```js
const {
  BlobServiceClient,
  generateBlobSASQueryParameters,
  BlobSASPermissions,
} = require("@azure/storage-blob");
const { DefaultAzureCredential } = require("@azure/identity");

const account = "stshop";
const service = new BlobServiceClient(
  `https://${account}.blob.core.windows.net`,
  new DefaultAzureCredential(),
);

async function getUploadUrl(blobName) {
  const startsOn = new Date();
  const expiresOn = new Date(startsOn.getTime() + 10 * 60 * 1000);
  const key = await service.getUserDelegationKey(startsOn, expiresOn);

  const sas = generateBlobSASQueryParameters(
    {
      containerName: "uploads",
      blobName,
      permissions: BlobSASPermissions.parse("cw"),
      startsOn,
      expiresOn,
    },
    key,
    account,
  ).toString();

  return `https://${account}.blob.core.windows.net/uploads/${blobName}?${sas}`;
}
```

The API's identity needs a role that includes the `generateUserDelegationKey` action, like "Storage Blob Delegator" or "Storage Blob Data Contributor".

## 221: What is blob lifecycle management?

Lifecycle management policies move or delete blobs automatically based on age or last access. For example: move to Cool after 30 days, to Archive after 180 days, delete after 7 years. Rules can target containers or name prefixes and blob index tags. It saves money without any custom scripts.

```json
{
  "rules": [
    {
      "name": "logs-retention",
      "enabled": true,
      "type": "Lifecycle",
      "definition": {
        "filters": { "blobTypes": ["blockBlob"], "prefixMatch": ["logs/"] },
        "actions": {
          "baseBlob": {
            "tierToCool": { "daysAfterModificationGreaterThan": 30 },
            "tierToArchive": { "daysAfterModificationGreaterThan": 180 },
            "delete": { "daysAfterModificationGreaterThan": 2555 }
          }
        }
      }
    }
  ]
}
```

## 222: What data protection features does Blob Storage have?

- **Soft delete** for blobs and containers: recover deleted data during a retention period.
- **Versioning:** every change keeps the previous version.
- **Point-in-time restore:** restore block blobs to an earlier state.
- **Snapshots:** read-only copies at a point in time.
- **Immutable storage (WORM):** time-based retention or legal holds that block changes and deletes.
- **Resource locks** on the account to block deletion of the account itself.

## 223: How do you host a static website in Azure Storage?

Turn on the static website feature. It creates a special `$web` container and gives you an endpoint like `https://<account>.z6.web.core.windows.net`. Upload your built files there. For custom domains with HTTPS and caching, put Azure Front Door in front of it. For apps that need APIs, auth and preview environments, Static Web Apps is usually a better fit.

```bash
az storage blob service-properties update --account-name stsite --static-website \
  --index-document index.html --404-document index.html
az storage blob upload-batch --account-name stsite -s ./dist -d '$web' --auth-mode login
```

## 224: How do you configure CORS for Blob Storage?

If a browser app on another domain calls Blob Storage directly (for example uploading with a SAS URL), you must add a CORS rule on the Blob service.

```bash
az storage cors add --account-name stshop --services b \
  --methods GET PUT OPTIONS --origins https://shop.example.com \
  --allowed-headers "*" --exposed-headers "*" --max-age 3600
```

## 225: What is AzCopy?

AzCopy is a command-line tool for copying data to, from and between storage accounts. It is fast because it transfers in parallel, and it can copy server-to-server without downloading. It supports Entra ID login and SAS tokens.

```bash
azcopy login
azcopy copy "./backups/*" "https://stshop.blob.core.windows.net/backups" --recursive
azcopy sync "./site" "https://stsite.blob.core.windows.net/\$web" --delete-destination=true
```

## 226: How do you upload a large file to Blob Storage efficiently from Node.js?

Use `uploadFile` or `uploadStream` on a `BlockBlobClient`. The SDK splits the file into blocks and uploads them in parallel, then commits the block list.

```js
const blockBlob = containerClient.getBlockBlobClient("videos/intro.mp4");
await blockBlob.uploadFile("./intro.mp4", {
  blockSize: 8 * 1024 * 1024, // 8 MB blocks
  concurrency: 8,
  blobHTTPHeaders: { blobContentType: "video/mp4" },
});
```

## 227: How do you choose a partition key in Cosmos DB?

A good partition key:

- has **many distinct values** (high cardinality), like `userId` or `tenantId`,
- spreads **requests and storage evenly**, so there are no hot partitions,
- is used in most queries, so queries hit one partition.

Bad choices are things like `country` or `status` with few values. The partition key can't be changed after the container is created without moving the data. If no single property works, use a synthetic key or hierarchical partition keys.

## 228: What are the Cosmos DB consistency levels?

From strongest to weakest:

1. **Strong:** reads always return the latest committed write.
2. **Bounded staleness:** reads can lag by at most K versions or T time.
3. **Session (default):** within one client session you read your own writes; others may see older data.
4. **Consistent prefix:** you never see writes out of order.
5. **Eventual:** no ordering guarantee, cheapest and fastest.

Stronger levels cost more RUs for reads and add latency in multi-region setups.

## 229: What are the Cosmos DB throughput options?

- **Provisioned (manual):** you set a fixed RU/s. Cheapest for steady traffic.
- **Autoscale:** you set a max RU/s and Cosmos scales between 10% and 100% of it. Good for variable traffic.
- **Serverless:** pay per RU used, no minimum. Good for dev/test and low or spiky traffic, with some limits on size and features.

Throughput can be set per container or shared at database level.

## 230: How do you query Cosmos DB from Node.js?

```js
const { CosmosClient } = require("@azure/cosmos");
const { DefaultAzureCredential } = require("@azure/identity");

const client = new CosmosClient({
  endpoint: "https://cosmos-shop.documents.azure.com",
  aadCredentials: new DefaultAzureCredential(),
});
const container = client.database("shop").container("orders");

const { resources } = await container.items
  .query(
    {
      query: "SELECT * FROM c WHERE c.customerId = @id AND c.status = @status",
      parameters: [
        { name: "@id", value: "cust-1" },
        { name: "@status", value: "paid" },
      ],
    },
    { partitionKey: "cust-1" },
  )
  .fetchAll();
```

Use parameters instead of string building to avoid injection and allow plan caching. Passing the partition key keeps the query on one partition.

## 231: What is the Cosmos DB change feed?

The change feed is an ordered log of inserts and updates in a container, per partition key range. You use it to react to changes: update a search index, build materialized views, send events or sync to another store. You can read it with the Azure Functions Cosmos DB trigger, the change feed processor in the SDK, or the pull model. By default it does not include deletes; use soft delete with TTL or the "all versions and deletes" mode.

## 232: What is TTL in Cosmos DB?

Time to live automatically deletes items after a number of seconds. You set a default TTL on the container and can override it per item with the `ttl` property. Deletion uses spare RUs, so it doesn't use your provisioned throughput directly. It's useful for sessions, caches, temporary data and logs.

## 233: How does indexing work in Cosmos DB?

By default Cosmos DB indexes every property of every item. That makes any query fast but makes writes more expensive in RUs. You can change the **indexing policy** to include only the paths you query, exclude large properties, and add **composite indexes** for `ORDER BY` on several fields or for filters plus sort. There are also spatial and vector indexes.

```json
{
  "indexingMode": "consistent",
  "includedPaths": [{ "path": "/customerId/?" }, { "path": "/createdAt/?" }],
  "excludedPaths": [{ "path": "/*" }],
  "compositeIndexes": [
    [
      { "path": "/customerId", "order": "ascending" },
      { "path": "/createdAt", "order": "descending" }
    ]
  ]
}
```

## 234: What is the difference between the DTU and vCore models in Azure SQL Database?

- **DTU:** a bundled measure of CPU, memory and IO. Simple tiers: Basic, Standard, Premium. Hard to compare with on-premises servers.
- **vCore:** you choose vCores, memory and storage separately in the General Purpose, Business Critical or Hyperscale tiers. You can use Azure Hybrid Benefit with existing SQL Server licenses and get reservations.

The vCore model is recommended for most new databases because it is more flexible and clear.

## 235: What is serverless compute in Azure SQL Database?

Serverless is a vCore compute tier that scales vCores automatically between a min and max based on load, and bills per second for the compute used. It can **auto-pause** after a period without activity, so you pay only for storage. The first connection after a pause takes some time while the database resumes. Good for dev/test and apps with unpredictable or rare use.

## 236: What is an elastic pool?

An elastic pool is a group of Azure SQL databases that share a set of resources (eDTUs or vCores). It is good for multi-tenant SaaS apps where each customer has their own database and their usage peaks at different times. You pay for the pool instead of sizing each database for its peak.

## 237: How do you connect a Node.js app to Azure SQL with Entra ID instead of a password?

Use the `mssql`/`tedious` driver with a token-based authentication type.

```js
const sql = require("mssql");

const pool = await sql.connect({
  server: "sql-shop.database.windows.net",
  database: "shop",
  options: { encrypt: true },
  authentication: {
    type: "azure-active-directory-default",
    options: { clientId: process.env.AZURE_CLIENT_ID }, // only for user-assigned identity
  },
});

const result = await pool.request().query("SELECT TOP 5 * FROM Orders");
```

In the database, create a user for the identity: `CREATE USER [my-shop-api] FROM EXTERNAL PROVIDER;` and give it roles like `db_datareader`.

## 238: What is the difference between active geo-replication and failover groups in Azure SQL?

**Active geo-replication** creates readable secondary databases in other regions, up to four, and you fail over each database by hand. **Failover groups** manage a group of databases together, give you listener endpoints (`<group>.database.windows.net` for read-write and `<group>.secondary.database.windows.net` for read-only) that follow the primary, and support automatic failover policies. Apps don't need to change connection strings after a failover.

## 239: How does point-in-time restore work in Azure SQL?

Azure SQL automatically takes full, differential and transaction log backups. You can restore a database to any point within the retention period (1 to 35 days, 7 by default) as a **new** database. For longer retention, set up **long-term retention** (LTR) policies for weekly, monthly or yearly backups kept up to 10 years.

## 240: What caching patterns do you use with Azure Cache for Redis?

- **Cache-aside:** the app checks the cache first; on a miss it reads from the database and writes to the cache with an expiry. The most common pattern.
- **Write-through:** the app writes to the cache and database at the same time.
- **Session store:** keep user sessions in Redis so any instance can serve the user.
- **Output caching:** cache whole rendered responses.

```js
async function getProduct(id) {
  const cached = await redis.get(`product:${id}`);
  if (cached) return JSON.parse(cached);

  const product = await db.products.findById(id);
  await redis.set(`product:${id}`, JSON.stringify(product), { EX: 300 });
  return product;
}
```

## 241: How do you add Application Insights to a Node.js app today?

Use the **Azure Monitor OpenTelemetry distro**. Call it before you load other modules so it can instrument HTTP, databases and other libraries.

```js
// at the very top of the entry file
const { useAzureMonitor } = require("@azure/monitor-opentelemetry");

useAzureMonitor({
  azureMonitorExporterOptions: {
    connectionString: process.env.APPLICATIONINSIGHTS_CONNECTION_STRING,
  },
});

const express = require("express");
```

The older `applicationinsights` SDK v2 is legacy; v3 of that package is built on the same OpenTelemetry distro.

## 242: Write a KQL query that shows the slowest API endpoints.

```kusto
AppRequests
| where TimeGenerated > ago(24h)
| summarize
    count = count(),
    p95 = percentile(DurationMs, 95),
    failures = countif(Success == false)
  by Name
| where count > 100
| order by p95 desc
| take 10
```

In the classic Application Insights view the same table is called `requests` with columns like `duration` and `success`.

## 243: How do you find failed dependencies for a specific request in Application Insights?

Requests and dependencies share an **operation ID**. Join or filter on it.

```kusto
let failedOps = AppRequests
  | where TimeGenerated > ago(1h) and Success == false
  | project OperationId;
AppDependencies
| where OperationId in (failedOps)
| where Success == false
| project TimeGenerated, Target, Name, ResultCode, DurationMs
| order by TimeGenerated desc
```

## 244: What are action groups?

An action group is a reusable list of notifications and actions that alerts call: email, SMS, voice, Azure app push, webhooks, Logic Apps, Functions, Automation runbooks, ITSM tools and Event Hubs. You create a few action groups (for example "on-call-team") and attach them to many alert rules.

## 245: What are Azure Monitor workbooks?

Workbooks are interactive reports in the Azure portal. They combine text, KQL queries, metrics, charts, parameters and grids in one page. Teams use them for troubleshooting guides, SLO dashboards and reports. Many services come with built-in workbooks, and you can save your own as Azure resources in IaC.

## 246: What are some common APIM policies?

Policies are XML blocks that run in four sections: `inbound`, `backend`, `outbound` and `on-error`.

```xml
<policies>
  <inbound>
    <base />
    <validate-jwt header-name="Authorization" failed-validation-httpcode="401">
      <openid-config url="https://login.microsoftonline.com/{tenant-id}/v2.0/.well-known/openid-configuration" />
      <audiences><audience>api://shop-api</audience></audiences>
    </validate-jwt>
    <rate-limit-by-key calls="100" renewal-period="60" counter-key="@(context.Subscription.Id)" />
    <set-header name="X-Request-Id" exists-action="skip">
      <value>@(context.RequestId.ToString())</value>
    </set-header>
  </inbound>
  <backend><base /></backend>
  <outbound><base /></outbound>
  <on-error><base /></on-error>
</policies>
```

## 247: What are products and subscriptions in APIM?

A **product** groups one or more APIs with terms of use, quotas and rate limits, for example "Free" and "Premium". Consumers **subscribe** to a product and get subscription keys, which they send in the `Ocp-Apim-Subscription-Key` header. You can require approval for subscriptions and set different limits per product.

## 248: What are the APIM tiers?

- **Consumption:** serverless, pay per call, scales automatically.
- **Developer:** for testing, no SLA.
- **Basic, Standard, Premium (classic):** dedicated units, Premium adds multi-region, VNet injection and availability zones.
- **Basic v2, Standard v2, Premium v2:** newer tiers with faster deployment and scaling, and VNet integration options.

There is also the **self-hosted gateway**, a container that runs the APIM gateway in your own environment.

## 249: How do routing rules and the rules engine work in Azure Front Door?

A Front Door profile has **endpoints**, **routes** and **origin groups**. A route matches domains and paths (like `/api/*`) and sends traffic to an origin group, with caching and HTTPS redirect settings. **Rule sets** run conditions and actions on requests and responses: redirect, rewrite URL, change headers, override caching or pick a different origin group.

## 250: How do you make sure only Front Door can reach your App Service origin?

1. Restrict access on the App Service to the `AzureFrontDoor.Backend` service tag.
2. Also check the `X-Azure-FDID` header equals your Front Door profile ID, because the service tag is shared by all Front Door customers.

Or better, use **Private Link** origins (Front Door Premium), so the app has no public access at all.

```bash
az webapp config access-restriction add -g rg-shop -n my-shop-api --priority 100 \
  --service-tag AzureFrontDoor.Backend --http-header x-azure-fdid=<front-door-id>
```

## 251: What WAF features do Front Door and Application Gateway offer?

Both support Azure Web Application Firewall with:

- **Managed rule sets:** Microsoft's Default Rule Set (based on OWASP), and the Bot Manager rule set.
- **Custom rules:** match on IP, geo location, headers, query strings, and so on.
- **Rate limiting** rules.
- **Detection mode** (log only) and **prevention mode** (block).

Start in detection mode, check logs for false positives, add exclusions, then switch to prevention.

## 252: How do you register an API and a client app in Entra ID so the client can call the API?

1. Register the **API** app. Under "Expose an API" set an Application ID URI like `api://shop-api` and add scopes like `Orders.Read`, or app roles for app-only access.
2. Register the **client** app (SPA, web app or daemon). Add API permissions for the scopes or app roles of the API.
3. Grant admin consent if needed.
4. The client gets a token for `api://shop-api/Orders.Read` (delegated) or `api://shop-api/.default` (app-only).
5. The API validates the token's issuer, audience, signature and scopes/roles.

## 253: What is the difference between delegated permissions (scopes) and application permissions (app roles)?

- **Delegated permissions** are used when a user is signed in. The app acts on behalf of the user, and the token has an `scp` claim. The effective access is the intersection of what the app is allowed and what the user can do.
- **Application permissions** are used by apps with no user, like daemons and background jobs. The token has a `roles` claim. They usually need admin consent.

## 254: Which OAuth 2.0 flow should each type of app use with Entra ID?

- **SPA (React, Angular):** authorization code flow with PKCE, using MSAL.js.
- **Server-side web app:** authorization code flow with a client secret or certificate.
- **Daemon or background service:** client credentials flow, ideally with a managed identity or federated credential.
- **API calling another API on behalf of a user:** on-behalf-of (OBO) flow.
- **Devices without a browser (CLI tools, TVs):** device code flow.

The implicit flow and the password (ROPC) flow should not be used for new apps.

## 255: How do you validate Entra ID tokens in a Node.js API?

Check the signature using the tenant's JWKS keys, plus issuer, audience, expiry and scopes. A library like `jose` handles the key fetching and caching.

```js
const { createRemoteJWKSet, jwtVerify } = require("jose");

const tenantId = process.env.TENANT_ID;
const jwks = createRemoteJWKSet(
  new URL(`https://login.microsoftonline.com/${tenantId}/discovery/v2.0/keys`),
);

async function authenticate(req, res, next) {
  try {
    const token = req.headers.authorization?.replace("Bearer ", "");
    const { payload } = await jwtVerify(token, jwks, {
      issuer: `https://login.microsoftonline.com/${tenantId}/v2.0`,
      audience: process.env.API_CLIENT_ID,
    });
    if (!payload.scp?.split(" ").includes("Orders.Read"))
      return res.sendStatus(403);
    req.user = payload;
    next();
  } catch {
    res.sendStatus(401);
  }
}
```

Make sure the API's app registration issues v2.0 tokens, or the issuer will be the older `sts.windows.net` format.

## 256: What is MSAL?

MSAL (Microsoft Authentication Library) is the official library for getting tokens from Entra ID. It handles the OAuth flows, token caching and refresh for you. There are versions for JavaScript (`@azure/msal-browser`, `@azure/msal-react`, `@azure/msal-angular`, `@azure/msal-node`), .NET, Python, Java, iOS and Android. It replaced the old ADAL library, which is no longer supported.

## 257: How do you create a custom RBAC role?

You define the allowed `Actions`, `NotActions`, `DataActions` and the assignable scopes in JSON, then create it.

```json
{
  "Name": "VM Operator",
  "Description": "Can start, stop and restart VMs",
  "Actions": [
    "Microsoft.Compute/virtualMachines/read",
    "Microsoft.Compute/virtualMachines/start/action",
    "Microsoft.Compute/virtualMachines/powerOff/action",
    "Microsoft.Compute/virtualMachines/restart/action",
    "Microsoft.Compute/virtualMachines/deallocate/action"
  ],
  "NotActions": [],
  "AssignableScopes": ["/subscriptions/<sub-id>"]
}
```

```bash
az role definition create --role-definition vm-operator.json
```

## 258: What is Privileged Identity Management (PIM)?

PIM gives just-in-time access to privileged roles, both Entra ID roles and Azure RBAC roles. Instead of being Owner all the time, a user is **eligible** for the role and **activates** it when needed, for a limited time, often with MFA, a reason and approval. All activations are logged. It reduces the risk of standing admin access. It needs an Entra ID P2 or Governance license.

## 259: What are the Azure Policy effects?

- **Deny:** block the request.
- **Audit:** allow it but mark it as non-compliant.
- **Append / Modify:** add or change properties or tags during the request.
- **DeployIfNotExists (DINE):** deploy a related resource if it's missing, like a diagnostic setting.
- **AuditIfNotExists:** audit if a related resource is missing.
- **Disabled:** turn the policy off.
- **DenyAction:** block specific actions, like delete.
- **Manual:** compliance is set by hand.

## 260: Write a simple Azure Policy that only allows certain regions.

```json
{
  "mode": "Indexed",
  "parameters": {
    "allowedLocations": { "type": "Array" }
  },
  "policyRule": {
    "if": {
      "not": {
        "field": "location",
        "in": "[parameters('allowedLocations')]"
      }
    },
    "then": { "effect": "deny" }
  }
}
```

There is also a built-in policy called "Allowed locations" that does the same thing, so in practice you would assign that one.

## 261: What is a policy initiative?

An initiative (policy set definition) is a group of policy definitions assigned together, for example "Microsoft cloud security benchmark" or your own "Company baseline". It's easier to manage and report compliance for one initiative than for dozens of separate assignments.

## 262: How does remediation work for DeployIfNotExists and Modify policies?

These policies fix new and updated resources automatically. For resources that already existed before the assignment, you create a **remediation task**. The policy assignment needs a managed identity with the right roles, because it deploys or changes resources on your behalf.

```bash
az policy remediation create --name fix-diag-settings \
  --policy-assignment <assignment-id> --resource-group rg-shop
```

## 263: What is an Azure landing zone?

A landing zone is a pre-configured environment in Azure that follows best practices for identity, networking, governance, security and management, ready for workloads to "land" in. The Azure landing zone reference architecture uses a management group hierarchy (platform, landing zones, sandbox, decommissioned), central networking (hub), policy assignments and subscription per workload. You can deploy it with Bicep, Terraform or the portal accelerator.

## 264: How do you enforce tags across an organization?

- Use Azure Policy with the **Deny** effect for "require a tag on resource groups".
- Use **Modify** policies to **inherit a tag from the resource group** to resources, so teams only set it once.
- Add tags in your IaC modules by default.
- Report on missing tags with Azure Resource Graph or policy compliance.

## 265: What are common ways to reduce Azure costs?

- Right-size or shut down unused VMs, disks, IPs and old snapshots (Advisor helps).
- Use autoscale and scale to zero (Functions, Container Apps).
- Buy reservations or savings plans for steady workloads.
- Use Azure Hybrid Benefit for Windows Server and SQL Server licenses.
- Use Spot VMs for interruptible work.
- Use storage lifecycle rules and the right access tier.
- Shut down dev/test resources outside work hours.
- Watch data egress and Log Analytics ingestion.

## 266: How do autoscale rules work for an App Service plan?

You create an autoscale setting with min, max and default instance counts and rules. Each rule has a metric, time window, threshold and action. Always create a matching scale-in rule, and make the thresholds far apart to avoid "flapping".

```bash
az monitor autoscale create -g rg-shop --resource plan-web \
  --resource-type Microsoft.Web/serverfarms --name plan-web-autoscale \
  --min-count 2 --max-count 10 --count 2

az monitor autoscale rule create -g rg-shop --autoscale-name plan-web-autoscale \
  --condition "CpuPercentage > 70 avg 10m" --scale out 2

az monitor autoscale rule create -g rg-shop --autoscale-name plan-web-autoscale \
  --condition "CpuPercentage < 30 avg 15m" --scale in 1
```

## 267: What is the difference between Uniform and Flexible orchestration in VM scale sets?

- **Uniform:** all instances are identical and managed as a group from one model. This is the older mode, used for large stateless scale-out.
- **Flexible:** you can mix VM sizes and Spot/regular VMs, use normal VM APIs on each instance, and spread instances across zones and fault domains. Flexible is now the recommended mode for most new scale sets.

## 268: How do you run setup scripts when a VM starts?

- **cloud-init** (Linux): pass a YAML file with `--custom-data`. It runs on first boot.
- **Custom Script Extension:** downloads and runs a script, works on Linux and Windows.
- **VM Applications** and **Azure Compute Gallery** images: bake software into a custom image so VMs start ready.

```bash
az vm create -g rg-demo -n vm-web-02 --image Ubuntu2404 \
  --custom-data cloud-init.yaml --generate-ssh-keys
```

```yaml
#cloud-config
package_upgrade: true
packages:
  - nginx
runcmd:
  - systemctl enable --now nginx
```

## 269: How do you mount an Azure file share in App Service or Container Apps?

In App Service (Linux) and Container Apps you can add a storage mount that points to an Azure Files share. It appears as a folder in the container, like `/mnt/data`. This is useful for content that must survive restarts or be shared between instances. File share performance is lower than local disk, so don't use it for databases.

```bash
az webapp config storage-account add -g rg-shop -n my-shop-api \
  --custom-id uploads --storage-type AzureFiles \
  --account-name stshop --share-name uploads \
  --access-key <key> --mount-path /mnt/uploads
```

## 270: How do APIs work in Azure Static Web Apps?

You can add an `api` folder with Azure Functions (managed functions), or link an existing back end: an Azure Functions app, App Service, Container Apps or API Management. Requests to `/api/*` go to the back end. Routing, auth and headers are configured in `staticwebapp.config.json`.

```json
{
  "routes": [{ "route": "/api/admin/*", "allowedRoles": ["admin"] }],
  "navigationFallback": { "rewrite": "/index.html", "exclude": ["/assets/*"] }
}
```

## 271: What is the difference between Logic Apps Consumption and Standard?

- **Consumption:** multi-tenant, one workflow per resource, pay per action execution.
- **Standard:** single-tenant, runs on the Functions runtime, many workflows per app, built-in connectors run in-process (faster), supports VNet integration, local development in VS Code and stateless workflows. You pay for the hosting plan.

Standard is better for enterprise integrations with private networking and high volume.

## 272: How do retries work for Azure Functions triggers?

It depends on the trigger. Service Bus, Storage Queue and Event Grid triggers have their own retry behavior (delivery count, dequeue count, Event Grid retries). For Timer, Event Hubs, Kafka and Cosmos DB triggers you can set a **retry policy** on the function, with fixed delay or exponential backoff.

```js
app.eventHub("ingest", {
  connection: "EventHubConnection",
  eventHubName: "telemetry",
  retry: {
    strategy: "exponentialBackoff",
    maxRetryCount: 5,
    minimumInterval: { seconds: 5 },
    maximumInterval: { minutes: 5 },
  },
  handler: async (events, context) => {
    /* ... */
  },
});
```

## 273: How do you troubleshoot an App Service app that won't start?

1. Check the **Diagnose and solve problems** blade.
2. Stream logs with `az webapp log tail` and check container logs (`docker.log` on Linux).
3. Make sure the app listens on the right port: App Service sets `PORT`, and for custom containers you set `WEBSITES_PORT`.
4. Check the startup command and that `node_modules` was included or built (`SCM_DO_BUILD_DURING_DEPLOYMENT=true`).
5. Check app settings, Key Vault reference status and the runtime version.
6. SSH into the container or use the Kudu console.

## 274: What is Azure Resource Graph?

Resource Graph lets you query all resources across subscriptions and management groups very quickly, using KQL. It's good for inventory, finding misconfigurations and compliance reporting.

```bash
az graph query -q "
Resources
| where type == 'microsoft.storage/storageaccounts'
| where properties.allowBlobPublicAccess == true
| project name, resourceGroup, subscriptionId"
```

## 275: How do you use JMESPath queries with the Azure CLI?

`--query` filters and reshapes JSON output.

```bash
# names of running VMs
az vm list -d --query "[?powerState=='VM running'].name" -o tsv

# get one value into a variable
STORAGE_ID=$(az storage account show -n stshop -g rg-shop --query id -o tsv)

# pick fields and rename them
az webapp list --query "[].{App:name, Plan:appServicePlanId, State:state}" -o table
```

## 276: What does az rest do?

`az rest` sends an authenticated request to any Azure REST API (ARM, Microsoft Graph or others) using your CLI login. It's useful for features the CLI doesn't have commands for yet.

```bash
az rest --method get \
  --url "https://management.azure.com/subscriptions/{subscriptionId}/resourceGroups?api-version=2021-04-01"

az rest --method get --url "https://graph.microsoft.com/v1.0/me"
```

The CLI replaces `{subscriptionId}` with your current subscription.

## 277: What should you check before moving resources to another resource group or subscription?

- Not every resource type supports moving; check the move support list.
- The resource ID changes, so scripts, IaC, alerts and role assignments at resource scope can break.
- Dependent resources often must move together (like a VM with its NIC and disks).
- Moving between subscriptions in different tenants is very limited.
- Locks and policies on the target can block it.

Run `az resource invoke-action --action validateMoveResources` or use the portal validation first.

## 278: What is a good naming convention for Azure resources?

The Cloud Adoption Framework suggests: `<resource-type-prefix>-<workload>-<environment>-<region>-<instance>`, for example `app-shop-prod-weu-001`, `kv-shop-prod-weu`, `rg-shop-prod-weu`. Some resources have special rules: storage account names must be 3-24 lowercase letters and numbers only and globally unique, like `stshopprodweu001`. Pick one convention, write it down and enforce it with policy or IaC modules.

## 279: How do you add sign-in to an App Service app without writing auth code?

Turn on **App Service Authentication** (often called Easy Auth). It runs as a module in front of your app, handles the sign-in flow with Entra ID, Google, GitHub, Apple or any OpenID Connect provider, and passes the user's identity to your app in headers like `X-MS-CLIENT-PRINCIPAL-NAME`. You can choose to require sign-in for all requests or let your app decide.

## 280: How do you call Microsoft Graph from an app using a managed identity?

Get a token for `https://graph.microsoft.com/.default` and give the managed identity application permissions on Graph (this is done with Graph API or PowerShell, since the portal doesn't show managed identities in the API permissions screen).

```js
const { DefaultAzureCredential } = require("@azure/identity");

const credential = new DefaultAzureCredential();
const { token } = await credential.getToken(
  "https://graph.microsoft.com/.default",
);

const res = await fetch("https://graph.microsoft.com/v1.0/users?$top=5", {
  headers: { Authorization: `Bearer ${token}` },
});
console.log(await res.json());
```

## 281: How does App Configuration handle feature flags?

Feature flags are stored as special keys with filters, like percentage rollout, time window or targeting specific users and groups. The app uses a feature management library to check them, and it refreshes values without a restart.

```js
const { load } = require("@azure/app-configuration-provider");
const {
  FeatureManager,
  ConfigurationMapFeatureFlagProvider,
} = require("@microsoft/feature-management");
const { DefaultAzureCredential } = require("@azure/identity");

const appConfig = await load(
  "https://appcs-shop.azconfig.io",
  new DefaultAzureCredential(),
  {
    featureFlagOptions: { enabled: true, refresh: { enabled: true } },
  },
);

const fm = new FeatureManager(
  new ConfigurationMapFeatureFlagProvider(appConfig),
);
if (await fm.isEnabled("NewCheckout")) {
  // show new checkout
}
```

## 282: What is the difference between Azure Functions and Azure Container Apps for background processing?

- **Functions:** event-driven with triggers and bindings, very little code for common cases, built-in Durable Functions for workflows. Best when the work fits the function model.
- **Container Apps:** any language, framework or long-running process in a container, scale rules from KEDA, Dapr, and jobs. Best when you need more control, have existing containerized services, or need long-running work.

You can also host Functions inside Container Apps to get both.

## 283: What is the difference between App Service, Container Apps and AKS for hosting a web API?

- **App Service:** simplest for a web app or API, built-in slots, auth and custom domains. Less suited for many microservices.
- **Container Apps:** containers and microservices without managing Kubernetes, scale to zero, revisions, Dapr. Good default for containerized microservices.
- **AKS:** full Kubernetes control, any operator or tool, complex networking. Highest operational effort; choose it when you need Kubernetes features or already have Kubernetes skills.

## 284: How do you set up a CI/CD pipeline for a Node.js app on App Service with GitHub Actions?

```yaml
name: deploy
on:
  push:
    branches: [main]

permissions:
  id-token: write
  contents: read

jobs:
  build-deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-node@v4
        with:
          node-version: 22
      - run: npm ci && npm run build && npm prune --omit=dev
      - uses: azure/login@v2
        with:
          client-id: ${{ secrets.AZURE_CLIENT_ID }}
          tenant-id: ${{ secrets.AZURE_TENANT_ID }}
          subscription-id: ${{ secrets.AZURE_SUBSCRIPTION_ID }}
      - uses: azure/webapps-deploy@v3
        with:
          app-name: my-shop-api
          slot-name: staging
          package: .
      - run: az webapp deployment slot swap -g rg-shop -n my-shop-api --slot staging --target-slot production
```

## 285: What are access restrictions in App Service?

Access restrictions are an IP firewall for an App Service app. You add allow or deny rules by IP range, service tag (like `AzureFrontDoor.Backend`) or VNet subnet (with service endpoints), with priorities. The SCM (Kudu) site can have its own rules. For full privacy, use a private endpoint and turn off public network access instead.

## 286: What does an Azure SQL firewall do?

Azure SQL has a server-level and database-level firewall. By default nothing can connect. You add rules for IP ranges, allow "Azure services" (which allows **all** Azure IPs, including other customers, so avoid it), use VNet rules with service endpoints, or turn off public access and use private endpoints. Most production setups use private endpoints.

## 287: How do you scale an Azure SQL database without downtime?

You can change the tier or compute size online with `az sql db update` or the portal. Azure creates the new compute, syncs it and then switches over. Open connections are dropped briefly at the end, so apps must have **retry logic** for transient errors. Moving to or from Hyperscale has some special rules.

```bash
az sql db update -g rg-shop -s sql-shop -n shop --service-objective GP_Gen5_8
```

## 288: What are transient errors and how do you handle them in Azure?

Transient errors are temporary failures, like a dropped connection during a failover, a throttling response (HTTP 429/503) or a timeout. Handle them with retries using exponential backoff and jitter. The Azure SDKs retry automatically by default; you can tune the retry options. Make sure the operations you retry are idempotent.

```js
const client = new CosmosClient({
  endpoint,
  aadCredentials: credential,
  connectionPolicy: {
    retryOptions: { maxRetryAttemptCount: 9, maxWaitTimeInSeconds: 30 },
  },
});
```

## 289: How do you protect a VM from being exposed to the internet?

- Don't give it a public IP; use Azure Bastion or a VPN for admin access.
- Use NSGs that deny inbound from the internet.
- If you need temporary access, use **just-in-time VM access** from Defender for Cloud, which opens ports only for a short time for an approved IP.
- Use Entra ID login for Linux and Windows VMs instead of local passwords.
- Keep it patched with Azure Update Manager.

## 290: What is Azure Update Manager?

Azure Update Manager manages OS updates for Windows and Linux machines in Azure and on-premises (through Azure Arc). It can check for missing updates, install updates on a schedule with maintenance configurations, and report compliance. It replaces the old Automation Update Management solution.

## 291: What is the difference between Azure Monitor Agent and the older agents?

The **Azure Monitor Agent (AMA)** is the single current agent for collecting logs and performance data from VMs and Arc servers. What to collect is set in **data collection rules (DCRs)**, which you can reuse and target to many machines. The older Log Analytics agent (MMA/OMS) was retired in August 2024, so existing setups had to move to AMA.

## 292: What are data collection rules?

A data collection rule defines what data to collect, how to transform it (with KQL), and where to send it. It is used by the Azure Monitor Agent, the Logs Ingestion API for custom logs, and some services. Transformations can filter out noisy rows or remove sensitive fields before ingestion, which also saves money.

## 293: How do you send custom logs from an app to Log Analytics?

Use the **Logs Ingestion API** with a data collection endpoint and data collection rule that map your JSON to a custom table (ending in `_CL`).

```js
const { LogsIngestionClient } = require("@azure/monitor-ingestion");
const { DefaultAzureCredential } = require("@azure/identity");

const client = new LogsIngestionClient(
  "https://dce-shop.westeurope-1.ingest.monitor.azure.com",
  new DefaultAzureCredential(),
);

await client.upload("dcr-immutable-id", "Custom-OrderEvents_CL", [
  { TimeGenerated: new Date().toISOString(), OrderId: "42", Status: "paid" },
]);
```

The identity needs the "Monitoring Metrics Publisher" role on the DCR.

## 294: How do you handle secrets in Container Apps?

Container Apps has app-level secrets that you can reference from environment variables. A secret can hold the value directly or reference a Key Vault secret using a managed identity, which is the better option.

```bash
az containerapp secret set -g rg-shop -n shop-api \
  --secrets db-password=keyvaultref:https://kv-shop.vault.azure.net/secrets/DbPassword,identityref:system

az containerapp update -g rg-shop -n shop-api \
  --set-env-vars DB_PASSWORD=secretref:db-password
```

## 295: How does the Cosmos DB Functions trigger work?

The Cosmos DB trigger uses the change feed. It needs a **lease container** where it stores its progress per partition range, so several instances can split the work. Each invocation receives a batch of changed documents.

```js
app.cosmosDB("ordersChanged", {
  connection: "CosmosConnection",
  databaseName: "shop",
  containerName: "orders",
  leaseContainerName: "leases",
  createLeaseContainerIfNotExists: true,
  handler: async (documents, context) => {
    for (const doc of documents) context.log("Changed order", doc.id);
  },
});
```

## 296: How do you protect against accidental deletion of a production resource group?

- Add a **CanNotDelete** lock.
- Limit who has Owner/Contributor and use PIM for just-in-time access.
- Use deployment stacks with deny settings.
- Turn on soft delete and backups for data services (storage, Key Vault, SQL, Cosmos DB continuous backup).
- Alert on delete operations in the activity log.

## 297: What is Azure Chaos Studio?

Chaos Studio lets you run controlled fault injection experiments on Azure resources: shut down VMs, add network latency, fail over Cosmos DB, stress CPU in AKS pods, block access to a dependency and so on. You use it to test that your app really survives failures, as part of resilience testing.

## 298: What is Azure Load Testing?

Azure Load Testing is a managed service for running large load tests using JMeter or Locust scripts. It generates traffic from Azure, collects client metrics and server-side metrics from your Azure resources, and can run in CI/CD with pass/fail criteria like "p95 response time under 500 ms".

## 299: How do you set up a custom domain with HTTPS on Azure Front Door?

1. Add the custom domain to the Front Door profile.
2. Prove ownership with a TXT record (`_dnsauth.<domain>`).
3. Choose an **AFD managed certificate** (free, auto-renewed) or your own certificate from Key Vault.
4. Add a CNAME from your domain to the Front Door endpoint host name.
5. Link the domain to a route.

For apex domains (no `www`), use Azure DNS alias records, since a CNAME is not allowed at the zone apex.

## 300: How would you organize subscriptions for a mid-sized company?

A common setup following the landing zone guidance:

- A **platform** management group with subscriptions for identity, management (logging) and connectivity (hub network).
- A **landing zones** management group with **one subscription per workload and environment**, like `shop-prod` and `shop-dev`, split into "corp" (private) and "online" (internet-facing) groups.
- A **sandbox** management group for experiments with relaxed policies and budgets.

This gives clean cost separation, smaller blast radius and clear access boundaries.

# Advanced Questions (301-450)

## 301: What are the five pillars of the Azure Well-Architected Framework?

1. **Reliability:** the system keeps working and recovers from failures.
2. **Security:** protect data and systems from threats.
3. **Cost Optimization:** get the most value for the money spent.
4. **Operational Excellence:** deployment, monitoring and processes that keep the system healthy.
5. **Performance Efficiency:** the system scales and responds well under load.

The pillars often trade off against each other, like reliability vs cost. Azure Advisor and the Well-Architected Review tool score your workloads against them.

## 302: What are RTO and RPO, and how do they affect your Azure design?

- **RTO (Recovery Time Objective):** how long the system can be down.
- **RPO (Recovery Point Objective):** how much data you can lose, measured in time.

An RPO of hours can be met with backups and geo-restore. An RPO of seconds needs continuous replication like SQL failover groups or Cosmos DB multi-region. An RTO of minutes needs a warm or active standby region and automated failover; an RTO of a day can use redeploy-from-IaC. Lower numbers mean higher cost, so agree on them with the business first.

## 303: Compare the main disaster recovery strategies on Azure.

- **Backup and restore:** cheapest, RTO hours to days. Restore from geo-redundant backups and redeploy from IaC.
- **Pilot light:** data is replicated to the second region, compute is created only during a disaster.
- **Warm standby:** a smaller copy of the full stack runs in the second region and is scaled up during failover.
- **Active-active:** both regions serve traffic all the time behind Front Door or Traffic Manager. Lowest RTO/RPO, highest cost and complexity, especially for data.

## 304: How do you design an active-active multi-region web app on Azure?

- **Front Door** routes users to the closest healthy region and fails over based on health probes.
- Each region has a full stateless stack: App Service or Container Apps, zone-redundant.
- **Data:** Cosmos DB with multi-region writes, or Azure SQL with a failover group (writes go to one region, reads can be local).
- **Caching** per region; avoid cross-region cache dependencies.
- **Messaging:** Service Bus Premium with geo-replication, or regional queues with idempotent consumers.
- **Secrets and config** replicated (Key Vault per region, App Configuration replicas).
- Deploy the same IaC to both regions and test failover regularly.

The hardest part is data consistency, so decide what must be strongly consistent and what can be eventually consistent.

## 305: How does conflict resolution work with Cosmos DB multi-region writes?

When two regions update the same item at the same time, Cosmos DB must pick a winner. The default policy is **last writer wins** based on `_ts` or a custom numeric property you choose. You can instead use a **custom** policy with a stored procedure that merges the conflicting versions, or leave conflicts in the **conflicts feed** for your app to resolve. Design the data model to reduce conflicts, for example by making each region the owner of certain items.

## 306: What happens to your app during an Azure SQL failover group failover?

The listener endpoint DNS changes to point to the new primary. Existing connections are dropped and the app must reconnect, so retry logic is required. With a **planned** failover the secondary is fully synced first, so no data is lost. With a **forced** failover, recent transactions that weren't replicated yet can be lost. Also keep in mind the app tier should run close to the new primary, or every query now crosses regions.

## 307: Why can Traffic Manager failover be slower than expected?

Traffic Manager works through DNS. After it marks an endpoint as unhealthy (based on probe interval and tolerated failures), clients and resolvers still use the cached DNS answer until its TTL expires. Some clients and resolvers ignore TTL or cache longer. Use a low TTL (for example 30-60 seconds) and faster probing, or use Front Door, which fails over at the HTTP layer without depending on client DNS caches.

## 308: How do you design for availability zones inside one region?

- Use zone-redundant services where possible: ZRS storage, zone-redundant App Service plans (at least 2-3 instances), zone-redundant SQL and Cosmos DB, Standard Load Balancer and Application Gateway v2 across zones.
- For VMs and AKS node pools, spread instances across zones 1, 2 and 3.
- Keep enough capacity to lose one zone, for example 3 instances when you need 2.
- Watch out for cross-zone latency and data transfer between zones in chatty services.

## 309: What does zone-redundant mean for App Service, and what do you need to turn it on?

A zone-redundant App Service plan spreads its instances across availability zones, so a zone outage doesn't take the app down. You need a Premium v2/v3/v4 or Isolated v2 plan in a region that supports zones, and at least two instances. You can turn it on when creating the plan, and on newer plans it can be changed later.

## 310: How do you do a zero-downtime database schema change while deploying a new app version?

Use the **expand and contract** pattern:

1. **Expand:** add new columns/tables in a backward-compatible way. The old app version keeps working.
2. Deploy the new app version that writes to both old and new structures, or reads the new ones with a fallback.
3. Backfill data.
4. **Contract:** after all instances run the new version, remove the old columns in a later release.

This matters with slot swaps and canary releases because old and new versions run at the same time.

## 311: How do you do a canary release with Azure Front Door or Container Apps?

- **Container Apps:** run two revisions and set traffic weights (95/5, then 80/20, then 100). Watch error rates and latency in Application Insights before moving forward.
- **App Service:** use deployment slots with "traffic routing" percentages to send a share of users to the staging slot.
- **Front Door:** put two origins (old and new) in one origin group with weights.

Automate the steps and the rollback, and decide in advance which metrics stop the rollout.

## 312: What are the networking options for AKS?

- **Azure CNI Overlay (recommended default):** pods get IPs from a private overlay range, not from the VNet, so you save VNet address space. Scales to large clusters.
- **Azure CNI (flat / VNet IPs):** each pod gets an IP from the VNet subnet. Pods are directly reachable from the network but it uses a lot of IPs.
- **Azure CNI powered by Cilium:** uses eBPF for faster routing, network policy and observability, on top of overlay or VNet modes.
- **Kubenet:** the older basic option, being retired; move to CNI Overlay.

## 313: What is AKS workload identity?

Workload identity lets pods get Entra ID tokens without secrets. The cluster has an OIDC issuer, and you create a **federated credential** on a user-assigned managed identity that trusts a specific Kubernetes service account. Pods using that service account get a projected token, which the Azure SDK exchanges for an Entra ID token. It replaced the deprecated AAD Pod Identity.

```bash
az identity federated-credential create --name shop-api-fic \
  --identity-name id-shop-api -g rg-aks \
  --issuer $(az aks show -g rg-aks -n aks-shop --query oidcIssuerProfile.issuerUrl -o tsv) \
  --subject system:serviceaccount:shop:shop-api
```

```yaml
apiVersion: v1
kind: ServiceAccount
metadata:
  name: shop-api
  namespace: shop
  annotations:
    azure.workload.identity/client-id: <identity-client-id>
---
# in the pod template
metadata:
  labels:
    azure.workload.identity/use: "true"
spec:
  serviceAccountName: shop-api
```

## 314: What is the difference between system and user node pools in AKS?

**System node pools** run critical cluster pods like CoreDNS and metrics-server. Every cluster needs at least one, and it should have at least 3 nodes in production. **User node pools** run your application pods. Separating them means a noisy app can't starve system pods. You can taint the system pool with `CriticalAddonsOnly=true:NoSchedule` and use different VM sizes, Spot VMs or GPU nodes in user pools.

## 315: How do the cluster autoscaler and HPA work together in AKS?

The **Horizontal Pod Autoscaler (HPA)** adds or removes pods based on CPU, memory or custom metrics. When new pods can't be scheduled because there isn't enough capacity, the **cluster autoscaler** adds nodes. When nodes are underused for a while, it removes them. For event-driven scaling, the **KEDA** add-on scales pods based on queue length, Event Hubs lag and so on. **Node auto-provisioning** (based on Karpenter) can pick the right VM sizes automatically.

## 316: How do you upgrade an AKS cluster safely?

- Check the supported Kubernetes versions; AKS supports about three minor versions, and you can only upgrade one minor version at a time.
- Set **Pod Disruption Budgets** so upgrades don't take down all replicas.
- Set `maxSurge` on node pools to add extra nodes during the upgrade.
- Upgrade the control plane, then node pools, starting with non-production clusters.
- Use **auto-upgrade channels** and **planned maintenance windows** for regular patching, and node OS auto-upgrade for security patches.
- For bigger risk, use a blue-green cluster approach.

## 317: What is AKS Automatic?

AKS Automatic is an AKS mode where Azure makes most decisions for you: node provisioning, scaling, upgrades, networking (CNI Overlay with Cilium), security settings like workload identity and image cleaner, and monitoring are configured with recommended defaults. You still get the full Kubernetes API. It's for teams that want Kubernetes without managing the details of node pools. The regular mode is now called AKS Standard.

## 318: How do you make an AKS cluster private?

Create the cluster with `--enable-private-cluster`. The API server then has only a private IP through a private endpoint, and is reachable only from the VNet, peered networks or on-premises over VPN/ExpressRoute. You need private DNS for the API server name, and your CI agents must run inside the network (or use `az aks command invoke`). Another option is **API server VNet integration**, which puts the API server directly in a subnet.

## 319: How do you use Key Vault secrets in AKS pods?

Use the **Secrets Store CSI Driver** with the Azure Key Vault provider (an AKS add-on). You define a `SecretProviderClass` that lists the secrets, and the pod mounts them as files. It can also sync them to Kubernetes secrets and rotate them. Authentication uses workload identity.

```yaml
apiVersion: secrets-store.csi.x-k8s.io/v1
kind: SecretProviderClass
metadata:
  name: kv-shop
  namespace: shop
spec:
  provider: azure
  parameters:
    keyvaultName: kv-shop-prod
    tenantId: <tenant-id>
    clientID: <workload-identity-client-id>
    objects: |
      array:
        - |
          objectName: DbPassword
          objectType: secret
```

## 320: What ingress options exist for AKS?

- **Application routing add-on:** managed NGINX ingress with Azure DNS and Key Vault certificate integration.
- **Application Gateway for Containers:** the newer layer 7 load balancer for AKS, supports the Gateway API, traffic splitting and fast updates.
- **AGIC (Application Gateway Ingress Controller):** the older way to use Application Gateway with AKS.
- **Istio service mesh add-on:** Istio ingress gateways.
- Self-managed controllers like NGINX, Traefik or Envoy Gateway.

Note that the community ingress-nginx project has been retired, so check the support plan for whichever NGINX option you pick.

## 321: How do you integrate AKS with Entra ID for user access?

Turn on **Entra ID integration** so `kubectl` users sign in with Entra ID. Then choose how to authorize:

- **Kubernetes RBAC with Entra groups:** create `RoleBinding`s that reference Entra group object IDs.
- **Azure RBAC for Kubernetes:** assign Azure roles like "Azure Kubernetes Service RBAC Reader" at cluster or namespace scope.

Disable local accounts (`--disable-local-accounts`) so nobody can bypass Entra ID with the admin kubeconfig.

## 322: What is the zero trust model and how do you apply it in Azure?

Zero trust means: **verify explicitly**, **use least privilege** and **assume breach**. In Azure that looks like:

- Strong identity with MFA and Conditional Access for every user.
- Managed identities and federated credentials instead of secrets.
- Least privilege RBAC with PIM for admin roles.
- Private endpoints and no public access to data services, NSGs and Azure Firewall between tiers.
- Encryption everywhere, logs to Sentinel, Defender for Cloud for threat detection.

## 323: How do you prevent data exfiltration from Azure PaaS services?

- Turn off public network access and use **private endpoints**.
- Use Azure Firewall with FQDN rules for outbound traffic, and block everything else.
- Turn off shared key access on storage; use Entra ID with tight RBAC.
- Use **network security perimeter** to group PaaS resources so they can only talk to each other.
- Use service endpoint policies to allow only specific storage accounts from a subnet.
- Monitor data access logs and use Defender for Storage and Purview DLP.

## 324: What are customer-managed keys (CMK) and when do you need them?

By default Azure encrypts data at rest with Microsoft-managed keys. With CMK, the service uses a key that **you** keep in Key Vault or Managed HSM to wrap the data encryption key. You control rotation and can revoke access by disabling the key, which makes the data unreadable. It's often required by compliance rules. The downside is more work: if the key is deleted and purge protection is off, the data is gone for good.

## 325: What is Azure Key Vault Managed HSM?

Managed HSM is a fully managed, single-tenant hardware security module pool, validated at FIPS 140-3 Level 3. You control the security domain and role-based access within the HSM. It's used when compliance requires dedicated HSMs for keys, for example in finance. Regular Key Vault Premium also stores keys in HSMs, but those are multi-tenant.

## 326: How does encryption in transit work in Azure?

- Azure encrypts traffic between data centers with MACsec on Microsoft's backbone.
- Services require TLS for client connections. Set `minimumTlsVersion` to TLS 1.2 or higher on storage, SQL, App Service and so on; TLS 1.0 and 1.1 are being retired across Azure.
- For VM-to-VM traffic, use TLS in the app, or encryption at the VNet level on supported VM sizes.
- VPN Gateway uses IPsec; ExpressRoute can add MACsec or IPsec.

## 327: What is Azure confidential computing?

Confidential computing protects data while it is being used (in memory) by running workloads inside a hardware-based **trusted execution environment**. Options include confidential VMs (AMD SEV-SNP, Intel TDX), confidential containers on AKS and Container Instances, and Intel SGX enclaves. Even the cloud operator can't read the memory. It's used for very sensitive data like health records or multi-party analytics.

## 328: How do you rotate secrets that can't be replaced by managed identities?

- Store them in Key Vault and have apps read them by name without a version, so new versions are picked up.
- Use the **two-key pattern**: services like storage, Cosmos DB and APIM have two keys. Switch apps to key 2, rotate key 1, then the other way next time.
- Use Key Vault **rotation policies** for keys and Event Grid "near expiry" events to trigger a Function that rotates the secret.
- Prefer turning off key-based auth altogether when the service supports Entra ID.

## 329: What are the risks of Entra app client secrets and what are the alternatives?

Client secrets are long-lived passwords that end up in config files, CI variables and laptops, and they leak. If someone gets one, they can act as your app from anywhere. Alternatives, in order of preference:

1. **Managed identities** for workloads running in Azure.
2. **Workload identity federation** (federated credentials) for GitHub Actions, Kubernetes, other clouds.
3. **Certificates** stored in Key Vault.

If you must use secrets, keep them short-lived, store them in Key Vault and restrict app permissions.

## 330: How do you limit what a compromised managed identity can do?

- Give each workload its own identity, not one shared identity for everything.
- Assign roles at the smallest scope (one Key Vault, one container) with data-plane roles only.
- Avoid Owner/Contributor or `*` permissions for app identities.
- Avoid broad Microsoft Graph permissions.
- Monitor sign-in logs for managed identities and unusual access.
- Network-restrict the resources it can reach.

## 331: How does Defender for Cloud's secure score work?

The secure score is the percentage of security recommendations you've implemented, weighted by how important each control is. Recommendations come from the **Microsoft cloud security benchmark** and other standards you add, like CIS or PCI DSS. Fixing all recommendations in a control raises the score. It gives teams a clear list of what to fix first.

## 332: What is Defender CSPM's attack path analysis?

Defender CSPM builds a graph of your cloud resources, identities, network exposure and vulnerabilities. Attack path analysis finds chains an attacker could use, like "internet-exposed VM with a critical vulnerability → has a managed identity → can read a storage account with sensitive data". It ranks them by risk so you fix the paths that matter most instead of thousands of separate findings.

## 333: How do you secure a Cosmos DB account?

- Turn off key-based auth (`disableLocalAuth: true`) and use Entra ID with Cosmos DB data-plane RBAC roles.
- Turn off public network access and use private endpoints.
- Use CMK if compliance needs it.
- Turn on continuous backup for point-in-time restore.
- Send diagnostic logs to Log Analytics and turn on Defender for Azure Cosmos DB.
- Use resource locks on the account.

## 334: Why should you create SDK clients like CosmosClient or BlobServiceClient only once?

Clients keep connection pools, metadata caches (like Cosmos DB partition maps) and token caches. Creating a new client per request opens new connections every time, which increases latency, wastes CPU, can exhaust ports and can even hit rate limits on the token endpoint. Create one client per service per app (a singleton) and reuse it.

## 335: What is SNAT port exhaustion and how do you fix it in App Service?

When an app calls external endpoints, outbound connections are translated (SNAT) to a shared public IP, and each instance has a limited number of SNAT ports per destination. Opening many short-lived connections without reuse uses up the ports, and new connections fail or hang. Fixes:

- Reuse HTTP connections with keep-alive (a shared `http.Agent` in Node.js, a single `HttpClient` in .NET).
- Reuse SDK clients and database connection pools.
- Use private endpoints or service endpoints for Azure services, which don't use SNAT.
- Use VNet integration with a NAT gateway, which gives many more ports.

```js
const https = require("https");
const agent = new https.Agent({ keepAlive: true, maxSockets: 50 });
// pass agent to your HTTP client
```

## 336: How do you detect and fix a hot partition in Cosmos DB?

Signs: 429 (throttled) errors while total RU usage looks low, and the **Normalized RU Consumption** metric near 100% for one partition key range. Use the "partition key statistics" and diagnostic logs (`CDBPartitionKeyRUConsumption`) to find the hot key. Fixes:

- Change to a key with higher cardinality (needs a new container and data migration).
- Use a synthetic key, like `tenantId-random(0..9)`, for write-heavy keys.
- Use **hierarchical partition keys** (like `tenantId/userId`) so large tenants spread across physical partitions.
- Cache hot reads.

## 337: Why are cross-partition queries expensive in Cosmos DB, and how do you avoid them?

If a query doesn't filter on the partition key, Cosmos sends it to every physical partition and merges the results. The RU cost grows with the number of partitions, and latency goes up. To avoid them:

- Design the partition key around the most common queries.
- Duplicate data into another container with a different partition key, kept in sync with the change feed.
- Use point reads (`item(id, pk).read()`) when you know the ID; they're the cheapest operation.

## 338: How do you do bulk inserts into Cosmos DB efficiently?

Use the SDK's bulk support, which groups operations by partition and sends them in parallel batches. Make sure you have enough RU/s, or raise throughput temporarily. Turn off indexing on paths you don't need, and keep items small.

```js
const operations = items.map((item) => ({
  operationType: "Create",
  resourceBody: item,
}));

const results = await container.items.executeBulkOperations(operations);
const failed = results.filter((r) => r.error);
```

For transactions inside one partition key, use `container.items.batch()` (transactional batch, up to 100 operations).

## 339: What is Azure SQL Hyperscale and when do you use it?

Hyperscale is an Azure SQL tier with a different architecture: compute is separate from storage, which is spread across page servers with a log service in between. It supports databases up to 128 TB, fast backups and restores (snapshot-based, size doesn't matter), quick scaling of compute, and up to 4 HA replicas and 30 named replicas for read scale-out. Use it for large databases or when you need fast scaling. It's now priced close to General Purpose, so it's a common default.

## 340: How do you find and fix slow queries in Azure SQL?

- **Query Performance Insight** and **Query Store** show the top queries by CPU, duration and IO, and plan changes.
- **Automatic tuning** can create/drop indexes and force the last good plan when a plan regresses.
- Check missing index recommendations and wait statistics (`sys.dm_db_wait_stats`).
- Look for parameter sniffing, implicit conversions and scans on big tables in the execution plan.
- Check if you are hitting resource limits (`sys.dm_db_resource_stats`) and need a bigger tier.

## 341: What is read scale-out in Azure SQL?

In Premium, Business Critical and Hyperscale tiers, a read-only replica exists for high availability. With read scale-out you send read-only queries to it by adding `ApplicationIntent=ReadOnly` to the connection string. It's useful for reports and analytics so they don't load the primary. Data on the replica can lag slightly behind.

## 342: How do you avoid large keys and other common problems with Redis on Azure?

- Keep values small (ideally under 100 KB); split big objects.
- Always set expiry on cache keys, and pick an eviction policy like `volatile-lru` or `allkeys-lru`.
- Avoid slow commands like `KEYS *` on large data sets; use `SCAN`.
- Reuse a single connection (multiplexed) instead of opening many.
- Watch server load, memory usage and connected clients metrics.
- Use clustering for more throughput and memory.
- Plan for patching failovers with retry logic.

## 343: How do you size Event Hubs throughput?

- **Standard:** throughput units (TUs). 1 TU = 1 MB/s or 1,000 events/s in, 2 MB/s out. Use **auto-inflate** to raise TUs automatically.
- **Premium:** processing units (PUs), dedicated resources, more predictable latency.
- **Dedicated:** capacity units for very high volume.

Also plan **partitions** for parallelism: the number of active consumers in a group is limited by the partition count. Partition count can be increased in Premium and Dedicated but not decreased.

## 344: How do you keep message order while scaling consumers?

You can only keep order per key, not globally, if you want parallel processing.

- **Event Hubs:** send events with a partition key (like `deviceId`); one consumer handles each partition in order.
- **Service Bus:** use **sessions** with `sessionId = orderId`; each session is locked to one receiver.
- Make processing idempotent and handle out-of-order cases anyway, because retries and failovers can still reorder messages.

## 345: What is the outbox pattern and how do you implement it on Azure?

The problem: you need to update the database and publish a message, but you can't do both in one transaction. With the outbox pattern you write the business data and an "outbox" record in the **same database transaction**. A separate process reads the outbox and publishes to Service Bus, then marks the record as sent.

On Azure, if you use Cosmos DB, you can use a transactional batch for the item and outbox entry, and the **change feed** (for example a Functions Cosmos DB trigger) to publish. With Azure SQL, a background worker polls the outbox table. Consumers must be idempotent because a message may be sent twice.

## 346: How do you make message consumers idempotent?

- Use a unique message ID and store processed IDs (with expiry) in a table, Cosmos DB or Redis; skip duplicates.
- Make operations naturally idempotent: "set status to paid" instead of "add 10 to balance".
- Use conditional writes with ETags or unique constraints.
- Combine the "mark as processed" write with the business update in one transaction where possible.

## 347: How do you handle poison messages?

A poison message is one that always fails. Without handling it can block a queue or cause endless retries. In Service Bus, set a reasonable **max delivery count** so it goes to the dead-letter queue. In Storage Queues, Functions move it to a `<queue>-poison` queue after 5 tries. Then:

- Alert when the DLQ length is above zero.
- Log enough context to understand the failure.
- Have a tool or process to inspect, fix and resubmit messages.

## 348: How does Durable Functions replay work, and why must orchestrators be deterministic?

Durable Functions stores every step of an orchestration as events in a history (event sourcing). When the orchestrator wakes up (for example after an activity finishes), it runs from the start again and **replays** the history: calls that already completed return their saved results instead of running again. That's why orchestrator code must be deterministic:

- Don't use `Date.now()`, use `context.df.currentUtcDateTime`.
- Don't use random numbers or new GUIDs directly.
- Don't do I/O (HTTP, database) in the orchestrator; do it in activities.
- Don't use non-durable timers like `setTimeout`; use `context.df.createTimer`.

## 349: What storage providers can Durable Functions use?

- **Azure Storage (default):** queues, tables and blobs. Simple, but has throughput limits.
- **Netherite:** uses Event Hubs and page blobs for much higher throughput. It is no longer recommended for new apps.
- **Microsoft SQL Server / Azure SQL:** runs on a database you manage.
- **Durable Task Scheduler:** a fully managed backend from Azure, with high performance and a built-in dashboard, now the recommended option for new high-scale apps.

## 350: How does the Azure Functions scale controller decide how many instances to run?

On Consumption and Premium plans, the scale controller looks at trigger-specific signals, like queue length and message age for queues, partition count and lag for Event Hubs, or request rate for HTTP, and adds or removes instances. Limits apply, for example Event Hubs can't use more instances than partitions. **Flex Consumption** scales HTTP functions together and other triggers per function, and uses **per-instance concurrency** settings to decide how many instances are needed. You can cap the max instance count to protect downstream systems.

## 351: What are ARM throttling limits and how do you deal with them?

ARM limits the number of read and write requests per subscription and per tenant (using a token bucket per region). When you go over, you get HTTP 429 with a `Retry-After` header. This happens with scripts that poll a lot, big parallel deployments, or many tools scanning resources. Fixes:

- Respect `Retry-After` and back off (the SDKs and CLI do this).
- Use **Azure Resource Graph** for reads across many resources instead of calling ARM for each.
- Spread workloads across subscriptions.
- Reduce polling frequency, use Event Grid events for resource changes.

## 352: How do you handle 429 responses from Azure services in your app?

- Read the `Retry-After` (or `x-ms-retry-after-ms`) header and wait at least that long.
- Use exponential backoff with jitter so all instances don't retry at the same time.
- Limit concurrency on your side (a queue or semaphore).
- For Cosmos DB, check the **429 rate** and raise throughput or use autoscale; a small rate of 429s (1-5%) is fine and handled by the SDK.
- For Azure OpenAI, watch tokens-per-minute quotas and use multiple deployments or provisioned throughput.
- Add a circuit breaker so you stop hammering a service that is overloaded.

## 353: How do you design a multi-tenant SaaS application on Azure?

Main decisions:

- **Isolation model:** shared everything (tenant ID column), database per tenant (elastic pools), or a full stamp per tenant/group. Many apps mix: shared app tier, separate databases for big customers.
- **Deployment stamps:** repeat the same stack per region or per group of tenants to scale and limit blast radius.
- **Identity:** Entra ID multi-tenant app registration or Entra External ID.
- **Noisy neighbors:** rate limits per tenant in APIM, Cosmos DB hierarchical partition keys by tenant, throughput per tenant.
- **Cost tracking:** tag or measure usage per tenant.
- **Tenant routing:** a catalog that maps tenant to stamp, with Front Door routing.

## 354: What is the deployment stamps pattern?

A deployment stamp is a full copy of your app's infrastructure (compute, data, storage) that serves a subset of users or tenants. To grow, you add another stamp instead of making one stamp bigger. Benefits: you avoid hitting service limits, failures only affect one stamp, and you can roll out updates stamp by stamp. A global layer (Front Door plus a tenant catalog) routes each user to their stamp.

## 355: How do you choose between Azure Firewall, NSGs and NVAs?

- **NSGs:** basic layer 3-4 allow/deny per subnet or NIC, free, everywhere.
- **Azure Firewall:** managed, stateful firewall for central control in the hub: FQDN filtering, threat intelligence, NAT, and in Premium TLS inspection, IDPS and URL filtering. Good default for egress control.
- **Third-party NVAs** (Palo Alto, Fortinet, and so on): when you need features or the same tooling as on-premises. More work to run highly available.

Most setups use NSGs everywhere plus Azure Firewall in the hub.

## 356: What is Azure Virtual WAN and when would you choose it over a hand-built hub-and-spoke?

Virtual WAN is a Microsoft-managed networking service with hubs in each region that connect VNets, branch offices (SD-WAN, VPN), remote users and ExpressRoute, with transitive routing between them all. Choose it when you have many regions, many branches or need any-to-any connectivity without managing route tables and gateways yourself. A customer-managed hub-and-spoke gives more control and can be cheaper for simple single-region setups.

## 357: How do you set up DNS for private endpoints in a hybrid network?

- Create the `privatelink.*` private DNS zones once, centrally (in the connectivity subscription), and link them to the hub VNet.
- Use **Azure DNS Private Resolver** in the hub: an inbound endpoint lets on-premises DNS servers forward Azure zones to it; an outbound endpoint with forwarding rules sends on-premises domains from Azure back to on-premises DNS.
- Spokes use the hub resolver (or Azure-provided DNS with zone links).
- Use Azure Policy (DINE) to automatically create the DNS record when someone creates a private endpoint.

## 358: What is forced tunneling and what problems can it cause?

Forced tunneling sends all internet-bound traffic from Azure through on-premises or a central firewall (route `0.0.0.0/0` to a firewall or VPN). It gives central inspection. Problems: some Azure services need direct access to Azure management endpoints (for example App Service Environment, SQL Managed Instance, AKS) and break if their traffic goes on-premises. Latency also goes up. You usually need specific routes or firewall rules for service tags these services rely on.

## 359: What is asymmetric routing and how does it break things in Azure?

Asymmetric routing happens when the request goes through one path (for example through a firewall) and the response comes back through another. Stateful devices like Azure Firewall drop the response because they never saw the request. It often happens when you add UDRs to only one subnet, or when a VM has a public IP and also a route through the firewall. Fix it by making routes symmetric, for example by adding matching UDRs on both sides or using DNAT/SNAT on the firewall.

## 360: What is Azure Private Link Service?

Private Link Service lets **you** offer your own service (behind a Standard Load Balancer) to other customers or other VNets privately. Consumers create a private endpoint in their own VNet that connects to your service, even across tenants, without peering and with overlapping IP ranges allowed. SaaS providers use it to give customers private connectivity.

## 361: How do you make a whole PaaS solution private (no public endpoints)?

- App Service / Functions: private endpoint for inbound, VNet integration for outbound, public access off.
- Storage, SQL, Cosmos DB, Key Vault, Service Bus, ACR: private endpoints, public access off.
- Front Door Premium with Private Link origins, or Application Gateway in the VNet, as the only public entry.
- Private DNS zones linked to the VNets.
- CI/CD runs from self-hosted agents in the VNet (or managed DevOps pools / GitHub-hosted runners with VNet injection).
- Admin access through Bastion or VPN.

Remember the deploy step: tools like `az webapp deploy` need network access to the SCM site.

## 362: How do Azure Front Door caching and origin shielding work?

Front Door caches responses at edge locations based on cache rules, query string behavior and the origin's `Cache-Control` headers. Each edge location requests from the origin on a miss. To reduce load on the origin, Front Door uses a tiered cache: some edge sites fetch from regional cache layers first. You can purge content by path, use cache keys carefully (include only needed query params), and use compression. Don't cache personalized responses.

## 363: How do you protect an API against DDoS attacks on Azure?

- **Azure DDoS infrastructure protection** is on by default for all Azure public IPs.
- **Azure DDoS Network Protection** or **IP Protection** adds tuned mitigation for your public IPs, alerts, reports and cost protection.
- Front Door and Application Gateway with WAF absorb layer 7 attacks: rate limiting rules, geo-filtering, bot protection.
- APIM rate limits per key or IP.
- Autoscale with a max limit so an attack doesn't cause unlimited cost.

## 364: How does distributed tracing work across Azure services?

Each request gets a trace ID that is passed along in the W3C `traceparent` header on HTTP calls and in message properties for Service Bus and Event Hubs. The OpenTelemetry instrumentation creates spans for incoming requests, outgoing dependencies and message handling, all with the same trace ID. Application Insights puts them together into the end-to-end transaction view and the application map. You need instrumentation in every service and the same Application Insights resource (or a workspace-based setup that can query across them).

## 365: How do you control Application Insights and Log Analytics costs?

- Use **sampling** (fixed-rate or rate-limited) to keep a percentage of telemetry; keep 100% of failures where possible.
- Lower log levels in production, drop noisy dependencies or health checks with OpenTelemetry processors.
- Use **DCR transformations** to filter rows and columns before ingestion.
- Use **Basic** or **Auxiliary** log tables for verbose logs you rarely query; they cost much less to ingest.
- Set daily caps as a safety net, and use commitment tiers for big, steady ingestion.
- Set retention per table and archive old data.

## 366: What is the difference between Analytics, Basic and Auxiliary logs in Log Analytics?

- **Analytics logs:** full KQL, alerts, best performance, highest ingestion cost.
- **Basic logs:** cheaper ingestion, limited KQL, pay per query, short interactive retention. Good for verbose debug logs.
- **Auxiliary logs:** cheapest, for very high-volume data you keep for auditing or occasional investigation, with slower queries.

You set the plan per table.

## 367: How do you define and monitor SLOs for an Azure app?

1. Pick **SLIs** that match user experience, like "percentage of requests under 500 ms" or "successful checkout rate".
2. Set **SLOs**, like 99.9% of requests succeed over 30 days.
3. Calculate them from Application Insights or Front Door logs with KQL.
4. Alert on **error budget burn rate** (how fast you are using up the allowed failures), not just on single spikes.
5. Show them in a workbook or Azure Managed Grafana dashboard.

```kusto
AppRequests
| where TimeGenerated > ago(30d)
| summarize total = count(), good = countif(Success and DurationMs < 500)
| extend sli = 100.0 * good / total
```

## 368: What is Azure Managed Grafana and Azure Monitor managed service for Prometheus?

**Managed Prometheus** collects Prometheus metrics from AKS and other sources into an Azure Monitor workspace without running Prometheus servers yourself. **Azure Managed Grafana** is a hosted Grafana with Entra ID sign-in and built-in data sources for Azure Monitor, Prometheus, Log Analytics and Data Explorer. Together they are the standard monitoring setup for AKS.

## 369: How would you troubleshoot intermittent 502 errors from Application Gateway?

1. Check **backend health** in the portal: are probes failing? Check probe path, host name and expected status codes.
2. Check if the backend's TLS certificate matches what the gateway expects (trusted root, SNI host name).
3. Look at access logs for `serverStatus` and `serverResponseLatency`. If the backend is slower than the request timeout (default 20 seconds), you get 502.
4. Check NSG and UDR on the gateway subnet; it needs certain inbound ports (65200-65535 for v2) and must not route probes through a firewall.
5. Check backend app logs for crashes or restarts and whether there are enough instances.

## 370: How would you troubleshoot high latency in a Node.js API on App Service?

- **Application Insights:** check the end-to-end transaction view: is time spent in the app or in dependencies (SQL, Cosmos, external API)?
- Look for cold starts after deployments or scale-out, and turn on health check and warm-up.
- Check CPU and memory per instance; Node.js is single-threaded, so one busy CPU-bound request blocks others. Use clustering (PM2) or more instances.
- Check for SNAT exhaustion and missing keep-alive.
- Check database DTU/RU usage, slow queries and connection pool limits.
- Use the **App Service diagnostics** and profiler, or attach a profiler over SSH.
- Check if the app and database are in the same region.

## 371: What is Azure App Service Environment (ASE)?

ASE v3 is a single-tenant deployment of App Service inside your VNet. It runs on the Isolated v2 tier and gives you full network isolation, internal load balancer options, very high scale and dedicated hardware. It's used by companies with strict isolation or compliance rules. It costs more than regular App Service with private endpoints and VNet integration, which is enough for many cases.

## 372: When would you choose Azure SQL Managed Instance over Azure SQL Database?

Choose Managed Instance when you're moving an existing SQL Server app that uses features Azure SQL Database doesn't support well: SQL Agent jobs, cross-database queries and transactions, CLR, Service Broker, linked servers, Database Mail, or you need near 100% compatibility. It's deployed into a VNet subnet. For new cloud-native apps, Azure SQL Database is usually simpler and cheaper.

## 373: How do you migrate an on-premises Node.js + PostgreSQL app to Azure?

1. **Assess:** dependencies, file system usage, sessions, background jobs, config.
2. **App:** containerize it and deploy to Container Apps or App Service; move config to app settings / App Configuration and secrets to Key Vault; make it stateless (sessions to Redis, files to Blob Storage).
3. **Database:** create Azure Database for PostgreSQL Flexible Server; migrate with the Azure Database Migration Service or `pg_dump`/`pg_restore` for small databases, or logical replication for minimal downtime.
4. **Network:** private endpoints, VNet integration.
5. **Monitoring:** OpenTelemetry to Application Insights.
6. **Cutover:** sync data, switch DNS, keep a rollback plan.

## 374: What are the main features of Azure Database for PostgreSQL Flexible Server you should know?

- Zone-redundant high availability with a standby replica in another zone.
- Read replicas, including in other regions.
- Built-in **PgBouncer** connection pooling.
- Entra ID authentication.
- Extensions like PostGIS, pgvector and pg_cron.
- Stop/start to save money in dev/test.
- Private access through VNet injection or private endpoints.
- Point-in-time restore and geo-redundant backups.

## 375: How do you implement retrieval-augmented generation (RAG) on Azure?

1. **Ingest:** load documents from Blob Storage, split them into chunks, create embeddings with an embedding model from Microsoft Foundry.
2. **Index:** store chunks and vectors in Azure AI Search (or Cosmos DB / PostgreSQL with vector search).
3. **Query:** embed the user's question, run hybrid (keyword + vector) search with semantic ranking, take the top chunks.
4. **Generate:** send the chunks and question to a chat model with instructions to answer only from the sources and cite them.
5. Add content safety, evaluation (groundedness, relevance) and access control (filter results by the user's permissions).

## 376: How do you call an Azure OpenAI deployment from Node.js with Entra ID auth?

Use the official `openai` package with a token provider from `@azure/identity`.

```js
const { AzureOpenAI } = require("openai");
const {
  DefaultAzureCredential,
  getBearerTokenProvider,
} = require("@azure/identity");

const azureADTokenProvider = getBearerTokenProvider(
  new DefaultAzureCredential(),
  "https://cognitiveservices.azure.com/.default",
);

const client = new AzureOpenAI({
  endpoint: "https://my-foundry.openai.azure.com",
  azureADTokenProvider,
  apiVersion: "2024-10-21",
});

const result = await client.chat.completions.create({
  model: "gpt-4o-mini", // your deployment name
  messages: [
    { role: "user", content: "Summarize Azure Front Door in one sentence." },
  ],
});
console.log(result.choices[0].message.content);
```

The identity needs a role like "Cognitive Services OpenAI User" (or the newer Foundry User role).

## 377: How do you handle quotas and scaling for Azure OpenAI in production?

- Quotas are set as **tokens per minute (TPM)** per model per region per subscription; requests above the limit get 429.
- Use **global** or **data zone** deployments for higher limits and automatic routing across regions.
- Use **provisioned throughput units (PTU)** for predictable latency and capacity on steady workloads, and spill over to pay-as-you-go deployments.
- Put **API Management** in front as an AI gateway: load balance across deployments, token rate limits per client, semantic caching and token usage logging.
- Retry with backoff and set `max_tokens` sensibly.

## 378: What is the "AI gateway" in Azure API Management?

It's a set of APIM features for managing access to AI model endpoints: token-based rate limits (`llm-token-limit`), emitting token metrics per consumer (`llm-emit-token-metric`), semantic caching with an embeddings model and Redis, load balancing and circuit breakers across several model backends, and content safety checks. It lets many teams share model capacity fairly and see who uses what.

## 379: How do you secure a public storage-backed file download feature for authenticated users only?

- Keep the container private.
- Users call your API, which checks their permissions.
- The API returns a short-lived **user delegation SAS** URL with read-only permission for that one blob, or streams the file itself.
- Serve through Front Door if you need caching (but don't cache per-user content publicly).
- Log access and set short expiry (minutes).

This avoids putting large file traffic through the API while keeping access controlled.

## 380: Design a file upload and processing pipeline on Azure.

1. The client asks the API for an upload URL; the API returns a short-lived user delegation SAS for `uploads/<id>`.
2. The client uploads directly to Blob Storage.
3. **Event Grid** fires `BlobCreated` and sends it to a Service Bus queue (for buffering and retries).
4. A Function or Container Apps job reads the queue, scans the file (Defender for Storage malware scanning), resizes/converts it, and writes results to a `processed` container.
5. Metadata goes into Cosmos DB or SQL; the client gets notified through Web PubSub or polling.
6. Lifecycle rules delete raw uploads after N days.

This keeps the API light, scales with load and handles failures with dead-lettering.

## 381: Design a URL shortener on Azure that can handle high read traffic.

- **API:** Container Apps or Functions to create short links (generate a base62 ID from a counter or random bytes, check for collisions).
- **Storage:** Cosmos DB with `id = shortCode` as the partition key, so redirects are point reads (~1 RU).
- **Cache:** Azure Managed Redis for hot links.
- **Redirects:** Front Door in front with caching of 301/302 responses for popular links.
- **Analytics:** send click events to Event Hubs and process them asynchronously (Stream Analytics or Fabric), so redirects stay fast.
- **Multi-region:** Cosmos DB replicated to several regions, Front Door routing to the nearest one.

## 382: How would you design an order processing system with Azure messaging?

- The API validates the order, saves it with status `Pending` and an outbox record, and returns 202.
- The outbox publisher sends `OrderPlaced` to a Service Bus **topic**.
- Subscriptions: `payments`, `inventory`, `notifications`, each with its own consumer.
- Each consumer is idempotent, uses peek-lock, and publishes its result events (`PaymentCompleted`, `StockReserved`).
- A **saga** (Durable Functions orchestrator or a state machine in the order service) tracks the steps and runs compensating actions if a step fails, like refunding payment when stock is not available.
- DLQs are monitored and alerts fire on growth.

## 383: How do you implement the saga pattern with Durable Functions?

The orchestrator calls each step as an activity and catches failures to run compensations in reverse order.

```js
df.app.orchestration("orderSaga", function* (context) {
  const order = context.df.getInput();
  const done = [];
  try {
    yield context.df.callActivity("reserveStock", order);
    done.push("reserveStock");
    yield context.df.callActivity("chargePayment", order);
    done.push("chargePayment");
    yield context.df.callActivity("createShipment", order);
    return "completed";
  } catch (err) {
    if (done.includes("chargePayment"))
      yield context.df.callActivity("refundPayment", order);
    if (done.includes("reserveStock"))
      yield context.df.callActivity("releaseStock", order);
    return "compensated";
  }
});
```

Activities must be idempotent because they can be retried.

## 384: What are the limits and gotchas of Azure Functions HTTP triggers?

- An HTTP-triggered function must respond within 230 seconds because of the Azure load balancer idle timeout, no matter the function timeout or plan. Use the async HTTP pattern (Durable Functions) for long work.
- Request body size is limited (100 MB by default).
- Scale-out takes time, so sudden spikes can see cold starts.
- Keys (`function`, `admin`) are not real user authentication; use Easy Auth, APIM or token validation.
- Each HTTP function shares the instance with others in the app, so heavy functions affect light ones.

## 385: How do you protect downstream systems from Azure Functions scaling too fast?

- Set the **maximum instance count** (Flex Consumption `maximumInstanceCount`, or `functionAppScaleLimit` on other plans).
- Limit per-instance concurrency (`maxConcurrentCalls` for Service Bus, batch sizes for queues, `maxConcurrentRequests` for HTTP).
- Put a queue in front of the slow system so work is buffered.
- Use connection pooling with a limited pool size.
- Use a circuit breaker or rate limiter in code.

## 386: How do you share code and configuration between many Function apps or microservices without coupling them?

- Share libraries as versioned npm packages (Azure Artifacts or GitHub Packages), not shared source folders.
- Use **App Configuration** for shared settings with labels per environment.
- Use contracts (JSON Schema, OpenAPI, AsyncAPI) for messages and APIs, and version them.
- Use common IaC modules (Bicep registry or Terraform modules) for consistent infrastructure.
- Keep data private to each service; integrate through APIs and events, not a shared database.

## 387: How does Azure handle platform maintenance on VMs, and how do you reduce its impact?

Most host updates use memory-preserving maintenance that pauses the VM for a few seconds. Some need a reboot. Azure sends **Scheduled Events** through the instance metadata service a few minutes before, so your app can drain traffic. To reduce impact:

- Run at least two instances across availability zones or availability sets.
- Use **maintenance configurations** to control when updates happen (for dedicated hosts and some VM sizes).
- Listen to Scheduled Events and remove the VM from the load balancer before maintenance.

```bash
curl -H Metadata:true "http://169.254.169.254/metadata/scheduledevents?api-version=2020-07-01"
```

## 388: What is the Azure Instance Metadata Service (IMDS)?

IMDS is a REST endpoint at `169.254.169.254` available from inside VMs and some other compute. It gives information about the instance (size, region, tags, network), scheduled events and **managed identity tokens**. It's only reachable from inside the VM. Because it can hand out tokens, protect it from SSRF attacks: requests need the `Metadata: true` header, and your app should never forward user-controlled URLs to internal addresses.

## 389: How do you protect against SSRF attacks that target managed identity tokens?

- Validate and allowlist outbound URLs; never fetch arbitrary user-provided URLs.
- Block requests to `169.254.169.254` and other internal ranges in your HTTP client.
- Run with least-privilege identities so a stolen token can't do much.
- On App Service and Functions, the identity endpoint uses a secret header (`X-IDENTITY-HEADER`), which helps, but don't rely on it alone.
- Monitor managed identity sign-ins from unexpected places.

## 390: How do you handle long-running operations (LROs) in the Azure SDKs?

Operations like creating a VM or copying a large blob return immediately with a **poller**. You can wait until it finishes, check progress or save its state to resume later.

```js
const { ComputeManagementClient } = require("@azure/arm-compute");

const client = new ComputeManagementClient(
  new DefaultAzureCredential(),
  subscriptionId,
);
const poller = await client.virtualMachines.beginStart("rg-demo", "vm-web-01");
await poller.pollUntilDone();
```

Under the hood, Azure returns `202 Accepted` with an `Azure-AsyncOperation` or `Location` header that you poll.

## 391: What are ETags and how do you use them for optimistic concurrency in Azure?

Most Azure data services (Blob Storage, Cosmos DB, Table Storage, App Configuration) return an **ETag** with each item. When updating, you send the ETag back with `If-Match`. If someone else changed the item since you read it, the ETag no longer matches and the service returns **412 Precondition Failed**, so you can reload and retry instead of overwriting their change.

```js
const { resource, etag } = await container.item("order-1", "cust-1").read();
resource.status = "shipped";
await container.item("order-1", "cust-1").replace(resource, {
  accessCondition: { type: "IfMatch", condition: etag },
});
```

## 392: How do you implement a distributed lock on Azure?

- **Blob leases:** acquire a lease (15-60 seconds or infinite) on a blob; only the holder can write it. Renew it while working. Used by Functions and Terraform state.
- **Redis:** `SET key value NX PX 30000`, with care about failover edge cases (Redlock has known issues).
- **Cosmos DB / SQL:** conditional insert with a unique key and TTL.

Always use expiry so a crashed holder doesn't block forever, and design for the case where two holders briefly overlap (fencing tokens).

## 393: What are the main egress (data transfer) cost traps in Azure?

- Data going out to the internet is charged per GB; data coming in is free.
- Traffic between regions is charged, including geo-replication and cross-region calls from chatty services.
- Traffic between availability zones can also be charged in some cases.
- NAT gateway and Azure Firewall charge per GB processed.
- Private endpoints charge per GB in and out.
- Log shipping to another region adds cost.

Keep chatty services in the same region, cache at the edge with Front Door, and compress responses.

## 394: How do you implement FinOps practices in Azure?

- **Visibility:** tags for owner, cost center and environment; Cost Management views and exports to storage or Fabric.
- **Accountability:** budgets per team with alerts, showback or chargeback reports.
- **Optimization:** regular reviews of Advisor recommendations, rightsizing, reservations and savings plans with utilization tracking, scheduling dev resources off.
- **Governance:** policies that block expensive SKUs in dev, require tags and limit regions.
- **Unit economics:** measure cost per customer or per transaction, not just total spend.

## 395: How do you decide between reservations and savings plans?

- **Reservations:** biggest discount, but locked to a specific resource type and region (with some size flexibility). Good for stable, known workloads like a SQL database or VMs that won't change family or region.
- **Savings plans:** a bit less discount, but apply to any eligible compute in any region automatically. Good when workloads move between VM families, regions or services.

Many companies combine them: reservations for the stable base, a savings plan for the rest, and pay-as-you-go for peaks.

## 396: What is subscription vending?

Subscription vending is an automated process for creating new subscriptions for teams with all the standard setup already applied: placed in the right management group, connected to the hub network, budgets, RBAC for the team, policies, tags and logging. Teams request a subscription (for example through a pull request or form), and a pipeline using Bicep or Terraform modules creates it. It gives teams speed while keeping governance.

## 397: How do you manage policy as code?

- Store policy definitions, initiatives and assignments in git as JSON/Bicep/Terraform.
- Deploy them with a pipeline to management groups, with `what-if` in pull requests.
- Start new policies with the **Audit** effect, check compliance, then move to **Deny**.
- Use **exemptions** with expiry dates instead of disabling policies.
- Tools like Enterprise Policy as Code (EPAC) help manage large sets of policies.

## 398: What is the difference between Azure Policy and Azure Blueprints?

Blueprints packaged policies, role assignments, ARM templates and resource groups into one versioned definition for setting up subscriptions. **Azure Blueprints was deprecated and retired in July 2026**, and Microsoft recommends **template specs** and **deployment stacks** together with Azure Policy instead. You may still see Blueprints in older docs and scripts that need to be migrated.

## 399: What are template specs?

A template spec stores an ARM template or Bicep file as a versioned Azure resource. Teams with access can deploy it by its resource ID, without needing the source repo. It's a way to share approved infrastructure patterns inside a company. The **Bicep public/private module registry** (an ACR) is another way to share modules.

```bash
az ts create -g rg-templates -n webapp-standard -v 1.0.0 --template-file webapp.bicep
```

## 400: How does Azure Resource Manager handle dependencies and parallelism in a Bicep deployment?

ARM builds a dependency graph from symbolic references in your Bicep (for example `storage.id` used in another resource) and deploys independent resources in parallel. You rarely need explicit `dependsOn`. Loops (`for`) also deploy in parallel by default; use the `@batchSize(n)` decorator to deploy items in smaller groups, for example to avoid throttling or to roll out in waves.

```bicep
@batchSize(2)
resource apps 'Microsoft.Web/sites@2023-12-01' = [for name in appNames: {
  name: name
  location: location
  properties: { serverFarmId: plan.id }
}]
```

## 401: How do you test Bicep and other infrastructure code?

- **Linting:** the Bicep linter runs on build, with rules in `bicepconfig.json`.
- **Validation:** `az deployment group validate` checks the template against ARM without deploying.
- **what-if** in pull requests to review changes.
- **Policy checks:** tools like PSRule for Azure check templates against Well-Architected rules before deployment.
- **Integration tests:** deploy to a temporary resource group, run smoke tests, then delete it.
- Keep environments in sync by deploying the same templates with different parameter files.

## 402: How do you handle configuration drift between your IaC and what's actually in Azure?

- Make IaC the only way to change production: limit Contributor access, use deployment stacks with deny settings.
- Run `what-if` or `terraform plan` on a schedule and alert when it shows changes nobody planned.
- Use Azure Policy to block or audit changes outside the rules.
- Review the activity log for manual changes.
- When drift is found, either update the code to match (if the change was right) or redeploy to remove it.

## 403: What is the blast radius concept and how do you limit it in Azure?

The blast radius is how much of your system is affected when something goes wrong: a bad deployment, an outage, a leaked credential or a mistaken delete. Ways to limit it:

- Separate subscriptions per workload and environment.
- Deployment stamps and cells.
- Gradual rollouts (rings, canary, region by region).
- Separate identities per service with least privilege.
- Availability zones and multiple regions.
- Resource locks and soft delete on critical data.

## 404: How would you roll out a change safely across many regions?

Use **safe deployment practices** like Microsoft does internally:

1. Deploy to a canary or test region first.
2. Then a small production region with low traffic.
3. Wait and watch health signals (error rates, latency, alerts) for a bake time.
4. Continue region by region, or in waves, never all regions at once, and never both regions of a pair at the same time.
5. Automate rollback when health checks fail.

GitHub Actions environments with approvals, or Azure Pipelines stages, can model these waves.

## 405: What is the Retry pattern vs the Circuit Breaker pattern, and how do they work together?

- **Retry:** try again after a short wait when an error is likely temporary (429, 503, timeouts).
- **Circuit breaker:** after many failures in a row, stop calling the failing service for a while and fail fast, then test with a few requests before closing the circuit again.

Use both: retries handle short blips, and the circuit breaker stops retries from making a long outage worse. Set a total timeout so retries don't keep a request waiting too long.

## 406: What is the Queue-Based Load Leveling pattern and when do you use it on Azure?

Put a queue (Service Bus or Storage Queue) between the part that receives work and the part that processes it. Spikes go into the queue, and workers process at a steady rate. This protects databases and APIs from sudden load and lets you scale workers based on queue length (KEDA, Functions). Use it when work doesn't need an immediate response, like order processing, emails or reports.

## 407: What is the Claim-Check pattern?

Messages in Service Bus have size limits (256 KB on Standard). With claim check, you store the large payload in Blob Storage and send only a reference (the blob URL or name) in the message. The receiver reads the blob. This keeps the message broker fast and cheap. Remember to clean up the blobs after processing, for example with lifecycle rules.

## 408: What is the Competing Consumers pattern?

Several instances of a worker read from the same queue, and each message goes to only one of them. This spreads the load and gives redundancy: if one worker dies, others keep going. Service Bus queues and Storage Queues support this. Messages can be processed out of order and possibly more than once, so workers must be idempotent.

## 409: What is the Valet Key pattern?

Instead of sending large files through your API, you give the client a token with limited access to the resource for a short time, like a SAS URL for one blob. The client talks to storage directly. This reduces load and cost on your servers. The token should have the minimum permissions and a short expiry, and the API should validate the request first.

## 410: What is the Strangler Fig pattern and how do you apply it when moving to Azure?

You replace a legacy system piece by piece. A facade (like Front Door, Application Gateway or API Management) sits in front and routes each route or feature either to the old system or the new service on Azure. Over time more routes move to new services until the old system can be turned off. It avoids a risky "big bang" rewrite.

## 411: What is the Backends for Frontends (BFF) pattern and how would you host it on Azure?

A BFF is a separate back-end API for each type of client (web, mobile, partner), tailored to what that client needs. It combines calls to internal microservices, reduces chattiness and handles client-specific auth. On Azure you might host each BFF in Container Apps or App Service, with APIM in front for policies. For SPAs, the BFF can also keep tokens on the server side and use cookies, which is safer than storing tokens in the browser.

## 412: How do you secure a single-page app that calls APIs with Entra ID?

- Use MSAL.js with authorization code flow and PKCE.
- Request tokens with only the needed scopes for each API.
- Tokens are kept in memory or session storage, not local storage when possible.
- Set a strict Content Security Policy to reduce XSS risk, since XSS can steal tokens.
- The API validates tokens (issuer, audience, scopes).
- For higher security, use the BFF pattern so tokens never reach the browser.

## 413: What are Continuous Access Evaluation (CAE) and token lifetimes in Entra ID?

Access tokens from Entra ID usually live 60-90 minutes, and services trust them until they expire. With **Continuous Access Evaluation**, supporting services (like Exchange, SharePoint, Graph, and apps that opt in) get near real-time signals, such as a user being disabled, password changed or leaving a trusted location, and reject the token right away. CAE-capable clients get longer-lived tokens (up to 28 hours) because they can be revoked. Your own APIs can support CAE by handling claims challenges.

## 414: How does Conditional Access apply to workload identities?

With **Microsoft Entra Workload ID**, you can apply Conditional Access policies to service principals, for example blocking a service principal from signing in from outside known IP ranges, or blocking it when its risk is high. This limits damage if an app's credentials leak. It applies to single-tenant service principals, not managed identities.

## 415: What is a cross-tenant scenario in Azure and how do you handle access?

Examples: a SaaS provider accessing customer subscriptions, or a company with several tenants after acquisitions. Options:

- **Azure Lighthouse:** a provider manages resources in customer tenants with delegated RBAC, without guest accounts.
- **Multi-tenant app registrations:** the app is consented in each customer tenant.
- **B2B guest users** for people.
- **Cross-tenant sync** and **multi-tenant organization** features for companies with several tenants.
- Federated credentials can trust another tenant's managed identity for some cross-tenant workloads.

## 416: What is Azure Lighthouse?

Azure Lighthouse lets a service provider (or a central IT tenant) manage resources in other tenants. The customer delegates subscriptions or resource groups to groups in the provider's tenant with specific RBAC roles. Provider users work from their own tenant and see all customers in one place. All actions are logged in the customer's activity log. It's commonly used by managed service providers.

## 417: How would you design a secure CI/CD pipeline for production Azure deployments?

- Use OIDC federated credentials, no stored secrets.
- Use separate identities per environment, with production identity limited to the production subscription and trusted only from the protected branch or environment.
- Require pull request reviews, status checks, and environment approvals for production.
- Run lint, tests, IaC `what-if`, security scans (dependencies, containers, IaC) on every PR.
- Build once, sign and promote the same artifact through environments.
- Use private agents/runners for private-network deployments.
- Keep audit logs of who deployed what and when.

## 418: How do you sign and verify container images on Azure?

Use **Notation** (Notary Project) to sign images in ACR with a key stored in Key Vault, or use Trusted Signing. In AKS, use **Ratify** with Azure Policy (or the image integrity feature) to block images that aren't signed by a trusted key. Combine it with ACR vulnerability scanning in Defender for Containers and only allowing images from your own registries.

## 419: What does Defender for Containers do?

Defender for Containers protects AKS and other Kubernetes clusters, plus registries:

- Vulnerability scanning of images in ACR and running containers.
- Runtime threat detection on nodes and in the control plane (suspicious processes, crypto miners, privileged containers).
- Kubernetes posture recommendations and policy enforcement through Azure Policy for Kubernetes (Gatekeeper).
- Attack path analysis for container workloads.

## 420: How do you enforce Kubernetes security rules in AKS with Azure Policy?

The **Azure Policy add-on for AKS** uses OPA Gatekeeper. You assign built-in policies like "Kubernetes cluster should not allow privileged containers", "containers should only use allowed images", "must have CPU and memory limits" or "should not use the default namespace". They run as admission controllers that deny or audit bad workloads, and compliance shows up in Azure Policy. Built-in initiatives match the Kubernetes Pod Security Standards (baseline and restricted).

## 421: How do you handle stateful workloads on AKS?

- Use persistent volumes with Azure Disk (single pod, zone-bound) or Azure Files (shared, slower). **Azure Container Storage** gives more options, including local NVMe.
- Use StatefulSets, Pod Disruption Budgets and zone-aware storage classes (ZRS disks) so pods can move between zones.
- Back up with **AKS Backup** (Velero-based).
- For databases, prefer managed services (Azure SQL, PostgreSQL, Cosmos DB) unless you have a strong reason to run them in the cluster.

## 422: What is the Istio-based service mesh add-on for AKS, and when do you need a service mesh?

The add-on installs and manages Istio for you, including upgrades. A service mesh gives you mTLS between services, traffic splitting and retries, fine-grained authorization policies and detailed telemetry, without changing app code. You need it when you have many services with strict security (zero trust between pods) or advanced traffic rules. For a handful of services it adds a lot of complexity and resource overhead, so it's often not worth it.

## 423: How do you reduce cold start and image pull time in Container Apps and AKS?

- Keep images small: multi-stage builds, slim or distroless base images, fewer layers.
- Put the registry in the same region, use ACR Premium geo-replication for multi-region.
- Use **artifact streaming** in AKS to start containers before the full image is downloaded.
- Keep `minReplicas` at 1 or more for latency-sensitive apps.
- Speed up app startup (lazy load modules, avoid heavy work at start).
- Use readiness and startup probes correctly so traffic arrives only when the app is ready.

## 424: How do probes work in Azure Container Apps, and what happens if they're misconfigured?

Container Apps supports **startup**, **liveness** and **readiness** probes (HTTP or TCP). Startup probes give the app time to boot, readiness probes control if a replica gets traffic, and liveness probes restart stuck containers. If the liveness probe is too strict (short timeout, checks a slow dependency), healthy containers get restarted again and again, which looks like a crash loop. If readiness is missing, traffic can hit replicas before they're ready, causing errors after each deployment or scale-out.

## 425: How do you design Cosmos DB data models differently from SQL?

- Model around **access patterns**, not normalization.
- **Embed** data that is read together and has a bounded size (order with its line items).
- **Reference** data that is large, unbounded or changes independently.
- **Denormalize** and duplicate where it saves queries; keep copies in sync with the change feed.
- Put different entity types in one container with the same partition key when they're queried together (like `customerId`), using a `type` property.
- Keep items small; the max item size is 2 MB.

## 426: How does Cosmos DB guarantee availability in a single region and across regions?

In each region, data is stored in physical partitions, and each partition is a replica set of four replicas spread across fault domains (and across zones if zone redundancy is on). Writes need a majority quorum. Across regions, data replicates according to the consistency level. With **service-managed failover** (or per-partition automatic failover), Cosmos promotes another region when the write region goes down. With multi-region writes, every region accepts writes, which gives the best availability SLA (99.999%).

## 427: What are hierarchical partition keys in Cosmos DB?

Hierarchical partition keys let you use up to three levels, like `/tenantId`, `/userId`, `/sessionId`. Data for one big tenant can spread over many physical partitions (beyond the 20 GB limit of a logical partition), while queries that filter by `tenantId` still only go to the partitions that hold that tenant. It solves the classic multi-tenant problem where a few tenants are much bigger than the rest.

## 428: How do you do vector search in Cosmos DB?

Cosmos DB for NoSQL supports storing embeddings in items and querying them with vector indexes (`flat`, `quantizedFlat`, `diskANN`). You define a vector embedding policy on the container and a vector index, then query with `VectorDistance`.

```sql
SELECT TOP 5 c.id, c.title, VectorDistance(c.embedding, @queryVector) AS score
FROM c
ORDER BY VectorDistance(c.embedding, @queryVector)
```

It keeps data and vectors in one store, which is handy for RAG apps that already use Cosmos DB. It also supports full-text and hybrid search.

## 429: How do you choose the right database on Azure for a new service?

- **Relational data, transactions, complex queries:** Azure SQL Database or PostgreSQL Flexible Server.
- **Global scale, low latency, flexible schema, known access patterns:** Cosmos DB for NoSQL.
- **Existing MongoDB code:** Cosmos DB for MongoDB (vCore or RU).
- **Caching, sessions, counters:** Azure Managed Redis.
- **Time-series and log analytics:** Azure Data Explorer or Fabric Real-Time Intelligence.
- **Search:** Azure AI Search.
- **Files and objects:** Blob Storage.

Consider team skills, cost model (RU vs vCore), consistency needs and how the data will grow.

## 430: How do you migrate a large production database to Azure with minimal downtime?

1. Create the target (Azure SQL, PostgreSQL Flexible Server, etc.) with the right size.
2. Do an initial full load (Azure Database Migration Service, backup/restore, or native tools).
3. Keep the target in sync with ongoing replication: transactional replication or the Managed Instance link for SQL Server, logical replication for PostgreSQL, change data capture.
4. Test the app against the target, including performance.
5. During a short window: stop writes, let replication catch up, switch connection strings, and validate.
6. Keep the source as a fallback for a while.

## 431: How do you make Azure Key Vault highly available and avoid it becoming a bottleneck?

Key Vault is replicated within the region and to the paired region automatically, and fails over in read-only mode during a regional outage. It has **throttling limits** per vault (a number of operations per 10 seconds). To avoid problems:

- Cache secrets in the app and refresh periodically instead of reading on every request.
- Use Key Vault references in App Service (cached by the platform).
- Use one vault per app per environment per region, which also limits blast radius.
- Handle 429 with backoff.

## 432: What is the difference between Azure Storage account failover and the old geo-redundancy behavior?

With GRS/GZRS, data is copied async to the secondary region. In a regional outage you can start a **customer-managed failover**: the secondary becomes the primary and the DNS of the endpoints is updated. Data that hadn't replicated yet (check **Last Sync Time**) is lost. After failover the account becomes LRS in the new primary, and you need to set geo-redundancy again. There is also **planned failover** for testing DR, which doesn't lose data. Microsoft can also do a failover in a major disaster, but you shouldn't rely on it.

## 433: How do you protect backups from ransomware in Azure?

- Use **immutable vaults** so backups can't be deleted or changed before they expire.
- Keep **soft delete** on (enhanced soft delete can be made always-on).
- Use **multi-user authorization** with Resource Guard, so a second person must approve dangerous actions like disabling soft delete.
- Store backups in a separate subscription with different admins.
- Use cross-region restore.
- Test restores regularly.

## 434: What's the difference between high availability and disaster recovery?

**High availability** keeps the system running through small, common failures inside a region: a VM crash, a disk failure, a zone outage. It uses redundancy like availability zones and multiple instances, and failover is automatic and fast. **Disaster recovery** is about recovering from large events, like a whole region going down or data corruption. It uses another region, backups and runbooks, and usually takes longer. You need both, and backups protect against things replication can't, like accidental deletes, because replication copies the mistake too.

## 435: How do you test that your disaster recovery plan actually works?

- Schedule regular DR drills: fail over to the secondary region and run real traffic or synthetic tests.
- Use Site Recovery **test failovers** in an isolated network.
- Do planned failovers for SQL failover groups, storage and Cosmos DB in non-production first.
- Use **Chaos Studio** to inject faults (zone down, dependency failure).
- Measure actual RTO and RPO and compare them to targets.
- Keep runbooks up to date and automate as much as possible.

## 436: How would you design logging and monitoring for 50 microservices across several subscriptions?

- One central **Log Analytics workspace** per region or per environment (in the management subscription), or a small number of them, with resource-context RBAC so teams see their own data.
- All services use the OpenTelemetry distro and send to workspace-based Application Insights resources.
- Platform logs go there through diagnostic settings enforced by Azure Policy (DINE).
- AKS uses Container Insights and Managed Prometheus/Grafana.
- Standard dashboards and alerts per service, defined in IaC.
- Cost control with sampling, table plans and retention per table.

## 437: How do you correlate logs from an Azure Function triggered by Service Bus with the HTTP request that started it?

The sender's OpenTelemetry instrumentation adds a `Diagnostic-Id` / `traceparent` application property to the Service Bus message. The Functions host and Service Bus SDK read it and continue the same trace, so in Application Insights the function execution appears in the same end-to-end transaction as the original request. If you send messages manually without instrumentation, set `traceparent` in the message's application properties yourself.

## 438: What happens when an Azure region has an outage and what can you do in advance?

During a regional outage, services in that region (and sometimes global control-plane operations) can be unavailable. Your options depend on preparation:

- Multi-region active-active or warm standby: Front Door shifts traffic automatically.
- Geo-replicated data: fail over SQL, storage and Cosmos DB.
- IaC and pipelines that can deploy to another region quickly, with **pre-approved quota** in that region.
- Don't depend on the failed region for things like DNS, Key Vault, container registry or the CI runners.
- Communication plan and Service Health alerts.

Capacity in nearby regions can be tight during big outages, so reservations or capacity reservations help.

## 439: What are on-demand capacity reservations?

A capacity reservation guarantees that a number of VMs of a specific size are available for you in a region or zone, without a time commitment. You pay for the reserved capacity whether you use it or not (reservation discounts can apply). It's used for DR plans and important events where you can't risk `AllocationFailed` errors when scaling.

## 440: How do you handle the "AllocationFailed" or "SkuNotAvailable" errors?

These mean Azure doesn't have capacity for that VM size in that region/zone right now, or the size isn't offered there for your subscription.

- Try another size in the same family or another zone.
- Use `az vm list-skus --location <region> --size <size>` to check availability and restrictions.
- Build flexibility in: VMSS Flexible with several sizes, AKS node auto-provisioning.
- Use capacity reservations for critical workloads.
- Request access for restricted SKUs through support.

## 441: How do you make Azure Functions or App Service handle a sudden 10x traffic spike?

- Pre-scale before known events (sales, launches) instead of relying on autoscale reacting.
- Use always-ready/pre-warmed instances (Flex Consumption, Premium) and set a high enough max instance count.
- Cache at the edge with Front Door and in Redis.
- Queue writes instead of processing them synchronously.
- Make sure downstream services (database RU/DTU, external APIs) can also take the load, or protect them with rate limits.
- Load test beforehand with Azure Load Testing to find the bottleneck.

## 442: Scenario: your Cosmos DB bill suddenly doubled. How do you investigate?

1. **Cost Management:** check whether the increase is RU/s throughput, storage, backups or extra regions.
2. **Metrics:** total request units by operation type and collection; check for spikes in a specific container.
3. **Diagnostic logs:** find the queries with the highest RU charge (`CDBQueryRuntimeStatistics`, `CDBDataPlaneRequests`).
4. Common causes: a new cross-partition query, a missing index causing scans, autoscale max raised, a new region added, an indexing policy change, or a bug writing in a loop.
5. Fix the query or index, add the partition key filter, cache, or lower the max RU/s.

## 443: Scenario: an App Service app slows down every day around the same time. What do you check?

- Scheduled jobs: backups, WebJobs, timer functions, index rebuilds or reports running at that time, on the same plan or on the database.
- Other apps on the same App Service plan using CPU or memory.
- Autoscale rules: does it scale in too early, or is the max too low?
- Database load at that time (DTU/RU charts, Query Store).
- Platform maintenance (check Resource Health and Service Health history).
- Traffic patterns (business hours in a different time zone).
- Memory leaks that build up until a daily restart.

## 444: Scenario: a developer accidentally committed a storage account key to a public GitHub repo. What do you do?

1. **Rotate the key immediately** (regenerate key1/key2), and update apps that legitimately used it. Assume it's already been used; bots scan GitHub within minutes.
2. Check storage logs and Defender for Storage alerts for unusual access, downloads or deletions.
3. Remove the key from the repo history (and invalidate any SAS tokens signed with it, which regenerating the key does).
4. Move apps to Entra ID auth with managed identities and turn off shared key access so this can't happen again.
5. Turn on GitHub secret scanning and push protection.

## 445: Scenario: a Service Bus queue keeps growing and consumers can't keep up. What do you do?

- Check consumer health: are they failing and retrying (high delivery count, DLQ growth) or just slow?
- Look at processing time per message and dependencies (database, APIs) in Application Insights.
- Scale out consumers (KEDA/Functions scaling), raise `maxConcurrentCalls` or prefetch, if downstream can handle it.
- Use batching for receives and database writes.
- Check if the namespace is throttled (Standard tier) and move to Premium or add messaging units.
- If one message type is expensive, split it into its own queue.
- If some messages are poison, make sure they dead-letter quickly instead of being retried many times.

## 446: Scenario: after enabling private endpoints on a storage account, your Function app can't start. Why?

The Function app uses the storage account (`AzureWebJobsStorage`) for its runtime and deployment package. After public access is turned off, the app can't reach it unless:

- The Function app has **VNet integration** into a subnet that can reach the private endpoints.
- Private endpoints exist for every sub-resource the app uses (blob, queue, table, and file if used).
- Private DNS zones for those sub-resources are linked to the VNet so names resolve to private IPs.
- For plans that use an Azure Files content share, `WEBSITE_CONTENTOVERVNET` is set (or use Flex Consumption, which doesn't use a file share).

## 447: Scenario: your team wants to move from App Service to AKS "because everyone uses Kubernetes". How do you respond?

Ask what problem AKS solves for them. AKS brings more control but also cluster upgrades, node management, networking, security hardening, monitoring and on-call work. If the app is a few web APIs, App Service or Container Apps give most of the benefits (containers, scaling, revisions) with much less work. AKS makes sense if they need things like custom operators, service mesh, specific Kubernetes tooling, very large scale, or portability across clouds, and have the skills to run it. A good middle step is Container Apps, since apps there are already containerized and could move to AKS later.

## 448: Scenario: you need to run a nightly job that takes 3 hours. Which Azure service would you use?

Not a regular Azure Function on the Consumption plan, because of its 10-minute maximum timeout. Good options:

- **Container Apps job** with a cron trigger: runs a container to completion, no time limit issues, pay only while it runs.
- **Durable Functions** if the work can be split into smaller activities (fan-out).
- **Azure Batch** if it's heavy parallel compute.
- **Data Factory or Fabric pipelines** for data movement and transformation.
- Functions on Flex Consumption or Premium (which allow longer or unbounded timeouts) if it must stay in Functions.

Make the job restartable with checkpoints, so a failure after 2 hours doesn't mean starting over.

## 449: Scenario: management wants to cut the Azure bill by 30% without hurting reliability. Where do you start?

1. Get visibility: break down cost by service, team and environment; find the top 10 cost items.
2. Quick wins: delete unused resources (orphaned disks, old snapshots, idle public IPs, empty App Service plans), turn off dev/test outside working hours.
3. Rightsizing: Advisor recommendations, oversized SQL/Cosmos throughput, overprovisioned AKS nodes.
4. Commitments: reservations and savings plans for the steady base load.
5. Architecture: autoscaling and scale to zero, storage tiers and lifecycle rules, Log Analytics ingestion reduction.
6. Licensing: Azure Hybrid Benefit.
7. Put budgets and regular reviews in place so savings stick.

## 450: Scenario: design the Azure architecture for a new e-commerce platform expected to grow fast.

- **Edge:** Azure Front Door Premium with WAF, caching static assets and product images, routing to two regions.
- **Front end:** Static Web Apps or Container Apps for a Next.js app.
- **APIs:** microservices (catalog, cart, orders, payments, users) on Container Apps, behind API Management.
- **Identity:** Entra External ID for customers, Entra ID for staff.
- **Data:** Cosmos DB for catalog and carts (partitioned by product/customer), Azure SQL or PostgreSQL for orders and payments (transactions), Azure Managed Redis for sessions and caching, AI Search for product search.
- **Messaging:** Service Bus topics for order events, Event Grid for blob events, Event Hubs for clickstream analytics.
- **Security:** managed identities everywhere, Key Vault, private endpoints, Defender for Cloud.
- **Operations:** Bicep/Terraform with GitHub Actions (OIDC), Application Insights with OpenTelemetry, SLO alerts, Chaos Studio and Load Testing before big sales.
- **Growth:** start in one region with zones, add the second region and deployment stamps as traffic grows.
