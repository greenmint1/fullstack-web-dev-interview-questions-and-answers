# Angular Micro Frontend Interview Questions and Answers

_Last updated: October 28, 2026_

450 interview questions with answers about building micro frontends with Angular, split into three levels: 150 easy, 150 moderate and 150 advanced.

The answers target modern Angular (v21 and later) with standalone components, signals and the esbuild-based application builder. Most examples use Native Federation (`@angular-architects/native-federation`), which is the usual choice for new Angular projects. Webpack Module Federation, Module Federation 2.0, Angular Elements, single-spa and iframes are also covered, since you will still meet them in real projects.

## Table of Contents

- [Easy Questions (1-150)](#easy-questions-1-150)
- [Moderate Questions (151-300)](#moderate-questions-151-300)
- [Advanced Questions (301-450)](#advanced-questions-301-450)

### Easy Questions (1-150)

- [1: What is a micro frontend?](#1-what-is-a-micro-frontend)
- [2: Why would a company use micro frontends?](#2-why-would-a-company-use-micro-frontends)
- [3: What is a monolithic frontend?](#3-what-is-a-monolithic-frontend)
- [4: What is the difference between a micro frontend and a component library?](#4-what-is-the-difference-between-a-micro-frontend-and-a-component-library)
- [5: What is a shell (host) application?](#5-what-is-a-shell-host-application)
- [6: What is a remote application?](#6-what-is-a-remote-application)
- [7: What does "independent deployment" mean for micro frontends?](#7-what-does-independent-deployment-mean-for-micro-frontends)
- [8: What are the common ways to build micro frontends in Angular?](#8-what-are-the-common-ways-to-build-micro-frontends-in-angular)
- [9: What is Module Federation?](#9-what-is-module-federation)
- [10: What is Native Federation?](#10-what-is-native-federation)
- [11: Why can't you use webpack Module Federation with the default Angular builder?](#11-why-cant-you-use-webpack-module-federation-with-the-default-angular-builder)
- [12: Which package do you install to use Native Federation in Angular?](#12-which-package-do-you-install-to-use-native-federation-in-angular)
- [13: How do you turn an Angular app into a Native Federation remote?](#13-how-do-you-turn-an-angular-app-into-a-native-federation-remote)
- [14: How do you turn an Angular app into a Native Federation host?](#14-how-do-you-turn-an-angular-app-into-a-native-federation-host)
- [15: What is the federation.config file?](#15-what-is-the-federationconfig-file)
- [16: What does the "exposes" option do?](#16-what-does-the-exposes-option-do)
- [17: What does the "shared" option do?](#17-what-does-the-shared-option-do)
- [18: What does shareAll do?](#18-what-does-shareall-do)
- [19: What is the federation manifest?](#19-what-is-the-federation-manifest)
- [20: What is remoteEntry.json?](#20-what-is-remoteentryjson)
- [21: What does initFederation do?](#21-what-does-initfederation-do)
- [22: Why is the bootstrap code moved into a separate bootstrap.ts file?](#22-why-is-the-bootstrap-code-moved-into-a-separate-bootstrapts-file)
- [23: What does loadRemoteModule do?](#23-what-does-loadremotemodule-do)
- [24: How do you load a remote component in an Angular route?](#24-how-do-you-load-a-remote-component-in-an-angular-route)
- [25: How do you load a whole set of remote routes?](#25-how-do-you-load-a-whole-set-of-remote-routes)
- [26: What is the difference between a static and a dynamic host?](#26-what-is-the-difference-between-a-static-and-a-dynamic-host)
- [27: Can a micro frontend run on its own?](#27-can-a-micro-frontend-run-on-its-own)
- [28: How do you run a host and a remote locally?](#28-how-do-you-run-a-host-and-a-remote-locally)
- [29: Why does every micro frontend need its own port in development?](#29-why-does-every-micro-frontend-need-its-own-port-in-development)
- [30: What is a vertical split?](#30-what-is-a-vertical-split)
- [31: What is a horizontal split?](#31-what-is-a-horizontal-split)
- [32: How should you decide where to split an app into micro frontends?](#32-how-should-you-decide-where-to-split-an-app-into-micro-frontends)
- [33: What is a bounded context and why does it matter here?](#33-what-is-a-bounded-context-and-why-does-it-matter-here)
- [34: What are the main downsides of micro frontends?](#34-what-are-the-main-downsides-of-micro-frontends)
- [35: When should you NOT use micro frontends?](#35-when-should-you-not-use-micro-frontends)
- [36: What is the difference between runtime and build-time integration?](#36-what-is-the-difference-between-runtime-and-build-time-integration)
- [37: What is Angular Elements?](#37-what-is-angular-elements)
- [38: How do you create a custom element from an Angular component?](#38-how-do-you-create-a-custom-element-from-an-angular-component)
- [39: What is a web component?](#39-what-is-a-web-component)
- [40: What is single-spa?](#40-what-is-single-spa)
- [41: What is the iframe approach to micro frontends?](#41-what-is-the-iframe-approach-to-micro-frontends)
- [42: What is a singleton shared dependency?](#42-what-is-a-singleton-shared-dependency)
- [43: What does strictVersion do?](#43-what-does-strictversion-do)
- [44: What does requiredVersion: 'auto' mean?](#44-what-does-requiredversion-auto-mean)
- [45: Why do micro frontends need to agree on the Angular version?](#45-why-do-micro-frontends-need-to-agree-on-the-angular-version)
- [46: What is an import map?](#46-what-is-an-import-map)
- [47: What is an ES module?](#47-what-is-an-es-module)
- [48: What is lazy loading and how does it relate to micro frontends?](#48-what-is-lazy-loading-and-how-does-it-relate-to-micro-frontends)
- [49: What is the "remote" name used for?](#49-what-is-the-remote-name-used-for)
- [50: What is an exposed module name like './Component'?](#50-what-is-an-exposed-module-name-like-component)
- [51: What is the @angular-architects/module-federation package?](#51-what-is-the-angular-architectsmodule-federation-package)
- [52: How do you set up a webpack Module Federation remote in Angular?](#52-how-do-you-set-up-a-webpack-module-federation-remote-in-angular)
- [53: What does a webpack.config.js for an Angular remote look like?](#53-what-does-a-webpackconfigjs-for-an-angular-remote-look-like)
- [54: How do you load a remote with webpack Module Federation in Angular?](#54-how-do-you-load-a-remote-with-webpack-module-federation-in-angular)
- [55: What is remoteEntry.js?](#55-what-is-remoteentryjs)
- [56: What is the difference between the shell and a remote in terms of who owns what?](#56-what-is-the-difference-between-the-shell-and-a-remote-in-terms-of-who-owns-what)
- [57: What happens if a remote is down?](#57-what-happens-if-a-remote-is-down)
- [58: How do you show a fallback when a remote fails to load?](#58-how-do-you-show-a-fallback-when-a-remote-fails-to-load)
- [59: Can micro frontends use different frameworks?](#59-can-micro-frontends-use-different-frameworks)
- [60: What is a monorepo?](#60-what-is-a-monorepo)
- [61: What is a polyrepo?](#61-what-is-a-polyrepo)
- [62: How do you create several Angular projects in one workspace?](#62-how-do-you-create-several-angular-projects-in-one-workspace)
- [63: What is Nx and why is it used with micro frontends?](#63-what-is-nx-and-why-is-it-used-with-micro-frontends)
- [64: How do you generate a host with remotes using Nx?](#64-how-do-you-generate-a-host-with-remotes-using-nx)
- [65: What is a design system and why is it important for micro frontends?](#65-what-is-a-design-system-and-why-is-it-important-for-micro-frontends)
- [66: What is the problem with global CSS in micro frontends?](#66-what-is-the-problem-with-global-css-in-micro-frontends)
- [67: How does Angular's view encapsulation help with micro frontends?](#67-how-does-angulars-view-encapsulation-help-with-micro-frontends)
- [68: What is Shadow DOM?](#68-what-is-shadow-dom)
- [69: How do micro frontends talk to each other?](#69-how-do-micro-frontends-talk-to-each-other)
- [70: Why should communication between micro frontends be kept small?](#70-why-should-communication-between-micro-frontends-be-kept-small)
- [71: How do you send a message between micro frontends with a custom event?](#71-how-do-you-send-a-message-between-micro-frontends-with-a-custom-event)
- [72: What is the URL's role in micro frontend communication?](#72-what-is-the-urls-role-in-micro-frontend-communication)
- [73: Can micro frontends share an Angular service?](#73-can-micro-frontends-share-an-angular-service)
- [74: What is a shared library in a micro frontend setup?](#74-what-is-a-shared-library-in-a-micro-frontend-setup)
- [75: How do you share a local monorepo library with Native Federation?](#75-how-do-you-share-a-local-monorepo-library-with-native-federation)
- [76: What is the "skip" option in the federation config?](#76-what-is-the-skip-option-in-the-federation-config)
- [77: What happens if a library is not shared?](#77-what-happens-if-a-library-is-not-shared)
- [78: How does routing work in a micro frontend shell?](#78-how-does-routing-work-in-a-micro-frontend-shell)
- [79: Should a remote have its own router?](#79-should-a-remote-have-its-own-router)
- [80: What is a "page-level" micro frontend?](#80-what-is-a-page-level-micro-frontend)
- [81: What is a "widget" or "fragment" micro frontend?](#81-what-is-a-widget-or-fragment-micro-frontend)
- [82: How do you load a remote component without the router?](#82-how-do-you-load-a-remote-component-without-the-router)
- [83: What is the difference between loadComponent and loadChildren for remotes?](#83-what-is-the-difference-between-loadcomponent-and-loadchildren-for-remotes)
- [84: Do remotes need to be standalone components?](#84-do-remotes-need-to-be-standalone-components)
- [85: How do you expose an NgModule from a remote (legacy)?](#85-how-do-you-expose-an-ngmodule-from-a-remote-legacy)
- [86: Where does the shell's layout live and where do remotes render?](#86-where-does-the-shells-layout-live-and-where-do-remotes-render)
- [87: What is the role of the CDN in micro frontends?](#87-what-is-the-role-of-the-cdn-in-micro-frontends)
- [88: Why shouldn't remoteEntry.json be cached for a long time?](#88-why-shouldnt-remoteentryjson-be-cached-for-a-long-time)
- [89: What is CORS and why does it matter for micro frontends?](#89-what-is-cors-and-why-does-it-matter-for-micro-frontends)
- [90: Do micro frontends need to be on the same domain?](#90-do-micro-frontends-need-to-be-on-the-same-domain)
- [91: What is a reverse proxy in this context?](#91-what-is-a-reverse-proxy-in-this-context)
- [92: How do you configure environment-specific remote URLs?](#92-how-do-you-configure-environment-specific-remote-urls)
- [93: Can you pass an object instead of a URL to initFederation?](#93-can-you-pass-an-object-instead-of-a-url-to-initfederation)
- [94: What is a contract between micro frontends?](#94-what-is-a-contract-between-micro-frontends)
- [95: How do you keep contracts typed between micro frontends?](#95-how-do-you-keep-contracts-typed-between-micro-frontends)
- [96: Can you use TypeScript types for a remote that is loaded at runtime?](#96-can-you-use-typescript-types-for-a-remote-that-is-loaded-at-runtime)
- [97: What is a "standalone mode" for a remote?](#97-what-is-a-standalone-mode-for-a-remote)
- [98: What is the difference between the remote's AppComponent and its exposed component?](#98-what-is-the-difference-between-the-remotes-appcomponent-and-its-exposed-component)
- [99: How do you build a micro frontend for production?](#99-how-do-you-build-a-micro-frontend-for-production)
- [100: Do you need to rebuild the shell when a remote changes?](#100-do-you-need-to-rebuild-the-shell-when-a-remote-changes)
- [101: What is the difference between Module Federation and Native Federation in simple words?](#101-what-is-the-difference-between-module-federation-and-native-federation-in-simple-words)
- [102: Is Native Federation part of the official Angular framework?](#102-is-native-federation-part-of-the-official-angular-framework)
- [103: How do you check that federation is set up correctly in a remote?](#103-how-do-you-check-that-federation-is-set-up-correctly-in-a-remote)
- [104: What changes does the Native Federation schematic make in angular.json?](#104-what-changes-does-the-native-federation-schematic-make-in-angularjson)
- [105: What is the bootstrap.ts file in a Native Federation app?](#105-what-is-the-bootstrapts-file-in-a-native-federation-app)
- [106: What does a remote's main.ts look like with Native Federation?](#106-what-does-a-remotes-maints-look-like-with-native-federation)
- [107: What is a micro frontend "team topology"?](#107-what-is-a-micro-frontend-team-topology)
- [108: What is a platform team?](#108-what-is-a-platform-team)
- [109: What is "Conway's Law" and how does it relate to micro frontends?](#109-what-is-conways-law-and-how-does-it-relate-to-micro-frontends)
- [110: Can one team own more than one micro frontend?](#110-can-one-team-own-more-than-one-micro-frontend)
- [111: What is a "remote entry point"?](#111-what-is-a-remote-entry-point)
- [112: How do you add a new remote to an existing dynamic host?](#112-how-do-you-add-a-new-remote-to-an-existing-dynamic-host)
- [113: What does it mean to "expose routes" from a remote?](#113-what-does-it-mean-to-expose-routes-from-a-remote)
- [114: What does "standalone" mean in Angular and why does it help micro frontends?](#114-what-does-standalone-mean-in-angular-and-why-does-it-help-micro-frontends)
- [115: What is the role of providers in an exposed routes file?](#115-what-is-the-role-of-providers-in-an-exposed-routes-file)
- [116: Why shouldn't a remote rely on the shell's app.config providers?](#116-why-shouldnt-a-remote-rely-on-the-shells-appconfig-providers)
- [117: What is a "shared state" problem in micro frontends?](#117-what-is-a-shared-state-problem-in-micro-frontends)
- [118: How do you share the logged-in user between micro frontends?](#118-how-do-you-share-the-logged-in-user-between-micro-frontends)
- [119: How do micro frontends handle authentication tokens?](#119-how-do-micro-frontends-handle-authentication-tokens)
- [120: Should each micro frontend have its own HTTP interceptors?](#120-should-each-micro-frontend-have-its-own-http-interceptors)
- [121: How do micro frontends share translations (i18n)?](#121-how-do-micro-frontends-share-translations-i18n)
- [122: Does Native Federation work with Angular's built-in i18n (@angular/localize)?](#122-does-native-federation-work-with-angulars-built-in-i18n-angularlocalize)
- [123: What is a "micro frontend registry"?](#123-what-is-a-micro-frontend-registry)
- [124: How can a shell build its menu from the remote list?](#124-how-can-a-shell-build-its-menu-from-the-remote-list)
- [125: What does router.resetConfig do?](#125-what-does-routerresetconfig-do)
- [126: What is provideAppInitializer and how is it used in micro frontends?](#126-what-is-provideappinitializer-and-how-is-it-used-in-micro-frontends)
- [127: What is the "mount" step of a micro frontend?](#127-what-is-the-mount-step-of-a-micro-frontend)
- [128: What is the "unmount" step and why does it matter?](#128-what-is-the-unmount-step-and-why-does-it-matter)
- [129: How do you clean up global listeners in a remote component?](#129-how-do-you-clean-up-global-listeners-in-a-remote-component)
- [130: What does "loosely coupled" mean for micro frontends?](#130-what-does-loosely-coupled-mean-for-micro-frontends)
- [131: What does "high cohesion" mean for micro frontends?](#131-what-does-high-cohesion-mean-for-micro-frontends)
- [132: Can you lazy load a remote only when a user clicks a button?](#132-can-you-lazy-load-a-remote-only-when-a-user-clicks-a-button)
- [133: What is the "version skew" problem?](#133-what-is-the-version-skew-problem)
- [134: What is semantic versioning and why is it used for shared libraries?](#134-what-is-semantic-versioning-and-why-is-it-used-for-shared-libraries)
- [135: What is the difference between ^ and ~ in a version range?](#135-what-is-the-difference-between--and--in-a-version-range)
- [136: What is "eager" in Module Federation shared config?](#136-what-is-eager-in-module-federation-shared-config)
- [137: What is the "Shared module is not available for eager consumption" error?](#137-what-is-the-shared-module-is-not-available-for-eager-consumption-error)
- [138: What is a federated module?](#138-what-is-a-federated-module)
- [139: What tools can you use to see what a remote loads in the browser?](#139-what-tools-can-you-use-to-see-what-a-remote-loads-in-the-browser)
- [140: What is the most common beginner mistake with micro frontends?](#140-what-is-the-most-common-beginner-mistake-with-micro-frontends)
- [141: Can you use Angular signals across micro frontends?](#141-can-you-use-angular-signals-across-micro-frontends)
- [142: Can you use NgRx in micro frontends?](#142-can-you-use-ngrx-in-micro-frontends)
- [143: What is a "smart shell" and a "dumb shell"?](#143-what-is-a-smart-shell-and-a-dumb-shell)
- [144: What are the benefits of using one framework (Angular) for all micro frontends?](#144-what-are-the-benefits-of-using-one-framework-angular-for-all-micro-frontends)
- [145: What is SSR and does it work with micro frontends?](#145-what-is-ssr-and-does-it-work-with-micro-frontends)
- [146: What is the difference between "client-side composition" and "server-side composition"?](#146-what-is-the-difference-between-client-side-composition-and-server-side-composition)
- [147: What is edge-side composition?](#147-what-is-edge-side-composition)
- [148: Do remotes need their own index.html?](#148-do-remotes-need-their-own-indexhtml)
- [149: Where do global styles go in a micro frontend setup?](#149-where-do-global-styles-go-in-a-micro-frontend-setup)
- [150: How would you explain micro frontends to a non-technical person?](#150-how-would-you-explain-micro-frontends-to-a-non-technical-person)

### Moderate Questions (151-300)

- [151: How does Native Federation load shared packages at runtime, step by step?](#151-how-does-native-federation-load-shared-packages-at-runtime-step-by-step)
- [152: How does Native Federation prepare npm packages for sharing at build time?](#152-how-does-native-federation-prepare-npm-packages-for-sharing-at-build-time)
- [153: Why is the first Native Federation build slower than the next ones?](#153-why-is-the-first-native-federation-build-slower-than-the-next-ones)
- [154: What happens when the host and a remote share the same package with different versions?](#154-what-happens-when-the-host-and-a-remote-share-the-same-package-with-different-versions)
- [155: When would you share a package without singleton?](#155-when-would-you-share-a-package-without-singleton)
- [156: How do you share only some packages instead of using shareAll?](#156-how-do-you-share-only-some-packages-instead-of-using-shareall)
- [157: What are secondary entry points and why do they matter for sharing?](#157-what-are-secondary-entry-points-and-why-do-they-matter-for-sharing)
- [158: What does the ignoreUnusedDeps feature do in Native Federation?](#158-what-does-the-ignoreunuseddeps-feature-do-in-native-federation)
- [159: Why do some npm packages fail to build with Native Federation?](#159-why-do-some-npm-packages-fail-to-build-with-native-federation)
- [160: How do you debug "Shared package not found" or version errors?](#160-how-do-you-debug-shared-package-not-found-or-version-errors)
- [161: How do you keep dependency versions aligned across many micro frontends?](#161-how-do-you-keep-dependency-versions-aligned-across-many-micro-frontends)
- [162: What is the single version policy?](#162-what-is-the-single-version-policy)
- [163: How do you upgrade Angular across a micro frontend system?](#163-how-do-you-upgrade-angular-across-a-micro-frontend-system)
- [164: Can you upgrade one micro frontend to a new Angular major without the others?](#164-can-you-upgrade-one-micro-frontend-to-a-new-angular-major-without-the-others)
- [165: What does a Native Federation host's federation config look like?](#165-what-does-a-native-federation-hosts-federation-config-look-like)
- [166: Can a remote also be a host?](#166-can-a-remote-also-be-a-host)
- [167: How do you handle a remote that exposes several components?](#167-how-do-you-handle-a-remote-that-exposes-several-components)
- [168: Should you expose many small components or a few big entry points?](#168-should-you-expose-many-small-components-or-a-few-big-entry-points)
- [169: How do you pass inputs to a remote component loaded dynamically?](#169-how-do-you-pass-inputs-to-a-remote-component-loaded-dynamically)
- [170: How do you listen to outputs of a dynamically loaded remote component?](#170-how-do-you-listen-to-outputs-of-a-dynamically-loaded-remote-component)
- [171: What is inputBinding and outputBinding in createComponent?](#171-what-is-inputbinding-and-outputbinding-in-createcomponent)
- [172: How do you configure a remote route to keep the shell's layout?](#172-how-do-you-configure-a-remote-route-to-keep-the-shells-layout)
- [173: How do you handle a full-screen remote that shouldn't show the shell's layout?](#173-how-do-you-handle-a-full-screen-remote-that-shouldnt-show-the-shells-layout)
- [174: How do you protect remote routes with guards?](#174-how-do-you-protect-remote-routes-with-guards)
- [175: Who should own the guards: the shell or the remote?](#175-who-should-own-the-guards-the-shell-or-the-remote)
- [176: How do you navigate from one micro frontend to another?](#176-how-do-you-navigate-from-one-micro-frontend-to-another)
- [177: Why is hard-coding another micro frontend's routes a problem?](#177-why-is-hard-coding-another-micro-frontends-routes-a-problem)
- [178: How do you keep two Angular routers in sync when using web components?](#178-how-do-you-keep-two-angular-routers-in-sync-when-using-web-components)
- [179: What is a wildcard route in a remote and why be careful with it?](#179-what-is-a-wildcard-route-in-a-remote-and-why-be-careful-with-it)
- [180: How do you test a remote in isolation?](#180-how-do-you-test-a-remote-in-isolation)
- [181: How do you test the shell without real remotes?](#181-how-do-you-test-the-shell-without-real-remotes)
- [182: What is contract testing for micro frontends?](#182-what-is-contract-testing-for-micro-frontends)
- [183: How do you do end-to-end tests for the whole micro frontend system?](#183-how-do-you-do-end-to-end-tests-for-the-whole-micro-frontend-system)
- [184: How do you set up CI/CD for micro frontends?](#184-how-do-you-set-up-cicd-for-micro-frontends)
- [185: How do you deploy a new version of a remote?](#185-how-do-you-deploy-a-new-version-of-a-remote)
- [186: Why should old chunk files stay on the server after a deployment?](#186-why-should-old-chunk-files-stay-on-the-server-after-a-deployment)
- [187: How do you roll back a broken remote deployment?](#187-how-do-you-roll-back-a-broken-remote-deployment)
- [188: What is versioned deployment of remotes?](#188-what-is-versioned-deployment-of-remotes)
- [189: How can you test a new remote version in production before releasing it to everyone?](#189-how-can-you-test-a-new-remote-version-in-production-before-releasing-it-to-everyone)
- [190: What is a canary release for micro frontends?](#190-what-is-a-canary-release-for-micro-frontends)
- [191: How do you use feature flags with micro frontends?](#191-how-do-you-use-feature-flags-with-micro-frontends)
- [192: How do you make the shell show a loading state while a remote loads?](#192-how-do-you-make-the-shell-show-a-loading-state-while-a-remote-loads)
- [193: How do you retry loading a remote after a network error?](#193-how-do-you-retry-loading-a-remote-after-a-network-error)
- [194: What happens if a remote's remoteEntry.json fails to load during initFederation?](#194-what-happens-if-a-remotes-remoteentryjson-fails-to-load-during-initfederation)
- [195: How do you track errors in micro frontends?](#195-how-do-you-track-errors-in-micro-frontends)
- [196: How can you know which micro frontend an error came from?](#196-how-can-you-know-which-micro-frontend-an-error-came-from)
- [197: How do you handle source maps in micro frontends?](#197-how-do-you-handle-source-maps-in-micro-frontends)
- [198: How do you debug a remote while it's running inside the shell?](#198-how-do-you-debug-a-remote-while-its-running-inside-the-shell)
- [199: How do you point a deployed shell to a local remote for debugging?](#199-how-do-you-point-a-deployed-shell-to-a-local-remote-for-debugging)
- [200: How do you share a design system across micro frontends?](#200-how-do-you-share-a-design-system-across-micro-frontends)
- [201: How do you theme micro frontends so they look the same?](#201-how-do-you-theme-micro-frontends-so-they-look-the-same)
- [202: How do you use Angular Material in micro frontends?](#202-how-do-you-use-angular-material-in-micro-frontends)
- [203: What problems can CDK overlays cause in micro frontends?](#203-what-problems-can-cdk-overlays-cause-in-micro-frontends)
- [204: How do you prevent CSS class name clashes between micro frontends?](#204-how-do-you-prevent-css-class-name-clashes-between-micro-frontends)
- [205: What is the downside of using Shadow DOM for Angular micro frontends?](#205-what-is-the-downside-of-using-shadow-dom-for-angular-micro-frontends)
- [206: How does Tailwind CSS work with micro frontends?](#206-how-does-tailwind-css-work-with-micro-frontends)
- [207: How do you load fonts once for all micro frontends?](#207-how-do-you-load-fonts-once-for-all-micro-frontends)
- [208: How do you share images and static assets between micro frontends?](#208-how-do-you-share-images-and-static-assets-between-micro-frontends)
- [209: How do you fix asset paths in a remote loaded by the shell?](#209-how-do-you-fix-asset-paths-in-a-remote-loaded-by-the-shell)
- [210: What is the difference between deployUrl and baseHref?](#210-what-is-the-difference-between-deployurl-and-basehref)
- [211: How do you share data between micro frontends with a shared service using signals?](#211-how-do-you-share-data-between-micro-frontends-with-a-shared-service-using-signals)
- [212: What are the risks of sharing state through a common service?](#212-what-are-the-risks-of-sharing-state-through-a-common-service)
- [213: How do you use BroadcastChannel between micro frontends?](#213-how-do-you-use-broadcastchannel-between-micro-frontends)
- [214: How do you create a small typed event bus for micro frontends?](#214-how-do-you-create-a-small-typed-event-bus-for-micro-frontends)
- [215: Why use window events instead of an RxJS Subject for an event bus?](#215-why-use-window-events-instead-of-an-rxjs-subject-for-an-event-bus)
- [216: When would a missed event be a problem and how do you solve it?](#216-when-would-a-missed-event-be-a-problem-and-how-do-you-solve-it)
- [217: How do you share data through web component attributes and properties?](#217-how-do-you-share-data-through-web-component-attributes-and-properties)
- [218: How does Angular Elements map inputs and outputs?](#218-how-does-angular-elements-map-inputs-and-outputs)
- [219: How do you use an Angular Elements micro frontend inside an Angular shell?](#219-how-do-you-use-an-angular-elements-micro-frontend-inside-an-angular-shell)
- [220: What is CUSTOM_ELEMENTS_SCHEMA?](#220-what-is-custom_elements_schema)
- [221: How do you combine Native Federation and web components?](#221-how-do-you-combine-native-federation-and-web-components)
- [222: How does Native Federation handle remotes built with other frameworks?](#222-how-does-native-federation-handle-remotes-built-with-other-frameworks)
- [223: What is @angular-architects/module-federation-tools?](#223-what-is-angular-architectsmodule-federation-tools)
- [224: How do you write a small wrapper component for a web component remote?](#224-how-do-you-write-a-small-wrapper-component-for-a-web-component-remote)
- [225: What is single-spa's root config?](#225-what-is-single-spas-root-config)
- [226: What does single-spa-angular do?](#226-what-does-single-spa-angular-do)
- [227: What are the downsides of single-spa compared to federation?](#227-what-are-the-downsides-of-single-spa-compared-to-federation)
- [228: When would single-spa still be a good choice?](#228-when-would-single-spa-still-be-a-good-choice)
- [229: How do you migrate from webpack Module Federation to Native Federation?](#229-how-do-you-migrate-from-webpack-module-federation-to-native-federation)
- [230: Can a Native Federation host load a webpack Module Federation remote?](#230-can-a-native-federation-host-load-a-webpack-module-federation-remote)
- [231: What is ngx-build-plus?](#231-what-is-ngx-build-plus)
- [232: What is Module Federation 2.0?](#232-what-is-module-federation-20)
- [233: What is Rspack and how does it relate to Angular micro frontends?](#233-what-is-rspack-and-how-does-it-relate-to-angular-micro-frontends)
- [234: What is mf-manifest.json?](#234-what-is-mf-manifestjson)
- [235: How do you load a remote with the Module Federation 2.0 runtime API?](#235-how-do-you-load-a-remote-with-the-module-federation-20-runtime-api)
- [236: How do you register remotes at runtime with Module Federation 2.0?](#236-how-do-you-register-remotes-at-runtime-with-module-federation-20)
- [237: How does Nx help run micro frontends locally?](#237-how-does-nx-help-run-micro-frontends-locally)
- [238: What is the Nx project graph and why is it useful here?](#238-what-is-the-nx-project-graph-and-why-is-it-useful-here)
- [239: How do you stop one micro frontend from importing another's code in a monorepo?](#239-how-do-you-stop-one-micro-frontend-from-importing-anothers-code-in-a-monorepo)
- [240: What is Sheriff?](#240-what-is-sheriff)
- [241: What is a "micro frontend per route" vs "micro frontend per component" decision?](#241-what-is-a-micro-frontend-per-route-vs-micro-frontend-per-component-decision)
- [242: How do you handle a remote that's slow to load?](#242-how-do-you-handle-a-remote-thats-slow-to-load)
- [243: How do you preload a remote before the user navigates to it?](#243-how-do-you-preload-a-remote-before-the-user-navigates-to-it)
- [244: Does Angular's PreloadAllModules work with remote routes?](#244-does-angulars-preloadallmodules-work-with-remote-routes)
- [245: How do you write a custom preloading strategy for remotes?](#245-how-do-you-write-a-custom-preloading-strategy-for-remotes)
- [246: How do you measure the bundle size of each micro frontend?](#246-how-do-you-measure-the-bundle-size-of-each-micro-frontend)
- [247: How do you set bundle budgets for micro frontends?](#247-how-do-you-set-bundle-budgets-for-micro-frontends)
- [248: What are Web Vitals and why do they matter more with micro frontends?](#248-what-are-web-vitals-and-why-do-they-matter-more-with-micro-frontends)
- [249: How do you avoid layout shift when a remote widget loads?](#249-how-do-you-avoid-layout-shift-when-a-remote-widget-loads)
- [250: How do you handle the user's language and locale across micro frontends?](#250-how-do-you-handle-the-users-language-and-locale-across-micro-frontends)
- [251: How do you share LOCALE_ID across micro frontends?](#251-how-do-you-share-locale_id-across-micro-frontends)
- [252: What is the difference between a remote's standalone appConfig and the providers it gets inside the shell?](#252-what-is-the-difference-between-a-remotes-standalone-appconfig-and-the-providers-it-gets-inside-the-shell)
- [253: How do you make a remote work both standalone and inside the shell without duplicating providers?](#253-how-do-you-make-a-remote-work-both-standalone-and-inside-the-shell-without-duplicating-providers)
- [254: What is the danger of calling provideHttpClient() again in a remote's routes?](#254-what-is-the-danger-of-calling-providehttpclient-again-in-a-remotes-routes)
- [255: How do you add a remote's NgRx feature state when loaded into the shell?](#255-how-do-you-add-a-remotes-ngrx-feature-state-when-loaded-into-the-shell)
- [256: Why is NgRx SignalStore often a better fit for remotes than a global store?](#256-why-is-ngrx-signalstore-often-a-better-fit-for-remotes-than-a-global-store)
- [257: How do you avoid duplicate HTTP requests when several micro frontends need the same data?](#257-how-do-you-avoid-duplicate-http-requests-when-several-micro-frontends-need-the-same-data)
- [258: How do you handle logout across micro frontends?](#258-how-do-you-handle-logout-across-micro-frontends)
- [259: How do you share permissions or roles with micro frontends?](#259-how-do-you-share-permissions-or-roles-with-micro-frontends)
- [260: How do you handle different back-end APIs for each micro frontend?](#260-how-do-you-handle-different-back-end-apis-for-each-micro-frontend)
- [261: What is a Backend For Frontend (BFF) in this context?](#261-what-is-a-backend-for-frontend-bff-in-this-context)
- [262: How do you load runtime configuration in a remote?](#262-how-do-you-load-runtime-configuration-in-a-remote)
- [263: Why might environment.ts files be a problem in micro frontends?](#263-why-might-environmentts-files-be-a-problem-in-micro-frontends)
- [264: How do you handle CORS for API calls from remotes?](#264-how-do-you-handle-cors-for-api-calls-from-remotes)
- [265: How do you set up a dev proxy when running a remote inside the shell?](#265-how-do-you-set-up-a-dev-proxy-when-running-a-remote-inside-the-shell)
- [266: How do remotes use the shell's HTTP interceptors?](#266-how-do-remotes-use-the-shells-http-interceptors)
- [267: How do you show global notifications (toasts) from any micro frontend?](#267-how-do-you-show-global-notifications-toasts-from-any-micro-frontend)
- [268: How do you handle dialogs opened by a remote?](#268-how-do-you-handle-dialogs-opened-by-a-remote)
- [269: How do you handle the browser back button with micro frontends?](#269-how-do-you-handle-the-browser-back-button-with-micro-frontends)
- [270: How do you pass route parameters from the shell to a remote?](#270-how-do-you-pass-route-parameters-from-the-shell-to-a-remote)
- [271: What is the role of data in remote routes?](#271-what-is-the-role-of-data-in-remote-routes)
- [272: How do you set the page title from a remote?](#272-how-do-you-set-the-page-title-from-a-remote)
- [273: How do you organize a monorepo with a shell, remotes and shared libraries?](#273-how-do-you-organize-a-monorepo-with-a-shell-remotes-and-shared-libraries)
- [274: How do you share code without sharing it at runtime?](#274-how-do-you-share-code-without-sharing-it-at-runtime)
- [275: When should a shared library be shared at runtime and when bundled?](#275-when-should-a-shared-library-be-shared-at-runtime-and-when-bundled)
- [276: How do you publish a shared Angular library to npm?](#276-how-do-you-publish-a-shared-angular-library-to-npm)
- [277: What are the trade-offs of a shared library in a polyrepo?](#277-what-are-the-trade-offs-of-a-shared-library-in-a-polyrepo)
- [278: How do you document what each micro frontend exposes?](#278-how-do-you-document-what-each-micro-frontend-exposes)
- [279: How do you handle breaking changes in an exposed module?](#279-how-do-you-handle-breaking-changes-in-an-exposed-module)
- [280: What is the "strangler fig" pattern?](#280-what-is-the-strangler-fig-pattern)
- [281: How do you migrate an AngularJS app to Angular using micro frontends?](#281-how-do-you-migrate-an-angularjs-app-to-angular-using-micro-frontends)
- [282: How do you split an existing Angular monolith into micro frontends?](#282-how-do-you-split-an-existing-angular-monolith-into-micro-frontends)
- [283: What is a "modular monolith" and how does it compare?](#283-what-is-a-modular-monolith-and-how-does-it-compare)
- [284: How do you decide between a modular monolith and micro frontends?](#284-how-do-you-decide-between-a-modular-monolith-and-micro-frontends)
- [285: What is the "distributed monolith" anti-pattern?](#285-what-is-the-distributed-monolith-anti-pattern)
- [286: What other anti-patterns are common with micro frontends?](#286-what-other-anti-patterns-are-common-with-micro-frontends)
- [287: How do you show a "not found" page for unknown routes under a remote?](#287-how-do-you-show-a-not-found-page-for-unknown-routes-under-a-remote)
- [288: How do you handle analytics tracking across micro frontends?](#288-how-do-you-handle-analytics-tracking-across-micro-frontends)
- [289: How do you check that a remote follows accessibility rules?](#289-how-do-you-check-that-a-remote-follows-accessibility-rules)
- [290: How should focus be handled when navigating between micro frontends?](#290-how-should-focus-be-handled-when-navigating-between-micro-frontends)
- [291: How do you keep the browser tab title and meta tags correct with remotes?](#291-how-do-you-keep-the-browser-tab-title-and-meta-tags-correct-with-remotes)
- [292: How do you handle a remote that needs a library the shell doesn't have?](#292-how-do-you-handle-a-remote-that-needs-a-library-the-shell-doesnt-have)
- [293: What happens if two remotes share a library but the shell doesn't use it?](#293-what-happens-if-two-remotes-share-a-library-but-the-shell-doesnt-use-it)
- [294: What is the order of loading in a Native Federation app?](#294-what-is-the-order-of-loading-in-a-native-federation-app)
- [295: How can you reduce the number of remoteEntry.json requests at startup?](#295-how-can-you-reduce-the-number-of-remoteentryjson-requests-at-startup)
- [296: How do you load remotes only for users who have access?](#296-how-do-you-load-remotes-only-for-users-who-have-access)
- [297: What should the shell do while initFederation is running?](#297-what-should-the-shell-do-while-initfederation-is-running)
- [298: How do you share a component that wraps a remote in several places of the shell?](#298-how-do-you-share-a-component-that-wraps-a-remote-in-several-places-of-the-shell)
- [299: How do you use @defer with remote widgets?](#299-how-do-you-use-defer-with-remote-widgets)
- [300: What questions would you ask before starting a micro frontend project?](#300-what-questions-would-you-ask-before-starting-a-micro-frontend-project)

### Advanced Questions (301-450)

- [301: Why exactly does having two copies of @angular/core break an app?](#301-why-exactly-does-having-two-copies-of-angularcore-break-an-app)
- [302: What is NG0203 and why does it often show up in micro frontend setups?](#302-what-is-ng0203-and-why-does-it-often-show-up-in-micro-frontend-setups)
- [303: How does Native Federation decide which version of a shared package wins?](#303-how-does-native-federation-decide-which-version-of-a-shared-package-wins)
- [304: Why does Native Federation use import maps instead of a custom loader?](#304-why-does-native-federation-use-import-maps-instead-of-a-custom-loader)
- [305: What limitations do import maps have that affect Native Federation?](#305-what-limitations-do-import-maps-have-that-affect-native-federation)
- [306: What is es-module-shims?](#306-what-is-es-module-shims)
- [307: How does Native Federation make a shared package available to a remote built separately?](#307-how-does-native-federation-make-a-shared-package-available-to-a-remote-built-separately)
- [308: How does webpack Module Federation share dependencies internally?](#308-how-does-webpack-module-federation-share-dependencies-internally)
- [309: What are `__webpack_init_sharing__` and `__webpack_share_scopes__`?](#309-what-are-__webpack_init_sharing__-and-__webpack_share_scopes__)
- [310: How would you build a simplified loadRemoteModule for Native Federation by hand?](#310-how-would-you-build-a-simplified-loadremotemodule-for-native-federation-by-hand)
- [311: Why does the remote's exposed code run against the host's import map instead of its own?](#311-why-does-the-remotes-exposed-code-run-against-the-hosts-import-map-instead-of-its-own)
- [312: How does Angular's esbuild builder output affect micro frontends?](#312-how-does-angulars-esbuild-builder-output-affect-micro-frontends)
- [313: What happens to tree shaking when you share a package?](#313-what-happens-to-tree-shaking-when-you-share-a-package)
- [314: How do shared packages affect initial load performance?](#314-how-do-shared-packages-affect-initial-load-performance)
- [315: How do you avoid a waterfall of requests when loading a remote?](#315-how-do-you-avoid-a-waterfall-of-requests-when-loading-a-remote)
- [316: How do you use modulepreload to speed up a remote?](#316-how-do-you-use-modulepreload-to-speed-up-a-remote)
- [317: How would you design caching for a micro frontend system?](#317-how-would-you-design-caching-for-a-micro-frontend-system)
- [318: What problem happens if a user has the app open during a remote deployment?](#318-what-problem-happens-if-a-user-has-the-app-open-during-a-remote-deployment)
- [319: How do you detect that a new version of a remote is available while the app is open?](#319-how-do-you-detect-that-a-new-version-of-a-remote-is-available-while-the-app-is-open)
- [320: How do you handle "Failed to fetch dynamically imported module" errors?](#320-how-do-you-handle-failed-to-fetch-dynamically-imported-module-errors)
- [321: What is a Service Worker and how can it interfere with micro frontends?](#321-what-is-a-service-worker-and-how-can-it-interfere-with-micro-frontends)
- [322: How do you guarantee one Angular platform when using Angular Elements micro frontends?](#322-how-do-you-guarantee-one-angular-platform-when-using-angular-elements-micro-frontends)
- [323: What are the real costs of running several Angular versions on one page?](#323-what-are-the-real-costs-of-running-several-angular-versions-on-one-page)
- [324: Why is Zone.js a problem when mixing Angular apps on one page?](#324-why-is-zonejs-a-problem-when-mixing-angular-apps-on-one-page)
- [325: How does zoneless change detection help micro frontends?](#325-how-does-zoneless-change-detection-help-micro-frontends)
- [326: What problem happens when a Zone.js remote runs in a zoneless shell?](#326-what-problem-happens-when-a-zonejs-remote-runs-in-a-zoneless-shell)
- [327: How do you design a micro frontend system so that teams can deploy on their own but Angular upgrades stay manageable?](#327-how-do-you-design-a-micro-frontend-system-so-that-teams-can-deploy-on-their-own-but-angular-upgrades-stay-manageable)
- [328: Why might you want the shell to own the versions of shared packages?](#328-why-might-you-want-the-shell-to-own-the-versions-of-shared-packages)
- [329: How would you enforce compatible versions at deploy time?](#329-how-would-you-enforce-compatible-versions-at-deploy-time)
- [330: How do you share a library that has secondary entry points with different usage per remote?](#330-how-do-you-share-a-library-that-has-secondary-entry-points-with-different-usage-per-remote)
- [331: What is the problem with sharing a library that depends on a non-shared library?](#331-what-is-the-problem-with-sharing-a-library-that-depends-on-a-non-shared-library)
- [332: How do you share a package with a custom entry point or non-standard format?](#332-how-do-you-share-a-package-with-a-custom-entry-point-or-non-standard-format)
- [333: How do you handle CommonJS packages in a Native Federation setup?](#333-how-do-you-handle-commonjs-packages-in-a-native-federation-setup)
- [334: How would you share code between micro frontends built with different Angular major versions?](#334-how-would-you-share-code-between-micro-frontends-built-with-different-angular-major-versions)
- [335: How would you design a framework-neutral design system for mixed micro frontends?](#335-how-would-you-design-a-framework-neutral-design-system-for-mixed-micro-frontends)
- [336: How do you make a web component work with Angular forms?](#336-how-do-you-make-a-web-component-work-with-angular-forms)
- [337: How does Angular Elements handle change detection inside custom elements?](#337-how-does-angular-elements-handle-change-detection-inside-custom-elements)
- [338: What happens when an Angular custom element is removed from the DOM?](#338-what-happens-when-an-angular-custom-element-is-removed-from-the-dom)
- [339: How do you avoid defining the same custom element name twice?](#339-how-do-you-avoid-defining-the-same-custom-element-name-twice)
- [340: What are Scoped Custom Element Registries and why are they interesting for micro frontends?](#340-what-are-scoped-custom-element-registries-and-why-are-they-interesting-for-micro-frontends)
- [341: How would you embed an Angular micro frontend into a React host?](#341-how-would-you-embed-an-angular-micro-frontend-into-a-react-host)
- [342: How do you expose a mount/unmount API instead of a custom element?](#342-how-do-you-expose-a-mountunmount-api-instead-of-a-custom-element)
- [343: What is the trade-off between a mount function and a custom element as a remote's API?](#343-what-is-the-trade-off-between-a-mount-function-and-a-custom-element-as-a-remotes-api)
- [344: How do you keep memory from leaking when a remote is mounted and unmounted many times?](#344-how-do-you-keep-memory-from-leaking-when-a-remote-is-mounted-and-unmounted-many-times)
- [345: How do you isolate a remote's errors so they don't crash the shell?](#345-how-do-you-isolate-a-remotes-errors-so-they-dont-crash-the-shell)
- [346: How would you build an "error boundary" component for remote widgets in Angular?](#346-how-would-you-build-an-error-boundary-component-for-remote-widgets-in-angular)
- [347: How do you secure a micro frontend system against loading malicious code?](#347-how-do-you-secure-a-micro-frontend-system-against-loading-malicious-code)
- [348: How does Content Security Policy (CSP) work with micro frontends?](#348-how-does-content-security-policy-csp-work-with-micro-frontends)
- [349: Why is Subresource Integrity (SRI) hard to use with runtime-loaded remotes?](#349-why-is-subresource-integrity-sri-hard-to-use-with-runtime-loaded-remotes)
- [350: What are the XSS risks specific to micro frontends?](#350-what-are-the-xss-risks-specific-to-micro-frontends)
- [351: How should authentication tokens be stored in a micro frontend system?](#351-how-should-authentication-tokens-be-stored-in-a-micro-frontend-system)
- [352: How do you implement single sign-on (SSO) across micro frontends?](#352-how-do-you-implement-single-sign-on-sso-across-micro-frontends)
- [353: What is the "BFF pattern for auth" and why is it recommended for SPAs today?](#353-what-is-the-bff-pattern-for-auth-and-why-is-it-recommended-for-spas-today)
- [354: How would you design permissions so remotes don't need shell changes for new rules?](#354-how-would-you-design-permissions-so-remotes-dont-need-shell-changes-for-new-rules)
- [355: How do you make sure one remote can't read another remote's data in the browser?](#355-how-do-you-make-sure-one-remote-cant-read-another-remotes-data-in-the-browser)
- [356: How do you communicate safely with an iframe micro frontend?](#356-how-do-you-communicate-safely-with-an-iframe-micro-frontend)
- [357: How do you design the shell for high availability?](#357-how-do-you-design-the-shell-for-high-availability)
- [358: How would you make initFederation resilient to a missing remote?](#358-how-would-you-make-initfederation-resilient-to-a-missing-remote)
- [359: How do you monitor the health of each micro frontend in production?](#359-how-do-you-monitor-the-health-of-each-micro-frontend-in-production)
- [360: How do you measure how long each remote takes to load?](#360-how-do-you-measure-how-long-each-remote-takes-to-load)
- [361: How do you decide what goes in the shell versus in a remote?](#361-how-do-you-decide-what-goes-in-the-shell-versus-in-a-remote)
- [362: How would you design the navigation menu so teams can add items without changing the shell?](#362-how-would-you-design-the-navigation-menu-so-teams-can-add-items-without-changing-the-shell)
- [363: How do you let remotes contribute items to shared UI areas like the header?](#363-how-do-you-let-remotes-contribute-items-to-shared-ui-areas-like-the-header)
- [364: How is a plugin architecture different from micro frontends?](#364-how-is-a-plugin-architecture-different-from-micro-frontends)
- [365: How do you handle a remote that must be available at startup, before any navigation?](#365-how-do-you-handle-a-remote-that-must-be-available-at-startup-before-any-navigation)
- [366: What is the impact of micro frontends on SEO?](#366-what-is-the-impact-of-micro-frontends-on-seo)
- [367: How does SSR work with Native Federation?](#367-how-does-ssr-work-with-native-federation)
- [368: What problems does SSR add to a micro frontend setup?](#368-what-problems-does-ssr-add-to-a-micro-frontend-setup)
- [369: How do you make a remote SSR-safe?](#369-how-do-you-make-a-remote-ssr-safe)
- [370: How does incremental hydration relate to micro frontends?](#370-how-does-incremental-hydration-relate-to-micro-frontends)
- [371: How would you architect a large e-commerce site with Angular micro frontends?](#371-how-would-you-architect-a-large-e-commerce-site-with-angular-micro-frontends)
- [372: How would you architect an internal admin portal with many teams?](#372-how-would-you-architect-an-internal-admin-portal-with-many-teams)
- [373: How would you migrate a big Angular 14 webpack Module Federation system to modern Angular?](#373-how-would-you-migrate-a-big-angular-14-webpack-module-federation-system-to-modern-angular)
- [374: What are the risks of a big-bang migration of all micro frontends at once?](#374-what-are-the-risks-of-a-big-bang-migration-of-all-micro-frontends-at-once)
- [375: How do you test version compatibility between shell and remotes automatically?](#375-how-do-you-test-version-compatibility-between-shell-and-remotes-automatically)
- [376: What is consumer-driven contract testing and how would you apply it here?](#376-what-is-consumer-driven-contract-testing-and-how-would-you-apply-it-here)
- [377: How do you test a remote's exposed module without the shell?](#377-how-do-you-test-a-remotes-exposed-module-without-the-shell)
- [378: How would you run end-to-end tests against several remote versions?](#378-how-would-you-run-end-to-end-tests-against-several-remote-versions)
- [379: How do you create preview environments for pull requests in a remote?](#379-how-do-you-create-preview-environments-for-pull-requests-in-a-remote)
- [380: How do you handle database or API changes that affect several micro frontends?](#380-how-do-you-handle-database-or-api-changes-that-affect-several-micro-frontends)
- [381: How would you handle shared state that must survive a page reload?](#381-how-would-you-handle-shared-state-that-must-survive-a-page-reload)
- [382: How do you avoid race conditions when several remotes load shared data at startup?](#382-how-do-you-avoid-race-conditions-when-several-remotes-load-shared-data-at-startup)
- [383: How do you version the shared event contracts?](#383-how-do-you-version-the-shared-event-contracts)
- [384: How do you trace a user action across several micro frontends and back-ends?](#384-how-do-you-trace-a-user-action-across-several-micro-frontends-and-back-ends)
- [385: How does OpenTelemetry fit into an Angular micro frontend setup?](#385-how-does-opentelemetry-fit-into-an-angular-micro-frontend-setup)
- [386: How would you handle a remote that blocks the main thread?](#386-how-would-you-handle-a-remote-that-blocks-the-main-thread)
- [387: How do Web Workers work in a federated remote?](#387-how-do-web-workers-work-in-a-federated-remote)
- [388: How do you handle cross-origin workers in remotes?](#388-how-do-you-handle-cross-origin-workers-in-remotes)
- [389: How do you handle the remote's global polyfills?](#389-how-do-you-handle-the-remotes-global-polyfills)
- [390: How do you choose which browsers to support across micro frontends?](#390-how-do-you-choose-which-browsers-to-support-across-micro-frontends)
- [391: How do you handle global configuration changes like a new theme across many remotes?](#391-how-do-you-handle-global-configuration-changes-like-a-new-theme-across-many-remotes)
- [392: What is the impact of shared singletons on the ability of remotes to run standalone?](#392-what-is-the-impact-of-shared-singletons-on-the-ability-of-remotes-to-run-standalone)
- [393: How can a remote know whether it's running standalone or inside the shell?](#393-how-can-a-remote-know-whether-its-running-standalone-or-inside-the-shell)
- [394: Why must injection tokens used across micro frontends come from a shared library?](#394-why-must-injection-tokens-used-across-micro-frontends-come-from-a-shared-library)
- [395: What is the problem with abstract class tokens across micro frontends?](#395-what-is-the-problem-with-abstract-class-tokens-across-micro-frontends)
- [396: How do you detect that a library is accidentally bundled twice?](#396-how-do-you-detect-that-a-library-is-accidentally-bundled-twice)
- [397: How can you prevent a library from being instantiated twice even if bundled twice?](#397-how-can-you-prevent-a-library-from-being-instantiated-twice-even-if-bundled-twice)
- [398: How do you share state between Angular and non-Angular micro frontends?](#398-how-do-you-share-state-between-angular-and-non-angular-micro-frontends)
- [399: How do you convert a framework-neutral store into an Angular signal?](#399-how-do-you-convert-a-framework-neutral-store-into-an-angular-signal)
- [400: How would you explain the trade-off between isolation and integration in micro frontends?](#400-how-would-you-explain-the-trade-off-between-isolation-and-integration-in-micro-frontends)
- [401: Scenario: after a remote deployment, users report a blank page on one route. How do you investigate?](#401-scenario-after-a-remote-deployment-users-report-a-blank-page-on-one-route-how-do-you-investigate)
- [402: Scenario: a service from a shared library has different state in the shell and in a remote. What's going on?](#402-scenario-a-service-from-a-shared-library-has-different-state-in-the-shell-and-in-a-remote-whats-going-on)
- [403: Scenario: the app works locally but a remote fails to load in production with a CORS error. What do you check?](#403-scenario-the-app-works-locally-but-a-remote-fails-to-load-in-production-with-a-cors-error-what-do-you-check)
- [404: Scenario: after upgrading Angular in the shell, one remote stopped working. How do you approach it?](#404-scenario-after-upgrading-angular-in-the-shell-one-remote-stopped-working-how-do-you-approach-it)
- [405: Scenario: the shell's initial load got 2 seconds slower after adding a few remotes. Where do you look?](#405-scenario-the-shells-initial-load-got-2-seconds-slower-after-adding-a-few-remotes-where-do-you-look)
- [406: Scenario: two teams both want to change the shared design system at the same time. How do you organize this?](#406-scenario-two-teams-both-want-to-change-the-shared-design-system-at-the-same-time-how-do-you-organize-this)
- [407: Scenario: a remote team wants to use React for their new feature. What do you consider?](#407-scenario-a-remote-team-wants-to-use-react-for-their-new-feature-what-do-you-consider)
- [408: Scenario: users see a flash of unstyled content when a remote loads. How do you fix it?](#408-scenario-users-see-a-flash-of-unstyled-content-when-a-remote-loads-how-do-you-fix-it)
- [409: Scenario: a remote's global CSS breaks the shell's layout. How do you prevent it in the future?](#409-scenario-a-remotes-global-css-breaks-the-shells-layout-how-do-you-prevent-it-in-the-future)
- [410: Scenario: the cart count in the header doesn't update after adding an item in a product remote. How do you debug?](#410-scenario-the-cart-count-in-the-header-doesnt-update-after-adding-an-item-in-a-product-remote-how-do-you-debug)
- [411: Scenario: a remote must run in two different shells (for example, customer portal and admin portal). How do you design it?](#411-scenario-a-remote-must-run-in-two-different-shells-for-example-customer-portal-and-admin-portal-how-do-you-design-it)
- [412: Scenario: one remote needs a newer version of a shared library than the shell provides. What are your options?](#412-scenario-one-remote-needs-a-newer-version-of-a-shared-library-than-the-shell-provides-what-are-your-options)
- [413: Scenario: you need to show an A/B test that swaps one micro frontend for another. How?](#413-scenario-you-need-to-show-an-ab-test-that-swaps-one-micro-frontend-for-another-how)
- [414: Scenario: a security audit finds that any user can override remote URLs with a query parameter. What do you do?](#414-scenario-a-security-audit-finds-that-any-user-can-override-remote-urls-with-a-query-parameter-what-do-you-do)
- [415: Scenario: the shell must work offline for field workers. How do micro frontends affect this?](#415-scenario-the-shell-must-work-offline-for-field-workers-how-do-micro-frontends-affect-this)
- [416: How would you design a versioning strategy for exposed modules?](#416-how-would-you-design-a-versioning-strategy-for-exposed-modules)
- [417: How does the choice between monorepo and polyrepo affect micro frontend independence?](#417-how-does-the-choice-between-monorepo-and-polyrepo-affect-micro-frontend-independence)
- [418: How would you set up deployment pipelines in an Nx monorepo so each remote deploys independently?](#418-how-would-you-set-up-deployment-pipelines-in-an-nx-monorepo-so-each-remote-deploys-independently)
- [419: What is the problem with "affected" when a shared library changes in a micro frontend monorepo?](#419-what-is-the-problem-with-affected-when-a-shared-library-changes-in-a-micro-frontend-monorepo)
- [420: How do you handle long-lived feature branches across micro frontends?](#420-how-do-you-handle-long-lived-feature-branches-across-micro-frontends)
- [421: How would you set up local development so a developer only runs what they need?](#421-how-would-you-set-up-local-development-so-a-developer-only-runs-what-they-need)
- [422: How do you share a mock back-end for micro frontend development?](#422-how-do-you-share-a-mock-back-end-for-micro-frontend-development)
- [423: How would you generate API clients for micro frontends?](#423-how-would-you-generate-api-clients-for-micro-frontends)
- [424: How does lazy loading inside a remote work under federation?](#424-how-does-lazy-loading-inside-a-remote-work-under-federation)
- [425: What happens if two remotes expose components with the same selector?](#425-what-happens-if-two-remotes-expose-components-with-the-same-selector)
- [426: How do you design remotes to be loaded multiple times on the same page?](#426-how-do-you-design-remotes-to-be-loaded-multiple-times-on-the-same-page)
- [427: How do you handle remotes that need different router configurations, like hash routing?](#427-how-do-you-handle-remotes-that-need-different-router-configurations-like-hash-routing)
- [428: What would you do if a team needs strong isolation for compliance reasons, like a payment form?](#428-what-would-you-do-if-a-team-needs-strong-isolation-for-compliance-reasons-like-a-payment-form)
- [429: How would you compare Native Federation, webpack Module Federation and Module Federation 2.0 for a new Angular project today?](#429-how-would-you-compare-native-federation-webpack-module-federation-and-module-federation-20-for-a-new-angular-project-today)
- [430: What would make you choose web components over federation for Angular micro frontends?](#430-what-would-make-you-choose-web-components-over-federation-for-angular-micro-frontends)
- [431: How would you share Angular itself when using Angular Elements micro frontends?](#431-how-would-you-share-angular-itself-when-using-angular-elements-micro-frontends)
- [432: What is "compile-time" versus "runtime" coupling between micro frontends?](#432-what-is-compile-time-versus-runtime-coupling-between-micro-frontends)
- [433: How do you handle the dependency on the shell's layout in a remote's design?](#433-how-do-you-handle-the-dependency-on-the-shells-layout-in-a-remotes-design)
- [434: How do you test a remote's visual appearance across shells and themes?](#434-how-do-you-test-a-remotes-visual-appearance-across-shells-and-themes)
- [435: How do you use Storybook with micro frontends?](#435-how-do-you-use-storybook-with-micro-frontends)
- [436: What metrics would show that micro frontends are actually helping the organization?](#436-what-metrics-would-show-that-micro-frontends-are-actually-helping-the-organization)
- [437: What are the hidden costs of micro frontends that teams often underestimate?](#437-what-are-the-hidden-costs-of-micro-frontends-that-teams-often-underestimate)
- [438: How would you reverse a micro frontend decision if it isn't working?](#438-how-would-you-reverse-a-micro-frontend-decision-if-it-isnt-working)
- [439: How does Angular's dependency injection hierarchy look when a remote is loaded via loadChildren?](#439-how-does-angulars-dependency-injection-hierarchy-look-when-a-remote-is-loaded-via-loadchildren)
- [440: What happens to services provided in a remote's route when the user navigates away?](#440-what-happens-to-services-provided-in-a-remotes-route-when-the-user-navigates-away)
- [441: How would you explain the difference between a remote's environment injector and the shell's root injector in an interview?](#441-how-would-you-explain-the-difference-between-a-remotes-environment-injector-and-the-shells-root-injector-in-an-interview)
- [442: How do you override a shell service for one remote only?](#442-how-do-you-override-a-shell-service-for-one-remote-only)
- [443: How would you load remotes based on a CMS-driven page layout?](#443-how-would-you-load-remotes-based-on-a-cms-driven-page-layout)
- [444: How do you keep a CMS-driven micro frontend page from becoming slow?](#444-how-do-you-keep-a-cms-driven-micro-frontend-page-from-becoming-slow)
- [445: How would you handle internationalized routes (like /de/orders) with remotes?](#445-how-would-you-handle-internationalized-routes-like-deorders-with-remotes)
- [446: What are the effects of micro frontends on accessibility landmarks and headings?](#446-what-are-the-effects-of-micro-frontends-on-accessibility-landmarks-and-headings)
- [447: How would you approach a performance budget for the whole system, not just per remote?](#447-how-would-you-approach-a-performance-budget-for-the-whole-system-not-just-per-remote)
- [448: How would you onboard a new team into an existing micro frontend platform?](#448-how-would-you-onboard-a-new-team-into-an-existing-micro-frontend-platform)
- [449: What would you put in a remote template or generator?](#449-what-would-you-put-in-a-remote-template-or-generator)
- [450: If you had to sum up the key principles of a good Angular micro frontend architecture, what would they be?](#450-if-you-had-to-sum-up-the-key-principles-of-a-good-angular-micro-frontend-architecture-what-would-they-be)

---

# Easy Questions (1-150)

## 1: What is a micro frontend?

A micro frontend is a part of a web app's UI that one team builds, tests and deploys on its own. You split a big front-end into smaller apps, for example "catalog", "cart" and "account", and put them together in the browser so the user still sees one application.

It is the same idea as microservices on the back-end, but applied to the UI.

## 2: Why would a company use micro frontends?

The main reasons are about teams, not technology:

- Several teams can work on the same product without blocking each other.
- Each team can release its part when it is ready, without waiting for a big shared release.
- A large code base is split into smaller pieces that are easier to understand.
- Old parts of the app can be rewritten one by one instead of all at once.

If you have one small team, you usually don't need micro frontends.

## 3: What is a monolithic frontend?

A monolithic frontend is one single front-end application that holds all features in one repository and one build. Every change goes through the same build and the same deployment.

This is the default for most Angular projects and it works well until the app and the number of teams get big. Then builds get slow, merges get painful and one broken feature can block the whole release.

## 4: What is the difference between a micro frontend and a component library?

A component library is a set of reusable UI pieces (buttons, inputs, dialogs) that you install as an npm package and use at build time. When the library changes, every app has to update the package and redeploy.

A micro frontend is a whole feature with its own routes, logic and data. It is usually loaded at runtime, so its team can deploy a new version without the other apps rebuilding.

## 5: What is a shell (host) application?

The shell, also called the host, is the main app the user opens first. It usually contains the layout (header, menu, footer), routing between features, login and other global things. It then loads the micro frontends into its pages.

The shell should stay small. If you put a lot of business logic into it, it turns into a new monolith.

## 6: What is a remote application?

A remote is a micro frontend that the shell loads. It is built and deployed separately and exposes some parts of itself, for example a component or a set of routes, so that the shell can load them at runtime.

A remote can usually also run on its own (standalone) during development.

## 7: What does "independent deployment" mean for micro frontends?

It means a team can put a new version of its micro frontend into production without rebuilding or redeploying the shell or other micro frontends. The shell loads the latest version from the remote's URL the next time the page loads.

This is one of the main benefits. If every change still needs a full rebuild of everything, you have the cost of micro frontends without the main advantage.

## 8: What are the common ways to build micro frontends in Angular?

The common options are:

- **Native Federation**, which works with Angular's esbuild-based build system.
- **Webpack Module Federation**, for projects that still use the webpack builder.
- **Angular Elements** (web components), which lets you wrap Angular components as custom HTML elements.
- **single-spa** with `single-spa-angular`, a framework that mounts and unmounts apps by route.
- **iframes**, the oldest and most isolated approach.
- **Build-time integration**, where each micro frontend is an npm package installed into the shell.

## 9: What is Module Federation?

Module Federation is a feature that first came with webpack 5. It lets one JavaScript application load code from another application at runtime, as if it were a normal import. Each app can say which modules it exposes and which libraries it wants to share.

In Angular, it is mostly used through the `@angular-architects/module-federation` package for projects that use webpack.

## 10: What is Native Federation?

Native Federation is a library from Angular Architects (`@angular-architects/native-federation`) that gives you the Module Federation idea without webpack. It works with Angular's esbuild-based application builder and uses browser standards like ES modules and import maps.

It is the usual choice for new Angular micro frontend projects because the Angular CLI uses esbuild by default since Angular 17.

## 11: Why can't you use webpack Module Federation with the default Angular builder?

Module Federation is a webpack plugin. Since Angular 17 new projects use the esbuild-based `application` builder, which doesn't run webpack at all, so there is nowhere to plug the webpack plugin in.

You have two choices: switch the project back to a webpack-based builder (with `ngx-build-plus` or a custom webpack builder), or use Native Federation, which was made for the esbuild builder.

## 12: Which package do you install to use Native Federation in Angular?

```bash
npm i @angular-architects/native-federation -D
```

The package version follows Angular's version, so for Angular 21 you install a 21.x version. After installing, you run its `init` schematic for each project that should be a host or a remote.

## 13: How do you turn an Angular app into a Native Federation remote?

Run the `init` schematic with the type `remote`:

```bash
ng g @angular-architects/native-federation:init --project mfe1 --port 4201 --type remote
```

It creates a `federation.config.mjs` (or `federation.config.js` in older versions), changes the build target in `angular.json` to the Native Federation builder, and moves the bootstrap code so that federation is set up before Angular starts.

## 14: How do you turn an Angular app into a Native Federation host?

Run the same schematic with the type `dynamic-host` (or `host`):

```bash
ng g @angular-architects/native-federation:init --project shell --port 4200 --type dynamic-host
```

A `dynamic-host` reads the list of remotes from a JSON manifest at runtime. That is the setup most teams use because the remote URLs can change per environment without a rebuild.

## 15: What is the federation.config file?

It is the config file Native Federation reads at build time. It says what the app is called, which files it exposes (for remotes) and which npm packages are shared.

```js
import {
  withNativeFederation,
  shareAll,
} from "@angular-architects/native-federation/config";

export default withNativeFederation({
  name: "mfe1",
  exposes: {
    "./Component": "./projects/mfe1/src/app/app.component.ts",
  },
  shared: {
    ...shareAll({
      singleton: true,
      strictVersion: true,
      requiredVersion: "auto",
    }),
  },
});
```

## 16: What does the "exposes" option do?

`exposes` is a map of public names to files in the remote. Only these files can be loaded by the host. The key is the name the host uses, and the value is the path in the remote project.

```js
exposes: {
  './routes': './projects/mfe1/src/app/app.routes.ts',
  './Component': './projects/mfe1/src/app/app.component.ts',
},
```

Think of it as the remote's public API. Everything else stays internal.

## 17: What does the "shared" option do?

`shared` lists npm packages that the host and remotes should share at runtime instead of each loading its own copy. For Angular, you nearly always share `@angular/core`, `@angular/common`, `@angular/router` and `rxjs`.

Sharing keeps the bundle size down and, more importantly, makes sure there is only one Angular instance running in the page.

## 18: What does shareAll do?

`shareAll` is a helper that marks every package in your `package.json` `dependencies` as shared, with the same options for all of them.

```js
shared: {
  ...shareAll({ singleton: true, strictVersion: true, requiredVersion: 'auto' }),
},
```

It saves you from listing every package by hand. You can still use `skip` to leave some packages out.

## 19: What is the federation manifest?

The manifest is a JSON file the host reads at startup. It maps each remote name to the URL of its metadata file:

```json
{
  "mfe1": "http://localhost:4201/remoteEntry.json",
  "mfe2": "http://localhost:4202/remoteEntry.json"
}
```

By default it lives at `src/assets/federation.manifest.json` (or `public/` in newer projects). Since it is just a file, you can have a different one per environment or even get it from an API.

## 20: What is remoteEntry.json?

`remoteEntry.json` is a file that Native Federation generates when it builds a remote. It describes what the remote exposes, which shared packages it needs and where the built files are.

The host downloads this file first, then uses it to build an import map and load the right files. In webpack Module Federation the matching file is `remoteEntry.js`, which is JavaScript instead of JSON.

## 21: What does initFederation do?

`initFederation` sets up federation in the browser before Angular starts. In the host you pass it the manifest; in a remote you call it with no arguments.

```ts
// host: main.ts
import { initFederation } from "@angular-architects/native-federation";

initFederation("/assets/federation.manifest.json")
  .catch((err) => console.error(err))
  .then(() => import("./bootstrap"))
  .catch((err) => console.error(err));
```

It reads the remote metadata, builds an import map for the shared packages, and only then the app is bootstrapped.

## 22: Why is the bootstrap code moved into a separate bootstrap.ts file?

Because shared packages like `@angular/core` must not be loaded before federation knows which version to use. If `main.ts` imported Angular directly, the browser would load it right away.

So `main.ts` first calls `initFederation()` and then does a dynamic `import('./bootstrap')`. The `bootstrap.ts` file holds the normal `bootstrapApplication(...)` call. The schematic makes this change for you.

## 23: What does loadRemoteModule do?

`loadRemoteModule` loads an exposed file from a remote at runtime and returns a promise with its exports.

```ts
import { loadRemoteModule } from "@angular-architects/native-federation";

const m = await loadRemoteModule("mfe1", "./Component");
// m.AppComponent is now available
```

You usually call it inside a lazy route, but you can call it from anywhere, for example to load a widget on button click.

## 24: How do you load a remote component in an Angular route?

Use `loadComponent` with `loadRemoteModule`:

```ts
import { Routes } from "@angular/router";
import { loadRemoteModule } from "@angular-architects/native-federation";

export const routes: Routes = [
  {
    path: "flights",
    loadComponent: () =>
      loadRemoteModule("mfe1", "./Component").then((m) => m.AppComponent),
  },
];
```

The remote is only downloaded the first time the user goes to `/flights`.

## 25: How do you load a whole set of remote routes?

Expose the remote's routes file and use `loadChildren`:

```ts
// remote federation.config
exposes: {
  './routes': './projects/mfe1/src/app/app.routes.ts',
},

// shell routes
{
  path: 'flights',
  loadChildren: () =>
    loadRemoteModule('mfe1', './routes').then(m => m.routes),
},
```

This way the remote team controls its own sub-routes, and the shell only owns the `flights` prefix.

## 26: What is the difference between a static and a dynamic host?

A static host has the remote URLs written into its build config, so changing a URL means rebuilding the shell.

A dynamic host reads the remote URLs at runtime, usually from a manifest JSON file. You can point the same shell build to different remotes in dev, test and production. Most real projects use a dynamic host.

## 27: Can a micro frontend run on its own?

Yes, and it should. A remote is still a normal Angular app with its own `main.ts` and `index.html`. You can start it with `ng serve mfe1` and open it on its own port.

This is handy for development: the team can work on its feature without starting the shell and all other remotes.

## 28: How do you run a host and a remote locally?

Start each project in its own terminal, each on its own port:

```bash
ng serve mfe1    # http://localhost:4201
ng serve shell   # http://localhost:4200
```

The shell's manifest points to `http://localhost:4201/remoteEntry.json`. Some setups add an npm script that runs all of them at once with a tool like `concurrently` or `npm-run-all`, or use Nx to run them together.

## 29: Why does every micro frontend need its own port in development?

Each `ng serve` starts its own dev server, and two servers can't listen on the same port. The `--port` option you pass to the `init` schematic is written to `angular.json` so each app always starts on the same port.

In production the remotes are usually served from different URLs or paths, not ports.

## 30: What is a vertical split?

A vertical split means each micro frontend owns a whole page or a whole section of the app, for example everything under `/orders` belongs to the orders team. Only one micro frontend is on screen at a time, apart from the shell.

It is the easiest split to manage because the teams rarely affect each other on the same screen.

## 31: What is a horizontal split?

A horizontal split means several micro frontends are shown on the same page at the same time, for example a header from one team, a product list from another and a recommendations box from a third.

It gives more flexibility but is harder: the pieces must agree on styles, must not slow each other down and need a way to talk to each other.

## 32: How should you decide where to split an app into micro frontends?

Split along business areas (domains), not technical layers. Good boundaries are things like "search", "checkout", "account" or "admin", where one team can own the whole flow.

Bad splits are "all forms", "all tables" or "the header". If a single user story always needs changes in three micro frontends, the boundary is probably in the wrong place.

## 33: What is a bounded context and why does it matter here?

A bounded context is a term from Domain-Driven Design. It is a part of the business with its own words, rules and data, for example "billing" or "shipping".

Bounded contexts are a good starting point for micro frontend boundaries because they already have little overlap with each other. One team, one bounded context, one micro frontend is a common setup.

## 34: What are the main downsides of micro frontends?

- More moving parts: more repos or projects, more pipelines, more deployments.
- Version problems with shared libraries like Angular.
- Harder to keep the UI and UX consistent.
- Harder to debug, since a bug can sit between two apps.
- Possible extra bundle size if libraries are not shared well.
- More work to set up local development.

You should only pay this cost when you have the team and app size that justify it.

## 35: When should you NOT use micro frontends?

Don't use them when:

- One or two teams work on the app.
- The app is small or medium size.
- All features are released together anyway.
- You don't have people to own the build and deployment setup.

In those cases a well-structured monolith with lazy-loaded features and clear folder boundaries is simpler and faster.

## 36: What is the difference between runtime and build-time integration?

With build-time integration, each micro frontend is published as an npm package and the shell installs it. Everything is bundled together, so any change needs the shell to update and redeploy.

With runtime integration, the shell loads the micro frontends from their own URLs while the app is running. Each team can deploy on its own. Module Federation, Native Federation and web components loaded from a URL are all runtime integration.

## 37: What is Angular Elements?

Angular Elements is the `@angular/elements` package. It turns an Angular component into a custom element (a web component) that you can use in any HTML page, like `<my-widget></my-widget>`.

It is used for micro frontends when the host is not Angular or when you want to mix different Angular versions.

## 38: How do you create a custom element from an Angular component?

Use `createApplication` and `createCustomElement`:

```ts
import { createApplication } from "@angular/platform-browser";
import { createCustomElement } from "@angular/elements";
import { CartWidgetComponent } from "./cart-widget.component";

(async () => {
  const app = await createApplication({ providers: [] });
  const element = createCustomElement(CartWidgetComponent, {
    injector: app.injector,
  });
  customElements.define("cart-widget", element);
})();
```

After this runs, any page that loads the script can use `<cart-widget></cart-widget>`.

## 39: What is a web component?

A web component is a custom HTML element built with browser standards: Custom Elements, Shadow DOM and HTML templates. It works in any framework or with no framework, because the browser itself knows how to create it.

That's why web components are often used as the "common language" between micro frontends built with different frameworks.

## 40: What is single-spa?

single-spa is a JavaScript framework for micro frontends. It registers several apps and decides which ones to mount or unmount based on the current URL. Each app can use a different framework.

For Angular there is the `single-spa-angular` helper. It was popular before Module Federation; today many new Angular projects use Native Federation instead, but you will still see single-spa in existing code bases.

## 41: What is the iframe approach to micro frontends?

You load each micro frontend inside an `<iframe>`. Each one runs in a fully separate browser context, so styles, JavaScript and even Angular versions can't clash.

The downsides are big: no shared routing, hard to resize, poor accessibility and SEO, communication only through `postMessage`, and every iframe loads its own copy of every library. It is mostly used for legacy apps or third-party content.

## 42: What is a singleton shared dependency?

A singleton shared dependency is a library that must only be loaded once in the page, no matter how many micro frontends use it. You mark it with `singleton: true`.

Angular itself must be a singleton. Two copies of `@angular/core` means two separate injectors, two zones and services that are not really shared, which leads to strange bugs.

## 43: What does strictVersion do?

With `strictVersion: true`, if the version a remote needs doesn't match the version that is already loaded, you get an error instead of a silent fallback.

It helps you find version problems early, at the moment the remote loads, instead of hunting for random bugs later in production.

## 44: What does requiredVersion: 'auto' mean?

It tells Native Federation (or the Angular Architects Module Federation plugin) to read the version range for each shared package from your `package.json` instead of you writing it by hand.

For example, if `package.json` says `"@angular/core": "^21.0.0"`, then `^21.0.0` becomes the required version for that shared package.

## 45: Why do micro frontends need to agree on the Angular version?

When Angular is shared as a singleton, only one version can be loaded. If the shell uses Angular 21 and a remote was built with Angular 19, the remote runs on the shell's Angular, which can break, or the load fails because of `strictVersion`.

The usual rule is: all micro frontends use the same major Angular version and upgrade together. If that is not possible, you need stronger isolation like web components with separate bundles.

## 46: What is an import map?

An import map is a browser feature that tells the browser where to find a module when the code does `import 'some-name'`.

```html
<script type="importmap">
  {
    "imports": {
      "@angular/core": "/shared/angular-core.js"
    }
  }
</script>
```

Native Federation builds an import map at runtime from the remotes' metadata, so all apps use the same copy of each shared package.

## 47: What is an ES module?

An ES module is the standard JavaScript module format with `import` and `export`. Browsers can load ES modules directly with `<script type="module">` or with a dynamic `import()`.

Native Federation outputs ES modules, which is why it doesn't need a special runtime like webpack's. The browser does the loading.

## 48: What is lazy loading and how does it relate to micro frontends?

Lazy loading means code is downloaded only when it is needed, for example when the user opens a route. In a normal Angular app you lazy load with `loadComponent` and `loadChildren`.

Micro frontends use the same routes API, but the lazy code comes from another app on another server instead of from the same build. So for the router, a remote is just another lazy-loaded route.

## 49: What is the "remote" name used for?

The remote name, like `mfe1`, is the key used to find a remote. It is set with `name` in the remote's federation config and used in the host's manifest and in `loadRemoteModule('mfe1', ...)`.

The names must be unique across the whole system. If two remotes use the same name, one will overwrite the other.

## 50: What is an exposed module name like './Component'?

It is the public key a remote gives to one of its files in `exposes`. The host uses this key, not the real file path, to load the file.

```ts
loadRemoteModule("mfe1", "./Component");
```

The leading `./` is just a convention from Module Federation. Keeping these names stable is important because changing them breaks the host.

## 51: What is the @angular-architects/module-federation package?

It is a package from Angular Architects that adds webpack Module Federation to Angular CLI projects. It gives you schematics to set up hosts and remotes, a `webpack.config.js` with helper functions like `withModuleFederationPlugin` and `shareAll`, and a `loadRemoteModule` function.

You use it in projects that still build with webpack. For new esbuild-based projects, Native Federation from the same authors is the usual pick.

## 52: How do you set up a webpack Module Federation remote in Angular?

```bash
ng add @angular-architects/module-federation --project mfe1 --port 4201 --type remote
```

This adds a `webpack.config.js`, switches the builder to one that can use a custom webpack config, and creates the `bootstrap.ts` split. Then you list what to expose in `webpack.config.js`.

## 53: What does a webpack.config.js for an Angular remote look like?

```js
const {
  shareAll,
  withModuleFederationPlugin,
} = require("@angular-architects/module-federation/webpack");

module.exports = withModuleFederationPlugin({
  name: "mfe1",
  exposes: {
    "./Component": "./projects/mfe1/src/app/app.component.ts",
  },
  shared: {
    ...shareAll({
      singleton: true,
      strictVersion: true,
      requiredVersion: "auto",
    }),
  },
});
```

It looks almost the same as the Native Federation config, which makes moving from one to the other easier.

## 54: How do you load a remote with webpack Module Federation in Angular?

With the `@angular-architects/module-federation` version of `loadRemoteModule`:

```ts
import { loadRemoteModule } from '@angular-architects/module-federation';

{
  path: 'flights',
  loadComponent: () =>
    loadRemoteModule({
      type: 'module',
      remoteEntry: 'http://localhost:4201/remoteEntry.js',
      exposedModule: './Component',
    }).then(m => m.AppComponent),
}
```

`type: 'module'` is used because Angular builds output ES modules.

## 55: What is remoteEntry.js?

`remoteEntry.js` is the small JavaScript file webpack Module Federation creates for each remote. The host loads it first. It contains a "container" that knows what the remote exposes and how to get its chunks.

It should never be cached for long, because it is the file that points to the current version of the remote.

## 56: What is the difference between the shell and a remote in terms of who owns what?

The shell team usually owns:

- The page layout and navigation
- Login and the user session
- Top-level routes
- Loading and error handling for remotes

The remote teams own their features end to end: their pages, sub-routes, components, API calls and tests. The shell should not know about the remote's internals, only the exposed entry points.

## 57: What happens if a remote is down?

If the shell tries to load a remote that is not reachable, the `loadRemoteModule` promise rejects. If you don't handle it, the route fails to load and the user may see a blank area or a router error.

That's why you should catch the error and show a fallback, like "This section is not available right now", and keep the rest of the app working.

## 58: How do you show a fallback when a remote fails to load?

Catch the error inside the route loader and return a fallback component:

```ts
{
  path: 'flights',
  loadComponent: () =>
    loadRemoteModule('mfe1', './Component')
      .then(m => m.AppComponent)
      .catch(() => import('./remote-error.component').then(m => m.RemoteErrorComponent)),
}
```

This way one broken team doesn't take down the whole application.

## 59: Can micro frontends use different frameworks?

Yes, but it costs more. A shell can load a React micro frontend and an Angular one if they are wrapped as web components or mounted through something like single-spa.

The cost is more bundle size (each framework is loaded), different styling, more complex communication and harder hiring and support. Most teams mix frameworks only during a migration, not as a long-term plan.

## 60: What is a monorepo?

A monorepo is one Git repository that holds several projects, for example the shell and all remotes. Tools like Nx or the Angular CLI workspace (`projects/` folder) help manage it.

Monorepos make it easy to share code and keep versions aligned, but you have to be careful that teams can still deploy separately.

## 61: What is a polyrepo?

A polyrepo setup means each micro frontend lives in its own Git repository with its own pipeline. Teams are more independent, but sharing code, keeping the same Angular version and making changes across apps is harder.

Many companies start with a monorepo for micro frontends and only split repos when team boundaries really need it.

## 62: How do you create several Angular projects in one workspace?

Create an empty workspace and add applications:

```bash
ng new my-workspace --no-create-application
cd my-workspace
ng generate application shell
ng generate application mfe1
ng generate application mfe2
```

Each app goes into `projects/<name>` and has its own entry in `angular.json`. Then you run the federation schematic for each one.

## 63: What is Nx and why is it used with micro frontends?

Nx is a build system and monorepo tool. It understands which projects depend on which, so it can build and test only what changed. It has generators for Angular hosts and remotes and can start the shell with all remotes at once.

It's popular for micro frontends because the hard part of micro frontends is managing many projects, and that's what Nx is made for.

## 64: How do you generate a host with remotes using Nx?

Nx has generators for this:

```bash
nx g @nx/angular:host apps/shell --remotes=mfe1,mfe2
nx g @nx/angular:remote apps/mfe3 --host=shell
```

They create the apps, the Module Federation config and the routes in the shell. Check the Nx docs for your version, because Nx has been changing how it wraps Module Federation.

## 65: What is a design system and why is it important for micro frontends?

A design system is a shared set of UI components, colors, spacing, fonts and rules. In micro frontends, each team builds its own UI, so without a design system the app quickly looks like five different products.

It is usually published as a shared library (for example an npm package) that every micro frontend uses.

## 66: What is the problem with global CSS in micro frontends?

Global CSS from one micro frontend can change the look of another. For example, if a remote adds `button { color: red; }` to its global styles, every button on the page turns red once that remote loads.

Teams should avoid global selectors in remotes, keep styles in component styles, and leave global styles to the shell or the design system.

## 67: How does Angular's view encapsulation help with micro frontends?

By default Angular uses `ViewEncapsulation.Emulated`, which adds unique attributes to a component's elements and rewrites its CSS selectors to match only those. So a component's styles don't leak out to other components.

This helps a lot, because most styles stay inside their own micro frontend. It doesn't protect against global stylesheets, though.

## 68: What is Shadow DOM?

Shadow DOM is a browser feature that gives an element its own hidden DOM tree with its own styles. Styles outside don't get in (except inherited ones like font and color) and styles inside don't get out.

In Angular you can use it with `encapsulation: ViewEncapsulation.ShadowDom`. It gives strong style isolation for micro frontends, especially web components.

## 69: How do micro frontends talk to each other?

Common options:

- URL and route parameters
- Custom browser events (`CustomEvent` on `window`)
- A small shared service or store loaded as a shared library
- Inputs and outputs on a web component
- `BroadcastChannel` for messages between tabs
- Shared storage like `localStorage` (only for simple cases)

The rule of thumb is to keep communication small and loose, so teams don't depend too much on each other.

## 70: Why should communication between micro frontends be kept small?

Every message or shared object is a contract between two teams. The more contracts, the more often a change in one micro frontend breaks another, and the more teams need to coordinate.

If two micro frontends talk a lot, it's often a sign they belong together in one micro frontend.

## 71: How do you send a message between micro frontends with a custom event?

Dispatch a `CustomEvent` on `window` and listen for it in the other app:

```ts
// in the cart micro frontend
window.dispatchEvent(new CustomEvent("cart:updated", { detail: { count: 3 } }));

// in the shell
window.addEventListener("cart:updated", (e: Event) => {
  const { count } = (e as CustomEvent<{ count: number }>).detail;
  console.log("items in cart", count);
});
```

It doesn't need any shared library, so it works between any frameworks.

## 72: What is the URL's role in micro frontend communication?

The URL is the simplest and most stable way to share state, like the selected product id or a search term. The shell and remotes can all read it, it survives a page refresh, and users can bookmark and share it.

Before adding a shared store, check whether the data can just live in the URL.

## 73: Can micro frontends share an Angular service?

Yes. If the service lives in a shared library that is marked as shared in the federation config, and it is `providedIn: 'root'`, then all micro frontends get the same instance because they share the same root injector.

```ts
@Injectable({ providedIn: "root" })
export class AuthService {
  readonly user = signal<User | null>(null);
}
```

This only works if the library is really shared (one copy). If each remote bundles its own copy, each gets its own instance.

## 74: What is a shared library in a micro frontend setup?

It is code that several micro frontends use, like a design system, an auth helper or common models. In a monorepo it is usually a library project (for example under `projects/` or `libs/`) mapped with a path in `tsconfig.json`.

You can share it at runtime through the federation config, so it's loaded once, or just bundle it into each app if it is small and doesn't hold state.

## 75: How do you share a local monorepo library with Native Federation?

Native Federation reads the path mappings from `tsconfig.json` and can share them like npm packages. You can control them with `sharedMappings`:

```js
export default withNativeFederation({
  name: "shell",
  shared: {
    ...shareAll({
      singleton: true,
      strictVersion: true,
      requiredVersion: "auto",
    }),
  },
  sharedMappings: ["@my-org/auth"],
});
```

If you don't list `sharedMappings`, all mapped paths are shared by default.

## 76: What is the "skip" option in the federation config?

`skip` lists packages or entry points that should not be shared, even if `shareAll` would include them. For example:

```js
skip: ['rxjs/ajax', 'rxjs/fetch', 'rxjs/testing', 'rxjs/webSocket'],
```

This avoids extra work at build time and extra files at runtime for things you don't use.

## 77: What happens if a library is not shared?

Each micro frontend bundles its own copy. This is fine for small, stateless helpers. For big libraries it adds to the download size. For stateful libraries, like Angular, a store or an auth client, it causes bugs because each app has its own separate instance.

## 78: How does routing work in a micro frontend shell?

The shell has the top-level routes. Each micro frontend gets a path prefix and the shell lazy loads its component or routes there:

```ts
export const routes: Routes = [
  { path: "", component: HomeComponent },
  {
    path: "orders",
    loadChildren: () =>
      loadRemoteModule("orders", "./routes").then((m) => m.routes),
  },
  {
    path: "account",
    loadChildren: () =>
      loadRemoteModule("account", "./routes").then((m) => m.routes),
  },
];
```

Inside the remote's routes, paths are relative to that prefix.

## 79: Should a remote have its own router?

When loaded through `loadChildren` in an Angular shell, the remote doesn't create a second router. Its routes are added as child routes to the shell's router. That's the normal setup and it keeps navigation simple.

When a remote is loaded as a web component, it is a separate Angular app and has its own router, so you need to keep the two routers in sync with the URL.

## 80: What is a "page-level" micro frontend?

It's a micro frontend that takes a whole route, like `/orders/**`. The shell gives it the main content area and it decides what to show inside. This is the vertical split and it's the most common setup with Angular federation.

## 81: What is a "widget" or "fragment" micro frontend?

It's a small piece of UI, like a mini cart, a notification bell or a recommendation box, that is placed inside a page owned by someone else. The host page loads it like a component.

Widgets need more care: they must be small, fast, and not break the page around them.

## 82: How do you load a remote component without the router?

Load it with `loadRemoteModule` and render it with `NgComponentOutlet` or `ViewContainerRef`:

```ts
@Component({
  selector: "app-mini-cart-slot",
  imports: [NgComponentOutlet],
  template: `
    @if (cmp(); as c) {
      <ng-container *ngComponentOutlet="c" />
    }
  `,
})
export class MiniCartSlotComponent {
  cmp = signal<Type<unknown> | null>(null);

  constructor() {
    loadRemoteModule("cart", "./MiniCart").then((m) =>
      this.cmp.set(m.MiniCartComponent),
    );
  }
}
```

## 83: What is the difference between loadComponent and loadChildren for remotes?

`loadComponent` loads one standalone component for a single route. Use it when the remote is just one page.

`loadChildren` loads a `Routes` array, so the remote can have many pages and its own guards and resolvers. Use it when the remote is a whole feature area. Most real remotes expose routes.

## 84: Do remotes need to be standalone components?

No, but it's much easier. With standalone components you expose a component or a routes array directly. With NgModules you have to expose a module and use `loadChildren` with that module.

Modern Angular apps are standalone by default, and most new micro frontend examples assume standalone.

## 85: How do you expose an NgModule from a remote (legacy)?

```js
exposes: {
  './Module': './projects/mfe1/src/app/flights/flights.module.ts',
},
```

```ts
{
  path: 'flights',
  loadChildren: () =>
    loadRemoteModule('mfe1', './Module').then(m => m.FlightsModule),
}
```

You will still see this in older projects. New code should expose standalone routes.

## 86: Where does the shell's layout live and where do remotes render?

The shell's `AppComponent` holds the layout with a `<router-outlet>`. Remotes loaded through routes render inside that outlet:

```html
<app-header />
<app-sidebar />
<main>
  <router-outlet />
</main>
```

So the header and menu stay on screen while the content area switches between micro frontends.

## 87: What is the role of the CDN in micro frontends?

Each micro frontend's built files are usually uploaded to a CDN or static file host. The shell loads them from there. A CDN serves files from servers close to the user, which makes loading faster.

You must set the caching headers right: hashed files can be cached for a long time, but `remoteEntry.json` and the manifest should not be cached for long.

## 88: Why shouldn't remoteEntry.json be cached for a long time?

Because it is the file that tells the host which version of the remote to use. If the browser or CDN caches an old copy, users keep getting the old remote even after the team deploys a new one.

Set something like `Cache-Control: no-cache` for it, while the hashed JS chunks can use a long cache.

## 89: What is CORS and why does it matter for micro frontends?

CORS (Cross-Origin Resource Sharing) is the browser rule that blocks loading some resources from another origin unless the server allows it. If the shell is on `app.example.com` and a remote is on `cart.example.com`, loading ES modules from the remote needs CORS headers.

The remote's server must send `Access-Control-Allow-Origin` for the shell's origin. Otherwise the browser refuses to load the module.

## 90: Do micro frontends need to be on the same domain?

No, but it's simpler if they are. A common setup is to serve everything under one domain with a reverse proxy or CDN paths, like `example.com/` for the shell and `example.com/mfe/cart/` for the cart.

Same domain means no CORS issues, cookies work the same everywhere and there's one place to set security headers.

## 91: What is a reverse proxy in this context?

A reverse proxy (like Nginx, a load balancer or a CDN routing rule) receives all requests on one domain and forwards them to the right server based on the path. For example `/mfe/cart/*` goes to the cart team's bucket and everything else goes to the shell.

For the browser it all looks like one site, but each team still deploys its own files.

## 92: How do you configure environment-specific remote URLs?

With a dynamic host, keep a manifest per environment and pick the right one at deploy time or at startup:

```ts
const manifest =
  location.hostname === "localhost"
    ? "/assets/federation.manifest.json"
    : "/assets/federation.manifest.prod.json";

initFederation(manifest).then(() => import("./bootstrap"));
```

Many teams instead write the manifest during deployment, or serve it from a small config API, so the same build works everywhere.

## 93: Can you pass an object instead of a URL to initFederation?

Yes. Instead of the manifest path you can pass an object with the remote names and URLs:

```ts
initFederation({
  mfe1: "http://localhost:4201/remoteEntry.json",
}).then(() => import("./bootstrap"));
```

This is useful when you already got the list from an API.

## 94: What is a contract between micro frontends?

A contract is what one micro frontend promises to others: the exposed module names, the exported component or routes, its inputs, the events it sends and the data shapes. As long as the contract stays the same, a team can change everything else.

Breaking a contract without telling others is the most common reason micro frontend setups break in production.

## 95: How do you keep contracts typed between micro frontends?

Put the shared types (event payloads, input shapes, route params) in a small shared library, for example `@my-org/contracts`. Both sides import the types from there.

```ts
export interface CartUpdatedEvent {
  count: number;
  total: number;
}
```

Types are removed at build time, so this adds nothing to the bundle, but it gives you compile errors when one side changes the shape.

## 96: Can you use TypeScript types for a remote that is loaded at runtime?

`loadRemoteModule` gives you an untyped result because TypeScript can't see the remote's code at build time. You can add the type yourself with a shared interface:

```ts
import { Routes } from "@angular/router";

interface FlightsRemote {
  routes: Routes;
}

const m = (await loadRemoteModule("mfe1", "./routes")) as FlightsRemote;
```

Keep these interfaces in a shared contracts library so both teams use the same one. Some tools (like Module Federation 2.0) can generate types for remotes automatically.

## 97: What is a "standalone mode" for a remote?

It's when you run the remote directly in the browser without the shell, for example at `localhost:4201`. The remote's own `AppComponent`, routes and `index.html` are used.

It's handy for development and demos. The remote should not depend on the shell to work in this mode, or at least should provide simple stubs for things the shell normally gives (like the logged-in user).

## 98: What is the difference between the remote's AppComponent and its exposed component?

The remote's `AppComponent` is what you see when you run the remote on its own. It often has a simple test layout.

The exposed component or routes are what the shell loads. Often you expose a feature component or routes file, not `AppComponent`, so the shell doesn't get the remote's own test layout.

## 99: How do you build a micro frontend for production?

The same way as a normal Angular app:

```bash
ng build mfe1
ng build shell
```

The Native Federation builder runs the normal Angular build and also writes `remoteEntry.json` and the shared package files. Each output folder (for example `dist/mfe1/browser`) is deployed to its own place.

## 100: Do you need to rebuild the shell when a remote changes?

No, not if you use runtime integration correctly. The shell only knows the remote's URL and its exposed names. When the remote team deploys a new version to the same URL, the shell picks it up on the next page load.

You only need to change the shell when the contract changes, for example a new exposed name or a new route prefix.

## 101: What is the difference between Module Federation and Native Federation in simple words?

Both let a host load code from remotes at runtime and share libraries. The difference is how:

- Module Federation is a webpack (and Rspack) feature with its own runtime that loads chunks.
- Native Federation is a separate library that works with any build tool, and in Angular it plugs into the esbuild builder. It uses browser standards (ES modules and import maps) to load code.

The config and the `loadRemoteModule` call look very similar in both.

## 102: Is Native Federation part of the official Angular framework?

No. It's an open source community project by Angular Architects, not a package from the Angular team. The Angular team builds the esbuild builder that Native Federation plugs into, but Native Federation itself is maintained separately.

That's worth knowing because its release cycle and support are separate from Angular's.

## 103: How do you check that federation is set up correctly in a remote?

Build or serve the remote and open `http://localhost:4201/remoteEntry.json` in the browser. You should see JSON with the remote's name, the exposed modules and the shared packages.

If the file is missing or empty, the build target is probably not the Native Federation builder, or the federation config has an error.

## 104: What changes does the Native Federation schematic make in angular.json?

It changes the `build` and `serve` targets to use the `@angular-architects/native-federation:build` builder. The original Angular builder is kept in a separate target (often called `esbuild`) that the Native Federation builder calls internally.

```json
"build": {
  "builder": "@angular-architects/native-federation:build",
  "options": {},
  "configurations": {
    "production": { "target": "mfe1:esbuild:production" },
    "development": { "target": "mfe1:esbuild:development", "dev": true }
  }
}
```

## 105: What is the bootstrap.ts file in a Native Federation app?

It's the file that starts Angular. It contains what `main.ts` used to have:

```ts
import { bootstrapApplication } from "@angular/platform-browser";
import { appConfig } from "./app/app.config";
import { AppComponent } from "./app/app.component";

bootstrapApplication(AppComponent, appConfig).catch((err) =>
  console.error(err),
);
```

`main.ts` only sets up federation and then imports this file dynamically.

## 106: What does a remote's main.ts look like with Native Federation?

```ts
import { initFederation } from "@angular-architects/native-federation";

initFederation()
  .catch((err) => console.error(err))
  .then(() => import("./bootstrap"))
  .catch((err) => console.error(err));
```

The remote calls `initFederation()` with no arguments because it doesn't load other remotes. It still needs it so shared packages are set up the same way when it runs on its own.

## 107: What is a micro frontend "team topology"?

It describes how teams are organized around micro frontends. The common setup is one cross-functional team per micro frontend, with front-end and often back-end developers, owning a business area end to end.

There's also usually a platform team that owns the shell, the design system and the shared tooling.

## 108: What is a platform team?

A platform team builds the things every feature team needs: the shell, the build and deployment pipelines, the design system, shared libraries and documentation. Its job is to make it easy for feature teams to ship their micro frontends.

Without a platform team, every feature team ends up solving the same setup problems differently.

## 109: What is "Conway's Law" and how does it relate to micro frontends?

Conway's Law says that the structure of a system tends to copy the structure of the organization that builds it. Micro frontends use this on purpose: you shape the app's boundaries to match team boundaries, so teams can work alone.

If the teams don't match the micro frontends, you get constant cross-team work.

## 110: Can one team own more than one micro frontend?

Yes, that's normal. A team might own "search" and "product details" because they're related. What you want to avoid is the opposite: one micro frontend owned by several teams, since then nobody really owns it.

## 111: What is a "remote entry point"?

It's the first file the host fetches from a remote to learn about it. In Native Federation it's `remoteEntry.json`; in webpack Module Federation it's `remoteEntry.js`; in Module Federation 2.0 it can also be `mf-manifest.json`.

The host only needs this one URL per remote. Everything else is found from there.

## 112: How do you add a new remote to an existing dynamic host?

1. Create the new Angular app and run the Native Federation `init` schematic with `--type remote`.
2. Expose its component or routes in its federation config.
3. Add its name and URL to the shell's manifest.
4. Add a route in the shell that calls `loadRemoteModule('newRemote', './routes')`.

Only steps 3 and 4 touch the shell. If routes are also driven by config, step 4 can go away too.

## 113: What does it mean to "expose routes" from a remote?

It means the remote makes its `Routes` array available to the host:

```ts
// projects/mfe1/src/app/app.routes.ts
export const routes: Routes = [
  { path: "", component: FlightSearchComponent },
  { path: ":id", component: FlightDetailsComponent },
];
```

```js
exposes: { './routes': './projects/mfe1/src/app/app.routes.ts' },
```

The shell mounts these routes under a prefix with `loadChildren`, and the remote team can add new pages without touching the shell.

## 114: What does "standalone" mean in Angular and why does it help micro frontends?

Standalone components, directives and pipes declare their own dependencies with `imports` instead of belonging to an NgModule. They're the default since Angular 19.

For micro frontends, this means you can expose and load a single component or a routes file without wrapping it in a module. It makes the exposed pieces smaller and the setup simpler.

## 115: What is the role of providers in an exposed routes file?

A route can have its own `providers`, which creates a new injector for that route and its children. A remote can use this to provide its own services without touching the shell's `app.config.ts`:

```ts
export const routes: Routes = [
  {
    path: "",
    providers: [FlightService, provideHttpClient()],
    children: [{ path: "", component: FlightSearchComponent }],
  },
];
```

This keeps the remote self-contained.

## 116: Why shouldn't a remote rely on the shell's app.config providers?

Because the remote is a separate app and may also run standalone or inside a different shell. If it silently depends on something the shell provides, it breaks when that changes.

Each remote should declare what it needs on its own routes, and the shell should only provide truly global things, like the router, HTTP client and auth.

## 117: What is a "shared state" problem in micro frontends?

It's when several micro frontends need the same data, like the logged-in user, the cart count or the selected language. If each one fetches and stores it separately, they get out of sync.

The fix is to choose one owner for each piece of data and share it through a shared service, events or the URL.

## 118: How do you share the logged-in user between micro frontends?

The usual way is a shared auth service in a shared library, provided in root. The shell logs the user in and sets the user; remotes read it:

```ts
@Injectable({ providedIn: "root" })
export class AuthStore {
  private readonly _user = signal<User | null>(null);
  readonly user = this._user.asReadonly();

  setUser(user: User | null) {
    this._user.set(user);
  }
}
```

The library must be shared as a singleton so everyone gets the same instance.

## 119: How do micro frontends handle authentication tokens?

Usually the shell handles login (for example with OIDC) and either:

- stores the token in memory in a shared auth service, or
- relies on an HTTP-only cookie set by the back-end, so the browser sends it automatically.

Remotes don't log in on their own. They use the shared service or the cookie when calling APIs. An HTTP interceptor in the shell or in a shared library can add the token to every request.

## 120: Should each micro frontend have its own HTTP interceptors?

Global interceptors like auth and error handling should live in one place, usually the shell or a shared library, so all requests behave the same.

A remote can add its own interceptors on its own routes with `provideHttpClient(withInterceptors([...]))` in route providers, but then it has its own `HttpClient` for that part of the app. Be careful that it doesn't lose the global auth interceptor by accident.

## 121: How do micro frontends share translations (i18n)?

There are two common ways:

- Each micro frontend has its own translation files and loads them itself. The shell only tells everyone which language is active.
- A shared translation library (like Transloco or ngx-translate) is shared as a singleton, and each remote adds its own translation scope.

Either way, the selected language should come from one place (the shell, the URL or a shared service).

## 122: Does Native Federation work with Angular's built-in i18n (@angular/localize)?

Yes, Native Federation supports Angular i18n since version 19.0.13, and it has a `shareAngularLocales` helper for sharing Angular locale data:

```js
shared: {
  ...shareAll({ singleton: true, strictVersion: true, requiredVersion: 'auto' }),
  ...shareAngularLocales(['en', 'de', 'fr']),
},
```

With built-in i18n there's one build per language, so the manifest has to point to the remote build for the right language.

## 123: What is a "micro frontend registry"?

It's a service or config file that lists which micro frontends exist, where they live, and sometimes extra data like their route, menu label or required permissions. The shell reads it at startup.

The federation manifest is the simplest form. Bigger setups use a small API so they can change the list without redeploying anything.

## 124: How can a shell build its menu from the remote list?

Extend the config with menu data and build routes and menu items from it:

```ts
interface RemoteConfig {
  name: string;
  path: string;
  label: string;
  exposedModule: string;
}

const remotes: RemoteConfig[] = await fetch("/assets/remotes.json").then((r) =>
  r.json(),
);

const routes: Routes = remotes.map((r) => ({
  path: r.path,
  loadChildren: () =>
    loadRemoteModule(r.name, r.exposedModule).then((m) => m.routes),
}));
```

Then you call `router.resetConfig([...staticRoutes, ...routes])` and show `remotes` in the menu.

## 125: What does router.resetConfig do?

`router.resetConfig(routes)` replaces the router's whole configuration at runtime. In micro frontends it's used to add routes for remotes that you only learn about at runtime, for example from a config API.

You usually call it once at startup, before the first navigation, or in an app initializer.

## 126: What is provideAppInitializer and how is it used in micro frontends?

`provideAppInitializer` runs a function while Angular starts the app and waits for it if it returns a promise or observable. Shells use it to load remote config or set up routes before the first page shows.

```ts
export const appConfig: ApplicationConfig = {
  providers: [
    provideRouter(routes),
    provideAppInitializer(() => {
      const config = inject(RemoteConfigService);
      return config.load();
    }),
  ],
};
```

It replaced the older `APP_INITIALIZER` token, which is deprecated.

## 127: What is the "mount" step of a micro frontend?

Mounting means creating the micro frontend's UI in a given place on the page. With Angular routes, the router does it when you navigate. With web components, the browser does it when the custom element is added to the DOM. With single-spa, the framework calls the app's `mount` function.

## 128: What is the "unmount" step and why does it matter?

Unmounting means removing the micro frontend from the page and cleaning up. With Angular routes, the router destroys the components. With web components, the custom element is removed and Angular destroys the component.

It matters because leftover subscriptions, timers or global event listeners keep running and leak memory. Each micro frontend must clean up properly, for example with `DestroyRef` or `takeUntilDestroyed()`.

## 129: How do you clean up global listeners in a remote component?

Use `DestroyRef` to remove them when the component is destroyed:

```ts
export class CartBadgeComponent {
  count = signal(0);

  constructor() {
    const handler = (e: Event) =>
      this.count.set((e as CustomEvent).detail.count);
    window.addEventListener("cart:updated", handler);
    inject(DestroyRef).onDestroy(() =>
      window.removeEventListener("cart:updated", handler),
    );
  }
}
```

Without this, every time the user leaves and comes back, another listener is added.

## 130: What does "loosely coupled" mean for micro frontends?

It means micro frontends know as little as possible about each other. They don't import each other's code, don't read each other's internal state and only talk through small, clear contracts like events or the URL.

Loose coupling is what makes independent deployment safe.

## 131: What does "high cohesion" mean for micro frontends?

It means everything that belongs together is in the same micro frontend. All the parts of "checkout" (pages, forms, API calls, state) live in one place and change together.

High cohesion plus loose coupling is the goal: each micro frontend is complete on its own and has few links to others.

## 132: Can you lazy load a remote only when a user clicks a button?

Yes. `loadRemoteModule` is just a function that returns a promise, so you can call it in any event handler:

```ts
async openChat() {
  const m = await loadRemoteModule('support', './ChatComponent');
  this.chatComponent.set(m.ChatComponent);
}
```

This keeps the remote out of the initial page load entirely.

## 133: What is the "version skew" problem?

Version skew is when different parts of the system run different versions that don't fit together. For example, the shell expects a remote to export `routes`, but the newly deployed remote renamed it to `flightRoutes`. Or the remote was built with a newer Angular minor than the shell.

Micro frontends have this risk all the time because parts are deployed separately.

## 134: What is semantic versioning and why is it used for shared libraries?

Semantic versioning (SemVer) uses `MAJOR.MINOR.PATCH` numbers. A patch is a bug fix, a minor adds features without breaking anything, and a major can break things.

Federation uses these ranges (`^21.0.0`, `~21.1.0`) to decide if a shared package version fits. If everyone follows SemVer, you can tell from the number whether an update is safe.

## 135: What is the difference between ^ and ~ in a version range?

- `^21.1.0` accepts any `21.x.x` version from `21.1.0` up, but not `22`.
- `~21.1.0` accepts only `21.1.x` patch versions.

For shared packages, these ranges decide whether the already loaded version can be reused. `requiredVersion: 'auto'` takes the range from `package.json`.

## 136: What is "eager" in Module Federation shared config?

In webpack Module Federation, `eager: true` puts a shared package into the initial chunk instead of loading it asynchronously. It avoids the async bootstrap step but makes the first bundle bigger and can lead to several copies being loaded.

In most Angular setups you leave it off and use the `bootstrap.ts` split instead.

## 137: What is the "Shared module is not available for eager consumption" error?

It's a webpack Module Federation error. It happens when the app imports a shared package (like `@angular/core`) synchronously at startup, before the federation runtime had a chance to pick a version.

The fix is the `bootstrap.ts` pattern: `main.ts` only does `import('./bootstrap')`, so everything is loaded asynchronously.

## 138: What is a federated module?

A federated module is any module that's loaded across app boundaries through federation, whether it's an exposed component, a routes file or a shared library. To the code that uses it, it looks like a normal module from a dynamic `import()`.

## 139: What tools can you use to see what a remote loads in the browser?

The browser DevTools:

- The **Network** tab shows `remoteEntry.json`, the remote's chunks and shared packages, and if anything failed.
- The **Sources** tab shows the loaded files.
- The **Console** shows federation errors, like version mismatches.

Searching for `importmap` in the **Elements** tab shows the import map Native Federation created.

## 140: What is the most common beginner mistake with micro frontends?

Splitting too early and too small. Teams split a medium-size app into many micro frontends by technical layer (header, footer, sidebar) and then every feature needs changes in several apps.

Start with a few big, domain-based micro frontends, and split more only when a team really needs it.

## 141: Can you use Angular signals across micro frontends?

Yes, as long as Angular is shared as a singleton. A signal in a shared service is a normal object in memory. Any micro frontend that injects the service can read it, and templates update when it changes.

If Angular is not shared (for example separate web component bundles), signals from one app won't trigger change detection in another.

## 142: Can you use NgRx in micro frontends?

Yes. Common approaches:

- One global store in the shell, with each remote adding its own feature state with `provideState` on its routes.
- Each remote uses its own local state (for example NgRx SignalStore) and only shares small things through events or a shared service.

The second approach keeps remotes more independent. A big shared global store creates tight coupling between teams.

## 143: What is a "smart shell" and a "dumb shell"?

A smart shell holds a lot of logic: shared state, business rules, data fetching. A dumb (thin) shell only does layout, routing, auth and loading remotes.

A thin shell is usually better, because the shell becomes a bottleneck if every team needs to change it for their features.

## 144: What are the benefits of using one framework (Angular) for all micro frontends?

- Angular is loaded once and shared.
- Developers can move between teams easily.
- Shared libraries, the design system and tooling work everywhere.
- Communication can use normal Angular services and signals.
- Upgrades can be planned for the whole system.

Most successful Angular micro frontend setups use Angular everywhere.

## 145: What is SSR and does it work with micro frontends?

SSR (Server-Side Rendering) means the server renders the HTML first, so the user sees content faster and search engines can read it. It's harder with micro frontends because the server also has to load remote code.

Native Federation has SSR and hydration support in recent versions, but it needs extra setup. Many micro frontend apps, especially internal ones, skip SSR.

## 146: What is the difference between "client-side composition" and "server-side composition"?

In client-side composition, the browser loads the shell and then the micro frontends, and puts them together. Module Federation, Native Federation and web components work this way.

In server-side composition, a server (or edge worker) builds the page from fragments before sending the HTML. It's better for SEO and first load, but more complex to run.

## 147: What is edge-side composition?

It's server-side composition done on a CDN edge, close to the user. Techniques like Edge Side Includes (ESI) or edge functions put HTML fragments from different services into one page.

It's not common in Angular apps, but you may hear about it in micro frontend architecture discussions.

## 148: Do remotes need their own index.html?

They have one, used when the remote runs standalone. When the shell loads a remote through federation, the remote's `index.html` is not used at all. Only the exposed JavaScript is loaded into the shell's page.

That's why anything a remote needs globally (fonts, global styles, polyfills) shouldn't only be in its own `index.html`.

## 149: Where do global styles go in a micro frontend setup?

Put true global styles (reset, fonts, theme variables) in the shell or in the design system package that the shell loads once. Remotes should use component styles and the design system's CSS variables.

If a remote needs global styles, scope them under a class or element name that only the remote uses, so they don't leak.

## 150: How would you explain micro frontends to a non-technical person?

Think of a big shopping mall. Each shop is run by its own owner, who can redecorate or change products any time without closing the whole mall. The mall itself (the shell) gives the building, the corridors and the main entrance.

Micro frontends work the same way: each team runs its own part of the website, and the shell keeps it all together so customers see one place.

# Moderate Questions (151-300)

## 151: How does Native Federation load shared packages at runtime, step by step?

1. The host calls `initFederation` with the manifest.
2. It downloads each remote's `remoteEntry.json`.
3. It compares the shared packages and versions from the host and all remotes.
4. For each shared package, it picks one version that fits (based on `singleton`, `requiredVersion` and so on).
5. It writes an import map into the page that points each package name to the chosen file.
6. When any code does `import '@angular/core'`, the browser uses the import map to load that one file.

So the browser does the actual loading, and Native Federation only decides which file each name points to.

## 152: How does Native Federation prepare npm packages for sharing at build time?

At build time it takes each shared package and bundles it as a separate ES module file, using esbuild. These files are written to the output folder next to the app's own chunks, and their names and versions go into `remoteEntry.json`.

The results are cached in `node_modules/.cache`, so the next build doesn't have to bundle the same package again.

## 153: Why is the first Native Federation build slower than the next ones?

On the first build, every shared package has to be bundled into its own ES module. That can be a lot of packages with `shareAll`. The results are cached, so later builds only bundle packages that changed.

If builds stay slow, check which packages are shared and use `skip` for ones you don't need to share.

## 154: What happens when the host and a remote share the same package with different versions?

It depends on the config:

- If `singleton: true` and the versions fit each other's ranges, one version is used by everyone, usually the highest one that fits.
- If `singleton: true` and they don't fit, with `strictVersion: true` you get an error; without it you get a warning and the singleton is still used.
- If `singleton` is false, both versions can be loaded and each app uses its own.

For Angular packages you always want one version, so keep them aligned.

## 155: When would you share a package without singleton?

When it's fine to have two versions in the page at the same time. That's true for stateless utility libraries like `date-fns` or `lodash-es`, where each app can safely use its own version.

You still get the benefit of sharing when versions match, and you avoid errors when they don't. Anything with global state or that Angular depends on should stay a singleton.

## 156: How do you share only some packages instead of using shareAll?

Use the `share` helper (or write the entries by hand) for the packages you want:

```js
import {
  withNativeFederation,
  share,
} from "@angular-architects/native-federation/config";

export default withNativeFederation({
  name: "mfe1",
  shared: share({
    "@angular/core": {
      singleton: true,
      strictVersion: true,
      requiredVersion: "auto",
    },
    "@angular/common": {
      singleton: true,
      strictVersion: true,
      requiredVersion: "auto",
    },
    "@angular/router": {
      singleton: true,
      strictVersion: true,
      requiredVersion: "auto",
    },
    rxjs: { singleton: true, strictVersion: true, requiredVersion: "auto" },
  }),
});
```

This gives you more control but you must remember to add new packages.

## 157: What are secondary entry points and why do they matter for sharing?

Many packages have more than one entry point, like `@angular/common` and `@angular/common/http`, or `rxjs` and `rxjs/operators`. Each one is a separate module for the browser.

Native Federation shares secondary entry points too, so `shareAll` can create many files. That's why `skip` is useful for entry points you never import, like `rxjs/testing`.

## 158: What does the ignoreUnusedDeps feature do in Native Federation?

With `ignoreUnusedDeps` enabled, Native Federation checks which shared packages your code actually imports and leaves out the ones you never use. This makes builds faster and the output smaller, without you writing a long `skip` list.

```js
export default withNativeFederation({
  name: "mfe1",
  shared: {
    ...shareAll({
      singleton: true,
      strictVersion: true,
      requiredVersion: "auto",
    }),
  },
  features: {
    ignoreUnusedDeps: true,
  },
});
```

Check the docs for your version, as newer versions turn this on by default.

## 159: Why do some npm packages fail to build with Native Federation?

Native Federation needs to turn each shared package into an ES module. Some old packages only ship CommonJS or use Node.js APIs, and they may not convert cleanly.

Fixes:

- Add the package to `skip` so it's not shared and just gets bundled normally.
- If it's only used at build time, move it to `devDependencies`.
- Describe it by hand with `packageInfo` in the shared config.

## 160: How do you debug "Shared package not found" or version errors?

1. Open each `remoteEntry.json` and compare the `shared` lists and versions.
2. Check the console for warnings about version mismatches.
3. Look at the generated import map in the page to see which file each package points to.
4. Compare `package.json` and the lock file in each project.

Most of the time, one remote was built with a different version of a package than the others.

## 161: How do you keep dependency versions aligned across many micro frontends?

- Use a monorepo with one `package.json` (the Nx "single version policy").
- In a polyrepo, use a shared config or a tool like Renovate to update all repos at the same time.
- Add a CI check that compares versions of key packages against an allowed list.
- Plan Angular major upgrades together, as one project across all teams.

## 162: What is the single version policy?

It's a monorepo rule that every project uses the same version of each external package, because there's only one root `package.json`. Nx recommends it by default.

For micro frontends, this removes most version problems with shared libraries. The trade-off is that every team must upgrade at the same time.

## 163: How do you upgrade Angular across a micro frontend system?

1. Agree on a target version and a time window across teams.
2. Upgrade the shared libraries and design system first.
3. Upgrade the shell and all remotes with `ng update`, plus the matching Native Federation version.
4. Test everything together in a staging environment.
5. Deploy all of them close together, since a singleton Angular can't mix majors.

In a monorepo with a single version policy, this happens in one pull request.

## 164: Can you upgrade one micro frontend to a new Angular major without the others?

Not if Angular is shared as a singleton, because only one version of `@angular/core` can run. You'd have to stop sharing Angular for that remote, which means the remote loads its own Angular.

That only works if the remote is fully isolated, for example as a web component with its own bundle, and it costs extra download size. It's a temporary trick during upgrades or migrations, not a normal setup.

## 165: What does a Native Federation host's federation config look like?

It looks like a remote's config but without `exposes`:

```js
import {
  withNativeFederation,
  shareAll,
} from "@angular-architects/native-federation/config";

export default withNativeFederation({
  name: "shell",
  shared: {
    ...shareAll({
      singleton: true,
      strictVersion: true,
      requiredVersion: "auto",
    }),
  },
  skip: ["rxjs/ajax", "rxjs/fetch", "rxjs/testing", "rxjs/webSocket"],
});
```

The host still needs a config because it also provides shared packages.

## 166: Can a remote also be a host?

Yes. A remote can load other remotes, which makes it both. For example, a "dashboard" remote can load small widget remotes. It then calls `loadRemoteModule` for those, and the shell's manifest (or its own) must know where they live.

Keep such nesting shallow. Deep chains of remotes make loading slower and debugging harder.

## 167: How do you handle a remote that exposes several components?

List each one under its own name:

```js
exposes: {
  './routes': './projects/cart/src/app/cart.routes.ts',
  './MiniCart': './projects/cart/src/app/mini-cart/mini-cart.component.ts',
  './AddToCartButton': './projects/cart/src/app/add-to-cart/add-to-cart.component.ts',
},
```

Each exposed file becomes its own entry point. Expose only what other teams really need.

## 168: Should you expose many small components or a few big entry points?

Prefer a few bigger entry points, like a routes file or a feature component. Each exposed module is a public contract you must keep stable, and many small ones make it hard to change anything.

Small exposed components (like a mini cart widget) are fine when they are clearly meant to be used by others.

## 169: How do you pass inputs to a remote component loaded dynamically?

With `NgComponentOutlet` you can pass inputs directly:

```html
@if (cmp(); as c) {
<ng-container *ngComponentOutlet="c; inputs: { productId: productId() }" />
}
```

With `ViewContainerRef`:

```ts
const ref = this.vcr.createComponent(m.ProductCardComponent);
ref.setInput("productId", 42);
```

Use `setInput` instead of setting the property directly so change detection and signal inputs work.

## 170: How do you listen to outputs of a dynamically loaded remote component?

With `ViewContainerRef`, subscribe to the output on the instance:

```ts
const ref = this.vcr.createComponent(m.AddToCartButtonComponent);
ref.setInput("productId", 42);
const sub = ref.instance.added.subscribe((qty: number) => this.onAdded(qty));
ref.onDestroy(() => sub.unsubscribe());
```

Signal-based `output()` and `@Output()` with `EventEmitter` both have `subscribe`, so this works with either.

## 171: What is inputBinding and outputBinding in createComponent?

Since Angular 20, `createComponent` accepts `bindings`, so you can connect inputs and outputs at creation time:

```ts
import { inputBinding, outputBinding } from "@angular/core";

this.vcr.createComponent(m.AddToCartButtonComponent, {
  bindings: [
    inputBinding("productId", this.productId),
    outputBinding<number>("added", (qty) => this.onAdded(qty)),
  ],
});
```

`inputBinding` with a signal keeps the input updated when the signal changes, which is handy for remote widgets.

## 172: How do you configure a remote route to keep the shell's layout?

Load the remote as child routes under a parent route that uses the shell's layout component:

```ts
{
  path: '',
  component: MainLayoutComponent,
  children: [
    { path: 'orders', loadChildren: () => loadRemoteModule('orders', './routes').then(m => m.routes) },
  ],
},
```

The remote renders inside the layout's `<router-outlet>`.

## 173: How do you handle a full-screen remote that shouldn't show the shell's layout?

Put its route outside the layout route:

```ts
export const routes: Routes = [
  {
    path: "checkout",
    loadChildren: () =>
      loadRemoteModule("checkout", "./routes").then((m) => m.routes),
  },
  { path: "", component: MainLayoutComponent, children: [/* normal pages */] },
];
```

Now `/checkout` renders without the header and menu.

## 174: How do you protect remote routes with guards?

Guards work the same as for normal lazy routes. You can put them in the shell on the route that loads the remote:

```ts
{
  path: 'admin',
  canMatch: [() => inject(AuthStore).isAdmin()],
  loadChildren: () => loadRemoteModule('admin', './routes').then(m => m.routes),
}
```

`canMatch` is best here because if it fails, the remote code is not even downloaded. Remotes can also add their own guards inside their routes.

## 175: Who should own the guards: the shell or the remote?

The shell should own global checks, like "the user must be logged in", because they apply everywhere.

The remote should own feature-specific checks, like "the user needs the `orders:edit` permission for this page", because only the remote team knows its rules. Putting those in the shell means the shell has to change every time a remote's rules change.

## 176: How do you navigate from one micro frontend to another?

Use the router with the full path. Since remotes loaded with `loadChildren` share the shell's router, normal navigation works:

```ts
inject(Router).navigateByUrl("/orders/123");
```

In templates you can use `routerLink="/orders/123"`. Use absolute paths, because relative paths are relative to the current remote.

## 177: Why is hard-coding another micro frontend's routes a problem?

If the cart team writes `/products/123` in its code, and the products team renames the route to `/p/123`, the link breaks without anyone noticing.

Better options are to keep shared route paths in a contracts library, or to send an event like `navigate:product` with the id and let the shell or the owning team decide the URL.

## 178: How do you keep two Angular routers in sync when using web components?

When each web component micro frontend has its own router, listen to URL changes and tell the others. A simple way is to have the inner app react to `popstate` and the shell's router events:

```ts
// inside the web component app
const router = inject(Router);
window.addEventListener("popstate", () =>
  router.navigateByUrl(location.pathname + location.search),
);
```

Libraries like `@angular-architects/module-federation-tools` used to include helpers for this. It's one reason why many teams prefer loading Angular remotes through federation routes instead.

## 179: What is a wildcard route in a remote and why be careful with it?

A wildcard route `path: '**'` catches every URL that didn't match. In a remote's child routes, a wildcard catches all unknown paths under that remote's prefix, which is fine.

But if the remote's routes are mounted at the root, its wildcard can swallow routes meant for other micro frontends. Usually only the shell should have a top-level `**` route for "not found".

## 180: How do you test a remote in isolation?

Test it like any Angular app: unit tests with TestBed (using Vitest or Jasmine), component tests, and end-to-end tests run against the remote in standalone mode.

Things the shell normally provides, like the current user, should be replaced with simple fakes in tests:

```ts
TestBed.configureTestingModule({
  providers: [
    { provide: AuthStore, useValue: { user: signal({ id: 1, name: "Test" }) } },
  ],
});
```

## 181: How do you test the shell without real remotes?

Replace remote loading with local stubs. One way is to wrap `loadRemoteModule` in a small service and mock it in tests:

```ts
@Injectable({ providedIn: "root" })
export class RemoteLoader {
  load<T>(remote: string, module: string): Promise<T> {
    return loadRemoteModule(remote, module);
  }
}
```

In tests, provide a fake `RemoteLoader` that returns a stub component or routes. Then shell tests don't need the remotes running.

## 182: What is contract testing for micro frontends?

Contract testing checks that a micro frontend still keeps its promises to others. For example, a test in the cart remote can check that `./MiniCart` is exposed, exports `MiniCartComponent` and that the component has the agreed inputs.

It catches breaking changes in the remote's own pipeline, before they reach the shell in production.

## 183: How do you do end-to-end tests for the whole micro frontend system?

Run the shell and all remotes (locally, in Docker or against a staging environment) and use a tool like Playwright or Cypress to test the main user journeys across micro frontends.

Keep these tests few and focused on cross-team flows, like "add to cart and check out". Detailed feature tests belong in each remote's own pipeline.

## 184: How do you set up CI/CD for micro frontends?

Each micro frontend gets its own pipeline: lint, test, build and deploy only that app. In a monorepo, tools like Nx `affected` run only the pipelines of projects that changed.

```bash
nx affected -t lint test build
```

Deployment uploads the build to the micro frontend's own location. The shell's manifest either stays the same (if the URL doesn't change) or gets updated by the pipeline.

## 185: How do you deploy a new version of a remote?

1. Build the remote.
2. Upload the hashed JS and CSS files to its location (S3 bucket, CDN, server).
3. Upload the new `remoteEntry.json` last, since it points to the new files.

Uploading `remoteEntry.json` last means users never get a metadata file that points to files that don't exist yet.

## 186: Why should old chunk files stay on the server after a deployment?

Users who already have the page open still use the old `remoteEntry.json` and will request old chunks when they navigate. If you delete them, those users get load errors.

Keep old hashed files for a while (days or weeks) and clean them up later.

## 187: How do you roll back a broken remote deployment?

If each version's files are kept, a rollback is just putting the previous `remoteEntry.json` back (or pointing the manifest to the previous version's folder). No rebuild is needed.

That's a good reason to deploy each version into its own folder, like `/cart/1.4.2/`, and have the manifest or a pointer file decide which one is live.

## 188: What is versioned deployment of remotes?

Each build is uploaded to its own path, for example `https://cdn.example.com/cart/2026-10-28-abc123/remoteEntry.json`. The manifest says which version each environment uses:

```json
{
  "cart": "https://cdn.example.com/cart/2026-10-28-abc123/remoteEntry.json"
}
```

Changing the manifest is the "release". This makes rollbacks, canary releases and testing different versions easy.

## 189: How can you test a new remote version in production before releasing it to everyone?

With a dynamic manifest, you can point some users to a new version. For example, the manifest API can return the new URL for internal users or for a small percentage of traffic.

You can also allow a query parameter or a cookie that overrides one remote's URL, so testers can try a new version in the real production shell. Be careful to restrict this so random users can't load arbitrary URLs.

## 190: What is a canary release for micro frontends?

It's when a new version of a micro frontend is shown only to a small group of users first. If errors stay low, you increase the group until everyone has the new version. If something breaks, you switch the group back.

Micro frontends make canaries easy because you only change which `remoteEntry.json` URL the manifest returns.

## 191: How do you use feature flags with micro frontends?

Feature flags let you turn features on or off without deploying. They can work at two levels:

- Inside a remote, to hide or show a new feature.
- In the shell, to decide whether a whole remote or route is available.

Use one flag service for all micro frontends, shared through a library or a simple API, so flags behave the same everywhere.

## 192: How do you make the shell show a loading state while a remote loads?

The router emits events when lazy loading starts and ends. You can track them in the shell:

```ts
export class AppComponent {
  loading = signal(false);

  constructor() {
    inject(Router)
      .events.pipe(takeUntilDestroyed())
      .subscribe((e) => {
        if (e instanceof RouteConfigLoadStart) this.loading.set(true);
        if (e instanceof RouteConfigLoadEnd) this.loading.set(false);
      });
  }
}
```

Then show a spinner or progress bar when `loading()` is true.

## 193: How do you retry loading a remote after a network error?

Wrap the load in a small retry helper:

```ts
async function loadWithRetry<T>(
  remote: string,
  module: string,
  retries = 2,
): Promise<T> {
  try {
    return await loadRemoteModule(remote, module);
  } catch (err) {
    if (retries === 0) throw err;
    await new Promise((r) => setTimeout(r, 1000));
    return loadWithRetry(remote, module, retries - 1);
  }
}
```

Use it in the route loaders. Combine it with a fallback component for when all retries fail.

## 194: What happens if a remote's remoteEntry.json fails to load during initFederation?

That depends on the version and setup. A failed remote can make `initFederation` reject, which, if you're not careful, stops the shell from starting at all.

Make sure one unreachable remote doesn't block the whole shell. Catch errors around `initFederation` and still bootstrap, then handle the missing remote at the route level with a fallback. Test this case on purpose by stopping one remote locally and reloading the shell.

## 195: How do you track errors in micro frontends?

Use one error tracking tool (like Sentry) for all micro frontends, set up in the shell or a shared library. Tag each error with the micro frontend it came from, its version and the user's route.

```ts
export class GlobalErrorHandler implements ErrorHandler {
  handleError(error: unknown) {
    // send to your tracking service with a tag for the current remote
    console.error(error);
  }
}
```

Without tags, you can't tell which team should fix an error.

## 196: How can you know which micro frontend an error came from?

Options:

- Look at the file URL in the stack trace (each remote is served from its own path).
- Upload source maps per remote to your error tool.
- Let each remote set its name in an error context when it loads.
- Use separate error handlers or tags per remote route.

Serving each remote from a clearly named path (like `/mfe/cart/`) makes this much easier.

## 197: How do you handle source maps in micro frontends?

Each micro frontend generates its own source maps at build time. Upload them to your error tracking service with the remote's name and version, and don't serve them publicly if you don't want your code visible.

In development, source maps from all remotes load in the browser DevTools, so you can debug each remote's TypeScript directly.

## 198: How do you debug a remote while it's running inside the shell?

Run the shell and the remote locally with `ng serve`. The shell's manifest points to the local remote. Now changes in the remote reload in the shell, and DevTools shows the remote's source files with source maps.

You can also run the shell from a deployed environment and point just one remote to localhost, if your manifest supports overrides.

## 199: How do you point a deployed shell to a local remote for debugging?

Some teams add a developer-only override, for example a value in `localStorage`:

```ts
const overrides = JSON.parse(localStorage.getItem("mf-overrides") ?? "{}");
const manifest = await fetch("/assets/federation.manifest.json").then((r) =>
  r.json(),
);
initFederation({ ...manifest, ...overrides }).then(() => import("./bootstrap"));
```

Then you set `{"cart": "http://localhost:4203/remoteEntry.json"}` in DevTools. Only enable this for non-production environments or trusted users, since it lets the page load code from any URL.

## 200: How do you share a design system across micro frontends?

Build it as an Angular library with standalone components and a theme (CSS variables). Then either:

- publish it to an npm registry and install it in each micro frontend, or
- keep it in the monorepo as a library.

Share it as a singleton in the federation config so it's loaded once and all micro frontends use the same version.

## 201: How do you theme micro frontends so they look the same?

Use CSS custom properties (variables) for colors, spacing and fonts, defined once by the shell or the design system:

```css
:root {
  --color-primary: #1d4ed8;
  --space-md: 16px;
  --font-body: "Inter", sans-serif;
}
```

Remotes use the variables in their component styles instead of hard-coded values. Changing the theme in one place then updates every micro frontend, even ones deployed at different times.

## 202: How do you use Angular Material in micro frontends?

Share `@angular/material` and `@angular/cdk` as singletons. Set up the Material theme once, in the shell's global styles. Remotes import the Material components they need in their standalone components but don't include their own theme.

If each remote added its own theme, you'd get duplicate CSS and theme conflicts.

## 203: What problems can CDK overlays cause in micro frontends?

Overlays (dialogs, menus, tooltips) are added to a container at the end of `<body>`, outside the remote's own DOM. If the remote uses Shadow DOM or scoped global styles, the overlay may not get those styles.

Also, if `@angular/cdk` is not shared as a singleton, two overlay containers can be created and z-index problems appear. Sharing the CDK and keeping the theme in the shell avoids most of this.

## 204: How do you prevent CSS class name clashes between micro frontends?

- Use Angular's default emulated view encapsulation for component styles.
- Prefix any global classes with the micro frontend's name, like `.cart-...`.
- Avoid styling plain element selectors (`button`, `a`) globally in remotes.
- Use the design system's components instead of custom global CSS.
- Consider Shadow DOM for widgets that must be fully isolated.

## 205: What is the downside of using Shadow DOM for Angular micro frontends?

Global styles from the shell and the design system don't reach inside the shadow root (except inherited properties and CSS variables). So you have to load the design system's CSS inside each shadow root, which can duplicate styles.

Some third-party libraries that query `document` or add elements to `body` also don't work well with Shadow DOM. Use it where you really need isolation.

## 206: How does Tailwind CSS work with micro frontends?

Each micro frontend's Tailwind build only includes the classes it uses. Problems appear when several remotes ship different Tailwind versions or configs, so the same class looks different, or global base styles (preflight) are loaded several times.

Common fixes: share one Tailwind config/preset across all apps, load base styles only in the shell, and optionally use a prefix per remote to avoid clashes.

## 207: How do you load fonts once for all micro frontends?

Load fonts in the shell (in its `index.html` or global styles). Remotes just use the font family by name or through a CSS variable.

If every remote loaded the same font file again, the browser may cache it, but you still add extra requests and risk loading different versions.

## 208: How do you share images and static assets between micro frontends?

Shared assets (logos, icons) should live in the design system or on a shared CDN path. Remote-specific assets should be loaded with full URLs or paths relative to the remote's own location.

A common bug is a remote using `/assets/logo.png`, which works when it runs alone but points to the shell's server when loaded inside the shell.

## 209: How do you fix asset paths in a remote loaded by the shell?

Build asset URLs from the remote's own base URL instead of the page's URL. One simple way is to use `import.meta.url` in the remote code:

```ts
const logoUrl = new URL("../assets/logo.png", import.meta.url).href;
```

This resolves relative to the JavaScript file, which lives on the remote's server. Another option is to serve all remotes under one domain with clear paths and use full paths like `/mfe/cart/assets/logo.png`.

## 210: What is the difference between deployUrl and baseHref?

`baseHref` sets the `<base href>` tag, which the router and relative URLs in the page use. `deployUrl` was an older option that told the build where the JS and CSS files are served from.

`deployUrl` is deprecated in the esbuild builder. For micro frontends, the remote's files are found from its `remoteEntry.json` URL, so you rarely need it. Use `import.meta.url` or full URLs for assets instead.

## 211: How do you share data between micro frontends with a shared service using signals?

Put the service in a shared library and mark that library as shared in the federation config:

```ts
@Injectable({ providedIn: "root" })
export class CartState {
  private readonly items = signal<CartItem[]>([]);
  readonly count = computed(() => this.items().length);

  add(item: CartItem) {
    this.items.update((list) => [...list, item]);
  }
}
```

The cart remote calls `add`, and the shell's header shows `count()`. Both inject the same instance because the library is a singleton.

## 212: What are the risks of sharing state through a common service?

- Teams become tightly coupled through the service's API.
- A breaking change in the service affects every micro frontend at the same time.
- It's easy to slowly put more and more state in it until it becomes a global store nobody owns.
- If the library is accidentally bundled twice, state silently splits.

Keep shared services small, with one owning team, and treat their API as a versioned contract.

## 213: How do you use BroadcastChannel between micro frontends?

`BroadcastChannel` sends messages between all scripts on the same origin, including other tabs:

```ts
const channel = new BroadcastChannel("auth");

// on logout
channel.postMessage({ type: "logout" });

// in any micro frontend or tab
channel.onmessage = (e) => {
  if (e.data.type === "logout") location.href = "/login";
};
```

It's handy for things like "log out in all tabs". Within one page, custom events are simpler.

## 214: How do you create a small typed event bus for micro frontends?

Put it in the shared contracts library:

```ts
export interface AppEvents {
  "cart:updated": { count: number };
  "user:logout": void;
}

export function emit<K extends keyof AppEvents>(type: K, detail: AppEvents[K]) {
  window.dispatchEvent(new CustomEvent(type, { detail }));
}

export function on<K extends keyof AppEvents>(
  type: K,
  fn: (detail: AppEvents[K]) => void,
) {
  const handler = (e: Event) => fn((e as CustomEvent<AppEvents[K]>).detail);
  window.addEventListener(type, handler);
  return () => window.removeEventListener(type, handler);
}
```

The types make sure sender and receiver agree on the payload, and the bus works even if the library is not shared at runtime.

## 215: Why use window events instead of an RxJS Subject for an event bus?

An RxJS `Subject` in a library only works if every micro frontend uses the same instance, which needs perfect runtime sharing. If one remote bundles its own copy, it gets its own subject and misses the messages.

`window` is always the same object for everyone on the page, so custom events work even with separate bundles or different frameworks.

## 216: When would a missed event be a problem and how do you solve it?

Events are fire-and-forget. If the cart remote sends `cart:updated` before the header has loaded and started listening, the header misses it and shows the wrong count.

Solutions: keep the latest value somewhere the late listener can read it (a shared service with a signal, `sessionStorage`, or an API), or let the late listener ask for the current state with a request event.

## 217: How do you share data through web component attributes and properties?

For web component micro frontends, the host passes data in with attributes (strings only) or properties (any value), and gets data out with DOM events:

```html
<product-card product-id="42"></product-card>
```

```ts
const card = document.querySelector("product-card")!;
(card as any).product = { id: 42, name: "Shoes" };
card.addEventListener("addToCart", (e) =>
  console.log((e as CustomEvent).detail),
);
```

Angular Elements maps component inputs to attributes and properties, and outputs to custom events.

## 218: How does Angular Elements map inputs and outputs?

When you create a custom element with `createCustomElement`:

- Each input becomes a property with the same name and an attribute in dash-case (`productId` becomes `product-id`).
- Each output becomes a `CustomEvent` with the output's name, and the emitted value goes into `event.detail`.

Attributes are strings, so for numbers or objects you should set the property instead.

## 219: How do you use an Angular Elements micro frontend inside an Angular shell?

Load the element's script and add `CUSTOM_ELEMENTS_SCHEMA` to the component that uses the tag:

```ts
function loadScript(src: string): Promise<void> {
  return new Promise((resolve, reject) => {
    const script = document.createElement("script");
    script.type = "module";
    script.src = src;
    script.onload = () => resolve();
    script.onerror = reject;
    document.head.appendChild(script);
  });
}

@Component({
  selector: "app-product-page",
  schemas: [CUSTOM_ELEMENTS_SCHEMA],
  template: `<product-card
    [productId]="id()"
    (addToCart)="onAdd($event)"
  ></product-card>`,
})
export class ProductPageComponent {
  id = input.required<number>();

  constructor() {
    loadScript("https://cdn.example.com/product-card/main.js");
  }

  onAdd(e: Event) {
    console.log((e as CustomEvent).detail);
  }
}
```

Without `CUSTOM_ELEMENTS_SCHEMA`, Angular complains that it doesn't know the element.

## 220: What is CUSTOM_ELEMENTS_SCHEMA?

It's a schema you add to a component's `schemas` to tell Angular that unknown elements with a dash in their name are custom elements. Angular then allows them in the template and lets you bind to any property or event on them.

The downside is you lose type checking for those elements, so typos in property names are not caught.

## 221: How do you combine Native Federation and web components?

You expose a file that registers the custom element, load it with `loadRemoteModule`, and then use the tag:

```ts
// remote exposes './web-components' which calls customElements.define('mfe-react', ...)
await loadRemoteModule("reactMfe", "./web-components");
```

This lets you load micro frontends from other frameworks (or other Angular versions) through federation, while the browser handles rendering through the custom element.

## 222: How does Native Federation handle remotes built with other frameworks?

Native Federation is not tied to Angular. There's the core `@softarc/native-federation` package with adapters for other build setups, so a React or Vue app built with esbuild or Vite can also be a remote.

The usual way to show such a remote in an Angular shell is to wrap it as a web component, expose that, and load it with `loadRemoteModule`.

## 223: What is @angular-architects/module-federation-tools?

It was a helper package with a `WebComponentWrapper` component and router helpers to load web component micro frontends (often from other frameworks or Angular versions) in a shell.

It's not actively developed for new Angular versions anymore. You will still see it in older multi-framework setups, but for new projects you can write a small wrapper yourself or use the newer Module Federation runtime APIs.

## 224: How do you write a small wrapper component for a web component remote?

```ts
@Component({
  selector: "app-wc-remote",
  template: "",
})
export class WebComponentRemoteComponent {
  remoteName = input.required<string>();
  exposedModule = input.required<string>();
  elementName = input.required<string>();

  private host = inject(ElementRef<HTMLElement>);

  constructor() {
    afterNextRender(async () => {
      await loadRemoteModule(this.remoteName(), this.exposedModule());
      this.host.nativeElement.appendChild(
        document.createElement(this.elementName()),
      );
    });
  }
}
```

You can use it in routes with `data` or with route inputs to show any web component remote.

## 225: What is single-spa's root config?

The root config is the main HTML page and script in single-spa. It registers each micro frontend with a name, a loading function and an "active when" rule:

```js
import { registerApplication, start } from "single-spa";

registerApplication({
  name: "@org/orders",
  app: () => System.import("@org/orders"),
  activeWhen: ["/orders"],
});

start();
```

single-spa mounts and unmounts each app as the URL changes.

## 226: What does single-spa-angular do?

`single-spa-angular` connects an Angular app to single-spa. It gives your Angular app the `bootstrap`, `mount` and `unmount` lifecycle functions single-spa needs, and handles starting and destroying the Angular app.

```ts
import {
  singleSpaAngular,
  getSingleSpaExtraProviders,
} from "single-spa-angular";

const lifecycles = singleSpaAngular({
  bootstrapFunction: () =>
    bootstrapApplication(AppComponent, {
      providers: [...appConfig.providers, getSingleSpaExtraProviders()],
    }),
  template: "<app-root />",
  NgZone,
  Router,
});

export const { bootstrap, mount, unmount } = lifecycles;
```

Check the version you use, since its support for new Angular versions and the esbuild builder has lagged behind Angular releases.

## 227: What are the downsides of single-spa compared to federation?

- Each Angular app usually bundles its own Angular unless you set up shared import maps by hand.
- Several Angular apps run at once, each with its own router.
- Extra setup for SystemJS or import maps and for lifecycles.
- Angular support depends on a community package.

Federation gives you shared Angular out of the box and uses the normal Angular router, which is simpler for Angular-only systems.

## 228: When would single-spa still be a good choice?

When you have many micro frontends in different frameworks (Angular, React, Vue, Svelte) and want one consistent way to mount them by route. single-spa is framework-neutral and has adapters for most frameworks.

It's also common in existing systems that started before Module Federation existed.

## 229: How do you migrate from webpack Module Federation to Native Federation?

1. Upgrade Angular and switch from `@angular-architects/module-federation` to `@angular-architects/native-federation`.
2. Run the Native Federation `init` schematic for each project, which creates `federation.config` and changes the builder.
3. Move `exposes`, `shared` and names from `webpack.config.js` to the new config.
4. Change `loadRemoteModule` calls to the Native Federation version, using remote names.
5. Change the manifest from `remoteEntry.js` URLs to `remoteEntry.json` URLs.
6. Remove the webpack config and `ngx-build-plus`.

Do one environment at a time and test everything, since a host and remote must use the same kind of federation.

## 230: Can a Native Federation host load a webpack Module Federation remote?

Not directly. They use different formats (`remoteEntry.json` with import maps versus `remoteEntry.js` with the webpack runtime). During a migration you either move host and remotes together, or you wrap the old remote as a web component and load its script separately.

## 231: What is ngx-build-plus?

`ngx-build-plus` is a package that extends the Angular CLI webpack builder so you can pass a partial webpack config. Older Angular Module Federation setups used it to add the Module Federation plugin.

With Angular's move to esbuild, it's mostly a legacy tool. You'll see it in older micro frontend projects.

## 232: What is Module Federation 2.0?

Module Federation 2.0 is the newer version of Module Federation, maintained by the module-federation.io team. Its runtime is in `@module-federation/enhanced` and works with webpack and Rspack. It adds things like:

- A runtime API you can use without the bundler plugin config (`loadRemote`, `registerRemotes`)
- An `mf-manifest.json` file with more metadata
- Automatic TypeScript types for remotes
- Runtime plugins and DevTools support

It's used more in React and Rspack setups but can be used with Angular projects that build with webpack or Rspack.

## 233: What is Rspack and how does it relate to Angular micro frontends?

Rspack is a fast, webpack-compatible bundler written in Rust. It supports Module Federation natively. There are community projects (like Nx's Angular Rspack support) to build Angular apps with Rspack, which lets you use Module Federation 2.0 while getting faster builds than webpack.

For most Angular teams on the default CLI, Native Federation is still the simpler path.

## 234: What is mf-manifest.json?

It's a JSON file Module Federation 2.0 generates. It describes a remote's exposed modules, shared dependencies and assets, similar to Native Federation's `remoteEntry.json`. Hosts can load a remote by pointing to its manifest instead of `remoteEntry.js`.

Tools like the Module Federation Chrome DevTools extension use it to show what's loaded.

## 235: How do you load a remote with the Module Federation 2.0 runtime API?

```ts
import { createInstance } from "@module-federation/enhanced/runtime";

const mf = createInstance({
  name: "shell",
  remotes: [
    { name: "cart", entry: "https://cdn.example.com/cart/mf-manifest.json" },
  ],
});

const mod = await mf.loadRemote<{ MiniCartComponent: Type<unknown> }>(
  "cart/MiniCart",
);
```

Older versions of the runtime used the global `init` and `loadRemote` functions instead of `createInstance`. Check your version's docs.

## 236: How do you register remotes at runtime with Module Federation 2.0?

Use `registerRemotes` on the instance:

```ts
mf.registerRemotes([
  { name: "orders", entry: "https://cdn.example.com/orders/mf-manifest.json" },
]);
```

This is the Module Federation 2.0 way of having a dynamic host, similar to a Native Federation manifest.

## 237: How does Nx help run micro frontends locally?

When you serve the host with Nx, it can also serve the remotes. Remotes you're not working on are served from a pre-built version (static files), and only the ones you're editing get a live dev server:

```bash
nx serve shell --devRemotes=cart
```

This saves a lot of memory and CPU compared to running every remote in dev mode.

## 238: What is the Nx project graph and why is it useful here?

The project graph shows which projects depend on which libraries. `nx graph` opens it in the browser. Nx uses it to know what's affected by a change.

For micro frontends, it shows quickly if one remote secretly imports another remote's code, which breaks independence. You can also add rules to block such imports.

## 239: How do you stop one micro frontend from importing another's code in a monorepo?

Use Nx module boundary rules with tags. Tag projects and libraries (`scope:cart`, `scope:orders`, `scope:shared`) and add an ESLint rule:

```json
"@nx/enforce-module-boundaries": [
  "error",
  {
    "depConstraints": [
      { "sourceTag": "scope:cart", "onlyDependOnLibsWithTags": ["scope:cart", "scope:shared"] },
      { "sourceTag": "scope:orders", "onlyDependOnLibsWithTags": ["scope:orders", "scope:shared"] }
    ]
  }
]
```

Now ESLint fails if the cart imports from orders. Sheriff is a similar tool that doesn't need Nx.

## 240: What is Sheriff?

Sheriff (`@softarc/sheriff-core`) is a tool from the same authors as Native Federation. It enforces module boundaries in TypeScript projects without Nx. You define modules and tags in a `sheriff.config.ts` and it reports imports that cross boundaries, through an ESLint plugin.

It's useful in Angular CLI workspaces that host several micro frontends in one repo.

## 241: What is a "micro frontend per route" vs "micro frontend per component" decision?

Per route (page-level) means each remote owns whole pages. It's simple and works well with the Angular router.

Per component (widget-level) means remotes provide pieces that are mixed on one page. It's more flexible but adds runtime loading on the same page, more communication and more risk of one widget slowing or breaking the page.

Most teams start with per route and add a few widgets only where really needed.

## 242: How do you handle a remote that's slow to load?

- Show a skeleton or spinner while it loads.
- Preload it when the user is likely to need it (on hover or when idle).
- Make sure its shared dependencies are really shared and not downloaded again.
- Check its bundle size and lazy load heavy parts inside the remote.
- Make sure the CDN and caching headers are set correctly.

## 243: How do you preload a remote before the user navigates to it?

Call `loadRemoteModule` early, for example when the browser is idle or on mouse hover over the menu link:

```ts
preloadOrders() {
  loadRemoteModule('orders', './routes').catch(() => {});
}
```

```html
<a routerLink="/orders" (mouseenter)="preloadOrders()">Orders</a>
```

The module stays cached, so the real navigation is instant. You can also write a custom Angular `PreloadingStrategy` for remote routes.

## 244: Does Angular's PreloadAllModules work with remote routes?

Yes. Remote routes use `loadChildren` or `loadComponent`, so Angular's preloading strategies treat them like any other lazy route. With `withPreloading(PreloadAllModules)`, the router loads all remotes in the background after the app starts.

That may load a lot of code users never need, so a custom strategy that preloads only some remotes is often better.

## 245: How do you write a custom preloading strategy for remotes?

```ts
@Injectable({ providedIn: "root" })
export class FlagPreloadingStrategy implements PreloadingStrategy {
  preload(route: Route, load: () => Observable<unknown>): Observable<unknown> {
    return route.data?.["preload"] ? load() : of(null);
  }
}

export const appConfig: ApplicationConfig = {
  providers: [provideRouter(routes, withPreloading(FlagPreloadingStrategy))],
};
```

Mark remote routes with `data: { preload: true }` to preload only those.

## 246: How do you measure the bundle size of each micro frontend?

Build each one with stats and look at the output:

```bash
ng build mfe1 --stats-json
```

Then open the stats file with a tool like `esbuild-visualizer` or a bundle analyzer. Also check the Network tab in the shell to see what each remote actually downloads at runtime, including shared packages.

## 247: How do you set bundle budgets for micro frontends?

Use Angular budgets in each project's `angular.json`:

```json
"budgets": [
  { "type": "initial", "maximumWarning": "500kB", "maximumError": "1MB" },
  { "type": "anyComponentStyle", "maximumWarning": "4kB" }
]
```

Each team sets its own budget, so one remote can't slowly grow without anyone noticing. The platform team can also check the total load in end-to-end tests.

## 248: What are Web Vitals and why do they matter more with micro frontends?

Web Vitals (LCP, INP, CLS) measure how fast and stable a page feels. Micro frontends add more network requests and runtime loading, which can make LCP slower. Widgets loading late can push content around and hurt CLS.

Each team should watch the Web Vitals of its pages, and the shell team should watch the overall numbers.

## 249: How do you avoid layout shift when a remote widget loads?

Reserve space for the widget before it loads, with a fixed height or a skeleton of the same size:

```css
.mini-cart-slot {
  min-height: 48px;
}
```

Without reserved space, the page jumps when the widget appears, which hurts CLS and annoys users.

## 250: How do you handle the user's language and locale across micro frontends?

Keep one source of truth, often the URL (`/de/orders`) or a shared settings service. When the language changes, notify everyone (signal in a shared service, or a custom event). Each micro frontend loads its own translations for that language.

Make sure the `LOCALE_ID` and date or number formats are the same everywhere, otherwise one part shows `28.10.2026` and another `10/28/2026`.

## 251: How do you share LOCALE_ID across micro frontends?

If Angular is shared and remotes are loaded as routes into the shell, they use the shell's root injector, so the `LOCALE_ID` the shell provides applies to them too:

```ts
export const appConfig: ApplicationConfig = {
  providers: [{ provide: LOCALE_ID, useValue: "de-DE" }],
};
```

Remotes should not provide their own `LOCALE_ID` at root. They also need the locale data registered once (`registerLocaleData`), which the shell can do.

## 252: What is the difference between a remote's standalone appConfig and the providers it gets inside the shell?

When the remote runs alone, `bootstrap.ts` uses the remote's own `appConfig` with its own `provideRouter`, `provideHttpClient` and so on.

When it's loaded inside the shell through `loadChildren`, its `appConfig` is not used at all. The remote's routes get the shell's root providers plus whatever the remote puts in route `providers`. So anything the remote needs inside the shell must be in its routes, not only in `appConfig`.

## 253: How do you make a remote work both standalone and inside the shell without duplicating providers?

Put the remote's feature providers in a function and use it in both places:

```ts
// remote: feature.providers.ts
export function provideFlightsFeature(): (Provider | EnvironmentProviders)[] {
  return [FlightService, provideState(flightsFeature)];
}

// remote: app.routes.ts (exposed)
export const routes: Routes = [
  { path: "", providers: [provideFlightsFeature()], children: [/* ... */] },
];

// remote: app.config.ts (standalone only)
export const appConfig: ApplicationConfig = {
  providers: [provideRouter(routes), provideHttpClient()],
};
```

The exposed routes carry the feature providers, and `appConfig` only adds what the shell would normally give.

## 254: What is the danger of calling provideHttpClient() again in a remote's routes?

It creates a new `HttpClient` for that part of the app, with its own interceptor chain. The shell's interceptors (like adding the auth token) won't run for the remote's requests unless you set them up again.

If you do need extra interceptors in a remote, use `withRequestsMadeViaParent()` so requests also go through the parent's interceptors:

```ts
providers: [
  provideHttpClient(
    withInterceptors([flightsInterceptor]),
    withRequestsMadeViaParent(),
  ),
];
```

## 255: How do you add a remote's NgRx feature state when loaded into the shell?

Provide the feature state on the remote's routes:

```ts
export const routes: Routes = [
  {
    path: "",
    providers: [provideState(ordersFeature), provideEffects(OrdersEffects)],
    children: [{ path: "", component: OrdersListComponent }],
  },
];
```

The shell provides `provideStore()` once at root. When the remote's route loads, its state slice is added to the global store. Both shell and remote must share `@ngrx/store` as a singleton.

## 256: Why is NgRx SignalStore often a better fit for remotes than a global store?

A SignalStore can be provided on the remote's own route or component, so its state lives and dies with the remote. It doesn't need a global store from the shell, and other teams can't easily depend on its internals.

```ts
export const OrdersStore = signalStore(
  withState({ orders: [] as Order[], loading: false }),
);

// in the remote's route
providers: [OrdersStore];
```

This keeps remotes more independent.

## 257: How do you avoid duplicate HTTP requests when several micro frontends need the same data?

Put the data loading in a shared service that caches the result, for example with a signal or `shareReplay`, and make sure the service is a singleton:

```ts
@Injectable({ providedIn: "root" })
export class UserProfileService {
  readonly profile = httpResource<UserProfile>(() => "/api/me");
}
```

All micro frontends read `profile.value()` from the same instance, so the request happens once. Or let the shell load it once and pass it to remotes.

## 258: How do you handle logout across micro frontends?

The shell handles logout: it clears the session (calls the back-end, clears tokens) and then notifies everyone, for example through a shared auth signal or a `user:logout` event. Remotes listen and clear their own cached data.

Often the simplest safe approach is to do a full page reload or redirect to the login page after logout, so no old state stays in memory.

## 259: How do you share permissions or roles with micro frontends?

The shell loads the user's permissions once after login and puts them in a shared auth service. Remotes check them with helper functions or directives from a shared library:

```ts
@Injectable({ providedIn: "root" })
export class Permissions {
  private readonly perms = signal<Set<string>>(new Set());
  has(p: string) {
    return this.perms().has(p);
  }
}
```

Always check permissions on the back-end too. Front-end checks are only for showing or hiding UI.

## 260: How do you handle different back-end APIs for each micro frontend?

Usually each micro frontend talks to its own back-end service (or Backend For Frontend). The base URL can come from a config file the remote loads at runtime, or from relative paths behind a reverse proxy (`/api/orders/...`).

Avoid putting all API URLs into the shell's config, because then every new endpoint needs a shell change.

## 261: What is a Backend For Frontend (BFF) in this context?

A BFF is a small back-end made for one front-end. In micro frontends, each team can have its own BFF that gives its micro frontend exactly the data it needs, in the right shape.

It keeps teams independent end to end: one team owns the micro frontend and its BFF, and can change both together.

## 262: How do you load runtime configuration in a remote?

Fetch a config JSON from the remote's own location, not the shell's. Use `import.meta.url` to build the URL:

```ts
@Injectable({ providedIn: "root" })
export class OrdersConfig {
  private readonly url = new URL("./config.json", import.meta.url).href;
  readonly config = httpResource<{ apiUrl: string }>(() => this.url);
}
```

This way, the remote always gets its own config, whether it runs alone or inside the shell.

## 263: Why might environment.ts files be a problem in micro frontends?

`environment.ts` values are baked in at build time. That means one build per environment, and a remote built for "test" points to test APIs forever.

For micro frontends you usually want one build that can be deployed anywhere, so runtime config (a JSON file loaded at startup) is a better fit than build-time environments.

## 264: How do you handle CORS for API calls from remotes?

The browser sends API calls from the page's origin, which is the shell's origin, not the remote's. So each back-end must allow the shell's origin with CORS headers, or you put the APIs behind the same domain with a reverse proxy.

Same domain (for example `/api/orders` proxied to the orders service) avoids CORS completely and keeps cookies simple.

## 265: How do you set up a dev proxy when running a remote inside the shell?

Configure the proxy in the shell, since its dev server receives the API calls:

```json
// projects/shell/proxy.conf.json
{
  "/api/orders": { "target": "http://localhost:3001", "secure": false },
  "/api/cart": { "target": "http://localhost:3002", "secure": false }
}
```

```json
"serve": { "options": { "proxyConfig": "projects/shell/proxy.conf.json" } }
```

Each remote also needs its own proxy for when it runs standalone.

## 266: How do remotes use the shell's HTTP interceptors?

If the remote is loaded through routes and doesn't create its own `HttpClient`, it injects the shell's root `HttpClient`, and all the shell's interceptors run for its requests automatically.

That's usually what you want for auth headers, error handling and logging.

## 267: How do you show global notifications (toasts) from any micro frontend?

The shell owns the toast UI and a notification service in a shared library. Remotes call the service:

```ts
inject(NotificationService).success("Order saved");
```

If the library is not shared, use a custom event like `notify` that the shell listens for. Either way, there's one place showing toasts, so they look and stack the same.

## 268: How do you handle dialogs opened by a remote?

If the remote uses Angular Material or CDK dialogs and those packages are shared, the dialog opens in the same overlay container as everything else and works fine.

Make sure the dialog component is part of the remote's code, and that it's closed when the user navigates away from the remote (Material does this by default with `closeOnNavigation`).

## 269: How do you handle the browser back button with micro frontends?

With remotes loaded into one Angular router, the back button works normally because there's one history.

With several routers (web components, single-spa), each router listens to `popstate`. They must all react correctly to URL changes and not push duplicate history entries. Test back/forward navigation carefully in these setups.

## 270: How do you pass route parameters from the shell to a remote?

When the remote's routes are mounted under the shell's route, the remote can read params with normal router APIs, including component input binding:

```ts
// shell: provideRouter(routes, withComponentInputBinding())

// remote component
export class OrderDetailsComponent {
  id = input.required<string>();
}
```

The `:id` in the remote's route is bound to the `id` input. Parent params from the shell need `paramsInheritanceStrategy: 'always'` to be available.

## 271: What is the role of data in remote routes?

Route `data` can carry static information like a page title, a breadcrumb label or a "preload" flag. The shell can read it to build breadcrumbs or the document title:

```ts
{ path: 'orders', data: { breadcrumb: 'Orders' }, loadChildren: () => loadRemoteModule('orders', './routes').then(m => m.routes) }
```

Remotes can add `data` on their own routes too, and the shell reads it from the router state.

## 272: How do you set the page title from a remote?

Use the route `title` property in the remote's routes. Angular's `TitleStrategy` (provided by the shell) sets `document.title` on navigation:

```ts
export const routes: Routes = [
  { path: "", title: "My orders", component: OrdersListComponent },
];
```

The shell can provide a custom `TitleStrategy` to add a suffix like " | MyShop" to every page.

## 273: How do you organize a monorepo with a shell, remotes and shared libraries?

A typical layout:

```text
apps/
  shell/
  cart/
  orders/
libs/
  shared/ui/          design system
  shared/auth/        auth service
  shared/contracts/   types and events
  cart/feature/       cart-only code
  orders/feature/     orders-only code
```

Remotes depend on their own libs and `shared/*`, never on each other.

## 274: How do you share code without sharing it at runtime?

Just import the library and don't list it in `shared`, or list it in `skip`. Each micro frontend then bundles its own copy at build time.

This is good for small, stateless code like utility functions or types. Updates still need each micro frontend to rebuild, but there's no runtime version risk.

## 275: When should a shared library be shared at runtime and when bundled?

Share at runtime (singleton) when:

- it holds state that must be the same everywhere (auth, store),
- it's big and used by most micro frontends (Angular, Material),
- it registers global things (custom elements, global styles).

Bundle it when it's small, stateless and teams may want different versions.

## 276: How do you publish a shared Angular library to npm?

Create a library project and build it with ng-packagr:

```bash
ng generate library @my-org/ui
ng build @my-org/ui
cd dist/my-org/ui
npm publish
```

Teams install it with `npm install @my-org/ui`. Use a private registry (GitHub Packages, Artifactory, Verdaccio) for internal libraries.

## 277: What are the trade-offs of a shared library in a polyrepo?

Pros: clear versioning, each team picks when to upgrade.

Cons: every change needs a publish and upgrades in many repos, different teams end up on different versions, and if the library is shared at runtime, version mismatches cause errors. Teams need a clear upgrade policy, like "stay at most one minor behind".

## 278: How do you document what each micro frontend exposes?

Keep a short README per remote with:

- Exposed module names and what they export
- Inputs, outputs and events
- Required providers or shared services
- Route prefix and main pages
- Owning team and contact

Some teams generate parts of this from the federation config and types. The important thing is that other teams can find it without asking.

## 279: How do you handle breaking changes in an exposed module?

Don't change the existing one in place. Add a new exposed name (for example `./routes-v2`), keep the old one working for a while, tell the consuming teams, and remove the old one only when nobody uses it anymore.

It's the same idea as versioning a public API.

## 280: What is the "strangler fig" pattern?

It's a way to replace an old system bit by bit. You put a new system in front of the old one and move features over one at a time, until the old system is gone.

With micro frontends, the shell (or a proxy) sends some routes to new Angular micro frontends and the rest to the old app. Over time, more routes move to the new side.

## 281: How do you migrate an AngularJS app to Angular using micro frontends?

You can:

- Run the AngularJS app as a "legacy" micro frontend in the shell (as a web component, in an iframe or with single-spa), and build new features as Angular remotes.
- Move one route at a time from AngularJS to a new Angular remote.
- Share login and navigation through the shell.

This avoids a big rewrite. Angular's `@angular/upgrade` (ngUpgrade) is another option when both must live in the same app.

## 282: How do you split an existing Angular monolith into micro frontends?

1. Find clear business areas in the existing code, ideally already lazy-loaded features.
2. Clean up imports between those features so they don't depend on each other.
3. Move shared code into libraries.
4. Turn the app into the shell and move one feature into a remote.
5. Load that feature with `loadRemoteModule` instead of a local lazy route.
6. Repeat for other features when it makes sense.

A monorepo with Nx or Sheriff boundaries makes steps 2 and 3 easier.

## 283: What is a "modular monolith" and how does it compare?

A modular monolith is one app and one deployment, but the code is split into clear modules with strict boundaries. In Angular this means lazy-loaded feature areas, libraries and enforced import rules.

It gives you most of the code organization benefits of micro frontends without the runtime complexity. Many teams should start here and only move to micro frontends when independent deployment is really needed.

## 284: How do you decide between a modular monolith and micro frontends?

Ask:

- Do several teams need to deploy on their own schedule?
- Do teams block each other often in the same code base?
- Is the build too slow even with caching?
- Do parts need different tech or release cycles?

If the answers are mostly no, a modular monolith is simpler. Micro frontends solve team and deployment problems, not code quality problems.

## 285: What is the "distributed monolith" anti-pattern?

It's when you split an app into micro frontends, but they're still so tied together that you must deploy them together and change them together. You get the complexity of many apps with none of the independence.

Signs: shared global state everywhere, lots of cross-remote imports, and releases that always need several teams.

## 286: What other anti-patterns are common with micro frontends?

- Too many tiny micro frontends.
- Splitting by technical layer instead of business area.
- A shell full of business logic.
- Different Angular versions with no plan.
- No design system, so the UI looks inconsistent.
- Remotes importing each other's code directly.
- No error handling when a remote fails to load.

## 287: How do you show a "not found" page for unknown routes under a remote?

Add a wildcard route at the end of the remote's routes:

```ts
export const routes: Routes = [
  { path: "", component: OrdersListComponent },
  { path: ":id", component: OrderDetailsComponent },
  { path: "**", component: OrdersNotFoundComponent },
];
```

And keep a top-level `**` route in the shell for URLs that don't match any remote.

## 288: How do you handle analytics tracking across micro frontends?

Set up analytics once in the shell, for example tracking page views on `NavigationEnd`. Give remotes a small shared tracking service (or event) for custom events:

```ts
inject(Analytics).track("order_submitted", { orderId });
```

This avoids every remote loading its own analytics script and makes sure events use the same names and format.

## 289: How do you check that a remote follows accessibility rules?

Each team runs accessibility checks in its own pipeline (for example axe-core in component or end-to-end tests). The design system should already be accessible, so using its components helps a lot.

The shell team should also test full pages, because focus handling and landmarks (`main`, `nav`) depend on how shell and remotes fit together.

## 290: How should focus be handled when navigating between micro frontends?

After a route change, move focus to the main content or its heading, so screen reader and keyboard users know the page changed. The shell can do this on `NavigationEnd` for every remote:

```ts
router.events.pipe(filter((e) => e instanceof NavigationEnd)).subscribe(() => {
  document.querySelector<HTMLElement>("main h1")?.focus();
});
```

The heading needs `tabindex="-1"` to be focusable.

## 291: How do you keep the browser tab title and meta tags correct with remotes?

Use route `title` for titles and the `Meta` service in each remote's page component for meta tags. The shell's `TitleStrategy` makes titles consistent.

Since this is all client-side, search engines only see it if they run JavaScript, unless you use SSR or prerendering.

## 292: How do you handle a remote that needs a library the shell doesn't have?

That's fine. If the library is only in the remote's `package.json`, the remote bundles or shares it on its own, and it's loaded when the remote loads. The shell doesn't need it.

Only libraries that several micro frontends use and need as one instance must be agreed on across teams.

## 293: What happens if two remotes share a library but the shell doesn't use it?

Shared packages can be provided by any app, not just the host. If two remotes both list the library as shared and versions fit, the one that loads first provides it and the second reuses it.

With Native Federation, the host decides the import map at startup based on all remotes' metadata, so the shared package still ends up loaded once.

## 294: What is the order of loading in a Native Federation app?

1. Browser loads the shell's `index.html` and `main.js`.
2. `initFederation` loads the manifest and each remote's `remoteEntry.json`.
3. Federation writes the import map for shared packages.
4. `bootstrap.ts` is imported, Angular (from the import map) loads and the shell starts.
5. When the user navigates to a remote route, `loadRemoteModule` imports the remote's exposed file, and the browser fetches only the chunks it needs.

## 295: How can you reduce the number of remoteEntry.json requests at startup?

Since the host loads every remote's `remoteEntry.json` during `initFederation`, many remotes mean many small requests at startup. Ways to reduce this:

- Use HTTP/2 or HTTP/3 so the requests run in parallel.
- Keep the files small and served from a fast CDN.
- Only list remotes the user can actually access (for example based on role) in the manifest.
- Keep the number of remotes reasonable.

## 296: How do you load remotes only for users who have access?

Build the manifest per user, for example from an API that checks roles:

```ts
const remotes = await fetch("/api/my-remotes", { credentials: "include" }).then(
  (r) => r.json(),
);
await initFederation(remotes);
```

Users without access to "admin" don't even see the admin remote's URL. This also improves startup time. The back-end must still protect admin APIs, since hiding the UI is not security.

## 297: What should the shell do while initFederation is running?

The user sees nothing until Angular starts, so keep `initFederation` fast. You can put a simple loading indicator directly in `index.html`:

```html
<app-root>
  <div class="app-loading">Loading...</div>
</app-root>
```

Angular replaces the content of `<app-root>` when it starts, so the loader disappears on its own.

## 298: How do you share a component that wraps a remote in several places of the shell?

Create a generic component that takes the remote name and exposed module as inputs, loads it, and renders it with `NgComponentOutlet`. Use it anywhere:

```html
<app-remote-slot remote="cart" module="./MiniCart" />
<app-remote-slot remote="recommendations" module="./Carousel" />
```

Put loading and error states inside this component so every slot behaves the same.

## 299: How do you use @defer with remote widgets?

`@defer` can delay rendering of a slot until it's visible or the browser is idle. If the slot component loads a remote, the remote is only fetched then:

```html
@defer (on viewport) {
<app-remote-slot remote="recommendations" module="./Carousel" />
} @placeholder {
<div class="carousel-placeholder"></div>
}
```

The deferred component itself must be a standalone component that's not referenced elsewhere in the eager part of the template.

## 300: What questions would you ask before starting a micro frontend project?

- How many teams will work on the front-end, and how are they organized?
- Do they need to deploy independently?
- Will all micro frontends use Angular and the same version?
- Who owns the shell, the design system and the shared tooling?
- What are the performance and SEO requirements?
- How will we test, deploy, roll back and monitor each part?

The answers decide whether micro frontends are worth it and which approach fits.

# Advanced Questions (301-450)

## 301: Why exactly does having two copies of @angular/core break an app?

Angular keeps important things in module-level variables inside `@angular/core`: the current injection context, the platform, internal tokens, the change detection scheduler and so on. Two copies means two separate sets of those variables.

So a component compiled against copy A, rendered by copy B, can fail with errors like "NG0203: inject() must be called from an injection context" or "No provider for X", even though the provider exists. `InjectionToken`s are also compared by object identity, so a token from copy A is a different object than the "same" token from copy B.

## 302: What is NG0203 and why does it often show up in micro frontend setups?

NG0203 means `inject()` was called outside an injection context. In normal apps it happens when you call `inject()` in a method or callback.

In micro frontends it often means there are two Angular copies on the page: the remote's code calls `inject()` from its own copy of `@angular/core`, which has no current injection context because the shell's copy is running the app. Check that `@angular/core` and the other Angular packages are shared as singletons and that the versions match.

## 303: How does Native Federation decide which version of a shared package wins?

At startup it collects every shared package's version from the host and all remotes. For singletons, it tries to find one version that satisfies everyone's `requiredVersion`, and usually picks the highest such version. If the host provides a version that fits, that's commonly used.

If no version fits everyone and `strictVersion` is on, loading the remote that doesn't fit throws. Without `strictVersion` it warns and uses the chosen version anyway. The exact rules can change between versions, so check the docs and test with mismatched versions on purpose.

## 304: Why does Native Federation use import maps instead of a custom loader?

Import maps are a browser standard, so the browser itself resolves bare imports like `@angular/core` to a URL and loads ES modules natively. No custom runtime is needed to find chunks, which keeps the runtime small and works with any tool that outputs ES modules.

It also means Native Federation doesn't depend on webpack's internals, which made it possible to support Angular's esbuild builder.

## 305: What limitations do import maps have that affect Native Federation?

- A page can only add import maps before the first module that uses them is loaded, so the import map must be ready before Angular starts. That's why `initFederation` runs first.
- Older browsers didn't support multiple import maps or dynamic import maps, which is why Native Federation used `es-module-shims` as a polyfill in the past.
- Import maps map names to URLs, but they don't do version negotiation themselves. Native Federation does that before writing the map.

## 306: What is es-module-shims?

`es-module-shims` is a small library that polyfills import maps and some newer ES module features in browsers that lack them. Native Federation used it to support browsers without native import map support and to allow changing import maps at runtime.

All modern browsers support import maps now, but you'll still see `es-module-shims` in older setups and in some features, like adding remotes after startup.

## 307: How does Native Federation make a shared package available to a remote built separately?

Each project builds its shared packages into its own output folder. When the host starts, it picks one version for each shared package and points the import map to that file, which may live on the host's server or on a remote's server.

The remote's own code just does `import '@angular/core'`. Because the import map is global for the page, the remote ends up using the file the host chose. That's why remotes built months apart can still use the same Angular instance, as long as versions fit.

## 308: How does webpack Module Federation share dependencies internally?

Each container (host or remote) registers its shared modules in a "share scope", a global object keyed by package name and version. When code imports a shared package, the runtime looks into the share scope, picks a version that fits the rules and loads that module's chunk.

This happens through webpack's own runtime functions (`__webpack_init_sharing__`, `container.init`, `container.get`), not through browser import maps.

## 309: What are `__webpack_init_sharing__` and `__webpack_share_scopes__`?

They are webpack Module Federation runtime internals. `__webpack_init_sharing__('default')` fills the default share scope with the host's shared modules, and `__webpack_share_scopes__.default` is the object that holds them. Loading a remote manually used to look like:

```js
await __webpack_init_sharing__("default");
const container = window.mfe1;
await container.init(__webpack_share_scopes__.default);
const factory = await container.get("./Component");
const module = factory();
```

The `loadRemoteModule` helper does this for you. You normally only see these names when debugging.

## 310: How would you build a simplified loadRemoteModule for Native Federation by hand?

The core idea is small:

```ts
async function loadRemote(remoteEntryUrl: string, exposed: string) {
  const info = await fetch(remoteEntryUrl).then((r) => r.json());
  const entry = info.exposes.find((e: { key: string }) => e.key === exposed);
  const base = remoteEntryUrl.substring(0, remoteEntryUrl.lastIndexOf("/") + 1);
  return import(/* @vite-ignore */ base + entry.outFileName);
}
```

The real library also builds the import map for shared packages and remembers loaded remotes. Being able to explain this shows you understand that, under the hood, it's just JSON plus a dynamic `import()`.

## 311: Why does the remote's exposed code run against the host's import map instead of its own?

A page has one module graph and import maps are global for the document. When a remote's ES module does `import { Component } from '@angular/core'`, the browser resolves the bare name with the page's import map, which federation set up during startup.

So a remote never "brings" its own Angular unless the import map points to it. That's what makes sharing work, and also why everything depends on the import map being right before anything loads.

## 312: How does Angular's esbuild builder output affect micro frontends?

The esbuild builder outputs ES modules with code splitting and content hashes, and doesn't have webpack's runtime. That's good for federation based on browser standards, but it means webpack-specific tricks (like `__webpack_public_path__` or the webpack share scope) don't exist.

Native Federation adds its own build step that bundles shared packages separately and writes metadata, then lets the normal Angular builder do the rest.

## 313: What happens to tree shaking when you share a package?

A shared package is bundled as a whole entry point, separately from your app, so the build can't tree shake unused exports based on your app's imports. With `shareAll`, every package and entry point is shared, which can add code you never use.

That's the trade-off for sharing one copy. Mitigations: `skip` unused entry points, enable `ignoreUnusedDeps`, and don't share big libraries that only one micro frontend uses.

## 314: How do shared packages affect initial load performance?

Each shared package is a separate file, so the browser makes more requests than with one bundled file. With HTTP/2 or HTTP/3 this is less of a problem, but many small files still add some overhead and can delay startup.

Measure in the Network tab. If startup is slow, look at how many shared files load before the first render and reduce what's shared or what's imported at startup.

## 315: How do you avoid a waterfall of requests when loading a remote?

A waterfall happens when the browser finds out about files one at a time: `remoteEntry.json`, then the exposed module, then its imports, then their imports. Ways to reduce it:

- Preload `remoteEntry.json` early or include remote metadata in the manifest response.
- Add `<link rel="modulepreload">` for chunks you know will be needed.
- Preload remotes on hover or when idle.
- Keep the exposed module's import tree shallow.

## 316: How do you use modulepreload to speed up a remote?

`modulepreload` tells the browser to download and parse an ES module early:

```ts
function preloadModule(url: string) {
  const link = document.createElement("link");
  link.rel = "modulepreload";
  link.href = url;
  document.head.appendChild(link);
}
```

You can call it for a remote's main exposed file once you know its URL from `remoteEntry.json`, before the user navigates. The browser then has it ready when `import()` runs.

## 317: How would you design caching for a micro frontend system?

- Hashed JS and CSS files: `Cache-Control: public, max-age=31536000, immutable`.
- `remoteEntry.json`, the manifest and `index.html`: `no-cache` (or a very short max-age) so new deployments show up right away.
- Shared package files are hashed too, so they can be cached long.
- Use a CDN in front of everything and invalidate only the non-hashed files on deploy.

This gives fast repeat visits and still makes new versions visible immediately.

## 318: What problem happens if a user has the app open during a remote deployment?

The user has old metadata in memory. When they navigate to that remote for the first time after the deployment, the shell may already have the old `remoteEntry.json` data and request old chunk files. If those were deleted, the load fails with a 404 or a "failed to fetch dynamically imported module" error.

Fixes: keep old files for a while, catch load errors and offer a reload, or detect new versions and ask the user to refresh.

## 319: How do you detect that a new version of a remote is available while the app is open?

Poll the remote's `remoteEntry.json` (or a small `version.json`) every few minutes and compare a version or hash with the one loaded at startup:

```ts
setInterval(
  async () => {
    const res = await fetch("/mfe/cart/version.json", { cache: "no-store" });
    const { version } = await res.json();
    if (version !== loadedVersion) showReloadBanner();
  },
  5 * 60 * 1000,
);
```

Show a "new version available, reload" banner instead of reloading automatically, so users don't lose work.

## 320: How do you handle "Failed to fetch dynamically imported module" errors?

This error means a dynamic `import()` failed, often because of a deployment (old chunk deleted), a network problem or a CORS issue. Handle it at the route loader or in a global error handler:

```ts
export class ChunkErrorHandler implements ErrorHandler {
  handleError(error: unknown) {
    const msg = String((error as Error)?.message ?? error);
    if (msg.includes("Failed to fetch dynamically imported module")) {
      if (confirm("A new version is available. Reload now?")) location.reload();
      return;
    }
    console.error(error);
  }
}
```

Also log these errors so you notice deployment problems.

## 321: What is a Service Worker and how can it interfere with micro frontends?

A Service Worker can cache files and serve them offline. Angular has `@angular/service-worker`. With micro frontends, a Service Worker in the shell may cache `remoteEntry.json` or remote chunks too aggressively, so users keep getting old remotes after a deployment.

If you use one, configure it to fetch metadata files from the network first, or exclude remote URLs from its caching rules, and test deployments with it active.

## 322: How do you guarantee one Angular platform when using Angular Elements micro frontends?

Each Angular Elements bundle normally calls `createApplication`, which creates an application and, if needed, a platform. If several element bundles each include their own copy of Angular, you get several platforms and several Angular copies on the page.

To keep one platform, load all elements through federation with Angular shared as a singleton. Then `createApplication` reuses the existing platform, and only the application injectors differ.

## 323: What are the real costs of running several Angular versions on one page?

- Each version adds roughly the size of Angular core, common, router and more to the download.
- Each copy has its own change detection and, if used, its own Zone.js patching, which can conflict.
- Services can't be shared between versions.
- Global things like `customElements` names and global styles can clash.
- Debugging is much harder.

It can work for a short migration, but it shouldn't be the long-term design.

## 324: Why is Zone.js a problem when mixing Angular apps on one page?

Zone.js patches browser APIs like `setTimeout`, `Promise` and event listeners globally. If two Angular apps each load their own Zone.js, the second load can complain or patch on top of the first, and change detection may run in the wrong zone or not at all.

Zoneless Angular avoids this problem. If you still use Zone.js, load it only once, in the shell, and make sure remotes don't include it in their polyfills when running inside the shell.

## 325: How does zoneless change detection help micro frontends?

With zoneless Angular (default for new apps since Angular 21, via `provideZonelessChangeDetection()` in older versions), change detection is triggered by signals, `markForCheck`, events in templates and similar, not by Zone.js patching every async API.

For micro frontends this removes a global patching layer that could conflict between apps, makes it easier to embed Angular remotes in non-Angular hosts, and lowers the runtime cost. All apps on the page should still agree on the change detection mode, since a remote that relies on Zone.js won't update correctly in a zoneless shell.

## 326: What problem happens when a Zone.js remote runs in a zoneless shell?

The remote's code may update plain class fields after HTTP calls or timers and expect Zone.js to trigger change detection. In a zoneless shell nothing triggers it, so the UI doesn't update until something else causes a refresh.

The fix is to make the remote zoneless-ready: use signals or `markForCheck`, `OnPush`, and `async` pipes, so it works in both modes. Test the remote inside the real shell, not only standalone.

## 327: How do you design a micro frontend system so that teams can deploy on their own but Angular upgrades stay manageable?

- Share Angular as a strict singleton and keep one major version across all apps.
- Plan majors as a coordinated, time-boxed upgrade, ideally in a monorepo where one PR updates all.
- Allow minor and patch differences with `^` ranges and `requiredVersion: 'auto'`.
- Run a CI check that blocks deployments with an incompatible Angular version.
- Upgrade the shell last for minors, or first for majors, depending on which side offers the shared version.

## 328: Why might you want the shell to own the versions of shared packages?

If the shell always provides the shared packages, then remotes have a clear target: "match the shell's versions". It gives one place to manage versions and makes behavior predictable, since the version doesn't depend on which remote loaded first.

The downside is that the shell must be updated for any shared package change. Many teams accept this because shared packages change rarely.

## 329: How would you enforce compatible versions at deploy time?

Add a CI step in each remote's pipeline that downloads the current production shell's `remoteEntry.json` (or a version list) and compares the remote's shared package versions against it:

```ts
const shell = await fetch("https://app.example.com/remoteEntry.json").then(
  (r) => r.json(),
);
const remote = JSON.parse(
  fs.readFileSync("dist/cart/browser/remoteEntry.json", "utf8"),
);
// compare remote.shared[*].requiredVersion with shell.shared[*].version using semver.satisfies
```

If a singleton doesn't fit, fail the build. This catches version problems before users see them.

## 330: How do you share a library that has secondary entry points with different usage per remote?

List the secondary entry points you need, or use `shareAll` with `skip` for the rest. Each secondary entry point is shared as its own module, so `@angular/common/http` can be shared even if one remote never imports it.

For libraries with dozens of entry points (like some UI kits), enable `ignoreUnusedDeps` or skip what you don't use, otherwise every build bundles all of them.

## 331: What is the problem with sharing a library that depends on a non-shared library?

If library A is shared but its dependency B is not, A's shared bundle includes its own copy of B. If your app also imports B directly, your app gets a second copy of B. If B has state, A and your app now see different state.

Share dependencies that hold state together with the libraries that use them, or don't share either.

## 332: How do you share a package with a custom entry point or non-standard format?

Use `packageInfo` in the shared config to tell Native Federation the entry file, version and whether it's ESM:

```js
shared: {
  ...shareAll({ singleton: true, strictVersion: true, requiredVersion: 'auto' }),
  'legacy-lib': {
    singleton: true,
    strictVersion: true,
    requiredVersion: 'auto',
    packageInfo: {
      entryPoint: '/path/to/node_modules/legacy-lib/dist/index.js',
      version: '2.3.1',
      esm: false,
    },
  },
},
```

This is for packages whose `package.json` doesn't give enough info for automatic detection.

## 333: How do you handle CommonJS packages in a Native Federation setup?

esbuild can convert many CommonJS packages to ESM when bundling them, so they often work as shared packages. Problems appear with packages using dynamic `require`, Node globals or side effects at import time.

If a CommonJS package doesn't convert well, don't share it: add it to `skip` so it's bundled normally into each app that uses it. Prefer ESM alternatives when you can.

## 334: How would you share code between micro frontends built with different Angular major versions?

You can't share Angular-dependent code (components, services that use Angular DI) across majors. You can share:

- Plain TypeScript or JavaScript utilities with no Angular dependency.
- Types and contracts.
- Web components built with a framework-neutral tool (or vanilla JS).
- CSS and design tokens.

Design your shared libraries with this split in mind if you expect version differences.

## 335: How would you design a framework-neutral design system for mixed micro frontends?

Build the core components as standard web components (for example with Lit or Stencil) and ship design tokens as CSS variables. Then add thin wrappers for Angular (and other frameworks) that give typed inputs, forms integration and nicer APIs.

This way, Angular, React and legacy apps can all use the same components, and the core doesn't depend on any framework version.

## 336: How do you make a web component work with Angular forms?

Angular forms need a `ControlValueAccessor` to talk to the element. Create a small directive that maps the element's value property and events:

```ts
@Directive({
  selector:
    "ds-input[formControlName], ds-input[formControl], ds-input[ngModel]",
  host: { "(input)": "onChange($event.target.value)", "(blur)": "onTouched()" },
  providers: [
    {
      provide: NG_VALUE_ACCESSOR,
      useExisting: DsInputValueAccessor,
      multi: true,
    },
  ],
})
export class DsInputValueAccessor implements ControlValueAccessor {
  private el = inject(ElementRef<HTMLElement & { value: string }>);
  onChange: (v: string) => void = () => {};
  onTouched: () => void = () => {};

  writeValue(v: string) {
    this.el.nativeElement.value = v ?? "";
  }
  registerOnChange(fn: (v: string) => void) {
    this.onChange = fn;
  }
  registerOnTouched(fn: () => void) {
    this.onTouched = fn;
  }
}
```

## 337: How does Angular Elements handle change detection inside custom elements?

`createCustomElement` creates a component strategy that creates the component when the element connects to the DOM, sets inputs from properties and attributes, and runs change detection when inputs change. Outputs are turned into DOM events.

With zoneless Angular, input changes still schedule change detection, but internal async work should use signals or `markForCheck` so the view updates.

## 338: What happens when an Angular custom element is removed from the DOM?

When the element is disconnected, Angular Elements schedules the component's destruction (after a short delay, so moving the element in the DOM doesn't destroy it). Then the component's `ngOnDestroy` and `DestroyRef` callbacks run.

If you add it back after it was destroyed, a new component instance is created and the old state is gone.

## 339: How do you avoid defining the same custom element name twice?

`customElements.define` throws if the name is already used. In micro frontends, this happens if a remote is loaded twice or two remotes bundle the same element. Guard it:

```ts
if (!customElements.get("cart-widget")) {
  customElements.define("cart-widget", element);
}
```

Also prefix element names with the team or micro frontend name to avoid clashes between teams.

## 340: What are Scoped Custom Element Registries and why are they interesting for micro frontends?

Normally there's one global `customElements` registry per page, so names must be unique across all micro frontends. Scoped Custom Element Registries is a newer web standard that lets a shadow root have its own registry, so two micro frontends can use different versions of `<ds-button>` without conflict.

Browser support is still limited, so check it before relying on it. It's useful to mention when discussing how to isolate web component micro frontends.

## 341: How would you embed an Angular micro frontend into a React host?

Package the Angular feature as a custom element with Angular Elements (or expose it through federation as a module that registers the element). In React, load the script and use the tag:

```tsx
function OrdersWidget({ userId }: { userId: string }) {
  return <orders-widget user-id={userId}></orders-widget>;
}
```

React 19 passes properties to custom elements and supports custom events better than older versions. For older React, set properties and add event listeners through a `ref`.

## 342: How do you expose a mount/unmount API instead of a custom element?

Expose functions that bootstrap and destroy the app on a given element:

```ts
import { createApplication } from "@angular/platform-browser";
import { createComponent } from "@angular/core";

export async function mount(host: HTMLElement) {
  const app = await createApplication({ providers: [] });
  const ref = createComponent(OrdersComponent, {
    environmentInjector: app.injector,
    hostElement: host,
  });
  app.attachView(ref.hostView);
  return () => {
    ref.destroy();
    app.destroy();
  };
}
```

The host calls `mount(el)` and later the returned function. This is framework-neutral and gives the host full control over the lifecycle.

## 343: What is the trade-off between a mount function and a custom element as a remote's API?

A custom element is declarative: the host just writes `<orders-widget>`, and the browser handles creation and removal. It works in any HTML. But inputs are attributes or properties, and data types are loose.

A mount function is explicit: the host controls exactly when the app starts and stops and can pass typed options. It needs a bit of glue code in the host. Many teams use custom elements for simple widgets and mount functions for whole pages.

## 344: How do you keep memory from leaking when a remote is mounted and unmounted many times?

- Destroy the Angular application (`appRef.destroy()`) or component on unmount.
- Remove global listeners, intervals and `BroadcastChannel`s with `DestroyRef`.
- Don't keep references to the remote's components in shell services.
- Avoid module-level caches that grow forever.
- Test with the DevTools Memory tab: mount and unmount many times and check that detached DOM nodes and heap size don't keep growing.

## 345: How do you isolate a remote's errors so they don't crash the shell?

- Catch load errors in route loaders and show a fallback.
- Use a global `ErrorHandler` that logs errors with the remote's name but doesn't stop the app.
- For dynamically created remote components, wrap the creation in try/catch.
- For full isolation of untrusted or unstable parts, use an iframe.

Angular doesn't have React-style error boundaries, so you need these patterns to keep one remote's failure local.

## 346: How would you build an "error boundary" component for remote widgets in Angular?

Load and create the component inside try/catch, and show a fallback on failure:

```ts
@Component({
  selector: "app-safe-remote",
  template: `
    @if (failed()) {
      <p class="remote-error">This part is not available right now.</p>
    }
    <ng-container #slot />
  `,
})
export class SafeRemoteComponent {
  remote = input.required<string>();
  module = input.required<string>();
  exportName = input.required<string>();
  failed = signal(false);
  slot = viewChild.required("slot", { read: ViewContainerRef });

  constructor() {
    afterNextRender(async () => {
      try {
        const m = await loadRemoteModule(this.remote(), this.module());
        this.slot().createComponent(m[this.exportName()]);
      } catch (err) {
        console.error(err);
        this.failed.set(true);
      }
    });
  }
}
```

It catches load and creation errors. Errors later during the remote's rendering still go to the global `ErrorHandler`.

## 347: How do you secure a micro frontend system against loading malicious code?

Remote code runs with the same rights as the shell, so a compromised remote can do anything. Protect against it by:

- Loading remotes only from trusted, fixed origins you control.
- Not allowing users to pass remote URLs through query strings in production.
- Using a strict Content Security Policy for `script-src`.
- Protecting the manifest and deployment pipelines (access control, signed artifacts).
- Using Subresource Integrity where your setup supports it.

## 348: How does Content Security Policy (CSP) work with micro frontends?

CSP tells the browser which origins can provide scripts, styles, images and so on. For micro frontends, `script-src` must include every origin that serves remote code, and `connect-src` must include the origins for `remoteEntry.json` and APIs:

```text
Content-Security-Policy: script-src 'self' https://cdn.example.com; connect-src 'self' https://cdn.example.com https://api.example.com
```

Import maps are inline scripts, so with a strict CSP you may need a nonce for them. Angular supports CSP nonces through `ngCspNonce` or the `CSP_NONCE` token.

## 349: Why is Subresource Integrity (SRI) hard to use with runtime-loaded remotes?

SRI checks that a downloaded file matches a known hash. But with micro frontends, the whole point is that the remote can change without the shell rebuilding, so the shell doesn't know the hash in advance.

You could put hashes into the manifest at deploy time and check them, but it adds complexity. Most teams rely on trusted origins, CSP and secure pipelines instead. Angular's build has a `subresourceIntegrity` option for the app's own files.

## 350: What are the XSS risks specific to micro frontends?

- One remote with an XSS bug exposes the whole app, since all remotes share the same page, cookies and storage.
- Global event buses may pass untrusted data that another team renders without care.
- Web component attributes can carry untrusted HTML if a team uses `innerHTML`.

Angular's template sanitization helps, but every team must follow the same rules: no `bypassSecurityTrust...` without review, and treat data from other micro frontends as untrusted.

## 351: How should authentication tokens be stored in a micro frontend system?

Prefer HTTP-only, secure, `SameSite` cookies set by the back-end (often through a BFF). JavaScript can't read them, so an XSS bug in any remote can't steal the token directly.

If you must use tokens in JavaScript (for example for third-party APIs), keep them in memory in the shared auth service, not in `localStorage`, and keep them short-lived. Remember that every remote's code can reach that memory, so all remotes must be trusted.

## 352: How do you implement single sign-on (SSO) across micro frontends?

The shell handles the OIDC or SAML flow once, through a shared library like `angular-auth-oidc-client` or a BFF. All micro frontends then use the same session:

- With a BFF and cookies, the browser sends the cookie to all APIs on the same domain.
- With tokens, the shared auth service gives remotes the access token.

Remotes should never start their own login flows. If the session expires, the shell handles the redirect to the login page.

## 353: What is the "BFF pattern for auth" and why is it recommended for SPAs today?

In this pattern, the browser never sees the access tokens. A small back-end (the BFF) does the OAuth flow, keeps the tokens on the server and gives the browser a secure HTTP-only session cookie. API calls go through the BFF, which adds the token.

It's recommended because it removes token theft through XSS. For micro frontends it also simplifies things: all remotes just call `/api/...` with the cookie, no token handling in JavaScript.

## 354: How would you design permissions so remotes don't need shell changes for new rules?

- The back-end returns a list of permission strings for the user (`orders:read`, `orders:edit`).
- The shell loads them once and exposes them through a shared service.
- Remotes define and check their own permission names in their own routes and components.

The shell never needs to know what `orders:edit` means. New rules only need back-end and remote changes.

## 355: How do you make sure one remote can't read another remote's data in the browser?

You can't fully, as long as they run in the same page. All JavaScript on a page shares the same global objects, storage and cookies. Angular's DI and encapsulation are for code organization, not for security.

If you need real isolation between parts (for example third-party or untrusted content), use an iframe with a different origin and the `sandbox` attribute, and talk to it through `postMessage` with origin checks.

## 356: How do you communicate safely with an iframe micro frontend?

Use `postMessage` with explicit origins on both sides:

```ts
// parent
iframe.contentWindow!.postMessage(
  { type: "init", userId: 42 },
  "https://legacy.example.com",
);

window.addEventListener("message", (e) => {
  if (e.origin !== "https://legacy.example.com") return;
  if (e.data?.type === "resize") iframe.style.height = `${e.data.height}px`;
});
```

Never use `'*'` as the target origin for sensitive data, always check `event.origin`, and validate the message shape before using it.

## 357: How do you design the shell for high availability?

- Keep the shell small and stable, with few dependencies on remotes at startup.
- Don't let one failed `remoteEntry.json` stop the shell from booting.
- Serve the shell and manifest from a CDN with high uptime.
- Have fallbacks for every remote slot.
- Monitor remote load failures and alert the owning team.

The shell is a single point of failure, so it deserves extra care.

## 358: How would you make initFederation resilient to a missing remote?

Load the manifest yourself, check each remote and only pass the reachable ones:

```ts
const manifest: Record<string, string> = await fetch(
  "/assets/federation.manifest.json",
).then((r) => r.json());

const checks = await Promise.allSettled(
  Object.entries(manifest).map(async ([name, url]) => {
    const res = await fetch(url, { method: "HEAD" });
    if (!res.ok) throw new Error(name);
    return [name, url] as const;
  }),
);

const available = Object.fromEntries(
  checks
    .filter((c) => c.status === "fulfilled")
    .map((c) => (c as PromiseFulfilledResult<readonly [string, string]>).value),
);

await initFederation(available).catch(console.error);
await import("./bootstrap");
```

Routes for missing remotes then fail at load time and show their fallback, while the rest of the app works. This adds requests at startup, so weigh it against your setup.

## 359: How do you monitor the health of each micro frontend in production?

- Real user monitoring with Web Vitals per route, tagged with the remote name.
- Error tracking with remote name and version tags.
- Metrics on remote load failures and load times.
- Synthetic checks that load each `remoteEntry.json` and key pages regularly.
- Dashboards per team, so each team sees its own part.

## 360: How do you measure how long each remote takes to load?

Wrap `loadRemoteModule` and use the Performance API:

```ts
async function timedLoad<T>(remote: string, module: string): Promise<T> {
  const start = performance.now();
  try {
    return await loadRemoteModule(remote, module);
  } finally {
    const duration = performance.now() - start;
    performance.measure(`remote:${remote}`, { start, duration });
    // send duration to your monitoring service
  }
}
```

Track percentiles (p50, p95), not just averages, because slow networks matter most.

## 361: How do you decide what goes in the shell versus in a remote?

Put something in the shell only if it is:

- needed on every page (layout, navigation),
- truly global (auth session, error handling, analytics setup),
- needed before any remote can load (federation setup, config).

Everything else, especially business logic, goes to a remote. If two remotes need something, put it in a shared library, not in the shell.

## 362: How would you design the navigation menu so teams can add items without changing the shell?

Drive the menu from the remote registry. Each remote's entry includes menu data:

```json
[
  {
    "name": "orders",
    "path": "orders",
    "label": "Orders",
    "icon": "receipt",
    "permission": "orders:read"
  },
  {
    "name": "cart",
    "path": "cart",
    "label": "Cart",
    "icon": "cart",
    "permission": null
  }
]
```

The shell builds routes and menu items from this list and hides items the user doesn't have permission for. A team adds a menu item by updating the registry, not the shell's code.

## 363: How do you let remotes contribute items to shared UI areas like the header?

Use an "extension point" pattern. The shell defines named slots (like `header-actions`), and remotes register components for them through the registry or a shared service:

```ts
@Injectable({ providedIn: "root" })
export class ExtensionRegistry {
  private readonly slots = signal<Record<string, Type<unknown>[]>>({});

  register(slot: string, cmp: Type<unknown>) {
    this.slots.update((s) => ({ ...s, [slot]: [...(s[slot] ?? []), cmp] }));
  }

  get(slot: string) {
    return computed(() => this.slots()[slot] ?? []);
  }
}
```

The shell renders each slot's components with `NgComponentOutlet`. This is like a plugin system.

## 364: How is a plugin architecture different from micro frontends?

A plugin system lets third parties or teams extend a host app through well-defined extension points. Micro frontends split an app into independent parts owned by teams.

They overlap a lot: both use runtime loading and contracts. A plugin system usually has a stricter, smaller API and may load untrusted code, so it needs more isolation. Native Federation can be used for both.

## 365: How do you handle a remote that must be available at startup, before any navigation?

For things like a global header or a chat widget shown on every page, load the remote during app initialization:

```ts
provideAppInitializer(async () => {
  const m = await loadRemoteModule('header', './HeaderComponent').catch(() => null);
  inject(ExtensionRegistry).register('header', m?.HeaderComponent ?? FallbackHeaderComponent);
}),
```

Startup now waits for this remote, so keep it small and always have a fallback.

## 366: What is the impact of micro frontends on SEO?

If the app renders only in the browser, search engines must run JavaScript to see the content. Google does this but with delays and limits; other crawlers may not. Runtime-loaded remotes add more delay.

For public pages where SEO matters, consider SSR, prerendering, or keeping those pages in a simpler setup (for example a separate SSR app) instead of client-side micro frontends.

## 367: How does SSR work with Native Federation?

The server also needs to load remote code. Native Federation's SSR support uses a Node.js side that can resolve shared packages and load remotes on the server, so the shell can render a page that includes remote content, then hydrate in the browser.

It needs extra setup (a server entry, federation init on the server, remotes reachable from the server), and remote and shell must be compatible with server rendering. Read the Native Federation SSR guide for your version before planning on it.

## 368: What problems does SSR add to a micro frontend setup?

- The server must fetch remote code at runtime, so remotes must be reachable from the server and secured properly.
- Caching remote code on the server and picking up new deployments gets tricky.
- Every remote must be SSR-safe (no direct `window` or `document` access at render time).
- Hydration mismatches can come from any remote.
- Debugging spans server and browser.

## 369: How do you make a remote SSR-safe?

- Don't access `window`, `document` or `localStorage` directly at render time. Use `afterNextRender` for browser-only code.
- Inject `DOCUMENT` instead of using the global.
- Check the platform only when needed (`isPlatformBrowser`).
- Avoid random values or dates in templates that differ between server and client.

```ts
constructor() {
  afterNextRender(() => {
    const saved = localStorage.getItem('orders-view');
    if (saved) this.view.set(saved);
  });
}
```

## 370: How does incremental hydration relate to micro frontends?

Incremental hydration lets parts of a server-rendered page stay "dehydrated" until they're needed, using `@defer` with hydrate triggers:

```html
@defer (hydrate on viewport) {
<app-remote-slot remote="reviews" module="./Reviews" />
}
```

For micro frontends this means the remote's JavaScript can wait until the user scrolls to it, even though its HTML is already there. It needs SSR with hydration and is supported by recent Native Federation versions, but test it carefully.

## 371: How would you architect a large e-commerce site with Angular micro frontends?

A possible design:

- **Shell**: layout, header, footer, auth, cart badge slot, federation setup.
- **Remotes by domain**: search and listing, product details, cart and checkout, account, help.
- **Widgets**: mini cart, recommendations, reviews, loaded into product and listing pages.
- **Shared libs**: design system, auth, contracts, analytics.
- **Back-end**: one BFF per domain.

Product and listing pages might use SSR for SEO, while account and checkout can be client-side. Checkout is full-screen and kept very stable with strict contracts.

## 372: How would you architect an internal admin portal with many teams?

- **Shell**: layout, menu built from a registry, SSO, permissions, notifications.
- **One remote per business area** (users, billing, reporting, settings), each with its own routes.
- **Dynamic manifest** from an API that only returns remotes the user can access.
- **Design system** shared as a singleton, with Angular Material or a custom kit.
- **No SSR**, since SEO doesn't matter and everything is behind login.

Teams add new areas by deploying a remote and registering it, without shell changes.

## 373: How would you migrate a big Angular 14 webpack Module Federation system to modern Angular?

1. Upgrade all apps step by step through Angular majors together, keeping webpack Module Federation working (update `@angular-architects/module-federation` with each major).
2. Convert to standalone components and modern APIs along the way (`ng generate @angular/core:standalone`).
3. Once on a recent version, switch to Native Federation and the esbuild builder, one environment at a time, moving all apps together.
4. Remove `ngx-build-plus` and webpack configs.
5. Move to zoneless and signals when the apps are ready.

The key constraint: host and remotes must use the same federation type and a compatible Angular at each step.

## 374: What are the risks of a big-bang migration of all micro frontends at once?

- Many teams change at once, so failures are hard to trace.
- A rollback means rolling back everything.
- Feature work stops for all teams during the migration.
- Testing everything together takes long.

When possible, do incremental steps where each step is small and can be rolled back. Where a coordinated step is needed (like a major Angular version), keep it focused only on the upgrade.

## 375: How do you test version compatibility between shell and remotes automatically?

Run an integration test environment where the latest build of each remote is loaded into the latest shell (and also into the current production shell). Run smoke tests for each remote's main pages.

In each remote's pipeline, load the new remote build into the production shell (for example with a manifest override in a test environment) before deploying. This catches contract and version breaks before production.

## 376: What is consumer-driven contract testing and how would you apply it here?

In consumer-driven contracts, the consumer (the shell) writes down what it expects from the provider (the remote), and the provider runs those expectations in its own pipeline.

For micro frontends, the shell could publish a test like "remote `cart` exposes `./MiniCart` with a component that accepts `size` input". The cart team runs it in CI, so they can't deploy a version that breaks the shell's expectations.

## 377: How do you test a remote's exposed module without the shell?

Write a test that imports the exposed file the same way the shell would use it:

```ts
import { routes } from "./app.routes";

describe("exposed routes", () => {
  it("has the agreed entry route", () => {
    expect(routes.some((r) => r.path === "")).toBe(true);
  });

  it("can render the entry page", async () => {
    TestBed.configureTestingModule({ providers: [provideRouter(routes)] });
    const harness = await RouterTestingHarness.create();
    await harness.navigateByUrl("/");
    expect(harness.routeNativeElement?.textContent).toContain("Orders");
  });
});
```

This checks the public contract without running federation.

## 378: How would you run end-to-end tests against several remote versions?

Use the dynamic manifest. In the test setup, point the shell to a specific version of each remote:

```ts
await page.addInitScript(
  (overrides) => {
    localStorage.setItem("mf-overrides", JSON.stringify(overrides));
  },
  { cart: "https://cdn.example.com/cart/pr-123/remoteEntry.json" },
);

await page.goto("https://staging.example.com");
```

This lets each pull request in a remote run end-to-end tests inside a real shell, with its own preview build.

## 379: How do you create preview environments for pull requests in a remote?

Deploy each PR's build to a unique path, like `/cart/pr-123/`. Then open the shared staging shell with an override that points `cart` to that path. Reviewers and tests can see the change inside the real app, without deploying a whole environment per PR.

This works well because the shell doesn't need to be rebuilt for each PR.

## 380: How do you handle database or API changes that affect several micro frontends?

Treat APIs like contracts too:

- Make API changes backwards compatible first (add fields, don't remove).
- Deploy the back-end change.
- Let each micro frontend move to the new fields on its own schedule.
- Remove old fields only when nobody uses them.

If an API is used by several micro frontends, it probably belongs to one domain, and the owning team should version it.

## 381: How would you handle shared state that must survive a page reload?

Keep it in the place that already survives reloads: the URL, the back-end, or browser storage. For example, the cart lives on the back-end and the shell fetches its count after load. Filter state lives in the URL.

Avoid keeping important cross-micro-frontend state only in memory, since a reload or deployment would lose it.

## 382: How do you avoid race conditions when several remotes load shared data at startup?

Use one owner that loads the data once and exposes the in-progress request:

```ts
@Injectable({ providedIn: "root" })
export class SessionService {
  private readonly http = inject(HttpClient);
  readonly session$ = this.http
    .get<Session>("/api/session")
    .pipe(shareReplay({ bufferSize: 1, refCount: false }));
}
```

All remotes subscribe to the same `session$` and share the one request. With signals, `httpResource` in a root service gives the same effect.

## 383: How do you version the shared event contracts?

- Include a version in the event type or payload (`cart:updated.v2` or `{ v: 2, ... }`).
- Keep sending the old event while consumers move to the new one.
- Only add optional fields to existing events, never remove or rename.
- Keep all event types in the contracts library with a changelog.

## 384: How do you trace a user action across several micro frontends and back-ends?

Use distributed tracing. The shell or a shared HTTP interceptor adds a trace header (like W3C `traceparent`) to API calls, and the back-ends pass it along. Front-end events can be tagged with the same trace id.

Tools like OpenTelemetry have browser SDKs that can do this. Then you can see "button click in cart remote, API call to cart BFF, call to inventory service" as one trace.

## 385: How does OpenTelemetry fit into an Angular micro frontend setup?

Set up the OpenTelemetry Web SDK once in the shell, with automatic instrumentation for fetch and XHR and document load. Remotes use a shared tracer from a library to add their own spans with the remote name as an attribute.

Because the SDK patches global `fetch` and `XMLHttpRequest`, it must only be initialized once, otherwise spans are recorded twice.

## 386: How would you handle a remote that blocks the main thread?

First find it with the Performance panel in DevTools or Long Tasks / Long Animation Frames data from real users, tagged by remote. Then:

- Move heavy work to a Web Worker.
- Break long tasks into smaller chunks (`scheduler.yield()` where supported, or `setTimeout`).
- Lazy load heavy libraries only when needed.
- Set performance budgets and alerts per team.

One remote with long tasks makes the whole page slow, so INP should be tracked per remote.

## 387: How do Web Workers work in a federated remote?

Angular supports workers with `new Worker(new URL('./app.worker', import.meta.url), { type: 'module' })`. The builder bundles the worker as a separate file in the remote's output.

Because `import.meta.url` resolves relative to the remote's own JavaScript file, the worker file is loaded from the remote's server even when the remote runs inside the shell. If the remote is on another origin, check that the worker loads, since workers have stricter same-origin rules.

## 388: How do you handle cross-origin workers in remotes?

Browsers only allow `new Worker(url)` for same-origin URLs. If the remote's files are on a different origin, a common workaround is to create a small same-origin blob that imports the real worker script:

```ts
const workerUrl = new URL("./app.worker.js", import.meta.url).href;
const blob = new Blob([`import '${workerUrl}';`], { type: "text/javascript" });
const worker = new Worker(URL.createObjectURL(blob), { type: "module" });
```

The remote's server still needs CORS headers. Serving everything from one domain avoids this.

## 389: How do you handle the remote's global polyfills?

Polyfills affect global objects, so they should be loaded once by the shell. Remotes shouldn't rely on polyfills from their own `polyfills` option when running inside the shell, since that file isn't loaded there.

Agree on a browser support target for the whole system, and let the shell load whatever polyfills that target needs.

## 390: How do you choose which browsers to support across micro frontends?

Use one shared `.browserslistrc` (or the Angular default) for all apps. If one remote targets older browsers than the others, it may produce code in a different style, and if another targets only new browsers, it may break for users of older ones.

In a monorepo, a single root config keeps it aligned. In a polyrepo, put it in a shared config package.

## 391: How do you handle global configuration changes like a new theme across many remotes?

Use runtime mechanisms that don't need rebuilds:

- CSS variables defined by the shell for colors and spacing.
- A shared settings service that remotes read.
- The design system served as a shared package (so a minor update reaches all remotes at the next load, if versions fit).

If a theme change requires all remotes to rebuild, your theming setup is too tightly bound to build time.

## 392: What is the impact of shared singletons on the ability of remotes to run standalone?

When standalone, the remote provides all its shared packages itself, so it works fine. Problems come from shared _services_ that expect the shell to set them up, like an auth store the shell fills after login.

Remotes should handle the "not set up" case: show a dev login, use a mock user in development, or set up the service themselves when they detect they are running alone.

## 393: How can a remote know whether it's running standalone or inside the shell?

Options:

- Check if it was started through its own `bootstrap.ts` (set a flag there).
- Provide an injection token in the shell (like `IN_SHELL`) and inject it with `{ optional: true }` in the remote.

```ts
export const IN_SHELL = new InjectionToken<boolean>("IN_SHELL");

// shell: providers: [{ provide: IN_SHELL, useValue: true }]
// remote:
const inShell = inject(IN_SHELL, { optional: true }) ?? false;
```

The token must come from a shared library so both sides use the same token object.

## 394: Why must injection tokens used across micro frontends come from a shared library?

An `InjectionToken` is matched by object identity, not by name. If the shell creates `new InjectionToken('CONFIG')` and the remote creates its own `new InjectionToken('CONFIG')`, they're two different tokens, and the remote's `inject()` won't find the shell's value.

Define cross-app tokens once in a library that's shared as a singleton, so both import the exact same object.

## 395: What is the problem with abstract class tokens across micro frontends?

Same as with injection tokens: the class itself is the token. If the shell provides `{ provide: Logger, useClass: ShellLogger }` and the remote injects `Logger` from its own bundled copy of the library, it's a different class object, so DI can't match it.

This is a common surprise when a shared library is accidentally bundled into a remote instead of shared.

## 396: How do you detect that a library is accidentally bundled twice?

- Look at the Network tab: the same library loading from two different URLs.
- Search the remote's build output for the library's code.
- Put a log or a global counter in the library's entry: `(globalThis as any).__myLibLoaded = ((globalThis as any).__myLibLoaded ?? 0) + 1`.
- Check the remote's `remoteEntry.json` to see if the library is in the `shared` list.
- Watch for symptoms: services that don't share state, DI errors, duplicate custom element errors.

## 397: How can you prevent a library from being instantiated twice even if bundled twice?

You can make the library store its singleton on `globalThis` with a well-known key:

```ts
const KEY = Symbol.for("@my-org/event-bus");

export function getEventBus(): EventBus {
  const g = globalThis as any;
  return (g[KEY] ??= new EventBus());
}
```

`Symbol.for` returns the same symbol everywhere on the page, so both copies get the same instance. This works for plain JS objects but not for Angular DI tokens or classes, which still need real sharing.

## 398: How do you share state between Angular and non-Angular micro frontends?

Use something framework-neutral:

- Custom events on `window` for notifications.
- A small store object on `globalThis` (with `Symbol.for`) with a subscribe method.
- The URL and browser storage.
- Web component properties and events.

In Angular, wrap it in a service that converts the store's changes into a signal, so components can use it normally.

## 399: How do you convert a framework-neutral store into an Angular signal?

```ts
interface ExternalStore<T> {
  get(): T;
  subscribe(fn: (v: T) => void): () => void;
}

export function fromExternalStore<T>(store: ExternalStore<T>): Signal<T> {
  const s = signal(store.get());
  const unsubscribe = store.subscribe((v) => s.set(v));
  inject(DestroyRef).onDestroy(unsubscribe);
  return s.asReadonly();
}
```

Call it in an injection context (a constructor or field initializer). Signal updates schedule change detection, so this works in zoneless apps too.

## 400: How would you explain the trade-off between isolation and integration in micro frontends?

More isolation (iframes, separate Angular copies, Shadow DOM) means teams can't break each other and can use different versions, but you pay with bigger downloads, harder communication and a less smooth UX.

More integration (shared Angular, one router, shared services) gives a fast, consistent app with easy communication, but teams must agree on versions and contracts.

Most Angular systems choose strong integration (shared Angular, federation) with a few isolated parts where really needed.

## 401: Scenario: after a remote deployment, users report a blank page on one route. How do you investigate?

1. Open the route and check the console and Network tab for failed requests (404 on chunks, CORS errors, version mismatch errors).
2. Open the remote's `remoteEntry.json` and check that the files it lists exist on the server.
3. Check caching: is an old `remoteEntry.json` cached by the CDN or a Service Worker?
4. Compare shared package versions between the shell and the new remote build.
5. Check that the exposed name and export (`./routes`, `routes`) didn't change.
6. If it's not obvious, roll back the remote to the previous version first, then investigate.

## 402: Scenario: a service from a shared library has different state in the shell and in a remote. What's going on?

Most likely the library is loaded twice, so each side has its own instance. Possible causes:

- The library isn't in the `shared` config of one of the apps (or is in `skip`).
- The versions don't match and the library isn't a singleton, so both versions load.
- The remote imports the library through a different path (a relative path instead of the mapped package name), so the bundler treats it as different code.
- The service is provided in a route or component instead of `providedIn: 'root'`.

Check the Network tab and `remoteEntry.json` to confirm.

## 403: Scenario: the app works locally but a remote fails to load in production with a CORS error. What do you check?

- Does the remote's server (or CDN) send `Access-Control-Allow-Origin` for the shell's origin on `remoteEntry.json` and all JS files?
- Are preflight requests (OPTIONS) handled?
- Is there a redirect (HTTP to HTTPS, or to a login page) that drops the CORS headers?
- Is the CSP blocking the origin, which can look similar in the console?

Locally everything was probably on `localhost`, where dev servers allow CORS by default.

## 404: Scenario: after upgrading Angular in the shell, one remote stopped working. How do you approach it?

The remote is now running on the shell's newer Angular. Check:

- Console errors about version mismatch from `strictVersion`.
- Use of APIs that were removed or changed in the new major.
- Whether the remote's shared range (`^20.0.0`) even accepts the new version (`21.x`). If not, federation may load a second Angular or fail.

The real fix is to upgrade the remote to the same major and redeploy. Plan majors together so this doesn't happen in production.

## 405: Scenario: the shell's initial load got 2 seconds slower after adding a few remotes. Where do you look?

- How many `remoteEntry.json` files are fetched before bootstrap, and how slow they are.
- Whether new shared packages are now loaded at startup.
- Whether a remote is loaded in an app initializer or on the first page instead of lazily.
- Whether preloading strategies started downloading remotes too early and compete with the critical files.
- CDN and cache headers on the new remotes.

Use the Performance panel and Network waterfall to see what's on the critical path.

## 406: Scenario: two teams both want to change the shared design system at the same time. How do you organize this?

- Give the design system a clear owner (often the platform team) who reviews and merges changes.
- Teams contribute through pull requests with a clear contribution guide.
- Use SemVer: new components or options are minor, breaking changes are major and announced in advance.
- Keep breaking changes rare and bundle them, with migration notes or schematics.

The goal is that the design system is shared code with an owner, not code everyone edits freely.

## 407: Scenario: a remote team wants to use React for their new feature. What do you consider?

- Will React add significant size for users of that area?
- How will it look the same as the rest (design system in React too, or web components)?
- How will it talk to Angular parts (events, URL, web component API)?
- Who will support it long-term, and can other teams help?
- Is there a strong reason, or is it just preference?

If it goes ahead, wrap it as a web component or a mount function and load it through federation, keeping the contract small.

## 408: Scenario: users see a flash of unstyled content when a remote loads. How do you fix it?

The remote's styles arrive after its HTML is in the page. Possible fixes:

- Make sure component styles are part of the component (Angular does this by default), not a separate global CSS file loaded later.
- If the remote has a global stylesheet, preload it or load it before rendering the remote.
- Show a placeholder or skeleton until the remote is ready.
- Put shared styles (theme, fonts) in the shell so they're already there.

## 409: Scenario: a remote's global CSS breaks the shell's layout. How do you prevent it in the future?

- Add a lint rule (for example Stylelint) that blocks global element selectors in remotes.
- Require remote global styles to be scoped under a remote-specific class.
- Use the design system's utilities and tokens instead of custom globals.
- Run visual regression tests of the shell with every remote loaded.
- For widgets, consider Shadow DOM.

Fix the immediate issue by scoping the selector and redeploying the remote.

## 410: Scenario: the cart count in the header doesn't update after adding an item in a product remote. How do you debug?

- Is the event or state update actually sent? Log in the product remote.
- Is the header listening to the same event name or the same service instance?
- If it's a shared service, is the library really a singleton (check for duplicate loading)?
- In a zoneless app, does the header use a signal or `markForCheck`, or does it set a plain field in an event listener?
- Was the header created after the event was sent and missed it?

## 411: Scenario: a remote must run in two different shells (for example, customer portal and admin portal). How do you design it?

- Keep the remote free of assumptions about the shell: no direct imports from either shell.
- Define what it needs as injection tokens or inputs in a shared contracts library (current user, API base URL, permissions).
- Each shell provides those tokens.
- Expose routes or components that read the tokens.
- Test the remote with both shells' providers.

This turns the remote into a reusable product, with a clear API to its hosts.

## 412: Scenario: one remote needs a newer version of a shared library than the shell provides. What are your options?

1. Update the shell (and other remotes) to the newer version, if it's backwards compatible. This is usually best.
2. Make the library non-singleton for that remote, so it loads its own version, if the library is stateless.
3. Wait for a coordinated upgrade.
4. If the library is stateful and must be a singleton, the remote can't use a different version safely; the teams have to align.

## 413: Scenario: you need to show an A/B test that swaps one micro frontend for another. How?

Use the manifest or registry. For users in group B, return a different remote (or a different version) for the same name or route:

```ts
const variant = await fetch("/api/experiments/checkout").then((r) => r.json());
const manifest = {
  ...baseManifest,
  checkout: variant === "B" ? CHECKOUT_B_URL : CHECKOUT_A_URL,
};
await initFederation(manifest);
```

Track which variant users got so results can be compared. Both variants must keep the same exposed contract.

## 414: Scenario: a security audit finds that any user can override remote URLs with a query parameter. What do you do?

This allows loading attacker-controlled JavaScript into your app, which is a serious XSS risk. Fix it by:

- Removing the override in production builds.
- If overrides are needed for testing, allow them only in non-production environments, or only for URLs on an allowlist of trusted origins.
- Adding a CSP `script-src` that only allows your own origins, as a second line of defense.

## 415: Scenario: the shell must work offline for field workers. How do micro frontends affect this?

Offline needs every needed file cached. With micro frontends, the Service Worker must cache the shell, the manifest, every remote's `remoteEntry.json`, its chunks and shared packages.

Since remote files are listed in their own metadata, you may need a custom Service Worker strategy that reads each `remoteEntry.json` and pre-caches its files. You also need a clear update flow so users get new versions when they're back online.

## 416: How would you design a versioning strategy for exposed modules?

- Treat each exposed module as a public API with a documented contract.
- Additive changes (new optional inputs, new routes) are fine in place.
- Breaking changes get a new exposed name (`./routes-v2`) while the old one stays for a deprecation period.
- Track which hosts use which exposed names (through logs or the registry), so you know when the old one can go.

## 417: How does the choice between monorepo and polyrepo affect micro frontend independence?

In a monorepo, it's easy to keep versions aligned and change contracts across apps in one PR, but it's also easy to create hidden coupling (imports across apps), and builds may be shared. Independence must be enforced with boundaries and separate deploy pipelines.

In a polyrepo, independence is natural, but alignment needs more process and tooling. Neither is "correct"; it depends on the organization and how much coordination you want.

## 418: How would you set up deployment pipelines in an Nx monorepo so each remote deploys independently?

- Each app has its own `deploy` target.
- CI runs `nx affected -t build test` and then deploys only affected apps.
- Changing a shared library marks all apps using it as affected, so they all rebuild and redeploy (or you choose to deploy them later if the library is shared at runtime).
- Use Nx remote caching so unaffected projects don't rebuild.

```bash
nx affected -t deploy --base=origin/main~1 --head=HEAD
```

## 419: What is the problem with "affected" when a shared library changes in a micro frontend monorepo?

If a shared library changes, every app that uses it is "affected" and will be rebuilt and possibly redeployed, which removes some independence. If the library is shared at runtime, an old remote might run with the new library loaded by the shell anyway.

Teams need a rule: which shared library changes require coordinated redeploys, and which are safe because of SemVer and runtime sharing.

## 420: How do you handle long-lived feature branches across micro frontends?

Avoid them when you can. Use trunk-based development with feature flags instead, so unfinished features are deployed but hidden.

If a feature really spans several remotes, put each remote's part behind the same flag and deploy them independently. Turn the flag on when all parts are deployed.

## 421: How would you set up local development so a developer only runs what they need?

- Run the shell and the remote they're working on locally.
- Point other remotes to a shared dev or staging environment through the manifest.
- Use Nx `--devRemotes` or a manifest override to choose which remotes run locally.
- Keep the remote working standalone with mocks for quick work.

This keeps memory use low and startup fast, even with many remotes.

## 422: How do you share a mock back-end for micro frontend development?

Use a tool like Mock Service Worker (MSW) or a shared mock server. Each team keeps mocks for its own APIs in its own repo or library. The shell can load all mocks in development mode, and each remote can load only its own when running standalone.

Keep the mocks close to the API contracts (for example generated from OpenAPI) so they don't drift.

## 423: How would you generate API clients for micro frontends?

Generate typed clients from each back-end's OpenAPI spec with a generator (like `openapi-generator` or `ng-openapi-gen`). Put each generated client in the owning team's library.

Don't make one giant generated client for all APIs shared by all remotes. That ties every remote to every API change and makes the shared package big.

## 424: How does lazy loading inside a remote work under federation?

A remote's own lazy routes and `@defer` blocks are split into chunks by its own build. When the remote is loaded into the shell, those chunks are fetched from the remote's server when needed, using URLs relative to the remote's files.

So lazy loading inside a remote works the same as in a normal app, and you should use it to keep the remote's exposed entry small.

## 425: What happens if two remotes expose components with the same selector?

Inside Angular templates, standalone components are resolved by their imports, not globally by selector, so two different components with the same selector in different remotes don't clash.

It's different for custom elements (Angular Elements): the browser's `customElements` registry is global, so two elements with the same tag name do clash. Prefix custom element names per team.

## 426: How do you design remotes to be loaded multiple times on the same page?

For widgets that can appear several times (like a product card), make sure:

- No module-level state is used for instance data; keep it in the component.
- Services that hold per-instance state are provided at component level, not root.
- Custom element definitions and global listeners are guarded so they're set up once.
- IDs in templates are unique per instance (for labels and ARIA).

## 427: How do you handle remotes that need different router configurations, like hash routing?

All remotes loaded into the shell use the shell's router settings (`withHashLocation`, `paramsInheritanceStrategy` and so on). A remote can't have its own location strategy in that case.

Agree on router settings across the system. If a legacy app needs hash routing, run it isolated (web component with its own router, or iframe) until it's migrated.

## 428: What would you do if a team needs strong isolation for compliance reasons, like a payment form?

Load that part in an iframe from a separate origin (often provided by the payment provider). It keeps card data out of your page, so other scripts can't read it, and reduces your compliance scope.

Communicate with the iframe through `postMessage` with strict origin checks, and only exchange tokens or status, never raw card data.

## 429: How would you compare Native Federation, webpack Module Federation and Module Federation 2.0 for a new Angular project today?

- **Native Federation**: works with the default Angular esbuild builder, uses web standards, has Angular-friendly schematics. The natural choice for most new Angular projects.
- **webpack Module Federation** (Angular Architects plugin): mature, but needs the webpack builder, which Angular is moving away from. Mainly for existing projects.
- **Module Federation 2.0**: strong runtime features and tooling, good for multi-framework systems on webpack or Rspack, but using it with Angular means leaving the default CLI builder.

Pick based on your build tool and whether you need multi-framework support.

## 430: What would make you choose web components over federation for Angular micro frontends?

- The host is not Angular, or several frameworks need to use the same piece.
- You need to run different Angular major versions on one page for a while.
- You want the micro frontend to be usable in other products or CMS pages through just a script tag.

The cost is weaker integration: separate Angular instances (unless combined with federation), loose typing and more glue code.

## 431: How would you share Angular itself when using Angular Elements micro frontends?

Combine Angular Elements with Native Federation: each micro frontend exposes a file that registers its custom element, Angular is shared as a singleton through federation, and the host loads each file with `loadRemoteModule`. This gives web component interfaces with only one copy of Angular.

Without federation, every Angular Elements bundle includes its own Angular, which is heavy.

## 432: What is "compile-time" versus "runtime" coupling between micro frontends?

Compile-time coupling is when one app imports code or types from another and needs it at build time. Runtime coupling is when apps depend on each other while running: exposed names, events, shared services, URLs.

Some compile-time coupling through shared contracts is good (type safety, no runtime cost). Too much runtime coupling hurts independence because it fails late, in production. The goal is few, explicit dependencies of either kind.

## 433: How do you handle the dependency on the shell's layout in a remote's design?

Remotes shouldn't assume a specific layout width or position. Use responsive layouts based on container size (CSS container queries) instead of viewport size, so a remote looks right whether it's full-width, in a sidebar or in a different shell.

```css
.orders-host {
  container-type: inline-size;
}

@container (min-width: 600px) {
  .orders-list {
    display: grid;
    grid-template-columns: 1fr 1fr;
  }
}
```

## 434: How do you test a remote's visual appearance across shells and themes?

Use visual regression tests (Playwright screenshots, Storybook with Chromatic, or similar) for the remote's main pages and widgets, rendered with the real design system and each theme.

Run them in the remote's pipeline, and run a smaller set in the shell's integration environment to catch layout issues from the combination.

## 435: How do you use Storybook with micro frontends?

Each team keeps a Storybook for its own components and widgets. The design system has its own Storybook too. Storybook's composition feature can combine several Storybooks into one view, which helps teams see what others have built.

Stories for remote widgets should provide the same tokens and services the shell provides, so they look and behave as they do in production.

## 436: What metrics would show that micro frontends are actually helping the organization?

- Deployment frequency per team goes up.
- Lead time from commit to production goes down.
- Fewer cross-team blocked releases.
- Build and test times per project stay low as the system grows.
- Change failure rate and time to restore stay the same or improve.

If these don't improve, the micro frontend setup may be adding cost without benefit.

## 437: What are the hidden costs of micro frontends that teams often underestimate?

- Building and maintaining the platform (shell, pipelines, design system, tooling).
- Coordinating upgrades across teams.
- Debugging problems that span several apps.
- Onboarding: new developers must learn the architecture, not just Angular.
- Keeping UX consistent.
- Running more infrastructure (more buckets, CDN paths, monitoring).

## 438: How would you reverse a micro frontend decision if it isn't working?

Merge remotes back into a modular monolith step by step:

1. Move a remote's code into the shell's repo as a library with clear boundaries.
2. Replace `loadRemoteModule` with a normal lazy `loadChildren` import.
3. Remove the remote's pipeline and deployment.
4. Repeat, keeping the module boundaries so you could split again later.

Because routes and contracts stay the same, users don't notice. Good boundaries make both directions possible.

## 439: How does Angular's dependency injection hierarchy look when a remote is loaded via loadChildren?

The remote's routes become child routes of the shell. If a route has `providers`, the router creates an `EnvironmentInjector` for it, whose parent is the shell's root (or parent route) injector. Components in the remote get element injectors as usual.

So a remote service can be scoped to the remote's routes, while `providedIn: 'root'` services come from the shell's root injector, which is why they're shared across all micro frontends.

## 440: What happens to services provided in a remote's route when the user navigates away?

Route-level environment injectors are kept after the route is first loaded; Angular doesn't destroy them when you navigate away, so services provided there keep their state. That's usually fine, but it means route-provided services act like long-lived singletons for that remote.

If you need state reset when leaving, provide the service at component level instead, or reset it on navigation.

## 441: How would you explain the difference between a remote's environment injector and the shell's root injector in an interview?

The shell's root injector is created at bootstrap with `appConfig.providers` and everything `providedIn: 'root'`. It lives as long as the app.

When the router loads a remote route with `providers`, it creates a child environment injector. Lookups start there and go up to the root. The remote can add or override services for its own part without touching the root, but anything not provided locally comes from the shell.

## 442: How do you override a shell service for one remote only?

Provide a different implementation in the remote's route providers:

```ts
export const routes: Routes = [
  {
    path: "",
    providers: [{ provide: Logger, useClass: OrdersLogger }],
    children: [/* ... */],
  },
];
```

Components in the remote now get `OrdersLogger`, while the rest of the app still uses the shell's `Logger`. The `Logger` token must be the same shared class for this to work.

## 443: How would you load remotes based on a CMS-driven page layout?

The CMS returns a page description with a list of blocks, each mapped to a remote and exposed component:

```json
{
  "blocks": [
    {
      "remote": "marketing",
      "module": "./Hero",
      "inputs": { "title": "Sale" }
    },
    {
      "remote": "catalog",
      "module": "./ProductGrid",
      "inputs": { "category": "shoes" }
    }
  ]
}
```

A page component loops over blocks, loads each with `loadRemoteModule` and renders it with `NgComponentOutlet` and its inputs. Validate the CMS data and only allow known remotes and modules.

## 444: How do you keep a CMS-driven micro frontend page from becoming slow?

- Load only the blocks above the fold first and use `@defer (on viewport)` for the rest.
- Load all block remotes in parallel, not one after another.
- Reserve space for each block to avoid layout shift.
- Cache the page description.
- Set limits on how many different remotes a page can use.

## 445: How would you handle internationalized routes (like /de/orders) with remotes?

Keep the language prefix in the shell's top-level routes and mount remotes under it:

```ts
{
  path: ':lang',
  children: [
    { path: 'orders', loadChildren: () => loadRemoteModule('orders', './routes').then(m => m.routes) },
  ],
}
```

Remotes read `lang` (with `paramsInheritanceStrategy: 'always'` or from a shared language service) and use relative links, so they don't need to know about the prefix.

## 446: What are the effects of micro frontends on accessibility landmarks and headings?

Each remote may add its own `<main>`, `<h1>` or `<nav>`, leading to several main landmarks or broken heading order on one page.

Agree on rules: the shell provides `<header>`, `<nav>` and `<main>`; page-level remotes provide the page's single `<h1>` inside `<main>`; widgets start at a lower heading level or take it as an input. Test whole pages with a screen reader, not just remotes alone.

## 447: How would you approach a performance budget for the whole system, not just per remote?

Define a budget per page type (like "product page: max 300 kB JS compressed, LCP under 2.5s"), not only per app. Then measure what each page actually loads: shell, shared packages, the page remote and widgets.

Assign each team a share of the budget for their parts and check it in CI with Lighthouse or a custom test that loads the page with all real remotes.

## 448: How would you onboard a new team into an existing micro frontend platform?

- Give them a template or generator that creates a working remote with the right config, linting, tests and pipeline.
- Document the contracts: how to expose, how to register, how to use shared services and events.
- Give a sandbox environment where they can register their remote in a real shell.
- Pair them with the platform team for the first deployment.

A good starting template saves weeks and keeps all remotes consistent.

## 449: What would you put in a remote template or generator?

- Native Federation setup with the agreed shared config.
- Standalone routes file exposed as `./routes`.
- Providers function for feature setup.
- Shared libraries already wired (design system, auth, contracts, analytics).
- Lint rules for boundaries and styles.
- Test setup (unit and a contract test for the exposed module).
- CI pipeline with build, test and deploy to the right path.
- A README with the contract and owner info.

## 450: If you had to sum up the key principles of a good Angular micro frontend architecture, what would they be?

- Split by business domain and team, not by technical layer.
- Keep the shell thin and stable.
- Share Angular and other stateful libraries as strict singletons, and keep versions aligned.
- Keep contracts small, typed and versioned.
- Let each team build, test and deploy alone, and roll back quickly.
- Handle failures so one remote can't take down the app.
- Invest in a design system and shared tooling.
- Only use micro frontends when team size and deployment needs justify the cost.
