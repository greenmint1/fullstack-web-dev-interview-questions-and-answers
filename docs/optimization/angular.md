# Angular Optimization Interview Questions and Answers

_Last updated: October 28, 2026_

450 interview questions with answers about making Angular apps fast, split into three levels: 150 easy, 150 moderate and 150 advanced. They cover load performance (bundles, lazy loading, `@defer`, images, SSR and hydration, caching) and runtime performance (change detection, signals, lists, memory, profiling).

The answers target Angular v22: OnPush by default, zoneless change detection (default for new apps since v21), signals and resources, incremental hydration on by default, the fetch-based `HttpClient`, `injectAsync()` and the esbuild-based build system. Older approaches (Zone.js, `*ngFor` with `trackBy`, `@angular/animations`) are mentioned where you will still meet them in real projects.

## Table of Contents

- [Easy Questions (1-150)](#easy-questions-1-150)
- [Moderate Questions (151-300)](#moderate-questions-151-300)
- [Advanced Questions (301-450)](#advanced-questions-301-450)

### Easy Questions (1-150)

- [1: What does performance optimization mean in an Angular app?](#1-what-does-performance-optimization-mean-in-an-angular-app)
- [2: What are the most common reasons an Angular app is slow?](#2-what-are-the-most-common-reasons-an-angular-app-is-slow)
- [3: What is change detection in Angular?](#3-what-is-change-detection-in-angular)
- [4: What triggers change detection in Angular?](#4-what-triggers-change-detection-in-angular)
- [5: What is Zone.js?](#5-what-is-zonejs)
- [6: What is zoneless change detection?](#6-what-is-zoneless-change-detection)
- [7: How do you enable zoneless change detection in an existing app?](#7-how-do-you-enable-zoneless-change-detection-in-an-existing-app)
- [8: What are the two change detection strategies?](#8-what-are-the-two-change-detection-strategies)
- [9: What is OnPush change detection?](#9-what-is-onpush-change-detection)
- [10: Why does OnPush make an app faster?](#10-why-does-onpush-make-an-app-faster)
- [11: What is a signal and how does it help performance?](#11-what-is-a-signal-and-how-does-it-help-performance)
- [12: What is a computed signal?](#12-what-is-a-computed-signal)
- [13: Why should you avoid calling methods in templates?](#13-why-should-you-avoid-calling-methods-in-templates)
- [14: What is a pure pipe?](#14-what-is-a-pure-pipe)
- [15: What is an impure pipe and why can it be slow?](#15-what-is-an-impure-pipe-and-why-can-it-be-slow)
- [16: What is the track expression in @for and why is it required?](#16-what-is-the-track-expression-in-for-and-why-is-it-required)
- [17: What should you use as the track value?](#17-what-should-you-use-as-the-track-value)
- [18: What is trackBy in \*ngFor?](#18-what-is-trackby-in-ngfor)
- [19: What is lazy loading?](#19-what-is-lazy-loading)
- [20: How do you lazy load a standalone component with the router?](#20-how-do-you-lazy-load-a-standalone-component-with-the-router)
- [21: How do you lazy load a group of routes?](#21-how-do-you-lazy-load-a-group-of-routes)
- [22: What is a bundle and what is a chunk?](#22-what-is-a-bundle-and-what-is-a-chunk)
- [23: Why does bundle size matter?](#23-why-does-bundle-size-matter)
- [24: How do you check the size of your bundles?](#24-how-do-you-check-the-size-of-your-bundles)
- [25: What is the difference between a development build and a production build?](#25-what-is-the-difference-between-a-development-build-and-a-production-build)
- [26: What is AOT compilation and how does it help performance?](#26-what-is-aot-compilation-and-how-does-it-help-performance)
- [27: What is tree shaking?](#27-what-is-tree-shaking)
- [28: What does providedIn: 'root' have to do with performance?](#28-what-does-providedin-root-have-to-do-with-performance)
- [29: What is @defer?](#29-what-is-defer)
- [30: What triggers can you use with @defer?](#30-what-triggers-can-you-use-with-defer)
- [31: What are the @placeholder, @loading and @error blocks?](#31-what-are-the-placeholder-loading-and-error-blocks)
- [32: What is prefetching in @defer?](#32-what-is-prefetching-in-defer)
- [33: What can and can't be deferred inside @defer?](#33-what-can-and-cant-be-deferred-inside-defer)
- [34: What is server-side rendering (SSR)?](#34-what-is-server-side-rendering-ssr)
- [35: What is hydration?](#35-what-is-hydration)
- [36: What is incremental hydration?](#36-what-is-incremental-hydration)
- [37: What is prerendering (SSG)?](#37-what-is-prerendering-ssg)
- [38: What is the difference between SSR, SSG and CSR?](#38-what-is-the-difference-between-ssr-ssg-and-csr)
- [39: What is NgOptimizedImage?](#39-what-is-ngoptimizedimage)
- [40: What does the priority attribute on NgOptimizedImage do?](#40-what-does-the-priority-attribute-on-ngoptimizedimage-do)
- [41: Why should images have width and height?](#41-why-should-images-have-width-and-height)
- [42: What is native lazy loading for images?](#42-what-is-native-lazy-loading-for-images)
- [43: What is a memory leak in an Angular app?](#43-what-is-a-memory-leak-in-an-angular-app)
- [44: How do you avoid memory leaks with subscriptions?](#44-how-do-you-avoid-memory-leaks-with-subscriptions)
- [45: What is the async pipe and why is it good for performance?](#45-what-is-the-async-pipe-and-why-is-it-good-for-performance)
- [46: What is takeUntilDestroyed?](#46-what-is-takeuntildestroyed)
- [47: What is Angular DevTools?](#47-what-is-angular-devtools)
- [48: How do you profile change detection with Angular DevTools?](#48-how-do-you-profile-change-detection-with-angular-devtools)
- [49: What is Lighthouse?](#49-what-is-lighthouse)
- [50: What are Core Web Vitals?](#50-what-are-core-web-vitals)
- [51: What is route preloading?](#51-what-is-route-preloading)
- [52: What is the difference between lazy loading and preloading?](#52-what-is-the-difference-between-lazy-loading-and-preloading)
- [53: What are standalone components and do they help performance?](#53-what-are-standalone-components-and-do-they-help-performance)
- [54: What is the virtual scroll in Angular CDK?](#54-what-is-the-virtual-scroll-in-angular-cdk)
- [55: When should you use virtual scrolling?](#55-when-should-you-use-virtual-scrolling)
- [56: What is pagination and why does it help?](#56-what-is-pagination-and-why-does-it-help)
- [57: What is the cost of a large DOM?](#57-what-is-the-cost-of-a-large-dom)
- [58: What is the difference between ng serve and ng build for performance testing?](#58-what-is-the-difference-between-ng-serve-and-ng-build-for-performance-testing)
- [59: What are build budgets?](#59-what-are-build-budgets)
- [60: What is minification?](#60-what-is-minification)
- [61: What is the difference between gzip and Brotli compression?](#61-what-is-the-difference-between-gzip-and-brotli-compression)
- [62: What is a CDN and why use it for an Angular app?](#62-what-is-a-cdn-and-why-use-it-for-an-angular-app)
- [63: Why do Angular build files have hashes in their names?](#63-why-do-angular-build-files-have-hashes-in-their-names)
- [64: What is output hashing configured with?](#64-what-is-output-hashing-configured-with)
- [65: What is the Angular service worker?](#65-what-is-the-angular-service-worker)
- [66: How do you cache HTTP responses in an Angular app?](#66-how-do-you-cache-http-responses-in-an-angular-app)
- [67: What is shareReplay and how does it help?](#67-what-is-sharereplay-and-how-does-it-help)
- [68: What is debouncing and where do you use it?](#68-what-is-debouncing-and-where-do-you-use-it)
- [69: What is throttling and how is it different from debouncing?](#69-what-is-throttling-and-how-is-it-different-from-debouncing)
- [70: Why is switchMap often used for HTTP calls?](#70-why-is-switchmap-often-used-for-http-calls)
- [71: What are the Angular animations performance concerns?](#71-what-are-the-angular-animations-performance-concerns)
- [72: Which CSS properties are cheap to animate?](#72-which-css-properties-are-cheap-to-animate)
- [73: What is a polyfill and why does it affect performance?](#73-what-is-a-polyfill-and-why-does-it-affect-performance)
- [74: What is the browserslist file?](#74-what-is-the-browserslist-file)
- [75: Why are some third-party libraries bad for performance?](#75-why-are-some-third-party-libraries-bad-for-performance)
- [76: What is the CommonJS warning in an Angular build?](#76-what-is-the-commonjs-warning-in-an-angular-build)
- [77: What does Angular do in development mode that it doesn't do in production?](#77-what-does-angular-do-in-development-mode-that-it-doesnt-do-in-production)
- [78: What is the ExpressionChangedAfterItHasBeenCheckedError?](#78-what-is-the-expressionchangedafterithasbeencheckederror)
- [79: What are lifecycle hooks and which ones can hurt performance?](#79-what-are-lifecycle-hooks-and-which-ones-can-hurt-performance)
- [80: What is the difference between ngOnInit and the constructor for performance?](#80-what-is-the-difference-between-ngoninit-and-the-constructor-for-performance)
- [81: What is the resource() API?](#81-what-is-the-resource-api)
- [82: What is httpResource?](#82-what-is-httpresource)
- [83: What is toSignal()?](#83-what-is-tosignal)
- [84: What is effect() and should you use it for state updates?](#84-what-is-effect-and-should-you-use-it-for-state-updates)
- [85: What is linkedSignal()?](#85-what-is-linkedsignal)
- [86: What does it mean that signals are "glitch-free"?](#86-what-does-it-mean-that-signals-are-glitch-free)
- [87: What are signal inputs?](#87-what-are-signal-inputs)
- [88: What is the @let block in templates?](#88-what-is-the-let-block-in-templates)
- [89: Why should you avoid subscribing to the same Observable twice in a template?](#89-why-should-you-avoid-subscribing-to-the-same-observable-twice-in-a-template)
- [90: What is the cost of global styles versus component styles?](#90-what-is-the-cost-of-global-styles-versus-component-styles)
- [91: What is critical CSS inlining?](#91-what-is-critical-css-inlining)
- [92: What is font inlining in Angular builds?](#92-what-is-font-inlining-in-angular-builds)
- [93: What is font-display: swap?](#93-what-is-font-display-swap)
- [94: What is preconnect and when do you use it?](#94-what-is-preconnect-and-when-do-you-use-it)
- [95: What is the difference between preload and prefetch?](#95-what-is-the-difference-between-preload-and-prefetch)
- [96: What image formats are best for performance?](#96-what-image-formats-are-best-for-performance)
- [97: What is an image loader in NgOptimizedImage?](#97-what-is-an-image-loader-in-ngoptimizedimage)
- [98: What does the fill attribute do in NgOptimizedImage?](#98-what-does-the-fill-attribute-do-in-ngoptimizedimage)
- [99: What is the placeholder option in NgOptimizedImage?](#99-what-is-the-placeholder-option-in-ngoptimizedimage)
- [100: What are the main tools to find performance problems in an Angular app?](#100-what-are-the-main-tools-to-find-performance-problems-in-an-angular-app)
- [101: What is the Chrome DevTools Performance panel used for?](#101-what-is-the-chrome-devtools-performance-panel-used-for)
- [102: What is a long task?](#102-what-is-a-long-task)
- [103: What is the main thread and why does it matter?](#103-what-is-the-main-thread-and-why-does-it-matter)
- [104: What is a web worker?](#104-what-is-a-web-worker)
- [105: What is the difference between initial load and runtime performance?](#105-what-is-the-difference-between-initial-load-and-runtime-performance)
- [106: What is Time to First Byte (TTFB)?](#106-what-is-time-to-first-byte-ttfb)
- [107: What is First Contentful Paint (FCP)?](#107-what-is-first-contentful-paint-fcp)
- [108: What is Largest Contentful Paint (LCP) and how do you improve it in Angular?](#108-what-is-largest-contentful-paint-lcp-and-how-do-you-improve-it-in-angular)
- [109: What is Cumulative Layout Shift (CLS) and how do you avoid it in Angular?](#109-what-is-cumulative-layout-shift-cls-and-how-do-you-avoid-it-in-angular)
- [110: What is Interaction to Next Paint (INP)?](#110-what-is-interaction-to-next-paint-inp)
- [111: Why should you measure on a real device or with CPU throttling?](#111-why-should-you-measure-on-a-real-device-or-with-cpu-throttling)
- [112: What is the difference between lab data and field data?](#112-what-is-the-difference-between-lab-data-and-field-data)
- [113: What are source maps and should you ship them to production?](#113-what-are-source-maps-and-should-you-ship-them-to-production)
- [114: What is the esbuild-based builder in Angular?](#114-what-is-the-esbuild-based-builder-in-angular)
- [115: What is hot module replacement (HMR) in Angular?](#115-what-is-hot-module-replacement-hmr-in-angular)
- [116: What is the purpose of the ngSkipHydration attribute?](#116-what-is-the-purpose-of-the-ngskiphydration-attribute)
- [117: What is TransferState?](#117-what-is-transferstate)
- [118: What is the HTTP transfer cache?](#118-what-is-the-http-transfer-cache)
- [119: What is event replay in hydration?](#119-what-is-event-replay-in-hydration)
- [120: What does isPlatformBrowser do?](#120-what-does-isplatformbrowser-do)
- [121: What is afterNextRender()?](#121-what-is-afternextrender)
- [122: Why should you set up third-party libraries outside Angular's change detection?](#122-why-should-you-set-up-third-party-libraries-outside-angulars-change-detection)
- [123: What is NgZone.runOutsideAngular()?](#123-what-is-ngzonerunoutsideangular)
- [124: What is event coalescing?](#124-what-is-event-coalescing)
- [125: Why are passive event listeners good for scrolling performance?](#125-why-are-passive-event-listeners-good-for-scrolling-performance)
- [126: Why is @HostListener on window scroll a problem?](#126-why-is-hostlistener-on-window-scroll-a-problem)
- [127: What is IntersectionObserver and why is it better than scroll events?](#127-what-is-intersectionobserver-and-why-is-it-better-than-scroll-events)
- [128: What is the async keyword's interaction with Zone.js?](#128-what-is-the-async-keywords-interaction-with-zonejs)
- [129: Why should you keep components small?](#129-why-should-you-keep-components-small)
- [130: What is the difference between a smart and a presentational component for performance?](#130-what-is-the-difference-between-a-smart-and-a-presentational-component-for-performance)
- [131: How does immutability help with OnPush?](#131-how-does-immutability-help-with-onpush)
- [132: What is the equal option of a signal?](#132-what-is-the-equal-option-of-a-signal)
- [133: What happens to a signal when you set the same value?](#133-what-happens-to-a-signal-when-you-set-the-same-value)
- [134: What is ChangeDetectorRef?](#134-what-is-changedetectorref)
- [135: What is the difference between markForCheck() and detectChanges()?](#135-what-is-the-difference-between-markforcheck-and-detectchanges)
- [136: What is the Angular CLI command to analyze a production build?](#136-what-is-the-angular-cli-command-to-analyze-a-production-build)
- [137: What is source-map-explorer?](#137-what-is-source-map-explorer)
- [138: What is the cost of importing a whole icon library?](#138-what-is-the-cost-of-importing-a-whole-icon-library)
- [139: Why is moment.js often called out in Angular performance reviews?](#139-why-is-momentjs-often-called-out-in-angular-performance-reviews)
- [140: What is the difference between lodash and lodash-es?](#140-what-is-the-difference-between-lodash-and-lodash-es)
- [141: Why should you keep index.html small and fast?](#141-why-should-you-keep-indexhtml-small-and-fast)
- [142: What is the cost of third-party scripts like analytics or chat widgets?](#142-what-is-the-cost-of-third-party-scripts-like-analytics-or-chat-widgets)
- [143: What does "do less work" mean for Angular performance?](#143-what-does-do-less-work-mean-for-angular-performance)
- [144: What is the purpose of the @empty block in @for?](#144-what-is-the-purpose-of-the-empty-block-in-for)
- [145: How is the built-in control flow faster than \*ngIf and \*ngFor?](#145-how-is-the-built-in-control-flow-faster-than-ngif-and-ngfor)
- [146: Can you lazy load a service?](#146-can-you-lazy-load-a-service)
- [147: What is ng update and how is it related to performance?](#147-what-is-ng-update-and-how-is-it-related-to-performance)
- [148: What is the difference between Eager and OnPush defaults in Angular 22?](#148-what-is-the-difference-between-eager-and-onpush-defaults-in-angular-22)
- [149: What are the first steps when someone says "the Angular app is slow"?](#149-what-are-the-first-steps-when-someone-says-the-angular-app-is-slow)
- [150: What is the cost of console.log in production code?](#150-what-is-the-cost-of-consolelog-in-production-code)

### Moderate Questions (151-300)

- [151: How does Angular decide which components to check in an OnPush tree?](#151-how-does-angular-decide-which-components-to-check-in-an-onpush-tree)
- [152: How do signals change the way OnPush components are refreshed?](#152-how-do-signals-change-the-way-onpush-components-are-refreshed)
- [153: What is a common bug when moving a component to OnPush?](#153-what-is-a-common-bug-when-moving-a-component-to-onpush)
- [154: How do you convert an Observable-based component to work well with OnPush and zoneless?](#154-how-do-you-convert-an-observable-based-component-to-work-well-with-onpush-and-zoneless)
- [155: What breaks when you remove Zone.js from an app?](#155-what-breaks-when-you-remove-zonejs-from-an-app)
- [156: How do you find components that will break in zoneless mode?](#156-how-do-you-find-components-that-will-break-in-zoneless-mode)
- [157: What does provideCheckNoChangesConfig do?](#157-what-does-providechecknochangesconfig-do)
- [158: How does zoneless change detection get scheduled?](#158-how-does-zoneless-change-detection-get-scheduled)
- [159: How do you migrate a large app from Eager to OnPush step by step?](#159-how-do-you-migrate-a-large-app-from-eager-to-onpush-step-by-step)
- [160: Why does mutating an array inside a signal not update the view?](#160-why-does-mutating-an-array-inside-a-signal-not-update-the-view)
- [161: How expensive is a computed() signal?](#161-how-expensive-is-a-computed-signal)
- [162: What is untracked() and when is it useful?](#162-what-is-untracked-and-when-is-it-useful)
- [163: How do you debounce a signal in Angular 22?](#163-how-do-you-debounce-a-signal-in-angular-22)
- [164: How do you combine signals and RxJS for a debounced search?](#164-how-do-you-combine-signals-and-rxjs-for-a-debounced-search)
- [165: What is the cost of effect() in terms of change detection?](#165-what-is-the-cost-of-effect-in-terms-of-change-detection)
- [166: What is afterRenderEffect() and when do you use it?](#166-what-is-afterrendereffect-and-when-do-you-use-it)
- [167: What is layout thrashing and how can it happen in Angular?](#167-what-is-layout-thrashing-and-how-can-it-happen-in-angular)
- [168: How do you optimize a large table in Angular?](#168-how-do-you-optimize-a-large-table-in-angular)
- [169: How do you configure CDK virtual scroll for better performance?](#169-how-do-you-configure-cdk-virtual-scroll-for-better-performance)
- [170: What are the limits of CDK virtual scroll?](#170-what-are-the-limits-of-cdk-virtual-scroll)
- [171: How do you write a custom preloading strategy?](#171-how-do-you-write-a-custom-preloading-strategy)
- [172: How do you skip preloading on slow networks?](#172-how-do-you-skip-preloading-on-slow-networks)
- [173: What is quicklink-style preloading?](#173-what-is-quicklink-style-preloading)
- [174: How do you decide what to put in a @defer block?](#174-how-do-you-decide-what-to-put-in-a-defer-block)
- [175: What does the minimum and after parameter do in @loading and @placeholder?](#175-what-does-the-minimum-and-after-parameter-do-in-loading-and-placeholder)
- [176: How do you avoid layout shift with @defer?](#176-how-do-you-avoid-layout-shift-with-defer)
- [177: How do you use on viewport and on interaction with a specific element?](#177-how-do-you-use-on-viewport-and-on-interaction-with-a-specific-element)
- [178: How do you test what goes into a @defer chunk?](#178-how-do-you-test-what-goes-into-a-defer-chunk)
- [179: How do @defer blocks behave during SSR?](#179-how-do-defer-blocks-behave-during-ssr)
- [180: What hydrate triggers are available for incremental hydration?](#180-what-hydrate-triggers-are-available-for-incremental-hydration)
- [181: What does hydrate never do?](#181-what-does-hydrate-never-do)
- [182: How do you turn off incremental hydration in Angular 22?](#182-how-do-you-turn-off-incremental-hydration-in-angular-22)
- [183: What causes hydration mismatches and why do they hurt performance?](#183-what-causes-hydration-mismatches-and-why-do-they-hurt-performance)
- [184: How do you verify that hydration is working?](#184-how-do-you-verify-that-hydration-is-working)
- [185: How do you configure render modes per route?](#185-how-do-you-configure-render-modes-per-route)
- [186: Why would you choose RenderMode.Client for some routes?](#186-why-would-you-choose-rendermodeclient-for-some-routes)
- [187: How do you prerender routes with parameters?](#187-how-do-you-prerender-routes-with-parameters)
- [188: How do you configure the HTTP transfer cache?](#188-how-do-you-configure-the-http-transfer-cache)
- [189: How do you cache server-rendered pages?](#189-how-do-you-cache-server-rendered-pages)
- [190: How do you avoid duplicate HTTP calls between server and client without HttpClient?](#190-how-do-you-avoid-duplicate-http-calls-between-server-and-client-without-httpclient)
- [191: What is PendingTasks and why does it matter for SSR?](#191-what-is-pendingtasks-and-why-does-it-matter-for-ssr)
- [192: What is pendingUntilEvent()?](#192-what-is-pendinguntilevent)
- [193: How do you set up the Angular service worker for caching app files?](#193-how-do-you-set-up-the-angular-service-worker-for-caching-app-files)
- [194: How do you cache API responses with the Angular service worker?](#194-how-do-you-cache-api-responses-with-the-angular-service-worker)
- [195: How do you register the service worker without hurting startup?](#195-how-do-you-register-the-service-worker-without-hurting-startup)
- [196: How do you handle service worker updates without stale code problems?](#196-how-do-you-handle-service-worker-updates-without-stale-code-problems)
- [197: How do you write a caching HTTP interceptor?](#197-how-do-you-write-a-caching-http-interceptor)
- [198: What changed in HttpClient in Angular 22 related to performance?](#198-what-changed-in-httpclient-in-angular-22-related-to-performance)
- [199: How do you cancel HTTP requests that are no longer needed?](#199-how-do-you-cancel-http-requests-that-are-no-longer-needed)
- [200: How do you avoid sending the same request from several components at once?](#200-how-do-you-avoid-sending-the-same-request-from-several-components-at-once)
- [201: What is the difference between shareReplay with refCount true and false?](#201-what-is-the-difference-between-sharereplay-with-refcount-true-and-false)
- [202: How do you make a list update fast when one item changes?](#202-how-do-you-make-a-list-update-fast-when-one-item-changes)
- [203: How does Angular's @for diffing work at a high level?](#203-how-does-angulars-for-diffing-work-at-a-high-level)
- [204: How do you handle a list where items can have duplicate ids?](#204-how-do-you-handle-a-list-where-items-can-have-duplicate-ids)
- [205: How do you measure how long a specific component takes to render?](#205-how-do-you-measure-how-long-a-specific-component-takes-to-render)
- [206: How do you enable Angular's integration with the Chrome DevTools Performance panel?](#206-how-do-you-enable-angulars-integration-with-the-chrome-devtools-performance-panel)
- [207: How do you find out why change detection runs so often?](#207-how-do-you-find-out-why-change-detection-runs-so-often)
- [208: What does a typical Angular DevTools flame graph show?](#208-what-does-a-typical-angular-devtools-flame-graph-show)
- [209: How do you find memory leaks in an Angular app?](#209-how-do-you-find-memory-leaks-in-an-angular-app)
- [210: What are detached DOM nodes and why do they matter?](#210-what-are-detached-dom-nodes-and-why-do-they-matter)
- [211: How do you clean up third-party libraries in a component?](#211-how-do-you-clean-up-third-party-libraries-in-a-component)
- [212: Why do services in root scope often cause memory leaks?](#212-why-do-services-in-root-scope-often-cause-memory-leaks)
- [213: How do you profile memory over time in Chrome?](#213-how-do-you-profile-memory-over-time-in-chrome)
- [214: How do you optimize forms with many fields?](#214-how-do-you-optimize-forms-with-many-fields)
- [215: What does updateOn: 'blur' do in reactive forms?](#215-what-does-updateon-blur-do-in-reactive-forms)
- [216: How do you debounce async validators?](#216-how-do-you-debounce-async-validators)
- [217: How do you use pure pipes for formatting instead of methods?](#217-how-do-you-use-pure-pipes-for-formatting-instead-of-methods)
- [218: How do you memoize a function in a component without signals?](#218-how-do-you-memoize-a-function-in-a-component-without-signals)
- [219: What is the cost of ngClass and ngStyle compared to class and style bindings?](#219-what-is-the-cost-of-ngclass-and-ngstyle-compared-to-class-and-style-bindings)
- [220: How do you speed up an app that has many event listeners in a list?](#220-how-do-you-speed-up-an-app-that-has-many-event-listeners-in-a-list)
- [221: What are the costs of using content projection (ng-content) heavily?](#221-what-are-the-costs-of-using-content-projection-ng-content-heavily)
- [222: How do you render content lazily with ng-template?](#222-how-do-you-render-content-lazily-with-ng-template)
- [223: How do you avoid running code twice on server and browser with SSR?](#223-how-do-you-avoid-running-code-twice-on-server-and-browser-with-ssr)
- [224: Why can a setInterval break or slow down SSR?](#224-why-can-a-setinterval-break-or-slow-down-ssr)
- [225: How do you lazy load a heavy library only when needed?](#225-how-do-you-lazy-load-a-heavy-library-only-when-needed)
- [226: How do you lazy load a component without the router?](#226-how-do-you-lazy-load-a-component-without-the-router)
- [227: How does route-level code splitting interact with shared code?](#227-how-does-route-level-code-splitting-interact-with-shared-code)
- [228: Do barrel files (index.ts) hurt bundle size?](#228-do-barrel-files-indexts-hurt-bundle-size)
- [229: What are side effects in modules and how do they affect tree shaking?](#229-what-are-side-effects-in-modules-and-how-do-they-affect-tree-shaking)
- [230: What does the allowedCommonJsDependencies option do?](#230-what-does-the-allowedcommonjsdependencies-option-do)
- [231: How do you set up budgets for lazy chunks too?](#231-how-do-you-set-up-budgets-for-lazy-chunks-too)
- [232: What is the "initial total" in the build output?](#232-what-is-the-initial-total-in-the-build-output)
- [233: How do you reduce the size of the main bundle?](#233-how-do-you-reduce-the-size-of-the-main-bundle)
- [234: What is the cost of providers in app.config.ts?](#234-what-is-the-cost-of-providers-in-appconfigts)
- [235: What are route-level providers?](#235-what-are-route-level-providers)
- [236: Why can provideAppInitializer slow down startup?](#236-why-can-provideappinitializer-slow-down-startup)
- [237: How do you speed up the time until the user sees something?](#237-how-do-you-speed-up-the-time-until-the-user-sees-something)
- [238: How do you analyze and reduce CSS size in an Angular app?](#238-how-do-you-analyze-and-reduce-css-size-in-an-angular-app)
- [239: Why can @import of a global Sass file in components increase bundle size?](#239-why-can-import-of-a-global-sass-file-in-components-increase-bundle-size)
- [240: What is ViewEncapsulation and does it affect performance?](#240-what-is-viewencapsulation-and-does-it-affect-performance)
- [241: How do you optimize fonts in an Angular app?](#241-how-do-you-optimize-fonts-in-an-angular-app)
- [242: How do you configure the image breakpoints for NgOptimizedImage?](#242-how-do-you-configure-the-image-breakpoints-for-ngoptimizedimage)
- [243: How do you use the sizes attribute with NgOptimizedImage?](#243-how-do-you-use-the-sizes-attribute-with-ngoptimizedimage)
- [244: How do you write a custom image loader?](#244-how-do-you-write-a-custom-image-loader)
- [245: What does NgOptimizedImage warn about in development mode?](#245-what-does-ngoptimizedimage-warn-about-in-development-mode)
- [246: How do you avoid too many priority images?](#246-how-do-you-avoid-too-many-priority-images)
- [247: How do you speed up Angular unit tests?](#247-how-do-you-speed-up-angular-unit-tests)
- [248: How do you speed up Angular builds in CI?](#248-how-do-you-speed-up-angular-builds-in-ci)
- [249: How do you configure the Angular CLI cache?](#249-how-do-you-configure-the-angular-cli-cache)
- [250: What is the cost of i18n in an Angular app and how do you keep it low?](#250-what-is-the-cost-of-i18n-in-an-angular-app-and-how-do-you-keep-it-low)
- [251: How do you keep a runtime translation pipe fast?](#251-how-do-you-keep-a-runtime-translation-pipe-fast)
- [252: How do you avoid blocking the UI when processing large data in the browser?](#252-how-do-you-avoid-blocking-the-ui-when-processing-large-data-in-the-browser)
- [253: How do you use a web worker generated by the Angular CLI?](#253-how-do-you-use-a-web-worker-generated-by-the-angular-cli)
- [254: What is the cost of sending data to a web worker?](#254-what-is-the-cost-of-sending-data-to-a-web-worker)
- [255: How do you make a dashboard with many widgets load faster?](#255-how-do-you-make-a-dashboard-with-many-widgets-load-faster)
- [256: How do you avoid request waterfalls in Angular?](#256-how-do-you-avoid-request-waterfalls-in-angular)
- [257: Are route resolvers good or bad for performance?](#257-are-route-resolvers-good-or-bad-for-performance)
- [258: How does withComponentInputBinding affect performance?](#258-how-does-withcomponentinputbinding-affect-performance)
- [259: How does Angular reuse components when only route params change?](#259-how-does-angular-reuse-components-when-only-route-params-change)
- [260: What is a RouteReuseStrategy and when would you use it for performance?](#260-what-is-a-routereusestrategy-and-when-would-you-use-it-for-performance)
- [261: How do you restore scroll position without extra work?](#261-how-do-you-restore-scroll-position-without-extra-work)
- [262: What are view transitions in the Angular router?](#262-what-are-view-transitions-in-the-angular-router)
- [263: How do you make a search input feel instant?](#263-how-do-you-make-a-search-input-feel-instant)
- [264: How do you handle frequent updates from WebSockets without killing performance?](#264-how-do-you-handle-frequent-updates-from-websockets-without-killing-performance)
- [265: What is the cost of console errors and warnings in dev mode?](#265-what-is-the-cost-of-console-errors-and-warnings-in-dev-mode)
- [266: How do you profile a slow click handler?](#266-how-do-you-profile-a-slow-click-handler)
- [267: How do you reduce work after a click in a big Angular page?](#267-how-do-you-reduce-work-after-a-click-in-a-big-angular-page)
- [268: How do you show feedback immediately during a slow operation?](#268-how-do-you-show-feedback-immediately-during-a-slow-operation)
- [269: How do you avoid heavy work in getters used in templates?](#269-how-do-you-avoid-heavy-work-in-getters-used-in-templates)
- [270: What is the problem with using the json pipe or functions in large lists?](#270-what-is-the-problem-with-using-the-json-pipe-or-functions-in-large-lists)
- [271: How do you check if Zone.js is still in your production bundle?](#271-how-do-you-check-if-zonejs-is-still-in-your-production-bundle)
- [272: What happens to NgZone in a zoneless app?](#272-what-happens-to-ngzone-in-a-zoneless-app)
- [273: What is the cost of afterEveryRender()?](#273-what-is-the-cost-of-aftereveryrender)
- [274: How do you use the Angular DevTools injector tree for performance work?](#274-how-do-you-use-the-angular-devtools-injector-tree-for-performance-work)
- [275: What is the cost of providing a service in a component's providers?](#275-what-is-the-cost-of-providing-a-service-in-a-components-providers)
- [276: How do you investigate a slow initial load in an Angular app?](#276-how-do-you-investigate-a-slow-initial-load-in-an-angular-app)
- [277: What is Total Blocking Time (TBT) and how does it relate to Angular?](#277-what-is-total-blocking-time-tbt-and-how-does-it-relate-to-angular)
- [278: How do you use the web-vitals library with Angular?](#278-how-do-you-use-the-web-vitals-library-with-angular)
- [279: How do you find which element is the LCP element?](#279-how-do-you-find-which-element-is-the-lcp-element)
- [280: How do you speed up a slow API response from the Angular side?](#280-how-do-you-speed-up-a-slow-api-response-from-the-angular-side)
- [281: What does optimistic UI mean and how do you do it in Angular?](#281-what-does-optimistic-ui-mean-and-how-do-you-do-it-in-angular)
- [282: How do you make lazy-loaded routes load faster on navigation?](#282-how-do-you-make-lazy-loaded-routes-load-faster-on-navigation)
- [283: What does modulepreload have to do with Angular builds?](#283-what-does-modulepreload-have-to-do-with-angular-builds)
- [284: How do you handle a very large NgModule-based shared module?](#284-how-do-you-handle-a-very-large-ngmodule-based-shared-module)
- [285: How do you migrate to the new control flow and why does it help performance?](#285-how-do-you-migrate-to-the-new-control-flow-and-why-does-it-help-performance)
- [286: How do you migrate inputs and queries to signals?](#286-how-do-you-migrate-inputs-and-queries-to-signals)
- [287: How does the inject() function relate to performance?](#287-how-does-the-inject-function-relate-to-performance)
- [288: How do you avoid loading data on the server that the client will load anyway?](#288-how-do-you-avoid-loading-data-on-the-server-that-the-client-will-load-anyway)
- [289: How do you keep SSR memory usage under control?](#289-how-do-you-keep-ssr-memory-usage-under-control)
- [290: How do you run SSR with Angular's Node app engine?](#290-how-do-you-run-ssr-with-angulars-node-app-engine)
- [291: Why should static files be served before the Angular SSR handler?](#291-why-should-static-files-be-served-before-the-angular-ssr-handler)
- [292: How do you cache SSR responses with headers?](#292-how-do-you-cache-ssr-responses-with-headers)
- [293: What is the cost of hydrating a big page all at once?](#293-what-is-the-cost-of-hydrating-a-big-page-all-at-once)
- [294: How do you decide which parts of a page to hydrate incrementally?](#294-how-do-you-decide-which-parts-of-a-page-to-hydrate-incrementally)
- [295: How does event replay work with incremental hydration?](#295-how-does-event-replay-work-with-incremental-hydration)
- [296: What is the trade-off of hydrate on interaction?](#296-what-is-the-trade-off-of-hydrate-on-interaction)
- [297: How do you avoid SSR rendering content that depends on the browser window size?](#297-how-do-you-avoid-ssr-rendering-content-that-depends-on-the-browser-window-size)
- [298: How do you lazy load a component inside a dialog?](#298-how-do-you-lazy-load-a-component-inside-a-dialog)
- [299: How do you reduce the number of change detection runs triggered by mouse movement?](#299-how-do-you-reduce-the-number-of-change-detection-runs-triggered-by-mouse-movement)
- [300: How do you build a fast autocomplete in Angular?](#300-how-do-you-build-a-fast-autocomplete-in-angular)

### Advanced Questions (301-450)

- [301: How does Angular's change detection work internally with LViews?](#301-how-does-angulars-change-detection-work-internally-with-lviews)
- [302: What does the compiled template function look like and why is it fast?](#302-what-does-the-compiled-template-function-look-like-and-why-is-it-fast)
- [303: How do signals mark views for refresh internally?](#303-how-do-signals-mark-views-for-refresh-internally)
- [304: What is the difference between markForCheck() and a signal change in how they mark the tree?](#304-what-is-the-difference-between-markforcheck-and-a-signal-change-in-how-they-mark-the-tree)
- [305: Why does an Eager component inside an OnPush parent behave unexpectedly?](#305-why-does-an-eager-component-inside-an-onpush-parent-behave-unexpectedly)
- [306: What does detach() really do and when is it worth using?](#306-what-does-detach-really-do-and-when-is-it-worth-using)
- [307: How does the zoneless scheduler avoid running change detection too often?](#307-how-does-the-zoneless-scheduler-avoid-running-change-detection-too-often)
- [308: What is error NG0103 and how does it relate to performance?](#308-what-is-error-ng0103-and-how-does-it-relate-to-performance)
- [309: How do effects get scheduled relative to change detection?](#309-how-do-effects-get-scheduled-relative-to-change-detection)
- [310: How would you design state for a large OnPush and zoneless app?](#310-how-would-you-design-state-for-a-large-onpush-and-zoneless-app)
- [311: Why is normalized state good for rendering performance?](#311-why-is-normalized-state-good-for-rendering-performance)
- [312: What is the cost of a computed() that depends on a large array?](#312-what-is-the-cost-of-a-computed-that-depends-on-a-large-array)
- [313: When should you use a custom equal function on computed()?](#313-when-should-you-use-a-custom-equal-function-on-computed)
- [314: How does Angular avoid "glitches" when several signals change at once?](#314-how-does-angular-avoid-glitches-when-several-signals-change-at-once)
- [315: How do you profile signal performance?](#315-how-do-you-profile-signal-performance)
- [316: How does Angular's @for algorithm handle moves efficiently?](#316-how-does-angulars-for-algorithm-handle-moves-efficiently)
- [317: What happens when you replace a list of 1,000 items with a new array with the same ids?](#317-what-happens-when-you-replace-a-list-of-1000-items-with-a-new-array-with-the-same-ids)
- [318: How do you render a list of 50,000 rows without virtual scrolling?](#318-how-do-you-render-a-list-of-50000-rows-without-virtual-scrolling)
- [319: What is content-visibility and how can it help Angular apps?](#319-what-is-content-visibility-and-how-can-it-help-angular-apps)
- [320: How do you build incremental rendering for a big list with signals?](#320-how-do-you-build-incremental-rendering-for-a-big-list-with-signals)
- [321: How does hydration match server DOM to client components?](#321-how-does-hydration-match-server-dom-to-client-components)
- [322: Why can HTML comment stripping by a CDN break hydration?](#322-why-can-html-comment-stripping-by-a-cdn-break-hydration)
- [323: What is the cost of serialized hydration data and how do you keep it small?](#323-what-is-the-cost-of-serialized-hydration-data-and-how-do-you-keep-it-small)
- [324: How does incremental hydration decide what code to download?](#324-how-does-incremental-hydration-decide-what-code-to-download)
- [325: What happens with signals and state changes inside a block that isn't hydrated yet?](#325-what-happens-with-signals-and-state-changes-inside-a-block-that-isnt-hydrated-yet)
- [326: How do you design a page with incremental hydration for the best INP?](#326-how-do-you-design-a-page-with-incremental-hydration-for-the-best-inp)
- [327: What are the main costs on the server for Angular SSR?](#327-what-are-the-main-costs-on-the-server-for-angular-ssr)
- [328: How would you load test an Angular SSR server?](#328-how-would-you-load-test-an-angular-ssr-server)
- [329: What is event loop lag and why does it matter for SSR?](#329-what-is-event-loop-lag-and-why-does-it-matter-for-ssr)
- [330: How do you avoid sharing state between requests in SSR?](#330-how-do-you-avoid-sharing-state-between-requests-in-ssr)
- [331: How do you decide between prerendering and SSR with caching?](#331-how-do-you-decide-between-prerendering-and-ssr-with-caching)
- [332: How do you prerender thousands of pages without slow builds?](#332-how-do-you-prerender-thousands-of-pages-without-slow-builds)
- [333: What are the internals of NgOptimizedImage's priority preloading in SSR?](#333-what-are-the-internals-of-ngoptimizedimages-priority-preloading-in-ssr)
- [334: How would you reduce LCP for a client-rendered Angular app without SSR?](#334-how-would-you-reduce-lcp-for-a-client-rendered-angular-app-without-ssr)
- [335: How does the build decide what goes into the initial chunk?](#335-how-does-the-build-decide-what-goes-into-the-initial-chunk)
- [336: How do you find why a library ended up in the initial bundle?](#336-how-do-you-find-why-a-library-ended-up-in-the-initial-bundle)
- [337: What is the cost of a large number of lazy chunks?](#337-what-is-the-cost-of-a-large-number-of-lazy-chunks)
- [338: How would you set up performance budgets in CI beyond bundle size?](#338-how-would-you-set-up-performance-budgets-in-ci-beyond-bundle-size)
- [339: How do you investigate high INP in production for an Angular app?](#339-how-do-you-investigate-high-inp-in-production-for-an-angular-app)
- [340: What is input delay and what causes it in Angular apps?](#340-what-is-input-delay-and-what-causes-it-in-angular-apps)
- [341: How do you split a long task in an Angular event handler?](#341-how-do-you-split-a-long-task-in-an-angular-event-handler)
- [342: Does Angular batch signal updates made in different tasks?](#342-does-angular-batch-signal-updates-made-in-different-tasks)
- [343: What is the cost of hydration on low-end devices and how do you measure it?](#343-what-is-the-cost-of-hydration-on-low-end-devices-and-how-do-you-measure-it)
- [344: How do you make Angular DevTools profiling results reliable?](#344-how-do-you-make-angular-devtools-profiling-results-reliable)
- [345: How can you profile a production build?](#345-how-can-you-profile-a-production-build)
- [346: What is the Long Animation Frames API and why is it useful for Angular apps?](#346-what-is-the-long-animation-frames-api-and-why-is-it-useful-for-angular-apps)
- [347: How do you track performance of route navigations?](#347-how-do-you-track-performance-of-route-navigations)
- [348: How does tree-shaking work with Angular's Ivy runtime?](#348-how-does-tree-shaking-work-with-angulars-ivy-runtime)
- [349: What is the cost of decorators like @Input in the final bundle?](#349-what-is-the-cost-of-decorators-like-input-in-the-final-bundle)
- [350: How does Angular handle styles per component and what is the runtime cost?](#350-how-does-angular-handle-styles-per-component-and-what-is-the-runtime-cost)
- [351: How does dependency injection affect startup time in a large app?](#351-how-does-dependency-injection-affect-startup-time-in-a-large-app)
- [352: How does injectAsync work and how do you prefetch with it?](#352-how-does-injectasync-work-and-how-do-you-prefetch-with-it)
- [353: What is the @Service decorator and does it help performance?](#353-what-is-the-service-decorator-and-does-it-help-performance)
- [354: How would you diagnose a slow app that uses NgRx Store heavily?](#354-how-would-you-diagnose-a-slow-app-that-uses-ngrx-store-heavily)
- [355: Why can a selector that returns a new array on every call hurt performance?](#355-why-can-a-selector-that-returns-a-new-array-on-every-call-hurt-performance)
- [356: How do you avoid re-rendering a whole page when a global store changes?](#356-how-do-you-avoid-re-rendering-a-whole-page-when-a-global-store-changes)
- [357: How do you make a real-time trading or monitoring screen fast in Angular?](#357-how-do-you-make-a-real-time-trading-or-monitoring-screen-fast-in-angular)
- [358: How would you use per-item signals for a large list with frequent updates?](#358-how-would-you-use-per-item-signals-for-a-large-list-with-frequent-updates)
- [359: What are the trade-offs of per-item signals?](#359-what-are-the-trade-offs-of-per-item-signals)
- [360: How do you design a component library to be fast by default?](#360-how-do-you-design-a-component-library-to-be-fast-by-default)
- [361: What are secondary entry points and why do they matter?](#361-what-are-secondary-entry-points-and-why-do-they-matter)
- [362: How does the CDK virtual scroll work internally?](#362-how-does-the-cdk-virtual-scroll-work-internally)
- [363: How do you write a custom virtual scroll strategy?](#363-how-do-you-write-a-custom-virtual-scroll-strategy)
- [364: How would you handle a list with variable and unknown item heights?](#364-how-would-you-handle-a-list-with-variable-and-unknown-item-heights)
- [365: How do you measure the real benefit of OnPush or zoneless before migrating a whole app?](#365-how-do-you-measure-the-real-benefit-of-onpush-or-zoneless-before-migrating-a-whole-app)
- [366: What is the risk of using OnPush everywhere with mutable data from a legacy service?](#366-what-is-the-risk-of-using-onpush-everywhere-with-mutable-data-from-a-legacy-service)
- [367: How do you handle third-party components that don't work with OnPush or zoneless?](#367-how-do-you-handle-third-party-components-that-dont-work-with-onpush-or-zoneless)
- [368: How do you keep an Angular Elements (web components) build small?](#368-how-do-you-keep-an-angular-elements-web-components-build-small)
- [369: How does Module Federation or Native Federation affect Angular performance?](#369-how-does-module-federation-or-native-federation-affect-angular-performance)
- [370: How would you reduce the cost of a large monolithic Angular app's startup?](#370-how-would-you-reduce-the-cost-of-a-large-monolithic-angular-apps-startup)
- [371: How do you deal with a slow first change detection run?](#371-how-do-you-deal-with-a-slow-first-change-detection-run)
- [372: What is the cost of many small components versus inline templates?](#372-what-is-the-cost-of-many-small-components-versus-inline-templates)
- [373: How do you optimize directives applied to many elements?](#373-how-do-you-optimize-directives-applied-to-many-elements)
- [374: How do you share one IntersectionObserver across many directive instances?](#374-how-do-you-share-one-intersectionobserver-across-many-directive-instances)
- [375: How do you optimize the ResizeObserver usage in a component?](#375-how-do-you-optimize-the-resizeobserver-usage-in-a-component)
- [376: How do you design an Angular app to work well on low-end Android devices?](#376-how-do-you-design-an-angular-app-to-work-well-on-low-end-android-devices)
- [377: How does the browser cache interact with Angular deployments?](#377-how-does-the-browser-cache-interact-with-angular-deployments)
- [378: How do you handle chunk load errors after a deploy?](#378-how-do-you-handle-chunk-load-errors-after-a-deploy)
- [379: How does the service worker's navigation handling affect performance?](#379-how-does-the-service-workers-navigation-handling-affect-performance)
- [380: How do you decide between performance and freshness strategies in dataGroups?](#380-how-do-you-decide-between-performance-and-freshness-strategies-in-datagroups)
- [381: How do you prevent a service worker from serving stale API data after logout?](#381-how-do-you-prevent-a-service-worker-from-serving-stale-api-data-after-logout)
- [382: How would you speed up the TypeScript type checking part of builds in a large app?](#382-how-would-you-speed-up-the-typescript-type-checking-part-of-builds-in-a-large-app)
- [383: What is the cost of strictTemplates and should you turn it off for speed?](#383-what-is-the-cost-of-stricttemplates-and-should-you-turn-it-off-for-speed)
- [384: How does an Nx monorepo help with build performance in Angular?](#384-how-does-an-nx-monorepo-help-with-build-performance-in-angular)
- [385: How would you set up a performance regression test for a key interaction?](#385-how-would-you-set-up-a-performance-regression-test-for-a-key-interaction)
- [386: How do you throttle the CPU in automated performance tests?](#386-how-do-you-throttle-the-cpu-in-automated-performance-tests)
- [387: How does Angular's SSR stream the response?](#387-how-does-angulars-ssr-stream-the-response)
- [388: What is the effect of slow server-side API calls on SSR and how do you limit it?](#388-what-is-the-effect-of-slow-server-side-api-calls-on-ssr-and-how-do-you-limit-it)
- [389: How do you add a timeout only for server-side HTTP requests?](#389-how-do-you-add-a-timeout-only-for-server-side-http-requests)
- [390: Why should SSR call APIs through internal URLs?](#390-why-should-ssr-call-apis-through-internal-urls)
- [391: How does the HTTP transfer cache build its cache keys?](#391-how-does-the-http-transfer-cache-build-its-cache-keys)
- [392: When does the HTTP transfer cache stop being used on the client?](#392-when-does-the-http-transfer-cache-stop-being-used-on-the-client)
- [393: How do you profile the SSR server's rendering?](#393-how-do-you-profile-the-ssr-servers-rendering)
- [394: What is the risk of rendering huge pages on the server?](#394-what-is-the-risk-of-rendering-huge-pages-on-the-server)
- [395: How do you keep hydration working with a third-party library that changes the DOM?](#395-how-do-you-keep-hydration-working-with-a-third-party-library-that-changes-the-dom)
- [396: How do you speed up an app that uses Angular Material heavily?](#396-how-do-you-speed-up-an-app-that-uses-angular-material-heavily)
- [397: How do you reduce the cost of mat-table or other complex tables?](#397-how-do-you-reduce-the-cost-of-mat-table-or-other-complex-tables)
- [398: What is the cost of change detection in deeply nested OnPush trees with markForCheck()?](#398-what-is-the-cost-of-change-detection-in-deeply-nested-onpush-trees-with-markforcheck)
- [399: How would you build a chart component that updates many times per second?](#399-how-would-you-build-a-chart-component-that-updates-many-times-per-second)
- [400: How do you decide if a performance optimization is worth it?](#400-how-do-you-decide-if-a-performance-optimization-is-worth-it)
- [401: Scenario: a product list page freezes for 2 seconds when filters change. How do you approach it?](#401-scenario-a-product-list-page-freezes-for-2-seconds-when-filters-change-how-do-you-approach-it)
- [402: Scenario: the app gets slower the longer a user keeps it open. What do you check?](#402-scenario-the-app-gets-slower-the-longer-a-user-keeps-it-open-what-do-you-check)
- [403: Scenario: Lighthouse shows a good score but users complain about slowness. Why?](#403-scenario-lighthouse-shows-a-good-score-but-users-complain-about-slowness-why)
- [404: Scenario: after enabling SSR, TTFB increased a lot. What can you do?](#404-scenario-after-enabling-ssr-ttfb-increased-a-lot-what-can-you-do)
- [405: Scenario: a dashboard sends 40 API requests on load. How do you improve it?](#405-scenario-a-dashboard-sends-40-api-requests-on-load-how-do-you-improve-it)
- [406: Scenario: a page has a high CLS score caused by an ad or banner loaded later. What do you do?](#406-scenario-a-page-has-a-high-cls-score-caused-by-an-ad-or-banner-loaded-later-what-do-you-do)
- [407: Scenario: a hydrated page re-renders completely after loading. How do you find the cause?](#407-scenario-a-hydrated-page-re-renders-completely-after-loading-how-do-you-find-the-cause)
- [408: Scenario: the initial bundle grew by 300 KB after a small feature was merged. How do you find out why?](#408-scenario-the-initial-bundle-grew-by-300-kb-after-a-small-feature-was-merged-how-do-you-find-out-why)
- [409: Scenario: a form with 200 fields lags on every keystroke. What would you check?](#409-scenario-a-form-with-200-fields-lags-on-every-keystroke-what-would-you-check)
- [410: Scenario: an app works fine on desktop but scrolling is janky on mobile. What can cause it?](#410-scenario-an-app-works-fine-on-desktop-but-scrolling-is-janky-on-mobile-what-can-cause-it)
- [411: Scenario: users report the app takes long to show anything after a deploy. Why might that be?](#411-scenario-users-report-the-app-takes-long-to-show-anything-after-a-deploy-why-might-that-be)
- [412: Scenario: Angular DevTools shows change detection running 60 times per second while the app is idle. What do you look for?](#412-scenario-angular-devtools-shows-change-detection-running-60-times-per-second-while-the-app-is-idle-what-do-you-look-for)
- [413: Scenario: a page with an infinite scroll feed becomes slow after loading many pages. How do you fix it?](#413-scenario-a-page-with-an-infinite-scroll-feed-becomes-slow-after-loading-many-pages-how-do-you-fix-it)
- [414: Scenario: a lazy route takes 3 seconds to open on 3G. How do you make it feel faster?](#414-scenario-a-lazy-route-takes-3-seconds-to-open-on-3g-how-do-you-make-it-feel-faster)
- [415: Scenario: memory keeps growing in a long-running kiosk app. How would you investigate?](#415-scenario-memory-keeps-growing-in-a-long-running-kiosk-app-how-would-you-investigate)
- [416: Scenario: an Angular app embedded in an iframe on a customer site is slow to start. What would you do?](#416-scenario-an-angular-app-embedded-in-an-iframe-on-a-customer-site-is-slow-to-start-what-would-you-do)
- [417: Scenario: a page with a large reactive form takes long to open. What can cause it and how to fix it?](#417-scenario-a-page-with-a-large-reactive-form-takes-long-to-open-what-can-cause-it-and-how-to-fix-it)
- [418: Scenario: switching tabs in a tab component is slow. What would you check?](#418-scenario-switching-tabs-in-a-tab-component-is-slow-what-would-you-check)
- [419: Scenario: an app with Zone.js has a Google Maps component and every map drag makes the whole app slow. Why and how do you fix it?](#419-scenario-an-app-with-zonejs-has-a-google-maps-component-and-every-map-drag-makes-the-whole-app-slow-why-and-how-do-you-fix-it)
- [420: Scenario: you need to show 100 charts on one page. How would you design it?](#420-scenario-you-need-to-show-100-charts-on-one-page-how-would-you-design-it)
- [421: How do you think about the trade-off between SSR and a fully static SPA on a CDN?](#421-how-do-you-think-about-the-trade-off-between-ssr-and-a-fully-static-spa-on-a-cdn)
- [422: Why might going zoneless not make your app noticeably faster?](#422-why-might-going-zoneless-not-make-your-app-noticeably-faster)
- [423: What is the risk of premature optimization in Angular projects?](#423-what-is-the-risk-of-premature-optimization-in-angular-projects)
- [424: How do you build a performance culture in an Angular team?](#424-how-do-you-build-a-performance-culture-in-an-angular-team)
- [425: How would you explain the performance difference between Angular's old and new reactivity models to a non-Angular developer?](#425-how-would-you-explain-the-performance-difference-between-angulars-old-and-new-reactivity-models-to-a-non-angular-developer)
- [426: How does @defer decide when to load dependencies when there are several triggers?](#426-how-does-defer-decide-when-to-load-dependencies-when-there-are-several-triggers)
- [427: What happens if a @defer block's chunk fails to load?](#427-what-happens-if-a-defer-blocks-chunk-fails-to-load)
- [428: How do you test the performance effect of @defer in unit tests?](#428-how-do-you-test-the-performance-effect-of-defer-in-unit-tests)
- [429: How would you design caching of reference data across the whole app?](#429-how-would-you-design-caching-of-reference-data-across-the-whole-app)
- [430: How do you use ETags with Angular HttpClient?](#430-how-do-you-use-etags-with-angular-httpclient)
- [431: How does the Fetch backend in Angular 22 affect caching?](#431-how-does-the-fetch-backend-in-angular-22-affect-caching)
- [432: How do you use fetch priority to improve LCP?](#432-how-do-you-use-fetch-priority-to-improve-lcp)
- [433: How do you avoid the "everything is critical" problem when preloading?](#433-how-do-you-avoid-the-everything-is-critical-problem-when-preloading)
- [434: How would you delay route preloading until the app is idle?](#434-how-would-you-delay-route-preloading-until-the-app-is-idle)
- [435: How do you measure the effect of preloading on users?](#435-how-do-you-measure-the-effect-of-preloading-on-users)
- [436: What is speculative loading with the Speculation Rules API and can Angular use it?](#436-what-is-speculative-loading-with-the-speculation-rules-api-and-can-angular-use-it)
- [437: How do you keep an Angular app fast as it grows to hundreds of routes?](#437-how-do-you-keep-an-angular-app-fast-as-it-grows-to-hundreds-of-routes)
- [438: How do you think about performance when choosing a state management approach?](#438-how-do-you-think-about-performance-when-choosing-a-state-management-approach)
- [439: How does the router's paramsInheritanceStrategy change in Angular 22 matter?](#439-how-does-the-routers-paramsinheritancestrategy-change-in-angular-22-matter)
- [440: How do you avoid reloading data when the user navigates back and forth?](#440-how-do-you-avoid-reloading-data-when-the-user-navigates-back-and-forth)
- [441: How do Angular's built-in animations (animate.enter and animate.leave) work, and why are they cheaper?](#441-how-do-angulars-built-in-animations-animateenter-and-animateleave-work-and-why-are-they-cheaper)
- [442: What does provideAnimationsAsync do and is it still relevant?](#442-what-does-provideanimationsasync-do-and-is-it-still-relevant)
- [443: How do you find out what is really in your polyfills and main chunks?](#443-how-do-you-find-out-what-is-really-in-your-polyfills-and-main-chunks)
- [444: How do you handle locale data for many languages without bloating bundles?](#444-how-do-you-handle-locale-data-for-many-languages-without-bloating-bundles)
- [445: How would you reduce JavaScript execution time during startup apart from bundle size?](#445-how-would-you-reduce-javascript-execution-time-during-startup-apart-from-bundle-size)
- [446: How do you prove that a performance fix worked in production?](#446-how-do-you-prove-that-a-performance-fix-worked-in-production)
- [447: What should you look for in a code review from a performance point of view?](#447-what-should-you-look-for-in-a-code-review-from-a-performance-point-of-view)
- [448: What are the trade-offs of using signals vs. RxJS for performance?](#448-what-are-the-trade-offs-of-using-signals-vs-rxjs-for-performance)
- [449: How does Angular's roadmap affect how you should optimize today?](#449-how-does-angulars-roadmap-affect-how-you-should-optimize-today)
- [450: If you could make only three changes to speed up a typical older Angular app, which would you pick?](#450-if-you-could-make-only-three-changes-to-speed-up-a-typical-older-angular-app-which-would-you-pick)

---

# Easy Questions (1-150)

## 1: What does performance optimization mean in an Angular app?

It means making the app load faster, react faster to user input and use less memory and CPU. In practice you work on two things:

- **Load performance**: how fast the first page shows up and becomes usable. Bundle size, lazy loading, images, fonts, SSR and caching matter here.
- **Runtime performance**: how fast the app responds after it has loaded. Change detection, rendering large lists, memory leaks and heavy JavaScript work matter here.

You should always measure first, then change something, then measure again.

## 2: What are the most common reasons an Angular app is slow?

The usual ones are:

- A big initial bundle because everything is loaded up front
- Too much change detection work (many components checked on every event)
- Large lists rendered all at once without `track` or virtual scrolling
- Heavy function calls inside templates
- Large, unoptimized images
- Memory leaks from subscriptions, timers or event listeners that are never cleaned up
- Too many HTTP requests or requests that are not cached
- Third-party libraries that are much bigger than needed

## 3: What is change detection in Angular?

Change detection is how Angular keeps the DOM in sync with your component state. When something might have changed, Angular walks the component tree, evaluates the template bindings and updates the DOM where a value is different from the last check.

It is one of the biggest factors in runtime performance. If Angular checks too many components too often, the app gets slow, especially on low-end devices.

## 4: What triggers change detection in Angular?

It depends on whether the app uses Zone.js or is zoneless.

With **Zone.js**, almost any async event triggers a check: DOM events, `setTimeout`, `setInterval`, promises, XHR and fetch callbacks.

In a **zoneless** app (the default for new apps since Angular 21), change detection runs only when Angular is told something changed:

- A signal read in a template is updated
- A bound DOM event handler runs
- `markForCheck()` is called (the `async` pipe calls it for you)
- An input of a component changes
- A view is attached or removed

## 5: What is Zone.js?

Zone.js is a library that patches browser async APIs like `setTimeout`, promises and `addEventListener`. Angular used it for many years to know when async work finished, so it could run change detection automatically.

The downside is that it adds to the bundle size and triggers change detection for every async event, even ones that change nothing in the UI. Modern Angular apps don't need it anymore.

## 6: What is zoneless change detection?

Zoneless means the app runs without Zone.js. Instead of reacting to every async event, Angular schedules change detection only when it gets a clear signal that state changed (signals, template event handlers, `markForCheck()`, input changes).

Benefits:

- Smaller bundle (no Zone.js)
- Fewer unnecessary change detection runs
- Easier to debug, cleaner stack traces
- Better compatibility with native `async`/`await`

New projects created with Angular 21 and later are zoneless by default. Older apps can add it with `provideZonelessChangeDetection()`.

## 7: How do you enable zoneless change detection in an existing app?

Add the provider and remove Zone.js from the polyfills:

```ts
// app.config.ts
import {
  ApplicationConfig,
  provideZonelessChangeDetection,
} from "@angular/core";

export const appConfig: ApplicationConfig = {
  providers: [provideZonelessChangeDetection()],
};
```

Then remove `"zone.js"` from the `polyfills` array in `angular.json` (and `zone.js/testing` from the test config). Before you switch, make sure your components use signals, the `async` pipe or `markForCheck()`, otherwise some views will stop updating.

## 8: What are the two change detection strategies?

- **Eager** (called `Default` before): the component is checked every time change detection runs anywhere in the app.
- **OnPush**: the component is checked only when one of its inputs changes, an event happens inside it, a signal it reads changes, or it is marked for check.

Since Angular 22, components without a `changeDetection` setting use **OnPush** by default. If you need the old behavior, set `ChangeDetectionStrategy.Eager`.

## 9: What is OnPush change detection?

OnPush tells Angular to skip a component (and its children) during change detection unless there is a reason to check it. A component is checked when:

- One of its inputs gets a new reference
- An event handler in its template runs
- A signal read in its template changes
- The `async` pipe receives a new value
- `markForCheck()` is called

```ts
@Component({
  selector: "app-user-card",
  changeDetection: ChangeDetectionStrategy.OnPush,
  template: `<p>{{ user().name }}</p>`,
})
export class UserCard {
  user = input.required<User>();
}
```

In Angular 22 and later you get this behavior without writing the `changeDetection` line.

## 10: Why does OnPush make an app faster?

Because Angular skips whole parts of the component tree. In a big app with hundreds of components, only the components whose data actually changed get checked. Less template evaluation means less CPU work per event, which is very noticeable on slow phones.

It also pushes you to use immutable data and signals, which makes data flow easier to follow.

## 11: What is a signal and how does it help performance?

A signal is a value that notifies Angular when it changes. When a template reads a signal, Angular knows that this view depends on it. When the signal changes, Angular marks only that view for checking.

```ts
count = signal(0);

increment() {
  this.count.update((c) => c + 1);
}
```

This is much more precise than Zone.js, which had no idea what changed and checked everything. Signals are the base for OnPush and zoneless apps.

## 12: What is a computed signal?

`computed()` creates a read-only signal that is derived from other signals. The value is cached and only recalculated when one of the signals it depends on changes.

```ts
items = signal<Item[]>([]);
total = computed(() => this.items().reduce((sum, i) => sum + i.price, 0));
```

If the template reads `total()` ten times, the sum is calculated once. That makes `computed()` a good replacement for methods called in templates.

## 13: Why should you avoid calling methods in templates?

A method in a template runs on every change detection pass for that component:

```html
<!-- runs on every check -->
<p>{{ getFullName() }}</p>
```

If the method does real work (filtering, sorting, formatting), this adds up quickly. Better options:

- A `computed()` signal
- A pure pipe
- A value calculated once when the data changes

Simple getters that just return a field are fine. The problem is expensive work.

## 14: What is a pure pipe?

A pure pipe only runs again when its input value changes (for objects and arrays, when the reference changes). Pipes are pure by default.

```ts
@Pipe({ name: "fullName" })
export class FullNamePipe implements PipeTransform {
  transform(user: User): string {
    return `${user.firstName} ${user.lastName}`;
  }
}
```

Angular caches the result, so using a pure pipe in a template is much cheaper than calling a method.

## 15: What is an impure pipe and why can it be slow?

An impure pipe (`pure: false`) runs on every change detection pass, even if the input did not change. The `async` pipe is an example.

If you write an impure pipe that filters or sorts a big array, it will run that work on every check. Use impure pipes only when you really need them, and keep their logic cheap.

## 16: What is the track expression in @for and why is it required?

`track` tells Angular how to identify each item in a list. When the list changes, Angular uses it to reuse existing DOM nodes instead of destroying and recreating them.

```html
@for (user of users(); track user.id) {
<app-user-row [user]="user" />
}
```

It is required because forgetting it was a very common performance problem with the old `*ngFor`. Without a good key, replacing the array (for example after an HTTP refresh) would re-render every row.

## 17: What should you use as the track value?

Use a unique and stable value from the item, usually an id:

```html
@for (product of products(); track product.id) { ... }
```

- `track $index` is fine for static lists that never reorder.
- `track item` (the object itself) only works if the same object references are kept between updates.

If the data comes from an API, the objects are new on every request, so tracking by identity will re-create the DOM. Track by id instead.

## 18: What is trackBy in *ngFor?

`trackBy` is the legacy version of `track`, used with `*ngFor`:

```ts
trackById(index: number, user: User) {
  return user.id;
}
```

```html
<li *ngFor="let user of users; trackBy: trackById">{{ user.name }}</li>
```

You will still see it in older code. In new code use `@for` with `track`, which is required and also faster.

## 19: What is lazy loading?

Lazy loading means loading a part of the app only when it is needed, instead of putting it in the initial bundle. In Angular you usually lazy load routes, so the code for a page is downloaded when the user navigates to it.

It makes the first load smaller and faster. Users don't pay for features they never open.

## 20: How do you lazy load a standalone component with the router?

Use `loadComponent`:

```ts
export const routes: Routes = [
  {
    path: "reports",
    loadComponent: () => import("./reports/reports").then((m) => m.Reports),
  },
];
```

If the component is the default export of the file, you can skip `.then()`:

```ts
{ path: "reports", loadComponent: () => import("./reports/reports") }
```

## 21: How do you lazy load a group of routes?

Use `loadChildren` and point it to a file that exports routes:

```ts
// app.routes.ts
{
  path: "admin",
  loadChildren: () => import("./admin/admin.routes").then((m) => m.ADMIN_ROUTES),
}
```

```ts
// admin/admin.routes.ts
export const ADMIN_ROUTES: Routes = [
  { path: "", component: AdminDashboard },
  { path: "users", component: AdminUsers },
];
```

All components used only in those routes go into a separate chunk.

## 22: What is a bundle and what is a chunk?

A bundle is the JavaScript file (or files) the build produces. The **initial bundle** is everything the browser needs to start the app (`main.js`, `polyfills.js`, `styles.css` and shared chunks they import).

A **chunk** is a separate file that is loaded later, for example for a lazy route or a `@defer` block. The build output shows initial chunks and lazy chunks separately, with their sizes.

## 23: Why does bundle size matter?

The browser has to download, parse, compile and run all JavaScript before the app becomes interactive. A bigger bundle means:

- Longer download, especially on mobile networks
- More CPU time to parse and run, especially on cheap phones
- Worse Core Web Vitals (LCP, INP)

Keeping the initial bundle small is one of the most effective ways to make an Angular app feel fast.

## 24: How do you check the size of your bundles?

Run a production build:

```bash
ng build
```

The CLI prints a table with each output file, its raw size and its estimated transfer size, split into initial and lazy chunks. For more detail, generate a stats file and open it in a bundle analyzer:

```bash
ng build --stats-json
```

## 25: What is the difference between a development build and a production build?

A production build (the default for `ng build`) turns on:

- Minification and tree shaking
- Removing dev-only checks (`ngDevMode` code)
- Hashing file names for caching
- CSS optimization and critical CSS inlining
- No source maps by default

The dev build used by `ng serve` skips most of this so rebuilds are fast. Never measure performance on `ng serve` output, it is much slower and bigger than what users get.

## 26: What is AOT compilation and how does it help performance?

AOT (ahead-of-time) compilation turns templates into JavaScript at build time instead of in the browser. It has been the default for years.

It helps because:

- The browser doesn't need the Angular compiler, so the bundle is smaller
- Templates don't have to be compiled at startup, so the app starts faster
- Template errors are caught at build time

## 27: What is tree shaking?

Tree shaking is removing code that is never used from the final bundle. The bundler looks at `import` and `export` statements and drops whatever nothing imports.

To get the most out of it:

- Use ES module libraries (not CommonJS)
- Import only what you need (`import { debounceTime } from "rxjs"`)
- Use `providedIn: "root"` for services so unused services can be dropped
- Use standalone components instead of big shared NgModules

## 28: What does providedIn: 'root' have to do with performance?

A service with `providedIn: "root"` is tree-shakable. If nothing injects it, the bundler removes it from the build. If it's only used in a lazy loaded route, it ends up in that lazy chunk.

```ts
@Injectable({ providedIn: "root" })
export class ReportsService {}
```

Services listed in a `providers` array are always included, whether used or not. Angular 22 also adds the `@Service()` decorator, which is `providedIn: "root"` by default.

## 29: What is @defer?

`@defer` lets you lazy load part of a template. The components, directives and pipes used inside the block are split into a separate chunk and loaded only when a trigger fires.

```html
@defer (on viewport) {
<app-comments [postId]="postId()" />
} @placeholder {
<p>Comments</p>
}
```

It is useful for heavy parts of a page that the user doesn't need right away, like charts, comments, maps or editors.

## 30: What triggers can you use with @defer?

- `on idle`: when the browser is idle (the default)
- `on viewport`: when the block (or a placeholder) scrolls into view
- `on interaction`: when the user clicks or presses a key on an element
- `on hover`: when the user hovers or focuses an element
- `on immediate`: right after the page finishes rendering
- `on timer(2s)`: after a delay
- `when condition`: when an expression becomes true

You can combine them: `@defer (on viewport; on timer(5s))`.

## 31: What are the @placeholder, @loading and @error blocks?

- `@placeholder`: shown before the defer block starts loading. Required for triggers like `on viewport` that need an element to watch.
- `@loading`: shown while the chunk is being downloaded.
- `@error`: shown if loading failed.

```html
@defer (on viewport) {
<app-chart [data]="data()" />
} @placeholder {
<div class="chart-box"></div>
} @loading (minimum 500ms) {
<app-spinner />
} @error {
<p>Could not load the chart.</p>
}
```

## 32: What is prefetching in @defer?

Prefetching downloads the chunk earlier than it is shown. The trigger decides when to load the code, and `prefetch` decides when to download it.

```html
@defer (on interaction; prefetch on idle) {
<app-editor />
} @placeholder {
<button>Open editor</button>
}
```

Here the editor code is downloaded when the browser is idle, so when the user clicks, it shows up almost immediately.

## 33: What can and can't be deferred inside @defer?

Only **standalone** components, directives and pipes can be deferred, and only if they are not used anywhere else in the same file outside a `@defer` block. If you also import them directly somewhere else in the component, they get loaded eagerly.

Code inside the `@placeholder`, `@loading` and `@error` blocks is loaded eagerly, so keep it light.

## 34: What is server-side rendering (SSR)?

SSR means the server runs the Angular app and sends fully rendered HTML to the browser. The user sees content before the JavaScript has loaded.

Benefits:

- Faster first content and better LCP
- Better SEO and link previews
- Content is visible on slow devices sooner

You add it with `ng add @angular/ssr` or choose it when running `ng new`.

## 35: What is hydration?

Hydration is the process where Angular in the browser takes over the HTML that came from the server. Instead of throwing it away and rendering again, it reuses the existing DOM nodes and attaches event listeners.

This avoids a flicker, saves work and improves LCP and CLS. You enable it with `provideClientHydration()`:

```ts
providers: [provideClientHydration()];
```

## 36: What is incremental hydration?

Incremental hydration lets parts of the page stay as static server HTML until they are needed. You mark them with `@defer` and a `hydrate` trigger:

```html
@defer (hydrate on viewport) {
<app-reviews />
}
```

The JavaScript for `app-reviews` is downloaded and the block is hydrated only when it scrolls into view. The user still sees the HTML right away. Since Angular 22, `provideClientHydration()` turns incremental hydration on by default.

## 37: What is prerendering (SSG)?

Prerendering renders pages to static HTML at build time. The server (or a CDN) just sends the saved file, so no rendering happens per request.

It's good for pages that are the same for every user, like a landing page, docs or blog posts. In Angular you set it per route with `RenderMode.Prerender` in the server routes config.

## 38: What is the difference between SSR, SSG and CSR?

- **CSR** (client-side rendering): the server sends an almost empty HTML page, the browser downloads JS and renders everything.
- **SSR**: the server renders HTML on each request.
- **SSG / prerendering**: HTML is rendered once at build time.

Angular lets you mix them per route: prerender static pages, server render dynamic ones, and use client rendering for pages behind login.

## 39: What is NgOptimizedImage?

`NgOptimizedImage` is a directive that applies image best practices for you. You use it by replacing `src` with `ngSrc`:

```ts
import { NgOptimizedImage } from "@angular/common";

@Component({
  imports: [NgOptimizedImage],
  template: `<img ngSrc="/hero.jpg" width="1200" height="600" priority />`,
})
export class Hero {}
```

It sets lazy loading for non-priority images, requires width and height to avoid layout shifts, generates `srcset` when a loader is configured, and warns in dev mode when something is wrong.

## 40: What does the priority attribute on NgOptimizedImage do?

It marks an image as important, usually the LCP image (the biggest image above the fold). Angular then:

- Sets `fetchpriority="high"`
- Sets `loading="eager"`
- Adds a preload link when using SSR

```html
<img ngSrc="/banner.webp" width="1600" height="500" priority />
```

In dev mode, Angular warns you if the LCP image doesn't have `priority`.

## 41: Why should images have width and height?

Without them, the browser doesn't know how much space to reserve, so the content below jumps when the image loads. That's a layout shift and it hurts the CLS score.

`NgOptimizedImage` requires `width` and `height` (or the `fill` attribute) for this reason. The values set the aspect ratio. You can still make the image responsive with CSS.

## 42: What is native lazy loading for images?

The `loading="lazy"` attribute tells the browser to load the image only when it's close to the viewport.

```html
<img src="/photo.jpg" loading="lazy" width="400" height="300" alt="" />
```

`NgOptimizedImage` adds it automatically for images that are not marked `priority`. Don't lazy load the main above-the-fold image, it makes LCP worse.

## 43: What is a memory leak in an Angular app?

A memory leak happens when objects are kept in memory after they are no longer needed. In Angular, the usual cause is a component that is destroyed but something still holds a reference to it, like:

- An RxJS subscription that never completes
- A `setInterval` that is never cleared
- A global event listener added with `addEventListener`
- A service that stores references to components

Over time the app uses more and more memory and gets slower.

## 44: How do you avoid memory leaks with subscriptions?

The common options are:

- Use the `async` pipe, which unsubscribes automatically
- Convert to a signal with `toSignal()`
- Use `takeUntilDestroyed()` from `@angular/core/rxjs-interop`

```ts
export class Prices {
  constructor() {
    inject(PriceService)
      .stream()
      .pipe(takeUntilDestroyed())
      .subscribe((p) => this.price.set(p));
  }

  price = signal(0);
}
```

HTTP requests from `HttpClient` complete on their own, so they don't leak in most cases.

## 45: What is the async pipe and why is it good for performance?

The `async` pipe subscribes to an Observable or Promise in the template, returns the latest value and unsubscribes when the component is destroyed. It also calls `markForCheck()` when a new value arrives, so it works with OnPush.

```html
@if (user$ | async; as user) {
<p>{{ user.name }}</p>
}
```

In new code, `toSignal()` is often simpler, but the `async` pipe is still common.

## 46: What is takeUntilDestroyed?

`takeUntilDestroyed()` is an RxJS operator from `@angular/core/rxjs-interop`. It completes the Observable when the component, directive or service that uses it is destroyed.

```ts
constructor() {
  this.route.paramMap.pipe(takeUntilDestroyed()).subscribe(...);
}
```

Called in an injection context (constructor or field initializer) it finds the `DestroyRef` on its own. Outside one, pass a `DestroyRef` to it.

## 47: What is Angular DevTools?

Angular DevTools is a browser extension for Chrome and Firefox. It lets you:

- Inspect the component tree, inputs, signals and state
- Profile change detection and see which components took the longest
- Look at the injector tree
- See the router tree

It works with apps running in development mode.

## 48: How do you profile change detection with Angular DevTools?

1. Open DevTools and go to the **Angular** tab.
2. Open the **Profiler** and click record.
3. Do the slow action in the app.
4. Stop recording.

You get a bar chart of change detection cycles. Clicking a cycle shows which components were checked and how long each took. Look for cycles that are long or happen too often, and for components checked when nothing changed.

## 49: What is Lighthouse?

Lighthouse is a tool built into Chrome DevTools that audits a page for performance, accessibility, SEO and best practices. For performance it measures metrics like LCP, CLS and Total Blocking Time and gives a list of suggestions (unused JavaScript, big images, render-blocking resources).

Run it on a production build, ideally in an incognito window so extensions don't affect the result.

## 50: What are Core Web Vitals?

They are three metrics Google uses to measure user experience:

- **LCP** (Largest Contentful Paint): how fast the main content shows up. Good is under 2.5 s.
- **INP** (Interaction to Next Paint): how fast the page responds to user input. Good is under 200 ms.
- **CLS** (Cumulative Layout Shift): how much the layout jumps. Good is under 0.1.

In Angular, LCP is affected by bundle size, SSR and images. INP is affected by change detection and heavy event handlers. CLS is affected by images without sizes and late-loading content.

## 51: What is route preloading?

Preloading downloads lazy loaded route chunks in the background after the app has started. The first load stays small, but when the user navigates, the code is often already there.

```ts
import {
  PreloadAllModules,
  provideRouter,
  withPreloading,
} from "@angular/router";

providers: [provideRouter(routes, withPreloading(PreloadAllModules))];
```

By default Angular uses `NoPreloading`, so lazy routes load only on navigation.

## 52: What is the difference between lazy loading and preloading?

Lazy loading moves code out of the initial bundle. Preloading decides when that lazy code gets downloaded.

- Lazy loading only: the chunk is downloaded when the user navigates to the route.
- Lazy loading + preloading: the chunk is downloaded in the background after startup, before the user asks for it.

You still get a small initial bundle in both cases.

## 53: What are standalone components and do they help performance?

Standalone components declare their own dependencies with `imports` instead of belonging to an NgModule. They are the default since Angular 19.

They help performance because the dependency graph is more precise. The bundler can see exactly what each component uses, which makes lazy loading and `@defer` easier and leaves less unused code in each chunk. With big shared NgModules, a lazy route often pulled in components it never used.

## 54: What is the virtual scroll in Angular CDK?

Virtual scrolling renders only the items that are visible on screen (plus a small buffer), instead of the whole list. As the user scrolls, the same DOM nodes are reused for new items.

```html
<cdk-virtual-scroll-viewport itemSize="48" class="list">
  <div *cdkVirtualFor="let item of items; trackBy: trackById">
    {{ item.name }}
  </div>
</cdk-virtual-scroll-viewport>
```

With 10,000 items you might only have 20-30 rows in the DOM. It comes from `@angular/cdk/scrolling`.

## 55: When should you use virtual scrolling?

Use it for long lists (hundreds or thousands of rows) where all items look similar and have a known or predictable height, like logs, chat history, product lists or tables.

For short lists it's not worth the added complexity. Also consider plain pagination or "load more" buttons, which are simpler and often good enough.

## 56: What is pagination and why does it help?

Pagination means loading and showing data in pages, for example 20 items at a time. It helps because:

- The API returns less data, so responses are faster
- The browser renders fewer DOM nodes
- Memory use stays low

It's often the simplest fix for a slow list. Infinite scrolling and "load more" are variants of the same idea.

## 57: What is the cost of a large DOM?

Every DOM node uses memory and takes time to create, style and lay out. With a large DOM:

- Initial rendering is slower
- Style recalculation and layout take longer on every change
- Change detection has more bindings to check
- Scrolling can feel janky

Lighthouse warns when a page has more than about 1,400 nodes. Pagination, virtual scrolling and `@defer` help keep the DOM small.

## 58: What is the difference between ng serve and ng build for performance testing?

`ng serve` runs a development build with no minification, extra dev checks, source maps and a dev server. It's built for fast rebuilds, not fast runtime.

`ng build` creates an optimized production build by default. For any performance test, run `ng build` and serve the `dist` folder with a static server or your SSR server:

```bash
ng build
npx http-server dist/my-app/browser
```

## 59: What are build budgets?

Budgets are size limits in `angular.json`. If a bundle goes over a limit, the build shows a warning or fails.

```json
"budgets": [
  { "type": "initial", "maximumWarning": "500kB", "maximumError": "1MB" },
  { "type": "anyComponentStyle", "maximumWarning": "4kB", "maximumError": "8kB" }
]
```

They help catch size regressions early, for example when someone adds a big library by mistake.

## 60: What is minification?

Minification removes whitespace, comments and long names from JavaScript and CSS, and rewrites code into a shorter form. The behavior stays the same, the file gets much smaller.

The Angular CLI minifies scripts and styles automatically in production builds, using esbuild.

## 61: What is the difference between gzip and Brotli compression?

Both compress text files (JS, CSS, HTML, JSON) before they are sent over the network. Brotli usually produces smaller files than gzip, often 15-20% smaller for JavaScript.

The Angular CLI doesn't compress files itself. Compression is done by the web server, CDN or hosting platform. Make sure it is turned on, because it often cuts transfer size by 70% or more.

## 62: What is a CDN and why use it for an Angular app?

A CDN (content delivery network) stores copies of your static files on servers around the world. Users download them from a server close to them, which lowers latency.

An Angular production build is mostly static files (JS, CSS, images, fonts), so it's a perfect fit. Most CDNs also handle compression, HTTP/2 or HTTP/3, and caching for you.

## 63: Why do Angular build files have hashes in their names?

Production builds add a content hash to file names, like `main-ABC123.js`. When the code changes, the hash changes, so the file name changes.

This lets you cache these files for a very long time (`Cache-Control: max-age=31536000, immutable`). When you deploy, the browser downloads only the files whose names changed. `index.html` should not be cached long, because it points to the new file names.

## 64: What is output hashing configured with?

The `outputHashing` option in `angular.json`. In production it is `"all"` by default:

- `all`: hash scripts, styles and media files
- `bundles`: hash only scripts and styles
- `media`: hash only media files
- `none`: no hashes

Keep it on `all` for production so you can cache files safely.

## 65: What is the Angular service worker?

`@angular/service-worker` is a ready-made service worker that caches your app files and selected API responses. After the first visit, the app can load from the cache, even offline.

You add it with:

```bash
ng add @angular/pwa
```

This creates `ngsw-config.json` where you configure what gets cached and how.

## 66: How do you cache HTTP responses in an Angular app?

There are a few levels:

- **Browser HTTP cache**: set `Cache-Control` headers on the API.
- **In-memory cache in a service**: store results in a signal or with `shareReplay`.
- **Interceptor cache**: an `HttpInterceptorFn` that returns stored responses for repeated GET requests.
- **Service worker data groups**: cache API responses in `ngsw-config.json`.
- **SSR transfer cache**: reuse server responses in the browser after hydration.

The right one depends on how fresh the data needs to be.

## 67: What is shareReplay and how does it help?

`shareReplay` makes several subscribers share one execution of an Observable and replays the last value to new subscribers. Without it, every subscription to an HTTP Observable sends a new request.

```ts
readonly countries$ = this.http.get<Country[]>("/api/countries").pipe(
  shareReplay({ bufferSize: 1, refCount: false }),
);
```

Here the request is made once and every component reuses the result.

## 68: What is debouncing and where do you use it?

Debouncing waits until something stops happening for a set time before acting. The classic use is a search box: don't call the API on every keystroke, wait until the user pauses.

```ts
this.search.valueChanges.pipe(
  debounceTime(300),
  distinctUntilChanged(),
  switchMap((q) => this.api.search(q)),
);
```

This cuts the number of requests and the amount of rendering a lot.

## 69: What is throttling and how is it different from debouncing?

Throttling allows an action at most once per time window, no matter how often the event fires. Debouncing waits until the events stop.

- Throttle: good for scroll or resize handlers where you want regular updates.
- Debounce: good for search input where you only care about the final value.

RxJS has `throttleTime()` and `debounceTime()` for both.

## 70: Why is switchMap often used for HTTP calls?

`switchMap` cancels the previous inner Observable when a new value arrives. For HTTP, that means an old request is cancelled when a new one starts.

```ts
this.query$.pipe(switchMap((q) => this.http.get(`/api/search?q=${q}`)));
```

This avoids wasted work and also prevents old responses from overwriting newer ones. With `mergeMap`, all requests would run and finish in random order.

## 71: What are the Angular animations performance concerns?

The legacy `@angular/animations` package adds JavaScript to the bundle and runs animation logic in JS. It was deprecated in Angular 20.2.

The modern approach is native CSS animations with `animate.enter` and `animate.leave`:

```html
@if (open()) {
<div class="panel" animate.enter="slide-in" animate.leave="slide-out"></div>
}
```

CSS animations of `transform` and `opacity` can run on the GPU and don't block the main thread, and you don't ship the animations package.

## 72: Which CSS properties are cheap to animate?

`transform` and `opacity`. The browser can animate them on the compositor without recalculating layout or repainting.

Animating `width`, `height`, `top`, `left` or `margin` triggers layout on every frame, which is much slower. For example, to slide an element, use `transform: translateX()` instead of changing `left`.

## 73: What is a polyfill and why does it affect performance?

A polyfill is code that adds a feature missing in older browsers. Each one adds to the bundle.

Angular targets modern browsers only, so the default `polyfills` list is usually just `zone.js` (or nothing in a zoneless app). Avoid adding polyfills you don't need, and check your `browserslist` config so you don't target very old browsers.

## 74: What is the browserslist file?

`.browserslistrc` (or the `browserslist` key in `package.json`) tells the build which browsers to support. The CLI uses it to decide which JavaScript syntax and CSS prefixes to output.

If the list includes old browsers, the build has to transform modern syntax into longer code, which makes bundles bigger. Angular already has a sensible default, so only add this file if you really need different targets.

## 75: Why are some third-party libraries bad for performance?

Some libraries are large, not tree-shakable or written as CommonJS. Importing one function might pull in the whole library. Examples are full builds of `moment` or `lodash`.

Before adding a library:

- Check its size on bundlephobia.com or pkg-size.dev
- Prefer ES module versions (`lodash-es`, `date-fns`)
- Check if a native API can do the job (`Intl.DateTimeFormat`, `structuredClone`)
- Load it lazily if it's only needed on one page

## 76: What is the CommonJS warning in an Angular build?

When a dependency is published as CommonJS (`require`/`module.exports`), the build prints a warning like "Module 'x' used by 'y' is not ESM". CommonJS can't be tree-shaken well, so it often adds more code than needed.

The fix is to use an ES module version of the library or a different library. If you have to keep it, you can silence the warning with `allowedCommonJsDependencies` in `angular.json`, but the size cost stays.

## 77: What does Angular do in development mode that it doesn't do in production?

In dev mode Angular runs extra checks to help you find bugs:

- It runs change detection a second time to catch `ExpressionChangedAfterItHasBeenCheckedError`
- It prints detailed error messages and warnings (like `NgOptimizedImage` hints)
- It keeps debugging info for Angular DevTools

All of this is removed in production builds because the code is wrapped in `ngDevMode` checks that get stripped. That's why dev mode is slower.

## 78: What is the ExpressionChangedAfterItHasBeenCheckedError?

It's a dev-mode error that shows when a binding value changes during the same change detection cycle, after Angular already checked it. Angular runs a second check in dev mode to find this.

It is not a performance problem by itself, but it often points to a design problem, like changing parent state from a child's lifecycle hook. Fix the data flow instead of hiding it with `setTimeout`.

## 79: What are lifecycle hooks and which ones can hurt performance?

Lifecycle hooks are methods Angular calls at certain moments, like `ngOnInit` or `ngOnDestroy`.

The risky ones run very often:

- `ngDoCheck`: runs on every change detection pass for the component
- `ngAfterViewChecked` and `ngAfterContentChecked`: run after every check

Any heavy work in these hooks is repeated constantly. Keep them empty or very light, or use signals and `computed()` instead.

## 80: What is the difference between ngOnInit and the constructor for performance?

Both run once per component, so neither is a performance problem by itself. The constructor should only set up fields and inject dependencies. `ngOnInit` runs after the first inputs are set, so it's where you start work that depends on inputs.

What matters more is not doing slow, blocking work in either one. Start async work (HTTP calls, resources) and let the template show a loading state.

## 81: What is the resource() API?

`resource()` loads async data and exposes it as signals. When its `params` change, it loads again and cancels the old request.

```ts
userId = input.required<string>();

user = resource({
  params: () => ({ id: this.userId() }),
  loader: ({ params, abortSignal }) =>
    fetch(`/api/users/${params.id}`, { signal: abortSignal }).then((r) =>
      r.json(),
    ),
});
```

You read `user.value()`, `user.isLoading()` and `user.error()` in the template. It works well with OnPush and zoneless apps. It became stable in Angular 22.

## 82: What is httpResource?

`httpResource` is a version of `resource()` built on `HttpClient`. You give it a function that returns a URL (or request object), and it fetches the data whenever the signals in that function change.

```ts
query = signal("");
results = httpResource<Product[]>(() => `/api/products?q=${this.query()}`);
```

It goes through your interceptors and cancels old requests when the URL changes, so you don't need `switchMap` here.

## 83: What is toSignal()?

`toSignal()` converts an Observable into a signal. It subscribes right away and unsubscribes when the injection context (usually the component) is destroyed.

```ts
private route = inject(ActivatedRoute);
id = toSignal(this.route.paramMap.pipe(map((p) => p.get("id"))));
```

It's an easy way to use RxJS data in OnPush or zoneless components without the `async` pipe or manual subscriptions.

## 84: What is effect() and should you use it for state updates?

`effect()` runs a function whenever the signals it reads change. It's for side effects that go outside Angular's state, like logging, writing to `localStorage` or calling a third-party chart API.

It should not be used to copy one signal into another. That creates extra change detection work and is hard to follow. Use `computed()` or `linkedSignal()` for derived values.

## 85: What is linkedSignal()?

`linkedSignal()` is a writable signal that resets itself when a source signal changes.

```ts
options = input.required<Option[]>();
selected = linkedSignal(() => this.options()[0]);
```

The user can change `selected`, but when `options` changes, it goes back to the first option. It replaces the pattern of using `effect()` to set one signal from another, which is slower and error-prone.

## 86: What does it mean that signals are "glitch-free"?

When several signals change, computed signals and templates never see a half-updated state. Angular updates dependencies in a way that a `computed()` is calculated once with the final values, not once per change.

For performance, this means updating several signals in a row doesn't cause several renders. Angular schedules one change detection pass after your code finishes.

## 87: What are signal inputs?

Signal inputs are created with `input()` instead of `@Input()`. The value is a signal.

```ts
export class Avatar {
  size = input(32);
  url = input.required<string>();
}
```

They work well with OnPush and zoneless apps: when the parent passes a new value, Angular knows exactly which component to update. You can also build `computed()` signals from them, which replaces most `ngOnChanges` code.

## 88: What is the @let block in templates?

`@let` declares a local variable in the template:

```html
@let user = user$ | async; @if (user) {
<h2>{{ user.name }}</h2>
<p>{{ user.email }}</p>
}
```

It helps performance a little by avoiding repeated expressions, for example subscribing to the same Observable twice with two `async` pipes. Mostly it makes templates easier to read.

## 89: Why should you avoid subscribing to the same Observable twice in a template?

Each `async` pipe creates its own subscription. For a cold Observable like an HTTP call, that means two requests:

```html
<!-- two requests -->
<p>{{ (user$ | async)?.name }}</p>
<p>{{ (user$ | async)?.email }}</p>
```

Fix it with `@let`, `@if (... ; as user)`, `toSignal()` or `shareReplay`.

## 90: What is the cost of global styles versus component styles?

Global styles in `styles.css` are part of the initial load for every page. Big global stylesheets (for example a full CSS framework) slow down the first render.

Component styles are bundled with the component, so styles of lazy loaded components load only when needed. Keep global CSS small (reset, variables, typography) and put the rest in components. Budgets for `anyComponentStyle` help keep component styles small too.

## 91: What is critical CSS inlining?

Critical CSS is the CSS needed to render the visible part of the page. With inlining, the build puts that CSS directly into `index.html` and loads the rest of the stylesheet without blocking rendering.

The Angular CLI does this by default in production (`optimization.styles.inlineCritical`). It improves First Contentful Paint because the browser doesn't have to wait for the full CSS file.

## 92: What is font inlining in Angular builds?

When you use Google Fonts with a `<link>` in `index.html`, the production build can download the font CSS and inline it into `index.html`. This saves one network round trip to the fonts server before text can render.

It's controlled by `optimization.fonts.inline` and is on by default in production.

## 93: What is font-display: swap?

`font-display: swap` tells the browser to show text in a fallback font right away and switch to the web font when it loads. Without it, text can be invisible for a while.

```css
@font-face {
  font-family: "Inter";
  src: url("/fonts/inter.woff2") format("woff2");
  font-display: swap;
}
```

For Google Fonts, add `&display=swap` to the URL. Also self-host and preload the main font when you can.

## 94: What is preconnect and when do you use it?

`preconnect` tells the browser to open a connection (DNS, TCP, TLS) to another origin early, before a request needs it.

```html
<link rel="preconnect" href="https://cdn.example.com" />
```

Use it for origins that the page will surely need soon, like an image CDN or API domain. `NgOptimizedImage` warns in dev mode if the LCP image is on an origin without a preconnect.

## 95: What is the difference between preload and prefetch?

- `preload`: download this resource now, it's needed for the current page (for example the hero image or main font).
- `prefetch`: download this resource at low priority, it may be needed for a future navigation.

```html
<link
  rel="preload"
  href="/fonts/inter.woff2"
  as="font"
  type="font/woff2"
  crossorigin
/>
```

Angular uses the same idea with route preloading and `@defer` prefetching.

## 96: What image formats are best for performance?

- **AVIF**: smallest files in most cases, good browser support today
- **WebP**: smaller than JPEG/PNG, supported everywhere
- **SVG**: for icons and logos
- **JPEG/PNG**: as a fallback or when nothing else fits

Also serve images at the right size. Sending a 3000 px wide photo to a 400 px slot wastes a lot of bandwidth. Image CDNs with `NgOptimizedImage` loaders handle both format and size for you.

## 97: What is an image loader in NgOptimizedImage?

A loader is a function that builds the image URL for a given width. With a loader, `NgOptimizedImage` can generate a `srcset` so the browser picks the right size.

Angular has built-in loaders for common CDNs:

```ts
import { provideImgixLoader } from "@angular/common";

providers: [provideImgixLoader("https://my-site.imgix.net/")];
```

There are also `provideCloudinaryLoader`, `provideImageKitLoader`, `provideCloudflareLoader` and `provideNetlifyLoader`. You can write your own with the `IMAGE_LOADER` token.

## 98: What does the fill attribute do in NgOptimizedImage?

`fill` makes the image fill its parent element instead of using fixed `width` and `height`. The parent must have `position: relative` (or `absolute`/`fixed`) and a size.

```html
<div class="cover">
  <img ngSrc="/cover.jpg" fill alt="" />
</div>
```

```css
.cover {
  position: relative;
  aspect-ratio: 16 / 9;
}
img {
  object-fit: cover;
}
```

It's useful for background-like images where you don't know the exact size.

## 99: What is the placeholder option in NgOptimizedImage?

`placeholder` shows a blurred low-resolution version of the image while the full one loads.

```html
<img ngSrc="/photo.jpg" width="800" height="600" placeholder />
```

With a loader configured, Angular requests a tiny version automatically. You can also pass a base64 data URL. It makes loading look smoother, but don't use it on the LCP image if it delays the real image.

## 100: What are the main tools to find performance problems in an Angular app?

- **Angular DevTools**: change detection profiling and component tree
- **Chrome DevTools Performance panel**: long tasks, scripting, rendering, layout
- **Chrome DevTools Memory panel**: heap snapshots for memory leaks
- **Network panel**: request sizes, timing, caching
- **Lighthouse**: lab audit with suggestions
- **Bundle analyzers**: what's inside your bundles (`ng build --stats-json`)
- **Real user monitoring**: the `web-vitals` library or a monitoring service to see real user data

## 101: What is the Chrome DevTools Performance panel used for?

It records what the browser does over time: JavaScript execution, style calculation, layout, painting and network activity. You use it to find:

- Long tasks (over 50 ms) that block the main thread
- Which functions take the most time (flame chart)
- Layout thrashing and forced reflows
- Slow interactions that hurt INP

For Angular apps, you can also see Angular-specific entries (change detection, component rendering) in a custom track when profiling is enabled.

## 102: What is a long task?

A long task is any piece of work on the main thread that takes more than 50 ms. While it runs, the browser can't respond to clicks or typing, so the page feels frozen.

In Angular apps, long tasks often come from big change detection runs, rendering a large list at once, heavy computations in event handlers or parsing a large JS bundle. Splitting work, deferring code and using web workers help.

## 103: What is the main thread and why does it matter?

The main thread is where the browser runs JavaScript, handles user input, calculates styles, does layout and paints. There is only one main thread per page.

Angular code (change detection, event handlers, rendering) runs there too. If your code keeps the main thread busy, everything else waits. Good performance means keeping main thread work short and moving heavy work elsewhere when possible.

## 104: What is a web worker?

A web worker runs JavaScript in a background thread, separate from the main thread. It can't touch the DOM, but it can do heavy calculations without freezing the UI.

The Angular CLI can create one:

```bash
ng generate web-worker app
```

Use it for things like parsing big files, image processing, complex filtering or encryption.

## 105: What is the difference between initial load and runtime performance?

- **Initial load**: everything until the app is visible and usable. Measured with LCP, FCP, TTFB. Improved by smaller bundles, SSR, caching, lazy loading and optimized images.
- **Runtime**: how the app behaves while the user uses it. Measured with INP, frame rate, memory. Improved by OnPush, signals, `track`, virtual scrolling and avoiding heavy work on the main thread.

Interviewers often want to see that you know these are different problems with different fixes.

## 106: What is Time to First Byte (TTFB)?

TTFB is the time from the request until the first byte of the response arrives. It includes DNS, connection setup and server processing.

For a static Angular app on a CDN, TTFB is usually low. With SSR it can go up because the server renders the page first. Caching rendered pages, prerendering static routes and keeping server-side API calls fast help.

## 107: What is First Contentful Paint (FCP)?

FCP is the time until the browser draws the first text or image. For a client-rendered Angular app, the page is blank until the JS loads and runs, so FCP depends a lot on bundle size.

SSR and prerendering improve FCP a lot because the HTML already contains content. Critical CSS inlining and font inlining help too.

## 108: What is Largest Contentful Paint (LCP) and how do you improve it in Angular?

LCP is the time until the biggest element in the viewport (often a hero image or heading) is rendered. Ways to improve it in Angular:

- Use SSR or prerendering so content is in the HTML
- Mark the LCP image with `priority` in `NgOptimizedImage`
- Keep the initial bundle small with lazy loading and `@defer`
- Use a CDN and good caching
- Avoid putting the LCP element inside a `@defer` block

## 109: What is Cumulative Layout Shift (CLS) and how do you avoid it in Angular?

CLS measures how much visible content jumps while the page loads. Common Angular causes and fixes:

- Images without sizes: use `NgOptimizedImage` with `width`/`height`
- Content that appears late and pushes things down: reserve space with a placeholder of the same size in `@defer` or loading states
- Web fonts swapping: use `font-display` and similar fallback fonts
- Hydration mismatches with SSR that re-render parts of the page

## 110: What is Interaction to Next Paint (INP)?

INP measures how long it takes from a user interaction (click, tap, key press) until the next frame is painted. A good value is under 200 ms.

In Angular, INP gets worse when an event handler or the change detection after it does a lot of work. OnPush, signals, smaller components, avoiding heavy template logic and splitting long tasks all help.

## 111: Why should you measure on a real device or with CPU throttling?

Developer laptops are much faster than the average user's phone. An interaction that takes 30 ms on your machine can take 300 ms on a mid-range Android phone.

In the Chrome DevTools Performance panel you can throttle the CPU (4x or 6x slowdown) and the network. Also look at real user data, because lab tests never show the full picture.

## 112: What is the difference between lab data and field data?

- **Lab data**: measured in a controlled setup, like Lighthouse or a DevTools recording. Easy to repeat and debug.
- **Field data**: measured from real users, like the Chrome UX Report (CrUX) or your own monitoring with the `web-vitals` library.

Lab data helps you find and fix problems. Field data tells you what users actually experience. INP in particular needs real interactions, so field data matters a lot.

## 113: What are source maps and should you ship them to production?

Source maps link minified code back to your original TypeScript, so stack traces and profiles are readable.

They don't slow down users, because browsers only download them when DevTools is open. The concern is that they expose your source code. A common setup is to generate them in production but upload them only to your error tracking tool (like Sentry) instead of serving them publicly.

## 114: What is the esbuild-based builder in Angular?

Since Angular 17, new projects use the `application` builder (now in the `@angular/build` package), which uses esbuild for production builds and Vite for the dev server. It replaced the old webpack-based builder.

It's much faster at building (often 2-4x or more), supports SSR and prerendering in the same build, and produces modern ES module output.

## 115: What is hot module replacement (HMR) in Angular?

HMR updates the running app in the browser when you change a file, without a full page reload. Since Angular 19, `ng serve` supports HMR for styles and templates by default, so editing a template keeps the app state.

It doesn't change production performance, but it makes development faster, which is why it may come up in interviews.

## 116: What is the purpose of the ngSkipHydration attribute?

`ngSkipHydration` tells Angular not to hydrate a component. Angular destroys the server-rendered DOM for it and renders it again on the client.

```html
<app-legacy-widget ngSkipHydration />
```

It's a workaround for components that change the DOM directly (for example through a third-party library) and break hydration. It costs performance, so use it only until you can fix the component.

## 117: What is TransferState?

`TransferState` passes data from the server render to the browser. Data that the server already fetched is written into the HTML, and the browser reads it instead of sending the same request again.

Angular uses it automatically for `HttpClient` requests through the HTTP transfer cache when hydration is enabled. You can use it directly with `makeStateKey()` for data fetched in other ways.

## 118: What is the HTTP transfer cache?

When you use SSR with `provideClientHydration()`, Angular caches `HttpClient` GET and HEAD responses made during server rendering and sends them in the page. During hydration, the browser uses those cached responses instead of calling the API again.

This avoids duplicate requests and keeps the page from flickering. It's on by default. You can configure it with `withHttpTransferCacheOptions()` or turn it off with `withNoHttpTransferCache()`.

## 119: What is event replay in hydration?

With SSR, the user can see the page and click a button before the JavaScript has loaded. Event replay records those events and replays them once the app is hydrated, so clicks are not lost.

```ts
provideClientHydration(withEventReplay());
```

Incremental hydration turns event replay on for you. It improves the user experience on slow connections.

## 120: What does isPlatformBrowser do?

`isPlatformBrowser(platformId)` tells you if the code is running in the browser or on the server. You use it to skip browser-only code during SSR, like accessing `window`, `localStorage` or measuring the DOM.

```ts
private platformId = inject(PLATFORM_ID);

ngOnInit() {
  if (isPlatformBrowser(this.platformId)) {
    // browser-only work
  }
}
```

For DOM work, `afterNextRender()` is often a cleaner choice because it never runs on the server.

## 121: What is afterNextRender()?

`afterNextRender()` runs a callback once, after Angular has finished rendering the next time. It runs only in the browser, never during SSR.

```ts
constructor() {
  afterNextRender(() => {
    this.chart = new Chart(this.canvas().nativeElement, config);
  });
}
```

It's the right place to set up third-party libraries that need the DOM, and it avoids errors on the server.

## 122: Why should you set up third-party libraries outside Angular's change detection?

Libraries like charts or maps often use their own timers, animation frames and event listeners. With Zone.js, every one of those triggers Angular change detection, even though Angular's state didn't change.

Running them with `NgZone.runOutsideAngular()` stops this. In zoneless apps this problem mostly goes away, because those events don't trigger change detection on their own.

## 123: What is NgZone.runOutsideAngular()?

It runs code outside the Angular zone, so async work inside it doesn't trigger change detection.

```ts
private zone = inject(NgZone);

constructor() {
  afterNextRender(() => {
    this.zone.runOutsideAngular(() => {
      window.addEventListener("scroll", this.onScroll, { passive: true });
    });
  });
}
```

When you need to update the UI from there, update a signal or use `zone.run()`. It's only relevant in apps that still use Zone.js.

## 124: What is event coalescing?

With Zone.js, a single click can trigger several event handlers (for example on a child and on a parent through bubbling), and each one starts change detection. Event coalescing groups them so change detection runs once.

```ts
provideZoneChangeDetection({ eventCoalescing: true });
```

New Zone.js-based projects have it on by default. Zoneless apps already batch change detection, so they don't need it.

## 125: Why are passive event listeners good for scrolling performance?

A passive listener promises it won't call `preventDefault()`. For `touchstart`, `touchmove` and `wheel`, this lets the browser start scrolling right away instead of waiting for your handler.

```ts
el.addEventListener("touchmove", handler, { passive: true });
```

Chrome treats some of these events as passive by default on the window and document, but for listeners on other elements you should set it yourself if you don't need `preventDefault()`.

## 126: Why is @HostListener on window scroll a problem?

`@HostListener("window:scroll")` (or a `host` binding for the same event) runs the handler on every scroll event, which can fire many times per second. With Zone.js, each one also triggers change detection for the whole app.

Better options are `IntersectionObserver` for "is this visible?" checks, CSS `position: sticky` for sticky headers, throttling the handler, or adding the listener outside Angular.

## 127: What is IntersectionObserver and why is it better than scroll events?

`IntersectionObserver` tells you when an element enters or leaves the viewport. The browser does the checking efficiently, without running your code on every scroll.

It's good for lazy loading, infinite scroll and "seen" tracking. Angular's `@defer (on viewport)` uses it internally.

## 128: What is the async keyword's interaction with Zone.js?

Zone.js can't patch native `async`/`await`, because it's part of the language. To make it work, the Angular CLI downlevels `async`/`await` into generator code when Zone.js is in the polyfills, which is a bit slower and bigger.

In zoneless apps this step is not needed, so native `async`/`await` is kept. That's one more small benefit of going zoneless.

## 129: Why should you keep components small?

Small components are easier to optimize:

- OnPush can skip more of the tree when only a small part changes
- A signal change updates only the small view that reads it
- They are easier to lazy load or defer
- Profiling shows exactly which part is slow

A huge page component with one big template has to re-check everything whenever anything in it changes.

## 130: What is the difference between a smart and a presentational component for performance?

A smart (container) component loads data and handles state. A presentational component just shows inputs and emits outputs.

Presentational components with OnPush and signal inputs are cheap: they only update when their inputs change. Keeping most of the UI presentational makes the app easier to optimize and easier to test.

## 131: How does immutability help with OnPush?

OnPush checks inputs by reference. If you change an object in place, the reference stays the same and the child component isn't updated.

```ts
// child won't update with OnPush
this.user.name = "Ann";

// child updates because the reference is new
this.user = { ...this.user, name: "Ann" };
```

With signals, use `update()` and return a new object or array so equality checks see the change.

## 132: What is the equal option of a signal?

Signals compare the old and new value with `Object.is` by default. If they are equal, nothing is notified. You can pass your own comparison:

```ts
filters = signal<Filters>(initial, {
  equal: (a, b) => a.query === b.query && a.page === b.page,
});
```

This can save work when the value is often set to an equivalent object. Don't make the comparison itself expensive.

## 133: What happens to a signal when you set the same value?

Nothing. If the new value is equal to the old one (`Object.is` by default), the signal doesn't notify its consumers, so no `computed()` recalculates and no view is marked for check.

That's why setting a primitive signal to the same number or string costs almost nothing. For objects and arrays, a new reference counts as a change even if the content is the same.

## 134: What is ChangeDetectorRef?

`ChangeDetectorRef` gives a component manual control over its change detection:

- `markForCheck()`: mark this view and its ancestors to be checked on the next run
- `detectChanges()`: check this view and its children right now
- `detach()` / `reattach()`: remove the view from or add it back to change detection

With signals, you rarely need it. It's still common in older OnPush code that uses RxJS subscriptions.

## 135: What is the difference between markForCheck() and detectChanges()?

- `markForCheck()` doesn't run anything immediately. It marks the view (and the path to the root) as dirty, so it's checked in the next scheduled change detection run.
- `detectChanges()` runs change detection for this component and its children right now, synchronously.

`markForCheck()` is usually the better choice because Angular can batch work. `detectChanges()` is for special cases, like a detached view or updating before measuring the DOM.

## 136: What is the Angular CLI command to analyze a production build?

There isn't a built-in visual analyzer, but the CLI can create the data for one:

```bash
ng build --stats-json
```

This writes a `stats.json` file (an esbuild metafile) to the output folder. You can upload it to the esbuild bundle analyzer at esbuild.github.io/analyze to see a treemap of what's in each chunk. Tools like `source-map-explorer` also work if source maps are on.

## 137: What is source-map-explorer?

`source-map-explorer` reads a JS file and its source map and shows a treemap of which source files and libraries take up the most space.

```bash
ng build --source-map
npx source-map-explorer dist/my-app/browser/*.js
```

It's a simple way to find large libraries or code that ended up in the wrong chunk.

## 138: What is the cost of importing a whole icon library?

Icon packs often have thousands of icons. If you import the whole set, all of them go into your bundle even if you use ten.

Better options:

- Import single icons (most libraries support per-icon imports)
- Use an SVG sprite with only the icons you need
- Use an icon font subset

Check with a bundle analyzer, icon sets are a very common hidden source of bundle size.

## 139: Why is moment.js often called out in Angular performance reviews?

`moment` is large (around 70 KB minified, more with locales), mutable and not tree-shakable. Many older Angular projects included it just to format a few dates.

Alternatives:

- Angular's `DatePipe` and `formatDate()`
- The native `Intl.DateTimeFormat` API
- Smaller tree-shakable libraries like `date-fns` or `dayjs`

## 140: What is the difference between lodash and lodash-es?

`lodash` is CommonJS, so importing from it often pulls in the whole library. `lodash-es` is the same library as ES modules, so the bundler can tree-shake it and keep only the functions you import.

```ts
import { debounce } from "lodash-es";
```

Many lodash functions also have native replacements now (`Array.prototype.flat`, `structuredClone`, optional chaining).

## 141: Why should you keep index.html small and fast?

`index.html` is the first file the browser loads, and nothing else starts until it arrives. Avoid:

- Big inline scripts
- Render-blocking third-party scripts in `<head>` (add `async` or `defer`, or load them later)
- Many stylesheet links

Also make sure `index.html` is served with a short cache time or `no-cache`, so new deploys are picked up.

## 142: What is the cost of third-party scripts like analytics or chat widgets?

They add JavaScript that runs on your main thread, often load more scripts, and can block rendering. With Zone.js, their timers and events can also trigger Angular change detection.

Ways to reduce the cost:

- Load them with `async` or after the app has loaded
- Load chat widgets only when the user clicks a button
- Use a lighter alternative
- Regularly check which ones are still needed

## 143: What does "do less work" mean for Angular performance?

Most performance fixes come down to doing less:

- Download less (smaller bundles, lazy loading, compression)
- Render less (pagination, virtual scroll, `@defer`)
- Check less (OnPush, signals, zoneless)
- Calculate less (`computed()`, pure pipes, memoization)
- Request less (caching, debouncing, `shareReplay`)

When you face a slow app, ask what work can be skipped before trying to make the work faster.

## 144: What is the purpose of the @empty block in @for?

`@empty` shows content when the list has no items:

```html
@for (order of orders(); track order.id) {
<app-order-row [order]="order" />
} @empty {
<p>No orders yet.</p>
}
```

It's not a big performance feature, but it replaces an extra `@if` check around the list and keeps the template simpler.

## 145: How is the built-in control flow faster than *ngIf and *ngFor?

The built-in `@if`, `@for` and `@switch` blocks are part of the template compiler, not directives. That means:

- No directive instances are created for them
- `@for` uses a faster diffing algorithm than `NgForOf`
- `track` is required, so lists are keyed correctly
- You don't need to import `CommonModule` or `NgIf`/`NgForOf`

Angular has reported up to 90% faster runtime in some list benchmarks. You can migrate with `ng generate @angular/core:control-flow`.

## 146: Can you lazy load a service?

Yes. Services with `providedIn: "root"` already end up in a lazy chunk if only lazy code uses them. Angular 22 also adds `injectAsync()`, which lets you load a service's code on demand:

```ts
export class Toolbar {
  private exporter = injectAsync(() =>
    import("./pdf-exporter").then((m) => m.PdfExporter),
  );

  async export() {
    (await this.exporter()).exportPage();
  }
}
```

The service must be auto-provided (`providedIn: "root"` or `@Service()`). This is useful for heavy services, like a PDF exporter, that are used rarely.

## 147: What is ng update and how is it related to performance?

`ng update` updates Angular and runs migrations. Staying on recent versions is one of the easiest ways to get performance improvements: faster builds, a better `@for`, signals, zoneless, incremental hydration and smaller runtime code all came through updates.

```bash
ng update @angular/core @angular/cli
```

Many updates also include migrations that move your code to faster APIs automatically.

## 148: What is the difference between Eager and OnPush defaults in Angular 22?

Before Angular 22, a component without a `changeDetection` setting used `Default`, which means it was checked on every change detection run. Since Angular 22, the default is `OnPush`.

`ChangeDetectionStrategy.Default` was renamed to `ChangeDetectionStrategy.Eager`. When you run `ng update` to v22, a migration adds `Eager` to existing components that don't set a strategy, so their behavior doesn't change. You can then move them to OnPush one by one.

## 149: What are the first steps when someone says "the Angular app is slow"?

1. Find out what "slow" means: initial load, a specific page, typing, scrolling?
2. Reproduce it on a production build, with CPU throttling.
3. Measure: Lighthouse for load, Performance panel and Angular DevTools for runtime.
4. Find the biggest cause (big bundle, long task, too many change detection runs, memory growth).
5. Fix that one thing and measure again.

Guessing and changing many things at once usually wastes time.

## 150: What is the cost of console.log in production code?

Calls to `console.log` are not free, especially when logging large objects, because the browser may keep references to them for the console. In a tight loop or a frequently called function, this can slow things down and keep objects in memory.

Remove debug logs before shipping, or use a logger that does nothing in production. Some teams use a lint rule (`no-console`) to catch them.

# Moderate Questions (151-300)

## 151: How does Angular decide which components to check in an OnPush tree?

When change detection runs, Angular walks the tree from the root. For each OnPush component it checks whether the view is marked dirty. If not, it skips that component and all its children.

A view gets marked dirty when an input reference changes, an event handler in it runs, the `async` pipe gets a value, or `markForCheck()` is called. Marking a view dirty also marks all its ancestors, so Angular can reach it from the root.

## 152: How do signals change the way OnPush components are refreshed?

When a signal read in a template changes, Angular marks only that view for refresh, not its ancestors. During change detection Angular walks down to the marked view and refreshes it, but it doesn't re-run the templates of the OnPush parents on the way.

This is more precise than `markForCheck()`, which marks the whole path up to the root as dirty, so all those parent templates are checked too. With signals, a change deep in the tree costs about the same as a change at the top.

## 153: What is a common bug when moving a component to OnPush?

The component mutates data instead of replacing it, or updates a plain field from an async callback:

```ts
ngOnInit() {
  this.api.load().subscribe((data) => {
    this.items = data; // OnPush view isn't marked dirty
  });
}
```

The data changes, but the view doesn't update until something else triggers a check. Fix it by storing the value in a signal, using the `async` pipe or `toSignal()`, or calling `markForCheck()`.

## 154: How do you convert an Observable-based component to work well with OnPush and zoneless?

Turn the streams into signals and read them in the template:

```ts
export class OrderList {
  private api = inject(OrderApi);
  orders = toSignal(this.api.orders$, { initialValue: [] });
  count = computed(() => this.orders().length);
}
```

```html
<h2>{{ count() }} orders</h2>
@for (o of orders(); track o.id) {
<app-order-row [order]="o" />
}
```

Signals notify Angular on their own, so you don't need manual subscriptions or `markForCheck()`.

## 155: What breaks when you remove Zone.js from an app?

Anything that relied on Zone.js to trigger change detection:

- Plain fields updated in `setTimeout`, promises or subscriptions without `markForCheck()`
- Code that waits for `NgZone.onStable` or `onMicrotaskEmpty`
- Tests using `fakeAsync` and `tick()` (need `zone.js/testing`)
- Libraries that assume Zone.js is present

Components that use signals, the `async` pipe or `markForCheck()` keep working. Moving everything to OnPush first is a good way to prepare.

## 156: How do you find components that will break in zoneless mode?

A good path:

1. Make all components OnPush (Angular 22 already defaults to it).
2. Turn on the exhaustive no-changes check in dev mode:

```ts
provideCheckNoChangesConfig({ exhaustive: true, interval: 1000 });
```

3. Run the app and tests. Angular throws `ExpressionChangedAfterItHasBeenChecked` for bindings that changed without notifying Angular.
4. Fix those places with signals or `markForCheck()`.

## 157: What does provideCheckNoChangesConfig do?

It configures the dev-mode check that verifies bindings didn't change after they were checked. With `exhaustive: true`, Angular checks all views, including OnPush views that weren't dirty. With `interval`, it also runs the check periodically.

It helps find state that changes without telling Angular, which is exactly what breaks in zoneless and OnPush apps. It has no effect in production builds.

## 158: How does zoneless change detection get scheduled?

Angular has an internal scheduler. When something notifies it (a signal used in a template changes, `markForCheck()` is called, an input is set, a template event fires), it schedules one change detection run. It uses a race between `setTimeout` and `requestAnimationFrame`, so the run happens before the next frame but after your current code finishes.

Several notifications in the same task lead to a single run, so updating five signals in a row renders once.

## 159: How do you migrate a large app from Eager to OnPush step by step?

1. Start with leaf components (buttons, cards, list rows). They usually just show inputs.
2. Make inputs immutable and convert them to `input()`.
3. Replace mutable state in components with signals.
4. Move up the tree: list components, then page components.
5. Use the Angular DevTools profiler before and after to see the difference.

In Angular 22, after `ng update`, components without a strategy get `Eager` added. Removing that line from a component makes it OnPush.

## 160: Why does mutating an array inside a signal not update the view?

```ts
items = signal<string[]>([]);

add(item: string) {
  this.items().push(item); // same array reference
}
```

The signal still holds the same array, so it never notifies anyone. Use `update()` and return a new array:

```ts
add(item: string) {
  this.items.update((list) => [...list, item]);
}
```

## 161: How expensive is a computed() signal?

Very cheap to read, because the value is cached. It only recalculates when a dependency changed and someone reads it. If nobody reads it, it doesn't recalculate at all (it's lazy).

The cost is in the function itself. A `computed()` that filters 50,000 items runs that filter every time any dependency changes. If the list is big, combine it with debouncing the filter input, or move the work to a web worker or the server.

## 162: What is untracked() and when is it useful?

`untracked()` reads a signal without making it a dependency of the current `computed()` or `effect()`.

```ts
effect(() => {
  const user = this.user();
  // log when user changes, but don't re-run when settings change
  this.logger.log(user, untracked(this.settings));
});
```

It avoids extra re-runs when you need a value but don't want to react to its changes.

## 163: How do you debounce a signal in Angular 22?

Angular 22 adds an experimental `debounced()` function. It returns a `Resource` whose value follows the source signal after a delay:

```ts
import { debounced } from "@angular/core";

query = signal("");
debouncedQuery = debounced(this.query, 300);

results = httpResource<Product[]>(
  () => `/api/products?q=${this.debouncedQuery.value()}`,
);
```

While the value is waiting, the resource status shows it's pending. Before v22, people converted the signal to an Observable with `toObservable()` and used `debounceTime`.

## 164: How do you combine signals and RxJS for a debounced search?

Use `toObservable()` to get a stream from the signal, apply RxJS operators, then convert back with `toSignal()`:

```ts
query = signal("");

results = toSignal(
  toObservable(this.query).pipe(
    debounceTime(300),
    distinctUntilChanged(),
    switchMap((q) => this.api.search(q)),
  ),
  { initialValue: [] },
);
```

This is still the most flexible option when you need operators like `retry` or `catchError`.

## 165: What is the cost of effect() in terms of change detection?

Effects run as part of Angular's change detection process. Component effects run before the component's view is refreshed, root effects run before the app is checked. Writing to signals inside an effect can mark views dirty again, which means more work in the same cycle.

So effects that set state make rendering more expensive and harder to follow. Keep effects for real side effects, and use `computed()` or `linkedSignal()` for derived state.

## 166: What is afterRenderEffect() and when do you use it?

`afterRenderEffect()` is like `effect()`, but it runs after Angular has rendered, and only in the browser. It also has phases (`earlyRead`, `write`, `mixedReadWrite`, `read`) so you can group DOM reads and writes and avoid layout thrashing.

```ts
afterRenderEffect({
  earlyRead: () => this.panel().nativeElement.offsetHeight,
  write: (height) => {
    this.chart.resize(this.width(), height());
  },
});
```

The value returned by one phase is passed to the next phase as a signal.

Use it for DOM work that depends on signals, like syncing a chart size or reading element sizes.

## 167: What is layout thrashing and how can it happen in Angular?

Layout thrashing is when code reads layout values (`offsetHeight`, `getBoundingClientRect()`) and writes styles in a loop. Each read after a write forces the browser to recalculate layout right away.

In Angular, it often happens in directives that measure and resize elements in `ngAfterViewChecked` or in lifecycle hooks on many items. Batch reads first, then writes, use `afterRenderEffect` phases, or use CSS solutions like flexbox, grid and `ResizeObserver`.

## 168: How do you optimize a large table in Angular?

- Paginate on the server, or use virtual scrolling for client data
- Use `@for` with a proper `track` key
- Make row components OnPush with signal inputs
- Avoid method calls and impure pipes in cells
- Precompute formatted values once when data arrives
- Sort and filter in `computed()` or on the server
- Keep cell templates small, defer heavy cell content (charts, menus) until needed

If the table still needs thousands of visible cells, consider a specialized grid library built for it.

## 169: How do you configure CDK virtual scroll for better performance?

```html
<cdk-virtual-scroll-viewport
  itemSize="56"
  minBufferPx="400"
  maxBufferPx="800"
  class="viewport"
>
  <app-row *cdkVirtualFor="let row of rows; trackBy: trackById" [row]="row" />
</cdk-virtual-scroll-viewport>
```

- `itemSize` must match the real row height
- `minBufferPx` / `maxBufferPx` control how much content is rendered outside the viewport
- `templateCacheSize` on `*cdkVirtualFor` sets how many views are kept for reuse

The viewport needs a fixed height in CSS.

## 170: What are the limits of CDK virtual scroll?

- It works best with a fixed item size. Variable heights need an experimental autosize strategy from `@angular/cdk-experimental`, or your own `VirtualScrollStrategy`.
- `Ctrl+F` browser search doesn't find items that aren't rendered
- Accessibility can suffer because screen readers see only some items
- It doesn't use `@for`; you use `*cdkVirtualFor`

For huge tables with variable rows, a dedicated grid library may fit better.

## 171: How do you write a custom preloading strategy?

Implement `PreloadingStrategy` and decide per route:

```ts
@Injectable({ providedIn: "root" })
export class FlagPreloading implements PreloadingStrategy {
  preload(route: Route, load: () => Observable<unknown>): Observable<unknown> {
    return route.data?.["preload"] ? load() : of(null);
  }
}
```

```ts
provideRouter(routes, withPreloading(FlagPreloading));

// in routes
{ path: "orders", loadComponent: () => import("./orders"), data: { preload: true } }
```

You can also add a delay, skip preloading on slow connections, or preload based on user role.

## 172: How do you skip preloading on slow networks?

Use the Network Information API (supported in Chromium-based browsers) inside a custom strategy:

```ts
preload(route: Route, load: () => Observable<unknown>) {
  const conn = (navigator as any).connection;
  if (conn?.saveData || /2g/.test(conn?.effectiveType ?? "")) {
    return of(null);
  }
  return load();
}
```

Users on mobile data or with "save data" turned on don't download chunks they may never use.

## 173: What is quicklink-style preloading?

It preloads only the routes linked from what's currently visible. When a `routerLink` enters the viewport, the route behind it gets downloaded. The `ngx-quicklink` library implements this as a preloading strategy.

It's a middle ground between preloading nothing and preloading everything. On big apps with many routes, `PreloadAllModules` can download a lot of code that's never used.

## 174: How do you decide what to put in a @defer block?

Good candidates:

- Below-the-fold content (comments, recommendations, footers with widgets)
- Heavy components (charts, maps, rich text editors, video players)
- Content shown after interaction (dialogs, tabs, menus)
- Features only some users use

Bad candidates:

- The LCP element or anything above the fold
- Tiny components where the extra request costs more than it saves
- Components that are imported eagerly elsewhere in the same file anyway

## 175: What does the minimum and after parameter do in @loading and @placeholder?

They prevent flicker:

```html
@defer (on viewport) {
<app-chart />
} @placeholder (minimum 500ms) {
<div class="skeleton"></div>
} @loading (after 100ms; minimum 1s) {
<app-spinner />
}
```

- `@placeholder (minimum 500ms)`: show the placeholder at least 500 ms
- `@loading (after 100ms)`: only show the loader if loading takes more than 100 ms
- `@loading (minimum 1s)`: once shown, keep it at least 1 s

Without these, a fast load can cause a quick flash of spinner content.

## 176: How do you avoid layout shift with @defer?

Give the `@placeholder` the same size as the final content:

```html
@defer (on viewport) {
<app-reviews />
} @placeholder {
<div style="min-height: 420px"></div>
}
```

If the placeholder is empty and the deferred content is 400 px tall, everything below jumps when it loads, which hurts CLS. A skeleton with the right size is best.

## 177: How do you use on viewport and on interaction with a specific element?

You can point the trigger at a template reference outside the block:

```html
<button #loadBtn>Show details</button>

@defer (on interaction(loadBtn); prefetch on hover(loadBtn)) {
<app-details />
}
```

This is useful when the placeholder isn't the thing the user interacts with. When a trigger has no reference, Angular uses the placeholder, which must have a single root element.

## 178: How do you test what goes into a @defer chunk?

Build the app and look at the output. Each defer block creates a lazy chunk, which you can see in the build table and in `stats.json`.

If the chunk is missing or tiny, the deferred component is probably also imported eagerly somewhere else in the same component (for example used outside the `@defer` block or referenced in TypeScript). The Angular compiler only defers dependencies used exclusively inside `@defer` blocks.

## 179: How do @defer blocks behave during SSR?

On the server, `@defer` blocks render their `@placeholder` (or nothing if there isn't one). The main content is not rendered on the server, and triggers don't fire there.

With incremental hydration (`hydrate` triggers), the server does render the main content as HTML, and the browser hydrates it later when the hydrate trigger fires. That's the main difference between plain `@defer` and `@defer` with hydrate triggers.

## 180: What hydrate triggers are available for incremental hydration?

- `hydrate on idle`
- `hydrate on viewport`
- `hydrate on interaction`
- `hydrate on hover`
- `hydrate on immediate`
- `hydrate on timer(…)`
- `hydrate when condition`
- `hydrate never`

```html
@defer (on viewport; hydrate on interaction) {
<app-product-gallery />
}
```

The regular trigger is used when the block is rendered on the client (for example after navigation). The hydrate trigger is used for blocks that came rendered from the server.

## 181: What does hydrate never do?

It keeps the server-rendered HTML as static content. Angular never loads the JavaScript for that block and never hydrates it.

```html
@defer (hydrate never) {
<app-legal-footer />
}
```

It's good for content that never needs interaction, like a static footer or article text. Note that the block won't react to signal changes either, it stays as the server left it.

## 182: How do you turn off incremental hydration in Angular 22?

Since v22 `provideClientHydration()` enables incremental hydration by default. If you need the old behavior:

```ts
provideClientHydration(withNoIncrementalHydration());
```

In v19 to v21, it was opt-in with `withIncrementalHydration()`. The v22 update includes a migration for existing configs.

## 183: What causes hydration mismatches and why do they hurt performance?

A mismatch happens when the DOM in the browser doesn't match what Angular expects from the server render. Common causes:

- Code that changes the DOM directly (`innerHTML`, jQuery, some libraries)
- Invalid HTML that the browser fixes (like a `<div>` inside a `<p>`)
- Different content on server and client (dates, random values, `window` checks in templates)
- CDNs or proxies that change or strip HTML comments

When it happens, Angular may throw away the server DOM and render again, which loses the benefit of SSR and can cause layout shifts. Angular shows errors like NG0500 in the console.

## 184: How do you verify that hydration is working?

- In dev mode, the console logs a message with hydration stats (number of components hydrated and skipped).
- Angular DevTools can show hydration status for components.
- Errors like NG0500-NG0507 point to mismatches.
- In the Performance panel, there should be no big re-render after the HTML appears.

Also check that the network panel doesn't show the same API calls again after load, which means the transfer cache is working.

## 185: How do you configure render modes per route?

In `app.routes.server.ts`:

```ts
import { RenderMode, ServerRoute } from "@angular/ssr";

export const serverRoutes: ServerRoute[] = [
  { path: "", renderMode: RenderMode.Prerender },
  {
    path: "blog/:slug",
    renderMode: RenderMode.Prerender,
    getPrerenderParams: async () => [{ slug: "hello" }],
  },
  { path: "account/**", renderMode: RenderMode.Client },
  { path: "**", renderMode: RenderMode.Server },
];
```

Then register them with `provideServerRendering(withRoutes(serverRoutes))`. Static pages get prerendered, dynamic ones are rendered per request, and private pages skip SSR.

## 186: Why would you choose RenderMode.Client for some routes?

- The page is behind login, so SEO doesn't matter and the content is user specific
- The page relies on browser-only APIs heavily
- Server rendering would add load on your servers with little benefit

Client-rendered routes are served as a plain shell, so they skip server CPU time. The trade-off is slower first content on those pages.

## 187: How do you prerender routes with parameters?

Use `getPrerenderParams` to return the list of param values at build time:

```ts
{
  path: "product/:id",
  renderMode: RenderMode.Prerender,
  async getPrerenderParams() {
    const ids = await inject(ProductApi).getAllIds();
    return ids.map((id) => ({ id }));
  },
}
```

You can call `inject()` inside it. Use `fallback` (for example `PrerenderFallback.Server`) to decide what happens with ids that weren't prerendered.

## 188: How do you configure the HTTP transfer cache?

```ts
provideClientHydration(
  withHttpTransferCacheOptions({
    includePostRequests: true,
    includeHeaders: ["ETag"],
    filter: (req) => !req.url.includes("/api/me"),
  }),
);
```

By default only GET and HEAD requests are cached and requests with `Authorization` or `Proxy-Authorization` headers are skipped. Exclude user-specific data so it isn't embedded in pages that might get cached by a CDN. You can also opt out per request with `transferCache: false` in the request options.

## 189: How do you cache server-rendered pages?

Rendering on every request costs CPU. Options:

- Prerender pages that don't change per user
- Put a CDN in front with `Cache-Control` and `stale-while-revalidate` for public pages
- Add an in-memory or Redis cache in your Node server keyed by URL
- Use shorter cache times for pages that change often

Never cache pages with user-specific content under a shared key.

## 190: How do you avoid duplicate HTTP calls between server and client without HttpClient?

If you use `fetch` directly or a third-party SDK, the transfer cache doesn't see those calls. Use `TransferState` yourself:

```ts
const KEY = makeStateKey<Config>("config");

export class ConfigService {
  private state = inject(TransferState);

  async load(): Promise<Config> {
    const cached = this.state.get(KEY, null);
    if (cached) return cached;
    const config = await fetch("/api/config").then((r) => r.json());
    this.state.set(KEY, config);
    return config;
  }
}
```

Angular 22 also adds a `transferCacheKey` option for `resource()` and `rxResource()`.

## 191: What is PendingTasks and why does it matter for SSR?

The server waits until the app is "stable" before sending HTML. Without Zone.js, Angular doesn't know about your custom async work unless you tell it. `PendingTasks` lets you register work the server should wait for:

```ts
private tasks = inject(PendingTasks);

load() {
  return this.tasks.run(() => this.fetchData());
}
```

`HttpClient`, the router and resources already do this. If you forget it for custom async work, the page can be sent before the data is there.

## 192: What is pendingUntilEvent()?

It's an RxJS operator from `@angular/core/rxjs-interop` that keeps the app "unstable" until the Observable emits, completes or errors.

```ts
this.data$ = this.socket.firstMessage$.pipe(pendingUntilEvent());
```

It's useful in SSR when a non-HTTP Observable delivers data that should be in the rendered HTML.

## 193: How do you set up the Angular service worker for caching app files?

`ngsw-config.json` has `assetGroups`:

```json
{
  "assetGroups": [
    {
      "name": "app",
      "installMode": "prefetch",
      "resources": {
        "files": ["/favicon.ico", "/index.html", "/*.css", "/*.js"]
      }
    },
    {
      "name": "assets",
      "installMode": "lazy",
      "updateMode": "prefetch",
      "resources": {
        "files": ["/assets/**", "/*.(svg|jpg|png|webp|avif|woff2)"]
      }
    }
  ]
}
```

`prefetch` downloads files when the worker installs, `lazy` caches them when they are first requested.

## 194: How do you cache API responses with the Angular service worker?

Use `dataGroups`:

```json
"dataGroups": [
  {
    "name": "catalog",
    "urls": ["/api/products/**"],
    "cacheConfig": {
      "strategy": "performance",
      "maxSize": 100,
      "maxAge": "1h"
    }
  },
  {
    "name": "orders",
    "urls": ["/api/orders/**"],
    "cacheConfig": {
      "strategy": "freshness",
      "maxSize": 20,
      "maxAge": "10m",
      "timeout": "3s"
    }
  }
]
```

`performance` serves from cache first. `freshness` tries the network first and falls back to cache after the timeout.

## 195: How do you register the service worker without hurting startup?

```ts
provideServiceWorker("ngsw-worker.js", {
  enabled: !isDevMode(),
  registrationStrategy: "registerWhenStable:30000",
});
```

`registerWhenStable:30000` waits until the app is stable (or 30 seconds) before registering. The worker installs and prefetches files without competing with the first page load. You can also use `registerAfterDelay` or `registerImmediately`.

## 196: How do you handle service worker updates without stale code problems?

Use `SwUpdate`:

```ts
private updates = inject(SwUpdate);

constructor() {
  this.updates.versionUpdates
    .pipe(filter((e) => e.type === "VERSION_READY"), takeUntilDestroyed())
    .subscribe(() => this.showReloadBanner.set(true));
}
```

When the user clicks reload, call `document.location.reload()`. Users get the new version without being stuck on old cached code, and you don't reload in the middle of their work.

## 197: How do you write a caching HTTP interceptor?

```ts
const cache = new Map<string, HttpResponse<unknown>>();

export const cacheInterceptor: HttpInterceptorFn = (req, next) => {
  if (req.method !== "GET" || !req.url.startsWith("/api/ref/")) {
    return next(req);
  }
  const hit = cache.get(req.urlWithParams);
  if (hit) return of(hit.clone());

  return next(req).pipe(
    tap((event) => {
      if (event instanceof HttpResponse) cache.set(req.urlWithParams, event);
    }),
  );
};
```

```ts
provideHttpClient(withInterceptors([cacheInterceptor]));
```

Only cache data that rarely changes, and think about how to clear the cache (logout, time-based expiry).

## 198: What changed in HttpClient in Angular 22 related to performance?

`HttpClient` now uses the `FetchBackend` by default instead of `XMLHttpRequest`. `withFetch()` is deprecated because it's no longer needed.

Fetch works better in SSR and service worker setups and is the standard API going forward. The main trade-off is that fetch doesn't report upload progress, so if you need it, use `provideHttpClient(withXhr())`.

## 199: How do you cancel HTTP requests that are no longer needed?

- Unsubscribe from the Observable (the request is aborted)
- Use `switchMap` so a new request cancels the previous one
- `httpResource` and `resource()` abort the old request when params change
- `takeUntilDestroyed()` cancels when the component is destroyed

```ts
results = httpResource(() => `/api/search?q=${this.query()}`);
```

Cancelling saves bandwidth and server work, and avoids processing responses that nobody needs.

## 200: How do you avoid sending the same request from several components at once?

Share it in a service:

```ts
@Injectable({ providedIn: "root" })
export class CurrentUser {
  private http = inject(HttpClient);
  readonly user = httpResource<User>(() => "/api/me");
}
```

Every component that injects `CurrentUser` reads the same `user` resource, so only one request is made. With Observables, use `shareReplay({ bufferSize: 1, refCount: true })`.

## 201: What is the difference between shareReplay with refCount true and false?

- `refCount: true`: when all subscribers unsubscribe, the source is unsubscribed too. The next subscriber starts a new request.
- `refCount: false`: the source stays subscribed and the cached value stays forever, even with no subscribers.

```ts
shareReplay({ bufferSize: 1, refCount: true });
```

For HTTP calls that complete, `false` keeps the result cached for the app's lifetime, which is often what you want for reference data. For long-lived streams (websockets, intervals), `false` can leak, so use `true`.

## 202: How do you make a list update fast when one item changes?

- Keep items immutable and replace only the changed item:

```ts
this.items.update((list) =>
  list.map((i) => (i.id === updated.id ? updated : i)),
);
```

- Track by id in `@for`, so Angular keeps all other DOM nodes
- Make row components OnPush with signal inputs, so only the row whose input changed re-renders

Angular then updates one row instead of the whole list.

## 203: How does Angular's @for diffing work at a high level?

On every update, `@for` compares the new collection with the previous one using the `track` keys. It figures out which items were added, removed or moved, then:

- Reuses the existing view for items with the same key (and updates its context)
- Creates views only for new keys
- Destroys views for removed keys
- Moves DOM nodes for reordered items

That's why a stable key is so important. With a bad key, every item looks new and every view is recreated.

## 204: How do you handle a list where items can have duplicate ids?

`@for` warns in dev mode when `track` produces duplicate keys, because it can't map views correctly and may re-create them.

Fix the data if you can. If duplicates are expected (for example the same product twice in a cart), track by a combined key or by `$index` if the list doesn't reorder:

```html
@for (line of cart(); track line.productId + "-" + $index) { ... }
```

## 205: How do you measure how long a specific component takes to render?

- **Angular DevTools Profiler**: shows time spent per component in each change detection cycle
- **Chrome Performance panel** with Angular profiling enabled: Angular adds its own track with component entries
- **`performance.mark()` and `performance.measure()`** around code you suspect

Look for components that take a lot of time in many cycles, not only in one.

## 206: How do you enable Angular's integration with the Chrome DevTools Performance panel?

Since Angular 20, Angular can add its own data to the Performance panel. In a dev build, run this in the console (or call `enableProfiling()` from `@angular/core` in your code):

```js
ng.enableProfiling();
```

Then record in the Performance panel. You get an Angular track showing change detection, component templates, lifecycle hooks and which signal or event triggered each run, right next to the browser's own data.

## 207: How do you find out why change detection runs so often?

1. Record with the Angular DevTools Profiler and look at the trigger of each cycle.
2. With Zone.js, look for timers (`setInterval`), polling, scroll listeners, `mousemove` handlers and third-party libraries.
3. In the Chrome Performance panel (with Angular profiling), see what started each run.

Then fix the source: move noisy code outside Angular, throttle it, or switch to signals and zoneless so those events stop triggering checks at all.

## 208: What does a typical Angular DevTools flame graph show?

It shows one change detection cycle as a tree of components. Each bar is a component, its width is the time spent checking it and its children. Colors show how expensive it was.

Wide bars deep in the tree point to components with heavy templates. Many bars for components that didn't change point to missing OnPush or bad data flow.

## 209: How do you find memory leaks in an Angular app?

1. Open the Chrome DevTools **Memory** panel.
2. Take a heap snapshot.
3. Do the action several times (open and close a page or dialog).
4. Force garbage collection and take another snapshot.
5. Compare them and search for your component class names.

If instances of a destroyed component keep growing, look at what retains them in the "Retainers" section. Usually it's a subscription, a listener, a timer or a service holding a reference.

## 210: What are detached DOM nodes and why do they matter?

A detached node is removed from the page but still referenced from JavaScript, so it can't be garbage collected. In Angular apps, this happens when a destroyed component's element is still referenced by:

- A third-party library that wasn't cleaned up
- A global event listener with a closure over the element
- A cache in a service

In a heap snapshot, filter by "Detached" to find them, then look at the retainers.

## 211: How do you clean up third-party libraries in a component?

Destroy them when the component is destroyed. Inject `DestroyRef` as a field, because `inject()` can't be called inside the `afterNextRender` callback:

```ts
export class MapView {
  private el = viewChild.required<ElementRef<HTMLElement>>("map");
  private destroyRef = inject(DestroyRef);

  constructor() {
    afterNextRender(() => {
      const map = new SomeMap(this.el().nativeElement);
      this.destroyRef.onDestroy(() => map.destroy());
    });
  }
}
```

Most chart, map and editor libraries have a `destroy()` or `dispose()` method that removes listeners and timers.

## 212: Why do services in root scope often cause memory leaks?

Root services live as long as the app. If a component registers something in a root service (a callback, a subscription, a reference to itself) and doesn't remove it on destroy, the service keeps the destroyed component in memory.

```ts
// leak: callback keeps the component alive
this.bus.register((msg) => this.handle(msg));
```

Always remove registrations in `onDestroy`, or use Observables with `takeUntilDestroyed()` so cleanup happens automatically.

## 213: How do you profile memory over time in Chrome?

Use the **Allocation instrumentation on timeline** option in the Memory panel, or record with the Performance panel and the "Memory" checkbox on. You see the JS heap size over time.

A healthy app goes up and down as the garbage collector runs. A sawtooth that keeps climbing after each navigation points to a leak. Then use heap snapshots to find which objects are retained.

## 214: How do you optimize forms with many fields?

- Use OnPush and signal-based or reactive forms instead of large template-driven forms
- Use `updateOn: "blur"` where you don't need validation on every keystroke
- Avoid expensive validators that run on every change, or debounce async validators
- Split very large forms into steps or sections, and `@defer` sections that aren't visible
- Avoid subscribing to `valueChanges` of the whole form for small updates

With Signal Forms (stable in Angular 22), fields are created lazily and validators only re-run when the data they read changes.

## 215: What does updateOn: 'blur' do in reactive forms?

It changes when a control updates its value and runs validation. The default is `"change"`, which updates on every keystroke.

```ts
email = new FormControl("", {
  validators: [Validators.email],
  updateOn: "blur",
});
```

With `"blur"`, validation and `valueChanges` happen only when the field loses focus. For big forms or expensive validators, this cuts a lot of work. `"submit"` is also available.

## 216: How do you debounce async validators?

Async validators run on every value change by default. For reactive forms, add a delay inside the validator:

```ts
export const usernameTaken =
  (api: UserApi): AsyncValidatorFn =>
  (control) =>
    timer(400).pipe(
      switchMap(() => api.exists(control.value)),
      map((taken) => (taken ? { taken: true } : null)),
    );
```

Because Angular unsubscribes from the old validator when the value changes, the timer is cancelled and only the last value hits the API. In Signal Forms, `validateAsync` and `validateHttp` support a `debounce` option since v22.

## 217: How do you use pure pipes for formatting instead of methods?

```ts
@Pipe({ name: "price" })
export class PricePipe implements PipeTransform {
  private format = new Intl.NumberFormat("en-US", {
    style: "currency",
    currency: "USD",
  });

  transform(value: number): string {
    return this.format.format(value);
  }
}
```

```html
@for (item of items(); track item.id) {
<td>{{ item.price | price }}</td>
}
```

The pipe instance is created once per usage and reuses the `Intl.NumberFormat`. It only runs again when `item.price` changes. A method in the template would run for every row on every check.

## 218: How do you memoize a function in a component without signals?

You can cache results by input:

```ts
private cache = new Map<string, string>();

label(code: string): string {
  let value = this.cache.get(code);
  if (value === undefined) {
    value = expensiveLookup(code);
    this.cache.set(code, value);
  }
  return value;
}
```

But in modern Angular, a `computed()` signal or a pure pipe is simpler and has no cache growth problems. Use manual memoization mainly in services or utilities.

## 219: What is the cost of ngClass and ngStyle compared to class and style bindings?

`ngClass` and `ngStyle` are directives. They have to diff the objects you pass on every check. Native bindings are handled by the compiler directly:

```html
<div [class.active]="isActive()" [style.width.px]="width()"></div>
<div [class]="{ active: isActive(), disabled: isDisabled() }"></div>
```

The native `[class]` and `[style]` bindings support objects too, so you rarely need `NgClass` or `NgStyle` in new code. The difference is small per element, but it adds up in big lists.

## 220: How do you speed up an app that has many event listeners in a list?

Use event delegation: one listener on the parent instead of one per row.

```html
<ul (click)="onListClick($event)">
  @for (item of items(); track item.id) {
  <li [attr.data-id]="item.id">{{ item.name }}</li>
  }
</ul>
```

```ts
onListClick(event: MouseEvent) {
  const id = (event.target as HTMLElement).closest("li")?.dataset["id"];
  if (id) this.select(id);
}
```

For most lists, per-row `(click)` is fine. Delegation helps when you have thousands of rows with several listeners each.

## 221: What are the costs of using content projection (ng-content) heavily?

Projected content belongs to the parent component, not the component that projects it. It's always created, even if the child hides it with `@if`. That means:

- Projected components are instantiated even when not shown
- Their change detection follows the parent

If you need to show content conditionally or lazily, pass an `ng-template` and render it with `ngTemplateOutlet` only when needed.

## 222: How do you render content lazily with ng-template?

```html
<!-- parent -->
<app-tabs>
  <ng-template #details>
    <app-heavy-details />
  </ng-template>
</app-tabs>
```

```ts
// tabs component
export class Tabs {
  details = contentChild<TemplateRef<unknown>>("details");
  open = signal(false);
}
```

```html
@if (open()) {
<ng-container [ngTemplateOutlet]="details()" />
}
```

`app-heavy-details` is only created when the template is rendered, unlike plain `<ng-content>`.

## 223: How do you avoid running code twice on server and browser with SSR?

Code in constructors and `ngOnInit` runs on both. To avoid repeating work:

- Let `HttpClient` use the transfer cache, so API calls aren't repeated
- Put browser-only code in `afterNextRender()` or `afterEveryRender()`
- Use `TransferState` for data loaded in other ways
- Don't start timers or polling on the server, they can keep the render from finishing

## 224: Why can a setInterval break or slow down SSR?

The server waits for the app to become stable before it sends the HTML. With Zone.js, a running `setInterval` keeps the zone busy forever, so the render can hang or wait until a timeout. It also wastes server CPU.

Start intervals only in the browser:

```ts
constructor() {
  afterNextRender(() => {
    const id = setInterval(() => this.tick(), 1000);
    this.destroyRef.onDestroy(() => clearInterval(id));
  });
}
```

## 225: How do you lazy load a heavy library only when needed?

Use a dynamic `import()`:

```ts
async exportExcel(rows: Row[]) {
  const XLSX = await import("xlsx");
  const sheet = XLSX.utils.json_to_sheet(rows);
  // ...
}
```

The library goes into its own chunk and is only downloaded when the user clicks export. This works for PDF generators, chart libraries, markdown parsers and similar big dependencies.

## 226: How do you lazy load a component without the router?

Use `@defer` in the template, which is the simplest. For full control, load it in code and create it with `ViewContainerRef`:

```ts
private vcr = inject(ViewContainerRef);

async openEditor() {
  const { Editor } = await import("./editor");
  this.vcr.createComponent(Editor);
}
```

Or use `NgComponentOutlet` with a signal holding the loaded component type.

## 227: How does route-level code splitting interact with shared code?

When two lazy routes use the same component or library, the bundler puts it into a shared chunk that both load. If code is used by the initial route, it stays in the initial bundle.

Problems show up when something big is imported from a file that's used everywhere, like a barrel file or a shared util that imports a heavy library. Then the heavy library ends up in the initial bundle. A bundle analyzer helps you spot these.

## 228: Do barrel files (index.ts) hurt bundle size?

Usually not much with esbuild, because it tree-shakes well as long as the modules have no side effects. But barrels can still cause problems:

- A module with side effects (top-level code) gets included when anything from the barrel is imported
- Builds, tests and editor tooling get slower in big projects
- It's easy to create circular imports

Many teams import directly from the file in large apps and use barrels only for library public APIs.

## 229: What are side effects in modules and how do they affect tree shaking?

A module has side effects if importing it does something, like changing a global, registering a polyfill or running code at the top level. The bundler can't drop such modules even when nothing from them is used.

Libraries mark themselves as side-effect free with `"sideEffects": false` in `package.json`. In your own code, avoid top-level code in files that only export functions and classes.

## 230: What does the allowedCommonJsDependencies option do?

It lists CommonJS packages that you accept, so the build stops warning about them:

```json
"options": {
  "allowedCommonJsDependencies": ["some-legacy-lib"]
}
```

It doesn't make the package smaller or tree-shakable. It just hides the warning. Use it only after checking there's no ES module alternative.

## 231: How do you set up budgets for lazy chunks too?

Use `anyComponentStyle`, `any`, `anyScript`, `bundle` and `initial` budget types:

```json
"budgets": [
  { "type": "initial", "maximumWarning": "400kB", "maximumError": "600kB" },
  { "type": "anyScript", "maximumWarning": "150kB", "maximumError": "250kB" },
  { "type": "bundle", "name": "admin", "maximumWarning": "200kB" }
]
```

`anyScript` applies to every JS file, including lazy chunks. `bundle` targets a named bundle. Run budgets in CI so a regression fails the build.

## 232: What is the "initial total" in the build output?

The build table lists initial chunks and then a total. Initial total is the size of everything the browser must download to start the app (main, polyfills, styles and shared chunks imported by them), raw and estimated after compression.

This is the number to watch. It's the most direct link between your code and LCP for client-rendered apps.

## 233: How do you reduce the size of the main bundle?

- Lazy load every route that isn't the landing page
- `@defer` heavy parts of the landing page
- Move app-wide providers and libraries out of `app.config.ts` when they're only used on some pages
- Remove unused dependencies and big polyfills
- Replace large libraries with smaller ones or native APIs
- Drop `@angular/animations` and Zone.js if you can
- Check for accidental imports into the initial chunk with a bundle analyzer

## 234: What is the cost of providers in app.config.ts?

Everything provided in `app.config.ts` (or imported there) is part of the initial bundle, because it's needed at bootstrap. Common mistakes:

- Providing a big library (charts, editors) globally when only one page needs it
- Adding `importProvidersFrom(SomeModule)` that pulls in a lot of code
- Registering a heavy `APP_INITIALIZER` / `provideAppInitializer` that blocks startup

Move providers to route-level `providers`, or use `providedIn: "root"` services that only load with the code that uses them.

## 235: What are route-level providers?

You can add providers to a route. They are created when the route is first activated and are part of that route's lazy chunk:

```ts
{
  path: "reports",
  loadComponent: () => import("./reports"),
  providers: [ReportsStore, provideCharts()],
}
```

This keeps feature-specific dependencies out of the initial bundle and gives the feature its own instance of the service.

## 236: Why can provideAppInitializer slow down startup?

Angular waits for every app initializer to finish before rendering anything. If an initializer makes an HTTP call (like loading config or the user), the user sees a blank page until it finishes.

```ts
provideAppInitializer(() => inject(ConfigService).load());
```

Keep initializers fast, run them in parallel, cache their results, or render a shell first and load non-critical data later. Only block startup for data you really can't render without.

## 237: How do you speed up the time until the user sees something?

- Prerender or server render the first page
- Put a lightweight loading shell in `index.html` (inside `<app-root>`) so something appears before JS runs
- Inline critical CSS (on by default)
- Avoid blocking app initializers
- Keep the initial bundle small
- Preload the LCP image and main font

## 238: How do you analyze and reduce CSS size in an Angular app?

- Check the `styles.css` size in the build output
- Use the `anyComponentStyle` budget to find big component styles
- Import only needed parts of CSS frameworks (for example Sass partials instead of the whole Bootstrap)
- With Tailwind, make sure unused classes are purged (Tailwind does this by scanning your templates)
- Avoid `@import` of large global files inside component styles, because they're duplicated in each component

## 239: Why can @import of a global Sass file in components increase bundle size?

Each component's styles are compiled separately. If every component imports a big partial that contains real CSS (not just variables and mixins), that CSS is copied into every component.

Only put variables, mixins and functions in files imported by components. Or use `@use` with partials that produce no output, and keep real global CSS in `styles.scss`.

## 240: What is ViewEncapsulation and does it affect performance?

`ViewEncapsulation.Emulated` (the default) adds unique attributes to elements and rewrites CSS selectors to use them. `ShadowDom` uses the browser's shadow DOM. `None` makes styles global.

The performance difference is small in most apps. Emulated selectors are a bit more specific, and `None` can cause style conflicts. Since Angular 22, styles are removed when their component's host element is gone, which reduces leftover CSS in long sessions.

## 241: How do you optimize fonts in an Angular app?

- Self-host fonts in WOFF2
- Use `font-display: swap` or `optional`
- Preload the one or two most important font files
- Subset fonts to the characters you need
- Use fewer font weights and styles, or a variable font
- Let the CLI inline Google Fonts CSS (`optimization.fonts.inline`)

Fonts often block text rendering and cause layout shifts, so they matter for both LCP and CLS.

## 242: How do you configure the image breakpoints for NgOptimizedImage?

Use `IMAGE_CONFIG`:

```ts
providers: [
  {
    provide: IMAGE_CONFIG,
    useValue: {
      breakpoints: [320, 640, 960, 1280, 1920],
      placeholderResolution: 40,
    },
  },
];
```

When the image has `sizes` and a loader, Angular generates a `srcset` using these widths. Fewer breakpoints means fewer image variants to cache on the CDN.

## 243: How do you use the sizes attribute with NgOptimizedImage?

`sizes` tells the browser how wide the image will be at different screen widths. Angular uses it to build a responsive `srcset`:

```html
<img
  ngSrc="products/shoe.jpg"
  width="800"
  height="800"
  sizes="(max-width: 768px) 100vw, 33vw"
/>
```

Without `sizes`, the browser assumes the image is 100% of the viewport, and may download a much bigger file than needed.

## 244: How do you write a custom image loader?

```ts
import { IMAGE_LOADER, ImageLoaderConfig } from "@angular/common";

providers: [
  {
    provide: IMAGE_LOADER,
    useValue: (config: ImageLoaderConfig) => {
      const width = config.width ? `&w=${config.width}` : "";
      return `https://img.example.com/${config.src}?format=auto${width}`;
    },
  },
];
```

Angular calls the loader with each width it needs for `srcset`. You can also pass extra values with `loaderParams` on the image.

## 245: What does NgOptimizedImage warn about in development mode?

Some of the checks:

- The LCP image doesn't have `priority`
- Missing `width`/`height` (or `fill`)
- The rendered size and aspect ratio don't match the image file
- The image file is much larger than how it's displayed
- No `preconnect` for the image origin when it's the LCP image
- Too many `priority` images

These warnings are a quick way to find image problems without running Lighthouse.

## 246: How do you avoid too many priority images?

Only the LCP image (and maybe one or two others clearly above the fold) should have `priority`. If every image is high priority, the browser can't prioritize, and the LCP image competes with the rest.

For carousels, mark only the first slide as `priority`. For product grids, mark only the first row if it's in the initial viewport.

## 247: How do you speed up Angular unit tests?

- Use Vitest, which is the default test runner for new projects since Angular 21 and is much faster than Karma
- Avoid importing big modules in `TestBed` when you only need a few providers
- Mock heavy dependencies (HTTP, charts, editors)
- Prefer testing logic in plain functions and services where possible
- Run tests in parallel and only for changed files in CI

## 248: How do you speed up Angular builds in CI?

- Use the esbuild `application` builder (`@angular/build`)
- Keep the CLI disk cache between CI runs (`.angular/cache`) when possible
- Use `npm ci` with a cached package directory
- Build only what changed in monorepos (Nx affected, Turborepo)
- Don't build source maps or stats files you don't use

## 249: How do you configure the Angular CLI cache?

The CLI caches build results in `.angular/cache` by default. You can control it in `angular.json`:

```json
"cli": {
  "cache": {
    "enabled": true,
    "environment": "all",
    "path": ".angular/cache"
  }
}
```

`environment` can be `local`, `ci` or `all`. By default the cache is only on locally, so set `all` or `ci` if you want to reuse it in CI.

## 250: What is the cost of i18n in an Angular app and how do you keep it low?

Angular's built-in i18n compiles a separate build for each locale (`ng build --localize`). Translations are baked in at build time, so there's no runtime cost and no extra translation bundle.

Runtime libraries (like ngx-translate or Transloco) load translation files at runtime and translate in templates. Keep them fast by lazy loading translation files per feature and avoiding impure pipes on huge lists.

## 251: How do you keep a runtime translation pipe fast?

A translate pipe usually has to be impure, because the language can change at runtime. That means it runs on every check for every use.

Ways to reduce the cost:

- Use a library that supports signals or structural directives, so translations are resolved once per view
- Cache the lookups inside the pipe
- Load only the translation files for the current feature
- Use OnPush everywhere so impure pipes run less often

Or use Angular's compile-time i18n, which has no runtime cost at all.

## 252: How do you avoid blocking the UI when processing large data in the browser?

- Move the work to a web worker
- Split it into chunks and yield to the browser between them (`scheduler.yield()` where supported, or `setTimeout`)
- Process data on the server and send what the UI needs
- Show partial results as they're ready

```ts
async processInChunks(rows: Row[]) {
  for (let i = 0; i < rows.length; i += 500) {
    this.handle(rows.slice(i, i + 500));
    await new Promise((r) => setTimeout(r));
  }
}
```

## 253: How do you use a web worker generated by the Angular CLI?

```bash
ng generate web-worker reports/report
```

This creates `report.worker.ts` and updates the tsconfig. Use it like this:

```ts
// report.worker.ts
addEventListener("message", ({ data }) => {
  postMessage(buildReport(data));
});
```

```ts
// component
const worker = new Worker(new URL("./report.worker", import.meta.url));
worker.onmessage = ({ data }) => this.report.set(data);
worker.postMessage(this.rows());
```

Remember to call `worker.terminate()` when it's no longer needed.

## 254: What is the cost of sending data to a web worker?

Data is copied between threads using structured cloning. For big objects (tens of MB), the copy itself can take time on the main thread.

Ways to reduce it:

- Send only what the worker needs
- Use transferable objects like `ArrayBuffer`, which are moved, not copied
- Keep data in the worker and send only small results back

If the computation is cheaper than the copy, a worker won't help.

## 255: How do you make a dashboard with many widgets load faster?

- `@defer (on viewport)` for widgets below the fold
- `@defer (on idle)` or `on timer` for above-the-fold widgets that aren't the main content
- Load each widget's data in parallel, not one after another
- Show skeletons with the right size to avoid CLS
- Lazy load chart libraries
- Cache widget data that doesn't change often

## 256: How do you avoid request waterfalls in Angular?

A waterfall is when requests run one after another because each waits for the previous one. Common causes in Angular:

- Parent loads data, then child loads its data after rendering
- A resolver waits for one call before starting the next
- Lazy chunk loads, then the component inside starts its request

Fixes: start independent requests in parallel (`forkJoin`, several resources at once), start loading in the route (resolver or route-level service) alongside the chunk download, or have the backend return combined data.

## 257: Are route resolvers good or bad for performance?

A resolver waits for data before the route activates. The user sees the old page until the data arrives, which can feel slow for slow APIs.

Good uses: small, fast data you can't render without. For slow data, it's often better to navigate right away and show a loading state in the component. You can also start the request in the resolver without waiting for it, by passing a resource or signal.

## 258: How does withComponentInputBinding affect performance?

It binds route params, query params and resolver data directly to component inputs:

```ts
provideRouter(routes, withComponentInputBinding());
```

```ts
export class ProductPage {
  id = input.required<string>();
  product = httpResource<Product>(() => `/api/products/${this.id()}`);
}
```

It doesn't make things faster by itself, but it removes `ActivatedRoute` subscriptions and fits signals and OnPush well.

## 259: How does Angular reuse components when only route params change?

By default, when you navigate from `/product/1` to `/product/2`, the router reuses the same component instance and only updates the params. Code that reads params only once in `ngOnInit` won't update.

This is good for performance (no destroy and recreate), but you need to react to param changes, with signal inputs and `computed()`/`httpResource`, or by subscribing to `paramMap`.

## 260: What is a RouteReuseStrategy and when would you use it for performance?

`RouteReuseStrategy` decides whether the router keeps a route's component tree in memory when you leave it, and restores it when you come back. A custom strategy can cache a heavy list page, so going back from a detail page is instant and keeps the scroll position.

The trade-off is memory use and stale data. Only cache a few routes, and clear them when data changes.

## 261: How do you restore scroll position without extra work?

```ts
provideRouter(
  routes,
  withInMemoryScrolling({
    scrollPositionRestoration: "enabled",
    anchorScrolling: "enabled",
  }),
);
```

The router saves the scroll position on navigation and restores it when going back. It only works well if the content is ready when the position is restored, so cache list data or keep it in a service.

## 262: What are view transitions in the Angular router?

```ts
provideRouter(routes, withViewTransitions());
```

The router uses the browser's View Transitions API to animate between pages. The browser takes snapshots of the old and new page and animates between them.

It doesn't make loading faster, but it can make navigation feel smoother. It adds a small delay while snapshots are taken, so check it doesn't hurt INP on heavy pages.

## 263: How do you make a search input feel instant?

- Update the input immediately, don't block typing on the request
- Debounce the request (200-300 ms)
- Cancel old requests (`switchMap` or `httpResource`)
- Show cached results right away and refresh them
- Keep the results list fast (track by id, OnPush rows, limit the number of results)

If filtering is local, `computed()` over a reasonably sized list is often fast enough without debouncing.

## 264: How do you handle frequent updates from WebSockets without killing performance?

- Batch updates instead of updating the UI on every message (`bufferTime(100)` or `auditTime`)
- Update only the items that changed, keeping other references the same
- Use signals so only affected views refresh
- In Zone.js apps, connect the socket outside Angular

```ts
this.socket.messages$
  .pipe(
    bufferTime(200),
    filter((batch) => batch.length > 0),
    takeUntilDestroyed(),
  )
  .subscribe((batch) => this.applyUpdates(batch));
```

## 265: What is the cost of console errors and warnings in dev mode?

Dev mode warnings (like `NgOptimizedImage` hints or `@for` duplicate key warnings) don't run in production, so they don't cost anything there. But if your app logs a lot in production, every log takes time and can retain objects.

Treat dev-mode performance warnings as real issues to fix. They usually point to the same problems that make production slow.

## 266: How do you profile a slow click handler?

1. Open the Chrome Performance panel, set CPU throttling to 4x.
2. Start recording, click the button, stop.
3. Find the click event in the main thread and expand it.
4. Look at the time split: your handler, Angular change detection after it, style/layout, paint.

If the handler is slow, optimize or move the work. If change detection after it is slow, look at which components are checked. If layout is slow, look for big DOM changes or forced reflows.

## 267: How do you reduce work after a click in a big Angular page?

- Make components OnPush so only affected views are checked
- Use signals so only views reading the changed state refresh
- Keep the handler fast, start async work and return
- Avoid rendering large new DOM at once, defer or paginate
- Split big updates with `scheduler.yield()` or `setTimeout` so the browser can paint first

The goal is to get the next frame painted quickly, which is what INP measures.

## 268: How do you show feedback immediately during a slow operation?

Update a signal first, then do the slow part after the browser had a chance to paint:

```ts
async save() {
  this.saving.set(true); // spinner shows
  await new Promise((r) => requestAnimationFrame(() => setTimeout(r)));
  this.heavyWork();
  this.saving.set(false);
}
```

This keeps INP low because the next paint (with the spinner) happens fast. For really heavy work, use a web worker.

## 269: How do you avoid heavy work in getters used in templates?

Getters are called every time the template is checked:

```ts
get visibleItems() {
  return this.items.filter((i) => i.visible); // runs on every check
}
```

Replace them with `computed()`:

```ts
visibleItems = computed(() => this.items().filter((i) => i.visible));
```

Now the filter runs only when `items` changes.

## 270: What is the problem with using the json pipe or functions in large lists?

Anything that runs per row runs N times per check. A function call or `json` pipe on a list of 1,000 rows means 1,000 calls every time the component is checked.

Prepare display data once when the data changes (in `computed()` or when mapping the API response) so the template only reads plain values.

## 271: How do you check if Zone.js is still in your production bundle?

- Look at `angular.json` under `polyfills`
- Check the build output for a `polyfills` chunk and its size
- Open the app and type `Zone` in the console. If it's defined, Zone.js is loaded
- Angular warns in dev mode when you use zoneless but Zone.js is still loaded

Removing it saves around 30 KB raw (about 10 KB compressed) and removes the patching overhead.

## 272: What happens to NgZone in a zoneless app?

Angular provides a no-op `NgZone`. `run()` and `runOutsideAngular()` just call the function, and `onStable` and similar events don't work like before.

So code that uses `runOutsideAngular()` still works without changes. Code that waits for `onStable` or `onMicrotaskEmpty` needs to move to `afterNextRender()` or `afterEveryRender()`.

## 273: What is the cost of afterEveryRender()?

The callback runs after every change detection run in the whole app, not only when your component changes. If the callback does heavy work or reads layout, it slows down every update.

Prefer `afterNextRender()` for one-time setup, and `afterRenderEffect()` when the work depends on specific signals. Use `afterEveryRender()` only for cheap work that really needs to run every time.

## 274: How do you use the Angular DevTools injector tree for performance work?

The injector tree shows where each service is provided. It helps find:

- Services provided in components that should be singletons (created again for every component instance)
- Duplicate instances of a heavy service in lazy routes
- Providers in the root that are only needed in one feature

Too many instances of a heavy service can cost memory and repeated HTTP calls.

## 275: What is the cost of providing a service in a component's providers?

Each instance of the component creates a new instance of the service. For a list of 500 rows that each provide a service, you get 500 service instances.

```ts
@Component({
  selector: "app-row",
  providers: [RowState], // one per row
})
```

That's fine when you need per-component state. But for shared or heavy services, use `providedIn: "root"` or provide at the feature level.

## 276: How do you investigate a slow initial load in an Angular app?

1. Run Lighthouse on a production build to get LCP, FCP, TBT.
2. Check the Network panel: total JS size, number of requests, waterfalls, compression, caching.
3. Check the build output: initial total size, biggest chunks.
4. Look at the Performance panel: time spent parsing and running JS, long tasks at startup.
5. Check app initializers and the first API calls.

Then fix the biggest item: often a big initial chunk, a blocking API call or an unoptimized LCP image.

## 277: What is Total Blocking Time (TBT) and how does it relate to Angular?

TBT is the total time between FCP and Time to Interactive during which the main thread was blocked by long tasks (the part over 50 ms of each one). It's a lab metric that relates to INP.

In Angular apps, TBT goes up with large bundles (parse and execution), heavy app initialization, big first change detection runs and hydration of big pages. Incremental hydration and `@defer` reduce it.

## 278: How do you use the web-vitals library with Angular?

```ts
import { onCLS, onINP, onLCP } from "web-vitals";

export function reportVitals() {
  const send = (metric: { name: string; value: number }) =>
    navigator.sendBeacon("/api/vitals", JSON.stringify(metric));
  onLCP(send);
  onINP(send);
  onCLS(send);
}
```

Call it once in the browser, for example from `afterNextRender()` in the root component or from `main.ts`. It gives you field data from real users, which you can split by page and device.

## 279: How do you find which element is the LCP element?

- In Chrome DevTools Performance panel, the LCP marker in the Timings track points to the element
- Lighthouse shows the LCP element in its report
- `web-vitals` with the attribution build gives the element selector
- `NgOptimizedImage` warns in dev mode when the LCP image isn't marked `priority`

Once you know it, make sure it's in the server HTML, not deferred, and loads with high priority.

## 280: How do you speed up a slow API response from the Angular side?

You can't fix the server from Angular, but you can hide or reduce the delay:

- Start the request earlier (in parallel with code loading, or in a resolver)
- Cache the response and show cached data first
- Request less data (only needed fields, pagination)
- Use SSR so the server fetches data close to the API
- Show skeletons so the page doesn't feel stuck

And measure it, so you can give the backend team concrete numbers.

## 281: What does optimistic UI mean and how do you do it in Angular?

Optimistic UI updates the screen right away, before the server confirms the change, and rolls back if it fails:

```ts
async toggleLike(post: Post) {
  const previous = post.liked;
  this.posts.update((list) => list.map((p) => (p.id === post.id ? { ...p, liked: !previous } : p)));
  try {
    await firstValueFrom(this.api.like(post.id, !previous));
  } catch {
    this.posts.update((list) => list.map((p) => (p.id === post.id ? { ...p, liked: previous } : p)));
  }
}
```

The app feels faster because the user doesn't wait for the network.

## 282: How do you make lazy-loaded routes load faster on navigation?

- Preload them (all, by flag, or by visible links)
- Keep each route chunk small, defer heavy parts inside the page
- Start the data request when navigation starts, not after the component renders
- Use HTTP/2 or HTTP/3 and a CDN so chunk requests are fast
- Cache chunks with long-lived headers (they have hashes)

## 283: What does modulepreload have to do with Angular builds?

`<link rel="modulepreload">` tells the browser to download and parse an ES module early. The Angular `application` builder adds `modulepreload` links in `index.html` for the initial chunks, so the browser can download them in parallel instead of discovering them one import at a time.

That shortens the waterfall of chunk requests at startup.

## 284: How do you handle a very large NgModule-based shared module?

A big `SharedModule` that exports dozens of components forces every lazy route that imports it to include all of them, even unused ones.

Fix it by:

- Converting the components to standalone (`ng generate @angular/core:standalone`)
- Importing only what each component needs
- Removing the shared module when it's empty

This usually shrinks lazy chunks noticeably.

## 285: How do you migrate to the new control flow and why does it help performance?

Run the schematic:

```bash
ng generate @angular/core:control-flow
```

It converts `*ngIf`, `*ngFor` and `*ngSwitch` to `@if`, `@for` and `@switch`. You get the faster `@for` diffing, required `track` keys and less directive overhead. Check the generated `track` expressions afterwards. Where the old code had no `trackBy`, the schematic can't know your id field, so replace the generated key with a real id.

## 286: How do you migrate inputs and queries to signals?

The CLI has migrations:

```bash
ng generate @angular/core:signal-input-migration
ng generate @angular/core:signal-queries-migration
ng generate @angular/core:output-migration
```

Signal inputs and queries let Angular know exactly which views depend on which values. That's a good step before switching components to OnPush and the app to zoneless.

## 287: How does the inject() function relate to performance?

`inject()` itself is not faster than constructor injection. But it enables patterns that help performance:

- Functional guards, resolvers and interceptors without extra classes
- Helper functions like `injectAsync()` for lazy services
- Easier composition of small reusable functions instead of big base classes

Since Angular 22, the `@Service()` decorator only supports `inject()`, not constructor injection.

## 288: How do you avoid loading data on the server that the client will load anyway?

If some data is only needed in the browser (for example user-specific widgets on a public page), skip it on the server:

- Put that part in a `@defer` block, which renders only the placeholder on the server
- Or load the data in `afterNextRender()`
- Or use `RenderMode.Client` for routes that are fully user specific

The server render gets faster, and the HTML can be cached for everyone.

## 289: How do you keep SSR memory usage under control?

- Don't store request data in module-level variables, they live across requests
- Don't keep large caches without limits in the Node process
- Make sure intervals and subscriptions don't start on the server
- Set a max heap size and monitor it
- Use `PendingTasks` correctly so renders finish

A leak on the server affects every user, not just one tab, so watch heap usage in production.

## 290: How do you run SSR with Angular's Node app engine?

The generated `server.ts` uses `AngularNodeAppEngine`:

```ts
import {
  AngularNodeAppEngine,
  createNodeRequestHandler,
  isMainModule,
  writeResponseToNodeResponse,
} from "@angular/ssr/node";
import express from "express";

const app = express();
const angularApp = new AngularNodeAppEngine();

app.use(express.static(browserDistFolder, { maxAge: "1y", index: false }));

app.use((req, res, next) => {
  angularApp
    .handle(req)
    .then((response) =>
      response ? writeResponseToNodeResponse(response, res) : next(),
    )
    .catch(next);
});

export const reqHandler = createNodeRequestHandler(app);
```

Static files are served directly with long cache times, and only page requests go through rendering.

## 291: Why should static files be served before the Angular SSR handler?

Static files (JS, CSS, images) don't need rendering. If they go through the Angular handler, the server wastes CPU, adds latency and may return the wrong content.

Serve them first with long cache headers (they have hashed names), ideally from a CDN, and let the SSR handler only deal with page routes.

## 292: How do you cache SSR responses with headers?

You can set headers per route in the server routes config:

```ts
{
  path: "blog/**",
  renderMode: RenderMode.Server,
  headers: { "Cache-Control": "public, max-age=60, stale-while-revalidate=600" },
}
```

A CDN in front then serves cached HTML for most requests. Only use public caching for pages that don't contain user-specific data.

## 293: What is the cost of hydrating a big page all at once?

Full hydration has to download all JavaScript for the page, create all components and walk the whole DOM before the page is fully interactive. On a long page with many components, that's a lot of main thread work, which shows up as long tasks and higher TBT and INP.

Incremental hydration fixes this by hydrating only what's needed, when it's needed.

## 294: How do you decide which parts of a page to hydrate incrementally?

- Hero and main content the user sees and interacts with first: hydrate normally
- Below-the-fold interactive parts: `hydrate on viewport`
- Parts that need a click: `hydrate on interaction`
- Menus and tooltips: `hydrate on hover`
- Static content: `hydrate never`

Profile before and after. The goal is fewer and shorter long tasks during startup.

## 295: How does event replay work with incremental hydration?

When a user clicks inside a block that isn't hydrated yet, Angular records the event. It then loads the code for that block (and its parents if needed), hydrates it, and replays the event to the right handler.

So the click isn't lost, it's just handled after a small delay. That's why `hydrate on interaction` is safe even for buttons.

## 296: What is the trade-off of hydrate on interaction?

The first interaction has a delay, because the code must be downloaded and the block hydrated before the handler runs. On slow networks this delay can be noticeable and hurt INP for that interaction.

Use `prefetch` (for example `prefetch on idle` or `prefetch on viewport`) together with the hydrate trigger, so the code is usually already there when the user interacts.

## 297: How do you avoid SSR rendering content that depends on the browser window size?

The server doesn't know the screen size, so content that depends on `window.innerWidth` will differ between server and client and cause mismatches or layout shifts.

Prefer CSS media queries for responsive layout. If you must change content by size, render a neutral version on the server and switch in `afterNextRender()`, or use client hints if your server supports them.

## 298: How do you lazy load a component inside a dialog?

With Angular CDK or Material dialogs, load the component class when the dialog opens:

```ts
private dialog = inject(Dialog);

async openSettings() {
  const { SettingsDialog } = await import("./settings-dialog");
  this.dialog.open(SettingsDialog);
}
```

The dialog code is only downloaded when the user opens it. You can prefetch it on hover of the button if it's a large component.

## 299: How do you reduce the number of change detection runs triggered by mouse movement?

- Use CSS for hover effects (`:hover`) instead of `(mouseenter)` and signals
- For drag or mousemove logic, add listeners outside Angular (in Zone.js apps) and update state with `requestAnimationFrame`
- Throttle updates to once per frame
- In zoneless apps, only update signals when the visible value actually changes

## 300: How do you build a fast autocomplete in Angular?

- Debounce input (`debounced()` in v22 or RxJS `debounceTime`)
- Cancel stale requests (`httpResource` or `switchMap`)
- Limit results to 10-20 items
- Cache recent queries
- Render options with `track` by id and OnPush option components
- Use `aria-activedescendant` instead of moving focus between options, which avoids extra rendering work

```ts
query = signal("");
debouncedQuery = debounced(this.query, 250);
options = httpResource<Option[]>(() => {
  const q = this.debouncedQuery.value();
  return q ? `/api/cities?q=${encodeURIComponent(q)}&limit=10` : undefined;
});
```

When the request function returns `undefined`, `httpResource` doesn't send a request.

# Advanced Questions (301-450)

## 301: How does Angular's change detection work internally with LViews?

Every component view is stored as an `LView`, an array that holds the view's state: DOM nodes, binding values from the last check, child views and flags. A shared `TView` holds the static template data for all instances of the same component.

During change detection, Angular calls the compiled template function in update mode for each view it refreshes. Each binding compares its new value with the value stored in the `LView` and touches the DOM only when they differ. Flags on the `LView` (dirty, needs refresh, has child views to refresh) decide which views are visited.

## 302: What does the compiled template function look like and why is it fast?

The compiler turns a template into a function with two parts: create mode (build DOM nodes once) and update mode (refresh bindings). Simplified:

```ts
function Hello_Template(rf: number, ctx: Hello) {
  if (rf & 1) {
    ɵɵelementStart(0, "h1");
    ɵɵtext(1);
    ɵɵelementEnd();
  }
  if (rf & 2) {
    ɵɵadvance();
    ɵɵtextInterpolate1("Hello ", ctx.name(), "");
  }
}
```

Update mode only runs the binding instructions, in a fixed order, with no template parsing at runtime. The instructions are small functions that tree-shake well, so features you don't use aren't in the bundle.

## 303: How do signals mark views for refresh internally?

Each template has a reactive consumer node. When the template reads a signal during rendering, the signal is recorded as a producer of that consumer. When the signal changes, it notifies its consumers, and the template's consumer marks its `LView` with a "refresh view" flag and marks ancestors with "has child views to refresh". It also tells the scheduler to run.

On the next run, Angular walks down to that view without refreshing the parents' bindings, then refreshes only that view. That's the targeted refresh people sometimes call "local change detection".

## 304: What is the difference between markForCheck() and a signal change in how they mark the tree?

- `markForCheck()` marks the current view and **every ancestor** as dirty. All those OnPush ancestors are refreshed in the next run, so their template bindings are evaluated.
- A signal change marks the view that read it for refresh and only flags ancestors as "has children to refresh". Ancestors are traversed but their own bindings are not evaluated.

So in a deep tree, signals avoid re-running the bindings of every parent.

## 305: Why does an Eager component inside an OnPush parent behave unexpectedly?

If an OnPush parent isn't dirty, Angular skips it and its whole subtree, including Eager children. So the Eager child isn't checked on every run, despite its strategy.

When the OnPush parent is refreshed, its Eager children are checked. With signals, if a signal in the Eager child changes, Angular can still reach and refresh it through the "has children to refresh" flag. The rule of thumb: once a parent is OnPush, children effectively follow its schedule unless they use signals.

## 306: What does detach() really do and when is it worth using?

`ChangeDetectorRef.detach()` removes the view from the change detection tree. Angular won't check it, even if its parent is checked, until you call `reattach()` or check it manually with `detectChanges()`.

```ts
export class Ticker {
  private cdr = inject(ChangeDetectorRef);

  constructor() {
    this.cdr.detach();
    afterNextRender(() => {
      setInterval(() => {
        this.update();
        this.cdr.detectChanges();
      }, 1000);
    });
  }
}
```

It's worth it for a component with very frequent updates that you want to render on your own schedule. With signals, you rarely need it.

## 307: How does the zoneless scheduler avoid running change detection too often?

When notified, the scheduler sets a flag and schedules one callback. Further notifications while a run is pending are ignored. The callback uses a race between `setTimeout` and `requestAnimationFrame`, whichever comes first, so the run lands before the next frame without waiting too long.

During a run, if code marks more views dirty (for example an effect writes a signal), Angular repeats the check loop a limited number of times in the same run instead of scheduling a new one. If it keeps looping, Angular throws an error (NG0103) to stop infinite loops.

## 308: What is error NG0103 and how does it relate to performance?

NG0103 means change detection kept finding dirty views after many passes and stopped, which is an infinite change detection loop. Usually something writes to state during rendering: an effect that sets a signal it reads, a getter that changes state, or `afterEveryRender` that sets a signal every time.

Besides the error, these loops waste CPU on every update. Fix the data flow with `computed()`, `linkedSignal()` or by moving writes into event handlers.

## 309: How do effects get scheduled relative to change detection?

There are two kinds:

- **Root effects** (created in services or outside components) run as part of the app-level change detection, before views are refreshed.
- **View effects** (created in components or directives) run during the refresh of their view, before the template is checked.

So an effect writing to a signal that a template reads will update in the same pass, without an extra cycle. But it still adds work to every pass where the effect's dependencies changed.

## 310: How would you design state for a large OnPush and zoneless app?

- Keep state in signal-based stores (services or NgRx SignalStore)
- Expose read-only signals and update with methods, no direct mutation
- Use `computed()` for derived data, close to where it's used
- Keep data normalized (entities by id) so updating one item doesn't replace big trees
- Pass small, specific inputs to components, not whole state objects
- Load data with resources so loading and errors are signals too

With this, a change refreshes only the views reading the changed signal.

## 311: Why is normalized state good for rendering performance?

If you store a list of orders where each has an embedded customer object, updating one customer means replacing many order objects. Every row with a changed reference re-renders.

With normalized state:

```ts
customers = signal<Record<string, Customer>>({});
orders = signal<Order[]>([]); // order.customerId
```

Updating one customer only changes `customers`. Row components that read `customers()[order.customerId]` through a `computed()` only update when their own customer object changes.

## 312: What is the cost of a computed() that depends on a large array?

The `computed()` re-runs whenever the array signal gets a new reference, even if only one element changed. If it filters or sorts 10,000 items, that's done in full every time.

Options:

- Split state so the big array changes rarely
- Use per-item signals or per-item computeds in row components
- Keep a pre-sorted index and update it incrementally
- Move the work to a worker or the server

Also give the `computed()` a custom `equal` function if it often produces equivalent results, so consumers aren't notified needlessly.

## 313: When should you use a custom equal function on computed()?

When the `computed()` often returns a new object or array with the same content:

```ts
selectedIds = computed(
  () =>
    this.items()
      .filter((i) => i.selected)
      .map((i) => i.id),
  {
    equal: (a, b) => a.length === b.length && a.every((v, i) => v === b[i]),
  },
);
```

Without `equal`, every new array counts as a change and every consumer updates. With it, consumers update only when the ids really changed. Keep the comparison cheaper than the work it saves.

## 314: How does Angular avoid "glitches" when several signals change at once?

Signals use a push-pull model. When a signal changes, it only pushes a "maybe dirty" notification to its consumers. Values are recomputed lazily when someone reads them (pull). Each `computed()` checks whether its producers really changed (by version numbers) before recomputing.

Since templates are read during change detection, after all your synchronous writes are done, every `computed()` sees the final values. There is never a render with one signal updated and another not yet.

## 315: How do you profile signal performance?

- Angular DevTools has a signal graph view showing signals, computeds and effects for a component and their dependencies
- The Chrome Performance panel with Angular profiling shows template refreshes and effect runs
- Count recomputations with a temporary `console.count()` inside a `computed()` during development

Look for computeds that recompute far more often than their inputs change, and effects that run on every pass.

## 316: How does Angular's @for algorithm handle moves efficiently?

`@for` uses a diffing algorithm optimized for common cases: items added or removed at the start or end, and a few items moving. It compares the start and end of the old and new lists first, then uses a map of keys for the remaining middle part.

Existing views are reused and only moved in the DOM when needed. Compared to `NgForOf` with `IterableDiffer`, it has less overhead and handles common operations with fewer DOM moves.

## 317: What happens when you replace a list of 1,000 items with a new array with the same ids?

With `track item.id`, Angular matches every new item to an existing view by key. No views are created or destroyed. It updates each view's context (the `$implicit` item) and then each row's bindings are checked. If row components are OnPush with signal inputs, only rows whose input value actually changed re-render.

With `track item` (identity), all 1,000 items would look new, so all views would be destroyed and recreated.

## 318: How do you render a list of 50,000 rows without virtual scrolling?

Usually you shouldn't. But if you must (for example for printing or `Ctrl+F` search):

- Render in chunks across frames (incremental rendering): show the first 200, then add more each frame
- Use CSS `content-visibility: auto` with `contain-intrinsic-size` so the browser skips layout and paint for off-screen rows
- Keep row templates minimal (no components per cell, no listeners per row)

```css
.row {
  content-visibility: auto;
  contain-intrinsic-size: auto 40px;
}
```

## 319: What is content-visibility and how can it help Angular apps?

`content-visibility: auto` tells the browser to skip rendering work (layout and paint) for elements that are off screen. The DOM nodes still exist, but the browser treats them as placeholders until they get close to the viewport.

For long pages built with Angular (feeds, long forms, docs), it can cut rendering time a lot without changing Angular code. Combine it with `contain-intrinsic-size` to keep scrollbar size stable. It doesn't reduce Angular's own change detection work, only the browser's rendering work.

## 320: How do you build incremental rendering for a big list with signals?

```ts
export class BigList {
  items = input.required<Item[]>();
  private count = signal(100);
  visible = computed(() => this.items().slice(0, this.count()));

  constructor() {
    afterNextRender(() => {
      const grow = () => {
        if (this.count() < this.items().length) {
          this.count.update((c) => c + 200);
          requestAnimationFrame(grow);
        }
      };
      requestAnimationFrame(grow);
    });
  }
}
```

The first frame shows 100 rows fast, then 200 more rows are added per frame until the list is complete. Each frame is a short task, so the page stays responsive.

## 321: How does hydration match server DOM to client components?

During SSR, Angular adds a small amount of info to the HTML: an `ngh` attribute on component hosts pointing to serialized data in a script tag (`ng-state`), describing how many nodes each view has, where containers are and which nodes were skipped.

On the client, Angular walks the existing DOM in the same order the template would create it, uses this info to find the right nodes and attaches them to the new views instead of creating new nodes. If the structure doesn't match, it reports a mismatch.

## 322: Why can HTML comment stripping by a CDN break hydration?

Angular uses HTML comments as markers for containers (like `@if` and `@for` anchors) in the server output. Some CDNs and HTML minifiers remove comments to save bytes.

Without those markers, Angular can't find the right anchor nodes during hydration and fails with error NG0507 or similar. Disable comment stripping for HTML responses in the CDN.

## 323: What is the cost of serialized hydration data and how do you keep it small?

The `ngh` data and the transfer state (cached HTTP responses) are embedded in the HTML. On data-heavy pages, the transfer cache can add hundreds of KB, because every response the server used is included.

Keep it small:

- Request only the fields you need from the API
- Exclude big responses from the transfer cache with `filter` or `transferCache: false`
- Don't fetch data on the server that the page doesn't render

Check the size of the `ng-state` script in the page source.

## 324: How does incremental hydration decide what code to download?

Each `@defer` block with hydrate triggers has its own chunk. When a trigger fires, Angular finds which deferred blocks must be hydrated, including parent defer blocks that aren't hydrated yet (a child can't hydrate before its parent). It downloads their chunks, hydrates top-down and replays events.

Blocks without a triggered hydrate stay as static HTML and their code is never downloaded.

## 325: What happens with signals and state changes inside a block that isn't hydrated yet?

A dehydrated block is just server HTML. There's no component instance, so it can't react to signal changes or inputs. If the parent changes data that the block displays, the block still shows the old server-rendered content until it's hydrated.

So `hydrate never` and long-delayed hydration only fit content that doesn't need to change based on client state, or where showing the server version for a while is acceptable.

## 326: How do you design a page with incremental hydration for the best INP?

- Keep the top-level shell small so the initial hydration is fast
- Wrap independent interactive sections in separate `@defer` blocks
- Use `hydrate on interaction` or `hydrate on hover` for widgets and `prefetch on idle` so code is ready
- Avoid one big defer block around everything, it brings back the "hydrate all" cost
- Avoid deeply nested defer blocks where an interaction at the bottom has to hydrate many parents first

## 327: What are the main costs on the server for Angular SSR?

- Bootstrapping the app per request (DI setup, creating components)
- Running change detection and generating HTML
- Waiting for data from APIs
- Serializing transfer state and hydration info
- Memory per concurrent request

Rendering is CPU bound, and Node is single threaded per process. Under load, use several processes (cluster or containers), cache rendered pages, prerender what you can, and keep server-side API calls fast and close.

## 328: How would you load test an Angular SSR server?

- Use a tool like k6, autocannon or wrk against real routes
- Test with realistic data and API latency (mock or staging APIs)
- Watch p95/p99 render time, CPU, event loop lag and memory
- Test with and without the CDN cache to see the worst case
- Find the requests per second per CPU core before latency climbs

Then decide how many instances you need, and which routes to prerender or cache.

## 329: What is event loop lag and why does it matter for SSR?

Event loop lag is how long callbacks wait before running because the event loop is busy. When one render takes 150 ms of CPU, every other request on that process waits.

Rendering is synchronous work in big pieces, so heavy pages directly increase lag. Monitor it (for example with `perf_hooks.monitorEventLoopDelay`) and scale out when it goes up.

## 330: How do you avoid sharing state between requests in SSR?

Angular creates a new injector tree per request, so `providedIn: "root"` services are per request on the server. Problems come from:

- Module-level variables (`let cache = ...` at the top of a file)
- Static class fields
- Singletons created outside Angular DI

Those live for the whole Node process and are shared by every user. Keep request data in DI services, and keep process-level caches only for data that is the same for everyone.

## 331: How do you decide between prerendering and SSR with caching?

Prerendering:

- Zero render cost per request, cheapest and fastest
- Needs a rebuild (or incremental rebuild) when content changes
- Doesn't scale well to millions of pages

SSR with CDN caching:

- Fresh content after cache expiry, no rebuild needed
- First request after expiry pays the render cost (hidden by `stale-while-revalidate`)
- Works for any number of pages

Many sites prerender the most visited pages and use cached SSR for the long tail.

## 332: How do you prerender thousands of pages without slow builds?

- Prerender only the most important pages, fall back to SSR for others (`PrerenderFallback.Server`)
- Make `getPrerenderParams` fast (one API call that returns all ids)
- Make sure data APIs used during prerender are fast or cached
- Split builds by site section if needed

The CLI renders pages in parallel using worker threads, but each page still costs time, so thousands of pages can add minutes to the build.

## 333: What are the internals of NgOptimizedImage's priority preloading in SSR?

When an image has `priority` and the app renders on the server, the directive registers a preload link with the image's `src`, `srcset` and `sizes`. The server adds `<link rel="preload" as="image" ...>` to the document `<head>`.

The browser discovers the image as soon as it parses the head, before it reaches the `<img>` tag or runs any JavaScript. Combined with `fetchpriority="high"`, this usually gives the biggest LCP improvement for image-heavy pages.

## 334: How would you reduce LCP for a client-rendered Angular app without SSR?

- Shrink the initial bundle as much as possible (lazy routes, `@defer`, remove heavy dependencies)
- Preload the LCP image manually in `index.html` if it's known
- Inline critical CSS (default)
- Avoid blocking initializers and API calls before first render
- Render a static shell in `index.html` that looks like the page
- Use a CDN with HTTP/2 or HTTP/3 and long caching for chunks

Still, SSR or prerendering is usually the biggest single LCP win for content pages.

## 335: How does the build decide what goes into the initial chunk?

The bundler starts from `main.ts` and follows every static `import`. Everything reachable that way is initial. Every dynamic `import()` (lazy routes, `@defer` dependencies, your own `import()` calls) starts a new lazy chunk.

Code shared between lazy chunks goes into shared chunks. If something is reachable from both `main.ts` and a lazy chunk, it stays in the initial bundle. So one static import in a file used at startup can pull a big library into the initial load.

## 336: How do you find why a library ended up in the initial bundle?

Use the esbuild metafile:

```bash
ng build --stats-json
```

Upload `stats.json` to esbuild.github.io/analyze. Click the library's files and look at the import path. It shows the chain of imports from the entry point to the library. Then break that chain: move the import behind a dynamic `import()`, a lazy route or `@defer`.

## 337: What is the cost of a large number of lazy chunks?

Each chunk is a separate request. Too many tiny chunks can add overhead:

- More requests and HTTP/2 stream handling
- Less compression efficiency (small files compress worse)
- Waterfalls if chunks import other chunks in sequence

In practice, with HTTP/2 and modulepreload, Angular apps rarely have problems with this. Focus on not loading code that's not needed, and only merge chunks if measurements show request overhead.

## 338: How would you set up performance budgets in CI beyond bundle size?

- **Bundle budgets** in `angular.json` (build fails on regression)
- **Lighthouse CI** on key pages with assertions on LCP, TBT and CLS
- **Bundle size diff** comments on pull requests
- **Field data alerts** from real user monitoring (p75 LCP and INP per page)
- **Performance tests** that record a Performance trace for key interactions

Lab budgets catch regressions early, field data shows what users really get.

## 339: How do you investigate high INP in production for an Angular app?

1. Collect INP with the `web-vitals` attribution build, which gives the element, event type, and time split (input delay, processing, presentation delay).
2. Group by page and interaction target to find the worst ones.
3. Reproduce locally with CPU throttling and record a trace.
4. If input delay is high: other long tasks were running (startup, hydration, timers).
5. If processing is high: the handler or the change detection after it is slow.
6. If presentation delay is high: large DOM updates, layout and paint.

Each part has a different fix.

## 340: What is input delay and what causes it in Angular apps?

Input delay is the time between the user's interaction and when the event handler starts running. The handler waits because the main thread is busy.

In Angular apps, common causes are: hydration or bootstrap still running, a big change detection run from another event, timers or polling doing heavy work, and third-party scripts. Incremental hydration, splitting long tasks and deferring non-critical work help.

## 341: How do you split a long task in an Angular event handler?

Do the urgent part, let the browser paint, then continue:

```ts
async onFilterChange(filter: Filter) {
  this.filter.set(filter); // update the input UI right away
  await yieldToMain();
  this.results.set(this.applyFilter(filter)); // heavier work
}
```

```ts
function yieldToMain(): Promise<void> {
  const s = (globalThis as any).scheduler;
  if (s?.yield) return s.yield();
  return new Promise((resolve) => setTimeout(resolve, 0));
}
```

In a zoneless app, Angular renders the first update before the `setTimeout` callback runs, so the user sees feedback right away.

## 342: Does Angular batch signal updates made in different tasks?

No. Angular batches updates made within the same task (and microtasks before the scheduled render). If you update a signal, then `await` a `setTimeout`, then update again, you get two renders.

That's usually what you want, because it lets the browser paint in between. But when you process many small updates from separate tasks (like socket messages), you should batch them yourself to avoid one render per message.

## 343: What is the cost of hydration on low-end devices and how do you measure it?

Hydration runs the app's bootstrap and creates all components for the hydrated part of the page. On a slow phone, a big page can take several hundred milliseconds of main thread time.

Measure it with a Performance trace on a real device or with 6x CPU throttling. Look at the long tasks after the HTML is shown. The Angular profiling track shows hydration and component creation. Compare TBT with and without incremental hydration.

## 344: How do you make Angular DevTools profiling results reliable?

- Profile dev builds only for finding which components are slow, not for absolute numbers. Dev mode adds extra checks
- Repeat the same action several times and look at averages
- Close other tabs and extensions
- Use CPU throttling to make differences clearer
- Confirm the improvement with a production build and the Chrome Performance panel

## 345: How can you profile a production build?

Production builds strip dev-only code, so Angular DevTools won't work. You can still:

- Use the Chrome Performance panel. With source maps, function names map back to your code
- Build with `"namedChunks": true` and source maps to make traces readable
- Add `performance.mark()` and `performance.measure()` around important code, they show in the Timings track
- Use the `web-vitals` library and long animation frame (LoAF) data from real users

## 346: What is the Long Animation Frames API and why is it useful for Angular apps?

The Long Animation Frames API (LoAF) reports frames that took longer than 50 ms, with details about which scripts ran, how long, and from which source file and function.

```ts
new PerformanceObserver((list) => {
  for (const entry of list.getEntries()) {
    sendToMonitoring(entry.toJSON());
  }
}).observe({ type: "long-animation-frame", buffered: true });
```

For Angular apps it tells you in production which handler, change detection or third-party script caused a slow frame, which is hard to get otherwise. It's supported in Chromium-based browsers.

## 347: How do you track performance of route navigations?

Listen to router events and measure the time between start and end:

```ts
const router = inject(Router);

router.events.subscribe((e) => {
  if (e instanceof NavigationStart) performance.mark(`nav-start-${e.id}`);
  if (e instanceof NavigationEnd) {
    performance.measure(`nav-${e.urlAfterRedirects}`, `nav-start-${e.id}`);
  }
});
```

This includes chunk loading, guards and resolvers. To include the moment content is shown, add a mark in `afterNextRender()` of the page component.

## 348: How does tree-shaking work with Angular's Ivy runtime?

In Ivy, each feature the compiler uses is a separate exported function (`ɵɵelementStart`, `ɵɵlistener`, `ɵɵpipe`, defer instructions, etc.). The compiled templates import only the instructions they use. Components also carry their own definitions (`ɵcmp`) instead of relying on a central module registry.

So if no template uses pipes or i18n, that code isn't in the bundle. This is why a small Angular app can be much smaller than with the old View Engine.

## 349: What is the cost of decorators like @Input in the final bundle?

The Angular compiler processes decorators at build time and turns them into static definitions (`ɵcmp`, `ɵdir`, `ɵfac`). The decorators themselves are removed from production builds, so there's no runtime reflection and no `reflect-metadata` needed.

Signal-based APIs (`input()`, `output()`, `viewChild()`) are regular function calls with similar compiled output. The bundle difference between them and decorators is small. The real benefit of signals is the runtime behavior.

## 350: How does Angular handle styles per component and what is the runtime cost?

Component styles are compiled at build time into strings in the component definition. When the first instance of a component is created, Angular adds a `<style>` element (or uses an adopted stylesheet in shadow DOM). With emulated encapsulation, the selectors were already rewritten at build time.

The runtime cost is adding styles once per component type. Since Angular 22, styles are removed when no host using them is left in the DOM. Very large component styles still cost parse time, which is why `anyComponentStyle` budgets exist.

## 351: How does dependency injection affect startup time in a large app?

Injectors are created lazily, and services are created the first time they're injected. Startup gets slow when:

- Root services do heavy work in their constructors (subscriptions, parsing, HTTP calls)
- Many services are injected eagerly by the root component or app initializers
- `importProvidersFrom` pulls in modules that create many providers

Keep constructors cheap, start work on demand and avoid injecting everything into `App`. `injectAsync()` (Angular 22) can delay loading and creating rarely used heavy services.

## 352: How does injectAsync work and how do you prefetch with it?

`injectAsync(loader)` returns a function. The first call runs the loader (a dynamic `import()`), gets the token and resolves it from the injector where `injectAsync` was called. Later calls reuse the same promise.

```ts
import { injectAsync, onIdle } from "@angular/core";

export class Editor {
  private spellcheck = injectAsync(
    () => import("./spellcheck.service").then((m) => m.SpellcheckService),
    { prefetch: onIdle },
  );

  async check(text: string) {
    return (await this.spellcheck()).check(text);
  }
}
```

With `prefetch: onIdle`, the code is downloaded when the browser is idle, so the first call is fast. The service must be auto-provided (`providedIn: "root"` or `@Service()`).

## 353: What is the @Service decorator and does it help performance?

`@Service()` is a new decorator in Angular 22, a simpler alternative to `@Injectable()`. It's `providedIn: "root"` by default (opt out with `autoProvided: false`), only supports `inject()` (no constructor injection), and has a single `factory` option instead of `useClass`/`useValue`.

```ts
@Service()
export class Cart {
  private http = inject(HttpClient);
}
```

It doesn't make code run faster, but it makes the tree-shakable, auto-provided setup the default. That's also what `injectAsync()` needs for lazy loading.

## 354: How would you diagnose a slow app that uses NgRx Store heavily?

- Check selectors: are they memoized with `createSelector`, or do they return new objects every time?
- Look for components selecting large slices and re-rendering on every state change
- Check effects that dispatch many actions in a row, each causing a change detection run
- Use the Redux DevTools to see action frequency
- Consider `selectSignal()` or SignalStore so components read signals

Often the fix is narrower selectors and OnPush components that receive only the data they show.

## 355: Why can a selector that returns a new array on every call hurt performance?

```ts
export const selectActive = createSelector(selectUsers, (users) =>
  users.filter((u) => u.active),
);
```

This one is fine because `createSelector` memoizes on `selectUsers`. But a selector without memoization, or one whose input changes on every action, returns a new array each time. Components using it get a new reference, OnPush sees a change and everything below re-renders.

Make sure selector inputs are stable and use `createSelector` for any derived data.

## 356: How do you avoid re-rendering a whole page when a global store changes?

- Select narrow pieces of state in each component, not the whole state
- Use signals (`selectSignal()` or SignalStore) so only views reading changed signals refresh
- Keep entity state normalized
- Don't pass the whole store slice down through inputs
- Use `computed()` with custom `equal` when a selector often returns equivalent data

## 357: How do you make a real-time trading or monitoring screen fast in Angular?

- Receive updates in batches (every 100-250 ms), not per message
- Keep data in per-item signals or a map, so one price change updates one cell
- Use OnPush and zoneless, so no other part of the page is checked
- Use virtual scrolling for long instrument lists
- Avoid animations on every cell update, or use cheap CSS transitions
- Move heavy calculations (aggregations, indicators) to a web worker
- Measure the time from message to paint with `performance.mark()`

## 358: How would you use per-item signals for a large list with frequent updates?

```ts
interface Row {
  id: string;
  price: WritableSignal<number>;
}

rows = signal<Row[]>([]);
private byId = new Map<string, Row>();

applyTick(id: string, price: number) {
  this.byId.get(id)?.price.set(price);
}
```

```html
@for (row of rows(); track row.id) {
<td>{{ row.price() }}</td>
}
```

The `rows` array never changes on a price tick, so `@for` doesn't diff anything. Only the cell that reads the changed price signal is refreshed.

## 359: What are the trade-offs of per-item signals?

Pros: very precise updates, no array diffing on value changes, cheap ticks.

Cons:

- More memory (one signal per item or field)
- Harder to serialize, compare and test state
- Mixing plain objects and signals can be confusing
- Libraries and stores that expect plain data may not fit

Use it only for hot paths with frequent updates. For most screens, immutable arrays with `track` and OnPush rows are fast enough.

## 360: How do you design a component library to be fast by default?

- OnPush (default since v22) and signal inputs everywhere
- No work in `ngDoCheck` or `*Checked` hooks
- Standalone components with secondary entry points so apps import only what they use
- No heavy dependencies at the top level, lazy load them inside the components that need them
- No global listeners unless needed, and always clean them up
- Works zoneless, uses `afterNextRender` for DOM work
- SSR safe, no direct `window` access

## 361: What are secondary entry points and why do they matter?

A library with secondary entry points exposes separate import paths, like `@my/lib/button` and `@my/lib/table`. Each one is built as its own module.

```ts
import { Button } from "@my/lib/button";
```

Apps that only use the button don't pull in the table code, even if tree-shaking would have trouble with a single big entry. Angular Material and CDK use this pattern. You set it up with ng-packagr by adding `ng-package.json` files in subfolders.

## 362: How does the CDK virtual scroll work internally?

The viewport listens to scroll events (outside Angular's zone) and asks its scroll strategy which range of items should be rendered. `*cdkVirtualFor` then renders only that range, reusing views from a template cache when items scroll out and in. A spacer element sets the total scroll height based on item count and size.

The fixed-size strategy calculates the range with simple math. The rendered block is moved with a CSS `transform` so the visible items line up with the scroll position.

## 363: How do you write a custom virtual scroll strategy?

Implement `VirtualScrollStrategy` and provide it with `VIRTUAL_SCROLL_STRATEGY`:

```ts
export class GroupedStrategy implements VirtualScrollStrategy {
  scrolledIndexChange = new Subject<number>();
  private viewport?: CdkVirtualScrollViewport;

  attach(viewport: CdkVirtualScrollViewport) {
    this.viewport = viewport;
    this.update();
  }
  detach() {
    this.viewport = undefined;
  }
  onContentScrolled() {
    this.update();
  }
  onDataLengthChanged() {
    this.update();
  }
  onContentRendered() {}
  onRenderedOffsetChanged() {}
  scrollToIndex(index: number, behavior: ScrollBehavior) {
    /* ... */
  }

  private update() {
    // use precomputed row offsets to find the range,
    // then call viewport.setRenderedRange() and setRenderedContentOffset()
  }
}
```

It's useful for lists with group headers or rows of known but different heights.

## 364: How would you handle a list with variable and unknown item heights?

Options:

- Estimate heights and correct them after rendering, measuring with `ResizeObserver` (what libraries like TanStack Virtual do)
- Use `content-visibility: auto` with an estimated `contain-intrinsic-size` and render all rows, if the count isn't huge
- Paginate or use "load more" instead
- Use the experimental CDK autosize strategy

Each estimate-and-correct approach can cause small scroll jumps, so test on real data.

## 365: How do you measure the real benefit of OnPush or zoneless before migrating a whole app?

- Pick a slow, representative page
- Record a baseline: Angular DevTools profiler (number of cycles and time per cycle), Chrome traces for key interactions, INP from a test
- Migrate only that page (OnPush components, signals)
- Record again under the same conditions
- For zoneless, try it in a branch with `provideZonelessChangeDetection()` and run the e2e tests

Concrete numbers from one page make it much easier to justify the full migration.

## 366: What is the risk of using OnPush everywhere with mutable data from a legacy service?

A legacy service that mutates shared objects in place (for example `this.state.user.name = "x"`) won't trigger updates in OnPush components because the reference doesn't change. Some views will show stale data, and bugs can be random depending on what else triggers checks.

Before switching, wrap that state in signals or make updates immutable. In Angular 22, the migration keeps such components on `Eager` so you can move them deliberately.

## 367: How do you handle third-party components that don't work with OnPush or zoneless?

- Check if a newer version supports signals or zoneless
- Wrap the component in your own component that manages its inputs and calls `markForCheck()` or `detectChanges()` when its internal state changes
- Keep that wrapper `Eager` while the rest of the app is OnPush
- In a zoneless app, if the library updates state in its own callbacks, call `ChangeDetectorRef.markForCheck()` in those callbacks
- As a last resort, replace the library

## 368: How do you keep an Angular Elements (web components) build small?

Angular Elements bundles the Angular runtime with your component. For a single widget, that can be large compared to the widget itself.

- Go zoneless to drop Zone.js
- Use only standalone components and avoid `@angular/animations`
- Share one Angular runtime if you embed several widgets on the same page (one bundle registering all elements)
- Lazy load heavy parts with `@defer` inside the element

## 369: How does Module Federation or Native Federation affect Angular performance?

Micro frontends load separate builds at runtime. The main costs are:

- Duplicate copies of Angular and libraries if sharing isn't set up correctly
- Extra network requests for remote entry files before the remote can load
- Version mismatches forcing separate copies

Configure shared dependencies as singletons, keep versions aligned, preload remotes the user will likely need, and monitor the total JS per page. Native Federation works with the esbuild builder.

## 370: How would you reduce the cost of a large monolithic Angular app's startup?

1. Measure: initial total, startup long tasks, app initializers.
2. Move every route except the landing page to lazy loading.
3. Remove root providers and initializers that aren't needed at startup.
4. `@defer` heavy parts of the landing page.
5. Remove or replace heavy dependencies found in the bundle analyzer.
6. Add SSR or prerender for public pages.
7. Add budgets to keep it from growing back.

## 371: How do you deal with a slow first change detection run?

The first render creates every component on the screen. If it's slow:

- Render less at first: paginate, `@defer` below-the-fold content, virtual scroll
- Avoid heavy constructors and `ngOnInit` work in many components
- Avoid deep nesting of tiny components inside huge lists
- Check for expensive template expressions evaluated per item

A Performance trace with Angular profiling shows which component templates take the most time during creation.

## 372: What is the cost of many small components versus inline templates?

Each component has some overhead: an `LView`, a host element, an injector lookup, lifecycle hooks. For most UIs this is tiny. But in a list of 10,000 cells, wrapping each cell in its own component adds measurable cost.

For hot paths with huge counts, inline the markup into the row template or use `ng-template` instead of a component per cell. Elsewhere, prefer small components for clarity and better OnPush skipping.

## 373: How do you optimize directives applied to many elements?

A directive on every row runs its constructor, host bindings and hooks for each element.

- Keep host bindings simple and based on signals
- Don't use `ngDoCheck`
- Share one global listener or observer (like one `IntersectionObserver` or `ResizeObserver` for all instances, managed by a service) instead of one per element
- Avoid injecting heavy services per instance

## 374: How do you share one IntersectionObserver across many directive instances?

```ts
@Injectable({ providedIn: "root" })
export class VisibilityService {
  private callbacks = new Map<Element, (visible: boolean) => void>();
  private observer =
    typeof IntersectionObserver !== "undefined"
      ? new IntersectionObserver((entries) => {
          for (const e of entries)
            this.callbacks.get(e.target)?.(e.isIntersecting);
        })
      : null;

  observe(el: Element, cb: (visible: boolean) => void) {
    this.callbacks.set(el, cb);
    this.observer?.observe(el);
  }

  unobserve(el: Element) {
    this.callbacks.delete(el);
    this.observer?.unobserve(el);
  }
}
```

Each directive calls `observe()` in `afterNextRender()` and `unobserve()` on destroy. One observer is much cheaper than thousands. The `typeof` check keeps it SSR safe.

## 375: How do you optimize the ResizeObserver usage in a component?

- Use one observer per component, or one shared across components
- Don't write to the DOM synchronously in the callback for the same elements, it can cause loops ("ResizeObserver loop" errors)
- Update a signal and let Angular render, or batch work with `requestAnimationFrame`
- Disconnect on destroy

```ts
private destroyRef = inject(DestroyRef);
width = signal(0);

constructor() {
  afterNextRender(() => {
    const ro = new ResizeObserver(([entry]) => this.width.set(entry.contentRect.width));
    ro.observe(this.host.nativeElement);
    this.destroyRef.onDestroy(() => ro.disconnect());
  });
}
```

## 376: How do you design an Angular app to work well on low-end Android devices?

- Keep JS small, these devices are slow at parsing and executing it
- Use SSR or prerendering and incremental hydration
- Avoid big animations and heavy CSS effects (blur, shadows on many elements)
- Use pagination or virtual scroll
- Zoneless and OnPush to reduce CPU per interaction
- Test on a real mid-range device and with 6x CPU throttling

## 377: How does the browser cache interact with Angular deployments?

Hashed files can be cached forever. The risk is `index.html`: if it's cached, users get old file names. If old files were deleted from the server, lazy chunk requests fail with a 404 ("ChunkLoadError" or "Failed to fetch dynamically imported module").

Serve `index.html` with `no-cache`, and keep old chunks available for a while after a deploy (or at least until users reload). With a service worker, handle `SwUpdate` events so users move to the new version.

## 378: How do you handle chunk load errors after a deploy?

Users with an open tab may request chunks that no longer exist. Handle it:

```ts
provideRouter(
  routes,
  withNavigationErrorHandler((error) => {
    if (String(error.error?.message).includes("dynamically imported module")) {
      location.reload();
    }
  }),
);
```

Better still: keep old assets for a few days after a deploy, so old tabs keep working. Avoid reload loops by remembering that you already reloaded once (for example in `sessionStorage`).

## 379: How does the service worker's navigation handling affect performance?

The Angular service worker serves `index.html` from cache for navigation requests, so the app shell loads instantly on repeat visits, even offline. It checks for a new version in the background.

The trade-off: users run the cached version until the new one is activated. You need an update strategy (prompt, or activate on next navigation) so they don't stay on old code for too long. `navigationRequestStrategy: "freshness"` lets you prefer the network for navigations if that fits better.

## 380: How do you decide between performance and freshness strategies in dataGroups?

- `performance`: cache first. Fast, but data can be up to `maxAge` old. Good for reference data, product catalogs, images metadata.
- `freshness`: network first, cache fallback after `timeout`. Good for user data, orders, anything where stale data causes problems.

You can also use `cacheOpaqueResponses` and `refreshAhead` for more control. Measure how often users would see stale data and whether that's acceptable for each API.

## 381: How do you prevent a service worker from serving stale API data after logout?

The service worker caches by URL, not by user. If two users share a device, cached responses from one may show to the other.

- Don't cache user-specific endpoints in `dataGroups`, or
- Clear caches on logout (`caches.keys()` then `caches.delete()`), and
- Use URLs that include a user or session identifier if you must cache per user

This is both a security and a correctness concern.

## 382: How would you speed up the TypeScript type checking part of builds in a large app?

- Turn on `incremental` in `tsconfig` and keep the CLI cache
- Avoid huge union types and very deep generic types that slow down the type checker
- Split the app into libraries (in an Nx workspace) so only changed parts are rebuilt and checked
- Keep `strictTemplates` on, but watch for templates with very complex expressions
- Use the latest TypeScript supported by your Angular version (Angular 22 requires TypeScript 6.0 or later)

## 383: What is the cost of strictTemplates and should you turn it off for speed?

`strictTemplates` makes the compiler type check templates fully, which adds some build time. But it catches real bugs, like passing the wrong type to an input. In Angular 22, `ng update` even adds it to projects that don't have it.

The build time cost is usually small compared to the rest of the build. Don't turn it off for speed, look at other ways to make builds faster first.

## 384: How does an Nx monorepo help with build performance in Angular?

- **Affected commands**: build and test only projects changed by a commit
- **Computation caching**: reuse results for unchanged projects, locally and in CI
- **Buildable libraries**: compile libraries once and reuse them
- **Task parallelism**: run builds and tests in parallel

It doesn't change the runtime performance of the app, but it can turn a 30-minute CI pipeline into a few minutes.

## 385: How would you set up a performance regression test for a key interaction?

Use Playwright or Puppeteer to record a Chrome trace or measure INP for the interaction:

```ts
test("filter interaction is fast", async ({ page }) => {
  await page.goto("/products");
  const duration = await page.evaluate(async () => {
    const input = document.querySelector<HTMLInputElement>("#filter")!;
    const start = performance.now();
    input.value = "shoe";
    input.dispatchEvent(new Event("input", { bubbles: true }));
    await new Promise((r) => requestAnimationFrame(() => setTimeout(r)));
    return performance.now() - start;
  });
  expect(duration).toBeLessThan(150);
});
```

Run it on a production build with CPU throttling via the Chrome DevTools Protocol, and track the numbers over time rather than relying on one strict threshold.

## 386: How do you throttle the CPU in automated performance tests?

With Playwright and Chromium, use a CDP session:

```ts
const client = await page.context().newCDPSession(page);
await client.send("Emulation.setCPUThrottlingRate", { rate: 4 });
```

Combine it with network throttling (`Network.emulateNetworkConditions`). Lighthouse CI does this for you with its mobile presets. Keep the setup the same across runs so results are comparable.

## 387: How does Angular's SSR stream the response?

Angular's SSR waits until the app is stable and then returns the full HTML. It doesn't stream partial HTML as components render. The response is returned as a web standard `Response`, and the Node adapter writes it to the Node response.

To get content to users faster, reduce what blocks stability: slow API calls on the server, waiting for data that could be loaded on the client, and content that can be put in `@defer` blocks (only the placeholder is rendered on the server).

## 388: What is the effect of slow server-side API calls on SSR and how do you limit it?

The server waits for all pending HTTP calls before rendering is complete. One slow API call delays the whole page for every user.

- Set timeouts for server-side requests (for example with an interceptor using `timeout()` only on the server)
- Load slow, non-critical data only on the client (in `@defer` blocks or `afterNextRender`)
- Cache API responses on the server
- Call internal APIs directly over the private network instead of through public URLs

## 389: How do you add a timeout only for server-side HTTP requests?

```ts
export const serverTimeoutInterceptor: HttpInterceptorFn = (req, next) => {
  if (isPlatformServer(inject(PLATFORM_ID))) {
    return next(req).pipe(timeout(2000));
  }
  return next(req);
};
```

If the call times out, handle the error so the page still renders with a fallback, and let the client try again after hydration.

## 390: Why should SSR call APIs through internal URLs?

When the Angular server calls `https://api.example.com`, the request may go out to the internet, through the CDN and load balancer, and back in. Calling `http://api.internal:8080` directly is much faster and cheaper.

You can rewrite URLs in a server-only interceptor. Be careful that the transfer cache key stays the same on server and client, since it's based on the request URL. Test that the browser doesn't send the requests again after hydration.

## 391: How does the HTTP transfer cache build its cache keys?

The key is built from the request method, URL, params and response type (and selected headers if configured). On the client, a request with the same values finds the cached response during hydration.

If the client builds the URL differently (for example absolute on the server, relative on the client, or params in a different order), the keys don't match and the request is sent again. Keep request building the same on both sides.

## 392: When does the HTTP transfer cache stop being used on the client?

The cached responses are used only until the app becomes stable after hydration. After that, requests go to the network as normal. This makes sure later requests (after user actions) get fresh data.

So a component created later, for example after a navigation, won't use the cached response even if the URL matches.

## 393: How do you profile the SSR server's rendering?

- Run Node with `--cpu-prof` or use `node --inspect` and the Chrome DevTools profiler
- Measure render time per route in your server handler with `performance.now()`
- Look for slow API calls, heavy synchronous work in constructors and large templates
- Use clinic.js or 0x for flame graphs under load

Then optimize like on the client: less work per render, fewer API calls, caching, and prerendering for hot routes.

## 394: What is the risk of rendering huge pages on the server?

- Long CPU time per request blocks the event loop
- Large HTML takes longer to send and parse
- Big transfer state and hydration data
- High memory per request under concurrency

Limit page size: paginate on the server, defer below-the-fold content, and render only the first part of long lists on the server.

## 395: How do you keep hydration working with a third-party library that changes the DOM?

- Initialize the library in `afterNextRender()`, after hydration, on an element Angular doesn't manage (an empty container)
- Keep Angular-rendered content and library-managed content separate
- If the component itself is incompatible, add `ngSkipHydration` to it, which costs a client re-render of that subtree only
- Look for an Angular-native alternative

## 396: How do you speed up an app that uses Angular Material heavily?

- Import only the Material components you use (standalone imports)
- Avoid big shared modules re-exporting all Material components
- Use `@defer` for dialogs, date pickers and other heavy pieces that aren't needed at first
- Use CDK virtual scrolling for long lists and `mat-table` with pagination
- Check theme CSS size, include only the component styles you use where possible

## 397: How do you reduce the cost of mat-table or other complex tables?

- Server-side pagination and sorting
- `trackBy` on the data source rows (`MatTable` supports `trackBy`)
- OnPush cells, plain text where possible
- Avoid custom components per cell for simple values
- Use `content-visibility` or virtual scrolling (with care, tables and virtual scroll need special handling for sticky headers)

## 398: What is the cost of change detection in deeply nested OnPush trees with markForCheck()?

`markForCheck()` marks every ancestor up to the root. In a deep tree, the next run refreshes the whole path, evaluating each ancestor's bindings. If many leaf components call it often (for example on every socket message), much of the tree's top is refreshed over and over.

Switching those leaves to signals removes the ancestor refresh. Batching the updates also helps.

## 399: How would you build a chart component that updates many times per second?

- Render with canvas or WebGL instead of SVG/DOM for many points
- Keep the chart library outside Angular's templates: create it in `afterNextRender()`, update it in an `effect()` or `afterRenderEffect()` when data signals change
- Throttle updates to animation frames
- Don't pass huge arrays through inputs on every tick, push only new points
- In Zone.js apps, run the library outside Angular

The component's own template stays tiny, so Angular does almost no work per update.

## 400: How do you decide if a performance optimization is worth it?

Ask:

- What metric does it improve, and by how much (measured, not guessed)?
- How many users or pages does it affect?
- How much complexity does it add to the code?
- Does it make the code harder to change later?

Big wins with small changes (lazy loading, `track`, image `priority`, OnPush) are almost always worth it. Complex tricks (per-item signals, custom strategies, detached views) are worth it only for proven hot paths.

## 401: Scenario: a product list page freezes for 2 seconds when filters change. How do you approach it?

1. Record a trace with CPU throttling while changing a filter.
2. Check where the time goes: the filter function, change detection, or DOM work (layout, paint).
3. Typical findings and fixes:
   - Filtering 20,000 items in a method called from the template: move it to `computed()` and debounce the filter input
   - Rendering all results: paginate or virtual scroll
   - `@for` without a stable key: track by id
   - Each row has heavy components: simplify rows, defer menus and tooltips
4. Measure again and compare.

## 402: Scenario: the app gets slower the longer a user keeps it open. What do you check?

That's almost always a memory leak or growing work:

- Heap snapshots before and after repeating a navigation several times
- Look for destroyed component instances still in memory and check their retainers
- Look for growing arrays or maps in services (caches without limits, event logs)
- Look for intervals and subscriptions that keep adding up
- Check for event listeners added on every navigation and never removed

Also check whether change detection runs get longer over time, which points to a growing DOM or more and more active components.

## 403: Scenario: Lighthouse shows a good score but users complain about slowness. Why?

Lighthouse is a lab test of one page load with a simulated device. Users may be:

- On slower devices or networks than the test profile
- Slow during interactions (INP), which a page load test barely covers
- Hitting slow pages that aren't tested
- Experiencing slow API responses that are fast in the test environment
- Long sessions with memory growth

Collect field data with `web-vitals` and LoAF, group by page and device, and look at p75 and p95 values instead of averages.

## 404: Scenario: after enabling SSR, TTFB increased a lot. What can you do?

- Check what the server waits for: slow API calls are the most common cause
- Call APIs over internal URLs and add server-side timeouts
- Move non-critical data loading to the client
- Prerender static routes
- Cache rendered HTML on a CDN for public pages
- Check the server has enough CPU and runs several processes

TTFB going up a little is normal with SSR, as long as FCP and LCP improve overall.

## 405: Scenario: a dashboard sends 40 API requests on load. How do you improve it?

- Find duplicate requests (same URL from several widgets) and share them through a service or `httpResource` in a root service
- Combine related data into one backend endpoint (a BFF)
- Defer widgets below the fold so their requests start later
- Cache stable data (user settings, reference data)
- Use HTTP/2 or HTTP/3 so parallel requests share one connection

Check the network waterfall to make sure requests run in parallel and not in a chain.

## 406: Scenario: a page has a high CLS score caused by an ad or banner loaded later. What do you do?

- Reserve fixed space for it with CSS (`min-height` or `aspect-ratio`)
- Render a placeholder of the right size in `@placeholder` if it's deferred
- Don't insert content above existing content after load, insert below or in a reserved slot
- For cookie banners, use an overlay (`position: fixed`) instead of pushing content down

## 407: Scenario: a hydrated page re-renders completely after loading. How do you find the cause?

1. Open the console in dev mode and look for hydration errors (NG05xx) and the hydration stats message.
2. Check if a CDN or proxy strips HTML comments.
3. Look for components that use `innerHTML` or touch the DOM directly.
4. Check for invalid HTML nesting in templates (like `<a>` in `<a>`, `<div>` in `<p>`).
5. Check if `provideClientHydration()` is actually in the client config.

Fix the cause instead of adding `ngSkipHydration` everywhere.

## 408: Scenario: the initial bundle grew by 300 KB after a small feature was merged. How do you find out why?

1. Build both versions with `--stats-json`.
2. Compare them in the esbuild analyzer, or diff the module lists.
3. Find the new modules in the initial chunk and their import chain.
4. Usually a new static import of a big library in a file used at startup, or a component added to the root route.
5. Move it behind `@defer`, a lazy route or a dynamic `import()`.

Then add or lower budgets so this gets caught in CI next time.

## 409: Scenario: a form with 200 fields lags on every keystroke. What would you check?

- Is the form component and all field components OnPush?
- Are there `valueChanges` subscriptions on the whole form that recalculate everything?
- Are validators expensive or async without debouncing?
- Do templates call methods for each field (like `getError(field)`)?
- Is the whole form re-rendered because of a parent state change on each keystroke?

Fixes: `updateOn: "blur"` where possible, `computed()` for derived values, split the form into sections and defer hidden sections, or move to Signal Forms where field state is tracked per field.

## 410: Scenario: an app works fine on desktop but scrolling is janky on mobile. What can cause it?

- Heavy scroll listeners triggering change detection (with Zone.js)
- Non-passive touch or wheel listeners
- Sticky elements or parallax done with JS instead of CSS
- Expensive CSS (box shadows, filters, `backdrop-filter`) on many elements
- Large images decoded during scroll
- Long lists without virtual scrolling or `content-visibility`

Record a trace on a real device with remote debugging and look at the frames during scrolling.

## 411: Scenario: users report the app takes long to show anything after a deploy. Why might that be?

After a deploy, all hashed files are new, so returning users must download everything again. If the bundle is big, the first visit after each deploy is slow.

- Reduce bundle size and split vendor code that rarely changes into stable chunks
- Make sure compression and CDN caching work for the new files
- With a service worker, new files are downloaded in the background, but users only get them on next load
- Deploy less often in big batches, or accept it and focus on bundle size

## 412: Scenario: Angular DevTools shows change detection running 60 times per second while the app is idle. What do you look for?

Something triggers it on every frame:

- A `requestAnimationFrame` loop or animation inside the Angular zone (with Zone.js)
- An `setInterval` with a short delay
- A third-party library polling or animating
- An effect or `afterEveryRender` that writes a signal and triggers another run

Use the Performance panel to see which callbacks run, then move them outside Angular, stop them when not needed, or fix the loop.

## 413: Scenario: a page with an infinite scroll feed becomes slow after loading many pages. How do you fix it?

The DOM and the list keep growing. Options:

- Use virtual scrolling so only visible items are in the DOM
- Remove items far above the viewport and keep their height with a spacer
- Use `content-visibility: auto` on feed items
- Keep each feed item light (defer comments, video players until visible)
- Make sure images below the fold are lazy loaded and old media is released

## 414: Scenario: a lazy route takes 3 seconds to open on 3G. How do you make it feel faster?

- Preload the route (on idle, or when the link is visible or hovered)
- Make the route chunk smaller (defer heavy parts, remove shared heavy imports)
- Start its data request in parallel with the chunk download (resolver or route-level loading)
- Show the new page shell right away, with skeletons for data
- Use the service worker to cache chunks for returning users

## 415: Scenario: memory keeps growing in a long-running kiosk app. How would you investigate?

- Use heap snapshots and the allocation timeline over a long period
- Look for caches without limits, logs kept in memory and growing signal arrays
- Check that intervals, socket listeners and observers are cleaned up on navigation
- Check third-party libraries (maps, video players) for missing `destroy()` calls
- Look at DOM node count over time

As a safety net, some kiosk apps reload themselves during quiet periods, but fix the leaks first.

## 416: Scenario: an Angular app embedded in an iframe on a customer site is slow to start. What would you do?

- Make the embedded app as small as possible (separate lightweight entry if needed)
- Lazy load everything not needed for the first view
- Use `loading="lazy"` on the iframe if it's below the fold
- Prerender the first view
- Preconnect from the host page to your origin if you control the embed snippet
- Check that caching works in the iframe context (third-party storage and cookie partitioning can affect it)

## 417: Scenario: a page with a large reactive form takes long to open. What can cause it and how to fix it?

Creating hundreds of `FormControl`s with validators, rendering all fields at once and setting initial values that trigger many `valueChanges` all take time.

- Build the form once, not on every navigation, when possible
- Use `{ emitEvent: false }` when patching initial values
- Defer hidden sections and tabs
- Use virtual scrolling for repeating rows (like line items)
- Consider Signal Forms, which create field state lazily

## 418: Scenario: switching tabs in a tab component is slow. What would you check?

- Are all tabs rendered at once and kept in the DOM? Use lazy tab content (`ng-template` or `@defer`)
- Is each tab destroyed and recreated on every switch? If tabs are expensive to create, keep them alive and hide them instead
- Does switching tabs trigger data reloading every time? Cache the data
- Are there heavy components (charts) resizing on show? Throttle resize work

The right choice between "destroy" and "keep alive" depends on memory vs. switch speed.

## 419: Scenario: an app with Zone.js has a Google Maps component and every map drag makes the whole app slow. Why and how do you fix it?

The map library fires many events (mousemove, animation frames) during a drag. Zone.js sees each one and runs change detection for the whole app.

Fix it by creating the map outside Angular:

```ts
afterNextRender(() => {
  this.zone.runOutsideAngular(() => {
    this.map = new google.maps.Map(this.el().nativeElement, options);
    this.map.addListener("idle", () => this.bounds.set(this.map.getBounds()));
  });
});
```

Update signals only for events you care about. Going zoneless fixes this kind of problem for the whole app.

## 420: Scenario: you need to show 100 charts on one page. How would you design it?

- Render charts only when they scroll into view (`@defer (on viewport)` or an `IntersectionObserver`)
- Use canvas-based charts, not SVG with thousands of nodes
- Load the chart library once, lazily
- Fetch data in batches or as charts become visible
- Destroy or pause charts far off screen if memory is a problem
- Consider small static images (sparklines rendered on the server) for overview, with interactive charts on click

## 421: How do you think about the trade-off between SSR and a fully static SPA on a CDN?

Static SPA:

- Cheapest and simplest to host, very low TTFB
- Slow first content on slow devices, worse SEO
- Fine for apps behind login

SSR:

- Faster first content, better SEO and link previews
- Needs servers, monitoring and scaling
- More complex code (browser-only APIs, hydration)

Many teams prerender public pages and serve the app part as a SPA, getting most of the benefit without full SSR servers.

## 422: Why might going zoneless not make your app noticeably faster?

If the app already used OnPush everywhere and had few noisy async events, Zone.js wasn't causing much extra work. The gains then are mostly the smaller bundle (no Zone.js) and simpler debugging.

The big wins come in apps where Zone.js triggered many useless change detection runs (timers, polling, third-party libraries) or where many components were Eager. Measure before promising big speedups.

## 423: What is the risk of premature optimization in Angular projects?

Spending time and adding complexity where it doesn't matter: detached change detectors, custom virtual scroll strategies, per-item signals, manual caching. The code gets harder to understand and change, and bugs creep in (stale views, cache inconsistencies).

Start with the defaults that are cheap and widely useful (lazy routes, OnPush, signals, `track`, `NgOptimizedImage`), measure, and only go further for proven problems.

## 424: How do you build a performance culture in an Angular team?

- Budgets in CI so regressions fail builds
- Field data dashboards for Core Web Vitals per page
- Performance review as part of code review for risky changes (new dependencies, big lists)
- Shared guidelines: OnPush, signals, `track`, lazy loading, image rules
- Regular updates of Angular to get new improvements
- Small performance retros when a regression gets to production

## 425: How would you explain the performance difference between Angular's old and new reactivity models to a non-Angular developer?

Old model (Zone.js): Angular got notified "something async happened, maybe something changed", and then checked every component's bindings to find out. Simple but wasteful.

New model (signals): every piece of state knows which parts of the UI use it. When it changes, only those parts are updated. Angular doesn't need to guess or check everything.

It's like checking every room in a house when you hear a noise versus having a sensor in each room tell you exactly which door opened.

## 426: How does @defer decide when to load dependencies when there are several triggers?

Triggers are combined with OR: the block loads when any trigger fires first. `prefetch` triggers are separate and only download the code, they don't render.

```html
@defer (on viewport; on timer(5s); prefetch on idle) { ... }
```

This loads when the block becomes visible or after 5 seconds, whichever is first, and downloads the code early when the browser is idle. You can also add a `when` condition. It's a one-time trigger: once it's true and the block has loaded, the block stays even if the condition becomes false again.

## 427: What happens if a @defer block's chunk fails to load?

Angular shows the `@error` block if there is one. If not, the block stays on the placeholder. It doesn't retry automatically.

For important content, add an `@error` block with a retry option (for example a button that toggles a `when` condition in a new `@defer` instance) or reload the page. Monitor chunk load errors in production, they're often caused by deploys deleting old chunks.

## 428: How do you test the performance effect of @defer in unit tests?

You don't test speed in unit tests, but you can test that blocks behave correctly. `TestBed` supports controlling defer blocks:

```ts
TestBed.configureTestingModule({
  deferBlockBehavior: DeferBlockBehavior.Manual,
});

const fixture = TestBed.createComponent(Page);
const [block] = await fixture.getDeferBlocks();
await block.render(DeferBlockState.Complete);
```

This lets you check placeholder, loading and complete states. Use e2e tests and bundle analysis to verify the performance side.

## 429: How would you design caching of reference data across the whole app?

- A root service holding a signal or resource per dataset (countries, currencies, settings)
- Load on first use, not at startup
- Cache in memory and optionally in `localStorage` or IndexedDB with a version or timestamp
- Refresh in the background (stale-while-revalidate) when the cache is old
- Use HTTP caching headers (`ETag`, `Cache-Control`) so refreshes are cheap

```ts
@Service()
export class Countries {
  readonly list = httpResource<Country[]>(() => "/api/countries");
}
```

Every component reads `countries.list.value()` and only one request is made.

## 430: How do you use ETags with Angular HttpClient?

The browser handles `ETag` and `If-None-Match` for you when the server sends them and the response is cacheable. On a repeat request, the browser sends `If-None-Match` and the server can answer `304 Not Modified` with no body.

`HttpClient` sees the cached `200` response, so your code doesn't change. Make sure the server sends `ETag` and an appropriate `Cache-Control` (like `no-cache`, which means "revalidate every time", not "don't cache").

## 431: How does the Fetch backend in Angular 22 affect caching?

`FetchBackend` uses the browser's `fetch`, which goes through the same HTTP cache as XHR. You can also pass fetch options through `HttpClient` request options, for example `cache`, `priority` and `keepalive` (supported when using the fetch backend).

```ts
this.http.get("/api/feed", { priority: "low", cache: "no-store" });
```

`priority: "low"` is useful for background requests that shouldn't compete with important ones.

## 432: How do you use fetch priority to improve LCP?

- Mark the LCP image with `priority` in `NgOptimizedImage` (adds `fetchpriority="high"`)
- Lower the priority of non-critical images and requests (`fetchpriority="low"`, or `priority: "low"` in `HttpClient` with the fetch backend)
- Don't preload too many things, it dilutes priority

The browser then gives bandwidth to what matters for the first view.

## 433: How do you avoid the "everything is critical" problem when preloading?

Every preload competes for bandwidth with the critical path. Common mistakes:

- `PreloadAllModules` on a big app starts downloading megabytes right after startup, competing with images and API calls
- Many `<link rel="preload">` tags in `index.html`
- Many `priority` images

Use selective preloading, delay route preloading until after the first page is loaded, and limit high priority resources to one or two per page.

## 434: How would you delay route preloading until the app is idle?

```ts
@Injectable({ providedIn: "root" })
export class IdlePreloading implements PreloadingStrategy {
  preload(route: Route, load: () => Observable<unknown>) {
    if (!route.data?.["preload"]) return of(null);
    return new Observable<void>((sub) => {
      const id = requestIdleCallback(() => {
        sub.next();
        sub.complete();
      });
      return () => cancelIdleCallback(id);
    }).pipe(switchMap(() => load()));
  }
}
```

`requestIdleCallback` isn't available in every browser, so add a `setTimeout` fallback in real code. This keeps preloading from competing with the first page.

## 435: How do you measure the effect of preloading on users?

- Track route navigation time (start to first render of the new page) with `performance.measure()` in production
- Compare the share of navigations where the chunk was already loaded
- Watch data use and initial page metrics (LCP, TBT) to make sure preloading doesn't hurt the first page
- A/B test strategies on a share of users if traffic allows it

## 436: What is speculative loading with the Speculation Rules API and can Angular use it?

The Speculation Rules API lets a page tell the browser to prefetch or prerender other pages:

```html
<script type="speculationrules">
  {
    "prefetch": [
      {
        "source": "document",
        "where": { "href_matches": "/products/*" },
        "eagerness": "moderate"
      }
    ]
  }
</script>
```

It's designed for multi-page navigation. In an Angular SPA, client-side navigations don't load new documents, so it helps mostly with full page loads, like links from a marketing site into the app, or between separate Angular apps. It's supported in Chromium-based browsers.

## 437: How do you keep an Angular app fast as it grows to hundreds of routes?

- Every feature is a lazy route with its own providers
- No feature imports another feature directly, shared code lives in small libraries
- Budgets for initial and per-chunk size
- Lint rules that block importing heavy libraries in shared or core code
- Selective preloading
- Regular bundle analysis and dependency cleanup

Nx module boundary rules can enforce the "no direct feature imports" rule.

## 438: How do you think about performance when choosing a state management approach?

- **Signals in services**: very fast, fine-grained updates, little code. Good default
- **NgRx SignalStore**: structure plus signals, fine-grained updates
- **NgRx Store (Redux)**: predictable, great tooling, but more boilerplate and you must keep selectors memoized and narrow
- **RxJS-only stores**: flexible, but needs care to avoid extra subscriptions and work

Performance problems usually come from how state is shaped and read (big objects passed down, unmemoized selectors), not from the library itself.

## 439: How does the router's paramsInheritanceStrategy change in Angular 22 matter?

In Angular 22 the default `paramsInheritanceStrategy` changed from `"emptyOnly"` to `"always"`. Child routes now inherit params from all parent routes.

For performance, this matters if components react to all route params: they may now see more params and recompute or reload data when a parent param changes. Check components that load data based on the full params object, and make them react only to the params they need.

## 440: How do you avoid reloading data when the user navigates back and forth?

- Cache data in a service keyed by id, and show cached data instantly
- Refresh in the background if the data can change
- Use a `RouteReuseStrategy` for expensive list pages
- Use `withInMemoryScrolling` to restore scroll position

```ts
private cache = new Map<string, Product>();

load(id: string) {
  const hit = this.cache.get(id);
  if (hit) return of(hit);
  return this.http.get<Product>(`/api/products/${id}`).pipe(tap((p) => this.cache.set(id, p)));
}
```

## 441: How do Angular's built-in animations (animate.enter and animate.leave) work, and why are they cheaper?

`animate.enter` and `animate.leave` add CSS classes when an element is added or before it's removed. The browser runs the CSS animation or transition, and for leave, Angular waits for the animation to finish before removing the element.

```html
@if (toast()) {
<div class="toast" animate.enter="fade-in" animate.leave="fade-out">
  {{ toast() }}
</div>
}
```

There is no animation engine in JavaScript and no extra package, so they cost almost nothing in bundle size. With `transform` and `opacity`, the browser can run them off the main thread.

## 442: What does provideAnimationsAsync do and is it still relevant?

`provideAnimationsAsync()` loads the legacy `@angular/animations` code lazily, after the app starts, instead of in the initial bundle. It was the recommended way to use Material and other libraries that depended on the animations package.

It's still relevant for apps that use the legacy animation DSL (`trigger`, `state`, `transition`), which was deprecated in Angular 20.2. For new code, use `animate.enter`/`animate.leave` or plain CSS, and you won't need the animations package at all.

## 443: How do you find out what is really in your polyfills and main chunks?

- Build with source maps and run `source-map-explorer` on each file
- Use `stats.json` in the esbuild analyzer and click into each chunk
- Search the output for library names you don't expect
- Check `angular.json` `polyfills` and any imports in `main.ts` and `app.config.ts`

Often you find old polyfills (`core-js`), locale data for many languages or a full icon set imported in startup code.

## 444: How do you handle locale data for many languages without bloating bundles?

Angular's locale data (for `DatePipe`, `CurrencyPipe`, etc.) is registered with `registerLocaleData`. Importing all locales statically adds them all to the bundle.

Load them on demand, with one `import()` per supported locale so the bundler creates a separate chunk for each:

```ts
const locales: Record<string, () => Promise<{ default: unknown }>> = {
  de: () => import("@angular/common/locales/de"),
  fr: () => import("@angular/common/locales/fr"),
  ja: () => import("@angular/common/locales/ja"),
};

async function loadLocale(id: string) {
  const mod = await locales[id]();
  registerLocaleData(mod.default);
}
```

Or use compile-time i18n with `--localize`, which includes only the locale data for each build.

## 445: How would you reduce JavaScript execution time during startup apart from bundle size?

- Avoid top-level code that runs on import (big object literals, setup code)
- Make root services and initializers lazy
- Render less in the first view (`@defer`, pagination)
- Use SSR with incremental hydration so only part of the app runs at first
- Move JSON parsing of big config or data to a worker or load it later
- Use `JSON.parse` on a string for very large static data, which is faster to parse than an equivalent JS object literal

## 446: How do you prove that a performance fix worked in production?

- Define the metric and segment before shipping (for example p75 INP on the product page on mobile)
- Ship behind a feature flag if possible and compare groups
- Look at field data for a few days, since daily traffic patterns vary
- Check that other metrics didn't get worse
- Keep a short write-up with before and after numbers

Without field data, you only know that the lab result changed, not that users noticed.

## 447: What should you look for in a code review from a performance point of view?

- New dependencies and their size, and where they're imported
- Lists without a proper `track` key or without pagination
- Methods, getters or impure pipes doing work in templates
- Subscriptions without cleanup, intervals, global listeners
- Components set to `Eager` without a reason
- Effects that write signals
- Images without `NgOptimizedImage`, sizes or `priority` on the LCP image
- Heavy work in event handlers or lifecycle hooks
- New providers in `app.config.ts`

## 448: What are the trade-offs of using signals vs. RxJS for performance?

Signals:

- Synchronous, always have a value, fine-grained template updates
- No subscriptions to manage, less risk of leaks
- Not built for event streams over time (debounce, retry, combining async sources)

RxJS:

- Great for async event streams and complex timing
- Needs subscription management
- Templates need the `async` pipe or `toSignal()` to update OnPush views

Common pattern: RxJS for async flows at the edges (HTTP, sockets, user events over time), signals for state and what the template reads.

## 449: How does Angular's roadmap affect how you should optimize today?

Recent versions made the fast options the default: standalone, built-in control flow, esbuild, zoneless for new apps (v21), OnPush by default and fetch-based HTTP and incremental hydration by default (v22).

So the best investment is to keep the app up to date and write code that fits these defaults: signals, OnPush-friendly data flow, no reliance on Zone.js, SSR-safe code. Custom tricks that work around the framework can become obstacles in future updates.

## 450: If you could make only three changes to speed up a typical older Angular app, which would you pick?

It depends on measurements, but for a typical app built a few years ago, these give the most for the effort:

1. **Lazy load routes and `@defer` heavy parts**: often cuts the initial bundle in half and improves LCP.
2. **OnPush with signals (and later zoneless)**: cuts change detection work on every interaction, improving INP.
3. **Fix images with `NgOptimizedImage`**: `priority` on the LCP image, sizes on every image, lazy loading below the fold, modern formats through a loader.

After that, look at SSR or prerendering for public pages, and at specific slow screens with the profiler.
