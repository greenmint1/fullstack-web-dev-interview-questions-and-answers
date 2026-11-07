# Terraform Interview Questions and Answers

_Last updated: November 5, 2026_

450 Terraform interview questions with answers, split into three levels: 150 easy, 150 moderate and 150 advanced.

The answers target Terraform 1.14 and 1.15 and use current features like `import`, `moved`, `removed` and `check` blocks, `terraform test`, ephemeral values, write-only arguments and S3 native state locking. Older approaches (DynamoDB locking, `terraform taint`, `null_resource`) are mentioned where you will still see them in real projects. Most examples use the AWS provider, but the ideas apply to any provider.

## Table of Contents

- [Easy Questions (1-150)](#easy-questions-1-150)
- [Moderate Questions (151-300)](#moderate-questions-151-300)
- [Advanced Questions (301-450)](#advanced-questions-301-450)

### Easy Questions (1-150)

- [1: What is Terraform?](#1-what-is-terraform)
- [2: What is infrastructure as code?](#2-what-is-infrastructure-as-code)
- [3: What language is Terraform configuration written in?](#3-what-language-is-terraform-configuration-written-in)
- [4: What does it mean that Terraform is declarative?](#4-what-does-it-mean-that-terraform-is-declarative)
- [5: What is a provider in Terraform?](#5-what-is-a-provider-in-terraform)
- [6: What is a resource?](#6-what-is-a-resource)
- [7: What is a data source?](#7-what-is-a-data-source)
- [8: What is the difference between a resource and a data source?](#8-what-is-the-difference-between-a-resource-and-a-data-source)
- [9: What is the Terraform state?](#9-what-is-the-terraform-state)
- [10: What are the main Terraform commands?](#10-what-are-the-main-terraform-commands)
- [11: What does terraform init do?](#11-what-does-terraform-init-do)
- [12: What does terraform plan do?](#12-what-does-terraform-plan-do)
- [13: What does terraform apply do?](#13-what-does-terraform-apply-do)
- [14: What does terraform destroy do?](#14-what-does-terraform-destroy-do)
- [15: What does terraform fmt do?](#15-what-does-terraform-fmt-do)
- [16: What does terraform validate do?](#16-what-does-terraform-validate-do)
- [17: What is the .terraform directory?](#17-what-is-the-terraform-directory)
- [18: What is the .terraform.lock.hcl file?](#18-what-is-the-terraformlockhcl-file)
- [19: Which files should be in .gitignore for a Terraform project?](#19-which-files-should-be-in-gitignore-for-a-terraform-project)
- [20: What is the terraform block?](#20-what-is-the-terraform-block)
- [21: What is required\_providers?](#21-what-is-required_providers)
- [22: How do version constraints work in Terraform?](#22-how-do-version-constraints-work-in-terraform)
- [23: What does required\_version do?](#23-what-does-required_version-do)
- [24: What is the Terraform Registry?](#24-what-is-the-terraform-registry)
- [25: What is a variable in Terraform?](#25-what-is-a-variable-in-terraform)
- [26: What are the ways to set variable values?](#26-what-are-the-ways-to-set-variable-values)
- [27: What is the order of precedence for variable values?](#27-what-is-the-order-of-precedence-for-variable-values)
- [28: What is a .tfvars file?](#28-what-is-a-tfvars-file)
- [29: What is an output value?](#29-what-is-an-output-value)
- [30: What is a local value?](#30-what-is-a-local-value)
- [31: What is the difference between variables, locals and outputs?](#31-what-is-the-difference-between-variables-locals-and-outputs)
- [32: What is a module?](#32-what-is-a-module)
- [33: What is the root module?](#33-what-is-the-root-module)
- [34: Where can modules come from?](#34-where-can-modules-come-from)
- [35: How do you pass values into a module and get values out of it?](#35-how-do-you-pass-values-into-a-module-and-get-values-out-of-it)
- [36: What is the standard file layout of a Terraform module?](#36-what-is-the-standard-file-layout-of-a-terraform-module)
- [37: Does the order of blocks or files matter in Terraform?](#37-does-the-order-of-blocks-or-files-matter-in-terraform)
- [38: How does Terraform know in which order to create resources?](#38-how-does-terraform-know-in-which-order-to-create-resources)
- [39: What is depends\_on?](#39-what-is-depends_on)
- [40: What are meta-arguments?](#40-what-are-meta-arguments)
- [41: What is count?](#41-what-is-count)
- [42: What is for\_each?](#42-what-is-for_each)
- [43: How do you create a resource only when a condition is true?](#43-how-do-you-create-a-resource-only-when-a-condition-is-true)
- [44: What is the lifecycle block?](#44-what-is-the-lifecycle-block)
- [45: What does prevent\_destroy do?](#45-what-does-prevent_destroy-do)
- [46: What does ignore\_changes do?](#46-what-does-ignore_changes-do)
- [47: What does create\_before\_destroy do?](#47-what-does-create_before_destroy-do)
- [48: What are the basic types in Terraform?](#48-what-are-the-basic-types-in-terraform)
- [49: How do you declare a variable with an object type?](#49-how-do-you-declare-a-variable-with-an-object-type)
- [50: How does string interpolation work?](#50-how-does-string-interpolation-work)
- [51: How do you write a multi-line string in Terraform?](#51-how-do-you-write-a-multi-line-string-in-terraform)
- [52: How do conditional expressions work?](#52-how-do-conditional-expressions-work)
- [53: What is a for expression?](#53-what-is-a-for-expression)
- [54: What is a splat expression?](#54-what-is-a-splat-expression)
- [55: Does Terraform have built-in functions?](#55-does-terraform-have-built-in-functions)
- [56: What is terraform console?](#56-what-is-terraform-console)
- [57: What do the merge, concat and lookup functions do?](#57-what-do-the-merge-concat-and-lookup-functions-do)
- [58: What is the difference between file and templatefile?](#58-what-is-the-difference-between-file-and-templatefile)
- [59: What are path.module, path.root and path.cwd?](#59-what-are-pathmodule-pathroot-and-pathcwd)
- [60: How do you write comments in Terraform?](#60-how-do-you-write-comments-in-terraform)
- [61: What does sensitive = true do on a variable?](#61-what-does-sensitive--true-do-on-a-variable)
- [62: How do sensitive outputs work?](#62-how-do-sensitive-outputs-work)
- [63: How do you validate input variables?](#63-how-do-you-validate-input-variables)
- [64: What does nullable = false do on a variable?](#64-what-does-nullable--false-do-on-a-variable)
- [65: What does terraform show do?](#65-what-does-terraform-show-do)
- [66: How do you see which resources are in the state?](#66-how-do-you-see-which-resources-are-in-the-state)
- [67: What is a backend?](#67-what-is-a-backend)
- [68: Why should teams use a remote backend?](#68-why-should-teams-use-a-remote-backend)
- [69: How do you configure the S3 backend?](#69-how-do-you-configure-the-s3-backend)
- [70: What is state locking?](#70-what-is-state-locking)
- [71: Should you commit the state file to Git?](#71-should-you-commit-the-state-file-to-git)
- [72: Why can the state file contain secrets?](#72-why-can-the-state-file-contain-secrets)
- [73: What is drift?](#73-what-is-drift)
- [74: What is a refresh-only plan?](#74-what-is-a-refresh-only-plan)
- [75: How do you force Terraform to recreate a resource?](#75-how-do-you-force-terraform-to-recreate-a-resource)
- [76: How do you bring an existing resource under Terraform management?](#76-how-do-you-bring-an-existing-resource-under-terraform-management)
- [77: Can Terraform generate the code for imported resources?](#77-can-terraform-generate-the-code-for-imported-resources)
- [78: What are workspaces?](#78-what-are-workspaces)
- [79: How do you use the current workspace name in your code?](#79-how-do-you-use-the-current-workspace-name-in-your-code)
- [80: What are provisioners?](#80-what-are-provisioners)
- [81: Why are provisioners called a last resort?](#81-why-are-provisioners-called-a-last-resort)
- [82: What is terraform\_data?](#82-what-is-terraform_data)
- [83: What is null\_resource?](#83-what-is-null_resource)
- [84: What is the random provider used for?](#84-what-is-the-random-provider-used-for)
- [85: How do you use the same provider with different settings, like two AWS regions?](#85-how-do-you-use-the-same-provider-with-different-settings-like-two-aws-regions)
- [86: How do providers get credentials?](#86-how-do-providers-get-credentials)
- [87: How do you debug Terraform?](#87-how-do-you-debug-terraform)
- [88: What other environment variables does Terraform use?](#88-what-other-environment-variables-does-terraform-use)
- [89: What is a resource address?](#89-what-is-a-resource-address)
- [90: What is the difference between an argument and a nested block?](#90-what-is-the-difference-between-an-argument-and-a-nested-block)
- [91: What is the timeouts block?](#91-what-is-the-timeouts-block)
- [92: What are default\_tags in the AWS provider?](#92-what-are-default_tags-in-the-aws-provider)
- [93: How is Terraform different from AWS CloudFormation?](#93-how-is-terraform-different-from-aws-cloudformation)
- [94: How is Terraform different from Ansible?](#94-how-is-terraform-different-from-ansible)
- [95: How is Terraform different from Pulumi?](#95-how-is-terraform-different-from-pulumi)
- [96: What is OpenTofu?](#96-what-is-opentofu)
- [97: What is the Terraform license?](#97-what-is-the-terraform-license)
- [98: What is HCP Terraform?](#98-what-is-hcp-terraform)
- [99: What is Terraform Enterprise?](#99-what-is-terraform-enterprise)
- [100: What does idempotent mean for Terraform?](#100-what-does-idempotent-mean-for-terraform)
- [101: What is immutable infrastructure and how does Terraform support it?](#101-what-is-immutable-infrastructure-and-how-does-terraform-support-it)
- [102: What is the difference between an in-place update and a replacement?](#102-what-is-the-difference-between-an-in-place-update-and-a-replacement)
- [103: What does the -target option do?](#103-what-does-the--target-option-do)
- [104: What does terraform graph do?](#104-what-does-terraform-graph-do)
- [105: What does terraform providers do?](#105-what-does-terraform-providers-do)
- [106: How do you add checksums for other platforms to the lock file?](#106-how-do-you-add-checksums-for-other-platforms-to-the-lock-file)
- [107: What does terraform login do?](#107-what-does-terraform-login-do)
- [108: What does -detailed-exitcode do?](#108-what-does--detailed-exitcode-do)
- [109: Which options are useful when running Terraform in CI?](#109-which-options-are-useful-when-running-terraform-in-ci)
- [110: What does -parallelism do?](#110-what-does--parallelism-do)
- [111: What happens if terraform apply fails halfway?](#111-what-happens-if-terraform-apply-fails-halfway)
- [112: How do you access elements of lists, maps and objects?](#112-how-do-you-access-elements-of-lists-maps-and-objects)
- [113: What does null mean in Terraform?](#113-what-does-null-mean-in-terraform)
- [114: Does Terraform convert types automatically?](#114-does-terraform-convert-types-automatically)
- [115: What do the length, join and split functions do?](#115-what-do-the-length-join-and-split-functions-do)
- [116: What does the format function do?](#116-what-does-the-format-function-do)
- [117: What does cidrsubnet do?](#117-what-does-cidrsubnet-do)
- [118: How do you write an IAM policy in Terraform without raw JSON strings?](#118-how-do-you-write-an-iam-policy-in-terraform-without-raw-json-strings)
- [119: What is the self object?](#119-what-is-the-self-object)
- [120: What is terraform.tfstate.backup?](#120-what-is-terraformtfstatebackup)
- [121: What is a moved block?](#121-what-is-a-moved-block)
- [122: What does "known after apply" mean in a plan?](#122-what-does-known-after-apply-mean-in-a-plan)
- [123: When does Terraform read data sources?](#123-when-does-terraform-read-data-sources)
- [124: What does terraform state rm do?](#124-what-does-terraform-state-rm-do)
- [125: What does terraform state mv do?](#125-what-does-terraform-state-mv-do)
- [126: What is the cloud block?](#126-what-is-the-cloud-block)
- [127: What is the provider plugin cache?](#127-what-is-the-provider-plugin-cache)
- [128: What happens if someone deletes a Terraform-managed resource by hand?](#128-what-happens-if-someone-deletes-a-terraform-managed-resource-by-hand)
- [129: How do you install Terraform and manage several versions?](#129-how-do-you-install-terraform-and-manage-several-versions)
- [130: What does the -chdir option do?](#130-what-does-the--chdir-option-do)
- [131: What are override files?](#131-what-are-override-files)
- [132: What naming conventions are common in Terraform?](#132-what-naming-conventions-are-common-in-terraform)
- [133: Why should variables and outputs have descriptions?](#133-why-should-variables-and-outputs-have-descriptions)
- [134: What do try and can do?](#134-what-do-try-and-can-do)
- [135: What does coalesce do?](#135-what-does-coalesce-do)
- [136: Why can't you pass a list directly to for\_each?](#136-why-cant-you-pass-a-list-directly-to-for_each)
- [137: What do keys and values do?](#137-what-do-keys-and-values-do)
- [138: What does flatten do?](#138-what-does-flatten-do)
- [139: What is the difference between element and index access?](#139-what-is-the-difference-between-element-and-index-access)
- [140: What does contains do?](#140-what-does-contains-do)
- [141: Why is using timestamp() in a resource a problem?](#141-why-is-using-timestamp-in-a-resource-a-problem)
- [142: What does terraform state pull do?](#142-what-does-terraform-state-pull-do)
- [143: How does a destroy-time provisioner work?](#143-how-does-a-destroy-time-provisioner-work)
- [144: How does Packer relate to Terraform?](#144-how-does-packer-relate-to-terraform)
- [145: What are the main block types in Terraform?](#145-what-are-the-main-block-types-in-terraform)
- [146: What is terraform-docs?](#146-what-is-terraform-docs)
- [147: What is TFLint?](#147-what-is-tflint)
- [148: Which checks do teams usually run in pre-commit hooks for Terraform?](#148-which-checks-do-teams-usually-run-in-pre-commit-hooks-for-terraform)
- [149: What does a typical Terraform workflow look like in a team?](#149-what-does-a-typical-terraform-workflow-look-like-in-a-team)
- [150: What are some basic Terraform best practices?](#150-what-are-some-basic-terraform-best-practices)

### Moderate Questions (151-300)

- [151: When should you use count and when for\_each?](#151-when-should-you-use-count-and-when-for_each)
- [152: What is the problem with count when you remove an item from the middle of a list?](#152-what-is-the-problem-with-count-when-you-remove-an-item-from-the-middle-of-a-list)
- [153: How do you switch a resource from count to for\_each without recreating it?](#153-how-do-you-switch-a-resource-from-count-to-for_each-without-recreating-it)
- [154: What is a dynamic block?](#154-what-is-a-dynamic-block)
- [155: When should you avoid dynamic blocks?](#155-when-should-you-avoid-dynamic-blocks)
- [156: How do you create resources for every combination of two lists?](#156-how-do-you-create-resources-for-every-combination-of-two-lists)
- [157: Can you use for\_each and count on modules?](#157-can-you-use-for_each-and-count-on-modules)
- [158: How do you pass a provider configuration to a child module?](#158-how-do-you-pass-a-provider-configuration-to-a-child-module)
- [159: What is configuration\_aliases?](#159-what-is-configuration_aliases)
- [160: Why shouldn't reusable modules contain provider blocks?](#160-why-shouldnt-reusable-modules-contain-provider-blocks)
- [161: How should you version your own modules?](#161-how-should-you-version-your-own-modules)
- [162: What is module composition?](#162-what-is-module-composition)
- [163: How do you organize code for several environments?](#163-how-do-you-organize-code-for-several-environments)
- [164: What is the terraform\_remote\_state data source?](#164-what-is-the-terraform_remote_state-data-source)
- [165: What are the downsides of terraform\_remote\_state and what are the alternatives?](#165-what-are-the-downsides-of-terraform_remote_state-and-what-are-the-alternatives)
- [166: What is partial backend configuration?](#166-what-is-partial-backend-configuration)
- [167: Can you use variables in the backend block?](#167-can-you-use-variables-in-the-backend-block)
- [168: How do you move state from one backend to another?](#168-how-do-you-move-state-from-one-backend-to-another)
- [169: What is the difference between -migrate-state and -reconfigure?](#169-what-is-the-difference-between--migrate-state-and--reconfigure)
- [170: How do you configure the Azure and Google Cloud backends?](#170-how-do-you-configure-the-azure-and-google-cloud-backends)
- [171: What workflows does HCP Terraform support?](#171-what-workflows-does-hcp-terraform-support)
- [172: What are variable sets in HCP Terraform?](#172-what-are-variable-sets-in-hcp-terraform)
- [173: What are run triggers in HCP Terraform?](#173-what-are-run-triggers-in-hcp-terraform)
- [174: What is the removed block?](#174-what-is-the-removed-block)
- [175: How do you import many resources at once?](#175-how-do-you-import-many-resources-at-once)
- [176: Why does a plan sometimes show changes right after an import?](#176-why-does-a-plan-sometimes-show-changes-right-after-an-import)
- [177: What is a check block?](#177-what-is-a-check-block)
- [178: What are preconditions and postconditions?](#178-what-are-preconditions-and-postconditions)
- [179: What is the difference between validation, preconditions, postconditions and check blocks?](#179-what-is-the-difference-between-validation-preconditions-postconditions-and-check-blocks)
- [180: What does replace\_triggered\_by do?](#180-what-does-replace_triggered_by-do)
- [181: What is terraform test?](#181-what-is-terraform-test)
- [182: What is the difference between command = plan and command = apply in a test?](#182-what-is-the-difference-between-command--plan-and-command--apply-in-a-test)
- [183: How do you mock providers in terraform test?](#183-how-do-you-mock-providers-in-terraform-test)
- [184: How do you test that a validation fails?](#184-how-do-you-test-that-a-validation-fails)
- [185: How do you run Terraform in GitHub Actions?](#185-how-do-you-run-terraform-in-github-actions)
- [186: How does OIDC authentication from CI to a cloud provider work?](#186-how-does-oidc-authentication-from-ci-to-a-cloud-provider-work)
- [187: Is it safe to pass a saved plan file between CI jobs?](#187-is-it-safe-to-pass-a-saved-plan-file-between-ci-jobs)
- [188: What is Atlantis?](#188-what-is-atlantis)
- [189: What is Infracost?](#189-what-is-infracost)
- [190: Which tools scan Terraform code for security issues?](#190-which-tools-scan-terraform-code-for-security-issues)
- [191: How do you handle secrets in Terraform?](#191-how-do-you-handle-secrets-in-terraform)
- [192: What do the sensitive and nonsensitive functions do?](#192-what-do-the-sensitive-and-nonsensitive-functions-do)
- [193: What are ephemeral resources?](#193-what-are-ephemeral-resources)
- [194: What are write-only arguments?](#194-what-are-write-only-arguments)
- [195: What are ephemeral variables and outputs?](#195-what-are-ephemeral-variables-and-outputs)
- [196: How do you use HashiCorp Vault with Terraform?](#196-how-do-you-use-hashicorp-vault-with-terraform)
- [197: How can you let AWS manage an RDS master password instead of Terraform?](#197-how-can-you-let-aws-manage-an-rds-master-password-instead-of-terraform)
- [198: How do you use a map of objects with for\_each?](#198-how-do-you-use-a-map-of-objects-with-for_each)
- [199: Why should you be careful with the any type?](#199-why-should-you-be-careful-with-the-any-type)
- [200: Why does a data source for the latest AMI cause instances to be replaced?](#200-why-does-a-data-source-for-the-latest-ami-cause-instances-to-be-replaced)
- [201: Why do resources with create\_before\_destroy often use name\_prefix?](#201-why-do-resources-with-create_before_destroy-often-use-name_prefix)
- [202: How do you roll out a new AMI to an autoscaling group without downtime?](#202-how-do-you-roll-out-a-new-ami-to-an-autoscaling-group-without-downtime)
- [203: How do you manage several AWS accounts from one configuration?](#203-how-do-you-manage-several-aws-accounts-from-one-configuration)
- [204: What is the problem with creating an EKS cluster and Kubernetes resources in the same configuration?](#204-what-is-the-problem-with-creating-an-eks-cluster-and-kubernetes-resources-in-the-same-configuration)
- [205: Why should you avoid depends\_on on modules?](#205-why-should-you-avoid-depends_on-on-modules)
- [206: What does the "Cycle" error mean and how do you fix it?](#206-what-does-the-cycle-error-mean-and-how-do-you-fix-it)
- [207: How do you speed up slow plans?](#207-how-do-you-speed-up-slow-plans)
- [208: What does -refresh=false do?](#208-what-does--refreshfalse-do)
- [209: What is Terragrunt?](#209-what-is-terragrunt)
- [210: What are the pitfalls of CLI workspaces for environments?](#210-what-are-the-pitfalls-of-cli-workspaces-for-environments)
- [211: How do you promote changes from dev to production?](#211-how-do-you-promote-changes-from-dev-to-production)
- [212: How do you read a plan as JSON?](#212-how-do-you-read-a-plan-as-json)
- [213: Why can't you use sensitive values as for\_each keys?](#213-why-cant-you-use-sensitive-values-as-for_each-keys)
- [214: What causes "Invalid for\_each argument" with values that are known after apply?](#214-what-causes-invalid-for_each-argument-with-values-that-are-known-after-apply)
- [215: How do template directives and strip markers work?](#215-how-do-template-directives-and-strip-markers-work)
- [216: How do regex and regexall work?](#216-how-do-regex-and-regexall-work)
- [217: What does the replace function do?](#217-what-does-the-replace-function-do)
- [218: What does zipmap do?](#218-what-does-zipmap-do)
- [219: What does setproduct do?](#219-what-does-setproduct-do)
- [220: What does the one function do?](#220-what-does-the-one-function-do)
- [221: Does merge do a deep merge?](#221-does-merge-do-a-deep-merge)
- [222: How do you drive infrastructure from a YAML file?](#222-how-do-you-drive-infrastructure-from-a-yaml-file)
- [223: How do you upload a folder of files to S3 with Terraform?](#223-how-do-you-upload-a-folder-of-files-to-s3-with-terraform)
- [224: What is the external data source?](#224-what-is-the-external-data-source)
- [225: What is the http data source?](#225-what-is-the-http-data-source)
- [226: Why should you be careful with local\_file?](#226-why-should-you-be-careful-with-local_file)
- [227: What is the risk of tls\_private\_key?](#227-what-is-the-risk-of-tls_private_key)
- [228: What is time\_sleep and when is it used?](#228-what-is-time_sleep-and-when-is-it-used)
- [229: What is eventual consistency and how does it affect Terraform?](#229-what-is-eventual-consistency-and-how-does-it-affect-terraform)
- [230: How do you upgrade a provider to a new major version?](#230-how-do-you-upgrade-a-provider-to-a-new-major-version)
- [231: How do you upgrade the Terraform CLI version?](#231-how-do-you-upgrade-the-terraform-cli-version)
- [232: How do you refactor a big root module into child modules without recreating resources?](#232-how-do-you-refactor-a-big-root-module-into-child-modules-without-recreating-resources)
- [233: How do you move resources from one state to another?](#233-how-do-you-move-resources-from-one-state-to-another)
- [234: What does terraform state replace-provider do?](#234-what-does-terraform-state-replace-provider-do)
- [235: What is a perpetual diff and how do you fix it?](#235-what-is-a-perpetual-diff-and-how-do-you-fix-it)
- [236: How do you migrate null\_resource to terraform\_data?](#236-how-do-you-migrate-null_resource-to-terraform_data)
- [237: Can a module output a whole resource object?](#237-can-a-module-output-a-whole-resource-object)
- [238: What should a reusable module repository contain?](#238-what-should-a-reusable-module-repository-contain)
- [239: How do you publish a module to the public Terraform Registry?](#239-how-do-you-publish-a-module-to-the-public-terraform-registry)
- [240: What is a private module registry?](#240-what-is-a-private-module-registry)
- [241: How do you keep providers and modules up to date?](#241-how-do-you-keep-providers-and-modules-up-to-date)
- [242: What is the difference between Sentinel and OPA for Terraform policies?](#242-what-is-the-difference-between-sentinel-and-opa-for-terraform-policies)
- [243: How do you check a plan with OPA and Conftest?](#243-how-do-you-check-a-plan-with-opa-and-conftest)
- [244: How do you detect drift regularly?](#244-how-do-you-detect-drift-regularly)
- [245: How do you control who can apply changes to production?](#245-how-do-you-control-who-can-apply-changes-to-production)
- [246: What do you do when you get "Error acquiring the state lock"?](#246-what-do-you-do-when-you-get-error-acquiring-the-state-lock)
- [247: What does "Provider produced inconsistent result after apply" mean?](#247-what-does-provider-produced-inconsistent-result-after-apply-mean)
- [248: What do you do when apply fails with "resource already exists"?](#248-what-do-you-do-when-apply-fails-with-resource-already-exists)
- [249: How do you handle API rate limiting?](#249-how-do-you-handle-api-rate-limiting)
- [250: What is kubernetes\_manifest?](#250-what-is-kubernetes_manifest)
- [251: How can you test Terraform code against AWS without a real account?](#251-how-can-you-test-terraform-code-against-aws-without-a-real-account)
- [252: What is Terratest?](#252-what-is-terratest)
- [253: Can Terraform manage things other than cloud infrastructure?](#253-can-terraform-manage-things-other-than-cloud-infrastructure)
- [254: Should Terraform code live in a monorepo or in many repos?](#254-should-terraform-code-live-in-a-monorepo-or-in-many-repos)
- [255: How do you pass Terraform outputs to Ansible?](#255-how-do-you-pass-terraform-outputs-to-ansible)
- [256: How do you do a blue/green deployment with Terraform?](#256-how-do-you-do-a-bluegreen-deployment-with-terraform)
- [257: How do you use providers in a network without internet access?](#257-how-do-you-use-providers-in-a-network-without-internet-access)
- [258: How do you output values from a resource created with for\_each?](#258-how-do-you-output-values-from-a-resource-created-with-for_each)
- [259: How do you ignore changes to just one tag?](#259-how-do-you-ignore-changes-to-just-one-tag)
- [260: What happens if a CI job is cancelled during apply?](#260-what-happens-if-a-ci-job-is-cancelled-during-apply)
- [261: What do you look for when reviewing a plan?](#261-what-do-you-look-for-when-reviewing-a-plan)
- [262: Can outputs have preconditions?](#262-can-outputs-have-preconditions)
- [263: Does the sensitive flag carry through modules?](#263-does-the-sensitive-flag-carry-through-modules)
- [264: What is the cloudinit\_config data source?](#264-what-is-the-cloudinit_config-data-source)
- [265: How do you add a nested block only when a condition is true?](#265-how-do-you-add-a-nested-block-only-when-a-condition-is-true)
- [266: How do you make a whole module optional?](#266-how-do-you-make-a-whole-module-optional)
- [267: Can you use variables in a module's source or version?](#267-can-you-use-variables-in-a-modules-source-or-version)
- [268: How should version constraints differ between reusable modules and root modules?](#268-how-should-version-constraints-differ-between-reusable-modules-and-root-modules)
- [269: How do you deploy a Lambda function with Terraform?](#269-how-do-you-deploy-a-lambda-function-with-terraform)
- [270: How do you stop Terraform from fighting with a CI pipeline that deploys new ECS task definitions?](#270-how-do-you-stop-terraform-from-fighting-with-a-ci-pipeline-that-deploys-new-ecs-task-definitions)
- [271: What should you not manage with Terraform?](#271-what-should-you-not-manage-with-terraform)
- [272: What does ignore\_tags in the AWS provider do?](#272-what-does-ignore_tags-in-the-aws-provider-do)
- [273: How do you handle names that must be unique across all AWS customers?](#273-how-do-you-handle-names-that-must-be-unique-across-all-aws-customers)
- [274: How do you create one resource per item of another for\_each resource?](#274-how-do-you-create-one-resource-per-item-of-another-for_each-resource)
- [275: How are permissions organized in HCP Terraform?](#275-how-are-permissions-organized-in-hcp-terraform)
- [276: What are agent pools in HCP Terraform?](#276-what-are-agent-pools-in-hcp-terraform)
- [277: What are dynamic provider credentials in HCP Terraform?](#277-what-are-dynamic-provider-credentials-in-hcp-terraform)
- [278: What is a speculative plan?](#278-what-is-a-speculative-plan)
- [279: What are the limits of -generate-config-out?](#279-what-are-the-limits-of--generate-config-out)
- [280: How do you know what ID to use when importing a resource?](#280-how-do-you-know-what-id-to-use-when-importing-a-resource)
- [281: What happens when a data source can't find anything?](#281-what-happens-when-a-data-source-cant-find-anything)
- [282: Why is depends\_on on a data source usually a bad idea?](#282-why-is-depends_on-on-a-data-source-usually-a-bad-idea)
- [283: How do you validate an ACM certificate with DNS in Terraform?](#283-how-do-you-validate-an-acm-certificate-with-dns-in-terraform)
- [284: How do you combine several IAM policy documents?](#284-how-do-you-combine-several-iam-policy-documents)
- [285: Why shouldn't you mix inline security group rules with separate rule resources?](#285-why-shouldnt-you-mix-inline-security-group-rules-with-separate-rule-resources)
- [286: How do you bring a manually built environment under Terraform?](#286-how-do-you-bring-a-manually-built-environment-under-terraform)
- [287: How does Crossplane compare to Terraform?](#287-how-does-crossplane-compare-to-terraform)
- [288: How do you safely remove a big piece of infrastructure?](#288-how-do-you-safely-remove-a-big-piece-of-infrastructure)
- [289: What makes a good module interface?](#289-what-makes-a-good-module-interface)
- [290: How do you pass lists and maps on the command line?](#290-how-do-you-pass-lists-and-maps-on-the-command-line)
- [291: How do you test a module in CI?](#291-how-do-you-test-a-module-in-ci)
- [292: How do you test a module from a separate test configuration?](#292-how-do-you-test-a-module-from-a-separate-test-configuration)
- [293: How do you share default settings across many items in a for\_each?](#293-how-do-you-share-default-settings-across-many-items-in-a-for_each)
- [294: Why are S3 bucket settings split into many resources in the AWS provider?](#294-why-are-s3-bucket-settings-split-into-many-resources-in-the-aws-provider)
- [295: What are provider-defined functions?](#295-what-are-provider-defined-functions)
- [296: How do you protect a database from deletion besides prevent\_destroy?](#296-how-do-you-protect-a-database-from-deletion-besides-prevent_destroy)
- [297: Can you use count or for\_each on data sources?](#297-can-you-use-count-or-for_each-on-data-sources)
- [298: What permissions does the S3 backend need?](#298-what-permissions-does-the-s3-backend-need)
- [299: What happens if you rename a module call in the root module?](#299-what-happens-if-you-rename-a-module-call-in-the-root-module)
- [300: How do you find which resources in state are not in your code anymore?](#300-how-do-you-find-which-resources-in-state-are-not-in-your-code-anymore)

### Advanced Questions (301-450)

- [301: How do Terraform core and providers talk to each other?](#301-how-do-terraform-core-and-providers-talk-to-each-other)
- [302: What are plugin protocol versions 5 and 6?](#302-what-are-plugin-protocol-versions-5-and-6)
- [303: What happens internally during terraform plan?](#303-what-happens-internally-during-terraform-plan)
- [304: What does the state file look like inside?](#304-what-does-the-state-file-look-like-inside)
- [305: What are serial and lineage in the state file?](#305-what-are-serial-and-lineage-in-the-state-file)
- [306: How does S3 native state locking work?](#306-how-does-s3-native-state-locking-work)
- [307: How do you move from DynamoDB locking to S3 native locking?](#307-how-do-you-move-from-dynamodb-locking-to-s3-native-locking)
- [308: How do unknown values work during planning?](#308-how-do-unknown-values-work-during-planning)
- [309: What are deferred actions?](#309-what-are-deferred-actions)
- [310: How does Terraform decide between an in-place update and a replace?](#310-how-does-terraform-decide-between-an-in-place-update-and-a-replace)
- [311: What is private data in state?](#311-what-is-private-data-in-state)
- [312: How are provider schema changes handled for existing state?](#312-how-are-provider-schema-changes-handled-for-existing-state)
- [313: What is the difference between the Terraform Plugin Framework and SDKv2?](#313-what-is-the-difference-between-the-terraform-plugin-framework-and-sdkv2)
- [314: How would you write a custom provider?](#314-how-would-you-write-a-custom-provider)
- [315: How are providers tested?](#315-how-are-providers-tested)
- [316: How do you test a locally built provider without publishing it?](#316-how-do-you-test-a-locally-built-provider-without-publishing-it)
- [317: How are modules installed and tracked?](#317-how-are-modules-installed-and-tracked)
- [318: What are the h1 and zh hashes in the lock file?](#318-what-are-the-h1-and-zh-hashes-in-the-lock-file)
- [319: How does Terraform verify that a provider is authentic?](#319-how-does-terraform-verify-that-a-provider-is-authentic)
- [320: How do you protect against supply chain attacks in Terraform?](#320-how-do-you-protect-against-supply-chain-attacks-in-terraform)
- [321: Why is running terraform plan on untrusted code dangerous?](#321-why-is-running-terraform-plan-on-untrusted-code-dangerous)
- [322: What options exist to encrypt Terraform state?](#322-what-options-exist-to-encrypt-terraform-state)
- [323: How do you decide where to split state?](#323-how-do-you-decide-where-to-split-state)
- [324: How would you structure Terraform for a large organization?](#324-how-would-you-structure-terraform-for-a-large-organization)
- [325: What are Terraform Stacks?](#325-what-are-terraform-stacks)
- [326: What does a Stack configuration look like?](#326-what-does-a-stack-configuration-look-like)
- [327: What is the action block in Terraform 1.14?](#327-what-is-the-action-block-in-terraform-114)
- [328: What is terraform query?](#328-what-is-terraform-query)
- [329: How do ephemeral resources work internally?](#329-how-do-ephemeral-resources-work-internally)
- [330: What are the limitations of ephemeral values and write-only arguments?](#330-what-are-the-limitations-of-ephemeral-values-and-write-only-arguments)
- [331: What sensitive data can end up in a saved plan file?](#331-what-sensitive-data-can-end-up-in-a-saved-plan-file)
- [332: Can TF\_LOG output leak secrets?](#332-can-tf_log-output-leak-secrets)
- [333: How do you give Terraform least-privilege permissions?](#333-how-do-you-give-terraform-least-privilege-permissions)
- [334: Why use permission boundaries for Terraform-created IAM roles?](#334-why-use-permission-boundaries-for-terraform-created-iam-roles)
- [335: How should the state bucket be secured?](#335-how-should-the-state-bucket-be-secured)
- [336: How do you set up CI so pull requests from forks can't steal credentials?](#336-how-do-you-set-up-ci-so-pull-requests-from-forks-cant-steal-credentials)
- [337: How do you recover from a corrupted state file?](#337-how-do-you-recover-from-a-corrupted-state-file)
- [338: How do you edit state by hand when no command can fix a problem?](#338-how-do-you-edit-state-by-hand-when-no-command-can-fix-a-problem)
- [339: What happens when two people apply at the same time without locking?](#339-what-happens-when-two-people-apply-at-the-same-time-without-locking)
- [340: How do you handle many teams who need to change the same state?](#340-how-do-you-handle-many-teams-who-need-to-change-the-same-state)
- [341: How do you manage the order of applies across many states?](#341-how-do-you-manage-the-order-of-applies-across-many-states)
- [342: How do you reduce the blast radius of Terraform changes?](#342-how-do-you-reduce-the-blast-radius-of-terraform-changes)
- [343: How does Terraform perform with very large states?](#343-how-does-terraform-perform-with-very-large-states)
- [344: When is it OK to skip the refresh in a pipeline?](#344-when-is-it-ok-to-skip-the-refresh-in-a-pipeline)
- [345: How does create\_before\_destroy spread through dependencies?](#345-how-does-create_before_destroy-spread-through-dependencies)
- [346: How does Terraform know the destroy order for resources removed from the code?](#346-how-does-terraform-know-the-destroy-order-for-resources-removed-from-the-code)
- [347: What are the rules and limits of moved blocks?](#347-what-are-the-rules-and-limits-of-moved-blocks)
- [348: Why should shared modules keep their moved blocks?](#348-why-should-shared-modules-keep-their-moved-blocks)
- [349: Where can import blocks be used?](#349-where-can-import-blocks-be-used)
- [350: How do you fix "Inconsistent conditional result types"?](#350-how-do-you-fix-inconsistent-conditional-result-types)
- [351: What errors can try not catch?](#351-what-errors-can-try-not-catch)
- [352: How do optional attribute defaults work with nested objects?](#352-how-do-optional-attribute-defaults-work-with-nested-objects)
- [353: What is the difference between passing null and leaving an argument out?](#353-what-is-the-difference-between-passing-null-and-leaving-an-argument-out)
- [354: Does jsonencode keep the sensitive mark?](#354-does-jsonencode-keep-the-sensitive-mark)
- [355: What happens when a provider block uses values that are unknown during the plan?](#355-what-happens-when-a-provider-block-uses-values-that-are-unknown-during-the-plan)
- [356: What does "Provider configuration not present" mean?](#356-what-does-provider-configuration-not-present-mean)
- [357: How do you remove a module that has its own provider block?](#357-how-do-you-remove-a-module-that-has-its-own-provider-block)
- [358: Can you use for\_each on provider blocks?](#358-can-you-use-for_each-on-provider-blocks)
- [359: How do Terraform and OpenTofu differ today?](#359-how-do-terraform-and-opentofu-differ-today)
- [360: How would you migrate from Terraform to OpenTofu?](#360-how-would-you-migrate-from-terraform-to-opentofu)
- [361: What stages does a run go through in HCP Terraform?](#361-what-stages-does-a-run-go-through-in-hcp-terraform)
- [362: What does a simple Sentinel policy look like?](#362-what-does-a-simple-sentinel-policy-look-like)
- [363: When should you use custom conditions and when policy as code?](#363-when-should-you-use-custom-conditions-and-when-policy-as-code)
- [364: What does a good testing strategy for Terraform look like?](#364-what-does-a-good-testing-strategy-for-terraform-look-like)
- [365: How does terraform test handle state and cleanup?](#365-how-does-terraform-test-handle-state-and-cleanup)
- [366: How would you design active-active infrastructure in two regions with Terraform?](#366-how-would-you-design-active-active-infrastructure-in-two-regions-with-terraform)
- [367: Why are multi-cloud abstraction modules usually a bad idea?](#367-why-are-multi-cloud-abstraction-modules-usually-a-bad-idea)
- [368: What is a thin wrapper module and why is it an anti-pattern?](#368-what-is-a-thin-wrapper-module-and-why-is-it-an-anti-pattern)
- [369: How do you choose between Terragrunt, HCP Terraform workspaces and Stacks?](#369-how-do-you-choose-between-terragrunt-hcp-terraform-workspaces-and-stacks)
- [370: What does GitOps for Terraform look like?](#370-what-does-gitops-for-terraform-look-like)
- [371: How would you create a temporary environment for each pull request?](#371-how-would-you-create-a-temporary-environment-for-each-pull-request)
- [372: How do you enforce tagging across all resources?](#372-how-do-you-enforce-tagging-across-all-resources)
- [373: How do you manage thousands of similar resources efficiently?](#373-how-do-you-manage-thousands-of-similar-resources-efficiently)
- [374: How do you handle many regions or accounts without for\_each on providers?](#374-how-do-you-handle-many-regions-or-accounts-without-for_each-on-providers)
- [375: When would you generate Terraform configuration as JSON?](#375-when-would-you-generate-terraform-configuration-as-json)
- [376: Why is -target dangerous in normal use?](#376-why-is--target-dangerous-in-normal-use)
- [377: What does "saved plan is stale" mean?](#377-what-does-saved-plan-is-stale-mean)
- [378: How do you find out if two states manage the same resource?](#378-how-do-you-find-out-if-two-states-manage-the-same-resource)
- [379: How do you rotate a secret that is set through a write-only argument?](#379-how-do-you-rotate-a-secret-that-is-set-through-a-write-only-argument)
- [380: How do you know in advance whether a change will replace a resource?](#380-how-do-you-know-in-advance-whether-a-change-will-replace-a-resource)
- [381: How do you change a database instance without unexpected downtime?](#381-how-do-you-change-a-database-instance-without-unexpected-downtime)
- [382: What are the risks of ignore\_changes?](#382-what-are-the-risks-of-ignore_changes)
- [383: How do you work around a provider bug?](#383-how-do-you-work-around-a-provider-bug)
- [384: How can you use a patched fork of a provider?](#384-how-can-you-use-a-patched-fork-of-a-provider)
- [385: How do you read Terraform TRACE logs?](#385-how-do-you-read-terraform-trace-logs)
- [386: How do you debug an unexpected diff?](#386-how-do-you-debug-an-unexpected-diff)
- [387: How do you verify that a big refactor only moves resources?](#387-how-do-you-verify-that-a-big-refactor-only-moves-resources)
- [388: How do you move a resource to a different account?](#388-how-do-you-move-a-resource-to-a-different-account)
- [389: How do you split one state into several?](#389-how-do-you-split-one-state-into-several)
- [390: How do you merge two states into one?](#390-how-do-you-merge-two-states-into-one)
- [391: How do you upgrade a very old Terraform project (0.11 or 0.12)?](#391-how-do-you-upgrade-a-very-old-terraform-project-011-or-012)
- [392: How do you audit who changed infrastructure and when?](#392-how-do-you-audit-who-changed-infrastructure-and-when)
- [393: What problems happen when Terraform manages Kubernetes objects that controllers also change?](#393-what-problems-happen-when-terraform-manages-kubernetes-objects-that-controllers-also-change)
- [394: What are the pros and cons of installing Helm charts with Terraform?](#394-what-are-the-pros-and-cons-of-installing-helm-charts-with-terraform)
- [395: What should you watch out for when upgrading a managed Kubernetes cluster with Terraform?](#395-what-should-you-watch-out-for-when-upgrading-a-managed-kubernetes-cluster-with-terraform)
- [396: How do you do a major version upgrade of an RDS database with Terraform?](#396-how-do-you-do-a-major-version-upgrade-of-an-rds-database-with-terraform)
- [397: How should outputs shared between states be designed?](#397-how-should-outputs-shared-between-states-be-designed)
- [398: How do you roll out a risky change across many regions?](#398-how-do-you-roll-out-a-risky-change-across-many-regions)
- [399: How are workspace states stored in the S3 backend?](#399-how-are-workspace-states-stored-in-the-s3-backend)
- [400: How do you work with tree-shaped data when HCL has no recursion?](#400-how-do-you-work-with-tree-shaped-data-when-hcl-has-no-recursion)
- [401: What is a data-only module?](#401-what-is-a-data-only-module)
- [402: What is dependency inversion in Terraform modules?](#402-what-is-dependency-inversion-in-terraform-modules)
- [403: Why can't a consumer use for\_each over a module output whose keys come from created resources?](#403-why-cant-a-consumer-use-for_each-over-a-module-output-whose-keys-come-from-created-resources)
- [404: How does Terraform evaluate locals and variables?](#404-how-does-terraform-evaluate-locals-and-variables)
- [405: How does HCP Terraform use check blocks for continuous validation?](#405-how-does-hcp-terraform-use-check-blocks-for-continuous-validation)
- [406: What compatibility promises does Terraform 1.x make?](#406-what-compatibility-promises-does-terraform-1x-make)
- [407: When is a refresh-only apply useful during an incident?](#407-when-is-a-refresh-only-apply-useful-during-an-incident)
- [408: What is the difference between timestamp and plantimestamp?](#408-what-is-the-difference-between-timestamp-and-plantimestamp)
- [409: Why can't a module with for\_each use a different provider for each instance?](#409-why-cant-a-module-with-for_each-use-a-different-provider-for-each-instance)
- [410: How do you run CI only for the Terraform folders that changed?](#410-how-do-you-run-ci-only-for-the-terraform-folders-that-changed)
- [411: Is it safe to cache the .terraform directory in CI?](#411-is-it-safe-to-cache-the-terraform-directory-in-ci)
- [412: How do you manage lock files in a monorepo with many root modules?](#412-how-do-you-manage-lock-files-in-a-monorepo-with-many-root-modules)
- [413: The plan wants to destroy and recreate a production database. What do you do?](#413-the-plan-wants-to-destroy-and-recreate-a-production-database-what-do-you-do)
- [414: Someone opened a port in a security group through the console and the plan wants to close it. What do you do?](#414-someone-opened-a-port-in-a-security-group-through-the-console-and-the-plan-wants-to-close-it-what-do-you-do)
- [415: Someone ran apply with a newer Terraform version and now others get an error reading the state. What do you do?](#415-someone-ran-apply-with-a-newer-terraform-version-and-now-others-get-an-error-reading-the-state-what-do-you-do)
- [416: An apply failed halfway in one of three regions. How do you recover?](#416-an-apply-failed-halfway-in-one-of-three-regions-how-do-you-recover)
- [417: A provider upgrade makes the plan want to replace hundreds of resources. What do you do?](#417-a-provider-upgrade-makes-the-plan-want-to-replace-hundreds-of-resources-what-do-you-do)
- [418: The plan for a configuration takes 30 minutes. How do you fix it?](#418-the-plan-for-a-configuration-takes-30-minutes-how-do-you-fix-it)
- [419: You found database passwords in plain text in your state. How do you fix it?](#419-you-found-database-passwords-in-plain-text-in-your-state-how-do-you-fix-it)
- [420: You need to rename a resource that exists in 50 workspaces. How do you do it safely?](#420-you-need-to-rename-a-resource-that-exists-in-50-workspaces-how-do-you-do-it-safely)
- [421: How would you migrate infrastructure from CloudFormation to Terraform?](#421-how-would-you-migrate-infrastructure-from-cloudformation-to-terraform)
- [422: Two teams need to use the same VPC. How do you set it up?](#422-two-teams-need-to-use-the-same-vpc-how-do-you-set-it-up)
- [423: A consumer of your module gets "count value depends on resource attributes that cannot be determined until apply". How do you fix it in the module?](#423-a-consumer-of-your-module-gets-count-value-depends-on-resource-attributes-that-cannot-be-determined-until-apply-how-do-you-fix-it-in-the-module)
- [424: AWS services keep adding tags to your resources and every plan shows changes. What do you do?](#424-aws-services-keep-adding-tags-to-your-resources-and-every-plan-shows-changes-what-do-you-do)
- [425: You need to set up 100 new AWS accounts with the same baseline. How do you approach it?](#425-you-need-to-set-up-100-new-aws-accounts-with-the-same-baseline-how-do-you-approach-it)
- [426: How would you design a Terraform platform for a company with many teams?](#426-how-would-you-design-a-terraform-platform-for-a-company-with-many-teams)
- [427: Someone ran terraform destroy on production by mistake. How do you recover?](#427-someone-ran-terraform-destroy-on-production-by-mistake-how-do-you-recover)
- [428: You need to rename a database, but the name forces replacement. How do you do it without data loss?](#428-you-need-to-rename-a-database-but-the-name-forces-replacement-how-do-you-do-it-without-data-loss)
- [429: How would you bring thousands of existing DNS records under Terraform?](#429-how-would-you-bring-thousands-of-existing-dns-records-under-terraform)
- [430: The plan keeps showing a list attribute reordered. What is going on?](#430-the-plan-keeps-showing-a-list-attribute-reordered-what-is-going-on)
- [431: A random\_password changed and caused a database password reset. Why?](#431-a-random_password-changed-and-caused-a-database-password-reset-why)
- [432: Destroying a Kubernetes namespace with Terraform hangs. Why?](#432-destroying-a-kubernetes-namespace-with-terraform-hangs-why)
- [433: Destroying a security group takes forever and fails. Why?](#433-destroying-a-security-group-takes-forever-and-fails-why)
- [434: CI fails with "saved plan is stale". What happened and what do you do?](#434-ci-fails-with-saved-plan-is-stale-what-happened-and-what-do-you-do)
- [435: Your team needs a feature that a community module doesn't support. What do you do?](#435-your-team-needs-a-feature-that-a-community-module-doesnt-support-what-do-you-do)
- [436: A developer wants to test infrastructure changes without breaking the shared dev environment. How?](#436-a-developer-wants-to-test-infrastructure-changes-without-breaking-the-shared-dev-environment-how)
- [437: Your rotation of the KMS key used by the state bucket went wrong and Terraform can't read state. What do you check?](#437-your-rotation-of-the-kms-key-used-by-the-state-bucket-went-wrong-and-terraform-cant-read-state-what-do-you-check)
- [438: Replacing an IAM policy broke the app for a few minutes. Why, and how do you avoid it?](#438-replacing-an-iam-policy-broke-the-app-for-a-few-minutes-why-and-how-do-you-avoid-it)
- [439: Plans on laptops and in CI give different results. What do you check?](#439-plans-on-laptops-and-in-ci-give-different-results-what-do-you-check)
- [440: You inherited a Terraform project with local state and secrets in tfvars files. What do you do first?](#440-you-inherited-a-terraform-project-with-local-state-and-secrets-in-tfvars-files-what-do-you-do-first)
- [441: An auditor asks you to prove that all S3 buckets are encrypted. How do you answer with Terraform?](#441-an-auditor-asks-you-to-prove-that-all-s3-buckets-are-encrypted-how-do-you-answer-with-terraform)
- [442: The cloud bill jumped after an apply. How do you find the cause?](#442-the-cloud-bill-jumped-after-an-apply-how-do-you-find-the-cause)
- [443: What are the main limitations of Terraform?](#443-what-are-the-main-limitations-of-terraform)
- [444: When would you not choose Terraform?](#444-when-would-you-not-choose-terraform)
- [445: Where is Terraform heading?](#445-where-is-terraform-heading)
- [446: How would you explain to a developer why Terraform needs state?](#446-how-would-you-explain-to-a-developer-why-terraform-needs-state)
- [447: What common Terraform mistakes do you see in real projects?](#447-what-common-terraform-mistakes-do-you-see-in-real-projects)
- [448: How do you decide when a plan is safe to auto-apply?](#448-how-do-you-decide-when-a-plan-is-safe-to-auto-apply)
- [449: How do you handle a Terraform change that needs a specific order across two applies?](#449-how-do-you-handle-a-terraform-change-that-needs-a-specific-order-across-two-applies)
- [450: You join a team with a messy Terraform codebase. What do you do in your first weeks?](#450-you-join-a-team-with-a-messy-terraform-codebase-what-do-you-do-in-your-first-weeks)

---

# Easy Questions (1-150)

## 1: What is Terraform?

Terraform is an infrastructure as code tool made by HashiCorp. You describe the infrastructure you want (servers, networks, databases, DNS records, Kubernetes objects and so on) in configuration files, and Terraform creates, updates and deletes the real resources to match.

It works with almost any platform through plugins called providers: AWS, Azure, Google Cloud, Kubernetes, GitHub, Cloudflare, Datadog and thousands more.

## 2: What is infrastructure as code?

Infrastructure as code (IaC) means managing infrastructure through files instead of clicking in a web console or running one-off commands. The files live in version control, so you get:

- A history of every change and who made it
- Code review before changes go live
- The same setup repeated across dev, staging and production
- Easy rebuilds if something is lost

Terraform, OpenTofu, Pulumi, AWS CloudFormation and Azure Bicep are all IaC tools.

## 3: What language is Terraform configuration written in?

Terraform uses HCL (HashiCorp Configuration Language). It is a declarative language made of blocks, arguments and expressions. Files end in `.tf`.

```hcl
resource "aws_s3_bucket" "logs" {
  bucket = "my-app-logs"

  tags = {
    Environment = "dev"
  }
}
```

Terraform can also read JSON files that end in `.tf.json`. These are mostly used when another program generates the configuration.

## 4: What does it mean that Terraform is declarative?

You describe the end result you want, not the steps to get there. For example, you say "I want three EC2 instances of this type". Terraform compares that with what exists and figures out whether it needs to create, change or delete anything.

With an imperative approach (like a shell script calling the AWS CLI) you write each step yourself and you have to handle the case where some resources already exist.

## 5: What is a provider in Terraform?

A provider is a plugin that lets Terraform talk to an API. The AWS provider knows how to create EC2 instances and S3 buckets, the Kubernetes provider knows how to create deployments, and so on. Each provider adds a set of resource types and data sources.

Providers are separate binaries. Terraform downloads them during `terraform init`, usually from the public Terraform Registry.

```hcl
provider "aws" {
  region = "eu-central-1"
}
```

## 6: What is a resource?

A resource is a single piece of infrastructure that Terraform manages, like a VM, a subnet, a database or a DNS record. It is the most important block in Terraform.

```hcl
resource "aws_instance" "web" {
  ami           = "ami-0123456789abcdef0"
  instance_type = "t3.micro"
}
```

The first label (`aws_instance`) is the resource type and the second (`web`) is the local name. Together they form the address `aws_instance.web`, which must be unique within a module.

## 7: What is a data source?

A data source reads information about something that already exists, without managing it. You use it to look up values like the latest AMI, an existing VPC or the current AWS account ID.

```hcl
data "aws_caller_identity" "current" {}

data "aws_ami" "ubuntu" {
  most_recent = true
  owners      = ["099720109477"]

  filter {
    name   = "name"
    values = ["ubuntu/images/hvm-ssd-gp3/ubuntu-noble-24.04-amd64-server-*"]
  }
}

output "account_id" {
  value = data.aws_caller_identity.current.account_id
}
```

You reference it with the `data.` prefix.

## 8: What is the difference between a resource and a data source?

A resource is created, updated and deleted by Terraform. Terraform owns its lifecycle and tracks it in state.

A data source is read only. Terraform just fetches its attributes on each plan. If you remove a data source from your code, nothing is deleted in the real world.

## 9: What is the Terraform state?

State is a file (by default `terraform.tfstate`) where Terraform records which real objects belong to which resources in your code, along with their attributes. It is JSON.

Terraform needs state to:

- Map `aws_instance.web` to the real instance ID `i-0abc...`
- Know what it created, so it can update or delete it later
- Track dependencies and metadata
- Speed up plans for large setups

Without state, Terraform would have no way of knowing which objects it manages.

## 10: What are the main Terraform commands?

The core workflow uses four commands:

- `terraform init` downloads providers and modules and sets up the backend
- `terraform plan` shows what changes Terraform would make
- `terraform apply` makes those changes
- `terraform destroy` deletes everything managed by the configuration

Other common ones are `fmt`, `validate`, `output`, `show`, `state`, `import`, `console`, `workspace`, `providers` and `test`.

## 11: What does terraform init do?

`terraform init` prepares a working directory. It:

- Downloads the providers listed in the configuration
- Downloads modules from the registry, Git or other sources
- Configures the backend where state is stored
- Creates or updates the dependency lock file `.terraform.lock.hcl`

You run it first in a new directory, and again whenever you add a provider, add a module or change the backend. It is safe to run many times.

## 12: What does terraform plan do?

`terraform plan` reads the current state, refreshes it against the real infrastructure, compares it with your configuration and prints what would change. Nothing is changed in the real world.

The output uses symbols:

- `+` create
- `-` destroy
- `~` update in place
- `-/+` destroy and then create (replace)
- `<=` read (data source)

You can save the plan with `terraform plan -out=tfplan` and apply exactly that plan later.

## 13: What does terraform apply do?

`terraform apply` makes the changes needed to reach the state in your configuration. Without arguments it creates a plan, shows it, and asks you to type `yes`.

```bash
terraform apply                 # plan, confirm, apply
terraform apply tfplan          # apply a saved plan, no prompt
terraform apply -auto-approve   # skip the prompt (CI only)
```

After it finishes, the state file is updated with the new resource attributes.

## 14: What does terraform destroy do?

It deletes all resources managed by the current configuration and state. It shows a plan first and asks for confirmation. It is the same as `terraform apply -destroy`.

You can preview it with `terraform plan -destroy`. To delete a single resource you can remove it from the code and run `apply`, or (rarely) use `-target`.

## 15: What does terraform fmt do?

`terraform fmt` rewrites `.tf` files in the standard style: two-space indentation, aligned equals signs and so on.

```bash
terraform fmt              # format files in the current directory
terraform fmt -recursive   # include subdirectories
terraform fmt -check       # exit with an error if anything is not formatted (good for CI)
```

## 16: What does terraform validate do?

`terraform validate` checks that the configuration is syntactically valid and internally consistent: correct block names, required arguments present, references that point to things that exist, correct types and so on.

It does not talk to cloud APIs or read remote state, so it cannot catch problems like an invalid AMI ID. It needs `terraform init` to have run first so it knows the provider schemas.

## 17: What is the .terraform directory?

`.terraform` is a local directory created by `terraform init`. It holds downloaded provider binaries, downloaded modules and some backend metadata. It should not be committed to Git. You can delete it and recreate it any time with `terraform init`.

## 18: What is the .terraform.lock.hcl file?

It is the dependency lock file. It records the exact provider versions Terraform selected and their checksums. The next `terraform init` uses the same versions, so everyone on the team and the CI pipeline run the same provider builds.

You should commit it to Git. To move to newer allowed versions, run `terraform init -upgrade`. Note that it only locks providers, not modules.

## 19: Which files should be in .gitignore for a Terraform project?

A typical `.gitignore`:

```gitignore
.terraform/
*.tfstate
*.tfstate.*
crash.log
crash.*.log
*.tfplan
override.tf
override.tf.json
*_override.tf
*_override.tf.json
```

Many teams also ignore `*.tfvars` files that contain secrets. Do commit `.terraform.lock.hcl`.

## 20: What is the terraform block?

The `terraform` block configures Terraform itself: the required Terraform version, the required providers and the backend.

```hcl
terraform {
  required_version = ">= 1.14"

  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 6.0"
    }
  }

  backend "s3" {
    bucket       = "my-tf-state"
    key          = "app/terraform.tfstate"
    region       = "eu-central-1"
    use_lockfile = true
  }
}
```

## 21: What is required_providers?

`required_providers` inside the `terraform` block lists the providers a module needs. For each one you give a local name, a `source` address and usually a `version` constraint.

The source has the form `[hostname/]namespace/type`, for example `hashicorp/aws` or `cloudflare/cloudflare`. The hostname defaults to `registry.terraform.io`. Every module should declare its own `required_providers`.

## 22: How do version constraints work in Terraform?

Version constraints are strings with operators:

- `= 1.2.0` or `1.2.0` exactly this version
- `!= 1.2.0` anything except this one
- `>`, `>=`, `<`, `<=` comparisons
- `~> 1.2` allows `1.x` from `1.2` upwards, but not `2.0`
- `~> 1.2.0` allows `1.2.x` only

You can combine them with commas: `">= 1.5, < 2.0"`. The `~>` operator (pessimistic constraint) is the most common.

## 23: What does required_version do?

`required_version` sets which Terraform CLI versions can run the configuration. If someone uses a version outside the range, Terraform stops with an error.

```hcl
terraform {
  required_version = ">= 1.10, < 2.0"
}
```

This prevents someone with an old CLI from running a plan that it does not fully understand, or someone with a newer one from upgrading the state format by accident.

## 24: What is the Terraform Registry?

The Terraform Registry (`registry.terraform.io`) is the public place where providers and modules are published. `terraform init` downloads from it by default.

Providers are marked by tier: official (owned by HashiCorp), partner (owned by a technology company) and community. You can also find documentation for every resource and argument there. HCP Terraform and Terraform Enterprise also offer a private registry for internal modules.

## 25: What is a variable in Terraform?

An input variable is a parameter for a module. It lets you reuse the same code with different values.

```hcl
variable "instance_type" {
  type        = string
  description = "EC2 instance type"
  default     = "t3.micro"
}

resource "aws_instance" "web" {
  ami           = var.ami_id
  instance_type = var.instance_type
}
```

You reference it with `var.<name>`. A variable without a default is required.

## 26: What are the ways to set variable values?

You can set variables in several ways:

- A `default` in the variable block
- A `terraform.tfvars` or `terraform.tfvars.json` file (loaded automatically)
- Any `*.auto.tfvars` or `*.auto.tfvars.json` file (loaded automatically)
- `-var-file=prod.tfvars` on the command line
- `-var="instance_type=t3.large"` on the command line
- Environment variables named `TF_VAR_<name>`, for example `TF_VAR_instance_type`

If a required variable has no value, Terraform asks for it interactively (unless you pass `-input=false`).

## 27: What is the order of precedence for variable values?

From lowest to highest, later sources win:

1. Environment variables (`TF_VAR_...`)
2. `terraform.tfvars`
3. `terraform.tfvars.json`
4. `*.auto.tfvars` and `*.auto.tfvars.json` in alphabetical order
5. `-var` and `-var-file` options, in the order they appear on the command line

The `default` in the variable block is used only when none of these set a value.

## 28: What is a .tfvars file?

A `.tfvars` file holds values for input variables, written as simple assignments.

```hcl
# prod.tfvars
instance_type = "m6i.large"
replica_count = 3
allowed_cidrs = ["10.0.0.0/16"]
```

`terraform.tfvars` and `*.auto.tfvars` load automatically. Other files need `-var-file`. A common pattern is one file per environment, like `dev.tfvars` and `prod.tfvars`.

## 29: What is an output value?

An output exposes a value from a module. In the root module, outputs are printed after `apply` and can be read with `terraform output`. In a child module, outputs are how the parent gets values from it.

```hcl
output "instance_ip" {
  description = "Public IP of the web server"
  value       = aws_instance.web.public_ip
}
```

```bash
terraform output instance_ip
terraform output -raw instance_ip   # no quotes, good for scripts
terraform output -json
```

## 30: What is a local value?

A local value (`locals`) gives a name to an expression so you can reuse it inside a module. It is like a local variable in a function. It cannot be set from outside.

```hcl
locals {
  name_prefix = "${var.project}-${var.environment}"
  common_tags = {
    Project     = var.project
    Environment = var.environment
    ManagedBy   = "terraform"
  }
}

resource "aws_s3_bucket" "data" {
  bucket = "${local.name_prefix}-data"
  tags   = local.common_tags
}
```

Note the block is `locals` but the reference is `local.<name>`.

## 31: What is the difference between variables, locals and outputs?

- **Variables** are inputs. Values come from outside the module (tfvars, CLI, parent module).
- **Locals** are internal helper values computed inside the module.
- **Outputs** are return values that the module exposes to its caller or to the user.

A simple way to think about it: a module is like a function, variables are its parameters, locals are its local variables, and outputs are its return values.

## 32: What is a module?

A module is a folder of `.tf` files that are used together. Every Terraform configuration is a module. The folder where you run Terraform is the root module, and modules it calls are child modules.

```hcl
module "vpc" {
  source  = "terraform-aws-modules/vpc/aws"
  version = "~> 6.0"

  name = "main"
  cidr = "10.0.0.0/16"
}
```

Modules let you package and reuse infrastructure patterns instead of copying code.

## 33: What is the root module?

The root module is the set of `.tf` files in the directory where you run `terraform plan` or `apply`. It is the entry point. It usually configures providers and the backend and calls child modules. Only the root module has a state file and a backend.

## 34: Where can modules come from?

The `source` argument supports many locations:

- Local paths: `./modules/network`
- The Terraform Registry: `hashicorp/consul/aws`
- A private registry: `app.terraform.io/my-org/vpc/aws`
- GitHub: `github.com/org/repo//modules/vpc?ref=v1.2.0`
- Generic Git: `git::https://example.com/repo.git?ref=v1.2.0`
- HTTP URLs, S3 buckets and GCS buckets

The `version` argument only works for registry modules. For Git sources, pin with `?ref=` set to a tag or commit.

## 35: How do you pass values into a module and get values out of it?

You pass values as arguments in the `module` block. They match the module's input variables. You read values through the module's outputs with `module.<name>.<output>`.

```hcl
module "web" {
  source        = "./modules/web"
  instance_type = "t3.small"
  subnet_id     = module.vpc.public_subnets[0]
}

output "web_url" {
  value = module.web.url
}
```

## 36: What is the standard file layout of a Terraform module?

There is no required layout, since Terraform loads every `.tf` file in the folder. The common convention is:

- `main.tf` main resources
- `variables.tf` input variables
- `outputs.tf` outputs
- `versions.tf` or `terraform.tf` the `terraform` block with version requirements
- `providers.tf` provider configuration (root module only)
- `locals.tf` and `data.tf` in larger modules
- `README.md`

Reusable modules usually live under a `modules/` folder.

## 37: Does the order of blocks or files matter in Terraform?

No. Terraform loads all `.tf` files in a directory and builds a dependency graph from references. The order of blocks and files does not affect what happens. You can reference a resource that is defined further down, or in another file, without problems.

## 38: How does Terraform know in which order to create resources?

It builds a dependency graph from references between resources. If resource B uses an attribute of resource A, Terraform creates A first.

```hcl
resource "aws_vpc" "main" {
  cidr_block = "10.0.0.0/16"
}

resource "aws_subnet" "a" {
  vpc_id     = aws_vpc.main.id   # implicit dependency on the VPC
  cidr_block = "10.0.1.0/24"
}
```

Resources with no dependency between them are created in parallel. Deletion happens in reverse order.

## 39: What is depends_on?

`depends_on` adds an explicit dependency when Terraform cannot see it from references. For example, an instance that needs an IAM policy to be attached before it starts, even though it does not reference the policy directly.

```hcl
resource "aws_instance" "app" {
  ami           = var.ami_id
  instance_type = "t3.micro"

  depends_on = [aws_iam_role_policy_attachment.app]
}
```

Use it only when needed. Normal references are clearer and Terraform handles them better.

## 40: What are meta-arguments?

Meta-arguments are special arguments that work with any resource (and most with modules), regardless of provider:

- `depends_on` explicit dependencies
- `count` create several copies by number
- `for_each` create several copies from a map or set
- `provider` choose a non-default provider configuration
- `lifecycle` change how create, update and delete behave

Modules support `count`, `for_each`, `depends_on` and `providers`.

## 41: What is count?

`count` creates a number of copies of a resource or module. Inside the block, `count.index` is the current index starting at 0.

```hcl
resource "aws_instance" "web" {
  count         = 3
  ami           = var.ami_id
  instance_type = "t3.micro"

  tags = {
    Name = "web-${count.index}"
  }
}
```

The copies are addressed as `aws_instance.web[0]`, `aws_instance.web[1]` and so on. To get all IDs: `aws_instance.web[*].id`.

## 42: What is for_each?

`for_each` creates one copy for each element of a map or set of strings. Inside the block you use `each.key` and `each.value`.

```hcl
variable "buckets" {
  type = map(string)
  default = {
    logs   = "private"
    assets = "public-read"
  }
}

resource "aws_s3_bucket" "this" {
  for_each = var.buckets
  bucket   = "myapp-${each.key}"
}
```

Instances are addressed by key: `aws_s3_bucket.this["logs"]`.

## 43: How do you create a resource only when a condition is true?

The usual trick is `count` with a conditional expression:

```hcl
resource "aws_cloudwatch_log_group" "debug" {
  count = var.enable_debug ? 1 : 0
  name  = "/app/debug"
}
```

When `enable_debug` is false, the resource is not created. You reference it as `aws_cloudwatch_log_group.debug[0]`, so be careful when it might not exist. You can also use `for_each` with an empty map.

## 44: What is the lifecycle block?

`lifecycle` changes the default behavior of a resource. Its main arguments are:

- `create_before_destroy` create the replacement first, then delete the old one
- `prevent_destroy` fail any plan that would delete this resource
- `ignore_changes` ignore changes to listed attributes
- `replace_triggered_by` replace this resource when something else changes
- `precondition` and `postcondition` custom checks

```hcl
resource "aws_db_instance" "main" {
  # ...
  lifecycle {
    prevent_destroy = true
  }
}
```

## 45: What does prevent_destroy do?

With `prevent_destroy = true`, Terraform fails with an error if a plan would delete the resource. It protects important things like production databases from being removed by accident.

It only protects against Terraform deleting the resource while the block is in the code. If someone removes the resource block itself, the protection goes away with it. It does not stop deletion from the console either.

## 46: What does ignore_changes do?

`ignore_changes` tells Terraform to ignore differences in certain attributes after the resource is created. It is useful when something outside Terraform changes those attributes, like an autoscaler changing the desired count.

```hcl
resource "aws_autoscaling_group" "web" {
  # ...
  desired_capacity = 2

  lifecycle {
    ignore_changes = [desired_capacity]
  }
}
```

`ignore_changes = all` ignores every attribute, so Terraform only creates and deletes the resource.

## 47: What does create_before_destroy do?

By default, when a resource must be replaced, Terraform deletes the old one first and then creates the new one. With `create_before_destroy = true` it creates the new one first, then deletes the old one. This avoids downtime.

It only works if the two can exist at the same time. Resources with unique names (like an S3 bucket name) will fail, so you often combine it with `name_prefix` or a random suffix.

## 48: What are the basic types in Terraform?

Primitive types:

- `string`
- `number`
- `bool`

Collection types (all elements have the same type):

- `list(<type>)` ordered
- `set(<type>)` unordered, unique values
- `map(<type>)` string keys

Structural types:

- `object({ name = string, port = number })`
- `tuple([string, number])`

There is also `any`, which lets Terraform figure out the type, and `null`.

## 49: How do you declare a variable with an object type?

```hcl
variable "database" {
  type = object({
    engine         = string
    instance_class = string
    storage_gb     = number
    multi_az       = optional(bool, false)
  })
}
```

`optional()` marks an attribute that the caller can leave out. The second argument is its default. You read the fields with `var.database.engine`.

## 50: How does string interpolation work?

Inside a quoted string, `${ ... }` inserts the value of an expression.

```hcl
resource "aws_s3_bucket" "logs" {
  bucket = "${var.project}-${var.environment}-logs"
}
```

If the whole value is just one expression, you don't need quotes: write `ami = var.ami_id`, not `ami = "${var.ami_id}"`. The quoted form was required in Terraform 0.11 and older and still shows up in old code.

## 51: How do you write a multi-line string in Terraform?

Use a heredoc. `<<EOT` keeps the text exactly as written. `<<-EOT` removes the common leading indentation, so you can indent the text along with your code.

```hcl
resource "aws_instance" "web" {
  ami           = var.ami_id
  instance_type = "t3.micro"

  user_data = <<-EOT
    #!/bin/bash
    apt-get update
    apt-get install -y nginx
  EOT
}
```

The closing marker must be on its own line. `EOT` is just a convention, any word works.

## 52: How do conditional expressions work?

Terraform uses the ternary syntax `condition ? true_value : false_value`.

```hcl
locals {
  instance_type = var.environment == "prod" ? "m6i.large" : "t3.micro"
}
```

Both results should have the same type, or types Terraform can convert to one type. There is no `if` statement in HCL. Conditions are always expressions.

## 53: What is a for expression?

A `for` expression builds a new list or map from another collection, like `map` and `filter` in other languages.

```hcl
locals {
  names = ["alice", "bob"]

  upper_names = [for n in local.names : upper(n)]
  # ["ALICE", "BOB"]

  name_lengths = { for n in local.names : n => length(n) }
  # { alice = 5, bob = 3 }

  long_names = [for n in local.names : n if length(n) > 3]
  # ["alice"]
}
```

Square brackets produce a list (tuple). Curly braces with `=>` produce a map (object).

## 54: What is a splat expression?

A splat expression `[*]` is a short way to get one attribute from every element of a list.

```hcl
output "instance_ids" {
  value = aws_instance.web[*].id
}
```

It is the same as `[for i in aws_instance.web : i.id]`. Splat works on lists, like resources created with `count`. For resources created with `for_each` (which are maps), use a `for` expression or `values(aws_instance.web)[*].id`.

## 55: Does Terraform have built-in functions?

Yes, many. They are grouped into categories:

- String: `upper`, `lower`, `format`, `join`, `split`, `replace`, `trimspace`
- Numeric: `min`, `max`, `ceil`, `floor`
- Collection: `length`, `concat`, `merge`, `lookup`, `keys`, `values`, `flatten`, `distinct`, `contains`
- Encoding: `jsonencode`, `jsondecode`, `yamlencode`, `base64encode`
- Filesystem: `file`, `templatefile`, `fileset`
- Networking: `cidrsubnet`, `cidrhost`
- Type conversion: `tostring`, `tonumber`, `tolist`, `toset`, `tomap`
- Others: `try`, `can`, `coalesce`, `timestamp`, `uuid`

You cannot define your own functions in HCL, but providers can ship their own functions (Terraform 1.8 and later).

## 56: What is terraform console?

`terraform console` opens an interactive prompt where you can test expressions and functions. It also loads your state, so you can inspect real values.

```bash
$ terraform console
> cidrsubnet("10.0.0.0/16", 8, 2)
"10.0.2.0/24"
> upper("hello")
"HELLO"
> aws_instance.web.private_ip
"10.0.1.15"
```

It is handy for trying out `for` expressions or functions before you put them in code.

## 57: What do the merge, concat and lookup functions do?

```hcl
merge({ a = 1 }, { b = 2 }, { a = 3 })
# { a = 3, b = 2 }  later maps win

concat(["a", "b"], ["c"])
# ["a", "b", "c"]

lookup({ dev = "t3.micro", prod = "m6i.large" }, "prod", "t3.small")
# "m6i.large"  the third argument is the default if the key is missing
```

`merge` is often used to combine common tags with resource-specific tags.

## 58: What is the difference between file and templatefile?

`file(path)` reads a file and returns its content as a string, as is.

`templatefile(path, vars)` reads a file and renders it as a template, replacing `${...}` placeholders with the variables you pass. It also supports `%{ for }` and `%{ if }` directives.

```hcl
user_data = templatefile("${path.module}/init.sh.tftpl", {
  app_port = 8080
  packages = ["nginx", "git"]
})
```

```bash
#!/bin/bash
%{ for p in packages ~}
apt-get install -y ${p}
%{ endfor ~}
echo "PORT=${app_port}" >> /etc/app.env
```

The `.tftpl` extension is the recommended convention for template files.

## 59: What are path.module, path.root and path.cwd?

- `path.module` the folder of the module where the expression is written
- `path.root` the folder of the root module
- `path.cwd` the current working directory where Terraform was run

Use `path.module` when reading files that belong to a module, so the path works no matter where the module is called from.

```hcl
policy = file("${path.module}/policies/s3-read.json")
```

## 60: How do you write comments in Terraform?

HCL supports three comment styles:

```hcl
# single line comment (the recommended style)
// also a single line comment
/* a block comment
   over several lines */
```

`terraform fmt` does not change `//` to `#`, but most style guides prefer `#`.

## 61: What does sensitive = true do on a variable?

It hides the value in `plan` and `apply` output. Terraform shows `(sensitive value)` instead. Any expression that uses the variable is also marked sensitive.

```hcl
variable "db_password" {
  type      = string
  sensitive = true
}
```

It does not encrypt anything. The value is still stored in plain text in the state file (unless you use ephemeral values or write-only arguments, covered later). It only stops it from being printed.

## 62: How do sensitive outputs work?

If an output uses a sensitive value, Terraform requires you to mark the output as `sensitive = true`, or it fails with an error.

```hcl
output "db_password" {
  value     = random_password.db.result
  sensitive = true
}
```

`terraform output` hides it in the list, but `terraform output db_password` or `terraform output -json` shows the real value. So anyone who can read state can still see it.

## 63: How do you validate input variables?

Add a `validation` block with a `condition` and an `error_message`. If the condition is false, Terraform stops with your message.

```hcl
variable "environment" {
  type = string

  validation {
    condition     = contains(["dev", "staging", "prod"], var.environment)
    error_message = "environment must be dev, staging or prod."
  }
}
```

You can have several `validation` blocks. Since Terraform 1.9, conditions can also refer to other variables, data sources and locals, not just the variable being checked.

## 64: What does nullable = false do on a variable?

By default a caller can pass `null` to a variable, and the variable becomes null even if it has a default. With `nullable = false`, passing `null` makes Terraform use the default instead (or fail if there is no default).

```hcl
variable "retention_days" {
  type     = number
  default  = 30
  nullable = false
}
```

This is useful in modules where callers do things like `retention_days = var.maybe_null`.

## 65: What does terraform show do?

`terraform show` prints the current state in a human-readable form. If you give it a saved plan file, it prints that plan instead.

```bash
terraform show                  # current state
terraform show tfplan           # saved plan
terraform show -json tfplan     # plan as JSON, used by policy tools
```

The JSON output is what tools like OPA, Checkov and Infracost read.

## 66: How do you see which resources are in the state?

Use `terraform state list`. To see the attributes of one resource, use `terraform state show`.

```bash
terraform state list
# aws_instance.web
# aws_s3_bucket.logs
# module.vpc.aws_vpc.this[0]

terraform state show aws_instance.web
```

`terraform state list` also accepts a filter, like `terraform state list module.vpc`.

## 67: What is a backend?

A backend decides where Terraform stores state. The default is the `local` backend, which writes `terraform.tfstate` in the working directory.

Remote backends store state somewhere shared, like S3, Azure Blob Storage, Google Cloud Storage, Consul, PostgreSQL, Kubernetes or HCP Terraform. Most remote backends also support state locking.

Backends are configured inside the `terraform` block. After changing the backend you must run `terraform init` again.

## 68: Why should teams use a remote backend?

With local state, the state file lives on one person's laptop. That causes problems:

- Others cannot run Terraform, or they run it with stale state and break things
- Two people can run `apply` at the same time and corrupt state
- The file can be lost
- It often ends up in Git, which leaks secrets

A remote backend keeps one shared copy, supports locking, can be encrypted and versioned, and works with CI/CD.

## 69: How do you configure the S3 backend?

```hcl
terraform {
  backend "s3" {
    bucket       = "acme-terraform-state"
    key          = "prod/network/terraform.tfstate"
    region       = "eu-central-1"
    encrypt      = true
    use_lockfile = true
  }
}
```

`use_lockfile = true` enables native S3 locking, which writes a `.tflock` file next to the state. It was added in Terraform 1.10 and replaces the older `dynamodb_table` setting, which is now deprecated. Turn on bucket versioning so you can recover old state versions.

## 70: What is state locking?

State locking stops two Terraform runs from writing the same state at the same time. When a run starts an operation that can change state, it takes a lock. Another run that tries to start waits or fails with a "state locked" error.

Without locking, two parallel applies can overwrite each other's changes and corrupt the state. Most remote backends lock automatically. If a run crashes and leaves a stale lock, you can remove it with `terraform force-unlock <LOCK_ID>`, but only after making sure nobody else is running.

## 71: Should you commit the state file to Git?

No. State often contains secrets in plain text (passwords, keys, connection strings), Git has no locking, and people forget to pull before running Terraform, which leads to stale or conflicting state. Use a remote backend instead and add `*.tfstate` to `.gitignore`.

## 72: Why can the state file contain secrets?

Terraform stores all attributes of every resource in state, including sensitive ones. For example, the password of an `aws_db_instance`, the result of `random_password`, or private keys from the `tls` provider. Marking them `sensitive` only hides them from the terminal.

That's why you should treat state as a secret: encrypt it at rest, limit who can read it, and avoid putting secrets in Terraform where possible. Newer features like ephemeral resources and write-only arguments let you pass some secrets without saving them in state.

## 73: What is drift?

Drift is when the real infrastructure no longer matches what Terraform has in state and in code. It usually happens when someone changes something by hand in the console, or another tool changes it.

`terraform plan` detects drift by refreshing state, and then proposes to change things back to match your code. HCP Terraform can also run drift detection on a schedule.

## 74: What is a refresh-only plan?

A refresh-only plan updates the state to match the real infrastructure without changing any resources.

```bash
terraform plan -refresh-only    # show what changed outside Terraform
terraform apply -refresh-only   # accept those changes into state
```

It replaces the old `terraform refresh` command, which updated state without showing you anything first. `terraform refresh` still exists but is deprecated because it was unsafe.

## 75: How do you force Terraform to recreate a resource?

Use the `-replace` option:

```bash
terraform plan -replace="aws_instance.web"
terraform apply -replace="aws_instance.web"
```

Terraform plans a replacement even though nothing changed in the code. This is the modern replacement for `terraform taint`, which marked a resource in state so the next apply would recreate it. `taint` is deprecated because it changes state before you see a plan.

## 76: How do you bring an existing resource under Terraform management?

Use an `import` block (Terraform 1.5 and later). You write the resource and an `import` block that maps it to the real ID, then run `plan` and `apply`.

```hcl
import {
  to = aws_s3_bucket.logs
  id = "my-existing-logs-bucket"
}

resource "aws_s3_bucket" "logs" {
  bucket = "my-existing-logs-bucket"
}
```

After the import is applied, you can delete the `import` block. The older way is the `terraform import aws_s3_bucket.logs my-existing-logs-bucket` command, which changes state right away with no plan.

## 77: Can Terraform generate the code for imported resources?

Yes. With `import` blocks, you can ask Terraform to write the resource configuration for you:

```bash
terraform plan -generate-config-out=generated.tf
```

For each `import` block whose target resource does not exist in your code, Terraform writes a resource block into `generated.tf` based on the real object. You usually need to clean it up (remove defaults, replace hard-coded IDs with references) before you keep it.

## 78: What are workspaces?

Workspaces (CLI workspaces) let one configuration have several separate state files. Each workspace has its own state, but they all share the same code and backend.

```bash
terraform workspace new staging
terraform workspace select staging
terraform workspace list
terraform workspace show
```

Every configuration starts with a workspace named `default`. Note that HCP Terraform also uses the word "workspace", but there it means something bigger: a whole unit with its own state, variables, settings and runs.

## 79: How do you use the current workspace name in your code?

Use `terraform.workspace`.

```hcl
locals {
  env = terraform.workspace
}

resource "aws_instance" "web" {
  instance_type = local.env == "prod" ? "m6i.large" : "t3.micro"
  ami           = var.ami_id

  tags = {
    Name = "web-${local.env}"
  }
}
```

This works, but if dev and prod differ a lot, the code fills up with conditions. Many teams prefer separate directories or separate tfvars per environment.

## 80: What are provisioners?

Provisioners run scripts on a local or remote machine as part of creating or destroying a resource. The built-in ones are:

- `local-exec` runs a command on the machine running Terraform
- `remote-exec` runs commands on the created resource over SSH or WinRM
- `file` copies files to the created resource

```hcl
resource "aws_instance" "web" {
  # ...
  provisioner "local-exec" {
    command = "echo ${self.private_ip} >> inventory.txt"
  }
}
```

By default they run at creation. With `when = destroy` they run before the resource is deleted.

## 81: Why are provisioners called a last resort?

HashiCorp's docs say to use provisioners only when nothing else works, because:

- Terraform cannot track what they did, so they are not part of the plan
- They run only once at creation, so changes to the script do nothing later
- A failed provisioner marks the resource as tainted
- `remote-exec` needs network access and credentials to the machine

Better options are `user_data` or cloud-init, pre-built images (made with Packer), configuration management tools like Ansible, or a provider resource that does the job natively.

## 82: What is terraform_data?

`terraform_data` is a built-in resource (Terraform 1.4 and later) that does not create anything real. It stores values in state and can be used to run provisioners or trigger replacements.

```hcl
resource "terraform_data" "migrate" {
  triggers_replace = [var.app_version]

  provisioner "local-exec" {
    command = "./run-migrations.sh"
  }
}
```

When `app_version` changes, the resource is replaced and the provisioner runs again. It replaces `null_resource` from the `hashicorp/null` provider, which you will still see in older code.

## 83: What is null_resource?

`null_resource` comes from the `hashicorp/null` provider. Like `terraform_data`, it does nothing by itself. It was used to attach provisioners and rerun them through its `triggers` map.

```hcl
resource "null_resource" "example" {
  triggers = {
    version = var.app_version
  }

  provisioner "local-exec" {
    command = "echo deploy"
  }
}
```

In new code use `terraform_data` instead, because it is built in and does not need an extra provider. You can move from one to the other with a `moved` block (supported since Terraform 1.9).

## 84: What is the random provider used for?

The `hashicorp/random` provider generates random values that stay the same between runs because they are saved in state. Common resources:

- `random_id` random bytes, often used for unique bucket name suffixes
- `random_password` passwords (marked sensitive)
- `random_string`, `random_pet`, `random_integer`, `random_shuffle`, `random_uuid`

```hcl
resource "random_id" "suffix" {
  byte_length = 4
}

resource "aws_s3_bucket" "data" {
  bucket = "myapp-data-${random_id.suffix.hex}"
}
```

## 85: How do you use the same provider with different settings, like two AWS regions?

Use provider aliases. You define extra provider blocks with an `alias`, then pick one with the `provider` meta-argument.

```hcl
provider "aws" {
  region = "eu-central-1"
}

provider "aws" {
  alias  = "us"
  region = "us-east-1"
}

resource "aws_acm_certificate" "cdn" {
  provider          = aws.us
  domain_name       = "example.com"
  validation_method = "DNS"
}
```

Resources without `provider` use the default (unaliased) provider block.

## 86: How do providers get credentials?

Each provider has its own options, but they usually support (in this order of preference):

- Environment variables, like `AWS_PROFILE`, `AWS_ACCESS_KEY_ID`, `ARM_CLIENT_ID`, `GOOGLE_APPLICATION_CREDENTIALS`
- Shared config files, like `~/.aws/config`
- Workload identity, like an IAM role on an EC2 instance or OIDC in CI
- Arguments in the provider block

Never hard-code keys in the provider block. In CI/CD, OIDC is the best choice because there are no long-lived keys at all.

## 87: How do you debug Terraform?

Set the `TF_LOG` environment variable to get detailed logs.

```bash
TF_LOG=DEBUG terraform plan
TF_LOG=TRACE TF_LOG_PATH=./tf.log terraform apply
```

Levels are `TRACE`, `DEBUG`, `INFO`, `WARN` and `ERROR`. You can also set `TF_LOG_CORE` and `TF_LOG_PROVIDER` separately to only log Terraform core or only providers. The logs can contain secrets, so don't share them as is.

## 88: What other environment variables does Terraform use?

Some common ones:

- `TF_VAR_<name>` sets an input variable
- `TF_LOG`, `TF_LOG_PATH` logging
- `TF_INPUT=0` disables interactive prompts
- `TF_CLI_ARGS` and `TF_CLI_ARGS_plan` extra arguments added to commands
- `TF_DATA_DIR` changes the location of `.terraform`
- `TF_WORKSPACE` selects a workspace
- `TF_PLUGIN_CACHE_DIR` shared folder for downloaded providers
- `TF_IN_AUTOMATION` makes output a bit more suited to CI

## 89: What is a resource address?

A resource address is the string that points to a resource instance in state. It is used by `state`, `-target`, `-replace`, `import` and `moved`.

```text
aws_instance.web
aws_instance.web[0]
aws_s3_bucket.this["logs"]
data.aws_ami.ubuntu
module.vpc.aws_subnet.private[1]
module.app["api"].aws_ecs_service.this
```

The pattern is `[module path.]type.name[index or key]`.

## 90: What is the difference between an argument and a nested block?

An argument assigns a value with `=`. A nested block has a block type and a body in braces, and can usually be repeated.

```hcl
resource "aws_security_group" "web" {
  name   = "web"          # argument
  vpc_id = var.vpc_id     # argument

  ingress {               # nested block
    from_port   = 443
    to_port     = 443
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }
}
```

The provider schema decides whether something is an argument or a block.

## 91: What is the timeouts block?

Some resources let you change how long Terraform waits for create, update and delete operations before failing.

```hcl
resource "aws_db_instance" "main" {
  # ...
  timeouts {
    create = "60m"
    delete = "2h"
  }
}
```

Only resources that support it accept a `timeouts` block. Check the provider docs.

## 92: What are default_tags in the AWS provider?

`default_tags` in the AWS provider block adds tags to every resource that supports tags, so you don't repeat them in each resource.

```hcl
provider "aws" {
  region = "eu-central-1"

  default_tags {
    tags = {
      Project   = "shop"
      ManagedBy = "terraform"
    }
  }
}
```

Tags set on a resource are merged with the default tags. If the same key appears in both, the resource tag wins.

## 93: How is Terraform different from AWS CloudFormation?

- **Clouds:** CloudFormation only works with AWS. Terraform works with any provider.
- **State:** CloudFormation keeps state inside AWS for you. Terraform needs you to store state.
- **Language:** CloudFormation uses JSON or YAML. Terraform uses HCL, which has better expressions and functions.
- **Rollback:** CloudFormation rolls back a failed stack update automatically. Terraform stops where it failed and leaves partial changes.
- **New services:** CloudFormation usually supports new AWS services on day one. The Terraform AWS provider is usually quick but can lag a bit.

## 94: How is Terraform different from Ansible?

Terraform is mainly for provisioning infrastructure (creating cloud resources) and is declarative with state. Ansible is mainly for configuration management (installing packages, editing files, running services on servers). It is procedural with tasks run in order, and does not keep state.

They overlap a little, but they work well together: Terraform creates the servers, Ansible configures them.

## 95: How is Terraform different from Pulumi?

Both are multi-cloud IaC tools with state. The main difference is the language. Terraform uses HCL. Pulumi uses general programming languages like TypeScript, Python, Go and C#, so you get loops, classes, packages and unit tests from that language.

HCL is simpler and more limited, which some teams like because configurations stay predictable. Pulumi gives more power and flexibility. Pulumi can also use many Terraform providers through a bridge.

## 96: What is OpenTofu?

OpenTofu is an open source fork of Terraform, created in 2023 after HashiCorp changed Terraform's license. It is run under the Linux Foundation and uses the MPL 2.0 license.

It started from Terraform 1.5 and stays mostly compatible: same HCL, same providers, same state format for most use cases. The CLI is called `tofu`. Since the fork, both projects added their own features, for example OpenTofu has built-in state encryption, so they are slowly drifting apart.

## 97: What is the Terraform license?

Since August 2023 (version 1.6 and later), Terraform uses the Business Source License (BSL 1.1). Before that it used the open source MPL 2.0.

For most users nothing changed: you can use Terraform freely for your own infrastructure. The BSL limits companies from offering Terraform as a competing commercial product. The change is what led to the OpenTofu fork. HashiCorp itself was bought by IBM, and the deal closed in early 2025.

## 98: What is HCP Terraform?

HCP Terraform (formerly Terraform Cloud) is HashiCorp's hosted service for running Terraform. It gives you:

- Remote state storage with locking and history
- Remote plan and apply runs
- VCS integration (runs on pull requests and merges)
- Variables and secrets per workspace
- A private module and provider registry
- Policy checks with Sentinel or OPA
- Team permissions, drift detection, run triggers and audit logs

There is a free tier with limits and paid tiers.

## 99: What is Terraform Enterprise?

Terraform Enterprise is the self-hosted version of HCP Terraform. It has the same features, but you run it on your own servers or Kubernetes cluster. Companies use it when they cannot use a SaaS product for security, compliance or network reasons.

## 100: What does idempotent mean for Terraform?

Running `terraform apply` many times with the same code and no outside changes gives the same result. After the first apply, later runs show "No changes. Your infrastructure matches the configuration."

If a plan keeps showing changes on every run, something is wrong. Common causes are a value that changes every time (like `timestamp()`), a provider that normalizes a value differently (like JSON key order), or another tool modifying the resource.

## 101: What is immutable infrastructure and how does Terraform support it?

Immutable infrastructure means you don't change servers after they are created. To update, you build a new one and throw away the old one. This avoids servers that slowly drift into unique, hard-to-rebuild states.

Terraform fits this well. For example, you change the AMI ID of an instance, and Terraform replaces the instance instead of patching it. Combined with `create_before_destroy`, an image built with Packer, and a load balancer or autoscaling group, you get rollouts with no manual server changes.

## 102: What is the difference between an in-place update and a replacement?

Some attributes can be changed on an existing resource through the API, like tags or the instance type of a stopped instance. Terraform does an in-place update (`~` in the plan).

Other attributes cannot be changed after creation, like the AMI of an EC2 instance or the name of an RDS instance in some cases. Changing them forces a replacement (`-/+`), and the plan marks the attribute with `# forces replacement`. Always look for this in plans, because replacing a database or a disk can mean data loss.

## 103: What does the -target option do?

`-target` limits a plan or apply to one resource or module and its dependencies.

```bash
terraform plan -target=aws_instance.web
terraform apply -target=module.vpc
```

It is meant for exceptional cases, like recovering from an error or breaking a dependency loop. Terraform prints a warning when you use it. Using it as part of the normal workflow leaves your state partly out of sync with your code.

## 104: What does terraform graph do?

`terraform graph` prints the dependency graph in DOT format, which you can turn into an image with Graphviz.

```bash
terraform graph | dot -Tsvg > graph.svg
```

It is useful for understanding why Terraform creates things in a certain order or for spotting unexpected dependencies. For large configurations the graph can be hard to read.

## 105: What does terraform providers do?

`terraform providers` shows which providers the configuration needs and which module requires each one. It helps when you get version conflicts between modules.

Related subcommands:

- `terraform providers lock` updates the lock file, for example for several platforms
- `terraform providers mirror` downloads providers into a local folder for offline use
- `terraform providers schema -json` prints the full schema of each provider

## 106: How do you add checksums for other platforms to the lock file?

By default `terraform init` only records checksums for your own OS and CPU. If a teammate uses a Mac with an ARM chip and CI runs on Linux, the lock file may be missing hashes. Add them with:

```bash
terraform providers lock \
  -platform=linux_amd64 \
  -platform=darwin_arm64 \
  -platform=windows_amd64
```

Then commit the updated `.terraform.lock.hcl`.

## 107: What does terraform login do?

`terraform login` gets an API token for HCP Terraform (or Terraform Enterprise, or another compatible host) and saves it in `~/.terraform.d/credentials.tfrc.json`. Terraform uses it to reach remote state, run remote operations and download private modules. `terraform logout` removes it.

In CI you usually set the token with the `TF_TOKEN_app_terraform_io` environment variable instead.

## 108: What does -detailed-exitcode do?

With `terraform plan -detailed-exitcode` the exit code tells you what the plan found:

- `0` no changes
- `1` error
- `2` the plan succeeded and there are changes

This is useful in scripts and CI, for example to detect drift on a schedule and send an alert when the code is `2`.

## 109: Which options are useful when running Terraform in CI?

```bash
terraform init -input=false
terraform plan -input=false -out=tfplan
terraform apply -input=false tfplan
```

- `-input=false` fails instead of waiting for input that will never come
- `-out=tfplan` saves the plan so the apply does exactly what was reviewed
- `-no-color` removes color codes from logs
- `-lock-timeout=5m` waits for a lock instead of failing at once

Setting `TF_IN_AUTOMATION=true` also changes some messages to make more sense in CI.

## 110: What does -parallelism do?

Terraform runs up to 10 resource operations at the same time by default. `-parallelism=N` changes that number.

```bash
terraform apply -parallelism=20
```

Raising it can speed up big applies. Lowering it helps when a provider hits API rate limits.

## 111: What happens if terraform apply fails halfway?

Terraform does not roll back. Resources that were created successfully stay created and are saved in state. The failed resource may be missing, or created but marked as tainted (so it gets replaced next time). Resources that depend on it are not touched.

Usually you fix the problem (permissions, quotas, a bad value) and run `apply` again. Terraform picks up where it stopped because the state shows what already exists.

## 112: How do you access elements of lists, maps and objects?

```hcl
var.subnets[0]                 # first element of a list
var.amis["eu-central-1"]       # map value by key
var.database.engine            # object attribute
var.servers["web"].ports[0]    # nested
```

Accessing an index or key that does not exist is an error. Use `lookup()` or `try()` when the key may be missing.

## 113: What does null mean in Terraform?

`null` means "no value". If you set a resource argument to `null`, Terraform acts as if you did not set it at all, so the provider uses its default.

```hcl
resource "aws_instance" "web" {
  ami           = var.ami_id
  instance_type = "t3.micro"
  key_name      = var.enable_ssh ? var.key_name : null
}
```

This makes it easy to set an argument only in some cases without duplicating the resource.

## 114: Does Terraform convert types automatically?

Yes, when the conversion is safe. A string `"5"` can be used where a number is needed, and `true` can become the string `"true"`. A tuple can become a list and an object can become a map if all values have the same type.

If conversion is not possible (like `"abc"` to a number), you get an error. You can also convert explicitly with `tostring`, `tonumber`, `tobool`, `tolist`, `toset` and `tomap`.

## 115: What do the length, join and split functions do?

```hcl
length(["a", "b", "c"])          # 3
length("hello")                  # 5
length({ a = 1, b = 2 })         # 2

join(",", ["a", "b", "c"])       # "a,b,c"
split(",", "a,b,c")              # ["a", "b", "c"]
```

`length` works on strings, lists, sets, maps, tuples and objects.

## 116: What does the format function do?

`format` builds a string from a template with placeholders, like `printf`.

```hcl
format("web-%02d", 3)                 # "web-03"
format("%s-%s", var.project, "logs")  # "shop-logs"
```

`formatlist` does the same for each element of a list:

```hcl
formatlist("arn:aws:s3:::%s/*", ["a", "b"])
# ["arn:aws:s3:::a/*", "arn:aws:s3:::b/*"]
```

## 117: What does cidrsubnet do?

`cidrsubnet(prefix, newbits, netnum)` calculates a subnet inside a bigger network. `newbits` is how many bits to add to the prefix length, and `netnum` is which subnet to pick.

```hcl
cidrsubnet("10.0.0.0/16", 8, 0)   # "10.0.0.0/24"
cidrsubnet("10.0.0.0/16", 8, 1)   # "10.0.1.0/24"
cidrsubnet("10.0.0.0/16", 4, 2)   # "10.0.32.0/20"
```

It is commonly used with `count` or `for_each` to create one subnet per availability zone without hard-coding CIDRs.

## 118: How do you write an IAM policy in Terraform without raw JSON strings?

Use `jsonencode` with an HCL object, or the `aws_iam_policy_document` data source.

```hcl
resource "aws_iam_policy" "read_logs" {
  name = "read-logs"
  policy = jsonencode({
    Version = "2012-10-17"
    Statement = [{
      Effect   = "Allow"
      Action   = ["s3:GetObject"]
      Resource = "${aws_s3_bucket.logs.arn}/*"
    }]
  })
}
```

Both approaches give you syntax checking and references to other resources, which a heredoc JSON string does not.

## 119: What is the self object?

`self` refers to the current resource. It can only be used inside `provisioner`, `connection` blocks and `postcondition` blocks, where referring to the resource by name would create a cycle.

```hcl
resource "aws_instance" "web" {
  # ...
  provisioner "local-exec" {
    command = "echo ${self.public_ip}"
  }
}
```

## 120: What is terraform.tfstate.backup?

With the local backend, Terraform keeps the previous version of the state in `terraform.tfstate.backup` every time it writes a new state. If the new state is broken, you can restore the old one from it. Remote backends don't create this file. Instead, you rely on the backend's versioning, like S3 bucket versioning or the state history in HCP Terraform.

## 121: What is a moved block?

A `moved` block tells Terraform that a resource got a new address, so it should update the state instead of deleting the old resource and creating a new one.

```hcl
moved {
  from = aws_instance.server
  to   = aws_instance.web
}
```

You use it when you rename a resource, move it into a module, or switch from `count` to `for_each`. It was added in Terraform 1.1 and is the code-based replacement for `terraform state mv`.

## 122: What does "known after apply" mean in a plan?

Some attributes are only known after the resource is created, like an instance ID, an IP address or an ARN. In the plan, Terraform shows them as `(known after apply)`.

Anything that depends on such a value is also unknown during the plan. This is why you sometimes cannot use those values in places that must be known during planning, like `count` or `for_each`.

## 123: When does Terraform read data sources?

Normally data sources are read during the plan, so their values are available for planning. If a data source's arguments depend on values that are only known after apply, or it depends on a resource with pending changes, Terraform waits and reads it during the apply instead. The plan shows `<= read (data resources)` for those.

## 124: What does terraform state rm do?

`terraform state rm` removes a resource from state without deleting the real object. Terraform simply forgets it.

```bash
terraform state rm aws_s3_bucket.old_logs
```

You use it when something should no longer be managed by this configuration, for example when you move it to another state. Since Terraform 1.7 the `removed` block does the same thing through code and a plan, which is safer.

## 125: What does terraform state mv do?

`terraform state mv` changes the address of a resource in state, so Terraform does not destroy and recreate it after you rename or move it in the code.

```bash
terraform state mv aws_instance.server aws_instance.web
terraform state mv aws_instance.web module.app.aws_instance.web
```

It changes state right away, without a plan, and every teammate has to know about it. The `moved` block is preferred today because it goes through code review and a plan.

## 126: What is the cloud block?

The `cloud` block inside the `terraform` block connects a configuration to HCP Terraform or Terraform Enterprise. It is used instead of a `backend` block.

```hcl
terraform {
  cloud {
    organization = "acme"

    workspaces {
      name = "shop-prod"
    }
  }
}
```

You can also select several workspaces with `tags`. The older way to do this was the `remote` backend, which still works but is not recommended for new setups.

## 127: What is the provider plugin cache?

By default every working directory downloads its own copy of each provider into `.terraform`. With many projects this wastes disk space and time. The plugin cache keeps one shared copy.

```bash
export TF_PLUGIN_CACHE_DIR="$HOME/.terraform.d/plugin-cache"
mkdir -p "$TF_PLUGIN_CACHE_DIR"
```

You can also set `plugin_cache_dir` in the CLI config file (`~/.terraformrc`). It is especially useful in CI agents.

## 128: What happens if someone deletes a Terraform-managed resource by hand?

On the next plan, Terraform refreshes state, sees that the object is gone, and plans to create it again. The resource was removed from state during the refresh, and your code still says it should exist.

If the deletion was intentional, remove the resource from the code as well (or use a `removed` block if it was already removed from state).

## 129: How do you install Terraform and manage several versions?

You can download the binary from `developer.hashicorp.com/terraform/install`, or use a package manager (`brew install hashicorp/tap/terraform`, apt or yum repositories from HashiCorp, or Chocolatey).

When different projects need different versions, people use version managers like `tfenv` or `tenv`. They read a `.terraform-version` file in the project and switch versions automatically.

## 130: What does the -chdir option do?

`-chdir` runs Terraform as if you had changed into another directory first. It goes before the subcommand.

```bash
terraform -chdir=environments/prod init
terraform -chdir=environments/prod plan
```

It is handy in scripts and CI where you don't want to `cd` around.

## 131: What are override files?

Files named `override.tf`, `override.tf.json` or ending in `_override.tf` are loaded last, and their blocks are merged into existing blocks with the same name instead of being added as new ones.

They can be used for local tweaks that should not be committed. In general they make code harder to understand, so most teams avoid them and add them to `.gitignore`.

## 132: What naming conventions are common in Terraform?

- Use `snake_case` for resource names, variables, outputs and locals: `aws_instance.web_server`
- Don't repeat the resource type in the name: `aws_s3_bucket.logs`, not `aws_s3_bucket.logs_bucket`
- Use `this` or `main` when a module has only one resource of that type
- Use nouns, not verbs
- Use plural names for variables that hold lists or maps: `subnet_ids`
- Add units to number variables where it helps: `disk_size_gb`, `timeout_seconds`

## 133: Why should variables and outputs have descriptions?

The `description` shows up in generated docs (like `terraform-docs`), in the registry, in HCP Terraform, and when Terraform prompts for a missing value. It tells users of the module what each input means and what values are expected, which saves them from reading the module code.

```hcl
variable "retention_days" {
  type        = number
  description = "Number of days to keep logs. Use 0 to keep them forever."
  default     = 30
}
```

## 134: What do try and can do?

`try` evaluates its arguments in order and returns the first one that doesn't cause an error.

```hcl
locals {
  port = try(var.settings.port, 8080)
}
```

`can` returns `true` if an expression works and `false` if it fails. It is mostly used in validation.

```hcl
validation {
  condition     = can(regex("^ami-", var.ami_id))
  error_message = "ami_id must start with ami-."
}
```

## 135: What does coalesce do?

`coalesce` returns the first argument that is not `null` or an empty string.

```hcl
locals {
  name = coalesce(var.custom_name, "${var.project}-default")
}
```

For lists there is `coalescelist`, which returns the first non-empty list.

## 136: Why can't you pass a list directly to for_each?

`for_each` only accepts a map or a set of strings. A list is not allowed, because lists can have duplicates and their order gives no stable key. Convert it with `toset()`:

```hcl
variable "users" {
  type    = list(string)
  default = ["alice", "bob"]
}

resource "aws_iam_user" "this" {
  for_each = toset(var.users)
  name     = each.value
}
```

For a set, `each.key` and `each.value` are the same.

## 137: What do keys and values do?

`keys` returns the keys of a map as a sorted list, and `values` returns the values in the same order.

```hcl
keys({ b = 2, a = 1 })     # ["a", "b"]
values({ b = 2, a = 1 })   # [1, 2]
```

They are handy for turning a `for_each` resource into a list, like `values(aws_instance.web)[*].id`.

## 138: What does flatten do?

`flatten` turns a list of lists into a single flat list.

```hcl
flatten([["a", "b"], [], ["c"]])   # ["a", "b", "c"]
```

It is often used with nested `for` expressions when you need one resource per combination of two things, like one subnet per network per zone.

## 139: What is the difference between element and index access?

`list[i]` fails if `i` is out of range. `element(list, i)` wraps around: if `i` is bigger than the list, it starts again from the beginning.

```hcl
element(["a", "b", "c"], 4)   # "b"
```

This is useful to spread resources over a fixed number of availability zones with `count.index`. Negative indexes are not allowed in either case. To get the last element, use `element(list, length(list) - 1)` or `list[length(list) - 1]`.

## 140: What does contains do?

`contains(list, value)` returns `true` if the list or set contains the value.

```hcl
contains(["dev", "staging"], var.environment)
```

It is common in validation blocks and conditional expressions.

## 141: Why is using timestamp() in a resource a problem?

`timestamp()` returns the current time on every run. If you put it in a resource argument, like a tag, the value is different on every plan, so Terraform always shows a change.

If you need a time value that stays the same, use the `time_static` resource from the `hashicorp/time` provider, or `plantimestamp()`, or ignore the attribute with `ignore_changes`.

## 142: What does terraform state pull do?

`terraform state pull` downloads the current state from the backend and prints it as JSON. It is useful for inspecting remote state or making a manual backup.

```bash
terraform state pull > backup.tfstate
```

There is also `terraform state push`, which uploads a local state file to the backend. Use it very carefully because it can overwrite good state.

## 143: How does a destroy-time provisioner work?

A provisioner with `when = destroy` runs before the resource is deleted. You can use it for cleanup, like removing a node from a cluster.

```hcl
resource "aws_instance" "node" {
  # ...
  provisioner "local-exec" {
    when    = destroy
    command = "./deregister.sh ${self.id}"
  }
}
```

Destroy provisioners can only reference `self`, `count.index` and `each.key`, not other resources or variables. They don't run if you remove the resource block together with the provisioner, or if the resource is tainted. They are not reliable for important cleanup.

## 144: How does Packer relate to Terraform?

Packer is another HashiCorp tool that builds machine images (like AWS AMIs, Azure images or Docker images) from a template. Terraform then uses those images to create servers.

A typical setup: Packer builds an AMI with your app and settings baked in, Terraform looks up the newest AMI with a data source and creates the instances. This keeps servers immutable and fast to start.

## 145: What are the main block types in Terraform?

- `terraform` settings, required providers and backend
- `provider` provider configuration
- `resource` managed infrastructure
- `data` data sources
- `variable` inputs
- `output` outputs
- `locals` local values
- `module` calls a child module
- `import`, `moved`, `removed` refactoring and importing
- `check` health checks and assertions
- `ephemeral` ephemeral resources (Terraform 1.10 and later)

Newer versions also add blocks like `action` and `list` (Terraform 1.14).

## 146: What is terraform-docs?

`terraform-docs` is a popular open source tool that generates documentation for a module from its code: inputs, outputs, providers, resources and their descriptions. It can write a Markdown table straight into the module's `README.md`.

```bash
terraform-docs markdown table --output-file README.md ./modules/vpc
```

Teams often run it in a pre-commit hook so the docs never get out of date.

## 147: What is TFLint?

TFLint is a linter for Terraform. It catches problems that `terraform validate` does not, such as:

- Invalid instance types or regions (with provider-specific plugins)
- Unused variables and declarations
- Deprecated syntax
- Naming convention violations

```bash
tflint --init
tflint --recursive
```

It is commonly run in CI and pre-commit hooks along with `terraform fmt -check` and `terraform validate`.

## 148: Which checks do teams usually run in pre-commit hooks for Terraform?

The `pre-commit-terraform` project bundles common hooks:

- `terraform_fmt` formatting
- `terraform_validate` validation
- `terraform_tflint` linting
- `terraform_docs` updating module docs
- `terraform_trivy` or `terraform_checkov` security scanning

Running them before each commit catches simple mistakes before they reach a pull request.

## 149: What does a typical Terraform workflow look like in a team?

1. Write or change code on a feature branch
2. Run `fmt`, `validate` and linting locally
3. Open a pull request
4. CI runs `terraform plan` and posts the output on the pull request
5. A teammate reviews both the code and the plan
6. After merge, CI (or HCP Terraform) runs `terraform apply` using the reviewed plan or a fresh one
7. State is stored remotely with locking

Nobody runs `apply` from a laptop against production.

## 150: What are some basic Terraform best practices?

- Store state in a remote backend with locking and encryption
- Pin Terraform, provider and module versions, and commit the lock file
- Never put secrets in code or tfvars files that go to Git
- Split big configurations into smaller ones (network, data, app)
- Use modules for repeated patterns, but don't wrap every single resource
- Review the plan before every apply
- Run Terraform from CI, not from laptops, for shared environments
- Use `prevent_destroy` on critical resources
- Format, validate and lint code automatically

# Moderate Questions (151-300)

## 151: When should you use count and when for_each?

Use `count` when:

- You just need N identical copies
- You want a simple on/off switch (`count = var.enabled ? 1 : 0`)

Use `for_each` when:

- Each instance is different (different name, size, settings)
- Items may be added or removed from the middle of the collection

For anything built from a list of named things, `for_each` is almost always the better choice, because instances are tracked by key instead of by position.

## 152: What is the problem with count when you remove an item from the middle of a list?

`count` tracks instances by index. If you have `["a", "b", "c"]` and remove `"b"`, then `"c"` moves from index 2 to index 1. Terraform sees that `[1]` changed from `b` to `c` and `[2]` disappeared, so it updates or replaces `[1]` and destroys `[2]`.

```hcl
resource "aws_iam_user" "this" {
  count = length(var.users)
  name  = var.users[count.index]
}
```

With `for_each = toset(var.users)`, removing `"b"` only destroys `aws_iam_user.this["b"]`. The others are not touched.

## 153: How do you switch a resource from count to for_each without recreating it?

Add `moved` blocks that map each old index to the new key, then run a plan to check that nothing is destroyed.

```hcl
resource "aws_iam_user" "this" {
  for_each = toset(["alice", "bob"])
  name     = each.value
}

moved {
  from = aws_iam_user.this[0]
  to   = aws_iam_user.this["alice"]
}

moved {
  from = aws_iam_user.this[1]
  to   = aws_iam_user.this["bob"]
}
```

The plan should say the resources "have moved" with no create or destroy actions.

## 154: What is a dynamic block?

A `dynamic` block generates repeated nested blocks from a collection. It works like `for_each` but for nested blocks inside a resource.

```hcl
variable "ingress_ports" {
  type    = list(number)
  default = [80, 443]
}

resource "aws_security_group" "web" {
  name   = "web"
  vpc_id = var.vpc_id

  dynamic "ingress" {
    for_each = var.ingress_ports
    content {
      from_port   = ingress.value
      to_port     = ingress.value
      protocol    = "tcp"
      cidr_blocks = ["0.0.0.0/0"]
    }
  }
}
```

The iterator is named after the block (`ingress`) unless you set `iterator = "port"`. It has `.key` and `.value`.

## 155: When should you avoid dynamic blocks?

Dynamic blocks make code harder to read. HashiCorp recommends using them only when you really need to build blocks from input data, mostly in reusable modules.

If you have two fixed `ingress` rules, just write them out. Also check if the provider has a separate resource for the thing, like `aws_vpc_security_group_ingress_rule`, which is often better than nested blocks.

## 156: How do you create resources for every combination of two lists?

Use nested `for` expressions with `flatten`, then turn the result into a map for `for_each`.

```hcl
locals {
  networks = {
    app = "10.0.0.0/16"
    db  = "10.1.0.0/16"
  }
  zones = ["eu-central-1a", "eu-central-1b"]

  subnets = flatten([
    for net_name, cidr in local.networks : [
      for i, zone in local.zones : {
        key  = "${net_name}-${zone}"
        cidr = cidrsubnet(cidr, 8, i)
        zone = zone
      }
    ]
  ])
}

resource "aws_subnet" "this" {
  for_each          = { for s in local.subnets : s.key => s }
  vpc_id            = var.vpc_id
  cidr_block        = each.value.cidr
  availability_zone = each.value.zone
}
```

`setproduct` is another option when you only need the combinations.

## 157: Can you use for_each and count on modules?

Yes, since Terraform 0.13. Each instance of the module gets its own address.

```hcl
module "service" {
  source   = "./modules/ecs-service"
  for_each = {
    api    = { cpu = 512, port = 8080 }
    worker = { cpu = 256, port = 0 }
  }

  name = each.key
  cpu  = each.value.cpu
  port = each.value.port
}

output "api_url" {
  value = module.service["api"].url
}
```

Resources inside are addressed like `module.service["api"].aws_ecs_service.this`.

## 158: How do you pass a provider configuration to a child module?

By default a child module uses the default provider configurations of its parent. To give it an aliased provider, use the `providers` map.

```hcl
provider "aws" {
  alias  = "us"
  region = "us-east-1"
}

module "cdn" {
  source = "./modules/cdn"
  providers = {
    aws = aws.us
  }
}
```

Inside the module, the resources just use `aws`, and it points to the `us-east-1` configuration.

## 159: What is configuration_aliases?

When a module needs more than one configuration of the same provider, it declares the extra names with `configuration_aliases`. The caller must then pass all of them.

```hcl
# inside the module
terraform {
  required_providers {
    aws = {
      source                = "hashicorp/aws"
      configuration_aliases = [aws.primary, aws.replica]
    }
  }
}

resource "aws_s3_bucket" "replica" {
  provider = aws.replica
  bucket   = "${var.name}-replica"
}
```

```hcl
# caller
module "storage" {
  source = "./modules/storage"
  providers = {
    aws.primary = aws
    aws.replica = aws.us
  }
}
```

## 160: Why shouldn't reusable modules contain provider blocks?

If a module has its own `provider` block:

- Callers cannot choose the region, account or credentials
- The module cannot be used with `count`, `for_each` or `depends_on`
- Removing the module from code is hard, because the provider config goes away together with the resources, so Terraform can't destroy them

Reusable modules should only declare `required_providers`. Provider blocks belong in the root module.

## 161: How should you version your own modules?

- Keep modules in their own Git repo (or a monorepo with clear tags)
- Tag releases with semantic versions like `v1.4.0`
- Bump the major version for breaking changes: removed variables, renamed outputs, changes that force resource replacement
- Pin the version in callers: `?ref=v1.4.0` for Git, `version = "~> 1.4"` for registry modules
- Keep a changelog

Pointing at `main` means any push can change your infrastructure on the next plan.

## 162: What is module composition?

Module composition means the root module wires together small, focused modules by passing outputs from one into another, instead of building deep chains of modules calling modules.

```hcl
module "network" {
  source = "./modules/network"
}

module "database" {
  source     = "./modules/database"
  subnet_ids = module.network.private_subnet_ids
}

module "app" {
  source       = "./modules/app"
  subnet_ids   = module.network.private_subnet_ids
  db_endpoint  = module.database.endpoint
}
```

HashiCorp recommends keeping the module tree flat (usually one level of child modules) because it is easier to understand and reuse.

## 163: How do you organize code for several environments?

There are three common approaches:

1. **Directory per environment:** `envs/dev`, `envs/prod`, each a root module calling shared modules, with its own backend. Clear and safe, a bit more code.
2. **One root module with a tfvars file per environment:** `-var-file=prod.tfvars`, with backend config passed at init. Less code, but you must be careful to pair the right vars with the right state.
3. **CLI workspaces:** same code and backend, different state per workspace. Simple, but easy to apply to the wrong one, and all environments must use the same backend and credentials.

Most teams pick option 1 or 2, often with Terragrunt or HCP Terraform workspaces on top.

## 164: What is the terraform_remote_state data source?

It reads the outputs of another Terraform configuration from its state.

```hcl
data "terraform_remote_state" "network" {
  backend = "s3"
  config = {
    bucket = "acme-terraform-state"
    key    = "prod/network/terraform.tfstate"
    region = "eu-central-1"
  }
}

resource "aws_instance" "app" {
  subnet_id     = data.terraform_remote_state.network.outputs.private_subnet_ids[0]
  ami           = var.ami_id
  instance_type = "t3.micro"
}
```

Only root module outputs are available.

## 165: What are the downsides of terraform_remote_state and what are the alternatives?

To read outputs, the consumer needs read access to the whole state file of the other project, which may contain secrets. It also creates a tight coupling to the backend layout.

Alternatives:

- Publish values to a store like AWS SSM Parameter Store, Consul or Azure App Configuration, and read them with a data source
- Look up resources directly with data sources by tag or name (like `data "aws_vpc"`)
- In HCP Terraform, use the `tfe_outputs` data source, which only exposes outputs

## 166: What is partial backend configuration?

You leave some or all backend settings out of the code and pass them at `terraform init`. This lets the same code use different state locations per environment.

```hcl
terraform {
  backend "s3" {}
}
```

```bash
terraform init -backend-config=backends/prod.hcl
terraform init -backend-config="key=prod/app.tfstate"
```

```hcl
# backends/prod.hcl
bucket       = "acme-tf-prod"
key          = "app/terraform.tfstate"
region       = "eu-central-1"
use_lockfile = true
```

## 167: Can you use variables in the backend block?

No. The backend is configured during `terraform init`, before variables are evaluated, so `var.` and `local.` references are not allowed there. Use partial configuration with `-backend-config`, environment variables supported by the backend, or a wrapper like Terragrunt.

## 168: How do you move state from one backend to another?

Change the backend block in the code, then run:

```bash
terraform init -migrate-state
```

Terraform asks whether to copy the existing state to the new backend. After that, check it with `terraform plan`, which should show no changes. Make a backup with `terraform state pull` before you start.

If you only want to point at a different backend without copying anything, use `terraform init -reconfigure`.

## 169: What is the difference between -migrate-state and -reconfigure?

- `-migrate-state` copies the state from the old backend to the new one.
- `-reconfigure` ignores the old backend settings and starts fresh with the new ones. Nothing is copied.

Use `-reconfigure` when switching between environments with partial backend configs. Use `-migrate-state` when you actually move state.

## 170: How do you configure the Azure and Google Cloud backends?

```hcl
terraform {
  backend "azurerm" {
    resource_group_name  = "tfstate-rg"
    storage_account_name = "acmetfstate"
    container_name       = "tfstate"
    key                  = "prod.terraform.tfstate"
    use_azuread_auth     = true
  }
}
```

```hcl
terraform {
  backend "gcs" {
    bucket = "acme-tf-state"
    prefix = "prod/network"
  }
}
```

Both lock state automatically: Azure uses blob leases and GCS uses a lock file in the bucket.

## 171: What workflows does HCP Terraform support?

- **VCS-driven:** the workspace is connected to a Git repo. Pull requests trigger speculative plans, merges trigger runs that can apply.
- **CLI-driven:** you run `terraform plan` and `apply` locally with a `cloud` block, but the run executes remotely in HCP Terraform and logs stream back to you.
- **API-driven:** your own tooling uploads configuration and starts runs through the API.

Each workspace can also choose local execution, where HCP Terraform only stores state.

## 172: What are variable sets in HCP Terraform?

A variable set is a group of variables (Terraform variables or environment variables) that you can apply to many workspaces or a whole project at once. Typical uses are cloud credentials and common tags. It saves you from copying the same values into each workspace and lets you rotate them in one place. Variables set directly in a workspace override those from a variable set.

## 173: What are run triggers in HCP Terraform?

Run triggers connect workspaces. When a source workspace (like `network`) finishes an apply, HCP Terraform automatically queues a run in the dependent workspace (like `app`). This keeps downstream workspaces up to date when shared infrastructure changes. Terraform Stacks are a newer way to handle such dependencies.

## 174: What is the removed block?

The `removed` block (Terraform 1.7) tells Terraform that a resource is no longer in the code, and lets you choose whether to destroy it or just forget it.

```hcl
removed {
  from = aws_s3_bucket.old_logs

  lifecycle {
    destroy = false
  }
}
```

With `destroy = false`, the plan says the resource will be removed from state but the real bucket stays. With `destroy = true` (the default), it is destroyed, which is the same as just deleting the resource block. It replaces `terraform state rm` with a reviewed, planned change.

## 175: How do you import many resources at once?

`import` blocks support `for_each` since Terraform 1.7.

```hcl
locals {
  buckets = {
    logs   = "acme-logs"
    assets = "acme-assets"
  }
}

import {
  for_each = local.buckets
  to       = aws_s3_bucket.this[each.key]
  id       = each.value
}

resource "aws_s3_bucket" "this" {
  for_each = local.buckets
  bucket   = each.value
}
```

The `id` can also be any expression, not just a fixed string, so you can build IDs from variables.

## 176: Why does a plan sometimes show changes right after an import?

The import fills state with the real attributes, but your code may not match them. For example, the real bucket has tags or versioning that your code doesn't mention, or your code sets a value that differs from reality.

Go through the plan and change the code until the plan shows no changes, unless you actually want to change those settings. Using `-generate-config-out` helps you start with code that is close to reality.

## 177: What is a check block?

A `check` block (Terraform 1.5) defines assertions that run at the end of every plan and apply. A failed check only shows a warning, it does not stop the run.

```hcl
check "website_up" {
  data "http" "home" {
    url = "https://${aws_lb.web.dns_name}/health"
  }

  assert {
    condition     = data.http.home.status_code == 200
    error_message = "Health check returned ${data.http.home.status_code}."
  }
}
```

The data source inside a check block is scoped to it. HCP Terraform can also run checks on a schedule as part of health assessments.

## 178: What are preconditions and postconditions?

They are custom checks inside `lifecycle` blocks (and outputs). A failing condition stops the run with your error.

```hcl
data "aws_ami" "app" {
  most_recent = true
  owners      = ["self"]
  filter {
    name   = "name"
    values = ["app-*"]
  }
}

resource "aws_instance" "app" {
  ami           = data.aws_ami.app.id
  instance_type = var.instance_type

  lifecycle {
    precondition {
      condition     = data.aws_ami.app.architecture == "x86_64"
      error_message = "The AMI must be x86_64."
    }

    postcondition {
      condition     = self.public_dns != ""
      error_message = "The instance must get a public DNS name."
    }
  }
}
```

A precondition runs before the resource is planned or applied. A postcondition runs after and can use `self`.

## 179: What is the difference between validation, preconditions, postconditions and check blocks?

- **Variable validation:** checks input values. Fails the run.
- **Precondition:** checks assumptions before a resource, data source or output is evaluated. Fails the run.
- **Postcondition:** checks the result after a resource or data source is created or read. Fails the run and blocks dependent resources.
- **Check block:** checks the overall state of the infrastructure. Only warns, never blocks.

Use validation for "is this input OK", conditions for "is this resource OK to use", and checks for "is the system working".

## 180: What does replace_triggered_by do?

`replace_triggered_by` replaces a resource when another resource or attribute changes, even if nothing in the resource itself changed.

```hcl
resource "terraform_data" "deploy_marker" {
  input = var.app_version
}

resource "aws_instance" "worker" {
  ami           = var.ami_id
  instance_type = "t3.micro"

  lifecycle {
    replace_triggered_by = [terraform_data.deploy_marker]
  }
}
```

It only accepts references to managed resources (or their attributes). To trigger on a plain variable, wrap it in `terraform_data` as above.

## 181: What is terraform test?

`terraform test` (Terraform 1.6 and later) is the built-in testing framework. Tests are written in HCL in files ending with `.tftest.hcl`, usually in a `tests/` folder.

```hcl
# tests/bucket.tftest.hcl
variables {
  bucket_name = "test-bucket-123"
}

run "creates_bucket_with_right_name" {
  command = plan

  assert {
    condition     = aws_s3_bucket.this.bucket == "test-bucket-123"
    error_message = "Bucket name is wrong."
  }
}
```

```bash
terraform test
```

Each `run` block executes a plan or apply and checks `assert` conditions.

## 182: What is the difference between command = plan and command = apply in a test?

- `command = plan` only plans. It is fast, creates nothing and works well for checking logic, names and conditionals. Values that are only known after apply cannot be asserted.
- `command = apply` (the default) creates real resources, runs assertions, and then destroys everything at the end of the test file.

Apply tests are integration tests. They are slower and cost money, but they prove the resources really work.

## 183: How do you mock providers in terraform test?

Since Terraform 1.7, you can use `mock_provider` so tests don't call real APIs or need credentials.

```hcl
mock_provider "aws" {
  mock_resource "aws_s3_bucket" {
    defaults = {
      arn = "arn:aws:s3:::mock-bucket"
    }
  }
}

run "bucket_arn_output" {
  command = apply

  assert {
    condition     = output.bucket_arn == "arn:aws:s3:::mock-bucket"
    error_message = "Unexpected ARN."
  }
}
```

Computed values that are not given a default get fake generated values. You can also use `override_resource`, `override_data` and `override_module` to replace single objects.

## 184: How do you test that a validation fails?

Use `expect_failures` in a `run` block. The test passes only if the listed object fails its check.

```hcl
run "rejects_bad_environment" {
  command = plan

  variables {
    environment = "qa"
  }

  expect_failures = [
    var.environment,
  ]
}
```

It works for variable validations, preconditions, postconditions and check blocks.

## 185: How do you run Terraform in GitHub Actions?

```yaml
name: terraform
on:
  pull_request:
  push:
    branches: [main]

permissions:
  contents: read
  id-token: write
  pull-requests: write

jobs:
  plan:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: hashicorp/setup-terraform@v3
        with:
          terraform_version: 1.14.0
      - uses: aws-actions/configure-aws-credentials@v4
        with:
          role-to-assume: arn:aws:iam::123456789012:role/github-terraform
          aws-region: eu-central-1
      - run: terraform init -input=false
      - run: terraform fmt -check -recursive
      - run: terraform validate
      - run: terraform plan -input=false -out=tfplan
```

On `main`, a separate job (often protected by a GitHub environment with required reviewers) runs `terraform apply`.

## 186: How does OIDC authentication from CI to a cloud provider work?

The CI system (GitHub Actions, GitLab CI and so on) issues a short-lived signed token (JWT) for each job. The cloud provider is set up to trust that issuer and to exchange the token for temporary credentials if claims like the repo and branch match.

In AWS, you create an IAM OIDC identity provider for `token.actions.githubusercontent.com` and a role whose trust policy checks the `sub` claim, for example `repo:acme/infra:ref:refs/heads/main`. No access keys are stored anywhere. Azure (federated credentials) and Google Cloud (workload identity federation) work the same way.

## 187: Is it safe to pass a saved plan file between CI jobs?

You can, and it is a good practice because the apply runs exactly what was reviewed. But keep in mind:

- The plan file contains the full configuration and variable values, including sensitive ones, in a form that is easy to read. Treat it as a secret and keep artifact retention short.
- The apply must use the same Terraform version, providers and working directory setup.
- If the state changed after the plan was made, the apply fails with a "saved plan is stale" error, which is a safety feature.

## 188: What is Atlantis?

Atlantis is an open source tool that runs Terraform from pull requests. It listens to webhooks from GitHub, GitLab or Bitbucket. When you open a pull request, it runs `plan` and posts the output as a comment. A reviewer comments `atlantis apply` to apply it.

It also locks the project while a pull request is open, so two pull requests can't change the same state at the same time. It is a self-hosted alternative to HCP Terraform's VCS workflow.

## 189: What is Infracost?

Infracost reads a Terraform plan (or code) and estimates how much the infrastructure costs per month, and how much a change adds or removes. It is usually run in CI and posts a cost comment on pull requests, so reviewers see that going from `t3.small` to `m6i.4xlarge` adds hundreds of dollars a month before it is merged.

## 190: Which tools scan Terraform code for security issues?

- **Checkov:** many built-in policies for AWS, Azure, GCP and Kubernetes
- **Trivy:** the general security scanner that absorbed tfsec
- **KICS:** open source scanner from Checkmarx
- **Terrascan:** policy scanner based on OPA (archived, still seen in older pipelines)

They catch things like public S3 buckets, unencrypted disks, security groups open to `0.0.0.0/0` and missing logging. Run them in CI on every pull request.

## 191: How do you handle secrets in Terraform?

- Don't put secrets in `.tf` files or committed tfvars
- Read them at runtime from a secrets manager (AWS Secrets Manager, Azure Key Vault, HashiCorp Vault) with ephemeral resources where possible, or data sources
- Use write-only arguments (like `password_wo`) so secrets don't land in state
- Let the cloud service manage the secret when it can, like RDS `manage_master_user_password = true`
- Pass remaining secrets with `TF_VAR_` environment variables from your CI secret store
- Mark variables and outputs `sensitive = true`
- Encrypt state and restrict access to it

## 192: What do the sensitive and nonsensitive functions do?

`sensitive(value)` marks a value as sensitive, so Terraform hides it in output. It is useful when a value is secret but doesn't come from a sensitive variable, for example a file you read.

`nonsensitive(value)` removes the sensitive mark. Use it only when you are sure the result is not secret, for example the length of a password or a hash.

```hcl
locals {
  api_key = sensitive(file("${path.module}/api_key.txt"))
}

output "password_length" {
  value = nonsensitive(length(var.db_password))
}
```

## 193: What are ephemeral resources?

Ephemeral resources (Terraform 1.10) are temporary values that Terraform reads during a run but never saves in the plan or state. They are meant for secrets and short-lived credentials.

```hcl
ephemeral "aws_secretsmanager_secret_version" "db" {
  secret_id = "prod/db/password"
}

provider "postgresql" {
  host     = aws_db_instance.main.address
  username = "admin"
  password = ephemeral.aws_secretsmanager_secret_version.db.secret_string
}
```

They are referenced with the `ephemeral.` prefix. You can only use them in places that also don't persist values: provider blocks, provisioners, other ephemeral values, and write-only arguments.

## 194: What are write-only arguments?

Write-only arguments (Terraform 1.11) are resource arguments that Terraform sends to the provider but never stores in plan or state. They usually end with `_wo` and come with a version argument, because Terraform can't detect changes to a value it doesn't store.

```hcl
ephemeral "random_password" "db" {
  length = 24
}

resource "aws_db_instance" "main" {
  identifier          = "app-db"
  engine              = "postgres"
  instance_class      = "db.t4g.micro"
  allocated_storage   = 20
  username            = "app"
  password_wo         = ephemeral.random_password.db.result
  password_wo_version = 1
  skip_final_snapshot = true
}
```

To rotate the password, change it at the source and increase `password_wo_version`.

## 195: What are ephemeral variables and outputs?

A variable with `ephemeral = true` can receive a value (like a token) that is used during the run but not saved in the plan file or state.

```hcl
variable "vault_token" {
  type      = string
  ephemeral = true
}
```

Ephemeral variables can only be used in ephemeral contexts. A child module can also have `ephemeral = true` outputs to pass such values up to its parent. The root module cannot have ephemeral outputs. When you apply a saved plan, you must pass ephemeral variables again because they were not saved.

## 196: How do you use HashiCorp Vault with Terraform?

The `hashicorp/vault` provider can both manage Vault (policies, auth methods, secret engines) and read secrets from it.

```hcl
provider "vault" {
  address = "https://vault.example.com"
}

ephemeral "vault_kv_secret_v2" "db" {
  mount = "secret"
  name  = "prod/db"
}
```

Vault can also hand out dynamic cloud credentials (for example the AWS secrets engine), so Terraform gets short-lived keys for each run. When reading secrets, prefer ephemeral resources over data sources so the values don't end up in state.

## 197: How can you let AWS manage an RDS master password instead of Terraform?

Set `manage_master_user_password = true`. RDS creates the password, stores it in AWS Secrets Manager and can rotate it. Terraform never sees the value.

```hcl
resource "aws_db_instance" "main" {
  identifier                  = "app-db"
  engine                      = "postgres"
  instance_class              = "db.t4g.small"
  allocated_storage           = 20
  username                    = "app"
  manage_master_user_password = true
}

output "db_secret_arn" {
  value = aws_db_instance.main.master_user_secret[0].secret_arn
}
```

Apps then read the password from Secrets Manager using the secret ARN.

## 198: How do you use a map of objects with for_each?

This is one of the most common patterns for flexible modules.

```hcl
variable "queues" {
  type = map(object({
    visibility_timeout = optional(number, 30)
    fifo               = optional(bool, false)
  }))
}

resource "aws_sqs_queue" "this" {
  for_each = var.queues

  name                       = each.value.fifo ? "${each.key}.fifo" : each.key
  fifo_queue                 = each.value.fifo
  visibility_timeout_seconds = each.value.visibility_timeout
}
```

```hcl
queues = {
  orders = { fifo = true }
  emails = {}
}
```

The map keys become stable instance keys, and `optional()` keeps the input short.

## 199: Why should you be careful with the any type?

`type = any` accepts anything, so Terraform can't check the input and you lose good error messages. Mistakes show up later as confusing errors deep inside the module.

Also, with `list(any)` or `map(any)`, all elements still have to convert to one common type. If they can't, you get an error, and sometimes values are converted in ways you didn't expect (for example numbers to strings). Prefer explicit `object()` types with `optional()` attributes.

## 200: Why does a data source for the latest AMI cause instances to be replaced?

With `most_recent = true`, every time a new image is published, the data source returns a new ID. Since `ami` forces replacement on `aws_instance`, the next plan wants to replace your instances, often when you didn't plan to roll out.

Options:

- Pin the AMI ID in a variable and update it on purpose
- Add `ignore_changes = [ami]` and roll out new images another way
- Use a launch template and autoscaling group with instance refresh, so new images roll out in a controlled way

## 201: Why do resources with create_before_destroy often use name_prefix?

With `create_before_destroy`, the old and new resource exist at the same time for a moment. If the name must be unique (security groups, launch templates, IAM roles, S3 buckets), the new one fails with "already exists".

Many AWS resources have a `name_prefix` argument. Terraform then adds a random suffix, so the two names never clash.

```hcl
resource "aws_security_group" "web" {
  name_prefix = "web-"
  vpc_id      = var.vpc_id

  lifecycle {
    create_before_destroy = true
  }
}
```

`create_before_destroy` also spreads to the resources this one depends on, so Terraform can keep the correct order.

## 202: How do you roll out a new AMI to an autoscaling group without downtime?

Put the AMI in a launch template and let the autoscaling group replace instances with an instance refresh.

```hcl
resource "aws_launch_template" "web" {
  name_prefix   = "web-"
  image_id      = var.ami_id
  instance_type = "t3.small"
}

resource "aws_autoscaling_group" "web" {
  name                = "web"
  min_size            = 2
  max_size            = 4
  vpc_zone_identifier = var.subnet_ids
  target_group_arns   = [aws_lb_target_group.web.arn]

  launch_template {
    id      = aws_launch_template.web.id
    version = aws_launch_template.web.latest_version
  }

  instance_refresh {
    strategy = "Rolling"
    preferences {
      min_healthy_percentage = 90
    }
  }
}
```

When `ami_id` changes, Terraform creates a new launch template version, and AWS replaces instances a few at a time while the load balancer keeps serving traffic.

## 203: How do you manage several AWS accounts from one configuration?

Use one provider block per account, each assuming a role in that account.

```hcl
provider "aws" {
  alias  = "prod"
  region = "eu-central-1"

  assume_role {
    role_arn     = "arn:aws:iam::111111111111:role/terraform"
    session_name = "terraform"
  }
}

provider "aws" {
  alias  = "shared"
  region = "eu-central-1"

  assume_role {
    role_arn = "arn:aws:iam::222222222222:role/terraform"
  }
}
```

The CI runner authenticates once (for example with OIDC to a tooling account), and the provider blocks switch into each target account. For many accounts, separate root modules per account are usually easier to manage than one huge configuration.

## 204: What is the problem with creating an EKS cluster and Kubernetes resources in the same configuration?

The Kubernetes and Helm providers need the cluster endpoint and credentials. When the cluster does not exist yet, those values are unknown during the plan, and providers can't be configured with unknown values. This leads to errors or to the provider quietly connecting to the wrong cluster (like `localhost`).

The usual advice is to split it into two configurations (or stacks): one creates the cluster, the other deploys things into it. If you keep them together, use `exec` based authentication so the token is fresh:

```hcl
provider "kubernetes" {
  host                   = aws_eks_cluster.main.endpoint
  cluster_ca_certificate = base64decode(aws_eks_cluster.main.certificate_authority[0].data)

  exec {
    api_version = "client.authentication.k8s.io/v1beta1"
    command     = "aws"
    args        = ["eks", "get-token", "--cluster-name", aws_eks_cluster.main.name]
  }
}
```

## 205: Why should you avoid depends_on on modules?

`depends_on` on a module makes every resource and data source in the module depend on everything listed. Data sources inside the module then often can't be read until apply, so their results become "known after apply". This spreads unknown values through the plan, can cause extra replacements, and makes plans harder to read.

It is better to pass the real dependency in as an input variable (for example an ARN), so Terraform sees an exact reference.

## 206: What does the "Cycle" error mean and how do you fix it?

It means resources depend on each other in a loop, so Terraform cannot decide which one to create first. A classic example is two security groups whose inline rules reference each other.

Fixes:

- Break inline rules out into separate resources (like `aws_vpc_security_group_ingress_rule`) so the groups are created first and the rules after
- Remove an unneeded `depends_on`
- Move a value into a variable or local that doesn't depend on the other resource

`terraform graph` can help you find the loop.

## 207: How do you speed up slow plans?

- Split huge states into smaller ones (network, data, apps). Each plan refreshes fewer resources.
- Use a provider plugin cache in CI so providers aren't downloaded each time
- Increase `-parallelism` if you are not hitting rate limits
- Avoid many data sources that call slow APIs
- Use `-refresh=false` for a quick look while developing (not for real applies)
- Use `-target` only in emergencies

The biggest win is almost always smaller states.

## 208: What does -refresh=false do?

`terraform plan -refresh=false` skips checking real infrastructure and only compares the code with the state as it is. It is much faster for large configurations.

The downside is that the plan won't notice drift, so it may be wrong. Use it for quick checks during development, and use normal plans for anything you will apply.

## 209: What is Terragrunt?

Terragrunt is an open source wrapper around Terraform (and OpenTofu) made by Gruntwork. It helps with things Terraform doesn't do well alone:

- Keeping backend and provider config DRY across many environments
- Generating backend config per folder automatically
- Running many root modules at once with dependencies between them
- Passing outputs from one module to another

```hcl
# live/prod/app/terragrunt.hcl
include "root" {
  path = find_in_parent_folders("root.hcl")
}

terraform {
  source = "git::https://github.com/acme/modules.git//app?ref=v1.3.0"
}

dependency "vpc" {
  config_path = "../vpc"
}

inputs = {
  subnet_ids = dependency.vpc.outputs.private_subnet_ids
}
```

## 210: What are the pitfalls of CLI workspaces for environments?

- It is easy to forget which workspace is selected and apply to production by mistake
- All workspaces share the same backend, so dev and prod state live in the same bucket with the same access rules
- All workspaces use the same code version, so you can't test a change in dev while prod stays on the old code (unless you control which commit you check out)
- Differences between environments end up as `terraform.workspace == "prod" ? ...` conditions everywhere

HashiCorp's own docs say CLI workspaces are not a good fit when environments need different credentials or access control.

## 211: How do you promote changes from dev to production?

Common approaches:

- **Module versions:** environments call shared modules by version tag. You bump the version in `dev`, apply, test, then bump it in `staging` and `prod`.
- **Same commit, ordered pipeline:** one pipeline applies to dev, then staging, then prod, with manual approval between stages.
- **Branches per environment:** possible, but usually discouraged because branches drift apart.

The key idea is that prod runs code that was already applied and tested in a lower environment.

## 212: How do you read a plan as JSON?

```bash
terraform plan -out=tfplan
terraform show -json tfplan > plan.json

# list resources that will be deleted
jq -r '.resource_changes[] | select(.change.actions | index("delete")) | .address' plan.json
```

Each entry in `resource_changes` has the address, the `actions` (`create`, `update`, `delete`, `no-op`, `read`) and the `before` and `after` values. Policy tools and custom CI checks use this format.

## 213: Why can't you use sensitive values as for_each keys?

Instance keys appear in resource addresses, plan output and logs, so Terraform refuses to use sensitive values there and errors out.

If the list itself isn't secret but got marked sensitive (for example it came from a sensitive output), you can remove the mark with `nonsensitive()`. If it really is secret, use something else for the keys, like names, and keep the secret only in arguments.

```hcl
resource "aws_iam_user" "this" {
  for_each = nonsensitive(toset(var.user_names))
  name     = each.value
}
```

## 214: What causes "Invalid for_each argument" with values that are known after apply?

`for_each` and `count` must be known during the plan, because Terraform needs to know how many instances exist. If the keys depend on attributes of resources that don't exist yet (like generated IDs), you get this error.

Fixes:

- Use keys that come from your input values (names) instead of generated IDs. The values can still be unknown, only the keys must be known.
- Split the work into two applies, or use `-target` once to create the dependency first

```hcl
# bad: keys are unknown until the subnets exist
for_each = toset(aws_subnet.private[*].id)

# good: keys are known, values can be unknown
for_each = { for k, s in aws_subnet.private : k => s.id }
```

## 215: How do template directives and strip markers work?

Inside strings and template files, `%{ }` adds logic and `~` removes whitespace and newlines next to the directive.

```hcl
locals {
  config = <<-EOT
    %{~ for name, port in var.services ~}
    ${name}=${port}
    %{~ endfor ~}
    %{ if var.debug }debug=true%{ endif }
  EOT
}
```

Without the `~` markers, each directive line would leave an empty line in the result.

## 216: How do regex and regexall work?

`regex(pattern, string)` returns the first match and fails if there is none. `regexall` returns a list of all matches, so it is safe to use for checks.

```hcl
regex("^arn:aws:iam::([0-9]+):", var.role_arn)[0]   # account ID

length(regexall("^[a-z0-9-]+$", var.name)) > 0       # true if valid
```

With named groups, `regex` returns a map:

```hcl
regex("(?P<user>[^@]+)@(?P<domain>.+)", "bob@example.com")
# { domain = "example.com", user = "bob" }
```

## 217: What does the replace function do?

`replace(string, search, replacement)` replaces all matches. If `search` is wrapped in slashes, it is treated as a regular expression.

```hcl
replace("my_app_name", "_", "-")       # "my-app-name"
replace("v1.2.3", "/[^0-9]/", "")      # "123"
```

A common use is cleaning names so they fit resource naming rules.

## 218: What does zipmap do?

`zipmap(keys, values)` builds a map from a list of keys and a list of values.

```hcl
zipmap(["a", "b"], [1, 2])   # { a = 1, b = 2 }

output "instance_ips" {
  value = zipmap(aws_instance.web[*].tags.Name, aws_instance.web[*].private_ip)
}
```

## 219: What does setproduct do?

`setproduct` returns every combination of elements from two or more lists.

```hcl
setproduct(["dev", "prod"], ["eu", "us"])
# [["dev","eu"], ["dev","us"], ["prod","eu"], ["prod","us"]]
```

```hcl
resource "aws_s3_bucket" "this" {
  for_each = {
    for pair in setproduct(var.envs, var.regions) :
    "${pair[0]}-${pair[1]}" => { env = pair[0], region = pair[1] }
  }
  bucket = "acme-${each.key}"
}
```

## 220: What does the one function do?

`one(list)` returns the only element of a list with zero or one elements, or `null` if the list is empty. It fails if there is more than one.

It is handy with resources that use `count = condition ? 1 : 0`:

```hcl
output "bastion_ip" {
  value = one(aws_instance.bastion[*].public_ip)
}
```

This gives `null` when the bastion is disabled instead of an index error.

## 221: Does merge do a deep merge?

No. `merge` is shallow. If both maps have the same key, the value from the later map replaces the whole value, even if it is a nested object.

```hcl
merge(
  { db = { size = 20, multi_az = true } },
  { db = { size = 50 } }
)
# { db = { size = 50 } }   multi_az is gone
```

For a deep merge you have to merge the nested maps yourself, for example with a `for` expression that calls `merge` on each nested value.

## 222: How do you drive infrastructure from a YAML file?

Read the file with `yamldecode(file(...))` and loop over it. This lets people add things (users, DNS records, repos) by editing YAML instead of HCL.

```yaml
# users.yaml
alice:
  groups: [admins]
bob:
  groups: [developers]
```

```hcl
locals {
  users = yamldecode(file("${path.module}/users.yaml"))
}

resource "aws_iam_user" "this" {
  for_each = local.users
  name     = each.key
}
```

Add validation (with `precondition` or `check`) because YAML has no type checks.

## 223: How do you upload a folder of files to S3 with Terraform?

Use `fileset` to list files and `for_each` to create one object per file.

```hcl
locals {
  mime_types = {
    ".html" = "text/html"
    ".css"  = "text/css"
    ".js"   = "application/javascript"
    ".svg"  = "image/svg+xml"
  }
}

resource "aws_s3_object" "site" {
  for_each = fileset("${path.module}/dist", "**")

  bucket       = aws_s3_bucket.site.id
  key          = each.value
  source       = "${path.module}/dist/${each.value}"
  etag         = filemd5("${path.module}/dist/${each.value}")
  content_type = lookup(local.mime_types, try(regex("\\.[^.]+$", each.value), ""), "application/octet-stream")
}
```

`etag` makes Terraform upload a file again when its content changes. For large or often-changing sites, a CLI sync in the deploy pipeline is usually better than Terraform.

## 224: What is the external data source?

The `external` data source (from `hashicorp/external`) runs a program that reads JSON on stdin and prints a JSON object of strings on stdout. Terraform uses the result as data.

```hcl
data "external" "git" {
  program = ["bash", "-c", "echo '{\"sha\": \"'$(git rev-parse --short HEAD)'\"}'"]
}

output "commit" {
  value = data.external.git.result.sha
}
```

It is an escape hatch. It runs on every plan, depends on tools installed on the machine, and makes the configuration less portable.

## 225: What is the http data source?

The `http` data source (from `hashicorp/http`) makes an HTTP GET request and returns the response body, headers and status code.

```hcl
data "http" "my_ip" {
  url = "https://checkip.amazonaws.com"
}

locals {
  my_ip = "${chomp(data.http.my_ip.response_body)}/32"
}
```

It is often used inside `check` blocks for health checks, or to fetch small pieces of public data.

## 226: Why should you be careful with local_file?

`local_file` writes a file on the machine running Terraform. The file content is stored in state, and if you run Terraform on another machine (or CI), the file won't exist there, so Terraform recreates it every time.

It is fine for generating config files that are used right away in the same run, but not as a way to deliver outputs. Use outputs, or write to a real store like S3 or a secrets manager.

## 227: What is the risk of tls_private_key?

`tls_private_key` generates a private key, and the key is saved in state in plain text. Anyone with state access has the key.

It is acceptable for test setups or short-lived certificates. For real secrets, generate keys outside Terraform, use a service that keeps the key inside (like AWS KMS or ACM), or use the ephemeral version of `tls_private_key` so the key never lands in state.

## 228: What is time_sleep and when is it used?

`time_sleep` from the `hashicorp/time` provider waits for a set time during create or destroy.

```hcl
resource "aws_iam_role_policy_attachment" "lambda" {
  role       = aws_iam_role.lambda.name
  policy_arn = "arn:aws:iam::aws:policy/service-role/AWSLambdaBasicExecutionRole"
}

resource "time_sleep" "wait_for_iam" {
  depends_on      = [aws_iam_role_policy_attachment.lambda]
  create_duration = "15s"
}
```

Other resources can then depend on `time_sleep.wait_for_iam`. It works around eventual consistency, but it is a workaround. A fixed wait may be too short on a slow day, so use it only when the provider doesn't handle retries itself.

## 229: What is eventual consistency and how does it affect Terraform?

Many cloud APIs are eventually consistent: after you create something, it can take a few seconds before other services see it. Terraform may create an IAM role and immediately try to use it, and the second call fails with "role not found" or "cannot be assumed".

Most providers already retry these errors for a while. When they don't, the options are `time_sleep`, splitting the change into two applies, or just running `apply` again. Report repeated cases to the provider, since they are often fixed with better retry logic.

## 230: How do you upgrade a provider to a new major version?

1. Read the provider's upgrade guide for breaking changes (removed resources, renamed arguments, new defaults)
2. Upgrade to the newest minor of the current major first and fix all deprecation warnings
3. Change the version constraint (for example `~> 5.0` to `~> 6.0`) and run `terraform init -upgrade`
4. Run `terraform plan` in a lower environment and check every change
5. Fix code until the plan is clean or only shows changes you expect
6. Roll out environment by environment

Never mix a major provider upgrade with other infrastructure changes in the same pull request.

## 231: How do you upgrade the Terraform CLI version?

- Read the changelog and upgrade notes for each version you skip
- Update `required_version` and the version in CI and `.terraform-version`
- Run `terraform init` and `plan` with the new version. The plan should show no changes.
- Apply in a lower environment first. Once a newer version writes the state, older CLIs may refuse to read it.
- Update all environments, so nobody keeps using an old version

Terraform 1.x has a compatibility promise, so upgrades within 1.x are usually smooth.

## 232: How do you refactor a big root module into child modules without recreating resources?

Move the resource blocks into the module and add `moved` blocks in the root module that map old addresses to new ones.

```hcl
module "network" {
  source = "./modules/network"
}

moved {
  from = aws_vpc.main
  to   = module.network.aws_vpc.this
}

moved {
  from = aws_subnet.private
  to   = module.network.aws_subnet.private
}
```

Run `terraform plan`. It should only show moves, no creates or destroys. Keep the `moved` blocks for a while (or for good in shared modules) so other copies of the config can catch up.

## 233: How do you move resources from one state to another?

There is no direct "move between states" command in the modern workflow. The safe way uses blocks:

1. In the old configuration, delete the resource block and add a `removed` block with `destroy = false`. Apply. The resource is now forgotten but still exists.
2. In the new configuration, add the resource block and an `import` block with the real ID. Apply.

Both steps go through plans and review. The older way was `terraform state mv -state-out=...` with local state files, which is error-prone with remote backends.

## 234: What does terraform state replace-provider do?

It changes the provider source address recorded for resources in state. You need it when a provider moves to a new namespace, or when you switch to a fork or a private mirror.

```bash
terraform state replace-provider registry.terraform.io/-/aws registry.terraform.io/hashicorp/aws
```

You'll see it most often when upgrading very old state from Terraform 0.12 or when switching between Terraform and OpenTofu registries.

## 235: What is a perpetual diff and how do you fix it?

A perpetual diff is a change that shows up in every plan even right after an apply. Common causes:

- The API normalizes a value (JSON policy key order, lowercase names, default values filled in)
- A value changes every run, like `timestamp()` or `uuid()`
- Two resources manage the same thing, like inline security group rules plus separate rule resources
- Something outside Terraform keeps changing the attribute

Fixes are writing the value the way the API returns it, using `jsonencode` or `aws_iam_policy_document`, removing the overlap, or using `ignore_changes` as a last step. If it's a provider bug, report it.

## 236: How do you migrate null_resource to terraform_data?

Since Terraform 1.9, you can use a `moved` block from `null_resource` to `terraform_data`, and Terraform converts the state without running provisioners again.

```hcl
resource "terraform_data" "bootstrap" {
  triggers_replace = {
    script_hash = filemd5("${path.module}/bootstrap.sh")
  }

  provisioner "local-exec" {
    command = "${path.module}/bootstrap.sh"
  }
}

moved {
  from = null_resource.bootstrap
  to   = terraform_data.bootstrap
}
```

After that you can drop the `hashicorp/null` provider if nothing else uses it.

## 237: Can a module output a whole resource object?

Yes. You can output the whole resource instead of picking attributes one by one.

```hcl
output "bucket" {
  value = aws_s3_bucket.this
}
```

The caller can then use `module.storage.bucket.arn`, `module.storage.bucket.id` and so on. It is convenient, but it makes the module's interface less clear and ties callers to the internal resource type. For public modules, explicit outputs are usually better.

## 238: What should a reusable module repository contain?

```text
terraform-aws-vpc/
├── main.tf
├── variables.tf
├── outputs.tf
├── versions.tf
├── README.md
├── CHANGELOG.md
├── examples/
│   ├── simple/
│   └── complete/
├── modules/          # optional submodules
└── tests/
    └── basic.tftest.hcl
```

The `examples/` folders show how to call the module and are often used as test fixtures. `tests/` holds `terraform test` files. The README is usually generated with `terraform-docs`.

## 239: How do you publish a module to the public Terraform Registry?

- Host it in a public GitHub repo named `terraform-<PROVIDER>-<NAME>`, like `terraform-aws-vpc`
- Use the standard module structure, with a README and a description
- Create releases with semantic version tags like `v1.0.0`
- Sign in to the registry with GitHub and publish the repo

New tags are picked up automatically and show up as new versions.

## 240: What is a private module registry?

A private registry is a place to share internal modules with versioning and documentation, without making them public. HCP Terraform and Terraform Enterprise include one, and some other tools (like GitLab and JFrog Artifactory) offer Terraform registry support too.

```hcl
module "vpc" {
  source  = "app.terraform.io/acme/vpc/aws"
  version = "~> 2.1"
}
```

The advantage over Git sources is proper `version` constraints and a searchable catalog with docs.

## 241: How do you keep providers and modules up to date?

- Use `~>` constraints so minor updates are allowed but majors are not
- Run `terraform init -upgrade` on purpose (not in every CI run) to update the lock file
- Use Renovate or Dependabot. Both understand Terraform and open pull requests that bump provider and module versions and the lock file
- Let CI run a plan on those pull requests so you see the impact

Small, regular upgrades are much easier than jumping several majors at once.

## 242: What is the difference between Sentinel and OPA for Terraform policies?

Both check a Terraform plan against rules before apply, like "no public S3 buckets" or "only these instance types".

- **Sentinel** is HashiCorp's own policy language, built into HCP Terraform and Terraform Enterprise (paid tiers). It has good access to plan, config and state data.
- **OPA** (Open Policy Agent) uses the Rego language. It is open source and works with HCP Terraform policy sets, Conftest, Atlantis or your own CI scripts on the plan JSON.

Both support enforcement levels: advisory (warn), soft mandatory (can be overridden) and hard mandatory.

## 243: How do you check a plan with OPA and Conftest?

Export the plan as JSON and run Conftest with Rego policies.

```rego
# policy/s3.rego
package main

deny contains msg if {
  rc := input.resource_changes[_]
  rc.type == "aws_s3_bucket_public_access_block"
  rc.change.after.block_public_acls == false
  msg := sprintf("%s must block public ACLs", [rc.address])
}
```

```bash
terraform plan -out=tfplan
terraform show -json tfplan > plan.json
conftest test plan.json
```

If any `deny` rule matches, Conftest exits with an error and fails the CI job.

## 244: How do you detect drift regularly?

- Run `terraform plan -detailed-exitcode` on a schedule in CI (nightly, for example) and alert when the exit code is `2`
- Use HCP Terraform health assessments, which run drift detection and check blocks automatically
- Use cloud-side tools like AWS Config for changes to important resources

When drift is found, decide whether to change it back (apply) or accept it (update the code, or apply with `-refresh-only`).

## 245: How do you control who can apply changes to production?

- Only CI (or HCP Terraform) has write credentials for production. People get read-only access.
- Protect the main branch and require reviews on pull requests
- Use a protected CI environment that requires manual approval before the apply job runs
- Give the plan role read-only permissions and the apply role write permissions
- In HCP Terraform, use team permissions per workspace and require confirmation of applies
- Add policy checks (Sentinel or OPA) as a gate

## 246: What do you do when you get "Error acquiring the state lock"?

First find out who holds the lock. The error shows the lock ID, who created it, when, and the operation.

- If another run is really in progress, wait for it or use `-lock-timeout=10m`
- If the run crashed or a CI job was killed, and you're sure nothing is running, release it with `terraform force-unlock <LOCK_ID>`

Never disable locking with `-lock=false` just to get past the error, because that is how state gets corrupted.

## 247: What does "Provider produced inconsistent result after apply" mean?

It means the provider told Terraform it would set an attribute to one value, but after the apply the real value was different. Terraform treats this as a provider bug.

The resource usually was created anyway, so check the real infrastructure and run `plan` again. Often upgrading the provider fixes it, because these bugs get reported and fixed. If not, report it with the debug log.

## 248: What do you do when apply fails with "resource already exists"?

It means the object exists in the cloud but not in your state. Maybe it was created by hand, by another configuration, or a previous apply created it but failed before saving state.

Don't delete it blindly. Add an `import` block for it, check that no other configuration manages it, and run plan and apply. If it was left behind by a failed run and is not needed, you can delete it manually and apply again.

## 249: How do you handle API rate limiting?

- Lower `-parallelism` so fewer calls run at once
- Use provider settings for retries, like `max_retries` in the AWS provider
- Split large configurations so fewer resources are refreshed per run
- Avoid many data sources that call the same API
- Run plans with `-refresh=false` during development

Rate limits often show up in big accounts where many pipelines share the same API quota.

## 250: What is kubernetes_manifest?

`kubernetes_manifest` in the Kubernetes provider lets you manage any Kubernetes object, including custom resources (CRDs), by writing the manifest as an HCL object.

```hcl
resource "kubernetes_manifest" "cert" {
  manifest = {
    apiVersion = "cert-manager.io/v1"
    kind       = "Certificate"
    metadata = {
      name      = "web"
      namespace = "default"
    }
    spec = {
      secretName = "web-tls"
      dnsNames   = ["example.com"]
      issuerRef  = { name = "letsencrypt", kind = "ClusterIssuer" }
    }
  }
}
```

It needs access to the cluster during the plan and the CRD must already exist, so you can't install a CRD and use it in the same plan. Use `yamldecode(file(...))` to reuse existing YAML.

## 251: How can you test Terraform code against AWS without a real account?

LocalStack runs a local imitation of many AWS services in Docker. You point the AWS provider at it:

```hcl
provider "aws" {
  region                      = "us-east-1"
  access_key                  = "test"
  secret_key                  = "test"
  skip_credentials_validation = true
  skip_requesting_account_id  = true

  endpoints {
    s3       = "http://localhost:4566"
    dynamodb = "http://localhost:4566"
    sqs      = "http://localhost:4566"
  }
}
```

There is also a `tflocal` wrapper that sets this up for you. It is fast and free for basic checks, but it doesn't behave exactly like AWS, so it doesn't replace tests in a real sandbox account. Mock providers in `terraform test` are another option for pure logic checks.

## 252: What is Terratest?

Terratest is a Go library from Gruntwork for testing infrastructure. A test runs `terraform init` and `apply` on an example, makes real checks (HTTP requests, SSH, AWS API calls), then runs `destroy`.

```go
func TestWebServer(t *testing.T) {
    opts := &terraform.Options{TerraformDir: "../examples/web"}
    defer terraform.Destroy(t, opts)
    terraform.InitAndApply(t, opts)

    url := terraform.Output(t, opts, "url")
    http_helper.HttpGetWithRetry(t, url, nil, 200, "OK", 30, 5*time.Second)
}
```

Today many teams use the built-in `terraform test` for most cases and keep Terratest for complex end-to-end checks.

## 253: Can Terraform manage things other than cloud infrastructure?

Yes. Anything with an API and a provider can be managed. Common examples:

- GitHub repos, teams, branch protection (`integrations/github`)
- DNS and CDN settings (Cloudflare)
- Monitoring dashboards and alerts (Datadog, Grafana, PagerDuty)
- Identity (Okta, Auth0, Entra ID)
- Databases and users (PostgreSQL, MySQL providers)

```hcl
resource "github_repository" "api" {
  name       = "api"
  visibility = "private"
}

resource "github_branch_protection" "main" {
  repository_id = github_repository.api.node_id
  pattern       = "main"

  required_pull_request_reviews {
    required_approving_review_count = 1
  }
}
```

## 254: Should Terraform code live in a monorepo or in many repos?

**Monorepo:** all modules and environments in one repo. Easy to find things and change many places in one pull request. Needs CI that only plans the folders that changed.

**Many repos:** each module in its own repo with version tags, and live environments in one or more other repos. Clear ownership and versioning, but changes across repos take more steps.

A common middle ground is one repo for shared modules (tagged per module) and one repo for live environments.

## 255: How do you pass Terraform outputs to Ansible?

Common options:

- Output the IPs and generate an inventory file from `terraform output -json` in the pipeline
- Use a dynamic inventory plugin that reads the cloud API by tags (like `amazon.aws.aws_ec2`), so Ansible doesn't need Terraform at all
- Write the inventory with a `local_file` resource and `templatefile`

```bash
terraform output -json web_ips | jq -r '.[]' > inventory.ini
ansible-playbook -i inventory.ini site.yml
```

Dynamic inventory by tags is usually the cleanest because the two tools stay independent.

## 256: How do you do a blue/green deployment with Terraform?

Create two copies of the app stack (blue and green), for example with `for_each` on a module, and switch traffic with a variable that controls the load balancer or DNS weights.

```hcl
variable "active" {
  type    = string
  default = "blue"
}

module "app" {
  source   = "./modules/app"
  for_each = toset(["blue", "green"])
  name     = each.key
  ami_id   = var.amis[each.key]
}

resource "aws_lb_listener" "web" {
  load_balancer_arn = aws_lb.web.arn
  port              = 443
  protocol          = "HTTPS"
  certificate_arn   = var.cert_arn

  default_action {
    type             = "forward"
    target_group_arn = module.app[var.active].target_group_arn
  }
}
```

You deploy the new version to the idle color, test it, then flip `active`. Rolling back is flipping it back.

## 257: How do you use providers in a network without internet access?

Download providers to a local folder or an internal mirror, and tell Terraform to install from there with a `provider_installation` block in the CLI config (`~/.terraformrc`).

```bash
terraform providers mirror /opt/terraform/providers
```

```hcl
provider_installation {
  filesystem_mirror {
    path    = "/opt/terraform/providers"
    include = ["registry.terraform.io/*/*"]
  }
  direct {
    exclude = ["registry.terraform.io/*/*"]
  }
}
```

You can also use `network_mirror` to point at an internal HTTPS server or a tool like Artifactory.

## 258: How do you output values from a resource created with for_each?

A `for_each` resource is a map of objects, so use a `for` expression to build the output.

```hcl
output "bucket_arns" {
  value = { for k, b in aws_s3_bucket.this : k => b.arn }
}

output "bucket_names" {
  value = [for b in aws_s3_bucket.this : b.bucket]
}
```

A map output keeps the keys, which makes it easy for callers to pick one item.

## 259: How do you ignore changes to just one tag?

`ignore_changes` accepts map keys.

```hcl
resource "aws_instance" "web" {
  ami           = var.ami_id
  instance_type = "t3.micro"

  tags = {
    Name = "web"
  }

  lifecycle {
    ignore_changes = [tags["LastPatched"]]
  }
}
```

Terraform will still manage the other tags. In the AWS provider you can also use `ignore_tags` in the provider block to ignore certain tag keys or prefixes across all resources.

## 260: What happens if a CI job is cancelled during apply?

Terraform gets a signal and tries to stop cleanly: it lets running operations finish, writes state and releases the lock. If the job is killed hard, it can't do that. You may end up with:

- A stale lock that needs `force-unlock`
- Resources that were created but are missing from state, so the next apply fails with "already exists"
- An `errored.tfstate` file in the working directory if writing state to the backend failed

Configure CI to send a soft stop and give Terraform time to finish, and never run two applies on the same state.

## 261: What do you look for when reviewing a plan?

- Any destroy (`-`) or replace (`-/+`), especially on databases, disks, buckets and DNS
- `# forces replacement` notes and why they appear
- The number of changes. Does it match what the pull request is supposed to do?
- Changes to IAM, security groups and public access
- Unexpected updates that hint at drift or a provider upgrade side effect
- `(known after apply)` values on things that should be stable
- Moves and imports that should not create or destroy anything

If the plan surprises you, stop and find out why before applying.

## 262: Can outputs have preconditions?

Yes. A `precondition` on an output checks a value before it is exposed, which is useful in modules to give clear errors to callers.

```hcl
output "api_url" {
  value = "https://${aws_lb.api.dns_name}"

  precondition {
    condition     = aws_lb.api.internal == false
    error_message = "The API load balancer must be internet facing."
  }
}
```

## 263: Does the sensitive flag carry through modules?

Yes. If a child module output uses a sensitive value, it must be marked `sensitive = true`, and the parent gets a sensitive value. Anything the parent builds from it is also sensitive. Terraform tracks this mark through expressions automatically.

This is why you sometimes see `(sensitive value)` in places you didn't expect. If a derived value is not actually secret, use `nonsensitive()` on it.

## 264: What is the cloudinit_config data source?

`cloudinit_config` from the `hashicorp/cloudinit` provider builds a multi-part cloud-init document from several pieces (shell scripts, cloud-config YAML) and can gzip and base64 encode it.

```hcl
data "cloudinit_config" "web" {
  gzip          = true
  base64_encode = true

  part {
    content_type = "text/cloud-config"
    content      = yamlencode({ packages = ["nginx"] })
  }

  part {
    content_type = "text/x-shellscript"
    content      = templatefile("${path.module}/start.sh.tftpl", { port = 8080 })
  }
}

resource "aws_launch_template" "web" {
  name_prefix = "web-"
  image_id    = var.ami_id
  user_data   = data.cloudinit_config.web.rendered
}
```

## 265: How do you add a nested block only when a condition is true?

Use a `dynamic` block with a list of zero or one element.

```hcl
resource "aws_s3_bucket_lifecycle_configuration" "this" {
  bucket = aws_s3_bucket.this.id

  rule {
    id     = "cleanup"
    status = "Enabled"

    filter {}

    dynamic "expiration" {
      for_each = var.expire_days == null ? [] : [var.expire_days]
      content {
        days = expiration.value
      }
    }
  }
}
```

When `expire_days` is null, the block is not generated at all.

## 266: How do you make a whole module optional?

Use `count` on the module block.

```hcl
module "bastion" {
  source = "./modules/bastion"
  count  = var.enable_bastion ? 1 : 0

  subnet_id = module.network.public_subnet_ids[0]
}

output "bastion_ip" {
  value = one(module.bastion[*].public_ip)
}
```

Remember that the address becomes `module.bastion[0]`. If you add `count` to an existing module, add a `moved` block from `module.bastion` to `module.bastion[0]`.

## 267: Can you use variables in a module's source or version?

Traditionally no. `source` and `version` are read during `terraform init`, before variables are evaluated, so they must be literal strings. This is why people used Terragrunt or code generation for that.

Terraform 1.15 started to loosen this by allowing variables declared as constant to be used in module sources during init. Check the docs for your exact version before relying on it.

## 268: How should version constraints differ between reusable modules and root modules?

- **Reusable modules** should use loose lower bounds, like `version = ">= 5.0"`, so they work with many provider versions and don't conflict with other modules.
- **Root modules** should be stricter, like `~> 6.2`, and rely on the lock file to pin the exact version.

If every module pins an exact provider version, combining modules becomes impossible because the constraints can't all be met at the same time.

## 269: How do you deploy a Lambda function with Terraform?

Zip the code with the `archive_file` data source and pass its hash so Terraform updates the function when the code changes.

```hcl
data "archive_file" "lambda" {
  type        = "zip"
  source_dir  = "${path.module}/src"
  output_path = "${path.module}/build/lambda.zip"
}

resource "aws_lambda_function" "api" {
  function_name    = "api"
  role             = aws_iam_role.lambda.arn
  runtime          = "nodejs22.x"
  handler          = "index.handler"
  filename         = data.archive_file.lambda.output_path
  source_code_hash = data.archive_file.lambda.output_base64sha256
}
```

For real apps with builds and dependencies, many teams build the artifact in CI, upload it to S3 or ECR, and pass only the version or image tag to Terraform.

## 270: How do you stop Terraform from fighting with a CI pipeline that deploys new ECS task definitions?

If the app pipeline registers new task definitions and updates the service, Terraform sees the service pointing at a different revision and tries to change it back. Common fixes:

- Have Terraform create the service and initial task definition, then ignore the field the pipeline changes:

```hcl
resource "aws_ecs_service" "app" {
  name            = "app"
  cluster         = aws_ecs_cluster.main.id
  task_definition = aws_ecs_task_definition.app.arn
  desired_count   = 2

  lifecycle {
    ignore_changes = [task_definition, desired_count]
  }
}
```

- Or let Terraform own deploys completely by passing the image tag as a variable from the pipeline

Pick one owner for each field. Two tools managing the same field always cause trouble.

## 271: What should you not manage with Terraform?

- Frequent application deploys (better done by CI/CD, Argo CD, Helm releases outside Terraform and so on)
- Data inside databases, like rows or migrations
- Things that change on their own all the time, like autoscaled counts
- Short-lived resources like test environments created per pull request, unless your setup is built for that
- Configuration inside servers (use images or configuration management)

Terraform is best at long-lived infrastructure with a clear desired state.

## 272: What does ignore_tags in the AWS provider do?

`ignore_tags` makes the AWS provider ignore certain tag keys or key prefixes on all resources. It is useful when other systems add tags you don't want Terraform to remove, like tags added by AWS Backup or a cost tool.

```hcl
provider "aws" {
  region = "eu-central-1"

  ignore_tags {
    keys         = ["LastScanned"]
    key_prefixes = ["kubernetes.io/"]
  }
}
```

## 273: How do you handle names that must be unique across all AWS customers?

S3 bucket names (and a few others) are global. Options:

- Add the account ID and region: `"acme-logs-${data.aws_caller_identity.current.account_id}-${var.region}"`
- Add a random suffix with `random_id`
- Use `bucket_prefix` and let AWS add a unique suffix

Including account and region is predictable and readable, and it avoids clashes between environments in different accounts.

## 274: How do you create one resource per item of another for_each resource?

Use the first resource directly as the `for_each` of the second. The keys stay the same, and `each.value` is the whole object of the matching instance.

```hcl
resource "aws_s3_bucket" "this" {
  for_each = toset(["logs", "assets"])
  bucket   = "acme-${each.key}"
}

resource "aws_s3_bucket_versioning" "this" {
  for_each = aws_s3_bucket.this
  bucket   = each.value.id

  versioning_configuration {
    status = "Enabled"
  }
}
```

This is called chaining `for_each`. It works because the keys are known even when the IDs are not.

## 275: How are permissions organized in HCP Terraform?

HCP Terraform has organizations, projects and workspaces. You give teams access at the organization, project or workspace level with roles like read, plan, write and admin, or with custom permissions.

A common setup: one project per product or environment group, the platform team has admin on all projects, app teams can plan on production workspaces but only CI can apply. Variable sets and policy sets can also be attached at the project level.

## 276: What are agent pools in HCP Terraform?

By default HCP Terraform runs plans and applies on HashiCorp-managed machines on the internet. If your infrastructure APIs are only reachable from a private network (like an on-prem vCenter or a private Kubernetes API), you run HCP Terraform agents inside that network. The agents poll HCP Terraform for work, so no inbound firewall rule is needed. Workspaces are then set to use that agent pool.

## 277: What are dynamic provider credentials in HCP Terraform?

Dynamic provider credentials let HCP Terraform get short-lived cloud credentials for each run using OIDC, like GitHub Actions does. You set up trust in AWS, Azure, Google Cloud or Vault once, then configure the workspace with environment variables such as:

```text
TFC_AWS_PROVIDER_AUTH = true
TFC_AWS_RUN_ROLE_ARN  = arn:aws:iam::123456789012:role/hcp-terraform
```

No static keys are stored in the workspace, and you can use different roles for plan and apply.

## 278: What is a speculative plan?

A speculative plan is a plan-only run that can never be applied. HCP Terraform runs one automatically for pull requests in VCS-connected workspaces, and also when you run `terraform plan` from the CLI with a `cloud` block. It shows the effect of a change without locking the workspace for an apply or letting anyone apply unreviewed code.

## 279: What are the limits of -generate-config-out?

- It writes every attribute it can read, including defaults and computed values, so the code is noisy
- Values are hard-coded instead of referencing other resources or variables
- Some attributes may conflict with each other and need manual cleanup before the plan works
- It doesn't create modules, `for_each` or anything structured
- Not every resource supports it well, and sensitive values are not filled in

Treat the generated file as a starting point, not finished code.

## 280: How do you know what ID to use when importing a resource?

Each resource type has its own import ID format, listed in the "Import" section at the bottom of the resource's page in the provider docs. Examples:

- `aws_instance` instance ID: `i-0abc123`
- `aws_s3_bucket` bucket name
- `aws_iam_role_policy_attachment` `role-name/policy-arn`
- `aws_security_group_rule` a long string built from several parts
- `azurerm_*` resources the full Azure resource ID

Some newer resources also accept an `identity` block in `import` instead of a string ID (Terraform 1.12 and later).

## 281: What happens when a data source can't find anything?

Most single-object data sources fail with an error if nothing matches, like `data "aws_vpc"` with a filter that matches no VPC. There is no built-in "optional" lookup.

If something may or may not exist, use the plural data source (they return empty lists instead of failing) and check the length.

```hcl
data "aws_vpcs" "tagged" {
  tags = {
    Name = "legacy"
  }
}

locals {
  legacy_vpc_id = one(data.aws_vpcs.tagged.ids)
}
```

## 282: Why is depends_on on a data source usually a bad idea?

When a data source has `depends_on` pointing at a resource with pending changes, Terraform waits until apply to read it. Its attributes become "known after apply", and everything using them becomes unknown too. That can turn harmless plans into plans full of unknown values and even replacements.

Prefer a real reference in an argument (for example, filtering by a name that comes from the resource), which gives Terraform the same ordering with less impact.

## 283: How do you validate an ACM certificate with DNS in Terraform?

Create a Route 53 record for each validation option, then wait for validation.

```hcl
resource "aws_acm_certificate" "site" {
  domain_name               = "example.com"
  subject_alternative_names = ["www.example.com"]
  validation_method         = "DNS"
}

resource "aws_route53_record" "validation" {
  for_each = {
    for o in aws_acm_certificate.site.domain_validation_options :
    o.domain_name => o
  }

  zone_id = var.zone_id
  name    = each.value.resource_record_name
  type    = each.value.resource_record_type
  records = [each.value.resource_record_value]
  ttl     = 60
}

resource "aws_acm_certificate_validation" "site" {
  certificate_arn         = aws_acm_certificate.site.arn
  validation_record_fqdns = [for r in aws_route53_record.validation : r.fqdn]
}
```

The keys are domain names, which are known during the plan, so `for_each` works even on the first run.

## 284: How do you combine several IAM policy documents?

`aws_iam_policy_document` can merge other documents with `source_policy_documents` and `override_policy_documents`.

```hcl
data "aws_iam_policy_document" "base" {
  statement {
    actions   = ["logs:CreateLogStream", "logs:PutLogEvents"]
    resources = ["*"]
  }
}

data "aws_iam_policy_document" "app" {
  source_policy_documents = [data.aws_iam_policy_document.base.json]

  statement {
    actions   = ["s3:GetObject"]
    resources = ["${aws_s3_bucket.data.arn}/*"]
  }
}
```

Statements with the same `sid` in override documents replace the matching ones.

## 285: Why shouldn't you mix inline security group rules with separate rule resources?

If a security group has inline `ingress` blocks and you also create separate rule resources for the same group, each one thinks it owns all the rules. The inline config removes rules it doesn't know about, the separate resources add them back, and every plan shows changes.

Pick one style per group. The AWS provider recommends the separate `aws_vpc_security_group_ingress_rule` and `aws_vpc_security_group_egress_rule` resources, one rule per resource.

## 286: How do you bring a manually built environment under Terraform?

1. Make an inventory of what exists (console, CLI, tags, cost reports)
2. Start with the base layers: network, then data stores, then apps
3. Write code and `import` blocks for one layer at a time (use `-generate-config-out` for a first draft)
4. Iterate until `plan` shows no changes
5. Restrict manual changes once a part is managed, for example with read-only console access
6. Move on to the next layer

Don't try to import everything in one big pull request.

## 287: How does Crossplane compare to Terraform?

Crossplane is a Kubernetes add-on that manages cloud resources as Kubernetes custom resources. A controller keeps reconciling them, so drift is fixed automatically without anyone running a command.

Terraform runs as a command (or in CI) and only changes things when you apply. It has a much larger provider ecosystem and is easier to adopt without Kubernetes. Crossplane fits teams that already run everything through Kubernetes and GitOps tools like Argo CD.

## 288: How do you safely remove a big piece of infrastructure?

1. Check what depends on it (other states, DNS, apps) before you start
2. Take backups or snapshots of data (final snapshots for databases)
3. Remove `prevent_destroy` and turn off deletion protection on purpose in a separate change
4. Delete the code and run a plan. Read every destroy line.
5. Apply in lower environments first
6. Clean up leftovers like DNS records and remote state references

For things that should stay but not be managed anymore, use a `removed` block with `destroy = false` instead.

## 289: What makes a good module interface?

- A small number of inputs with clear names, types, descriptions and sensible defaults
- `object()` types with `optional()` attributes for groups of settings
- Validation with helpful error messages
- Outputs for everything callers are likely to need (IDs, ARNs, names)
- No provider blocks inside
- Secure defaults (encryption on, public access off)
- No surprise behavior: don't create extra resources the caller didn't ask for

A module should hide complexity, not just rename the arguments of one resource.

## 290: How do you pass lists and maps on the command line?

Use HCL syntax and quote it for your shell.

```bash
terraform apply -var='allowed_cidrs=["10.0.0.0/16","10.1.0.0/16"]'
terraform apply -var='tags={Team="payments",Env="dev"}'

export TF_VAR_allowed_cidrs='["10.0.0.0/16"]'
```

For anything more than a simple value, a `.tfvars` file is easier to read and less error-prone.

## 291: How do you test a module in CI?

- Run `fmt -check`, `validate` and TFLint on every pull request
- Run `terraform test` with `command = plan` and mock providers on every pull request (fast, no cloud access)
- Run `terraform test` with real applies in a sandbox account on merge or nightly
- Use the folders under `examples/` as test fixtures so the examples keep working
- Make sure tests destroy what they create, and clean the sandbox account regularly in case a test crashes

## 292: How do you test a module from a separate test configuration?

A `run` block can point to a different module with a `module` block. This lets you create helper resources first, then test the real module.

```hcl
run "setup" {
  module {
    source = "./tests/setup"
  }
}

run "main" {
  variables {
    vpc_id = run.setup.vpc_id
  }

  assert {
    condition     = length(output.subnet_ids) == 2
    error_message = "Expected two subnets."
  }
}
```

Outputs from earlier runs are available as `run.<name>.<output>`.

## 293: How do you share default settings across many items in a for_each?

Merge a defaults object with each item's settings in a `locals` block.

```hcl
locals {
  service_defaults = {
    cpu    = 256
    memory = 512
    count  = 1
  }

  services = {
    for name, cfg in var.services :
    name => merge(local.service_defaults, cfg)
  }
}
```

Each service only needs to list what is different. With object types, `optional()` with defaults in the variable type often does the same job more cleanly.

## 294: Why are S3 bucket settings split into many resources in the AWS provider?

Since AWS provider v4, things like versioning, encryption, lifecycle rules, policies and website hosting are configured with separate resources instead of nested blocks in `aws_s3_bucket`.

```hcl
resource "aws_s3_bucket" "data" {
  bucket = "acme-data"
}

resource "aws_s3_bucket_versioning" "data" {
  bucket = aws_s3_bucket.data.id
  versioning_configuration {
    status = "Enabled"
  }
}

resource "aws_s3_bucket_server_side_encryption_configuration" "data" {
  bucket = aws_s3_bucket.data.id
  rule {
    apply_server_side_encryption_by_default {
      sse_algorithm = "aws:kms"
    }
  }
}
```

This matches how the S3 API works (each setting has its own API call) and avoids huge resources with conflicting fields.

## 295: What are provider-defined functions?

Since Terraform 1.8, providers can ship their own functions. You call them with the `provider::<name>::<function>` syntax.

```hcl
locals {
  role = provider::aws::arn_parse(var.role_arn)
}

output "account_id" {
  value = local.role.account_id
}
```

The provider must be listed in `required_providers`. This fills the gap left by not being able to write your own functions in HCL.

## 296: How do you protect a database from deletion besides prevent_destroy?

Use the provider's own deletion protection setting too, because it also protects against deletion from the console, CLI and other tools.

```hcl
resource "aws_db_instance" "main" {
  # ...
  deletion_protection       = true
  skip_final_snapshot       = false
  final_snapshot_identifier = "app-db-final"

  lifecycle {
    prevent_destroy = true
  }
}
```

Add backups and point-in-time recovery, and limit IAM permissions for delete actions.

## 297: Can you use count or for_each on data sources?

Yes. Data sources support `count` and `for_each` the same way resources do.

```hcl
data "aws_ssm_parameter" "config" {
  for_each = toset(["db_host", "db_port"])
  name     = "/app/prod/${each.key}"
}

locals {
  db_host = data.aws_ssm_parameter.config["db_host"].value
}
```

## 298: What permissions does the S3 backend need?

On the bucket:

- `s3:ListBucket`

On the state file key:

- `s3:GetObject`
- `s3:PutObject`

With `use_lockfile = true`, also `s3:GetObject`, `s3:PutObject` and `s3:DeleteObject` on the `.tflock` key. If the bucket uses a customer-managed KMS key, the role needs `kms:Encrypt`, `kms:Decrypt` and `kms:GenerateDataKey` on that key. Using workspaces adds more keys under the `env:/` prefix that need the same access.

## 299: What happens if you rename a module call in the root module?

All resources inside it get new addresses (`module.old_name...` becomes `module.new_name...`). Without a `moved` block, Terraform plans to destroy everything in the old module and create it all again.

```hcl
moved {
  from = module.old_name
  to   = module.new_name
}
```

One `moved` block for the module moves every resource inside it.

## 300: How do you find which resources in state are not in your code anymore?

Terraform handles this for you: if a resource is in state but not in the code, the plan shows it as a destroy. So a `terraform plan` after removing code is the check.

To compare more broadly (for example, find cloud resources that no Terraform state manages), you need outside tools. Some options are tag policies that require a `ManagedBy` tag, AWS Config rules, or open source tools that compare cloud inventories with state files.

# Advanced Questions (301-450)

## 301: How do Terraform core and providers talk to each other?

Providers are separate programs. When Terraform needs a provider, it starts the provider binary as a child process and talks to it over gRPC on a local connection, using HashiCorp's `go-plugin` library.

Core handles the configuration, graph, state and plan. The provider handles everything specific to an API. Core calls RPCs like `GetProviderSchema`, `ValidateResourceConfig`, `PlanResourceChange`, `ApplyResourceChange`, `ReadResource` and `ImportResourceState`. This split is why providers can be released on their own schedule and written by anyone.

## 302: What are plugin protocol versions 5 and 6?

They are versions of the gRPC protocol between core and providers. Protocol 5 is used by providers built with the older SDKv2. Protocol 6 is used by the newer Plugin Framework and supports things like nested attributes (attributes that hold objects, not just nested blocks).

Terraform 1.0 and later supports both, which is why old and new providers work side by side. Newer features like ephemeral resources, write-only arguments, provider functions and resource identity need provider support through newer protocol messages.

## 303: What happens internally during terraform plan?

Roughly:

1. Load and parse all configuration files and modules
2. Load the state and start the needed providers, get their schemas
3. Build a graph of all resources, data sources, variables, locals, outputs and providers
4. Walk the graph in dependency order, in parallel where possible
5. For each resource: refresh it with `ReadResource`, evaluate its config, then ask the provider for the planned new state with `PlanResourceChange`
6. Compare prior and planned state to choose an action (no-op, create, update, replace, delete)
7. Run conditions and checks, and print the plan (or save it with `-out`)

Apply walks a similar graph and calls `ApplyResourceChange` for each change, saving state as it goes.

## 304: What does the state file look like inside?

It is a JSON document with a top-level structure like this:

```json
{
  "version": 4,
  "terraform_version": "1.14.0",
  "serial": 42,
  "lineage": "3f1c2a9e-...",
  "outputs": {},
  "resources": [
    {
      "mode": "managed",
      "type": "aws_instance",
      "name": "web",
      "provider": "provider[\"registry.terraform.io/hashicorp/aws\"]",
      "instances": [
        {
          "schema_version": 1,
          "attributes": { "id": "i-0abc", "instance_type": "t3.micro" },
          "sensitive_attributes": [],
          "dependencies": ["aws_security_group.web"]
        }
      ]
    }
  ],
  "check_results": null
}
```

`version` is the state format version, not the Terraform version. Each instance stores its attributes, the provider's schema version and its dependencies. Don't build tools that depend on this format. Use `terraform show -json` instead, which is a stable public format.

## 305: What are serial and lineage in the state file?

- **lineage** is a random ID created when a state is first made. All later versions of the same state keep the same lineage.
- **serial** is a number that goes up each time the state is written.

Terraform uses them as a safety check. It refuses to push a state with a different lineage (it's a different state, maybe from another project) or a lower serial (it's older than what's in the backend), unless you force it. Saved plans also record them, so applying a plan made against an older state fails.

## 306: How does S3 native state locking work?

With `use_lockfile = true`, Terraform creates a lock object next to the state (`<key>.tflock`) using an S3 conditional write (`If-None-Match: *`). The write only succeeds if no lock object already exists, which makes it atomic. When the run finishes, Terraform deletes the lock object.

This became possible after S3 added support for conditional writes in 2024. Before that, the S3 backend needed a DynamoDB table for locking.

## 307: How do you move from DynamoDB locking to S3 native locking?

1. Upgrade to Terraform 1.11 or later (1.10 had it as experimental)
2. Add `use_lockfile = true` while keeping `dynamodb_table`. Terraform then takes both locks, so old and new clients stay safe during the switch.
3. Run `terraform init -reconfigure` and make sure everyone and every pipeline uses a version that supports the lock file
4. Remove `dynamodb_table`, run init again, and delete the DynamoDB table later

Also grant `s3:DeleteObject` on the `.tflock` key, since Terraform deletes the lock file when done.

## 308: How do unknown values work during planning?

When an attribute can't be known until apply (like an ID), the provider marks it as unknown in the planned state. Terraform keeps the unknown marker through every expression that uses it: `"${aws_instance.web.id}-x"` is also unknown, and so is `length()` of a list containing unknowns in some cases.

Unknowns are fine in most arguments, since providers know how to plan with them. They are not allowed in `count`, `for_each` keys, provider configuration (for some providers), and anything needed to build the graph. That's where the "cannot be determined until apply" errors come from.

## 309: What are deferred actions?

Deferred actions are an experimental feature (available in alpha builds) that lets Terraform handle unknown values in `count`, `for_each` and provider configuration. Instead of failing, Terraform plans what it can, defers the parts it can't plan, and after the apply you run another plan to finish them.

```bash
terraform plan -allow-deferral
```

Terraform Stacks use the same idea to handle things like "create a Kubernetes cluster and deploy into it" in one configuration, by applying in several rounds. In regular Terraform it is not stable yet.

## 310: How does Terraform decide between an in-place update and a replace?

Core doesn't decide on its own. During `PlanResourceChange`, the provider returns the planned new state and a list of attribute paths that require replacement (`RequiresReplace`). If that list is non-empty and the values differ, core plans a replace. Core also forces replacement for `-replace`, `replace_triggered_by`, and tainted resources.

This is why the same change can be in-place in one provider version and a replacement in another: the provider's schema and plan logic decide.

## 311: What is private data in state?

Providers can store an opaque blob called private data with each resource instance in state. Core never looks inside it, it just keeps it and passes it back on the next call. Providers use it for internal bookkeeping like timeouts or schema migration details.

You'll see it as a `private` field in the raw state file, base64 encoded. Don't change it by hand.

## 312: How are provider schema changes handled for existing state?

Each resource type has a schema version. When a provider changes how it stores a resource (renames an attribute, changes a type), it bumps the schema version and provides an upgrade function. When Terraform finds state written with an older schema version, it calls `UpgradeResourceState` and the provider converts the old data to the new shape.

This is why downgrading a provider after an apply can fail: the older provider doesn't understand the newer schema version written in state.

## 313: What is the difference between the Terraform Plugin Framework and SDKv2?

Both are Go libraries for writing providers.

- **SDKv2** is the older one. It uses protocol 5 and has some legacy behavior, like not being able to tell the difference between an empty value and an unset one.
- **Plugin Framework** is the recommended one for new providers. It uses protocol 6, has a clearer type system, supports nested attributes, and is the only way to use newer features like ephemeral resources, provider functions and write-only arguments.

Big providers like AWS and Azure are moving resource by resource from SDKv2 to the Framework, using a mux server that combines both in one binary.

## 314: How would you write a custom provider?

1. Start from the `terraform-provider-scaffolding-framework` template
2. Implement the provider type: schema for its configuration and a `Configure` method that creates an API client
3. For each resource, implement `Schema`, `Create`, `Read`, `Update`, `Delete` and usually `ImportState`
4. Add data sources, functions or ephemeral resources as needed
5. Write acceptance tests that run real Terraform configs against the API
6. Build with Go, sign releases with GPG and publish to a registry

A typical reason to write one is managing an internal platform API the same way as your cloud resources.

## 315: How are providers tested?

Providers mostly use acceptance tests. Each test is a small Terraform config that the test framework applies against the real API, checks attributes, runs a plan to make sure there's no diff, tests import, and destroys everything at the end.

```bash
TF_ACC=1 go test ./internal/... -run TestAccWidget -v
```

`TF_ACC=1` is required so these slow, costly tests don't run by accident. Unit tests cover helper logic.

## 316: How do you test a locally built provider without publishing it?

Use `dev_overrides` in the CLI config file. Terraform then uses your local binary for that provider.

```hcl
# ~/.terraformrc
provider_installation {
  dev_overrides {
    "acme/widgets" = "/Users/me/go/bin"
  }
  direct {}
}
```

Terraform prints a warning that overrides are active. You don't need `terraform init` for the overridden provider, and the lock file is not updated for it.

## 317: How are modules installed and tracked?

During `terraform init`, Terraform downloads each module call into `.terraform/modules/` and writes `.terraform/modules/modules.json`, which maps each module key to its source, version and local folder. Local path modules are not copied, they are read in place.

Modules are not in the dependency lock file. That's why pinning module versions in the `version` argument or Git `ref` matters. A new module version is only picked up when you run `terraform init` (or `init -upgrade` for version ranges).

## 318: What are the h1 and zh hashes in the lock file?

```hcl
provider "registry.terraform.io/hashicorp/aws" {
  version     = "6.2.0"
  constraints = "~> 6.0"
  hashes = [
    "h1:abc...=",
    "zh:0123...",
  ]
}
```

- `zh:` hashes are SHA-256 of the official release zip files, as published by the registry for each platform.
- `h1:` hashes are a hash of the extracted package contents, which Terraform can check for any install method (registry, mirror, cache).

When you run `init` on a new platform, Terraform may only be able to add the `h1:` hash for that platform, which is why `terraform providers lock` with all platforms is useful.

## 319: How does Terraform verify that a provider is authentic?

When downloading from a registry, Terraform gets the release's `SHA256SUMS` file and its GPG signature. It checks the signature against the provider's signing key, then checks that the downloaded zip matches the checksum. After that, the lock file hashes make sure the same package is used every time.

Official providers are signed by HashiCorp. Partner and community providers are signed with keys their authors registered.

## 320: How do you protect against supply chain attacks in Terraform?

- Commit the lock file so provider binaries can't change silently
- Only use providers and modules from trusted publishers, and review community modules before using them
- Pin modules to a version or, better, a commit SHA for Git sources
- Mirror approved providers and modules into an internal registry
- Use Renovate or Dependabot so updates are visible pull requests
- Keep CI credentials scoped, because providers and modules run with them

Remember that a module can include `local-exec` provisioners or `external` data sources that run commands during your plan or apply.

## 321: Why is running terraform plan on untrusted code dangerous?

`plan` is not read only in terms of code execution. During a plan:

- Providers run with your credentials and can call any API
- `external` data sources run any program
- A malicious provider or module from a pull request can send your credentials anywhere
- Data sources like `http` can send data to outside URLs

So a pull request from a fork that changes Terraform code can steal secrets if CI runs `plan` with real credentials. Plans on untrusted pull requests should run without credentials or with read-only, tightly scoped ones, and only after a maintainer approves the run.

## 322: What options exist to encrypt Terraform state?

- **Backend encryption at rest:** S3 with SSE-KMS, Azure Storage encryption, GCS with customer-managed keys. Protects the stored file but anyone with read access to the bucket and key sees plain text.
- **HCP Terraform:** encrypts state with Vault-backed keys and controls access per workspace.
- **Client-side encryption:** OpenTofu has built-in state encryption (since 1.7) with keys from KMS or a passphrase. Terraform itself doesn't have this feature.

The most important controls are still limiting who can read state and keeping secrets out of it with ephemeral values.

## 323: How do you decide where to split state?

Good boundaries usually follow:

- **Rate of change:** the network changes rarely, apps change daily
- **Ownership:** the team that owns it should own its state
- **Blast radius:** a mistake in one state can't destroy things in another
- **Environment and region:** prod and dev never share a state
- **Lifecycle:** things created and destroyed together belong together

Too few states make plans slow and risky. Too many make cross-state dependencies painful. A state with a few hundred resources is usually fine. Thousands is a sign to split.

## 324: How would you structure Terraform for a large organization?

A common layout:

- **Foundation:** accounts or subscriptions, organization policies, identity, logging and billing, owned by a platform team
- **Shared networking:** hub VPCs, transit gateways, DNS
- **Shared services:** CI runners, container registries, monitoring
- **Product stacks:** each product team has its own states per environment, using approved modules

Around this you have a private module registry, standard pipelines, policy checks, and tooling for orchestration (HCP Terraform, Terragrunt, Atlantis or Stacks). Account vending is often itself a Terraform workflow.

## 325: What are Terraform Stacks?

Stacks are a feature of HCP Terraform for managing many related configurations as one unit. A stack has:

- **Components:** each one is a Terraform module (like network, cluster, app) with its own inputs and providers
- **Deployments:** copies of the whole stack, usually one per environment, region or account

Stacks handle ordering and passing values between components, run all deployments from one configuration, and can defer parts of a plan that depend on unknown values (like a cluster that doesn't exist yet). They are an alternative to wiring many workspaces together with run triggers and remote state.

## 326: What does a Stack configuration look like?

Components are defined in `.tfcomponent.hcl` files and deployments in `.tfdeploy.hcl` files.

```hcl
# components.tfcomponent.hcl
component "network" {
  source = "./modules/network"
  inputs = {
    cidr = var.cidr
  }
  providers = {
    aws = provider.aws.this
  }
}

component "app" {
  source = "./modules/app"
  inputs = {
    subnet_ids = component.network.private_subnet_ids
  }
  providers = {
    aws = provider.aws.this
  }
}
```

```hcl
# deployments.tfdeploy.hcl
deployment "dev" {
  inputs = {
    cidr = "10.0.0.0/16"
  }
}

deployment "prod" {
  inputs = {
    cidr = "10.10.0.0/16"
  }
}
```

Providers in stacks are declared with `required_providers` and `provider` blocks in the component files, and provider blocks can use `for_each`, which is useful for many regions.

## 327: What is the action block in Terraform 1.14?

Actions let you run operations that are not create, read, update or delete, like invoking a Lambda function, stopping an instance or invalidating a CDN cache. Providers define the action types.

```hcl
action "aws_lambda_invoke" "warm_cache" {
  config {
    function_name = aws_lambda_function.cache.function_name
    payload       = jsonencode({ mode = "warm" })
  }
}

resource "aws_lambda_function" "cache" {
  # ...
  lifecycle {
    action_trigger {
      events  = [after_create, after_update]
      actions = [action.aws_lambda_invoke.warm_cache]
    }
  }
}
```

Actions can be triggered by resource lifecycle events or run on their own with `terraform apply -invoke=action.aws_lambda_invoke.warm_cache`. They replace many uses of `local-exec` provisioners.

## 328: What is terraform query?

`terraform query` (Terraform 1.14) searches for existing resources in your cloud using `list` blocks in `.tfquery.hcl` files. Providers implement list resources for the types they support.

```hcl
# find.tfquery.hcl
list "aws_instance" "all" {
  provider = aws
}
```

```bash
terraform query
terraform query -generate-config-out=imported.tf
```

With `-generate-config-out`, Terraform writes resource and `import` blocks for what it found. It makes bulk imports much easier than looking up IDs one by one.

## 329: How do ephemeral resources work internally?

An ephemeral resource has a different lifecycle from a managed resource. Instead of create, read, update and delete, the provider implements:

- **Open:** get the value (read a secret, create a temporary token)
- **Renew:** extend a lease if the run takes longer than its lifetime
- **Close:** clean up, like revoking the token

Terraform opens it when it's needed in a run (in both plan and apply, separately) and closes it when it's no longer needed. Nothing is saved, so values may differ between plan and apply. That's why ephemeral values are only allowed in places where that doesn't matter.

## 330: What are the limitations of ephemeral values and write-only arguments?

- Ephemeral values can't go into normal resource arguments, outputs of the root module, `count` or `for_each`
- Because write-only values are never stored, Terraform can't detect if they changed. You have to bump a version argument to push a new value.
- Not every resource has write-only arguments yet. It depends on the provider.
- You need Terraform 1.10 or 1.11 and later, and providers built with the Plugin Framework support
- Ephemeral variables must be provided again when applying a saved plan

They reduce secrets in state, but they don't remove the need to protect state.

## 331: What sensitive data can end up in a saved plan file?

A saved plan contains the full configuration, the values of all input variables, the prior state and the planned new state, including sensitive values in plain form (it's a zip with readable files). Only ephemeral values are left out.

Anyone with access to the plan artifact can read the secrets. Store plan files like state: encrypted, access controlled, and deleted soon after use. Never post `terraform show -json` output of a plan in public places.

## 332: Can TF_LOG output leak secrets?

Yes. At `DEBUG` and `TRACE` levels, logs can include request and response bodies from providers, which may contain passwords, tokens and keys. Sensitive marking doesn't apply to provider HTTP logs.

Only enable detailed logging when needed, write it to a file with `TF_LOG_PATH` instead of CI logs, and clean it before sharing it in a bug report.

## 333: How do you give Terraform least-privilege permissions?

- Use separate roles per state or team instead of one admin role for everything
- Give plan jobs a read-only role and apply jobs a write role
- Scope apply roles to the services and resource names that state manages, using tags or name prefixes in conditions
- Use permission boundaries so Terraform can create IAM roles but can't give them more power than allowed
- Restrict the OIDC trust policy to specific repos, branches and environments
- Log everything with CloudTrail (or the equivalent) and review it

Complete least privilege is hard because Terraform needs many permissions, so start with clear boundaries and tighten over time.

## 334: Why use permission boundaries for Terraform-created IAM roles?

If Terraform can create IAM roles and attach policies, a pull request could create a role with full admin rights and use it to bypass every other control. A permission boundary is a policy that sets the maximum permissions any role can have.

You allow Terraform to create roles only if they have a specific boundary attached (using an IAM condition on `iam:PermissionsBoundary`). Then even a bad pull request can't create a role more powerful than the boundary.

## 335: How should the state bucket be secured?

- Block all public access
- Enable versioning so you can restore old state
- Encrypt with a KMS key and limit who can use the key
- Allow access only to the Terraform roles and a small admin group
- Enable access logging or CloudTrail data events
- Consider cross-region replication for disaster recovery
- Put state buckets in a separate, locked-down account
- Use lifecycle rules to remove very old noncurrent versions

## 336: How do you set up CI so pull requests from forks can't steal credentials?

- Don't give pull requests from forks access to secrets or OIDC roles (GitHub Actions does this by default for the `pull_request` event)
- Don't use `pull_request_target` to check out and run untrusted code with secrets
- Require a maintainer to approve workflow runs from outside contributors
- Scope the OIDC role trust policy to specific branches and environments, for example only `refs/heads/main` can assume the apply role
- Run plans for untrusted code without cloud credentials, or with a read-only role that can't reach secrets

## 337: How do you recover from a corrupted state file?

1. Stop all runs on that state
2. Get a previous version: S3 versioning, HCP Terraform state history, or `terraform.tfstate.backup` for local state
3. Download it, check it's valid JSON and look at its serial and resources
4. Push it back with `terraform state push` (you may need `-force` if the serial is lower)
5. Run `terraform plan` and compare with reality. Resources created after that version will be missing, so import them.

If no good version exists, you rebuild state by importing every resource, ideally with `import` blocks and `terraform query`.

## 338: How do you edit state by hand when no command can fix a problem?

As a last resort:

```bash
terraform state pull > state.json
cp state.json state.backup.json
# edit state.json carefully, and increase "serial" by 1
terraform state push state.json
terraform plan
```

Keep `lineage` the same, increase `serial`, and keep valid JSON. Make sure nobody else runs Terraform at the same time. Today `moved`, `removed`, `import` and the `state` subcommands cover almost every case, so hand edits should be very rare.

## 339: What happens when two people apply at the same time without locking?

Both read the same state version, make their changes and each write a new state. The second write overwrites the first. The resources created by the first apply exist in the cloud but are no longer in state.

The next plan tries to create them again and fails with "already exists", or worse, creates duplicates for resources without unique names. You fix it by importing the lost resources. This is why locking must never be disabled.

## 340: How do you handle many teams who need to change the same state?

That's a sign the state is too big or has unclear ownership. Options:

- Split the state by ownership so each team has its own
- Have the owning team expose a module or a self-service interface (like a YAML file in a repo) that others can change through pull requests
- Use a queue (Atlantis locks, HCP Terraform run queue) so runs don't overlap

Lock contention and long queues are a signal to rethink state boundaries, not just a scheduling problem.

## 341: How do you manage the order of applies across many states?

Terraform doesn't orchestrate across states by itself. Options:

- A CI pipeline with stages in dependency order (network, then data, then apps)
- Terragrunt `run --all`, which builds a graph from `dependency` blocks
- HCP Terraform run triggers or Stacks
- Keep dependencies one-way and stable, so most changes only touch one state

Design shared outputs to change rarely. If a change has to touch several states in order, handle it as a planned rollout, not an everyday thing.

## 342: How do you reduce the blast radius of Terraform changes?

- Small states with clear boundaries
- Separate accounts or subscriptions per environment
- `prevent_destroy` and provider deletion protection on critical resources
- Policy checks that fail plans with destroys of certain types
- CI that highlights deletes and replacements and requires extra approval for them
- Rolling out changes environment by environment and region by region
- Least privilege roles per state

## 343: How does Terraform perform with very large states?

Plan time grows with the number of resources, because each one is refreshed with API calls and evaluated. With thousands of resources, plans can take many minutes and hit API rate limits. Memory use also grows, and every run locks the whole state.

Main fixes are splitting the state, reducing data sources, raising parallelism when limits allow, and running plans with `-refresh=false` for some fast checks. `-target` can help in emergencies but is not a fix.

## 344: When is it OK to skip the refresh in a pipeline?

Skipping refresh (`-refresh=false`) is OK for quick feedback, like a lint-style plan on every push to see syntax and logic errors. The final plan that gets applied should always refresh, because otherwise it may miss drift and make wrong decisions (like updating a resource that was deleted).

Some teams run a fast no-refresh plan on each commit and a full plan right before apply.

## 345: How does create_before_destroy spread through dependencies?

If resource A has `create_before_destroy = true` and depends on B, then B must also be replaced in create-before-destroy order when both are replaced, or the order of operations would be impossible. Terraform automatically turns on create-before-destroy for those dependencies and records it in state.

This can surprise you: a resource without the flag in the code may still behave as create-before-destroy. That can fail for resources with unique names that you didn't expect to be affected.

## 346: How does Terraform know the destroy order for resources removed from the code?

When a resource is removed from the configuration, its dependencies are no longer in the code. Terraform uses the `dependencies` list stored with each instance in state to build the correct destroy order. This is one reason state keeps dependency information.

If you edit state by hand and break this list, destroy order can be wrong and deletions may fail (like deleting a VPC before its subnets).

## 347: What are the rules and limits of moved blocks?

- `from` and `to` must be the same resource type, unless the provider supports moving between types (Terraform 1.8 and later added cross-type moves for providers that implement them)
- You can move into and out of modules, but only within the same configuration (state)
- You can't move to an address that already exists in state
- You can't use `moved` to change providers
- Chains of moves (`a` to `b`, `b` to `c`) are followed
- In a module, `moved` blocks can only refer to resources inside that module

If a `moved` block's `from` doesn't exist in state, Terraform ignores it, so keeping old blocks around is safe.

## 348: Why should shared modules keep their moved blocks?

A shared module is used by many callers who upgrade at different times. If you rename a resource in version 2.0 and add a `moved` block, a caller upgrading from 1.x gets the move. If you delete the block in 2.1, a caller jumping from 1.x straight to 2.1 gets a destroy and create instead.

So in shared modules, keep `moved` blocks for a long time, or forever. In a root module used only by one team, you can delete them once all environments have applied.

## 349: Where can import blocks be used?

For most of Terraform 1.x, `import` blocks are only allowed in the root module. To import a resource that lives in a child module, you still write the block in the root module with the full address:

```hcl
import {
  to = module.network.aws_vpc.this
  id = "vpc-0abc123"
}
```

Newer releases started to allow `import` blocks inside modules. Check the docs for your version. Import blocks can be left in code after applying, they do nothing once the resource is in state.

## 350: How do you fix "Inconsistent conditional result types"?

Both sides of a conditional must have types that can be unified. Objects with different attributes can't, so this fails:

```hcl
locals {
  config = var.prod ? { size = 100, multi_az = true } : { size = 20 }
}
```

Fixes: give both sides the same attributes (use `null` for the missing ones), or use a map lookup:

```hcl
locals {
  config = var.prod ? { size = 100, multi_az = true } : { size = 20, multi_az = null }
}
```

```hcl
locals {
  configs = {
    prod = { size = 100, multi_az = true }
    dev  = { size = 20, multi_az = false }
  }
  config = local.configs[var.prod ? "prod" : "dev"]
}
```

## 351: What errors can try not catch?

`try` only catches errors that happen while evaluating an expression with real values, like a missing map key, a wrong index or a failed type conversion. It does not catch:

- References to things that don't exist in the config (undeclared variables or resources), because those are found before evaluation
- Syntax errors
- Errors that happen later, inside providers, during plan or apply

Also, if the expression is unknown during the plan, `try` returns an unknown value instead of choosing a fallback. Use `try` for shaky data like decoded JSON or YAML, not to hide mistakes in your code.

## 352: How do optional attribute defaults work with nested objects?

Defaults from `optional()` are applied when the caller leaves the attribute out. For nested objects, defaults inside are only applied if the nested object itself exists.

```hcl
variable "settings" {
  type = object({
    logging = optional(object({
      enabled   = optional(bool, true)
      retention = optional(number, 30)
    }), {})
  })
}
```

If the caller passes `settings = {}`, `logging` becomes `{}` (its default), and then its own defaults kick in, giving `{ enabled = true, retention = 30 }`. Without the `{}` default on `logging`, it would be `null` and the inner defaults would not apply.

## 353: What is the difference between passing null and leaving an argument out?

For resource arguments, there is no difference: `null` means "not set" and the provider uses its default.

For module inputs, it depends. If you leave the input out, the variable's `default` is used. If you pass `null`, the variable becomes `null`, unless it has `nullable = false`, in which case the default is used. For `optional()` attributes in an object, passing `null` also gives you the default.

So in modules, set `nullable = false` on inputs that should always have a value. Callers can then pass `null` to mean "use the default".

## 354: Does jsonencode keep the sensitive mark?

Yes. If any part of the input to a function is sensitive, the result is sensitive too. `jsonencode({ password = var.db_password, user = "app" })` produces a sensitive string, and Terraform hides the whole JSON in the plan.

This is a common reason why big policies or configs show as `(sensitive value)` and become hard to review. Keep sensitive values out of large documents where you can, for example by referencing a secret ARN instead of the secret itself.

## 355: What happens when a provider block uses values that are unknown during the plan?

Terraform has to configure the provider before it can plan resources that use it. If the configuration contains unknown values, Terraform passes them as unknown and it's up to the provider. Some providers can still plan (they postpone API calls), some fail with an error, and some silently use defaults (like connecting to `localhost`), which is the worst case.

The safe approach is to make sure provider configuration only depends on values known at plan time: variables, data sources that can be read during plan, or outputs of another state. Deferred actions and Stacks are meant to handle this case properly.

## 356: What does "Provider configuration not present" mean?

It appears when state contains resources that were created with a provider configuration (like `aws.us`) that no longer exists in the code. Terraform needs that provider to delete or refresh those resources, but can't find it.

Usually it happens after removing a module that contained its own `provider` block, or after deleting an aliased provider while resources still use it. The fix is to put the provider configuration back, apply the removal of the resources, and only then delete the provider block.

## 357: How do you remove a module that has its own provider block?

You can't just delete the module call, because the provider configuration disappears together with the resources it is needed to destroy. Steps:

1. Keep the module call but destroy its resources first, for example by setting a variable that makes all resources `count = 0`, or run `terraform destroy -target=module.legacy`
2. Apply
3. Delete the module call

Better yet, refactor the module to receive its provider from the caller (with `providers = {}`), so this problem goes away in the future.

## 358: Can you use for_each on provider blocks?

Not in regular Terraform. Provider configurations are static, so you need one block per region or account, written by hand or generated. Also, a module instance created with `for_each` can't pick a different provider per instance, since the `providers` map must be static.

Terraform Stacks support `for_each` on provider blocks, and OpenTofu added `for_each` for providers in version 1.9. In plain Terraform, people use code generation, Terragrunt, or one root module per region.

## 359: How do Terraform and OpenTofu differ today?

They share the same base up to Terraform 1.5 and are still very similar, but each added its own features since then. Examples:

- **OpenTofu only:** client-side state encryption, `for_each` on providers, early variable evaluation in backend and module source blocks, the `-exclude` option, `.tofu` file extension overrides
- **Terraform only:** Stacks and the HCP Terraform integration, `terraform query` and list resources, actions, some newer test features

Both have ephemeral resources and provider-defined functions, though details differ. Most providers work with both. Using a feature that only one supports makes the code non-portable.

## 360: How would you migrate from Terraform to OpenTofu?

1. Check that your Terraform version is one OpenTofu supports for migration (their docs list paths for each version)
2. Remove or replace any Terraform-only features (like `cloud` blocks if you're leaving HCP Terraform)
3. Install `tofu` and run `tofu init` in a copy. Providers come from the OpenTofu registry, which mirrors most providers.
4. Run `tofu plan` and make sure it shows no changes
5. Back up state, then switch the pipelines over environment by environment

State files are compatible for the shared versions, so no conversion is usually needed. Rolling back gets harder once you use OpenTofu-only features.

## 361: What stages does a run go through in HCP Terraform?

A typical run:

1. **Pending:** waiting in the queue (only one run per workspace at a time)
2. **Pre-plan run tasks:** optional outside checks
3. **Plan**
4. **Post-plan run tasks:** for example security scanners
5. **Cost estimation**
6. **Policy check:** Sentinel or OPA policy sets
7. **Pre-apply run tasks**
8. **Apply:** after manual confirmation or automatically if auto-apply is on
9. **Post-apply run tasks**

A failing mandatory policy or run task stops the run before apply.

## 362: What does a simple Sentinel policy look like?

```sentinel
import "tfplan/v2" as tfplan

allowed_types = ["t3.micro", "t3.small", "t3.medium"]

instances = filter tfplan.resource_changes as _, rc {
  rc.type is "aws_instance" and
  rc.mode is "managed" and
  (rc.change.actions contains "create" or rc.change.actions contains "update")
}

main = rule {
  all instances as _, i {
    i.change.after.instance_type in allowed_types
  }
}
```

The policy reads the plan through the `tfplan/v2` import and passes only if every new or changed instance uses an allowed type.

## 363: When should you use custom conditions and when policy as code?

- **Custom conditions** (validation, preconditions, checks) belong to the module. They describe what the module itself needs to work correctly, like "subnets must be in at least two zones". They travel with the module.
- **Policy as code** (Sentinel, OPA) belongs to the organization. It enforces rules across all teams and modules, like "no public buckets" or "only approved regions", and authors of a module can't skip it.

Use both: modules protect their own assumptions, policies protect the company.

## 364: What does a good testing strategy for Terraform look like?

From cheap to expensive:

1. **Static checks:** `fmt`, `validate`, TFLint, security scanners on every commit
2. **Plan tests:** `terraform test` with `command = plan` and mock providers to check logic
3. **Policy tests:** run OPA or Sentinel against real plans
4. **Integration tests:** `terraform test` with real applies (or Terratest) in a sandbox account
5. **Post-deploy checks:** `check` blocks and monitoring in real environments

Most bugs are caught by the first three steps, which are fast and free. Real applies catch problems with permissions, quotas and API behavior.

## 365: How does terraform test handle state and cleanup?

Each test file gets its own fresh state (per module under test), separate from your real state. `run` blocks in a file execute in order, and each one builds on the state left by earlier runs. At the end of the file, Terraform destroys everything in reverse order.

If cleanup fails (for example a resource can't be deleted), Terraform reports which resources were left behind, and you must remove them by hand. That's why integration tests should run in a separate sandbox account with regular cleanup jobs.

## 366: How would you design active-active infrastructure in two regions with Terraform?

- Put the per-region stack in a module and call it once per region with an aliased provider (or use one root module per region)
- Keep global resources (DNS, CDN, IAM, global tables) in a separate state
- Use a global routing layer like Route 53 latency or failover records pointing at both regions
- Replicate data (DynamoDB global tables, Aurora global databases, S3 replication)
- Apply region by region so one bad change doesn't hit both at once

Separate states per region also mean you can still change one region if the other region's APIs are having problems.

## 367: Why are multi-cloud abstraction modules usually a bad idea?

A module that hides whether it creates an AWS, Azure or GCP database must reduce everything to features common to all three. You lose each cloud's useful options, and the module gets complicated with many conditionals. Different clouds also work differently for networking, IAM and limits, so the abstraction leaks anyway.

Terraform gives you one workflow across clouds, not one API. It's usually better to have good modules per cloud with a similar style.

## 368: What is a thin wrapper module and why is it an anti-pattern?

A thin wrapper module just wraps a single resource and passes every argument through as a variable. It adds a layer to maintain, hides the provider docs, and every new provider argument needs a new variable. It gives nothing in return.

A module is worth it when it combines several resources into a meaningful unit (like a bucket with encryption, logging, policy and replication) or enforces standards. Otherwise use the resource directly.

## 369: How do you choose between Terragrunt, HCP Terraform workspaces and Stacks?

- **Terragrunt:** open source, works with any backend and CI, good at DRY config and running many modules in order. Adds another tool and file format.
- **HCP Terraform workspaces:** managed runs, state, permissions and policies. Cross-workspace dependencies need run triggers and outputs.
- **Stacks:** built into HCP Terraform for many environments of the same set of components, with ordering and deferred changes. Newer, so ecosystem and patterns are still growing.

The choice usually depends on whether you use HCP Terraform at all, and on how many environments of the same thing you run.

## 370: What does GitOps for Terraform look like?

In GitOps, Git is the single source of truth and an automated system applies whatever is on the main branch. For Terraform:

- Atlantis or HCP Terraform VCS workflows: plans on pull requests, applies on merge or approval
- Kubernetes controllers like the Flux Tofu Controller, which reconcile Terraform modules on a loop like Kubernetes objects
- Scheduled drift detection that alerts or opens pull requests when reality differs from Git

The main difference from pure Kubernetes GitOps is that Terraform applies can destroy things, so auto-applying without review is risky.

## 371: How would you create a temporary environment for each pull request?

- Use a separate state per pull request, for example a backend key like `preview/pr-123.tfstate` or a workspace named after the pull request
- Use names with the pull request number so resources don't clash
- Keep it small: reuse shared networking and databases where possible, and create only the app layer
- Destroy it automatically when the pull request is closed, plus a scheduled job that destroys old leftovers
- Set budgets and alerts on the sandbox account

Shared heavy resources (like a database cluster) usually come from a data source, not created per pull request.

## 372: How do you enforce tagging across all resources?

- `default_tags` in the AWS provider (or similar in other providers) for the common tags
- A module that builds the standard tag map from inputs like team and environment
- Policy checks (OPA, Sentinel, Checkov) that fail plans when required tags are missing
- Cloud-side rules like AWS Organizations tag policies and AWS Config rules to catch resources not made with Terraform

Note that some resources don't support tags, and some services apply tags differently, so policies need exceptions.

## 373: How do you manage thousands of similar resources efficiently?

- Drive them from data (a YAML or JSON file, or a map variable) with `for_each`, not copy-pasted blocks
- Split them across several states if one state gets too slow, for example by team or by first letter of the name
- Use bulk resources where the provider has them, like a single resource that manages many records
- Watch out for API rate limits and lower parallelism if needed

At some point, a purpose-built tool or a small service talking to the API may fit better than Terraform for very dynamic data.

## 374: How do you handle many regions or accounts without for_each on providers?

Since each provider configuration must be written out, common approaches are:

- Generate the provider blocks and module calls with a script or template from a list of regions
- Use one root module per region or account and run them with Terragrunt or a pipeline matrix
- Use Terraform Stacks, which allow `for_each` on providers
- Use OpenTofu, which supports it natively

A pipeline matrix (one job per region running the same root module with different variables and backend keys) is often the simplest.

## 375: When would you generate Terraform configuration as JSON?

Terraform accepts `.tf.json` files with the same structure as HCL. Generating JSON is easier and safer than generating HCL text when a program creates the config, because every language has a JSON library.

```json
{
  "resource": {
    "aws_s3_bucket": {
      "logs": {
        "bucket": "acme-logs"
      }
    }
  }
}
```

Typical uses are internal platforms that create configs from a database or UI. Humans should still write HCL, since JSON is harder to read and doesn't allow comments in the usual way.

## 376: Why is -target dangerous in normal use?

- Terraform only plans the targeted resources and their dependencies. Other changes in the code are not applied, so the state and code drift apart.
- Outputs and resources that depend on the target may not be updated
- It's easy to forget something and leave the system half updated
- The next full plan may include surprising changes from earlier targeted runs

HashiCorp says to use it only for recovering from errors or working around Terraform limits, and to follow up with a full plan and apply.

## 377: What does "saved plan is stale" mean?

When you save a plan, Terraform records the state's lineage and serial. If the state was changed after that (by another apply, an import or a state command), applying the old plan would use outdated data. Terraform refuses with a "Saved plan is stale" error.

The fix is to create a new plan and review it again. In CI, keep the time between plan and apply short, and lock the state or queue runs so nothing else applies in between.

## 378: How do you find out if two states manage the same resource?

Terraform can't detect this by itself, since each state is independent. Signs are perpetual diffs where two configs keep changing the same setting back and forth.

To find it:

- Export resource IDs from all states (`terraform show -json` and jq) and look for duplicates
- Use a `ManagedBy` or `TerraformState` tag that includes the state name, and check for conflicts
- Search the code for the same names or IDs in `import` blocks

Prevent it by clear ownership rules and by never importing something without checking whether another state already has it.

## 379: How do you rotate a secret that is set through a write-only argument?

Since Terraform doesn't store the value, it can't see that the value changed. The provider adds a version argument for this:

```hcl
ephemeral "aws_secretsmanager_secret_version" "db" {
  secret_id = aws_secretsmanager_secret.db.id
}

resource "aws_db_instance" "main" {
  # ...
  password_wo         = ephemeral.aws_secretsmanager_secret_version.db.secret_string
  password_wo_version = 2   # was 1
}
```

Update the secret at the source, increase `password_wo_version`, and apply. The provider sends the new value because the version changed. The version is stored in state, but the secret is not.

## 380: How do you know in advance whether a change will replace a resource?

- Read the provider docs. Many arguments are marked as forcing a new resource.
- Run `terraform plan` and look for `-/+` and `# forces replacement` next to the attribute
- In CI, parse the plan JSON for actions `["delete", "create"]` or `["create", "delete"]` and flag them
- Test the change in a lower environment first

```bash
jq -r '.resource_changes[] | select((.change.actions | length) == 2) | .address' plan.json
```

## 381: How do you change a database instance without unexpected downtime?

- Check whether the change is in-place or a replacement in the plan
- Know that some in-place changes still cause a restart, like changing the instance class
- Use the provider's options for timing. On RDS, `apply_immediately = false` (the default) waits for the maintenance window, `true` applies now.
- Use Multi-AZ so a failover happens instead of a long outage
- For changes that need replacement (like some engine changes), use a blue/green deployment or snapshot and restore instead of letting Terraform recreate it

## 382: What are the risks of ignore_changes?

`ignore_changes` hides real differences. If someone changes an ignored attribute by hand, Terraform never notices. If you later change that attribute in code, Terraform also ignores your change, which surprises people.

With `ignore_changes = all`, the resource becomes create-only: no updates ever. Use it only for attributes that are truly owned by something else, and leave a comment explaining why.

## 383: How do you work around a provider bug?

- Check the provider's issue tracker. There may be a workaround or a fixed version.
- Pin to the last version that worked
- Use `ignore_changes` for a perpetual diff caused by the bug
- Manage the broken part another way temporarily (another resource type, a `terraform_data` with `local-exec`, or the cloud CLI in the pipeline)
- Report the bug with a minimal config and `TF_LOG=DEBUG` output

Add a comment and a ticket for every workaround, so it gets removed once the bug is fixed.

## 384: How can you use a patched fork of a provider?

- Build the patched provider and publish it to a private registry or a network mirror under your own namespace (like `acme/aws`), then point `required_providers` at it
- Use `terraform state replace-provider` to move existing resources to the new source address
- For local testing only, use `dev_overrides`

Maintaining a fork is costly, so contribute the fix upstream and switch back as soon as it's released.

## 385: How do you read Terraform TRACE logs?

With `TF_LOG=TRACE`, logs show the graph build, each graph node evaluation, the gRPC calls to providers, and (from providers) HTTP requests and responses. Useful things to search for:

- `[ERROR]` and `[WARN]` lines
- The resource address you care about, to follow its plan and apply
- Provider HTTP requests, to see what was actually sent to the API

If Terraform itself crashes, it writes a `crash.log` file with a stack trace, which you attach to a bug report.

## 386: How do you debug an unexpected diff?

1. Run `terraform plan` and note exactly which attribute changes and from what to what
2. Run `terraform state show <address>` to see what state has
3. Check the real object in the console or CLI to see the actual value
4. Use `terraform console` to evaluate the expression in your code
5. Compare `before` and `after` in `terraform show -json` for complex values

Often the cause is a normalized value (order, case, defaults), a value computed differently each time, or another system changing the resource.

## 387: How do you verify that a big refactor only moves resources?

Run a plan with your `moved` blocks and check the JSON. A moved resource with no changes has `previous_address` set and the `no-op` action.

```bash
terraform plan -out=tfplan
terraform show -json tfplan > plan.json

# anything that is not a no-op
jq -r '.resource_changes[] | select(.change.actions != ["no-op"]) | "\(.change.actions) \(.address)"' plan.json
```

If this list is empty (or only contains things you expect), the refactor is safe to apply.

## 388: How do you move a resource to a different account?

You can't move most cloud resources between accounts at all. Terraform can't do it either, since it only reflects what the API allows.

So you create a new resource in the target account, move the data (snapshots shared across accounts, S3 replication, database replication), switch traffic, then remove the old one. In Terraform that means new resource blocks with an aliased provider for the new account, and later a removal of the old ones. For resources that some services can transfer (like domains), you transfer outside Terraform and then `import` in the new state.

## 389: How do you split one state into several?

1. Create the new root module with the code for the resources you're moving
2. In the new module, add `import` blocks for those resources, and in the old module add `removed` blocks with `destroy = false` and delete the resource code
3. Plan both and make sure the old one only forgets and the new one only imports
4. Apply the old one first, then the new one
5. Replace references between them with remote state, data sources or a parameter store

With many resources, a script can generate the `import` blocks from `terraform state list` and `terraform state show` output.

## 390: How do you merge two states into one?

Same idea in reverse: move the code from one configuration into the other, add `import` blocks in the target for every resource, and `removed` blocks with `destroy = false` in the source. Apply the source first so the resources are forgotten, then the target to import them.

The older way was `terraform state mv -state=a.tfstate -state-out=b.tfstate` with local copies and pushing them back, which is faster but has no plan or review and is easy to get wrong.

## 391: How do you upgrade a very old Terraform project (0.11 or 0.12)?

- Go step by step through the old upgrade paths: 0.11 to 0.12 (big syntax change, the old `0.12upgrade` command helped), then 0.13 (`required_providers` with source addresses), then 0.14 and 0.15
- After 0.15, you can usually go straight to the latest 1.x
- At each step, run `init`, `plan` (should show no changes) and `apply`, so the state is upgraded
- Upgrade providers along the way, since very old provider versions don't support new Terraform and the other way round

Read the upgrade guide for each version before you start. Doing it in a copy of the state first is a good idea.

## 392: How do you audit who changed infrastructure and when?

- Git history and pull requests show who changed the code and who approved it
- CI logs show who triggered the apply and the plan that was applied
- HCP Terraform keeps run history, state versions and an audit trail
- State bucket versioning shows when state changed
- Cloud audit logs (CloudTrail, Azure Activity Log, GCP Audit Logs) show the actual API calls and which role made them

Using a dedicated role per pipeline makes cloud logs much easier to connect to a specific state.

## 393: What problems happen when Terraform manages Kubernetes objects that controllers also change?

Kubernetes controllers often add or change fields: annotations, labels, default values, status, replica counts from the HPA. Terraform sees those as drift and tries to remove them, causing perpetual diffs or fights with the controller.

Fixes are `ignore_changes` on those fields, the `field_manager` and `computed_fields` settings in `kubernetes_manifest`, or leaving app-level objects to tools like Helm or Argo CD and keeping Terraform for the cluster and platform add-ons.

## 394: What are the pros and cons of installing Helm charts with Terraform?

Pros:

- One tool and one pipeline for the cluster and its base add-ons (ingress controller, cert-manager, monitoring)
- Values can come straight from Terraform outputs (IAM role ARNs, DNS names)

Cons:

- The plan shows the Helm values diff but not the full Kubernetes changes the chart makes
- A failed Helm release can leave state and cluster out of sync
- App deploys through Terraform are slow and couple app releases to infrastructure runs

A common split is Terraform for the cluster and a few platform charts, and a GitOps tool for everything else.

## 395: What should you watch out for when upgrading a managed Kubernetes cluster with Terraform?

- Upgrade the control plane version first, then node groups, one minor version at a time
- Check the plan: some changes to node groups replace them instead of rolling, which can cause downtime
- Make sure add-ons and their versions are compatible with the new version
- Watch for API removals in Kubernetes that break manifests managed by the Kubernetes or Helm providers
- Use `create_before_destroy` or blue/green node groups to move workloads safely

Test the upgrade in a non-production cluster with the same Terraform code first.

## 396: How do you do a major version upgrade of an RDS database with Terraform?

Change `engine_version` and set `allow_major_version_upgrade = true`. You may also need a new parameter group for the new version family.

```hcl
resource "aws_db_parameter_group" "pg17" {
  name   = "app-pg17"
  family = "postgres17"
}

resource "aws_db_instance" "main" {
  # ...
  engine_version              = "17"
  parameter_group_name        = aws_db_parameter_group.pg17.name
  allow_major_version_upgrade = true
  apply_immediately           = true
}
```

Take a snapshot first and test in a copy. For less downtime, RDS blue/green deployments are often a better option than an in-place upgrade.

## 397: How should outputs shared between states be designed?

Treat them as a public API between teams:

- Keep names stable and document them
- Output simple values (IDs, ARNs, names) instead of whole resource objects
- Add new outputs instead of changing the meaning of existing ones
- Deprecate before removing, and tell the consuming teams
- Prefer publishing values to a parameter store, so consumers don't need access to your state

Changing a widely used output is like a breaking API change and needs the same care.

## 398: How do you roll out a risky change across many regions?

- Apply to one low-traffic region first, wait, watch metrics and alarms
- Continue in waves (one region, then a few, then the rest)
- Use separate states per region so each wave is a separate apply
- Have a tested rollback, which in Terraform usually means reverting the code and applying again
- Pause the rollout automatically if alarms fire

A pipeline with one stage per region and manual or automatic gates between them works well.

## 399: How are workspace states stored in the S3 backend?

The `default` workspace uses the `key` you set. Other workspaces are stored under `<workspace_key_prefix>/<workspace name>/<key>`, and the prefix defaults to `env:`.

```text
s3://acme-tf/app/terraform.tfstate              # default
s3://acme-tf/env:/staging/app/terraform.tfstate # staging
s3://acme-tf/env:/prod/app/terraform.tfstate    # prod
```

This matters when writing IAM policies for the state bucket, because each workspace's path must be allowed separately if you want to restrict access per environment.

## 400: How do you work with tree-shaped data when HCL has no recursion?

HCL has no recursive functions, so you can't walk a tree of unknown depth. Options:

- Limit the depth and use nested `for` expressions for each level
- Store the data flat, with each item pointing to its parent (`parent = "engineering"`), and look up parents with maps
- Pre-process the data outside Terraform (a script that flattens YAML into JSON)

```hcl
locals {
  teams = {
    engineering = { parent = null }
    backend     = { parent = "engineering" }
    payments    = { parent = "backend" }
  }
}
```

Resources that need a parent ID (like nested OUs or groups) can then reference each other by key. Deep hierarchies may need one resource block per level.

## 401: What is a data-only module?

A data-only module contains only data sources and outputs, no managed resources. It looks things up and gives them standard names, for example "find the shared VPC and its private subnets for this environment".

```hcl
# modules/network-lookup/main.tf
data "aws_vpc" "this" {
  tags = { Name = "shared-${var.environment}" }
}

data "aws_subnets" "private" {
  filter {
    name   = "vpc-id"
    values = [data.aws_vpc.this.id]
  }
  tags = { Tier = "private" }
}

output "vpc_id" {
  value = data.aws_vpc.this.id
}

output "private_subnet_ids" {
  value = data.aws_subnets.private.ids
}
```

Consumers get a simple, stable interface without needing access to the network team's state.

## 402: What is dependency inversion in Terraform modules?

Instead of a module creating everything it needs (its own VPC, its own IAM role, its own KMS key), it takes those as inputs. The caller decides where they come from: created in the same configuration, looked up with a data source, or read from another state.

```hcl
module "app" {
  source     = "./modules/app"
  vpc_id     = module.network.vpc_id
  subnet_ids = module.network.private_subnet_ids
  kms_key_id = data.aws_kms_key.shared.arn
}
```

This makes modules smaller, easier to reuse and easier to test. HashiCorp's module guide recommends this style.

## 403: Why can't a consumer use for_each over a module output whose keys come from created resources?

If a module outputs a map keyed by generated values (like resource IDs), those keys are unknown during the first plan. A consumer using that map in `for_each` gets "Invalid for_each argument".

The fix is in the module design: key outputs by values from the input (names), not by computed attributes.

```hcl
# good: keys are the input names, values may be unknown
output "subnet_ids" {
  value = { for k, s in aws_subnet.this : k => s.id }
}
```

## 404: How does Terraform evaluate locals and variables?

Locals are not evaluated top to bottom like a script. Each local, variable, resource and output is a node in the graph, and it's evaluated when the things it references are ready. That's why the order in files doesn't matter.

It also means locals that refer to each other in a loop (`a` uses `b`, `b` uses `a`) cause a cycle error. Locals are evaluated per module instance, so a module with `for_each` evaluates its locals once for each instance.

## 405: How does HCP Terraform use check blocks for continuous validation?

Check block results are stored with each state. HCP Terraform health assessments re-run them on a schedule, without an apply, and show which checks are failing. Combined with drift detection, this tells you when something is broken or changed long after the last deploy, like a certificate about to expire or an endpoint that stopped answering.

You can get notifications for failing checks, so they work as simple monitoring defined right next to the infrastructure.

## 406: What compatibility promises does Terraform 1.x make?

Terraform 1.x promises that configurations, state, plugin protocols and the main CLI workflow written for 1.0 keep working on all later 1.x versions. Things that can still change include experimental features, provider behavior (providers are versioned separately), and details of human-readable output.

This is why upgrades within 1.x are usually low risk, while provider major versions are where most breaking changes happen.

## 407: When is a refresh-only apply useful during an incident?

During an incident, people often change things by hand (scale up, open a port, change a setting). Afterwards, a normal apply would revert those changes. A refresh-only plan lets you see exactly what changed outside Terraform.

You then either update the code to match (keep the change) or apply normally to revert it. `terraform apply -refresh-only` accepts the real values into state without changing anything, which is useful when you want state to match reality before deciding.

## 408: What is the difference between timestamp and plantimestamp?

`timestamp()` returns the time when it's evaluated, so it's unknown during the plan and becomes a different value during apply. It causes changes on every run when used in resources.

`plantimestamp()` (Terraform 1.5 and later) returns the time the plan was created, and is known during the plan. It's useful in checks and conditions, like checking if a certificate expires within 30 days:

```hcl
check "cert_not_expiring" {
  assert {
    condition     = timecmp(aws_acm_certificate.site.not_after, timeadd(plantimestamp(), "720h")) > 0
    error_message = "Certificate expires in less than 30 days."
  }
}
```

## 409: Why can't a module with for_each use a different provider for each instance?

The `providers` map in a module block is static. Every instance of a `for_each` module gets the same provider configurations, so this does not work:

```hcl
module "regional" {
  source   = "./modules/regional"
  for_each = toset(["eu-central-1", "us-east-1"])

  providers = {
    aws = aws[each.key]   # not allowed
  }
}
```

Terraform needs to know the provider for every resource while building the graph, before `for_each` is evaluated. You have to write one module block per region, each with its own aliased provider, or use Stacks or OpenTofu which support this.

## 410: How do you run CI only for the Terraform folders that changed?

In a repo with many root modules, planning everything on each pull request is slow. Options:

- Use path filters in CI to find changed folders, and build a job matrix from them
- Also include folders that use a changed local module (find them by searching for its `source` path)
- Atlantis and HCP Terraform can trigger runs based on changed paths
- Terragrunt has options to run only modules affected by changes

Always run everything on a schedule as well, to catch drift and changes to shared modules you missed.

## 411: Is it safe to cache the .terraform directory in CI?

Caching provider downloads is safe and common: set `TF_PLUGIN_CACHE_DIR` and cache that folder, keyed by the lock file hash. The lock file still checks the hashes.

Caching the whole `.terraform` folder is riskier, because it also contains backend config and module copies. A stale cache can point at the wrong backend or use old module code. Most teams cache only the plugin cache and run `terraform init` on every job.

## 412: How do you manage lock files in a monorepo with many root modules?

Each root module has its own `.terraform.lock.hcl` file, because each one selects its own provider versions. Keeping them consistent takes effort:

- Use Renovate or Dependabot to update all lock files together
- Run `terraform providers lock` with all platforms in each root module
- Add a CI check that fails if a lock file is missing hashes for the CI platform or is out of date

Some teams also share a common `versions.tf` pattern so constraints are the same everywhere.

## 413: The plan wants to destroy and recreate a production database. What do you do?

1. Don't apply. Find out why from the `# forces replacement` line in the plan.
2. Common causes: a renamed resource (needs a `moved` block), a changed attribute that forces replacement (like engine, identifier or subnet group), a provider upgrade that changed behavior, or a `count` to `for_each` switch
3. Fix the code so the plan shows no replacement: add `moved`, revert the attribute, or use `ignore_changes` if the change is not needed
4. If the change really needs a new database, plan a proper migration (snapshot and restore, blue/green, replication) instead of letting Terraform do it

Also make sure `prevent_destroy` and `deletion_protection` are on, so this can't happen by accident.

## 414: Someone opened a port in a security group through the console and the plan wants to close it. What do you do?

First find out why it was opened. Talk to the person, or check CloudTrail.

- If it was a mistake or a temporary fix, apply to close it and communicate it
- If it is needed, add the rule to the code and open a pull request. The plan should then show no change.

Then fix the process: limit console write access, and set up drift detection so the next manual change is found quickly.

## 415: Someone ran apply with a newer Terraform version and now others get an error reading the state. What do you do?

The newer version may have written the state in a way older versions refuse to read. Options:

- Upgrade everyone and CI to that newer version (usually the simplest and correct choice)
- If you must go back, restore the previous state version from backend history, then check with a plan in the older version that nothing changed in between

To prevent it, set `required_version` with an upper bound or an exact pin, use `.terraform-version` with a version manager, and only apply from CI.

## 416: An apply failed halfway in one of three regions. How do you recover?

1. Read the error and fix the cause (quota, permissions, a bad value)
2. Look at the state: resources created before the failure are saved, the failed one may be tainted
3. Run a new plan for that region. It should show only the remaining changes and the tainted replacement.
4. Apply again
5. If the other regions are in separate states, they are not affected. If everything is in one state, the other regions' changes may also be half done, so read the plan carefully.

Separate states per region make this much simpler.

## 417: A provider upgrade makes the plan want to replace hundreds of resources. What do you do?

Stop and don't apply. Then:

- Read the provider's changelog and upgrade guide. Often a default changed or an attribute was renamed, and there's an explained migration path.
- Check if the provider added a state migration that needs a specific intermediate version
- Change the code to match the new behavior (set the old default explicitly, rename the argument)
- If it's a bug, pin the previous version and report it

Upgrade in a non-production environment first, and keep provider upgrades in their own pull request.

## 418: The plan for a configuration takes 30 minutes. How do you fix it?

- Measure first: `TF_LOG=DEBUG` timestamps show where time goes (refresh of certain resource types, slow data sources, rate limiting retries)
- Split the state by lifecycle or ownership. This is usually the real fix.
- Remove or reduce slow data sources
- Raise `-parallelism` if the provider isn't being throttled
- Move rarely changing parts (like DNS records or IAM) to their own state

Long plans make people avoid running plans, which leads to drift and bigger, riskier changes.

## 419: You found database passwords in plain text in your state. How do you fix it?

1. Treat the secret as leaked if many people or systems could read the state. Rotate it.
2. Lock down access to the state backend and its history (old versions still contain the secret)
3. Change the code so the secret no longer goes into state: write-only arguments, ephemeral resources, or let the service manage it (like RDS `manage_master_user_password`)
4. Apply, so new state versions don't have the secret
5. Delete old state versions that contain it, if your policy allows
6. Check where else the state or plans were copied (CI artifacts, laptops)

## 420: You need to rename a resource that exists in 50 workspaces. How do you do it safely?

Add a `moved` block next to the rename in the shared code. Each workspace picks up the move on its next run, with no destroy or create.

Then:

- Run plans across all workspaces (a script or the HCP Terraform API) and check that every plan only shows moves
- Apply them in waves
- Keep the `moved` block until all workspaces have applied, and in shared modules keep it for good

Never use `terraform state mv` in 50 places by hand.

## 421: How would you migrate infrastructure from CloudFormation to Terraform?

1. Pick one stack at a time, starting with low risk ones
2. Set `DeletionPolicy: Retain` on all resources in the stack and update the stack, so deleting it won't delete resources
3. Write Terraform code and `import` blocks for the resources (`terraform query` or `-generate-config-out` help)
4. Plan until there are no changes, then apply the import
5. Delete the CloudFormation stack. Resources stay because of `Retain`.
6. Run a final plan to confirm

Watch out for resources CloudFormation created implicitly, and for outputs other stacks import with `Fn::ImportValue`.

## 422: Two teams need to use the same VPC. How do you set it up?

- A network team owns the VPC in its own state (or account, with AWS RAM sharing subnets to other accounts)
- The VPC state exposes stable values through outputs, SSM parameters, or tags for data lookups
- App teams look up the VPC and subnets with data sources or a data-only module, and create only their own resources (security groups, load balancers, services)
- Changes to the shared VPC go through the network team's pull requests

App teams should never manage the VPC itself, to avoid two states owning the same object.

## 423: A consumer of your module gets "count value depends on resource attributes that cannot be determined until apply". How do you fix it in the module?

The module probably uses an input in `count` or `for_each`, and the caller passed an unknown value, like `create_dns = aws_route53_zone.x.id != ""`.

Fixes in the module:

- Use a separate boolean input (like `create_dns = true`) for the decision, which callers set from known values, and pass the ID in another variable
- Key `for_each` by names the caller knows, not by IDs
- Document which inputs must be known at plan time

This pattern of "flag plus value" inputs is common in well-designed public modules.

## 424: AWS services keep adding tags to your resources and every plan shows changes. What do you do?

Some services add their own tags, like AWS Backup, Elastic Beanstalk or cost tools. Options:

- Add `ignore_tags` with the keys or prefixes to the AWS provider, which ignores them for all resources
- Use `ignore_changes = [tags["key"]]` on specific resources
- Note that `tags_all` includes provider default tags, so look at both `tags` and `tags_all` in the plan to see what really changed

Ignoring by prefix in the provider is usually the cleanest solution.

## 425: You need to set up 100 new AWS accounts with the same baseline. How do you approach it?

- Create accounts through AWS Organizations, using Control Tower Account Factory for Terraform (AFT), an account vending module, or the `aws_organizations_account` resource
- Write a baseline module (IAM roles, logging, guardrails, budgets, default VPC cleanup)
- Apply the baseline per account with its own state, through a pipeline matrix, Terragrunt or Stacks deployments
- Use organization-level controls (SCPs, delegated admin services) for anything that should apply to all accounts at once instead of per-account Terraform
- Make account creation itself a pull request to a list of accounts

## 426: How would you design a Terraform platform for a company with many teams?

- **Modules:** a private registry with versioned, tested, secure-by-default modules owned by a platform team
- **Pipelines:** a standard pipeline template (fmt, validate, lint, scan, plan, policy, apply) that teams reuse
- **State:** remote, encrypted, one state per team and environment, with clear naming
- **Access:** OIDC roles per state, read-only for plans, approvals for production applies
- **Policies:** organization-wide policy checks with clear exceptions
- **Visibility:** drift detection, cost estimates on pull requests, dashboards of module versions in use
- **Docs and support:** examples, templates for new projects, office hours

The goal is that teams can ship infrastructure on their own, with guardrails instead of tickets.

## 427: Someone ran terraform destroy on production by mistake. How do you recover?

1. Stop further runs on that state
2. Find out what was deleted (the run output, CloudTrail)
3. Restore data first: database snapshots and point-in-time recovery, S3 versioning or backups, EBS snapshots. Resources with deletion protection may have survived.
4. Run `terraform apply` to recreate the infrastructure from code. Point databases at snapshots with `snapshot_identifier` where needed.
5. Fix DNS, secrets and anything not in Terraform

Afterwards: remove destroy permissions from people, require approval for destroy plans, add `prevent_destroy`, and test restore procedures regularly.

## 428: You need to rename a database, but the name forces replacement. How do you do it without data loss?

Terraform can't rename it in place if the API can't. Options:

- Check if the provider supports in-place rename for that resource (for example, RDS allows changing the identifier in place in many cases)
- Otherwise, create a new database from a snapshot or with replication, switch the app over, and remove the old one
- Or just don't rename it: the real name may not matter. Rename only the Terraform address with a `moved` block and keep the cloud name.

The last option is often the right answer: renaming the Terraform resource and renaming the cloud object are different things.

## 429: How would you bring thousands of existing DNS records under Terraform?

- Export records from the provider API (a script, or `terraform query` where list resources exist)
- Turn them into a data file (YAML or JSON) keyed by name and type
- Write one `for_each` resource that reads the data file, and `import` blocks with `for_each` built from the same data
- Plan until it shows only imports and no changes, then apply
- Split into states per zone if one state becomes too slow

After that, people change DNS by editing the data file in a pull request.

## 430: The plan keeps showing a list attribute reordered. What is going on?

The API probably returns the items in a different order than you wrote them, and the provider treats the attribute as an ordered list. Terraform sees a different order as a change.

Fixes:

- Sort the values in your code the same way the API returns them (often `sort()` helps for strings)
- Check if the provider has a newer version that treats it as a set
- Use `ignore_changes` on that attribute as a last resort

For policies, using `jsonencode` or `aws_iam_policy_document` often fixes order issues because the provider compares them semantically.

## 431: A random_password changed and caused a database password reset. Why?

`random_password` generates a new value when the resource is replaced. Replacement happens when its arguments change (like `length` or `special`), when one of its `keepers` changes, or when it's moved without a `moved` block.

```hcl
resource "random_password" "db" {
  length  = 24
  special = true
  keepers = {
    db_id = var.db_identifier
  }
}
```

Check the plan for `random_password` replacements before applying, and be careful with `keepers` that depend on values that can change. Ephemeral random passwords with write-only arguments avoid this problem.

## 432: Destroying a Kubernetes namespace with Terraform hangs. Why?

Kubernetes doesn't delete a namespace until everything inside it is deleted and all finalizers are cleared. If a resource inside has a finalizer whose controller is already gone (maybe Terraform deleted the controller earlier in the same run), the namespace stays in `Terminating` forever.

Fixes are to make sure controllers are destroyed after the resources they manage (with dependencies), clean up stuck objects manually, and avoid putting the controller and its custom resources in the same destroy without ordering.

## 433: Destroying a security group takes forever and fails. Why?

A security group can't be deleted while network interfaces still use it. Common causes are Lambda functions in a VPC (their ENIs are cleaned up slowly, sometimes after many minutes), load balancers, or resources created outside Terraform that use the group.

Fixes:

- Find the ENIs that use the group (`aws ec2 describe-network-interfaces --filters Name=group-id,Values=sg-...`)
- Wait for AWS to release Lambda ENIs, or detach them
- Use `create_before_destroy` and `name_prefix` on security groups so replacements don't block
- In some cases, the provider's `revoke_rules_on_delete` option helps with groups that reference each other

## 434: CI fails with "saved plan is stale". What happened and what do you do?

Something changed the state after the plan was created: another pipeline applied, someone ran `apply` or a state command, or the same pipeline ran twice.

Create a new plan and review it again, because the changes may be different now. To prevent it, queue runs per state (CI concurrency groups, Atlantis locks or HCP Terraform workspaces), and keep the time between plan and apply short.

## 435: Your team needs a feature that a community module doesn't support. What do you do?

Options, from best to worst usually:

1. Contribute the feature upstream and use it once released
2. Add the missing resource next to the module in your own code, using the module's outputs (composition)
3. Wrap the module in your own module that adds the extra resources
4. Fork the module and maintain the fork

Forks drift from upstream quickly, so they are a last resort. Composition often solves the problem without touching the module at all.

## 436: A developer wants to test infrastructure changes without breaking the shared dev environment. How?

- Give them a personal sandbox account or project with budget limits
- Let them use the same root module with a different backend key and a name prefix variable
- Use `terraform test` with mocks for logic changes
- Use short-lived pull request environments for app-level changes
- Clean up with automatic destroy jobs and account nuke tools for sandboxes

The shared dev environment should be changed through the normal pipeline like other environments.

## 437: Your rotation of the KMS key used by the state bucket went wrong and Terraform can't read state. What do you check?

- The Terraform role still has `kms:Decrypt` and `kms:GenerateDataKey` on the key (or the new key)
- Old state objects are still encrypted with the old key. If you switched keys, the old key must stay enabled until all objects are rewritten.
- The key policy wasn't changed in a way that blocks the role
- The key isn't scheduled for deletion or disabled

AWS KMS automatic rotation keeps old key material, so it doesn't break reads. Problems usually come from switching to a completely new key or editing key policies.

## 438: Replacing an IAM policy broke the app for a few minutes. Why, and how do you avoid it?

By default Terraform deletes the old resource before creating the new one. For a policy or attachment that forces replacement, there is a short time with no policy attached, and the app loses permissions. IAM eventual consistency can make that window longer.

Avoid it with `create_before_destroy = true` (and `name_prefix` so names don't clash), by making changes in place instead of replacing, or by adding the new permissions first in one apply and removing the old ones in a second apply.

## 439: Plans on laptops and in CI give different results. What do you check?

- The Terraform CLI version in both places
- The lock file is committed and both use it (no `init -upgrade` in one place)
- The same variable values: auto-loaded tfvars files or `TF_VAR_` environment variables on the laptop
- The same backend and workspace
- The same credentials and permissions (a data source may return different results based on access)
- Local override files that are ignored by Git

Running plans only in CI removes most of these differences.

## 440: You inherited a Terraform project with local state and secrets in tfvars files. What do you do first?

1. Back up the state file safely
2. Move the state to a remote backend with locking and encryption (`terraform init -migrate-state`)
3. Remove secrets from the repo, rotate them since they're in Git history, and load them from a secrets manager or CI secrets
4. Add a proper `.gitignore` and commit the lock file
5. Run a plan to see current drift before making any changes
6. Set up CI with plan on pull requests

Make no infrastructure changes until the basics are safe.

## 441: An auditor asks you to prove that all S3 buckets are encrypted. How do you answer with Terraform?

- Show the policy checks (OPA, Sentinel, Checkov) that fail any plan creating a bucket without encryption, and their run history
- Show the module code that enforces encryption by default
- Use `terraform show -json` across states to list buckets and their encryption settings
- Back it up with cloud-side evidence (AWS Config rules, Security Hub), because Terraform only knows about buckets it manages

Since 2023, S3 encrypts new objects by default, but auditors often want KMS keys and bucket policies, so check the actual requirement.

## 442: The cloud bill jumped after an apply. How do you find the cause?

- Look at the Terraform plan and Git diff of recent applies for new or bigger resources (instance sizes, counts, NAT gateways, storage classes, provisioned throughput)
- Check cost tools grouped by tag, which works well if your Terraform resources are tagged by project and state
- Look for resources stuck in loops (autoscaling with a wrong setting, log retention forever)

For the future, add Infracost to pull requests and set budget alerts per account.

## 443: What are the main limitations of Terraform?

- State must be stored and protected, and it can hold secrets
- No automatic rollback after failed applies
- Unknown values limit `count`, `for_each` and provider config
- HCL has no user-defined functions or recursion
- Provider configuration can't be dynamic (no `for_each`)
- Large states get slow
- Provider quality varies, and provider bugs become your bugs
- It's not a good fit for fast-changing app deploys or data

Most of these have workarounds, but they are worth knowing before you design a large setup.

## 444: When would you not choose Terraform?

- An AWS-only team that wants zero state management and automatic rollback might prefer CloudFormation or CDK
- A team that wants to write infrastructure in a general-purpose language with real unit tests might choose Pulumi
- Kubernetes-first teams with GitOps might prefer Crossplane or plain manifests with Argo CD
- If you need an open source license, OpenTofu is the direct alternative
- Very dynamic resources (per-user, per-request) are better handled by app code calling APIs

Terraform is the most common choice for multi-provider, long-lived infrastructure.

## 445: Where is Terraform heading?

Recent releases point in a few directions:

- **Less secret data in state:** ephemeral resources, write-only arguments
- **Better refactoring and import:** `moved`, `removed`, `import` with `for_each`, `terraform query` and list resources
- **Beyond CRUD:** actions for things like invoking functions or running operations
- **Many environments at scale:** Stacks with deployments and deferred changes
- **Testing:** `terraform test` with mocks

Following the changelog for each minor release is the best way to keep up, since many features land as experiments first.

## 446: How would you explain to a developer why Terraform needs state?

Terraform needs to know which real objects it created so it can update or delete them later. Many cloud resources have no reliable way to tag ownership, and searching every API on every run would be slow and incomplete.

State is that memory: the link between `aws_instance.web` in code and `i-0abc123` in AWS, plus the last known attributes and dependencies. Without it, Terraform couldn't tell a resource you removed from code (should be deleted) from one that was never managed (should be left alone).

## 447: What common Terraform mistakes do you see in real projects?

- State on laptops or in Git
- No version pinning, so a new provider release breaks plans
- One giant state for everything
- Copy-pasted code instead of modules, or the opposite: modules for every single resource
- Secrets in tfvars or code
- Using `count` with lists of named items
- Applying from laptops to production
- Ignoring plan output and applying with `-auto-approve` everywhere
- Manual console changes that never make it back to code

## 448: How do you decide when a plan is safe to auto-apply?

Auto-apply can be fine for low-risk changes if strong checks are in place:

- The environment is not production, or the change type is known to be safe
- No deletes or replacements in the plan (checked by script or policy)
- All policy and security checks pass
- The number of changes is below a limit
- The code was reviewed and merged

For production, many teams auto-apply only plans that create or update in place and require a human for anything that destroys or replaces.

## 449: How do you handle a Terraform change that needs a specific order across two applies?

Some changes can't be done safely in one apply, like moving traffic before deleting the old thing, or adding a new permission before removing the old one. Do it in steps:

1. First pull request: add the new resource or setting alongside the old one. Apply.
2. Switch usage (DNS, app config, references). Apply.
3. Last pull request: remove the old one. Apply.

Each step is a normal, reviewable plan. It takes longer but avoids downtime and makes rollback easy at each point.

## 450: You join a team with a messy Terraform codebase. What do you do in your first weeks?

1. Learn how it is run today: where state lives, who applies, which versions
2. Run plans for every root module and note drift and errors, without changing anything
3. Fix safety issues first: remote state with locking, secrets out of Git, version pins, a lock file, CI plans on pull requests
4. Write down the current layout and owners
5. Then improve step by step: split large states with `removed` and `import`, rename with `moved`, add modules where there's clear duplication, add tests and policy checks

Small, reviewed refactors with clean plans build trust. A big rewrite usually causes more problems than it solves.
