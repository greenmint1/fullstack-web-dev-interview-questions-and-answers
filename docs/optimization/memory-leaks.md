# Memory Leaks Interview Questions and Answers

_Last updated: November 25, 2026_

This file has 450 interview questions and answers about memory leaks in full stack web apps: 150 easy, 150 moderate and 150 advanced. Most answers focus on JavaScript and TypeScript in the browser and in Node.js, with framework examples for React, Angular and Vue. The tools covered are the current Chrome DevTools Memory panel and the current Node.js LTS.

## Table of Contents

- [Easy Questions (1-150)](#easy-questions-1-150)
- [Moderate Questions (151-300)](#moderate-questions-151-300)
- [Advanced Questions (301-450)](#advanced-questions-301-450)

### Easy Questions (1-150)

- [1: What is a memory leak?](#1-what-is-a-memory-leak)
- [2: Can you have memory leaks in a language with a garbage collector?](#2-can-you-have-memory-leaks-in-a-language-with-a-garbage-collector)
- [3: What is garbage collection?](#3-what-is-garbage-collection)
- [4: What does "reachable" mean in garbage collection?](#4-what-does-reachable-mean-in-garbage-collection)
- [5: What are GC roots?](#5-what-are-gc-roots)
- [6: What is the mark-and-sweep algorithm?](#6-what-is-the-mark-and-sweep-algorithm)
- [7: What is reference counting and why don't JavaScript engines use it alone?](#7-what-is-reference-counting-and-why-dont-javascript-engines-use-it-alone)
- [8: Do circular references cause memory leaks in modern JavaScript?](#8-do-circular-references-cause-memory-leaks-in-modern-javascript)
- [9: What is the difference between the stack and the heap?](#9-what-is-the-difference-between-the-stack-and-the-heap)
- [10: What are the common signs that an app has a memory leak?](#10-what-are-the-common-signs-that-an-app-has-a-memory-leak)
- [11: What is the difference between a memory leak and high memory usage?](#11-what-is-the-difference-between-a-memory-leak-and-high-memory-usage)
- [12: What is memory bloat?](#12-what-is-memory-bloat)
- [13: What are the most common causes of memory leaks in browser JavaScript?](#13-what-are-the-most-common-causes-of-memory-leaks-in-browser-javascript)
- [14: What are the most common causes of memory leaks in Node.js?](#14-what-are-the-most-common-causes-of-memory-leaks-in-nodejs)
- [15: What is an accidental global variable?](#15-what-is-an-accidental-global-variable)
- [16: How does strict mode help prevent memory leaks?](#16-how-does-strict-mode-help-prevent-memory-leaks)
- [17: How can a forgotten setInterval cause a memory leak?](#17-how-can-a-forgotten-setinterval-cause-a-memory-leak)
- [18: Can setTimeout cause a memory leak?](#18-can-settimeout-cause-a-memory-leak)
- [19: How do event listeners cause memory leaks?](#19-how-do-event-listeners-cause-memory-leaks)
- [20: Why must you pass the same function to removeEventListener?](#20-why-must-you-pass-the-same-function-to-removeeventlistener)
- [21: How can AbortController be used to remove event listeners?](#21-how-can-abortcontroller-be-used-to-remove-event-listeners)
- [22: What is the once option in addEventListener?](#22-what-is-the-once-option-in-addeventlistener)
- [23: What is a detached DOM node?](#23-what-is-a-detached-dom-node)
- [24: How can a closure cause a memory leak?](#24-how-can-a-closure-cause-a-memory-leak)
- [25: How can a cache become a memory leak?](#25-how-can-a-cache-become-a-memory-leak)
- [26: What is an LRU cache?](#26-what-is-an-lru-cache)
- [27: What is a WeakMap?](#27-what-is-a-weakmap)
- [28: Why can't you iterate over a WeakMap?](#28-why-cant-you-iterate-over-a-weakmap)
- [29: What is a WeakSet?](#29-what-is-a-weakset)
- [30: What is a WeakRef?](#30-what-is-a-weakref)
- [31: What is the difference between a Map and a WeakMap when it comes to memory?](#31-what-is-the-difference-between-a-map-and-a-weakmap-when-it-comes-to-memory)
- [32: Can console.log cause a memory leak?](#32-can-consolelog-cause-a-memory-leak)
- [33: What is the Chrome DevTools Memory panel?](#33-what-is-the-chrome-devtools-memory-panel)
- [34: What is a heap snapshot?](#34-what-is-a-heap-snapshot)
- [35: What is the difference between shallow size and retained size?](#35-what-is-the-difference-between-shallow-size-and-retained-size)
- [36: What are retainers in a heap snapshot?](#36-what-are-retainers-in-a-heap-snapshot)
- [37: What is the Performance Monitor in Chrome DevTools?](#37-what-is-the-performance-monitor-in-chrome-devtools)
- [38: How can you use the browser Task Manager to spot leaks?](#38-how-can-you-use-the-browser-task-manager-to-spot-leaks)
- [39: Why should you force garbage collection before taking measurements?](#39-why-should-you-force-garbage-collection-before-taking-measurements)
- [40: What does process.memoryUsage() return in Node.js?](#40-what-does-processmemoryusage-return-in-nodejs)
- [41: What is RSS?](#41-what-is-rss)
- [42: What does "JavaScript heap out of memory" mean in Node.js?](#42-what-does-javascript-heap-out-of-memory-mean-in-nodejs)
- [43: What does the --max-old-space-size flag do?](#43-what-does-the---max-old-space-size-flag-do)
- [44: Why is increasing the memory limit not a real fix for a leak?](#44-why-is-increasing-the-memory-limit-not-a-real-fix-for-a-leak)
- [45: How do you check if a page leaks memory by repeating an action?](#45-how-do-you-check-if-a-page-leaks-memory-by-repeating-an-action)
- [46: Why are single page apps more likely to have memory leaks than multi page apps?](#46-why-are-single-page-apps-more-likely-to-have-memory-leaks-than-multi-page-apps)
- [47: How do you avoid memory leaks in a React useEffect?](#47-how-do-you-avoid-memory-leaks-in-a-react-useeffect)
- [48: Why does React run effects twice in development with Strict Mode?](#48-why-does-react-run-effects-twice-in-development-with-strict-mode)
- [49: How do you cancel a fetch request when a React component unmounts?](#49-how-do-you-cancel-a-fetch-request-when-a-react-component-unmounts)
- [50: Does setting state on an unmounted React component cause a memory leak?](#50-does-setting-state-on-an-unmounted-react-component-cause-a-memory-leak)
- [51: How do you avoid memory leaks with RxJS subscriptions in Angular?](#51-how-do-you-avoid-memory-leaks-with-rxjs-subscriptions-in-angular)
- [52: Do you need to unsubscribe from Angular HttpClient requests?](#52-do-you-need-to-unsubscribe-from-angular-httpclient-requests)
- [53: How do you clean up in a Vue component?](#53-how-do-you-clean-up-in-a-vue-component)
- [54: Why do third-party libraries often need a destroy method call?](#54-why-do-third-party-libraries-often-need-a-destroy-method-call)
- [55: How can WebSockets cause memory leaks?](#55-how-can-websockets-cause-memory-leaks)
- [56: What is URL.createObjectURL and why can it leak memory?](#56-what-is-urlcreateobjecturl-and-why-can-it-leak-memory)
- [57: Do IntersectionObserver and ResizeObserver need cleanup?](#57-do-intersectionobserver-and-resizeobserver-need-cleanup)
- [58: Do Web Workers leak memory if you don't terminate them?](#58-do-web-workers-leak-memory-if-you-dont-terminate-them)
- [59: What is an EventEmitter leak in Node.js?](#59-what-is-an-eventemitter-leak-in-nodejs)
- [60: What is MaxListenersExceededWarning?](#60-what-is-maxlistenersexceededwarning)
- [61: How do you remove a listener from a Node.js EventEmitter?](#61-how-do-you-remove-a-listener-from-a-nodejs-eventemitter)
- [62: Why is storing request data in a global variable a leak in Node.js?](#62-why-is-storing-request-data-in-a-global-variable-a-leak-in-nodejs)
- [63: Why is the default express-session MemoryStore not for production?](#63-why-is-the-default-express-session-memorystore-not-for-production)
- [64: How can unclosed database connections cause problems?](#64-how-can-unclosed-database-connections-cause-problems)
- [65: What is a connection pool?](#65-what-is-a-connection-pool)
- [66: Can unclosed streams cause memory leaks in Node.js?](#66-can-unclosed-streams-cause-memory-leaks-in-nodejs)
- [67: What happens to memory when you set a variable to null?](#67-what-happens-to-memory-when-you-set-a-variable-to-null)
- [68: Does the delete operator free memory?](#68-does-the-delete-operator-free-memory)
- [69: How do you empty an array or a Map so its items can be garbage collected?](#69-how-do-you-empty-an-array-or-a-map-so-its-items-can-be-garbage-collected)
- [70: What is a minor GC and a major GC?](#70-what-is-a-minor-gc-and-a-major-gc)
- [71: What is the generational hypothesis?](#71-what-is-the-generational-hypothesis)
- [72: What is a GC pause?](#72-what-is-a-gc-pause)
- [73: Why does a memory leak make an app slower before it crashes?](#73-why-does-a-memory-leak-make-an-app-slower-before-it-crashes)
- [74: How do you open the DevTools Memory panel?](#74-how-do-you-open-the-devtools-memory-panel)
- [75: What profiling types are in the Chrome Memory panel?](#75-what-profiling-types-are-in-the-chrome-memory-panel)
- [76: What views does a heap snapshot have in Chrome DevTools?](#76-what-views-does-a-heap-snapshot-have-in-chrome-devtools)
- [77: What is the Comparison view in a heap snapshot?](#77-what-is-the-comparison-view-in-a-heap-snapshot)
- [78: What does "Detached" mean in a heap snapshot?](#78-what-does-detached-mean-in-a-heap-snapshot)
- [79: How do you take a heap snapshot in Node.js?](#79-how-do-you-take-a-heap-snapshot-in-nodejs)
- [80: How do you connect Chrome DevTools to a Node.js process?](#80-how-do-you-connect-chrome-devtools-to-a-nodejs-process)
- [81: Does taking a heap snapshot affect the app?](#81-does-taking-a-heap-snapshot-affect-the-app)
- [82: What are the steps to fix a memory leak?](#82-what-are-the-steps-to-fix-a-memory-leak)
- [83: How do memory leaks affect mobile users?](#83-how-do-memory-leaks-affect-mobile-users)
- [84: Can loading too many images cause memory problems?](#84-can-loading-too-many-images-cause-memory-problems)
- [85: How does infinite scroll cause memory growth?](#85-how-does-infinite-scroll-cause-memory-growth)
- [86: What is list virtualization?](#86-what-is-list-virtualization)
- [87: Can a global state store like Redux leak memory?](#87-can-a-global-state-store-like-redux-leak-memory)
- [88: How can an undo history leak memory?](#88-how-can-an-undo-history-leak-memory)
- [89: Does localStorage cause memory leaks?](#89-does-localstorage-cause-memory-leaks)
- [90: What is performance.memory and should you use it?](#90-what-is-performancememory-and-should-you-use-it)
- [91: Do other browsers have memory tools?](#91-do-other-browsers-have-memory-tools)
- [92: Can iframes cause memory leaks?](#92-can-iframes-cause-memory-leaks)
- [93: How can a memoized function leak memory?](#93-how-can-a-memoized-function-leak-memory)
- [94: What is the problem with an unbounded array of logs in memory?](#94-what-is-the-problem-with-an-unbounded-array-of-logs-in-memory)
- [95: Can logging libraries cause memory growth in Node.js?](#95-can-logging-libraries-cause-memory-growth-in-nodejs)
- [96: What is the difference between a memory leak and a resource leak?](#96-what-is-the-difference-between-a-memory-leak-and-a-resource-leak)
- [97: What does "EMFILE: too many open files" mean?](#97-what-does-emfile-too-many-open-files-mean)
- [98: Why is garbage collection not predictable in JavaScript?](#98-why-is-garbage-collection-not-predictable-in-javascript)
- [99: Do closures always keep their entire scope alive?](#99-do-closures-always-keep-their-entire-scope-alive)
- [100: How can a closure inside a loop cause memory growth?](#100-how-can-a-closure-inside-a-loop-cause-memory-growth)
- [101: What does a "sawtooth" memory graph mean?](#101-what-does-a-sawtooth-memory-graph-mean)
- [102: What does a "staircase" memory graph usually mean?](#102-what-does-a-staircase-memory-graph-usually-mean)
- [103: What is OOMKilled in Kubernetes?](#103-what-is-oomkilled-in-kubernetes)
- [104: What does exit code 137 mean?](#104-what-does-exit-code-137-mean)
- [105: Why do restarts hide memory leaks?](#105-why-do-restarts-hide-memory-leaks)
- [106: Can serverless functions have memory leaks?](#106-can-serverless-functions-have-memory-leaks)
- [107: Does TypeScript prevent memory leaks?](#107-does-typescript-prevent-memory-leaks)
- [108: Why should you test memory in an incognito window or a clean profile?](#108-why-should-you-test-memory-in-an-incognito-window-or-a-clean-profile)
- [109: Does Lighthouse detect memory leaks?](#109-does-lighthouse-detect-memory-leaks)
- [110: What is MemLab?](#110-what-is-memlab)
- [111: What is event delegation and how does it help memory?](#111-what-is-event-delegation-and-how-does-it-help-memory)
- [112: Do you need to remove listeners from elements before removing them from the page?](#112-do-you-need-to-remove-listeners-from-elements-before-removing-them-from-the-page)
- [113: Does requestAnimationFrame need cleanup?](#113-does-requestanimationframe-need-cleanup)
- [114: How do you release a camera or microphone stream?](#114-how-do-you-release-a-camera-or-microphone-stream)
- [115: Why can reading a whole file into memory be a problem in Node.js?](#115-why-can-reading-a-whole-file-into-memory-be-a-problem-in-nodejs)
- [116: Why is loading all rows from a database at once risky?](#116-why-is-loading-all-rows-from-a-database-at-once-risky)
- [117: Can building a large string cause memory problems?](#117-can-building-a-large-string-cause-memory-problems)
- [118: What does "Invalid string length" mean in JavaScript?](#118-what-does-invalid-string-length-mean-in-javascript)
- [119: What is a singleton and how can it leak memory?](#119-what-is-a-singleton-and-how-can-it-leak-memory)
- [120: How does the Node.js module cache relate to memory?](#120-how-does-the-nodejs-module-cache-relate-to-memory)
- [121: What does timer.unref() do in Node.js?](#121-what-does-timerunref-do-in-nodejs)
- [122: What is AbortSignal.timeout()?](#122-what-is-abortsignaltimeout)
- [123: How can Promise.race with a timeout leak a timer?](#123-how-can-promiserace-with-a-timeout-leak-a-timer)
- [124: What is the "Collect garbage" button in Chrome DevTools?](#124-what-is-the-collect-garbage-button-in-chrome-devtools)
- [125: Can CSS cause memory leaks?](#125-can-css-cause-memory-leaks)
- [126: What is a GPU memory leak in a web app?](#126-what-is-a-gpu-memory-leak-in-a-web-app)
- [127: How do you release memory used by a canvas?](#127-how-do-you-release-memory-used-by-a-canvas)
- [128: What happens to memory when a user closes a browser tab?](#128-what-happens-to-memory-when-a-user-closes-a-browser-tab)
- [129: What is bfcache and how does it relate to memory?](#129-what-is-bfcache-and-how-does-it-relate-to-memory)
- [130: Why should you avoid the unload event?](#130-why-should-you-avoid-the-unload-event)
- [131: What is a memory budget?](#131-what-is-a-memory-budget)
- [132: How do you monitor memory of a Node.js app in production?](#132-how-do-you-monitor-memory-of-a-nodejs-app-in-production)
- [133: Why should you look at memory trends over days, not minutes?](#133-why-should-you-look-at-memory-trends-over-days-not-minutes)
- [134: What is heap size versus heap used?](#134-what-is-heap-size-versus-heap-used)
- [135: Why doesn't memory go down right away after you free objects?](#135-why-doesnt-memory-go-down-right-away-after-you-free-objects)
- [136: What are global variables in ES modules?](#136-what-are-global-variables-in-es-modules)
- [137: How do you find which objects are growing in a heap snapshot?](#137-how-do-you-find-which-objects-are-growing-in-a-heap-snapshot)
- [138: What does the Distance column mean in a heap snapshot?](#138-what-does-the-distance-column-mean-in-a-heap-snapshot)
- [139: Why do some objects in heap snapshots have names in parentheses?](#139-why-do-some-objects-in-heap-snapshots-have-names-in-parentheses)
- [140: Why does naming your functions help when debugging memory?](#140-why-does-naming-your-functions-help-when-debugging-memory)
- [141: Can a memory leak happen in the server rendering of a React or Next.js app?](#141-can-a-memory-leak-happen-in-the-server-rendering-of-a-react-or-nextjs-app)
- [142: Can a development server leak memory while a production build does not?](#142-can-a-development-server-leak-memory-while-a-production-build-does-not)
- [143: What is the Prisma client hot-reload problem in Next.js?](#143-what-is-the-prisma-client-hot-reload-problem-in-nextjs)
- [144: How do you clean up a jQuery plugin or jQuery data?](#144-how-do-you-clean-up-a-jquery-plugin-or-jquery-data)
- [145: What is the difference between remove() and detach() in jQuery?](#145-what-is-the-difference-between-remove-and-detach-in-jquery)
- [146: How can a chat or live feed app leak memory?](#146-how-can-a-chat-or-live-feed-app-leak-memory)
- [147: Can a memory leak cause a security problem?](#147-can-a-memory-leak-cause-a-security-problem)
- [148: Is it safe to share heap snapshots?](#148-is-it-safe-to-share-heap-snapshots)
- [149: What is memory pressure?](#149-what-is-memory-pressure)
- [150: What is a good first step when someone reports that an app gets slow after a while?](#150-what-is-a-good-first-step-when-someone-reports-that-an-app-gets-slow-after-a-while)

### Moderate Questions (151-300)

- [151: What is the three-snapshot technique?](#151-what-is-the-three-snapshot-technique)
- [152: How do you read a retainer path to find the cause of a leak?](#152-how-do-you-read-a-retainer-path-to-find-the-cause-of-a-leak)
- [153: How do you use Allocations on timeline in Chrome DevTools?](#153-how-do-you-use-allocations-on-timeline-in-chrome-devtools)
- [154: When would you use Allocation sampling instead of a heap snapshot?](#154-when-would-you-use-allocation-sampling-instead-of-a-heap-snapshot)
- [155: What is the Detached elements profile in Chrome DevTools?](#155-what-is-the-detached-elements-profile-in-chrome-devtools)
- [156: What is queryObjects() in the DevTools console?](#156-what-is-queryobjects-in-the-devtools-console)
- [157: How do you find a leak in a React app using heap snapshots?](#157-how-do-you-find-a-leak-in-a-react-app-using-heap-snapshots)
- [158: Can a useRef cause a memory leak?](#158-can-a-useref-cause-a-memory-leak)
- [159: How do you safely subscribe to an external store in React?](#159-how-do-you-safely-subscribe-to-an-external-store-in-react)
- [160: How does TanStack Query keep its cache from growing forever?](#160-how-does-tanstack-query-keep-its-cache-from-growing-forever)
- [161: Can an Apollo Client cache grow too large?](#161-can-an-apollo-client-cache-grow-too-large)
- [162: How does the takeUntil pattern work in Angular and what is the common mistake?](#162-how-does-the-takeuntil-pattern-work-in-angular-and-what-is-the-common-mistake)
- [163: What is DestroyRef in Angular?](#163-what-is-destroyref-in-angular)
- [164: Do Angular @HostListener and Renderer2.listen need manual cleanup?](#164-do-angular-hostlistener-and-renderer2listen-need-manual-cleanup)
- [165: Do Angular signals and effects need cleanup?](#165-do-angular-signals-and-effects-need-cleanup)
- [166: How can an Angular root service leak component data?](#166-how-can-an-angular-root-service-leak-component-data)
- [167: How can shareReplay cause a memory leak in RxJS?](#167-how-can-sharereplay-cause-a-memory-leak-in-rxjs)
- [168: How do you clean up an event bus in Vue?](#168-how-do-you-clean-up-an-event-bus-in-vue)
- [169: How does KeepAlive in Vue affect memory?](#169-how-does-keepalive-in-vue-affect-memory)
- [170: How do Pinia store subscriptions behave on unmount?](#170-how-do-pinia-store-subscriptions-behave-on-unmount)
- [171: How does Svelte handle store subscriptions?](#171-how-does-svelte-handle-store-subscriptions)
- [172: How do you destroy a Chart.js chart?](#172-how-do-you-destroy-a-chartjs-chart)
- [173: How do you clean up map libraries like Leaflet or Mapbox GL?](#173-how-do-you-clean-up-map-libraries-like-leaflet-or-mapbox-gl)
- [174: How do you clean up the Monaco editor?](#174-how-do-you-clean-up-the-monaco-editor)
- [175: How do you clean up animation libraries like GSAP?](#175-how-do-you-clean-up-animation-libraries-like-gsap)
- [176: Can modals and tooltips appended to document.body leak?](#176-can-modals-and-tooltips-appended-to-documentbody-leak)
- [177: How do you clean up custom elements (web components)?](#177-how-do-you-clean-up-custom-elements-web-components)
- [178: Do debounced functions need cleanup on unmount?](#178-do-debounced-functions-need-cleanup-on-unmount)
- [179: Which other browser APIs need explicit closing?](#179-which-other-browser-apis-need-explicit-closing)
- [180: How can Cache Storage in a service worker keep growing?](#180-how-can-cache-storage-in-a-service-worker-keep-growing)
- [181: Can history.pushState state objects use a lot of memory?](#181-can-historypushstate-state-objects-use-a-lot-of-memory)
- [182: How can error tracking or analytics code cause memory growth?](#182-how-can-error-tracking-or-analytics-code-cause-memory-growth)
- [183: How do you set up an LRU cache with limits in Node.js?](#183-how-do-you-set-up-an-lru-cache-with-limits-in-nodejs)
- [184: What is the difference between TTL and LRU eviction?](#184-what-is-the-difference-between-ttl-and-lru-eviction)
- [185: Why should a DataLoader be created per request?](#185-why-should-a-dataloader-be-created-per-request)
- [186: How can an ORM's identity map grow in a long-running process?](#186-how-can-an-orms-identity-map-grow-in-a-long-running-process)
- [187: How do Prometheus metrics with high-cardinality labels cause memory growth?](#187-how-do-prometheus-metrics-with-high-cardinality-labels-cause-memory-growth)
- [188: How can OpenTelemetry spans leak memory?](#188-how-can-opentelemetry-spans-leak-memory)
- [189: What happens if you don't consume a fetch response body in Node.js?](#189-what-happens-if-you-dont-consume-a-fetch-response-body-in-nodejs)
- [190: What is stream backpressure and how does ignoring it use memory?](#190-what-is-stream-backpressure-and-how-does-ignoring-it-use-memory)
- [191: How can a Socket.IO server leak memory?](#191-how-can-a-socketio-server-leak-memory)
- [192: Why is adding process.on listeners inside a function a problem?](#192-why-is-adding-processon-listeners-inside-a-function-a-problem)
- [193: What is AsyncLocalStorage and can it hold memory longer than expected?](#193-what-is-asynclocalstorage-and-can-it-hold-memory-longer-than-expected)
- [194: How can a promise that never settles cause a leak?](#194-how-can-a-promise-that-never-settles-cause-a-leak)
- [195: How do you write a simple memory leak test in Node.js?](#195-how-do-you-write-a-simple-memory-leak-test-in-nodejs)
- [196: What does the --heapsnapshot-near-heap-limit flag do?](#196-what-does-the---heapsnapshot-near-heap-limit-flag-do)
- [197: What does the --trace-gc flag show?](#197-what-does-the---trace-gc-flag-show)
- [198: What does v8.getHeapStatistics() return?](#198-what-does-v8getheapstatistics-return)
- [199: What does the --heap-prof flag do in Node.js?](#199-what-does-the---heap-prof-flag-do-in-nodejs)
- [200: How do you reproduce a server-side leak locally?](#200-how-do-you-reproduce-a-server-side-leak-locally)
- [201: How can Jest help you notice memory leaks in tests?](#201-how-can-jest-help-you-notice-memory-leaks-in-tests)
- [202: How can you measure page memory in a Playwright or Puppeteer test?](#202-how-can-you-measure-page-memory-in-a-playwright-or-puppeteer-test)
- [203: What does a MemLab scenario look like?](#203-what-does-a-memlab-scenario-look-like)
- [204: How do you use performance.measureUserAgentSpecificMemory()?](#204-how-do-you-use-performancemeasureuseragentspecificmemory)
- [205: Why is collecting memory data from real users useful?](#205-why-is-collecting-memory-data-from-real-users-useful)
- [206: Why should you measure memory in a production build of a frontend app?](#206-why-should-you-measure-memory-in-a-production-build-of-a-frontend-app)
- [207: Can browser devtools extensions keep objects alive during memory tests?](#207-can-browser-devtools-extensions-keep-objects-alive-during-memory-tests)
- [208: How can a hot module reload in the browser leak memory during development?](#208-how-can-a-hot-module-reload-in-the-browser-leak-memory-during-development)
- [209: How do you size the Node.js heap inside a container?](#209-how-do-you-size-the-nodejs-heap-inside-a-container)
- [210: Why do front-end builds sometimes fail with "heap out of memory"?](#210-why-do-front-end-builds-sometimes-fail-with-heap-out-of-memory)
- [211: What does PM2's max_memory_restart do?](#211-what-does-pm2s-max_memory_restart-do)
- [212: How do you limit memory for Node.js worker threads?](#212-how-do-you-limit-memory-for-nodejs-worker-threads)
- [213: How can Puppeteer or Playwright leak memory in a server app?](#213-how-can-puppeteer-or-playwright-leak-memory-in-a-server-app)
- [214: How can child processes leak in Node.js?](#214-how-can-child-processes-leak-in-nodejs)
- [215: How should you handle file uploads to avoid memory spikes?](#215-how-should-you-handle-file-uploads-to-avoid-memory-spikes)
- [216: Why should you set a body size limit in an Express app?](#216-why-should-you-set-a-body-size-limit-in-an-express-app)
- [217: How can an in-memory rate limiter or dedup set leak?](#217-how-can-an-in-memory-rate-limiter-or-dedup-set-leak)
- [218: How do you periodically clean up expired entries in a Map?](#218-how-do-you-periodically-clean-up-expired-entries-in-a-map)
- [219: What is the risk of caching promises?](#219-what-is-the-risk-of-caching-promises)
- [220: How can capturing the request object in a closure cause a leak?](#220-how-can-capturing-the-request-object-in-a-closure-cause-a-leak)
- [221: How can you avoid closures holding large objects you don't need?](#221-how-can-you-avoid-closures-holding-large-objects-you-dont-need)
- [222: How does Reselect 5 avoid memory growth in memoized selectors?](#222-how-does-reselect-5-avoid-memory-growth-in-memoized-selectors)
- [223: When should you use a WeakMap as a cache?](#223-when-should-you-use-a-weakmap-as-a-cache)
- [224: Why can deep copies double memory usage?](#224-why-can-deep-copies-double-memory-usage)
- [225: How do you handle very large JSON payloads in Node.js?](#225-how-do-you-handle-very-large-json-payloads-in-nodejs)
- [226: What does lean() do in Mongoose and why does it save memory?](#226-what-does-lean-do-in-mongoose-and-why-does-it-save-memory)
- [227: How do you process a large database table without loading it all?](#227-how-do-you-process-a-large-database-table-without-loading-it-all)
- [228: How can BullMQ jobs use more and more Redis memory?](#228-how-can-bullmq-jobs-use-more-and-more-redis-memory)
- [229: How can an in-memory job or retry queue cause problems?](#229-how-can-an-in-memory-job-or-retry-queue-cause-problems)
- [230: How can HTTP keep-alive agents hold memory?](#230-how-can-http-keep-alive-agents-hold-memory)
- [231: Why shouldn't you create a new Redis or database client per request?](#231-why-shouldnt-you-create-a-new-redis-or-database-client-per-request)
- [232: How can image processing with sharp use a lot of memory?](#232-how-can-image-processing-with-sharp-use-a-lot-of-memory)
- [233: How do async generators relate to leaks?](#233-how-do-async-generators-relate-to-leaks)
- [234: How should GraphQL subscriptions be cleaned up on the server?](#234-how-should-graphql-subscriptions-be-cleaned-up-on-the-server)
- [235: Can holding a reference to window.open() leak memory?](#235-can-holding-a-reference-to-windowopen-leak-memory)
- [236: How can third-party scripts cause leaks you can't fix directly?](#236-how-can-third-party-scripts-cause-leaks-you-cant-fix-directly)
- [237: How do you read heap snapshots of minified code?](#237-how-do-you-read-heap-snapshots-of-minified-code)
- [238: Why do leaks often show up as growing arrays of listeners?](#238-why-do-leaks-often-show-up-as-growing-arrays-of-listeners)
- [239: How do you check the number of event listeners on an element?](#239-how-do-you-check-the-number-of-event-listeners-on-an-element)
- [240: What is the difference between a leak in the DOM and a leak in JavaScript objects?](#240-what-is-the-difference-between-a-leak-in-the-dom-and-a-leak-in-javascript-objects)
- [241: Why can a detached DOM node keep a much bigger tree alive?](#241-why-can-a-detached-dom-node-keep-a-much-bigger-tree-alive)
- [242: How can storing DOM nodes in a JavaScript array cause a leak?](#242-how-can-storing-dom-nodes-in-a-javascript-array-cause-a-leak)
- [243: How can postMessage listeners leak in apps that use iframes or workers?](#243-how-can-postmessage-listeners-leak-in-apps-that-use-iframes-or-workers)
- [244: What happens to timers and listeners when an iframe is removed?](#244-what-happens-to-timers-and-listeners-when-an-iframe-is-removed)
- [245: How can a global error handler leak memory?](#245-how-can-a-global-error-handler-leak-memory)
- [246: Can capturing stack traces use a lot of memory?](#246-can-capturing-stack-traces-use-a-lot-of-memory)
- [247: How can logging the same object many times keep it alive in Node.js?](#247-how-can-logging-the-same-object-many-times-keep-it-alive-in-nodejs)
- [248: What is a ring buffer and when would you use one to avoid leaks?](#248-what-is-a-ring-buffer-and-when-would-you-use-one-to-avoid-leaks)
- [249: How can a pub/sub or observer pattern you write yourself leak?](#249-how-can-a-pubsub-or-observer-pattern-you-write-yourself-leak)
- [250: What is the difference between a leak caused by your code and one caused by the runtime?](#250-what-is-the-difference-between-a-leak-caused-by-your-code-and-one-caused-by-the-runtime)
- [251: What is cross-request state pollution in server rendering?](#251-what-is-cross-request-state-pollution-in-server-rendering)
- [252: How should you create a Redux store in a Next.js App Router app?](#252-how-should-you-create-a-redux-store-in-a-nextjs-app-router-app)
- [253: How does React's cache() function help with per-request data on the server?](#253-how-does-reacts-cache-function-help-with-per-request-data-on-the-server)
- [254: What is cacheMaxMemorySize in Next.js?](#254-what-is-cachemaxmemorysize-in-nextjs)
- [255: How does Nuxt avoid cross-request state on the server?](#255-how-does-nuxt-avoid-cross-request-state-on-the-server)
- [256: Why must you call seal() on styled-components' ServerStyleSheet?](#256-why-must-you-call-seal-on-styled-components-serverstylesheet)
- [257: How can axios interceptors leak in a SPA?](#257-how-can-axios-interceptors-leak-in-a-spa)
- [258: Why is adding middleware inside a route handler a leak in Express?](#258-why-is-adding-middleware-inside-a-route-handler-a-leak-in-express)
- [259: How can a WebSocket reconnect loop create duplicate connections?](#259-how-can-a-websocket-reconnect-loop-create-duplicate-connections)
- [260: Why might polling keep running in a hidden tab, and how do you handle it?](#260-why-might-polling-keep-running-in-a-hidden-tab-and-how-do-you-handle-it)
- [261: Why can removeEventListener fail in class components with bind?](#261-why-can-removeeventlistener-fail-in-class-components-with-bind)
- [262: How do you stop a MobX reaction?](#262-how-do-you-stop-a-mobx-reaction)
- [263: How do you unsubscribe from a Zustand store outside React?](#263-how-do-you-unsubscribe-from-a-zustand-store-outside-react)
- [264: Why is lodash memoize risky on a server?](#264-why-is-lodash-memoize-risky-on-a-server)
- [265: Why does a Map keyed by objects from JSON.parse never get cache hits?](#265-why-does-a-map-keyed-by-objects-from-jsonparse-never-get-cache-hits)
- [266: Does deleting an entry from require.cache free the module's memory?](#266-does-deleting-an-entry-from-requirecache-free-the-modules-memory)
- [267: How can vm contexts or new Function per request cause memory growth?](#267-how-can-vm-contexts-or-new-function-per-request-cause-memory-growth)
- [268: How can template compilation per request be a problem?](#268-how-can-template-compilation-per-request-be-a-problem)
- [269: How can an AbortSignal leak listeners?](#269-how-can-an-abortsignal-leak-listeners)
- [270: What is events.once in Node.js and how does it help with cleanup?](#270-what-is-eventsonce-in-nodejs-and-how-does-it-help-with-cleanup)
- [271: How can storing Timeout objects in a Map leak memory in Node.js?](#271-how-can-storing-timeout-objects-in-a-map-leak-memory-in-nodejs)
- [272: Why shouldn't you call global.gc() in production code?](#272-why-shouldnt-you-call-globalgc-in-production-code)
- [273: How can a watch-mode build tool or long-running CLI leak memory?](#273-how-can-a-watch-mode-build-tool-or-long-running-cli-leak-memory)
- [274: How can jsdom-based tests leak memory?](#274-how-can-jsdom-based-tests-leak-memory)
- [275: How can you analyze Node.js heap snapshots with MemLab?](#275-how-can-you-analyze-nodejs-heap-snapshots-with-memlab)
- [276: What can you do when DevTools can't open a large heap snapshot?](#276-what-can-you-do-when-devtools-cant-open-a-large-heap-snapshot)
- [277: How do you observe GC events in Node.js from code?](#277-how-do-you-observe-gc-events-in-nodejs-from-code)
- [278: How is event loop lag related to memory leaks?](#278-how-is-event-loop-lag-related-to-memory-leaks)
- [279: What memory metric should you alert on for a Node.js service?](#279-what-memory-metric-should-you-alert-on-for-a-nodejs-service)
- [280: Is it a good idea to expose a heap snapshot endpoint in production?](#280-is-it-a-good-idea-to-expose-a-heap-snapshot-endpoint-in-production)
- [281: What is a Node.js diagnostic report and how does it help with memory issues?](#281-what-is-a-nodejs-diagnostic-report-and-how-does-it-help-with-memory-issues)
- [282: What is the difference between memory requests and limits in Kubernetes?](#282-what-is-the-difference-between-memory-requests-and-limits-in-kubernetes)
- [283: How do you tell whether memory growth is in the JS heap or outside it?](#283-how-do-you-tell-whether-memory-growth-is-in-the-js-heap-or-outside-it)
- [284: Why don't Buffer contents show up as heap size in snapshots?](#284-why-dont-buffer-contents-show-up-as-heap-size-in-snapshots)
- [285: How can a WeakMap still cause a leak?](#285-how-can-a-weakmap-still-cause-a-leak)
- [286: What is FinalizationRegistry?](#286-what-is-finalizationregistry)
- [287: What is the explicit resource management proposal (using) and how does it help?](#287-what-is-the-explicit-resource-management-proposal-using-and-how-does-it-help)
- [288: What is DisposableStack?](#288-what-is-disposablestack)
- [289: How do you prevent memory leaks when using setInterval for polling in a component?](#289-how-do-you-prevent-memory-leaks-when-using-setinterval-for-polling-in-a-component)
- [290: How can React Context keep large data alive?](#290-how-can-react-context-keep-large-data-alive)
- [291: How can a big closure in a useCallback or useMemo keep old data alive?](#291-how-can-a-big-closure-in-a-usecallback-or-usememo-keep-old-data-alive)
- [292: Why might a memory leak show up only after a user logs out and in again?](#292-why-might-a-memory-leak-show-up-only-after-a-user-logs-out-and-in-again)
- [293: How can switching tabs or routes in a SPA reveal leaks?](#293-how-can-switching-tabs-or-routes-in-a-spa-reveal-leaks)
- [294: What is the difference between leaks from lifecycle bugs and leaks from data growth?](#294-what-is-the-difference-between-leaks-from-lifecycle-bugs-and-leaks-from-data-growth)
- [295: How do you review code for memory leaks during a pull request?](#295-how-do-you-review-code-for-memory-leaks-during-a-pull-request)
- [296: Are there lint rules that help catch leak patterns?](#296-are-there-lint-rules-that-help-catch-leak-patterns)
- [297: How do you add memory leak checks to CI?](#297-how-do-you-add-memory-leak-checks-to-ci)
- [298: Why is a memory leak harder to find in production than locally?](#298-why-is-a-memory-leak-harder-to-find-in-production-than-locally)
- [299: How do you tell if a memory problem started with a specific deploy?](#299-how-do-you-tell-if-a-memory-problem-started-with-a-specific-deploy)
- [300: When is it OK to accept growing memory instead of fixing it?](#300-when-is-it-ok-to-accept-growing-memory-instead-of-fixing-it)

### Advanced Questions (301-450)

- [301: How is the V8 heap organized?](#301-how-is-the-v8-heap-organized)
- [302: How does the V8 Scavenger work?](#302-how-does-the-v8-scavenger-work)
- [303: How does an object get promoted to the old generation?](#303-how-does-an-object-get-promoted-to-the-old-generation)
- [304: What does the Mark-Compact collector do?](#304-what-does-the-mark-compact-collector-do)
- [305: What is Orinoco in V8?](#305-what-is-orinoco-in-v8)
- [306: What is a write barrier and why does the GC need it?](#306-what-is-a-write-barrier-and-why-does-the-gc-need-it)
- [307: What are remembered sets in V8?](#307-what-are-remembered-sets-in-v8)
- [308: What does --max-semi-space-size do and when would you tune it?](#308-what-does---max-semi-space-size-do-and-when-would-you-tune-it)
- [309: What is the difference between a high allocation rate and a memory leak?](#309-what-is-the-difference-between-a-high-allocation-rate-and-a-memory-leak)
- [310: How does DevTools compute retained size?](#310-how-does-devtools-compute-retained-size)
- [311: What is a dominator in a heap snapshot and why does it matter for leaks?](#311-what-is-a-dominator-in-a-heap-snapshot-and-why-does-it-matter-for-leaks)
- [312: How are weak references shown in a Chrome heap snapshot?](#312-how-are-weak-references-shown-in-a-chrome-heap-snapshot)
- [313: What is the shared closure context problem in V8?](#313-what-is-the-shared-closure-context-problem-in-v8)
- [314: What was the famous Meteor memory leak with closures?](#314-what-was-the-famous-meteor-memory-leak-with-closures)
- [315: How do you fix a shared closure context leak?](#315-how-do-you-fix-a-shared-closure-context-leak)
- [316: Why does using eval in a function keep its whole scope alive?](#316-why-does-using-eval-in-a-function-keep-its-whole-scope-alive)
- [317: Can an open debugger change what is kept in memory?](#317-can-an-open-debugger-change-what-is-kept-in-memory)
- [318: What are sliced strings and how can they retain memory?](#318-what-are-sliced-strings-and-how-can-they-retain-memory)
- [319: How do you force a copy of a substring so it doesn't keep the parent string?](#319-how-do-you-force-a-copy-of-a-substring-so-it-doesnt-keep-the-parent-string)
- [320: What are cons strings in V8?](#320-what-are-cons-strings-in-v8)
- [321: What are hidden classes (maps) and how do they relate to memory?](#321-what-are-hidden-classes-maps-and-how-do-they-relate-to-memory)
- [322: What is dictionary mode for objects?](#322-what-is-dictionary-mode-for-objects)
- [323: How can sparse arrays use more memory than expected?](#323-how-can-sparse-arrays-use-more-memory-than-expected)
- [324: Why can arrays of numbers use more memory than you expect?](#324-why-can-arrays-of-numbers-use-more-memory-than-you-expect)
- [325: What is pointer compression in V8?](#325-what-is-pointer-compression-in-v8)
- [326: How does marking handle WeakMap entries (ephemerons)?](#326-how-does-marking-handle-weakmap-entries-ephemerons)
- [327: What does it mean that WeakRef keeps its target alive during the current job?](#327-what-does-it-mean-that-weakref-keeps-its-target-alive-during-the-current-job)
- [328: What are the rules for the held value in FinalizationRegistry?](#328-what-are-the-rules-for-the-held-value-in-finalizationregistry)
- [329: Why shouldn't you rely on FinalizationRegistry to close important resources?](#329-why-shouldnt-you-rely-on-finalizationregistry-to-close-important-resources)
- [330: What do suspended async functions keep in memory?](#330-what-do-suspended-async-functions-keep-in-memory)
- [331: What do suspended generators keep in memory?](#331-what-do-suspended-generators-keep-in-memory)
- [332: Do promise chains keep earlier values alive?](#332-do-promise-chains-keep-earlier-values-alive)
- [333: How does Chrome collect cycles between DOM nodes and JavaScript objects?](#333-how-does-chrome-collect-cycles-between-dom-nodes-and-javascript-objects)
- [334: What were the classic Internet Explorer memory leak patterns?](#334-what-were-the-classic-internet-explorer-memory-leak-patterns)
- [335: How does the Node.js Buffer pool cause unexpected retention?](#335-how-does-the-nodejs-buffer-pool-cause-unexpected-retention)
- [336: How can slicing a Buffer retain a large amount of memory?](#336-how-can-slicing-a-buffer-retain-a-large-amount-of-memory)
- [337: What is external memory and why does it matter to the GC?](#337-what-is-external-memory-and-why-does-it-matter-to-the-gc)
- [338: How can a native addon cause a leak that heap snapshots don't show?](#338-how-can-a-native-addon-cause-a-leak-that-heap-snapshots-dont-show)
- [339: Why can RSS keep growing even when the JS heap is flat and nothing leaks?](#339-why-can-rss-keep-growing-even-when-the-js-heap-is-flat-and-nothing-leaks)
- [340: How do MALLOC_ARENA_MAX and jemalloc help with RSS growth in Node.js?](#340-how-do-malloc_arena_max-and-jemalloc-help-with-rss-growth-in-nodejs)
- [341: Why can compression with zlib cause memory fragmentation in Node.js?](#341-why-can-compression-with-zlib-cause-memory-fragmentation-in-nodejs)
- [342: What is a decompression bomb and how do you protect against it?](#342-what-is-a-decompression-bomb-and-how-do-you-protect-against-it)
- [343: How does V8 handle the large object space?](#343-how-does-v8-handle-the-large-object-space)
- [344: What is heap fragmentation inside V8?](#344-what-is-heap-fragmentation-inside-v8)
- [345: What does V8 do when the heap is close to its limit?](#345-what-does-v8-do-when-the-heap-is-close-to-its-limit)
- [346: Why does an app sometimes get very slow right before an out-of-memory crash?](#346-why-does-an-app-sometimes-get-very-slow-right-before-an-out-of-memory-crash)
- [347: What does the V8 memory reducer do?](#347-what-does-the-v8-memory-reducer-do)
- [348: Why might heap usage in a snapshot be lower than heapUsed reported a moment earlier?](#348-why-might-heap-usage-in-a-snapshot-be-lower-than-heapused-reported-a-moment-earlier)
- [349: How does an object's size get counted in a heap snapshot?](#349-how-does-an-objects-size-get-counted-in-a-heap-snapshot)
- [350: Is there a sizeof operator for JavaScript objects?](#350-is-there-a-sizeof-operator-for-javascript-objects)
- [351: How can custom async_hooks code leak memory?](#351-how-can-custom-async_hooks-code-leak-memory)
- [352: How did AsyncLocalStorage change in recent Node.js versions?](#352-how-did-asynclocalstorage-change-in-recent-nodejs-versions)
- [353: What happens to unhandled promise rejections in modern Node.js and why does it matter for memory?](#353-what-happens-to-unhandled-promise-rejections-in-modern-nodejs-and-why-does-it-matter-for-memory)
- [354: How can slow clients cause memory exhaustion on a Node.js server?](#354-how-can-slow-clients-cause-memory-exhaustion-on-a-nodejs-server)
- [355: What is load shedding based on memory and how would you implement it?](#355-what-is-load-shedding-based-on-memory-and-how-would-you-implement-it)
- [356: Why does Promise.all on a huge list cause a memory spike?](#356-why-does-promiseall-on-a-huge-list-cause-a-memory-spike)
- [357: Does using p-limit with a big array still hold memory?](#357-does-using-p-limit-with-a-big-array-still-hold-memory)
- [358: How should a Server-Sent Events endpoint clean up?](#358-how-should-a-server-sent-events-endpoint-clean-up)
- [359: How can GraphQL queries be used to exhaust server memory?](#359-how-can-graphql-queries-be-used-to-exhaust-server-memory)
- [360: What is the billion laughs attack?](#360-what-is-the-billion-laughs-attack)
- [361: Walk through how you would handle a production memory leak incident.](#361-walk-through-how-you-would-handle-a-production-memory-leak-incident)
- [362: Memory grows under high load and comes back down when load drops. Is it a leak?](#362-memory-grows-under-high-load-and-comes-back-down-when-load-drops-is-it-a-leak)
- [363: RSS keeps growing but heapUsed is flat. How do you investigate?](#363-rss-keeps-growing-but-heapused-is-flat-how-do-you-investigate)
- [364: Memory started leaking right after a Node.js major version upgrade. What do you do?](#364-memory-started-leaking-right-after-a-nodejs-major-version-upgrade-what-do-you-do)
- [365: A heap snapshot shows a huge amount of retained size in strings held by a Map in one module. What's likely going on?](#365-a-heap-snapshot-shows-a-huge-amount-of-retained-size-in-strings-held-by-a-map-in-one-module-whats-likely-going-on)
- [366: A heap snapshot shows hundreds of thousands of Promise objects. What could cause it?](#366-a-heap-snapshot-shows-hundreds-of-thousands-of-promise-objects-what-could-cause-it)
- [367: The number of Socket objects in heap snapshots keeps growing. Where would you look?](#367-the-number-of-socket-objects-in-heap-snapshots-keeps-growing-where-would-you-look)
- [368: What can you do if the leak is inside a third-party library you can't easily change?](#368-what-can-you-do-if-the-leak-is-inside-a-third-party-library-you-cant-easily-change)
- [369: When does object pooling help memory and when does it hurt?](#369-when-does-object-pooling-help-memory-and-when-does-it-hurt)
- [370: How can you reduce memory when holding a very large dataset in Node.js?](#370-how-can-you-reduce-memory-when-holding-a-very-large-dataset-in-nodejs)
- [371: Why might converting an array of objects to columnar storage save memory?](#371-why-might-converting-an-array-of-objects-to-columnar-storage-save-memory)
- [372: How does string deduplication save memory in large datasets?](#372-how-does-string-deduplication-save-memory-in-large-datasets)
- [373: What memory issues can occur in a Node.js cluster or multi-process setup?](#373-what-memory-issues-can-occur-in-a-nodejs-cluster-or-multi-process-setup)
- [374: How would you design an in-memory cache for a multi-tenant SaaS backend?](#374-how-would-you-design-an-in-memory-cache-for-a-multi-tenant-saas-backend)
- [375: What is a two-tier cache and how does it affect memory?](#375-what-is-a-two-tier-cache-and-how-does-it-affect-memory)
- [376: How can an event-sourced or replay-based system use too much memory?](#376-how-can-an-event-sourced-or-replay-based-system-use-too-much-memory)
- [377: How can you measure memory use per request or per operation in Node.js?](#377-how-can-you-measure-memory-use-per-request-or-per-operation-in-nodejs)
- [378: How do you find which endpoint leaks when you have many?](#378-how-do-you-find-which-endpoint-leaks-when-you-have-many)
- [379: How can request-scoped dependency injection leak in frameworks like NestJS?](#379-how-can-request-scoped-dependency-injection-leak-in-frameworks-like-nestjs)
- [380: How can a logger with child loggers leak?](#380-how-can-a-logger-with-child-loggers-leak)
- [381: How can the default in-memory store of a rate limiter or session library hurt you at scale?](#381-how-can-the-default-in-memory-store-of-a-rate-limiter-or-session-library-hurt-you-at-scale)
- [382: What memory problems can happen in a WebSocket server with many connections?](#382-what-memory-problems-can-happen-in-a-websocket-server-with-many-connections)
- [383: How do you handle backpressure when broadcasting to many WebSocket clients?](#383-how-do-you-handle-backpressure-when-broadcasting-to-many-websocket-clients)
- [384: How can message queue consumers run out of memory?](#384-how-can-message-queue-consumers-run-out-of-memory)
- [385: Why can a long-running Node.js script that processes files in a loop still grow in memory?](#385-why-can-a-long-running-nodejs-script-that-processes-files-in-a-loop-still-grow-in-memory)
- [386: Why can Node.js EventEmitter listeners keep a whole object graph alive in a long-lived service?](#386-why-can-nodejs-eventemitter-listeners-keep-a-whole-object-graph-alive-in-a-long-lived-service)
- [387: How can a memory leak in a dependency show up only under specific configuration?](#387-how-can-a-memory-leak-in-a-dependency-show-up-only-under-specific-configuration)
- [388: Why are active timers never garbage collected in Node.js?](#388-why-are-active-timers-never-garbage-collected-in-nodejs)
- [389: What problems can memory leaks cause in serverless platforms beyond crashes?](#389-what-problems-can-memory-leaks-cause-in-serverless-platforms-beyond-crashes)
- [390: How do you test for leaks in a serverless function?](#390-how-do-you-test-for-leaks-in-a-serverless-function)
- [391: How can the Edge or Workers runtime differ for memory leaks?](#391-how-can-the-edge-or-workers-runtime-differ-for-memory-leaks)
- [392: What are the trade-offs of using WeakRef for a cache?](#392-what-are-the-trade-offs-of-using-weakref-for-a-cache)
- [393: How do you prevent memory problems when exporting large reports from a web app?](#393-how-do-you-prevent-memory-problems-when-exporting-large-reports-from-a-web-app)
- [394: How can logging request and response bodies cause memory issues?](#394-how-can-logging-request-and-response-bodies-cause-memory-issues)
- [395: How can a server-side rendering cache leak memory?](#395-how-can-a-server-side-rendering-cache-leak-memory)
- [396: Why should you be careful with in-memory caches in auto-scaled services?](#396-why-should-you-be-careful-with-in-memory-caches-in-auto-scaled-services)
- [397: How can a feature flag SDK or config client grow memory?](#397-how-can-a-feature-flag-sdk-or-config-client-grow-memory)
- [398: How do you avoid leaks when using Node.js worker threads for CPU work?](#398-how-do-you-avoid-leaks-when-using-nodejs-worker-threads-for-cpu-work)
- [399: How does transferring an ArrayBuffer to a worker affect memory?](#399-how-does-transferring-an-arraybuffer-to-a-worker-affect-memory)
- [400: What is the difference between structured cloning and transferring for memory?](#400-what-is-the-difference-between-structured-cloning-and-transferring-for-memory)
- [401: What is a "Detached Window" in a Chrome heap snapshot?](#401-what-is-a-detached-window-in-a-chrome-heap-snapshot)
- [402: How does site isolation affect memory in Chrome?](#402-how-does-site-isolation-affect-memory-in-chrome)
- [403: How does Chrome's Memory Saver affect long-running apps?](#403-how-does-chromes-memory-saver-affect-long-running-apps)
- [404: What is Vue's effectScope and how does it help with cleanup?](#404-what-is-vues-effectscope-and-how-does-it-help-with-cleanup)
- [405: How do React 19 ref callback cleanup functions help prevent leaks?](#405-how-do-react-19-ref-callback-cleanup-functions-help-prevent-leaks)
- [406: Why is subscribing during render a leak risk in React?](#406-why-is-subscribing-during-render-a-leak-risk-in-react)
- [407: Can a React component that never commits still leak?](#407-can-a-react-component-that-never-commits-still-leak)
- [408: How does Zone.js relate to memory in Angular apps?](#408-how-does-zonejs-relate-to-memory-in-angular-apps)
- [409: How do you release memory used by a video element?](#409-how-do-you-release-memory-used-by-a-video-element)
- [410: Why should you call close() on ImageBitmap and VideoFrame objects?](#410-why-should-you-call-close-on-imagebitmap-and-videoframe-objects)
- [411: How do you free WebGL resources and contexts?](#411-how-do-you-free-webgl-resources-and-contexts)
- [412: How can an OffscreenCanvas in a worker leak memory?](#412-how-can-an-offscreencanvas-in-a-worker-leak-memory)
- [413: How do you profile memory inside a web worker?](#413-how-do-you-profile-memory-inside-a-web-worker)
- [414: How can large Blobs or downloads in the browser cause memory issues?](#414-how-can-large-blobs-or-downloads-in-the-browser-cause-memory-issues)
- [415: How can micro-frontends cause memory leaks?](#415-how-can-micro-frontends-cause-memory-leaks)
- [416: What memory problems can Module Federation shared singletons cause?](#416-what-memory-problems-can-module-federation-shared-singletons-cause)
- [417: How can an Electron app leak memory between the main and renderer processes?](#417-how-can-an-electron-app-leak-memory-between-the-main-and-renderer-processes)
- [418: How would you use real user memory data to detect a leak introduced by a release?](#418-how-would-you-use-real-user-memory-data-to-detect-a-leak-introduced-by-a-release)
- [419: How would you build a leak regression test suite for a large SPA?](#419-how-would-you-build-a-leak-regression-test-suite-for-a-large-spa)
- [420: A dashboard tab uses 1 GB after being open for 8 hours. How would you investigate?](#420-a-dashboard-tab-uses-1-gb-after-being-open-for-8-hours-how-would-you-investigate)
- [421: A detached DOM node is retained only through a React FiberNode. What does that tell you?](#421-a-detached-dom-node-is-retained-only-through-a-react-fibernode-what-does-that-tell-you)
- [422: What does "context" mean in a retainer path in a heap snapshot?](#422-what-does-context-mean-in-a-retainer-path-in-a-heap-snapshot)
- [423: What does a growing "(compiled code)" category in a heap snapshot suggest?](#423-what-does-a-growing-compiled-code-category-in-a-heap-snapshot-suggest)
- [424: What does it mean when an object is retained by "(Global handles)" or "(Internal)"?](#424-what-does-it-mean-when-an-object-is-retained-by-global-handles-or-internal)
- [425: How can you analyze heap snapshots programmatically?](#425-how-can-you-analyze-heap-snapshots-programmatically)
- [426: How do you write a custom leak filter in MemLab?](#426-how-do-you-write-a-custom-leak-filter-in-memlab)
- [427: How do you decide who owns the cleanup of a resource?](#427-how-do-you-decide-who-owns-the-cleanup-of-a-resource)
- [428: How do you design a library API so users don't leak memory with it?](#428-how-do-you-design-a-library-api-so-users-dont-leak-memory-with-it)
- [429: How does tying cleanup to an AbortSignal simplify complex components?](#429-how-does-tying-cleanup-to-an-abortsignal-simplify-complex-components)
- [430: Why do memory leaks often hide behind feature flags or rare UI paths?](#430-why-do-memory-leaks-often-hide-behind-feature-flags-or-rare-ui-paths)
- [431: How does a leak in one browser tab affect the rest of the browser?](#431-how-does-a-leak-in-one-browser-tab-affect-the-rest-of-the-browser)
- [432: Why can a page leak more memory in Safari or Firefox than in Chrome, or the other way around?](#432-why-can-a-page-leak-more-memory-in-safari-or-firefox-than-in-chrome-or-the-other-way-around)
- [433: How do Chrome's DevTools heap snapshots handle objects only reachable from DevTools?](#433-how-do-chromes-devtools-heap-snapshots-handle-objects-only-reachable-from-devtools)
- [434: Why should you take more than one snapshot after an action before concluding there is a leak?](#434-why-should-you-take-more-than-one-snapshot-after-an-action-before-concluding-there-is-a-leak)
- [435: How can a framework's own caches look like leaks in heap snapshots?](#435-how-can-a-frameworks-own-caches-look-like-leaks-in-heap-snapshots)
- [436: Why might calling a cleanup function not actually free memory?](#436-why-might-calling-a-cleanup-function-not-actually-free-memory)
- [437: How can a memory leak test give a false positive?](#437-how-can-a-memory-leak-test-give-a-false-positive)
- [438: How can a memory leak test give a false negative?](#438-how-can-a-memory-leak-test-give-a-false-negative)
- [439: Why are object counts often better than heap size for leak assertions?](#439-why-are-object-counts-often-better-than-heap-size-for-leak-assertions)
- [440: What metrics would you put on a memory dashboard for a full stack app?](#440-what-metrics-would-you-put-on-a-memory-dashboard-for-a-full-stack-app)
- [441: How can sharing large objects between requests on purpose go wrong?](#441-how-can-sharing-large-objects-between-requests-on-purpose-go-wrong)
- [442: How can an append-only audit trail kept in memory become a leak?](#442-how-can-an-append-only-audit-trail-kept-in-memory-become-a-leak)
- [443: How would you explain the difference between memory leaks in JavaScript and in C or C++?](#443-how-would-you-explain-the-difference-between-memory-leaks-in-javascript-and-in-c-or-c)
- [444: How do garbage collected server languages like Java, Go or Python compare when it comes to leaks?](#444-how-do-garbage-collected-server-languages-like-java-go-or-python-compare-when-it-comes-to-leaks)
- [445: Why are goroutine or thread leaks similar to promise leaks in JavaScript?](#445-why-are-goroutine-or-thread-leaks-similar-to-promise-leaks-in-javascript)
- [446: How can WebAssembly modules leak memory?](#446-how-can-webassembly-modules-leak-memory)
- [447: Why can't WebAssembly memory shrink, and what does that mean for long-running apps?](#447-why-cant-webassembly-memory-shrink-and-what-does-that-mean-for-long-running-apps)
- [448: How would you prevent memory leaks by design in a new full stack project?](#448-how-would-you-prevent-memory-leaks-by-design-in-a-new-full-stack-project)
- [449: What would you say in an interview about the most common memory leak you've fixed?](#449-what-would-you-say-in-an-interview-about-the-most-common-memory-leak-youve-fixed)
- [450: What are the key habits that prevent most memory leaks?](#450-what-are-the-key-habits-that-prevent-most-memory-leaks)

---

# Easy Questions (1-150)

## 1: What is a memory leak?

A memory leak happens when a program keeps memory it no longer needs and never gives it back. In JavaScript this usually means some object is still reachable from your code, so the garbage collector can't free it, even though the app will never use it again. One leak is often small, but if it happens on every click, request or page change, memory keeps growing until the app gets slow or crashes.

## 2: Can you have memory leaks in a language with a garbage collector?

Yes. A garbage collector only frees memory that nothing points to anymore. If your code still holds a reference to an object, for example in a global array, a cache or an event listener, the collector has to assume you still need it. So garbage collection removes the "forgot to call free" kind of leak, but not the "forgot to drop the reference" kind.

## 3: What is garbage collection?

Garbage collection is the automatic process that finds memory the program can no longer use and frees it. In JavaScript you never call something like `free()` yourself. The engine (V8 in Chrome and Node.js, SpiderMonkey in Firefox, JavaScriptCore in Safari) runs the collector from time to time and cleans up objects that are no longer reachable.

## 4: What does "reachable" mean in garbage collection?

An object is reachable if the program can get to it by following references starting from a root. Roots are things like global variables, the current call stack and some internal engine objects. If there is any chain of references from a root to an object, that object stays alive. If there is no such chain, the object is garbage and can be freed.

## 5: What are GC roots?

GC roots are the starting points the garbage collector uses to find live objects. In a browser they include the `window` object, global variables, local variables on the current call stack, and DOM nodes in the document. In Node.js they include the `globalThis` object, module scope that is still referenced, the stack, and handles held by the runtime like active timers and open sockets.

## 6: What is the mark-and-sweep algorithm?

Mark-and-sweep is the basic way most JavaScript engines collect garbage. In the mark phase, the collector starts from the roots and marks every object it can reach. In the sweep phase, it frees every object that was not marked. Because it works from reachability, it handles objects that point to each other in a cycle without any problem.

## 7: What is reference counting and why don't JavaScript engines use it alone?

Reference counting keeps a counter on each object for how many references point to it, and frees the object when the counter drops to zero. Its big problem is cycles: if object A points to B and B points to A, both counters stay at 1 even when nothing else uses them, so they are never freed. Old Internet Explorer versions used reference counting for DOM objects, which caused famous leaks. Modern engines use tracing collectors like mark-and-sweep instead.

## 8: Do circular references cause memory leaks in modern JavaScript?

No, not by themselves. Modern engines use tracing garbage collection, so if a group of objects only point to each other and nothing from a root points into the group, the whole group is freed. Circular references only leak when something reachable still holds one of the objects in the cycle.

## 9: What is the difference between the stack and the heap?

The stack holds function call frames: local variables, arguments and return addresses. It is small, fast and cleaned up automatically when a function returns. The heap is a larger area where objects, arrays, closures and strings live. Memory leaks in JavaScript are almost always heap leaks, because heap objects live as long as something references them.

## 10: What are the common signs that an app has a memory leak?

The most common sign is memory usage that keeps going up over time and never comes back down, even after the user leaves a page or the server finishes its requests. Other signs are the app getting slower the longer it runs, more frequent and longer garbage collection pauses, browser tabs crashing with "Aw, Snap! Out of memory", and Node.js processes dying with "JavaScript heap out of memory" or being killed by the container.

## 11: What is the difference between a memory leak and high memory usage?

High memory usage means the app uses a lot of memory, but the amount is stable. For example, a large in-memory dataset or a big cache with a size limit. A memory leak means memory keeps growing without limit as the app does the same work again and again. To tell them apart, repeat an action many times and see if memory goes back to a stable baseline or keeps climbing.

## 12: What is memory bloat?

Memory bloat is when an app uses much more memory than it should, but the amount doesn't keep growing. Examples are loading a full 50 MB JSON file when you only need a few fields, or keeping thousands of hidden DOM nodes on the page. It's not a leak, but it causes similar problems like slow pages and crashes on low-end devices.

## 13: What are the most common causes of memory leaks in browser JavaScript?

The usual ones are:

- Accidental global variables.
- Timers (`setInterval`, `setTimeout`) that are never cleared.
- Event listeners that are never removed.
- Detached DOM nodes still referenced from JavaScript.
- Closures that hold large objects longer than needed.
- Caches and maps that grow forever.
- Subscriptions (WebSockets, observables, stores) that are never closed.

## 14: What are the most common causes of memory leaks in Node.js?

The usual ones are:

- Module-level caches or maps that grow with every request.
- Event listeners added per request to a long-lived emitter.
- Timers and intervals that are never cleared.
- Storing request or user data in global variables.
- Promises that never settle and keep their closures alive.
- Unclosed streams, sockets or database connections.
- Native memory from Buffers or addons that isn't released.

## 15: What is an accidental global variable?

It's a variable that becomes a property of the global object by mistake, usually because you assigned to a name without declaring it. In sloppy mode JavaScript, `count = 5` inside a function creates `window.count` or `globalThis.count`. Globals are roots, so anything they reference is never collected.

```js
function handleClick() {
  data = new Array(1_000_000).fill(0); // no let/const, becomes a global
}
```

## 16: How does strict mode help prevent memory leaks?

In strict mode, assigning to an undeclared variable throws a `ReferenceError` instead of quietly creating a global. This catches accidental globals early. ES modules and class bodies are always in strict mode, so most modern code already has this protection. In old scripts you can add `"use strict";` at the top of the file or function.

## 17: How can a forgotten setInterval cause a memory leak?

An active interval is kept alive by the runtime, and so is its callback and everything the callback's closure references. If you start an interval in a component or a request handler and never call `clearInterval`, the callback keeps running and keeps its data in memory forever.

```js
const id = setInterval(() => {
  updateChart(bigDataset);
}, 1000);

// later, when the chart is removed
clearInterval(id);
```

## 18: Can setTimeout cause a memory leak?

A single `setTimeout` usually doesn't, because once it fires the callback is released. It can still cause problems if the delay is very long and the callback holds a lot of data, or if code keeps scheduling new timeouts in a loop (a timeout that schedules itself again) that never stops. If the work is no longer needed, call `clearTimeout`.

## 19: How do event listeners cause memory leaks?

When you add a listener, the target object keeps a reference to the callback, and the callback keeps references to whatever its closure uses. If the target lives longer than the code that added the listener, for example `window`, `document` or a global event bus, the callback and its data stay in memory until you remove the listener.

```js
function onResize() {
  layout(widget);
}

window.addEventListener("resize", onResize);
// when the widget is destroyed:
window.removeEventListener("resize", onResize);
```

## 20: Why must you pass the same function to removeEventListener?

`removeEventListener` finds the listener by comparing the function reference, the event type and the capture option. If you added an inline arrow function, you have no reference to it, so you can't remove it. Store the handler in a variable (or use an `AbortController` signal) so you can remove exactly the same function later.

```js
// this does nothing, it's a different function
el.addEventListener("click", () => save());
el.removeEventListener("click", () => save());
```

## 21: How can AbortController be used to remove event listeners?

You can pass an `AbortSignal` in the listener options. When you call `abort()`, every listener added with that signal is removed. This makes cleanup easy when one component adds many listeners.

```js
const controller = new AbortController();
const { signal } = controller;

window.addEventListener("resize", onResize, { signal });
document.addEventListener("keydown", onKey, { signal });

// cleanup
controller.abort();
```

## 22: What is the once option in addEventListener?

`{ once: true }` makes the browser remove the listener automatically after it runs the first time. It's handy for one-time events like a first click or a single `load` event, and it means you don't have to remember to clean it up. If the event never fires, though, the listener still stays attached.

## 23: What is a detached DOM node?

A detached DOM node is an element that was removed from the document but is still referenced from JavaScript. Since your code still points to it, the browser can't free it, and if it's the root of a big subtree, the whole subtree stays in memory too. Detached nodes are one of the most common leaks in single page apps.

```js
let button = document.querySelector("#save");
button.remove(); // removed from the page
// still in memory because "button" points to it
button = null; // now it can be collected
```

## 24: How can a closure cause a memory leak?

A closure keeps the variables from its outer scope alive as long as the closure itself is alive. If a long-lived function, like an event handler or a cached callback, closes over a large object, that object stays in memory even if the function never uses it again. The closure itself is fine; the leak comes from the closure living too long.

```js
function setup() {
  const hugeData = loadHugeData();
  document.addEventListener("click", () => {
    console.log(hugeData.length); // hugeData lives as long as this listener
  });
}
```

## 25: How can a cache become a memory leak?

A cache that adds entries but never removes them grows forever. For example, a `Map` keyed by user ID or URL on a server will keep every value it has ever seen. A cache needs a limit: a maximum number of entries, a time-to-live, or both. Libraries like `lru-cache` handle this for you.

## 26: What is an LRU cache?

LRU means "least recently used". An LRU cache has a maximum size, and when it's full it drops the entry that hasn't been read or written for the longest time. This keeps memory bounded while keeping the most useful entries. It's a simple way to stop a cache from turning into a leak.

## 27: What is a WeakMap?

A `WeakMap` is a map whose keys must be objects (or non-registered symbols) and are held weakly. If nothing else references a key object, the garbage collector can free it, and its entry disappears from the map. This makes `WeakMap` good for attaching extra data to objects without keeping those objects alive.

```js
const metadata = new WeakMap();

function track(el) {
  metadata.set(el, { clicks: 0 });
}
// when "el" is gone, its entry can be collected too
```

## 28: Why can't you iterate over a WeakMap?

Because entries can disappear at any time when the garbage collector runs. If you could list the keys or read the size, your code would depend on when GC runs, which is not predictable. So `WeakMap` only has `get`, `set`, `has` and `delete`.

## 29: What is a WeakSet?

A `WeakSet` is a set of objects held weakly. You can check if an object is in the set, but the set doesn't keep the object alive. It's useful for marking objects, for example "this element was already processed", without stopping them from being garbage collected.

## 30: What is a WeakRef?

A `WeakRef` holds a weak reference to an object. You call `deref()` to get the object back, and it returns `undefined` if the object was already collected. It's meant for special cases like caches of large objects. Most apps never need it, and the spec warns against using it unless you really have to.

```js
const ref = new WeakRef(bigObject);

const obj = ref.deref();
if (obj) {
  use(obj);
}
```

## 31: What is the difference between a Map and a WeakMap when it comes to memory?

A `Map` holds its keys strongly, so any object used as a key stays alive as long as the map does. A `WeakMap` holds keys weakly, so it doesn't stop them from being collected. If you use objects like DOM nodes or request objects as keys and the map lives for the whole app, use `WeakMap`, or remember to call `delete` on the `Map`.

## 32: Can console.log cause a memory leak?

Yes, in the browser when DevTools is open. The console keeps references to logged objects so you can expand and inspect them later, which keeps those objects alive. Logging large objects in a loop can make memory grow a lot during debugging. In production this matters less, but it's still a good idea to remove noisy debug logs.

## 33: What is the Chrome DevTools Memory panel?

It's the panel in Chrome DevTools for looking at JavaScript memory. It can take heap snapshots, record allocations on a timeline, run allocation sampling, and find detached elements. You use it to see what objects are in memory, how big they are, and what keeps them alive.

## 34: What is a heap snapshot?

A heap snapshot is a full picture of all objects in the JavaScript heap at one moment, including their sizes and the references between them. You can take one in the Chrome DevTools Memory panel or in Node.js with `v8.writeHeapSnapshot()`. Comparing snapshots taken before and after an action is the main way to find what's leaking.

## 35: What is the difference between shallow size and retained size?

Shallow size is the memory used by the object itself, not counting what it points to. Retained size is the memory that would be freed if this object were deleted, which includes every object that is only reachable through it. A small object with a huge retained size is often the thing holding a leak in place.

## 36: What are retainers in a heap snapshot?

Retainers are the objects that hold a reference to the selected object. In the DevTools Memory panel, the Retainers section shows the chain of references from the object back toward a GC root. Reading this chain tells you why the object is still alive, for example "array in a global cache" or "listener on window".

## 37: What is the Performance Monitor in Chrome DevTools?

The Performance Monitor is a small panel that shows live graphs of JS heap size, DOM node count, event listener count and more. You can open it from the Command Menu (Ctrl+Shift+P or Cmd+Shift+P, then type "Performance monitor"). It's a quick way to see if heap size or DOM nodes keep growing while you use the app.

## 38: How can you use the browser Task Manager to spot leaks?

Chrome has its own Task Manager (Shift+Esc on Windows and Linux, or from the Chrome menu under More tools). It shows memory used by each tab, and you can turn on a "JavaScript memory" column. If a tab's memory keeps going up while you repeat the same action, there's likely a leak. It's a rough check before you open DevTools.

## 39: Why should you force garbage collection before taking measurements?

Without a GC, memory numbers include garbage that just hasn't been collected yet, so they look higher than the real live memory. The DevTools Memory panel has a "Collect garbage" button, and taking a heap snapshot also runs a GC first. In Node.js you can start with `--expose-gc` and call `global.gc()` in tests. This gives you more stable numbers to compare.

## 40: What does process.memoryUsage() return in Node.js?

It returns an object with memory numbers in bytes:

- `rss`: total memory held by the process (resident set size).
- `heapTotal`: memory V8 reserved for the JavaScript heap.
- `heapUsed`: memory used by live JavaScript objects.
- `external`: memory for C++ objects tied to JS objects.
- `arrayBuffers`: memory for `ArrayBuffer` and `Buffer` data (also included in `external`).

```js
const { heapUsed, rss } = process.memoryUsage();
console.log(
  `heap ${Math.round(heapUsed / 1024 / 1024)} MB, rss ${Math.round(rss / 1024 / 1024)} MB`,
);
```

## 41: What is RSS?

RSS stands for resident set size. It's the amount of physical memory (RAM) the process is currently using, including the JavaScript heap, native code, Buffers, thread stacks and memory held by the allocator. Container limits and the operating system look at memory like this, so RSS is what gets your process killed, not just `heapUsed`.

## 42: What does "JavaScript heap out of memory" mean in Node.js?

It means V8 tried to allocate memory but the old generation heap had already reached its limit, and garbage collection couldn't free enough space. The process crashes with "FATAL ERROR: ... JavaScript heap out of memory". It's caused either by a leak or by the app really needing more memory than the limit allows.

## 43: What does the --max-old-space-size flag do?

It sets the maximum size, in megabytes, of V8's old generation, which is where most long-lived objects are stored. For example, `node --max-old-space-size=4096 app.js` allows about 4 GB. Raising it can fix crashes caused by real high memory needs, but if there's a leak, it only delays the crash.

## 44: Why is increasing the memory limit not a real fix for a leak?

A leak grows without limit, so any fixed amount of memory runs out sooner or later. More memory only buys time, and it can make the problem harder to notice, for example a crash every week instead of every day. It can also make GC pauses longer because there's more heap to scan. The real fix is to find and remove the reference that keeps the objects alive.

## 45: How do you check if a page leaks memory by repeating an action?

Pick one action, like opening and closing a modal or going to a page and back. Do it once to warm up, take a heap snapshot, then repeat the action many times (for example 10 or 20), and take another snapshot. If memory or the count of certain objects keeps growing with the number of repeats, something from that action is not being freed.

## 46: Why are single page apps more likely to have memory leaks than multi page apps?

In a multi page app, every navigation loads a new document and the browser throws away the old page's JavaScript heap. In a single page app the same page stays open for hours, and components are created and destroyed many times. Any reference that survives a component's destruction adds up over time, so small leaks that would never matter on a normal page become a real problem.

## 47: How do you avoid memory leaks in a React useEffect?

Return a cleanup function from the effect that undoes whatever the effect set up: remove listeners, clear timers, close connections and cancel subscriptions. React runs the cleanup before the effect runs again and when the component unmounts.

```jsx
useEffect(() => {
  const id = setInterval(() => setNow(Date.now()), 1000);
  return () => clearInterval(id);
}, []);
```

## 48: Why does React run effects twice in development with Strict Mode?

In development, Strict Mode mounts a component, runs its effects, runs their cleanups and then runs the effects again. This is done on purpose to show you effects that are missing a cleanup. If something breaks or doubles (two intervals, two socket connections), your effect probably leaks in production too. It only happens in development.

## 49: How do you cancel a fetch request when a React component unmounts?

Create an `AbortController` in the effect, pass its signal to `fetch`, and call `abort()` in the cleanup. This stops the request and makes sure you don't hold on to the response or update state after the component is gone.

```jsx
useEffect(() => {
  const controller = new AbortController();
  fetch(`/api/users/${id}`, { signal: controller.signal })
    .then((res) => res.json())
    .then(setUser)
    .catch((err) => {
      if (err.name !== "AbortError") throw err;
    });
  return () => controller.abort();
}, [id]);
```

## 50: Does setting state on an unmounted React component cause a memory leak?

Older React versions showed a warning saying it "indicates a memory leak", but React 18 removed that warning because in most cases it wasn't a real leak. A finished promise that calls `setState` once is harmless. The real leak is a subscription, timer or listener that keeps calling `setState` forever because it was never cleaned up. Fix the missing cleanup, not the warning.

## 51: How do you avoid memory leaks with RxJS subscriptions in Angular?

Every manual `subscribe()` on a long-lived observable must be stopped when the component is destroyed. The simple options are:

- Use the `async` pipe in the template, which unsubscribes for you.
- Use `takeUntilDestroyed()` from `@angular/core/rxjs-interop`.
- Store the `Subscription` and call `unsubscribe()` in `ngOnDestroy`.

```ts
export class PriceComponent {
  constructor(private prices: PriceService) {
    this.prices.stream$
      .pipe(takeUntilDestroyed())
      .subscribe((p) => (this.price = p));
  }
}
```

## 52: Do you need to unsubscribe from Angular HttpClient requests?

Usually not. `HttpClient` observables emit one response and then complete, which ends the subscription. You still might want to cancel a slow request when the user leaves the page, to avoid extra work and running code after the component is gone. Long-lived observables like store selectors, `interval`, router events or WebSocket streams always need cleanup.

## 53: How do you clean up in a Vue component?

Use `onUnmounted` (or `onBeforeUnmount`) in the Composition API, or `unmounted` in the Options API, to remove listeners, clear timers and close subscriptions you created manually. Watchers created with `watch` inside `setup` stop automatically when the component unmounts, but ones created outside a component or asynchronously need to be stopped by calling the function that `watch` returns.

```js
import { onMounted, onUnmounted } from "vue";

onMounted(() => window.addEventListener("scroll", onScroll));
onUnmounted(() => window.removeEventListener("scroll", onScroll));
```

## 54: Why do third-party libraries often need a destroy method call?

Libraries like charts, maps, rich text editors and date pickers often add their own listeners, timers, observers and DOM nodes. If you remove the container element without calling the library's `destroy()`, `dispose()` or similar method, those things stay behind. Always check the library docs and call its cleanup method when your component unmounts.

## 55: How can WebSockets cause memory leaks?

A WebSocket keeps its connection and its message handlers alive until you close it. If a component opens a socket and never calls `close()`, the handlers and everything they reference stay in memory, and new sockets pile up each time the component mounts. On the server, keeping closed or dead connections in a list of clients is a common leak too.

## 56: What is URL.createObjectURL and why can it leak memory?

`URL.createObjectURL(blob)` creates a URL that points to a `Blob` or `File` in memory, for example to preview an uploaded image. The browser keeps the blob alive as long as the URL exists, which is until the document is unloaded. In a long-lived page, call `URL.revokeObjectURL(url)` when you no longer need it.

```js
const url = URL.createObjectURL(file);
img.src = url;
img.onload = () => URL.revokeObjectURL(url);
```

## 57: Do IntersectionObserver and ResizeObserver need cleanup?

Yes. An observer keeps references to its callback and to the elements it observes. Call `unobserve(el)` for single elements or `disconnect()` when you're done with the whole observer, usually when the component unmounts. The same goes for `MutationObserver`, which only has `disconnect()`.

```js
const observer = new ResizeObserver(onResize);
observer.observe(panel);
// cleanup
observer.disconnect();
```

## 58: Do Web Workers leak memory if you don't terminate them?

A dedicated worker runs in its own thread with its own heap. If you create a worker and never call `worker.terminate()` (or `self.close()` inside the worker), it keeps running and keeps its memory, even if the page doesn't use it anymore. Creating a new worker every time a component mounts without terminating the old one is a common leak.

## 59: What is an EventEmitter leak in Node.js?

It happens when code keeps adding listeners to a long-lived `EventEmitter`, often once per request or per connection, and never removes them. Each listener and its closure stay in memory. Node.js warns about this when an emitter gets more than 10 listeners for the same event.

```js
// leak: a new listener on a global emitter for every request
app.get("/data", (req, res) => {
  bus.on("update", (u) => console.log(req.url, u));
  res.send("ok");
});
```

## 60: What is MaxListenersExceededWarning?

It's a warning Node.js prints when more than 10 listeners (the default) are added for the same event on one emitter. It's a hint that you may be adding listeners in a loop or per request without removing them. You can raise the limit with `emitter.setMaxListeners(n)` if many listeners are expected, but first check that it's not a leak.

## 61: How do you remove a listener from a Node.js EventEmitter?

Call `emitter.off(eventName, listener)` or its alias `removeListener`, with the same function you added. To remove all listeners for an event, use `removeAllListeners(eventName)`, but be careful, since it also removes listeners that other code added. If the listener should run once, use `once` instead.

```js
function onData(chunk) {
  /* ... */
}
stream.on("data", onData);
// later
stream.off("data", onData);
```

## 62: Why is storing request data in a global variable a leak in Node.js?

A Node.js server is one long-running process that handles many requests. Anything you put in a module-level variable or `globalThis` lives as long as the process. If you push request data, user objects or responses into a global array or map and never remove them, memory grows with every request until the process crashes.

## 63: Why is the default express-session MemoryStore not for production?

The Express session docs say the default `MemoryStore` is meant for development only. It keeps all sessions in the Node.js process memory, it leaks memory under most conditions, and it doesn't scale past one process. In production, use a store like Redis, a database, or another supported session store.

## 64: How can unclosed database connections cause problems?

Each open connection uses memory on the client and on the database server. If code opens a new connection or creates a new client per request and never closes it, connections and their buffers pile up until you hit memory limits or the database's connection limit. Use a connection pool, create it once, and always release connections back to the pool.

## 65: What is a connection pool?

A connection pool is a set of open database connections that your app reuses. When code needs a connection, it borrows one from the pool and returns it when done. This saves the cost of opening connections and keeps the number of connections, and their memory, under a fixed limit.

## 66: Can unclosed streams cause memory leaks in Node.js?

Yes. A stream that is never finished or destroyed keeps its buffers, file handles and listeners in memory. If you read a file or a request body and stop early, call `stream.destroy()`. Using `pipeline` from `node:stream/promises` helps because it destroys all streams in the chain when one fails or finishes.

```js
import { pipeline } from "node:stream/promises";
import { createReadStream, createWriteStream } from "node:fs";
import { createGzip } from "node:zlib";

await pipeline(
  createReadStream("in.log"),
  createGzip(),
  createWriteStream("in.log.gz"),
);
```

## 67: What happens to memory when you set a variable to null?

Setting a variable to `null` removes that one reference to the object. If it was the last reference, the object becomes unreachable and the garbage collector can free it the next time it runs. If other references still exist, nothing changes. You don't need to set local variables to `null` at the end of a function, since they go away when the function returns.

## 68: Does the delete operator free memory?

`delete obj.prop` removes a property from an object, which drops that object's reference to the value. If nothing else references the value, it can then be collected. `delete` doesn't free memory directly, and it can't delete variables declared with `let`, `const` or `var`. For maps, use `map.delete(key)`.

## 69: How do you empty an array or a Map so its items can be garbage collected?

For arrays, set `arr.length = 0` or assign a new empty array. Setting the length clears the existing array for everyone who holds a reference to it, while reassigning only changes your variable. For a `Map` or `Set`, call `clear()`. After that, the old items can be collected if nothing else points to them.

## 70: What is a minor GC and a major GC?

V8 splits the heap into a young generation for new objects and an old generation for objects that survived a few collections. A minor GC (scavenge) cleans only the young generation. It's fast and runs often. A major GC (mark-compact) cleans the whole heap. It's slower and runs less often. Leaked objects survive minor GCs and end up in the old generation.

## 71: What is the generational hypothesis?

It's the idea that most objects die young. Things like temporary strings, arrays inside a loop or small objects in a function are usually garbage soon after they are created. Engines use this by collecting the young generation often and cheaply, and checking older objects less often.

## 72: What is a GC pause?

A GC pause is a moment when the JavaScript main thread stops running your code so the garbage collector can do work. Modern engines do most work on background threads to keep pauses short, but some pauses are still needed. A leak makes the heap larger, so major GCs take longer and happen more often, which can cause jank in the browser or slow responses on a server.

## 73: Why does a memory leak make an app slower before it crashes?

A larger heap means more work for the garbage collector. As memory grows, the engine runs GC more often and each major GC has more objects to mark. The main thread spends more time in GC and less time running your code. On devices with low RAM, the system may also start swapping, which is very slow.

## 74: How do you open the DevTools Memory panel?

Open Chrome DevTools (F12, or Ctrl+Shift+I on Windows and Linux, Cmd+Option+I on macOS) and click the Memory tab. If you don't see it, use the "more tabs" arrow. From there, pick a profiling type such as Heap snapshot, Allocations on timeline, Allocation sampling or Detached elements, and click the start or take button.

## 75: What profiling types are in the Chrome Memory panel?

The main ones are:

- **Heap snapshot**: a full picture of memory at one moment.
- **Allocations on timeline**: records allocations over time and shows which ones are still alive.
- **Allocation sampling**: low-overhead sampling of which functions allocate memory.
- **Detached elements**: lists DOM elements that are removed from the page but still retained.

## 76: What views does a heap snapshot have in Chrome DevTools?

A snapshot can be shown in several views:

- **Summary**: objects grouped by constructor name.
- **Comparison**: the difference between two snapshots.
- **Containment**: the object tree starting from roots like `window`.
- **Statistics**: a chart of memory by type.

Summary and Comparison are the ones you use most when looking for leaks.

## 77: What is the Comparison view in a heap snapshot?

The Comparison view shows the difference between the current snapshot and an earlier one. For each constructor it lists how many objects were added, deleted and the size change. If you repeat an action 10 times and see about 10 or 100 new objects of some type that were never deleted, those are leak candidates.

## 78: What does "Detached" mean in a heap snapshot?

DevTools marks DOM nodes as "Detached" when they're no longer in the document tree but are still kept in memory by something. You can type "Detached" in the class filter of the Summary view to find them, or use the "Detached elements" profiling type. Then look at the retainers to see what JavaScript is holding them.

## 79: How do you take a heap snapshot in Node.js?

There are a few ways:

- Call `v8.writeHeapSnapshot()` from code. It writes a `.heapsnapshot` file and returns its name.
- Start Node with `--heapsnapshot-signal=SIGUSR2` and send that signal to the process.
- Connect Chrome DevTools with `--inspect` and use its Memory tab.

You can open the file in the Chrome DevTools Memory panel by loading it.

```js
import v8 from "node:v8";

const file = v8.writeHeapSnapshot();
console.log(`Snapshot written to ${file}`);
```

## 80: How do you connect Chrome DevTools to a Node.js process?

Start Node with `node --inspect app.js` (or `--inspect-brk` to pause on the first line). Then open `chrome://inspect` in Chrome and click "inspect" under your target, or click the Node.js icon in DevTools. You get the same Memory and Performance tools you use for web pages.

## 81: Does taking a heap snapshot affect the app?

Yes. Taking a snapshot stops the JavaScript thread while it walks the whole heap, and it needs extra memory, which can be about as large as the heap itself. On a big production server that can mean a pause of many seconds, or even an out-of-memory crash. Do it on one instance taken out of the load balancer, or in a test environment that reproduces the leak.

## 82: What are the steps to fix a memory leak?

1. Confirm there is a leak: memory keeps growing under the same repeated work.
2. Find a reliable way to reproduce it.
3. Take heap snapshots before and after repeating the action, and compare them.
4. Find the objects that grow and follow their retainers to the reference that keeps them alive.
5. Fix the code: remove the listener, clear the timer, bound the cache and so on.
6. Repeat the test to make sure memory now stays flat.

## 83: How do memory leaks affect mobile users?

Phones have less memory than laptops, and mobile browsers kill or reload tabs more aggressively when memory runs low. A leak that's fine on your 32 GB dev machine can make a page crash or reload on a cheap phone after a few minutes. Always test long sessions on real or throttled devices.

## 84: Can loading too many images cause memory problems?

Yes. A decoded image uses much more memory than its file size, roughly width times height times 4 bytes. A 4000 by 3000 photo takes about 48 MB when decoded, even if the JPEG is 2 MB. Showing many large images in a long list or keeping them in a JavaScript array can use a lot of memory. Serve images at the size you show them and use lazy loading.

## 85: How does infinite scroll cause memory growth?

Infinite scroll keeps adding new items to the page and often to a JavaScript array, but never removes the old ones. After a long session you may have thousands of DOM nodes and a lot of data in memory. The fix is virtualization (only render the rows on screen) and capping how much data you keep.

## 86: What is list virtualization?

List virtualization (also called windowing) means rendering only the rows that are visible on screen plus a small buffer, instead of every row in the list. As the user scrolls, rows are reused or swapped. This keeps the DOM node count small no matter how long the list is. Libraries like TanStack Virtual and react-window do this.

## 87: Can a global state store like Redux leak memory?

A store isn't a leak by itself, but it lives for the whole app, so anything you put in it stays forever unless you remove it. Common problems are caching every API response without ever clearing old ones, storing large blobs or DOM references, and keeping full history for undo. Remove data that a page no longer needs and keep the store normalized.

## 88: How can an undo history leak memory?

An undo feature saves past states so the user can go back. If it saves a full copy of a large document on every change and never limits the number of steps, memory grows with every keystroke. Limit the history to a fixed number of entries, or store small diffs instead of full copies.

## 89: Does localStorage cause memory leaks?

Not in the usual sense. `localStorage` is stored on disk, has a size limit of about 5 MB per origin, and is not part of the JavaScript heap. The risk is reading a large value and keeping the parsed object around, or filling storage until writes throw a `QuotaExceededError`. Leaks in this area usually come from in-memory copies, not from storage itself.

## 90: What is performance.memory and should you use it?

`performance.memory` is a non-standard, Chrome-only property that shows heap size numbers like `usedJSHeapSize`. It's deprecated, the numbers are coarse, and other browsers don't support it. The standard replacement is `performance.measureUserAgentSpecificMemory()`, which is more accurate but only works on cross-origin isolated pages.

## 91: Do other browsers have memory tools?

Yes. Firefox DevTools has a Memory panel that takes snapshots and shows a dominators view, and `about:memory` gives a detailed report for the whole browser. Safari's Web Inspector has a Timelines tab with JavaScript allocations and heap snapshots. Chrome's tools are the most common in interviews, but the same ideas apply in all of them.

## 92: Can iframes cause memory leaks?

Yes. Each iframe has its own document and JavaScript heap. If you remove an iframe but your main page still holds a reference to its `contentWindow`, its document or objects created inside it, the whole iframe's memory can stay alive. Remove listeners you added across frames and drop those references when the iframe is removed.

## 93: How can a memoized function leak memory?

Memoization stores results in a cache keyed by the arguments. If the function is called with many different arguments, the cache grows forever. A memoize helper with no limit on a function that gets user IDs, dates or search strings is a slow leak. Use a size limit, an LRU cache or a `WeakMap` when the arguments are objects.

## 94: What is the problem with an unbounded array of logs in memory?

Some apps keep logs, errors or analytics events in an array to send later or show in a debug panel. If the array is never trimmed or flushed, it grows for the whole session or the whole life of the server process. Keep a fixed size buffer (for example the last 500 items) or send and clear the buffer on a schedule.

## 95: Can logging libraries cause memory growth in Node.js?

Yes, in some setups. If logs are written faster than the output (a file, a network target or a slow terminal) can accept them, the library buffers them in memory. Under heavy load this buffer can grow large. Use async logging that drops or blocks when the buffer is full, and avoid logging huge objects on every request.

## 96: What is the difference between a memory leak and a resource leak?

A memory leak is about heap memory that's never freed. A resource leak is about other limited things that are not released: file descriptors, sockets, database connections, timers or threads. They often happen together, for example an unclosed socket also keeps its buffers and handlers in memory. Both are fixed by releasing the resource when you're done.

## 97: What does "EMFILE: too many open files" mean?

It means the Node.js process hit the operating system's limit on open file descriptors. Files, sockets and pipes all count. It's often caused by a resource leak: files or connections that are opened but never closed. Raising the limit can help in some cases, but first make sure your code closes what it opens.

## 98: Why is garbage collection not predictable in JavaScript?

The engine decides when to run GC based on its own heuristics, like how much memory was allocated and how busy the thread is. There's no standard API to force or schedule it in normal code. That's why you shouldn't build logic that depends on an object being collected at a certain time, and why `WeakRef` and `FinalizationRegistry` give no timing guarantees.

## 99: Do closures always keep their entire scope alive?

Not always. Modern engines like V8 try to keep only the variables a closure actually uses. But all closures created in the same scope share one context object, so if one closure uses a big variable, every closure from that scope can keep it alive. You shouldn't rely on the engine removing unused variables.

## 100: How can a closure inside a loop cause memory growth?

If a loop creates a closure on every iteration and stores each one somewhere long-lived, like an array of handlers or a global emitter, every closure keeps its own copy of the loop variables. That's fine for small loops, but if the loop runs on every request or every frame and the closures are never removed, they pile up.

## 101: What does a "sawtooth" memory graph mean?

A sawtooth graph goes up as the app allocates objects, then drops sharply when the garbage collector runs, again and again. This is normal and healthy. What you want to check is the low points after each drop. If they stay at the same level, there's no leak. If each low point is higher than the last one, memory is leaking.

## 102: What does a "staircase" memory graph usually mean?

A staircase graph steps up after each action and never comes back down, even after GC. For example, memory jumps every time a modal opens and stays there after it closes. That pattern strongly suggests each action leaves something behind, which is the classic sign of a leak.

## 103: What is OOMKilled in Kubernetes?

OOMKilled means the container used more memory than its limit, so the Linux kernel's out-of-memory killer stopped it. Kubernetes shows this as the reason the container was terminated, with exit code 137. In a Node.js app it often happens without any "heap out of memory" error, because the container limit was reached before V8's heap limit.

## 104: What does exit code 137 mean?

Exit code 137 means the process was killed with signal 9 (`SIGKILL`), because 128 + 9 = 137. In containers this almost always means the out-of-memory killer stopped it for going over its memory limit. It's a strong hint to check for leaks or to set Node's heap limit below the container limit.

## 105: Why do restarts hide memory leaks?

If a server restarts often, for example on every deploy or when a process manager restarts it at a memory limit, a slow leak never gets big enough to crash anything. The leak is still there, and it shows up as soon as deploys become less frequent or traffic goes up. Tools like PM2's `max_memory_restart` are a safety net, not a fix.

## 106: Can serverless functions have memory leaks?

Yes. Serverless platforms like AWS Lambda reuse the same instance for many invocations while it's warm. Anything stored in module scope, like a global array or cache, survives between invocations. If it grows every time, the instance will eventually run out of memory. Treat module scope in a serverless function like a long-running server.

## 107: Does TypeScript prevent memory leaks?

No. TypeScript checks types at compile time, but the compiled JavaScript runs the same way and is garbage collected the same way. A forgotten listener, timer or global cache leaks just the same in TypeScript. Some lint rules can catch patterns like floating promises, but leaks are about object lifetimes, which the type system doesn't track.

## 108: Why should you test memory in an incognito window or a clean profile?

Browser extensions run code in your pages and can create their own objects, listeners and DOM nodes. That shows up in heap snapshots and makes it look like your app leaks when it doesn't, or hides real leaks in noise. A clean profile or an incognito window with extensions disabled gives cleaner results.

## 109: Does Lighthouse detect memory leaks?

No. Lighthouse loads a page once and measures load performance, accessibility, SEO and best practices. Memory leaks happen over time as the user interacts with the app, which Lighthouse doesn't do. To find leaks you need repeated interactions and heap snapshots, either by hand or with a tool like MemLab.

## 110: What is MemLab?

MemLab is an open source tool from Meta for finding memory leaks in web pages. You write a scenario that says how to go to a page, do an action and undo it. MemLab runs it in headless Chrome, takes heap snapshots, compares them and reports objects that leaked along with their retainer traces. It's useful for running leak checks in CI.

## 111: What is event delegation and how does it help memory?

Event delegation means adding one listener to a parent element instead of one listener on each child. The handler checks `event.target` to see which child was clicked. Fewer listeners means less memory, and you don't need to add or remove listeners when child elements are added or removed.

```js
list.addEventListener("click", (e) => {
  const item = e.target.closest("li");
  if (item) select(item.dataset.id);
});
```

## 112: Do you need to remove listeners from elements before removing them from the page?

In modern browsers, no, as long as nothing else references the element or the listener. If an element is removed and becomes unreachable, its listeners are collected with it. You do need to remove listeners added to long-lived targets like `window`, `document` or a parent that stays on the page, and listeners whose handler is also referenced from somewhere else.

## 113: Does requestAnimationFrame need cleanup?

Yes, if it runs in a loop. A rAF loop calls itself every frame, so it never stops on its own. If a component starts one and is removed without calling `cancelAnimationFrame`, the loop keeps running and keeps its closure alive.

```js
let frameId;
function tick() {
  draw();
  frameId = requestAnimationFrame(tick);
}
frameId = requestAnimationFrame(tick);
// cleanup
cancelAnimationFrame(frameId);
```

## 114: How do you release a camera or microphone stream?

Call `stop()` on every track of the `MediaStream`. Just removing the video element or setting `srcObject` to `null` doesn't release the device. If you don't stop the tracks, the camera light stays on and the browser keeps the stream and its buffers in memory.

```js
stream.getTracks().forEach((track) => track.stop());
video.srcObject = null;
```

## 115: Why can reading a whole file into memory be a problem in Node.js?

`fs.readFile` loads the entire file into one Buffer. For a few kilobytes that's fine, but a 2 GB log file needs 2 GB of memory, and many requests doing this at the same time can crash the server. Use streams to process large files in small chunks so memory stays flat.

## 116: Why is loading all rows from a database at once risky?

A query like `SELECT * FROM orders` with no limit can return millions of rows, and the driver or ORM builds an object for each row in memory. Memory spikes, GC pauses get long and the process may crash. Use pagination, cursors or streaming for large result sets, and select only the columns you need.

## 117: Can building a large string cause memory problems?

Yes. Strings are immutable, so building a huge string by adding pieces in a loop creates many intermediate strings and puts pressure on the GC. V8 also has a maximum string length (about 512 MB on 64-bit systems), and going over it throws "Invalid string length". For large outputs, write to a stream or join an array of parts at the end.

## 118: What does "Invalid string length" mean in JavaScript?

It's a `RangeError` thrown when a string would go over the engine's maximum string length. It often happens when you `JSON.stringify` a very large object, concatenate log output without limit, or read a huge file as one string. It's a sign you should stream or split the data instead of keeping it as one string.

## 119: What is a singleton and how can it leak memory?

A singleton is an object that exists only once for the whole app, like a service, a store or a module-level instance. Since it lives forever, anything it collects in arrays or maps also lives forever. Singletons are fine, but any list they keep needs a way to remove items.

## 120: How does the Node.js module cache relate to memory?

When you `require` or `import` a module, Node.js runs it once and caches the result. Any state at module level, like `const cache = new Map()`, is shared across the whole process and lives as long as the process. That makes module-level state behave like a global, so it needs the same care.

## 121: What does timer.unref() do in Node.js?

`unref()` tells Node.js not to keep the process running just because this timer exists. The timer still fires if the process is alive for other reasons. It's useful for background timers like cache cleanup, so they don't stop the process from exiting. It doesn't free memory by itself; you still need `clearInterval` to stop a timer you no longer need.

## 122: What is AbortSignal.timeout()?

`AbortSignal.timeout(ms)` returns a signal that aborts on its own after the given time. You can pass it to `fetch` and other APIs to set a timeout without creating and clearing your own `setTimeout`. This avoids the common leak where a manual timeout timer is left running after the request finished.

```js
const res = await fetch(url, { signal: AbortSignal.timeout(5000) });
```

## 123: How can Promise.race with a timeout leak a timer?

A common pattern races a request against a `setTimeout` promise. If the request wins, the timer is still scheduled and keeps its closure alive until it fires. With a long timeout and many requests, lots of timers pile up. Clear the timer when the race is settled, or use `AbortSignal.timeout`.

```js
let timer;
const timeout = new Promise((_, reject) => {
  timer = setTimeout(() => reject(new Error("timeout")), 30_000);
});
try {
  return await Promise.race([doWork(), timeout]);
} finally {
  clearTimeout(timer);
}
```

## 124: What is the "Collect garbage" button in Chrome DevTools?

It's the trash can icon in the Memory panel (and in the Performance panel). Clicking it forces a full garbage collection right away. Use it before you look at memory numbers so you only see objects that are really alive, not garbage that's waiting to be collected.

## 125: Can CSS cause memory leaks?

Not in the usual JavaScript sense, since CSS doesn't hold references to objects. But CSS can increase memory use, for example by promoting many elements to their own compositor layers with `will-change` or 3D transforms, which uses GPU memory. Adding style elements in a loop without removing them can also grow memory over time.

## 126: What is a GPU memory leak in a web app?

Some resources live in GPU memory, like WebGL textures and buffers, canvas backing stores and compositor layers. If you create WebGL textures or buffers and never delete them, or create many large canvases, GPU memory grows. In WebGL you free resources with calls like `gl.deleteTexture()` and `gl.deleteBuffer()`. Libraries like Three.js have `dispose()` methods for this.

## 127: How do you release memory used by a canvas?

A canvas keeps a bitmap of its size, so a 4000 by 4000 canvas uses about 64 MB. To release it, remove references to the canvas element and its context. A common trick is to set its `width` and `height` to 0 before dropping it, which makes the browser free the bitmap right away. Creating many temporary canvases in a loop and keeping them in arrays is a common source of growth.

## 128: What happens to memory when a user closes a browser tab?

The browser destroys the tab's renderer process or its document, which frees all its JavaScript heap, DOM and other memory. That's why leaks in normal websites often go unnoticed: people close tabs. The problem shows up in apps that stay open for hours, like dashboards, email clients and chat apps.

## 129: What is bfcache and how does it relate to memory?

The back/forward cache (bfcache) keeps a full copy of a page in memory when the user leaves it, so going back is instant. The page is frozen, not destroyed. Pages with open connections or certain listeners, like `unload`, may not be eligible. It's not a leak, but it means a page's memory can stay around for a while after navigation.

## 130: Why should you avoid the unload event?

The `unload` event is unreliable, especially on mobile, and having an `unload` listener can stop a page from using the back/forward cache. Use `pagehide` or `visibilitychange` to save state or send analytics instead. This is about reliability and performance, but it's often asked together with page lifecycle and cleanup.

## 131: What is a memory budget?

A memory budget is a target for how much memory a page or service is allowed to use, for example "the dashboard must stay under 200 MB of JS heap after one hour". It turns vague concerns into something you can test. Teams check it in performance tests and alert in monitoring when it's exceeded.

## 132: How do you monitor memory of a Node.js app in production?

Report `process.memoryUsage()` numbers (`rss`, `heapUsed`, `external`) to your metrics system on a regular interval, and graph them over time. Most APM tools and the OpenTelemetry runtime metrics for Node.js do this for you. Set alerts on steady growth and on getting close to the container limit, not just on crashes.

## 133: Why should you look at memory trends over days, not minutes?

Many leaks are slow, a few kilobytes per request. Over a few minutes memory looks flat because normal GC noise is larger than the leak. Over days, the low points keep rising. Looking at long time ranges, and comparing memory after the same amount of traffic, shows slow leaks that short tests miss.

## 134: What is heap size versus heap used?

Heap size (`heapTotal` in Node.js) is how much memory V8 has reserved for the heap. Heap used (`heapUsed`) is how much of that is filled with live objects and garbage that hasn't been collected yet. V8 grows and shrinks the reserved size as needed, so a high heap size with low heap used just means the engine kept some free space.

## 135: Why doesn't memory go down right away after you free objects?

Two reasons. First, garbage is only freed when the GC runs, which may be later. Second, even after GC, the engine and the memory allocator often keep the freed memory reserved for future use instead of giving it back to the operating system. So RSS can stay high for a while. What matters is whether memory keeps growing, not whether it drops instantly.

## 136: What are global variables in ES modules?

Top-level `let`, `const` and `function` in an ES module are scoped to that module, not added to the global object. But the module itself stays loaded for the whole life of the app, so its top-level variables live just as long as real globals. A module-level array that you keep pushing to leaks the same way a global would.

## 137: How do you find which objects are growing in a heap snapshot?

Take a snapshot, repeat the suspect action several times, then take another snapshot. Switch the second one to the Comparison view and sort by "# Delta" or "Size Delta". Constructors with a large positive delta that matches the number of repeats, like 10 new `ChatMessage` objects after 10 repeats, are where you start looking.

## 138: What does the Distance column mean in a heap snapshot?

Distance is the number of references on the shortest path from a GC root to the object. Objects with small distance are close to globals or the window. When looking for leaks, it helps you spot which objects are held by something near the top, which is often the place where the leak starts.

## 139: Why do some objects in heap snapshots have names in parentheses?

Names like `(closure)`, `(array)`, `(string)`, `(compiled code)` and `(system)` are internal groups, not your own classes. For example `(closure)` groups function objects and `(array)` groups V8's internal arrays. Your own classes show up by their constructor name, which is one reason using classes or named constructors makes snapshots easier to read.

## 140: Why does naming your functions help when debugging memory?

In heap snapshots and allocation profiles, anonymous functions show up with no useful name, which makes retainer chains hard to read. Named functions and named classes show up with their names, so you can quickly see "`onResize` in `window` listeners" instead of an anonymous function. It's a small habit that saves time.

## 141: Can a memory leak happen in the server rendering of a React or Next.js app?

Yes. Server rendering runs your component code in a long-running Node.js process. If code puts per-request data into module-level variables, global stores or caches without limits, that data stays after the request ends. Each request adds more, and the server eventually runs out of memory.

## 142: Can a development server leak memory while a production build does not?

Yes. Dev servers with hot module replacement re-run modules on every change. If a module creates a database client, opens a connection or adds a listener at the top level, each reload creates a new one while the old ones stay alive. That's why some guides store a single client on `globalThis` in development, for example the common Prisma client pattern.

## 143: What is the Prisma client hot-reload problem in Next.js?

In development, Next.js reloads modules on every change. If you write `const prisma = new PrismaClient()` at module level, each reload creates a new client with its own connection pool, which can exhaust database connections and memory. The common fix is to keep one client on `globalThis` in development.

```ts
import { PrismaClient } from "@prisma/client";

const globalForPrisma = globalThis as unknown as { prisma?: PrismaClient };

export const prisma = globalForPrisma.prisma ?? new PrismaClient();

if (process.env.NODE_ENV !== "production") globalForPrisma.prisma = prisma;
```

## 144: How do you clean up a jQuery plugin or jQuery data?

jQuery stores event handlers and `.data()` values in its own internal storage. Using jQuery's `.remove()` or `.empty()` cleans that storage for the removed elements, but removing elements with plain DOM methods like `el.remove()` or `innerHTML = ""` does not. In old jQuery apps, mixing plain DOM removal with jQuery data is a common source of leaks.

## 145: What is the difference between remove() and detach() in jQuery?

Both take elements out of the page. `.remove()` also deletes jQuery data and event handlers for those elements, so they can be freed. `.detach()` keeps the data and handlers because you plan to put the elements back later. If you `detach()` and never reinsert or drop the elements, you keep them in memory.

## 146: How can a chat or live feed app leak memory?

Chat and live feeds keep receiving new messages. If the app adds every message to the DOM and to an array forever, a long session holds thousands of messages and nodes. Common fixes are keeping only the last N messages in memory, virtualizing the list and loading older messages on demand when the user scrolls up.

## 147: Can a memory leak cause a security problem?

Yes. A leak that grows with each request can be used for denial of service: an attacker sends many requests until the server runs out of memory. Leaks can also keep sensitive data like tokens or personal data in memory longer than expected, which matters if memory is dumped, for example in heap snapshots shared for debugging.

## 148: Is it safe to share heap snapshots?

Be careful. A heap snapshot contains every string and object in memory, which can include passwords, API keys, session tokens, user emails and other personal data. Treat snapshots from production like a database dump: store them securely, share them only with people who need them, and delete them when you're done.

## 149: What is memory pressure?

Memory pressure is when the system is running low on free memory. The browser or operating system reacts by freeing caches, discarding background tabs, running GC more aggressively or killing processes. On mobile, a page under memory pressure may be reloaded when the user returns to it.

## 150: What is a good first step when someone reports that an app gets slow after a while?

Try to reproduce it and watch memory while you do. Open the Performance Monitor or Task Manager, repeat what the user was doing for several minutes, and see if JS heap size, DOM nodes or listener count keep growing. If they do, you likely have a leak and can move on to heap snapshots. If they don't, look at other causes like CPU work or slow network calls.

# Moderate Questions (151-300)

## 151: What is the three-snapshot technique?

It's a simple way to separate real leaks from normal one-time allocations:

1. Load the page, warm it up, and take snapshot 1.
2. Do the action and undo it (open and close a dialog), then take snapshot 2.
3. Do the same action again, then take snapshot 3.

Objects that were allocated between snapshot 1 and 2 and are still alive in snapshot 3 are strong leak candidates. In DevTools you can select snapshot 3 and filter to "Objects allocated between Snapshot 1 and Snapshot 2".

## 152: How do you read a retainer path to find the cause of a leak?

Select a leaked object in a snapshot and look at the Retainers panel. Each row is an object that references the one below it, going up toward a GC root. Skip internal rows like `(system)` or `(internal array)` and look for the first thing you recognize from your code, like a property name on your service, a listener list on `window` or a key in a `Map`. That object is usually where you need to remove the reference.

## 153: How do you use Allocations on timeline in Chrome DevTools?

Pick "Allocations on timeline", start recording, do the suspect action a few times and stop. The chart shows a bar for each burst of allocations. Blue parts are objects that are still alive at the end, and gray parts were collected. Blue bars that keep showing up for each action point to objects that are never freed. Select a bar to see which constructors were allocated in that time.

## 154: When would you use Allocation sampling instead of a heap snapshot?

Allocation sampling records which functions allocate memory, with low overhead, over a longer period. It's good for finding code that allocates a lot, for example a hot function creating many temporary objects, and it can run on bigger apps where full snapshots are too slow. A heap snapshot is better for finding what is still alive and why, which is what you need for leaks.

## 155: What is the Detached elements profile in Chrome DevTools?

It's a profiling type in the Memory panel that lists DOM elements that are detached from the document but still kept alive by JavaScript. It groups them by their detached subtree and lets you jump to their retainers. It's faster than filtering a full heap snapshot for "Detached" when you only care about DOM leaks.

## 156: What is queryObjects() in the DevTools console?

`queryObjects(Constructor)` is a console utility that lists all live objects created with that constructor or having it in their prototype chain. For example, after closing a dialog 10 times, `queryObjects(Dialog)` shows whether 10 dialog instances are still alive. It's a quick check without reading a whole snapshot. It only works in the DevTools console, not in page code.

## 157: How do you find a leak in a React app using heap snapshots?

Mount and unmount the suspect component several times, then compare snapshots. Filter for "Detached" to find detached DOM nodes and for `FiberNode` to see if fiber objects keep growing. Follow the retainers of a detached node or fiber. Often you'll find a listener on `window`, a subscription in a store, a timer or a module-level variable that still holds a callback from the unmounted component.

## 158: Can a useRef cause a memory leak?

A ref itself is freed with the component. The problem is when you put a ref value somewhere that lives longer, like a module-level variable, a global map or a third-party library. For example, storing `ref.current` (a DOM node) in a global registry and never removing it keeps the node and its subtree alive after unmount.

## 159: How do you safely subscribe to an external store in React?

Use `useSyncExternalStore`. You pass a `subscribe` function that returns an unsubscribe function, and React calls it at the right time when the component mounts and unmounts. This avoids forgetting to unsubscribe and also avoids tearing in concurrent rendering.

```jsx
function useOnlineStatus() {
  return useSyncExternalStore(
    (callback) => {
      window.addEventListener("online", callback);
      window.addEventListener("offline", callback);
      return () => {
        window.removeEventListener("online", callback);
        window.removeEventListener("offline", callback);
      };
    },
    () => navigator.onLine,
  );
}
```

## 160: How does TanStack Query keep its cache from growing forever?

Every query has a `gcTime` (called `cacheTime` before v5). When no component uses a query anymore, it becomes inactive, and after `gcTime` (5 minutes by default) it's removed from the cache. If you set `gcTime: Infinity` or create queries with unique keys for every request, the cache can keep growing, so pick keys and times with care.

## 161: Can an Apollo Client cache grow too large?

Yes. Apollo's normalized cache keeps every object it has seen by ID. In a long session that loads many different records, the cache can hold a lot of data. You can remove objects with `cache.evict()` and then run `cache.gc()` to remove anything no longer reachable from the root queries.

## 162: How does the takeUntil pattern work in Angular and what is the common mistake?

You create a `Subject` that emits in `ngOnDestroy`, and pipe your streams through `takeUntil(destroy$)` so they complete when it emits. The common mistake is putting `takeUntil` before operators like `switchMap` or `mergeMap`. Inner subscriptions created after `takeUntil` won't be stopped. Put `takeUntil` last in the pipe. In modern Angular, `takeUntilDestroyed()` is simpler.

```ts
this.route.params
  .pipe(
    switchMap((p) => this.api.watch(p["id"])),
    takeUntil(this.destroy$), // keep it last
  )
  .subscribe((data) => (this.data = data));
```

## 163: What is DestroyRef in Angular?

`DestroyRef` is an injectable that lets you register cleanup callbacks that run when the current component, directive, service or injector is destroyed. You can use it in services and helper functions where there's no `ngOnDestroy`. `takeUntilDestroyed()` uses it under the hood.

```ts
const destroyRef = inject(DestroyRef);
const id = setInterval(refresh, 5000);
destroyRef.onDestroy(() => clearInterval(id));
```

## 164: Do Angular @HostListener and Renderer2.listen need manual cleanup?

`@HostListener` and the `host` property listeners are removed automatically when the directive or component is destroyed. `Renderer2.listen()` returns an unlisten function. Angular cleans up listeners on the component's own elements, but if you listen to `window` or `document` through Renderer2, call the returned function in `ngOnDestroy` to be safe.

## 165: Do Angular signals and effects need cleanup?

An `effect()` created in an injection context, like a component constructor, is destroyed automatically with that component. Effects created elsewhere need to be destroyed by calling `destroy()` on the `EffectRef`. Inside an effect you can use the `onCleanup` callback to clean up things like timers between runs.

## 166: How can an Angular root service leak component data?

A service with `providedIn: 'root'` lives for the whole app. If components register themselves, their callbacks or DOM elements in arrays inside the service and never unregister, those components can't be collected after they're destroyed. Always pair "register" with "unregister" in `ngOnDestroy`, or let the service store things in a `WeakMap`.

## 167: How can shareReplay cause a memory leak in RxJS?

`shareReplay(1)` without `refCount` keeps the source subscription alive even after all subscribers unsubscribe, and keeps the last value in memory. If the source is a long-lived stream like an interval or a WebSocket, it keeps running forever. Use `shareReplay({ bufferSize: 1, refCount: true })` when the source should stop once nobody listens.

## 168: How do you clean up an event bus in Vue?

Vue 3 removed `$on` and `$off`, so most apps use a small library like `mitt`. Since the bus lives for the whole app, every component that calls `emitter.on()` must call `emitter.off()` with the same handler in `onUnmounted`. Otherwise every mounted instance leaves a handler and its component behind.

## 169: How does KeepAlive in Vue affect memory?

`<KeepAlive>` caches component instances instead of destroying them when you switch away, so their state and DOM stay in memory. Without a limit, every visited tab or route stays cached. Use the `max` prop to limit the number of cached instances. Vue then drops the least recently used one when the limit is reached.

```vue
<KeepAlive :max="5">
  <component :is="currentView" />
</KeepAlive>
```

## 170: How do Pinia store subscriptions behave on unmount?

`store.$subscribe()` and `store.$onAction()` called inside a component's `setup` are removed automatically when the component unmounts. If you pass `{ detached: true }`, they stay active after unmount, and you must call the returned function to stop them yourself.

## 171: How does Svelte handle store subscriptions?

When you use the `$store` syntax in a component, Svelte subscribes for you and unsubscribes when the component is destroyed. If you call `store.subscribe()` manually, you get an unsubscribe function and need to call it in `onDestroy`, or return it from an `$effect` in Svelte 5.

## 172: How do you destroy a Chart.js chart?

Call `chart.destroy()` before removing the canvas or before creating a new chart on the same canvas. It removes Chart.js listeners, animations and internal references. Creating a new chart on every data update without destroying the old one is a common leak in dashboards.

```js
let chart;
function render(data) {
  chart?.destroy();
  chart = new Chart(canvas, { type: "line", data });
}
```

## 173: How do you clean up map libraries like Leaflet or Mapbox GL?

Both have a `map.remove()` method that removes the map's DOM, listeners and, for Mapbox GL and MapLibre GL, the WebGL context and its resources. Call it when the component unmounts. Just removing the container element leaves listeners on `window` and GPU resources behind.

## 174: How do you clean up the Monaco editor?

Call `editor.dispose()` on the editor instance and `dispose()` on any models you created with `monaco.editor.createModel()`. Models are stored globally and aren't removed when the editor is disposed, so creating a new model each time a file is opened, without disposing old ones, leaks memory.

## 175: How do you clean up animation libraries like GSAP?

GSAP tweens and timelines keep references to their targets until they finish or are killed. Infinite or long timelines on removed elements keep those elements alive. Use `gsap.context()` to group animations and call `ctx.revert()` on unmount, or use the `useGSAP` hook in React, which does this for you.

## 176: Can modals and tooltips appended to document.body leak?

Yes. Many libraries move modal or tooltip elements to `document.body` so they're above other content. If the component that created them unmounts without the library's cleanup, those elements stay in the body, sometimes hidden. Check the DOM after closing modals and leaving pages to make sure their containers are removed.

## 177: How do you clean up custom elements (web components)?

Use `disconnectedCallback`, which runs when the element is removed from the document. Remove listeners on `window` or `document`, clear timers, disconnect observers and close connections there. Keep in mind that an element can be connected again later, so set things up in `connectedCallback`, not only in the constructor.

```js
class LiveClock extends HTMLElement {
  connectedCallback() {
    this.timer = setInterval(
      () => (this.textContent = new Date().toLocaleTimeString()),
      1000,
    );
  }
  disconnectedCallback() {
    clearInterval(this.timer);
  }
}
customElements.define("live-clock", LiveClock);
```

## 178: Do debounced functions need cleanup on unmount?

Yes. A debounced or throttled function holds a pending timer. If the component unmounts while a call is pending, the timer still fires later and runs code that references the old component. Libraries like lodash give you a `cancel()` method; call it in the cleanup.

```jsx
const save = useMemo(() => debounce((value) => api.save(value), 500), []);
useEffect(() => () => save.cancel(), [save]);
```

## 179: Which other browser APIs need explicit closing?

Besides timers, listeners and observers, these keep resources until you close them:

- `WebSocket`: `close()`
- `EventSource`: `close()`
- `BroadcastChannel`: `close()`
- `MessagePort`: `close()`
- `IDBDatabase` (IndexedDB): `close()`
- `AudioContext`: `close()`
- `Worker`: `terminate()`

## 180: How can Cache Storage in a service worker keep growing?

The Cache Storage API stores responses on disk, and nothing removes old entries unless your code does. A service worker that caches every API response or every versioned asset forever slowly fills the origin's storage quota. Delete old caches in the `activate` event and limit runtime caches by number of entries or age, which Workbox's expiration plugin can do for you.

## 181: Can history.pushState state objects use a lot of memory?

Yes. The browser keeps the state object for each history entry, and it's structured-cloned. Putting large data like a full list of results into `pushState` for every page change keeps many copies in memory for the session. Browsers also limit state size. Store only small values, like IDs or a scroll position, and refetch the rest.

## 182: How can error tracking or analytics code cause memory growth?

Error and analytics SDKs keep queues of events, breadcrumbs and context. If they can't send data (offline, blocked or failing endpoint) and the queue has no limit, it grows. Custom code that keeps every error object, with its stack and attached data, in an array has the same problem. Good SDKs cap the number of breadcrumbs; your own code should do the same.

## 183: How do you set up an LRU cache with limits in Node.js?

The `lru-cache` package is a common choice. You can limit by count with `max`, by total size with `maxSize` and `sizeCalculation`, and by age with `ttl`.

```js
import { LRUCache } from "lru-cache";

const cache = new LRUCache({
  max: 500,
  maxSize: 50 * 1024 * 1024,
  sizeCalculation: (value) => Buffer.byteLength(JSON.stringify(value)),
  ttl: 1000 * 60 * 5,
});
```

## 184: What is the difference between TTL and LRU eviction?

TTL (time to live) removes an entry after a fixed time, no matter how often it's used. It's about freshness. LRU removes the least recently used entry when the cache is full. It's about keeping memory bounded. TTL alone doesn't cap memory if many new keys arrive quickly, so for memory safety you usually want a size limit too.

## 185: Why should a DataLoader be created per request?

DataLoader caches every key it loads, and it never evicts them by default. If you create one DataLoader at module level and share it across all requests, its cache grows with every new ID ever requested, and users can see stale or other users' data. The recommended pattern is a new DataLoader per request, usually created in the GraphQL context.

```js
const server = new ApolloServer({ typeDefs, resolvers });
await startStandaloneServer(server, {
  context: async () => ({
    userLoader: new DataLoader((ids) => getUsersByIds(ids)),
  }),
});
```

## 186: How can an ORM's identity map grow in a long-running process?

ORMs like MikroORM keep an identity map: every entity loaded through an EntityManager is tracked there. If you use one global EntityManager for all requests, the map keeps every entity ever loaded. That's why these ORMs tell you to fork a new EntityManager per request, often with a middleware like `RequestContext`.

## 187: How do Prometheus metrics with high-cardinality labels cause memory growth?

Each unique combination of label values creates a new time series that the metrics client keeps in memory. If you use labels like user ID, full URL with query string or request ID, the number of series grows with traffic and never shrinks. Use labels with a small, fixed set of values, like route pattern, method and status code.

## 188: How can OpenTelemetry spans leak memory?

A span holds attributes, events and links until it's ended. If code starts spans and doesn't end them on every code path, including errors, they can pile up in memory and in the exporter's buffers. Use `startActiveSpan` with `try`/`finally` and call `span.end()` in the `finally` block.

## 189: What happens if you don't consume a fetch response body in Node.js?

Node's `fetch` is built on undici. If you don't read or cancel the response body, the connection may not be returned to the pool, and the body's buffers stay in memory until garbage collection, which may be much later. Under load this can exhaust connections and grow memory. Always read the body (`await res.json()`, `res.text()`) or cancel it with `await res.body?.cancel()`.

## 190: What is stream backpressure and how does ignoring it use memory?

Backpressure is when a writable stream can't keep up with the data you write. `writable.write()` returns `false` when its buffer is full. If you keep writing anyway, the data piles up in memory. You should wait for the `drain` event before writing more, or use `pipeline`, which handles backpressure for you.

```js
for (const row of rows) {
  if (!out.write(format(row))) {
    await once(out, "drain");
  }
}
```

## 191: How can a Socket.IO server leak memory?

Common causes are keeping your own map of user to socket and not removing entries on `disconnect`, adding listeners to global emitters inside the connection handler, and starting per-socket intervals that are never cleared. Clean everything in the `disconnect` handler.

```js
io.on("connection", (socket) => {
  const timer = setInterval(() => socket.emit("ping"), 25_000);
  users.set(socket.id, socket.data.user);

  socket.on("disconnect", () => {
    clearInterval(timer);
    users.delete(socket.id);
  });
});
```

## 192: Why is adding process.on listeners inside a function a problem?

`process` lives for the whole app. If a function that runs many times, like a request handler or a factory, calls `process.on("SIGTERM", ...)` or `process.on("exit", ...)`, each call adds another listener with its closure. You'll get `MaxListenersExceededWarning` and a leak. Register process-level listeners once at startup.

## 193: What is AsyncLocalStorage and can it hold memory longer than expected?

`AsyncLocalStorage` from `node:async_hooks` keeps a store that follows async operations, like a request context. The store stays alive as long as any async work started inside that context is pending. If a request starts a long timer or a never-ending promise, the request's store, and whatever you put in it, stays in memory. Keep stores small and don't leave async work hanging.

## 194: How can a promise that never settles cause a leak?

A pending promise keeps its `then` callbacks alive, and those callbacks keep their closures alive. If you create a promise per request that waits for an event that never comes, and something long-lived (like an emitter listener or a map of pending requests) holds the resolve function, each request leaves objects behind. Always add timeouts and clean up pending maps on error and on timeout.

## 195: How do you write a simple memory leak test in Node.js?

Run the suspect code many times, force GC, and check that heap use doesn't grow by more than a small amount. Start Node with `--expose-gc` so `global.gc()` exists.

```js
// node --expose-gc leak-test.js
async function measure(fn, runs) {
  for (let i = 0; i < runs; i++) await fn();
  global.gc();
  return process.memoryUsage().heapUsed;
}

await measure(handleRequest, 1000); // warm up
const before = await measure(handleRequest, 1000);
const after = await measure(handleRequest, 10_000);
console.log(`growth: ${((after - before) / 1024).toFixed(0)} KB`);
```

## 196: What does the --heapsnapshot-near-heap-limit flag do?

`node --heapsnapshot-near-heap-limit=2 app.js` makes Node write up to 2 heap snapshots when the heap gets close to its limit. This lets you capture what the heap looked like just before an out-of-memory crash, without having to catch it live. Writing the snapshot needs extra memory and pauses the process, so use it with care in production.

## 197: What does the --trace-gc flag show?

`node --trace-gc app.js` prints a line for every garbage collection: its type (Scavenge, Mark-Compact and so on), heap size before and after, and how long it took. It's a quick way to see if major GCs happen more often and if heap size after GC keeps rising, without any extra tools.

## 198: What does v8.getHeapStatistics() return?

It returns numbers about the V8 heap, like `total_heap_size`, `used_heap_size`, `heap_size_limit` and `total_available_size`. `heap_size_limit` tells you the maximum heap size the process is running with, which helps check if `--max-old-space-size` is set as you expect. For per-space details, use `v8.getHeapSpaceStatistics()`.

## 199: What does the --heap-prof flag do in Node.js?

`node --heap-prof app.js` starts the V8 sampling heap profiler when the process starts and writes a `.heapprofile` file when it exits. You can load that file in the Chrome DevTools Memory panel to see which functions allocated the most memory. It has much lower overhead than heap snapshots and is good for finding code that allocates heavily.

## 200: How do you reproduce a server-side leak locally?

Run the server with `--inspect`, then send steady load to the suspect endpoints with a load testing tool like autocannon or k6. Take a heap snapshot after a warm up, keep the load going for a few minutes, force GC and take another snapshot. Compare them and look for objects whose count grows with the number of requests.

## 201: How can Jest help you notice memory leaks in tests?

Jest has a few flags for this. `--logHeapUsage` prints heap usage after each test file, so you can see if it keeps climbing. `--detectLeaks` (experimental) fails a test file if its objects aren't garbage collected after it finishes. And `workerIdleMemoryLimit` restarts test workers that go over a memory limit, which is a workaround when test code or modules leak between files.

## 202: How can you measure page memory in a Playwright or Puppeteer test?

You can open a Chrome DevTools Protocol session, force GC and read the heap size. Run the user flow many times and check that the heap doesn't keep growing.

```js
const client = await page.context().newCDPSession(page);

async function heapUsed() {
  await client.send("HeapProfiler.collectGarbage");
  const { usedSize } = await client.send("Runtime.getHeapUsage");
  return usedSize;
}

const before = await heapUsed();
for (let i = 0; i < 20; i++) {
  await page.click("#open-dialog");
  await page.click("#close-dialog");
}
const after = await heapUsed();
expect(after - before).toBeLessThan(1_000_000);
```

This only works in Chromium.

## 203: What does a MemLab scenario look like?

A scenario is a file that tells MemLab where to start, what action to do and how to undo it. MemLab takes snapshots at each step and reports what stayed in memory after the undo.

```js
// scenario.js
module.exports = {
  url: () => "http://localhost:3000/inbox",
  action: async (page) => {
    await page.click("[data-testid=open-thread]");
  },
  back: async (page) => {
    await page.click("[data-testid=close-thread]");
  },
};
```

Run it with `memlab run --scenario scenario.js`.

## 204: How do you use performance.measureUserAgentSpecificMemory()?

It returns a promise with the memory used by the page, broken down by type and frame. It only works on pages that are cross-origin isolated, which needs the `Cross-Origin-Opener-Policy: same-origin` and `Cross-Origin-Embedder-Policy: require-corp` (or `credentialless`) headers. It's currently supported in Chromium-based browsers. Results may take a while because the browser waits for the next GC.

```js
if (crossOriginIsolated && performance.measureUserAgentSpecificMemory) {
  const result = await performance.measureUserAgentSpecificMemory();
  sendToAnalytics({ bytes: result.bytes });
}
```

## 205: Why is collecting memory data from real users useful?

Lab tests only cover the flows you thought of, on fast machines, for a short time. Real users keep tabs open for hours, use features in odd orders and run on low-memory phones. Sampling memory from real sessions over time, grouped by app version, shows whether a new release made memory growth worse.

## 206: Why should you measure memory in a production build of a frontend app?

Development builds keep extra data for warnings, hot reload and debugging. React in development, for example, keeps extra info on fibers and runs effects twice in Strict Mode. Hot reload can leave old module copies behind. Numbers from a dev build can look like leaks that don't exist in production, or hide the real ones. Use a production build, ideally with source maps or without minification of names so snapshots stay readable.

## 207: Can browser devtools extensions keep objects alive during memory tests?

Yes. React DevTools, Redux DevTools and Vue DevTools keep references to components, fibers, actions and state history so you can inspect them. Redux DevTools in particular keeps the full action history by default. When you measure memory, disable these extensions or test in a clean profile so they don't distort the results.

## 208: How can a hot module reload in the browser leak memory during development?

When a module is replaced, its old version may have started timers, added listeners on `window` or created global objects. Unless the module cleans up using the HMR API, like `import.meta.hot.dispose()` in Vite, those things stay behind. After many edits the dev tab can become slow. It's a dev-only problem, but it's good to know so you don't chase it as a production leak.

## 209: How do you size the Node.js heap inside a container?

Set `--max-old-space-size` below the container's memory limit so V8 runs GC harder, and fails with a clear "heap out of memory" error, before the kernel kills the container. A common rule is about 70 to 80 percent of the limit, which leaves room for Buffers, native memory, stacks and the allocator. Recent Node versions also look at container limits when picking a default, but setting it explicitly makes the behavior clear.

```dockerfile
ENV NODE_OPTIONS="--max-old-space-size=1536"
```

## 210: Why do front-end builds sometimes fail with "heap out of memory"?

Bundlers and TypeScript type checking load a lot of source code, ASTs and source maps into memory. Large monorepos can go over the default heap limit. The usual fixes are raising the limit with `NODE_OPTIONS=--max-old-space-size=...`, turning off source maps for builds that don't need them, splitting type checking into its own step, and upgrading tools. Here a bigger limit is a valid fix, because it's not a leak, just a big job.

## 211: What does PM2's max_memory_restart do?

It tells PM2 to restart a process when its memory goes over a set value, like `500M`. This keeps a leaking app from taking down the server, but users may see errors during the restart, and the leak is still in the code. Use it as a safety net while you find and fix the real cause.

## 212: How do you limit memory for Node.js worker threads?

Pass `resourceLimits` when you create the `Worker`. You can set `maxOldGenerationSizeMb`, `maxYoungGenerationSizeMb` and others. If the worker goes over the limit, it's terminated and emits an `error` event, instead of taking down the whole process.

```js
import { Worker } from "node:worker_threads";

const worker = new Worker("./resize.js", {
  resourceLimits: { maxOldGenerationSizeMb: 256 },
});
worker.on("error", (err) => console.error("worker failed", err));
```

## 213: How can Puppeteer or Playwright leak memory in a server app?

Server apps that use a headless browser for PDFs or screenshots often open a new page or browser per request. If an error happens before `page.close()` or `browser.close()`, the page or the whole Chromium process stays open. Memory and process count grow until the server dies. Always close in a `finally` block and set timeouts.

```js
const page = await browser.newPage();
try {
  await page.goto(url, { timeout: 15_000 });
  return await page.pdf();
} finally {
  await page.close();
}
```

## 214: How can child processes leak in Node.js?

Spawning a child process for each job without waiting for it to exit, or without killing it on timeout, leaves processes running. Each one uses its own memory, and the parent keeps handles and stream buffers for it. Track child processes, kill them on timeout or shutdown, and handle the `exit` and `error` events.

## 215: How should you handle file uploads to avoid memory spikes?

Don't buffer whole files in memory. For example, Multer's `memoryStorage()` keeps each uploaded file as a Buffer, so several large uploads at once can use gigabytes. Use disk storage or stream the upload straight to object storage like S3, and always set a file size limit.

```js
import multer from "multer";

const upload = multer({
  dest: "/tmp/uploads",
  limits: { fileSize: 20 * 1024 * 1024 },
});
```

## 216: Why should you set a body size limit in an Express app?

`express.json()` reads the whole request body into memory and parses it. Without a reasonable limit, a client can send a huge body and use a lot of memory per request, which makes memory denial of service easy. The default limit is 100 KB; keep it small and raise it only for routes that need it.

```js
app.use(express.json({ limit: "100kb" }));
```

## 217: How can an in-memory rate limiter or dedup set leak?

A rate limiter that stores a counter per IP in a `Map`, or a set of processed message IDs used to skip duplicates, grows with every new key. If entries never expire, a server that sees many unique IPs or messages slowly fills memory. Give every entry a TTL, clean up expired ones on a schedule, or use Redis with key expiration.

## 218: How do you periodically clean up expired entries in a Map?

Run a timer that walks the map and deletes expired entries. Call `unref()` on the timer so it doesn't keep the process alive, and keep its handle so you can stop it on shutdown.

```js
const entries = new Map(); // key -> { value, expiresAt }

const sweeper = setInterval(() => {
  const now = Date.now();
  for (const [key, entry] of entries) {
    if (entry.expiresAt <= now) entries.delete(key);
  }
}, 60_000);
sweeper.unref();
```

## 219: What is the risk of caching promises?

Caching the promise instead of the value is a nice way to dedupe concurrent requests. Two problems are common. If the promise rejects, the failed promise stays cached forever unless you remove it. And the promise's callbacks can capture the request or other large objects. Remove the entry on failure and add a size or TTL limit.

```js
function getUser(id) {
  if (!cache.has(id)) {
    const p = fetchUser(id).catch((err) => {
      cache.delete(id);
      throw err;
    });
    cache.set(id, p);
  }
  return cache.get(id);
}
```

## 220: How can capturing the request object in a closure cause a leak?

The request object in Node.js references the socket, headers, the parsed body and often user data. If a callback that lives longer than the request, like a cache entry, a listener on a global emitter or a long timer, references `req`, all of that stays in memory. Copy only the fields you need, like `const userId = req.user.id`, before creating long-lived callbacks.

## 221: How can you avoid closures holding large objects you don't need?

Pull out the small values you need before creating the closure, so the closure doesn't reference the big object at all. Also avoid declaring big temporary values in the same scope as long-lived callbacks.

```js
function attach(report) {
  const title = report.title; // copy the small part
  button.addEventListener("click", () => alert(title));
  // "report" isn't referenced by the handler
}
```

## 222: How does Reselect 5 avoid memory growth in memoized selectors?

Reselect 5 uses `weakMapMemoize` by default. It caches results in a tree of `WeakMap`s keyed by the argument objects, so it can cache many argument combinations, and cached results are freed when the argument objects themselves are garbage collected. Older versions kept only the last result, which avoided growth but caused more cache misses.

## 223: When should you use a WeakMap as a cache?

Use a `WeakMap` when the cache key is an object whose lifetime you don't control, like a DOM node, a request object or a data object from a store, and the cached value only makes sense while that object exists. The cache then cleans itself up. It doesn't work for string or number keys, and you can't set a size limit or TTL, so it's not a replacement for an LRU cache.

## 224: Why can deep copies double memory usage?

`structuredClone`, `JSON.parse(JSON.stringify(x))` or spreading in a loop all create full copies. If you copy a large state object on every change and keep both, you use twice the memory, and keeping history of copies uses much more. Use immutable updates that share unchanged parts (like Immer does) and avoid keeping old copies you don't need.

## 225: How do you handle very large JSON payloads in Node.js?

`JSON.parse` needs the whole string in memory and then builds the whole object, so a 500 MB JSON file can use several gigabytes. For large data, use a streaming JSON parser that emits items one by one, or switch the format to newline-delimited JSON (NDJSON) so you can process one line at a time.

```js
import { createReadStream } from "node:fs";
import { createInterface } from "node:readline";

const rl = createInterface({ input: createReadStream("events.ndjson") });
for await (const line of rl) {
  if (line) handle(JSON.parse(line));
}
```

## 226: What does lean() do in Mongoose and why does it save memory?

By default Mongoose turns every result into a full Mongoose document with change tracking, getters, setters and methods. `.lean()` returns plain JavaScript objects instead. They use much less memory and are faster to create. Use `lean()` for read-only queries, especially ones that return many documents.

```js
const users = await User.find({ active: true }).select("name email").lean();
```

## 227: How do you process a large database table without loading it all?

Use a cursor or stream to read rows in batches, or page through with keyset pagination (`WHERE id > lastId ORDER BY id LIMIT 1000`). Each batch is processed and then dropped before loading the next one, so memory stays flat. For example, Mongoose queries have `.cursor()` and most SQL drivers support streaming results.

```js
for await (const doc of Order.find({ status: "open" }).lean().cursor()) {
  await process(doc);
}
```

## 228: How can BullMQ jobs use more and more Redis memory?

By default BullMQ keeps completed and failed jobs in Redis, including their data and return values. In a busy queue that adds up to a lot of memory. Set `removeOnComplete` and `removeOnFail` on jobs or as default job options, either as `true` or with a count or age limit.

```js
await queue.add("email", payload, {
  removeOnComplete: { count: 1000 },
  removeOnFail: { age: 24 * 3600 },
});
```

## 229: How can an in-memory job or retry queue cause problems?

If jobs are added faster than they're processed, or retries pile up while a downstream service is down, an in-memory array grows without limit. The process may crash, and you lose all queued jobs when it does. Put a maximum size on the queue, reject or drop new work when it's full, and use a real queue (like Redis or a message broker) for work that must not be lost.

## 230: How can HTTP keep-alive agents hold memory?

An HTTP agent with keep-alive keeps idle sockets open to reuse them. If you create a new agent per request, or a new HTTP client instance with its own agent, sockets aren't reused and many stay open. Create one agent or client and reuse it. You can also limit `maxSockets` and `maxFreeSockets` on an `http.Agent`.

## 231: Why shouldn't you create a new Redis or database client per request?

Each client opens connections, keeps buffers and often starts timers for reconnects and health checks. Creating one per request and forgetting to close it leaks connections and memory, and even when you do close it, it's slow. Create the client once at startup, reuse it, and close it on shutdown.

## 232: How can image processing with sharp use a lot of memory?

`sharp` uses the libvips library, which works in native memory outside the V8 heap and keeps an operation cache. Processing many large images at once can use a lot of RSS even if `heapUsed` looks small. You can limit concurrency with `sharp.concurrency()`, turn off or shrink the cache with `sharp.cache(false)`, and limit how many images you process in parallel.

## 233: How do async generators relate to leaks?

An async generator holds its state, like open connections or file handles, until it finishes. When a `for await` loop exits early with `break`, `return` or an exception, JavaScript calls the generator's `return()` method, which runs its `finally` blocks. Put cleanup in `finally` inside the generator. If you call `next()` manually and stop early, call `return()` yourself.

```js
async function* readRows(db) {
  const cursor = db.openCursor();
  try {
    for await (const row of cursor) yield row;
  } finally {
    await cursor.close();
  }
}
```

## 234: How should GraphQL subscriptions be cleaned up on the server?

Each subscription is usually an async iterator tied to a pub/sub system. When the client disconnects or unsubscribes, the server calls `return()` on the iterator, and your pub/sub must remove its listener there. Custom iterators that ignore `return()` keep listeners in the pub/sub for every subscription that ever existed.

## 235: Can holding a reference to window.open() leak memory?

Yes. `window.open()` returns a reference to the new window. If you keep it in a variable or array after the popup is closed, you may keep parts of that window's state alive. Set the reference to `null` once the popup is closed, and remove any `message` listeners you added for it.

## 236: How can third-party scripts cause leaks you can't fix directly?

Ads, chat widgets, analytics and A/B testing scripts run in your page and can leak just like your code. To check, use DevTools request blocking to block one script at a time and repeat your test. If the leak goes away, report it to the vendor, update the script, load it in an iframe you can remove, or load it only on pages that need it.

## 237: How do you read heap snapshots of minified code?

Minified code renames classes and functions to short names like `e` or `t`, which makes snapshots hard to read. DevTools doesn't map heap snapshot names through source maps. The easiest fix is testing with a production build where class and function names are kept (for example, the `keep_classnames` and `keep_fnames` options in Terser, or `keepNames` in esbuild), or reproducing the leak in a development build after confirming it exists in production.

## 238: Why do leaks often show up as growing arrays of listeners?

Many libraries store listeners in arrays or sets. When a component subscribes and never unsubscribes, each mount adds one more entry. In a heap snapshot you see a listener array that grows by one per action, with closures pointing to old component instances. Looking for growing `Array` or `Set` objects with your callbacks inside is a quick way to find these.

## 239: How do you check the number of event listeners on an element?

In Chrome DevTools, select the element in the Elements panel and open the Event Listeners tab. In the console, `getEventListeners(element)` returns an object with the listeners for each event type. The Performance Monitor also shows the total JS event listener count for the page, which is helpful to see if it keeps rising.

## 240: What is the difference between a leak in the DOM and a leak in JavaScript objects?

A DOM leak means DOM nodes, often whole detached subtrees, stay alive. You see it as a growing DOM node count and "Detached" entries in snapshots. A JavaScript object leak means plain objects, arrays, closures or strings stay alive, often in caches or stores. The two are often linked: a JS object holds a DOM node, or a DOM node's listener holds a JS object.

## 241: Why can a detached DOM node keep a much bigger tree alive?

A DOM node points to its parent, children and siblings, and to its document. If your code holds one cell from a removed table, the whole table and all its rows can stay alive through those parent and child links. That's why a tiny reference to one element can retain megabytes of memory.

## 242: How can storing DOM nodes in a JavaScript array cause a leak?

Code often caches elements in arrays or maps for quick access, like a list of rendered row elements. When rows are removed from the page but not from the array, the array keeps them all alive. Remove entries when you remove the elements, or store data instead of DOM nodes, or use a `WeakMap` or `WeakRef` where it fits.

## 243: How can postMessage listeners leak in apps that use iframes or workers?

Each `message` listener you add to `window` for talking to an iframe or popup stays until you remove it. If you add a new one each time an iframe is created, and never remove it when the iframe is removed, the listeners and their closures pile up. Remove them when the iframe or worker is gone, or use a `MessageChannel` and close its ports.

## 244: What happens to timers and listeners when an iframe is removed?

When an iframe is removed, its document is unloaded and its timers and listeners are stopped. But if the parent page holds references into the iframe, like its `contentWindow`, its elements or functions created inside it, those objects and sometimes the whole iframe document can stay alive. The iframe won't run code anymore, but its memory isn't freed.

## 245: How can a global error handler leak memory?

A handler on `window.onerror`, `unhandledrejection` or `process.on("uncaughtException")` that stores every error in an array keeps every error object, its stack and anything attached to it. A recurring error, like one thrown every animation frame, can fill memory fast. Cap stored errors, send them out and drop them, or dedupe by message.

## 246: Can capturing stack traces use a lot of memory?

Each `Error` object captures a stack trace. V8 stores it in a compact form and only formats the `stack` string when you read it, but reading and keeping formatted stacks for many errors adds up. Creating errors in hot code paths just for control flow, or storing many errors with their stacks, increases memory and CPU. `Error.stackTraceLimit` controls how many frames are captured.

## 247: How can logging the same object many times keep it alive in Node.js?

In Node.js, `console.log` formats the object into a string and writes it out, so it doesn't keep the object. But if you attach the inspector with DevTools open, logged objects are kept so you can expand them, just like in the browser. Some logging libraries also buffer objects before writing. When looking at memory while debugging, keep in mind that the debugger itself may be keeping objects alive.

## 248: What is a ring buffer and when would you use one to avoid leaks?

A ring buffer (circular buffer) is a fixed-size array where new items overwrite the oldest ones when it's full. It's a simple way to keep "the last N things", like recent log lines, metrics samples or chat messages, with memory that never grows past the limit.

```js
class RingBuffer {
  constructor(size) {
    this.items = new Array(size);
    this.index = 0;
  }
  push(item) {
    this.items[this.index] = item;
    this.index = (this.index + 1) % this.items.length;
  }
}
```

## 249: How can a pub/sub or observer pattern you write yourself leak?

If `subscribe` adds a callback to a list but there's no way to unsubscribe, or callers forget to, the list only grows. Every subscriber's closure stays alive. Always return an unsubscribe function from `subscribe` and use a `Set` so removal is easy.

```js
function createStore(state) {
  const listeners = new Set();
  return {
    getState: () => state,
    setState(next) {
      state = next;
      listeners.forEach((l) => l(state));
    },
    subscribe(listener) {
      listeners.add(listener);
      return () => listeners.delete(listener);
    },
  };
}
```

## 250: What is the difference between a leak caused by your code and one caused by the runtime?

Most leaks come from app code keeping references it doesn't need. Sometimes the leak is in a library, the framework, the browser or Node.js itself. To tell them apart, build the smallest example that reproduces it. If plain code with no libraries still leaks on one runtime version and not another, it's likely a runtime bug; check the issue tracker and try upgrading. Assume your own code first, though, since that's far more common.

## 251: What is cross-request state pollution in server rendering?

It's when state from one user's request ends up visible in another user's request, because it was stored in a module-level variable or a shared store on the server. It's a correctness and security bug, and it's also a memory leak, because that shared state often keeps growing. The fix is the same for both: create stores and per-user data per request, not at module level.

## 252: How should you create a Redux store in a Next.js App Router app?

Create a new store per request instead of exporting one global store from a module. The Redux docs show a `makeStore` function and a client component that creates the store once per browser session with `useRef`. On the server, each request then gets its own store, which is freed when the request ends.

```tsx
"use client";
import { useRef } from "react";
import { Provider } from "react-redux";
import { makeStore, type AppStore } from "./store";

export function StoreProvider({ children }: { children: React.ReactNode }) {
  const storeRef = useRef<AppStore | null>(null);
  if (!storeRef.current) storeRef.current = makeStore();
  return <Provider store={storeRef.current}>{children}</Provider>;
}
```

## 253: How does React's cache() function help with per-request data on the server?

`cache` from React wraps a function so its results are memoized for the length of one server request. Calls with the same arguments during that render share the result, and the cache is thrown away after the request. It's a safe replacement for module-level memoization, which would keep data for every request forever.

```ts
import { cache } from "react";

export const getUser = cache(async (id: string) => {
  return db.user.findUnique({ where: { id } });
});
```

## 254: What is cacheMaxMemorySize in Next.js?

It's a `next.config.js` option that sets the size of Next.js's in-memory cache for things like ISR pages and data cache entries when running on a self-hosted server. The default is 50 MB. Setting it to 0 turns off in-memory caching, which is common when you use a custom cache handler like Redis so multiple instances share one cache.

## 255: How does Nuxt avoid cross-request state on the server?

Nuxt tells you not to define reactive state with `ref()` at module level, because on the server it would be shared by all requests. Use `useState` (or a Pinia store), which is created per request and passed to the client during hydration. Module-level refs also leak memory if they keep collecting data.

## 256: Why must you call seal() on styled-components' ServerStyleSheet?

During server rendering, `ServerStyleSheet` collects styles for the current page. Calling `sheet.seal()` in a `finally` block after rendering frees those resources. If rendering throws and you skip `seal()`, the sheet and its collected styles may not be freed. The docs recommend `try`/`finally` for this.

## 257: How can axios interceptors leak in a SPA?

`axios.interceptors.request.use()` adds the interceptor to a global list on the axios instance and returns an ID. If a component adds an interceptor on mount, for example to attach a token from its state, each mount adds another one, and old closures stay alive. Call `axios.interceptors.request.eject(id)` in the cleanup, or add interceptors once at app startup.

```jsx
useEffect(() => {
  const id = api.interceptors.request.use((config) => {
    config.headers.Authorization = `Bearer ${token}`;
    return config;
  });
  return () => api.interceptors.request.eject(id);
}, [token]);
```

## 258: Why is adding middleware inside a route handler a leak in Express?

`app.use()` adds middleware to the app's router stack, which lives for the life of the app. Calling it inside a request handler adds a new middleware on every request. The stack grows forever, memory goes up, and each request gets slower because it runs through more and more middleware. Register middleware once at startup.

## 259: How can a WebSocket reconnect loop create duplicate connections?

A reconnect function often runs on `close` and creates a new socket. If it doesn't check whether a connection or a pending reconnect already exists, or the component that owns it was unmounted, you can end up with several sockets open at once, each with its own handlers. Keep one reference, clear the reconnect timer on cleanup, and stop reconnecting after the component or app is shut down.

## 260: Why might polling keep running in a hidden tab, and how do you handle it?

`setInterval` polling keeps fetching data even when the tab is in the background, and each response adds to memory if you append results. Browsers throttle timers in background tabs, but they don't stop them. Listen to `visibilitychange` and pause polling while `document.hidden` is true, or use a library that does this for you.

## 261: Why can removeEventListener fail in class components with bind?

Each call to `this.handler.bind(this)` creates a new function. If you add the listener with one bound function and try to remove it with another `bind` call, the references don't match and the listener stays. Bind once in the constructor or use a class field arrow function, then use that same reference for both calls.

```js
class Widget {
  onResize = () => this.layout();

  mount() {
    window.addEventListener("resize", this.onResize);
  }
  unmount() {
    window.removeEventListener("resize", this.onResize);
  }
}
```

## 262: How do you stop a MobX reaction?

`autorun`, `reaction` and `when` return a disposer function. A reaction stays active as long as the observables it reads are alive, so if those observables live in a global store, the reaction lives forever unless you call the disposer. Call it on unmount or when the owning object is no longer needed.

```js
const dispose = autorun(() => console.log(store.count));
// later
dispose();
```

## 263: How do you unsubscribe from a Zustand store outside React?

`store.subscribe(listener)` returns an unsubscribe function. Inside React, the hook handles subscriptions for you. When you subscribe manually, for example in a non-React module or a third-party integration, keep the returned function and call it when you're done.

```js
const unsubscribe = useCartStore.subscribe((state) =>
  syncBadge(state.items.length),
);
// later
unsubscribe();
```

## 264: Why is lodash memoize risky on a server?

By default, `_.memoize` uses the first argument as the cache key and stores results in a `Map` with no size limit. On a long-running server called with many different arguments, the cache grows forever. You can clear it with `fn.cache.clear()` or replace `_.memoize.Cache` with a bounded cache, but it's often simpler to use an LRU cache.

## 265: Why does a Map keyed by objects from JSON.parse never get cache hits?

Every `JSON.parse` call creates new objects, so two parsed objects with the same content are still different keys in a `Map`. A cache keyed by those objects never finds an existing entry, it only adds new ones, and it grows forever. Use a stable primitive key like an ID or a serialized string, and still add a size limit.

## 266: Does deleting an entry from require.cache free the module's memory?

Not always. Deleting from `require.cache` only makes the next `require` load a fresh copy. The old module's exports and closures stay alive if anything still references them, like listeners it registered, timers it started or objects other modules kept. Code that reloads modules this way, for example for plugins or config, often leaks a copy of the module each time.

## 267: How can vm contexts or new Function per request cause memory growth?

Creating a new `vm` context or compiling new code on every request builds new compiled code and a new global object each time. If references to them are kept, for example in a cache or by listeners, they're never freed, and compiled code takes a fair amount of memory. Compile once and reuse, and avoid creating contexts per request where you can.

## 268: How can template compilation per request be a problem?

Template engines like Handlebars compile a template into a function. Some engines cache compiled templates by their source or name. If you compile a different template string on each request, for example with user data mixed into the template itself, the cache can grow without limit. Compile templates once at startup and pass data at render time.

## 269: How can an AbortSignal leak listeners?

When you pass a long-lived `AbortSignal`, like an app-wide shutdown signal, to many operations, each one adds an `abort` listener to it. If those operations finish but don't remove their listeners, the signal's listener list grows, and Node.js prints a `MaxListenersExceededWarning`. APIs that accept a signal usually clean up after themselves; your own code should remove its listener when the work is done, or use `AbortSignal.any()` to combine signals per operation.

```js
function waitFor(ms, signal) {
  return new Promise((resolve, reject) => {
    const onAbort = () => {
      clearTimeout(timer);
      reject(signal.reason);
    };
    const timer = setTimeout(() => {
      signal.removeEventListener("abort", onAbort);
      resolve();
    }, ms);
    signal.addEventListener("abort", onAbort, { once: true });
  });
}
```

## 270: What is events.once in Node.js and how does it help with cleanup?

`events.once(emitter, name)` returns a promise that resolves the next time the event fires. It removes its listener when the event fires, and also listens for `error`, so you don't have to clean up by hand. It also accepts an `AbortSignal`, which is useful for adding a timeout.

```js
import { once } from "node:events";

const [socket] = await once(server, "connection", {
  signal: AbortSignal.timeout(10_000),
});
```

## 271: How can storing Timeout objects in a Map leak memory in Node.js?

`setTimeout` in Node.js returns a `Timeout` object that holds the callback and its closure. Code that tracks timers per key, like per user or per job, must delete the map entry when the timer fires or is cleared. Otherwise the map keeps all the old `Timeout` objects and their closures even after they've run.

## 272: Why shouldn't you call global.gc() in production code?

`global.gc()` only exists when Node runs with `--expose-gc`, and calling it forces a full, blocking garbage collection. V8's own scheduling is usually better than manual calls, and forcing GC often makes latency worse. If you feel you need it to keep memory down, it usually means there's a leak or a large allocation pattern to fix. It's fine in tests and benchmarks.

## 273: How can a watch-mode build tool or long-running CLI leak memory?

Watch-mode tools like dev servers, test watchers and type checkers stay running for hours and rebuild on every change. Caches of ASTs, modules or source maps that are never trimmed, and listeners added on each rebuild, grow over time. If a watcher gets slow or crashes after many changes, it's often a leak in the tool or a plugin. Restarting it or upgrading usually helps.

## 274: How can jsdom-based tests leak memory?

Each jsdom environment creates a full fake DOM and window. Timers, listeners and global patches that tests add and don't clean up can keep the old window alive in long test runs. Use fake timers or clear real ones in `afterEach`, unmount rendered components (Testing Library does this automatically with supported runners), and restore mocks.

## 275: How can you analyze Node.js heap snapshots with MemLab?

MemLab can analyze heap snapshots that you took elsewhere, including from Node.js. You give it three snapshots: a baseline, a target after doing the action and a final after undoing it. It reports objects that leaked along with their retainer traces.

```bash
memlab find-leaks --baseline s1.heapsnapshot --target s2.heapsnapshot --final s3.heapsnapshot
```

## 276: What can you do when DevTools can't open a large heap snapshot?

A snapshot from a multi-gigabyte heap can be too big for DevTools to load. Options are: reproduce the leak with a smaller heap limit so the snapshot is smaller, use command-line tools that parse snapshots without the UI (MemLab has analysis commands for this), or start Chrome with more memory for DevTools. Often the easiest path is reproducing the leak locally on a smaller scale.

## 277: How do you observe GC events in Node.js from code?

Use `PerformanceObserver` from `node:perf_hooks` with the `gc` entry type. Each entry has the GC kind and duration. You can send these to your metrics to see how much time the process spends in GC and spot long pauses.

```js
import { PerformanceObserver, constants } from "node:perf_hooks";

const obs = new PerformanceObserver((list) => {
  for (const entry of list.getEntries()) {
    const major = entry.detail?.kind === constants.NODE_PERFORMANCE_GC_MAJOR;
    metrics.gcDuration.observe({ major: String(major) }, entry.duration);
  }
});
obs.observe({ entryTypes: ["gc"] });
```

## 278: How is event loop lag related to memory leaks?

As a leaking heap grows, major GCs take longer and run more often, and they block the main thread. That shows up as event loop lag: callbacks and timers run late, and request latency goes up. If event loop lag and heap size rise together over time, a leak is a likely cause. You can measure lag with `perf_hooks.monitorEventLoopDelay()`.

## 279: What memory metric should you alert on for a Node.js service?

Raw `heapUsed` jumps up and down, so alerts on it are noisy. Better signals are: heap used right after major GCs trending up over hours, RSS getting close to the container limit (for example over 85 percent), and container restarts with OOMKilled. Combining a trend alert with a "close to limit" alert catches both slow leaks and sudden spikes.

## 280: Is it a good idea to expose a heap snapshot endpoint in production?

Only with strong protection. A heap snapshot contains secrets and user data, and taking one pauses the process and can double its memory. If you add an admin endpoint or a signal handler for this, make sure it's authenticated, not public, rate limited and logged. Many teams prefer sending a signal with `--heapsnapshot-signal` to one instance pulled out of traffic.

## 281: What is a Node.js diagnostic report and how does it help with memory issues?

`process.report.writeReport()` (or the `--report-on-fatalerror` flag) writes a JSON report with the JavaScript and native stack, heap statistics, resource usage, loaded libraries and active handles. Running with `--report-on-fatalerror` gives you a report when the process crashes with an out-of-memory error, which helps you see the heap state and what was running at that moment.

## 282: What is the difference between memory requests and limits in Kubernetes?

The request is the amount of memory the scheduler reserves for the container when placing it on a node. The limit is the maximum it can use before being OOMKilled. If the limit is much higher than the request, pods may be placed on nodes that can't actually give them that memory under load. For Node.js apps, set the heap limit based on the container limit, and set the request close to real usage.

## 283: How do you tell whether memory growth is in the JS heap or outside it?

Compare `heapUsed` with `rss` and `external` from `process.memoryUsage()` over time. If `heapUsed` grows along with RSS, the leak is in JavaScript objects, and heap snapshots will show it. If `heapUsed` is flat but RSS and `external` or `arrayBuffers` grow, the memory is in Buffers, native addons or the allocator, and heap snapshots won't show much.

## 284: Why don't Buffer contents show up as heap size in snapshots?

A `Buffer` is a JavaScript object that points to bytes stored outside the V8 heap. The heap snapshot shows the small JS wrapper, and newer DevTools versions show the backing store size too, but the bytes are counted in `external` and `arrayBuffers`, not `heapUsed`. Leaked Buffers may look small in the snapshot while RSS grows a lot. Look at `system / JSArrayBufferData` or `ArrayBuffer` entries and their retained size.

## 285: How can a WeakMap still cause a leak?

A `WeakMap` holds its keys weakly but its values strongly as long as the key is alive. If the value references the key, the engine handles that fine (these are called ephemerons). But if the key is kept alive by something else, like a global list or a listener, the value stays too. A `WeakMap` only helps if the key object itself can be garbage collected.

## 286: What is FinalizationRegistry?

`FinalizationRegistry` lets you register a callback that may run after an object is garbage collected. You can use it to clean up related resources, like removing a cache entry for a `WeakRef`. There's no guarantee the callback runs, or when, so it must never be the only way important resources get cleaned up.

```js
const registry = new FinalizationRegistry((key) => cache.delete(key));

function remember(key, obj) {
  cache.set(key, new WeakRef(obj));
  registry.register(obj, key);
}
```

## 287: What is the explicit resource management proposal (using) and how does it help?

JavaScript has added `using` and `await using` declarations. When a `using` block or function ends, the runtime calls the object's `[Symbol.dispose]()` (or `[Symbol.asyncDispose]()`) method, even if an error was thrown. It's like `try`/`finally`, but you can't forget the cleanup. It's supported in recent versions of Chrome, Firefox and Node.js, and in TypeScript 5.2 and later.

```js
import { openSync, closeSync, writeSync } from "node:fs";

function openTempFile() {
  const handle = openSync("/tmp/data", "w");
  return {
    handle,
    [Symbol.dispose]() {
      closeSync(handle);
    },
  };
}

{
  using file = openTempFile();
  writeSync(file.handle, "hello");
} // closed here
```

## 288: What is DisposableStack?

`DisposableStack` (and `AsyncDisposableStack`) collects several cleanup actions and runs them in reverse order when it's disposed. It's useful when a function sets up many things, like listeners, timers and connections, and needs to undo all of them. You can `use()` disposable objects, `defer()` plain callbacks, or `adopt()` a value with a custom cleanup.

```js
function setupWidget(el) {
  const stack = new DisposableStack();
  const onClick = () => toggle(el);
  el.addEventListener("click", onClick);
  stack.defer(() => el.removeEventListener("click", onClick));
  const id = setInterval(refresh, 1000);
  stack.defer(() => clearInterval(id));
  return stack; // caller calls stack.dispose()
}
```

## 289: How do you prevent memory leaks when using setInterval for polling in a component?

Clear the interval in the cleanup, avoid overlapping requests if one takes longer than the interval, and cancel the in-flight request on unmount. A chained `setTimeout` makes it easier to wait for each request before scheduling the next.

```jsx
useEffect(() => {
  const controller = new AbortController();
  let timer;
  async function poll() {
    try {
      const res = await fetch("/api/status", { signal: controller.signal });
      setStatus(await res.json());
    } catch (err) {
      if (err.name === "AbortError") return;
    }
    timer = setTimeout(poll, 5000);
  }
  poll();
  return () => {
    controller.abort();
    clearTimeout(timer);
  };
}, []);
```

## 290: How can React Context keep large data alive?

A context value lives as long as the provider is mounted, often at the top of the app. If you put large objects, like full API responses, file contents or a big normalized dataset, into a top-level provider, they stay for the whole session even after the pages that used them are closed. Keep only what's shared and needed in high-level context, and clear data when it's no longer needed.

## 291: How can a big closure in a useCallback or useMemo keep old data alive?

`useCallback` and `useMemo` keep the latest function or value and its closure. That's usually fine, since React only keeps one. The problem appears when the memoized callback is passed to something long-lived, like a global event bus or a third-party library, and never removed. Then the library keeps an old closure with old state and props, possibly a large dataset, after the component is gone.

## 292: Why might a memory leak show up only after a user logs out and in again?

Logout often clears some state but not all. Caches keyed by user, subscriptions to user-specific channels, socket connections and timers started after login may survive logout. Logging in again creates new ones next to the old ones. Make logout tear down everything that login set up, or do a full page reload on logout, which is simple and reliable.

## 293: How can switching tabs or routes in a SPA reveal leaks?

Each route change unmounts one set of components and mounts another. If any of them forget cleanup, switching back and forth 20 times shows clear growth: more listeners, more detached nodes, more instances of a component class. It's one of the best manual tests for SPA leaks. Watch the Performance Monitor while switching, then confirm with heap snapshots.

## 294: What is the difference between leaks from lifecycle bugs and leaks from data growth?

Lifecycle leaks come from not undoing setup: listeners, timers and subscriptions left behind after something is destroyed. They grow with how many times components or requests are created. Data growth leaks come from collections that only add, like caches, logs and stores. They grow with how much data the app sees. You fix the first with cleanup code and the second with limits and eviction.

## 295: How do you review code for memory leaks during a pull request?

Look for setup without matching teardown: every `addEventListener` should have a `removeEventListener` or an abort signal, every `setInterval` a `clearInterval`, every `subscribe` an unsubscribe, every `on` an `off`. Check module-level `Map`, `Set` and arrays for a size limit or eviction. Check that resources like sockets, streams, pages and connections are closed in `finally` blocks.

## 296: Are there lint rules that help catch leak patterns?

Some. `eslint-plugin-react-hooks` checks effect dependencies, which helps you write correct cleanups. `@typescript-eslint/no-floating-promises` catches promises that nobody awaits or handles. RxJS has lint rules like `rxjs-x/no-ignored-subscription` to flag subscriptions that aren't stored. No linter can find all leaks, since they depend on object lifetimes at runtime.

## 297: How do you add memory leak checks to CI?

Run a few key user flows many times in a headless browser and compare heap size or object counts before and after, failing the build if growth is above a threshold. MemLab is built for this. For backend code, run a load test against a test server for a few minutes and check that heap used after GC stays flat. Keep the thresholds a bit loose, because memory numbers have some noise.

## 298: Why is a memory leak harder to find in production than locally?

Production has real traffic patterns, many users, long uptimes and data you don't have locally. A leak might depend on a rare code path, a specific error, or a slow downstream service. Locally you often don't run long enough to see it. That's why production metrics with good labels, like version and instance, plus the ability to take a snapshot from one instance, are so useful.

## 299: How do you tell if a memory problem started with a specific deploy?

Graph memory with deploy markers. If the slope of memory growth after GC changed right after a deploy, compare the code changes in that release. Rolling back, or running the old and new versions side by side on a few instances, confirms it. This is much faster than hunting through snapshots without a starting point.

## 300: When is it OK to accept growing memory instead of fixing it?

Rarely, but sometimes. If the growth is tiny, the process restarts often anyway (like short-lived serverless instances or nightly jobs), and the fix is risky or the leak is in a dependency you can't change yet, a scheduled restart or memory-based restart can be a reasonable short-term choice. Document it, monitor it, and plan the real fix. Don't hide it.

# Advanced Questions (301-450)

## 301: How is the V8 heap organized?

V8 splits the heap into spaces. The young generation (new space) holds new objects and is split into two semi-spaces. The old generation (old space) holds objects that survived a couple of young collections. There's also a large object space for objects too big to move cheaply, a code space for compiled code, and a few others for internal use. Each space has its own collection strategy, which is why short-lived garbage is cheap and long-lived objects cost more.

## 302: How does the V8 Scavenger work?

The Scavenger collects the young generation. It copies live objects from the "from" semi-space to the "to" semi-space (or to old space if they already survived once), updates pointers, and then treats the whole "from" space as free. The cost depends on the number of live objects, not on how much garbage there is, so it's very cheap when most young objects die. V8 runs it in parallel on several threads.

## 303: How does an object get promoted to the old generation?

An object that survives a scavenge is copied to the other semi-space. If it survives a second scavenge, it's promoted (moved) to old space. Leaked objects always get promoted, since they never die. Promotion also happens to objects that just live slightly too long, like data held during a slow request, which increases old-space work even without a leak.

## 304: What does the Mark-Compact collector do?

Mark-Compact collects the whole heap. It marks all live objects starting from roots, sweeps dead objects to make their memory reusable, and compacts some pages by moving live objects together to reduce fragmentation. It costs much more than a scavenge, so V8 does most of the marking in the background and in small steps to keep main thread pauses short.

## 305: What is Orinoco in V8?

Orinoco is the name of V8's garbage collector project that made GC mostly parallel, incremental and concurrent. Parallel means several threads work on the same GC step at once. Incremental means marking is split into small chunks between JavaScript execution. Concurrent means helper threads do marking and sweeping while JavaScript keeps running. Together they cut long stop-the-world pauses down a lot.

## 306: What is a write barrier and why does the GC need it?

When marking runs incrementally or concurrently, JavaScript keeps changing objects at the same time. A write barrier is a small piece of code the engine runs on pointer writes to tell the GC about changes, for example when an already-scanned object now points to an unmarked one. Without it, the GC could miss a live object and free it. Write barriers also record old-to-new pointers so the Scavenger knows which old objects point into the young generation.

## 307: What are remembered sets in V8?

A remembered set records which slots in old-space objects point to young objects. When the Scavenger runs, it treats those slots as extra roots so it doesn't need to scan the whole old generation. Code that keeps writing new objects into long-lived ones, like pushing fresh objects into a big global array, makes remembered sets larger and scavenges slower, even before memory is technically leaked.

## 308: What does --max-semi-space-size do and when would you tune it?

It sets the maximum size in megabytes of each young generation semi-space. A bigger young generation means fewer scavenges and fewer short-lived objects promoted by mistake, which can help apps with high allocation rates like busy API servers. The trade-off is more memory and slightly longer scavenge pauses. Measure GC time and latency before and after changing it.

```bash
node --max-semi-space-size=64 server.js
```

## 309: What is the difference between a high allocation rate and a memory leak?

A high allocation rate means the app creates a lot of short-lived objects per second. It causes frequent scavenges and CPU overhead, but the heap after GC stays flat. A leak means some objects are never released, so the heap after GC keeps rising. Allocation sampling or `--heap-prof` helps with the first problem, heap snapshot comparisons with the second.

## 310: How does DevTools compute retained size?

It builds a dominator tree from the heap graph. Object A dominates object B if every path from the roots to B goes through A. The retained size of A is its own size plus the sizes of all objects it dominates, since those would all become unreachable if A were removed. That's why an object shared by two parents shows up in neither parent's retained size.

## 311: What is a dominator in a heap snapshot and why does it matter for leaks?

A dominator of an object is a node that every path from the roots must pass through to reach it. If you find the closest dominator of a large group of leaked objects, you've found the single reference whose removal would free them all. Firefox has a Dominators view, and Chrome's retained size is based on the same idea.

## 312: How are weak references shown in a Chrome heap snapshot?

Weak edges, like those from `WeakMap` and `WeakRef`, don't keep objects alive, and DevTools marks them as weak in the retainers view (often shown in gray or with a "weak" label). When you read retainer paths, skip weak edges, because they aren't the reason the object is alive. Look for the first strong path back to a root.

## 313: What is the shared closure context problem in V8?

All closures created in the same function call share one context object holding the captured variables. If any closure in that scope uses a large variable, it goes into the shared context, and every closure from that scope keeps it alive. So a small, long-lived closure can keep a big object alive just because a different closure from the same scope used it.

```js
function setup() {
  const big = new Array(1_000_000).fill("x");
  const unused = () => big.length; // puts "big" in the shared context
  return () => "small"; // still keeps "big" alive
}
const keep = setup();
```

## 314: What was the famous Meteor memory leak with closures?

It was a bug pattern described by the Meteor team in 2013. A function replaced a global object every time it ran. Inside, a closure that was never called referenced the previous object, and a different long-lived closure (a method on the new object) shared the same context. So each new object kept the previous one alive through the shared context, building a chain that grew on every call. It's the classic example of the shared closure context problem.

```js
let theThing = null;
function replaceThing() {
  const originalThing = theThing;
  const unused = () => originalThing; // captures the old object
  theThing = {
    longStr: "*".repeat(1_000_000),
    someMethod() {}, // shares the context with "unused"
  };
}
setInterval(replaceThing, 1000);
```

## 315: How do you fix a shared closure context leak?

Make sure the big value isn't captured in a scope that also produces long-lived closures. You can set the variable to `null` once it's no longer needed, move the closure that uses it into a separate function so it gets its own context, or pass the needed value as an argument instead of capturing it. In the Meteor example, adding `originalThing = null` at the end of the function breaks the chain.

## 316: Why does using eval in a function keep its whole scope alive?

Direct `eval` can read any variable in the surrounding scope by name, and the engine can't know which ones ahead of time. So V8 has to keep all variables in that scope (and outer scopes) in a context, and any closure from there keeps everything alive. `with` has a similar effect. Avoid direct `eval` and `with`, especially in long-lived code.

## 317: Can an open debugger change what is kept in memory?

Yes. When DevTools is attached, the engine may keep extra information so you can inspect variables in scopes, and the console keeps logged objects. Breakpoints and paused execution keep the paused frames' locals alive. So memory measured with DevTools open, especially with a populated console, may be higher than in normal use. Clear the console and close panels you don't need before measuring.

## 318: What are sliced strings and how can they retain memory?

When you take a substring of a long string, V8 may create a sliced string that points to the original string with an offset and length instead of copying the characters. This saves time, but if you keep the small substring and drop the original, the whole original stays in memory. For example, keeping a 10-character token cut out of a 50 MB file keeps all 50 MB alive.

## 319: How do you force a copy of a substring so it doesn't keep the parent string?

There's no official API for it, because it depends on engine internals. Common tricks are ones that make the engine build a new flat string, like `JSON.parse(JSON.stringify(s))` or going through a `Buffer` in Node.js (`Buffer.from(s).toString()`). A cleaner design is to avoid reading huge strings in the first place, for example by streaming and parsing only the parts you need.

## 320: What are cons strings in V8?

When you concatenate strings, V8 can create a cons string (rope), which is a small object that points to the left and right parts instead of copying them. It's flattened into a normal string later when needed, for example when you index into it. Long chains of concatenation create deep ropes that keep all their pieces alive and use more memory than one flat string until they're flattened.

## 321: What are hidden classes (maps) and how do they relate to memory?

V8 gives each object a hidden class (called a map internally) that describes its shape: which properties it has and where they're stored. Objects with the same shape share a map, which saves memory and makes property access fast. If you create objects with many different shapes, for example by adding properties in different orders, V8 creates many maps. This is memory overhead, not usually a leak, but it can be large in code that builds objects with dynamic keys.

## 322: What is dictionary mode for objects?

When an object has many properties added and deleted, or keys that look like a dictionary, V8 may switch it to dictionary mode, storing properties in a hash table instead of a fixed layout. This uses more memory per property and makes access slower. Using `delete` on objects in hot code, or using plain objects as large dynamic maps, can trigger it. A `Map` is a better fit for dynamic keys.

## 323: How can sparse arrays use more memory than expected?

An array with big holes, like `arr[1_000_000] = 1` on an empty array, usually switches to a dictionary-style storage, which is slower per element. On the other side, an array created with `new Array(n)` and then filled can keep a large backing store, and an array you keep pushing to grows its capacity in steps and may not shrink right away when you remove items. If memory per element matters, use typed arrays for numbers.

## 324: Why can arrays of numbers use more memory than you expect?

V8 stores small integers (Smis) directly in the array slots, but other numbers, like doubles, may be stored in a separate `HeapNumber` object unless the array is a packed double array. Mixing types in an array forces it into a generic elements kind where each number may need its own heap object. For large numeric data, `Float64Array` or `Int32Array` store raw values in a compact buffer.

## 325: What is pointer compression in V8?

Pointer compression stores pointers in the heap as 32-bit offsets from a base address instead of full 64-bit addresses. This reduces heap size a lot, often by around 40 percent in Chrome. The trade-off is that each heap must fit in a 4 GB region. Chrome uses it; official Node.js builds don't enable it by default, which is why Node can have larger heaps but uses more memory per object.

## 326: How does marking handle WeakMap entries (ephemerons)?

A `WeakMap` entry is an ephemeron: the value is kept alive only if the key is alive. During marking, the GC can't decide about an entry until it knows if the key is reachable, and the value might itself make other keys reachable. So V8 processes ephemerons in rounds until nothing changes. Very large or deeply chained `WeakMap` structures can make marking slower, though it's rarely a problem in practice.

## 327: What does it mean that WeakRef keeps its target alive during the current job?

When you create a `WeakRef` or call `deref()` and get the object back, the spec says the object stays alive until the end of the current synchronous job (the current run of the event loop task or microtask checkpoint). This means two `deref()` calls in the same synchronous code give the same result. It also means a `WeakRef` target is never collected in the middle of code that just used it.

## 328: What are the rules for the held value in FinalizationRegistry?

The held value passed to `register(target, heldValue)` is given to your callback after the target is collected. It must not be the target itself (that throws), and it must not reference the target, or the target can never be collected. Usually it's a small key like an ID or a file handle number. You can also pass an unregister token to cancel the registration later with `unregister()`.

## 329: Why shouldn't you rely on FinalizationRegistry to close important resources?

Callbacks may run late, in an order you can't control, or never at all, for example if the program exits first or the engine decides not to collect the object. A file handle or connection that only closes in a finalizer can stay open far longer than expected. Use explicit cleanup (`close()`, `dispose()`, `using`) as the main path, and finalizers only as a backup to catch mistakes.

## 330: What do suspended async functions keep in memory?

When an async function hits `await`, its frame is saved on the heap: all live local variables, the promise it returns and where to continue. That state lives until the awaited promise settles. If the awaited promise never settles, the frame and everything it references stays forever. A pending `await` on a promise that nothing will ever resolve is a quiet leak.

## 331: What do suspended generators keep in memory?

A generator that has started and not finished keeps its frame, including local variables, alive as long as the generator object is reachable. If you keep an iterator in a list and never finish it or call `return()`, its locals, which might include large buffers or open resources, stay in memory. Finished generators release their frame.

## 332: Do promise chains keep earlier values alive?

Each `then` callback and its closure stay alive until the promise it's attached to settles, and after that they're released. A settled promise keeps its result value as long as the promise object itself is reachable. So storing promises in a long-lived cache keeps their results alive too. Long chains of pending promises, like a recursive "wait then retry" chain that builds a new promise each round, can grow if earlier promises in the chain stay referenced.

## 333: How does Chrome collect cycles between DOM nodes and JavaScript objects?

Chrome's Blink engine uses Oilpan (also called cppgc), a garbage collector for C++ objects, and it's unified with V8. During a full GC, V8 and Oilpan trace through each other's objects, so a cycle like "JS object holds a DOM node, DOM node's listener holds the JS object" is collected when nothing outside the cycle references it. That's why the old Internet Explorer DOM cycle leaks don't happen in modern browsers.

## 334: What were the classic Internet Explorer memory leak patterns?

Old Internet Explorer managed DOM objects with reference counting (COM) and JavaScript with a separate tracing GC. A cycle that crossed the two, like a DOM element with an `onclick` handler whose closure referenced that element, could never be freed, even after leaving the page in some versions. Developers had to null out handlers on unload. These patterns don't apply to modern browsers, but they still come up in interviews and older articles.

## 335: How does the Node.js Buffer pool cause unexpected retention?

Small Buffers created with `Buffer.allocUnsafe()`, `Buffer.from(string)` and similar methods are sliced from a shared pool, 8 KB by default (`Buffer.poolSize`). A Buffer smaller than half the pool size can come from it. If you keep a tiny slice of the pool, the whole 8 KB pool chunk stays alive. Keeping many small long-lived Buffers can keep many pool chunks alive. `Buffer.alloc()` doesn't use the pool.

## 336: How can slicing a Buffer retain a large amount of memory?

`buf.subarray()` (and the deprecated `buf.slice()`) return a view on the same memory, not a copy. If you read a 100 MB file into a Buffer and keep a 20-byte header slice, the whole 100 MB stays alive. Copy the small part with `Buffer.from(buf.subarray(0, 20))` or `Buffer.copyBytesFrom()` so the large buffer can be freed.

```js
const header = Buffer.from(fileBuffer.subarray(0, 20)); // copy, not a view
```

## 337: What is external memory and why does it matter to the GC?

External memory is memory that a JavaScript object owns but that lives outside the V8 heap, like `ArrayBuffer` contents or native objects from addons. V8 only knows about it if the embedder or addon reports it (using `AdjustAmountOfExternalAllocatedMemory` in the C++ API). If it's not reported, V8 sees only small JS wrappers and doesn't feel pressure to run GC, so native memory can grow a lot before the wrappers are collected.

## 338: How can a native addon cause a leak that heap snapshots don't show?

An addon can allocate memory in C or C++ and never free it, or free it only when a JS wrapper is collected. If the leak is purely native, heap snapshots look normal and only RSS grows. Tools like `valgrind`, `heaptrack` or AddressSanitizer on a debug build can find native leaks. Updating the addon, or replacing it with a pure JS or WebAssembly version, often fixes it.

## 339: Why can RSS keep growing even when the JS heap is flat and nothing leaks?

Memory allocators like glibc's `malloc` don't always return freed memory to the operating system, and they can fragment memory into many partly used pages. With many threads (the libuv threadpool, zlib, native addons), glibc creates multiple arenas, each holding its own free memory. RSS can then grow and stay high even though no objects are leaked. This is fragmentation, not a leak, but the effect on container limits is the same.

## 340: How do MALLOC_ARENA_MAX and jemalloc help with RSS growth in Node.js?

Setting the environment variable `MALLOC_ARENA_MAX=2` (or a small number) limits how many glibc arenas are created, which often reduces fragmentation and RSS for multi-threaded workloads. Another option is preloading a different allocator like jemalloc with `LD_PRELOAD`, which tends to fragment less. Both are worth trying when RSS grows but the JS heap and `external` stay flat. Measure before and after.

## 341: Why can compression with zlib cause memory fragmentation in Node.js?

zlib streams allocate fairly large native buffers, and they run on the libuv threadpool. Many concurrent compression streams, for example WebSocket `permessage-deflate` on lots of connections, cause many native allocations from different threads, which fragments memory. The `ws` library documents this and has a `concurrencyLimit` option for its compression. Limiting concurrency or turning off per-message compression helps.

## 342: What is a decompression bomb and how do you protect against it?

A decompression bomb is a small compressed payload that expands to a huge size, like a few kilobytes that become gigabytes. If a server decompresses user uploads or request bodies without a limit, one request can use all its memory. Node's zlib has a `maxOutputLength` option for the sync and convenience methods, and for streams you can count bytes and destroy the stream when it goes over a limit.

```js
import { gunzipSync } from "node:zlib";

const data = gunzipSync(input, { maxOutputLength: 10 * 1024 * 1024 });
```

## 343: How does V8 handle the large object space?

Objects above a certain size (around a few hundred kilobytes, depending on the version) go into the large object space, each on its own pages. They're never moved by compaction, since copying them would be slow. They're freed when unreachable like other objects. Creating and dropping many large objects, like big arrays or strings in a loop, causes many page allocations and can raise RSS and GC work.

## 344: What is heap fragmentation inside V8?

After sweeping, old-space pages can have free gaps between live objects. If the gaps are small and scattered, new objects may not fit, and V8 needs more pages even though the total free memory is large. Compaction fixes this by moving live objects together on selected pages. Heavy fragmentation shows up as `heapTotal` growing much more than `heapUsed`.

## 345: What does V8 do when the heap is close to its limit?

As it approaches the limit, V8 runs full GCs more and more often, trying to free space. If GCs free very little, the app spends most of its time in GC ("GC thrashing") and becomes extremely slow before finally crashing with "heap out of memory". Node.js can register a near-heap-limit callback, which is how `--heapsnapshot-near-heap-limit` writes a snapshot, temporarily raising the limit to have room to do it.

## 346: Why does an app sometimes get very slow right before an out-of-memory crash?

When the heap is nearly full, every allocation can trigger another full GC, and each GC finds almost nothing to free. The main thread ends up doing almost nothing but marking the same live objects again. Request latency spikes, health checks may time out, and the process may be restarted for being unresponsive before it actually crashes. Watching GC time as a fraction of wall time catches this early.

## 347: What does the V8 memory reducer do?

The memory reducer is a V8 heuristic that runs extra GCs when the app looks idle, to shrink the heap and give memory back. It helps apps whose memory was high during a busy period and then drops. It's one reason memory can fall some time after load stops, and it's also why measuring memory right after a burst may show higher numbers than a few seconds later.

## 348: Why might heap usage in a snapshot be lower than heapUsed reported a moment earlier?

Taking a heap snapshot runs a full GC first, so the snapshot only contains reachable objects. `heapUsed` before the snapshot included garbage that hadn't been collected yet. Also, the snapshot counts some internal objects differently. Compare snapshots with snapshots, and runtime metrics with runtime metrics, rather than mixing the two.

## 349: How does an object's size get counted in a heap snapshot?

Shallow size is the bytes used by the object itself: its header, its in-object properties and, for arrays and strings, their element storage when it's inline. Out-of-object property storage and elements backing stores are separate objects, shown as their own nodes. That's why a big array may appear small in shallow size and large in retained size, with the elements store as a separate `(array)` or `(object elements)` entry.

## 350: Is there a sizeof operator for JavaScript objects?

No. JavaScript has no built-in way to get an object's memory size, and the real size depends on the engine, hidden classes, string representation and shared structures. Libraries that estimate size by walking properties are only rough guesses. For real numbers, use heap snapshots, or measure `heapUsed` after forced GC before and after creating many copies of the object, then divide.

## 351: How can custom async_hooks code leak memory?

A common pattern is storing data in a `Map` keyed by `asyncId` in the `init` hook and deleting it in `destroy`. But `destroy` isn't called for every resource in a timely way. For promises, it only fires when the promise is garbage collected, and some resources never get it. Entries can pile up in the map. Prefer `AsyncLocalStorage`, which handles context without you managing per-resource maps, and avoid custom hooks in production code where you can.

## 352: How did AsyncLocalStorage change in recent Node.js versions?

Node.js 24 switched `AsyncLocalStorage` to an implementation based on `AsyncContextFrame` by default. Instead of using async hooks to copy the store to every new async resource, the context is captured as a frame that flows with promises and callbacks. It has lower overhead, but the main rule is the same: the store stays alive as long as any pending async work started in its context, so keep stores small and don't leave work hanging.

## 353: What happens to unhandled promise rejections in modern Node.js and why does it matter for memory?

Since Node.js 15, an unhandled rejection crashes the process by default (`--unhandled-rejections=throw`). Before that, they only printed a warning. Code that creates rejected promises without handlers used to keep running and could build up rejected promises and their data. Now these bugs crash early, which is safer. Don't switch the mode back to `warn` to hide them.

## 354: How can slow clients cause memory exhaustion on a Node.js server?

Each open connection keeps a socket, buffers and request state. Clients that send headers or bodies very slowly (slowloris-style attacks), or read responses very slowly, keep connections and their buffered data open for a long time. Node's `http` server has `headersTimeout`, `requestTimeout` and `keepAliveTimeout` settings to close them. Keep them set to sensible values and put a reverse proxy in front for extra protection.

## 355: What is load shedding based on memory and how would you implement it?

Load shedding means rejecting some requests, usually with a 503, when the server is close to its limits, so it doesn't crash and fail all requests. For memory, you check heap used or RSS and refuse new work above a threshold. In Fastify, the `@fastify/under-pressure` plugin does this with options like `maxHeapUsedBytes` and `maxRssBytes`, and it can also watch event loop delay.

```js
await fastify.register(import("@fastify/under-pressure"), {
  maxHeapUsedBytes: 1_200_000_000,
  maxRssBytes: 1_800_000_000,
  maxEventLoopDelay: 1000,
});
```

## 356: Why does Promise.all on a huge list cause a memory spike?

`Promise.all(items.map(doWork))` starts every operation at once. With a million items you create a million promises, a million closures and often a million open requests or queries, all in memory at the same time. Process in batches or with a concurrency limit, for example with `p-limit`, so only a fixed number of operations are in flight.

```js
import pLimit from "p-limit";

const limit = pLimit(20);
const results = await Promise.all(
  items.map((item) => limit(() => doWork(item))),
);
```

## 357: Does using p-limit with a big array still hold memory?

Yes, partly. `p-limit` limits how many operations run at once, but `items.map(...)` still creates a pending promise and a queued closure for every item right away, and `Promise.all` keeps every result. For very large inputs, process items as a stream or in chunks, and write results out as you go instead of collecting them all.

```js
for (let i = 0; i < items.length; i += 1000) {
  const chunk = items.slice(i, i + 1000);
  const results = await Promise.all(chunk.map(doWork));
  await saveResults(results);
}
```

## 358: How should a Server-Sent Events endpoint clean up?

The server usually keeps a list of connected clients to push events to. When the client disconnects, the request emits `close`; remove the client from the list, clear any heartbeat timer and remove listeners on shared emitters. If you miss this, the list holds dead responses forever and writes to them may throw or buffer.

```js
app.get("/events", (req, res) => {
  res.writeHead(200, { "Content-Type": "text/event-stream" });
  clients.add(res);
  const ping = setInterval(() => res.write(": ping\n\n"), 15_000);
  req.on("close", () => {
    clearInterval(ping);
    clients.delete(res);
  });
});
```

## 359: How can GraphQL queries be used to exhaust server memory?

A client can send a deeply nested or very wide query that makes the server load and build huge response objects, or ask for many aliases of an expensive field. The response is built in memory before it's sent. Protect the server with query depth limits, complexity or cost limits, pagination limits on list fields, and timeouts.

## 360: What is the billion laughs attack?

It's an XML attack where a small document defines entities that reference other entities, each expanding many times, so a few kilobytes turn into gigabytes of text when the parser expands them. Parsers that expand entities without limits will run out of memory. Use XML parsers with entity expansion turned off or limited. The same idea applies to YAML aliases and other formats with references.

## 361: Walk through how you would handle a production memory leak incident.

1. Stop the bleeding: scale out, add memory-based restarts or roll back the last deploy if the timing matches.
2. Collect data: memory graphs (heap, RSS, external) per instance and version, deploy times, traffic changes.
3. Check if it's heap or native memory by comparing `heapUsed` and RSS.
4. Take heap snapshots from one instance pulled out of traffic, early and later, or reproduce under load in staging.
5. Compare snapshots, find growing objects and their retainers.
6. Fix, test with a load test that shows flat memory, and deploy.
7. Add a regression test or monitor so it doesn't come back.

## 362: Memory grows under high load and comes back down when load drops. Is it a leak?

Probably not. It sounds like work piling up: queued requests, buffered responses, in-flight promises or a cache filling during the peak. When load drops, the work finishes and memory is freed. It's still a risk, since a bigger spike could crash the server, so add backpressure, concurrency limits or load shedding. A real leak would not come back down after load drops.

## 363: RSS keeps growing but heapUsed is flat. How do you investigate?

Look at `external` and `arrayBuffers`. If they grow, look for leaked Buffers, streams that buffer without limit, or typed arrays held in caches. If they're flat too, the growth is native: an addon, a native library (image processing, compression, crypto) or allocator fragmentation. Try `MALLOC_ARENA_MAX` or jemalloc, turn off native features one at a time, and use native memory tools like `heaptrack` or `valgrind` in a test environment.

## 364: Memory started leaking right after a Node.js major version upgrade. What do you do?

First confirm it with a side-by-side comparison of the old and new versions under the same load. Then check if it's in your code being hit by a behavior change, in a dependency (native addons often need rebuilding or updates), or in Node itself. Search the Node.js and dependency issue trackers, try the latest patch release, and build a minimal reproduction. Roll back if it's urgent while you investigate.

## 365: A heap snapshot shows a huge amount of retained size in strings held by a Map in one module. What's likely going on?

That's usually an unbounded cache or registry: something like a `Map` from URL, query text, user ID or rendered HTML to a string value, where entries are added and never removed. Check where the map is written, what the keys are and whether keys can be unbounded (user input, timestamps, query params). Add a size limit and TTL with an LRU cache, or remove the cache if it doesn't help.

## 366: A heap snapshot shows hundreds of thousands of Promise objects. What could cause it?

Usually promises that never settle, or long chains being built up. Look at the retainers of a sample of promises: they often point to a `Map` of pending requests waiting for a response that never came, a queue waiting for a lock that's never released, or a retry loop that creates new promises without bounds. Add timeouts, make sure every path resolves or rejects, and clean up pending maps on error.

## 367: The number of Socket objects in heap snapshots keeps growing. Where would you look?

Check outbound connections first: HTTP clients created per request, missing keep-alive agent reuse, response bodies that are never consumed, and database or Redis clients created and not closed. Then check inbound: WebSocket or long-polling connections tracked in your own lists and not removed on close. Retainers of a socket will usually show which agent, pool or list keeps it.

## 368: What can you do if the leak is inside a third-party library you can't easily change?

Options, from best to worst: upgrade to a version that fixes it, report it with a minimal repro, patch it locally with a tool like `patch-package` until a fix is released, wrap it so you create and dispose of it in a controlled way (or run it in a worker you restart), replace the library, or as a last resort schedule restarts of the affected process. Document the workaround and track the upstream issue.

## 369: When does object pooling help memory and when does it hurt?

Object pooling reuses objects instead of creating new ones, which can reduce allocation rate and GC work in hot paths like game loops or high-throughput parsers. But pooled objects live forever and end up in old space, they can hold stale references to other data if not reset, and a pool that grows without limit is a leak. In most web code, V8's young generation handles short-lived objects well, so measure before adding pooling.

## 370: How can you reduce memory when holding a very large dataset in Node.js?

Store it in a compact format: typed arrays for numbers, columnar layouts instead of arrays of objects, and integer IDs instead of repeated strings. Avoid keeping both raw JSON and parsed objects. Consider whether the data should live in Redis, a database or a memory-mapped file instead. For lookups, a `Map` with numeric keys or a sorted typed array with binary search can use much less memory than millions of small objects.

## 371: Why might converting an array of objects to columnar storage save memory?

Each JS object has a header and a pointer to its hidden class, and each property value may be a pointer to a separate heap object. A million objects with five fields means millions of small heap objects. Columnar storage keeps one typed array per field, so each value takes a fixed number of bytes with no per-object overhead. It can cut memory several times and is also faster to scan.

## 372: How does string deduplication save memory in large datasets?

When you parse big datasets, the same string values, like country names or status codes, appear millions of times, and each parsed copy can be a separate string in memory. Keeping a `Map` from string to one shared instance (interning) and using that instance replaces copies with references. For a small set of values, replacing strings with small integer codes saves even more.

## 373: What memory issues can occur in a Node.js cluster or multi-process setup?

Each worker process has its own heap, so a leak happens in every worker, and the total memory is the sum of all of them. In-memory caches are duplicated per worker, which multiplies memory and makes the cache less useful. Process managers may restart one leaking worker at a time, hiding the problem. Use shared caches like Redis for big data, and size each worker's heap so the total fits on the machine.

## 374: How would you design an in-memory cache for a multi-tenant SaaS backend?

Bound it by total bytes, not just entry count, and give each tenant a fair share so one large tenant can't push everyone else out. Use TTLs for freshness, LRU or LFU eviction for capacity, and metrics per tenant for hit rate and size. Key entries with tenant ID to avoid data leaks between tenants. For data shared across instances, put a Redis layer behind the local cache.

## 375: What is a two-tier cache and how does it affect memory?

A two-tier cache uses a small in-process cache (L1) in front of a shared cache like Redis (L2). The L1 cache gives very fast reads for hot keys and is kept small and bounded, while the L2 holds the bigger dataset outside the Node.js heap. This keeps process memory predictable and lets many instances share most of the cached data.

## 376: How can an event-sourced or replay-based system use too much memory?

Rebuilding state by replaying all events into memory works for small streams, but with millions of events the whole history, or the rebuilt state, may not fit in memory. Projections that keep every event in arrays also grow forever. Use snapshots so you replay only recent events, stream events instead of loading them all, and store projections in a database.

## 377: How can you measure memory use per request or per operation in Node.js?

There's no exact per-request number, because all requests share one heap. You can estimate by running one kind of request many times in isolation and measuring heap growth after GC, or use sampling heap profiles (`--heap-prof` or the DevTools allocation sampler) to see which code paths allocate the most. In production, correlating memory growth with traffic per endpoint can point to the endpoint that leaks.

## 378: How do you find which endpoint leaks when you have many?

Correlate memory growth with traffic per endpoint over time, look for growth that matches one endpoint's request count, then confirm with a load test hitting only that endpoint. Heap snapshot retainers often mention route-specific code or data shapes. Another approach is bisecting: send load to half the endpoints, see which half leaks, and keep splitting.

## 379: How can request-scoped dependency injection leak in frameworks like NestJS?

Request-scoped providers are created for every request and should be freed after it. If a singleton provider keeps a reference to a request-scoped one, for example by caching it in a field or registering its callback on a global emitter, every request's instance stays alive. Request scope also bubbles up the injection chain, creating many instances per request, which adds memory and CPU overhead even without a leak.

## 380: How can a logger with child loggers leak?

Some logging setups create a child logger per request with request-specific fields. That's fine if the child is dropped after the request. It leaks if children are stored in a map by request ID and never removed, or if each child adds a listener or a transport to a shared parent. Check the library's guidance and don't register transports per request.

## 381: How can the default in-memory store of a rate limiter or session library hurt you at scale?

In-memory stores keep all keys in the process. They grow with the number of unique clients, they're duplicated per instance, and they reset on restart. Under an attack with many spoofed IPs or session IDs, they can grow very fast. Use a shared external store like Redis with key expiration, and keep the in-memory version for development and tests.

## 382: What memory problems can happen in a WebSocket server with many connections?

Each connection has a socket, read and write buffers, per-connection state and possibly compression contexts. With tens of thousands of connections, small per-connection costs add up. Slow clients that don't read cause write buffers to grow. Check `bufferedAmount` (in `ws`, `socket.bufferedAmount`) before sending more, drop or disconnect slow clients, keep per-connection state small, and be careful with per-message compression.

## 383: How do you handle backpressure when broadcasting to many WebSocket clients?

Before sending to each client, check how much data is already buffered for it. If it's above a threshold, skip the message, send a smaller one or close the connection. Otherwise one slow client can make the server buffer every broadcast in memory for that connection.

```js
for (const client of wss.clients) {
  if (client.readyState !== WebSocket.OPEN) continue;
  if (client.bufferedAmount > 1_000_000) {
    client.terminate();
    continue;
  }
  client.send(message);
}
```

## 384: How can message queue consumers run out of memory?

If a consumer fetches messages faster than it processes them, unprocessed messages build up in its memory. In RabbitMQ that's controlled by the prefetch count, and in Kafka by fetch and batch settings. A high prefetch with slow processing, or processing messages concurrently without a limit, can use a lot of memory. Set prefetch or batch sizes to match processing speed and limit concurrency.

## 385: Why can a long-running Node.js script that processes files in a loop still grow in memory?

Common reasons: results are collected in an array instead of written out, errors are pushed into a list, a `Map` used for deduplication grows with every record, promises are created without waiting, or a logging library buffers output faster than it's written. Process and write one item or batch at a time, keep only counters or small summaries, and `await` each step.

## 386: Why can Node.js EventEmitter listeners keep a whole object graph alive in a long-lived service?

A listener on a long-lived emitter keeps its closure alive, and the closure may reference a request, a component, a connection object or a large result. That object may reference many more. One forgotten listener can retain a large graph. When the retained size of an emitter's listener array is large in a snapshot, look at which closures are in it and where they were added.

## 387: How can a memory leak in a dependency show up only under specific configuration?

Some leaks only happen on certain code paths: retries, a specific error type, a TLS option, a compression setting, or a feature flag. For example, a client library might leak only when a request times out, or a driver only when reconnecting. Reproduce with the same configuration and failure conditions as production, including failures of downstream services.

## 388: Why are active timers never garbage collected in Node.js?

Active timers are held by Node's timer lists, which are roots, so an active timer's callback and closure are never collected, no matter what else references them. A `setInterval` with no `clearInterval`, or a recursive `setTimeout` that keeps rescheduling itself, holds its data forever. `unref()` doesn't change this; it only lets the process exit. The only fix is clearing the timer.

## 389: What problems can memory leaks cause in serverless platforms beyond crashes?

Warm instances that leak get slower over time due to GC work, which raises duration and cost. Latency becomes unpredictable, since a request might hit a fresh or an old instance. Some platforms recycle instances quietly, hiding the leak but causing more cold starts. Memory limits also affect CPU allocation on some platforms, so you may raise memory and pay more just to work around a leak.

## 390: How do you test for leaks in a serverless function?

Invoke the handler many times in the same process locally, with the module loaded once, just like a warm instance does. Force GC and measure heap used between batches of calls. Check module-scope caches and clients. In production, watch memory used per invocation on long-lived instances, which most platforms report, and look for growth with invocation count.

## 391: How can the Edge or Workers runtime differ for memory leaks?

Edge runtimes like Cloudflare Workers run code in V8 isolates with small memory limits, often 128 MB, and reuse isolates across requests. Global state survives between requests, just like in Node, so global caches and arrays leak the same way, but you hit the limit much sooner. They also don't give you heap snapshot tools as easily, so keep global state minimal and bounded.

## 392: What are the trade-offs of using WeakRef for a cache?

A `WeakRef` cache lets the GC free values under memory pressure, which sounds nice. But collection timing is unpredictable, so hit rates vary with GC behavior, and values may disappear right after being cached, or stay much longer than expected. Results become hard to test and reason about. An LRU cache with a size limit is usually clearer; use `WeakRef` only when you've measured that it helps.

## 393: How do you prevent memory problems when exporting large reports from a web app?

Don't build the whole file in memory on the server. Stream rows from the database through a formatter (CSV, NDJSON) straight into the response, with backpressure. For heavy formats like Excel, use streaming writers or generate in a background job that writes to object storage and give the user a download link. On the client side, avoid building huge Blobs; let the browser download the response directly.

## 394: How can logging request and response bodies cause memory issues?

Logging full bodies means large strings are created for every request, sometimes copies of big uploads or API responses. With async logging, they're buffered in memory until written. Under high load or large payloads this uses a lot of memory and also puts sensitive data in logs. Log sizes and IDs, truncate bodies, and sample detailed logs.

## 395: How can a server-side rendering cache leak memory?

Caching rendered HTML per URL helps performance, but URLs include query strings, tracking parameters and user-specific paths. Without a limit, every unique URL adds a new entry. Normalize keys (drop tracking params), only cache pages that are the same for all users, set a byte-based limit and TTL, and consider caching at a CDN instead of in the process.

## 396: Why should you be careful with in-memory caches in auto-scaled services?

Each instance builds its own cache, so memory per instance is the same no matter how many instances you run, and caches start cold on every new instance, sending load to the database during scale-out. Large caches also make instances slower to start and more likely to be OOMKilled. A shared cache tier, plus small local caches for the hottest keys, usually works better.

## 397: How can a feature flag SDK or config client grow memory?

These SDKs keep flag definitions in memory and update them through streaming or polling. Problems happen when you create a new client per request, which opens new connections and timers each time, or when you evaluate flags with highly unique contexts and the SDK keeps per-context data for analytics. Create one client at startup and check the SDK's docs for context caching limits.

## 398: How do you avoid leaks when using Node.js worker threads for CPU work?

Create a fixed pool of workers (with a library like Piscina) instead of a new worker per task, set `resourceLimits`, and terminate workers on shutdown. Transfer large `ArrayBuffer`s instead of copying them, and make sure tasks that fail or time out don't leave entries in the pool's internal queues. A worker that crashes from out-of-memory should be replaced, not take down the main thread.

## 399: How does transferring an ArrayBuffer to a worker affect memory?

When you `postMessage(buf, [buf])`, the buffer is transferred, not copied: the worker gets the memory and the sender's buffer becomes detached with length 0. This avoids having two copies, which matters for large data. If you post without the transfer list, the data is structured-cloned, so for a moment both threads hold a full copy.

## 400: What is the difference between structured cloning and transferring for memory?

Structured cloning copies the data, so memory use doubles until one side drops its copy, and cloning big objects costs CPU time. Transferring moves ownership of transferable objects, like `ArrayBuffer`, `MessagePort`, `ImageBitmap` and streams, with no copy. You can also call `structuredClone(value, { transfer: [buf] })` to move buffers inside the same thread.

## 401: What is a "Detached Window" in a Chrome heap snapshot?

It's the global object of a frame, like an iframe or a popup, whose document has been closed or removed but which is still kept alive by references from another frame. A detached window can retain that frame's whole JavaScript heap and DOM. In the snapshot, follow its retainers back to the code in your main page, often a stored `contentWindow`, a listener or an object created inside the iframe.

## 402: How does site isolation affect memory in Chrome?

With site isolation, pages from different sites run in separate renderer processes, including cross-site iframes. This improves security but means each site has its own heap and process overhead. A page with several cross-site iframes uses more memory than one process would. It also means a leak in a cross-site iframe shows up in a different process than your main page in the Task Manager.

## 403: How does Chrome's Memory Saver affect long-running apps?

Memory Saver discards background tabs that haven't been used for a while to free memory. When the user comes back, the page reloads from scratch. Your app should be ready for that: save important state (like unsent form data) and restore it on load. You can check `document.wasDiscarded` to know the page was discarded, and listen to the `freeze` and `resume` page lifecycle events.

## 404: What is Vue's effectScope and how does it help with cleanup?

`effectScope()` creates a scope that collects all reactive effects created inside it, like `computed`, `watch` and `watchEffect`. Calling `scope.stop()` stops all of them at once. It's useful for composables or stores that create effects outside a component, where there's no automatic cleanup on unmount.

```js
import { effectScope, ref, watch } from "vue";

const scope = effectScope();
scope.run(() => {
  const count = ref(0);
  watch(count, (v) => console.log(v));
});
// later
scope.stop();
```

## 405: How do React 19 ref callback cleanup functions help prevent leaks?

In React 19, a ref callback can return a cleanup function. React calls it when the element is removed or the ref changes, instead of calling the ref with `null`. This makes it easy to set up observers or listeners on a DOM node and tear them down in one place.

```jsx
<div
  ref={(node) => {
    const observer = new ResizeObserver(onResize);
    observer.observe(node);
    return () => observer.disconnect();
  }}
/>
```

## 406: Why is subscribing during render a leak risk in React?

Render can run many times without committing, especially with concurrent rendering, Suspense and Strict Mode double rendering. If you subscribe, start a timer or add a listener during render, React has no matching cleanup to call for renders that are thrown away. Those subscriptions leak. Side effects belong in `useEffect`, `useLayoutEffect`, event handlers or `useSyncExternalStore`.

## 407: Can a React component that never commits still leak?

Yes, if its render function has side effects. A component that suspends or is interrupted may render several times and never commit, so its effects never run and their cleanups never run either. Anything it set up during render, like a subscription or a module-level cache entry, stays. Keep render pure and put setup in effects.

## 408: How does Zone.js relate to memory in Angular apps?

Zone.js patches async APIs like `setTimeout`, `addEventListener` and promises to know when to run change detection. It keeps small task objects for pending timers and listeners, so leaked timers and listeners also keep zone tasks alive. Newer Angular versions support zoneless change detection, which removes this layer, but the leaks themselves come from missing cleanup either way.

## 409: How do you release memory used by a video element?

Pausing and removing a `<video>` may not free its media buffers right away, especially if the element is still referenced. A common approach is to pause, remove the `src` attribute (or clear `srcObject`), call `load()` to reset the media element, and drop references. For media from `URL.createObjectURL`, also revoke the URL.

```js
video.pause();
video.removeAttribute("src");
video.load();
```

## 410: Why should you call close() on ImageBitmap and VideoFrame objects?

`ImageBitmap` and WebCodecs `VideoFrame` objects hold decoded image data, which can be large and may live in GPU memory. The garbage collector doesn't know how heavy they are, so they may stay alive longer than you'd like. Calling `close()` frees the data right away. For `VideoFrame`, not closing frames can even stall the decoder, because it runs out of frame buffers.

## 411: How do you free WebGL resources and contexts?

Delete each resource you created with `gl.deleteTexture()`, `gl.deleteBuffer()`, `gl.deleteFramebuffer()`, `gl.deleteProgram()` and so on. Browsers also limit how many WebGL contexts can be active at once, and creating too many makes the oldest ones get lost. To release a context early, use the `WEBGL_lose_context` extension's `loseContext()`, then drop references to the canvas.

## 412: How can an OffscreenCanvas in a worker leak memory?

An `OffscreenCanvas` transferred to a worker keeps its backing bitmap in the worker. If the worker keeps creating new canvases, bitmaps or WebGL resources for each frame or task without freeing them, memory grows in the worker, which is easy to miss when you only watch the main page heap. Profile the worker too: DevTools lets you pick the worker's context in the Memory panel.

## 413: How do you profile memory inside a web worker?

In Chrome DevTools, the Memory panel has a JavaScript VM instance selector. Each worker appears there with its own heap, and you can take snapshots of it separately. The Performance Monitor and Task Manager also show worker memory. Remember that a leak in a worker doesn't show up in the main thread's snapshots.

## 414: How can large Blobs or downloads in the browser cause memory issues?

Building a big file in memory, for example by collecting chunks in an array and creating a `Blob` at the end, keeps all the data in memory, sometimes twice during conversion. Browsers may back big Blobs with disk, but behavior varies. For large downloads, let the browser download the file directly from the server, or stream the data to disk with the File System Access API's writable streams where it's supported.

## 415: How can micro-frontends cause memory leaks?

Each micro-frontend mounts and unmounts as the user navigates. If one doesn't clean up global listeners, timers, global variables, injected styles or shared event buses on unmount, every navigation leaves its pieces behind. Since they're written by different teams, cleanup rules are easy to skip. Frameworks like single-spa have an `unmount` lifecycle, and every micro-frontend should fully undo its `mount` there.

## 416: What memory problems can Module Federation shared singletons cause?

Shared singletons, like one React or one store used by several remotes, live for the whole app. If a remote registers state, reducers, routes or listeners on a shared singleton and doesn't remove them when it's unloaded, those stay alive with the host. Loading different versions of a "shared" library by mistake can also load several copies into memory.

## 417: How can an Electron app leak memory between the main and renderer processes?

In the renderer, `ipcRenderer.on` listeners added in components must be removed with `ipcRenderer.removeListener` on unmount, or they pile up with each mount. In the main process, references to closed `BrowserWindow` or `webContents` objects stored in arrays keep their native resources alive. Listeners added to `app` or `ipcMain` per window must also be removed when that window closes.

## 418: How would you use real user memory data to detect a leak introduced by a release?

Collect `measureUserAgentSpecificMemory()` samples (on cross-origin isolated pages) or other memory signals at intervals in long sessions, tagged with the app version and session duration. Compare the memory growth per hour of session time between versions, using percentiles since the data is noisy. If a new version shows a clearly steeper slope, look at what changed in that release for the flows those users used most.

## 419: How would you build a leak regression test suite for a large SPA?

Pick the main user flows that create and destroy a lot: route changes, opening and closing dialogs, switching tabs, opening records. For each, write a scenario with an action and an undo step. Run them in headless Chromium with MemLab or your own CDP script, repeating each several times, and fail if retained objects or heap growth pass a threshold. Run it on a production build, ideally nightly, and store results to track trends.

## 420: A dashboard tab uses 1 GB after being open for 8 hours. How would you investigate?

First find out what grows: JS heap, DOM nodes or listeners, using the Performance Monitor while the dashboard runs. Dashboards usually leak through polling and real-time updates, so watch memory over 10 to 20 minutes of updates with no user input. Take snapshots a few minutes apart and compare. Look for growing chart data arrays, chart instances that are recreated but not destroyed, growing socket message buffers, and timers per widget that aren't cleared when widgets refresh.

## 421: A detached DOM node is retained only through a React FiberNode. What does that tell you?

The fiber's `stateNode` points to the DOM node, so the question is why the fiber is still alive. Unmounted fibers should be unreachable. Keep following the retainer chain up from the fiber. Usually you'll find a closure in a listener, a subscription or a timer that captured something linked to that fiber, like state setters or props. Fix that reference and the fiber and its DOM will be freed.

## 422: What does "context" mean in a retainer path in a heap snapshot?

A `system / Context` entry is a closure context: the object V8 creates to hold variables captured by closures in a scope. When you see an object retained through `context` by a function, the function's closure is keeping the object alive. Look at which function owns the context, where that function is referenced from, and whether the captured variable is really needed.

## 423: What does a growing "(compiled code)" category in a heap snapshot suggest?

It suggests the app keeps generating new code: using `eval` or `new Function` with different strings, creating many `vm` contexts, loading new script copies, or recompiling regular expressions with dynamic patterns. Each piece of generated code needs compiled code and metadata. Cache compiled functions, avoid generating code from data, and reuse regular expressions.

## 424: What does it mean when an object is retained by "(Global handles)" or "(Internal)"?

These are roots managed by the engine or the embedder, not by your JavaScript. Global handles are used by browser and Node.js internals and by native addons to keep JS objects alive from C++. If your leak goes through them, the reference might be held by a native API, like an active timer, a pending callback, a DOM API or an addon. Look at the object just below the handle to see which API holds it.

## 425: How can you analyze heap snapshots programmatically?

A `.heapsnapshot` file is JSON with nodes, edges and strings in flat arrays. You can parse it yourself, but it's much easier to use MemLab's heap analysis API, which loads snapshots and lets you query objects by constructor name, compute retainer traces and write custom leak filters. This is useful for big snapshots or for checks in CI that DevTools can't do.

```js
import { getFullHeapFromFile } from "@memlab/heap-analysis";

const heap = await getFullHeapFromFile("./final.heapsnapshot");
let count = 0;
heap.nodes.forEach((node) => {
  if (node.name === "ChatMessage") count++;
});
console.log(`ChatMessage objects: ${count}`);
```

## 426: How do you write a custom leak filter in MemLab?

MemLab lets you define a `leakFilter` function in your scenario. It's called for each object that was allocated during the action and still alive after the undo step, and you return `true` for ones you consider leaks. This helps cut noise, for example by only flagging detached DOM nodes or instances of your own classes.

```js
module.exports = {
  url: () => "http://localhost:3000/",
  action: async (page) => page.click("#open"),
  back: async (page) => page.click("#close"),
  leakFilter(node) {
    return node.name === "Modal" || node.name.startsWith("Detached ");
  },
};
```

## 427: How do you decide who owns the cleanup of a resource?

The code that creates or subscribes to a resource should own its cleanup, and its lifetime should be tied to a clear owner: a component, a request, a session or the app. When ownership is unclear, like a service creating something that a component uses, resources tend to leak. A good rule is that every API that sets something up returns a way to tear it down, and the caller stores and calls it.

## 428: How do you design a library API so users don't leak memory with it?

Return a disposer from every subscribe, listen or create function, and support `AbortSignal` options so cleanup can be tied to existing lifetimes. Implement `Symbol.dispose` or `Symbol.asyncDispose` on objects that hold resources. Keep internal caches bounded by default, don't store references to user objects longer than needed, and document what must be cleaned up and when.

## 429: How does tying cleanup to an AbortSignal simplify complex components?

Instead of keeping a list of handles to clean up, you create one `AbortController` per lifetime (a component instance, a request, a connection) and pass its signal to everything: `addEventListener`, `fetch`, streams, `events.on` and your own functions. One `abort()` call then tears it all down. This also makes cancellation and cleanup the same path, which leaves fewer places for bugs.

## 430: Why do memory leaks often hide behind feature flags or rare UI paths?

Leaks need repetition to become visible. A flow that most users do once per session, or that only some users see because of a flag, leaks too slowly for anyone to notice in testing. Then one customer who uses it 500 times a day reports crashes. Include flagged and power-user flows in leak tests, and include flags in memory telemetry tags.

## 431: How does a leak in one browser tab affect the rest of the browser?

Each tab usually has its own renderer process, so a leak mostly affects that tab: it slows down and eventually crashes. But it uses system RAM shared with everything else, so on a low-memory device it can cause other tabs to be discarded and the whole machine to slow down from swapping. GPU memory leaks can affect the GPU process, which is shared by all tabs.

## 432: Why can a page leak more memory in Safari or Firefox than in Chrome, or the other way around?

Each engine has its own GC, DOM implementation, image caching and JIT. A pattern that one engine handles well might keep more alive in another, for example how closures capture variables, how detached iframes are handled or how media buffers are released. Engine bugs also exist. If users on one browser report problems, reproduce the leak in that browser with its own memory tools.

## 433: How do Chrome's DevTools heap snapshots handle objects only reachable from DevTools?

Taking a snapshot tries to exclude objects that are only held by the DevTools front end, but the console history and objects you inspected can still be retained. Expanding objects in the console, using `$0`, or keeping a breakpoint on a function can keep extra things alive. Before trusting a snapshot, clear the console, deselect elements, and close panels like the Elements panel if you suspect they affect results.

## 434: Why should you take more than one snapshot after an action before concluding there is a leak?

Some objects stay alive for a short time on purpose: lazy caches, the last opened dialog kept for fast reopening, animation frames finishing, or pending network requests. One snapshot can't separate those from real leaks. If memory grows with every repetition, and not just once, you have a leak. That's why the three-snapshot technique and repeating actions many times work better than one before/after pair.

## 435: How can a framework's own caches look like leaks in heap snapshots?

Frameworks keep caches on purpose: compiled templates, style sheets, router preloads, the last value of memoized selectors or query data within its cache time. After one repetition these appear as new objects. If they don't grow with more repetitions, they're not leaks. Check the framework's docs for the cache and its limits, and repeat your action enough times to tell growth from a one-time cost.

## 436: Why might calling a cleanup function not actually free memory?

The cleanup might remove one reference but miss others. For example, you remove the listener from `window`, but the same handler was also stored in a global array, or the component instance is still in a store's subscriber list. The GC frees an object only when all paths from roots are gone. After a fix, take new snapshots and check retainers again to be sure.

## 437: How can a memory leak test give a false positive?

Common causes: measuring a development build, DevTools or extensions keeping objects alive, lazy initialization that happens on the first repetition, caches filling up to their limit, JIT compiled code being added during warm-up, and not forcing GC before measuring. Warm up first, force GC, measure several times, use a production build and use thresholds instead of exact equality.

## 438: How can a memory leak test give a false negative?

It may not repeat the action enough times for a small leak to rise above noise, it may run too short, the leak may depend on real data sizes or timing, or the test may undo the action in a way users don't (like a full page reload). Data-growth leaks also don't show up with the same data every time. Use realistic data, many repetitions and assert on object counts where possible, which are less noisy than byte totals.

## 439: Why are object counts often better than heap size for leak assertions?

Heap size changes with things unrelated to the leak: JIT code, internal caches, string tables and GC timing. Counts of specific objects, like instances of a component class, detached DOM nodes or listeners, are much more stable. "After 20 open and close cycles, there are 0 extra `Modal` instances" is a sharper and more reliable test than "heap grew by less than 2 MB".

## 440: What metrics would you put on a memory dashboard for a full stack app?

For backend services: RSS, heap used, heap total, external and arrayBuffers per instance; GC time and pause duration; event loop delay; container memory against limit; OOMKilled and restart counts; all with version and deploy markers. For the frontend: memory samples from real users by session length and version, DOM node counts in long sessions, and crash or reload rates. Alerts go on trends and closeness to limits.

## 441: How can sharing large objects between requests on purpose go wrong?

Sharing read-only data, like loaded config or a parsed dictionary, saves memory. The risk is someone mutating it, for example adding per-request fields to a shared object, which both leaks data between requests and can grow memory. Freeze shared data with `Object.freeze` (deep freeze for nested data), keep it immutable by design, and copy it before changing.

## 442: How can an append-only audit trail kept in memory become a leak?

Some code keeps an in-memory log of changes, for example for undo, auditing or debugging. Without a size limit or flushing to storage, it grows for the life of the process or session. Audit data belongs in persistent storage; keep only a small window in memory for features like undo, and flush or trim it regularly.

## 443: How would you explain the difference between memory leaks in JavaScript and in C or C++?

In C or C++ you allocate and free memory yourself, so a leak usually means you forgot to call `free` or `delete`, and the memory becomes unreachable but still allocated. In JavaScript the GC frees unreachable memory for you, so leaks happen the other way around: memory stays reachable through a reference you forgot about. C has other bugs JavaScript avoids, like use-after-free. JavaScript's leaks are logical, not about pointers.

## 444: How do garbage collected server languages like Java, Go or Python compare when it comes to leaks?

They have the same main kind of leak as JavaScript: objects kept reachable by static fields, caches, listeners, thread-locals or goroutines that never exit. Go adds goroutine leaks, where blocked goroutines keep their stacks and data. Python uses reference counting plus a cycle collector, and its C extensions can leak native memory. Java has tools like heap dumps and Eclipse MAT that work much like Chrome's heap snapshots.

## 445: Why are goroutine or thread leaks similar to promise leaks in JavaScript?

A blocked goroutine or thread waiting on a channel or lock that will never be signaled keeps its stack and everything it references alive forever. A JavaScript promise that never settles does the same with its pending callbacks and suspended async frames. In both cases the fix is to always give waiting work a way out: timeouts, cancellation (context in Go, `AbortSignal` in JS) and closing channels or rejecting promises on shutdown.

## 446: How can WebAssembly modules leak memory?

A WebAssembly instance has a linear memory (`WebAssembly.Memory`) that can grow but never shrink. If the Wasm code (for example compiled from C, C++ or Rust) leaks internally, the linear memory keeps growing. Also, JS objects that wrap Wasm-side objects (common with tools like wasm-bindgen) often need an explicit `free()` call; relying on finalizers can leave memory allocated for a long time.

## 447: Why can't WebAssembly memory shrink, and what does that mean for long-running apps?

The WebAssembly spec only lets linear memory grow. Even if the Wasm program frees most of its data, the memory stays reserved at its peak size until the instance itself is dropped. For long-running apps, a one-time spike leaves memory high forever. If that matters, run the Wasm work in a worker or a separate instance that you can throw away and recreate after heavy jobs.

## 448: How would you prevent memory leaks by design in a new full stack project?

Set rules early: every setup returns a disposer, lifetimes are tied to components, requests or sessions through `AbortSignal` or framework hooks, and all caches have size limits and TTLs. Create clients and pools once, never per request. Keep server state per request, not in module scope. Add lint rules for floating promises and subscriptions, leak tests for key flows in CI, and memory dashboards with alerts from day one.

## 449: What would you say in an interview about the most common memory leak you've fixed?

Pick a real, specific example and walk through it: the symptom (memory growth or crashes), how you confirmed it (graphs, repeated actions), how you found it (snapshot comparison and retainers), what the root cause was (for example a listener on `window` added on every route change), how you fixed it, and how you checked the fix and prevented it from coming back (a test or monitor). Interviewers care about your debugging process as much as the bug itself.

## 450: What are the key habits that prevent most memory leaks?

1. Clean up everything you set up: listeners, timers, subscriptions, observers, sockets and streams.
2. Bound every collection that lives longer than one operation: caches, queues, logs and maps.
3. Keep per-request and per-user data out of module scope on the server.
4. Use weak references only for metadata tied to objects you don't control.
5. Close resources in `finally` blocks or with `using`.
6. Measure: test repeated actions, watch memory trends in production and alert before limits.
