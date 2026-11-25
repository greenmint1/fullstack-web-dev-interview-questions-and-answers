# Node.js Worker Threads and Clustering Interview Questions and Answers

_Last updated: November 25, 2026_

This file has 150 interview questions and answers about Node.js worker threads and the cluster module: 50 easy, 50 moderate and 50 advanced. The answers target Node.js 24 LTS and newer. Code examples use ES modules unless a question is about CommonJS.

## Table of Contents

- [Easy Questions (1-50)](#easy-questions-1-50)
- [Moderate Questions (51-100)](#moderate-questions-51-100)
- [Advanced Questions (101-150)](#advanced-questions-101-150)

### Easy Questions (1-50)

- [1: What are worker threads in Node.js?](#1-what-are-worker-threads-in-nodejs)
- [2: What is the cluster module?](#2-what-is-the-cluster-module)
- [3: Node.js is already asynchronous. Why do we need worker threads or clustering?](#3-nodejs-is-already-asynchronous-why-do-we-need-worker-threads-or-clustering)
- [4: What is the main difference between worker threads and cluster?](#4-what-is-the-main-difference-between-worker-threads-and-cluster)
- [5: How do you create a worker thread?](#5-how-do-you-create-a-worker-thread)
- [6: What is isMainThread?](#6-what-is-ismainthread)
- [7: What is parentPort?](#7-what-is-parentport)
- [8: What is workerData?](#8-what-is-workerdata)
- [9: How do the main thread and a worker exchange messages?](#9-how-do-the-main-thread-and-a-worker-exchange-messages)
- [10: What events does a Worker object emit?](#10-what-events-does-a-worker-object-emit)
- [11: What is threadId?](#11-what-is-threadid)
- [12: How do you stop a worker thread?](#12-how-do-you-stop-a-worker-thread)
- [13: Which Node.js APIs can you use inside a worker thread?](#13-which-nodejs-apis-can-you-use-inside-a-worker-thread)
- [14: Do worker threads share memory by default?](#14-do-worker-threads-share-memory-by-default)
- [15: What is the structured clone algorithm?](#15-what-is-the-structured-clone-algorithm)
- [16: What can't you send with postMessage?](#16-what-cant-you-send-with-postmessage)
- [17: What is the difference between CPU-bound and I/O-bound work?](#17-what-is-the-difference-between-cpu-bound-and-io-bound-work)
- [18: When should you not use worker threads?](#18-when-should-you-not-use-worker-threads)
- [19: How do you create a basic cluster?](#19-how-do-you-create-a-basic-cluster)
- [20: What is cluster.isPrimary?](#20-what-is-clusterisprimary)
- [21: How many cluster workers should you start?](#21-how-many-cluster-workers-should-you-start)
- [22: How can several cluster workers listen on the same port?](#22-how-can-several-cluster-workers-listen-on-the-same-port)
- [23: What does the primary process do in a cluster?](#23-what-does-the-primary-process-do-in-a-cluster)
- [24: How do the primary and cluster workers communicate?](#24-how-do-the-primary-and-cluster-workers-communicate)
- [25: What events does the cluster module emit?](#25-what-events-does-the-cluster-module-emit)
- [26: How do you restart a cluster worker that crashed?](#26-how-do-you-restart-a-cluster-worker-that-crashed)
- [27: What are cluster.workers and cluster.worker?](#27-what-are-clusterworkers-and-clusterworker)
- [28: Does each cluster worker have its own memory?](#28-does-each-cluster-worker-have-its-own-memory)
- [29: Why are in-memory sessions a problem when you use cluster?](#29-why-are-in-memory-sessions-a-problem-when-you-use-cluster)
- [30: How does cluster balance load by default?](#30-how-does-cluster-balance-load-by-default)
- [31: What is PM2 cluster mode?](#31-what-is-pm2-cluster-mode)
- [32: What is the difference between child_process.fork() and cluster.fork()?](#32-what-is-the-difference-between-child_processfork-and-clusterfork)
- [33: What is the libuv thread pool, and how is it different from worker threads?](#33-what-is-the-libuv-thread-pool-and-how-is-it-different-from-worker-threads)
- [34: What is UV_THREADPOOL_SIZE?](#34-what-is-uv_threadpool_size)
- [35: Can you use ES modules in a worker thread?](#35-can-you-use-es-modules-in-a-worker-thread)
- [36: What does the eval option of Worker do?](#36-what-does-the-eval-option-of-worker-do)
- [37: How do you handle errors thrown inside a worker thread?](#37-how-do-you-handle-errors-thrown-inside-a-worker-thread)
- [38: What happens when process.exit() is called inside a worker thread?](#38-what-happens-when-processexit-is-called-inside-a-worker-thread)
- [39: What does the exit code in the worker 'exit' event tell you?](#39-what-does-the-exit-code-in-the-worker-exit-event-tell-you)
- [40: How do you wrap a worker thread in a Promise?](#40-how-do-you-wrap-a-worker-thread-in-a-promise)
- [41: What is a worker pool?](#41-what-is-a-worker-pool)
- [42: Why is it a bad idea to start a new worker thread for every HTTP request?](#42-why-is-it-a-bad-idea-to-start-a-new-worker-thread-for-every-http-request)
- [43: Does console.log work inside a worker thread?](#43-does-consolelog-work-inside-a-worker-thread)
- [44: Can a worker thread start its own workers?](#44-can-a-worker-thread-start-its-own-workers)
- [45: What is SharedArrayBuffer?](#45-what-is-sharedarraybuffer)
- [46: What is Atomics?](#46-what-is-atomics)
- [47: What is MessageChannel?](#47-what-is-messagechannel)
- [48: How do you check how many CPU cores the machine has?](#48-how-do-you-check-how-many-cpu-cores-the-machine-has)
- [49: Does clustering help on a machine with one CPU core?](#49-does-clustering-help-on-a-machine-with-one-cpu-core)
- [50: Can cluster workers get different environment variables or run different code?](#50-can-cluster-workers-get-different-environment-variables-or-run-different-code)

### Moderate Questions (51-100)

- [51: How do you send an ArrayBuffer to a worker without copying it?](#51-how-do-you-send-an-arraybuffer-to-a-worker-without-copying-it)
- [52: What happens to a transferred ArrayBuffer on the sending side?](#52-what-happens-to-a-transferred-arraybuffer-on-the-sending-side)
- [53: What does markAsUntransferable do?](#53-what-does-markasuntransferable-do)
- [54: Why can't you transfer the memory behind a small Buffer?](#54-why-cant-you-transfer-the-memory-behind-a-small-buffer)
- [55: How do you limit how much memory a worker thread can use?](#55-how-do-you-limit-how-much-memory-a-worker-thread-can-use)
- [56: What happens when a worker thread runs out of memory?](#56-what-happens-when-a-worker-thread-runs-out-of-memory)
- [57: How does process.env work inside a worker thread?](#57-how-does-processenv-work-inside-a-worker-thread)
- [58: What are setEnvironmentData and getEnvironmentData?](#58-what-are-setenvironmentdata-and-getenvironmentdata)
- [59: What do ref() and unref() do on a Worker?](#59-what-do-ref-and-unref-do-on-a-worker)
- [60: How would you build a simple worker pool yourself?](#60-how-would-you-build-a-simple-worker-pool-yourself)
- [61: What is Piscina, and why would you use it?](#61-what-is-piscina-and-why-would-you-use-it)
- [62: Which Piscina options do you usually tune?](#62-which-piscina-options-do-you-usually-tune)
- [63: How do you cancel a task that is running in a Piscina pool?](#63-how-do-you-cancel-a-task-that-is-running-in-a-piscina-pool)
- [64: How do you give a worker its own MessagePort?](#64-how-do-you-give-a-worker-its-own-messageport)
- [65: How can two worker threads talk to each other directly?](#65-how-can-two-worker-threads-talk-to-each-other-directly)
- [66: What is BroadcastChannel in worker_threads?](#66-what-is-broadcastchannel-in-worker_threads)
- [67: What is receiveMessageOnPort?](#67-what-is-receivemessageonport)
- [68: When is the 'messageerror' event emitted?](#68-when-is-the-messageerror-event-emitted)
- [69: How do the stdout, stderr and stdin options of Worker work?](#69-how-do-the-stdout-stderr-and-stdin-options-of-worker-work)
- [70: How can you see how busy a worker thread is?](#70-how-can-you-see-how-busy-a-worker-thread-is)
- [71: How do you shut down a cluster gracefully?](#71-how-do-you-shut-down-a-cluster-gracefully)
- [72: What is the difference between worker.kill() and worker.disconnect() in cluster?](#72-what-is-the-difference-between-workerkill-and-workerdisconnect-in-cluster)
- [73: What is worker.exitedAfterDisconnect and why does it matter?](#73-what-is-workerexitedafterdisconnect-and-why-does-it-matter)
- [74: How do you restart a cluster app with zero downtime?](#74-how-do-you-restart-a-cluster-app-with-zero-downtime)
- [75: How do you avoid a crash loop in a cluster?](#75-how-do-you-avoid-a-crash-loop-in-a-cluster)
- [76: How do you change the cluster scheduling policy?](#76-how-do-you-change-the-cluster-scheduling-policy)
- [77: What does cluster.setupPrimary() do?](#77-what-does-clustersetupprimary-do)
- [78: How do you run a scheduled job only once when the app runs in cluster mode?](#78-how-do-you-run-a-scheduled-job-only-once-when-the-app-runs-in-cluster-mode)
- [79: How do you share a cache across cluster workers?](#79-how-do-you-share-a-cache-across-cluster-workers)
- [80: How do WebSockets and Socket.IO work with cluster?](#80-how-do-websockets-and-socketio-work-with-cluster)
- [81: What are sticky sessions?](#81-what-are-sticky-sessions)
- [82: Should you use cluster or several containers behind a load balancer?](#82-should-you-use-cluster-or-several-containers-behind-a-load-balancer)
- [83: What should you watch out for when using cluster inside a container?](#83-what-should-you-watch-out-for-when-using-cluster-inside-a-container)
- [84: How do you debug worker threads and cluster workers?](#84-how-do-you-debug-worker-threads-and-cluster-workers)
- [85: How do you pass command line flags and arguments to a worker thread?](#85-how-do-you-pass-command-line-flags-and-arguments-to-a-worker-thread)
- [86: Can you run a TypeScript file in a worker thread?](#86-can-you-run-a-typescript-file-in-a-worker-thread)
- [87: How do you test code that uses worker threads?](#87-how-do-you-test-code-that-uses-worker-threads)
- [88: What happens when you send a class instance to a worker thread?](#88-what-happens-when-you-send-a-class-instance-to-a-worker-thread)
- [89: How do you handle uncaught exceptions in cluster workers?](#89-how-do-you-handle-uncaught-exceptions-in-cluster-workers)
- [90: When would you use child_process instead of worker threads for CPU work?](#90-when-would-you-use-child_process-instead-of-worker-threads-for-cpu-work)
- [91: How do you match replies to requests when you send many messages to one worker?](#91-how-do-you-match-replies-to-requests-when-you-send-many-messages-to-one-worker)
- [92: How much does postMessage cost for large objects?](#92-how-much-does-postmessage-cost-for-large-objects)
- [93: Can worker threads share one database connection pool?](#93-can-worker-threads-share-one-database-connection-pool)
- [94: How does clustering affect database connection counts?](#94-how-does-clustering-affect-database-connection-counts)
- [95: How do you handle logs from many cluster workers?](#95-how-do-you-handle-logs-from-many-cluster-workers)
- [96: What is the difference between the 'online' and 'listening' events in cluster?](#96-what-is-the-difference-between-the-online-and-listening-events-in-cluster)
- [97: How do you send a message to every cluster worker?](#97-how-do-you-send-a-message-to-every-cluster-worker)
- [98: What happens when you call server.listen() inside a cluster worker?](#98-what-happens-when-you-call-serverlisten-inside-a-cluster-worker)
- [99: How do you put the main thread code and the worker code in the same file?](#99-how-do-you-put-the-main-thread-code-and-the-worker-code-in-the-same-file)
- [100: How do you add backpressure when sending tasks to a worker pool?](#100-how-do-you-add-backpressure-when-sending-tasks-to-a-worker-pool)

### Advanced Questions (101-150)

- [101: How are worker threads built internally?](#101-how-are-worker-threads-built-internally)
- [102: What is shared between worker threads in one process, and what is not?](#102-what-is-shared-between-worker-threads-in-one-process-and-what-is-not)
- [103: Why does starting a worker thread take time and memory?](#103-why-does-starting-a-worker-thread-take-time-and-memory)
- [104: How does round-robin load balancing work inside the cluster module?](#104-how-does-round-robin-load-balancing-work-inside-the-cluster-module)
- [105: Why did the cluster module move away from letting the OS pick the worker?](#105-why-did-the-cluster-module-move-away-from-letting-the-os-pick-the-worker)
- [106: Why isn't round-robin the default on Windows?](#106-why-isnt-round-robin-the-default-on-windows)
- [107: What is the reusePort option, and how does it compare to cluster?](#107-what-is-the-reuseport-option-and-how-does-it-compare-to-cluster)
- [108: What happens if cluster workers call server.listen(0)?](#108-what-happens-if-cluster-workers-call-serverlisten0)
- [109: What does exclusive: true do in server.listen() in a cluster worker?](#109-what-does-exclusive-true-do-in-serverlisten-in-a-cluster-worker)
- [110: How do you build a simple mutex with Atomics?](#110-how-do-you-build-a-simple-mutex-with-atomics)
- [111: Can you call Atomics.wait() on the Node.js main thread?](#111-can-you-call-atomicswait-on-the-nodejs-main-thread)
- [112: How do you avoid race conditions with SharedArrayBuffer?](#112-how-do-you-avoid-race-conditions-with-sharedarraybuffer)
- [113: Why do you need Atomics even for simple reads and writes on shared memory?](#113-why-do-you-need-atomics-even-for-simple-reads-and-writes-on-shared-memory)
- [114: What does Atomics.waitAsync() do?](#114-what-does-atomicswaitasync-do)
- [115: How can you make a synchronous call to a worker thread?](#115-how-can-you-make-a-synchronous-call-to-a-worker-thread)
- [116: How do you design a worker pool that survives crashed workers?](#116-how-do-you-design-a-worker-pool-that-survives-crashed-workers)
- [117: How do you decide how many threads a worker pool should have?](#117-how-do-you-decide-how-many-threads-a-worker-pool-should-have)
- [118: How do worker threads interact with the libuv thread pool?](#118-how-do-worker-threads-interact-with-the-libuv-thread-pool)
- [119: What problems can native addons cause in worker threads?](#119-what-problems-can-native-addons-cause-in-worker-threads)
- [120: How do you put a timeout on a task that runs in a worker thread?](#120-how-do-you-put-a-timeout-on-a-task-that-runs-in-a-worker-thread)
- [121: What happens to the code running in a worker when you call terminate()?](#121-what-happens-to-the-code-running-in-a-worker-when-you-call-terminate)
- [122: What happens to messages that are in flight when a worker exits?](#122-what-happens-to-messages-that-are-in-flight-when-a-worker-exits)
- [123: How do you take a heap snapshot of a worker thread?](#123-how-do-you-take-a-heap-snapshot-of-a-worker-thread)
- [124: How do you find a memory leak in one of many cluster workers?](#124-how-do-you-find-a-memory-leak-in-one-of-many-cluster-workers)
- [125: How does clustering affect memory use and garbage collection?](#125-how-does-clustering-affect-memory-use-and-garbage-collection)
- [126: Why might clustering not make a slow app any faster?](#126-why-might-clustering-not-make-a-slow-app-any-faster)
- [127: An Express endpoint generates PDF reports and makes other requests slow. How would you fix it?](#127-an-express-endpoint-generates-pdf-reports-and-makes-other-requests-slow-how-would-you-fix-it)
- [128: When would you use a job queue like BullMQ instead of worker threads?](#128-when-would-you-use-a-job-queue-like-bullmq-instead-of-worker-threads)
- [129: How does postMessage compare with SharedArrayBuffer for performance?](#129-how-does-postmessage-compare-with-sharedarraybuffer-for-performance)
- [130: How do you stream data to or from a worker thread?](#130-how-do-you-stream-data-to-or-from-a-worker-thread)
- [131: Are worker threads a security sandbox for running untrusted code?](#131-are-worker-threads-a-security-sandbox-for-running-untrusted-code)
- [132: How is the vm module different from worker threads?](#132-how-is-the-vm-module-different-from-worker-threads)
- [133: How do you give many workers access to a large read-only dataset?](#133-how-do-you-give-many-workers-access-to-a-large-read-only-dataset)
- [134: How should a cluster app handle SIGTERM in Kubernetes?](#134-how-should-a-cluster-app-handle-sigterm-in-kubernetes)
- [135: Does the primary automatically pass signals to cluster workers?](#135-does-the-primary-automatically-pass-signals-to-cluster-workers)
- [136: How can you pass a server or socket handle between processes without cluster?](#136-how-can-you-pass-a-server-or-socket-handle-between-processes-without-cluster)
- [137: Why can sticky sessions by IP address lead to uneven load?](#137-why-can-sticky-sessions-by-ip-address-lead-to-uneven-load)
- [138: How do you give one cluster worker a special role, like running background jobs?](#138-how-do-you-give-one-cluster-worker-a-special-role-like-running-background-jobs)
- [139: How do you collect Prometheus metrics from all cluster workers?](#139-how-do-you-collect-prometheus-metrics-from-all-cluster-workers)
- [140: What happens if a worker thread throws and the main thread has no 'error' listener?](#140-what-happens-if-a-worker-thread-throws-and-the-main-thread-has-no-error-listener)
- [141: What is advanced serialization in cluster and child_process?](#141-what-is-advanced-serialization-in-cluster-and-child_process)
- [142: Why can posting a huge message still block the main thread?](#142-why-can-posting-a-huge-message-still-block-the-main-thread)
- [143: How do you find code that should be moved to a worker thread?](#143-how-do-you-find-code-that-should-be-moved-to-a-worker-thread)
- [144: You can't send functions to a worker. How do you run different kinds of tasks in one pool?](#144-you-cant-send-functions-to-a-worker-how-do-you-run-different-kinds-of-tasks-in-one-pool)
- [145: How would you design an image processing service on an 8-core server?](#145-how-would-you-design-an-image-processing-service-on-an-8-core-server)
- [146: How can a cluster primary become a bottleneck?](#146-how-can-a-cluster-primary-become-a-bottleneck)
- [147: What happens to open keep-alive connections when you disconnect a cluster worker?](#147-what-happens-to-open-keep-alive-connections-when-you-disconnect-a-cluster-worker)
- [148: How do you keep an in-memory state consistent across cluster workers if you can't use Redis?](#148-how-do-you-keep-an-in-memory-state-consistent-across-cluster-workers-if-you-cant-use-redis)
- [149: What are common mistakes with worker threads?](#149-what-are-common-mistakes-with-worker-threads)
- [150: What are common mistakes with the cluster module?](#150-what-are-common-mistakes-with-the-cluster-module)

---

# Easy Questions (1-50)

## 1: What are worker threads in Node.js?

Worker threads let you run JavaScript in parallel inside one Node.js process. Each worker has its own V8 instance, its own event loop and its own memory heap, so a heavy calculation in a worker does not block the main thread. They come from the built-in `node:worker_threads` module and are stable since Node.js 12.

## 2: What is the cluster module?

The `node:cluster` module starts several Node.js processes that run the same app and share one server port. There is one primary process that starts and watches the workers, and the workers handle the actual requests. It is the built-in way to use all CPU cores for an HTTP server.

## 3: Node.js is already asynchronous. Why do we need worker threads or clustering?

Async I/O only helps while the code is waiting for the network or the disk. Your JavaScript itself still runs on one thread. If a request does something CPU-heavy, like hashing, image resizing or parsing a huge JSON file, every other request waits. Workers move that work off the main thread, and cluster runs more copies of the app so more cores do work at the same time.

## 4: What is the main difference between worker threads and cluster?

Worker threads are threads inside one process. They are cheaper to start and can share memory through `SharedArrayBuffer`. Cluster workers are separate OS processes with completely separate memory, and they talk to each other through IPC. You use cluster to scale a server across cores, and worker threads to offload CPU-heavy tasks.

## 5: How do you create a worker thread?

Create a `Worker` and give it the path to a script. The worker sends results back with `parentPort.postMessage`.

```js
// main.js
import { Worker } from "node:worker_threads";

const worker = new Worker(new URL("./worker.js", import.meta.url), {
  workerData: { n: 40 },
});

worker.on("message", (result) => console.log("result:", result));
worker.on("error", (err) => console.error(err));
```

```js
// worker.js
import { parentPort, workerData } from "node:worker_threads";

function fib(n) {
  return n < 2 ? n : fib(n - 1) + fib(n - 2);
}

parentPort.postMessage(fib(workerData.n));
```

## 6: What is isMainThread?

`isMainThread` is a boolean from `node:worker_threads`. It is `true` in the main thread and `false` inside a worker. People use it when one file contains both the main code and the worker code.

## 7: What is parentPort?

`parentPort` is the message port a worker uses to talk to the thread that created it. You call `parentPort.postMessage()` to send data and `parentPort.on('message', ...)` to receive it. In the main thread `parentPort` is `null`.

## 8: What is workerData?

`workerData` is a value you pass in the `Worker` options when you create the worker. The worker reads it from `workerData` in `node:worker_threads`. It is a copy made with the structured clone algorithm, so changes in the worker do not affect the original object.

## 9: How do the main thread and a worker exchange messages?

Both sides use `postMessage()` to send and a `'message'` listener to receive. The main thread calls `worker.postMessage()` and listens with `worker.on('message')`. The worker uses `parentPort.postMessage()` and `parentPort.on('message')`. Messages are copied, not shared, unless you transfer them or use `SharedArrayBuffer`.

## 10: What events does a Worker object emit?

- `'online'`: the worker started running JavaScript.
- `'message'`: the worker sent a message.
- `'messageerror'`: a message could not be deserialized.
- `'error'`: an uncaught exception happened in the worker.
- `'exit'`: the worker stopped. The listener gets the exit code.

## 11: What is threadId?

Every worker gets a unique integer `threadId`. Inside the worker you read it from `threadId` in `node:worker_threads`, and in the main thread from `worker.threadId`. The main thread's `threadId` is `0`. It is handy for logs.

## 12: How do you stop a worker thread?

Call `worker.terminate()`. It stops the worker as soon as possible and returns a Promise that resolves with the exit code. A worker also stops on its own when it has nothing left to do, or when it calls `process.exit()`.

```js
const code = await worker.terminate();
console.log("worker stopped with code", code);
```

## 13: Which Node.js APIs can you use inside a worker thread?

Almost all of them: `fs`, `http`, `crypto`, timers, `fetch`, npm packages and so on. A few process-wide things are limited. For example, `process.chdir()` is not available, and you cannot set signal handlers with `process.on('SIGINT')` inside a worker. There is also no DOM, because this is Node.js, not a browser.

## 14: Do worker threads share memory by default?

No. Each worker has its own heap, so normal objects and variables are not shared. When you post a message, the data is copied. The exception is `SharedArrayBuffer`, which all threads that have it can read and write at the same time.

## 15: What is the structured clone algorithm?

It is the algorithm `postMessage()` uses to copy data between threads. It supports plain objects, arrays, `Date`, `RegExp`, `Map`, `Set`, typed arrays, `ArrayBuffer`, `Error` objects and more. It handles circular references. You can try it yourself with the global `structuredClone()` function.

## 16: What can't you send with postMessage?

Functions cannot be cloned, and trying throws a `DataCloneError`. Class instances arrive as plain objects, so their methods and prototype are lost. Symbols, getters and DOM-like host objects are not copied either. Send plain data and rebuild objects on the other side if needed.

## 17: What is the difference between CPU-bound and I/O-bound work?

CPU-bound work keeps the processor busy, like math, compression, encryption or image processing. I/O-bound work mostly waits, like database queries, HTTP calls or reading files. Node.js handles I/O-bound work well on a single thread. CPU-bound work is where worker threads help.

## 18: When should you not use worker threads?

Don't use them for I/O work like database calls or HTTP requests. Node.js already handles those without blocking, and a worker only adds startup cost and message copying. Also skip them for tiny tasks, where sending the data back and forth takes longer than doing the work on the main thread.

## 19: How do you create a basic cluster?

```js
import cluster from "node:cluster";
import http from "node:http";
import { availableParallelism } from "node:os";

if (cluster.isPrimary) {
  for (let i = 0; i < availableParallelism(); i++) {
    cluster.fork();
  }
  cluster.on("exit", (worker, code) => {
    console.log(`worker ${worker.process.pid} exited with ${code}`);
  });
} else {
  http
    .createServer((req, res) => res.end(`hello from ${process.pid}\n`))
    .listen(3000);
}
```

The same file runs in the primary and in every worker. `cluster.isPrimary` decides which branch runs.

## 20: What is cluster.isPrimary?

`cluster.isPrimary` is `true` in the process that started the cluster and `false` in forked workers. `cluster.isWorker` is the opposite. Older code uses `cluster.isMaster`, which is deprecated since Node.js 16 but still works.

## 21: How many cluster workers should you start?

A common default is one worker per CPU core. Use `os.availableParallelism()`, which is the recommended API since Node.js 18.14. Older code uses `os.cpus().length`. Some teams leave one core free for the OS or other processes. In the end, measure under real load.

## 22: How can several cluster workers listen on the same port?

When a worker calls `server.listen(3000)`, it doesn't really bind the port itself. It asks the primary over IPC. The primary opens the port once and either hands out incoming connections (round-robin) or shares the listening socket with the workers. So many processes can serve one port without an `EADDRINUSE` error.

## 23: What does the primary process do in a cluster?

It forks workers, watches them and restarts them when they die. With the default round-robin policy it also accepts incoming connections and passes them to workers. Usually it does not handle requests itself and stays small and simple.

## 24: How do the primary and cluster workers communicate?

Through an IPC channel that Node.js sets up for every forked worker. The primary calls `worker.send(message)` and listens with `worker.on('message')`. A worker calls `process.send(message)` and listens with `process.on('message')`. Messages are serialized as JSON by default.

```js
// primary
worker.send({ type: "config", debug: true });

// worker
process.on("message", (msg) => {
  if (msg.type === "config") console.log("got config", msg);
});
```

## 25: What events does the cluster module emit?

On the `cluster` object in the primary:

- `'fork'`: a new worker was forked.
- `'online'`: the worker started running.
- `'listening'`: the worker called `listen()` and the server is ready.
- `'disconnect'`: the worker's IPC channel closed.
- `'exit'`: the worker process died.
- `'message'`: a worker sent a message.

## 26: How do you restart a cluster worker that crashed?

Listen for `'exit'` in the primary and fork a new one. Skip the restart if the worker was stopped on purpose.

```js
cluster.on("exit", (worker, code, signal) => {
  if (!worker.exitedAfterDisconnect) {
    console.log(`worker ${worker.process.pid} died, starting a new one`);
    cluster.fork();
  }
});
```

## 27: What are cluster.workers and cluster.worker?

`cluster.workers` exists in the primary. It is an object of all live workers keyed by their id. `cluster.worker` exists in a worker process and points to the current worker's own `Worker` object, so you can read things like `cluster.worker.id`.

## 28: Does each cluster worker have its own memory?

Yes. Each worker is a full Node.js process with its own heap, its own globals and its own module cache. A variable you change in one worker does not change in the others. Memory usage of the whole app grows roughly with the number of workers.

## 29: Why are in-memory sessions a problem when you use cluster?

Requests from the same user can land on different workers. If the session lives in a `Map` inside one worker, the next request may go to a worker that has never seen it, and the user looks logged out. Store sessions, caches and rate-limit counters in a shared store like Redis or a database.

## 30: How does cluster balance load by default?

On every platform except Windows, the default is round-robin. The primary accepts each connection and hands it to the next worker in turn. On Windows the default is to let the OS decide which worker accepts the connection.

## 31: What is PM2 cluster mode?

PM2 is a popular process manager for Node.js. In cluster mode it uses the cluster module for you, so you don't write the primary code yourself. `pm2 start app.js -i max` starts one instance per CPU, and `pm2 reload app` restarts them one by one without downtime.

## 32: What is the difference between child_process.fork() and cluster.fork()?

`cluster.fork()` is built on top of `child_process.fork()`. Both start a new Node.js process with an IPC channel. `cluster.fork()` adds server port sharing, connection distribution and the cluster events. Use `child_process.fork()` when you just need a separate Node.js process that does not serve the same port.

## 33: What is the libuv thread pool, and how is it different from worker threads?

libuv has a small pool of C++ threads that Node.js uses for some async work: file system calls, DNS lookups with `dns.lookup`, some `crypto` functions and `zlib`. You can't run your own JavaScript on it. Worker threads run your JavaScript code in parallel. The two are separate things.

## 34: What is UV_THREADPOOL_SIZE?

It is an environment variable that sets the size of the libuv thread pool. The default is 4 and the maximum is 1024. If your app does many parallel `fs` or `crypto.pbkdf2` calls, a bigger pool can help. Set it before the process starts, for example `UV_THREADPOOL_SIZE=8 node app.js`.

## 35: Can you use ES modules in a worker thread?

Yes. Pass a file URL or a path to an `.mjs` file, or a `.js` file in a package with `"type": "module"`. The usual pattern is `new URL('./worker.js', import.meta.url)`, because ES modules have no `__dirname`. The worker file can use `import` and top-level `await`.

## 36: What does the eval option of Worker do?

With `eval: true`, the first argument is treated as JavaScript source code, not a file path. It is useful for quick tests or very small workers. The code runs as CommonJS.

```js
import { Worker } from "node:worker_threads";

const code = `
  const { parentPort } = require('node:worker_threads');
  parentPort.postMessage(2 + 2);
`;
new Worker(code, { eval: true }).on("message", console.log); // 4
```

## 37: How do you handle errors thrown inside a worker thread?

Inside the worker, wrap risky code in `try/catch` and send an error message back if you want the worker to keep running. If an exception is not caught, the worker stops and the `Worker` object in the main thread emits `'error'` with that error, followed by `'exit'`. Always attach an `'error'` listener.

## 38: What happens when process.exit() is called inside a worker thread?

Only that worker stops, not the whole process. The `Worker` object in the main thread then emits `'exit'` with the code you passed. This is different from calling `process.exit()` in the main thread, which ends everything.

## 39: What does the exit code in the worker 'exit' event tell you?

`0` usually means the worker finished normally. `1` is used when the worker died from an uncaught exception. If you called `worker.terminate()`, the code is `1`. A custom code means the worker called `process.exit(code)` itself.

## 40: How do you wrap a worker thread in a Promise?

```js
import { Worker } from "node:worker_threads";

function runWorker(file, data) {
  return new Promise((resolve, reject) => {
    const worker = new Worker(file, { workerData: data });
    worker.once("message", resolve);
    worker.once("error", reject);
    worker.once("exit", (code) => {
      if (code !== 0) reject(new Error(`Worker stopped with code ${code}`));
    });
  });
}

const result = await runWorker(new URL("./worker.js", import.meta.url), {
  n: 40,
});
```

This creates a new worker for every call, which is fine for rare jobs. For frequent jobs, use a pool.

## 41: What is a worker pool?

A worker pool is a fixed set of workers that stay alive and take tasks from a queue. When a worker finishes a task, it picks up the next one. This avoids the cost of starting a new worker every time and limits how many threads run at once. Libraries like Piscina give you a ready-made pool.

## 42: Why is it a bad idea to start a new worker thread for every HTTP request?

Starting a worker means booting a new V8 instance and Node.js environment, which takes several milliseconds and a few megabytes of memory. Under load you could end up with hundreds of threads fighting over a few cores. Use a pool with a limited size instead.

## 43: Does console.log work inside a worker thread?

Yes. By default the worker's `stdout` and `stderr` are piped to the main thread's output. The output is passed through the main thread asynchronously, so if the main thread is blocked, worker logs show up late. Logs can also be lost if the process exits right after.

## 44: Can a worker thread start its own workers?

Yes. A worker can create nested workers the same way the main thread does. In practice it's rarely needed and makes the code harder to follow. A single pool managed by the main thread is usually simpler.

## 45: What is SharedArrayBuffer?

A `SharedArrayBuffer` is a block of raw memory that several threads can see at the same time. When you post it to a worker, it is not copied: both sides point to the same memory. You read and write it through typed arrays like `Int32Array`.

## 46: What is Atomics?

`Atomics` is a global object with methods for safe operations on shared memory, like `Atomics.add`, `Atomics.load`, `Atomics.store` and `Atomics.compareExchange`. Each operation finishes fully before another thread can touch the same value. It also has `Atomics.wait` and `Atomics.notify` to let threads sleep and wake each other.

## 47: What is MessageChannel?

`MessageChannel` creates a pair of connected ports, `port1` and `port2`. A message posted on one port arrives on the other. You can transfer one port to a worker to get a private channel, or give each port to a different worker so they can talk directly.

## 48: How do you check how many CPU cores the machine has?

Use `os.availableParallelism()`. It returns how many threads the program can really run in parallel. `os.cpus().length` also works on most machines, but it can return `0` on some systems, so the newer function is safer.

```js
import { availableParallelism } from "node:os";
console.log(availableParallelism());
```

## 49: Does clustering help on a machine with one CPU core?

Not for throughput. Only one process can run at a time, so more workers just take turns and add memory and context-switch overhead. The only small benefit is that one crashed worker does not take the whole app down while another restarts.

## 50: Can cluster workers get different environment variables or run different code?

Yes. `cluster.fork(env)` takes an object of extra environment variables for that worker. To run a different script than the main one, call `cluster.setupPrimary({ exec: 'worker.js' })` before forking.

```js
cluster.fork({ ROLE: "scheduler" });
cluster.fork({ ROLE: "web" });
```

# Moderate Questions (51-100)

## 51: How do you send an ArrayBuffer to a worker without copying it?

Pass it in the transfer list, the second argument of `postMessage()`. Ownership moves to the receiver, so no copy is made. This is much faster for large binary data like images or audio.

```js
const buf = new ArrayBuffer(50 * 1024 * 1024);
worker.postMessage({ buf }, [buf]);
console.log(buf.byteLength); // 0, the buffer now belongs to the worker
```

## 52: What happens to a transferred ArrayBuffer on the sending side?

It becomes detached. Its `byteLength` is `0`, and any typed array on top of it has length `0`. You can't read or write it anymore. If you still need the data in the sender, you have to copy it instead of transferring it.

## 53: What does markAsUntransferable do?

`markAsUntransferable(object)` from `node:worker_threads` marks an `ArrayBuffer` so it is always copied, never transferred, even if it is put in a transfer list. Node.js uses this for its internal Buffer pool. You can use it for a buffer that other parts of your code still depend on. `isMarkedAsUntransferable()` checks the flag.

## 54: Why can't you transfer the memory behind a small Buffer?

Small Buffers made with `Buffer.from()` or `Buffer.allocUnsafe()` often live inside a shared pool, one big `ArrayBuffer` used by many Buffers. Transferring it would break all the others, so Node.js marks the pool as untransferable and copies instead. If you want a real transfer, create the memory yourself with `new ArrayBuffer()` or `Buffer.alloc()`.

## 55: How do you limit how much memory a worker thread can use?

Use the `resourceLimits` option. Values are in megabytes.

```js
const worker = new Worker(file, {
  resourceLimits: {
    maxOldGenerationSizeMb: 256,
    maxYoungGenerationSizeMb: 32,
    codeRangeSizeMb: 16,
    stackSizeMb: 4,
  },
});
```

These limits apply to the JavaScript heap of that worker only. Memory used outside the heap, like `ArrayBuffer` contents, is not counted.

## 56: What happens when a worker thread runs out of memory?

If the worker hits its `resourceLimits`, Node.js stops that worker and emits `'error'` with an `ERR_WORKER_OUT_OF_MEMORY` error, then `'exit'`. The main thread and other workers keep running. Without limits, a worker can grow until the whole process runs out of memory and crashes.

## 57: How does process.env work inside a worker thread?

By default each worker gets its own copy of the parent's `process.env` at the moment it was created. Changes in the worker are not seen by the parent, and the other way around. Pass `env: SHARE_ENV` to make the worker and parent share one `process.env`. You can also pass your own object as `env`.

```js
import { Worker, SHARE_ENV } from "node:worker_threads";
new Worker(file, { env: SHARE_ENV });
```

## 58: What are setEnvironmentData and getEnvironmentData?

They let you set values that every new worker can read without passing them in `workerData`. You call `setEnvironmentData(key, value)` in the parent, and the worker reads it with `getEnvironmentData(key)`. Values are cloned into each new worker when it starts. Good for small shared config.

```js
// main
import { setEnvironmentData } from "node:worker_threads";
setEnvironmentData("region", "eu-west-1");

// worker
import { getEnvironmentData } from "node:worker_threads";
console.log(getEnvironmentData("region"));
```

## 59: What do ref() and unref() do on a Worker?

A running worker keeps the main event loop alive, so the process won't exit while it runs. `worker.unref()` tells Node.js not to wait for that worker. If nothing else is going on, the process can exit and the worker is stopped. `worker.ref()` undoes it. Message ports have the same methods.

## 60: How would you build a simple worker pool yourself?

Keep an array of idle workers and a queue of tasks. When a task comes in, give it to an idle worker or queue it. When a worker replies, resolve the task's promise and give the worker the next queued task.

```js
import { Worker } from "node:worker_threads";

export class Pool {
  constructor(file, size) {
    this.file = file;
    this.idle = [];
    this.queue = [];
    for (let i = 0; i < size; i++) this.idle.push(new Worker(file));
  }

  run(data) {
    return new Promise((resolve, reject) => {
      this.queue.push({ data, resolve, reject });
      this.next();
    });
  }

  next() {
    if (!this.idle.length || !this.queue.length) return;
    const worker = this.idle.pop();
    const task = this.queue.shift();
    const done = (w) => {
      worker.off("message", onMessage);
      worker.off("error", onError);
      this.idle.push(w);
      this.next();
    };
    const onMessage = (result) => {
      done(worker);
      task.resolve(result);
    };
    // A worker with an uncaught error is dead, so replace it.
    const onError = (err) => {
      done(new Worker(this.file));
      task.reject(err);
    };
    worker.once("message", onMessage);
    worker.once("error", onError);
    worker.postMessage(task.data);
  }
}
```

This version has no timeouts and no shutdown method. In real projects a library like Piscina is usually the better choice.

## 61: What is Piscina, and why would you use it?

Piscina is a popular worker pool library for Node.js, maintained by people from the Node.js project. It handles the queue, the number of threads, idle timeouts, task cancellation, transfers and replacing crashed workers. The worker file just exports a function, and you call `pool.run(data)`.

```js
// main.js
import { Piscina } from "piscina";

const pool = new Piscina({
  filename: new URL("./task.js", import.meta.url).href,
});
console.log(await pool.run({ a: 2, b: 3 }));
```

```js
// task.js
export default ({ a, b }) => a + b;
```

## 62: Which Piscina options do you usually tune?

- `minThreads` and `maxThreads`: how many workers to keep and the upper limit.
- `idleTimeout`: how long an idle worker lives before it is stopped.
- `maxQueue`: how many tasks can wait. When it is full, `run()` rejects, which gives you backpressure.
- `concurrentTasksPerWorker`: allow more than one task per worker, useful only when the task code is async.
- `resourceLimits`: memory limits passed to each worker.

## 63: How do you cancel a task that is running in a Piscina pool?

Pass an `AbortSignal` to `run()`. If the task is still queued, it is removed. If it is already running, Piscina terminates that worker and starts a new one, because there is no other way to stop running synchronous code.

```js
const ac = new AbortController();
const promise = pool.run(data, { signal: ac.signal });
setTimeout(() => ac.abort(), 5000);

try {
  await promise;
} catch (err) {
  if (err.name === "AbortError") console.log("task cancelled");
}
```

## 64: How do you give a worker its own MessagePort?

Create a `MessageChannel`, keep one port and send the other to the worker in the transfer list. Ports must be transferred, not cloned.

```js
import { Worker, MessageChannel } from "node:worker_threads";

const { port1, port2 } = new MessageChannel();
const worker = new Worker(file);
worker.postMessage({ port: port2 }, [port2]);
port1.on("message", (msg) => console.log("from worker:", msg));
```

```js
// worker
import { parentPort } from "node:worker_threads";
parentPort.once("message", ({ port }) => port.postMessage("hello"));
```

## 65: How can two worker threads talk to each other directly?

Create a `MessageChannel` in the main thread and transfer `port1` to one worker and `port2` to the other. After that, their messages go straight between them without passing through the main thread's code. This keeps the main thread free.

## 66: What is BroadcastChannel in worker_threads?

`BroadcastChannel` lets any thread send a message to all other threads that opened a channel with the same name. You don't need to pass ports around. It's useful for things like "clear your cache" or "config changed" messages to every worker. Remember to call `close()` when done, otherwise it keeps the thread alive.

```js
import { BroadcastChannel } from "node:worker_threads";

const bc = new BroadcastChannel("events");
bc.onmessage = (event) => console.log(event.data);
bc.postMessage({ type: "reload-config" });
```

## 67: What is receiveMessageOnPort?

`receiveMessageOnPort(port)` reads one message from a port synchronously. It returns `{ message }` if there was one, or `undefined` if the queue is empty. It's mainly used together with `Atomics.wait` when you need a blocking, synchronous answer from another thread.

## 68: When is the 'messageerror' event emitted?

When a message arrives but can't be deserialized on the receiving side. For example, an object whose class is not available on that side, or a failure while rebuilding a host object. The message is dropped and `'messageerror'` is emitted instead of `'message'`. It's rare, but worth logging.

## 69: How do the stdout, stderr and stdin options of Worker work?

By default worker output goes straight to the parent's `process.stdout` and `process.stderr`. With `stdout: true` or `stderr: true`, it is not piped automatically, and you read it from `worker.stdout` and `worker.stderr` streams instead. With `stdin: true`, you get a writable `worker.stdin` that the worker reads as `process.stdin`.

## 70: How can you see how busy a worker thread is?

Use `worker.performance.eventLoopUtilization()` from the main thread. It tells you what part of the time the worker's event loop was busy, as a number from 0 to 1. Inside any thread you can call `performance.eventLoopUtilization()` from `node:perf_hooks`.

```js
const start = worker.performance.eventLoopUtilization();
setTimeout(() => {
  const elu = worker.performance.eventLoopUtilization(start);
  console.log("worker busy:", (elu.utilization * 100).toFixed(1) + "%");
}, 1000);
```

## 71: How do you shut down a cluster gracefully?

Stop taking new connections, let current requests finish, then exit. In the primary, call `worker.disconnect()` for each worker. That closes all servers in the worker and the IPC channel. The worker exits once its open connections end. Add a timeout that kills workers which take too long.

```js
process.on("SIGTERM", () => {
  for (const worker of Object.values(cluster.workers)) {
    worker.disconnect();
    setTimeout(() => worker.kill(), 10_000).unref();
  }
});
```

## 72: What is the difference between worker.kill() and worker.disconnect() in cluster?

`worker.disconnect()` is the soft way. The worker stops accepting new connections, finishes the open ones and then exits. `worker.kill(signal)` sends a signal to the worker process, `SIGTERM` by default, and the process dies right away unless it handles that signal. Both set `exitedAfterDisconnect` to `true`.

## 73: What is worker.exitedAfterDisconnect and why does it matter?

It is `true` if the worker exited because you called `disconnect()` or `kill()`, and `false` if it died on its own. You check it in the `'exit'` handler so you only restart workers that crashed, not ones you stopped on purpose, for example during shutdown.

## 74: How do you restart a cluster app with zero downtime?

Replace workers one at a time. Fork a new worker, wait for its `'listening'` event, then disconnect one old worker. Repeat until all old workers are gone. At every moment some workers are serving traffic. PM2 does this with `pm2 reload`.

```js
async function rollingRestart() {
  for (const old of Object.values(cluster.workers)) {
    const fresh = cluster.fork();
    await new Promise((r) => fresh.once("listening", r));
    old.disconnect();
  }
}
```

## 75: How do you avoid a crash loop in a cluster?

If a worker crashes on startup, for example because the database is down, naive restart code will fork and crash in a tight loop. Count restarts in a time window, wait longer between attempts (backoff), and stop and alert after too many failures. Also log the exit code and signal of each crash.

## 76: How do you change the cluster scheduling policy?

Set `cluster.schedulingPolicy` to `cluster.SCHED_RR` (round-robin) or `cluster.SCHED_NONE` (let the OS decide) before the first `fork()`. You can also use the environment variable `NODE_CLUSTER_SCHED_POLICY` with `rr` or `none`. The setting can't be changed after workers are started.

## 77: What does cluster.setupPrimary() do?

It changes the default settings for workers forked after the call. Common options are `exec` (the worker script), `args`, `execArgv`, `silent` (pipe worker output to the primary), `serialization` and `inspectPort`. Older code calls the deprecated `cluster.setupMaster()`.

```js
cluster.setupPrimary({
  exec: "./server.js",
  execArgv: ["--max-old-space-size=512"],
});
cluster.fork();
```

## 78: How do you run a scheduled job only once when the app runs in cluster mode?

Every worker runs the same code, so a `setInterval` or cron job in the app runs once per worker. Options: run the job in the primary, start one worker with a special env variable like `ROLE=scheduler`, or use a distributed lock (for example in Redis) so only one instance runs it. The lock is the only option that also works across several servers.

## 79: How do you share a cache across cluster workers?

Each worker has its own memory, so a plain in-memory cache is duplicated and goes out of sync. The common fix is an external cache like Redis or Memcached. Another option is to keep the cache in the primary and ask for values over IPC, but every lookup becomes a message round trip, so it is slower and the primary becomes a bottleneck.

## 80: How do WebSockets and Socket.IO work with cluster?

A WebSocket connection stays on the worker that accepted it, so that part works. Problems start with Socket.IO's HTTP long-polling fallback, where each request of one client must reach the same worker. You need sticky sessions, for example with `@socket.io/sticky`, and an adapter such as `@socket.io/cluster-adapter` or the Redis adapter, so that broadcasts reach clients connected to other workers.

## 81: What are sticky sessions?

Sticky sessions mean that all requests from the same client go to the same worker or server. It's usually done by client IP or a cookie. It's needed when a worker keeps state for a client, like Socket.IO polling. The downside is less even load, and when a worker dies its clients lose their state.

## 82: Should you use cluster or several containers behind a load balancer?

In Kubernetes or ECS, the common advice is one Node.js process per container and scale with more replicas. The orchestrator already restarts crashed processes, balances traffic and does rolling updates. Cluster still makes sense on a plain VM or a big machine without an orchestrator, or when you can only run one container.

## 83: What should you watch out for when using cluster inside a container?

The number of cores Node.js sees may not match the container's CPU limit. If you fork one worker per core on a 64-core host but the container only gets 2 CPUs, the workers fight over 2 CPUs and use far more memory than needed. Set the worker count from config or an env variable, and also check that the memory limit fits all workers.

## 84: How do you debug worker threads and cluster workers?

For worker threads, the VS Code debugger can attach to them and stop at breakpoints inside worker code when you start the app with `--inspect`. Logging the `threadId` in every log line also helps a lot. For cluster, each worker is a separate process, so it needs its own inspector port. If the primary runs with `--inspect`, Node.js gives each worker the next port number. You can also set `inspectPort` in `cluster.setupPrimary()`.

## 85: How do you pass command line flags and arguments to a worker thread?

Use `argv` to add values to the worker's `process.argv`, and `execArgv` to pass Node.js flags. By default a worker inherits the parent's `execArgv`.

```js
new Worker(file, {
  argv: ["--mode", "fast"],
  execArgv: ["--enable-source-maps"],
});
```

Some flags only make sense per process, like `--max-old-space-size`. For worker heap size, use `resourceLimits`.

## 86: Can you run a TypeScript file in a worker thread?

In Node.js 24 you can, as long as the file only uses TypeScript syntax that can be removed without transforming code. Node.js strips the types itself, so `new Worker(new URL('./task.ts', import.meta.url))` works. Features like `enum` or parameter properties still need a build step or a loader. In older versions you had to compile first or register a loader like `tsx` through `execArgv`.

## 87: How do you test code that uses worker threads?

Keep the real work in a plain function in its own module and unit test that function directly, without any threads. Then add a few integration tests that start a real worker or pool and check messages, errors and shutdown. Always terminate workers in test teardown, or the test runner may hang.

## 88: What happens when you send a class instance to a worker thread?

It arrives as a plain object with the same own fields, but its prototype is gone, so methods and `instanceof` checks don't work. To get a real instance back, send the data and rebuild the object on the other side, for example with a `fromJSON()` static method. `Map`, `Set`, `Date` and `Error` are handled by structured clone and arrive correctly.

## 89: How do you handle uncaught exceptions in cluster workers?

Log the error, stop accepting new requests and exit. The app may be in a broken state after an uncaught exception, so don't keep running. The primary sees the `'exit'` event and forks a new worker.

```js
process.on("uncaughtException", (err) => {
  console.error("fatal error", err);
  server.close(() => process.exit(1));
  setTimeout(() => process.exit(1), 5000).unref();
});
```

## 90: When would you use child_process instead of worker threads for CPU work?

Use a child process when you need full isolation: a crash or memory leak can't affect the parent, and you can run a different Node.js version or a program in another language, like Python or ffmpeg. Worker threads start faster, use less memory and can share memory, so they suit short CPU tasks inside one app.

## 91: How do you match replies to requests when you send many messages to one worker?

Add an id to every message and keep a map of pending promises. The worker sends back the same id with its answer.

```js
let nextId = 0;
const pending = new Map();

worker.on("message", ({ id, result, error }) => {
  const p = pending.get(id);
  pending.delete(id);
  error ? p.reject(new Error(error)) : p.resolve(result);
});

function call(payload) {
  const id = nextId++;
  return new Promise((resolve, reject) => {
    pending.set(id, { resolve, reject });
    worker.postMessage({ id, payload });
  });
}
```

## 92: How much does postMessage cost for large objects?

Structured clone walks the whole object and copies it, and the receiver rebuilds it. For a big nested object this can take longer than the work you wanted to offload, and it happens on the sending thread. Send less data, use binary formats in an `ArrayBuffer` and transfer it, or use `SharedArrayBuffer`.

## 93: Can worker threads share one database connection pool?

No. A connection pool is a JavaScript object with sockets, and it can't be cloned to another thread. Each worker that talks to the database needs its own pool. Usually it's better to keep database access on the main thread and send only CPU work to workers.

## 94: How does clustering affect database connection counts?

Each cluster worker has its own pool. With 8 workers and a pool size of 20, you can open up to 160 connections, and more again across several servers. That can hit the database's connection limit. Lower the pool size per worker, or put a pooler like PgBouncer in front of PostgreSQL.

## 95: How do you handle logs from many cluster workers?

Add the process id or worker id to every log line so you can tell workers apart. Log to stdout as JSON and let the platform collect the logs, or send them to a central system. Avoid having every worker write to the same file directly, because lines can get mixed up.

## 96: What is the difference between the 'online' and 'listening' events in cluster?

`'online'` fires when the worker process has started and is running code. `'listening'` fires later, when the worker called `listen()` on a server and it's ready for connections. Wait for `'listening'` if you need to know the worker can take traffic, for example during a rolling restart.

## 97: How do you send a message to every cluster worker?

Loop over `cluster.workers` in the primary and call `send()` on each. To send from one worker to all others, the worker first sends to the primary, and the primary forwards it.

```js
function broadcast(msg) {
  for (const worker of Object.values(cluster.workers)) {
    worker.send(msg);
  }
}
```

## 98: What happens when you call server.listen() inside a cluster worker?

The worker sends a request to the primary over IPC. If the primary already has a server for that address and port, it reuses it. Otherwise it creates one. With round-robin, the primary accepts connections and passes each one to a worker. With `SCHED_NONE`, the primary sends the listening socket handle to the worker, and workers accept connections themselves.

## 99: How do you put the main thread code and the worker code in the same file?

Check `isMainThread` and start a worker that points to the same file.

```js
import {
  Worker,
  isMainThread,
  parentPort,
  workerData,
} from "node:worker_threads";

if (isMainThread) {
  const worker = new Worker(new URL(import.meta.url), { workerData: 10 });
  worker.on("message", console.log);
} else {
  parentPort.postMessage(workerData * 2);
}
```

In CommonJS, use `new Worker(__filename)`.

## 100: How do you add backpressure when sending tasks to a worker pool?

Don't let the queue grow without a limit, or memory blows up under load and requests wait forever. Set a maximum queue size and reject or answer with HTTP 503 when it's full. In Piscina, set `maxQueue`. You can also check `pool.queueSize` before you accept new work.

# Advanced Questions (101-150)

## 101: How are worker threads built internally?

Each worker is a real OS thread inside the same process. Node.js creates a new V8 isolate for it, a new Node.js environment with its own module loader and globals, and a separate libuv event loop. Messages go through a native message port: the sender serializes the value with V8's serializer, and the receiver's event loop is woken up to deserialize it.

## 102: What is shared between worker threads in one process, and what is not?

Not shared: the JavaScript heap, globals, the module cache, timers and the event loop. Shared: the process itself, including its memory limits, file descriptors, `process.pid`, current working directory, signal handling and the libuv thread pool. Native addons are loaded once per process, so their global C++ state is shared too. `SharedArrayBuffer` memory is shared on purpose.

## 103: Why does starting a worker thread take time and memory?

Node.js has to create a V8 isolate, set up the heap, run the Node.js bootstrap code and load your worker modules. That takes a few milliseconds to tens of milliseconds, and each worker uses several megabytes of memory even when idle, plus whatever your modules load. That's why pools that reuse workers are the normal approach.

## 104: How does round-robin load balancing work inside the cluster module?

The primary owns the listening socket. When a connection arrives, the primary accepts it, picks the next free worker, and sends the connection handle to that worker over the IPC channel. The worker wraps the handle in a socket and emits `'connection'` on its server. So every new connection passes through the primary once, but the request data after that goes directly to the worker.

## 105: Why did the cluster module move away from letting the OS pick the worker?

With `SCHED_NONE`, all workers wait on the same socket and the OS wakes one of them. In practice on Linux, the OS tends to give most connections to the same few processes, which leads to very uneven load. Round-robin in the primary gives a much fairer spread. It became the default in Node.js 0.12.

## 106: Why isn't round-robin the default on Windows?

On Windows, passing connection handles between processes is expensive and works differently than on Unix. The libuv team found that sending every connection from the primary to a worker was slow there, so Windows keeps the OS-based approach by default. You can still force round-robin with the `NODE_CLUSTER_SCHED_POLICY=rr` setting.

## 107: What is the reusePort option, and how does it compare to cluster?

Newer Node.js versions support `reusePort: true` in `server.listen()` options on platforms with `SO_REUSEPORT`, like Linux and FreeBSD. Several independent processes can then bind the same port, and the kernel spreads connections between them. Unlike cluster, there is no primary in the request path and the processes don't need a parent-child relationship. It doesn't give you cluster's restart logic, so you still need a process manager.

## 108: What happens if cluster workers call server.listen(0)?

Outside a cluster, port `0` means "pick a random free port". In a cluster, the primary chooses the random port once and every worker that calls `listen(0)` gets that same port. That way all workers still share one server. If you really want different ports per worker, give each worker its own port number.

## 109: What does exclusive: true do in server.listen() in a cluster worker?

It tells the worker not to share the handle through the primary. The worker binds the address itself, as if it weren't in a cluster. If two workers do that on the same port, the second one fails with `EADDRINUSE`, unless the OS allows port reuse. It's useful when each worker needs its own port, for example a per-worker metrics endpoint.

## 110: How do you build a simple mutex with Atomics?

Use one `Int32Array` slot: 0 means unlocked, 1 means locked. Use `compareExchange` to grab the lock, `wait` to sleep while it is taken, and `notify` to wake a waiting thread when you release it.

```js
const UNLOCKED = 0;
const LOCKED = 1;

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

Every thread creates its own `Mutex` object around the same `SharedArrayBuffer`. Since `lock()` blocks, use it only in worker threads.

## 111: Can you call Atomics.wait() on the Node.js main thread?

Yes. Browsers forbid it on the main thread, but Node.js allows it. It is still almost always a bad idea, because it blocks the whole event loop: no I/O, no timers, no other requests until it returns. On the main thread use `Atomics.waitAsync()` instead, which returns a promise.

## 112: How do you avoid race conditions with SharedArrayBuffer?

A race happens when two threads read and write the same memory at the same time, for example both doing `arr[0]++`, which is a read and a write, so updates get lost. Use `Atomics` operations like `Atomics.add` for single values, and a lock for changes that touch several values. Better still, design the code so each thread writes only to its own part of the buffer.

```js
// Wrong: lost updates under contention
counter[0]++;

// Right
Atomics.add(counter, 0, 1);
```

## 113: Why do you need Atomics even for simple reads and writes on shared memory?

Without `Atomics`, the JIT compiler and the CPU can reorder or cache memory operations, so another thread might see writes in a different order or not at all for a while. `Atomics.load` and `Atomics.store` give ordering guarantees: once a thread sees a value written with `Atomics.store`, it also sees all writes that happened before it. That's what makes a "data is ready" flag safe.

## 114: What does Atomics.waitAsync() do?

It works like `Atomics.wait()` but doesn't block. It returns an object with a `value` that is either a result string right away or a promise that resolves to `'ok'` or `'timed-out'` when another thread calls `Atomics.notify`. That lets the main thread wait for shared memory changes without freezing the event loop.

```js
const res = Atomics.waitAsync(arr, 0, 0);
if (res.async) {
  await res.value;
}
console.log("value changed:", Atomics.load(arr, 0));
```

## 115: How can you make a synchronous call to a worker thread?

Combine `Atomics.wait` with `receiveMessageOnPort`. The caller posts a request with a shared flag, blocks on `Atomics.wait`, and the worker sets the flag and calls `Atomics.notify` after posting the reply. Then the caller reads the reply synchronously. Libraries like `synckit` use this to make async APIs usable in sync code, such as ESLint plugins.

```js
import {
  Worker,
  MessageChannel,
  receiveMessageOnPort,
} from "node:worker_threads";

const worker = new Worker(new URL("./async-worker.js", import.meta.url));
const signal = new Int32Array(new SharedArrayBuffer(4));
const { port1, port2 } = new MessageChannel();
worker.postMessage({ port: port2, signal }, [port2]);

export function callSync(data) {
  Atomics.store(signal, 0, 0);
  port1.postMessage(data);
  Atomics.wait(signal, 0, 0);
  return receiveMessageOnPort(port1).message;
}
```

```js
// async-worker.js
import { parentPort } from "node:worker_threads";

parentPort.once("message", ({ port, signal }) => {
  port.on("message", async (data) => {
    const result = await fetch(data.url).then((r) => r.status);
    port.postMessage(result);
    Atomics.store(signal, 0, 1);
    Atomics.notify(signal, 0);
  });
});
```

This blocks the calling thread for as long as the work takes, so use it only when an API must be synchronous.

## 116: How do you design a worker pool that survives crashed workers?

Track which task each worker is running. On `'error'` or an unexpected `'exit'`, reject that task's promise, remove the worker and start a replacement, so the pool size stays the same. Add a limit on how fast workers are recreated, so a task that always crashes the worker doesn't cause a restart storm. Optionally retry tasks that failed because of a crash, not because of a thrown error.

## 117: How do you decide how many threads a worker pool should have?

Start with the number of available cores minus one, so the main thread has room for I/O. If the tasks also wait on I/O, a few more can help. More threads than cores for pure CPU work only adds context switching. Remember the libuv pool and other processes on the same machine also need CPU. Then measure throughput and latency under realistic load and adjust.

## 118: How do worker threads interact with the libuv thread pool?

All threads in a process share one libuv thread pool, 4 threads by default. If many workers do `fs`, `zlib` or `crypto.pbkdf2` work at once, they queue up for those 4 threads, and the main thread's file reads wait too. Raise `UV_THREADPOOL_SIZE` at process start if that's a bottleneck. It's read once when the pool is first used, so changing it later in code has no effect.

## 119: What problems can native addons cause in worker threads?

An addon must be "context-aware" to be loaded in more than one thread. Addons built with Node-API usually are. Older addons that keep global C++ state may crash or fail with an error that the module can't be loaded in a worker. Addons also need cleanup hooks, so they release resources when a worker stops. If a library doesn't support workers, run that code in a child process instead.

## 120: How do you put a timeout on a task that runs in a worker thread?

You can't interrupt a synchronous loop from outside without stopping the thread. So start a timer in the main thread. If the task doesn't finish in time, call `worker.terminate()`, reject the task and start a new worker. For long tasks you control, you can also check a shared flag in a `SharedArrayBuffer` inside the loop and stop early in a cooperative way.

## 121: What happens to the code running in a worker when you call terminate()?

Node.js asks V8 to stop JavaScript execution in that thread as soon as possible, even in the middle of a loop. Pending `finally` blocks, `'exit'` handlers that do async work and unfinished promises in the worker don't get a chance to complete. Open files and sockets are closed by Node.js when the environment is torn down. Don't rely on the worker cleaning up after itself when it is terminated.

## 122: What happens to messages that are in flight when a worker exits?

Messages that the worker posted before it exited are still delivered to the parent, usually before the `'exit'` event. Messages sent to a worker that already stopped are dropped without an error. So if the main thread posts a task to a dead worker, the task's promise can hang forever. Track worker state and fail pending tasks on `'exit'`.

## 123: How do you take a heap snapshot of a worker thread?

From the main thread, call `worker.getHeapSnapshot()`. It returns a promise for a readable stream with the snapshot data. Inside the worker, you can call `v8.writeHeapSnapshot()`. Load the file in Chrome DevTools' Memory tab.

```js
import { createWriteStream } from "node:fs";
import { pipeline } from "node:stream/promises";

const stream = await worker.getHeapSnapshot();
await pipeline(
  stream,
  createWriteStream(`worker-${worker.threadId}.heapsnapshot`),
);
```

## 124: How do you find a memory leak in one of many cluster workers?

Watch memory per worker (by pid) in your metrics, and look for one that keeps growing. Start the app with `--heapsnapshot-signal=SIGUSR2`, then send that signal to the leaking worker's pid to write a snapshot. Take two or three snapshots over time and compare them in DevTools to see which objects grow. As a short-term fix, recycle workers after a number of requests or when memory passes a limit, but still fix the leak.

## 125: How does clustering affect memory use and garbage collection?

Each worker has its own heap and its own garbage collector. Total memory is roughly the base memory of one worker times the number of workers, plus duplicated caches. On the plus side, each heap is smaller, so GC pauses only affect one worker at a time. Set `--max-old-space-size` per worker so the total still fits the machine's memory.

## 126: Why might clustering not make a slow app any faster?

Clustering helps only when the Node.js process itself is the bottleneck because one CPU core is maxed out. If the time goes into slow database queries, external APIs, locks or network, more workers just send more load to the same slow place. Profile first. Check CPU usage per process and where request time is spent before adding workers.

## 127: An Express endpoint generates PDF reports and makes other requests slow. How would you fix it?

The PDF work blocks the event loop, so all other requests wait. Options, from simple to bigger:

1. Move the generation into a worker pool like Piscina, so the event loop stays free.
2. If reports take seconds or longer, put them in a job queue like BullMQ, return a job id right away, and let the client fetch the result later.
3. If load grows, run the workers as a separate service that you scale on its own.

Also limit how many reports can be generated at once, so a burst can't use all CPUs.

## 128: When would you use a job queue like BullMQ instead of worker threads?

Use a queue when jobs must survive a restart, need retries, scheduling or priorities, or should run on other machines. Worker threads live inside one process, so if the process crashes, running and queued tasks are lost. Worker threads are better for short CPU tasks where the HTTP request waits for the answer. Often you combine both: a BullMQ worker process that uses threads or sandboxed processors for heavy jobs.

## 129: How does postMessage compare with SharedArrayBuffer for performance?

`postMessage` copies the data, so the cost grows with the message size, plus some fixed overhead for waking the other thread. For small, rare messages that's fine. For big data sent often, `SharedArrayBuffer` avoids copying entirely, but you need `Atomics` for coordination and you can only store raw binary data, not objects. Transferring an `ArrayBuffer` is a middle ground: no copy, but only one side owns it at a time.

## 130: How do you stream data to or from a worker thread?

Web streams are transferable. You can create a `ReadableStream` or `WritableStream` and pass it in the transfer list. The other side then reads or writes it with normal stream code, and chunks move across threads with backpressure. For simple cases, you can also send chunks as messages over a `MessagePort`, but then you have to build backpressure yourself.

```js
const { readable, writable } = new TransformStream();
worker.postMessage({ input: readable }, [readable]);

const writer = writable.getWriter();
await writer.write("chunk 1");
await writer.close();
```

## 131: Are worker threads a security sandbox for running untrusted code?

No. A worker runs in the same process with the same permissions. It can read files, open network connections, change shared memory and load native modules. `resourceLimits` only limits heap size, not what the code can do. For untrusted code, use a separate process with OS-level isolation like containers, or a library that gives a real isolate boundary such as `isolated-vm`, and also use the Node.js permission model where it fits.

## 132: How is the vm module different from worker threads?

The `vm` module runs code in a different global context on the same thread. It doesn't run anything in parallel, and it is not a security boundary either: the Node.js docs say not to use it for untrusted code. Worker threads run code on another thread with a separate isolate, which gives you parallelism. They solve different problems.

## 133: How do you give many workers access to a large read-only dataset?

Posting a big object to each worker copies it once per worker, which wastes time and memory. Better options: load the data into a `SharedArrayBuffer` once and post that, so all workers read the same memory. Or let each worker load and build its own copy from disk at startup, if memory allows. Or keep the data in an external store like Redis and query only what you need.

## 134: How should a cluster app handle SIGTERM in Kubernetes?

Kubernetes sends `SIGTERM` to the main process, which is the primary, and kills everything after the grace period (30 seconds by default). The primary should catch `SIGTERM`, stop forking new workers, call `disconnect()` on every worker, wait for them to exit, and then exit itself. Add a timeout below the grace period that kills stuck workers. Also make the readiness probe fail early, so no new traffic is routed to the pod.

## 135: Does the primary automatically pass signals to cluster workers?

No. Signals sent to the primary's pid with `kill` go only to the primary. You must forward them or call `disconnect()`. Pressing Ctrl+C in a terminal is different: the terminal sends `SIGINT` to the whole foreground process group, so the primary and all workers receive it at the same time. That's why shutdown can look fine locally and fail in production.

## 136: How can you pass a server or socket handle between processes without cluster?

`child_process` lets you send a handle as the second argument of `send()`. You can send a `net.Server` or a `net.Socket` to another Node.js process. This is what cluster uses under the hood. It's useful for custom setups, for example a parent that accepts a connection, reads the first bytes, and then hands the socket to the right child.

```js
// parent
const child = fork("child.js");
const server = net.createServer();
server.listen(3000, () => child.send("server", server));

// child
process.on("message", (msg, server) => {
  if (msg === "server") server.on("connection", (socket) => socket.end("hi"));
});
```

## 137: Why can sticky sessions by IP address lead to uneven load?

Many users can share one IP, for example behind a company NAT, a mobile carrier or a proxy. All of them end up on the same worker. On the other hand, if there is a reverse proxy in front, every request may seem to come from the proxy's IP. Cookie-based stickiness, or a design with no per-worker state, spreads load better.

## 138: How do you give one cluster worker a special role, like running background jobs?

Fork that worker with an extra env variable and check it in the worker code. Remember the role if that worker dies, so you restart it with the same role.

```js
const roles = new Map();

function forkWith(role) {
  const worker = cluster.fork({ ROLE: role });
  roles.set(worker.id, role);
}

cluster.on("exit", (worker) => {
  const role = roles.get(worker.id);
  roles.delete(worker.id);
  if (!worker.exitedAfterDisconnect) forkWith(role);
});
```

## 139: How do you collect Prometheus metrics from all cluster workers?

Each worker has its own metrics, so scraping `/metrics` through the shared port would hit a random worker. The `prom-client` library has an `AggregatorRegistry` for this. Workers register metrics as usual, and the primary calls `clusterMetrics()` to ask every worker over IPC and merge the results. Serve that from a separate HTTP server in the primary on its own port.

## 140: What happens if a worker thread throws and the main thread has no 'error' listener?

The `Worker` is an `EventEmitter`, and emitting `'error'` with no listener throws. So the worker's error is rethrown in the main thread as an uncaught exception, and the whole process crashes. Always attach an `'error'` listener to every worker, even if it only logs and starts a replacement.

## 141: What is advanced serialization in cluster and child_process?

By default IPC messages between processes are sent as JSON, so `Map`, `Set`, `BigInt`, `Date` and circular objects don't survive. With `serialization: 'advanced'` in `child_process.fork()` or `cluster.setupPrimary()`, Node.js uses V8's serializer, which supports the same types as structured clone. It can be a bit slower for simple JSON-like data.

## 142: Why can posting a huge message still block the main thread?

Serialization happens on the sending thread, synchronously, inside `postMessage()`. If you post a deeply nested object with millions of entries, the main thread spends that time copying it, and the event loop is blocked even though the "real work" runs in the worker. Use binary data and transfer it, split the data into chunks, or let the worker load the data itself.

## 143: How do you find code that should be moved to a worker thread?

Measure event loop delay and utilization. `monitorEventLoopDelay()` from `node:perf_hooks` shows how long the loop gets stuck, and `performance.eventLoopUtilization()` shows how busy it is. Then profile with `--cpu-prof` or Clinic.js to find the functions that take the time. Look for synchronous loops, big `JSON.parse` calls, regex on large input, sync crypto and image work.

```js
import { monitorEventLoopDelay } from "node:perf_hooks";

const h = monitorEventLoopDelay({ resolution: 20 });
h.enable();
setInterval(() => {
  console.log("p99 delay ms:", h.percentile(99) / 1e6);
  h.reset();
}, 10_000);
```

## 144: You can't send functions to a worker. How do you run different kinds of tasks in one pool?

Put all task functions in the worker module and send a task name plus data. The worker looks up the function by name. Piscina also supports a `name` option on `run()` to call a named export of the worker file. Sending code as a string with `eval` is possible but hard to debug and risky, so avoid it.

```js
// tasks.js (Piscina worker)
export function resize({ image, width }) {
  /* ... */
}
export function hash({ text }) {
  /* ... */
}

// main
await pool.run({ text: "abc" }, { name: "hash" });
```

## 145: How would you design an image processing service on an 8-core server?

Keep the HTTP layer on the main thread and do the resizing in a worker pool of about 6-7 threads. Read uploads as streams, put the bytes in an `ArrayBuffer` and transfer it to the worker, then transfer the result back. Set a max queue size and return 503 when it's full. Note that libraries like `sharp` already use their own native threads, so measure first: for them, a worker pool may add little. Scale out with more instances behind a load balancer when one server isn't enough.

## 146: How can a cluster primary become a bottleneck?

With round-robin, the primary accepts every new connection. With many short-lived connections, like no keep-alive or lots of small clients, the primary's single thread can become the limit. If you also route IPC messages, metrics or cache lookups through the primary, it gets worse. Keep the primary light, use keep-alive, or switch to `reusePort` or several instances behind a real load balancer.

## 147: What happens to open keep-alive connections when you disconnect a cluster worker?

`disconnect()` closes the server, so it accepts no new connections, but existing keep-alive connections stay open and the worker can't exit until they close. A browser may hold an idle connection for a long time. In the worker, call `server.closeIdleConnections()` and, after a timeout, `server.closeAllConnections()` on the HTTP server so the worker can exit on time.

## 148: How do you keep an in-memory state consistent across cluster workers if you can't use Redis?

Make the primary the single owner of the state. Workers send update and read requests over IPC, and the primary applies them in order and replies. This works for small, low-traffic state, but every read is a round trip, and the state is lost if the primary dies. For anything important, an external store is the right answer. This is a good point to make in an interview.

## 149: What are common mistakes with worker threads?

- Creating a new worker for every task instead of using a pool.
- Using workers for I/O work, which Node.js already handles well.
- Sending huge objects with `postMessage` and paying for the copy.
- No `'error'` listener, so one worker error crashes the process.
- Forgetting to handle `'exit'`, so pending task promises never settle.
- Plain reads and writes on `SharedArrayBuffer` without `Atomics`.
- Leaving workers or channels running in tests, so the process never exits.

## 150: What are common mistakes with the cluster module?

- Keeping sessions, caches or rate limits in worker memory.
- Running cron jobs in every worker.
- Restarting workers in a tight loop with no backoff.
- Forking one worker per host core inside a CPU-limited container.
- Not handling `SIGTERM`, so deploys drop in-flight requests.
- Multiplying database connections by the number of workers without noticing.
- Using cluster in Kubernetes when more replicas would be simpler.
