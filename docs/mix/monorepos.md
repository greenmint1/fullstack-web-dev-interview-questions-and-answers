# Monorepos Interview Questions and Answers

_Last updated: November 25, 2026_

This file has 450 interview questions and answers about monorepos: 150 easy, 150 moderate and 150 advanced. The answers target the tools people use today: npm, Yarn and pnpm workspaces (pnpm 10+), Turborepo 2.x, Nx 22+, Changesets and TypeScript project references. Code examples use JavaScript, Node.js and the usual JSON or YAML config files.

## Table of Contents

- [Easy Questions (1-150)](#easy-questions-1-150)
- [Moderate Questions (151-300)](#moderate-questions-151-300)
- [Advanced Questions (301-450)](#advanced-questions-301-450)

### Easy Questions (1-150)

- [1: What is a monorepo?](#1-what-is-a-monorepo)
- [2: What is a polyrepo?](#2-what-is-a-polyrepo)
- [3: Is a monorepo the same as a monolith?](#3-is-a-monorepo-the-same-as-a-monolith)
- [4: Why do teams use monorepos?](#4-why-do-teams-use-monorepos)
- [5: What are the main downsides of a monorepo?](#5-what-are-the-main-downsides-of-a-monorepo)
- [6: Which well-known companies use monorepos?](#6-which-well-known-companies-use-monorepos)
- [7: What is a workspace in a JavaScript monorepo?](#7-what-is-a-workspace-in-a-javascript-monorepo)
- [8: How do you set up npm workspaces?](#8-how-do-you-set-up-npm-workspaces)
- [9: How do you set up pnpm workspaces?](#9-how-do-you-set-up-pnpm-workspaces)
- [10: How do you set up Yarn workspaces?](#10-how-do-you-set-up-yarn-workspaces)
- [11: Why should the root package.json be private?](#11-why-should-the-root-packagejson-be-private)
- [12: What is a typical folder layout for a JavaScript monorepo?](#12-what-is-a-typical-folder-layout-for-a-javascript-monorepo)
- [13: What is the difference between an app and a package in a monorepo?](#13-what-is-the-difference-between-an-app-and-a-package-in-a-monorepo)
- [14: What does the workspace protocol mean in a dependency version?](#14-what-does-the-workspace-protocol-mean-in-a-dependency-version)
- [15: Does npm support the workspace protocol?](#15-does-npm-support-the-workspace-protocol)
- [16: How do you install a dependency into one workspace with npm?](#16-how-do-you-install-a-dependency-into-one-workspace-with-npm)
- [17: How do you install a dependency into one workspace with pnpm?](#17-how-do-you-install-a-dependency-into-one-workspace-with-pnpm)
- [18: How do you install a dependency at the root of a pnpm workspace?](#18-how-do-you-install-a-dependency-at-the-root-of-a-pnpm-workspace)
- [19: How do you run a script in every workspace with npm?](#19-how-do-you-run-a-script-in-every-workspace-with-npm)
- [20: How do you run a script in every workspace with pnpm?](#20-how-do-you-run-a-script-in-every-workspace-with-pnpm)
- [21: How do you run a script in one workspace with Yarn?](#21-how-do-you-run-a-script-in-one-workspace-with-yarn)
- [22: What is a single lockfile and why does it matter?](#22-what-is-a-single-lockfile-and-why-does-it-matter)
- [23: What is hoisting?](#23-what-is-hoisting)
- [24: What is a phantom dependency?](#24-what-is-a-phantom-dependency)
- [25: How does pnpm store packages?](#25-how-does-pnpm-store-packages)
- [26: What is a task runner in a monorepo?](#26-what-is-a-task-runner-in-a-monorepo)
- [27: What is Turborepo?](#27-what-is-turborepo)
- [28: What is Nx?](#28-what-is-nx)
- [29: What is Lerna?](#29-what-is-lerna)
- [30: What is Changesets?](#30-what-is-changesets)
- [31: What is a dependency graph in a monorepo?](#31-what-is-a-dependency-graph-in-a-monorepo)
- [32: What is a task graph?](#32-what-is-a-task-graph)
- [33: How do you see the dependency graph in Nx?](#33-how-do-you-see-the-dependency-graph-in-nx)
- [34: How do you see the task graph in Turborepo?](#34-how-do-you-see-the-task-graph-in-turborepo)
- [35: What does "affected" mean in a monorepo?](#35-what-does-affected-mean-in-a-monorepo)
- [36: How do you run tasks only for affected projects in Nx?](#36-how-do-you-run-tasks-only-for-affected-projects-in-nx)
- [37: How do you run tasks only for affected packages in Turborepo?](#37-how-do-you-run-tasks-only-for-affected-packages-in-turborepo)
- [38: What is task caching?](#38-what-is-task-caching)
- [39: What is a cache hit and a cache miss?](#39-what-is-a-cache-hit-and-a-cache-miss)
- [40: What is remote caching?](#40-what-is-remote-caching)
- [41: Where does Turborepo store its local cache?](#41-where-does-turborepo-store-its-local-cache)
- [42: Where does Nx store its local cache?](#42-where-does-nx-store-its-local-cache)
- [43: What does a basic turbo.json look like?](#43-what-does-a-basic-turbojson-look-like)
- [44: What does the caret mean in dependsOn, like "^build"?](#44-what-does-the-caret-mean-in-dependson-like-build)
- [45: What is the outputs key in turbo.json?](#45-what-is-the-outputs-key-in-turbojson)
- [46: Why should the dev task not be cached?](#46-why-should-the-dev-task-not-be-cached)
- [47: What was the pipeline key in turbo.json?](#47-what-was-the-pipeline-key-in-turbojson)
- [48: How do you run a task with Turborepo?](#48-how-do-you-run-a-task-with-turborepo)
- [49: How do you run a task for one package with Turborepo?](#49-how-do-you-run-a-task-for-one-package-with-turborepo)
- [50: How do you run a task for one project with Nx?](#50-how-do-you-run-a-task-for-one-project-with-nx)
- [51: How do you run a task for many projects with Nx?](#51-how-do-you-run-a-task-for-many-projects-with-nx)
- [52: What is nx.json?](#52-what-is-nxjson)
- [53: What is project.json in Nx?](#53-what-is-projectjson-in-nx)
- [54: What are inferred tasks in Nx?](#54-what-are-inferred-tasks-in-nx)
- [55: How do you create a new Nx workspace?](#55-how-do-you-create-a-new-nx-workspace)
- [56: How do you create a new Turborepo monorepo?](#56-how-do-you-create-a-new-turborepo-monorepo)
- [57: How do you add Turborepo to an existing workspace?](#57-how-do-you-add-turborepo-to-an-existing-workspace)
- [58: Should you install turbo globally or locally?](#58-should-you-install-turbo-globally-or-locally)
- [59: What is an internal package?](#59-what-is-an-internal-package)
- [60: What is a shared config package?](#60-what-is-a-shared-config-package)
- [61: How do you share a tsconfig across packages?](#61-how-do-you-share-a-tsconfig-across-packages)
- [62: How do you share an ESLint config across packages?](#62-how-do-you-share-an-eslint-config-across-packages)
- [63: Why do you scope package names like @acme/ui?](#63-why-do-you-scope-package-names-like-acmeui)
- [64: How does one app import a shared package?](#64-how-does-one-app-import-a-shared-package)
- [65: What is the exports field in package.json?](#65-what-is-the-exports-field-in-packagejson)
- [66: Why do monorepo tools need to know the order of builds?](#66-why-do-monorepo-tools-need-to-know-the-order-of-builds)
- [67: What is a root script in a monorepo?](#67-what-is-a-root-script-in-a-monorepo)
- [68: What is the difference between dependencies and devDependencies in a workspace package?](#68-what-is-the-difference-between-dependencies-and-devdependencies-in-a-workspace-package)
- [69: What is a peer dependency and why does it matter in monorepos?](#69-what-is-a-peer-dependency-and-why-does-it-matter-in-monorepos)
- [70: Why is having two copies of React in a monorepo a problem?](#70-why-is-having-two-copies-of-react-in-a-monorepo-a-problem)
- [71: What does "single version policy" mean?](#71-what-does-single-version-policy-mean)
- [72: What are pnpm catalogs?](#72-what-are-pnpm-catalogs)
- [73: What is a CODEOWNERS file?](#73-what-is-a-codeowners-file)
- [74: How does a monorepo help with atomic changes?](#74-how-does-a-monorepo-help-with-atomic-changes)
- [75: What is trunk-based development and why is it common with monorepos?](#75-what-is-trunk-based-development-and-why-is-it-common-with-monorepos)
- [76: What does the .gitignore of a JavaScript monorepo usually include?](#76-what-does-the-gitignore-of-a-javascript-monorepo-usually-include)
- [77: What is the difference between a monorepo tool and a package manager?](#77-what-is-the-difference-between-a-monorepo-tool-and-a-package-manager)
- [78: Can you have a monorepo without any special tool?](#78-can-you-have-a-monorepo-without-any-special-tool)
- [79: How do you list all workspaces with pnpm?](#79-how-do-you-list-all-workspaces-with-pnpm)
- [80: How do you list all projects in Nx?](#80-how-do-you-list-all-projects-in-nx)
- [81: How does a pnpm filter work?](#81-how-does-a-pnpm-filter-work)
- [82: What does pnpm --filter web... do?](#82-what-does-pnpm---filter-web-do)
- [83: What is a dependent in a monorepo?](#83-what-is-a-dependent-in-a-monorepo)
- [84: What is the difference between direct and transitive dependencies here?](#84-what-is-the-difference-between-direct-and-transitive-dependencies-here)
- [85: What does the Turborepo log prefix mean, like "web:build:"?](#85-what-does-the-turborepo-log-prefix-mean-like-webbuild)
- [86: What is the Turborepo terminal UI?](#86-what-is-the-turborepo-terminal-ui)
- [87: How do you force a task to run without the cache in Turborepo?](#87-how-do-you-force-a-task-to-run-without-the-cache-in-turborepo)
- [88: How do you skip the cache in Nx?](#88-how-do-you-skip-the-cache-in-nx)
- [89: What is the Nx daemon?](#89-what-is-the-nx-daemon)
- [90: What is a generator in Nx?](#90-what-is-a-generator-in-nx)
- [91: What is an executor in Nx?](#91-what-is-an-executor-in-nx)
- [92: What is nx:run-commands?](#92-what-is-nxrun-commands)
- [93: What are tags in Nx?](#93-what-are-tags-in-nx)
- [94: What are module boundaries?](#94-what-are-module-boundaries)
- [95: How do you check module boundaries in Nx?](#95-how-do-you-check-module-boundaries-in-nx)
- [96: What is semantic versioning?](#96-what-is-semantic-versioning)
- [97: What is the difference between fixed and independent versioning?](#97-what-is-the-difference-between-fixed-and-independent-versioning)
- [98: How do you add a changeset?](#98-how-do-you-add-a-changeset)
- [99: What does a changeset file look like?](#99-what-does-a-changeset-file-look-like)
- [100: How do you set up Changesets in a repo?](#100-how-do-you-set-up-changesets-in-a-repo)
- [101: What does changeset version do?](#101-what-does-changeset-version-do)
- [102: What does changeset publish do?](#102-what-does-changeset-publish-do)
- [103: What is the Changesets GitHub Action?](#103-what-is-the-changesets-github-action)
- [104: What is a monorepo "package" in Nx terms versus a "project"?](#104-what-is-a-monorepo-package-in-nx-terms-versus-a-project)
- [105: What is a package-based monorepo versus an integrated monorepo in Nx?](#105-what-is-a-package-based-monorepo-versus-an-integrated-monorepo-in-nx)
- [106: Why do some monorepos use a single root package.json for all dependencies?](#106-why-do-some-monorepos-use-a-single-root-packagejson-for-all-dependencies)
- [107: What does "build once, deploy many" mean in a monorepo?](#107-what-does-build-once-deploy-many-mean-in-a-monorepo)
- [108: How does a monorepo affect code reviews?](#108-how-does-a-monorepo-affect-code-reviews)
- [109: What is the biggest CI problem in a growing monorepo?](#109-what-is-the-biggest-ci-problem-in-a-growing-monorepo)
- [110: How do you speed up npm install in a big monorepo?](#110-how-do-you-speed-up-npm-install-in-a-big-monorepo)
- [111: What does pnpm install --frozen-lockfile do?](#111-what-does-pnpm-install---frozen-lockfile-do)
- [112: How do you add a new package to a pnpm monorepo?](#112-how-do-you-add-a-new-package-to-a-pnpm-monorepo)
- [113: How do you remove a package from a monorepo safely?](#113-how-do-you-remove-a-package-from-a-monorepo-safely)
- [114: What does pnpm why do?](#114-what-does-pnpm-why-do)
- [115: What is a root tsconfig.json used for in a monorepo?](#115-what-is-a-root-tsconfigjson-used-for-in-a-monorepo)
- [116: What are TypeScript project references?](#116-what-are-typescript-project-references)
- [117: What does composite: true do?](#117-what-does-composite-true-do)
- [118: What are TypeScript path aliases and how are they used in monorepos?](#118-what-are-typescript-path-aliases-and-how-are-they-used-in-monorepos)
- [119: What is a "just-in-time" or source-only internal package?](#119-what-is-a-just-in-time-or-source-only-internal-package)
- [120: What is a compiled internal package?](#120-what-is-a-compiled-internal-package)
- [121: What is a publishable package?](#121-what-is-a-publishable-package)
- [122: How does a monorepo affect onboarding?](#122-how-does-a-monorepo-affect-onboarding)
- [123: Can different apps in a monorepo use different frameworks?](#123-can-different-apps-in-a-monorepo-use-different-frameworks)
- [124: Can a monorepo hold code in several languages?](#124-can-a-monorepo-hold-code-in-several-languages)
- [125: What is Bazel?](#125-what-is-bazel)
- [126: What is Rush?](#126-what-is-rush)
- [127: What is moon?](#127-what-is-moon)
- [128: How do you pick between Turborepo and Nx?](#128-how-do-you-pick-between-turborepo-and-nx)
- [129: What is a "Version Packages" pull request?](#129-what-is-a-version-packages-pull-request)
- [130: What is a monorepo's "main" or "trunk" branch?](#130-what-is-a-monorepos-main-or-trunk-branch)
- [131: What is a merge queue?](#131-what-is-a-merge-queue)
- [132: How does a monorepo make dependency upgrades easier?](#132-how-does-a-monorepo-make-dependency-upgrades-easier)
- [133: How does a monorepo make dependency upgrades harder?](#133-how-does-a-monorepo-make-dependency-upgrades-harder)
- [134: What is Renovate or Dependabot used for in a monorepo?](#134-what-is-renovate-or-dependabot-used-for-in-a-monorepo)
- [135: What is npx turbo prune used for?](#135-what-is-npx-turbo-prune-used-for)
- [136: How does Nx help build a Docker image for one app?](#136-how-does-nx-help-build-a-docker-image-for-one-app)
- [137: Why shouldn't each app commit its own lockfile in a workspace?](#137-why-shouldnt-each-app-commit-its-own-lockfile-in-a-workspace)
- [138: What is a .npmrc used for in a pnpm monorepo?](#138-what-is-a-npmrc-used-for-in-a-pnpm-monorepo)
- [139: What is the files field in package.json?](#139-what-is-the-files-field-in-packagejson)
- [140: Can a monorepo have both public and private packages?](#140-can-a-monorepo-have-both-public-and-private-packages)
- [141: What is a scoped npm registry setting?](#141-what-is-a-scoped-npm-registry-setting)
- [142: What is Verdaccio and why would you use it with a monorepo?](#142-what-is-verdaccio-and-why-would-you-use-it-with-a-monorepo)
- [143: What is pnpm dlx or npx?](#143-what-is-pnpm-dlx-or-npx)
- [144: Why is a consistent Node version important across a monorepo?](#144-why-is-a-consistent-node-version-important-across-a-monorepo)
- [145: What is the packageManager field?](#145-what-is-the-packagemanager-field)
- [146: What is Corepack?](#146-what-is-corepack)
- [147: How do you run a dev server for one app and its packages with Turborepo?](#147-how-do-you-run-a-dev-server-for-one-app-and-its-packages-with-turborepo)
- [148: What is turbo watch?](#148-what-is-turbo-watch)
- [149: Why might a cached build in CI not match a local build?](#149-why-might-a-cached-build-in-ci-not-match-a-local-build)
- [150: What should a README at the root of a monorepo cover?](#150-what-should-a-readme-at-the-root-of-a-monorepo-cover)

### Moderate Questions (151-300)

- [151: What goes into a Turborepo task hash?](#151-what-goes-into-a-turborepo-task-hash)
- [152: What does the inputs key do in turbo.json?](#152-what-does-the-inputs-key-do-in-turbojson)
- [153: What does the env key do in turbo.json?](#153-what-does-the-env-key-do-in-turbojson)
- [154: What is strict environment mode in Turborepo?](#154-what-is-strict-environment-mode-in-turborepo)
- [155: What is the difference between env and passThroughEnv?](#155-what-is-the-difference-between-env-and-passthroughenv)
- [156: What are globalDependencies and globalEnv?](#156-what-are-globaldependencies-and-globalenv)
- [157: How do you configure a task differently for one package in Turborepo?](#157-how-do-you-configure-a-task-differently-for-one-package-in-turborepo)
- [158: How do you define a task that only runs in one specific package?](#158-how-do-you-define-a-task-that-only-runs-in-one-specific-package)
- [159: What are root tasks in Turborepo?](#159-what-are-root-tasks-in-turborepo)
- [160: How do you see what Turborepo would run without running it?](#160-how-do-you-see-what-turborepo-would-run-without-running-it)
- [161: How do you debug a Turborepo cache miss?](#161-how-do-you-debug-a-turborepo-cache-miss)
- [162: How do you filter Turborepo tasks by changed files?](#162-how-do-you-filter-turborepo-tasks-by-changed-files)
- [163: What do the different filter forms in Turborepo mean?](#163-what-do-the-different-filter-forms-in-turborepo-mean)
- [164: What does --continue do in Turborepo?](#164-what-does---continue-do-in-turborepo)
- [165: How do you limit parallel tasks in Turborepo?](#165-how-do-you-limit-parallel-tasks-in-turborepo)
- [166: How do you set up Vercel Remote Cache for Turborepo?](#166-how-do-you-set-up-vercel-remote-cache-for-turborepo)
- [167: Can you self-host a Turborepo remote cache?](#167-can-you-self-host-a-turborepo-remote-cache)
- [168: How do you make sure remote cache artifacts can't be tampered with in Turborepo?](#168-how-do-you-make-sure-remote-cache-artifacts-cant-be-tampered-with-in-turborepo)
- [169: What are namedInputs in Nx?](#169-what-are-namedinputs-in-nx)
- [170: Why do Nx workspaces often have a "production" named input?](#170-why-do-nx-workspaces-often-have-a-production-named-input)
- [171: What do {projectRoot} and {workspaceRoot} mean in Nx config?](#171-what-do-projectroot-and-workspaceroot-mean-in-nx-config)
- [172: What are targetDefaults in Nx?](#172-what-are-targetdefaults-in-nx)
- [173: How does Nx merge task config from different places?](#173-how-does-nx-merge-task-config-from-different-places)
- [174: How do you add Nx settings in package.json instead of project.json?](#174-how-do-you-add-nx-settings-in-packagejson-instead-of-projectjson)
- [175: How do you set the base for nx affected in CI?](#175-how-do-you-set-the-base-for-nx-affected-in-ci)
- [176: Why does nx affected need full Git history in CI?](#176-why-does-nx-affected-need-full-git-history-in-ci)
- [177: How do you connect an Nx workspace to Nx Cloud?](#177-how-do-you-connect-an-nx-workspace-to-nx-cloud)
- [178: What is nx migrate?](#178-what-is-nx-migrate)
- [179: What is nx sync?](#179-what-is-nx-sync)
- [180: What is nx release?](#180-what-is-nx-release)
- [181: How do you run a pnpm command for packages changed since main?](#181-how-do-you-run-a-pnpm-command-for-packages-changed-since-main)
- [182: What does pnpm --filter "...^web" mean?](#182-what-does-pnpm---filter-web-mean)
- [183: What is pnpm deploy?](#183-what-is-pnpm-deploy)
- [184: How do you publish all changed packages with pnpm?](#184-how-do-you-publish-all-changed-packages-with-pnpm)
- [185: What is the difference between workspace:*, workspace:^ and workspace:~?](#185-what-is-the-difference-between-workspace-workspace-and-workspace)
- [186: What are pnpm overrides?](#186-what-are-pnpm-overrides)
- [187: What are named catalogs in pnpm?](#187-what-are-named-catalogs-in-pnpm)
- [188: What is the catalogMode setting in pnpm?](#188-what-is-the-catalogmode-setting-in-pnpm)
- [189: What are Yarn constraints?](#189-what-are-yarn-constraints)
- [190: What is Yarn Plug'n'Play and how does it affect monorepos?](#190-what-is-yarn-plugnplay-and-how-does-it-affect-monorepos)
- [191: What does nodeLinker do in pnpm?](#191-what-does-nodelinker-do-in-pnpm)
- [192: What do shamefully-hoist and public-hoist-pattern do in pnpm?](#192-what-do-shamefully-hoist-and-public-hoist-pattern-do-in-pnpm)
- [193: How do you check that all packages use the same dependency versions?](#193-how-do-you-check-that-all-packages-use-the-same-dependency-versions)
- [194: What is syncpack?](#194-what-is-syncpack)
- [195: How do you run Jest across a monorepo?](#195-how-do-you-run-jest-across-a-monorepo)
- [196: How do you run Vitest across a monorepo?](#196-how-do-you-run-vitest-across-a-monorepo)
- [197: How does Next.js use a workspace package that ships TypeScript source?](#197-how-does-nextjs-use-a-workspace-package-that-ships-typescript-source)
- [198: How does Vite handle workspace packages?](#198-how-does-vite-handle-workspace-packages)
- [199: How do you handle environment variables in a monorepo?](#199-how-do-you-handle-environment-variables-in-a-monorepo)
- [200: How do you share validated env config between apps?](#200-how-do-you-share-validated-env-config-between-apps)
- [201: How do you set up a GitHub Actions workflow for a Turborepo monorepo?](#201-how-do-you-set-up-a-github-actions-workflow-for-a-turborepo-monorepo)
- [202: How do you set up a GitHub Actions workflow for an Nx monorepo?](#202-how-do-you-set-up-a-github-actions-workflow-for-an-nx-monorepo)
- [203: Without a remote cache, how can you cache Turborepo results in GitHub Actions?](#203-without-a-remote-cache-how-can-you-cache-turborepo-results-in-github-actions)
- [204: How do you build a Docker image for one app with turbo prune?](#204-how-do-you-build-a-docker-image-for-one-app-with-turbo-prune)
- [205: Why do you copy package.json files before source code in a Dockerfile?](#205-why-do-you-copy-packagejson-files-before-source-code-in-a-dockerfile)
- [206: What does Changesets config.json look like?](#206-what-does-changesets-configjson-look-like)
- [207: What do fixed and linked mean in Changesets?](#207-what-do-fixed-and-linked-mean-in-changesets)
- [208: What does updateInternalDependencies do in Changesets?](#208-what-does-updateinternaldependencies-do-in-changesets)
- [209: How do you make prereleases with Changesets?](#209-how-do-you-make-prereleases-with-changesets)
- [210: What are snapshot releases in Changesets?](#210-what-are-snapshot-releases-in-changesets)
- [211: How does Lerna version packages?](#211-how-does-lerna-version-packages)
- [212: What are conventional commits and how do release tools use them?](#212-what-are-conventional-commits-and-how-do-release-tools-use-them)
- [213: How do you enforce conventional commit messages in a monorepo?](#213-how-do-you-enforce-conventional-commit-messages-in-a-monorepo)
- [214: How do you run lint only on staged files in a monorepo?](#214-how-do-you-run-lint-only-on-staged-files-in-a-monorepo)
- [215: How do you run ESLint across a monorepo efficiently?](#215-how-do-you-run-eslint-across-a-monorepo-efficiently)
- [216: Should each package have its own ESLint config file?](#216-should-each-package-have-its-own-eslint-config-file)
- [217: How do you type-check a whole monorepo with TypeScript project references?](#217-how-do-you-type-check-a-whole-monorepo-with-typescript-project-references)
- [218: Why does tsc -b need references to match package dependencies?](#218-why-does-tsc--b-need-references-to-match-package-dependencies)
- [219: How do you make editors jump to source instead of .d.ts files in a monorepo?](#219-how-do-you-make-editors-jump-to-source-instead-of-dts-files-in-a-monorepo)
- [220: What are custom export conditions and how do they help in monorepos?](#220-what-are-custom-export-conditions-and-how-do-they-help-in-monorepos)
- [221: How do you build a library package with tsup?](#221-how-do-you-build-a-library-package-with-tsup)
- [222: How do you share React components between two apps?](#222-how-do-you-share-react-components-between-two-apps)
- [223: How do you share styles like Tailwind CSS between packages?](#223-how-do-you-share-styles-like-tailwind-css-between-packages)
- [224: How do you share TypeScript types between frontend and backend?](#224-how-do-you-share-typescript-types-between-frontend-and-backend)
- [225: How do you set up Storybook in a monorepo?](#225-how-do-you-set-up-storybook-in-a-monorepo)
- [226: How do you share test helpers across packages?](#226-how-do-you-share-test-helpers-across-packages)
- [227: How do you share a database schema or ORM client between services?](#227-how-do-you-share-a-database-schema-or-orm-client-between-services)
- [228: How do you make a generate task run before build in Turborepo?](#228-how-do-you-make-a-generate-task-run-before-build-in-turborepo)
- [229: How do you handle circular dependencies between packages?](#229-how-do-you-handle-circular-dependencies-between-packages)
- [230: How do you find circular imports in Nx?](#230-how-do-you-find-circular-imports-in-nx)
- [231: What does nx show project web --web do?](#231-what-does-nx-show-project-web---web-do)
- [232: How do Nx plugins infer targets?](#232-how-do-nx-plugins-infer-targets)
- [233: How do you exclude some projects from an Nx plugin?](#233-how-do-you-exclude-some-projects-from-an-nx-plugin)
- [234: How do you run tasks for projects with a certain tag in Nx?](#234-how-do-you-run-tasks-for-projects-with-a-certain-tag-in-nx)
- [235: How do Nx tags map to an architecture?](#235-how-do-nx-tags-map-to-an-architecture)
- [236: Can you enforce module boundaries without Nx?](#236-can-you-enforce-module-boundaries-without-nx)
- [237: What is turbo boundaries?](#237-what-is-turbo-boundaries)
- [238: How do you migrate an existing repo into a monorepo without losing Git history?](#238-how-do-you-migrate-an-existing-repo-into-a-monorepo-without-losing-git-history)
- [239: What is nx import?](#239-what-is-nx-import)
- [240: How do you split a package out of a monorepo into its own repo?](#240-how-do-you-split-a-package-out-of-a-monorepo-into-its-own-repo)
- [241: What is Git sparse checkout?](#241-what-is-git-sparse-checkout)
- [242: What is a partial clone?](#242-what-is-a-partial-clone)
- [243: How do you keep VS Code fast in a big monorepo?](#243-how-do-you-keep-vs-code-fast-in-a-big-monorepo)
- [244: What is a multi-root workspace in VS Code?](#244-what-is-a-multi-root-workspace-in-vs-code)
- [245: How do you run e2e tests in a monorepo?](#245-how-do-you-run-e2e-tests-in-a-monorepo)
- [246: What are implicitDependencies in Nx?](#246-what-are-implicitdependencies-in-nx)
- [247: How do you make a non-JavaScript file affect a task's cache?](#247-how-do-you-make-a-non-javascript-file-affect-a-tasks-cache)
- [248: How do you make a task depend on a tool version in Nx?](#248-how-do-you-make-a-task-depend-on-a-tool-version-in-nx)
- [249: What are externalDependencies inputs in Nx?](#249-what-are-externaldependencies-inputs-in-nx)
- [250: What does dependentTasksOutputFiles do in Nx?](#250-what-does-dependenttasksoutputfiles-do-in-nx)
- [251: How do you debug why a project is affected in Nx?](#251-how-do-you-debug-why-a-project-is-affected-in-nx)
- [252: Why does changing the lockfile sometimes mark everything as affected?](#252-why-does-changing-the-lockfile-sometimes-mark-everything-as-affected)
- [253: How do you avoid one global config file busting all caches?](#253-how-do-you-avoid-one-global-config-file-busting-all-caches)
- [254: How do you handle a package that needs different build outputs for different apps?](#254-how-do-you-handle-a-package-that-needs-different-build-outputs-for-different-apps)
- [255: What is the problem with relative imports across packages?](#255-what-is-the-problem-with-relative-imports-across-packages)
- [256: How do you prevent deep imports into another package's internals?](#256-how-do-you-prevent-deep-imports-into-another-packages-internals)
- [257: How do you version an internal package that's never published?](#257-how-do-you-version-an-internal-package-thats-never-published)
- [258: How does a monorepo deploy only the apps that changed?](#258-how-does-a-monorepo-deploy-only-the-apps-that-changed)
- [259: What is turbo-ignore?](#259-what-is-turbo-ignore)
- [260: How do you deploy several apps from one monorepo on Vercel?](#260-how-do-you-deploy-several-apps-from-one-monorepo-on-vercel)
- [261: How do you deploy a Node.js service from a monorepo to a container platform?](#261-how-do-you-deploy-a-nodejs-service-from-a-monorepo-to-a-container-platform)
- [262: Why bundle a Node.js service with esbuild in a monorepo?](#262-why-bundle-a-nodejs-service-with-esbuild-in-a-monorepo)
- [263: How do you handle native modules in a monorepo Docker image?](#263-how-do-you-handle-native-modules-in-a-monorepo-docker-image)
- [264: What is the difference between npm ci and npm install in a workspace?](#264-what-is-the-difference-between-npm-ci-and-npm-install-in-a-workspace)
- [265: How do you install only one workspace's dependencies in CI?](#265-how-do-you-install-only-one-workspaces-dependencies-in-ci)
- [266: What is the root node_modules/.bin and how do workspace scripts find binaries?](#266-what-is-the-root-node_modulesbin-and-how-do-workspace-scripts-find-binaries)
- [267: Should shared dev tools be installed at the root or in each package?](#267-should-shared-dev-tools-be-installed-at-the-root-or-in-each-package)
- [268: How do you give each package its own scripts but keep them consistent?](#268-how-do-you-give-each-package-its-own-scripts-but-keep-them-consistent)
- [269: What is a typecheck task and why separate it from build?](#269-what-is-a-typecheck-task-and-why-separate-it-from-build)
- [270: How do you speed up TypeScript checks in a monorepo?](#270-how-do-you-speed-up-typescript-checks-in-a-monorepo)
- [271: How do you share a Prettier config in a monorepo?](#271-how-do-you-share-a-prettier-config-in-a-monorepo)
- [272: What are the trade-offs of fixed versioning for published packages?](#272-what-are-the-trade-offs-of-fixed-versioning-for-published-packages)
- [273: How do you test a published package before releasing it from a monorepo?](#273-how-do-you-test-a-published-package-before-releasing-it-from-a-monorepo)
- [274: What is publint?](#274-what-is-publint)
- [275: How do you handle breaking changes to a shared library used by many apps?](#275-how-do-you-handle-breaking-changes-to-a-shared-library-used-by-many-apps)
- [276: What is a feature flag and why is it common in monorepos?](#276-what-is-a-feature-flag-and-why-is-it-common-in-monorepos)
- [277: How do you keep main green in a busy monorepo?](#277-how-do-you-keep-main-green-in-a-busy-monorepo)
- [278: What is the role of a platform or developer experience team in a monorepo?](#278-what-is-the-role-of-a-platform-or-developer-experience-team-in-a-monorepo)
- [279: How do you add a new app to an Nx workspace?](#279-how-do-you-add-a-new-app-to-an-nx-workspace)
- [280: How do you write a local Nx generator?](#280-how-do-you-write-a-local-nx-generator)
- [281: What is Turborepo's code generation feature?](#281-what-is-turborepos-code-generation-feature)
- [282: How do you rename or move a project in Nx?](#282-how-do-you-rename-or-move-a-project-in-nx)
- [283: How do you remove a project in Nx?](#283-how-do-you-remove-a-project-in-nx)
- [284: What happens when two packages have the same name?](#284-what-happens-when-two-packages-have-the-same-name)
- [285: What if a package has no name in package.json?](#285-what-if-a-package-has-no-name-in-packagejson)
- [286: How do you run a one-off script across all packages?](#286-how-do-you-run-a-one-off-script-across-all-packages)
- [287: What is the order in which pnpm -r runs scripts?](#287-what-is-the-order-in-which-pnpm--r-runs-scripts)
- [288: Why might you still want Turborepo or Nx if pnpm -r already sorts packages?](#288-why-might-you-still-want-turborepo-or-nx-if-pnpm--r-already-sorts-packages)
- [289: What is the Nx terminal UI?](#289-what-is-the-nx-terminal-ui)
- [290: What is continuous tasks in Nx?](#290-what-is-continuous-tasks-in-nx)
- [291: How does Turborepo handle a task that depends on a persistent task?](#291-how-does-turborepo-handle-a-task-that-depends-on-a-persistent-task)
- [292: What does the interruptible option do in Turborepo?](#292-what-does-the-interruptible-option-do-in-turborepo)
- [293: How do you pass arguments to the underlying script with Turborepo?](#293-how-do-you-pass-arguments-to-the-underlying-script-with-turborepo)
- [294: How do you pass arguments to a task with Nx?](#294-how-do-you-pass-arguments-to-a-task-with-nx)
- [295: What are configurations in an Nx target?](#295-what-are-configurations-in-an-nx-target)
- [296: What is the parallel option in Nx?](#296-what-is-the-parallel-option-in-nx)
- [297: How do you exclude a project from Nx without removing it?](#297-how-do-you-exclude-a-project-from-nx-without-removing-it)
- [298: How do you make sure a task never runs from cache in Nx?](#298-how-do-you-make-sure-a-task-never-runs-from-cache-in-nx)
- [299: Why shouldn't you cache deploy tasks?](#299-why-shouldnt-you-cache-deploy-tasks)
- [300: How do you run a task after every other task in Turborepo?](#300-how-do-you-run-a-task-after-every-other-task-in-turborepo)

### Advanced Questions (301-450)

- [301: How would you decide between a monorepo and a polyrepo for a company?](#301-how-would-you-decide-between-a-monorepo-and-a-polyrepo-for-a-company)
- [302: What does "hermetic build" mean?](#302-what-does-hermetic-build-mean)
- [303: Why are Turborepo and Nx not fully hermetic?](#303-why-are-turborepo-and-nx-not-fully-hermetic)
- [304: What can go wrong if a task reads an undeclared input?](#304-what-can-go-wrong-if-a-task-reads-an-undeclared-input)
- [305: How does Bazel enforce hermeticity?](#305-how-does-bazel-enforce-hermeticity)
- [306: What is remote execution?](#306-what-is-remote-execution)
- [307: What is distributed task execution in Nx?](#307-what-is-distributed-task-execution-in-nx)
- [308: How would you split CI work across machines without Nx Agents?](#308-how-would-you-split-ci-work-across-machines-without-nx-agents)
- [309: What is the problem with naive sharding by package count?](#309-what-is-the-problem-with-naive-sharding-by-package-count)
- [310: How does Turborepo hash files quickly?](#310-how-does-turborepo-hash-files-quickly)
- [311: How does Nx compute the project graph and keep it fast?](#311-how-does-nx-compute-the-project-graph-and-keep-it-fast)
- [312: Why can a slow Nx plugin make every command slow?](#312-why-can-a-slow-nx-plugin-make-every-command-slow)
- [313: How would you profile a slow Turborepo run?](#313-how-would-you-profile-a-slow-turborepo-run)
- [314: What is the critical path of a task graph?](#314-what-is-the-critical-path-of-a-task-graph)
- [315: When should a test task not depend on ^build?](#315-when-should-a-test-task-not-depend-on-build)
- [316: What is the transit node pattern in Turborepo?](#316-what-is-the-transit-node-pattern-in-turborepo)
- [317: Why can parallel tasks without dependsOn still give wrong cache results?](#317-why-can-parallel-tasks-without-dependson-still-give-wrong-cache-results)
- [318: How does Nx include dependencies in a task's hash?](#318-how-does-nx-include-dependencies-in-a-tasks-hash)
- [319: What makes a build non-deterministic and how does it hurt caching?](#319-what-makes-a-build-non-deterministic-and-how-does-it-hurt-caching)
- [320: How do absolute paths break cache sharing between machines?](#320-how-do-absolute-paths-break-cache-sharing-between-machines)
- [321: What is cache poisoning in a remote cache?](#321-what-is-cache-poisoning-in-a-remote-cache)
- [322: How do you protect a remote cache from poisoning?](#322-how-do-you-protect-a-remote-cache-from-poisoning)
- [323: How do you give developers read-only access to the Turborepo remote cache?](#323-how-do-you-give-developers-read-only-access-to-the-turborepo-remote-cache)
- [324: What are the risks of running CI for pull requests from forks with a remote cache?](#324-what-are-the-risks-of-running-ci-for-pull-requests-from-forks-with-a-remote-cache)
- [325: Can secrets end up in the cache?](#325-can-secrets-end-up-in-the-cache)
- [326: How do you design env var handling so caching stays correct and safe?](#326-how-do-you-design-env-var-handling-so-caching-stays-correct-and-safe)
- [327: What is the downside of putting NEXT_PUBLIC_* style vars in the hash?](#327-what-is-the-downside-of-putting-next_public_-style-vars-in-the-hash)
- [328: How does pnpm 10 handle dependency lifecycle scripts, and why does it matter in a monorepo?](#328-how-does-pnpm-10-handle-dependency-lifecycle-scripts-and-why-does-it-matter-in-a-monorepo)
- [329: What is minimumReleaseAge in pnpm and why use it?](#329-what-is-minimumreleaseage-in-pnpm-and-why-use-it)
- [330: How would you limit the blast radius of a compromised npm package in a monorepo?](#330-how-would-you-limit-the-blast-radius-of-a-compromised-npm-package-in-a-monorepo)
- [331: What is npm trusted publishing and why does it fit monorepo releases?](#331-what-is-npm-trusted-publishing-and-why-does-it-fit-monorepo-releases)
- [332: How do you scale CODEOWNERS in a very large monorepo?](#332-how-do-you-scale-codeowners-in-a-very-large-monorepo)
- [333: How do you handle access control when some code must be private to one team?](#333-how-do-you-handle-access-control-when-some-code-must-be-private-to-one-team)
- [334: How do you handle a monorepo where one app must be open source and the rest private?](#334-how-do-you-handle-a-monorepo-where-one-app-must-be-open-source-and-the-rest-private)
- [335: How do you scale Git for a monorepo with millions of files?](#335-how-do-you-scale-git-for-a-monorepo-with-millions-of-files)
- [336: What does git maintenance do?](#336-what-does-git-maintenance-do)
- [337: Why is git status slow in big repos and how do you fix it?](#337-why-is-git-status-slow-in-big-repos-and-how-do-you-fix-it)
- [338: How do you handle large binary files in a monorepo?](#338-how-do-you-handle-large-binary-files-in-a-monorepo)
- [339: How do lockfile merge conflicts happen and how do you resolve them?](#339-how-do-lockfile-merge-conflicts-happen-and-how-do-you-resolve-them)
- [340: Why do lockfile changes cause so many conflicts in big monorepos and how do you reduce them?](#340-why-do-lockfile-changes-cause-so-many-conflicts-in-big-monorepos-and-how-do-you-reduce-them)
- [341: How do you handle two apps that need different major versions of the same library?](#341-how-do-you-handle-two-apps-that-need-different-major-versions-of-the-same-library)
- [342: What happens with peer dependencies when a shared package is used by apps on different React versions?](#342-what-happens-with-peer-dependencies-when-a-shared-package-is-used-by-apps-on-different-react-versions)
- [343: What is pnpm's injected dependencies feature?](#343-what-is-pnpms-injected-dependencies-feature)
- [344: How does a single version policy affect very large teams?](#344-how-does-a-single-version-policy-affect-very-large-teams)
- [345: How would you upgrade a major dependency like React across 40 apps?](#345-how-would-you-upgrade-a-major-dependency-like-react-across-40-apps)
- [346: What is a codemod and why do monorepos use them a lot?](#346-what-is-a-codemod-and-why-do-monorepos-use-them-a-lot)
- [347: Write a small codemod that renames an imported function across the repo.](#347-write-a-small-codemod-that-renames-an-imported-function-across-the-repo)
- [348: How do you measure the health of a monorepo over time?](#348-how-do-you-measure-the-health-of-a-monorepo-over-time)
- [349: What is a "god package" and why is it a problem?](#349-what-is-a-god-package-and-why-is-it-a-problem)
- [350: How do you split a large shared package without breaking everyone?](#350-how-do-you-split-a-large-shared-package-without-breaking-everyone)
- [351: How do you design the package structure for a large product monorepo?](#351-how-do-you-design-the-package-structure-for-a-large-product-monorepo)
- [352: How small should packages be?](#352-how-small-should-packages-be)
- [353: What is the cost of having too many tiny packages?](#353-what-is-the-cost-of-having-too-many-tiny-packages)
- [354: How do you handle code that two business areas both need but neither owns?](#354-how-do-you-handle-code-that-two-business-areas-both-need-but-neither-owns)
- [355: How would you migrate five separate repos into one monorepo?](#355-how-would-you-migrate-five-separate-repos-into-one-monorepo)
- [356: What breaks most often when merging repos into a monorepo?](#356-what-breaks-most-often-when-merging-repos-into-a-monorepo)
- [357: How would you migrate from Lerna to a modern setup?](#357-how-would-you-migrate-from-lerna-to-a-modern-setup)
- [358: How would you migrate from Turborepo to Nx or the other way?](#358-how-would-you-migrate-from-turborepo-to-nx-or-the-other-way)
- [359: What are the main differences in default inputs between Turborepo and Nx?](#359-what-are-the-main-differences-in-default-inputs-between-turborepo-and-nx)
- [360: How do you handle a task that depends on files generated by another package's task?](#360-how-do-you-handle-a-task-that-depends-on-files-generated-by-another-packages-task)
- [361: How would you generate a typed API client from an OpenAPI spec in a monorepo?](#361-how-would-you-generate-a-typed-api-client-from-an-openapi-spec-in-a-monorepo)
- [362: Should generated code be committed in a monorepo?](#362-should-generated-code-be-committed-in-a-monorepo)
- [363: How do you check that a committed generated file is up to date?](#363-how-do-you-check-that-a-committed-generated-file-is-up-to-date)
- [364: What are micro-frontends and how do they relate to monorepos?](#364-what-are-micro-frontends-and-how-do-they-relate-to-monorepos)
- [365: What is Module Federation?](#365-what-is-module-federation)
- [366: What are the risks of sharing dependencies with Module Federation?](#366-what-are-the-risks-of-sharing-dependencies-with-module-federation)
- [367: How do Turborepo microfrontends work?](#367-how-do-turborepo-microfrontends-work)
- [368: How do you run React Native in a monorepo?](#368-how-do-you-run-react-native-in-a-monorepo)
- [369: How do you share code between web and React Native apps?](#369-how-do-you-share-code-between-web-and-react-native-apps)
- [370: How do you handle a polyglot monorepo with Node.js and Go services?](#370-how-do-you-handle-a-polyglot-monorepo-with-nodejs-and-go-services)
- [371: How do you share types between a Node.js API and a Go service?](#371-how-do-you-share-types-between-a-nodejs-api-and-a-go-service)
- [372: What is Buck2?](#372-what-is-buck2)
- [373: When would you choose Bazel over Nx or Turborepo?](#373-when-would-you-choose-bazel-over-nx-or-turborepo)
- [374: What is the difference between package-level and file-level build graphs?](#374-what-is-the-difference-between-package-level-and-file-level-build-graphs)
- [375: How do you make test runs more precise than per-package affected?](#375-how-do-you-make-test-runs-more-precise-than-per-package-affected)
- [376: What is test impact analysis?](#376-what-is-test-impact-analysis)
- [377: How do you deal with flaky tests in a monorepo?](#377-how-do-you-deal-with-flaky-tests-in-a-monorepo)
- [378: Does Turborepo cache failed tasks?](#378-does-turborepo-cache-failed-tasks)
- [379: What is Nx self-healing CI?](#379-what-is-nx-self-healing-ci)
- [380: How do you handle cache size and eviction?](#380-how-do-you-handle-cache-size-and-eviction)
- [381: How do you estimate the benefit of a remote cache before paying for one?](#381-how-do-you-estimate-the-benefit-of-a-remote-cache-before-paying-for-one)
- [382: Why is the first CI run on main after a merge often a cache hit?](#382-why-is-the-first-ci-run-on-main-after-a-merge-often-a-cache-hit)
- [383: How do you make sure a cache hit is truly safe to deploy?](#383-how-do-you-make-sure-a-cache-hit-is-truly-safe-to-deploy)
- [384: What is the difference between task caching and build tool caching like webpack's filesystem cache?](#384-what-is-the-difference-between-task-caching-and-build-tool-caching-like-webpacks-filesystem-cache)
- [385: Why exclude .next/cache from Turborepo outputs?](#385-why-exclude-nextcache-from-turborepo-outputs)
- [386: How does Nx decide which files to restore on a cache hit?](#386-how-does-nx-decide-which-files-to-restore-on-a-cache-hit)
- [387: What is a common cause of "works on cache miss, fails on cache hit"?](#387-what-is-a-common-cause-of-works-on-cache-miss-fails-on-cache-hit)
- [388: What is a common cause of "works on cache hit, fails on cache miss"?](#388-what-is-a-common-cause-of-works-on-cache-hit-fails-on-cache-miss)
- [389: How would you test that your cache configuration is correct?](#389-how-would-you-test-that-your-cache-configuration-is-correct)
- [390: How does Nx handle tasks that write outputs into the same folder?](#390-how-does-nx-handle-tasks-that-write-outputs-into-the-same-folder)
- [391: Why should each package build into its own folder rather than a shared root dist?](#391-why-should-each-package-build-into-its-own-folder-rather-than-a-shared-root-dist)
- [392: How do you design a release process for 30 independently versioned packages?](#392-how-do-you-design-a-release-process-for-30-independently-versioned-packages)
- [393: How do you check in CI that a pull request includes a changeset?](#393-how-do-you-check-in-ci-that-a-pull-request-includes-a-changeset)
- [394: How does nx release decide what to bump?](#394-how-does-nx-release-decide-what-to-bump)
- [395: What are version plans in nx release?](#395-what-are-version-plans-in-nx-release)
- [396: How do you release packages and deploy apps from the same monorepo?](#396-how-do-you-release-packages-and-deploy-apps-from-the-same-monorepo)
- [397: How do you roll back one app in a monorepo without rolling back others?](#397-how-do-you-roll-back-one-app-in-a-monorepo-without-rolling-back-others)
- [398: How do you handle database migrations when several services share a database?](#398-how-do-you-handle-database-migrations-when-several-services-share-a-database)
- [399: Explain expand and contract migrations in a monorepo context.](#399-explain-expand-and-contract-migrations-in-a-monorepo-context)
- [400: Why can't you assume all apps in a monorepo are deployed at the same time?](#400-why-cant-you-assume-all-apps-in-a-monorepo-are-deployed-at-the-same-time)
- [401: How do you version an API used by several apps in the same monorepo?](#401-how-do-you-version-an-api-used-by-several-apps-in-the-same-monorepo)
- [402: How would you design CI for a monorepo with 200 projects and 100 engineers?](#402-how-would-you-design-ci-for-a-monorepo-with-200-projects-and-100-engineers)
- [403: Why use one summary check for branch protection in a monorepo?](#403-why-use-one-summary-check-for-branch-protection-in-a-monorepo)
- [404: How do you handle CI for changes that only touch documentation?](#404-how-do-you-handle-ci-for-changes-that-only-touch-documentation)
- [405: What is a "trigger everything" file and how do you handle it?](#405-what-is-a-trigger-everything-file-and-how-do-you-handle-it)
- [406: How do you decide what belongs in globalDependencies or sharedGlobals?](#406-how-do-you-decide-what-belongs-in-globaldependencies-or-sharedglobals)
- [407: How would you handle a CI workflow change that should test everything?](#407-how-would-you-handle-a-ci-workflow-change-that-should-test-everything)
- [408: What are the trade-offs of putting infrastructure code (Terraform, Kubernetes) in the monorepo?](#408-what-are-the-trade-offs-of-putting-infrastructure-code-terraform-kubernetes-in-the-monorepo)
- [409: How would you prevent one team's broken build from blocking everyone?](#409-how-would-you-prevent-one-teams-broken-build-from-blocking-everyone)
- [410: What is a "monorepo-wide refactor" and how do you do it safely?](#410-what-is-a-monorepo-wide-refactor-and-how-do-you-do-it-safely)
- [411: How do you get a large cross-team change reviewed when CODEOWNERS requires many approvals?](#411-how-do-you-get-a-large-cross-team-change-reviewed-when-codeowners-requires-many-approvals)
- [412: How does Google's monorepo handle so much code?](#412-how-does-googles-monorepo-handle-so-much-code)
- [413: What is a virtual file system for a monorepo?](#413-what-is-a-virtual-file-system-for-a-monorepo)
- [414: What is Sapling?](#414-what-is-sapling)
- [415: What are stacked pull requests and why are they useful in monorepos?](#415-what-are-stacked-pull-requests-and-why-are-they-useful-in-monorepos)
- [416: How do you set up a monorepo for multiple teams with different release speeds?](#416-how-do-you-set-up-a-monorepo-for-multiple-teams-with-different-release-speeds)
- [417: What is a release train and does it fit a monorepo?](#417-what-is-a-release-train-and-does-it-fit-a-monorepo)
- [418: How do you cherry-pick a fix to a release branch in a monorepo?](#418-how-do-you-cherry-pick-a-fix-to-a-release-branch-in-a-monorepo)
- [419: What would you do if CI time doubled over six months?](#419-what-would-you-do-if-ci-time-doubled-over-six-months)
- [420: Your remote cache hit rate dropped from 80% to 20% overnight. How do you investigate?](#420-your-remote-cache-hit-rate-dropped-from-80-to-20-overnight-how-do-you-investigate)
- [421: A developer says a build passes locally but fails in CI with the same commit. What do you check?](#421-a-developer-says-a-build-passes-locally-but-fails-in-ci-with-the-same-commit-what-do-you-check)
- [422: Why do case-sensitive file names cause monorepo CI failures?](#422-why-do-case-sensitive-file-names-cause-monorepo-ci-failures)
- [423: A shared package change broke an app that wasn't in the affected list. How could that happen?](#423-a-shared-package-change-broke-an-app-that-wasnt-in-the-affected-list-how-could-that-happen)
- [424: How does Nx find dependencies between projects?](#424-how-does-nx-find-dependencies-between-projects)
- [425: How does Turborepo find dependencies between packages?](#425-how-does-turborepo-find-dependencies-between-packages)
- [426: What are the pros and cons of import analysis versus package.json analysis for graphs?](#426-what-are-the-pros-and-cons-of-import-analysis-versus-packagejson-analysis-for-graphs)
- [427: What is the risk of TypeScript path aliases in a package-based monorepo?](#427-what-is-the-risk-of-typescript-path-aliases-in-a-package-based-monorepo)
- [428: How would you design a dev environment so starting the full system is fast?](#428-how-would-you-design-a-dev-environment-so-starting-the-full-system-is-fast)
- [429: How do you handle very long install times in a monorepo dev container or codespace?](#429-how-do-you-handle-very-long-install-times-in-a-monorepo-dev-container-or-codespace)
- [430: How do you install Playwright browsers efficiently in a monorepo?](#430-how-do-you-install-playwright-browsers-efficiently-in-a-monorepo)
- [431: What are the security implications of a single repo for all code?](#431-what-are-the-security-implications-of-a-single-repo-for-all-code)
- [432: How do you prevent secrets from being committed to a monorepo?](#432-how-do-you-prevent-secrets-from-being-committed-to-a-monorepo)
- [433: How do you run npm audit or vulnerability scans in a monorepo?](#433-how-do-you-run-npm-audit-or-vulnerability-scans-in-a-monorepo)
- [434: What is SBOM and how does a monorepo complicate it?](#434-what-is-sbom-and-how-does-a-monorepo-complicate-it)
- [435: How would you enforce that apps don't import from other apps?](#435-how-would-you-enforce-that-apps-dont-import-from-other-apps)
- [436: How would you enforce a layered architecture across packages?](#436-how-would-you-enforce-a-layered-architecture-across-packages)
- [437: How do you prevent a package from growing unbounded dependencies?](#437-how-do-you-prevent-a-package-from-growing-unbounded-dependencies)
- [438: How do you keep the bundle size of apps under control when sharing packages?](#438-how-do-you-keep-the-bundle-size-of-apps-under-control-when-sharing-packages)
- [439: What is the problem with barrel files in monorepo packages?](#439-what-is-the-problem-with-barrel-files-in-monorepo-packages)
- [440: What does "sideEffects": false do for a shared package?](#440-what-does-sideeffects-false-do-for-a-shared-package)
- [441: How do you publish a package from a monorepo that works for both ESM and CommonJS users?](#441-how-do-you-publish-a-package-from-a-monorepo-that-works-for-both-esm-and-commonjs-users)
- [442: What is the dual package hazard?](#442-what-is-the-dual-package-hazard)
- [443: How would you structure a monorepo for a SaaS product with web, mobile, API and workers?](#443-how-would-you-structure-a-monorepo-for-a-saas-product-with-web-mobile-api-and-workers)
- [444: In that SaaS layout, why keep db out of web and mobile?](#444-in-that-saas-layout-why-keep-db-out-of-web-and-mobile)
- [445: How do you share business logic between the API and a background worker?](#445-how-do-you-share-business-logic-between-the-api-and-a-background-worker)
- [446: How would you explain to management why the monorepo needs a platform team?](#446-how-would-you-explain-to-management-why-the-monorepo-needs-a-platform-team)
- [447: When would you move away from a monorepo?](#447-when-would-you-move-away-from-a-monorepo)
- [448: Interview scenario: a team wants to add a heavy Python ML service to your JavaScript monorepo. What do you consider?](#448-interview-scenario-a-team-wants-to-add-a-heavy-python-ml-service-to-your-javascript-monorepo-what-do-you-consider)
- [449: Interview scenario: builds pass but the deployed app uses an old version of a shared package. How do you debug?](#449-interview-scenario-builds-pass-but-the-deployed-app-uses-an-old-version-of-a-shared-package-how-do-you-debug)
- [450: What are the three most important things to get right when starting a monorepo?](#450-what-are-the-three-most-important-things-to-get-right-when-starting-a-monorepo)

---

# Easy Questions (1-150)

## 1: What is a monorepo?

A monorepo is a single Git repository that holds the code for many projects, like several apps and the libraries they share. Each project still has its own folder, its own `package.json` and its own build and test scripts. The key point is that they live side by side and can depend on each other directly, without publishing to a registry first.

## 2: What is a polyrepo?

A polyrepo setup (sometimes called multi-repo) means each project lives in its own repository. A shared library is published to a registry like npm, and every app that uses it installs a version from there. This is the opposite of a monorepo, where all of those projects share one repository.

## 3: Is a monorepo the same as a monolith?

No. A monolith is one big application that is built and deployed as a single unit. A monorepo is about where the code is stored, not how it is deployed. You can have a monorepo with twenty small services that are each deployed on their own, and you can have a monolith that lives in its own repository.

## 4: Why do teams use monorepos?

The main reasons are:

- Sharing code is easy. A shared library is just another folder.
- One change can update a library and every app that uses it in a single commit and pull request.
- Tooling, linting rules, CI config and dependency versions can be kept the same across projects.
- It's easier to see the whole system and search through all the code at once.

## 5: What are the main downsides of a monorepo?

The repository gets big, so clone times, CI times and editor performance can suffer without good tooling. Everyone shares one main branch, so a broken build can block many teams. Access control is harder because Git doesn't support per-folder permissions. You also need extra tools (a task runner, caching, affected detection) that a small single-project repo doesn't need.

## 6: Which well-known companies use monorepos?

Google keeps most of its code in one huge repository and built its own tools for it (Piper and Blaze, which later became the open source Bazel). Meta, Microsoft (for some products), Uber and Airbnb also use large monorepos. In the open source world, projects like React, Babel, Next.js, Vue and Angular all use monorepos with many packages.

## 7: What is a workspace in a JavaScript monorepo?

A workspace is a package inside the monorepo that the package manager knows about. You list the workspace folders in the root config, and the package manager installs dependencies for all of them at once and links them together. So if `apps/web` depends on `@acme/ui`, the package manager links the local `packages/ui` folder instead of downloading it from npm.

## 8: How do you set up npm workspaces?

Add a `workspaces` field to the root `package.json` with the folders or glob patterns that hold your packages:

```json
{
  "name": "acme",
  "private": true,
  "workspaces": ["apps/*", "packages/*"]
}
```

Then run `npm install` at the root. npm installs all dependencies and creates symlinks in the root `node_modules` for every workspace package.

## 9: How do you set up pnpm workspaces?

pnpm doesn't read the `workspaces` field from `package.json`. You create a `pnpm-workspace.yaml` file at the root instead:

```yaml
packages:
  - "apps/*"
  - "packages/*"
```

Then run `pnpm install` at the root. pnpm installs everything and links local packages to each other.

## 10: How do you set up Yarn workspaces?

Yarn uses the same `workspaces` field in the root `package.json` as npm:

```json
{
  "private": true,
  "workspaces": ["apps/*", "packages/*"]
}
```

Running `yarn install` at the root installs and links all workspaces. Modern Yarn (version 2 and later, often called Yarn Berry) adds extra workspace features like `yarn workspaces foreach` and constraints.

## 11: Why should the root package.json be private?

Setting `"private": true` stops anyone from accidentally publishing the root package to npm. The root is just a container for the workspaces and shared dev tools, not a real package. npm and Yarn also require the root to be private when you use the `workspaces` field.

## 12: What is a typical folder layout for a JavaScript monorepo?

A common layout looks like this:

```
acme/
  apps/
    web/
    admin/
    api/
  packages/
    ui/
    utils/
    eslint-config/
    tsconfig/
  package.json
  pnpm-workspace.yaml
  turbo.json
```

`apps/` holds things you deploy. `packages/` holds shared libraries and shared config. The names are a convention, not a rule.

## 13: What is the difference between an app and a package in a monorepo?

An app is something you deploy or run, like a website, an API or a mobile app. Nothing else in the repo imports it. A package (or library) is code that other projects import, like a UI component library or a set of helper functions. Keeping the two apart makes the dependency direction clear: apps depend on packages, and packages should not depend on apps.

## 14: What does the workspace protocol mean in a dependency version?

The `workspace:` protocol tells pnpm or Yarn to always use the local package from the monorepo and never download it from the registry:

```json
{
  "dependencies": {
    "@acme/ui": "workspace:*"
  }
}
```

If the local package can't be found, the install fails instead of silently pulling a published copy. When you publish, the package manager replaces `workspace:*` with the real version number.

## 15: Does npm support the workspace protocol?

No. npm doesn't understand `workspace:*`. With npm workspaces you use a normal version range like `"@acme/ui": "*"` or `"^1.0.0"`, and npm links the local package if its version matches. If the version doesn't match, npm may try to fetch it from the registry, which is one reason many teams prefer pnpm or Yarn for monorepos.

## 16: How do you install a dependency into one workspace with npm?

Use the `-w` (or `--workspace`) flag with the package name or folder:

```bash
npm install zod -w @acme/api
npm install zod --workspace=apps/api
```

This adds `zod` to `apps/api/package.json` only.

## 17: How do you install a dependency into one workspace with pnpm?

Use `--filter` with the package name:

```bash
pnpm add zod --filter @acme/api
```

You can also `cd` into the package folder and run `pnpm add zod` there. pnpm will still use the shared lockfile at the root.

## 18: How do you install a dependency at the root of a pnpm workspace?

Use the `-w` flag, which stands for workspace root:

```bash
pnpm add -D typescript -w
```

Without `-w`, pnpm refuses to add dependencies to the root to stop you from doing it by mistake. Root dependencies are usually dev tools like TypeScript, Prettier or Turborepo.

## 19: How do you run a script in every workspace with npm?

Use `--workspaces` (or `-ws`):

```bash
npm run test --workspaces
npm run build -ws --if-present
```

`--if-present` skips workspaces that don't have that script instead of failing.

## 20: How do you run a script in every workspace with pnpm?

Use the `-r` (recursive) flag:

```bash
pnpm -r run build
pnpm -r --parallel run dev
```

pnpm runs the script in every package that has it, in dependency order by default. `--parallel` ignores order and runs them all at once, which is useful for long-running `dev` servers.

## 21: How do you run a script in one workspace with Yarn?

Use `yarn workspace` with the package name:

```bash
yarn workspace @acme/web run build
yarn workspace @acme/web add react
```

To run a script in all workspaces with modern Yarn, use `yarn workspaces foreach -A run build`.

## 22: What is a single lockfile and why does it matter?

A workspace setup has one lockfile at the root (`package-lock.json`, `pnpm-lock.yaml` or `yarn.lock`) for all packages. Every install for every project resolves from this one file, so everyone gets the same versions. It also means one dependency upgrade can be reviewed and tested for the whole repo at once.

## 23: What is hoisting?

Hoisting means the package manager moves dependencies up to the root `node_modules` folder instead of putting a copy in every package's own `node_modules`. If ten packages use `lodash`, it's installed once at the root. This saves disk space and install time, but it also lets packages accidentally import things they never declared.

## 24: What is a phantom dependency?

A phantom dependency is a package your code imports even though it isn't listed in that package's `package.json`. It works only because some other package depends on it and it got hoisted to the root `node_modules`. If that other package drops it, or you publish your package on its own, the import breaks. pnpm's strict layout catches most of these.

## 25: How does pnpm store packages?

pnpm keeps every package version once in a global content-addressable store on your machine. Each project's `node_modules` contains hard links to the store, so the same file isn't copied again for each project. Inside `node_modules`, pnpm only puts your direct dependencies at the top level and keeps the rest in a hidden `.pnpm` folder, which is why phantom dependencies fail.

## 26: What is a task runner in a monorepo?

A task runner (also called a build system or orchestrator) runs scripts like `build`, `test` and `lint` across many packages. It knows the dependency graph, so it builds `@acme/ui` before `apps/web`. It can run independent tasks in parallel, cache results and skip work that hasn't changed. Turborepo and Nx are the most common ones in the JavaScript world.

## 27: What is Turborepo?

Turborepo is a build system for JavaScript and TypeScript monorepos, made by Vercel. It runs your existing `package.json` scripts across workspaces, in the right order and in parallel. It caches task results locally and optionally in a remote cache, so work that has already been done isn't repeated. You configure it with a `turbo.json` file at the root.

## 28: What is Nx?

Nx is a build system and set of tools for monorepos, made by the company Nx (formerly Nrwl). It builds a project graph, runs tasks with caching, and figures out which projects are affected by a change. It also has plugins for many tools (React, Next.js, Node, Vite, Jest, Playwright and more) and code generators that create new apps and libraries for you.

## 29: What is Lerna?

Lerna was one of the first tools for JavaScript monorepos, mainly used to version and publish many packages from one repository. It was close to dead in 2022 until the Nx team took over maintenance. Modern Lerna uses Nx under the hood to run tasks and still offers `lerna version` and `lerna publish`. New projects often pick Changesets or `nx release` instead, but you'll still see Lerna in older repos.

## 30: What is Changesets?

Changesets is a tool for managing versions and changelogs in a monorepo. When you make a change, you run `npx changeset` and write a small file that says which packages changed and whether it's a patch, minor or major bump. Later, `changeset version` applies those bumps and writes changelogs, and `changeset publish` publishes the packages to npm.

## 31: What is a dependency graph in a monorepo?

It's a map of which projects depend on which other projects. If `apps/web` imports `@acme/ui` and `@acme/ui` imports `@acme/utils`, the graph has edges from web to ui and from ui to utils. Tools use this graph to decide build order, run things in parallel when they don't depend on each other, and find which projects a change affects.

## 32: What is a task graph?

A task graph is built from the dependency graph plus your task rules. It has one node per task, for example `@acme/ui#build` or `web#test`, and edges that say which tasks must finish first. If `web#build` depends on `^build`, then it waits for the build of every package `web` depends on. The task runner walks this graph to decide what to run and when.

## 33: How do you see the dependency graph in Nx?

Run:

```bash
npx nx graph
```

It opens an interactive page in your browser that shows every project and the edges between them. You can focus on one project, see what depends on it, and also view the task graph for a command.

## 34: How do you see the task graph in Turborepo?

Use the `--graph` flag:

```bash
npx turbo run build --graph
```

By default it prints the graph in a text format you can paste into a Graphviz viewer. You can also write it to a file, for example `--graph=graph.html` or `--graph=graph.svg`. Turborepo also has a `turbo query` command that answers questions about the repo graph.

## 35: What does "affected" mean in a monorepo?

A project is affected by a change if its own files changed, or if any project it depends on changed. If you edit `@acme/utils`, then `utils`, every package that imports `utils`, and every app that imports those packages are affected. Running tests only for affected projects is how monorepos keep CI time under control.

## 36: How do you run tasks only for affected projects in Nx?

Use `nx affected`:

```bash
npx nx affected -t test
npx nx affected -t lint test build --base=origin/main --head=HEAD
```

Nx compares the two Git refs, finds the changed files, maps them to projects and then adds every project that depends on them.

## 37: How do you run tasks only for affected packages in Turborepo?

Use the `--affected` flag:

```bash
npx turbo run test --affected
```

Turborepo compares the current branch with the default branch (usually `main`) and runs the task only in packages whose files changed, plus the packages that depend on them. You can also use a filter like `--filter=...[origin/main]` for more control.

## 38: What is task caching?

Task caching means that when a task runs, the tool saves its output (files and logs) under a key made from its inputs. Next time the inputs are the same, it restores the saved output instead of running the task again. A build that took two minutes can come back in under a second if nothing relevant changed.

## 39: What is a cache hit and a cache miss?

A cache hit means the tool found a saved result for the exact same inputs and replayed it. A cache miss means no saved result matched, so the task actually ran and its result was then stored. In Turborepo and Nx logs you see markers like "cache hit, replaying logs" so you know which tasks really ran.

## 40: What is remote caching?

Remote caching stores task results on a shared server instead of only on your own machine. If a teammate or a CI job already built the same code, you can download their result instead of building it again. Turborepo can use Vercel Remote Cache or a self-hosted cache server, and Nx has Nx Cloud or self-hosted options.

## 41: Where does Turborepo store its local cache?

In current versions, Turborepo stores the local cache in `.turbo/cache` at the root of the repo. Older versions used `node_modules/.cache/turbo`. You should add `.turbo` to `.gitignore` so cache files never get committed.

## 42: Where does Nx store its local cache?

By default Nx stores its cache in `.nx/cache` at the workspace root, and some workspace data in `.nx/workspace-data`. You can change the cache folder with the `cacheDirectory` option in `nx.json`. The `.nx` folder should be in `.gitignore`.

## 43: What does a basic turbo.json look like?

```json
{
  "$schema": "https://turborepo.com/schema.json",
  "tasks": {
    "build": {
      "dependsOn": ["^build"],
      "outputs": ["dist/**", ".next/**", "!.next/cache/**"]
    },
    "test": {
      "dependsOn": ["^build"]
    },
    "lint": {},
    "dev": {
      "cache": false,
      "persistent": true
    }
  }
}
```

Each key under `tasks` matches a script name in your workspaces' `package.json` files.

## 44: What does the caret mean in dependsOn, like "^build"?

`^build` means "run the `build` task in all of this package's dependencies first". So before `web#build` runs, every workspace package that `web` depends on is built. Without the caret, `"dependsOn": ["lint"]` means "run `lint` in the same package first".

## 45: What is the outputs key in turbo.json?

`outputs` lists the files a task produces, as glob patterns relative to the package. Turborepo saves these files in the cache and restores them on a cache hit. If you forget to list them, a cache hit replays the logs but your `dist` folder won't be there, which causes confusing errors later.

## 46: Why should the dev task not be cached?

A `dev` task starts a long-running server that watches files. It doesn't produce a final output worth saving, and restoring it from cache makes no sense. So you set `"cache": false`. You also set `"persistent": true` so Turborepo knows the task never exits and won't let other tasks depend on it.

## 47: What was the pipeline key in turbo.json?

In Turborepo 1.x the task definitions lived under a key called `pipeline`. Turborepo 2.0 renamed it to `tasks`. If you see `pipeline` in a repo, it's an old config, and you can update it with `npx @turbo/codemod migrate`.

## 48: How do you run a task with Turborepo?

```bash
npx turbo run build
npx turbo build        # short form
npx turbo build test lint
```

Turborepo finds every workspace that has the script, builds the task graph from `turbo.json`, and runs the tasks in parallel where it can. You can run several tasks in one command.

## 49: How do you run a task for one package with Turborepo?

Use `--filter`:

```bash
npx turbo run build --filter=web
npx turbo run build --filter=@acme/ui
```

Because of `^build`, the packages `web` depends on also get built first. If you're inside the package folder, plain `turbo run build` scopes to that package automatically.

## 50: How do you run a task for one project with Nx?

```bash
npx nx build web
npx nx run web:build
npx nx test ui
```

`nx <target> <project>` is the short form, and `nx run <project>:<target>` is the long form. Nx also builds dependencies first if the target has `dependsOn` set up.

## 51: How do you run a task for many projects with Nx?

Use `run-many`:

```bash
npx nx run-many -t build
npx nx run-many -t lint test --projects=web,api
```

`-t` is short for `--targets`. Without `--projects` it runs the target in every project that has it.

## 52: What is nx.json?

`nx.json` is the root config file for Nx. It holds workspace-wide settings like `targetDefaults` (default settings for tasks such as `build`), `namedInputs` (reusable file sets for caching), plugins, the default base branch and release settings. Each project can then override these in its own `project.json` or `package.json`.

## 53: What is project.json in Nx?

`project.json` describes one Nx project: its name, root folder, tags and targets (tasks). It's optional. Nx can read scripts from `package.json`, and Nx plugins can infer targets from tool config files like `vite.config.ts`. You use `project.json` when you want to add or override targets explicitly.

## 54: What are inferred tasks in Nx?

Inferred tasks (introduced as "Project Crystal" in Nx 18) are targets that Nx plugins create by reading your tool config files. For example, if a project has a `vite.config.ts`, the `@nx/vite` plugin adds `build`, `serve` and `test` targets with correct cache inputs and outputs. You don't have to write them in `project.json`. Run `nx show project <name>` to see what was inferred.

## 55: How do you create a new Nx workspace?

```bash
npx create-nx-workspace@latest acme
```

It asks a few questions (stack, framework, whether to use Nx Cloud) and creates the workspace. You can also add Nx to an existing repo with `npx nx@latest init`.

## 56: How do you create a new Turborepo monorepo?

```bash
npx create-turbo@latest
```

It creates a starter repo with a couple of apps, some shared packages and a `turbo.json`. You can also add Turborepo to an existing workspace by installing `turbo` as a root dev dependency and writing a `turbo.json`.

## 57: How do you add Turborepo to an existing workspace?

Install it at the root and add a `turbo.json`:

```bash
pnpm add -D turbo -w
```

```json
{
  "$schema": "https://turborepo.com/schema.json",
  "tasks": {
    "build": { "dependsOn": ["^build"], "outputs": ["dist/**"] }
  }
}
```

Then add a root script like `"build": "turbo run build"`. Your existing workspace scripts keep working as before.

## 58: Should you install turbo globally or locally?

Both are common. The local install at the root as a dev dependency pins the version for the whole team and CI, which is the important part. A global install is just a shortcut so you can type `turbo` anywhere. When both exist, the global `turbo` hands off to the local version from the repo.

## 59: What is an internal package?

An internal package is a workspace package that is only used inside the monorepo and never published to npm. It usually has `"private": true` in its `package.json`. Shared UI components, config packages and helpers for your own apps are typical internal packages.

## 60: What is a shared config package?

It's a workspace package that holds config other packages extend, like ESLint rules, TypeScript settings or Prettier options. For example, `packages/tsconfig` might export `base.json`, and every package's `tsconfig.json` extends it. This keeps settings the same across the repo and lets you change them in one place.

## 61: How do you share a tsconfig across packages?

Create a package with a base config:

```json
{
  "name": "@acme/tsconfig",
  "private": true,
  "files": ["base.json"]
}
```

Then in each package:

```json
{
  "extends": "@acme/tsconfig/base.json",
  "compilerOptions": { "outDir": "dist" },
  "include": ["src"]
}
```

Add `"@acme/tsconfig": "workspace:*"` to that package's dev dependencies so the link exists.

## 62: How do you share an ESLint config across packages?

Make a package that exports a flat config array:

```js
// packages/eslint-config/index.js
import js from "@eslint/js";

export default [js.configs.recommended, { rules: { "no-console": "warn" } }];
```

Then each package's `eslint.config.js` imports it:

```js
import base from "@acme/eslint-config";

export default [...base];
```

## 63: Why do you scope package names like @acme/ui?

A scope groups your packages under one name and avoids clashes with public npm packages. `ui` or `utils` are almost certainly taken on npm, but `@acme/ui` is yours. Scopes also make imports clear: anything starting with `@acme/` comes from your own monorepo.

## 64: How does one app import a shared package?

Add it as a dependency and import it like any npm package:

```json
{
  "dependencies": {
    "@acme/utils": "workspace:*"
  }
}
```

```js
import { formatPrice } from "@acme/utils";
```

After `pnpm install`, `node_modules/@acme/utils` is a symlink to `packages/utils`, so Node and bundlers resolve it from there.

## 65: What is the exports field in package.json?

`exports` defines which files of a package can be imported and from which paths. It replaces the older `main` field for modern Node and bundlers:

```json
{
  "name": "@acme/utils",
  "type": "module",
  "exports": {
    ".": "./dist/index.js",
    "./date": "./dist/date.js"
  }
}
```

Anything not listed can't be imported from outside, which keeps a package's private files private.

## 66: Why do monorepo tools need to know the order of builds?

If `web` imports `@acme/ui` and `ui` must be compiled to `dist` first, then building `web` before `ui` fails or uses old files. The task runner reads the dependency graph and makes sure `ui#build` finishes before `web#build` starts. Tasks with no relation between them can still run at the same time.

## 67: What is a root script in a monorepo?

A root script is a script in the root `package.json`, usually a short command that runs a task across the whole repo:

```json
{
  "scripts": {
    "build": "turbo run build",
    "dev": "turbo run dev",
    "lint": "turbo run lint",
    "format": "prettier --write ."
  }
}
```

It gives everyone one easy entry point like `pnpm build`.

## 68: What is the difference between dependencies and devDependencies in a workspace package?

`dependencies` are needed at runtime by whoever uses the package. `devDependencies` are only needed while developing or building it, like TypeScript, test tools or bundlers. For internal packages that are never published, the difference matters less, but keeping it right helps with Docker images and with publishing later.

## 69: What is a peer dependency and why does it matter in monorepos?

A peer dependency says "I need this package, but whoever uses me must provide it". UI libraries list `react` as a peer dependency so the app's React instance is used. In a monorepo this avoids having two copies of React (one for the library, one for the app), which breaks hooks.

```json
{
  "peerDependencies": { "react": "^19.0.0" }
}
```

## 70: Why is having two copies of React in a monorepo a problem?

React hooks rely on a single shared React instance. If your component library resolves one copy of `react` and the app resolves another, hooks throw "Invalid hook call" errors. This often happens in monorepos when versions don't match or when a package lists `react` in `dependencies` instead of `peerDependencies`.

## 71: What does "single version policy" mean?

It means every package in the monorepo uses the same version of each third-party dependency. If the repo uses React 19, every app uses React 19. Google's monorepo works this way. It avoids duplicate copies and odd bugs, but upgrades have to be done for the whole repo at once.

## 72: What are pnpm catalogs?

Catalogs let you define dependency versions once in `pnpm-workspace.yaml` and refer to them from any package:

```yaml
packages:
  - "apps/*"
  - "packages/*"
catalog:
  react: ^19.1.0
  zod: ^3.24.0
```

```json
{
  "dependencies": {
    "react": "catalog:",
    "zod": "catalog:"
  }
}
```

To upgrade React everywhere, you change one line.

## 73: What is a CODEOWNERS file?

`CODEOWNERS` is a GitHub (and GitLab) file that maps paths to the people or teams who own them:

```
/apps/web/        @acme/web-team
/packages/ui/     @acme/design-system
/packages/auth/   @acme/security
```

When a pull request touches those paths, the owners are asked to review it automatically. In a monorepo this is how teams keep control of their own folders.

## 74: How does a monorepo help with atomic changes?

An atomic change updates many projects in one commit. If you rename a function in `@acme/utils`, you can update every caller in the same pull request. Either all of it is merged or none of it is. In a polyrepo you'd publish a new library version, then open a pull request in each app repo, and the repos would be out of sync for a while.

## 75: What is trunk-based development and why is it common with monorepos?

Trunk-based development means everyone merges small changes into one main branch (the trunk) often, instead of keeping long-lived feature branches. It fits monorepos because long branches in a big shared repo quickly drift and cause painful merges. Unfinished features are hidden behind feature flags instead of living on a branch.

## 76: What does the .gitignore of a JavaScript monorepo usually include?

```
node_modules
dist
build
.next
coverage
.turbo
.nx/cache
.nx/workspace-data
.env*.local
```

Build outputs and caches should never be committed. A single root `.gitignore` covers all packages because Git patterns without a leading slash match at any folder depth.

## 77: What is the difference between a monorepo tool and a package manager?

The package manager (npm, pnpm, Yarn) installs dependencies and links workspace packages. The monorepo tool (Turborepo, Nx) runs tasks across those packages, with ordering, parallel runs, caching and affected detection. They work together: the tool reads the workspace layout that the package manager set up.

## 78: Can you have a monorepo without any special tool?

Yes. Plain npm, pnpm or Yarn workspaces are enough to link packages and run scripts in all of them. Many small repos work fine that way. Tools like Turborepo or Nx become worth it once builds and tests get slow, because they add caching and only run what changed.

## 79: How do you list all workspaces with pnpm?

```bash
pnpm ls -r --depth -1
```

This prints every workspace package with its name, version and path. With npm you can use `npm query .workspace`, and with Yarn Berry `yarn workspaces list`.

## 80: How do you list all projects in Nx?

```bash
npx nx show projects
npx nx show projects --affected
npx nx show project web
```

The first lists every project, the second only affected ones, and the third prints the full resolved config of one project, including inferred targets.

## 81: How does a pnpm filter work?

`--filter` (or `-F`) picks which workspace packages a command runs in:

```bash
pnpm --filter web build          # one package by name
pnpm --filter "./apps/**" test   # by folder
pnpm --filter "@acme/*" lint     # by name pattern
```

Filters also support graph selectors, like including dependencies or dependents, which are covered in later questions.

## 82: What does pnpm --filter web... do?

The three dots after the name mean "this package and all of its dependencies". So `pnpm --filter web... build` builds `web` and every workspace package it depends on. Dots before the name, `...web`, mean "this package and everything that depends on it".

## 83: What is a dependent in a monorepo?

A dependent is a package that depends on another one. If `web` imports `@acme/ui`, then `web` is a dependent of `ui`, and `ui` is a dependency of `web`. When you change `ui`, its dependents might break, so they need to be tested too.

## 84: What is the difference between direct and transitive dependencies here?

A direct dependency is listed in your own `package.json`. A transitive dependency is a dependency of one of your dependencies. If `web` depends on `ui` and `ui` depends on `utils`, then `utils` is a transitive dependency of `web`. A change to `utils` affects `web` even though `web` never imports `utils` directly.

## 85: What does the Turborepo log prefix mean, like "web:build:"?

Turborepo prefixes each log line with the package and task name, for example `web:build: compiled successfully`. Since many tasks run in parallel, the prefix tells you which task wrote which line. You can change the output style with `--log-order` (stream, grouped) or use the terminal UI with `--ui=tui`.

## 86: What is the Turborepo terminal UI?

Since Turborepo 2.0 there is an interactive terminal UI (`--ui=tui`, or `"ui": "tui"` in `turbo.json`). It shows a list of tasks on one side and the selected task's logs on the other. You can switch between tasks and even type into a task that needs input, like an interactive dev server.

## 87: How do you force a task to run without the cache in Turborepo?

```bash
npx turbo run build --force
```

`--force` ignores existing cache entries and runs every task, but still writes new results to the cache. To skip writing too, use `--cache=local:r,remote:r` for read-only or disable caching for the task in `turbo.json`.

## 88: How do you skip the cache in Nx?

```bash
npx nx build web --skip-nx-cache
```

This runs the task for real even if a matching cache entry exists. To clear the cache completely, run `npx nx reset`, which also stops the Nx daemon.

## 89: What is the Nx daemon?

The Nx daemon is a background process that keeps the project graph in memory and watches files for changes. Without it, Nx would rebuild the graph from scratch every time you run a command, which is slow in big repos. If things look stale, `nx reset` restarts it. You can turn it off with `NX_DAEMON=false`, which CI sometimes does.

## 90: What is a generator in Nx?

A generator is a script that creates or changes files for you, like scaffolding a new library with the right folder layout, config and tests. You run one with `nx generate` (or `nx g`):

```bash
npx nx g @nx/react:library packages/ui
```

Plugins ship generators, and you can write your own to keep new projects consistent.

## 91: What is an executor in Nx?

An executor is a function that runs a task, like building with Vite or running Jest. In `project.json`, a target can say `"executor": "@nx/vite:build"` with options. With inferred tasks, many projects now just run the tool's own CLI command instead, and executors are used less, but you'll still see them in many repos.

## 92: What is nx:run-commands?

It's a built-in Nx executor that runs one or more shell commands as a target:

```json
{
  "targets": {
    "deploy": {
      "executor": "nx:run-commands",
      "options": { "command": "node scripts/deploy.js", "cwd": "apps/api" }
    }
  }
}
```

It's the simple way to wrap any script as an Nx task with caching and dependencies.

## 93: What are tags in Nx?

Tags are labels you put on projects, like `type:ui`, `scope:checkout` or `platform:server`:

```json
{ "name": "ui", "tags": ["type:ui", "scope:shared"] }
```

They're used to group projects for commands and, more importantly, to set import rules. For example, a rule can say that `type:ui` libraries can't import `type:data-access` libraries.

## 94: What are module boundaries?

Module boundaries are rules about which projects may import which other projects. For example: apps may import libraries, but libraries may not import apps; the `checkout` team's code may not import the `admin` team's code. Without these rules, a monorepo can turn into a tangle where everything imports everything.

## 95: How do you check module boundaries in Nx?

Nx has an ESLint rule, `@nx/enforce-module-boundaries`, that reads project tags and fails lint when an import breaks the rules:

```js
{
  rules: {
    "@nx/enforce-module-boundaries": ["error", {
      depConstraints: [
        { sourceTag: "type:app", onlyDependOnLibsWithTags: ["type:feature", "type:ui", "type:util"] },
        { sourceTag: "type:ui", onlyDependOnLibsWithTags: ["type:ui", "type:util"] },
      ],
    }],
  },
}
```

## 96: What is semantic versioning?

Semantic versioning (semver) uses `MAJOR.MINOR.PATCH` numbers. You bump PATCH for bug fixes, MINOR for new backward-compatible features and MAJOR for breaking changes. In monorepos that publish packages, each package usually has its own semver version, and tools like Changesets help pick the right bump.

## 97: What is the difference between fixed and independent versioning?

With fixed (or locked) versioning, all packages share one version number. Release 3.2.0 bumps every package to 3.2.0, even if it didn't change. Angular and Babel work roughly this way. With independent versioning, each package has its own version and only changed packages get bumped. Lerna, Changesets and `nx release` support both modes.

## 98: How do you add a changeset?

```bash
npx changeset
```

It asks which packages changed and what kind of bump each needs, then asks for a short summary. It writes a markdown file in `.changeset/` that you commit with your pull request. That file is used later to bump versions and write changelog entries.

## 99: What does a changeset file look like?

```md
---
"@acme/ui": minor
"@acme/utils": patch
---

Add a Tooltip component and fix date formatting in utils.
```

The front matter lists packages and bump types, and the body becomes the changelog entry.

## 100: How do you set up Changesets in a repo?

```bash
pnpm add -D @changesets/cli -w
npx changeset init
```

`init` creates a `.changeset` folder with a `config.json` and a README. Then contributors run `npx changeset` with their changes, and a release step runs `changeset version` and `changeset publish`.

## 101: What does changeset version do?

It reads all changeset files, bumps the versions in each affected `package.json`, updates internal dependency ranges, writes `CHANGELOG.md` entries and deletes the used changeset files. You review and commit these changes, usually through a "Version Packages" pull request.

## 102: What does changeset publish do?

It publishes every package whose version in `package.json` isn't on the npm registry yet, and creates Git tags for them. Run it after `changeset version` has been merged. Private packages are skipped.

## 103: What is the Changesets GitHub Action?

`changesets/action` automates releases in CI. When changesets are merged to `main`, it opens or updates a "Version Packages" pull request with the version bumps and changelogs. When that pull request is merged, the action runs your publish command. This gives you a review step before anything goes to npm.

## 104: What is a monorepo "package" in Nx terms versus a "project"?

Nx uses the word "project" for anything it can run tasks for, whether it's an app or a library, and whether it has a `package.json` or just a `project.json`. A "package" usually means something with a `package.json` that a package manager knows about. In a package-based Nx repo the two are the same thing.

## 105: What is a package-based monorepo versus an integrated monorepo in Nx?

In a package-based repo, every project is a normal workspace package with its own `package.json` and dependencies, and Nx mainly adds task running and caching. In an integrated repo (an older Nx style), projects often share one root `package.json` and are wired through TypeScript path aliases, with Nx plugins doing most of the build work. Nx now pushes the package-based style with TypeScript project references for new workspaces.

## 106: Why do some monorepos use a single root package.json for all dependencies?

It's the simplest way to have one version of everything: there's only one place to declare dependencies. Older Nx integrated repos did this. The downside is that each project's real dependencies aren't written down, which makes Docker images, publishing and dependency analysis harder. Most teams now give each package its own `package.json`.

## 107: What does "build once, deploy many" mean in a monorepo?

It means you build an artifact (like a Docker image or a bundle) once in CI and promote that exact artifact through staging and production, instead of rebuilding it for each environment. In a monorepo the caching layer helps with this, because the build for a given commit is already cached and every later step reuses it.

## 108: How does a monorepo affect code reviews?

One pull request can touch many projects, so it may need reviews from several teams. `CODEOWNERS` helps by requesting the right reviewers automatically. It also means reviewers see the full change, for example a library change plus every caller, in one place instead of across several repositories.

## 109: What is the biggest CI problem in a growing monorepo?

Running every test and build for every change. As the repo grows, CI gets slower and slower until each pull request takes an hour. The fixes are running only affected tasks, caching results (locally and remotely), and splitting work across several CI machines.

## 110: How do you speed up npm install in a big monorepo?

Use pnpm or Yarn with a stable lockfile and a cached store in CI. Run `npm ci` or `pnpm install --frozen-lockfile` so the lockfile is never rewritten. Cache the package manager's store between CI runs. Avoid installing dependencies for packages you don't need in a given job, for example with `pnpm install --filter`.

## 111: What does pnpm install --frozen-lockfile do?

It installs exactly what `pnpm-lock.yaml` says and fails if the lockfile doesn't match the `package.json` files. In CI this catches the case where someone changed a dependency but didn't commit the updated lockfile. pnpm turns it on by default when it detects a CI environment.

## 112: How do you add a new package to a pnpm monorepo?

Create the folder under one of the workspace globs, add a `package.json` with a scoped name, and run `pnpm install` at the root:

```json
{
  "name": "@acme/logger",
  "version": "0.0.0",
  "private": true,
  "type": "module",
  "exports": { ".": "./src/index.js" }
}
```

Then add `"@acme/logger": "workspace:*"` to any package that wants to use it and run `pnpm install` again.

## 113: How do you remove a package from a monorepo safely?

First search for imports of it and remove them, and remove it from every `package.json` that lists it. Then delete the folder and run the install again so the lockfile updates. Nx's project graph or `pnpm why @acme/old-package` helps you find anything that still depends on it.

## 114: What does pnpm why do?

`pnpm why <package>` shows which of your packages depend on a given package and through which chain. In a monorepo it's handy for finding why some old version of a library is still installed, or which workspace still uses a package you want to remove.

## 115: What is a root tsconfig.json used for in a monorepo?

It often holds the project references that list every package, so `tsc -b` at the root can type-check the whole repo in the right order. It may also hold shared compiler options, though those are usually better in a shared `tsconfig.base.json` that each package extends.

## 116: What are TypeScript project references?

Project references let one TypeScript project point to others it depends on:

```json
{
  "compilerOptions": { "composite": true, "outDir": "dist" },
  "references": [{ "path": "../utils" }]
}
```

`tsc -b` (build mode) then builds referenced projects first and only rebuilds what changed. In monorepos this speeds up type checking and makes TypeScript aware of package boundaries.

## 117: What does composite: true do?

It marks a TypeScript project as one that can be referenced by others. It requires `declaration` output to be on and makes sure all files are covered by `include` or `files`. TypeScript uses it to produce `.d.ts` files and a `.tsbuildinfo` file so other projects can build against it quickly.

## 118: What are TypeScript path aliases and how are they used in monorepos?

Path aliases in `compilerOptions.paths` map an import name to a folder:

```json
{
  "compilerOptions": {
    "paths": { "@acme/utils": ["packages/utils/src/index.ts"] }
  }
}
```

Older Nx integrated repos used this to link libraries without workspace packages. It works for TypeScript, but bundlers and Node need extra config to follow the same aliases. Workspace packages with `package.json` are now the more common way to link code.

## 119: What is a "just-in-time" or source-only internal package?

It's an internal package that is never built on its own. Its `exports` point straight at the TypeScript source:

```json
{
  "name": "@acme/ui",
  "exports": { "./button": "./src/button.tsx" }
}
```

The app's bundler (Next.js, Vite) compiles it together with the app. This removes the build step for the package, but every app has to be set up to compile it, and you lose per-package build caching.

## 120: What is a compiled internal package?

It's a package that builds its own output, for example with `tsc` or `tsup`, into a `dist` folder, and its `exports` point to `dist`. Apps use it like any npm package. It needs a build step before the app can use it, but that step can be cached, and the app doesn't need special config to compile it.

## 121: What is a publishable package?

A publishable package is one you release to npm (public or private registry) for people outside the monorepo to use. It must have a real version, correct `exports`, a `files` list or `.npmignore`, built output, and no `workspace:` dependencies left after packing. It needs more care than an internal package because other people depend on its API.

## 122: How does a monorepo affect onboarding?

New developers clone one repository and run one install command to get everything. They can search all the code, see how pieces fit together and use the same scripts everywhere. On the other hand, a very big repo can be overwhelming, so good README files, a clear folder layout and owner info help.

## 123: Can different apps in a monorepo use different frameworks?

Yes. One monorepo can have a Next.js site, a Vite React admin app, an Express API and a React Native app. The task runner doesn't care what each package does, it just runs the scripts. Sharing code between them works best for framework-free code like types, validation schemas and helper functions.

## 124: Can a monorepo hold code in several languages?

Yes. Google's monorepo has C++, Java, Go, Python and more. In the JavaScript world, Nx has plugins for Go, Java (Gradle, Maven), .NET, Rust and others. Turborepo is mainly built around `package.json` scripts, so other languages need a small `package.json` wrapper. Bazel and Pants are built for many languages from the start.

## 125: What is Bazel?

Bazel is an open source build tool from Google, based on their internal tool Blaze. It builds and tests code in many languages with strict, sandboxed builds and remote caching and remote execution. It's very fast and reliable at huge scale but has a steep learning curve, and every build target is described in `BUILD` files.

## 126: What is Rush?

Rush is a monorepo manager from Microsoft for large JavaScript and TypeScript repos. It handles installs (usually with pnpm), incremental builds, version policies and publishing, and it has strict rules about dependency versions. It's used for big multi-team repos like the ones inside Microsoft.

## 127: What is moon?

moon is a monorepo build tool written in Rust. Like Nx and Turborepo, it has task graphs, caching and affected detection. It also manages tool versions (for example Node, Bun or Deno) through its sibling tool proto, so every developer and CI uses the same versions.

## 128: How do you pick between Turborepo and Nx?

Turborepo is small and easy to adopt: you add `turbo.json` and it runs your existing scripts with caching. Nx does more: inferred tasks, generators, module boundary rules, a graph UI, release tooling, plugins for many languages and distributed task running. A rough rule: if you want a fast task runner with little setup, start with Turborepo; if you want a full platform with structure and rules, pick Nx.

## 129: What is a "Version Packages" pull request?

It's a pull request opened by the Changesets GitHub Action. It contains the version bumps and changelog updates from all pending changesets. The team can keep merging features, and this pull request keeps updating. When you're ready to release, you merge it, and the action publishes the new versions.

## 130: What is a monorepo's "main" or "trunk" branch?

It's the single branch everyone merges into, usually `main`. In a monorepo it's shared by every team, so it must stay green. Most teams protect it with required checks, required reviews and often a merge queue so broken changes can't land.

## 131: What is a merge queue?

A merge queue tests each pull request against the latest `main` plus the other pull requests ahead of it before merging. Without it, two pull requests that pass on their own can break `main` when merged together. GitHub has a built-in merge queue, and it matters most in busy monorepos with many merges per hour.

## 132: How does a monorepo make dependency upgrades easier?

With one lockfile and one place to change versions (like pnpm catalogs), you upgrade a dependency once and CI tests every project that uses it. You fix breakages in the same pull request. In a polyrepo you'd repeat the upgrade in each repository, often months apart, and versions would drift.

## 133: How does a monorepo make dependency upgrades harder?

Because everyone shares versions, one upgrade must work for every project at once. If a major React upgrade breaks three apps, you can't merge until all three are fixed, or you have to allow two versions for a while. The more projects you have, the bigger each upgrade gets.

## 134: What is Renovate or Dependabot used for in a monorepo?

They open automatic pull requests to update dependencies. Both understand workspaces, so one pull request can update a dependency in every package that uses it. Renovate can also group related updates (for example all `@nx/*` packages) and understands pnpm catalogs, which keeps the number of pull requests manageable.

## 135: What is npx turbo prune used for?

It creates a smaller copy of the monorepo with just one app and the packages it needs, plus a trimmed lockfile:

```bash
npx turbo prune web --docker
```

It's used to build Docker images that don't contain the whole repo. The `--docker` flag splits the output into a `json` folder (for installing dependencies) and a `full` folder (for the source), which helps Docker cache layers.

## 136: How does Nx help build a Docker image for one app?

Nx can write a trimmed `package.json` and lockfile for one app, for example with the `generatePackageJson` option on some build executors or the `@nx/js:prune-lockfile` executor in newer versions. Then the Dockerfile installs only those dependencies and copies the built output. The goal is the same as `turbo prune`: don't ship the whole monorepo in every image.

## 137: Why shouldn't each app commit its own lockfile in a workspace?

The workspace already has one root lockfile that covers all packages. A second lockfile inside an app would not match the root one and would confuse tools and developers. If you need a lockfile for one app (for Docker), generate it with a tool like `turbo prune` instead of keeping it in Git.

## 138: What is a .npmrc used for in a pnpm monorepo?

`.npmrc` holds settings for the package manager, like the registry URL, auth tokens for private registries, or pnpm options. In pnpm 10 many workspace settings moved to `pnpm-workspace.yaml`, but `.npmrc` is still used for registry and auth config. Never commit real tokens; use an environment variable like `${NPM_TOKEN}`.

## 139: What is the files field in package.json?

`files` lists which files and folders go into the published tarball:

```json
{ "files": ["dist", "README.md"] }
```

Without it, npm publishes almost everything in the folder, including source and tests. In a monorepo this matters for publishable packages so you don't ship test fixtures or config files.

## 140: Can a monorepo have both public and private packages?

Yes. You mark internal ones with `"private": true` so they can't be published, and leave publishable ones public. Changesets and `nx release` skip private packages when publishing. Some teams also publish to a private registry for packages shared with other internal repos.

## 141: What is a scoped npm registry setting?

You can point one scope at a different registry in `.npmrc`:

```
@acme:registry=https://npm.pkg.github.com
//npm.pkg.github.com/:_authToken=${NPM_TOKEN}
```

Then `@acme/*` packages come from GitHub Packages while everything else comes from the public npm registry.

## 142: What is Verdaccio and why would you use it with a monorepo?

Verdaccio is a small self-hosted npm registry. With monorepos it's used for local testing of publishing: you start Verdaccio, publish your packages to it, then install them in a test project to make sure they work when consumed from a registry. Nx uses it in some of its generated setups for exactly this.

## 143: What is pnpm dlx or npx?

They download a package temporarily and run its binary without adding it to your dependencies. In monorepos you use them for one-off commands like `npx create-turbo@latest` or `npx @turbo/codemod migrate`. For tools the team uses every day, install them as root dev dependencies so the version is pinned.

## 144: Why is a consistent Node version important across a monorepo?

All packages run with the same Node during development and in CI. If one developer uses Node 20 and CI uses Node 24, you get different behavior and different cache keys. Teams pin the version with `.nvmrc`, the `engines` field, Volta, or the `packageManager` field together with Corepack for the package manager version.

## 145: What is the packageManager field?

It's a field in the root `package.json` that records which package manager and version the repo uses:

```json
{ "packageManager": "pnpm@10.12.1" }
```

Corepack reads it and uses that exact version. Turborepo also uses it to know which package manager the repo uses. It keeps everyone on the same version so lockfiles don't flip between formats.

## 146: What is Corepack?

Corepack is a tool that manages package manager versions based on the `packageManager` field. It has shipped with Node since version 16, but it's being removed from the default Node install starting with Node 25, so you may need to install it with `npm install -g corepack`. With it enabled, running `pnpm` or `yarn` uses the version the repo asks for.

## 147: How do you run a dev server for one app and its packages with Turborepo?

```bash
npx turbo run dev --filter=web...
```

The `...` after `web` includes the packages `web` depends on, so their `dev` scripts (like `tsc --watch`) start too. Without it, only `web`'s own `dev` runs.

## 148: What is turbo watch?

`turbo watch` re-runs tasks when files change, following the task graph:

```bash
npx turbo watch build lint
```

If you change `@acme/ui`, it reruns `ui#build` and then the tasks in packages that depend on it. It's useful for packages that don't have their own watch mode.

## 149: Why might a cached build in CI not match a local build?

The inputs that go into the cache key differ. Common reasons are different environment variables, different Node or package manager versions, different OS, or files that aren't committed. Turborepo and Nx both have ways to see what went into a hash so you can compare.

## 150: What should a README at the root of a monorepo cover?

It should explain how to install, the main scripts (`dev`, `build`, `test`, `lint`), the folder layout (`apps/`, `packages/`), how to add a new package, how releases work and who owns what. Each package can also have its own short README for its purpose and usage.

# Moderate Questions (151-300)

## 151: What goes into a Turborepo task hash?

The hash for a task is built from the task's input files (by default all Git-tracked files in the package), the `turbo.json` config for that task, the environment variables listed in `env`, the hashes of the tasks it depends on, the resolved versions of its external dependencies from the lockfile, and global inputs like `globalDependencies` and `globalEnv`. If any of these change, the hash changes and the task runs again.

## 152: What does the inputs key do in turbo.json?

`inputs` narrows which files count toward a task's hash. By default every tracked file in the package counts. For a test task you might only care about source and test files:

```json
{
  "tasks": {
    "test": {
      "inputs": ["$TURBO_DEFAULT$", "!README.md", "!docs/**"]
    }
  }
}
```

`$TURBO_DEFAULT$` keeps the default set, and the `!` patterns remove files, so editing the README no longer busts the test cache.

## 153: What does the env key do in turbo.json?

`env` lists environment variables that affect a task's output. Their values are added to the hash:

```json
{
  "tasks": {
    "build": {
      "env": ["API_URL", "NEXT_PUBLIC_*"],
      "outputs": [".next/**", "!.next/cache/**"]
    }
  }
}
```

If you build with `API_URL=staging` and then with `API_URL=prod`, you get two separate cache entries. Forgetting a variable here means a cache hit can return a build made with the wrong value.

## 154: What is strict environment mode in Turborepo?

In strict mode (the default since Turborepo 2.0), tasks only see environment variables that are listed in `env`, `globalEnv`, `passThroughEnv` or `globalPassThroughEnv`. Everything else is removed from the task's environment. This forces you to declare variables, so they can't affect output without being part of the hash. Loose mode (`--env-mode=loose`) passes all variables through and is easier but less safe.

## 155: What is the difference between env and passThroughEnv?

Variables in `env` are passed to the task and also included in the hash. Variables in `passThroughEnv` are passed to the task but not hashed. Use `passThroughEnv` for things that don't change the output, like a token needed to upload source maps or a CI-only flag that only changes logging.

## 156: What are globalDependencies and globalEnv?

They're root-level settings in `turbo.json` that affect every task's hash:

```json
{
  "globalDependencies": [".env", "tsconfig.base.json"],
  "globalEnv": ["NODE_ENV"],
  "tasks": {}
}
```

If any listed file or variable changes, every task gets a new hash. Use them for things that truly affect all packages, and keep the list short, because each entry can wipe out the cache for the whole repo.

## 157: How do you configure a task differently for one package in Turborepo?

Add a `turbo.json` inside that package that extends the root config:

```json
{
  "extends": ["//"],
  "tasks": {
    "build": {
      "outputs": ["storybook-static/**"]
    }
  }
}
```

`"//"` means the root workspace. Settings here override the root for that package only. This is called a package configuration.

## 158: How do you define a task that only runs in one specific package?

Use the `package#task` syntax in the root `turbo.json`:

```json
{
  "tasks": {
    "build": { "dependsOn": ["^build"] },
    "web#build": {
      "dependsOn": ["^build", "@acme/env#validate"],
      "env": ["NEXT_PUBLIC_API_URL"]
    }
  }
}
```

`web#build` overrides the generic `build` for the `web` package. You can also depend on a specific task in another package, like `@acme/env#validate`.

## 159: What are root tasks in Turborepo?

Root tasks are scripts in the root `package.json` that you want Turborepo to run and cache. You define them with the `//#` prefix:

```json
{
  "tasks": {
    "//#format:check": {}
  }
}
```

This runs the `format:check` script from the root `package.json`. It's useful for repo-wide checks like Prettier that don't belong to any one package.

## 160: How do you see what Turborepo would run without running it?

Use a dry run:

```bash
npx turbo run build --dry
npx turbo run build --dry=json
```

It prints every task it would run, with its hash, inputs, outputs, dependencies and whether it would be a cache hit. The JSON form is handy for scripts.

## 161: How do you debug a Turborepo cache miss?

Run with `--summarize`, which writes a JSON file in `.turbo/runs/` for each run. It lists every task with the hash of each input file, the env vars and the dependencies. Make two runs, then compare the two summaries to see which input changed. `--dry=json` gives similar info without running anything.

## 162: How do you filter Turborepo tasks by changed files?

Use a Git range in the filter:

```bash
npx turbo run test --filter="...[origin/main]"
npx turbo run lint --filter="[HEAD^1]"
```

`[origin/main]` means "packages with changes since origin/main". Adding `...` in front includes packages that depend on the changed ones, which is what you want for tests.

## 163: What do the different filter forms in Turborepo mean?

- `--filter=web` runs only in `web`.
- `--filter=web...` runs in `web` and its dependencies.
- `--filter=...web` runs in `web` and its dependents.
- `--filter=...^web` runs only in `web`'s dependents, not `web` itself.
- `--filter=./apps/*` runs in packages under that folder.
- `--filter=!docs` excludes `docs`.

You can pass several `--filter` flags, and the results are combined.

## 164: What does --continue do in Turborepo?

By default Turborepo stops when a task fails. With `--continue`, it keeps running tasks that don't depend on the failed one, so you see every failure in one CI run instead of fixing them one at a time. Newer versions also accept `--continue=dependencies-successful`, which only runs tasks whose dependencies all passed.

## 165: How do you limit parallel tasks in Turborepo?

```bash
npx turbo run test --concurrency=4
npx turbo run test --concurrency=50%
```

The default is 10. Lowering it helps when tasks are memory-heavy (like many Jest runs) and the machine runs out of RAM. `--concurrency=1` runs tasks one by one, which can help when debugging.

## 166: How do you set up Vercel Remote Cache for Turborepo?

```bash
npx turbo login
npx turbo link
```

`login` signs you in to Vercel and `link` connects the repo to a team. In CI you set `TURBO_TOKEN` (an access token) and `TURBO_TEAM` (the team slug) as environment variables, and Turborepo uses the remote cache automatically.

## 167: Can you self-host a Turborepo remote cache?

Yes. Turborepo's remote cache uses a documented HTTP API, so any server that implements it works. There are open source servers that store artifacts in S3, Google Cloud Storage or Azure. You point Turborepo at it with `--api` and `--token` flags, the `TURBO_API` and `TURBO_TOKEN` env vars, or the `remoteCache` settings in `turbo.json`.

## 168: How do you make sure remote cache artifacts can't be tampered with in Turborepo?

Turn on signatures:

```json
{
  "remoteCache": { "signature": true }
}
```

Then set `TURBO_REMOTE_CACHE_SIGNATURE_KEY` in the environment. Turborepo signs each artifact with an HMAC when uploading and checks the signature when downloading. If someone uploads a fake artifact without the key, it's rejected.

## 169: What are namedInputs in Nx?

`namedInputs` are reusable sets of file patterns defined in `nx.json`:

```json
{
  "namedInputs": {
    "default": ["{projectRoot}/**/*", "sharedGlobals"],
    "production": [
      "default",
      "!{projectRoot}/**/*.spec.ts",
      "!{projectRoot}/jest.config.ts"
    ],
    "sharedGlobals": ["{workspaceRoot}/tsconfig.base.json"]
  }
}
```

Tasks then refer to them by name in their `inputs`.

## 170: Why do Nx workspaces often have a "production" named input?

A build doesn't depend on test files, so editing a test shouldn't make a build cache miss. The `production` named input excludes spec files, test config and similar. Build targets use `"inputs": ["production", "^production"]`, meaning their own production files plus their dependencies' production files.

## 171: What do {projectRoot} and {workspaceRoot} mean in Nx config?

They're placeholders Nx replaces with real paths. `{projectRoot}` is the folder of the project the task belongs to, like `packages/ui`. `{workspaceRoot}` is the root of the repo. They let you write one rule in `nx.json` that works for every project:

```json
{ "outputs": ["{projectRoot}/dist"] }
```

## 172: What are targetDefaults in Nx?

`targetDefaults` in `nx.json` set default options for targets by name across all projects:

```json
{
  "targetDefaults": {
    "build": {
      "dependsOn": ["^build"],
      "inputs": ["production", "^production"],
      "outputs": ["{projectRoot}/dist"],
      "cache": true
    },
    "test": { "inputs": ["default", "^production"], "cache": true }
  }
}
```

Project-level config in `project.json` or `package.json` overrides them.

## 173: How does Nx merge task config from different places?

Nx builds a project's targets in layers. First, plugins infer targets from tool config files. Then `targetDefaults` from `nx.json` are applied. Then the project's own `project.json` or `package.json` `nx` field is applied last, so it wins. `nx show project <name>` shows the final result and where each setting came from.

## 174: How do you add Nx settings in package.json instead of project.json?

Use the `nx` field:

```json
{
  "name": "@acme/ui",
  "scripts": { "build": "tsup" },
  "nx": {
    "tags": ["type:ui"],
    "targets": {
      "build": { "outputs": ["{projectRoot}/dist"] }
    }
  }
}
```

This is common in package-based repos where you don't want an extra file per project.

## 175: How do you set the base for nx affected in CI?

Nx needs a base commit to compare against. In GitHub Actions the `nrwl/nx-set-shas` action finds the last commit on `main` where CI passed and sets `NX_BASE` and `NX_HEAD`:

```yaml
- uses: nrwl/nx-set-shas@v4
- run: npx nx affected -t lint test build
```

Using the last green commit instead of just the previous commit means a failed run's changes still get tested next time.

## 176: Why does nx affected need full Git history in CI?

Nx compares the base and head commits. Many CI systems do a shallow clone with only the latest commit, so the base commit isn't there and Nx can't compute the diff. In GitHub Actions you set `fetch-depth: 0` on `actions/checkout` so the history is available.

## 177: How do you connect an Nx workspace to Nx Cloud?

```bash
npx nx connect
```

This adds an `nxCloudId` to `nx.json` and links the workspace to Nx Cloud, which gives you remote caching and run insights. In CI, Nx reads the access token from the `NX_CLOUD_ACCESS_TOKEN` environment variable when you need one.

## 178: What is nx migrate?

`nx migrate` upgrades Nx and its plugins, and runs code migrations that update your config and code for the new version:

```bash
npx nx migrate latest
pnpm install
npx nx migrate --run-migrations
```

The first step updates `package.json` and writes a `migrations.json`. The last step applies the migrations. It handles breaking changes for you, which is why it's better than bumping versions by hand.

## 179: What is nx sync?

`nx sync` runs sync generators that keep generated config files in line with the project graph. The common case is TypeScript project references: when you add a dependency between two projects, `nx sync` adds the matching `references` entry to `tsconfig.json`. `nx sync:check` fails in CI if files are out of date.

## 180: What is nx release?

`nx release` is Nx's built-in tool for versioning, changelogs and publishing:

```bash
npx nx release --dry-run
npx nx release
```

It can work out version bumps from conventional commits or ask you, update `package.json` versions and internal dependency ranges, write changelogs, create Git tags and GitHub releases, and publish to npm. It supports fixed and independent versioning through `release.projectsRelationship` in `nx.json`.

## 181: How do you run a pnpm command for packages changed since main?

```bash
pnpm --filter "...[origin/main]" test
pnpm --filter "[origin/main]" lint
```

`[origin/main]` selects packages with changed files since that ref. The leading `...` adds their dependents. This gives you basic affected testing with only pnpm.

## 182: What does pnpm --filter "...^web" mean?

The `^` means "exclude the package itself". So `...^web` selects everything that depends on `web` but not `web` itself, and `web^...` selects `web`'s dependencies without `web`. It's handy when you want to build a package's dependencies before starting its dev server.

## 183: What is pnpm deploy?

`pnpm deploy` copies one workspace package and its production dependencies into a separate folder with a real `node_modules`, with no symlinks back into the monorepo:

```bash
pnpm --filter @acme/api deploy --prod out/api
```

It's useful for Docker images and serverless bundles. In pnpm 10 it needs `inject-workspace-packages=true` or the `--legacy` flag, so check the docs for your version.

## 184: How do you publish all changed packages with pnpm?

```bash
pnpm publish -r
```

It publishes every public workspace package whose version isn't on the registry yet, in dependency order, and replaces `workspace:` ranges with real versions. Usually Changesets or `nx release` calls this for you after bumping versions.

## 185: What is the difference between workspace:*, workspace:^ and workspace:~?

They all link the local package. The difference shows up when publishing. `workspace:*` becomes the exact version, like `1.4.2`. `workspace:^` becomes `^1.4.2`, and `workspace:~` becomes `~1.4.2`. For publishable libraries, `workspace:^` is a common choice so consumers can get compatible patch and minor updates.

## 186: What are pnpm overrides?

Overrides force a specific version of a dependency anywhere in the tree:

```yaml
# pnpm-workspace.yaml
overrides:
  "semver@<7.5.2": ">=7.5.2"
  "lodash": "4.17.21"
```

They're used to fix security issues in deep dependencies or remove duplicates. In pnpm 10 they live in `pnpm-workspace.yaml` (older versions used the `pnpm.overrides` field in the root `package.json`). npm has the `overrides` field and Yarn has `resolutions`.

## 187: What are named catalogs in pnpm?

Besides the default `catalog`, you can define several named catalogs:

```yaml
catalogs:
  react18:
    react: ^18.3.1
    react-dom: ^18.3.1
  react19:
    react: ^19.1.0
    react-dom: ^19.1.0
```

```json
{ "dependencies": { "react": "catalog:react18" } }
```

This helps during migrations, when some apps are on the old version and some on the new one, while still keeping each group in sync.

## 188: What is the catalogMode setting in pnpm?

`catalogMode` controls what happens when you run `pnpm add` for a package that's in a catalog. With `strict`, pnpm only allows the catalog version. With `prefer`, it uses the catalog version when it can. With `manual` (the default), it doesn't use the catalog unless you write `catalog:` yourself. Setting it helps stop people from adding versions that don't match.

## 189: What are Yarn constraints?

Yarn Berry has a `yarn constraints` command that checks rules about your workspaces' `package.json` files. You write the rules in a `yarn.config.cjs` file in JavaScript, for example "every workspace must use the same version of React" or "every package must have a license field". `yarn constraints --fix` fixes what it can automatically.

## 190: What is Yarn Plug'n'Play and how does it affect monorepos?

Plug'n'Play (PnP) is Yarn Berry's install mode that skips `node_modules` entirely. Yarn writes a `.pnp.cjs` file that tells Node where each package lives. It's strict, so phantom dependencies fail, and installs are fast. Some tools don't support it well, so many monorepos set `nodeLinker: node-modules` in `.yarnrc.yml` to get a normal layout.

## 191: What does nodeLinker do in pnpm?

The `nodeLinker` setting changes how pnpm lays out `node_modules`. The default `isolated` uses symlinks into `.pnpm`. `hoisted` makes a flat `node_modules` like npm, which helps with tools that break on symlinks, like some React Native setups. `pnp` uses Plug'n'Play. Most repos stay on the default and only switch when a tool forces them.

## 192: What do shamefully-hoist and public-hoist-pattern do in pnpm?

`shamefully-hoist=true` hoists everything to the root `node_modules`, like npm. It fixes tools that rely on phantom dependencies but loses pnpm's strictness. `public-hoist-pattern` hoists only matching packages, for example `*eslint*` or `*prettier*`, which some editor plugins need. Use the narrow one when possible.

## 193: How do you check that all packages use the same dependency versions?

Some options:

- pnpm catalogs, so packages don't write versions at all.
- `syncpack`, a tool that lists and fixes mismatched versions across `package.json` files.
- Yarn constraints.
- Nx's `@nx/dependency-checks` ESLint rule, which checks that a project's `package.json` matches what its code imports.

Running one of these in CI stops drift.

## 194: What is syncpack?

syncpack is a CLI that finds and fixes dependency version mismatches across a monorepo's `package.json` files:

```bash
npx syncpack list-mismatches
npx syncpack fix-mismatches
```

It can also enforce rules, like "all `@types/*` must be dev dependencies" or "pin these packages to exact versions", through a config file.

## 195: How do you run Jest across a monorepo?

The usual approach is to give each package its own Jest config and `test` script, and let Turborepo or Nx run them with caching. Jest also has a `projects` option in a root config that runs many configs in one process, but then you lose per-package caching. Most teams prefer per-package scripts.

## 196: How do you run Vitest across a monorepo?

Like Jest, each package can have its own `vitest.config.ts` and `test` script, run by the task runner. Vitest also supports running several projects in one process with the `projects` option in the root config (older versions used a `vitest.workspace` file, which is now deprecated):

```js
import { defineConfig } from "vitest/config";

export default defineConfig({
  test: { projects: ["packages/*", "apps/*"] },
});
```

## 197: How does Next.js use a workspace package that ships TypeScript source?

Next.js doesn't compile files from `node_modules` by default. You list the package in `transpilePackages`:

```js
// apps/web/next.config.js
export default {
  transpilePackages: ["@acme/ui"],
};
```

Then Next.js compiles `@acme/ui`'s TypeScript and JSX along with the app.

## 198: How does Vite handle workspace packages?

Vite treats linked workspace packages (resolved outside `node_modules` through symlinks) as source code, so it transforms them and watches them for changes during dev. That's why source-only internal packages usually work in Vite without extra config. If a linked package is pre-bundled or excluded in a strange way, the `optimizeDeps.include` and `optimizeDeps.exclude` options control that.

## 199: How do you handle environment variables in a monorepo?

Keep `.env` files per app, not at the root, so each app only gets what it needs. List the variables that change build output in `turbo.json` `env` (or Nx inputs) so caching is correct. Validate them at startup with a schema (for example with `zod`) in a shared `@acme/env` package. Never commit real secrets; commit an `.env.example` instead.

## 200: How do you share validated env config between apps?

Create a small package that validates env vars with a schema and exports a typed object:

```js
// packages/env/src/index.js
import { z } from "zod";

const schema = z.object({
  DATABASE_URL: z.string().url(),
  NODE_ENV: z.enum(["development", "test", "production"]),
});

export const env = schema.parse(process.env);
```

Each server app imports it, and a missing or wrong variable fails fast at startup instead of at the first request.

## 201: How do you set up a GitHub Actions workflow for a Turborepo monorepo?

```yaml
name: CI
on: [pull_request]

jobs:
  ci:
    runs-on: ubuntu-latest
    env:
      TURBO_TOKEN: ${{ secrets.TURBO_TOKEN }}
      TURBO_TEAM: ${{ vars.TURBO_TEAM }}
    steps:
      - uses: actions/checkout@v4
        with:
          fetch-depth: 0
      - uses: pnpm/action-setup@v4
      - uses: actions/setup-node@v4
        with:
          node-version: 22
          cache: pnpm
      - run: pnpm install --frozen-lockfile
      - run: pnpm turbo run lint test build --affected
```

The remote cache env vars make builds from other runs reusable, and `--affected` limits work to changed packages.

## 202: How do you set up a GitHub Actions workflow for an Nx monorepo?

```yaml
jobs:
  main:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
        with:
          fetch-depth: 0
      - uses: pnpm/action-setup@v4
      - uses: actions/setup-node@v4
        with:
          node-version: 22
          cache: pnpm
      - run: pnpm install --frozen-lockfile
      - uses: nrwl/nx-set-shas@v4
      - run: pnpm nx affected -t lint test build
```

If the workspace is connected to Nx Cloud, remote caching works without extra steps.

## 203: Without a remote cache, how can you cache Turborepo results in GitHub Actions?

Cache the `.turbo/cache` folder with `actions/cache`:

```yaml
- uses: actions/cache@v4
  with:
    path: .turbo/cache
    key: ${{ runner.os }}-turbo-${{ github.sha }}
    restore-keys: |
      ${{ runner.os }}-turbo-
```

The key includes the commit SHA so each run saves a new entry, and `restore-keys` picks up the most recent older one. It works, but the folder can grow large, so a real remote cache is usually better.

## 204: How do you build a Docker image for one app with turbo prune?

```dockerfile
FROM node:22-alpine AS base
RUN corepack enable

FROM base AS pruner
WORKDIR /app
COPY . .
RUN npx turbo@^2 prune web --docker

FROM base AS builder
WORKDIR /app
COPY --from=pruner /app/out/json/ .
RUN pnpm install --frozen-lockfile
COPY --from=pruner /app/out/full/ .
RUN pnpm turbo run build --filter=web

FROM base AS runner
WORKDIR /app
COPY --from=builder /app .
CMD ["node", "apps/web/server.js"]
```

Installing from `out/json` first means Docker reuses the `node_modules` layer when only source files change. For Next.js, the `output: "standalone"` option lets you copy a much smaller set of files into the final stage.

## 205: Why do you copy package.json files before source code in a Dockerfile?

Docker caches each layer and rebuilds from the first layer that changed. If you copy only `package.json` files and the lockfile, then install, that install layer stays cached until dependencies change. Source code changes then only rebuild the later layers. In a monorepo, `turbo prune --docker` gives you exactly those files in `out/json`.

## 206: What does Changesets config.json look like?

```json
{
  "$schema": "https://unpkg.com/@changesets/config@3.1.1/schema.json",
  "changelog": "@changesets/cli/changelog",
  "commit": false,
  "fixed": [],
  "linked": [],
  "access": "restricted",
  "baseBranch": "main",
  "updateInternalDependencies": "patch",
  "ignore": []
}
```

`access` is `restricted` by default; set it to `public` for public scoped packages. `baseBranch` is what changesets compare against.

## 207: What do fixed and linked mean in Changesets?

`fixed` groups packages that always share the same version. If one is bumped, all are bumped to the same new version. `linked` groups packages that share the highest bump type and version number when they're released together, but a package that has no changes isn't bumped. Use `fixed` for packages that must always move together, like a framework and its core plugins.

## 208: What does updateInternalDependencies do in Changesets?

When package A depends on package B and B gets a new version, this setting decides when A's dependency range is updated. With `"patch"` (the default), A's range is updated on any bump of B. With `"minor"`, it's only updated when B's new version falls outside A's current range. Updating A's range also causes a patch bump for A.

## 209: How do you make prereleases with Changesets?

Enter pre mode, then version and publish as usual:

```bash
npx changeset pre enter beta
npx changeset version   # 2.0.0-beta.0
npx changeset publish --tag beta
npx changeset pre exit
```

While in pre mode, versions get a `-beta.N` suffix. Exiting pre mode makes the next `version` produce normal versions.

## 210: What are snapshot releases in Changesets?

Snapshot releases publish temporary versions for testing, without changing the real version history:

```bash
npx changeset version --snapshot pr-123
npx changeset publish --tag pr-123 --no-git-tag
```

Versions look like `0.0.0-pr-123-20261125120000`. Teams use them to let someone try a package from a pull request before it's merged.

## 211: How does Lerna version packages?

```bash
npx lerna version --conventional-commits
npx lerna publish from-git
```

`lerna version` finds packages that changed since the last release, bumps their versions (asking you or using conventional commits), updates internal dependencies, commits and tags. `lerna publish from-git` publishes the packages tagged in the current commit. In `lerna.json`, `"version": "independent"` switches to independent mode.

## 212: What are conventional commits and how do release tools use them?

Conventional commits are commit messages that follow a format like `feat(ui): add tooltip` or `fix(api): handle empty body`. Tools like `nx release`, Lerna and semantic-release read them to decide version bumps: `fix` means patch, `feat` means minor, and `BREAKING CHANGE` or `!` means major. The scope tells which package changed.

## 213: How do you enforce conventional commit messages in a monorepo?

Use commitlint with a Git hook:

```bash
pnpm add -D @commitlint/cli @commitlint/config-conventional -w
```

```js
// commitlint.config.js
export default { extends: ["@commitlint/config-conventional"] };
```

Run it in a `commit-msg` hook (with husky or lefthook) and in CI for pull request titles if you squash merge.

## 214: How do you run lint only on staged files in a monorepo?

Use lint-staged in a pre-commit hook:

```json
{
  "lint-staged": {
    "*.{js,ts,tsx}": ["eslint --fix", "prettier --write"],
    "*.{json,md,yml}": "prettier --write"
  }
}
```

It runs the commands only on the files you're committing, so the hook stays fast even in a big repo.

## 215: How do you run ESLint across a monorepo efficiently?

Give each package a `lint` script and let the task runner run them in parallel with caching. Only affected packages get linted on pull requests. A single root ESLint run over the whole repo is simpler but can't be cached per package and gets slow as the repo grows. ESLint's own `--cache` flag helps a bit locally.

## 216: Should each package have its own ESLint config file?

With ESLint flat config, you can have one root `eslint.config.js` with per-folder overrides, or a small `eslint.config.js` in each package that imports a shared config. Per-package files work better with per-package lint tasks and caching, because each package's lint only depends on its own files and the shared config package.

## 217: How do you type-check a whole monorepo with TypeScript project references?

Make a root `tsconfig.json` that only references packages:

```json
{
  "files": [],
  "references": [
    { "path": "packages/utils" },
    { "path": "packages/ui" },
    { "path": "apps/web" }
  ]
}
```

Then run `tsc -b`. TypeScript builds each project in dependency order and skips projects whose inputs haven't changed, using `.tsbuildinfo` files.

## 218: Why does tsc -b need references to match package dependencies?

TypeScript doesn't read `package.json` dependencies. If `ui` imports `utils` but `ui/tsconfig.json` has no reference to `utils`, `tsc -b` may build `ui` before `utils`, or use stale `.d.ts` files. Keeping references in sync by hand is error-prone, which is why Nx has `nx sync` and why some teams write a script to generate them.

## 219: How do you make editors jump to source instead of .d.ts files in a monorepo?

With compiled packages, "go to definition" lands in `dist/index.d.ts`. Options:

- Turn on `declarationMap: true`, so `.d.ts.map` files point back to the source.
- Use source-only packages whose `exports` point to `.ts` files.
- Use a custom export condition that points to source during development.

Declaration maps are the simplest fix for compiled packages.

## 220: What are custom export conditions and how do they help in monorepos?

You can add your own condition name to `exports`:

```json
{
  "exports": {
    ".": {
      "@acme/source": "./src/index.ts",
      "default": "./dist/index.js"
    }
  }
}
```

Then you tell TypeScript (`customConditions` in `tsconfig.json`) and your bundler (Vite `resolve.conditions`) to use `@acme/source`. In the monorepo, tools read source directly; published consumers get `dist`. Nx uses this approach in its newer TypeScript setups.

## 221: How do you build a library package with tsup?

```json
{
  "name": "@acme/utils",
  "type": "module",
  "exports": {
    ".": { "types": "./dist/index.d.ts", "import": "./dist/index.js" }
  },
  "scripts": { "build": "tsup src/index.ts --format esm --dts" }
}
```

tsup bundles with esbuild and writes `.d.ts` files with `--dts`. It's a common pick for small packages because it needs almost no config. tsdown is a newer tool with a similar idea.

## 222: How do you share React components between two apps?

Put them in a package like `packages/ui`, list `react` and `react-dom` as peer dependencies, and add the package to each app with `workspace:*`. Either compile it with tsup or let each app compile the source (`transpilePackages` in Next.js). Keep app-specific logic out of it, so the components stay reusable.

## 223: How do you share styles like Tailwind CSS between packages?

With Tailwind CSS v4, you can put shared theme variables in a CSS file in a package and import it in each app. Each app's CSS must also tell Tailwind to scan the shared package for class names, for example with `@source "../../packages/ui/src";`. If you forget, classes used only in the shared components won't be generated.

## 224: How do you share TypeScript types between frontend and backend?

Make a package like `@acme/types` or `@acme/contracts` with shared types and, better, runtime schemas:

```js
// packages/contracts/src/user.js
import { z } from "zod";

export const User = z.object({
  id: z.string(),
  email: z.string().email(),
});
```

The API uses the schema to validate requests, and the frontend uses the same schema (and inferred types) for forms. Changing a field breaks both sides at compile time in the same pull request.

## 225: How do you set up Storybook in a monorepo?

Common options are one Storybook in the UI package that shows its components, or one central Storybook app that loads stories from several packages with globs in `.storybook/main.js`. The central one gives one place to browse everything, but its build depends on many packages. Cache the `build-storybook` task and list `storybook-static/**` as its output.

## 226: How do you share test helpers across packages?

Create a package like `@acme/test-utils` with custom render functions, mock factories and fixtures, and add it as a dev dependency where needed:

```json
{ "devDependencies": { "@acme/test-utils": "workspace:*" } }
```

Keep it a dev dependency so it never ends up in production bundles.

## 227: How do you share a database schema or ORM client between services?

Put the schema and generated client in one package, like `@acme/db`, and have services depend on it. The package's `build` (or a `generate` task) runs the ORM's code generation, and other tasks depend on it with `dependsOn`. Only one package owns migrations, so two services can't fight over the database structure.

## 228: How do you make a generate task run before build in Turborepo?

```json
{
  "tasks": {
    "db:generate": { "cache": false },
    "build": {
      "dependsOn": ["^build", "^db:generate"],
      "outputs": ["dist/**"]
    }
  }
}
```

`^db:generate` makes every package that depends on `@acme/db` wait for its generate step. You might cache `db:generate` if its outputs are listed and its inputs are just the schema file.

## 229: How do you handle circular dependencies between packages?

Package managers allow cycles, but task runners can't order them, and they make the code hard to reason about. Turborepo reports an error for cycles in the task graph, and Nx's graph and lint rules flag circular imports. The fix is to move the shared part into a new, lower-level package that both can depend on, or to merge the two packages.

## 230: How do you find circular imports in Nx?

The `@nx/enforce-module-boundaries` ESLint rule reports circular dependencies between projects by default. `nx graph` also shows them visually. For import cycles inside one package, tools like `madge --circular` work at the file level.

## 231: What does nx show project web --web do?

It opens the project details view in the browser for the `web` project. You see every target, including inferred ones, with their inputs, outputs, cache settings and the source of each setting (plugin, `targetDefaults` or project config). It's one of the fastest ways to understand why a task behaves a certain way.

## 232: How do Nx plugins infer targets?

A plugin exports a `createNodesV2` function with a glob, like `**/vite.config.{js,ts}`. Nx calls it with every matching file, and the plugin returns target definitions for the projects those files belong to. Plugins are listed in `nx.json`:

```json
{
  "plugins": [
    { "plugin": "@nx/vite/plugin", "options": { "buildTargetName": "build" } }
  ]
}
```

## 233: How do you exclude some projects from an Nx plugin?

Use `include` and `exclude` globs on the plugin entry:

```json
{
  "plugins": [
    {
      "plugin": "@nx/jest/plugin",
      "include": ["packages/**/*"],
      "exclude": ["packages/legacy/**/*"]
    }
  ]
}
```

That way you can use one plugin for most projects and handle special ones by hand.

## 234: How do you run tasks for projects with a certain tag in Nx?

```bash
npx nx run-many -t test --projects=tag:scope:checkout
npx nx affected -t build --exclude=tag:type:e2e
```

`--projects` and `--exclude` accept tags, names and glob patterns, so you can run tasks for one team's projects or skip slow ones.

## 235: How do Nx tags map to an architecture?

A common setup uses two dimensions. `scope:*` says which business area a project belongs to (`scope:shop`, `scope:admin`, `scope:shared`). `type:*` says what kind of code it is (`type:app`, `type:feature`, `type:ui`, `type:data-access`, `type:util`). Boundary rules then say, for example, `scope:shop` can only use `scope:shop` and `scope:shared`, and `type:util` can only use other `type:util`.

## 236: Can you enforce module boundaries without Nx?

Yes, with other tools:

- ESLint's `no-restricted-imports` with patterns.
- `eslint-plugin-boundaries`, which defines element types by folder.
- dependency-cruiser, which checks import rules from a config file.
- Turborepo's `turbo boundaries` command (experimental), which checks for imports of undeclared packages and supports tag rules.

Package `exports` also stop deep imports into a package's internal files.

## 237: What is turbo boundaries?

`turbo boundaries` is a Turborepo command (experimental) that checks imports across packages. It reports imports of files outside the package's folder and imports of packages that aren't listed in its `package.json`. You can also give packages tags in their `turbo.json` and write allow and deny rules between tags, similar to Nx module boundaries.

## 238: How do you migrate an existing repo into a monorepo without losing Git history?

Move the old repo's files into a subfolder in a branch of that repo, then merge that branch into the monorepo with `--allow-unrelated-histories`:

```bash
# in the old repo
git filter-repo --to-subdirectory-filter apps/billing
# in the monorepo
git remote add billing ../billing
git fetch billing
git merge billing/main --allow-unrelated-histories
```

`git filter-repo` rewrites history so every old commit looks like it touched `apps/billing`, so `git log` on that folder shows the full history.

## 239: What is nx import?

`nx import` brings another repository into an Nx workspace, keeping its Git history:

```bash
npx nx import https://github.com/acme/billing apps/billing
```

It moves the files into the target folder, merges history, and can detect which Nx plugins the imported code needs. It saves you from doing the `git filter-repo` steps by hand.

## 240: How do you split a package out of a monorepo into its own repo?

Use `git filter-repo` (or the older `git subtree split`) to make a new history with only that folder:

```bash
git clone acme acme-ui
cd acme-ui
git filter-repo --subdirectory-filter packages/ui
```

The result is a repo where `packages/ui` is the root and only commits touching it remain. You then replace its `workspace:` dependencies with real versions.

## 241: What is Git sparse checkout?

Sparse checkout lets you have only some folders of a repo in your working tree:

```bash
git clone --filter=blob:none --sparse https://github.com/acme/monorepo
cd monorepo
git sparse-checkout set apps/web packages/ui packages/utils
```

You still have the full history, but only the listed folders are on disk. In a huge monorepo this makes checkout and editor indexing much faster.

## 242: What is a partial clone?

A partial clone (`git clone --filter=blob:none`) downloads all commits and trees but skips file contents until you need them. Git fetches blobs on demand when you check out or look at a file. Combined with sparse checkout, it makes cloning big monorepos fast without losing the ability to see history.

## 243: How do you keep VS Code fast in a big monorepo?

Exclude build and cache folders from search and file watching:

```json
{
  "files.watcherExclude": {
    "**/node_modules/**": true,
    "**/dist/**": true,
    "**/.turbo/**": true,
    "**/.nx/**": true
  },
  "search.exclude": { "**/dist": true, "**/.next": true }
}
```

You can also open only the folders you work on with a multi-root workspace file, and use TypeScript project references so the language server doesn't load every file.

## 244: What is a multi-root workspace in VS Code?

It's a `.code-workspace` file that opens several folders as separate roots:

```json
{
  "folders": [{ "path": "apps/web" }, { "path": "packages/ui" }]
}
```

Each root can have its own settings. In a monorepo it lets a developer open just the parts they work on, while still being in one Git repo.

## 245: How do you run e2e tests in a monorepo?

Put e2e tests in their own project, like `apps/web-e2e`, that depends on the app it tests. In Turborepo, its `test:e2e` task depends on `web#build`. In Nx, the e2e project has an implicit dependency on `web`. That way e2e tests run when the app or anything it uses changes, and not otherwise.

## 246: What are implicitDependencies in Nx?

`implicitDependencies` add graph edges Nx can't see from imports:

```json
{
  "name": "web-e2e",
  "implicitDependencies": ["web"]
}
```

Now changes to `web` mark `web-e2e` as affected even though the e2e project never imports `web`'s code. You can also remove an edge with `"!project-name"`.

## 247: How do you make a non-JavaScript file affect a task's cache?

Add it to the task's inputs. In Turborepo, a file outside the package can be added with `$TURBO_ROOT$`:

```json
{
  "tasks": {
    "build": { "inputs": ["$TURBO_DEFAULT$", "$TURBO_ROOT$/config/brand.json"] }
  }
}
```

In Nx, use `{workspaceRoot}/config/brand.json` in `inputs` or in a named input like `sharedGlobals`.

## 248: How do you make a task depend on a tool version in Nx?

Use a runtime input, which runs a command and hashes its output:

```json
{
  "targetDefaults": {
    "build": {
      "inputs": ["production", "^production", { "runtime": "node --version" }]
    }
  }
}
```

Now upgrading Node changes the hash and the build reruns. Nx also supports `{ "env": "API_URL" }` and `{ "externalDependencies": ["vite"] }` inputs.

## 249: What are externalDependencies inputs in Nx?

They tell Nx to hash only specific npm packages instead of all of them:

```json
{
  "inputs": [
    "default",
    { "externalDependencies": ["eslint", "typescript-eslint"] }
  ]
}
```

For a `run-commands` lint task, Nx can't know which tools it uses, so by default it hashes all external dependencies, which means any upgrade busts the cache. Listing just the ones the task uses keeps caching precise.

## 250: What does dependentTasksOutputFiles do in Nx?

It's an input type that hashes the output files of the tasks this task depends on, instead of their source:

```json
{ "inputs": [{ "dependentTasksOutputFiles": "**/*.d.ts", "transitive": true }] }
```

For example, a type-check task only cares about the `.d.ts` files its dependencies produced. If a dependency's code changes but its public types don't, the type-check stays cached.

## 251: How do you debug why a project is affected in Nx?

Run `nx show projects --affected` to list them, and use `nx graph --affected` to see them in the graph with the changed projects highlighted. Usually the cause is a change in a shared file listed in `sharedGlobals`, a lockfile change, or a dependency you didn't know about. Setting `NX_VERBOSE_LOGGING=true` gives more detail about how the graph was built.

## 252: Why does changing the lockfile sometimes mark everything as affected?

The lockfile holds the versions of all external dependencies. Turborepo and Nx try to work out which packages use the changed dependency and only mark those, but some changes (like a root dev dependency or a package used everywhere) really do affect every project. If the tool can't parse the lockfile change, it may play it safe and mark everything.

## 253: How do you avoid one global config file busting all caches?

Keep global inputs small and specific. Instead of listing a big root `tsconfig.json` as a global input, split shared settings into small files and list only the relevant one for each task. Avoid putting frequently changing files (like a root README or a changelog) into `globalDependencies` or Nx `sharedGlobals`.

## 254: How do you handle a package that needs different build outputs for different apps?

Usually you don't. Build the package once in a neutral way (plain ESM, no app-specific env) and let each app's bundler do the rest. If the outputs really must differ, use separate tasks (`build:web`, `build:mobile`) with their own outputs, or pass the difference through an env var listed in `env` so each variant gets its own cache entry.

## 255: What is the problem with relative imports across packages?

An import like `import { x } from "../../packages/utils/src"` bypasses the package system. The task runner doesn't see the dependency, so build order and affected detection are wrong. Package boundaries and `exports` are ignored. Always import other packages by their name, like `@acme/utils`, and lint against cross-package relative imports.

## 256: How do you prevent deep imports into another package's internals?

Define `exports` in the package's `package.json` so only the public entry points can be imported:

```json
{
  "exports": {
    ".": "./dist/index.js",
    "./testing": "./dist/testing.js"
  }
}
```

An import like `@acme/utils/dist/internal/cache.js` then fails to resolve. Nx's boundary rule also flags deep imports by default.

## 257: How do you version an internal package that's never published?

Many teams just leave it at `0.0.0` and always use `workspace:*`, because every consumer always uses the current code in the same commit. The version number carries no meaning for internal packages. Changesets ignores private packages for publishing, and you can use its `ignore` option to skip them completely.

## 258: How does a monorepo deploy only the apps that changed?

The CI job runs a check like `turbo run build --affected` or `nx affected -t deploy`, so only affected apps get built and deployed. Vercel and Netlify also have "ignored build step" checks for monorepos, for example `npx turbo-ignore`, which skips a deploy if the app and its dependencies didn't change.

## 259: What is turbo-ignore?

`turbo-ignore` is a small CLI that exits with a code telling the hosting platform whether to build. Run in an app's folder, it checks whether that app or any package it depends on changed since the last deploy. Vercel uses it in the "Ignored Build Step" setting so pushes that only touch other apps don't trigger a redeploy.

## 260: How do you deploy several apps from one monorepo on Vercel?

Create one Vercel project per app and set each project's root directory, like `apps/web` or `apps/docs`. Vercel detects the monorepo, installs from the root and builds with the package manager and Turborepo. Each project can have its own env vars, domains and ignored build step.

## 261: How do you deploy a Node.js service from a monorepo to a container platform?

Build a Docker image that contains only that service and the packages it needs, using `turbo prune --docker`, `pnpm deploy`, or a bundler that outputs a single file (like esbuild with all workspace packages inlined). Push the image to a registry and deploy it. CI decides which services to build based on affected detection.

## 262: Why bundle a Node.js service with esbuild in a monorepo?

Bundling the service's code and its workspace packages into one file removes the need for symlinked `node_modules` at runtime:

```bash
esbuild apps/api/src/main.js --bundle --platform=node --format=esm \
  --outfile=apps/api/dist/main.js --external:pg --external:sharp
```

Your own workspace packages get inlined, and only packages you mark as external (usually ones with native code) need to be installed in the image. Be careful with `--packages=external`: it marks every bare import as external, including your own `@acme/*` packages, so they wouldn't be bundled. This makes Docker images and serverless deploys simpler.

## 263: How do you handle native modules in a monorepo Docker image?

Native modules (like `sharp` or `bcrypt`) are compiled for a specific OS and CPU. Install dependencies inside the same base image you run in, not on your Mac, and don't copy a local `node_modules` into the image. With pnpm, `supportedArchitectures` in the workspace config can install binaries for several platforms when you need to.

## 264: What is the difference between npm ci and npm install in a workspace?

`npm ci` deletes `node_modules` and installs exactly what's in `package-lock.json`, failing if it doesn't match `package.json`. It never writes to the lockfile. `npm install` can update the lockfile. Use `npm ci` in CI so builds are reproducible.

## 265: How do you install only one workspace's dependencies in CI?

With pnpm:

```bash
pnpm install --frozen-lockfile --filter web...
```

This installs dependencies for `web` and the workspace packages it depends on. With npm, `npm ci --workspace=apps/web` also limits the install, though npm still installs the root's dependencies. It's useful for jobs that only touch one app.

## 266: What is the root node_modules/.bin and how do workspace scripts find binaries?

Package managers put command-line tools from dependencies in `node_modules/.bin`. When you run a script in a workspace, the package manager adds the package's own `.bin` and the root `.bin` to `PATH`. So a tool installed at the root, like `tsc` or `eslint`, can be used in any workspace's scripts.

## 267: Should shared dev tools be installed at the root or in each package?

Common practice is to install repo-wide tools (Turborepo, Prettier, husky, Changesets) at the root, and tools a package's own scripts use (TypeScript, Vitest, ESLint) in that package. Listing them per package is more accurate: the task runner knows which package uses which tool, and the package can be extracted later. Catalogs keep the versions the same.

## 268: How do you give each package its own scripts but keep them consistent?

Write the same script names in every package (`build`, `dev`, `test`, `lint`, `typecheck`) so the task runner can run them all. Use shared config packages so the commands are short. Nx generators or a template folder help create new packages with the same scripts. A CI check or Yarn constraints can verify every package has the required scripts.

## 269: What is a typecheck task and why separate it from build?

Some builds (esbuild, SWC, Vite) strip types without checking them, so a separate `typecheck` script runs `tsc --noEmit`. In a monorepo, it's its own cached task with its own inputs. It can depend on `^build` if it needs `.d.ts` files from dependencies, or run against source if packages use project references.

## 270: How do you speed up TypeScript checks in a monorepo?

Use project references and `tsc -b` so unchanged projects are skipped. Turn on `incremental` so `.tsbuildinfo` files are reused. Run type checks as cached tasks per package. Avoid one huge `tsconfig.json` that includes every file in the repo. TypeScript 7, the native Go port, also makes type checking much faster when your setup can use it.

## 271: How do you share a Prettier config in a monorepo?

Put one `.prettierrc` (or `prettier.config.js`) and `.prettierignore` at the root. Prettier looks up the folder tree for config, so every package uses it. Run Prettier from the root with one command; there's little gain in running it per package. If some packages need different settings, use `overrides` in the root config.

## 272: What are the trade-offs of fixed versioning for published packages?

Fixed versioning is simple to explain: every package has the same version, and users know which versions go together. The downside is that packages get new versions with no changes, which creates noise and makes users update for nothing. Independent versioning is more precise, but users have to figure out which versions of your packages work together.

## 273: How do you test a published package before releasing it from a monorepo?

Pack it and install the tarball in a test project:

```bash
cd packages/ui
pnpm pack
cd /tmp/test-app
npm install /path/to/acme-ui-1.2.0.tgz
```

This catches missing files, wrong `exports` and leftover `workspace:` versions. Tools like `publint` and `@arethetypeswrong/cli` check a package's `exports` and types for common mistakes.

## 274: What is publint?

publint is a linter for npm packages. It checks `package.json` fields like `exports`, `main`, `types` and `files` against the files actually in the package, and reports problems like a missing file, wrong format or a `types` condition in the wrong place. Running it on every publishable package in CI catches broken releases early.

## 275: How do you handle breaking changes to a shared library used by many apps?

In a monorepo you can usually update all callers in the same pull request. If that's too big, add the new API next to the old one, mark the old one as deprecated, move callers over in smaller pull requests, then remove the old API. This expand-then-contract approach keeps `main` green the whole time.

## 276: What is a feature flag and why is it common in monorepos?

A feature flag is a switch that turns code on or off at runtime. In trunk-based monorepos, unfinished work is merged to `main` behind a flag instead of living in a long branch. This keeps branches short, reduces merge conflicts and lets teams ship whenever they want without waiting for others.

## 277: How do you keep main green in a busy monorepo?

Require CI checks before merging, run affected tests on every pull request, use a merge queue so pull requests are tested together with `main`, and quickly revert anything that breaks. Caching and affected detection keep CI fast enough that people don't try to skip it.

## 278: What is the role of a platform or developer experience team in a monorepo?

Big monorepos usually have a team that owns the shared tooling: CI, caching, the task runner config, code generators, dependency upgrades and lint rules. Product teams then focus on their apps. Without someone owning this, tooling slowly breaks and CI times creep up.

## 279: How do you add a new app to an Nx workspace?

Use a generator from the right plugin:

```bash
npx nx g @nx/react:app apps/admin --bundler=vite
npx nx g @nx/node:app apps/worker
```

The generator creates the folder, config files and tests, and registers what Nx needs. Use `--dry-run` first to see what files would be created.

## 280: How do you write a local Nx generator?

Create a plugin in the workspace and add a generator:

```bash
npx nx g @nx/plugin:plugin tools/acme-plugin
npx nx g @nx/plugin:generator tools/acme-plugin/src/generators/service
```

The generator is a function that gets a virtual file tree and options:

```js
import { generateFiles, formatFiles, joinPathFragments } from "@nx/devkit";

export default async function (tree, options) {
  generateFiles(
    tree,
    joinPathFragments(__dirname, "files"),
    `apps/${options.name}`,
    options,
  );
  await formatFiles(tree);
}
```

Teams use these to create new services with their own standard layout.

## 281: What is Turborepo's code generation feature?

Turborepo has `turbo gen`, which runs generators built on Plop:

```bash
npx turbo gen workspace --name @acme/logger
npx turbo gen my-generator
```

`turbo gen workspace` creates a new package, optionally copying an existing one. Custom generators live in `turbo/generators/config.ts` and use Plop's prompts and templates.

## 282: How do you rename or move a project in Nx?

Use the move generator:

```bash
npx nx g @nx/workspace:move --projectName=ui --destination=packages/shared/ui
```

It moves the files and updates imports, path aliases and config that point to the project. Doing it by hand is easy to get wrong in a big repo.

## 283: How do you remove a project in Nx?

```bash
npx nx g @nx/workspace:remove --projectName=old-lib
```

It deletes the project and its config. It fails if other projects still depend on it, unless you pass `--forceRemove`, which you should only do after removing those imports yourself.

## 284: What happens when two packages have the same name?

Package managers and task runners identify workspaces by name, so duplicates break things. pnpm and Turborepo fail with an error about duplicate names, and Nx reports conflicting project names. Every workspace package must have a unique `name`. This often happens when someone copies a package folder and forgets to rename it.

## 285: What if a package has no name in package.json?

npm and pnpm can still install it, but you can't depend on it by name, and Turborepo requires workspace packages to have names. Nx can name a project from `project.json` instead. Always give every workspace package a scoped name, even if nothing depends on it yet.

## 286: How do you run a one-off script across all packages?

With pnpm:

```bash
pnpm -r exec rm -rf dist
pnpm -r --filter "./packages/*" exec node -e "console.log(require('./package.json').name)"
```

`pnpm -r exec` runs any command in each package's folder. npm has `npm exec --workspaces`, and Yarn Berry has `yarn workspaces foreach -A exec`.

## 287: What is the order in which pnpm -r runs scripts?

By default, `pnpm -r run` sorts packages topologically, so dependencies run before the packages that use them. Packages with no relation run in parallel up to the `--workspace-concurrency` limit (4 by default). `--no-sort` turns off sorting, and `--parallel` runs everything at once and streams output.

## 288: Why might you still want Turborepo or Nx if pnpm -r already sorts packages?

`pnpm -r` doesn't cache results, so it reruns every build every time. It doesn't know task-level dependencies, like "test needs build of dependencies but not lint". It has no remote cache, no detailed task graph, and only basic change detection. For small repos that's fine. For bigger ones, caching alone saves a lot of CI time.

## 289: What is the Nx terminal UI?

Since Nx 21, running many tasks shows an interactive terminal UI by default. It lists tasks with their status, and you can pick a task to see its full output, filter the list, or interact with a running task. You can turn it off with `--tui=false` or the `tui` settings in `nx.json`, which CI does automatically.

## 290: What is continuous tasks in Nx?

Continuous tasks (added in Nx 21) are tasks that never exit, like a dev server. You mark them with `"continuous": true`. Other tasks can then depend on them. For example, an e2e task can depend on `web:serve`, and Nx starts the server first and keeps it running while the tests run, then stops it.

## 291: How does Turborepo handle a task that depends on a persistent task?

It doesn't allow it. If a task depends on a task marked `"persistent": true`, Turborepo reports an error, because the persistent task never finishes and the dependent would wait forever. Since Turborepo 2.x, you can use `"with"` to start sidecar tasks together, like running the API's `dev` alongside the web `dev`:

```json
{
  "tasks": {
    "dev": { "persistent": true, "cache": false, "with": ["api#dev"] }
  }
}
```

## 292: What does the interruptible option do in Turborepo?

In `turbo watch`, persistent tasks aren't restarted when files change, because Turborepo doesn't know if it's safe. Setting `"interruptible": true` on a persistent task tells `turbo watch` it's OK to stop and restart that task when its inputs change. It's useful for dev servers that don't have their own hot reload.

## 293: How do you pass arguments to the underlying script with Turborepo?

Put them after `--`:

```bash
npx turbo run test --filter=@acme/utils -- --watch
```

Everything after `--` is passed to the script in every selected package. These arguments are included in the task hash, so `test -- --coverage` gets a different cache entry from plain `test`.

## 294: How do you pass arguments to a task with Nx?

Pass them as flags after the target:

```bash
npx nx test ui --watch
npx nx build web --configuration=production
```

Unknown flags are forwarded to the underlying command or executor. Configurations in `project.json` group options for named setups like `production` or `development`.

## 295: What are configurations in an Nx target?

A target can have named sets of options:

```json
{
  "build": {
    "executor": "@nx/vite:build",
    "options": { "outputPath": "dist/apps/web" },
    "configurations": {
      "production": { "mode": "production" },
      "development": { "mode": "development" }
    },
    "defaultConfiguration": "production"
  }
}
```

You choose one with `-c development`. Each configuration has its own cache entries.

## 296: What is the parallel option in Nx?

`--parallel` sets how many tasks Nx runs at once:

```bash
npx nx run-many -t test --parallel=5
```

The default is 3. You can also set it in `nx.json` with the `parallel` property. Setting it too high on a small CI machine causes memory pressure and can be slower overall.

## 297: How do you exclude a project from Nx without removing it?

Remove its targets from the graph with plugin `exclude` globs, or add the folder to `.nxignore`, which works like `.gitignore` for Nx project detection. Projects inside ignored folders aren't added to the graph, so Nx won't run tasks for them.

## 298: How do you make sure a task never runs from cache in Nx?

Set `"cache": false` on the target, or leave out `cache: true`. In current Nx, a target is only cached if `cache` is true, either directly or through `targetDefaults` or a plugin. Deploy and publish tasks should never be cached because their effect is outside the repo.

## 299: Why shouldn't you cache deploy tasks?

A deploy changes something outside the repo, like a server or a CDN. If it came from cache, the logs would say it succeeded but nothing would actually be deployed. Caching only makes sense for tasks whose whole effect is the files they write and the logs they print.

## 300: How do you run a task after every other task in Turborepo?

Make it depend on the exact tasks it should wait for. For example, a root task that merges coverage after the tests of some packages:

```json
{
  "tasks": {
    "test": { "outputs": ["coverage/**"] },
    "//#coverage:merge": { "dependsOn": ["web#test", "@acme/ui#test"] }
  }
}
```

Note that `^test` wouldn't work here, because the root workspace doesn't depend on the other packages. If the list gets long, it's often simpler to run `turbo run test` and then the merge script as a separate CI step.

# Advanced Questions (301-450)

## 301: How would you decide between a monorepo and a polyrepo for a company?

Look at how the code is shared and who changes it. If many projects share libraries, change together often and are owned by teams that work closely, a monorepo saves a lot of coordination. If projects are truly independent, use different stacks, have strict access rules or are owned by separate companies or vendors, polyrepos fit better. Also check whether you have people to own the tooling, because a monorepo without good tooling gets slow fast.

## 302: What does "hermetic build" mean?

A hermetic build only depends on inputs that are declared and tracked: source files, pinned tool versions and declared dependencies. It doesn't read random env vars, the network, the current time or files outside its inputs. Hermetic builds give the same output for the same inputs, which is what makes caching safe. Bazel enforces this with sandboxing; Turborepo and Nx rely on you declaring inputs correctly.

## 303: Why are Turborepo and Nx not fully hermetic?

They run your normal scripts as normal processes. Those scripts can read any file on disk, any env var (in loose mode), the network and the clock. The tools hash what you tell them to, but they can't stop a script from reading something undeclared. Turborepo's strict env mode reduces one source of leaks by filtering env vars, but file access is still open.

## 304: What can go wrong if a task reads an undeclared input?

You get wrong cache hits. For example, a build reads `../../shared/config.json` but that file isn't in its inputs. Someone changes the config, the hash doesn't change, and the cache returns the old build. The bug shows up in production with the old config, and nobody can reproduce it locally because their cache is different.

## 305: How does Bazel enforce hermeticity?

Each action runs in a sandbox that only contains the files declared as its inputs. If a build step tries to read an undeclared file, it fails because the file isn't there. Network access can be blocked. Tool versions are pinned and downloaded by Bazel itself. This strictness is why Bazel caching is very reliable, and also why setting it up takes much more work.

## 306: What is remote execution?

Remote execution runs build actions on a cluster of remote machines instead of your own computer. Bazel, Buck2 and Pants support it through the Remote Execution API. Your laptop sends the action and its input hashes, workers fetch the inputs from a content-addressable store, run the action and store the outputs. Builds can run on hundreds of cores at once.

## 307: What is distributed task execution in Nx?

Nx Agents (part of Nx Cloud) split the task graph across several CI machines. The main job sends tasks to agents, respecting dependencies, and the agents share results through the remote cache. You set the number of agents, or let Nx scale it based on the size of the change. It's different from remote execution in that whole tasks (like a project's tests) run remotely, not individual compiler actions.

## 308: How would you split CI work across machines without Nx Agents?

Use CI matrix jobs. One job computes the affected projects and writes them as JSON. Then a matrix job runs one entry per project or per group:

```yaml
jobs:
  plan:
    outputs:
      projects: ${{ steps.p.outputs.projects }}
    steps:
      - id: p
        run: echo "projects=$(npx nx show projects --affected -t test --json)" >> "$GITHUB_OUTPUT"
  test:
    needs: plan
    strategy:
      matrix:
        project: ${{ fromJson(needs.plan.outputs.projects) }}
    steps:
      - run: npx nx test ${{ matrix.project }}
```

A remote cache lets each job reuse dependency builds done by other jobs.

## 309: What is the problem with naive sharding by package count?

Packages aren't equal. One package's tests may take ten minutes while twenty others take ten seconds each. Splitting by count leaves some machines idle while one runs forever. Better splits use past task durations to balance the work, which is what Nx Agents and some CI tools do. Splitting one large test suite with the test runner's own sharding (like `vitest --shard=1/4`) also helps.

## 310: How does Turborepo hash files quickly?

Turborepo uses Git's object hashes when it can. For tracked files that haven't changed, Git already knows their hash, so Turborepo doesn't need to read them. For changed or untracked files, it hashes the contents itself. Turborepo is written in Rust, and it hashes many files in parallel. This keeps hashing fast even in big repos.

## 311: How does Nx compute the project graph and keep it fast?

Nx reads workspace config, runs plugins' `createNodesV2` to find projects and targets, and analyzes source files to find imports between projects. This work is done in a mix of TypeScript and Rust, and the results are cached. The Nx daemon keeps the graph in memory and watches files, so only changed files are re-analyzed. In CI without the daemon, the graph is rebuilt each run, so plugin speed matters.

## 312: Why can a slow Nx plugin make every command slow?

Every Nx command needs the project graph, and building the graph calls every plugin's `createNodesV2`. If a plugin spawns a process or loads a heavy config file for each project, it adds that cost to every command. Nx caches plugin results by file hash, but cold runs in CI still pay it. When graph creation is slow, profile it with `NX_PERF_LOGGING=true` and look at plugin timings.

## 313: How would you profile a slow Turborepo run?

Run with `--profile=profile.json` to write a Chrome trace file of the run, then open it in Perfetto or Chrome's tracing tool. It shows where time goes: hashing, cache restore, task execution. `--summarize` shows per-task timing and cache status. Often the issue is one slow task on the critical path, or many small cache misses from a bad input config.

## 314: What is the critical path of a task graph?

The critical path is the longest chain of dependent tasks, measured in time. Even with infinite machines, the run can't finish faster than this chain. If `utils#build` (2 min) feeds `ui#build` (3 min), which feeds `web#build` (5 min), the critical path is 10 minutes. To speed up CI, shorten the critical path: split big packages, remove unneeded `dependsOn`, or make the slow tasks faster.

## 315: When should a test task not depend on ^build?

If the test runner can read dependencies' source directly (Vitest or Jest with TypeScript transforms, source-only packages, or custom export conditions), there's no need to wait for dependencies to build. Removing `^build` from `test` lets tests start right away and shortens the critical path. Keep `^build` only if tests actually import from `dist`.

## 316: What is the transit node pattern in Turborepo?

Sometimes you want a task to be rerun when dependencies change, but the task doesn't need dependencies' outputs. A common example is `typecheck` for packages using source files. You add an empty task as a "transit node":

```json
{
  "tasks": {
    "transit": { "dependsOn": ["^transit"] },
    "typecheck": { "dependsOn": ["transit"] }
  }
}
```

`transit` has no script, so nothing runs, but the dependency chain puts dependencies' hashes into `typecheck`'s hash. Tasks can run in parallel while caching stays correct.

## 317: Why can parallel tasks without dependsOn still give wrong cache results?

If `ui#typecheck` reads `utils`' source files but has no dependency on any `utils` task, then a change in `utils` doesn't change `ui#typecheck`'s hash. Turborepo will replay the old result even though types in `utils` changed. You need some edge (like `^build` or a transit node) so the dependency's changes flow into the hash.

## 318: How does Nx include dependencies in a task's hash?

Through inputs like `^production` or `^default`. The caret means "the matching files of all projects this project depends on". So with `"inputs": ["production", "^production"]`, a change to a dependency's production files changes this task's hash, even if the task doesn't depend on any of the dependency's tasks.

## 319: What makes a build non-deterministic and how does it hurt caching?

Output that changes between runs with the same inputs: timestamps embedded in files, random IDs, absolute paths, file order from directory listing, or values pulled from the network. Caching still "works", but downstream tasks that hash these outputs (like `dependentTasksOutputFiles` in Nx or Docker layers) see changes every time and miss the cache. Fix it by removing timestamps, sorting outputs and using relative paths.

## 320: How do absolute paths break cache sharing between machines?

If a build writes `/Users/alex/code/acme/packages/ui/src/button.tsx` into source maps or bundles, the output differs on every machine. Worse, if absolute paths sneak into the hash, CI and local runs never share entries. Turborepo and Nx hash relative paths, but your build tools might embed absolute ones. Configure tools to use relative source map paths.

## 321: What is cache poisoning in a remote cache?

Cache poisoning is when someone uploads a bad artifact under a valid hash, so others download and use it. It can be an accident (a broken local build with an undeclared input) or an attack (a malicious artifact that injects code). Since cached outputs end up in production builds, a poisoned cache can ship malware without any change in source code.

## 322: How do you protect a remote cache from poisoning?

- Let only CI write to the remote cache, and give developers read-only access.
- Sign artifacts (Turborepo's `remoteCache.signature`) so unsigned uploads are rejected.
- Use separate caches or namespaces for trusted branches like `main` and for pull requests from forks.
- Never give write tokens to untrusted pull request workflows.

## 323: How do you give developers read-only access to the Turborepo remote cache?

Use `--cache=local:rw,remote:r` (or set `TURBO_CACHE=local:rw,remote:r` in the environment) on developer machines. They can download artifacts from CI but not upload their own. CI uses the full `remote:rw`. With a self-hosted cache, you can also enforce this on the server by giving developers tokens that only allow reads.

## 324: What are the risks of running CI for pull requests from forks with a remote cache?

Fork pull requests run untrusted code. If the workflow has a write token, the pull request can upload poisoned artifacts that later runs on `main` will use. GitHub doesn't pass secrets to `pull_request` workflows from forks by default, but `pull_request_target` workflows do, and they're often misused. Run fork pull requests without write access to the cache.

## 325: Can secrets end up in the cache?

Yes. If a build bakes an env var like an API key into its output, that output is uploaded to the remote cache. Anyone with read access gets the secret. Also, logs are cached and replayed, so a script that prints a secret leaks it to the cache. Don't put secrets in build output, and treat cache access like access to the artifacts themselves.

## 326: How do you design env var handling so caching stays correct and safe?

Split vars into three groups. Build-time vars that change output go in `env` (hashed). Runtime-only vars like database URLs aren't needed during build at all; read them when the app starts. Secrets needed during build but not in output (like a source map upload token) go in `passThroughEnv`. Keep strict env mode on so anything undeclared is invisible to tasks.

## 327: What is the downside of putting NEXT_PUBLIC_* style vars in the hash?

Every distinct value creates a separate cache entry. If staging and production builds use different public URLs, each needs its own build, so you can't build once and promote the same artifact. To truly build once, read config at runtime (for example from a `/config.json` loaded by the browser or server-side env), and keep build output free of environment values.

## 328: How does pnpm 10 handle dependency lifecycle scripts, and why does it matter in a monorepo?

pnpm 10 doesn't run `postinstall` and other lifecycle scripts of dependencies by default. You allow specific packages with `onlyBuiltDependencies` in the workspace config:

```yaml
onlyBuiltDependencies:
  - esbuild
  - sharp
```

In a monorepo, one install brings in thousands of packages for every project, so one compromised dependency with a malicious install script could hit every developer and CI machine. Blocking scripts by default reduces that risk.

## 329: What is minimumReleaseAge in pnpm and why use it?

`minimumReleaseAge` (in minutes) tells pnpm not to install package versions published more recently than that:

```yaml
minimumReleaseAge: 1440
```

Many supply chain attacks publish a malicious version that gets caught and removed within hours. Waiting a day before using new versions avoids most of them. You can exclude your own packages with `minimumReleaseAgeExclude`.

## 330: How would you limit the blast radius of a compromised npm package in a monorepo?

Keep the lockfile committed and install with `--frozen-lockfile`. Block dependency install scripts (pnpm 10 default). Use a minimum release age. Review dependency updates instead of merging them blindly. Run CI with least-privilege tokens, and keep publish tokens only in release jobs. Use npm provenance or trusted publishing for your own packages so consumers can verify where they came from.

## 331: What is npm trusted publishing and why does it fit monorepo releases?

Trusted publishing lets a CI workflow publish to npm using OpenID Connect, without a long-lived npm token. You configure the package on npmjs.com to trust a specific GitHub repo and workflow file. In a monorepo releasing many packages from one workflow, this removes the biggest secret from CI and adds provenance, a signed link from each package version to the commit and build that made it.

## 332: How do you scale CODEOWNERS in a very large monorepo?

A single giant `CODEOWNERS` file gets hard to maintain and slow to review. Approaches: generate it from per-project metadata (like Nx tags or an `owners` field in each `package.json`), check it in CI so every project has an owner, and use team handles instead of individuals. Some companies use per-folder `OWNERS` files with custom bots instead, like Google and Chromium do.

## 333: How do you handle access control when some code must be private to one team?

Git doesn't support per-folder read permissions, so everyone with access to the repo can read everything. Options are: keep that code in a separate repo and consume it as a package, use a hosting product that supports path-level permissions, or accept read access for all and control writes through `CODEOWNERS` and branch protection. If read access is a legal requirement, the code shouldn't be in the shared monorepo.

## 334: How do you handle a monorepo where one app must be open source and the rest private?

Common approaches: keep the open source part in its own public repo and use it as a dependency, or develop it in the private monorepo and sync that folder to a public mirror with a tool like Copybara or a `git filter-repo` job. Mirroring needs care: external contributions have to be imported back, and private code must never leak into the mirrored folder.

## 335: How do you scale Git for a monorepo with millions of files?

Use partial clone and sparse checkout so developers only fetch and check out what they need. Turn on Git's file system monitor (`core.fsmonitor`) and the untracked cache so `git status` doesn't scan everything. Keep the commit-graph and multi-pack-index up to date with `git maintenance`. Microsoft's `scalar` tool sets all of this up for you. Avoid committing large binaries; use Git LFS for them.

## 336: What does git maintenance do?

`git maintenance start` registers the repo for background tasks: prefetching from remotes, updating the commit-graph, packing loose objects and repacking. These keep commands like `git log`, `git status` and `git fetch` fast in big repos. Without them, performance slowly gets worse as objects pile up.

## 337: Why is git status slow in big repos and how do you fix it?

`git status` must check every tracked file for changes and scan for untracked files. With hundreds of thousands of files, that's a lot of file system calls. The built-in file system monitor (`git config core.fsmonitor true`) watches for changes and tells Git which files to check. `git config core.untrackedCache true` caches untracked file results. Sparse checkout also helps by reducing the number of files.

## 338: How do you handle large binary files in a monorepo?

Don't commit them directly. Every version stays in history forever and makes every clone bigger. Use Git LFS, which stores pointers in Git and the files on a separate server. Better still, keep large assets (videos, design files, datasets) outside Git in object storage and reference them by URL or version.

## 339: How do lockfile merge conflicts happen and how do you resolve them?

Two pull requests that both change dependencies edit the same lockfile, and Git can't merge them cleanly. Don't fix lockfile conflicts by hand. Take one side (usually `main`'s), then run the install again so the package manager adds your changes:

```bash
git checkout --theirs pnpm-lock.yaml
pnpm install
git add pnpm-lock.yaml
```

pnpm can also resolve these conflicts itself when you run `pnpm install` on a conflicted lockfile.

## 340: Why do lockfile changes cause so many conflicts in big monorepos and how do you reduce them?

With one lockfile and many teams, dependency changes collide often. Reduce them by batching dependency updates (Renovate groups and schedules), using catalogs so versions change in one place, merging dependency update pull requests quickly, and using a merge queue so conflicts are found right away instead of after review.

## 341: How do you handle two apps that need different major versions of the same library?

Ideally you avoid it, but during migrations it's normal. Each app lists its own version in its own `package.json` (or uses a named pnpm catalog), and pnpm's isolated layout lets both versions coexist. Watch out for shared packages that import the library: they need it as a peer dependency so each app's version is used. Set a deadline to finish the migration so the repo doesn't keep two versions forever.

## 342: What happens with peer dependencies when a shared package is used by apps on different React versions?

By default a workspace package is a symlink to its own folder, so when `@acme/ui` imports `react`, Node resolves it from `packages/ui/node_modules`, not from the app. That means `@acme/ui` uses whatever React it has as a dev dependency, which may not be the app's React. Bundlers often hide this with dedupe settings (like Vite's `resolve.dedupe`), but the clean fix is pnpm's injected dependencies (next question), which give each app its own copy of `@acme/ui` linked to that app's React. Either way, the peer range must cover both versions.

## 343: What is pnpm's injected dependencies feature?

By default a workspace dependency is a symlink to the package folder. With `injected: true` (in `dependenciesMeta`) or the `inject-workspace-packages` setting, pnpm hard-links a copy of the package into the consumer's `node_modules` instead. This lets each consumer resolve the package's peer dependencies separately, and it's how `pnpm deploy` makes a self-contained folder. The downside is the copy must be re-synced after the package is rebuilt.

## 344: How does a single version policy affect very large teams?

It guarantees consistency, but each upgrade touches everyone. At Google's scale, upgrades are done by a central team with automated refactoring tools, sometimes over months, landing many small changes. Smaller companies usually can't afford that, so they allow exceptions with a clear owner and deadline. The policy is a goal, and the cost of keeping it grows with repo size.

## 345: How would you upgrade a major dependency like React across 40 apps?

Plan it in steps. First upgrade shared packages so they support both versions (peer range like `^18 || ^19`). Use codemods to apply API changes automatically. Move apps over in batches using named catalogs, starting with low-risk ones. Track progress with a dashboard or a lint rule. Once every app is moved, remove the old version and narrow the peer range. Turbo or Nx affected runs keep each batch's CI fast.

## 346: What is a codemod and why do monorepos use them a lot?

A codemod is a script that rewrites code automatically, usually by parsing it into an AST and changing it. Tools include jscodeshift, ts-morph and ast-grep. In a monorepo, one codemod can update every caller of a changed API in one pull request, which is one of the biggest advantages over polyrepos. Nx migrations are codemods packaged with version upgrades.

## 347: Write a small codemod that renames an imported function across the repo.

With jscodeshift:

```js
// rename-format.js
export default function transform(file, api) {
  const j = api.jscodeshift;
  const root = j(file.source);

  root
    .find(j.ImportDeclaration, { source: { value: "@acme/utils" } })
    .find(j.ImportSpecifier, { imported: { name: "formatMoney" } })
    .forEach((path) => {
      path.node.imported.name = "formatPrice";
    });

  return root.toSource();
}
```

```bash
npx jscodeshift -t rename-format.js --extensions=ts,tsx --parser=tsx apps packages
```

This only renames the import specifier. If the local name isn't aliased, you also need to rename uses in the file, which a full version would handle.

## 348: How do you measure the health of a monorepo over time?

Track CI duration (median and p95), cache hit rate, time to merge, flaky test count, number of projects affected by an average pull request, install time and graph creation time. A rising "affected per pull request" number often means a shared package has become too central and should be split. Nx Cloud and Vercel show some of this; otherwise export run summaries and chart them.

## 349: What is a "god package" and why is it a problem?

A god package is a shared package that almost everything depends on and that changes often, like `@acme/common` with types, helpers, constants and config all mixed. Every change to it marks the whole repo as affected, so CI runs everything. Split it into focused packages by purpose, so a change to date helpers doesn't retest code that only uses API types.

## 350: How do you split a large shared package without breaking everyone?

Create the new smaller packages and move code into them. Keep the old package as a thin re-export layer so existing imports still work. Use a codemod to update imports to the new packages, team by team. Add a lint rule that warns on imports from the old package. When nothing uses it anymore, delete it. Each step is a small, safe pull request.

## 351: How do you design the package structure for a large product monorepo?

Group by business area first, then by type. For example, `packages/checkout/feature-cart`, `packages/checkout/data-access`, `packages/shared/ui`, `packages/shared/util-date`. Apps stay thin and mostly compose features. Dependencies only point downward: app to feature, feature to data-access and ui, everything to util. Enforce it with tags and boundary rules so it doesn't decay.

## 352: How small should packages be?

Small enough that a change in one doesn't mark half the repo as affected, and large enough that the overhead (config, `package.json`, build setup, graph nodes) is worth it. A useful test: if two packages are always changed together and always used together, merge them. If a package has parts that different consumers use separately and that change at different rates, split it.

## 353: What is the cost of having too many tiny packages?

Every package adds config files, a node in the graph, a task per target and a cache entry per task. Thousands of tiny packages make graph creation, hashing and install slower, and developers spend time hunting for where things live. Some repos that went too far later merged packages back. Aim for packages that match real boundaries, not one per file.

## 354: How do you handle code that two business areas both need but neither owns?

Move it to a shared area with a clear owner, often the platform team, and keep it small. If both areas need different variations, don't force one shared version; let each own a copy until a real common shape appears. Shared code without an owner tends to collect hacks for every consumer and becomes a god package.

## 355: How would you migrate five separate repos into one monorepo?

Steps that usually work:

1. Agree on the layout, package manager, Node version and task runner.
2. Import each repo with history (`git filter-repo` into a subfolder, or `nx import`).
3. Make each one install and build inside the workspace, at first with its own dependency versions if needed.
4. Replace published internal libraries with `workspace:*` links.
5. Add caching and affected CI.
6. Over time, align dependency versions and shared config.

Move one repo at a time, freeze changes in the old repo during the move, and archive it afterwards.

## 356: What breaks most often when merging repos into a monorepo?

Dependency version conflicts (two repos used different React or TypeScript versions), phantom dependencies that worked because of a different hoisting layout, hard-coded paths in scripts that assume the repo root, CI configs that expect one project per repo, and duplicate package names. Plan time for each of these instead of expecting a clean move.

## 357: How would you migrate from Lerna to a modern setup?

Modern Lerna already runs on Nx, so you can keep `lerna version` and `lerna publish` while adding Nx caching. If you want to drop Lerna, move versioning and publishing to Changesets or `nx release`, move task running to Turborepo or Nx, and delete `lerna.json`. Make sure the old tags (like `@acme/ui@1.2.0`) are kept, because release tools use them to find what changed since the last release.

## 358: How would you migrate from Turborepo to Nx or the other way?

Nx has `nx init`, which detects `turbo.json` and can map tasks to Nx config. Going from Nx to Turborepo, you translate `targetDefaults` and inputs into `turbo.json` tasks and make sure every project has real `package.json` scripts, because Turborepo only runs scripts. In both directions, test cache correctness (inputs, outputs, env) carefully, because the defaults differ.

## 359: What are the main differences in default inputs between Turborepo and Nx?

Turborepo by default hashes all Git-tracked files in the package plus declared env vars and dependency hashes. Nx hashes what the target's `inputs` say; without them it defaults to all files in the project plus all files of dependencies, and plugins usually set precise inputs. So a Turborepo task reruns when any file in the package changes, unless you narrow `inputs`.

## 360: How do you handle a task that depends on files generated by another package's task?

Declare the dependency so both ordering and hashing are correct. In Turborepo, `"dependsOn": ["@acme/api#openapi"]`. In Nx, `"dependsOn": [{ "projects": ["api"], "target": "openapi" }]` and add the generated file to inputs. Also make sure the generator task lists the file in its `outputs`, or a cache hit won't restore it.

## 361: How would you generate a typed API client from an OpenAPI spec in a monorepo?

Let the API package produce `openapi.json` as a cached task. A `@acme/api-client` package has a `generate` task that depends on it and writes the client into its `src/generated` folder, listed in `outputs`. Apps depend on `@acme/api-client`. Now changing the API spec automatically regenerates the client and rebuilds and tests every app that uses it.

## 362: Should generated code be committed in a monorepo?

It depends. Committing it makes the repo work without running generators and shows changes in code review, but it can get out of date, and pull requests fill with noise. Not committing it keeps the repo clean but every task needs the generate step first. Many teams don't commit it and rely on cached generate tasks, but commit things that are slow or need external access to generate.

## 363: How do you check that a committed generated file is up to date?

Run the generator in CI and fail if Git sees a change:

```bash
pnpm turbo run generate
git diff --exit-code -- packages/api-client/src/generated
```

The same pattern works for `nx sync:check`, formatted code and lockfiles.

## 364: What are micro-frontends and how do they relate to monorepos?

Micro-frontends split a web frontend into parts owned by different teams that can be built and deployed separately and composed in the browser or at the edge. They can live in a monorepo or in separate repos. A monorepo makes sharing a design system and types easier and keeps versions aligned, while the separate deployments keep teams independent.

## 365: What is Module Federation?

Module Federation is a feature (first in webpack 5, now also in Rspack and Vite through plugins) that lets one app load code from another app at runtime. A "host" app loads "remote" modules over the network, and both can share dependencies like React so they load once. In monorepos, Nx has generators for host and remote apps, and it's a common way to build micro-frontends.

## 366: What are the risks of sharing dependencies with Module Federation?

Shared modules are resolved at runtime. If the host and a remote expect different major versions, you can get two copies or, worse, one copy that doesn't match what a remote was built against. You need `singleton` and `requiredVersion` settings for libraries like React, and you need to deploy compatible versions. A monorepo with one version per dependency makes this much easier to keep right.

## 367: How do Turborepo microfrontends work?

Turborepo has a microfrontends feature where a `microfrontends.json` file describes several apps and which URL paths each one serves. During local development, Turborepo runs a proxy that routes requests to the right app's dev server, so you can work on one app while others come from production or local servers. On Vercel, the same config drives routing in production. It's path-based composition, not runtime module loading.

## 368: How do you run React Native in a monorepo?

Metro (React Native's bundler) historically had trouble with symlinks and folders outside the app. Recent versions of Metro and Expo support monorepos much better, and Expo configures `watchFolders` and resolution for you. With pnpm, some setups still use `node-linker=hoisted` because native build tools expect packages in a flat `node_modules`. Shared packages should be plain TypeScript without web-only APIs.

## 369: How do you share code between web and React Native apps?

Share business logic, API clients, validation, state management and types freely. For UI, either keep separate components per platform with a shared props interface, or use a cross-platform library. Use platform-specific files (`button.web.tsx`, `button.native.tsx`) when a component needs a different implementation. Avoid importing DOM APIs in shared packages; a lint rule can enforce that.

## 370: How do you handle a polyglot monorepo with Node.js and Go services?

Turborepo needs a `package.json` per workspace, so Go services get a small `package.json` with scripts like `"build": "go build ./..."`, and inputs set to `**/*.go`, `go.mod` and `go.sum`. Nx has community and official plugins for Go and other languages that infer targets. Bazel and Pants handle many languages natively. Whatever you pick, make sure each language's dependency files are part of the cache inputs.

## 371: How do you share types between a Node.js API and a Go service?

You can't share TypeScript types directly with Go. Use a language-neutral schema as the source of truth, like OpenAPI, Protocol Buffers or JSON Schema, and generate types for both languages. In a monorepo, the schema package has a `generate` task, and both services depend on it, so a schema change rebuilds and tests both.

## 372: What is Buck2?

Buck2 is Meta's build system, rewritten in Rust and open sourced in 2023. Like Bazel, it uses fine-grained build rules, hermetic actions and remote execution, and it works across many languages. It's designed for very large monorepos. Rules are written in Starlark, the same Python-like language Bazel uses.

## 373: When would you choose Bazel over Nx or Turborepo?

When the repo is very large, has many languages (C++, Java, Go, JavaScript, Python), needs hermetic and reproducible builds, or needs remote execution across many machines. The cost is high: every target is described in `BUILD` files, JavaScript tooling integration takes work (through rules_js), and the team needs Bazel experts. For mostly JavaScript repos, Nx or Turborepo are usually enough.

## 374: What is the difference between package-level and file-level build graphs?

Turborepo and Nx work at the package (project) level: a change to any input file reruns the whole package's task. Bazel and Buck2 work at the file or target level: a change to one file reruns only the actions that use it, like compiling that file and linking. File-level graphs are more precise and scale better, but need much more detailed build descriptions.

## 375: How do you make test runs more precise than per-package affected?

Use the test runner's own change detection within a package, like `vitest --changed` or `jest --changedSince=origin/main`, which only run tests that import changed files. Combined with package-level affected, this cuts test time further. Some companies use test impact analysis, mapping tests to the code they cover from past runs, but that adds complexity and can miss things.

## 376: What is test impact analysis?

Test impact analysis picks which tests to run based on which code they actually executed in earlier runs. If a change only touches files that test A covered, only test A runs. It's more precise than import graphs, but coverage data can go stale and dynamic code paths can be missed. Teams that use it still run the full suite on `main` or nightly as a safety net.

## 377: How do you deal with flaky tests in a monorepo?

Flaky tests hurt more in monorepos because they block everyone's pull requests. Track flakiness (Nx Cloud detects flaky tasks; CI tools report retries), quarantine flaky tests into a separate non-blocking job, and assign owners through `CODEOWNERS`. Automatic retry of failed tasks helps short term but hides real bugs if used forever. Never cache a failed run as success.

## 378: Does Turborepo cache failed tasks?

No. Turborepo only caches tasks that exit successfully. A failed task runs again next time. Nx also caches only successful runs by default. This means a flaky failure doesn't get stuck in the cache, but it also means a deterministic failure reruns each time, which is fine because you need to fix it anyway.

## 379: What is Nx self-healing CI?

It's an Nx Cloud feature that uses AI to look at failed tasks in CI, propose a fix, and check it by rerunning the task. The developer sees the suggested change and can apply it to the pull request. Whether it's worth using depends on the team, but it shows a general trend of monorepo tools moving into CI automation beyond caching.

## 380: How do you handle cache size and eviction?

Local caches grow without limit by default in many setups. Turborepo 2.10 added `cacheMaxAge` and `cacheMaxSize` options for automatic eviction, and Nx has `maxCacheSize` in `nx.json`. For self-hosted remote caches, set lifecycle rules on the storage bucket (for example, delete objects older than 14 days). Old entries are rarely hit, since most hits come from recent commits.

## 381: How do you estimate the benefit of a remote cache before paying for one?

Look at CI summaries for a week: how much time is spent on tasks whose inputs were already built in an earlier run (same hash seen before). With `--summarize` or `--dry=json` you can collect hashes and durations and compute how much time would have been saved. Most of the win usually comes from pull request reruns and from `main` builds reusing pull request results.

## 382: Why is the first CI run on main after a merge often a cache hit?

If the pull request was tested against the latest `main` (for example via a merge queue or rebase), the merge commit has the same file contents the pull request already built. The hashes match, so `main`'s CI downloads results from the remote cache. That's why merge queues and remote caches work so well together.

## 383: How do you make sure a cache hit is truly safe to deploy?

Make sure every input that affects the artifact is in its hash: source, lockfile, tool versions, env vars, config. Build artifacts for deploy only from trusted CI runs, and only trust remote cache entries written by trusted jobs. Some teams skip the cache for production deploy builds altogether, paying the time cost for extra safety.

## 384: What is the difference between task caching and build tool caching like webpack's filesystem cache?

Task caching (Turborepo, Nx) skips a whole task when its inputs match. Build tool caching (webpack's `cache: { type: "filesystem" }`, Next.js `.next/cache`, TypeScript's `.tsbuildinfo`) makes a task faster when it does run, by reusing parts of the previous build. They work together. Exclude the build tool's cache folder from the task's `outputs` (like `!.next/cache/**`), because it's large and not part of the result.

## 385: Why exclude .next/cache from Turborepo outputs?

`.next/cache` holds Next.js's incremental build data and fetch cache. It can be huge, and it isn't needed to run or deploy the app. Including it bloats every cache entry and slows uploads and downloads. The recommended output for Next.js is `[".next/**", "!.next/cache/**"]`.

## 386: How does Nx decide which files to restore on a cache hit?

It restores everything listed in the target's `outputs`. If outputs aren't set and the target is inferred, the plugin usually sets them from the tool's config (for example Vite's `build.outDir`). If a task writes files that aren't in outputs, those files won't be restored, and later tasks that need them fail with confusing "file not found" errors only on cache hits.

## 387: What is a common cause of "works on cache miss, fails on cache hit"?

Missing `outputs`. When the task runs, it writes files that later tasks use. When it's a cache hit, only the declared outputs are restored, so the undeclared files are missing. Another cause is a task with side effects outside the repo (like starting a container or writing to a global folder) that a replay doesn't repeat.

## 388: What is a common cause of "works on cache hit, fails on cache miss"?

A task depends on another task's output but doesn't declare it in `dependsOn`. On a cache hit everything is restored quickly, so the timing happens to work. On a miss, the task starts before its real dependency finishes. Running with `--force` or a cold cache in CI now and then exposes these hidden ordering bugs.

## 389: How would you test that your cache configuration is correct?

Run the full pipeline cold (`--force` or clean cache), save the outputs, then run again with the cache and compare outputs file by file. Then make a small change in a shared package and check that exactly the expected tasks miss the cache. Also try changing env vars and tool versions. Some teams run a weekly cold build in CI and compare it with cached artifacts.

## 390: How does Nx handle tasks that write outputs into the same folder?

Two tasks with overlapping `outputs` (for example both writing to `dist/`) can corrupt each other's cache entries, because restoring one overwrites the other's files. Nx warns about this in some cases. Give each task its own output folder, or make one task depend on the other and include both outputs in the later task.

## 391: Why should each package build into its own folder rather than a shared root dist?

Some older setups build everything into a root `dist/apps/web`, `dist/libs/ui`. That works, but package-based tools assume a package's outputs live inside it, which matches how npm packages work and how `exports` point to files. Building into the package's own folder keeps it self-contained, so it can be packed, published or copied into Docker on its own.

## 392: How do you design a release process for 30 independently versioned packages?

Use Changesets or `nx release` in independent mode. Developers add a changeset with each pull request. CI checks that pull requests touching publishable packages include a changeset (`changeset status --since=origin/main`). A bot keeps a version pull request open. Merging it publishes only changed packages, with changelogs and tags per package, using trusted publishing. Dependents get patch bumps automatically when their dependencies' ranges change.

## 393: How do you check in CI that a pull request includes a changeset?

```bash
npx changeset status --since=origin/main
```

It exits with an error if packages changed since `origin/main` but have no changeset. Teams allow "empty" changesets (`npx changeset --empty`) for changes that shouldn't release anything, like test-only edits.

## 394: How does nx release decide what to bump?

It depends on config. With `conventionalCommits: true`, Nx reads commit messages since the last release tag for each project and picks the bump type from `fix`, `feat` and breaking changes. You can also use version plans (files similar to changesets, created with `nx release plan`) or pass a specifier like `nx release minor`. It then bumps dependents when their dependency ranges need updating.

## 395: What are version plans in nx release?

Version plans are markdown files in `.nx/version-plans/` that describe which projects should be bumped and how, much like changesets:

```md
---
ui: minor
utils: patch
---

Add the Tooltip component.
```

You create them with `nx release plan` and enable them with `"versionPlans": true` in the release config. They let you record release intent in the pull request instead of relying on commit messages.

## 396: How do you release packages and deploy apps from the same monorepo?

Treat them as separate flows. Publishable packages go through Changesets or `nx release` with semver and changelogs. Apps don't need versions; they're deployed on merge to `main` based on affected detection, maybe with a commit SHA or date as their identifier. Mixing the two (versioning apps with semver just because packages are versioned) adds work without much value.

## 397: How do you roll back one app in a monorepo without rolling back others?

Deploy each app from its own artifact, tagged with the commit SHA. To roll back, redeploy the previous artifact for that app only. Avoid rolling back by reverting commits on `main` when other apps changed in the same commits. Keeping deploy artifacts and a per-app deploy history (in your CD tool) makes this a one-step action.

## 398: How do you handle database migrations when several services share a database?

Ideally, each service owns its own database or schema, so migrations aren't shared. If they do share, put migrations in one package with a clear owner, run them in a separate deploy step before the services, and make them backward compatible (expand, then deploy services, then contract). Never let two services each run their own migrations against the same tables.

## 399: Explain expand and contract migrations in a monorepo context.

First expand: add the new column or table without removing the old one, and deploy. Then update all services to write to both and read from the new one, which in a monorepo can be one pull request across services. Backfill data. Then contract: remove the old column once nothing uses it. Each step is safe to deploy on its own, which matters because services in a monorepo still deploy separately.

## 400: Why can't you assume all apps in a monorepo are deployed at the same time?

Even though they're in the same commit, each app deploys separately and at its own pace. Rollouts take minutes, some apps deploy only when affected, and mobile apps stay on old versions for months. So changes between services must be backward compatible. The monorepo makes the code consistent, not the running system.

## 401: How do you version an API used by several apps in the same monorepo?

If all clients deploy together with the API, you can change it freely in one pull request. If clients deploy separately (mobile apps, external users, other services), you need backward compatibility: add new fields instead of changing old ones, support old and new versions side by side, and remove old versions only after clients have moved. The monorepo helps you find every internal caller, but doesn't remove the need for compatibility.

## 402: How would you design CI for a monorepo with 200 projects and 100 engineers?

- Affected-only tasks on pull requests with a remote cache written only by CI.
- Distributed execution across several machines, balanced by past task durations.
- A merge queue so `main` stays green.
- Per-project owners in `CODEOWNERS`.
- Required checks computed per pull request, with one summary check that branch protection depends on.
- Weekly cold builds to catch cache config bugs.
- Dashboards for CI time, cache hit rate and flaky tests.

## 403: Why use one summary check for branch protection in a monorepo?

Branch protection needs a fixed list of required check names. In a monorepo, which jobs run depends on what changed, so a project's test job might not run at all for an unrelated pull request, and GitHub waits for it forever. A final job that `needs` all others and passes when they passed or were skipped gives branch protection one stable name to require.

## 404: How do you handle CI for changes that only touch documentation?

Use path filters or affected detection so docs-only changes skip builds and tests. With affected tools, if no project's inputs changed, nothing runs. Make sure the summary required check still reports success, otherwise the pull request is blocked. Lint and format checks for markdown can still run quickly.

## 405: What is a "trigger everything" file and how do you handle it?

Some files affect every project: the root lockfile for shared tools, the base `tsconfig`, the CI config, the root ESLint config. Changes to them mark everything as affected and trigger a full CI run. That's correct, but expensive. Keep such files few and stable, split them where possible, and accept that these pull requests take longer.

## 406: How do you decide what belongs in globalDependencies or sharedGlobals?

Include only files that truly change the output of every task, like the base TypeScript config or a root Babel config. Don't include the CI workflow file, the root README or files used by only a few packages; add those to the specific tasks instead. Every extra global input reduces cache hit rates across the whole repo.

## 407: How would you handle a CI workflow change that should test everything?

When the CI config itself changes, a pull request should prove the full pipeline still works, so run all tasks, not just affected ones. You can detect changes to `.github/workflows/**` and switch to `run-many` or `turbo run` without `--affected` in that case. The remote cache still makes most of the run fast.

## 408: What are the trade-offs of putting infrastructure code (Terraform, Kubernetes) in the monorepo?

Pros: an app and its infrastructure change in one pull request, reviewers see both, and affected detection can trigger an infra plan when an app's config changes. Cons: infra changes need different reviewers and stricter controls, the tools (Terraform, Helm) don't fit JavaScript task runners naturally, and infra deploys usually shouldn't happen automatically on every merge. Many teams keep infra in the monorepo with separate pipelines and owners.

## 409: How would you prevent one team's broken build from blocking everyone?

Affected-only CI means a broken package only blocks pull requests that touch it or its dependents. A merge queue stops broken changes from landing on `main`. Fast revert policies help when something slips through. For really independent areas, some companies use separate required checks per area so an unrelated failure doesn't block a pull request.

## 410: What is a "monorepo-wide refactor" and how do you do it safely?

It's a change that touches code across many projects, like renaming a core API or upgrading a framework. Do it with codemods, split by owner so each team reviews its own part, and land in small batches if the full change is too big. Use deprecations and compatibility layers so batches can land separately. Run the full test suite, not just affected, for the final step.

## 411: How do you get a large cross-team change reviewed when CODEOWNERS requires many approvals?

Split the pull request by owner area so each team reviews only its part, with the shared change landing first in a backward-compatible way. For purely mechanical changes, some companies allow a "global approver" group to approve codemod pull requests. Without one of these, a 50-team pull request can wait weeks for every approval.

## 412: How does Google's monorepo handle so much code?

Google's repository is stored in Piper, a custom version control system built on their own distributed storage. Developers use CitC (Clients in the Cloud), a virtual file system that shows the whole repo but only fetches files when they're read. Builds use Blaze (open sourced as Bazel) with remote caching and remote execution. Large refactors use tools like Rosie, which splits a change into many small reviewed pieces. Normal Git and Node tools wouldn't scale to that size.

## 413: What is a virtual file system for a monorepo?

It's a layer that shows the full repository in your file system but only downloads file contents when you open them. Google's CitC, Meta's EdenFS and Microsoft's former VFS for Git (GVFS) are examples. They make huge repos usable without cloning everything. In the Git world, sparse checkout and partial clone give a simpler version of the same idea.

## 414: What is Sapling?

Sapling is a source control client from Meta, open sourced in 2022. It can work with Git repositories (including GitHub) and is designed for large monorepos and stacked changes. It has a smart log, easy commit stacking and undo. It's an option for teams that like stacked diffs and work in big repos, though most teams still use plain Git.

## 415: What are stacked pull requests and why are they useful in monorepos?

A stack is a series of small pull requests where each builds on the one before. Instead of one huge pull request touching ten packages, you have ten small ones that can be reviewed by the right owners in order. Tools like Graphite, ghstack, Sapling and git-town help manage stacks. They fit trunk-based monorepos because they keep changes small without waiting for each to merge.

## 416: How do you set up a monorepo for multiple teams with different release speeds?

Let each team deploy its own apps on its own schedule using affected detection and per-app pipelines. Shared packages use semver if published, or stay internal and always current. Teams that release slowly (like mobile) pin to tested versions of backend APIs through compatibility rules. The monorepo shares code and tools, but doesn't force a single release train.

## 417: What is a release train and does it fit a monorepo?

A release train ships on a fixed schedule, with whatever is ready. Mobile apps and enterprise software often use them. In a monorepo, a release branch can be cut from `main` for the train, and only fixes are cherry-picked into it. It fits for products that must release together, but most web services in a monorepo deploy continuously instead.

## 418: How do you cherry-pick a fix to a release branch in a monorepo?

Cut release branches from `main` (like `release/2026-11`) and cherry-pick the fix commit onto it. Keep fixes small and focused on one area, because in a monorepo a commit can easily touch unrelated projects, and cherry-picking those brings in unwanted changes. CI on the release branch should run the full suite for the released apps, since affected detection compared to `main` doesn't apply there.

## 419: What would you do if CI time doubled over six months?

Look at the data before changing anything. Check cache hit rate (did a global input start busting caches?), the average number of affected projects (did a god package appear?), the critical path (did one slow task get slower?), and install time. Common fixes are narrowing inputs, splitting a central package, removing unneeded `dependsOn`, adding distributed execution and fixing slow tests.

## 420: Your remote cache hit rate dropped from 80% to 20% overnight. How do you investigate?

Compare task summaries from before and after to see which hash inputs differ. Likely causes: a new env var in `globalEnv`, a change to a global config file that now changes every run (like a generated timestamp), a CI image update that changed the Node version (if hashed), a lockfile change, or the cache server failing or evicting too much. Check the cache server's logs and storage too.

## 421: A developer says a build passes locally but fails in CI with the same commit. What do you check?

Differences in environment: Node and package manager versions, env vars, OS (case-sensitive file names on Linux), uncommitted or ignored files present locally, and a stale local cache hiding a failure. Ask them to run with the cache disabled (`--force` or `--skip-nx-cache`) on a clean clone. Also check whether CI uses a frozen lockfile while local installs updated it.

## 422: Why do case-sensitive file names cause monorepo CI failures?

macOS and Windows file systems are usually case-insensitive, so `import Button from "./button"` works even if the file is `Button.tsx`. Linux CI is case-sensitive, so the import fails there. Renaming files only by case also confuses Git on macOS. A lint rule like `import/no-unresolved` with case checking or TypeScript's `forceConsistentCasingInFileNames` catches it early.

## 423: A shared package change broke an app that wasn't in the affected list. How could that happen?

The dependency wasn't visible to the tool. Maybe the app imports the package through a relative path, a dynamic `require` with a computed string, or a TypeScript path alias the tool doesn't read. Or the package is used through a config file (like a Tailwind preset or a Babel plugin) that isn't analyzed. Fix it by importing by package name, adding the dependency to `package.json`, or adding an implicit dependency.

## 424: How does Nx find dependencies between projects?

It combines several sources: `package.json` dependencies between workspace packages, static analysis of `import` and `require` statements in source files (mapped to projects through package names or TypeScript path aliases), `implicitDependencies` in project config, and dependencies that plugins add. You can view the result with `nx graph` and check why an edge exists by clicking it.

## 425: How does Turborepo find dependencies between packages?

Turborepo uses only `package.json` dependencies (`dependencies`, `devDependencies`, `optionalDependencies`) between workspace packages. It doesn't scan imports. So if a package imports another workspace package without listing it, Turborepo doesn't see the link. This is simpler and faster, but it means your `package.json` files must be accurate. `turbo boundaries` helps find undeclared imports.

## 426: What are the pros and cons of import analysis versus package.json analysis for graphs?

Import analysis (Nx) finds real dependencies even if `package.json` is wrong, and works for repos that link code with path aliases. But it can be slower, and dynamic imports or unusual patterns may be missed or mis-detected. `package.json` analysis (Turborepo, pnpm) is fast and matches what package managers and publishing see, but trusts that declarations are correct. Many teams use `package.json` graphs plus a lint rule that checks imports match declarations.

## 427: What is the risk of TypeScript path aliases in a package-based monorepo?

Path aliases let code import a package by name without it being in `package.json`. TypeScript is happy, and maybe the bundler too, but the package manager, Turborepo, Docker pruning and publishing don't know about the dependency. Builds work in dev and break in production or in a pruned Docker image. If you use workspace packages, prefer real `package.json` dependencies over path aliases.

## 428: How would you design a dev environment so starting the full system is fast?

Don't start everything. Let developers start the app they work on plus its direct dependencies, and point other services at a shared staging environment or lightweight mocks. Use cached builds for packages so dev servers start from built outputs. Use `turbo watch` or Nx continuous tasks to rebuild only what changes. Document one command per common scenario.

## 429: How do you handle very long install times in a monorepo dev container or codespace?

Prebuild the container image with dependencies installed, using the lockfile hash as the cache key. Use pnpm's store in a shared volume. GitHub Codespaces prebuilds and similar features do this automatically. Also check for heavy postinstall scripts (Playwright browsers, native builds) and only run them in the projects that need them.

## 430: How do you install Playwright browsers efficiently in a monorepo?

Only install browsers in jobs that run e2e tests, not in every CI job. Cache the browser folder (`~/.cache/ms-playwright`) with a key that includes the Playwright version. Install only the browsers you test with (`npx playwright install --with-deps chromium`). Keep one Playwright version across the repo with a catalog so the cache is shared.

## 431: What are the security implications of a single repo for all code?

Anyone with read access sees all code, including internal tools and possibly secrets someone committed by mistake. A compromised developer account exposes everything. On the other hand, security fixes and dependency patches apply everywhere at once, and scanning tools (secret scanning, dependency audit, static analysis) cover all code with one setup. Treat repo access as sensitive and turn on secret scanning with push protection.

## 432: How do you prevent secrets from being committed to a monorepo?

Turn on GitHub secret scanning with push protection so pushes containing known token formats are blocked. Add a pre-commit hook with a scanner like gitleaks. Keep `.env` files ignored and commit only `.env.example`. If a secret is committed, rotate it right away. Removing it from history doesn't help because it's already in clones and caches.

## 433: How do you run npm audit or vulnerability scans in a monorepo?

Run `pnpm audit` or `npm audit` at the root, which checks the whole lockfile. Tools like Dependabot alerts, Snyk or Socket scan the lockfile and map issues to packages. Use overrides to patch transitive vulnerabilities quickly. Focus on production dependencies of deployed apps (`pnpm audit --prod`), since dev-only issues are usually lower risk.

## 434: What is SBOM and how does a monorepo complicate it?

An SBOM (software bill of materials) lists every component and version in a piece of software. In a monorepo, the lockfile covers all projects together, but each deployed app needs its own SBOM with only its dependencies. You generate per-app SBOMs from a pruned lockfile (`turbo prune`, `pnpm deploy`) or from the built container image with tools like Syft.

## 435: How would you enforce that apps don't import from other apps?

Mark apps with a tag (Nx `type:app`) and add a boundary rule that nothing may depend on `type:app`. Without Nx, set `"private": true` and give apps no `exports`, and add an ESLint `no-restricted-imports` pattern for app paths. Also check `package.json` files in CI to make sure no package lists an app as a dependency.

## 436: How would you enforce a layered architecture across packages?

Define layers like `util`, `data-access`, `ui`, `feature`, `app`, and a rule that each layer can only import layers below it. Tag every project with its layer and enforce the rule in lint (Nx module boundaries, `turbo boundaries` tags or dependency-cruiser). Fail CI on violations. Without enforcement, deadline pressure slowly adds shortcuts until the layers mean nothing.

## 437: How do you prevent a package from growing unbounded dependencies?

Track the number of dependencies per package and fail CI if a "leaf" package (like a util) gains a dependency on a heavy library. Nx's `@nx/dependency-checks` rule keeps declared dependencies honest. Bundle size checks (size-limit) catch heavy imports in packages that ship to browsers. Code review by owners is the last line.

## 438: How do you keep the bundle size of apps under control when sharing packages?

Make shared packages tree-shakeable: ESM output, `"sideEffects": false` in `package.json` when true, and many small named exports instead of one big default object. Avoid barrel files that import everything if your bundler can't tree-shake them well. Add per-app bundle size checks in CI so a change to a shared package that adds weight shows up in review.

## 439: What is the problem with barrel files in monorepo packages?

A barrel file (`index.ts` that re-exports everything) makes imports easy, but some tools have to load every re-exported module to resolve one import. This slows down dev servers, tests and type checking, and can break tree shaking if any module has side effects. Options are multiple entry points in `exports` (`@acme/ui/button`), or keeping barrels but making sure `sideEffects: false` is set and tools optimize them.

## 440: What does "sideEffects": false do for a shared package?

It tells bundlers that importing a module from this package has no effects other than defining exports. So if an app imports one function and doesn't use the rest, the bundler can drop the unused modules entirely. If some files do have side effects (like CSS imports or global polyfills), list them instead: `"sideEffects": ["*.css"]`.

## 441: How do you publish a package from a monorepo that works for both ESM and CommonJS users?

In 2026, many libraries ship ESM only, since modern Node can `require()` ESM modules in most cases. If you still need both, build two outputs and use conditional `exports`:

```json
{
  "type": "module",
  "exports": {
    ".": {
      "types": "./dist/index.d.ts",
      "import": "./dist/index.js",
      "require": "./dist/index.cjs"
    }
  }
}
```

Check with publint and `@arethetypeswrong/cli`, because dual packages are easy to get wrong.

## 442: What is the dual package hazard?

If a package ships both ESM and CommonJS builds, an app might load both copies: one through `import` and one through `require`. Then there are two instances of any state or class, so `instanceof` checks fail and singletons aren't single. In a monorepo with mixed ESM and CommonJS code, this happens more easily. Shipping ESM only, or making the CommonJS build a thin wrapper around ESM, avoids it.

## 443: How would you structure a monorepo for a SaaS product with web, mobile, API and workers?

```
apps/
  web/          Next.js
  mobile/       Expo
  api/          Node.js HTTP API
  worker/       background jobs
packages/
  contracts/    zod schemas and types
  api-client/   typed client for web and mobile
  db/           schema, migrations, client
  ui-web/       web components
  ui-native/    mobile components
  domain/       pure business logic
  config/       eslint, tsconfig, prettier
```

Rules: apps depend on packages only, `domain` depends on nothing app-specific, `db` is only used by `api` and `worker`, and `contracts` is the source of truth shared across all of them.

## 444: In that SaaS layout, why keep db out of web and mobile?

The database client contains connection code, credentials handling and server-only drivers. If a web or mobile package imports it, even by mistake, you might leak server code into a client bundle or break the build. A boundary rule (`platform:client` can't depend on `platform:server`) makes this a lint error instead of a production incident.

## 445: How do you share business logic between the API and a background worker?

Put it in a package like `@acme/domain` that holds pure functions and service classes, with dependencies like the database passed in rather than imported. The API and worker each create the real dependencies and call the shared logic. This keeps the logic testable without a database and avoids both apps opening connections they don't need at import time.

## 446: How would you explain to management why the monorepo needs a platform team?

Put it in numbers. Show CI time per pull request, hours lost waiting per engineer per week, and time spent on cross-repo changes or upgrades. Then show what investment in caching, affected detection and tooling would save. A monorepo's benefits depend on tooling that someone has to own; without it, the costs (slow CI, broken builds, messy dependencies) grow with every new team.

## 447: When would you move away from a monorepo?

When the costs keep exceeding the benefits even with good tooling: teams that never share code, strict access rules that can't be met, very different stacks or release cycles, or a company split where parts move to a different organization. It's usually partial: one part leaves (with history via `git filter-repo`) while the rest stays. Do it because of real problems, not because CI is slow, since that's usually fixable.

## 448: Interview scenario: a team wants to add a heavy Python ML service to your JavaScript monorepo. What do you consider?

Check whether it shares code or contracts with the rest. If it uses the same API schemas and changes together with them, keeping it in the repo has value. Then consider tooling: Python dependency management (uv or Poetry), how the task runner will hash Python inputs, large model files (keep them out of Git), CI images with GPUs, and separate owners. If it shares nothing, a separate repo may be simpler.

## 449: Interview scenario: builds pass but the deployed app uses an old version of a shared package. How do you debug?

Check which artifact was deployed and from which commit. If it came from the cache, look at its hash inputs: maybe the shared package isn't a declared dependency (relative import or path alias), so its change didn't affect the app's hash. Also check that the Docker build used `workspace:*` links and not a published version from the registry, and that the package's `exports` point to freshly built files.

## 450: What are the three most important things to get right when starting a monorepo?

First, accurate dependencies: every package declares what it uses in `package.json`, enforced by a strict package manager and lint rules. Second, correct caching: inputs, outputs and env vars declared for every task, with the remote cache written only by CI. Third, clear boundaries and ownership: tags or rules for what can import what, and `CODEOWNERS` so every folder has someone responsible. Most monorepo problems later come from skipping one of these.
