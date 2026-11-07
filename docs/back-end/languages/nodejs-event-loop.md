# Node.js Event Loop Interview Questions and Answers

_Last updated: October 28, 2026_

450 interview questions with answers about the Node.js event loop, split into three levels: 150 easy, 150 moderate and 150 advanced.

This file is about the event loop in Node.js (libuv, its phases, `process.nextTick`, `setImmediate`, the thread pool and so on), not the browser event loop. The answers are based on the current Node.js LTS lines (24 and 26). Where behavior changed between versions (for example in Node 11 and Node 20), the version is mentioned. Unless a question says otherwise, code examples are CommonJS scripts run with `node file.js`, because ES modules change the order of some callbacks (this is covered in its own question).

## Table of Contents

- [Easy Questions (1-150)](#easy-questions-1-150)
- [Moderate Questions (151-300)](#moderate-questions-151-300)
- [Advanced Questions (301-450)](#advanced-questions-301-450)

### Easy Questions (1-150)

- [1: What is the event loop in Node.js?](#1-what-is-the-event-loop-in-nodejs)
- [2: Why does Node.js need an event loop?](#2-why-does-nodejs-need-an-event-loop)
- [3: Is Node.js single-threaded?](#3-is-nodejs-single-threaded)
- [4: What is libuv?](#4-what-is-libuv)
- [5: What does non-blocking I/O mean?](#5-what-does-non-blocking-io-mean)
- [6: What is the difference between blocking and non-blocking code?](#6-what-is-the-difference-between-blocking-and-non-blocking-code)
- [7: What is the call stack?](#7-what-is-the-call-stack)
- [8: What is a callback?](#8-what-is-a-callback)
- [9: What happens when you call an async function like fs.readFile?](#9-what-happens-when-you-call-an-async-function-like-fsreadfile)
- [10: What are the phases of the Node.js event loop?](#10-what-are-the-phases-of-the-nodejs-event-loop)
- [11: What happens in the timers phase?](#11-what-happens-in-the-timers-phase)
- [12: What happens in the pending callbacks phase?](#12-what-happens-in-the-pending-callbacks-phase)
- [13: What are the idle and prepare phases?](#13-what-are-the-idle-and-prepare-phases)
- [14: What happens in the poll phase?](#14-what-happens-in-the-poll-phase)
- [15: What happens in the check phase?](#15-what-happens-in-the-check-phase)
- [16: What happens in the close callbacks phase?](#16-what-happens-in-the-close-callbacks-phase)
- [17: What is one iteration of the event loop called?](#17-what-is-one-iteration-of-the-event-loop-called)
- [18: When does the event loop start?](#18-when-does-the-event-loop-start)
- [19: When does a Node.js process exit?](#19-when-does-a-nodejs-process-exit)
- [20: What is setTimeout in Node.js?](#20-what-is-settimeout-in-nodejs)
- [21: What does setTimeout return in Node.js?](#21-what-does-settimeout-return-in-nodejs)
- [22: What is setInterval?](#22-what-is-setinterval)
- [23: How do you cancel a timer?](#23-how-do-you-cancel-a-timer)
- [24: What is setImmediate?](#24-what-is-setimmediate)
- [25: How do you cancel setImmediate?](#25-how-do-you-cancel-setimmediate)
- [26: What is process.nextTick?](#26-what-is-processnexttick)
- [27: What is a microtask?](#27-what-is-a-microtask)
- [28: What is the microtask queue?](#28-what-is-the-microtask-queue)
- [29: What is queueMicrotask?](#29-what-is-queuemicrotask)
- [30: What are macrotasks in Node.js?](#30-what-are-macrotasks-in-nodejs)
- [31: What is the difference between process.nextTick and setImmediate?](#31-what-is-the-difference-between-processnexttick-and-setimmediate)
- [32: Why are the names nextTick and setImmediate confusing?](#32-why-are-the-names-nexttick-and-setimmediate-confusing)
- [33: What is the difference between setTimeout(fn, 0) and setImmediate(fn)?](#33-what-is-the-difference-between-settimeoutfn-0-and-setimmediatefn)
- [34: Does setTimeout(fn, 0) really run after 0 ms?](#34-does-settimeoutfn-0-really-run-after-0-ms)
- [35: Is the setTimeout delay guaranteed?](#35-is-the-settimeout-delay-guaranteed)
- [36: What is the minimum delay for setTimeout in Node.js?](#36-what-is-the-minimum-delay-for-settimeout-in-nodejs)
- [37: Where do promise callbacks run?](#37-where-do-promise-callbacks-run)
- [38: Which runs first, process.nextTick or a resolved promise's then?](#38-which-runs-first-processnexttick-or-a-resolved-promises-then)
- [39: What is the output order of sync code, a timer, a promise and nextTick?](#39-what-is-the-output-order-of-sync-code-a-timer-a-promise-and-nexttick)
- [40: What does async/await do with the event loop?](#40-what-does-asyncawait-do-with-the-event-loop)
- [41: What happens after await?](#41-what-happens-after-await)
- [42: Does async code run in parallel in Node.js?](#42-does-async-code-run-in-parallel-in-nodejs)
- [43: What is the difference between concurrency and parallelism in Node.js?](#43-what-is-the-difference-between-concurrency-and-parallelism-in-nodejs)
- [44: What is the thread pool in Node.js?](#44-what-is-the-thread-pool-in-nodejs)
- [45: What is the default thread pool size?](#45-what-is-the-default-thread-pool-size)
- [46: Which operations use the thread pool?](#46-which-operations-use-the-thread-pool)
- [47: Which operations do not use the thread pool?](#47-which-operations-do-not-use-the-thread-pool)
- [48: How does Node handle network I/O without threads?](#48-how-does-node-handle-network-io-without-threads)
- [49: What are epoll, kqueue and IOCP?](#49-what-are-epoll-kqueue-and-iocp)
- [50: What does "blocking the event loop" mean?](#50-what-does-blocking-the-event-loop-mean)
- [51: What are some examples of code that blocks the event loop?](#51-what-are-some-examples-of-code-that-blocks-the-event-loop)
- [52: Why are sync fs methods like readFileSync dangerous in a server?](#52-why-are-sync-fs-methods-like-readfilesync-dangerous-in-a-server)
- [53: When is it fine to use sync methods?](#53-when-is-it-fine-to-use-sync-methods)
- [54: What is a CPU-bound task?](#54-what-is-a-cpu-bound-task)
- [55: What is an I/O-bound task?](#55-what-is-an-io-bound-task)
- [56: Why is Node.js good at I/O-bound work?](#56-why-is-nodejs-good-at-io-bound-work)
- [57: Why is Node.js not great at CPU-heavy work by default?](#57-why-is-nodejs-not-great-at-cpu-heavy-work-by-default)
- [58: What is the callback queue?](#58-what-is-the-callback-queue)
- [59: Is there one queue or many queues in the Node.js event loop?](#59-is-there-one-queue-or-many-queues-in-the-nodejs-event-loop)
- [60: What is an EventEmitter?](#60-what-is-an-eventemitter)
- [61: Are EventEmitter listeners called synchronously or asynchronously?](#61-are-eventemitter-listeners-called-synchronously-or-asynchronously)
- [62: How is the Node.js event loop different from the browser event loop?](#62-how-is-the-nodejs-event-loop-different-from-the-browser-event-loop)
- [63: Does Node.js have requestAnimationFrame?](#63-does-nodejs-have-requestanimationframe)
- [64: What is the role of V8 compared to libuv?](#64-what-is-the-role-of-v8-compared-to-libuv)
- [65: Who runs JavaScript, V8 or libuv?](#65-who-runs-javascript-v8-or-libuv)
- [66: What is the timers/promises module?](#66-what-is-the-timerspromises-module)
- [67: How do you wait for some time with promises in Node.js?](#67-how-do-you-wait-for-some-time-with-promises-in-nodejs)
- [68: What is the node:timers module?](#68-what-is-the-nodetimers-module)
- [69: Can you pass arguments to a setTimeout callback?](#69-can-you-pass-arguments-to-a-settimeout-callback)
- [70: What is this inside a setTimeout callback in Node.js?](#70-what-is-this-inside-a-settimeout-callback-in-nodejs)
- [71: What does unref() do on a timer?](#71-what-does-unref-do-on-a-timer)
- [72: What does ref() do on a timer?](#72-what-does-ref-do-on-a-timer)
- [73: What does hasRef() return?](#73-what-does-hasref-return)
- [74: What is timeout.refresh()?](#74-what-is-timeoutrefresh)
- [75: What happens if you pass a delay larger than 2147483647?](#75-what-happens-if-you-pass-a-delay-larger-than-2147483647)
- [76: What happens if you pass a negative delay or NaN to setTimeout?](#76-what-happens-if-you-pass-a-negative-delay-or-nan-to-settimeout)
- [77: What is the order of setTimeout(fn, 0) and setImmediate(fn) in the main script?](#77-what-is-the-order-of-settimeoutfn-0-and-setimmediatefn-in-the-main-script)
- [78: What is the order of setTimeout(fn, 0) and setImmediate(fn) inside an I/O callback?](#78-what-is-the-order-of-settimeoutfn-0-and-setimmediatefn-inside-an-io-callback)
- [79: What does "tick" mean in process.nextTick?](#79-what-does-tick-mean-in-processnexttick)
- [80: Can you pass arguments to process.nextTick?](#80-can-you-pass-arguments-to-processnexttick)
- [81: What is event loop starvation?](#81-what-is-event-loop-starvation)
- [82: Can process.nextTick starve the event loop?](#82-can-processnexttick-starve-the-event-loop)
- [83: Can setImmediate starve the event loop?](#83-can-setimmediate-starve-the-event-loop)
- [84: What is the event loop doing when nothing is happening?](#84-what-is-the-event-loop-doing-when-nothing-is-happening)
- [85: How does the loop decide how long to wait in the poll phase?](#85-how-does-the-loop-decide-how-long-to-wait-in-the-poll-phase)
- [86: Why might a timer fire late?](#86-why-might-a-timer-fire-late)
- [87: What happens if a timer callback throws an error?](#87-what-happens-if-a-timer-callback-throws-an-error)
- [88: Why can't you catch async errors with a try/catch around the call?](#88-why-cant-you-catch-async-errors-with-a-trycatch-around-the-call)
- [89: What does Node do with an unhandled promise rejection?](#89-what-does-node-do-with-an-unhandled-promise-rejection)
- [90: What is the uncaughtException event?](#90-what-is-the-uncaughtexception-event)
- [91: What is the beforeExit event?](#91-what-is-the-beforeexit-event)
- [92: What is the exit event?](#92-what-is-the-exit-event)
- [93: Can you run async code in the exit event?](#93-can-you-run-async-code-in-the-exit-event)
- [94: What does process.exit() do to pending callbacks?](#94-what-does-processexit-do-to-pending-callbacks)
- [95: What keeps a Node.js process alive?](#95-what-keeps-a-nodejs-process-alive)
- [96: Does a pending promise keep the process alive?](#96-does-a-pending-promise-keep-the-process-alive)
- [97: What is a handle in libuv?](#97-what-is-a-handle-in-libuv)
- [98: What is a request in libuv?](#98-what-is-a-request-in-libuv)
- [99: What is the main thread in Node.js?](#99-what-is-the-main-thread-in-nodejs)
- [100: What happens when you run node app.js?](#100-what-happens-when-you-run-node-appjs)
- [101: When does the main script run compared to the event loop?](#101-when-does-the-main-script-run-compared-to-the-event-loop)
- [102: How does fs.promises relate to the event loop?](#102-how-does-fspromises-relate-to-the-event-loop)
- [103: What is the difference between fs.readFile and fs.readFileSync for the event loop?](#103-what-is-the-difference-between-fsreadfile-and-fsreadfilesync-for-the-event-loop)
- [104: What is the difference between callback-based and promise-based APIs?](#104-what-is-the-difference-between-callback-based-and-promise-based-apis)
- [105: What is callback hell and does it affect the event loop?](#105-what-is-callback-hell-and-does-it-affect-the-event-loop)
- [106: What is util.promisify?](#106-what-is-utilpromisify)
- [107: How does an HTTP server use the event loop?](#107-how-does-an-http-server-use-the-event-loop)
- [108: Why can one Node process handle many connections?](#108-why-can-one-node-process-handle-many-connections)
- [109: What happens if one request handler runs a slow loop?](#109-what-happens-if-one-request-handler-runs-a-slow-loop)
- [110: What are worker threads?](#110-what-are-worker-threads)
- [111: What is the cluster module?](#111-what-is-the-cluster-module)
- [112: What is the difference between worker threads and the libuv thread pool?](#112-what-is-the-difference-between-worker-threads-and-the-libuv-thread-pool)
- [113: What is the difference between worker threads and child processes?](#113-what-is-the-difference-between-worker-threads-and-child-processes)
- [114: Does each worker thread have its own event loop?](#114-does-each-worker-thread-have-its-own-event-loop)
- [115: What is event loop delay?](#115-what-is-event-loop-delay)
- [116: How can you quickly check if the event loop is blocked?](#116-how-can-you-quickly-check-if-the-event-loop-is-blocked)
- [117: What is perf_hooks?](#117-what-is-perf_hooks)
- [118: Does Promise.all run tasks in parallel?](#118-does-promiseall-run-tasks-in-parallel)
- [119: Is Promise.resolve().then() synchronous?](#119-is-promiseresolvethen-synchronous)
- [120: What is the general order of sync code, nextTick, promises, timers and setImmediate?](#120-what-is-the-general-order-of-sync-code-nexttick-promises-timers-and-setimmediate)
- [121: Do timers with the same delay run in the order they were created?](#121-do-timers-with-the-same-delay-run-in-the-order-they-were-created)
- [122: What happens with two timers that have different delays?](#122-what-happens-with-two-timers-that-have-different-delays)
- [123: What is setInterval drift?](#123-what-is-setinterval-drift)
- [124: How do you repeat a task without runs overlapping?](#124-how-do-you-repeat-a-task-without-runs-overlapping)
- [125: What happens if a setInterval callback takes longer than the interval?](#125-what-happens-if-a-setinterval-callback-takes-longer-than-the-interval)
- [126: How do you stop an interval from inside its callback?](#126-how-do-you-stop-an-interval-from-inside-its-callback)
- [127: How do you cancel a promise-based timer?](#127-how-do-you-cancel-a-promise-based-timer)
- [128: What is AbortSignal.timeout()?](#128-what-is-abortsignaltimeout)
- [129: Does console.log block the event loop?](#129-does-consolelog-block-the-event-loop)
- [130: Is JSON.parse blocking?](#130-is-jsonparse-blocking)
- [131: Can regular expressions block the event loop?](#131-can-regular-expressions-block-the-event-loop)
- [132: Is crypto.createHash blocking?](#132-is-cryptocreatehash-blocking)
- [133: Is crypto.pbkdf2 blocking?](#133-is-cryptopbkdf2-blocking)
- [134: Is require() blocking?](#134-is-require-blocking)
- [135: Is import() blocking?](#135-is-import-blocking)
- [136: What is top-level await and how does it relate to the event loop?](#136-what-is-top-level-await-and-how-does-it-relate-to-the-event-loop)
- [137: How are streams related to the event loop?](#137-how-are-streams-related-to-the-event-loop)
- [138: When does the data event of a readable stream fire?](#138-when-does-the-data-event-of-a-readable-stream-fire)
- [139: What is backpressure?](#139-what-is-backpressure)
- [140: What does "run to completion" mean?](#140-what-does-run-to-completion-mean)
- [141: Can one callback be interrupted by another callback?](#141-can-one-callback-be-interrupted-by-another-callback)
- [142: Do you need locks in Node.js?](#142-do-you-need-locks-in-nodejs)
- [143: What is a race condition in async Node.js code?](#143-what-is-a-race-condition-in-async-nodejs-code)
- [144: What is event-driven architecture in Node.js?](#144-what-is-event-driven-architecture-in-nodejs)
- [145: What is the reactor pattern?](#145-what-is-the-reactor-pattern)
- [146: What is the difference between the event loop and EventEmitter?](#146-what-is-the-difference-between-the-event-loop-and-eventemitter)
- [147: Is the event loop part of the JavaScript language?](#147-is-the-event-loop-part-of-the-javascript-language)
- [148: How do you check which libuv and V8 versions your Node uses?](#148-how-do-you-check-which-libuv-and-v8-versions-your-node-uses)
- [149: Does using async functions make code faster?](#149-does-using-async-functions-make-code-faster)
- [150: What are common misconceptions about the Node.js event loop?](#150-what-are-common-misconceptions-about-the-nodejs-event-loop)

### Moderate Questions (151-300)

- [151: Can you walk through one full iteration of the event loop?](#151-can-you-walk-through-one-full-iteration-of-the-event-loop)
- [152: How exactly does Node process the nextTick and microtask queues?](#152-how-exactly-does-node-process-the-nexttick-and-microtask-queues)
- [153: What changed in Node 11 regarding timers and microtasks?](#153-what-changed-in-node-11-regarding-timers-and-microtasks)
- [154: What changed in libuv 1.45 (Node 20) regarding timers?](#154-what-changed-in-libuv-145-node-20-regarding-timers)
- [155: What is the output order of timers, immediates, promises and nextTick inside an I/O callback?](#155-what-is-the-output-order-of-timers-immediates-promises-and-nexttick-inside-an-io-callback)
- [156: What is the output when process.nextTick is called inside a promise callback?](#156-what-is-the-output-when-processnexttick-is-called-inside-a-promise-callback)
- [157: What is the output when promises and nested nextTick calls are queued from a nextTick callback?](#157-what-is-the-output-when-promises-and-nested-nexttick-calls-are-queued-from-a-nexttick-callback)
- [158: What is the output order of an async function with await, nextTick and a promise?](#158-what-is-the-output-order-of-an-async-function-with-await-nexttick-and-a-promise)
- [159: What is the output when setTimeout and setImmediate are scheduled inside a timer callback?](#159-what-is-the-output-when-settimeout-and-setimmediate-are-scheduled-inside-a-timer-callback)
- [160: What is the output when setTimeout and setImmediate are scheduled inside a setImmediate callback?](#160-what-is-the-output-when-settimeout-and-setimmediate-are-scheduled-inside-a-setimmediate-callback)
- [161: What is the output when two timers are due and the first one queues nextTick and a promise?](#161-what-is-the-output-when-two-timers-are-due-and-the-first-one-queues-nexttick-and-a-promise)
- [162: What is the output when setImmediate is called inside another setImmediate callback?](#162-what-is-the-output-when-setimmediate-is-called-inside-another-setimmediate-callback)
- [163: Why does nextTick run before promises in CommonJS but not in ES modules?](#163-why-does-nexttick-run-before-promises-in-commonjs-but-not-in-es-modules)
- [164: How many microtask ticks does await take?](#164-how-many-microtask-ticks-does-await-take)
- [165: Does return await change timing compared to return?](#165-does-return-await-change-timing-compared-to-return)
- [166: When should you use process.nextTick?](#166-when-should-you-use-processnexttick)
- [167: When should you use queueMicrotask instead of process.nextTick?](#167-when-should-you-use-queuemicrotask-instead-of-processnexttick)
- [168: When should you use setImmediate?](#168-when-should-you-use-setimmediate)
- [169: How do you make an API always async?](#169-how-do-you-make-an-api-always-async)
- [170: Why do some constructors emit events with process.nextTick?](#170-why-do-some-constructors-emit-events-with-processnexttick)
- [171: Why is the listening event safe to attach after calling server.listen()?](#171-why-is-the-listening-event-safe-to-attach-after-calling-serverlisten)
- [172: How do you split a long CPU task into chunks?](#172-how-do-you-split-a-long-cpu-task-into-chunks)
- [173: Why use setImmediate instead of process.nextTick for chunking work?](#173-why-use-setimmediate-instead-of-processnexttick-for-chunking-work)
- [174: How do you move CPU work to a worker thread?](#174-how-do-you-move-cpu-work-to-a-worker-thread)
- [175: How do you pass data between the main thread and a worker?](#175-how-do-you-pass-data-between-the-main-thread-and-a-worker)
- [176: What does it cost to send data to a worker?](#176-what-does-it-cost-to-send-data-to-a-worker)
- [177: What is a worker pool and why use one?](#177-what-is-a-worker-pool-and-why-use-one)
- [178: How do you change UV_THREADPOOL_SIZE?](#178-how-do-you-change-uv_threadpool_size)
- [179: When should you increase the thread pool size?](#179-when-should-you-increase-the-thread-pool-size)
- [180: What happens when all thread pool threads are busy?](#180-what-happens-when-all-thread-pool-threads-are-busy)
- [181: Why can slow crypto calls slow down file operations?](#181-why-can-slow-crypto-calls-slow-down-file-operations)
- [182: What is the difference between dns.lookup and dns.resolve in terms of the event loop?](#182-what-is-the-difference-between-dnslookup-and-dnsresolve-in-terms-of-the-event-loop)
- [183: How does fs.promises use the thread pool?](#183-how-does-fspromises-use-the-thread-pool)
- [184: Why don't many parallel file reads get faster after a point?](#184-why-dont-many-parallel-file-reads-get-faster-after-a-point)
- [185: How do you limit concurrency of async operations?](#185-how-do-you-limit-concurrency-of-async-operations)
- [186: What is monitorEventLoopDelay?](#186-what-is-monitoreventloopdelay)
- [187: What is event loop utilization (ELU)?](#187-what-is-event-loop-utilization-elu)
- [188: How do you measure event loop utilization of a worker thread?](#188-how-do-you-measure-event-loop-utilization-of-a-worker-thread)
- [189: What does the --trace-sync-io flag do?](#189-what-does-the---trace-sync-io-flag-do)
- [190: How do you find what is blocking the event loop?](#190-how-do-you-find-what-is-blocking-the-event-loop)
- [191: How do you use --cpu-prof?](#191-how-do-you-use---cpu-prof)
- [192: What is process.getActiveResourcesInfo()?](#192-what-is-processgetactiveresourcesinfo)
- [193: Why does a Node.js process not exit, and how do you debug it?](#193-why-does-a-nodejs-process-not-exit-and-how-do-you-debug-it)
- [194: Why do tests hang after finishing, and how do you fix it?](#194-why-do-tests-hang-after-finishing-and-how-do-you-fix-it)
- [195: How do unref'd timers help with background tasks?](#195-how-do-unrefd-timers-help-with-background-tasks)
- [196: How do you add a timeout to a promise?](#196-how-do-you-add-a-timeout-to-a-promise)
- [197: How does setTimeout from timers/promises support cancellation?](#197-how-does-settimeout-from-timerspromises-support-cancellation)
- [198: How does setInterval from timers/promises work?](#198-how-does-setinterval-from-timerspromises-work)
- [199: What are scheduler.wait() and scheduler.yield()?](#199-what-are-schedulerwait-and-scheduleryield)
- [200: How do you avoid leaking timers?](#200-how-do-you-avoid-leaking-timers)
- [201: Can you use the using keyword with timers?](#201-can-you-use-the-using-keyword-with-timers)
- [202: How are Node.js timers different from browser timers?](#202-how-are-nodejs-timers-different-from-browser-timers)
- [203: Does Node.js clamp nested timers to 4 ms like browsers?](#203-does-nodejs-clamp-nested-timers-to-4-ms-like-browsers)
- [204: Can an endless promise chain starve the event loop?](#204-can-an-endless-promise-chain-starve-the-event-loop)
- [205: Why doesn't await Promise.resolve() let I/O run?](#205-why-doesnt-await-promiseresolve-let-io-run)
- [206: How does the drain event relate to the event loop?](#206-how-does-the-drain-event-relate-to-the-event-loop)
- [207: How do streams help avoid blocking with large files?](#207-how-do-streams-help-avoid-blocking-with-large-files)
- [208: How does stream.pipeline help?](#208-how-does-streampipeline-help)
- [209: Why is reading a 1 GB file with readFile a problem?](#209-why-is-reading-a-1-gb-file-with-readfile-a-problem)
- [210: How do you handle large JSON without blocking the loop?](#210-how-do-you-handle-large-json-without-blocking-the-loop)
- [211: What is ReDoS and how does it relate to the event loop?](#211-what-is-redos-and-how-does-it-relate-to-the-event-loop)
- [212: How do you protect against ReDoS?](#212-how-do-you-protect-against-redos)
- [213: Why can sorting a big array be a problem in a request handler?](#213-why-can-sorting-a-big-array-be-a-problem-in-a-request-handler)
- [214: How do error handling styles differ between callbacks and promises?](#214-how-do-error-handling-styles-differ-between-callbacks-and-promises)
- [215: How do you use the unhandledRejection event?](#215-how-do-you-use-the-unhandledrejection-event)
- [216: What does the --unhandled-rejections flag do?](#216-what-does-the---unhandled-rejections-flag-do)
- [217: What is the uncaughtExceptionMonitor event?](#217-what-is-the-uncaughtexceptionmonitor-event)
- [218: Why should a process exit after an uncaught exception?](#218-why-should-a-process-exit-after-an-uncaught-exception)
- [219: How do you implement graceful shutdown?](#219-how-do-you-implement-graceful-shutdown)
- [220: What do server.close(), closeIdleConnections() and closeAllConnections() do?](#220-what-do-serverclose-closeidleconnections-and-closeallconnections-do)
- [221: How are signals like SIGTERM delivered to your code?](#221-how-are-signals-like-sigterm-delivered-to-your-code)
- [222: How do you make EventEmitter listeners run asynchronously?](#222-how-do-you-make-eventemitter-listeners-run-asynchronously)
- [223: How do events.once and events.on work with the event loop?](#223-how-do-eventsonce-and-eventson-work-with-the-event-loop)
- [224: What is captureRejections in EventEmitter?](#224-what-is-capturerejections-in-eventemitter)
- [225: How does AbortController work with async APIs in Node?](#225-how-does-abortcontroller-work-with-async-apis-in-node)
- [226: What is AsyncLocalStorage?](#226-what-is-asynclocalstorage)
- [227: How does AsyncLocalStorage keep its value across await and callbacks?](#227-how-does-asynclocalstorage-keep-its-value-across-await-and-callbacks)
- [228: What are async_hooks and why are they discouraged?](#228-what-are-async_hooks-and-why-are-they-discouraged)
- [229: What are executionAsyncId and triggerAsyncId?](#229-what-are-executionasyncid-and-triggerasyncid)
- [230: What is AsyncResource used for?](#230-what-is-asyncresource-used-for)
- [231: How do async stack traces work in Node.js?](#231-how-do-async-stack-traces-work-in-nodejs)
- [232: Why are stack traces from callbacks often short?](#232-why-are-stack-traces-from-callbacks-often-short)
- [233: How does the cluster module distribute connections?](#233-how-does-the-cluster-module-distribute-connections)
- [234: When should you use cluster and when worker threads?](#234-when-should-you-use-cluster-and-when-worker-threads)
- [235: How do you share memory between worker threads?](#235-how-do-you-share-memory-between-worker-threads)
- [236: Can you use Atomics.wait on the main thread in Node.js?](#236-can-you-use-atomicswait-on-the-main-thread-in-nodejs)
- [237: How are worker thread messages delivered?](#237-how-are-worker-thread-messages-delivered)
- [238: What does worker.unref() do?](#238-what-does-workerunref-do)
- [239: What is the difference between exec and execSync for the event loop?](#239-what-is-the-difference-between-exec-and-execsync-for-the-event-loop)
- [240: How does spawn stream its output through the event loop?](#240-how-does-spawn-stream-its-output-through-the-event-loop)
- [241: What is the difference between the exit and close events of a child process?](#241-what-is-the-difference-between-the-exit-and-close-events-of-a-child-process)
- [242: How does an HTTP request flow through the event loop phases?](#242-how-does-an-http-request-flow-through-the-event-loop-phases)
- [243: How does HTTP keep-alive affect the event loop?](#243-how-does-http-keep-alive-affect-the-event-loop)
- [244: Can fetch keep a Node.js process alive?](#244-can-fetch-keep-a-nodejs-process-alive)
- [245: How does socket.setTimeout work?](#245-how-does-socketsettimeout-work)
- [246: What are the main HTTP server timeouts?](#246-what-are-the-main-http-server-timeouts)
- [247: How does fs.watch work with the event loop?](#247-how-does-fswatch-work-with-the-event-loop)
- [248: How does garbage collection affect the event loop?](#248-how-does-garbage-collection-affect-the-event-loop)
- [249: What V8 flags can help with GC-related latency?](#249-what-v8-flags-can-help-with-gc-related-latency)
- [250: How do you detect long GC pauses?](#250-how-do-you-detect-long-gc-pauses)
- [251: How do you test timer-based code with node:test?](#251-how-do-you-test-timer-based-code-with-nodetest)
- [252: What should you know about fake timers in Jest and Vitest?](#252-what-should-you-know-about-fake-timers-in-jest-and-vitest)
- [253: What is a flushPromises helper and when do you need it?](#253-what-is-a-flushpromises-helper-and-when-do-you-need-it)
- [254: How does util.promisify(setTimeout) work?](#254-how-does-utilpromisifysettimeout-work)
- [255: How do you read a file line by line without blocking?](#255-how-do-you-read-a-file-line-by-line-without-blocking)
- [256: What is the difference between sequential and parallel await?](#256-what-is-the-difference-between-sequential-and-parallel-await)
- [257: Why doesn't forEach wait for async callbacks?](#257-why-doesnt-foreach-wait-for-async-callbacks)
- [258: What is the difference between Promise.all, allSettled, race and any?](#258-what-is-the-difference-between-promiseall-allsettled-race-and-any)
- [259: What happens to I/O events that arrive while a callback is running?](#259-what-happens-to-io-events-that-arrive-while-a-callback-is-running)
- [260: How do you debounce or throttle work on the server?](#260-how-do-you-debounce-or-throttle-work-on-the-server)
- [261: How do you implement retry with backoff?](#261-how-do-you-implement-retry-with-backoff)
- [262: Are many timers expensive in Node.js?](#262-are-many-timers-expensive-in-nodejs)
- [263: How do you deal with a third-party library that blocks the event loop?](#263-how-do-you-deal-with-a-third-party-library-that-blocks-the-event-loop)
- [264: How does a blocked event loop affect Kubernetes health checks?](#264-how-does-a-blocked-event-loop-affect-kubernetes-health-checks)
- [265: How can a readiness check reflect event loop health?](#265-how-can-a-readiness-check-reflect-event-loop-health)
- [266: What is load shedding based on the event loop?](#266-what-is-load-shedding-based-on-the-event-loop)
- [267: What event loop metrics should you monitor in production?](#267-what-event-loop-metrics-should-you-monitor-in-production)
- [268: How does loading code with require affect startup and the event loop?](#268-how-does-loading-code-with-require-affect-startup-and-the-event-loop)
- [269: How does top-level await affect module loading?](#269-how-does-top-level-await-affect-module-loading)
- [270: How do you keep a Node.js process alive on purpose?](#270-how-do-you-keep-a-nodejs-process-alive-on-purpose)
- [271: How can beforeExit be used for final async work?](#271-how-can-beforeexit-be-used-for-final-async-work)
- [272: What is the difference between process.exit() and process.exitCode?](#272-what-is-the-difference-between-processexit-and-processexitcode)
- [273: Why can output get lost when calling process.exit()?](#273-why-can-output-get-lost-when-calling-processexit)
- [274: How should you handle the error event on EventEmitters?](#274-how-should-you-handle-the-error-event-on-eventemitters)
- [275: Do timers depend on the system clock?](#275-do-timers-depend-on-the-system-clock)
- [276: What is the cached loop time in libuv?](#276-what-is-the-cached-loop-time-in-libuv)
- [277: How do you measure durations accurately in Node.js?](#277-how-do-you-measure-durations-accurately-in-nodejs)
- [278: How is reading from a socket different from reading a file?](#278-how-is-reading-from-a-socket-different-from-reading-a-file)
- [279: What is the difference between zlib sync and async functions?](#279-what-is-the-difference-between-zlib-sync-and-async-functions)
- [280: When is crypto.randomBytes sync fine and when is it not?](#280-when-is-cryptorandombytes-sync-fine-and-when-is-it-not)
- [281: Why should you use async bcrypt functions in a server?](#281-why-should-you-use-async-bcrypt-functions-in-a-server)
- [282: Can adding await everywhere slow your code down?](#282-can-adding-await-everywhere-slow-your-code-down)
- [283: Is the event loop the same on Windows and Linux?](#283-is-the-event-loop-the-same-on-windows-and-linux)
- [284: How is Node's event loop different from Deno's and Bun's?](#284-how-is-nodes-event-loop-different-from-denos-and-buns)
- [285: How do you schedule something to run at a specific time?](#285-how-do-you-schedule-something-to-run-at-a-specific-time)
- [286: How do you handle delays longer than 24.8 days?](#286-how-do-you-handle-delays-longer-than-248-days)
- [287: What are common event loop mistakes in Express apps?](#287-what-are-common-event-loop-mistakes-in-express-apps)
- [288: How does a database connection pool work with the event loop?](#288-how-does-a-database-connection-pool-work-with-the-event-loop)
- [289: How do you process background jobs without hurting request latency?](#289-how-do-you-process-background-jobs-without-hurting-request-latency)
- [290: How does the event loop affect WebSocket servers?](#290-how-does-the-event-loop-affect-websocket-servers)
- [291: How do you time an async operation correctly?](#291-how-do-you-time-an-async-operation-correctly)
- [292: What happens if a queueMicrotask callback throws?](#292-what-happens-if-a-queuemicrotask-callback-throws)
- [293: How do you read a stream with for await?](#293-how-do-you-read-a-stream-with-for-await)
- [294: How can you check in a test that code doesn't block the event loop for too long?](#294-how-can-you-check-in-a-test-that-code-doesnt-block-the-event-loop-for-too-long)
- [295: What is the difference between setTimeout and setImmediate when deferring work in a handler?](#295-what-is-the-difference-between-settimeout-and-setimmediate-when-deferring-work-in-a-handler)
- [296: Why might Promise.all over 100,000 items cause trouble?](#296-why-might-promiseall-over-100000-items-cause-trouble)
- [297: What does process.memoryUsage() tell you and how does it relate to the event loop?](#297-what-does-processmemoryusage-tell-you-and-how-does-it-relate-to-the-event-loop)
- [298: What is the role of the poll phase timeout when there are no timers?](#298-what-is-the-role-of-the-poll-phase-timeout-when-there-are-no-timers)
- [299: How do callbacks from native addons and database drivers run?](#299-how-do-callbacks-from-native-addons-and-database-drivers-run)
- [300: How would you explain the Node.js event loop in two minutes in an interview?](#300-how-would-you-explain-the-nodejs-event-loop-in-two-minutes-in-an-interview)

### Advanced Questions (301-450)

- [301: What does libuv's uv_run loop look like in recent versions?](#301-what-does-libuvs-uv_run-loop-look-like-in-recent-versions)
- [302: How does libuv decide the poll timeout?](#302-how-does-libuv-decide-the-poll-timeout)
- [303: When is the libuv loop considered alive?](#303-when-is-the-libuv-loop-considered-alive)
- [304: How are JavaScript timers implemented on top of libuv?](#304-how-are-javascript-timers-implemented-on-top-of-libuv)
- [305: Why does Node group timers by duration?](#305-why-does-node-group-timers-by-duration)
- [306: What does it cost to create and clear timers at high volume?](#306-what-does-it-cost-to-create-and-clear-timers-at-high-volume)
- [307: How is setImmediate implemented?](#307-how-is-setimmediate-implemented)
- [308: How does Node run nextTick and microtasks after a native callback?](#308-how-does-node-run-nexttick-and-microtasks-after-a-native-callback)
- [309: What does processTicksAndRejections do?](#309-what-does-processticksandrejections-do)
- [310: How does Node control when V8 runs microtasks?](#310-how-does-node-control-when-v8-runs-microtasks)
- [311: Why exactly do promise callbacks run before nextTick in an ES module?](#311-why-exactly-do-promise-callbacks-run-before-nexttick-in-an-es-module)
- [312: How does the ES module loader use the event loop?](#312-how-does-the-es-module-loader-use-the-event-loop)
- [313: How is the libuv thread pool implemented?](#313-how-is-the-libuv-thread-pool-implemented)
- [314: Does the thread pool treat DNS lookups differently from file operations?](#314-does-the-thread-pool-treat-dns-lookups-differently-from-file-operations)
- [315: How does libuv perform file I/O under the hood?](#315-how-does-libuv-perform-file-io-under-the-hood)
- [316: Why does libuv use a thread pool for files instead of epoll?](#316-why-does-libuv-use-a-thread-pool-for-files-instead-of-epoll)
- [317: What is io_uring and what is its status in libuv and Node?](#317-what-is-io_uring-and-what-is-its-status-in-libuv-and-node)
- [318: How do you diagnose thread pool saturation?](#318-how-do-you-diagnose-thread-pool-saturation)
- [319: Is the thread pool shared between worker threads?](#319-is-the-thread-pool-shared-between-worker-threads)
- [320: What happens if you set UV_THREADPOOL_SIZE after the pool is used?](#320-what-happens-if-you-set-uv_threadpool_size-after-the-pool-is-used)
- [321: How do native addons use the event loop?](#321-how-do-native-addons-use-the-event-loop)
- [322: What is uv_async_send?](#322-what-is-uv_async_send)
- [323: How does libuv deliver signals to the event loop?](#323-how-does-libuv-deliver-signals-to-the-event-loop)
- [324: How are child process exits detected?](#324-how-are-child-process-exits-detected)
- [325: How does dns.resolve integrate with the event loop?](#325-how-does-dnsresolve-integrate-with-the-event-loop)
- [326: Can a busy poll phase delay timers?](#326-can-a-busy-poll-phase-delay-timers)
- [327: Is there a limit on how many callbacks run in one phase?](#327-is-there-a-limit-on-how-many-callbacks-run-in-one-phase)
- [328: What kinds of callbacks end up in the pending callbacks phase?](#328-what-kinds-of-callbacks-end-up-in-the-pending-callbacks-phase)
- [329: How does closing a handle work?](#329-how-does-closing-a-handle-work)
- [330: Where does HTTP parsing happen?](#330-where-does-http-parsing-happen)
- [331: How does TLS affect the event loop?](#331-how-does-tls-affect-the-event-loop)
- [332: How does a worker thread start and what does it cost?](#332-how-does-a-worker-thread-start-and-what-does-it-cost)
- [333: What are resourceLimits for workers?](#333-what-are-resourcelimits-for-workers)
- [334: How does worker.terminate() work?](#334-how-does-workerterminate-work)
- [335: How do you enforce a timeout on CPU-heavy work?](#335-how-do-you-enforce-a-timeout-on-cpu-heavy-work)
- [336: How is event loop utilization calculated?](#336-how-is-event-loop-utilization-calculated)
- [337: Why is ELU often a better signal than CPU usage?](#337-why-is-elu-often-a-better-signal-than-cpu-usage)
- [338: Why can latency be high while event loop delay is low?](#338-why-can-latency-be-high-while-event-loop-delay-is-low)
- [339: How does V8's garbage collector interact with the event loop?](#339-how-does-v8s-garbage-collector-interact-with-the-event-loop)
- [340: How do you create a flame graph of event loop work?](#340-how-do-you-create-a-flame-graph-of-event-loop-work)
- [341: How do you take a CPU profile in production without restarting?](#341-how-do-you-take-a-cpu-profile-in-production-without-restarting)
- [342: How can you find which handlers block the loop in production?](#342-how-can-you-find-which-handlers-block-the-loop-in-production)
- [343: How is AsyncLocalStorage implemented in newer Node versions?](#343-how-is-asynclocalstorage-implemented-in-newer-node-versions)
- [344: What is the performance cost of AsyncLocalStorage?](#344-what-is-the-performance-cost-of-asynclocalstorage)
- [345: Why is async_hooks.createHook expensive?](#345-why-is-async_hookscreatehook-expensive)
- [346: How do you keep async context across APIs that lose it?](#346-how-do-you-keep-async-context-across-apis-that-lose-it)
- [347: How can microtask starvation happen in real code?](#347-how-can-microtask-starvation-happen-in-real-code)
- [348: Why can a loop of await null hang I/O?](#348-why-can-a-loop-of-await-null-hang-io)
- [349: How would you design an in-memory rate limiter without leaking timers?](#349-how-would-you-design-an-in-memory-rate-limiter-without-leaking-timers)
- [350: How would you design a service that handles CPU-heavy jobs in Node?](#350-how-would-you-design-a-service-that-handles-cpu-heavy-jobs-in-node)
- [351: How would you handle heartbeats for 100,000 WebSocket connections?](#351-how-would-you-handle-heartbeats-for-100000-websocket-connections)
- [352: The p99 latency spikes every few seconds. How do you investigate?](#352-the-p99-latency-spikes-every-few-seconds-how-do-you-investigate)
- [353: One CPU core is at 100% and the others are idle. What does it tell you?](#353-one-cpu-core-is-at-100-and-the-others-are-idle-what-does-it-tell-you)
- [354: The app got slow after adding password hashing. Why, and how do you fix it?](#354-the-app-got-slow-after-adding-password-hashing-why-and-how-do-you-fix-it)
- [355: File uploads become slow whenever outgoing API calls spike. What could be the reason?](#355-file-uploads-become-slow-whenever-outgoing-api-calls-spike-what-could-be-the-reason)
- [356: A test suite hangs after all tests pass. How do you find the cause?](#356-a-test-suite-hangs-after-all-tests-pass-how-do-you-find-the-cause)
- [357: A script exits before its async work finishes. Why?](#357-a-script-exits-before-its-async-work-finishes-why)
- [358: Memory grows slowly and the number of active handles grows too. What is likely happening?](#358-memory-grows-slowly-and-the-number-of-active-handles-grows-too-what-is-likely-happening)
- [359: Health checks fail under load even though the server is up. Why?](#359-health-checks-fail-under-load-even-though-the-server-is-up-why)
- [360: Logging made the server slow. How can logging block the event loop?](#360-logging-made-the-server-slow-how-can-logging-block-the-event-loop)
- [361: A large JSON response blocks the server. What are your options?](#361-a-large-json-response-blocks-the-server-what-are-your-options)
- [362: Timers fire seconds late in production. What would you check?](#362-timers-fire-seconds-late-in-production-what-would-you-check)
- [363: How does a slow request handler cause head-of-line blocking in Node?](#363-how-does-a-slow-request-handler-cause-head-of-line-blocking-in-node)
- [364: How do you design a fair scheduler for heavy work across requests?](#364-how-do-you-design-a-fair-scheduler-for-heavy-work-across-requests)
- [365: How do vm timeouts relate to the event loop?](#365-how-do-vm-timeouts-relate-to-the-event-loop)
- [366: What was the domain module and why is it deprecated?](#366-what-was-the-domain-module-and-why-is-it-deprecated)
- [367: When exactly does Node decide that a rejection is unhandled?](#367-when-exactly-does-node-decide-that-a-rejection-is-unhandled)
- [368: What is the rejectionHandled event?](#368-what-is-the-rejectionhandled-event)
- [369: What is the output of a script mixing fs.readFile, timers, immediates, promises and nextTick?](#369-what-is-the-output-of-a-script-mixing-fsreadfile-timers-immediates-promises-and-nexttick)
- [370: What is the output when an immediate queues nextTick and a promise before a second immediate runs?](#370-what-is-the-output-when-an-immediate-queues-nexttick-and-a-promise-before-a-second-immediate-runs)
- [371: What is the output of two interleaved promise chains?](#371-what-is-the-output-of-two-interleaved-promise-chains)
- [372: What is the output when an async function returns a promise instead of a value?](#372-what-is-the-output-when-an-async-function-returns-a-promise-instead-of-a-value)
- [373: What is the output when you await a custom thenable object?](#373-what-is-the-output-when-you-await-a-custom-thenable-object)
- [374: What is the output when an EventEmitter listener emits another event?](#374-what-is-the-output-when-an-eventemitter-listener-emits-another-event)
- [375: What is the output of a long recursive process.nextTick chain, and why is it a problem?](#375-what-is-the-output-of-a-long-recursive-processnexttick-chain-and-why-is-it-a-problem)
- [376: Why does await on a non-promise value still pause the function?](#376-why-does-await-on-a-non-promise-value-still-pause-the-function)
- [377: What is the difference between Promise.resolve(p) and new Promise(r => r(p))?](#377-what-is-the-difference-between-promiseresolvep-and-new-promiser--rp)
- [378: Why exactly is the order of setTimeout(0) and setImmediate non-deterministic in the main script?](#378-why-exactly-is-the-order-of-settimeout0-and-setimmediate-non-deterministic-in-the-main-script)
- [379: What happens to timers when the event loop was blocked for a long time?](#379-what-happens-to-timers-when-the-event-loop-was-blocked-for-a-long-time)
- [380: Does setInterval catch up on missed runs after the loop was blocked?](#380-does-setinterval-catch-up-on-missed-runs-after-the-loop-was-blocked)
- [381: Is the order of timers with different durations that become due at the same moment guaranteed?](#381-is-the-order-of-timers-with-different-durations-that-become-due-at-the-same-moment-guaranteed)
- [382: When can sync APIs actually be better than async ones?](#382-when-can-sync-apis-actually-be-better-than-async-ones)
- [383: Why can fs.readFile be slower than fs.readFileSync for many small files?](#383-why-can-fsreadfile-be-slower-than-fsreadfilesync-for-many-small-files)
- [384: How does the event loop behave in AWS Lambda?](#384-how-does-the-event-loop-behave-in-aws-lambda)
- [385: How do container CPU limits affect a Node app?](#385-how-do-container-cpu-limits-affect-a-node-app)
- [386: How do you size processes, worker threads and the thread pool together?](#386-how-do-you-size-processes-worker-threads-and-the-thread-pool-together)
- [387: How would you build a job queue between threads using SharedArrayBuffer?](#387-how-would-you-build-a-job-queue-between-threads-using-sharedarraybuffer)
- [388: When is Node.js the wrong choice because of its event loop model?](#388-when-is-nodejs-the-wrong-choice-because-of-its-event-loop-model)
- [389: Why do Node streams use process.nextTick internally, and how can it surprise you?](#389-why-do-node-streams-use-processnexttick-internally-and-how-can-it-surprise-you)
- [390: Why are stream errors after destroy() delivered asynchronously?](#390-why-are-stream-errors-after-destroy-delivered-asynchronously)
- [391: How does an HTTP agent's connection pool cause queueing?](#391-how-does-an-http-agents-connection-pool-cause-queueing)
- [392: How does HTTP/2 change the picture for the event loop?](#392-how-does-http2-change-the-picture-for-the-event-loop)
- [393: How do you safely run regexes provided by users?](#393-how-do-you-safely-run-regexes-provided-by-users)
- [394: Why does a while loop waiting for a flag set by a callback never end?](#394-why-does-a-while-loop-waiting-for-a-flag-set-by-a-callback-never-end)
- [395: What is the difference between a busy-wait sleep and Atomics.wait?](#395-what-is-the-difference-between-a-busy-wait-sleep-and-atomicswait)
- [396: Can you get a deadlock in Node.js?](#396-can-you-get-a-deadlock-in-nodejs)
- [397: How do you implement an async mutex?](#397-how-do-you-implement-an-async-mutex)
- [398: How do you avoid running the same async work twice at the same time?](#398-how-do-you-avoid-running-the-same-async-work-twice-at-the-same-time)
- [399: What happens if a producer writes to a stream faster than the consumer reads?](#399-what-happens-if-a-producer-writes-to-a-stream-faster-than-the-consumer-reads)
- [400: How do you tune highWaterMark?](#400-how-do-you-tune-highwatermark)
- [401: What is the difference between deep synchronous recursion and async recursion?](#401-what-is-the-difference-between-deep-synchronous-recursion-and-async-recursion)
- [402: Can async recursion leak memory?](#402-can-async-recursion-leak-memory)
- [403: What happens to in-flight requests when the process crashes from an uncaught exception?](#403-what-happens-to-in-flight-requests-when-the-process-crashes-from-an-uncaught-exception)
- [404: How would you write a solid graceful shutdown?](#404-how-would-you-write-a-solid-graceful-shutdown)
- [405: What is EMFILE and how does it relate to the event loop?](#405-what-is-emfile-and-how-does-it-relate-to-the-event-loop)
- [406: What happens to new connections while the event loop is blocked?](#406-what-happens-to-new-connections-while-the-event-loop-is-blocked)
- [407: What is Atomics.waitAsync?](#407-what-is-atomicswaitasync)
- [408: Can MessageChannel be used to yield to the event loop?](#408-can-messagechannel-be-used-to-yield-to-the-event-loop)
- [409: How do process.nextTick, promises and setImmediate compare in cost?](#409-how-do-processnexttick-promises-and-setimmediate-compare-in-cost)
- [410: What happens to timers and I/O when you pause in the debugger?](#410-what-happens-to-timers-and-io-when-you-pause-in-the-debugger)
- [411: How do you tell queueing time from handler time for a request?](#411-how-do-you-tell-queueing-time-from-handler-time-for-a-request)
- [412: How do you use ELU for capacity planning?](#412-how-do-you-use-elu-for-capacity-planning)
- [413: How expensive is monitorEventLoopDelay and what does resolution mean?](#413-how-expensive-is-monitoreventloopdelay-and-what-does-resolution-mean)
- [414: How does diagnostics_channel relate to the event loop?](#414-how-does-diagnostics_channel-relate-to-the-event-loop)
- [415: Does AsyncLocalStorage context follow EventEmitter listeners?](#415-does-asynclocalstorage-context-follow-eventemitter-listeners)
- [416: How do WeakRef and FinalizationRegistry interact with the event loop?](#416-how-do-weakref-and-finalizationregistry-interact-with-the-event-loop)
- [417: Why does reading from process.stdin keep the process alive?](#417-why-does-reading-from-processstdin-keep-the-process-alive)
- [418: How does Node itself run the libuv loop?](#418-how-does-node-itself-run-the-libuv-loop)
- [419: When does a worker thread's event loop end?](#419-when-does-a-worker-threads-event-loop-end)
- [420: How can you keep crypto work from starving fs operations in the thread pool?](#420-how-can-you-keep-crypto-work-from-starving-fs-operations-in-the-thread-pool)
- [421: How can you tell whether an uncaught error came from a throw or a rejected promise?](#421-how-can-you-tell-whether-an-uncaught-error-came-from-a-throw-or-a-rejected-promise)
- [422: What happens if workers send messages while the main thread is blocked?](#422-what-happens-if-workers-send-messages-while-the-main-thread-is-blocked)
- [423: Can you run a periodic task with sub-millisecond precision in Node?](#423-can-you-run-a-periodic-task-with-sub-millisecond-precision-in-node)
- [424: Which Buffer operations can block the event loop?](#424-which-buffer-operations-can-block-the-event-loop)
- [425: How do you process a huge database result without blocking or running out of memory?](#425-how-do-you-process-a-huge-database-result-without-blocking-or-running-out-of-memory)
- [426: How should a Node server handle a sudden burst of 10,000 requests?](#426-how-should-a-node-server-handle-a-sudden-burst-of-10000-requests)
- [427: How do you choose between chunking with setImmediate and using worker threads?](#427-how-do-you-choose-between-chunking-with-setimmediate-and-using-worker-threads)
- [428: Is structuredClone expensive for the event loop?](#428-is-structuredclone-expensive-for-the-event-loop)
- [429: How can you reduce GC pressure in hot paths?](#429-how-can-you-reduce-gc-pressure-in-hot-paths)
- [430: How can APM and tracing agents affect the event loop?](#430-how-can-apm-and-tracing-agents-affect-the-event-loop)
- [431: How can event loop ordering cause flaky tests?](#431-how-can-event-loop-ordering-cause-flaky-tests)
- [432: What should you watch for when moving code that relies on nextTick ordering to ES modules?](#432-what-should-you-watch-for-when-moving-code-that-relies-on-nexttick-ordering-to-es-modules)
- [433: Can microtasks run between two listeners of the same emit() call?](#433-can-microtasks-run-between-two-listeners-of-the-same-emit-call)
- [434: Do microtasks run between two I/O callbacks in the same poll phase?](#434-do-microtasks-run-between-two-io-callbacks-in-the-same-poll-phase)
- [435: How would you explain the event loop with a small model in code?](#435-how-would-you-explain-the-event-loop-with-a-small-model-in-code)
- [436: Why can web streams be slower than Node streams in Node.js?](#436-why-can-web-streams-be-slower-than-node-streams-in-nodejs)
- [437: How would you investigate an incident where the event loop was blocked for 30 seconds?](#437-how-would-you-investigate-an-incident-where-the-event-loop-was-blocked-for-30-seconds)
- [438: How can you detect a blocked main thread from another thread?](#438-how-can-you-detect-a-blocked-main-thread-from-another-thread)
- [439: What are the downsides of making the thread pool very large?](#439-what-are-the-downsides-of-making-the-thread-pool-very-large)
- [440: How much does an idle connection cost in a Node server?](#440-how-much-does-an-idle-connection-cost-in-a-node-server)
- [441: Should library code still use process.nextTick?](#441-should-library-code-still-use-processnexttick)
- [442: How could the TC39 AsyncContext proposal change async context in Node?](#442-how-could-the-tc39-asynccontext-proposal-change-async-context-in-node)
- [443: What are the main event loop changes across Node.js versions?](#443-what-are-the-main-event-loop-changes-across-nodejs-versions)
- [444: How would you design a Node service that stays responsive under heavy mixed load?](#444-how-would-you-design-a-node-service-that-stays-responsive-under-heavy-mixed-load)
- [445: Can a setImmediate be unref'd?](#445-can-a-setimmediate-be-unrefd)
- [446: Why does batching reduce the overhead of crossing from C++ to JavaScript?](#446-why-does-batching-reduce-the-overhead-of-crossing-from-c-to-javascript)
- [447: How does the poll phase use epoll on Linux?](#447-how-does-the-poll-phase-use-epoll-on-linux)
- [448: What happens when you call socket.write()?](#448-what-happens-when-you-call-socketwrite)
- [449: How do you protect a server from slow clients?](#449-how-do-you-protect-a-server-from-slow-clients)
- [450: What do you look for in a code review to catch event loop problems?](#450-what-do-you-look-for-in-a-code-review-to-catch-event-loop-problems)

---

# Easy Questions (1-150)

## 1: What is the event loop in Node.js?

The event loop is the part of Node.js that decides what code runs next. Your JavaScript runs on one main thread. When you start something slow, like reading a file or waiting for a network response, Node hands the work off and keeps going. When the work is done, its callback is put in a queue, and the event loop picks it up and runs it on the main thread.

So the event loop is basically a loop that keeps checking: "is there any finished work or due timer whose callback I should run?" It keeps going until there is nothing left to wait for, then the process exits.

## 2: Why does Node.js need an event loop?

Node runs JavaScript on a single thread. Without an event loop, every slow operation (disk, network, database) would stop the whole program until it finished, and a server could only handle one request at a time.

The event loop lets Node start many operations, wait for all of them at the same time, and run each callback when its result is ready. That is how one Node process can serve thousands of connections without creating a thread per connection.

## 3: Is Node.js single-threaded?

Your JavaScript code runs on a single thread, the main thread. But the Node.js process as a whole uses several threads:

- The main thread runs JavaScript and the event loop.
- libuv has a thread pool (4 threads by default) for things like file system calls, `dns.lookup`, some `crypto` functions and `zlib`.
- V8 uses extra threads for garbage collection and compiling code.
- You can create more threads yourself with `worker_threads`.

So the right answer in an interview is: "JavaScript execution is single-threaded, but Node is not."

## 4: What is libuv?

libuv is a C library that Node.js uses for asynchronous I/O. It provides the event loop itself, the thread pool, timers, TCP and UDP sockets, pipes, file system operations, DNS, child processes and signal handling.

libuv hides the differences between operating systems. On Linux it uses epoll, on macOS and BSD it uses kqueue, and on Windows it uses IOCP. Node's JavaScript APIs like `fs`, `net` and `timers` are built on top of it. You can see which libuv version your Node uses with `process.versions.uv`.

## 5: What does non-blocking I/O mean?

Non-blocking I/O means that when you start an I/O operation, the call returns right away instead of waiting for the result. Your program keeps running other code, and you get the result later through a callback, a promise or an event.

```js
const fs = require("node:fs");

fs.readFile("data.txt", "utf8", (err, text) => {
  console.log("file read done");
});

console.log("this runs first");
```

The file read happens in the background. The main thread is free to do other work in the meantime.

## 6: What is the difference between blocking and non-blocking code?

Blocking code stops the main thread until it finishes. Nothing else can run during that time: no other requests, no timers, no I/O callbacks.

Non-blocking code starts the work and returns at once. The result comes back later through the event loop.

```js
const fs = require("node:fs");

// Blocking: the thread waits here
const a = fs.readFileSync("a.txt", "utf8");

// Non-blocking: the thread continues, callback runs later
fs.readFile("b.txt", "utf8", (err, b) => {});
```

Note that CPU-heavy JavaScript (big loops, heavy parsing) is also blocking, even if there is no I/O involved.

## 7: What is the call stack?

The call stack is where V8 keeps track of the functions that are running right now. When you call a function, it is pushed on the stack. When it returns, it is popped off.

The event loop can only run the next callback when the call stack is empty. That is why a long-running function blocks everything else: the loop has to wait until the function returns.

## 8: What is a callback?

A callback is a function you pass to another function so it can be called later. In Node, most older async APIs take a callback as the last argument, and by convention the first argument of the callback is an error (the "error-first" style).

```js
fs.readFile("config.json", "utf8", (err, data) => {
  if (err) {
    console.error(err);
    return;
  }
  console.log(data);
});
```

The event loop is what eventually calls these callbacks when the operation finishes.

## 9: What happens when you call an async function like fs.readFile?

Roughly this:

1. Your code calls `fs.readFile`. Node creates a request and gives it to libuv.
2. libuv sends the file work to its thread pool. `fs.readFile` returns right away.
3. Your code keeps running until the current call stack is empty.
4. A thread pool thread reads the file. When it is done, it tells the event loop.
5. On a later loop iteration, the event loop runs your callback on the main thread with the result.

Your JavaScript never runs on the thread pool. Only the actual file reading does.

## 10: What are the phases of the Node.js event loop?

Each loop iteration goes through these phases in order:

1. **Timers**: runs `setTimeout` and `setInterval` callbacks whose time has come.
2. **Pending callbacks**: runs some I/O callbacks that were deferred from the previous iteration, for example some TCP errors.
3. **Idle, prepare**: used only inside Node and libuv.
4. **Poll**: waits for new I/O events and runs most I/O callbacks (network data, finished file reads and so on).
5. **Check**: runs `setImmediate` callbacks.
6. **Close callbacks**: runs close handlers, like `socket.on("close")`.

```
   ┌───────────────────────────┐
┌─>│           timers          │
│  └─────────────┬─────────────┘
│  ┌─────────────┴─────────────┐
│  │     pending callbacks     │
│  └─────────────┬─────────────┘
│  ┌─────────────┴─────────────┐
│  │       idle, prepare       │
│  └─────────────┬─────────────┘
│  ┌─────────────┴─────────────┐
│  │           poll            │
│  └─────────────┬─────────────┘
│  ┌─────────────┴─────────────┐
│  │           check           │
│  └─────────────┬─────────────┘
│  ┌─────────────┴─────────────┐
└──┤      close callbacks      │
   └───────────────────────────┘
```

`process.nextTick` callbacks and promise callbacks are not part of any phase. They run after every single callback, before the loop moves on.

## 11: What happens in the timers phase?

In the timers phase the loop runs the callbacks of `setTimeout` and `setInterval` timers whose delay has passed. It only runs timers that are due. A timer set for 100 ms will not run in this phase if only 50 ms have passed.

After each timer callback, Node runs all pending `process.nextTick` callbacks and promise callbacks before moving to the next timer.

## 12: What happens in the pending callbacks phase?

This phase runs some system-level I/O callbacks that libuv put off to the next iteration. A common example is certain TCP errors, like `ECONNREFUSED` on some systems, which are reported here instead of right away.

In everyday code you rarely think about this phase. Most I/O callbacks run in the poll phase.

## 13: What are the idle and prepare phases?

They are internal phases used by libuv and Node itself. You cannot schedule your own callbacks there from JavaScript. Node uses them for housekeeping. For example, Node uses an idle handle to make sure the poll phase does not block when there are `setImmediate` callbacks waiting.

In an interview it is enough to say they exist and are for internal use only.

## 14: What happens in the poll phase?

The poll phase does two things:

1. It asks the operating system for new I/O events (new connections, data on a socket, a finished file operation from the thread pool) and runs their callbacks.
2. If there is nothing to do, it waits (blocks) for new events, but only as long as it makes sense.

If there are `setImmediate` callbacks waiting, the poll phase does not wait and moves on to the check phase. If a timer is due soon, it waits only until that timer is due. Most of your I/O callbacks run in this phase.

## 15: What happens in the check phase?

The check phase runs `setImmediate` callbacks. It comes right after the poll phase, so `setImmediate` is a way to say "run this right after the current I/O processing is done".

All immediates that were queued before the check phase started are run. If one of them calls `setImmediate` again, the new one waits until the next loop iteration.

## 16: What happens in the close callbacks phase?

This phase runs callbacks for handles that were closed, for example the `"close"` event of a socket after `socket.destroy()`. If a handle is closed abruptly, its close callback is run here. Other close events may be emitted through `process.nextTick` instead.

## 17: What is one iteration of the event loop called?

One full pass through all the phases (timers, pending, idle/prepare, poll, check, close) is often called a "tick" or a "loop iteration".

Be careful in interviews: `process.nextTick` does not mean "next loop iteration". Its callback runs right after the current operation, long before the next iteration. The name is historical and a bit misleading.

## 18: When does the event loop start?

When you run `node app.js`, Node first sets things up and runs your main script from top to bottom synchronously. Everything in the main script runs before the event loop processes any callback.

After the main script finishes (and after `process.nextTick` and promise callbacks queued by it have run), Node enters the event loop and starts processing timers, I/O and so on.

## 19: When does a Node.js process exit?

The process exits when the event loop has nothing left to do. That means there are no active timers, no open servers or sockets, no pending I/O requests and no other active handles that keep the loop alive.

It can also exit earlier if you call `process.exit()`, if there is an uncaught exception, or if the process gets a signal like `SIGTERM` without a handler.

```js
setTimeout(() => console.log("done"), 1000);
// Process stays alive about 1 second, prints "done", then exits.
```

## 20: What is setTimeout in Node.js?

`setTimeout(callback, delay, ...args)` schedules a callback to run once after at least `delay` milliseconds. The callback runs in the timers phase of the event loop.

```js
setTimeout(
  (name) => {
    console.log(`Hello, ${name}`);
  },
  500,
  "Ann",
);
```

It is a global in Node, so you don't need to import it, but it also exists in the `node:timers` module.

## 21: What does setTimeout return in Node.js?

In Node, `setTimeout` returns a `Timeout` object, not a number like in the browser. The object has methods such as `ref()`, `unref()`, `hasRef()`, `refresh()` and `close()`.

```js
const t = setTimeout(() => {}, 1000);
console.log(typeof t); // "object"
clearTimeout(t);
```

If you need a number, you can convert the object with `+t` (it has `Symbol.toPrimitive`), and `clearTimeout` accepts that number too.

## 22: What is setInterval?

`setInterval(callback, delay)` runs the callback again and again, every `delay` milliseconds, until you stop it with `clearInterval`. Like `setTimeout`, it runs in the timers phase, and the delay is a minimum, not an exact time.

```js
let count = 0;
const id = setInterval(() => {
  count++;
  console.log("tick", count);
  if (count === 3) clearInterval(id);
}, 1000);
```

## 23: How do you cancel a timer?

Use `clearTimeout` for `setTimeout` and `clearInterval` for `setInterval`, passing the object that was returned.

```js
const t = setTimeout(() => console.log("never runs"), 1000);
clearTimeout(t);
```

Calling `clearTimeout` on a timer that already fired, or on `undefined`, does nothing and does not throw. In Node the two clear functions are interchangeable, but using the matching one makes the code easier to read.

## 24: What is setImmediate?

`setImmediate(callback, ...args)` schedules a callback to run in the check phase, which is right after the poll phase of the current or next loop iteration.

```js
setImmediate(() => {
  console.log("runs after current I/O callbacks");
});
```

It is useful when you want to run something "as soon as possible, but after the event loop had a chance to handle I/O". It is a Node feature and does not exist in browsers as a standard.

## 25: How do you cancel setImmediate?

`setImmediate` returns an `Immediate` object. Pass it to `clearImmediate`.

```js
const im = setImmediate(() => console.log("never runs"));
clearImmediate(im);
```

## 26: What is process.nextTick?

`process.nextTick(callback, ...args)` puts a callback into the "next tick queue". This queue is processed right after the current JavaScript operation finishes, before the event loop continues to the next callback or phase, and even before promise callbacks.

```js
process.nextTick(() => console.log("nextTick"));
console.log("sync");
// sync
// nextTick
```

It is not really part of the event loop phases. It runs "in between" everything.

## 27: What is a microtask?

A microtask is a small job that runs right after the current piece of JavaScript finishes and before the event loop moves on. In Node, the main microtasks are:

- Promise callbacks (`then`, `catch`, `finally`, and the code after `await`)
- Callbacks queued with `queueMicrotask`

`process.nextTick` callbacks are similar in timing, but they live in their own queue that Node handles before the promise microtask queue.

## 28: What is the microtask queue?

The microtask queue is a queue managed by V8 that holds promise reactions and `queueMicrotask` callbacks. Node drains it completely after each callback from the event loop (after first draining the `process.nextTick` queue).

"Drains completely" means that if a microtask adds another microtask, the new one also runs before the loop continues.

## 29: What is queueMicrotask?

`queueMicrotask(callback)` adds a function to the microtask queue, the same queue promise callbacks use. It is a standard web API and works the same in Node and in browsers.

```js
queueMicrotask(() => console.log("microtask"));
console.log("sync");
// sync
// microtask
```

The Node docs suggest `queueMicrotask` over `process.nextTick` for most user code, because it is portable and its order with promises is easy to reason about.

## 30: What are macrotasks in Node.js?

"Macrotask" is an informal name for callbacks that run from the event loop phases: timer callbacks, I/O callbacks, `setImmediate` callbacks and close callbacks. The term is borrowed from browser discussions.

The simple rule is: one macrotask runs, then all `nextTick` callbacks and microtasks run, then the next macrotask runs. Node's docs don't use the word "macrotask" much; they talk about phases and queues instead.

## 31: What is the difference between process.nextTick and setImmediate?

- `process.nextTick` runs right after the current operation, before the event loop continues. It runs before promise callbacks and before any I/O or timers.
- `setImmediate` runs in the check phase, after the poll phase. Other I/O callbacks can run before it.

```js
setImmediate(() => console.log("immediate"));
process.nextTick(() => console.log("nextTick"));
// nextTick
// immediate
```

`nextTick` is "now, but after this function". `setImmediate` is "soon, after I/O had a chance".

## 32: Why are the names nextTick and setImmediate confusing?

Because they are backwards. `process.nextTick` runs immediately after the current operation, and `setImmediate` runs on a later iteration of the loop (in the check phase). The Node docs even say the names should be swapped, but changing them would break a lot of npm packages, so they stay as they are.

## 33: What is the difference between setTimeout(fn, 0) and setImmediate(fn)?

- `setTimeout(fn, 0)` runs in the timers phase once at least 1 ms has passed (Node turns 0 into 1).
- `setImmediate(fn)` runs in the check phase, right after poll.

Which one runs first depends on where you call them. From the main script the order is not guaranteed. Inside an I/O callback, `setImmediate` always runs first, because the check phase comes right after poll and the timers phase only comes in the next iteration.

## 34: Does setTimeout(fn, 0) really run after 0 ms?

No. In Node a delay of 0 is changed to 1 ms. Also, the callback can only run when the event loop reaches the timers phase and the call stack is empty. If the main thread is busy, it runs later.

So `setTimeout(fn, 0)` means "run this at the next chance in the timers phase, after at least 1 ms".

## 35: Is the setTimeout delay guaranteed?

No. The delay is a minimum. Node promises the callback will not run before the delay, but it can run later if:

- The main thread is busy running other code.
- Many other callbacks are waiting.
- The poll phase is processing a lot of I/O.
- The machine is overloaded or the process was paused.

Never use timers for exact timing.

## 36: What is the minimum delay for setTimeout in Node.js?

1 millisecond. If you pass 0, a negative number, `NaN` or a non-number, Node uses 1 ms. Unlike browsers, Node does not clamp nested timers to 4 ms.

## 37: Where do promise callbacks run?

Promise callbacks (`.then`, `.catch`, `.finally`, and code after `await`) run as microtasks. They run after the current callback finishes and after the `process.nextTick` queue is empty, but before the event loop moves to the next callback or phase.

They never run in the middle of other synchronous code, even if the promise is already resolved.

## 38: Which runs first, process.nextTick or a resolved promise's then?

In a CommonJS script, `process.nextTick` runs first.

```js
Promise.resolve().then(() => console.log("promise"));
process.nextTick(() => console.log("nextTick"));
// nextTick
// promise
```

Node drains the `nextTick` queue first, then the promise microtask queue. In an ES module the main code itself runs as part of a promise job, so there the promise callback runs first. That difference is covered in more detail in the moderate section.

## 39: What is the output order of sync code, a timer, a promise and nextTick?

```js
console.log("A");
setTimeout(() => console.log("B"), 0);
Promise.resolve().then(() => console.log("C"));
process.nextTick(() => console.log("D"));
console.log("E");
```

Output:

```
A
E
D
C
B
```

`A` and `E` are synchronous. Then the `nextTick` queue runs (`D`), then promise callbacks (`C`). The timer (`B`) runs later in the timers phase of the event loop.

## 40: What does async/await do with the event loop?

`async`/`await` is built on promises. When an `async` function hits `await`, it stops and returns control to the caller. The rest of the function is scheduled as a promise callback (a microtask) that runs once the awaited value is ready.

```js
async function load() {
  console.log("1");
  await null;
  console.log("3");
}

load();
console.log("2");
// 1, 2, 3
```

`await` does not block the thread. It only pauses that one function.

## 41: What happens after await?

When the awaited promise settles, the rest of the async function is queued as a microtask. It runs after the current callback is done and after the `nextTick` queue. If the awaited promise is already resolved, the rest still does not run synchronously. It always waits at least one microtask.

## 42: Does async code run in parallel in Node.js?

Your JavaScript does not run in parallel. Only one callback runs at a time on the main thread. What runs in parallel is the waiting: many network requests, file reads or database queries can be in progress at the same time, handled by the OS or the thread pool.

If you need JavaScript code itself to run in parallel, you need worker threads or multiple processes.

## 43: What is the difference between concurrency and parallelism in Node.js?

- **Concurrency** means many tasks are in progress at the same time, but they take turns on one thread. Node is very good at this through the event loop.
- **Parallelism** means tasks really run at the same moment on different CPU cores.

Node's main thread gives you concurrency. The thread pool, worker threads and the cluster module give you parallelism.

## 44: What is the thread pool in Node.js?

The thread pool is a set of threads managed by libuv. It is used for work that cannot be done in a non-blocking way by the operating system, or that is too CPU-heavy for the main thread. When the work is finished, the result is passed back to the event loop, and your callback runs on the main thread.

You don't create or manage these threads yourself. Node uses them inside some built-in APIs.

## 45: What is the default thread pool size?

4 threads. You can change it with the `UV_THREADPOOL_SIZE` environment variable, up to 1024.

```bash
UV_THREADPOOL_SIZE=8 node server.js
```

There is one thread pool per process. Worker threads in the same process share it.

## 46: Which operations use the thread pool?

The main ones are:

- Almost all `fs` file operations (except `fs.watch` and the sync versions, which run on the main thread).
- `dns.lookup` (and anything that uses it, like `http.get("http://example.com")` by default).
- Async `crypto` functions that are CPU-heavy: `pbkdf2`, `scrypt`, `randomBytes`, `randomFill`, `generateKeyPair` and others.
- Async `zlib` functions like `zlib.gzip`.
- Native addons that use the thread pool.

## 47: Which operations do not use the thread pool?

- Network I/O: TCP, UDP, HTTP sockets, pipes. These use the OS event mechanisms (epoll, kqueue, IOCP) directly on the main thread.
- `dns.resolve*` functions, which use the c-ares library and talk to DNS servers over the network.
- Timers.
- All your JavaScript code.
- Sync APIs like `fs.readFileSync` or `crypto.pbkdf2Sync`, which run on the main thread and block it.

## 48: How does Node handle network I/O without threads?

Operating systems can watch many sockets at once and tell a program which ones are ready to read or write. Node (through libuv) registers all sockets with that OS mechanism. In the poll phase, it asks the OS "which sockets are ready?" and runs the callbacks for those.

This means one thread can handle thousands of connections. It only does work when data actually arrives.

## 49: What are epoll, kqueue and IOCP?

They are the OS features libuv uses to watch many I/O sources at once:

- **epoll**: Linux.
- **kqueue**: macOS and BSD.
- **IOCP** (I/O completion ports): Windows.

epoll and kqueue tell you when a socket is ready. IOCP tells you when an operation has completed. libuv hides this difference so Node behaves the same on all platforms.

## 50: What does "blocking the event loop" mean?

It means some code takes so long on the main thread that the event loop can't run anything else. While it runs, no timers fire, no requests are handled, and no I/O callbacks run.

```js
app.get("/slow", (req, res) => {
  const end = Date.now() + 5000;
  while (Date.now() < end) {} // blocks everyone for 5 seconds
  res.send("done");
});
```

During those 5 seconds, every other user of the server waits too.

## 51: What are some examples of code that blocks the event loop?

- Long `for` or `while` loops over big data.
- `JSON.parse` or `JSON.stringify` on very large objects.
- Sync APIs: `fs.readFileSync`, `crypto.pbkdf2Sync`, `zlib.gzipSync`, `child_process.execSync`.
- Bad regular expressions that take very long on certain input (ReDoS).
- Sorting or processing huge arrays.
- Heavy math, image processing, or compression done in JavaScript.
- Very heavy synchronous logging.

## 52: Why are sync fs methods like readFileSync dangerous in a server?

Because they run on the main thread and block it until the disk work is done. In a server, every request that calls `readFileSync` makes all other requests wait. With a slow disk or a big file, that can add a lot of latency for everyone.

The async versions (`fs.readFile`, `fs.promises.readFile`) do the work on the thread pool and keep the main thread free.

## 53: When is it fine to use sync methods?

Sync methods are fine when nothing else needs to run at the same time:

- At startup, before the server starts listening (for example, reading a config file).
- In CLI tools and build scripts that do one thing at a time.
- In small one-off scripts.

They are a problem inside request handlers or any code that runs while the app is serving traffic.

## 54: What is a CPU-bound task?

A CPU-bound task is one whose speed depends on how fast the CPU can compute, not on waiting for I/O. Examples are hashing, image resizing, compression, encryption, parsing large data, and complex calculations.

In Node, CPU-bound JavaScript runs on the main thread and blocks the event loop, so it needs special handling (worker threads, splitting work, or another service).

## 55: What is an I/O-bound task?

An I/O-bound task spends most of its time waiting: for a database, a network call, a file read or another service. The CPU is mostly idle.

Node is a good fit for I/O-bound work, because the event loop can wait for many of these at once and do other work in the meantime.

## 56: Why is Node.js good at I/O-bound work?

Because waiting is cheap in Node. A pending network request does not need its own thread. It's just a registered event. One process can have thousands of requests waiting on databases and APIs, and the main thread only spends time on the small bits of JavaScript that handle each result.

Thread-per-request servers need memory and context switching for each waiting thread. Node avoids most of that.

## 57: Why is Node.js not great at CPU-heavy work by default?

Because all JavaScript runs on one main thread. If one request does 2 seconds of CPU work, every other request has to wait 2 seconds. You can't use more cores unless you add worker threads or more processes.

Node can do CPU-heavy work, but you have to design for it: move it to worker threads, use native modules, or put it in a separate service.

## 58: What is the callback queue?

"Callback queue" (or "event queue") is a simple way to describe where finished work waits before its callback runs. In reality Node does not have one single queue. Each phase has its own queue (timers, I/O callbacks, immediates, close callbacks), and there are also the `nextTick` queue and the promise microtask queue.

In interviews it's good to mention that the single "callback queue" picture is a simplification.

## 59: Is there one queue or many queues in the Node.js event loop?

Many. The main ones are:

- Timers (stored in a sorted structure, not a simple queue)
- Pending callbacks
- Poll / I/O events
- Check (`setImmediate`)
- Close callbacks
- The `process.nextTick` queue
- The promise microtask queue (managed by V8)

The phases run in a fixed order, and the `nextTick` and microtask queues are drained after each callback.

## 60: What is an EventEmitter?

`EventEmitter` from `node:events` is a class that lets objects emit named events and lets other code listen for them. Many Node core objects are emitters: servers, sockets, streams, `process`.

```js
const { EventEmitter } = require("node:events");

const bus = new EventEmitter();
bus.on("order", (id) => console.log("new order", id));
bus.emit("order", 42);
```

## 61: Are EventEmitter listeners called synchronously or asynchronously?

Synchronously. `emit()` calls every listener one after another, right away, in the order they were added, and returns only after all of them are done.

```js
bus.on("x", () => console.log("listener"));
bus.emit("x");
console.log("after emit");
// listener
// after emit
```

EventEmitter itself has nothing to do with the event loop. The async part comes from the code that calls `emit` (for example, a socket emitting `"data"` from an I/O callback).

## 62: How is the Node.js event loop different from the browser event loop?

The main differences:

- Node's loop is from libuv and has named phases (timers, poll, check and so on). Browsers follow the HTML spec, which has task queues and a rendering step.
- Node has `process.nextTick` and `setImmediate`. Browsers don't.
- Browsers have rendering, `requestAnimationFrame` and user input events. Node doesn't.
- Node exits when the loop has nothing to do. A browser tab keeps running.
- Node has a thread pool for file system and some crypto work.

Both drain the microtask queue after each task, and since Node 11 the order between timers and microtasks matches browsers.

## 63: Does Node.js have requestAnimationFrame?

No. `requestAnimationFrame` is tied to screen rendering, and Node has no screen. If you need to run something on the next loop iteration, use `setImmediate`. If you need a delay, use `setTimeout`.

## 64: What is the role of V8 compared to libuv?

- **V8** is the JavaScript engine. It parses, compiles and runs your JavaScript, manages memory and garbage collection, and handles promises and the microtask queue.
- **libuv** handles the event loop, async I/O, timers and the thread pool.

Node glues them together: libuv tells Node an event happened, and Node asks V8 to run the matching JavaScript callback.

## 65: Who runs JavaScript, V8 or libuv?

V8 runs all JavaScript. libuv never runs JavaScript. It only runs C code for I/O and tells Node when something is ready. Even work done on the libuv thread pool is C/C++ code (like reading a file); the JavaScript callback for it still runs on the main thread through V8.

## 66: What is the timers/promises module?

`node:timers/promises` gives you promise-based versions of timers:

```js
const {
  setTimeout,
  setImmediate,
  setInterval,
} = require("node:timers/promises");

async function main() {
  await setTimeout(1000); // wait 1 second
  const value = await setImmediate("hi"); // resolves with "hi"

  for await (const _ of setInterval(500)) {
    console.log("every 500 ms");
    break;
  }
}
main();
```

They accept an `AbortSignal` for cancelling.

## 67: How do you wait for some time with promises in Node.js?

Use `setTimeout` from `node:timers/promises`:

```js
const { setTimeout: sleep } = require("node:timers/promises");

async function run() {
  console.log("start");
  await sleep(2000);
  console.log("2 seconds later");
}
run();
```

This does not block the thread. Other code keeps running during those 2 seconds. In older code you will see `new Promise((r) => setTimeout(r, ms))`, which does the same.

## 68: What is the node:timers module?

`node:timers` is the core module that contains `setTimeout`, `setInterval`, `setImmediate` and their clear functions. The same functions are also available as globals, so you usually don't need to import it. Its sub-module `node:timers/promises` has the promise-based versions.

## 69: Can you pass arguments to a setTimeout callback?

Yes. Any arguments after the delay are passed to the callback:

```js
setTimeout(
  (a, b) => {
    console.log(a + b);
  },
  100,
  2,
  3,
); // prints 5
```

The same works for `setInterval` and `setImmediate` (where arguments come right after the callback).

## 70: What is this inside a setTimeout callback in Node.js?

If you use a normal function (not an arrow function), `this` is the `Timeout` object. In browsers it is `window`, so this is a small difference.

```js
setTimeout(function () {
  console.log(this.constructor.name); // "Timeout"
}, 10);
```

With arrow functions, `this` comes from the surrounding scope as usual.

## 71: What does unref() do on a timer?

By default an active timer keeps the process alive. Calling `unref()` tells Node "don't keep the process running just for this timer". If nothing else is keeping the loop alive, the process exits and the timer never fires.

```js
const t = setInterval(() => console.log("metrics"), 10000);
t.unref(); // the app can still exit normally
```

This is useful for background jobs like metrics or cache cleanup.

## 72: What does ref() do on a timer?

`ref()` undoes `unref()`. It makes the timer keep the process alive again. Timers are ref'd by default, so you only need `ref()` if you called `unref()` before.

## 73: What does hasRef() return?

`timeout.hasRef()` returns `true` if the timer is currently keeping the process alive (ref'd), and `false` if it was unref'd.

```js
const t = setTimeout(() => {}, 1000);
console.log(t.hasRef()); // true
t.unref();
console.log(t.hasRef()); // false
```

## 74: What is timeout.refresh()?

`refresh()` restarts the timer with its original delay, starting from now, without creating a new timer object. It's useful for things like idle timeouts that should reset on each activity.

```js
const idle = setTimeout(() => socket.end(), 30000);

socket.on("data", () => {
  idle.refresh(); // push the deadline 30 seconds forward
});
```

It is cheaper than calling `clearTimeout` and `setTimeout` again.

## 75: What happens if you pass a delay larger than 2147483647?

The maximum delay is 2147483647 ms (about 24.8 days), the largest 32-bit signed integer. If you pass a bigger value, Node sets the delay to 1 ms and prints a `TimeoutOverflowWarning`. So the callback runs almost right away, which is usually a bug.

For very long delays, use a scheduler library or chain several shorter timers.

## 76: What happens if you pass a negative delay or NaN to setTimeout?

Node treats it as 1 ms. The callback runs at the next timers phase after at least 1 ms. Since Node 23, passing a negative number also emits a `TimeoutNegativeWarning`, and `NaN` emits a `TimeoutNaNWarning`, to help you catch the bug.

## 77: What is the order of setTimeout(fn, 0) and setImmediate(fn) in the main script?

It is not guaranteed.

```js
setTimeout(() => console.log("timeout"), 0);
setImmediate(() => console.log("immediate"));
```

Sometimes you get `timeout` first, sometimes `immediate`. The timer needs at least 1 ms to pass. If the loop reaches the timers phase after 1 ms, the timeout runs first. If it gets there faster, the timer is not due yet, and the immediate runs first in the check phase. It depends on how busy the machine is.

## 78: What is the order of setTimeout(fn, 0) and setImmediate(fn) inside an I/O callback?

Inside an I/O callback, `setImmediate` always runs first:

```js
const fs = require("node:fs");

fs.readFile(__filename, () => {
  setTimeout(() => console.log("timeout"), 0);
  setImmediate(() => console.log("immediate"));
});
// immediate
// timeout
```

The I/O callback runs in the poll phase. The next phase is check (immediates), and the timers phase only comes after that.

## 79: What does "tick" mean in process.nextTick?

In Node, a "tick" loosely means one run of JavaScript that was started by the event loop, plus the queues that are drained after it. `process.nextTick` puts the callback at the end of the current tick, so it runs as soon as the current code finishes, before the event loop does anything else. It does not wait for the next loop iteration, despite the name.

## 80: Can you pass arguments to process.nextTick?

Yes. Extra arguments after the callback are passed to it:

```js
process.nextTick(
  (a, b) => {
    console.log(a, b);
  },
  "x",
  "y",
);
```

This avoids creating a closure, which is why Node core uses it a lot.

## 81: What is event loop starvation?

Starvation is when some callbacks never get a chance to run because other work keeps taking all the time. For example, if code keeps adding `process.nextTick` callbacks in a loop, Node keeps draining that queue and never reaches the poll phase, so I/O callbacks and timers wait forever.

## 82: Can process.nextTick starve the event loop?

Yes. The `nextTick` queue is drained completely before the loop continues, including callbacks added while draining.

```js
function spin() {
  process.nextTick(spin);
}
spin();

setTimeout(() => console.log("never runs"), 0);
```

The timer never runs, and the process uses 100% CPU. Promise microtasks that keep scheduling new microtasks cause the same problem.

## 83: Can setImmediate starve the event loop?

No. If a `setImmediate` callback schedules another `setImmediate`, the new one runs in the next loop iteration, not in the current check phase. So the loop still goes through timers and poll between them.

```js
function work() {
  // do a small piece of work
  setImmediate(work);
}
work();
// Timers and I/O keep running in between.
```

This is why `setImmediate` is the right tool for splitting long work into pieces.

## 84: What is the event loop doing when nothing is happening?

It waits in the poll phase. It asks the OS to wake it up when an I/O event arrives, with a timeout based on the next timer. While waiting, the process uses almost no CPU. When an event arrives or a timer is due, the loop wakes up and continues.

## 85: How does the loop decide how long to wait in the poll phase?

Roughly:

- If there are `setImmediate` callbacks waiting, or the loop is stopping, it does not wait at all.
- If there are timers, it waits at most until the nearest timer is due.
- If there are no timers but there are other active handles (like an open server), it can wait forever until an I/O event comes.

## 86: Why might a timer fire late?

Because a timer can only run when the loop reaches the timers phase. Common reasons for a delay:

- A long synchronous function is running.
- Many I/O callbacks are being processed in the poll phase.
- A large number of microtasks or `nextTick` callbacks are being drained.
- Garbage collection is pausing the thread.
- The machine is busy or the container is CPU-limited.

## 87: What happens if a timer callback throws an error?

The error is not caught by the code that called `setTimeout`, because that code already returned. It becomes an uncaught exception. By default Node prints the stack trace and exits with code 1.

```js
try {
  setTimeout(() => {
    throw new Error("boom");
  }, 10);
} catch (e) {
  // never reached
}
```

You need to handle errors inside the callback itself.

## 88: Why can't you catch async errors with a try/catch around the call?

Because the callback runs later, from the event loop, in a different call stack. By then the `try/catch` block has already finished. The fix is to put `try/catch` inside the callback, use the error-first callback argument, or use promises with `await` inside a `try/catch`:

```js
async function read() {
  try {
    const data = await fs.promises.readFile("missing.txt");
  } catch (err) {
    console.error("caught:", err.code);
  }
}
```

With `await`, the error comes back into your function, so `try/catch` works.

## 89: What does Node do with an unhandled promise rejection?

Since Node 15, an unhandled promise rejection is treated like an uncaught exception: Node prints the error and exits with a non-zero code. Before that, Node only printed a warning.

```js
Promise.reject(new Error("nobody handles me"));
// The process crashes after the microtask queue is processed.
```

You can listen for `process.on("unhandledRejection", ...)` to log these, but the real fix is to always handle rejections.

## 90: What is the uncaughtException event?

`process.on("uncaughtException", handler)` is called when an error is thrown and not caught anywhere. If you add a listener, Node doesn't exit by default anymore.

```js
process.on("uncaughtException", (err) => {
  console.error("fatal", err);
  process.exit(1);
});
```

The safe practice is to log the error and then exit, because the app may be in a broken state.

## 91: What is the beforeExit event?

`process.on("beforeExit")` fires when the event loop has no more work and the process is about to exit. If the listener schedules new async work, the loop continues and `beforeExit` may fire again later.

```js
process.on("beforeExit", (code) => {
  console.log("loop is empty, code", code);
});
```

It does not fire when you call `process.exit()` or on an uncaught exception.

## 92: What is the exit event?

`process.on("exit", (code) => {})` fires when the process is about to exit, either because the loop is empty or because `process.exit()` was called. At this point the event loop is done. Only synchronous code in the listener will run.

## 93: Can you run async code in the exit event?

No. Anything async scheduled in an `"exit"` listener (timers, file writes with callbacks, promises) will not complete, because the event loop is no longer running.

```js
process.on("exit", () => {
  setTimeout(() => console.log("never printed"), 0);
  console.log("this prints");
});
```

If you need async cleanup, do it before exiting, for example in a `SIGTERM` handler or in `beforeExit`.

## 94: What does process.exit() do to pending callbacks?

It stops the process as soon as possible. Pending timers, I/O callbacks, promises and even some pending writes to stdout may be lost. Only `"exit"` listeners run.

That's why it's often better to set `process.exitCode = 1` and let the process end naturally when the loop is empty.

## 95: What keeps a Node.js process alive?

Anything that is active and ref'd in the event loop, such as:

- A pending timer or interval
- A listening server
- An open socket or connection
- Pending file system or DNS requests
- A child process or worker that hasn't exited
- `process.stdin` when it is being read

When none of these are left, the process exits.

## 96: Does a pending promise keep the process alive?

No. A promise by itself is just an object in memory. If nothing else (a timer, a socket, an I/O request) is going to resolve it, Node has nothing to wait for and exits.

```js
new Promise(() => {}); // never resolves
console.log("end");
// Process exits right away.
```

In an ES module with top-level `await` on such a promise, Node exits with code 13 and a warning about an unsettled top-level await.

## 97: What is a handle in libuv?

A handle is a long-lived object that represents something that can produce events over time, for example a TCP server, a socket, a timer, a signal watcher or a child process. As long as an active handle is ref'd, it keeps the event loop alive. Handles are closed with `uv_close`, and their close callback runs in the close phase.

## 98: What is a request in libuv?

A request is a short-lived, one-time operation, like a single file read, a single write to a socket, or a `dns.lookup` call. It is active until the operation finishes, and it also keeps the loop alive while pending. Handles live long; requests are one-shot.

## 99: What is the main thread in Node.js?

The main thread is the thread that runs your JavaScript and the event loop. All callbacks, promise handlers and event listeners run on it. If it's busy, nothing else in your app's JavaScript can run.

Worker threads each have their own separate main-like thread with their own event loop.

## 100: What happens when you run node app.js?

In short:

1. Node starts, sets up V8, libuv and the core modules.
2. It loads and runs `app.js` from top to bottom. All synchronous code runs now. Async calls register timers, I/O requests and so on.
3. It drains the `nextTick` and microtask queues.
4. It enters the event loop and processes timers, I/O, immediates and close callbacks.
5. When nothing is left to do, it emits `beforeExit`, then `exit`, and the process ends.

## 101: When does the main script run compared to the event loop?

The main script runs first, completely, before the event loop processes any callbacks. Even a `setTimeout(fn, 0)` scheduled on the first line can't run until the whole script has finished.

```js
setTimeout(() => console.log("timer"), 0);
for (let i = 0; i < 1e9; i++) {} // takes a while
console.log("script done");
// script done
// timer
```

## 102: How does fs.promises relate to the event loop?

`fs.promises` (or `node:fs/promises`) gives you promise-based file APIs. Under the hood they work like the callback versions: the work is done on the libuv thread pool, and when it finishes, the promise is resolved on the main thread. The code after `await` then runs as a microtask.

```js
const { readFile } = require("node:fs/promises");

async function main() {
  const text = await readFile("notes.txt", "utf8");
  console.log(text.length);
}
main();
```

## 103: What is the difference between fs.readFile and fs.readFileSync for the event loop?

- `fs.readFileSync` reads the file on the main thread. Nothing else runs until it's done.
- `fs.readFile` sends the read to the thread pool and returns right away. The callback runs later from the poll phase.

For one small file at startup there's little difference. In a busy server, `readFileSync` makes every other request wait.

## 104: What is the difference between callback-based and promise-based APIs?

They do the same async work. The difference is how you get the result:

- Callback-based: you pass a function, usually error-first, that's called when the work is done.
- Promise-based: the function returns a promise you can `await` or chain with `.then`.

For the event loop, the main difference is timing of the final step: a callback runs directly from the loop phase, while promise handlers run as microtasks right after that.

## 105: What is callback hell and does it affect the event loop?

Callback hell is deeply nested callbacks that are hard to read and maintain:

```js
getUser(id, (err, user) => {
  getOrders(user, (err, orders) => {
    getItems(orders, (err, items) => {
      // ...
    });
  });
});
```

It's a readability problem, not a performance problem. The event loop handles it fine. Promises and `async`/`await` fix the readability.

## 106: What is util.promisify?

`util.promisify` turns a function that uses an error-first callback into one that returns a promise.

```js
const util = require("node:util");
const fs = require("node:fs");

const readFile = util.promisify(fs.readFile);

readFile("a.txt", "utf8").then((text) => console.log(text));
```

Most core modules already have promise versions (`fs/promises`, `dns/promises`, `timers/promises`), so you need it mostly for older libraries.

## 107: How does an HTTP server use the event loop?

When you call `server.listen()`, Node creates a listening socket and registers it with the OS. In the poll phase:

1. A new connection arrives. Node accepts it and emits `"connection"`.
2. Data arrives on the socket. Node parses the HTTP request and calls your request handler.
3. Your handler starts async work (database, files) and returns.
4. When that work finishes, its callback runs, and you send the response.

Thousands of connections can be open at once. Each only uses the main thread when something happens on it.

## 108: Why can one Node process handle many connections?

Because an idle connection costs almost nothing. It's just a socket registered with the OS, not a thread. The main thread only spends time on a connection when data arrives or a response needs sending. As long as each handler does only a small amount of synchronous work, one process can handle many thousands of open connections.

## 109: What happens if one request handler runs a slow loop?

Every other request waits. The event loop can't accept new connections, read data from other sockets or fire timers until that loop finishes. Response times go up for all users, health checks can fail, and timeouts can trigger. This is the most common performance mistake in Node servers.

## 110: What are worker threads?

Worker threads (`node:worker_threads`) let you run JavaScript in parallel on other threads. Each worker has its own V8 instance and its own event loop. They are meant for CPU-heavy work, so that the main thread stays free.

```js
const { Worker } = require("node:worker_threads");

const worker = new Worker("./heavy-task.js", { workerData: { n: 40 } });
worker.on("message", (result) => console.log("result", result));
worker.on("error", console.error);
```

## 111: What is the cluster module?

The `node:cluster` module lets you start several Node processes (workers) that share the same server port. Each worker is a separate process with its own event loop and memory. The primary process distributes incoming connections between them.

It's a way to use all CPU cores for a server. Today many teams use a process manager (like PM2) or containers and a load balancer for the same goal.

## 112: What is the difference between worker threads and the libuv thread pool?

- The **thread pool** is internal to libuv. It runs C/C++ work for Node's built-in APIs (fs, dns.lookup, crypto, zlib). You can't run your own JavaScript there.
- **Worker threads** run your own JavaScript in parallel. You create and control them.

Both use extra threads, but for different purposes.

## 113: What is the difference between worker threads and child processes?

- **Worker threads** run in the same process. They start faster, use less memory, and can share memory with `SharedArrayBuffer` and transfer data cheaply.
- **Child processes** (`child_process`, `cluster`) are separate OS processes with their own memory. They are more isolated: if one crashes, the others keep running. They can also run non-Node programs.

Use worker threads for CPU-heavy JavaScript. Use child processes for isolation or to run other programs.

## 114: Does each worker thread have its own event loop?

Yes. Each worker has its own event loop, its own timers, its own microtask queue and its own JavaScript heap. Blocking a worker's loop doesn't block the main thread, and the other way around. The libuv thread pool, however, is shared by the whole process.

## 115: What is event loop delay?

Event loop delay (also called lag) is how long a callback waits beyond when it should have run. If you schedule a 10 ms timer and it fires after 60 ms, the loop was about 50 ms late.

High delay means the main thread is too busy: too much synchronous work, too many callbacks, or long GC pauses. It's one of the most useful health metrics for a Node service.

## 116: How can you quickly check if the event loop is blocked?

A simple way is to schedule a timer and measure how late it fires:

```js
let last = Date.now();
setInterval(() => {
  const now = Date.now();
  const lag = now - last - 500;
  if (lag > 50) console.warn(`event loop lag: ${lag} ms`);
  last = now;
}, 500).unref();
```

For real monitoring, use `perf_hooks.monitorEventLoopDelay()`, which is more accurate and cheaper.

## 117: What is perf_hooks?

`node:perf_hooks` is the core module for performance measurement. For the event loop, the useful parts are:

- `monitorEventLoopDelay()`: a histogram of event loop delay.
- `performance.eventLoopUtilization()`: how busy the loop is.
- `performance.now()`, `performance.mark()` and `performance.measure()` for timing code.
- `PerformanceObserver` for watching things like GC events.

## 118: Does Promise.all run tasks in parallel?

`Promise.all` doesn't run anything by itself. It waits for promises that are already running. If those promises are I/O operations (network calls, file reads), they are in progress at the same time, so they finish faster than doing them one by one.

```js
const [user, orders] = await Promise.all([getUser(id), getOrders(id)]);
```

But if the work is CPU-bound JavaScript, it still runs one piece at a time on the main thread. `Promise.all` doesn't add threads.

## 119: Is Promise.resolve().then() synchronous?

No. Even though the promise is already resolved, the `.then` callback is queued as a microtask and runs after the current synchronous code finishes.

```js
Promise.resolve().then(() => console.log("then"));
console.log("sync");
// sync
// then
```

Promise callbacks are always async. This makes their behavior predictable.

## 120: What is the general order of sync code, nextTick, promises, timers and setImmediate?

In a CommonJS script, the usual order is:

1. Synchronous code
2. `process.nextTick` callbacks
3. Promise callbacks and `queueMicrotask`
4. Then the event loop phases: timers (`setTimeout`, `setInterval`), I/O callbacks (poll), `setImmediate` (check), close callbacks

After each callback in step 4, steps 2 and 3 run again. Remember that the order between a `setTimeout(fn, 0)` and a `setImmediate` in the main script isn't fixed.

## 121: Do timers with the same delay run in the order they were created?

Yes. Timers with the same delay are kept in a list in creation order, so they fire in that order.

```js
setTimeout(() => console.log("first"), 10);
setTimeout(() => console.log("second"), 10);
// first
// second
```

## 122: What happens with two timers that have different delays?

The one that becomes due first runs first, no matter which was created first:

```js
setTimeout(() => console.log("200"), 200);
setTimeout(() => console.log("100"), 100);
// 100
// 200
```

If the loop was blocked long enough that both are already due, Node still runs them in order of their due time.

## 123: What is setInterval drift?

Drift means the callbacks slowly get out of step with the "ideal" schedule. Each run can be a bit late because of other work on the main thread, and Node schedules the next run based on when the current one ran, not the original start time. Over many runs, `setInterval(fn, 1000)` won't fire exactly at 1 s, 2 s, 3 s.

If you need timing tied to the wall clock, compute the next delay from `Date.now()` each time.

## 124: How do you repeat a task without runs overlapping?

Use a chained `setTimeout` (or a loop with `await`) instead of `setInterval`, so the next run is scheduled only after the current one finishes:

```js
const { setTimeout: sleep } = require("node:timers/promises");

async function poll() {
  while (true) {
    await checkQueue(); // may take a variable time
    await sleep(5000); // then wait 5 seconds
  }
}
poll();
```

With `setInterval` and an async callback, a slow run can overlap with the next one.

## 125: What happens if a setInterval callback takes longer than the interval?

If the callback is synchronous, it blocks the loop, so the next run can't start until it's done. Node doesn't queue up "missed" runs; it just runs the next one when it can.

If the callback is `async` and awaits I/O, the sync part finishes quickly, and the next run can start while the previous one is still waiting. That can cause overlapping work, which is a common bug.

## 126: How do you stop an interval from inside its callback?

Keep the returned object and call `clearInterval` on it, or use `this` in a normal function (it's the `Timeout` object in Node):

```js
let n = 0;
const id = setInterval(() => {
  n++;
  if (n === 5) clearInterval(id);
}, 100);
```

## 127: How do you cancel a promise-based timer?

Pass an `AbortSignal`. When it's aborted, the promise rejects with an `AbortError` and the timer is cleared.

```js
const { setTimeout: sleep } = require("node:timers/promises");

const ac = new AbortController();
sleep(10000, null, { signal: ac.signal }).catch((err) => {
  console.log(err.name); // "AbortError"
});

ac.abort();
```

## 128: What is AbortSignal.timeout()?

`AbortSignal.timeout(ms)` creates a signal that aborts itself after `ms` milliseconds. It's a simple way to put a time limit on APIs that accept a signal:

```js
const res = await fetch("https://example.com/api", {
  signal: AbortSignal.timeout(3000),
});
```

The timer behind it is unref'd, so it doesn't keep the process alive on its own.

## 129: Does console.log block the event loop?

It can. Depending on where output goes, writes to stdout and stderr can be synchronous. For example, writing to a file is synchronous, and on Linux so is writing to a terminal. For a few log lines that doesn't matter, but logging a lot (or logging huge objects) in a hot path can slow down the whole server.

For production, use a fast logger (like pino) that writes asynchronously or in a separate thread.

## 130: Is JSON.parse blocking?

Yes. `JSON.parse` and `JSON.stringify` are synchronous and run on the main thread. For small payloads they're fast. For payloads of many megabytes they can take tens or hundreds of milliseconds, and the event loop is blocked for that time.

## 131: Can regular expressions block the event loop?

Yes. Regex matching is synchronous. Some patterns, like `/(a+)+$/`, can take exponential time on certain inputs. An attacker can send such input and freeze your server. This is called ReDoS (regular expression denial of service).

Avoid nested quantifiers on user input, limit input length, and test risky patterns.

## 132: Is crypto.createHash blocking?

Yes. `createHash().update().digest()` runs synchronously on the main thread. For small inputs it's very fast and fine. For hashing big files, use streams so the work is done in chunks as data arrives, or move it to a worker thread.

## 133: Is crypto.pbkdf2 blocking?

The callback version `crypto.pbkdf2()` is not. It runs on the libuv thread pool and calls your callback when done. `crypto.pbkdf2Sync()` is blocking and runs on the main thread. The same goes for `scrypt` and `scryptSync`. In a server, always use the async versions for password hashing.

## 134: Is require() blocking?

Yes. `require()` reads and runs the module file synchronously. That's normally fine because it happens at startup. Calling `require()` for the first time inside a request handler blocks the loop while the file is loaded (later calls use the cache and are cheap).

## 135: Is import() blocking?

Dynamic `import()` returns a promise, and loading happens asynchronously, so it doesn't block like a first-time `require()`. The module's top-level code still runs synchronously on the main thread when it's evaluated, so a module with heavy top-level work will still take main-thread time.

## 136: What is top-level await and how does it relate to the event loop?

In ES modules you can use `await` at the top level, outside any function:

```js
// config.mjs
const res = await fetch("https://example.com/config.json");
export const config = await res.json();
```

While it waits, the event loop keeps running. Modules that import this one wait until it's done. If the awaited promise never settles and nothing keeps the loop alive, Node exits with code 13.

## 137: How are streams related to the event loop?

Streams process data in chunks. Each chunk arrives through an I/O callback from the event loop, and events like `"data"`, `"end"` and `"drain"` are emitted from there. Because work is done chunk by chunk, the main thread never has to handle the whole data at once, and other callbacks can run between chunks.

## 138: When does the data event of a readable stream fire?

It fires each time a chunk of data is available and the stream is in flowing mode (for example, after you add a `"data"` listener or call `pipe`). For sockets and files, chunks come from I/O callbacks in the poll phase. Each `"data"` call is one callback on the main thread, followed by draining the microtask queues.

## 139: What is backpressure?

Backpressure is when a writable side can't keep up with the readable side. In Node, `writable.write()` returns `false` when its internal buffer is full. You should stop writing and wait for the `"drain"` event before continuing. `pipe()` and `stream.pipeline()` handle this for you.

Ignoring backpressure doesn't block the loop, but it can fill memory with buffered data.

## 140: What does "run to completion" mean?

It means once a JavaScript callback starts, it runs until it returns. Nothing else can interrupt it in the middle: no other callback, no timer, no I/O handler. Only after it returns can the next callback run.

This makes code easier to reason about (no data races inside a single function), but it also means a long function blocks everything.

## 141: Can one callback be interrupted by another callback?

No. On the main thread, callbacks never interrupt each other. A callback can only pause itself with `await` (in an async function), which ends the current synchronous part. Then other callbacks may run before it continues.

## 142: Do you need locks in Node.js?

For plain synchronous code on the main thread, no. Two callbacks can't touch the same variable at the same moment.

But you can still have race conditions across `await` points, because other code can run while you wait. Also, if you share memory between worker threads with `SharedArrayBuffer`, you need `Atomics` to coordinate.

## 143: What is a race condition in async Node.js code?

It's a bug where the result depends on the order in which async operations finish. Example:

```js
let balance = 100;

async function withdraw(amount) {
  const current = balance; // read
  await saveLog(amount); // other code may run here
  balance = current - amount; // write based on old value
}

withdraw(30);
withdraw(50);
// balance may end up 70 or 50 instead of 20
```

Both calls read 100 before either writes. Fix it by doing the read and write without an `await` between them, or by queuing the operations.

## 144: What is event-driven architecture in Node.js?

It means your code mostly reacts to events instead of running in a straight line: a request arrived, a file finished reading, a timer fired, a message came from a queue. You register handlers, and the event loop calls them when things happen. Node's core (servers, sockets, streams, `EventEmitter`) is built this way.

## 145: What is the reactor pattern?

The reactor pattern is the design behind the Node event loop. One thread waits for events from many sources (using something like epoll), and when an event happens, it calls the handler registered for it. Handlers should be short and not block, so the reactor can go back to waiting quickly.

## 146: What is the difference between the event loop and EventEmitter?

- The **event loop** is the system that schedules and runs callbacks from timers, I/O and other sources.
- **EventEmitter** is a simple class for publishing and subscribing to named events. Its `emit()` is synchronous and doesn't involve the loop at all.

They're often confused because both have "event" in the name. Many emitters emit events from inside event loop callbacks, which is where they connect.

## 147: Is the event loop part of the JavaScript language?

No. The ECMAScript spec defines promises and jobs (microtasks), but not timers, I/O or an event loop. The event loop is provided by the host environment: browsers implement it based on the HTML spec, and Node implements it with libuv. That's why the two loops differ in details.

## 148: How do you check which libuv and V8 versions your Node uses?

Use `process.versions`:

```js
console.log(process.versions.node); // e.g. "24.x.x"
console.log(process.versions.uv); // libuv version
console.log(process.versions.v8); // V8 version
```

This matters because some event loop details changed with libuv versions, for example how timers run since libuv 1.45 (Node 20).

## 149: Does using async functions make code faster?

Not by itself. `async` doesn't move work off the main thread. If an `async` function does heavy synchronous work, it blocks the loop just like a normal function. `async`/`await` only helps when you're waiting on something truly async, like I/O, so other work can run while you wait. Adding `async` everywhere also adds a little overhead from extra promises.

## 150: What are common misconceptions about the Node.js event loop?

- "Node is single-threaded." Only your JavaScript is. libuv and V8 use more threads.
- "async functions run in the background." They run on the main thread; only the I/O they wait on is in the background.
- "process.nextTick runs on the next loop iteration." It runs right after the current operation.
- "setTimeout(fn, 0) runs immediately." It runs after at least 1 ms, in the timers phase.
- "Everything async uses the thread pool." Network I/O doesn't; it uses OS event mechanisms.
- "Promise.all runs things in parallel threads." It only waits on promises that are already running.

# Moderate Questions (151-300)

## 151: Can you walk through one full iteration of the event loop?

1. **Timers**: run all `setTimeout`/`setInterval` callbacks that are due. After each one, drain the `nextTick` queue and the microtask queue.
2. **Pending callbacks**: run I/O callbacks deferred from the last iteration.
3. **Idle/prepare**: internal work.
4. **Poll**: compute how long to wait, wait for I/O events, and run their callbacks (socket data, finished file reads, new connections). After each callback, drain `nextTick` and microtasks.
5. **Check**: run the `setImmediate` callbacks queued before this phase started, draining the queues after each.
6. **Close**: run close callbacks.
7. If any ref'd handles or requests are still active, start the next iteration. Otherwise, emit `beforeExit` and exit if nothing new was scheduled.

## 152: How exactly does Node process the nextTick and microtask queues?

After each callback that Node calls from C++ into JavaScript (a timer, an I/O callback, an immediate), Node runs a function that:

1. Runs every callback in the `nextTick` queue, including ones added while running.
2. Asks V8 to run all microtasks (promise reactions, `queueMicrotask`), including ones added while running.
3. If step 2 added new `nextTick` callbacks, goes back to step 1.

So the two queues are fully drained, with `nextTick` getting priority each round, before the loop moves on to the next callback.

## 153: What changed in Node 11 regarding timers and microtasks?

Before Node 11, Node ran all due timers in the timers phase first and only then drained `nextTick` and microtasks. Since Node 11, the queues are drained after each individual timer (and each `setImmediate`) callback, which matches browser behavior.

```js
setTimeout(() => {
  console.log("t1");
  Promise.resolve().then(() => console.log("p1"));
}, 0);
setTimeout(() => console.log("t2"), 0);

// Node 11+: t1, p1, t2
// Node 10 and older: t1, t2, p1
```

## 154: What changed in libuv 1.45 (Node 20) regarding timers?

Before libuv 1.45, timers were run at the start of each loop iteration, before polling. Starting with libuv 1.45.0 (Node 20), timers are run after the poll phase (after check and close) in each iteration. To stay backward compatible, libuv still runs timers once before entering the loop.

In practice, the order of phases you see from JavaScript is the same cycle (timers, poll, check, close, timers, ...), but some edge cases around when timers fire relative to `setImmediate` can differ from older Node versions. Don't write code that depends on those edge cases.

## 155: What is the output order of timers, immediates, promises and nextTick inside an I/O callback?

```js
const fs = require("node:fs");

fs.readFile(__filename, () => {
  setTimeout(() => console.log("timeout"), 0);
  setImmediate(() => console.log("immediate"));
  Promise.resolve().then(() => console.log("promise"));
  process.nextTick(() => console.log("nextTick"));
  console.log("sync");
});
```

```
sync
nextTick
promise
immediate
timeout
```

The callback runs in the poll phase. After its sync code, the `nextTick` queue runs, then the promise. Then the loop goes to the check phase (`immediate`), and the timer only runs in the next timers phase.

## 156: What is the output when process.nextTick is called inside a promise callback?

```js
Promise.resolve()
  .then(() => {
    console.log("p1");
    process.nextTick(() => console.log("tick"));
  })
  .then(() => console.log("p2"));

Promise.resolve().then(() => console.log("p3"));
```

```
p1
p3
p2
tick
```

Once Node starts draining microtasks, V8 runs all of them, including new ones (`p2` is queued when `p1` finishes, after `p3`). The `nextTick` added from inside a microtask has to wait until the microtask queue is empty.

## 157: What is the output when promises and nested nextTick calls are queued from a nextTick callback?

```js
process.nextTick(() => {
  console.log("t1");
  Promise.resolve().then(() => console.log("promise"));
  process.nextTick(() => console.log("t3"));
});
process.nextTick(() => console.log("t2"));
```

```
t1
t2
t3
promise
```

The whole `nextTick` queue is drained first, including `t3`, which was added while draining. Only then does Node run the microtask queue.

## 158: What is the output order of an async function with await, nextTick and a promise?

```js
async function task() {
  console.log("a1");
  await null;
  console.log("a2");
}

console.log("start");
task();
process.nextTick(() => console.log("tick"));
Promise.resolve().then(() => console.log("p"));
console.log("end");
```

```
start
a1
end
tick
a2
p
```

`a1` runs synchronously when `task()` is called. The rest of `task` is queued as a microtask at the `await`, before `p` is queued. `tick` runs before all microtasks.

## 159: What is the output when setTimeout and setImmediate are scheduled inside a timer callback?

```js
setTimeout(() => {
  console.log("timeout 1");
  setTimeout(() => console.log("timeout 2"), 0);
  setImmediate(() => console.log("immediate"));
}, 0);
```

```
timeout 1
immediate
timeout 2
```

`timeout 1` runs in the timers phase. The loop then goes through poll to check, so `immediate` runs before the loop gets back to timers for `timeout 2`. This order is reliable.

## 160: What is the output when setTimeout and setImmediate are scheduled inside a setImmediate callback?

```js
setImmediate(() => {
  console.log("immediate 1");
  setTimeout(() => console.log("timeout"), 0);
  setImmediate(() => console.log("immediate 2"));
});
```

`immediate 1` always comes first. The order of `timeout` and `immediate 2` is not guaranteed. After the check phase, the loop runs close callbacks and then timers. If at least 1 ms has passed by then, `timeout` runs first; otherwise the timer isn't due yet and `immediate 2` runs first in the next check phase. A good answer explains why it's not fixed.

## 161: What is the output when two timers are due and the first one queues nextTick and a promise?

```js
setTimeout(() => {
  console.log("t1");
  process.nextTick(() => console.log("tick"));
  Promise.resolve().then(() => console.log("promise"));
}, 0);

setTimeout(() => console.log("t2"), 0);
```

On Node 11 and later:

```
t1
tick
promise
t2
```

The `nextTick` and microtask queues are drained after each timer callback, before the next timer.

## 162: What is the output when setImmediate is called inside another setImmediate callback?

```js
setImmediate(() => {
  console.log("i1");
  setImmediate(() => console.log("i3"));
});
setImmediate(() => console.log("i2"));
```

```
i1
i2
i3
```

The check phase only runs the immediates that were queued before it started (`i1` and `i2`). `i3` was added during the phase, so it runs in the next iteration.

## 163: Why does nextTick run before promises in CommonJS but not in ES modules?

In a CommonJS script, your main code runs as a normal synchronous call. When it finishes, Node drains the `nextTick` queue first, then microtasks.

In an ES module, Node loads and evaluates the module through promises. Your top-level code runs while V8 is already processing a promise job, so any promise callbacks you queue run in the same microtask drain, before Node gets the chance to process the `nextTick` queue.

```js
// main.mjs
process.nextTick(() => console.log("nextTick"));
Promise.resolve().then(() => console.log("promise"));
// promise
// nextTick
```

This is one reason the Node docs suggest `queueMicrotask` over `process.nextTick` for most code.

## 164: How many microtask ticks does await take?

Since V8 7.2 (Node 12), `await` on a native promise takes one microtask tick to resume. `await` on a plain value (like `await 5`) also takes one tick. `await` on a non-native thenable takes more, because V8 has to call its `then` method in a separate job.

Older Node versions used three ticks for `await`, so very old blog posts may show different output for ordering puzzles.

## 165: Does return await change timing compared to return?

Inside an `async` function, `return promise` and `return await promise` resolve the outer promise at slightly different microtask ticks. Returning a promise makes the outer promise adopt it, which costs a couple of extra ticks, while `return await` resolves with the plain value.

The timing difference only matters in ordering puzzles. The real-world difference is error handling and stack traces: with `return await` inside a `try/catch`, the rejection is caught in that function, and the function shows up in the async stack trace.

```js
async function load() {
  try {
    return await fetchData(); // errors are caught below
  } catch (err) {
    return fallback();
  }
}
```

## 166: When should you use process.nextTick?

Use it when you need a callback to run after the current function returns, but before any I/O or timers, and you are writing low-level or library code. Common cases:

- Making a callback API always async, even when the result is available right away.
- Emitting an event after a constructor returns, so the caller has time to add listeners.
- Reporting errors asynchronously in the same order as success cases.

For normal application code, `queueMicrotask` or `setImmediate` is usually a better choice.

## 167: When should you use queueMicrotask instead of process.nextTick?

Use `queueMicrotask` when you want "run this right after the current code" behavior and:

- You want the same code to work in browsers and Node.
- You want ordering consistent with promise callbacks.
- You don't need `nextTick`'s higher priority.

The Node docs recommend `queueMicrotask` for most user code. Both can starve the loop if used recursively.

## 168: When should you use setImmediate?

Use `setImmediate` when you want to run something after the current I/O callbacks, giving the event loop a chance to handle other events first. Typical uses:

- Splitting a long CPU task into chunks so other requests can be served in between.
- Deferring non-urgent work until after the current batch of I/O.
- Breaking recursion that would otherwise starve the loop.

```js
const { setImmediate: yieldLoop } = require("node:timers/promises");

async function processAll(items) {
  for (let i = 0; i < items.length; i++) {
    handle(items[i]);
    if (i % 1000 === 0) await yieldLoop();
  }
}
```

## 169: How do you make an API always async?

If a callback API sometimes calls the callback synchronously and sometimes later, callers get unpredictable behavior. This is sometimes called "releasing Zalgo". Fix it by always deferring the callback:

```js
const cache = new Map();

function getUser(id, cb) {
  if (cache.has(id)) {
    process.nextTick(cb, null, cache.get(id)); // async, even on cache hit
    return;
  }
  db.findUser(id, (err, user) => {
    if (!err) cache.set(id, user);
    cb(err, user);
  });
}
```

With promises this problem goes away, since `.then` callbacks are always async.

## 170: Why do some constructors emit events with process.nextTick?

Because if a constructor emits an event synchronously, nobody can have attached a listener yet:

```js
const { EventEmitter } = require("node:events");

class Job extends EventEmitter {
  constructor() {
    super();
    process.nextTick(() => this.emit("ready"));
  }
}

const job = new Job();
job.on("ready", () => console.log("ready")); // works
```

Without `nextTick`, the `"ready"` event would fire before `job.on` is called, and it would be missed.

## 171: Why is the listening event safe to attach after calling server.listen()?

When you call `server.listen(port)`, the `"listening"` event is emitted asynchronously (Node queues it with `process.nextTick`). So code like this works even though the listener is added after `listen`:

```js
const server = http.createServer(handler);
server.listen(3000);
server.on("listening", () => console.log("listening"));
```

This is a classic example the Node docs use to explain `process.nextTick`.

## 172: How do you split a long CPU task into chunks?

Process a part of the work, then yield to the event loop with `setImmediate` before continuing:

```js
function sumLargeArray(arr, done) {
  let i = 0;
  let total = 0;

  function chunk() {
    const end = Math.min(i + 10000, arr.length);
    for (; i < end; i++) total += arr[i];

    if (i < arr.length) setImmediate(chunk);
    else done(total);
  }

  chunk();
}
```

Between chunks, the loop can handle other requests and timers. The total time is a bit longer, but nobody waits seconds for a response.

## 173: Why use setImmediate instead of process.nextTick for chunking work?

Because `nextTick` callbacks run before the loop continues. If you chunk with `nextTick`, all chunks still run back to back without letting I/O in, so the loop is just as blocked as before. `setImmediate` puts each chunk on the next loop iteration, so the poll phase runs in between. Using a promise (`await Promise.resolve()`) has the same problem as `nextTick`.

## 174: How do you move CPU work to a worker thread?

Put the heavy work in a separate file and run it in a `Worker`. Wrap it in a promise so it's easy to use:

```js
// hash-worker.js
const { parentPort, workerData } = require("node:worker_threads");
const crypto = require("node:crypto");

let hash = workerData.input;
for (let i = 0; i < 1_000_000; i++) {
  hash = crypto.createHash("sha256").update(hash).digest("hex");
}
parentPort.postMessage(hash);
```

```js
// main.js
const { Worker } = require("node:worker_threads");

function runHash(input) {
  return new Promise((resolve, reject) => {
    const worker = new Worker("./hash-worker.js", { workerData: { input } });
    worker.once("message", resolve);
    worker.once("error", reject);
  });
}
```

The main event loop stays free while the worker computes.

## 175: How do you pass data between the main thread and a worker?

- `workerData` passes initial data when the worker is created.
- `worker.postMessage()` and `parentPort.postMessage()` send messages both ways.
- `MessageChannel` creates extra channels.
- `SharedArrayBuffer` lets both sides share the same memory.

Messages are copied with the structured clone algorithm. Messages arrive as events on the receiving thread's event loop.

## 176: What does it cost to send data to a worker?

By default, `postMessage` copies data using structured clone. For large objects, copying takes time on both threads and can block each side for a while. Options to reduce the cost:

- Transfer `ArrayBuffer`s instead of copying them, by passing them in the transfer list. The sender loses access to them.
- Use `SharedArrayBuffer` for data both sides read.
- Send only the data the worker really needs.

```js
const buf = new ArrayBuffer(10 * 1024 * 1024);
worker.postMessage(buf, [buf]); // moved, not copied
```

## 177: What is a worker pool and why use one?

Starting a worker thread takes time and memory (a new V8 instance). If you create one per request, you waste a lot. A worker pool starts a fixed number of workers once and sends tasks to whichever is free, queueing tasks when all are busy.

Libraries like `piscina` do this for you:

```js
const Piscina = require("piscina");
const pool = new Piscina({ filename: require.resolve("./task.js") });

const result = await pool.run({ n: 42 });
```

## 178: How do you change UV_THREADPOOL_SIZE?

Set the environment variable before the process starts:

```bash
UV_THREADPOOL_SIZE=16 node server.js
```

The pool is created the first time something uses it, and its size can't change after that. Setting `process.env.UV_THREADPOOL_SIZE` at the very top of your entry file can work on some platforms, but it's fragile, so setting it outside the process is the safe choice. The maximum is 1024.

## 179: When should you increase the thread pool size?

When your app does a lot of thread pool work at the same time and requests queue up behind each other, for example:

- Many parallel file reads or writes
- Many `dns.lookup` calls (for example, lots of outgoing HTTP requests to different hosts)
- Heavy use of async `crypto` (`pbkdf2`, `scrypt`) or `zlib`

Measure first. If the work is CPU-heavy (crypto, compression), more threads than CPU cores won't help much. For slow I/O like a network file system, more threads can help a lot.

## 180: What happens when all thread pool threads are busy?

New tasks wait in a queue until a thread is free. Your JavaScript isn't blocked, but those operations take longer. For example, with the default 4 threads, a fifth `fs.readFile` waits until one of the first four finishes. This waiting doesn't show up as event loop delay, which makes it easy to miss.

## 181: Why can slow crypto calls slow down file operations?

Because they share the same thread pool. If four `crypto.pbkdf2` calls take 100 ms each, all four default threads are busy for 100 ms, and every `fs` call and `dns.lookup` in the meantime has to wait in the queue. A login spike can make unrelated file reads slow.

Fixes: increase `UV_THREADPOOL_SIZE`, move password hashing to worker threads or a separate service, or limit how many hashes run at once.

## 182: What is the difference between dns.lookup and dns.resolve in terms of the event loop?

- `dns.lookup` uses the OS resolver (`getaddrinfo`), which is a blocking call, so libuv runs it on the thread pool. It follows `/etc/hosts` and system settings. Most networking APIs (`http.get`, `net.connect`, `fetch`) use it by default.
- `dns.resolve*` functions use the c-ares library, which sends DNS queries over the network without the thread pool. They ignore `/etc/hosts`.

If an app makes many outgoing connections to different hostnames, `dns.lookup` calls can fill the thread pool. Caching DNS results or using a custom `lookup` function helps.

## 183: How does fs.promises use the thread pool?

The same way as the callback API: each operation (open, read, write, stat) is a request sent to the thread pool. Note that `fs.promises.readFile` on a big file can make several thread pool requests (open, stat or reads in chunks, close), and each one goes through the queue. So many concurrent `readFile` calls on large files compete for the 4 default threads.

## 184: Why don't many parallel file reads get faster after a point?

Because file operations go through the thread pool, which has 4 threads by default. Starting 1,000 reads at once doesn't make 1,000 reads happen at once. Only 4 run, and the rest wait in the queue. The disk itself also has limits. Past a point, more concurrency only adds memory use and queueing. A bounded concurrency of a few dozen is usually as fast as unbounded.

## 185: How do you limit concurrency of async operations?

Run only N operations at a time. You can use a library like `p-limit`, or a small helper:

```js
async function mapLimit(items, limit, fn) {
  const results = new Array(items.length);
  let next = 0;

  async function runner() {
    while (next < items.length) {
      const i = next++;
      results[i] = await fn(items[i]);
    }
  }

  await Promise.all(Array.from({ length: limit }, runner));
  return results;
}

await mapLimit(files, 10, (f) => fs.promises.readFile(f));
```

This avoids flooding the thread pool, the database or a remote API.

## 186: What is monitorEventLoopDelay?

`monitorEventLoopDelay()` from `node:perf_hooks` samples event loop delay using a timer inside libuv and stores the results in a histogram. It's cheap enough to run in production.

```js
const { monitorEventLoopDelay } = require("node:perf_hooks");

const h = monitorEventLoopDelay({ resolution: 20 });
h.enable();

setInterval(() => {
  console.log({
    p50: h.percentile(50) / 1e6, // ms
    p99: h.percentile(99) / 1e6,
    max: h.max / 1e6,
  });
  h.reset();
}, 10000).unref();
```

Values are in nanoseconds.

## 187: What is event loop utilization (ELU)?

ELU is the share of time the event loop is busy running code, compared to time it spends idle waiting in the poll phase. It's a number from 0 to 1.

```js
const { performance } = require("node:perf_hooks");

let last = performance.eventLoopUtilization();
setInterval(() => {
  const elu = performance.eventLoopUtilization(last);
  console.log("ELU", elu.utilization.toFixed(2));
  last = performance.eventLoopUtilization();
}, 5000).unref();
```

An ELU close to 1 means the loop has no spare time, and latency will grow as load increases.

## 188: How do you measure event loop utilization of a worker thread?

From the main thread, use `worker.performance.eventLoopUtilization()`. Inside the worker, `performance.eventLoopUtilization()` works the same as on the main thread.

```js
const { Worker } = require("node:worker_threads");
const worker = new Worker("./task.js");

setInterval(() => {
  console.log(worker.performance.eventLoopUtilization());
}, 1000).unref();
```

This is useful for checking whether a worker pool is overloaded.

## 189: What does the --trace-sync-io flag do?

It prints a warning with a stack trace whenever synchronous I/O (like `fs.readFileSync`) is used after the first turn of the event loop, that is, after startup.

```bash
node --trace-sync-io server.js
```

It's a quick way to find sync calls hidden in request handlers or in dependencies. Sync I/O during startup is not reported.

## 190: How do you find what is blocking the event loop?

Common steps:

1. Confirm the problem with an event loop delay metric (`monitorEventLoopDelay` or ELU).
2. Take a CPU profile while the problem happens: `node --cpu-prof`, Chrome DevTools via `--inspect`, or the `inspector` module in production.
3. Look at the flame graph for wide, long frames on the main thread: JSON work, regexes, sorting, sync crypto, template rendering.
4. Use `--trace-sync-io` to catch sync I/O.
5. Check GC activity if there are no obvious hot functions.

## 191: How do you use --cpu-prof?

Start Node with the flag. When the process exits, it writes a `.cpuprofile` file you can open in Chrome DevTools (Performance tab) or other viewers.

```bash
node --cpu-prof --cpu-prof-dir=./profiles server.js
```

Run your load test, then stop the process normally (for example with Ctrl+C if you handle `SIGINT` and exit cleanly). Look for functions that take a long time on the main thread.

## 192: What is process.getActiveResourcesInfo()?

It returns a list of strings describing the resources currently keeping the event loop alive, such as `"Timeout"`, `"TCPServerWrap"`, `"TCPSocketWrap"` or `"FSReqCallback"`.

```js
setTimeout(() => {}, 1000);
console.log(process.getActiveResourcesInfo());
// [ 'TTYWrap', 'Timeout' ] (depends on the environment)
```

It's handy for debugging why a process doesn't exit.

## 193: Why does a Node.js process not exit, and how do you debug it?

Something is still keeping the event loop alive: an open server, a database connection pool, a socket with keep-alive, an interval, a file watcher, or a worker. To find it:

- Print `process.getActiveResourcesInfo()` at the point you expect the process to end.
- In tests, use your test runner's open handle detection (for example `jest --detectOpenHandles`).
- Make sure you call `close()` / `end()` / `disconnect()` on servers, DB clients and Redis clients.
- `unref()` background timers that shouldn't keep the process alive.

## 194: Why do tests hang after finishing, and how do you fix it?

Usually because a test opened something that keeps the event loop alive: a server that wasn't closed, a DB connection, an interval, or an HTTP keep-alive socket. The test runner waits for the process to end, and it never does.

Fix it by cleaning up in `afterAll`/`after` hooks:

```js
after(async () => {
  await new Promise((resolve) => server.close(resolve));
  await db.end();
});
```

Forcing exit (like `jest --forceExit`) hides the problem instead of fixing it.

## 195: How do unref'd timers help with background tasks?

An app often has timers that should run while the app is alive but shouldn't keep it alive on their own: metrics reporters, cache cleanup, heartbeat logs. If they are ref'd, the process never exits cleanly, and tests or scripts hang.

```js
const cleanup = setInterval(() => cache.prune(), 60_000);
cleanup.unref();
```

Now the process exits as soon as the real work (like the server) is done.

## 196: How do you add a timeout to a promise?

Use `Promise.race` with a timer, and clear the timer afterwards:

```js
const { setTimeout: sleep } = require("node:timers/promises");

async function withTimeout(promise, ms) {
  const ac = new AbortController();
  const timeout = sleep(ms, null, { signal: ac.signal }).then(() => {
    throw new Error(`Timed out after ${ms} ms`);
  });
  try {
    return await Promise.race([promise, timeout]);
  } finally {
    ac.abort(); // stop the timer so it doesn't keep the process alive
  }
}
```

Aborting the timer in `finally` makes its promise reject, but `Promise.race` already attached a handler to it, so this is not an unhandled rejection. Note that this only stops waiting; the original operation keeps running unless it supports an `AbortSignal` itself.

## 197: How does setTimeout from timers/promises support cancellation?

It takes an options object with `signal` and `ref`:

```js
const { setTimeout } = require("node:timers/promises");

const ac = new AbortController();
const p = setTimeout(5000, "value", { signal: ac.signal, ref: false });

ac.abort(); // p rejects with an AbortError
```

`ref: false` makes the timer not keep the process alive, like `unref()`.

## 198: How does setInterval from timers/promises work?

It returns an async iterator that yields every `delay` milliseconds:

```js
const { setInterval } = require("node:timers/promises");

async function heartbeat(signal) {
  for await (const startTime of setInterval(1000, Date.now(), { signal })) {
    console.log("alive", Date.now() - startTime);
  }
}
```

Breaking out of the loop or aborting the signal stops the interval.

## 199: What are scheduler.wait() and scheduler.yield()?

They are in `node:timers/promises` and match an API proposed for browsers:

- `scheduler.wait(delay, { signal })` is like the promise-based `setTimeout`.
- `scheduler.yield()` returns a promise that resolves on a later turn of the event loop, giving other work a chance to run. In Node it behaves like `await setImmediate()`.

Both are still marked experimental in the Node docs, so check the stability status before relying on them.

## 200: How do you avoid leaking timers?

- Always keep the timer object if you may need to clear it, and clear it when the related work ends (request finished, socket closed, component disposed).
- Prefer `timeout.refresh()` over creating new timers for idle timeouts.
- Use `AbortSignal` with promise timers so you can cancel them.
- `unref()` background timers.
- Be careful with closures: a pending interval keeps everything it references alive in memory.

## 201: Can you use the using keyword with timers?

Yes, in Node versions with explicit resource management support (Node 24 and later). `Timeout` and `Immediate` objects have a `Symbol.dispose` method that clears them. With `using`, the timer is cleared automatically when the block ends:

```js
function waitForReply(socket) {
  using timer = setTimeout(() => socket.destroy(), 5000);
  // ... work that may return early or throw
} // timer is cleared here
```

## 202: How are Node.js timers different from browser timers?

- Node returns a `Timeout` object; browsers return a number.
- Node has `ref`, `unref`, `hasRef` and `refresh`.
- Node turns delays below 1 into 1 ms. Browsers clamp nested timers (5+ levels) to at least 4 ms and throttle timers in background tabs.
- `this` in a normal function callback is the `Timeout` object in Node, and `window` in browsers.
- Node has `setImmediate` and `timers/promises`.

## 203: Does Node.js clamp nested timers to 4 ms like browsers?

No. The 4 ms clamp for deeply nested timers is part of the HTML spec for browsers. Node doesn't do it. A chain of `setTimeout(fn, 0)` calls in Node runs each step about 1 ms apart (or as fast as the loop allows), not 4 ms apart.

## 204: Can an endless promise chain starve the event loop?

Yes. If a microtask keeps scheduling new microtasks, V8 keeps draining them and never returns to the event loop:

```js
function loop() {
  return Promise.resolve().then(loop);
}
loop();

setTimeout(() => console.log("never"), 0);
```

No timer, I/O or `setImmediate` callback will ever run. The same applies to a `while (true) { await somethingAlreadyResolved; }` loop.

## 205: Why doesn't await Promise.resolve() let I/O run?

Because the code after `await` continues as a microtask, and microtasks run before the event loop goes back to its phases. So `await Promise.resolve()` only lets other microtasks run, not I/O, timers or other requests.

To really yield to the event loop, wait on something that is scheduled in a phase:

```js
const { setImmediate: yieldToLoop } = require("node:timers/promises");
await yieldToLoop();
```

## 206: How does the drain event relate to the event loop?

When `writable.write()` returns `false`, the stream's buffer is over its `highWaterMark`. As the underlying resource (socket, file) accepts data through I/O callbacks, the buffer empties, and when it's empty enough the stream emits `"drain"`. You wait for it before writing more:

```js
const { once } = require("node:events");

async function writeMany(stream, lines) {
  for (const line of lines) {
    if (!stream.write(line)) {
      await once(stream, "drain");
    }
  }
}
```

This keeps memory use stable while still letting the loop do other work.

## 207: How do streams help avoid blocking with large files?

Instead of loading the whole file into memory and processing it in one go, a stream reads it in chunks (64 KB by default for file streams). Each chunk is handled in a separate callback. Between chunks, the loop can run other callbacks, so other requests aren't stuck for the whole file. Memory use stays small no matter how big the file is.

## 208: How does stream.pipeline help?

`pipeline` connects streams, handles backpressure between them, forwards errors, and destroys all streams if one fails. The promise version is easy to use with `await`:

```js
const { pipeline } = require("node:stream/promises");
const fs = require("node:fs");
const zlib = require("node:zlib");

await pipeline(
  fs.createReadStream("big.log"),
  zlib.createGzip(),
  fs.createWriteStream("big.log.gz"),
);
```

Here gzip work runs on the thread pool chunk by chunk, so the main thread stays responsive.

## 209: Why is reading a 1 GB file with readFile a problem?

- The whole file goes into memory as one buffer, which can hit memory limits (buffers also have a maximum size).
- Any processing afterwards (`toString`, `split`, `JSON.parse`) is one huge synchronous operation that blocks the loop.

Use streams or line-by-line reading instead, so both memory and main-thread time stay small per chunk.

## 210: How do you handle large JSON without blocking the loop?

Options:

- Avoid producing huge JSON responses in the first place (pagination, field selection).
- Use a streaming JSON parser or serializer that processes data in chunks.
- Use NDJSON (one JSON object per line) and parse line by line.
- Do the parse or stringify in a worker thread (note the cost of copying the result back).
- For responses, stream an array item by item instead of calling `JSON.stringify` on the whole thing.

## 211: What is ReDoS and how does it relate to the event loop?

ReDoS (regular expression denial of service) happens when a regex with heavy backtracking is run on a carefully chosen input, and matching takes seconds or longer. Since regex matching is synchronous on the main thread, one request can freeze the whole server.

```js
const re = /^(a+)+$/;
re.test("a".repeat(30) + "!"); // can take a very long time
```

## 212: How do you protect against ReDoS?

- Avoid nested quantifiers like `(a+)+` or `(.*)*` and overlapping alternatives.
- Limit input length before running the regex.
- Use tools that flag unsafe patterns (lint rules, `safe-regex` style checkers).
- Use a linear-time regex engine like RE2 (`re2` package) for user-supplied or complex patterns.
- Never run user-provided regexes on the main thread without limits.

## 213: Why can sorting a big array be a problem in a request handler?

`Array.prototype.sort` is synchronous. Sorting a few hundred items is instant, but sorting hundreds of thousands of objects with a custom compare function can take tens or hundreds of milliseconds. Doing that per request blocks every other request. Sort in the database, cache the sorted result, or limit the data size.

## 214: How do error handling styles differ between callbacks and promises?

- **Callbacks**: errors are passed as the first argument. If you forget to check it, the error is lost. If you throw inside the callback, it's an uncaught exception.
- **Promises**: errors become rejections. They flow down the chain to the next `.catch` or `try/catch` around `await`. If nobody handles them, Node treats it as an unhandled rejection and by default crashes.

## 215: How do you use the unhandledRejection event?

```js
process.on("unhandledRejection", (reason, promise) => {
  logger.error({ reason }, "unhandled rejection");
  process.exitCode = 1;
  // optionally start graceful shutdown here
});
```

Use it to log and alert, not to keep running as if nothing happened. Each unhandled rejection is a bug, usually a missing `await` or `.catch`.

## 216: What does the --unhandled-rejections flag do?

It controls what Node does with unhandled rejections. Main modes:

- `throw` (default since Node 15): emit `unhandledRejection`; if there's no listener, throw it as an uncaught exception.
- `strict`: always throw it as an uncaught exception.
- `warn`: only print a warning.
- `none`: do nothing.
- `warn-with-error-code`: warn and set the exit code to 1.

## 217: What is the uncaughtExceptionMonitor event?

`process.on("uncaughtExceptionMonitor", (err, origin) => {})` lets you observe uncaught exceptions (for logging or metrics) without changing Node's default behavior. Unlike `uncaughtException`, adding this listener doesn't stop the process from crashing.

## 218: Why should a process exit after an uncaught exception?

When an exception escapes, the code that threw it stopped halfway. Locks might not be released, connections might be half-used, and in-memory state might be inconsistent. Continuing to serve traffic on top of that can cause strange bugs or data corruption.

The safe pattern: log the error, stop accepting new work, try to finish in-flight work for a short time, then exit and let a process manager restart the app.

## 219: How do you implement graceful shutdown?

```js
const server = app.listen(3000);

function shutdown(signal) {
  console.log(`${signal} received, shutting down`);

  server.close(async () => {
    await db.close();
    process.exit(0);
  });

  // force exit if it takes too long
  setTimeout(() => process.exit(1), 10_000).unref();
}

process.on("SIGTERM", shutdown);
process.on("SIGINT", shutdown);
```

`server.close()` stops accepting new connections and calls its callback when existing ones are done. The unref'd timer is a safety net in case something hangs.

## 220: What do server.close(), closeIdleConnections() and closeAllConnections() do?

- `server.close()`: stops accepting new connections. The callback runs when all existing connections are closed. Since Node 19, it also closes idle keep-alive connections.
- `server.closeIdleConnections()`: closes connections that aren't currently handling a request.
- `server.closeAllConnections()`: closes all connections, including active ones. Use it as a last step when a timeout runs out.

Keep-alive sockets used to be a common reason why `server.close()` never finished.

## 221: How are signals like SIGTERM delivered to your code?

libuv catches the OS signal and turns it into an event on the event loop. Your `process.on("SIGTERM", ...)` handler then runs on the main thread like any other callback. This means a handler can't run while the loop is blocked: if the main thread is stuck in a long loop, the signal handler waits. Also, if you add a listener for `SIGTERM` or `SIGINT`, Node no longer exits on that signal by default; you have to do it yourself.

## 222: How do you make EventEmitter listeners run asynchronously?

`emit` is always synchronous, so if a listener should run later, schedule it inside the listener:

```js
emitter.on("order", (order) => {
  setImmediate(() => sendEmail(order));
});
```

Or emit asynchronously from the producer side with `process.nextTick`, `queueMicrotask` or `setImmediate`. Be careful: a slow synchronous listener blocks the code that called `emit` and the whole loop.

## 223: How do events.once and events.on work with the event loop?

They turn events into promises and async iterators:

```js
const { once, on } = require("node:events");

await once(server, "listening");

for await (const [msg] of on(socket, "message")) {
  console.log(msg);
}
```

`once` resolves on the first event (or rejects on `"error"`). `on` buffers events that arrive while your loop body is running, so you don't miss them. Both accept an `AbortSignal`.

## 224: What is captureRejections in EventEmitter?

If an event listener is an `async` function and it rejects, the rejection is normally unhandled. With `captureRejections: true`, the emitter catches it and emits it as an `"error"` event (or calls `Symbol.for("nodejs.rejection")` if defined).

```js
const { EventEmitter } = require("node:events");

const ee = new EventEmitter({ captureRejections: true });
ee.on("job", async () => {
  throw new Error("failed");
});
ee.on("error", (err) => console.error("caught", err.message));
ee.emit("job");
```

## 225: How does AbortController work with async APIs in Node?

`AbortController` gives you a `signal` you pass to async operations. Calling `abort()` triggers the signal, and APIs that support it stop their work and reject with an `AbortError`. Many core APIs accept it: `fetch`, `fs.promises.readFile`, `timers/promises`, `events.once`, `child_process.spawn`, `stream.pipeline`.

```js
const ac = new AbortController();
const p = fs.promises.readFile("big.bin", { signal: ac.signal });
ac.abort();
await p.catch((e) => console.log(e.name)); // AbortError
```

## 226: What is AsyncLocalStorage?

`AsyncLocalStorage` from `node:async_hooks` lets you store data that follows an async flow, like thread-local storage in other languages. A common use is a request ID that every log line in that request can read, without passing it through every function.

```js
const { AsyncLocalStorage } = require("node:async_hooks");
const als = new AsyncLocalStorage();

app.use((req, res, next) => {
  als.run({ requestId: crypto.randomUUID() }, next);
});

function log(msg) {
  const store = als.getStore();
  console.log(store?.requestId, msg);
}
```

It's stable and is the recommended API for this (instead of using `async_hooks` directly).

## 227: How does AsyncLocalStorage keep its value across await and callbacks?

When an async operation is created (a promise, a timer, an I/O request), Node remembers which context was active at that moment. When the callback for that operation runs later, Node restores that context before calling it. So `getStore()` returns the right value even after `await`, inside `setTimeout`, or in an I/O callback, even though many other requests ran on the same thread in between.

Since Node 24, this is implemented with `AsyncContextFrame` by default, which is faster than the older `async_hooks`-based approach.

## 228: What are async_hooks and why are they discouraged?

`async_hooks.createHook()` lets you register callbacks (`init`, `before`, `after`, `destroy`, `promiseResolve`) that fire for every async resource Node creates. It was used for tracing and context propagation.

The Node docs discourage it because it has a real performance cost (especially with promises), it exposes internal details that change between versions, and the API is still experimental. Use `AsyncLocalStorage` for context, and `diagnostics_channel` or tracing tools for observability.

## 229: What are executionAsyncId and triggerAsyncId?

They come from `node:async_hooks`:

- `executionAsyncId()` returns the ID of the async resource whose callback is running right now.
- `triggerAsyncId()` returns the ID of the resource that caused the current one to be created.

Together they let tools build a tree of "this callback was caused by that one". You rarely need them in application code.

## 230: What is AsyncResource used for?

`AsyncResource` lets you tell Node "this callback belongs to the async context where it was created", which is needed when you build your own queue or pool that calls callbacks later. Without it, `AsyncLocalStorage` may return the wrong store inside those callbacks.

```js
const { AsyncResource } = require("node:async_hooks");

class JobQueue {
  jobs = [];
  add(fn) {
    this.jobs.push(AsyncResource.bind(fn)); // keep the caller's context
  }
  runAll() {
    for (const job of this.jobs) job();
  }
}
```

## 231: How do async stack traces work in Node.js?

V8 can add frames from earlier `await` calls to an error's stack trace, so you see the chain of async functions that led to the error (marked with `at async`). This works for `async`/`await` chains with native promises and is on by default.

```
Error: not found
    at findUser (users.js:10:11)
    at async getProfile (profile.js:5:16)
    at async handler (routes.js:22:20)
```

It doesn't work as well across plain callbacks or `.then` chains, which is one more reason to prefer `await`.

## 232: Why are stack traces from callbacks often short?

Because each callback runs from the event loop with a fresh call stack. The function that started the operation already returned, so it's no longer on the stack. A stack trace from an `fs.readFile` callback, for example, often only shows the callback and some Node internals, not the code that called `readFile`.

## 233: How does the cluster module distribute connections?

The primary process accepts connections and passes them to workers. On most platforms the default is round-robin: the primary hands each new connection to the next worker in turn. On Windows the default is to let workers accept connections directly from a shared socket. Each worker has its own event loop, so a blocked worker only affects the connections it owns.

## 234: When should you use cluster and when worker threads?

- **Cluster (or multiple processes)**: to scale a web server across CPU cores. Each process handles its own requests. Good isolation; a crash in one doesn't kill the others.
- **Worker threads**: to move specific CPU-heavy tasks (hashing, image processing, parsing) off the main thread inside one process, with cheaper communication and shared memory.

Many apps use both: several processes for scaling, and a worker pool inside each one for heavy tasks. In containers, you often run one process per container and scale containers instead of using cluster.

## 235: How do you share memory between worker threads?

Use a `SharedArrayBuffer`. Both threads see the same memory, and you use `Atomics` to read and write safely:

```js
const { Worker } = require("node:worker_threads");

const shared = new SharedArrayBuffer(4);
const counter = new Int32Array(shared);

const worker = new Worker(
  `
  const { workerData } = require("node:worker_threads");
  const c = new Int32Array(workerData);
  for (let i = 0; i < 1000; i++) Atomics.add(c, 0, 1);
`,
  { eval: true, workerData: shared },
);

worker.on("exit", () => console.log(Atomics.load(counter, 0))); // 1000
```

## 236: Can you use Atomics.wait on the main thread in Node.js?

Yes. Browsers don't allow `Atomics.wait` on the main thread, but Node does. It blocks the thread completely until another thread notifies it or the timeout passes, so the event loop stops during that time.

```js
const sab = new SharedArrayBuffer(4);
const arr = new Int32Array(sab);
Atomics.wait(arr, 0, 0, 1000); // blocks the main thread for 1 second
```

It's sometimes used as a "sleep" in sync scripts, but never in a server. `Atomics.waitAsync` is the non-blocking version.

## 237: How are worker thread messages delivered?

`postMessage` puts the message in a queue for the receiving thread and wakes up that thread's event loop. The message is then delivered as a `"message"` event, like any other event loop callback, and the microtask queues are drained after it. So messages only arrive when the receiving thread's loop isn't busy. A blocked worker won't see messages until it's free.

## 238: What does worker.unref() do?

Like `unref()` on a timer, it means "don't keep the main process alive just because this worker is running". If the main thread has nothing else to do, the process can exit while the worker is still running. `worker.ref()` undoes it. The same goes for `MessagePort` objects, which also keep the loop alive while they have listeners.

## 239: What is the difference between exec and execSync for the event loop?

- `child_process.exec()` starts the command and returns right away. Output is collected through I/O events, and your callback runs when the process exits.
- `child_process.execSync()` blocks the main thread until the command finishes. Nothing else runs in the meantime.

`execSync` is fine in build scripts and CLIs, but in a server it freezes all requests for as long as the command runs.

## 240: How does spawn stream its output through the event loop?

`spawn` creates the child process and pipes for its stdin, stdout and stderr. libuv watches those pipes, and when the child writes data, the parent gets `"data"` events in the poll phase. The `"exit"` event arrives when the child ends.

```js
const { spawn } = require("node:child_process");

const ls = spawn("ls", ["-la"]);
ls.stdout.on("data", (chunk) => process.stdout.write(chunk));
ls.on("close", (code) => console.log("exit code", code));
```

Unlike `exec`, `spawn` doesn't buffer all output in memory, so it's better for long-running commands or large output.

## 241: What is the difference between the exit and close events of a child process?

- `"exit"` fires when the child process ends. Its stdio streams may still have unread data.
- `"close"` fires after the process has ended and all its stdio streams are closed.

If you need all the output, wait for `"close"`. Both events come from the event loop on the parent side.

## 242: How does an HTTP request flow through the event loop phases?

1. A new connection is accepted in the poll phase.
2. Data arrives on the socket (poll phase). Node's HTTP parser runs on the main thread and, once headers are parsed, calls your `"request"` handler.
3. Your handler starts async work, like a DB query, and returns.
4. The DB response arrives on its own socket (poll phase), and your callback or `await` continues.
5. `res.end()` writes data to the socket. The write completes later through another I/O event.

Between each of these steps, many other requests can be processed.

## 243: How does HTTP keep-alive affect the event loop?

Keep-alive keeps sockets open after a response so they can be reused. Open sockets are handles that keep the event loop alive.

- On the server: idle keep-alive connections stay open until `server.keepAliveTimeout` (5 seconds by default) or until closed during shutdown.
- On the client: since Node 19, the global HTTP agent uses keep-alive by default, so pooled sockets can stay open after your request.

Pooled client sockets are unref'd while idle, so they normally don't stop a script from exiting, but server-side keep-alive connections can delay `server.close()`.

## 244: Can fetch keep a Node.js process alive?

Pending `fetch` requests keep the process alive until they finish, like any network request. After the response, the connection is kept in undici's pool for reuse, but idle pooled connections don't prevent the process from exiting.

A common gotcha: if you don't read the response body, the connection stays busy until garbage collection, which can cause slow connection pool exhaustion. Always consume or cancel the body.

```js
const res = await fetch(url);
await res.body?.cancel(); // when you don't need the body
```

## 245: How does socket.setTimeout work?

`socket.setTimeout(ms)` starts an inactivity timer. If no data is sent or received for `ms` milliseconds, the socket emits `"timeout"`. It does not close the socket by itself; you have to do that:

```js
socket.setTimeout(30_000);
socket.on("timeout", () => {
  socket.destroy();
});
```

Internally it uses a Node timer that is refreshed on each read or write, so it's cheap even with many sockets.

## 246: What are the main HTTP server timeouts?

- `server.headersTimeout`: max time to receive the full request headers (60 seconds by default).
- `server.requestTimeout`: max time to receive the whole request (300 seconds by default since Node 18).
- `server.keepAliveTimeout`: how long an idle keep-alive connection is kept open (5 seconds).
- `server.timeout`: socket inactivity timeout (0, disabled, by default).

They're all implemented with timers on the event loop. They protect against slow clients holding connections forever.

## 247: How does fs.watch work with the event loop?

`fs.watch` uses OS notification APIs (inotify on Linux, FSEvents/kqueue on macOS, `ReadDirectoryChangesW` on Windows). libuv registers the watcher as a handle, and change events arrive in the poll phase without using the thread pool. An active watcher keeps the process alive until you call `watcher.close()`.

`fs.watchFile` works differently: it polls with `stat` on an interval, which is slower and uses more resources.

## 248: How does garbage collection affect the event loop?

V8 does most GC work on background threads, but some parts still pause the main thread. While the main thread is paused, no callbacks run, so GC pauses show up as event loop delay. Apps that create lots of short-lived objects (big JSON, many small allocations per request) trigger GC more often. A very full heap leads to longer, more frequent pauses and higher latency.

## 249: What V8 flags can help with GC-related latency?

- `--max-old-space-size=<MB>`: raise the old generation heap limit, so the app doesn't run out of memory or GC constantly near the limit. Set it with the container's memory limit in mind.
- `--max-semi-space-size=<MB>`: a bigger young generation means fewer scavenges for apps that allocate a lot of short-lived objects.

Change these only after measuring. Usually the best fix is to allocate less.

## 250: How do you detect long GC pauses?

Use a `PerformanceObserver` for `"gc"` entries:

```js
const { PerformanceObserver } = require("node:perf_hooks");

const obs = new PerformanceObserver((list) => {
  for (const entry of list.getEntries()) {
    if (entry.duration > 50) {
      console.warn(`GC took ${entry.duration.toFixed(1)} ms`, entry.detail);
    }
  }
});
obs.observe({ entryTypes: ["gc"] });
```

You can also run with `--trace-gc` while debugging to print every GC event.

## 251: How do you test timer-based code with node:test?

The built-in test runner has mock timers:

```js
const { test, mock } = require("node:test");
const assert = require("node:assert");

test("debounce calls once", () => {
  mock.timers.enable({ apis: ["setTimeout"] });
  const fn = mock.fn();
  const debounced = debounce(fn, 100);

  debounced();
  debounced();
  mock.timers.tick(100);

  assert.strictEqual(fn.mock.callCount(), 1);
  mock.timers.reset();
});
```

It can mock `setTimeout`, `setInterval`, `setImmediate` and `Date`. Time only moves when you call `tick()` or `runAll()`.

## 252: What should you know about fake timers in Jest and Vitest?

- `jest.useFakeTimers()` and `vi.useFakeTimers()` replace timer functions so time only moves when you advance it (`advanceTimersByTime`, `runAllTimers`).
- Jest's fake timers also fake `process.nextTick` and `queueMicrotask` by default. Vitest doesn't fake them by default. Both let you choose which APIs to fake.
- Promises are never faked, so code that mixes timers and `await` may need the async variants, like `await jest.advanceTimersByTimeAsync(1000)` or `await vi.advanceTimersByTimeAsync(1000)`, which let microtasks run between timers.
- Fake timers with real I/O (like a DB call) can make tests hang, because the I/O doesn't care about fake time.

## 253: What is a flushPromises helper and when do you need it?

It's a small helper used in tests to wait until pending promise callbacks have run:

```js
const flushPromises = () => new Promise((resolve) => setImmediate(resolve));

test("updates state after async call", async () => {
  startLoading(); // triggers promise chains
  await flushPromises();
  expect(state.loaded).toBe(true);
});
```

Because `setImmediate` runs in the check phase, all microtasks queued before it are already done. Note it won't wait for real I/O that hasn't completed yet.

## 254: How does util.promisify(setTimeout) work?

`setTimeout` has a special `util.promisify.custom` property, so `util.promisify(setTimeout)` returns a function where the first argument is the delay and the optional second argument is the value to resolve with:

```js
const util = require("node:util");
const sleep = util.promisify(setTimeout);

await sleep(500, "done"); // resolves with "done"
```

This is the same as `setTimeout` from `node:timers/promises`, which is the more common choice today.

## 255: How do you read a file line by line without blocking?

Use `readline` with a read stream and `for await`:

```js
const fs = require("node:fs");
const readline = require("node:readline");

async function countErrors(file) {
  const rl = readline.createInterface({
    input: fs.createReadStream(file),
    crlfDelay: Infinity,
  });

  let errors = 0;
  for await (const line of rl) {
    if (line.includes("ERROR")) errors++;
  }
  return errors;
}
```

The file is read in chunks, and other callbacks can run between chunks.

## 256: What is the difference between sequential and parallel await?

```js
// Sequential: total time = a + b
const user = await getUser(id);
const orders = await getOrders(id);

// Parallel: total time = max(a, b)
const [user2, orders2] = await Promise.all([getUser(id), getOrders(id)]);
```

Use sequential when the second call needs the result of the first. Use parallel when they are independent. Forgetting this is a common reason for slow endpoints.

## 257: Why doesn't forEach wait for async callbacks?

`forEach` calls the callback and ignores its return value, including the promise from an `async` function. So all callbacks start, and `forEach` returns right away without waiting:

```js
items.forEach(async (item) => {
  await save(item);
});
console.log("done"); // runs before saves finish
```

Use `for...of` with `await` for one-at-a-time, or `Promise.all(items.map(...))` for all at once (with a concurrency limit for big lists).

## 258: What is the difference between Promise.all, allSettled, race and any?

- `Promise.all`: resolves when all resolve; rejects as soon as one rejects.
- `Promise.allSettled`: waits for all, and gives you each result or error.
- `Promise.race`: settles with the first one that settles, success or failure.
- `Promise.any`: resolves with the first success; rejects with an `AggregateError` if all fail.

None of them cancel the other operations. With `all` and `race`, the losing operations keep running in the background unless you abort them with an `AbortSignal`.

## 259: What happens to I/O events that arrive while a callback is running?

They wait. The OS keeps track of them (data stays in socket buffers, finished thread pool work stays in a queue), and Node picks them up the next time the loop reaches the poll phase. Nothing is lost, it's only delayed. If the delay is long, clients may time out, and kernel buffers or connection backlogs can fill up.

## 260: How do you debounce or throttle work on the server?

The same ideas as in the browser, using timers:

```js
function debounce(fn, ms) {
  let timer;
  return (...args) => {
    clearTimeout(timer);
    timer = setTimeout(() => fn(...args), ms);
  };
}

const saveSettings = debounce(writeSettingsToDisk, 500);
```

On the server, this is useful for batching writes, cache invalidation or reacting to file change events. If the process may exit, remember that a pending debounced call might never run, so flush it during shutdown.

## 261: How do you implement retry with backoff?

```js
const { setTimeout: sleep } = require("node:timers/promises");

async function retry(fn, { retries = 5, baseMs = 100 } = {}) {
  for (let attempt = 0; ; attempt++) {
    try {
      return await fn();
    } catch (err) {
      if (attempt >= retries) throw err;
      const delay = baseMs * 2 ** attempt * (0.5 + Math.random());
      await sleep(delay);
    }
  }
}
```

The wait doesn't block the loop. The random factor (jitter) stops many clients from retrying at the same moment.

## 262: Are many timers expensive in Node.js?

Not very. Node groups timers that share the same delay into lists, and only one underlying libuv timer is used for all of them. Creating and clearing timers is cheap, and `refresh()` is even cheaper. A server with tens of thousands of socket timeouts is normal.

What does cost is the callbacks themselves, and memory held by closures in pending timers.

## 263: How do you deal with a third-party library that blocks the event loop?

Options, from simplest to most work:

1. Check if the library has an async or streaming version of the call.
2. Limit the input size so each call is short.
3. Run the call in a worker thread or worker pool.
4. Run it in a separate process or service.
5. Replace the library.

First confirm it's really the library with a CPU profile, not your own code around it.

## 264: How does a blocked event loop affect Kubernetes health checks?

Liveness and readiness probes usually call an HTTP endpoint on the app. If the event loop is blocked, the probe request can't be handled, it times out, and Kubernetes may mark the pod not ready or restart it. Under heavy load this can cause restarts that make things worse.

Keep probe handlers trivial, set realistic timeouts, and fix the blocking itself.

## 265: How can a readiness check reflect event loop health?

Report not ready when the loop is overloaded, so the load balancer sends traffic elsewhere:

```js
const { performance } = require("node:perf_hooks");

let lastElu = performance.eventLoopUtilization();
let overloaded = false;

setInterval(() => {
  const elu = performance.eventLoopUtilization(lastElu);
  lastElu = performance.eventLoopUtilization();
  overloaded = elu.utilization > 0.9;
}, 1000).unref();

app.get("/ready", (req, res) => {
  res.status(overloaded ? 503 : 200).end();
});
```

Keep liveness checks simpler, so a busy app isn't restarted just for being busy.

## 266: What is load shedding based on the event loop?

Load shedding means rejecting some requests quickly (for example with `503`) when the server is overloaded, instead of accepting everything and getting slow for everyone. Event loop delay and ELU are good signals for this. Fastify has the `@fastify/under-pressure` plugin with options like `maxEventLoopDelay` and `maxEventLoopUtilization`. In Express you can write a small middleware that checks the same metrics.

## 267: What event loop metrics should you monitor in production?

- Event loop delay: p50, p99 and max, from `monitorEventLoopDelay`.
- Event loop utilization.
- GC pause time and frequency.
- CPU usage of the process.
- Heap used and RSS.
- Active handles count (to spot leaks of sockets or timers).

`prom-client`'s default metrics include event loop lag (`nodejs_eventloop_lag_seconds` and percentiles), and OpenTelemetry has runtime instrumentation that reports event loop delay and utilization.

## 268: How does loading code with require affect startup and the event loop?

`require` reads and compiles modules synchronously, so a big dependency tree makes startup slower, and nothing else can run during that time. This is fine at boot, but a first-time `require` inside a request handler (lazy loading) blocks that request and every other one. Newer Node versions also support `require()` of ES modules synchronously, as long as they don't use top-level `await`.

## 269: How does top-level await affect module loading?

When a module uses top-level `await`, any module that imports it waits until it finishes. Modules that don't depend on it can still be evaluated. During the wait, the event loop runs normally, so timers and I/O work.

```js
// db.mjs
export const db = await connect(process.env.DB_URL);

// app.mjs
import { db } from "./db.mjs"; // waits until connect resolves
```

This is handy for setup code, but a slow top-level `await` delays the whole app startup.

## 270: How do you keep a Node.js process alive on purpose?

Keep a ref'd handle open. Normally that's a server, a queue consumer or a connection. For a simple script that should run until stopped:

```js
const keepAlive = setInterval(() => {}, 1 << 30);

process.on("SIGTERM", () => {
  clearInterval(keepAlive);
});
```

In real apps you rarely need this. The open server or consumer connection already keeps the loop alive.

## 271: How can beforeExit be used for final async work?

`beforeExit` runs when the loop is empty and lets you schedule more async work, like flushing buffered logs or metrics:

```js
let flushed = false;

process.on("beforeExit", async () => {
  if (flushed) return;
  flushed = true;
  await metrics.flush(); // async is allowed here
});
```

The guard is needed because after your async work finishes, the loop empties again and `beforeExit` fires again. It does not run on `process.exit()`, signals or crashes, so it's not a replacement for proper shutdown handling.

## 272: What is the difference between process.exit() and process.exitCode?

- `process.exit(code)` stops the process right away. Pending async work is dropped.
- `process.exitCode = code` only sets the code. The process ends normally when the event loop is empty, so pending writes and callbacks can finish.

```js
if (hasErrors) {
  process.exitCode = 1; // let logs flush, then exit with 1
}
```

Prefer `exitCode` in CLIs and scripts unless you really need to stop at once.

## 273: Why can output get lost when calling process.exit()?

Writes to `process.stdout` and `process.stderr` are sometimes async, for example when they go to a pipe (common in containers and CI). If you call `process.exit()` right after a big write, the process ends before the data is flushed, and the end of the output is missing. Setting `process.exitCode` and returning avoids this.

## 274: How should you handle the error event on EventEmitters?

`"error"` is special: if an emitter emits `"error"` and there is no listener, Node throws the error, which usually crashes the process. Always add an `"error"` listener to streams, sockets, servers and other emitters you create.

```js
const stream = fs.createReadStream("missing.txt");
stream.on("error", (err) => {
  console.error("read failed:", err.code);
});
```

Using `stream.pipeline` or `events.once` also handles errors for you.

## 275: Do timers depend on the system clock?

No. Node timers use a monotonic clock, which only moves forward and isn't affected by changes to the system time (NTP adjustments, manual changes, daylight saving time). A 10-minute `setTimeout` fires after about 10 minutes of real time, even if someone changes the clock.

`Date.now()` uses the wall clock, so don't use it for measuring durations where clock jumps could matter. Use `performance.now()` or `process.hrtime.bigint()`.

## 276: What is the cached loop time in libuv?

libuv reads the current time at the start of each loop iteration (and at a few other points) and caches it. Timers use this cached "now" to decide whether they're due and to compute the due time of new timers. This avoids calling the system clock for every timer. A side effect: if a callback runs for a long time, timers created inside it are based on the time from before that callback started, so they may fire a bit sooner than you'd expect counting from when `setTimeout` was actually called.

## 277: How do you measure durations accurately in Node.js?

Use a monotonic high-resolution clock:

```js
const { performance } = require("node:perf_hooks");

const start = performance.now();
await doWork();
console.log(`took ${(performance.now() - start).toFixed(2)} ms`);

const t0 = process.hrtime.bigint();
doSyncWork();
console.log(`took ${(process.hrtime.bigint() - t0) / 1000n} µs`);
```

Remember that the time you measure for an async operation includes time spent waiting in the event loop, not only the operation itself.

## 278: How is reading from a socket different from reading a file?

- **Sockets** are watched with epoll/kqueue/IOCP. The OS tells Node when data is ready, and Node reads it on the main thread without blocking. No thread pool needed.
- **Regular files** are always "ready" from the OS's point of view, but a read can still block on disk. So libuv performs file reads on the thread pool and reports back when they're done.

That's why a slow disk can fill the thread pool, but a slow network client cannot.

## 279: What is the difference between zlib sync and async functions?

- `zlib.gzipSync()` compresses on the main thread and blocks it.
- `zlib.gzip()` and zlib streams do the compression on the thread pool, and your callback or stream events run on the main thread.

For compressing HTTP responses or large files in a server, use the async or stream versions. Note that heavy compression can still fill the thread pool.

## 280: When is crypto.randomBytes sync fine and when is it not?

`crypto.randomBytes(size)` without a callback is synchronous. For small sizes (like a 16- or 32-byte token) it's fast and fine anywhere. For large buffers, or when called very often, use the async version with a callback, which runs on the thread pool. `crypto.randomUUID()` is synchronous but very cheap because Node caches random data for it.

## 281: Why should you use async bcrypt functions in a server?

bcrypt is slow on purpose; one hash can take 50-300 ms depending on the cost factor. `bcrypt.hashSync` and `compareSync` run on the main thread, so every login blocks all other requests. The async `hash` and `compare` functions in the `bcrypt` native package run on the libuv thread pool. Pure-JS versions like `bcryptjs` do the work in JavaScript on the main thread, even in their async versions (they only split the work into chunks).

## 282: Can adding await everywhere slow your code down?

A little. Each `await` creates promises and takes at least one microtask tick, which has a small cost. In hot loops, awaiting things that are not really async (like `await` on a sync function's result) adds overhead for no benefit. It also makes the code look async when it's not. Only `await` real async operations, and avoid making very hot small functions `async` without a reason.

## 283: Is the event loop the same on Windows and Linux?

The phases and the JavaScript-visible behavior are the same, because libuv hides the differences. Internally, Linux uses epoll (readiness-based) and Windows uses IOCP (completion-based). A few details differ: signal support (Windows has limited signals), file watching, how cluster distributes connections by default, and some timing edge cases. Don't rely on exact ordering that isn't documented.

## 284: How is Node's event loop different from Deno's and Bun's?

All three run JavaScript on a main thread with an event loop and microtask queue, and they try to be compatible with Node's APIs. The implementation differs: Node uses libuv, Deno uses Rust's Tokio runtime, and Bun has its own event loop written in Zig. Ordering of Node-specific things like `process.nextTick` and `setImmediate` is emulated in Deno and Bun and may differ in edge cases. If your code depends on exact ordering, test it on the runtime you use.

## 285: How do you schedule something to run at a specific time?

For a one-off at a specific time, compute the delay:

```js
const runAt = new Date("2026-12-31T23:59:00Z");
const delay = runAt.getTime() - Date.now();
setTimeout(job, delay);
```

But remember the 24.8-day max delay, and that the timer is lost if the process restarts. For recurring jobs ("every day at 3 AM"), use a cron library or an external scheduler (system cron, Kubernetes CronJob, a job queue with delayed jobs). Those handle restarts and long delays better.

## 286: How do you handle delays longer than 24.8 days?

Split the wait into steps that are each within the limit:

```js
const MAX = 2 ** 31 - 1;

function longTimeout(fn, ms) {
  if (ms > MAX) {
    return setTimeout(() => longTimeout(fn, ms - MAX), MAX);
  }
  return setTimeout(fn, ms);
}
```

In practice, a process rarely stays up that long, so a persistent scheduler is the better solution.

## 287: What are common event loop mistakes in Express apps?

- Using sync APIs (`readFileSync`, `execSync`, `pbkdf2Sync`) in route handlers.
- Big `JSON.stringify`/`JSON.parse` on every request.
- Heavy work in middleware that runs for every request.
- Unsafe regexes in validation.
- Logging large objects synchronously.
- Not handling rejected promises (in Express 4, a rejected async handler isn't passed to `next` automatically; Express 5 does this).
- Starting unlimited parallel work per request.

## 288: How does a database connection pool work with the event loop?

The pool keeps a few open connections (sockets). When you run a query, the driver takes a free connection, writes the query to the socket and returns a promise. The response comes back as an I/O event in the poll phase, and the promise resolves. If all connections are busy, new queries wait in the pool's queue in JavaScript.

So a slow database doesn't block the event loop, but it can fill the pool, and requests then wait for a free connection. That shows up as high latency with low CPU.

## 289: How do you process background jobs without hurting request latency?

- Run job consumers in a separate process from the web server, so heavy jobs don't block API requests.
- Limit consumer concurrency (most queue libraries have a `concurrency` option).
- Move CPU-heavy job steps to worker threads.
- Yield between batches with `setImmediate` if you must process big batches in the same process.

## 290: How does the event loop affect WebSocket servers?

Each WebSocket connection is a socket in the event loop, so one process can hold many connections. But:

- Broadcasting a message to 50,000 clients in one synchronous loop takes main-thread time. Large broadcasts may need batching.
- Heartbeat (ping/pong) timers for each connection are cheap, but their callbacks add up.
- Parsing and serializing big messages blocks the loop like any JSON work.
- If the loop is blocked, pings are late and clients may disconnect.

## 291: How do you time an async operation correctly?

Start the timer right before starting the operation and stop it in the callback or after `await`:

```js
const start = performance.now();
const rows = await db.query(sql);
const ms = performance.now() - start;
```

This measures the full wait as seen by your code, including any event loop delay before your continuation ran. If the loop was busy, the number will be higher than the database's own timing. Comparing both is a good way to tell if the DB or the loop is slow.

## 292: What happens if a queueMicrotask callback throws?

The error is reported as an uncaught exception (the `"uncaughtException"` event, or a crash by default). This is different from throwing inside a `.then` callback, which turns into a rejected promise and is reported as an unhandled rejection only if nobody handles it.

```js
queueMicrotask(() => {
  throw new Error("boom"); // uncaught exception
});

Promise.resolve().then(() => {
  throw new Error("boom"); // rejected promise
});
```

`process.nextTick` callbacks behave like `queueMicrotask` here.

## 293: How do you read a stream with for await?

Readable streams are async iterables:

```js
const fs = require("node:fs");

async function countBytes(path) {
  let total = 0;
  for await (const chunk of fs.createReadStream(path)) {
    total += chunk.length;
  }
  return total;
}
```

Each chunk is processed when it arrives. The stream is paused while your loop body runs, which gives you backpressure for free. Breaking out of the loop destroys the stream.

## 294: How can you check in a test that code doesn't block the event loop for too long?

Measure the event loop delay while running the code:

```js
const { monitorEventLoopDelay } = require("node:perf_hooks");

test("processing does not block for more than 50 ms", async () => {
  const h = monitorEventLoopDelay({ resolution: 10 });
  h.enable();
  await processBigBatch(items);
  h.disable();
  assert.ok(h.max / 1e6 < 50, `max delay was ${h.max / 1e6} ms`);
});
```

Such tests are sensitive to machine speed, so use generous limits and run them separately from fast unit tests.

## 295: What is the difference between setTimeout and setImmediate when deferring work in a handler?

Both defer work out of the current callback, but:

- `setImmediate` runs in the check phase of the current iteration (right after poll). It has no minimum delay.
- `setTimeout(fn, 0)` waits at least 1 ms and runs in the timers phase.

For "do this after the current I/O batch", `setImmediate` is more direct and slightly faster. For "do this after a specific time", use `setTimeout`.

## 296: Why might Promise.all over 100,000 items cause trouble?

`Promise.all(items.map(fetchItem))` starts all 100,000 operations at once:

- Lots of memory for promises, sockets, buffers and results.
- The thread pool, DB pool or remote API gets flooded, and many requests time out or get rate-limited.
- When results come back, processing them is a burst of main-thread work.

Process the items with a concurrency limit or in batches.

## 297: What does process.memoryUsage() tell you and how does it relate to the event loop?

It returns `rss`, `heapTotal`, `heapUsed`, `external` and `arrayBuffers`. It doesn't measure the event loop directly, but memory and loop health are connected: a growing heap leads to more and longer GC pauses, which show up as event loop delay. Leaked timers, sockets or listeners often show up as both growing memory and a growing number of active handles.

## 298: What is the role of the poll phase timeout when there are no timers?

If there are no timers and no immediates, but there are active handles (for example, a listening server), the poll phase can wait without a timeout until an I/O event arrives. The process sleeps and uses no CPU. As soon as a request comes in, the OS wakes the loop up. That's why an idle Node server uses almost no CPU.

## 299: How do callbacks from native addons and database drivers run?

Most native drivers do their I/O either through libuv sockets or on their own threads. When a result is ready, they must call back into JavaScript on the main thread, usually through libuv (`uv_async_send`) or N-API thread-safe functions. So their callbacks run from the event loop like any other callback, and they're subject to the same delays when the loop is busy.

## 300: How would you explain the Node.js event loop in two minutes in an interview?

A good short answer:

"Node runs JavaScript on one main thread. Slow operations like network and file I/O are handed off to the OS or to libuv's thread pool, so the main thread doesn't wait. When an operation finishes, its callback is queued, and the event loop runs it. The loop goes through phases: timers, pending callbacks, poll for I/O, check for `setImmediate`, and close callbacks. After every callback, Node runs `process.nextTick` callbacks and then promise microtasks. Because everything shares one thread, long synchronous work blocks all other requests, so CPU-heavy work should go to worker threads or be split up."

Then be ready to go deeper on any part.

# Advanced Questions (301-450)

## 301: What does libuv's uv_run loop look like in recent versions?

Simplified, for libuv 1.45 and later (Node 20+):

```c
int uv_run(uv_loop_t* loop, uv_run_mode mode) {
  int r = uv__loop_alive(loop);
  if (!r) uv__update_time(loop);

  // run due timers once before entering the loop (backward compatibility)
  if (mode == UV_RUN_DEFAULT && r != 0 && loop->stop_flag == 0) {
    uv__update_time(loop);
    uv__run_timers(loop);
  }

  while (r != 0 && loop->stop_flag == 0) {
    uv__run_pending(loop);
    uv__run_idle(loop);
    uv__run_prepare(loop);

    int timeout = 0;
    if ((mode == UV_RUN_ONCE && can_sleep) || mode == UV_RUN_DEFAULT)
      timeout = uv__backend_timeout(loop);

    uv__io_poll(loop, timeout);
    uv__run_check(loop);
    uv__run_closing_handles(loop);

    uv__update_time(loop);
    uv__run_timers(loop);

    r = uv__loop_alive(loop);
    if (mode == UV_RUN_ONCE || mode == UV_RUN_NOWAIT) break;
  }
  return r;
}
```

The key point is that timers now run at the end of each iteration, after check and close, instead of at the start. Node calls `uv_run` in default mode and then checks for `beforeExit` and whether the loop became alive again.

## 302: How does libuv decide the poll timeout?

`uv__backend_timeout` returns:

- `0` (don't block) if the loop is stopping, if there are no active handles or requests, if there are active idle handles, if there are pending callbacks, or if handles are closing.
- Otherwise, the time until the nearest timer is due.
- `-1` (block forever) if there are no timers.

Node uses this on purpose: when `setImmediate` callbacks are waiting, Node starts an idle handle, which forces the poll timeout to 0 so the check phase is reached quickly.

## 303: When is the libuv loop considered alive?

`uv__loop_alive` returns true if there are:

- Active and ref'd handles (timers, servers, sockets, signal watchers, child processes, etc.), or
- Active requests (pending fs operations, DNS lookups, writes, thread pool work), or
- Handles that are still closing.

Unref'd handles are not counted. When nothing is alive, `uv_run` returns, Node emits `beforeExit`, and if no new work was scheduled, the process exits.

## 304: How are JavaScript timers implemented on top of libuv?

Node doesn't create a libuv timer for every `setTimeout`. In `lib/internal/timers.js`:

- Timers with the same duration go into one linked list (`TimersList`), keyed by that duration in a map.
- Each list has an expiry time (the earliest timer in it). Lists are kept in a binary heap (priority queue) ordered by expiry.
- One libuv timer handle is scheduled for the earliest expiry.
- When it fires, C++ calls `processTimers(now)`, which takes lists from the heap, runs all expired timers in them, drains `nextTick` and microtasks after each callback, and reschedules the libuv timer for the next expiry.

## 305: Why does Node group timers by duration?

Because timers with the same duration are created in increasing order of time, so a new timer always goes to the end of its list, and the list stays sorted by expiry without any sorting. Inserting is O(1), and clearing is O(1) because it's a linked list. Only the heap of lists needs O(log n) work, and the number of distinct durations is usually small. This makes thousands of socket timeouts (which mostly share the same duration) very cheap.

## 306: What does it cost to create and clear timers at high volume?

Creating a timer allocates a `Timeout` object and appends it to a list, which is cheap. Clearing removes it from the list. If a list becomes empty, it's removed from the heap. The main costs at high volume are:

- Garbage: many short-lived `Timeout` objects create GC pressure.
- Closures: each timer keeps its callback and everything it references alive.

For repeating deadlines on the same object, `timeout.refresh()` reuses the object and avoids both costs.

## 307: How is setImmediate implemented?

Node keeps immediates in a JavaScript linked list. In C++, a libuv check handle runs after each poll phase and calls into JavaScript to process the list. To make sure the poll phase doesn't block while immediates are waiting, Node starts a libuv idle handle whenever there are ref'd immediates (which makes the poll timeout 0) and stops it when the queue is empty.

When processing, Node takes the current list, so immediates added during processing go into a new list for the next iteration. That's why recursive `setImmediate` doesn't starve I/O.

## 308: How does Node run nextTick and microtasks after a native callback?

When C++ calls a JavaScript callback (for example from an I/O completion), it uses an `InternalCallbackScope`. When that scope closes:

- If the `nextTick` queue is empty and there are no pending rejections, Node just runs a V8 microtask checkpoint.
- Otherwise, it calls the JavaScript function `processTicksAndRejections`.

So the "drain after every callback" behavior is tied to every transition from C++ into JavaScript, not to the phases themselves.

## 309: What does processTicksAndRejections do?

It lives in `lib/internal/process/task_queues.js`. Simplified:

```js
function processTicksAndRejections() {
  let tock;
  do {
    while ((tock = queue.shift()) !== null) {
      // restore async context, run the tick callback with its args
      callback(...tock.args);
    }
    runMicrotasks(); // V8 drains the whole microtask queue
  } while (!queue.isEmpty() || processPromiseRejections());
  setHasTickScheduled(false);
  setHasRejectionToWarn(false);
}
```

It explains the classic ordering: all ticks, then all microtasks, repeated until both are empty, and then unhandled rejections are processed.

## 310: How does Node control when V8 runs microtasks?

Node sets V8's microtask policy to explicit. V8 doesn't run microtasks on its own whenever the JavaScript stack empties; Node decides when, by calling `runMicrotasks()` or a microtask checkpoint. That's what makes it possible to run the `nextTick` queue before promise jobs, and to drain both after each callback from the loop.

## 311: Why exactly do promise callbacks run before nextTick in an ES module?

ESM loading and evaluation is promise-based. The top-level code of the entry module runs inside a step of that promise chain, while V8 is already running microtasks. Any promise reaction your module queues gets added to the queue V8 is currently draining, so it runs before control returns to Node. Only after the microtask queue is empty can Node process the `nextTick` queue.

In CommonJS, the main module runs as a plain synchronous call, and Node then calls `processTicksAndRejections`, which runs ticks first. The same difference can appear inside other promise-driven code: a `nextTick` queued from inside a `.then` waits until all microtasks are done.

## 312: How does the ES module loader use the event loop?

Loading ES modules is async: Node resolves specifiers, reads files (asynchronously), parses them and builds the module graph using promises. Then it links and evaluates the modules. Modules without top-level `await` are evaluated synchronously in dependency order; a module with top-level `await` makes its evaluation async, and its dependents wait for it.

Because loading goes through the event loop, timers and I/O can run while a big graph is being loaded, and code that depends on startup ordering can behave differently than with CommonJS.

## 313: How is the libuv thread pool implemented?

- It's a global, process-wide pool created lazily the first time work is queued (`uv_queue_work` or an fs/dns request).
- The size comes from `UV_THREADPOOL_SIZE` (default 4, max 1024), read once at creation.
- Work items go into a shared queue protected by a mutex. Idle threads wait on a condition variable.
- When a thread finishes a task, it puts the result on the owning loop's completed queue and calls `uv_async_send` to wake up that loop.
- The loop then runs the "after work" callbacks on its own thread, which in Node leads to your JavaScript callback.

## 314: Does the thread pool treat DNS lookups differently from file operations?

Yes. libuv marks `getaddrinfo` and `getnameinfo` as "slow I/O" and lets at most about half of the pool threads run slow I/O at the same time. The idea is that slow DNS lookups shouldn't take every thread and stall file operations. So with the default pool of 4, only 2 DNS lookups run at once, and further lookups queue up even if threads are free for fs work.

## 315: How does libuv perform file I/O under the hood?

Each fs call (`open`, `read`, `write`, `stat`, `close`) becomes a `uv_fs_t` request. Without a callback, libuv runs the system call on the current thread (that's how sync APIs work). With a callback, it queues the request on the thread pool, a pool thread runs the blocking system call, and the completion is sent back to the loop. A single `fs.readFile` is several such requests in a row, each a round trip through the pool.

## 316: Why does libuv use a thread pool for files instead of epoll?

epoll and kqueue work on readiness: "is this file descriptor ready to read without blocking?" Regular files always report ready, even if the actual read will wait on a slow disk. So readiness-based APIs don't help for files. The portable solution is to run blocking file calls on other threads. On Linux, io_uring offers real async file I/O, which libuv can use (see the next question).

## 317: What is io_uring and what is its status in libuv and Node?

io_uring is a Linux kernel interface for truly asynchronous I/O, including files. libuv 1.45 (Node 20) added support for using it for file operations, which can avoid the thread pool and be much faster for some workloads.

Because of bugs and a security issue found later, Node and libuv became more careful: in current versions, io_uring for file operations is off by default and can be enabled with the `UV_USE_IO_URING=1` environment variable. Check the release notes for your exact Node version before relying on it.

## 318: How do you diagnose thread pool saturation?

Signs:

- File, DNS or crypto operations get slow, but event loop delay and CPU on the main thread look normal.
- Latency grows in steps as concurrency passes 4 (or your pool size).
- Outgoing HTTP calls to many hosts are slow to start (stuck in `dns.lookup`).

Ways to confirm:

- Time how long a trivial `fs.stat` takes under load; it should be under a millisecond.
- Raise `UV_THREADPOOL_SIZE` in a test and see if latency drops.
- Use OS tools (like `perf` or `top -H`) to see the pool threads busy.
- Count concurrent crypto/zlib/fs operations in your code.

## 319: Is the thread pool shared between worker threads?

Yes. There is one libuv thread pool per process. The main thread and all worker threads queue work to the same pool. So a worker doing lots of async file I/O or `crypto.scrypt` can slow down file operations on the main thread. Size the pool for the whole process, not per thread.

## 320: What happens if you set UV_THREADPOOL_SIZE after the pool is used?

Nothing. libuv reads the variable once, when the pool is first created. Any later change is ignored. Even setting it at the top of your entry file can be too late if some module you `require` first already touched the pool (for example by reading a file asynchronously during import). That's why the safe way is to set it in the environment before Node starts.

## 321: How do native addons use the event loop?

With Node-API, the two main tools are:

- `napi_create_async_work`: you provide an `execute` function that runs on the libuv thread pool (no JavaScript allowed there) and a `complete` function that runs on the main thread, where you can resolve a promise or call a JavaScript callback.
- `napi_create_threadsafe_function`: lets any thread (including the addon's own threads) queue calls to a JavaScript function. They're delivered on the main thread through the event loop.

Addons that block the main thread inside a synchronous JavaScript call block the loop like any other sync code.

## 322: What is uv_async_send?

It's the libuv function other threads use to wake up an event loop. An async handle registered on the loop has an internal file descriptor (an eventfd on Linux, a pipe elsewhere). Calling `uv_async_send` from another thread writes to it, which wakes the loop from the poll phase, and the handle's callback then runs on the loop thread. Several sends before the loop wakes up can be merged into one callback. Thread pool completions, worker messages and thread-safe functions all depend on this.

## 323: How does libuv deliver signals to the event loop?

Unix signal handlers can only safely do very little. libuv's signal handler just writes the signal number to an internal pipe (the "self-pipe trick"). The loop watches that pipe, so in the poll phase it reads the signal and calls the callbacks of matching signal handles. In Node, those callbacks emit `process.on("SIGTERM")` and similar events. That's why your signal handler runs on the main thread and can be delayed by blocking code.

## 324: How are child process exits detected?

On Unix, libuv installs a `SIGCHLD` handler (through the same signal mechanism). When a child exits, the loop wakes up, calls `waitpid` to collect the exit status, and runs the process handle's exit callback. Node then emits `"exit"` on the `ChildProcess` and, once its stdio is closed, `"close"`. On Windows, libuv waits on the process handle instead.

## 325: How does dns.resolve integrate with the event loop?

`dns.resolve*` uses the c-ares library. c-ares creates UDP/TCP sockets to talk to DNS servers, and Node registers those sockets with libuv, so responses arrive as normal I/O events in the poll phase. c-ares retry and timeout logic is driven by a libuv timer. No thread pool is used, so many `resolve` calls can run in parallel without affecting fs operations.

## 326: Can a busy poll phase delay timers?

Yes. Within one poll phase, libuv processes the I/O events it got from the OS, and each callback runs JavaScript plus the microtask queues. If many sockets have data, or each callback does a lot of work, the poll phase can run well past a timer's due time. Timers then run late, in the timers phase at the end of that iteration. libuv limits how many rounds of events it handles in one poll phase so that other phases still get a turn, but long callbacks still cause delay.

## 327: Is there a limit on how many callbacks run in one phase?

- **Timers**: all timers that are due at the cached "now" are run.
- **Poll**: libuv handles a bounded number of event batches before moving on (system-dependent), but each I/O callback runs fully.
- **Check**: all immediates queued before the phase started.
- **nextTick and microtasks**: no limit at all, they're drained completely, which is why they can starve the loop.

## 328: What kinds of callbacks end up in the pending callbacks phase?

libuv uses the pending queue for I/O callbacks it decided not to run immediately, so as not to run user code in the middle of internal processing. Examples include some write completions and errors on streams, and on some systems certain connection errors. From JavaScript you rarely notice this phase. It's mostly important for understanding that "I/O callbacks" are not all in one place.

## 329: How does closing a handle work?

`uv_close(handle, cb)` stops the handle immediately (no more events), but the close callback runs later in the close phase. This gives libuv a safe point to free resources, because the handle might still be referenced by code that's running in the current iteration. In Node, `socket.destroy()` and `server.close()` lead to `uv_close`, and `"close"` events are emitted from there or through `nextTick`.

## 330: Where does HTTP parsing happen?

Node parses HTTP/1 with llhttp, a C library, but it runs on the main thread, called synchronously when data arrives. So parsing cost counts against the event loop. For typical requests it's tiny, but very large headers, huge numbers of small requests, or pipelined requests do consume main-thread time. Request bodies are delivered as stream chunks, which you parse yourself (often with `JSON.parse`, which is also main-thread work).

## 331: How does TLS affect the event loop?

TLS encryption, decryption and especially handshakes run in OpenSSL on the main thread. A full handshake with RSA or ECDHE takes noticeable CPU time. A burst of new TLS connections (after a deploy, or a reconnect storm) can block the loop for a while. Mitigations:

- Terminate TLS at a load balancer or proxy.
- Enable session resumption (session tickets) so returning clients skip the expensive part.
- Use ECDSA certificates, which are cheaper than RSA.
- Scale out across more processes.

## 332: How does a worker thread start and what does it cost?

Creating a `Worker` starts a new OS thread with its own V8 isolate, its own event loop and its own copy of Node's bootstrap code. It takes tens of milliseconds and several megabytes of memory. The worker then loads your script and its imports, which takes more time. That's why you should keep workers alive in a pool instead of creating one per task.

## 333: What are resourceLimits for workers?

`resourceLimits` lets you cap a worker's memory, so a bad task can't take down the whole process:

```js
new Worker("./task.js", {
  resourceLimits: {
    maxOldGenerationSizeMb: 256,
    maxYoungGenerationSizeMb: 32,
    stackSizeMb: 4,
  },
});
```

If the worker goes over its limit, it's terminated with an `ERR_WORKER_OUT_OF_MEMORY` error, and the main thread gets an `"error"` event.

## 334: How does worker.terminate() work?

`worker.terminate()` asks V8 to stop executing JavaScript in the worker as soon as possible, even in the middle of an infinite loop, and then shuts the worker down. It returns a promise that resolves with the exit code. Cleanup inside the worker (like `finally` blocks) may not run. Thread pool work already started on the worker's behalf will still finish, but its callback is dropped.

This is the only reliable way to stop runaway synchronous JavaScript, which is why "run untrusted or unbounded work in a worker with a timeout" is a common pattern.

## 335: How do you enforce a timeout on CPU-heavy work?

You can't interrupt synchronous code on the main thread from JavaScript, because no other code runs until it returns. So run the work in a worker and terminate it if it takes too long:

```js
const { Worker } = require("node:worker_threads");

function runWithTimeout(file, data, ms) {
  return new Promise((resolve, reject) => {
    const worker = new Worker(file, { workerData: data });
    const timer = setTimeout(() => {
      worker.terminate();
      reject(new Error("timed out"));
    }, ms);

    worker.once("message", (result) => {
      clearTimeout(timer);
      resolve(result);
    });
    worker.once("error", (err) => {
      clearTimeout(timer);
      reject(err);
    });
  });
}
```

## 336: How is event loop utilization calculated?

libuv tracks how long the loop spends idle inside the poll phase, waiting for events (`uv_metrics_idle_time`). Node's `performance.eventLoopUtilization()` returns `idle` and `active` times, where active is the time since the loop started (or since your last sample) minus idle time, and `utilization = active / (active + idle)`. Because it uses the loop's own idle time, it measures how busy the loop is, not how busy the whole process or CPU is.

## 337: Why is ELU often a better signal than CPU usage?

Process CPU usage includes time from all threads: GC helper threads, the thread pool, worker threads. A process can show 150% CPU while the main loop still has room, or 60% CPU while the main loop is completely saturated. ELU measures only the main event loop, which is what decides whether new requests can be handled quickly. It also works well in containers where CPU numbers can be confusing.

## 338: Why can latency be high while event loop delay is low?

Because the loop isn't the bottleneck. Common causes:

- Waiting for a slow database, cache or downstream API.
- A full connection pool (requests waiting for a free connection).
- Thread pool saturation (slow fs, DNS or crypto).
- Rate limiting or retries with backoff.
- Network problems.

Low event loop delay just tells you the main thread is free. You need tracing or per-dependency timing to find the slow part.

## 339: How does V8's garbage collector interact with the event loop?

V8 uses a generational GC:

- **Scavenges** (young generation) are frequent and short. They do most work in parallel on helper threads but still pause the main thread briefly.
- **Mark-compact** (old generation) uses concurrent and incremental marking on background threads, but has pauses on the main thread for parts of the work.

Node also lets V8 do some GC work during idle time. Any main-thread pause is time when no callbacks run, so it appears as event loop delay. Lots of allocation means more scavenges; a big, busy old generation means longer major GCs.

## 340: How do you create a flame graph of event loop work?

Options:

- `node --cpu-prof app.js` and open the `.cpuprofile` in Chrome DevTools, which shows a flame chart.
- `node --inspect app.js`, connect DevTools and record a profile during load.
- `0x` or Linux `perf` with `--perf-basic-prof` for system-level flame graphs that include native frames.

Look for wide bars on the main thread: those are functions that take a lot of time. Tall, narrow stacks are rarely the problem.

## 341: How do you take a CPU profile in production without restarting?

Use the `inspector` module from inside the process, for example triggered by an admin endpoint or a signal:

```js
const inspector = require("node:inspector/promises");
const fs = require("node:fs/promises");

async function profile(ms) {
  const session = new inspector.Session();
  session.connect();
  await session.post("Profiler.enable");
  await session.post("Profiler.start");
  await new Promise((r) => setTimeout(r, ms));
  const { profile } = await session.post("Profiler.stop");
  await fs.writeFile(
    `profile-${Date.now()}.cpuprofile`,
    JSON.stringify(profile),
  );
  session.disconnect();
}
```

Protect such endpoints well. Profiling has a cost, so keep the duration short.

## 342: How can you find which handlers block the loop in production?

- Keep an event loop delay histogram and alert on high p99 or max.
- Record the duration of each request handler's synchronous part. One way is to measure ELU before and after the handler, or time from start of the handler until its first `await`.
- Use APM tools that report blocking spans or long tasks.
- Take on-demand CPU profiles when delay spikes.
- Use `diagnostics_channel` hooks (for example `http.server.request.start`) to attach timing without changing route code.

## 343: How is AsyncLocalStorage implemented in newer Node versions?

Older versions built `AsyncLocalStorage` on `async_hooks` and V8 promise hooks, which ran code for every promise and every async resource, and cost noticeable performance.

Since Node 24, the default implementation uses `AsyncContextFrame`, which relies on V8's support for carrying a "continuation preserved embedder data" value through promise jobs. The current context is a frame captured when an async operation is created and restored when its continuation runs. This removes most of the per-promise overhead. It's also close to how the TC39 `AsyncContext` proposal is expected to work.

## 344: What is the performance cost of AsyncLocalStorage?

With the newer `AsyncContextFrame` implementation, the cost is small: capturing and restoring a reference when async work is scheduled and run. With the older `async_hooks`-based implementation, enabling `AsyncLocalStorage` made every promise more expensive, and benchmarks showed real slowdowns in promise-heavy code.

Advice: use one or a few `AsyncLocalStorage` instances, store a small object (like `{ requestId, user }`), and avoid `enterWith` in shared code because it changes context for the rest of the current synchronous execution.

## 345: Why is async_hooks.createHook expensive?

When any hook is enabled, Node has to call your `init`, `before`, `after` and `destroy` callbacks for every async resource and every promise. For promises, it also enables V8 promise hooks, which slow down all promise operations. In a busy app that's millions of extra function calls per second. On top of that, your hook callbacks must be careful, because calling async APIs inside them (like `console.log`, which can be async) can cause infinite recursion.

## 346: How do you keep async context across APIs that lose it?

Some libraries queue callbacks in their own data structures and call them later, from another context (connection pools, custom event systems). Then `AsyncLocalStorage.getStore()` returns the wrong store. Fixes:

```js
const { AsyncLocalStorage, AsyncResource } = require("node:async_hooks");

// bind one function to the current context
pool.acquire(
  AsyncResource.bind((err, conn) => {
    /* ... */
  }),
);

// or capture the whole context and run something in it later
const runInContext = AsyncLocalStorage.snapshot();
queue.push(() => runInContext(() => handleJob()));
```

Many popular libraries now do this internally, but custom pools often need it.

## 347: How can microtask starvation happen in real code?

Common cases:

- A recursive async function that only awaits already-resolved values (for example, data from an in-memory cache) and never real I/O.
- An async loop over a huge array where each step awaits a sync-resolved promise.
- A stream or event handler that keeps re-queueing work with `queueMicrotask` or `process.nextTick`.

Each step yields only to the microtask queue, so I/O, timers and other requests can't run until the whole thing ends. Symptom: event loop delay spikes, but the CPU profile shows small functions, not one big one.

## 348: Why can a loop of await null hang I/O?

```js
async function busy() {
  while (!done) {
    await null; // only yields to microtasks
  }
}
```

If `done` is meant to be set by an I/O callback or a timer, it never will be, because those callbacks can't run while the microtask queue keeps getting new jobs. The loop spins forever at 100% CPU. Replace `await null` with `await setImmediate()` from `node:timers/promises`, or better, wait on an event or promise that is resolved when `done` changes.

## 349: How would you design an in-memory rate limiter without leaking timers?

Avoid one timer per client. Store timestamps or counters and clean up in bulk:

```js
const windows = new Map(); // key -> { count, resetAt }

function allow(key, limit, windowMs) {
  const now = Date.now();
  let w = windows.get(key);
  if (!w || w.resetAt <= now) {
    w = { count: 0, resetAt: now + windowMs };
    windows.set(key, w);
  }
  w.count++;
  return w.count <= limit;
}

// one unref'd timer cleans expired entries
setInterval(() => {
  const now = Date.now();
  for (const [key, w] of windows) if (w.resetAt <= now) windows.delete(key);
}, 60_000).unref();
```

One timer for all keys keeps the timer count constant. For multiple processes, use Redis instead, since in-memory limits are per process.

## 350: How would you design a service that handles CPU-heavy jobs in Node?

- Keep the HTTP layer thin: validate, enqueue, respond (or stream progress).
- Run the CPU work in a worker pool sized to the number of cores available to the container (`os.availableParallelism()`), leaving room for the main thread.
- Put a bounded queue in front of the pool, and reject or shed load when it's full instead of letting latency grow without limit.
- Set timeouts per job and terminate workers that run too long.
- Watch ELU of the main thread and of each worker.
- If the jobs are very heavy or long, move them to a separate service consuming from a message queue, so web traffic and batch work scale separately.

## 351: How would you handle heartbeats for 100,000 WebSocket connections?

Don't create a separate interval per connection. Use one interval that walks all connections:

```js
const HEARTBEAT_MS = 30_000;

setInterval(() => {
  for (const ws of wss.clients) {
    if (ws.isAlive === false) {
      ws.terminate();
      continue;
    }
    ws.isAlive = false;
    ws.ping();
  }
}, HEARTBEAT_MS).unref();

wss.on("connection", (ws) => {
  ws.isAlive = true;
  ws.on("pong", () => (ws.isAlive = true));
});
```

If one loop over 100,000 clients takes too long, split the clients into buckets and process one bucket per tick, so the work is spread over the interval.

## 352: The p99 latency spikes every few seconds. How do you investigate?

1. Check event loop delay and ELU. If delay spikes match the latency spikes, something blocks the main thread.
2. Check GC metrics. Regular spikes often line up with major GCs caused by heap growth or large allocations.
3. Look for periodic jobs in the same process: cache refreshes, metric flushes, cron-like `setInterval` tasks doing big synchronous work.
4. Take a CPU profile during a spike.
5. If the loop looks fine, look outside: connection pool exhaustion, DB checkpoints, noisy neighbors, CPU throttling in the container (check cgroup throttling metrics).

## 353: One CPU core is at 100% and the others are idle. What does it tell you?

The Node main thread is saturated, and nothing is spreading the work to other cores. The event loop can only use one core for JavaScript. Next steps:

- Check ELU; it will be close to 1.
- Profile to see if the work is necessary or can be made cheaper.
- Scale out: more processes (cluster, more containers) behind a load balancer.
- Move CPU-heavy parts to worker threads.

If the busy thread is not the main thread, it may be a GC thread or a thread pool thread, which points to a different problem.

## 354: The app got slow after adding password hashing. Why, and how do you fix it?

Possible reasons:

- A sync API (`bcrypt.hashSync`, `crypto.scryptSync`) blocks the main thread for each login.
- With async APIs, every hash uses a thread pool thread for 100+ ms. With 4 threads, only 4 hashes run at once, and fs and DNS operations queue behind them.
- A pure-JS bcrypt runs on the main thread even in its "async" mode.

Fixes: use async native implementations (`crypto.scrypt`, native `bcrypt`), increase `UV_THREADPOOL_SIZE` to match cores, limit concurrent hashing, move hashing to a worker pool or a separate auth service, and rate-limit login attempts.

## 355: File uploads become slow whenever outgoing API calls spike. What could be the reason?

They likely share the thread pool. Outgoing HTTP calls use `dns.lookup` by default, which runs on the thread pool. If you call many different hosts, or DNS is slow, lookups occupy pool threads. File writes for uploads also use the pool and have to wait.

Fixes: cache DNS results (custom `lookup` with caching, or reuse keep-alive connections so lookups are rare), increase `UV_THREADPOOL_SIZE`, or use `dns.resolve`-based lookups that don't use the pool. Measuring `fs` operation latency during the spike confirms it.

## 356: A test suite hangs after all tests pass. How do you find the cause?

1. Run with your runner's open handle detection (`jest --detectOpenHandles`) or print `process.getActiveResourcesInfo()` in a global teardown.
2. Look for: servers not closed, DB or Redis clients not disconnected, intervals not cleared, file watchers, workers, child processes, keep-alive agents.
3. Close them in `after`/`afterAll` hooks, awaiting the close callbacks.
4. Unref background timers in the app code itself if they shouldn't keep the process alive.

Using `--forceExit` hides the leak, and leaked handles can also cause flaky tests.

## 357: A script exits before its async work finishes. Why?

The loop had nothing ref'd to wait for. Common causes:

- The work is waiting on a promise that nothing will resolve (no timer or I/O behind it).
- The only handle was unref'd (a timer, socket or worker).
- The code calls `process.exit()` before the work completes.
- A top-level `await` waits on a promise that never settles (ESM exits with code 13 and a warning).
- A rejected promise crashed the process, and the error output was missed.

Keep a reference to the work and `await` it, and avoid `process.exit()` in the normal flow.

## 358: Memory grows slowly and the number of active handles grows too. What is likely happening?

Something creates handles and never closes them: intervals that are never cleared, sockets not destroyed after errors, event listeners added on every request to a long-lived emitter, file watchers, or timers holding big closures. Each handle and its closure keeps memory alive.

Check `process.getActiveResourcesInfo()` over time to see which type grows, take heap snapshots to find what holds the memory, and look for "MaxListenersExceededWarning" in the logs.

## 359: Health checks fail under load even though the server is up. Why?

Under load, the event loop is busy, and the probe request waits in line with everything else (or the main thread is blocked by a long task). If the probe timeout is shorter than the event loop delay, the probe fails, and the orchestrator may restart a pod that was only busy, making the overload worse.

Fixes: remove blocking work from handlers, add load shedding so the loop doesn't get overwhelmed, set realistic probe timeouts and thresholds, and keep the liveness check as cheap as possible.

## 360: Logging made the server slow. How can logging block the event loop?

- `console.log` to a file or terminal is synchronous, and to pipes can be either sync or async depending on the platform.
- Formatting large objects (`util.inspect`, `JSON.stringify`) is main-thread work.
- Logging on every request at debug level multiplies all that.

Fixes: use a fast structured logger (like pino), send logs to a separate thread or process (pino transports run in worker threads), lower the log level in production, avoid logging large objects, and log fields rather than whole request or response objects.

## 361: A large JSON response blocks the server. What are your options?

1. Return less data: pagination, field selection, limits.
2. Stream the response: write items one by one instead of `JSON.stringify` on the whole array.
3. Precompute and cache the serialized response if it rarely changes.
4. Serialize in a worker thread if it must be one big document (the string still has to be copied back, but the main thread is free during serialization).
5. Use a schema-based serializer (for example Fastify's `fast-json-stringify`), which is faster than generic `JSON.stringify`.

## 362: Timers fire seconds late in production. What would you check?

- Event loop delay: a blocked or overloaded loop delays every timer.
- GC pauses.
- CPU throttling of the container (CFS quota): the process is paused by the kernel even if Node is fine.
- The process being suspended (debugger, `SIGSTOP`, VM pauses, laptop sleep in dev).
- Timers created with a huge delay that overflowed to 1 ms (wrong the other way, but still a timing bug).
- Whether the timer is really started when you think it is (for example after a slow `await`).

## 363: How does a slow request handler cause head-of-line blocking in Node?

In Node, there's no per-request thread. If one handler runs 300 ms of synchronous work, every other request that becomes ready during those 300 ms waits behind it, even if those requests only need 1 ms. Under load, these waits stack up, and latency grows for all users. That's why you measure the synchronous part of each handler and keep it short, and move heavy work off the main thread.

## 364: How do you design a fair scheduler for heavy work across requests?

If several requests each need a lot of CPU work in the main thread, process them in small slices and rotate between them, yielding to the loop between slices:

```js
const { setImmediate: yieldLoop } = require("node:timers/promises");

async function processInSlices(items, handle, sliceMs = 10) {
  let start = performance.now();
  for (const item of items) {
    handle(item);
    if (performance.now() - start > sliceMs) {
      await yieldLoop(); // let I/O and other requests run
      start = performance.now();
    }
  }
}
```

Each request's work interleaves with others, and I/O runs between slices. Yielding based on time rather than item count adapts to how expensive each item is.

## 365: How do vm timeouts relate to the event loop?

`vm.runInContext(code, ctx, { timeout: 100 })` stops synchronous code that runs longer than 100 ms. It doesn't cover async work the code schedules: promises, timers and callbacks run later on the normal event loop, outside the timeout. Also, promise jobs created in the context normally run in the main microtask queue, so an infinite promise loop escapes the timeout.

With `microtaskMode: "afterEvaluate"`, the context gets its own microtask queue that runs right after the script, inside the timeout. Note that `vm` is not a security boundary; for untrusted code use separate processes or isolates.

## 366: What was the domain module and why is it deprecated?

`domain` was an early attempt to catch errors from all async operations started within a "domain", so one request's errors could be handled without crashing the process. It was implemented with hooks on the event loop and EventEmitter. It was deprecated because it was hard to use correctly, didn't work well with promises, and encouraged keeping a process running after an unknown error. Use `try/catch` with `async`/`await`, error events, and `AsyncLocalStorage` for context instead.

## 367: When exactly does Node decide that a rejection is unhandled?

When a promise is rejected with no handler, V8 notifies Node, and Node adds it to a list of possibly unhandled rejections. If a handler is attached later, V8 notifies Node again and it's removed from the list. Node checks the list at the end of `processTicksAndRejections`, after the `nextTick` and microtask queues are drained. So a handler attached in the same tick or in a microtask is fine, but one attached in a `setTimeout` is too late:

```js
const p = Promise.reject(new Error("x"));
setTimeout(() => p.catch(() => {}), 0); // too late: crash in default mode
```

## 368: What is the rejectionHandled event?

It fires when a promise that was already reported as unhandled gets a handler later. It only matters when the process didn't crash on the unhandled rejection (for example with `--unhandled-rejections=warn` or an `unhandledRejection` listener). Tracking both events lets you keep a list of rejections that are still unhandled.

## 369: What is the output of a script mixing fs.readFile, timers, immediates, promises and nextTick?

```js
const fs = require("node:fs");

console.log("1");
setTimeout(() => console.log("2 timeout"), 0);
setImmediate(() => console.log("3 immediate"));

fs.readFile(__filename, () => {
  console.log("4 readFile");
  setTimeout(() => console.log("5 timeout in I/O"), 0);
  setImmediate(() => console.log("6 immediate in I/O"));
  process.nextTick(() => console.log("7 nextTick in I/O"));
});

Promise.resolve().then(() => console.log("8 promise"));
process.nextTick(() => console.log("9 nextTick"));
console.log("10");
```

```
1
10
9 nextTick
8 promise
2 timeout / 3 immediate (order between these two can vary)
4 readFile
7 nextTick in I/O
6 immediate in I/O
5 timeout in I/O
```

`fs.readFile` needs several thread pool round trips (open, stat, read, close), so its callback comes several iterations later, after the first timer and immediate. Inside it, the usual I/O rules apply: nextTick first, then the immediate, then the timer.

## 370: What is the output when an immediate queues nextTick and a promise before a second immediate runs?

```js
setTimeout(() => {
  console.log("timeout");

  setImmediate(() => {
    console.log("immediate 1");
    process.nextTick(() => console.log("tick"));
    Promise.resolve().then(() => console.log("promise"));
  });

  setImmediate(() => console.log("immediate 2"));
}, 0);
```

```
timeout
immediate 1
tick
promise
immediate 2
```

Both immediates run in the same check phase. After `immediate 1` finishes, Node drains its `nextTick` and promise queues before running `immediate 2`. Before Node 11, `immediate 2` would run before `tick` and `promise`.

## 371: What is the output of two interleaved promise chains?

```js
Promise.resolve()
  .then(() => console.log(1))
  .then(() => console.log(2))
  .then(() => console.log(3));

Promise.resolve()
  .then(() => console.log(4))
  .then(() => console.log(5))
  .then(() => console.log(6));
```

```
1
4
2
5
3
6
```

Each `.then` in a chain is only queued when the previous one finishes, so the two chains take turns, one step per microtask.

## 372: What is the output when an async function returns a promise instead of a value?

```js
async function f() {
  return Promise.resolve("f");
}

f().then((v) => console.log(v));

Promise.resolve()
  .then(() => console.log("a"))
  .then(() => console.log("b"))
  .then(() => console.log("c"));
```

```
a
b
f
c
```

When an `async` function returns a promise, its result promise has to "adopt" that promise. That takes two extra microtask ticks: one job to call `.then` on the returned promise, and one for that `.then` to run. So `f` is logged after `b`. If `f` returned a plain value, it would be logged before `b`.

## 373: What is the output when you await a custom thenable object?

```js
const thenable = {
  then(resolve) {
    console.log("then called");
    resolve("value");
  },
};

(async () => {
  const v = await thenable;
  console.log("got", v);
})();

console.log("sync");
```

```
sync
then called
got value
```

`await` on a non-promise thenable doesn't call `then` right away. V8 schedules a job to call it, so `then called` is printed after the synchronous code. This is also why thenables cost extra ticks compared to native promises.

## 374: What is the output when an EventEmitter listener emits another event?

```js
const { EventEmitter } = require("node:events");
const e = new EventEmitter();

e.on("x", () => {
  console.log("A");
  e.emit("y");
  console.log("B");
});
e.on("y", () => console.log("C"));

console.log("start");
e.emit("x");
console.log("end");
```

```
start
A
C
B
end
```

`emit` is a plain synchronous function call. Emitting `"y"` inside the `"x"` listener runs the `"y"` listener right there, before `B`. No event loop involved.

## 375: What is the output of a long recursive process.nextTick chain, and why is it a problem?

```js
let n = 0;

function tick() {
  if (++n < 1_000_000) process.nextTick(tick);
}
tick();

setImmediate(() => console.log("immediate, n =", n));
setTimeout(() => console.log("timeout, n =", n), 0);
```

Both log `n = 1000000` (in either order). All one million `nextTick` callbacks run before the loop even gets to the timers or check phase. With a counter it ends, but with an unbounded condition this pattern starves the loop forever. That's why recursive `nextTick` is dangerous and recursive `setImmediate` is the safe alternative.

## 376: Why does await on a non-promise value still pause the function?

The spec says `await value` first converts `value` to a promise (like `Promise.resolve(value)`) and then waits on it. Waiting on a promise always continues in a microtask, even if the promise is already resolved. So `await 5` always gives other microtasks a chance to run before the function continues, and the rest of the function never runs synchronously. This keeps behavior consistent: you never have to wonder if code after `await` runs now or later.

## 377: What is the difference between Promise.resolve(p) and new Promise(r => r(p))?

If `p` is a native promise, `Promise.resolve(p)` returns `p` itself, with no extra ticks. `new Promise((r) => r(p))` creates a new promise that has to adopt `p`'s state, which needs a job to call `p.then` and then another to pass the result, so it settles two microtask ticks later than `p`.

```js
const p = Promise.resolve(1);
console.log(Promise.resolve(p) === p); // true
```

This is the same mechanism that makes `return somePromise` in an `async` function take extra ticks.

## 378: Why exactly is the order of setTimeout(0) and setImmediate non-deterministic in the main script?

`setTimeout(fn, 0)` becomes a 1 ms timer, with its start time taken from libuv's cached loop time. When the loop starts, libuv updates its time and runs due timers once before the first iteration. Whether the timer is due at that moment depends on how much real time passed between scheduling it and that check:

- If at least 1 ms passed (slow startup, busy machine), the timeout runs first.
- If less than 1 ms passed, the timer isn't due. The loop goes to poll (which doesn't block because an immediate is pending), then check, so the immediate runs first.

It's a race against the clock, which is why it changes between runs.

## 379: What happens to timers when the event loop was blocked for a long time?

When the loop finally reaches the timers phase, every timer that's due by now runs in that phase, in order of their due time. If you had 50 timers that should have fired over the last 2 seconds, all 50 fire back to back. After each, the `nextTick` and microtask queues are drained. This burst can cause a second wave of delay. Timers don't remember how late they were; you can measure it yourself if you need to.

## 380: Does setInterval catch up on missed runs after the loop was blocked?

No. When an interval callback runs, Node schedules the next run `delay` ms from the time it ran, based on the loop's current time. If the loop was blocked for 5 seconds with a 1-second interval, you get one run when the block ends, not five. If you need "one run per period no matter what", track the expected times yourself and compute how many periods passed.

## 381: Is the order of timers with different durations that become due at the same moment guaranteed?

No. Timers are grouped by duration, and the lists are ordered by expiry in a priority queue. If a 10 ms timer created at time 0 and a 5 ms timer created at time 5 are both due at time 10, their relative order isn't something you should rely on. It also depends on libuv's cached time when each timer was created. If order matters, chain the work explicitly instead of relying on timers.

## 382: When can sync APIs actually be better than async ones?

- At startup and in CLIs, where nothing else needs to run in parallel. Sync calls avoid the overhead of the thread pool round trip and promises, so they're often faster.
- For very small, local operations (like reading a tiny config file once).
- Inside a worker thread whose job is just that work, since blocking the worker's loop doesn't affect the main thread.

The rule isn't "never use sync", it's "never block a loop that other work depends on".

## 383: Why can fs.readFile be slower than fs.readFileSync for many small files?

Each async `readFile` is several thread pool round trips (open, stat, read, close). Each round trip involves queueing work, a thread switch, waking up the loop and running callbacks, plus promise overhead with the promise API. For thousands of tiny files, this overhead can be larger than the actual disk work, so the sync version finishes the batch faster. But during that batch the loop is blocked, so this only makes sense in scripts, build tools or workers.

## 384: How does the event loop behave in AWS Lambda?

Lambda runs your handler, and for `async` handlers the invocation ends when the returned promise settles. Any timers, sockets or callbacks still pending are frozen with the execution environment. If the same environment is reused for the next invocation, they may resume then, which can cause confusing bugs (for example, a log write or metric flush that happens during the next request).

For callback-style handlers, the `context.callbackWaitsForEmptyEventLoop` setting controls whether Lambda waits for the loop to be empty before freezing. Best practice: `await` everything your handler starts before returning.

## 385: How do container CPU limits affect a Node app?

- With a CPU quota (for example 1 CPU in Kubernetes), the kernel can pause your process when it uses up its quota in a period. That shows up as event loop delay even if your code didn't block.
- `os.cpus().length` can report the host's cores, not the container's limit. `os.availableParallelism()` is better, but depending on the version it may not reflect a CPU quota either, so check it in your environment.
- Starting too many workers, cluster processes or thread pool threads for the actual CPU limit causes more throttling, not more throughput.

Size worker pools and thread pools from the real CPU limit, often passed in through an environment variable.

## 386: How do you size processes, worker threads and the thread pool together?

Think about the total CPU you have and who uses it:

- Each Node process has a main thread (one core when busy).
- Each worker thread doing CPU work uses up to a core.
- Thread pool threads use CPU for crypto/zlib, but mostly wait for fs.

A common starting point on N cores: either N processes with small or no worker pools (for I/O-heavy web services), or 1-2 processes with a worker pool of about N-1 (for CPU-heavy services). Set `UV_THREADPOOL_SIZE` higher only if you see pool waits. Then load test and adjust using ELU and latency.

## 387: How would you build a job queue between threads using SharedArrayBuffer?

Use a ring buffer in shared memory with head and tail indexes, updated with `Atomics`:

- The producer writes data into the next slot, then increments `tail` with `Atomics.store` and calls `Atomics.notify` to wake a waiting consumer.
- The consumer reads at `head`, increments it, and when the queue is empty, waits with `Atomics.wait` (in a worker) or `Atomics.waitAsync` (if it must keep its event loop running).

This avoids `postMessage` copying and event loop overhead, which matters for very high message rates. It's also much harder to get right, so only do it after `postMessage` (with transferables) has proven too slow.

## 388: When is Node.js the wrong choice because of its event loop model?

- Mostly CPU-bound services (video encoding, heavy numeric work, ML inference in JavaScript) where every request needs a lot of computation.
- Workloads that need hard real-time or very precise timing, since GC pauses and loop delays add jitter.
- Teams that would end up putting most code in worker threads anyway; at that point a multi-threaded runtime may be simpler.

Node is a great fit for I/O-heavy APIs, gateways, real-time apps with many connections, and glue services. You can still use it for CPU work if you plan for workers or native modules.

## 389: Why do Node streams use process.nextTick internally, and how can it surprise you?

Streams use `nextTick` to keep events async and in a consistent order. For example, `"end"`, `"finish"`, `"close"` and errors after `destroy()` are often emitted on the next tick, so that listeners attached right after a call still see them.

The surprise is that the exact timing differs between event types and between Node versions. Code that assumes "`"end"` fires synchronously after the last `"data"`" or that two events come in a specific tick order can break on upgrade. Use `stream.finished()` or `pipeline()` instead of guessing which event comes last.

## 390: Why are stream errors after destroy() delivered asynchronously?

When you call `stream.destroy(err)`, the stream stops immediately but emits `"error"` and `"close"` later (on `nextTick`). This gives the code that called `destroy` time to finish and gives other code a chance to attach listeners. It also prevents re-entrancy bugs where a listener runs in the middle of another stream method. A consequence: if you check for errors right after `destroy()`, you won't see them yet.

## 391: How does an HTTP agent's connection pool cause queueing?

If you set `maxSockets` on an `http.Agent` (or connections on an undici pool), requests beyond that limit wait in a JavaScript queue until a socket is free. This is a queue that doesn't show up as event loop delay or thread pool waits; requests just take longer to start. With a slow downstream API, this queue can grow a lot. Monitor pending requests per agent, use timeouts that include queue time, and size the pool for the downstream's capacity.

## 392: How does HTTP/2 change the picture for the event loop?

HTTP/2 multiplexes many streams over one TCP connection. In Node, one session's frames are all parsed on the main thread through nghttp2. A few points:

- Many requests from one client share one socket, so one client can create a lot of work quickly.
- Flow control windows decide how much data can be in flight; a slow consumer on one stream doesn't block other streams at the protocol level, but a slow synchronous handler still blocks all of them because they share the loop.
- Settings like `maxConcurrentStreams` limit how much one connection can ask for at once.

## 393: How do you safely run regexes provided by users?

- Don't run them on the main thread. Use a worker with a timeout and terminate it if it takes too long.
- Or use a linear-time engine like RE2, which doesn't support backtracking features (backreferences, lookarounds) and can't blow up exponentially.
- Limit both the pattern length and the input length.
- Validate patterns before saving them, rejecting known dangerous constructs.

## 394: Why does a while loop waiting for a flag set by a callback never end?

```js
let ready = false;
setTimeout(() => (ready = true), 100);

while (!ready) {} // never ends
```

The `setTimeout` callback can only run when the current code finishes and the loop reaches the timers phase. But the current code is the `while` loop, which waits for the callback. Neither can make progress. In Node you can't busy-wait for an async event on the same thread. Use `await` on a promise that the callback resolves.

## 395: What is the difference between a busy-wait sleep and Atomics.wait?

Both block the thread, but:

- A busy-wait (`while (Date.now() < end) {}`) keeps a CPU core at 100% the whole time.
- `Atomics.wait` puts the thread to sleep in the OS, using no CPU, and can be woken early by `Atomics.notify` from another thread.

```js
function sleepSync(ms) {
  Atomics.wait(new Int32Array(new SharedArrayBuffer(4)), 0, 0, ms);
}
```

Either way, the event loop of that thread is stopped, so this only makes sense in scripts or workers.

## 396: Can you get a deadlock in Node.js?

Yes, even without locks. Examples:

- A worker thread blocked in `Atomics.wait` for a value that the main thread will only set after receiving a message from that same worker.
- An async mutex acquired twice in the same async flow (waiting for itself).
- A connection pool of size N, where each request holds a connection and then waits for a second one: with N concurrent requests, everyone waits forever.
- Awaiting a promise that only resolves when an event is emitted, but the emitter is waiting for your code to finish first.

The symptom is usually requests that hang forever with low CPU. Timeouts on every wait help turn deadlocks into visible errors.

## 397: How do you implement an async mutex?

Chain each critical section onto a promise, so they run one after another even across `await` points:

```js
class Mutex {
  #last = Promise.resolve();

  async run(fn) {
    const prev = this.#last;
    let release;
    this.#last = new Promise((r) => (release = r));
    await prev;
    try {
      return await fn();
    } finally {
      release();
    }
  }
}

const lock = new Mutex();
await lock.run(async () => {
  const balance = await getBalance();
  await setBalance(balance - 10);
});
```

This only protects code in the same process. Across processes or servers you need a lock in the database or in Redis.

## 398: How do you avoid running the same async work twice at the same time?

Store the in-flight promise and let concurrent callers share it (request coalescing):

```js
const inflight = new Map();

function getConfig(key) {
  if (inflight.has(key)) return inflight.get(key);

  const p = loadConfigFromDb(key).finally(() => inflight.delete(key));
  inflight.set(key, p);
  return p;
}
```

Because the check and the `set` happen in the same synchronous step, no other request can sneak in between. This prevents the "thundering herd" problem when a cache entry expires and hundreds of requests try to rebuild it at once.

## 399: What happens if a producer writes to a stream faster than the consumer reads?

If the producer ignores `write()` returning `false`, data piles up in the writable's internal buffer. The event loop isn't blocked, but memory grows until the process slows down from GC or runs out of memory. With sockets, a slow client can cause this on the server for every response written without backpressure. Respect `write()`'s return value and wait for `"drain"`, or use `pipeline()`.

## 400: How do you tune highWaterMark?

`highWaterMark` sets how much data a stream buffers before applying backpressure (16 KB by default for most byte streams, 64 KB for file read streams, 16 objects in object mode).

- Larger values mean fewer callbacks and less overhead per byte, which helps throughput for big transfers, but use more memory per stream.
- Smaller values mean less memory and more responsive backpressure, but more callbacks.

With many concurrent streams, memory per stream matters more. Measure throughput and memory before changing it.

## 401: What is the difference between deep synchronous recursion and async recursion?

- Deep sync recursion uses the call stack. With enough depth, you get `RangeError: Maximum call stack size exceeded`. It also blocks the loop the whole time.
- Async recursion (a function that calls itself after `await` or from a callback) starts with a fresh stack each step, so it never overflows the stack. Other work can run between steps if each step waits on real async work.

```js
async function walk(dir) {
  for (const entry of await fs.promises.readdir(dir, { withFileTypes: true })) {
    if (entry.isDirectory()) await walk(path.join(dir, entry.name));
  }
}
```

## 402: Can async recursion leak memory?

Yes, if each call keeps a reference to the next one's promise in a growing chain. For example, an endless `async function loop() { await work(); return loop(); }` creates a chain where each promise waits for the next, and none of them can be collected. Over a long time, memory grows.

Use a plain loop instead:

```js
async function run() {
  while (!stopped) {
    await work();
  }
}
```

## 403: What happens to in-flight requests when the process crashes from an uncaught exception?

They are lost. The process exits, sockets are closed by the OS, and clients get connection resets or errors. Any work they started (DB transactions, writes) is cut off in whatever state it was in. That's why you should:

- Catch errors in request handlers so one bad request doesn't crash the process.
- Make critical operations idempotent or transactional.
- Run several instances behind a load balancer so a crash only affects some requests.
- On a fatal error, try a short graceful shutdown instead of exiting instantly, if the app state allows it.

## 404: How would you write a solid graceful shutdown?

```js
let shuttingDown = false;

app.get("/ready", (req, res) => res.status(shuttingDown ? 503 : 200).end());

async function shutdown() {
  if (shuttingDown) return;
  shuttingDown = true;

  // 1. fail readiness so the load balancer stops sending traffic
  await sleep(5000);

  // 2. stop accepting connections, close idle keep-alive ones
  const closed = new Promise((resolve) => server.close(resolve));
  server.closeIdleConnections();

  // 3. give in-flight requests time to finish, then force close
  const force = setTimeout(() => server.closeAllConnections(), 15_000);
  await closed;
  clearTimeout(force);

  // 4. close resources that keep the loop alive
  await Promise.allSettled([db.end(), redis.quit(), queue.close()]);
  process.exitCode = 0;
}

process.on("SIGTERM", shutdown);
```

If everything is closed properly, the event loop empties and the process exits by itself. If it doesn't, something is still open, which is useful to know.

## 405: What is EMFILE and how does it relate to the event loop?

`EMFILE` means the process hit its limit of open file descriptors. Every socket, file, pipe and watcher uses one. A server with many connections, or code that opens many files in parallel without a limit, can hit the default limit (often 1024). Then new connections or file opens fail.

Fixes: raise the limit (`ulimit -n`, or container settings), limit concurrency of file operations, close files and sockets reliably, and use packages like `graceful-fs` that queue and retry opens when this happens.

## 406: What happens to new connections while the event loop is blocked?

The kernel still completes TCP handshakes and puts new connections in the listen backlog queue (Node's default backlog is 511). They wait there until the loop runs the poll phase and accepts them. If the block lasts long enough for the backlog to fill, new connection attempts are dropped or refused, and clients see timeouts. Data from already-connected clients waits in kernel socket buffers.

## 407: What is Atomics.waitAsync?

`Atomics.waitAsync` is the non-blocking version of `Atomics.wait`. It returns an object whose `value` is a promise that resolves when another thread calls `Atomics.notify` on that location (or when the timeout passes). The thread's event loop keeps running in the meantime.

```js
const arr = new Int32Array(sharedBuffer);
const result = Atomics.waitAsync(arr, 0, 0, 1000);
if (result.async) {
  const status = await result.value; // "ok" or "timed-out"
}
```

It lets the main thread wait for shared-memory signals from workers without blocking.

## 408: Can MessageChannel be used to yield to the event loop?

Yes. Messages on a `MessagePort` are delivered as event loop callbacks, not microtasks, so posting a message to yourself lets I/O run in between. Browser schedulers use this trick. In Node, `setImmediate` is simpler and cheaper for the same goal. Also, a `MessagePort` with a listener keeps the process alive until you close or unref it, which is easy to forget.

## 409: How do process.nextTick, promises and setImmediate compare in cost?

Roughly, from cheapest to most expensive per call:

- `process.nextTick`: a push to a JavaScript array-based queue. Very cheap.
- `queueMicrotask` / promise callbacks: handled inside V8, also cheap, with some extra cost for promise allocation.
- `setImmediate`: creates an `Immediate` object and goes through the check phase, which also means a full loop iteration between calls if you chain them.

The difference only matters in very hot paths. Pick based on the ordering you need, not micro-benchmarks. When chunking long work, the extra cost of `setImmediate` is the price of letting I/O run.

## 410: What happens to timers and I/O when you pause in the debugger?

When execution is paused at a breakpoint, the main thread is stopped, so the event loop doesn't run. Timers become overdue, incoming data waits in kernel buffers, and clients may time out. When you resume, all overdue timers fire at once and pending I/O is processed. This can cause behavior you'd never see in production, like retry timeouts firing together. Keep it in mind when debugging timing-related bugs.

## 411: How do you tell queueing time from handler time for a request?

Record timestamps at different points:

- When the request handler starts running (from your server framework's hooks).
- When the synchronous part of the handler returns.
- When the response finishes.

Compare the start time with a timestamp taken as early as possible, for example in the `"connection"` event or from the load balancer's request start header. A large gap before your handler starts means the request waited for the event loop. A large gap inside the handler means your code or its dependencies were slow. Event loop delay metrics give you the queueing part in aggregate.

## 412: How do you use ELU for capacity planning?

Run a load test and record ELU along with throughput and latency. Usually latency stays flat while ELU is low, then rises quickly as ELU approaches 1, because work starts to queue. Find the ELU level where p99 latency is still acceptable (often around 0.7 to 0.8) and treat that as the safe capacity per process. Then scale out (more processes or pods) when ELU stays above that level, rather than scaling on CPU percentage alone.

## 413: How expensive is monitorEventLoopDelay and what does resolution mean?

`monitorEventLoopDelay` uses a libuv timer that fires every `resolution` milliseconds (10 by default) and records how late each firing was in a native histogram. The cost is one tiny timer callback per interval in C++, with no JavaScript involved, so it's fine for production. A smaller resolution catches shorter blocks but adds more wakeups. A very large resolution can miss short blocks that happen between samples.

## 414: How does diagnostics_channel relate to the event loop?

`diagnostics_channel` is a publish/subscribe API that Node core and libraries use to expose events like "HTTP request started" or "query finished". Publishing is synchronous: subscribers run right away in the publisher's call stack, like `EventEmitter`. So a slow subscriber slows down the code that publishes. Subscribers should do minimal work and defer anything heavy.

```js
const dc = require("node:diagnostics_channel");

dc.subscribe("http.server.request.start", ({ request }) => {
  request.startTime = performance.now();
});
```

## 415: Does AsyncLocalStorage context follow EventEmitter listeners?

Not the way people often expect. `emit()` is a synchronous call, so listeners run in the context of whoever called `emit`, not the context in which the listener was registered. For example, a listener added during request A but triggered by code running in request B sees request B's store (or none).

If listeners should run in the context where they were registered, bind them with `AsyncResource.bind(listener)`, or use `EventEmitterAsyncResource` from `node:events`, which runs listeners in the emitter's own async context.

## 416: How do WeakRef and FinalizationRegistry interact with the event loop?

`FinalizationRegistry` callbacks run on the main thread at some point after the garbage collector has collected the object. V8 schedules them as separate tasks, and Node runs them between other work. There is no guarantee when, or even if, they run (for example, if the process exits first). `WeakRef` targets also stay alive at least until the end of the current synchronous job. Never use either for important cleanup like closing files; use explicit `close()` calls or `using`.

## 417: Why does reading from process.stdin keep the process alive?

Once you start reading stdin (by adding a `"data"` listener, calling `resume()`, or using `readline`), stdin becomes an active handle in the event loop, waiting for input. The process won't exit until stdin ends (EOF, Ctrl+D) or you pause it or close the readline interface. CLI tools that ask a question and then hang usually forgot to call `rl.close()`.

## 418: How does Node itself run the libuv loop?

After bootstrapping and running the main script, Node runs something like this (simplified from the C++ `SpinEventLoop`):

```cpp
do {
  uv_run(loop, UV_RUN_DEFAULT);
  platform->DrainTasks(isolate);   // V8 background-task results

  more = uv_loop_alive(loop);
  if (more && !env->is_stopping()) continue;

  EmitProcessBeforeExit(env);      // JS 'beforeExit' event
  more = uv_loop_alive(loop);      // did a listener schedule new work?
} while (more && !env->is_stopping());

EmitProcessExit(env);              // JS 'exit' event
```

This is why `beforeExit` can keep the process going: if a listener schedules new work, the loop is alive again and Node goes back to `uv_run`.

## 419: When does a worker thread's event loop end?

A worker exits when its own event loop has nothing left to do, just like the main process, or when it calls `process.exit()`, or when the main thread calls `worker.terminate()`. A common surprise: `parentPort.on("message", ...)` keeps the worker's loop alive forever, because the port is an active handle. That's usually what you want for pool workers. If not, call `parentPort.close()` or `parentPort.unref()` when the worker is done.

## 420: How can you keep crypto work from starving fs operations in the thread pool?

Since both share the same pool, add your own limit on the CPU-heavy work:

```js
const crypto = require("node:crypto");
const { promisify } = require("node:util");
const scrypt = promisify(crypto.scrypt);

let running = 0;
const waiting = [];
const MAX_HASHES = 2; // leave the other pool threads free for fs and dns

async function hashPassword(pw, salt) {
  if (running >= MAX_HASHES) await new Promise((r) => waiting.push(r));
  running++;
  try {
    return await scrypt(pw, salt, 64);
  } finally {
    running--;
    waiting.shift()?.();
  }
}
```

Together with a bigger `UV_THREADPOOL_SIZE`, this keeps a login spike from slowing down every file read.

## 421: How can you tell whether an uncaught error came from a throw or a rejected promise?

The `"uncaughtException"` handler gets a second argument, `origin`, which is `"uncaughtException"` for a normal throw and `"unhandledRejection"` when an unhandled rejection was turned into an exception (the default `throw` mode).

```js
process.on("uncaughtException", (err, origin) => {
  logger.fatal({ err, origin }, "fatal error");
  process.exit(1);
});
```

This helps you find whether the bug is a missing `try/catch` or a missing `await`/`.catch`.

## 422: What happens if workers send messages while the main thread is blocked?

The messages are queued for the main thread. They can't be handled until the main loop is free. If workers keep sending (for example progress updates or results) while the main thread is blocked or just slow, the queue grows and uses memory, and when the main thread frees up it has a big burst of callbacks to process. Send fewer, bigger messages, and design a flow control step (the worker waits for an acknowledgement) if the producer can outrun the consumer.

## 423: Can you run a periodic task with sub-millisecond precision in Node?

Not with timers. Node timers work in whole milliseconds, and their callbacks are also delayed by whatever else the loop is doing and by GC. For tighter timing you would need a dedicated worker thread that busy-waits on `process.hrtime.bigint()` (burning a core), or native code. Even then, GC pauses and OS scheduling add jitter. If you really need precise timing, Node is probably not the right tool for that part.

## 424: Which Buffer operations can block the event loop?

All Buffer operations are synchronous, so with large data they can block:

- `Buffer.concat` of many chunks copies everything into a new buffer.
- `buffer.toString()` on hundreds of megabytes decodes everything at once.
- `Buffer.from(bigString)` encodes it at once.
- Searching with `indexOf` over huge buffers.

Process data in chunks as it arrives instead of collecting everything and converting it in one go.

## 425: How do you process a huge database result without blocking or running out of memory?

Use a cursor or streaming query, and handle rows in batches:

```js
const cursor = collection.find({ status: "active" }).batchSize(1000);

for await (const doc of cursor) {
  await handle(doc);
}
```

Rows are fetched in batches over the network, so memory stays bounded and the loop handles other requests between network reads. Avoid `toArray()` (or the equivalent) on queries that can return millions of rows.

## 426: How should a Node server handle a sudden burst of 10,000 requests?

- Accept them, but don't start unlimited work: put limits on DB queries, outgoing calls and CPU tasks so downstream systems and the thread pool aren't flooded.
- Use load shedding: when event loop delay or ELU crosses a threshold, return `503` quickly for new requests instead of making everyone slow.
- Set timeouts on everything, so stuck work doesn't pile up.
- Keep per-request synchronous work small.
- Scale horizontally (more processes or pods) for sustained load.

The goal is to keep latency stable for accepted requests instead of failing slowly for everyone.

## 427: How do you choose between chunking with setImmediate and using worker threads?

Use chunking when:

- The work is moderate (tens to hundreds of ms in total) and easy to split.
- You need direct access to main-thread state.
- Total throughput isn't critical, only responsiveness.

Use worker threads when:

- The work is heavy or frequent enough to use a lot of CPU.
- You want to use more cores.
- The work can't easily be split (like a single big `JSON.parse` or a library call).
- You need to be able to kill it on timeout.

Chunking keeps the loop responsive but doesn't add CPU capacity. Workers add capacity but cost startup and data copying.

## 428: Is structuredClone expensive for the event loop?

`structuredClone` is synchronous and copies the whole object graph on the main thread. For small objects it's fine. For big objects (large arrays, deep nested data, big Maps) it can take a long time and block the loop, and it doubles memory while both copies exist. The same algorithm runs when you `postMessage` to a worker. Avoid cloning large structures per request; share immutable data or transfer buffers instead.

## 429: How can you reduce GC pressure in hot paths?

- Avoid creating temporary objects and arrays in tight loops (for example, chained `map`/`filter` on big arrays creates several intermediate arrays).
- Reuse buffers where it's safe.
- Avoid string concatenation of huge strings piece by piece; use arrays and join, or streams.
- Don't keep large caches without limits; use an LRU with a size cap.
- Avoid closures that capture large objects in long-lived timers or listeners.

Less allocation means fewer scavenges and shorter pauses, which means lower event loop delay.

## 430: How can APM and tracing agents affect the event loop?

They wrap functions, patch modules and track async context, which adds work to every request. Older agents relied on `async_hooks`, which slows down promise-heavy code. Some agents also serialize and export data on the main thread. In most apps the overhead is small, but in high-throughput services it can be noticeable. Measure with and without the agent, use sampling, and prefer agents that use `diagnostics_channel` and `AsyncLocalStorage` and export from a separate thread.

## 431: How can event loop ordering cause flaky tests?

- Tests that depend on `setTimeout(0)` vs `setImmediate` order in the main module.
- Assertions right after triggering async work, which pass only when the work happens to finish in time.
- Mixing fake timers with real promises or real I/O.
- Shared state between tests that a leftover timer or callback from a previous test changes.
- Assumptions about the order of events from streams or sockets.

Fix them by awaiting the actual event or promise you care about (`events.once`, returned promises), cleaning up handles after each test, and not relying on undocumented ordering.

## 432: What should you watch for when moving code that relies on nextTick ordering to ES modules?

In an ES module, promise callbacks queued at the top level run before `nextTick` callbacks, while in CommonJS it's the other way around. Code that used `process.nextTick` to make sure something runs "before any promise callbacks" can change order after converting to ESM. The safest approach is to not depend on the order between the two queues at all: if B must run after A, call B from A or chain them with `await`. Switching such code to `queueMicrotask` also makes the order the same in both module systems.

## 433: Can microtasks run between two listeners of the same emit() call?

No. `emit()` calls all listeners one after another in a single synchronous loop. Microtasks only run when the JavaScript stack is empty, so all listeners finish before any promise callback runs. But if a listener is `async`, only its synchronous part runs during `emit`; the part after its first `await` runs later, after `emit` has returned and possibly after other listeners' async parts.

## 434: Do microtasks run between two I/O callbacks in the same poll phase?

Yes. Each I/O callback is a separate call from C++ into JavaScript, and Node drains the `nextTick` and microtask queues when each call returns. So if two sockets have data in the same poll phase, the promise continuations from the first socket's callback run before the second socket's callback starts. This is the same per-callback draining that applies to timers and immediates since Node 11.

## 435: How would you explain the event loop with a small model in code?

A simplified model in JavaScript:

```js
while (loopIsAlive()) {
  runDueTimers(); // each followed by drainTicksAndMicrotasks()
  runPendingCallbacks();
  const timeout = immediatesQueued() ? 0 : timeUntilNextTimer();
  const events = waitForIo(timeout); // epoll / kqueue / IOCP
  for (const ev of events) {
    ev.callback();
    drainTicksAndMicrotasks();
  }
  for (const im of takeImmediates()) {
    im();
    drainTicksAndMicrotasks();
  }
  runCloseCallbacks();
}

function drainTicksAndMicrotasks() {
  do {
    runAllNextTicks();
    runAllPromiseJobs();
  } while (hasNextTicks());
}
```

It leaves out details (like the libuv 1.45 change in where timers run) but shows the main ideas: phases, waiting for I/O with a timeout, and draining the queues after every callback.

## 436: Why can web streams be slower than Node streams in Node.js?

Web streams (`ReadableStream`, `WritableStream`) are built on promises. Each chunk usually goes through several promise resolutions, which means several microtasks and allocations per chunk. Node streams use callbacks and synchronous paths for much of their work. For high-throughput, small-chunk pipelines in Node, classic Node streams are usually faster. Web streams are worth it for portability with browsers and other runtimes. `Readable.toWeb()` and `Readable.fromWeb()` let you convert at the edges.

## 437: How would you investigate an incident where the event loop was blocked for 30 seconds?

1. Find out what was running: check logs around the time for slow requests, cron-like tasks, large uploads or unusual inputs.
2. Look at the metrics: was CPU at 100% on one core (JavaScript work), or was the process idle (`Atomics.wait`, sync call waiting on something, CPU throttling, the process being paused)?
3. Check GC metrics and heap size. A heap near its limit can cause back-to-back long GCs.
4. Try to reproduce with the same input and take a CPU profile.
5. Look for ReDoS-prone regexes, huge JSON payloads, sync calls in rarely used code paths, and accidental `O(n²)` loops on big data.
6. Afterwards, add protection: input size limits, a watchdog that reports long blocks, and load shedding.

## 438: How can you detect a blocked main thread from another thread?

Use a watchdog worker. The main thread updates a heartbeat value in shared memory on a timer; the worker checks it and acts when it's stale:

```js
// main.js
const { Worker } = require("node:worker_threads");
const heartbeat = new Int32Array(new SharedArrayBuffer(4));
setInterval(() => Atomics.add(heartbeat, 0, 1), 100).unref();
new Worker("./watchdog.js", { workerData: heartbeat.buffer }).unref();
```

```js
// watchdog.js
const { workerData } = require("node:worker_threads");
const hb = new Int32Array(workerData);
let last = Atomics.load(hb, 0);

setInterval(() => {
  const now = Atomics.load(hb, 0);
  if (now === last) {
    console.error("main thread blocked for over 2 s");
  }
  last = now;
}, 2000);
```

Since the worker has its own event loop, it keeps working while the main thread is stuck. It can log, send an alert, or end the process so the orchestrator restarts it.

## 439: What are the downsides of making the thread pool very large?

- Each thread reserves memory for its stack.
- If the work is CPU-bound (crypto, zlib), more threads than cores just adds context switching and competes with the main thread for CPU, which can increase event loop delay.
- Disks have limited parallelism; hundreds of parallel file operations can make each one slower.
- It can hide the real issue, like unbounded concurrency in your code.

A bigger pool helps most when the pool work is waiting (slow network file systems, slow DNS), not computing.

## 440: How much does an idle connection cost in a Node server?

An idle TCP connection is mostly a file descriptor, kernel socket buffers, a libuv handle and some JavaScript objects (the socket, maybe an HTTP parser, timers). That's a few kilobytes up to tens of kilobytes depending on buffers and what your app attaches to it. It doesn't cost any CPU while idle. This is why Node can hold tens or hundreds of thousands of idle WebSocket connections per process, as long as you watch file descriptor limits and per-connection data.

## 441: Should library code still use process.nextTick?

There are good reasons both ways:

- `nextTick` gives you "before any I/O and before promise callbacks" in CommonJS, which libraries used to keep event order consistent (streams in Node core still do).
- But its order relative to promises differs in ESM, it doesn't exist in browsers or some other runtimes, and recursive use can starve the loop.

For new library code, `queueMicrotask` is usually the better default, and `setImmediate` when you want I/O to run first. Use `nextTick` only when you specifically need its priority and are only targeting Node.

## 442: How could the TC39 AsyncContext proposal change async context in Node?

The `AsyncContext` proposal adds async context propagation (like `AsyncLocalStorage`) to the JavaScript language itself, with `AsyncContext.Variable` and `AsyncContext.Snapshot`. If it's standardized, context would flow through promises, `await` and host callbacks in every runtime, not only in Node, and engines could optimize it. Node's move to `AsyncContextFrame` already follows the same design, so `AsyncLocalStorage` would likely become a thin layer over it.

## 443: What are the main event loop changes across Node.js versions?

- **Node 11**: `nextTick` and microtasks drained after each timer and immediate callback, matching browsers.
- **Node 12**: faster `await` (one tick instead of three, from V8 7.2).
- **Node 15**: unhandled rejections crash the process by default; `timers/promises` added.
- **Node 16+**: `AbortSignal` support across many async APIs.
- **Node 18/19**: `fetch` built in; keep-alive on by default for the global HTTP agent (19); `server.close()` closes idle connections (19).
- **Node 20**: libuv 1.45, timers run after poll instead of before; io_uring support for file I/O (later made opt-in).
- **Node 23**: warnings for negative and `NaN` timer delays.
- **Node 24**: `AsyncLocalStorage` uses `AsyncContextFrame` by default.

## 444: How would you design a Node service that stays responsive under heavy mixed load?

- Keep request handlers short and I/O-bound. Measure the synchronous time of each route.
- Put CPU-heavy work in a worker pool with a bounded queue and per-job timeouts.
- Limit concurrency to every downstream (DB pool size, outgoing request limits, thread pool budgets).
- Stream large payloads instead of buffering them.
- Monitor event loop delay, ELU, GC and pool waits, and shed load when they cross thresholds.
- Run several processes or pods and scale on ELU and latency.
- Handle shutdown gracefully and every error explicitly so one bad request doesn't take the process down.

## 445: Can a setImmediate be unref'd?

Yes. The `Immediate` object returned by `setImmediate` has `ref()`, `unref()` and `hasRef()`, like timers. An unref'd immediate doesn't keep the process alive, and Node doesn't start the idle handle for it, so it also doesn't stop the poll phase from blocking. In practice that means an unref'd immediate may wait until something else wakes the loop up, or never run if the process exits first.

## 446: Why does batching reduce the overhead of crossing from C++ to JavaScript?

Every callback from the event loop into JavaScript has fixed overhead: setting up the callback scope, async context tracking, calling into V8, and the microtask checkpoint afterwards. For large chunks of work, this is negligible. For tiny events (very small socket reads, one message per row), the fixed cost can be a large share of the total. Larger chunk sizes, batched messages and fewer, bigger writes reduce the number of crossings and improve throughput.

## 447: How does the poll phase use epoll on Linux?

libuv keeps one epoll instance per loop. When a socket needs watching, libuv registers it with `epoll_ctl`. In the poll phase, libuv calls `epoll_wait` with the computed timeout, which returns a batch of file descriptors that are ready. libuv then calls the watcher callback for each, which reads or writes as much as possible without blocking and calls into JavaScript. One system call can return many ready sockets at once, which is what makes handling many connections on one thread efficient.

## 448: What happens when you call socket.write()?

libuv first tries to write the data straight away with a non-blocking system call. If the kernel's socket buffer has room, the write completes immediately. If not, libuv queues the rest and asks the OS to report when the socket becomes writable, finishing the write in a later poll phase. The `write` callback (or the `"drain"` event) tells you when the data has been handed to the kernel, not when the client received it. `socket.writableLength` shows how much is still queued, which is a good way to spot slow clients.

## 449: How do you protect a server from slow clients?

A slow client reads its responses slowly, so data piles up in your process (in the socket's write queue) for that connection. With many such clients, memory grows. Protect the server by:

- Respecting backpressure when writing responses (stream with `pipeline`, check `write()` results).
- Setting socket and request timeouts (`headersTimeout`, `requestTimeout`, `socket.setTimeout`).
- Limiting the number of concurrent connections per client at a proxy or load balancer.
- Monitoring `writableLength` for long-lived connections like WebSockets and dropping clients that fall too far behind.

## 450: What do you look for in a code review to catch event loop problems?

- Sync APIs (`*Sync`, `execSync`, `pbkdf2Sync`) in request paths.
- `JSON.parse`/`JSON.stringify`, sorting or loops over data whose size depends on user input.
- Regexes run on user input, especially with nested quantifiers.
- `Promise.all` or `map` over unbounded lists without a concurrency limit.
- Missing `await` or `.catch` (unhandled rejections), and `async` callbacks passed to `forEach` or `EventEmitter` without error handling.
- Timers, intervals, listeners and sockets that are created but never cleared or closed.
- Recursive `nextTick` or microtask loops.
- Large data read fully into memory instead of streamed.
- Heavy work in middleware that runs on every request.
