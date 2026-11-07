# Node.js Interview Questions and Answers

_Last updated: October 28, 2026_

450 Node.js interview questions with answers and code examples, split into three levels: 150 easy, 150 moderate and 150 advanced.

The answers are based on the current Node.js LTS releases (22 and 24) and mention newer versions where it matters. When an API was added in a specific version, the version is noted, so you can tell what works on the Node version you use. Code examples use ES modules unless the question is about CommonJS.

## Table of Contents

- [Easy Questions (1-150)](#easy-questions)
- [Moderate Questions (151-300)](#moderate-questions)
- [Advanced Questions (301-450)](#advanced-questions)

### Easy Questions (1-150)

- [1: What is Node.js?](#1-what-is-nodejs)
- [2: Is Node.js a programming language or a framework?](#2-is-nodejs-a-programming-language-or-a-framework)
- [3: What is V8?](#3-what-is-v8)
- [4: What is libuv?](#4-what-is-libuv)
- [5: Is Node.js single-threaded?](#5-is-nodejs-single-threaded)
- [6: What is the event loop?](#6-what-is-the-event-loop)
- [7: What does non-blocking I/O mean?](#7-what-does-non-blocking-io-mean)
- [8: What is the difference between blocking and non-blocking code? Give an example.](#8-what-is-the-difference-between-blocking-and-non-blocking-code-give-an-example)
- [9: How do you check which version of Node.js and npm you have?](#9-how-do-you-check-which-version-of-nodejs-and-npm-you-have)
- [10: What is npm?](#10-what-is-npm)
- [11: What is package.json?](#11-what-is-packagejson)
- [12: What is package-lock.json and should you commit it?](#12-what-is-package-lockjson-and-should-you-commit-it)
- [13: What is the difference between dependencies and devDependencies?](#13-what-is-the-difference-between-dependencies-and-devdependencies)
- [14: What is the difference between npm install and npm ci?](#14-what-is-the-difference-between-npm-install-and-npm-ci)
- [15: What is npx?](#15-what-is-npx)
- [16: What is semantic versioning and what do ^ and ~ mean?](#16-what-is-semantic-versioning-and-what-do--and--mean)
- [17: What is the difference between a global and a local package install?](#17-what-is-the-difference-between-a-global-and-a-local-package-install)
- [18: What are npm scripts?](#18-what-are-npm-scripts)
- [19: What is a module in Node.js?](#19-what-is-a-module-in-nodejs)
- [20: What is the difference between CommonJS and ES modules?](#20-what-is-the-difference-between-commonjs-and-es-modules)
- [21: How do you use ES modules in Node.js?](#21-how-do-you-use-es-modules-in-nodejs)
- [22: How does require() work at a basic level?](#22-how-does-require-work-at-a-basic-level)
- [23: What is the difference between module.exports and exports?](#23-what-is-the-difference-between-moduleexports-and-exports)
- [24: How do import and export work in ES modules?](#24-how-do-import-and-export-work-in-es-modules)
- [25: What are core modules in Node.js?](#25-what-are-core-modules-in-nodejs)
- [26: Why should you use the node: prefix when importing core modules?](#26-why-should-you-use-the-node-prefix-when-importing-core-modules)
- [27: What are `__dirname` and `__filename`? How do you get them in ES modules?](#27-what-are-__dirname-and-__filename-how-do-you-get-them-in-es-modules)
- [28: What is the global object in Node.js?](#28-what-is-the-global-object-in-nodejs)
- [29: What is the process object?](#29-what-is-the-process-object)
- [30: What is process.argv?](#30-what-is-processargv)
- [31: How do you use environment variables in Node.js?](#31-how-do-you-use-environment-variables-in-nodejs)
- [32: How do you load a .env file without the dotenv package?](#32-how-do-you-load-a-env-file-without-the-dotenv-package)
- [33: How do you exit a Node.js process, and what are exit codes?](#33-how-do-you-exit-a-nodejs-process-and-what-are-exit-codes)
- [34: What is the Node.js REPL?](#34-what-is-the-nodejs-repl)
- [35: What are the different ways to run JavaScript code with the node command?](#35-what-are-the-different-ways-to-run-javascript-code-with-the-node-command)
- [36: What is a callback function?](#36-what-is-a-callback-function)
- [37: What is an error-first callback?](#37-what-is-an-error-first-callback)
- [38: What is callback hell and how do you avoid it?](#38-what-is-callback-hell-and-how-do-you-avoid-it)
- [39: What is a Promise?](#39-what-is-a-promise)
- [40: What are the states of a Promise?](#40-what-are-the-states-of-a-promise)
- [41: What is async/await?](#41-what-is-asyncawait)
- [42: How do you handle errors with async/await?](#42-how-do-you-handle-errors-with-asyncawait)
- [43: What is the difference between Promise.all, Promise.allSettled, Promise.race and Promise.any?](#43-what-is-the-difference-between-promiseall-promiseallsettled-promiserace-and-promiseany)
- [44: What is the difference between setTimeout and setInterval?](#44-what-is-the-difference-between-settimeout-and-setinterval)
- [45: What is setImmediate?](#45-what-is-setimmediate)
- [46: What is process.nextTick?](#46-what-is-processnexttick)
- [47: What is the timers/promises module?](#47-what-is-the-timerspromises-module)
- [48: What is the difference between fs.readFile and fs.readFileSync?](#48-what-is-the-difference-between-fsreadfile-and-fsreadfilesync)
- [49: What is fs/promises?](#49-what-is-fspromises)
- [50: How do you write and append to a file?](#50-how-do-you-write-and-append-to-a-file)
- [51: How do you check if a file exists?](#51-how-do-you-check-if-a-file-exists)
- [52: How do you read the contents of a directory?](#52-how-do-you-read-the-contents-of-a-directory)
- [53: How do you delete files and folders?](#53-how-do-you-delete-files-and-folders)
- [54: What is the path module? What is the difference between path.join and path.resolve?](#54-what-is-the-path-module-what-is-the-difference-between-pathjoin-and-pathresolve)
- [55: Which other path functions are useful?](#55-which-other-path-functions-are-useful)
- [56: What is the os module used for?](#56-what-is-the-os-module-used-for)
- [57: What is a Buffer?](#57-what-is-a-buffer)
- [58: What are the ways to create a Buffer?](#58-what-are-the-ways-to-create-a-buffer)
- [59: How do you convert a Buffer to different encodings?](#59-how-do-you-convert-a-buffer-to-different-encodings)
- [60: What are streams?](#60-what-are-streams)
- [61: What are the types of streams?](#61-what-are-the-types-of-streams)
- [62: What does pipe() do?](#62-what-does-pipe-do)
- [63: What is EventEmitter?](#63-what-is-eventemitter)
- [64: What is the difference between on() and once(), and how do you remove a listener?](#64-what-is-the-difference-between-on-and-once-and-how-do-you-remove-a-listener)
- [65: Why is the 'error' event special?](#65-why-is-the-error-event-special)
- [66: How do you create a simple HTTP server without a framework?](#66-how-do-you-create-a-simple-http-server-without-a-framework)
- [67: What are the req and res objects in an HTTP server?](#67-what-are-the-req-and-res-objects-in-an-http-server)
- [68: How do you set status codes and headers in a response?](#68-how-do-you-set-status-codes-and-headers-in-a-response)
- [69: How do you read query string parameters in a plain Node.js server?](#69-how-do-you-read-query-string-parameters-in-a-plain-nodejs-server)
- [70: Does Node.js have fetch built in?](#70-does-nodejs-have-fetch-built-in)
- [71: How do you read and write JSON in Node.js?](#71-how-do-you-read-and-write-json-in-nodejs)
- [72: What is Express.js?](#72-what-is-expressjs)
- [73: What is middleware?](#73-what-is-middleware)
- [74: How does routing work in Express?](#74-how-does-routing-work-in-express)
- [75: How do you serve static files with Express?](#75-how-do-you-serve-static-files-with-express)
- [76: What is a REST API?](#76-what-is-a-rest-api)
- [77: What are the common HTTP methods and status codes?](#77-what-are-the-common-http-methods-and-status-codes)
- [78: How do you restart a Node.js app automatically when files change?](#78-how-do-you-restart-a-nodejs-app-automatically-when-files-change)
- [79: What is the util module and what does util.promisify do?](#79-what-is-the-util-module-and-what-does-utilpromisify-do)
- [80: What do util.format and util.inspect do?](#80-what-do-utilformat-and-utilinspect-do)
- [81: How do you parse command line arguments without a library?](#81-how-do-you-parse-command-line-arguments-without-a-library)
- [82: How do you print colored text in the terminal without a library?](#82-how-do-you-print-colored-text-in-the-terminal-without-a-library)
- [83: What is the crypto module used for?](#83-what-is-the-crypto-module-used-for)
- [84: How do you create a hash of a string?](#84-how-do-you-create-a-hash-of-a-string)
- [85: What useful console methods are there besides console.log?](#85-what-useful-console-methods-are-there-besides-consolelog)
- [86: How do you debug a Node.js application?](#86-how-do-you-debug-a-nodejs-application)
- [87: What is the built-in test runner?](#87-what-is-the-built-in-test-runner)
- [88: What is the assert module?](#88-what-is-the-assert-module)
- [89: Do ES modules run in strict mode?](#89-do-es-modules-run-in-strict-mode)
- [90: What are the main differences between JavaScript in Node.js and in the browser?](#90-what-are-the-main-differences-between-javascript-in-nodejs-and-in-the-browser)
- [91: What is Node.js good for and what is it not good for?](#91-what-is-nodejs-good-for-and-what-is-it-not-good-for)
- [92: What is an LTS release of Node.js?](#92-what-is-an-lts-release-of-nodejs)
- [93: How do you install and switch between Node.js versions?](#93-how-do-you-install-and-switch-between-nodejs-versions)
- [94: How do you tell other developers and tools which Node version a project needs?](#94-how-do-you-tell-other-developers-and-tools-which-node-version-a-project-needs)
- [95: What is Corepack?](#95-what-is-corepack)
- [96: What are yarn and pnpm?](#96-what-are-yarn-and-pnpm)
- [97: What is the node_modules folder?](#97-what-is-the-node_modules-folder)
- [98: How does Node find a package when you import it by name?](#98-how-does-node-find-a-package-when-you-import-it-by-name)
- [99: What are the "main" and "exports" fields in package.json?](#99-what-are-the-main-and-exports-fields-in-packagejson)
- [100: Are modules cached in Node.js?](#100-are-modules-cached-in-nodejs)
- [101: What is a circular dependency?](#101-what-is-a-circular-dependency)
- [102: What is the cluster module?](#102-what-is-the-cluster-module)
- [103: What is the child_process module?](#103-what-is-the-child_process-module)
- [104: What are worker threads?](#104-what-are-worker-threads)
- [105: How do you write an error handling middleware in Express?](#105-how-do-you-write-an-error-handling-middleware-in-express)
- [106: What is CORS?](#106-what-is-cors)
- [107: How do you read a JSON request body in Express?](#107-how-do-you-read-a-json-request-body-in-express)
- [108: What is the difference between res.send, res.json and res.end in Express?](#108-what-is-the-difference-between-ressend-resjson-and-resend-in-express)
- [109: What is NODE_ENV?](#109-what-is-node_env)
- [110: What is the Error object and what is error.cause?](#110-what-is-the-error-object-and-what-is-errorcause)
- [111: What kinds of errors do you meet in Node.js?](#111-what-kinds-of-errors-do-you-meet-in-nodejs)
- [112: What is the uncaughtException event?](#112-what-is-the-uncaughtexception-event)
- [113: What happens when a promise rejection is not handled?](#113-what-happens-when-a-promise-rejection-is-not-handled)
- [114: How do you use the URL class?](#114-how-do-you-use-the-url-class)
- [115: What is the difference between the querystring module and URLSearchParams?](#115-what-is-the-difference-between-the-querystring-module-and-urlsearchparams)
- [116: What is the readline module?](#116-what-is-the-readline-module)
- [117: How do you ask the user for input in a terminal app?](#117-how-do-you-ask-the-user-for-input-in-a-terminal-app)
- [118: What is the zlib module?](#118-what-is-the-zlib-module)
- [119: What is the dns module?](#119-what-is-the-dns-module)
- [120: What is the net module?](#120-what-is-the-net-module)
- [121: What is the dgram module?](#121-what-is-the-dgram-module)
- [122: What is the difference between the http and https modules?](#122-what-is-the-difference-between-the-http-and-https-modules)
- [123: Can Node.js run TypeScript directly?](#123-can-nodejs-run-typescript-directly)
- [124: What is top-level await?](#124-what-is-top-level-await)
- [125: How do you make a Node.js script into a command line tool?](#125-how-do-you-make-a-nodejs-script-into-a-command-line-tool)
- [126: What is structuredClone?](#126-what-is-structuredclone)
- [127: What is AbortController?](#127-what-is-abortcontroller)
- [128: When should you use fs.createReadStream instead of fs.readFile?](#128-when-should-you-use-fscreatereadstream-instead-of-fsreadfile)
- [129: What is a template engine?](#129-what-is-a-template-engine)
- [130: Does Node.js have a built-in database?](#130-does-nodejs-have-a-built-in-database)
- [131: What is an ORM?](#131-what-is-an-orm)
- [132: What is a JWT?](#132-what-is-a-jwt)
- [133: What is the difference between cookies and sessions?](#133-what-is-the-difference-between-cookies-and-sessions)
- [134: How should you store user passwords?](#134-how-should-you-store-user-passwords)
- [135: What are WebSockets and does Node support them?](#135-what-are-websockets-and-does-node-support-them)
- [136: What is the difference between HTTP and WebSocket?](#136-what-is-the-difference-between-http-and-websocket)
- [137: What is the difference between a process and a thread?](#137-what-is-the-difference-between-a-process-and-a-thread)
- [138: How does garbage collection work in Node.js at a basic level?](#138-how-does-garbage-collection-work-in-nodejs-at-a-basic-level)
- [139: How do you check how much memory a Node process is using?](#139-how-do-you-check-how-much-memory-a-node-process-is-using)
- [140: What is the difference between process.cwd() and \_\_dirname?](#140-what-is-the-difference-between-processcwd-and-__dirname)
- [141: In what order do setTimeout, setImmediate and process.nextTick run?](#141-in-what-order-do-settimeout-setimmediate-and-processnexttick-run)
- [142: What are pre and post scripts in npm?](#142-what-are-pre-and-post-scripts-in-npm)
- [143: What is npm audit?](#143-what-is-npm-audit)
- [144: What are npm workspaces?](#144-what-are-npm-workspaces)
- [145: How do you control which files are published to npm?](#145-how-do-you-control-which-files-are-published-to-npm)
- [146: What is a peer dependency?](#146-what-is-a-peer-dependency)
- [147: How do you send different kinds of request bodies with fetch?](#147-how-do-you-send-different-kinds-of-request-bodies-with-fetch)
- [148: What are Blob and File in Node.js?](#148-what-are-blob-and-file-in-nodejs)
- [149: What is node --run?](#149-what-is-node---run)
- [150: What are the popular Node.js web frameworks?](#150-what-are-the-popular-nodejs-web-frameworks)

### Moderate Questions (151-300)

- [151: What are the phases of the event loop?](#151-what-are-the-phases-of-the-event-loop)
- [152: What is the difference between microtasks and macrotasks?](#152-what-is-the-difference-between-microtasks-and-macrotasks)
- [153: What does this code print, and why?](#153-what-does-this-code-print-and-why)
- [154: Why is the order of setTimeout(fn, 0) and setImmediate not fixed in the main module?](#154-why-is-the-order-of-settimeoutfn-0-and-setimmediate-not-fixed-in-the-main-module)
- [155: What is the difference between process.nextTick and queueMicrotask?](#155-what-is-the-difference-between-processnexttick-and-queuemicrotask)
- [156: How can process.nextTick starve the event loop?](#156-how-can-processnexttick-starve-the-event-loop)
- [157: What is the libuv thread pool and which operations use it?](#157-what-is-the-libuv-thread-pool-and-which-operations-use-it)
- [158: What are flowing and paused modes in readable streams?](#158-what-are-flowing-and-paused-modes-in-readable-streams)
- [159: What is backpressure in streams?](#159-what-is-backpressure-in-streams)
- [160: Why is stream.pipeline better than pipe?](#160-why-is-streampipeline-better-than-pipe)
- [161: How do you create a custom Readable stream?](#161-how-do-you-create-a-custom-readable-stream)
- [162: How do you create a custom Writable stream?](#162-how-do-you-create-a-custom-writable-stream)
- [163: What is a Transform stream? Show an example.](#163-what-is-a-transform-stream-show-an-example)
- [164: What is a Duplex stream and how is it different from Transform?](#164-what-is-a-duplex-stream-and-how-is-it-different-from-transform)
- [165: What is objectMode in streams?](#165-what-is-objectmode-in-streams)
- [166: What is highWaterMark?](#166-what-is-highwatermark)
- [167: How do you read a stream with for await...of?](#167-how-do-you-read-a-stream-with-for-awaitof)
- [168: What does Readable.from do?](#168-what-does-readablefrom-do)
- [169: What are Web Streams in Node.js and how do you convert between them and Node streams?](#169-what-are-web-streams-in-nodejs-and-how-do-you-convert-between-them-and-node-streams)
- [170: How do you know when a stream is completely done or has failed?](#170-how-do-you-know-when-a-stream-is-completely-done-or-has-failed)
- [171: What does the "MaxListenersExceededWarning" mean?](#171-what-does-the-maxlistenersexceededwarning-mean)
- [172: How do you wait for an event with a promise?](#172-how-do-you-wait-for-an-event-with-a-promise)
- [173: What happens if an event listener is an async function and it throws?](#173-what-happens-if-an-event-listener-is-an-async-function-and-it-throws)
- [174: What is the difference between EventEmitter and EventTarget in Node?](#174-what-is-the-difference-between-eventemitter-and-eventtarget-in-node)
- [175: What is events.errorMonitor?](#175-what-is-eventserrormonitor)
- [176: Where is Buffer memory stored, and why is Buffer.allocUnsafe unsafe?](#176-where-is-buffer-memory-stored-and-why-is-bufferallocunsafe-unsafe)
- [177: What is the difference between Buffer.byteLength and string.length?](#177-what-is-the-difference-between-bufferbytelength-and-stringlength)
- [178: What is the relationship between Buffer, Uint8Array and TextEncoder?](#178-what-is-the-relationship-between-buffer-uint8array-and-textencoder)
- [179: What is StringDecoder and when do you need it?](#179-what-is-stringdecoder-and-when-do-you-need-it)
- [180: What is the difference between spawn, exec, execFile and fork?](#180-what-is-the-difference-between-spawn-exec-execfile-and-fork)
- [181: How do parent and child processes talk to each other with fork?](#181-how-do-parent-and-child-processes-talk-to-each-other-with-fork)
- [182: Why is exec dangerous with user input?](#182-why-is-exec-dangerous-with-user-input)
- [183: How does the cluster module distribute connections?](#183-how-does-the-cluster-module-distribute-connections)
- [184: When should you use cluster and when worker_threads?](#184-when-should-you-use-cluster-and-when-worker_threads)
- [185: How do you send data to and from worker threads?](#185-how-do-you-send-data-to-and-from-worker-threads)
- [186: What are SharedArrayBuffer and Atomics used for?](#186-what-are-sharedarraybuffer-and-atomics-used-for)
- [187: Why should you use a worker pool instead of creating a worker per task?](#187-why-should-you-use-a-worker-pool-instead-of-creating-a-worker-per-task)
- [188: What is HTTP keep-alive and what does http.Agent do?](#188-what-is-http-keep-alive-and-what-does-httpagent-do)
- [189: Which timeouts does an http.Server have?](#189-which-timeouts-does-an-httpserver-have)
- [190: How do you shut down a Node.js server gracefully?](#190-how-do-you-shut-down-a-nodejs-server-gracefully)
- [191: What are SIGTERM and SIGINT and how do you handle them?](#191-what-are-sigterm-and-sigint-and-how-do-you-handle-them)
- [192: How do you set a timeout on a fetch request?](#192-how-do-you-set-a-timeout-on-a-fetch-request)
- [193: What is AbortSignal.any?](#193-what-is-abortsignalany)
- [194: How do you stream a large file download to the client correctly?](#194-how-do-you-stream-a-large-file-download-to-the-client-correctly)
- [195: How do you handle file uploads in Node.js?](#195-how-do-you-handle-file-uploads-in-nodejs)
- [196: Why does middleware order matter in Express?](#196-why-does-middleware-order-matter-in-express)
- [197: How are errors in async route handlers handled in Express 5?](#197-how-are-errors-in-async-route-handlers-handled-in-express-5)
- [198: What are the main changes in Express 5 compared to Express 4?](#198-what-are-the-main-changes-in-express-5-compared-to-express-4)
- [199: How is Fastify different from Express?](#199-how-is-fastify-different-from-express)
- [200: How do you validate request input?](#200-how-do-you-validate-request-input)
- [201: When would you choose sessions over JWTs, and the other way round?](#201-when-would-you-choose-sessions-over-jwts-and-the-other-way-round)
- [202: Why do you need timingSafeEqual when comparing secrets?](#202-why-do-you-need-timingsafeequal-when-comparing-secrets)
- [203: How do you add rate limiting to an API?](#203-how-do-you-add-rate-limiting-to-an-api)
- [204: Why use a logging library like pino instead of console.log?](#204-why-use-a-logging-library-like-pino-instead-of-consolelog)
- [205: How should you manage configuration and secrets?](#205-how-should-you-manage-configuration-and-secrets)
- [206: How does Node resolve a relative require() call?](#206-how-does-node-resolve-a-relative-require-call)
- [207: What are conditional exports?](#207-what-are-conditional-exports)
- [208: What are subpath imports (the "imports" field)?](#208-what-are-subpath-imports-the-imports-field)
- [209: What is the dual package hazard?](#209-what-is-the-dual-package-hazard)
- [210: Can you require() an ES module?](#210-can-you-require-an-es-module)
- [211: What is dynamic import()?](#211-what-is-dynamic-import)
- [212: What is import.meta?](#212-what-is-importmeta)
- [213: How do you import JSON files in ES modules?](#213-how-do-you-import-json-files-in-es-modules)
- [214: How do you use require() inside an ES module?](#214-how-do-you-use-require-inside-an-es-module)
- [215: What is the module wrapper function in CommonJS?](#215-what-is-the-module-wrapper-function-in-commonjs)
- [216: How can you clear a module from the require cache?](#216-how-can-you-clear-a-module-from-the-require-cache)
- [217: How do circular dependencies behave in CommonJS vs ESM?](#217-how-do-circular-dependencies-behave-in-commonjs-vs-esm)
- [218: How do you use hooks and subtests in node:test?](#218-how-do-you-use-hooks-and-subtests-in-nodetest)
- [219: How do you mock functions and timers with node:test?](#219-how-do-you-mock-functions-and-timers-with-nodetest)
- [220: How do you get code coverage with the built-in test runner?](#220-how-do-you-get-code-coverage-with-the-built-in-test-runner)
- [221: How do you run tests in watch mode and choose which tests run?](#221-how-do-you-run-tests-in-watch-mode-and-choose-which-tests-run)
- [222: How do you test an HTTP server without extra libraries?](#222-how-do-you-test-an-http-server-without-extra-libraries)
- [223: What ways are there to debug Node.js besides console.log?](#223-what-ways-are-there-to-debug-nodejs-besides-consolelog)
- [224: What is util.debuglog / NODE_DEBUG?](#224-what-is-utildebuglog--node_debug)
- [225: What is util.promisify.custom?](#225-what-is-utilpromisifycustom)
- [226: What are util.types and util.isDeepStrictEqual?](#226-what-are-utiltypes-and-utilisdeepstrictequal)
- [227: What are common mistakes when handling errors in async code?](#227-what-are-common-mistakes-when-handling-errors-in-async-code)
- [228: How do you create custom error classes?](#228-how-do-you-create-custom-error-classes)
- [229: What is the difference between operational errors and programmer errors?](#229-what-is-the-difference-between-operational-errors-and-programmer-errors)
- [230: How do you keep a Node.js app running in production?](#230-how-do-you-keep-a-nodejs-app-running-in-production)
- [231: What are good practices for running Node.js in Docker?](#231-what-are-good-practices-for-running-nodejs-in-docker)
- [232: Why should you validate environment variables at startup?](#232-why-should-you-validate-environment-variables-at-startup)
- [233: What caching strategies can you use in a Node.js app?](#233-what-caching-strategies-can-you-use-in-a-nodejs-app)
- [234: What are common causes of memory leaks in Node.js?](#234-what-are-common-causes-of-memory-leaks-in-nodejs)
- [235: How do you measure how long code takes in Node.js?](#235-how-do-you-measure-how-long-code-takes-in-nodejs)
- [236: How do you measure event loop delay?](#236-how-do-you-measure-event-loop-delay)
- [237: How do you find code that blocks the event loop?](#237-how-do-you-find-code-that-blocks-the-event-loop)
- [238: How do you handle CPU-heavy work in a Node.js server?](#238-how-do-you-handle-cpu-heavy-work-in-a-nodejs-server)
- [239: Why can JSON.parse and JSON.stringify be a problem on a server?](#239-why-can-jsonparse-and-jsonstringify-be-a-problem-on-a-server)
- [240: How do you return a large list of records from an API efficiently?](#240-how-do-you-return-a-large-list-of-records-from-an-api-efficiently)
- [241: What is database connection pooling and why is it important?](#241-what-is-database-connection-pooling-and-why-is-it-important)
- [242: How do you prevent SQL injection?](#242-how-do-you-prevent-sql-injection)
- [243: How do you use transactions and prepared statements with node:sqlite?](#243-how-do-you-use-transactions-and-prepared-statements-with-nodesqlite)
- [244: What HTTP security headers should a Node.js app set?](#244-what-http-security-headers-should-a-nodejs-app-set)
- [245: What is prototype pollution?](#245-what-is-prototype-pollution)
- [246: What is ReDoS?](#246-what-is-redos)
- [247: How do you protect a project from malicious or vulnerable npm packages?](#247-how-do-you-protect-a-project-from-malicious-or-vulnerable-npm-packages)
- [248: What is path traversal and how do you prevent it?](#248-what-is-path-traversal-and-how-do-you-prevent-it)
- [249: How do you set up an HTTPS server with good TLS settings?](#249-how-do-you-set-up-an-https-server-with-good-tls-settings)
- [250: What is the http2 module and when would you use it?](#250-what-is-the-http2-module-and-when-would-you-use-it)
- [251: How do you compress HTTP responses with zlib?](#251-how-do-you-compress-http-responses-with-zlib)
- [252: How do you encrypt and decrypt data with crypto?](#252-how-do-you-encrypt-and-decrypt-data-with-crypto)
- [253: What is the difference between Math.random and crypto random functions?](#253-what-is-the-difference-between-mathrandom-and-crypto-random-functions)
- [254: What is the Web Crypto API in Node.js?](#254-what-is-the-web-crypto-api-in-nodejs)
- [255: How do you verify a webhook signature?](#255-how-do-you-verify-a-webhook-signature)
- [256: How do you read a very large file line by line?](#256-how-do-you-read-a-very-large-file-line-by-line)
- [257: What is the difference between fs.watch and fs.watchFile?](#257-what-is-the-difference-between-fswatch-and-fswatchfile)
- [258: How do you find files with glob patterns without a library?](#258-how-do-you-find-files-with-glob-patterns-without-a-library)
- [259: What is a FileHandle and when do you use fs.open?](#259-what-is-a-filehandle-and-when-do-you-use-fsopen)
- [260: How do you create temporary files and folders safely?](#260-how-do-you-create-temporary-files-and-folders-safely)
- [261: How do you write a file atomically?](#261-how-do-you-write-a-file-atomically)
- [262: What is AsyncLocalStorage?](#262-what-is-asynclocalstorage)
- [263: What is diagnostics_channel?](#263-what-is-diagnostics_channel)
- [264: What do timer.unref() and timer.ref() do?](#264-what-do-timerunref-and-timerref-do)
- [265: Why is setInterval not exact, and how do you run something at a steady rate?](#265-why-is-setinterval-not-exact-and-how-do-you-run-something-at-a-steady-rate)
- [266: What is Promise.withResolvers?](#266-what-is-promisewithresolvers)
- [267: Which newer JavaScript features can you use in current Node.js LTS versions?](#267-which-newer-javascript-features-can-you-use-in-current-nodejs-lts-versions)
- [268: What is explicit resource management (using / await using)?](#268-what-is-explicit-resource-management-using--await-using)
- [269: What can't structuredClone copy?](#269-what-cant-structuredclone-copy)
- [270: How do you build a WebSocket server in Node.js?](#270-how-do-you-build-a-websocket-server-in-nodejs)
- [271: What are Server-Sent Events and how do you implement them?](#271-what-are-server-sent-events-and-how-do-you-implement-them)
- [272: How do you handle CORS without a library?](#272-how-do-you-handle-cors-without-a-library)
- [273: What is the difference between REST, GraphQL and gRPC?](#273-what-is-the-difference-between-rest-graphql-and-grpc)
- [274: How do microservices written in Node.js talk to each other?](#274-how-do-microservices-written-in-nodejs-talk-to-each-other)
- [275: What are message queues and when should you use one?](#275-what-are-message-queues-and-when-should-you-use-one)
- [276: What is idempotency and why does it matter for APIs?](#276-what-is-idempotency-and-why-does-it-matter-for-apis)
- [277: How do you version an API?](#277-how-do-you-version-an-api)
- [278: How do you set up a monorepo for several Node.js packages?](#278-how-do-you-set-up-a-monorepo-for-several-nodejs-packages)
- [279: How do you publish a package to npm?](#279-how-do-you-publish-a-package-to-npm)
- [280: What are the limits of Node's built-in TypeScript support?](#280-what-are-the-limits-of-nodes-built-in-typescript-support)
- [281: What are the alternatives for running TypeScript in Node.js?](#281-what-are-the-alternatives-for-running-typescript-in-nodejs)
- [282: How do you deal with dates and time zones on the server?](#282-how-do-you-deal-with-dates-and-time-zones-on-the-server)
- [283: What is process.hrtime.bigint() used for?](#283-what-is-processhrtimebigint-used-for)
- [284: Why use os.availableParallelism() instead of os.cpus().length?](#284-why-use-osavailableparallelism-instead-of-oscpuslength)
- [285: What is a Single Executable Application (SEA)?](#285-what-is-a-single-executable-application-sea)
- [286: What is the Node.js permission model?](#286-what-is-the-nodejs-permission-model)
- [287: How do the --watch flags work in detail?](#287-how-do-the---watch-flags-work-in-detail)
- [288: How does node --run differ from npm run?](#288-how-does-node---run-differ-from-npm-run)
- [289: When should you use fetch, and when the http module or undici directly?](#289-when-should-you-use-fetch-and-when-the-http-module-or-undici-directly)
- [290: How do you process a very large JSON file without loading it all into memory?](#290-how-do-you-process-a-very-large-json-file-without-loading-it-all-into-memory)
- [291: What is event loop utilization (ELU)?](#291-what-is-event-loop-utilization-elu)
- [292: How should you design health check endpoints?](#292-how-should-you-design-health-check-endpoints)
- [293: What changes when your Node app runs behind a reverse proxy or load balancer?](#293-what-changes-when-your-node-app-runs-behind-a-reverse-proxy-or-load-balancer)
- [294: What are sticky sessions and when do you need them?](#294-what-are-sticky-sessions-and-when-do-you-need-them)
- [295: How do you implement retries with exponential backoff?](#295-how-do-you-implement-retries-with-exponential-backoff)
- [296: What is a circuit breaker?](#296-what-is-a-circuit-breaker)
- [297: How do you run scheduled jobs (cron) in Node.js?](#297-how-do-you-run-scheduled-jobs-cron-in-nodejs)
- [298: What can and can't you do in a process.on('exit') handler?](#298-what-can-and-cant-you-do-in-a-processonexit-handler)
- [299: What is the difference between the beforeExit and exit events?](#299-what-is-the-difference-between-the-beforeexit-and-exit-events)
- [300: How do you handle Ctrl+C correctly in a CLI tool?](#300-how-do-you-handle-ctrlc-correctly-in-a-cli-tool)

### Advanced Questions (301-450)

- [301: How does the event loop work inside libuv?](#301-how-does-the-event-loop-work-inside-libuv)
- [302: Why does network I/O scale well in Node, while file I/O goes to the thread pool?](#302-why-does-network-io-scale-well-in-node-while-file-io-goes-to-the-thread-pool)
- [303: How does V8 execute JavaScript? What are Ignition, Sparkplug, Maglev and TurboFan?](#303-how-does-v8-execute-javascript-what-are-ignition-sparkplug-maglev-and-turbofan)
- [304: What are hidden classes and inline caches?](#304-what-are-hidden-classes-and-inline-caches)
- [305: What causes V8 to deoptimize a function?](#305-what-causes-v8-to-deoptimize-a-function)
- [306: How is the V8 heap organized?](#306-how-is-the-v8-heap-organized)
- [307: How does garbage collection work in V8 (Orinoco)?](#307-how-does-garbage-collection-work-in-v8-orinoco)
- [308: How do you control V8 heap size, and what do you need to know about containers?](#308-how-do-you-control-v8-heap-size-and-what-do-you-need-to-know-about-containers)
- [309: How do you take a heap snapshot, including in production?](#309-how-do-you-take-a-heap-snapshot-including-in-production)
- [310: How do you find a memory leak step by step?](#310-how-do-you-find-a-memory-leak-step-by-step)
- [311: What are WeakRef and FinalizationRegistry, and should you use them?](#311-what-are-weakref-and-finalizationregistry-and-should-you-use-them)
- [312: When is a WeakMap a good choice?](#312-when-is-a-weakmap-a-good-choice)
- [313: How do you CPU-profile a Node.js app and read a flame graph?](#313-how-do-you-cpu-profile-a-nodejs-app-and-read-a-flame-graph)
- [314: What are --prof and --prof-process?](#314-what-are---prof-and---prof-process)
- [315: What is a diagnostic report?](#315-what-is-a-diagnostic-report)
- [316: What are async_hooks, and why are they discouraged?](#316-what-are-async_hooks-and-why-are-they-discouraged)
- [317: How does AsyncLocalStorage work internally, and what changed in Node 24?](#317-how-does-asynclocalstorage-work-internally-and-what-changed-in-node-24)
- [318: What are tracing channels in diagnostics_channel?](#318-what-are-tracing-channels-in-diagnostics_channel)
- [319: How does OpenTelemetry instrument a Node app, and why does --import matter?](#319-how-does-opentelemetry-instrument-a-node-app-and-why-does---import-matter)
- [320: What are module customization hooks?](#320-what-are-module-customization-hooks)
- [321: What is the difference between --import and --require?](#321-what-is-the-difference-between---import-and---require)
- [322: How does loading an ES module work under the hood?](#322-how-does-loading-an-es-module-work-under-the-hood)
- [323: What are live bindings in ESM?](#323-what-are-live-bindings-in-esm)
- [324: How does Node let you import named exports from a CommonJS module?](#324-how-does-node-let-you-import-named-exports-from-a-commonjs-module)
- [325: What are the limits of require(esm)?](#325-what-are-the-limits-of-requireesm)
- [326: How do custom export conditions work, and what conditions does Node know?](#326-how-do-custom-export-conditions-work-and-what-conditions-does-node-know)
- [327: How do you write a native addon, and what is Node-API?](#327-how-do-you-write-a-native-addon-and-what-is-node-api)
- [328: How do you use WebAssembly and WASI in Node.js?](#328-how-do-you-use-webassembly-and-wasi-in-nodejs)
- [329: How are worker threads implemented, and what are resourceLimits?](#329-how-are-worker-threads-implemented-and-what-are-resourcelimits)
- [330: What are MessageChannel and BroadcastChannel used for?](#330-what-are-messagechannel-and-broadcastchannel-used-for)
- [331: How can you implement a mutex between worker threads with Atomics?](#331-how-can-you-implement-a-mutex-between-worker-threads-with-atomics)
- [332: How can the libuv thread pool become a bottleneck, and how do you fix it?](#332-how-can-the-libuv-thread-pool-become-a-bottleneck-and-how-do-you-fix-it)
- [333: What is the difference between dns.lookup and dns.resolve, and why does it matter?](#333-what-is-the-difference-between-dnslookup-and-dnsresolve-and-why-does-it-matter)
- [334: Why might you see random 502 errors behind a load balancer, and how do you fix them?](#334-why-might-you-see-random-502-errors-behind-a-load-balancer-and-how-do-you-fix-them)
- [335: What is undici's dispatcher, and how do you configure fetch globally?](#335-what-is-undicis-dispatcher-and-how-do-you-configure-fetch-globally)
- [336: How do HTTP/2 streams and flow control work in Node?](#336-how-do-http2-streams-and-flow-control-work-in-node)
- [337: What do SNI, ALPN and TLS session resumption do?](#337-what-do-sni-alpn-and-tls-session-resumption-do)
- [338: How do Readable streams work internally?](#338-how-do-readable-streams-work-internally)
- [339: How should you handle errors and cleanup in streams?](#339-how-should-you-handle-errors-and-cleanup-in-streams)
- [340: How do you write a lot of data to a stream manually without blowing up memory?](#340-how-do-you-write-a-lot-of-data-to-a-stream-manually-without-blowing-up-memory)
- [341: How do async generators work with pipeline?](#341-how-do-async-generators-work-with-pipeline)
- [342: What are stream operators like map and filter, and how does compose work?](#342-what-are-stream-operators-like-map-and-filter-and-how-does-compose-work)
- [343: How does Node's Buffer pool work, and what is allocUnsafeSlow?](#343-how-does-nodes-buffer-pool-work-and-what-is-allocunsafeslow)
- [344: Why is Buffer.slice deprecated, and what should you use?](#344-why-is-bufferslice-deprecated-and-what-should-you-use)
- [345: What encoding problems can you run into with Buffers and strings?](#345-what-encoding-problems-can-you-run-into-with-buffers-and-strings)
- [346: Why is running Node as PID 1 in Docker a problem?](#346-why-is-running-node-as-pid-1-in-docker-a-problem)
- [347: How do you do a zero-downtime graceful shutdown in Kubernetes?](#347-how-do-you-do-a-zero-downtime-graceful-shutdown-in-kubernetes)
- [348: How can you reload a clustered app without downtime?](#348-how-can-you-reload-a-clustered-app-without-downtime)
- [349: What do you need to consider when scaling Node.js horizontally?](#349-what-do-you-need-to-consider-when-scaling-nodejs-horizontally)
- [350: How would you monitor event loop health in production and act on it?](#350-how-would-you-monitor-event-loop-health-in-production-and-act-on-it)
- [351: How do you use PerformanceObserver and the perf_hooks histogram?](#351-how-do-you-use-performanceobserver-and-the-perf_hooks-histogram)
- [352: What are common mistakes in micro-benchmarks?](#352-what-are-common-mistakes-in-micro-benchmarks)
- [353: How can you make JSON serialization faster?](#353-how-can-you-make-json-serialization-faster)
- [354: What is a megamorphic call site and how does it affect performance?](#354-what-is-a-megamorphic-call-site-and-how-does-it-affect-performance)
- [355: How do you speed up Node.js startup?](#355-how-do-you-speed-up-nodejs-startup)
- [356: What is a startup snapshot?](#356-what-is-a-startup-snapshot)
- [357: What should you know when shipping a Single Executable Application?](#357-what-should-you-know-when-shipping-a-single-executable-application)
- [358: How does the permission model work in more detail?](#358-how-does-the-permission-model-work-in-more-detail)
- [359: Can the vm module be used to run untrusted code safely?](#359-can-the-vm-module-be-used-to-run-untrusted-code-safely)
- [360: What is the vm module actually good for?](#360-what-is-the-vm-module-actually-good-for)
- [361: How do you protect an app from prototype pollution in depth?](#361-how-do-you-protect-an-app-from-prototype-pollution-in-depth)
- [362: What timing attacks exist besides string comparison, and how do you prevent them?](#362-what-timing-attacks-exist-besides-string-comparison-and-how-do-you-prevent-them)
- [363: What is SSRF and how do you prevent it in Node.js?](#363-what-is-ssrf-and-how-do-you-prevent-it-in-nodejs)
- [364: How do you set a strict Content Security Policy for server-rendered pages?](#364-how-do-you-set-a-strict-content-security-policy-for-server-rendered-pages)
- [365: How do you avoid leaking secrets from a Node.js process?](#365-how-do-you-avoid-leaking-secrets-from-a-nodejs-process)
- [366: What supply chain attacks target npm, and how do you defend against them?](#366-what-supply-chain-attacks-target-npm-and-how-do-you-defend-against-them)
- [367: Why should you crash on uncaughtException instead of continuing?](#367-why-should-you-crash-on-uncaughtexception-instead-of-continuing)
- [368: What was the domain module and why is it deprecated?](#368-what-was-the-domain-module-and-why-is-it-deprecated)
- [369: What do the --unhandled-rejections modes do?](#369-what-do-the---unhandled-rejections-modes-do)
- [370: How can promises cause memory leaks?](#370-how-can-promises-cause-memory-leaks)
- [371: How do async stack traces and source maps work in Node?](#371-how-do-async-stack-traces-and-source-maps-work-in-node)
- [372: What are Error.captureStackTrace and Error.stackTraceLimit?](#372-what-are-errorcapturestacktrace-and-errorstacktracelimit)
- [373: How do you work with AggregateError and error cause chains?](#373-how-do-you-work-with-aggregateerror-and-error-cause-chains)
- [374: How do you pass cancellation through all layers of an app?](#374-how-do-you-pass-cancellation-through-all-layers-of-an-app)
- [375: How do you write a concurrency limiter (like p-limit) from scratch?](#375-how-do-you-write-a-concurrency-limiter-like-p-limit-from-scratch)
- [376: How do you implement a token bucket rate limiter?](#376-how-do-you-implement-a-token-bucket-rate-limiter)
- [377: How do you implement an LRU cache?](#377-how-do-you-implement-an-lru-cache)
- [378: How would you implement a basic EventEmitter yourself?](#378-how-would-you-implement-a-basic-eventemitter-yourself)
- [379: How would you implement util.promisify yourself?](#379-how-would-you-implement-utilpromisify-yourself)
- [380: How would you implement Promise.all yourself?](#380-how-would-you-implement-promiseall-yourself)
- [381: How do Koa-style middleware (compose) work? Implement it.](#381-how-do-koa-style-middleware-compose-work-implement-it)
- [382: What is request coalescing (single flight), and how do you implement it?](#382-what-is-request-coalescing-single-flight-and-how-do-you-implement-it)
- [383: What is a cache stampede and how do you prevent it?](#383-what-is-a-cache-stampede-and-how-do-you-prevent-it)
- [384: How do you implement a distributed lock with Redis, and what are its limits?](#384-how-do-you-implement-a-distributed-lock-with-redis-and-what-are-its-limits)
- [385: What is the transactional outbox pattern?](#385-what-is-the-transactional-outbox-pattern)
- [386: How do you build a reliable message consumer?](#386-how-do-you-build-a-reliable-message-consumer)
- [387: How do you handle backpressure between services, not just inside streams?](#387-how-do-you-handle-backpressure-between-services-not-just-inside-streams)
- [388: How do you stream a large upload directly to object storage?](#388-how-do-you-stream-a-large-upload-directly-to-object-storage)
- [389: How do you parse a huge CSV file efficiently?](#389-how-do-you-parse-a-huge-csv-file-efficiently)
- [390: How do you manage database connections in serverless functions?](#390-how-do-you-manage-database-connections-in-serverless-functions)
- [391: What affects cold start time for Node.js on serverless platforms?](#391-what-affects-cold-start-time-for-nodejs-on-serverless-platforms)
- [392: How are edge runtimes different from Node.js?](#392-how-are-edge-runtimes-different-from-nodejs)
- [393: How compatible are Bun and Deno with Node.js?](#393-how-compatible-are-bun-and-deno-with-nodejs)
- [394: What is HTTP request smuggling, and how does Node protect against it?](#394-what-is-http-request-smuggling-and-how-does-node-protect-against-it)
- [395: What is a Slowloris attack, and which Node settings help?](#395-what-is-a-slowloris-attack-and-which-node-settings-help)
- [396: How do you protect a Node API from payload-based denial of service?](#396-how-do-you-protect-a-node-api-from-payload-based-denial-of-service)
- [397: How do you use the inspector module programmatically?](#397-how-do-you-use-the-inspector-module-programmatically)
- [398: How do you debug a running production process safely?](#398-how-do-you-debug-a-running-production-process-safely)
- [399: How do you investigate crashes in native code or hard-to-reproduce aborts?](#399-how-do-you-investigate-crashes-in-native-code-or-hard-to-reproduce-aborts)
- [400: Which V8 and Node trace flags are useful for performance work?](#400-which-v8-and-node-trace-flags-are-useful-for-performance-work)
- [401: How are timers implemented in Node.js?](#401-how-are-timers-implemented-in-nodejs)
- [402: What changed in Node 11 about microtasks between timers, and why does it matter?](#402-what-changed-in-node-11-about-microtasks-between-timers-and-why-does-it-matter)
- [403: What happens when a queueMicrotask callback throws?](#403-what-happens-when-a-queuemicrotask-callback-throws)
- [404: What keeps a Node process alive, and how do you see it?](#404-what-keeps-a-node-process-alive-and-how-do-you-see-it)
- [405: Why does a test process hang after all tests pass, and how do you fix it?](#405-why-does-a-test-process-hang-after-all-tests-pass-and-how-do-you-fix-it)
- [406: Why can RSS grow even when the JS heap is stable?](#406-why-can-rss-grow-even-when-the-js-heap-is-stable)
- [407: How can small strings keep large strings in memory?](#407-how-can-small-strings-keep-large-strings-in-memory)
- [408: How do closures cause unexpected memory retention?](#408-how-do-closures-cause-unexpected-memory-retention)
- [409: What are elements kinds in V8 arrays, and why do they matter?](#409-what-are-elements-kinds-in-v8-arrays-and-why-do-they-matter)
- [410: When should you use BigInt, and what are its costs?](#410-when-should-you-use-bigint-and-what-are-its-costs)
- [411: How does internationalization (Intl) work in Node.js?](#411-how-does-internationalization-intl-work-in-nodejs)
- [412: How do Node-API versions and prebuilt binaries work?](#412-how-do-node-api-versions-and-prebuilt-binaries-work)
- [413: What problems do people hit with node-gyp, and how do you avoid them?](#413-what-problems-do-people-hit-with-node-gyp-and-how-do-you-avoid-them)
- [414: What must a native addon do to work in worker threads?](#414-what-must-a-native-addon-do-to-work-in-worker-threads)
- [415: What cross-platform problems should you watch for in Node.js code?](#415-what-cross-platform-problems-should-you-watch-for-in-nodejs-code)
- [416: What are the advanced options when spawning child processes?](#416-what-are-the-advanced-options-when-spawning-child-processes)
- [417: Why does spawning a .bat or .cmd file on Windows fail without shell: true?](#417-why-does-spawning-a-bat-or-cmd-file-on-windows-fail-without-shell-true)
- [418: How do you stream data through an external program like ffmpeg?](#418-how-do-you-stream-data-through-an-external-program-like-ffmpeg)
- [419: Why does my CLI crash with EPIPE when piped to head, and how do you fix it?](#419-why-does-my-cli-crash-with-epipe-when-piped-to-head-and-how-do-you-fix-it)
- [420: Are process.stdout writes synchronous or asynchronous?](#420-are-processstdout-writes-synchronous-or-asynchronous)
- [421: How do pino transports use worker threads, and why?](#421-how-do-pino-transports-use-worker-threads-and-why)
- [422: How should you publish a library in 2026 to support both ESM and CommonJS users?](#422-how-should-you-publish-a-library-in-2026-to-support-both-esm-and-commonjs-users)
- [423: Which tsconfig settings work best with Node's native TypeScript support?](#423-which-tsconfig-settings-work-best-with-nodes-native-typescript-support)
- [424: What advanced features does node:test have for larger projects?](#424-what-advanced-features-does-nodetest-have-for-larger-projects)
- [425: How do you test code that depends on time and timers?](#425-how-do-you-test-code-that-depends-on-time-and-timers)
- [426: How do you write integration tests against real databases and services?](#426-how-do-you-write-integration-tests-against-real-databases-and-services)
- [427: How do you benchmark an HTTP server?](#427-how-do-you-benchmark-an-http-server)
- [428: How do you estimate how many instances you need?](#428-how-do-you-estimate-how-many-instances-you-need)
- [429: How do you expose application metrics from Node.js?](#429-how-do-you-expose-application-metrics-from-nodejs)
- [430: How do you add a request ID to every log line automatically?](#430-how-do-you-add-a-request-id-to-every-log-line-automatically)
- [431: How can you reload configuration without restarting the process?](#431-how-can-you-reload-configuration-without-restarting-the-process)
- [432: How would you build a plugin system in Node.js?](#432-how-would-you-build-a-plugin-system-in-nodejs)
- [433: How do you do dependency injection in Node.js without a framework?](#433-how-do-you-do-dependency-injection-in-nodejs-without-a-framework)
- [434: How would you structure a large Node.js backend?](#434-how-would-you-structure-a-large-nodejs-backend)
- [435: How should you handle money and decimal numbers in Node.js?](#435-how-should-you-handle-money-and-decimal-numbers-in-nodejs)
- [436: How do you read and write binary data formats in Node.js?](#436-how-do-you-read-and-write-binary-data-formats-in-nodejs)
- [437: How do you handle message framing over a TCP socket?](#437-how-do-you-handle-message-framing-over-a-tcp-socket)
- [438: How do you write a simple HTTP reverse proxy with streams?](#438-how-do-you-write-a-simple-http-reverse-proxy-with-streams)
- [439: How does await work internally, and why did it get faster?](#439-how-does-await-work-internally-and-why-did-it-get-faster)
- [440: What are DisposableStack and AsyncDisposableStack?](#440-what-are-disposablestack-and-asyncdisposablestack)
- [441: What is the Node.js stability index, and how do features become stable?](#441-what-is-the-nodejs-stability-index-and-how-do-features-become-stable)
- [442: How do v8.serialize and the "advanced" IPC serialization work?](#442-how-do-v8serialize-and-the-advanced-ipc-serialization-work)
- [443: How does Node's model compare to thread-per-request servers?](#443-how-does-nodes-model-compare-to-thread-per-request-servers)
- [444: How does Node parse HTTP requests?](#444-how-does-node-parse-http-requests)
- [445: How would you design a reliable webhook delivery system in Node.js?](#445-how-would-you-design-a-reliable-webhook-delivery-system-in-nodejs)
- [446: How would you design a real-time chat backend in Node.js?](#446-how-would-you-design-a-real-time-chat-backend-in-nodejs)
- [447: What is the N+1 query problem, and how do you solve it in Node?](#447-what-is-the-n1-query-problem-and-how-do-you-solve-it-in-node)
- [448: Why should you always consume or cancel a fetch response body?](#448-why-should-you-always-consume-or-cancel-a-fetch-response-body)
- [449: What is "releasing Zalgo", and how do you avoid it?](#449-what-is-releasing-zalgo-and-how-do-you-avoid-it)
- [450: What are the most important changes in recent Node.js versions (22, 24 and newer)?](#450-what-are-the-most-important-changes-in-recent-nodejs-versions-22-24-and-newer)

---

## Easy Questions

### 1: What is Node.js?

Node.js is a runtime that lets you run JavaScript outside the browser. It uses Google's V8 engine to execute JavaScript and the libuv library to handle things like files, networking and timers. People mostly use it to build web servers, APIs, command line tools and build tooling.

```js
// hello.js
console.log("Hello from Node.js");
```

```bash
node hello.js
```

### 2: Is Node.js a programming language or a framework?

Neither. The language is JavaScript (or TypeScript, which Node can now run after stripping types). Node.js is a runtime environment. Frameworks like Express, Fastify or NestJS are built on top of Node.js.

### 3: What is V8?

V8 is the JavaScript engine written by Google for Chrome. It compiles JavaScript to machine code and manages memory with a garbage collector. Node.js embeds V8, so the JavaScript features you get in Node depend on the V8 version that ships with it. You can check it with:

```bash
node -p process.versions.v8
```

### 4: What is libuv?

libuv is a C library that Node.js uses for asynchronous I/O. It provides the event loop, a thread pool, and a common API over the operating system's async mechanisms (epoll on Linux, kqueue on macOS, IOCP on Windows). File system operations, DNS lookups and some crypto work run on its thread pool, while network sockets use the OS's non-blocking APIs directly.

### 5: Is Node.js single-threaded?

Your JavaScript code runs on a single main thread. But Node.js itself is not fully single-threaded. libuv has a thread pool (4 threads by default) for blocking work like file reads, and V8 uses extra threads for garbage collection and compilation. You can also create your own threads with the `worker_threads` module.

### 6: What is the event loop?

The event loop is what lets Node.js handle many operations without blocking. Node starts slow operations (reading a file, waiting for a network response), keeps running other code, and when an operation finishes, its callback is put in a queue. The event loop keeps picking callbacks from these queues and running them on the main thread.

```js
console.log("start");

setTimeout(() => console.log("timeout done"), 0);

console.log("end");
// start
// end
// timeout done
```

### 7: What does non-blocking I/O mean?

It means that when Node.js asks for I/O (disk, network), it does not sit and wait for the result. It continues with the next piece of code and gets notified later when the data is ready. This is why one Node process can serve thousands of connections at the same time.

### 8: What is the difference between blocking and non-blocking code? Give an example.

Blocking code stops everything until it finishes. Non-blocking code starts the work and lets the program continue.

```js
import fs from "node:fs";

// Blocking
const data = fs.readFileSync("file.txt", "utf8");
console.log(data);
console.log("This runs after the file is read");

// Non-blocking
fs.readFile("file.txt", "utf8", (err, data) => {
  if (err) throw err;
  console.log(data);
});
console.log("This runs before the file is read");
```

In a server, blocking calls hurt every user because no other request can be handled while the main thread is busy.

### 9: How do you check which version of Node.js and npm you have?

```bash
node -v        # or node --version
npm -v
node -p process.versions   # versions of V8, libuv, OpenSSL and others
```

### 10: What is npm?

npm stands for Node Package Manager. It is three things: a public registry of packages (npmjs.com), a command line tool that comes with Node.js, and the format for describing packages (`package.json`). You use it to install libraries, run scripts and publish your own packages.

```bash
npm install express
npm uninstall express
npm update
```

### 11: What is package.json?

It is the main file that describes a Node.js project. It holds the project name, version, scripts, dependencies, the module type and other settings.

```json
{
  "name": "my-app",
  "version": "1.0.0",
  "type": "module",
  "main": "index.js",
  "scripts": {
    "start": "node index.js",
    "test": "node --test"
  },
  "dependencies": {
    "express": "^5.1.0"
  },
  "devDependencies": {
    "eslint": "^9.0.0"
  }
}
```

You can create one with `npm init` or `npm init -y`.

### 12: What is package-lock.json and should you commit it?

`package-lock.json` records the exact version of every package that was installed, including nested dependencies. This makes installs repeatable, so every developer and every CI run gets the same tree. Yes, you should commit it for applications. For libraries it is still useful for your own development, but users of your library will not use it.

### 13: What is the difference between dependencies and devDependencies?

`dependencies` are packages your app needs to run in production (for example `express`). `devDependencies` are only needed during development or build (test tools, linters, TypeScript compiler).

```bash
npm install express          # goes to dependencies
npm install -D typescript    # goes to devDependencies
npm install --omit=dev       # install without devDependencies
```

### 14: What is the difference between npm install and npm ci?

`npm install` reads `package.json`, can update the lock file, and installs what is needed. `npm ci` is made for CI and production builds. It deletes `node_modules`, installs exactly what is in `package-lock.json`, and fails if the lock file and `package.json` do not match. It never changes the lock file.

### 15: What is npx?

`npx` runs a command from an npm package without installing it globally. If the package is installed locally it uses that one, otherwise it downloads it to a cache and runs it.

```bash
npx create-vite@latest my-app
npx eslint .
```

### 16: What is semantic versioning and what do ^ and ~ mean?

Semantic versioning uses `MAJOR.MINOR.PATCH`. A major bump means breaking changes, minor means new features that do not break anything, patch means bug fixes.

- `^1.4.2` allows `1.x.x` updates, so `>=1.4.2 <2.0.0`.
- `~1.4.2` allows only patch updates, so `>=1.4.2 <1.5.0`.
- `1.4.2` means that exact version.

For `0.x` versions `^` is stricter: `^0.4.2` means `>=0.4.2 <0.5.0`.

### 17: What is the difference between a global and a local package install?

A local install (`npm install pkg`) puts the package in the project's `node_modules` and adds it to `package.json`. A global install (`npm install -g pkg`) puts it in a system-wide folder so its commands are available everywhere. Prefer local installs and `npx` for project tools so every developer uses the same version.

### 18: What are npm scripts?

They are commands defined in the `scripts` section of `package.json`. npm adds `node_modules/.bin` to the PATH when running them, so you can call local tools by name.

```json
{
  "scripts": {
    "dev": "node --watch src/index.js",
    "test": "node --test",
    "lint": "eslint ."
  }
}
```

```bash
npm run dev
npm test        # start, test, stop and restart don't need "run"
```

### 19: What is a module in Node.js?

A module is a file (or a package) whose code is isolated from other files. Variables inside it are private unless you export them. Node supports two module systems: CommonJS (`require`) and ECMAScript modules (`import`).

### 20: What is the difference between CommonJS and ES modules?

|                   | CommonJS                       | ES modules                               |
| ----------------- | ------------------------------ | ---------------------------------------- |
| Syntax            | `require()` / `module.exports` | `import` / `export`                      |
| Loading           | Synchronous                    | Asynchronous, parsed before running      |
| File extension    | `.js` (default) or `.cjs`      | `.mjs`, or `.js` with `"type": "module"` |
| Top-level `await` | No                             | Yes                                      |
| `__dirname`       | Available                      | Use `import.meta.dirname`                |

ES modules are the standard for JavaScript and are recommended for new code.

```js
// CommonJS
const fs = require("node:fs");
module.exports = { add: (a, b) => a + b };

// ES module
import fs from "node:fs";
export const add = (a, b) => a + b;
```

### 21: How do you use ES modules in Node.js?

Either name the file with `.mjs`, or add `"type": "module"` to `package.json` so all `.js` files in that package are treated as ES modules.

```json
{
  "type": "module"
}
```

In recent versions Node can also detect ES module syntax in a `.js` file with no `type` field and run it as ESM, but setting `"type"` explicitly is clearer and faster.

### 22: How does require() work at a basic level?

`require()` takes a module name or path, finds the file, wraps its code in a function, runs it once, and returns its `module.exports`. The result is cached, so requiring the same file again returns the same object without running the code again.

```js
const math = require("./math.js");
console.log(math.add(2, 3));
```

### 23: What is the difference between module.exports and exports?

`exports` is just a shortcut that points to `module.exports`. You can add properties to it, but if you reassign `exports` itself the link breaks and nothing is exported. `require()` always returns `module.exports`.

```js
// Works
exports.hello = () => "hi";

// Works
module.exports = { hello: () => "hi" };

// Does NOT work, exports now points to a new object
exports = { hello: () => "hi" };
```

### 24: How do import and export work in ES modules?

```js
// math.js
export const PI = 3.14;
export function add(a, b) {
  return a + b;
}
export default function multiply(a, b) {
  return a * b;
}

// app.js
import multiply, { add, PI } from "./math.js";
import * as math from "./math.js";
```

In ES modules you must include the file extension in relative imports (`./math.js`, not `./math`).

### 25: What are core modules in Node.js?

Core (built-in) modules come with Node.js, so you don't install them. Examples: `fs`, `path`, `http`, `https`, `os`, `events`, `stream`, `crypto`, `url`, `util`, `child_process`, `worker_threads`, `zlib`, `test`, `sqlite`.

```js
import { readFile } from "node:fs/promises";
import os from "node:os";
```

### 26: Why should you use the node: prefix when importing core modules?

The `node:` prefix makes it clear that you mean the built-in module and not a package from npm with the same name. It also skips the lookup in `node_modules`. Some newer modules only work with the prefix, like `node:test`, `node:sqlite` and `node:sea`.

```js
import { test } from "node:test"; // prefix required
import fs from "node:fs"; // prefix recommended
```

### 27: What are `__dirname` and `__filename`? How do you get them in ES modules?

In CommonJS, `__dirname` is the folder of the current file and `__filename` is its full path. They don't exist in ES modules. Since Node 20.11 you can use `import.meta.dirname` and `import.meta.filename`.

```js
// CommonJS
console.log(__dirname, __filename);

// ES module
console.log(import.meta.dirname, import.meta.filename);

// Older way in ESM
import { fileURLToPath } from "node:url";
import path from "node:path";
const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);
```

### 28: What is the global object in Node.js?

In Node the global object is called `global`, and the standard name that works everywhere (browser, Node, workers) is `globalThis`. Things like `setTimeout`, `console`, `process`, `fetch`, `URL` and `structuredClone` are available globally. Unlike browsers, variables declared at the top level of a module do not become properties of the global object.

```js
globalThis.appName = "demo"; // avoid this in real code
console.log(appName);
```

### 29: What is the process object?

`process` is a global object that gives information about and control over the current Node.js process: arguments, environment variables, the current directory, memory usage, exit codes, and events like `exit` or signals.

```js
console.log(process.pid);
console.log(process.platform); // 'linux', 'darwin', 'win32'
console.log(process.cwd());
console.log(process.uptime());
```

### 30: What is process.argv?

It is an array of the command line arguments. The first item is the path to the Node binary, the second is the path to the script, and the rest are the arguments you passed.

```js
// node app.js hello --port=3000
console.log(process.argv);
// ['/usr/local/bin/node', '/path/app.js', 'hello', '--port=3000']

const args = process.argv.slice(2);
```

For real parsing, use `util.parseArgs` (see question 81).

### 31: How do you use environment variables in Node.js?

They are available through `process.env`. All values are strings (or `undefined`).

```js
const port = Number(process.env.PORT) || 3000;
const isProd = process.env.NODE_ENV === "production";
```

```bash
PORT=8080 node app.js
```

Never commit secrets to the repo. Keep them in environment variables or a secret manager.

### 32: How do you load a .env file without the dotenv package?

Node has built-in support since version 20.6. You can use the `--env-file` flag, or call `process.loadEnvFile()` from code.

```bash
node --env-file=.env app.js
node --env-file-if-exists=.env.local app.js
```

```js
process.loadEnvFile(); // loads ./.env
process.loadEnvFile(".env.dev");
console.log(process.env.DB_URL);
```

### 33: How do you exit a Node.js process, and what are exit codes?

The process exits on its own when there is nothing left to do. You can force it with `process.exit(code)`. Exit code `0` means success, anything else means failure. A better option is to set `process.exitCode` and let the process finish naturally, so pending writes (like logs) are not cut off.

```js
if (!config) {
  console.error("Missing config");
  process.exitCode = 1;
  return;
}
```

### 34: What is the Node.js REPL?

REPL means Read, Eval, Print, Loop. Running `node` with no file starts an interactive shell where you can type JavaScript and see results right away. Useful commands: `.help`, `.exit`, `.load file.js`, `.editor`. The `_` variable holds the last result. Top-level `await` works in the REPL.

```bash
$ node
> 2 + 2
4
> await fetch('https://example.com').then(r => r.status)
200
```

### 35: What are the different ways to run JavaScript code with the node command?

```bash
node app.js                 # run a file
node -e "console.log(1+1)"  # evaluate a string
node -p "1+1"               # evaluate and print the result
node --watch app.js         # restart on file changes
node --run dev              # run a package.json script
node app.ts                 # run TypeScript (type stripping)
echo "console.log('hi')" | node   # read from stdin
```

### 36: What is a callback function?

A callback is a function you pass to another function, which calls it later, usually when some work is done. Older Node.js APIs are built on callbacks.

```js
import fs from "node:fs";

fs.readFile("notes.txt", "utf8", (err, text) => {
  if (err) {
    console.error(err);
    return;
  }
  console.log(text);
});
```

### 37: What is an error-first callback?

It is the convention used by Node's callback APIs: the first argument of the callback is an error (or `null` if everything went fine), and the following arguments are the results.

```js
function divide(a, b, callback) {
  if (b === 0) {
    callback(new Error("Cannot divide by zero"));
    return;
  }
  callback(null, a / b);
}

divide(10, 2, (err, result) => {
  if (err) return console.error(err.message);
  console.log(result); // 5
});
```

### 38: What is callback hell and how do you avoid it?

Callback hell is when callbacks are nested inside callbacks many levels deep, which makes code hard to read and errors hard to handle.

```js
getUser(id, (err, user) => {
  getOrders(user, (err, orders) => {
    getInvoice(orders[0], (err, invoice) => {
      // ...
    });
  });
});
```

Fix it by using promises and `async/await`:

```js
const user = await getUser(id);
const orders = await getOrders(user);
const invoice = await getInvoice(orders[0]);
```

Other options are splitting code into named functions and using `util.promisify` for old callback APIs.

### 39: What is a Promise?

A Promise is an object that represents a value that will be available later (or an error). You attach handlers with `.then()`, `.catch()` and `.finally()`.

```js
const wait = (ms) => new Promise((resolve) => setTimeout(resolve, ms));

wait(1000)
  .then(() => console.log("1 second passed"))
  .catch((err) => console.error(err))
  .finally(() => console.log("done"));
```

### 40: What are the states of a Promise?

- **pending**: the work is still in progress.
- **fulfilled**: it finished successfully with a value.
- **rejected**: it failed with a reason (usually an `Error`).

Once a promise is fulfilled or rejected it is "settled" and its state never changes again.

### 41: What is async/await?

It is syntax built on top of promises that lets you write async code that reads like normal sequential code. An `async` function always returns a promise. `await` pauses the function until the promise settles, without blocking the thread.

```js
async function getTodo(id) {
  const res = await fetch(`https://jsonplaceholder.typicode.com/todos/${id}`);
  return res.json();
}

const todo = await getTodo(1);
console.log(todo.title);
```

### 42: How do you handle errors with async/await?

Use `try/catch` around the `await`. Any rejected promise turns into a thrown error.

```js
async function loadConfig() {
  try {
    const text = await readFile("config.json", "utf8");
    return JSON.parse(text);
  } catch (err) {
    console.error("Could not load config:", err.message);
    return {};
  }
}
```

You can also call `.catch()` on the returned promise. Don't forget to handle errors somewhere, because an unhandled rejection crashes the process by default.

### 43: What is the difference between Promise.all, Promise.allSettled, Promise.race and Promise.any?

- `Promise.all` waits for all promises and fails as soon as one fails.
- `Promise.allSettled` waits for all and gives you the status of each, never fails.
- `Promise.race` settles with the first promise that settles, success or failure.
- `Promise.any` resolves with the first success, and fails only if all fail (with an `AggregateError`).

```js
const [users, posts] = await Promise.all([getUsers(), getPosts()]);

const results = await Promise.allSettled([a(), b()]);
results.forEach((r) => console.log(r.status, r.value ?? r.reason));

const fastest = await Promise.any([mirror1(), mirror2()]);
```

### 44: What is the difference between setTimeout and setInterval?

`setTimeout` runs a function once after a delay. `setInterval` runs it again and again with the given delay between runs. Both return a `Timeout` object you can cancel.

```js
const t = setTimeout(() => console.log("once"), 1000);
clearTimeout(t);

let count = 0;
const i = setInterval(() => {
  console.log("tick", ++count);
  if (count === 3) clearInterval(i);
}, 500);
```

The delay is a minimum, not an exact time. If the main thread is busy, the callback runs later.

### 45: What is setImmediate?

`setImmediate` schedules a callback to run in the "check" phase of the event loop, right after the current I/O polling is done. It is Node-specific. It is useful when you want to run something after the current operation and after pending I/O callbacks.

```js
setImmediate(() => console.log("immediate"));
console.log("sync");
// sync
// immediate
```

### 46: What is process.nextTick?

`process.nextTick(fn)` runs `fn` right after the current operation finishes, before the event loop continues and even before promise callbacks. It is mostly used inside libraries to make sure a callback always runs asynchronously. In application code, `queueMicrotask` or promises are usually a better choice.

```js
// script.cjs (CommonJS)
process.nextTick(() => console.log("nextTick"));
Promise.resolve().then(() => console.log("promise"));
console.log("sync");
// sync
// nextTick
// promise
```

One catch: if you run the same code as an ES module (`.mjs`), you get `sync`, `promise`, `nextTick`. The top level of an ES module itself runs as part of a promise job, so the promise queue is emptied before Node gets to the `nextTick` queue.

### 47: What is the timers/promises module?

It gives you promise versions of the timer functions, so you can `await` them.

```js
import { setTimeout as sleep, setInterval } from "node:timers/promises";

await sleep(1000);
console.log("waited 1 second");

for await (const _ of setInterval(1000)) {
  console.log("every second");
  break;
}
```

It also supports an `AbortSignal` to cancel the wait.

### 48: What is the difference between fs.readFile and fs.readFileSync?

`readFileSync` blocks the main thread until the whole file is read and returns the content. `readFile` is asynchronous and gives you the content in a callback. Use the sync version only in startup code or scripts, never inside request handlers.

```js
import fs from "node:fs";

const config = fs.readFileSync("config.json", "utf8");

fs.readFile("big.log", "utf8", (err, data) => {
  if (err) throw err;
  console.log(data.length);
});
```

### 49: What is fs/promises?

It is the promise-based version of the file system API. It is the recommended way to work with files in modern code.

```js
import { readFile, writeFile, mkdir } from "node:fs/promises";

await mkdir("out", { recursive: true });
const text = await readFile("input.txt", "utf8");
await writeFile("out/output.txt", text.toUpperCase());
```

### 50: How do you write and append to a file?

```js
import { writeFile, appendFile } from "node:fs/promises";

await writeFile("log.txt", "first line\n"); // creates or overwrites
await appendFile("log.txt", "second line\n"); // adds to the end

// write JSON
await writeFile("data.json", JSON.stringify({ a: 1 }, null, 2));
```

For many small writes, a write stream (`fs.createWriteStream`) is more efficient.

### 51: How do you check if a file exists?

`fs.exists()` is deprecated. Use `fs.existsSync()` for simple sync checks, or `access()` / `stat()` with promises. Often the better approach is to just try to open or read the file and handle the `ENOENT` error, since the file can be deleted between the check and the use.

```js
import { existsSync } from "node:fs";
import { access, readFile } from "node:fs/promises";

if (existsSync("config.json")) {
  /* ... */
}

try {
  await access("config.json");
} catch {
  console.log("not found");
}

try {
  const data = await readFile("config.json", "utf8");
} catch (err) {
  if (err.code === "ENOENT") console.log("file missing");
  else throw err;
}
```

### 52: How do you read the contents of a directory?

```js
import { readdir } from "node:fs/promises";

const names = await readdir("./src");

const entries = await readdir("./src", { withFileTypes: true });
for (const e of entries) {
  console.log(e.name, e.isDirectory() ? "dir" : "file");
}

// all files in all subfolders
const all = await readdir("./src", { recursive: true });
```

### 53: How do you delete files and folders?

```js
import { unlink, rm } from "node:fs/promises";

await unlink("old.txt"); // one file
await rm("dist", { recursive: true, force: true }); // folder and everything inside
```

`force: true` means no error if the path doesn't exist. Don't use `rmdir` with `recursive`, it is deprecated in favor of `rm`.

### 54: What is the path module? What is the difference between path.join and path.resolve?

The `path` module helps you build and parse file paths in a way that works on every OS.

- `path.join()` glues segments together with the right separator and cleans up `..` and `.`.
- `path.resolve()` builds an absolute path, processing from right to left until it has an absolute one. If none is absolute, it uses the current working directory.

```js
import path from "node:path";

path.join("/users", "john", "../anna", "file.txt"); // '/users/anna/file.txt'
path.resolve("src", "index.js"); // '/current/working/dir/src/index.js'
path.resolve("/a", "/b", "c"); // '/b/c'
```

### 55: Which other path functions are useful?

```js
import path from "node:path";

const p = "/home/user/docs/report.final.pdf";
path.basename(p); // 'report.final.pdf'
path.basename(p, ".pdf"); // 'report.final'
path.dirname(p); // '/home/user/docs'
path.extname(p); // '.pdf'
path.parse(p);
// { root: '/', dir: '/home/user/docs', base: 'report.final.pdf', ext: '.pdf', name: 'report.final' }
path.isAbsolute(p); // true
path.relative("/a/b", "/a/c/d"); // '../c/d'
path.sep; // '/' or '\\'
```

### 56: What is the os module used for?

It gives information about the operating system and machine.

```js
import os from "node:os";

os.platform(); // 'linux'
os.cpus().length; // number of logical CPUs
os.availableParallelism(); // recommended way to get CPU count for parallel work
os.totalmem(); // bytes
os.freemem();
os.homedir();
os.tmpdir();
os.hostname();
os.EOL; // '\n' or '\r\n'
```

### 57: What is a Buffer?

A `Buffer` is a fixed-size chunk of raw binary data. Node uses buffers for files, network packets, images and anything that is not plain text. `Buffer` is a subclass of `Uint8Array` and is available globally.

```js
const buf = Buffer.from("Hello");
console.log(buf); // <Buffer 48 65 6c 6c 6f>
console.log(buf.length); // 5
console.log(buf[0]); // 72
console.log(buf.toString()); // 'Hello'
```

### 58: What are the ways to create a Buffer?

```js
Buffer.from("text", "utf8"); // from a string
Buffer.from([1, 2, 3]); // from an array of bytes
Buffer.from(otherBuffer); // copy
Buffer.alloc(10); // 10 bytes, filled with zeros
Buffer.allocUnsafe(10); // 10 bytes, not cleared (faster but may contain old data)
Buffer.concat([buf1, buf2]); // join buffers
```

`new Buffer()` is deprecated and should not be used.

### 59: How do you convert a Buffer to different encodings?

```js
const buf = Buffer.from("Hello world");

buf.toString("utf8"); // 'Hello world'
buf.toString("hex"); // '48656c6c6f20776f726c64'
buf.toString("base64"); // 'SGVsbG8gd29ybGQ='
buf.toString("base64url");

Buffer.from("SGVsbG8gd29ybGQ=", "base64").toString(); // 'Hello world'
```

Supported encodings include `utf8`, `utf16le`, `latin1`, `base64`, `base64url`, `hex` and `ascii`.

### 60: What are streams?

Streams let you work with data piece by piece instead of loading all of it into memory at once. For example, you can send a 2 GB video to a client while reading it from disk in small chunks. HTTP requests and responses, files, sockets, `process.stdin` and `process.stdout` are all streams.

```js
import { createReadStream } from "node:fs";

createReadStream("big.log", "utf8")
  .on("data", (chunk) => console.log("got", chunk.length, "chars"))
  .on("end", () => console.log("done"));
```

### 61: What are the types of streams?

- **Readable**: you read data from it (`fs.createReadStream`, HTTP request on the server).
- **Writable**: you write data to it (`fs.createWriteStream`, HTTP response).
- **Duplex**: both readable and writable, independently (a TCP socket).
- **Transform**: a duplex stream that changes data as it passes through (`zlib.createGzip()`).

### 62: What does pipe() do?

`pipe()` connects a readable stream to a writable stream so data flows from one to the other, and it handles backpressure for you.

```js
import { createReadStream, createWriteStream } from "node:fs";
import { createGzip } from "node:zlib";

createReadStream("input.txt")
  .pipe(createGzip())
  .pipe(createWriteStream("input.txt.gz"));
```

`pipe()` does not forward errors or clean up streams on failure. In real code use `pipeline()` from `node:stream/promises` instead (see question 160).

### 63: What is EventEmitter?

`EventEmitter` is a class from the `events` module that lets objects emit named events and lets other code listen to them. Many core objects (streams, HTTP servers, `process`) extend it.

```js
import { EventEmitter } from "node:events";

class Order extends EventEmitter {}
const order = new Order();

order.on("paid", (amount) => console.log(`Paid ${amount}`));
order.emit("paid", 50); // Paid 50
```

Listeners are called synchronously, in the order they were added.

### 64: What is the difference between on() and once(), and how do you remove a listener?

`on()` (same as `addListener()`) runs the listener every time the event fires. `once()` runs it only the first time and then removes it.

```js
const handler = () => console.log("connected");

emitter.on("connect", handler);
emitter.once("ready", () => console.log("ready, only once"));

emitter.off("connect", handler); // same as removeListener
emitter.removeAllListeners("connect");
```

To remove a listener you need a reference to the same function, so avoid anonymous functions when you plan to remove them.

### 65: Why is the 'error' event special?

If an `EventEmitter` emits `'error'` and there is no listener for it, Node throws the error, which usually crashes the process. Always add an `'error'` listener to streams, sockets and other emitters.

```js
const stream = fs.createReadStream("missing.txt");
stream.on("error", (err) => {
  console.error("Read failed:", err.code); // ENOENT
});
```

### 66: How do you create a simple HTTP server without a framework?

```js
import http from "node:http";

const server = http.createServer((req, res) => {
  if (req.url === "/" && req.method === "GET") {
    res.writeHead(200, { "Content-Type": "text/plain" });
    res.end("Hello world");
    return;
  }
  res.writeHead(404);
  res.end("Not found");
});

server.listen(3000, () => {
  console.log("Listening on http://localhost:3000");
});
```

### 67: What are the req and res objects in an HTTP server?

`req` is an `http.IncomingMessage`. It is a readable stream and has `method`, `url`, `headers` and other request info. `res` is an `http.ServerResponse`. It is a writable stream with methods like `setHeader`, `writeHead`, `write` and `end`.

```js
http.createServer(async (req, res) => {
  console.log(req.method, req.url, req.headers["user-agent"]);

  let body = "";
  for await (const chunk of req) body += chunk;

  res.setHeader("Content-Type", "application/json");
  res.end(JSON.stringify({ received: body.length }));
});
```

### 68: How do you set status codes and headers in a response?

```js
res.statusCode = 201;
res.setHeader("Content-Type", "application/json");
res.setHeader("Cache-Control", "no-store");
res.end(JSON.stringify({ id: 1 }));

// or all at once
res.writeHead(301, { Location: "/new-url" });
res.end();
```

Headers must be set before the body is sent. Once you call `write()` or `end()`, headers are sent and changing them throws an error.

### 69: How do you read query string parameters in a plain Node.js server?

Use the global `URL` class and its `searchParams`.

```js
http
  .createServer((req, res) => {
    const url = new URL(req.url, `http://${req.headers.host}`);
    const page = Number(url.searchParams.get("page") ?? 1);
    const tags = url.searchParams.getAll("tag");
    res.end(`page=${page}, tags=${tags.join(",")}`);
  })
  .listen(3000);

// GET /items?page=2&tag=a&tag=b
```

### 70: Does Node.js have fetch built in?

Yes. `fetch` is available globally and stable since Node 21 (it was there behind no flag since Node 18). It is based on the `undici` HTTP client and follows the web standard, so it returns `Response` objects just like in browsers.

```js
const res = await fetch("https://api.github.com/repos/nodejs/node");
if (!res.ok) throw new Error(`HTTP ${res.status}`);
const repo = await res.json();
console.log(repo.stargazers_count);

await fetch("https://example.com/api/items", {
  method: "POST",
  headers: { "Content-Type": "application/json" },
  body: JSON.stringify({ name: "book" }),
});
```

Note that `fetch` does not reject on 404 or 500. You have to check `res.ok`.

### 71: How do you read and write JSON in Node.js?

```js
import { readFile, writeFile } from "node:fs/promises";

const data = JSON.parse(await readFile("data.json", "utf8"));
data.count++;
await writeFile("data.json", JSON.stringify(data, null, 2));
```

In ES modules you can also import JSON with an import attribute:

```js
import config from "./config.json" with { type: "json" };
```

In CommonJS, `require('./config.json')` works, but the result is cached, so it won't see changes made to the file later.

### 72: What is Express.js?

Express is a small and popular web framework for Node.js. It adds routing, middleware, and helpers on top of the `http` module. Express 5 is the current major version and it handles rejected promises in route handlers for you.

```js
import express from "express";

const app = express();
app.use(express.json());

app.get("/users/:id", async (req, res) => {
  const user = await db.findUser(req.params.id);
  if (!user) return res.status(404).json({ error: "Not found" });
  res.json(user);
});

app.listen(3000);
```

### 73: What is middleware?

Middleware is a function that runs during the request/response cycle. It gets `req`, `res` and `next`. It can read or change the request, send a response, or call `next()` to pass control to the next middleware. Logging, authentication, body parsing and error handling are usually done with middleware.

```js
function logger(req, res, next) {
  const start = Date.now();
  res.on("finish", () => {
    console.log(req.method, req.url, res.statusCode, Date.now() - start, "ms");
  });
  next();
}

app.use(logger);
```

### 74: How does routing work in Express?

You map an HTTP method and a path to a handler. You can group routes with `express.Router()`.

```js
const router = express.Router();

router.get("/", listProducts);
router.get("/:id", getProduct);
router.post("/", createProduct);
router.put("/:id", updateProduct);
router.delete("/:id", deleteProduct);

app.use("/products", router);
```

Route parameters are in `req.params`, query string values in `req.query`, and the parsed body in `req.body`.

### 75: How do you serve static files with Express?

Use the built-in `express.static` middleware.

```js
app.use(express.static("public"));
// public/logo.png is now available at /logo.png

app.use("/assets", express.static(path.join(import.meta.dirname, "public")));
```

For production traffic, a CDN or a reverse proxy like nginx is usually better at serving static files.

### 76: What is a REST API?

REST is a style for building web APIs. Data is organized as resources with URLs (`/users/42`), and HTTP methods say what to do with them. Requests are stateless, so each request carries everything the server needs, like an auth token. Responses usually use JSON and proper status codes.

```
GET    /users        list users
GET    /users/42     get one user
POST   /users        create a user
PUT    /users/42     replace a user
PATCH  /users/42     update part of a user
DELETE /users/42     delete a user
```

### 77: What are the common HTTP methods and status codes?

Methods: `GET` (read), `POST` (create), `PUT` (replace), `PATCH` (partial update), `DELETE` (remove), `HEAD` (headers only), `OPTIONS` (what is allowed, used for CORS preflight).

Status codes:

- `200` OK, `201` Created, `204` No Content
- `301` / `302` redirects, `304` Not Modified
- `400` Bad Request, `401` Unauthorized (not logged in), `403` Forbidden (logged in but not allowed), `404` Not Found, `409` Conflict, `422` Unprocessable Content, `429` Too Many Requests
- `500` Internal Server Error, `502` Bad Gateway, `503` Service Unavailable, `504` Gateway Timeout

### 78: How do you restart a Node.js app automatically when files change?

Before, people used `nodemon`. Now Node has a built-in watch mode (stable since Node 22).

```bash
node --watch app.js
node --watch-path=./src --watch-path=./config app.js
node --watch --env-file=.env app.js
```

```json
{
  "scripts": {
    "dev": "node --watch src/server.js"
  }
}
```

### 79: What is the util module and what does util.promisify do?

`util` contains helper functions. `util.promisify` turns a function that uses an error-first callback into one that returns a promise.

```js
import { promisify } from "node:util";
import { exec } from "node:child_process";

const execAsync = promisify(exec);
const { stdout } = await execAsync("git --version");
console.log(stdout);
```

Most core modules already have promise versions (`fs/promises`, `dns/promises`, `timers/promises`, `stream/promises`), so you mostly need `promisify` for older libraries.

### 80: What do util.format and util.inspect do?

`util.format` builds a string with placeholders, like `printf`. `util.inspect` turns any value into a readable string, which is what `console.log` uses internally.

```js
import util from "node:util";

util.format("%s is %d years old", "Anna", 30); // 'Anna is 30 years old'

const deep = { a: { b: { c: { d: 1 } } } };
console.log(util.inspect(deep, { depth: null, colors: true }));
```

### 81: How do you parse command line arguments without a library?

Use `util.parseArgs`, which is built in and stable.

```js
import { parseArgs } from "node:util";

const { values, positionals } = parseArgs({
  options: {
    port: { type: "string", short: "p", default: "3000" },
    verbose: { type: "boolean", short: "v" },
  },
  allowPositionals: true,
});

console.log(values.port, values.verbose, positionals);
// node cli.js build -p 8080 -v  ->  '8080' true ['build']
```

### 82: How do you print colored text in the terminal without a library?

Use `util.styleText`. It respects `NO_COLOR` and checks whether the output stream supports colors.

```js
import { styleText } from "node:util";

console.log(styleText("green", "Success"));
console.log(styleText(["red", "bold"], "Error!"));
```

### 83: What is the crypto module used for?

It provides hashing, HMAC, encryption, decryption, signing, random values and key generation. It is built on OpenSSL. A very common use is generating random IDs.

```js
import { randomUUID, randomBytes, randomInt } from "node:crypto";

randomUUID(); // '1b9d6bcd-bbfd-4b2d-9b5d-ab8dfbbd4bed'
randomBytes(16).toString("hex"); // random token
randomInt(1, 7); // dice roll, 1 to 6
```

`crypto.randomUUID()` is also available globally as `crypto.randomUUID()` through the Web Crypto object.

### 84: How do you create a hash of a string?

```js
import { createHash, hash } from "node:crypto";

createHash("sha256").update("hello").digest("hex");

// shorter one-shot helper (Node 21.7+ / 20.12+)
hash("sha256", "hello"); // hex by default
hash("sha256", "hello", "base64");
```

Don't use plain SHA hashes for passwords. Use `scrypt`, `argon2` or `bcrypt` instead (see question 134).

### 85: What useful console methods are there besides console.log?

```js
console.error("goes to stderr");
console.warn("also stderr");
console.table([
  { id: 1, name: "A" },
  { id: 2, name: "B" },
]);
console.time("query");
// ... work
console.timeEnd("query"); // query: 12.3ms
console.count("hit"); // hit: 1
console.group("Group");
console.log("indented");
console.groupEnd();
console.dir(obj, { depth: null });
console.trace("where am I");
console.assert(x > 0, "x must be positive");
```

### 86: How do you debug a Node.js application?

Start Node with `--inspect` (or `--inspect-brk` to pause on the first line), then open `chrome://inspect` in Chrome or attach the VS Code debugger. You can set breakpoints, step through code and look at variables. You can also put a `debugger;` statement in code.

```bash
node --inspect app.js
node --inspect-brk app.js
node --inspect=0.0.0.0:9229 app.js   # only in safe, private networks
```

In VS Code you can also just open a "JavaScript Debug Terminal" and run your app as usual.

### 87: What is the built-in test runner?

Node has a test runner in `node:test` (stable since Node 20). You don't need Jest or Mocha for most projects.

```js
// math.test.js
import { test, describe } from "node:test";
import assert from "node:assert/strict";
import { add } from "./math.js";

describe("add", () => {
  test("adds two numbers", () => {
    assert.equal(add(2, 3), 5);
  });

  test("works with async code", async () => {
    const result = await Promise.resolve(add(1, 1));
    assert.equal(result, 2);
  });
});
```

```bash
node --test                 # finds *.test.js, test-*.js, files in test/ and more
node --test --watch
```

### 88: What is the assert module?

`node:assert` gives functions that throw an `AssertionError` when a check fails. It is used in tests and sometimes to check assumptions in code. Use the strict version.

```js
import assert from "node:assert/strict";

assert.equal(1 + 1, 2);
assert.deepEqual({ a: [1, 2] }, { a: [1, 2] });
assert.ok(user.isActive);
assert.throws(() => JSON.parse("{bad"), SyntaxError);
await assert.rejects(fetchMissing(), { code: "ENOENT" });
```

### 89: Do ES modules run in strict mode?

Yes. ES modules are always in strict mode, you don't need `'use strict'`. CommonJS files are not strict unless you add `'use strict'` at the top. Strict mode turns some silent mistakes into errors, like assigning to undeclared variables.

### 90: What are the main differences between JavaScript in Node.js and in the browser?

- Node has no `window` or `document` (no DOM). It has `process`, `Buffer`, `fs` and other server APIs.
- Node can read files, open sockets and start processes. Browsers are sandboxed.
- Node supports both CommonJS and ES modules.
- You control the Node version, so you know which JavaScript features you can use.
- Both now share many web APIs: `fetch`, `URL`, `AbortController`, `TextEncoder`, `structuredClone`, Web Streams, `WebSocket` client and Web Crypto.

### 91: What is Node.js good for and what is it not good for?

Good for:

- APIs and web servers with lots of I/O
- Real-time apps (chat, live updates, WebSockets)
- Command line tools and build tools
- Backend for frontend, proxies, streaming

Not ideal for:

- Heavy CPU work on the main thread (video encoding, big calculations). You can still do it with worker threads or by calling native code, but other languages may fit better.

### 92: What is an LTS release of Node.js?

LTS means Long Term Support. Even-numbered major versions (20, 22, 24, ...) become LTS and get bug fixes and security fixes for about 30 months. Odd-numbered versions are "Current" releases that live for a short time and never become LTS. For production, use an Active LTS or Maintenance LTS version. Check the official release schedule at nodejs.org for end-of-life dates.

### 93: How do you install and switch between Node.js versions?

Use a version manager.

```bash
# nvm
nvm install 24
nvm use 24
nvm alias default 24

# fnm (fast, works on Windows too)
fnm install --lts
fnm use 24
```

Other options are Volta and the official installers or Docker images.

### 94: How do you tell other developers and tools which Node version a project needs?

Add an `.nvmrc` (or `.node-version`) file and the `engines` field in `package.json`.

```
# .nvmrc
24
```

```json
{
  "engines": {
    "node": ">=22"
  }
}
```

`engines` only shows a warning by default. Setting `engine-strict=true` in `.npmrc` makes npm fail on the wrong version.

### 95: What is Corepack?

Corepack is a tool that manages package manager versions (yarn, pnpm) based on the `packageManager` field in `package.json`. It was bundled with Node from 16.9 up to 24. Starting with Node 25 it is no longer shipped with Node, so you install it separately with `npm install -g corepack` if you want it.

```json
{
  "packageManager": "pnpm@10.0.0"
}
```

### 96: What are yarn and pnpm?

They are alternatives to npm. Both use the same registry.

- **pnpm** stores every package version once on disk and links it into projects, which saves space and is fast. It is also strict, so you can only import packages you declared.
- **yarn** was created to fix npm's old speed and lock file problems. Yarn Berry (v2+) adds Plug'n'Play, which removes `node_modules`.

npm has caught up a lot, so the choice is mostly team preference.

### 97: What is the node_modules folder?

It is where npm puts installed packages. npm flattens it as much as it can, so dependencies of dependencies often sit at the top level. Don't commit it to git and don't edit files in it by hand. You can always recreate it with `npm install` or `npm ci`.

### 98: How does Node find a package when you import it by name?

For `import x from 'lodash'` or `require('lodash')`, Node looks for a `node_modules/lodash` folder in the current directory, then in the parent, then the grandparent, all the way up to the root. When it finds the package, it reads its `package.json` to see which file to load (`exports` field, or `main`, or `index.js`).

### 99: What are the "main" and "exports" fields in package.json?

`main` is the old way to say which file is the entry point of a package. `exports` is the modern way. It lets you define several entry points, different files for `import` and `require`, and it hides all files you don't list.

```json
{
  "name": "my-lib",
  "main": "./dist/index.cjs",
  "exports": {
    ".": {
      "import": "./dist/index.js",
      "require": "./dist/index.cjs"
    },
    "./utils": "./dist/utils.js"
  }
}
```

If `exports` is present, users can't import `my-lib/dist/internal.js` because it is not listed.

### 100: Are modules cached in Node.js?

Yes. The first time a module is loaded, Node runs it and caches the result. Later imports get the same object. This means module-level code runs only once, and module-level state is shared, which is why a module that exports an object works like a singleton.

```js
// counter.js
let count = 0;
export const inc = () => ++count;

// a.js and b.js both import inc and share the same count
```

### 101: What is a circular dependency?

It is when module A imports module B and B imports A, directly or through other modules. Node does not crash, but one of the modules will see the other one only partly loaded, which can lead to `undefined` values or "cannot access before initialization" errors. The fix is usually to move the shared code into a third module.

### 102: What is the cluster module?

`cluster` lets you start several Node processes (workers) that share the same server port. The primary process forks workers, usually one per CPU core, and spreads incoming connections between them. This makes use of all cores for an HTTP server.

```js
import cluster from "node:cluster";
import http from "node:http";
import os from "node:os";

if (cluster.isPrimary) {
  for (let i = 0; i < os.availableParallelism(); i++) cluster.fork();
} else {
  http.createServer((req, res) => res.end(`pid ${process.pid}`)).listen(3000);
}
```

In containers people often run one process per container and let Kubernetes or another orchestrator scale it instead.

### 103: What is the child_process module?

It lets you run other programs (shell commands, scripts, binaries) from Node. The main functions are `spawn`, `exec`, `execFile` and `fork`.

```js
import { execFile } from "node:child_process";
import { promisify } from "node:util";

const run = promisify(execFile);
const { stdout } = await run("git", ["rev-parse", "HEAD"]);
console.log(stdout.trim());
```

### 104: What are worker threads?

Worker threads (`node:worker_threads`) let you run JavaScript in parallel threads inside the same process. Each worker has its own V8 instance and event loop. They are good for CPU-heavy tasks like image processing or parsing large data, so the main thread stays free.

```js
import { Worker } from "node:worker_threads";

const worker = new Worker(new URL("./heavy.js", import.meta.url), {
  workerData: { n: 40 },
});
worker.on("message", (result) => console.log("result", result));
worker.on("error", console.error);
```

```js
// heavy.js
import { parentPort, workerData } from "node:worker_threads";
const fib = (n) => (n < 2 ? n : fib(n - 1) + fib(n - 2));
parentPort.postMessage(fib(workerData.n));
```

### 105: How do you write an error handling middleware in Express?

An error handler has four arguments: `(err, req, res, next)`. Put it after all routes.

```js
app.get("/boom", () => {
  throw new Error("Something broke");
});

app.use((err, req, res, next) => {
  console.error(err);
  res.status(err.status ?? 500).json({ error: "Internal Server Error" });
});
```

In Express 5, if an `async` handler throws or returns a rejected promise, the error goes to this handler automatically. In Express 4 you had to call `next(err)` yourself.

### 106: What is CORS?

CORS (Cross-Origin Resource Sharing) is a browser rule that blocks a web page from reading responses from a different origin unless the server allows it with headers like `Access-Control-Allow-Origin`. It only affects browsers. Server-to-server requests are not limited by it.

```js
import cors from "cors";

app.use(cors({ origin: ["https://myapp.com"], credentials: true }));
```

### 107: How do you read a JSON request body in Express?

Use the built-in `express.json()` middleware. Without it, `req.body` is `undefined`.

```js
app.use(express.json({ limit: "100kb" }));
app.use(express.urlencoded({ extended: false })); // HTML forms

app.post("/users", (req, res) => {
  const { name, email } = req.body;
  res.status(201).json({ name, email });
});
```

### 108: What is the difference between res.send, res.json and res.end in Express?

- `res.end()` comes from Node's `http` module. It ends the response with optional data and sets nothing extra.
- `res.send()` is from Express. It sets `Content-Type` based on the data (HTML for strings, JSON for objects, binary for buffers) and the `Content-Length`.
- `res.json()` always converts the value to JSON and sets `Content-Type: application/json`.

### 109: What is NODE_ENV?

`NODE_ENV` is an environment variable that by convention tells libraries which mode you are in, usually `development`, `production` or `test`. Express, for example, caches views and shows less error detail in production. Node itself doesn't read it. Don't use it to switch between different configs for different deployments (staging, prod). Use separate config variables for that.

```bash
NODE_ENV=production node server.js
```

### 110: What is the Error object and what is error.cause?

`Error` is the base class for errors. It has `message`, `name` and `stack`. The `cause` option lets you wrap a low-level error in a more meaningful one without losing the original.

```js
try {
  await db.query(sql);
} catch (err) {
  throw new Error("Failed to load user", { cause: err });
}
```

When printed, Node shows both errors and their stack traces.

### 111: What kinds of errors do you meet in Node.js?

- **Standard JavaScript errors**: `SyntaxError`, `TypeError`, `RangeError`, `ReferenceError`.
- **System errors**: from the OS, with a `code` like `ENOENT` (no such file), `EACCES` (permission denied), `EADDRINUSE` (port in use), `ECONNREFUSED`, `ETIMEDOUT`.
- **Node.js errors**: with codes like `ERR_INVALID_ARG_TYPE` or `ERR_MODULE_NOT_FOUND`.
- **Assertion errors** from `node:assert`.
- **Your own errors**, usually custom classes that extend `Error`.

Always check `err.code` instead of the message, because messages can change.

### 112: What is the uncaughtException event?

It fires when an error is thrown and nothing catches it. By default Node prints the stack and exits with code 1. You can listen to it to log the error, but you should still exit, because the app may be in a broken state.

```js
process.on("uncaughtException", (err) => {
  console.error("Uncaught:", err);
  process.exit(1);
});
```

### 113: What happens when a promise rejection is not handled?

Since Node 15, an unhandled rejection is treated like an uncaught exception: Node prints the error and exits with code 1. You can listen to `unhandledRejection` for logging, but the right fix is to always handle rejections with `await` inside `try/catch` or with `.catch()`.

```js
process.on("unhandledRejection", (reason) => {
  console.error("Unhandled rejection:", reason);
  process.exit(1);
});
```

### 114: How do you use the URL class?

`URL` is the WHATWG standard URL parser, available globally.

```js
const url = new URL("https://user:pass@example.com:8080/path/page?x=1&y=2#top");

url.protocol; // 'https:'
url.hostname; // 'example.com'
url.port; // '8080'
url.pathname; // '/path/page'
url.searchParams.get("x"); // '1'
url.hash; // '#top'

url.searchParams.append("z", "3");
url.toString();

URL.canParse("not a url"); // false
```

The old `url.parse()` function is deprecated and has security problems, so use `new URL()`.

### 115: What is the difference between the querystring module and URLSearchParams?

`querystring` is an older Node-only module for parsing query strings. It is marked as legacy. `URLSearchParams` is the web standard and works the same in browsers and Node. Use `URLSearchParams` in new code.

```js
const params = new URLSearchParams("a=1&b=2&b=3");
params.get("a"); // '1'
params.getAll("b"); // ['2', '3']
Object.fromEntries(params); // { a: '1', b: '3' }

new URLSearchParams({ q: "node js", page: "2" }).toString(); // 'q=node+js&page=2'
```

### 116: What is the readline module?

`readline` reads input from a readable stream one line at a time. It is used for interactive command line programs and for reading files line by line. There is a promise version in `node:readline/promises`.

```js
import { createInterface } from "node:readline";
import { createReadStream } from "node:fs";

const rl = createInterface({ input: createReadStream("access.log") });
for await (const line of rl) {
  if (line.includes("ERROR")) console.log(line);
}
```

### 117: How do you ask the user for input in a terminal app?

```js
import * as readline from "node:readline/promises";
import { stdin as input, stdout as output } from "node:process";

const rl = readline.createInterface({ input, output });
const name = await rl.question("What is your name? ");
console.log(`Hello, ${name}`);
rl.close();
```

### 118: What is the zlib module?

`zlib` compresses and decompresses data with gzip, deflate and Brotli (and Zstandard in recent versions, still experimental). It has sync, callback, promise-like (with `promisify`) and stream APIs.

```js
import { gzipSync, gunzipSync } from "node:zlib";

const compressed = gzipSync("hello ".repeat(1000));
console.log(compressed.length);
console.log(gunzipSync(compressed).toString().length);
```

Use the stream versions (`createGzip()`) for large data.

### 119: What is the dns module?

It resolves domain names to IP addresses and does other DNS lookups.

```js
import dns from "node:dns/promises";

await dns.lookup("nodejs.org"); // uses the OS resolver, like most apps
await dns.resolve4("nodejs.org"); // asks DNS servers directly
await dns.resolveMx("gmail.com");
```

### 120: What is the net module?

`net` is for TCP servers and clients (and Unix sockets / Windows named pipes). The `http` module is built on top of it.

```js
import net from "node:net";

const server = net.createServer((socket) => {
  socket.write("Welcome\n");
  socket.on("data", (data) => socket.write(`You said: ${data}`));
});
server.listen(4000);
```

### 121: What is the dgram module?

`dgram` is for UDP sockets. UDP sends separate messages (datagrams) with no connection and no guarantee of delivery or order. It is used for things like DNS, game state updates, metrics (StatsD) and discovery.

```js
import dgram from "node:dgram";

const server = dgram.createSocket("udp4");
server.on("message", (msg, rinfo) => {
  console.log(`${msg} from ${rinfo.address}:${rinfo.port}`);
});
server.bind(41234);
```

### 122: What is the difference between the http and https modules?

`https` is the same as `http` but uses TLS to encrypt traffic. To run an HTTPS server you need a private key and a certificate. In many deployments, TLS is handled by a load balancer or reverse proxy, and the Node app itself only speaks plain HTTP.

```js
import https from "node:https";
import { readFileSync } from "node:fs";

https
  .createServer(
    { key: readFileSync("key.pem"), cert: readFileSync("cert.pem") },
    (req, res) => res.end("secure"),
  )
  .listen(443);
```

### 123: Can Node.js run TypeScript directly?

Yes. Since Node 22.18 and 23.6, Node can run `.ts` files without any flag by stripping the type annotations ("type stripping"). It does not check types, so you still run `tsc --noEmit` for that. It only supports syntax that can simply be erased, so features like `enum` and `namespace` need the `--experimental-transform-types` flag or should be avoided.

```ts
// app.ts
interface User {
  name: string;
}
const u: User = { name: "Ana" };
console.log(u.name);
```

```bash
node app.ts
```

### 124: What is top-level await?

In ES modules you can use `await` outside of an `async` function, at the top level of the file. It does not work in CommonJS.

```js
// config.mjs
const res = await fetch("https://example.com/config.json");
export const config = await res.json();
```

Any module that imports this one waits until it finishes loading.

### 125: How do you make a Node.js script into a command line tool?

Add a shebang line at the top of the file and a `bin` field in `package.json`.

```js
#!/usr/bin/env node
// bin/hello.js
console.log(`Hello, ${process.argv[2] ?? "world"}`);
```

```json
{
  "name": "hello-cli",
  "bin": { "hello": "./bin/hello.js" }
}
```

After `npm install -g` (or `npm link` while developing) you can run `hello Ana`.

### 126: What is structuredClone?

`structuredClone` is a global function that makes a deep copy of a value. It handles nested objects, arrays, `Date`, `Map`, `Set`, typed arrays and circular references. It cannot copy functions, DOM nodes or class instances' prototypes (you get a plain object back).

```js
const original = { date: new Date(), list: [1, 2], map: new Map([["a", 1]]) };
const copy = structuredClone(original);
copy.list.push(3);
console.log(original.list); // [1, 2]
```

This is better than `JSON.parse(JSON.stringify(x))`, which loses dates, maps, `undefined` and more.

### 127: What is AbortController?

`AbortController` is a standard way to cancel async operations. You pass its `signal` to an API and call `abort()` when you want to stop. Many Node APIs accept a signal: `fetch`, `fs.readFile`, `setTimeout` from `timers/promises`, `child_process`, `events.once`, streams.

```js
const controller = new AbortController();
setTimeout(() => controller.abort(), 2000);

try {
  const res = await fetch("https://example.com/slow", {
    signal: controller.signal,
  });
} catch (err) {
  if (err.name === "AbortError") console.log("Request cancelled");
}

// shorter for timeouts:
await fetch(url, { signal: AbortSignal.timeout(2000) });
```

### 128: When should you use fs.createReadStream instead of fs.readFile?

`readFile` loads the whole file into memory. That is fine for small files like configs. For big files (logs, videos, CSV exports), use `createReadStream` so you only keep a small chunk (64 KB by default) in memory at a time, and so you can start sending data before the whole file is read.

```js
import { createReadStream } from "node:fs";

http
  .createServer((req, res) => {
    res.setHeader("Content-Type", "video/mp4");
    createReadStream("movie.mp4").pipe(res);
  })
  .listen(3000);
```

### 129: What is a template engine?

A template engine fills HTML templates with data on the server. Examples are EJS, Pug, Handlebars and Nunjucks. In Express you set it with `app.set('view engine', ...)` and call `res.render()`.

```js
app.set("view engine", "ejs");
app.get("/", (req, res) => {
  res.render("index", { title: "Home", user: req.user });
});
```

Many modern apps use a frontend framework or a meta-framework (Next.js, Nuxt, Remix, Astro) instead.

### 130: Does Node.js have a built-in database?

Node has a built-in SQLite module, `node:sqlite`. It was added in Node 22.5 and no longer needs a flag since 22.13 and 23.4. It is still marked as under active development, so check the docs for your version. For other databases you install a driver from npm, like `pg` for PostgreSQL or `mysql2`.

```js
import { DatabaseSync } from "node:sqlite";

const db = new DatabaseSync("app.db");
db.exec("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT)");

const insert = db.prepare("INSERT INTO users (name) VALUES (?)");
insert.run("Ana");

const users = db.prepare("SELECT * FROM users").all();
console.log(users);
```

### 131: What is an ORM?

An ORM (Object Relational Mapper) lets you work with database rows as JavaScript objects and write queries with code instead of raw SQL. Popular ones in Node: Prisma, Drizzle, TypeORM, Sequelize, MikroORM. Query builders like Knex sit between raw SQL and a full ORM. ORMs save time on simple queries but can make complex queries harder and slower, so many teams mix ORM code with raw SQL.

### 132: What is a JWT?

A JSON Web Token is a signed string with three parts: header, payload and signature, separated by dots. The server signs it on login and the client sends it back with each request, usually in the `Authorization: Bearer <token>` header. The server checks the signature to trust the payload without looking anything up in a database.

```js
import jwt from "jsonwebtoken";

const token = jwt.sign(
  { sub: user.id, role: "admin" },
  process.env.JWT_SECRET,
  {
    expiresIn: "15m",
  },
);

const payload = jwt.verify(token, process.env.JWT_SECRET);
```

The payload is only encoded (base64url), not encrypted, so never put secrets in it.

### 133: What is the difference between cookies and sessions?

A cookie is a small piece of data the server asks the browser to store and send back with every request. A session is data stored on the server (in memory, Redis, a database) for a user. Usually the cookie only holds a random session ID, and the server uses it to find the session data. Set cookies with `HttpOnly`, `Secure` and `SameSite` to protect them.

```js
res.cookie("sid", sessionId, {
  httpOnly: true,
  secure: true,
  sameSite: "lax",
  maxAge: 1000 * 60 * 60,
});
```

### 134: How should you store user passwords?

Never store them as plain text or with a fast hash like SHA-256. Use a slow, salted password hashing function: Argon2, bcrypt or scrypt. Node has `scrypt` built in.

```js
import { scrypt, randomBytes, timingSafeEqual } from "node:crypto";
import { promisify } from "node:util";

const scryptAsync = promisify(scrypt);

export async function hashPassword(password) {
  const salt = randomBytes(16);
  const key = await scryptAsync(password, salt, 64);
  return `${salt.toString("hex")}:${key.toString("hex")}`;
}

export async function verifyPassword(password, stored) {
  const [saltHex, keyHex] = stored.split(":");
  const key = await scryptAsync(password, Buffer.from(saltHex, "hex"), 64);
  return timingSafeEqual(key, Buffer.from(keyHex, "hex"));
}
```

### 135: What are WebSockets and does Node support them?

A WebSocket is a long-lived, two-way connection between client and server over one TCP connection. It is used for chats, live dashboards and multiplayer games. Since Node 22, a browser-compatible `WebSocket` client is available globally. For a WebSocket server you still use a library like `ws` (or Socket.IO, which adds rooms, reconnects and fallbacks).

```js
// client, built in
const ws = new WebSocket("wss://echo.websocket.org");
ws.addEventListener("open", () => ws.send("hello"));
ws.addEventListener("message", (e) => console.log(e.data));
```

```js
// server, with the ws package
import { WebSocketServer } from "ws";
const wss = new WebSocketServer({ port: 8080 });
wss.on("connection", (socket) => {
  socket.on("message", (msg) => socket.send(`echo: ${msg}`));
});
```

### 136: What is the difference between HTTP and WebSocket?

With HTTP the client sends a request and the server sends one response. The server can't send data on its own unless the client asks. A WebSocket starts as an HTTP request and then "upgrades" to a permanent connection where both sides can send messages at any time. If you only need server-to-client updates, Server-Sent Events (SSE) over normal HTTP are often simpler.

### 137: What is the difference between a process and a thread?

A process is a running program with its own memory. Processes don't share memory and talk through IPC, pipes or the network. A thread runs inside a process and shares that process's memory. In Node, `child_process` and `cluster` create processes, and `worker_threads` creates threads. Worker threads are lighter, but each still has its own JavaScript heap. They share memory only through `SharedArrayBuffer`.

### 138: How does garbage collection work in Node.js at a basic level?

V8 frees memory that is no longer reachable from your code. Most objects die young, so V8 splits the heap into a small "young generation" that is cleaned often and quickly, and an "old generation" for objects that survive longer, which is cleaned less often. You don't free memory yourself, but you can cause leaks by keeping references you no longer need, like growing arrays, caches without limits, or listeners you never remove.

### 139: How do you check how much memory a Node process is using?

```js
const m = process.memoryUsage();
console.log({
  rss: m.rss, // total memory the process uses
  heapTotal: m.heapTotal, // V8 heap allocated
  heapUsed: m.heapUsed, // V8 heap actually used
  external: m.external, // memory used by C++ objects tied to JS objects
  arrayBuffers: m.arrayBuffers, // Buffers and ArrayBuffers
});

process.memoryUsage.rss(); // faster if you only need rss
```

### 140: What is the difference between process.cwd() and \_\_dirname?

`process.cwd()` is the folder you ran `node` from. It can be different every time. `__dirname` (or `import.meta.dirname` in ESM) is the folder that contains the current file and never changes. Use `__dirname` / `import.meta.dirname` to load files that live next to your code.

```bash
cd /home/me
node projects/app/index.js
# process.cwd()        -> /home/me
# import.meta.dirname  -> /home/me/projects/app
```

### 141: In what order do setTimeout, setImmediate and process.nextTick run?

When you call them from the main script:

```js
setTimeout(() => console.log("timeout"), 0);
setImmediate(() => console.log("immediate"));
process.nextTick(() => console.log("nextTick"));
Promise.resolve().then(() => console.log("promise"));
console.log("sync");
```

`sync` runs first, then `nextTick`, then `promise` (in an ES module the last two are swapped, see question 46). After that, `timeout` and `immediate` can come in either order, because it depends on how fast the event loop starts compared to the 1 ms timer. Inside an I/O callback, `setImmediate` always runs before `setTimeout`. More detail is in question 154.

### 142: What are pre and post scripts in npm?

If you define `prebuild` or `postbuild`, npm runs them automatically before and after `build`. This works for any script name.

```json
{
  "scripts": {
    "prebuild": "rm -rf dist",
    "build": "tsc",
    "postbuild": "node scripts/copy-assets.js"
  }
}
```

There are also lifecycle scripts like `prepare` (runs after `npm install` and before publish) and `postinstall`. Be careful with `postinstall` in dependencies, it is a common way for malicious packages to run code.

### 143: What is npm audit?

`npm audit` checks your installed packages against a database of known vulnerabilities and prints a report. `npm audit fix` tries to update to safe versions within allowed ranges. It doesn't find every problem, and not every finding is a real risk for your app, but you should run it in CI.

```bash
npm audit
npm audit --omit=dev
npm audit fix
```

### 144: What are npm workspaces?

Workspaces let you keep several packages in one repository (a monorepo) and install them all with one `npm install`. Local packages are linked to each other, so changes show up right away.

```json
{
  "name": "my-monorepo",
  "private": true,
  "workspaces": ["packages/*"]
}
```

```bash
npm install                      # installs everything
npm run test --workspace=api     # run a script in one package
npm run build --workspaces       # run in all packages
```

### 145: How do you control which files are published to npm?

Use the `files` field in `package.json` as an allow list. Anything not listed is left out, except `package.json`, `README` and `LICENSE`, which are always included. You can also use `.npmignore`, but an allow list is safer. Check the result with `npm pack --dry-run`.

```json
{
  "files": ["dist", "bin"]
}
```

### 146: What is a peer dependency?

A peer dependency is a package that your package needs but expects the app to install. Plugins use it. For example, a React component library lists `react` as a peer dependency so the app doesn't end up with two copies of React. Since npm 7, peer dependencies are installed automatically, and conflicts cause an error unless you use `--legacy-peer-deps`.

```json
{
  "peerDependencies": {
    "react": ">=18"
  }
}
```

### 147: How do you send different kinds of request bodies with fetch?

```js
// JSON
await fetch(url, {
  method: "POST",
  headers: { "Content-Type": "application/json" },
  body: JSON.stringify({ title: "hi" }),
});

// form fields and files
const form = new FormData();
form.append("name", "avatar");
form.append("file", new Blob([await readFile("a.png")]), "a.png");
await fetch(url, { method: "POST", body: form });

// URL-encoded
await fetch(url, { method: "POST", body: new URLSearchParams({ a: "1" }) });
```

`fetch` sets the right `Content-Type` for `FormData` and `URLSearchParams` by itself.

### 148: What are Blob and File in Node.js?

`Blob` and `File` are the same web APIs you know from browsers, available globally in Node. A `Blob` is immutable binary data with a type. `File` adds a name and a last-modified date. They are useful with `fetch` and `FormData`. You can also get a `Blob` backed by a file on disk with `fs.openAsBlob()`.

```js
import { openAsBlob } from "node:fs";

const blob = await openAsBlob("report.pdf", { type: "application/pdf" });
const form = new FormData();
form.append("file", blob, "report.pdf");
```

### 149: What is node --run?

`node --run <script>` runs a script from `package.json` without starting npm, so it starts faster. It was added in Node 22. It doesn't run `pre` and `post` scripts and doesn't support everything npm does, but it's good for simple scripts.

```bash
node --run build
node --run test -- --watch
```

### 150: What are the popular Node.js web frameworks?

- **Express**: small, flexible and the most used. Huge ecosystem of middleware.
- **Fastify**: focused on speed, has built-in JSON schema validation and a plugin system.
- **NestJS**: opinionated framework with modules, decorators and dependency injection, similar to Angular. Runs on Express or Fastify.
- **Koa**: from the Express team, smaller, built around async middleware.
- **Hono**: very small, built on web standards, runs on Node, Bun, Deno and edge platforms.
- **AdonisJS**: full-stack, batteries included, similar to Laravel.

## Moderate Questions

### 151: What are the phases of the event loop?

Each round (tick) of the event loop goes through these phases in order:

1. **timers**: runs callbacks from `setTimeout` and `setInterval` whose time has come.
2. **pending callbacks**: runs some I/O callbacks that were deferred from the previous round, like certain TCP errors.
3. **idle, prepare**: used internally.
4. **poll**: gets new I/O events and runs their callbacks. If nothing else is scheduled, Node waits here for I/O.
5. **check**: runs `setImmediate` callbacks.
6. **close callbacks**: runs `'close'` handlers, like `socket.on('close')`.

Between each callback, Node empties the `process.nextTick` queue and then the promise microtask queue.

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
│  │           poll            │<── incoming connections, data
│  └─────────────┬─────────────┘
│  ┌─────────────┴─────────────┐
│  │           check           │
│  └─────────────┬─────────────┘
│  ┌─────────────┴─────────────┐
└──┤      close callbacks      │
   └───────────────────────────┘
```

### 152: What is the difference between microtasks and macrotasks?

Macrotasks are the callbacks in the event loop phases: timers, I/O callbacks, `setImmediate`, close events. Microtasks are promise callbacks (`.then`, code after `await`) and `queueMicrotask`. Node also has the `process.nextTick` queue, which runs even before microtasks.

After every single macrotask, Node runs all `nextTick` callbacks, then all microtasks, and only then moves to the next macrotask.

```js
setTimeout(() => {
  console.log("timeout 1");
  Promise.resolve().then(() => console.log("micro inside timeout 1"));
}, 0);
setTimeout(() => console.log("timeout 2"), 0);

// timeout 1
// micro inside timeout 1
// timeout 2
```

### 153: What does this code print, and why?

```js
// order.cjs (CommonJS)
console.log("1");

setTimeout(() => console.log("2"), 0);

Promise.resolve().then(() => {
  console.log("3");
  process.nextTick(() => console.log("4"));
});

process.nextTick(() => console.log("5"));

queueMicrotask(() => console.log("6"));

(async () => {
  console.log("7");
  await null;
  console.log("8");
})();

console.log("9");
```

Output: `1 7 9 5 3 6 8 4 2`

- `1`, `7`, `9` are synchronous. The async function runs synchronously until its first `await`.
- After the main script, the `nextTick` queue runs first: `5`.
- Then the microtask queue in order: `3`, `6`, `8`. While running `3` a new `nextTick` is added.
- After the microtask queue is empty, Node checks the `nextTick` queue again: `4`.
- Finally, the event loop reaches the timers phase: `2`.

If you save the same code as `order.mjs`, the output is `1 7 9 3 6 8 5 4 2`. An ES module's top-level code runs inside a promise job, so the microtask queue (`3 6 8`) is drained before Node looks at the `nextTick` queue (`5`, then `4`). Interviewers like this detail, so it's worth knowing.

### 154: Why is the order of setTimeout(fn, 0) and setImmediate not fixed in the main module?

`setTimeout(fn, 0)` is really `setTimeout(fn, 1)`. When the event loop starts, it checks if 1 ms has passed. If the process took longer than 1 ms to get there, the timer runs first. If not, the loop moves on to the check phase and `setImmediate` runs first. So it depends on machine speed.

Inside an I/O callback the order is always the same, because after the poll phase comes the check phase, and timers only come in the next round:

```js
import fs from "node:fs";

fs.readFile(import.meta.filename, () => {
  setTimeout(() => console.log("timeout"), 0);
  setImmediate(() => console.log("immediate"));
});
// immediate
// timeout   (always)
```

### 155: What is the difference between process.nextTick and queueMicrotask?

Both run before the event loop continues, but `nextTick` callbacks have their own queue that is processed before the promise microtask queue. `queueMicrotask` uses the same queue as promises and is a web standard, so it also works in browsers. The Node docs suggest `queueMicrotask` for most cases. `nextTick` is mainly useful when you need code to run before any promise callbacks, for example to emit an event right after a constructor returns.

### 156: How can process.nextTick starve the event loop?

If a `nextTick` callback schedules another `nextTick` over and over, Node keeps processing that queue and never gets back to I/O or timers. The same can happen with an endless chain of microtasks.

```js
function loop() {
  process.nextTick(loop); // the event loop never moves on
}
loop();

setTimeout(() => console.log("never runs"), 0);
```

If you need to split work into pieces, use `setImmediate`, which lets I/O run between pieces.

### 157: What is the libuv thread pool and which operations use it?

libuv keeps a pool of threads to run work that the OS can't do asynchronously. In Node these use it:

- Most `fs` operations (except `fs.watch`)
- `dns.lookup()` (but not `dns.resolve*()`)
- Async `crypto` functions like `pbkdf2`, `scrypt`, `randomBytes`, `generateKeyPair`
- Async `zlib` functions
- Some native addons

The pool has 4 threads by default. You can change it with the `UV_THREADPOOL_SIZE` environment variable (max 1024) before the pool is first used. If you start many slow file or crypto operations, they wait for a free thread, which can make even DNS lookups slow.

```bash
UV_THREADPOOL_SIZE=16 node server.js
```

Network I/O (TCP, HTTP) does not use the thread pool. It uses the OS's event mechanisms.

### 158: What are flowing and paused modes in readable streams?

A readable stream starts in paused mode. In paused mode you pull data with `read()`, usually inside a `'readable'` event. It switches to flowing mode when you add a `'data'` listener, call `resume()`, or `pipe()` it. In flowing mode data is pushed to you as fast as it arrives.

```js
// flowing
stream.on("data", (chunk) => handle(chunk));

// paused
stream.on("readable", () => {
  let chunk;
  while ((chunk = stream.read()) !== null) handle(chunk);
});
```

Today the simplest way is to use `for await...of`, which handles this for you.

### 159: What is backpressure in streams?

Backpressure happens when data comes in faster than it can be written out. If you ignore it, data piles up in memory. A writable stream signals this: `write()` returns `false` when its internal buffer is above `highWaterMark`. You should stop writing until it emits `'drain'`.

```js
import { once } from "node:events";

async function writeMany(stream, lines) {
  for (const line of lines) {
    if (!stream.write(line + "\n")) {
      await once(stream, "drain");
    }
  }
  stream.end();
}
```

`pipe()` and `pipeline()` do this automatically.

### 160: Why is stream.pipeline better than pipe?

`pipe()` doesn't pass errors along the chain and doesn't close the other streams when one fails, which can cause leaks and hanging file handles. `pipeline()` forwards errors, destroys all streams on failure, and tells you when everything is done. Use the promise version from `node:stream/promises`.

```js
import { pipeline } from "node:stream/promises";
import { createReadStream, createWriteStream } from "node:fs";
import { createGzip } from "node:zlib";

try {
  await pipeline(
    createReadStream("access.log"),
    createGzip(),
    createWriteStream("access.log.gz"),
  );
  console.log("done");
} catch (err) {
  console.error("pipeline failed", err);
}
```

### 161: How do you create a custom Readable stream?

Extend `Readable` and implement `_read()`, or pass a `read` function to the constructor. Call `this.push(data)` to add data and `this.push(null)` to end the stream.

```js
import { Readable } from "node:stream";

class Counter extends Readable {
  constructor(max) {
    super();
    this.n = 0;
    this.max = max;
  }
  _read() {
    this.n++;
    if (this.n > this.max) this.push(null);
    else this.push(`${this.n}\n`);
  }
}

new Counter(5).pipe(process.stdout);
```

### 162: How do you create a custom Writable stream?

Implement `write` (or `_write`). Call the callback when you're done with the chunk, or with an error if it failed.

```js
import { Writable } from "node:stream";

const saveToDb = new Writable({
  objectMode: true,
  async write(record, encoding, callback) {
    try {
      await db.insert(record);
      callback();
    } catch (err) {
      callback(err);
    }
  },
});
```

You can also implement `writev` to handle many chunks at once and `final` to run code before the stream finishes.

### 163: What is a Transform stream? Show an example.

A Transform stream changes data as it passes through. You implement `transform(chunk, encoding, callback)` and push the result.

```js
import { Transform } from "node:stream";
import { pipeline } from "node:stream/promises";

const upper = new Transform({
  transform(chunk, encoding, callback) {
    callback(null, chunk.toString().toUpperCase());
  },
});

await pipeline(process.stdin, upper, process.stdout);
```

`flush(callback)` runs at the end and lets you push any remaining data.

### 164: What is a Duplex stream and how is it different from Transform?

A Duplex stream has a readable side and a writable side that work independently. A TCP socket is a good example: what you write goes to the other machine, and what you read comes from it. In a Transform stream, the readable output is computed from the writable input. Every Transform is a Duplex, but not every Duplex is a Transform.

```js
import { Duplex } from "node:stream";

const duplex = new Duplex({
  read() {
    this.push("from read side");
    this.push(null);
  },
  write(chunk, enc, cb) {
    console.log("written:", chunk.toString());
    cb();
  },
});
```

### 165: What is objectMode in streams?

By default, streams work with strings, Buffers or `Uint8Array`. With `objectMode: true` they can carry any JavaScript value, like objects from a database. `highWaterMark` is then counted in objects instead of bytes (default 16).

```js
import { Readable, Transform } from "node:stream";

const rows = Readable.from([{ id: 1 }, { id: 2 }]); // objectMode by default
const toJSONLine = new Transform({
  writableObjectMode: true,
  transform(obj, enc, cb) {
    cb(null, JSON.stringify(obj) + "\n");
  },
});
rows.pipe(toJSONLine).pipe(process.stdout);
```

### 166: What is highWaterMark?

It is the buffer size limit that controls backpressure. For readable streams it is how much data the stream reads ahead. For writable streams it is the point where `write()` starts returning `false`. It is not a hard limit, just a signal. Default values: 64 KB for byte streams (it was 16 KB before Node 22) and 16 objects in object mode. You can check or change the default with `stream.getDefaultHighWaterMark()` and `stream.setDefaultHighWaterMark()`.

```js
fs.createReadStream("big.bin", { highWaterMark: 1024 * 1024 }); // 1 MB chunks
```

### 167: How do you read a stream with for await...of?

Readable streams are async iterable. This is the simplest way to consume them and it handles backpressure, because the next chunk is only read when your loop body is done.

```js
import { createReadStream } from "node:fs";

let bytes = 0;
for await (const chunk of createReadStream("data.bin")) {
  bytes += chunk.length;
}
console.log(bytes);
```

If an error happens, the loop throws, so wrap it in `try/catch`. If you `break` out of the loop, the stream is destroyed.

### 168: What does Readable.from do?

It creates a readable stream from an iterable or async iterable (array, generator, async generator). It is the easiest way to make a stream from data you already have or generate.

```js
import { Readable } from "node:stream";
import { pipeline } from "node:stream/promises";
import { createWriteStream } from "node:fs";

async function* rows() {
  for (let page = 1; page <= 3; page++) {
    const data = await fetchPage(page);
    for (const row of data) yield JSON.stringify(row) + "\n";
  }
}

await pipeline(Readable.from(rows()), createWriteStream("out.jsonl"));
```

### 169: What are Web Streams in Node.js and how do you convert between them and Node streams?

Node implements the web standard `ReadableStream`, `WritableStream` and `TransformStream` globally. `fetch` uses them, for example `response.body` is a web `ReadableStream`. You can convert between the two kinds:

```js
import { Readable, Writable } from "node:stream";
import { createWriteStream } from "node:fs";
import { pipeline } from "node:stream/promises";

const res = await fetch("https://example.com/big.zip");

// web -> Node
await pipeline(Readable.fromWeb(res.body), createWriteStream("big.zip"));

// Node -> web
const webStream = Readable.toWeb(fs.createReadStream("file.txt"));
```

Node streams are usually a bit faster inside Node, while web streams are portable between runtimes.

### 170: How do you know when a stream is completely done or has failed?

Use `finished()` from `node:stream/promises`. It resolves when the stream has ended or finished, and rejects if it errored or closed early. It works for readable, writable and duplex streams.

```js
import { finished } from "node:stream/promises";

const ws = fs.createWriteStream("out.txt");
ws.write("hello");
ws.end();
await finished(ws);
console.log("all data flushed");
```

### 171: What does the "MaxListenersExceededWarning" mean?

By default, an `EventEmitter` warns when more than 10 listeners are added for the same event. It usually means a leak, for example adding a listener on every request and never removing it. Fix the leak first. If you really need many listeners, raise the limit.

```js
emitter.setMaxListeners(50);
// or for all emitters
import { EventEmitter } from "node:events";
EventEmitter.defaultMaxListeners = 20;
```

### 172: How do you wait for an event with a promise?

Use `events.once()`, which returns a promise that resolves with the event's arguments. It rejects if the emitter emits `'error'` first. `events.on()` gives you an async iterator over all events.

```js
import { once, on } from "node:events";

const server = http.createServer().listen(3000);
await once(server, "listening");
console.log("server ready");

const ac = new AbortController();
for await (const [msg] of on(chat, "message", { signal: ac.signal })) {
  console.log(msg);
  if (msg === "bye") ac.abort();
}
```

### 173: What happens if an event listener is an async function and it throws?

The `emit()` call doesn't wait for or catch the promise, so the rejection becomes an unhandled rejection and crashes the process. You can enable `captureRejections` so the rejection is sent to the `'error'` event instead.

```js
import { EventEmitter } from "node:events";

const emitter = new EventEmitter({ captureRejections: true });
emitter.on("job", async () => {
  throw new Error("failed");
});
emitter.on("error", (err) => console.error("caught:", err.message));
emitter.emit("job");
```

### 174: What is the difference between EventEmitter and EventTarget in Node?

`EventTarget` is the web standard API (`addEventListener`, `dispatchEvent`) and is available globally in Node. `AbortSignal` and `MessagePort` use it. `EventEmitter` is Node's own API, used by streams, servers and most Node modules. `EventEmitter` passes any arguments to listeners, while `EventTarget` always passes an `Event` object. `EventTarget` doesn't have a special `'error'` event, and errors in its listeners are reported as uncaught exceptions.

```js
const target = new EventTarget();
target.addEventListener("ping", (e) => console.log(e.type, e.detail));
target.dispatchEvent(new CustomEvent("ping", { detail: 42 }));
```

### 175: What is events.errorMonitor?

It is a special symbol you can listen to in order to watch errors (for logging or metrics) without handling them. If there is no regular `'error'` listener, the error is still thrown.

```js
import { EventEmitter, errorMonitor } from "node:events";

emitter.on(errorMonitor, (err) => metrics.increment("emitter.errors"));
emitter.on("error", (err) => logger.error(err));
```

### 176: Where is Buffer memory stored, and why is Buffer.allocUnsafe unsafe?

Buffer memory lives outside the V8 heap, which is why it shows up as `external` and `arrayBuffers` in `process.memoryUsage()`. `Buffer.allocUnsafe()` doesn't clear the memory it hands you, so it can contain old data from earlier use, including secrets. Node also uses a shared pool for small `allocUnsafe` and `Buffer.from` allocations (under about 4 KB), which makes them fast. Use `allocUnsafe` only if you'll overwrite every byte right away. Otherwise use `Buffer.alloc()`.

### 177: What is the difference between Buffer.byteLength and string.length?

`string.length` counts UTF-16 code units. `Buffer.byteLength()` counts how many bytes the string takes in a given encoding (UTF-8 by default). They differ for anything outside ASCII. Use `byteLength` for the `Content-Length` header.

```js
const s = "héllo 👋";
s.length; // 8
Buffer.byteLength(s); // 11
```

### 178: What is the relationship between Buffer, Uint8Array and TextEncoder?

`Buffer` is a subclass of `Uint8Array`, so any API that accepts `Uint8Array` accepts a `Buffer`. Buffers add Node-specific methods like `toString('hex')`, `readUInt32BE()` and `equals()`. `TextEncoder` and `TextDecoder` are web standard APIs that convert strings to `Uint8Array` and back. Use them in code that should also run in browsers.

```js
const bytes = new TextEncoder().encode("hi"); // Uint8Array [104, 105]
new TextDecoder().decode(bytes); // 'hi'

const buf = Buffer.from(bytes.buffer, bytes.byteOffset, bytes.byteLength); // no copy
```

One difference: `buf.slice()` on a Buffer shares memory, while `Uint8Array.prototype.slice()` copies. That's why `Buffer.slice` is deprecated in favor of `subarray()`, which shares memory on both.

### 179: What is StringDecoder and when do you need it?

When you read UTF-8 text in chunks, a multi-byte character can be split between two chunks. If you call `chunk.toString()` on each chunk, you get broken characters. `StringDecoder` keeps incomplete bytes until the next chunk arrives.

```js
import { StringDecoder } from "node:string_decoder";

const decoder = new StringDecoder("utf8");
const euro = Buffer.from("€"); // 3 bytes
console.log(decoder.write(euro.subarray(0, 1))); // ''
console.log(decoder.write(euro.subarray(1))); // '€'
```

Streams do this for you when you call `setEncoding('utf8')` or pass an encoding to `createReadStream`.

### 180: What is the difference between spawn, exec, execFile and fork?

- `spawn(cmd, args)`: starts a process and gives you streams for stdin, stdout and stderr. Good for long-running processes or big output. No shell by default.
- `exec(command)`: runs a command in a shell and buffers all output (default limit 1 MB). Convenient, but risky with user input.
- `execFile(file, args)`: like `exec`, but runs the program directly without a shell. Safer.
- `fork(modulePath)`: a special `spawn` for Node scripts that sets up an IPC channel so parent and child can send messages.

```js
import { spawn } from "node:child_process";

const ls = spawn("ls", ["-la"]);
ls.stdout.on("data", (d) => process.stdout.write(d));
ls.on("close", (code) => console.log("exited with", code));
```

There are also sync versions (`execSync`, `spawnSync`), which block the event loop.

### 181: How do parent and child processes talk to each other with fork?

`fork()` creates an IPC channel. Both sides use `send()` and the `'message'` event. Messages are serialized (JSON by default, or `'advanced'` serialization, which supports more types).

```js
// parent.js
import { fork } from "node:child_process";

const child = fork("./child.js");
child.on("message", (msg) => {
  console.log("from child:", msg);
  child.kill();
});
child.send({ n: 10 });
```

```js
// child.js
process.on("message", ({ n }) => {
  process.send({ result: n * 2 });
});
```

### 182: Why is exec dangerous with user input?

`exec` passes the string to a shell, so special characters like `;`, `&&`, `|` or `$()` are interpreted. If part of the command comes from a user, they can run any command.

```js
// Dangerous: filename = "a.txt; rm -rf ~"
exec(`cat ${filename}`);

// Safe: arguments are passed directly, no shell
execFile("cat", [filename]);
spawn("cat", [filename]);
```

Also avoid `shell: true` with `spawn` when arguments come from users.

### 183: How does the cluster module distribute connections?

The primary process accepts connections and passes them to workers in round-robin order (the default on all platforms except Windows). The alternative is to let workers accept connections directly from a shared socket, where the OS decides, which often leads to uneven load. Workers are separate processes, so they don't share memory. Things like sessions or in-memory caches must be stored outside (Redis, a database). If a worker dies, the primary can start a new one.

```js
if (cluster.isPrimary) {
  for (let i = 0; i < os.availableParallelism(); i++) cluster.fork();
  cluster.on("exit", (worker, code) => {
    console.log(
      `worker ${worker.process.pid} died (${code}), starting a new one`,
    );
    cluster.fork();
  });
}
```

### 184: When should you use cluster and when worker_threads?

Use `cluster` (or several containers) to handle more incoming requests by running several copies of your server, one per CPU core. Each copy is a full process with its own memory, so a crash only affects one worker. Use `worker_threads` to move CPU-heavy work off the main thread inside one process, for example resizing images or parsing a huge file. Workers start faster than processes, use less memory, and can share memory with `SharedArrayBuffer`.

### 185: How do you send data to and from worker threads?

Use `workerData` for the initial data and `postMessage()` for messages in both directions. Data is copied with the structured clone algorithm. To avoid copying big binary data, transfer an `ArrayBuffer` with a transfer list. After transfer, the sender can't use it anymore.

```js
// main.js
import { Worker } from "node:worker_threads";

const worker = new Worker(new URL("./worker.js", import.meta.url));
const buf = new ArrayBuffer(1024 * 1024 * 100);

worker.postMessage({ buf }, [buf]); // moved, not copied
console.log(buf.byteLength); // 0
worker.on("message", (msg) => console.log(msg));
```

```js
// worker.js
import { parentPort } from "node:worker_threads";

parentPort.on("message", ({ buf }) => {
  parentPort.postMessage(`got ${buf.byteLength} bytes`);
});
```

### 186: What are SharedArrayBuffer and Atomics used for?

A `SharedArrayBuffer` is memory that several threads can see at the same time, without copying. Because two threads can change the same data at once, you use `Atomics` to read and write safely and to wait for or wake other threads.

```js
// main
const shared = new SharedArrayBuffer(4);
const counter = new Int32Array(shared);
const workers = Array.from(
  { length: 4 },
  () =>
    new Worker(new URL("./inc.js", import.meta.url), { workerData: shared }),
);

// inc.js
import { workerData } from "node:worker_threads";
const counter = new Int32Array(workerData);
for (let i = 0; i < 1000; i++) Atomics.add(counter, 0, 1);
```

Without `Atomics.add`, using `counter[0]++` would lose updates.

### 187: Why should you use a worker pool instead of creating a worker per task?

Starting a worker takes time (tens of milliseconds) and memory because each has its own V8 instance. Creating one per request is slow and can run you out of memory under load. A pool creates a fixed number of workers once and gives them tasks from a queue. Libraries like `piscina` or `workerpool` do this for you.

```js
import Piscina from "piscina";

const pool = new Piscina({
  filename: new URL("./resize.js", import.meta.url).href,
});

app.post("/resize", async (req, res) => {
  const result = await pool.run({ image: req.body.image, width: 200 });
  res.json(result);
});
```

### 188: What is HTTP keep-alive and what does http.Agent do?

Keep-alive means reusing a TCP connection (and TLS session) for several HTTP requests instead of opening a new one each time. This saves a lot of time. On the client side, `http.Agent` manages a pool of connections per host. Since Node 19, the global agent uses keep-alive by default. You can create your own agent to control limits.

```js
import http from "node:http";

const agent = new http.Agent({
  keepAlive: true,
  maxSockets: 50,
  maxFreeSockets: 10,
});
http.get({ host: "api.local", path: "/", agent }, (res) => res.resume());
```

`fetch` uses undici, which has its own connection pooling and keep-alive.

### 189: Which timeouts does an http.Server have?

- `server.requestTimeout` (default 300000 ms): max time to receive the whole request.
- `server.headersTimeout` (default 60000 ms): max time to receive the request headers.
- `server.keepAliveTimeout` (default 5000 ms): how long an idle keep-alive connection stays open.
- `server.timeout` (default 0, no timeout): socket inactivity timeout.

```js
const server = http.createServer(app);
server.keepAliveTimeout = 65_000;
server.headersTimeout = 66_000;
server.requestTimeout = 30_000;
```

Behind a load balancer, set `keepAliveTimeout` higher than the load balancer's idle timeout. Otherwise Node may close a connection just as the load balancer sends a request on it, and you get random 502 errors.

### 190: How do you shut down a Node.js server gracefully?

Stop accepting new connections, let current requests finish, close database connections and other resources, then exit. Add a timeout in case something hangs.

```js
const server = app.listen(3000);

async function shutdown(signal) {
  console.log(`${signal} received, shutting down`);
  const timer = setTimeout(() => process.exit(1), 10_000);
  timer.unref();

  server.close(async () => {
    await db.end();
    process.exit(0);
  });
  server.closeIdleConnections();
}

process.on("SIGTERM", shutdown);
process.on("SIGINT", shutdown);
```

`server.close()` stops new connections and waits for open ones. `closeIdleConnections()` closes keep-alive connections that aren't doing anything, so `close()` doesn't wait for them.

### 191: What are SIGTERM and SIGINT and how do you handle them?

They are OS signals asking a process to stop. `SIGINT` is sent when you press Ctrl+C. `SIGTERM` is the normal "please stop" signal from Docker, Kubernetes, systemd and process managers. If you don't handle them, Node exits right away. Add listeners to clean up first. `SIGKILL` can't be caught.

```js
process.on("SIGTERM", () => {
  cleanup().finally(() => process.exit(0));
});
```

On Windows, signals are emulated and only some work (`SIGINT`, `SIGBREAK`, and a few others).

### 192: How do you set a timeout on a fetch request?

`fetch` has no timeout option, but you can pass `AbortSignal.timeout()`. The error you get is a `TimeoutError`.

```js
try {
  const res = await fetch("https://api.example.com/data", {
    signal: AbortSignal.timeout(5000),
  });
  console.log(await res.json());
} catch (err) {
  if (err.name === "TimeoutError") console.log("took longer than 5s");
  else throw err;
}
```

Note that the signal also covers reading the body. If the body is very large, a short timeout may abort it partway.

### 193: What is AbortSignal.any?

It creates one signal that aborts when any of the given signals aborts. It's handy when you want to cancel on either a timeout or a user action.

```js
async function download(url, userSignal) {
  const signal = AbortSignal.any([userSignal, AbortSignal.timeout(10_000)]);
  const res = await fetch(url, { signal });
  return res.arrayBuffer();
}

const ac = new AbortController();
cancelButton.on("click", () => ac.abort());
await download("https://example.com/file", ac.signal);
```

### 194: How do you stream a large file download to the client correctly?

Set the headers, then stream the file with `pipeline` so errors and client disconnects clean up the file handle.

```js
import { createReadStream } from "node:fs";
import { stat } from "node:fs/promises";
import { pipeline } from "node:stream/promises";

app.get("/download/report", async (req, res, next) => {
  try {
    const file = "./files/report.pdf";
    const { size } = await stat(file);
    res.writeHead(200, {
      "Content-Type": "application/pdf",
      "Content-Length": size,
      "Content-Disposition": 'attachment; filename="report.pdf"',
    });
    await pipeline(createReadStream(file), res);
  } catch (err) {
    if (!res.headersSent) next(err);
  }
});
```

In Express you can also use `res.download()` or `res.sendFile()`, which handle ranges and caching headers.

### 195: How do you handle file uploads in Node.js?

File uploads from HTML forms use `multipart/form-data`. `express.json()` doesn't parse it. Use a library such as `multer` (for Express) or `busboy`, or `@fastify/multipart` in Fastify. Set file size limits and check file types. For big files, stream them to disk or cloud storage instead of keeping them in memory.

```js
import multer from "multer";

const upload = multer({
  dest: "uploads/",
  limits: { fileSize: 5 * 1024 * 1024 },
});

app.post("/avatar", upload.single("avatar"), (req, res) => {
  res.json({ file: req.file.filename, size: req.file.size });
});
```

You can also use the built-in `request.formData()` if you work with web `Request` objects, but it buffers everything in memory.

### 196: Why does middleware order matter in Express?

Express runs middleware and routes in the order you register them. If the body parser comes after a route, that route sees `req.body` as `undefined`. If the auth middleware comes after a route, that route is public. The 404 handler must come after all routes, and the error handler must be last.

```js
app.use(helmet());
app.use(express.json());
app.use(requestLogger);

app.use("/public", publicRouter);
app.use(authenticate); // everything below needs auth
app.use("/api", apiRouter);

app.use((req, res) => res.status(404).json({ error: "Not found" }));
app.use(errorHandler);
```

### 197: How are errors in async route handlers handled in Express 5?

In Express 5, if a handler or middleware returns a promise that rejects, Express catches it and calls `next(err)` for you. In Express 4, a rejected promise was not caught, so the request hung and you got an unhandled rejection. People used wrappers like `express-async-errors`.

```js
// Express 5: this error goes to the error handler
app.get("/user/:id", async (req, res) => {
  const user = await User.findById(req.params.id); // may throw
  res.json(user);
});

// Express 4 needed something like this
const wrap = (fn) => (req, res, next) =>
  Promise.resolve(fn(req, res, next)).catch(next);
```

Errors thrown in callbacks like `setTimeout` are still not caught. You must pass them to `next()` yourself.

### 198: What are the main changes in Express 5 compared to Express 4?

- Rejected promises from handlers go to the error handler.
- New path syntax (path-to-regexp v8): wildcards must have names, like `/*splat`, and optional parts use braces, like `/:file{.:ext}`. Regex characters in strings are no longer supported.
- `req.body` is `undefined` (not `{}`) when no body parser ran.
- `req.query` is a getter and can't be changed. The default query parser is now `simple`.
- Removed old methods: `app.del()`, `res.sendfile()`, `req.param()`, `res.send(status)` with a number.
- `express.urlencoded` uses `extended: false` by default.
- `app.listen` passes errors to its callback.
- Requires Node 18 or newer.

### 199: How is Fastify different from Express?

Fastify is built for speed and uses JSON Schema to validate input and to serialize output faster. It has a plugin system with encapsulation, so plugins can add routes, hooks and decorators that only apply in their own scope. It has built-in logging with `pino`, and async handlers are first class. Express has a bigger ecosystem and is simpler to start with.

```js
import Fastify from "fastify";

const app = Fastify({ logger: true });

app.post(
  "/users",
  {
    schema: {
      body: {
        type: "object",
        required: ["email"],
        properties: { email: { type: "string", format: "email" } },
      },
    },
  },
  async (request) => {
    return { created: request.body.email };
  },
);

await app.listen({ port: 3000 });
```

### 200: How do you validate request input?

Never trust input from the client. Check types, required fields, lengths and formats before using the data. Common tools are `zod`, `valibot`, `joi`, `ajv` (JSON Schema) and Fastify's built-in schemas.

```js
import { z } from "zod";

const CreateUser = z.object({
  email: z.string().email(),
  name: z.string().min(1).max(100),
  age: z.number().int().positive().optional(),
});

app.post("/users", (req, res) => {
  const result = CreateUser.safeParse(req.body);
  if (!result.success) {
    return res.status(400).json({ errors: result.error.issues });
  }
  const user = result.data; // typed and checked
  res.status(201).json(user);
});
```

### 201: When would you choose sessions over JWTs, and the other way round?

**Sessions** (server-side storage plus a cookie with an ID): easy to revoke (just delete the session), small cookie, and the data stays on the server. You need shared storage like Redis if you run several servers. Good for normal web apps.

**JWTs** (signed tokens): the server doesn't need to look anything up, so they work well between services and for APIs used by mobile apps. But you can't easily revoke a token before it expires. The usual fix is short-lived access tokens (5 to 15 minutes) plus refresh tokens that are stored and can be revoked.

For browsers, keep tokens in `HttpOnly` cookies rather than `localStorage`, so XSS can't read them.

### 202: Why do you need timingSafeEqual when comparing secrets?

A normal `===` comparison stops at the first different character. An attacker can measure how long the comparison takes and guess a secret (like an API key or HMAC signature) one character at a time. `crypto.timingSafeEqual` always takes the same time for buffers of the same length.

```js
import { timingSafeEqual, createHmac } from "node:crypto";

function isValidSignature(payload, signature, secret) {
  const expected = createHmac("sha256", secret).update(payload).digest();
  const given = Buffer.from(signature, "hex");
  return given.length === expected.length && timingSafeEqual(given, expected);
}
```

### 203: How do you add rate limiting to an API?

Rate limiting caps how many requests a client can make in a time window. It protects against brute-force attacks and abuse. For a single server you can use `express-rate-limit` or `@fastify/rate-limit`. With several servers, store the counters in Redis so all of them share the limits. Often it's done at the API gateway or reverse proxy instead.

```js
import rateLimit from "express-rate-limit";

app.use(
  "/login",
  rateLimit({
    windowMs: 15 * 60 * 1000,
    limit: 5,
    standardHeaders: "draft-8",
    legacyHeaders: false,
  }),
);
```

Return `429 Too Many Requests` with a `Retry-After` header when the limit is reached.

### 204: Why use a logging library like pino instead of console.log?

`console.log` writes plain text, has no log levels and, when writing to a pipe, can slow down your app. A logging library gives you log levels, structured JSON output (easy to search in tools like Elasticsearch, Loki or Datadog), extra fields like request IDs, and redaction of secrets. `pino` is very fast because it does little work in the main thread and can move formatting to a worker thread.

```js
import pino from "pino";

const logger = pino({
  level: process.env.LOG_LEVEL ?? "info",
  redact: ["req.headers.authorization", "password"],
});

logger.info({ userId: 42, orderId: "A1" }, "order created");
logger.error({ err }, "payment failed");
```

### 205: How should you manage configuration and secrets?

- Read config from environment variables (12-factor style), not from code.
- Validate all config at startup and fail fast if something is missing.
- Keep secrets out of git. Use a secret manager (AWS Secrets Manager, Vault, Kubernetes secrets) in production. `.env` files are only for local development.
- Keep config in one module and import it from there, instead of reading `process.env` all over the code.

```js
// config.js
import { z } from "zod";

const schema = z.object({
  PORT: z.coerce.number().default(3000),
  DATABASE_URL: z.string().url(),
  JWT_SECRET: z.string().min(32),
});

export const config = schema.parse(process.env);
```

### 206: How does Node resolve a relative require() call?

For `require('./utils')`, Node tries, in order:

1. The exact path `./utils`
2. `./utils.js`, `./utils.json`, `./utils.node`
3. If `./utils` is a folder: its `package.json` `main` field, then `./utils/index.js`, `index.json`, `index.node`

ES modules don't do any of this guessing. You must write the full path with the extension, like `./utils.js` or `./utils/index.js`. Folder imports are not supported in ESM.

### 207: What are conditional exports?

Conditional exports let a package point to different files depending on how it is loaded. Common conditions are `import`, `require`, `node`, `browser`, `types` and `default`. Node picks the first matching condition in object order, so put more specific ones first and `default` last.

```json
{
  "exports": {
    ".": {
      "types": "./dist/index.d.ts",
      "node": {
        "import": "./dist/node.mjs",
        "require": "./dist/node.cjs"
      },
      "browser": "./dist/browser.js",
      "default": "./dist/index.mjs"
    },
    "./package.json": "./package.json"
  }
}
```

You can use your own conditions with `node --conditions=development app.js`.

### 208: What are subpath imports (the "imports" field)?

The `imports` field lets you create private aliases that start with `#`. They work only inside your package. This avoids long relative paths like `../../../utils` without any build tool. It can also use conditions.

```json
{
  "imports": {
    "#config": "./src/config.js",
    "#utils/*": "./src/utils/*.js",
    "#db": {
      "node": "./src/db/node.js",
      "default": "./src/db/memory.js"
    }
  }
}
```

```js
import { config } from "#config";
import { slugify } from "#utils/strings";
```

### 209: What is the dual package hazard?

If a package ships both a CommonJS and an ESM version, an app can end up loading both copies, one through `require` and one through `import`. Then you have two separate module instances: `instanceof` checks fail and any module state (like a cache or a registry) is duplicated. Ways to avoid it: ship only ESM (now easier since `require(esm)` works), make the ESM version a thin wrapper that re-exports the CommonJS one, or keep state outside the module.

### 210: Can you require() an ES module?

Yes, in current Node versions. `require(esm)` works without a flag in Node 22.12+, 20.19+ and all newer versions. It returns the module namespace object. The only limit is that the ES module (and everything it imports) must not use top-level `await`. If it does, you get `ERR_REQUIRE_ASYNC_MODULE` and must use `import()` instead.

```js
// math.mjs
export const add = (a, b) => a + b;
export default function hello() {
  return "hi";
}

// app.cjs
const math = require("./math.mjs");
console.log(math.add(1, 2)); // 3
console.log(math.default()); // 'hi'
```

This makes it much easier for library authors to publish ESM only.

### 211: What is dynamic import()?

`import()` loads a module at runtime and returns a promise. It works in both CommonJS and ESM. Use it to load code only when needed, to choose a module based on a condition, or to load ESM from CommonJS when the module uses top-level await.

```js
const lang = process.env.LANG?.startsWith("de") ? "de" : "en";
const { messages } = await import(`./i18n/${lang}.js`);

// in CommonJS
async function main() {
  const { default: chalk } = await import("chalk");
}
```

### 212: What is import.meta?

`import.meta` is an object with information about the current ES module.

```js
import.meta.url; // 'file:///home/me/app/index.js'
import.meta.filename; // '/home/me/app/index.js'
import.meta.dirname; // '/home/me/app'
import.meta.resolve("./data.json"); // absolute URL of a module, without loading it
import.meta.main; // true if this file is the entry point (newer Node versions)
```

`new URL('./file.txt', import.meta.url)` is the usual way to build paths relative to the current file. `import.meta.main` is fairly new (added in Node 24.2), so on older versions you compare `import.meta.filename` with `process.argv[1]`.

### 213: How do you import JSON files in ES modules?

You need an import attribute that tells Node the type. This is required because importing a file shouldn't be able to run code by surprise.

```js
import pkg from "./package.json" with { type: "json" };
console.log(pkg.version);

const { default: data } = await import("./data.json", {
  with: { type: "json" },
});
```

JSON modules only have a default export. For files that change at runtime, read them with `fs` instead, since imports are cached.

### 214: How do you use require() inside an ES module?

Use `module.createRequire()`. This is useful for loading CommonJS-only features like JSON files the old way, or using `require.resolve`.

```js
import { createRequire } from "node:module";

const require = createRequire(import.meta.url);
const legacy = require("./legacy.cjs");
const path = require.resolve("some-package");
```

### 215: What is the module wrapper function in CommonJS?

Before running a CommonJS file, Node wraps it in a function like this:

```js
(function (exports, require, module, __filename, __dirname) {
  // your code
});
```

That's why each file has its own scope, and why `exports`, `require`, `module`, `__filename` and `__dirname` look like globals but are actually function parameters. ES modules don't use this wrapper, which is why those names don't exist there.

### 216: How can you clear a module from the require cache?

`require.cache` is an object with loaded modules keyed by their full path. Deleting an entry makes the next `require` load the file again. This is sometimes used in tests or hot reload tools, but be careful: other modules may still hold references to the old exports.

```js
const file = require.resolve("./config.js");
delete require.cache[file];
const fresh = require("./config.js");
```

ES modules have no public API to clear their cache. A common trick is to import with a query string (`import('./x.js?v=' + Date.now())`), but each version stays in memory.

### 217: How do circular dependencies behave in CommonJS vs ESM?

In **CommonJS**, when A requires B and B requires A, B gets A's `module.exports` as it is at that moment, which may be an empty or partly filled object. Values added later by A won't be seen by B if B copied them out with destructuring.

In **ESM**, imports are live bindings. B gets a reference to A's exports. If B uses an export of A before A's code has run, you get a `ReferenceError` (temporal dead zone). If B only uses it later, inside a function, it works fine.

```js
// a.mjs
import { b } from "./b.mjs";
export const a = "A";
console.log(b);

// b.mjs
import { a } from "./a.mjs";
export const b = "B";
export function useA() {
  return a;
} // fine when called later
// console.log(a);  // ReferenceError if run at load time
```

### 218: How do you use hooks and subtests in node:test?

```js
import { describe, it, before, after, beforeEach, afterEach } from "node:test";
import assert from "node:assert/strict";

describe("UserService", () => {
  let db;

  before(async () => {
    db = await connectTestDb();
  });
  after(async () => {
    await db.close();
  });
  beforeEach(async () => {
    await db.reset();
  });

  it("creates a user", async () => {
    const user = await createUser(db, { name: "Ana" });
    assert.equal(user.name, "Ana");
  });

  it.skip("not ready yet", () => {});
  it.todo("handles duplicates");
});
```

You can also run only some tests with `it.only` plus `--test-only`, or filter by name with `--test-name-pattern`.

### 219: How do you mock functions and timers with node:test?

The test context and the `mock` object give you spies, method mocks and fake timers. Mocks are reset after each test when you use `t.mock`.

```js
import { test, mock } from "node:test";
import assert from "node:assert/strict";

test("calls the callback", () => {
  const fn = mock.fn((x) => x * 2);
  [1, 2].map(fn);
  assert.equal(fn.mock.callCount(), 2);
  assert.deepEqual(fn.mock.calls[0].arguments, [1, 0, [1, 2]]);
});

test("mocks a method", (t) => {
  t.mock.method(Math, "random", () => 0.5);
  assert.equal(Math.random(), 0.5);
});

test("fake timers", (t) => {
  t.mock.timers.enable({ apis: ["setTimeout", "Date"] });
  const cb = t.mock.fn();
  setTimeout(cb, 1000);
  t.mock.timers.tick(1000);
  assert.equal(cb.mock.callCount(), 1);
});
```

### 220: How do you get code coverage with the built-in test runner?

```bash
node --test --experimental-test-coverage
node --test --experimental-test-coverage \
  --test-coverage-include='src/**' \
  --test-coverage-lines=80 \
  --test-reporter=lcov --test-reporter-destination=lcov.info
```

`--test-coverage-lines`, `--test-coverage-branches` and `--test-coverage-functions` make the run fail if coverage is below the number. Coverage is still marked experimental. Another option is `c8`, which uses the same V8 coverage data.

### 221: How do you run tests in watch mode and choose which tests run?

```bash
node --test --watch
node --test 'src/**/*.test.js'
node --test --test-name-pattern="login"
node --test --test-concurrency=4
node --test --test-reporter=spec
node --test --test-shard=1/3      # split tests across CI machines
```

By default each test file runs in its own child process, so files don't affect each other. `--test-isolation=none` runs all files in one process, which is faster but shares state.

### 222: How do you test an HTTP server without extra libraries?

Start the server on port `0` so the OS picks a free port, then call it with `fetch`.

```js
import { test, before, after } from "node:test";
import assert from "node:assert/strict";
import { once } from "node:events";
import { createApp } from "../src/app.js";

let server, baseUrl;

before(async () => {
  server = createApp().listen(0);
  await once(server, "listening");
  baseUrl = `http://localhost:${server.address().port}`;
});

after(() => server.close());

test("GET /health returns 200", async () => {
  const res = await fetch(`${baseUrl}/health`);
  assert.equal(res.status, 200);
  assert.deepEqual(await res.json(), { ok: true });
});
```

`supertest` is a popular library that does something similar without having to start the server yourself.

### 223: What ways are there to debug Node.js besides console.log?

- `node --inspect` with Chrome DevTools (`chrome://inspect`) or VS Code
- `node --inspect-brk` to stop before the first line
- `debugger;` statements, which act as breakpoints when a debugger is attached
- `node inspect app.js` for the built-in terminal debugger
- `NODE_DEBUG=http,net node app.js` to see Node's own debug output
- `--trace-warnings`, `--trace-uncaught`, `--trace-deprecation` for more detail on warnings and errors
- `--cpu-prof` and `--heap-prof` for performance problems

### 224: What is util.debuglog / NODE_DEBUG?

`util.debuglog(section)` creates a logging function that only prints when the `NODE_DEBUG` environment variable includes that section name. Node core uses it internally, and you can use it in your own libraries.

```js
import { debuglog } from "node:util";
const debug = debuglog("cache");

debug("miss for key %s", key); // prints only if NODE_DEBUG includes 'cache'
```

```bash
NODE_DEBUG=cache node app.js
NODE_DEBUG=http,net node app.js
```

### 225: What is util.promisify.custom?

Some functions don't follow the normal error-first pattern, so plain `promisify` gets them wrong. You can tell `promisify` which promise version to use by setting `util.promisify.custom` on the function. Node does this for `setTimeout` and others.

```js
import { promisify } from "node:util";

function lookup(name, cb) {
  /* callback(err, address, family) */
}
lookup[promisify.custom] = (name) =>
  new Promise((resolve, reject) =>
    lookup(name, (err, address, family) =>
      err ? reject(err) : resolve({ address, family }),
    ),
  );

const lookupAsync = promisify(lookup);
const { address } = await lookupAsync("example.com");
```

### 226: What are util.types and util.isDeepStrictEqual?

`util.types` has reliable type checks for built-in objects that `typeof` and `instanceof` can't always handle, for example values coming from another realm or a worker. `util.isDeepStrictEqual` compares two values deeply, the same way `assert.deepStrictEqual` does, but returns a boolean instead of throwing.

```js
import util from "node:util";

util.types.isPromise(Promise.resolve()); // true
util.types.isDate(new Date()); // true
util.types.isProxy(new Proxy({}, {})); // true
util.types.isNativeError(new TypeError()); // true

util.isDeepStrictEqual({ a: [1, 2] }, { a: [1, 2] }); // true
util.isDeepStrictEqual({ a: 1 }, { a: "1" }); // false
```

### 227: What are common mistakes when handling errors in async code?

- **Forgetting `await`**: a `try/catch` around `doThing()` without `await` won't catch its rejection.
- **Using `async` callbacks with `forEach`**: `forEach` doesn't wait, so errors become unhandled. Use `for...of` or `Promise.all`.
- **Returning without `await` inside `try`**: `return promise` inside `try` skips the `catch`. Use `return await promise` there.
- **Swallowing errors**: an empty `catch {}` hides real problems.
- **Throwing non-Error values**: `throw 'oops'` has no stack trace.

```js
// wrong
try {
  items.forEach(async (i) => await save(i));
} catch (e) {
  /* never reached */
}

// right
for (const i of items) await save(i);
// or in parallel
await Promise.all(items.map(save));
```

### 228: How do you create custom error classes?

Extend `Error`, set `name`, and add fields like a status code or error code. This lets you tell error types apart with `instanceof` or `code` and turn them into proper HTTP responses.

```js
export class AppError extends Error {
  constructor(message, { status = 500, code = "INTERNAL", cause } = {}) {
    super(message, { cause });
    this.name = this.constructor.name;
    this.status = status;
    this.code = code;
  }
}

export class NotFoundError extends AppError {
  constructor(what) {
    super(`${what} not found`, { status: 404, code: "NOT_FOUND" });
  }
}

app.use((err, req, res, next) => {
  if (err instanceof AppError) {
    return res
      .status(err.status)
      .json({ code: err.code, message: err.message });
  }
  req.log.error(err);
  res.status(500).json({ code: "INTERNAL", message: "Something went wrong" });
});
```

### 229: What is the difference between operational errors and programmer errors?

**Operational errors** are expected problems at runtime: a file is missing, the network is down, the user sent bad input, the database timed out. You handle them: retry, return a 4xx/5xx response, log a warning.

**Programmer errors** are bugs: reading a property of `undefined`, calling a function with wrong arguments, a typo. You can't really "handle" these. The best thing is to log them, crash, and let a process manager restart the app, then fix the code.

### 230: How do you keep a Node.js app running in production?

A Node process exits when it crashes, so something has to restart it. Options:

- **Container orchestrators** (Kubernetes, ECS, Docker with a restart policy): the most common today. Run one process per container.
- **systemd** on a plain Linux server.
- **PM2**: a Node process manager with restarts, cluster mode, log handling and zero-downtime reloads.

```bash
pm2 start server.js -i max --name api
pm2 reload api
```

Whatever you choose, also add health checks, logs and a graceful shutdown.

### 231: What are good practices for running Node.js in Docker?

- Use an official slim or alpine image of an LTS version, and pin the version.
- Use multi-stage builds so dev tools don't end up in the final image.
- Copy `package*.json` first and run `npm ci`, so the dependency layer is cached.
- Run as a non-root user (the official images have a `node` user).
- Start with `node server.js`, not `npm start`, so signals reach Node directly.
- Handle `SIGTERM` for graceful shutdown. Use `--init` or `tini` if your app starts child processes.
- Add a `.dockerignore` with `node_modules`, `.git` and `.env`.

```dockerfile
FROM node:24-slim AS deps
WORKDIR /app
COPY package*.json ./
RUN npm ci --omit=dev

FROM node:24-slim
WORKDIR /app
ENV NODE_ENV=production
COPY --from=deps /app/node_modules ./node_modules
COPY . .
USER node
EXPOSE 3000
CMD ["node", "server.js"]
```

### 232: Why should you validate environment variables at startup?

If a required variable is missing or wrong, you want the app to fail right away with a clear message, not hours later when some code path finally uses it. Also, all values in `process.env` are strings, so `"false"` is truthy and `"3000"` is not a number. Parse and validate them once (with `zod` or similar, see question 205) and export a typed config object.

### 233: What caching strategies can you use in a Node.js app?

- **In-process memory** (a `Map` or `lru-cache`): fastest, but each instance has its own copy and it's lost on restart. Always set a size limit.
- **Shared cache** (Redis, Valkey, Memcached): shared between instances, survives restarts of the app.
- **HTTP caching**: `Cache-Control`, `ETag` and `Last-Modified` headers, so browsers and CDNs cache responses.
- **CDN** for static and public responses.

Common patterns are cache-aside (check cache, else load and store), setting TTLs, and deleting keys when data changes.

```js
async function getUser(id) {
  const key = `user:${id}`;
  const cached = await redis.get(key);
  if (cached) return JSON.parse(cached);

  const user = await db.users.find(id);
  await redis.set(key, JSON.stringify(user), { EX: 300 });
  return user;
}
```

### 234: What are common causes of memory leaks in Node.js?

- Caches or maps that grow forever.
- Event listeners added again and again and never removed.
- Timers (`setInterval`) that are never cleared and hold references.
- Closures that keep large objects alive.
- Global variables, or storing request objects in module-level arrays.
- Promises that never settle and keep their closures alive.
- Not consuming HTTP response bodies, which keeps sockets and buffers around.

The symptom is `heapUsed` or `rss` that keeps growing and never goes down after garbage collection.

### 235: How do you measure how long code takes in Node.js?

Use `performance.now()` for high-resolution timing, `performance.mark/measure` for named measurements, or `process.hrtime.bigint()` for nanoseconds. `performance.timerify` wraps a function to measure every call.

```js
const start = performance.now();
await doWork();
console.log(`took ${(performance.now() - start).toFixed(1)} ms`);

performance.mark("a");
await step();
performance.mark("b");
const m = performance.measure("step", "a", "b");
console.log(m.duration);
```

`performance` is a global, and more tools are in `node:perf_hooks`.

### 236: How do you measure event loop delay?

Use `monitorEventLoopDelay` from `perf_hooks`. It samples how late timers fire, which shows how much the main thread is blocked.

```js
import { monitorEventLoopDelay } from "node:perf_hooks";

const h = monitorEventLoopDelay({ resolution: 20 });
h.enable();

setInterval(() => {
  console.log({
    p50: h.percentile(50) / 1e6,
    p99: h.percentile(99) / 1e6,
    max: h.max / 1e6,
  }); // in ms
  h.reset();
}, 10_000).unref();
```

If p99 is often above tens of milliseconds, something is blocking the loop.

### 237: How do you find code that blocks the event loop?

- Measure event loop delay (question 236) to confirm there is a problem.
- Take a CPU profile with `node --cpu-prof` or the DevTools Profiler, and look for long synchronous functions.
- Use `--trace-sync-io` to print a warning every time sync I/O is used after the first tick.
- Look for usual suspects: `*Sync` functions, `JSON.parse`/`stringify` on huge objects, heavy regex, big loops, sync crypto like `pbkdf2Sync`, sorting large arrays.

```bash
node --trace-sync-io server.js
node --cpu-prof --cpu-prof-dir=./profiles server.js
```

### 238: How do you handle CPU-heavy work in a Node.js server?

Options, from simplest to most complex:

1. Make it cheaper (better algorithm, caching, do less).
2. Split it into small chunks and yield with `setImmediate` between them, so I/O can run.
3. Move it to worker threads with a pool (`piscina`).
4. Move it to a separate service or a job queue (BullMQ, RabbitMQ) and process it in the background.
5. Use native code or WebAssembly for hot spots.

```js
async function processInChunks(items, fn, size = 1000) {
  for (let i = 0; i < items.length; i += size) {
    items.slice(i, i + size).forEach(fn);
    await new Promise(setImmediate); // let the event loop breathe
  }
}
```

### 239: Why can JSON.parse and JSON.stringify be a problem on a server?

They are synchronous and run on the main thread. Parsing or stringifying a large payload (several MB) can block the event loop for tens or hundreds of milliseconds, and every other request waits. Fixes: limit request body size, paginate responses, stream large data as NDJSON, use a streaming parser, or move the work to a worker. Faster serializers like `fast-json-stringify` (used by Fastify) help when the shape of the data is known.

### 240: How do you return a large list of records from an API efficiently?

- **Pagination**: return a page at a time. Cursor-based pagination (`?after=lastId`) is faster and more stable than `OFFSET` for large tables.
- **Streaming**: stream rows from the database to the response as they arrive (for exports), for example as NDJSON or CSV.
- **Select only needed columns** and compress the response.

```js
app.get("/export", async (req, res) => {
  res.setHeader("Content-Type", "application/x-ndjson");
  const cursor = db.query("SELECT id, email FROM users").stream();
  await pipeline(
    cursor,
    new Transform({
      objectMode: true,
      transform(row, _, cb) {
        cb(null, JSON.stringify(row) + "\n");
      },
    }),
    res,
  );
});
```

### 241: What is database connection pooling and why is it important?

Opening a database connection is slow (TCP, TLS, auth). A pool keeps a set of open connections and lends them to queries. Without a pool you either open a connection per request (slow) or use one connection for everything (queries queue up). Set the pool size based on the database's connection limit divided by the number of app instances.

```js
import pg from "pg";

const pool = new pg.Pool({
  connectionString: process.env.DATABASE_URL,
  max: 10,
  idleTimeoutMillis: 30_000,
});

const { rows } = await pool.query("SELECT * FROM users WHERE id = $1", [id]);

// for transactions, take one client and always release it
const client = await pool.connect();
try {
  await client.query("BEGIN");
  // ...
  await client.query("COMMIT");
} catch (e) {
  await client.query("ROLLBACK");
  throw e;
} finally {
  client.release();
}
```

### 242: How do you prevent SQL injection?

Never build SQL by joining strings with user input. Use parameterized queries (placeholders), where the driver sends values separately from the SQL text. ORMs and query builders do this for you, but be careful with their "raw" functions.

```js
// vulnerable
db.query(`SELECT * FROM users WHERE email = '${req.body.email}'`);

// safe
db.query("SELECT * FROM users WHERE email = $1", [req.body.email]);
```

Column names and sort directions can't be parameters, so check them against an allow list.

### 243: How do you use transactions and prepared statements with node:sqlite?

```js
import { DatabaseSync } from "node:sqlite";

const db = new DatabaseSync(":memory:");
db.exec(`
  CREATE TABLE accounts (id INTEGER PRIMARY KEY, balance INTEGER NOT NULL);
  INSERT INTO accounts (balance) VALUES (100), (50);
`);

const update = db.prepare(
  "UPDATE accounts SET balance = balance + ? WHERE id = ?",
);

function transfer(from, to, amount) {
  db.exec("BEGIN");
  try {
    update.run(-amount, from);
    update.run(amount, to);
    db.exec("COMMIT");
  } catch (err) {
    db.exec("ROLLBACK");
    throw err;
  }
}

transfer(1, 2, 30);
console.log(db.prepare("SELECT * FROM accounts").all());
```

The API is synchronous, which is fine for SQLite since it's a local file, but very slow queries will block the event loop.

### 244: What HTTP security headers should a Node.js app set?

- `Content-Security-Policy`: limits where scripts, styles and images can load from.
- `Strict-Transport-Security`: forces HTTPS.
- `X-Content-Type-Options: nosniff`: stops browsers from guessing content types.
- `X-Frame-Options` or CSP `frame-ancestors`: protects against clickjacking.
- `Referrer-Policy`: controls how much of the URL is sent to other sites.
- Remove `X-Powered-By` so you don't advertise your framework.

The `helmet` middleware sets good defaults:

```js
import helmet from "helmet";
app.use(helmet());
app.disable("x-powered-by"); // helmet already does this
```

### 245: What is prototype pollution?

It is when an attacker sends a payload like `{"__proto__": {"isAdmin": true}}` and some code merges it into an object without checks. That changes `Object.prototype`, so every object in the app suddenly has `isAdmin: true`. It usually happens in deep merge, clone or "set by path" helpers.

Protection:

- Validate input with a schema that doesn't allow unknown keys.
- Skip `__proto__`, `constructor` and `prototype` keys when merging.
- Use `Object.create(null)` or `Map` for dictionaries built from user data.
- Run Node with `--disable-proto=delete` to remove `__proto__` entirely.
- Keep dependencies updated, since many old libraries had this bug.

### 246: What is ReDoS?

Regular expression Denial of Service. Some regex patterns, like `/(a+)+$/`, take exponential time on certain inputs because of backtracking. Since regex runs on the main thread, one bad request can freeze the whole server.

```js
const bad = /^(\w+\s?)*$/;
bad.test("a".repeat(30) + "!"); // can take a very long time
```

Fixes: avoid nested quantifiers, limit input length before matching, use tested validation libraries, and check patterns with tools like `safe-regex` or the linting rules for it.

### 247: How do you protect a project from malicious or vulnerable npm packages?

- Commit the lock file and install with `npm ci`.
- Run `npm audit` (or Snyk, Socket, Dependabot) in CI.
- Review new dependencies: how popular, who maintains them, how many dependencies they pull in.
- Consider `npm install --ignore-scripts` or `ignore-scripts=true` in `.npmrc`, since install scripts are a common attack path.
- Check package provenance (`npm audit signatures`).
- Use exact or limited version ranges for critical packages, and use tools that delay new versions for a few days.
- Don't install from random URLs or git repos.

### 248: What is path traversal and how do you prevent it?

Path traversal is when user input like `../../etc/passwd` is used to build a file path, so the attacker reads files outside the folder you meant. Resolve the full path and check it stays inside the allowed folder.

```js
import path from "node:path";

const ROOT = path.resolve("uploads");

function safePath(userInput) {
  const full = path.resolve(ROOT, userInput);
  if (!full.startsWith(ROOT + path.sep)) {
    throw new Error("Invalid path");
  }
  return full;
}
```

Also be careful with null bytes and with symlinks inside the allowed folder.

### 249: How do you set up an HTTPS server with good TLS settings?

```js
import https from "node:https";
import { readFileSync } from "node:fs";

const server = https.createServer(
  {
    key: readFileSync("/etc/ssl/private/key.pem"),
    cert: readFileSync("/etc/ssl/certs/fullchain.pem"),
    minVersion: "TLSv1.2",
  },
  app,
);

server.listen(443);
```

Node's TLS defaults are already reasonable. In practice, many teams terminate TLS at a load balancer or proxy (nginx, Caddy, a cloud load balancer) that handles certificate renewal, and run Node over plain HTTP inside the private network.

### 250: What is the http2 module and when would you use it?

HTTP/2 sends many requests over one connection at the same time (multiplexing), compresses headers, and uses binary framing. Browsers only support it over TLS. Node's `http2` module has a compatibility API similar to `http`, and a lower-level stream API.

```js
import http2 from "node:http2";
import { readFileSync } from "node:fs";

const server = http2.createSecureServer({
  key: readFileSync("key.pem"),
  cert: readFileSync("cert.pem"),
  allowHTTP1: true,
});

server.on("stream", (stream, headers) => {
  stream.respond({ ":status": 200, "content-type": "text/plain" });
  stream.end(`You asked for ${headers[":path"]}`);
});

server.listen(8443);
```

Often a reverse proxy speaks HTTP/2 or HTTP/3 to clients and HTTP/1.1 to Node. HTTP/2 is also required for gRPC.

### 251: How do you compress HTTP responses with zlib?

Check the `Accept-Encoding` header and pipe the response through the right compressor. Brotli usually gives smaller output, gzip is faster and supported everywhere.

```js
import zlib from "node:zlib";
import { pipeline } from "node:stream/promises";

http
  .createServer(async (req, res) => {
    const accept = req.headers["accept-encoding"] ?? "";
    const source = fs.createReadStream("big.json");
    res.setHeader("Content-Type", "application/json");
    res.setHeader("Vary", "Accept-Encoding");

    if (accept.includes("br")) {
      res.setHeader("Content-Encoding", "br");
      await pipeline(source, zlib.createBrotliCompress(), res);
    } else if (accept.includes("gzip")) {
      res.setHeader("Content-Encoding", "gzip");
      await pipeline(source, zlib.createGzip(), res);
    } else {
      await pipeline(source, res);
    }
  })
  .listen(3000);
```

In Express you can use the `compression` middleware, or let the proxy or CDN do it.

### 252: How do you encrypt and decrypt data with crypto?

Use an authenticated cipher such as AES-256-GCM. Use a random IV for every message and store the IV and the auth tag along with the ciphertext. The key must be 32 random bytes kept secret.

```js
import { createCipheriv, createDecipheriv, randomBytes } from "node:crypto";

const key = randomBytes(32); // load from a secret store in real apps

function encrypt(text) {
  const iv = randomBytes(12);
  const cipher = createCipheriv("aes-256-gcm", key, iv);
  const data = Buffer.concat([cipher.update(text, "utf8"), cipher.final()]);
  const tag = cipher.getAuthTag();
  return Buffer.concat([iv, tag, data]).toString("base64");
}

function decrypt(payload) {
  const buf = Buffer.from(payload, "base64");
  const iv = buf.subarray(0, 12);
  const tag = buf.subarray(12, 28);
  const data = buf.subarray(28);
  const decipher = createDecipheriv("aes-256-gcm", key, iv);
  decipher.setAuthTag(tag);
  return Buffer.concat([decipher.update(data), decipher.final()]).toString(
    "utf8",
  );
}

console.log(decrypt(encrypt("secret message")));
```

Never reuse an IV with the same key in GCM mode.

### 253: What is the difference between Math.random and crypto random functions?

`Math.random()` is fast but not cryptographically secure. Its output can be predicted. Use it for things like shuffling a UI list. For tokens, passwords, session IDs, OTP codes or anything security-related, use `crypto.randomBytes`, `crypto.randomInt`, `crypto.randomUUID` or `crypto.getRandomValues`.

```js
import { randomInt, randomBytes } from "node:crypto";

const otp = randomInt(0, 1_000_000).toString().padStart(6, "0");
const resetToken = randomBytes(32).toString("base64url");
```

### 254: What is the Web Crypto API in Node.js?

It is the browser's `crypto.subtle` API, available globally in Node. It is promise based and works the same in browsers, Deno, Bun and edge runtimes, so it is a good choice for code that must run in many places. The `node:crypto` module has more features and is often more convenient for Node-only code.

```js
const data = new TextEncoder().encode("hello");
const digest = await crypto.subtle.digest("SHA-256", data);
console.log(Buffer.from(digest).toString("hex"));

const key = await crypto.subtle.generateKey(
  { name: "HMAC", hash: "SHA-256" },
  true,
  ["sign", "verify"],
);
const sig = await crypto.subtle.sign("HMAC", key, data);
```

### 255: How do you verify a webhook signature?

Most webhook providers sign the raw request body with HMAC and a shared secret. Compute the same HMAC on the raw bytes (not on re-serialized JSON) and compare with `timingSafeEqual`. Also check the timestamp to block replay attacks.

```js
import express from "express";
import { createHmac, timingSafeEqual } from "node:crypto";

app.post("/webhook", express.raw({ type: "application/json" }), (req, res) => {
  const sig = Buffer.from(req.get("x-signature") ?? "", "hex");
  const expected = createHmac("sha256", process.env.WEBHOOK_SECRET)
    .update(req.body) // Buffer with the raw body
    .digest();

  if (sig.length !== expected.length || !timingSafeEqual(sig, expected)) {
    return res.sendStatus(401);
  }
  const event = JSON.parse(req.body.toString("utf8"));
  res.sendStatus(200);
});
```

### 256: How do you read a very large file line by line?

Use `readline` with a file stream, or `fs.promises` `FileHandle.readLines()`. Memory stays low no matter how big the file is.

```js
import { open } from "node:fs/promises";

const file = await open("huge.csv");
let count = 0;
for await (const line of file.readLines()) {
  if (line.startsWith("ERROR")) count++;
}
console.log(count);
```

### 257: What is the difference between fs.watch and fs.watchFile?

`fs.watch` uses OS events (inotify, FSEvents, ReadDirectoryChangesW), so it's fast and efficient, but its behavior differs between platforms. It can fire twice for one change and doesn't always report filenames. `recursive: true` works on Linux, macOS and Windows in current versions. `fs.watchFile` polls the file with `stat` on an interval. It's slower and uses more CPU but is consistent, and it also works on network file systems.

```js
import { watch } from "node:fs/promises";

const ac = new AbortController();
for await (const event of watch("./src", {
  recursive: true,
  signal: ac.signal,
})) {
  console.log(event.eventType, event.filename);
}
```

For serious use, libraries like `chokidar` smooth over the differences.

### 258: How do you find files with glob patterns without a library?

`fs.glob`, `fs.globSync` and `fs.promises.glob` are built in (added in Node 22).

```js
import { glob } from "node:fs/promises";

for await (const file of glob("src/**/*.{js,ts}", {
  exclude: ["**/node_modules/**"],
})) {
  console.log(file);
}

const tests = await Array.fromAsync(glob("**/*.test.js"));
```

`path.matchesGlob(path, pattern)` checks if a single path matches a pattern.

### 259: What is a FileHandle and when do you use fs.open?

`fs.promises.open()` returns a `FileHandle`, an object wrapping a file descriptor. You use it when you need several operations on the same file, reading or writing at specific positions, or more control than `readFile` gives. Always close it, or use `await using` so it closes automatically.

```js
import { open } from "node:fs/promises";

const fh = await open("data.bin", "r");
try {
  const buf = Buffer.alloc(16);
  const { bytesRead } = await fh.read(buf, 0, 16, 100); // read 16 bytes at offset 100
  console.log(bytesRead, buf);
  const { size } = await fh.stat();
} finally {
  await fh.close();
}

// Node 24+: closes automatically at the end of the block
{
  await using file = await open("notes.txt");
  console.log(await file.readFile("utf8"));
}
```

### 260: How do you create temporary files and folders safely?

Use `fs.mkdtemp` with a prefix inside `os.tmpdir()`. It adds random characters so names don't collide. Clean up in `finally`. Newer Node versions also have `fs.mkdtempDisposable()`, which works with `await using`.

```js
import { mkdtemp, writeFile, rm } from "node:fs/promises";
import { tmpdir } from "node:os";
import path from "node:path";

const dir = await mkdtemp(path.join(tmpdir(), "myapp-"));
try {
  await writeFile(path.join(dir, "data.txt"), "temp");
  // ...
} finally {
  await rm(dir, { recursive: true, force: true });
}
```

### 261: How do you write a file atomically?

If the process crashes during `writeFile`, the file can be left half written. To avoid this, write to a temp file in the same folder, then `rename` it over the real file. `rename` is atomic on the same file system, so readers see either the old or the new version.

```js
import { writeFile, rename } from "node:fs/promises";
import { randomUUID } from "node:crypto";

async function writeAtomic(file, data) {
  const tmp = `${file}.${randomUUID()}.tmp`;
  await writeFile(tmp, data);
  await rename(tmp, file);
}
```

For full durability you would also `fsync` the file before renaming. Libraries like `write-file-atomic` handle the details.

### 262: What is AsyncLocalStorage?

`AsyncLocalStorage` (in `node:async_hooks`) stores data that follows an async flow, like thread-local storage in other languages. You set a value at the start of a request and can read it anywhere down the call chain, even after `await`s and callbacks, without passing it through every function. It's used for request IDs in logs, tracing and per-request context.

```js
import { AsyncLocalStorage } from "node:async_hooks";
import { randomUUID } from "node:crypto";

const als = new AsyncLocalStorage();

app.use((req, res, next) => {
  als.run({ requestId: req.get("x-request-id") ?? randomUUID() }, next);
});

export function log(msg) {
  const ctx = als.getStore();
  console.log(JSON.stringify({ requestId: ctx?.requestId, msg }));
}

app.get("/", async (req, res) => {
  await db.query("...");
  log("handled"); // still knows the request id
  res.end();
});
```

### 263: What is diagnostics_channel?

It is a module for publishing diagnostic data that tools can subscribe to. Libraries publish events on named channels, and APM or logging tools listen without patching the library's code. If no one subscribes, publishing costs almost nothing. Node core publishes events for `http`, `net`, `undici` (fetch), `worker_threads` and more.

```js
import diagnostics_channel from "node:diagnostics_channel";

diagnostics_channel.subscribe("http.server.request.start", ({ request }) => {
  console.log("request", request.method, request.url);
});

// in your own library
const channel = diagnostics_channel.channel("mylib:query");
if (channel.hasSubscribers) channel.publish({ sql });
```

### 264: What do timer.unref() and timer.ref() do?

A pending timer keeps the process alive. `unref()` tells Node not to wait for this timer when deciding whether to exit. It's useful for background jobs like metrics flushing or cache cleanup that should not stop the process from exiting. `ref()` undoes it. Servers, sockets and child processes have the same methods.

```js
const interval = setInterval(flushMetrics, 10_000);
interval.unref(); // the process can still exit when other work is done
```

### 265: Why is setInterval not exact, and how do you run something at a steady rate?

Timers are not real-time. They fire at the earliest after the delay, and only when the event loop gets to them. If the loop is busy, they fire late. Also, if each callback takes a while, `setInterval` doesn't wait for it, so async callbacks can overlap. For a job that must not overlap, chain `setTimeout` after each run finishes. For steady rate, compute the next run based on the clock.

```js
async function every(ms, job) {
  while (true) {
    const started = performance.now();
    await job();
    const elapsed = performance.now() - started;
    await new Promise((r) => setTimeout(r, Math.max(0, ms - elapsed)));
  }
}
```

### 266: What is Promise.withResolvers?

`Promise.withResolvers()` returns an object with a new promise and its `resolve` and `reject` functions. It saves you from the old pattern of copying them out of the constructor callback. Available since Node 22.

```js
function waitForEvent(emitter, name) {
  const { promise, resolve, reject } = Promise.withResolvers();
  emitter.once(name, resolve);
  emitter.once("error", reject);
  return promise;
}
```

### 267: Which newer JavaScript features can you use in current Node.js LTS versions?

Node 22 and 24 include, among others:

- `Object.groupBy` and `Map.groupBy`
- Array methods that don't mutate: `toSorted`, `toReversed`, `toSpliced`, `with`, and `findLast`
- `Array.fromAsync`
- `Set` methods: `union`, `intersection`, `difference`, `symmetricDifference`, `isSubsetOf`
- Iterator helpers: `.map`, `.filter`, `.take`, `.drop`, `.toArray` on iterators
- `Promise.withResolvers`, `Promise.try` (Node 24 / V8 13+)
- `RegExp` `v` flag, and `RegExp.escape` (Node 24)
- `Error.isError`, `Float16Array` (Node 24)
- Explicit resource management: `using` and `await using` (Node 24)

```js
const byRole = Object.groupBy(users, (u) => u.role);
const top = users.toSorted((a, b) => b.score - a.score).slice(0, 3);
const admins = new Set(a).intersection(new Set(b));
const firstTen = someIterator().filter(isValid).take(10).toArray();
```

### 268: What is explicit resource management (using / await using)?

It is a JavaScript feature, supported from Node 24, that cleans up resources automatically when a block ends, even if an error is thrown. An object is disposable if it has a `[Symbol.dispose]()` or `[Symbol.asyncDispose]()` method. Several Node objects support it, like `FileHandle`, timers and some stream objects.

```js
class Lock {
  constructor(name) {
    this.name = name;
    console.log("lock", name);
  }
  [Symbol.dispose]() {
    console.log("unlock", this.name);
  }
}

function work() {
  using lock = new Lock("orders");
  // do stuff, even if this throws, unlock runs
}

async function readConfig() {
  await using fh = await fs.promises.open("config.json");
  return JSON.parse(await fh.readFile("utf8"));
} // fh.close() is called here
```

### 269: What can't structuredClone copy?

- Functions (throws `DataCloneError`)
- Class instances keep their own data but lose their prototype, so they become plain objects
- Symbols as values, getters and setters (getters are evaluated, the result is copied)
- Property descriptors, so read-only properties become writable
- Some native objects like sockets or streams

Errors, `Date`, `RegExp`, `Map`, `Set`, `ArrayBuffer`, typed arrays, `Blob` and circular references are supported. You can also pass a transfer list to move `ArrayBuffer`s instead of copying them.

### 270: How do you build a WebSocket server in Node.js?

Node core has a WebSocket client but not a server. Use the `ws` package, which is small and fast and can share a port with your HTTP server.

```js
import http from "node:http";
import { WebSocketServer } from "ws";

const server = http.createServer(app);
const wss = new WebSocketServer({ server });

wss.on("connection", (socket, req) => {
  socket.on("message", (data) => {
    for (const client of wss.clients) {
      if (client.readyState === client.OPEN) client.send(data.toString());
    }
  });
  socket.on("close", () => console.log("client left"));
});

server.listen(3000);
```

Remember to check authentication during the upgrade and to send pings to detect dead connections. With several servers you need a pub/sub system (Redis) to send messages to clients connected to other instances.

### 271: What are Server-Sent Events and how do you implement them?

SSE is a simple way for the server to push text events to the browser over a normal HTTP response that stays open. The browser uses `EventSource` and reconnects automatically. It's one-way only (server to client), which is enough for notifications, progress bars and live feeds.

```js
app.get("/events", (req, res) => {
  res.writeHead(200, {
    "Content-Type": "text/event-stream",
    "Cache-Control": "no-cache",
    Connection: "keep-alive",
  });

  const timer = setInterval(() => {
    res.write(`event: tick\ndata: ${JSON.stringify({ time: Date.now() })}\n\n`);
  }, 1000);

  req.on("close", () => clearInterval(timer));
});
```

### 272: How do you handle CORS without a library?

For simple requests, set `Access-Control-Allow-Origin`. For requests with custom headers or methods like `PUT`, the browser sends a preflight `OPTIONS` request first, and you must answer it with the allowed methods and headers.

```js
const allowed = new Set(["https://app.example.com"]);

app.use((req, res, next) => {
  const origin = req.headers.origin;
  if (origin && allowed.has(origin)) {
    res.setHeader("Access-Control-Allow-Origin", origin);
    res.setHeader("Access-Control-Allow-Credentials", "true");
    res.setHeader("Vary", "Origin");
  }
  if (req.method === "OPTIONS") {
    res.setHeader("Access-Control-Allow-Methods", "GET,POST,PUT,DELETE");
    res.setHeader("Access-Control-Allow-Headers", "Content-Type,Authorization");
    res.setHeader("Access-Control-Max-Age", "600");
    return res.sendStatus(204);
  }
  next();
});
```

Never reflect any origin while also allowing credentials. That lets any site make logged-in requests.

### 273: What is the difference between REST, GraphQL and gRPC?

- **REST**: resources over HTTP with JSON. Simple, cacheable, works everywhere. Can need many requests or return more data than needed.
- **GraphQL**: one endpoint where the client asks for exactly the fields it wants. Good for complex frontends. Harder to cache, and you must protect against very expensive queries. Libraries: Apollo Server, GraphQL Yoga, Mercurius.
- **gRPC**: binary protocol over HTTP/2 using Protocol Buffers and generated clients. Fast with strict contracts. Good for service-to-service calls. Not directly usable from browsers. Library: `@grpc/grpc-js`.

### 274: How do microservices written in Node.js talk to each other?

- **Synchronous**: HTTP/REST, gRPC or GraphQL calls. Simple, but the caller waits and fails if the other service is down. Add timeouts, retries and circuit breakers.
- **Asynchronous**: message brokers and queues like RabbitMQ, Kafka, NATS, Redis Streams, SQS. Services publish events and others consume them. This decouples services and handles traffic spikes, but makes the flow harder to follow and requires handling duplicate messages.

Most systems use both: sync calls for reads that need an answer now, and events for things that can happen later.

### 275: What are message queues and when should you use one?

A message queue stores jobs or events until a consumer processes them. Use one when work can happen later (sending emails, generating reports, resizing images), when you want to smooth out traffic spikes, or when several services need to react to the same event. In Node, BullMQ (on Redis) is popular for job queues. Kafka and RabbitMQ are common for events between services.

```js
import { Queue, Worker } from "bullmq";

const emails = new Queue("emails", { connection });
await emails.add(
  "welcome",
  { userId: 42 },
  { attempts: 3, backoff: { type: "exponential", delay: 1000 } },
);

new Worker(
  "emails",
  async (job) => {
    await sendWelcomeEmail(job.data.userId);
  },
  { connection },
);
```

### 276: What is idempotency and why does it matter for APIs?

An operation is idempotent if doing it several times has the same effect as doing it once. `GET`, `PUT` and `DELETE` should be idempotent. `POST` usually isn't. Networks fail, clients retry and queues deliver messages twice, so you want retries to be safe. A common approach is an idempotency key: the client sends a unique key with the request, the server saves the result under that key and returns the same result for repeats.

```js
app.post("/payments", async (req, res) => {
  const key = req.get("Idempotency-Key");
  if (!key) return res.status(400).json({ error: "Idempotency-Key required" });

  const existing = await store.get(key);
  if (existing) return res.status(existing.status).json(existing.body);

  const payment = await createPayment(req.body);
  await store.set(key, { status: 201, body: payment }, { ttl: 86400 });
  res.status(201).json(payment);
});
```

### 277: How do you version an API?

Common approaches:

- **In the URL**: `/v1/users`, `/v2/users`. Most common and easy to see.
- **In a header**: `Accept: application/vnd.myapp.v2+json` or a custom header.
- **In a query parameter**: `?version=2`.

In Express you can mount separate routers per version. Try to make changes backward compatible (adding fields is fine, removing or renaming isn't) so you rarely need a new version. When you do, keep the old one for a while and announce when it will be removed.

```js
app.use("/v1", v1Router);
app.use("/v2", v2Router);
```

### 278: How do you set up a monorepo for several Node.js packages?

Use workspaces from npm, pnpm or yarn so packages link to each other. Add a task runner like Turborepo or Nx to run builds and tests only for packages that changed, with caching. Share base configs (TypeScript, ESLint) from the root.

```
my-repo/
  package.json        # "workspaces": ["apps/*", "packages/*"]
  apps/
    api/
    web/
  packages/
    db/
    shared-types/
```

```json
// apps/api/package.json
{
  "dependencies": { "@acme/db": "*" }
}
```

pnpm uses `pnpm-workspace.yaml` and the `workspace:*` version syntax.

### 279: How do you publish a package to npm?

```bash
npm login
npm version patch        # bumps version, creates a git tag
npm pack --dry-run       # check which files will be included
npm publish              # add --access public for scoped packages
```

Before publishing, set `name`, `version`, `exports`, `files`, `license`, `repository` and `engines` in `package.json`. Publishing from CI with `npm publish --provenance` (or trusted publishing) links the package to its source repo and build, which helps users trust it. Use `npm deprecate` for bad versions instead of unpublishing.

### 280: What are the limits of Node's built-in TypeScript support?

Type stripping replaces type annotations with spaces and runs the result. Because of that:

- It doesn't check types. Run `tsc --noEmit` in CI or in your editor.
- Syntax that needs real code generation doesn't work by default: `enum`, `namespace` with code, parameter properties in constructors (`constructor(private x: number)`), and legacy decorators. `--experimental-transform-types` handles some of these.
- `tsconfig.json` is ignored, so `paths` aliases don't work. Use `imports` in `package.json` instead.
- Imports must use the real file extension: `import { x } from './utils.ts'`.
- Type-only imports need `import type`, otherwise Node tries to import something that doesn't exist at runtime.
- It doesn't work for `.ts` files inside `node_modules`.

Setting `"erasableSyntaxOnly": true` and `"verbatimModuleSyntax": true` in `tsconfig.json` makes `tsc` warn you about code Node can't run.

```ts
import type { User } from "./types.ts";
import { getUser } from "./db.ts";

const u: User = await getUser(1);
```

### 281: What are the alternatives for running TypeScript in Node.js?

- **Node's type stripping**: built in, no setup, erasable syntax only.
- **tsx**: uses esbuild, supports all TS syntax and `tsconfig` paths, very popular for development.
- **ts-node**: older, can type check while running, slower.
- **Compile first with `tsc`** (or `tsup`, `esbuild`, `swc`) and run the JavaScript output. This is still common for production and libraries, because you ship plain JS and `.d.ts` files.

```bash
node src/index.ts
npx tsx watch src/index.ts
npx tsc && node dist/index.js
```

### 282: How do you deal with dates and time zones on the server?

- Store and send times in UTC (ISO 8601 strings like `2026-03-01T10:00:00Z`, or timestamps).
- Convert to the user's time zone only for display, using `Intl.DateTimeFormat`.
- Set `TZ=UTC` on servers so `new Date()` behaves the same everywhere.
- For date math across time zones and daylight saving time, use a library like `date-fns-tz` or Luxon, or the `Temporal` API where your Node version supports it.

```js
const fmt = new Intl.DateTimeFormat("en-GB", {
  timeZone: "Asia/Tbilisi",
  dateStyle: "medium",
  timeStyle: "short",
});
console.log(fmt.format(new Date()));
```

Node ships with full ICU data, so all locales and time zones work by default.

### 283: What is process.hrtime.bigint() used for?

It returns the current time of a monotonic clock in nanoseconds as a `BigInt`. Monotonic means it never jumps backward when the system clock changes, so it's correct for measuring durations. `Date.now()` can jump when NTP adjusts the clock.

```js
const start = process.hrtime.bigint();
await work();
const ns = process.hrtime.bigint() - start;
console.log(`${Number(ns) / 1e6} ms`);
```

`performance.now()` is also monotonic and is usually enough.

### 284: Why use os.availableParallelism() instead of os.cpus().length?

`os.cpus()` builds an array with details about every CPU, which is wasteful if you only want a count, and it can return an empty array on some systems. `os.availableParallelism()` returns the number of CPUs the process may use, according to libuv. Use it when deciding how many workers or cluster processes to start. In containers, also keep CPU limits in mind, since you may be allowed fewer cores than the machine has.

### 285: What is a Single Executable Application (SEA)?

SEA lets you bundle a Node.js app into a single executable file that includes Node itself, so users don't need to install Node. You write a config, generate a blob with your bundled script, and inject it into a copy of the `node` binary with `postject`.

```json
// sea-config.json
{ "main": "dist/app.js", "output": "sea-prep.blob" }
```

```bash
node --experimental-sea-config sea-config.json
cp $(command -v node) myapp
npx postject myapp NODE_SEA_BLOB sea-prep.blob \
  --sentinel-fuse NODE_SEA_FUSE_fce680ab2cc467b6e072b8b5df1996b2
./myapp
```

The main script must be a single file (bundle your code with esbuild or similar first). On macOS you need to remove and re-add the code signature. Check the docs for your Node version, as the build steps keep getting simpler.

### 286: What is the Node.js permission model?

It lets you limit what a Node process is allowed to do. When you start Node with `--permission`, access to the file system, child processes, worker threads, native addons and WASI is blocked unless you allow it. It is no longer experimental in current versions. It is a safety net against mistakes and some supply chain attacks, not a full sandbox for untrusted code.

```bash
node --permission \
  --allow-fs-read=/app \
  --allow-fs-write=/app/tmp \
  app.js
```

```js
process.permission.has("fs.write", "/etc/passwd"); // false
```

Newer versions also add `--allow-net` to control network access.

### 287: How do the --watch flags work in detail?

`node --watch app.js` watches the entry file and every module it imports, and restarts the process when one changes. `--watch-path` watches specific folders instead (supported on macOS and Windows, and on Linux in newer versions). `--watch-preserve-output` keeps the console from being cleared on restart. Watch mode also works with the test runner (`node --test --watch`).

```bash
node --watch --watch-preserve-output server.js
node --watch-path=./src --watch-path=./views server.js
```

Note that files you read with `fs` (like templates) are not watched unless you use `--watch-path`.

### 288: How does node --run differ from npm run?

`node --run` is faster because it doesn't load npm. It adds `node_modules/.bin` to the PATH and sets a few environment variables, like `npm run` does. But it doesn't run `pre`/`post` scripts, doesn't set all the `npm_package_*` variables, and doesn't support workspaces flags the way npm does. Use it for quick local scripts. Use `npm run` when you rely on npm-specific behavior.

### 289: When should you use fetch, and when the http module or undici directly?

- Use **`fetch`** for most HTTP client work. It's standard, simple and portable.
- Use **`undici` directly** (`undici.request`, `Pool`, `Agent`) when you need the best performance, detailed connection pool control, or features like mocking (`MockAgent`) and interceptors.
- Use **`http.request`** when you need low-level control over sockets, upgrades or unusual protocols, or for very old code.

```js
import { request } from "undici";

const { statusCode, body } = await request("https://api.example.com/items");
const data = await body.json();
```

### 290: How do you process a very large JSON file without loading it all into memory?

`JSON.parse` needs the whole string in memory. For huge files, use a streaming parser like `stream-json`, or better, store data as NDJSON (one JSON object per line) and read it line by line.

```js
import { open } from "node:fs/promises";

const fh = await open("events.ndjson");
let total = 0;
for await (const line of fh.readLines()) {
  if (!line) continue;
  const event = JSON.parse(line);
  total += event.amount;
}
console.log(total);
```

### 291: What is event loop utilization (ELU)?

ELU is the share of time the event loop spent actually running code compared to waiting for I/O. A value close to 1 means the loop is always busy, so new requests have to wait. It's a better signal for autoscaling and load shedding than CPU usage alone.

```js
import { performance } from "node:perf_hooks";

let last = performance.eventLoopUtilization();
setInterval(() => {
  const now = performance.eventLoopUtilization();
  const diff = performance.eventLoopUtilization(now, last);
  console.log("ELU", diff.utilization.toFixed(2));
  last = now;
}, 5000).unref();
```

### 292: How should you design health check endpoints?

Have two kinds:

- **Liveness** (`/livez`): "is the process alive and not stuck?" Keep it cheap and don't check dependencies, or a database outage will make the orchestrator restart every instance.
- **Readiness** (`/readyz`): "can this instance take traffic now?" Check that startup finished and important dependencies are reachable. Return 503 while starting or shutting down.

```js
let ready = false;

app.get("/livez", (req, res) => res.sendStatus(200));
app.get("/readyz", async (req, res) => {
  if (!ready) return res.sendStatus(503);
  try {
    await db.query("SELECT 1");
    res.sendStatus(200);
  } catch {
    res.sendStatus(503);
  }
});

await connectEverything();
ready = true;
process.on("SIGTERM", () => {
  ready = false; /* then shut down */
});
```

### 293: What changes when your Node app runs behind a reverse proxy or load balancer?

The connection comes from the proxy, so `req.socket.remoteAddress` is the proxy's IP, and the protocol may look like HTTP even if the client used HTTPS. The proxy passes the real values in `X-Forwarded-For`, `X-Forwarded-Proto` and `X-Forwarded-Host`. In Express, set `trust proxy` to the right value so `req.ip`, `req.protocol` and secure cookies work. Only trust these headers from your own proxy, because clients can fake them.

```js
app.set("trust proxy", 1); // trust the first proxy in front of the app
app.get("/", (req, res) => res.send(`${req.ip} via ${req.protocol}`));
```

Also match the timeouts (see question 189).

### 294: What are sticky sessions and when do you need them?

Sticky sessions mean the load balancer always sends a given client to the same server. You need them when servers keep per-client state in memory, like in-memory sessions or Socket.IO with long-polling fallback. They make scaling and deploys harder and load less even. It's usually better to keep servers stateless and store state in Redis or a database, so any instance can handle any request.

### 295: How do you implement retries with exponential backoff?

Retry only errors that are likely temporary (timeouts, 502, 503, 429, connection resets), wait longer after each attempt, add random jitter so many clients don't retry at the same moment, and give up after a few tries. Only retry operations that are safe to repeat.

```js
async function withRetry(fn, { retries = 3, base = 200, max = 5000 } = {}) {
  for (let attempt = 0; ; attempt++) {
    try {
      return await fn();
    } catch (err) {
      if (attempt >= retries || !isRetryable(err)) throw err;
      const delay = Math.min(max, base * 2 ** attempt);
      const jitter = Math.random() * delay;
      await new Promise((r) => setTimeout(r, jitter));
    }
  }
}

const isRetryable = (err) =>
  ["ECONNRESET", "ETIMEDOUT", "ECONNREFUSED"].includes(err.code) ||
  [429, 502, 503, 504].includes(err.status);
```

### 296: What is a circuit breaker?

A circuit breaker stops calling a service that keeps failing, so your app doesn't waste time and resources on calls that will fail anyway, and gives the other service time to recover. It has three states:

- **Closed**: calls go through normally. Failures are counted.
- **Open**: after too many failures, calls fail right away without trying.
- **Half-open**: after a cool-down, a few test calls are allowed. If they succeed, it closes again.

In Node, `opossum` is a common library.

```js
import CircuitBreaker from "opossum";

const breaker = new CircuitBreaker(callPaymentService, {
  timeout: 3000,
  errorThresholdPercentage: 50,
  resetTimeout: 30_000,
});
breaker.fallback(() => ({ status: "pending" }));

const result = await breaker.fire(order);
```

### 297: How do you run scheduled jobs (cron) in Node.js?

For simple cases in a single instance, use a library like `node-cron` or `croner`. If you run several instances, every instance would run the job, so use a distributed scheduler: BullMQ repeatable jobs, a database lock, Kubernetes CronJobs, or cloud schedulers that call an endpoint or start a container.

```js
import cron from "node-cron";

cron.schedule(
  "0 3 * * *",
  async () => {
    await cleanupExpiredSessions();
  },
  { timezone: "UTC" },
);
```

### 298: What can and can't you do in a process.on('exit') handler?

The `exit` event runs when the process is about to exit. Only synchronous code works there: the event loop has stopped, so timers, promises and async I/O won't complete. Use it for last sync actions like writing a final line with `fs.writeSync`. Do async cleanup in signal handlers or before you call `process.exit()`.

```js
process.on("exit", (code) => {
  fs.writeSync(1, `exiting with code ${code}\n`);
  setTimeout(() => console.log("never runs"), 0);
});
```

### 299: What is the difference between the beforeExit and exit events?

`beforeExit` fires when the event loop has nothing more to do and the process is about to exit naturally. You can schedule async work there, and if you do, the process keeps running (and `beforeExit` fires again later). It does not fire when you call `process.exit()` or on uncaught exceptions. `exit` always fires at the very end, and only sync code works there.

```js
process.on("beforeExit", async () => {
  if (!flushed) {
    await flushLogs(); // keeps the process alive until done
    flushed = true;
  }
});
```

### 300: How do you handle Ctrl+C correctly in a CLI tool?

Listen for `SIGINT`, stop or cancel the current work, clean up (temp files, cursor state), and exit with code 130, which is the usual code for "terminated by Ctrl+C". If the user presses Ctrl+C a second time, exit right away.

```js
let stopping = false;
const ac = new AbortController();

process.on("SIGINT", () => {
  if (stopping) process.exit(130);
  stopping = true;
  console.error("\nStopping... press Ctrl+C again to force");
  ac.abort();
});

try {
  await runTask({ signal: ac.signal });
} catch (err) {
  if (err.name !== "AbortError") throw err;
  process.exitCode = 130;
} finally {
  await cleanupTempFiles();
}
```

## Advanced Questions

### 301: How does the event loop work inside libuv?

`uv_run()` is a loop that, on each iteration:

1. Updates its cached "now" time.
2. Runs due timers (stored in a min-heap ordered by expiry time).
3. Runs pending callbacks.
4. Runs idle and prepare handles.
5. Computes a poll timeout: zero if there are pending immediates or the loop is stopping, otherwise the time until the nearest timer, or infinite if there are no timers.
6. Blocks in the OS poller (`epoll_wait`, `kevent`, `GetQueuedCompletionStatusEx`) for up to that timeout, then runs I/O callbacks for ready handles.
7. Runs check handles (Node's `setImmediate` queue).
8. Runs close callbacks.

The loop keeps going while there are active and referenced handles (servers, sockets, timers) or requests (pending fs or dns work). Node adds its own layer on top: after each callback that libuv calls into JavaScript, Node drains the `nextTick` queue and the V8 microtask queue.

### 302: Why does network I/O scale well in Node, while file I/O goes to the thread pool?

Sockets can be put into non-blocking mode, and the OS can tell you when one is readable or writable (epoll, kqueue, IOCP). One thread can watch tens of thousands of sockets. Regular files on most systems don't support this kind of readiness notification. A file read always "looks ready" but may block on the disk. So libuv runs file operations as blocking calls on thread pool threads and posts the result back to the loop. That's why many slow file operations at once can fill the 4-thread pool and delay other pool users like `dns.lookup` and `crypto.pbkdf2`. On Linux, libuv can use `io_uring` for some file operations, but it has been turned off by default in recent releases because of security and stability issues, so don't count on it.

### 303: How does V8 execute JavaScript? What are Ignition, Sparkplug, Maglev and TurboFan?

V8 has a tiered pipeline:

1. **Parser** creates an AST. Functions are parsed lazily: only when first called.
2. **Ignition** is the interpreter. It compiles the AST to bytecode and runs it, while collecting type feedback (which shapes and types each operation sees).
3. **Sparkplug** is a fast baseline compiler that turns bytecode into machine code without optimizing. It removes interpreter overhead.
4. **Maglev** is a mid-tier optimizing compiler. It compiles quickly and uses the type feedback for good-enough code.
5. **TurboFan** is the top-tier optimizing compiler for hot code. It makes speculative assumptions based on feedback (for example, "this is always a small integer").

If an assumption breaks at runtime, V8 **deoptimizes**: it drops the optimized code and goes back to bytecode, and may optimize again later with new feedback.

### 304: What are hidden classes and inline caches?

V8 gives every object a hidden class (called a "map" or "shape") that describes its properties and their order in memory. Objects created the same way share the same hidden class. When code accesses `obj.x`, V8 remembers (caches) where `x` was for that hidden class. This is an inline cache. If the same code always sees one shape, it's **monomorphic** and very fast. A few shapes is **polymorphic**. Many shapes (more than 4) is **megamorphic**, and V8 falls back to a slower generic lookup.

```js
// same shape, fast
function Point(x, y) {
  this.x = x;
  this.y = y;
}

// different shapes for the same "kind" of object, slower
const a = { x: 1, y: 2 };
const b = { y: 2, x: 1 }; // different order -> different hidden class
const c = { x: 1 };
c.y = 2; // added later -> different transition path
```

Tips: initialize all fields in the constructor, in the same order, and avoid `delete obj.prop` on hot objects (set it to `undefined` instead).

### 305: What causes V8 to deoptimize a function?

- Types change: a function optimized for numbers suddenly gets strings.
- Object shapes change, or a site that was monomorphic now sees new shapes.
- Arrays change elements kind (for example from integers to doubles, or from packed to holey).
- Reading out of bounds of an array.
- Integer overflow from small integers (Smi) into heap numbers.
- Changing prototypes of objects used in hot code.

You can see this with flags:

```bash
node --trace-opt --trace-deopt app.js | grep -i myFunction
```

In practice you rarely need this. Profile first, and only look at deopts in the hot functions the profile shows.

### 306: How is the V8 heap organized?

- **New space (young generation)**: small (a few MB to tens of MB), split into two semi-spaces. New objects go here.
- **Old space**: objects that survived two scavenges in new space get promoted here.
- **Large object space**: objects bigger than a threshold are put here directly and never moved.
- **Code space**: compiled machine code.
- **Read-only space** and other smaller spaces for internal objects.

`v8.getHeapSpaceStatistics()` shows the size of each space.

```js
import v8 from "node:v8";
console.table(
  v8.getHeapSpaceStatistics().map((s) => ({
    space: s.space_name,
    usedMB: (s.space_used_size / 1e6).toFixed(1),
  })),
);
```

Buffers and ArrayBuffer backing stores are not in the V8 heap. They are counted as external memory.

### 307: How does garbage collection work in V8 (Orinoco)?

- **Minor GC (Scavenger)**: cleans the young generation often. It copies live objects from one semi-space to the other (or promotes them to old space) and frees the rest in one go. Most objects die young, so this is cheap. It runs in parallel on several threads but still pauses JavaScript briefly.
- **Major GC (Mark-Compact)**: cleans the whole heap. It marks all reachable objects starting from roots, sweeps dead ones and compacts fragmented pages. Most marking is **concurrent** (on background threads while JS runs) and **incremental** (in small steps), and sweeping is concurrent too, so pauses are short.

Write barriers track pointers from old to new objects so the scavenger doesn't have to scan the entire old space. You can watch GC with `--trace-gc` or with `PerformanceObserver` and the `gc` entry type.

### 308: How do you control V8 heap size, and what do you need to know about containers?

The old space limit is set by `--max-old-space-size` (in MB). If the heap gets close to this limit, GC runs more and more often, and if it can't free enough memory, the process crashes with "JavaScript heap out of memory". By default V8 picks a limit based on the machine's memory. Inside a container with a memory limit, set the heap limit yourself so it sits below the container limit, leaving room for Buffers, native memory and the stack, or the container gets OOM-killed before V8 notices.

```bash
node --max-old-space-size=1536 server.js        # container limit 2 GB
NODE_OPTIONS="--max-old-space-size=1536" npm start
node --max-semi-space-size=64 server.js         # bigger young generation, fewer scavenges
```

Newer versions also let you set the heap as a percentage of available memory with `--max-old-space-size-percentage`. Check that your version has it. `v8.getHeapStatistics().heap_size_limit` shows the current limit.

### 309: How do you take a heap snapshot, including in production?

```js
import v8 from "node:v8";
const file = v8.writeHeapSnapshot(); // writes Heap.<date>.heapsnapshot
```

```bash
node --heapsnapshot-signal=SIGUSR2 server.js
kill -USR2 <pid>

node --heapsnapshot-near-heap-limit=2 server.js   # writes up to 2 snapshots just before OOM
```

You can also take one from Chrome DevTools' Memory tab when attached with `--inspect`. Taking a snapshot stops the process and can need about as much memory again as the heap itself, so be careful on loaded production servers. Take it from one instance that's out of the load balancer if you can.

### 310: How do you find a memory leak step by step?

1. **Confirm it**: watch `heapUsed` and `rss` over time under steady load. A leak keeps growing even after major GCs.
2. **Find out if it's JS heap or native**: if `heapUsed` grows, it's JS objects. If `rss` grows but heap doesn't, look at Buffers (`arrayBuffers`, `external`) or native addons.
3. **Take three heap snapshots**: after warm-up, after some load, after more load.
4. **Compare them** in DevTools ("Comparison" view). Sort by "# Delta" or "Size Delta" to see which objects keep increasing.
5. **Look at retainers**: for a leaking object, the "Retainers" panel shows the chain of references keeping it alive, often ending in a module-level `Map`, an event listener, a closure or a timer.
6. **Fix and verify** with the same test.

Tools like `clinic heapprofiler` or `--heap-prof` (sampling heap profiler) help when snapshots are too big.

### 311: What are WeakRef and FinalizationRegistry, and should you use them?

`WeakRef` holds a reference to an object without stopping it from being garbage collected. `deref()` returns the object or `undefined` if it was collected. `FinalizationRegistry` lets you register a callback that may run some time after an object is collected.

```js
const cache = new Map();
const registry = new FinalizationRegistry((key) => {
  if (!cache.get(key)?.deref()) cache.delete(key);
});

function setCached(key, value) {
  cache.set(key, new WeakRef(value));
  registry.register(value, key);
}

function getCached(key) {
  return cache.get(key)?.deref();
}
```

Use them rarely. GC timing is unpredictable, finalizers may never run, and behavior can differ between engines. Never use them for important cleanup like closing files. Use explicit `close()` or `using` for that.

### 312: When is a WeakMap a good choice?

A `WeakMap` uses objects as keys and doesn't keep them alive. When a key object is collected, its entry disappears. It's good for attaching extra data to objects you don't own (like a request object or a DOM-like node), without leaking memory when those objects go away. You can't iterate it or get its size.

```js
const meta = new WeakMap();

function track(req) {
  meta.set(req, { start: performance.now() });
}

function duration(req) {
  return performance.now() - meta.get(req).start;
}
```

### 313: How do you CPU-profile a Node.js app and read a flame graph?

```bash
node --cpu-prof --cpu-prof-dir=./prof server.js
# run load, stop the server, open the .cpuprofile in Chrome DevTools or speedscope

npx 0x server.js            # creates a flame graph
npx clinic flame -- node server.js
```

In a flame graph, the x-axis is total time (not timeline order), the y-axis is call stack depth, and wider boxes mean more time on CPU. Look for wide boxes near the top ("plateaus"): those are functions where the CPU actually spends time. Typical findings: JSON serialization, regex, logging, sync crypto, template rendering, deep object cloning.

### 314: What are --prof and --prof-process?

`--prof` uses V8's built-in sampling profiler and writes a `isolate-*.log` file with ticks for JS and native (C++) code. `--prof-process` turns the log into a readable summary showing where time was spent, including time in GC and inside Node's C++ code, which `--cpu-prof` shows less clearly.

```bash
node --prof app.js
node --prof-process isolate-0x*.log > profile.txt
```

`--cpu-prof` is easier to use for most JavaScript problems. `--prof` is useful when time goes to native code.

### 315: What is a diagnostic report?

A diagnostic report is a JSON file with a lot of information about the process at one moment: JS and native stack traces, heap stats, libuv handles, environment, loaded shared libraries, resource usage and more. It's very useful for crashes and hangs in production.

```bash
node --report-on-fatalerror --report-uncaught-exception \
     --report-on-signal --report-signal=SIGUSR2 \
     --report-directory=/var/log/node server.js
```

```js
process.report.writeReport(); // write one now
const report = process.report.getReport(); // as an object
console.log(report.header.nodejsVersion, report.libuv.length);
```

### 316: What are async_hooks, and why are they discouraged?

`async_hooks.createHook()` lets you get callbacks (`init`, `before`, `after`, `destroy`, `promiseResolve`) for every async resource created in the process. It was the basis for tracking async context. The Node docs discourage it now: it has a noticeable performance cost (especially for promises), the API is hard to use correctly, and it exposes internals that may change. Use `AsyncLocalStorage` for context, and `diagnostics_channel` for tracing. `executionAsyncId()` and `triggerAsyncId()` are still sometimes useful for debugging.

### 317: How does AsyncLocalStorage work internally, and what changed in Node 24?

Before Node 24, `AsyncLocalStorage` was built on async_hooks: each new async resource copied the current store from the resource that created it. Since Node 24, it's built on `AsyncContextFrame` by default, which uses V8's support for keeping a "continuation preserved embedder data" slot with every promise reaction and callback. The current context is stored as an immutable map and captured automatically when async work is scheduled, so there are no hooks running on every resource. It's faster and behaves more like the upcoming `AsyncContext` proposal for JavaScript.

A few edge cases changed: for example the context seen inside some event emitter callbacks or after `unhandledRejection` can differ. If you hit them, `--no-async-context-frame` brings back the old implementation.

```js
const als = new AsyncLocalStorage();

als.run({ id: 1 }, async () => {
  await null;
  setTimeout(() => console.log(als.getStore()), 10); // { id: 1 }
});

// bind a callback to the current context
const bound = AsyncLocalStorage.bind(() => als.getStore());

// snapshot and restore context later
const snapshot = AsyncLocalStorage.snapshot();
```

### 318: What are tracing channels in diagnostics_channel?

`diagnostics_channel.tracingChannel(name)` creates a set of channels (`start`, `end`, `asyncStart`, `asyncEnd`, `error`) for one operation. Libraries use it to describe operations, and APM tools subscribe to build spans with correct timing and errors, without monkey patching. Node uses it internally for `http`, `fetch` (undici) and module loading.

```js
import dc from "node:diagnostics_channel";

const queryChannel = dc.tracingChannel("mydb:query");

export function query(sql) {
  return queryChannel.tracePromise(async () => runQuery(sql), { sql });
}

// in a tracing tool
queryChannel.subscribe({
  start(ctx) {
    ctx.startTime = performance.now();
  },
  asyncEnd(ctx) {
    console.log(ctx.sql, performance.now() - ctx.startTime);
  },
  error(ctx) {
    console.error("query failed", ctx.error);
  },
});
```

### 319: How does OpenTelemetry instrument a Node app, and why does --import matter?

OpenTelemetry's Node SDK creates spans and metrics for HTTP, databases and other libraries automatically. Many instrumentations work by patching modules when they load, so the SDK must start **before** your app imports those modules. In ESM, that means using a preload with `--import` and a loader hook (`module.register`) so `import` statements can be intercepted. Newer instrumentations use `diagnostics_channel`, which doesn't need patching.

```js
// instrumentation.mjs
import { NodeSDK } from "@opentelemetry/sdk-node";
import { getNodeAutoInstrumentations } from "@opentelemetry/auto-instrumentations-node";

new NodeSDK({ instrumentations: [getNodeAutoInstrumentations()] }).start();
```

```bash
node --import ./instrumentation.mjs server.js
```

### 320: What are module customization hooks?

They let you change how Node resolves and loads modules: transpile files on the fly, load from a different source, mock modules in tests, or add instrumentation. There are two APIs:

- **`module.register(url)`**: async hooks (`resolve`, `load`) that run in a separate loader thread. They work for ESM and for CommonJS when loaded through ESM.
- **`module.registerHooks({ resolve, load })`**: synchronous hooks that run in the main thread (added in Node 22.15 / 23.5). They also apply to `require()` and are simpler, so they are now the recommended choice for most cases.

```js
// register-yaml.mjs
import { registerHooks } from "node:module";
import { readFileSync } from "node:fs";
import { fileURLToPath } from "node:url";
import YAML from "yaml";

registerHooks({
  load(url, context, nextLoad) {
    if (url.endsWith(".yaml")) {
      const text = readFileSync(fileURLToPath(url), "utf8");
      return {
        format: "module",
        source: `export default ${JSON.stringify(YAML.parse(text))};`,
        shortCircuit: true,
      };
    }
    return nextLoad(url, context);
  },
});
```

```bash
node --import ./register-yaml.mjs app.js
```

### 321: What is the difference between --import and --require?

`--require` (`-r`) preloads a CommonJS module before the main entry. `--import` preloads an ES module, and it can use top-level await and register module hooks. Both run before your main file. Use `--import` for ESM projects and for anything that needs to hook `import`. Both can be put in `NODE_OPTIONS`.

```bash
node --require dotenv/config server.cjs
node --import ./telemetry.mjs --import ./hooks.mjs server.mjs
```

### 322: How does loading an ES module work under the hood?

ESM loading has three phases:

1. **Construction**: Node resolves each specifier to a URL, fetches the source and parses it to find `import` statements, then does the same for each dependency. This builds a module graph. No code runs yet.
2. **Instantiation (linking)**: for each module, memory slots are created for exports, and imports are connected to the exporting module's slots (live bindings). Missing named exports are reported here, as a `SyntaxError`, before anything runs.
3. **Evaluation**: modules run in post-order (dependencies first). Modules with top-level await make their parents wait.

Because imports must be known before running, `import` statements must be static and at the top level. Dynamic `import()` starts a new graph load at runtime.

### 323: What are live bindings in ESM?

An imported name is a live, read-only view of the exporting module's variable, not a copy. If the exporting module changes the variable, importers see the new value. Importers can't assign to it. In CommonJS, destructuring `require()` copies the value at that moment.

```js
// counter.mjs
export let count = 0;
export function inc() {
  count++;
}

// main.mjs
import { count, inc } from "./counter.mjs";
console.log(count); // 0
inc();
console.log(count); // 1
// count = 5;       // TypeError: Assignment to constant variable
```

### 324: How does Node let you import named exports from a CommonJS module?

When ESM imports a CommonJS file, Node can't know the exports until the file runs, but ESM needs export names during linking. So Node uses a static analyzer (`cjs-module-lexer`) that scans the source for patterns like `exports.foo = ...`, `module.exports = { foo }` and some re-export forms. Names it detects become named exports. Anything else is only available through the default export, which is always `module.exports`.

```js
// lib.cjs
exports.a = 1;
module.exports.b = 2;
const c = 3;
Object.assign(module.exports, { c }); // not detected

// app.mjs
import lib, { a, b } from "./lib.cjs";
console.log(a, b, lib.c);
// import { c } from './lib.cjs';  // SyntaxError: not detected
```

In the other direction (`require(esm)`), a module can export a name `'module.exports'` to control exactly what `require()` returns:

```js
// esm-lib.mjs
export default class Foo {}
export { Foo as "module.exports" };
```

### 325: What are the limits of require(esm)?

- The ES module graph must be fully synchronous. If any module in it uses top-level `await`, you get `ERR_REQUIRE_ASYNC_MODULE`. Use `import()` there.
- `require()` returns the namespace object, so the default export is at `.default`, unless the module exports `'module.exports'`.
- If the ESM graph is already being loaded by `import` and you `require` it in the middle (cycles), you can get `ERR_REQUIRE_CYCLE_MODULE`.
- Some tools and loaders that patch `require` may not see ESM loaded this way.
- Using it from very old Node versions (before 20.19 / 22.12) needs `--experimental-require-module`.

`process.features.require_module` tells you whether it is available.

### 326: How do custom export conditions work, and what conditions does Node know?

Node always checks `node`, `import` or `require` (depending on how the file is loaded), `module-sync` (for ESM that is safe to `require`), `node-addons`, and `default`. You can add your own with `--conditions` (`-C`). Tools like bundlers and TypeScript also understand conditions like `types`, `browser`, `development` and `production`. Conditions are checked in the order they're written in `package.json`, and the first match wins, even if a later one is more specific.

```json
{
  "exports": {
    ".": {
      "development": "./src/index.ts",
      "module-sync": "./dist/index.mjs",
      "require": "./dist/index.cjs",
      "default": "./dist/index.mjs"
    }
  }
}
```

```bash
node -C development app.js
```

### 327: How do you write a native addon, and what is Node-API?

Native addons are shared libraries (`.node` files) written in C or C++ (or Rust through `napi-rs`) that Node loads with `require`. **Node-API (N-API)** is a stable C API for writing them. Its ABI doesn't change between Node versions, so one compiled binary works on many Node releases. `node-addon-api` is a C++ wrapper on top of it. The older approach of using V8 and NAN directly breaks with every V8 update.

```cpp
// hello.cc
#include <napi.h>

Napi::String Hello(const Napi::CallbackInfo& info) {
  return Napi::String::New(info.Env(), "world");
}

Napi::Object Init(Napi::Env env, Napi::Object exports) {
  exports.Set("hello", Napi::Function::New(env, Hello));
  return exports;
}

NODE_API_MODULE(hello, Init)
```

```js
const addon = require("./build/Release/hello.node");
console.log(addon.hello()); // 'world'
```

Use addons for existing C/C++ libraries or very heavy computation. For most other cases, WebAssembly is easier to ship.

### 328: How do you use WebAssembly and WASI in Node.js?

WebAssembly modules run at near native speed in a sandbox, and the same `.wasm` file works on all platforms, so you don't need to compile per OS like native addons. Load them with the global `WebAssembly` API. WASI (`node:wasi`) gives a WASM module limited access to things like files and environment, but it is still experimental in Node.

```js
import { readFile } from "node:fs/promises";

const bytes = await readFile(new URL("./add.wasm", import.meta.url));
const { instance } = await WebAssembly.instantiate(bytes);
console.log(instance.exports.add(2, 3));
```

Many npm packages (image codecs, parsers, `esbuild-wasm`, SQLite builds) ship WASM for portability. Crossing the JS/WASM boundary has a cost, so pass data in larger batches.

### 329: How are worker threads implemented, and what are resourceLimits?

Each worker is a real OS thread with its own V8 isolate, its own heap, its own event loop and its own copy of Node's built-in modules. They share the process's libuv thread pool and native memory. Communication goes through `MessagePort`s, which serialize data with the structured clone algorithm. Because of the separate isolate, starting a worker costs time and memory (around a few MB), and objects can't be shared, only copied, transferred or put in `SharedArrayBuffer`.

`resourceLimits` sets heap and stack limits per worker, so one runaway task can't use all the memory. If a worker hits its limit, only that worker is terminated with `ERR_WORKER_OUT_OF_MEMORY`.

```js
const worker = new Worker("./task.js", {
  resourceLimits: {
    maxOldGenerationSizeMb: 256,
    maxYoungGenerationSizeMb: 32,
    stackSizeMb: 4,
  },
});
worker.on("error", (err) => console.error(err.code));
```

### 330: What are MessageChannel and BroadcastChannel used for?

`MessageChannel` creates a pair of connected ports. You can transfer one port to a worker so two workers can talk directly, without going through the main thread. `BroadcastChannel` sends a message to every thread that opened a channel with the same name.

```js
import { Worker, MessageChannel, BroadcastChannel } from "node:worker_threads";

const { port1, port2 } = new MessageChannel();
const a = new Worker("./a.js");
const b = new Worker("./b.js");
a.postMessage({ port: port1 }, [port1]);
b.postMessage({ port: port2 }, [port2]);

// anywhere, in any thread
const bc = new BroadcastChannel("config");
bc.postMessage({ reload: true });
bc.onmessage = (e) => console.log("got", e.data);
```

### 331: How can you implement a mutex between worker threads with Atomics?

Use a shared `Int32Array` slot as a lock: `0` means free, `1` means taken. `Atomics.compareExchange` takes the lock atomically, `Atomics.wait` sleeps while it's taken, and `Atomics.notify` wakes one waiter on unlock. `Atomics.wait` blocks the thread, so don't use it on the main thread. Newer runtimes have `Atomics.waitAsync` for that case.

```js
export class Mutex {
  constructor(sab, index = 0) {
    this.lock = new Int32Array(sab);
    this.i = index;
  }
  acquire() {
    while (Atomics.compareExchange(this.lock, this.i, 0, 1) !== 0) {
      Atomics.wait(this.lock, this.i, 1);
    }
  }
  release() {
    Atomics.store(this.lock, this.i, 0);
    Atomics.notify(this.lock, this.i, 1);
  }
}
```

### 332: How can the libuv thread pool become a bottleneck, and how do you fix it?

All of these share the same 4 threads: async `fs`, `dns.lookup`, async `crypto` (`pbkdf2`, `scrypt`, `randomFill`), async `zlib`, and some addons. A burst of slow work (password hashing during a login spike, many file reads from a slow network disk, gzip of big responses) fills the pool. Then everything else that needs it waits, including `dns.lookup` behind every new outgoing HTTP connection. Requests look slow, but CPU and event loop delay look fine.

Fixes:

- Increase `UV_THREADPOOL_SIZE` (set before startup, for example 16 to 64).
- Use `dns.resolve*` or a DNS cache for outgoing connections, and keep-alive so you resolve less.
- Move CPU work like hashing to a worker pool.
- Use streaming instead of many small file operations, and avoid `fs` calls per request (cache file contents).

### 333: What is the difference between dns.lookup and dns.resolve, and why does it matter?

`dns.lookup()` calls the OS's `getaddrinfo`, which uses `/etc/hosts`, `nsswitch` and system DNS settings, the same as other programs. But `getaddrinfo` is blocking, so libuv runs it on the thread pool. `dns.resolve*()` uses the c-ares library, which talks to DNS servers directly over the network, asynchronously, without the thread pool, but ignores `/etc/hosts` and some system settings. `http`, `net` and `fetch` use `lookup` by default. You can pass a custom `lookup` function to `http.Agent` or use a caching library like `cacheable-lookup`.

Another thing: by default `dns.lookup` returns addresses in the order the resolver gave them (`verbatim`). If IPv6 is listed first but not reachable, connections can fail. Node's "happy eyeballs" (`autoSelectFamily`, on by default since Node 20) tries IPv4 and IPv6 in parallel to avoid this.

### 334: Why might you see random 502 errors behind a load balancer, and how do you fix them?

A common cause is a keep-alive timeout race. The load balancer keeps idle connections to Node open for, say, 60 seconds. Node's `server.keepAliveTimeout` is 5 seconds by default, so Node closes the idle connection first. If the load balancer sends a new request on that connection at the same moment Node closes it, the request fails and the LB returns 502.

Fix: make Node's keep-alive timeout longer than the LB's idle timeout, and `headersTimeout` a bit longer than that.

```js
server.keepAliveTimeout = 65_000; // LB idle timeout is 60s
server.headersTimeout = 66_000;
```

Other causes are the process crashing, the event loop being blocked longer than the LB's timeout, and closing connections during deploys without draining first.

### 335: What is undici's dispatcher, and how do you configure fetch globally?

Undici is the HTTP/1.1 client behind Node's `fetch`. A dispatcher decides how requests are sent: `Agent` (pools per origin), `Pool` (many connections to one origin), `Client` (one connection), `ProxyAgent`, `RetryAgent` and `MockAgent` for tests. You can set a global dispatcher or pass one per request. To use these APIs you install the `undici` package from npm. Its version may not match the one bundled in Node, so check compatibility.

```js
import { Agent, setGlobalDispatcher, ProxyAgent, MockAgent } from "undici";

setGlobalDispatcher(
  new Agent({
    connections: 100,
    keepAliveTimeout: 30_000,
    connect: { timeout: 5_000 },
  }),
);

await fetch("https://api.example.com", {
  dispatcher: new ProxyAgent("http://proxy.internal:8080"),
});

// tests
const mock = new MockAgent();
mock.disableNetConnect();
mock
  .get("https://api.example.com")
  .intercept({ path: "/users" })
  .reply(200, []);
setGlobalDispatcher(mock);
```

Newer Node versions also support standard proxy environment variables (`HTTP_PROXY`, `HTTPS_PROXY`, `NO_PROXY`) for `fetch` and the `http` modules when you start Node with `--use-env-proxy` or set `NODE_USE_ENV_PROXY=1`.

### 336: How do HTTP/2 streams and flow control work in Node?

In HTTP/2, one TCP connection carries many streams. Each request/response pair is a stream with an ID, and frames from different streams are interleaved. Each stream and the whole connection have flow control windows. A sender can only send as many bytes as the receiver's window allows, and the receiver sends `WINDOW_UPDATE` frames to allow more. In Node, each `Http2Stream` is a Duplex stream, so normal stream backpressure maps onto HTTP/2 flow control. Settings like `maxConcurrentStreams` and `initialWindowSize` limit resources. Server push is deprecated by browsers, so don't build on it. Watch out for attack patterns like "rapid reset" (CVE-2023-44487), which Node has patched. Keep Node updated.

### 337: What do SNI, ALPN and TLS session resumption do?

- **SNI** (Server Name Indication): the client sends the hostname in the TLS handshake, so one server/IP can present different certificates for different domains. In Node use `SNICallback` or `server.addContext()`.
- **ALPN**: the client and server agree on the application protocol during the handshake, for example `h2` or `http/1.1`. `http2.createSecureServer` with `allowHTTP1` uses it.
- **Session resumption**: lets a client reuse earlier TLS session state (session tickets or session IDs) to skip a full handshake. This saves CPU and a round trip. Node's `https.Agent` caches sessions per host by default.

```js
const server = tls.createServer({
  SNICallback(servername, cb) {
    cb(null, contexts.get(servername) ?? defaultContext);
  },
  ALPNProtocols: ["h2", "http/1.1"],
});
```

### 338: How do Readable streams work internally?

A readable stream has an internal buffer (`readableState.buffer`) and a `highWaterMark`. When the buffered size is below the mark, the stream calls `_read(size)`. Your implementation calls `this.push(chunk)` one or more times. `push()` returns `false` when the buffer is at or above the mark, which means "stop producing until `_read` is called again". `push(null)` signals the end. In flowing mode, the stream emits `'data'` for each chunk and keeps calling `_read`. If a consumer (like `pipe`) sees that `write()` returned `false`, it pauses the readable until the writable emits `'drain'`.

```js
class DbCursorStream extends Readable {
  constructor(cursor) {
    super({ objectMode: true, highWaterMark: 100 });
    this.cursor = cursor;
  }
  async _read() {
    try {
      const rows = await this.cursor.next(100);
      if (rows.length === 0) return this.push(null);
      for (const row of rows) {
        if (!this.push(row)) break; // _read will be called again later
      }
    } catch (err) {
      this.destroy(err);
    }
  }
  async _destroy(err, cb) {
    await this.cursor.close().catch(() => {});
    cb(err);
  }
}
```

### 339: How should you handle errors and cleanup in streams?

- Always use `pipeline()` (or `compose`) to connect streams, so an error in any stream destroys all of them.
- Implement `_destroy(err, callback)` in custom streams to release resources (file handles, DB cursors). It's called on errors, `destroy()` and normal completion with `autoDestroy` (on by default).
- Call `this.destroy(err)` (or pass the error to the callback) instead of emitting `'error'` yourself.
- Use `stream.finished()` to know when a stream is done, errored or closed early (for example `ERR_STREAM_PREMATURE_CLOSE` when an HTTP client disconnects).
- Pass an `AbortSignal` to `pipeline` to cancel the whole chain.

```js
const ac = new AbortController();
req.on("close", () => ac.abort());

await pipeline(source, transform, res, { signal: ac.signal });
```

### 340: How do you write a lot of data to a stream manually without blowing up memory?

Respect the return value of `write()` and wait for `'drain'`. Also handle errors and wait for `'finish'` at the end.

```js
import { once } from "node:events";
import { createWriteStream } from "node:fs";
import { finished } from "node:stream/promises";

async function writeRows(path, rows) {
  const out = createWriteStream(path);
  for (const row of rows) {
    if (!out.write(JSON.stringify(row) + "\n")) {
      await once(out, "drain");
    }
  }
  out.end();
  await finished(out);
}
```

If you ignore `false` and keep writing, the data still goes into the stream's internal buffer, which can grow until the process runs out of memory.

### 341: How do async generators work with pipeline?

`pipeline()` accepts async generator functions as steps. Each one gets the previous stream as an async iterable and yields values for the next step. This is often simpler than writing a Transform class, and backpressure still works because the generator only runs when the next step asks for data.

```js
import { pipeline } from "node:stream/promises";
import { createReadStream, createWriteStream } from "node:fs";
import { createGunzip } from "node:zlib";
import split2 from "split2";

await pipeline(
  createReadStream("events.ndjson.gz"),
  createGunzip(),
  split2(),
  async function* (lines) {
    for await (const line of lines) {
      const e = JSON.parse(line);
      if (e.type === "purchase") yield `${e.userId},${e.amount}\n`;
    }
  },
  createWriteStream("purchases.csv"),
);
```

### 342: What are stream operators like map and filter, and how does compose work?

Readable streams have helper methods that return new streams: `map`, `filter`, `flatMap`, `take`, `drop`, `forEach`, `reduce`, `toArray`, `some`, `find`, `every`. `map` and others accept a `concurrency` option, so you can process several items in parallel while keeping backpressure. They are still marked experimental in the docs. `stream.compose()` combines several streams or generator functions into one Duplex that you can reuse.

```js
import { Readable, compose } from "node:stream";

const ids = Readable.from(userIds);

const users = await ids
  .map(async (id) => fetchUser(id), { concurrency: 5 })
  .filter((u) => u.active)
  .toArray();

const csvToJson = compose(splitLines, async function* (src) {
  for await (const line of src) yield JSON.stringify(line.split(",")) + "\n";
});
```

### 343: How does Node's Buffer pool work, and what is allocUnsafeSlow?

For small allocations (less than half of `Buffer.poolSize`, which is 8 KB by default), `Buffer.allocUnsafe()` and `Buffer.from()` take a slice of a shared, preallocated 8 KB `ArrayBuffer` instead of allocating a new one. This makes many small allocations fast. The side effect is that a tiny Buffer can keep the whole 8 KB chunk alive, and `buf.buffer` points to the shared pool, so `buf.buffer.byteLength` isn't your data's length. Always use `byteOffset` and `byteLength` when you pass `buf.buffer` somewhere.

`Buffer.allocUnsafeSlow()` always allocates its own memory, outside the pool. Use it when you plan to keep a small buffer for a long time, so it doesn't keep a pool chunk alive.

```js
const small = Buffer.from("hi");
small.buffer.byteLength; // 8192 (the pool)
new Uint8Array(small.buffer, small.byteOffset, small.byteLength); // correct view
```

### 344: Why is Buffer.slice deprecated, and what should you use?

`Buffer.prototype.slice` returns a view that shares memory with the original buffer, while `Uint8Array.prototype.slice` (and `Array.prototype.slice`) return a copy. Since `Buffer` extends `Uint8Array`, the same method name doing different things caused bugs. Use `subarray()` when you want a view (no copy), and `Buffer.from(buf.subarray(...))` or `Uint8Array.prototype.slice.call(buf, ...)` when you want a copy.

```js
const buf = Buffer.from("hello");
const view = buf.subarray(0, 2);
view[0] = 0x4a; // 'J'
buf.toString(); // 'Jello' - shared memory

const copy = Buffer.from(buf.subarray(0, 2));
```

### 345: What encoding problems can you run into with Buffers and strings?

- **Split multi-byte characters** across chunks (use `setEncoding` or `StringDecoder`, see question 179).
- **Invalid UTF-8** bytes are silently replaced with `U+FFFD` (�) when converting to a string. Use `buffer.isUtf8()` to check, or `new TextDecoder('utf-8', { fatal: true })` to throw.
- **`latin1` / `binary`** maps each byte to one character, which is useful for raw bytes but breaks real text.
- **`string.length` vs byte length** (question 177).
- **BOM** at the start of UTF-8 files from Windows tools (`﻿`), which can break `JSON.parse`.
- **Unicode normalization**: `'é'` can be one code point or two. Use `str.normalize('NFC')` before comparing or hashing user input.

```js
import { isUtf8 } from "node:buffer";
isUtf8(Buffer.from([0xff, 0xfe])); // false
```

### 346: Why is running Node as PID 1 in Docker a problem?

PID 1 in a Linux container has special rules: the kernel doesn't apply default signal handlers to it, so if your app doesn't handle `SIGTERM`, it ignores it and Docker has to `SIGKILL` it after the timeout. PID 1 is also responsible for reaping zombie child processes. Node doesn't reap children it didn't start through `child_process`. And if you start with `npm start`, npm becomes PID 1 and may not forward signals to Node.

Fixes:

- Run `node` directly in `CMD` (exec form, not shell form).
- Handle `SIGTERM` and `SIGINT` in your app.
- Use `docker run --init` or `tini` as PID 1 if you spawn child processes.

```dockerfile
ENTRYPOINT ["/usr/bin/tini", "--"]
CMD ["node", "server.js"]
```

### 347: How do you do a zero-downtime graceful shutdown in Kubernetes?

When a pod is deleted, Kubernetes sends `SIGTERM` and at the same time starts removing the pod from Service endpoints. These two things happen in parallel, so for a few seconds new requests can still arrive after `SIGTERM`. A good sequence:

1. On `SIGTERM`, mark the app as not ready (`/readyz` returns 503), but keep serving.
2. Wait a few seconds (or use a `preStop` hook with `sleep`) so the endpoint removal reaches all proxies.
3. Call `server.close()` to stop accepting connections, and `server.closeIdleConnections()`.
4. Wait for in-flight requests, then close DB pools, queues, telemetry exporters.
5. Exit before `terminationGracePeriodSeconds` (default 30s), with a forced exit as a safety net.

```js
process.on("SIGTERM", async () => {
  ready = false;
  await setTimeout(5000); // from timers/promises
  server.close();
  server.closeIdleConnections();
  const force = global.setTimeout(() => server.closeAllConnections(), 15_000);
  force.unref();
  await once(server, "close");
  await Promise.allSettled([db.end(), queue.close(), otel.shutdown()]);
  process.exit(0);
});
```

### 348: How can you reload a clustered app without downtime?

Restart workers one at a time: start a new worker, wait until it's listening, then tell an old worker to disconnect (stop taking new connections and finish current ones), then move to the next. There is always at least one worker serving. PM2's `pm2 reload` does this for you.

```js
async function rollingRestart() {
  for (const old of Object.values(cluster.workers)) {
    const fresh = cluster.fork();
    await once(fresh, "listening");
    old.disconnect();
    await once(old, "exit");
  }
}

process.on("SIGHUP", rollingRestart);
```

In Kubernetes, rolling deployments with readiness probes and graceful shutdown give you the same result at the pod level.

### 349: What do you need to consider when scaling Node.js horizontally?

- **Stateless instances**: no sessions, uploads, or caches that only one instance knows about. Use Redis, a database or object storage.
- **WebSockets and SSE**: connections live on one instance, so use pub/sub (Redis, NATS) to deliver messages to clients on other instances.
- **Scheduled jobs**: make sure only one instance runs each job (locks or a separate worker).
- **Database connections**: total connections = pool size × instances. Use a pooler like PgBouncer if needed.
- **Rate limits and idempotency keys** must be stored in a shared place.
- **Config and deploys**: all instances should have the same version and config, and the app should tolerate old and new versions running side by side during a rollout.

### 350: How would you monitor event loop health in production and act on it?

Collect event loop delay (p50, p99, max) with `monitorEventLoopDelay`, event loop utilization, heap usage, GC pause times and active handles, and export them as metrics (for example with `prom-client`, which has default Node metrics). Alert when p99 delay or ELU stays high. In the app itself you can do load shedding: when the loop is overloaded, reject new requests early with 503 instead of letting all requests become slow. `@fastify/under-pressure` does this.

```js
import { monitorEventLoopDelay, performance } from "node:perf_hooks";

const h = monitorEventLoopDelay();
h.enable();
let elu = performance.eventLoopUtilization();

app.use((req, res, next) => {
  const now = performance.eventLoopUtilization(elu);
  if (h.percentile(99) / 1e6 > 200 || now.utilization > 0.98) {
    res.setHeader("Retry-After", "1");
    return res.sendStatus(503);
  }
  next();
});

setInterval(() => {
  h.reset();
  elu = performance.eventLoopUtilization();
}, 5000).unref();
```

### 351: How do you use PerformanceObserver and the perf_hooks histogram?

`PerformanceObserver` lets you subscribe to performance entries: your own `mark`/`measure`, `gc`, `function` (from `timerify`), `http`, `dns`, `net` and `resource`. `createHistogram` records values and gives percentiles, which is handy for latency.

```js
import {
  PerformanceObserver,
  createHistogram,
  performance,
} from "node:perf_hooks";

const obs = new PerformanceObserver((list) => {
  for (const e of list.getEntries()) {
    console.log(e.entryType, e.name, e.duration.toFixed(2));
  }
});
obs.observe({ entryTypes: ["gc", "http", "measure"] });

const latency = createHistogram();
const t0 = performance.now();
await handle();
latency.record(Math.round((performance.now() - t0) * 1000)); // microseconds, must be an integer
console.log(latency.percentile(99));
```

### 352: What are common mistakes in micro-benchmarks?

- **No warm-up**: the first runs are in the interpreter, later ones are optimized.
- **Dead code elimination**: if the result isn't used, V8 may skip the work entirely.
- **Constant folding**: using the same constant input lets V8 compute the answer once.
- **Measuring too little**: timer resolution and noise dominate. Run many iterations and repeat.
- **GC noise**: a GC can land in the middle of one run.
- **Different conditions**: comparing code with different input shapes, or after the other test already polluted the inline caches.
- **Not testing real workloads**: a faster micro-op might not matter in the full app.

Use a proper tool (`mitata`, `tinybench`), run each case in a separate process for big comparisons, and confirm with an end-to-end benchmark or a profile.

### 353: How can you make JSON serialization faster?

- **Send less**: select only needed fields and paginate.
- **Schema-based serializers** like `fast-json-stringify` (used by Fastify response schemas) generate a specialized function for one shape, which avoids generic type checks.
- **Avoid `toJSON` and big `replacer` functions** on hot paths.
- **Cache** serialized output for responses that don't change often.
- **Stream** large arrays instead of building one huge string.
- **Move it off the main thread** only if it's really large, because sending data to a worker also costs serialization.

Recent V8 versions (in Node 25 and newer) made `JSON.stringify` itself much faster for plain data objects without replacers or getters, so measure on your version before adding complexity.

### 354: What is a megamorphic call site and how does it affect performance?

A call site or property access that sees more than about four different object shapes becomes megamorphic. V8 stops using fast inline caches for it and uses a slower global lookup cache instead. This often happens in generic code like `function getId(obj) { return obj.id }` used with many object types, or with objects built from user data with different key orders. Usually it's not worth worrying about. But if a profile shows a hot function like that, you can normalize objects into one shape (for example with a class or a factory that always sets the same keys in the same order) or split the function by type.

### 355: How do you speed up Node.js startup?

- **Compile cache**: `module.enableCompileCache()` or `NODE_COMPILE_CACHE=dir` stores V8 code cache for loaded modules on disk, so later starts skip parsing and compiling. Big win for CLIs.
- **Bundle** your app into one file with esbuild to reduce file system lookups.
- **Lazy-load** heavy modules with `import()` only when needed.
- **Avoid sync work at import time** (reading large files, building big objects).
- **Startup snapshots** (question 356) for apps that do a lot of setup.
- Check what's slow with `node --cpu-prof` on startup and look at the module loading part of the profile.

```js
// at the very top of a CLI entry point
import module from "node:module";
module.enableCompileCache?.();
```

### 356: What is a startup snapshot?

V8 can save a snapshot of the heap after some initialization code has run, and Node can start from that snapshot later instead of running the code again. This is useful when your app builds large data structures at startup. You build the snapshot with `--build-snapshot` and run with `--snapshot-blob`. Code in the snapshot can't keep things like open handles, and you use `v8.startupSnapshot` APIs to set the main function and fix up state after load.

```js
// entry.js
const v8 = require("node:v8");
const bigTable = buildLookupTable(); // expensive

v8.startupSnapshot.setDeserializeMainFunction(() => {
  console.log("ready with", bigTable.size, "entries");
});
```

```bash
node --snapshot-blob snap.blob --build-snapshot entry.js
node --snapshot-blob snap.blob
```

Snapshots can also be included in Single Executable Applications with `"useSnapshot": true`.

### 357: What should you know when shipping a Single Executable Application?

- Bundle your code into one CommonJS or ESM file first (esbuild, rollup). Older versions only support CommonJS as the main script, so check your version.
- Inside a SEA, `require()` only loads built-in modules by default. Use `module.createRequire(process.execPath)` or bundle everything.
- Use the `assets` field in the SEA config to embed files, and read them with `sea.getAsset()` from `node:sea`.
- Native addons can't be bundled into the blob directly. Extract them to disk at runtime or avoid them.
- You must re-sign the binary on macOS (`codesign`) and may want to sign on Windows. Remove the existing signature before injecting.
- Turn on `useCodeCache` or `useSnapshot` in the config for faster startup.
- The binary is as big as `node` itself (tens of MB).

```js
import { getAsset, isSea } from "node:sea";
const template = isSea()
  ? getAsset("template.html", "utf8")
  : readFileSync("template.html", "utf8");
```

### 358: How does the permission model work in more detail?

When you run Node with `--permission`, these are denied unless allowed:

- File system reads and writes: `--allow-fs-read=<path>`, `--allow-fs-write=<path>` (globs and multiple flags allowed).
- `child_process`: `--allow-child-process`.
- `worker_threads`: `--allow-worker`.
- Native addons: `--allow-addons`. WASI: `--allow-wasi`.
- Network: `--allow-net` (added in newer versions).

Denied operations throw `ERR_ACCESS_DENIED`. Code can check access with `process.permission.has(scope, reference)`. Limits to keep in mind: permissions are inherited by workers, already opened file descriptors aren't checked, symlinks can be tricky, and code that can run native code or start child processes can bypass it. It reduces damage from bugs and malicious dependencies, but it is not a sandbox for running untrusted code.

```bash
node --permission --allow-fs-read=./config --allow-fs-write=/tmp app.js
```

You can also put the permissions in a config file with `--experimental-config-file` in newer versions.

### 359: Can the vm module be used to run untrusted code safely?

No. The Node docs say clearly that `vm` is not a security mechanism. Code in a `vm` context can often escape through prototypes of objects passed in (for example `this.constructor.constructor('return process')()`), and it shares the same process, event loop and memory, so it can block or crash everything with `while(true){}` or huge allocations. `vm2` is deprecated because of repeated escapes. To run untrusted code, use real isolation: a separate process with OS sandboxing, containers or microVMs (Firecracker, gVisor), `isolated-vm` (separate V8 isolates), or WebAssembly.

### 360: What is the vm module actually good for?

It runs code in a separate V8 context (its own globals) inside the same process. It's useful for template engines, REPL-like tools, test runners that need fresh globals, evaluating config files, and running scripts with a limited set of globals and a timeout (for trusted code).

```js
import vm from "node:vm";

const context = vm.createContext({ items: [1, 2, 3], result: null });
vm.runInContext("result = items.reduce((a, b) => a + b, 0)", context, {
  timeout: 50,
});
console.log(context.result); // 6

const script = new vm.Script("x * 2");
console.log(script.runInNewContext({ x: 21 })); // 42
```

`timeout` only stops synchronous code. A promise loop or async code can still run after it.

### 361: How do you protect an app from prototype pollution in depth?

- **Validate input** with a strict schema (`additionalProperties: false`, `z.strictObject`).
- **Use safe structures**: `Map` for dynamic keys, `Object.create(null)` for dictionaries, and check `Object.hasOwn(obj, key)` instead of `obj[key]` or `in`.
- **Freeze the prototype** at startup in apps where you control all code: `Object.freeze(Object.prototype)`. It can break some libraries, so test it.
- **`--disable-proto=delete`** or `--disable-proto=throw` removes or blocks `Object.prototype.__proto__`. It doesn't stop `constructor.prototype` attacks, so it's only a partial fix.
- **Avoid unsafe deep merge** helpers, or use ones that block `__proto__`, `constructor` and `prototype`.
- **Use `JSON.parse` carefully**: it creates an own property called `__proto__`, which becomes dangerous only when merged.

```js
function safeMerge(target, source) {
  for (const key of Object.keys(source)) {
    if (key === "__proto__" || key === "constructor" || key === "prototype")
      continue;
    const val = source[key];
    if (val && typeof val === "object" && !Array.isArray(val)) {
      target[key] = safeMerge(
        Object.hasOwn(target, key) ? target[key] : {},
        val,
      );
    } else {
      target[key] = val;
    }
  }
  return target;
}
```

### 362: What timing attacks exist besides string comparison, and how do you prevent them?

- **User enumeration on login**: if "user not found" returns fast but "wrong password" takes longer (because you hashed it), attackers learn which emails exist. Always run the hash, even for unknown users, using a dummy hash.
- **Token lookups**: looking up a token by value in a database index can leak timing. Store a hash of the token and look up by a separate ID.
- **Early returns in signature checks**: compare full HMACs with `timingSafeEqual`.
- **Length leaks**: `timingSafeEqual` throws on different lengths, so check lengths first or compare hashes of both values (which have fixed length).

```js
const DUMMY = await hashPassword("dummy-password");

async function login(email, password) {
  const user = await users.findByEmail(email);
  const ok = await verifyPassword(password, user?.passwordHash ?? DUMMY);
  if (!user || !ok) throw new AuthError("Invalid email or password");
  return user;
}
```

### 363: What is SSRF and how do you prevent it in Node.js?

Server-Side Request Forgery is when an attacker makes your server send requests to URLs they choose, like `http://169.254.169.254/` (cloud metadata with credentials) or internal services. It happens in features like "fetch this URL", webhooks, image proxies and PDF generators.

Prevention:

- Allow only expected hosts or domains when possible.
- Only allow `http:` and `https:` schemes.
- Resolve the hostname and block private, loopback, link-local and metadata IP ranges. Check the IP you actually connect to (to avoid DNS rebinding), for example with a custom `lookup` in the HTTP agent.
- Don't follow redirects automatically, or re-check each redirect target.
- Set timeouts and response size limits.
- Run these features in a network segment without access to internal services, and use IMDSv2 on AWS.

```js
import { lookup } from "node:dns/promises";
import ipaddr from "ipaddr.js";

async function assertPublicUrl(raw) {
  const url = new URL(raw);
  if (!["http:", "https:"].includes(url.protocol))
    throw new Error("Bad scheme");
  const addrs = await lookup(url.hostname, { all: true });
  for (const { address } of addrs) {
    if (ipaddr.parse(address).range() !== "unicast")
      throw new Error("Blocked address");
  }
  return url;
}
```

### 364: How do you set a strict Content Security Policy for server-rendered pages?

Generate a random nonce for every response, put it in the CSP header, and add it to each inline `<script>` you trust. Scripts without the right nonce won't run, which blocks most XSS even if an attacker injects HTML. `strict-dynamic` lets your trusted scripts load others.

```js
import { randomBytes } from "node:crypto";
import helmet from "helmet";

app.use((req, res, next) => {
  res.locals.nonce = randomBytes(16).toString("base64");
  next();
});

app.use(
  helmet({
    contentSecurityPolicy: {
      directives: {
        defaultSrc: ["'self'"],
        scriptSrc: [
          "'self'",
          (req, res) => `'nonce-${res.locals.nonce}'`,
          "'strict-dynamic'",
        ],
        objectSrc: ["'none'"],
        baseUri: ["'none'"],
      },
    },
  }),
);

// in the template: <script nonce="<%= nonce %>">...</script>
```

Still escape all output in templates. CSP is a second line of defense, not a replacement.

### 365: How do you avoid leaking secrets from a Node.js process?

- Don't log whole request objects, headers, configs or `process.env`. Use logger redaction (`pino` `redact`).
- Don't include stack traces or internal error messages in API responses in production.
- Remember that child processes inherit `process.env` by default. Pass an explicit `env` to `spawn`.
- Heap snapshots and core dumps contain secrets. Protect them like secrets.
- Error tracking tools (Sentry etc.) may capture local variables and request bodies. Configure scrubbing.
- Load secrets from a secret manager at startup, keep them in memory, and rotate them.
- Use `--disallow-code-generation-from-strings` if you don't need `eval`, to reduce what an injection can do.

```js
spawn("convert", args, { env: { PATH: process.env.PATH } }); // only what's needed
```

### 366: What supply chain attacks target npm, and how do you defend against them?

Attacks:

- **Typosquatting**: `expresss`, `lodahs`.
- **Dependency confusion**: a public package with the same name as your internal one, but a higher version.
- **Account takeover**: a maintainer's token is stolen and a malicious version is published. Some self-spreading attacks in 2025 used stolen tokens to publish infected versions of many popular packages.
- **Malicious install scripts** that steal tokens and env vars.
- **Protestware** or sabotage by the real maintainer.

Defenses:

- Lock files plus `npm ci`, and review lock file changes in PRs.
- Use scoped packages (`@company/x`) for internal code and map the scope to your private registry in `.npmrc`.
- Disable install scripts by default (`ignore-scripts=true`) and allow them only for packages that need them. pnpm blocks them by default in recent versions.
- Add a minimum release age before using new versions (supported by pnpm, Yarn and Renovate settings).
- Check provenance and signatures, enable 2FA and use trusted publishing (OIDC) instead of long-lived npm tokens.
- Use tools like Socket, Snyk or `npm audit`, and keep the number of dependencies small.
- Run CI with limited secrets, and run Node with `--permission` where possible.

### 367: Why should you crash on uncaughtException instead of continuing?

After an uncaught exception, you don't know what state the app is in. A request may have been half processed, a lock may be held, a transaction left open, an object half updated, or a stream left in a broken state. Continuing can cause data corruption and strange bugs that are much harder to find than a crash. The safe approach: log the error with as much context as possible, try to stop accepting new work, give in-flight requests a short time to finish, then exit with a non-zero code and let the orchestrator restart a clean process. Run several instances so one crash doesn't cause downtime.

```js
process.on("uncaughtException", (err, origin) => {
  logger.fatal({ err, origin }, "uncaught exception, shutting down");
  server.close();
  setTimeout(() => process.exit(1), 5000).unref();
});
```

`process.setUncaughtExceptionCaptureCallback()` exists too, but it's meant for tools like REPLs.

### 368: What was the domain module and why is it deprecated?

`domain` was an early attempt (Node 0.8) to group async operations and catch their errors together, so a server could handle an error for one request without crashing. It worked by patching event emitters and callbacks, had many edge cases, didn't work well with promises, and encouraged the risky practice of continuing after unknown errors. It has been deprecated for a long time. Today you use `async/await` with `try/catch`, proper error handling in frameworks, and `AsyncLocalStorage` for request context.

### 369: What do the --unhandled-rejections modes do?

- `throw` (default since Node 15): emit `unhandledRejection`. If there's no listener, throw it as an uncaught exception.
- `strict`: always raise it as an uncaught exception. If that's handled, `unhandledRejection` is emitted.
- `warn`: always print a warning, never crash.
- `warn-with-error-code`: like `warn`, but sets the exit code to 1.
- `none`: silence warnings.

Keep the default in production. Using `warn` hides real bugs and leaves the app in an unknown state, just like ignoring uncaught exceptions.

### 370: How can promises cause memory leaks?

- **Promises that never settle** keep their `.then` callbacks and closures in memory forever, for example waiting for an event that never comes, without a timeout.
- **`Promise.race` with a long-lived promise**: each `race` adds a reaction to that promise. If you race against the same "shutdown" promise in a loop, the reactions pile up, because the race doesn't remove them from the losing promise.
- **Big closures** captured in callbacks that wait a long time.
- **Unbounded `Promise.all`** on huge arrays creates all the work at once.

```js
// leaks: every iteration adds a reaction to `stopped`
while (true) {
  await Promise.race([nextJob(), stopped]);
}

// better: use an AbortSignal
while (!signal.aborted) {
  await nextJob({ signal });
}
```

### 371: How do async stack traces and source maps work in Node?

V8 has "zero-cost async stack traces": when an `async` function is resumed after `await`, V8 can reconstruct the chain of async functions that were awaiting it and show them as `at async fn` lines. This only works through `await`. Plain `.then()` chains and callbacks don't give full traces, which is another reason to prefer `async/await`.

For TypeScript or bundled code, use `--enable-source-maps` (or `process.setSourceMapsEnabled(true)`, or `module.setSourceMapsSupport()` in newer versions) so stack traces point to your original files and lines. It adds some cost when creating stack traces, so it's slow if your app creates many errors.

```bash
node --enable-source-maps dist/server.js
```

### 372: What are Error.captureStackTrace and Error.stackTraceLimit?

`Error.captureStackTrace(obj, fn)` adds a `stack` property to any object, and hides all frames above `fn`. Libraries use it to remove their own internal frames from stack traces. `Error.stackTraceLimit` sets how many frames are recorded (default 10). Raising it helps debugging deep async code. Setting it to 0 makes creating errors cheaper, which some performance-sensitive libraries do for errors used for flow control.

```js
class ValidationError extends Error {
  constructor(msg) {
    super(msg);
    Error.captureStackTrace(this, ValidationError);
  }
}

Error.stackTraceLimit = 50;
```

```bash
node --stack-trace-limit=50 app.js
```

### 373: How do you work with AggregateError and error cause chains?

`AggregateError` holds several errors in its `errors` array. `Promise.any` throws it when all promises reject, and you can create one yourself when collecting errors (for example from `Promise.allSettled`). `cause` chains link errors through layers. Node's `util.inspect` prints the whole chain, but your logger may need to walk it.

```js
const results = await Promise.allSettled(tasks.map((t) => t()));
const failures = results
  .filter((r) => r.status === "rejected")
  .map((r) => r.reason);
if (failures.length)
  throw new AggregateError(failures, `${failures.length} tasks failed`);

function* causes(err) {
  while (err) {
    yield err;
    err = err.cause;
  }
}
for (const e of causes(error)) console.log(e.name, e.message);
```

### 374: How do you pass cancellation through all layers of an app?

Accept an `AbortSignal` in every async function that does I/O or waits, and pass it down to `fetch`, database drivers, `timers/promises`, streams and child processes. At the top, create the signal from the request (abort when the client disconnects) combined with a timeout. Check `signal.throwIfAborted()` between steps of long CPU work.

```js
app.get("/report", async (req, res, next) => {
  const ac = new AbortController();
  res.on("close", () => {
    if (!res.writableFinished) ac.abort();
  });
  const signal = AbortSignal.any([ac.signal, AbortSignal.timeout(10_000)]);

  try {
    res.json(await buildReport(req.query, { signal }));
  } catch (err) {
    if (signal.aborted) return; // client gone or timed out
    next(err);
  }
});

async function buildReport(query, { signal }) {
  const data = await fetch(`${API}/data`, { signal }).then((r) => r.json());
  signal.throwIfAborted();
  const rows = await db.query(sql, params, { signal });
  return summarize(rows);
}
```

### 375: How do you write a concurrency limiter (like p-limit) from scratch?

Keep a count of running tasks and a queue of waiting ones. When a task finishes, start the next from the queue.

```js
export function limit(concurrency) {
  let active = 0;
  const queue = [];

  const next = () => {
    if (active >= concurrency || queue.length === 0) return;
    active++;
    const { fn, resolve, reject } = queue.shift();
    Promise.resolve()
      .then(fn)
      .then(resolve, reject)
      .finally(() => {
        active--;
        next();
      });
  };

  return (fn) =>
    new Promise((resolve, reject) => {
      queue.push({ fn, resolve, reject });
      next();
    });
}

const run = limit(3);
const pages = await Promise.all(
  urls.map((u) => run(() => fetch(u).then((r) => r.text()))),
);
```

For big queues, use an index or a linked list instead of `shift()`, which is O(n).

### 376: How do you implement a token bucket rate limiter?

Each client has a bucket with a maximum number of tokens. Tokens are added at a fixed rate. Each request takes one token. If the bucket is empty, the request is rejected. This allows short bursts while keeping a steady average rate. You don't need a timer: compute how many tokens to add from the time since the last request.

```js
export class TokenBucket {
  constructor({ capacity, refillPerSec }) {
    this.capacity = capacity;
    this.refillPerMs = refillPerSec / 1000;
    this.buckets = new Map();
  }

  take(key, now = performance.now()) {
    let b = this.buckets.get(key);
    if (!b) {
      b = { tokens: this.capacity, last: now };
      this.buckets.set(key, b);
    }
    b.tokens = Math.min(
      this.capacity,
      b.tokens + (now - b.last) * this.refillPerMs,
    );
    b.last = now;
    if (b.tokens < 1) return false;
    b.tokens -= 1;
    return true;
  }
}

const limiter = new TokenBucket({ capacity: 10, refillPerSec: 5 });
app.use((req, res, next) =>
  limiter.take(req.ip) ? next() : res.sendStatus(429),
);
```

In production, clean up old buckets, and with several instances do the same logic in Redis with a Lua script so it's atomic.

### 377: How do you implement an LRU cache?

A `Map` keeps insertion order, so you can delete and re-insert a key to mark it as recently used, and evict the first key when the cache is full. All operations are O(1).

```js
export class LRUCache {
  constructor(max = 1000) {
    this.max = max;
    this.map = new Map();
  }

  get(key) {
    if (!this.map.has(key)) return undefined;
    const value = this.map.get(key);
    this.map.delete(key);
    this.map.set(key, value);
    return value;
  }

  set(key, value) {
    if (this.map.has(key)) this.map.delete(key);
    this.map.set(key, value);
    if (this.map.size > this.max) {
      this.map.delete(this.map.keys().next().value);
    }
  }
}
```

Real caches also need TTLs and maybe size-based limits. The `lru-cache` package handles these.

### 378: How would you implement a basic EventEmitter yourself?

```js
export class MiniEmitter {
  #events = new Map();

  on(name, fn) {
    if (!this.#events.has(name)) this.#events.set(name, []);
    this.#events.get(name).push(fn);
    return this;
  }

  off(name, fn) {
    const list = this.#events.get(name);
    if (list)
      this.#events.set(
        name,
        list.filter((l) => l !== fn && l.original !== fn),
      );
    return this;
  }

  once(name, fn) {
    const wrapper = (...args) => {
      this.off(name, wrapper);
      fn.apply(this, args);
    };
    wrapper.original = fn;
    return this.on(name, wrapper);
  }

  emit(name, ...args) {
    const list = this.#events.get(name);
    if (!list || list.length === 0) {
      if (name === "error") throw args[0];
      return false;
    }
    for (const fn of [...list]) fn.apply(this, args); // copy so changes during emit are safe
    return true;
  }
}
```

Points interviewers look for: listeners are called synchronously, the list is copied before looping, `once` can be removed with the original function, and an unhandled `'error'` throws.

### 379: How would you implement util.promisify yourself?

```js
export function promisify(fn) {
  if (typeof fn[promisify.custom] === "function") return fn[promisify.custom];

  return function (...args) {
    return new Promise((resolve, reject) => {
      fn.call(this, ...args, (err, ...results) => {
        if (err) return reject(err);
        resolve(results.length > 1 ? results : results[0]);
      });
    });
  };
}
promisify.custom = Symbol.for("nodejs.util.promisify.custom");
```

Keeping `this` with `fn.call(this, ...)` matters for methods. The real `util.promisify` resolves with only the first result unless the function defines a custom version.

### 380: How would you implement Promise.all yourself?

```js
function promiseAll(iterable) {
  return new Promise((resolve, reject) => {
    const items = Array.from(iterable);
    const results = new Array(items.length);
    let remaining = items.length;

    if (remaining === 0) return resolve(results);

    items.forEach((item, i) => {
      Promise.resolve(item).then((value) => {
        results[i] = value;
        if (--remaining === 0) resolve(results);
      }, reject);
    });
  });
}
```

Key details: keep results in the original order (not finish order), handle non-promise values with `Promise.resolve`, resolve right away for an empty input, and reject on the first failure. The other promises keep running, because promises can't be cancelled.

### 381: How do Koa-style middleware (compose) work? Implement it.

Each middleware gets `ctx` and `next`. Calling `await next()` runs the rest of the chain and then returns to the current middleware, so code after `await next()` runs on the way back out (the "onion" model). This makes timing, error handling and response changes easy.

```js
function compose(middleware) {
  return function (ctx) {
    let index = -1;
    function dispatch(i) {
      if (i <= index) return Promise.reject(new Error("next() called twice"));
      index = i;
      const fn = middleware[i];
      if (!fn) return Promise.resolve();
      try {
        return Promise.resolve(fn(ctx, () => dispatch(i + 1)));
      } catch (err) {
        return Promise.reject(err);
      }
    }
    return dispatch(0);
  };
}

const app = compose([
  async (ctx, next) => {
    const t = Date.now();
    await next();
    ctx.ms = Date.now() - t;
  },
  async (ctx, next) => {
    ctx.body = "hello";
    await next();
  },
]);

const ctx = {};
await app(ctx);
console.log(ctx); // { body: 'hello', ms: 0 }
```

### 382: What is request coalescing (single flight), and how do you implement it?

When many requests ask for the same thing at the same time (say, the same product while the cache is empty), you only want one call to the database or upstream service. The others wait for that same promise. This prevents a "thundering herd".

```js
const inFlight = new Map();

export function singleFlight(key, fn) {
  if (inFlight.has(key)) return inFlight.get(key);
  const p = Promise.resolve()
    .then(fn)
    .finally(() => inFlight.delete(key));
  inFlight.set(key, p);
  return p;
}

app.get("/product/:id", async (req, res) => {
  const product = await singleFlight(`product:${req.params.id}`, () =>
    loadProduct(req.params.id),
  );
  res.json(product);
});
```

This works inside one process. Across instances, combine it with a shared cache and a short lock.

### 383: What is a cache stampede and how do you prevent it?

When a popular cache key expires, many requests miss at the same moment and all hit the database together, which can take it down. Ways to prevent it:

- **Request coalescing** (question 382) per instance.
- **A lock** in Redis so only one instance rebuilds the value, and others wait or serve stale data.
- **Stale-while-revalidate**: keep serving the old value after its "soft" expiry while one request refreshes it in the background.
- **Random jitter** in TTLs, so many keys don't expire at the same time.
- **Early refresh** with a probability that grows as expiry gets closer.

```js
async function getWithSWR(
  key,
  loader,
  { ttl = 60_000, staleTtl = 300_000 } = {},
) {
  const entry = cache.get(key);
  const now = Date.now();

  if (entry && now < entry.freshUntil) return entry.value;

  if (entry && now < entry.staleUntil) {
    singleFlight(key, async () => {
      const value = await loader();
      cache.set(key, {
        value,
        freshUntil: Date.now() + ttl,
        staleUntil: Date.now() + staleTtl,
      });
    }).catch(() => {});
    return entry.value; // serve stale
  }

  const value = await singleFlight(key, loader);
  cache.set(key, { value, freshUntil: now + ttl, staleUntil: now + staleTtl });
  return value;
}
```

### 384: How do you implement a distributed lock with Redis, and what are its limits?

Use `SET key token NX PX ttl` to take the lock only if it's free, with an expiry so a crashed holder doesn't block forever. Release it only if you still own it, by comparing the token in a Lua script (so another holder's lock isn't deleted by mistake).

```js
import { randomUUID } from "node:crypto";

async function withLock(redis, key, ttlMs, fn) {
  const token = randomUUID();
  const ok = await redis.set(key, token, { NX: true, PX: ttlMs });
  if (!ok) throw new Error("Lock busy");
  try {
    return await fn();
  } finally {
    await redis.eval(
      `if redis.call('get', KEYS[1]) == ARGV[1] then return redis.call('del', KEYS[1]) else return 0 end`,
      { keys: [key], arguments: [token] },
    );
  }
}
```

Limits: if your work takes longer than the TTL (because of a GC pause or a slow network), the lock expires and someone else gets it while you're still running. For correctness-critical cases, use fencing tokens (an increasing number checked by the storage layer) or rely on database constraints and transactions instead of a lock.

### 385: What is the transactional outbox pattern?

When you save data and also need to publish an event (for example "order created"), doing both separately can fail halfway: the DB write succeeds but the message isn't sent, or the other way round. With the outbox pattern you write the event into an `outbox` table in the **same database transaction** as the data. A separate process reads the outbox and publishes events to the broker, marking them as sent. Delivery is at-least-once, so consumers must be idempotent.

```js
await db.transaction(async (tx) => {
  const order = await tx.insert("orders", data);
  await tx.insert("outbox", {
    id: randomUUID(),
    type: "order.created",
    payload: JSON.stringify(order),
  });
});

// relay worker
setInterval(async () => {
  const events = await db.query(
    `SELECT * FROM outbox WHERE sent_at IS NULL ORDER BY created_at LIMIT 100 FOR UPDATE SKIP LOCKED`,
  );
  for (const e of events) {
    await broker.publish(e.type, e.payload, { messageId: e.id });
    await db.query("UPDATE outbox SET sent_at = now() WHERE id = $1", [e.id]);
  }
}, 1000);
```

### 386: How do you build a reliable message consumer?

Most brokers give at-least-once delivery, so messages can arrive twice or out of order. A reliable consumer:

- **Acknowledges only after** the work is done (and committed).
- **Is idempotent**: records processed message IDs in the same transaction as the side effect, or uses upserts and unique constraints.
- **Retries with backoff** on temporary errors and sends messages that keep failing to a dead-letter queue.
- **Limits concurrency** (prefetch count) so it doesn't take more than it can handle.
- **Shuts down gracefully**: stops pulling new messages, finishes current ones, then acknowledges and closes.

```js
async function handle(msg) {
  await db.transaction(async (tx) => {
    const inserted = await tx.query(
      "INSERT INTO processed_messages (id) VALUES ($1) ON CONFLICT DO NOTHING RETURNING id",
      [msg.id],
    );
    if (inserted.rowCount === 0) return; // duplicate
    await applyBusinessLogic(tx, msg.body);
  });
}
```

### 387: How do you handle backpressure between services, not just inside streams?

- **Bound everything**: limit concurrent outgoing requests (connection pool size, a concurrency limiter), queue lengths and request body sizes.
- **Return 429 or 503 early** when overloaded, with `Retry-After`, instead of accepting work you can't finish.
- **Respect upstream signals**: when you get 429 or 503, back off with jitter.
- **Use queues** between producers and slow consumers, and watch queue depth.
- **Timeouts and deadlines**: pass a deadline down the call chain, so services stop work the caller has already given up on.
- **Bulkheads**: separate pools for different dependencies, so one slow dependency doesn't use all your connections.

Without these, a slow downstream service makes requests pile up in memory in every service above it, until they all fall over together.

### 388: How do you stream a large upload directly to object storage?

Don't buffer the whole file in memory or on disk. Parse the multipart stream with `busboy` and pipe each file stream straight to S3 (or another store) using a multipart upload, which accepts streams of unknown length. Enforce size limits while streaming.

```js
import busboy from "busboy";
import { Upload } from "@aws-sdk/lib-storage";

app.post("/upload", (req, res, next) => {
  const bb = busboy({
    headers: req.headers,
    limits: { fileSize: 500 * 1024 * 1024, files: 1 },
  });

  bb.on("file", async (name, file, info) => {
    file.on("limit", () => file.destroy(new Error("File too large")));
    try {
      const upload = new Upload({
        client: s3,
        params: {
          Bucket: "uploads",
          Key: `${randomUUID()}-${info.filename}`,
          Body: file,
          ContentType: info.mimeType,
        },
      });
      const result = await upload.done();
      res.status(201).json({ key: result.Key });
    } catch (err) {
      next(err);
    }
  });

  req.pipe(bb);
});
```

An often better option is to give the client a pre-signed URL so it uploads to storage directly, and your server never touches the bytes.

### 389: How do you parse a huge CSV file efficiently?

Stream it and parse row by row with a streaming parser (`csv-parse`, `papaparse`), process in batches (for example insert 1000 rows per DB query), and use `pipeline` so backpressure slows the reading when the database is busy.

```js
import { parse } from "csv-parse";
import { pipeline } from "node:stream/promises";
import { createReadStream } from "node:fs";

let batch = [];

await pipeline(
  createReadStream("users.csv"),
  parse({ columns: true, skip_empty_lines: true }),
  async function (rows) {
    for await (const row of rows) {
      batch.push(row);
      if (batch.length === 1000) {
        await db.insertMany("users", batch);
        batch = [];
      }
    }
    if (batch.length) await db.insertMany("users", batch);
  },
);
```

### 390: How do you manage database connections in serverless functions?

Each function instance has its own process, and there can be hundreds of instances during a spike. If each one opens a pool of 10 connections, the database runs out of connections quickly. Tips:

- Create the client **outside the handler**, so warm invocations reuse it.
- Use a **small pool** (1 or 2) per instance.
- Use a **connection pooler or proxy** in front of the database (RDS Proxy, PgBouncer, Supabase/Neon poolers), or HTTP-based database drivers made for serverless.
- Set short idle timeouts, since frozen instances keep connections open without using them.

```js
import pg from "pg";
const pool = new pg.Pool({
  connectionString: process.env.DATABASE_URL,
  max: 1,
});

export async function handler(event) {
  const { rows } = await pool.query("SELECT now()");
  return { statusCode: 200, body: JSON.stringify(rows[0]) };
}
```

### 391: What affects cold start time for Node.js on serverless platforms?

- **Bundle size and number of files**: loading many small modules from `node_modules` is slow. Bundle and minify with esbuild, and tree-shake.
- **Work at import time**: SDK clients, big config parsing, and connecting to services before the first request.
- **Heavy dependencies**: some SDKs and ORMs take hundreds of milliseconds to load. Use modular SDKs (AWS SDK v3 per-service clients).
- **Memory setting**: on many platforms more memory also means more CPU, which speeds up startup.
- **Platform features**: provisioned concurrency, snapshots (like Lambda SnapStart, where supported) and keeping functions warm.
- The **V8 compile cache** can help where the file system is writable and kept between starts.

### 392: How are edge runtimes different from Node.js?

Edge runtimes (Cloudflare Workers, Vercel Edge, Deno Deploy) run JavaScript in V8 isolates close to users. They mostly use web standard APIs: `fetch`, `Request`, `Response`, Web Streams, Web Crypto, `URL`. Many Node APIs like `fs`, `child_process`, `net` or native addons are missing or only partly supported through compatibility layers. There are stricter CPU time and memory limits, and no long-lived processes. The WinterTC group (at Ecma, formerly WinterCG) defines a common set of APIs for these runtimes. To write portable code, use web standard APIs, avoid Node-only modules in shared code, and use frameworks like Hono that work everywhere.

### 393: How compatible are Bun and Deno with Node.js?

Both aim for high Node compatibility. Bun implements most Node APIs and runs most npm packages directly, with its own fast bundler, test runner and package manager. Deno supports `npm:` specifiers, `node:` built-ins and `package.json`, and has a permission system and built-in TypeScript. Compatibility is good for common packages, but differences appear in edge cases: native addons, less common Node APIs (`vm`, `inspector`, some `worker_threads` and `http2` details), exact timing of the event loop, and error messages. If you depend on the exact Node behavior, test on the target runtime.

### 394: What is HTTP request smuggling, and how does Node protect against it?

Request smuggling happens when a front-end proxy and a back-end server disagree about where one HTTP request ends and the next begins, for example because of conflicting `Content-Length` and `Transfer-Encoding` headers, or unusual whitespace. An attacker can then hide a second request inside the first and have it processed as a request from another user. Node's HTTP parser (llhttp) is strict by default: it rejects requests with both headers, invalid chunk encoding and other ambiguous input. Don't turn on `insecureHTTPParser` (or `--insecure-http-parser`) unless you really have to, keep Node updated (several smuggling CVEs have been fixed), and make sure your proxy normalizes requests.

### 395: What is a Slowloris attack, and which Node settings help?

Slowloris opens many connections and sends request headers extremely slowly, keeping each connection open as long as possible, so the server runs out of sockets or memory. Node's defaults help: `headersTimeout` (60 s) drops connections that don't finish headers in time, and `requestTimeout` (300 s) limits the whole request. You can make these stricter, limit header size with `maxHeaderSize` (16 KB default), and limit connections with `server.maxConnections`. In production, a reverse proxy or load balancer in front of Node usually takes most of this load.

```js
const server = http.createServer({ maxHeaderSize: 8192 }, app);
server.headersTimeout = 20_000;
server.requestTimeout = 30_000;
server.maxConnections = 10_000;
```

### 396: How do you protect a Node API from payload-based denial of service?

- **Limit body size** (`express.json({ limit: '100kb' })`), and limit uploads per file and per request.
- **Limit JSON depth and array lengths** in your validation schema, since deeply nested JSON can be slow to process or cause stack overflows in recursive code.
- **Limit query string parameters** (count, depth). Express 5's `simple` parser avoids nested objects by default.
- **Avoid expensive regex** on user input (ReDoS).
- **Limit decompression**: a small gzip body can expand to gigabytes (zip bomb). Set `maxOutputLength` in zlib, or check the size while streaming.
- **Rate limit** and set timeouts on everything.
- **Put expensive endpoints** (search, exports, image processing) behind queues or worker pools.

```js
import { gunzip } from "node:zlib";
gunzip(body, { maxOutputLength: 10 * 1024 * 1024 }, (err, out) => {
  /* ERR_BUFFER_TOO_LARGE */
});
```

### 397: How do you use the inspector module programmatically?

`node:inspector` (and `node:inspector/promises`) lets your code open a session with its own V8 inspector. You can take CPU profiles, heap snapshots or run code coverage from inside the app, for example from an admin endpoint, without restarting with `--inspect`.

```js
import { Session } from "node:inspector/promises";
import { writeFile } from "node:fs/promises";

export async function profileFor(ms) {
  const session = new Session();
  session.connect();
  await session.post("Profiler.enable");
  await session.post("Profiler.start");
  await new Promise((r) => setTimeout(r, ms));
  const { profile } = await session.post("Profiler.stop");
  session.disconnect();
  await writeFile(`./cpu-${Date.now()}.cpuprofile`, JSON.stringify(profile));
}
```

Protect any endpoint like this. Profiling and snapshots cost CPU and memory, and the output can contain sensitive data.

### 398: How do you debug a running production process safely?

- Sending `SIGUSR1` to a running Node process (on Linux and macOS) turns on the inspector on `127.0.0.1:9229`. Then use an SSH tunnel to connect from your machine. Never expose the inspector port to the network, because anyone who connects can run any code in the process.
- Prefer non-intrusive data first: logs, metrics, diagnostic reports (`--report-on-signal`), and a short CPU profile.
- Breakpoints pause the whole process, so don't use them on a server that serves real traffic. Use logpoints instead, or take the instance out of the load balancer first.
- You can disable `SIGUSR1` activation with `--disable-sigusr1` if you don't want this possibility in production.

```bash
kill -USR1 <pid>
ssh -L 9229:127.0.0.1:9229 user@server
# then open chrome://inspect
```

### 399: How do you investigate crashes in native code or hard-to-reproduce aborts?

- Run with `--abort-on-uncaught-exception` so Node aborts and writes a core dump (if `ulimit -c unlimited` is set) instead of just exiting. Then you can inspect the exact state.
- Use `llnode` (an LLDB plugin) to read JavaScript stack frames and objects from a core dump.
- Use `--report-on-fatalerror` to get a diagnostic report with native and JS stacks when V8 hits a fatal error.
- Check `dmesg` and container events for OOM kills, which leave no Node logs at all.
- For native addons, build a debug version and run under `gdb` or `lldb`, or with sanitizers (ASan).

### 400: Which V8 and Node trace flags are useful for performance work?

```bash
node --trace-gc app.js                  # one line per GC with pause times
node --trace-gc-verbose app.js
node --trace-opt --trace-deopt app.js   # what is optimized and deoptimized
node --trace-warnings app.js            # stack traces for warnings
node --trace-sync-io app.js             # warn on sync I/O after startup
node --trace-event-categories v8,node.async_hooks,node.perf app.js   # Chrome trace format, open in Perfetto
node --cpu-prof --heap-prof app.js      # profiles on exit
```

`node --v8-options` lists all V8 flags. Most are for debugging only and can change between versions, so don't rely on them in production.

### 401: How are timers implemented in Node.js?

Node doesn't create one libuv timer per `setTimeout`. It groups timers by duration: all timers with the same delay go into one linked list, because timers with the same delay that are added later always expire later, so the list stays sorted. A priority queue (binary heap) holds one entry per list, ordered by the next expiry time. Node uses a single libuv timer set to the earliest expiry. When it fires, Node runs all expired timers from the lists, and between each timer callback it drains the `nextTick` and microtask queues. This makes adding and removing timers cheap even with many thousands of them, like per-socket timeouts.

### 402: What changed in Node 11 about microtasks between timers, and why does it matter?

Before Node 11, when several timers expired at the same time, Node ran all their callbacks first and only then the microtasks. Since Node 11, Node runs the `nextTick` and microtask queues after **each** timer and each `setImmediate` callback, which matches how browsers behave.

```js
setTimeout(() => {
  console.log("t1");
  Promise.resolve().then(() => console.log("p1"));
}, 0);
setTimeout(() => {
  console.log("t2");
  Promise.resolve().then(() => console.log("p2"));
}, 0);

// Node 11+: t1 p1 t2 p2
// Node 10:  t1 t2 p1 p2
```

It matters when reasoning about old code or old blog posts, and when you rely on ordering between callbacks.

### 403: What happens when a queueMicrotask callback throws?

The error is not turned into a rejected promise. It's reported like an uncaught exception, which goes to `process.on('uncaughtException')` and, by default, crashes the process. Inside a promise `.then` callback, an error turns into a rejected promise instead. So if you use `queueMicrotask` for library code, catch your errors and report them in a controlled way.

```js
queueMicrotask(() => {
  throw new Error("boom"); // uncaught exception, process exits
});
```

### 404: What keeps a Node process alive, and how do you see it?

The process stays alive while there are **referenced** handles or pending requests in libuv: listening servers, open sockets, timers, child processes, file watchers, workers, pending fs or dns work, `process.stdin` in flowing mode. When none are left, the process exits. `unref()` on a handle stops it from keeping the process alive. To see what's still open:

```js
console.log(process.getActiveResourcesInfo());
// [ 'TCPServerWrap', 'Timeout', 'FSReqCallback', ... ]
```

A diagnostic report (`process.report.getReport().libuv`) shows more detail about each handle.

### 405: Why does a test process hang after all tests pass, and how do you fix it?

Something is still keeping the event loop alive: an open database pool, a Redis client, an HTTP server that wasn't closed, a `setInterval`, a keep-alive socket from `fetch` or a file watcher. Fix it by closing resources in `after` hooks. To find the culprit, print `process.getActiveResourcesInfo()` at the end or use a tool like `why-is-node-running`. Using `--test-force-exit` in `node:test` makes it exit anyway, but it hides the leak. It's better to find it, because the same leak may matter in production.

```js
after(async () => {
  await server.close();
  await pool.end();
  await redis.quit();
});
```

### 406: Why can RSS grow even when the JS heap is stable?

RSS includes everything the process uses: V8 heap, Buffers and ArrayBuffers (outside the heap), native memory from addons, OpenSSL, zlib contexts, thread stacks, the code itself, and memory the allocator keeps after it's freed. Common reasons for RSS growth with a flat heap:

- **Buffers kept alive** by references (for example in caches or pending sockets).
- **Native leaks** in addons or in use of `zlib` without closing streams.
- **Malloc fragmentation**: glibc creates many memory "arenas" for threads, and freed memory isn't always returned to the OS. Setting `MALLOC_ARENA_MAX=2` or using jemalloc (`LD_PRELOAD`) often reduces RSS a lot for Node apps on Linux.
- **Many worker threads**, each with its own heap.

Compare `heapUsed`, `external`, `arrayBuffers` and `rss` over time to narrow it down.

### 407: How can small strings keep large strings in memory?

V8 uses special string types for speed. A **sliced string** created with `substring` or `slice` may point into the original string instead of copying. If you keep a 10-character slice of a 10 MB string, the whole 10 MB stays alive. **Cons strings** (ropes) are created by `+` concatenation and keep both parts until flattened. This is usually invisible, but it can cause "leaks" when you extract small parts from huge inputs (like reading one field from a big file) and store them long-term. Forcing a copy breaks the link, for example by round-tripping through a Buffer.

```js
const big = await readFile("huge.log", "utf8");
const id = big.slice(0, 10); // may keep `big` alive
const safeId = Buffer.from(id).toString(); // independent copy
```

### 408: How do closures cause unexpected memory retention?

All closures created in the same function share one "context" object holding the variables any of them use. If one closure uses a large variable and another, long-lived closure is created in the same scope, the long-lived one also keeps the large variable alive, even though it never uses it.

```js
function setup() {
  const hugeData = new Array(1e6).fill("x");
  const unused = () => hugeData.length; // makes hugeData part of the shared context
  return () => console.log("tick"); // keeps hugeData alive too
}
setInterval(setup(), 1000);
```

Fix: avoid creating unrelated closures in the same scope as large data, set large variables to `null` when you're done with them, or move the long-lived function to a different scope.

### 409: What are elements kinds in V8 arrays, and why do they matter?

V8 tracks the kind of values in an array to pick a fast storage format: `PACKED_SMI_ELEMENTS` (small integers), `PACKED_DOUBLE_ELEMENTS`, `PACKED_ELEMENTS` (anything), and `HOLEY_*` versions for arrays with gaps. Transitions only go one way, to more general kinds. Once an array has a hole or a string, it never goes back. Holey arrays need extra checks along the prototype chain on every access.

```js
const a = [1, 2, 3]; // PACKED_SMI
a.push(4.5); // PACKED_DOUBLE
a.push("x"); // PACKED_ELEMENTS

const b = new Array(3); // HOLEY_SMI (has holes)
const c = [];
c[100] = 1; // holey, and may even become dictionary mode
```

For hot numeric code, prefer arrays filled in order from empty, or typed arrays (`Float64Array`, `Int32Array`), which have fixed types.

### 410: When should you use BigInt, and what are its costs?

Use `BigInt` when integers can go beyond `Number.MAX_SAFE_INTEGER` (2^53 - 1): 64-bit IDs from databases (Twitter-style snowflake IDs, Postgres `bigint`), nanosecond timestamps (`process.hrtime.bigint()`), cryptography or exact large counters. Costs: it's slower than numbers, you can't mix it with numbers in math without converting, `JSON.stringify` throws on it (you must convert to string), and `Math` functions don't accept it. Many DB drivers return `bigint` columns as strings by default for this reason.

```js
const id = 9007199254740993n;
id + 1n; // 9007199254740994n
// id + 1;          // TypeError: Cannot mix BigInt and other types

JSON.stringify({ id }, (k, v) => (typeof v === "bigint" ? v.toString() : v));
buf.readBigUInt64BE(0); // read 64-bit integers from binary data
```

### 411: How does internationalization (Intl) work in Node.js?

Node uses the ICU library for `Intl` (date and number formatting, collation, plural rules, segmentation), `String.prototype.localeCompare`, `toLocaleString` and time zones. Official Node builds come with full ICU data, so all locales work. Custom or minimal builds may have `small-icu` and only English. You can check with `process.versions.icu` and `Intl.DateTimeFormat().resolvedOptions()`. Time zone data comes from ICU too, so updating Node also updates time zone rules.

```js
new Intl.NumberFormat("de-DE", { style: "currency", currency: "EUR" }).format(
  1234.5,
); // '1.234,50 €'
new Intl.RelativeTimeFormat("en", { numeric: "auto" }).format(-1, "day"); // 'yesterday'
[...new Intl.Segmenter("en", { granularity: "word" }).segment("Hello world")]
  .length;
["ä", "a", "z"].sort(new Intl.Collator("sv").compare);
```

### 412: How do Node-API versions and prebuilt binaries work?

Each Node release supports a set of Node-API versions (`process.versions.napi`). An addon built against Node-API version N works on every Node release that supports N or higher, without recompiling. To avoid making users compile code on install (which needs Python and a C++ toolchain), packages ship **prebuilt binaries** for each platform and architecture. Common ways: `prebuildify` plus `node-gyp-build` (binaries inside the package), or separate optional dependency packages per platform, which is what `esbuild`, `@swc/core` and `sharp` do using the `os` and `cpu` fields in `package.json`.

```json
{
  "name": "@acme/native-linux-x64",
  "os": ["linux"],
  "cpu": ["x64"]
}
```

### 413: What problems do people hit with node-gyp, and how do you avoid them?

`node-gyp` compiles native addons during `npm install`. Common problems: missing Python or a C++ compiler (Xcode CLI tools, `build-essential`, Visual Studio Build Tools), wrong Node headers, building inside Alpine images that use musl instead of glibc, and very slow CI installs. Ways to avoid them: prefer packages that ship prebuilt binaries or WASM, use the same OS/libc in build and runtime images (for example build on `node:24-slim` and run on `node:24-slim`), cache builds in CI, and in Docker install build tools only in the build stage of a multi-stage build.

### 414: What must a native addon do to work in worker threads?

Each worker has its own V8 isolate and its own copy of every addon's module state. An addon loaded in a worker must be **context-aware**: it shouldn't keep JS objects or per-instance state in static/global C++ variables, and it must clean up when the worker exits. Node-API addons are context-aware when they store state with `napi_set_instance_data` (or `Napi::Addon` in `node-addon-api`) and use `NAPI_MODULE_INIT`. Old-style addons that aren't context-aware throw an error when loaded in a worker.

### 415: What cross-platform problems should you watch for in Node.js code?

- **Paths**: use `path.join`, never hardcode `/` or `\`. Use `fileURLToPath` and `pathToFileURL` to convert between URLs and paths, since `new URL(...).pathname` breaks on Windows drive letters and spaces.
- **Line endings**: `\r\n` on Windows. Split lines with `/\r?\n/` and use `os.EOL` when writing for the local system.
- **Case sensitivity**: macOS and Windows file systems are usually case-insensitive, Linux is not. An import with the wrong case works locally and fails in CI or Docker.
- **Signals**: Windows doesn't have most POSIX signals. `SIGTERM` handlers may not run, and `process.kill()` behaves differently.
- **Shell commands**: `rm -rf`, `cp` and environment syntax (`FOO=bar cmd`) don't work in Windows `cmd`. Use Node APIs (`fs.rm`, `fs.cp`) or tools like `cross-env`.
- **Spawning**: `.cmd` and `.bat` files need a shell on Windows (see question 417).
- **File locking and EBUSY/EPERM** errors on Windows when files are open.

### 416: What are the advanced options when spawning child processes?

```js
import { spawn } from "node:child_process";

const ac = new AbortController();
const child = spawn("ffmpeg", ["-i", "in.mp4", "out.webm"], {
  cwd: "/work",
  env: { PATH: process.env.PATH }, // don't leak all env vars
  stdio: ["ignore", "pipe", "inherit"], // stdin ignored, stdout piped, stderr shared
  signal: ac.signal, // abort kills the child
  timeout: 60_000, // kill after 60s
  killSignal: "SIGTERM",
  detached: false,
});
```

- `stdio` can use `'pipe'`, `'inherit'`, `'ignore'`, `'ipc'`, a stream or a file descriptor.
- `detached: true` with `child.unref()` lets the child keep running after the parent exits (for daemons). On POSIX it also makes the child the leader of a new process group.
- Killing a whole process tree: start it detached and kill the group with `process.kill(-child.pid, 'SIGTERM')` on POSIX. On Windows use `taskkill /T` or a library like `tree-kill`.
- Always handle `'error'` (spawn failed, for example `ENOENT`) and `'exit'`/`'close'` (it ran and exited).

### 417: Why does spawning a .bat or .cmd file on Windows fail without shell: true?

In April 2024 Node fixed a security issue (CVE-2024-27980, "BatBadBut") where arguments passed to `.bat` and `.cmd` files could be used for command injection, because Windows runs them through `cmd.exe` with its own parsing rules. Since then, `spawn` and `execFile` refuse to run `.bat`/`.cmd` files without `shell: true` and throw `EINVAL`. With `shell: true`, you are responsible for escaping arguments. This often shows up with `npm.cmd` or `npx.cmd` on Windows.

```js
// On Windows
spawn("npm.cmd", ["install"]); // throws EINVAL
spawn("npm.cmd", ["install"], { shell: true }); // works, but don't pass user input
```

### 418: How do you stream data through an external program like ffmpeg?

Pipe your input stream into the child's stdin and its stdout into your output, using `pipeline` so errors and early closing on either side clean up both. Also watch the exit code, because the process can fail after streams are done.

```js
import { spawn } from "node:child_process";
import { pipeline } from "node:stream/promises";
import { once } from "node:events";

app.post("/convert", async (req, res, next) => {
  const ff = spawn("ffmpeg", ["-i", "pipe:0", "-f", "mp3", "pipe:1"], {
    stdio: ["pipe", "pipe", "ignore"],
  });
  res.setHeader("Content-Type", "audio/mpeg");

  try {
    const exited = once(ff, "close");
    await Promise.all([pipeline(req, ff.stdin), pipeline(ff.stdout, res)]);
    const [code] = await exited;
    if (code !== 0) throw new Error(`ffmpeg exited with ${code}`);
  } catch (err) {
    ff.kill("SIGKILL");
    if (!res.headersSent) next(err);
    else res.destroy(err);
  }
});
```

### 419: Why does my CLI crash with EPIPE when piped to head, and how do you fix it?

When you run `mycli | head -n 5`, `head` closes its input after 5 lines. Further writes to `process.stdout` fail with `EPIPE`, which shows up as an error event on `stdout`, and an unhandled `'error'` event crashes the process with an ugly stack trace. Handle it and exit quietly, which is what Unix tools do.

```js
process.stdout.on("error", (err) => {
  if (err.code === "EPIPE") process.exit(0);
  throw err;
});

for (let i = 0; i < 1e6; i++) {
  if (!process.stdout.write(`${i}\n`)) await once(process.stdout, "drain");
}
```

Respecting `drain` also stops the process from buffering huge amounts of output in memory.

### 420: Are process.stdout writes synchronous or asynchronous?

It depends on what stdout is connected to and on the OS:

- **Files**: synchronous on all platforms.
- **TTYs (terminals)**: synchronous on Linux and macOS, asynchronous on Windows.
- **Pipes and sockets**: can be asynchronous. For example, on macOS writes to a pipe are asynchronous. The exact rules per platform are in the "A note on process I/O" section of the `process` docs.

Why it matters: if you call `process.exit()` right after writing a lot of output, data still waiting in the buffer is lost. This is easy to see:

```js
// e.js
process.stdout.write("x".repeat(1e6));
process.exit(0);
```

```bash
node e.js | wc -c    # on macOS prints 65536, not 1000000
```

Instead of `process.exit()`, set `process.exitCode` and let the process end on its own, or exit in the write callback.

```js
process.stdout.write(bigOutput, () => process.exit(1));
// or simply
process.exitCode = 1;
```

### 421: How do pino transports use worker threads, and why?

Formatting logs and sending them over the network (to a file, Elasticsearch, Loki, Datadog) takes CPU and I/O. Pino keeps the main thread work tiny: it serializes the log line to JSON quickly and writes it into a shared buffer. A **transport** runs in a separate worker thread, reads from that buffer, and does the slow part (pretty printing, batching, HTTP calls). This keeps logging from blocking request handling. On exit, pino flushes the worker so logs aren't lost, which is another reason to shut down cleanly.

```js
import pino from "pino";

const logger = pino({
  transport: {
    targets: [
      { target: "pino/file", options: { destination: "/var/log/app.log" } },
      { target: "pino-pretty", level: "debug", options: { destination: 1 } },
    ],
  },
});
```

In containers, the simplest option is often to write JSON to stdout and let the platform's log agent ship it.

### 422: How should you publish a library in 2026 to support both ESM and CommonJS users?

Since `require(esm)` works in all supported Node versions (20.19+, 22.12+ and newer), the simplest approach for many libraries is to **publish ESM only**, as long as the library doesn't use top-level await. CommonJS users can still `require()` it. Steps:

- Set `"type": "module"` and an `exports` map, plus `types`.
- Avoid top-level await in the public entry points.
- If you want `require()` to return the default export directly, add `export { x as 'module.exports' }`.
- Set `engines.node` to versions that support `require(esm)`.
- Test both `import` and `require` in CI.

If you must support older Node versions or tools that don't handle `require(esm)`, ship dual builds (with `tsup` or `tshy`) and watch for the dual package hazard (question 209).

```json
{
  "type": "module",
  "exports": {
    ".": { "types": "./dist/index.d.ts", "default": "./dist/index.js" }
  },
  "engines": { "node": ">=20.19" }
}
```

### 423: Which tsconfig settings work best with Node's native TypeScript support?

```json
{
  "compilerOptions": {
    "target": "esnext",
    "module": "nodenext",
    "moduleResolution": "nodenext",
    "allowImportingTsExtensions": true,
    "rewriteRelativeImportExtensions": true,
    "erasableSyntaxOnly": true,
    "verbatimModuleSyntax": true,
    "noEmit": true,
    "strict": true
  }
}
```

- `module: nodenext` makes TypeScript follow Node's real ESM/CJS rules.
- `allowImportingTsExtensions` lets you write `import './x.ts'`, which Node needs.
- `rewriteRelativeImportExtensions` (TS 5.7+) rewrites `.ts` to `.js` if you also compile with `tsc` for publishing.
- `erasableSyntaxOnly` (TS 5.8+) reports `enum`, `namespace` and parameter properties, which Node can't strip.
- `verbatimModuleSyntax` forces `import type` for types, so Node doesn't try to import them.
- `noEmit` because Node runs the `.ts` files directly. `tsc` is only for type checking.

### 424: What advanced features does node:test have for larger projects?

- **Module mocking**: `mock.module('specifier', { namedExports, defaultExport })`, behind `--experimental-test-module-mocks`.
- **Process isolation**: each file runs in a child process by default. `--test-isolation=none` runs everything in one process for speed.
- **Sharding**: `--test-shard=2/4` splits files across CI jobs.
- **Concurrency**: `--test-concurrency` for files, `{ concurrency: true }` for subtests in one file.
- **Snapshots**: `t.assert.snapshot(value)`, updated with `--test-update-snapshots`.
- **Reporters**: `spec`, `tap`, `dot`, `junit`, `lcov`, or your own, and several at once with `--test-reporter-destination`.
- **Global setup**: `--test-global-setup=file.js` to start shared services once (newer versions).
- **Planning**: `t.plan(n)` to make sure a certain number of assertions run.

```js
import { test, mock } from "node:test";

test("uses a mocked module", async (t) => {
  t.mock.module("./mailer.js", {
    namedExports: { send: t.mock.fn(async () => ({ id: "fake" })) },
  });
  const { signup } = await import("./signup.js");
  const result = await signup("a@b.com");
  t.assert.equal(result.mailId, "fake");
});
```

### 425: How do you test code that depends on time and timers?

Use fake timers so tests don't actually wait and are deterministic. In `node:test`, `mock.timers` can fake `setTimeout`, `setInterval`, `setImmediate`, `scheduler.wait` and `Date`. You move time forward with `tick()` or run everything with `runAll()`. You can also set the start date.

```js
import { test } from "node:test";
import assert from "node:assert/strict";

test("session expires after 30 minutes", (t) => {
  t.mock.timers.enable({
    apis: ["setTimeout", "Date"],
    now: new Date("2026-01-01T00:00:00Z"),
  });

  const session = createSession();
  assert.equal(session.isExpired(), false);

  t.mock.timers.tick(30 * 60 * 1000);
  assert.equal(session.isExpired(), true);
  assert.equal(new Date().toISOString(), "2026-01-01T00:30:00.000Z");
});
```

A cleaner design is to inject a clock (`{ now: () => Date.now() }`) into your code, so tests can pass a fake clock without patching globals.

### 426: How do you write integration tests against real databases and services?

Start real dependencies in Docker for the test run, using `testcontainers` or `docker compose`. Run migrations once, then reset data between tests (truncate tables, or wrap each test in a transaction and roll it back). This catches problems that mocks hide: SQL errors, constraint violations, transaction behavior and driver quirks.

```js
import { PostgreSqlContainer } from "@testcontainers/postgresql";
import { before, after, test } from "node:test";

let container, pool;

before(async () => {
  container = await new PostgreSqlContainer("postgres:17").start();
  pool = new pg.Pool({ connectionString: container.getConnectionUri() });
  await migrate(pool);
});

after(async () => {
  await pool.end();
  await container.stop();
});

test("creates an order", async () => {
  const order = await createOrder(pool, { userId: 1, total: 100 });
  assert.equal(order.total, 100);
});
```

### 427: How do you benchmark an HTTP server?

Use a load generator like `autocannon` (written in Node), `wrk`/`wrk2` or `k6`. Run it from a different machine (or at least different cores) than the server, warm up first, and look at latency percentiles (p50, p99), not only requests per second. Test with realistic payloads and keep-alive settings similar to production.

```bash
npx autocannon -c 100 -d 30 -p 10 http://localhost:3000/api/items
# -c connections, -d duration in seconds, -p pipelining
```

While it runs, watch the server's CPU, event loop delay and memory, and take a CPU profile to see where time goes.

### 428: How do you estimate how many instances you need?

Start from measurements: find the maximum throughput one instance can handle while keeping latency targets (for example p99 under 200 ms) using a load test. Then use Little's Law: concurrent requests in flight = arrival rate × average latency. For example, 2000 requests per second with 50 ms average latency means about 100 requests in flight at any moment. If one instance handles 500 rps within your latency target, you need at least 4 instances, plus extra room for spikes, deploys and a failed instance (often 30 to 50% headroom). Re-test after big changes, and make sure downstream systems (database, caches) can handle the total load too.

### 429: How do you expose application metrics from Node.js?

Use `prom-client` for Prometheus or the OpenTelemetry metrics SDK. Collect default process metrics (CPU, memory, event loop lag, GC, handles) plus business and HTTP metrics: request counts by route and status, latency histograms, queue sizes, external call durations. Use route templates (`/users/:id`) as labels, never raw URLs or user IDs, or you'll create too many time series.

```js
import client from "prom-client";

client.collectDefaultMetrics();

const httpDuration = new client.Histogram({
  name: "http_request_duration_seconds",
  help: "HTTP request duration",
  labelNames: ["method", "route", "status"],
  buckets: [0.01, 0.05, 0.1, 0.3, 1, 3],
});

app.use((req, res, next) => {
  const end = httpDuration.startTimer();
  res.on("finish", () =>
    end({
      method: req.method,
      route: req.route?.path ?? "unknown",
      status: res.statusCode,
    }),
  );
  next();
});

app.get("/metrics", async (req, res) => {
  res.set("Content-Type", client.register.contentType);
  res.end(await client.register.metrics());
});
```

### 430: How do you add a request ID to every log line automatically?

Combine `AsyncLocalStorage` with your logger. Create or read the request ID at the start of each request, store a child logger in the async context, and get it from there anywhere in the code. Also pass the ID to downstream calls in a header (or use OpenTelemetry trace context) so logs from different services can be linked.

```js
import { AsyncLocalStorage } from "node:async_hooks";
import { randomUUID } from "node:crypto";
import pino from "pino";

const baseLogger = pino();
const als = new AsyncLocalStorage();

export const log = () => als.getStore()?.logger ?? baseLogger;

app.use((req, res, next) => {
  const requestId = req.get("x-request-id") ?? randomUUID();
  res.setHeader("x-request-id", requestId);
  als.run({ logger: baseLogger.child({ requestId }) }, next);
});

async function chargeCard(order) {
  log().info({ orderId: order.id }, "charging card"); // includes requestId
}
```

### 431: How can you reload configuration without restarting the process?

Listen for `SIGHUP` (the traditional "reload config" signal), or watch the config file. Load the new config, validate it fully, and only then swap it in atomically. If validation fails, keep the old config and log an error. Code should always read config through a getter, not copy values at startup.

```js
let current = await loadAndValidate();

export const config = () => current;

process.on("SIGHUP", async () => {
  try {
    const next = await loadAndValidate();
    current = next;
    logger.info("config reloaded");
  } catch (err) {
    logger.error({ err }, "config reload failed, keeping old config");
  }
});
```

Some settings (ports, pool sizes) can't change at runtime safely. For those, do a rolling restart instead.

### 432: How would you build a plugin system in Node.js?

Define a clear plugin interface, load plugins by path or package name with dynamic `import()`, give each plugin a limited API object instead of access to everything, and run hooks in order with error isolation so one bad plugin doesn't break the others.

```js
// plugin interface: export default { name, setup(api) }
export async function loadPlugins(specifiers, api) {
  const plugins = [];
  for (const spec of specifiers) {
    const mod = await import(spec);
    const plugin = mod.default;
    if (typeof plugin?.setup !== "function")
      throw new Error(`${spec} is not a valid plugin`);
    await plugin.setup(api);
    plugins.push(plugin);
  }
  return plugins;
}

const hooks = new Map();
const api = {
  on(hook, fn) {
    (hooks.get(hook) ?? hooks.set(hook, []).get(hook)).push(fn);
  },
  logger,
};

async function runHook(name, payload) {
  for (const fn of hooks.get(name) ?? []) {
    try {
      payload = (await fn(payload)) ?? payload;
    } catch (err) {
      logger.error({ err, hook: name }, "plugin failed");
    }
  }
  return payload;
}
```

Plugins still run with full process permissions. For untrusted plugins you need process or VM-level isolation.

### 433: How do you do dependency injection in Node.js without a framework?

The simplest form is passing dependencies as arguments to factory functions, and wiring everything together in one place (the "composition root"). This makes code easy to test, because tests pass fakes. Frameworks like NestJS or libraries like `awilix` automate this for larger apps, but plain functions are often enough.

```js
// services/user-service.js
export function createUserService({ db, mailer, clock = Date }) {
  return {
    async register(email) {
      const user = await db.users.insert({ email, createdAt: clock.now() });
      await mailer.send(email, "Welcome!");
      return user;
    },
  };
}

// main.js (composition root)
const db = createDb(config.databaseUrl);
const mailer = createMailer(config.smtp);
const userService = createUserService({ db, mailer });
const app = createApp({ userService });

// test
const svc = createUserService({ db: fakeDb, mailer: { send: async () => {} } });
```

### 434: How would you structure a large Node.js backend?

Group code by feature (domain) rather than by technical type, and keep layers with clear directions of dependency:

- **Transport layer** (HTTP routes, queue consumers, CLI): parses input, validates, calls services, formats output. No business logic.
- **Service / domain layer**: business rules. Doesn't know about HTTP or SQL details.
- **Data access layer** (repositories): talks to databases and external APIs.

```
src/
  modules/
    orders/
      orders.routes.js
      orders.service.js
      orders.repository.js
      orders.schema.js
      orders.test.js
    users/
  shared/
    db.js
    logger.js
    errors.js
  app.js
  server.js
```

Keep `app.js` (building the app) separate from `server.js` (listening on a port), so tests can create the app without starting a server. Avoid circular imports between modules. Let them talk through services or events.

### 435: How should you handle money and decimal numbers in Node.js?

JavaScript numbers are binary floating point, so `0.1 + 0.2 !== 0.3`. Never use them for money calculations. Options:

- Store and calculate amounts as **integers in the smallest unit** (cents), and convert only for display.
- Use `BigInt` for very large integer amounts.
- Use a decimal library (`decimal.js`, `big.js`, `dinero.js`) when you need fractional math like interest or currency conversion with specific rounding rules.
- In the database, use `DECIMAL`/`NUMERIC` types. Drivers usually return them as strings to avoid precision loss, so don't convert them to `Number` by accident.
- Format with `Intl.NumberFormat` and the right currency.

```js
0.1 + 0.2; // 0.30000000000000004
const totalCents = 1999 + 1; // 2000
new Intl.NumberFormat("en-US", { style: "currency", currency: "USD" }).format(
  totalCents / 100,
); // '$20.00'
```

### 436: How do you read and write binary data formats in Node.js?

Use Buffer's read/write methods or a `DataView`. Pay attention to byte order (big-endian vs little-endian), signed vs unsigned, and offsets.

```js
// a header: 2-byte type (uint16 BE), 4-byte length (uint32 BE), 8-byte timestamp (int64 BE)
function encodeHeader(type, length, ts) {
  const buf = Buffer.alloc(14);
  buf.writeUInt16BE(type, 0);
  buf.writeUInt32BE(length, 2);
  buf.writeBigInt64BE(BigInt(ts), 6);
  return buf;
}

function decodeHeader(buf) {
  return {
    type: buf.readUInt16BE(0),
    length: buf.readUInt32BE(2),
    ts: Number(buf.readBigInt64BE(6)),
  };
}

// the same with DataView, works in browsers too
const view = new DataView(arrayBuffer);
const type = view.getUint16(0, false); // false = big-endian
```

### 437: How do you handle message framing over a TCP socket?

TCP is a byte stream, not a message stream. One `'data'` event can contain half a message, or several messages at once. You need framing, for example a length prefix: each message starts with 4 bytes for its length. Keep a buffer, add incoming chunks, and take complete messages out while there are enough bytes.

```js
import net from "node:net";

function frame(obj) {
  const body = Buffer.from(JSON.stringify(obj));
  const header = Buffer.alloc(4);
  header.writeUInt32BE(body.length);
  return Buffer.concat([header, body]);
}

net
  .createServer((socket) => {
    let buffer = Buffer.alloc(0);

    socket.on("data", (chunk) => {
      buffer = Buffer.concat([buffer, chunk]);
      while (buffer.length >= 4) {
        const len = buffer.readUInt32BE(0);
        if (len > 1_000_000)
          return socket.destroy(new Error("Message too large"));
        if (buffer.length < 4 + len) break; // wait for more data
        const msg = JSON.parse(buffer.subarray(4, 4 + len).toString());
        buffer = buffer.subarray(4 + len);
        socket.write(frame({ echo: msg }));
      }
    });
  })
  .listen(5000);
```

Always set a maximum message size, otherwise a client can make you buffer forever. Other framing methods are delimiters (like newlines in NDJSON) and fixed-size messages.

### 438: How do you write a simple HTTP reverse proxy with streams?

Forward the incoming request to the target with `http.request`, pipe the request body to it, and pipe the response back, copying status and headers. Handle errors on both sides and abort the upstream request if the client disconnects.

```js
import http from "node:http";
import { pipeline } from "node:stream/promises";

const TARGET = { host: "127.0.0.1", port: 4000 };

http
  .createServer((req, res) => {
    const upstream = http.request({
      ...TARGET,
      method: req.method,
      path: req.url,
      headers: {
        ...req.headers,
        host: `${TARGET.host}:${TARGET.port}`,
        "x-forwarded-for": req.socket.remoteAddress,
      },
    });

    upstream.on("response", (up) => {
      res.writeHead(up.statusCode, up.headers);
      pipeline(up, res).catch(() => {});
    });
    upstream.on("error", () => {
      if (!res.headersSent) res.writeHead(502);
      res.end();
    });
    res.on("close", () => upstream.destroy());

    pipeline(req, upstream).catch(() => {});
  })
  .listen(8080);
```

A real proxy also removes hop-by-hop headers (`connection`, `keep-alive`, `transfer-encoding`, `upgrade`), handles WebSocket upgrades and sets timeouts. Libraries like `http-proxy-3` or `@fastify/http-proxy` do this.

### 439: How does await work internally, and why did it get faster?

An `async` function is like a generator driven by promises. At `await v`, V8 wraps `v` in a promise, attaches internal resume handlers to it, suspends the function and returns. When the promise settles, the handlers schedule a microtask that resumes the function with the value or throws the error into it. Older V8 versions created an extra "throwaway" promise and needed three microtask ticks per `await`. Since V8 7.2 (Node 12), awaiting a native promise uses it directly and takes only one tick, which made `async/await` faster than many hand-written `.then` chains. One effect: `await somePromise` and `return somePromise` from an async function can resolve in a different number of ticks, which can change ordering in tricky tests.

### 440: What are DisposableStack and AsyncDisposableStack?

They collect several cleanup actions and run them in reverse order when the stack is disposed, even if one of them throws. They are useful when you open resources step by step and want all of them cleaned up correctly whether setup finishes or fails. Available in Node 24 and newer.

```js
async function startApp() {
  await using stack = new AsyncDisposableStack();

  const db = stack.use(await connectDb()); // db must have Symbol.asyncDispose
  const cache = await connectRedis();
  stack.defer(async () => cache.quit()); // any cleanup function
  const server = await startServer({ db, cache });
  stack.defer(() => new Promise((r) => server.close(r)));

  // Setup succeeded, so keep everything open and return a cleanup handle
  const resources = stack.move();
  return { server, close: () => resources.disposeAsync() };
}
```

If any step throws, `await using` disposes everything collected so far. If two cleanup steps throw, you get a `SuppressedError` that keeps both errors.

### 441: What is the Node.js stability index, and how do features become stable?

Every API in the Node docs has a stability level:

- **0 - Deprecated**: may be removed. Deprecations go from documentation-only, to runtime warnings, to end-of-life (removed).
- **1 - Experimental**: may change or be removed. Split into 1.0 (early development), 1.1 (active development) and 1.2 (release candidate).
- **2 - Stable**: compatibility is a priority.
- **3 - Legacy**: still supported but not recommended, for example `url.parse` or `querystring`.

Features usually land behind a flag in a Current release, lose the flag after feedback, get backported to LTS lines, and become stable later. Experimental features print a warning (`ExperimentalWarning`). Check the docs for your exact version before relying on one.

### 442: How do v8.serialize and the "advanced" IPC serialization work?

`v8.serialize()` turns a value into a Buffer using the same structured clone format as `postMessage`, and `v8.deserialize()` turns it back. It supports more types than JSON: `Map`, `Set`, `Date`, `RegExp`, `BigInt`, typed arrays, `undefined`, circular references and errors. `child_process.fork()` with `serialization: 'advanced'` uses this format for IPC instead of JSON, so you can send those types between processes.

```js
import v8 from "node:v8";

const data = { when: new Date(), tags: new Set(["a"]), big: 10n };
const buf = v8.serialize(data);
const copy = v8.deserialize(buf);
console.log(copy.tags.has("a")); // true

const child = fork("./child.js", { serialization: "advanced" });
child.send({ ids: new Set([1, 2]) });
```

The format can change between V8 versions, so don't use it for long-term storage or between different Node versions.

### 443: How does Node's model compare to thread-per-request servers?

A thread-per-request server (classic Java servlets, Apache prefork) gives each request its own thread, which blocks on I/O. It's simple to write, but each thread costs memory (often 1 MB of stack) and context switches, so thousands of idle connections are expensive. Node uses one thread and an event loop: waiting connections cost only a small object, so it handles many concurrent I/O-bound connections cheaply (the C10K problem). The trade-off: any CPU-heavy or blocking code delays every request, and one process uses one core for JavaScript, so you scale out with more processes. Modern platforms are moving toward a middle ground (Java virtual threads, Go goroutines), but the trade-offs are similar.

### 444: How does Node parse HTTP requests?

Node uses **llhttp**, a parser written in TypeScript that is compiled to C. It is a state machine that reads raw bytes from the socket and calls back for the method, URL, each header, body chunks and message end. It's much faster than the older `http_parser` and strict by default (see question 394). Node's `_http_server` builds `IncomingMessage` objects from these callbacks, and the body is pushed into the request's readable stream as it arrives. Limits like `maxHeaderSize` and `headersTimeout` are enforced around the parser. `undici` (used by `fetch`) also uses llhttp, compiled to WebAssembly.

### 445: How would you design a reliable webhook delivery system in Node.js?

- When an event happens, write a delivery job to a queue or outbox table (don't call the customer's URL inside the request that caused the event).
- Workers send the HTTP request with a short timeout, a signature header (HMAC of the body with a per-customer secret plus a timestamp) and a unique event ID for idempotency.
- Treat any 2xx as success. Retry other results with exponential backoff and jitter for hours or days, then mark the delivery as failed and notify the customer.
- Limit concurrency per customer so one slow endpoint doesn't block others.
- Protect against SSRF (customers choose the URLs, see question 363).
- Store delivery attempts for debugging, and offer a "resend" button.

```js
async function deliver(job) {
  const body = JSON.stringify(job.event);
  const ts = Math.floor(Date.now() / 1000);
  const sig = createHmac("sha256", job.secret)
    .update(`${ts}.${body}`)
    .digest("hex");

  const res = await fetch(job.url, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      "X-Signature": `t=${ts},v1=${sig}`,
      "X-Event-Id": job.event.id,
    },
    body,
    signal: AbortSignal.timeout(10_000),
    redirect: "manual",
  });
  if (!res.ok) throw new Error(`Webhook failed with ${res.status}`);
}
```

### 446: How would you design a real-time chat backend in Node.js?

- **Connections**: WebSocket servers (`ws` or Socket.IO) behind a load balancer that supports upgrades. Authenticate during the upgrade using a token.
- **Fan-out across instances**: each instance subscribes to Redis pub/sub (or NATS) channels for the rooms its clients are in. A message sent to one instance is published and delivered by all instances that have members of that room.
- **Persistence**: save messages to a database first (with an ID and timestamp), then broadcast. Clients that reconnect ask for messages after the last ID they saw.
- **Presence and typing indicators**: short-lived keys in Redis with TTLs.
- **Backpressure**: check `socket.bufferedAmount` and drop or disconnect slow clients instead of buffering forever.
- **Heartbeats**: ping/pong to detect dead connections.
- **Scaling**: watch the number of connections and event loop delay per instance, and drain connections gracefully on deploys (clients reconnect to other instances).

### 447: What is the N+1 query problem, and how do you solve it in Node?

N+1 happens when you load a list (1 query) and then run one query per item to load related data (N queries). It's common with ORMs and GraphQL resolvers. Fixes: use joins or `IN (...)` queries to load related data in one go, use the ORM's eager loading (`include`), or in GraphQL use **DataLoader**, which collects all keys requested in the same tick and loads them with one batched query.

```js
import DataLoader from "dataloader";

const authorLoader = new DataLoader(async (ids) => {
  const rows = await db.query("SELECT * FROM authors WHERE id = ANY($1)", [
    ids,
  ]);
  const byId = new Map(rows.map((r) => [r.id, r]));
  return ids.map((id) => byId.get(id) ?? null); // same order as ids
});

// resolver: called once per post, but only one SQL query runs
const resolvers = {
  Post: { author: (post) => authorLoader.load(post.authorId) },
};
```

Create a new DataLoader per request, so its cache doesn't leak data between users.

### 448: Why should you always consume or cancel a fetch response body?

With undici (Node's `fetch`), the connection is only returned to the pool after the response body has been fully read or cancelled. If you check `res.status` and ignore the body, the connection stays busy until the garbage collector cleans it up, which can take a long time. Under load this uses up the connection pool, and later requests wait or time out.

```js
const res = await fetch(url);
if (!res.ok) {
  await res.body?.cancel(); // release the connection
  throw new Error(`HTTP ${res.status}`);
}
const data = await res.json(); // reading the body also releases it

// HEAD-like checks
const r = await fetch(url, { method: "HEAD" });
```

The same applies to `http.get`: call `res.resume()` if you don't need the data.

### 449: What is "releasing Zalgo", and how do you avoid it?

"Zalgo" is when a function sometimes calls its callback synchronously and sometimes asynchronously, for example sync when the value is cached and async when it's not. Code calling it then behaves differently depending on timing, which causes very confusing bugs. The rule: an API should be always sync or always async. In callback APIs, defer the cached case with `process.nextTick` or `queueMicrotask`. With promises this is handled for you, because `.then` callbacks always run asynchronously.

```js
// bad
function getUser(id, cb) {
  if (cache.has(id)) return cb(null, cache.get(id)); // sync
  db.load(id, cb); // async
}

// good
function getUser(id, cb) {
  if (cache.has(id)) return process.nextTick(cb, null, cache.get(id));
  db.load(id, cb);
}
```

The same idea is why Node emits errors from constructors with `nextTick`: it gives the caller a chance to attach an `'error'` listener first.

### 450: What are the most important changes in recent Node.js versions (22, 24 and newer)?

**Node 22 (LTS)**

- `require()` of ES modules without a flag (from 22.12).
- Built-in `WebSocket` client, `--watch` stable, `node --run`.
- `fs.glob`, `node:sqlite` (22.5+, no flag from 22.13).
- Type stripping for TypeScript (no flag from 22.18).
- `module.enableCompileCache()`, sync module hooks (`registerHooks`, 22.15+).
- V8 12.4: `Array.fromAsync`, `Set` methods, iterator helpers, `Promise.withResolvers`.
- Default stream `highWaterMark` raised to 64 KB.

**Node 24 (LTS since October 2025)**

- V8 13.6: `using` / `await using`, `RegExp.escape`, `Float16Array`, `Error.isError`, `Promise.try`.
- `AsyncLocalStorage` uses `AsyncContextFrame` by default.
- `URLPattern` available globally.
- Permission model under `--permission` (no longer experimental).
- npm 11, test runner waits for subtests automatically.
- `url.parse()` and some legacy APIs move further toward removal.

**Node 25 and newer (Current)**

- Newer V8 with faster `JSON.stringify` and `Uint8Array` base64/hex methods.
- Web Storage (`localStorage`) enabled by default (needs `--localstorage-file` to persist).
- `--allow-net` for the permission model.
- Corepack no longer shipped with Node.
- Removal of long-deprecated APIs like `SlowBuffer`.

Always check the official changelog for the exact version you use, since features keep moving from experimental to stable and are backported to LTS lines.
