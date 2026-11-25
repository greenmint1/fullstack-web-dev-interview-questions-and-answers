# Web Workers & Browser Concurrency Interview Questions and Answers

_Last updated: November 25, 2026_

This file has 450 interview questions and answers about Web Workers and concurrency in the browser: 150 easy, 150 moderate and 150 advanced. It covers dedicated, shared and service workers, worklets, message passing, transferable objects, SharedArrayBuffer and Atomics, OffscreenCanvas, and main thread scheduling with the Scheduler API. The answers target the APIs available in current versions of Chrome, Edge, Firefox and Safari as of late 2026.

## Table of Contents

- [Easy Questions (1-150)](#easy-questions-1-150)
- [Moderate Questions (151-300)](#moderate-questions-151-300)
- [Advanced Questions (301-450)](#advanced-questions-301-450)

### Easy Questions (1-150)

- [1: Is JavaScript in the browser single-threaded?](#1-is-javascript-in-the-browser-single-threaded)
- [2: What is the main thread?](#2-what-is-the-main-thread)
- [3: What is a Web Worker?](#3-what-is-a-web-worker)
- [4: Why would you use a Web Worker?](#4-why-would-you-use-a-web-worker)
- [5: What is the difference between concurrency and parallelism?](#5-what-is-the-difference-between-concurrency-and-parallelism)
- [6: Does async/await make code run in parallel?](#6-does-asyncawait-make-code-run-in-parallel)
- [7: What are the main types of workers in the browser?](#7-what-are-the-main-types-of-workers-in-the-browser)
- [8: What is a dedicated worker?](#8-what-is-a-dedicated-worker)
- [9: How do you create a Web Worker?](#9-how-do-you-create-a-web-worker)
- [10: How does the main thread send data to a worker?](#10-how-does-the-main-thread-send-data-to-a-worker)
- [11: How does a worker receive messages?](#11-how-does-a-worker-receive-messages)
- [12: How does a worker send a result back to the page?](#12-how-does-a-worker-send-a-result-back-to-the-page)
- [13: What is self inside a worker?](#13-what-is-self-inside-a-worker)
- [14: Can a Web Worker access the DOM?](#14-can-a-web-worker-access-the-dom)
- [15: What APIs are available inside a Web Worker?](#15-what-apis-are-available-inside-a-web-worker)
- [16: Can you use localStorage in a Web Worker?](#16-can-you-use-localstorage-in-a-web-worker)
- [17: How do you stop a worker from the main thread?](#17-how-do-you-stop-a-worker-from-the-main-thread)
- [18: How does a worker stop itself?](#18-how-does-a-worker-stop-itself)
- [19: What is the difference between terminate() and close()?](#19-what-is-the-difference-between-terminate-and-close)
- [20: What is the structured clone algorithm?](#20-what-is-the-structured-clone-algorithm)
- [21: What happens if you try to send a function with postMessage?](#21-what-happens-if-you-try-to-send-a-function-with-postmessage)
- [22: Is the data passed to a worker shared or copied?](#22-is-the-data-passed-to-a-worker-shared-or-copied)
- [23: What are transferable objects?](#23-what-are-transferable-objects)
- [24: How do you transfer an ArrayBuffer to a worker?](#24-how-do-you-transfer-an-arraybuffer-to-a-worker)
- [25: What does it mean that a buffer is detached?](#25-what-does-it-mean-that-a-buffer-is-detached)
- [26: What is a module worker?](#26-what-is-a-module-worker)
- [27: What is a classic worker?](#27-what-is-a-classic-worker)
- [28: What does importScripts do?](#28-what-does-importscripts-do)
- [29: Can you use import statements in a worker?](#29-can-you-use-import-statements-in-a-worker)
- [30: How do you handle errors thrown inside a worker?](#30-how-do-you-handle-errors-thrown-inside-a-worker)
- [31: What is the messageerror event?](#31-what-is-the-messageerror-event)
- [32: How do you report a handled error from a worker back to the page?](#32-how-do-you-report-a-handled-error-from-a-worker-back-to-the-page)
- [33: Does a worker share global variables with the page?](#33-does-a-worker-share-global-variables-with-the-page)
- [34: Can a worker make network requests?](#34-can-a-worker-make-network-requests)
- [35: Can a worker use timers?](#35-can-a-worker-use-timers)
- [36: Does a worker have its own event loop?](#36-does-a-worker-have-its-own-event-loop)
- [37: What is navigator.hardwareConcurrency?](#37-what-is-navigatorhardwareconcurrency)
- [38: How many workers can you create?](#38-how-many-workers-can-you-create)
- [39: Is creating a worker cheap?](#39-is-creating-a-worker-cheap)
- [40: When should you not use a Web Worker?](#40-when-should-you-not-use-a-web-worker)
- [41: What is a long task?](#41-what-is-a-long-task)
- [42: How do you know if the main thread is blocked?](#42-how-do-you-know-if-the-main-thread-is-blocked)
- [43: Why does a heavy loop freeze the page?](#43-why-does-a-heavy-loop-freeze-the-page)
- [44: What is the difference between a Web Worker and a service worker?](#44-what-is-the-difference-between-a-web-worker-and-a-service-worker)
- [45: What is a shared worker?](#45-what-is-a-shared-worker)
- [46: How does a shared worker receive connections?](#46-how-does-a-shared-worker-receive-connections)
- [47: What is a MessageChannel?](#47-what-is-a-messagechannel)
- [48: What is a MessagePort?](#48-what-is-a-messageport)
- [49: What is BroadcastChannel?](#49-what-is-broadcastchannel)
- [50: What is the difference between BroadcastChannel and postMessage on a worker?](#50-what-is-the-difference-between-broadcastchannel-and-postmessage-on-a-worker)
- [51: Can a worker create another worker?](#51-can-a-worker-create-another-worker)
- [52: What is a worker script's origin rule?](#52-what-is-a-worker-scripts-origin-rule)
- [53: How can you create a worker without a separate file?](#53-how-can-you-create-a-worker-without-a-separate-file)
- [54: What is the worker-src CSP directive?](#54-what-is-the-worker-src-csp-directive)
- [55: Does a worker have access to window.location?](#55-does-a-worker-have-access-to-windowlocation)
- [56: What is navigator inside a worker?](#56-what-is-navigator-inside-a-worker)
- [57: Can you use console.log in a worker?](#57-can-you-use-consolelog-in-a-worker)
- [58: How do you debug a Web Worker in Chrome DevTools?](#58-how-do-you-debug-a-web-worker-in-chrome-devtools)
- [59: What is OffscreenCanvas?](#59-what-is-offscreencanvas)
- [60: How do you let a worker draw on a canvas that is on the page?](#60-how-do-you-let-a-worker-draw-on-a-canvas-that-is-on-the-page)
- [61: What is SharedArrayBuffer?](#61-what-is-sharedarraybuffer)
- [62: What is the Atomics object?](#62-what-is-the-atomics-object)
- [63: What does cross-origin isolated mean?](#63-what-does-cross-origin-isolated-mean)
- [64: How do you check if a page is cross-origin isolated?](#64-how-do-you-check-if-a-page-is-cross-origin-isolated)
- [65: What is a race condition?](#65-what-is-a-race-condition)
- [66: Why don't Web Workers usually have race conditions?](#66-why-dont-web-workers-usually-have-race-conditions)
- [67: What is the message passing model?](#67-what-is-the-message-passing-model)
- [68: What is the event loop?](#68-what-is-the-event-loop)
- [69: What is the difference between a task and a microtask?](#69-what-is-the-difference-between-a-task-and-a-microtask)
- [70: Is a message event a task or a microtask?](#70-is-a-message-event-a-task-or-a-microtask)
- [71: What is requestAnimationFrame?](#71-what-is-requestanimationframe)
- [72: What is requestIdleCallback?](#72-what-is-requestidlecallback)
- [73: What is the Scheduler API?](#73-what-is-the-scheduler-api)
- [74: What does scheduler.yield do?](#74-what-does-scheduleryield-do)
- [75: What is yielding to the main thread?](#75-what-is-yielding-to-the-main-thread)
- [76: What is the difference between splitting work and moving it to a worker?](#76-what-is-the-difference-between-splitting-work-and-moving-it-to-a-worker)
- [77: What is a worklet?](#77-what-is-a-worklet)
- [78: What is an AudioWorklet?](#78-what-is-an-audioworklet)
- [79: Can you use Web Workers with React?](#79-can-you-use-web-workers-with-react)
- [80: How do you create a worker in a Vite project?](#80-how-do-you-create-a-worker-in-a-vite-project)
- [81: How does webpack 5 handle workers?](#81-how-does-webpack-5-handle-workers)
- [82: What is Comlink?](#82-what-is-comlink)
- [83: Do workers run in background tabs?](#83-do-workers-run-in-background-tabs)
- [84: What is a worker's name option?](#84-what-is-a-workers-name-option)
- [85: Can a worker read files the user picked?](#85-can-a-worker-read-files-the-user-picked)
- [86: What is FileReaderSync?](#86-what-is-filereadersync)
- [87: Can a worker use IndexedDB?](#87-can-a-worker-use-indexeddb)
- [88: Can a worker use WebAssembly?](#88-can-a-worker-use-webassembly)
- [89: What does postMessage return?](#89-what-does-postmessage-return)
- [90: Is postMessage synchronous or asynchronous?](#90-is-postmessage-synchronous-or-asynchronous)
- [91: What is the difference between onmessage and addEventListener("message")?](#91-what-is-the-difference-between-onmessage-and-addeventlistenermessage)
- [92: Can you send multiple values in one postMessage?](#92-can-you-send-multiple-values-in-one-postmessage)
- [93: What is a common message format for workers?](#93-what-is-a-common-message-format-for-workers)
- [94: Can a worker use Promises and async/await?](#94-can-a-worker-use-promises-and-asyncawait)
- [95: What happens to a worker when the page is closed?](#95-what-happens-to-a-worker-when-the-page-is-closed)
- [96: Can a worker show alerts or prompts?](#96-can-a-worker-show-alerts-or-prompts)
- [97: Can a worker access cookies?](#97-can-a-worker-access-cookies)
- [98: Can a worker use the crypto API?](#98-can-a-worker-use-the-crypto-api)
- [99: What is a worker pool?](#99-what-is-a-worker-pool)
- [100: What are some real use cases for Web Workers?](#100-what-are-some-real-use-cases-for-web-workers)
- [101: What is globalThis in a worker?](#101-what-is-globalthis-in-a-worker)
- [102: How can code check if it is running inside a worker?](#102-how-can-code-check-if-it-is-running-inside-a-worker)
- [103: What is the Worker constructor's options object?](#103-what-is-the-worker-constructors-options-object)
- [104: Can you pass arguments to a worker when you create it?](#104-can-you-pass-arguments-to-a-worker-when-you-create-it)
- [105: Can you send a Map or Set to a worker?](#105-can-you-send-a-map-or-set-to-a-worker)
- [106: Can you send a Date to a worker?](#106-can-you-send-a-date-to-a-worker)
- [107: Can you send a class instance to a worker?](#107-can-you-send-a-class-instance-to-a-worker)
- [108: Is JSON.stringify needed before postMessage?](#108-is-jsonstringify-needed-before-postmessage)
- [109: What is structuredClone?](#109-what-is-structuredclone)
- [110: What is a blob URL?](#110-what-is-a-blob-url)
- [111: Can a data URL be used for a worker?](#111-can-a-data-url-be-used-for-a-worker)
- [112: What is the difference between a thread and a process?](#112-what-is-the-difference-between-a-thread-and-a-process)
- [113: Do Web Workers run in a separate process?](#113-do-web-workers-run-in-a-separate-process)
- [114: What is the compositor thread?](#114-what-is-the-compositor-thread)
- [115: Why are CSS transform animations smoother than JS animations?](#115-why-are-css-transform-animations-smoother-than-js-animations)
- [116: What is INP and how does it relate to the main thread?](#116-what-is-inp-and-how-does-it-relate-to-the-main-thread)
- [117: What does it mean for an API to be thread-safe?](#117-what-does-it-mean-for-an-api-to-be-thread-safe)
- [118: Can multiple workers run at the same time?](#118-can-multiple-workers-run-at-the-same-time)
- [119: Does a worker make code run faster?](#119-does-a-worker-make-code-run-faster)
- [120: What happens if a worker script fails to load?](#120-what-happens-if-a-worker-script-fails-to-load)
- [121: What MIME type must a worker script have?](#121-what-mime-type-must-a-worker-script-have)
- [122: Can a worker read the page's URL?](#122-can-a-worker-read-the-pages-url)
- [123: Can workers use fetch with relative URLs?](#123-can-workers-use-fetch-with-relative-urls)
- [124: What is a ReadableStream and can it be sent to a worker?](#124-what-is-a-readablestream-and-can-it-be-sent-to-a-worker)
- [125: What is the CSS Paint API?](#125-what-is-the-css-paint-api)
- [126: What is the difference between a worklet and a worker?](#126-what-is-the-difference-between-a-worklet-and-a-worker)
- [127: Can a worker use requestAnimationFrame?](#127-can-a-worker-use-requestanimationframe)
- [128: What does it mean that a worker is idle?](#128-what-does-it-mean-that-a-worker-is-idle)
- [129: How do you send a large typed array to a worker quickly?](#129-how-do-you-send-a-large-typed-array-to-a-worker-quickly)
- [130: How can the worker send the data back without copying?](#130-how-can-the-worker-send-the-data-back-without-copying)
- [131: What is the Web Locks API?](#131-what-is-the-web-locks-api)
- [132: Is Web Locks available in workers?](#132-is-web-locks-available-in-workers)
- [133: What is the difference between a SharedArrayBuffer and an ArrayBuffer?](#133-what-is-the-difference-between-a-sharedarraybuffer-and-an-arraybuffer)
- [134: Why was SharedArrayBuffer disabled for a while?](#134-why-was-sharedarraybuffer-disabled-for-a-while)
- [135: What headers are needed to enable SharedArrayBuffer?](#135-what-headers-are-needed-to-enable-sharedarraybuffer)
- [136: What is Cross-Origin-Opener-Policy?](#136-what-is-cross-origin-opener-policy)
- [137: What is Cross-Origin-Embedder-Policy?](#137-what-is-cross-origin-embedder-policy)
- [138: What is Atomics.wait?](#138-what-is-atomicswait)
- [139: Can you call Atomics.wait on the main thread?](#139-can-you-call-atomicswait-on-the-main-thread)
- [140: What is Atomics.notify?](#140-what-is-atomicsnotify)
- [141: What is the difference between a worker and a child process in Node.js?](#141-what-is-the-difference-between-a-worker-and-a-child-process-in-nodejs)
- [142: What is the main difference between browser Web Workers and Node.js worker_threads?](#142-what-is-the-main-difference-between-browser-web-workers-and-nodejs-worker_threads)
- [143: What is a service worker used for?](#143-what-is-a-service-worker-used-for)
- [144: Should you run heavy computation in a service worker?](#144-should-you-run-heavy-computation-in-a-service-worker)
- [145: Can a worker be used by an iframe?](#145-can-a-worker-be-used-by-an-iframe)
- [146: What is a race between two postMessage calls?](#146-what-is-a-race-between-two-postmessage-calls)
- [147: Are messages from a worker delivered in order?](#147-are-messages-from-a-worker-delivered-in-order)
- [148: How do you clean up event listeners on a worker?](#148-how-do-you-clean-up-event-listeners-on-a-worker)
- [149: What is the TypeScript setup for writing a worker?](#149-what-is-the-typescript-setup-for-writing-a-worker)
- [150: What is the simplest way to explain Web Workers to a beginner?](#150-what-is-the-simplest-way-to-explain-web-workers-to-a-beginner)

### Moderate Questions (151-300)

- [151: How do you wrap a worker call in a Promise?](#151-how-do-you-wrap-a-worker-call-in-a-promise)
- [152: Why do you need request IDs when talking to a worker?](#152-why-do-you-need-request-ids-when-talking-to-a-worker)
- [153: How do you handle a worker crash in a promise wrapper?](#153-how-do-you-handle-a-worker-crash-in-a-promise-wrapper)
- [154: How do you add a timeout to a worker request?](#154-how-do-you-add-a-timeout-to-a-worker-request)
- [155: How do you cancel a task running in a worker?](#155-how-do-you-cancel-a-task-running-in-a-worker)
- [156: How do you use AbortController with a worker call?](#156-how-do-you-use-abortcontroller-with-a-worker-call)
- [157: How does a worker check for a cancel message during a long loop?](#157-how-does-a-worker-check-for-a-cancel-message-during-a-long-loop)
- [158: How do you report progress from a worker?](#158-how-do-you-report-progress-from-a-worker)
- [159: How do you build a simple worker pool?](#159-how-do-you-build-a-simple-worker-pool)
- [160: How do you choose the size of a worker pool?](#160-how-do-you-choose-the-size-of-a-worker-pool)
- [161: How do you split a large array across multiple workers?](#161-how-do-you-split-a-large-array-across-multiple-workers)
- [162: When is copying data to a worker slower than doing the work on the main thread?](#162-when-is-copying-data-to-a-worker-slower-than-doing-the-work-on-the-main-thread)
- [163: How do you measure the cost of postMessage?](#163-how-do-you-measure-the-cost-of-postmessage)
- [164: What kinds of objects are slow to clone?](#164-what-kinds-of-objects-are-slow-to-clone)
- [165: How can you make large data cheaper to send to a worker?](#165-how-can-you-make-large-data-cheaper-to-send-to-a-worker)
- [166: What is a columnar data layout and why does it help with workers?](#166-what-is-a-columnar-data-layout-and-why-does-it-help-with-workers)
- [167: What does the transfer option in structuredClone do?](#167-what-does-the-transfer-option-in-structuredclone-do)
- [168: What is ArrayBuffer.prototype.transfer?](#168-what-is-arraybufferprototypetransfer)
- [169: What happens if you list the same buffer twice in a transfer list?](#169-what-happens-if-you-list-the-same-buffer-twice-in-a-transfer-list)
- [170: Can you transfer a typed array directly?](#170-can-you-transfer-a-typed-array-directly)
- [171: How do you transfer a MessagePort to a worker?](#171-how-do-you-transfer-a-messageport-to-a-worker)
- [172: How do two workers talk to each other directly?](#172-how-do-two-workers-talk-to-each-other-directly)
- [173: Why do you need to call port.start()?](#173-why-do-you-need-to-call-portstart)
- [174: How do you close a MessagePort?](#174-how-do-you-close-a-messageport)
- [175: How do you sync state across tabs with BroadcastChannel?](#175-how-do-you-sync-state-across-tabs-with-broadcastchannel)
- [176: What is the difference between BroadcastChannel and the storage event?](#176-what-is-the-difference-between-broadcastchannel-and-the-storage-event)
- [177: When would you use a SharedWorker instead of BroadcastChannel?](#177-when-would-you-use-a-sharedworker-instead-of-broadcastchannel)
- [178: How do you share one WebSocket connection across tabs?](#178-how-do-you-share-one-websocket-connection-across-tabs)
- [179: How does a shared worker know a tab has closed?](#179-how-does-a-shared-worker-know-a-tab-has-closed)
- [180: What are the limits of SharedWorker support?](#180-what-are-the-limits-of-sharedworker-support)
- [181: How do you debug a SharedWorker?](#181-how-do-you-debug-a-sharedworker)
- [182: What is the name option for a SharedWorker?](#182-what-is-the-name-option-for-a-sharedworker)
- [183: How do you handle errors in a SharedWorker?](#183-how-do-you-handle-errors-in-a-sharedworker)
- [184: What is the difference between a dedicated worker and a SharedWorker in how you send messages?](#184-what-is-the-difference-between-a-dedicated-worker-and-a-sharedworker-in-how-you-send-messages)
- [185: How do you use OffscreenCanvas for chart rendering in a worker?](#185-how-do-you-use-offscreencanvas-for-chart-rendering-in-a-worker)
- [186: How do you handle canvas resizing with OffscreenCanvas?](#186-how-do-you-handle-canvas-resizing-with-offscreencanvas)
- [187: How do you handle mouse events with an OffscreenCanvas in a worker?](#187-how-do-you-handle-mouse-events-with-an-offscreencanvas-in-a-worker)
- [188: What is createImageBitmap and why is it useful in workers?](#188-what-is-createimagebitmap-and-why-is-it-useful-in-workers)
- [189: How do you resize an image in a worker?](#189-how-do-you-resize-an-image-in-a-worker)
- [190: What does ImageBitmap.close do?](#190-what-does-imagebitmapclose-do)
- [191: How do you apply a pixel filter in a worker?](#191-how-do-you-apply-a-pixel-filter-in-a-worker)
- [192: How do you parse a big JSON file in a worker?](#192-how-do-you-parse-a-big-json-file-in-a-worker)
- [193: Is JSON.parse in a worker always a win?](#193-is-jsonparse-in-a-worker-always-a-win)
- [194: How do you stream and process a large CSV file in a worker?](#194-how-do-you-stream-and-process-a-large-csv-file-in-a-worker)
- [195: How do you run a search index in a worker?](#195-how-do-you-run-a-search-index-in-a-worker)
- [196: How do you debounce search input that goes to a worker?](#196-how-do-you-debounce-search-input-that-goes-to-a-worker)
- [197: How do you load WebAssembly in a worker?](#197-how-do-you-load-webassembly-in-a-worker)
- [198: What happens to messages that arrive before a module worker finishes its top-level await?](#198-what-happens-to-messages-that-arrive-before-a-module-worker-finishes-its-top-level-await)
- [199: How do you implement a ready handshake with a worker?](#199-how-do-you-implement-a-ready-handshake-with-a-worker)
- [200: How do you send a compiled WebAssembly module to several workers?](#200-how-do-you-send-a-compiled-webassembly-module-to-several-workers)
- [201: How do you use scheduler.postTask with priorities?](#201-how-do-you-use-schedulerposttask-with-priorities)
- [202: How do you cancel a task scheduled with postTask?](#202-how-do-you-cancel-a-task-scheduled-with-posttask)
- [203: How do you add a delay with scheduler.postTask?](#203-how-do-you-add-a-delay-with-schedulerposttask)
- [204: What is the difference between scheduler.yield and setTimeout(0)?](#204-what-is-the-difference-between-scheduleryield-and-settimeout0)
- [205: How do you write a yield helper that works in all browsers?](#205-how-do-you-write-a-yield-helper-that-works-in-all-browsers)
- [206: Why not yield after every single item?](#206-why-not-yield-after-every-single-item)
- [207: What was navigator.scheduling.isInputPending?](#207-what-was-navigatorschedulingisinputpending)
- [208: How do you make a click handler respond faster when it has heavy work?](#208-how-do-you-make-a-click-handler-respond-faster-when-it-has-heavy-work)
- [209: How does requestAnimationFrame plus setTimeout help to run code after paint?](#209-how-does-requestanimationframe-plus-settimeout-help-to-run-code-after-paint)
- [210: How do you test a module that uses Web Workers in Vitest or Jest?](#210-how-do-you-test-a-module-that-uses-web-workers-in-vitest-or-jest)
- [211: Why is it good to keep worker logic in separate pure functions?](#211-why-is-it-good-to-keep-worker-logic-in-separate-pure-functions)
- [212: How do you test Web Workers end to end with Playwright?](#212-how-do-you-test-web-workers-end-to-end-with-playwright)
- [213: What CSP issues come up with workers?](#213-what-csp-issues-come-up-with-workers)
- [214: How do Trusted Types affect worker creation?](#214-how-do-trusted-types-affect-worker-creation)
- [215: Can a module worker import scripts from a CDN?](#215-can-a-module-worker-import-scripts-from-a-cdn)
- [216: How do you load a worker script from a CDN when the same-origin rule blocks it?](#216-how-do-you-load-a-worker-script-from-a-cdn-when-the-same-origin-rule-blocks-it)
- [217: How do you use Web Workers in Angular?](#217-how-do-you-use-web-workers-in-angular)
- [218: How do you use Web Workers in Next.js?](#218-how-do-you-use-web-workers-in-nextjs)
- [219: Why should workers be created inside useEffect in React, not during render?](#219-why-should-workers-be-created-inside-useeffect-in-react-not-during-render)
- [220: Why might a worker be created twice in React development mode?](#220-why-might-a-worker-be-created-twice-in-react-development-mode)
- [221: How do you share a single worker across many components?](#221-how-do-you-share-a-single-worker-across-many-components)
- [222: What problems can Comlink solve and what are its limits?](#222-what-problems-can-comlink-solve-and-what-are-its-limits)
- [223: How do you pass a callback to a worker with Comlink?](#223-how-do-you-pass-a-callback-to-a-worker-with-comlink)
- [224: How do you transfer a buffer with Comlink?](#224-how-do-you-transfer-a-buffer-with-comlink)
- [225: What is the difference between importScripts and dynamic import in workers?](#225-what-is-the-difference-between-importscripts-and-dynamic-import-in-workers)
- [226: How do you use fetch with a progress indicator inside a worker?](#226-how-do-you-use-fetch-with-a-progress-indicator-inside-a-worker)
- [227: How do you compress data in a worker?](#227-how-do-you-compress-data-in-a-worker)
- [228: Can a worker use the Origin Private File System?](#228-can-a-worker-use-the-origin-private-file-system)
- [229: Why are sync access handles only in workers?](#229-why-are-sync-access-handles-only-in-workers)
- [230: How do you run SQLite in the browser with a worker?](#230-how-do-you-run-sqlite-in-the-browser-with-a-worker)
- [231: How do you handle unhandled promise rejections inside a worker?](#231-how-do-you-handle-unhandled-promise-rejections-inside-a-worker)
- [232: How do you send logs from a worker to your error tracking?](#232-how-do-you-send-logs-from-a-worker-to-your-error-tracking)
- [233: Do Error objects keep their stack when sent with postMessage?](#233-do-error-objects-keep-their-stack-when-sent-with-postmessage)
- [234: How do source maps work with workers?](#234-how-do-source-maps-work-with-workers)
- [235: What are common mistakes when using Web Workers?](#235-what-are-common-mistakes-when-using-web-workers)
- [236: How do you find memory leaks related to workers?](#236-how-do-you-find-memory-leaks-related-to-workers)
- [237: Why can a pending-requests map cause memory leaks?](#237-why-can-a-pending-requests-map-cause-memory-leaks)
- [238: What is the cost of a worker's memory?](#238-what-is-the-cost-of-a-workers-memory)
- [239: How do you decide what runs on the main thread and what runs in a worker?](#239-how-do-you-decide-what-runs-on-the-main-thread-and-what-runs-in-a-worker)
- [240: What is the "off main thread" architecture?](#240-what-is-the-off-main-thread-architecture)
- [241: How can you run a Redux-style store in a worker?](#241-how-can-you-run-a-redux-style-store-in-a-worker)
- [242: What is Partytown?](#242-what-is-partytown)
- [243: How do you handle third-party scripts that block the main thread?](#243-how-do-you-handle-third-party-scripts-that-block-the-main-thread)
- [244: What is the Long Animation Frames API?](#244-what-is-the-long-animation-frames-api)
- [245: How do you measure how long a task took inside a worker?](#245-how-do-you-measure-how-long-a-task-took-inside-a-worker)
- [246: Are performance.now() values in a worker comparable with the page's?](#246-are-performancenow-values-in-a-worker-comparable-with-the-pages)
- [247: How do you see worker activity in the Performance panel?](#247-how-do-you-see-worker-activity-in-the-performance-panel)
- [248: What does "DataCloneError: could not be cloned" usually mean?](#248-what-does-datacloneerror-could-not-be-cloned-usually-mean)
- [249: Can you send a Proxy or a Vue/MobX reactive object to a worker?](#249-can-you-send-a-proxy-or-a-vuemobx-reactive-object-to-a-worker)
- [250: How do you use BigInt with workers?](#250-how-do-you-use-bigint-with-workers)
- [251: How do you enable cross-origin isolation on a static host?](#251-how-do-you-enable-cross-origin-isolation-on-a-static-host)
- [252: What breaks when you turn on COEP require-corp?](#252-what-breaks-when-you-turn-on-coep-require-corp)
- [253: What breaks when you turn on COOP same-origin?](#253-what-breaks-when-you-turn-on-coop-same-origin)
- [254: What is COEP credentialless?](#254-what-is-coep-credentialless)
- [255: How do you use SharedArrayBuffer when you can't set headers?](#255-how-do-you-use-sharedarraybuffer-when-you-cant-set-headers)
- [256: How do you share a counter between threads safely?](#256-how-do-you-share-a-counter-between-threads-safely)
- [257: Why is counter[0]++ unsafe on shared memory?](#257-why-is-counter0-unsafe-on-shared-memory)
- [258: What does Atomics.compareExchange do?](#258-what-does-atomicscompareexchange-do)
- [259: What is the difference between Atomics.load and a normal read?](#259-what-is-the-difference-between-atomicsload-and-a-normal-read)
- [260: How do you signal a worker that new data is ready using Atomics?](#260-how-do-you-signal-a-worker-that-new-data-is-ready-using-atomics)
- [261: How does Atomics.waitAsync work?](#261-how-does-atomicswaitasync-work)
- [262: How do you tell a worker to stop a loop using shared memory?](#262-how-do-you-tell-a-worker-to-stop-a-loop-using-shared-memory)
- [263: What is a growable SharedArrayBuffer?](#263-what-is-a-growable-sharedarraybuffer)
- [264: What is a resizable ArrayBuffer and can it be transferred?](#264-what-is-a-resizable-arraybuffer-and-can-it-be-transferred)
- [265: How do you share a large read-only dataset across many workers?](#265-how-do-you-share-a-large-read-only-dataset-across-many-workers)
- [266: Why is it safe to read shared data without Atomics if it was written before posting?](#266-why-is-it-safe-to-read-shared-data-without-atomics-if-it-was-written-before-posting)
- [267: What is a service worker message channel used for?](#267-what-is-a-service-worker-message-channel-used-for)
- [268: Can a dedicated worker talk to the service worker?](#268-can-a-dedicated-worker-talk-to-the-service-worker)
- [269: Do fetch requests from a worker go through the service worker?](#269-do-fetch-requests-from-a-worker-go-through-the-service-worker)
- [270: How do you send a message from a service worker to all open tabs?](#270-how-do-you-send-a-message-from-a-service-worker-to-all-open-tabs)
- [271: When should you use BroadcastChannel versus clients.matchAll in a service worker?](#271-when-should-you-use-broadcastchannel-versus-clientsmatchall-in-a-service-worker)
- [272: How do you pick between Web Locks and a SharedWorker to coordinate tabs?](#272-how-do-you-pick-between-web-locks-and-a-sharedworker-to-coordinate-tabs)
- [273: How do you elect a leader tab with Web Locks?](#273-how-do-you-elect-a-leader-tab-with-web-locks)
- [274: What happens to a held Web Lock when a tab crashes?](#274-what-happens-to-a-held-web-lock-when-a-tab-crashes)
- [275: How do you request a Web Lock without waiting?](#275-how-do-you-request-a-web-lock-without-waiting)
- [276: What are shared locks in the Web Locks API?](#276-what-are-shared-locks-in-the-web-locks-api)
- [277: How do you prevent the UI from freezing when rendering a long list?](#277-how-do-you-prevent-the-ui-from-freezing-when-rendering-a-long-list)
- [278: How do you sort a large dataset in a worker and keep the UI responsive?](#278-how-do-you-sort-a-large-dataset-in-a-worker-and-keep-the-ui-responsive)
- [279: How do you use workers for syntax highlighting in an editor?](#279-how-do-you-use-workers-for-syntax-highlighting-in-an-editor)
- [280: How does Monaco Editor use web workers?](#280-how-does-monaco-editor-use-web-workers)
- [281: What is the "actor model" in the context of web workers?](#281-what-is-the-actor-model-in-the-context-of-web-workers)
- [282: How do you pass messages between workers in a pipeline?](#282-how-do-you-pass-messages-between-workers-in-a-pipeline)
- [283: How do you apply backpressure when sending data to a worker?](#283-how-do-you-apply-backpressure-when-sending-data-to-a-worker)
- [284: How do transferable streams help with backpressure?](#284-how-do-transferable-streams-help-with-backpressure)
- [285: How do you use a TransformStream in a worker?](#285-how-do-you-use-a-transformstream-in-a-worker)
- [286: How do you keep animations smooth while a worker runs?](#286-how-do-you-keep-animations-smooth-while-a-worker-runs)
- [287: Can too many worker messages hurt the main thread?](#287-can-too-many-worker-messages-hurt-the-main-thread)
- [288: How do you implement a debounced save in a worker?](#288-how-do-you-implement-a-debounced-save-in-a-worker)
- [289: What is the difference between Web Workers and Web Workers with WebAssembly threads?](#289-what-is-the-difference-between-web-workers-and-web-workers-with-webassembly-threads)
- [290: How do Emscripten pthreads work in the browser?](#290-how-do-emscripten-pthreads-work-in-the-browser)
- [291: What is wasm-bindgen-rayon?](#291-what-is-wasm-bindgen-rayon)
- [292: How do you fall back when SharedArrayBuffer isn't available?](#292-how-do-you-fall-back-when-sharedarraybuffer-isnt-available)
- [293: How do you share code between the page and a worker without duplicating bundles?](#293-how-do-you-share-code-between-the-page-and-a-worker-without-duplicating-bundles)
- [294: How do you handle worker versioning when you deploy a new release?](#294-how-do-you-handle-worker-versioning-when-you-deploy-a-new-release)
- [295: How do you restart a worker that crashed?](#295-how-do-you-restart-a-worker-that-crashed)
- [296: What happens when a worker runs out of memory?](#296-what-happens-when-a-worker-runs-out-of-memory)
- [297: How do you avoid running workers during server-side rendering?](#297-how-do-you-avoid-running-workers-during-server-side-rendering)
- [298: How do you lazy-load a worker only when needed?](#298-how-do-you-lazy-load-a-worker-only-when-needed)
- [299: How do you preload a worker script?](#299-how-do-you-preload-a-worker-script)
- [300: How do you explain the trade-offs of using Web Workers in a code review?](#300-how-do-you-explain-the-trade-offs-of-using-web-workers-in-a-code-review)

### Advanced Questions (301-450)

- [301: How does the browser actually send a message between threads?](#301-how-does-the-browser-actually-send-a-message-between-threads)
- [302: Why does postMessage cost time on both threads?](#302-why-does-postmessage-cost-time-on-both-threads)
- [303: What is an agent and an agent cluster in the JavaScript spec?](#303-what-is-an-agent-and-an-agent-cluster-in-the-javascript-spec)
- [304: Why can't a SharedArrayBuffer be sent to a service worker from a page?](#304-why-cant-a-sharedarraybuffer-be-sent-to-a-service-worker-from-a-page)
- [305: What is the JavaScript memory model in simple terms?](#305-what-is-the-javascript-memory-model-in-simple-terms)
- [306: What is tearing in shared memory?](#306-what-is-tearing-in-shared-memory)
- [307: What is a data race and why are they dangerous even in JavaScript?](#307-what-is-a-data-race-and-why-are-they-dangerous-even-in-javascript)
- [308: How do you implement a mutex with SharedArrayBuffer and Atomics?](#308-how-do-you-implement-a-mutex-with-sharedarraybuffer-and-atomics)
- [309: How would you make a mutex usable from the main thread?](#309-how-would-you-make-a-mutex-usable-from-the-main-thread)
- [310: What is the problem with the simple two-state mutex?](#310-what-is-the-problem-with-the-simple-two-state-mutex)
- [311: What is a spin lock and why is it usually bad in the browser?](#311-what-is-a-spin-lock-and-why-is-it-usually-bad-in-the-browser)
- [312: How do you build a single-producer single-consumer ring buffer with shared memory?](#312-how-do-you-build-a-single-producer-single-consumer-ring-buffer-with-shared-memory)
- [313: Why does the ring buffer write the data before updating the index?](#313-why-does-the-ring-buffer-write-the-data-before-updating-the-index)
- [314: Where are ring buffers with SharedArrayBuffer used in practice?](#314-where-are-ring-buffers-with-sharedarraybuffer-used-in-practice)
- [315: Why shouldn't you use postMessage inside an AudioWorklet's process method?](#315-why-shouldnt-you-use-postmessage-inside-an-audioworklets-process-method)
- [316: What constraints does code inside an AudioWorkletProcessor have?](#316-what-constraints-does-code-inside-an-audioworkletprocessor-have)
- [317: What is false sharing?](#317-what-is-false-sharing)
- [318: Why is high-resolution timing tied to cross-origin isolation?](#318-why-is-high-resolution-timing-tied-to-cross-origin-isolation)
- [319: How could SharedArrayBuffer be used as a timer in an attack?](#319-how-could-sharedarraybuffer-be-used-as-a-timer-in-an-attack)
- [320: Is a Web Worker a security sandbox for untrusted code?](#320-is-a-web-worker-a-security-sandbox-for-untrusted-code)
- [321: How can you run untrusted user code more safely in the browser?](#321-how-can-you-run-untrusted-user-code-more-safely-in-the-browser)
- [322: How do you enforce a time limit on untrusted or buggy code in a worker?](#322-how-do-you-enforce-a-time-limit-on-untrusted-or-buggy-code-in-a-worker)
- [323: What should you validate in messages coming from a worker or another window?](#323-what-should-you-validate-in-messages-coming-from-a-worker-or-another-window)
- [324: Can a worker be used to bypass Content Security Policy?](#324-can-a-worker-be-used-to-bypass-content-security-policy)
- [325: How does storage partitioning affect shared workers?](#325-how-does-storage-partitioning-affect-shared-workers)
- [326: How does storage partitioning affect BroadcastChannel?](#326-how-does-storage-partitioning-affect-broadcastchannel)
- [327: What happens to workers in a page that enters the back/forward cache?](#327-what-happens-to-workers-in-a-page-that-enters-the-backforward-cache)
- [328: How do mobile browsers treat workers in the background?](#328-how-do-mobile-browsers-treat-workers-in-the-background)
- [329: What is the Page Lifecycle API and how does it relate to workers?](#329-what-is-the-page-lifecycle-api-and-how-does-it-relate-to-workers)
- [330: How are timers in workers throttled compared to the main thread?](#330-how-are-timers-in-workers-throttled-compared-to-the-main-thread)
- [331: Why do some apps run a timer inside a worker?](#331-why-do-some-apps-run-a-timer-inside-a-worker)
- [332: How does a worker's event loop differ from the main thread's?](#332-how-does-a-workers-event-loop-differ-from-the-main-threads)
- [333: What happens if a worker runs an infinite loop?](#333-what-happens-if-a-worker-runs-an-infinite-loop)
- [334: How do you design a worker pool with priorities?](#334-how-do-you-design-a-worker-pool-with-priorities)
- [335: What is work stealing and is it useful in browser worker pools?](#335-what-is-work-stealing-and-is-it-useful-in-browser-worker-pools)
- [336: How do you choose chunk sizes when splitting work across workers?](#336-how-do-you-choose-chunk-sizes-when-splitting-work-across-workers)
- [337: Why might parallel code in workers be slower than single-threaded code?](#337-why-might-parallel-code-in-workers-be-slower-than-single-threaded-code)
- [338: How does the JIT warm-up affect workers?](#338-how-does-the-jit-warm-up-affect-workers)
- [339: How do big.LITTLE CPUs on phones affect worker performance?](#339-how-do-biglittle-cpus-on-phones-affect-worker-performance)
- [340: What is Amdahl's law and why does it matter for workers?](#340-what-is-amdahls-law-and-why-does-it-matter-for-workers)
- [341: How do you merge results from many workers efficiently?](#341-how-do-you-merge-results-from-many-workers-efficiently)
- [342: How would you design a client-side image editor with workers?](#342-how-would-you-design-a-client-side-image-editor-with-workers)
- [343: How would you design a spreadsheet calculation engine using workers?](#343-how-would-you-design-a-spreadsheet-calculation-engine-using-workers)
- [344: How would you build offline full-text search for a docs site?](#344-how-would-you-build-offline-full-text-search-for-a-docs-site)
- [345: How would you design a live dashboard that receives thousands of updates per second?](#345-how-would-you-design-a-live-dashboard-that-receives-thousands-of-updates-per-second)
- [346: How do you avoid sending stale results from a worker after the input changed?](#346-how-do-you-avoid-sending-stale-results-from-a-worker-after-the-input-changed)
- [347: How does Figma-style or Google Docs-style rendering use workers and WASM?](#347-how-does-figma-style-or-google-docs-style-rendering-use-workers-and-wasm)
- [348: How do you use WebGPU from a worker?](#348-how-do-you-use-webgpu-from-a-worker)
- [349: How do you run ML models in the browser without blocking the UI?](#349-how-do-you-run-ml-models-in-the-browser-without-blocking-the-ui)
- [350: What is the WebAssembly threads proposal and its main parts?](#350-what-is-the-webassembly-threads-proposal-and-its-main-parts)
- [351: How do you create a shared WebAssembly memory?](#351-how-do-you-create-a-shared-webassembly-memory)
- [352: What happens to typed array views when shared WebAssembly memory grows?](#352-what-happens-to-typed-array-views-when-shared-webassembly-memory-grows)
- [353: Why is Atomics.wait not allowed on the main thread, and how do WASM threads deal with it?](#353-why-is-atomicswait-not-allowed-on-the-main-thread-and-how-do-wasm-threads-deal-with-it)
- [354: What is the PROXY_TO_PTHREAD pattern?](#354-what-is-the-proxy_to_pthread-pattern)
- [355: How can a deadlock happen with workers?](#355-how-can-a-deadlock-happen-with-workers)
- [356: How do you debug a suspected deadlock between workers?](#356-how-do-you-debug-a-suspected-deadlock-between-workers)
- [357: What is the ABA problem?](#357-what-is-the-aba-problem)
- [358: How would you synchronize a structured record (several fields) between threads without a lock?](#358-how-would-you-synchronize-a-structured-record-several-fields-between-threads-without-a-lock)
- [359: How do you implement a semaphore with Atomics?](#359-how-do-you-implement-a-semaphore-with-atomics)
- [360: What is a barrier and how would you build one for workers?](#360-what-is-a-barrier-and-how-would-you-build-one-for-workers)
- [361: What does Atomics.wait return if the value already changed?](#361-what-does-atomicswait-return-if-the-value-already-changed)
- [362: What is the lost wakeup problem?](#362-what-is-the-lost-wakeup-problem)
- [363: Can Atomics.notify wake a waitAsync waiter on the main thread?](#363-can-atomicsnotify-wake-a-waitasync-waiter-on-the-main-thread)
- [364: What is a typical way to build synchronous calls from a worker to the main thread?](#364-what-is-a-typical-way-to-build-synchronous-calls-from-a-worker-to-the-main-thread)
- [365: Why would code in a worker need synchronous calls to the main thread?](#365-why-would-code-in-a-worker-need-synchronous-calls-to-the-main-thread)
- [366: What is the alternative to SharedArrayBuffer for synchronous worker calls on pages that aren't cross-origin isolated?](#366-what-is-the-alternative-to-sharedarraybuffer-for-synchronous-worker-calls-on-pages-that-arent-cross-origin-isolated)
- [367: What is Atomics.pause?](#367-what-is-atomicspause)
- [368: How do you avoid allocation and GC pauses in a hot worker loop?](#368-how-do-you-avoid-allocation-and-gc-pauses-in-a-hot-worker-loop)
- [369: Does garbage collection in a worker pause the main thread?](#369-does-garbage-collection-in-a-worker-pause-the-main-thread)
- [370: How do you measure memory used by workers?](#370-how-do-you-measure-memory-used-by-workers)
- [371: What happens to the transfer list if postMessage throws?](#371-what-happens-to-the-transfer-list-if-postmessage-throws)
- [372: Can you transfer an ArrayBuffer that a WebAssembly.Memory uses?](#372-can-you-transfer-an-arraybuffer-that-a-webassemblymemory-uses)
- [373: What are the security considerations for transferring OffscreenCanvas?](#373-what-are-the-security-considerations-for-transferring-offscreencanvas)
- [374: How does OffscreenCanvas rendering in a worker reach the screen?](#374-how-does-offscreencanvas-rendering-in-a-worker-reach-the-screen)
- [375: What is the difference between drawing to a transferred OffscreenCanvas and a standalone one?](#375-what-is-the-difference-between-drawing-to-a-transferred-offscreencanvas-and-a-standalone-one)
- [376: How do you sync OffscreenCanvas animation in a worker with the display refresh?](#376-how-do-you-sync-offscreencanvas-animation-in-a-worker-with-the-display-refresh)
- [377: What is ImageBitmapRenderingContext used for?](#377-what-is-imagebitmaprenderingcontext-used-for)
- [378: How do you process video frames in a worker?](#378-how-do-you-process-video-frames-in-a-worker)
- [379: Why must you close VideoFrame objects quickly?](#379-why-must-you-close-videoframe-objects-quickly)
- [380: How does WebCodecs fit with workers?](#380-how-does-webcodecs-fit-with-workers)
- [381: What happens to a message posted to a worker that was already terminated?](#381-what-happens-to-a-message-posted-to-a-worker-that-was-already-terminated)
- [382: What happens if the main thread posts a message before the worker script has loaded?](#382-what-happens-if-the-main-thread-posts-a-message-before-the-worker-script-has-loaded)
- [383: What happens to queued messages if the worker throws during startup?](#383-what-happens-to-queued-messages-if-the-worker-throws-during-startup)
- [384: How does the browser decide whether to reuse an existing SharedWorker?](#384-how-does-the-browser-decide-whether-to-reuse-an-existing-sharedworker)
- [385: How do you upgrade a long-running SharedWorker to a new version?](#385-how-do-you-upgrade-a-long-running-sharedworker-to-a-new-version)
- [386: How do you handle a SharedWorker that becomes a single point of failure?](#386-how-do-you-handle-a-sharedworker-that-becomes-a-single-point-of-failure)
- [387: How do you protect a SharedWorker from a bad or old tab?](#387-how-do-you-protect-a-sharedworker-from-a-bad-or-old-tab)
- [388: How do you share an authenticated session across tabs safely?](#388-how-do-you-share-an-authenticated-session-across-tabs-safely)
- [389: How do you avoid the thundering herd when many tabs wake up at once?](#389-how-do-you-avoid-the-thundering-herd-when-many-tabs-wake-up-at-once)
- [390: How does a service worker's lifetime affect long tasks?](#390-how-does-a-service-workers-lifetime-affect-long-tasks)
- [391: Can you use SharedArrayBuffer in a SharedWorker?](#391-can-you-use-sharedarraybuffer-in-a-sharedworker)
- [392: How do you make a dedicated worker cross-origin isolated?](#392-how-do-you-make-a-dedicated-worker-cross-origin-isolated)
- [393: What happens if one iframe on an isolated page isn't served with COEP?](#393-what-happens-if-one-iframe-on-an-isolated-page-isnt-served-with-coep)
- [394: What is the Document-Isolation-Policy header?](#394-what-is-the-document-isolation-policy-header)
- [395: How do you test a feature that depends on SharedArrayBuffer in CI?](#395-how-do-you-test-a-feature-that-depends-on-sharedarraybuffer-in-ci)
- [396: How would you profile postMessage overhead in a real app?](#396-how-would-you-profile-postmessage-overhead-in-a-real-app)
- [397: Why can sending many small objects be slower than sending one big typed array?](#397-why-can-sending-many-small-objects-be-slower-than-sending-one-big-typed-array)
- [398: Is sending a JSON string ever faster than sending an object?](#398-is-sending-a-json-string-ever-faster-than-sending-an-object)
- [399: How does Blob passing work without copying large data?](#399-how-does-blob-passing-work-without-copying-large-data)
- [400: How would you hash a multi-gigabyte file in the browser without running out of memory?](#400-how-would-you-hash-a-multi-gigabyte-file-in-the-browser-without-running-out-of-memory)
- [401: How would you design a generic RPC layer for workers?](#401-how-would-you-design-a-generic-rpc-layer-for-workers)
- [402: How do you design worker APIs to avoid chatty communication?](#402-how-do-you-design-worker-apis-to-avoid-chatty-communication)
- [403: How do you keep type safety across the worker boundary in TypeScript?](#403-how-do-you-keep-type-safety-across-the-worker-boundary-in-typescript)
- [404: How do you handle errors that cross the worker boundary in a typed way?](#404-how-do-you-handle-errors-that-cross-the-worker-boundary-in-a-typed-way)
- [405: Why is instanceof unreliable for objects received from a worker?](#405-why-is-instanceof-unreliable-for-objects-received-from-a-worker)
- [406: What happens to object identity and circular references when posting a message?](#406-what-happens-to-object-identity-and-circular-references-when-posting-a-message)
- [407: How do you keep a large state in a worker and sync only changes to the UI?](#407-how-do-you-keep-a-large-state-in-a-worker-and-sync-only-changes-to-the-ui)
- [408: What are the risks of putting app state in a worker?](#408-what-are-the-risks-of-putting-app-state-in-a-worker)
- [409: How should a text input that depends on worker results stay responsive?](#409-how-should-a-text-input-that-depends-on-worker-results-stay-responsive)
- [410: How do you handle ordering when several workers produce results for the same view?](#410-how-do-you-handle-ordering-when-several-workers-produce-results-for-the-same-view)
- [411: How do you implement speculative work in a worker?](#411-how-do-you-implement-speculative-work-in-a-worker)
- [412: How would you implement a worker-side LRU cache for expensive computations?](#412-how-would-you-implement-a-worker-side-lru-cache-for-expensive-computations)
- [413: How do you decide between one worker and a pool for an app feature?](#413-how-do-you-decide-between-one-worker-and-a-pool-for-an-app-feature)
- [414: How do you make a worker pool adapt to the device?](#414-how-do-you-make-a-worker-pool-adapt-to-the-device)
- [415: What is navigator.deviceMemory and how does it help with workers?](#415-what-is-navigatordevicememory-and-how-does-it-help-with-workers)
- [416: How does the browser schedule worker threads on CPU cores?](#416-how-does-the-browser-schedule-worker-threads-on-cpu-cores)
- [417: What is priority inversion and can it happen with workers?](#417-what-is-priority-inversion-and-can-it-happen-with-workers)
- [418: How do scheduler priorities in the main thread interact with workers?](#418-how-do-scheduler-priorities-in-the-main-thread-interact-with-workers)
- [419: How does scheduler.yield keep priority with postTask?](#419-how-does-scheduleryield-keep-priority-with-posttask)
- [420: How do you break up a long main-thread task that must run in a specific order?](#420-how-do-you-break-up-a-long-main-thread-task-that-must-run-in-a-specific-order)
- [421: What is the interaction between microtasks and yielding?](#421-what-is-the-interaction-between-microtasks-and-yielding)
- [422: Why do some libraries use MessageChannel as a scheduler?](#422-why-do-some-libraries-use-messagechannel-as-a-scheduler)
- [423: How does React's concurrent rendering relate to browser concurrency?](#423-how-does-reacts-concurrent-rendering-relate-to-browser-concurrency)
- [424: When is cooperative scheduling better than a worker?](#424-when-is-cooperative-scheduling-better-than-a-worker)
- [425: How would you diagnose a poor INP score in an app that already uses workers?](#425-how-would-you-diagnose-a-poor-inp-score-in-an-app-that-already-uses-workers)
- [426: What is the impact of structured clone on the main thread when a worker sends back large results?](#426-what-is-the-impact-of-structured-clone-on-the-main-thread-when-a-worker-sends-back-large-results)
- [427: How do you handle a huge dataset that the UI needs to scroll through?](#427-how-do-you-handle-a-huge-dataset-that-the-ui-needs-to-scroll-through)
- [428: How do you combine IndexedDB and a worker for an offline-first app?](#428-how-do-you-combine-indexeddb-and-a-worker-for-an-offline-first-app)
- [429: What are the concerns with opening IndexedDB in several workers and tabs?](#429-what-are-the-concerns-with-opening-indexeddb-in-several-workers-and-tabs)
- [430: How do OPFS sync access handles handle multiple tabs?](#430-how-do-opfs-sync-access-handles-handle-multiple-tabs)
- [431: How would you design a real-time collaborative editor's client side with workers?](#431-how-would-you-design-a-real-time-collaborative-editors-client-side-with-workers)
- [432: What are the risks of running CRDT merging on the main thread?](#432-what-are-the-risks-of-running-crdt-merging-on-the-main-thread)
- [433: How do you share a worker between the main page and an iframe on the same origin?](#433-how-do-you-share-a-worker-between-the-main-page-and-an-iframe-on-the-same-origin)
- [434: What is the difference between window.postMessage and worker.postMessage?](#434-what-is-the-difference-between-windowpostmessage-and-workerpostmessage)
- [435: Why should you avoid "*" as targetOrigin in window.postMessage?](#435-why-should-you-avoid--as-targetorigin-in-windowpostmessage)
- [436: How do you handle backward compatibility for browsers without module workers?](#436-how-do-you-handle-backward-compatibility-for-browsers-without-module-workers)
- [437: How do you ship a library that uses workers?](#437-how-do-you-ship-a-library-that-uses-workers)
- [438: What problems appear when a worker URL is served from a CDN on another origin?](#438-what-problems-appear-when-a-worker-url-is-served-from-a-cdn-on-another-origin)
- [439: How does Node.js-style code like Buffer or process work in workers?](#439-how-does-nodejs-style-code-like-buffer-or-process-work-in-workers)
- [440: How would you run the same worker code in the browser and Node.js?](#440-how-would-you-run-the-same-worker-code-in-the-browser-and-nodejs)
- [441: How do workers behave in Deno and Bun compared to browsers?](#441-how-do-workers-behave-in-deno-and-bun-compared-to-browsers)
- [442: What is a common mistake with new URL and import.meta.url for workers?](#442-what-is-a-common-mistake-with-new-url-and-importmetaurl-for-workers)
- [443: How do you decide between a Web Worker and doing the work on the server?](#443-how-do-you-decide-between-a-web-worker-and-doing-the-work-on-the-server)
- [444: How would you explain a production bug where the app freezes only on some phones after adding a worker?](#444-how-would-you-explain-a-production-bug-where-the-app-freezes-only-on-some-phones-after-adding-a-worker)
- [445: How would you migrate an existing heavy main-thread function into a worker step by step?](#445-how-would-you-migrate-an-existing-heavy-main-thread-function-into-a-worker-step-by-step)
- [446: How do you keep a fallback path if workers fail?](#446-how-do-you-keep-a-fallback-path-if-workers-fail)
- [447: What questions would you ask before adding SharedArrayBuffer to a production app?](#447-what-questions-would-you-ask-before-adding-sharedarraybuffer-to-a-production-app)
- [448: What concurrency bugs would you look for in a code review of shared-memory code?](#448-what-concurrency-bugs-would-you-look-for-in-a-code-review-of-shared-memory-code)
- [449: What are the main browser concurrency tools, and when do you use each?](#449-what-are-the-main-browser-concurrency-tools-and-when-do-you-use-each)
- [450: If you had to summarize best practices for browser concurrency, what would they be?](#450-if-you-had-to-summarize-best-practices-for-browser-concurrency-what-would-they-be)

---

# Easy Questions (1-150)

## 1: Is JavaScript in the browser single-threaded?

Yes, your page's JavaScript runs on one thread, the main thread. Only one piece of your code runs at a time there, and it shares that thread with style calculation, layout, painting and input handling. The browser itself uses many threads (network, compositor, GPU, workers), but your page code only gets extra threads if you create workers.

## 2: What is the main thread?

The main thread is the thread where the browser runs your page's JavaScript, handles user input, calculates styles, does layout and paints. Because all of this happens on the same thread, a slow script blocks everything else. If a function runs for 500 ms, the page can't respond to clicks or update the screen for those 500 ms.

## 3: What is a Web Worker?

A Web Worker is a script that runs on a background thread, separate from the main thread. It has its own global scope, its own event loop and its own memory. The page and the worker talk by sending messages to each other. Workers let you run heavy work without freezing the UI.

```js
// main.js
const worker = new Worker("worker.js");
worker.postMessage(10);
worker.onmessage = (event) => console.log("Result:", event.data);

// worker.js
self.onmessage = (event) => {
  self.postMessage(event.data * 2);
};
```

## 4: Why would you use a Web Worker?

You use a worker to move CPU-heavy work off the main thread so the page stays responsive. Typical cases are parsing large JSON or CSV files, image processing, compression, encryption, search indexing and running WebAssembly code. The UI keeps handling clicks and animations while the worker does the slow part.

## 5: What is the difference between concurrency and parallelism?

Concurrency means several tasks make progress during the same period, but they may take turns on a single thread. Parallelism means tasks really run at the same moment on different CPU cores. Promises and async/await give you concurrency on the main thread. Workers give you real parallelism.

## 6: Does async/await make code run in parallel?

No. async/await only lets the main thread do other things while it waits for something like a network request or a timer. The JavaScript itself still runs on one thread. If you put a heavy loop inside an async function, it still blocks the main thread.

```js
async function slow() {
  // This still blocks the main thread for the whole loop
  let sum = 0;
  for (let i = 0; i < 1e9; i++) sum += i;
  return sum;
}
```

## 7: What are the main types of workers in the browser?

There are three main types:

- **Dedicated workers**: used by one page (the script that created them).
- **Shared workers**: can be used by several pages, tabs or iframes from the same origin.
- **Service workers**: act as a network proxy between the page and the network, used for caching, offline support and push notifications.

There are also worklets (audio, paint and others), which are lighter, special-purpose scripts.

## 8: What is a dedicated worker?

A dedicated worker is created with `new Worker(url)` and belongs to the script that created it. Only that page can talk to it. It is the most common kind of worker and the one people usually mean when they say "Web Worker". It stops when the page closes or when you call `terminate()`.

## 9: How do you create a Web Worker?

You call the `Worker` constructor with the URL of the worker script. The script must be on the same origin as the page (or be a blob URL created by the page).

```js
const worker = new Worker("/workers/math.js");
```

For a module worker, pass `{ type: "module" }`:

```js
const worker = new Worker(new URL("./math.js", import.meta.url), {
  type: "module",
});
```

## 10: How does the main thread send data to a worker?

It calls `worker.postMessage(data)`. The data is copied using the structured clone algorithm, so the worker gets its own copy, not a reference to the same object.

```js
worker.postMessage({ type: "sum", numbers: [1, 2, 3] });
```

## 11: How does a worker receive messages?

The worker listens for the `message` event on its global scope. You can use `self.onmessage` or `self.addEventListener("message", ...)`. The data is in `event.data`.

```js
self.addEventListener("message", (event) => {
  const { type, numbers } = event.data;
  if (type === "sum") {
    self.postMessage(numbers.reduce((a, b) => a + b, 0));
  }
});
```

## 12: How does a worker send a result back to the page?

Inside the worker you call `self.postMessage(data)` (or just `postMessage(data)`). On the page, you listen for the `message` event on the worker object.

```js
// worker.js
postMessage({ done: true, result: 42 });

// main.js
worker.addEventListener("message", (event) => {
  console.log(event.data.result);
});
```

## 13: What is self inside a worker?

`self` refers to the worker's global scope object. In a dedicated worker it is a `DedicatedWorkerGlobalScope`, in a shared worker it is a `SharedWorkerGlobalScope`, and in a service worker it is a `ServiceWorkerGlobalScope`. There is no `window` in a worker, so `self` (or `globalThis`) is what you use instead.

## 14: Can a Web Worker access the DOM?

No. Workers have no access to `document`, `window` or any DOM elements. The DOM is not thread-safe, so only the main thread can touch it. If a worker needs to change the page, it sends a message and the main thread does the DOM update.

## 15: What APIs are available inside a Web Worker?

Workers have many APIs, but no DOM. Some common ones:

- `fetch`, `WebSocket`, `EventSource`
- `setTimeout`, `setInterval`
- `IndexedDB`, Cache API
- `crypto` and `crypto.subtle`
- `TextEncoder`, `TextDecoder`, `URL`, `Blob`, `FileReader`
- `OffscreenCanvas`, `createImageBitmap`
- `importScripts` (classic workers) and `import` (module workers)
- `navigator` (a limited `WorkerNavigator`) and `location` (a `WorkerLocation`)

## 16: Can you use localStorage in a Web Worker?

No. `localStorage` and `sessionStorage` are not available in workers because they are synchronous and tied to the window. Use IndexedDB instead, which works in both the main thread and workers.

## 17: How do you stop a worker from the main thread?

Call `worker.terminate()`. The worker stops right away, without finishing its current task and without any cleanup event inside the worker.

```js
worker.terminate();
```

After that, sending more messages to the worker does nothing.

## 18: How does a worker stop itself?

The worker calls `self.close()`. It finishes the current task, drops any queued tasks and then shuts down. Use this when the worker knows it has nothing more to do.

```js
self.onmessage = (event) => {
  postMessage(doWork(event.data));
  self.close();
};
```

## 19: What is the difference between terminate() and close()?

`terminate()` is called from the page and kills the worker at once, even in the middle of a loop. `close()` is called from inside the worker and lets the current task finish before stopping. Neither one fires an event you can use for cleanup, so if you need cleanup, send a "shutdown" message first and let the worker clean up before calling `close()`.

## 20: What is the structured clone algorithm?

It is the algorithm browsers use to copy values between threads, for example in `postMessage`. It can copy most data: primitives, plain objects, arrays, `Date`, `RegExp`, `Map`, `Set`, `ArrayBuffer`, typed arrays, `Blob`, `File`, `ImageData` and more. It also handles circular references. It can't copy functions, DOM nodes or class instance prototypes.

## 21: What happens if you try to send a function with postMessage?

The call throws a `DataCloneError`, because functions can't be cloned. The same happens for DOM nodes and some other objects. If you need the worker to run some logic, put that logic in the worker script and send only the data plus a message type.

```js
try {
  worker.postMessage({ fn: () => 1 });
} catch (err) {
  console.log(err.name); // "DataCloneError"
}
```

## 22: Is the data passed to a worker shared or copied?

By default it is copied. Each side gets its own copy, so changing the object in the worker doesn't change it on the page. The two exceptions are transferable objects, which are moved instead of copied, and `SharedArrayBuffer`, whose memory is really shared between threads.

## 23: What are transferable objects?

Transferable objects can be moved from one thread to another instead of copied. After the move, the sender can no longer use the object. This is very fast for large data because no bytes are copied. Common transferables are `ArrayBuffer`, `MessagePort`, `ImageBitmap`, `OffscreenCanvas`, `ReadableStream`, `WritableStream` and `TransformStream`.

## 24: How do you transfer an ArrayBuffer to a worker?

Pass the buffer in the transfer list, the second argument of `postMessage`.

```js
const buffer = new ArrayBuffer(64 * 1024 * 1024); // 64 MB
worker.postMessage({ buffer }, [buffer]);
console.log(buffer.byteLength); // 0, it now belongs to the worker
```

You can also use the options form: `worker.postMessage(data, { transfer: [buffer] })`.

## 25: What does it mean that a buffer is detached?

After you transfer an `ArrayBuffer`, the original buffer on the sending side becomes detached. Its `byteLength` is 0 and any typed array view over it also has length 0. Trying to read or write it gives you nothing useful. The memory now belongs to the receiving thread.

## 26: What is a module worker?

A module worker is a worker created with `{ type: "module" }`. Its script is loaded as an ES module, so you can use `import` and `export`, top-level `await`, and strict mode is on by default. It's supported in all current major browsers and is the modern way to write workers.

```js
// main.js
const worker = new Worker(new URL("./worker.js", import.meta.url), {
  type: "module",
});

// worker.js
import { parseCsv } from "./csv.js";
self.onmessage = (e) => postMessage(parseCsv(e.data));
```

## 27: What is a classic worker?

A classic worker is the default kind, created without `type: "module"`. Its script runs as a normal script, not a module. It can't use `import` statements, and it loads other scripts with `importScripts()`. Classic workers still work everywhere, but for new code module workers are the better choice.

## 28: What does importScripts do?

`importScripts()` loads and runs one or more scripts inside a classic worker, synchronously and in order. All loaded scripts share the worker's global scope.

```js
// classic worker
importScripts("/libs/lodash.min.js", "/libs/helpers.js");
```

It doesn't work in module workers. There you use `import` instead.

## 29: Can you use import statements in a worker?

Yes, in a module worker. Create the worker with `{ type: "module" }` and you can use static `import` at the top of the file and dynamic `import()` anywhere. In a classic worker, static `import` is a syntax error, though dynamic `import()` may work depending on the browser.

## 30: How do you handle errors thrown inside a worker?

If the worker throws an uncaught error, an `error` event fires on the worker object in the page. The event has `message`, `filename` and `lineno`. Call `event.preventDefault()` to stop the error from also being logged as uncaught.

```js
worker.onerror = (event) => {
  console.error("Worker error:", event.message, event.filename, event.lineno);
  event.preventDefault();
};
```

## 31: What is the messageerror event?

`messageerror` fires when a message arrives but can't be deserialized. This is rare. For example, it can happen when a `SharedArrayBuffer` is sent to a context that isn't allowed to receive it. You can listen for it on the worker, on `self` in the worker, and on `MessagePort` and `BroadcastChannel` objects.

## 32: How do you report a handled error from a worker back to the page?

Catch the error in the worker and send it as a normal message. `Error` objects can be structured cloned, so you can send them directly, but sending a plain object with a message and a type is easier to work with.

```js
self.onmessage = (e) => {
  try {
    postMessage({ ok: true, result: heavyTask(e.data) });
  } catch (err) {
    postMessage({ ok: false, error: err.message });
  }
};
```

## 33: Does a worker share global variables with the page?

No. A worker has its own global scope and its own memory. A variable you set on `window` in the page doesn't exist in the worker, and a variable you set in the worker doesn't exist in the page. The only ways to share data are messages, `SharedArrayBuffer`, or storage like IndexedDB.

## 34: Can a worker make network requests?

Yes. Workers can use `fetch`, `XMLHttpRequest`, `WebSocket` and `EventSource`. Doing large downloads and parsing in a worker is a good pattern, since the main thread only gets the final, smaller result.

```js
self.onmessage = async (e) => {
  const res = await fetch(e.data.url);
  const data = await res.json();
  postMessage(data.items.length);
};
```

## 35: Can a worker use timers?

Yes, `setTimeout`, `setInterval`, `clearTimeout` and `clearInterval` all work in workers. A worker doesn't have `requestAnimationFrame` in every case, though. It's available in dedicated workers in current browsers, mainly for use with `OffscreenCanvas`.

## 36: Does a worker have its own event loop?

Yes. Each worker has its own event loop, task queue and microtask queue, separate from the main thread's. Promises, timers and message events inside the worker are handled by the worker's own loop. A long loop in a worker blocks only that worker, not the page.

## 37: What is navigator.hardwareConcurrency?

It returns the number of logical CPU cores the browser reports, for example 8. You can use it to decide how many workers to create for a pool. Some browsers cap or round this number for privacy, so treat it as a hint.

```js
const size = Math.max(1, (navigator.hardwareConcurrency || 4) - 1);
```

## 38: How many workers can you create?

There is no fixed number in the spec, but each worker is a real thread with its own memory and startup cost. Creating hundreds of workers wastes memory and doesn't make things faster, because you only have so many CPU cores. A common rule is to create about as many workers as `navigator.hardwareConcurrency` minus one, and reuse them.

## 39: Is creating a worker cheap?

Not really. Creating a worker means starting a new thread, a new JavaScript environment and loading and parsing its script. This can take tens of milliseconds and a few megabytes of memory. For small tasks the overhead is bigger than the gain, so create workers once and reuse them.

## 40: When should you not use a Web Worker?

Don't use a worker when the task is small and fast, when it mostly needs the DOM, or when copying the data to the worker costs more than doing the work on the main thread. Also, network waiting (fetch) doesn't block the main thread anyway, so moving a simple fetch to a worker gains little. Workers help most with long CPU work.

## 41: What is a long task?

A long task is any task on the main thread that runs for more than 50 ms. During a long task the browser can't respond to input or paint, so the page feels stuck. Long tasks are a main cause of bad Interaction to Next Paint (INP) scores. You fix them by splitting the work into smaller chunks or moving it to a worker.

## 42: How do you know if the main thread is blocked?

Open the Performance panel in Chrome DevTools and record. Long tasks show up as gray blocks with a red corner in the Main track. In code, you can watch for them with a `PerformanceObserver`:

```js
new PerformanceObserver((list) => {
  for (const entry of list.getEntries()) {
    console.log("Long task:", Math.round(entry.duration), "ms");
  }
}).observe({ type: "longtask", buffered: true });
```

## 43: Why does a heavy loop freeze the page?

Because the loop runs on the main thread and the browser can't interrupt it. The event loop only picks the next task (a click, a paint, a timer) after the current one finishes. Until the loop ends, no input is handled and nothing is redrawn.

## 44: What is the difference between a Web Worker and a service worker?

A Web Worker is a background thread for your own computation, created by a page and tied to it. A service worker sits between your site and the network. It intercepts requests, serves from cache, and handles push and background sync. It runs even when no page is open for short periods, and the browser starts and stops it when needed. You don't use a service worker for heavy computation.

## 45: What is a shared worker?

A shared worker is a worker that several browsing contexts from the same origin can connect to, such as two tabs or a page and an iframe. Each connection gets its own `MessagePort`. It stays alive as long as at least one page is connected.

```js
const shared = new SharedWorker("/shared.js");
shared.port.start();
shared.port.postMessage("hello");
shared.port.onmessage = (e) => console.log(e.data);
```

## 46: How does a shared worker receive connections?

A shared worker listens for the `connect` event. Each event gives a port for the new client. The worker keeps the ports to talk to each client.

```js
// shared.js
const ports = [];

self.onconnect = (event) => {
  const port = event.ports[0];
  ports.push(port);
  port.onmessage = (e) => {
    for (const p of ports) p.postMessage(e.data);
  };
};
```

## 47: What is a MessageChannel?

A `MessageChannel` creates a pair of connected ports, `port1` and `port2`. A message posted on one port arrives on the other. You can transfer one of the ports to a worker or iframe, so the two sides get a private communication line.

```js
const { port1, port2 } = new MessageChannel();
worker.postMessage({ port: port2 }, [port2]);
port1.onmessage = (e) => console.log("From worker:", e.data);
```

## 48: What is a MessagePort?

A `MessagePort` is one end of a `MessageChannel`. It has `postMessage()`, a `message` event, `start()` and `close()`. Ports are transferable, so you can pass them to workers, iframes or other windows. Shared workers also use ports to talk to each connected page.

## 49: What is BroadcastChannel?

`BroadcastChannel` lets any context on the same origin (tabs, iframes, workers) send messages to all others that joined the same channel name. You don't need to keep references to each tab.

```js
const channel = new BroadcastChannel("auth");
channel.postMessage({ type: "logout" });
channel.onmessage = (e) => {
  if (e.data.type === "logout") location.reload();
};
```

The sender doesn't receive its own message.

## 50: What is the difference between BroadcastChannel and postMessage on a worker?

`worker.postMessage` sends to one specific worker that you hold a reference to. `BroadcastChannel` sends to every listener on the same channel name in the same origin, and you don't need references to them. Use `postMessage` for one-to-one work requests and `BroadcastChannel` for one-to-many updates, such as syncing state across tabs.

## 51: Can a worker create another worker?

Yes. Dedicated workers can create their own workers, called nested workers or subworkers. All current major browsers support this (Safari added it in version 15.5). The child script URL is resolved relative to the parent worker's script.

```js
// inside worker.js
const child = new Worker(new URL("./child.js", import.meta.url), {
  type: "module",
});
```

## 52: What is a worker script's origin rule?

The worker script must come from the same origin as the page that creates it. You can't do `new Worker("https://other-site.com/worker.js")`. If you need code from a CDN, load it inside a same-origin worker with `importScripts()` or `import`, which can fetch cross-origin scripts if CORS allows it for modules.

## 53: How can you create a worker without a separate file?

You can put the code in a `Blob`, create a blob URL and pass that to `new Worker`.

```js
const code = `
  self.onmessage = (e) => postMessage(e.data * 2);
`;
const blob = new Blob([code], { type: "text/javascript" });
const url = URL.createObjectURL(blob);
const worker = new Worker(url);
```

Call `URL.revokeObjectURL(url)` once the worker has started, so the blob can be freed. Note that a strict Content Security Policy may block blob URLs for workers.

## 54: What is the worker-src CSP directive?

`worker-src` is a Content Security Policy directive that controls which URLs can be loaded as `Worker`, `SharedWorker` or `ServiceWorker` scripts. If it isn't set, browsers fall back to `child-src`, then `script-src`, then `default-src`.

```
Content-Security-Policy: worker-src 'self' blob:
```

## 55: Does a worker have access to window.location?

Not `window.location`, but it has `self.location`, which is a read-only `WorkerLocation`. It holds the URL of the worker script, not the page URL. You can read `href`, `origin`, `pathname` and so on, but you can't navigate with it.

## 56: What is navigator inside a worker?

Inside a worker, `navigator` is a `WorkerNavigator`. It has a smaller set of properties than the window's navigator, such as `userAgent`, `language`, `languages`, `onLine`, `hardwareConcurrency`, `storage`, `locks` and, in some browsers, `gpu`. It doesn't have things like `geolocation` or `clipboard`.

## 57: Can you use console.log in a worker?

Yes. `console.log` and other console methods work in workers. In Chrome DevTools, the messages appear in the Console with the worker's name next to them, and you can pick the worker context from the context dropdown at the top of the Console.

## 58: How do you debug a Web Worker in Chrome DevTools?

Open the Sources panel. Worker scripts appear in the left pane under their own thread, and the Threads section lists the main thread and each worker. You can set breakpoints in worker code and step through it like page code. You can also add a `debugger` statement in the worker script.

## 59: What is OffscreenCanvas?

`OffscreenCanvas` is a canvas that isn't attached to the DOM, so it can be used inside a worker. You can draw on it with 2D context, WebGL or WebGPU off the main thread. It's supported in all current major browsers.

```js
// inside a worker
const canvas = new OffscreenCanvas(256, 256);
const ctx = canvas.getContext("2d");
ctx.fillStyle = "tomato";
ctx.fillRect(0, 0, 256, 256);
const blob = await canvas.convertToBlob({ type: "image/png" });
```

## 60: How do you let a worker draw on a canvas that is on the page?

Call `transferControlToOffscreen()` on the `<canvas>` element and transfer the result to the worker. The worker then draws, and the result shows up in the page's canvas without the main thread doing anything.

```js
// main.js
const offscreen = document.querySelector("canvas").transferControlToOffscreen();
worker.postMessage({ canvas: offscreen }, [offscreen]);

// worker.js
self.onmessage = (e) => {
  const ctx = e.data.canvas.getContext("2d");
  ctx.fillRect(10, 10, 100, 100);
};
```

## 61: What is SharedArrayBuffer?

`SharedArrayBuffer` is like `ArrayBuffer`, but its memory can be shared between the main thread and workers. When you post it to a worker, both sides see the same bytes, so a change on one side is visible on the other. It needs the page to be cross-origin isolated to work.

```js
const sab = new SharedArrayBuffer(1024);
const view = new Int32Array(sab);
worker.postMessage(sab); // shared, not copied
```

## 62: What is the Atomics object?

`Atomics` is a built-in object with static methods for safe operations on shared memory, like `Atomics.add`, `Atomics.load`, `Atomics.store`, `Atomics.compareExchange`, `Atomics.wait` and `Atomics.notify`. Each operation finishes fully before another thread can see the value, so two threads updating the same counter don't lose updates.

```js
const counter = new Int32Array(new SharedArrayBuffer(4));
Atomics.add(counter, 0, 1);
console.log(Atomics.load(counter, 0)); // 1
```

## 63: What does cross-origin isolated mean?

A page is cross-origin isolated when it is served with two headers: `Cross-Origin-Opener-Policy: same-origin` and `Cross-Origin-Embedder-Policy: require-corp` (or `credentialless`). This puts the page in its own process and stops it from loading cross-origin resources that didn't opt in. Only then can the page use `SharedArrayBuffer` and some high-precision timers.

## 64: How do you check if a page is cross-origin isolated?

Read `self.crossOriginIsolated` (or `window.crossOriginIsolated`). It's `true` when the page has the right COOP and COEP headers.

```js
if (crossOriginIsolated) {
  const sab = new SharedArrayBuffer(1024);
} else {
  console.warn("SharedArrayBuffer is not available");
}
```

## 65: What is a race condition?

A race condition happens when two threads read and write the same data at the same time, and the result depends on which one runs first. In browsers, this can only happen with shared memory (`SharedArrayBuffer`). Normal message passing doesn't have this problem because each thread works on its own copy.

## 66: Why don't Web Workers usually have race conditions?

Because by default they don't share memory. Each worker has its own heap, and data moves between threads by copying or transferring. One thread never touches another thread's objects. Races only show up once you use `SharedArrayBuffer`, which is why it comes with the `Atomics` API.

## 67: What is the message passing model?

In message passing, threads don't share variables. Instead, they send each other messages with data. Web Workers follow this model: you call `postMessage` and the other side gets a `message` event. It's simpler and safer than shared memory because there are no locks and no data races.

## 68: What is the event loop?

The event loop is the mechanism that runs tasks one at a time on a thread. It takes a task from a queue (a click handler, a timer callback, a message), runs it to the end, runs all queued microtasks, and then, on the main thread, gives the browser a chance to render. Then it picks the next task. Every worker has its own event loop.

## 69: What is the difference between a task and a microtask?

A task (also called a macrotask) is a unit of work like a timer callback, an event handler or a `message` event. A microtask is a smaller job, like a promise callback or a `queueMicrotask` callback. After each task, the browser runs all microtasks before taking the next task or rendering. So a never-ending chain of microtasks can block the page just like a long loop.

## 70: Is a message event a task or a microtask?

A `message` event from `postMessage` is a task. It's queued on the receiving thread's event loop and runs after the current task and its microtasks are done. This is why `postMessage` is sometimes used as a way to schedule work after the current task.

## 71: What is requestAnimationFrame?

`requestAnimationFrame(callback)` asks the browser to call your function right before the next repaint, usually 60 times a second (or more on high-refresh screens). It's the right place for visual updates and animations. It pauses in background tabs to save battery.

```js
function tick(time) {
  box.style.transform = `translateX(${(time / 10) % 300}px)`;
  requestAnimationFrame(tick);
}
requestAnimationFrame(tick);
```

## 72: What is requestIdleCallback?

`requestIdleCallback(callback)` runs your function when the browser has free time at the end of a frame. The callback gets a deadline object with `timeRemaining()`, so you can do small chunks of low-priority work, like sending analytics. It's supported in Chrome, Edge and Firefox, but stable Safari still doesn't ship it, so check for it and fall back to `setTimeout`.

```js
requestIdleCallback((deadline) => {
  while (deadline.timeRemaining() > 0 && queue.length) {
    processItem(queue.shift());
  }
});
```

## 73: What is the Scheduler API?

The Prioritized Task Scheduling API adds a global `scheduler` object with `scheduler.postTask()` and `scheduler.yield()`. `postTask` lets you schedule a task with a priority (`user-blocking`, `user-visible` or `background`). `yield` lets a long function pause and let the browser handle input before it continues. It works in Chromium browsers and Firefox 142+, but not in Safari yet.

## 74: What does scheduler.yield do?

`scheduler.yield()` returns a promise that resolves in a new task, so awaiting it gives the browser a chance to handle input and render. The rest of your function continues soon after, ahead of other normal tasks. Use it inside long loops to keep the page responsive.

```js
async function processAll(items) {
  for (const item of items) {
    process(item);
    if (globalThis.scheduler?.yield) await scheduler.yield();
  }
}
```

## 75: What is yielding to the main thread?

Yielding means stopping your work for a moment so the browser can handle other tasks, like a click or a frame. You split a long job into small pieces and give control back between them. You can yield with `scheduler.yield()` or, as a fallback, with `await new Promise((r) => setTimeout(r, 0))`.

## 76: What is the difference between splitting work and moving it to a worker?

Splitting work keeps it on the main thread but in small chunks, so input can be handled in between. The total time is the same or a bit longer. Moving it to a worker runs it on another thread, so the main thread is free the whole time. Splitting is easier when the code needs the DOM. A worker is better for long CPU work that doesn't need the DOM.

## 77: What is a worklet?

A worklet is a small, lightweight script that runs inside a specific part of the browser's rendering or audio pipeline. Examples are `AudioWorklet`, `PaintWorklet` (CSS Paint API) and `AnimationWorklet`. Worklets have a very limited set of APIs and the browser controls when and where they run.

## 78: What is an AudioWorklet?

An `AudioWorklet` lets you write custom audio processing code that runs on the browser's audio rendering thread. You define an `AudioWorkletProcessor` with a `process()` method that handles 128-sample blocks. It replaced the old `ScriptProcessorNode`, which ran on the main thread and caused glitches.

```js
// main.js
const ctx = new AudioContext();
await ctx.audioWorklet.addModule("noise-processor.js");
const node = new AudioWorkletNode(ctx, "noise-processor");
node.connect(ctx.destination);
```

## 79: Can you use Web Workers with React?

Yes. You create the worker in a component or a custom hook, post messages to it and update state when results come back. Create it once (for example in `useEffect` or a module-level variable) and terminate it on unmount.

```js
function usePrimeWorker() {
  const [result, setResult] = useState(null);
  const workerRef = useRef(null);

  useEffect(() => {
    const worker = new Worker(new URL("./primes.js", import.meta.url), {
      type: "module",
    });
    worker.onmessage = (e) => setResult(e.data);
    workerRef.current = worker;
    return () => worker.terminate();
  }, []);

  return [result, (n) => workerRef.current.postMessage(n)];
}
```

## 80: How do you create a worker in a Vite project?

Use the `new Worker(new URL("./worker.js", import.meta.url), { type: "module" })` pattern. Vite detects it, bundles the worker file and its imports, and gives it the right URL in production. Vite also supports the `?worker` import suffix.

```js
import MyWorker from "./worker.js?worker";
const worker = new MyWorker();
```

## 81: How does webpack 5 handle workers?

webpack 5 has built-in worker support. It recognizes `new Worker(new URL("./worker.js", import.meta.url))` and creates a separate chunk for the worker. The old `worker-loader` package isn't needed anymore.

## 82: What is Comlink?

Comlink is a small library from Google Chrome Labs that hides `postMessage` behind a proxy. You expose an object in the worker and call its methods from the main thread as if they were local async functions. It handles message IDs and promises for you.

```js
// worker.js
import * as Comlink from "comlink";
Comlink.expose({ add: (a, b) => a + b });

// main.js
import * as Comlink from "comlink";
const api = Comlink.wrap(
  new Worker(new URL("./worker.js", import.meta.url), { type: "module" }),
);
console.log(await api.add(2, 3)); // 5
```

## 83: Do workers run in background tabs?

Yes, but browsers may slow them down. Timers in background pages get throttled, and some browsers also slow down timers in workers of hidden pages after a while. A worker running a long CPU loop keeps running, but don't count on precise timing when the tab is hidden.

## 84: What is a worker's name option?

You can pass a `name` when creating a worker: `new Worker(url, { name: "image-worker" })`. Inside the worker, `self.name` returns it. DevTools shows the name, which helps when you have several workers. For shared workers, the name is also part of how the browser decides whether to reuse an existing instance.

## 85: Can a worker read files the user picked?

Yes. You can send `File` or `Blob` objects from an `<input type="file">` to a worker with `postMessage`. Blobs are cloned cheaply because the browser just shares a handle to the data. The worker can then read them with `await file.text()`, `await file.arrayBuffer()`, `file.stream()` or `FileReaderSync`.

## 86: What is FileReaderSync?

`FileReaderSync` is a synchronous version of `FileReader` that only works in workers. Because workers don't block the UI, blocking reads are fine there. It has methods like `readAsText`, `readAsArrayBuffer` and `readAsDataURL`. In modern code, `await blob.text()` and `await blob.arrayBuffer()` usually do the same job.

```js
// inside a worker
const reader = new FileReaderSync();
const text = reader.readAsText(file);
```

## 87: Can a worker use IndexedDB?

Yes. IndexedDB is available in dedicated, shared and service workers. A worker can read and write the same databases as the page from the same origin. This is a good way to do heavy data imports in the background.

## 88: Can a worker use WebAssembly?

Yes. Workers can compile and run WebAssembly with `WebAssembly.instantiateStreaming` or `WebAssembly.instantiate`. Running heavy WASM code in a worker is common, since it keeps the main thread free. You can also send a compiled `WebAssembly.Module` to a worker with `postMessage`.

## 89: What does postMessage return?

It returns `undefined`. `postMessage` is fire-and-forget: it only queues the message. There is no built-in reply or promise. If you need a response, the other side must send a message back, and you match it to the request yourself, often with an ID.

## 90: Is postMessage synchronous or asynchronous?

The call itself is synchronous: the data is cloned right away, during the call. But delivery is asynchronous. The receiver gets a `message` event later, as a task in its own event loop. This is why changing an object right after posting it doesn't affect the copy the worker receives.

## 91: What is the difference between onmessage and addEventListener("message")?

Both listen for messages. `onmessage` is a single property, so assigning a new function replaces the old one. `addEventListener` lets you attach several listeners and remove them with `removeEventListener`. One detail: setting `port.onmessage` on a `MessagePort` starts the port automatically, while with `addEventListener` you must call `port.start()`.

## 92: Can you send multiple values in one postMessage?

Yes, wrap them in an object or array. `postMessage` takes one message value, but that value can be any cloneable structure.

```js
worker.postMessage({ type: "resize", width: 800, height: 600, quality: 0.9 });
```

## 93: What is a common message format for workers?

A common format is an object with a `type` field and a `payload`, plus an `id` when you need replies. The worker switches on `type` and replies with the same `id`.

```js
// main.js
worker.postMessage({ id: 1, type: "parse", payload: csvText });

// worker.js
self.onmessage = ({ data }) => {
  if (data.type === "parse") {
    postMessage({ id: data.id, result: parseCsv(data.payload) });
  }
};
```

## 94: Can a worker use Promises and async/await?

Yes. Workers support all of modern JavaScript, including promises, async/await, generators and top-level await in module workers. Async code inside a worker runs on the worker's event loop.

## 95: What happens to a worker when the page is closed?

A dedicated worker is stopped when its owner page is closed or navigates away. A shared worker keeps running until all connected pages are gone. A service worker isn't tied to a page at all and is started and stopped by the browser.

## 96: Can a worker show alerts or prompts?

No. `alert`, `confirm` and `prompt` belong to `window`, which doesn't exist in a worker. If you need to show something to the user, send a message to the page and let it show the dialog or UI.

## 97: Can a worker access cookies?

Not with `document.cookie`, since there is no document. But `fetch` requests from a worker still send cookies as usual, based on the `credentials` option. In browsers that support the Cookie Store API in workers, service workers can use `cookieStore` to read and change cookies.

## 98: Can a worker use the crypto API?

Yes. `crypto.getRandomValues()`, `crypto.randomUUID()` and `crypto.subtle` are available in workers. Running heavy hashing or encryption in a worker keeps the page responsive.

```js
// inside a worker
const data = new TextEncoder().encode("hello");
const hash = await crypto.subtle.digest("SHA-256", data);
```

## 99: What is a worker pool?

A worker pool is a fixed set of workers that you create once and reuse for many tasks. Tasks wait in a queue and each free worker takes the next one. This avoids the cost of starting a new worker for every task and limits how many threads run at once.

## 100: What are some real use cases for Web Workers?

Common uses include:

- Parsing big JSON, CSV or XML files
- Image filters, resizing and compression
- Syntax highlighting and code linting in online editors
- Full-text search over local data
- Running WebAssembly (games, video, PDF rendering)
- Encryption, hashing and compression
- Data processing for charts and spreadsheets
- Rendering with OffscreenCanvas

## 101: What is globalThis in a worker?

`globalThis` is the standard way to get the global object in any JavaScript environment. In a worker it points to the same object as `self`. Using `globalThis` is handy in code that must run in the page, in workers and in Node.js without changes.

## 102: How can code check if it is running inside a worker?

You can check for `WorkerGlobalScope`, which only exists in workers, or check that `document` is missing.

```js
const inWorker =
  typeof WorkerGlobalScope !== "undefined" && self instanceof WorkerGlobalScope;
```

To check for a specific kind, use `DedicatedWorkerGlobalScope`, `SharedWorkerGlobalScope` or `ServiceWorkerGlobalScope`.

## 103: What is the Worker constructor's options object?

The second argument of `new Worker(url, options)` accepts:

- `type`: `"classic"` (default) or `"module"`
- `name`: a label, available as `self.name` inside the worker
- `credentials`: `"omit"`, `"same-origin"` (default) or `"include"`, used for module worker script requests

```js
new Worker(url, { type: "module", name: "parser", credentials: "same-origin" });
```

## 104: Can you pass arguments to a worker when you create it?

Not directly, apart from the `name` option. The usual way is to send an "init" message right after creating the worker. You can also put simple values in the script URL as query parameters and read them from `self.location.search`.

```js
const worker = new Worker("/worker.js?mode=fast");
// inside worker.js
const mode = new URL(self.location.href).searchParams.get("mode");
```

## 105: Can you send a Map or Set to a worker?

Yes. `Map` and `Set` are supported by the structured clone algorithm. The worker gets a new `Map` or `Set` with copies of the keys and values.

```js
worker.postMessage(
  new Map([
    ["a", 1],
    ["b", 2],
  ]),
);
```

## 106: Can you send a Date to a worker?

Yes. `Date` objects are cloned as real `Date` objects, so the worker can call `getTime()` and other methods on them.

## 107: Can you send a class instance to a worker?

You can send it, but only its own data properties are copied. The prototype is lost, so on the other side it's a plain object without the class's methods. If you need the class, recreate it in the worker from the plain data.

```js
class Point {
  constructor(x, y) {
    this.x = x;
    this.y = y;
  }
  length() {
    return Math.hypot(this.x, this.y);
  }
}
worker.postMessage(new Point(3, 4));
// worker gets { x: 3, y: 4 } without the length method
```

## 108: Is JSON.stringify needed before postMessage?

No. `postMessage` already handles objects through structured clone, which supports more types than JSON (Map, Set, Date, typed arrays, Blob and circular references). Stringifying first adds extra work and loses those types. In rare cases with very simple data, strings can be slightly faster to send, but measure before doing it.

## 109: What is structuredClone?

`structuredClone(value)` is a global function that makes a deep copy of a value using the same algorithm as `postMessage`. It's available in pages, workers and Node.js. It's a good way to deep copy objects without JSON tricks.

```js
const original = { date: new Date(), tags: new Set(["a"]) };
const copy = structuredClone(original);
```

## 110: What is a blob URL?

A blob URL looks like `blob:https://example.com/uuid` and points to a `Blob` in memory. You create one with `URL.createObjectURL(blob)` and release it with `URL.revokeObjectURL(url)`. Blob URLs are often used to create workers from code strings or to download generated files.

## 111: Can a data URL be used for a worker?

Yes, but a worker created from a `data:` URL gets an opaque origin. That means it can't use same-origin features like IndexedDB or same-origin fetch with cookies. Blob URLs don't have this problem because they keep the page's origin, so they are usually a better choice.

## 112: What is the difference between a thread and a process?

A process has its own memory space. Threads live inside a process and can share memory. Browsers like Chrome use many processes (a browser process, renderer processes per site, a GPU process) for security and stability. Inside a renderer process, there are many threads: the main thread, the compositor thread, worker threads and others.

## 113: Do Web Workers run in a separate process?

Dedicated workers usually run as threads inside the same renderer process as the page. They get their own JavaScript heap and event loop, but not their own process. Shared workers and service workers may run in a different process, depending on the browser.

## 114: What is the compositor thread?

The compositor thread is a browser thread that takes painted layers and combines them into the final frame. It can handle scrolling and some animations (like `transform` and `opacity`) without the main thread. That's why CSS transform animations stay smooth even when the main thread is busy.

## 115: Why are CSS transform animations smoother than JS animations?

Animations of `transform` and `opacity` can run on the compositor thread. They don't need the main thread to run JavaScript or do layout on every frame. JavaScript animations that change `left` or `width` need the main thread for every frame, so they stutter when it's busy.

## 116: What is INP and how does it relate to the main thread?

Interaction to Next Paint (INP) is a Core Web Vital that measures how long it takes from a user's click, tap or key press until the next frame is painted. If the main thread is busy with long tasks, the browser can't respond quickly and INP gets worse. Moving work to workers and yielding often both help INP.

## 117: What does it mean for an API to be thread-safe?

A thread-safe API can be used by several threads at the same time without breaking its data. The DOM is not thread-safe, which is why only the main thread can access it. Web Workers avoid most thread-safety issues by not sharing memory with the page.

## 118: Can multiple workers run at the same time?

Yes. Each worker is its own thread, and the operating system can run them on different CPU cores at the same time. On a machine with 8 cores, you can have several workers really doing work in parallel.

## 119: Does a worker make code run faster?

Not by itself. The same code runs at about the same speed in a worker. The gain is that the main thread stays free, so the page feels faster. Real speedups come only when you split work across several workers on different cores. Also, copying data to and from the worker adds some time.

## 120: What happens if a worker script fails to load?

If the URL returns a 404, a network error or the wrong MIME type, an `error` event fires on the `Worker` object. The worker never starts. Listen for `error` on the worker to catch this.

```js
const worker = new Worker("/missing.js");
worker.onerror = () => console.error("Worker failed to start");
```

## 121: What MIME type must a worker script have?

The server should send worker scripts with a JavaScript MIME type, such as `text/javascript`. Module workers are strict about this and fail to load if the MIME type is wrong. Classic workers are more forgiving in some browsers, but serving the right type is always the safe choice.

## 122: Can a worker read the page's URL?

Not directly. `self.location` gives the worker script's URL, not the page URL. If the worker needs the page URL, the page has to send it in a message.

## 123: Can workers use fetch with relative URLs?

Yes, but relative URLs are resolved against the worker script's URL, not the page's URL. If the worker lives at `/workers/w.js`, then `fetch("data.json")` requests `/workers/data.json`. Use absolute paths or full URLs to avoid confusion.

## 124: What is a ReadableStream and can it be sent to a worker?

A `ReadableStream` is a stream of data chunks you can read over time, like a large file or a fetch response body. Streams are transferable in current browsers, so you can pass one to a worker in the transfer list and the worker reads it chunk by chunk.

```js
const res = await fetch("/big.csv");
worker.postMessage({ stream: res.body }, [res.body]);
```

## 125: What is the CSS Paint API?

The CSS Paint API (part of CSS Houdini) lets you write a paint worklet that draws an image for CSS properties like `background-image`. You register a class with a `paint()` method and use it in CSS with `paint(name)`. It's supported in Chromium browsers, but not in Firefox or Safari.

```js
CSS.paintWorklet.addModule("checker.js");
```

```css
.box {
  background-image: paint(checker);
}
```

## 126: What is the difference between a worklet and a worker?

A worker is a general-purpose background thread that you control and talk to with messages. A worklet is a small script that plugs into a specific browser pipeline, like audio or painting. The browser decides when to run worklet code, it may create several instances, and worklets have a very limited set of APIs.

## 127: Can a worker use requestAnimationFrame?

Yes, dedicated workers have `requestAnimationFrame` and `cancelAnimationFrame` in current browsers. It's mainly useful when the worker draws to an `OffscreenCanvas` that was transferred from a page canvas, so the drawing lines up with the display's frames.

## 128: What does it mean that a worker is idle?

A worker is idle when its event loop has no tasks to run. It still exists and holds its memory, but it uses no CPU. An idle worker wakes up when a new message or timer arrives. Idle workers still cost memory, so terminate them when you no longer need them.

## 129: How do you send a large typed array to a worker quickly?

Transfer its underlying buffer instead of copying it.

```js
const pixels = new Uint8ClampedArray(4 * 1920 * 1080);
worker.postMessage({ pixels }, [pixels.buffer]);
```

The worker gets the same memory without a copy. The page's `pixels` becomes empty.

## 130: How can the worker send the data back without copying?

The worker transfers the buffer back in its own `postMessage`. This "ping-pong" pattern lets one buffer move between threads with no copies.

```js
// worker.js
self.onmessage = ({ data }) => {
  invert(data.pixels);
  postMessage({ pixels: data.pixels }, [data.pixels.buffer]);
};
```

## 131: What is the Web Locks API?

The Web Locks API (`navigator.locks`) lets code in tabs and workers of the same origin take a named lock, so only one of them runs a piece of code at a time. It's useful when several tabs must not do the same job at once, like refreshing a token.

```js
await navigator.locks.request("refresh-token", async () => {
  await refreshToken();
});
```

## 132: Is Web Locks available in workers?

Yes. `navigator.locks` is available in pages, dedicated workers, shared workers and service workers. A lock taken in a worker blocks the same lock name in a page, as long as they are on the same origin.

## 133: What is the difference between a SharedArrayBuffer and an ArrayBuffer?

An `ArrayBuffer` belongs to one thread. When posted, it is copied or transferred. A `SharedArrayBuffer` is shared: when posted, both threads point to the same memory. Changes from one thread are visible to the other. Because of this, `SharedArrayBuffer` needs `Atomics` for safe updates and requires cross-origin isolation.

## 134: Why was SharedArrayBuffer disabled for a while?

In January 2018, browsers turned off `SharedArrayBuffer` after the Spectre attacks were found. Shared memory can be used to build a very precise timer, which helps read memory that a page shouldn't see. It came back later, but only on cross-origin isolated pages (COOP and COEP headers), where the risk is much lower.

## 135: What headers are needed to enable SharedArrayBuffer?

The page must be served with:

```
Cross-Origin-Opener-Policy: same-origin
Cross-Origin-Embedder-Policy: require-corp
```

Instead of `require-corp`, you can use `credentialless`, which lets the page load cross-origin resources without cookies. Worker scripts also need the COEP header.

## 136: What is Cross-Origin-Opener-Policy?

COOP is a header that controls whether your page shares a browsing context group with pages it opens or that open it. With `same-origin`, cross-origin popups and openers get separated from your page, so they can't keep a reference to your `window`. It's one of the two headers needed for cross-origin isolation.

## 137: What is Cross-Origin-Embedder-Policy?

COEP is a header that controls which cross-origin resources the page can load. With `require-corp`, every cross-origin resource must opt in with CORS or a `Cross-Origin-Resource-Policy` header. With `credentialless`, cross-origin requests are sent without cookies so they don't need to opt in. It's the second header needed for cross-origin isolation.

## 138: What is Atomics.wait?

`Atomics.wait(typedArray, index, value, timeout)` blocks the current thread while the value at that index still equals `value`, until another thread calls `Atomics.notify` or the timeout ends. It returns `"ok"`, `"not-equal"` or `"timed-out"`. It only works on an `Int32Array` or `BigInt64Array` over a `SharedArrayBuffer`.

## 139: Can you call Atomics.wait on the main thread?

No. Browsers don't allow blocking the main thread, so `Atomics.wait` throws a `TypeError` there. Use it only in workers. On the main thread, use `Atomics.waitAsync`, which returns a promise instead of blocking.

## 140: What is Atomics.notify?

`Atomics.notify(typedArray, index, count)` wakes up threads that are waiting with `Atomics.wait` (or `waitAsync`) on that index. `count` is how many waiters to wake; leave it out to wake all of them. It returns the number of threads that were woken.

```js
Atomics.store(flags, 0, 1);
Atomics.notify(flags, 0);
```

## 141: What is the difference between a worker and a child process in Node.js?

This question comes up because both are about concurrency. In Node.js, `worker_threads` are threads in the same process, similar to browser workers. `child_process` starts a whole new OS process. Browser Web Workers are threads, like Node's worker threads, and their APIs look similar (`postMessage`, `MessageChannel`, transferables, `SharedArrayBuffer`).

## 142: What is the main difference between browser Web Workers and Node.js worker_threads?

They share many ideas: `postMessage`, structured clone, transferables, `MessageChannel` and `SharedArrayBuffer`. The differences are in the API details. Node's `Worker` uses `parentPort` and `workerData`, emits events with `.on("message")`, and its messages arrive as the value itself rather than as an event object. In Node, `SharedArrayBuffer` doesn't need special headers.

## 143: What is a service worker used for?

A service worker is used for network-related features: caching assets for offline use, custom responses to requests, push notifications and background sync. It runs separately from pages, has no DOM, and the browser can stop it when idle. It's the base of Progressive Web Apps.

## 144: Should you run heavy computation in a service worker?

No. Service workers are meant to handle network events quickly and can be stopped by the browser when idle. Long computations there slow down every request the service worker handles. Use a dedicated worker for heavy CPU work.

## 145: Can a worker be used by an iframe?

An iframe can create its own workers, just like a page. It can also connect to a shared worker if it's on the same origin as the worker script. Note that storage partitioning means an iframe embedded in a different top-level site may get a separate shared worker instance.

## 146: What is a race between two postMessage calls?

Messages sent from one side to the same target arrive in the order they were sent. But messages from different senders (for example, two workers sending to the page) can arrive in any order. If order matters across senders, include a sequence number or timestamp in the message.

## 147: Are messages from a worker delivered in order?

Yes. Messages from one sender to one receiver over the same channel are delivered in the order they were posted. So if a worker posts A then B, the page gets A before B.

## 148: How do you clean up event listeners on a worker?

Use `removeEventListener` with the same function you added, or set `onmessage = null`. If you're done with the worker, calling `terminate()` frees everything at once. Leaving old listeners can keep closures and data in memory.

## 149: What is the TypeScript setup for writing a worker?

Add `"WebWorker"` to the `lib` array in a separate `tsconfig.json` for worker files, so TypeScript knows about `self`, `postMessage` and other worker types. Some teams put a reference at the top of the worker file instead.

```ts
/// <reference lib="webworker" />
declare const self: DedicatedWorkerGlobalScope;

self.onmessage = (e: MessageEvent<number>) => {
  self.postMessage(e.data * 2);
};
```

## 150: What is the simplest way to explain Web Workers to a beginner?

The browser page is like a shop with one cashier. If the cashier stops to do a long calculation, the whole line waits. A Web Worker is like a helper in the back room: the cashier gives the helper a note with the task, keeps serving customers, and later gets a note back with the answer. The helper can't talk to customers (no DOM), only to the cashier.

# Moderate Questions (151-300)

## 151: How do you wrap a worker call in a Promise?

Give each request an ID, store its `resolve` and `reject`, and settle the right promise when a reply with that ID comes back.

```js
const worker = new Worker(new URL("./worker.js", import.meta.url), {
  type: "module",
});
const pending = new Map();
let nextId = 0;

worker.onmessage = ({ data }) => {
  const entry = pending.get(data.id);
  if (!entry) return;
  pending.delete(data.id);
  data.error ? entry.reject(new Error(data.error)) : entry.resolve(data.result);
};

export function call(type, payload, transfer = []) {
  const id = nextId++;
  return new Promise((resolve, reject) => {
    pending.set(id, { resolve, reject });
    worker.postMessage({ id, type, payload }, transfer);
  });
}
```

## 152: Why do you need request IDs when talking to a worker?

Because `postMessage` has no built-in reply. If you send several requests and the worker answers them in a different order (for example, because some are async), you need a way to match each answer to its request. An ID in both the request and the reply solves that.

## 153: How do you handle a worker crash in a promise wrapper?

Listen for the worker's `error` event and reject all pending promises, since none of them will get a reply. Then decide whether to create a new worker.

```js
worker.onerror = (event) => {
  for (const { reject } of pending.values()) {
    reject(new Error(event.message || "Worker crashed"));
  }
  pending.clear();
};
```

## 154: How do you add a timeout to a worker request?

Start a timer when you send the request. If no reply arrives in time, reject the promise and remove it from the pending map. If the worker might be stuck in a loop, terminate it and start a new one.

```js
function callWithTimeout(type, payload, ms = 5000) {
  return Promise.race([
    call(type, payload),
    new Promise((_, reject) =>
      setTimeout(() => reject(new Error("Worker timeout")), ms),
    ),
  ]);
}
```

## 155: How do you cancel a task running in a worker?

There's no built-in cancel. You have three options:

- Send a "cancel" message with the task ID. This only works if the worker's task is async or yields so the message gets handled.
- Use a shared flag in a `SharedArrayBuffer` that the worker checks inside its loop.
- Call `terminate()` and create a new worker. This always works but loses the worker's state.

## 156: How do you use AbortController with a worker call?

`AbortSignal` can't be sent to a worker, but you can listen to it on the main thread and send a cancel message, or reject the promise right away.

```js
function run(payload, { signal } = {}) {
  const id = nextId++;
  return new Promise((resolve, reject) => {
    pending.set(id, { resolve, reject });
    signal?.addEventListener(
      "abort",
      () => {
        pending.delete(id);
        worker.postMessage({ id, type: "cancel" });
        reject(signal.reason);
      },
      { once: true },
    );
    worker.postMessage({ id, type: "run", payload });
  });
}
```

## 157: How does a worker check for a cancel message during a long loop?

A cancel message can only be handled between tasks. A long sync loop blocks the worker's event loop, so the message waits. To let it in, break the loop into chunks and give the event loop a turn between them, for example with `await new Promise((r) => setTimeout(r, 0))`, then check a cancelled set.

```js
const cancelled = new Set();

self.onmessage = async ({ data }) => {
  if (data.type === "cancel") return cancelled.add(data.id);
  for (let i = 0; i < data.payload.length; i++) {
    if (i % 10000 === 0) {
      await new Promise((r) => setTimeout(r, 0));
      if (cancelled.has(data.id)) return;
    }
    work(data.payload[i]);
  }
  postMessage({ id: data.id, result: "done" });
};
```

## 158: How do you report progress from a worker?

Send progress messages from time to time while the task runs, then a final result message. Don't send one message per item, since each message has overhead. Send one every N items or every few hundred milliseconds.

```js
for (let i = 0; i < rows.length; i++) {
  processRow(rows[i]);
  if (i % 5000 === 0)
    postMessage({ type: "progress", done: i, total: rows.length });
}
postMessage({ type: "done" });
```

## 159: How do you build a simple worker pool?

Create N workers, keep a queue of tasks, and give a task to each free worker. When a worker finishes, give it the next task.

```js
export class WorkerPool {
  constructor(url, size = navigator.hardwareConcurrency || 4) {
    this.queue = [];
    this.idle = [];
    for (let i = 0; i < size; i++) {
      this.idle.push(new Worker(url, { type: "module" }));
    }
  }

  run(data) {
    return new Promise((resolve, reject) => {
      this.queue.push({ data, resolve, reject });
      this.#next();
    });
  }

  #next() {
    if (!this.queue.length || !this.idle.length) return;
    const worker = this.idle.pop();
    const { data, resolve, reject } = this.queue.shift();
    worker.onmessage = (e) => {
      resolve(e.data);
      this.idle.push(worker);
      this.#next();
    };
    worker.onerror = (e) => {
      reject(e);
      this.idle.push(worker);
      this.#next();
    };
    worker.postMessage(data);
  }
}
```

## 160: How do you choose the size of a worker pool?

Start with `navigator.hardwareConcurrency - 1` so one core stays for the main thread. For CPU-bound work, more workers than cores don't help and add memory and switching costs. On low-end phones, use fewer (2 to 4). Measure on real devices, because the browser and other apps also use the cores.

## 161: How do you split a large array across multiple workers?

Divide the array into chunks, send one chunk to each worker, wait for all results with `Promise.all`, and combine them.

```js
async function parallelSum(numbers, pool, parts = 4) {
  const size = Math.ceil(numbers.length / parts);
  const jobs = [];
  for (let i = 0; i < parts; i++) {
    jobs.push(pool.run(numbers.slice(i * size, (i + 1) * size)));
  }
  const partials = await Promise.all(jobs);
  return partials.reduce((a, b) => a + b, 0);
}
```

## 162: When is copying data to a worker slower than doing the work on the main thread?

When the data is large and the work per item is small. For example, summing a 100 MB array is fast, but cloning 100 MB to a worker can take longer than the sum itself. In that case, transfer the buffer instead of copying, use a `SharedArrayBuffer`, or keep the data in the worker from the start (load it there directly).

## 163: How do you measure the cost of postMessage?

Time the round trip with `performance.now()`. Send the data, have the worker echo it back right away, and measure. Compare with the time to do the actual work on the main thread.

```js
const start = performance.now();
worker.onmessage = () => {
  console.log("Round trip:", performance.now() - start, "ms");
};
worker.postMessage(bigObject);
```

Also look at the Performance panel, which shows serialization time on both threads.

## 164: What kinds of objects are slow to clone?

Large, deeply nested objects with many small properties are the slowest, because structured clone visits each value. Big arrays of objects (like 100,000 rows of `{ id, name, ... }`) are a common problem. Typed arrays and `ArrayBuffer`s are much faster to clone because they are one block of bytes, and transferring them is almost free.

## 165: How can you make large data cheaper to send to a worker?

Some options:

- Transfer `ArrayBuffer`s instead of copying them.
- Store data in typed arrays (columnar format) instead of arrays of objects.
- Send only what the worker needs, not whole objects.
- Load the data inside the worker with `fetch` instead of passing it through the page.
- Use `SharedArrayBuffer` for data both sides read often.

## 166: What is a columnar data layout and why does it help with workers?

Instead of an array of objects like `[{ x, y }, { x, y }]`, you keep one typed array per field: `xs: Float64Array`, `ys: Float64Array`. Typed arrays are compact, fast to loop over and can be transferred or shared with no copy. This is how many charting and data apps send big datasets to workers.

## 167: What does the transfer option in structuredClone do?

`structuredClone(value, { transfer: [buffer] })` copies the value but moves the listed buffers instead of copying them. The originals become detached. It's useful when you want to give away ownership of a buffer inside the same thread.

```js
const buffer = new ArrayBuffer(1024);
const moved = structuredClone(buffer, { transfer: [buffer] });
console.log(buffer.byteLength, moved.byteLength); // 0 1024
```

## 168: What is ArrayBuffer.prototype.transfer?

`buffer.transfer(newLength)` creates a new `ArrayBuffer` with the same contents and detaches the old one. It's part of ES2024 and supported in current browsers. It's a short way to take ownership of a buffer or resize it while moving it.

```js
const a = new ArrayBuffer(8);
const b = a.transfer();
console.log(a.detached, b.byteLength); // true 8
```

## 169: What happens if you list the same buffer twice in a transfer list?

`postMessage` throws a `DataCloneError`. Each transferable may appear only once. It also throws if the buffer is already detached, for example if you try to transfer it a second time after the first transfer.

## 170: Can you transfer a typed array directly?

No, you transfer its `buffer`. The typed array itself goes in the message, and its `.buffer` goes in the transfer list. If several typed arrays share one buffer, transfer the buffer once and all views move together.

```js
const a = new Float32Array(1000);
worker.postMessage({ a }, [a.buffer]);
```

## 171: How do you transfer a MessagePort to a worker?

Put the port in the message and in the transfer list. Ports must be transferred, not cloned.

```js
const { port1, port2 } = new MessageChannel();
workerA.postMessage({ port: port1 }, [port1]);
workerB.postMessage({ port: port2 }, [port2]);
// now workerA and workerB can talk directly
```

## 172: How do two workers talk to each other directly?

Create a `MessageChannel` on the main thread and transfer one port to each worker. After that, the workers send messages through their ports without going through the main thread. This is useful for pipelines where one worker's output goes to another.

## 173: Why do you need to call port.start()?

When you listen to a `MessagePort` with `addEventListener("message")`, messages are queued until you call `port.start()`. Setting `port.onmessage` calls `start()` for you. If messages "never arrive" on a port, a missing `start()` is a common cause.

## 174: How do you close a MessagePort?

Call `port.close()`. After that, no more messages are sent or received on that port. Chromium browsers also fire a `close` event on the other port when one end closes, which helps detect that a peer is gone, but don't rely on it everywhere yet.

## 175: How do you sync state across tabs with BroadcastChannel?

Each tab opens a channel with the same name and posts updates when its state changes. Other tabs listen and apply the update. Since the sender doesn't receive its own message, there are no loops.

```js
const channel = new BroadcastChannel("cart");

function addToCart(item) {
  cart.push(item);
  render();
  channel.postMessage({ type: "add", item });
}

channel.onmessage = ({ data }) => {
  if (data.type === "add") {
    cart.push(data.item);
    render();
  }
};
```

## 176: What is the difference between BroadcastChannel and the storage event?

The `storage` event fires in other tabs when `localStorage` changes, but you can only send strings and it requires writing to storage. `BroadcastChannel` sends any cloneable value, doesn't touch storage and works in workers. For new code, `BroadcastChannel` is the cleaner choice.

## 177: When would you use a SharedWorker instead of BroadcastChannel?

Use a `SharedWorker` when you need one shared instance that holds state or a resource for all tabs, like a single WebSocket connection or an in-memory cache. `BroadcastChannel` only passes messages, it has no central place to keep state. A shared worker lets several tabs share one connection instead of each tab opening its own.

## 178: How do you share one WebSocket connection across tabs?

Open the WebSocket inside a `SharedWorker`. Each tab connects to the shared worker, sends outgoing messages through its port, and the worker forwards incoming socket messages to all connected ports.

```js
// shared-socket.js
const ports = new Set();
const socket = new WebSocket("wss://example.com/live");

socket.onmessage = (e) => {
  for (const port of ports) port.postMessage(e.data);
};

self.onconnect = (e) => {
  const port = e.ports[0];
  ports.add(port);
  port.onmessage = (msg) => socket.send(msg.data);
};
```

## 179: How does a shared worker know a tab has closed?

It doesn't get a reliable event when a tab disappears. Common solutions are: the tab sends a "bye" message on `pagehide`, or the worker pings each port and drops ports that don't answer. In Chromium, the port's `close` event can also help. Without this, the worker keeps dead ports and leaks memory.

## 180: What are the limits of SharedWorker support?

Shared workers work in desktop Chrome, Edge, Firefox and Safari (Safari brought them back in version 16). Support on mobile has been weaker: for a long time Chrome for Android didn't support them. Always check for `typeof SharedWorker !== "undefined"` and have a fallback, such as a dedicated worker per tab plus `BroadcastChannel`.

## 181: How do you debug a SharedWorker?

In Chrome, open `chrome://inspect/#workers`, find your shared worker and click "inspect". This opens a separate DevTools window for it. `console.log` from a shared worker doesn't show in the page's console, which surprises many people. In Firefox, use `about:debugging#workers`.

## 182: What is the name option for a SharedWorker?

`new SharedWorker(url, { name: "chat" })` gives the shared worker a name. Pages that use the same URL and the same name connect to the same instance. Different names create different instances from the same script. This lets you have separate shared workers for separate purposes.

## 183: How do you handle errors in a SharedWorker?

Uncaught errors inside a shared worker don't fire `error` on the page's `SharedWorker` object in the same way as with dedicated workers. Catch errors inside the worker and send them to the ports as messages. The page's `SharedWorker` object does get an `error` event if the script fails to load.

## 184: What is the difference between a dedicated worker and a SharedWorker in how you send messages?

With a dedicated worker you call `worker.postMessage()` and listen with `worker.onmessage`. With a shared worker you go through its port: `sharedWorker.port.postMessage()` and `sharedWorker.port.onmessage`. Inside, a dedicated worker uses `self.postMessage`, while a shared worker uses each client's port from the `connect` event.

## 185: How do you use OffscreenCanvas for chart rendering in a worker?

Transfer the canvas control to a worker, send data updates as messages, and let the worker draw. The main thread only handles input and sends data, so heavy redraws don't slow down the UI.

```js
// main.js
const canvas = document.getElementById("chart");
const offscreen = canvas.transferControlToOffscreen();
chartWorker.postMessage({ type: "init", canvas: offscreen }, [offscreen]);
chartWorker.postMessage({ type: "data", points: new Float32Array(points) });

// chart-worker.js
let ctx;
self.onmessage = ({ data }) => {
  if (data.type === "init") ctx = data.canvas.getContext("2d");
  if (data.type === "data") draw(ctx, data.points);
};
```

## 186: How do you handle canvas resizing with OffscreenCanvas?

After `transferControlToOffscreen()`, you can't change the canvas `width` and `height` from the main thread. Watch the element's size with `ResizeObserver` on the main thread, send the new size to the worker, and let the worker set `canvas.width` and `canvas.height` and redraw.

```js
new ResizeObserver(([entry]) => {
  const { width, height } = entry.contentRect;
  worker.postMessage({
    type: "resize",
    width: width * devicePixelRatio,
    height: height * devicePixelRatio,
  });
}).observe(canvasEl);
```

## 187: How do you handle mouse events with an OffscreenCanvas in a worker?

The worker can't receive DOM events. Listen for pointer events on the canvas element in the main thread, pick the fields you need (like `offsetX`, `offsetY`, `buttons`), and send them to the worker. You can't send the event object itself because it isn't cloneable.

```js
canvasEl.addEventListener("pointermove", (e) => {
  worker.postMessage({ type: "pointer", x: e.offsetX, y: e.offsetY });
});
```

## 188: What is createImageBitmap and why is it useful in workers?

`createImageBitmap(source)` decodes an image (from a `Blob`, `ImageData`, canvas and others) into an `ImageBitmap` that is ready to draw. It's async and available in workers, so you can decode big images off the main thread. `ImageBitmap` is also transferable.

```js
// inside a worker
const res = await fetch(url);
const bitmap = await createImageBitmap(await res.blob());
postMessage({ bitmap }, [bitmap]);
```

## 189: How do you resize an image in a worker?

Decode it with `createImageBitmap`, draw it on a smaller `OffscreenCanvas`, and export with `convertToBlob`.

```js
self.onmessage = async ({ data: file }) => {
  const bitmap = await createImageBitmap(file);
  const scale = 800 / bitmap.width;
  const canvas = new OffscreenCanvas(800, Math.round(bitmap.height * scale));
  canvas.getContext("2d").drawImage(bitmap, 0, 0, canvas.width, canvas.height);
  bitmap.close();
  postMessage(
    await canvas.convertToBlob({ type: "image/jpeg", quality: 0.85 }),
  );
};
```

## 190: What does ImageBitmap.close do?

`bitmap.close()` frees the memory used by the bitmap right away, instead of waiting for garbage collection. Bitmaps can be large (width x height x 4 bytes), so closing them when you're done helps avoid memory spikes when processing many images.

## 191: How do you apply a pixel filter in a worker?

Get the pixel data as `ImageData`, transfer its buffer to the worker, change the bytes, and transfer it back.

```js
// worker.js
self.onmessage = ({ data }) => {
  const { pixels } = data; // Uint8ClampedArray
  for (let i = 0; i < pixels.length; i += 4) {
    const gray =
      0.299 * pixels[i] + 0.587 * pixels[i + 1] + 0.114 * pixels[i + 2];
    pixels[i] = pixels[i + 1] = pixels[i + 2] = gray;
  }
  postMessage({ pixels }, [pixels.buffer]);
};
```

## 192: How do you parse a big JSON file in a worker?

Fetch and parse it inside the worker, then send back only what the UI needs. If you fetch on the main thread and post the text, you pay for the copy and the main thread still holds the big string.

```js
// worker.js
self.onmessage = async ({ data: url }) => {
  const res = await fetch(url);
  const items = await res.json();
  const summary = items
    .filter((i) => i.active)
    .map(({ id, name }) => ({ id, name }));
  postMessage(summary);
};
```

## 193: Is JSON.parse in a worker always a win?

Not always. Parsing in the worker frees the main thread, but sending the parsed result back uses structured clone, which can cost as much as parsing. If the main thread needs the whole object anyway, the win is small. It's a clear win when the worker can reduce the data (filter, aggregate, index) before sending it back.

## 194: How do you stream and process a large CSV file in a worker?

Read the file as a stream in the worker, decode it with `TextDecoderStream`, and process it line by line. This keeps memory low even for very large files.

```js
self.onmessage = async ({ data: file }) => {
  const reader = file.stream().pipeThrough(new TextDecoderStream()).getReader();
  let leftover = "";
  let rows = 0;
  while (true) {
    const { value, done } = await reader.read();
    if (done) break;
    const lines = (leftover + value).split("\n");
    leftover = lines.pop();
    rows += lines.length;
  }
  if (leftover) rows++;
  postMessage({ rows });
};
```

## 195: How do you run a search index in a worker?

Build the index inside the worker once (from fetched data or IndexedDB), keep it in the worker's memory, and send only queries and result IDs back and forth. The big index never crosses the thread boundary, so each search message is small and fast.

## 196: How do you debounce search input that goes to a worker?

Debounce on the main thread so you don't flood the worker with a message per keystroke. Also tag each query with an ID and ignore replies for older queries, so a slow old result doesn't overwrite a newer one.

```js
let latest = 0;
input.addEventListener(
  "input",
  debounce((e) => {
    const id = ++latest;
    searchWorker.postMessage({ id, query: e.target.value });
  }, 150),
);

searchWorker.onmessage = ({ data }) => {
  if (data.id === latest) showResults(data.results);
};
```

## 197: How do you load WebAssembly in a worker?

Use `WebAssembly.instantiateStreaming` with a fetch inside the worker, then call the exported functions when messages arrive.

```js
// worker.js
const { instance } = await WebAssembly.instantiateStreaming(fetch("/sum.wasm"));

self.onmessage = ({ data }) => {
  postMessage(instance.exports.sum(data.a, data.b));
};
```

Since this is top-level await, create it as a module worker.

## 198: What happens to messages that arrive before a module worker finishes its top-level await?

Messages that the page sends early are queued by the browser, but if your `message` listener is only added after a long `await`, it's easy to end up with confusing timing, and browsers haven't always behaved the same here. It's safer not to depend on it: either register the listener first and await the init inside it, or have the worker send a "ready" message and wait for it on the main thread.

## 199: How do you implement a ready handshake with a worker?

The worker sends a "ready" message after setup. The main thread waits for it before sending work.

```js
// worker.js
await loadModel();
postMessage({ type: "ready" });

// main.js
const ready = new Promise((resolve) => {
  worker.addEventListener("message", function onReady(e) {
    if (e.data.type === "ready") {
      worker.removeEventListener("message", onReady);
      resolve();
    }
  });
});
await ready;
worker.postMessage({ type: "run" });
```

## 200: How do you send a compiled WebAssembly module to several workers?

Compile once on the main thread with `WebAssembly.compileStreaming`, then post the `WebAssembly.Module` to each worker. Modules can be structured cloned (within the same agent cluster), and each worker instantiates it without compiling again.

```js
const module = await WebAssembly.compileStreaming(fetch("/engine.wasm"));
for (const w of workers) w.postMessage({ module });

// worker.js
self.onmessage = async ({ data }) => {
  const instance = await WebAssembly.instantiate(data.module);
};
```

## 201: How do you use scheduler.postTask with priorities?

Pass a callback and an options object with `priority`. The promise resolves with the callback's return value.

```js
scheduler.postTask(() => renderSearchResults(), { priority: "user-blocking" });
scheduler.postTask(() => prefetchNextPage(), { priority: "user-visible" });
scheduler.postTask(() => sendAnalytics(), { priority: "background" });
```

`user-visible` is the default. Higher-priority tasks run before lower ones when both are waiting.

## 202: How do you cancel a task scheduled with postTask?

Use a `TaskController` (or an `AbortController`) and pass its signal. Aborting rejects the task's promise with an `AbortError` if it hasn't started yet.

```js
const controller = new TaskController({ priority: "background" });
scheduler
  .postTask(() => buildIndex(), { signal: controller.signal })
  .catch((err) => console.log(err.name)); // "AbortError"
controller.abort();
```

`TaskController` also lets you change priority later with `controller.setPriority("user-blocking")`.

## 203: How do you add a delay with scheduler.postTask?

Use the `delay` option, in milliseconds. The task is queued after the delay, with its priority.

```js
scheduler.postTask(() => saveDraft(), { priority: "background", delay: 2000 });
```

## 204: What is the difference between scheduler.yield and setTimeout(0)?

Both give the browser a chance to handle input and render. After `setTimeout(0)`, your code goes to the back of the task queue, so other queued tasks (like third-party scripts) can run first and delay you. After `scheduler.yield()`, the rest of your work is given priority over other tasks of the same priority, so it resumes sooner. Also, nested `setTimeout` calls get clamped to at least 4 ms after a few levels.

## 205: How do you write a yield helper that works in all browsers?

Use `scheduler.yield` when it exists and fall back to `setTimeout`.

```js
function yieldToMain() {
  if (globalThis.scheduler?.yield) return scheduler.yield();
  return new Promise((resolve) => setTimeout(resolve, 0));
}

async function processItems(items) {
  let lastYield = performance.now();
  for (const item of items) {
    process(item);
    if (performance.now() - lastYield > 50) {
      await yieldToMain();
      lastYield = performance.now();
    }
  }
}
```

## 206: Why not yield after every single item?

Each yield has a cost: a new task, possible rendering, and other tasks running in between. Yielding after every tiny item can make the total job much slower. A common pattern is to yield based on time, for example every 50 ms or less, as shown in the helper with `performance.now()`.

## 207: What was navigator.scheduling.isInputPending?

`isInputPending()` was a Chromium-only API that told you if there was user input waiting, so you could yield only when needed. Chrome now recommends using `scheduler.yield()` instead, which handles this better and works in more browsers. You may still see `isInputPending` in older code.

## 208: How do you make a click handler respond faster when it has heavy work?

Do the visual update first, then yield, then do the heavy part. This lets the browser paint the feedback before the slow work starts, which improves INP.

```js
button.addEventListener("click", async () => {
  button.classList.add("loading");
  await yieldToMain();
  const result = await worker.call("compute", data);
  showResult(result);
  button.classList.remove("loading");
});
```

## 209: How does requestAnimationFrame plus setTimeout help to run code after paint?

A common trick is to call `setTimeout` inside a `requestAnimationFrame` callback. rAF runs before the next paint, and the `setTimeout` task runs after that paint. This lets you run non-urgent work right after the user sees an update.

```js
requestAnimationFrame(() => {
  setTimeout(() => doNonUrgentWork(), 0);
});
```

## 210: How do you test a module that uses Web Workers in Vitest or Jest?

jsdom doesn't have a real `Worker`. Common options are:

- Keep worker logic in plain functions in a separate module and unit test those functions directly.
- Mock the worker wrapper (for example the module that exports `call()`).
- Use a polyfill package like `@vitest/web-worker` that runs the worker code in the same thread for tests.
- Use browser mode or Playwright for real worker tests.

## 211: Why is it good to keep worker logic in separate pure functions?

It makes the logic easy to test and reuse. The worker file becomes a thin layer that only handles messages and calls the functions. The same functions can also run on the main thread as a fallback, or in Node.js for tests.

```js
// csv.js
export function parseCsv(text) {
  /* ... */
}

// worker.js
import { parseCsv } from "./csv.js";
self.onmessage = (e) => postMessage(parseCsv(e.data));
```

## 212: How do you test Web Workers end to end with Playwright?

Load the page in a real browser and check the UI result after the worker finishes. Playwright also has a `page.on("worker")` event and a `Worker` object that lets you run `evaluate` inside a worker, which is useful for checking worker state.

```js
page.on("worker", (worker) => console.log("Worker started:", worker.url()));
await page.click("#run");
await expect(page.locator("#result")).toHaveText("Done");
```

## 213: What CSP issues come up with workers?

A strict CSP may block worker scripts from blob URLs or from other paths. Add the right sources to `worker-src`, such as `'self'` and, if you build workers from blobs, `blob:`. Module workers also follow `script-src` rules for their imports. Errors usually show in the console as "Refused to create a worker".

## 214: How do Trusted Types affect worker creation?

When a page enforces Trusted Types (`require-trusted-types-for 'script'`), passing a plain string to `new Worker()` is blocked. You must pass a `TrustedScriptURL` created by a Trusted Types policy. This prevents attackers from injecting a worker URL.

```js
const policy = trustedTypes.createPolicy("workers", {
  createScriptURL: (url) => {
    if (new URL(url, location.href).origin === location.origin) return url;
    throw new Error("Bad worker URL");
  },
});
new Worker(policy.createScriptURL("/worker.js"), { type: "module" });
```

## 215: Can a module worker import scripts from a CDN?

Yes, a module worker can `import` from another origin, but the CDN must send proper CORS headers (`Access-Control-Allow-Origin`). If the page is cross-origin isolated with `require-corp`, the resources also need to satisfy COEP. The worker script itself must still be same-origin.

## 216: How do you load a worker script from a CDN when the same-origin rule blocks it?

Create a small same-origin worker that imports the CDN code, or create a blob worker that does it.

```js
const src = `importScripts("https://cdn.example.com/lib/worker.js");`;
const url = URL.createObjectURL(new Blob([src], { type: "text/javascript" }));
const worker = new Worker(url);
```

For module workers, use `import "https://cdn.example.com/lib/worker.mjs";` in the blob code and create the worker with `type: "module"`.

## 217: How do you use Web Workers in Angular?

Run `ng generate web-worker <location>`. The Angular CLI creates a worker file, updates the tsconfig and creates code like this:

```ts
if (typeof Worker !== "undefined") {
  const worker = new Worker(new URL("./app.worker", import.meta.url));
  worker.onmessage = ({ data }) => console.log(data);
  worker.postMessage("hello");
}
```

The CLI bundles the worker as a separate file. Remember that workers don't run during server-side rendering.

## 218: How do you use Web Workers in Next.js?

Create the worker in a client component, inside `useEffect`, using `new Worker(new URL("./worker.js", import.meta.url))`. The bundler picks it up. Don't create it at module level in code that runs on the server, because `Worker` doesn't exist there.

```js
"use client";
useEffect(() => {
  const worker = new Worker(new URL("../workers/heavy.js", import.meta.url));
  worker.onmessage = (e) => setResult(e.data);
  return () => worker.terminate();
}, []);
```

## 219: Why should workers be created inside useEffect in React, not during render?

Render must be pure and can run many times (and twice in Strict Mode in development). Creating a worker during render would start a new thread on every render and leak them. `useEffect` runs after mount and gives a cleanup function where you call `terminate()`.

## 220: Why might a worker be created twice in React development mode?

React 18+ Strict Mode mounts, unmounts and mounts again in development to find missing cleanup. If your effect creates a worker and the cleanup terminates it, you get one worker after the second mount, which is fine. If you don't terminate in cleanup, you end up with two workers. It only happens in development.

## 221: How do you share a single worker across many components?

Create it once at module level in a separate file and export a function that talks to it. All components import the same module, so they share one worker. Create it lazily to avoid issues during server-side rendering.

```js
let worker;
export function getWorker() {
  worker ??= new Worker(new URL("./shared.js", import.meta.url), {
    type: "module",
  });
  return worker;
}
```

## 222: What problems can Comlink solve and what are its limits?

Comlink removes the boilerplate of message IDs, promises and handlers, and supports callbacks through `Comlink.proxy()`. Its limits: every call is still a `postMessage` round trip, so chatty APIs are slow; objects are cloned unless you use `Comlink.transfer()`; and proxies need to be released with `proxy[Comlink.releaseProxy]()` to avoid leaks.

## 223: How do you pass a callback to a worker with Comlink?

Wrap the function with `Comlink.proxy()`. The worker can then call it, and the call is sent back to the main thread as a message.

```js
await api.processFile(
  file,
  Comlink.proxy((percent) => {
    progressBar.value = percent;
  }),
);
```

## 224: How do you transfer a buffer with Comlink?

Use `Comlink.transfer(value, transferList)`.

```js
const buffer = await file.arrayBuffer();
const result = await api.hash(Comlink.transfer(buffer, [buffer]));
```

## 225: What is the difference between importScripts and dynamic import in workers?

`importScripts()` is synchronous, only works in classic workers and puts everything in the global scope. Dynamic `import()` is async, returns a module namespace, and works in module workers. Use dynamic `import()` in module workers to load code only when needed.

```js
self.onmessage = async ({ data }) => {
  if (data.type === "pdf") {
    const { renderPdf } = await import("./pdf.js");
    postMessage(await renderPdf(data.file));
  }
};
```

## 226: How do you use fetch with a progress indicator inside a worker?

Read the response body as a stream and count bytes, sending progress messages to the page.

```js
self.onmessage = async ({ data: url }) => {
  const res = await fetch(url);
  const total = Number(res.headers.get("Content-Length")) || 0;
  const reader = res.body.getReader();
  let received = 0;
  const chunks = [];
  while (true) {
    const { done, value } = await reader.read();
    if (done) break;
    chunks.push(value);
    received += value.length;
    postMessage({ type: "progress", received, total });
  }
  const blob = new Blob(chunks);
  postMessage({ type: "done", blob });
};
```

## 227: How do you compress data in a worker?

Use the built-in `CompressionStream`, which works in workers in all current browsers.

```js
self.onmessage = async ({ data: text }) => {
  const stream = new Blob([text])
    .stream()
    .pipeThrough(new CompressionStream("gzip"));
  const compressed = await new Response(stream).arrayBuffer();
  postMessage(compressed, [compressed]);
};
```

## 228: Can a worker use the Origin Private File System?

Yes. A worker can get a directory with `navigator.storage.getDirectory()`. Dedicated workers can also use `createSyncAccessHandle()` on a file handle, which gives fast synchronous reads and writes. Sync access handles are only available in dedicated workers.

```js
// dedicated worker
const root = await navigator.storage.getDirectory();
const fileHandle = await root.getFileHandle("data.bin", { create: true });
const access = await fileHandle.createSyncAccessHandle();
access.write(new Uint8Array([1, 2, 3]), { at: 0 });
access.flush();
access.close();
```

## 229: Why are sync access handles only in workers?

Synchronous file I/O would block the main thread and freeze the page. In a dedicated worker, blocking is fine because no UI depends on it. This is why libraries like SQLite compiled to WebAssembly run their storage layer in a worker with OPFS sync access handles.

## 230: How do you run SQLite in the browser with a worker?

The official SQLite WebAssembly build can run in a worker and store data in OPFS. The page sends SQL queries to the worker and gets rows back. Running it in a worker keeps queries off the main thread and allows the fast synchronous OPFS API.

## 231: How do you handle unhandled promise rejections inside a worker?

Listen for `unhandledrejection` on the worker's global scope and forward the error to the page. An unhandled rejection in a worker doesn't fire the `error` event on the `Worker` object.

```js
self.addEventListener("unhandledrejection", (event) => {
  postMessage({ type: "error", message: String(event.reason) });
});
```

## 232: How do you send logs from a worker to your error tracking?

Most error tracking SDKs have a worker-compatible build, but a simple approach is to catch errors in the worker and send them to the main thread, which already has the SDK set up. Include the stack trace, since `Error` objects can be cloned and keep `message`, `name` and `stack` in current browsers.

## 233: Do Error objects keep their stack when sent with postMessage?

Error objects are cloneable. The `name` and `message` are kept, and current browsers also keep `stack`, but it's not guaranteed in every browser. For reliable reporting, send a plain object with the fields you need.

```js
postMessage({
  error: { name: err.name, message: err.message, stack: err.stack },
});
```

## 234: How do source maps work with workers?

Bundlers produce source maps for worker chunks just like for main chunks. DevTools loads them when you debug the worker, so you see the original source. Make sure the worker bundle's `//# sourceMappingURL` points to a reachable file, and upload worker source maps to your error tracker too.

## 235: What are common mistakes when using Web Workers?

Common mistakes:

- Creating a new worker for every small task.
- Sending huge objects back and forth instead of transferring or reducing them.
- Forgetting to terminate workers, which leaks memory.
- Expecting DOM access in the worker.
- Using relative URLs that resolve against the wrong base.
- Not handling worker errors, so promises hang forever.
- Moving tiny tasks to a worker where messaging costs more than the work.

## 236: How do you find memory leaks related to workers?

In Chrome DevTools, the Memory panel lets you pick a worker's JavaScript heap and take a heap snapshot of it. Compare snapshots to find growing objects. Also check that workers you no longer need are terminated, and that the main thread isn't keeping references to old workers or pending promise maps that never clear.

## 237: Why can a pending-requests map cause memory leaks?

If replies never come (the worker crashed or a message was ignored), the entries stay in the map forever, holding their callbacks and any data they captured. Clear entries on error, on timeout and when you terminate the worker.

## 238: What is the cost of a worker's memory?

Each worker has its own JavaScript heap, its own copy of loaded scripts and libraries, and its own thread stack. A simple worker may use a few megabytes, while one that loads a big library or WASM module can use much more. Ten workers each loading the same 5 MB library use 50 MB.

## 239: How do you decide what runs on the main thread and what runs in a worker?

Keep on the main thread: DOM updates, event handling, small state changes and anything that needs `window`. Move to a worker: anything CPU-heavy that takes more than about 50 ms and needs only data in and data out. A useful model is "UI on the main thread, logic and data processing in workers".

## 240: What is the "off main thread" architecture?

It's an app design where the main thread only does UI work, and business logic, state, data fetching and processing live in one or more workers. The UI sends actions to the worker and receives new state to render. It keeps the main thread mostly idle and the UI responsive, at the cost of more complex code and messaging.

## 241: How can you run a Redux-style store in a worker?

Put the reducer and state in the worker. The UI posts actions; the worker runs the reducer and posts the new state (or a diff) back. The main thread just renders. The cost is cloning state on every update, so send only the parts the UI needs or send diffs.

```js
// store-worker.js
let state = initialState;
self.onmessage = ({ data: action }) => {
  state = reducer(state, action);
  postMessage(selectVisible(state));
};
```

## 242: What is Partytown?

Partytown is a library that moves third-party scripts (analytics, tag managers) into a web worker. Since those scripts expect DOM access, it proxies DOM calls from the worker to the main thread using synchronous messaging (through a service worker or `Atomics`). It can reduce main-thread work, but some scripts don't work correctly with it.

## 243: How do you handle third-party scripts that block the main thread?

Options include: loading them with `async` or `defer`, delaying them until after the page is interactive, loading them on user interaction, and moving them to a worker with tools like Partytown. Measure their impact with the Performance panel and Long Animation Frames data first.

## 244: What is the Long Animation Frames API?

The Long Animation Frames API (LoAF) reports frames that took longer than 50 ms to render, with details about which scripts ran during them. It's more useful than the old Long Tasks API because it includes rendering work and points to script sources. It's supported in Chromium browsers.

```js
new PerformanceObserver((list) => {
  for (const entry of list.getEntries()) {
    console.log(
      entry.duration,
      entry.scripts.map((s) => s.sourceURL),
    );
  }
}).observe({ type: "long-animation-frame", buffered: true });
```

## 245: How do you measure how long a task took inside a worker?

Use `performance.now()` inside the worker. You can also use `performance.mark()` and `performance.measure()`, which show up in the worker's track in the DevTools Performance panel.

```js
performance.mark("parse-start");
const rows = parseCsv(text);
performance.measure("parse", "parse-start");
```

## 246: Are performance.now() values in a worker comparable with the page's?

Not directly. Each context has its own `performance.timeOrigin`, which is when that context started. To compare times, convert to absolute time with `performance.timeOrigin + performance.now()` on both sides.

## 247: How do you see worker activity in the Performance panel?

Record a profile in Chrome DevTools. Each worker gets its own track under the Main track, showing its tasks, function calls and `performance.measure` entries. You can see when messages are posted and handled and how long each part takes.

## 248: What does "DataCloneError: could not be cloned" usually mean?

You tried to post something that structured clone can't copy, such as a function, a DOM element, a Proxy, a Symbol, an object with a getter that throws, or a class instance holding one of these. Find the bad field by trying `structuredClone()` on parts of your object, then send only plain data.

## 249: Can you send a Proxy or a Vue/MobX reactive object to a worker?

No, a `Proxy` can't be cloned, so posting a reactive object usually throws `DataCloneError`. Convert it to a plain object first, for example with `toRaw()` in Vue (and then clone nested proxies), MobX `toJS()`, or `structuredClone` of a plain copy.

```js
import { toRaw } from "vue";
worker.postMessage(JSON.parse(JSON.stringify(toRaw(state.items))));
```

## 250: How do you use BigInt with workers?

`BigInt` values are cloneable, so you can post them directly. For shared memory, use `BigInt64Array` or `BigUint64Array` over a `SharedArrayBuffer`, and the `Atomics` methods work on those too.

```js
const big = new BigInt64Array(new SharedArrayBuffer(8));
Atomics.add(big, 0, 10n);
```

## 251: How do you enable cross-origin isolation on a static host?

Add the COOP and COEP headers in the host's config. For example, in a Netlify `_headers` file:

```
/*
  Cross-Origin-Opener-Policy: same-origin
  Cross-Origin-Embedder-Policy: require-corp
```

Then check `crossOriginIsolated` in the console. In local development with Vite, set the same headers in `server.headers` in `vite.config.js`.

## 252: What breaks when you turn on COEP require-corp?

Every cross-origin resource (images, scripts, fonts, iframes) must now send CORS headers or `Cross-Origin-Resource-Policy: cross-origin`. Third-party images, ads, embedded videos and analytics often break. Switching to `credentialless` fixes many of these, since resources load without cookies and don't need to opt in.

## 253: What breaks when you turn on COOP same-origin?

Your page can no longer keep a `window` reference to cross-origin popups it opens, and they can't access `window.opener`. This breaks popup-based login flows (like some OAuth or payment popups) that post messages back to the opener. `same-origin-allow-popups` keeps popups working but doesn't give cross-origin isolation.

## 254: What is COEP credentialless?

`Cross-Origin-Embedder-Policy: credentialless` lets a page load cross-origin `no-cors` resources without them opting in, but the requests are sent without cookies or other credentials. It still gives cross-origin isolation, so `SharedArrayBuffer` works. It's supported in Chromium and Firefox, but Safari doesn't support it, so Safari still needs `require-corp`.

## 255: How do you use SharedArrayBuffer when you can't set headers?

Some hosts (like GitHub Pages) don't let you set headers. A known workaround is a service worker that adds COOP and COEP headers to responses, such as the `coi-serviceworker` script. It reloads the page once after the service worker installs. It works, but it's a workaround; setting real headers is better.

## 256: How do you share a counter between threads safely?

Use an `Int32Array` over a `SharedArrayBuffer` and update it with `Atomics.add`, never with `counter[0]++`.

```js
// main.js
const sab = new SharedArrayBuffer(4);
const counter = new Int32Array(sab);
workers.forEach((w) => w.postMessage(sab));

// worker.js
self.onmessage = ({ data }) => {
  const counter = new Int32Array(data);
  for (let i = 0; i < 1000; i++) Atomics.add(counter, 0, 1);
};
```

## 257: Why is counter[0]++ unsafe on shared memory?

`counter[0]++` is three steps: read, add one, write. Two threads can both read 5, both add one, and both write 6, so one update is lost. `Atomics.add` does the read-add-write as one step that no other thread can interrupt.

## 258: What does Atomics.compareExchange do?

`Atomics.compareExchange(arr, index, expected, replacement)` writes `replacement` only if the current value equals `expected`, and returns the old value either way. It's the building block for locks and lock-free structures.

```js
const UNLOCKED = 0,
  LOCKED = 1;
if (Atomics.compareExchange(lock, 0, UNLOCKED, LOCKED) === UNLOCKED) {
  // we got the lock
}
```

## 259: What is the difference between Atomics.load and a normal read?

`Atomics.load` reads the value with sequentially consistent ordering. It guarantees that you see the latest value written with `Atomics.store` or other atomic ops, and that reads and writes around it aren't reordered across it. A normal read on shared memory can be reordered or optimized by the engine or CPU, so another thread's write might not be seen in the order you expect.

## 260: How do you signal a worker that new data is ready using Atomics?

Write the data, then set a flag with `Atomics.store` and wake the worker with `Atomics.notify`. The worker waits on the flag with `Atomics.wait`.

```js
// main.js
data[0] = 42;
Atomics.store(flag, 0, 1);
Atomics.notify(flag, 0);

// worker.js
Atomics.wait(flag, 0, 0); // sleep while flag is 0
console.log(data[0]); // 42
```

## 261: How does Atomics.waitAsync work?

`Atomics.waitAsync` is like `Atomics.wait` but doesn't block. It returns an object `{ async, value }`. If `async` is `true`, `value` is a promise that resolves to `"ok"` or `"timed-out"`. If the value already didn't match, `async` is `false` and `value` is `"not-equal"`. It can be used on the main thread. It's supported in Chromium, Safari and Firefox 145+.

```js
const result = Atomics.waitAsync(flag, 0, 0);
if (result.async) {
  await result.value;
}
console.log("Flag changed");
```

## 262: How do you tell a worker to stop a loop using shared memory?

Share a flag. The main thread sets it with `Atomics.store`, and the worker checks it with `Atomics.load` in its loop. This works even when the worker's event loop is blocked by a long sync loop, unlike a cancel message.

```js
// worker.js
const stop = new Int32Array(sab);
for (let i = 0; i < hugeNumber; i++) {
  if ((i & 0xffff) === 0 && Atomics.load(stop, 0) === 1) break;
  work(i);
}

// main.js
Atomics.store(stop, 0, 1);
```

## 263: What is a growable SharedArrayBuffer?

Since ES2024, you can create a `SharedArrayBuffer` with a `maxByteLength`, and later call `grow()` to make it bigger (it can't shrink). All threads see the new size. Typed arrays created without a fixed length track the new size automatically.

```js
const sab = new SharedArrayBuffer(1024, { maxByteLength: 1024 * 1024 });
const view = new Uint8Array(sab); // length tracks the buffer
sab.grow(4096);
console.log(view.length); // 4096
```

## 264: What is a resizable ArrayBuffer and can it be transferred?

A resizable `ArrayBuffer` is created with `new ArrayBuffer(size, { maxByteLength })` and can grow or shrink with `resize()`. It can be transferred with `postMessage` like a normal buffer, and the receiver gets a resizable buffer with the same max length.

## 265: How do you share a large read-only dataset across many workers?

Put it in a `SharedArrayBuffer` once and send that buffer to all workers. Each worker reads from the same memory, so there are no copies and memory use stays low. Because nobody writes to it after setup, you don't need `Atomics` for reads, as long as the workers start reading after the data was written and posted.

## 266: Why is it safe to read shared data without Atomics if it was written before posting?

`postMessage` creates a happens-before relationship: writes made before the post are visible to the receiver after it gets the message. So if the main thread fills the buffer and then posts it, the workers see the full data. You only need `Atomics` when threads keep writing while others read.

## 267: What is a service worker message channel used for?

Pages can talk to their service worker with `navigator.serviceWorker.controller.postMessage()`, and the service worker can reply through `event.source.postMessage()` or a transferred `MessagePort`. It's used for things like telling the service worker to skip waiting, clearing caches, or sending cache status to the page.

```js
// page
navigator.serviceWorker.controller?.postMessage({ type: "SKIP_WAITING" });

// sw.js
self.addEventListener("message", (event) => {
  if (event.data.type === "SKIP_WAITING") self.skipWaiting();
});
```

## 268: Can a dedicated worker talk to the service worker?

Yes, but not directly in a portable way, since `navigator.serviceWorker` isn't reliably available in dedicated workers across browsers. The usual approach is a `MessageChannel`: create it on the page, send one port to the worker and the other to the service worker. Note that `fetch` requests from a dedicated worker already go through the page's service worker.

## 269: Do fetch requests from a worker go through the service worker?

Yes. Requests made by a dedicated worker or shared worker are controlled by the service worker that controls that worker's client. For dedicated workers, that's usually the same service worker as the page. This means caching rules apply to worker fetches too.

## 270: How do you send a message from a service worker to all open tabs?

Use `clients.matchAll()` and post to each client.

```js
// sw.js
const allClients = await self.clients.matchAll({ type: "window" });
for (const client of allClients) {
  client.postMessage({ type: "NEW_VERSION" });
}
```

## 271: When should you use BroadcastChannel versus clients.matchAll in a service worker?

Both reach all open tabs. `clients.matchAll()` gives you each client's ID, URL and type, so you can target specific tabs or check whether a window is focused. `BroadcastChannel` is simpler for "tell everyone" messages and also reaches workers. Choose `clients` when you need to pick targets.

## 272: How do you pick between Web Locks and a SharedWorker to coordinate tabs?

Use Web Locks when you only need "one at a time" or leader election, such as making sure only one tab runs a sync job. Use a SharedWorker when you need a shared instance with state or a connection. Web Locks is also supported on more platforms, including mobile browsers where SharedWorker support has been weak.

## 273: How do you elect a leader tab with Web Locks?

Each tab requests the same lock and holds it forever. Only one tab gets it; when that tab closes, the lock is released and the next tab becomes leader.

```js
navigator.locks.request("leader", () => {
  startLeaderWork(); // e.g. open the WebSocket
  return new Promise(() => {}); // hold the lock until the tab closes
});
```

## 274: What happens to a held Web Lock when a tab crashes?

The browser releases the lock automatically when the context that held it goes away, including crashes and closing tabs. This is a big advantage over hand-made locks in `localStorage`, which can stay locked forever if a tab dies.

## 275: How do you request a Web Lock without waiting?

Use `ifAvailable: true`. If the lock is free, your callback runs with the lock. If not, the callback runs right away with `null`.

```js
await navigator.locks.request("sync", { ifAvailable: true }, async (lock) => {
  if (!lock) return; // someone else is syncing
  await syncData();
});
```

## 276: What are shared locks in the Web Locks API?

By default locks are `exclusive`. With `mode: "shared"`, many holders can have the lock at once, but no exclusive holder can get it while they do. This gives you a read-write lock: readers take shared locks and writers take exclusive ones.

## 277: How do you prevent the UI from freezing when rendering a long list?

Don't render thousands of DOM nodes at once. Use virtualization (render only visible rows), or render in chunks and yield between them. Data work like sorting and filtering can move to a worker, but DOM creation must stay on the main thread, so chunking or virtualization is the real fix for rendering.

## 278: How do you sort a large dataset in a worker and keep the UI responsive?

Send the data (ideally as typed arrays) to the worker, sort there, and send back sorted indexes instead of the whole sorted data. The main thread keeps its original data and just uses the index order to render.

```js
// worker.js
self.onmessage = ({ data: { values } }) => {
  const order = new Uint32Array(values.length).map((_, i) => i);
  order.sort((a, b) => values[a] - values[b]);
  postMessage({ order }, [order.buffer]);
};
```

## 279: How do you use workers for syntax highlighting in an editor?

Send the text (or changed ranges) to a worker that runs the tokenizer, and send back token positions and types. The main thread applies the styles. Monaco Editor uses this approach: language services like TypeScript checking run in workers.

## 280: How does Monaco Editor use web workers?

Monaco runs an editor worker for diffs and basic tasks, and language workers (TypeScript, JSON, CSS, HTML) for validation, completions and formatting. You configure where to load them with `self.MonacoEnvironment.getWorker` or a bundler plugin. Without the workers, Monaco falls back to running on the main thread and the editor becomes slow.

## 281: What is the "actor model" in the context of web workers?

In the actor model, each actor has its own private state and talks to others only through messages. Web Workers fit this model well: each worker is an actor with its own memory, and `postMessage` is how actors communicate. Thinking in actors helps design apps with several workers without shared state bugs.

## 282: How do you pass messages between workers in a pipeline?

Connect them with `MessageChannel` ports so data flows from worker A to B to C without going through the main thread. Transfer buffers at each step to avoid copies.

```js
const ab = new MessageChannel();
const bc = new MessageChannel();
workerA.postMessage({ out: ab.port1 }, [ab.port1]);
workerB.postMessage({ in: ab.port2, out: bc.port1 }, [ab.port2, bc.port1]);
workerC.postMessage({ in: bc.port2 }, [bc.port2]);
```

## 283: How do you apply backpressure when sending data to a worker?

If the main thread sends faster than the worker can process, messages pile up in memory. Limit how many messages are in flight: wait for the worker to acknowledge before sending more, or use transferable streams, which handle backpressure for you.

```js
let inFlight = 0;
const MAX = 4;
async function send(chunk) {
  while (inFlight >= MAX) await waitForAck();
  inFlight++;
  worker.postMessage(chunk, [chunk.buffer]);
}
```

## 284: How do transferable streams help with backpressure?

When you transfer a `ReadableStream` or `WritableStream` to a worker, the browser connects both sides and respects the stream's queue limits. If the worker reads slowly, the writer's `ready` promise waits, so the producer slows down automatically. You don't need to write your own acknowledgment messages.

```js
// main.js
const { readable, writable } = new TransformStream();
worker.postMessage({ readable }, [readable]);
const writer = writable.getWriter();
for (const chunk of chunks) {
  await writer.ready;
  writer.write(chunk);
}
writer.close();
```

## 285: How do you use a TransformStream in a worker?

Transfer the `TransformStream` itself to the worker, or build one inside the worker and send back its `readable` and `writable` ends. The worker processes chunks off the main thread, and the page uses the stream like any other.

## 286: How do you keep animations smooth while a worker runs?

Workers run on separate threads, so they don't block main-thread animation. But if the worker posts many messages and the main thread updates the DOM for each one, the main thread can still get busy. Batch updates: collect worker results and apply them once per frame inside `requestAnimationFrame`.

```js
let latest;
worker.onmessage = (e) => {
  latest = e.data;
};
function frame() {
  if (latest) {
    render(latest);
    latest = null;
  }
  requestAnimationFrame(frame);
}
requestAnimationFrame(frame);
```

## 287: Can too many worker messages hurt the main thread?

Yes. Each incoming message is a task on the main thread, plus the cost of deserializing the data. Thousands of small messages per second can keep the main thread busy and cause jank. Batch results in the worker and send fewer, larger messages.

## 288: How do you implement a debounced save in a worker?

Run the debounce logic inside the worker: each "change" message resets a timer, and when it fires the worker writes to IndexedDB. The main thread just posts changes and doesn't care about timing.

```js
let timer;
let pendingData;
self.onmessage = ({ data }) => {
  pendingData = data;
  clearTimeout(timer);
  timer = setTimeout(() => saveToIndexedDB(pendingData), 1000);
};
```

## 289: What is the difference between Web Workers and Web Workers with WebAssembly threads?

Plain Web Workers each run separate JavaScript with separate memory. WebAssembly threads use workers too, but all of them share one `WebAssembly.Memory` created with `shared: true`, which is backed by a `SharedArrayBuffer`. This lets C, C++ or Rust code with real threads (like pthreads) run in the browser, but it needs cross-origin isolation.

## 290: How do Emscripten pthreads work in the browser?

When you compile C/C++ with `-pthread`, Emscripten creates a pool of Web Workers, each running the same WASM module with a shared memory. A `pthread_create` call picks a worker from the pool. You can set the pool size with `-sPTHREAD_POOL_SIZE`. The page must be cross-origin isolated for this to work.

## 291: What is wasm-bindgen-rayon?

`wasm-bindgen-rayon` is a Rust crate that lets the Rayon data-parallelism library run in the browser. It sets up a pool of Web Workers that share WASM memory, so Rust code using `par_iter()` runs in parallel. Like other WASM threads, it needs cross-origin isolation.

## 292: How do you fall back when SharedArrayBuffer isn't available?

Check `crossOriginIsolated` at startup. If it's false, use a version of your code that relies on message passing, or a single-threaded WASM build. Many libraries (like FFmpeg.wasm) ship both a multi-threaded and a single-threaded build for this reason.

```js
const wasmUrl = crossOriginIsolated ? "/engine-mt.wasm" : "/engine-st.wasm";
```

## 293: How do you share code between the page and a worker without duplicating bundles?

Put shared code in separate modules and import them in both. Bundlers create separate chunks for the worker, so some shared code may end up in both bundles. That's usually fine. For very large libraries, load them only in the worker and keep the main thread thin.

## 294: How do you handle worker versioning when you deploy a new release?

Bundlers add a content hash to the worker file name (like `worker-3f9a.js`), so a new release loads a new worker file. Shared workers are trickier: an old page and a new page may connect to different versions, or an old shared worker may keep running. Include a version in the URL or `name` so old and new don't mix.

## 295: How do you restart a worker that crashed?

Listen for `error`, terminate the broken worker, create a new one, set it up again, and retry or reject the pending tasks. Add a limit on restarts so a worker that crashes at startup doesn't loop forever.

```js
function startWorker() {
  const w = new Worker(url, { type: "module" });
  w.onerror = () => {
    w.terminate();
    if (restarts++ < 3) worker = startWorker();
  };
  return w;
}
```

## 296: What happens when a worker runs out of memory?

The worker's JavaScript engine throws an out-of-memory error, which usually ends the worker. On the main thread you get an `error` event, or sometimes nothing useful at all. The page itself may survive, but in some browsers a heavy OOM can crash the whole tab. Keep worker memory use bounded, process data in chunks, and avoid holding huge objects.

## 297: How do you avoid running workers during server-side rendering?

`Worker` doesn't exist in Node.js on the server. Create workers only in browser-only code: inside `useEffect`, `onMounted`, `afterNextRender` (Angular) or behind a `typeof window !== "undefined"` check. Don't create them at module top level in shared code.

## 298: How do you lazy-load a worker only when needed?

Create the worker the first time it's needed, not at startup. This saves memory and startup time for users who never use the feature.

```js
let imageWorker;
async function processImage(file) {
  imageWorker ??= new Worker(new URL("./image.js", import.meta.url), {
    type: "module",
  });
  return callWorker(imageWorker, file);
}
```

## 299: How do you preload a worker script?

Use `<link rel="modulepreload">` for module workers or `<link rel="prefetch">` for classic worker scripts. This downloads the file early so the worker starts faster when you create it. Some bundlers add preload hints for workers automatically.

```html
<link rel="modulepreload" href="/assets/worker-3f9a.js" />
```

## 300: How do you explain the trade-offs of using Web Workers in a code review?

Gains: the main thread stays free, INP improves, and heavy work can run on several cores. Costs: more files and messaging code, data must be cloned or transferred, no DOM access, debugging is harder, and each worker uses memory and startup time. A worker is worth it when the work is CPU-heavy and its inputs and outputs are small compared to the work itself.

# Advanced Questions (301-450)

## 301: How does the browser actually send a message between threads?

When you call `postMessage`, the browser serializes the value on the sending thread into an internal format (structured serialize), adds a task to the receiver's port message queue, and the receiving thread deserializes it into new objects in its own heap when the task runs. Transferred objects skip the byte copy: the browser moves ownership of the backing memory and detaches the original. So the cost is split: serialization on the sender, deserialization on the receiver.

## 302: Why does postMessage cost time on both threads?

Serialization happens synchronously inside `postMessage` on the sender, and deserialization happens on the receiver before the `message` handler runs. For large objects both steps can take many milliseconds. This means sending a big object to a worker can still block the main thread for the serialization part, which surprises people who expected the worker to take all the cost.

## 303: What is an agent and an agent cluster in the JavaScript spec?

An agent is a thread of execution with its own job queues and execution context stack: the main thread is one agent and each worker is another. An agent cluster is a group of agents that can share memory. `SharedArrayBuffer` and shared `WebAssembly.Memory` can only be sent between agents in the same cluster. A page and its dedicated workers are in the same cluster; with cross-origin isolation, the browser can put that cluster in its own process.

## 304: Why can't a SharedArrayBuffer be sent to a service worker from a page?

Service workers are not in the same agent cluster as the page, because they aren't owned by one page and can serve many clients. Sending a `SharedArrayBuffer` to a context outside the cluster fails, and the receiver gets a `messageerror` event instead of a `message`. Shared memory works between a page, its dedicated workers and their nested workers.

## 305: What is the JavaScript memory model in simple terms?

The memory model defines what values a thread may see when reading shared memory that other threads write to. Atomic operations are sequentially consistent: all threads agree on one order for them. Non-atomic reads and writes can be reordered by the compiler or CPU, and a racy non-atomic read can see an old value or, for values that span more than one element, a mix of old and new bytes (tearing). Use `Atomics` whenever threads write and read the same location at the same time.

## 306: What is tearing in shared memory?

Tearing happens when a read sees part of one write and part of another. The spec says normal reads and writes of a single integer typed array element (like `Int32Array`) don't tear, but `Float64Array` and `BigInt64Array` elements may. Data that spans several elements, like an `{x, y}` pair stored in two slots, can always be seen half-updated, so for that you need your own synchronization (a lock or a sequence counter).

## 307: What is a data race and why are they dangerous even in JavaScript?

A data race is when two threads access the same memory at the same time, at least one writes, and they don't use atomics. In JavaScript a data race doesn't crash the engine, but the values you read are unpredictable, and the engine's optimizations may make the bug appear only in some builds or devices. They're hard to reproduce and debug, so design to avoid them instead of testing for them.

## 308: How do you implement a mutex with SharedArrayBuffer and Atomics?

Use one `Int32Array` slot: 0 means unlocked, 1 means locked. Take the lock with `compareExchange` and sleep with `Atomics.wait` if it's taken. Release with `store` and `notify`.

```js
const UNLOCKED = 0,
  LOCKED = 1;

export class Mutex {
  constructor(sab, index = 0) {
    this.arr = new Int32Array(sab);
    this.i = index;
  }
  lock() {
    while (
      Atomics.compareExchange(this.arr, this.i, UNLOCKED, LOCKED) !== UNLOCKED
    ) {
      Atomics.wait(this.arr, this.i, LOCKED);
    }
  }
  unlock() {
    Atomics.store(this.arr, this.i, UNLOCKED);
    Atomics.notify(this.arr, this.i, 1);
  }
}
```

This version works only in workers, because `Atomics.wait` can't run on the main thread.

## 309: How would you make a mutex usable from the main thread?

Use `Atomics.waitAsync` instead of `Atomics.wait`, and make `lock()` async. The main thread awaits the promise instead of blocking.

```js
async lockAsync() {
  while (Atomics.compareExchange(this.arr, this.i, 0, 1) !== 0) {
    const r = Atomics.waitAsync(this.arr, this.i, 1);
    if (r.async) await r.value;
  }
}
```

Keep the critical section short on the main thread, since other threads waiting for the lock are blocked until you release it.

## 310: What is the problem with the simple two-state mutex?

`unlock()` always calls `Atomics.notify`, even when no thread is waiting, which costs a system call in some engines. A better mutex uses three states: 0 unlocked, 1 locked with no waiters, 2 locked with waiters. Unlock only notifies when the state was 2. This is the classic futex-based mutex design by Ulrich Drepper.

## 311: What is a spin lock and why is it usually bad in the browser?

A spin lock loops checking a value until it changes, without sleeping. It burns CPU and battery, and if the lock holder is on the same core or paused, the spinner wastes its whole time slice. In browsers, prefer `Atomics.wait` in workers or `waitAsync` on the main thread. Short spinning before sleeping can make sense only for very short critical sections.

## 312: How do you build a single-producer single-consumer ring buffer with shared memory?

Use a `SharedArrayBuffer` with a data area and two indexes: write index (owned by the producer) and read index (owned by the consumer). Each side updates only its own index with `Atomics.store` and reads the other's with `Atomics.load`.

```js
export class RingBuffer {
  constructor(sab, capacity) {
    this.idx = new Int32Array(sab, 0, 2); // [read, write]
    this.data = new Float32Array(sab, 8, capacity);
    this.cap = capacity;
  }
  push(value) {
    const w = Atomics.load(this.idx, 1);
    const r = Atomics.load(this.idx, 0);
    if ((w + 1) % this.cap === r) return false; // full
    this.data[w] = value;
    Atomics.store(this.idx, 1, (w + 1) % this.cap);
    return true;
  }
  pop() {
    const r = Atomics.load(this.idx, 0);
    if (r === Atomics.load(this.idx, 1)) return undefined; // empty
    const value = this.data[r];
    Atomics.store(this.idx, 0, (r + 1) % this.cap);
    return value;
  }
}
// create with: new SharedArrayBuffer(8 + capacity * 4)
```

## 313: Why does the ring buffer write the data before updating the index?

The `Atomics.store` on the write index acts as a release: all writes before it (the data) become visible to a thread that later reads the index with `Atomics.load`. If you updated the index first, the consumer could see the new index and read the slot before the data is written. Order matters with shared memory.

## 314: Where are ring buffers with SharedArrayBuffer used in practice?

They're common in audio: a worker or the main thread produces samples and an `AudioWorkletProcessor` consumes them in real time without allocations or messages. They're also used for streaming data between a WASM engine and the UI, and for logging from hot loops. Libraries like `ringbuf.js` implement this pattern.

## 315: Why shouldn't you use postMessage inside an AudioWorklet's process method?

`process()` is called every 128 samples (about every 2.7 ms at 48 kHz) on a real-time audio thread. `postMessage` allocates memory and may trigger garbage collection, which can cause audio glitches. Use a shared ring buffer to move data in and out, and keep allocations out of `process()`.

## 316: What constraints does code inside an AudioWorkletProcessor have?

It must finish each `process()` call within the time budget of one render quantum, it should not allocate memory in the hot path, and it has no `fetch`, no timers and no `importScripts`. It talks to the main thread through the node's `port` or through shared memory. Heavy work like decoding should happen elsewhere.

## 317: What is false sharing?

False sharing happens when two threads write to different variables that sit on the same CPU cache line (usually 64 bytes). The CPU keeps moving that cache line between cores even though the threads don't touch each other's data, which slows both down. With `SharedArrayBuffer`, put frequently written per-thread counters at least 64 bytes apart.

```js
// each worker gets its own counter, 64 bytes apart
const STRIDE = 16; // 16 * 4 bytes = 64 bytes
const counters = new Int32Array(new SharedArrayBuffer(workers * 64));
// worker k uses counters[k * STRIDE]
```

## 318: Why is high-resolution timing tied to cross-origin isolation?

Precise timers help side-channel attacks like Spectre measure tiny differences in memory access time. Browsers reduce `performance.now()` precision (for example to 100 microseconds) on normal pages and give finer precision (around 5 microseconds) only on cross-origin isolated pages. `SharedArrayBuffer` can also be used to build a precise timer, which is why it also needs isolation.

## 319: How could SharedArrayBuffer be used as a timer in an attack?

A worker runs a tight loop that increments a value in shared memory. The main thread reads that value before and after an operation, and the difference works like a very precise clock. This makes timing attacks possible even when `performance.now()` is coarse. Cross-origin isolation reduces the risk by keeping sensitive cross-origin data out of the process.

## 320: Is a Web Worker a security sandbox for untrusted code?

No. A worker runs with the same origin as the page, so it can use `fetch` with the user's cookies, read the origin's IndexedDB, and post messages to the page. It also shares the same process in most cases. To run untrusted code, use a sandboxed cross-origin iframe (and maybe a worker inside that iframe), or a separate origin.

## 321: How can you run untrusted user code more safely in the browser?

Put it in an `<iframe sandbox="allow-scripts">` served from a different origin, so it can't access your cookies, storage or DOM. Inside the iframe you can create a worker to keep it off the iframe's thread, and use `terminate()` as a hard timeout. Communicate only through `postMessage` and check every message on your side.

## 322: How do you enforce a time limit on untrusted or buggy code in a worker?

Start a timer on the main thread when you post the job. If no result arrives before the timer fires, call `worker.terminate()` and create a new worker. This works even for infinite loops, because termination doesn't need the worker's cooperation.

```js
function runWithLimit(code, ms) {
  return new Promise((resolve, reject) => {
    const w = new Worker(sandboxUrl);
    const t = setTimeout(() => {
      w.terminate();
      reject(new Error("Too slow"));
    }, ms);
    w.onmessage = (e) => {
      clearTimeout(t);
      w.terminate();
      resolve(e.data);
    };
    w.postMessage(code);
  });
}
```

## 323: What should you validate in messages coming from a worker or another window?

For other windows and iframes, check `event.origin` against an allow list and ignore everything else. For any message, check its shape (type field, expected fields) before using it, and never pass message content to `innerHTML` or `eval`. Workers you created are trusted at the origin level, but if they run third-party or user code, treat their messages as untrusted too.

## 324: Can a worker be used to bypass Content Security Policy?

Workers have their own CSP rules. For classic workers created from same-origin URLs, the worker's own response headers define its CSP; for blob and data workers, they inherit the creator's policy. A wrong `worker-src` that allows `blob:` together with a script injection bug could let an attacker run code in a worker. Keep `worker-src` tight and enable Trusted Types.

## 325: How does storage partitioning affect shared workers?

Browsers now partition storage and some communication APIs by top-level site. A shared worker created by an iframe from `widget.com` embedded in `a.com` is a different instance from one created by the same iframe embedded in `b.com`. This stops cross-site tracking, but it means a third-party widget can't use one shared worker across all sites that embed it.

## 326: How does storage partitioning affect BroadcastChannel?

`BroadcastChannel` is also partitioned by top-level site in current browsers. Two iframes from the same origin embedded in different top-level sites can't talk to each other over a `BroadcastChannel` anymore. Same-site tabs still work as before.

## 327: What happens to workers in a page that enters the back/forward cache?

When a page goes into the bfcache, its dedicated workers are paused along with it and resumed if the user comes back. Some features can stop a page from being cached; in the past open shared workers or broadcast channels did that in some browsers. Use the `pagehide` and `pageshow` events, check `event.persisted`, and don't assume `pagehide` means the workers are gone.

## 328: How do mobile browsers treat workers in the background?

Mobile browsers aggressively freeze or throttle hidden tabs to save battery. A worker in a hidden tab may be paused completely, and the page may be killed later. Don't rely on workers for long background jobs on mobile. For work that must finish, save progress often (IndexedDB) and resume when the page is visible, or use server-side processing.

## 329: What is the Page Lifecycle API and how does it relate to workers?

The Page Lifecycle API adds `freeze` and `resume` events in Chromium. When a page is frozen, its timers and tasks stop, including those of its dedicated workers. Listen to `freeze` to save state and close connections, and `resume` to restore them.

```js
document.addEventListener("freeze", () =>
  worker.postMessage({ type: "flush" }),
);
```

## 330: How are timers in workers throttled compared to the main thread?

On the main thread, browsers clamp nested `setTimeout` calls to at least 4 ms after five levels, and throttle timers in hidden tabs heavily (for example to once per second, or once per minute after a long time in Chrome). Dedicated worker timers aren't throttled as much in some browsers, which is why some apps move timer-based logic into a worker. But this behavior isn't guaranteed and may change.

## 331: Why do some apps run a timer inside a worker?

Because timers in hidden tabs on the main thread can be throttled to once per second or less, which breaks things like session keep-alive pings or game clocks. Worker timers have historically been throttled less. It can help, but browsers may still freeze the whole page, so it's not a reliable way to run background jobs.

## 332: How does a worker's event loop differ from the main thread's?

A worker's event loop has task queues and a microtask queue, but no rendering step (except that dedicated workers can have `requestAnimationFrame` for `OffscreenCanvas`). There's no input handling, no layout and no paint. So a worker task can run long without hurting frame rate, but it still blocks other messages to that worker until it finishes.

## 333: What happens if a worker runs an infinite loop?

That worker's thread is stuck forever. It can't handle messages, timers or promises. The main thread and other workers keep working. The only way out is `worker.terminate()` from the page. This is a good reason to wrap worker calls with timeouts.

## 334: How do you design a worker pool with priorities?

Keep separate queues per priority (or one priority queue) and always take tasks from the highest non-empty queue when a worker is free. Consider aging, which raises the priority of tasks that waited long, so low-priority work doesn't starve.

```js
const queues = { high: [], normal: [], low: [] };
function nextTask() {
  return queues.high.shift() ?? queues.normal.shift() ?? queues.low.shift();
}
```

## 335: What is work stealing and is it useful in browser worker pools?

In work stealing, each worker has its own queue, and an idle worker takes tasks from another worker's queue. It balances uneven workloads without a central queue. In browsers, workers can't directly read each other's queues unless you use shared memory, so most browser pools use a central queue on the main thread, which is simpler and good enough for most cases.

## 336: How do you choose chunk sizes when splitting work across workers?

Too large chunks cause bad load balancing: one slow chunk keeps a worker busy while others wait. Too small chunks waste time on messaging. A good start is several chunks per worker (for example 4 to 8 times the pool size), each taking tens to hundreds of milliseconds. Measure and adjust.

## 337: Why might parallel code in workers be slower than single-threaded code?

Common reasons: the data copying costs more than the work, the work is memory-bound so more threads fight over memory bandwidth, chunks are uneven, workers start cold (JIT not warmed up, scripts parsing), or the device has few fast cores and many slow ones. Always measure, and include setup and messaging time.

## 338: How does the JIT warm-up affect workers?

Each worker has its own JavaScript engine instance, so code that's already optimized on the main thread starts cold in a worker. The first calls run in the interpreter and get faster over time. Short-lived workers may never reach optimized code. Long-lived pooled workers avoid paying this cost again and again.

## 339: How do big.LITTLE CPUs on phones affect worker performance?

Many phones have a few fast cores and several slow ones. `hardwareConcurrency` counts all of them. If you split work evenly across 8 workers, the chunks on slow cores finish much later, and the total time is set by the slowest worker. Smaller chunks with a shared queue help, because fast workers just take more chunks.

## 340: What is Amdahl's law and why does it matter for workers?

Amdahl's law says the speedup from parallelism is limited by the part of the work that must run serially. If 20% of a job must stay on one thread, the best speedup is 5x no matter how many workers you add. For workers, serial parts include splitting data, messaging and merging results. Reduce them before adding more workers.

## 341: How do you merge results from many workers efficiently?

Have workers send compact results, like partial sums, counts or sorted runs as typed arrays. Then merge on the main thread or in one worker. For sorting, each worker sorts its chunk and you do a k-way merge. For large merges, do the merge in a worker too, so the main thread only gets the final result.

## 342: How would you design a client-side image editor with workers?

Keep the UI and the canvas display on the main thread (or render via `OffscreenCanvas` in a worker). Store image layers as `ArrayBuffer`s in a worker, apply filters there with WASM or JS, and send back only the visible region as an `ImageBitmap`. For heavy filters, split the image into tiles across a worker pool. Keep an undo history in the worker or in IndexedDB, not as copies on the main thread.

## 343: How would you design a spreadsheet calculation engine using workers?

Run the formula engine in a worker that holds the cell data and dependency graph. When the user edits a cell, the main thread sends the change, the worker recalculates only dependent cells and sends back the changed values for visible cells. Use request IDs or version numbers so stale results are ignored. For huge sheets, split independent parts of the graph across workers.

## 344: How would you build offline full-text search for a docs site?

Prebuild a search index at build time, fetch it in a worker, and keep it in memory there (and cache it in the Cache API or IndexedDB). The search box sends queries to the worker and gets back ranked result IDs and snippets. The main thread never loads the full index, so the page stays light.

## 345: How would you design a live dashboard that receives thousands of updates per second?

Open the WebSocket in a worker (or a shared worker for multiple tabs). The worker parses, aggregates and throttles updates, and sends a batched snapshot to the main thread at most once per frame or every 100 to 250 ms. Charts could render with `OffscreenCanvas` in the same or another worker. The main thread only handles UI and small DOM changes.

## 346: How do you avoid sending stale results from a worker after the input changed?

Tag each request with a version number. The worker can check whether a newer request arrived before doing expensive work, and the main thread drops any reply whose version isn't the latest. For long jobs, use a shared cancel flag so the worker stops early.

## 347: How does Figma-style or Google Docs-style rendering use workers and WASM?

Large design and document apps often run their core engine in WebAssembly, render to a canvas with WebGL or WebGPU, and use workers for tasks like image decoding, font processing, file import and export. The main thread focuses on input and the render loop. The exact architecture varies, but the idea is the same: heavy logic off the main thread, small messages, shared or transferred buffers for big data.

## 348: How do you use WebGPU from a worker?

`navigator.gpu` is available in dedicated workers in browsers that support WebGPU. Transfer an `OffscreenCanvas` to the worker, call `canvas.getContext("webgpu")`, and run the whole render loop there. You can also use WebGPU in a worker for compute work, like ML inference, without any canvas.

```js
// worker.js
self.onmessage = async ({ data: { canvas } }) => {
  const adapter = await navigator.gpu.requestAdapter();
  const device = await adapter.requestDevice();
  const ctx = canvas.getContext("webgpu");
  ctx.configure({ device, format: navigator.gpu.getPreferredCanvasFormat() });
  // render loop with requestAnimationFrame
};
```

## 349: How do you run ML models in the browser without blocking the UI?

Load the model and run inference in a worker using libraries like ONNX Runtime Web or Transformers.js, which support WebGPU and WASM backends. Send inputs (as typed arrays when possible) and get results back. Loading a large model can take seconds and lots of memory, so start it early, show progress, and keep the worker alive for reuse.

## 350: What is the WebAssembly threads proposal and its main parts?

It adds three things: shared linear memory (`WebAssembly.Memory` with `shared: true`, backed by a `SharedArrayBuffer`), atomic memory instructions (load, store, read-modify-write, compare-exchange), and wait/notify instructions. Threads themselves are still created as Web Workers by the JavaScript glue code. It's supported in all current major browsers on cross-origin isolated pages.

## 351: How do you create a shared WebAssembly memory?

Create a `WebAssembly.Memory` with `shared: true` and a `maximum`. Its `buffer` is a `SharedArrayBuffer`, which you can post to workers. Each worker instantiates the same module importing that memory.

```js
const memory = new WebAssembly.Memory({
  initial: 256,
  maximum: 4096,
  shared: true,
});
console.log(memory.buffer instanceof SharedArrayBuffer); // true
for (const w of workers) w.postMessage({ module, memory });
```

## 352: What happens to typed array views when shared WebAssembly memory grows?

When a shared memory grows, `memory.buffer` returns a new `SharedArrayBuffer` object with the larger size, but views created on the old buffer object keep the old length. Each thread must recreate its views after growth. Emscripten handles this by checking the buffer size and rebuilding views (the `HEAP8`, `HEAP32` and so on) when it changes.

## 353: Why is Atomics.wait not allowed on the main thread, and how do WASM threads deal with it?

Blocking the main thread would freeze the UI and can deadlock if the thread being waited on needs the main thread to make progress. WASM code compiled with pthreads may block on locks, so toolchains like Emscripten busy-wait on the main thread for short locks, or recommend running the whole app in a worker (the `PROXY_TO_PTHREAD` option) so the main thread never blocks.

## 354: What is the PROXY_TO_PTHREAD pattern?

In Emscripten, `-sPROXY_TO_PTHREAD` runs the program's `main()` in a worker instead of on the main thread. The main thread only handles browser APIs that need it, and calls from the worker that need the main thread are proxied there. This avoids blocking the UI and avoids main-thread deadlocks when the program uses locks.

## 355: How can a deadlock happen with workers?

A deadlock happens when two threads each wait for something the other holds. For example, worker A holds lock 1 and waits for lock 2, while worker B holds lock 2 and waits for lock 1. Another case: a worker blocks with `Atomics.wait` for a value that only the main thread sets, but the main thread is waiting for a message from that same worker. Prevent it by always taking locks in the same order and avoiding blocking waits on message-based replies.

## 356: How do you debug a suspected deadlock between workers?

Pause each worker in DevTools (Sources panel, Threads list) and see where each one is stopped. A worker stuck inside `Atomics.wait` shows that call on its stack. Add logging around lock acquire and release with thread names. Add timeouts to `Atomics.wait` in development builds so a stuck wait reports itself instead of hanging forever.

## 357: What is the ABA problem?

In lock-free code, a thread reads value A, gets paused, another thread changes it to B and back to A, and the first thread's `compareExchange` succeeds because it still sees A, even though the state changed in between. It's a classic issue in lock-free stacks and queues. A common fix is to pair the value with a version counter that increases on every change.

## 358: How would you synchronize a structured record (several fields) between threads without a lock?

Use a sequence lock (seqlock). The writer increments a sequence number (making it odd), writes the fields, then increments again (even). The reader reads the sequence, reads the fields, and reads the sequence again; if it was odd or changed, it retries.

```js
// writer
Atomics.add(seq, 0, 1);
data[0] = x;
data[1] = y;
Atomics.add(seq, 0, 1);

// reader
let s1, s2, x, y;
do {
  s1 = Atomics.load(seq, 0);
  x = data[0];
  y = data[1];
  s2 = Atomics.load(seq, 0);
} while (s1 !== s2 || s1 & 1);
```

This works well when writes are rare and reads are frequent.

## 359: How do you implement a semaphore with Atomics?

Store the number of available permits. `acquire` decrements when the count is above zero (using `compareExchange` in a loop) and waits when it's zero. `release` increments and notifies one waiter.

```js
function acquire(arr, i) {
  while (true) {
    const n = Atomics.load(arr, i);
    if (n > 0 && Atomics.compareExchange(arr, i, n, n - 1) === n) return;
    if (n === 0) Atomics.wait(arr, i, 0);
  }
}
function release(arr, i) {
  Atomics.add(arr, i, 1);
  Atomics.notify(arr, i, 1);
}
```

## 360: What is a barrier and how would you build one for workers?

A barrier makes N workers wait until all of them reach the same point. Keep a counter and a generation number. Each worker increments the counter; the last one resets it, bumps the generation and notifies all. The others wait until the generation changes.

```js
function barrier(arr, n) {
  const gen = Atomics.load(arr, 1);
  if (Atomics.add(arr, 0, 1) === n - 1) {
    Atomics.store(arr, 0, 0);
    Atomics.add(arr, 1, 1);
    Atomics.notify(arr, 1);
  } else {
    Atomics.wait(arr, 1, gen);
  }
}
```

## 361: What does Atomics.wait return if the value already changed?

It returns `"not-equal"` immediately without sleeping. This is important: it avoids the "lost wakeup" problem where the other thread changes the value and calls `notify` between your check and your wait. Because `wait` checks and sleeps in one atomic step, you won't miss a notification that happens after your check.

## 362: What is the lost wakeup problem?

A thread checks a condition, decides to sleep, but before it actually sleeps another thread changes the condition and sends a wake-up signal. The signal is lost and the first thread sleeps forever. `Atomics.wait` avoids this by comparing the expected value and going to sleep atomically, so pass the value you saw as the expected value.

## 363: Can Atomics.notify wake a waitAsync waiter on the main thread?

Yes. `Atomics.notify` wakes both blocking waiters (`Atomics.wait` in workers) and async waiters (`Atomics.waitAsync` anywhere) on that index, in the order they started waiting. The async waiter's promise resolves on its own thread's event loop.

## 364: What is a typical way to build synchronous calls from a worker to the main thread?

The worker writes a request into shared memory, posts a message (or sets a flag) and then blocks with `Atomics.wait`. The main thread handles the request asynchronously and writes the response into shared memory, then calls `Atomics.notify`. The worker wakes and reads the result. Tools like Partytown and some WASM runtimes use this to give synchronous APIs to code running in a worker.

## 365: Why would code in a worker need synchronous calls to the main thread?

Some code was written to call DOM or browser APIs synchronously, like third-party scripts reading `document.cookie` or C code calling a blocking filesystem API. That code can't easily be rewritten to async. Blocking the worker with `Atomics.wait` while the main thread does the work lets this code run in a worker unchanged.

## 366: What is the alternative to SharedArrayBuffer for synchronous worker calls on pages that aren't cross-origin isolated?

A known trick is a synchronous `XMLHttpRequest` from the worker to a URL that a service worker intercepts. The service worker waits for the main thread's answer and returns it as the XHR response. It's slower and hacky, but it works without cross-origin isolation. Partytown uses this as a fallback.

## 367: What is Atomics.pause?

`Atomics.pause()` is a newer addition that gives the CPU a hint that the code is in a spin-wait loop, similar to the `pause` instruction on x86. It doesn't block or yield to other threads; it just makes short spin loops more efficient. It's useful only in very short spin-then-wait patterns. Check browser support before relying on it.

## 368: How do you avoid allocation and GC pauses in a hot worker loop?

Reuse typed arrays instead of creating new ones per iteration, avoid creating temporary objects and closures, and keep data in flat numeric arrays. Garbage collection in a worker only pauses that worker, but for real-time work (audio, rendering at 60 fps) those pauses still cause dropped frames or glitches.

## 369: Does garbage collection in a worker pause the main thread?

Usually not. Each worker has its own heap and its own garbage collector, so a GC in the worker pauses that worker only. Some engine work is shared at the process level, but for most purposes worker GC doesn't stop the main thread. Large deserialization of messages on the main thread, however, does create garbage there.

## 370: How do you measure memory used by workers?

In Chromium on cross-origin isolated pages, `performance.measureUserAgentSpecificMemory()` returns a breakdown of memory use that includes workers. In DevTools, the Memory panel lets you select each worker's heap. You can also watch overall memory in the browser's task manager (Shift+Esc in Chrome), where dedicated workers are counted with their page.

## 371: What happens to the transfer list if postMessage throws?

If serialization fails (for example `DataCloneError`), nothing is transferred and the original buffers stay usable on the sender side. Transfer only happens when the whole message is serialized successfully. This makes it safe to catch the error and retry with fixed data.

## 372: Can you transfer an ArrayBuffer that a WebAssembly.Memory uses?

No. A buffer that belongs to a `WebAssembly.Memory` can't be detached by transfer; trying throws a `TypeError` or `DataCloneError`. To send WASM memory data, copy the bytes you need into a new `ArrayBuffer` and transfer that, or use shared WASM memory so other threads can see it directly.

## 373: What are the security considerations for transferring OffscreenCanvas?

Once transferred, the canvas element on the page shows what the worker draws, and the worker has full control of the drawing. If the canvas becomes tainted by drawing cross-origin images without CORS, reading pixels back (`getImageData`, `convertToBlob`) throws a `SecurityError`, in the worker as well. Same rules apply as on the main thread.

## 374: How does OffscreenCanvas rendering in a worker reach the screen?

For a canvas obtained with `transferControlToOffscreen()`, the worker's draws are committed to the placeholder canvas on the page automatically at the end of each worker task or animation frame. The compositor shows the new frame without the main thread doing any work. This is why worker-rendered canvases keep updating even when the main thread is busy.

## 375: What is the difference between drawing to a transferred OffscreenCanvas and a standalone one?

A standalone `new OffscreenCanvas(w, h)` isn't connected to anything on screen. You get output by calling `transferToImageBitmap()` or `convertToBlob()` and sending it somewhere. A canvas from `transferControlToOffscreen()` is linked to a `<canvas>` element, so draws appear on the page automatically.

## 376: How do you sync OffscreenCanvas animation in a worker with the display refresh?

Use `requestAnimationFrame` inside the dedicated worker. It's tied to the display's refresh for the linked canvas, so your render loop runs once per frame. Don't use `setInterval(16)`, which drifts and doesn't match high-refresh displays.

```js
function loop(t) {
  draw(t);
  self.requestAnimationFrame(loop);
}
self.requestAnimationFrame(loop);
```

## 377: What is ImageBitmapRenderingContext used for?

`canvas.getContext("bitmaprenderer")` gives a context with `transferFromImageBitmap(bitmap)`, which shows an `ImageBitmap` without copying. A common pattern is: worker renders to a standalone `OffscreenCanvas`, calls `transferToImageBitmap()`, transfers the bitmap to the main thread, and the main thread displays it with the bitmap renderer. It's an alternative when you can't transfer canvas control.

## 378: How do you process video frames in a worker?

Use WebCodecs and Insertable Streams. `VideoFrame` objects are transferable, so you can send frames to a worker, process them there (with `OffscreenCanvas`, WebGL or WebGPU), and send them back. In Chromium, `MediaStreamTrackProcessor` gives a `ReadableStream` of frames that you can transfer to the worker directly.

```js
// main.js (Chromium)
const [track] = stream.getVideoTracks();
const processor = new MediaStreamTrackProcessor({ track });
worker.postMessage({ frames: processor.readable }, [processor.readable]);
```

## 379: Why must you close VideoFrame objects quickly?

A `VideoFrame` holds GPU or decoder memory, often from a small pool. If you don't call `frame.close()`, the decoder or camera runs out of frame buffers and stalls. Close frames as soon as you've drawn or encoded them, in the worker or wherever they end up.

## 380: How does WebCodecs fit with workers?

`VideoEncoder`, `VideoDecoder`, `AudioEncoder` and `AudioDecoder` are available in dedicated workers. Encoding and decoding already happen off the main thread, but the callbacks and frame handling run on the thread that owns the codec. Putting the whole pipeline in a worker keeps frame handling and muxing from competing with the UI.

## 381: What happens to a message posted to a worker that was already terminated?

It's silently dropped. `postMessage` doesn't throw and no event fires. Any promise waiting for a reply will hang unless your wrapper tracks the worker's state and rejects calls after termination.

## 382: What happens if the main thread posts a message before the worker script has loaded?

The message is queued. Once the worker script is loaded and run, queued messages are delivered in order. So you can call `postMessage` right after `new Worker()`. The gotcha is with handlers registered late (after an `await`); in classic and simple module workers that register `onmessage` at the top level, this works as expected.

## 383: What happens to queued messages if the worker throws during startup?

If the script throws at the top level, the `error` event fires on the `Worker` object. Depending on where it threw, the `message` handler may never be set, so queued messages are dropped without any reply. Wrappers should treat a startup error as fatal and reject all pending calls.

## 384: How does the browser decide whether to reuse an existing SharedWorker?

It matches on the script URL, the `name` option and the storage key (origin plus partition). If a running shared worker matches all three, the new page connects to it. If the `type` or `credentials` options differ from the running one, the constructor fails with an error event. Changing the URL (for example a new hashed file) creates a new instance.

## 385: How do you upgrade a long-running SharedWorker to a new version?

Old tabs keep the old shared worker alive. Options: include the app version in the worker `name` or URL so new tabs start a new instance; have new tabs send a "version" message and ask the old worker to tell its clients to reload; or keep the protocol between pages and the worker backward compatible. Plan for mixed versions running at the same time.

## 386: How do you handle a SharedWorker that becomes a single point of failure?

If the shared worker crashes, all tabs lose its features at once. Wrap its logic in try/catch, catch errors per port, and have tabs detect a dead worker (no reply to pings) and reconnect by creating a new `SharedWorker`. For critical features, have a fallback path that works per tab.

## 387: How do you protect a SharedWorker from a bad or old tab?

Treat each port as an independent client. Check message shapes and versions, and ignore or reject unknown messages. Don't let one client's bad input throw an uncaught error that breaks the whole worker. Limit per-client resources, like queue sizes, so one tab can't eat all the memory.

## 388: How do you share an authenticated session across tabs safely?

Use a single owner for refresh logic (a shared worker, or the tab holding a Web Lock) so only one refresh request runs at a time. Share the new access token through `BroadcastChannel` or the shared worker. Don't put long-lived tokens in places JavaScript can read if you can avoid it; HTTP-only cookies avoid most cross-tab token sharing.

## 389: How do you avoid the thundering herd when many tabs wake up at once?

When the network comes back or a token expires, every tab may fire the same request. Use Web Locks with `ifAvailable` so only one tab does the work, and have it broadcast the result. For polling, elect a leader tab that polls and shares the data with others.

## 390: How does a service worker's lifetime affect long tasks?

Browsers stop an idle service worker after about 30 seconds and may limit how long a single event can keep it alive, even with `event.waitUntil()`. Long computations or long-lived connections in a service worker can be cut off. Move heavy work to a dedicated worker in a page, and use Background Fetch or Background Sync for work that must survive the page.

## 391: Can you use SharedArrayBuffer in a SharedWorker?

A shared worker can create and use a `SharedArrayBuffer` internally if the shared worker itself is cross-origin isolated. But a shared worker isn't in the same agent cluster as its client pages, so you can't send a `SharedArrayBuffer` between a page and a shared worker. Sharing memory works only within one page's cluster (page, dedicated workers, nested workers).

## 392: How do you make a dedicated worker cross-origin isolated?

A dedicated worker inherits cross-origin isolation from its creator, but its script response must also be served with a COEP header (`require-corp` or `credentialless`) in browsers that check it. If the worker script is missing COEP, the worker may fail to load or not be isolated. Serve the same headers for worker scripts as for the page.

## 393: What happens if one iframe on an isolated page isn't served with COEP?

With `require-corp`, a cross-origin iframe must also send COEP and a CORP header, or it won't load. A same-origin iframe without COEP is blocked too. This is often the hardest part of enabling isolation on a real site with ads or embeds. The `credentialless` iframe attribute (`<iframe credentialless>`) in Chromium can help load third-party iframes without them opting in.

## 394: What is the Document-Isolation-Policy header?

`Document-Isolation-Policy` is a newer Chromium header that lets a single document become cross-origin isolated without requiring the whole page tree to use COOP and COEP. The browser puts that document in its own process instead. It aims to make `SharedArrayBuffer` easier to use on pages with popups and third-party content. Support is limited to Chromium, so you still need the COOP/COEP setup for other browsers.

## 395: How do you test a feature that depends on SharedArrayBuffer in CI?

Run tests in real browsers (Playwright or WebDriver) against a dev server that sends COOP and COEP headers. Assert `crossOriginIsolated === true` at the start so a missing header fails loudly instead of silently using the fallback. Also test the fallback path by turning the headers off.

## 396: How would you profile postMessage overhead in a real app?

Record a Performance profile and look for "Serialize" or `postMessage` time on the sender and the deserialization before `onmessage` on the receiver. Add `performance.mark` before posting and at the start of the handler. Compare payload sizes, try transferring or reshaping data, and measure again. Look at both the time and the extra garbage created.

## 397: Why can sending many small objects be slower than sending one big typed array?

Structured clone visits each object and property, writes type tags and handles references, so a million small objects mean millions of steps on both sides and many new objects for the GC. A typed array of the same data is one memory copy (or no copy if transferred). Reshaping data into typed arrays often gives 10x or bigger speedups for worker messaging.

## 398: Is sending a JSON string ever faster than sending an object?

Sometimes, for large plain-data objects. Cloning a string is a single memory copy, and `JSON.parse` is very optimized. In some benchmarks, `JSON.stringify` plus posting a string plus `JSON.parse` beat posting the object directly. But it loses types like `Map`, `Date` and typed arrays, and results vary by browser. Measure your real data before choosing.

## 399: How does Blob passing work without copying large data?

A `Blob` is an immutable handle to data that may live in browser-managed memory or on disk. Cloning a `Blob` copies only the handle, not the data. So posting a 1 GB `File` to a worker is cheap. The worker reads it lazily with `stream()`, `slice()` or `arrayBuffer()`.

## 400: How would you hash a multi-gigabyte file in the browser without running out of memory?

Send the `File` to a worker (cheap, it's a handle), read it in chunks with `file.slice()` or `file.stream()`, and update an incremental hash. `crypto.subtle.digest` doesn't support incremental hashing, so use a streaming hash library (often WASM-based) in the worker.

```js
self.onmessage = async ({ data: file }) => {
  const hasher = await createSha256(); // e.g. from a WASM hashing library
  const reader = file.stream().getReader();
  while (true) {
    const { done, value } = await reader.read();
    if (done) break;
    hasher.update(value);
  }
  postMessage(hasher.digest("hex"));
};
```

## 401: How would you design a generic RPC layer for workers?

Define a small protocol: requests have `{ id, method, args }`, replies have `{ id, result }` or `{ id, error }`, and events have `{ event, data }` without an ID. On the worker side, map method names to functions and catch all errors. On the main side, keep a pending map with timeouts, reject everything on worker error, and support transfer lists. Comlink is a ready-made version of this idea.

```js
// worker side
const methods = { parse, search, stats };
self.onmessage = async ({ data: { id, method, args } }) => {
  try {
    postMessage({ id, result: await methods[method](...args) });
  } catch (err) {
    postMessage({ id, error: { name: err.name, message: err.message } });
  }
};
```

## 402: How do you design worker APIs to avoid chatty communication?

Make each call do a meaningful chunk of work. Instead of `getCell(row, col)` called 10,000 times, offer `getRange(rows, cols)`. Keep state in the worker so the main thread sends only small changes. Batch events and send them once per frame. Each message round trip costs at least a few tens of microseconds plus serialization, which adds up fast.

## 403: How do you keep type safety across the worker boundary in TypeScript?

Define the message types in a shared module and use discriminated unions for requests and replies. Or define the worker API as an interface and use Comlink's `Remote<T>` type, which turns every method into a promise-returning one.

```ts
// api.ts
export interface ParserApi {
  parse(text: string): Promise<Row[]>;
}

// main.ts
import * as Comlink from "comlink";
import type { ParserApi } from "./api";
const api = Comlink.wrap<ParserApi>(
  new Worker(new URL("./parser.ts", import.meta.url), { type: "module" }),
);
```

## 404: How do you handle errors that cross the worker boundary in a typed way?

Errors lose their class when cloned (custom error subclasses come back as plain `Error` or object). Send a serializable error shape with a `code` field, like `{ code: "PARSE_ERROR", message, line }`, and rebuild a proper error class on the main thread. Then callers can check `err.code` instead of `instanceof`.

## 405: Why is instanceof unreliable for objects received from a worker?

Objects from a worker are created fresh in the receiving thread from cloned data. Custom classes become plain objects, so `instanceof MyClass` is false. Built-in types like `Date`, `Map` and `Error` are recreated with the receiving thread's constructors, so `instanceof Date` works. Use explicit type fields for your own data.

## 406: What happens to object identity and circular references when posting a message?

Within one message, structured clone keeps shared references and cycles: if two properties point to the same object, they point to the same new object on the other side. Across different messages there's no identity: posting the same object twice gives two separate copies. If you need identity across messages, use IDs.

## 407: How do you keep a large state in a worker and sync only changes to the UI?

Keep the full state in the worker and send patches (like JSON Patch operations or a list of changed IDs with new values). The UI applies the patches to its own copy. Version each patch so the UI can detect gaps and ask for a full snapshot if it missed something. Immer's `produceWithPatches` is one way to create these patches.

## 408: What are the risks of putting app state in a worker?

The UI has to wait a message round trip for every state read, which can cause flicker or delays for things like text input. Debugging gets harder, and some libraries assume synchronous access. A common compromise is to keep UI state (input values, open menus) on the main thread and put only heavy data and derived calculations in the worker.

## 409: How should a text input that depends on worker results stay responsive?

Update the input value synchronously on the main thread; never wait for the worker to echo it back. Send the value to the worker for the heavy part (search, validation, formatting suggestions), and show those results when they come, ignoring stale ones. The user should never see their typing lag because of a worker round trip.

## 410: How do you handle ordering when several workers produce results for the same view?

Tag each result with the request version and the chunk index. The main thread keeps the latest version and fills chunks as they arrive, ignoring results from older versions. Render partial results if the UI allows it, or wait until all chunks for the current version are in.

## 411: How do you implement speculative work in a worker?

Start computing likely next results before the user asks, for example prefetching the next page of search results or pre-rendering zoom levels. Use low priority so it doesn't delay real requests, keep it cancellable, and cache results by key. Drop the speculation when inputs change.

## 412: How would you implement a worker-side LRU cache for expensive computations?

Keep a `Map` in the worker, since `Map` keeps insertion order. On a hit, delete and re-insert the key to mark it as recent. When the size goes over the limit, delete the first key.

```js
const cache = new Map();
const LIMIT = 500;
function cached(key, compute) {
  if (cache.has(key)) {
    const v = cache.get(key);
    cache.delete(key);
    cache.set(key, v);
    return v;
  }
  const v = compute();
  cache.set(key, v);
  if (cache.size > LIMIT) cache.delete(cache.keys().next().value);
  return v;
}
```

## 413: How do you decide between one worker and a pool for an app feature?

Use one worker when tasks depend on shared state (like an index or a database connection) or are small and sequential. Use a pool when tasks are independent and CPU-heavy, like processing many images. A mix is common: one stateful worker for data, plus a stateless pool for parallel number crunching.

## 414: How do you make a worker pool adapt to the device?

Start with a small pool and grow it when the queue gets long, up to `hardwareConcurrency - 1`. Shrink it by terminating idle workers after some time. Consider `navigator.deviceMemory` (Chromium) to use fewer workers on low-memory devices. Check timing too: if adding workers stops reducing total time, stop growing.

## 415: What is navigator.deviceMemory and how does it help with workers?

`navigator.deviceMemory` returns an approximate amount of RAM in gigabytes (for example 2, 4 or 8), and it's available in Chromium browsers, including in workers. You can use it to pick smaller pool sizes, smaller caches or lighter models on low-memory devices. It's rounded for privacy, so treat it as a rough hint.

## 416: How does the browser schedule worker threads on CPU cores?

The browser creates real OS threads for workers, and the operating system decides which core runs them and when. Browsers may set thread priorities, for example lower priority for workers of background tabs. You can't pin a worker to a core or set its priority from JavaScript.

## 417: What is priority inversion and can it happen with workers?

Priority inversion happens when a high-priority task waits on a resource held by a low-priority task, which can't run because medium-priority tasks keep the CPU busy. In browsers it can happen if the main thread waits (with `waitAsync` or a message) for a lock held by a background worker that the OS gives little CPU time. Keep critical sections short and avoid making the main thread wait on background workers.

## 418: How do scheduler priorities in the main thread interact with workers?

They don't directly. `scheduler.postTask` priorities only order tasks on the thread where you call it. Workers have their own `scheduler` object (in browsers that support it) with their own queue. A `user-blocking` task on the main thread doesn't speed up a worker. To prioritize across threads, use your own message priorities or a shared queue.

## 419: How does scheduler.yield keep priority with postTask?

When called inside a task scheduled with `postTask`, `scheduler.yield()` continues with the same priority as that task. A `background` task that yields continues as background, and a `user-blocking` task continues as user-blocking. Outside of `postTask`, it continues with `user-visible` priority but ahead of other tasks of that level.

## 420: How do you break up a long main-thread task that must run in a specific order?

Process items in a loop, yield every ~50 ms with `scheduler.yield()`, and keep the state in local variables or a closure. Order is preserved because the same async function continues after each yield. Guard against new input arriving mid-way, for example by checking a version number after each yield and stopping if it changed.

```js
async function rebuild(version, items) {
  let last = performance.now();
  for (const item of items) {
    handle(item);
    if (performance.now() - last > 50) {
      await yieldToMain();
      if (version !== currentVersion) return;
      last = performance.now();
    }
  }
}
```

## 421: What is the interaction between microtasks and yielding?

`await Promise.resolve()` doesn't yield to the browser: it only runs a microtask, and microtasks all run before the browser can render or handle input. To really yield, you must end the current task, which `setTimeout`, `MessageChannel` or `scheduler.yield()` do. A common bug is using `await null` in a loop and expecting the UI to update.

## 422: Why do some libraries use MessageChannel as a scheduler?

Posting a message to a `MessageChannel` port queues a task without the 4 ms clamping that nested `setTimeout` gets. React's scheduler, for example, uses a `MessageChannel` (when `setImmediate` isn't available) to yield back to the browser between chunks of rendering work quickly.

```js
const { port1, port2 } = new MessageChannel();
port1.onmessage = () => runNextChunk();
function scheduleNext() {
  port2.postMessage(null);
}
```

## 423: How does React's concurrent rendering relate to browser concurrency?

React's concurrent features (transitions, `useDeferredValue`, Suspense) don't use threads. They split rendering into small units on the main thread and yield to the browser between them, so urgent updates like typing can interrupt slow renders. It's cooperative scheduling, not parallelism. Heavy calculations still benefit from workers.

## 424: When is cooperative scheduling better than a worker?

When the work needs the DOM or framework state, when data transfer would cost more than the work, or when the work is moderate and can be split into small pieces. Rendering lists, updating many components and DOM-based layout calculations are examples. Workers are better when the work is pure computation on data that is cheap to send.

## 425: How would you diagnose a poor INP score in an app that already uses workers?

Look at the Long Animation Frames data or a Performance trace for slow interactions. Common causes: the main thread spends time serializing large messages to the worker, deserializing large replies, applying big DOM updates from worker results all at once, or running other scripts. Fix by reducing message size, transferring buffers, batching DOM updates per frame, and yielding in handlers.

## 426: What is the impact of structured clone on the main thread when a worker sends back large results?

Deserialization runs on the main thread before your `onmessage` handler, as part of the message task. A 50 MB result can block the main thread for a long time, even though the worker did the work. Send smaller results, transfer `ArrayBuffer`s, or let the worker keep the data and send only what the current view needs.

## 427: How do you handle a huge dataset that the UI needs to scroll through?

Keep the full dataset in a worker. The UI uses a virtualized list and asks the worker only for the rows in view (plus a small buffer), getting back small batches. Sorting, filtering and grouping happen in the worker, which returns row index ranges. The main thread holds only a few hundred rows at a time.

## 428: How do you combine IndexedDB and a worker for an offline-first app?

Do all IndexedDB reads, writes and migrations in a worker, which also handles sync with the server. The UI sends commands and receives query results. This keeps transaction work and large data conversions off the main thread. Use Web Locks or a single owner so two tabs don't run sync at the same time.

## 429: What are the concerns with opening IndexedDB in several workers and tabs?

All of them share the same database. Version upgrades block until other connections close, so each connection should listen for `versionchange` and close itself. Writes from different contexts are ordered by transactions, but your app logic still has to handle another tab changing data underneath it. `BroadcastChannel` can tell other tabs to refresh after a write.

## 430: How do OPFS sync access handles handle multiple tabs?

By default, `createSyncAccessHandle()` takes an exclusive lock on the file, so a second tab trying to open the same file gets an error. Chromium added a `mode` option (`readwrite-unsafe`, `read-only`) to allow more sharing. Apps like SQLite on OPFS usually use Web Locks or a single leader tab to manage the database file.

## 431: How would you design a real-time collaborative editor's client side with workers?

Keep the CRDT or OT document model (for example Yjs or Automerge) in a worker together with the WebSocket and the IndexedDB persistence. The main thread runs the editor UI and sends local edits as small operations. The worker merges remote and local changes and sends back only the changes for the visible part of the document. Fast local typing stays on the main thread, so the user never waits for the worker.

## 432: What are the risks of running CRDT merging on the main thread?

Merging a large batch of remote changes (like after being offline) can take hundreds of milliseconds and freeze the editor. Loading a big document's history can be even slower. Moving merging and loading to a worker keeps typing smooth. The trade-off is keeping two views of the document in sync.

## 433: How do you share a worker between the main page and an iframe on the same origin?

A same-origin iframe can reach the parent's objects, but it's cleaner to use a `MessageChannel`: the parent creates the channel, keeps one port connected to its worker logic, and passes the other port to the iframe with `iframe.contentWindow.postMessage(msg, origin, [port])`. Or use a `SharedWorker`, which both can connect to.

## 434: What is the difference between window.postMessage and worker.postMessage?

`window.postMessage(message, targetOrigin, transfer)` sends to another window or iframe and requires a target origin for safety. The receiver should check `event.origin`. `worker.postMessage(message, transfer)` sends to a worker you created, so there's no origin argument. Both use structured clone and support transfer lists.

## 435: Why should you avoid "*" as targetOrigin in window.postMessage?

With `"*"`, the message is delivered to whatever page is in that window, even if it navigated to an attacker's site. Sensitive data could leak. Always pass the exact expected origin, for example `"https://app.example.com"`, so the browser drops the message if the origin doesn't match.

## 436: How do you handle backward compatibility for browsers without module workers?

All current major browsers support module workers. If you must support older ones (like Firefox before 114), have the bundler build a classic worker bundle without `import` statements, or detect support by trying to create a module worker and catching the failure.

```js
function supportsModuleWorkers() {
  let supports = false;
  try {
    new Worker("data:,", {
      get type() {
        supports = true;
        return "module";
      },
    }).terminate();
  } catch {}
  return supports;
}
```

## 437: How do you ship a library that uses workers?

Ship the worker as a separate file referenced with `new URL("./worker.js", import.meta.url)`, which modern bundlers understand and copy into the app's build. Let users override the worker URL in config for unusual setups (CDNs, strict CSP). Avoid building workers from blob strings in libraries, since CSP often blocks them. Document COOP/COEP needs if you use shared memory.

## 438: What problems appear when a worker URL is served from a CDN on another origin?

`new Worker()` requires the same origin, so a worker file on `cdn.example.com` can't be loaded directly from `app.example.com`. Solutions: serve the worker from the app origin, use a small same-origin bootstrap worker that imports the CDN script (with CORS for modules), or use a blob bootstrap if CSP allows `blob:`.

## 439: How does Node.js-style code like Buffer or process work in workers?

It doesn't, unless your bundler polyfills it. Browser workers don't have `Buffer`, `process` or `require`. Use web equivalents: `Uint8Array` and `TextEncoder` instead of `Buffer`, and ES imports instead of `require`. Libraries that support both environments usually check `typeof process` or have a separate browser build.

## 440: How would you run the same worker code in the browser and Node.js?

Write the core logic as pure ES modules, and write two thin adapters: one using `self.onmessage` for browsers and one using `parentPort` from `worker_threads` for Node.js. Libraries like `comlink` (with its Node adapter) or `threads.js` hide these differences.

```js
// node-adapter.js
import { parentPort } from "node:worker_threads";
import { handle } from "./core.js";
parentPort.on("message", async (msg) =>
  parentPort.postMessage(await handle(msg)),
);
```

## 441: How do workers behave in Deno and Bun compared to browsers?

Deno and Bun implement the browser `Worker` API (with `type: "module"`), so code like `new Worker(new URL("./w.js", import.meta.url), { type: "module" })` works there with `self.onmessage` and `postMessage`. They add their own options, like permissions in Deno. This makes worker code more portable than Node's `worker_threads`.

## 442: What is a common mistake with new URL and import.meta.url for workers?

Putting the URL in a variable first, like `const u = new URL("./w.js", import.meta.url); new Worker(u)`, may stop some bundlers from detecting the worker, because they look for the exact pattern inside the `Worker` call. Write it inline. Also, the path must be a static string; bundlers can't follow a computed path.

## 443: How do you decide between a Web Worker and doing the work on the server?

Do it in a worker when the data is already on the client, privacy matters (data shouldn't leave the device), you want offline support, or round trips would be slow. Do it on the server when the data is huge, the work needs secrets or a database, results can be cached for many users, or client devices are too weak. Some apps do both: fast preview in a worker, final result on the server.

## 444: How would you explain a production bug where the app freezes only on some phones after adding a worker?

Likely causes: the worker sends back large results and deserialization blocks the main thread on slow CPUs; the pool is sized by `hardwareConcurrency` and too many workers run on low-memory devices, causing GC pressure or tab kills; or the main thread waits on a lock held by a worker that the OS runs on a slow core. Collect traces from a real low-end device, check memory, and limit pool size and message size.

## 445: How would you migrate an existing heavy main-thread function into a worker step by step?

First, make the function pure: its inputs and outputs should be plain data with no DOM or global state. Second, measure it and its input/output sizes. Third, move it into a worker module and call it through a promise wrapper, keeping the main-thread version as a fallback. Fourth, optimize data transfer (typed arrays, transfer). Finally, ship behind a flag and compare INP and error rates.

## 446: How do you keep a fallback path if workers fail?

Keep the core logic in a module that can run on both the main thread and in the worker. If creating the worker fails (CSP, old browser, crash loop), import the module on the main thread and run it there, maybe in chunks with yielding. The app still works, just with a busier main thread.

```js
async function getEngine() {
  try {
    return createWorkerEngine();
  } catch {
    const { engine } = await import("./engine.js");
    return engine;
  }
}
```

## 447: What questions would you ask before adding SharedArrayBuffer to a production app?

Can we set COOP and COEP on all pages that need it, including dev and staging? Will it break third-party embeds, ads, popups or OAuth flows? Is `credentialless` enough, and what about Safari? Do we really need shared memory, or would transferring buffers be fast enough? Who will maintain the concurrency code, and how will we test races?

## 448: What concurrency bugs would you look for in a code review of shared-memory code?

Look for non-atomic reads and writes on shared locations that other threads change, `Atomics.wait` called on the main thread, a wrong expected value in `wait` (lost wakeups), missing `notify` after releasing a lock, locks taken in different orders (deadlocks), data written after the index update in queues, and views created on an old buffer after memory growth.

## 449: What are the main browser concurrency tools, and when do you use each?

- **Dedicated worker**: CPU-heavy work for one page.
- **Worker pool**: many independent CPU-heavy tasks in parallel.
- **SharedWorker**: one shared instance and state for several tabs.
- **Service worker**: network proxy, caching, offline, push.
- **Worklets**: audio processing and rendering hooks.
- **OffscreenCanvas**: rendering off the main thread.
- **SharedArrayBuffer and Atomics**: shared memory and low-level sync, needs isolation.
- **BroadcastChannel and Web Locks**: cross-tab messages and coordination.
- **scheduler.yield and postTask**: splitting and prioritizing work on the main thread.

## 450: If you had to summarize best practices for browser concurrency, what would they be?

Keep the main thread for UI and input, and move heavy pure computation to workers. Create workers once and reuse them. Send small messages, use typed arrays and transfer buffers for big data. Handle errors and timeouts so promises never hang. Yield on the main thread for work that must stay there. Use shared memory only when message passing is really too slow, and then use `Atomics` correctly. Always measure on real, low-end devices before and after the change.
