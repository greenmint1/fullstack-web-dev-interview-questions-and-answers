# React Micro Frontend Interview Questions and Answers

_Last updated: October 28, 2026_

450 interview questions with answers about building micro frontends with React, split into three levels: 150 easy, 150 moderate and 150 advanced.

The answers target React 19 with `createRoot`, React Router 7 and modern build tools. Most examples use Module Federation, either the classic webpack 5 plugin or Module Federation 2.0 (`@module-federation/enhanced`) with webpack, Rspack or Vite (`@module-federation/vite`). single-spa, web components, iframes, build-time packages and Next.js Multi-Zones are also covered, since you will still meet them in real projects.

## Table of Contents

- [Easy Questions (1-150)](#easy-questions-1-150)
- [Moderate Questions (151-300)](#moderate-questions-151-300)
- [Advanced Questions (301-450)](#advanced-questions-301-450)

### Easy Questions (1-150)

- [1: What is a micro frontend?](#1-what-is-a-micro-frontend)
- [2: Why would a company use micro frontends with React?](#2-why-would-a-company-use-micro-frontends-with-react)
- [3: What is a monolithic frontend?](#3-what-is-a-monolithic-frontend)
- [4: What is the difference between a micro frontend and a React component library?](#4-what-is-the-difference-between-a-micro-frontend-and-a-react-component-library)
- [5: What is a host (shell) application?](#5-what-is-a-host-shell-application)
- [6: What is a remote application?](#6-what-is-a-remote-application)
- [7: What does "independent deployment" mean?](#7-what-does-independent-deployment-mean)
- [8: What are the common ways to build micro frontends with React?](#8-what-are-the-common-ways-to-build-micro-frontends-with-react)
- [9: What is Module Federation?](#9-what-is-module-federation)
- [10: What is Module Federation 2.0?](#10-what-is-module-federation-20)
- [11: What is the ModuleFederationPlugin?](#11-what-is-the-modulefederationplugin)
- [12: What does the name option do in Module Federation?](#12-what-does-the-name-option-do-in-module-federation)
- [13: What does the filename option do?](#13-what-does-the-filename-option-do)
- [14: What does the exposes option do?](#14-what-does-the-exposes-option-do)
- [15: What does the remotes option do?](#15-what-does-the-remotes-option-do)
- [16: What does the shared option do?](#16-what-does-the-shared-option-do)
- [17: Why must React be a singleton in a micro frontend setup?](#17-why-must-react-be-a-singleton-in-a-micro-frontend-setup)
- [18: What does singleton: true mean?](#18-what-does-singleton-true-mean)
- [19: What does requiredVersion do?](#19-what-does-requiredversion-do)
- [20: What does strictVersion do?](#20-what-does-strictversion-do)
- [21: What does eager: true do for a shared module?](#21-what-does-eager-true-do-for-a-shared-module)
- [22: What is the bootstrap pattern in Module Federation?](#22-what-is-the-bootstrap-pattern-in-module-federation)
- [23: What does the error "Shared module is not available for eager consumption" mean?](#23-what-does-the-error-shared-module-is-not-available-for-eager-consumption-mean)
- [24: How do you load a remote component in a React host?](#24-how-do-you-load-a-remote-component-in-a-react-host)
- [25: Why do you need Suspense around a remote component?](#25-why-do-you-need-suspense-around-a-remote-component)
- [26: Why should a remote component be wrapped in an error boundary?](#26-why-should-a-remote-component-be-wrapped-in-an-error-boundary)
- [27: How do you write an error boundary in React 19?](#27-how-do-you-write-an-error-boundary-in-react-19)
- [28: How does TypeScript know the types of a remote module?](#28-how-does-typescript-know-the-types-of-a-remote-module)
- [29: What is a remote entry file?](#29-what-is-a-remote-entry-file)
- [30: What is a container in Module Federation?](#30-what-is-a-container-in-module-federation)
- [31: What is a share scope?](#31-what-is-a-share-scope)
- [32: Can an app be both a host and a remote?](#32-can-an-app-be-both-a-host-and-a-remote)
- [33: What is a vertical split?](#33-what-is-a-vertical-split)
- [34: What is a horizontal split?](#34-what-is-a-horizontal-split)
- [35: How should you decide where to split an app?](#35-how-should-you-decide-where-to-split-an-app)
- [36: What is a bounded context?](#36-what-is-a-bounded-context)
- [37: What are the main downsides of micro frontends?](#37-what-are-the-main-downsides-of-micro-frontends)
- [38: When should you NOT use micro frontends?](#38-when-should-you-not-use-micro-frontends)
- [39: What is the difference between runtime and build-time integration?](#39-what-is-the-difference-between-runtime-and-build-time-integration)
- [40: What is single-spa?](#40-what-is-single-spa)
- [41: What is single-spa-react?](#41-what-is-single-spa-react)
- [42: What is the iframe approach to micro frontends?](#42-what-is-the-iframe-approach-to-micro-frontends)
- [43: What is a web component?](#43-what-is-a-web-component)
- [44: How can you wrap a React app as a custom element?](#44-how-can-you-wrap-a-react-app-as-a-custom-element)
- [45: What is server-side composition?](#45-what-is-server-side-composition)
- [46: What is client-side composition?](#46-what-is-client-side-composition)
- [47: What is an import map?](#47-what-is-an-import-map)
- [48: What is a design system and why does it matter for micro frontends?](#48-what-is-a-design-system-and-why-does-it-matter-for-micro-frontends)
- [49: Can different micro frontends use different React versions?](#49-can-different-micro-frontends-use-different-react-versions)
- [50: Can a React host load a micro frontend built with another framework?](#50-can-a-react-host-load-a-micro-frontend-built-with-another-framework)
- [51: What is the role of the host's routing in a micro frontend app?](#51-what-is-the-role-of-the-hosts-routing-in-a-micro-frontend-app)
- [52: How do you load a remote for one route with React Router?](#52-how-do-you-load-a-remote-for-one-route-with-react-router)
- [53: Which package do you import React Router from in v7?](#53-which-package-do-you-import-react-router-from-in-v7)
- [54: Should each micro frontend have its own BrowserRouter?](#54-should-each-micro-frontend-have-its-own-browserrouter)
- [55: How can a remote run both standalone and inside the host?](#55-how-can-a-remote-run-both-standalone-and-inside-the-host)
- [56: Why does every micro frontend need its own port in development?](#56-why-does-every-micro-frontend-need-its-own-port-in-development)
- [57: How do you run a host and its remotes locally?](#57-how-do-you-run-a-host-and-its-remotes-locally)
- [58: What is output.publicPath and why does it matter?](#58-what-is-outputpublicpath-and-why-does-it-matter)
- [59: What does publicPath: 'auto' do?](#59-what-does-publicpath-auto-do)
- [60: What does a basic remote webpack config look like?](#60-what-does-a-basic-remote-webpack-config-look-like)
- [61: What does a basic host webpack config look like?](#61-what-does-a-basic-host-webpack-config-look-like)
- [62: What does the "shop@http://..." syntax in remotes mean?](#62-what-does-the-shophttp-syntax-in-remotes-mean)
- [63: Can you use Module Federation with Vite?](#63-can-you-use-module-federation-with-vite)
- [64: What does a Vite remote config look like?](#64-what-does-a-vite-remote-config-look-like)
- [65: What is Rspack and why is it popular for micro frontends?](#65-what-is-rspack-and-why-is-it-popular-for-micro-frontends)
- [66: What is Rsbuild?](#66-what-is-rsbuild)
- [67: What is mf-manifest.json?](#67-what-is-mf-manifestjson)
- [68: What is the Module Federation runtime?](#68-what-is-the-module-federation-runtime)
- [69: What does loadRemote do?](#69-what-does-loadremote-do)
- [70: What does registerRemotes do?](#70-what-does-registerremotes-do)
- [71: What is a dynamic remote?](#71-what-is-a-dynamic-remote)
- [72: What is the difference between a static and a dynamic remote?](#72-what-is-the-difference-between-a-static-and-a-dynamic-remote)
- [73: Where should the list of remote URLs live in production?](#73-where-should-the-list-of-remote-urls-live-in-production)
- [74: What does lazy loading mean in a micro frontend setup?](#74-what-does-lazy-loading-mean-in-a-micro-frontend-setup)
- [75: How can micro frontends communicate with each other?](#75-how-can-micro-frontends-communicate-with-each-other)
- [76: How do you pass data from the host to a remote component?](#76-how-do-you-pass-data-from-the-host-to-a-remote-component)
- [77: How can a remote send an event to the host using CustomEvent?](#77-how-can-a-remote-send-an-event-to-the-host-using-customevent)
- [78: What is an event bus?](#78-what-is-an-event-bus)
- [79: Why is the URL a good way to share state between micro frontends?](#79-why-is-the-url-a-good-way-to-share-state-between-micro-frontends)
- [80: Can micro frontends share a React context?](#80-can-micro-frontends-share-a-react-context)
- [81: What is a shared library in Module Federation?](#81-what-is-a-shared-library-in-module-federation)
- [82: Should you share every dependency?](#82-should-you-share-every-dependency)
- [83: How do you read the shared versions from package.json?](#83-how-do-you-read-the-shared-versions-from-packagejson)
- [84: What happens if the host and a remote have different React patch versions?](#84-what-happens-if-the-host-and-a-remote-have-different-react-patch-versions)
- [85: What is the "Invalid hook call" error and how is it related to micro frontends?](#85-what-is-the-invalid-hook-call-error-and-how-is-it-related-to-micro-frontends)
- [86: What is a micro frontend "contract"?](#86-what-is-a-micro-frontend-contract)
- [87: What should a remote expose: a component, routes or a mount function?](#87-what-should-a-remote-expose-a-component-routes-or-a-mount-function)
- [88: How do you style micro frontends without conflicts?](#88-how-do-you-style-micro-frontends-without-conflicts)
- [89: What are CSS Modules and why do they help?](#89-what-are-css-modules-and-why-do-they-help)
- [90: What is Shadow DOM?](#90-what-is-shadow-dom)
- [91: What is a monorepo and how does it relate to micro frontends?](#91-what-is-a-monorepo-and-how-does-it-relate-to-micro-frontends)
- [92: What is a polyrepo setup?](#92-what-is-a-polyrepo-setup)
- [93: What is Nx and how does it help with React micro frontends?](#93-what-is-nx-and-how-does-it-help-with-react-micro-frontends)
- [94: What is Turborepo?](#94-what-is-turborepo)
- [95: What does "team autonomy" mean in micro frontends?](#95-what-does-team-autonomy-mean-in-micro-frontends)
- [96: What is the "strangler fig" pattern?](#96-what-is-the-strangler-fig-pattern)
- [97: How can micro frontends help migrate an old React app?](#97-how-can-micro-frontends-help-migrate-an-old-react-app)
- [98: How do you share a design system between micro frontends?](#98-how-do-you-share-a-design-system-between-micro-frontends)
- [99: What are design tokens?](#99-what-are-design-tokens)
- [100: What is a fallback UI?](#100-what-is-a-fallback-ui)
- [101: What is a skeleton screen?](#101-what-is-a-skeleton-screen)
- [102: Why should remote entry files not be cached for long?](#102-why-should-remote-entry-files-not-be-cached-for-long)
- [103: Why do chunk files have hashes in their names?](#103-why-do-chunk-files-have-hashes-in-their-names)
- [104: What is CORS and why does it matter for remotes?](#104-what-is-cors-and-why-does-it-matter-for-remotes)
- [105: How do you allow CORS on a webpack dev server for a remote?](#105-how-do-you-allow-cors-on-a-webpack-dev-server-for-a-remote)
- [106: Where are micro frontends usually hosted?](#106-where-are-micro-frontends-usually-hosted)
- [107: What does "technology agnostic" mean in micro frontends?](#107-what-does-technology-agnostic-mean-in-micro-frontends)
- [108: Is it a good idea to mix many frameworks in one app?](#108-is-it-a-good-idea-to-mix-many-frameworks-in-one-app)
- [109: What is a remote component?](#109-what-is-a-remote-component)
- [110: What is a shell layout?](#110-what-is-a-shell-layout)
- [111: Who should own the header and navigation?](#111-who-should-own-the-header-and-navigation)
- [112: What is a platform team?](#112-what-is-a-platform-team)
- [113: What is a feature team?](#113-what-is-a-feature-team)
- [114: What is Conway's Law?](#114-what-is-conways-law)
- [115: How do micro frontends affect bundle size?](#115-how-do-micro-frontends-affect-bundle-size)
- [116: Can micro frontends be server-side rendered?](#116-can-micro-frontends-be-server-side-rendered)
- [117: What is Next.js Multi-Zones?](#117-what-is-nextjs-multi-zones)
- [118: Can you use Module Federation with Next.js?](#118-can-you-use-module-federation-with-nextjs)
- [119: What is the difference between createRoot and ReactDOM.render?](#119-what-is-the-difference-between-createroot-and-reactdomrender)
- [120: Why is root.unmount() important for micro frontends?](#120-why-is-rootunmount-important-for-micro-frontends)
- [121: What is a mount/unmount contract?](#121-what-is-a-mountunmount-contract)
- [122: Can a micro frontend have its own React root?](#122-can-a-micro-frontend-have-its-own-react-root)
- [123: What is the difference between a remote component and a remote app?](#123-what-is-the-difference-between-a-remote-component-and-a-remote-app)
- [124: What is Module Federation's bridge for React?](#124-what-is-module-federations-bridge-for-react)
- [125: Why do teams use a monorepo tool's generators for micro frontends?](#125-why-do-teams-use-a-monorepo-tools-generators-for-micro-frontends)
- [126: What is a standalone mode for a remote?](#126-what-is-a-standalone-mode-for-a-remote)
- [127: What is a remote's "public API"?](#127-what-is-a-remotes-public-api)
- [128: What is the problem with deep imports from a remote?](#128-what-is-the-problem-with-deep-imports-from-a-remote)
- [129: What is semantic versioning and why does it matter here?](#129-what-is-semantic-versioning-and-why-does-it-matter-here)
- [130: What does ^ mean in a version range?](#130-what-does--mean-in-a-version-range)
- [131: How do micro frontends handle authentication?](#131-how-do-micro-frontends-handle-authentication)
- [132: Where should the access token live in a micro frontend app?](#132-where-should-the-access-token-live-in-a-micro-frontend-app)
- [133: How do remotes call back-end APIs?](#133-how-do-remotes-call-back-end-apis)
- [134: What is a Backend for Frontend (BFF)?](#134-what-is-a-backend-for-frontend-bff)
- [135: What is a feature flag?](#135-what-is-a-feature-flag)
- [136: Can each micro frontend use a different state library?](#136-can-each-micro-frontend-use-a-different-state-library)
- [137: Should you use one global Redux store for all micro frontends?](#137-should-you-use-one-global-redux-store-for-all-micro-frontends)
- [138: What is a shared singleton service?](#138-what-is-a-shared-singleton-service)
- [139: How do you add analytics to micro frontends?](#139-how-do-you-add-analytics-to-micro-frontends)
- [140: What is the role of index.html in a micro frontend setup?](#140-what-is-the-role-of-indexhtml-in-a-micro-frontend-setup)
- [141: What does "loosely coupled" mean for micro frontends?](#141-what-does-loosely-coupled-mean-for-micro-frontends)
- [142: What is a "distributed monolith"?](#142-what-is-a-distributed-monolith)
- [143: How do you show which micro frontend rendered a part of the page?](#143-how-do-you-show-which-micro-frontend-rendered-a-part-of-the-page)
- [144: What is the Module Federation Chrome DevTools extension?](#144-what-is-the-module-federation-chrome-devtools-extension)
- [145: What is the "dts" option in Module Federation 2.0?](#145-what-is-the-dts-option-in-module-federation-20)
- [146: How do you add type declarations for remotes by hand?](#146-how-do-you-add-type-declarations-for-remotes-by-hand)
- [147: What does "exposes" path like './Button' mean?](#147-what-does-exposes-path-like-button-mean)
- [148: How do you load a remote that exposes a named export?](#148-how-do-you-load-a-remote-that-exposes-a-named-export)
- [149: What are good first steps when a remote fails to load?](#149-what-are-good-first-steps-when-a-remote-fails-to-load)
- [150: What should you say if asked "are micro frontends worth it?"](#150-what-should-you-say-if-asked-are-micro-frontends-worth-it)

### Moderate Questions (151-300)

- [151: How does Module Federation pick a version for a shared package?](#151-how-does-module-federation-pick-a-version-for-a-shared-package)
- [152: What is shareStrategy in Module Federation 2.0?](#152-what-is-sharestrategy-in-module-federation-20)
- [153: What happens to a shared package when a remote is offline under version-first?](#153-what-happens-to-a-shared-package-when-a-remote-is-offline-under-version-first)
- [154: What does the import option in shared config do?](#154-what-does-the-import-option-in-shared-config-do)
- [155: What does shareKey do?](#155-what-does-sharekey-do)
- [156: What does packageName do in shared config?](#156-what-does-packagename-do-in-shared-config)
- [157: How do you share a package's sub-paths like react/jsx-runtime?](#157-how-do-you-share-a-packages-sub-paths-like-reactjsx-runtime)
- [158: What is the difference between eager sharing and the bootstrap pattern?](#158-what-is-the-difference-between-eager-sharing-and-the-bootstrap-pattern)
- [159: How does experiments.asyncStartup work in Module Federation 2.0?](#159-how-does-experimentsasyncstartup-work-in-module-federation-20)
- [160: How do you load a dynamic remote with plain webpack 5 (without the 2.0 runtime)?](#160-how-do-you-load-a-dynamic-remote-with-plain-webpack-5-without-the-20-runtime)
- [161: How do you create a React component that loads a remote by URL at runtime?](#161-how-do-you-create-a-react-component-that-loads-a-remote-by-url-at-runtime)
- [162: Why must you not create a lazy component inside a render function without memoizing it?](#162-why-must-you-not-create-a-lazy-component-inside-a-render-function-without-memoizing-it)
- [163: What is createInstance in the Module Federation runtime?](#163-what-is-createinstance-in-the-module-federation-runtime)
- [164: How do you combine build-time and runtime remotes?](#164-how-do-you-combine-build-time-and-runtime-remotes)
- [165: What are runtime plugins in Module Federation 2.0?](#165-what-are-runtime-plugins-in-module-federation-20)
- [166: How do you write a runtime plugin that shows a fallback when a remote fails?](#166-how-do-you-write-a-runtime-plugin-that-shows-a-fallback-when-a-remote-fails)
- [167: Which runtime plugin hooks are commonly used?](#167-which-runtime-plugin-hooks-are-commonly-used)
- [168: How can you rewrite remote URLs per environment with a runtime plugin?](#168-how-can-you-rewrite-remote-urls-per-environment-with-a-runtime-plugin)
- [169: How do you preload a remote?](#169-how-do-you-preload-a-remote)
- [170: How can you preload a remote route on link hover?](#170-how-can-you-preload-a-remote-route-on-link-hover)
- [171: How do you structure routes so a remote owns its sub-routes?](#171-how-do-you-structure-routes-so-a-remote-owns-its-sub-routes)
- [172: How should a remote build links when it doesn't know its base path?](#172-how-should-a-remote-build-links-when-it-doesnt-know-its-base-path)
- [173: How can a remote that has its own router stay in sync with the host's URL?](#173-how-can-a-remote-that-has-its-own-router-stay-in-sync-with-the-hosts-url)
- [174: Why would a remote use a MemoryRouter?](#174-why-would-a-remote-use-a-memoryrouter)
- [175: What is the basename option in React Router?](#175-what-is-the-basename-option-in-react-router)
- [176: How do you share React Router between host and remotes?](#176-how-do-you-share-react-router-between-host-and-remotes)
- [177: How do you handle a 404 inside a remote's area?](#177-how-do-you-handle-a-404-inside-a-remotes-area)
- [178: How do you lazy load routes from a remote with data routers?](#178-how-do-you-lazy-load-routes-from-a-remote-with-data-routers)
- [179: Can a remote expose route objects instead of a component?](#179-can-a-remote-expose-route-objects-instead-of-a-component)
- [180: What is patchRoutesOnNavigation in React Router?](#180-what-is-patchroutesonnavigation-in-react-router)
- [181: How should the host build its navigation menu when remotes are dynamic?](#181-how-should-the-host-build-its-navigation-menu-when-remotes-are-dynamic)
- [182: How do you pass the current user to remotes?](#182-how-do-you-pass-the-current-user-to-remotes)
- [183: How do you create a shared context package that works across remotes?](#183-how-do-you-create-a-shared-context-package-that-works-across-remotes)
- [184: Why can a context provided by the host be undefined in a remote?](#184-why-can-a-context-provided-by-the-host-be-undefined-in-a-remote)
- [185: How can you share a Zustand store between micro frontends?](#185-how-can-you-share-a-zustand-store-between-micro-frontends)
- [186: Why share a store package and not let the remote expose the store?](#186-why-share-a-store-package-and-not-let-the-remote-expose-the-store)
- [187: How can you use BroadcastChannel between micro frontends?](#187-how-can-you-use-broadcastchannel-between-micro-frontends)
- [188: How do you send data between a host and an iframe micro frontend?](#188-how-do-you-send-data-between-a-host-and-an-iframe-micro-frontend)
- [189: How do you build a typed event bus for micro frontends?](#189-how-do-you-build-a-typed-event-bus-for-micro-frontends)
- [190: How do you use an event bus inside a React component safely?](#190-how-do-you-use-an-event-bus-inside-a-react-component-safely)
- [191: How would you sync state through the URL in a remote?](#191-how-would-you-sync-state-through-the-url-in-a-remote)
- [192: When is passing callbacks as props a bad idea between host and remote?](#192-when-is-passing-callbacks-as-props-a-bad-idea-between-host-and-remote)
- [193: How do you share a design system without loading it twice?](#193-how-do-you-share-a-design-system-without-loading-it-twice)
- [194: How do you handle CSS-in-JS libraries like Emotion in micro frontends?](#194-how-do-you-handle-css-in-js-libraries-like-emotion-in-micro-frontends)
- [195: How do you use Tailwind CSS in micro frontends without class conflicts?](#195-how-do-you-use-tailwind-css-in-micro-frontends-without-class-conflicts)
- [196: Why can a remote's CSS reset break the host?](#196-why-can-a-remotes-css-reset-break-the-host)
- [197: How do you load a remote's CSS with Module Federation?](#197-how-do-you-load-a-remotes-css-with-module-federation)
- [198: What is CSS leakage on unmount?](#198-what-is-css-leakage-on-unmount)
- [199: How do you theme micro frontends consistently?](#199-how-do-you-theme-micro-frontends-consistently)
- [200: How do you use React portals in micro frontends?](#200-how-do-you-use-react-portals-in-micro-frontends)
- [201: How do you set up single-spa with a React host?](#201-how-do-you-set-up-single-spa-with-a-react-host)
- [202: What does activeWhen do in single-spa?](#202-what-does-activewhen-do-in-single-spa)
- [203: What are customProps in single-spa?](#203-what-are-customprops-in-single-spa)
- [204: What is a single-spa parcel?](#204-what-is-a-single-spa-parcel)
- [205: What is a single-spa utility module?](#205-what-is-a-single-spa-utility-module)
- [206: How does single-spa load apps in the browser?](#206-how-does-single-spa-load-apps-in-the-browser)
- [207: What is import-map-overrides?](#207-what-is-import-map-overrides)
- [208: How do you share React in a single-spa setup?](#208-how-do-you-share-react-in-a-single-spa-setup)
- [209: When would you choose single-spa over Module Federation?](#209-when-would-you-choose-single-spa-over-module-federation)
- [210: How do you create a React custom element that reacts to attribute changes?](#210-how-do-you-create-a-react-custom-element-that-reacts-to-attribute-changes)
- [211: How does a React custom element send events to the page around it?](#211-how-does-a-react-custom-element-send-events-to-the-page-around-it)
- [212: How does React 19 handle props on custom elements?](#212-how-does-react-19-handle-props-on-custom-elements)
- [213: How do you listen to custom element events from React?](#213-how-do-you-listen-to-custom-element-events-from-react)
- [214: How do you render a React app inside Shadow DOM?](#214-how-do-you-render-a-react-app-inside-shadow-dom)
- [215: How do you get styles into a Shadow DOM micro frontend?](#215-how-do-you-get-styles-into-a-shadow-dom-micro-frontend)
- [216: What problems can React have inside Shadow DOM?](#216-what-problems-can-react-have-inside-shadow-dom)
- [217: How do you pass a complex object to a React-based custom element?](#217-how-do-you-pass-a-complex-object-to-a-react-based-custom-element)
- [218: How do you build an iframe micro frontend that resizes to its content?](#218-how-do-you-build-an-iframe-micro-frontend-that-resizes-to-its-content)
- [219: How do you handle routing for iframe-based micro frontends?](#219-how-do-you-handle-routing-for-iframe-based-micro-frontends)
- [220: How do you integrate micro frontends at build time with npm packages?](#220-how-do-you-integrate-micro-frontends-at-build-time-with-npm-packages)
- [221: What should a build-time micro frontend package ship?](#221-what-should-a-build-time-micro-frontend-package-ship)
- [222: Why should React be a peerDependency in micro frontend packages?](#222-why-should-react-be-a-peerdependency-in-micro-frontend-packages)
- [223: How do you run all micro frontends with Nx?](#223-how-do-you-run-all-micro-frontends-with-nx)
- [224: How does Nx decide what to rebuild in a micro frontend monorepo?](#224-how-does-nx-decide-what-to-rebuild-in-a-micro-frontend-monorepo)
- [225: How do you enforce module boundaries in an Nx monorepo?](#225-how-do-you-enforce-module-boundaries-in-an-nx-monorepo)
- [226: How do you set up CI/CD so each micro frontend deploys on its own?](#226-how-do-you-set-up-cicd-so-each-micro-frontend-deploys-on-its-own)
- [227: Why deploy remotes to versioned folders?](#227-why-deploy-remotes-to-versioned-folders)
- [228: How do you roll back a broken remote?](#228-how-do-you-roll-back-a-broken-remote)
- [229: What is a canary release for a micro frontend?](#229-what-is-a-canary-release-for-a-micro-frontend)
- [230: How do you test a remote component in isolation?](#230-how-do-you-test-a-remote-component-in-isolation)
- [231: How do you test a host that imports remote modules?](#231-how-do-you-test-a-host-that-imports-remote-modules)
- [232: What are contract tests for micro frontends?](#232-what-are-contract-tests-for-micro-frontends)
- [233: How do you write a simple contract test for an exposed module?](#233-how-do-you-write-a-simple-contract-test-for-an-exposed-module)
- [234: How do you run end-to-end tests across micro frontends?](#234-how-do-you-run-end-to-end-tests-across-micro-frontends)
- [235: How do you test a remote against the production host?](#235-how-do-you-test-a-remote-against-the-production-host)
- [236: What is the advantage of a preview environment per pull request?](#236-what-is-the-advantage-of-a-preview-environment-per-pull-request)
- [237: How do you handle environment variables in micro frontends?](#237-how-do-you-handle-environment-variables-in-micro-frontends)
- [238: Why is "build once, deploy many" important for micro frontends?](#238-why-is-build-once-deploy-many-important-for-micro-frontends)
- [239: How do you share a runtime config with all remotes?](#239-how-do-you-share-a-runtime-config-with-all-remotes)
- [240: How do you debug a shared version mismatch?](#240-how-do-you-debug-a-shared-version-mismatch)
- [241: What does the warning "Unsatisfied version ... of shared singleton module" mean?](#241-what-does-the-warning-unsatisfied-version--of-shared-singleton-module-mean)
- [242: Why do you sometimes see React loaded twice even with sharing configured?](#242-why-do-you-sometimes-see-react-loaded-twice-even-with-sharing-configured)
- [243: How do you add hot reload to a remote while it runs inside the host?](#243-how-do-you-add-hot-reload-to-a-remote-while-it-runs-inside-the-host)
- [244: How do you handle a remote that is slow to load?](#244-how-do-you-handle-a-remote-that-is-slow-to-load)
- [245: How do you add a timeout when loading a remote?](#245-how-do-you-add-a-timeout-when-loading-a-remote)
- [246: How do you retry loading a remote after it fails?](#246-how-do-you-retry-loading-a-remote-after-it-fails)
- [247: How can the user retry a failed remote from the UI?](#247-how-can-the-user-retry-a-failed-remote-from-the-ui)
- [248: How do you log errors from micro frontends?](#248-how-do-you-log-errors-from-micro-frontends)
- [249: How do you know which micro frontend version is running in production?](#249-how-do-you-know-which-micro-frontend-version-is-running-in-production)
- [250: How do you handle source maps for remotes?](#250-how-do-you-handle-source-maps-for-remotes)
- [251: How do you measure the performance cost of micro frontends?](#251-how-do-you-measure-the-performance-cost-of-micro-frontends)
- [252: What is a performance budget for a micro frontend?](#252-what-is-a-performance-budget-for-a-micro-frontend)
- [253: What is Rsdoctor?](#253-what-is-rsdoctor)
- [254: How do you avoid a "waterfall" when loading nested remotes?](#254-how-do-you-avoid-a-waterfall-when-loading-nested-remotes)
- [255: How can you reduce the size of the remote entry?](#255-how-can-you-reduce-the-size-of-the-remote-entry)
- [256: How do you avoid layout shift when remote widgets load?](#256-how-do-you-avoid-layout-shift-when-remote-widgets-load)
- [257: How do you share images and fonts between micro frontends?](#257-how-do-you-share-images-and-fonts-between-micro-frontends)
- [258: How do you version a remote's exposed modules?](#258-how-do-you-version-a-remotes-exposed-modules)
- [259: How do you make a breaking change to a remote's props safely?](#259-how-do-you-make-a-breaking-change-to-a-remotes-props-safely)
- [260: How do you share TypeScript types for remote contracts?](#260-how-do-you-share-typescript-types-for-remote-contracts)
- [261: How do you configure dts in Module Federation 2.0?](#261-how-do-you-configure-dts-in-module-federation-20)
- [262: Why might automatic type sharing fail in CI?](#262-why-might-automatic-type-sharing-fail-in-ci)
- [263: How do you handle i18n (translations) in micro frontends?](#263-how-do-you-handle-i18n-translations-in-micro-frontends)
- [264: How can each remote load its own translations with i18next?](#264-how-can-each-remote-load-its-own-translations-with-i18next)
- [265: How do you handle accessibility across micro frontends?](#265-how-do-you-handle-accessibility-across-micro-frontends)
- [266: Who should manage focus after a navigation between micro frontends?](#266-who-should-manage-focus-after-a-navigation-between-micro-frontends)
- [267: How do you set the document title in micro frontends?](#267-how-do-you-set-the-document-title-in-micro-frontends)
- [268: How do you load data in a remote component?](#268-how-do-you-load-data-in-a-remote-component)
- [269: How do you share one TanStack Query client between micro frontends?](#269-how-do-you-share-one-tanstack-query-client-between-micro-frontends)
- [270: How do you prevent query key collisions in a shared query cache?](#270-how-do-you-prevent-query-key-collisions-in-a-shared-query-cache)
- [271: How do you use the React 19 use hook with remote data?](#271-how-do-you-use-the-react-19-use-hook-with-remote-data)
- [272: How do Suspense boundaries help with several remotes on one page?](#272-how-do-suspense-boundaries-help-with-several-remotes-on-one-page)
- [273: What is SuspenseList and can you use it?](#273-what-is-suspenselist-and-can-you-use-it)
- [274: How do you handle transitions when switching between remotes?](#274-how-do-you-handle-transitions-when-switching-between-remotes)
- [275: How do you share feature flags with remotes?](#275-how-do-you-share-feature-flags-with-remotes)
- [276: How can you A/B test two versions of a remote?](#276-how-can-you-ab-test-two-versions-of-a-remote)
- [277: How do you handle permissions for micro frontends?](#277-how-do-you-handle-permissions-for-micro-frontends)
- [278: How do you protect a remote route that needs login?](#278-how-do-you-protect-a-remote-route-that-needs-login)
- [279: How do you share an authenticated fetch helper?](#279-how-do-you-share-an-authenticated-fetch-helper)
- [280: How do you handle logout across all micro frontends?](#280-how-do-you-handle-logout-across-all-micro-frontends)
- [281: How do you choose between Module Federation, single-spa and web components?](#281-how-do-you-choose-between-module-federation-single-spa-and-web-components)
- [282: How do you migrate from @originjs/vite-plugin-federation to @module-federation/vite?](#282-how-do-you-migrate-from-originjsvite-plugin-federation-to-module-federationvite)
- [283: How does a Vite host load a remote in @module-federation/vite?](#283-how-does-a-vite-host-load-a-remote-in-module-federationvite)
- [284: Can a webpack host load a Vite remote?](#284-can-a-webpack-host-load-a-vite-remote)
- [285: Why is the remote entry of a Vite remote an ES module?](#285-why-is-the-remote-entry-of-a-vite-remote-an-es-module)
- [286: What is the library option in ModuleFederationPlugin?](#286-what-is-the-library-option-in-modulefederationplugin)
- [287: How do you use Module Federation with single-spa?](#287-how-do-you-use-module-federation-with-single-spa)
- [288: How do you organize folders in a React micro frontend monorepo?](#288-how-do-you-organize-folders-in-a-react-micro-frontend-monorepo)
- [289: How do you share webpack or Rspack config between micro frontends?](#289-how-do-you-share-webpack-or-rspack-config-between-micro-frontends)
- [290: How do you keep dependency versions aligned across micro frontends?](#290-how-do-you-keep-dependency-versions-aligned-across-micro-frontends)
- [291: What are pnpm catalogs and how do they help?](#291-what-are-pnpm-catalogs-and-how-do-they-help)
- [292: How do you upgrade React across many micro frontends?](#292-how-do-you-upgrade-react-across-many-micro-frontends)
- [293: How do you handle a remote that must stay on an older React version?](#293-how-do-you-handle-a-remote-that-must-stay-on-an-older-react-version)
- [294: How do you remove a micro frontend that is no longer needed?](#294-how-do-you-remove-a-micro-frontend-that-is-no-longer-needed)
- [295: What are the trade-offs of putting the header in the host vs a separate remote?](#295-what-are-the-trade-offs-of-putting-the-header-in-the-host-vs-a-separate-remote)
- [296: How does a micro frontend handle global keyboard shortcuts?](#296-how-does-a-micro-frontend-handle-global-keyboard-shortcuts)
- [297: How do you keep a consistent loading experience across remotes?](#297-how-do-you-keep-a-consistent-loading-experience-across-remotes)
- [298: How do you log which remotes and versions a user loaded?](#298-how-do-you-log-which-remotes-and-versions-a-user-loaded)
- [299: What should a remote do when the host passes invalid props?](#299-what-should-a-remote-do-when-the-host-passes-invalid-props)
- [300: How do you document a micro frontend's contract?](#300-how-do-you-document-a-micro-frontends-contract)

### Advanced Questions (301-450)

- [301: How does Module Federation work under the hood when a host imports a remote module?](#301-how-does-module-federation-work-under-the-hood-when-a-host-imports-a-remote-module)
- [302: What do the container's init and get methods do?](#302-what-do-the-containers-init-and-get-methods-do)
- [303: Why is the remote entry small even when the remote app is big?](#303-why-is-the-remote-entry-small-even-when-the-remote-app-is-big)
- [304: What is the global `__FEDERATION__` object?](#304-what-is-the-global-__federation__-object)
- [305: How does the share scope handle two versions of a non-singleton package?](#305-how-does-the-share-scope-handle-two-versions-of-a-non-singleton-package)
- [306: What are the risks of singleton sharing with loose version ranges?](#306-what-are-the-risks-of-singleton-sharing-with-loose-version-ranges)
- [307: Which app's shared version wins when several provide the same singleton?](#307-which-apps-shared-version-wins-when-several-provide-the-same-singleton)
- [308: Why can the result of shared version selection change between page loads?](#308-why-can-the-result-of-shared-version-selection-change-between-page-loads)
- [309: How can you force all remotes to use the host's React?](#309-how-can-you-force-all-remotes-to-use-the-hosts-react)
- [310: How would you use a runtime plugin to control which shared version is used?](#310-how-would-you-use-a-runtime-plugin-to-control-which-shared-version-is-used)
- [311: What is the tree-shaking problem with shared packages?](#311-what-is-the-tree-shaking-problem-with-shared-packages)
- [312: How do you decide between sharing a library and bundling it?](#312-how-do-you-decide-between-sharing-a-library-and-bundling-it)
- [313: How does Module Federation 2.0's manifest improve loading?](#313-how-does-module-federation-20s-manifest-improve-loading)
- [314: What is the cost of version-first share strategy at startup?](#314-what-is-the-cost-of-version-first-share-strategy-at-startup)
- [315: How would you design remote discovery for 50 micro frontends?](#315-how-would-you-design-remote-discovery-for-50-micro-frontends)
- [316: How do you make the remote registry fail safe?](#316-how-do-you-make-the-remote-registry-fail-safe)
- [317: How would you implement per-user remote overrides for testing in production?](#317-how-would-you-implement-per-user-remote-overrides-for-testing-in-production)
- [318: Why are remote overrides a security risk?](#318-why-are-remote-overrides-a-security-risk)
- [319: How do you secure micro frontends that load code from other origins?](#319-how-do-you-secure-micro-frontends-that-load-code-from-other-origins)
- [320: How do you write a Content Security Policy for a micro frontend app?](#320-how-do-you-write-a-content-security-policy-for-a-micro-frontend-app)
- [321: Can you use Subresource Integrity with Module Federation?](#321-can-you-use-subresource-integrity-with-module-federation)
- [322: How do you add an integrity attribute to remote entry scripts?](#322-how-do-you-add-an-integrity-attribute-to-remote-entry-scripts)
- [323: How do Trusted Types affect micro frontends?](#323-how-do-trusted-types-affect-micro-frontends)
- [324: How do you limit what a third-party micro frontend can do?](#324-how-do-you-limit-what-a-third-party-micro-frontend-can-do)
- [325: Why does every remote have full access to the page in Module Federation?](#325-why-does-every-remote-have-full-access-to-the-page-in-module-federation)
- [326: How do you design auth so a compromised remote does less damage?](#326-how-do-you-design-auth-so-a-compromised-remote-does-less-damage)
- [327: What is the risk of shared mutable globals between remotes?](#327-what-is-the-risk-of-shared-mutable-globals-between-remotes)
- [328: How do you prevent one remote's polyfills from affecting others?](#328-how-do-you-prevent-one-remotes-polyfills-from-affecting-others)
- [329: How would you design a micro frontend architecture for an e-commerce site?](#329-how-would-you-design-a-micro-frontend-architecture-for-an-e-commerce-site)
- [330: How would you split a large admin dashboard into micro frontends?](#330-how-would-you-split-a-large-admin-dashboard-into-micro-frontends)
- [331: What are the signs that a micro frontend split is wrong?](#331-what-are-the-signs-that-a-micro-frontend-split-is-wrong)
- [332: When would you merge two micro frontends?](#332-when-would-you-merge-two-micro-frontends)
- [333: How do you avoid the host becoming a bottleneck?](#333-how-do-you-avoid-the-host-becoming-a-bottleneck)
- [334: How do you handle slots or extension points in the host?](#334-how-do-you-handle-slots-or-extension-points-in-the-host)
- [335: How would you build a reusable RemoteBoundary component?](#335-how-would-you-build-a-reusable-remoteboundary-component)
- [336: How do you handle errors thrown in a remote's event handlers?](#336-how-do-you-handle-errors-thrown-in-a-remotes-event-handlers)
- [337: How can you tell which remote threw an uncaught error?](#337-how-can-you-tell-which-remote-threw-an-uncaught-error)
- [338: Why do you get "Script error." for errors from remotes?](#338-why-do-you-get-script-error-for-errors-from-remotes)
- [339: How do you design for partial failure in a micro frontend page?](#339-how-do-you-design-for-partial-failure-in-a-micro-frontend-page)
- [340: How do you handle a remote deployed with a bug that crashes on render?](#340-how-do-you-handle-a-remote-deployed-with-a-bug-that-crashes-on-render)
- [341: How do you handle users with an old host version loading new remotes?](#341-how-do-you-handle-users-with-an-old-host-version-loading-new-remotes)
- [342: How do you handle chunk load errors after a deployment?](#342-how-do-you-handle-chunk-load-errors-after-a-deployment)
- [343: Why keep previous remote versions on the CDN?](#343-why-keep-previous-remote-versions-on-the-cdn)
- [344: How does server-side rendering work with Module Federation?](#344-how-does-server-side-rendering-work-with-module-federation)
- [345: What are the hard parts of SSR with micro frontends?](#345-what-are-the-hard-parts-of-ssr-with-micro-frontends)
- [346: How can streaming SSR help with slow remotes?](#346-how-can-streaming-ssr-help-with-slow-remotes)
- [347: What happens if a remote's server and client versions differ during hydration?](#347-what-happens-if-a-remotes-server-and-client-versions-differ-during-hydration)
- [348: How do you do server-side composition without Module Federation?](#348-how-do-you-do-server-side-composition-without-module-federation)
- [349: What is Edge Side Includes (ESI)?](#349-what-is-edge-side-includes-esi)
- [350: How do you hydrate independent fragments on one page?](#350-how-do-you-hydrate-independent-fragments-on-one-page)
- [351: How do React Server Components fit with micro frontends?](#351-how-do-react-server-components-fit-with-micro-frontends)
- [352: What are the downsides of Next.js Multi-Zones?](#352-what-are-the-downsides-of-nextjs-multi-zones)
- [353: How do you configure Multi-Zones in Next.js?](#353-how-do-you-configure-multi-zones-in-nextjs)
- [354: How would you share client state across Next.js zones?](#354-how-would-you-share-client-state-across-nextjs-zones)
- [355: How do you avoid duplicate React when combining web components from different teams on one page?](#355-how-do-you-avoid-duplicate-react-when-combining-web-components-from-different-teams-on-one-page)
- [356: Can two React copies on one page cause bugs if they render into separate roots?](#356-can-two-react-copies-on-one-page-cause-bugs-if-they-render-into-separate-roots)
- [357: How do React's event delegation and roots affect micro frontends?](#357-how-do-reacts-event-delegation-and-roots-affect-micro-frontends)
- [358: How do you mount a React 19 remote into a React 18 host safely?](#358-how-do-you-mount-a-react-19-remote-into-a-react-18-host-safely)
- [359: What is the React bridge in Module Federation 2.0 actually doing?](#359-what-is-the-react-bridge-in-module-federation-20-actually-doing)
- [360: How do you use createBridgeComponent and createRemoteAppComponent?](#360-how-do-you-use-createbridgecomponent-and-createremoteappcomponent)
- [361: What do you lose when a remote runs in its own React root?](#361-what-do-you-lose-when-a-remote-runs-in-its-own-react-root)
- [362: How do you design a stable interface between host and remote apps?](#362-how-do-you-design-a-stable-interface-between-host-and-remote-apps)
- [363: Why is passing React elements between micro frontends risky?](#363-why-is-passing-react-elements-between-micro-frontends-risky)
- [364: How would you build a cross-framework micro frontend host with React?](#364-how-would-you-build-a-cross-framework-micro-frontend-host-with-react)
- [365: How do you handle props updates for a mounted non-React micro frontend?](#365-how-do-you-handle-props-updates-for-a-mounted-non-react-micro-frontend)
- [366: How does React Strict Mode affect micro frontend mounting code?](#366-how-does-react-strict-mode-affect-micro-frontend-mounting-code)
- [367: What is the "createRoot on a container that already has a root" warning?](#367-what-is-the-createroot-on-a-container-that-already-has-a-root-warning)
- [368: How do you prevent memory leaks in long-running micro frontend apps?](#368-how-do-you-prevent-memory-leaks-in-long-running-micro-frontend-apps)
- [369: How do you find which micro frontend is leaking memory?](#369-how-do-you-find-which-micro-frontend-is-leaking-memory)
- [370: How do you optimize the first page load of a micro frontend app?](#370-how-do-you-optimize-the-first-page-load-of-a-micro-frontend-app)
- [371: How can the host add preload hints for the current route's remote?](#371-how-can-the-host-add-preload-hints-for-the-current-routes-remote)
- [372: Why does serving remotes from different domains hurt performance?](#372-why-does-serving-remotes-from-different-domains-hurt-performance)
- [373: How do you avoid duplicate code that isn't shared, like lodash in each remote?](#373-how-do-you-avoid-duplicate-code-that-isnt-shared-like-lodash-in-each-remote)
- [374: How do you measure Web Vitals per micro frontend?](#374-how-do-you-measure-web-vitals-per-micro-frontend)
- [375: How do you stop one remote from blocking the main thread for others?](#375-how-do-you-stop-one-remote-from-blocking-the-main-thread-for-others)
- [376: How do you load a remote only when it scrolls into view?](#376-how-do-you-load-a-remote-only-when-it-scrolls-into-view)
- [377: How do you cache remote modules with a service worker?](#377-how-do-you-cache-remote-modules-with-a-service-worker)
- [378: Can micro frontends work offline?](#378-can-micro-frontends-work-offline)
- [379: How do you handle a remote that needs a different browser target than the host?](#379-how-do-you-handle-a-remote-that-needs-a-different-browser-target-than-the-host)
- [380: How would you handle global CSS that must be shared, like fonts and resets?](#380-how-would-you-handle-global-css-that-must-be-shared-like-fonts-and-resets)
- [381: How do you handle CSS ordering problems between remotes?](#381-how-do-you-handle-css-ordering-problems-between-remotes)
- [382: How do CSS cascade layers help in micro frontends?](#382-how-do-css-cascade-layers-help-in-micro-frontends)
- [383: How do you share a theme with CSS-in-JS when remotes can't share a provider?](#383-how-do-you-share-a-theme-with-css-in-js-when-remotes-cant-share-a-provider)
- [384: How do you build a design system for micro frontends with different React versions?](#384-how-do-you-build-a-design-system-for-micro-frontends-with-different-react-versions)
- [385: What is the trade-off of sharing the design system at runtime vs bundling it?](#385-what-is-the-trade-off-of-sharing-the-design-system-at-runtime-vs-bundling-it)
- [386: How do you do visual regression testing across micro frontends?](#386-how-do-you-do-visual-regression-testing-across-micro-frontends)
- [387: How would you set up contract testing with consumer-driven contracts?](#387-how-would-you-set-up-contract-testing-with-consumer-driven-contracts)
- [388: How do you test a remote's build output before deployment?](#388-how-do-you-test-a-remotes-build-output-before-deployment)
- [389: How do you run integration tests that mix local and deployed remotes?](#389-how-do-you-run-integration-tests-that-mix-local-and-deployed-remotes)
- [390: How do you test what happens when a remote is down?](#390-how-do-you-test-what-happens-when-a-remote-is-down)
- [391: How do you handle the host's dependency on remote TypeScript types in a polyrepo?](#391-how-do-you-handle-the-hosts-dependency-on-remote-typescript-types-in-a-polyrepo)
- [392: What happens to type safety when a remote deploys without the host rebuilding?](#392-what-happens-to-type-safety-when-a-remote-deploys-without-the-host-rebuilding)
- [393: How do you validate props at runtime at a micro frontend boundary?](#393-how-do-you-validate-props-at-runtime-at-a-micro-frontend-boundary)
- [394: How do you handle state that must survive navigation between remotes?](#394-how-do-you-handle-state-that-must-survive-navigation-between-remotes)
- [395: How do you design a shared store so teams don't step on each other?](#395-how-do-you-design-a-shared-store-so-teams-dont-step-on-each-other)
- [396: How would you design an event contract that can evolve?](#396-how-would-you-design-an-event-contract-that-can-evolve)
- [397: How do you handle events fired before a listener is ready?](#397-how-do-you-handle-events-fired-before-a-listener-is-ready)
- [398: What are the downsides of using window CustomEvents for all communication?](#398-what-are-the-downsides-of-using-window-customevents-for-all-communication)
- [399: How would you prevent a "chatty" relationship between micro frontends?](#399-how-would-you-prevent-a-chatty-relationship-between-micro-frontends)
- [400: How do you handle shared forms that span several micro frontends?](#400-how-do-you-handle-shared-forms-that-span-several-micro-frontends)
- [401: How do you manage the cost of many CI pipelines?](#401-how-do-you-manage-the-cost-of-many-ci-pipelines)
- [402: How do you make a shared CI template for micro frontends?](#402-how-do-you-make-a-shared-ci-template-for-micro-frontends)
- [403: How do you promote a remote version from staging to production?](#403-how-do-you-promote-a-remote-version-from-staging-to-production)
- [404: How would you implement automatic rollback for a remote?](#404-how-would-you-implement-automatic-rollback-for-a-remote)
- [405: How do you handle database or API changes that a remote depends on?](#405-how-do-you-handle-database-or-api-changes-that-a-remote-depends-on)
- [406: How do you coordinate a release that needs changes in several remotes?](#406-how-do-you-coordinate-a-release-that-needs-changes-in-several-remotes)
- [407: What is the risk of Module Federation remotes in a monorepo importing each other at build time?](#407-what-is-the-risk-of-module-federation-remotes-in-a-monorepo-importing-each-other-at-build-time)
- [408: How would you handle a shared library with a breaking change in a federated setup?](#408-how-would-you-handle-a-shared-library-with-a-breaking-change-in-a-federated-setup)
- [409: How can shareKey help during a major version migration?](#409-how-can-sharekey-help-during-a-major-version-migration)
- [410: How do you debug "Cannot read properties of undefined (reading 'call')" in Module Federation?](#410-how-do-you-debug-cannot-read-properties-of-undefined-reading-call-in-module-federation)
- [411: Why does each federated webpack app need a unique uniqueName?](#411-why-does-each-federated-webpack-app-need-a-unique-uniquename)
- [412: How does Module Federation handle two remotes that expose the same module name?](#412-how-does-module-federation-handle-two-remotes-that-expose-the-same-module-name)
- [413: How do you load the same remote twice with different versions?](#413-how-do-you-load-the-same-remote-twice-with-different-versions)
- [414: How do you replace a loaded remote with a newer version without a page reload?](#414-how-do-you-replace-a-loaded-remote-with-a-newer-version-without-a-page-reload)
- [415: How do you detect that a new version of a remote is available?](#415-how-do-you-detect-that-a-new-version-of-a-remote-is-available)
- [416: How do you share code between the host's and remote's Node SSR servers safely?](#416-how-do-you-share-code-between-the-hosts-and-remotes-node-ssr-servers-safely)
- [417: Why is module-level state dangerous in SSR micro frontends?](#417-why-is-module-level-state-dangerous-in-ssr-micro-frontends)
- [418: How do you refresh server-side remotes without restarting the server?](#418-how-do-you-refresh-server-side-remotes-without-restarting-the-server)
- [419: How do you handle SEO for client-side rendered micro frontends?](#419-how-do-you-handle-seo-for-client-side-rendered-micro-frontends)
- [420: How do you handle meta tags when several remotes are on one page?](#420-how-do-you-handle-meta-tags-when-several-remotes-are-on-one-page)
- [421: How do you think about micro frontends vs a modular monolith?](#421-how-do-you-think-about-micro-frontends-vs-a-modular-monolith)
- [422: How would you migrate a modular monolith to micro frontends later?](#422-how-would-you-migrate-a-modular-monolith-to-micro-frontends-later)
- [423: How would you migrate from single-spa to Module Federation?](#423-how-would-you-migrate-from-single-spa-to-module-federation)
- [424: How would you migrate a webpack Module Federation setup to Rspack?](#424-how-would-you-migrate-a-webpack-module-federation-setup-to-rspack)
- [425: How would you migrate a federated app from webpack to Vite?](#425-how-would-you-migrate-a-federated-app-from-webpack-to-vite)
- [426: What are common pitfalls with @module-federation/vite?](#426-what-are-common-pitfalls-with-module-federationvite)
- [427: How do you handle remotes that use different state management libraries in the same React tree?](#427-how-do-you-handle-remotes-that-use-different-state-management-libraries-in-the-same-react-tree)
- [428: How do you design a micro frontend platform for many independent teams?](#428-how-do-you-design-a-micro-frontend-platform-for-many-independent-teams)
- [429: What governance rules would you set for micro frontend teams?](#429-what-governance-rules-would-you-set-for-micro-frontend-teams)
- [430: How do you measure if a micro frontend architecture is working?](#430-how-do-you-measure-if-a-micro-frontend-architecture-is-working)
- [431: How do you handle a team that keeps breaking other teams' remotes?](#431-how-do-you-handle-a-team-that-keeps-breaking-other-teams-remotes)
- [432: How would you handle a slow host build that blocks all teams?](#432-how-would-you-handle-a-slow-host-build-that-blocks-all-teams)
- [433: How would you design local development for 20 remotes?](#433-how-would-you-design-local-development-for-20-remotes)
- [434: How do you handle authentication in local development with remote environments?](#434-how-do-you-handle-authentication-in-local-development-with-remote-environments)
- [435: How do you handle mixed content and HTTPS in local remote overrides?](#435-how-do-you-handle-mixed-content-and-https-in-local-remote-overrides)
- [436: How would you implement a dev panel to switch remote versions?](#436-how-would-you-implement-a-dev-panel-to-switch-remote-versions)
- [437: What questions would you ask before recommending micro frontends?](#437-what-questions-would-you-ask-before-recommending-micro-frontends)
- [438: How do you explain the trade-off between isolation and integration?](#438-how-do-you-explain-the-trade-off-between-isolation-and-integration)
- [439: How would you build a plugin system for a SaaS product with micro frontends?](#439-how-would-you-build-a-plugin-system-for-a-saas-product-with-micro-frontends)
- [440: How do you handle a remote that needs data from the host on every render?](#440-how-do-you-handle-a-remote-that-needs-data-from-the-host-on-every-render)
- [441: How do you avoid re-rendering a remote when the host re-renders?](#441-how-do-you-avoid-re-rendering-a-remote-when-the-host-re-renders)
- [442: Does the React Compiler work across micro frontends?](#442-does-the-react-compiler-work-across-micro-frontends)
- [443: How would you design error handling contracts between host and remote?](#443-how-would-you-design-error-handling-contracts-between-host-and-remote)
- [444: What are the biggest mistakes teams make with React micro frontends?](#444-what-are-the-biggest-mistakes-teams-make-with-react-micro-frontends)
- [445: How do you explain Module Federation to a non-technical stakeholder?](#445-how-do-you-explain-module-federation-to-a-non-technical-stakeholder)
- [446: How would you approach a performance regression after splitting into micro frontends?](#446-how-would-you-approach-a-performance-regression-after-splitting-into-micro-frontends)
- [447: How do you handle cookies and storage keys across micro frontends?](#447-how-do-you-handle-cookies-and-storage-keys-across-micro-frontends)
- [448: How would you design micro frontends for a mobile web app with slow networks?](#448-how-would-you-design-micro-frontends-for-a-mobile-web-app-with-slow-networks)
- [449: What trends do you see in React micro frontends right now?](#449-what-trends-do-you-see-in-react-micro-frontends-right-now)
- [450: If you had to sum up the key principles of a good React micro frontend architecture, what would they be?](#450-if-you-had-to-sum-up-the-key-principles-of-a-good-react-micro-frontend-architecture-what-would-they-be)

---

# Easy Questions (1-150)

## 1: What is a micro frontend?

A micro frontend is a part of a web app's UI that one team builds, tests and deploys on its own. You split a big front-end into smaller apps, for example "catalog", "cart" and "account", and put them together in the browser so the user still sees one application.

It is the same idea as microservices on the back-end, but applied to the UI.

## 2: Why would a company use micro frontends with React?

The reasons are mostly about teams, not about React itself:

- Several teams can work on one product without blocking each other.
- Each team can release its part when it is ready.
- A big code base is split into smaller apps that are easier to understand and build.
- Old parts (for example a class component app or a jQuery page) can be replaced step by step.

If you have one small team, a normal React app is usually the better choice.

## 3: What is a monolithic frontend?

It is one front-end app with all features in one repository, one build and one deployment. Most React projects start this way, and it works fine for a long time.

Problems show up when the app and the number of teams grow: builds get slow, merge conflicts are common, and one broken feature can block the release of everything else.

## 4: What is the difference between a micro frontend and a React component library?

A component library is a set of reusable UI pieces (buttons, inputs, modals) published as an npm package. Apps install it at build time, so a change means every app has to update the version and redeploy.

A micro frontend is a full feature with its own pages, logic and data calls. It is usually loaded at runtime, so its team can deploy a new version without the other apps rebuilding.

## 5: What is a host (shell) application?

The host, also called the shell or container, is the app the user opens first. It usually holds the layout (header, navigation, footer), top-level routing, login and other global things, and it loads the micro frontends into its pages.

Keep the host small. If business logic piles up there, it turns into a new monolith.

## 6: What is a remote application?

A remote is a micro frontend that the host loads at runtime. It is built and deployed on its own and exposes some modules, for example a component or a set of routes, that the host can import.

A remote can usually also run as a normal standalone React app during development.

## 7: What does "independent deployment" mean?

It means a team can ship a new version of its micro frontend to production without rebuilding or redeploying the host or other micro frontends. The host picks up the new version the next time the page loads.

This is the main benefit. If every change still needs a full rebuild of all apps, you pay the cost of micro frontends and get little back.

## 8: What are the common ways to build micro frontends with React?

- **Module Federation** with webpack, Rspack or Vite. The most common option today.
- **single-spa**, a framework that mounts and unmounts apps based on the URL.
- **Web components**, where a React app is wrapped in a custom element.
- **iframes**, the oldest and most isolated option.
- **Build-time integration**, where each part is an npm package installed into the host.
- **Server-side composition**, for example Next.js Multi-Zones or edge-side includes.

## 9: What is Module Federation?

Module Federation is a feature that first shipped with webpack 5. It lets one JavaScript app load code from another app at runtime, as if it were a normal import. Each app declares which modules it exposes and which libraries it shares with others.

Today it is a separate project with its own runtime (Module Federation 2.0) that works with webpack, Rspack, Rsbuild and Vite.

## 10: What is Module Federation 2.0?

Module Federation 2.0 is the newer version maintained by the Module Federation team (mostly ByteDance and Zack Jackson). It lives in the `@module-federation/*` packages, for example `@module-federation/enhanced`.

Compared to the original webpack plugin it adds a separate runtime you can call from code, a manifest file (`mf-manifest.json`), automatic TypeScript type sharing, runtime plugins, a Chrome DevTools extension and support for more bundlers.

## 11: What is the ModuleFederationPlugin?

It is the build plugin that turns an app into a host, a remote, or both. In plain webpack 5 you import it from webpack itself:

```js
const { ModuleFederationPlugin } = require("webpack").container;
```

With Module Federation 2.0 you import it from `@module-federation/enhanced/webpack` (or `/rspack` for Rspack). The options look almost the same.

## 12: What does the name option do in Module Federation?

`name` is the unique name of the app inside the federation. Other apps use it to refer to this remote, and it is also the name of the global container object the remote creates.

Pick a short, stable name like `shop` or `cart`. Changing it later breaks every host that points to it.

## 13: What does the filename option do?

`filename` is the name of the remote entry file the build produces, usually `remoteEntry.js`. The host loads this small file first. It contains a map of what the remote exposes and which shared libraries it needs, but not the actual feature code.

## 14: What does the exposes option do?

`exposes` lists which files of the remote other apps may load. The key is the public name and the value is the local path.

```js
exposes: {
  './ProductList': './src/components/ProductList.tsx',
  './routes': './src/routes.tsx',
},
```

It is the public API of the remote. Everything not listed stays private.

## 15: What does the remotes option do?

`remotes` tells a host where to find its remotes. The key is the alias you use in imports, and the value points to the remote entry.

```js
remotes: {
  shop: 'shop@http://localhost:3001/remoteEntry.js',
},
```

After that, `import('shop/ProductList')` in the host loads the `./ProductList` module from the `shop` remote.

## 16: What does the shared option do?

`shared` lists npm packages that the host and remotes should share at runtime instead of each loading its own copy. For React apps you nearly always share `react` and `react-dom`, and often `react-router` and your state library.

Sharing makes the page smaller and, more importantly, keeps one React instance in the page.

## 17: Why must React be a singleton in a micro frontend setup?

React keeps internal state, like the current hook dispatcher, in its module. If a host and a remote each load their own copy of React, a component from the remote may render with one copy while `react-dom` from the host uses another one.

That breaks hooks and context and gives the "Invalid hook call" error. Setting `singleton: true` for `react` and `react-dom` makes sure only one copy is used.

## 18: What does singleton: true mean?

It tells Module Federation that only one version of the package may exist in the page. If the host and remotes ask for different versions, one version is picked (normally the highest that was registered) and everyone uses it.

```js
shared: {
  react: { singleton: true, requiredVersion: '^19.0.0' },
  'react-dom': { singleton: true, requiredVersion: '^19.0.0' },
},
```

## 19: What does requiredVersion do?

`requiredVersion` is the version range the app needs, for example `^19.0.0`. At runtime Module Federation checks if the shared version that was picked fits this range. If it doesn't, it prints a warning, or throws when `strictVersion` is on.

A common pattern is to read it from `package.json` so it never gets out of date.

## 20: What does strictVersion do?

With `strictVersion: true`, a version mismatch for a shared package throws an error instead of only printing a warning. If the package is not a singleton, the app falls back to its own copy.

It is useful when a mismatch would cause hard-to-find bugs. Without it, you only see a console warning and the app may still break in odd ways.

## 21: What does eager: true do for a shared module?

Normally shared modules are loaded asynchronously, after Module Federation has decided which version to use. `eager: true` puts the package into the initial bundle so it is available right away.

It can fix the "Shared module is not available for eager consumption" error, but it makes the entry bundle bigger and can lead to duplicate copies. The usual fix is the async bootstrap pattern instead.

## 22: What is the bootstrap pattern in Module Federation?

You move the real app startup into a separate file and load it with a dynamic import from the entry file:

```js
// src/index.js
import("./bootstrap");
```

```jsx
// src/bootstrap.jsx
import { createRoot } from "react-dom/client";
import App from "./App";

createRoot(document.getElementById("root")).render(<App />);
```

The dynamic import gives Module Federation time to set up shared modules before any code imports React.

## 23: What does the error "Shared module is not available for eager consumption" mean?

It means your code imported a shared package (usually React) synchronously, before Module Federation finished setting up the share scope. This happens when the entry file imports React directly.

Fix it with the bootstrap pattern (`import('./bootstrap')`). In Module Federation 2.0 you can also turn on `experiments: { asyncStartup: true }`, which does the same thing for you.

## 24: How do you load a remote component in a React host?

Use `React.lazy` with a dynamic import and wrap it in `Suspense`:

```jsx
import { lazy, Suspense } from "react";

const ProductList = lazy(() => import("shop/ProductList"));

export function ShopPage() {
  return (
    <Suspense fallback={<p>Loading products...</p>}>
      <ProductList />
    </Suspense>
  );
}
```

The remote code is fetched only when the component is rendered for the first time.

## 25: Why do you need Suspense around a remote component?

Loading a remote is asynchronous, because the browser has to download the remote entry and the module's chunks. `React.lazy` suspends while this happens, and React needs a `Suspense` boundary above it to know what to show in the meantime.

Without a boundary, the suspension goes up to the nearest one, which may hide a much bigger part of the page.

## 26: Why should a remote component be wrapped in an error boundary?

A remote is a separate deployment and can fail: the server is down, the network is slow, or the new version has a bug. Without an error boundary, an error while loading or rendering it unmounts the whole React tree.

An error boundary around each remote keeps the rest of the page working and lets you show a simple fallback message.

## 27: How do you write an error boundary in React 19?

Error boundaries still need a class component. Many teams use the `react-error-boundary` package instead of writing one:

```jsx
import { ErrorBoundary } from "react-error-boundary";

<ErrorBoundary fallback={<p>Shop is not available right now.</p>}>
  <Suspense fallback={<p>Loading...</p>}>
    <ProductList />
  </Suspense>
</ErrorBoundary>;
```

## 28: How does TypeScript know the types of a remote module?

By default it doesn't, so `import('shop/ProductList')` gives a "cannot find module" error. You have two options:

- Write a declaration by hand: `declare module 'shop/ProductList';`
- Use Module Federation 2.0, which can generate types for exposed modules and download them into the host (the `dts` option).

## 29: What is a remote entry file?

It is the small JavaScript file (usually `remoteEntry.js`) that a remote publishes. When the host loads it, it registers a container with two functions: `init`, to receive the shared modules, and `get`, to return an exposed module.

It is the only file whose URL the host needs to know.

## 30: What is a container in Module Federation?

A container is the object a remote creates when its remote entry runs. It holds the list of exposed modules and the info about shared packages.

The host talks to the remote only through this container: it calls `init` with the share scope and `get('./ProductList')` to get a module factory.

## 31: What is a share scope?

A share scope is a registry of shared packages and their versions that all apps in the page fill in together. When a module needs `react`, Module Federation looks into the share scope and picks the best version for it.

The default scope is called `default`. You rarely need another one.

## 32: Can an app be both a host and a remote?

Yes. An app can expose modules and consume other remotes at the same time. For example, a `checkout` app can expose a `CheckoutPage` and also load a `PaymentForm` from a `payments` remote.

Be careful with this, because long chains of remotes make loading slower and debugging harder.

## 33: What is a vertical split?

In a vertical split each micro frontend owns whole pages or routes. For example `/products/*` belongs to the shop team and `/account/*` to the account team. Only one micro frontend is on screen at a time, plus the host's layout.

It is the easiest split to work with, because teams rarely step on each other.

## 34: What is a horizontal split?

In a horizontal split several micro frontends share the same page. For example the product page shows a "recommendations" widget from one team and a "reviews" widget from another.

It gives more flexibility, but you need more coordination: layout, loading states, shared data and errors on one page.

## 35: How should you decide where to split an app?

Split by business domain, not by technical layer. Good boundaries are areas that change for different reasons and belong to different teams, like "search", "checkout" or "account".

A bad split is "all forms in one micro frontend and all tables in another". Then every feature change touches several teams.

## 36: What is a bounded context?

It is a term from Domain-Driven Design. A bounded context is an area of the business with its own language and rules, for example "orders" or "billing".

Micro frontend boundaries often follow bounded contexts, so one team owns one context from the UI down to the API.

## 37: What are the main downsides of micro frontends?

- More complex setup: many repos or projects, pipelines and deployments.
- Risk of loading duplicate libraries and bigger bundles.
- Harder debugging across apps.
- UI can become inconsistent if teams don't share a design system.
- Version alignment of React and shared libraries takes work.
- More things that can fail at runtime.

## 38: When should you NOT use micro frontends?

When you have one team or a few developers, when the app is small, or when the problem is really bad code structure, not team scaling. In those cases a well-organized monolith or a monorepo with clear modules is simpler and faster.

Micro frontends solve an organizational problem. If you don't have that problem, you only get the costs.

## 39: What is the difference between runtime and build-time integration?

With build-time integration each micro frontend is an npm package that the host installs and bundles. It is simple and type-safe, but every change needs a host rebuild and redeploy.

With runtime integration the host loads the micro frontend from a URL in the browser. Teams can deploy on their own, but you have to handle versions, failures and loading at runtime.

## 40: What is single-spa?

single-spa is a JavaScript framework for running several front-end apps on one page. Each app registers lifecycle functions (`bootstrap`, `mount`, `unmount`), and single-spa mounts or unmounts it based on the URL.

It works with React, Vue, Angular and others, so it is common when different teams use different frameworks.

## 41: What is single-spa-react?

It is a helper library that turns a React root component into the lifecycle functions single-spa expects:

```jsx
import React from "react";
import ReactDOMClient from "react-dom/client";
import singleSpaReact from "single-spa-react";
import Root from "./Root";

const lifecycles = singleSpaReact({
  React,
  ReactDOMClient,
  rootComponent: Root,
  errorBoundary: () => <p>Something went wrong.</p>,
});

export const { bootstrap, mount, unmount } = lifecycles;
```

## 42: What is the iframe approach to micro frontends?

Each micro frontend is a separate page loaded inside an `<iframe>` in the host. It gives the strongest isolation: separate JavaScript, CSS and global state.

The downsides are a heavier page, harder communication (via `postMessage`), awkward sizing and scrolling, and poor accessibility and SEO. It is still a fair choice for third-party or legacy content.

## 43: What is a web component?

A web component is a custom HTML element built with browser standards: Custom Elements, Shadow DOM and HTML templates. Once you register it, you can use it like any tag, for example `<product-card>`.

In micro frontends, web components are a framework-neutral way to embed one app in another.

## 44: How can you wrap a React app as a custom element?

Create a class that extends `HTMLElement` and render React into it:

```jsx
import { createRoot } from "react-dom/client";
import ProductCard from "./ProductCard";

class ProductCardElement extends HTMLElement {
  connectedCallback() {
    this.root = createRoot(this);
    this.root.render(<ProductCard id={this.getAttribute("product-id")} />);
  }

  disconnectedCallback() {
    this.root.unmount();
  }
}

customElements.define("product-card", ProductCardElement);
```

## 45: What is server-side composition?

The page is put together on the server (or at the edge) before it reaches the browser. Each part of the page comes from a different service, joined with techniques like Server Side Includes, Edge Side Includes or a composition layer.

It is good for SEO and first load speed, but client-side interactivity between the parts needs extra work.

## 46: What is client-side composition?

The browser loads a host page, and the host's JavaScript loads and renders the micro frontends. Module Federation, single-spa and web components are all client-side composition.

It is the most common approach for React apps because it is simple to set up and works well for app-like UIs.

## 47: What is an import map?

An import map is a JSON block that tells the browser where to find a module for a bare name:

```html
<script type="importmap">
  {
    "imports": {
      "@acme/shop": "https://cdn.example.com/shop/1.4.0/main.js"
    }
  }
</script>
```

After that, `import('@acme/shop')` loads that URL. single-spa setups often use import maps to point to the current version of each micro frontend.

## 48: What is a design system and why does it matter for micro frontends?

A design system is a shared set of UI components, colors, fonts and rules. When several teams build parts of the same page, it is the main thing that keeps the app looking like one product.

It is usually published as an npm package, and often shared at runtime too, so all micro frontends use the same version.

## 49: Can different micro frontends use different React versions?

Technically yes, if each one renders into its own DOM node with its own React and `react-dom`, for example through web components or single-spa. But then you load React more than once and can't pass React elements or context between them.

With Module Federation, the normal setup is one shared React version. Mixing major versions should be a short-term thing during a migration.

## 50: Can a React host load a micro frontend built with another framework?

Yes. The host just needs a way to mount it into a DOM node. Common options are a web component, single-spa, or a remote that exposes a `mount(element)` function instead of a React component.

```jsx
useEffect(() => {
  let unmount;
  import("vueApp/mount").then(({ mount }) => {
    unmount = mount(ref.current);
  });
  return () => unmount?.();
}, []);
```

## 51: What is the role of the host's routing in a micro frontend app?

The host usually owns the top-level routes and decides which micro frontend to show for each URL, for example `/shop/*` goes to the shop remote. The remote then handles its own sub-routes below that path.

This keeps routing ownership clear: the host knows only the entry path of each team, not their inner pages.

## 52: How do you load a remote for one route with React Router?

Use a lazy component as the route element and let the remote handle the rest of the path with a `/*` route:

```jsx
import { lazy, Suspense } from "react";
import { BrowserRouter, Routes, Route } from "react-router";

const ShopApp = lazy(() => import("shop/App"));

export function App() {
  return (
    <BrowserRouter>
      <Suspense fallback={<p>Loading...</p>}>
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/shop/*" element={<ShopApp />} />
        </Routes>
      </Suspense>
    </BrowserRouter>
  );
}
```

## 53: Which package do you import React Router from in v7?

In React Router 7 the main package is `react-router`. Things like `BrowserRouter`, `Routes`, `Route`, `Link` and `useNavigate` are all imported from it.

`react-router-dom` still exists, but only re-exports from `react-router` to make upgrades easier. New code should import from `react-router`.

## 54: Should each micro frontend have its own BrowserRouter?

No, not when they render inside the same React tree. There should be one router, owned by the host, and remotes should use `Routes` and `Route` that work inside it. Two `BrowserRouter`s on one page fight over the URL and get out of sync.

A remote can still wrap itself in a `BrowserRouter` when it runs standalone, but not when the host renders it.

## 55: How can a remote run both standalone and inside the host?

Give the remote two entry points. The standalone one (`bootstrap.jsx`) adds the things the host normally provides, like a router and providers. The exposed one only exports the feature component.

```jsx
// bootstrap.jsx (standalone)
createRoot(document.getElementById("root")).render(
  <BrowserRouter>
    <ShopApp />
  </BrowserRouter>,
);
```

```js
// exposes in the remote's config
exposes: { './App': './src/ShopApp.jsx' },
```

## 56: Why does every micro frontend need its own port in development?

Each one is a separate app with its own dev server. The host needs a URL for each remote entry, for example `http://localhost:3001/remoteEntry.js` for shop and `http://localhost:3002/remoteEntry.js` for cart.

Fixed ports per app make the local config predictable for the whole team.

## 57: How do you run a host and its remotes locally?

Start every remote's dev server and then the host's dev server. In a monorepo, a tool like Nx or Turborepo can start them all with one command, and many teams add a script like:

```json
"scripts": {
  "dev": "concurrently \"npm:dev:*\"",
  "dev:shell": "npm --prefix shell run dev",
  "dev:shop": "npm --prefix shop run dev"
}
```

## 58: What is output.publicPath and why does it matter?

`publicPath` tells webpack where the app's chunks live. A remote's chunks must be loaded from the remote's own URL, not the host's. If `publicPath` is wrong, the host tries to load `shop`'s chunks from its own domain and gets 404 errors.

The safe setting is `publicPath: 'auto'`, which works out the path from the URL the remote entry was loaded from.

## 59: What does publicPath: 'auto' do?

It makes webpack figure out the base URL at runtime from the `<script>` that loaded the bundle (via `document.currentScript` or the import URL). So the same build works on `localhost`, staging and production without a rebuild.

For remotes it is the usual recommended value.

## 60: What does a basic remote webpack config look like?

```js
const { ModuleFederationPlugin } = require("webpack").container;
const deps = require("./package.json").dependencies;

module.exports = {
  output: { publicPath: "auto" },
  plugins: [
    new ModuleFederationPlugin({
      name: "shop",
      filename: "remoteEntry.js",
      exposes: {
        "./ProductList": "./src/ProductList.jsx",
      },
      shared: {
        react: { singleton: true, requiredVersion: deps.react },
        "react-dom": { singleton: true, requiredVersion: deps["react-dom"] },
      },
    }),
  ],
};
```

## 61: What does a basic host webpack config look like?

```js
const { ModuleFederationPlugin } = require("webpack").container;
const deps = require("./package.json").dependencies;

module.exports = {
  output: { publicPath: "auto" },
  plugins: [
    new ModuleFederationPlugin({
      name: "shell",
      remotes: {
        shop: "shop@http://localhost:3001/remoteEntry.js",
      },
      shared: {
        react: { singleton: true, requiredVersion: deps.react },
        "react-dom": { singleton: true, requiredVersion: deps["react-dom"] },
      },
    }),
  ],
};
```

## 62: What does the "shop@http://..." syntax in remotes mean?

The part before `@` is the global name of the remote's container (the remote's `name`), and the part after it is the URL of its remote entry. Module Federation loads the script from the URL and then looks for a global variable with that name.

So the name must match the `name` set in the remote's own config.

## 63: Can you use Module Federation with Vite?

Yes. The recommended plugin today is `@module-federation/vite`, from the Module Federation team. It uses the same option names (`name`, `exposes`, `remotes`, `shared`).

The older `@originjs/vite-plugin-federation` is still found in many tutorials, but it is a different plugin with its own behavior. For new projects prefer `@module-federation/vite`.

## 64: What does a Vite remote config look like?

```js
// vite.config.js
import { defineConfig } from "vite";
import react from "@vitejs/plugin-react";
import { federation } from "@module-federation/vite";

export default defineConfig({
  server: { port: 3001 },
  plugins: [
    react(),
    federation({
      name: "shop",
      filename: "remoteEntry.js",
      exposes: { "./ProductList": "./src/ProductList.jsx" },
      shared: { react: { singleton: true }, "react-dom": { singleton: true } },
    }),
  ],
});
```

## 65: What is Rspack and why is it popular for micro frontends?

Rspack is a webpack-compatible bundler written in Rust. It is much faster than webpack and supports most webpack config and plugins, including Module Federation, which is built in.

Teams with big webpack-based micro frontend setups often move to Rspack (or Rsbuild on top of it) to get faster builds without rewriting their config.

## 66: What is Rsbuild?

Rsbuild is a build tool on top of Rspack with sensible defaults, similar to how Vite sits on top of Rollup and esbuild. For React you add the React plugin, and for Module Federation you add `@module-federation/rsbuild-plugin`.

```js
import { defineConfig } from "@rsbuild/core";
import { pluginReact } from "@rsbuild/plugin-react";
import { pluginModuleFederation } from "@module-federation/rsbuild-plugin";

export default defineConfig({
  plugins: [
    pluginReact(),
    pluginModuleFederation({
      name: "shop",
      exposes: { "./ProductList": "./src/ProductList.tsx" },
      shared: ["react", "react-dom"],
    }),
  ],
});
```

## 67: What is mf-manifest.json?

It is a file that Module Federation 2.0 generates next to the remote entry. It describes the remote in JSON: its name, exposed modules, shared packages, the files for each module and where its types are.

Hosts can point to the manifest instead of `remoteEntry.js`. Tools like the Chrome DevTools extension and preloading use the extra info.

```js
remotes: {
  shop: 'shop@http://localhost:3001/mf-manifest.json',
},
```

## 68: What is the Module Federation runtime?

It is the part of Module Federation 2.0 that runs in the browser and does the real work: loading remote entries, resolving shared packages and returning modules. It is published as `@module-federation/runtime` and re-exported from `@module-federation/enhanced/runtime`.

You can call it directly from your code, which lets you load remotes that weren't known at build time.

## 69: What does loadRemote do?

`loadRemote` loads an exposed module from a remote at runtime, using the `remoteName/exposedName` id:

```js
import { loadRemote } from "@module-federation/enhanced/runtime";

const mod = await loadRemote("shop/ProductList");
const ProductList = mod.default;
```

It returns a promise, so in React you usually wrap it in `lazy`.

## 70: What does registerRemotes do?

`registerRemotes` adds remotes to the runtime after startup. It is useful when the list of remotes comes from an API or a config file:

```js
import {
  registerRemotes,
  loadRemote,
} from "@module-federation/enhanced/runtime";

registerRemotes([
  { name: "shop", entry: "https://shop.example.com/mf-manifest.json" },
]);

const { default: ProductList } = await loadRemote("shop/ProductList");
```

## 71: What is a dynamic remote?

A dynamic remote is one whose URL is not written into the build config. The host learns it at runtime, for example from a JSON file per environment, a feature flag service or an API.

It lets you use one host build for dev, staging and production, and lets teams change remote versions without rebuilding the host.

## 72: What is the difference between a static and a dynamic remote?

A static remote has its URL in the bundler config (`remotes: { shop: 'shop@https://...' }`). It is simple, but changing the URL needs a host rebuild.

A dynamic remote is registered at runtime (for example with `registerRemotes`). It is more flexible but needs code to load the config and handle errors.

## 73: Where should the list of remote URLs live in production?

Usually in a small JSON file or a config service that the host fetches at startup, for example `/mf-remotes.json`. Each environment has its own file, and a deployment pipeline updates it when a remote ships a new version.

This way the host build is the same in every environment.

## 74: What does lazy loading mean in a micro frontend setup?

It means a micro frontend's code is downloaded only when the user needs it, for example when they open its route. With Module Federation, remotes are lazy by default when you load them with dynamic `import()` or `loadRemote`.

It keeps the first page load fast even when the app has many micro frontends.

## 75: How can micro frontends communicate with each other?

Common options, from the most loosely coupled to the most tightly coupled:

- The URL (path and query params).
- Browser events (`CustomEvent` on `window`) or a small event bus.
- Props passed from the host to the remote component.
- A shared store loaded as a singleton (for example Zustand).
- `BroadcastChannel` or `localStorage` events for communication between tabs.

Keep it as small as you can. A lot of shared state is a sign the split is wrong.

## 76: How do you pass data from the host to a remote component?

The simplest way is props, like any React component:

```jsx
const Cart = lazy(() => import("cart/Cart"));

<Cart userId={user.id} onCheckout={() => navigate("/checkout")} />;
```

This works because the host and the remote share the same React. Treat the props as a public contract and keep them stable and documented.

## 77: How can a remote send an event to the host using CustomEvent?

```js
// in the remote
window.dispatchEvent(
  new CustomEvent("cart:item-added", { detail: { productId: 42 } }),
);
```

```jsx
// in the host
useEffect(() => {
  const handler = (e) => setCount((c) => c + 1);
  window.addEventListener("cart:item-added", handler);
  return () => window.removeEventListener("cart:item-added", handler);
}, []);
```

Prefix event names with the domain to avoid clashes.

## 78: What is an event bus?

An event bus is a small object that lets code publish named events and subscribe to them, without the sender knowing who listens. In micro frontends it is often a thin wrapper around `window` events or a tiny shared module.

It keeps apps loosely coupled, but you should document the events like an API, because nothing in the code checks that a listener exists.

## 79: Why is the URL a good way to share state between micro frontends?

The URL is already shared by everyone, survives a page reload and can be bookmarked or shared. Things like the current product id, search filters or page number fit well there.

Each micro frontend reads the parts it cares about. No extra library and no tight coupling is needed.

## 80: Can micro frontends share a React context?

Yes, if they render in the same React tree and use the same React copy, and the context object itself comes from the same module instance. That usually means the context is defined in a shared package marked as a singleton.

If each app bundles its own copy of the module that creates the context, they get two different context objects and the remote won't see the host's provider.

## 81: What is a shared library in Module Federation?

It is an npm package listed under `shared`. Instead of bundling it into every app, Module Federation loads it once and gives the same instance to all apps that ask for a compatible version.

Typical shared libraries are `react`, `react-dom`, `react-router`, a design system package and a state library.

## 82: Should you share every dependency?

No. Share the libraries that need a single instance (React, router, state, design system) and big ones that many apps use. Small utilities are often cheaper to just bundle.

Sharing everything adds runtime work, many small requests and version negotiation for packages where it doesn't matter.

## 83: How do you read the shared versions from package.json?

```js
const deps = require('./package.json').dependencies;

shared: {
  react: { singleton: true, requiredVersion: deps.react },
  'react-dom': { singleton: true, requiredVersion: deps['react-dom'] },
  'react-router': { singleton: true, requiredVersion: deps['react-router'] },
},
```

This keeps the federation config in sync with what you actually install.

## 84: What happens if the host and a remote have different React patch versions?

With `singleton: true`, only one copy is used, usually the highest registered version. If the other app's `requiredVersion` is `^19.1.0` and the chosen version is `19.2.x`, the range still matches and nothing is printed.

Patch and minor differences are normally safe. Different major versions are where real problems start.

## 85: What is the "Invalid hook call" error and how is it related to micro frontends?

React throws "Invalid hook call" when hooks are called outside a component, when rules of hooks are broken, or when there is more than one copy of React. In micro frontends the last cause is the usual one: the remote bundled its own React instead of using the shared one.

Check that `react` and `react-dom` are in `shared` with `singleton: true` in every app.

## 86: What is a micro frontend "contract"?

It is the agreed public interface between a micro frontend and the apps that use it: the exposed module names, the props they take, the events they fire and the routes they own.

Treat it like an API. Breaking it without a plan breaks other teams' apps in production.

## 87: What should a remote expose: a component, routes or a mount function?

- **A component** is the simplest and works well inside one React app.
- **Routes** let the remote own a whole section of the app.
- **A mount function** (`mount(el, props)`) works across frameworks and React versions, because the host doesn't depend on React to render it.

Choose based on how tightly the host and remote are coupled.

## 88: How do you style micro frontends without conflicts?

Use scoped styles so one app's CSS can't leak into another:

- CSS Modules, which generate unique class names.
- CSS-in-JS libraries with unique prefixes.
- A class prefix per app, for example `shop-` (or Tailwind's prefix option).
- Shadow DOM, when you use web components.

Avoid global selectors like `h1 { }` or `.button { }` inside a micro frontend.

## 89: What are CSS Modules and why do they help?

CSS Modules are CSS files where every class name is local by default. The bundler changes `.title` into something like `ProductCard_title__x7f2a`.

```jsx
import styles from "./ProductCard.module.css";

<h2 className={styles.title}>{name}</h2>;
```

Two micro frontends can both have a `.title` class without affecting each other.

## 90: What is Shadow DOM?

Shadow DOM is a browser feature that attaches a separate, hidden DOM tree to an element. Styles inside the shadow tree don't leak out, and page styles (except inherited properties like `color` and `font`) don't leak in.

It gives strong style isolation for web-component-based micro frontends, but it makes global themes and some libraries (like portals and modals) harder to use.

## 91: What is a monorepo and how does it relate to micro frontends?

A monorepo keeps many projects in one Git repository. Many micro frontend setups use one, with each app in its own folder, so it is easy to share code, keep versions aligned and run all apps locally.

It doesn't stop independent deployment. Each app can still have its own pipeline that runs only when its folder changes.

## 92: What is a polyrepo setup?

Each micro frontend lives in its own repository. Teams get full control over their repo, tools and release flow.

The cost is harder sharing of code, dependency versions that drift apart, and more work to test everything together.

## 93: What is Nx and how does it help with React micro frontends?

Nx is a monorepo tool. It has generators that create a React host and remotes with Module Federation already set up, a dependency graph, caching and "affected" commands that build or test only what changed.

```bash
npx nx g @nx/react:host apps/shell --remotes=shop,cart
```

## 94: What is Turborepo?

Turborepo is a build system for JavaScript monorepos. It runs scripts like `build`, `test` and `dev` across many packages with caching and correct ordering.

It doesn't set up Module Federation for you, but it is a common choice to run and build many micro frontends in one repo.

## 95: What does "team autonomy" mean in micro frontends?

It means a team can decide how to build and when to release its part without asking others. It includes its own backlog, code, pipeline and, within agreed limits, its own libraries.

Autonomy is never total. Things like the React version, design system and contracts still need agreement.

## 96: What is the "strangler fig" pattern?

It is a way to replace an old app step by step. You put a new host in front of the old app and move one route or feature at a time into new micro frontends. The old app keeps serving everything that hasn't been moved yet.

Over time the old app shrinks until you can turn it off.

## 97: How can micro frontends help migrate an old React app?

You can build new features as separate apps with the new stack (for example React 19 with Vite) while the old app keeps running. The host routes to old or new code based on the URL.

This avoids a risky "big bang" rewrite and lets you ship value during the migration.

## 98: How do you share a design system between micro frontends?

Publish it as an npm package, install it in every app and list it in `shared` with `singleton: true` so all apps use one instance at runtime.

```js
shared: {
  '@acme/ui': { singleton: true, requiredVersion: deps['@acme/ui'] },
},
```

Also share the CSS (or design tokens) so colors and fonts match.

## 99: What are design tokens?

Design tokens are named values for colors, spacing, fonts and so on, for example `--color-primary: #0055ff`. They are usually exposed as CSS variables.

If all micro frontends use the same tokens, a theme change in one place updates the whole app.

## 100: What is a fallback UI?

It is what you show while a micro frontend loads or when it fails, for example a spinner, a skeleton or a short "Not available right now" message.

Good fallbacks keep the page usable. Each remote should have both a loading fallback (`Suspense`) and an error fallback (error boundary).

## 101: What is a skeleton screen?

A skeleton screen is a placeholder that looks like the shape of the real content, for example gray boxes where text and images will appear. It is a nicer loading state than a spinner because the layout doesn't jump when the content arrives.

For remote widgets on a shared page, skeletons with a fixed size also stop layout shift.

## 102: Why should remote entry files not be cached for long?

The remote entry is the file that points to the current version of a remote's chunks. If browsers or a CDN cache it for a long time, users keep loading the old version after a deployment.

Serve `remoteEntry.js` (and `mf-manifest.json`) with `Cache-Control: no-cache` or a very short max age, and give the hashed chunks a long cache time.

## 103: Why do chunk files have hashes in their names?

A hash like `main.8f3a1c.js` changes whenever the content changes. That lets you cache the file "forever", because a new version always has a new name.

The remote entry, which has a fixed name, is the only file that must be revalidated.

## 104: What is CORS and why does it matter for remotes?

CORS (Cross-Origin Resource Sharing) is a browser rule about which origins may read responses from another origin. If a host on `app.example.com` loads remote code from `shop.example.com`, some requests (like fetching `mf-manifest.json` or loading module scripts) need the right `Access-Control-Allow-Origin` header.

If you see CORS errors when loading a remote, configure the remote's server or CDN to allow the host's origin.

## 105: How do you allow CORS on a webpack dev server for a remote?

```js
devServer: {
  port: 3001,
  headers: {
    'Access-Control-Allow-Origin': '*',
  },
},
```

Using `*` is fine locally. In production, list the real host origins instead.

## 106: Where are micro frontends usually hosted?

Most teams build them into static files and put them on a CDN or object storage (like S3 with CloudFront, Azure Blob Storage or Cloudflare). Each micro frontend has its own path or subdomain, for example `cdn.example.com/shop/`.

Since they are static files, hosting is cheap and each team can upload its files on its own.

## 107: What does "technology agnostic" mean in micro frontends?

It means the approach doesn't force every team to use the same framework. single-spa, web components and iframes are technology agnostic.

Module Federation itself is also framework neutral, but sharing components between apps only really works when they use the same framework.

## 108: Is it a good idea to mix many frameworks in one app?

Usually not. Every framework adds download size and runtime cost, and developers can't move easily between teams. Different frameworks also make shared components and a shared design system much harder.

Mixing frameworks is reasonable during a migration or when you integrate a product you bought. As a long-term plan, one framework is simpler.

## 109: What is a remote component?

It is a React component that lives in a remote app and is loaded into the host at runtime. From the host's point of view it is just a lazy component.

```jsx
const Reviews = lazy(() => import("reviews/ReviewList"));
```

## 110: What is a shell layout?

It is the frame the host draws around every page: header, navigation, footer and maybe a sidebar. Micro frontends render in the main content area.

Keeping the layout in the host avoids every team building its own header and makes the page look the same across sections.

## 111: Who should own the header and navigation?

Usually the platform or shell team. The navigation needs to know about all sections, and it is the most visible part of the app.

Some companies expose the header as its own micro frontend so it can be released separately, but it still has one owner.

## 112: What is a platform team?

It is a team that owns the shared parts of a micro frontend setup: the host, build tooling, CI templates, the design system, shared libraries and guidelines. Its job is to make the feature teams faster.

Without such a team, every team solves the same problems in a different way.

## 113: What is a feature team?

A feature team owns one business area end to end, for example "checkout", and the micro frontend for it. It usually also owns the related back-end services.

Micro frontends are a way to let feature teams work and release on their own.

## 114: What is Conway's Law?

Conway's Law says that the structure of a system tends to copy the communication structure of the organization that builds it. If you have three teams, you tend to get three parts.

Micro frontends use this on purpose: split the front-end the way the teams are split.

## 115: How do micro frontends affect bundle size?

They can make it worse if every app bundles its own copy of React and other libraries. They can also make it better than a monolith if each micro frontend is loaded only when needed.

Sharing the big libraries and lazy loading remotes are the two main tools to keep the size under control.

## 116: Can micro frontends be server-side rendered?

Yes, but it is harder than in a normal app. The server has to load remote code too, and the client has to hydrate the same markup. Module Federation 2.0 supports Node, and frameworks like Modern.js add SSR support for remotes.

Many teams start with client-side rendering for micro frontends and add SSR only where SEO or first load speed need it.

## 117: What is Next.js Multi-Zones?

Multi-Zones is a Next.js feature for splitting one domain into several Next.js apps. Each app (zone) serves a set of paths, and one app rewrites the other paths to the right zone.

It is server-side composition by route. Each zone is deployed on its own, but moving between zones is a full page load, not a client-side navigation.

## 118: Can you use Module Federation with Next.js?

There was a plugin, `@module-federation/nextjs-mf`, that worked with the Pages Router. It is no longer actively developed and doesn't support the App Router.

For new Next.js projects the Next.js team recommends Multi-Zones. If you need runtime component sharing, it is easier with a client-rendered React host or a framework that supports Module Federation directly, like Modern.js.

## 119: What is the difference between createRoot and ReactDOM.render?

`createRoot` (from `react-dom/client`) is the React 18+ way to start an app and turns on concurrent features. `ReactDOM.render` was the old API and was removed in React 19.

```jsx
import { createRoot } from "react-dom/client";

const root = createRoot(document.getElementById("root"));
root.render(<App />);
```

Old micro frontends that still use `ReactDOM.render` must be updated before moving to React 19.

## 120: Why is root.unmount() important for micro frontends?

When a micro frontend is mounted into a DOM node with its own `createRoot` (for example in single-spa or a web component), you must call `root.unmount()` when it is removed. Otherwise effects keep running, listeners stay attached and memory leaks.

## 121: What is a mount/unmount contract?

It is a framework-neutral way to expose a micro frontend: the remote exports a function that renders into a DOM element and returns a cleanup function.

```jsx
// exposed by the remote
import { createRoot } from "react-dom/client";
import App from "./App";

export function mount(el, props) {
  const root = createRoot(el);
  root.render(<App {...props} />);
  return () => root.unmount();
}
```

## 122: Can a micro frontend have its own React root?

Yes. With a mount function, single-spa or web components, each micro frontend calls `createRoot` on its own DOM node. It then has its own render tree.

The trade-off: context, error boundaries and Suspense from the host don't reach into that tree, and data must be passed as props or events.

## 123: What is the difference between a remote component and a remote app?

A remote component is a piece of UI rendered inside the host's React tree. It shares the host's context, router and React instance.

A remote app has its own root and its own providers (and maybe its own router). It is more isolated and easier to version, but harder to integrate.

## 124: What is Module Federation's bridge for React?

`@module-federation/bridge-react` is a helper from Module Federation 2.0 for loading a remote as a full app with its own root and router. The remote wraps its app with `createBridgeComponent`, and the host loads it with `createRemoteAppComponent`.

It handles mounting, unmounting, props and routing between the host and the remote app.

## 125: Why do teams use a monorepo tool's generators for micro frontends?

Setting up Module Federation by hand takes a lot of config: ports, remotes, shared packages, dev servers and TypeScript. Generators (for example in Nx) create a working host and remotes in minutes with the same structure everywhere.

That makes new remotes cheap to add and keeps them consistent.

## 126: What is a standalone mode for a remote?

It means the remote runs as a normal app on its own dev server, with its own `index.html`, router and mock data. Developers can work on it without starting the host.

This speeds up development and helps prove that the remote doesn't secretly depend on host internals.

## 127: What is a remote's "public API"?

It is everything other apps are allowed to use: exposed modules, component props, events and routes. Everything else is internal and may change at any time.

Keeping the public API small makes it easier to change the remote without breaking others.

## 128: What is the problem with deep imports from a remote?

A deep import means using a remote's internal file that wasn't meant to be public. With Module Federation you can only import exposed modules, which helps. But in a monorepo, apps can still import each other's source files directly.

That couples the apps at build time and destroys independent deployment. Use lint rules or module boundary checks to stop it.

## 129: What is semantic versioning and why does it matter here?

Semantic versioning (semver) uses `MAJOR.MINOR.PATCH`. A major bump means a breaking change, a minor bump adds features and a patch fixes bugs.

Module Federation uses semver ranges (`^19.0.0`) to decide if a shared package version is compatible. Remotes also use semver for their own contracts.

## 130: What does ^ mean in a version range?

`^19.1.0` means "19.1.0 or any newer version with the same major", so `>=19.1.0 <20.0.0`. It is the usual range for shared packages.

`~19.1.0` is stricter and allows only patch updates (`>=19.1.0 <19.2.0`).

## 131: How do micro frontends handle authentication?

Usually the host handles login and stores the session, often as a secure HTTP-only cookie or tokens handled by an auth library. Remotes get the user info or a way to get tokens from the host, through props, a shared auth module or a shared context.

Remotes should not each run their own login flow.

## 132: Where should the access token live in a micro frontend app?

Ideally in an HTTP-only cookie the browser sends automatically, so JavaScript can't read it. If you must use tokens in JavaScript, keep them in memory inside one shared auth module that remotes call, for example `getAccessToken()`.

Avoid putting tokens in `localStorage`, because any script on the page, including a compromised remote, can read it.

## 133: How do remotes call back-end APIs?

Each remote usually calls its own team's API (often through a backend-for-frontend). Shared concerns like the base URL, auth headers and error handling should come from a small shared HTTP helper or be passed by the host.

## 134: What is a Backend for Frontend (BFF)?

A BFF is a small back-end made for one front-end. It combines and shapes data from several services so the UI gets exactly what it needs.

In micro frontend setups each team often owns a BFF next to its micro frontend.

## 135: What is a feature flag?

A feature flag is a switch that turns a feature on or off at runtime without a deployment. In micro frontends, flags can decide which remote version to load, show a new widget to some users, or turn off a broken remote quickly.

## 136: Can each micro frontend use a different state library?

Yes, and that is often fine, because each team picks what works for its domain. Problems start only when state has to be shared between apps.

For shared state, agree on a small shared module or use events and the URL instead of forcing one global store.

## 137: Should you use one global Redux store for all micro frontends?

Usually no. One global store couples all teams: any change to its shape can break others, and every remote depends on the store setup in the host.

A better default is local state per micro frontend and a small, explicit shared layer for what is truly global, like the current user.

## 138: What is a shared singleton service?

It is a module that all micro frontends import from one shared package, so they get the same instance, for example an auth client, an analytics client or an event bus.

It works only if the package is in `shared` with `singleton: true`. Otherwise each app creates its own instance.

## 139: How do you add analytics to micro frontends?

Load the analytics library once (in the host) and give remotes a small shared API like `track(event, data)`. Agree on event names and common fields, such as which micro frontend sent the event.

This avoids several copies of the analytics script and messy, inconsistent data.

## 140: What is the role of index.html in a micro frontend setup?

The host's `index.html` is the page the user actually loads. It contains the root element and the host's scripts. Remotes' `index.html` files are used only when they run standalone.

In single-spa setups, the root `index.html` also contains the import map.

## 141: What does "loosely coupled" mean for micro frontends?

It means micro frontends know as little as possible about each other. They talk through small, stable contracts and can change their internals without the others noticing.

Loose coupling is what makes independent deployment safe.

## 142: What is a "distributed monolith"?

It is a system that is split into separate apps but still has to be released together, because the apps depend tightly on each other. You get all the complexity of micro frontends and none of the independence.

Common causes are a shared global store, deep imports and strict lockstep versions.

## 143: How do you show which micro frontend rendered a part of the page?

A simple trick is to add a `data-mfe="shop"` attribute on each remote's root element, or a dev-only outline. The Module Federation Chrome extension can also show which remotes and shared packages are loaded.

It helps a lot when a bug report says "the button is broken" and you need to know which team owns it.

## 144: What is the Module Federation Chrome DevTools extension?

It is a browser extension for Module Federation 2.0 apps. It shows the remotes and shared packages in the page, their versions and which app provided each shared package.

It can also override a remote's URL so you can point production to your local dev server for debugging.

## 145: What is the "dts" option in Module Federation 2.0?

`dts` controls automatic type generation. When on, a remote builds `.d.ts` files for its exposed modules and serves them as an archive. The host downloads them into a local `@mf-types` folder, so imports like `shop/ProductList` are fully typed.

It is on by default when the project has TypeScript set up.

## 146: How do you add type declarations for remotes by hand?

Create a `.d.ts` file in the host:

```ts
// src/remotes.d.ts
declare module "shop/ProductList" {
  import type { FC } from "react";
  const ProductList: FC<{ category?: string }>;
  export default ProductList;
}
```

It works, but the types can drift from the real code, so automatic types are better when available.

## 147: What does "exposes" path like './Button' mean?

The leading `./` is required by Module Federation. The host imports it as `remoteName/Button`, without the `./`.

```js
exposes: { './Button': './src/Button.jsx' }
// host
import('ui/Button');
```

## 148: How do you load a remote that exposes a named export?

`React.lazy` needs a default export. If the remote exposes a named one, map it:

```jsx
const ProductList = lazy(() =>
  import("shop/components").then((m) => ({ default: m.ProductList })),
);
```

## 149: What are good first steps when a remote fails to load?

Open the browser's Network tab and check:

- Did the remote entry load, or did it fail with 404, CORS or a timeout?
- Is the URL right for this environment?
- Do the chunk URLs point to the remote's origin (`publicPath`)?
- Are there console warnings about shared versions?

Most problems are wrong URLs, `publicPath` issues or shared version conflicts.

## 150: What should you say if asked "are micro frontends worth it?"

Say it depends on the team size and how independently teams need to release. For a few large teams on one product they can help a lot. For one team they usually add complexity without much gain.

Mention the costs too (setup, duplicate code, versioning, debugging) and that a modular monolith is often a good first step.

# Moderate Questions (151-300)

## 151: How does Module Federation pick a version for a shared package?

Every app registers the versions it can provide in the share scope. When code asks for a package, Module Federation looks for the highest registered version that fits the consumer's `requiredVersion`. For a singleton there is only one copy, so it picks one version and everyone uses it, even if it doesn't fit, in which case it warns (or throws with `strictVersion`).

In Module Federation 2.0 you can change this with `shareStrategy`.

## 152: What is shareStrategy in Module Federation 2.0?

It is a runtime option that controls how shared packages are chosen:

- `'version-first'` (the default) loads the remote entries of all remotes at startup so it can see every version and pick the best one.
- `'loaded-first'` uses a version that is already loaded if it fits, and doesn't load all remote entries up front.

`'loaded-first'` is lighter at startup and avoids failing early when a remote is down, but you may end up with a lower version than possible.

## 153: What happens to a shared package when a remote is offline under version-first?

With `version-first`, the runtime tries to load every remote's entry during startup to collect versions. If one remote is offline, that request fails, and depending on your setup it can slow or break startup.

That is one reason teams switch to `loaded-first` or add a runtime plugin that handles failed remote entries.

## 154: What does the import option in shared config do?

`import` says which module to use as the local fallback for the shared package. Setting `import: false` means "don't bundle this package at all, always use the one from the share scope".

```js
shared: {
  react: { singleton: true, import: false },
},
```

It is useful in remotes that should never bring their own React. But if no other app provides it, the remote breaks.

## 155: What does shareKey do?

`shareKey` is the name the package is registered under in the share scope. By default it is the package name. You can change it to share a package under another name, or to keep two variants apart.

It is rarely needed, but helps in unusual cases like aliasing a library.

## 156: What does packageName do in shared config?

`packageName` tells Module Federation which `package.json` to read for the version when it can't work it out from the import path, for example with deep imports or aliases.

## 157: How do you share a package's sub-paths like react/jsx-runtime?

Packages with sub-path imports need those paths shared too, or each app may bundle its own copy. The automatic JSX runtime imports `react/jsx-runtime`, so in some setups you list it explicitly:

```js
shared: {
  react: { singleton: true, requiredVersion: deps.react },
  'react/jsx-runtime': { singleton: true, requiredVersion: deps.react },
  'react-dom': { singleton: true, requiredVersion: deps['react-dom'] },
  'react-dom/client': { singleton: true, requiredVersion: deps['react-dom'] },
},
```

A trailing slash key like `'lodash/'` shares all sub-paths of a package in webpack.

## 158: What is the difference between eager sharing and the bootstrap pattern?

Eager sharing puts the shared package into the initial chunk so it can be used synchronously. It is easy, but it increases the entry size and that copy may be used even if a higher version exists elsewhere.

The bootstrap pattern keeps sharing async and only delays the start of the app by one dynamic import. It is the recommended default.

## 159: How does experiments.asyncStartup work in Module Federation 2.0?

With `experiments: { asyncStartup: true }`, the plugin makes the entry start asynchronously and waits for federation to be ready before running your code. You can import React at the top of `index.jsx` without adding a separate bootstrap file.

```js
new ModuleFederationPlugin({
  name: "shell",
  experiments: { asyncStartup: true },
  // ...
});
```

## 160: How do you load a dynamic remote with plain webpack 5 (without the 2.0 runtime)?

You load the script yourself and then use webpack's low-level container API:

```js
async function loadComponent(scope, module, url) {
  await loadScript(url); // adds a <script> tag and waits for onload
  await __webpack_init_sharing__("default");
  const container = window[scope];
  await container.init(__webpack_share_scopes__.default);
  const factory = await container.get(module);
  return factory();
}

const Mod = await loadComponent(
  "shop",
  "./ProductList",
  "https://shop.example.com/remoteEntry.js",
);
```

This is the legacy way. With Module Federation 2.0, `registerRemotes` and `loadRemote` do this for you.

## 161: How do you create a React component that loads a remote by URL at runtime?

```jsx
import { lazy, Suspense, useMemo } from "react";
import {
  registerRemotes,
  loadRemote,
} from "@module-federation/enhanced/runtime";

export function RemoteWidget({ name, entry, module, ...props }) {
  const Component = useMemo(() => {
    registerRemotes([{ name, entry }]);
    return lazy(() => loadRemote(`${name}/${module}`));
  }, [name, entry, module]);

  return (
    <Suspense fallback={<p>Loading...</p>}>
      <Component {...props} />
    </Suspense>
  );
}
```

Memoizing the lazy component is important. A new `lazy()` on every render would remount the remote each time.

## 162: Why must you not create a lazy component inside a render function without memoizing it?

Each call to `lazy()` creates a new component type. If you call it on every render, React sees a different type each time, throws away the old tree and mounts a new one. That loses state and can cause endless loading.

Create lazy components at module level, or memoize them by their inputs.

## 163: What is createInstance in the Module Federation runtime?

`createInstance` creates a separate federation runtime instance with its own name, remotes, shared packages and plugins:

```js
import { createInstance } from "@module-federation/enhanced/runtime";

const mf = createInstance({
  name: "shell",
  remotes: [
    { name: "shop", entry: "https://shop.example.com/mf-manifest.json" },
  ],
});

const mod = await mf.loadRemote("shop/ProductList");
```

It is the newer, recommended API. The older global `init` function is kept for compatibility.

## 164: How do you combine build-time and runtime remotes?

You can declare stable remotes in the bundler plugin's `remotes` option and register extra ones at runtime with `registerRemotes`. Both end up in the same runtime instance.

A common setup is to declare none at build time, load a JSON config at startup, and register all remotes from it.

## 165: What are runtime plugins in Module Federation 2.0?

Runtime plugins are objects with hooks that run during the federation lifecycle, for example before a remote is requested or when loading fails. You add them in the build config or at runtime:

```js
new ModuleFederationPlugin({
  name: "shell",
  runtimePlugins: ["./src/mf-plugins/offline-fallback.ts"],
});
```

They are used for retries, fallbacks, logging, auth headers and custom resolution of URLs.

## 166: How do you write a runtime plugin that shows a fallback when a remote fails?

```ts
import type { ModuleFederationRuntimePlugin } from "@module-federation/enhanced/runtime";

export default function offlineFallback(): ModuleFederationRuntimePlugin {
  return {
    name: "offline-fallback",
    errorLoadRemote({ id, error }) {
      console.error(`Failed to load ${id}`, error);
      return { default: () => null };
    },
  };
}
```

Returning a module from `errorLoadRemote` gives the host something to render instead of crashing.

## 167: Which runtime plugin hooks are commonly used?

- `beforeInit` to change options before the instance starts.
- `beforeRequest` to change the remote id or entry URL before loading.
- `afterResolve` to inspect or change the resolved remote info.
- `onLoad` after an exposed module is loaded.
- `errorLoadRemote` when loading a remote or module fails.
- `beforeLoadShare` and `resolveShare` to control which shared version is used.
- `createScript` to change how the script tag is created (for example adding attributes).

## 168: How can you rewrite remote URLs per environment with a runtime plugin?

```ts
export default function envUrls() {
  return {
    name: "env-urls",
    beforeRequest(args) {
      args.options.remotes.forEach((remote) => {
        if ("entry" in remote) {
          remote.entry = remote.entry.replace("{CDN}", window.__CDN_URL__);
        }
      });
      return args;
    },
  };
}
```

The build uses placeholders, and the real CDN URL is filled in at runtime.

## 169: How do you preload a remote?

Module Federation 2.0 has `preloadRemote`, which downloads a remote's entry and the assets of chosen exposes before they are needed:

```js
import { preloadRemote } from "@module-federation/enhanced/runtime";

preloadRemote([{ nameOrAlias: "shop", exposes: ["ProductList"] }]);
```

Call it on hover over a link or when the browser is idle, so the route opens instantly.

## 170: How can you preload a remote route on link hover?

Keep the import function in one place, use it for `lazy`, and call it on hover:

```jsx
const loadShop = () => import("shop/App");
const ShopApp = lazy(loadShop);

<Link to="/shop" onMouseEnter={loadShop}>
  Shop
</Link>;
```

The browser caches the module, so when `ShopApp` renders, it is already there.

## 171: How do you structure routes so a remote owns its sub-routes?

The host maps a path prefix to the remote, and the remote defines relative routes:

```jsx
// host
<Route path="/shop/*" element={<ShopApp />} />
```

```jsx
// remote: ShopApp.jsx
import { Routes, Route } from "react-router";

export default function ShopApp() {
  return (
    <Routes>
      <Route index element={<ProductList />} />
      <Route path=":productId" element={<ProductDetails />} />
    </Routes>
  );
}
```

Relative paths mean the remote doesn't care if it is mounted at `/shop` or `/store`.

## 172: How should a remote build links when it doesn't know its base path?

Use relative links, which React Router resolves against the current route:

```jsx
<Link to="123">Details</Link>      {/* /shop/123 */}
<Link to="..">Back to list</Link>
```

For links to other micro frontends, use absolute paths that are part of the agreed contract, like `/account/orders`.

## 173: How can a remote that has its own router stay in sync with the host's URL?

If the remote runs in its own root with its own router (for example a `MemoryRouter`), you sync both ways:

- The host passes the current path into the remote as a prop.
- The remote calls back (`onNavigate(path)`) when its route changes, and the host calls `navigate`.

The Module Federation React bridge does this for you. If you can, avoid two routers and share one instead.

## 174: Why would a remote use a MemoryRouter?

A `MemoryRouter` keeps the history in memory instead of the address bar. It is used when the remote has its own React root but must not touch the browser URL directly, for example in an embedded widget.

The host then decides how and if remote navigation shows up in the URL.

## 175: What is the basename option in React Router?

`basename` is a prefix that the router strips from and adds to every URL. A remote running standalone at `/` and inside the host at `/shop` can use it:

```jsx
<BrowserRouter basename="/shop">
  <ShopRoutes />
</BrowserRouter>
```

It is mainly useful when the remote owns its own router. With a shared router, use relative routes instead.

## 176: How do you share React Router between host and remotes?

List `react-router` as a singleton in every app's `shared` config. Then the remote's `Routes`, `Link` and hooks use the same router context the host created.

If the remote bundles its own copy, you get errors like "useNavigate() may be used only in the context of a Router component", because the remote's copy can't see the host's context.

## 177: How do you handle a 404 inside a remote's area?

Add a catch-all route in the remote:

```jsx
<Routes>
  <Route index element={<ProductList />} />
  <Route path=":id" element={<ProductDetails />} />
  <Route path="*" element={<NotFound />} />
</Routes>
```

The host has its own catch-all for unknown top-level paths. Both can reuse a shared `NotFound` component from the design system.

## 178: How do you lazy load routes from a remote with data routers?

With `createBrowserRouter`, the route's `lazy` function can load the remote module:

```jsx
import { createBrowserRouter, RouterProvider } from "react-router";

const router = createBrowserRouter([
  {
    path: "/",
    element: <Layout />,
    children: [
      { index: true, element: <Home /> },
      {
        path: "shop/*",
        lazy: async () => {
          const { default: Component } = await import("shop/App");
          return { Component };
        },
      },
    ],
  },
]);

createRoot(root).render(<RouterProvider router={router} />);
```

## 179: Can a remote expose route objects instead of a component?

Yes. The remote exports an array of route objects and the host adds them to its router with `patchRoutesOnNavigation` or by building the router after loading them.

```js
// remote: routes.jsx
export const routes = [
  { index: true, element: <ProductList /> },
  { path: ":id", element: <ProductDetails /> },
];
```

This gives the host one route tree, but it couples the remote to the host's router version and setup more tightly.

## 180: What is patchRoutesOnNavigation in React Router?

It is a data router option that lets you add routes lazily when the user navigates to a path that isn't known yet. It is useful for micro frontends because the host doesn't need to know all remote routes up front.

```jsx
const router = createBrowserRouter(baseRoutes, {
  async patchRoutesOnNavigation({ path, patch }) {
    if (path.startsWith("/shop")) {
      const { routes } = await import("shop/routes");
      patch("shop", routes);
    }
  },
});
```

`patch(routeId, children)` adds children to the route with that id.

## 181: How should the host build its navigation menu when remotes are dynamic?

Put menu entries into the remote config, not the host code. For example each entry in `mf-remotes.json` has a label, path, icon and permission. The host reads the config and renders the menu.

Then adding a new micro frontend only changes config, not the host.

## 182: How do you pass the current user to remotes?

Options:

- Props from the host to each remote component.
- A shared auth module (singleton) with `getUser()` and `onUserChange()`.
- A shared React context, if remotes render in the host's tree and the context comes from a shared package.

Props are the most explicit and the easiest to test.

## 183: How do you create a shared context package that works across remotes?

Put the context and its hook in a separate package, for example `@acme/session`, and share it as a singleton:

```jsx
// @acme/session
import { createContext, useContext } from "react";

export const SessionContext = createContext(null);
export const useSession = () => useContext(SessionContext);
```

```js
shared: { '@acme/session': { singleton: true, requiredVersion: '^1.0.0' } }
```

The host renders `<SessionContext value={session}>` and remotes call `useSession()`.

## 184: Why can a context provided by the host be undefined in a remote?

Usually because the host and remote use two different copies of the module that called `createContext`. Each copy creates its own context object, so the remote's `useContext` looks for a provider that doesn't exist.

Fix it by sharing that module as a singleton, and check that React itself is shared too.

## 185: How can you share a Zustand store between micro frontends?

Create the store in a shared package with the vanilla API and share the package as a singleton:

```js
// @acme/cart-store
import { createStore } from "zustand/vanilla";

export const cartStore = createStore((set) => ({
  items: [],
  add: (item) => set((s) => ({ items: [...s.items, item] })),
}));
```

```jsx
// any micro frontend
import { useStore } from "zustand";
import { cartStore } from "@acme/cart-store";

const count = useStore(cartStore, (s) => s.items.length);
```

## 186: Why share a store package and not let the remote expose the store?

Both work. A shared npm package is clearer: it has a version, types and tests, and any app can use it. A store exposed by one remote ties every other app to that remote being online and loaded first.

Either way, keep the shared store small. It is a contract between teams.

## 187: How can you use BroadcastChannel between micro frontends?

`BroadcastChannel` sends messages between tabs, windows and iframes from the same origin:

```js
const channel = new BroadcastChannel("auth");

channel.postMessage({ type: "logout" });

channel.onmessage = (e) => {
  if (e.data.type === "logout") window.location.assign("/login");
};
```

It is handy for logging out in all tabs or syncing state between iframe-based micro frontends.

## 188: How do you send data between a host and an iframe micro frontend?

Use `postMessage` and always check the origin:

```js
// host
iframe.contentWindow.postMessage(
  { type: "theme", value: "dark" },
  "https://shop.example.com",
);

// inside the iframe
window.addEventListener("message", (e) => {
  if (e.origin !== "https://app.example.com") return;
  if (e.data.type === "theme") setTheme(e.data.value);
});
```

## 189: How do you build a typed event bus for micro frontends?

```ts
type Events = {
  "cart:item-added": { productId: string; quantity: number };
  "auth:logout": undefined;
};

export function emit<K extends keyof Events>(type: K, detail: Events[K]) {
  window.dispatchEvent(new CustomEvent(type, { detail }));
}

export function on<K extends keyof Events>(
  type: K,
  fn: (d: Events[K]) => void,
) {
  const handler = (e: Event) => fn((e as CustomEvent<Events[K]>).detail);
  window.addEventListener(type, handler);
  return () => window.removeEventListener(type, handler);
}
```

Publish it as a shared package so all teams use the same event types.

## 190: How do you use an event bus inside a React component safely?

Subscribe in `useEffect` and return the unsubscribe function, so the listener is removed on unmount:

```jsx
useEffect(() => on("cart:item-added", () => setCount((c) => c + 1)), []);
```

Forgetting cleanup is a common source of duplicated handlers when a remote mounts and unmounts.

## 191: How would you sync state through the URL in a remote?

Use React Router's `useSearchParams`:

```jsx
import { useSearchParams } from "react-router";

function Filters() {
  const [params, setParams] = useSearchParams();
  const category = params.get("category") ?? "all";

  return (
    <select
      value={category}
      onChange={(e) => setParams({ category: e.target.value })}
    >
      <option value="all">All</option>
      <option value="shoes">Shoes</option>
    </select>
  );
}
```

Other micro frontends on the same page can read the same param.

## 192: When is passing callbacks as props a bad idea between host and remote?

When the remote has its own React root or lives in another framework, or when the callback must survive a remote being reloaded or replaced. Also when many remotes need the same event, because the host turns into a hub of glue code.

In those cases, events or a shared service are cleaner.

## 193: How do you share a design system without loading it twice?

- Install the same major version in all apps.
- Share it as a singleton with `requiredVersion` from `package.json`.
- Ship the CSS once (from the host) or make components inject their own scoped styles.
- Keep React and the styling library shared too, since the design system depends on them.

## 194: How do you handle CSS-in-JS libraries like Emotion in micro frontends?

Share the library as a singleton so there is one style cache and one theme context. If each remote has its own copy, class names can clash and the theme provider from the host won't reach remote components.

If remotes must stay separate, give each its own cache with a unique `key` (Emotion's `createCache({ key: 'shop' })`).

## 195: How do you use Tailwind CSS in micro frontends without class conflicts?

Two common approaches:

- All apps use the same Tailwind version and design tokens, and the host loads the CSS for all of them.
- Each app uses a prefix, so its classes can't clash. In Tailwind v4:

```css
@import "tailwindcss" prefix(shop);
```

```jsx
<div className="shop:flex shop:gap-4">...</div>
```

Also turn off or scope the preflight (base reset) in remotes, so they don't reset the host's styles.

## 196: Why can a remote's CSS reset break the host?

A CSS reset like Tailwind's preflight or `normalize.css` uses global selectors (`*`, `h1`, `button`). When a remote loads it, it changes elements all over the page, not only inside the remote.

Only the host should load a global reset. Remotes should ship scoped styles only.

## 197: How do you load a remote's CSS with Module Federation?

When a remote imports CSS in its components, the bundler creates CSS chunks and the federation runtime loads them together with the JS chunks. You don't need to add `<link>` tags by hand.

Check that the remote's `publicPath` is right, otherwise CSS files 404 even when JS loads.

## 198: What is CSS leakage on unmount?

When a remote is unmounted, styles it injected (with `<style>` or `<link>` tags) usually stay in the page. If those styles are global, they keep affecting the host after the user leaves that section.

Scoped styles (CSS Modules, prefixes) make leftover styles harmless.

## 199: How do you theme micro frontends consistently?

Use CSS variables (design tokens) set by the host on `:root` or a wrapper, and have all micro frontends read them:

```css
:root {
  --color-primary: #1d4ed8;
  --radius: 8px;
}

.button {
  background: var(--color-primary);
  border-radius: var(--radius);
}
```

CSS variables also pass into Shadow DOM, which makes them work with web components too.

## 200: How do you use React portals in micro frontends?

Portals render into a DOM node outside the component's parent, often `document.body`, for modals and tooltips. They still keep the React context of where they were created.

Agree on one portal target (for example a `#modal-root` from the host) and a shared z-index scale, otherwise modals from different remotes overlap badly.

## 201: How do you set up single-spa with a React host?

In single-spa there is usually no React host. The "root config" is a small plain JavaScript file that registers the apps and starts single-spa:

```js
import { registerApplication, start } from "single-spa";

registerApplication({
  name: "@acme/navbar",
  app: () => import("@acme/navbar"),
  activeWhen: ["/"],
});

registerApplication({
  name: "@acme/shop",
  app: () => import("@acme/shop"),
  activeWhen: ["/shop"],
});

start();
```

Each React app is then built with `single-spa-react` and mounted by single-spa.

## 202: What does activeWhen do in single-spa?

`activeWhen` decides when an app should be mounted. It can be a path prefix, an array of prefixes or a function:

```js
activeWhen: (location) => location.pathname.startsWith('/shop'),
```

When the URL changes, single-spa checks all apps, unmounts the ones that are no longer active and mounts the new ones.

## 203: What are customProps in single-spa?

`customProps` are extra values passed to an app's lifecycle functions. With `single-spa-react`, they reach the root component as props:

```js
registerApplication({
  name: "@acme/shop",
  app: () => import("@acme/shop"),
  activeWhen: "/shop",
  customProps: { authToken: getToken, apiUrl: "https://api.example.com" },
});
```

## 204: What is a single-spa parcel?

A parcel is a framework-neutral component that can be mounted manually anywhere, not based on routes. You use it for shared widgets, for example a React date picker inside a Vue app.

In React you can mount a parcel with the `Parcel` component from `single-spa-react/parcel`.

## 205: What is a single-spa utility module?

It is a module that doesn't render anything but shares code between apps, for example an auth client, an API helper or a style guide. It is loaded through the import map like any app, so all apps share one instance.

## 206: How does single-spa load apps in the browser?

Most single-spa setups use an import map with in-browser ES modules or SystemJS. The root config imports each app by name (`@acme/shop`), and the import map says which URL that name points to.

To release a new version, you update the URL in the import map. No other app needs a rebuild.

## 207: What is import-map-overrides?

It is a small library (often used with single-spa) that lets developers override import map entries in their own browser. You can point `@acme/shop` to `http://localhost:8080/acme-shop.js` while the rest of the app comes from production.

It makes local development and debugging of one micro frontend much easier.

## 208: How do you share React in a single-spa setup?

Mark React as external in each app's build and load it once through the import map:

```html
<script type="importmap">
  {
    "imports": {
      "react": "https://cdn.jsdelivr.net/npm/react@19.2.0/+esm",
      "react-dom/client": "https://cdn.jsdelivr.net/npm/react-dom@19.2.0/client/+esm"
    }
  }
</script>
```

Many teams now combine single-spa with Module Federation instead, so sharing uses version negotiation.

## 209: When would you choose single-spa over Module Federation?

When you need to run apps built with different frameworks side by side and want a clear mount/unmount lifecycle by route, or when you already have a single-spa platform.

When all apps use React and you mostly want to share components and libraries, Module Federation is simpler. The two can also be used together.

## 210: How do you create a React custom element that reacts to attribute changes?

```jsx
import { createRoot } from "react-dom/client";
import PriceTag from "./PriceTag";

class PriceTagElement extends HTMLElement {
  static observedAttributes = ["amount", "currency"];

  connectedCallback() {
    this.root = createRoot(this);
    this.render();
  }

  attributeChangedCallback() {
    if (this.root) this.render();
  }

  disconnectedCallback() {
    this.root?.unmount();
    this.root = null;
  }

  render() {
    this.root.render(
      <PriceTag
        amount={Number(this.getAttribute("amount"))}
        currency={this.getAttribute("currency")}
      />,
    );
  }
}

customElements.define("price-tag", PriceTagElement);
```

## 211: How does a React custom element send events to the page around it?

Dispatch a `CustomEvent` from the element itself:

```js
this.dispatchEvent(
  new CustomEvent("add-to-cart", {
    detail: { id },
    bubbles: true,
    composed: true,
  }),
);
```

`bubbles` lets parents catch it, and `composed` lets it cross Shadow DOM boundaries. Pass a callback into the React component that calls this.

## 212: How does React 19 handle props on custom elements?

React 19 added full support for custom elements. When you pass a prop to a custom element, React sets it as a property if the element has that property, otherwise as an attribute. So you can pass objects and arrays, not only strings.

In older React versions only string attributes worked, and you needed a ref to set properties and add event listeners.

## 213: How do you listen to custom element events from React?

A ref with `addEventListener` works in every React version:

```jsx
function Page() {
  const ref = useRef(null);

  useEffect(() => {
    const el = ref.current;
    const handler = (e) => console.log("added", e.detail.id);
    el.addEventListener("add-to-cart", handler);
    return () => el.removeEventListener("add-to-cart", handler);
  }, []);

  return <product-card ref={ref} product-id="42" />;
}
```

## 214: How do you render a React app inside Shadow DOM?

Attach a shadow root and render into a container inside it:

```jsx
class ShopWidget extends HTMLElement {
  connectedCallback() {
    const shadow = this.attachShadow({ mode: "open" });
    const container = document.createElement("div");
    shadow.appendChild(container);
    this.root = createRoot(container);
    this.root.render(<ShopApp />);
  }

  disconnectedCallback() {
    this.root.unmount();
  }
}
```

Remember that styles must be added inside the shadow root, not in the document head.

## 215: How do you get styles into a Shadow DOM micro frontend?

Options:

- Add a `<style>` or `<link rel="stylesheet">` element inside the shadow root.
- Use constructable stylesheets: `shadow.adoptedStyleSheets = [sheet]`.
- Configure your CSS-in-JS library to inject into the shadow root (Emotion's `createCache({ key, container: shadowRoot })`).

By default most bundlers inject CSS into `document.head`, which doesn't reach inside the shadow root.

## 216: What problems can React have inside Shadow DOM?

- Styles from bundlers and libraries go to `document.head` and don't apply.
- Portals to `document.body` render outside the shadow root and lose its styles.
- Some third-party libraries look up elements with `document.querySelector` and can't find them.
- Focus management and some accessibility tools behave differently.

Modern React handles events inside shadow roots fine, since it attaches listeners to the root container.

## 217: How do you pass a complex object to a React-based custom element?

Define a property setter on the element and re-render when it changes:

```js
class OrderSummary extends HTMLElement {
  set order(value) {
    this._order = value;
    this.render();
  }
  // ...
}
```

```jsx
// from React 19, this sets the property directly
<order-summary order={order} />
```

Attributes only hold strings, so use properties for objects and arrays.

## 218: How do you build an iframe micro frontend that resizes to its content?

The child measures its height and tells the parent:

```js
// inside the iframe
new ResizeObserver(() => {
  parent.postMessage(
    { type: "resize", height: document.body.scrollHeight },
    "https://app.example.com",
  );
}).observe(document.body);
```

```js
// in the host
window.addEventListener("message", (e) => {
  if (e.origin === "https://shop.example.com" && e.data.type === "resize") {
    iframe.style.height = `${e.data.height}px`;
  }
});
```

## 219: How do you handle routing for iframe-based micro frontends?

The host owns the browser URL. When the iframe navigates, it sends its path to the host with `postMessage`, and the host updates its URL (for example `/shop/123`). On page load, the host turns its URL into the iframe's `src`.

Without this sync, the back button and deep links don't work as users expect.

## 220: How do you integrate micro frontends at build time with npm packages?

Each team publishes its micro frontend as a package, and the host installs it:

```bash
npm i @acme/shop@2.3.0
```

```jsx
import { ShopApp } from "@acme/shop";
```

It is simple, gives full type checking and one optimized bundle. The downside is that every remote release needs a host release, so there's no independent deployment.

## 221: What should a build-time micro frontend package ship?

- Compiled ES modules and type definitions.
- React and other shared libraries as `peerDependencies`, not `dependencies`.
- CSS as a separate file or scoped styles.
- A clear public API from one entry point.

Keeping React as a peer dependency avoids duplicate React copies in the host.

## 222: Why should React be a peerDependency in micro frontend packages?

If a package lists React under `dependencies`, npm may install a separate copy for it, and you end up with two Reacts in the bundle. As a `peerDependency`, the package uses the React the host installed.

```json
"peerDependencies": {
  "react": "^19.0.0",
  "react-dom": "^19.0.0"
}
```

## 223: How do you run all micro frontends with Nx?

Nx's Module Federation setup lets you serve the host and its remotes with one command:

```bash
npx nx serve shell
```

By default it starts the host with a dev server and serves the remotes from built (cached) files. You pass `--devRemotes=shop` to run the remotes you are working on with hot reload.

## 224: How does Nx decide what to rebuild in a micro frontend monorepo?

Nx builds a project graph from imports and config. `nx affected -t build` compares your branch to the base branch and runs the target only for projects affected by the changed files.

With remote caching, unchanged projects are pulled from the cache, so CI stays fast as the number of micro frontends grows.

## 225: How do you enforce module boundaries in an Nx monorepo?

Tag projects in their config and use the `@nx/enforce-module-boundaries` lint rule:

```json
"@nx/enforce-module-boundaries": ["error", {
  "depConstraints": [
    { "sourceTag": "type:app", "onlyDependOnLibsWithTags": ["type:feature", "type:ui", "type:util"] },
    { "sourceTag": "scope:shop", "onlyDependOnLibsWithTags": ["scope:shop", "scope:shared"] }
  ]
}]
```

This stops one team's code from importing another team's internals.

## 226: How do you set up CI/CD so each micro frontend deploys on its own?

- One pipeline per micro frontend, triggered only by changes in its folder or repo.
- Build to a versioned folder on the CDN, for example `/shop/1.8.0/`.
- Run unit and contract tests.
- Update the remote config (or import map) to point to the new version.
- Run smoke tests against the composed app.

The host's pipeline is separate and runs only when the host changes.

## 227: Why deploy remotes to versioned folders?

If each build goes to its own folder (`/shop/1.8.0/remoteEntry.js`), old versions stay available. Rolling back is just pointing the config to the previous folder, with no rebuild.

It also lets you run two versions side by side for canary releases.

## 228: How do you roll back a broken remote?

If remotes are deployed to versioned folders and the host reads a config file, change the config to point to the last good version. The fix is live on the next page load.

If the URL is baked into the host build or the remote overwrites the same folder, rollback needs a new build or redeploy, which is slower.

## 229: What is a canary release for a micro frontend?

A canary release sends a new version to a small share of users first. The host (or an edge function) decides per user which remote URL to load, for example 5% get `/shop/1.9.0/` and the rest `/shop/1.8.0/`.

If errors go up, you switch everyone back. If not, you increase the share.

## 230: How do you test a remote component in isolation?

Test it like any React component with Vitest or Jest and React Testing Library. Provide what the host normally provides (router, providers, props):

```jsx
import { render, screen } from "@testing-library/react";
import { MemoryRouter } from "react-router";
import ProductList from "./ProductList";

test("shows products", async () => {
  render(
    <MemoryRouter>
      <ProductList category="shoes" />
    </MemoryRouter>,
  );
  expect(await screen.findByText("Running shoe")).toBeInTheDocument();
});
```

## 231: How do you test a host that imports remote modules?

In unit tests, the remote isn't available, so mock the import:

```js
// vitest
vi.mock("shop/ProductList", () => ({
  default: () => <div>Mock product list</div>,
}));
```

With Jest, use `moduleNameMapper` to point remote ids to a mock file:

```js
moduleNameMapper: { '^shop/(.*)$': '<rootDir>/__mocks__/remote.jsx' }
```

## 232: What are contract tests for micro frontends?

Contract tests check that a micro frontend still matches its agreed interface: exposed module names, props, events and URLs. The remote team runs them on every build, and the host team checks that it uses the contract correctly.

They catch breaking changes before deployment, which unit tests in each repo can't see.

## 233: How do you write a simple contract test for an exposed module?

Build the remote, load its exposed modules and check their shape:

```js
import * as ProductList from "../src/ProductList";

test("ProductList contract", () => {
  expect(typeof ProductList.default).toBe("function");
});
```

For props, shared TypeScript types published as a package are often the most practical contract: the host gets a type error if the remote changes them.

## 234: How do you run end-to-end tests across micro frontends?

Use Playwright or Cypress against the composed app (host plus real remotes) in a test or staging environment. Focus on a few key user flows that cross micro frontends, like "search, add to cart, check out".

Keep most tests inside each micro frontend. Cross-app E2E tests are slow and fragile, so keep them few.

## 235: How do you test a remote against the production host?

Use a URL override: a query param, a cookie, `import-map-overrides` or the Module Federation DevTools extension. The production host then loads your remote from a preview deployment or `localhost`.

This lets you test real integration without deploying to everyone.

## 236: What is the advantage of a preview environment per pull request?

Each PR of a remote gets its own deployed version. The team (and testers) can open the real host with that remote loaded through an override, before merging.

It catches integration problems early and makes reviews easier.

## 237: How do you handle environment variables in micro frontends?

Build-time variables (`process.env`, `import.meta.env`) get baked into each remote's bundle, which means a different build per environment. For independent deployments, prefer runtime config: a JSON file fetched at startup or values passed from the host.

That way the same build can move from staging to production.

## 238: Why is "build once, deploy many" important for micro frontends?

If each environment needs a separate build, what you tested in staging isn't exactly what runs in production. With runtime config, one build artifact is promoted through all environments.

It also makes rollbacks and canaries much simpler.

## 239: How do you share a runtime config with all remotes?

The host loads `config.json` at startup and passes the values down, or puts them in a small shared module:

```js
// @acme/config
let config;
export async function loadConfig() {
  config = await fetch("/config.json").then((r) => r.json());
}
export const getConfig = () => config;
```

Share `@acme/config` as a singleton so every remote sees the same values.

## 240: How do you debug a shared version mismatch?

- Read the console warnings from Module Federation. They name the package and versions.
- Use the Module Federation DevTools extension to see which app provided each shared package.
- In code, inspect `__FEDERATION__` (Module Federation 2.0) or `__webpack_share_scopes__` (webpack 5).
- Compare the `requiredVersion` in each app's config and lock file.

## 241: What does the warning "Unsatisfied version ... of shared singleton module" mean?

It means a singleton was already chosen in a version that doesn't match this app's `requiredVersion`. For example the host provides React 18.3 and a remote requires `^19.0.0`. The remote still gets 18.3, because there can be only one.

It is a warning by default. With `strictVersion: true` it becomes an error. Either way, align the versions.

## 242: Why do you sometimes see React loaded twice even with sharing configured?

Common causes:

- `react-dom/client` or `react/jsx-runtime` is not shared, so it pulls in a second React.
- One app uses an alias or a different package name.
- A dependency bundles React inside itself.
- Versions don't match and `singleton` is missing.

Check the Network tab for two React chunks and the DevTools extension for shared providers.

## 243: How do you add hot reload to a remote while it runs inside the host?

Both webpack and Rspack dev servers support HMR for remotes, but React Fast Refresh across app boundaries can be unreliable. Module Federation 2.0 has improved dev support, and some teams just reload the page after a remote change.

A practical setup: work on the remote in standalone mode with fast refresh, and test inside the host less often.

## 244: How do you handle a remote that is slow to load?

- Show a skeleton with the final size to avoid layout shift.
- Preload it on hover or when the browser is idle.
- Set a timeout and show a fallback if it takes too long.
- Check the remote's bundle size and its own lazy loading.

## 245: How do you add a timeout when loading a remote?

```js
function withTimeout(promise, ms) {
  return Promise.race([
    promise,
    new Promise((_, reject) =>
      setTimeout(() => reject(new Error("Remote timeout")), ms),
    ),
  ]);
}

const Reviews = lazy(() => withTimeout(import("reviews/ReviewList"), 8000));
```

The error boundary around `Reviews` shows the fallback if the timeout hits.

## 246: How do you retry loading a remote after it fails?

Wrap the import in a retry helper:

```js
async function retry(fn, times = 2, delay = 1000) {
  try {
    return await fn();
  } catch (err) {
    if (times === 0) throw err;
    await new Promise((r) => setTimeout(r, delay));
    return retry(fn, times - 1, delay * 2);
  }
}

const Reviews = lazy(() => retry(() => import("reviews/ReviewList")));
```

Note that some browsers cache a failed dynamic import of the same URL, so with plain ES modules a retry may need a cache-busting URL. Module Federation's runtime or a runtime plugin can also handle retries.

## 247: How can the user retry a failed remote from the UI?

With `react-error-boundary`, the fallback gets a `resetErrorBoundary` function:

```jsx
<ErrorBoundary
  fallbackRender={({ resetErrorBoundary }) => (
    <div>
      <p>Reviews could not be loaded.</p>
      <button onClick={resetErrorBoundary}>Try again</button>
    </div>
  )}
>
  <Suspense fallback={<Spinner />}>
    <Reviews />
  </Suspense>
</ErrorBoundary>
```

A `lazy` component remembers a rejected promise, so for a real retry you also need to create a new lazy component (for example with a `key` and a new import).

## 248: How do you log errors from micro frontends?

Send errors to one monitoring tool (like Sentry) and tag each error with the micro frontend that caused it. Use error boundaries' `onError` and a global `window.onerror` handler from the host.

```jsx
<ErrorBoundary
  fallback={<Fallback />}
  onError={(error) => monitor.captureException(error, { tags: { mfe: 'shop' } })}
>
```

Then each team can filter for its own errors.

## 249: How do you know which micro frontend version is running in production?

Have each remote expose or log its version, for example a `version` export, a meta tag or a field in `mf-manifest.json`. Add the version to error reports and analytics.

When a bug comes in, you know exactly which build of each remote the user had.

## 250: How do you handle source maps for remotes?

Each remote generates its own source maps and uploads them to the error monitoring tool with its version (release). Don't serve them publicly if you don't want your source to be visible.

Because remotes deploy separately, the upload must be part of each remote's pipeline, not the host's.

## 251: How do you measure the performance cost of micro frontends?

- Check Web Vitals (LCP, INP, CLS) for real users, split by route.
- Look at the Network tab: number of requests, remote entry size, duplicate libraries.
- Use bundle analyzers (`webpack-bundle-analyzer`, Rsdoctor) on each app.
- Compare against a budget per micro frontend.

## 252: What is a performance budget for a micro frontend?

It is a limit each team agrees to, for example "the shop remote must be under 150 KB gzipped JS on first load". Check it in CI and fail the build when a change goes over.

Without budgets, each team adds "just a bit" and the whole page gets slow.

## 253: What is Rsdoctor?

Rsdoctor is a build analysis tool for Rspack and webpack. It shows bundle content, duplicate packages, loader and plugin time, and Module Federation info.

It helps you find why a remote is big or why a shared package was bundled twice.

## 254: How do you avoid a "waterfall" when loading nested remotes?

A waterfall happens when the host loads remote A, A then loads remote B, and B loads C, one after another. Each step waits for the one before.

Avoid deep nesting, preload remotes you know will be needed, and use the manifest-based preloading in Module Federation 2.0 to fetch several remotes in parallel.

## 255: How can you reduce the size of the remote entry?

The remote entry should be small: just the container code and module map. Keep heavy code out of it by:

- Not marking big packages as `eager`.
- Keeping exposed modules lazy (they are loaded on `get`, not with the entry).
- Not adding app startup code to the entry.

## 256: How do you avoid layout shift when remote widgets load?

Reserve space for each widget before it loads: a fixed height, `min-height`, `aspect-ratio`, or a skeleton with the right size. When the widget arrives, it replaces the placeholder without moving other content.

Layout shift from late widgets is one of the most common CLS issues in micro frontend pages.

## 257: How do you share images and fonts between micro frontends?

Put them on a shared CDN path owned by the platform team and load fonts once from the host. Remotes reference them by absolute URL or through design tokens.

If each remote bundles the same fonts, the user downloads them several times.

## 258: How do you version a remote's exposed modules?

Options:

- Keep exposed names stable and evolve them in a backward-compatible way.
- Add new names for breaking versions, like `./ProductListV2`, and remove the old one later.
- Deploy versioned folders and let the host pin a major version in its config.

Most teams use the first one and add a new name only for real breaking changes.

## 259: How do you make a breaking change to a remote's props safely?

Add the new prop and keep the old one working (marked as deprecated) for a while. Tell the consuming teams, wait until they move, then remove the old prop in a later release.

This is the same "expand and contract" approach you use for APIs and database changes.

## 260: How do you share TypeScript types for remote contracts?

Two common ways:

- Module Federation 2.0's `dts` feature generates and downloads types automatically.
- A shared package (for example `@acme/shop-contract`) with the prop types and event types, used by both sides.

The shared package is more explicit and works with any integration method.

## 261: How do you configure dts in Module Federation 2.0?

```js
new ModuleFederationPlugin({
  name: "shop",
  exposes: { "./ProductList": "./src/ProductList.tsx" },
  dts: {
    generateTypes: true,
    consumeTypes: true,
  },
});
```

The host needs `"paths": { "*": ["./@mf-types/*"] }` in `tsconfig.json` so TypeScript finds the downloaded types.

## 262: Why might automatic type sharing fail in CI?

The host downloads types from the remote's URL during the build. In CI that URL may not be reachable, or the remote may not be deployed yet. Then the build fails or uses old types.

Common fixes: point to deployed remotes in CI, allow builds without fresh types (`abortOnError: false`), or commit generated types.

## 263: How do you handle i18n (translations) in micro frontends?

Usually the host decides the user's language and shares it with remotes (via props, a shared context or a shared i18n instance). Each remote owns and loads its own translation files, so it can change texts without the host.

Share the i18n library (for example `i18next` and `react-i18next`) as a singleton if remotes use the host's instance.

## 264: How can each remote load its own translations with i18next?

Use namespaces per remote:

```js
import i18n from "i18next";

export async function loadShopTranslations(lang) {
  const res = await fetch(`https://cdn.example.com/shop/locales/${lang}.json`);
  i18n.addResourceBundle(lang, "shop", await res.json(), true, true);
}
```

```jsx
const { t } = useTranslation("shop");
```

Namespaces keep keys from different teams from clashing.

## 265: How do you handle accessibility across micro frontends?

- Use the shared design system, which should be accessible by default.
- Agree on page structure: one `<h1>`, landmarks (`<header>`, `<main>`, `<nav>`) owned by the host.
- Manage focus on route changes, for example move focus to the main heading.
- Run automated checks (axe) in each remote and on the composed page.

## 266: Who should manage focus after a navigation between micro frontends?

Usually the host, since it knows when the route changes. After a remote loads, focus should move to the main content or its heading, and screen readers should hear the new page title.

If every remote does this its own way, keyboard users get an inconsistent experience.

## 267: How do you set the document title in micro frontends?

In React 19 you can render `<title>` in any component, and React puts it in the `<head>`:

```jsx
function ProductPage({ product }) {
  return (
    <>
      <title>{`${product.name} | Acme Shop`}</title>
      <h1>{product.name}</h1>
    </>
  );
}
```

Agree on a title format so pages from different teams look the same in the browser tab.

## 268: How do you load data in a remote component?

The remote fetches its own data, usually from its own API, with whatever it prefers (`fetch`, TanStack Query, the data router's loaders). The host should not fetch data for remotes, because that couples them.

If several remotes need the same data, share a small client module or cache to avoid double requests.

## 269: How do you share one TanStack Query client between micro frontends?

Share `@tanstack/react-query` as a singleton and let the host create the `QueryClient` and the provider. Remotes then use `useQuery` with the host's client and share its cache.

If you want teams fully isolated, give each remote its own `QueryClient` and provider. Then caches are separate, which is simpler but may double some requests.

## 270: How do you prevent query key collisions in a shared query cache?

Prefix keys by domain or remote:

```js
useQuery({ queryKey: ["shop", "products", category], queryFn: fetchProducts });
```

Treat any keys that are shared on purpose (like `['session', 'user']`) as part of the contract.

## 271: How do you use the React 19 use hook with remote data?

`use` reads a promise inside a component and suspends until it resolves. The promise must be created outside the render (or cached), not inside the component:

```jsx
import { use } from "react";

function Reviews({ reviewsPromise }) {
  const reviews = use(reviewsPromise);
  return reviews.map((r) => <p key={r.id}>{r.text}</p>);
}
```

The host can start the request early and pass the promise down, so loading the remote code and the data happen in parallel.

## 272: How do Suspense boundaries help with several remotes on one page?

Each remote can have its own `Suspense` boundary so it shows its own fallback and appears as soon as it is ready. Or you group remotes in one boundary so they appear together and the page doesn't "pop in" piece by piece.

Choose based on what looks better to users. Nested boundaries give you both.

## 273: What is SuspenseList and can you use it?

`SuspenseList` was an experimental React component for controlling the order in which Suspense boundaries reveal their content. It is not part of stable React 19.

In stable React you control reveal order by how you nest and group `Suspense` boundaries.

## 274: How do you handle transitions when switching between remotes?

Wrap the navigation in `startTransition` (React Router does this for its navigations). Then React keeps showing the old page while the new remote loads, instead of showing a fallback right away.

```jsx
import { startTransition } from "react";

startTransition(() => setSection("shop"));
```

Use `useTransition` to get an `isPending` flag for a small loading indicator.

## 275: How do you share feature flags with remotes?

Load flags once in the host (from a flag service) and expose them through a shared module or context with a simple API like `isEnabled('new-checkout')`. Remotes shouldn't each start their own flag client.

Also use flags at the host level to pick which remote or version to load.

## 276: How can you A/B test two versions of a remote?

The host or an edge function assigns the user to a group and loads a different remote URL or exposed module for each group:

```js
const entry =
  user.group === "B"
    ? "https://cdn.example.com/shop/2.0.0/mf-manifest.json"
    : "https://cdn.example.com/shop/1.9.0/mf-manifest.json";

registerRemotes([{ name: "shop", entry }]);
```

Track the group in analytics so you can compare results.

## 277: How do you handle permissions for micro frontends?

The host knows the user's roles and decides which sections to show in the menu and routes. Each remote also checks permissions for its own features, because the host's checks are only UI.

Real authorization must happen on the server. UI checks only hide what the user can't use.

## 278: How do you protect a remote route that needs login?

Wrap the route in a guard component in the host:

```jsx
function RequireAuth({ children }) {
  const { user } = useSession();
  const location = useLocation();
  if (!user) return <Navigate to="/login" state={{ from: location }} replace />;
  return children;
}

<Route
  path="/account/*"
  element={
    <RequireAuth>
      <AccountApp />
    </RequireAuth>
  }
/>;
```

With this guard, the remote code isn't loaded for users who aren't logged in.

## 279: How do you share an authenticated fetch helper?

Put it in a shared package so every remote adds the token and handles 401 errors the same way:

```js
// @acme/http
import { getAccessToken, logout } from "@acme/auth";

export async function apiFetch(url, options = {}) {
  const token = await getAccessToken();
  const res = await fetch(url, {
    ...options,
    headers: { ...options.headers, Authorization: `Bearer ${token}` },
  });
  if (res.status === 401) logout();
  return res;
}
```

## 280: How do you handle logout across all micro frontends?

The host (or shared auth module) clears the session, emits a `logout` event, and redirects. Remotes listen for the event to clear their own caches and state. Use `BroadcastChannel` to log out other tabs too.

Since most remotes are unmounted after the redirect, clearing shared caches (like the query cache) is the important part.

## 281: How do you choose between Module Federation, single-spa and web components?

- **Module Federation**: all apps use React, you want to share components and libraries, and you want good performance.
- **single-spa**: several frameworks, route-based apps, or an existing single-spa platform.
- **Web components**: you need to embed React widgets in pages you don't control, or in other frameworks.

They can be combined, for example single-spa for app lifecycles and Module Federation for loading and sharing.

## 282: How do you migrate from @originjs/vite-plugin-federation to @module-federation/vite?

- Replace the plugin import and check the option names (they are close but not the same).
- Remote entries change from a plain URL to `{ type: 'module', name, entry }` in the host.
- Test shared packages carefully, because the sharing behavior is different.
- Update any code that used the old plugin's virtual modules or helpers.

Move one app at a time and test the host with mixed remotes.

## 283: How does a Vite host load a remote in @module-federation/vite?

```js
federation({
  name: "shell",
  remotes: {
    shop: {
      type: "module",
      name: "shop",
      entry: "http://localhost:3001/remoteEntry.js",
    },
  },
  shared: { react: { singleton: true }, "react-dom": { singleton: true } },
});
```

Then `import('shop/ProductList')` works like with webpack.

## 284: Can a webpack host load a Vite remote?

Yes, if both use Module Federation 2.0 compatible plugins. `@module-federation/vite` produces a remote entry that the Module Federation runtime understands, so webpack, Rspack and Vite apps can load each other.

Check that shared packages are configured the same way on both sides and test it, since mixed setups have more edge cases.

## 285: Why is the remote entry of a Vite remote an ES module?

Vite builds ES modules, so its remote entry is loaded with `import()` instead of a classic `<script>` tag. That's why the host config uses `type: 'module'` for Vite remotes.

Webpack remote entries are usually classic scripts that define a global variable, though webpack can also output ES modules.

## 286: What is the library option in ModuleFederationPlugin?

`library` sets how the remote container is exposed, for example as a global variable (`var`), an ES module (`module`) or SystemJS (`system`):

```js
new ModuleFederationPlugin({
  name: "shop",
  filename: "remoteEntry.js",
  library: { type: "module" },
});
```

The host must load it the matching way. `var` is the default and the most common.

## 287: How do you use Module Federation with single-spa?

Each app is a remote that exposes its single-spa lifecycles. The root config loads them through federation instead of an import map:

```js
registerApplication({
  name: "shop",
  app: () => import("shop/spa"),
  activeWhen: "/shop",
});
```

You get single-spa's lifecycle and routing plus Module Federation's sharing.

## 288: How do you organize folders in a React micro frontend monorepo?

A common layout:

```
apps/
  shell/
  shop/
  cart/
packages/
  ui/          (design system)
  auth/        (shared auth client)
  contracts/   (shared types and events)
  config/      (shared build config)
```

Apps never import each other directly. They only use `packages/*` and remote modules.

## 289: How do you share webpack or Rspack config between micro frontends?

Put a function in a shared package that returns the common config, and let each app pass its own options:

```js
// packages/config/mf.js
module.exports = function mfConfig({ name, exposes = {}, remotes = {} }) {
  const deps = require(process.cwd() + "/package.json").dependencies;
  return {
    name,
    filename: "remoteEntry.js",
    exposes,
    remotes,
    shared: {
      react: { singleton: true, requiredVersion: deps.react },
      "react-dom": { singleton: true, requiredVersion: deps["react-dom"] },
    },
  };
};
```

It keeps sharing rules the same everywhere.

## 290: How do you keep dependency versions aligned across micro frontends?

- In a monorepo, use one root `package.json` or a tool that checks versions (syncpack, pnpm catalogs).
- In polyrepos, use Renovate or Dependabot with grouped updates for React and shared packages.
- Have the platform team announce and plan major upgrades.
- Fail CI if a shared singleton version is outside the agreed range.

## 291: What are pnpm catalogs and how do they help?

pnpm catalogs let you define dependency versions once in `pnpm-workspace.yaml` and refer to them in each package:

```yaml
catalog:
  react: ^19.2.0
  react-dom: ^19.2.0
```

```json
"dependencies": { "react": "catalog:", "react-dom": "catalog:" }
```

All micro frontends in the monorepo then use the same React version.

## 292: How do you upgrade React across many micro frontends?

- Make the host and all remotes work with both versions where possible (allow `^18.3.0 || ^19.0.0` in `requiredVersion` during the move).
- Upgrade remotes first, while the host still provides the old version, and fix warnings.
- Then upgrade the host so the new version is shared.
- Remove the old range when all apps are done.

If a clean shared upgrade isn't possible, isolate the slow apps with their own React root for a while.

## 293: How do you handle a remote that must stay on an older React version?

Load it with its own React and its own root, not as a shared component. Expose a `mount(el, props)` function or wrap it as a web component, and don't share `react` with it.

The page loads two Reacts until that remote is upgraded, so treat it as temporary.

## 294: How do you remove a micro frontend that is no longer needed?

- Remove its routes and menu entries from the host config.
- Redirect its URLs to the new place.
- Check that no other app imports its exposed modules or listens to its events.
- Keep the deployed files for a short time for users with old tabs open, then delete them.

## 295: What are the trade-offs of putting the header in the host vs a separate remote?

In the host, the header is always available and fast, and there is no extra request. But changes to it need a host release.

As a remote, the header team can release on its own, but if it fails to load, every page loses its navigation. Many teams keep it in the host or load it with a strong fallback.

## 296: How does a micro frontend handle global keyboard shortcuts?

Shortcuts like "Ctrl+K for search" should be owned by the host or one shared module, so remotes don't register the same keys. Remotes register shortcuts only while they are mounted and remove them on unmount.

A shared shortcut registry helps catch conflicts during development.

## 297: How do you keep a consistent loading experience across remotes?

Provide shared fallback components (skeletons, spinners, error cards) in the design system and use them in the host's `Suspense` and error boundaries. Agree on when to show a full-page loader vs a small one.

Users notice when each section loads in a different way.

## 298: How do you log which remotes and versions a user loaded?

A runtime plugin can record each loaded remote:

```ts
export default function loadLogger() {
  return {
    name: "load-logger",
    onLoad(args) {
      analytics.track("mf_loaded", { id: args.id });
      return args;
    },
  };
}
```

Attach remote names and versions to error reports, so you can match bugs to deployments.

## 299: What should a remote do when the host passes invalid props?

Fail softly: use default values, log a warning and render something sensible instead of crashing. Validate important inputs at the boundary (for example with TypeScript plus a runtime check like Zod for data from outside).

The remote can't trust that every host version passes exactly what it expects.

## 300: How do you document a micro frontend's contract?

Keep a short README or doc page per remote with:

- Exposed modules and their props (with types).
- Events it emits and listens to.
- Routes it owns.
- Required shared packages and versions.
- Owner team and contact.

Generating parts of it from TypeScript types keeps it accurate.

# Advanced Questions (301-450)

## 301: How does Module Federation work under the hood when a host imports a remote module?

At build time, the bundler turns `import('shop/ProductList')` into a call to the federation runtime instead of a normal chunk load. At runtime:

1. The runtime loads the remote entry (or manifest) for `shop`.
2. It initializes the remote's container with the share scope, so both sides register their shared packages.
3. It calls `container.get('./ProductList')`, which loads the module's chunks from the remote's origin and returns a factory.
4. Calling the factory runs the module, and shared imports inside it are resolved from the share scope.

## 302: What do the container's init and get methods do?

`init(shareScope)` connects the remote to the host's share scope. The remote adds the versions it can provide and from then on resolves its shared imports from that scope.

`get(moduleName)` returns a promise of a factory for an exposed module. It loads only that module's chunks, not the whole remote.

## 303: Why is the remote entry small even when the remote app is big?

The remote entry only contains the container code, the map of exposed modules to chunk ids, and the shared package info. Feature code lives in separate chunks that are loaded when `get` is called.

This is why a host can know about many remotes without paying for their code until it needs them.

## 304: What is the global `__FEDERATION__` object?

In Module Federation 2.0 the runtime keeps its state in a global `__FEDERATION__` object: the runtime instances, loaded remotes, shared packages and their versions. It lets several builds in the same page work with one shared state.

It is useful for debugging, but don't depend on its structure in app code, since it is internal.

## 305: How does the share scope handle two versions of a non-singleton package?

Both versions are registered. Each consumer gets the highest version that matches its own `requiredVersion`. If nothing matches, the consumer uses its own bundled fallback copy.

So you can end up with two versions of a library in one page, which is fine for stateless utilities but wrong for anything with global state.

## 306: What are the risks of singleton sharing with loose version ranges?

With a singleton, everyone uses one version even if it is outside their range (with only a warning). A remote built and tested against React 19.2 might run on 19.0 because the host provides it, and use an API that doesn't exist there.

Mitigations: `strictVersion` for critical packages, version alignment checks in CI, and testing remotes against the versions the host actually provides.

## 307: Which app's shared version wins when several provide the same singleton?

By default, the runtime uses the highest version that was registered before the package was first loaded. Which versions are registered depends on which remote entries have been initialized at that moment.

With `shareStrategy: 'version-first'`, the runtime initializes all remote entries up front, so the highest version among all apps wins. With `'loaded-first'`, whatever is already loaded (usually the host's) wins.

## 308: Why can the result of shared version selection change between page loads?

Because it depends on timing. If a remote entry is initialized before or after React is first used, the set of registered versions differs. Network speed, caching and user navigation can change this order.

That makes bugs hard to reproduce. Make loading order deterministic (version-first or host-provided singletons with `import: false` in remotes) for packages where it matters.

## 309: How can you force all remotes to use the host's React?

In each remote, set `import: false` for React so it never bundles its own copy and always uses the share scope:

```js
shared: {
  react: { singleton: true, import: false, requiredVersion: '^19.0.0' },
  'react-dom': { singleton: true, import: false, requiredVersion: '^19.0.0' },
}
```

The trade-off is that the remote can't run without a host that provides React, so the standalone dev setup needs its own config.

## 310: How would you use a runtime plugin to control which shared version is used?

The `resolveShare` hook lets you change the chosen version:

```ts
export default function preferHostReact() {
  return {
    name: "prefer-host-react",
    resolveShare(args) {
      const { shareScopeMap, scope, pkgName } = args;
      if (pkgName !== "react" && pkgName !== "react-dom") return args;
      const versions = shareScopeMap[scope][pkgName];
      const hostVersion = Object.keys(versions).find(
        (v) => versions[v].from === "shell",
      );
      if (hostVersion) args.resolver = () => versions[hostVersion];
      return args;
    },
  };
}
```

Use this only for special cases. The default rules are usually enough.

## 311: What is the tree-shaking problem with shared packages?

A shared package has to be the full package, because the runtime doesn't know which exports each consumer needs. So sharing a big library like `lodash` or an icon set can ship far more code than any single app uses.

Module Federation 2.0 has work on tree-shaking for shared packages, but the safe approach is to share only libraries that really need one instance and let bundlers tree-shake the rest locally.

## 312: How do you decide between sharing a library and bundling it?

Share it if:

- It must be a single instance (React, router, state, context-based libraries).
- It is large and used by most apps in the same version.

Bundle it if:

- It is small or tree-shakes well.
- Only one or two apps use it.
- Apps need different major versions.

## 313: How does Module Federation 2.0's manifest improve loading?

The manifest lists each exposed module's JS and CSS files and the shared packages. With it, the runtime can preload all assets of a module in parallel, instead of discovering chunks one by one.

It also gives tools (DevTools, type sharing, SSR) a standard description of the remote without running its code.

## 314: What is the cost of version-first share strategy at startup?

Version-first loads the remote entry of every known remote when the app starts, even remotes the user may never open. With many remotes, that's many requests before the first render, and a failing remote can slow startup.

For apps with many remotes, `loaded-first` plus careful version alignment is often a better choice.

## 315: How would you design remote discovery for 50 micro frontends?

- A registry service (or JSON in a CDN) lists each remote with name, manifest URL, version, routes, menu entries and permissions.
- The deployment pipeline of each remote updates its registry entry.
- The host fetches the registry at startup (cached at the edge), registers remotes lazily, and only loads entries for routes the user visits.
- The registry supports environments, canaries and per-user overrides.

Keep the registry small and fast. It's on the critical path of every page load.

## 316: How do you make the remote registry fail safe?

- Cache the last known good registry in the host's build or in the CDN.
- If the fetch fails, fall back to that copy.
- Validate the registry's shape before using it, and ignore broken entries instead of failing everything.
- Monitor registry errors separately.

## 317: How would you implement per-user remote overrides for testing in production?

The host checks a signed cookie or a query parameter (allowed only for internal users) and replaces matching registry entries:

```js
function applyOverrides(remotes) {
  if (!isInternalUser()) return remotes;
  const overrides = JSON.parse(localStorage.getItem("mf-overrides") ?? "{}");
  return remotes.map((r) =>
    overrides[r.name] ? { ...r, entry: overrides[r.name] } : r,
  );
}
```

Restrict which origins an override can point to. Otherwise it becomes a way to inject any script into your app.

## 318: Why are remote overrides a security risk?

An override lets someone change which JavaScript runs in your app. If any user can set it (for example through a public query parameter), an attacker can send a link that loads their own script with full access to the page and the user's session.

Allow overrides only for authenticated internal users, only to allowed origins, and never through plain URL params in production.

## 319: How do you secure micro frontends that load code from other origins?

- Load remotes only from allowed origins listed in a Content Security Policy.
- Serve everything over HTTPS.
- Protect the remote registry and CDN buckets: only CI can write to them.
- Use Subresource Integrity where the URLs are fixed.
- Review third-party remotes like any other dependency.

Every remote has full access to the page. One compromised remote compromises the whole app.

## 320: How do you write a Content Security Policy for a micro frontend app?

List each origin that serves remote code in `script-src`, and the API origins in `connect-src`:

```
Content-Security-Policy:
  default-src 'self';
  script-src 'self' https://cdn.example.com;
  style-src 'self' https://cdn.example.com;
  connect-src 'self' https://api.example.com https://cdn.example.com;
  img-src 'self' https://cdn.example.com data:;
```

Avoid `'unsafe-eval'`. Some older federation setups and tools need it, so check your setup works without it.

## 321: Can you use Subresource Integrity with Module Federation?

Partly. SRI requires knowing the hash of the file when you write the script tag. For static, versioned remotes you can store hashes in the registry and add `integrity` attributes, for example through the runtime's `createScript` hook.

For chunks loaded inside the remote, the remote's own build must add the hashes (webpack and Rspack have SRI plugins). It is more work than in a normal app and many teams rely on a locked-down CDN instead.

## 322: How do you add an integrity attribute to remote entry scripts?

With a Module Federation 2.0 runtime plugin:

```ts
export default function sriPlugin(hashes: Record<string, string>) {
  return {
    name: "sri",
    createScript({ url }) {
      const integrity = hashes[url];
      if (!integrity) return;
      const script = document.createElement("script");
      script.src = url;
      script.integrity = integrity;
      script.crossOrigin = "anonymous";
      return script;
    },
  };
}
```

The hashes come from the registry, which is written by each remote's CI.

## 323: How do Trusted Types affect micro frontends?

Trusted Types is a browser feature that blocks dangerous DOM sinks (like `innerHTML` or setting `script.src`) unless the value passes through an approved policy. Script loaders, including federation runtimes, set `script.src`, so they need a policy that allows your remote origins.

Turn on Trusted Types in report-only mode first to see what breaks across all remotes.

## 324: How do you limit what a third-party micro frontend can do?

Don't load it with Module Federation into your page, because it would get full access. Use an iframe with the `sandbox` attribute and a separate origin, and talk with it only through `postMessage` with a small, validated set of messages.

```html
<iframe
  src="https://partner.example.net/widget"
  sandbox="allow-scripts allow-forms"
></iframe>
```

## 325: Why does every remote have full access to the page in Module Federation?

Remote code runs in the same JavaScript context as the host. It can read the DOM, cookies that aren't HTTP-only, `localStorage`, global variables and in-memory tokens, and it can patch global objects.

Module Federation gives code-sharing, not isolation. Only load remotes you trust as much as your own code.

## 326: How do you design auth so a compromised remote does less damage?

- Use HTTP-only, `Secure`, `SameSite` cookies so scripts can't read the session.
- Keep tokens short-lived and narrowly scoped.
- Use a BFF that adds tokens on the server, so the browser never sees them.
- Use CSP to limit where scripts can send data (`connect-src`).

## 327: What is the risk of shared mutable globals between remotes?

If remotes use globals like `window.store` or patch shared objects (like `fetch` or `Array.prototype`), one team's change can break another team in ways that are hard to find. Two remotes can also overwrite each other's globals.

Use explicit shared modules with versions instead of globals, and lint against patching built-ins.

## 328: How do you prevent one remote's polyfills from affecting others?

Let the host own polyfills for the browsers you support, loaded once. Remotes should build for the same browser targets and not include their own global polyfills.

Otherwise two different polyfills for the same API can be loaded and fight with each other.

## 329: How would you design a micro frontend architecture for an e-commerce site?

- Host: layout, auth, navigation, error handling, remote registry.
- Remotes by domain: search/catalog, product details, cart, checkout, account.
- Vertical split by route, with small horizontal widgets (mini-cart in the header, recommendations).
- Shared: React, router, design system, auth and analytics clients.
- Product pages server-rendered for SEO; account and checkout client-rendered.
- Each team owns its BFF and deploys independently, with canaries and quick rollback.

## 330: How would you split a large admin dashboard into micro frontends?

Split by business area (users, billing, reports, settings), each owned by one team and mapped to a route prefix. The host provides the layout, permissions, navigation and shared design system.

Shared components like tables and forms belong in the design system, not in a separate "tables" remote. Widgets on the overview page can be small exposed components from each area's remote.

## 331: What are the signs that a micro frontend split is wrong?

- Most features need changes in several remotes at once.
- Remotes share a lot of state or call each other's internals.
- Teams must release together.
- Lots of "glue" code in the host.
- Remotes are split by technical layer, not domain.

Then merging some remotes or redrawing boundaries is usually cheaper than adding more communication.

## 332: When would you merge two micro frontends?

When they always change together, are owned by the same team, share most of their state, or are too small to be worth their own pipeline. Merging removes a contract and a deployment unit.

Splitting is not free, so it should keep paying for itself.

## 333: How do you avoid the host becoming a bottleneck?

- Keep it thin: layout, routing shell, auth, registry.
- Make remote registration config-driven, so adding a remote doesn't need host code.
- Give remotes ways to add menu entries or widgets via config.
- Have the host team own platform concerns, not features.

If every feature needs a host change, the host is a bottleneck.

## 334: How do you handle slots or extension points in the host?

Define named slots (for example `header-actions`, `dashboard-widgets`) that remotes can fill through the registry:

```jsx
function Slot({ name }) {
  const items = useRegistry().slots[name] ?? [];
  return items.map((item) => (
    <RemoteBoundary key={item.id} remote={item.remote} module={item.module} />
  ));
}
```

The host doesn't know the widgets ahead of time. It only renders what the registry lists for that slot.

## 335: How would you build a reusable RemoteBoundary component?

It should combine error handling, loading and lazy loading in one place:

```jsx
import { lazy, Suspense, useMemo } from "react";
import { ErrorBoundary } from "react-error-boundary";
import { loadRemote } from "@module-federation/enhanced/runtime";

export function RemoteBoundary({ remote, module, fallback = null, ...props }) {
  const Component = useMemo(
    () => lazy(() => loadRemote(`${remote}/${module}`)),
    [remote, module],
  );

  return (
    <ErrorBoundary
      fallback={<RemoteError remote={remote} />}
      onError={(error) => reportError(error, { remote, module })}
    >
      <Suspense fallback={fallback}>
        <Component {...props} />
      </Suspense>
    </ErrorBoundary>
  );
}
```

## 336: How do you handle errors thrown in a remote's event handlers?

Error boundaries only catch errors during rendering, lifecycle and effects. Errors in event handlers and async code (`setTimeout`, promises) don't reach them.

Catch them in the remote and report them, and add global `window.onerror` and `unhandledrejection` handlers in the host that tag errors with the remote (for example by the script URL in the stack).

## 337: How can you tell which remote threw an uncaught error?

Look at the stack trace URLs: each remote's chunks come from its own path or origin, for example `cdn.example.com/shop/`. Map URL prefixes to remote names in the global error handler:

```js
window.addEventListener("error", (e) => {
  const remote = remotes.find((r) => e.filename?.startsWith(r.baseUrl));
  monitor.captureException(e.error, { tags: { mfe: remote?.name ?? "host" } });
});
```

For cross-origin scripts you need `crossorigin` and CORS headers, or the browser hides the details ("Script error.").

## 338: Why do you get "Script error." for errors from remotes?

Browsers hide error details from scripts loaded from another origin unless the script was loaded with `crossorigin="anonymous"` and the server sends `Access-Control-Allow-Origin`. Without that, you only get "Script error." with no stack.

Set the `crossOriginLoading` option in webpack/Rspack (for example `'anonymous'`) and configure CORS on the CDN.

## 339: How do you design for partial failure in a micro frontend page?

- Each remote is wrapped in its own error and Suspense boundary.
- Critical remotes (like checkout) have a clear error page with retry; optional widgets just disappear.
- The host keeps working if the registry or any remote fails.
- Timeouts stop a slow remote from blocking the page.
- Monitoring alerts per remote, so the right team gets paged.

## 340: How do you handle a remote deployed with a bug that crashes on render?

Short term: roll back by pointing the registry to the last good version, or turn it off with a feature flag. The error boundary keeps the rest of the page alive in the meantime.

Long term: canary releases and automatic rollback when error rates go up for the new version.

## 341: How do you handle users with an old host version loading new remotes?

Users can keep a tab open for days, so an old host may load a newly deployed remote. Make remotes backward compatible with older hosts (within a supported window), and avoid breaking changes to shared contracts.

For forced updates, the host can poll for a new version and ask the user to reload.

## 342: How do you handle chunk load errors after a deployment?

If a remote deletes old chunks on deploy, users with an old remote entry in memory get 404s for chunks they haven't loaded yet ("ChunkLoadError").

Keep old versions' files on the CDN for some time (versioned folders do this), and on `ChunkLoadError` show a "new version available, reload" message.

## 343: Why keep previous remote versions on the CDN?

Users in the middle of a session still reference old chunk URLs. Rollbacks need old versions. Canaries need two versions live at once.

Clean up old versions only after a safe time window, for example a few weeks.

## 344: How does server-side rendering work with Module Federation?

The server also needs to load remote code, so each remote produces a Node build (a server remote entry) besides the browser one. The server host loads remotes through the federation runtime in Node, renders HTML, and the browser host hydrates using the browser builds.

Module Federation 2.0 supports this with `@module-federation/node`, and Modern.js has it built in. You must keep server and client versions of each remote in sync.

## 345: What are the hard parts of SSR with micro frontends?

- Loading and caching remote code on the server, and refreshing it when a remote deploys without restarting the server.
- Server and client using exactly the same remote version, or hydration fails.
- Sending the right CSS and preload links for each remote in the HTML.
- A slow remote slowing down the whole server response.
- Running remote code you don't control in your server process.

## 346: How can streaming SSR help with slow remotes?

With `renderToPipeableStream` (or `renderToReadableStream`), React sends the HTML shell first and streams each Suspense boundary when it is ready. A slow remote inside a Suspense boundary doesn't block the rest of the page.

The fallback is sent first, and the real content replaces it when the remote finishes rendering on the server.

## 347: What happens if a remote's server and client versions differ during hydration?

React finds that the HTML from the server doesn't match what the client renders, and reports a hydration error. In React 19 it then re-renders that part on the client, which can cause a flash or lost state.

Pin the remote version per request: the server includes it in the HTML, and the client loads exactly that version.

## 348: How do you do server-side composition without Module Federation?

Each team runs a service that returns an HTML fragment for its part of the page. A composition layer (an edge worker, a Node server, or a CDN with Edge Side Includes) fetches the fragments in parallel and stitches them into one page. Each fragment brings its own JS for hydration.

Tools and patterns for this include edge-side includes, Podium and custom edge workers.

## 349: What is Edge Side Includes (ESI)?

ESI is a markup language supported by some CDNs. The page contains tags like `<esi:include src="https://shop.example.com/fragment/cart" />`, and the CDN replaces them with the fetched fragment before sending the page.

It enables server-side composition at the edge with caching per fragment. Each fragment can have its own cache time.

## 350: How do you hydrate independent fragments on one page?

Each fragment renders into its own container and has its own client script that calls `hydrateRoot` on it:

```jsx
import { hydrateRoot } from "react-dom/client";
import Cart from "./Cart";

const el = document.getElementById("cart-fragment");
hydrateRoot(el, <Cart {...JSON.parse(el.dataset.props)} />);
```

Fragments are separate React roots, so they communicate through events or shared modules, not context.

## 351: How do React Server Components fit with micro frontends?

Server Components run only on the server and are tied to a framework's bundler setup (like Next.js). Each RSC app has its own server, bundler manifest and client references, so you can't simply load another team's Server Component at runtime with Module Federation today.

In practice, teams split RSC apps by route (for example with Next.js Multi-Zones) and share client components through packages. Federation of Server Components is still an area of active work, not a mainstream approach.

## 352: What are the downsides of Next.js Multi-Zones?

- Moving between zones is a full page load, so it feels slower than client-side navigation.
- Shared layout (header, footer) has to be duplicated or shared as a package in each zone.
- Global state doesn't carry over between zones except through cookies, storage or the server.
- Each zone needs its own `assetPrefix` so static files don't clash.

It works well when zones are mostly separate parts of the site.

## 353: How do you configure Multi-Zones in Next.js?

Each zone sets an `assetPrefix`, and the main app rewrites paths to the other zones:

```js
// next.config.js of the main app
module.exports = {
  async rewrites() {
    return [
      { source: "/blog", destination: `${process.env.BLOG_DOMAIN}/blog` },
      {
        source: "/blog/:path+",
        destination: `${process.env.BLOG_DOMAIN}/blog/:path+`,
      },
      {
        source: "/blog-static/:path+",
        destination: `${process.env.BLOG_DOMAIN}/blog-static/:path+`,
      },
    ];
  },
};
```

```js
// next.config.js of the blog zone
module.exports = { assetPrefix: "/blog-static" };
```

Links to other zones should use plain `<a>` tags, not `next/link`.

## 354: How would you share client state across Next.js zones?

You can't share in-memory state, because each zone is a separate page load. Use:

- Cookies for things the server needs (session, locale).
- `localStorage` or `sessionStorage` for client-only preferences.
- The server (a user profile API) for anything important, like the cart.

Design zones so they need little shared client state.

## 355: How do you avoid duplicate React when combining web components from different teams on one page?

Each React-based web component that bundles React brings its own copy. With several such components, the page loads React several times.

Options: build them against a shared React loaded through an import map or Module Federation, or accept the cost for a few widgets. For many widgets, sharing is worth the extra setup.

## 356: Can two React copies on one page cause bugs if they render into separate roots?

Not by themselves. Two Reacts with separate roots work fine, but they can't share context, Suspense or error boundaries, and React elements from one can't be rendered by the other (you'd get errors about invalid elements).

The main costs are bundle size and memory, plus confusion if code tries to mix them.

## 357: How do React's event delegation and roots affect micro frontends?

Since React 17, React attaches event listeners to the root container instead of `document`. That makes it safe to have several React roots (even different versions) on one page: each handles events only in its own container.

Calling `e.stopPropagation()` in one root still stops the native event from reaching outer roots, which can surprise the host.

## 358: How do you mount a React 19 remote into a React 18 host safely?

Don't share React between them. Have the remote expose a mount function that brings its own React 19 and renders into a DOM node the host gives it:

```jsx
// host (React 18)
function LegacyBridge({ load, ...props }) {
  const ref = useRef(null);
  useEffect(() => {
    let cleanup = () => {};
    let cancelled = false;
    load().then(({ mount }) => {
      if (!cancelled) cleanup = mount(ref.current, props);
    });
    return () => {
      cancelled = true;
      cleanup();
    };
  }, []);
  return <div ref={ref} />;
}
```

Props updates need an extra `update` function or a remount.

## 359: What is the React bridge in Module Federation 2.0 actually doing?

`createBridgeComponent` in the remote returns an object with `render` and `destroy` functions that create and remove a React root for the remote app, with its own router set to the right basename. `createRemoteAppComponent` in the host loads that object and renders a placeholder element, calling `render` on mount and `destroy` on unmount, passing props and route info.

So the remote app runs in its own root and can even use a different React version than the host.

## 360: How do you use createBridgeComponent and createRemoteAppComponent?

```jsx
// remote: src/export-app.jsx
import { createBridgeComponent } from "@module-federation/bridge-react";
import App from "./App";

export default createBridgeComponent({ rootComponent: App });
```

```jsx
// host
import { createRemoteAppComponent } from "@module-federation/bridge-react";
import { loadRemote } from "@module-federation/enhanced/runtime";

const ShopApp = createRemoteAppComponent({
  loader: () => loadRemote("shop/export-app"),
  fallback: ({ error }) => <p>Shop failed: {error.message}</p>,
  loading: <p>Loading...</p>,
});

<Route path="/shop/*" element={<ShopApp basename="/shop" />} />;
```

## 361: What do you lose when a remote runs in its own React root?

- The host's context providers (theme, auth, query client) don't reach it.
- The host's Suspense and error boundaries don't catch its errors.
- Transitions and concurrent rendering don't coordinate across roots.
- Every prop change goes through a re-render call across the boundary.

You gain isolation and version freedom. Pass what's needed explicitly as props.

## 362: How do you design a stable interface between host and remote apps?

Keep it small and data-only:

```ts
export interface RemoteAppProps {
  basename: string;
  locale: string;
  user: { id: string; roles: string[] } | null;
  navigate: (to: string) => void;
  onEvent?: (name: string, payload: unknown) => void;
}
```

Avoid passing React elements, class instances or library objects across the boundary, since they tie both sides to the same versions.

## 363: Why is passing React elements between micro frontends risky?

A React element is an object with an internal `$$typeof` symbol and a reference to a component type. If the host and remote use different React copies, the receiver doesn't recognize the element as valid ("Objects are not valid as a React child").

Even with one React, it ties the host and remote tightly together. Pass data and render on each side instead.

## 364: How would you build a cross-framework micro frontend host with React?

The host only knows a generic contract, for example:

```ts
type MicroApp = {
  mount(el: HTMLElement, props: Record<string, unknown>): void;
  update?(props: Record<string, unknown>): void;
  unmount(): void;
};
```

A React wrapper calls `mount` in an effect, `update` when props change and `unmount` on cleanup. Each remote implements the contract with its own framework. Module Federation, import maps or single-spa can load them.

## 365: How do you handle props updates for a mounted non-React micro frontend?

Call the `update` function in a separate effect:

```jsx
function MicroAppHost({ app, ...props }) {
  const ref = useRef(null);

  useEffect(() => {
    app.mount(ref.current, props);
    return () => app.unmount();
  }, [app]);

  useEffect(() => {
    app.update?.(props);
  }, [app, JSON.stringify(props)]);

  return <div ref={ref} />;
}
```

`JSON.stringify` here is a simple way to compare props by value. For big props, use a custom comparison.

## 366: How does React Strict Mode affect micro frontend mounting code?

In development, Strict Mode runs effects twice (mount, unmount, mount) to catch missing cleanup. Mount functions that don't clean up properly create two roots, two listeners or two subscriptions.

Make every mount function idempotent and return a correct cleanup. If it breaks under Strict Mode, it will leak in production when users navigate.

## 367: What is the "createRoot on a container that already has a root" warning?

React warns when you call `createRoot` twice on the same DOM node without unmounting first. It often happens in micro frontend mount code that runs twice (Strict Mode or remounting) and creates a new root each time.

Store the root and reuse it, or unmount before creating a new one.

## 368: How do you prevent memory leaks in long-running micro frontend apps?

- Unmount React roots when micro frontends are removed.
- Remove event listeners, intervals and subscriptions in effect cleanup.
- Don't keep references to unmounted components in shared stores or globals.
- Clear caches of remotes the user left, if they can grow without limit.
- Use Chrome DevTools heap snapshots after navigating between remotes to look for detached DOM nodes.

## 369: How do you find which micro frontend is leaking memory?

Take a heap snapshot, navigate in and out of one remote several times, take another and compare. Look for growing object counts and detached DOM trees, and check their retainers to see which code holds them.

Repeat per remote. Leaks often come from listeners on `window` or subscriptions to shared stores that aren't removed.

## 370: How do you optimize the first page load of a micro frontend app?

- Keep the host bundle small, and lazy load remotes.
- Preload the remote for the landing route in the HTML (`<link rel="modulepreload">` or `preload`).
- Use the manifest to fetch remote assets in parallel.
- Avoid version-first loading of all remote entries if you have many.
- Server-render or prerender the first view where possible.
- Cache remote chunks long term and remote entries briefly.

## 371: How can the host add preload hints for the current route's remote?

If the host server knows the route, it can add the remote's entry and main chunks to the HTML:

```html
<link
  rel="preload"
  href="https://cdn.example.com/shop/1.8.0/remoteEntry.js"
  as="script"
  crossorigin
/>
<link rel="preconnect" href="https://cdn.example.com" crossorigin />
```

For a client-only host, start `preloadRemote` as early as possible, before React renders.

## 372: Why does serving remotes from different domains hurt performance?

Each new origin needs DNS lookup, TCP and TLS setup before the first byte. With remotes on many domains, the browser does this for each one, and HTTP/2 or HTTP/3 connections can't be reused across them.

Serve all remotes from one CDN domain with different paths, or at least `preconnect` to the domains you need early.

## 373: How do you avoid duplicate code that isn't shared, like lodash in each remote?

- Use bundle analysis per remote and across all remotes to find duplicates.
- Share packages that most remotes use in the same major version.
- Prefer smaller, tree-shakable libraries.
- Have the platform team offer standard utilities in a shared package.

Some duplication is fine. Fight it only where it costs real size.

## 374: How do you measure Web Vitals per micro frontend?

Use the `web-vitals` library in the host and attach the current route and active remotes to each metric. For INP and CLS, the attribution build tells you which element caused the issue, which you can map to a remote by its container.

```js
import { onINP } from "web-vitals/attribution";

onINP(({ value, attribution }) => {
  const el = document.querySelector(attribution.interactionTarget);
  const mfe = el?.closest("[data-mfe]")?.dataset.mfe ?? "host";
  analytics.track("inp", { value, mfe });
});
```

## 375: How do you stop one remote from blocking the main thread for others?

All remotes share one main thread, so a heavy remote hurts everyone's INP. Have each team:

- Break long tasks into smaller ones (`scheduler.yield()` where supported, or `setTimeout`).
- Use `startTransition` for expensive updates.
- Move heavy work to Web Workers.
- Watch long tasks per remote in monitoring.

Performance budgets should include main-thread time, not only bundle size.

## 376: How do you load a remote only when it scrolls into view?

```jsx
function LazyWhenVisible({ children, minHeight = 300 }) {
  const ref = useRef(null);
  const [visible, setVisible] = useState(false);

  useEffect(() => {
    const observer = new IntersectionObserver(
      ([entry]) => {
        if (entry.isIntersecting) {
          setVisible(true);
          observer.disconnect();
        }
      },
      { rootMargin: "200px" },
    );
    observer.observe(ref.current);
    return () => observer.disconnect();
  }, []);

  return (
    <div ref={ref} style={{ minHeight }}>
      {visible && children}
    </div>
  );
}

<LazyWhenVisible>
  <RemoteBoundary remote="reviews" module="ReviewList" productId={id} />
</LazyWhenVisible>;
```

## 377: How do you cache remote modules with a service worker?

A service worker can cache remote chunks with a cache-first strategy (they are hashed) and the remote entry/manifest with network-first or stale-while-revalidate. Workbox makes this simple with routing rules per URL pattern.

Be careful: caching the remote entry too aggressively brings back the "old version" problem. Users should get the new entry soon after a deployment.

## 378: Can micro frontends work offline?

Yes, with a service worker that pre-caches the host and the remotes users need offline. The registry and remote entries must also be cached, with a plan for updating them when online.

It is harder than for a single app because many teams deploy files independently. Usually only a few key remotes are made available offline.

## 379: How do you handle a remote that needs a different browser target than the host?

All remotes should agree on one browserslist config, owned by the platform team. If a remote builds for newer browsers only, it can break for users the host supports, and older-target remotes ship extra code.

Put the browser targets in a shared config package and check them in CI.

## 380: How would you handle global CSS that must be shared, like fonts and resets?

The host loads it once: a reset, base typography, fonts and design tokens. Remotes assume it is there and only ship component-scoped styles. For standalone mode, remotes load the same global CSS package in their dev entry.

This keeps one source of truth and avoids remotes overriding each other's globals.

## 381: How do you handle CSS ordering problems between remotes?

When several remotes inject styles at different times, the order of `<style>` tags depends on load order, and selectors of equal specificity override each other unpredictably.

Use scoped class names so rules don't compete, and use CSS cascade layers to fix the order between host, design system and remotes:

```css
@layer reset, design-system, remotes;
```

## 382: How do CSS cascade layers help in micro frontends?

`@layer` lets you set priority between groups of styles regardless of the order they load in. If the host declares `@layer reset, ds, app;` first, then any rule in the `app` layer beats the `ds` layer, even if `ds` styles load later.

Remotes wrap their styles in their layer, and the host's order stays the same no matter which remote loads first.

## 383: How do you share a theme with CSS-in-JS when remotes can't share a provider?

Use CSS variables as the theme source. The host sets them once, and each remote's CSS-in-JS styles read `var(--color-primary)`. Since CSS variables are inherited by the DOM, they work across React roots, Shadow DOM and frameworks.

Theme switching then only changes variables on one element.

## 384: How do you build a design system for micro frontends with different React versions?

- Build components against a peer range like `^18.3.0 || ^19.0.0`.
- Ship styles as plain CSS or CSS variables, not runtime-only CSS-in-JS.
- Offer web component versions of key components for non-React or isolated apps.
- Version it with semver and support the last major for a while.

## 385: What is the trade-off of sharing the design system at runtime vs bundling it?

Runtime sharing gives one copy and lets a design system fix reach all remotes without rebuilding them. But a bad release can break every remote at once, and remotes run against a version they weren't tested with.

Bundling gives each remote the version it tested with, at the cost of bigger downloads and visual drift between remotes. Many teams share a major version at runtime and rely on good testing of minor releases.

## 386: How do you do visual regression testing across micro frontends?

Each remote runs visual tests for its own components (for example with Storybook and a screenshot tool). The platform team runs a few visual tests on the composed app to catch layout and style conflicts between remotes.

Run the composed tests when the design system or host changes, and on a schedule to catch drift.

## 387: How would you set up contract testing with consumer-driven contracts?

The host (consumer) writes down what it expects from a remote: exposed module names, required props and events. The remote (provider) runs these expectations in its CI against its build. If the remote breaks one, its build fails before deployment.

Tools like Pact are designed for API contracts. For UI contracts teams often use shared TypeScript types plus a small test suite that loads the built remote.

## 388: How do you test a remote's build output before deployment?

Start a static server for the built remote and load it with the federation runtime in a test (Node or a headless browser):

```js
import { createInstance } from "@module-federation/enhanced/runtime";

test("exposes ProductList", async () => {
  const mf = createInstance({
    name: "contract-test",
    remotes: [
      { name: "shop", entry: "http://localhost:4173/mf-manifest.json" },
    ],
  });
  const mod = await mf.loadRemote("shop/ProductList");
  expect(typeof mod.default).toBe("function");
});
```

Running it in a real browser with Playwright is closer to production.

## 389: How do you run integration tests that mix local and deployed remotes?

Start the host and the remote under test locally, and point the other remotes to a shared staging environment through the registry or overrides. Playwright can set the override before the page loads.

This tests your change against real versions of the other remotes without running everything locally.

## 390: How do you test what happens when a remote is down?

In Playwright, block the remote's URL and check that the fallback shows and the rest of the page works:

```js
test("page works when reviews remote is down", async ({ page }) => {
  await page.route("**/reviews/**", (route) => route.abort());
  await page.goto("/product/42");
  await expect(page.getByText("Reviews are not available")).toBeVisible();
  await expect(page.getByRole("button", { name: "Add to cart" })).toBeEnabled();
});
```

## 391: How do you handle the host's dependency on remote TypeScript types in a polyrepo?

Options:

- Each remote publishes a small contract package with types to a private npm registry.
- Module Federation 2.0 generates and serves types from the deployed remote.
- Types are generated into the host's repo by a CI job.

The contract package is the most explicit and version-controlled. Automatic types are more convenient but depend on remote URLs at build time.

## 392: What happens to type safety when a remote deploys without the host rebuilding?

Types were checked against the old contract at the host's build time. If the remote changes props in a breaking way and deploys, the host's types are now wrong, and you only find out at runtime.

That's why types alone are not enough. You need backward-compatible changes, runtime validation at the boundary and contract tests in the remote's CI.

## 393: How do you validate props at runtime at a micro frontend boundary?

Use a schema library like Zod in the remote's exposed component:

```tsx
import { z } from "zod";

const Props = z.object({
  productId: z.string(),
  quantity: z.number().int().min(1).default(1),
});

export default function AddToCart(rawProps: unknown) {
  const result = Props.safeParse(rawProps);
  if (!result.success) {
    console.warn("AddToCart: invalid props", result.error.issues);
    return null;
  }
  return <AddToCartButton {...result.data} />;
}
```

## 394: How do you handle state that must survive navigation between remotes?

Keep it outside the remotes' React trees: in the host, in a shared store module, in the URL, or on the server. When a remote unmounts, its React state is gone.

For example, a cart should live on the server and in a shared store, not in the cart remote's component state.

## 395: How do you design a shared store so teams don't step on each other?

- Split it into slices owned by one team each.
- Expose only actions and selectors, not direct setters for the whole state.
- Version the shared package and treat its shape as a contract.
- Keep it small: most state should stay inside each remote.

## 396: How would you design an event contract that can evolve?

- Name events with domain and past tense: `cart:item-added`.
- Include a `version` field in the payload.
- Only add fields; never change the meaning of existing ones.
- For breaking changes, send a new event name (`cart:item-added.v2`) and keep sending the old one for a while.
- Keep the event types in a shared contract package.

## 397: How do you handle events fired before a listener is ready?

A remote that loads later misses events fired before it subscribed. Solutions:

- Store the last value of important events and give it to new subscribers (like a "replay last" behavior).
- Use a shared store for state, and events only for notifications.
- Let the remote ask for the current value on mount.

```js
const last = new Map();
export function emit(type, detail) {
  last.set(type, detail);
  window.dispatchEvent(new CustomEvent(type, { detail }));
}
export const getLast = (type) => last.get(type);
```

## 398: What are the downsides of using window CustomEvents for all communication?

- No type checking unless you add a typed wrapper.
- Events are global, so names can clash.
- Hard to trace who sends and who listens.
- Missed events if the listener mounts late.
- Easy to create hidden coupling that grows over time.

They are good for simple notifications, but a shared typed module is better for anything bigger.

## 399: How would you prevent a "chatty" relationship between micro frontends?

If two remotes exchange many events, they probably belong together or share a concept that should live in a shared service. Look at what data moves between them and why.

Reduce communication by moving shared data to the URL or the server, merging the remotes, or redrawing the boundary.

## 400: How do you handle shared forms that span several micro frontends?

Try to avoid it, because a form split across teams needs shared validation and submit logic. If you must, keep one owner for the form state (for example the checkout remote) and let other remotes provide only presentational parts through props.

Or let each remote save its part to the server separately, so there's no shared client form state.

## 401: How do you manage the cost of many CI pipelines?

- Use shared pipeline templates (GitHub Actions reusable workflows, GitLab includes) owned by the platform team.
- Use build caching (Nx remote cache, Turborepo cache) so unchanged apps don't rebuild.
- Run only affected pipelines on each change.
- Keep pipelines fast by running heavy E2E tests on a schedule or before release, not on every commit.

## 402: How do you make a shared CI template for micro frontends?

```yaml
# .github/workflows/mfe-deploy.yml (reusable)
on:
  workflow_call:
    inputs:
      app:
        required: true
        type: string

jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-node@v4
        with:
          node-version: 22
      - run: npm ci
      - run: npm run build --workspace=apps/${{ inputs.app }}
      - run: npm test --workspace=apps/${{ inputs.app }}
      - run: ./scripts/upload.sh ${{ inputs.app }} ${{ github.sha }}
      - run: ./scripts/update-registry.sh ${{ inputs.app }} ${{ github.sha }}
```

Each app's workflow calls it with its own name.

## 403: How do you promote a remote version from staging to production?

Since the build is the same, promotion only changes the registry entry for the production environment to the version already tested in staging. No rebuild happens.

Keep the history of registry changes (who changed what and when), so rollback is one step back.

## 404: How would you implement automatic rollback for a remote?

After updating the registry, monitor error rates and key metrics for the new version (tagged in errors and analytics). If they cross a threshold within a time window, a job switches the registry back to the previous version and alerts the team.

This needs good version tagging in monitoring and a registry that supports quick changes.

## 405: How do you handle database or API changes that a remote depends on?

Deploy back-end changes first in a backward-compatible way, then the remote that uses them. The old remote must keep working with the new API, and the new remote should handle the old API during rollout if possible.

Since remotes and back-ends deploy separately, "expand and contract" applies to both.

## 406: How do you coordinate a release that needs changes in several remotes?

Try to avoid it with backward-compatible changes and feature flags. Each team deploys its part with the feature turned off, then the flag turns the feature on for everyone at once.

If you often need coordinated releases, the boundaries are probably wrong.

## 407: What is the risk of Module Federation remotes in a monorepo importing each other at build time?

If app A imports app B's source directly (not through federation), B's code is bundled into A. Changes in B then need A to rebuild and redeploy, and you may run two versions of B in the page.

Use lint rules to forbid direct imports between apps. All cross-app usage should go through remotes or shared packages.

## 408: How would you handle a shared library with a breaking change in a federated setup?

- Release the new major version of the shared library.
- Since a singleton can only be one version, remotes on the old major and the new one can't share it at the same time.
- Either upgrade all apps together (with flags), or temporarily make the library non-singleton so each app uses the version it needs, if it has no global state.
- Or give the new major a different `shareKey` during migration.

Plan breaking changes in shared libraries carefully, because they affect every app.

## 409: How can shareKey help during a major version migration?

You can share both majors under different keys so they don't conflict:

```js
// apps on the new version
shared: {
  '@acme/ui': { singleton: true, shareKey: '@acme/ui@3', requiredVersion: '^3.0.0' },
}
```

Apps still on v2 use the normal key. Each group shares its own copy. When all apps move to v3, you go back to the normal key.

## 410: How do you debug "Cannot read properties of undefined (reading 'call')" in Module Federation?

This error often means webpack tried to run a module that wasn't loaded, usually because of:

- Two webpack runtimes with the same `output.uniqueName` overwriting each other's chunk registry.
- A remote's `publicPath` pointing to the wrong place.
- Mismatched chunk files after a deployment (old entry, new chunks).

Give each app a unique `name`/`uniqueName`, use `publicPath: 'auto'` and versioned deployments.

## 411: Why does each federated webpack app need a unique uniqueName?

Webpack uses `output.uniqueName` (by default from `package.json` name) to name its global chunk loading variable, like `webpackChunkshop`. If two apps have the same name, they write chunks into the same global array and load each other's modules by id, causing random failures.

In monorepos with copied `package.json` files, this is easy to miss. Set it explicitly.

## 412: How does Module Federation handle two remotes that expose the same module name?

Exposed names are scoped by the remote name (`shop/Button` vs `ui/Button`), so they don't clash. Problems only appear if two remotes register under the same remote name, in which case one overwrites the other.

Keep a registry check that rejects duplicate remote names.

## 413: How do you load the same remote twice with different versions?

Register them under different names and load each separately:

```js
registerRemotes([
  {
    name: "shop_v1",
    alias: "shopV1",
    entry: "https://cdn.example.com/shop/1.9.0/mf-manifest.json",
  },
  {
    name: "shop_v2",
    alias: "shopV2",
    entry: "https://cdn.example.com/shop/2.0.0/mf-manifest.json",
  },
]);
```

This only works if each build was made with that unique `name`, since the name is part of the build. Most teams avoid running two versions of one remote on the same page.

## 414: How do you replace a loaded remote with a newer version without a page reload?

In general you can't safely. Modules are cached once loaded, and the old code is still running in components on screen. Module Federation 2.0's runtime has options to register remotes again with `force: true`, but already loaded modules and mounted components keep using the old code.

The practical approach is to show "a new version is available" and reload the page, or reload on the next full navigation.

## 415: How do you detect that a new version of a remote is available?

Poll the registry or manifest every few minutes (or when the tab becomes visible) and compare the version with the one loaded. If it changed, show a non-blocking message or reload on the next navigation.

```js
document.addEventListener("visibilitychange", async () => {
  if (document.visibilityState !== "visible") return;
  const registry = await fetch("/mf-registry.json", { cache: "no-store" }).then(
    (r) => r.json(),
  );
  if (registry.shop.version !== loadedVersions.shop) showUpdateBanner();
});
```

## 416: How do you share code between the host's and remote's Node SSR servers safely?

Server-side remotes run inside the host's Node process, so they share memory and globals across all requests. Code that stores per-user data in module-level variables leaks data between users.

Remotes must keep request data in request-scoped context (props, `AsyncLocalStorage`), never in module state. Review server remote code like your own server code.

## 417: Why is module-level state dangerous in SSR micro frontends?

On the server, a module is loaded once and reused for all requests. A shared store created at module level (`const store = createStore()`) holds data from one user's request and shows it to the next.

Create stores per request on the server and pass them down, or use framework support for request scope.

## 418: How do you refresh server-side remotes without restarting the server?

The server's federation runtime caches loaded remote code. When a remote deploys, you need to clear that cache and load the new entry. Module Federation's Node tooling supports checking for updated remote entries and reloading them.

Many teams instead run SSR remotes as separate services that return HTML fragments, which avoids running remote code in the host's process.

## 419: How do you handle SEO for client-side rendered micro frontends?

Google can render JavaScript, but it's slower and less reliable than server HTML, especially when content needs several remote loads. For pages where SEO matters:

- Server-render or prerender them.
- Keep important content in one remote per page, not spread across lazy widgets.
- Make sure titles, meta tags and canonical URLs are set correctly by the page owner.

## 420: How do you handle meta tags when several remotes are on one page?

The page owner (the route's main remote or the host) sets the title, description and canonical URL. Widgets must not set them.

In React 19, `<title>` and `<meta>` rendered anywhere are hoisted to `<head>`, so two remotes rendering them would conflict. Make it a rule in the contract.

## 421: How do you think about micro frontends vs a modular monolith?

A modular monolith keeps one app and one deployment but enforces boundaries in code (folders, lint rules, separate packages in a monorepo). You get most of the code-organization benefits with much less runtime complexity.

Micro frontends add independent deployment and runtime composition. Choose them when release independence between teams is the real problem; otherwise start with a modular monolith.

## 422: How would you migrate a modular monolith to micro frontends later?

If modules already have clear boundaries and public APIs, each module can become a remote:

1. Set up the host from the current app shell.
2. Turn one module into a remote that exposes its routes, keep the rest in the host.
3. Move shared code into shared packages.
4. Repeat for other modules.

A good modular monolith makes this migration much easier.

## 423: How would you migrate from single-spa to Module Federation?

- Keep single-spa for lifecycles at first, but load apps through federation instead of the import map.
- Share React and common libraries through federation's `shared` config.
- Move React apps that live in the same tree to be remote components instead of separate single-spa apps.
- Remove single-spa when no app needs its framework-neutral lifecycle anymore.

Do it app by app, never all at once.

## 424: How would you migrate a webpack Module Federation setup to Rspack?

Rspack supports the same Module Federation config, so the migration is mostly about the bundler:

- Replace `webpack` with `@rspack/core` and the CLI, and swap loaders (for example `babel-loader` to `builtin:swc-loader`).
- Use `@module-federation/enhanced/rspack` (or Rspack's built-in plugin).
- Migrate one remote at a time. Webpack and Rspack remotes can load each other.
- Compare bundles and test shared packages after each move.

## 425: How would you migrate a federated app from webpack to Vite?

- Switch the bundler and use `@module-federation/vite`.
- Remotes now build ES module remote entries, so update hosts to load them with `type: 'module'`.
- Replace webpack-only features (`require.context`, loaders, magic comments).
- Test that shared packages resolve the same way, especially React and its sub-paths.

Move remotes first and the host last, and keep both bundlers working during the migration.

## 426: What are common pitfalls with @module-federation/vite?

- Dev mode behaves differently from the production build, so always test the built output.
- Shared packages with sub-path exports may need explicit config.
- Some Vite plugins don't play well with the federation virtual modules.
- Mixed webpack/Vite setups need careful testing of shared versions.

Check the plugin's changelog; it evolves quickly.

## 427: How do you handle remotes that use different state management libraries in the same React tree?

That's fine as long as each library is either bundled in the remote (no sharing needed) or shared as a singleton when the host provides its provider. Each remote wraps its own subtree in its own provider:

```jsx
export default function ShopApp() {
  return (
    <Provider store={shopStore}>
      <ShopRoutes />
    </Provider>
  );
}
```

Problems come when two remotes share the same library but expect different versions or different store instances under one provider.

## 428: How do you design a micro frontend platform for many independent teams?

- **Contracts**: registry format, exposed module rules, event and prop contracts, versioning rules.
- **Tooling**: generators for new remotes, shared build config, CI templates, local dev with overrides.
- **Runtime**: thin host, registry service, error and loading boundaries, runtime plugins for retries and logging.
- **Shared libs**: design system, auth, HTTP client, analytics, i18n.
- **Governance**: React and dependency upgrade plans, performance budgets, security review for new remotes.
- **Observability**: errors, Web Vitals and versions tagged per remote.

## 429: What governance rules would you set for micro frontend teams?

- One supported React major (with a migration window during upgrades).
- No global CSS or global JS side effects in remotes.
- Every remote has an owner, a contract doc and on-call contacts.
- Breaking contract changes need a deprecation period.
- Performance and accessibility budgets checked in CI.
- New shared dependencies go through the platform team.

Keep the rules few and automated where possible. Long rule lists get ignored.

## 430: How do you measure if a micro frontend architecture is working?

- Deployment frequency per team and how often teams must release together.
- Lead time from commit to production.
- Incidents caused by cross-app integration.
- Page performance compared to before the split.
- Time to create a new remote.
- Developer survey feedback on local development.

If teams don't deploy more independently than before, the architecture isn't giving its main benefit.

## 431: How do you handle a team that keeps breaking other teams' remotes?

First, find the technical gap: missing contract tests, loose shared versions, global CSS or undocumented events. Add automated checks that catch the specific problem in that team's CI.

Then agree on clear ownership and review rules for shared contracts. Most of these problems are fixed better by tooling than by meetings.

## 432: How would you handle a slow host build that blocks all teams?

The host should change rarely and build fast. Move feature code out of it, use caching, and make remote additions config-only. Check that the host doesn't bundle remote code through direct imports.

If the host still changes often, its responsibilities are too broad. Split platform features into shared packages or separate remotes.

## 433: How would you design local development for 20 remotes?

Developers shouldn't run all 20. Typical setup:

- Run the host and the one or two remotes you work on locally.
- Load all other remotes from a shared dev or staging environment through the registry.
- Use overrides (DevTools extension or a dev panel) to switch any remote to `localhost`.
- Provide one command to start this setup.

## 434: How do you handle authentication in local development with remote environments?

Local hosts usually run on `localhost`, but staging auth cookies are set for the staging domain. Options:

- Run the local host under a staging subdomain with a hosts file entry and local HTTPS.
- Use a dev auth mode that gets a token for a test user.
- Proxy API calls through the local dev server so cookies work.

Document the setup, since it's one of the most common onboarding problems.

## 435: How do you handle mixed content and HTTPS in local remote overrides?

If production runs on HTTPS and you override a remote to `http://localhost:3001`, the browser blocks it as mixed content (except some browsers treat `localhost` as secure). Run local dev servers with HTTPS (for example with `mkcert` certificates) to avoid surprises.

Also allow `localhost` in your CSP only for internal or dev builds.

## 436: How would you implement a dev panel to switch remote versions?

The host renders a small panel (only for internal users) that lists remotes from the registry, their current versions and available ones. Selecting a version or entering a URL stores an override in `localStorage` and reloads the page.

The host applies overrides before registering remotes and shows a clear banner when any override is active, so testers don't forget they're on a custom setup.

## 437: What questions would you ask before recommending micro frontends?

- How many teams work on the front-end, and how often do they block each other?
- Do teams need to release independently?
- Are there clear business domains to split by?
- Is there a platform team to own the host and tooling?
- What are the performance and SEO needs?
- Is there legacy code to migrate gradually?

If most answers point to a small team with one release cycle, recommend a modular monolith.

## 438: How do you explain the trade-off between isolation and integration?

More isolation (iframes, separate roots, no shared libraries) means fewer side effects between teams and more version freedom, but heavier pages and harder UX consistency.

More integration (shared React tree, shared context, shared libraries) gives a smoother, lighter app but couples teams on versions and contracts. Most setups pick integration by default and isolation for legacy or third-party parts.

## 439: How would you build a plugin system for a SaaS product with micro frontends?

Third-party plugins should not run in your page context. Load them in sandboxed iframes on a separate origin, with a typed `postMessage` API (an SDK) that exposes only allowed actions and data. Host-side code checks every message and the plugin's permissions.

Internal plugins from your own teams can use Module Federation, since you trust their code.

## 440: How do you handle a remote that needs data from the host on every render?

Pass it as props and keep it small. If many remotes need the same changing data (like the current user or cart count), use a shared store with selectors, so each remote subscribes to only what it needs and re-renders only when that changes.

Avoid passing large objects that change identity on every host render, since that re-renders the whole remote.

## 441: How do you avoid re-rendering a remote when the host re-renders?

Remote components are normal React components, so the usual tools apply: keep props stable (`useMemo`, `useCallback`), and wrap the remote in `memo` if its props rarely change. The React Compiler can do much of this memoization automatically.

```jsx
const Reviews = lazy(() => import("reviews/ReviewList"));

const ReviewsSection = memo(function ReviewsSection({ productId }) {
  return <Reviews productId={productId} />;
});
```

Also check that context providers in the host don't change their value on every render.

## 442: Does the React Compiler work across micro frontends?

The React Compiler runs at build time inside each app's build. Each remote must be compiled on its own. It optimizes code inside each remote and the host, but it can't see across the federation boundary.

All apps should use a compatible React version for the compiler's runtime (`react/compiler-runtime` in React 19), and that should be shared like React itself.

## 443: How would you design error handling contracts between host and remote?

- Remotes catch and report their own errors and render their own error UI where it makes sense.
- Errors that escape are caught by the host's boundary around the remote, with a generic fallback.
- Remotes can signal fatal states to the host through an event (`mfe:fatal`) so the host can show a page-level message.
- All errors are tagged with remote name and version.

## 444: What are the biggest mistakes teams make with React micro frontends?

- Splitting too early, before team size needs it.
- Splitting by technical layer instead of business domain.
- Not sharing React correctly, leading to "Invalid hook call" and huge bundles.
- Global CSS and side effects in remotes.
- A big shared global store that couples everyone.
- No error boundaries or fallbacks around remotes.
- Caching remote entries for too long.
- No owner for the host, design system and tooling.

## 445: How do you explain Module Federation to a non-technical stakeholder?

It is like a website made of parts that different teams build and update on their own schedule. When a user opens the site, the main app fetches the latest version of each part and puts them together on the screen.

The benefit is that teams don't wait for each other to release. The cost is more setup and more things to monitor.

## 446: How would you approach a performance regression after splitting into micro frontends?

1. Compare Web Vitals and bundle sizes before and after.
2. Check for duplicate libraries (especially React) and shared config errors.
3. Look for loading waterfalls between host and remotes.
4. Check caching headers on remote entries and chunks.
5. Look at main-thread time per remote.
6. Fix the biggest issue first and add budgets so it doesn't come back.

## 447: How do you handle cookies and storage keys across micro frontends?

All remotes on one origin share cookies, `localStorage` and `sessionStorage`. Prefix keys with the remote name (`shop:recentlyViewed`) to avoid clashes, and have only the host or auth module touch session cookies.

Clear each remote's keys on logout through a shared helper that knows all prefixes.

## 448: How would you design micro frontends for a mobile web app with slow networks?

- Fewer, larger remotes instead of many small ones, to avoid waterfalls.
- Server-render the first view.
- Aggressive caching of hashed chunks and a service worker for repeat visits.
- Preload the next likely remote when the network is idle (check `navigator.connection.saveData` and skip if it's on).
- Small performance budgets per remote.

## 449: What trends do you see in React micro frontends right now?

- Module Federation 2.0 becoming the standard runtime across webpack, Rspack and Vite.
- Rspack and Rsbuild replacing webpack for faster builds.
- Manifest-based loading, automatic type sharing and runtime plugins.
- Interest in using React Server Components with federation, still early.
- More teams choosing modular monoliths and only splitting where release independence is really needed.

## 450: If you had to sum up the key principles of a good React micro frontend architecture, what would they be?

- Split by business domain and team, not by technical layer.
- Keep the host thin and config-driven.
- Share React and a few key libraries as singletons, and nothing more than needed.
- Keep contracts small, typed, versioned and backward compatible.
- Isolate failures with error and Suspense boundaries around every remote.
- Scope all styles and avoid global side effects.
- Deploy each remote independently with versioned files, fast rollback and good monitoring.
- Start with a modular monolith if you don't yet need independent deployment.
