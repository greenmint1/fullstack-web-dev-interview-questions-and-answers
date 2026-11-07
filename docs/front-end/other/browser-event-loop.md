# Browser Event Loop Interview Questions and Answers

_Last updated: October 28, 2026_

450 interview questions about the JavaScript event loop in the browser, with answers, split into three levels: 150 easy, 150 moderate and 150 advanced.

This file is only about the browser (the event loop described in the HTML Standard and used by Chrome, Firefox and Safari). The Node.js event loop works differently and has its own file. Newer scheduling APIs such as `scheduler.postTask()` and `scheduler.yield()` are covered too, with notes on browser support where it is still uneven.

## Table of Contents

- [Easy Questions (1-150)](#easy-questions-1-150)
- [Moderate Questions (151-300)](#moderate-questions-151-300)
- [Advanced Questions (301-450)](#advanced-questions-301-450)

### Easy Questions (1-150)

- [1: What is the event loop in the browser?](#1-what-is-the-event-loop-in-the-browser)
- [2: Why does JavaScript in the browser need an event loop?](#2-why-does-javascript-in-the-browser-need-an-event-loop)
- [3: What does it mean that JavaScript is single-threaded in the browser?](#3-what-does-it-mean-that-javascript-is-single-threaded-in-the-browser)
- [4: What is the call stack?](#4-what-is-the-call-stack)
- [5: What happens when the call stack grows too large?](#5-what-happens-when-the-call-stack-grows-too-large)
- [6: What is a task?](#6-what-is-a-task)
- [7: What is a microtask?](#7-what-is-a-microtask)
- [8: What is the difference between a task and a microtask?](#8-what-is-the-difference-between-a-task-and-a-microtask)
- [9: Which browser APIs schedule tasks?](#9-which-browser-apis-schedule-tasks)
- [10: Which browser APIs schedule microtasks?](#10-which-browser-apis-schedule-microtasks)
- [11: What is the task queue?](#11-what-is-the-task-queue)
- [12: What is the microtask queue?](#12-what-is-the-microtask-queue)
- [13: What is the output of this code and why?](#13-what-is-the-output-of-this-code-and-why)
- [14: What does setTimeout(fn, 0) actually do?](#14-what-does-settimeoutfn-0-actually-do)
- [15: Is the delay in setTimeout guaranteed?](#15-is-the-delay-in-settimeout-guaranteed)
- [16: What is setInterval?](#16-what-is-setinterval)
- [17: How do you cancel a timer?](#17-how-do-you-cancel-a-timer)
- [18: What happens if you call clearTimeout with an id that already ran or does not exist?](#18-what-happens-if-you-call-cleartimeout-with-an-id-that-already-ran-or-does-not-exist)
- [19: What are Web APIs in the context of the event loop?](#19-what-are-web-apis-in-the-context-of-the-event-loop)
- [20: Who counts down the time for setTimeout?](#20-who-counts-down-the-time-for-settimeout)
- [21: Is the event loop part of JavaScript (ECMAScript)?](#21-is-the-event-loop-part-of-javascript-ecmascript)
- [22: Where is the browser event loop specified?](#22-where-is-the-browser-event-loop-specified)
- [23: When does a Promise then callback run?](#23-when-does-a-promise-then-callback-run)
- [24: Is the function passed to new Promise synchronous?](#24-is-the-function-passed-to-new-promise-synchronous)
- [25: What does queueMicrotask do?](#25-what-does-queuemicrotask-do)
- [26: What is requestAnimationFrame?](#26-what-is-requestanimationframe)
- [27: When do requestAnimationFrame callbacks run in the event loop?](#27-when-do-requestanimationframe-callbacks-run-in-the-event-loop)
- [28: How do you cancel a requestAnimationFrame callback?](#28-how-do-you-cancel-a-requestanimationframe-callback)
- [29: What does "rendering" mean in the context of the event loop?](#29-what-does-rendering-mean-in-the-context-of-the-event-loop)
- [30: How often does the browser render a frame?](#30-how-often-does-the-browser-render-a-frame)
- [31: What is the frame budget?](#31-what-is-the-frame-budget)
- [32: What does "blocking the main thread" mean?](#32-what-does-blocking-the-main-thread-mean)
- [33: What happens to the page when a long synchronous loop runs?](#33-what-happens-to-the-page-when-a-long-synchronous-loop-runs)
- [34: What is a long task?](#34-what-is-a-long-task)
- [35: What is the main thread?](#35-what-is-the-main-thread)
- [36: What kind of work runs on the main thread?](#36-what-kind-of-work-runs-on-the-main-thread)
- [37: What work runs off the main thread?](#37-what-work-runs-off-the-main-thread)
- [38: What is a Web Worker?](#38-what-is-a-web-worker)
- [39: Does a Web Worker share the event loop with the page?](#39-does-a-web-worker-share-the-event-loop-with-the-page)
- [40: How does the page communicate with a worker?](#40-how-does-the-page-communicate-with-a-worker)
- [41: How do async and await relate to the event loop?](#41-how-do-async-and-await-relate-to-the-event-loop)
- [42: What exactly happens at an await?](#42-what-exactly-happens-at-an-await)
- [43: Does code inside an async function before the first await run synchronously?](#43-does-code-inside-an-async-function-before-the-first-await-run-synchronously)
- [44: What does an async function return?](#44-what-does-an-async-function-return)
- [45: Does using async make code run in parallel?](#45-does-using-async-make-code-run-in-parallel)
- [46: What is a callback in the context of the event loop?](#46-what-is-a-callback-in-the-context-of-the-event-loop)
- [47: When does an event listener run?](#47-when-does-an-event-listener-run)
- [48: What happens when the user clicks while JavaScript is running?](#48-what-happens-when-the-user-clicks-while-javascript-is-running)
- [49: Is dispatchEvent synchronous or asynchronous?](#49-is-dispatchevent-synchronous-or-asynchronous)
- [50: Does event bubbling happen across several tasks?](#50-does-event-bubbling-happen-across-several-tasks)
- [51: When do fetch callbacks run?](#51-when-do-fetch-callbacks-run)
- [52: Does fetch block the main thread?](#52-does-fetch-block-the-main-thread)
- [53: What is a synchronous XMLHttpRequest and why should you avoid it?](#53-what-is-a-synchronous-xmlhttprequest-and-why-should-you-avoid-it)
- [54: What do alert, confirm and prompt do to the event loop?](#54-what-do-alert-confirm-and-prompt-do-to-the-event-loop)
- [55: What is "run to completion"?](#55-what-is-run-to-completion)
- [56: Can a click handler interrupt a function that is already running?](#56-can-a-click-handler-interrupt-a-function-that-is-already-running)
- [57: What is the difference between concurrency and parallelism in browser JavaScript?](#57-what-is-the-difference-between-concurrency-and-parallelism-in-browser-javascript)
- [58: What is one "turn" or "tick" of the event loop?](#58-what-is-one-turn-or-tick-of-the-event-loop)
- [59: Do all pending microtasks run between two tasks?](#59-do-all-pending-microtasks-run-between-two-tasks)
- [60: Can a microtask schedule more microtasks?](#60-can-a-microtask-schedule-more-microtasks)
- [61: What is MutationObserver and when does its callback run?](#61-what-is-mutationobserver-and-when-does-its-callback-run)
- [62: What is the "callback queue"?](#62-what-is-the-callback-queue)
- [63: Is "macrotask" an official term?](#63-is-macrotask-an-official-term)
- [64: If two setTimeout calls have the same delay, which runs first?](#64-if-two-settimeout-calls-have-the-same-delay-which-runs-first)
- [65: What is the output when timers have different delays?](#65-what-is-the-output-when-timers-have-different-delays)
- [66: Is a then callback on an already resolved promise still asynchronous?](#66-is-a-then-callback-on-an-already-resolved-promise-still-asynchronous)
- [67: What is printed here?](#67-what-is-printed-here)
- [68: How does Promise.all work in terms of the event loop?](#68-how-does-promiseall-work-in-terms-of-the-event-loop)
- [69: What is an unhandled promise rejection?](#69-what-is-an-unhandled-promise-rejection)
- [70: Why does try/catch around setTimeout not catch an error thrown inside the callback?](#70-why-does-trycatch-around-settimeout-not-catch-an-error-thrown-inside-the-callback)
- [71: Why does try/catch not catch a rejected promise unless you await it?](#71-why-does-trycatch-not-catch-a-rejected-promise-unless-you-await-it)
- [72: What is the window error event?](#72-what-is-the-window-error-event)
- [73: Does an uncaught error in one task stop the event loop?](#73-does-an-uncaught-error-in-one-task-stop-the-event-loop)
- [74: Why does a for loop with var and setTimeout print the same number?](#74-why-does-a-for-loop-with-var-and-settimeout-print-the-same-number)
- [75: How do you write a sleep or delay function?](#75-how-do-you-write-a-sleep-or-delay-function)
- [76: What is the minimum delay of setTimeout?](#76-what-is-the-minimum-delay-of-settimeout)
- [77: What happens to timers in a background tab?](#77-what-happens-to-timers-in-a-background-tab)
- [78: Why does requestAnimationFrame stop in background tabs?](#78-why-does-requestanimationframe-stop-in-background-tabs)
- [79: What is requestIdleCallback?](#79-what-is-requestidlecallback)
- [80: What does deadline.timeRemaining() return in requestIdleCallback?](#80-what-does-deadlinetimeremaining-return-in-requestidlecallback)
- [81: What is scheduler.postTask?](#81-what-is-schedulerposttask)
- [82: What is scheduler.yield?](#82-what-is-scheduleryield)
- [83: What does "yielding to the main thread" mean?](#83-what-does-yielding-to-the-main-thread-mean)
- [84: Why should you break up long tasks?](#84-why-should-you-break-up-long-tasks)
- [85: How can you split a long loop into chunks with setTimeout?](#85-how-can-you-split-a-long-loop-into-chunks-with-settimeout)
- [86: What is INP and how does it relate to the event loop?](#86-what-is-inp-and-how-does-it-relate-to-the-event-loop)
- [87: Why is requestAnimationFrame better than setTimeout for animations?](#87-why-is-requestanimationframe-better-than-settimeout-for-animations)
- [88: What is jank?](#88-what-is-jank)
- [89: Can CSS animations keep running when the main thread is blocked?](#89-can-css-animations-keep-running-when-the-main-thread-is-blocked)
- [90: What is the compositor thread?](#90-what-is-the-compositor-thread)
- [91: How do DOMContentLoaded and load relate to the event loop?](#91-how-do-domcontentloaded-and-load-relate-to-the-event-loop)
- [92: When do classic script tags run?](#92-when-do-classic-script-tags-run)
- [93: What is the difference between async and defer scripts in terms of when they run?](#93-what-is-the-difference-between-async-and-defer-scripts-in-terms-of-when-they-run)
- [94: Do module scripts behave like defer scripts?](#94-do-module-scripts-behave-like-defer-scripts)
- [95: Is there one event loop per tab?](#95-is-there-one-event-loop-per-tab)
- [96: Do iframes share the event loop with the parent page?](#96-do-iframes-share-the-event-loop-with-the-parent-page)
- [97: What is window.postMessage and how is the message delivered?](#97-what-is-windowpostmessage-and-how-is-the-message-delivered)
- [98: What is MessageChannel?](#98-what-is-messagechannel)
- [99: Does setImmediate exist in browsers?](#99-does-setimmediate-exist-in-browsers)
- [100: Does process.nextTick exist in the browser?](#100-does-processnexttick-exist-in-the-browser)
- [101: What is the main difference between the browser event loop and the Node.js event loop?](#101-what-is-the-main-difference-between-the-browser-event-loop-and-the-nodejs-event-loop)
- [102: How can you see tasks and the main thread in Chrome DevTools?](#102-how-can-you-see-tasks-and-the-main-thread-in-chrome-devtools)
- [103: Is console.log asynchronous?](#103-is-consolelog-asynchronous)
- [104: What is the difference between synchronous and asynchronous code?](#104-what-is-the-difference-between-synchronous-and-asynchronous-code)
- [105: What does non-blocking I/O mean in the browser?](#105-what-does-non-blocking-io-mean-in-the-browser)
- [106: Can setTimeout take a string instead of a function?](#106-can-settimeout-take-a-string-instead-of-a-function)
- [107: How do you pass arguments to a setTimeout callback?](#107-how-do-you-pass-arguments-to-a-settimeout-callback)
- [108: What is this inside a setTimeout callback?](#108-what-is-this-inside-a-settimeout-callback)
- [109: What happens if you pass a negative number or NaN as the delay?](#109-what-happens-if-you-pass-a-negative-number-or-nan-as-the-delay)
- [110: What is the maximum delay for setTimeout?](#110-what-is-the-maximum-delay-for-settimeout)
- [111: What is the output of this code?](#111-what-is-the-output-of-this-code)
- [112: What happens when you await a value that is not a promise?](#112-what-happens-when-you-await-a-value-that-is-not-a-promise)
- [113: What are jobs in ECMAScript?](#113-what-are-jobs-in-ecmascript)
- [114: What is printed by this code?](#114-what-is-printed-by-this-code)
- [115: What is a task source?](#115-what-is-a-task-source)
- [116: Is there only one task queue?](#116-is-there-only-one-task-queue)
- [117: What is the "update the rendering" step?](#117-what-is-the-update-the-rendering-step)
- [118: Does the browser render after every task?](#118-does-the-browser-render-after-every-task)
- [119: Does a DOM change appear on screen right away?](#119-does-a-dom-change-appear-on-screen-right-away)
- [120: Why does changing a style twice in the same task only show the last value?](#120-why-does-changing-a-style-twice-in-the-same-task-only-show-the-last-value)
- [121: What is layout (reflow)?](#121-what-is-layout-reflow)
- [122: What is a forced synchronous layout?](#122-what-is-a-forced-synchronous-layout)
- [123: Which DOM properties and methods force layout when you read them?](#123-which-dom-properties-and-methods-force-layout-when-you-read-them)
- [124: How often does the scroll event fire?](#124-how-often-does-the-scroll-event-fire)
- [125: What is debouncing?](#125-what-is-debouncing)
- [126: What is throttling?](#126-what-is-throttling)
- [127: What is ResizeObserver and when does its callback run?](#127-what-is-resizeobserver-and-when-does-its-callback-run)
- [128: When does an IntersectionObserver callback run?](#128-when-does-an-intersectionobserver-callback-run)
- [129: What is the visibilitychange event?](#129-what-is-the-visibilitychange-event)
- [130: What happens to timers when a page goes into the back/forward cache?](#130-what-happens-to-timers-when-a-page-goes-into-the-backforward-cache)
- [131: Is the abort event of AbortController synchronous?](#131-is-the-abort-event-of-abortcontroller-synchronous)
- [132: What is a passive event listener and how does it help?](#132-what-is-a-passive-event-listener-and-how-does-it-help)
- [133: Does the browser give user input priority over other tasks?](#133-does-the-browser-give-user-input-priority-over-other-tasks)
- [134: What happens if a microtask throws an error?](#134-what-happens-if-a-microtask-throws-an-error)
- [135: When does a finally callback run?](#135-when-does-a-finally-callback-run)
- [136: What is the argument passed to a requestAnimationFrame callback?](#136-what-is-the-argument-passed-to-a-requestanimationframe-callback)
- [137: Can you stop the event loop from JavaScript?](#137-can-you-stop-the-event-loop-from-javascript)
- [138: What does the "Page Unresponsive" dialog mean?](#138-what-does-the-page-unresponsive-dialog-mean)
- [139: What is a dropped frame?](#139-what-is-a-dropped-frame)
- [140: Is JSON.parse blocking?](#140-is-jsonparse-blocking)
- [141: Is postMessage free?](#141-is-postmessage-free)
- [142: How do frameworks like Vue use microtasks?](#142-how-do-frameworks-like-vue-use-microtasks)
- [143: How are steps in a promise chain scheduled?](#143-how-are-steps-in-a-promise-chain-scheduled)
- [144: If several then callbacks are attached to the same promise, in what order do they run?](#144-if-several-then-callbacks-are-attached-to-the-same-promise-in-what-order-do-they-run)
- [145: In what order do event listeners on the same element run?](#145-in-what-order-do-event-listeners-on-the-same-element-run)
- [146: What does the once option of addEventListener do?](#146-what-does-the-once-option-of-addeventlistener-do)
- [147: How do you repeat code with setTimeout instead of setInterval?](#147-how-do-you-repeat-code-with-settimeout-instead-of-setinterval)
- [148: Does a Service Worker run on the main thread?](#148-does-a-service-worker-run-on-the-main-thread)
- [149: Is localStorage synchronous?](#149-is-localstorage-synchronous)
- [150: What are common beginner mistakes about the event loop?](#150-what-are-common-beginner-mistakes-about-the-event-loop)

### Moderate Questions (151-300)

- [151: What is the output of this code?](#151-what-is-the-output-of-this-code)
- [152: What is printed when promises and timers are nested?](#152-what-is-printed-when-promises-and-timers-are-nested)
- [153: What is the output when an async function awaits another async function?](#153-what-is-the-output-when-an-async-function-awaits-another-async-function)
- [154: Can you predict the order between rAF and setTimeout?](#154-can-you-predict-the-order-between-raf-and-settimeout)
- [155: How many microtask hops does await take?](#155-how-many-microtask-hops-does-await-take)
- [156: Why does return await sometimes run sooner than return in an async function?](#156-why-does-return-await-sometimes-run-sooner-than-return-in-an-async-function)
- [157: What is the difference between Promise.resolve(p) and wrapping p in a new Promise?](#157-what-is-the-difference-between-promiseresolvep-and-wrapping-p-in-a-new-promise)
- [158: How do two independent promise chains interleave?](#158-how-do-two-independent-promise-chains-interleave)
- [159: What is microtask starvation?](#159-what-is-microtask-starvation)
- [160: Why does a recursive setTimeout not freeze the page, but a recursive microtask does?](#160-why-does-a-recursive-settimeout-not-freeze-the-page-but-a-recursive-microtask-does)
- [161: What are the problems with setInterval?](#161-what-are-the-problems-with-setinterval)
- [162: How do you build a countdown timer that stays accurate?](#162-how-do-you-build-a-countdown-timer-that-stays-accurate)
- [163: What is the difference between performance.now() and Date.now()?](#163-what-is-the-difference-between-performancenow-and-datenow)
- [164: How do you yield to the main thread with scheduler.yield and a fallback?](#164-how-do-you-yield-to-the-main-thread-with-scheduleryield-and-a-fallback)
- [165: What priorities does scheduler.postTask support?](#165-what-priorities-does-schedulerposttask-support)
- [166: How do you cancel or change the priority of posted tasks?](#166-how-do-you-cancel-or-change-the-priority-of-posted-tasks)
- [167: What does the timeout option of requestIdleCallback do?](#167-what-does-the-timeout-option-of-requestidlecallback-do)
- [168: What should you avoid doing inside requestIdleCallback?](#168-what-should-you-avoid-doing-inside-requestidlecallback)
- [169: How do you batch DOM reads and writes?](#169-how-do-you-batch-dom-reads-and-writes)
- [170: What is layout thrashing and how do you find it?](#170-what-is-layout-thrashing-and-how-do-you-find-it)
- [171: What is the double requestAnimationFrame trick?](#171-what-is-the-double-requestanimationframe-trick)
- [172: How do you run code right after the browser paints a frame?](#172-how-do-you-run-code-right-after-the-browser-paints-a-frame)
- [173: Why do some libraries use MessageChannel instead of setTimeout(fn, 0)?](#173-why-do-some-libraries-use-messagechannel-instead-of-settimeoutfn-0)
- [174: How does React's scheduler use the event loop?](#174-how-does-reacts-scheduler-use-the-event-loop)
- [175: How did Angular use Zone.js to know when to update, and what changed?](#175-how-did-angular-use-zonejs-to-know-when-to-update-and-what-changed)
- [176: How do you write a debounce that can be cancelled and flushed?](#176-how-do-you-write-a-debounce-that-can-be-cancelled-and-flushed)
- [177: How do you throttle with requestAnimationFrame?](#177-how-do-you-throttle-with-requestanimationframe)
- [178: What happens if you call preventDefault in a passive listener?](#178-what-happens-if-you-call-preventdefault-in-a-passive-listener)
- [179: Why doesn't preventDefault work after an await?](#179-why-doesnt-preventdefault-work-after-an-await)
- [180: What is user activation and how can await break it?](#180-what-is-user-activation-and-how-can-await-break-it)
- [181: Do microtasks run between event listeners?](#181-do-microtasks-run-between-event-listeners)
- [182: What is printed when dispatching a custom event between promises?](#182-what-is-printed-when-dispatching-a-custom-event-between-promises)
- [183: How do you use custom events to decouple parts of an app, and what should you watch out for?](#183-how-do-you-use-custom-events-to-decouple-parts-of-an-app-and-what-should-you-watch-out-for)
- [184: When is the unhandledrejection event fired?](#184-when-is-the-unhandledrejection-event-fired)
- [185: What is reportError?](#185-what-is-reporterror)
- [186: What are async stack traces in DevTools?](#186-what-are-async-stack-traces-in-devtools)
- [187: How do you detect long tasks in production?](#187-how-do-you-detect-long-tasks-in-production)
- [188: What is the Long Animation Frames (LoAF) API?](#188-what-is-the-long-animation-frames-loaf-api)
- [189: How do you measure interaction latency in code?](#189-how-do-you-measure-interaction-latency-in-code)
- [190: How do you process a big array without blocking, using a time budget?](#190-how-do-you-process-a-big-array-without-blocking-using-a-time-budget)
- [191: What is navigator.scheduling.isInputPending?](#191-what-is-navigatorschedulingisinputpending)
- [192: How do you move heavy work to a Web Worker with a promise-based API?](#192-how-do-you-move-heavy-work-to-a-web-worker-with-a-promise-based-api)
- [193: What are transferable objects?](#193-what-are-transferable-objects)
- [194: How does a worker's event loop differ from a window's event loop?](#194-how-does-a-workers-event-loop-differ-from-a-windows-event-loop)
- [195: When is a Web Worker not worth it?](#195-when-is-a-web-worker-not-worth-it)
- [196: How does a Service Worker's event loop and lifetime affect your code?](#196-how-does-a-service-workers-event-loop-and-lifetime-affect-your-code)
- [197: How exactly are timers throttled in background tabs?](#197-how-exactly-are-timers-throttled-in-background-tabs)
- [198: How can you keep work going when the tab is in the background?](#198-how-can-you-keep-work-going-when-the-tab-is-in-the-background)
- [199: What is the Page Lifecycle API (freeze and resume)?](#199-what-is-the-page-lifecycle-api-freeze-and-resume)
- [200: How does reading a fetch response body work with the event loop?](#200-how-does-reading-a-fetch-response-body-work-with-the-event-loop)
- [201: When does fetch reject after you call abort()?](#201-when-does-fetch-reject-after-you-call-abort)
- [202: How do you add a timeout to a promise without leaking timers?](#202-how-do-you-add-a-timeout-to-a-promise-without-leaking-timers)
- [203: How do Promise.all, allSettled, any and race differ, and do they change the timing?](#203-how-do-promiseall-allsettled-any-and-race-differ-and-do-they-change-the-timing)
- [204: How does for await...of work with the event loop?](#204-how-does-for-awaitof-work-with-the-event-loop)
- [205: What is the difference between awaiting in sequence and in parallel?](#205-what-is-the-difference-between-awaiting-in-sequence-and-in-parallel)
- [206: Why does forEach with an async callback not wait?](#206-why-does-foreach-with-an-async-callback-not-wait)
- [207: How do you limit how many async operations run at once?](#207-how-do-you-limit-how-many-async-operations-run-at-once)
- [208: Why doesn't a loading spinner appear during heavy synchronous work?](#208-why-doesnt-a-loading-spinner-appear-during-heavy-synchronous-work)
- [209: How do you update a progress bar during a long loop?](#209-how-do-you-update-a-progress-bar-during-a-long-loop)
- [210: How do you make an animation run at the same speed on 60 Hz and 120 Hz screens?](#210-how-do-you-make-an-animation-run-at-the-same-speed-on-60-hz-and-120-hz-screens)
- [211: Why doesn't a CSS transition run when you add an element and its class in the same task?](#211-why-doesnt-a-css-transition-run-when-you-add-an-element-and-its-class-in-the-same-task)
- [212: What is @starting-style and how does it help with entry transitions?](#212-what-is-starting-style-and-how-does-it-help-with-entry-transitions)
- [213: Does the Web Animations API run on the main thread?](#213-does-the-web-animations-api-run-on-the-main-thread)
- [214: What are scroll-driven animations and why are they better than scroll listeners?](#214-what-are-scroll-driven-animations-and-why-are-they-better-than-scroll-listeners)
- [215: What does the "ResizeObserver loop completed with undelivered notifications" error mean?](#215-what-does-the-resizeobserver-loop-completed-with-undelivered-notifications-error-mean)
- [216: Why use IntersectionObserver instead of a scroll handler for lazy loading?](#216-why-use-intersectionobserver-instead-of-a-scroll-handler-for-lazy-loading)
- [217: How does MutationObserver batch changes?](#217-how-does-mutationobserver-batch-changes)
- [218: How can a MutationObserver cause an infinite loop?](#218-how-can-a-mutationobserver-cause-an-infinite-loop)
- [219: How do fake timers work in tests?](#219-how-do-fake-timers-work-in-tests)
- [220: Why do tests with fake timers sometimes hang or miss promise callbacks?](#220-why-do-tests-with-fake-timers-sometimes-hang-or-miss-promise-callbacks)
- [221: How do you flush pending promises in a test?](#221-how-do-you-flush-pending-promises-in-a-test)
- [222: How do you test code that uses requestAnimationFrame?](#222-how-do-you-test-code-that-uses-requestanimationframe)
- [223: How do you find out which part of a task is slow in the Performance panel?](#223-how-do-you-find-out-which-part-of-a-task-is-slow-in-the-performance-panel)
- [224: What do Recalculate Style, Layout, Paint and Composite mean in a performance recording?](#224-what-do-recalculate-style-layout-paint-and-composite-mean-in-a-performance-recording)
- [225: How do you use performance.mark and performance.measure?](#225-how-do-you-use-performancemark-and-performancemeasure)
- [226: Why do frameworks batch state updates in a microtask?](#226-why-do-frameworks-batch-state-updates-in-a-microtask)
- [227: How does React batch updates?](#227-how-does-react-batch-updates)
- [228: Do microtasks run after each requestAnimationFrame callback?](#228-do-microtasks-run-after-each-requestanimationframe-callback)
- [229: What happens if you call requestAnimationFrame inside a requestAnimationFrame callback?](#229-what-happens-if-you-call-requestanimationframe-inside-a-requestanimationframe-callback)
- [230: What is the difference between setTimeout inside rAF and rAF inside setTimeout?](#230-what-is-the-difference-between-settimeout-inside-raf-and-raf-inside-settimeout)
- [231: Why do browsers align or coalesce timers?](#231-why-do-browsers-align-or-coalesce-timers)
- [232: How can a long inline script delay the first paint?](#232-how-can-a-long-inline-script-delay-the-first-paint)
- [233: Why are JavaScript parsing and compiling a main thread concern?](#233-why-are-javascript-parsing-and-compiling-a-main-thread-concern)
- [234: How do you handle a huge JSON response without freezing the page?](#234-how-do-you-handle-a-huge-json-response-without-freezing-the-page)
- [235: How do you add a lot of DOM nodes without hurting performance?](#235-how-do-you-add-a-lot-of-dom-nodes-without-hurting-performance)
- [236: What is list virtualization and why does it help the main thread?](#236-what-is-list-virtualization-and-why-does-it-help-the-main-thread)
- [237: What does content-visibility: auto do?](#237-what-does-content-visibility-auto-do)
- [238: How does event delegation affect main thread work?](#238-how-does-event-delegation-affect-main-thread-work)
- [239: How do you separate urgent and non-urgent work in an input handler?](#239-how-do-you-separate-urgent-and-non-urgent-work-in-an-input-handler)
- [240: How do you schedule non-critical work after an interaction?](#240-how-do-you-schedule-non-critical-work-after-an-interaction)
- [241: What is the "idle until urgent" pattern?](#241-what-is-the-idle-until-urgent-pattern)
- [242: What is lazy or partial hydration and how does it help the event loop?](#242-what-is-lazy-or-partial-hydration-and-how-does-it-help-the-event-loop)
- [243: How do third-party scripts affect the event loop and how do you limit the damage?](#243-how-do-third-party-scripts-affect-the-event-loop-and-how-do-you-limit-the-damage)
- [244: What is the difference between the delay option of postTask and setTimeout?](#244-what-is-the-difference-between-the-delay-option-of-posttask-and-settimeout)
- [245: What priority does the continuation after scheduler.yield get?](#245-what-priority-does-the-continuation-after-scheduleryield-get)
- [246: How do you write a cancellable delay?](#246-how-do-you-write-a-cancellable-delay)
- [247: How are WebSocket messages delivered and what happens if they arrive very fast?](#247-how-are-websocket-messages-delivered-and-what-happens-if-they-arrive-very-fast)
- [248: How do you handle high-frequency updates without overloading the main thread?](#248-how-do-you-handle-high-frequency-updates-without-overloading-the-main-thread)
- [249: How are BroadcastChannel and storage events delivered?](#249-how-are-broadcastchannel-and-storage-events-delivered)
- [250: Why does an IndexedDB transaction fail after awaiting a fetch?](#250-why-does-an-indexeddb-transaction-fail-after-awaiting-a-fetch)
- [251: Can you use Atomics.wait on the main thread?](#251-can-you-use-atomicswait-on-the-main-thread)
- [252: What do you need to use SharedArrayBuffer in the browser?](#252-what-do-you-need-to-use-sharedarraybuffer-in-the-browser)
- [253: What is OffscreenCanvas and how does it help the main thread?](#253-what-is-offscreencanvas-and-how-does-it-help-the-main-thread)
- [254: Does WebAssembly run off the main thread?](#254-does-webassembly-run-off-the-main-thread)
- [255: What does img.decode() do?](#255-what-does-imgdecode-do)
- [256: What is createImageBitmap used for?](#256-what-is-createimagebitmap-used-for)
- [257: How do you wait for fonts before measuring text?](#257-how-do-you-wait-for-fonts-before-measuring-text)
- [258: What is requestVideoFrameCallback?](#258-what-is-requestvideoframecallback)
- [259: Are focus and blur events fired synchronously?](#259-are-focus-and-blur-events-fired-synchronously)
- [260: Which DOM operations fire events synchronously?](#260-which-dom-operations-fire-events-synchronously)
- [261: How can you use generators to split work into chunks?](#261-how-can-you-use-generators-to-split-work-into-chunks)
- [262: How do you avoid showing stale results when requests finish out of order?](#262-how-do-you-avoid-showing-stale-results-when-requests-finish-out-of-order)
- [263: Why might your DOM not be updated right after setting state in a framework?](#263-why-might-your-dom-not-be-updated-right-after-setting-state-in-a-framework)
- [264: How do you debug a slow interaction (poor INP)?](#264-how-do-you-debug-a-slow-interaction-poor-inp)
- [265: Why can a page sometimes scroll smoothly while JavaScript is blocking the main thread?](#265-why-can-a-page-sometimes-scroll-smoothly-while-javascript-is-blocking-the-main-thread)
- [266: How do non-passive wheel or touch listeners slow down scrolling?](#266-how-do-non-passive-wheel-or-touch-listeners-slow-down-scrolling)
- [267: What does will-change do?](#267-what-does-will-change-do)
- [268: How do you reduce the input delay part of INP?](#268-how-do-you-reduce-the-input-delay-part-of-inp)
- [269: How do you reduce the processing time part of INP?](#269-how-do-you-reduce-the-processing-time-part-of-inp)
- [270: How do you reduce the presentation delay part of INP?](#270-how-do-you-reduce-the-presentation-delay-part-of-inp)
- [271: Which page lifecycle events should you use when the user leaves the page?](#271-which-page-lifecycle-events-should-you-use-when-the-user-leaves-the-page)
- [272: How do you send data reliably when the page is closing?](#272-how-do-you-send-data-reliably-when-the-page-is-closing)
- [273: What happens to timers and pending promises when the user navigates away?](#273-what-happens-to-timers-and-pending-promises-when-the-user-navigates-away)
- [274: How do timers and listeners cause memory leaks?](#274-how-do-timers-and-listeners-cause-memory-leaks)
- [275: How do you clean up timers and async work in a React effect?](#275-how-do-you-clean-up-timers-and-async-work-in-a-react-effect)
- [276: How do you poll a server with exponential backoff?](#276-how-do-you-poll-a-server-with-exponential-backoff)
- [277: How do you choose between a microtask, a task, requestAnimationFrame and an idle callback?](#277-how-do-you-choose-between-a-microtask-a-task-requestanimationframe-and-an-idle-callback)
- [278: Is it true that setTimeout(fn, 0) runs fn right after the current function?](#278-is-it-true-that-settimeoutfn-0-runs-fn-right-after-the-current-function)
- [279: How do RxJS schedulers map to the browser event loop?](#279-how-do-rxjs-schedulers-map-to-the-browser-event-loop)
- [280: How do you wait for a web component to finish rendering?](#280-how-do-you-wait-for-a-web-component-to-finish-rendering)
- [281: When do useLayoutEffect and useEffect run compared to the browser paint?](#281-when-do-uselayouteffect-and-useeffect-run-compared-to-the-browser-paint)
- [282: When do custom element lifecycle callbacks run?](#282-when-do-custom-element-lifecycle-callbacks-run)
- [283: How do you run code after an inserted element has been rendered?](#283-how-do-you-run-code-after-an-inserted-element-has-been-rendered)
- [284: When should you use queueMicrotask instead of setTimeout?](#284-when-should-you-use-queuemicrotask-instead-of-settimeout)
- [285: Why do you get fewer mousemove events when the page is busy?](#285-why-do-you-get-fewer-mousemove-events-when-the-page-is-busy)
- [286: How do you measure the frame rate in JavaScript?](#286-how-do-you-measure-the-frame-rate-in-javascript)
- [287: What is Promise.withResolvers and when is it useful?](#287-what-is-promisewithresolvers-and-when-is-it-useful)
- [288: How do you combine a timeout with user cancellation?](#288-how-do-you-combine-a-timeout-with-user-cancellation)
- [289: Does await inside a loop let the browser render?](#289-does-await-inside-a-loop-let-the-browser-render)
- [290: What happens if an event listener is an async function?](#290-what-happens-if-an-event-listener-is-an-async-function)
- [291: How do you run low-priority work with a fallback when requestIdleCallback is missing?](#291-how-do-you-run-low-priority-work-with-a-fallback-when-requestidlecallback-is-missing)
- [292: Should you batch DOM updates in a microtask or in requestAnimationFrame?](#292-should-you-batch-dom-updates-in-a-microtask-or-in-requestanimationframe)
- [293: Is it expensive to create many small timers?](#293-is-it-expensive-to-create-many-small-timers)
- [294: What is the Web Locks API and how does it relate to async code?](#294-what-is-the-web-locks-api-and-how-does-it-relate-to-async-code)
- [295: Does requestAnimationFrame keep running for elements that are off-screen?](#295-does-requestanimationframe-keep-running-for-elements-that-are-off-screen)
- [296: In what order do rAF, ResizeObserver and IntersectionObserver callbacks run in a frame?](#296-in-what-order-do-raf-resizeobserver-and-intersectionobserver-callbacks-run-in-a-frame)
- [297: How should you think about ordering between different async APIs?](#297-how-should-you-think-about-ordering-between-different-async-apis)
- [298: Why is it a bad idea to measure performance with setTimeout callbacks?](#298-why-is-it-a-bad-idea-to-measure-performance-with-settimeout-callbacks)
- [299: What does an event loop iteration look like in a typical click scenario?](#299-what-does-an-event-loop-iteration-look-like-in-a-typical-click-scenario)
- [300: What are some common wrong statements about the browser event loop?](#300-what-are-some-common-wrong-statements-about-the-browser-event-loop)

### Advanced Questions (301-450)

- [301: Walk through the event loop processing model as the HTML spec describes it.](#301-walk-through-the-event-loop-processing-model-as-the-html-spec-describes-it)
- [302: The spec says task queues are "sets", not queues. Why does that matter?](#302-the-spec-says-task-queues-are-sets-not-queues-why-does-that-matter)
- [303: How does Chrome decide which task to run next?](#303-how-does-chrome-decide-which-task-to-run-next)
- [304: What exactly happens during a microtask checkpoint?](#304-what-exactly-happens-during-a-microtask-checkpoint)
- [305: When exactly does a microtask checkpoint happen besides "after each task"?](#305-when-exactly-does-a-microtask-checkpoint-happen-besides-after-each-task)
- [306: List the steps of "update the rendering" in order.](#306-list-the-steps-of-update-the-rendering-in-order)
- [307: What is a "rendering opportunity" and when can the browser skip rendering?](#307-what-is-a-rendering-opportunity-and-when-can-the-browser-skip-rendering)
- [308: Why are scroll and resize events tied to frames?](#308-why-are-scroll-and-resize-events-tied-to-frames)
- [309: When are transitionend and animationend events fired?](#309-when-are-transitionend-and-animationend-events-fired)
- [310: How does the ResizeObserver loop algorithm prevent infinite loops?](#310-how-does-the-resizeobserver-loop-algorithm-prevent-infinite-loops)
- [311: Why are IntersectionObserver callbacks tasks while ResizeObserver callbacks run inside rendering?](#311-why-are-intersectionobserver-callbacks-tasks-while-resizeobserver-callbacks-run-inside-rendering)
- [312: What timestamp do rAF callbacks get, and why do all callbacks in a frame get the same one?](#312-what-timestamp-do-raf-callbacks-get-and-why-do-all-callbacks-in-a-frame-get-the-same-one)
- [313: How does the browser decide the idle deadline for requestIdleCallback?](#313-how-does-the-browser-decide-the-idle-deadline-for-requestidlecallback)
- [314: What types of event loops exist in the browser?](#314-what-types-of-event-loops-exist-in-the-browser)
- [315: What is an agent and an agent cluster, and how do they relate to event loops?](#315-what-is-an-agent-and-an-agent-cluster-and-how-do-they-relate-to-event-loops)
- [316: How does site isolation change which pages share an event loop?](#316-how-does-site-isolation-change-which-pages-share-an-event-loop)
- [317: How does the browser connect ECMAScript jobs to the HTML microtask queue?](#317-how-does-the-browser-connect-ecmascript-jobs-to-the-html-microtask-queue)
- [318: Do promise callbacks for a removed iframe still run?](#318-do-promise-callbacks-for-a-removed-iframe-still-run)
- [319: Why does resolving a promise with another promise take extra ticks?](#319-why-does-resolving-a-promise-with-another-promise-take-extra-ticks)
- [320: How did the await optimization change the number of ticks?](#320-how-did-the-await-optimization-change-the-number-of-ticks)
- [321: What does this print?](#321-what-does-this-print)
- [322: How many ticks does an async generator need per value?](#322-how-many-ticks-does-an-async-generator-need-per-value)
- [323: How is the microtask queue implemented in V8 and Blink?](#323-how-is-the-microtask-queue-implemented-in-v8-and-blink)
- [324: How does a frame get produced in Chrome, from vsync to pixels?](#324-how-does-a-frame-get-produced-in-chrome-from-vsync-to-pixels)
- [325: What is rAF-aligned input in Chromium?](#325-what-is-raf-aligned-input-in-chromium)
- [326: What are getCoalescedEvents and getPredictedEvents?](#326-what-are-getcoalescedevents-and-getpredictedevents)
- [327: How is the Long Tasks API different from LoAF?](#327-how-is-the-long-tasks-api-different-from-loaf)
- [328: What information does a LoAF script entry give you?](#328-what-information-does-a-loaf-script-entry-give-you)
- [329: How exactly does yielding improve INP?](#329-how-exactly-does-yielding-improve-inp)
- [330: Should you yield before or after updating the DOM in an event handler?](#330-should-you-yield-before-or-after-updating-the-dom-in-an-event-handler)
- [331: Why can setTimeout-based yielding perform worse than scheduler.yield in practice?](#331-why-can-settimeout-based-yielding-perform-worse-than-scheduleryield-in-practice)
- [332: How would you build a small cooperative scheduler like React's?](#332-how-would-you-build-a-small-cooperative-scheduler-like-reacts)
- [333: What is starvation in a priority scheduler and how do you prevent it?](#333-what-is-starvation-in-a-priority-scheduler-and-how-do-you-prevent-it)
- [334: How would you keep a large data grid responsive while sorting 1 million rows?](#334-how-would-you-keep-a-large-data-grid-responsive-while-sorting-1-million-rows)
- [335: What does the spec say about timer clamping and ordering?](#335-what-does-the-spec-say-about-timer-clamping-and-ordering)
- [336: Why are browser timers less precise than they could be?](#336-why-are-browser-timers-less-precise-than-they-could-be)
- [337: How does Chrome's intensive timer throttling decide what to throttle?](#337-how-does-chromes-intensive-timer-throttling-decide-what-to-throttle)
- [338: Why might a timer in a background tab fire later than one second even without intensive throttling?](#338-why-might-a-timer-in-a-background-tab-fire-later-than-one-second-even-without-intensive-throttling)
- [339: Are timers in Web Workers throttled in background tabs?](#339-are-timers-in-web-workers-throttled-in-background-tabs)
- [340: How does Atomics.waitAsync help build async locks and queues?](#340-how-does-atomicswaitasync-help-build-async-locks-and-queues)
- [341: What does "spin the event loop" mean in the spec?](#341-what-does-spin-the-event-loop-mean-in-the-spec)
- [342: Can other events run while an alert dialog is open?](#342-can-other-events-run-while-an-alert-dialog-is-open)
- [343: How do DevTools breakpoints affect the event loop?](#343-how-do-devtools-breakpoints-affect-the-event-loop)
- [344: When do custom element reactions run, and how is that different from microtasks?](#344-when-do-custom-element-reactions-run-and-how-is-that-different-from-microtasks)
- [345: When does a custom element upgrade happen?](#345-when-does-a-custom-element-upgrade-happen)
- [346: How does event dispatch handle listeners added or removed during dispatch?](#346-how-does-event-dispatch-handle-listeners-added-or-removed-during-dispatch)
- [347: How can you use AbortSignal to remove event listeners?](#347-how-can-you-use-abortsignal-to-remove-event-listeners)
- [348: How does the browser track unhandled promise rejections?](#348-how-does-the-browser-track-unhandled-promise-rejections)
- [349: What happens to the other callbacks when one rAF callback or event listener throws?](#349-what-happens-to-the-other-callbacks-when-one-raf-callback-or-event-listener-throws)
- [350: What is the difference between deep recursion with microtasks and deep recursion on the stack?](#350-what-is-the-difference-between-deep-recursion-with-microtasks-and-deep-recursion-on-the-stack)
- [351: How can pending promises cause memory leaks?](#351-how-can-pending-promises-cause-memory-leaks)
- [352: How does Zone.js work, and why can it not patch native async/await?](#352-how-does-zonejs-work-and-why-can-it-not-patch-native-asyncawait)
- [353: How does zoneless Angular schedule change detection?](#353-how-does-zoneless-angular-schedule-change-detection)
- [354: How does React prioritize updates relative to the event loop?](#354-how-does-react-prioritize-updates-relative-to-the-event-loop)
- [355: How does Vue's scheduler order updates and watchers?](#355-how-does-vues-scheduler-order-updates-and-watchers)
- [356: Should an event bus deliver events synchronously or asynchronously?](#356-should-an-event-bus-deliver-events-synchronously-or-asynchronously)
- [357: A search box filters 10,000 items and typing feels slow. How do you fix it?](#357-a-search-box-filters-10000-items-and-typing-feels-slow-how-do-you-fix-it)
- [358: An animation stutters every few seconds. How do you find the cause?](#358-an-animation-stutters-every-few-seconds-how-do-you-find-the-cause)
- [359: A tooltip flickers and the page is slow when you hover over a list. What is likely going on?](#359-a-tooltip-flickers-and-the-page-is-slow-when-you-hover-over-a-list-what-is-likely-going-on)
- [360: A dashboard gets slower the longer it stays open. What do you check?](#360-a-dashboard-gets-slower-the-longer-it-stays-open-what-do-you-check)
- [361: Your INP is poor and the slowest interactions are simple clicks. The handlers look tiny. What could it be?](#361-your-inp-is-poor-and-the-slowest-interactions-are-simple-clicks-the-handlers-look-tiny-what-could-it-be)
- [362: An infinite scroll feed is janky. How would you improve it?](#362-an-infinite-scroll-feed-is-janky-how-would-you-improve-it)
- [363: Exporting a large CSV freezes the page for several seconds. What do you do?](#363-exporting-a-large-csv-freezes-the-page-for-several-seconds-what-do-you-do)
- [364: Scrolling through an image gallery is janky. What could be blocking?](#364-scrolling-through-an-image-gallery-is-janky-what-could-be-blocking)
- [365: A test passes locally but fails randomly in CI. How can event loop assumptions cause this?](#365-a-test-passes-locally-but-fails-randomly-in-ci-how-can-event-loop-assumptions-cause-this)
- [366: A modal's closing animation is cut off. What is wrong and how do you fix it?](#366-a-modals-closing-animation-is-cut-off-what-is-wrong-and-how-do-you-fix-it)
- [367: getBoundingClientRect returns zeros for an element you just created. Why?](#367-getboundingclientrect-returns-zeros-for-an-element-you-just-created-why)
- [368: A page hangs right after load and DevTools shows no long JavaScript task in the flame chart. How do you find the cause?](#368-a-page-hangs-right-after-load-and-devtools-shows-no-long-javascript-task-in-the-flame-chart-how-do-you-find-the-cause)
- [369: How would you design a Web Worker pool?](#369-how-would-you-design-a-web-worker-pool)
- [370: How can a worker report progress without flooding the main thread with messages?](#370-how-can-a-worker-report-progress-without-flooding-the-main-thread-with-messages)
- [371: A worker sends results back very fast and the page becomes slow. Why, and how do you fix it?](#371-a-worker-sends-results-back-very-fast-and-the-page-becomes-slow-why-and-how-do-you-fix-it)
- [372: How do you build a canvas game loop with a fixed time step?](#372-how-do-you-build-a-canvas-game-loop-with-a-fixed-time-step)
- [373: Users report that the page ignores clicks for a few seconds after it loads. What is happening?](#373-users-report-that-the-page-ignores-clicks-for-a-few-seconds-after-it-loads-what-is-happening)
- [374: In an autocomplete, clicking a suggestion closes the list before the click is handled. Why?](#374-in-an-autocomplete-clicking-a-suggestion-closes-the-list-before-the-click-is-handled-why)
- [375: How does top-level await in a module affect the event loop?](#375-how-does-top-level-await-in-a-module-affect-the-event-loop)
- [376: When does code from a dynamic import() run?](#376-when-does-code-from-a-dynamic-import-run)
- [377: Why is document.write bad for the event loop?](#377-why-is-documentwrite-bad-for-the-event-loop)
- [378: What stops a page from entering the back/forward cache, and why does it matter for the event loop?](#378-what-stops-a-page-from-entering-the-backforward-cache-and-why-does-it-matter-for-the-event-loop)
- [379: How does Safari's Low Power Mode affect requestAnimationFrame?](#379-how-does-safaris-low-power-mode-affect-requestanimationframe)
- [380: Why can event loop quiz answers differ between browsers?](#380-why-can-event-loop-quiz-answers-differ-between-browsers)
- [381: How do browsers throttle cross-origin iframes?](#381-how-do-browsers-throttle-cross-origin-iframes)
- [382: How can you detect main thread hangs in production with a heartbeat?](#382-how-can-you-detect-main-thread-hangs-in-production-with-a-heartbeat)
- [383: What is the JS Self-Profiling API?](#383-what-is-the-js-self-profiling-api)
- [384: How does priority inheritance work with postTask and TaskSignal?](#384-how-does-priority-inheritance-work-with-posttask-and-tasksignal)
- [385: Why does Web Audio use an AudioWorklet instead of the main thread?](#385-why-does-web-audio-use-an-audioworklet-instead-of-the-main-thread)
- [386: What are paint worklets and where do they run?](#386-what-are-paint-worklets-and-where-do-they-run)
- [387: When do canvas drawings become visible on screen?](#387-when-do-canvas-drawings-become-visible-on-screen)
- [388: How does WebGPU work with the event loop?](#388-how-does-webgpu-work-with-the-event-loop)
- [389: How does backpressure work in the Streams API?](#389-how-does-backpressure-work-in-the-streams-api)
- [390: Why can reading a stream in tiny chunks be slow?](#390-why-can-reading-a-stream-in-tiny-chunks-be-slow)
- [391: How do you process a huge text download without blocking the page?](#391-how-do-you-process-a-huge-text-download-without-blocking-the-page)
- [392: How expensive is structuredClone?](#392-how-expensive-is-structuredclone)
- [393: What are transferable streams?](#393-what-are-transferable-streams)
- [394: How do postMessage, SharedArrayBuffer and BroadcastChannel compare for talking to workers?](#394-how-do-postmessage-sharedarraybuffer-and-broadcastchannel-compare-for-talking-to-workers)
- [395: How would you design an app-wide scheduling helper?](#395-how-would-you-design-an-app-wide-scheduling-helper)
- [396: How would you approximate scheduler.yield's priority in a polyfill?](#396-how-would-you-approximate-scheduleryields-priority-in-a-polyfill)
- [397: How do you run several long jobs fairly without one hogging the main thread?](#397-how-do-you-run-several-long-jobs-fairly-without-one-hogging-the-main-thread)
- [398: What are good patterns for cancelling scheduled work?](#398-what-are-good-patterns-for-cancelling-scheduled-work)
- [399: What ordering guarantees can you rely on across browsers?](#399-what-ordering-guarantees-can-you-rely-on-across-browsers)
- [400: How can the event loop be used in timing side-channel attacks?](#400-how-can-the-event-loop-be-used-in-timing-side-channel-attacks)
- [401: How does garbage collection interact with the event loop?](#401-how-does-garbage-collection-interact-with-the-event-loop)
- [402: How do you reduce GC pauses in an animation or game loop?](#402-how-do-you-reduce-gc-pauses-in-an-animation-or-game-loop)
- [403: What is the "latest value wins" pattern and when should you use it?](#403-what-is-the-latest-value-wins-pattern-and-when-should-you-use-it)
- [404: What happens if requestAnimationFrame callbacks take longer than a frame?](#404-what-happens-if-requestanimationframe-callbacks-take-longer-than-a-frame)
- [405: How do variable refresh rate displays affect rAF?](#405-how-do-variable-refresh-rate-displays-affect-raf)
- [406: Describe what happens from a physical click to the next paint.](#406-describe-what-happens-from-a-physical-click-to-the-next-paint)
- [407: Describe what happens to a fetch() call, from call to callback.](#407-describe-what-happens-to-a-fetch-call-from-call-to-callback)
- [408: How does the compositor decide whether input needs the main thread?](#408-how-does-the-compositor-decide-whether-input-needs-the-main-thread)
- [409: How do View Transitions interact with the event loop?](#409-how-do-view-transitions-interact-with-the-event-loop)
- [410: How does the HTML parser share the main thread with other work during page load?](#410-how-does-the-html-parser-share-the-main-thread-with-other-work-during-page-load)
- [411: What are render-blocking resources and how do they relate to rendering opportunities?](#411-what-are-render-blocking-resources-and-how-do-they-relate-to-rendering-opportunities)
- [412: How do you schedule startup work without delaying the first paint?](#412-how-do-you-schedule-startup-work-without-delaying-the-first-paint)
- [413: What happens if you call requestAnimationFrame from a ResizeObserver callback?](#413-what-happens-if-you-call-requestanimationframe-from-a-resizeobserver-callback)
- [414: What happens if you change the DOM inside an IntersectionObserver callback?](#414-what-happens-if-you-change-the-dom-inside-an-intersectionobserver-callback)
- [415: What were Mutation Events and why were they removed?](#415-what-were-mutation-events-and-why-were-they-removed)
- [416: How does window.open without noopener affect the event loop of both pages?](#416-how-does-windowopen-without-noopener-affect-the-event-loop-of-both-pages)
- [417: What are the downsides of using window.postMessage to yourself as a fast task?](#417-what-are-the-downsides-of-using-windowpostmessage-to-yourself-as-a-fast-task)
- [418: How do the page's event loop and the service worker's event loop work together during a fetch?](#418-how-do-the-pages-event-loop-and-the-service-workers-event-loop-work-together-during-a-fetch)
- [419: Why must event.respondWith be called synchronously in a service worker?](#419-why-must-eventrespondwith-be-called-synchronously-in-a-service-worker)
- [420: How expensive are calls between JavaScript and the DOM?](#420-how-expensive-are-calls-between-javascript-and-the-dom)
- [421: How much JavaScript can you run per frame at 60 Hz?](#421-how-much-javascript-can-you-run-per-frame-at-60-hz)
- [422: What is the RAIL model?](#422-what-is-the-rail-model)
- [423: How do you profile event loop behavior on a real mobile device?](#423-how-do-you-profile-event-loop-behavior-on-a-real-mobile-device)
- [424: How do you write an automated test that catches main thread blocking?](#424-how-do-you-write-an-automated-test-that-catches-main-thread-blocking)
- [425: What does this print?](#425-what-does-this-print)
- [426: What does this print?](#426-what-does-this-print)
- [427: What does this print?](#427-what-does-this-print)
- [428: What does this print, and which part is not guaranteed?](#428-what-does-this-print-and-which-part-is-not-guaranteed)
- [429: Why does a MessagePort sometimes never receive messages?](#429-why-does-a-messageport-sometimes-never-receive-messages)
- [430: How are timers, listeners and observers garbage collected?](#430-how-are-timers-listeners-and-observers-garbage-collected)
- [431: Why is reading layout at the start of a rAF callback cheap, but reading after a write expensive?](#431-why-is-reading-layout-at-the-start-of-a-raf-callback-cheap-but-reading-after-a-write-expensive)
- [432: How does CSS containment reduce rendering work?](#432-how-does-css-containment-reduce-rendering-work)
- [433: What are the trade-offs of an off-main-thread architecture?](#433-what-are-the-trade-offs-of-an-off-main-thread-architecture)
- [434: How do you coordinate multiple schedulers in one app?](#434-how-do-you-coordinate-multiple-schedulers-in-one-app)
- [435: Why can you await inside an IndexedDB transaction when using a promise wrapper like idb?](#435-why-can-you-await-inside-an-indexeddb-transaction-when-using-a-promise-wrapper-like-idb)
- [436: How can you deadlock with Atomics and workers?](#436-how-can-you-deadlock-with-atomics-and-workers)
- [437: Why can Promise.all leave work running and still cause unhandled rejections?](#437-why-can-promiseall-leave-work-running-and-still-cause-unhandled-rejections)
- [438: As a library author, which async primitive should you use to call user callbacks?](#438-as-a-library-author-which-async-primitive-should-you-use-to-call-user-callbacks)
- [439: Can a flood of tasks prevent the browser from rendering?](#439-can-a-flood-of-tasks-prevent-the-browser-from-rendering)
- [440: Can timers be starved by input or rendering?](#440-can-timers-be-starved-by-input-or-rendering)
- [441: How does one rendering update handle several documents, like same-origin iframes?](#441-how-does-one-rendering-update-handle-several-documents-like-same-origin-iframes)
- [442: How does a background-priority postTask compare with requestIdleCallback?](#442-how-does-a-background-priority-posttask-compare-with-requestidlecallback)
- [443: How would you migrate a codebase from setTimeout-based chunking to scheduler.yield?](#443-how-would-you-migrate-a-codebase-from-settimeout-based-chunking-to-scheduleryield)
- [444: How do you control the main thread time used by third-party scripts?](#444-how-do-you-control-the-main-thread-time-used-by-third-party-scripts)
- [445: How would you explain the event loop on a whiteboard?](#445-how-would-you-explain-the-event-loop-on-a-whiteboard)
- [446: How does the event loop affect LCP and CLS, not just INP?](#446-how-does-the-event-loop-affect-lcp-and-cls-not-just-inp)
- [447: How do you handle "time jumps" in long-lived apps?](#447-how-do-you-handle-time-jumps-in-long-lived-apps)
- [448: Design question: how do you keep typing latency low in a collaborative text editor?](#448-design-question-how-do-you-keep-typing-latency-low-in-a-collaborative-text-editor)
- [449: Design question: how do you render 100,000 data points smoothly in a chart?](#449-design-question-how-do-you-render-100000-data-points-smoothly-in-a-chart)
- [450: What is your checklist for keeping a page responsive?](#450-what-is-your-checklist-for-keeping-a-page-responsive)

---

# Easy Questions (1-150)

## 1: What is the event loop in the browser?

The event loop is the mechanism that decides what the main thread does next. JavaScript in a page runs on one thread, so the browser needs a way to line up work: run your scripts, handle clicks, fire timers, deliver network responses and redraw the screen.

In a simplified form, every turn of the loop does this:

1. Take one task from a task queue and run it.
2. Run all microtasks that are waiting.
3. If it is time to draw a new frame, update the rendering (run `requestAnimationFrame` callbacks, recalculate styles, layout, paint).
4. Repeat.

## 2: Why does JavaScript in the browser need an event loop?

Because JavaScript on a page runs on a single main thread, but a page has to deal with many things that happen at unpredictable times: user input, timers, network responses, messages from workers and so on.

Without an event loop you would either block the thread while waiting (and freeze the page) or need many threads touching the DOM at once (which would be very hard to make safe). The event loop lets the browser wait for things in the background and then run your callback on the main thread when the result is ready.

## 3: What does it mean that JavaScript is single-threaded in the browser?

It means your page's JavaScript runs on one thread, the main thread, and only one piece of your code runs at any given moment. While a function is running, nothing else on that thread can run: no other callbacks, no event handlers, and no rendering.

The browser itself is not single-threaded. Networking, timers, image decoding, the compositor and other work happen on other threads or processes. Only your page's JavaScript (plus style, layout and paint) shares the main thread. Web Workers give you extra threads, but each worker has its own separate JavaScript environment.

## 4: What is the call stack?

The call stack is how the JavaScript engine keeps track of which function is currently running and where to return when it finishes. When a function is called, a frame is pushed onto the stack. When it returns, the frame is popped.

```js
function c() {
  console.log("in c");
}
function b() {
  c();
}
function a() {
  b();
}

a(); // stack while in c: a -> b -> c
```

The event loop only picks up the next task or microtask when the call stack is empty.

## 5: What happens when the call stack grows too large?

You get a stack overflow. The engine throws a `RangeError: Maximum call stack size exceeded` error. This usually comes from recursion without a proper exit condition.

```js
function loop() {
  loop();
}

loop(); // RangeError: Maximum call stack size exceeded
```

The exact limit depends on the browser and the size of each stack frame, so you should not rely on a specific number.

## 6: What is a task?

A task (often called a macrotask) is a unit of work that the event loop picks up and runs from start to finish. Examples are:

- Running a `<script>` element
- Calling a `setTimeout` or `setInterval` callback
- Dispatching a user event like `click` or `keydown`
- Delivering a `message` from `postMessage`
- Many network and storage callbacks

The event loop runs one task per turn, then runs microtasks, then may render.

## 7: What is a microtask?

A microtask is a small piece of work that runs right after the current script finishes, before the event loop moves on to the next task and before rendering. The most common microtasks are promise callbacks (`then`, `catch`, `finally`, and the code after `await`).

```js
console.log("start");

Promise.resolve().then(() => console.log("microtask"));

console.log("end");

// start
// end
// microtask
```

## 8: What is the difference between a task and a microtask?

- **Tasks** are taken one per event loop turn. Between two tasks the browser can run microtasks and render a frame.
- **Microtasks** are run in a batch after the current script finishes. The browser runs all of them, including any new ones added while running, before it continues.

So microtasks always run before the next task and before the next render. That is why a `Promise.then` callback runs before a `setTimeout(fn, 0)` callback that was scheduled earlier.

## 9: Which browser APIs schedule tasks?

Common ones:

- `setTimeout` and `setInterval`
- User input events (`click`, `keydown`, `input`, and so on)
- `postMessage` (window, worker, `MessageChannel`)
- Network events, such as `XMLHttpRequest` events and `WebSocket` messages
- `IndexedDB` request events
- `scheduler.postTask()`
- Running a `<script>` element

The spec groups these into task sources (timers, user interaction, networking, DOM manipulation and others).

## 10: Which browser APIs schedule microtasks?

- Promise reactions: `then`, `catch`, `finally`
- The code after `await` in an async function
- `queueMicrotask()`
- `MutationObserver` callbacks

```js
queueMicrotask(() => console.log("from queueMicrotask"));
Promise.resolve().then(() => console.log("from promise"));

// from queueMicrotask
// from promise
```

They all go into the same microtask queue, so they run in the order they were queued.

## 11: What is the task queue?

The task queue is where tasks wait until the event loop can run them. When a timer expires or a user clicks, the browser does not run your callback right away. It puts a task in a queue, and the event loop runs it when the main thread is free.

In the spec there are actually several task queues, one per kind of task (or group of kinds). The browser can choose which queue to take the next task from, which lets it give priority to things like user input.

## 12: What is the microtask queue?

The microtask queue holds microtasks waiting to run. There is one microtask queue per event loop, and it is a real first-in, first-out queue.

When the call stack becomes empty (for example after a task or an event listener finishes), the browser runs a microtask checkpoint: it keeps taking microtasks from the queue and running them until the queue is empty.

## 13: What is the output of this code and why?

```js
console.log("1");

setTimeout(() => console.log("2"), 0);

Promise.resolve().then(() => console.log("3"));

console.log("4");
```

Output:

```text
1
4
3
2
```

`1` and `4` are synchronous and print first. The promise callback is a microtask, so it runs as soon as the script finishes. The `setTimeout` callback is a task, so it waits for the next turn of the event loop.

## 14: What does setTimeout(fn, 0) actually do?

It asks the browser to queue a task that calls `fn` after at least 0 ms. It does not run `fn` immediately. `fn` runs only after:

- the current script finishes,
- all pending microtasks run,
- any tasks already ahead of it are processed (and maybe a frame is rendered).

People use it to "defer" some work until after the current code. Today there are better tools for that depending on the goal: `queueMicrotask` for "right after this code", `requestAnimationFrame` for "before the next paint" and `scheduler.yield()` or `scheduler.postTask()` for "let the browser breathe".

## 15: Is the delay in setTimeout guaranteed?

No. The delay is a minimum, not an exact time. The callback runs at the earliest after the delay, but it can run much later if:

- the main thread is busy with other code,
- other tasks are ahead in the queue,
- the browser clamps the delay (for example to 4 ms for deeply nested timers),
- the tab is in the background and timers are throttled.

```js
const start = performance.now();
setTimeout(() => {
  console.log(performance.now() - start); // often more than 100
}, 100);

// Busy loop for 300 ms
while (performance.now() - start < 300) {}
```

Here the callback runs after about 300 ms, not 100.

## 16: What is setInterval?

`setInterval(fn, delay)` queues `fn` to run repeatedly, every `delay` milliseconds, until you cancel it with `clearInterval`.

```js
let count = 0;
const id = setInterval(() => {
  count++;
  console.log("tick", count);
  if (count === 3) clearInterval(id);
}, 1000);
```

Like `setTimeout`, the timing is not exact. If the main thread is busy, ticks get delayed. Browsers do not queue a backlog of missed ticks either, so you cannot count on getting one call per interval.

## 17: How do you cancel a timer?

Save the id returned by `setTimeout` or `setInterval` and pass it to `clearTimeout` or `clearInterval`.

```js
const timeoutId = setTimeout(() => console.log("never runs"), 1000);
clearTimeout(timeoutId);

const intervalId = setInterval(() => console.log("tick"), 1000);
clearInterval(intervalId);
```

In browsers, timeouts and intervals share the same pool of ids, so `clearTimeout` can cancel an interval and the other way around, but it is clearer to use the matching function.

## 18: What happens if you call clearTimeout with an id that already ran or does not exist?

Nothing. `clearTimeout` silently ignores ids that are unknown or already finished. It does not throw.

This means you can safely call `clearTimeout(id)` in cleanup code without checking whether the timer already fired.

## 19: What are Web APIs in the context of the event loop?

Web APIs are features the browser provides to JavaScript that are not part of the JavaScript language itself: `setTimeout`, `fetch`, DOM events, `requestAnimationFrame`, `IndexedDB` and so on.

When you call one of them, the browser does the waiting or the work outside your JavaScript code (often on another thread). When the result is ready, it queues a task or resolves a promise so your callback runs on the main thread through the event loop.

## 20: Who counts down the time for setTimeout?

The browser does, not the JavaScript engine. When you call `setTimeout`, the browser records the timer and keeps track of time in its own code. Your JavaScript is free to keep running or the thread can go idle.

When the time is up, the browser queues a task. The callback still has to wait for the main thread to be free before it can run.

## 21: Is the event loop part of JavaScript (ECMAScript)?

No. The ECMAScript spec only defines "jobs" (used for promises) and says the host environment must run them. The event loop itself, with tasks, microtasks and rendering, is defined in the HTML Standard for browsers.

That is why the browser and Node.js have different event loops even though they both run JavaScript. The engine (V8, SpiderMonkey, JavaScriptCore) runs the code; the host (the browser or Node.js) decides when to run what.

## 22: Where is the browser event loop specified?

In the HTML Living Standard maintained by WHATWG, in the section called "Event loops". It describes:

- the types of event loops (window, worker, worklet),
- task queues and task sources,
- the microtask queue and microtask checkpoints,
- the processing model, including the "update the rendering" steps.

Browsers follow this model, though they have freedom in some areas, like which task queue to pick next and how often to render.

## 23: When does a Promise then callback run?

When the promise settles, its `then` callbacks are queued as microtasks. They do not run synchronously, even if the promise is already resolved.

```js
const p = Promise.resolve(42);

p.then((value) => console.log("then:", value));
console.log("after then");

// after then
// then: 42
```

This is a deliberate rule so that promise callbacks always run in a consistent, asynchronous way.

## 24: Is the function passed to new Promise synchronous?

Yes. The executor function runs immediately and synchronously when you create the promise. Only the `then`, `catch` and `finally` callbacks are async.

```js
console.log("A");

new Promise((resolve) => {
  console.log("B");
  resolve();
}).then(() => console.log("D"));

console.log("C");

// A
// B
// C
// D
```

## 25: What does queueMicrotask do?

`queueMicrotask(fn)` adds `fn` to the microtask queue. It runs after the current script finishes and before the next task or render, just like a promise callback.

```js
queueMicrotask(() => console.log("microtask"));
console.log("sync");

// sync
// microtask
```

It is cleaner than `Promise.resolve().then(fn)` when you just want a microtask, and errors thrown inside it are reported like normal uncaught errors instead of turning into rejected promises.

## 26: What is requestAnimationFrame?

`requestAnimationFrame(callback)` asks the browser to call `callback` right before it renders the next frame. It is the right tool for visual updates like animations, because your code runs in step with the screen refresh.

```js
const box = document.querySelector(".box");
let x = 0;

function step() {
  x += 2;
  box.style.transform = `translateX(${x}px)`;
  if (x < 300) requestAnimationFrame(step);
}

requestAnimationFrame(step);
```

The callback runs once. To keep animating, call `requestAnimationFrame` again inside it.

## 27: When do requestAnimationFrame callbacks run in the event loop?

They run in the "update the rendering" step of the event loop, which happens after a task and its microtasks are done, and only when the browser decides it is time to draw a new frame (usually once per display refresh, for example every ~16.7 ms on a 60 Hz screen).

Within that step, rAF callbacks run before style recalculation, layout and paint. So any DOM change you make inside rAF is included in the frame that is about to be drawn.

## 28: How do you cancel a requestAnimationFrame callback?

`requestAnimationFrame` returns an id. Pass it to `cancelAnimationFrame`.

```js
const id = requestAnimationFrame(() => console.log("frame"));
cancelAnimationFrame(id);
```

This is useful when a component is removed or an animation is stopped before the next frame.

## 29: What does "rendering" mean in the context of the event loop?

Rendering is the work the browser does to turn the DOM and CSS into pixels on the screen. On the main thread this mainly includes:

- **Style**: working out which CSS rules apply to each element.
- **Layout**: calculating the size and position of every element.
- **Paint**: recording what to draw (text, colors, borders, images).

After that, other threads rasterize and composite the result to the screen. Rendering only happens between tasks, never in the middle of your JavaScript.

## 30: How often does the browser render a frame?

Usually as often as the display refreshes: about 60 times per second on a 60 Hz screen, 120 on a 120 Hz screen. But the browser only renders when needed and when it can:

- if nothing changed, it can skip a frame,
- if the main thread is busy, frames are delayed or dropped,
- in background tabs, rendering mostly stops,
- some devices lower the rate to save power.

## 31: What is the frame budget?

The frame budget is how much time the browser has to produce one frame. At 60 Hz it is about 16.7 ms (1000 / 60). In that time the browser needs to run your JavaScript, style, layout, paint and compositing.

In practice your own JavaScript should use much less than the full 16.7 ms per frame, since the browser needs time for its own work. On 120 Hz screens the budget is about 8.3 ms.

## 32: What does "blocking the main thread" mean?

It means running code on the main thread for so long that the browser cannot do anything else. While your code runs:

- clicks and key presses are not handled,
- nothing gets repainted,
- timers and network callbacks wait.

```js
button.addEventListener("click", () => {
  const end = Date.now() + 3000;
  while (Date.now() < end) {} // page is frozen for 3 seconds
});
```

## 33: What happens to the page when a long synchronous loop runs?

The page freezes until the loop ends. Animations driven by JavaScript stop, buttons do not respond, text inputs do not update and the page is not repainted. Some CSS animations and scrolling can keep going if they are handled by the compositor thread, but anything that needs the main thread waits.

If it takes long enough, the browser may show a "Page unresponsive" dialog and offer to stop the script.

## 34: What is a long task?

A long task is any task that keeps the main thread busy for more than 50 ms. The 50 ms number comes from the idea that a response to user input within about 100 ms feels instant, so tasks should be short enough to leave room for handling input.

You can see long tasks in the Chrome DevTools Performance panel (they have a red corner) and watch them in code with the Long Tasks API:

```js
new PerformanceObserver((list) => {
  for (const entry of list.getEntries()) {
    console.log("Long task:", entry.duration, "ms");
  }
}).observe({ type: "longtask", buffered: true });
```

## 35: What is the main thread?

The main thread is the thread where the browser runs your page's JavaScript and also does style calculation, layout, paint and most event handling for that page. Because all of this shares one thread, a slow piece of JavaScript delays everything else on the page.

## 36: What kind of work runs on the main thread?

- Parsing HTML and running scripts
- Event handlers, timers and promise callbacks
- `requestAnimationFrame` callbacks
- Style recalculation, layout and paint
- Most DOM API calls
- Garbage collection work (partly; modern engines also do a lot of it on other threads)

If any of these takes too long, the others have to wait.

## 37: What work runs off the main thread?

Browsers move a lot of work to other threads or processes:

- Network requests
- Image decoding (often)
- Rasterization and compositing (turning paint records into pixels and putting layers on screen)
- Scrolling and some animations, when the compositor can handle them alone
- Web Workers, Service Workers and Audio Worklets
- Parts of JavaScript parsing, compiling and garbage collection

This is why scrolling can stay smooth on some pages even when JavaScript is busy.

## 38: What is a Web Worker?

A Web Worker runs JavaScript on a separate background thread. It is useful for heavy work like parsing large files, image processing or complex calculations that would otherwise block the main thread.

```js
// main.js
const worker = new Worker("worker.js");
worker.postMessage({ numbers: [1, 2, 3, 4] });
worker.onmessage = (event) => console.log("sum:", event.data);

// worker.js
self.onmessage = (event) => {
  const sum = event.data.numbers.reduce((a, b) => a + b, 0);
  self.postMessage(sum);
};
```

Workers cannot touch the DOM directly. They talk to the page by sending messages.

## 39: Does a Web Worker share the event loop with the page?

No. Each worker has its own event loop, its own task queues and its own microtask queue. A long task in a worker does not block the page, and a long task on the page does not block the worker.

A worker's event loop has no rendering step, because workers do not render the DOM.

## 40: How does the page communicate with a worker?

With `postMessage` and the `message` event. The data is copied using the structured clone algorithm, so the worker gets its own copy. For large binary data you can transfer ownership instead of copying.

```js
const buffer = new ArrayBuffer(1024 * 1024);
worker.postMessage(buffer, [buffer]); // transferred, not copied
console.log(buffer.byteLength); // 0, the page no longer owns it
```

Each received message is delivered as a task in the receiver's event loop.

## 41: How do async and await relate to the event loop?

`async` and `await` are syntax built on promises. When an async function reaches `await`, it pauses and returns control to the caller. When the awaited promise settles, the rest of the function is queued as a microtask.

```js
async function load() {
  console.log("1");
  await null;
  console.log("3");
}

load();
console.log("2");

// 1
// 2
// 3
```

So `await` does not block the thread. It splits your function into pieces that run at different times.

## 42: What exactly happens at an await?

1. The expression after `await` is evaluated and turned into a promise if it is not one.
2. The async function is paused and its state is saved.
3. Control goes back to whoever called the function (it gets a pending promise).
4. When the awaited promise settles, a microtask is queued to resume the function from where it stopped.

Even `await` on a value that is already available (like `await 5`) pauses the function until the next microtask checkpoint.

## 43: Does code inside an async function before the first await run synchronously?

Yes. An async function runs synchronously until it hits the first `await` (or a `return`). Only the code after an `await` is deferred.

```js
async function run() {
  console.log("inside, before await");
  await Promise.resolve();
  console.log("inside, after await");
}

console.log("before call");
run();
console.log("after call");

// before call
// inside, before await
// after call
// inside, after await
```

## 44: What does an async function return?

Always a promise. If the function returns a value, the promise is fulfilled with that value. If it throws, the promise is rejected with the error.

```js
async function getNumber() {
  return 7;
}

getNumber().then((n) => console.log(n)); // 7
console.log(getNumber() instanceof Promise); // true
```

## 45: Does using async make code run in parallel?

No. `async` code still runs on the same main thread, one piece at a time. It lets you wait for things like network requests without blocking, but CPU-heavy code inside an async function still blocks the page.

```js
async function heavy() {
  // This still blocks the main thread
  for (let i = 0; i < 1e9; i++) {}
}
```

For real parallel work you need a Web Worker.

## 46: What is a callback in the context of the event loop?

A callback is a function you pass to an API so it can be called later. With async APIs, the browser calls your callback through the event loop when something happens: a timer fires, an event is dispatched, a response arrives.

```js
setTimeout(function callback() {
  console.log("called later by the event loop");
}, 500);
```

## 47: When does an event listener run?

When the event is dispatched. For events caused by the user or the browser (clicks, key presses, network events), the browser queues a task, and when the event loop runs that task, it dispatches the event and calls your listeners one by one.

For events you dispatch yourself with `dispatchEvent()`, listeners run synchronously, right inside the `dispatchEvent` call.

## 48: What happens when the user clicks while JavaScript is running?

The click is not handled right away. The browser records the input and queues a task to dispatch the event. Your current code keeps running until it finishes. After that, microtasks run, and then the event loop can pick the click task.

So if the main thread is blocked for 2 seconds, a click made during that time gets handled after the 2 seconds. This delay is part of what INP (Interaction to Next Paint) measures.

## 49: Is dispatchEvent synchronous or asynchronous?

Synchronous. All listeners run before `dispatchEvent` returns.

```js
const target = new EventTarget();
target.addEventListener("ping", () => console.log("listener"));

console.log("before");
target.dispatchEvent(new Event("ping"));
console.log("after");

// before
// listener
// after
```

This is different from real user events, which are queued as tasks.

## 50: Does event bubbling happen across several tasks?

No. The whole dispatch of one event, through the capture phase, the target and the bubble phase, happens within a single task. All listeners on all elements in the path are called one after another during that task.

Microtasks may run between listeners (when the event came from the browser, not from `dispatchEvent`), but the event loop does not move on to other tasks or render in the middle of a dispatch.

## 51: When do fetch callbacks run?

`fetch()` returns a promise right away. The network request happens outside the main thread. When the response headers arrive, the browser queues a task that resolves the promise, and your `then` callbacks (or the code after `await`) run as microtasks after that.

```js
console.log("start");

fetch("/api/user")
  .then((res) => res.json())
  .then((user) => console.log("user:", user));

console.log("request sent");

// start
// request sent
// user: {...} (later)
```

Reading the body with `res.json()` is another async step that resolves later.

## 52: Does fetch block the main thread?

No. The request and the download happen in the browser's network stack, off the main thread. The main thread is free to do other work while it waits.

What can block the main thread is what you do with the result. For example, calling `JSON.parse` on a 50 MB string, or rendering 10,000 rows into the DOM at once.

## 53: What is a synchronous XMLHttpRequest and why should you avoid it?

`XMLHttpRequest` has a mode where the third argument of `open` is `false`. The call to `send()` then blocks until the response arrives.

```js
const xhr = new XMLHttpRequest();
xhr.open("GET", "/api/data", false); // synchronous, avoid this
xhr.send();
console.log(xhr.responseText);
```

During that wait, the page is frozen: no input, no rendering. Browsers warn about it in the console, and some features (like sync XHR during page dismissal) are not allowed anymore. Use `fetch` with `await` instead.

## 54: What do alert, confirm and prompt do to the event loop?

They block. While the dialog is open, your script is paused at that line and the event loop for the page is paused too. Timers do not fire, and other callbacks wait until the dialog is closed.

```js
setTimeout(() => console.log("timer"), 0);
alert("Close me"); // timer waits until the dialog is closed
console.log("after alert");
```

This is one reason these dialogs are disliked in modern apps. A custom modal (or the `<dialog>` element) does not block anything.

## 55: What is "run to completion"?

Run to completion means that once a task (or a microtask) starts running JavaScript, it runs until it finishes. Nothing else on the same thread can interrupt it in the middle: no event handler, no timer callback, no other microtask.

This makes JavaScript easier to reason about. Inside one synchronous piece of code, you do not need locks, because no other code can change your variables at the same time.

## 56: Can a click handler interrupt a function that is already running?

No. The click handler waits until the running code finishes (and the microtasks after it). JavaScript on the main thread is never preempted by other JavaScript on the same thread.

```js
let counter = 0;

button.addEventListener("click", () => {
  counter = 100;
});

function work() {
  counter = 1;
  // Even if the user clicks here, the handler cannot run yet
  console.log(counter); // always 1
}
```

## 57: What is the difference between concurrency and parallelism in browser JavaScript?

- **Concurrency** means several pieces of work are in progress at the same time, but only one actually runs at any moment. The event loop gives you concurrency: many fetches, timers and handlers can be pending, and they take turns on the main thread.
- **Parallelism** means work really runs at the same time on different CPU cores. In the browser you get this with Web Workers (or with browser internals like network and raster threads).

## 58: What is one "turn" or "tick" of the event loop?

One turn is one pass through the loop:

1. Pick the oldest runnable task from one of the task queues and run it.
2. Run a microtask checkpoint (empty the microtask queue).
3. If it is a good time to render, update the rendering.
4. If there is nothing to do, the browser may run idle callbacks.

"Tick" is an informal word. People sometimes use it for one event loop turn and sometimes for one microtask, so it helps to ask which one is meant.

## 59: Do all pending microtasks run between two tasks?

Yes. After each task, the browser runs a microtask checkpoint and keeps running microtasks until the queue is empty. Only then does it continue to rendering or the next task.

```js
setTimeout(() => console.log("task 2"), 0);

Promise.resolve()
  .then(() => console.log("micro 1"))
  .then(() => console.log("micro 2"))
  .then(() => console.log("micro 3"));

// micro 1
// micro 2
// micro 3
// task 2
```

## 60: Can a microtask schedule more microtasks?

Yes, and those new microtasks also run in the same checkpoint, before the event loop moves on.

```js
queueMicrotask(() => {
  console.log("first");
  queueMicrotask(() => console.log("added by first"));
});

setTimeout(() => console.log("timeout"), 0);

// first
// added by first
// timeout
```

This is handy, but it also means a microtask that always adds another one will never let the event loop continue (see microtask starvation).

## 61: What is MutationObserver and when does its callback run?

`MutationObserver` watches the DOM for changes (added or removed nodes, attribute changes, text changes). Its callback runs as a microtask, after the code that made the changes finishes.

```js
const observer = new MutationObserver((records) => {
  console.log("mutations:", records.length);
});

observer.observe(document.body, { childList: true });

document.body.append(document.createElement("div"));
document.body.append(document.createElement("div"));
console.log("sync code done");

// sync code done
// mutations: 2
```

Several changes made in the same script are delivered together in one callback.

## 62: What is the "callback queue"?

"Callback queue" is an informal name used in many tutorials for the task queue: the place where callbacks from timers, events and other APIs wait until the call stack is empty.

The HTML spec does not use that name. It talks about task queues (there can be several) and one microtask queue. In an interview, it is good to know both the informal and the spec terms.

## 63: Is "macrotask" an official term?

No. The HTML spec only says "task". "Macrotask" became popular to make the contrast with "microtask" clearer. When someone says macrotask, they mean a normal task, like a `setTimeout` callback or an event dispatch.

## 64: If two setTimeout calls have the same delay, which runs first?

The one that was scheduled first. The HTML spec says timers are run in order of their scheduled time, and timers with the same timeout run in the order they were created.

```js
setTimeout(() => console.log("A"), 10);
setTimeout(() => console.log("B"), 10);

// A
// B
```

## 65: What is the output when timers have different delays?

```js
setTimeout(() => console.log("100ms"), 100);
setTimeout(() => console.log("0ms"), 0);
setTimeout(() => console.log("50ms"), 50);
```

Output:

```text
0ms
50ms
100ms
```

The order follows when each timer expires, not the order of the `setTimeout` calls.

## 66: Is a then callback on an already resolved promise still asynchronous?

Yes. Even if the promise is already fulfilled, the callback is queued as a microtask and runs after the current code.

```js
const done = Promise.resolve("ready");

done.then((v) => console.log(v));
console.log("this prints first");

// this prints first
// ready
```

This avoids the problem where the same code sometimes runs synchronously and sometimes asynchronously.

## 67: What is printed here?

```js
console.log("A");

Promise.resolve().then(() => console.log("B"));

queueMicrotask(() => console.log("C"));

console.log("D");
```

Output:

```text
A
D
B
C
```

`A` and `D` are synchronous. `B` and `C` are both microtasks. They run in the order they were queued.

## 68: How does Promise.all work in terms of the event loop?

`Promise.all` subscribes to every promise you pass with `then`. Each time one settles, a microtask records the result. When the last one fulfills, the promise returned by `Promise.all` fulfills, and its `then` callback is queued as another microtask.

```js
const a = fetch("/a");
const b = fetch("/b");

const [resA, resB] = await Promise.all([a, b]);
```

The requests run at the same time in the network layer. `Promise.all` does not make anything parallel by itself; it just waits for all of them.

## 69: What is an unhandled promise rejection?

It is a promise that was rejected and has no `catch` (or rejection handler in `then`) by the time the browser checks. The browser logs an error in the console and fires the `unhandledrejection` event on `window`.

```js
window.addEventListener("unhandledrejection", (event) => {
  console.log("Unhandled:", event.reason);
});

Promise.reject(new Error("Oops"));
```

You should handle rejections with `catch` or `try/catch` around `await`.

## 70: Why does try/catch around setTimeout not catch an error thrown inside the callback?

Because the callback runs later, in a different task. By the time it runs, the `try/catch` block has already finished.

```js
try {
  setTimeout(() => {
    throw new Error("Boom");
  }, 0);
} catch (e) {
  console.log("never reached");
}
```

Put the `try/catch` inside the callback instead:

```js
setTimeout(() => {
  try {
    throw new Error("Boom");
  } catch (e) {
    console.log("caught:", e.message);
  }
}, 0);
```

## 71: Why does try/catch not catch a rejected promise unless you await it?

Without `await`, the promise is rejected later, after the `try` block has finished. The `try/catch` only sees errors that are thrown synchronously in the block.

```js
async function fail() {
  throw new Error("Failed");
}

try {
  fail(); // returns a rejected promise, nothing is thrown here
} catch {
  console.log("not reached");
}

async function main() {
  try {
    await fail(); // the rejection is turned into a throw here
  } catch (e) {
    console.log("caught:", e.message);
  }
}
```

## 72: What is the window error event?

The `error` event on `window` fires when an uncaught error happens in a task, for example in a timer callback or an event listener. It is commonly used for logging errors.

```js
window.addEventListener("error", (event) => {
  console.log("Error:", event.message, event.filename, event.lineno);
});

setTimeout(() => {
  throw new Error("Uncaught in timer");
}, 0);
```

Rejected promises are reported through `unhandledrejection`, not `error`.

## 73: Does an uncaught error in one task stop the event loop?

No. The error is reported (in the console and through the `error` event), the current task stops, and the event loop goes on with the next task. Other timers, event handlers and promises continue to work.

The code after the `throw` in that same task does not run, though, so the page can be left in a half-updated state.

## 74: Why does a for loop with var and setTimeout print the same number?

```js
for (var i = 0; i < 3; i++) {
  setTimeout(() => console.log(i), 0);
}
// 3
// 3
// 3
```

The loop finishes before any timer callback runs. With `var`, there is only one `i` for the whole loop, and by the time the callbacks run it is `3`.

Use `let`, which creates a new binding for each iteration:

```js
for (let i = 0; i < 3; i++) {
  setTimeout(() => console.log(i), 0);
}
// 0
// 1
// 2
```

## 75: How do you write a sleep or delay function?

Wrap `setTimeout` in a promise:

```js
function sleep(ms) {
  return new Promise((resolve) => setTimeout(resolve, ms));
}

async function run() {
  console.log("start");
  await sleep(1000);
  console.log("one second later");
}
```

This does not block the thread. Other code keeps running during the wait.

## 76: What is the minimum delay of setTimeout?

You can pass `0`, but the HTML spec says that once timers are nested more than 5 levels deep (a timer callback that schedules a timer, and so on), the delay is raised to at least 4 ms.

```js
let last = performance.now();
let n = 0;

function tick() {
  const now = performance.now();
  console.log(n, (now - last).toFixed(2));
  last = now;
  if (++n < 10) setTimeout(tick, 0);
}

setTimeout(tick, 0);
// The first few gaps are small; later gaps are around 4 ms or more
```

In background tabs the minimum is much larger (usually around 1 second).

## 77: What happens to timers in a background tab?

Browsers slow them down to save battery and CPU. In a hidden tab, timers usually fire at most once per second. Chrome goes further for pages hidden for a long time: chained timers can be limited to about once per minute.

So a countdown or polling loop based on `setTimeout` will run much less often in the background. If you need correct elapsed time, compare timestamps instead of counting ticks.

## 78: Why does requestAnimationFrame stop in background tabs?

`requestAnimationFrame` runs before the browser renders a frame. A hidden tab does not render, so rAF callbacks are paused. When the tab becomes visible again, they continue.

This is a good thing for animations, because there is no point animating something nobody can see. Do not use rAF for work that must keep running in the background.

## 79: What is requestIdleCallback?

`requestIdleCallback(callback)` asks the browser to call `callback` when the main thread is idle, meaning there is no urgent work and time is left before the next frame. It is meant for low priority work like sending analytics or preparing data you might need later.

```js
requestIdleCallback((deadline) => {
  while (deadline.timeRemaining() > 0 && tasks.length > 0) {
    doTask(tasks.shift());
  }
});
```

Safari was late to support it and its support has had problems, so check the current status and keep a fallback (such as `setTimeout`).

## 80: What does deadline.timeRemaining() return in requestIdleCallback?

It returns an estimate, in milliseconds, of how much idle time is left in the current idle period. It is never more than 50 ms. When it reaches 0, you should stop and schedule another idle callback for the rest of the work.

`deadline.didTimeout` is `true` when the callback runs because the `timeout` option expired, not because the browser became idle.

## 81: What is scheduler.postTask?

`scheduler.postTask(callback, options)` is part of the Prioritized Task Scheduling API. It queues a task with a priority and returns a promise for the callback's result.

```js
scheduler.postTask(() => console.log("important"), {
  priority: "user-blocking",
});

scheduler.postTask(() => console.log("normal")); // "user-visible" by default

scheduler.postTask(() => console.log("whenever"), {
  priority: "background",
});
```

It is supported in Chromium browsers and Firefox but not in Safari at the time of writing, so feature-detect it.

## 82: What is scheduler.yield?

`scheduler.yield()` returns a promise that resolves in a new task. You `await` it in the middle of long work to give the browser a chance to handle input and render, and then your code continues.

```js
async function processAll(items) {
  for (const item of items) {
    process(item);
    await scheduler.yield();
  }
}
```

The difference from `await new Promise(r => setTimeout(r, 0))` is that the continuation gets higher priority, so it runs before other queued tasks of the same priority. Chromium (from version 129) and Firefox (from version 142) support it; Safari does not yet.

## 83: What does "yielding to the main thread" mean?

It means stopping your JavaScript on purpose for a moment, so the event loop can run other things (like handling a click or painting a frame), and then continuing in a later task.

You yield by ending the current task and scheduling the rest of the work with something like `scheduler.yield()`, `setTimeout` or `scheduler.postTask()`. An `await` on an already resolved promise does not yield, because microtasks run before the browser gets control back.

## 84: Why should you break up long tasks?

Because while a long task runs, the browser cannot respond to input or update the screen. Breaking one 500 ms task into many small tasks lets the browser handle clicks and paint between them.

The total work takes about the same time, but the page feels responsive. This directly improves INP, which is one of the Core Web Vitals.

## 85: How can you split a long loop into chunks with setTimeout?

```js
function processInChunks(items, chunkSize = 100) {
  let index = 0;

  function nextChunk() {
    const end = Math.min(index + chunkSize, items.length);
    for (; index < end; index++) {
      process(items[index]);
    }
    if (index < items.length) {
      setTimeout(nextChunk, 0);
    }
  }

  nextChunk();
}
```

Each chunk is a separate task, so the browser can handle input and render between chunks. `scheduler.yield()` is the modern alternative where supported.

## 86: What is INP and how does it relate to the event loop?

INP (Interaction to Next Paint) is a Core Web Vital that measures how long it takes from a user interaction (click, tap, key press) until the next frame is painted. It replaced FID in March 2024.

It has three parts that all come from the event loop:

- **Input delay**: time the event waits because the main thread is busy.
- **Processing time**: time your event listeners take to run.
- **Presentation delay**: time to run rendering work and show the next frame.

Good INP is 200 ms or less. Long tasks hurt all three parts.

## 87: Why is requestAnimationFrame better than setTimeout for animations?

- rAF runs right before the browser renders, so each update lands in a frame. A `setTimeout(fn, 16)` is not synced with the display, so updates can be too early, too late or two in one frame, which looks jerky.
- rAF adapts to the screen's refresh rate (60 Hz, 120 Hz and so on).
- rAF pauses in background tabs, saving battery.
- rAF gives you a timestamp you can use to calculate smooth movement.

## 88: What is jank?

Jank is when scrolling, animations or typing feel choppy because frames are dropped or delayed. It usually happens when the main thread is busy for longer than one frame, so the browser cannot produce new frames on time.

Common causes are long JavaScript tasks, heavy layout or style work, large DOM updates and repeated forced layouts.

## 89: Can CSS animations keep running when the main thread is blocked?

Some can. Animations and transitions that only change `transform` or `opacity` (and a few other properties) can usually be run by the compositor thread. They keep going smoothly even if JavaScript is busy.

Animations of properties like `width`, `top` or `background-color` need the main thread for layout or paint, so they freeze or stutter when the main thread is blocked.

## 90: What is the compositor thread?

The compositor thread is a separate thread in the browser's renderer that takes painted layers and combines them into the final image on screen. It can handle some things alone, without the main thread:

- scrolling (when no JavaScript needs to block it),
- `transform` and `opacity` animations,
- pinch zoom.

This is why a page with busy JavaScript can sometimes still scroll smoothly.

## 91: How do DOMContentLoaded and load relate to the event loop?

Both are fired as tasks.

- `DOMContentLoaded` fires after the HTML is fully parsed and all `defer` and module scripts have run.
- `load` fires on `window` after the page and its subresources (images, stylesheets, iframes) have loaded.

Since they are tasks, a long script before them delays them, and microtasks from your code always run before the next of these events.

## 92: When do classic script tags run?

A normal `<script>` without `async` or `defer` blocks the HTML parser. The parser stops, the script is downloaded (if external) and executed, and then parsing continues.

After each script finishes running, a microtask checkpoint happens, so promise callbacks queued by that script run before the parser continues to the next part of the page.

## 93: What is the difference between async and defer scripts in terms of when they run?

- **defer**: downloaded in parallel with parsing, run in order after parsing finishes, before `DOMContentLoaded`.
- **async**: downloaded in parallel, run as soon as each one is ready, in any order. It may run before or after `DOMContentLoaded`.

```html
<script defer src="app.js"></script>
<script async src="analytics.js"></script>
```

Both avoid blocking the parser while downloading. But when they run, they still run on the main thread and can block it.

## 94: Do module scripts behave like defer scripts?

Yes, by default. `<script type="module">` is deferred: it does not block the parser and runs after the document is parsed, in order with other deferred scripts. You can add `async` to a module script so it runs as soon as it and its imports are ready.

```html
<script type="module" src="main.js"></script>
```

## 95: Is there one event loop per tab?

Roughly, yes, but not exactly. The spec says each "agent" (a group of same-site windows that can reach each other) has one event loop. In practice:

- a normal tab with its own site has its own event loop,
- same-origin iframes inside it share that event loop,
- cross-site iframes usually run in another process with their own event loop (because of site isolation),
- each worker has its own event loop.

## 96: Do iframes share the event loop with the parent page?

Same-origin (and same-site) iframes that can access each other share the event loop with the parent. A long task in one blocks the other.

Cross-site iframes are usually put in a different process by modern browsers (site isolation in Chrome and Firefox), so they have their own event loop and do not block the parent's main thread.

## 97: What is window.postMessage and how is the message delivered?

`postMessage` sends data to another window (for example an iframe or a popup), a worker or a `MessagePort`. The receiver gets a `message` event, which is queued as a task.

```js
// Parent page
iframe.contentWindow.postMessage({ type: "hello" }, "https://child.example");

// Inside the iframe
window.addEventListener("message", (event) => {
  if (event.origin !== "https://parent.example") return;
  console.log(event.data.type); // "hello"
});
```

Always check `event.origin` when receiving messages from other windows.

## 98: What is MessageChannel?

`MessageChannel` creates a pair of connected ports. A message sent on one port arrives as a `message` event on the other, as a task.

```js
const channel = new MessageChannel();

channel.port1.onmessage = (event) => {
  console.log("received:", event.data);
};

channel.port2.postMessage("hi");
```

It is used for communication between windows, iframes and workers. It is also used as a trick to queue a task without the 4 ms clamp that nested `setTimeout` calls get.

## 99: Does setImmediate exist in browsers?

No. `setImmediate` was a non-standard API that only Internet Explorer and old Edge supported. It exists in Node.js but not in modern browsers.

If you see it in browser code, it is probably coming from a polyfill. In the browser, use `setTimeout`, `MessageChannel`, `scheduler.postTask` or `queueMicrotask` depending on what you need.

## 100: Does process.nextTick exist in the browser?

No. `process.nextTick` is a Node.js API. The closest browser equivalent is `queueMicrotask` (or `Promise.resolve().then`). Bundlers do not add `process` to browser code by default anymore, so code that depends on it may fail with `process is not defined`.

## 101: What is the main difference between the browser event loop and the Node.js event loop?

Both run JavaScript on one thread with tasks and microtasks, but they are built for different jobs:

- The **browser** event loop is defined in the HTML Standard. It has task queues, a microtask queue and a rendering step (`requestAnimationFrame`, style, layout, paint).
- The **Node.js** event loop comes from libuv. It runs in phases (timers, poll, check, close callbacks and so on), has no rendering, and has extra queues like `process.nextTick` and `setImmediate`.

The rules for promise microtasks are the same in both, since those come from the JavaScript spec.

## 102: How can you see tasks and the main thread in Chrome DevTools?

Open DevTools, go to the **Performance** panel, click record, use the page, then stop. In the **Main** track you will see:

- grey **Task** bars, one per event loop task,
- inside them, the functions that ran (yellow is scripting, purple is style and layout, green is paint),
- a red corner on tasks that took longer than 50 ms.

The **Interactions** track shows clicks and key presses with how long each one took to get to the next paint.

## 103: Is console.log asynchronous?

`console.log` itself runs synchronously. But in Chrome DevTools, objects you log are shown by reference: when you expand an object in the console, you see its current values, not the values at the time of logging.

```js
const user = { name: "Ann" };
console.log(user);
user.name = "Bob";
// When you expand the logged object later, it may show name: "Bob"
```

To log a snapshot, log a copy: `console.log(structuredClone(user))` or `JSON.stringify(user)`.

## 104: What is the difference between synchronous and asynchronous code?

- **Synchronous** code runs line by line. Each line finishes before the next starts, and the thread waits for it.
- **Asynchronous** code starts something and lets the rest of the program continue. The result comes later through a callback, an event or a promise.

```js
console.log("sync 1");
setTimeout(() => console.log("async"), 0);
console.log("sync 2");

// sync 1
// sync 2
// async
```

## 105: What does non-blocking I/O mean in the browser?

It means that input/output operations like network requests, reading files with `FileReader` or `Blob.text()`, or `IndexedDB` queries do not freeze the main thread while they wait. The browser does the waiting elsewhere and notifies your code later through the event loop.

The few blocking exceptions, like synchronous XHR, `alert()` and `localStorage`, should be used carefully or avoided.

## 106: Can setTimeout take a string instead of a function?

Yes, for historical reasons. The string is evaluated as code, similar to `eval`.

```js
setTimeout("console.log('hi')", 100); // works, but avoid it
```

You should avoid this. It is slower, harder to debug, and it is blocked by a Content Security Policy that does not allow `unsafe-eval`. Always pass a function.

## 107: How do you pass arguments to a setTimeout callback?

Any arguments after the delay are passed to the callback:

```js
function greet(name, punctuation) {
  console.log(`Hello, ${name}${punctuation}`);
}

setTimeout(greet, 500, "Ann", "!"); // Hello, Ann!
```

You can also use an arrow function: `setTimeout(() => greet("Ann", "!"), 500)`.

## 108: What is this inside a setTimeout callback?

With a regular function, `this` is the global object (`window`) in non-strict code. In strict mode and in modules it is still `window` for timers called from a window, because the browser calls the callback with the global object as `this`. Either way, it is not the object you probably expect.

```js
const counter = {
  count: 0,
  start() {
    setTimeout(function () {
      console.log(this === counter); // false
    }, 0);
    setTimeout(() => {
      console.log(this === counter); // true, arrow functions keep this
    }, 0);
  },
};

counter.start();
```

Use an arrow function or `bind` to keep `this`.

## 109: What happens if you pass a negative number or NaN as the delay?

It is treated as `0`. The browser converts the delay to a number, and anything negative or not a number becomes 0.

```js
setTimeout(() => console.log("runs soon"), -1000);
setTimeout(() => console.log("also runs soon"), "abc");
```

## 110: What is the maximum delay for setTimeout?

The delay is stored as a signed 32-bit integer, so the maximum is 2,147,483,647 ms (about 24.8 days). If you pass a bigger number, it overflows and the timer fires almost immediately.

```js
setTimeout(() => console.log("fires right away!"), 2 ** 31);
```

For very long waits, store the target time and check it with shorter timers.

## 111: What is the output of this code?

```js
console.log("1");

setTimeout(() => console.log("2"), 0);

new Promise((resolve) => {
  console.log("3");
  resolve();
  console.log("4");
}).then(() => console.log("5"));

console.log("6");
```

Output:

```text
1
3
4
6
5
2
```

The promise executor runs synchronously, so `3` and `4` print right away (calling `resolve()` does not stop the executor). `5` is a microtask and `2` is a task.

## 112: What happens when you await a value that is not a promise?

The value is wrapped in a resolved promise, and the function still pauses until the next microtask checkpoint.

```js
async function test() {
  console.log("before");
  const x = await 42;
  console.log("after", x);
}

test();
console.log("outside");

// before
// outside
// after 42
```

So `await` always makes the rest of the function asynchronous, even for plain values.

## 113: What are jobs in ECMAScript?

"Job" is the JavaScript spec's word for work that must run later, when no other JavaScript is running. Promise reactions are jobs. The JavaScript spec does not say how to schedule them; it asks the host to do it.

In browsers, the HTML spec puts promise jobs into the microtask queue. So when someone says "job queue" in a JavaScript context, it usually means the microtask queue.

## 114: What is printed by this code?

```js
async function a() {
  console.log("a start");
  await b();
  console.log("a end");
}

async function b() {
  console.log("b");
}

console.log("script start");
a();
console.log("script end");
```

Output:

```text
script start
a start
b
script end
a end
```

`a` runs synchronously until `await`. `b()` runs right away and prints `b`. Then `a` pauses, `script end` prints, and `a end` runs as a microtask.

## 115: What is a task source?

A task source is a category of tasks. Examples from the HTML spec:

- DOM manipulation task source
- User interaction task source
- Networking task source
- History traversal task source
- Timer task source

Tasks from the same source always run in the order they were queued. Tasks from different sources can be reordered by the browser, which lets it prioritize, for example, input over timers.

## 116: Is there only one task queue?

No. The spec says an event loop has one or more task queues, and each task source is assigned to one of them. The browser picks which queue to take the next task from.

This is why you cannot always predict the exact order between, for example, a `setTimeout` callback and a click event that happen close together. There is only one microtask queue, though, and that one is strictly first-in, first-out.

## 117: What is the "update the rendering" step?

It is the part of the event loop where the browser prepares and draws a new frame. It runs after a task and its microtasks, but only when the browser has a rendering opportunity (usually once per display refresh). It includes, among other steps:

- running resize and scroll events,
- running `requestAnimationFrame` callbacks,
- recalculating styles and layout,
- delivering `ResizeObserver` and `IntersectionObserver` updates,
- painting.

## 118: Does the browser render after every task?

No. Tasks can run many times per frame. The browser only renders when a new frame is due (for example every ~16.7 ms at 60 Hz) and when there is something to update. If you run ten quick tasks in one frame, the screen updates once, after all of them.

On the other hand, if one task takes 200 ms, no frame can be drawn during those 200 ms.

## 119: Does a DOM change appear on screen right away?

No. The DOM is updated immediately in memory, so reading it back gives you the new value. But the screen is only updated in the next rendering step, after your current code and microtasks finish.

```js
box.textContent = "Loading...";
doHeavyWorkFor2Seconds();
box.textContent = "Done";
// The user never sees "Loading...", only "Done"
```

To show "Loading..." first, yield to the browser before starting the heavy work.

## 120: Why does changing a style twice in the same task only show the last value?

Because the browser does not render in the middle of a task. It only looks at the final state when it renders the next frame.

```js
box.style.background = "red";
box.style.background = "blue";
// The user only sees blue. Red never gets painted.
```

This is also why adding an element and a class that starts a CSS transition in the same task often does not animate: the browser never saw the starting state.

## 121: What is layout (reflow)?

Layout is the step where the browser calculates the position and size of every element on the page, based on the DOM and the computed styles. It is also called reflow.

Layout runs during the rendering step. But it can also be forced earlier, in the middle of your JavaScript, if you read a layout value (like `offsetHeight`) after changing the DOM.

## 122: What is a forced synchronous layout?

It happens when your code changes the DOM or styles and then reads a value that depends on layout. The browser has to run layout right away, in the middle of your script, to give you a correct answer.

```js
element.style.width = "300px"; // change
const h = element.offsetHeight; // read: forces layout now
```

Once is fine. Doing it in a loop (write, read, write, read) is called layout thrashing and can be very slow.

## 123: Which DOM properties and methods force layout when you read them?

Common ones:

- `offsetWidth`, `offsetHeight`, `offsetTop`, `offsetLeft`
- `clientWidth`, `clientHeight`, `clientTop`, `clientLeft`
- `scrollWidth`, `scrollHeight`, `scrollTop`, `scrollLeft`
- `getBoundingClientRect()`, `getClientRects()`
- `getComputedStyle()` (for layout-dependent values)
- `innerText`
- `focus()` (it may need to scroll the element into view)

They only force layout if something changed since the last layout. Reading them when nothing changed is cheap.

## 124: How often does the scroll event fire?

In modern browsers, `scroll` events on the page are fired during the rendering step, so they fire at most once per frame, not on every pixel of movement. They are tied to the frame rate.

Even so, scroll handlers run on the main thread and can slow scrolling down if they do heavy work. For many cases, like lazy loading or "sticky" effects, `IntersectionObserver` or CSS (`position: sticky`, scroll-driven animations) is a better choice.

## 125: What is debouncing?

Debouncing delays running a function until some time has passed since the last call. It is useful for things like search inputs, where you want to wait until the user stops typing.

```js
function debounce(fn, delay) {
  let timer;
  return (...args) => {
    clearTimeout(timer);
    timer = setTimeout(() => fn(...args), delay);
  };
}

input.addEventListener(
  "input",
  debounce((e) => search(e.target.value), 300),
);
```

## 126: What is throttling?

Throttling limits how often a function can run, for example at most once every 200 ms, no matter how often it is called.

```js
function throttle(fn, interval) {
  let last = 0;
  return (...args) => {
    const now = Date.now();
    if (now - last >= interval) {
      last = now;
      fn(...args);
    }
  };
}

window.addEventListener("resize", throttle(updateLayout, 200));
```

The difference from debouncing: throttling runs regularly during a burst of calls; debouncing runs only after the burst ends.

## 127: What is ResizeObserver and when does its callback run?

`ResizeObserver` tells you when an element's size changes. Its callback runs during the rendering step, after layout and before paint. That means you can react to the new size and make changes that show up in the same frame.

```js
const observer = new ResizeObserver((entries) => {
  for (const entry of entries) {
    console.log("new width:", entry.contentRect.width);
  }
});

observer.observe(document.querySelector(".panel"));
```

## 128: When does an IntersectionObserver callback run?

The browser checks intersections during the rendering step, after layout. If something changed, it queues a task to call your callback. So the callback runs asynchronously, a little after the element actually entered or left the viewport.

```js
const observer = new IntersectionObserver((entries) => {
  for (const entry of entries) {
    if (entry.isIntersecting) {
      entry.target.src = entry.target.dataset.src;
      observer.unobserve(entry.target);
    }
  }
});

document
  .querySelectorAll("img[data-src]")
  .forEach((img) => observer.observe(img));
```

## 129: What is the visibilitychange event?

It fires on `document` when the page becomes hidden (tab switched, window minimized, phone locked) or visible again. You can check `document.visibilityState`.

```js
document.addEventListener("visibilitychange", () => {
  if (document.visibilityState === "hidden") {
    pauseVideo();
    saveDraft();
  } else {
    resumeVideo();
  }
});
```

It matters for the event loop because hidden pages get their timers throttled and rendering paused.

## 130: What happens to timers when a page goes into the back/forward cache?

When a page is stored in the back/forward cache (bfcache), it is frozen: its tasks, including timers, are paused. If the user comes back with the Back button, the page is restored and paused tasks continue. The `pageshow` event fires with `event.persisted === true`.

```js
window.addEventListener("pageshow", (event) => {
  if (event.persisted) {
    console.log("Restored from bfcache");
    refreshData();
  }
});
```

## 131: Is the abort event of AbortController synchronous?

Yes. When you call `controller.abort()`, the `abort` event on the signal fires synchronously, and its listeners run before `abort()` returns.

```js
const controller = new AbortController();
controller.signal.addEventListener("abort", () => console.log("aborted"));

controller.abort();
console.log("after abort()");

// aborted
// after abort()
```

APIs like `fetch` that use the signal will reject their promise, and the rejection handlers run later as microtasks.

## 132: What is a passive event listener and how does it help?

A passive listener promises that it will not call `preventDefault()`. For `touchstart`, `touchmove` and `wheel`, this lets the browser start scrolling right away on the compositor thread, without waiting for your JavaScript to finish on the main thread.

```js
window.addEventListener("touchmove", onTouchMove, { passive: true });
```

Modern browsers already treat `touchstart`, `touchmove` and `wheel` listeners on `window`, `document` and `body` as passive by default.

## 133: Does the browser give user input priority over other tasks?

Browsers are allowed to, and they do. Since there are several task queues, the browser can choose to run input events before, for example, timer tasks that are also waiting. Chrome's scheduler gives high priority to input.

But this only helps between tasks. If one long task is already running, input still has to wait until it ends.

## 134: What happens if a microtask throws an error?

The error is reported (as with any uncaught error) and the other microtasks in the queue still run. For a promise callback, the error does not show up as a global error. It rejects the promise returned by `then`, and if nobody handles that rejection, you get an `unhandledrejection` event.

```js
queueMicrotask(() => {
  throw new Error("Bad microtask"); // reported as an uncaught error
});

queueMicrotask(() => console.log("still runs"));
```

## 135: When does a finally callback run?

`finally` runs as a microtask after the promise settles, whether it was fulfilled or rejected. It gets no arguments, and it passes the original result or error along, unless it throws or returns a rejected promise itself.

```js
setLoading(true);

fetch("/api/data")
  .then((res) => res.json())
  .then(render)
  .catch(showError)
  .finally(() => setLoading(false));
```

## 136: What is the argument passed to a requestAnimationFrame callback?

A `DOMHighResTimeStamp`: the time in milliseconds (same clock as `performance.now()`) that marks the start of the current frame. All rAF callbacks in the same frame get the same timestamp.

```js
let start;

function animate(timestamp) {
  if (start === undefined) start = timestamp;
  const elapsed = timestamp - start;
  box.style.transform = `translateX(${Math.min(elapsed / 5, 300)}px)`;
  if (elapsed < 1500) requestAnimationFrame(animate);
}

requestAnimationFrame(animate);
```

Using the elapsed time instead of "move 2px per frame" makes the speed the same on 60 Hz and 120 Hz screens.

## 137: Can you stop the event loop from JavaScript?

There is no API to stop it. But an endless synchronous loop, like `while (true) {}`, keeps the current task running forever. The event loop never gets a chance to continue, so the page is frozen until the browser kills the script or the tab.

```js
while (true) {} // freezes the tab
```

## 138: What does the "Page Unresponsive" dialog mean?

The browser shows it when the main thread has been busy for a long time (several seconds) without returning to the event loop. Usually this is an infinite loop, an endless chain of microtasks or a very heavy calculation. The user can wait or kill the page.

Seeing this dialog means some task is far too long and should be split up or moved to a worker.

## 139: What is a dropped frame?

A dropped frame is a frame the browser should have drawn but could not, usually because the main thread was busy. The screen keeps showing the old frame, and animations look like they skip or stutter.

DevTools shows frames in the **Frames** track of the Performance panel. Dropped or partially presented frames are marked there.

## 140: Is JSON.parse blocking?

Yes. `JSON.parse` and `JSON.stringify` are synchronous and run on the thread that calls them. For small data this does not matter, but parsing tens of megabytes can take hundreds of milliseconds and freeze the page.

For big data you can parse it in a Web Worker, request smaller pieces from the server or use streaming formats like NDJSON.

## 141: Is postMessage free?

No. The data is copied using the structured clone algorithm. Serializing on one side and deserializing on the other takes time on both threads, and for big objects it can be slow enough to cause jank.

You can reduce the cost by sending less data, sending `ArrayBuffer`s as transferables (moved instead of copied) or using `SharedArrayBuffer` when the page is cross-origin isolated.

## 142: How do frameworks like Vue use microtasks?

Vue batches DOM updates. When you change reactive state, Vue does not update the DOM right away. It queues an update job and flushes the queue in a microtask. So many changes in the same synchronous code lead to only one DOM update.

```js
import { nextTick } from "vue";

count.value++;
count.value++;
// DOM is not updated yet
await nextTick();
// DOM is updated now
```

`nextTick` gives you a promise that resolves after that flush.

## 143: How are steps in a promise chain scheduled?

Each `then` in a chain runs as a separate microtask, one after another. The next step is only queued after the previous one returns.

```js
Promise.resolve(1)
  .then((x) => x + 1)
  .then((x) => x * 2)
  .then((x) => console.log(x)); // 4
```

All three steps still run before the next task, since they are microtasks.

## 144: If several then callbacks are attached to the same promise, in what order do they run?

In the order they were attached.

```js
const p = Promise.resolve();

p.then(() => console.log("first"));
p.then(() => console.log("second"));
p.then(() => console.log("third"));

// first
// second
// third
```

## 145: In what order do event listeners on the same element run?

In the order they were added, within the same phase (capture or bubble). Listeners in the capture phase run before those in the bubble phase.

```js
button.addEventListener("click", () => console.log("A"));
button.addEventListener("click", () => console.log("B"));
// Click: A, then B
```

`stopImmediatePropagation()` in one listener stops the remaining listeners on the same element.

## 146: What does the once option of addEventListener do?

It makes the listener run at most one time. After the first call, the browser removes it.

```js
button.addEventListener("click", () => console.log("only once"), {
  once: true,
});
```

It saves you from calling `removeEventListener` yourself, and it is useful for one-time setup or waiting for a single event.

## 147: How do you repeat code with setTimeout instead of setInterval?

Schedule the next timeout at the end of each run:

```js
function poll() {
  checkForUpdates();
  setTimeout(poll, 5000);
}

setTimeout(poll, 5000);
```

This guarantees a gap of at least 5 seconds between the end of one run and the start of the next. With `setInterval`, a slow callback could make runs happen back to back.

## 148: Does a Service Worker run on the main thread?

No. A Service Worker runs on its own thread with its own event loop, separate from any page. It sits between the page and the network and can handle `fetch`, `push` and `sync` events even when no page is open.

It is also short-lived. The browser can stop it when it is idle and start it again when the next event arrives, so you cannot keep state in global variables reliably.

## 149: Is localStorage synchronous?

Yes. `localStorage.getItem` and `setItem` are synchronous and run on the main thread. Usually they are fast, but they may need disk access, and storing or reading large values can block the page.

For large data or frequent writes, use `IndexedDB`, which is asynchronous.

## 150: What are common beginner mistakes about the event loop?

- Thinking `setTimeout(fn, 0)` runs `fn` immediately.
- Thinking `async` code runs in parallel.
- Thinking the DOM change is visible on screen right after you set it.
- Wrapping an async call in `try/catch` without `await` and expecting it to catch errors.
- Using `setInterval` for animations instead of `requestAnimationFrame`.
- Doing heavy work inside a click handler and wondering why the button feels slow.
- Using `forEach` with an async callback and expecting it to wait.

# Moderate Questions (151-300)

## 151: What is the output of this code?

```js
console.log("script start");

setTimeout(() => console.log("setTimeout"), 0);

Promise.resolve()
  .then(() => console.log("promise 1"))
  .then(() => console.log("promise 2"));

(async () => {
  console.log("async start");
  await null;
  console.log("async end");
})();

console.log("script end");
```

Output:

```text
script start
async start
script end
promise 1
async end
promise 2
setTimeout
```

The synchronous lines print first. Then the microtask queue holds `promise 1` and the rest of the async function, in that order. Running `promise 1` queues `promise 2`, which goes after `async end`. The timer runs last because it is a task.

## 152: What is printed when promises and timers are nested?

```js
setTimeout(() => {
  console.log("timeout 1");
  Promise.resolve().then(() => console.log("promise in timeout 1"));
}, 0);

setTimeout(() => console.log("timeout 2"), 0);

Promise.resolve().then(() => {
  console.log("promise 1");
  setTimeout(() => console.log("timeout in promise"), 0);
});
```

Output:

```text
promise 1
timeout 1
promise in timeout 1
timeout 2
timeout in promise
```

After each task, all microtasks run. So `promise in timeout 1` runs right after `timeout 1` and before `timeout 2`. The timer created inside `promise 1` was queued after the other two timers.

## 153: What is the output when an async function awaits another async function?

```js
async function first() {
  console.log("first start");
  await second();
  console.log("first end");
}

async function second() {
  console.log("second start");
  await null;
  console.log("second end");
}

first();
Promise.resolve().then(() => console.log("promise"));
console.log("sync");
```

Output:

```text
first start
second start
sync
second end
promise
first end
```

`second` pauses at `await null` and queues its continuation first. Then the `promise` callback is queued. When `second end` runs, `second`'s promise resolves, which queues `first end` after `promise`.

## 154: Can you predict the order between rAF and setTimeout?

Not reliably.

```js
setTimeout(() => console.log("timeout"), 0);
requestAnimationFrame(() => console.log("raf"));
```

It depends on how far the browser is from the next frame. If a frame is due very soon, `raf` can print first. Usually `timeout` prints first, but you should never write code that depends on this order. If you need a fixed order, chain them: schedule one from inside the other.

## 155: How many microtask hops does await take?

For a native promise, `await` takes one hop: the rest of the function is queued as a microtask when the promise settles. This was improved in ES2019. Before that, `await` on a native promise took three hops.

For a non-native "thenable" (an object with a `then` method), there are extra hops, because the engine has to call its `then` method inside a microtask first.

```js
const thenable = {
  then(resolve) {
    resolve("done");
  },
};

async function run() {
  console.log(await thenable); // takes an extra microtask to get the value
}
```

## 156: Why does return await sometimes run sooner than return in an async function?

When an async function does `return somePromise`, the function's own promise has to adopt the state of `somePromise`. That adds two extra microtask hops (one for a job that calls `then` on it and one for that `then` callback). With `return await somePromise`, the value is unwrapped first and returned directly, which takes one hop.

```js
async function a() {
  return Promise.resolve("a");
}
async function b() {
  return await Promise.resolve("b");
}

a().then(console.log);
b().then(console.log);

// b
// a
```

The difference is tiny and rarely matters for speed. What matters more: inside a `try/catch`, `return await` is needed if you want the `catch` to handle a rejection.

## 157: What is the difference between Promise.resolve(p) and wrapping p in a new Promise?

`Promise.resolve(p)` returns `p` itself if it is a native promise of the same constructor. No extra work is done.

`new Promise((r) => r(p))` creates a new promise that follows `p`. Resolving with a thenable schedules a job that calls `p.then`, so the new promise settles two microtasks later than `p`.

```js
const p = Promise.resolve(1);

console.log(Promise.resolve(p) === p); // true
console.log(new Promise((r) => r(p)) === p); // false
```

## 158: How do two independent promise chains interleave?

Each step of a chain is queued only after the previous step runs, so two chains take turns.

```js
Promise.resolve()
  .then(() => console.log("A1"))
  .then(() => console.log("A2"));

Promise.resolve()
  .then(() => console.log("B1"))
  .then(() => console.log("B2"));

// A1
// B1
// A2
// B2
```

At the start the queue holds `A1` and `B1`. Running `A1` queues `A2` at the end, after `B1`, and so on.

## 159: What is microtask starvation?

It happens when microtasks keep adding new microtasks forever. The microtask checkpoint only ends when the queue is empty, so the event loop never gets to handle input, run timers or render. The page freezes, just like with `while (true)`.

```js
function loop() {
  queueMicrotask(loop);
}

loop(); // freezes the page
```

## 160: Why does a recursive setTimeout not freeze the page, but a recursive microtask does?

Each `setTimeout` callback is a separate task. Between tasks, the browser can handle input and render frames. A microtask scheduled from a microtask runs in the same checkpoint, so control never returns to the event loop.

```js
// Page stays responsive
function withTimeout() {
  setTimeout(withTimeout, 0);
}

// Page freezes
function withMicrotask() {
  Promise.resolve().then(withMicrotask);
}
```

The `setTimeout` version still wastes CPU, but the page keeps working.

## 161: What are the problems with setInterval?

- **Drift**: the interval is a minimum, not exact, and delays add up over time.
- **Overlap of work**: if the callback starts async work that takes longer than the interval, new calls start before old ones finish.
- **No backlog**: if the main thread is busy, missed ticks are not all replayed, so you cannot count ticks to measure time.
- **Forgotten intervals**: an interval that is never cleared keeps running and keeps references alive, which is a common memory leak.

A recursive `setTimeout` (or `requestAnimationFrame` for visual updates) is often a better choice.

## 162: How do you build a countdown timer that stays accurate?

Do not count ticks. Store the end time and compute the remaining time from the clock on every update.

```js
function startCountdown(seconds, onTick, onDone) {
  const end = Date.now() + seconds * 1000;

  function update() {
    const remaining = Math.max(0, end - Date.now());
    onTick(Math.ceil(remaining / 1000));
    if (remaining > 0) {
      setTimeout(update, Math.min(remaining, 250));
    } else {
      onDone();
    }
  }

  update();
}
```

Even if timers are delayed or throttled in a background tab, the displayed value is correct once the next update runs.

## 163: What is the difference between performance.now() and Date.now()?

- `Date.now()` gives the wall-clock time in whole milliseconds since 1970. It can jump if the system clock changes.
- `performance.now()` gives milliseconds (with fractions) since the page started (the time origin). It always goes forward and is not affected by system clock changes.

Use `performance.now()` to measure durations, for example how long a task took. Use `Date.now()` when you need a real date and time, like an end time for a countdown that must survive page reloads.

## 164: How do you yield to the main thread with scheduler.yield and a fallback?

```js
function yieldToMain() {
  if (globalThis.scheduler?.yield) {
    return scheduler.yield();
  }
  return new Promise((resolve) => setTimeout(resolve, 0));
}

async function runTasks(tasks) {
  for (const task of tasks) {
    task();
    await yieldToMain();
  }
}
```

`scheduler.yield()` gives the continuation higher priority than other queued work, so your job finishes sooner. The `setTimeout` fallback works everywhere, but the continuation goes to the back of the queue.

## 165: What priorities does scheduler.postTask support?

There are three:

- **user-blocking**: work the user is waiting for right now, like responding to input.
- **user-visible**: the default. Work the user will notice, but not as urgent, like rendering secondary content.
- **background**: work that can wait, like logging or prefetching.

```js
scheduler.postTask(updateSearchResults, { priority: "user-blocking" });
scheduler.postTask(renderSidebar); // user-visible
scheduler.postTask(sendAnalytics, { priority: "background" });
```

You can also pass a `delay` option in milliseconds and a `signal` for cancelling.

## 166: How do you cancel or change the priority of posted tasks?

Use a `TaskController`. Its signal can abort tasks and change their priority.

```js
const controller = new TaskController({ priority: "background" });

scheduler.postTask(prefetchData, { signal: controller.signal }).catch((err) => {
  if (err.name === "AbortError") console.log("cancelled");
});

// The user hovered the link, so make it urgent
controller.setPriority("user-blocking");

// Or cancel it
controller.abort();
```

A plain `AbortController` signal works too if you only need cancelling.

## 167: What does the timeout option of requestIdleCallback do?

It sets a deadline. If the browser has not found idle time within `timeout` milliseconds, it calls your callback anyway, and `deadline.didTimeout` is `true`.

```js
requestIdleCallback(
  (deadline) => {
    if (deadline.didTimeout) {
      console.log("Ran because of timeout, not idle time");
    }
    flushAnalytics();
  },
  { timeout: 2000 },
);
```

Without `timeout`, on a busy page an idle callback might wait a long time.

## 168: What should you avoid doing inside requestIdleCallback?

- **DOM changes**: idle callbacks run after a frame was drawn. If you change the DOM, the browser may need to recalculate layout, which can take longer than the idle time and delay the next frame. Schedule DOM work with `requestAnimationFrame` instead.
- **Resolving promises whose callbacks do heavy work**: those microtasks run right after the idle callback and are not covered by the deadline.
- **Work you cannot split**: if one piece takes longer than `timeRemaining()`, it will overrun.

Idle callbacks are best for small, splittable, non-visual work.

## 169: How do you batch DOM reads and writes?

Do all reads first, then all writes. This way the browser only needs one layout.

```js
// Bad: read, write, read, write... forces layout on every read
for (const item of items) {
  const width = item.offsetWidth;
  item.style.height = `${width / 2}px`;
}

// Good: read everything, then write everything
const widths = items.map((item) => item.offsetWidth);
items.forEach((item, i) => {
  item.style.height = `${widths[i] / 2}px`;
});
```

## 170: What is layout thrashing and how do you find it?

Layout thrashing is when code repeatedly writes to the DOM and then reads a layout value, forcing the browser to recompute layout again and again in one task.

In the Chrome DevTools Performance panel, look for many purple **Layout** blocks inside one task, often with a warning "Forced reflow is a likely performance bottleneck". Clicking one shows the line of JavaScript that triggered it. The fix is to separate reads and writes, cache values or use `ResizeObserver` instead of reading sizes in a loop.

## 171: What is the double requestAnimationFrame trick?

Calling `requestAnimationFrame` inside a `requestAnimationFrame` callback runs your code in the next frame, after the current one was rendered.

```js
element.classList.add("start-state");

requestAnimationFrame(() => {
  requestAnimationFrame(() => {
    element.classList.add("end-state"); // the transition now runs
  });
});
```

The first callback runs before the browser renders the start state. The second one runs after that frame, so the browser has already seen the start state and can animate to the end state. It is often used for CSS transitions on newly added elements.

## 172: How do you run code right after the browser paints a frame?

There is no direct "after paint" callback, but a common pattern is to schedule a task from inside `requestAnimationFrame`. rAF runs right before rendering, and the task runs after rendering is done.

```js
function afterNextPaint(callback) {
  requestAnimationFrame(() => {
    setTimeout(callback, 0);
  });
}

afterNextPaint(() => {
  console.log("The frame with my changes has been rendered");
});
```

A `MessageChannel` message can be used instead of `setTimeout` to avoid timer clamping. This pattern is also used to measure how long an update took to reach the screen.

## 173: Why do some libraries use MessageChannel instead of setTimeout(fn, 0)?

Because nested `setTimeout` calls get clamped to at least 4 ms after a few levels, and timers can be throttled in other ways. A message on a `MessageChannel` is a regular task with no minimum delay.

```js
const channel = new MessageChannel();
const queue = [];

channel.port1.onmessage = () => {
  const fn = queue.shift();
  fn?.();
};

function postTaskFallback(fn) {
  queue.push(fn);
  channel.port2.postMessage(null);
}
```

React's scheduler uses this approach in the browser to run its work loop in small chunks.

## 174: How does React's scheduler use the event loop?

React's scheduler package splits rendering work into small units. It runs work in a loop and checks after each unit whether it has been running for more than about 5 ms. If so, it stops and posts a new task (using `MessageChannel` in browsers) to continue later.

This lets the browser handle input and paint between chunks. It is how concurrent features like `startTransition` keep the page responsive during large re-renders.

## 175: How did Angular use Zone.js to know when to update, and what changed?

Zone.js patches browser async APIs (`setTimeout`, `addEventListener`, promises, `fetch` and so on). When any async callback finishes, Zone.js tells Angular, and Angular runs change detection to update the view. It works but runs change detection more often than needed and adds overhead.

Modern Angular can run without Zone.js ("zoneless"). Updates are scheduled when signals change, when template event handlers run or when `markForCheck` is called. Zoneless change detection is the default for new projects from Angular 21.

## 176: How do you write a debounce that can be cancelled and flushed?

```js
function debounce(fn, delay) {
  let timer = null;
  let lastArgs;

  function debounced(...args) {
    lastArgs = args;
    clearTimeout(timer);
    timer = setTimeout(() => {
      timer = null;
      fn(...lastArgs);
    }, delay);
  }

  debounced.cancel = () => {
    clearTimeout(timer);
    timer = null;
  };

  debounced.flush = () => {
    if (timer !== null) {
      debounced.cancel();
      fn(...lastArgs);
    }
  };

  return debounced;
}
```

`cancel` is useful when a component is removed. `flush` is useful when you need the latest value saved right now, for example before the page is hidden.

## 177: How do you throttle with requestAnimationFrame?

Run the handler at most once per frame. This is a good fit for `pointermove`, `scroll` or `resize` handlers that update the screen.

```js
function rafThrottle(fn) {
  let scheduled = false;
  let lastArgs;

  return (...args) => {
    lastArgs = args;
    if (scheduled) return;
    scheduled = true;
    requestAnimationFrame(() => {
      scheduled = false;
      fn(...lastArgs);
    });
  };
}

window.addEventListener(
  "pointermove",
  rafThrottle((e) => {
    cursor.style.transform = `translate(${e.clientX}px, ${e.clientY}px)`;
  }),
);
```

You always use the latest event data, and you never do more work than the screen can show.

## 178: What happens if you call preventDefault in a passive listener?

The call is ignored, and the browser logs a warning in the console. The default action (for example scrolling) still happens, because the browser already started it without waiting for your listener.

```js
document.addEventListener(
  "wheel",
  (e) => {
    e.preventDefault(); // ignored, warning in console
  },
  { passive: true },
);
```

If you really need to block scrolling, register the listener with `{ passive: false }` on the specific element, and keep the handler very fast.

## 179: Why doesn't preventDefault work after an await?

Because the event dispatch is already over. The browser decides what to do with the default action right after all listeners return. Code after `await` runs later in a microtask, when it is too late.

```js
form.addEventListener("submit", async (event) => {
  await validate(); // the form has already been submitted by now
  event.preventDefault(); // too late
});

// Correct
form.addEventListener("submit", async (event) => {
  event.preventDefault();
  const ok = await validate();
  if (ok) form.submit();
});
```

The same goes for `stopPropagation()`. Call these synchronously, before any `await`.

## 180: What is user activation and how can await break it?

Some APIs, like opening a popup with `window.open`, starting fullscreen or playing audio with sound, need a recent user gesture (a click or key press). The browser gives the page "transient activation" when the user interacts, and it expires after a short time (a few seconds in most browsers).

```js
button.addEventListener("click", async () => {
  const url = await fetchShareUrl(); // if this takes long, activation may expire
  window.open(url); // can be blocked as a popup
});
```

A common fix is to open the window synchronously first, then set its location when the data arrives.

## 181: Do microtasks run between event listeners?

It depends on how the event was dispatched.

- For a real user click, each listener is called by the browser with an empty JavaScript stack. After each listener, a microtask checkpoint runs.
- For `element.click()` or `dispatchEvent()` called from your code, the listeners run inside your script, so the stack is not empty and microtasks wait until your script finishes.

```js
button.addEventListener("click", () => {
  Promise.resolve().then(() => console.log("micro 1"));
  console.log("listener 1");
});
button.addEventListener("click", () => {
  Promise.resolve().then(() => console.log("micro 2"));
  console.log("listener 2");
});

// Real click:       listener 1, micro 1, listener 2, micro 2
// button.click():   listener 1, listener 2, micro 1, micro 2
```

## 182: What is printed when dispatching a custom event between promises?

```js
const target = new EventTarget();
target.addEventListener("ping", () => console.log("listener"));

Promise.resolve().then(() => console.log("microtask"));

console.log("before dispatch");
target.dispatchEvent(new Event("ping"));
console.log("after dispatch");
```

Output:

```text
before dispatch
listener
after dispatch
microtask
```

`dispatchEvent` is synchronous, so the listener runs inside the script. The microtask waits until the script is done.

## 183: How do you use custom events to decouple parts of an app, and what should you watch out for?

You can dispatch `CustomEvent`s with data on `document`, `window` or any `EventTarget`:

```js
const bus = new EventTarget();

bus.addEventListener("cart:updated", (e) => {
  renderCartBadge(e.detail.count);
});

bus.dispatchEvent(new CustomEvent("cart:updated", { detail: { count: 3 } }));
```

Things to watch:

- Dispatch is synchronous, so a slow listener slows down the code that dispatched the event.
- An error in a listener is reported but does not reach the dispatcher's `try/catch`.
- If you want async delivery, wrap the dispatch in `queueMicrotask` or a task.

## 184: When is the unhandledrejection event fired?

After a microtask checkpoint finishes, the browser looks at promises that were rejected without a handler during that time. For each one that still has no handler, it queues a task to fire `unhandledrejection`.

So a rejection is not "unhandled" just because it has no handler at the moment it rejects. You can still attach a handler later in the same synchronous code or in a following microtask. If you attach one after the event fired, the browser fires `rejectionhandled`.

```js
const p = Promise.reject(new Error("late"));

setTimeout(() => {
  p.catch(() => console.log("handled late"));
}, 0);

window.addEventListener("rejectionhandled", () => {
  console.log("rejectionhandled fired");
});
```

## 185: What is reportError?

`reportError(error)` reports an error to the global error handlers (`window.onerror` and the `error` event) and the console, as if it was uncaught, without stopping your code.

```js
for (const listener of listeners) {
  try {
    listener(data);
  } catch (err) {
    reportError(err); // log it, keep going with the other listeners
  }
}
```

It is useful in your own event or callback systems, so one broken callback does not stop the others but its error is still visible.

## 186: What are async stack traces in DevTools?

Normally the call stack only shows the functions in the current task. Async stack traces let DevTools show where an async callback was scheduled: which code called `setTimeout`, `then`, `addEventListener` or `await`.

In Chrome DevTools, the Sources panel's call stack shows these as extra frames separated by labels like "setTimeout" or "await". This helps a lot when debugging code that jumps across many tasks and microtasks. Native `async/await` gives better async stack traces than hand-written promise chains.

## 187: How do you detect long tasks in production?

Use a `PerformanceObserver` with the `longtask` type and send the data to your analytics:

```js
const observer = new PerformanceObserver((list) => {
  for (const entry of list.getEntries()) {
    sendToAnalytics({
      type: "longtask",
      duration: Math.round(entry.duration),
      startTime: Math.round(entry.startTime),
    });
  }
});

observer.observe({ type: "longtask", buffered: true });
```

The Long Tasks API tells you that a long task happened but not much about why. The newer Long Animation Frames API gives much better details (see the next question). Both are supported mainly in Chromium browsers.

## 188: What is the Long Animation Frames (LoAF) API?

It reports frames where the time from the start of work to the frame being rendered took more than 50 ms. Unlike the Long Tasks API, it includes rendering work and gives details about which scripts ran.

```js
new PerformanceObserver((list) => {
  for (const entry of list.getEntries()) {
    console.log("Frame duration:", entry.duration);
    console.log("Blocking duration:", entry.blockingDuration);
    for (const script of entry.scripts) {
      console.log(script.invoker, script.sourceURL, script.duration);
    }
  }
}).observe({ type: "long-animation-frame", buffered: true });
```

It is available in Chromium browsers (since Chrome 123) and is very useful for finding what causes poor INP.

## 189: How do you measure interaction latency in code?

Use the Event Timing API. Each entry tells you when the event started, when processing started and ended, and the total time until the next frame was presented.

```js
new PerformanceObserver((list) => {
  for (const entry of list.getEntries()) {
    if (!entry.interactionId) continue;
    const inputDelay = entry.processingStart - entry.startTime;
    const processing = entry.processingEnd - entry.processingStart;
    const presentation = entry.startTime + entry.duration - entry.processingEnd;
    console.log(entry.name, { inputDelay, processing, presentation });
  }
}).observe({ type: "event", durationThreshold: 16, buffered: true });
```

In practice most teams use the `web-vitals` library (`onINP`), which handles the details of grouping events into interactions.

## 190: How do you process a big array without blocking, using a time budget?

Instead of a fixed chunk size, work until a time budget is used up, then yield.

```js
async function processWithBudget(items, handle, budgetMs = 8) {
  let i = 0;
  while (i < items.length) {
    const start = performance.now();
    while (i < items.length && performance.now() - start < budgetMs) {
      handle(items[i++]);
    }
    if (i < items.length) {
      await new Promise((resolve) => setTimeout(resolve, 0));
    }
  }
}
```

This adapts to fast and slow devices. On a fast machine, each chunk handles many items; on a slow one, fewer.

## 191: What is navigator.scheduling.isInputPending?

It is a Chromium-only method that tells you whether there is user input waiting to be handled. The idea was to keep working until the user does something and only then yield.

```js
while (work.length > 0) {
  if (navigator.scheduling?.isInputPending()) {
    await yieldToMain();
  }
  doUnitOfWork(work.shift());
}
```

The Chrome team no longer recommends it. Pending input is not the only reason to yield (rendering also needs time), and `scheduler.yield()` covers the same need in a simpler way. Prefer yielding regularly, for example every ~50 ms or less.

## 192: How do you move heavy work to a Web Worker with a promise-based API?

Wrap the message exchange in a promise, and use an id so you can match responses to requests.

```js
// main.js
const worker = new Worker(new URL("./worker.js", import.meta.url), {
  type: "module",
});
let nextId = 0;
const pending = new Map();

worker.onmessage = (e) => {
  const { id, result } = e.data;
  pending.get(id)?.(result);
  pending.delete(id);
};

function runInWorker(payload) {
  return new Promise((resolve) => {
    const id = nextId++;
    pending.set(id, resolve);
    worker.postMessage({ id, payload });
  });
}

const sorted = await runInWorker(bigArray);

// worker.js
self.onmessage = (e) => {
  const { id, payload } = e.data;
  const result = payload.toSorted((a, b) => a - b);
  self.postMessage({ id, result });
};
```

Libraries like Comlink do this for you.

## 193: What are transferable objects?

Transferable objects can be moved between threads instead of copied. After transfer, the sender cannot use them anymore. Examples: `ArrayBuffer`, `MessagePort`, `ImageBitmap`, `OffscreenCanvas`, `ReadableStream`.

```js
const pixels = new Uint8ClampedArray(4 * 1920 * 1080);
worker.postMessage({ pixels }, [pixels.buffer]);
console.log(pixels.byteLength); // 0, ownership moved to the worker
```

Transfer is almost free regardless of size, while copying tens of megabytes can take long enough to cause jank on both threads.

## 194: How does a worker's event loop differ from a window's event loop?

- It has no rendering step: no style, layout or paint.
- It has no DOM, so no DOM events or `MutationObserver`.
- It still has tasks (`message` events, timers, network events) and its own microtask queue.
- Dedicated workers can use `requestAnimationFrame` in Chromium and Firefox, mainly to draw with `OffscreenCanvas` in sync with the display.
- A dedicated worker lives as long as its page (or until `terminate()`); a service worker can be stopped by the browser when idle.

## 195: When is a Web Worker not worth it?

- The work is small (a few milliseconds). Starting a worker and copying data back and forth can cost more than the work itself.
- The work needs the DOM a lot. Workers cannot touch the DOM, so you would send messages back and forth for every change.
- The data is huge and cannot be transferred. Copying it with structured clone may block for as long as the work you saved.

Workers shine for CPU-heavy, self-contained work like parsing, compression, image processing, search indexing or data crunching.

## 196: How does a Service Worker's event loop and lifetime affect your code?

A service worker wakes up for an event (`fetch`, `push`, `message`, `sync`), runs its handler and then can be stopped by the browser when idle, sometimes after only about 30 seconds.

To keep it alive until async work finishes, pass a promise to `event.waitUntil()` or `event.respondWith()`:

```js
self.addEventListener("push", (event) => {
  event.waitUntil(
    (async () => {
      const data = event.data.json();
      await self.registration.showNotification(data.title, { body: data.body });
    })(),
  );
});
```

Without `waitUntil`, the browser may stop the worker before your `await` finishes. Global variables are also lost when it stops.

## 197: How exactly are timers throttled in background tabs?

Details differ by browser, but in Chrome:

- **Hidden pages**: timers are aligned to run at most once per second.
- **Intensive throttling**: if the page has been hidden for 5 minutes, the timer chain is deep (a timer scheduled from a timer, 5 or more levels), the page has been silent for at least 30 seconds and it is not using WebRTC, wake-ups are limited to once per minute.
- **Offscreen cross-origin iframes** can also have their timers and rendering throttled.

Firefox and Safari have similar rules. Code that must stay accurate should use timestamps and not assume timers fire on time.

## 198: How can you keep work going when the tab is in the background?

You mostly should not rely on it, but options exist:

- Do the work on the server and push results when the user comes back.
- Move the logic into a Web Worker. Worker timers are often throttled less, but browsers can still limit them.
- Use a Service Worker for things like push notifications and background sync.
- On `visibilitychange` to visible, catch up: compare timestamps and refresh data.

Playing audio or using WebRTC also keeps pages from heavy throttling, but you should not use them just as a trick.

## 199: What is the Page Lifecycle API (freeze and resume)?

In Chromium, the browser can freeze a background tab to save resources. While frozen, no tasks run at all: no timers, no fetch callbacks. It fires `freeze` before and `resume` after.

```js
document.addEventListener("freeze", () => {
  // Save state, close connections
  saveState();
});

document.addEventListener("resume", () => {
  // Reopen connections, refresh data
  reconnect();
});
```

The browser can also discard a frozen tab completely to free memory. When the user returns, the page reloads and `document.wasDiscarded` is `true`.

## 200: How does reading a fetch response body work with the event loop?

The body comes in chunks over time. Each chunk that arrives is delivered through the stream, and when you read the stream with `await reader.read()`, each read resolves as a promise.

```js
const res = await fetch("/large-file");
const reader = res.body.getReader();
let received = 0;

while (true) {
  const { done, value } = await reader.read();
  if (done) break;
  received += value.length;
  progress.textContent = `${received} bytes`;
}
```

Because chunks arrive from the network in separate tasks, the page has chances to render between them, so a progress display like this can update while the download continues.

## 201: When does fetch reject after you call abort()?

When you call `controller.abort()`, the `abort` event fires synchronously, and the fetch promise is rejected right away with an `AbortError` (or with the reason you passed to `abort`). Your `catch` handler runs as a microtask after the current code.

```js
const controller = new AbortController();

fetch("/api/search?q=a", { signal: controller.signal })
  .then((res) => res.json())
  .catch((err) => {
    if (err.name === "AbortError") console.log("request cancelled");
  });

controller.abort();
console.log("abort called");

// abort called
// request cancelled
```

If the response already arrived and you are reading the body, the body read is aborted too.

## 202: How do you add a timeout to a promise without leaking timers?

Use `AbortSignal.timeout()` for APIs that take a signal, like `fetch`:

```js
const res = await fetch("/api/data", { signal: AbortSignal.timeout(5000) });
```

For other promises, race them against a timer and clear the timer when done:

```js
function withTimeout(promise, ms) {
  let timer;
  const timeout = new Promise((_, reject) => {
    timer = setTimeout(() => reject(new Error("Timed out")), ms);
  });
  return Promise.race([promise, timeout]).finally(() => clearTimeout(timer));
}
```

Without `clearTimeout`, the timer keeps running after the promise settles. Note that `Promise.race` does not stop the original work; it just stops waiting for it.

## 203: How do Promise.all, allSettled, any and race differ, and do they change the timing?

- `Promise.all`: fulfills when all fulfill; rejects as soon as one rejects.
- `Promise.allSettled`: waits for all to settle and gives you each result or error.
- `Promise.any`: fulfills with the first fulfilled value; rejects with an `AggregateError` if all reject.
- `Promise.race`: settles like the first one to settle.

None of them start or speed up any work. They only decide when to settle based on the input promises, and their callbacks run as microtasks like any other promise.

## 204: How does for await...of work with the event loop?

`for await` calls the async iterator's `next()` method and awaits each result. Each iteration takes at least one microtask hop, and if the values come from the network or a timer, the loop waits for those tasks.

```js
async function* numbers() {
  for (let i = 0; i < 3; i++) {
    await new Promise((r) => setTimeout(r, 100));
    yield i;
  }
}

for await (const n of numbers()) {
  console.log(n); // 0, 1, 2 with 100 ms gaps
}
```

If the async generator never awaits anything slow, the whole loop runs in microtasks and does not yield to rendering.

## 205: What is the difference between awaiting in sequence and in parallel?

```js
// Sequential: total time = time(a) + time(b)
const a = await fetchUser();
const b = await fetchPosts();

// Parallel: total time = max(time(a), time(b))
const [user, posts] = await Promise.all([fetchUser(), fetchPosts()]);
```

In the sequential version, the second request does not start until the first one finishes. Start independent requests first, then await them together.

## 206: Why does forEach with an async callback not wait?

`forEach` calls the callback and ignores its return value. An async callback returns a promise, which `forEach` throws away, so the loop finishes immediately.

```js
// Does not wait
items.forEach(async (item) => {
  await save(item);
});
console.log("done?"); // prints before the saves finish

// Sequential
for (const item of items) {
  await save(item);
}

// Parallel
await Promise.all(items.map((item) => save(item)));
```

## 207: How do you limit how many async operations run at once?

Use a small pool: start up to N operations, and each time one finishes, start the next.

```js
async function mapWithLimit(items, limit, fn) {
  const results = new Array(items.length);
  let next = 0;

  async function worker() {
    while (next < items.length) {
      const index = next++;
      results[index] = await fn(items[index]);
    }
  }

  await Promise.all(
    Array.from({ length: Math.min(limit, items.length) }, worker),
  );
  return results;
}

const pages = await mapWithLimit(urls, 4, (url) =>
  fetch(url).then((r) => r.text()),
);
```

The `next++` is safe without locks because JavaScript on one thread never runs two pieces of code at the same moment.

## 208: Why doesn't a loading spinner appear during heavy synchronous work?

Because the browser cannot render while your code is running. Showing the spinner and doing the work in the same task means the spinner is added to the DOM but never painted before the work ends.

```js
// Spinner never shows
spinner.hidden = false;
heavyComputation();
spinner.hidden = true;

// Spinner shows: let the browser paint first
spinner.hidden = false;
await new Promise((r) => requestAnimationFrame(() => setTimeout(r, 0)));
heavyComputation();
spinner.hidden = true;
```

Even then, an animated spinner may freeze during the work unless it is a compositor-only animation (`transform`). Better: split the work or move it to a worker.

## 209: How do you update a progress bar during a long loop?

Split the loop and yield between chunks so the browser can paint the new progress.

```js
async function processAll(items) {
  for (let i = 0; i < items.length; i++) {
    process(items[i]);

    if (i % 500 === 0) {
      progress.value = i / items.length;
      await yieldToMain();
    }
  }
  progress.value = 1;
}
```

Updating `progress.value` without yielding changes the DOM but nothing is drawn until the loop ends.

## 210: How do you make an animation run at the same speed on 60 Hz and 120 Hz screens?

Base the movement on elapsed time, not on the number of frames.

```js
const speed = 200; // pixels per second
let x = 0;
let last;

function frame(now) {
  if (last !== undefined) {
    const dt = (now - last) / 1000; // seconds since last frame
    x += speed * dt;
    ball.style.transform = `translateX(${x}px)`;
  }
  last = now;
  requestAnimationFrame(frame);
}

requestAnimationFrame(frame);
```

On a 120 Hz screen, rAF runs twice as often, but `dt` is half as big, so the speed is the same.

## 211: Why doesn't a CSS transition run when you add an element and its class in the same task?

The browser only computes styles when needed. If you add an element and immediately add the class that sets the final value, the browser never computes the starting style, so there is nothing to transition from.

```css
.panel {
  opacity: 0;
  transition: opacity 0.3s;
}
.panel.visible {
  opacity: 1;
}
```

```js
const panel = document.createElement("div");
panel.className = "panel";
document.body.append(panel);

// Option 1: force a style calculation
panel.getBoundingClientRect();
panel.classList.add("visible");

// Option 2: wait for the next frame (double rAF)
```

The Web Animations API (`element.animate()`) or CSS `@starting-style` avoid this problem.

## 212: What is @starting-style and how does it help with entry transitions?

`@starting-style` lets you define the style an element starts from on its first style update. The browser uses it as the "before" state, so the transition runs without any JavaScript timing tricks.

```css
.toast {
  opacity: 1;
  transition: opacity 0.3s;

  @starting-style {
    opacity: 0;
  }
}
```

Now you can add the element in any task and it fades in. It is supported in current versions of all major browsers.

## 213: Does the Web Animations API run on the main thread?

`element.animate()` creates an animation managed by the browser. If it only animates `transform`, `opacity` or a few other compositor-friendly properties, the browser can run it on the compositor thread, so it stays smooth even if JavaScript is busy.

```js
box.animate(
  [{ transform: "translateX(0)" }, { transform: "translateX(300px)" }],
  { duration: 1000, easing: "ease-in-out", fill: "forwards" },
);
```

If you animate layout properties like `width` or `left`, each frame needs main thread work, just like a JavaScript animation.

## 214: What are scroll-driven animations and why are they better than scroll listeners?

Scroll-driven animations link a CSS animation to the scroll position, using `animation-timeline: scroll()` or `view()`. The browser can run them on the compositor, so they stay in sync with scrolling without any JavaScript.

```css
.progress-bar {
  transform-origin: left;
  animation: grow linear;
  animation-timeline: scroll();
}

@keyframes grow {
  from {
    transform: scaleX(0);
  }
  to {
    transform: scaleX(1);
  }
}
```

A JavaScript scroll listener runs on the main thread and can lag behind scrolling if the thread is busy. Scroll-driven animations are supported in Chromium and Safari 26; Firefox support is still in progress, so add a fallback.

## 215: What does the "ResizeObserver loop completed with undelivered notifications" error mean?

It means a `ResizeObserver` callback changed the size of an observed element in a way that would need another round of notifications, and the browser stopped to avoid an infinite loop. The remaining notifications are delivered in the next frame.

```js
const ro = new ResizeObserver(([entry]) => {
  // Changing the observed element's size from inside the callback
  entry.target.style.height = `${entry.contentRect.width / 2}px`;
});
```

It is often harmless, but it shows the layout is going back and forth. Avoid changing the size of the elements you observe, or move the change to `requestAnimationFrame`.

## 216: Why use IntersectionObserver instead of a scroll handler for lazy loading?

- A scroll handler runs on the main thread during scrolling and usually calls `getBoundingClientRect()`, which can force layout.
- `IntersectionObserver` is computed by the browser during the rendering step, uses the layout it already has and only calls you when visibility changes.

```js
const io = new IntersectionObserver(
  (entries) => {
    for (const entry of entries) {
      if (!entry.isIntersecting) continue;
      loadMore();
    }
  },
  { rootMargin: "500px" }, // start loading before the element is visible
);

io.observe(document.querySelector("#list-end"));
```

For images, `loading="lazy"` does it with no JavaScript at all.

## 217: How does MutationObserver batch changes?

All DOM mutations that happen before the observer's microtask runs are collected into one list of records. If you add 1,000 nodes in a loop, the callback runs once with up to 1,000 records, not 1,000 times.

```js
const mo = new MutationObserver((records) => {
  console.log("records:", records.length);
});

mo.observe(list, { childList: true });

for (let i = 0; i < 1000; i++) {
  list.append(document.createElement("li"));
}
// records: 1000 (one callback)
```

You can also call `mo.takeRecords()` to get pending records synchronously, for example before disconnecting.

## 218: How can a MutationObserver cause an infinite loop?

If the callback changes the same part of the DOM it is watching, it produces new records, which run the callback again in another microtask, and so on. Because these are microtasks, the page freezes.

```js
const mo = new MutationObserver(() => {
  el.setAttribute("data-count", String(Math.random())); // triggers itself
});

mo.observe(el, { attributes: true });
el.setAttribute("data-count", "1");
```

Fix it by checking whether a change is needed, disconnecting while you make changes or filtering with `attributeFilter`.

## 219: How do fake timers work in tests?

Test frameworks like Vitest and Jest can replace `setTimeout`, `setInterval`, `Date` and similar with fake versions. Time only moves when you tell it to.

```js
import { vi, test, expect } from "vitest";

test("debounced search runs once", () => {
  vi.useFakeTimers();
  const search = vi.fn();
  const debounced = debounce(search, 300);

  debounced("a");
  debounced("ab");
  vi.advanceTimersByTime(299);
  expect(search).not.toHaveBeenCalled();

  vi.advanceTimersByTime(1);
  expect(search).toHaveBeenCalledWith("ab");

  vi.useRealTimers();
});
```

This makes timer-based tests fast and deterministic.

## 220: Why do tests with fake timers sometimes hang or miss promise callbacks?

Fake timers replace timers, but native promises still use the real microtask queue. When your code mixes timers and `await`, advancing timers synchronously does not run the microtasks between timer callbacks.

```js
async function retry(fn) {
  try {
    return await fn();
  } catch {
    await new Promise((r) => setTimeout(r, 1000));
    return fn();
  }
}

// Use the async versions so microtasks get a chance to run
await vi.advanceTimersByTimeAsync(1000);
// or: await vi.runAllTimersAsync();
```

Jest has the same async helpers (`jest.advanceTimersByTimeAsync`). Also check whether your fake timer setup fakes `queueMicrotask`, since that can change ordering in tests.

## 221: How do you flush pending promises in a test?

Await something that resolves after the current microtasks. A simple helper:

```js
const flushPromises = () => new Promise((resolve) => setTimeout(resolve, 0));

test("loads data", async () => {
  render(<UserList />);
  await flushPromises();
  expect(screen.getByText("Ann")).toBeInTheDocument();
});
```

A task-based helper works better than `await Promise.resolve()`, because a single microtask hop may not be enough for chains of several `then` steps. With real network or DOM updates, prefer helpers like Testing Library's `findBy*` or `waitFor`, which retry until the condition is true. Do not use this helper while fake timers are on, because the `setTimeout` inside it is fake too.

## 222: How do you test code that uses requestAnimationFrame?

Options:

- Fake timers can fake `requestAnimationFrame` too (in Vitest, include it in `toFake`), then advance time by about 16 ms per frame.
- Mock it yourself and call the callbacks manually:

```js
let rafCallbacks = [];
vi.stubGlobal("requestAnimationFrame", (cb) => {
  rafCallbacks.push(cb);
  return rafCallbacks.length;
});

function nextFrame(time = performance.now()) {
  const cbs = rafCallbacks;
  rafCallbacks = [];
  cbs.forEach((cb) => cb(time));
}
```

Real visual behavior is best tested in a real browser with Playwright or Vitest browser mode.

## 223: How do you find out which part of a task is slow in the Performance panel?

1. Record the slow interaction.
2. Find the long task in the **Main** track (red corner).
3. Look at the flame chart under it. The width of each bar is its duration; bars below are functions it called.
4. Use the **Bottom-Up** tab to see which functions take the most self time, and **Call Tree** to see the top-down view.
5. Check for purple blocks (style and layout) inside the task; they mean forced layout or heavy style work.

Turning on CPU throttling (4x or 6x slowdown) helps you see problems that real users on slower phones will have.

## 224: What do Recalculate Style, Layout, Paint and Composite mean in a performance recording?

- **Recalculate Style**: the browser works out which CSS rules apply to changed elements.
- **Layout**: it computes sizes and positions.
- **Paint**: it records drawing commands for the changed layers.
- **Composite Layers** (or "Commit"): it sends layer information to the compositor thread to put on screen.

If a task shows a lot of style and layout work, look for large DOM changes, complex selectors or forced layouts. If paint is large, look for big repaints, like changing properties that affect large areas.

## 225: How do you use performance.mark and performance.measure?

They let you add your own timings, which show up in the DevTools Performance panel (in the **Timings** track) and can be collected with a `PerformanceObserver`.

```js
performance.mark("filter-start");
const result = filterProducts(products, query);
performance.mark("filter-end");

performance.measure("filter products", "filter-start", "filter-end");

const [measure] = performance.getEntriesByName("filter products");
console.log(measure.duration.toFixed(1), "ms");
```

This is useful to check how long your own code takes inside a bigger task.

## 226: Why do frameworks batch state updates in a microtask?

If every state change updated the DOM right away, ten changes in one handler would cause ten DOM updates and maybe ten layouts. By collecting changes and applying them in a microtask, the framework:

- updates the DOM once with the final state,
- still finishes before the browser renders, so the user never sees a half-updated screen,
- keeps the result predictable: right after `await`, the DOM is up to date.

Vue, Lit, Svelte and others use this approach. A task would also batch, but it could let a frame render with the old state first.

## 227: How does React batch updates?

Since React 18, all state updates are batched automatically, whether they happen in event handlers, promises, timeouts or native event listeners. Updates made in the same synchronous code are processed together in one render.

```js
function handleClick() {
  setCount((c) => c + 1);
  setFlag((f) => !f);
  // one re-render, not two
}

setTimeout(() => {
  setCount((c) => c + 1);
  setFlag((f) => !f);
  // also one re-render in React 18+
}, 0);
```

If you really need the DOM updated right away, `flushSync` from `react-dom` forces it, but it should be rare.

## 228: Do microtasks run after each requestAnimationFrame callback?

Yes. Each rAF callback is invoked separately, and when it returns, the JavaScript stack is empty, so a microtask checkpoint runs before the next rAF callback.

```js
requestAnimationFrame(() => {
  console.log("raf 1");
  Promise.resolve().then(() => console.log("micro from raf 1"));
});
requestAnimationFrame(() => console.log("raf 2"));

// raf 1
// micro from raf 1
// raf 2
```

The same is true for each event listener (for real events), each `ResizeObserver` callback and so on.

## 229: What happens if you call requestAnimationFrame inside a requestAnimationFrame callback?

The new callback is scheduled for the next frame, not the current one. The browser takes the list of callbacks at the start of the rAF step, so callbacks added during it wait.

```js
requestAnimationFrame((t1) => {
  requestAnimationFrame((t2) => {
    console.log(t2 > t1); // true: runs in the next frame
  });
});
```

This is why a recursive rAF loop runs exactly once per frame instead of forever in one frame.

## 230: What is the difference between setTimeout inside rAF and rAF inside setTimeout?

- **setTimeout inside rAF**: the timeout task runs after the current frame is rendered. Good for "after paint" work.
- **rAF inside setTimeout**: the rAF callback runs before the next frame. Good for "do this work later, but apply visual changes right before rendering".

```js
requestAnimationFrame(() => {
  setTimeout(() => console.log("after this frame was rendered"), 0);
});

setTimeout(() => {
  requestAnimationFrame(() => console.log("right before a later frame"));
}, 100);
```

## 231: Why do browsers align or coalesce timers?

To save power. Waking the CPU for every small timer uses battery. Browsers may group timers that are due close together and run them in one wake-up, especially in background tabs, on battery or for timers in iframes.

This is another reason timers are not exact. If two timers are a few milliseconds apart, they might run back to back.

## 232: How can a long inline script delay the first paint?

The browser cannot render while the main thread runs a script. A large synchronous script in the `<head>` blocks parsing and runs before anything is shown.

```html
<head>
  <!-- Blocks parsing and first render until downloaded and run -->
  <script src="big-bundle.js"></script>
</head>
```

Use `defer` or `type="module"` for most scripts, inline only critical small code, and split large bundles so less JavaScript runs before the first paint.

## 233: Why are JavaScript parsing and compiling a main thread concern?

Before a script runs, the engine must parse and compile it. Engines do part of this on background threads (streaming compilation, lazy parsing), but some work still happens on the main thread, and the script's top-level code always runs there.

Large bundles mean more of this work at load time, which shows up as long tasks named "Evaluate Script" or "Compile Code" in DevTools. Code splitting, removing unused code and loading non-critical code later with `import()` all reduce it.

## 234: How do you handle a huge JSON response without freezing the page?

Options:

- Ask the server for less: pagination, filtering, only the fields you need.
- Parse in a Web Worker: `fetch` and `res.json()` inside the worker, then send only the part the page needs.
- Stream it: use a format like NDJSON (one JSON object per line), read the body stream and parse line by line, yielding between chunks.

```js
// worker.js
self.onmessage = async () => {
  const data = await (await fetch("/big.json")).json();
  const summary = summarize(data);
  self.postMessage(summary);
};
```

Note that `res.json()` on the main thread still parses on the main thread, even though it returns a promise.

## 235: How do you add a lot of DOM nodes without hurting performance?

- Build nodes in a `DocumentFragment` or a detached container and insert them once.
- Use `append(...nodes)` or `replaceChildren(...nodes)` instead of many single inserts.
- Avoid reading layout values between inserts.
- For really long lists, render only the visible part (virtualization).
- Split the work into chunks if it still takes too long.

```js
const fragment = document.createDocumentFragment();
for (const item of items) {
  const li = document.createElement("li");
  li.textContent = item.name;
  fragment.append(li);
}
list.append(fragment); // one insert, one layout later
```

## 236: What is list virtualization and why does it help the main thread?

Virtualization means rendering only the rows that are visible (plus a small buffer) instead of the whole list. As the user scrolls, rows are reused or swapped.

With 10,000 rows, the browser would have to style, lay out and keep in memory 10,000 rows. With virtualization it handles maybe 30. This makes initial rendering, updates and layout much cheaper. Libraries like TanStack Virtual and react-window do this.

## 237: What does content-visibility: auto do?

It tells the browser it can skip rendering work (style, layout, paint) for an element's content while it is off-screen. When the element comes near the viewport, the browser renders it.

```css
.article-section {
  content-visibility: auto;
  contain-intrinsic-size: auto 800px; /* placeholder size to avoid scroll jumps */
}
```

This can make long pages render much faster. It is supported in all major browsers now.

## 238: How does event delegation affect main thread work?

Event delegation means adding one listener on a parent instead of one per child, and using `event.target` to find which child was clicked.

```js
list.addEventListener("click", (e) => {
  const item = e.target.closest("li[data-id]");
  if (!item) return;
  selectItem(item.dataset.id);
});
```

It saves memory and setup time when there are many children, and new children work automatically. The handler itself runs once per event, so its cost does not grow with the number of children.

## 239: How do you separate urgent and non-urgent work in an input handler?

Do the minimum that the user needs to see right away, then yield and do the rest later.

```js
input.addEventListener("input", async (e) => {
  // Urgent: show the typed text and a quick update
  label.textContent = e.target.value;

  // Let the browser paint this frame
  await yieldToMain();

  // Non-urgent: heavy filtering and rendering
  renderResults(filter(allItems, e.target.value));
});
```

In React, `startTransition` or `useDeferredValue` does a similar split for state updates.

## 240: How do you schedule non-critical work after an interaction?

Do the visible part first, then move things like analytics, logging or saving to later tasks.

```js
button.addEventListener("click", () => {
  openMenu(); // visible update

  // Run after the next paint, at low priority if supported
  if (globalThis.scheduler?.postTask) {
    scheduler.postTask(() => trackMenuOpen(), { priority: "background" });
  } else {
    setTimeout(trackMenuOpen, 0);
  }
});
```

Analytics code in click handlers is a very common cause of poor INP.

## 241: What is the "idle until urgent" pattern?

Do expensive setup work during idle time, but if the result is needed before it is ready, compute it right away.

```js
class IdleValue {
  #value;
  #done = false;
  #handle;

  constructor(init) {
    this.init = init;
    this.#handle = requestIdleCallback(() => this.#compute());
  }

  #compute() {
    if (this.#done) return;
    this.#value = this.init();
    this.#done = true;
  }

  get() {
    if (!this.#done) {
      cancelIdleCallback(this.#handle);
      this.#compute();
    }
    return this.#value;
  }
}

const formatter = new IdleValue(
  () => new Intl.DateTimeFormat("en-US", { dateStyle: "full" }),
);
// Later, inside a click handler:
formatter.get().format(new Date());
```

## 242: What is lazy or partial hydration and how does it help the event loop?

When a server-rendered page loads, frameworks "hydrate" it: they run component code and attach event listeners. Hydrating the whole page at once is often a long task that blocks input right after load.

Lazy or partial hydration hydrates parts only when needed (when visible, on interaction or when idle). Islands architectures (Astro), React's selective hydration with `Suspense`, Angular's incremental hydration with `@defer` triggers, and Qwik's resumability are examples. Less work up front means fewer long tasks during load.

## 243: How do third-party scripts affect the event loop and how do you limit the damage?

Analytics, ads, chat widgets and tag managers run on the same main thread as your code. Their long tasks delay your input handlers and rendering, and you do not control their code.

Ways to limit it:

- Load them with `async` or `defer`, or after the page is interactive.
- Load widgets on interaction (show a static "facade" until the user clicks).
- Remove scripts you do not need.
- Use the LoAF API to see which third-party scripts block the main thread.
- Some teams try running them in a worker (for example with Partytown), with trade-offs in compatibility.

## 244: What is the difference between the delay option of postTask and setTimeout?

Both wait at least the given time. But `scheduler.postTask(fn, { delay })` queues the task with a priority when the delay ends, and you can cancel it or change its priority with a `TaskSignal`. It also returns a promise with the result.

```js
const controller = new TaskController({ priority: "background" });

const result = await scheduler.postTask(() => computeStats(), {
  delay: 1000,
  signal: controller.signal,
});
```

`setTimeout` tasks have no priority control and no built-in promise.

## 245: What priority does the continuation after scheduler.yield get?

The continuation inherits the priority of the task that called `yield`. If you call `scheduler.yield()` inside a `postTask` callback with `priority: "background"`, the continuation is also background. In a normal task, it is treated like user-visible.

Continuations are also placed ahead of other tasks with the same priority, so your work does not fall behind new tasks that were queued while you yielded. That is the main advantage over `setTimeout`.

## 246: How do you write a cancellable delay?

Accept an `AbortSignal` and clear the timer when it aborts.

```js
function delay(ms, { signal } = {}) {
  return new Promise((resolve, reject) => {
    if (signal?.aborted) return reject(signal.reason);

    const timer = setTimeout(() => {
      signal?.removeEventListener("abort", onAbort);
      resolve();
    }, ms);

    function onAbort() {
      clearTimeout(timer);
      reject(signal.reason);
    }

    signal?.addEventListener("abort", onAbort, { once: true });
  });
}

const controller = new AbortController();
delay(5000, { signal: controller.signal }).catch((e) => console.log(e.name)); // AbortError
controller.abort();
```

## 247: How are WebSocket messages delivered and what happens if they arrive very fast?

Each incoming message is queued as a task that fires a `message` event. If the server sends thousands of messages per second, the page gets thousands of tasks, each with its own handler work and maybe DOM updates. The main thread can fall behind, input gets slow and memory grows as messages pile up.

The standard `WebSocket` API has no way to slow down the sender. You need to handle it in your app (see the next question), or use `WebSocketStream` in Chromium, which supports backpressure through streams.

## 248: How do you handle high-frequency updates without overloading the main thread?

Store incoming data as it arrives, and update the UI once per frame with the latest state.

```js
let latestPrices = new Map();
let scheduled = false;

socket.addEventListener("message", (e) => {
  const { symbol, price } = JSON.parse(e.data);
  latestPrices.set(symbol, price);

  if (!scheduled) {
    scheduled = true;
    requestAnimationFrame(() => {
      scheduled = false;
      renderPrices(latestPrices);
      latestPrices = new Map();
    });
  }
});
```

The handler stays tiny, and the DOM is updated at most once per frame. For very high volumes, move the parsing to a worker.

## 249: How are BroadcastChannel and storage events delivered?

Both are queued as tasks in the receiving page's event loop.

- `BroadcastChannel` sends messages between same-origin windows, tabs, iframes and workers. Each receiver gets a `message` event.
- The `storage` event fires in other same-origin windows when `localStorage` changes. It does not fire in the window that made the change.

```js
const channel = new BroadcastChannel("auth");
channel.onmessage = (e) => {
  if (e.data === "logout") showLoggedOut();
};

// In another tab
new BroadcastChannel("auth").postMessage("logout");
```

## 250: Why does an IndexedDB transaction fail after awaiting a fetch?

IndexedDB transactions commit automatically when there are no pending requests and control returns to the event loop. If you `await` something that is not an IndexedDB request (like `fetch`), the transaction sees no pending requests at the end of the current task and commits. Using it afterwards throws `TransactionInactiveError`.

```js
const tx = db.transaction("users", "readwrite");
const store = tx.objectStore("users");

const user = await fetch("/api/user").then((r) => r.json()); // transaction is done here
store.put(user); // TransactionInactiveError
```

Fetch the data first, then open the transaction and do only IndexedDB work inside it.

## 251: Can you use Atomics.wait on the main thread?

No. `Atomics.wait` blocks the thread until another thread wakes it. Browsers do not allow it on the main thread, because it would freeze the page; it throws a `TypeError` there. It is allowed in workers.

On the main thread you can use `Atomics.waitAsync`, which returns a promise instead of blocking:

```js
const shared = new Int32Array(new SharedArrayBuffer(4));

const { async, value } = Atomics.waitAsync(shared, 0, 0);
if (async) {
  value.then((result) => console.log("woken:", result)); // "ok" or "timed-out"
}

// In a worker: Atomics.store(shared, 0, 1); Atomics.notify(shared, 0);
```

Browser support for `waitAsync` varies, so check before using it.

## 252: What do you need to use SharedArrayBuffer in the browser?

The page must be cross-origin isolated. You get that by sending two headers with the document:

```text
Cross-Origin-Opener-Policy: same-origin
Cross-Origin-Embedder-Policy: require-corp
```

(`credentialless` is another option for COEP.) You can check with `self.crossOriginIsolated`. This requirement was added after the Spectre attacks, because shared memory can be used to build very precise timers.

## 253: What is OffscreenCanvas and how does it help the main thread?

`OffscreenCanvas` lets a worker draw to a canvas. You transfer control of a `<canvas>` to a worker, and the worker does all the drawing, so heavy rendering (charts, games, image effects) does not block the page.

```js
// main.js
const canvas = document.querySelector("canvas");
const offscreen = canvas.transferControlToOffscreen();
const worker = new Worker("draw-worker.js");
worker.postMessage({ canvas: offscreen }, [offscreen]);

// draw-worker.js
self.onmessage = (e) => {
  const ctx = e.data.canvas.getContext("2d");
  function draw(t) {
    ctx.clearRect(0, 0, 300, 150);
    ctx.fillRect(150 + Math.sin(t / 300) * 100, 60, 30, 30);
    requestAnimationFrame(draw);
  }
  requestAnimationFrame(draw);
};
```

## 254: Does WebAssembly run off the main thread?

No, not by default. WebAssembly code runs on whatever thread calls it. If you call a slow Wasm function from the page, it blocks the main thread just like slow JavaScript.

Compiling a Wasm module can be done asynchronously with `WebAssembly.compileStreaming` or `instantiateStreaming`, which keeps compilation from blocking. To run heavy Wasm work without blocking, run it in a worker.

## 255: What does img.decode() do?

Image decoding (turning compressed PNG or JPEG data into pixels) can be slow for big images. If it happens when the image is first painted, it can cause a long frame.

`img.decode()` returns a promise that resolves when the image is decoded and ready to paint, so you can insert it into the page without a decode hiccup.

```js
const img = new Image();
img.src = "/large-photo.jpg";
await img.decode();
gallery.append(img);
```

The `decoding="async"` attribute on `<img>` gives the browser a similar hint for normal images.

## 256: What is createImageBitmap used for?

`createImageBitmap()` decodes an image (from a `Blob`, `ImageData`, `<img>` and so on) asynchronously and returns an `ImageBitmap` that can be drawn to a canvas quickly. It also works in workers.

```js
const res = await fetch("/sprite.png");
const bitmap = await createImageBitmap(await res.blob());
ctx.drawImage(bitmap, 0, 0);
```

It is the standard way to load images for canvas or WebGL work without blocking the main thread on decoding.

## 257: How do you wait for fonts before measuring text?

If you measure text before a web font loads, you get the size of the fallback font. Wait for `document.fonts.ready` or load a specific font:

```js
await document.fonts.ready;
const width = label.getBoundingClientRect().width; // measured with the real font

// Or a specific font
await document.fonts.load('16px "Inter"');
```

`document.fonts.ready` is a promise that resolves when the fonts that are currently loading are done.

## 258: What is requestVideoFrameCallback?

`video.requestVideoFrameCallback(callback)` calls your function when a new video frame is sent to the compositor. It is like `requestAnimationFrame`, but tied to the video's frames instead of the display's refresh.

```js
function onFrame(now, metadata) {
  drawOverlay(metadata.mediaTime);
  video.requestVideoFrameCallback(onFrame);
}

video.requestVideoFrameCallback(onFrame);
```

It is useful for video effects, overlays and analysis, where you want exactly one callback per video frame. It is supported in all major browsers now.

## 259: Are focus and blur events fired synchronously?

When you call `element.focus()` from JavaScript, `blur`/`focusout` on the old element and `focus`/`focusin` on the new one fire synchronously, inside the `focus()` call.

```js
input.addEventListener("focus", () => console.log("focus"));

console.log("before");
input.focus();
console.log("after");

// before
// focus
// after
```

This can surprise you: a focus handler might change state while your code is still in the middle of something.

## 260: Which DOM operations fire events synchronously?

Some common ones:

- `dispatchEvent()`
- `element.click()` (fires `click`)
- `element.focus()` and `element.blur()`
- `form.reset()` (fires `reset`)
- `form.requestSubmit()` (fires `submit`)
- `abortController.abort()` (fires `abort` on the signal)

Not every method works like this. For example, `dialog.close()` fires its `close` event later, as a task.

The safe assumption: events you trigger with a method call may run handlers before the method returns. Read the docs for each API instead of guessing.

## 261: How can you use generators to split work into chunks?

A generator can pause after each unit of work. A small runner calls it until a time budget runs out and then yields to the browser.

```js
function* processItems(items) {
  for (const item of items) {
    heavyWork(item);
    yield;
  }
}

async function runWithBudget(generator, budgetMs = 10) {
  let done = false;
  while (!done) {
    const start = performance.now();
    while (!done && performance.now() - start < budgetMs) {
      done = generator.next().done;
    }
    if (!done) await yieldToMain();
  }
}

await runWithBudget(processItems(bigList));
```

The work code stays simple, and the scheduling is in one place.

## 262: How do you avoid showing stale results when requests finish out of order?

If a user types "a", then "ab", the response for "a" may arrive after "ab". Without care, the old results overwrite the new ones.

Abort the previous request:

```js
let controller;

input.addEventListener("input", async (e) => {
  controller?.abort();
  controller = new AbortController();

  try {
    const res = await fetch(`/search?q=${encodeURIComponent(e.target.value)}`, {
      signal: controller.signal,
    });
    renderResults(await res.json());
  } catch (err) {
    if (err.name !== "AbortError") throw err;
  }
});
```

Another way is to keep a request counter and ignore any response that is not from the latest request.

## 263: Why might your DOM not be updated right after setting state in a framework?

Most frameworks batch updates and apply them later (in a microtask or during their own scheduling). So right after `setState` or changing a reactive value, the DOM still shows the old state.

```js
// Vue
count.value++;
console.log(el.textContent); // old value
await nextTick();
console.log(el.textContent); // new value
```

In React, read the DOM in `useLayoutEffect` or `useEffect` after the render. In Angular, use `afterNextRender`. Do not depend on the DOM changing synchronously.

## 264: How do you debug a slow interaction (poor INP)?

1. Reproduce it with DevTools open; the **Performance** panel's live metrics show INP and which interaction caused it.
2. Record a trace and look at the **Interactions** track. Each interaction shows input delay, processing duration and presentation delay.
3. If input delay is high, something else was running when the user clicked (check the tasks before it).
4. If processing is high, look at your event handlers in the flame chart.
5. If presentation delay is high, look at style, layout and paint after the handler.

In the field, collect INP with the `web-vitals` library and its attribution build, which uses LoAF data to point to the scripts involved.

## 265: Why can a page sometimes scroll smoothly while JavaScript is blocking the main thread?

Scrolling can be handled by the compositor thread. If there are no non-passive `wheel` or `touch` listeners that could cancel the scroll, the compositor moves the already painted layers without asking the main thread.

But anything that needs the main thread (new content that was not painted yet, scroll-linked JavaScript effects, `position: sticky` in some cases, layout changes) will lag. You may see blank areas ("checkerboarding") if the user scrolls into a part of the page that has not been painted.

## 266: How do non-passive wheel or touch listeners slow down scrolling?

If a `wheel` or `touchmove` listener might call `preventDefault()`, the browser has to wait for it to run on the main thread before it knows whether to scroll. If the main thread is busy, scrolling is delayed until the listener runs.

```js
// Scrolling must wait for this to run every time
scroller.addEventListener("wheel", onWheel, { passive: false });
```

Only use non-passive listeners when you really need to cancel scrolling, and attach them to the smallest element possible, not to `document`.

## 267: What does will-change do?

`will-change` tells the browser that a property is going to change soon, so it can prepare, for example by putting the element on its own compositor layer. Then animations of `transform` or `opacity` can start smoothly without repainting.

```css
.drawer {
  will-change: transform;
}
```

Use it sparingly. Each layer uses memory, and adding it to many elements can make things slower. It is best added just before an animation and removed after.

## 268: How do you reduce the input delay part of INP?

Input delay happens when the main thread is busy when the user interacts. To reduce it:

- Break up long tasks so there is always a chance to handle input soon.
- Do less work during page load (less JavaScript, lazy hydration, defer non-critical scripts).
- Avoid big timers or intervals that do heavy work at random times.
- Watch out for third-party scripts running long tasks.

## 269: How do you reduce the processing time part of INP?

Processing time is how long your event listeners run. To reduce it:

- Do only the work needed for the next frame in the handler.
- Move non-visual work (analytics, saving, logging) to later tasks.
- Yield inside the handler after the visual update.
- Avoid forced layouts and big DOM changes inside handlers.
- In frameworks, avoid re-rendering large parts of the tree for a small change.

## 270: How do you reduce the presentation delay part of INP?

Presentation delay is the time from the end of your handlers to the frame being shown. It is mostly rendering work. To reduce it:

- Keep the DOM smaller and simpler.
- Avoid changes that cause style recalculation or layout for large parts of the page.
- Use `content-visibility: auto` for off-screen content.
- Avoid big `requestAnimationFrame` callbacks right after the interaction.
- Do not render huge amounts of HTML (for example large `innerHTML` updates) in response to input.

## 271: Which page lifecycle events should you use when the user leaves the page?

- **visibilitychange** (to `hidden`): the most reliable signal, especially on mobile. Save state and send analytics here.
- **pagehide**: fires when the page is being unloaded or put in the bfcache.
- **beforeunload**: only for warning about unsaved changes. Add it only when needed and remove it after.
- **unload**: avoid it. It is unreliable on mobile, blocks the bfcache and Chrome is deprecating it.

```js
document.addEventListener("visibilitychange", () => {
  if (document.visibilityState === "hidden") {
    navigator.sendBeacon("/analytics", JSON.stringify(collectedData));
  }
});
```

## 272: How do you send data reliably when the page is closing?

Normal `fetch` requests can be cancelled when the page unloads. Use:

- `navigator.sendBeacon(url, data)`: queues a small POST that the browser sends even after the page is gone.
- `fetch(url, { method: "POST", body, keepalive: true })`: the same idea, with more control over headers and method.

```js
addEventListener("pagehide", () => {
  fetch("/api/save-draft", {
    method: "POST",
    body: JSON.stringify(draft),
    headers: { "Content-Type": "application/json" },
    keepalive: true,
  });
});
```

Both have a size limit (around 64 KB in total for in-flight keepalive requests).

## 273: What happens to timers and pending promises when the user navigates away?

When the document is unloaded (and not saved in the bfcache), its timers are cleared, pending tasks for it are dropped and in-flight fetches are cancelled. Promises that were waiting never settle, because the document and its JavaScript environment are gone.

So never rely on a `setTimeout` or a promise callback to run during navigation. Use `visibilitychange`/`pagehide` with `sendBeacon` or `keepalive` for last-moment work.

## 274: How do timers and listeners cause memory leaks?

A timer or listener keeps a reference to its callback, and the callback keeps references to everything it closes over. If you never clear it, that memory can never be freed.

```js
function mountWidget(el) {
  const bigData = loadHugeData();
  const id = setInterval(() => {
    el.textContent = summarize(bigData);
  }, 1000);

  return () => clearInterval(id); // call this when the widget is removed
}
```

Common sources in single-page apps: intervals that are not cleared, listeners on `window` or `document` not removed, and observers not disconnected after a component is gone.

## 275: How do you clean up timers and async work in a React effect?

Return a cleanup function from `useEffect`. React calls it before the effect runs again and when the component unmounts.

```jsx
useEffect(() => {
  const controller = new AbortController();
  const id = setInterval(refresh, 10_000);

  fetch(`/api/items/${itemId}`, { signal: controller.signal })
    .then((r) => r.json())
    .then(setItems)
    .catch((err) => {
      if (err.name !== "AbortError") setError(err);
    });

  return () => {
    clearInterval(id);
    controller.abort();
  };
}, [itemId]);
```

Aborting the fetch also prevents setting state from an old request after the item has changed.

## 276: How do you poll a server with exponential backoff?

Use a recursive `setTimeout` and increase the delay after errors.

```js
async function poll(url, { onData, base = 2000, max = 60_000, signal }) {
  let delayMs = base;

  while (!signal?.aborted) {
    try {
      const res = await fetch(url, { signal });
      if (!res.ok) throw new Error(`HTTP ${res.status}`);
      onData(await res.json());
      delayMs = base; // reset on success
    } catch (err) {
      if (err.name === "AbortError") return;
      delayMs = Math.min(delayMs * 2, max);
    }
    await new Promise((r) => setTimeout(r, delayMs));
  }
}
```

A new request only starts after the previous one finished, so requests never pile up. For live updates, consider Server-Sent Events or WebSockets instead.

## 277: How do you choose between a microtask, a task, requestAnimationFrame and an idle callback?

- **Microtask** (`queueMicrotask`, promises): "after this code, before anything else". Good for batching state changes. Does not let the browser render.
- **Task** (`setTimeout`, `postTask`, `scheduler.yield`): "later, after the browser had a chance to do other things". Good for splitting long work and deferring non-urgent work.
- **requestAnimationFrame**: "right before the next paint". Good for visual updates and reading or writing layout once per frame.
- **requestIdleCallback** or background `postTask`: "when nothing else is going on". Good for low priority work.

## 278: Is it true that setTimeout(fn, 0) runs fn right after the current function?

No. Several things can happen in between:

- All microtasks run first.
- The browser may render a frame (including all rAF callbacks).
- Other tasks that are already queued may run first, such as user input.
- The delay may be clamped to 4 ms or more, and much more in background tabs.

If you want "right after the current code", use `queueMicrotask`. If you want "after the browser has updated the screen", use the rAF + `setTimeout` pattern.

## 279: How do RxJS schedulers map to the browser event loop?

- `queueScheduler`: synchronous, runs work right away in a queue (avoids recursion).
- `asapScheduler`: runs work as a microtask (uses a promise).
- `asyncScheduler`: runs work as a task using `setInterval`/`setTimeout`. This is the default for time-based operators like `delay` and `debounceTime`.
- `animationFrameScheduler`: runs work in `requestAnimationFrame`.

```js
import { of, observeOn, asapScheduler } from "rxjs";

of(1, 2, 3).pipe(observeOn(asapScheduler)).subscribe(console.log);
console.log("sync");
// sync, 1, 2, 3
```

## 280: How do you wait for a web component to finish rendering?

It depends on the library. Lit, for example, batches property changes and renders in a microtask. Each element has an `updateComplete` promise that resolves after the render:

```js
const el = document.querySelector("my-counter");
el.count = 5;
await el.updateComplete;
console.log(el.shadowRoot.textContent); // shows 5
```

For plain custom elements, it depends on how the component schedules its rendering. If it renders synchronously in a setter, no waiting is needed.

## 281: When do useLayoutEffect and useEffect run compared to the browser paint?

- **useLayoutEffect** runs synchronously after React updates the DOM, before the browser gets a chance to paint. Use it to measure the DOM and fix layout before the user sees anything. It blocks painting, so keep it short.
- **useEffect** usually runs after the browser has painted. It is for side effects that do not need to block the screen, like fetching data or subscribing.

One nuance: for updates caused by discrete user input like clicks, React may run `useEffect` callbacks synchronously before paint to keep results consistent.

## 282: When do custom element lifecycle callbacks run?

Custom element reactions like `connectedCallback`, `disconnectedCallback` and `attributeChangedCallback` run synchronously, right after the DOM operation that caused them, before control returns to your script. They are not microtasks or tasks.

```js
class MyEl extends HTMLElement {
  connectedCallback() {
    console.log("connected");
  }
}
customElements.define("my-el", MyEl);

console.log("before");
document.body.append(document.createElement("my-el"));
console.log("after");

// before
// connected
// after
```

## 283: How do you run code after an inserted element has been rendered?

After inserting, the element is in the DOM right away, and you can measure it (this forces layout). If you need the element to actually be painted on screen, wait for the next frame:

```js
container.append(card);

// Measuring works now (forces layout)
console.log(card.getBoundingClientRect().height);

// After it has been painted
requestAnimationFrame(() => {
  setTimeout(() => {
    console.log("card is on screen now");
  }, 0);
});
```

Measuring right away is fine once. Measuring after each insert in a loop causes layout thrashing.

## 284: When should you use queueMicrotask instead of setTimeout?

Use `queueMicrotask` when you want the work to run after the current synchronous code, but before the browser renders or handles anything else. Typical cases:

- Batching several synchronous calls into one update.
- Making a callback always async (so callers do not see it run synchronously sometimes and async other times).

Use `setTimeout` (or `postTask`/`scheduler.yield`) when you want the browser to be able to render or handle input first. Do not use microtasks to split up long work; they do not let the browser breathe.

## 285: Why do you get fewer mousemove events when the page is busy?

Browsers do not queue one task per hardware mouse movement. Continuous events like `pointermove`, `mousemove` and `touchmove` are coalesced: if several arrive before the main thread can handle them, they are merged into one event with the latest position.

In Chromium, these events are also aligned with frames, so they are dispatched at most once per frame. If you need every point (for example in a drawing app), use `event.getCoalescedEvents()` in `pointermove`.

## 286: How do you measure the frame rate in JavaScript?

Count `requestAnimationFrame` callbacks over time:

```js
let frames = 0;
let last = performance.now();

function count(now) {
  frames++;
  if (now - last >= 1000) {
    console.log("FPS:", frames);
    frames = 0;
    last = now;
  }
  requestAnimationFrame(count);
}

requestAnimationFrame(count);
```

This tells you how often the rAF step ran, which is close to the frame rate. It is not perfect: rAF can run even if the compositor fails to show the frame in time. DevTools' frame rendering stats are more accurate for debugging.

## 287: What is Promise.withResolvers and when is it useful?

`Promise.withResolvers()` returns a promise together with its `resolve` and `reject` functions. It is handy when the code that creates the promise is not the code that settles it, for example when bridging events to promises.

```js
function waitForMessage(port, type) {
  const { promise, resolve } = Promise.withResolvers();

  port.addEventListener("message", function handler(e) {
    if (e.data.type === type) {
      port.removeEventListener("message", handler);
      resolve(e.data);
    }
  });

  return promise;
}
```

It does not change the timing: callbacks still run as microtasks after `resolve` is called.

## 288: How do you combine a timeout with user cancellation?

Use `AbortSignal.any()`, which creates a signal that aborts when any of the given signals aborts.

```js
const userCancel = new AbortController();
cancelButton.onclick = () => userCancel.abort();

const signal = AbortSignal.any([
  userCancel.signal,
  AbortSignal.timeout(10_000),
]);

try {
  const res = await fetch("/api/report", { signal });
  show(await res.json());
} catch (err) {
  if (err.name === "TimeoutError") showMessage("Took too long");
  else if (err.name === "AbortError") showMessage("Cancelled");
  else throw err;
}
```

## 289: Does await inside a loop let the browser render?

Only if what you await is resolved by a task or a later event. Awaiting something already resolved, or a promise that resolves in a microtask, keeps you in the same microtask checkpoint, so the browser cannot render.

```js
// Does NOT yield: the whole loop runs before the next frame
for (const item of items) {
  await Promise.resolve();
  process(item);
}

// Does yield: each step waits for a new task
for (const item of items) {
  await new Promise((r) => setTimeout(r, 0));
  process(item);
}
```

## 290: What happens if an event listener is an async function?

The browser calls it and ignores the returned promise. The part before the first `await` runs during dispatch; the rest runs later as microtasks after the dispatch has finished.

That means:

- `preventDefault()` and `stopPropagation()` after `await` have no effect.
- Errors after `await` become unhandled promise rejections, not `error` events.
- The browser does not wait for the async work before continuing.

```js
button.addEventListener("click", async () => {
  const data = await load();
  render(data);
});
```

This is fine for normal async work, as long as you know these limits.

## 291: How do you run low-priority work with a fallback when requestIdleCallback is missing?

Feature-detect and fall back to a timer:

```js
const runWhenIdle =
  typeof requestIdleCallback === "function"
    ? (cb) => requestIdleCallback(cb, { timeout: 2000 })
    : (cb) =>
        setTimeout(() => {
          const start = performance.now();
          cb({
            didTimeout: false,
            timeRemaining: () => Math.max(0, 50 - (performance.now() - start)),
          });
        }, 1);

runWhenIdle((deadline) => {
  while (deadline.timeRemaining() > 0 && queue.length) {
    queue.shift()();
  }
});
```

The fallback does not know if the browser is idle, but it keeps the same API, so the rest of your code does not change.

## 292: Should you batch DOM updates in a microtask or in requestAnimationFrame?

- **Microtask**: the update happens very soon, before any rendering, so the next frame is always correct. Several updates in one synchronous block are merged. But updates from different tasks in the same frame are not merged.
- **rAF**: all updates within a frame are merged, even from many tasks. But the DOM stays outdated until right before the frame, and rAF does not run in background tabs.

Frameworks usually use microtasks for state-driven updates. rAF is better for high-frequency visual updates like pointer tracking or streaming data.

## 293: Is it expensive to create many small timers?

Each timer has some overhead: the browser stores it, and when it fires it becomes a separate task with its own microtask checkpoint and possibly a separate render. Thousands of timers firing at similar times cause many small tasks and more work for the scheduler.

If you have many things that need to happen at similar times, use one timer or one rAF loop that handles all of them, for example one ticking clock for all "time ago" labels instead of one timer per label.

## 294: What is the Web Locks API and how does it relate to async code?

`navigator.locks.request(name, callback)` gives you a lock that is shared across tabs and workers of the same origin. The callback runs when the lock is granted, and the lock is held until the promise it returns settles.

```js
await navigator.locks.request("sync-cart", async () => {
  const cart = await readCartFromIndexedDB();
  await sendToServer(cart);
});
```

Within one thread you rarely need locks, because code runs to completion. But across `await` points, or between tabs, two pieces of async code can interleave, and Web Locks help prevent that.

## 295: Does requestAnimationFrame keep running for elements that are off-screen?

Yes, if the tab is visible. rAF is tied to the document, not to a specific element. A rAF loop animating something far below the viewport keeps running every frame and wastes CPU.

Stop such loops when the element is not visible, for example using `IntersectionObserver`:

```js
let running = false;

const io = new IntersectionObserver(([entry]) => {
  running = entry.isIntersecting;
  if (running) requestAnimationFrame(loop);
});

function loop(t) {
  if (!running) return;
  draw(t);
  requestAnimationFrame(loop);
}

io.observe(canvas);
```

Note that cross-origin iframes that are off-screen are throttled by Chromium automatically, but your own page's rAF is not.

## 296: In what order do rAF, ResizeObserver and IntersectionObserver callbacks run in a frame?

In the rendering step, roughly:

1. `resize` and `scroll` events
2. `requestAnimationFrame` callbacks
3. Style and layout
4. `ResizeObserver` callbacks (and layout again if they changed things, repeated as needed)
5. Intersection checks; `IntersectionObserver` callbacks are queued as tasks and run after this frame
6. Paint

So rAF runs before layout, `ResizeObserver` after layout, and `IntersectionObserver` callbacks a bit later.

## 297: How should you think about ordering between different async APIs?

Only rely on order guarantees that the specs give you:

- Microtasks run in the order they were queued.
- Tasks from the same task source run in order (for example two timers with the same delay, or messages on one port).
- All microtasks run before the next task.

Do not rely on the order between different task sources, like a timer and a message from a worker, or a timer and a rAF callback. If order matters, chain the operations so each one schedules the next.

## 298: Why is it a bad idea to measure performance with setTimeout callbacks?

Timer callbacks can be delayed by other tasks, clamping, throttling and power saving. If you measure something by how long a `setTimeout` took to fire, you mostly measure how busy the main thread was, not the thing you wanted.

Use `performance.now()` around the code you want to measure, `performance.mark`/`measure`, and the Performance panel. For user-facing metrics, use the Event Timing API, LoAF and the `web-vitals` library.

## 299: What does an event loop iteration look like in a typical click scenario?

1. The user clicks. The browser queues a task for `pointerdown`, `pointerup`, `click` (and related events).
2. The event loop runs the task. Your `click` listeners run, and microtasks run after each listener.
3. Your handler changed the DOM. Nothing is painted yet.
4. When the next frame is due, the rendering step runs: rAF callbacks, style, layout, `ResizeObserver`, paint.
5. The compositor puts the new frame on screen.

The time from step 1 to step 5 is what INP measures for that interaction.

## 300: What are some common wrong statements about the browser event loop?

- "JavaScript is multi-threaded because of async." (No, async is about waiting, not threads.)
- "Promises run in parallel." (The work they wait for may, but the callbacks run on one thread.)
- "Microtasks run after rendering." (They run before.)
- "requestAnimationFrame runs every 16 ms." (It follows the display and pauses in hidden tabs.)
- "`await` gives the browser a chance to render." (Only if it waits for a task or an event.)
- "There is one task queue." (There are several; only the microtask queue is single.)
- "The event loop is part of V8." (It is defined by the HTML spec and implemented by the browser.)

# Advanced Questions (301-450)

## 301: Walk through the event loop processing model as the HTML spec describes it.

For a window event loop, each iteration roughly does this:

1. Pick a task queue that has at least one runnable task (the browser chooses which one). If none, skip to the microtask step.
2. Take the oldest runnable task from that queue and run it. Track the time for long task reporting.
3. Perform a microtask checkpoint: run microtasks until the queue is empty, then handle unhandled promise rejections.
4. Update the rendering, if this is a rendering opportunity for any document in this event loop. This includes resize, scroll, media query and animation steps, rAF callbacks, style and layout, `ResizeObserver`, intersection observations and painting.
5. If there is no other work and no rendering is needed, compute an idle deadline and start an idle period (for `requestIdleCallback`).

Then it goes back to step 1. Worker event loops follow the same model without the rendering step.

## 302: The spec says task queues are "sets", not queues. Why does that matter?

A task queue in the spec is a set of tasks, and the event loop takes the first runnable task, not just the first task. A task is runnable only if its document is "fully active" (not in the bfcache, not detached).

So tasks for a frozen or inactive document are skipped and stay waiting, while tasks behind them for other documents can run. Also, since the browser picks which task queue to use, there is no global first-in, first-out order across task sources.

## 303: How does Chrome decide which task to run next?

Chrome's renderer has a main thread scheduler (in Blink) with many internal task queues, each with a priority. Roughly:

- Input events and urgent rendering work get high priority.
- Normal page tasks (timers, network, `postMessage`) get normal priority.
- Background and idle work gets low priority.
- Throttled queues (timers in hidden pages) are only allowed to run at certain times.

It also uses signals like "the user is scrolling" or "a frame is due" to change priorities on the fly. `scheduler.postTask` priorities map into this system. Other browsers have their own versions of the same idea.

## 304: What exactly happens during a microtask checkpoint?

From the spec:

1. If the event loop is already performing a checkpoint, return (no nesting).
2. Set the "performing a microtask checkpoint" flag.
3. While the microtask queue is not empty, take the oldest microtask and run it.
4. For each environment settings object, notify about rejected promises (this is where `unhandledrejection` events are queued).
5. Clean up IndexedDB transactions.
6. Clear the flag.

The no-nesting rule means that if code running inside a microtask triggers something that would normally run a checkpoint (like dispatching an event synchronously), the inner checkpoint is skipped and the microtasks just stay in the queue for the outer loop.

## 305: When exactly does a microtask checkpoint happen besides "after each task"?

The spec runs a checkpoint in "clean up after running script": when a callback or script finishes and the JavaScript execution context stack becomes empty. That covers:

- after each task,
- after each event listener called by the browser (not by `dispatchEvent` from JS),
- after each `requestAnimationFrame` callback,
- after each `ResizeObserver` and similar observer callback,
- after each `<script>` element runs during parsing.

That is why user-generated events run microtasks between listeners while `element.click()` does not: in the second case, your script is still on the stack.

## 306: List the steps of "update the rendering" in order.

For each document that needs rendering in this frame, roughly in this order:

1. Reveal steps and flush autofocus candidates.
2. Run the resize steps (fire `resize`).
3. Run the scroll steps (fire `scroll` and `scrollend`).
4. Evaluate media queries and report changes (`MediaQueryList` `change` events).
5. Update animations and send events (Web Animations and CSS animation/transition events).
6. Run the fullscreen steps.
7. Run animation frame callbacks (`requestAnimationFrame`).
8. Update style and layout, then gather and broadcast `ResizeObserver` notifications, repeating as long as observations get deeper.
9. Update intersection observations (queues the `IntersectionObserver` callback tasks).
10. Paint, then the frame is handed to the compositor.

The exact list grows as the spec evolves (for example with view transitions and content-visibility), but the main order of events, rAF, layout, `ResizeObserver` and paint is stable.

## 307: What is a "rendering opportunity" and when can the browser skip rendering?

A rendering opportunity is a point where the browser could update the screen, usually tied to the display's vsync. The spec lets browsers skip rendering for a document when:

- the browser decides an update would not be visible (hidden tab, off-screen iframe),
- it is better to skip to keep a steady frame rate (for example running at 30 fps instead of uneven 40 fps),
- the document has nothing to update (no rAF callbacks, no changes),
- the main thread is too busy and the browser wants to process more tasks first.

When rendering is skipped, rAF callbacks for that document are not run.

## 308: Why are scroll and resize events tied to frames?

Because they are dispatched inside the "update the rendering" step, not as separate tasks for every change. A scroll position can change many times between frames, but the browser only fires one `scroll` event per frame per target.

This keeps handlers from running more often than the screen can show changes. It also means a `scroll` handler and a rAF callback in the same frame see the same scroll position, and the scroll handler runs first.

## 309: When are transitionend and animationend events fired?

In the "update animations and send events" part of the rendering step. The browser updates the timelines, and events from CSS animations and transitions (`transitionstart`, `transitionend`, `animationstart`, `animationiteration`, `animationend` and so on) are queued and dispatched in a batch, sorted by their scheduled time.

So they are aligned to frames too. A `transitionend` event does not fire at the exact millisecond the transition ends; it fires at the next rendering opportunity after that.

## 310: How does the ResizeObserver loop algorithm prevent infinite loops?

After layout, the browser gathers active observations at a depth deeper than the shallowest depth handled so far, delivers them, and runs layout again if needed. It keeps going only while there are observations deeper in the tree than the last round.

If observations remain that are not deeper (meaning a callback changed something at the same level or above), the browser stops, reports the error "ResizeObserver loop completed with undelivered notifications", and delivers those notifications in the next frame. The depth rule guarantees the loop always ends.

## 311: Why are IntersectionObserver callbacks tasks while ResizeObserver callbacks run inside rendering?

`ResizeObserver` is meant for layout-dependent changes that should show in the same frame (like adjusting a component to its new size), so it runs between layout and paint and can trigger another layout.

`IntersectionObserver` is meant for things like lazy loading and visibility tracking, which do not need to be in the same frame. The intersection check happens in the rendering step, but the callback is queued as a task. This keeps it from adding work to the frame, and the browser can even run it with lower priority.

## 312: What timestamp do rAF callbacks get, and why do all callbacks in a frame get the same one?

They get the frame's start time, as a `DOMHighResTimeStamp` on the same clock as `performance.now()`. The spec passes the same time to every callback in that run of animation frame callbacks.

This makes animations consistent: if two animations update in the same frame, they compute their positions for the same moment. It also means if an earlier callback took 10 ms, a later one still gets the original timestamp, not "now". Use `performance.now()` if you need the actual current time.

## 313: How does the browser decide the idle deadline for requestIdleCallback?

When there is no task to run and no rendering to do, the event loop computes a deadline:

- at most 50 ms from now,
- no later than the next expected frame if rendering is going to be needed,
- no later than the next timer that is due.

`deadline.timeRemaining()` is the time left until that deadline. The 50 ms limit makes sure that if the user interacts during idle work, the response still feels quick.

## 314: What types of event loops exist in the browser?

The HTML spec defines three:

- **Window event loop**: used by documents (windows and same-agent iframes). It has the rendering step.
- **Worker event loop**: one for each dedicated, shared or service worker. No rendering step.
- **Worklet event loop**: for worklets like Audio Worklet and Paint Worklet. They run in a very limited environment and are driven by the browser's own pipelines.

## 315: What is an agent and an agent cluster, and how do they relate to event loops?

In the JavaScript spec, an agent is a set of execution contexts with one job queue that runs on one thread at a time. An agent cluster is a set of agents that can share memory (with `SharedArrayBuffer`).

The HTML spec maps this as:

- A **similar-origin window agent** holds windows that can reach each other synchronously (same site, related browsing contexts). They share one event loop.
- Each **worker** is its own agent with its own event loop.

A page and its workers can be in the same agent cluster (so they can share memory when cross-origin isolated), but they never share an event loop.

## 316: How does site isolation change which pages share an event loop?

Site isolation puts documents from different sites into different renderer processes. So a cross-site iframe runs on a different main thread from its parent and has its own event loop. A long task in an ad iframe does not block the parent page (though they still compete for CPU).

Same-site documents that can reach each other (for example a same-origin iframe, or a popup opened with `window.open` without `noopener`) must be in the same process and share an event loop, because they can call each other's functions synchronously. Using `noopener` or COOP headers can let the browser separate them.

## 317: How does the browser connect ECMAScript jobs to the HTML microtask queue?

The ECMAScript spec calls host hooks when it needs to schedule work:

- `HostEnqueuePromiseJob(job, realm)`: the HTML spec queues a microtask that runs the job, after checking that the related document is fully active.
- `HostMakeJobCallback` and `HostCallJobCallback`: used to remember and restore the "incumbent settings object", which affects things like which origin is used for some APIs called inside the callback.

So promise ordering comes from the JavaScript spec, and the microtask queue and checkpoints come from the HTML spec.

## 318: Do promise callbacks for a removed iframe still run?

Generally no. When the HTML spec queues a promise job, it checks whether the realm's document is fully active. If the iframe was removed (or its document navigated away), the job is skipped and the callback never runs.

```js
const iframe = document.createElement("iframe");
document.body.append(iframe);
const IframePromise = iframe.contentWindow.Promise;

const p = IframePromise.resolve();
iframe.remove();

p.then(() => console.log("may never run"));
```

Browsers have had different behaviors here, so do not write code that depends on work running in a removed frame's realm.

## 319: Why does resolving a promise with another promise take extra ticks?

When you resolve promise A with a thenable B, the spec does not copy B's state directly. It queues a `NewPromiseResolveThenableJob`. That job calls `B.then(resolveA, rejectA)`. Then, when B is (already) fulfilled, its reaction is queued as another microtask, which finally resolves A. Then A's own `then` callbacks are queued.

So `resolve(B)` costs two extra microtask hops compared with `resolve(value)`. This is the reason `return promise` in an async function or `new Promise(r => r(p))` settles later than you might expect.

## 320: How did the await optimization change the number of ticks?

Before ES2019, `await x` was roughly `new Promise(r => r(x)).then(continue)`, which went through `NewPromiseResolveThenableJob` and cost three microtask hops for a native promise.

The spec was changed to use `PromiseResolve(x)`, which returns `x` itself when it is already a native promise. Then it attaches the continuation directly with `PerformPromiseThen`. That made `await nativePromise` cost one hop. V8 shipped this in 2018, and all engines follow it now.

This changed the output of some well-known quizzes, which is why old blog posts may show a different order.

## 321: What does this print?

```js
const thenable = {
  then(resolve) {
    console.log("thenable.then called");
    resolve("T");
  },
};

(async () => {
  const v = await thenable;
  console.log("await done", v);
})();

Promise.resolve()
  .then(() => console.log("p1"))
  .then(() => console.log("p2"))
  .then(() => console.log("p3"));
```

Output:

```text
thenable.then called
p1
await done T
p2
p3
```

`await thenable` wraps the object in a new promise, which queues a `NewPromiseResolveThenableJob` (microtask 1). `p1` is microtask 2. Microtask 1 calls `thenable.then`, which resolves the wrapper and queues the async function's continuation after `p1`. When `p1` runs, it queues `p2` after the continuation.

## 322: How many ticks does an async generator need per value?

More than a sync generator. Each `next()` call returns a promise, the generator body runs to the `yield`, and `yield` in an async generator awaits the yielded value. Then the result promise is resolved and the consumer's `await` (in `for await`) takes another hop.

The exact number depends on what is yielded, but it is always a few microtasks per value. For tight loops over many small values, async iteration is noticeably slower than a sync loop and still does not yield to rendering. Use it for values that really arrive over time, not as a general loop tool.

## 323: How is the microtask queue implemented in V8 and Blink?

V8 keeps a `MicrotaskQueue` object. The embedder (Blink in Chrome) decides when to run it. Blink uses V8's "scoped" policy: microtasks run when the outermost script scope ends, which matches the HTML spec's "clean up after running script" step.

Blink also adds its own microtasks to the same queue (for example `MutationObserver` delivery), so all of them run in order. Firefox (SpiderMonkey + Gecko) and Safari (JavaScriptCore + WebKit) have their own versions, but the observable behavior follows the specs.

## 324: How does a frame get produced in Chrome, from vsync to pixels?

1. The display's vsync signal reaches the compositor thread in the renderer.
2. If the main thread has work for this frame, the compositor sends it a "BeginMainFrame" signal.
3. On the main thread, Blink runs the rendering steps: input that was waiting for the frame, rAF callbacks, style, layout, `ResizeObserver`, paint (recording display lists).
4. The main thread "commits" the result to the compositor thread.
5. The compositor and raster workers turn display lists into tiles of pixels (often on the GPU).
6. The compositor builds a frame from layers and sends it to the GPU process (Viz), which shows it.

Steps 5 and 6 happen off the main thread, which is why compositor-only animations keep running when the main thread is busy.

## 325: What is rAF-aligned input in Chromium?

Chromium does not dispatch continuous input events (like `pointermove`, `touchmove`, `wheel`) as soon as they arrive. It holds them and dispatches them at the start of the next frame, right before rAF callbacks, after coalescing them into one event per frame.

Discrete events (`pointerdown`, `pointerup`, `click`, `keydown`) are dispatched right away as their own tasks, because the order and timing of each one matters.

This means continuous event handlers run at most once per frame, so throttling them with rAF yourself often adds nothing except an extra frame of delay.

## 326: What are getCoalescedEvents and getPredictedEvents?

When several `pointermove` events are merged into one, `event.getCoalescedEvents()` returns all the original events with their exact positions and timestamps. This is important for drawing apps, where you want smooth lines, not jumps.

`event.getPredictedEvents()` returns positions the browser predicts the pointer will reach soon. Drawing those (temporarily) can make a pen feel more responsive.

```js
canvas.addEventListener("pointermove", (e) => {
  for (const ev of e.getCoalescedEvents()) {
    drawPoint(ev.clientX, ev.clientY);
  }
});
```

## 327: How is the Long Tasks API different from LoAF?

- **Long Tasks** report a single task over 50 ms. They do not include rendering work, give almost no attribution (just a container like "window" or an iframe) and miss cases where many short tasks plus rendering together block a frame.
- **LoAF** reports animation frames (from the start of the first task to the end of rendering) that took over 50 ms. It includes `renderStart`, `styleAndLayoutStart`, `blockingDuration`, and a list of scripts with details.

LoAF is a better match for what users feel, and it is the data source the `web-vitals` library uses for INP attribution.

## 328: What information does a LoAF script entry give you?

Each item in `entry.scripts` describes a script that ran during the frame. Useful fields:

- `invoker` and `invokerType`: what called it, like `BUTTON#save.onclick`, `TimerHandler:setTimeout`, `Response.json.then` or `classic-script`.
- `sourceURL`, `sourceFunctionName`, `sourceCharPosition`: where the code is.
- `duration` and `executionStart`.
- `forcedStyleAndLayoutDuration`: time spent in forced layouts inside this script.
- `pauseDuration`: time spent in sync pauses like `alert()` or sync XHR.

With these you can tell whether your code, a framework or a third-party script caused a slow frame, and whether forced layout was the problem.

## 329: How exactly does yielding improve INP?

INP measures from input to the next paint. If a handler does 300 ms of work in one task, the next paint waits 300 ms.

If the handler does the visual part (say 20 ms), then yields, the browser can render that frame right away. The remaining 280 ms run in later tasks. INP for that interaction is about 20 ms plus rendering.

Yielding also helps other interactions: if the user clicks again during the remaining work, their input can be handled between chunks instead of waiting for the whole job.

## 330: Should you yield before or after updating the DOM in an event handler?

Usually after. The pattern is:

1. Do the minimal DOM update that shows the user something happened.
2. Yield, so the browser can paint that update.
3. Do the rest.

```js
button.addEventListener("click", async () => {
  button.disabled = true;
  status.textContent = "Saving...";

  await yieldToMain(); // scheduler.yield() with a setTimeout fallback

  const data = collectFormData(); // heavy
  await save(data);
  status.textContent = "Saved";
});
```

Yielding before any update just delays the feedback. Remember that `preventDefault()` must be called before the first yield.

## 331: Why can setTimeout-based yielding perform worse than scheduler.yield in practice?

With `setTimeout(resolve, 0)`, the continuation is a normal timer task. Any tasks queued in the meantime (other scripts' timers, third-party work, message events) can run first. On a busy page, your job can wait a long time between chunks, so it takes much longer to finish. Nested timers also get the 4 ms clamp.

`scheduler.yield()` puts the continuation in a special queue ahead of other tasks of the same priority, while still letting input and rendering go first. You get the responsiveness benefit without losing your place.

## 332: How would you build a small cooperative scheduler like React's?

```js
const queue = [];
const channel = new MessageChannel();
let running = false;
const BUDGET_MS = 5;

channel.port1.onmessage = () => {
  const start = performance.now();
  while (queue.length && performance.now() - start < BUDGET_MS) {
    const job = queue[0];
    const next = job(); // a job returns a function to continue, or nothing
    if (typeof next === "function") queue[0] = next;
    else queue.shift();
  }
  if (queue.length) channel.port2.postMessage(null);
  else running = false;
};

export function schedule(job) {
  queue.push(job);
  if (!running) {
    running = true;
    channel.port2.postMessage(null);
  }
}
```

Each run works for about 5 ms and then posts a new task, so input and rendering can happen in between. Real schedulers add priorities, expiration times (so low priority jobs do not starve) and a min-heap instead of an array.

## 333: What is starvation in a priority scheduler and how do you prevent it?

If high priority work keeps coming in, low priority work may never run. For example, constant input handling might keep a background save from ever happening.

Common fixes:

- **Aging / expiration**: each task has a deadline based on its priority. When it expires, it is treated as urgent. React's scheduler does this.
- **Fairness quotas**: always run at least one low priority task every N high priority ones.
- **Time-based fallback**: a `timeout` like in `requestIdleCallback`.

The browser's own scheduler uses similar tricks to keep, for example, timers from being starved by input.

## 334: How would you keep a large data grid responsive while sorting 1 million rows?

- Do the sort in a Web Worker, so the main thread stays free. Send the data as a transferable (typed arrays work best) or keep the data in the worker and only send the visible rows.
- Use virtualization so only visible rows are rendered.
- Show feedback immediately on click (sort icon, "Sorting..."), then yield.
- Cancel an older sort when a new one starts (send a cancel message or terminate and restart the worker).
- If the data must stay on the main thread, sort in chunks with a merge sort that yields every few milliseconds.

## 335: What does the spec say about timer clamping and ordering?

The HTML spec's timer initialization steps:

- If the delay is negative, it is set to 0.
- If the timer nesting level is greater than 5 and the delay is less than 4, the delay is set to 4.
- The nesting level increases by one when a timer is created inside a timer callback.
- The browser may add extra delay for reasons like power saving or background throttling.

For ordering, the spec waits until all timers that were started earlier with the same or shorter timeout have finished their wait. This is why two timers with the same delay always fire in creation order, even if they are delayed.

## 336: Why are browser timers less precise than they could be?

For security and power:

- **Security**: precise timers make timing attacks easier, like Spectre-style attacks that read memory by measuring tiny time differences. After Spectre, browsers reduced the precision of `performance.now()` and added jitter. Chrome uses 100 microseconds normally and 5 microseconds when the page is cross-origin isolated. Other browsers use their own values.
- **Power**: waking the CPU often for timers drains batteries, so browsers align and delay timers, especially in background tabs.

## 337: How does Chrome's intensive timer throttling decide what to throttle?

Intensive throttling applies to timers when all of these are true:

- the page has been hidden for at least 5 minutes,
- the timer is part of a chain (its chain count is 5 or more, meaning it was scheduled from a timer callback that was scheduled from a timer, and so on),
- the page has been silent (no audio) for at least 30 seconds,
- the page is not using WebRTC.

Those timers are then aligned to run only once per minute. Non-chained timers (like a timer started from a `message` event) still use the normal once-per-second limit.

## 338: Why might a timer in a background tab fire later than one second even without intensive throttling?

Besides the once-per-second alignment, browsers can:

- use a CPU time budget for background pages, delaying timers when the page used too much CPU recently,
- freeze the page completely (Chrome's tab freezing, energy saver or memory saver modes),
- discard the tab, which kills the page until the user comes back,
- on mobile, suspend the whole browser when it goes to the background.

So for background work, assume timers can be delayed by minutes or never run.

## 339: Are timers in Web Workers throttled in background tabs?

Less than on the page in many cases, but you cannot rely on it. Dedicated workers are tied to their page's lifetime, and browsers have been adding throttling to workers of hidden pages too. When a page is frozen or put in the bfcache, its workers are paused as well.

Service workers are different: they do not run timers between events reliably at all, because the browser stops them when they are idle.

## 340: How does Atomics.waitAsync help build async locks and queues?

`Atomics.waitAsync(int32Array, index, expectedValue, timeout)` returns a promise that resolves when another thread calls `Atomics.notify` on that index. It lets the main thread wait on shared memory without blocking the event loop.

```js
// A simple async mutex on shared memory (0 = unlocked, 1 = locked)
async function lock(i32, idx = 0) {
  while (Atomics.compareExchange(i32, idx, 0, 1) !== 0) {
    const res = Atomics.waitAsync(i32, idx, 1);
    if (res.async) await res.value;
  }
}

function unlock(i32, idx = 0) {
  Atomics.store(i32, idx, 0);
  Atomics.notify(i32, idx, 1);
}
```

This only works with `SharedArrayBuffer` on a cross-origin isolated page. Check browser support before relying on `waitAsync`.

## 341: What does "spin the event loop" mean in the spec?

Some algorithms need to wait for something while they are in the middle of running, for example sync XHR, `alert()` or parsing a script. The spec handles this with "spin the event loop" or "pause": the current task is suspended, and the browser either waits (pause) or lets the event loop continue with other tasks until a condition is true (spin), then resumes.

`alert()`, `confirm()`, `prompt()` and `print()` use "pause": the event loop does nothing until the dialog is closed. Spinning is used inside the spec in places like the HTML parser waiting for a script to load.

## 342: Can other events run while an alert dialog is open?

According to the spec, no: `alert()` pauses, and no tasks or microtasks for that event loop run until it closes.

In practice browsers have had exceptions over the years, like some events or message deliveries happening during modal dialogs in certain browsers or situations. Tasks for other event loops (other tabs, cross-site iframes in other processes, workers) keep running. Treat modal dialogs as "everything on this page stops", and avoid them in new code.

## 343: How do DevTools breakpoints affect the event loop?

When execution stops at a breakpoint, the page's event loop is paused: no other tasks run, nothing renders, timers do not fire. After you resume, timers that expired during the pause fire as soon as possible, all at once.

This can change behavior you are trying to debug, for example race conditions, debounce logic or animations. For timing problems, prefer `console.log` with `performance.now()` timestamps, logpoints (which do not pause) or a performance recording.

## 344: When do custom element reactions run, and how is that different from microtasks?

Custom element reactions (`connectedCallback`, `attributeChangedCallback` and so on) use a "custom element reactions stack". DOM methods marked with `[CEReactions]` push a frame on the stack, and when the method returns, all reactions queued during it run before returning to your code.

So they run synchronously at the end of the DOM operation, not in a microtask. There is also a "backup element queue" for changes made by the parser or other places without a stack frame, and that one is processed in a microtask. That is why some reactions caused by HTML parsing appear later than you might expect.

## 345: When does a custom element upgrade happen?

If elements like `<my-widget>` are in the DOM before `customElements.define("my-widget", ...)` is called, they are "undefined" elements. When you call `define`, the browser upgrades all existing ones in document order: it runs the constructor and then `connectedCallback` (and `attributeChangedCallback` for observed attributes), as custom element reactions.

```js
await customElements.whenDefined("my-widget");
// Now every <my-widget> in the document is upgraded
```

Elements created after `define` are upgraded right when they are created or connected.

## 346: How does event dispatch handle listeners added or removed during dispatch?

- The **event path** (the list of targets from window down to the target and back) is computed once at the start. Moving the element in the DOM during dispatch does not change the path for this event.
- For each target, the browser takes a copy of the listener list before calling them. Listeners **added** to that target during dispatch are not called for this event.
- Listeners **removed** during dispatch are marked as removed and are skipped if they have not run yet.

```js
button.addEventListener("click", () => {
  button.addEventListener("click", () => console.log("added later"));
  console.log("first");
});
// First click: "first"
// Second click: "first", "added later"
```

## 347: How can you use AbortSignal to remove event listeners?

Pass `signal` to `addEventListener`. When the signal aborts, the browser removes the listener. One controller can remove many listeners at once.

```js
function setupDrag(el) {
  const controller = new AbortController();
  const { signal } = controller;

  el.addEventListener("pointerdown", onDown, { signal });
  window.addEventListener("pointermove", onMove, { signal });
  window.addEventListener("pointerup", onUp, { signal });

  return () => controller.abort(); // removes all three
}
```

It is cleaner than keeping references to every handler, and it works well with framework cleanup functions.

## 348: How does the browser track unhandled promise rejections?

The HTML spec keeps an "about-to-be-notified rejected promises" list for each environment. When a promise is rejected with no handler, it is added to the list (through the JavaScript `HostPromiseRejectionTracker` hook). If a handler is added before the end of the microtask checkpoint, it is removed from the list.

At the end of the microtask checkpoint, a task is queued to fire `unhandledrejection` for each promise still in the list that still has no handler. Those promises are then kept in an "outstanding rejected promises" weak set; if a handler is added later, `rejectionhandled` fires.

## 349: What happens to the other callbacks when one rAF callback or event listener throws?

The error is reported (console and `window` `error` event), and the browser continues with the next callback. One broken rAF callback does not stop other rAF callbacks in the same frame, and one broken listener does not stop the other listeners for the same event.

Microtasks queued by the failing callback before it threw still run at the next checkpoint. Only the rest of the throwing function is skipped.

## 350: What is the difference between deep recursion with microtasks and deep recursion on the stack?

Synchronous recursion uses the call stack. It fails fast with "Maximum call stack size exceeded".

Recursion through microtasks (`queueMicrotask(loop)` or `then(loop)`) does not grow the stack, because each microtask starts with an empty stack. It never hits a stack limit. Instead it can run forever (freezing the page) or slowly use up memory if each step keeps data alive.

Recursion through tasks (`setTimeout(loop)`) also does not grow the stack and keeps the page responsive, but it is slower because of task overhead and clamping.

## 351: How can pending promises cause memory leaks?

A pending promise keeps its reaction callbacks alive, and those callbacks keep their closures alive. If a promise never settles (for example it waits for an event that never comes), everything those callbacks reference stays in memory.

```js
function waitForReady(el) {
  return new Promise((resolve) => {
    el.addEventListener("ready", resolve, { once: true });
  });
}

// If "ready" never fires, the listener, the promise and whatever
// awaits it (with its local variables) are kept as long as el is alive.
```

Fixes: add timeouts or abort signals to waits, remove listeners on cleanup, and avoid long-lived promise chains that keep growing (like a "queue" built by chaining `then` forever without the chain being released).

## 352: How does Zone.js work, and why can it not patch native async/await?

Zone.js replaces browser APIs (`setTimeout`, `addEventListener`, `Promise`, `fetch`, `MutationObserver` and many more) with wrappers. Each wrapper remembers the current "zone" when the callback is scheduled and restores it when the callback runs, so the framework knows when async work starts and ends.

Native `async/await` does not call the global `Promise.prototype.then`. The engine resumes the function internally, so Zone.js cannot see it. That is why Angular apps using Zone.js had to compile `async/await` down to generators and promises (ES2017 target). Zoneless Angular removes this limitation.

## 353: How does zoneless Angular schedule change detection?

Without Zone.js, Angular schedules a change detection run when it knows something changed:

- a signal read in a template changes,
- a template event listener runs,
- `markForCheck()` is called (for example by the `async` pipe),
- a component input changes or views are attached or removed.

The scheduler batches these notifications and runs one change detection pass. It races `setTimeout` against `requestAnimationFrame`, so updates are applied quickly and normally before the next paint. Because it no longer runs after every async callback, there are far fewer unnecessary checks.

## 354: How does React prioritize updates relative to the event loop?

React assigns each update a "lane" (a priority):

- **SyncLane**: updates from discrete events like clicks and key presses. React processes them in a microtask right after the event handler, so the result is ready before the next paint.
- **DefaultLane**: updates from timers, network responses and so on. They are processed through the scheduler in a task.
- **Transition lanes**: updates wrapped in `startTransition`. They render in time slices of about 5 ms, yield between slices and can be interrupted by more urgent updates.

So React uses microtasks for urgent work and tasks with time slicing for non-urgent work.

## 355: How does Vue's scheduler order updates and watchers?

Vue collects jobs in queues and flushes them in a microtask:

- **pre** jobs: watchers with `flush: 'pre'` (the default) run before component updates.
- component update jobs, sorted by component id so parents update before children.
- **post** jobs: watchers with `flush: 'post'` and some lifecycle hooks run after the DOM is updated.

`flush: 'sync'` watchers skip the queue and run right away on every change, which is useful but can be expensive. `nextTick()` waits for the flush to finish.

## 356: Should an event bus deliver events synchronously or asynchronously?

**Synchronous delivery**

- Pros: simple, predictable, listeners see the state at the moment of the event, and the caller knows all listeners ran.
- Cons: a slow listener blocks the emitter, re-entrancy bugs (a listener emits another event while the first is still being processed), errors can break the caller if not isolated.

**Async delivery (microtask or task)**

- Pros: the emitter is never blocked by listeners, no re-entrancy, natural batching.
- Cons: listeners may see a newer state than when the event was emitted, harder to debug and test, ordering across buses is harder to reason about.

A common compromise: deliver synchronously but isolate errors with `try/catch` + `reportError`, and let listeners defer heavy work themselves.

## 357: A search box filters 10,000 items and typing feels slow. How do you fix it?

1. **Measure**: record a trace while typing. You will likely see one long task per keystroke for filtering and rendering.
2. **Keep the input fast**: let the input update on its own (do not re-render the whole list synchronously on every key).
3. **Defer the expensive part**: debounce the filter (150 to 300 ms), or use `startTransition`/`useDeferredValue` in React so the list renders at lower priority and can be interrupted.
4. **Render less**: virtualize the result list.
5. **Make filtering cheaper**: precompute lowercase strings, use an index, or move it to a worker for very large data.
6. **Cancel stale work**: if a new key arrives, drop the old filtering job.

## 358: An animation stutters every few seconds. How do you find the cause?

Record a trace in the Performance panel during the stutter and look at what happens on the main thread at those moments:

- **Long tasks from timers or intervals**: periodic polling, analytics flushing or autosave.
- **Garbage collection**: "Major GC" or "Minor GC" blocks; often caused by allocating many objects per frame (creating arrays or objects in the rAF loop).
- **Layout or style work**: something changing classes on large parts of the page.
- **Image decoding** when new images appear.

Fixes: move periodic work to idle time or a worker, reuse objects in the animation loop, animate only `transform` and `opacity` so the compositor can do it, and decode images before showing them.

## 359: A tooltip flickers and the page is slow when you hover over a list. What is likely going on?

A common cause is layout thrashing in a `mousemove` or `mouseover` handler: the code reads `getBoundingClientRect()` of the target, writes the tooltip's `top`/`left`, then reads again, and so on, sometimes for many elements. Each read after a write forces layout. The tooltip may also be positioned before its content is set, so it jumps on the next frame.

Fix it by:

- doing all reads first, then all writes, inside one rAF callback per frame,
- positioning with `transform` instead of `top`/`left`,
- setting content before measuring the tooltip,
- or using CSS anchor positioning where supported, which removes most of the JavaScript.

## 360: A dashboard gets slower the longer it stays open. What do you check?

This usually means work or memory grows over time:

- **Intervals or listeners that are never removed**: each navigation or widget re-mount adds another one, so after an hour you have 50 intervals doing the same thing.
- **Growing data structures**: arrays of history points or logs that are never trimmed.
- **Detached DOM nodes**: elements removed from the page but still referenced from JavaScript.
- **Observers not disconnected**.

Use the Performance panel to see whether there are more tasks per second than at the start, and the Memory panel (heap snapshots, "Detached elements") to find leaks. Fix with proper cleanup and caps on data size.

## 361: Your INP is poor and the slowest interactions are simple clicks. The handlers look tiny. What could it be?

The click handler may be small, but other things can run in the same interaction:

- **Third-party listeners** on the same click (analytics, tag managers, A/B testing tools) doing heavy work.
- **Framework re-renders** caused by a small state change that updates a large tree.
- **Input delay**: a long task that was already running when the user clicked (hydration, polling, a big `setInterval` job).
- **Presentation delay**: a large style or layout recalculation after the change.

Use LoAF data (or the `web-vitals` attribution build) to see which scripts ran during the slow frames and whether the time went to input delay, processing or rendering.

## 362: An infinite scroll feed is janky. How would you improve it?

- Replace scroll listeners with an `IntersectionObserver` on a sentinel element near the end of the list.
- Prefetch the next page before the user reaches the end (use `rootMargin`).
- Append new items in one batch with a fragment, not one by one.
- Virtualize the list or use `content-visibility: auto` on items so off-screen items cost less.
- Reserve space for images (`width`/`height` or `aspect-ratio`) to avoid layout shifts.
- Decode images off the critical path (`decoding="async"`, `loading="lazy"`).
- Keep any scroll-linked effect in CSS (scroll-driven animations) instead of JavaScript.

## 363: Exporting a large CSV freezes the page for several seconds. What do you do?

- Move the export to a Web Worker: send the data (or let the worker fetch it), build the CSV there and send back a `Blob`.
- If it must stay on the main thread, build the CSV in chunks and yield between chunks, updating a progress indicator.
- Avoid building one giant string with `+=` in a loop; collect chunks in an array and create a `Blob` from the array, which avoids extra copies.
- For really big exports, stream them to a file with the File System Access API where available, or generate them on the server.

```js
// worker.js
self.onmessage = ({ data: rows }) => {
  const parts = rows.map((r) => r.map(escapeCsv).join(",") + "\n");
  self.postMessage(new Blob(parts, { type: "text/csv" }));
};
```

## 364: Scrolling through an image gallery is janky. What could be blocking?

- **Image decoding** of large images on the main thread when they enter the viewport.
- **Layout shifts** because images have no reserved size.
- **Scroll handlers** doing work on every frame.
- **Too many images** loaded at full resolution.

Fixes: serve images at the displayed size (`srcset`, `sizes`), use `loading="lazy"` and `decoding="async"`, set `width` and `height`, decode before inserting (`img.decode()`) for dynamic galleries, and use thumbnails in the grid.

## 365: A test passes locally but fails randomly in CI. How can event loop assumptions cause this?

Common causes:

- The test assumes a fixed order between a timer and a network response, a timer and rAF, or two different task sources.
- The test waits a fixed time (`await sleep(100)`) for something that is slower on a busy CI machine.
- A single `await Promise.resolve()` is used to "flush" work that actually needs several microtasks or a task.
- Fake timers are mixed with real async APIs, so some callbacks run and some do not.

Fixes: wait for conditions (`waitFor`, `findBy*`, polling assertions) instead of time, use async fake timer helpers, and remove order assumptions between unrelated sources.

## 366: A modal's closing animation is cut off. What is wrong and how do you fix it?

Usually the element is removed from the DOM in the same task that starts the closing transition. The browser never renders the transition, because the element is gone before the next frame.

```js
// Wrong
modal.classList.add("closing");
modal.remove();

// Right: wait for the transition (with a fallback timeout)
modal.classList.add("closing");
await Promise.race([
  new Promise((r) =>
    modal.addEventListener("transitionend", r, { once: true }),
  ),
  new Promise((r) => setTimeout(r, 400)),
]);
modal.remove();
```

The timeout fallback matters: `transitionend` does not fire if the transition is cancelled or the user has reduced motion settings that remove it. With the Web Animations API, you can await `animation.finished` instead.

## 367: getBoundingClientRect returns zeros for an element you just created. Why?

Layout values are computed for elements that are in the document and rendered. You get zeros if:

- the element is not attached to the document yet,
- it or a parent has `display: none`,
- it is inside a closed `<details>` or a hidden `<dialog>`,
- it is in a `content-visibility: hidden` subtree.

Timing is not the problem: once the element is attached and visible, reading its rect forces layout and gives correct numbers in the same task. If the size depends on a web font or image that is still loading, the value can change later; wait for `document.fonts.ready` or the image's `load`/`decode`, or use a `ResizeObserver`.

## 368: A page hangs right after load and DevTools shows no long JavaScript task in the flame chart. How do you find the cause?

If the tab is fully frozen, you may not be able to stop a recording. Instead:

1. Open the **Sources** panel and press **Pause** (or F8). DevTools stops wherever JavaScript is running.
2. Look at the call stack. If it is inside a microtask (`Promise.then`, `queueMicrotask`) that keeps re-queuing itself, it is microtask starvation; if it is in a loop, it is a synchronous infinite loop.
3. Check async stack traces to find which code started the chain.

You can also enable "Pause on caught exceptions" or add conditional breakpoints in suspected code to catch the loop early.

## 369: How would you design a Web Worker pool?

- Create `navigator.hardwareConcurrency - 1` workers (with a cap), lazily, so you do not start more threads than needed.
- Keep a queue of jobs. When a worker is free, give it the next job; when it finishes, resolve that job's promise and pick the next one.
- Use job ids to match responses to requests.
- Transfer large data instead of copying it.
- Support cancellation: either let the worker check a cancel flag between steps or terminate it and start a new one.
- Handle worker errors (`error` and `messageerror` events), and restart crashed workers.
- Terminate idle workers after some time to free memory.

```js
class WorkerPool {
  #idle = [];
  #queue = [];

  constructor(url, size) {
    for (let i = 0; i < size; i++) {
      this.#idle.push(new Worker(url, { type: "module" }));
    }
  }

  run(data, transfer = []) {
    return new Promise((resolve, reject) => {
      this.#queue.push({ data, transfer, resolve, reject });
      this.#next();
    });
  }

  #next() {
    if (!this.#idle.length || !this.#queue.length) return;
    const worker = this.#idle.pop();
    const job = this.#queue.shift();
    worker.onmessage = (e) => {
      job.resolve(e.data);
      this.#idle.push(worker);
      this.#next();
    };
    worker.onerror = (e) => {
      job.reject(e);
      this.#idle.push(worker);
      this.#next();
    };
    worker.postMessage(job.data, job.transfer);
  }
}
```

## 370: How can a worker report progress without flooding the main thread with messages?

Option 1: send progress messages only every N items or every ~100 ms, not on every item.

Option 2: share memory. The worker writes progress into a `SharedArrayBuffer`, and the page reads it once per frame:

```js
// main.js
const progress = new Int32Array(new SharedArrayBuffer(4));
worker.postMessage({ progress, items });

function update() {
  bar.value = Atomics.load(progress, 0) / items.length;
  if (bar.value < 1) requestAnimationFrame(update);
}
requestAnimationFrame(update);

// worker.js
self.onmessage = ({ data: { progress, items } }) => {
  items.forEach((item, i) => {
    process(item);
    Atomics.store(progress, 0, i + 1);
  });
};
```

The second option needs cross-origin isolation.

## 371: A worker sends results back very fast and the page becomes slow. Why, and how do you fix it?

Each message is a task on the main thread, and each one costs deserialization time plus whatever your handler does (often a DOM update). Thousands of messages per second can keep the main thread busy even though the "heavy work" is in the worker.

Fixes:

- Batch results in the worker and send them every ~16 to 100 ms.
- On the page, just store incoming data in the handler and render once per frame.
- Send compact data (typed arrays, transferables) instead of large object graphs.
- Do as much formatting and filtering as possible in the worker so the page receives only what it needs to show.

## 372: How do you build a canvas game loop with a fixed time step?

Use rAF for drawing and a fixed step for the game logic, so the simulation behaves the same at any frame rate.

```js
const STEP = 1000 / 60; // 60 updates per second
let last = performance.now();
let acc = 0;

function frame(now) {
  acc += Math.min(now - last, 250); // avoid a huge catch-up after a pause
  last = now;

  while (acc >= STEP) {
    update(STEP); // physics, input, game state
    acc -= STEP;
  }

  render(acc / STEP); // interpolate between states for smooth drawing
  requestAnimationFrame(frame);
}

requestAnimationFrame(frame);
```

Capping the elapsed time avoids running hundreds of updates after the tab was hidden (when rAF was paused).

## 373: Users report that the page ignores clicks for a few seconds after it loads. What is happening?

The page looks ready (it is rendered), but the main thread is still busy: running large bundles, hydrating the whole page, initializing third-party scripts or doing data processing. Clicks during that time wait in the queue (high input delay), or worse, the click lands before the listener is attached and does nothing.

Fixes:

- Ship less JavaScript and split bundles by route.
- Use partial, lazy or progressive hydration.
- Break long startup work into chunks and yield.
- Load third-party scripts later.
- For critical buttons, make them work without JavaScript (real links, real forms) or capture early clicks and replay them after hydration.

## 374: In an autocomplete, clicking a suggestion closes the list before the click is handled. Why?

Event order. When the user presses the mouse on a suggestion, the input loses focus first: `pointerdown`, `mousedown`, then `blur`/`focusout` on the input, and only later `mouseup` and `click`. If the `blur` handler hides the list, the element is gone (or moved) by the time `click` would fire, so the click never reaches it.

Fixes:

- Handle selection on `pointerdown`/`mousedown` instead of `click`.
- Call `preventDefault()` in `mousedown` on the list, which keeps focus in the input.
- In the `blur` handler, check `event.relatedTarget` and do not close if focus is moving into the list.

## 375: How does top-level await in a module affect the event loop?

A module with top-level `await` becomes asynchronous: its evaluation pauses at the `await`, and modules that import it (directly or indirectly) wait for it to finish. Other unrelated code, events and rendering can continue in the meantime, because the module evaluation is suspended, not blocking.

```js
// config.js
const res = await fetch("/config.json");
export const config = await res.json();

// main.js
import { config } from "./config.js"; // main.js waits until config.js finishes
```

The downside is that a slow top-level `await` delays everything that depends on that module, which can delay startup. Use it for small, required setup, not for slow or optional work.

## 376: When does code from a dynamic import() run?

`import()` returns a promise. The browser fetches the module and its dependencies (network tasks), parses them, and then evaluates the module graph in a task. The module's top-level code runs during that evaluation, and then the promise resolves with the module namespace, so your `then` or the code after `await` runs as a microtask after the evaluation.

```js
button.addEventListener("click", async () => {
  const { openEditor } = await import("./editor.js");
  openEditor();
});
```

If `editor.js` is large, evaluating it can itself be a long task. Preloading it (`<link rel="modulepreload">`) on hover or idle time can make the click faster.

## 377: Why is document.write bad for the event loop?

`document.write` inserts HTML into the parser stream while parsing. If it writes a `<script src>`, the parser has to stop, fetch and run that script before continuing, which blocks rendering. Chrome even blocks `document.write`-inserted scripts in some slow network conditions.

Calling `document.write` after the page has loaded is worse: it replaces the whole document. Avoid it; use DOM methods or `async`/`defer` scripts instead.

## 378: What stops a page from entering the back/forward cache, and why does it matter for the event loop?

Common blockers (they vary by browser):

- `unload` event listeners,
- `Cache-Control: no-store` on the main document (in some browsers),
- open connections like WebSocket or WebRTC that cannot be paused,
- in-progress IndexedDB transactions or held Web Locks,
- the page being opened by another window that still references it.

When a page is in the bfcache, all its tasks, timers and promise jobs are paused instead of thrown away. When the user goes back, they resume. So if your page is bfcache-eligible, code must handle "time jumped": refresh stale data on `pageshow` with `persisted === true`, and reconnect closed connections.

## 379: How does Safari's Low Power Mode affect requestAnimationFrame?

On iOS and macOS with Low Power Mode on, Safari can limit rendering to 30 frames per second, so rAF callbacks run about every 33 ms instead of every 16.7 ms. Safari can also throttle rAF in cross-origin iframes the user has not interacted with.

If your animation logic assumes a fixed number of frames per second, it will run at half speed. Time-based animation (using the rAF timestamp) handles this correctly.

## 380: Why can event loop quiz answers differ between browsers?

The parts that are strictly specified give the same answers everywhere: synchronous code, microtask order, the fact that all microtasks run before the next task, and the order of timers with the same delay.

The parts left to the browser can differ:

- which task queue goes first (timer vs. message vs. network),
- when rendering happens relative to a given timer, so rAF vs. `setTimeout` order,
- timer clamping and throttling,
- some event dispatch details.

Old engines also had bugs or older spec behavior (for example the pre-ES2019 `await` timing), which is why some older articles show different outputs.

## 381: How do browsers throttle cross-origin iframes?

Chromium throttles rendering (and rAF) in cross-origin iframes that are not visible, for example scrolled out of view or `display: none`. It may also throttle their timers. Safari can throttle cross-origin iframes the user has not interacted with.

This saves resources on pages with many embeds, but it means an embedded widget cannot count on rAF running while off-screen. Widgets should use `IntersectionObserver` and time-based logic.

## 382: How can you detect main thread hangs in production with a heartbeat?

Schedule a repeating timer and measure how late it fires. If it fires much later than expected, the main thread was blocked.

```js
const INTERVAL = 100;
let expected = performance.now() + INTERVAL;

function heartbeat() {
  const lag = performance.now() - expected;
  if (lag > 200 && document.visibilityState === "visible") {
    report({ type: "main-thread-lag", lag: Math.round(lag) });
  }
  expected = performance.now() + INTERVAL;
  setTimeout(heartbeat, INTERVAL);
}

setTimeout(heartbeat, INTERVAL);
```

This works in all browsers, but it is rough and adds a small cost. In Chromium, LoAF gives much better data with no polling. Ignore lag while the page is hidden, since timers are throttled then.

## 383: What is the JS Self-Profiling API?

It lets a page sample its own JavaScript call stacks in production, like a lightweight profiler. The page must be served with the `Document-Policy: js-profiling` header, and it is available in Chromium browsers.

```js
const profiler = new Profiler({ sampleInterval: 10, maxBufferSize: 10_000 });

await doSomethingSlow();

const trace = await profiler.stop();
sendToServer(trace); // frames, stacks and samples
```

Combined with LoAF or long task data, it can show which functions were running during slow frames for real users. It has some overhead, so teams usually enable it for a small sample of sessions.

## 384: How does priority inheritance work with postTask and TaskSignal?

- A task posted with a `signal` from a `TaskController` gets its priority from the signal, and changes with `controller.setPriority()`.
- `scheduler.yield()` inside such a task inherits the task's signal, so the continuation keeps the same priority and is aborted if the controller aborts.
- `TaskSignal.any([...signals], { priority })` creates a signal that aborts when any input aborts, with a fixed or inherited priority.

```js
const controller = new TaskController({ priority: "background" });

scheduler.postTask(
  async () => {
    for (const chunk of chunks) {
      processChunk(chunk);
      await scheduler.yield(); // stays background, cancelled with the controller
    }
  },
  { signal: controller.signal },
);
```

Support for these details follows `postTask` support, so test in your target browsers.

## 385: Why does Web Audio use an AudioWorklet instead of the main thread?

Audio must be produced on a strict schedule. If samples are late by even a few milliseconds, you hear clicks or gaps. The main thread can be blocked at any time by layout, GC or long tasks, so it cannot be trusted with real-time audio.

`AudioWorkletProcessor` code runs on the audio rendering thread, with its own small worklet event loop. The browser calls its `process()` method for each block of 128 samples. You communicate with it through `port.postMessage`, and the main thread can be slow without causing audio glitches.

## 386: What are paint worklets and where do they run?

The CSS Painting API lets you register a `paint()` function with `CSS.paintWorklet.addModule()` and use it in CSS (`background-image: paint(myPainter)`). The browser calls it when it needs to paint the element.

Paint worklets run in a worklet global scope with no DOM access and are designed so the browser can run them off the main thread or in parallel. In practice, support is mainly in Chromium, and they are still called as part of the rendering pipeline, so a slow paint function still makes frames slow.

## 387: When do canvas drawings become visible on screen?

Drawing commands on a 2D or WebGL canvas update its buffer immediately, but the canvas is shown on screen during the next rendering update, after your task finishes, just like DOM changes.

For `OffscreenCanvas` in a worker, the frame is committed when the worker's task ends (or in sync with the worker's rAF), and the compositor shows it without needing the main thread. This is why canvas animation in a worker can stay smooth while the page is busy.

## 388: How does WebGPU work with the event loop?

WebGPU commands are recorded and submitted to a queue with `device.queue.submit()`. The GPU runs them later, in parallel with JavaScript. Results come back through promises:

```js
device.queue.submit([commandEncoder.finish()]);

await device.queue.onSubmittedWorkDone(); // GPU finished this work

await readBuffer.mapAsync(GPUMapMode.READ); // safe to read results now
const data = new Float32Array(readBuffer.getMappedRange());
```

So heavy GPU compute does not block the main thread, but reading results back requires waiting for the GPU, which is async. Calling `mapAsync` too often in a loop adds latency because each call waits for the GPU and the event loop.

## 389: How does backpressure work in the Streams API?

Each stream has a queue and a `highWaterMark` (how much it should buffer). `desiredSize` tells the producer how much more it should enqueue. When the consumer reads slowly, the queue fills up, `desiredSize` goes to zero or below, and a well-behaved source stops producing until the consumer catches up.

```js
const stream = new ReadableStream(
  {
    async pull(controller) {
      // called only when the consumer wants more data
      const chunk = await getNextChunk();
      if (chunk) controller.enqueue(chunk);
      else controller.close();
    },
  },
  { highWaterMark: 4 },
);
```

Using `pull` instead of pushing everything in `start` lets the event loop pace the producer to the consumer, which keeps memory and main thread work under control.

## 390: Why can reading a stream in tiny chunks be slow?

Each `await reader.read()` involves promises and at least one microtask hop. If chunks are tiny (a few bytes), most of the time goes into the overhead of creating promises and running microtasks rather than the actual work. If all chunks are already buffered, the loop also runs through microtasks without yielding to rendering.

Use reasonable chunk sizes, combine small chunks before processing, use `pipeThrough` with built-in transform streams (like `TextDecoderStream` and `DecompressionStream`), and yield explicitly if processing is heavy.

## 391: How do you process a huge text download without blocking the page?

Stream it, decode it incrementally, and handle it line by line:

```js
const res = await fetch("/logs.ndjson");
const lines = res.body
  .pipeThrough(new TextDecoderStream())
  .pipeThrough(splitLines()); // a TransformStream that splits on "\n"

let count = 0;
for await (const line of lines) {
  handle(JSON.parse(line));
  if (++count % 1000 === 0) await yieldToMain();
}
```

Iterating a `ReadableStream` with `for await` works in Chrome and Firefox, but Safari support has lagged, so check it or use `getReader()` instead. You never hold the whole response as one string, and the page stays responsive. For even larger data, run the same code in a worker.

## 392: How expensive is structuredClone?

`structuredClone(value)` does a deep copy using the same algorithm as `postMessage`. It is synchronous and runs on the calling thread. Its cost grows with the size and number of objects: cloning a large nested object can take tens or hundreds of milliseconds.

It also copies `ArrayBuffer`s unless you transfer them:

```js
const copy = structuredClone(bigState); // blocks while copying

const moved = structuredClone({ buffer }, { transfer: [buffer] }); // no copy, buffer detached
```

Do not clone large state on every update. Use immutable updates (sharing unchanged parts) or keep big data in one place.

## 393: What are transferable streams?

`ReadableStream`, `WritableStream` and `TransformStream` can be transferred to a worker with `postMessage`. The data then flows between threads through the stream, with backpressure, without you writing a message protocol.

```js
// main.js
const res = await fetch("/big-file");
worker.postMessage({ stream: res.body }, [res.body]);

// worker.js
self.onmessage = async ({ data: { stream } }) => {
  const reader = stream.getReader();
  while (true) {
    const { done, value } = await reader.read();
    if (done) break;
    processChunk(value);
  }
};
```

The worker reads the network data as it arrives, and the main thread barely touches it.

## 394: How do postMessage, SharedArrayBuffer and BroadcastChannel compare for talking to workers?

- **postMessage**: simple, works everywhere, copies data (or transfers buffers). Each message is a task on the receiver. Good default.
- **SharedArrayBuffer + Atomics**: zero-copy shared memory, very fast for numeric data and progress counters. Needs cross-origin isolation and careful synchronization. No notifications by itself; combine with `Atomics.notify`/`waitAsync` or polling.
- **BroadcastChannel**: one-to-many messages between same-origin contexts (tabs, workers). Convenient for "tell everyone" events, but always copies data and has no request/response pairing.
- **MessageChannel**: a private two-way pipe you can hand to another context, good for connecting two workers directly.

## 395: How would you design an app-wide scheduling helper?

A small module that hides browser differences and gives the team clear choices:

```js
const hasPostTask = typeof globalThis.scheduler?.postTask === "function";
const hasYield = typeof globalThis.scheduler?.yield === "function";

export function yieldToMain() {
  if (hasYield) return scheduler.yield();
  return new Promise((r) => setTimeout(r, 0));
}

export function runLater(fn, priority = "user-visible") {
  if (hasPostTask) return scheduler.postTask(fn, { priority });
  const delay = priority === "background" ? 100 : 0;
  return new Promise((resolve, reject) =>
    setTimeout(() => {
      try {
        resolve(fn());
      } catch (e) {
        reject(e);
      }
    }, delay),
  );
}

export function beforeNextPaint(fn) {
  return requestAnimationFrame(fn);
}

export function afterNextPaint(fn) {
  requestAnimationFrame(() => setTimeout(fn, 0));
}
```

The point is a shared vocabulary ("urgent", "visible", "background", "before paint", "after paint") so code is consistent and easy to change when browser support improves.

## 396: How would you approximate scheduler.yield's priority in a polyfill?

You cannot get the real "continuation queue" without browser support, but you can get closer than plain `setTimeout`:

- Use a `MessageChannel` message instead of `setTimeout` to avoid the 4 ms clamp.
- Keep your own queue of continuations and resolve them all from one message handler, in order, before other app-level work you control.
- If `scheduler.postTask` exists but not `yield`, use `postTask` with `user-blocking` priority as the continuation.

```js
export function yieldPolyfill() {
  if (globalThis.scheduler?.yield) return scheduler.yield();
  if (globalThis.scheduler?.postTask) {
    return scheduler.postTask(() => {}, { priority: "user-blocking" });
  }
  return new Promise((resolve) => {
    const { port1, port2 } = new MessageChannel();
    port1.onmessage = () => {
      port1.close();
      resolve();
    };
    port2.postMessage(null);
  });
}
```

## 397: How do you run several long jobs fairly without one hogging the main thread?

Use round-robin: give each job a small time slice in turn, then yield.

```js
async function runFairly(jobs, sliceMs = 4) {
  // each job is an iterator; next() does one small unit of work
  const active = [...jobs];
  while (active.length) {
    const start = performance.now();
    for (let i = 0; i < active.length; i++) {
      const sliceEnd = performance.now() + sliceMs;
      while (performance.now() < sliceEnd) {
        if (active[i].next().done) {
          active.splice(i--, 1);
          break;
        }
      }
      if (performance.now() - start > 12) break; // keep the whole task short
    }
    await yieldToMain();
  }
}
```

Each job gets a turn every round, and the whole task stays well under the 50 ms long task limit.

## 398: What are good patterns for cancelling scheduled work?

- **Timers and frames**: keep the id and call `clearTimeout`, `clearInterval` or `cancelAnimationFrame` in cleanup.
- **Async functions**: pass an `AbortSignal` and check `signal.aborted` (or call `signal.throwIfAborted()`) after each `await`.
- **APIs that accept a signal**: `fetch`, `addEventListener`, `scheduler.postTask` and streams take a signal directly.
- **Workers**: send a cancel message the worker checks between steps, or `terminate()` it.
- **Generation counters**: increment a counter when starting new work, and have old work check that it is still the current generation before applying results.

```js
async function loadAll(ids, signal) {
  for (const id of ids) {
    signal.throwIfAborted();
    await loadOne(id, { signal });
    await yieldToMain();
  }
}
```

## 399: What ordering guarantees can you rely on across browsers?

Safe to rely on:

- Synchronous code runs to completion.
- Microtasks run in the order queued, and all of them run before the next task and before rendering.
- `then` callbacks on the same promise run in registration order.
- Tasks from the same task source run in order (timers with the same delay, messages on one port, events in dispatch order).
- rAF callbacks in a frame run in registration order and before style and layout of that frame.

Not safe to rely on:

- Order between different task sources (timer vs. network vs. message).
- Order between `setTimeout` and rAF.
- Exact timer delays or frame timing.
- How many frames happen between two tasks.

## 400: How can the event loop be used in timing side-channel attacks?

When two documents share an event loop (or a process), one can measure how busy the other is. An attacker page can post many small tasks or messages and measure gaps between them. When a cross-origin document running in the same event loop does work, the gaps get larger, which can leak information like which page the user is on or how big a response was.

Mitigations in browsers: site isolation (separate processes and event loops for different sites), lower timer precision, cross-origin isolation requirements for high-resolution timers and `SharedArrayBuffer`, and headers like COOP that cut links between windows. For your own site, using COOP and avoiding being framed by untrusted sites (`frame-ancestors` in CSP) reduces exposure.

## 401: How does garbage collection interact with the event loop?

The JavaScript heap has to be cleaned up on some thread. Modern engines (V8's Orinoco, SpiderMonkey, JavaScriptCore) do most of the marking and sweeping concurrently on helper threads, but some steps still pause the main thread:

- **Minor GC** (young generation): short pauses, frequent if you allocate a lot.
- **Major GC**: mostly concurrent, with smaller main thread pauses for finalization.

Chrome also uses idle time between frames for some GC work, which is one reason idle periods matter. In a performance trace, GC shows as "Minor GC" or "Major GC" blocks inside tasks. Lots of allocation in hot code (per frame, per event) means more frequent pauses.

## 402: How do you reduce GC pauses in an animation or game loop?

Allocate less per frame:

- Reuse objects and arrays instead of creating new ones every frame.
- Use typed arrays for numeric data (positions, velocities).
- Avoid creating closures, temporary strings (template literals in hot loops) and spread copies per frame.
- Use object pools for things like particles or bullets.

```js
// Allocates a new object every frame
function updateBad(p) {
  return { x: p.x + p.vx, y: p.y + p.vy };
}

// Updates in place
function updateGood(p) {
  p.x += p.vx;
  p.y += p.vy;
}
```

Check the Memory panel's allocation timeline or the Performance panel's GC events to see if this matters for your case.

## 403: What is the "latest value wins" pattern and when should you use it?

When updates come faster than you can show them, process only the newest one and drop the rest. Queuing every update just builds lag: the screen shows older and older states.

```js
let pending = null;
let busy = false;

async function onData(value) {
  pending = value;
  if (busy) return;
  busy = true;
  while (pending !== null) {
    const v = pending;
    pending = null;
    await render(v); // may take longer than updates arrive
  }
  busy = false;
}
```

Use it for things like live charts, cursor positions, search previews and progress indicators. Do not use it where every message matters (chat messages, financial transactions).

## 404: What happens if requestAnimationFrame callbacks take longer than a frame?

The frame cannot be produced on time, so it is dropped or delayed. The browser finishes the callbacks, does style, layout and paint, and shows that frame late. The next rAF callbacks run at the next opportunity, so you effectively get a lower frame rate.

Because each frame passes the start time, a time-based animation still lands in the right position, it just looks less smooth. If rAF work is heavy, move the calculation to a worker and keep rAF for applying the results.

## 405: How do variable refresh rate displays affect rAF?

On 120 Hz and adaptive displays (ProMotion, VRR monitors), the browser may run rAF at 120 Hz, at 60 Hz, or change the rate on the fly depending on content, power state and browser policy. Some browsers limit rAF to 60 Hz in certain cases; others follow the display.

So:

- never assume a fixed frame duration,
- compute movement from the rAF timestamp,
- remember the per-frame budget can be about 8 ms, which makes heavy rAF work more likely to drop frames on fast screens.

## 406: Describe what happens from a physical click to the next paint.

1. The OS delivers the mouse event to the browser process.
2. The browser process finds the right tab and sends the event to its renderer process (or to the right iframe's process).
3. The renderer's compositor thread receives it. For a click, it must go to the main thread.
4. The main thread scheduler queues an input task. If a long task is running, it waits (input delay).
5. The task runs: hit testing finds the target, then `pointerdown`, `mousedown`, `pointerup`, `mouseup`, `click` are dispatched (some may be separate tasks), with microtasks after each listener.
6. Your handler changes the DOM.
7. At the next frame, the rendering step runs: rAF, style, layout, paint, commit.
8. The compositor and GPU process put the frame on screen.

INP for this interaction is the time from step 1's event timestamp to step 8.

## 407: Describe what happens to a fetch() call, from call to callback.

1. `fetch()` runs synchronously: it creates a request and a promise, and hands the request to the browser's network service (another process or thread).
2. Your code continues; the main thread is free.
3. The network service does DNS, connection, sends the request and receives the response headers (possibly through a service worker first).
4. A task is queued on the networking task source to resolve the fetch promise with a `Response`.
5. When that task runs, the promise is resolved and your `then`/`await` continuation runs as a microtask.
6. Calling `res.json()` starts reading the body. Body chunks arrive in more tasks; when the body is complete, it is parsed (on the main thread) and the `json()` promise resolves, scheduling another microtask.

So one `await (await fetch(url)).json()` involves at least two network tasks and several microtasks.

## 408: How does the compositor decide whether input needs the main thread?

The compositor keeps a map of regions where scrolling or touch input might be handled by JavaScript (sometimes called non-fast scrollable regions or touch-action regions). It is built from:

- elements with non-passive `wheel`, `touchstart` or `touchmove` listeners,
- `touch-action` CSS values,
- some scroll containers the compositor cannot scroll by itself.

If input hits outside these regions, the compositor scrolls directly. If it hits inside, it has to ask the main thread and wait for the listener to decide. That is why a non-passive listener on `document` can make scrolling depend on the main thread for the whole page.

## 409: How do View Transitions interact with the event loop?

`document.startViewTransition(updateCallback)`:

1. Captures the current state of the page. This needs a rendering step, so the update callback is not called synchronously.
2. Calls your update callback in a later task, with rendering paused, so the user does not see the in-between state.
3. Waits for the promise returned by the callback (`transition.updateCallbackDone`).
4. Captures the new state and runs the animation (`transition.ready` resolves, then `transition.finished`).

```js
const transition = document.startViewTransition(async () => {
  await updateDom(); // rendering is paused while this runs
});
await transition.finished;
```

Because rendering is paused during the update, a slow callback freezes the screen. If it takes too long, the browser abandons the transition. Keep the callback quick, and do data loading before starting the transition.

## 410: How does the HTML parser share the main thread with other work during page load?

Parsing runs in tasks. The parser does not parse the whole document in one go; Chromium's parser, for example, stops after a time budget or a number of tokens and posts a new task to continue. Between those tasks the browser can run other tasks and render, which is how users see partial content before the page is fully loaded.

Parser-blocking scripts stop this process: the parser waits for the script to load and run. Very large inline scripts or many synchronous scripts in the `<body>` make loading feel slow even when the network is fast.

## 411: What are render-blocking resources and how do they relate to rendering opportunities?

Stylesheets in the `<head>` (and synchronous scripts that come before them) are render-blocking. Until they load, the browser does not render the document, even if the main thread is idle, because showing unstyled content would cause a flash.

You can also mark elements as render-blocking explicitly:

```html
<link rel="stylesheet" href="critical.css" blocking="render" />
<script src="theme.js" blocking="render" async></script>
```

So "the main thread is free" does not always mean "the page can paint". First paint needs both free main thread time and all render-blocking resources.

## 412: How do you schedule startup work without delaying the first paint?

- Keep only what is needed for the first view in the critical path.
- Load other scripts with `defer`, `type="module"` or dynamic `import()`.
- Start non-critical work after the first paint: use the rAF + `setTimeout` pattern or listen for `load` and then use `requestIdleCallback`/`postTask` with background priority.
- Split initialization into small tasks so the first interactions are not blocked.

```js
addEventListener("load", () => {
  requestAnimationFrame(() => {
    setTimeout(() => {
      initAnalytics();
      prefetchNextRoutes();
    }, 0);
  });
});
```

## 413: What happens if you call requestAnimationFrame from a ResizeObserver callback?

The callback is scheduled for the next frame. `ResizeObserver` callbacks run after the rAF step of the current frame, so the current frame's rAF list has already been processed.

That means changes made in that rAF callback are one frame late. If you want a size-dependent change to appear in the same frame, make it directly in the `ResizeObserver` callback (keeping the loop rules in mind).

## 414: What happens if you change the DOM inside an IntersectionObserver callback?

The callback runs in a task after the frame where the intersection was detected. Any DOM change you make shows up in the next frame. So there is at least one frame where the element is visible but not updated yet.

For lazy loading that is fine. For visual effects that must match scrolling exactly (like a sticky header changing style), the one-frame delay can be visible. CSS options like `position: sticky`, scroll-driven animations or scroll-state container queries avoid that.

## 415: What were Mutation Events and why were they removed?

Mutation Events (`DOMNodeInserted`, `DOMSubtreeModified`, `DOMAttrModified` and others) fired synchronously during every DOM change. That caused serious problems:

- they slowed down every DOM operation, even when no one was listening in the relevant part of the tree,
- listeners could change the DOM in the middle of another DOM operation, causing bugs and crashes,
- they fired once per change, so bulk updates triggered thousands of events.

`MutationObserver` replaced them with batched, asynchronous (microtask) delivery. Chrome removed Mutation Events in version 127, and other browsers are removing them too.

## 416: How does window.open without noopener affect the event loop of both pages?

If you open a same-site page with `window.open` and keep the reference (no `noopener`), the two windows can access each other synchronously. To make that possible, the browser has to keep them in the same process and the same event loop. A long task in one blocks the other.

Using `noopener` (or `rel="noopener"` on links, which is the default for `target="_blank"` in modern browsers) and COOP headers lets the browser put the new page in its own process with its own event loop.

## 417: What are the downsides of using window.postMessage to yourself as a fast task?

`window.postMessage(data, "*")` to the same window queues a task without the timer clamp, and older libraries used it as a `setImmediate` polyfill. Problems:

- Every `message` listener on the window gets your messages, including third-party scripts and other libraries, which may parse or log them.
- Your listener also gets messages from iframes and other windows, so you must filter carefully.
- Data is structured-cloned.

A private `MessageChannel` avoids all of these, and `scheduler.postTask` or `scheduler.yield` are better when supported.

## 418: How do the page's event loop and the service worker's event loop work together during a fetch?

1. The page calls `fetch()`. The request goes to the browser, which sees there is a controlling service worker.
2. The browser starts the service worker if needed and queues a `fetch` event task in the worker's event loop.
3. The worker's handler calls `event.respondWith(promise)`. The worker can do cache lookups, network fetches and so on, all on its own thread.
4. When the response is ready, the browser sends it back, and a task in the page's event loop resolves the page's fetch promise.

The page's main thread is not blocked during this. But a slow service worker (for example one that takes time to start or waits on a busy IndexedDB) makes every request slower.

## 419: Why must event.respondWith be called synchronously in a service worker?

The browser needs to know during the dispatch of the `fetch` event whether the worker will handle the request. When the dispatch ends (all listeners have returned), if nobody called `respondWith`, the browser sends the request to the network as usual.

```js
self.addEventListener("fetch", (event) => {
  // Wrong: respondWith after await is too late
  // const cached = await caches.match(event.request);

  event.respondWith(
    (async () => {
      const cached = await caches.match(event.request);
      return cached ?? fetch(event.request);
    })(),
  );
});
```

Calling it after an `await` throws an `InvalidStateError`. Pass a promise to `respondWith` and do the async work inside it.

## 420: How expensive are calls between JavaScript and the DOM?

Each DOM API call crosses from the JavaScript engine into the browser's C++ code (through bindings). Engines have made this fast, but it is still more costly than plain JavaScript, especially for calls that do real work (style lookup, layout reads, creating nodes).

For the event loop, the impact is that DOM-heavy tasks get long quickly. Ten thousand `appendChild` calls or style changes in a loop add up. Batching changes, building HTML in one go (templates, `replaceChildren`) and doing data work in plain JavaScript before touching the DOM all help.

## 421: How much JavaScript can you run per frame at 60 Hz?

A 60 Hz frame is about 16.7 ms. The browser needs part of that for its own work: input handling, style, layout, paint and commit. On a typical page that can be several milliseconds, more on low-end phones.

A common rule is to keep your JavaScript per frame to around 10 ms or less, and much less inside animation loops on low-end devices. At 120 Hz, the whole frame is 8.3 ms, so even 5 ms of JavaScript may be too much. This is why heavy work belongs in workers or in idle time.

## 422: What is the RAIL model?

RAIL is an older performance model from Google that ties user perception to event loop budgets:

- **Response**: respond to input within 100 ms, so handle events in under 50 ms (because other work may be running).
- **Animation**: produce each frame within 16 ms, which leaves about 10 ms for your code.
- **Idle**: do background work in chunks of 50 ms or less.
- **Load**: show content quickly (originally within about 5 seconds on mid-range mobile).

Today the Core Web Vitals (LCP, INP, CLS) are the main metrics, but RAIL's numbers still explain why the 50 ms long task threshold exists.

## 423: How do you profile event loop behavior on a real mobile device?

- **Android + Chrome**: connect via USB, enable USB debugging, open `chrome://inspect` on desktop, and use DevTools (including the Performance panel) against the phone.
- **iOS + Safari**: enable Web Inspector on the device, connect it to a Mac, and use Safari's Develop menu. The Timelines tab shows JavaScript, layout and rendering.
- **Field data**: collect INP and LoAF data with real user monitoring, since lab tests rarely match real devices.

Desktop CPU throttling helps, but real mid-range phones are often slower in ways throttling does not capture (thermal limits, slower memory, background apps).

## 424: How do you write an automated test that catches main thread blocking?

Run the page in a real browser (for example with Playwright), observe long tasks or LoAF in the page, perform the interaction and assert on the results.

```js
import { test, expect } from "@playwright/test";

test("opening the filter panel does not block the main thread", async ({
  page,
}) => {
  await page.goto("/products");
  await page.evaluate(() => {
    window.__longFrames = [];
    new PerformanceObserver((list) => {
      window.__longFrames.push(...list.getEntries().map((e) => e.duration));
    }).observe({ type: "long-animation-frame" });
  });

  await page.click("#open-filters");
  await page.waitForTimeout(500);

  const longFrames = await page.evaluate(() => window.__longFrames);
  expect(Math.max(0, ...longFrames)).toBeLessThan(100);
});
```

CI machines vary in speed, so use generous thresholds and track trends rather than exact numbers. Lighthouse CI with performance budgets is another option.

## 425: What does this print?

```js
const div = document.createElement("div");
const mo = new MutationObserver((records) => {
  console.log("mutation", records.length);
});
mo.observe(div, { attributes: true });

Promise.resolve().then(() => console.log("promise"));
div.setAttribute("a", "1");
queueMicrotask(() => console.log("microtask"));
div.setAttribute("a", "2");
console.log("sync");
```

Output:

```text
sync
promise
mutation 2
microtask
```

The promise callback is queued first. The first `setAttribute` queues the mutation observer microtask. The second `setAttribute` only adds a record, because that microtask is already queued. `queueMicrotask` runs after the mutation callback because it was queued after it.

## 426: What does this print?

```js
const target = new EventTarget();

target.addEventListener("ping", () => {
  console.log("listener");
  queueMicrotask(() => console.log("micro from listener"));
});

queueMicrotask(() => {
  console.log("micro 1 start");
  target.dispatchEvent(new Event("ping"));
  console.log("micro 1 end");
});

queueMicrotask(() => console.log("micro 2"));
```

Output:

```text
micro 1 start
listener
micro 1 end
micro 2
micro from listener
```

`dispatchEvent` runs the listener synchronously inside micro 1. The microtask queued by the listener goes to the end of the queue, after micro 2. No nested checkpoint happens, because the browser is already performing one.

## 427: What does this print?

```js
async function run() {
  try {
    console.log("try");
    await null;
    return "value";
  } finally {
    console.log("finally");
  }
}

run().then((v) => console.log("then", v));
setTimeout(() => console.log("timeout"), 0);
Promise.resolve().then(() => console.log("p"));
console.log("sync");
```

Output:

```text
try
sync
finally
p
then value
timeout
```

After the synchronous part, the queue holds the continuation of `run` and then `p`. The continuation returns, runs `finally` and resolves `run`'s promise, which queues `then value` after `p`.

## 428: What does this print, and which part is not guaranteed?

```js
setTimeout(() => {
  console.log("timeout 1");
  Promise.resolve().then(() => console.log("micro"));
  requestAnimationFrame(() => console.log("raf"));
  setTimeout(() => console.log("timeout 2"), 0);
}, 0);
```

Guaranteed: `timeout 1` and then `micro`, because microtasks run right after the task.

Not guaranteed: the order of `raf` and `timeout 2`. If a frame is due before the next timer task is picked, `raf` comes first; otherwise `timeout 2` does. Both outputs are valid:

```text
timeout 1
micro
raf
timeout 2
```

```text
timeout 1
micro
timeout 2
raf
```

## 429: Why does a MessagePort sometimes never receive messages?

A `MessagePort` starts with its message queue disabled. Setting `port.onmessage` starts it automatically, but `addEventListener("message", ...)` does not. If you use `addEventListener`, you must call `port.start()`.

```js
const { port1, port2 } = new MessageChannel();

port1.addEventListener("message", (e) => console.log(e.data));
port1.start(); // without this, messages wait forever

port2.postMessage("hello");
```

Until the port is started, messages are queued but not dispatched, which looks like they are lost.

## 430: How are timers, listeners and observers garbage collected?

- **Timers**: a pending timer is held by the browser's timer list, so its callback and closures stay alive until it fires (for `setTimeout`) or until it is cleared. An interval that is never cleared keeps everything it references alive forever.
- **Event listeners**: held by their target. If the element is removed and nothing else references it, the element and its listeners can be collected together. Listeners on `window` or `document` live as long as the page.
- **Observers**: an observer is kept alive while it observes nodes that are alive. Disconnecting or letting the observed nodes go lets it be collected.
- **Pending promises**: kept alive by whatever can still resolve them.

So leaks usually come from long-lived roots (`window`, intervals, global caches) pointing at short-lived things.

## 431: Why is reading layout at the start of a rAF callback cheap, but reading after a write expensive?

At the start of a rAF callback, the last layout is usually still valid. Unless some earlier code in this frame changed the DOM, reading `offsetHeight` or `getBoundingClientRect()` just returns cached values.

After you write (change styles or the DOM), the layout is marked dirty. The next read forces the browser to run style and layout right away, in the middle of your callback. If you do read-write-read-write, it happens again and again.

So a good order inside a frame is: read everything first, then write everything. Some libraries (like fastdom) enforce this by batching reads and writes in rAF.

## 432: How does CSS containment reduce rendering work?

`contain` tells the browser an element's insides do not affect the outside in certain ways, so it can limit how much it recalculates:

- `contain: layout`: layout inside does not affect outside layout, so changes inside do not need a full page layout.
- `contain: paint`: content does not paint outside the box, so the browser can skip painting it when it is off-screen.
- `contain: size`: the element's size does not depend on its children.
- `contain: strict` / `content`: common combinations.

```css
.widget {
  contain: content; /* layout + paint + style */
}
```

For large pages with many independent widgets, this can make each frame's rendering step much cheaper. `content-visibility: auto` builds on the same ideas.

## 433: What are the trade-offs of an off-main-thread architecture?

Moving app logic (state, data processing, business rules) to a worker and keeping only UI on the main thread:

**Pros**

- The main thread stays free for input and rendering.
- Heavy logic cannot cause long tasks on the page.
- Clear separation between UI and logic.

**Cons**

- Every state change crosses threads, with serialization cost and latency (often at least a frame).
- Debugging across threads is harder.
- Libraries that expect the DOM or `window` do not work in the worker.
- More complex build and tooling.

It works well for apps with a lot of computation (editors, data tools, games). For typical CRUD apps, careful chunking on the main thread is often enough.

## 434: How do you coordinate multiple schedulers in one app?

A big app may have React's scheduler, your own `postTask` calls, a data grid library with its own rAF loop and third-party scripts with timers. They do not know about each other, so they can all decide to run at the same time.

Approaches:

- Route your own app work through one helper (see the scheduling helper question) with clear priorities.
- Prefer the browser's scheduler (`postTask`, `scheduler.yield`) where supported, since it is shared by all code on the page.
- Keep each chunk short, so whichever scheduler runs, others get a turn soon.
- Watch LoAF data to find which scheduler is responsible for slow frames.

## 435: Why can you await inside an IndexedDB transaction when using a promise wrapper like idb?

The transaction stays active while its request events are being dispatched. When a request's `success` event fires, the wrapper resolves a promise. Your continuation runs as a microtask right after the event listener returns, still inside that task, while the transaction is active. So you can issue the next request in the continuation.

```js
import { openDB } from "idb";

const db = await openDB("shop", 1);
const tx = db.transaction("cart", "readwrite");
const item = await tx.store.get("apple"); // fine
item.qty += 1;
await tx.store.put(item); // fine: still the same transaction
await tx.done;
```

The rule is: only await IndexedDB requests inside a transaction. Awaiting anything else (a fetch, a timer) lets the task end with no pending requests, and the transaction commits.

## 436: How can you deadlock with Atomics and workers?

`Atomics.wait` blocks a worker until another thread notifies it. A deadlock happens when threads wait for each other:

- Worker A waits for a flag that worker B sets, while B waits for a flag that A sets.
- A worker blocks with `Atomics.wait` waiting for the main thread to respond to a `postMessage`. Fine in theory, but if the main thread is waiting on that worker's result (for example a promise that resolves on its message), neither moves.
- A worker blocks in `Atomics.wait` and so cannot process its own `message` events, including the one that would have told it to continue.

Rules that help: set timeouts on `Atomics.wait`, keep a clear lock order, never block a thread that must process messages to make progress, and prefer `Atomics.waitAsync` where possible.

## 437: Why can Promise.all leave work running and still cause unhandled rejections?

`Promise.all` rejects as soon as one input rejects, but the other operations keep running. Their results are ignored. If several inputs reject, `Promise.all` handles them for you (no unhandled rejection), but the work they started (network requests, timers) continues and may change state later.

```js
const controller = new AbortController();
const { signal } = controller;

try {
  await Promise.all([
    fetch("/a", { signal }),
    fetch("/b", { signal }),
    fetch("/c", { signal }),
  ]);
} catch (err) {
  controller.abort(); // stop the others
  throw err;
}
```

Unhandled rejections happen when you create promises but do not pass them to `Promise.all` right away (for example you create them, then `await` something else first). If one rejects while you are waiting on the other thing, it has no handler yet.

## 438: As a library author, which async primitive should you use to call user callbacks?

It depends on what you promise to users:

- **Synchronous**: simplest and fastest, but user code runs inside your code. Guard with `try/catch` + `reportError` so one bad callback does not break your library's state.
- **queueMicrotask**: consistent "always async" behavior, errors are reported as uncaught errors (not lost in a promise), and it runs before rendering.
- **Promise.then**: errors become rejected promises, which may surface as `unhandledrejection` with less context. Fine if you return the promise to the user.
- **Tasks** (`setTimeout`, `postTask`): use only when you deliberately want the browser to render or handle input first.

Whatever you choose, document it and do not mix: an API that is sometimes sync and sometimes async is a common source of bugs.

## 439: Can a flood of tasks prevent the browser from rendering?

The spec lets the browser choose when to render, so in theory many quick tasks could delay rendering. In practice, browsers protect rendering. Chrome's scheduler, for example, raises the priority of rendering if a frame has been delayed for too long, so a stream of small `postMessage` tasks does not block frames forever.

Microtasks are different: rendering cannot happen during a microtask checkpoint, so an endless microtask chain does block rendering completely. And a single long task blocks rendering no matter what the scheduler wants.

## 440: Can timers be starved by input or rendering?

Partly. When the user is scrolling or interacting, browsers may give input and rendering higher priority, so timer tasks run a bit later. They are not starved forever, since schedulers include protections against starving lower priority queues.

This is another reason timers are not exact. If your logic depends on precise timing during heavy interaction (like a game), use the rAF timestamp or `performance.now()` to compute what should have happened, instead of counting on timers firing on time.

## 441: How does one rendering update handle several documents, like same-origin iframes?

A window event loop can serve several documents (the top page and same-origin iframes in the same agent). In "update the rendering", the browser collects all documents that need rendering and runs each step for all of them, in tree order: resize events for all, then scroll events for all, then rAF callbacks for each document, then style and layout, and so on.

So rAF callbacks in the parent and in a same-origin iframe run in the same frame, parent first. A slow rAF in the iframe delays the parent's frame too.

## 442: How does a background-priority postTask compare with requestIdleCallback?

- **requestIdleCallback** runs only during idle periods, gives you a `deadline`, and may not run at all on a busy page unless you set a `timeout`. Safari support has been weak.
- **postTask with background priority** runs when there are no higher priority tasks, without a deadline object. It is part of the browser's normal task scheduling, supports cancellation and priority changes through `TaskController`, and works well with `scheduler.yield()`.

For splitting non-urgent work into chunks with priorities, `postTask` is usually the better tool. For "only when truly idle, with a time limit per call", `requestIdleCallback` fits better. Both need feature detection.

## 443: How would you migrate a codebase from setTimeout-based chunking to scheduler.yield?

1. Find the places that yield with `setTimeout(..., 0)`, `MessageChannel` tricks or custom `sleep(0)` helpers.
2. Replace them with one shared `yieldToMain()` helper that uses `scheduler.yield()` when available and falls back to `setTimeout`.
3. Check any code that relied on other tasks running before the continuation (with `scheduler.yield`, your continuation now runs before other queued tasks of the same priority).
4. If some work should be lower priority, wrap it in `scheduler.postTask` with a priority, so its yields inherit it.
5. Measure INP and LoAF before and after, and compare browsers with and without support.

## 444: How do you control the main thread time used by third-party scripts?

- Measure it: use LoAF `scripts` entries and group by `sourceURL` to see how much main thread time each vendor takes in real sessions.
- Set budgets per vendor and review them like any other performance budget.
- Delay loading until after the page is interactive or until user intent (facades for chat widgets, video embeds, maps).
- Load them in sandboxed cross-origin iframes when possible, so they run in another process with their own event loop.
- Remove tags that are not used; tag managers tend to collect old scripts.

## 445: How would you explain the event loop on a whiteboard?

Draw four boxes and one loop:

1. **Call stack**: where JavaScript runs right now.
2. **Browser APIs**: timers, network, DOM events, doing their waiting outside the stack.
3. **Task queues**: callbacks waiting to run, picked one at a time.
4. **Microtask queue**: promise callbacks, emptied completely after each task.
5. **Render step**: rAF, style, layout, paint, roughly once per frame.

Then walk through one small example (sync log, `setTimeout`, `Promise.then`, a click) and show where each callback waits and when it moves to the stack. Finish with the main rule: one thing at a time; long tasks block everything, including input and rendering.

## 446: How does the event loop affect LCP and CLS, not just INP?

- **LCP (Largest Contentful Paint)**: the largest element can only be painted when the main thread is free to render. Long tasks during load (big bundles, hydration) delay the frame that shows it, even if the image or text is already loaded. Rendering it with JavaScript (client-side rendering) adds script execution time before LCP can happen.
- **CLS (Cumulative Layout Shift)**: content inserted by late callbacks (ads, banners, fetch results) pushes other content down. The later the task runs, the more likely the user already started reading. Reserving space and avoiding late DOM insertions above existing content keeps CLS low.

## 447: How do you handle "time jumps" in long-lived apps?

A page can be frozen, put in the bfcache, throttled or the device can sleep. When the page runs again, minutes or hours may have passed, but your timers and state think no time passed.

Handle it by:

- storing timestamps, not counters, for anything time-based,
- listening to `visibilitychange`, `pageshow` (with `persisted`), and `resume`, and refreshing data and tokens there,
- checking for large gaps between expected and actual time in your loops,
- reconnecting WebSockets and restarting polling after a resume,
- capping catch-up work so the page does not run hours of missed updates at once.

## 448: Design question: how do you keep typing latency low in a collaborative text editor?

- Apply the user's keystroke to the local document and DOM immediately, with as little work as possible in the input handler.
- Defer everything else: syntax highlighting, spell checking, sending operations to the server, updating outlines or previews. Use `postTask`/`yield` or a worker.
- Batch outgoing operations (for example every 50 ms) instead of one network message per key.
- Apply incoming remote operations in batches once per frame, using the "latest state" approach for presence data like cursors.
- Run heavy merging (CRDT or OT operations on large documents) in a worker if it shows up in profiles.
- Virtualize rendering of very long documents.
- Track INP and keyboard interaction latency in the field.

## 449: Design question: how do you render 100,000 data points smoothly in a chart?

- Do not use one DOM or SVG element per point. Use Canvas 2D or WebGL/WebGPU.
- Downsample on the fly to about the number of pixels available (for example min/max per pixel column), so you draw thousands, not 100,000, items per frame.
- Do data processing (downsampling, aggregation, layout) in a worker, and draw with `OffscreenCanvas` there if possible.
- On pan or zoom, update only what changed, and use rAF to render at most once per frame with the latest view state.
- For hover tooltips, use a spatial index (grid or quadtree) instead of looping over all points on every `pointermove`.
- Keep transfers cheap: typed arrays and transferables.

## 450: What is your checklist for keeping a page responsive?

- Keep tasks short: aim for under 50 ms and yield in long work.
- Respond to input first: do the visual update, yield, then do the rest.
- Move heavy computation to Web Workers.
- Do visual updates in `requestAnimationFrame` and batch DOM reads before writes.
- Use the compositor: animate `transform` and `opacity`, use passive listeners, prefer CSS for scroll effects.
- Render less: virtualization, `content-visibility`, smaller DOM.
- Load less JavaScript up front and hydrate lazily.
- Control third-party scripts.
- Never trust timers for accuracy; use timestamps.
- Clean up timers, listeners and observers.
- Measure in the field with INP and LoAF, and in the lab with the Performance panel on throttled CPUs.
