# Full Stack Web App Optimization and Debugging Interview Questions and Answers

_Last updated: October 28, 2026_

450 questions split into three levels: 150 easy, 150 moderate and 150 advanced. Each level covers the same ten subject areas, from the browser all the way down to the database, the operating system and the cloud.

The answers target current versions of the platform: evergreen Chrome and Chrome DevTools, modern HTML, CSS, JavaScript and DOM APIs, and Node.js 22/24 LTS. Where a feature is recent or Chrome-only, the answer says so.

## Table of Contents

- [Easy Questions (1-150)](#easy-questions-1-150)
  - [Web Platform Fundamentals (1-15)](#easy-web-platform-fundamentals-1-15)
  - [Google Chrome and Browser Internals (16-30)](#easy-google-chrome-and-browser-internals-16-30)
  - [Browser Developer and Performance Tools (31-45)](#easy-browser-developer-and-performance-tools-31-45)
  - [JavaScript Runtime and Server-Side Fundamentals (46-60)](#easy-javascript-runtime-and-server-side-fundamentals-46-60)
  - [Networking and Web Protocols (61-75)](#easy-networking-and-web-protocols-61-75)
  - [Databases and Data Access (76-90)](#easy-databases-and-data-access-76-90)
  - [Operating Systems and Server Resources (91-105)](#easy-operating-systems-and-server-resources-91-105)
  - [Cloud Infrastructure and Delivery (106-120)](#easy-cloud-infrastructure-and-delivery-106-120)
  - [Observability, Profiling and Reliability (121-135)](#easy-observability-profiling-and-reliability-121-135)
  - [Web Performance Standards and Metrics (136-150)](#easy-web-performance-standards-and-metrics-136-150)
- [Moderate Questions (151-300)](#moderate-questions-151-300)
  - [Web Platform Fundamentals (151-165)](#moderate-web-platform-fundamentals-151-165)
  - [Google Chrome and Browser Internals (166-180)](#moderate-google-chrome-and-browser-internals-166-180)
  - [Browser Developer and Performance Tools (181-195)](#moderate-browser-developer-and-performance-tools-181-195)
  - [JavaScript Runtime and Server-Side Fundamentals (196-210)](#moderate-javascript-runtime-and-server-side-fundamentals-196-210)
  - [Networking and Web Protocols (211-225)](#moderate-networking-and-web-protocols-211-225)
  - [Databases and Data Access (226-240)](#moderate-databases-and-data-access-226-240)
  - [Operating Systems and Server Resources (241-255)](#moderate-operating-systems-and-server-resources-241-255)
  - [Cloud Infrastructure and Delivery (256-270)](#moderate-cloud-infrastructure-and-delivery-256-270)
  - [Observability, Profiling and Reliability (271-285)](#moderate-observability-profiling-and-reliability-271-285)
  - [Web Performance Standards and Metrics (286-300)](#moderate-web-performance-standards-and-metrics-286-300)
- [Advanced Questions (301-450)](#advanced-questions-301-450)
  - [Web Platform Fundamentals (301-315)](#advanced-web-platform-fundamentals-301-315)
  - [Google Chrome and Browser Internals (316-330)](#advanced-google-chrome-and-browser-internals-316-330)
  - [Browser Developer and Performance Tools (331-345)](#advanced-browser-developer-and-performance-tools-331-345)
  - [JavaScript Runtime and Server-Side Fundamentals (346-360)](#advanced-javascript-runtime-and-server-side-fundamentals-346-360)
  - [Networking and Web Protocols (361-375)](#advanced-networking-and-web-protocols-361-375)
  - [Databases and Data Access (376-390)](#advanced-databases-and-data-access-376-390)
  - [Operating Systems and Server Resources (391-405)](#advanced-operating-systems-and-server-resources-391-405)
  - [Cloud Infrastructure and Delivery (406-420)](#advanced-cloud-infrastructure-and-delivery-406-420)
  - [Observability, Profiling and Reliability (421-435)](#advanced-observability-profiling-and-reliability-421-435)
  - [Web Performance Standards and Metrics (436-450)](#advanced-web-performance-standards-and-metrics-436-450)

### Easy Questions (1-150)

- [1: What is semantic HTML, and does it have anything to do with performance?](#1-what-is-semantic-html-and-does-it-have-anything-to-do-with-performance)
- [2: Why does DOM size matter?](#2-why-does-dom-size-matter)
- [3: What does `<link rel="preload">` do?](#3-what-does-link-relpreload-do)
- [4: What is the difference between `preconnect` and `dns-prefetch`?](#4-what-is-the-difference-between-preconnect-and-dns-prefetch)
- [5: How does native lazy loading work?](#5-how-does-native-lazy-loading-work)
- [6: Why is CSS considered render-blocking?](#6-why-is-css-considered-render-blocking)
- [7: What is critical CSS?](#7-what-is-critical-css)
- [8: Which CSS properties are cheap to animate?](#8-which-css-properties-are-cheap-to-animate)
- [9: What is the event loop in the browser?](#9-what-is-the-event-loop-in-the-browser)
- [10: What is the difference between debouncing and throttling?](#10-what-is-the-difference-between-debouncing-and-throttling)
- [11: What is a Web Worker?](#11-what-is-a-web-worker)
- [12: What is event delegation?](#12-what-is-event-delegation)
- [13: What is layout thrashing?](#13-what-is-layout-thrashing)
- [14: What is `IntersectionObserver` used for?](#14-what-is-intersectionobserver-used-for)
- [15: When would you pick SVG over Canvas, or the other way around?](#15-when-would-you-pick-svg-over-canvas-or-the-other-way-around)
- [16: What is Chrome's multi-process architecture?](#16-what-is-chromes-multi-process-architecture)
- [17: What does a renderer process do?](#17-what-does-a-renderer-process-do)
- [18: What is site isolation?](#18-what-is-site-isolation)
- [19: What is the difference between Chromium and Chrome?](#19-what-is-the-difference-between-chromium-and-chrome)
- [20: What is Blink?](#20-what-is-blink)
- [21: What is V8?](#21-what-is-v8)
- [22: What are the main steps of the browser rendering pipeline?](#22-what-are-the-main-steps-of-the-browser-rendering-pipeline)
- [23: What is the difference between layout (reflow) and repaint?](#23-what-is-the-difference-between-layout-reflow-and-repaint)
- [24: What is compositing?](#24-what-is-compositing)
- [25: What is the difference between the memory cache and the disk cache in Chrome?](#25-what-is-the-difference-between-the-memory-cache-and-the-disk-cache-in-chrome)
- [26: What is the Cache Storage API?](#26-what-is-the-cache-storage-api)
- [27: What is a long task?](#27-what-is-a-long-task)
- [28: What is the difference between microtasks and macrotasks?](#28-what-is-the-difference-between-microtasks-and-macrotasks)
- [29: Why do timers run slower in background tabs?](#29-why-do-timers-run-slower-in-background-tabs)
- [30: How can you see which tab is using the most resources in Chrome?](#30-how-can-you-see-which-tab-is-using-the-most-resources-in-chrome)
- [31: What is the Chrome DevTools Performance panel used for?](#31-what-is-the-chrome-devtools-performance-panel-used-for)
- [32: What does the Network panel show?](#32-what-does-the-network-panel-show)
- [33: What is the Coverage tab?](#33-what-is-the-coverage-tab)
- [34: What can you do with the Rendering tab?](#34-what-can-you-do-with-the-rendering-tab)
- [35: What is the Application panel for?](#35-what-is-the-application-panel-for)
- [36: What is Lighthouse?](#36-what-is-lighthouse)
- [37: What categories does Lighthouse check?](#37-what-categories-does-lighthouse-check)
- [38: What is PageSpeed Insights and what is the difference between its field data and lab data?](#38-what-is-pagespeed-insights-and-what-is-the-difference-between-its-field-data-and-lab-data)
- [39: What is WebPageTest?](#39-what-is-webpagetest)
- [40: What is the Chrome UX Report (CrUX)?](#40-what-is-the-chrome-ux-report-crux)
- [41: How do you measure how long your own code takes in the browser?](#41-how-do-you-measure-how-long-your-own-code-takes-in-the-browser)
- [42: What does the Navigation Timing API give you?](#42-what-does-the-navigation-timing-api-give-you)
- [43: Why should you use network and CPU throttling in DevTools?](#43-why-should-you-use-network-and-cpu-throttling-in-devtools)
- [44: What is Perfetto?](#44-what-is-perfetto)
- [45: How can you debug a Node.js app with Chrome DevTools?](#45-how-can-you-debug-a-nodejs-app-with-chrome-devtools)
- [46: What is the Node.js event loop?](#46-what-is-the-nodejs-event-loop)
- [47: Why is Node.js good at handling I/O-heavy workloads?](#47-why-is-nodejs-good-at-handling-io-heavy-workloads)
- [48: What is libuv?](#48-what-is-libuv)
- [49: What does "blocking the event loop" mean? Give an example.](#49-what-does-blocking-the-event-loop-mean-give-an-example)
- [50: What are streams in Node.js?](#50-what-are-streams-in-nodejs)
- [51: What is backpressure?](#51-what-is-backpressure)
- [52: What are worker threads in Node.js?](#52-what-are-worker-threads-in-nodejs)
- [53: What is the `cluster` module?](#53-what-is-the-cluster-module)
- [54: What is the difference between promises and async/await?](#54-what-is-the-difference-between-promises-and-asyncawait)
- [55: What is the difference between `Promise.all`, `Promise.allSettled`, `Promise.race` and `Promise.any`?](#55-what-is-the-difference-between-promiseall-promiseallsettled-promiserace-and-promiseany)
- [56: What is the difference between `process.nextTick` and `setImmediate`?](#56-what-is-the-difference-between-processnexttick-and-setimmediate)
- [57: How are browser Web Workers and Node.js worker threads similar and different?](#57-how-are-browser-web-workers-and-nodejs-worker-threads-similar-and-different)
- [58: What are Deno and Bun?](#58-what-are-deno-and-bun)
- [59: How do you check memory usage in a Node.js process?](#59-how-do-you-check-memory-usage-in-a-nodejs-process)
- [60: How should a Node.js server shut down gracefully?](#60-how-should-a-nodejs-server-shut-down-gracefully)
- [61: What is the main difference between HTTP/1.1 and HTTP/2?](#61-what-is-the-main-difference-between-http11-and-http2)
- [62: What is HTTP/3?](#62-what-is-http3)
- [63: Why does HTTPS add latency, and how does TLS 1.3 help?](#63-why-does-https-add-latency-and-how-does-tls-13-help)
- [64: What is the difference between TCP and UDP?](#64-what-is-the-difference-between-tcp-and-udp)
- [65: What is a DNS lookup, and what does TTL mean?](#65-what-is-a-dns-lookup-and-what-does-ttl-mean)
- [66: What is a CDN?](#66-what-is-a-cdn)
- [67: What is the difference between WebSockets and Server-Sent Events?](#67-what-is-the-difference-between-websockets-and-server-sent-events)
- [68: What is the difference between Gzip and Brotli?](#68-what-is-the-difference-between-gzip-and-brotli)
- [69: What does the `Cache-Control` header do?](#69-what-does-the-cache-control-header-do)
- [70: What is an ETag and how does it produce a 304 response?](#70-what-is-an-etag-and-how-does-it-produce-a-304-response)
- [71: What are `Last-Modified` and `If-Modified-Since`?](#71-what-are-last-modified-and-if-modified-since)
- [72: What is the difference between `preload` and `prefetch`?](#72-what-is-the-difference-between-preload-and-prefetch)
- [73: What is HTTP keep-alive?](#73-what-is-http-keep-alive)
- [74: What is RTT and why does it matter for web performance?](#74-what-is-rtt-and-why-does-it-matter-for-web-performance)
- [75: What is head-of-line blocking?](#75-what-is-head-of-line-blocking)
- [76: What is a database index?](#76-what-is-a-database-index)
- [77: What is a query plan?](#77-what-is-a-query-plan)
- [78: What is the difference between `EXPLAIN` and `EXPLAIN ANALYZE` in PostgreSQL?](#78-what-is-the-difference-between-explain-and-explain-analyze-in-postgresql)
- [79: What is a database transaction?](#79-what-is-a-database-transaction)
- [80: What is the N+1 query problem?](#80-what-is-the-n1-query-problem)
- [81: What is a database connection pool?](#81-what-is-a-database-connection-pool)
- [82: Why is `SELECT *` often a bad idea?](#82-why-is-select--often-a-bad-idea)
- [83: What is the difference between offset and cursor pagination?](#83-what-is-the-difference-between-offset-and-cursor-pagination)
- [84: What is Redis commonly used for?](#84-what-is-redis-commonly-used-for)
- [85: What does TTL mean in Redis?](#85-what-does-ttl-mean-in-redis)
- [86: What is the cache-aside pattern?](#86-what-is-the-cache-aside-pattern)
- [87: How do you check if a MongoDB query uses an index?](#87-how-do-you-check-if-a-mongodb-query-uses-an-index)
- [88: What is a projection in MongoDB?](#88-what-is-a-projection-in-mongodb)
- [89: What is VACUUM in PostgreSQL?](#89-what-is-vacuum-in-postgresql)
- [90: What is an ORM, and what performance costs can it add?](#90-what-is-an-orm-and-what-performance-costs-can-it-add)
- [91: What is the difference between a process and a thread?](#91-what-is-the-difference-between-a-process-and-a-thread)
- [92: What is a file descriptor, and what does `EMFILE` mean?](#92-what-is-a-file-descriptor-and-what-does-emfile-mean)
- [93: What is a system call?](#93-what-is-a-system-call)
- [94: What is the difference between CPU utilization and load average?](#94-what-is-the-difference-between-cpu-utilization-and-load-average)
- [95: What is the difference between RSS and heap memory?](#95-what-is-the-difference-between-rss-and-heap-memory)
- [96: What is a memory leak?](#96-what-is-a-memory-leak)
- [97: What is swap, and why is it bad for server performance?](#97-what-is-swap-and-why-is-it-bad-for-server-performance)
- [98: What is I/O wait?](#98-what-is-io-wait)
- [99: What is a socket and a port?](#99-what-is-a-socket-and-a-port)
- [100: What are `top` and `htop` used for?](#100-what-are-top-and-htop-used-for)
- [101: What happens when a Docker container hits its memory limit?](#101-what-happens-when-a-docker-container-hits-its-memory-limit)
- [102: How do CPU limits work in Docker?](#102-how-do-cpu-limits-work-in-docker)
- [103: What is the difference between SIGTERM and SIGKILL?](#103-what-is-the-difference-between-sigterm-and-sigkill)
- [104: What does the `ss` command do?](#104-what-does-the-ss-command-do)
- [105: What is `ulimit`?](#105-what-is-ulimit)
- [106: What is the difference between vertical and horizontal scaling?](#106-what-is-the-difference-between-vertical-and-horizontal-scaling)
- [107: What is a load balancer?](#107-what-is-a-load-balancer)
- [108: What is the difference between an AWS ALB and an NLB?](#108-what-is-the-difference-between-an-aws-alb-and-an-nlb)
- [109: What is autoscaling?](#109-what-is-autoscaling)
- [110: What CloudWatch metrics would you look at first when an API on AWS gets slow?](#110-what-cloudwatch-metrics-would-you-look-at-first-when-an-api-on-aws-gets-slow)
- [111: What is a cache hit ratio?](#111-what-is-a-cache-hit-ratio)
- [112: How do CloudFront and Cloudflare cache content at the edge?](#112-how-do-cloudfront-and-cloudflare-cache-content-at-the-edge)
- [113: Why serve static files from S3 instead of your app server?](#113-why-serve-static-files-from-s3-instead-of-your-app-server)
- [114: What is a reverse proxy?](#114-what-is-a-reverse-proxy)
- [115: How do you turn on compression in Nginx?](#115-how-do-you-turn-on-compression-in-nginx)
- [116: What is a health check?](#116-what-is-a-health-check)
- [117: What are resource requests and limits in Kubernetes?](#117-what-are-resource-requests-and-limits-in-kubernetes)
- [118: Why should CI pipelines cache dependencies?](#118-why-should-ci-pipelines-cache-dependencies)
- [119: What is bundle analysis, and why run it in CI?](#119-what-is-bundle-analysis-and-why-run-it-in-ci)
- [120: What is Infrastructure as Code, and how does it help with performance work?](#120-what-is-infrastructure-as-code-and-how-does-it-help-with-performance-work)
- [121: What is the difference between latency and throughput?](#121-what-is-the-difference-between-latency-and-throughput)
- [122: What are latency percentiles, and why are they better than averages?](#122-what-are-latency-percentiles-and-why-are-they-better-than-averages)
- [123: What is error rate?](#123-what-is-error-rate)
- [124: What is saturation?](#124-what-is-saturation)
- [125: What is distributed tracing?](#125-what-is-distributed-tracing)
- [126: What is OpenTelemetry?](#126-what-is-opentelemetry)
- [127: What is a span?](#127-what-is-a-span)
- [128: What is structured logging?](#128-what-is-structured-logging)
- [129: What is APM?](#129-what-is-apm)
- [130: What is a flame graph?](#130-what-is-a-flame-graph)
- [131: What is load testing? Show a simple example.](#131-what-is-load-testing-show-a-simple-example)
- [132: What is the difference between a stress test and a soak test?](#132-what-is-the-difference-between-a-stress-test-and-a-soak-test)
- [133: What is autocannon?](#133-what-is-autocannon)
- [134: What is the difference between an SLI, an SLO and an SLA?](#134-what-is-the-difference-between-an-sli-an-slo-and-an-sla)
- [135: What is an error budget?](#135-what-is-an-error-budget)
- [136: What are the Core Web Vitals and their "good" thresholds?](#136-what-are-the-core-web-vitals-and-their-good-thresholds)
- [137: What is LCP?](#137-what-is-lcp)
- [138: What is INP?](#138-what-is-inp)
- [139: What is CLS?](#139-what-is-cls)
- [140: What is First Contentful Paint (FCP)?](#140-what-is-first-contentful-paint-fcp)
- [141: What is Time to First Byte (TTFB)?](#141-what-is-time-to-first-byte-ttfb)
- [142: What is Speed Index?](#142-what-is-speed-index)
- [143: What is Total Blocking Time (TBT)?](#143-what-is-total-blocking-time-tbt)
- [144: What is the critical rendering path?](#144-what-is-the-critical-rendering-path)
- [145: What is the difference between `async` and `defer` on script tags?](#145-what-is-the-difference-between-async-and-defer-on-script-tags)
- [146: What does `font-display: swap` do?](#146-what-does-font-display-swap-do)
- [147: What are WebP and AVIF?](#147-what-are-webp-and-avif)
- [148: What do `srcset` and `sizes` do?](#148-what-do-srcset-and-sizes-do)
- [149: What is tree shaking?](#149-what-is-tree-shaking)
- [150: What is Real User Monitoring (RUM)?](#150-what-is-real-user-monitoring-rum)

### Moderate Questions (151-300)

- [151: What does `content-visibility: auto` do, and when should you use it?](#151-what-does-content-visibility-auto-do-and-when-should-you-use-it)
- [152: What is CSS containment (`contain`) and how does it help performance?](#152-what-is-css-containment-contain-and-how-does-it-help-performance)
- [153: What is the `fetchpriority` attribute?](#153-what-is-the-fetchpriority-attribute)
- [154: What is `MutationObserver` and what are its performance pitfalls?](#154-what-is-mutationobserver-and-what-are-its-performance-pitfalls)
- [155: How do you insert many DOM elements efficiently?](#155-how-do-you-insert-many-dom-elements-efficiently)
- [156: When should you use `requestAnimationFrame`?](#156-when-should-you-use-requestanimationframe)
- [157: How can you use the Streams API with `fetch` in the browser?](#157-how-can-you-use-the-streams-api-with-fetch-in-the-browser)
- [158: What caching strategies can a Service Worker use?](#158-what-caching-strategies-can-a-service-worker-use)
- [159: Why can `localStorage` hurt performance, and when should you use IndexedDB instead?](#159-why-can-localstorage-hurt-performance-and-when-should-you-use-indexeddb-instead)
- [160: How do you cancel a `fetch` request, and why does it matter for performance?](#160-how-do-you-cancel-a-fetch-request-and-why-does-it-matter-for-performance)
- [161: What are passive event listeners?](#161-what-are-passive-event-listeners)
- [162: Does CSS selector performance still matter?](#162-does-css-selector-performance-still-matter)
- [163: What is `will-change`, and how can it be overused?](#163-what-is-will-change-and-how-can-it-be-overused)
- [164: What are transferable objects, and why do they matter for Web Workers?](#164-what-are-transferable-objects-and-why-do-they-matter-for-web-workers)
- [165: How do you make Canvas rendering faster?](#165-how-do-you-make-canvas-rendering-faster)
- [166: Why can scrolling stay smooth even when the main thread is busy?](#166-why-can-scrolling-stay-smooth-even-when-the-main-thread-is-busy)
- [167: What makes style recalculation expensive?](#167-what-makes-style-recalculation-expensive)
- [168: What is the back/forward cache, and what stops a page from using it?](#168-what-is-the-backforward-cache-and-what-stops-a-page-from-using-it)
- [169: How do storage quotas work in Chrome?](#169-how-do-storage-quotas-work-in-chrome)
- [170: What is HTTP cache partitioning, and how did it change CDN caching benefits?](#170-what-is-http-cache-partitioning-and-how-did-it-change-cdn-caching-benefits)
- [171: How does Chrome decide resource priorities?](#171-how-does-chrome-decide-resource-priorities)
- [172: What is the frame budget, and where does `requestAnimationFrame` fit in a frame?](#172-what-is-the-frame-budget-and-where-does-requestanimationframe-fit-in-a-frame)
- [173: What are hidden classes and inline caches in V8?](#173-what-are-hidden-classes-and-inline-caches-in-v8)
- [174: What are V8's compilation tiers?](#174-what-are-v8s-compilation-tiers)
- [175: How does V8's garbage collector work at a high level?](#175-how-does-v8s-garbage-collector-work-at-a-high-level)
- [176: What happens to a tab when Chrome freezes or discards it?](#176-what-happens-to-a-tab-when-chrome-freezes-or-discards-it)
- [177: What is `scheduler.postTask`, and how does it differ from `setTimeout`?](#177-what-is-schedulerposttask-and-how-does-it-differ-from-settimeout)
- [178: What is the preload scanner?](#178-what-is-the-preload-scanner)
- [179: What is V8 code caching?](#179-what-is-v8-code-caching)
- [180: What are rasterization and tiles?](#180-what-are-rasterization-and-tiles)
- [181: How do you find a memory leak using heap snapshots in Chrome DevTools?](#181-how-do-you-find-a-memory-leak-using-heap-snapshots-in-chrome-devtools)
- [182: What is the difference between "Allocations on timeline" and "Allocation sampling" in the Memory panel?](#182-what-is-the-difference-between-allocations-on-timeline-and-allocation-sampling-in-the-memory-panel)
- [183: How do you find detached DOM elements in DevTools?](#183-how-do-you-find-detached-dom-elements-in-devtools)
- [184: How do you read the main thread flame chart in the Performance panel?](#184-how-do-you-read-the-main-thread-flame-chart-in-the-performance-panel)
- [185: How do you debug a slow interaction (poor INP) in DevTools?](#185-how-do-you-debug-a-slow-interaction-poor-inp-in-devtools)
- [186: What does each part of a request's Timing tab mean in the Network panel?](#186-what-does-each-part-of-a-requests-timing-tab-mean-in-the-network-panel)
- [187: How can you test a performance fix in production without deploying it?](#187-how-can-you-test-a-performance-fix-in-production-without-deploying-it)
- [188: How do you run Lighthouse in CI to catch regressions?](#188-how-do-you-run-lighthouse-in-ci-to-catch-regressions)
- [189: What are Lighthouse's navigation, timespan and snapshot modes?](#189-what-are-lighthouses-navigation-timespan-and-snapshot-modes)
- [190: What does WebPageTest show that Lighthouse doesn't?](#190-what-does-webpagetest-show-that-lighthouse-doesnt)
- [191: How do you query the CrUX API?](#191-how-do-you-query-the-crux-api)
- [192: What is the Resource Timing API, and why do cross-origin entries have zeros?](#192-what-is-the-resource-timing-api-and-why-do-cross-origin-entries-have-zeros)
- [193: How do you detect long tasks in the field?](#193-how-do-you-detect-long-tasks-in-the-field)
- [194: How do you CPU-profile a Node.js app?](#194-how-do-you-cpu-profile-a-nodejs-app)
- [195: How do you take a heap snapshot of a running Node.js process?](#195-how-do-you-take-a-heap-snapshot-of-a-running-nodejs-process)
- [196: How do you measure event loop lag in Node.js?](#196-how-do-you-measure-event-loop-lag-in-nodejs)
- [197: When should you change `UV_THREADPOOL_SIZE`?](#197-when-should-you-change-uv_threadpool_size)
- [198: How do you stream a large response in Node.js instead of buffering it?](#198-how-do-you-stream-a-large-response-in-nodejs-instead-of-buffering-it)
- [199: How do you handle backpressure manually when writing to a stream?](#199-how-do-you-handle-backpressure-manually-when-writing-to-a-stream)
- [200: Why use a worker pool instead of creating a worker thread per request?](#200-why-use-a-worker-pool-instead-of-creating-a-worker-thread-per-request)
- [201: Should you use the `cluster` module or run several containers?](#201-should-you-use-the-cluster-module-or-run-several-containers)
- [202: What happens with an unhandled promise rejection in Node.js?](#202-what-happens-with-an-unhandled-promise-rejection-in-nodejs)
- [203: What is `AsyncLocalStorage`, and does it cost much?](#203-what-is-asynclocalstorage-and-does-it-cost-much)
- [204: If a function is `async`, does it still block the event loop?](#204-if-a-function-is-async-does-it-still-block-the-event-loop)
- [205: Why can `JSON.parse` and `JSON.stringify` be a bottleneck, and what can you do?](#205-why-can-jsonparse-and-jsonstringify-be-a-bottleneck-and-what-can-you-do)
- [206: How does connection pooling work for outbound HTTP calls in Node.js?](#206-how-does-connection-pooling-work-for-outbound-http-calls-in-nodejs)
- [207: How do you limit the number of concurrent async operations?](#207-how-do-you-limit-the-number-of-concurrent-async-operations)
- [208: Why must every outbound call have a timeout?](#208-why-must-every-outbound-call-have-a-timeout)
- [209: How would you fairly compare the performance of Node.js, Deno and Bun for your service?](#209-how-would-you-fairly-compare-the-performance-of-nodejs-deno-and-bun-for-your-service)
- [210: How do you size the V8 heap for a Node.js app in a container?](#210-how-do-you-size-the-v8-heap-for-a-nodejs-app-in-a-container)
- [211: With HTTP/2 multiplexing, do you still need to bundle JavaScript?](#211-with-http2-multiplexing-do-you-still-need-to-bundle-javascript)
- [212: What is connection coalescing in HTTP/2 and HTTP/3?](#212-what-is-connection-coalescing-in-http2-and-http3)
- [213: HTTP/2 Server Push was removed from Chrome. What replaced it?](#213-http2-server-push-was-removed-from-chrome-what-replaced-it)
- [214: How can you reduce TLS overhead?](#214-how-can-you-reduce-tls-overhead)
- [215: What is HSTS, and how does it help performance?](#215-what-is-hsts-and-how-does-it-help-performance)
- [216: What is 0-RTT in TLS 1.3 and QUIC, and what is the risk?](#216-what-is-0-rtt-in-tls-13-and-quic-and-what-is-the-risk)
- [217: What is TCP slow start, and what is the "14 KB rule"?](#217-what-is-tcp-slow-start-and-what-is-the-14-kb-rule)
- [218: How can DNS add hidden latency, and how do you reduce it?](#218-how-can-dns-add-hidden-latency-and-how-do-you-reduce-it)
- [219: What is a CDN cache key, and how does the `Vary` header affect it?](#219-what-is-a-cdn-cache-key-and-how-does-the-vary-header-affect-it)
- [220: What do `stale-while-revalidate` and `stale-if-error` do?](#220-what-do-stale-while-revalidate-and-stale-if-error-do)
- [221: What problems come up when scaling WebSockets?](#221-what-problems-come-up-when-scaling-websockets)
- [222: How do Server-Sent Events handle reconnection, and how do they behave on HTTP/1.1 vs HTTP/2?](#222-how-do-server-sent-events-handle-reconnection-and-how-do-they-behave-on-http11-vs-http2)
- [223: How do you pick a compression level for dynamic responses, and when should you avoid compression?](#223-how-do-you-pick-a-compression-level-for-dynamic-responses-and-when-should-you-avoid-compression)
- [224: How do you use the Speculation Rules API?](#224-how-do-you-use-the-speculation-rules-api)
- [225: How do you add conditional request support to a Node.js API?](#225-how-do-you-add-conditional-request-support-to-a-nodejs-api)
- [226: How do you choose column order in a composite index?](#226-how-do-you-choose-column-order-in-a-composite-index)
- [227: How do you read a PostgreSQL `EXPLAIN ANALYZE` output?](#227-how-do-you-read-a-postgresql-explain-analyze-output)
- [228: Why might PostgreSQL ignore an index you created?](#228-why-might-postgresql-ignore-an-index-you-created)
- [229: What are partial and covering indexes?](#229-what-are-partial-and-covering-indexes)
- [230: How do you find the slowest queries in PostgreSQL?](#230-how-do-you-find-the-slowest-queries-in-postgresql)
- [231: What is PgBouncer, and what is transaction pooling?](#231-what-is-pgbouncer-and-what-is-transaction-pooling)
- [232: How do you size a database connection pool?](#232-how-do-you-size-a-database-connection-pool)
- [233: What is the ESR rule for MongoDB indexes?](#233-what-is-the-esr-rule-for-mongodb-indexes)
- [234: How do you make a MongoDB aggregation pipeline faster?](#234-how-do-you-make-a-mongodb-aggregation-pipeline-faster)
- [235: When should you embed documents in MongoDB, and when should you reference them?](#235-when-should-you-embed-documents-in-mongodb-and-when-should-you-reference-them)
- [236: What are Redis eviction policies, and which should you choose for a cache?](#236-what-are-redis-eviction-policies-and-which-should-you-choose-for-a-cache)
- [237: What is a cache stampede, and how do you prevent it?](#237-what-is-a-cache-stampede-and-how-do-you-prevent-it)
- [238: What is a hot key in Redis, and how do you deal with one?](#238-what-is-a-hot-key-in-redis-and-how-do-you-deal-with-one)
- [239: How does DataLoader solve N+1 in GraphQL or similar APIs?](#239-how-does-dataloader-solve-n1-in-graphql-or-similar-apis)
- [240: How do you process a very large query result in Node.js without loading it all into memory?](#240-how-do-you-process-a-very-large-query-result-in-nodejs-without-loading-it-all-into-memory)
- [241: What are context switches, and how do you check them?](#241-what-are-context-switches-and-how-do-you-check-them)
- [242: How do you read `vmstat` output?](#242-how-do-you-read-vmstat-output)
- [243: How do you read `iostat -x` output?](#243-how-do-you-read-iostat--x-output)
- [244: How can `strace` help debug a slow or stuck process?](#244-how-can-strace-help-debug-a-slow-or-stuck-process)
- [245: How do you use `perf` to profile a Node.js process?](#245-how-do-you-use-perf-to-profile-a-nodejs-process)
- [246: What is `TIME_WAIT`, and how can it exhaust ephemeral ports?](#246-what-is-time_wait-and-how-can-it-exhaust-ephemeral-ports)
- [247: What is the listen backlog, and why does `somaxconn` matter?](#247-what-is-the-listen-backlog-and-why-does-somaxconn-matter)
- [248: What is the difference between virtual memory (VSZ) and RSS?](#248-what-is-the-difference-between-virtual-memory-vsz-and-rss)
- [249: Why does a Linux server show very little "free" memory even when it is not under pressure?](#249-why-does-a-linux-server-show-very-little-free-memory-even-when-it-is-not-under-pressure)
- [250: How does the Linux OOM killer choose a process?](#250-how-does-the-linux-oom-killer-choose-a-process)
- [251: How do you detect CPU throttling in a container?](#251-how-do-you-detect-cpu-throttling-in-a-container)
- [252: What is the "PID 1 problem" in Docker?](#252-what-is-the-pid-1-problem-in-docker)
- [253: What does `fsync` do, and why does it matter for performance?](#253-what-does-fsync-do-and-why-does-it-matter-for-performance)
- [254: The load average is high but CPU usage is low. What could be going on?](#254-the-load-average-is-high-but-cpu-usage-is-low-what-could-be-going-on)
- [255: How do you choose the number of worker threads or processes in a container?](#255-how-do-you-choose-the-number-of-worker-threads-or-processes-in-a-container)
- [256: Why does a Node.js app behind an AWS ALB sometimes return random 502 errors, and how do you fix it?](#256-why-does-a-nodejs-app-behind-an-aws-alb-sometimes-return-random-502-errors-and-how-do-you-fix-it)
- [257: Which metric should drive autoscaling for a web API?](#257-which-metric-should-drive-autoscaling-for-a-web-api)
- [258: What is CloudFront Origin Shield (or tiered caching), and when does it help?](#258-what-is-cloudfront-origin-shield-or-tiered-caching-and-when-does-it-help)
- [259: What is the difference between a CloudFront cache policy and an origin request policy?](#259-what-is-the-difference-between-a-cloudfront-cache-policy-and-an-origin-request-policy)
- [260: How do you upload and download large files to and from S3 efficiently?](#260-how-do-you-upload-and-download-large-files-to-and-from-s3-efficiently)
- [261: What does `proxy_buffering` do in Nginx?](#261-what-does-proxy_buffering-do-in-nginx)
- [262: How do you enable keep-alive connections from Nginx to upstream servers?](#262-how-do-you-enable-keep-alive-connections-from-nginx-to-upstream-servers)
- [263: What do 502, 503 and 504 errors from Nginx usually mean?](#263-what-do-502-503-and-504-errors-from-nginx-usually-mean)
- [264: Which load balancing algorithm is best for an API?](#264-which-load-balancing-algorithm-is-best-for-an-api)
- [265: What is the difference between readiness, liveness and startup probes in Kubernetes?](#265-what-is-the-difference-between-readiness-liveness-and-startup-probes-in-kubernetes)
- [266: How does the Kubernetes Horizontal Pod Autoscaler work?](#266-how-does-the-kubernetes-horizontal-pod-autoscaler-work)
- [267: How do you make Docker images for Node.js smaller and builds faster?](#267-how-do-you-make-docker-images-for-nodejs-smaller-and-builds-faster)
- [268: How do you catch performance regressions in CI before they reach production?](#268-how-do-you-catch-performance-regressions-in-ci-before-they-reach-production)
- [269: How does Terraform help make load tests trustworthy?](#269-how-does-terraform-help-make-load-tests-trustworthy)
- [270: How do you pick the right instance type for a Node.js service on AWS?](#270-how-do-you-pick-the-right-instance-type-for-a-nodejs-service-on-aws)
- [271: Why should latency be recorded as a histogram instead of an average or a gauge?](#271-why-should-latency-be-recorded-as-a-histogram-instead-of-an-average-or-a-gauge)
- [272: What are the RED and USE methods?](#272-what-are-the-red-and-use-methods)
- [273: How does trace context propagation work?](#273-how-does-trace-context-propagation-work)
- [274: What is the difference between head sampling and tail sampling?](#274-what-is-the-difference-between-head-sampling-and-tail-sampling)
- [275: How much overhead can logging add, and how do you reduce it?](#275-how-much-overhead-can-logging-add-and-how-do-you-reduce-it)
- [276: How do you connect logs with traces?](#276-how-do-you-connect-logs-with-traces)
- [277: An APM tool shows an endpoint's p95 went from 200 ms to 900 ms. How do you find the cause?](#277-an-apm-tool-shows-an-endpoints-p95-went-from-200-ms-to-900-ms-how-do-you-find-the-cause)
- [278: How can you CPU profile a Node.js service in production safely?](#278-how-can-you-cpu-profile-a-nodejs-service-in-production-safely)
- [279: What is the difference between a heap snapshot and a heap profile?](#279-what-is-the-difference-between-a-heap-snapshot-and-a-heap-profile)
- [280: What is the difference between closed and open workload models in load testing?](#280-what-is-the-difference-between-closed-and-open-workload-models-in-load-testing)
- [281: How do you model a realistic workload for a load test?](#281-how-do-you-model-a-realistic-workload-for-a-load-test)
- [282: What should you watch during a soak test?](#282-what-should-you-watch-during-a-soak-test)
- [283: How do you choose good SLIs for a web application?](#283-how-do-you-choose-good-slis-for-a-web-application)
- [284: What is a burn rate alert, and why use multiple windows?](#284-what-is-a-burn-rate-alert-and-why-use-multiple-windows)
- [285: What is Little's Law, and how do you use it in capacity planning?](#285-what-is-littles-law-and-how-do-you-use-it-in-capacity-planning)
- [286: What are the four parts of LCP, and what should each look like?](#286-what-are-the-four-parts-of-lcp-and-what-should-each-look-like)
- [287: How do you improve LCP when it is a hero image?](#287-how-do-you-improve-lcp-when-it-is-a-hero-image)
- [288: How do you improve INP by breaking up long tasks?](#288-how-do-you-improve-inp-by-breaking-up-long-tasks)
- [289: How do you fix common causes of CLS?](#289-how-do-you-fix-common-causes-of-cls)
- [290: What are best practices for loading web fonts quickly?](#290-what-are-best-practices-for-loading-web-fonts-quickly)
- [291: How do third-party scripts hurt performance, and how do you control them?](#291-how-do-third-party-scripts-hurt-performance-and-how-do-you-control-them)
- [292: When do you use `<picture>` instead of just `srcset`?](#292-when-do-you-use-picture-instead-of-just-srcset)
- [293: What do `decoding="async"` and `img.decode()` do?](#293-what-do-decodingasync-and-imgdecode-do)
- [294: How do you code split a frontend app?](#294-how-do-you-code-split-a-frontend-app)
- [295: What is the difference between tree shaking and dead code elimination, and what is the `sideEffects` flag?](#295-what-is-the-difference-between-tree-shaking-and-dead-code-elimination-and-what-is-the-sideeffects-flag)
- [296: How do you respect `prefers-reduced-motion`, and does it affect performance?](#296-how-do-you-respect-prefers-reduced-motion-and-does-it-affect-performance)
- [297: How do you segment RUM data to make it useful?](#297-how-do-you-segment-rum-data-to-make-it-useful)
- [298: How does the `web-vitals` attribution build help you debug?](#298-how-does-the-web-vitals-attribution-build-help-you-debug)
- [299: What kinds of performance budgets can you set?](#299-what-kinds-of-performance-budgets-can-you-set)
- [300: Why do lab results (Lighthouse) and field results (CrUX/RUM) often disagree?](#300-why-do-lab-results-lighthouse-and-field-results-cruxrum-often-disagree)

### Advanced Questions (301-450)

- [301: How would you build a virtualized list, and what are the hard parts?](#301-how-would-you-build-a-virtualized-list-and-what-are-the-hard-parts)
- [302: What does "ResizeObserver loop completed with undelivered notifications" mean, and how do you avoid it?](#302-what-does-resizeobserver-loop-completed-with-undelivered-notifications-mean-and-how-do-you-avoid-it)
- [303: Which DOM APIs force synchronous layout or style, and how do you find them in a trace?](#303-which-dom-apis-force-synchronous-layout-or-style-and-how-do-you-find-them-in-a-trace)
- [304: How do you build a browser stream pipeline that respects backpressure?](#304-how-do-you-build-a-browser-stream-pipeline-that-respects-backpressure)
- [305: What does a Service Worker cost on navigation, and how do you reduce it?](#305-what-does-a-service-worker-cost-on-navigation-and-how-do-you-reduce-it)
- [306: How do you make IndexedDB fast?](#306-how-do-you-make-indexeddb-fast)
- [307: How do you handle backpressure with WebSockets in the browser?](#307-how-do-you-handle-backpressure-with-websockets-in-the-browser)
- [308: What do you need to use `SharedArrayBuffer`, and when is it worth it?](#308-what-do-you-need-to-use-sharedarraybuffer-and-when-is-it-worth-it)
- [309: What are the performance considerations for View Transitions?](#309-what-are-the-performance-considerations-for-view-transitions)
- [310: How do you keep complex SVG animations smooth?](#310-how-do-you-keep-complex-svg-animations-smooth)
- [311: How do you build a high-performance animation loop with `OffscreenCanvas` in a worker?](#311-how-do-you-build-a-high-performance-animation-loop-with-offscreencanvas-in-a-worker)
- [312: How do you handle high-frequency pointer input efficiently?](#312-how-do-you-handle-high-frequency-pointer-input-efficiently)
- [313: What are the common sources of memory leaks in long-lived single-page apps, and how do you design against them?](#313-what-are-the-common-sources-of-memory-leaks-in-long-lived-single-page-apps-and-how-do-you-design-against-them)
- [314: Why is hydration expensive, and what are the ways to reduce it?](#314-why-is-hydration-expensive-and-what-are-the-ways-to-reduce-it)
- [315: What are some advanced `fetch` options that affect performance?](#315-what-are-some-advanced-fetch-options-that-affect-performance)
- [316: Walk through Chrome's RenderingNG pipeline from a DOM change to pixels on screen.](#316-walk-through-chromes-renderingng-pipeline-from-a-dom-change-to-pixels-on-screen)
- [317: Why might an animation fail to run on the compositor, even if it only animates `transform`?](#317-why-might-an-animation-fail-to-run-on-the-compositor-even-if-it-only-animates-transform)
- [318: What is layer explosion, and how does overlap cause it?](#318-what-is-layer-explosion-and-how-does-overlap-cause-it)
- [319: How does Blink decide which elements need style recalculation after a change?](#319-how-does-blink-decide-which-elements-need-style-recalculation-after-a-change)
- [320: What can make layout expensive, and what is a layout boundary?](#320-what-can-make-layout-expensive-and-what-is-a-layout-boundary)
- [321: What causes V8 deoptimization, and how do you investigate it?](#321-what-causes-v8-deoptimization-and-how-do-you-investigate-it)
- [322: What are V8 elements kinds, and why can they affect array performance?](#322-what-are-v8-elements-kinds-and-why-can-they-affect-array-performance)
- [323: How does V8's Orinoco garbage collector reduce pause times, and why can GC still hurt?](#323-how-does-v8s-orinoco-garbage-collector-reduce-pause-times-and-why-can-gc-still-hurt)
- [324: What is pointer compression in V8, and why does it matter for Chrome vs Node.js?](#324-what-is-pointer-compression-in-v8-and-why-does-it-matter-for-chrome-vs-nodejs)
- [325: How does the Blink scheduler prioritize work on the main thread?](#325-how-does-the-blink-scheduler-prioritize-work-on-the-main-thread)
- [326: What is the performance and memory cost of site isolation and out-of-process iframes?](#326-what-is-the-performance-and-memory-cost-of-site-isolation-and-out-of-process-iframes)
- [327: How does Blink manage DOM memory, and how can leaks cross between V8 and Blink?](#327-how-does-blink-manage-dom-memory-and-how-can-leaks-cross-between-v8-and-blink)
- [328: In what order does Chrome check its caches when a request is made?](#328-in-what-order-does-chrome-check-its-caches-when-a-request-is-made)
- [329: How does prerendering work internally, and what code needs care?](#329-how-does-prerendering-work-internally-and-what-code-needs-care)
- [330: How does Chrome throttle background pages, and what is exempt?](#330-how-does-chrome-throttle-background-pages-and-what-is-exempt)
- [331: How would you use a Perfetto trace to find why frames are being dropped?](#331-how-would-you-use-a-perfetto-trace-to-find-why-frames-are-being-dropped)
- [332: What advanced features of the DevTools Performance panel help with rendering problems?](#332-what-advanced-features-of-the-devtools-performance-panel-help-with-rendering-problems)
- [333: How do you read the Frames track, and what is the difference between dropped and partially presented frames?](#333-how-do-you-read-the-frames-track-and-what-is-the-difference-between-dropped-and-partially-presented-frames)
- [334: How do you use Long Animation Frames data in production to find the scripts behind poor INP?](#334-how-do-you-use-long-animation-frames-data-in-production-to-find-the-scripts-behind-poor-inp)
- [335: How does the Event Timing API represent interactions, and what are its quirks?](#335-how-does-the-event-timing-api-represent-interactions-and-what-are-its-quirks)
- [336: In a heap snapshot, what do shallow size, retained size, distance and dominators mean?](#336-in-a-heap-snapshot-what-do-shallow-size-retained-size-distance-and-dominators-mean)
- [337: Walk through investigating a memory leak in a production Node.js service.](#337-walk-through-investigating-a-memory-leak-in-a-production-nodejs-service)
- [338: What is a Node.js diagnostic report, and when is it useful?](#338-what-is-a-nodejs-diagnostic-report-and-when-is-it-useful)
- [339: How do you use WebPageTest to evaluate a change like moving to a new CDN or adding Early Hints?](#339-how-do-you-use-webpagetest-to-evaluate-a-change-like-moving-to-a-new-cdn-or-adding-early-hints)
- [340: What is the difference between Lighthouse's simulated, DevTools and provided throttling?](#340-what-is-the-difference-between-lighthouses-simulated-devtools-and-provided-throttling)
- [341: How do you analyze CrUX data in BigQuery?](#341-how-do-you-analyze-crux-data-in-bigquery)
- [342: How can you automate performance tracing with Puppeteer or the Chrome DevTools Protocol?](#342-how-can-you-automate-performance-tracing-with-puppeteer-or-the-chrome-devtools-protocol)
- [343: When reading a Node.js CPU profile, what do `(garbage collector)`, `(program)` and `(idle)` mean, and how do you map TypeScript back to source?](#343-when-reading-a-nodejs-cpu-profile-what-do-garbage-collector-program-and-idle-mean-and-how-do-you-map-typescript-back-to-source)
- [344: How do you use V8's tick profiler (`--prof`), and when would you choose it over `--cpu-prof`?](#344-how-do-you-use-v8s-tick-profiler---prof-and-when-would-you-choose-it-over---cpu-prof)
- [345: How do you trace Node.js internals with trace events and view them in Perfetto?](#345-how-do-you-trace-nodejs-internals-with-trace-events-and-view-them-in-perfetto)
- [346: Predict and explain the output order of this Node.js code.](#346-predict-and-explain-the-output-order-of-this-nodejs-code)
- [347: Your Node.js API slows down under load even though CPU isn't maxed. Profiling shows long waits in password hashing, file reads and DNS. What is going on?](#347-your-nodejs-api-slows-down-under-load-even-though-cpu-isnt-maxed-profiling-shows-long-waits-in-password-hashing-file-reads-and-dns-what-is-going-on)
- [348: How can microtasks or `process.nextTick` starve the event loop?](#348-how-can-microtasks-or-processnexttick-starve-the-event-loop)
- [349: How do `highWaterMark`, object mode and async iteration interact in Node.js streams?](#349-how-do-highwatermark-object-mode-and-async-iteration-interact-in-nodejs-streams)
- [350: How do you write a custom Transform stream with proper error handling and backpressure?](#350-how-do-you-write-a-custom-transform-stream-with-proper-error-handling-and-backpressure)
- [351: How do you share memory and coordinate between Node.js worker threads, and how do you limit their resources?](#351-how-do-you-share-memory-and-coordinate-between-nodejs-worker-threads-and-how-do-you-limit-their-resources)
- [352: How does the `cluster` module distribute connections, and what problems does that cause for WebSockets?](#352-how-does-the-cluster-module-distribute-connections-and-what-problems-does-that-cause-for-websockets)
- [353: How do you read `--trace-gc` output, and when would you tune `--max-semi-space-size`?](#353-how-do-you-read---trace-gc-output-and-when-would-you-tune---max-semi-space-size)
- [354: Why can RSS keep growing in a Node.js process when the V8 heap is stable?](#354-why-can-rss-keep-growing-in-a-nodejs-process-when-the-v8-heap-is-stable)
- [355: When is it worth moving CPU-heavy work to WebAssembly or a native addon in Node.js?](#355-when-is-it-worth-moving-cpu-heavy-work-to-webassembly-or-a-native-addon-in-nodejs)
- [356: Which Node.js HTTP server settings matter for performance and resilience?](#356-which-nodejs-http-server-settings-matter-for-performance-and-resilience)
- [357: How do you implement load shedding in a Node.js service?](#357-how-do-you-implement-load-shedding-in-a-nodejs-service)
- [358: How do Deno and Bun differ from Node.js in ways that affect performance?](#358-how-do-deno-and-bun-differ-from-nodejs-in-ways-that-affect-performance)
- [359: How do you reduce Node.js startup time?](#359-how-do-you-reduce-nodejs-startup-time)
- [360: How do you handle CPU-bound requests in a Node.js API without hurting other users?](#360-how-do-you-handle-cpu-bound-requests-in-a-nodejs-api-without-hurting-other-users)
- [361: How does request prioritization work in HTTP/2 and HTTP/3, and what is RFC 9218?](#361-how-does-request-prioritization-work-in-http2-and-http3-and-what-is-rfc-9218)
- [362: How does HTTP/2 flow control work, and how can it limit throughput?](#362-how-does-http2-flow-control-work-and-how-can-it-limit-throughput)
- [363: Why might HTTP/3 sometimes be slower than HTTP/2, and how does congestion control affect both?](#363-why-might-http3-sometimes-be-slower-than-http2-and-how-does-congestion-control-affect-both)
- [364: How have newer TLS features changed handshake size and latency?](#364-how-have-newer-tls-features-changed-handshake-size-and-latency)
- [365: Which Linux TCP settings affect web server performance?](#365-which-linux-tcp-settings-affect-web-server-performance)
- [366: What is bufferbloat, and how does it show up in web performance?](#366-what-is-bufferbloat-and-how-does-it-show-up-in-web-performance)
- [367: How do Happy Eyeballs and IPv6 affect connection latency, including in Node.js?](#367-how-do-happy-eyeballs-and-ipv6-affect-connection-latency-including-in-nodejs)
- [368: How do you invalidate CDN caches efficiently at scale?](#368-how-do-you-invalidate-cdn-caches-efficiently-at-scale)
- [369: What is Compression Dictionary Transport, and when does it help?](#369-what-is-compression-dictionary-transport-and-when-does-it-help)
- [370: How does streaming HTML (early flush) improve performance, and what can break it?](#370-how-does-streaming-html-early-flush-improve-performance-and-what-can-break-it)
- [371: What are WebSockets over HTTP/2 and WebTransport, and why might you use them?](#371-what-are-websockets-over-http2-and-webtransport-and-why-might-you-use-them)
- [372: How does head-of-line blocking show up at different layers, and how should it change your protocol choices?](#372-how-does-head-of-line-blocking-show-up-at-different-layers-and-how-should-it-change-your-protocol-choices)
- [373: What are the pitfalls of ETags in multi-server and CDN setups?](#373-what-are-the-pitfalls-of-etags-in-multi-server-and-cdn-setups)
- [374: How do you cache HTML at the CDN while keeping browser caching safe?](#374-how-do-you-cache-html-at-the-cdn-while-keeping-browser-caching-safe)
- [375: Why do long-lived HTTP/2 or gRPC connections cause uneven load, and how do you fix it?](#375-why-do-long-lived-http2-or-grpc-connections-cause-uneven-load-and-how-do-you-fix-it)
- [376: How does PostgreSQL choose between nested loop, hash and merge joins, and how does `work_mem` affect them?](#376-how-does-postgresql-choose-between-nested-loop-hash-and-merge-joins-and-how-does-work_mem-affect-them)
- [377: Why does PostgreSQL misestimate rows for queries filtering on correlated columns, and how do extended statistics help?](#377-why-does-postgresql-misestimate-rows-for-queries-filtering-on-correlated-columns-and-how-do-extended-statistics-help)
- [378: How do you diagnose and fix table bloat and autovacuum problems in PostgreSQL?](#378-how-do-you-diagnose-and-fix-table-bloat-and-autovacuum-problems-in-postgresql)
- [379: How do you find and fix lock contention in PostgreSQL?](#379-how-do-you-find-and-fix-lock-contention-in-postgresql)
- [380: How do prepared statements and plan caching work in PostgreSQL, and when do they hurt?](#380-how-do-prepared-statements-and-plan-caching-work-in-postgresql-and-when-do-they-hurt)
- [381: When would you use GIN, GiST, BRIN or hash indexes instead of B-tree?](#381-when-would-you-use-gin-gist-brin-or-hash-indexes-instead-of-b-tree)
- [382: How does table partitioning help performance in PostgreSQL, and what are its traps?](#382-how-does-table-partitioning-help-performance-in-postgresql-and-what-are-its-traps)
- [383: How do read replicas help performance, and how do you handle replication lag?](#383-how-do-read-replicas-help-performance-and-how-do-you-handle-replication-lag)
- [384: What determines MongoDB performance at scale, and how do you choose a shard key?](#384-what-determines-mongodb-performance-at-scale-and-how-do-you-choose-a-shard-key)
- [385: How do you investigate a MongoDB query that picks a bad plan?](#385-how-do-you-investigate-a-mongodb-query-that-picks-a-bad-plan)
- [386: Why can Redis latency spike, and how do you diagnose it?](#386-why-can-redis-latency-spike-and-how-do-you-diagnose-it)
- [387: What race conditions can happen with cache invalidation, and how do you avoid serving stale data?](#387-what-race-conditions-can-happen-with-cache-invalidation-and-how-do-you-avoid-serving-stale-data)
- [388: How do you find and fix ORM overhead in a production Node.js app?](#388-how-do-you-find-and-fix-orm-overhead-in-a-production-nodejs-app)
- [389: How can a connection pool deadlock itself, and how do you detect pool exhaustion?](#389-how-can-a-connection-pool-deadlock-itself-and-how-do-you-detect-pool-exhaustion)
- [390: How do you implement keyset pagination with multiple sort columns, and how do you show total counts cheaply?](#390-how-do-you-implement-keyset-pagination-with-multiple-sort-columns-and-how-do-you-show-total-counts-cheaply)
- [391: A service has high latency but its CPU flame graph shows nothing unusual. What do you do next?](#391-a-service-has-high-latency-but-its-cpu-flame-graph-shows-nothing-unusual-what-do-you-do-next)
- [392: Which eBPF tools are most useful for debugging server performance, and what do they show?](#392-which-ebpf-tools-are-most-useful-for-debugging-server-performance-and-what-do-they-show)
- [393: How do you get accurate `perf` profiles of Node.js, including inside containers?](#393-how-do-you-get-accurate-perf-profiles-of-nodejs-including-inside-containers)
- [394: What are page faults and transparent huge pages, and how can they affect Node.js, Redis or databases?](#394-what-are-page-faults-and-transparent-huge-pages-and-how-can-they-affect-nodejs-redis-or-databases)
- [395: How does cgroup v2 memory accounting work, and what is the difference between `memory.high` and `memory.max`?](#395-how-does-cgroup-v2-memory-accounting-work-and-what-is-the-difference-between-memoryhigh-and-memorymax)
- [396: How do NUMA, hyperthreading and CPU steal affect server performance?](#396-how-do-numa-hyperthreading-and-cpu-steal-affect-server-performance)
- [397: What does "nf_conntrack: table full, dropping packet" mean, and how do you fix it?](#397-what-does-nf_conntrack-table-full-dropping-packet-mean-and-how-do-you-fix-it)
- [398: How do you use `ss -ti` to understand TCP performance for a connection?](#398-how-do-you-use-ss--ti-to-understand-tcp-performance-for-a-connection)
- [399: Why might disk-heavy workloads on cloud VMs suddenly get slow?](#399-why-might-disk-heavy-workloads-on-cloud-vms-suddenly-get-slow)
- [400: How do you find a file descriptor leak?](#400-how-do-you-find-a-file-descriptor-leak)
- [401: How do you make Kubernetes rolling deploys drop zero requests?](#401-how-do-you-make-kubernetes-rolling-deploys-drop-zero-requests)
- [402: Why does Kubernetes report higher memory use than the app's RSS, and why can a pod be evicted with "free" memory on the node?](#402-why-does-kubernetes-report-higher-memory-use-than-the-apps-rss-and-why-can-a-pod-be-evicted-with-free-memory-on-the-node)
- [403: How does the Linux scheduler decide which thread runs, and how does that affect latency?](#403-how-does-the-linux-scheduler-decide-which-thread-runs-and-how-does-that-affect-latency)
- [404: When would you use `strace`, `ltrace`, `perf trace` or eBPF, given their overhead?](#404-when-would-you-use-strace-ltrace-perf-trace-or-ebpf-given-their-overhead)
- [405: How do you capture and analyze a core dump from a crashed Node.js process?](#405-how-do-you-capture-and-analyze-a-core-dump-from-a-crashed-nodejs-process)
- [406: How do you use ALB access logs to find where request time is spent?](#406-how-do-you-use-alb-access-logs-to-find-where-request-time-is-spent)
- [407: How do you stop autoscaling from oscillating or reacting too late?](#407-how-do-you-stop-autoscaling-from-oscillating-or-reacting-too-late)
- [408: The CDN cache hit ratio is 40% on content that should be cacheable. How do you raise it?](#408-the-cdn-cache-hit-ratio-is-40-on-content-that-should-be-cacheable-how-do-you-raise-it)
- [409: When should you run code at the edge, and what are the trade-offs between edge platforms?](#409-when-should-you-run-code-at-the-edge-and-what-are-the-trade-offs-between-edge-platforms)
- [410: How do S3 request rate limits work, and how do you handle `503 SlowDown` errors?](#410-how-do-s3-request-rate-limits-work-and-how-do-you-handle-503-slowdown-errors)
- [411: Which Nginx settings matter at high traffic?](#411-which-nginx-settings-matter-at-high-traffic)
- [412: How can retries at proxies and clients make an outage worse, and how do you configure them safely?](#412-how-can-retries-at-proxies-and-clients-make-an-outage-worse-and-how-do-you-configure-them-safely)
- [413: How should you set CPU requests and limits for Node.js pods, and what are QoS classes?](#413-how-should-you-set-cpu-requests-and-limits-for-nodejs-pods-and-what-are-qos-classes)
- [414: What networking issues inside Kubernetes commonly add latency?](#414-what-networking-issues-inside-kubernetes-commonly-add-latency)
- [415: How do you deploy without dropping connections behind an AWS load balancer?](#415-how-do-you-deploy-without-dropping-connections-behind-an-aws-load-balancer)
- [416: How do you make CI pipelines much faster for a large JavaScript monorepo?](#416-how-do-you-make-ci-pipelines-much-faster-for-a-large-javascript-monorepo)
- [417: How do you detect frontend performance regressions in CI without false alarms from noise?](#417-how-do-you-detect-frontend-performance-regressions-in-ci-without-false-alarms-from-noise)
- [418: How do you use Terraform to build repeatable performance test environments, and what are the pitfalls?](#418-how-do-you-use-terraform-to-build-repeatable-performance-test-environments-and-what-are-the-pitfalls)
- [419: How do you reduce cold start latency for Node.js on AWS Lambda?](#419-how-do-you-reduce-cold-start-latency-for-nodejs-on-aws-lambda)
- [420: What are the trade-offs of running a web app in multiple regions for latency?](#420-what-are-the-trade-offs-of-running-a-web-app-in-multiple-regions-for-latency)
- [421: What is tail latency amplification in fan-out requests, and how do you reduce it?](#421-what-is-tail-latency-amplification-in-fan-out-requests-and-how-do-you-reduce-it)
- [422: What is coordinated omission, and how do HDR histograms help?](#422-what-is-coordinated-omission-and-how-do-hdr-histograms-help)
- [423: How do you design an OpenTelemetry Collector pipeline for a high-traffic system?](#423-how-do-you-design-an-opentelemetry-collector-pipeline-for-a-high-traffic-system)
- [424: How do you find the critical path in a distributed trace?](#424-how-do-you-find-the-critical-path-in-a-distributed-trace)
- [425: What are exemplars, and how do they connect metrics to traces?](#425-what-are-exemplars-and-how-do-they-connect-metrics-to-traces)
- [426: Why is high cardinality a problem in metrics, and how do you avoid it?](#426-why-is-high-cardinality-a-problem-in-metrics-and-how-do-you-avoid-it)
- [427: How do continuous profiling and differential flame graphs help find regressions?](#427-how-do-continuous-profiling-and-differential-flame-graphs-help-find-regressions)
- [428: Show how allocation profiling can reduce GC pressure in a hot path.](#428-show-how-allocation-profiling-can-reduce-gc-pressure-in-a-hot-path)
- [429: How do you find lock contention in a Node.js system, given JavaScript is single-threaded?](#429-how-do-you-find-lock-contention-in-a-nodejs-system-given-javascript-is-single-threaded)
- [430: What goes wrong when running large load tests, and how do you avoid it?](#430-what-goes-wrong-when-running-large-load-tests-and-how-do-you-avoid-it)
- [431: How do you find a system's capacity limit, and what does the Universal Scalability Law say?](#431-how-do-you-find-a-systems-capacity-limit-and-what-does-the-universal-scalability-law-say)
- [432: During a 12-hour soak test, memory grows slowly. How do you tell a leak from normal behavior, and pin it down?](#432-during-a-12-hour-soak-test-memory-grows-slowly-how-do-you-tell-a-leak-from-normal-behavior-and-pin-it-down)
- [433: How do you design latency SLOs that actually reflect user experience?](#433-how-do-you-design-latency-slos-that-actually-reflect-user-experience)
- [434: How do you design alerts that catch real problems without causing alert fatigue?](#434-how-do-you-design-alerts-that-catch-real-problems-without-causing-alert-fatigue)
- [435: How do you use fault injection to verify that timeouts, retries and fallbacks actually work?](#435-how-do-you-use-fault-injection-to-verify-that-timeouts-retries-and-fallbacks-actually-work)
- [436: How exactly is INP calculated for a page?](#436-how-exactly-is-inp-calculated-for-a-page)
- [437: How does CLS session windowing work, and how do you measure CLS correctly in a single-page app?](#437-how-does-cls-session-windowing-work-and-how-do-you-measure-cls-correctly-in-a-single-page-app)
- [438: What are the less obvious rules about which element counts as LCP?](#438-what-are-the-less-obvious-rules-about-which-element-counts-as-lcp)
- [439: What are soft navigations, and how are they measured?](#439-what-are-soft-navigations-and-how-are-they-measured)
- [440: How do prerendering and bfcache change how TTFB, FCP and LCP should be measured?](#440-how-do-prerendering-and-bfcache-change-how-ttfb-fcp-and-lcp-should-be-measured)
- [441: How do CSS and scripts interact to block rendering and parsing, and what does `blocking="render"` do?](#441-how-do-css-and-scripts-interact-to-block-rendering-and-parsing-and-what-does-blockingrender-do)
- [442: How would you design an image delivery pipeline for a large site?](#442-how-would-you-design-an-image-delivery-pipeline-for-a-large-site)
- [443: How do you ship less JavaScript to modern browsers without breaking older ones?](#443-how-do-you-ship-less-javascript-to-modern-browsers-without-breaking-older-ones)
- [444: What are the trade-offs of running third-party scripts in a Web Worker (for example with Partytown)?](#444-what-are-the-trade-offs-of-running-third-party-scripts-in-a-web-worker-for-example-with-partytown)
- [445: How do SSR streaming, React Server Components and selective hydration affect Core Web Vitals?](#445-how-do-ssr-streaming-react-server-components-and-selective-hydration-affect-core-web-vitals)
- [446: How would you design a RUM pipeline that gives accurate percentiles without huge cost?](#446-how-would-you-design-a-rum-pipeline-that-gives-accurate-percentiles-without-huge-cost)
- [447: How do you run a performance budget program across several teams?](#447-how-do-you-run-a-performance-budget-program-across-several-teams)
- [448: How do you connect performance improvements to business metrics in a trustworthy way?](#448-how-do-you-connect-performance-improvements-to-business-metrics-in-a-trustworthy-way)
- [449: How are accessibility and performance connected beyond reduced motion?](#449-how-are-accessibility-and-performance-connected-beyond-reduced-motion)
- [450: Users in one region report the site is slow, but your dashboards look fine. Walk through how you would debug it end to end.](#450-users-in-one-region-report-the-site-is-slow-but-your-dashboards-look-fine-walk-through-how-you-would-debug-it-end-to-end)

---

## Easy Questions (1-150)

### Easy: Web Platform Fundamentals (1-15)

#### 1: What is semantic HTML, and does it have anything to do with performance?

Semantic HTML means using elements for what they mean: `<header>`, `<nav>`, `<main>`, `<article>`, `<button>`, `<ul>` and so on, instead of a pile of `<div>` and `<span>` tags. It helps performance in a few indirect ways:

- Native elements come with built-in behavior. A `<button>` is focusable and handles Enter and Space for free, so you ship less JavaScript.
- The markup is usually smaller and flatter than div soup, which means fewer DOM nodes to style and lay out.
- Screen readers and search engines understand the page without extra ARIA work.

```html
<!-- Avoid -->
<div class="btn" onclick="save()">Save</div>

<!-- Prefer -->
<button type="button" onclick="save()">Save</button>
```

#### 2: Why does DOM size matter?

Every node costs memory, and every node may need to go through style calculation, layout and paint. A large DOM makes all of those steps slower, and it makes `querySelectorAll` calls and full-tree style invalidations more expensive. Lighthouse warns when a page has more than about 1,400 elements, or when it is very deep or has a parent with lots of children. Common fixes are virtualizing long lists, removing hidden markup that is never shown, and rendering content only when it is needed.

#### 3: What does `<link rel="preload">` do?

It tells the browser to start downloading a resource right away, at high priority, because the page will need it soon. It is useful for things the browser finds late, like a font referenced inside a CSS file or a hero image set through CSS `background-image`.

```html
<link
  rel="preload"
  href="/fonts/inter.woff2"
  as="font"
  type="font/woff2"
  crossorigin
/>
<link rel="preload" href="/img/hero.avif" as="image" fetchpriority="high" />
```

The `as` attribute is required so the browser can set the right priority and reuse the response. If you preload something and don't use it within a few seconds, Chrome logs a warning in the console. Preloading too many things defeats the purpose because they all compete for bandwidth.

#### 4: What is the difference between `preconnect` and `dns-prefetch`?

`dns-prefetch` only resolves the domain name. `preconnect` resolves the name, opens the TCP (or QUIC) connection and finishes the TLS handshake, so the first request to that origin can be sent immediately.

```html
<link rel="preconnect" href="https://cdn.example.com" crossorigin />
<link rel="dns-prefetch" href="https://analytics.example.com" />
```

Use `preconnect` for a small number of origins you will definitely use early (two or three at most), since open connections that go unused waste resources. Use `dns-prefetch` as a cheap hint for other third-party origins.

#### 5: How does native lazy loading work?

You add `loading="lazy"` to an `<img>` or `<iframe>`. The browser then waits to fetch it until it gets close to the viewport. Chrome uses a distance threshold that depends on the connection speed.

```html
<img
  src="/photo.jpg"
  alt="Team photo"
  width="800"
  height="600"
  loading="lazy"
/>
<iframe
  src="https://www.youtube.com/embed/xyz"
  loading="lazy"
  title="Demo"
></iframe>
```

Do not lazy load the LCP image or anything above the fold. That delays the most important content. Always set `width` and `height` (or `aspect-ratio`) so lazy images don't cause layout shifts when they arrive.

#### 6: Why is CSS considered render-blocking?

The browser will not paint the page until it has downloaded and parsed all the stylesheets in the `<head>` that apply to the current media. If it painted earlier, the user would see unstyled content that then jumps around. So a slow CSS file directly delays First Contentful Paint. You can reduce the cost by making CSS small, inlining the critical part, and using the `media` attribute for stylesheets that only apply in some cases, like `media="print"`.

#### 7: What is critical CSS?

Critical CSS is the small set of styles needed to render the part of the page the user sees first. You inline it in a `<style>` tag in the `<head>` so the first paint doesn't wait for a network request, then load the rest of the CSS without blocking.

```html
<head>
  <style>
    /* header, hero, layout grid */
  </style>
  <link
    rel="preload"
    href="/main.css"
    as="style"
    onload="this.rel='stylesheet'"
  />
  <noscript><link rel="stylesheet" href="/main.css" /></noscript>
</head>
```

Keep the inline part small (roughly under 14 KB compressed, so it fits in the first round trip with a typical initial congestion window).

#### 8: Which CSS properties are cheap to animate?

`transform` and `opacity`. When the element is on its own compositor layer, the browser can change these on the compositor thread without running layout or paint again. Animating `width`, `height`, `top`, `left` or `margin` triggers layout on every frame, and animating `background-color` or `box-shadow` triggers paint.

```css
/* Slow: layout every frame */
.panel {
  transition: left 300ms;
}

/* Fast: compositor only */
.panel {
  transition: transform 300ms;
}
.panel.open {
  transform: translateX(240px);
}
```

#### 9: What is the event loop in the browser?

JavaScript in a page runs on one main thread. The event loop picks a task from a queue (a click handler, a timer callback, a network callback), runs it to completion, runs all queued microtasks (promise callbacks), and then, if it is time for a new frame, gives the browser a chance to run `requestAnimationFrame` callbacks, style, layout and paint. Then it picks the next task. If a single task takes a long time, nothing else can happen, including rendering and responding to input.

#### 10: What is the difference between debouncing and throttling?

Debouncing waits until events stop for some time and then runs the function once. Throttling runs the function at most once per time window, no matter how many events arrive.

```js
function debounce(fn, wait) {
  let id;
  return (...args) => {
    clearTimeout(id);
    id = setTimeout(() => fn(...args), wait);
  };
}

function throttle(fn, wait) {
  let last = 0;
  return (...args) => {
    const now = performance.now();
    if (now - last >= wait) {
      last = now;
      fn(...args);
    }
  };
}

searchInput.addEventListener("input", debounce(runSearch, 300));
window.addEventListener("scroll", throttle(updateProgressBar, 100));
```

Debounce fits search boxes and resize handlers. Throttle fits scroll position tracking and drag updates.

#### 11: What is a Web Worker?

A Web Worker runs JavaScript on a separate background thread. It has no access to the DOM, and it talks to the page through `postMessage`. You use it for heavy work like parsing a big file, image processing or complex calculations, so the main thread stays free to handle input and rendering.

```js
// main.js
const worker = new Worker(new URL("./worker.js", import.meta.url), {
  type: "module",
});
worker.postMessage({ numbers: bigArray });
worker.onmessage = (e) => console.log("sum", e.data);

// worker.js
self.onmessage = (e) => {
  const sum = e.data.numbers.reduce((a, b) => a + b, 0);
  self.postMessage(sum);
};
```

#### 12: What is event delegation?

Instead of attaching a listener to each child element, you attach one listener to a common parent and check `event.target` inside it. This works because most events bubble. It saves memory, reduces setup time for large lists, and it automatically covers items added later.

```js
document.querySelector("#todo-list").addEventListener("click", (e) => {
  const button = e.target.closest('button[data-action="delete"]');
  if (!button) return;
  button.closest("li").remove();
});
```

#### 13: What is layout thrashing?

It happens when code alternates between writing to the DOM and reading layout values like `offsetHeight` or `getBoundingClientRect()`. Each read after a write forces the browser to recalculate layout right away (a forced synchronous layout). In a loop this can mean hundreds of layouts in a single frame.

```js
// Bad: read, write, read, write...
items.forEach((el) => {
  el.style.height = el.offsetWidth / 2 + "px";
});

// Better: read everything first, then write
const widths = items.map((el) => el.offsetWidth);
items.forEach((el, i) => {
  el.style.height = widths[i] / 2 + "px";
});
```

#### 14: What is `IntersectionObserver` used for?

It tells you when an element enters or leaves the viewport (or another container), without you having to listen to scroll events and measure positions yourself. Typical uses are lazy loading, infinite scroll, starting animations when visible, and tracking ad or content impressions.

```js
const io = new IntersectionObserver(
  (entries) => {
    for (const entry of entries) {
      if (entry.isIntersecting) {
        loadMore();
      }
    }
  },
  { rootMargin: "200px" },
);

io.observe(document.querySelector("#sentinel"));
```

The callback runs asynchronously and the browser does the geometry work efficiently, so it is much cheaper than scroll handlers.

#### 15: When would you pick SVG over Canvas, or the other way around?

SVG is part of the DOM. Each shape is an element you can style with CSS, attach events to, and make accessible. It scales without blurring. It is a good fit for icons, logos, charts with a moderate number of points, and simple diagrams. It slows down when you have thousands of elements because each one is a DOM node.

Canvas is a bitmap you draw on with JavaScript. It has no DOM per shape, so it handles tens of thousands of moving objects well, like in games, heatmaps or large data plots. The downside is that you handle hit testing, accessibility and high-DPI scaling yourself.

---

### Easy: Google Chrome and Browser Internals (16-30)

#### 16: What is Chrome's multi-process architecture?

Chrome splits work across several operating system processes instead of running everything in one. The main ones are:

- **Browser process**: the UI, tabs, navigation, and coordination of everything else.
- **Renderer processes**: run Blink and V8 for web content.
- **GPU process**: talks to the graphics hardware and draws the final frames.
- **Network service**: handles all network requests.
- **Utility processes**: audio, storage and other services.

If a renderer crashes, only that tab (or those tabs) dies. It also lets Chrome sandbox web content, so a bug in a renderer has a harder time reaching the rest of the system.

#### 17: What does a renderer process do?

It turns HTML, CSS and JavaScript into pixels for one or more pages from the same site. It runs the HTML parser, the DOM, style calculation, layout and paint (Blink), plus the JavaScript engine (V8). Inside the renderer, the main thread does most of this work, the compositor thread handles scrolling and some animations, and raster worker threads turn paint commands into bitmaps.

#### 18: What is site isolation?

Site isolation puts pages from different sites into different renderer processes, including cross-site iframes. For example, an `<iframe>` from `ads.example` inside `news.example` runs in its own process. It was turned on by default on desktop to protect against Spectre-style attacks, where one site could read another site's memory if they shared a process. The cost is more processes and more memory use.

#### 19: What is the difference between Chromium and Chrome?

Chromium is the open-source project that contains the browser code: Blink, V8, the networking stack, the UI and so on. Google Chrome is Google's product built on top of Chromium, with some extra pieces like auto-update, some media codecs, crash reporting and Google account sync. Edge, Brave, Opera and Vivaldi are also built on Chromium, so most performance advice for Chrome also applies to them.

#### 20: What is Blink?

Blink is the rendering engine in Chromium. It parses HTML into the DOM, parses CSS, computes styles, lays out boxes, creates paint records and hands off to the compositor. It also implements most web platform APIs, like the DOM, `fetch`, `IntersectionObserver` and so on. It was forked from WebKit in 2013.

#### 21: What is V8?

V8 is the JavaScript and WebAssembly engine used by Chrome and Node.js. It parses JavaScript, runs it first with the Ignition interpreter, and then compiles frequently used functions with faster compilers (Sparkplug, Maglev and TurboFan). It also manages memory with a garbage collector. Deno also uses V8. Bun uses JavaScriptCore instead.

#### 22: What are the main steps of the browser rendering pipeline?

1. **JavaScript** runs and may change the DOM or styles.
2. **Style** calculates the final computed style for each element.
3. **Layout** works out the size and position of every box.
4. **Paint** records drawing commands (text, colors, borders, images).
5. **Composite** splits the page into layers, rasterizes them, and combines them into the final frame on the GPU.

Not every change runs every step. Changing `transform` can skip layout and paint. Changing `color` skips layout but needs paint. Changing `width` usually needs all of them.

#### 23: What is the difference between layout (reflow) and repaint?

Layout (also called reflow) recalculates positions and sizes of elements. Repaint redraws pixels for elements whose look changed but not their geometry. Layout is usually more expensive because a change can affect many other elements, like siblings and parents. Changing `color` or `visibility` causes repaint. Changing `width`, `font-size`, or adding elements causes layout and then repaint.

#### 24: What is compositing?

Compositing is the last step of rendering. The page is split into layers, each layer is rasterized into tiles, and the GPU combines the layers into the final image. Because layers are separate, the browser can move or fade a layer (using `transform` or `opacity`) without repainting what is inside it. That is why compositor-only animations stay smooth even when the main thread is busy.

#### 25: What is the difference between the memory cache and the disk cache in Chrome?

The memory cache lives inside the renderer and holds resources used by the current page, like images and scripts already fetched during this page load. It is very fast but goes away when the tab closes or navigates. The disk cache is the HTTP cache stored on disk, shared across tabs for the same partition, and it follows HTTP caching headers like `Cache-Control`. In the DevTools Network panel the Size column shows "(memory cache)" or "(disk cache)" for each.

#### 26: What is the Cache Storage API?

It is a storage area that scripts control directly, mostly used by Service Workers. You put `Request`/`Response` pairs in named caches and read them back later, which lets you build offline support or custom caching rules.

```js
const cache = await caches.open("static-v3");
await cache.addAll(["/", "/app.js", "/styles.css"]);
const res = await cache.match("/app.js");
```

Unlike the HTTP cache, the browser does not expire these entries based on headers. Your code has to clean up old caches.

#### 27: What is a long task?

A long task is any task on the main thread that runs for more than 50 milliseconds. While it runs, the page can't respond to clicks or key presses, so the user feels lag. The 50 ms number comes from the RAIL model: if work is split into chunks under 50 ms, the browser can still respond to input within about 100 ms. DevTools marks long tasks with a red triangle in the Performance panel.

#### 28: What is the difference between microtasks and macrotasks?

Macrotasks (just "tasks" in the spec) include timers, I/O callbacks and UI events. Microtasks include promise callbacks, `queueMicrotask` and `MutationObserver` callbacks. After each task, the browser runs every microtask in the queue, including new ones added while draining, before moving on.

```js
console.log("1");
setTimeout(() => console.log("4 - task"), 0);
Promise.resolve().then(() => console.log("3 - microtask"));
console.log("2");
// 1, 2, 3 - microtask, 4 - task
```

A loop that keeps adding microtasks can freeze the page just like a long synchronous loop.

#### 29: Why do timers run slower in background tabs?

To save battery and CPU, Chrome throttles hidden tabs. Timers in background tabs are limited to run at most once per second, and after a page has been hidden for several minutes, Chrome applies "intensive throttling" that groups timer wake-ups to once per minute in some cases. `requestAnimationFrame` stops entirely in hidden tabs. Don't rely on timers for accurate timing in the background; use the Page Visibility API to pause and resume work.

```js
document.addEventListener("visibilitychange", () => {
  if (document.hidden) pausePolling();
  else resumePolling();
});
```

#### 30: How can you see which tab is using the most resources in Chrome?

Open Chrome's Task Manager with Shift+Esc on Windows and Linux, or from the menu (More tools > Task manager) on macOS. It shows memory, CPU, network and process ID for each tab, extension and helper process. Chrome's Memory Saver feature can discard inactive tabs to free memory, and Energy Saver limits background activity when on battery. Hovering a tab also shows its memory use in recent versions.

---

### Easy: Browser Developer and Performance Tools (31-45)

#### 31: What is the Chrome DevTools Performance panel used for?

It records what the browser does over a period of time: JavaScript execution, style, layout, paint, network requests and frames. You use it to find what makes a page slow to load or slow to respond. When you open it, it also shows live Core Web Vitals (LCP, CLS and INP) for the current page, and it can show real-user field data from CrUX next to your local numbers. After a recording, the Insights sidebar points out common problems like render-blocking requests, layout shifts and long interactions.

#### 32: What does the Network panel show?

It lists every request the page makes, with status, type, size, timing and the initiator (what caused the request). The waterfall column shows when each request started and how long each phase took: queueing, DNS, connection, TLS, waiting for the server (TTFB) and content download. Useful options include "Disable cache" (only while DevTools is open), throttling presets like "Slow 4G", and filters by type or text.

#### 33: What is the Coverage tab?

It shows how much of each JavaScript and CSS file was actually used while you interacted with the page. You open it from the Command Menu (Ctrl+Shift+P or Cmd+Shift+P, then type "Coverage"), start recording and reload. Red bars mean unused bytes. A file that is 80% unused on page load is a good candidate for code splitting or for removing dead CSS.

#### 34: What can you do with the Rendering tab?

The Rendering tab (from the three-dot menu > More tools > Rendering) has visual debugging aids:

- **Paint flashing**: highlights areas being repainted in green.
- **Layout shift regions**: highlights areas that moved, in blue.
- **Layer borders**: shows compositor layer and tile borders.
- **Frame rendering stats**: shows frame rate and GPU memory.
- **Scrolling performance issues**: highlights elements that slow down scrolling.
- Emulation for `prefers-color-scheme`, `prefers-reduced-motion`, print media and vision deficiencies.

#### 35: What is the Application panel for?

It lets you inspect and change everything the page stores: cookies, Local Storage, Session Storage, IndexedDB, Cache Storage, Service Workers, the web app manifest, and storage quota usage. It also has a Back/forward cache section that tests whether the page can be restored from bfcache and tells you why if it can't. "Clear site data" is handy for testing a true first visit.

#### 36: What is Lighthouse?

Lighthouse is an open-source tool that loads a page in a controlled environment and audits it. It is built into DevTools (the Lighthouse panel), available as a CLI (`npx lighthouse https://example.com`), as a Node module, and it powers PageSpeed Insights. It gives a score from 0 to 100 and a list of specific problems and suggestions.

#### 37: What categories does Lighthouse check?

Performance, Accessibility, Best Practices and SEO. The old PWA category was removed in Lighthouse 12. The performance score is a weighted mix of lab metrics: First Contentful Paint, Speed Index, Largest Contentful Paint, Total Blocking Time and Cumulative Layout Shift. TBT and LCP carry the most weight. It can't measure INP because it doesn't interact with the page during a normal load, so TBT is used as a lab stand-in.

#### 38: What is PageSpeed Insights and what is the difference between its field data and lab data?

PageSpeed Insights (pagespeed.web.dev) is a Google tool that shows two kinds of data for a URL:

- **Field data** comes from the Chrome UX Report: real Chrome users over the last 28 days. It reports LCP, INP, CLS, FCP and TTFB at the 75th percentile, and it is what Google uses for the Core Web Vitals assessment.
- **Lab data** comes from a Lighthouse run on Google's servers with a simulated mid-range mobile device and a throttled network. It is repeatable and good for debugging, but it is one synthetic visit.

When the two disagree, trust field data for "how are users doing" and lab data for "why is it slow".

#### 39: What is WebPageTest?

WebPageTest is a tool that loads your page in real browsers from many locations and network profiles, then gives you a detailed waterfall, a filmstrip of how the page looked over time, video, Core Web Vitals and more. It is good for comparing before and after, testing from far-away regions, and spotting slow third parties. It can also run scripted multi-step tests and repeat views to check caching.

#### 40: What is the Chrome UX Report (CrUX)?

CrUX is a public dataset of real-user performance data collected from Chrome users who opted in to sharing usage statistics. It covers origins and popular URLs and includes LCP, INP, CLS, FCP and TTFB. You can access it through PageSpeed Insights, the CrUX API, the CrUX History API, BigQuery, the CrUX Vis tool, and Search Console. A page needs enough traffic to appear in the dataset.

#### 41: How do you measure how long your own code takes in the browser?

Use the User Timing API with `performance.mark()` and `performance.measure()`. The measures also show up in the Timings track of the DevTools Performance panel.

```js
performance.mark("render-start");
renderProductList(products);
performance.mark("render-end");

const m = performance.measure("render-products", "render-start", "render-end");
console.log(`${m.name}: ${m.duration.toFixed(1)} ms`);
```

For a quick check you can also use `console.time('label')` and `console.timeEnd('label')`.

#### 42: What does the Navigation Timing API give you?

It gives timestamps for the main page load: redirect, DNS, connection, TLS, request, response, DOM processing and load events. You read it as a `PerformanceNavigationTiming` entry.

```js
const [nav] = performance.getEntriesByType("navigation");
console.log("TTFB", nav.responseStart - nav.startTime);
console.log("DOMContentLoaded", nav.domContentLoadedEventEnd - nav.startTime);
console.log("Load", nav.loadEventEnd - nav.startTime);
console.log("Type", nav.type); // navigate, reload, back_forward, prerender
```

#### 43: Why should you use network and CPU throttling in DevTools?

Developers usually test on fast laptops with fast connections, which hides problems real users have. DevTools lets you slow down the network (for example "Slow 4G" or "3G") and the CPU (4x, 6x, 20x slowdown). Recent versions of Chrome can calibrate CPU throttling against your machine to match "low-tier mobile" and "mid-tier mobile" devices. Throttling is not a perfect copy of a real phone, but it exposes long tasks and slow loading that you would otherwise miss.

#### 44: What is Perfetto?

Perfetto is a tracing tool from Google for Chrome, Android and Linux. You can record a Chrome trace through `chrome://tracing` or the Perfetto UI at ui.perfetto.dev and see what every thread in every process did: the browser process, renderers, GPU and compositor threads. It shows much more than the DevTools Performance panel, which helps when the problem is inside the browser itself or spans several processes. It also has a SQL interface for querying traces.

#### 45: How can you debug a Node.js app with Chrome DevTools?

Start Node with the `--inspect` flag (or `--inspect-brk` to pause on the first line), then open `chrome://inspect` in Chrome and click "inspect" under your target, or click the Node icon in DevTools. You get the Sources panel with breakpoints, the Console, the Memory panel for heap snapshots, and the Performance panel for CPU profiles.

```bash
node --inspect=127.0.0.1:9229 server.js
```

Never expose the inspector port to the public internet. Anyone who connects can run code in your process.

---

### Easy: JavaScript Runtime and Server-Side Fundamentals (46-60)

#### 46: What is the Node.js event loop?

It is the loop that keeps a Node.js process running and decides which callback runs next. It goes through phases in order: timers (`setTimeout`, `setInterval`), pending callbacks, poll (waiting for and running I/O callbacks), check (`setImmediate`), and close callbacks. Between each callback, Node runs `process.nextTick` callbacks and promise microtasks. Your JavaScript runs on one thread, so while one callback runs, nothing else does.

#### 47: Why is Node.js good at handling I/O-heavy workloads?

Node does I/O without blocking the JavaScript thread. When you read a file or query a database, Node hands the work to the operating system or a thread pool and keeps serving other requests. When the result is ready, a callback is queued. One process can keep thousands of connections open with little memory, which is why Node works well for APIs, proxies and real-time apps that mostly wait on networks and databases.

#### 48: What is libuv?

libuv is the C library under Node.js that provides the event loop and asynchronous I/O. It uses the operating system's best mechanism for network I/O (epoll on Linux, kqueue on macOS, IOCP on Windows). For work that has no good async OS API, like most file system calls, DNS lookups with `dns.lookup`, some `crypto` functions and `zlib`, it uses a thread pool with 4 threads by default.

#### 49: What does "blocking the event loop" mean? Give an example.

It means running synchronous code that takes so long that Node can't handle anything else, so every other request waits.

```js
import http from "node:http";

http
  .createServer((req, res) => {
    if (req.url === "/slow") {
      // Blocks every other request for several seconds
      let n = 0;
      for (let i = 0; i < 5e9; i++) n += i;
      return res.end(String(n));
    }
    res.end("ok");
  })
  .listen(3000);
```

Other common causes are `fs.readFileSync` in request handlers, `JSON.parse` on huge payloads, heavy regular expressions, and synchronous crypto like `crypto.pbkdf2Sync`.

#### 50: What are streams in Node.js?

Streams process data piece by piece instead of loading it all into memory. There are four types:

- **Readable**: a source, like `fs.createReadStream` or an HTTP request.
- **Writable**: a destination, like `fs.createWriteStream` or an HTTP response.
- **Duplex**: both, like a TCP socket.
- **Transform**: a duplex that changes data as it passes, like `zlib.createGzip()`.

```js
import { createReadStream, createWriteStream } from "node:fs";
import { createGzip } from "node:zlib";
import { pipeline } from "node:stream/promises";

await pipeline(
  createReadStream("access.log"),
  createGzip(),
  createWriteStream("access.log.gz"),
);
```

#### 51: What is backpressure?

Backpressure is what happens when data comes in faster than it can be written out. If you ignore it, data piles up in memory. In Node, `writable.write()` returns `false` when its internal buffer is full, and you should wait for the `'drain'` event before writing more. `pipeline()` and `.pipe()` handle this for you, which is the main reason to use them.

#### 52: What are worker threads in Node.js?

The `node:worker_threads` module lets you run JavaScript on extra threads inside the same process. Each worker has its own V8 instance and event loop. You use them for CPU-heavy work like image resizing, compression, or big calculations so the main event loop stays responsive. They communicate through `postMessage` and can share memory with `SharedArrayBuffer`.

```js
import { Worker } from "node:worker_threads";

const worker = new Worker(new URL("./hash-worker.js", import.meta.url), {
  workerData: { input: "big string" },
});
worker.on("message", (hash) => console.log(hash));
```

#### 53: What is the `cluster` module?

`node:cluster` starts several Node processes (workers) that share the same server port. The primary process distributes incoming connections between them. This lets a single machine use all its CPU cores, since one Node process runs JavaScript on only one core. Each worker has separate memory, so in-memory state like sessions or caches is not shared. Today many teams run one process per container and let Kubernetes or a process manager like PM2 do the scaling instead.

#### 54: What is the difference between promises and async/await?

There is no real performance difference; `async`/`await` is syntax on top of promises. `await` pauses the async function and resumes it in a microtask when the promise settles. The main benefit is readability and simpler error handling with `try/catch`. A common mistake is awaiting things one by one when they could run at the same time.

```js
// Sequential: total time = a + b
const user = await getUser(id);
const orders = await getOrders(id);

// Parallel: total time = max(a, b)
const [user2, orders2] = await Promise.all([getUser(id), getOrders(id)]);
```

#### 55: What is the difference between `Promise.all`, `Promise.allSettled`, `Promise.race` and `Promise.any`?

- `Promise.all` waits for all promises and rejects as soon as one rejects.
- `Promise.allSettled` waits for all and gives you the status and result of each, never rejecting.
- `Promise.race` settles with the first promise to settle, success or failure.
- `Promise.any` resolves with the first success and only rejects if all fail (with an `AggregateError`).

Use `allSettled` when partial results are fine, like loading several optional widgets. Use `race` or `AbortSignal.timeout()` for timeouts.

#### 56: What is the difference between `process.nextTick` and `setImmediate`?

`process.nextTick` callbacks run right after the current operation, before promise microtasks and before the event loop moves on. `setImmediate` callbacks run in the check phase of the event loop, after I/O polling. Overusing `nextTick` recursively can starve I/O because the loop never gets to continue. For most code, `queueMicrotask` or `setImmediate` is the safer choice.

```js
setImmediate(() => console.log("immediate"));
Promise.resolve().then(() => console.log("promise"));
process.nextTick(() => console.log("nextTick"));
// nextTick, promise, immediate
```

#### 57: How are browser Web Workers and Node.js worker threads similar and different?

Both run JavaScript on a separate thread with its own global scope and event loop, both use `postMessage`, and both support transferring `ArrayBuffer` and sharing `SharedArrayBuffer`. Differences: Web Workers have no DOM access but have browser APIs like `fetch` and `IndexedDB`. Node worker threads have Node APIs like `fs` and can receive startup data through `workerData`. Both are fairly heavy to create, so you usually keep a pool of them instead of creating one per job.

#### 58: What are Deno and Bun?

Both are JavaScript and TypeScript runtimes that compete with Node.js.

- **Deno** is built on V8 and Rust. It runs TypeScript directly, is secure by default (you grant file and network access with flags), uses web-standard APIs, and since Deno 2 works with most npm packages.
- **Bun** is built on JavaScriptCore (Safari's engine) and written in Zig. It focuses on fast startup and includes a package manager, bundler and test runner. It aims to be a drop-in Node replacement.

Both can be faster than Node in some benchmarks, but real apps are usually limited by I/O and databases, so measure your own workload before switching.

#### 59: How do you check memory usage in a Node.js process?

Use `process.memoryUsage()`.

```js
const m = process.memoryUsage();
console.log({
  rssMB: (m.rss / 1024 / 1024).toFixed(1), // total memory held by the process
  heapUsedMB: (m.heapUsed / 1024 / 1024).toFixed(1), // JS objects in use
  heapTotalMB: (m.heapTotal / 1024 / 1024).toFixed(1),
  externalMB: (m.external / 1024 / 1024).toFixed(1), // memory for C++ objects tied to JS
  arrayBuffersMB: (m.arrayBuffers / 1024 / 1024).toFixed(1),
});
```

If `heapUsed` keeps growing across many requests and never drops after garbage collection, you probably have a leak. If `rss` grows while the heap is flat, look at Buffers, native modules or memory fragmentation.

#### 60: How should a Node.js server shut down gracefully?

On `SIGTERM` (what Docker and Kubernetes send first), stop accepting new connections, let in-flight requests finish, close database pools, and then exit. Add a timeout so it doesn't hang forever.

```js
const server = app.listen(3000);

process.on("SIGTERM", () => {
  console.log("SIGTERM received, closing");
  server.close(async () => {
    await db.end();
    process.exit(0);
  });
  server.closeIdleConnections();
  setTimeout(() => process.exit(1), 10_000).unref();
});
```

---

### Easy: Networking and Web Protocols (61-75)

#### 61: What is the main difference between HTTP/1.1 and HTTP/2?

HTTP/1.1 sends one request at a time per connection, so browsers open up to 6 connections per origin to load things in parallel. HTTP/2 multiplexes many requests and responses over a single connection as interleaved frames. It also compresses headers (HPACK) and uses a binary format. This makes old tricks like domain sharding and spriting less useful, and they can even hurt on HTTP/2.

#### 62: What is HTTP/3?

HTTP/3 is HTTP running on QUIC, a transport protocol built on UDP instead of TCP. QUIC has TLS 1.3 built in, so setting up a secure connection takes fewer round trips. Each stream is independent, so a lost packet only stalls the stream it belongs to, not all of them. It also supports connection migration, which helps when a phone switches from Wi-Fi to mobile data. Servers advertise it with the `Alt-Svc` header or an HTTPS DNS record.

#### 63: Why does HTTPS add latency, and how does TLS 1.3 help?

Before any HTTP data is sent, the client and server do a TLS handshake to agree on keys and check the certificate. With TLS 1.2 that took two round trips on top of the TCP handshake. TLS 1.3 cuts it to one round trip, and for returning visitors it can support 0-RTT resumption where the first request is sent with the handshake. Reusing connections (keep-alive) avoids paying the handshake cost again.

#### 64: What is the difference between TCP and UDP?

TCP is connection-based and reliable. It guarantees ordered delivery, retransmits lost packets and controls how fast data is sent. UDP just sends packets with no guarantees of delivery or order, so it has less overhead. HTTP/1.1 and HTTP/2 use TCP. HTTP/3 uses QUIC, which runs on UDP but adds its own reliability and congestion control per stream. DNS and many real-time apps like video calls also use UDP.

#### 65: What is a DNS lookup, and what does TTL mean?

A DNS lookup turns a domain name like `api.example.com` into an IP address. On a cold lookup this can take anywhere from a few to a few hundred milliseconds. The TTL (time to live) on a DNS record says how long resolvers and browsers can cache the answer. A longer TTL means fewer lookups, but changes like moving to a new server take longer to reach users. Chrome also keeps its own short-lived host cache.

#### 66: What is a CDN?

A Content Delivery Network is a set of servers (edges) spread across many locations. Users connect to a nearby edge, which serves cached copies of your content. This cuts latency because the data travels a shorter distance, reduces load on your origin server, and helps absorb traffic spikes and some attacks. CDNs are used for static assets, images, video, and more and more for cached HTML and API responses.

#### 67: What is the difference between WebSockets and Server-Sent Events?

**WebSockets** give you a full two-way connection. Both sides can send messages at any time. Good for chat, multiplayer games and collaborative editing.

**Server-Sent Events (SSE)** use a normal HTTP response that stays open, and only the server sends data. The browser's `EventSource` reconnects automatically. Good for notifications, live feeds and streaming AI responses.

```js
const es = new EventSource("/events");
es.onmessage = (e) => console.log(JSON.parse(e.data));
```

SSE works well with HTTP/2 because many streams share one connection. On HTTP/1.1 browsers limit you to about 6 open connections per origin.

#### 68: What is the difference between Gzip and Brotli?

Both compress text responses like HTML, CSS, JS and JSON. Brotli usually produces files 15 to 25% smaller than Gzip for web content, partly because it has a built-in dictionary of common web strings. Brotli at high levels (10 to 11) is slow to compress, so you use it for pre-compressed static files at build time and a lower level (around 4 to 6) for dynamic responses. All modern browsers support Brotli over HTTPS. Chrome also supports Zstandard (`zstd`), which compresses quickly at good ratios.

#### 69: What does the `Cache-Control` header do?

It tells browsers and CDNs whether and how long they can cache a response. Common values:

- `max-age=31536000, immutable`: cache for a year and don't revalidate. Use for files with a hash in the name, like `app.3f9a1c.js`.
- `no-cache`: you can store it, but you must check with the server before using it.
- `no-store`: don't store it at all. Use for sensitive data.
- `private`: only the browser can cache it, not shared caches like CDNs.
- `s-maxage=600`: separate lifetime for shared caches.

```http
Cache-Control: public, max-age=31536000, immutable
```

#### 70: What is an ETag and how does it produce a 304 response?

An ETag is an identifier for a specific version of a resource, often a hash of its content. The server sends `ETag: "abc123"`. Later, when the cached copy needs revalidation, the browser sends `If-None-Match: "abc123"`. If the resource hasn't changed, the server replies `304 Not Modified` with no body, so the browser reuses its cached copy and saves bandwidth. You still pay for one round trip.

#### 71: What are `Last-Modified` and `If-Modified-Since`?

They do the same job as ETags but use dates. The server sends `Last-Modified: Tue, 20 Oct 2026 10:00:00 GMT`, and the browser later asks with `If-Modified-Since` and that date. If nothing changed, the server returns 304. Dates have one-second precision and can be unreliable across several servers with different file times, so ETags are usually preferred. When both are present, `If-None-Match` takes priority.

#### 72: What is the difference between `preload` and `prefetch`?

`preload` is for resources the current page needs soon. It is fetched at high priority. `prefetch` is for resources the user will probably need on the next page. It is fetched at the lowest priority when the browser is idle and kept in the HTTP cache.

```html
<link rel="preload" href="/css/above-fold.css" as="style" />
<link rel="prefetch" href="/js/checkout.js" />
```

For whole next-page navigations, the Speculation Rules API (Chrome) is now the better option because it can prefetch or even prerender the page.

#### 73: What is HTTP keep-alive?

Keep-alive means reusing the same TCP connection for several requests instead of opening a new one each time. Without it, each request pays for a TCP handshake and possibly a TLS handshake. In HTTP/1.1 it is the default. On the server side, make sure your HTTP client (for example in Node) reuses connections to upstream services. Node's global `fetch` (undici) and `http.globalAgent` in recent Node versions keep connections alive by default.

#### 74: What is RTT and why does it matter for web performance?

RTT (round-trip time) is how long it takes a packet to go to the server and back. Many steps of a page load cost at least one RTT each: DNS, TCP handshake, TLS handshake, each redirect, and the request itself. On a mobile network RTT can be 100 ms or more, so a page that needs 8 round trips before the first byte arrives already loses close to a second. Reducing round trips (fewer redirects, connection reuse, a CDN close to users, HTTP/3) is often more effective than reducing bytes.

#### 75: What is head-of-line blocking?

It is when one slow or lost item holds up everything behind it. In HTTP/1.1, a slow response blocks the next request on that connection. HTTP/2 fixed that at the HTTP level, but because everything shares one TCP connection, a single lost packet still stalls all streams until it is resent. HTTP/3 over QUIC fixes this at the transport level because each stream is delivered independently.

---

### Easy: Databases and Data Access (76-90)

#### 76: What is a database index?

An index is a separate data structure, usually a B-tree, that keeps a column's values sorted with pointers to the rows. It lets the database find matching rows without scanning the whole table, much like a book index. Indexes speed up reads, `WHERE`, `JOIN` and `ORDER BY`, but they slow down writes a bit and take disk space, because every insert or update must also update the index.

```sql
CREATE INDEX idx_orders_customer_id ON orders (customer_id);
```

#### 77: What is a query plan?

A query plan is the set of steps the database decides to use to run your query: which tables to read first, whether to use an index or scan the table, how to join, and how to sort. The query planner picks the plan it estimates is cheapest, based on table statistics. Looking at the plan is the first step when a query is slow.

#### 78: What is the difference between `EXPLAIN` and `EXPLAIN ANALYZE` in PostgreSQL?

`EXPLAIN` shows the plan the database would use and its estimated costs and row counts, without running the query. `EXPLAIN ANALYZE` actually runs the query and shows real timings and row counts next to the estimates. Big gaps between estimated and actual rows often explain a bad plan. Be careful with `EXPLAIN ANALYZE` on `INSERT`, `UPDATE` or `DELETE` because the changes really happen; wrap it in a transaction and roll back.

```sql
BEGIN;
EXPLAIN (ANALYZE, BUFFERS) DELETE FROM sessions WHERE expires_at < now();
ROLLBACK;
```

#### 79: What is a database transaction?

A transaction groups several statements so they either all succeed or all fail. It follows the ACID properties: atomicity, consistency, isolation and durability. For example, moving money between two accounts should debit one and credit the other in one transaction. From a performance view, keep transactions short. Long transactions hold locks, block other queries, and in PostgreSQL they stop VACUUM from cleaning up dead rows.

#### 80: What is the N+1 query problem?

It happens when code runs one query to load a list, then one more query for each item in the list. With 100 items you get 101 queries, each paying network and parse overhead.

```js
// N+1: one query for posts, then one per post for the author
const posts = await db.query("SELECT * FROM posts LIMIT 100");
for (const post of posts.rows) {
  post.author = (
    await db.query("SELECT * FROM users WHERE id = $1", [post.user_id])
  ).rows[0];
}

// Fixed: one query with a JOIN (or a second query with WHERE id = ANY($1))
const { rows } = await db.query(`
  SELECT p.*, u.name AS author_name
  FROM posts p JOIN users u ON u.id = p.user_id
  LIMIT 100`);
```

ORMs make this easy to cause by accident through lazy-loaded relations.

#### 81: What is a database connection pool?

A pool keeps a set of open database connections and lends them to your code when needed. Opening a new connection is slow, since it needs a TCP handshake, maybe TLS, authentication and, in PostgreSQL, starting a new backend process. With a pool, a request borrows a connection, runs its query and returns it.

```js
import pg from "pg";
const pool = new pg.Pool({ max: 10, idleTimeoutMillis: 30_000 });

const { rows } = await pool.query("SELECT now()");
```

#### 82: Why is `SELECT *` often a bad idea?

It fetches every column, even ones you don't use. That means more data read from disk, more data sent over the network, more memory to parse, and it can stop the database from using an index-only scan. It also breaks silently when someone adds a large column like a JSON blob. Select only the columns you need.

#### 83: What is the difference between offset and cursor pagination?

Offset pagination uses `LIMIT 20 OFFSET 10000`. It is simple, but the database still has to read and throw away the first 10,000 rows, so deep pages get slower. Rows can also be skipped or repeated if data changes between requests.

Cursor (keyset) pagination remembers the last item seen and asks for rows after it. With an index it stays fast on every page.

```sql
-- Offset
SELECT id, title FROM posts ORDER BY id DESC LIMIT 20 OFFSET 10000;

-- Cursor
SELECT id, title FROM posts WHERE id < $1 ORDER BY id DESC LIMIT 20;
```

#### 84: What is Redis commonly used for?

Redis is an in-memory key-value store. Because it keeps data in RAM, reads and writes take well under a millisecond. Common uses are caching database results or rendered pages, storing sessions, rate limiting, counters and leaderboards (sorted sets), queues, pub/sub messages and distributed locks. Valkey is an open-source fork of Redis that works the same way for these use cases.

#### 85: What does TTL mean in Redis?

TTL (time to live) is how long a key exists before Redis deletes it automatically. You set it with `EX` on `SET`, or with `EXPIRE`. `TTL key` returns how many seconds are left, `-1` if there is no expiry, and `-2` if the key doesn't exist.

```bash
SET product:42 '{"name":"Lamp"}' EX 300
TTL product:42   # 300
```

Putting a TTL on cache keys keeps stale data from living forever and stops memory from filling up with old entries.

#### 86: What is the cache-aside pattern?

The application checks the cache first. On a miss, it reads from the database, stores the result in the cache with a TTL, and returns it. On writes, it updates the database and deletes the cache key.

```js
async function getProduct(id) {
  const key = `product:${id}`;
  const cached = await redis.get(key);
  if (cached) return JSON.parse(cached);

  const { rows } = await db.query(
    "SELECT id, name, price FROM products WHERE id = $1",
    [id],
  );
  await redis.set(key, JSON.stringify(rows[0]), { EX: 300 });
  return rows[0];
}

async function updateProduct(id, data) {
  await db.query("UPDATE products SET name = $1, price = $2 WHERE id = $3", [
    data.name,
    data.price,
    id,
  ]);
  await redis.del(`product:${id}`);
}
```

#### 87: How do you check if a MongoDB query uses an index?

Run `explain("executionStats")` on the query. Look at the winning plan stage: `IXSCAN` means it used an index, `COLLSCAN` means it scanned every document. Compare `totalDocsExamined` with `nReturned`. If you examine 100,000 documents to return 10, you need a better index.

```js
db.orders.find({ customerId: 42, status: "paid" }).explain("executionStats");

db.orders.createIndex({ customerId: 1, status: 1 });
```

#### 88: What is a projection in MongoDB?

A projection limits which fields are returned. It reduces network transfer and memory use, and if the index contains all requested fields, MongoDB can answer from the index alone (a covered query) without reading the documents.

```js
db.users.find({ country: "GE" }, { name: 1, email: 1, _id: 0 });
```

#### 89: What is VACUUM in PostgreSQL?

When you update or delete a row in PostgreSQL, the old version isn't removed right away (because other transactions might still need it). These dead rows take up space and slow down scans. VACUUM marks that space as reusable and updates visibility information. Autovacuum runs this in the background automatically. `VACUUM FULL` rewrites the whole table to shrink it on disk, but it locks the table, so avoid it on busy tables. `ANALYZE` updates the statistics the planner uses.

#### 90: What is an ORM, and what performance costs can it add?

An ORM (Object-Relational Mapper) such as Prisma, TypeORM, Sequelize, Drizzle or Mongoose lets you work with database rows as objects. It saves time, but it can hide costs:

- N+1 queries from lazy-loaded relations.
- Fetching every column when you need two.
- Turning each row into a full object with methods and change tracking (hydration), which costs CPU and memory for large result sets.
- Generating SQL that doesn't use your indexes well.

Turn on query logging during development so you can see the SQL it actually sends.

---

### Easy: Operating Systems and Server Resources (91-105)

#### 91: What is the difference between a process and a thread?

A process is a running program with its own memory space, file descriptors and resources. A thread is a unit of execution inside a process. Threads in the same process share memory. Creating a process is more expensive and processes are isolated from each other. Threads are lighter but need care when sharing data. A Node.js process runs your JavaScript on one main thread, but it also has threads for libuv's pool, V8's garbage collector and compiler.

#### 92: What is a file descriptor, and what does `EMFILE` mean?

A file descriptor is a number the operating system gives a process for each open file, socket or pipe. Every open network connection uses one. Each process has a limit (often 1,024 by default for the soft limit on Linux). When you hit it, calls fail with `EMFILE: too many open files`. You fix it by raising the limit with `ulimit -n` or the systemd `LimitNOFILE` setting, and by checking for connections or files that are never closed.

#### 93: What is a system call?

A system call is how a program asks the operating system kernel to do something it can't do directly, like reading a file (`read`), opening a socket (`socket`), allocating memory (`mmap`) or creating a process (`fork`). Each call switches from user mode to kernel mode, which has a small cost. Code that makes many tiny system calls, like writing one byte at a time, can be slow. Buffering helps.

#### 94: What is the difference between CPU utilization and load average?

CPU utilization is the percentage of time the CPU was busy. Load average (shown by `uptime` and `top`) is the average number of processes running or waiting to run over 1, 5 and 15 minutes. On Linux it also counts processes waiting on disk I/O. Compare it to the number of cores: a load of 4 on a 4-core machine means it is fully busy, and a load of 8 means work is queuing.

#### 95: What is the difference between RSS and heap memory?

RSS (resident set size) is how much physical RAM the whole process is using right now: code, stack, heap, buffers and native libraries. The heap is the part where the program allocates objects. In Node.js, the V8 heap holds JavaScript objects, while Buffers and native memory live outside it but still count in RSS. Container memory limits are enforced on total memory, not on the V8 heap.

#### 96: What is a memory leak?

A memory leak is memory the program keeps holding but no longer needs. In JavaScript, the garbage collector frees objects only when nothing references them, so leaks happen when references are kept by mistake. Common causes:

- Global arrays or maps that keep growing (unbounded caches).
- Event listeners that are added but never removed.
- Timers that never get cleared.
- Closures that capture large objects.
- Detached DOM nodes still referenced from JavaScript.

The symptom is memory that keeps rising over time, eventually leading to slow garbage collection or crashes.

#### 97: What is swap, and why is it bad for server performance?

Swap is disk space the operating system uses as extra memory when RAM runs low. Moving memory pages to and from disk is thousands of times slower than RAM, so a server that is swapping becomes very slow, and the cause can be hard to spot because CPU usage may look normal. Many container setups disable swap and prefer to kill the process (OOM) rather than let it crawl. `free -h` and `vmstat` show swap usage.

#### 98: What is I/O wait?

I/O wait (`wa` in `top`, `%iowait` in `iostat`) is the percentage of time the CPU sat idle while there were outstanding disk I/O requests. High I/O wait means your workload is limited by disk speed, not by CPU. Common causes are heavy logging to disk, database queries that don't fit in memory, and swapping.

#### 99: What is a socket and a port?

A socket is an endpoint for network communication, identified by an IP address and a port number. A server listens on a port, like 443 for HTTPS. Each TCP connection is identified by four values: source IP, source port, destination IP and destination port. When your server connects out to a database, the OS picks a temporary source port from the ephemeral port range.

#### 100: What are `top` and `htop` used for?

They show live system activity: CPU usage per core, memory and swap, load average, and a list of processes sorted by CPU or memory. `htop` is a friendlier version with colors, a tree view, mouse support and easy sorting and filtering. In `top`, press `1` to see each core, `M` to sort by memory and `P` to sort by CPU. In `htop`, press `H` to show or hide threads.

#### 101: What happens when a Docker container hits its memory limit?

If a container uses more memory than its limit (`--memory 512m`), the kernel's OOM killer stops the process. The container exits with code 137 (128 + 9, meaning SIGKILL), and `docker inspect` shows `OOMKilled: true`. For Node.js, keep the V8 heap below the container limit with `--max-old-space-size`, leaving room for Buffers and native memory.

```bash
docker run --memory 512m -e NODE_OPTIONS="--max-old-space-size=384" my-api
```

#### 102: How do CPU limits work in Docker?

`--cpus 1.5` lets the container use up to 1.5 CPUs' worth of time. Under the hood it uses CFS quota and period settings in cgroups. If the container uses its quota early in a period (100 ms by default), it is throttled until the next period, which shows up as latency spikes. `--cpu-shares` (or CPU weight in cgroup v2) only sets relative priority when the machine is busy and doesn't cap usage.

#### 103: What is the difference between SIGTERM and SIGKILL?

SIGTERM asks a process to stop. The process can catch it, clean up and exit. SIGKILL forces the process to stop immediately; it can't be caught or ignored. `docker stop` and Kubernetes send SIGTERM first, wait for a grace period (10 seconds in Docker, 30 seconds in Kubernetes by default), then send SIGKILL. If your app doesn't handle SIGTERM, in-flight requests are dropped.

#### 104: What does the `ss` command do?

`ss` shows socket information. It is the modern replacement for `netstat` and is faster on busy servers.

```bash
ss -tlnp            # TCP sockets that are listening, with process names
ss -tan state established | wc -l   # count established TCP connections
ss -s               # summary by state
```

It helps answer questions like "how many connections does my server have?" and "is something listening on port 3000?".

#### 105: What is `ulimit`?

`ulimit` shows and sets per-process resource limits in the shell, like the number of open files (`-n`), the number of processes (`-u`), and core dump size (`-c`). Soft limits can be raised up to the hard limit by the user. For services, set limits in the systemd unit file (`LimitNOFILE=65535`) or in Docker with `--ulimit nofile=65535:65535`, because a `ulimit` in your shell doesn't apply to them.

```bash
ulimit -n        # show open file limit
ulimit -n 65535  # raise it for this shell
```

---

### Easy: Cloud Infrastructure and Delivery (106-120)

#### 106: What is the difference between vertical and horizontal scaling?

Vertical scaling means giving one machine more resources: a bigger instance with more CPU and RAM. It is simple but has an upper limit and often needs a restart. Horizontal scaling means adding more machines behind a load balancer. It can grow much further and survives single-machine failures, but your app needs to be stateless (sessions and caches stored outside the process).

#### 107: What is a load balancer?

A load balancer sits in front of a group of servers and spreads incoming requests between them. It runs health checks and stops sending traffic to unhealthy servers. It often handles TLS termination too. Common strategies are round robin, least connections and hashing on a key. Examples are AWS Application Load Balancer, Nginx, HAProxy and Envoy.

#### 108: What is the difference between an AWS ALB and an NLB?

An **Application Load Balancer (ALB)** works at layer 7 (HTTP). It can route by path, host or headers, terminate TLS, handle WebSockets and gRPC, and integrate with WAF.

A **Network Load Balancer (NLB)** works at layer 4 (TCP, UDP, TLS). It handles very high connection rates with very low added latency, supports static IPs, and passes through the client IP. Use it for non-HTTP traffic or when you need raw TCP performance.

#### 109: What is autoscaling?

Autoscaling adds or removes servers automatically based on load. In AWS, an Auto Scaling group can use a target tracking policy, for example "keep average CPU at 50%" or "keep requests per target at 1,000". It saves money when traffic is low and adds capacity when traffic rises. New instances take time to start and warm up, so autoscaling doesn't help with sudden spikes unless you keep some spare capacity.

#### 110: What CloudWatch metrics would you look at first when an API on AWS gets slow?

For an ALB: `TargetResponseTime` (look at p95 and p99, not just average), `RequestCount`, `HTTPCode_Target_5XX_Count`, `HTTPCode_ELB_5XX_Count`, and `UnHealthyHostCount`. For EC2 or ECS: `CPUUtilization` and memory (memory needs the CloudWatch agent on EC2). For RDS: `CPUUtilization`, `DatabaseConnections`, `ReadLatency`, `WriteLatency` and `FreeableMemory`. This quickly tells you if the problem is in the app, the database or the load balancer.

#### 111: What is a cache hit ratio?

It is the percentage of requests served from cache instead of going to the origin. If a CDN gets 1,000 requests and 900 are served from the edge, the hit ratio is 90%. A higher ratio means faster responses and less origin load. Low ratios usually come from short TTLs, `Cache-Control: private` or `no-store` on cacheable content, or cache keys that include unneeded query strings, cookies or headers.

#### 112: How do CloudFront and Cloudflare cache content at the edge?

When a user requests a file, the nearest edge location checks its cache. On a hit it returns the file immediately. On a miss it fetches the file from your origin (or from a middle tier like CloudFront Regional Edge Caches or Cloudflare Tiered Cache), stores it, and returns it. How long it stays cached depends on your `Cache-Control` headers and the CDN's cache policy settings. You can force updates with an invalidation (CloudFront) or purge (Cloudflare), but versioned file names are better.

#### 113: Why serve static files from S3 instead of your app server?

S3 is cheap, durable and scales without you doing anything. Serving files from it (usually behind CloudFront) takes that load off your Node.js servers, which are better spent on dynamic requests. For user uploads and downloads, you can give the browser a presigned URL so it talks to S3 directly and the file never passes through your server.

```js
import { S3Client, GetObjectCommand } from "@aws-sdk/client-s3";
import { getSignedUrl } from "@aws-sdk/s3-request-presigner";

const s3 = new S3Client({ region: "eu-central-1" });
const url = await getSignedUrl(
  s3,
  new GetObjectCommand({ Bucket: "reports", Key: "q3.pdf" }),
  { expiresIn: 300 },
);
```

#### 114: What is a reverse proxy?

A reverse proxy sits in front of your application servers and receives requests on their behalf. It can terminate TLS, compress responses, serve static files, cache, buffer slow clients, enforce rate limits and spread traffic across backends. Nginx, HAProxy, Caddy, Envoy and Traefik are common choices. A Node.js app behind Nginx doesn't have to deal with slow clients holding connections open.

#### 115: How do you turn on compression in Nginx?

Gzip is built in. Brotli needs the `ngx_brotli` module.

```nginx
gzip on;
gzip_comp_level 5;
gzip_min_length 1024;
gzip_types text/css application/javascript application/json image/svg+xml;
gzip_vary on;

# With ngx_brotli installed
brotli on;
brotli_comp_level 5;
brotli_types text/css application/javascript application/json image/svg+xml;
```

`text/html` is always compressed when gzip is on. Don't compress images like JPEG, PNG or WebP, they are already compressed. For static files, pre-compress at build time and use `gzip_static on` / `brotli_static on`.

#### 116: What is a health check?

A health check is a request a load balancer or orchestrator sends regularly to see if an instance is working, usually something like `GET /healthz` expecting a 200 response. Instances that fail several checks in a row are taken out of rotation. Keep the endpoint cheap. A health check that runs heavy database queries can add load and fail exactly when the system is busy.

#### 117: What are resource requests and limits in Kubernetes?

A **request** is what the scheduler reserves for a container. It decides which node the pod goes on. A **limit** is the maximum the container can use. Going over the CPU limit leads to throttling. Going over the memory limit gets the container OOM killed.

```yaml
resources:
  requests:
    cpu: "500m"
    memory: "512Mi"
  limits:
    memory: "512Mi"
```

Many teams set memory limit equal to the request and skip the CPU limit to avoid throttling, relying on requests for fair sharing.

#### 118: Why should CI pipelines cache dependencies?

Installing dependencies from scratch on every run downloads the same packages again and again, which can take minutes. Caching the package manager's store (like `~/.npm` or the pnpm store) keyed on the lockfile hash makes installs much faster. Build tools like Turborepo and Nx can also cache build and test outputs so unchanged packages are skipped.

```yaml
# GitHub Actions
- uses: actions/setup-node@v4
  with:
    node-version: 24
    cache: npm
- run: npm ci
```

#### 119: What is bundle analysis, and why run it in CI?

Bundle analysis shows what is inside your JavaScript bundles and how big each part is. Tools include `rollup-plugin-visualizer` (works with Vite), `webpack-bundle-analyzer`, `source-map-explorer` and `size-limit`. Running a size check in CI catches a new heavy dependency before it reaches production, instead of finding out from users later.

```json
// package.json with size-limit
"size-limit": [{ "path": "dist/assets/index-*.js", "limit": "170 kB" }]
```

#### 120: What is Infrastructure as Code, and how does it help with performance work?

Infrastructure as Code (IaC) means describing servers, networks, load balancers and databases in files, using tools like Terraform, OpenTofu, AWS CDK or Pulumi. For performance work, it lets you create a test environment that matches production exactly, run a load test, and tear it down. You can also review infrastructure changes like instance sizes and timeouts in pull requests, the same way you review code.

---

### Easy: Observability, Profiling and Reliability (121-135)

#### 121: What is the difference between latency and throughput?

Latency is how long a single request takes, for example 120 ms. Throughput is how many requests the system handles per unit of time, for example 2,000 requests per second. They are related but different: a system can have high throughput and poor latency if requests wait in a queue. When you push throughput close to capacity, latency usually rises sharply.

#### 122: What are latency percentiles, and why are they better than averages?

A percentile tells you the value below which a certain share of requests fall. p50 (median) is the typical request. p95 means 95% of requests were faster than that value. p99 shows the slowest 1%. Averages hide outliers: if 99 requests take 50 ms and one takes 5 seconds, the average is about 100 ms, which describes no real request. The slow tail is often where users notice problems, and on a page that makes many requests, most users hit at least one slow one.

#### 123: What is error rate?

Error rate is the share of requests that fail, usually counted as 5xx responses, timeouts and dropped connections divided by total requests. 4xx responses are usually the client's fault and are tracked separately, though a sudden spike in 4xx can still mean a bug, like a broken frontend sending bad requests. Error rate is one of the "golden signals" along with latency, traffic and saturation.

#### 124: What is saturation?

Saturation is how full a resource is, or how much work is waiting for it. Examples are CPU run queue length, memory close to the limit, a connection pool with requests waiting, disk queue depth, or Node.js event loop delay. A resource can be at 70% utilization and already have a queue, so saturation is often an earlier warning than utilization.

#### 125: What is distributed tracing?

Distributed tracing follows one request as it moves through many services. Each service records what it did and how long it took, and passes a trace ID along to the next service in a header. A tracing UI like Jaeger, Grafana Tempo, Honeycomb or Datadog then shows the full request as a timeline, so you can see exactly which service or database call made it slow.

#### 126: What is OpenTelemetry?

OpenTelemetry (OTel) is an open, vendor-neutral standard and set of SDKs for collecting traces, metrics and logs. You instrument your code once and send the data to any backend. In Node.js, the auto-instrumentation package hooks into common libraries like `http`, Express, `pg` and Redis clients without code changes.

```bash
npm install @opentelemetry/api @opentelemetry/auto-instrumentations-node
export OTEL_SERVICE_NAME=orders-api
export OTEL_EXPORTER_OTLP_ENDPOINT=http://otel-collector:4318
node --import @opentelemetry/auto-instrumentations-node/register server.js
```

#### 127: What is a span?

A span is one unit of work inside a trace, like "handle HTTP request", "SQL SELECT orders" or "call payment API". It has a name, a start time, a duration, attributes (like `http.route` or `db.statement`), a status and a parent span ID. Spans nest to form a tree that shows how the request flowed and where the time went.

#### 128: What is structured logging?

Structured logging means writing logs as data, usually JSON, instead of free text. Each line has fields you can search and filter on, like `level`, `msg`, `requestId`, `userId` and `durationMs`. Pino is the most common fast logger for Node.js.

```js
import pino from "pino";
const log = pino({ level: "info" });

log.info(
  { requestId: req.id, route: "/orders", durationMs: 42 },
  "request completed",
);
// {"level":30,"time":1761213600000,"requestId":"a1b2","route":"/orders","durationMs":42,"msg":"request completed"}
```

#### 129: What is APM?

APM (Application Performance Monitoring) tools like Datadog, New Relic, Dynatrace, Elastic APM or Sentry Performance collect request traces, response times, error rates, database query timings and external call latency from your application, usually through an agent or OpenTelemetry. They let you find the slowest endpoints and the queries or services behind them without adding logs everywhere.

#### 130: What is a flame graph?

A flame graph is a picture of where CPU time is spent, built from many stack samples. Each box is a function. Its width shows how much of the total time that function (and the functions it called) was on the CPU. Boxes stacked on top are the functions it called. Wide boxes at the top of a stack are where the CPU actually did the work, and they are usually your best place to optimize. Colors usually have no meaning.

#### 131: What is load testing? Show a simple example.

Load testing sends realistic traffic to a system to see how it behaves at a certain load: response times, error rates and resource usage. k6 is a popular tool where tests are written in JavaScript.

```js
// load-test.js, run with: k6 run load-test.js
import http from "k6/http";
import { check, sleep } from "k6";

export const options = {
  vus: 50,
  duration: "2m",
  thresholds: {
    http_req_duration: ["p(95)<300"],
    http_req_failed: ["rate<0.01"],
  },
};

export default function () {
  const res = http.get("https://staging.example.com/api/products");
  check(res, { "status is 200": (r) => r.status === 200 });
  sleep(1);
}
```

#### 132: What is the difference between a stress test and a soak test?

A **stress test** pushes load higher and higher until the system breaks, to find its limits and see how it fails (slow responses, errors, crashes) and whether it recovers.

A **soak test** (endurance test) runs normal or slightly high load for a long time, like 4 to 24 hours. It finds problems that only show up over time: memory leaks, connection leaks, disks filling with logs, and slowly growing response times.

#### 133: What is autocannon?

autocannon is a fast HTTP benchmarking tool written in Node.js. It is handy for quick tests of a single endpoint during development.

```bash
npx autocannon -c 100 -d 30 http://localhost:3000/api/products
```

This opens 100 connections for 30 seconds and reports requests per second, latency percentiles and throughput. Run it from a different machine than the server if you can, or the load generator competes with the server for CPU.

#### 134: What is the difference between an SLI, an SLO and an SLA?

- **SLI (Service Level Indicator)**: a measurement, like "percentage of requests served in under 300 ms".
- **SLO (Service Level Objective)**: an internal target for that measurement, like "99% of requests under 300 ms over 28 days".
- **SLA (Service Level Agreement)**: a contract with customers that includes consequences, like refunds, if a level isn't met. SLAs are usually looser than SLOs.

#### 135: What is an error budget?

An error budget is the amount of failure an SLO allows. If your availability SLO is 99.9% over 30 days, you are allowed 0.1% failure, which is about 43 minutes of full downtime. While you have budget left, the team can ship features quickly. When the budget is used up, the focus shifts to reliability work until it recovers.

---

### Easy: Web Performance Standards and Metrics (136-150)

#### 136: What are the Core Web Vitals and their "good" thresholds?

The three Core Web Vitals, measured at the 75th percentile of page loads:

| Metric                          | Measures         | Good           | Poor             |
| ------------------------------- | ---------------- | -------------- | ---------------- |
| LCP (Largest Contentful Paint)  | Loading          | 2.5 s or less  | more than 4 s    |
| INP (Interaction to Next Paint) | Responsiveness   | 200 ms or less | more than 500 ms |
| CLS (Cumulative Layout Shift)   | Visual stability | 0.1 or less    | more than 0.25   |

INP replaced First Input Delay (FID) as a Core Web Vital in March 2024.

#### 137: What is LCP?

Largest Contentful Paint is the time from the start of navigation until the largest image, video poster or text block in the viewport is rendered. It is a good stand-in for "when did the main content appear". The usual LCP element is a hero image or headline. Main causes of poor LCP are slow server response, render-blocking CSS and JS, the LCP image being found late or lazy loaded, and large unoptimized images.

#### 138: What is INP?

Interaction to Next Paint measures how quickly the page responds to clicks, taps and key presses. For each interaction it measures the time from the input to when the next frame is painted, including the input delay, the event handler time and the rendering time. The page's INP is roughly the worst interaction during the visit (for pages with many interactions, a few outliers are ignored). Long tasks and heavy event handlers are the most common causes of poor INP.

#### 139: What is CLS?

Cumulative Layout Shift measures how much visible content moves around unexpectedly. Each shift gets a score based on how much of the viewport moved and how far. Shifts are grouped into windows (up to 5 seconds, with less than 1 second between shifts), and CLS is the worst window. Shifts within 500 ms of a user input don't count. Common causes are images without dimensions, ads and embeds without reserved space, late-loading web fonts and content injected above existing content.

#### 140: What is First Contentful Paint (FCP)?

FCP is the time until the browser renders the first bit of content from the DOM: text, an image, an SVG or a non-white canvas. It tells the user something is happening. A good FCP is 1.8 seconds or less. It is mainly affected by server response time and render-blocking resources.

#### 141: What is Time to First Byte (TTFB)?

TTFB is the time from the start of navigation until the first byte of the response arrives. It includes redirects, DNS, connection setup, TLS and the time the server spends generating the response. A good TTFB is 0.8 seconds or less. Everything else on the page waits for it, so a slow TTFB pushes FCP and LCP later.

#### 142: What is Speed Index?

Speed Index is a lab metric that measures how quickly the visible content of a page fills in during load. It is calculated from video frames: the faster the page gets visually complete, the lower (better) the score. Two pages with the same load time can have very different Speed Index values if one shows content gradually and the other shows nothing until the end. Lighthouse and WebPageTest report it.

#### 143: What is Total Blocking Time (TBT)?

TBT is a lab metric that adds up the "blocking" part of every long task between First Contentful Paint and Time to Interactive. For each task over 50 ms, the part above 50 ms is counted. A 120 ms task adds 70 ms. Good TBT on Lighthouse's mobile test is under 200 ms. It correlates with INP, which is why Lighthouse uses it, since lab tests don't have real user interactions.

#### 144: What is the critical rendering path?

It is the sequence of steps the browser has to finish before it can show the first pixels: download HTML, build the DOM, download and parse CSS to build the CSSOM, run blocking scripts, combine DOM and CSSOM into the render tree, run layout, and paint. Optimizing it means making the HTML arrive quickly and reducing how many render-blocking resources there are, how big they are and how many round trips they need.

#### 145: What is the difference between `async` and `defer` on script tags?

Both download the script without blocking HTML parsing.

- `async` runs the script as soon as it downloads, which may be before parsing finishes, in no guaranteed order. Good for independent scripts like analytics.
- `defer` runs scripts after the HTML is fully parsed, in document order, before `DOMContentLoaded`. Good for your app code.

```html
<script src="/analytics.js" async></script>
<script src="/vendor.js" defer></script>
<script src="/app.js" defer></script>
```

Module scripts (`type="module"`) are deferred by default.

#### 146: What does `font-display: swap` do?

It tells the browser to show text right away in a fallback font and swap in the web font when it loads. Without it, some browsers hide text for up to 3 seconds while waiting for the font. `swap` avoids invisible text but can cause a layout shift when the font changes. `optional` gives the font a very short time to load and otherwise uses the fallback for that page view, which avoids shifts.

```css
@font-face {
  font-family: "Inter";
  src: url("/fonts/inter.woff2") format("woff2");
  font-display: swap;
}
```

#### 147: What are WebP and AVIF?

They are modern image formats that are much smaller than JPEG and PNG at similar quality. WebP is usually around 25 to 35% smaller than JPEG. AVIF is often smaller than WebP, especially for photos, but encoding is slower. Both support transparency and animation. All current major browsers support both. You can serve them with a fallback using `<picture>`:

```html
<picture>
  <source srcset="/img/hero.avif" type="image/avif" />
  <source srcset="/img/hero.webp" type="image/webp" />
  <img src="/img/hero.jpg" alt="Hero" width="1200" height="600" />
</picture>
```

#### 148: What do `srcset` and `sizes` do?

`srcset` lists several versions of an image at different widths. `sizes` tells the browser how wide the image will be shown at different viewport sizes. The browser then picks the smallest file that looks sharp on the current screen, so a phone doesn't download a 2,000 px desktop image.

```html
<img
  src="/img/card-800.jpg"
  srcset="
    /img/card-400.jpg   400w,
    /img/card-800.jpg   800w,
    /img/card-1600.jpg 1600w
  "
  sizes="(max-width: 600px) 100vw, 33vw"
  alt="Product"
  width="800"
  height="600"
  loading="lazy"
/>
```

#### 149: What is tree shaking?

Tree shaking is when a bundler removes code you import but never use. It works with ES modules (`import`/`export`) because their structure can be analyzed at build time. Vite (with Rollup or Rolldown), webpack, esbuild and Parcel all support it. It works best when packages ship ES modules and mark themselves as side-effect free with `"sideEffects": false` in `package.json`.

```js
// Only debounce ends up in the bundle
import { debounce } from "lodash-es";
```

#### 150: What is Real User Monitoring (RUM)?

RUM collects performance data from real visitors' browsers as they use your site, then sends it to your analytics backend. It captures what lab tests miss: slow phones, bad networks, different countries, logged-in states and real interactions. The `web-vitals` library from Google is the usual starting point.

```js
import { onLCP, onINP, onCLS } from "web-vitals";

function send(metric) {
  navigator.sendBeacon(
    "/rum",
    JSON.stringify({ name: metric.name, value: metric.value, id: metric.id }),
  );
}
onLCP(send);
onINP(send);
onCLS(send);
```

---

## Moderate Questions (151-300)

### Moderate: Web Platform Fundamentals (151-165)

#### 151: What does `content-visibility: auto` do, and when should you use it?

It lets the browser skip style, layout and paint for an element's contents while that element is off-screen. When it gets close to the viewport, the browser renders it normally. On long pages with many sections, like a blog feed or a documentation page, this can cut initial rendering time a lot.

```css
.feed-item {
  content-visibility: auto;
  contain-intrinsic-size: auto 400px;
}
```

`contain-intrinsic-size` gives the skipped element a placeholder size so the scrollbar doesn't jump. The `auto` keyword makes the browser remember the real size once it has been rendered. Skipped content is still in the DOM and accessible to find-in-page and screen readers, but measuring it with `getBoundingClientRect()` forces it to render, which removes the benefit.

#### 152: What is CSS containment (`contain`) and how does it help performance?

`contain` tells the browser that an element's insides are independent from the rest of the page, so changes inside don't require work outside.

- `layout`: layout inside doesn't affect outside, and the element becomes a containing block.
- `paint`: children don't paint outside the element's box.
- `size`: the element's size doesn't depend on its children.
- `style`: counters and quotes don't leak out.
- `content` is a shortcut for `layout paint style`. `strict` adds `size`.

```css
.widget {
  contain: content;
}
```

It is useful for widgets that update often, like a live ticker or chat panel. When something inside changes, the browser can limit layout and paint to that subtree instead of the whole document.

#### 153: What is the `fetchpriority` attribute?

It is a hint that raises or lowers the priority of a resource compared to its default. It works on `<img>`, `<link>`, `<script>` and `<iframe>`, and as the `priority` option in `fetch()`.

```html
<!-- LCP image: fetch early at high priority -->
<img
  src="/hero.avif"
  fetchpriority="high"
  alt="..."
  width="1200"
  height="600"
/>

<!-- Carousel images that are not visible yet -->
<img src="/slide-2.avif" fetchpriority="low" alt="..." />

<script>
  fetch("/api/recommendations", { priority: "low" });
</script>
```

Chrome starts images at low priority and only raises them after layout shows they are in the viewport. `fetchpriority="high"` on the LCP image skips that wait, which often improves LCP by a few hundred milliseconds.

#### 154: What is `MutationObserver` and what are its performance pitfalls?

It calls your function when the DOM changes: children added or removed, attributes changed or text changed. Callbacks run as microtasks with a batch of records, so it is far cheaper than the old Mutation Events, which fired synchronously for every change and have now been removed from Chrome.

```js
const mo = new MutationObserver((records) => {
  for (const r of records) {
    r.addedNodes.forEach((n) => n.nodeType === 1 && enhance(n));
  }
});
mo.observe(document.querySelector("#app"), { childList: true, subtree: true });
```

Pitfalls: observing `subtree: true` on `document.body` with `attributes: true` can fire constantly on busy pages. Changing the DOM inside the callback can cause a loop. Doing heavy work in the callback blocks the main thread. Use `attributeFilter`, observe the smallest subtree you can, and call `disconnect()` when done.

#### 155: How do you insert many DOM elements efficiently?

Build the nodes outside the live document and insert them in one operation. That way style and layout run once instead of once per insert.

```js
const frag = document.createDocumentFragment();
for (const item of items) {
  const li = document.createElement("li");
  li.textContent = item.name;
  frag.append(li);
}
list.append(frag);

// Replacing all children at once
list.replaceChildren(...newNodes);
```

Avoid `innerHTML +=` in a loop; it re-parses and rebuilds the whole content every time and also loses event listeners. For very long lists, render only what is visible (virtualization).

#### 156: When should you use `requestAnimationFrame`?

Use it for visual updates that should happen once per frame, like animations or applying the result of a scroll or pointer event. The callback runs right before the browser does style and layout for the next frame, so your changes get included in that frame and you don't do more work than the screen can show.

```js
let pending = false;
let lastY = 0;

window.addEventListener(
  "scroll",
  () => {
    lastY = window.scrollY;
    if (!pending) {
      pending = true;
      requestAnimationFrame(() => {
        header.classList.toggle("compact", lastY > 100);
        pending = false;
      });
    }
  },
  { passive: true },
);
```

Don't put heavy calculations in rAF. They delay the frame. rAF also pauses in background tabs.

#### 157: How can you use the Streams API with `fetch` in the browser?

`response.body` is a `ReadableStream`, so you can process data as it arrives instead of waiting for the whole response. This is useful for large files, NDJSON feeds and streaming text from AI APIs.

```js
const res = await fetch("/api/export.ndjson");
const reader = res.body.pipeThrough(new TextDecoderStream()).getReader();

let buffer = "";
while (true) {
  const { value, done } = await reader.read();
  if (done) break;
  buffer += value;
  const lines = buffer.split("\n");
  buffer = lines.pop();
  for (const line of lines) if (line) addRow(JSON.parse(line));
}
```

The first rows show up quickly and memory stays flat because you never hold the full response.

#### 158: What caching strategies can a Service Worker use?

- **Cache first**: serve from cache, go to network only on a miss. For versioned static assets.
- **Network first**: try the network, fall back to cache if offline. For HTML and API data that should be fresh.
- **Stale-while-revalidate**: serve from cache right away and update the cache in the background. For things where a slightly old copy is fine, like avatars or config.
- **Network only** and **cache only** for special cases.

```js
self.addEventListener("fetch", (event) => {
  if (event.request.destination !== "image") return;
  event.respondWith(
    (async () => {
      const cache = await caches.open("images-v1");
      const cached = await cache.match(event.request);
      const network = fetch(event.request).then((res) => {
        if (res.ok) cache.put(event.request, res.clone());
        return res;
      });
      if (cached) {
        event.waitUntil(network.catch(() => {}));
        return cached;
      }
      return network;
    })(),
  );
});
```

Also enable navigation preload so the service worker startup time doesn't delay navigation requests. Workbox wraps these patterns if you don't want to write them by hand.

#### 159: Why can `localStorage` hurt performance, and when should you use IndexedDB instead?

`localStorage` is synchronous. Every `getItem` and `setItem` runs on the main thread, and the first access may have to load the whole origin's data from disk. It only stores strings, so you pay for `JSON.stringify` and `JSON.parse` every time, and it is limited to about 5 MB per origin. It is fine for small settings.

IndexedDB is asynchronous, stores structured data (objects, Blobs, ArrayBuffers) without manual serialization, supports indexes and transactions, and can hold far more data within the origin's quota. It also works inside Web Workers and Service Workers, which `localStorage` does not. Use it for offline data, large caches and anything you need to query.

#### 160: How do you cancel a `fetch` request, and why does it matter for performance?

Use an `AbortController`. Cancelling requests the user no longer needs, like old search queries or data for a page they left, saves bandwidth and avoids wasted parsing and rendering. It also prevents bugs where an old response overwrites a newer one.

```js
let controller;

async function search(q) {
  controller?.abort();
  controller = new AbortController();
  try {
    const res = await fetch(`/api/search?q=${encodeURIComponent(q)}`, {
      signal: AbortSignal.any([controller.signal, AbortSignal.timeout(5000)]),
    });
    render(await res.json());
  } catch (err) {
    if (err.name !== "AbortError" && err.name !== "TimeoutError") throw err;
  }
}
```

#### 161: What are passive event listeners?

A passive listener promises it won't call `preventDefault()`. For `touchstart`, `touchmove` and `wheel`, this lets the browser start scrolling right away on the compositor thread without waiting for your JavaScript to finish, which keeps scrolling smooth.

```js
window.addEventListener("touchmove", onTouchMove, { passive: true });
```

Chrome already treats these events as passive by default when the listener is on `window`, `document` or `document.body`. For listeners on other elements you need to set it yourself. If you really need to block scrolling, set `passive: false` and keep that handler very fast, or use the CSS `touch-action` property instead.

#### 162: Does CSS selector performance still matter?

Usually much less than people think. Modern engines match selectors right to left and use filters and caches that make most selectors fast. It starts to matter when you have a very large DOM, lots of rules, and frequent style changes, because every invalidation means re-matching. Things to watch:

- Broad `:has()` selectors on large subtrees, which can make invalidation expensive.
- Universal descendant selectors like `.app *` paired with frequent class changes on a high ancestor.
- Toggling a class on `<body>` or `<html>` that many rules depend on, which recalculates style for the whole page.

To check, look at "Recalculate Style" events in the Performance panel and turn on "Enable CSS selector stats" in the Performance panel settings to see which selectors cost the most time.

#### 163: What is `will-change`, and how can it be overused?

`will-change: transform` (or `opacity`) tells the browser an element is about to animate so it can promote it to its own compositor layer ahead of time. That avoids a repaint and a jank spike when the animation starts.

```css
.drawer {
  will-change: transform;
}
```

Each layer uses GPU memory, often width × height × 4 bytes or more. Putting `will-change` on hundreds of elements, or using `* { will-change: transform }`, can use a lot of memory and slow things down, especially on phones. Add it only to elements that will really animate, and ideally add and remove it with JavaScript around the animation.

#### 164: What are transferable objects, and why do they matter for Web Workers?

By default `postMessage` copies data using the structured clone algorithm. For a 50 MB `ArrayBuffer` that means copying 50 MB on the main thread. Transferable objects move ownership instead: the buffer is handed to the worker with no copy, and it becomes unusable (detached) on the sender side.

```js
const buffer = new ArrayBuffer(50 * 1024 * 1024);
worker.postMessage({ buffer }, [buffer]);
console.log(buffer.byteLength); // 0, it now belongs to the worker
```

`ArrayBuffer`, `MessagePort`, `ImageBitmap`, `OffscreenCanvas`, and streams (`ReadableStream` and others) can be transferred. `structuredClone(value, { transfer: [buf] })` uses the same mechanism.

#### 165: How do you make Canvas rendering faster?

- Move rendering to a worker with `OffscreenCanvas` so it doesn't compete with the main thread.
- Use several stacked canvases: a static background drawn once and a small dynamic layer redrawn each frame.
- Redraw only the area that changed instead of clearing the whole canvas.
- Batch drawing: build one path with many `lineTo` calls, then call `stroke()` once.
- Avoid changing state like `fillStyle` and `font` for every shape. Group shapes by style.
- Draw complex sprites once to an offscreen canvas and reuse them with `drawImage`.
- Scale for `devicePixelRatio` but don't go beyond what the screen needs.

```js
// main.js
const offscreen = document.querySelector("canvas").transferControlToOffscreen();
const worker = new Worker("render.js");
worker.postMessage({ canvas: offscreen }, [offscreen]);
```

For very large scenes, WebGL or WebGPU moves the drawing work to the GPU.

---

### Moderate: Google Chrome and Browser Internals (166-180)

#### 166: Why can scrolling stay smooth even when the main thread is busy?

Chrome handles scrolling on the compositor thread. The page content is already rasterized into tiles, so the compositor can move the layers and show new tiles without asking the main thread. This only works if nothing forces the scroll to wait for the main thread: non-passive `wheel` or `touch` listeners, some uses of `background-attachment: fixed`, or scroll-linked effects that run in JavaScript. Scroll-driven animations in CSS (`animation-timeline: scroll()`) can run on the compositor, so they stay smooth too.

#### 167: What makes style recalculation expensive?

The cost is roughly the number of elements whose style must be recalculated multiplied by the work per element (how many rules need matching). It gets expensive when:

- A change invalidates a large subtree, like toggling a class on `<body>` that many selectors depend on.
- The DOM is huge.
- There are complex selectors, especially broad `:has()`, `:nth-child()` on big lists, or deep descendant selectors.
- Many custom properties are defined at the root and change often, since inheriting elements need updating.

In the Performance panel, the "Recalculate Style" event shows "Elements Affected". Change classes on the smallest element you can, and prefer `transform` or `opacity` changes for animations.

#### 168: What is the back/forward cache, and what stops a page from using it?

The bfcache keeps a full snapshot of a page in memory (DOM, JS heap) when you navigate away, so pressing back or forward restores it instantly with no reload. Common reasons a page is not eligible:

- An `unload` event listener. Chrome is phasing out `unload`, so use `pagehide` or `visibilitychange` instead.
- `Cache-Control: no-store` on the main document (Chrome has started relaxing this in some cases, but don't count on it).
- Open connections like WebSockets or WebRTC at the time the user leaves.
- A `window.opener` reference from another window.

You can test it in DevTools under Application > Back/forward cache, and in the field read `notRestoredReasons` from the navigation entry.

```js
window.addEventListener("pageshow", (e) => {
  if (e.persisted) console.log("Restored from bfcache");
});
const [nav] = performance.getEntriesByType("navigation");
console.log(nav.notRestoredReasons);
```

#### 169: How do storage quotas work in Chrome?

All storage for an origin (IndexedDB, Cache Storage, OPFS and others) shares one quota. In Chrome an origin can use up to 60% of total disk space, and when the device runs low on space, Chrome can evict "best-effort" data from the least recently used origins. You can check usage and ask for persistent storage, which is not evicted automatically:

```js
const { usage, quota } = await navigator.storage.estimate();
console.log(`${(usage / 1e6).toFixed(1)} MB of ${(quota / 1e6).toFixed(0)} MB`);

const persisted = await navigator.storage.persist();
```

Writes that exceed the quota fail with a `QuotaExceededError`, so handle it and clean old caches.

#### 170: What is HTTP cache partitioning, and how did it change CDN caching benefits?

Since Chrome 86 the HTTP cache is partitioned by the top-level site (and frame site). A file cached while you were on `site-a.com` won't be reused when `site-b.com` loads the same URL. This stops sites from detecting your history through cache timing. The side effect is that loading popular libraries from a shared public CDN no longer gives a "probably already cached" benefit. Self-hosting those files on your own domain is often faster now, since it also avoids an extra connection.

#### 171: How does Chrome decide resource priorities?

Each request gets a priority: Highest, High, Medium, Low or Lowest. Roughly:

- The main document and CSS in the `<head>`: Highest.
- Fonts: High (after being discovered).
- Scripts in the `<head>` without `async`/`defer`: High. `async` and `defer` scripts: Low.
- Images: Low by default. Chrome gives the first few large images Medium, and raises images to High once layout shows they are in the viewport.
- `fetch()` and XHR: High.
- `prefetch`: Lowest.

You can see the priority in the Network panel by enabling the Priority column. `fetchpriority` and `preload` let you adjust it.

#### 172: What is the frame budget, and where does `requestAnimationFrame` fit in a frame?

At 60 Hz you get about 16.7 ms per frame. The browser needs some of that for its own work, so aim for around 10 ms of your own code per frame. On 120 Hz displays the budget halves. A typical frame looks like: input events, rAF callbacks, style, layout, paint, then commit to the compositor. rAF callbacks run just before style and layout, which is why they are the right place to make visual changes. A rendering opportunity only happens when the browser decides to produce a frame, so not every task is followed by a render.

#### 173: What are hidden classes and inline caches in V8?

V8 gives objects internal "shapes" (called maps or hidden classes) based on which properties they have and in what order. Objects with the same shape share it. When code accesses `obj.x`, V8 remembers the shape and where `x` lives (an inline cache), so next time it is a quick offset lookup.

If the same code sees objects with many different shapes (megamorphic), the cache stops helping and property access gets slower.

```js
// Good: same shape every time
function makePoint(x, y) {
  return { x, y };
}

// Bad: shapes differ depending on input order and optional fields
const p1 = { x: 1, y: 2 };
const p2 = { y: 2, x: 1 };
const p3 = { x: 1 };
p3.y = 2;
p3.z = 3;
```

Initialize all fields in the constructor, in the same order, and avoid `delete` on hot objects.

#### 174: What are V8's compilation tiers?

1. **Ignition**: the interpreter. Turns code into bytecode and runs it, collecting type feedback.
2. **Sparkplug**: a fast baseline compiler that turns bytecode into machine code without optimizing.
3. **Maglev**: a mid-tier optimizing compiler (added in Chrome 117) that uses type feedback and compiles quickly.
4. **TurboFan**: the top-tier optimizing compiler for very hot code. Slower to compile, fastest code.

Functions move up the tiers as they get hotter. If an optimized function sees a type it didn't expect, V8 deoptimizes it back to a lower tier. Stable types in hot code help V8 keep optimized code.

#### 175: How does V8's garbage collector work at a high level?

V8 uses a generational heap based on the idea that most objects die young.

- **Young generation**: new objects are allocated here. It is small and collected often by the Scavenger, which copies live objects and is fast. Objects that survive two scavenges move to the old generation.
- **Old generation**: collected by Mark-Compact. It marks live objects starting from roots, sweeps dead ones and sometimes compacts memory.

Most marking and sweeping run concurrently on helper threads, and V8 uses incremental steps and idle time to keep main-thread pauses short. Still, high allocation rates cause frequent scavenges, and a big old generation makes full GCs slower, which shows up as "Major GC" and "Minor GC" in the Performance panel.

#### 176: What happens to a tab when Chrome freezes or discards it?

To save resources, Chrome may **freeze** a background tab, stopping its timers and tasks, or **discard** it, removing it from memory completely. A discarded tab reloads when the user goes back to it. Memory Saver discards inactive tabs more aggressively. The Page Lifecycle API lets you react:

```js
document.addEventListener("freeze", () => saveDraftToIndexedDB());
document.addEventListener("resume", () => reconnectSocket());

if (document.wasDiscarded) restoreStateFromStorage();
```

Save important state when the page becomes hidden, because you can't count on getting another chance.

#### 177: What is `scheduler.postTask`, and how does it differ from `setTimeout`?

`scheduler.postTask()` schedules a task with a priority: `user-blocking`, `user-visible` (default) or `background`. The browser runs higher priority tasks first. It returns a promise, supports `AbortSignal` for cancellation, and you can change priority later with a `TaskController`. `setTimeout(fn, 0)` has no priority, can be clamped to 4 ms after nesting, and is harder to cancel in groups.

```js
const controller = new TaskController({ priority: "background" });
scheduler.postTask(() => prefetchNextPage(), { signal: controller.signal });

// Later, if it becomes urgent:
controller.setPriority("user-visible");
```

It is supported in Chromium browsers and recent Firefox. Always feature-detect `'scheduler' in window`.

#### 178: What is the preload scanner?

While the main HTML parser is blocked (for example, on a synchronous script), a second lightweight parser scans ahead in the HTML for resources like `<img>`, `<link rel="stylesheet">` and `<script src>` and starts downloading them early. Resources it can't see are found late: images set in CSS, content inserted by JavaScript, client-side rendered markup, and `<img>` tags using `data-src` for lazy loading. That's why a server-rendered `<img>` for the hero usually beats one rendered by React after hydration.

#### 179: What is V8 code caching?

Parsing and compiling JavaScript takes time on every page load. V8 can store compiled bytecode in the browser's cache alongside the script, so later loads skip most of the compile work. In Chrome the cache is created after a script runs a couple of times within a short period, and scripts stored by a Service Worker in Cache Storage can get their code cache right away. Keeping script URLs stable between deploys (and splitting rarely changed vendor code into its own file) helps the cache survive. Node.js uses the same idea through `v8.Script` cached data, its built-in compile cache (`module.enableCompileCache()` or `NODE_COMPILE_CACHE`), and single executable app snapshots.

#### 180: What are rasterization and tiles?

After paint creates a list of drawing commands, rasterization turns them into pixels. Chrome splits each layer into tiles (small rectangles), rasterizes the tiles that are visible or about to be visible first, and does most of this on the GPU. During fast scrolling you might briefly see blank or checkered areas when tiles aren't ready yet. Huge layers, very large or complex images, heavy filters and `box-shadow`s on big areas make rasterization slow. The Layers panel and the Rendering tab's layer borders help you see this.

---

### Moderate: Browser Developer and Performance Tools (181-195)

#### 181: How do you find a memory leak using heap snapshots in Chrome DevTools?

A common approach is the "three snapshot" technique:

1. Open the Memory panel, load the page, and take a heap snapshot (DevTools forces a garbage collection first).
2. Perform the action you suspect leaks, like opening and closing a modal, several times. Take a second snapshot.
3. Repeat the action again and take a third snapshot.
4. View snapshot 3 in "Objects allocated between Snapshot 1 and Snapshot 2" mode, or use the Comparison view. Objects that keep piling up and are still alive in the last snapshot are suspects.
5. Click a suspect object and read the **Retainers** panel to see the reference chain that keeps it alive, like a listener in a global array or a closure.

Search for "Detached" in the class filter to find DOM nodes removed from the page but still referenced by JavaScript.

#### 182: What is the difference between "Allocations on timeline" and "Allocation sampling" in the Memory panel?

- **Allocations on timeline** records every allocation with a timestamp while you interact. Blue bars show memory allocated at that time that is still alive; gray bars were freed. It is precise and helps you see which action allocates memory that stays, but it adds more overhead.
- **Allocation sampling** samples allocations with very low overhead and shows which functions allocated the most memory, as a tree or chart. It is good for long sessions or finding "who allocates so much garbage" that causes frequent GC.

Use the timeline for leaks tied to a specific action and sampling for overall allocation pressure.

#### 183: How do you find detached DOM elements in DevTools?

Detached elements are nodes removed from the document but still referenced from JavaScript, so they can't be garbage collected. In current Chrome, the Memory panel has a **Detached elements** profile type that lists them directly and groups them by their detached tree. You can also take a heap snapshot and filter by "Detached" to see `Detached HTMLDivElement` entries, then check the Retainers view. A typical cause is a component that keeps a reference to its root element in a module-level variable or an event listener that was never removed.

#### 184: How do you read the main thread flame chart in the Performance panel?

The x-axis is time and the y-axis is the call stack. The top bar is a task, and below it are the functions that ran inside it. Wide bars took a long time. Colors indicate work type: yellow for scripting, purple for rendering (style and layout), green for painting.

Below the chart, the tabs help:

- **Summary**: time split by category for the selection.
- **Bottom-up**: functions that took the most self time. The best place to start.
- **Call tree**: top-down view of where time went.
- **Event log**: chronological list of events.

Click a long task, check Bottom-up to find the function that used the most time, and click through to the source to see the actual line.

#### 185: How do you debug a slow interaction (poor INP) in DevTools?

1. Open the Performance panel. The live metrics view shows INP and logs each interaction you make with its duration.
2. Enable CPU throttling (for example 4x or a calibrated mobile preset) to match real devices.
3. Click Record, perform the slow interaction, and stop.
4. Find the interaction in the **Interactions** track. Its bar is split into input delay, processing duration and presentation delay.
5. Look at the main thread at that time. A long input delay means something else was running when the user clicked. Long processing means your event handler is slow. Long presentation delay means rendering (style, layout, paint) after the handler was expensive.
6. The Insights sidebar's "INP breakdown" summarizes this.

#### 186: What does each part of a request's Timing tab mean in the Network panel?

- **Queueing**: the browser waited before starting, due to lower priority, the 6 connections per host limit on HTTP/1.1, or disk cache allocation.
- **Stalled**: time waiting after queueing but before sending, for example waiting for a connection.
- **DNS Lookup**, **Initial connection**, **SSL**: connection setup.
- **Request sent**: usually tiny.
- **Waiting for server response (TTFB)**: server processing plus one round trip. Long values point to the backend.
- **Content Download**: time to receive the body. Long values point to large files or slow bandwidth.

Lots of queueing on HTTP/1.1 suggests too many requests to one host. Long TTFB suggests server work, and long download suggests size.

#### 187: How can you test a performance fix in production without deploying it?

Use DevTools **Local Overrides**. In the Sources panel, enable overrides and pick a local folder. Then you can edit any response (HTML, JS, CSS) or its headers and Chrome serves your edited version on reload. From the Network panel you can right-click a request and choose "Override content" or "Override headers". This lets you try things like adding `fetchpriority="high"` to an image, inlining critical CSS, or changing `Cache-Control`, and measure the impact on the real site. Request blocking (right-click > Block request URL) lets you see how much a third-party script costs by removing it.

#### 188: How do you run Lighthouse in CI to catch regressions?

Use Lighthouse CI (`@lhci/cli`). It runs Lighthouse several times per URL, checks results against assertions, and can upload reports to a server or temporary storage.

```js
// lighthouserc.js
module.exports = {
  ci: {
    collect: {
      startServerCommand: "npm run start",
      url: ["http://localhost:3000/", "http://localhost:3000/products"],
      numberOfRuns: 3,
    },
    assert: {
      assertions: {
        "categories:performance": ["error", { minScore: 0.9 }],
        "largest-contentful-paint": ["error", { maxNumericValue: 2500 }],
        "total-blocking-time": ["warn", { maxNumericValue: 200 }],
        "cumulative-layout-shift": ["error", { maxNumericValue: 0.1 }],
      },
    },
    upload: { target: "temporary-public-storage" },
  },
};
```

```bash
npx @lhci/cli autorun
```

Running several times and using the median reduces noise. CI machines vary, so keep the runner type consistent.

#### 189: What are Lighthouse's navigation, timespan and snapshot modes?

- **Navigation**: the classic mode. It loads a page and measures load performance.
- **Timespan**: records over a period while you interact with the page. Good for measuring interactions, INP-related issues and layout shifts after load.
- **Snapshot**: audits the page in its current state, for example after opening a menu, mostly for accessibility and best practices.

You can combine them into a user flow with Puppeteer, for example: navigate to the home page, timespan while adding to cart, snapshot of the cart drawer. The DevTools Recorder panel can export recorded flows to run with Lighthouse.

#### 190: What does WebPageTest show that Lighthouse doesn't?

- A detailed **waterfall** with connection reuse, priorities, and when each request started and finished, on real browsers at real locations.
- A **connection view** showing how requests share connections.
- A **filmstrip and video**, with Start Render and Visually Complete.
- **First view vs repeat view**, which shows how well caching works.
- Main thread activity aligned with the waterfall.
- Custom network profiles, scripting for multi-step flows, and test blocking of specific domains.
- Side-by-side comparison videos.

It is great for answering "what exactly happens during load, and in what order".

#### 191: How do you query the CrUX API?

Send a POST request with an origin or URL, an optional form factor and the metrics you want. You need a Google Cloud API key.

```js
const res = await fetch(
  `https://chromeuxreport.googleapis.com/v1/records:queryRecord?key=${API_KEY}`,
  {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({
      origin: "https://www.example.com",
      formFactor: "PHONE",
      metrics: [
        "largest_contentful_paint",
        "interaction_to_next_paint",
        "cumulative_layout_shift",
      ],
    }),
  },
);
const data = await res.json();
console.log(data.record.metrics.largest_contentful_paint.percentiles.p75);
```

The data is a rolling 28-day window, updated daily. The CrUX History API gives weekly data going back months, which is useful for spotting when a regression began.

#### 192: What is the Resource Timing API, and why do cross-origin entries have zeros?

It gives timing details for every resource the page loaded: DNS, connect, TLS, request, response, sizes and the protocol used.

```js
for (const r of performance.getEntriesByType("resource")) {
  console.log(
    r.name,
    r.initiatorType,
    r.duration.toFixed(0),
    r.transferSize,
    r.nextHopProtocol,
  );
}
```

For cross-origin resources, the detailed timings and sizes are zero unless the server sends a `Timing-Allow-Origin` header, which prevents leaking information about other sites:

```http
Timing-Allow-Origin: https://www.example.com
```

The buffer holds 250 entries by default. Use a `PerformanceObserver` or `performance.setResourceTimingBufferSize()` on resource-heavy pages.

#### 193: How do you detect long tasks in the field?

Use a `PerformanceObserver` with the `longtask` type. For more detail, the Long Animation Frames API (`long-animation-frame`, Chrome 123+) reports frames that took over 50 ms and includes which scripts ran, their source URLs and how long each took.

```js
new PerformanceObserver((list) => {
  for (const entry of list.getEntries()) {
    report({
      type: "loaf",
      duration: entry.duration,
      blocking: entry.blockingDuration,
      scripts: entry.scripts.map((s) => ({
        src: s.sourceURL,
        fn: s.sourceFunctionName,
        duration: s.duration,
      })),
    });
  }
}).observe({ type: "long-animation-frame", buffered: true });
```

The Long Tasks API only tells you a task was long and gives little attribution, so LoAF is more useful for finding which script is to blame.

#### 194: How do you CPU-profile a Node.js app?

Several options:

- `node --cpu-prof app.js` writes a `.cpuprofile` file when the process exits. Open it in the Chrome DevTools Performance panel or in speedscope.
- Connect DevTools with `--inspect`, open the Performance panel (or the dedicated Node DevTools window), and record while sending load.
- Use `0x` to generate a flame graph directly.
- On Linux, run `perf` with `node --perf-basic-prof` so JIT-compiled functions show up with names.

```bash
node --cpu-prof --cpu-prof-dir=./profiles server.js
# in another terminal
npx autocannon -c 50 -d 20 http://localhost:3000/api/report
# stop the server with Ctrl+C, then open ./profiles/*.cpuprofile
```

Always profile under load. An idle server's profile tells you nothing.

#### 195: How do you take a heap snapshot of a running Node.js process?

```bash
# Take a snapshot when the process receives a signal
node --heapsnapshot-signal=SIGUSR2 server.js
kill -USR2 <pid>

# Write snapshots automatically as the heap nears its limit
node --heapsnapshot-near-heap-limit=2 server.js
```

```js
// From code, for example behind an admin-only endpoint
import v8 from "node:v8";
const file = v8.writeHeapSnapshot();
console.log("Wrote", file);
```

Load the `.heapsnapshot` file into the Chrome DevTools Memory panel. Writing a snapshot pauses the process and needs roughly as much extra memory as the heap itself, so take the instance out of the load balancer first and make sure the container has headroom.

---

### Moderate: JavaScript Runtime and Server-Side Fundamentals (196-210)

#### 196: How do you measure event loop lag in Node.js?

Use `monitorEventLoopDelay` for a histogram of delays and `eventLoopUtilization` for how busy the loop is.

```js
import { monitorEventLoopDelay, performance } from "node:perf_hooks";

const h = monitorEventLoopDelay({ resolution: 20 });
h.enable();

let lastELU = performance.eventLoopUtilization();
setInterval(() => {
  const elu = performance.eventLoopUtilization(lastELU);
  lastELU = performance.eventLoopUtilization();
  console.log({
    p50ms: (h.percentile(50) / 1e6).toFixed(1),
    p99ms: (h.percentile(99) / 1e6).toFixed(1),
    maxMs: (h.max / 1e6).toFixed(1),
    utilization: elu.utilization.toFixed(2),
  });
  h.reset();
}, 10_000).unref();
```

A p99 delay above 50 to 100 ms or utilization close to 1 means the loop is overloaded or blocked. Export these as metrics and alert on them.

#### 197: When should you change `UV_THREADPOOL_SIZE`?

libuv's thread pool has 4 threads by default and is used for file system operations, `dns.lookup()`, `crypto.pbkdf2`, `crypto.scrypt`, `crypto.randomBytes` (async) and `zlib`. If your app does a lot of these at once, like hashing passwords or reading many files, requests queue for a free thread, even though the CPU might be idle. You can raise it (up to 1024) with an environment variable set before Node starts:

```bash
UV_THREADPOOL_SIZE=16 node server.js
```

Network I/O does not use the pool, so this doesn't help with slow HTTP calls. Raising it far beyond your CPU count doesn't help CPU-bound work like hashing either. A common sign you need it is `dns.lookup()` latency rising under load; using `dns.resolve*` or a DNS cache avoids the pool entirely for that case.

#### 198: How do you stream a large response in Node.js instead of buffering it?

Pipe a readable source into the response with `pipeline`, which handles backpressure and errors.

```js
import { createReadStream } from "node:fs";
import { pipeline } from "node:stream/promises";
import { createGzip } from "node:zlib";

app.get("/export", async (req, res) => {
  res.setHeader("Content-Type", "text/csv");
  res.setHeader("Content-Encoding", "gzip");
  try {
    await pipeline(createReadStream("/data/export.csv"), createGzip(), res);
  } catch (err) {
    req.log.warn({ err }, "export stream failed");
  }
});
```

Memory stays flat no matter how big the file is, and the client starts receiving data immediately. The same works with a database cursor stream feeding a transform that converts rows to CSV.

#### 199: How do you handle backpressure manually when writing to a stream?

Check the return value of `write()`. When it is `false`, stop and wait for `'drain'`.

```js
import { once } from "node:events";
import { createWriteStream } from "node:fs";

const out = createWriteStream("big.ndjson");

for await (const row of fetchRows()) {
  if (!out.write(JSON.stringify(row) + "\n")) {
    await once(out, "drain");
  }
}
out.end();
await once(out, "finish");
```

Without the check, `write()` just keeps buffering in memory, and if the source is faster than the disk or network, the process can run out of memory.

#### 200: Why use a worker pool instead of creating a worker thread per request?

Starting a worker thread means creating a new V8 isolate, loading modules and starting an event loop. That takes tens of milliseconds and several MB of memory. Doing it for every request adds latency and can exhaust memory under load. A pool keeps a fixed number of warm workers and queues tasks for them. Piscina is a widely used library for this.

```js
import Piscina from "piscina";

const pool = new Piscina({
  filename: new URL("./resize-worker.js", import.meta.url).href,
  maxThreads: 4,
});

app.post("/resize", async (req, res) => {
  const output = await pool.run({ image: req.body, width: 800 });
  res.type("image/webp").send(output);
});
```

Size the pool to available CPU cores and set a max queue length so overload turns into fast errors instead of huge queues.

#### 201: Should you use the `cluster` module or run several containers?

Both get you one Node process per core. The difference is who manages them.

- **cluster / PM2**: one container or VM runs several Node processes. Good on plain VMs. It needs no extra infrastructure but makes per-process metrics and memory limits trickier, and a container's memory limit is shared by all workers.
- **One process per container**: Kubernetes or ECS runs many small containers, each with one Node process. Scaling, health checks, restarts and resource limits are all handled per process by the platform. This is the usual choice in containerized environments.

Either way, keep the app stateless. Avoid running `cluster` inside containers that are already scaled horizontally, since it makes CPU and memory sizing confusing.

#### 202: What happens with an unhandled promise rejection in Node.js?

Since Node 15 the default mode is `throw`: an unhandled rejection is raised as an uncaught exception and the process exits with a non-zero code. That is better than silently ignoring errors, but it means one missing `catch` can crash your server.

```js
process.on("unhandledRejection", (reason) => {
  logger.fatal({ err: reason }, "unhandled rejection");
  process.exitCode = 1;
  shutdownGracefully();
});
```

Use this as a last line of defense for logging and clean shutdown, not as normal error handling. Fix the root cause by awaiting promises and handling errors where they occur. A common bug is starting a promise without awaiting it (`sendEmail(user)` without `await` or `.catch`).

#### 203: What is `AsyncLocalStorage`, and does it cost much?

It stores values that follow an async call chain, like a request ID, without passing them through every function. Loggers and tracing tools use it to attach request context.

```js
import { AsyncLocalStorage } from "node:async_hooks";
const als = new AsyncLocalStorage();

app.use((req, res, next) => {
  als.run(
    { requestId: req.headers["x-request-id"] ?? crypto.randomUUID() },
    next,
  );
});

function log(msg) {
  console.log(JSON.stringify({ requestId: als.getStore()?.requestId, msg }));
}
```

It used to be built on `async_hooks` and had noticeable overhead. Since Node 24 it uses `AsyncContextFrame` by default, which is much cheaper. For most services the cost is now small compared to I/O, but measure it in very hot paths.

#### 204: If a function is `async`, does it still block the event loop?

Yes, if it does CPU work. `async` only changes how the result is returned; the code between `await`s still runs synchronously on the main thread.

```js
// Still blocks for the whole loop
async function sumAll(arr) {
  let s = 0;
  for (const n of arr) s += heavy(n);
  return s;
}
```

Fixes: move it to a worker thread, or split it into chunks and yield to the event loop between chunks so other requests can run.

```js
import { setImmediate as yieldLoop } from "node:timers/promises";

async function sumAllChunked(arr) {
  let s = 0;
  for (let i = 0; i < arr.length; i++) {
    s += heavy(arr[i]);
    if (i % 1000 === 0) await yieldLoop();
  }
  return s;
}
```

Chunking increases total time a bit but keeps the server responsive.

#### 205: Why can `JSON.parse` and `JSON.stringify` be a bottleneck, and what can you do?

Both are synchronous and their cost grows with payload size. Parsing a 50 MB JSON body can block the event loop for hundreds of milliseconds and create many objects for the GC to deal with. Options:

- Limit request body size (`express.json({ limit: '1mb' })`).
- Paginate or stream large responses, for example as NDJSON, one object per line.
- Return only the fields clients need.
- Use a stream parser for big inputs.
- Use schema-based serializers, like Fastify's `fast-json-stringify`, which are faster than generic `JSON.stringify` for known shapes.
- Move huge parsing jobs to a worker thread.

#### 206: How does connection pooling work for outbound HTTP calls in Node.js?

Node's global `fetch` is built on undici, which keeps connections alive and pools them per origin. The `node:http` agent also keeps connections alive by default since Node 19. To tune the pool, create an undici `Agent`:

```js
import { Agent, setGlobalDispatcher } from "undici";

setGlobalDispatcher(
  new Agent({
    connections: 50, // max sockets per origin
    keepAliveTimeout: 10_000,
    keepAliveMaxTimeout: 60_000,
    connect: { timeout: 5_000 },
  }),
);
```

Without reuse, every call pays for TCP and TLS handshakes, and the server can run out of ephemeral ports from all the `TIME_WAIT` sockets. Keep the client's keep-alive timeout lower than the upstream server's idle timeout, or you get occasional `ECONNRESET` errors from reusing a socket the server just closed.

#### 207: How do you limit the number of concurrent async operations?

Running `Promise.all` over 10,000 items starts 10,000 requests at once, which can overload the database, hit rate limits or run out of sockets. Limit concurrency instead.

```js
async function mapLimit(items, limit, fn) {
  const results = new Array(items.length);
  let next = 0;
  async function worker() {
    while (next < items.length) {
      const i = next++;
      results[i] = await fn(items[i], i);
    }
  }
  await Promise.all(
    Array.from({ length: Math.min(limit, items.length) }, worker),
  );
  return results;
}

const users = await mapLimit(userIds, 10, (id) => fetchUser(id));
```

Libraries like `p-limit` do the same. Pick the limit based on what the downstream system can handle, like the size of your DB pool.

#### 208: Why must every outbound call have a timeout?

Without a timeout, a hung dependency keeps your request, its socket and its memory busy forever. Under load these pile up until the service runs out of connections or memory, so one slow dependency takes down everything (cascading failure). In modern Node use `AbortSignal.timeout()`:

```js
try {
  const res = await fetch("https://payments.internal/charge", {
    method: "POST",
    body: JSON.stringify(payload),
    headers: { "content-type": "application/json" },
    signal: AbortSignal.timeout(2000),
  });
} catch (err) {
  if (err.name === "TimeoutError") {
    // fail fast, maybe retry with backoff, or return a fallback
  }
  throw err;
}
```

Set timeouts based on the dependency's normal p99 latency plus some margin, and make sure the total time across retries fits inside your own SLO.

#### 209: How would you fairly compare the performance of Node.js, Deno and Bun for your service?

- Benchmark your real workload (routes, database calls, JSON sizes), not a "hello world".
- Use the same hardware, container limits and runtime flags, with production builds.
- Warm up first, since JIT compilation needs time, then run long enough to include garbage collection.
- Measure latency percentiles and errors at a fixed request rate, not just max requests per second.
- Check memory (RSS) and CPU per request, not only throughput.
- Check compatibility: native modules, APM agents, `node:` APIs your libraries use.

Often the database and network dominate, and runtime differences shrink to a few percent. Startup time, which matters for serverless and CLIs, is where Bun and Deno often show bigger gains.

#### 210: How do you size the V8 heap for a Node.js app in a container?

The V8 old space has a maximum size set by `--max-old-space-size` (in MB). If the heap needs more, V8 runs GC harder and eventually crashes with "JavaScript heap out of memory". If the container limit is lower than what V8 thinks it can use, the kernel OOM kills the process first, with no useful error.

A common rule is to set the heap to about 70 to 80% of the container memory limit, leaving room for Buffers, native code, thread stacks and the young generation.

```dockerfile
ENV NODE_OPTIONS="--max-old-space-size=1536"
# with a 2 GiB container memory limit
```

Check what V8 actually uses with `v8.getHeapStatistics().heap_size_limit`. For apps that allocate a lot of short-lived objects, raising the young generation with `--max-semi-space-size` (for example 32 or 64 MB) can reduce the number of scavenges and improve throughput. Measure before and after.

---

### Moderate: Networking and Web Protocols (211-225)

#### 211: With HTTP/2 multiplexing, do you still need to bundle JavaScript?

Yes, but less aggressively than before. HTTP/2 removes the per-request connection cost, so many small files are fine at the network level. But each module still has overhead: request headers, a separate cache entry, and less effective compression, since compression works better on bigger files. Deep import chains also add round trips, because the browser only discovers module B after downloading module A. The usual approach is to bundle into a moderate number of chunks (by route and shared vendor code) and use `modulepreload` for critical chunks to avoid waterfalls.

```html
<link rel="modulepreload" href="/assets/router-7c1e.js" />
```

#### 212: What is connection coalescing in HTTP/2 and HTTP/3?

If two hostnames resolve to the same IP address and the TLS certificate covers both, the browser can send requests for both over one existing connection instead of opening a new one. For example, `static.example.com` and `www.example.com` on the same CDN with a wildcard certificate can share a connection. This saves DNS, TCP and TLS time. It is one reason splitting assets across many subdomains (domain sharding) is now harmful: if coalescing doesn't apply, each hostname costs a full connection setup.

#### 213: HTTP/2 Server Push was removed from Chrome. What replaced it?

Chrome removed Server Push in version 106 because it rarely helped, often pushed things the browser already had cached, and was hard to get right. The replacements are:

- **`<link rel="preload">`** in the HTML or as a `Link` header.
- **103 Early Hints**: the server sends an early informational response with `Link` headers while it is still generating the page, so the browser can preconnect or preload during server "think time".

```http
HTTP/1.1 103 Early Hints
Link: </css/main.css>; rel=preload; as=style
Link: <https://cdn.example.com>; rel=preconnect

HTTP/1.1 200 OK
Content-Type: text/html
...
```

Early Hints help most when TTFB is long. Many CDNs, such as Cloudflare, can generate them automatically from cached `Link` headers.

#### 214: How can you reduce TLS overhead?

- Use **TLS 1.3**, which needs one round trip instead of two.
- Enable **session resumption** (session tickets / PSK) so returning clients skip the full handshake.
- Use **ECDSA certificates**. They are smaller and faster to verify than RSA, and you can serve both for older clients.
- Keep the **certificate chain short** and don't send the root certificate. A big chain can overflow the first round trip.
- **Reuse connections** with keep-alive, HTTP/2 or HTTP/3, so the handshake happens once.
- **Terminate TLS at the edge** (a CDN) close to users, so handshake round trips are short.

#### 215: What is HSTS, and how does it help performance?

HTTP Strict Transport Security (`Strict-Transport-Security` header) tells the browser to always use HTTPS for your domain. Without it, a user typing `example.com` goes to `http://` first and gets redirected to `https://`, which costs a full extra round trip or more. With HSTS, the browser upgrades the URL internally. If your domain is on the HSTS preload list built into browsers, even the very first visit skips the redirect.

```http
Strict-Transport-Security: max-age=63072000; includeSubDomains; preload
```

Be careful with `includeSubDomains` and preloading: every subdomain must support HTTPS, and removing yourself from the preload list takes a long time.

#### 216: What is 0-RTT in TLS 1.3 and QUIC, and what is the risk?

With 0-RTT, a returning client sends application data, like the first HTTP request, together with the handshake, using keys from a previous session. This removes a full round trip. The risk is replay: an attacker who captures that first flight can send it again, and the server may process it twice. Servers and CDNs usually only accept 0-RTT for safe, idempotent requests like `GET` without side effects, and they can mark them (for example with the `Early-Data: 1` header) so the app can reject anything risky with `425 Too Early`.

#### 217: What is TCP slow start, and what is the "14 KB rule"?

A new TCP connection doesn't know how much bandwidth is available, so it starts by sending only a small amount of data (the initial congestion window, usually 10 packets, about 14 KB) and roughly doubles it each round trip if no loss is seen. So the first round trip of a response can only deliver around 14 KB. If your HTML and inline critical CSS fit in that, the browser can start rendering after one round trip. Larger responses need more round trips, which hurts on high-latency mobile networks. QUIC has similar behavior. It is a guideline, not a hard rule, since TLS records and headers also take space.

#### 218: How can DNS add hidden latency, and how do you reduce it?

- **CNAME chains**: `www.example.com` → `example.cdn.net` → `edge123.cdn.net` can mean several lookups. Keep chains short, or use CNAME flattening / ALIAS records at the apex.
- **Low TTLs** (like 30 to 60 seconds) cause frequent cache misses at resolvers.
- **Many third-party domains** each need their own lookup.
- **Slow authoritative DNS providers**: use a fast anycast DNS provider.

Fixes: fewer origins, `dns-prefetch` and `preconnect` for the critical ones, reasonable TTLs (minutes to hours for stable records), and HTTPS DNS records (type 65), which let browsers learn that a server supports HTTP/3 in the same lookup instead of waiting for an `Alt-Svc` header.

#### 219: What is a CDN cache key, and how does the `Vary` header affect it?

The cache key is what the CDN uses to decide whether two requests can share a cached response. By default it is usually the host and path, sometimes plus the query string. Adding things to the key (cookies, headers, unneeded query parameters like `utm_source`) creates many versions of the same content and drops the hit ratio.

`Vary` tells caches that the response depends on certain request headers. `Vary: Accept-Encoding` is normal. `Vary: User-Agent` or `Vary: Cookie` can almost destroy caching, because nearly every user has a different value. Better options are to normalize what you vary on, for example into "mobile" and "desktop", or to use the CDN's cache key settings to include only the values that really change the response.

#### 220: What do `stale-while-revalidate` and `stale-if-error` do?

They are `Cache-Control` extensions:

- `stale-while-revalidate=60`: after `max-age` expires, a cache can serve the stale response for up to 60 more seconds while it fetches a fresh one in the background. The user doesn't wait for revalidation.
- `stale-if-error=86400`: if the origin returns an error or can't be reached, the cache can serve the stale copy for up to a day.

```http
Cache-Control: public, max-age=60, stale-while-revalidate=300, stale-if-error=86400
```

Chrome supports `stale-while-revalidate` in its HTTP cache, and major CDNs support both, although some CDNs need it enabled or have their own settings. They are a cheap way to make cached APIs and HTML pages both fast and resilient.

#### 221: What problems come up when scaling WebSockets?

- **Long-lived connections** stay pinned to one server, so load balancing is uneven and deploys must drain connections.
- **Fan-out**: a message for a user connected to server A must reach them even if it was produced on server B. You need a pub/sub layer like Redis, NATS or Kafka.
- **Idle timeouts** on load balancers and proxies (for example AWS ALB's 60-second default) close quiet connections. Send heartbeats (ping/pong) more often than the shortest idle timeout.
- **Reconnect storms**: after a deploy or outage, every client reconnects at once. Use exponential backoff with random jitter.
- **Memory per connection**: each socket has buffers. Watch for slow clients and limit per-connection buffer size.
- **File descriptor limits**: each connection uses one, so raise `ulimit -n`.

#### 222: How do Server-Sent Events handle reconnection, and how do they behave on HTTP/1.1 vs HTTP/2?

If the connection drops, `EventSource` reconnects automatically after a delay (the server can set it with `retry:`). If the server includes an `id:` with each event, the browser sends `Last-Event-ID` on reconnect so the server can resume from where it stopped.

```js
// Node.js SSE endpoint
app.get("/events", (req, res) => {
  res.writeHead(200, {
    "Content-Type": "text/event-stream",
    "Cache-Control": "no-cache",
    Connection: "keep-alive",
  });
  const lastId = Number(req.headers["last-event-id"] ?? 0);
  const send = (evt) =>
    res.write(`id: ${evt.id}\ndata: ${JSON.stringify(evt.data)}\n\n`);
  replayEventsAfter(lastId).forEach(send);
  const unsubscribe = bus.subscribe(send);
  req.on("close", unsubscribe);
});
```

On HTTP/1.1, each SSE connection takes one of the browser's 6 connections per origin, so several tabs can block other requests. On HTTP/2 and HTTP/3, SSE streams share one connection, so this problem goes away. Make sure proxies don't buffer the stream (in Nginx, `proxy_buffering off` or send the `X-Accel-Buffering: no` header).

#### 223: How do you pick a compression level for dynamic responses, and when should you avoid compression?

Higher levels give smaller output but cost more CPU and add latency, with diminishing returns. For responses compressed on every request, Brotli level 4 to 6 or Gzip level 5 to 6 is a good balance. Save Brotli 11 for static assets compressed once at build time. Zstandard is also a good choice for dynamic content in clients that support it, since it compresses quickly at good ratios.

Avoid or think twice when:

- The content is already compressed (images, video, ZIP, WOFF2).
- The response is tiny (under about 1 KB), where headers dominate.
- A response contains a secret (like a CSRF token) and also reflects user input, over HTTPS. That combination enables BREACH-style attacks. Separate the secret from the reflected input or mask the token on each response.

#### 224: How do you use the Speculation Rules API?

It lets you tell Chrome (and other Chromium browsers) which pages to prefetch or fully prerender, so the next navigation can be close to instant.

```html
<script type="speculationrules">
  {
    "prerender": [
      { "where": { "href_matches": "/products/*" }, "eagerness": "moderate" }
    ],
    "prefetch": [
      {
        "where": {
          "and": [
            { "href_matches": "/*" },
            { "not": { "href_matches": "/logout" } }
          ]
        },
        "eagerness": "conservative"
      }
    ]
  }
</script>
```

`eagerness` controls when it triggers: `immediate`, `eager`, `moderate` (on hover for about 200 ms on desktop) or `conservative` (on pointer down). Prerendered pages run their JavaScript, so delay analytics until activation by checking `document.prerendering` and the `prerenderingchange` event. Exclude URLs with side effects like logout or "add to cart". You can also send rules in a `Speculation-Rules` HTTP header.

#### 225: How do you add conditional request support to a Node.js API?

Express already generates weak ETags for `res.send()` and `res.json()` and returns 304 when the client's `If-None-Match` matches. You can do it yourself for more control, such as using a version number from the database instead of hashing the body:

```js
app.get("/api/products/:id", async (req, res) => {
  const product = await getProduct(req.params.id);
  const etag = `"p${product.id}-v${product.version}"`;

  res.setHeader("ETag", etag);
  res.setHeader("Cache-Control", "private, no-cache");

  if (req.headers["if-none-match"] === etag) {
    return res.status(304).end();
  }
  res.json(product);
});
```

Using a version or `updated_at` value means you can answer 304 without building and hashing the full response, which saves server CPU as well as bandwidth. The full `If-None-Match` header can list several ETags, so a production version should handle that.

---

### Moderate: Databases and Data Access (226-240)

#### 226: How do you choose column order in a composite index?

A B-tree composite index on `(a, b, c)` is sorted by `a`, then `b`, then `c`. It can be used for filters on `a`, on `a` and `b`, or on all three, but traditionally not for a filter on `b` alone. General rules:

- Put columns used with equality (`=`) first.
- Then columns used for sorting (`ORDER BY`).
- Then range filters (`>`, `<`, `BETWEEN`), since after a range the rest of the index can't be used for ordering.

```sql
-- Query
SELECT id, total FROM orders
WHERE customer_id = $1 AND status = 'paid'
ORDER BY created_at DESC
LIMIT 20;

-- Matching index
CREATE INDEX idx_orders_cust_status_created
  ON orders (customer_id, status, created_at DESC);
```

PostgreSQL 18 added B-tree skip scan, which can use a composite index even when the leading column isn't filtered, if it has few distinct values. It's still best to design the index around your most important queries.

#### 227: How do you read a PostgreSQL `EXPLAIN ANALYZE` output?

```text
Limit  (cost=0.43..8.95 rows=20 width=16) (actual time=0.031..0.112 rows=20 loops=1)
  Buffers: shared hit=24
  ->  Index Scan using idx_orders_cust_status_created on orders
        (cost=0.43..1205.10 rows=2830 width=16) (actual time=0.030..0.105 rows=20 loops=1)
        Index Cond: ((customer_id = 42) AND (status = 'paid'))
Planning Time: 0.210 ms
Execution Time: 0.140 ms
```

- Read from the most indented node outward. Inner nodes feed outer ones.
- `cost` is the planner's estimate in arbitrary units. `actual time` is real milliseconds: startup..total per loop.
- Compare estimated `rows` with actual `rows`. Big differences (10x or more) mean bad statistics and often a bad plan. Run `ANALYZE` or increase statistics on the column.
- `loops` multiplies the time. A node with 0.1 ms and 50,000 loops costs 5 seconds.
- `Buffers: shared hit` is pages read from memory, `read` is pages from disk.
- Watch for `Seq Scan` on big tables with selective filters, `Sort` nodes that spill to disk ("external merge"), and `Nested Loop` with many outer rows.

In PostgreSQL 18, `EXPLAIN ANALYZE` includes buffer statistics by default.

#### 228: Why might PostgreSQL ignore an index you created?

- **A function or cast on the column**: `WHERE lower(email) = 'a@b.com'` can't use an index on `email`. Create an expression index on `lower(email)`.
- **Type mismatch**: comparing a `text` column with a number, or `timestamp` with `timestamptz`, can stop index use.
- **Leading wildcard**: `LIKE '%term'` can't use a B-tree. Use a `pg_trgm` GIN index or full-text search.
- **Low selectivity**: if the filter matches a large part of the table, a sequential scan really is cheaper.
- **Stale statistics**: the planner thinks the table is tiny. Run `ANALYZE`.
- **Wrong column order** in a composite index.
- **`OR` conditions** across different columns, which may need separate indexes combined with a bitmap scan or a rewrite with `UNION`.
- **Small tables**, where a sequential scan is faster anyway.

```sql
CREATE INDEX idx_users_email_lower ON users (lower(email));
```

#### 229: What are partial and covering indexes?

A **partial index** only includes rows that match a condition. It is smaller and faster to update and scan when queries always use that condition.

```sql
CREATE INDEX idx_orders_pending ON orders (created_at) WHERE status = 'pending';
```

A **covering index** contains every column a query needs, so PostgreSQL can do an index-only scan without reading the table. Use `INCLUDE` to add columns that aren't searched on.

```sql
CREATE INDEX idx_orders_customer_cover
  ON orders (customer_id) INCLUDE (total, created_at);

SELECT total, created_at FROM orders WHERE customer_id = 42;
```

Index-only scans also depend on the visibility map, so a table that VACUUM rarely processes may still need table lookups ("Heap Fetches" in the plan).

#### 230: How do you find the slowest queries in PostgreSQL?

Enable the `pg_stat_statements` extension. It groups queries by shape and tracks calls, total time, mean time, rows and buffer usage.

```sql
CREATE EXTENSION IF NOT EXISTS pg_stat_statements;

SELECT query, calls,
       round(total_exec_time::numeric, 0) AS total_ms,
       round(mean_exec_time::numeric, 2)  AS mean_ms,
       rows
FROM pg_stat_statements
ORDER BY total_exec_time DESC
LIMIT 10;
```

Sort by `total_exec_time` to find queries that use the most database time overall, often a fast query called millions of times. Sort by `mean_exec_time` for individually slow queries. You can also set `log_min_duration_statement = 500` to log queries slower than 500 ms, and use `auto_explain` to log their plans.

#### 231: What is PgBouncer, and what is transaction pooling?

PgBouncer is a lightweight connection pooler for PostgreSQL. Each PostgreSQL connection is a separate backend process using several MB of memory, so thousands of direct connections from many app instances hurt the database. PgBouncer accepts many client connections and shares a smaller number of real server connections between them.

- **Session pooling**: a client keeps a server connection for its whole session. Safe but saves little.
- **Transaction pooling**: a server connection is assigned only for the duration of a transaction, then returned. Much more efficient.

In transaction mode, features that depend on session state don't work as expected: session-level `SET`, advisory locks held across transactions, `LISTEN/NOTIFY`, and temporary tables. Protocol-level prepared statements are supported since PgBouncer 1.21 when `max_prepared_statements` is set.

#### 232: How do you size a database connection pool?

More connections is not faster. The database has limited CPU cores and disk, and too many concurrent queries cause contention and context switching. A common starting point for the database's total active connections is:

```text
connections ≈ (CPU cores × 2) + number of effective disks
```

So a 16-core database might do best with 30 to 40 active connections in total. Then divide that across all app instances: 10 pods with a pool of 4 each, not 10 pods with 50 each. Also:

- Set a connection acquire timeout so requests fail fast instead of waiting forever.
- Watch pool wait time and the number of waiting requests as metrics.
- Remember autoscaling: 50 pods × pool size can exceed `max_connections`.
- Use PgBouncer or RDS Proxy when instance counts are high or variable.

#### 233: What is the ESR rule for MongoDB indexes?

ESR stands for Equality, Sort, Range. In a compound index, put fields matched by equality first, then fields you sort on, then fields filtered by range. This lets MongoDB use the index for both filtering and sorting and avoid an in-memory sort.

```js
// Query
db.orders
  .find({ customerId: 42, total: { $gte: 100 } })
  .sort({ createdAt: -1 });

// ESR index
db.orders.createIndex({ customerId: 1, createdAt: -1, total: 1 });
```

In `explain()` output, a `SORT` stage means the sort happened in memory. Large in-memory sorts can be slow and can fail if they exceed the memory limit and `allowDiskUse` is off.

#### 234: How do you make a MongoDB aggregation pipeline faster?

- Put `$match` as early as possible so fewer documents flow through the pipeline, and make sure it can use an index.
- `$sort` early (right after `$match`) can use an index. A `$sort` + `$limit` pair keeps only the top N in memory.
- `$project` or `$unset` early to drop fields you don't need, which reduces memory per document.
- Be careful with `$lookup`. It runs per document, so index the foreign field, and filter before it.
- Avoid `$unwind` on large arrays unless needed, since it multiplies document counts.
- Use `explain('executionStats')` on the aggregation to see each stage's cost.

```js
db.orders.aggregate([
  { $match: { status: "paid", createdAt: { $gte: ISODate("2026-01-01") } } },
  { $project: { customerId: 1, total: 1 } },
  { $group: { _id: "$customerId", revenue: { $sum: "$total" } } },
  { $sort: { revenue: -1 } },
  { $limit: 10 },
]);
```

#### 235: When should you embed documents in MongoDB, and when should you reference them?

**Embed** when the data is read together, belongs to one parent, and has a bounded size, for example an order with its line items or a user with a few addresses. One read gets everything and updates are atomic within the document.

**Reference** when the related data is large or unbounded (comments on a popular post), shared by many parents (products referenced by many orders), or updated on its own very often.

Watch out for the 16 MB document limit and for arrays that grow without bound. Large documents are slower to read and update and use more cache. Patterns like the subset pattern (embed the latest 10 reviews, reference the rest) and the bucket pattern (group time-series data into documents per hour) help balance this.

#### 236: What are Redis eviction policies, and which should you choose for a cache?

When Redis reaches `maxmemory`, the `maxmemory-policy` decides what happens:

- `noeviction` (the default): writes fail with an error. Good when Redis holds data you can't lose, bad for a cache.
- `allkeys-lru`: evict the least recently used keys. A good default for a cache.
- `allkeys-lfu`: evict the least frequently used keys. Better when some keys are steadily popular.
- `volatile-lru` / `volatile-lfu` / `volatile-ttl`: only evict keys that have a TTL.
- `allkeys-random` / `volatile-random`.

```bash
CONFIG SET maxmemory 2gb
CONFIG SET maxmemory-policy allkeys-lfu
```

For a pure cache use `allkeys-lru` or `allkeys-lfu`. If the same instance also stores important data without TTLs, use a `volatile-*` policy, or better, use separate instances. Watch `evicted_keys` in `INFO stats`.

#### 237: What is a cache stampede, and how do you prevent it?

A stampede (thundering herd) happens when a popular cache key expires and many requests miss at the same time, all hitting the database to rebuild the same value. This can overload the database.

Ways to prevent it:

- **Request coalescing**: only one request rebuilds the value; others wait for it. In one process, share the in-flight promise. Across instances, use a short Redis lock.
- **Early refresh**: refresh the value in the background before it expires.
- **TTL jitter**: add random time to TTLs so keys don't expire together.
- **Serve stale**: keep serving the old value while one worker refreshes.

```js
const inFlight = new Map();

async function getCached(key, ttl, load) {
  const hit = await redis.get(key);
  if (hit) return JSON.parse(hit);
  if (inFlight.has(key)) return inFlight.get(key);

  const p = (async () => {
    try {
      const value = await load();
      const jitter = Math.floor(Math.random() * ttl * 0.1);
      await redis.set(key, JSON.stringify(value), { EX: ttl + jitter });
      return value;
    } finally {
      inFlight.delete(key);
    }
  })();
  inFlight.set(key, p);
  return p;
}
```

#### 238: What is a hot key in Redis, and how do you deal with one?

A hot key is a single key that receives a huge share of traffic, like a home page config or a celebrity's profile. Redis runs commands on one main thread, and in a cluster a key lives on one shard, so one hot key can saturate a single node while others sit idle.

To find them: `redis-cli --hotkeys` (needs an LFU eviction policy), `MONITOR` briefly (it is expensive), or client-side metrics.

To fix them:

- Cache the value in the application's memory for a few seconds (a small local LRU in front of Redis).
- Use Redis client-side caching (tracking), where the server tells the client when the key changes.
- Replicate the key: write `config:1` through `config:N` and read a random one.
- Use read replicas for read-heavy keys.

Also watch for **big keys** (huge hashes or lists). Commands on them block Redis; use `redis-cli --bigkeys` and `UNLINK` instead of `DEL` to free them in the background.

#### 239: How does DataLoader solve N+1 in GraphQL or similar APIs?

DataLoader collects all the `.load(id)` calls made during one tick of the event loop and turns them into a single batch call. It also caches results per request, so the same ID is fetched once.

```js
import DataLoader from "dataloader";

function createLoaders() {
  return {
    user: new DataLoader(async (ids) => {
      const { rows } = await db.query(
        "SELECT * FROM users WHERE id = ANY($1)",
        [ids],
      );
      const byId = new Map(rows.map((u) => [u.id, u]));
      return ids.map((id) => byId.get(id) ?? null); // must keep the same order as ids
    }),
  };
}

// In a resolver: called 100 times, but one SQL query is sent
const author = await ctx.loaders.user.load(post.userId);
```

Create new loaders per request so cached data doesn't leak between users.

#### 240: How do you process a very large query result in Node.js without loading it all into memory?

Use a server-side cursor and stream the rows. With PostgreSQL and `pg`, use `pg-query-stream` or `pg-cursor`:

```js
import QueryStream from "pg-query-stream";
import { pipeline } from "node:stream/promises";
import { Transform } from "node:stream";

app.get("/export/orders.csv", async (req, res) => {
  const client = await pool.connect();
  try {
    const rows = client.query(
      new QueryStream("SELECT id, total, created_at FROM orders", [], {
        batchSize: 1000,
      }),
    );
    const toCsv = new Transform({
      objectMode: true,
      transform(row, _enc, cb) {
        cb(null, `${row.id},${row.total},${row.created_at.toISOString()}\n`);
      },
    });
    res.setHeader("Content-Type", "text/csv");
    await pipeline(rows, toCsv, res);
  } finally {
    client.release();
  }
});
```

For MongoDB, `find()` already returns a cursor that you can iterate with `for await`. For batch jobs that update rows, process them in chunks using keyset pagination (`WHERE id > $last ORDER BY id LIMIT 1000`), so you never hold a long transaction open.

---

### Moderate: Operating Systems and Server Resources (241-255)

#### 241: What are context switches, and how do you check them?

A context switch is when the CPU stops running one thread and starts another, saving and restoring registers and often losing CPU cache warmth. **Voluntary** switches happen when a thread waits on I/O or a lock. **Involuntary** switches happen when the scheduler preempts a thread because its time slice ran out or a higher-priority thread needs the CPU.

```bash
pidstat -w -p <pid> 1
# cswch/s   = voluntary switches per second
# nvcswch/s = involuntary switches per second
vmstat 1    # "cs" column: system-wide switches per second
```

Lots of involuntary switches mean CPU contention: too many busy threads for the cores, or a container hitting its CPU quota. Lots of voluntary switches can point to lock contention or many tiny I/O operations.

#### 242: How do you read `vmstat` output?

```bash
vmstat 1
procs -----------memory---------- ---swap-- -----io---- -system-- ------cpu-----
 r  b   swpd   free   buff  cache   si   so    bi    bo   in   cs us sy id wa st
 6  0      0 812344  91200 2304112    0    0     4    80 2100 5400 72 10 18  0  0
```

- `r`: threads running or waiting for CPU. Consistently more than the core count means CPU saturation.
- `b`: threads blocked on I/O.
- `si` / `so`: swap in and out. Any steady non-zero value is bad for a server.
- `bi` / `bo`: blocks read from and written to disk.
- `cs`: context switches per second.
- `us`, `sy`: user and kernel CPU time. High `sy` suggests lots of syscalls or network overhead.
- `wa`: CPU waiting on I/O.
- `st`: steal time, CPU taken by the hypervisor for other VMs. High steal on cloud VMs means a noisy neighbor or a burstable instance that ran out of credits.

#### 243: How do you read `iostat -x` output?

```bash
iostat -x 1
Device   r/s   w/s   rkB/s   wkB/s  r_await  w_await  aqu-sz  %util
nvme0n1  120   900   4800    36000     0.30     2.10    1.90   78.0
```

- `r/s`, `w/s`: read and write operations per second (IOPS).
- `rkB/s`, `wkB/s`: throughput.
- `r_await`, `w_await`: average time in ms each request took, including queueing. This is what your app feels.
- `aqu-sz`: average queue length.
- `%util`: share of time the device was busy. On SSDs and NVMe drives, which handle many requests in parallel, 100% doesn't necessarily mean saturated. Look at `await` and queue size instead.

On cloud volumes like AWS EBS, compare IOPS and throughput with the volume's provisioned limits. Hitting them causes latency to jump suddenly.

#### 244: How can `strace` help debug a slow or stuck process?

`strace` shows the system calls a process makes. It answers "what is the process waiting on?"

```bash
# Summary of syscalls by time and count, for 10 seconds
timeout 10 strace -c -f -p <pid>

# Live trace of network and file calls with timing
strace -f -tt -T -e trace=network,openat,read,write -p <pid>
```

For example, it can show a process opening the same config file on every request, thousands of tiny `write` calls, a `connect` to an IP that times out, or a thread stuck in `futex` (waiting on a lock). `strace` slows the traced process down a lot, so use it briefly in production. For lower overhead, eBPF tools like `bpftrace` or `perf trace` are better.

#### 245: How do you use `perf` to profile a Node.js process?

`perf` samples what the CPU is doing across user space and the kernel. JavaScript functions are JIT compiled, so `perf` needs a map file to show their names. Start Node with `--perf-basic-prof`:

```bash
node --perf-basic-prof server.js &
perf record -F 99 -g -p $(pgrep -f server.js) -- sleep 30
perf script > out.perf
# turn into a flame graph with Brendan Gregg's FlameGraph scripts
./stackcollapse-perf.pl out.perf | ./flamegraph.pl > flame.svg
```

The benefit over V8's own profiler is that you see time spent in the kernel, in libuv, in native addons and in GC together with JavaScript. `perf top -p <pid>` gives a live view. The map files in `/tmp` grow over time, so don't leave the flag on forever in production without cleanup.

#### 246: What is `TIME_WAIT`, and how can it exhaust ephemeral ports?

When a TCP connection closes, the side that closes first keeps the socket in `TIME_WAIT` for a while (60 seconds on Linux) to handle late packets. A service that opens and closes many short outbound connections, for example calling an API without keep-alive, can pile up tens of thousands of `TIME_WAIT` sockets. Each one holds a local port for the same destination IP and port, and the default ephemeral range (`32768`–`60999`) is about 28,000 ports. When it runs out, new connections fail with `EADDRNOTAVAIL` or time out.

```bash
ss -tan state time-wait | wc -l
cat /proc/sys/net/ipv4/ip_local_port_range
```

The real fix is connection reuse (keep-alive and pooling). Widening the port range and enabling `net.ipv4.tcp_tw_reuse` for outgoing connections also help.

#### 247: What is the listen backlog, and why does `somaxconn` matter?

When clients connect, the kernel completes the TCP handshake and puts the connection in the accept queue until the application calls `accept()`. The queue size is the smaller of the backlog the app asks for (Node's default is 511) and `net.core.somaxconn` (4096 on newer kernels, 128 on older ones). If the app is slow to accept, for example because the event loop is blocked, the queue fills up and new connections are dropped or reset, and clients see timeouts.

```bash
ss -ltn    # for listening sockets: Recv-Q = current queue, Send-Q = max backlog
nstat -az TcpExtListenOverflows TcpExtListenDrops
```

Raising the backlog helps with short bursts, but if the queue is always full, the real problem is that the app can't keep up.

#### 248: What is the difference between virtual memory (VSZ) and RSS?

VSZ (virtual size) is all the address space a process has reserved, including memory that was never touched, memory-mapped files and shared libraries. RSS is the part actually held in physical RAM right now. Node.js and other JIT runtimes often reserve large virtual ranges (V8 reserves address space up front for the heap), so VSZ can be many GB while RSS is a few hundred MB. VSZ is mostly irrelevant for capacity. Watch RSS, and in containers, the cgroup's memory usage, which also counts page cache used by the container.

#### 249: Why does a Linux server show very little "free" memory even when it is not under pressure?

Linux uses unused RAM as page cache for files read from or written to disk. That makes `free` look small, but this memory can be reclaimed instantly when programs need it. Look at the `available` column instead:

```bash
free -h
              total   used   free  shared  buff/cache  available
Mem:           15Gi   4.1Gi  420Mi   12Mi       11Gi       10Gi
```

Here only 420 MB is "free", but 10 GB is available. Real memory pressure shows up as low `available`, swap activity, high values in `/proc/pressure/memory` (PSI), or OOM kills in `dmesg`.

#### 250: How does the Linux OOM killer choose a process?

When the system (or a cgroup) runs out of memory and can't reclaim enough, the kernel picks a process to kill based on its `oom_score`, which is mostly how much memory it uses, adjusted by `oom_score_adj` (from -1000 to 1000). The process using the most memory usually dies. In containers, the OOM happens at the cgroup level when the container exceeds its memory limit, and only processes in that cgroup are candidates.

```bash
dmesg -T | grep -i -E 'killed process|out of memory'
cat /proc/<pid>/oom_score
```

To protect a critical process, lower its `oom_score_adj`. For Node apps, set `--max-old-space-size` lower than the limit so V8 hits its own limit first and you at least get a clear "heap out of memory" error and stack trace.

#### 251: How do you detect CPU throttling in a container?

With CFS quotas, a container that uses its quota early in a 100 ms period is paused until the next period, even if the host has idle CPU. This causes latency spikes, especially for multi-threaded runtimes, since all threads count against the same quota. Node uses extra threads for GC, JIT and libuv.

```bash
# cgroup v2, inside the container
cat /sys/fs/cgroup/cpu.stat
# nr_periods 120000
# nr_throttled 18000      <- periods where throttling happened
# throttled_usec 950000000
```

If `nr_throttled / nr_periods` is more than a few percent, you are being throttled. In Kubernetes, look at the `container_cpu_cfs_throttled_periods_total` metric from cAdvisor. Fixes: raise or remove the CPU limit, reduce threads, or spread load across more pods.

#### 252: What is the "PID 1 problem" in Docker?

The first process in a container runs as PID 1, which Linux treats specially. PID 1 doesn't get default signal handlers, so if your app doesn't install a `SIGTERM` handler, `docker stop` signals are ignored and the container gets SIGKILLed after the timeout. PID 1 is also responsible for reaping zombie child processes.

Problems also come from running `npm start` as PID 1, since npm may not forward signals to Node reliably, and from shell-form `CMD`, where `sh` is PID 1.

```dockerfile
# Use exec form, run node directly
CMD ["node", "server.js"]
```

```bash
# Or add a tiny init process
docker run --init my-api
```

In Kubernetes, set `shareProcessNamespace` or include `tini` in the image if you spawn child processes.

#### 253: What does `fsync` do, and why does it matter for performance?

When a program writes to a file, the data usually goes into the OS page cache first and is written to disk later. That is fast but data can be lost on power failure. `fsync` forces the data to be written to the physical device before returning. It is slow, from hundreds of microseconds to many milliseconds depending on the disk. Databases call it on commit to guarantee durability, which is why commit latency depends on disk latency. Grouping writes (PostgreSQL's group commit, batching inserts in one transaction) reduces the number of `fsync` calls. Turning durability off (`synchronous_commit = off` in PostgreSQL) trades a small window of possible data loss for speed.

#### 254: The load average is high but CPU usage is low. What could be going on?

On Linux, load average counts both runnable threads and threads in uninterruptible sleep (state `D`), which are usually waiting on disk or network storage. So a high load with low CPU often means I/O problems: a slow or saturated disk, an NFS or EBS volume with high latency, or heavy swapping.

```bash
vmstat 1                       # look at "b" (blocked) and "wa"
iostat -x 1                    # look at await and queue size
ps -eo state,pid,cmd | grep '^D'
cat /proc/pressure/io
```

It can also be many threads briefly waiting on locks in the kernel. Pressure stall information (PSI) in `/proc/pressure/` shows directly how much time tasks were stalled on CPU, memory or I/O.

#### 255: How do you choose the number of worker threads or processes in a container?

Base it on the CPU your container can actually use, not on the host's core count. `os.cpus().length` returns all host CPUs, which can be 64 even if your container is limited to 2. `os.availableParallelism()` (Node 18.14+) respects CPU affinity, and depending on your Node and libuv version it may or may not account for a cgroup CPU quota, so check its value in your environment.

```js
import os from "node:os";
const workers =
  Number(process.env.WORKERS) || Math.max(1, os.availableParallelism() - 1);
```

Passing the number explicitly through an environment variable that matches the container's CPU limit is the most reliable option. Too many workers for the quota causes throttling and context switching. Too few leaves CPU unused.

---

### Moderate: Cloud Infrastructure and Delivery (256-270)

#### 256: Why does a Node.js app behind an AWS ALB sometimes return random 502 errors, and how do you fix it?

The ALB keeps idle connections to targets open and reuses them. Its idle timeout is 60 seconds by default. Node's `server.keepAliveTimeout` defaults to 5 seconds. So Node closes an idle connection after 5 seconds, and if the ALB sends a new request on that connection at the same moment, the request fails and the ALB returns 502.

The fix is to make Node's keep-alive timeout longer than the load balancer's idle timeout:

```js
const server = app.listen(3000);
server.keepAliveTimeout = 65_000; // more than ALB's 60 s
server.headersTimeout = 66_000; // must be greater than keepAliveTimeout
```

The same rule applies to any proxy in front of Node, like Nginx with upstream keep-alive: the upstream (Node) should keep idle connections open longer than the proxy does.

#### 257: Which metric should drive autoscaling for a web API?

- **CPU utilization** is simple and works for CPU-bound services. For Node, average CPU can look fine while the event loop is saturated on a single thread, so make sure the CPU metric is per process or per container.
- **Request count per target** (ALB `RequestCountPerTarget`) works well when requests have similar costs, and it reacts faster than CPU.
- **Custom metrics** like event loop lag, queue depth, or concurrency (in-flight requests) are closest to real saturation.
- **Latency** is a poor scaling signal on its own, since it can rise because of a slow database, and adding app servers then makes things worse.

Scale out quickly and scale in slowly. Set a minimum capacity that can handle normal peaks while new instances warm up.

#### 258: What is CloudFront Origin Shield (or tiered caching), and when does it help?

Without it, every edge location that misses goes straight to your origin. With dozens of edges, a popular new file can cause dozens of origin requests. Origin Shield adds a central caching layer in front of your origin. Edge misses go to the shield first, and only the shield's misses reach the origin. Cloudflare's Tiered Cache works the same way.

It helps when content is cached across many regions, when the origin is expensive or fragile (for example on-demand image processing), and when you want a higher overall hit ratio. It adds a small extra hop on misses and has extra costs, so it's less useful when your traffic is concentrated in one region.

#### 259: What is the difference between a CloudFront cache policy and an origin request policy?

- The **cache policy** decides the cache key (which headers, cookies and query strings make responses different) and TTLs (min, default, max).
- The **origin request policy** decides which headers, cookies and query strings are forwarded to the origin, without adding them to the cache key.

This split lets you forward something the origin needs for logging or processing, like a `CloudFront-Viewer-Country` header, without reducing your hit ratio. A common mistake is putting all cookies or all headers in the cache key, which makes almost every request unique. Include only the values that actually change the response.

#### 260: How do you upload and download large files to and from S3 efficiently?

- **Multipart upload**: split files over about 100 MB into parts (5 MB to 5 GB each) and upload them in parallel. Failed parts are retried alone. The AWS SDK's `Upload` helper in `@aws-sdk/lib-storage` does this for you.
- **Byte-range fetches**: download parts of an object in parallel with `Range` headers, or read only the part you need.
- **Presigned URLs** so clients upload and download directly to S3 instead of through your servers.
- **S3 Transfer Acceleration** or CloudFront for users far from the bucket's region.
- Add a lifecycle rule to abort incomplete multipart uploads, or orphaned parts keep costing money.

```js
import { Upload } from "@aws-sdk/lib-storage";

const upload = new Upload({
  client: s3,
  params: {
    Bucket: "videos",
    Key: "talk.mp4",
    Body: fs.createReadStream("talk.mp4"),
  },
  queueSize: 4,
  partSize: 16 * 1024 * 1024,
});
upload.on("httpUploadProgress", (p) => console.log(p.loaded, "/", p.total));
await upload.done();
```

#### 261: What does `proxy_buffering` do in Nginx?

With `proxy_buffering on` (the default), Nginx reads the response from your app as fast as the app can send it, stores it in memory buffers (and temp files if large), and then sends it to the client at the client's speed. Your Node process is freed quickly even if the client is on a slow mobile connection. That's one of the main benefits of putting Nginx in front of an app.

Turn it off for streaming responses where the client needs data immediately, like Server-Sent Events or streamed AI output, either with `proxy_buffering off;` in that location or by sending `X-Accel-Buffering: no` from the app. Tune `proxy_buffers` and `proxy_buffer_size` if responses are often larger than the default buffers and Nginx writes them to temp files.

#### 262: How do you enable keep-alive connections from Nginx to upstream servers?

By default Nginx opens a new connection to the upstream for every request and uses HTTP/1.0. That adds latency and creates many `TIME_WAIT` sockets. To reuse connections:

```nginx
upstream api {
    server 10.0.1.10:3000;
    server 10.0.1.11:3000;
    keepalive 64;            # idle connections kept per worker
    keepalive_timeout 60s;
}

server {
    location /api/ {
        proxy_pass http://api;
        proxy_http_version 1.1;
        proxy_set_header Connection "";
    }
}
```

`proxy_http_version 1.1` and clearing the `Connection` header are both required. Make sure the Node server's `keepAliveTimeout` is longer than Nginx's `keepalive_timeout` for that upstream.

#### 263: What do 502, 503 and 504 errors from Nginx usually mean?

- **502 Bad Gateway**: Nginx couldn't get a valid response from the upstream. The app crashed, isn't listening, closed the connection (often a keep-alive timeout mismatch), or sent an invalid response.
- **503 Service Unavailable**: no upstream was available, or a rate or connection limit was hit (`limit_req`, `limit_conn`), or the app returned 503 itself.
- **504 Gateway Timeout**: the upstream didn't respond within `proxy_read_timeout` (60 seconds by default), or connecting took longer than `proxy_connect_timeout`.

```nginx
location /api/reports/ {
    proxy_pass http://api;
    proxy_connect_timeout 5s;
    proxy_read_timeout 120s;   # only for slow report endpoints
}
```

Check the Nginx error log first. It says exactly which upstream failed and why ("upstream timed out", "connection refused", "upstream prematurely closed connection").

#### 264: Which load balancing algorithm is best for an API?

- **Round robin**: simple, works when requests cost about the same and servers are identical.
- **Least connections / least outstanding requests**: sends new requests to the server with the fewest active ones. Better when request costs vary a lot, since a server stuck on slow requests gets less new work. AWS ALB supports "least outstanding requests".
- **Consistent hashing**: routes the same key (user ID, URL) to the same server. Useful for local caches, but can create hot spots.
- **Weighted** versions for servers with different capacities.
- **Power of two random choices**: pick two servers at random and use the less loaded one. Envoy and others use this, and it works well with many load balancers that each have only a partial view.

For Node services with mixed request costs, least outstanding requests usually gives better tail latency than round robin.

#### 265: What is the difference between readiness, liveness and startup probes in Kubernetes?

- **Readiness probe**: "can this pod receive traffic now?" If it fails, the pod is removed from Service endpoints but not restarted. Use it during startup, warm-up and graceful shutdown.
- **Liveness probe**: "is this process stuck?" If it fails, Kubernetes restarts the container. Keep it simple and avoid checking dependencies, otherwise a database outage restarts every pod at once and makes things worse.
- **Startup probe**: gives slow-starting apps time to boot. Liveness and readiness checks don't start until it passes.

```yaml
readinessProbe:
  httpGet: { path: /readyz, port: 3000 }
  periodSeconds: 5
  failureThreshold: 2
livenessProbe:
  httpGet: { path: /livez, port: 3000 }
  periodSeconds: 10
  failureThreshold: 3
  timeoutSeconds: 2
```

A Node app with a blocked event loop fails liveness checks, which leads to restarts that look random. Check event loop lag when you see unexplained restarts.

#### 266: How does the Kubernetes Horizontal Pod Autoscaler work?

The HPA checks metrics periodically (every 15 seconds by default) and changes the replica count to keep a metric near its target. For CPU, the target is a percentage of the pod's CPU **request**, not its limit.

```yaml
apiVersion: autoscaling/v2
kind: HorizontalPodAutoscaler
metadata: { name: api }
spec:
  scaleTargetRef: { apiVersion: apps/v1, kind: Deployment, name: api }
  minReplicas: 3
  maxReplicas: 30
  metrics:
    - type: Resource
      resource:
        name: cpu
        target: { type: Utilization, averageUtilization: 60 }
  behavior:
    scaleDown:
      stabilizationWindowSeconds: 300
```

You can also scale on custom or external metrics, like requests per second or queue length, through a metrics adapter or KEDA. Pods need accurate requests and fast startup for the HPA to work well, and new nodes may be needed too (Cluster Autoscaler or Karpenter), which adds minutes.

#### 267: How do you make Docker images for Node.js smaller and builds faster?

- **Multi-stage builds**: build in one stage, copy only the output and production dependencies to a slim final image.
- **Order layers** so dependencies install before you copy the source. Then code changes don't reinstall packages.
- **BuildKit cache mounts** for the npm cache.
- Use a slim base image (`node:24-slim` or a distroless Node image), and a `.dockerignore` that excludes `node_modules`, `.git` and tests.

```dockerfile
# syntax=docker/dockerfile:1
FROM node:24-slim AS build
WORKDIR /app
COPY package.json package-lock.json ./
RUN --mount=type=cache,target=/root/.npm npm ci
COPY . .
RUN npm run build && npm prune --omit=dev

FROM node:24-slim
WORKDIR /app
ENV NODE_ENV=production
COPY --from=build /app/node_modules ./node_modules
COPY --from=build /app/dist ./dist
USER node
CMD ["node", "dist/server.js"]
```

Smaller images pull faster, which shortens scale-out time and deploys.

#### 268: How do you catch performance regressions in CI before they reach production?

- **Bundle size checks** (size-limit, bundlesize, or the build tool's report) that fail a pull request when a chunk grows past a budget.
- **Lighthouse CI** with assertions on LCP, TBT and CLS for key pages, run several times to reduce noise.
- **Backend benchmarks**: a short k6 or autocannon run against a staging build, comparing p95 latency to the main branch.
- **Query checks**: run the test suite with query counting to catch new N+1 patterns, or snapshot `EXPLAIN` plans for critical queries.
- **Compare against a baseline**, not a fixed number, so changes in CI hardware don't cause false alarms.

Post the results as a pull request comment so reviewers see the impact. Hard failures work best for big, reliable signals like bundle size, and warnings work best for noisy metrics.

#### 269: How does Terraform help make load tests trustworthy?

Load test results only mean something if the environment matches production. With Terraform (or OpenTofu) you define the staging environment from the same modules as production: same instance types, same database class and parameters, same load balancer settings, same autoscaling limits, only with different variables like counts. You can spin it up for a test and destroy it afterwards to save money. Since everything is in code, you can see exactly what changed between two test runs ("we moved from `m6i.large` to `m7g.large`") and you avoid "works on staging" surprises caused by manual changes.

#### 270: How do you pick the right instance type for a Node.js service on AWS?

- Node runs JavaScript on one main thread per process, so single-core speed matters. Newer generations (for example Graviton-based `m8g`/`c8g`, or recent Intel/AMD) are usually faster and cheaper per request than old ones.
- **Compute optimized (c family)** for CPU-heavy services, **general purpose (m family)** for balanced ones, **memory optimized (r family)** for big in-memory caches.
- **Graviton (ARM)** instances often give better price-performance for Node. Check that native modules and Docker images support `arm64`.
- **Burstable (t family)** instances run out of CPU credits under steady load and then slow down. Watch `CPUCreditBalance`.
- Don't guess. Load test two or three candidates and compare cost per 1,000 requests at your target p95 latency.

---

### Moderate: Observability, Profiling and Reliability (271-285)

#### 271: Why should latency be recorded as a histogram instead of an average or a gauge?

A histogram counts requests in buckets (for example under 50 ms, under 100 ms, under 250 ms). From those counts you can calculate percentiles over any time range and combine data from many instances. You can't average percentiles across instances, so per-instance p99 gauges can't be merged correctly. In Prometheus:

```js
import client from "prom-client";

const httpDuration = new client.Histogram({
  name: "http_request_duration_seconds",
  help: "HTTP request duration",
  labelNames: ["method", "route", "status"],
  buckets: [0.025, 0.05, 0.1, 0.25, 0.5, 1, 2.5, 5],
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
```

```promql
histogram_quantile(0.99, sum by (le, route) (rate(http_request_duration_seconds_bucket[5m])))
```

Choose buckets around your SLO threshold. Use the route pattern as a label, never the raw URL, to avoid an explosion of time series.

#### 272: What are the RED and USE methods?

- **RED** is for services: **R**ate (requests per second), **E**rrors (failed requests per second), **D**uration (latency distribution). It tells you how users experience the service.
- **USE** is for resources: **U**tilization (how busy), **S**aturation (how much work is waiting), **E**rrors. Apply it to CPU, memory, disks, network interfaces, connection pools and thread pools.

Use RED dashboards to spot that something is wrong, then USE on the resources behind the service to find which one is the bottleneck.

#### 273: How does trace context propagation work?

When service A calls service B, it adds a `traceparent` header (W3C Trace Context standard) containing the trace ID, the current span ID and flags. Service B reads it and creates its spans as children of A's span, so the whole request ends up in one trace.

```http
traceparent: 00-4bf92f3577b34da6a3ce929d0e0e4736-00f067aa0ba902b7-01
             ver  trace-id (16 bytes)             parent-span-id   flags (01 = sampled)
tracestate: vendor1=opaque-value
```

OpenTelemetry instrumentation injects and extracts this header automatically for HTTP and gRPC. For queues like Kafka or SQS, put the context in message headers or attributes. Traces often break at places with no instrumentation, like a custom HTTP client, a proxy that strips headers, or a job queue.

#### 274: What is the difference between head sampling and tail sampling?

- **Head sampling** decides at the start of a request whether to record its trace, for example keeping 5% at random. It is cheap and simple, but it throws away most of the rare slow or failed requests you care about.
- **Tail sampling** waits until the trace is complete and then decides, for example "keep all traces with errors, all traces slower than 1 second, and 2% of the rest". It keeps the interesting traces, but all spans have to be buffered somewhere, usually in the OpenTelemetry Collector's `tail_sampling` processor, which needs memory and requires that all spans of a trace reach the same collector instance.

Many teams combine them: light head sampling in the SDK to control volume, and tail sampling in the collector.

#### 275: How much overhead can logging add, and how do you reduce it?

Logging costs CPU (formatting, JSON serialization), memory, and I/O. In Node, writes to `process.stdout` can be synchronous depending on what it is connected to (files and, on Linux, pipes), so heavy `console.log` in a hot path can block the event loop. At high volume, the log pipeline and storage also cost real money.

Ways to reduce it:

- Use a fast structured logger like Pino, ideally with transports running in a worker thread.
- Set the level to `info` or `warn` in production. Avoid building expensive log messages unless the level is enabled.
- Don't log full request or response bodies.
- Sample high-volume logs, for example 1% of successful request logs and 100% of errors.
- Never log secrets or personal data. Redaction (Pino's `redact` option) also costs a little CPU.

```js
const log = pino({
  level: process.env.LOG_LEVEL ?? "info",
  redact: ["req.headers.authorization"],
});
if (log.isLevelEnabled("debug"))
  log.debug({ payload: summarize(big) }, "details");
```

#### 276: How do you connect logs with traces?

Add the current trace ID and span ID to every log line. Then from a slow trace you can jump to its logs, and from an error log you can open the full trace. OpenTelemetry has instrumentations for Pino and Winston that do this automatically (`@opentelemetry/instrumentation-pino`), or you can do it manually:

```js
import { trace } from "@opentelemetry/api";

function withTrace(obj = {}) {
  const span = trace.getActiveSpan();
  const ctx = span?.spanContext();
  return ctx ? { ...obj, trace_id: ctx.traceId, span_id: ctx.spanId } : obj;
}

log.info(withTrace({ orderId }), "order created");
```

Also return a request ID or trace ID to the client in a response header so support teams can look up a specific user's failed request.

#### 277: An APM tool shows an endpoint's p95 went from 200 ms to 900 ms. How do you find the cause?

1. Check if the change matches a deploy, a config change, or a traffic change (more requests, different mix).
2. Open slow traces for that endpoint and compare them to normal ones. See which span grew: a database query, an external API, or time spent in the app itself (gaps between spans often mean CPU work or event loop blocking).
3. If a query span grew, look at the query text, rows returned and the database metrics (CPU, locks, connections). Check if a plan changed or a table grew.
4. If an external call grew, check that dependency's own latency and whether calls are made sequentially instead of in parallel.
5. If time is in the app, look at event loop lag, GC metrics and a CPU profile under load.
6. Check if only some instances or some customers are slow, using the trace attributes.

#### 278: How can you CPU profile a Node.js service in production safely?

- Profile a **single instance**, ideally one taken out of the load balancer or with only a share of traffic.
- Use **sampling profilers**, which add little overhead: V8's CPU profiler, `perf` with `--perf-basic-prof`, or a continuous profiler like Pyroscope, Datadog or Grafana's profiling, which sample all the time at low cost.
- Trigger a short profile (30 to 60 seconds) on demand, for example through the inspector protocol behind an admin-only endpoint:

```js
import { Session } from "node:inspector/promises";
import fs from "node:fs/promises";

export async function profileFor(ms) {
  const session = new Session();
  session.connect();
  await session.post("Profiler.enable");
  await session.post("Profiler.start");
  await new Promise((r) => setTimeout(r, ms));
  const { profile } = await session.post("Profiler.stop");
  await fs.writeFile(
    `/tmp/cpu-${Date.now()}.cpuprofile`,
    JSON.stringify(profile),
  );
  session.disconnect();
}
```

Never expose `--inspect` publicly. Don't run allocation tracking or heap snapshots on a busy instance without spare memory.

#### 279: What is the difference between a heap snapshot and a heap profile?

- A **heap snapshot** is a full picture of every live object at one moment, with references between them. It is best for finding what is retaining memory (leaks). It is big, pauses the process while taken, and needs extra memory.
- A **heap (allocation) profile** samples allocations over time and shows which functions allocated the most memory. It has low overhead and is best for finding code that creates a lot of garbage and causes frequent GC.

In Node you can collect a sampling heap profile with `--heap-prof` (writes a `.heapprofile` file on exit) or through the inspector's `HeapProfiler.startSampling`. Both file types open in Chrome DevTools.

#### 280: What is the difference between closed and open workload models in load testing?

- **Closed model**: a fixed number of virtual users, each sending a request, waiting for the response, then sending the next. If the server slows down, users send fewer requests, so the load drops on its own. This hides how bad things get, a problem known as coordinated omission.
- **Open model**: requests arrive at a fixed rate no matter how fast the server responds, like real traffic from many independent users. If the server slows down, requests queue up, which is what really happens in production.

In k6, use the arrival-rate executors for an open model:

```js
export const options = {
  scenarios: {
    api: {
      executor: "ramping-arrival-rate",
      startRate: 50,
      timeUnit: "1s",
      preAllocatedVUs: 200,
      maxVUs: 1000,
      stages: [
        { target: 200, duration: "5m" },
        { target: 200, duration: "10m" },
        { target: 400, duration: "5m" },
      ],
    },
  },
};
```

#### 281: How do you model a realistic workload for a load test?

- **Use production traffic mix**: what percentage of requests hit each endpoint, from access logs or APM.
- **Realistic data**: many different users, products and search terms, not the same ID every time. Otherwise caches hide the real cost.
- **Think time and sessions**: users browse, pause and then act. Include login, browsing and checkout in the same proportions as real users.
- **Payload sizes** like production: large carts, long lists.
- **Ramp up gradually** and include a warm-up period, so you don't measure JIT warm-up or cold caches unless you want to.
- **Production-like environment and data volume**: a 1,000-row test database won't show index problems that a 100-million-row table has.
- **Include third parties** or realistic mocks with real latency.

#### 282: What should you watch during a soak test?

Look for things that slowly drift instead of failing right away:

- **Memory**: RSS and heap after GC should level off. A steady upward slope is a leak.
- **Latency over time**: p95 and p99 should stay flat. Slow growth points to growing data structures, fragmentation or table bloat.
- **GC time** per minute.
- **File descriptors and connections**: open sockets, DB pool usage, `TIME_WAIT` count.
- **Disk**: logs and temp files filling up.
- **Database**: table and index bloat, autovacuum activity, replication lag.
- **Error rate**: small error rates that grow over time.
- **Cache behavior**: hit ratio, evictions, Redis memory.

Compare the first hour with the last hour. Any metric that is clearly different is worth investigating.

#### 283: How do you choose good SLIs for a web application?

Pick measurements that reflect what users actually experience, measured as close to the user as you can:

- **Availability**: share of valid requests that didn't fail (no 5xx, no timeouts), measured at the load balancer or edge, not inside the app (where crashed instances report nothing).
- **Latency**: share of requests faster than a threshold, like "99% of `/api/search` requests under 400 ms". Set separate thresholds for different kinds of endpoints.
- **Frontend experience**: share of page views with "good" LCP, INP and CLS from RUM data.
- **Correctness or freshness** for data pipelines: share of records processed within 5 minutes.

Express SLIs as good events divided by valid events. That makes error budgets and burn rates simple to calculate.

#### 284: What is a burn rate alert, and why use multiple windows?

Burn rate is how fast you are using your error budget compared to the rate that would use it exactly by the end of the SLO period. A burn rate of 1 uses the budget in exactly 30 days. A burn rate of 14.4 uses 2% of a 30-day budget in one hour.

Multi-window alerts check a long and a short window together, for example: "page if burn rate is above 14.4 over the last 1 hour **and** over the last 5 minutes". The long window makes sure the problem is significant, and the short window makes sure it is still happening, so the alert clears quickly after a fix. A second, slower alert (like burn rate above 6 over 6 hours and 30 minutes) catches slower problems and can open a ticket instead of paging someone.

#### 285: What is Little's Law, and how do you use it in capacity planning?

Little's Law says: **L = λ × W**. The average number of requests in the system (L) equals the arrival rate (λ) times the average time each request spends in the system (W).

Examples:

- An API receives 500 requests per second and each takes 200 ms on average. On average, 500 × 0.2 = 100 requests are in flight. If each instance handles 25 concurrent requests well, you need at least 4 instances plus headroom.
- Each request holds a DB connection for 20 ms and you have 1,000 requests per second: 1,000 × 0.02 = 20 connections busy on average. A pool of 10 would force requests to wait.

It also shows why latency increases are dangerous: if a dependency slows from 200 ms to 2 seconds at the same traffic, in-flight requests grow tenfold, which can exhaust connections and memory.

---

### Moderate: Web Performance Standards and Metrics (286-300)

#### 286: What are the four parts of LCP, and what should each look like?

LCP can be split into:

1. **Time to First Byte**: until the HTML starts arriving.
2. **Resource load delay**: from TTFB until the browser starts loading the LCP resource (image). Long when the image is discovered late.
3. **Resource load duration**: how long the image download takes.
4. **Element render delay**: from when the image finished loading until it is painted. Long when render-blocking CSS or JS, or client-side rendering, holds back the paint.

For a well-optimized page, most of the time should be in TTFB and resource load duration (roughly 40% each), and the two delays should be small (under 10% each). If LCP is text, there is no resource to load, so only TTFB and render delay apply. The DevTools Performance panel's "LCP breakdown" insight and the `web-vitals` attribution build both show these parts.

#### 287: How do you improve LCP when it is a hero image?

- Make it discoverable in the initial HTML: a real `<img>` tag with `src`, not a CSS background or something rendered later by JavaScript. If it must be a background, `preload` it.
- Add `fetchpriority="high"` so it isn't queued behind other images.
- Never put `loading="lazy"` on it.
- Serve it in AVIF or WebP at the right size for the device using `srcset` and `sizes`.
- Serve it from the same origin as the HTML, or `preconnect` to the image CDN.
- Reduce render-blocking CSS and JS so the image can be painted as soon as it arrives.
- Improve TTFB with caching at the CDN.

```html
<img
  src="/img/hero-1200.avif"
  srcset="
    /img/hero-800.avif   800w,
    /img/hero-1200.avif 1200w,
    /img/hero-1800.avif 1800w
  "
  sizes="100vw"
  width="1200"
  height="600"
  fetchpriority="high"
  alt="Summer collection"
/>
```

#### 288: How do you improve INP by breaking up long tasks?

Find the slow handler, then do only the work needed for visual feedback right away and move the rest to later tasks, yielding to the browser in between so it can paint.

```js
async function yieldToMain() {
  if (globalThis.scheduler?.yield) return scheduler.yield();
  return new Promise((resolve) => setTimeout(resolve, 0));
}

button.addEventListener("click", async () => {
  button.classList.add("loading"); // visible feedback first
  await yieldToMain(); // let the browser paint

  const result = computeTotals(cart); // heavy work
  await yieldToMain();

  renderSummary(result);
  await yieldToMain();

  sendAnalytics("checkout_click"); // not urgent
});
```

`scheduler.yield()` (Chrome 129 and later, and recent Firefox) puts the remaining work at the front of the queue, so it resumes sooner than `setTimeout`. Other fixes: debounce input handlers, avoid layout thrashing in handlers, reduce DOM size, move heavy computation to a Web Worker, and avoid big re-renders in frameworks (memoization, smaller state updates).

#### 289: How do you fix common causes of CLS?

- **Images and video without dimensions**: always set `width` and `height` attributes, or CSS `aspect-ratio`. The browser then reserves space before the file loads.
- **Ads, embeds and iframes**: reserve space with a fixed-size container or `min-height`.
- **Content injected above existing content** like banners or cookie notices: reserve space, overlay it instead, or insert it below the fold.
- **Web fonts**: use `font-display: optional`, or match the fallback font's metrics with `size-adjust`, `ascent-override` and `descent-override` so the swap doesn't move text.
- **Animations**: animate `transform`, not `top`, `left`, `width` or `height`.
- **bfcache**: pages restored from bfcache don't cause new load shifts, so making pages eligible helps too.

```css
.ad-slot {
  min-height: 250px;
}
.video-embed {
  aspect-ratio: 16 / 9;
  width: 100%;
}
```

In DevTools, the Layout Shift Regions option and the "Layout shift culprits" insight show which elements moved and why.

#### 290: What are best practices for loading web fonts quickly?

- Use **WOFF2** only. Every modern browser supports it.
- **Self-host** fonts on your own origin so they share the existing connection.
- **Preload** the one or two most important font files used above the fold.
- **Subset** fonts to the characters you need with `unicode-range` and tools like `pyftsubset` or `glyphhanger`.
- Use **variable fonts** when you need several weights, since one file can replace many.
- Choose a `font-display` value: `swap` for brand fonts that must show, `optional` to avoid layout shifts.
- Adjust the **fallback font metrics** to match the web font.

```css
@font-face {
  font-family: "Brand";
  src: url("/fonts/brand-var.woff2") format("woff2");
  font-weight: 100 900;
  font-display: swap;
  unicode-range: U+0000-00FF, U+0131, U+0152-0153;
}
@font-face {
  font-family: "Brand Fallback";
  src: local("Arial");
  size-adjust: 104%;
  ascent-override: 92%;
  descent-override: 24%;
}
body {
  font-family: "Brand", "Brand Fallback", sans-serif;
}
```

#### 291: How do third-party scripts hurt performance, and how do you control them?

They add network connections, download and parse time, main-thread work (often long tasks that hurt INP), layout shifts, and sometimes chains of more scripts. You also don't control when they change.

To control them:

- **Audit them**: in DevTools, group by third party in the Performance panel summary, or block a domain in the Network panel and measure the difference.
- **Remove** unused tags. Tag managers tend to collect old ones.
- **Load them later**: `async` or `defer`, or wait until after the page has loaded or the user interacts.
- **Use facades**: show a static preview of a chat widget or YouTube embed and load the real thing on click.
- **Self-host** when allowed, to avoid extra connections.
- **Preconnect** to third parties you can't avoid.
- **Set budgets** and review new tags like code changes.

```html
<!-- Facade: real player only loads on click -->
<button
  class="yt-facade"
  data-id="dQw4w9WgXcQ"
  style="background-image:url(/img/thumb.webp)"
>
  Play video
</button>
```

#### 292: When do you use `<picture>` instead of just `srcset`?

Use `srcset` with `sizes` when you have the same image at different resolutions and the browser should choose based on screen size and density. Use `<picture>` when you need control:

- **Format fallback**: offer AVIF, then WebP, then JPEG.
- **Art direction**: a different crop for mobile (a tall image) and desktop (a wide banner).

```html
<picture>
  <source
    media="(max-width: 600px)"
    type="image/avif"
    srcset="/img/banner-tall-600.avif 600w, /img/banner-tall-1200.avif 1200w"
    sizes="100vw"
  />
  <source
    type="image/avif"
    srcset="/img/banner-wide-1200.avif 1200w, /img/banner-wide-2400.avif 2400w"
    sizes="100vw"
  />
  <img
    src="/img/banner-wide-1200.jpg"
    alt="Sale"
    width="1200"
    height="400"
    fetchpriority="high"
  />
</picture>
```

The `<img>` inside is required. It carries `alt`, dimensions, `loading` and `fetchpriority`, and is the fallback. Browsers pick the first matching `<source>`, so order matters.

#### 293: What do `decoding="async"` and `img.decode()` do?

Decoding turns compressed image bytes into pixels and can take a while for large images. `decoding="async"` tells the browser it can decode the image off the critical path and doesn't have to present it in the same frame as other content, so it doesn't delay other updates. Chrome already decodes most images off the main thread, so the gain is often small, but it doesn't hurt for non-critical images.

`img.decode()` returns a promise that resolves when the image is decoded and ready to paint. This is useful for swapping images without a flash of partly decoded content:

```js
const img = new Image();
img.src = "/img/large-photo.avif";
await img.decode();
gallery.replaceChildren(img);
```

#### 294: How do you code split a frontend app?

Load code only when it is needed, using dynamic `import()`. Bundlers create a separate chunk for each dynamic import.

- **Route-based splitting**: each page is its own chunk.
- **Component-based splitting**: heavy components like editors, charts and maps load when used.
- **Interaction-based loading**: load code on hover or click.

```js
// Vanilla
button.addEventListener("click", async () => {
  const { openEditor } = await import("./editor.js");
  openEditor();
});

// React
const Chart = React.lazy(() => import("./Chart.jsx"));
<Suspense fallback={<Spinner />}>
  <Chart data={data} />
</Suspense>;
```

Watch for overly small chunks and for waterfalls where one chunk imports another. Preload chunks the user is likely to need next (`modulepreload`, or importing on hover).

#### 295: What is the difference between tree shaking and dead code elimination, and what is the `sideEffects` flag?

- **Tree shaking** works at the module level: it removes exports that nothing imports.
- **Dead code elimination** works inside the code: the minifier (Terser, esbuild, SWC, Oxc) removes code that can never run, like `if (false) {...}` or `if (process.env.NODE_ENV !== 'production')` after the value is replaced at build time.

A bundler can't remove a module that might do something just by being imported, like changing a global or adding CSS, unless the package says it is safe. That's what `"sideEffects"` in `package.json` is for:

```json
{
  "name": "my-ui-lib",
  "sideEffects": ["*.css"]
}
```

This means "every file except CSS can be dropped if unused". Other things that block tree shaking: CommonJS modules (`require`), barrel files that re-export everything through code with side effects, and classes with static initializers.

#### 296: How do you respect `prefers-reduced-motion`, and does it affect performance?

Some users set their system to reduce motion because animations can cause dizziness or nausea. Respect that by removing or reducing non-essential animation. It also saves CPU and battery on those devices.

```css
.card {
  transition: transform 300ms ease;
}

@media (prefers-reduced-motion: reduce) {
  *,
  *::before,
  *::after {
    animation-duration: 0.01ms !important;
    animation-iteration-count: 1 !important;
    transition-duration: 0.01ms !important;
    scroll-behavior: auto !important;
  }
}
```

```js
const reduce = matchMedia("(prefers-reduced-motion: reduce)");
if (!reduce.matches) startParallax();
reduce.addEventListener("change", (e) =>
  e.matches ? stopParallax() : startParallax(),
);
```

You can test it in DevTools: Rendering tab > Emulate CSS media feature `prefers-reduced-motion`.

#### 297: How do you segment RUM data to make it useful?

A single global p75 hides problems. Break the data down by:

- **Page type or route** (home, product, search, checkout), since each has different bottlenecks.
- **Device type** (mobile vs desktop) and, if you collect it, device memory or CPU cores.
- **Network quality**: `navigator.connection.effectiveType` where supported (Chromium only).
- **Country or region**, which shows CDN or server placement problems.
- **Navigation type**: first load, reload, back/forward (bfcache), prerendered.
- **Logged in vs anonymous**, cache hit vs miss, or A/B test variant.
- **Release version**, to spot regressions right after a deploy.

Always report percentiles (p75 like CrUX, plus p95) and sample counts, since small segments are noisy.

#### 298: How does the `web-vitals` attribution build help you debug?

The attribution build adds details to each metric that tell you _why_ it was slow, so you can fix it from field data alone.

```js
import { onLCP, onINP, onCLS } from "web-vitals/attribution";

onINP(({ value, attribution }) => {
  send({
    metric: "INP",
    value,
    target: attribution.interactionTarget, // CSS selector of the element
    type: attribution.interactionType, // pointer or keyboard
    inputDelay: attribution.inputDelay,
    processing: attribution.processingDuration,
    presentation: attribution.presentationDelay,
    scripts: attribution.longAnimationFrameEntries?.flatMap((f) =>
      f.scripts.map((s) => s.sourceURL),
    ),
  });
});

onLCP(({ value, attribution }) => {
  send({
    metric: "LCP",
    value,
    element: attribution.target,
    ttfb: attribution.timeToFirstByte,
    loadDelay: attribution.resourceLoadDelay,
    loadDuration: attribution.resourceLoadDuration,
    renderDelay: attribution.elementRenderDelay,
  });
});

onCLS(({ value, attribution }) => {
  send({
    metric: "CLS",
    value,
    largestShiftTarget: attribution.largestShiftTarget,
  });
});
```

With this, you can group slow INP by element and script, and slow LCP by which part of the load is the problem.

#### 299: What kinds of performance budgets can you set?

- **Quantity budgets**: total JavaScript under 170 KB compressed for the initial route, total page weight under 1 MB, no more than 50 requests, no more than 3 third-party origins.
- **Timing budgets**: LCP under 2.5 seconds and TBT under 200 ms in lab tests on a mid-range mobile profile. Field p75 INP under 200 ms.
- **Rule-based budgets**: Lighthouse performance score of at least 90.

Lighthouse CI assertions and tools like size-limit can enforce budgets in pull requests. (The old Lighthouse `budget.json` option was removed in Lighthouse 12, so use Lighthouse CI assertions instead.) Base budgets on your current state and competitors, then tighten them over time. A budget only works if someone owns it and a broken budget blocks the merge or triggers a conversation.

#### 300: Why do lab results (Lighthouse) and field results (CrUX/RUM) often disagree?

- **Devices and networks**: Lighthouse uses one simulated mid-range phone and connection. Real users range from new flagships to old cheap phones.
- **Cache state**: Lighthouse usually tests a cold cache. Real users often have cached assets, or come back via bfcache.
- **Interactions**: lab tests don't click or scroll, so they miss INP and layout shifts that happen later.
- **Content differences**: real users see personalized content, logged-in pages, cookie banners, A/B tests and ads that a lab run might not.
- **Geography**: lab runs from one location; users come from everywhere.
- **Time window**: CrUX is a 28-day rolling window, so fixes take weeks to show fully.
- **LCP element differences**: on different screen sizes a different element may be the LCP.

Use field data to decide what to work on and lab tools to diagnose and test fixes.

---

## Advanced Questions (301-450)

### Advanced: Web Platform Fundamentals (301-315)

#### 301: How would you build a virtualized list, and what are the hard parts?

A virtualized list renders only the rows near the viewport plus a small buffer, and uses a spacer (or a translated container) to keep the scrollbar the right size. With 100,000 rows you might have only 30 DOM nodes at a time.

```js
const ROW_HEIGHT = 32;
const BUFFER = 10;
const viewport = document.querySelector("#viewport"); // overflow: auto; height: 600px
const spacer = document.querySelector("#spacer"); // height = total
const rowsEl = document.querySelector("#rows"); // position: absolute

spacer.style.height = `${items.length * ROW_HEIGHT}px`;

function render() {
  const start = Math.max(
    0,
    Math.floor(viewport.scrollTop / ROW_HEIGHT) - BUFFER,
  );
  const end = Math.min(
    items.length,
    Math.ceil((viewport.scrollTop + viewport.clientHeight) / ROW_HEIGHT) +
      BUFFER,
  );
  rowsEl.style.transform = `translateY(${start * ROW_HEIGHT}px)`;
  rowsEl.replaceChildren(...items.slice(start, end).map(makeRow));
}

let ticking = false;
viewport.addEventListener(
  "scroll",
  () => {
    if (ticking) return;
    ticking = true;
    requestAnimationFrame(() => {
      render();
      ticking = false;
    });
  },
  { passive: true },
);
render();
```

The hard parts:

- **Variable row heights**: you have to measure rows (with `ResizeObserver`), cache heights and keep a prefix-sum of offsets. Scroll position jumps if estimates are wrong.
- **Node recycling**: reusing row elements instead of creating new ones cuts GC and layout work.
- **Accessibility**: screen readers only see rendered rows. Use `aria-rowcount` and `aria-rowindex`, and make sure keyboard navigation and focus survive when rows are recycled.
- **Find-in-page** doesn't find unrendered rows. If that matters, `content-visibility: auto` on real rows is a simpler alternative for lists in the low thousands.
- **Scroll anchoring and fast scrolling**: blank areas appear if rendering can't keep up.

#### 302: What does "ResizeObserver loop completed with undelivered notifications" mean, and how do you avoid it?

`ResizeObserver` callbacks run after layout in the rendering step. If your callback changes something that resizes an observed element again, the browser runs another round of layout and observation in the same frame. To avoid infinite loops, it only processes elements deeper in the tree on each extra round. If there are still pending notifications after that, it skips them for this frame and fires that error event. It is a warning that you are causing extra layouts per frame, and it often means a feedback loop.

Ways to fix it:

- Don't change the observed element's own size in its callback. Change children or other elements, or use CSS (container queries often replace this pattern entirely).
- Compare the new size to the last one and do nothing if nothing meaningful changed.
- If you must write a size, defer it to the next frame with `requestAnimationFrame`, accepting a one-frame delay.

```js
const last = new WeakMap();
const ro = new ResizeObserver((entries) => {
  for (const e of entries) {
    const w = Math.round(e.contentBoxSize[0].inlineSize);
    if (last.get(e.target) === w) continue;
    last.set(e.target, w);
    requestAnimationFrame(() => updateChartFor(e.target, w));
  }
});
```

#### 303: Which DOM APIs force synchronous layout or style, and how do you find them in a trace?

Reading anything that depends on current geometry or computed style while there are pending changes forces the browser to do that work right away. Common examples:

- `offsetTop/Left/Width/Height`, `clientWidth/Height`, `scrollTop/Height/Width`
- `getBoundingClientRect()`, `getClientRects()`
- `getComputedStyle()` (for layout-dependent properties, and it forces style in any case)
- `innerText` (needs layout to know what is rendered)
- `focus()` (it may scroll), `scrollIntoView()`, `scrollTo()` reads
- `window.innerWidth`/`innerHeight` in some cases, `elementFromPoint()`
- `checkVisibility()` when it needs current style

In the DevTools Performance panel, these appear as "Recalculate Style" or "Layout" events inside your JavaScript call stack, marked with a red triangle and a "Forced reflow" warning that links to the line of code. The "Forced reflow" insight lists the worst ones. In the field, the Long Animation Frames API reports `forcedStyleAndLayoutDuration` per script.

The fix is to batch reads before writes, cache values that don't change, or use observers (`ResizeObserver`, `IntersectionObserver`) that give you geometry without forcing layout.

#### 304: How do you build a browser stream pipeline that respects backpressure?

Streams in the browser use a queuing strategy. A `ReadableStream` with `pull()` only produces data when the consumer has room, and `pipeThrough`/`pipeTo` pass backpressure along the chain automatically.

```js
function rowsFromApi(url) {
  let cursor = null;
  return new ReadableStream(
    {
      async pull(controller) {
        const res = await fetch(`${url}?cursor=${cursor ?? ""}`);
        const { rows, next } = await res.json();
        rows.forEach((r) => controller.enqueue(r));
        cursor = next;
        if (!next) controller.close();
      },
    },
    new CountQueuingStrategy({ highWaterMark: 500 }),
  );
}

const toCsv = new TransformStream({
  transform(row, controller) {
    controller.enqueue(`${row.id},${row.name}\n`);
  },
});

const handle = await window.showSaveFilePicker({ suggestedName: "export.csv" });
await rowsFromApi("/api/rows")
  .pipeThrough(toCsv)
  .pipeThrough(new TextEncoderStream())
  .pipeThrough(new CompressionStream("gzip"))
  .pipeTo(await handle.createWritable());
```

Because `pull()` is only called when the queue is below `highWaterMark`, a slow disk write slows down the API fetches instead of letting rows pile up in memory. `CompressionStream` and `DecompressionStream` are built in, so you don't need a library for gzip. (`showSaveFilePicker` is Chromium-only, so use another writable sink elsewhere.)

#### 305: What does a Service Worker cost on navigation, and how do you reduce it?

If a Service Worker controls the page, every navigation goes through it. If the worker isn't running, the browser has to start it first (spin up a thread and run the script), which can add tens to hundreds of milliseconds, more on slow phones. Then your `fetch` handler runs before the network request starts.

Ways to reduce it:

- **Navigation preload**: the browser starts the network request in parallel with the worker startup, and you use `event.preloadResponse`.

```js
self.addEventListener("activate", (e) => {
  e.waitUntil(self.registration.navigationPreload?.enable());
});
self.addEventListener("fetch", (e) => {
  if (e.request.mode === "navigate") {
    e.respondWith(
      (async () => (await e.preloadResponse) || fetch(e.request))(),
    );
  }
});
```

- **Static Routing API** (Chrome 123+): declare routes at install time so the browser can skip starting the worker for matching requests and go straight to the network or cache.

```js
self.addEventListener("install", (e) => {
  e.addRoutes?.([
    { condition: { urlPattern: "/api/*" }, source: "network" },
    { condition: { urlPattern: "/assets/*" }, source: "cache" },
  ]);
});
```

- **Keep the worker script small** and avoid heavy work at the top level.
- **Don't add a `fetch` handler you don't need**. A worker without one doesn't delay navigations.

Measure with `PerformanceNavigationTiming`: `workerStart` and `fetchStart` show worker startup time.

#### 306: How do you make IndexedDB fast?

- **Batch writes into one transaction**. Each transaction has a fixed cost and, with strict durability, a disk flush. Writing 10,000 records in 10,000 transactions is far slower than one transaction.
- **Use relaxed durability** for data you can rebuild, like caches. Recent Chrome versions default to relaxed, but set it explicitly to be clear.
- **Use `getAll()` and `getAllKeys()`** with a key range and a count instead of iterating a cursor one record at a time. Each cursor step is an async round trip.
- **Create indexes** for the fields you query, and use key ranges instead of loading everything and filtering in JavaScript.
- **Store compact data**. Values go through structured cloning, so big nested objects cost CPU to write and read.
- **Run heavy work in a worker**. IndexedDB is async, but serialization still happens on the calling thread.

```js
const tx = db.transaction("products", "readwrite", { durability: "relaxed" });
const store = tx.objectStore("products");
for (const p of products) store.put(p);
await new Promise((ok, fail) => {
  tx.oncomplete = ok;
  tx.onerror = () => fail(tx.error);
});

const page = await new Promise((ok) => {
  const req = db
    .transaction("products")
    .objectStore("products")
    .index("byCategory")
    .getAll(IDBKeyRange.only("lamps"), 100);
  req.onsuccess = () => ok(req.result);
});
```

#### 307: How do you handle backpressure with WebSockets in the browser?

The classic `WebSocket` API has no backpressure. `send()` never blocks; data just piles up in an internal buffer. You can check `bufferedAmount` to see how many bytes are queued and slow down yourself:

```js
async function sendAll(ws, chunks) {
  for (const chunk of chunks) {
    while (ws.bufferedAmount > 1_000_000) {
      await new Promise((r) => setTimeout(r, 50));
    }
    ws.send(chunk);
  }
}
```

Incoming messages are also delivered as fast as they arrive, even if your handler can't keep up, so a fast server can flood a slow client with work on the main thread.

`WebSocketStream` (Chromium, since Chrome 124) exposes the connection as streams, so writes wait when the buffer is full and reads only happen when you ask:

```js
const wss = new WebSocketStream("wss://example.com/feed");
const { readable, writable } = await wss.opened;
const writer = writable.getWriter();
await writer.write("subscribe:prices");

for await (const msg of readable) {
  await handle(msg); // the next message isn't read until this finishes
}
```

For new projects needing multiple streams, unreliable datagrams and backpressure, WebTransport over HTTP/3 is another option.

#### 308: What do you need to use `SharedArrayBuffer`, and when is it worth it?

`SharedArrayBuffer` lets the main thread and workers share the same memory instead of copying messages. Because it enables high-resolution timers that can be used for Spectre attacks, browsers only allow it when the page is **cross-origin isolated**. You need these headers on the document:

```http
Cross-Origin-Opener-Policy: same-origin
Cross-Origin-Embedder-Policy: require-corp
```

(or `Cross-Origin-Embedder-Policy: credentialless`, which is easier with third-party resources). Check `self.crossOriginIsolated` at runtime. Every cross-origin resource must then allow embedding through CORS or `Cross-Origin-Resource-Policy`, which can break ads, embeds and OAuth popups.

```js
// main
const sab = new SharedArrayBuffer(4 * 1024);
const counter = new Int32Array(sab);
worker.postMessage(sab);

// worker
self.onmessage = ({ data }) => {
  const counter = new Int32Array(data);
  Atomics.add(counter, 0, 1);
  Atomics.notify(counter, 0);
};
```

It is worth it for WebAssembly threads (for example video encoding or ML inference), large shared buffers like audio or image data processed in parallel, and lock-free ring buffers between threads. For ordinary message passing, transferables are simpler and fast enough.

#### 309: What are the performance considerations for View Transitions?

The View Transitions API (same-document in all major browsers, cross-document in Chromium and Safari) captures snapshots of old and new states and animates between them with CSS.

Things to watch:

- **Capture cost**: each element with a `view-transition-name` becomes a separate snapshot and layer. Hundreds of named elements (for example, every item in a long grid) use a lot of GPU memory and slow the start of the transition.
- **Rendering is paused** during `startViewTransition` while the update callback runs. A slow DOM update (or a slow data fetch inside the callback) freezes the page and hurts INP. Fetch data first, then start the transition with a quick synchronous DOM update.
- **Animations run on the compositor** by default (transforms and opacity on pseudo-elements). Custom animations of layout properties on the pseudo-elements lose that.
- **Cross-document transitions** wait for the new page to be render-ready. Use `<link rel="expect" blocking="render">` carefully, as it can delay first paint.
- **Reduced motion**: turn transitions off or make them simpler with `@media (prefers-reduced-motion: reduce)`.

```js
async function navigate(url) {
  const data = await fetchPage(url); // slow part outside the transition
  if (!document.startViewTransition) return render(data);
  document.startViewTransition(() => render(data)); // keep this fast
}
```

#### 310: How do you keep complex SVG animations smooth?

- **Animate transforms and opacity** on SVG elements with CSS or the Web Animations API. Changing path data (`d`), `points`, or attributes like `width` re-triggers SVG layout and repaint of the whole affected area.
- **Avoid animating filters** (`feGaussianBlur`, drop shadows) and masks over large areas. They are expensive to repaint every frame.
- **Reduce path complexity**: an icon exported with 20,000 path points costs time to rasterize. Simplify with SVGO or by lowering precision.
- **Limit the number of elements**. Thousands of small animated SVG nodes are DOM nodes with style and layout costs. Switch to Canvas or WebGL beyond a few thousand.
- **Give the animated part its own layer** by wrapping it in an HTML element with `will-change: transform` so changes don't repaint the rest of the SVG.
- **Prefer CSS or WAAPI over SMIL** (`<animate>`) for transforms, since browsers can sometimes run them on the compositor. SMIL animations always run on the main thread.
- **Use `<img src="icon.svg">` for static SVGs** where you don't need styling. The browser caches the rasterized image and it doesn't add nodes to your DOM.

Check the effect with Paint flashing in the Rendering tab and the Frames track in the Performance panel.

#### 311: How do you build a high-performance animation loop with `OffscreenCanvas` in a worker?

Moving rendering into a worker keeps it smooth even when the main thread is busy with framework updates or input handling. Workers that own an `OffscreenCanvas` can use `requestAnimationFrame` too.

```js
// main.js
const canvas = document.querySelector("canvas");
const off = canvas.transferControlToOffscreen();
const worker = new Worker(new URL("./render-worker.js", import.meta.url), {
  type: "module",
});
worker.postMessage({ type: "init", canvas: off, dpr: devicePixelRatio }, [off]);

new ResizeObserver(([e]) => {
  const { inlineSize: w, blockSize: h } = e.devicePixelContentBoxSize[0];
  worker.postMessage({ type: "resize", w, h });
}).observe(canvas);

// render-worker.js
let ctx,
  particles = [];
self.onmessage = ({ data }) => {
  if (data.type === "init") {
    ctx = data.canvas.getContext("2d", { alpha: false, desynchronized: true });
    requestAnimationFrame(loop);
  }
  if (data.type === "resize") {
    ctx.canvas.width = data.w;
    ctx.canvas.height = data.h;
  }
};

function loop(t) {
  ctx.fillStyle = "#000";
  ctx.fillRect(0, 0, ctx.canvas.width, ctx.canvas.height);
  ctx.fillStyle = "#4af";
  ctx.beginPath();
  for (const p of particles) {
    ctx.moveTo(p.x + 2, p.y);
    ctx.arc(p.x, p.y, 2, 0, Math.PI * 2);
  }
  ctx.fill(); // one fill for all particles
  requestAnimationFrame(loop);
}
```

Notes: `alpha: false` lets the browser skip blending with the page. `desynchronized: true` lowers latency for drawing apps but may cause tearing. `devicePixelContentBoxSize` gives exact device pixels so the canvas is sharp without guessing. Send input events to the worker in batches, not one message per `pointermove`.

#### 312: How do you handle high-frequency pointer input efficiently?

Browsers already align `pointermove`, `mousemove` and `touchmove` to frames (roughly one event per frame). For drawing apps that need every point, use `getCoalescedEvents()` to get the in-between samples, and `getPredictedEvents()` to reduce perceived latency.

```js
canvas.addEventListener("pointermove", (e) => {
  for (const ce of e.getCoalescedEvents?.() ?? [e]) {
    points.push([ce.offsetX, ce.offsetY, ce.pressure]);
  }
  scheduleDraw();
});
```

Other practices:

- Use pointer events instead of separate mouse and touch handlers.
- Use `pointerrawupdate` (Chromium) only if you really need lower latency than per-frame events, since it fires much more often.
- Keep handlers tiny: store the data, then draw in `requestAnimationFrame`.
- Use `touch-action: none` on drawing surfaces so the browser doesn't wait to decide if the gesture is a scroll.
- Use `setPointerCapture` instead of adding listeners to `document` on pointerdown.
- For delegated handlers on huge containers, check the target with a cheap test (`dataset`, `matches`) before calling `closest()` up a deep tree.

#### 313: What are the common sources of memory leaks in long-lived single-page apps, and how do you design against them?

- **Listeners on global objects** (`window`, `document`, a global event bus) added by components and never removed. The closure keeps the component and its DOM alive.
- **Timers and intervals** not cleared on unmount.
- **Observers** (`ResizeObserver`, `IntersectionObserver`, `MutationObserver`) not disconnected.
- **Caches** in module scope (`Map` keyed by object or ID) that only grow.
- **Detached DOM** held by references in state, closures or third-party libraries.
- **Pending promises and subscriptions** (WebSocket handlers, RxJS subscriptions) that capture component state.

A clean pattern is to give each component one `AbortController` and pass its signal to everything:

```js
function mountWidget(root) {
  const ac = new AbortController();
  const { signal } = ac;

  window.addEventListener("resize", onResize, { signal });
  document.addEventListener("keydown", onKey, { signal });
  fetch("/api/widget", { signal })
    .then(render)
    .catch(() => {});

  const ro = new ResizeObserver(onResize);
  ro.observe(root);
  signal.addEventListener("abort", () => ro.disconnect());

  const id = setInterval(poll, 5000);
  signal.addEventListener("abort", () => clearInterval(id));

  return () => ac.abort(); // one call cleans up everything
}
```

Use `WeakMap` for metadata keyed by objects so entries disappear with the key. `WeakRef` and `FinalizationRegistry` exist, but GC timing is not guaranteed, so don't build correctness on them. Test with the heap snapshot technique after repeating the mount/unmount cycle many times.

#### 314: Why is hydration expensive, and what are the ways to reduce it?

With server-side rendering, the HTML arrives ready to display, but frameworks then download the JavaScript for every component, run it, rebuild the virtual tree and attach event listeners, which is hydration. On big pages this means a large bundle and long tasks right at the point when users start interacting, so the page looks ready but doesn't respond (bad INP and TBT). Hydration mismatches can also force the framework to re-render parts of the page from scratch.

Ways to reduce it:

- **Ship less JS**: React Server Components and similar models keep server-only components out of the client bundle.
- **Partial hydration / islands** (Astro, Fresh): only interactive widgets get hydrated; the rest stays static HTML.
- **Selective and progressive hydration**: React 18+ hydrates `Suspense` boundaries separately and prioritizes the ones the user interacts with. Angular and others support deferred or incremental hydration.
- **Resumability** (Qwik): serializes state into HTML so no hydration pass is needed; code loads on interaction.
- **Lazy hydration triggers**: hydrate below-the-fold components when visible or idle.
- **Avoid mismatches**: no `Date.now()`, random values or `window` checks that render differently on server and client.

Measure with the Performance panel: look for one huge "Evaluate Script" and long tasks right after FCP.

#### 315: What are some advanced `fetch` options that affect performance?

- **`priority`**: `'high'`, `'low'` or `'auto'`, to change scheduling against other requests.
- **`keepalive: true`**: the request survives page unload, like `sendBeacon` but with any method and headers. Total body size for in-flight keepalive requests is limited to 64 KB.
- **Request body streaming**: send a `ReadableStream` as the body with `duplex: 'half'` to upload while data is still being produced. Chrome requires HTTP/2 or HTTP/3 for this.
- **`signal`** with `AbortSignal.timeout()` and `AbortSignal.any()` for cancellation.
- **`cache`** mode: `'no-store'`, `'reload'`, `'no-cache'`, `'force-cache'`, `'only-if-cached'` (same-origin only), to control the HTTP cache for that request.
- **`fetchLater()`** (Chromium, newer): queues a request that the browser sends on unload or after a timeout, for reliable analytics beacons.

```js
const { readable, writable } = new TransformStream();
const upload = fetch("/api/upload", {
  method: "POST",
  body: readable.pipeThrough(new CompressionStream("gzip")),
  duplex: "half",
  headers: { "Content-Encoding": "gzip" },
  priority: "low",
});

const writer = writable.getWriter();
for await (const chunk of recordAudioChunks()) await writer.write(chunk);
await writer.close();
await upload;
```

---

### Advanced: Google Chrome and Browser Internals (316-330)

#### 316: Walk through Chrome's RenderingNG pipeline from a DOM change to pixels on screen.

1. **Main thread (renderer)**: JavaScript changes the DOM or styles. In the next rendering opportunity, Blink runs rAF callbacks, then **style** (compute styles for invalidated elements), **layout** (LayoutNG builds an immutable fragment tree), **pre-paint** (builds property trees for transforms, clips, effects and scroll), and **paint** (records display items into paint chunks). It also decides compositing layers (**layerize**).
2. **Commit**: the main thread hands the layer list and property trees to the **compositor thread** (cc). The main thread is then free.
3. **Compositor thread**: handles scroll and compositor animations, and decides which tiles to rasterize.
4. **Raster**: tiles are rasterized, usually on the GPU through the GPU process (with Skia), using raster worker threads to prepare work.
5. **Activate**: rasterized tiles move from the pending tree to the active tree, so the compositor never shows half-finished content.
6. **Draw**: the compositor makes a compositor frame (quads that point to textures) and sends it to **Viz** in the GPU process.
7. **Viz display compositor**: combines frames from all renderers (including cross-site iframes in other processes) and the browser UI, and presents the result to the screen on vsync.

Because steps 3 to 7 don't need the main thread, scrolling and compositor animations stay smooth when JavaScript is busy, but anything needing a new main-thread frame (DOM changes, non-composited animations) waits.

#### 317: Why might an animation fail to run on the compositor, even if it only animates `transform`?

DevTools shows these as "non-composited animations" in the Performance panel and in Lighthouse, with a reason. Common reasons:

- The animation also includes a property that can't be composited, like `width`, `top`, `background-color` or most `filter`s in some cases. One non-composited property makes the whole animation run on the main thread.
- The element uses `transform` with percentages that depend on the element's size, and the size changes during the animation.
- The animation uses a timing function or composite mode the compositor doesn't support, or a custom property animated with `@property` that feeds a non-composited property.
- The element can't get its own layer, for example with some SVG content.
- It is driven by JavaScript every frame (`requestAnimationFrame` changing `style.transform`) instead of CSS or the Web Animations API. That still skips layout and paint, but it depends on the main thread being free each frame.

The fix is to animate only `transform`, `opacity` and (in Chromium) some `filter` and `clip-path` cases, declared with CSS or WAAPI, and to check the reason Chrome reports.

#### 318: What is layer explosion, and how does overlap cause it?

When an element gets its own compositor layer, any element painted on top of it that overlaps it may also need its own layer, to keep the correct stacking order. This is called "overlap testing". A single `will-change: transform` on an element low in the stacking order can cause many elements painted above it to be promoted, sometimes hundreds. Chrome tries to "squash" these into fewer layers, but squashing doesn't always work (for example, with different clip or scroll parents).

Symptoms: high GPU memory, slow "Layerize" or "Update Layer Tree" steps, slow raster, and jank on low-end devices. To check: the **Layers** panel in DevTools shows each layer, its size, memory estimate and the reason it was composited ("Overlaps other composited content", "has a will-change transform", and so on).

Fixes: put promoted elements high in the stacking order (`z-index`) so other elements don't overlap them, give them their own stacking context with `isolation: isolate`, remove unnecessary `will-change` and `translateZ(0)` hacks, and avoid promoting many large elements.

#### 319: How does Blink decide which elements need style recalculation after a change?

Blink uses **invalidation sets** built from your stylesheets. For each class, ID or attribute used in selectors, it records which other features depend on it. For example, with `.menu.open .item { ... }`, the invalidation set for class `open` says "elements with class `item` in the subtree need restyling". When you toggle `open`, Blink marks only matching descendants instead of the whole subtree.

Things that make invalidation broad:

- Selectors where the rightmost part is generic, like `.open *` or `.open div`, which mark the whole subtree.
- Sibling combinators (`~`, `+`) and `:nth-child()`, which can invalidate many siblings when one changes.
- `:has()`, which invalidates up the tree (ancestors), and Blink has to do extra work to figure out which ancestors are affected.
- Changes on `<html>` or `<body>` that many rules depend on, like theme classes.
- Changes to inherited properties or custom properties defined high in the tree.

In DevTools, the Performance panel's "Recalculate Style" event shows elements affected, and the "Selector stats" view (enable it in the panel settings) shows match attempts and time per selector.

#### 320: What can make layout expensive, and what is a layout boundary?

Layout gets expensive when a change dirties a large part of the tree. Normally a change to one element marks it and all ancestors as needing layout, and the parent may then have to lay out its other children too. Expensive patterns:

- Changes to elements whose size affects the parent: `width: auto` containers, flex and grid items, especially in big flex or grid layouts where one item's size change re-runs the algorithm for all of them.
- Tables with `table-layout: auto`, which need to look at all cells.
- Text with lots of inline content where a small change re-flows long paragraphs.
- Forced layouts inside loops.

A layout boundary is an element whose size and layout can't be affected by its contents, so changes inside don't propagate up. Elements with `contain: strict` or `contain: size layout` (or fixed width and height with `overflow: hidden` in some cases) work as boundaries. Using `contain` on widgets that update frequently keeps their layout local. LayoutNG also caches layout results for subtrees whose constraints didn't change, which helps, but avoiding unnecessary invalidation is still the main lever.

#### 321: What causes V8 deoptimization, and how do you investigate it?

TurboFan and Maglev generate code based on assumptions from type feedback, like "this argument is always a small integer" or "these objects always have shape X". When an assumption fails at runtime, V8 throws away the optimized code and goes back to a lower tier (deopt). If this happens repeatedly, the function may be stuck in slower code.

Common causes:

- Functions seeing different object shapes (polymorphic or megamorphic call sites).
- Numbers switching between small integers and doubles, or values that are sometimes `undefined`.
- Arrays changing their element kind (adding a double or a hole to an integer array).
- Using `arguments` in odd ways or `delete` on objects.
- `try/catch` used to be an issue but no longer is.

To investigate in Node:

```bash
node --trace-opt --trace-deopt app.js 2>&1 | grep -E 'deoptimizing|bailout' | head
```

This prints which function deoptimized and why ("wrong map", "not a Smi", "insufficient type feedback"). Tools like Deopt Explorer (VS Code extension) and `--prof` logs help visualize it. Only chase deopts in functions that a CPU profile shows are hot. Most code doesn't need this level of tuning.

#### 322: What are V8 elements kinds, and why can they affect array performance?

V8 tracks what kind of values an array holds to choose a fast representation:

- `PACKED_SMI_ELEMENTS`: only small integers, no holes.
- `PACKED_DOUBLE_ELEMENTS`: numbers including doubles, stored unboxed.
- `PACKED_ELEMENTS`: any values.
- `HOLEY_*` variants of each: the array has holes.

Transitions only go toward more general kinds: SMI → DOUBLE → ELEMENTS, and PACKED → HOLEY. They never go back, even if you remove the double or fill the hole.

```js
const a = [1, 2, 3]; // PACKED_SMI
a.push(4.5); // PACKED_DOUBLE, forever
a.push("x"); // PACKED_ELEMENTS, forever

const b = new Array(3); // HOLEY_SMI (holes from the start)
b[0] = 1;
b[1] = 2;
b[2] = 3; // still HOLEY

const c = []; // better: push to build packed arrays
for (let i = 0; i < 3; i++) c.push(i);
```

Holey arrays need extra checks on access (V8 must check the prototype chain for missing indexes). Generic element arrays store pointers to boxed numbers. For numeric hot loops, typed arrays (`Float64Array`, `Int32Array`) avoid all of this and have predictable memory use.

#### 323: How does V8's Orinoco garbage collector reduce pause times, and why can GC still hurt?

Orinoco combines several techniques:

- **Parallel scavenging**: the young generation is collected by several threads at once during a short pause.
- **Concurrent marking**: most of the old-generation marking runs on background threads while JavaScript keeps running. Write barriers record pointer changes made by JavaScript during marking so the collector stays correct.
- **Incremental marking**: the remaining main-thread marking is split into small steps.
- **Concurrent sweeping and parallel compaction**: dead memory is freed in the background, and compaction (moving objects to defragment) runs on several threads.
- **Idle-time GC**: in Chrome, GC work is scheduled in idle periods between frames.

GC can still hurt because:

- High allocation rates fill the young generation quickly, so scavenges run very often. Each one is short, but they add up and run on the main thread too.
- Objects that live a bit too long get promoted, which makes old-generation collections more frequent and bigger.
- When the heap is near its limit, V8 runs full collections over and over with little memory freed, which looks like the app freezing (in Node, this ends in "heap out of memory").
- Concurrent work still uses CPU on other cores, which matters in CPU-limited containers.
- Write barriers add a small cost to every pointer write during marking.

The fix is usually to allocate less in hot paths: reuse objects and buffers, avoid creating closures and arrays per item in tight loops, and stream instead of building huge arrays.

#### 324: What is pointer compression in V8, and why does it matter for Chrome vs Node.js?

With pointer compression, V8 stores heap pointers as 32-bit offsets from a base address instead of full 64-bit pointers. Objects become noticeably smaller (often around 40% less heap memory), which also improves cache use and GC speed. The trade-off is that each isolate's heap lives inside a 4 GB address range (the "cage"), so the heap of a single isolate can't grow beyond 4 GB.

Chrome enables it because tabs rarely need more than that and memory savings matter. Node.js does not enable it by default, because some server apps need heaps larger than 4 GB and because of native addon compatibility. There are experimental Node builds with pointer compression that show large memory savings for typical services. If your service uses well under 4 GB per process, this is worth watching, because it could cut memory use and GC time a lot. It's also another reason to prefer several smaller processes over one giant heap.

#### 325: How does the Blink scheduler prioritize work on the main thread?

The main thread doesn't use a single first-in, first-out queue. Blink's scheduler has several task queues with priorities, for example:

- **Input** (discrete input like clicks and key presses gets the highest priority, continuous input like mousemove is aligned with frames).
- **Rendering / compositor**: the "update the rendering" step, which gets boosted if it has been delayed too long so frames aren't starved.
- **Default**: networking callbacks, `postMessage`, most timers.
- **Low / idle**: `requestIdleCallback`, background `scheduler.postTask` tasks, some internal work.
- **Loading**-specific queues during page load, which may be given priority to speed up first paint.

Some details that matter:

- A task, once started, is never interrupted. Priority only affects which task runs next.
- Microtasks run after each task and can't be prioritized.
- `setTimeout` tasks share queues with other default-priority work, so they can be delayed by heavy activity.
- `scheduler.postTask()` maps to these priorities, and `scheduler.yield()` continuations go before other tasks of the same priority, which is why yielding with it doesn't lose your place in line.
- Background tabs and frozen frames have their queues throttled or paused.

So the main defense for responsiveness is still short tasks: the scheduler can only pick input first if the current task finishes quickly.

#### 326: What is the performance and memory cost of site isolation and out-of-process iframes?

Each site-isolated renderer process has a fixed overhead, often tens of MB for V8, Blink and its own caches, so pages with many cross-site iframes (ads, embeds, widgets) use much more memory. On low-memory Android devices Chrome isolates only some sites (for example, those where users log in) to reduce this.

Performance effects:

- **Out-of-process iframes (OOPIFs)** are rendered in separate processes and composited together by Viz. Layout and input handling across frames need inter-process communication.
- **`postMessage` between a page and a cross-site iframe** crosses process boundaries and is slower than same-process messaging. Avoid chatty high-frequency messaging.
- **Synchronous access** across frames (like reading `frames[0].document`) is impossible for cross-site frames, which removes some old patterns.
- **Process startup** for a new site costs time. Chrome keeps a "spare renderer" process warm to reduce this for navigations.
- **Process limits**: when Chrome hits its process limit, it starts sharing processes between same-site tabs, but never between different sites when isolation is on.

For your own app, avoid unnecessary cross-site iframes, put related widgets on the same site, and lazy load iframes below the fold.

#### 327: How does Blink manage DOM memory, and how can leaks cross between V8 and Blink?

DOM objects are C++ objects in Blink, managed by **Oilpan** (also called cppgc), a garbage-collected C++ heap. JavaScript objects live in V8's heap. Each DOM node has a JavaScript wrapper. V8 and Oilpan work together through **unified heap** tracing: during a major GC, marking follows references from JS objects to C++ objects and back, so they are collected together.

Leak patterns that cross the boundary:

- A JS closure (for example, an event listener on `window`) references a DOM node that was removed from the document. Oilpan can't free the node because V8 says it's reachable. This is the classic "detached DOM tree", and one detached node can keep its whole subtree alive.
- A DOM node references a JS object through an expando property or listener, and that JS object references large data.
- Native resources held by DOM objects, like decoded images in `<img>` or WebGL contexts, can be much bigger than the heap snapshot suggests.

In heap snapshots, look for `Detached` entries and follow retainers through "(internal)" and "InternalNode" links, which represent the C++ side.

#### 328: In what order does Chrome check its caches when a request is made?

For a typical subresource request, roughly:

1. **Memory cache** in the renderer: resources already loaded by this document (images, scripts, preloads). This is checked first and can even ignore some cache headers for the life of the document.
2. **Service Worker**: if the page is controlled, the request goes to the worker's `fetch` handler, which may answer from Cache Storage or call the network. (The Static Routing API can skip this step.)
3. **HTTP cache** (disk cache in the network service), keyed by URL plus the network isolation key (top-level site and frame site). Fresh entries are served directly. Stale ones are revalidated with `If-None-Match` or `If-Modified-Since`.
4. **Network**, possibly reusing an existing HTTP/2 or HTTP/3 connection, or a pushed/early-hinted preload.

Separate from these, the **back/forward cache** stores whole pages on history navigation, and **prefetch/prerender caches** from speculation rules hold responses for upcoming navigations. Knowing the order helps debugging: a Service Worker bug can serve stale files even when HTTP headers are correct, and "Disable cache" in DevTools doesn't bypass the Service Worker unless you also tick "Bypass for network" in the Application panel.

#### 329: How does prerendering work internally, and what code needs care?

When speculation rules trigger a prerender, Chrome loads the page in a hidden, separate "prerendered" page, often in a new renderer process. The page parses, runs JavaScript, fetches resources and renders, but it isn't visible. When the user navigates to it, Chrome **activates** it by swapping it in instantly. `document.prerendering` is `true` until activation, and the navigation entry's `activationStart` records when activation happened.

While prerendering, some APIs are deferred until activation: things that need user permission or attention, like geolocation, notifications, camera, `window.open` and fullscreen. Some cross-origin iframes are delayed too.

Code that needs care:

- **Analytics**: don't count a page view until activation.
- **Metrics**: measure LCP and TTFB relative to `activationStart`, otherwise prerendered pages look like they loaded before the user clicked (the `web-vitals` library handles this).
- **Side effects**: ad impressions, "seen" markers or anything that changes server state should wait.
- **Memory and data use**: prerendering costs the user bandwidth and CPU. Chrome limits how many prerenders run and cancels them on low memory or Data Saver.

```js
function whenActivated(fn) {
  if (document.prerendering) {
    document.addEventListener("prerenderingchange", fn, { once: true });
  } else {
    fn();
  }
}
whenActivated(() => analytics.pageView());
```

#### 330: How does Chrome throttle background pages, and what is exempt?

Chrome applies several layers of throttling to hidden pages and iframes:

- **Basic throttling**: timers in hidden pages run at most once per second.
- **Budget-based throttling**: after a page has been hidden for about 10 seconds, timer tasks share a limited CPU time budget. When the budget runs out, timers wait until it refills.
- **Intensive throttling**: after about 5 minutes hidden (if the page is quiet), chained timers may be aligned to run only once per minute.
- **Freezing**: on some platforms, especially Android, background pages may be frozen fully (no tasks run) and later discarded.
- `requestAnimationFrame` doesn't run at all in hidden pages, and cross-origin iframes that are out of view are throttled too.

Pages are generally exempt from the stronger throttling while they play audio, have an active WebRTC connection, or hold certain Web Locks or IndexedDB connections in some cases. Rules change between versions, so don't depend on precise behavior.

Design implications: don't use timers to keep state in sync in the background. Use Web Push, Service Worker background sync, or re-fetch on `visibilitychange`. For WebSocket heartbeats, expect delays in background tabs and make the server tolerant of them.

---

### Advanced: Browser Developer and Performance Tools (331-345)

#### 331: How would you use a Perfetto trace to find why frames are being dropped?

1. Record a trace from `ui.perfetto.dev` or `chrome://tracing` with categories that include rendering: the default "Rendering" or "Web developer" presets, plus `cc`, `gpu`, `viz`, and `blink` if needed. Reproduce the jank for a few seconds.
2. Open it in the Perfetto UI. Find the renderer process for your tab and the GPU process.
3. Look at the **frame timeline** tracks ("Expected Timeline" and "Actual Timeline" in newer traces, or `PipelineReporter` slices). They show each frame and whether it was presented on time, dropped or partially presented, and which stage was late.
4. For a late frame, check what stage took too long:
   - Main thread busy (long `ThreadControllerImpl::RunTask` slices, V8 execution, `LocalFrameView::UpdateLifecyclePhases`) means JavaScript, style or layout.
   - Compositor thread or raster workers busy means raster or too many layers.
   - GPU process (`VizCompositorThread`, GPU main thread) busy means GPU work, often big textures or heavy filters.
5. Use Perfetto's SQL query view to measure across many frames, for example:

```sql
SELECT name, COUNT(*) AS n, AVG(dur) / 1e6 AS avg_ms, MAX(dur) / 1e6 AS max_ms
FROM slice
WHERE name IN ('ThreadControllerImpl::RunTask', 'LocalFrameView::UpdateLifecyclePhases')
GROUP BY name;
```

This finds problems the DevTools Performance panel can't show clearly, like GPU process stalls or work from other tabs and extensions.

#### 332: What advanced features of the DevTools Performance panel help with rendering problems?

- **Enable advanced rendering instrumentation** (in panel settings, previously "advanced paint instrumentation"): records detailed paint and layer information, so you can click a paint event and see the paint profiler, or see layers per frame.
- **Enable CSS selector stats**: shows which selectors took the most time in each "Recalculate Style" event.
- **Initiators**: selecting an event like a "Layout" or a timer task shows arrows to what triggered it, such as the script line that invalidated layout or the `setTimeout` that scheduled the task.
- **Layout shift tracking**: the Layout Shifts track shows each shift and its culprits (images without size, fonts, injected content).
- **Annotations**: you can label regions and entries in a trace and save it, which helps when sharing findings with others.
- **Ignore list**: hide framework and library frames so your own code stands out in the flame chart.
- **Insights sidebar**: LCP breakdown, INP breakdown, render-blocking requests, forced reflow, DOM size, third parties, and more, each linked to the trace.
- **AI assistance** (if enabled): can explain a selected event or insight in plain language.
- **Saving traces**: export the trace (optionally with source maps and resource content) to share or compare later.

#### 333: How do you read the Frames track, and what is the difference between dropped and partially presented frames?

The Frames track in the Performance panel shows each frame the browser expected to produce:

- **Green or white (presented)**: the frame was shown on time.
- **Red (dropped)**: the browser couldn't produce a new frame in time, so the user saw the previous one again.
- **Yellow / dashed (partially presented)**: the compositor produced a frame on time, for example with an updated scroll position, but some main-thread updates weren't ready, so the frame shows partial changes. This is typical when the main thread is busy but the compositor can still scroll.
- **Idle**: nothing changed, so no frame was needed.

A run of dropped frames during an animation usually means compositor or GPU work is too slow (rasterization, too many layers). A run of partially presented frames during scrolling usually means the main thread is busy, so content updates like lazy-loaded images or scroll-linked JS lag behind the scroll. Click a frame to see its duration and the main-thread work that overlapped it.

#### 334: How do you use Long Animation Frames data in production to find the scripts behind poor INP?

Collect LoAF entries that overlap slow interactions and send the script details along with the INP value. Each `PerformanceScriptTiming` in `entry.scripts` includes:

- `invoker` and `invokerType`: what started it, like `BUTTON#buy.onclick`, a timer, a promise resolver or a classic script.
- `sourceURL`, `sourceFunctionName`, `sourceCharPosition`: where the code lives.
- `duration`, `executionStart`, `pauseDuration` (synchronous pauses like `alert`), and `forcedStyleAndLayoutDuration` (time spent in forced layouts).

```js
const loafs = [];
new PerformanceObserver((list) => loafs.push(...list.getEntries())).observe({
  type: "long-animation-frame",
  buffered: true,
});

new PerformanceObserver((list) => {
  for (const e of list.getEntries()) {
    if (!e.interactionId || e.duration < 200) continue;
    const end = e.startTime + e.duration;
    const overlapping = loafs.filter(
      (f) => f.startTime < end && f.startTime + f.duration > e.startTime,
    );
    send({
      inp: e.duration,
      target: e.target?.tagName,
      scripts: overlapping
        .flatMap((f) => f.scripts)
        .map((s) => ({
          invoker: s.invoker,
          url: s.sourceURL,
          fn: s.sourceFunctionName,
          dur: Math.round(s.duration),
          forcedLayout: Math.round(s.forcedStyleAndLayoutDuration),
        })),
    });
  }
}).observe({ type: "event", durationThreshold: 40, buffered: true });
```

Aggregate by `sourceURL` and `invoker` in your backend to find which first-party modules or third-party scripts cause the worst interactions. Cross-origin scripts only report their URL if served with CORS (`crossorigin` attribute plus CORS headers). The `web-vitals` attribution build does the matching for you via `longAnimationFrameEntries`.

#### 335: How does the Event Timing API represent interactions, and what are its quirks?

Each input event over the threshold produces a `PerformanceEventTiming` entry with:

- `startTime`: when the hardware event happened.
- `processingStart` / `processingEnd`: when handlers started and finished.
- `duration`: from `startTime` to the next paint after processing, **rounded to the nearest 8 ms**.
- `interactionId`: a non-zero ID shared by all events belonging to one user interaction (for example, `pointerdown`, `pointerup` and `click` from one tap). Events like `mousemove` have `interactionId` 0 and don't count toward INP.

```js
new PerformanceObserver((list) => {
  const byInteraction = new Map();
  for (const e of list.getEntries()) {
    if (!e.interactionId) continue;
    const prev = byInteraction.get(e.interactionId);
    if (!prev || e.duration > prev.duration)
      byInteraction.set(e.interactionId, e);
  }
  for (const e of byInteraction.values()) {
    console.log(e.name, e.duration, {
      inputDelay: e.processingStart - e.startTime,
      processing: e.processingEnd - e.processingStart,
      presentation: e.startTime + e.duration - e.processingEnd,
    });
  }
}).observe({ type: "event", durationThreshold: 16, buffered: true });
```

Quirks:

- The default `durationThreshold` is 104 ms, and the minimum is 16 ms, so short interactions aren't reported. `performance.interactionCount` (where supported) gives the total count.
- An interaction's latency is the max duration of its events.
- Because of rounding, presentation delay is approximate.
- Interactions inside cross-origin iframes are not visible to the parent page, but they do count in CrUX INP for the page. This is a common reason RUM and CrUX disagree.
- Keyboard interactions group `keydown` and `keyup`; scrolling isn't an interaction.

#### 336: In a heap snapshot, what do shallow size, retained size, distance and dominators mean?

- **Shallow size**: memory held by the object itself, not counting what it references. A string or array's shallow size includes its own storage.
- **Retained size**: how much memory would be freed if this object were deleted, meaning the object plus everything only reachable through it. This is usually the number that matters when hunting leaks.
- **Distance**: the shortest number of references from a GC root (like the global object or the stack) to this object. Objects with an unexpectedly large distance or that should be unreachable are interesting.
- **Dominator**: object A dominates B if every path from the roots to B goes through A. The retained size of A includes all objects it dominates. The dominator tree shows "who really owns" a big block of memory.

Useful tricks:

- Sort the Summary view by retained size and expand the largest constructors.
- Entries like `(closure)`, `(system)`, `(compiled code)`, `(array)` and `(string)` are internal groups. `system / Context` objects are closure scopes and often explain why a variable is kept alive.
- Use the Comparison view between two snapshots to see `# New`, `# Deleted` and `# Delta` per constructor.
- Naming your classes (rather than plain object literals) makes snapshots much easier to read, since objects are grouped by constructor name.

#### 337: Walk through investigating a memory leak in a production Node.js service.

1. **Confirm it's a leak**: look at heap used after GC over days, not RSS right after startup. A sawtooth pattern with a rising floor is a leak. A level plateau is just a warm cache.
2. **Check if it's the JS heap or native memory**: compare `heapUsed` with RSS and `external`/`arrayBuffers`. If RSS grows but the heap doesn't, look at Buffers, native addons, or allocator fragmentation instead of heap snapshots.
3. **Reproduce if you can**: replay the traffic mix against a staging instance with `--inspect` and take snapshots under load.
4. **Capture snapshots in production safely**: take the instance out of rotation, then trigger snapshots with `--heapsnapshot-signal=SIGUSR2` at two or three points in time, for example 1 hour apart. Make sure the container has spare memory, since writing a snapshot needs roughly the heap size again. As a backup, `--heapsnapshot-near-heap-limit=1` captures one just before a crash.
5. **Compare snapshots** in DevTools: Comparison view, sort by `# Delta` and size delta. Look for constructors that grow steadily, like `Socket`, `IncomingMessage`, `Promise`, `Timeout`, closures, or your own classes.
6. **Follow retainers** of a few growing objects to the root: a module-level `Map`, an `EventEmitter` listener array, an `AsyncLocalStorage` store kept by a long-lived resource, or an unresolved promise held by a queue.
7. **Fix and verify** with a soak test, then watch the post-GC heap trend in production.

Common Node leaks: unbounded memoization caches, listeners added per request to a shared emitter (watch for `MaxListenersExceededWarning`), timers not cleared, promises that never settle, global arrays used as "temporary" buffers, and per-request closures captured by a long-lived object such as a DB client.

#### 338: What is a Node.js diagnostic report, and when is it useful?

A diagnostic report is a JSON file describing the state of a Node process: JavaScript and native stack traces, heap statistics (per space), resource usage (CPU, memory, page faults), libuv handles (open sockets, timers, files), environment variables, command-line flags, loaded shared libraries, OS limits (`ulimit`) and the Node/V8 versions.

```bash
node --report-on-fatalerror --report-uncaught-exception --report-on-signal \
     --report-signal=SIGUSR2 --report-directory=/var/log/node-reports server.js
```

```js
process.report.writeReport(); // from code
const r = process.report.getReport();
console.log(r.libuv.filter((h) => h.type === "tcp").length, "TCP handles");
```

It is useful when:

- The process crashes with a native error or OOM and you need to see the last state.
- The process hangs and you need the current JS stack without attaching a debugger.
- You suspect a handle leak (thousands of open sockets or timers).
- You need to compare environment and limits between a working and failing machine.

Reports may include environment variables with secrets, so treat them as sensitive. Exclude the environment with `--report-exclude-env` (Node 22+) if needed.

#### 339: How do you use WebPageTest to evaluate a change like moving to a new CDN or adding Early Hints?

1. **Set up a controlled comparison**: same test location, browser, connection profile and number of runs (at least 5 to 9, use the median). Test first view and repeat view.
2. **Test both variants side by side**: use two URLs, or one URL with a script that overrides DNS (`setDns`) or sets a header or cookie to choose the variant. For CDN changes, run from several regions, since the impact is often regional.
3. **Compare waterfalls**: look at DNS, connect and TLS times for the main origin, TTFB, when the critical resources start, and whether connections are reused or coalesced. For Early Hints, check that preloads start before the HTML response arrives.
4. **Compare filmstrips and the visual progress chart**: Start Render, LCP and Speed Index should improve, not just "Document Complete".
5. **Use custom metrics**: WebPageTest can run JavaScript at the end of the test to collect values like `nav.responseStart` or a server timing header.
6. **Check the "Opportunities and Experiments" feature** (on the hosted version), which lets you test changes like adding preloads or deferring scripts without deploying.
7. **Check variance**: if runs differ a lot, increase run count or investigate the cause before drawing conclusions.

#### 340: What is the difference between Lighthouse's simulated, DevTools and provided throttling?

- **Simulated throttling** (default in the CLI, Lighthouse CI and PageSpeed Insights): the page loads at full speed, then Lighthouse's Lantern model simulates how the load would go on a slow network and CPU, using the observed dependency graph. It is fast and less noisy, but it is an estimate and can be wrong for pages with unusual loading patterns, service workers or lots of late-discovered resources.
- **DevTools (applied) throttling**: the network and CPU are actually slowed down while loading (request-level latency and bandwidth limits plus CPU slowdown). It is closer to reality for some cases but noisier, and request-level throttling doesn't model TCP effects perfectly.
- **Provided**: no throttling from Lighthouse. You run it on real slow hardware or with OS-level network shaping (for example `tc` or a throttled proxy), which is the most realistic but needs the most setup.

```bash
npx lighthouse https://example.com --throttling-method=devtools --output=json --output-path=./lh.json
```

When simulated and observed results differ a lot, Lighthouse shows a warning. Use the same method consistently when comparing runs over time.

#### 341: How do you analyze CrUX data in BigQuery?

The public `chrome-ux-report` dataset has monthly tables and pre-aggregated "materialized" tables. For a quick look at p75 trends for an origin:

```sql
SELECT date, device, p75_lcp, p75_inp, p75_cls, p75_ttfb
FROM `chrome-ux-report.materialized.device_summary`
WHERE origin = 'https://www.example.com'
  AND date >= '2026-01-01'
ORDER BY date, device;
```

For histogram detail, query the raw monthly tables, where each metric is stored as histogram bins with density:

```sql
SELECT
  bin.start AS lcp_ms,
  SUM(bin.density) AS density
FROM `chrome-ux-report.all.202609`,
  UNNEST(largest_contentful_paint.histogram.bin) AS bin
WHERE origin = 'https://www.example.com'
GROUP BY lcp_ms
ORDER BY lcp_ms;
```

BigQuery is useful for comparing your site against competitors, looking at monthly history beyond what the API keeps, and slicing by country (the `country_*` tables) or effective connection type. Queries on the raw tables scan a lot of data, so watch your BigQuery costs and use the materialized tables when you can.

#### 342: How can you automate performance tracing with Puppeteer or the Chrome DevTools Protocol?

Puppeteer controls Chrome through the DevTools Protocol, so you can script a user flow, record a trace, and collect metrics in CI.

```js
import puppeteer from "puppeteer";

const browser = await puppeteer.launch();
const page = await browser.newPage();
const client = await page.createCDPSession();

await client.send("Network.emulateNetworkConditions", {
  offline: false,
  latency: 150,
  downloadThroughput: 1.6e6 / 8,
  uploadThroughput: 750e3 / 8,
});
await client.send("Emulation.setCPUThrottlingRate", { rate: 4 });

await page.tracing.start({ path: "trace.json", screenshots: true });
await page.goto("https://staging.example.com/", { waitUntil: "networkidle0" });
await page.click("#add-to-cart");
await page.waitForSelector(".cart-count");
await page.tracing.stop();

const lcp = await page.evaluate(
  () =>
    new Promise((resolve) => {
      new PerformanceObserver((l) =>
        resolve(l.getEntries().at(-1).startTime),
      ).observe({ type: "largest-contentful-paint", buffered: true });
    }),
);
console.log("LCP", lcp);
await browser.close();
```

The `trace.json` file opens in the DevTools Performance panel or Perfetto. Lighthouse user flows build on the same idea. Run each scenario several times and compare medians, because single runs are noisy.

#### 343: When reading a Node.js CPU profile, what do `(garbage collector)`, `(program)` and `(idle)` mean, and how do you map TypeScript back to source?

- **(idle)**: the event loop was waiting with nothing to do. A mostly idle profile under load means the bottleneck is elsewhere, like the database or a downstream service, or a lock or pool limit.
- **(program)**: time in native code that V8 couldn't attribute to a JavaScript function, such as parts of the runtime, native addons or the embedder. A large share may mean heavy native work like compression or TLS.
- **(garbage collector)**: time on the main thread doing GC. More than 5 to 10% under load points to high allocation rates.

For TypeScript or bundled code, enable source maps so profiles show original file names and lines:

```bash
node --enable-source-maps --cpu-prof dist/server.js
```

DevTools also uses source maps when loading a profile if it can find them. Keep in mind that inlining by TurboFan can hide small functions inside their callers. If a function vanishes from the profile, it may have been inlined. Run with `--no-turbo-inlining` only for diagnosis, never in production.

#### 344: How do you use V8's tick profiler (`--prof`), and when would you choose it over `--cpu-prof`?

`--prof` writes a V8 log of samples ("ticks") with both JavaScript and native C++ frames. You then process it with Node's built-in tool:

```bash
node --prof server.js
# run load, then stop the server
node --prof-process --preprocess isolate-0x*.log > processed.json
node --prof-process isolate-0x*.log > profile.txt
```

The text output has a "Summary" (JavaScript, C++, GC, shared libraries), a list of the hottest functions, and a "Bottom up (heavy) profile" showing callers.

Choose it when:

- A lot of time is in C++ or shared libraries (`libc`, `libcrypto`, `libz`) and you need to see which native functions are hot, which `--cpu-prof` shows only as `(program)`.
- You want to see whether functions are optimized (the log marks `*` for optimized and `~` for interpreted code).

Otherwise, `--cpu-prof` is easier because it opens straight in DevTools. For mixed native and JS views on Linux, `perf` with `--perf-basic-prof` is another strong option.

#### 345: How do you trace Node.js internals with trace events and view them in Perfetto?

Node can emit trace events in the Chrome trace format for V8, Node internals and your own code.

```bash
node --trace-event-categories v8,node,node.async_hooks,node.perf.usertiming \
     --trace-event-file-pattern 'trace-${pid}-${rotation}.log' server.js
```

You can also turn categories on at runtime:

```js
import trace_events from "node:trace_events";
const tracing = trace_events.createTracing({ categories: ["node.perf", "v8"] });
tracing.enable();
// ... later
tracing.disable();
```

`performance.mark()` and `performance.measure()` from `node:perf_hooks` appear in the `node.perf.usertiming` category, so your own spans show up on the same timeline as GC and V8 compile events.

Open the resulting file in `ui.perfetto.dev` or `chrome://tracing`. This is useful for seeing exactly when GC pauses happen relative to your requests, how long module loading and compilation take at startup, and async operation timing, all on one timeline. `node.async_hooks` adds a lot of events and overhead, so enable it only briefly.

---

### Advanced: JavaScript Runtime and Server-Side Fundamentals (346-360)

#### 346: Predict and explain the output order of this Node.js code.

```js
const fs = require("node:fs");

fs.readFile(__filename, () => {
  setTimeout(() => console.log("timeout"), 0);
  setImmediate(() => console.log("immediate"));
  process.nextTick(() => console.log("nextTick"));
  Promise.resolve().then(() => console.log("promise"));
});
console.log("sync");
```

Output:

```text
sync
nextTick
promise
immediate
timeout
```

Explanation:

- `sync` prints first, as synchronous code runs before the loop starts.
- The `readFile` callback runs in the **poll** phase. When it finishes, Node drains the `nextTick` queue and then the promise microtask queue, so `nextTick` and then `promise`.
- After poll, the loop goes to the **check** phase, so `setImmediate` runs: `immediate`.
- Then the loop goes around to the **timers** phase, so `timeout`.

Outside an I/O callback (in the main module), the order of `setTimeout(0)` and `setImmediate` is not guaranteed, because it depends on whether 1 ms has passed when the loop starts. Inside an I/O callback, `setImmediate` always runs first. In ES modules, top-level code runs as part of module evaluation, which itself is async, so timing can differ again.

#### 347: Your Node.js API slows down under load even though CPU isn't maxed. Profiling shows long waits in password hashing, file reads and DNS. What is going on?

These all use libuv's thread pool, which has 4 threads by default. `bcrypt` (native), `crypto.scrypt`/`pbkdf2`, `fs.*` calls, `dns.lookup()` (used by `http.request` and most clients for hostname resolution) and `zlib` compete for those 4 threads. When a few slow hashing jobs occupy all threads, every file read and DNS lookup waits behind them. Latency grows while CPU looks only partly used, because only 4 threads work at a time.

How to confirm: time `dns.lookup()` and `fs.promises.readFile()` under load, or use `async_hooks`/trace events to see queueing. Event loop lag stays low, which points away from main-thread blocking.

Fixes:

- Raise `UV_THREADPOOL_SIZE` to match CPU cores (set before startup).
- Move password hashing to a dedicated worker thread pool with its own concurrency limit, so it can't starve other work.
- Avoid `dns.lookup()` on hot paths: use connection keep-alive (fewer lookups), a DNS cache, or `dns.resolve*` (which uses c-ares and the network, not the pool).
- Read config and templates once at startup instead of per request.
- Use `zlib` streaming at lower compression levels, or offload compression to a proxy or CDN.

#### 348: How can microtasks or `process.nextTick` starve the event loop?

Node drains the whole `nextTick` queue and then the whole microtask queue before continuing the loop, and new entries added during the drain are also run. Recursive scheduling therefore never yields:

```js
function spin() {
  process.nextTick(spin); // I/O, timers and new requests never get a turn
}
spin();
```

The same happens with a promise chain that keeps resolving synchronously in a loop, for example an `async` function that processes a large in-memory array with `await` on already-resolved values:

```js
async function processAll(items) {
  for (const item of items) {
    await handle(item); // if handle() is sync-ish and returns resolved promises,
  } // this never yields to I/O
}
```

Each `await` continues in a microtask, so if nothing actually waits on I/O, the loop runs to the end without letting other callbacks run. Event loop delay metrics look awful while CPU stays at 100% on one core.

Fixes: yield explicitly with `await setImmediate()` from `node:timers/promises` every N items, use `setImmediate` instead of `nextTick` for recursive scheduling, or move the work to a worker.

#### 349: How do `highWaterMark`, object mode and async iteration interact in Node.js streams?

- `highWaterMark` is the buffer threshold that triggers backpressure. For byte streams it is in bytes (default 64 KB for most streams since Node 22, previously 16 KB, and file read streams use 64 KB). For object mode streams it counts objects (default 16).
- In **object mode**, each chunk is one JavaScript value, whatever its size. A `highWaterMark` of 16 objects could be 16 tiny rows or 16 huge documents, so memory use depends on object size.
- **`for await...of`** on a readable stream reads one chunk at a time and only pulls more when your loop body finishes. That gives natural backpressure: a slow loop body slows the source.

```js
import { Readable, Transform } from "node:stream";
import { pipeline } from "node:stream/promises";

const source = Readable.from(generateRows(), {
  objectMode: true,
  highWaterMark: 100,
});

for await (const row of source) {
  await saveToDb(row); // source is paused while this awaits
}

// Or as a pipeline stage with async generator functions
await pipeline(
  source,
  async function* (rows) {
    for await (const r of rows) yield JSON.stringify(r) + "\n";
  },
  process.stdout,
);
```

Pitfalls: mixing `on('data')` (flowing mode, no backpressure unless you call `pause()`) with async handlers, forgetting that `Readable.from(array)` puts everything in memory up front anyway, and setting huge `highWaterMark` values "for speed", which just uses more memory without real gains once the buffer is bigger than a few chunks.

#### 350: How do you write a custom Transform stream with proper error handling and backpressure?

Implement `transform` (and `flush` if you need to output data at the end), call the callback once per chunk, and push output with `this.push()` or by passing it to the callback. Use `pipeline` so errors in any stage destroy all stages and close file handles and sockets.

```js
import { Transform } from "node:stream";
import { pipeline } from "node:stream/promises";
import { createReadStream, createWriteStream } from "node:fs";

class LineSplitter extends Transform {
  constructor() {
    super({ readableObjectMode: true });
    this.tail = "";
  }
  _transform(chunk, _enc, cb) {
    const lines = (this.tail + chunk.toString("utf8")).split("\n");
    this.tail = lines.pop();
    for (const line of lines) {
      if (!line) continue;
      try {
        this.push(JSON.parse(line));
      } catch (err) {
        return cb(new Error(`Bad JSON: ${line.slice(0, 80)}`, { cause: err }));
      }
    }
    cb();
  }
  _flush(cb) {
    if (this.tail) {
      try {
        this.push(JSON.parse(this.tail));
      } catch (err) {
        return cb(err);
      }
    }
    cb();
  }
}

const toCsv = new Transform({
  writableObjectMode: true,
  transform(obj, _enc, cb) {
    cb(null, `${obj.id},${obj.total}\n`);
  },
});

const ac = new AbortController();
setTimeout(() => ac.abort(), 60_000).unref();

await pipeline(
  createReadStream("orders.ndjson"),
  new LineSplitter(),
  toCsv,
  createWriteStream("orders.csv"),
  { signal: ac.signal },
);
```

Key points: never call the callback twice; if `push()` returns `false`, Node handles backpressure because the callback is what tells it you're ready for the next chunk; decode strings carefully (a multibyte UTF-8 character can be split across chunks, so for real code use `StringDecoder` or `setEncoding('utf8')`); and pass an `AbortSignal` so a stuck pipeline can be cancelled.

#### 351: How do you share memory and coordinate between Node.js worker threads, and how do you limit their resources?

`SharedArrayBuffer` gives all threads access to the same memory. `Atomics` gives safe operations on it, plus `wait`/`notify` for blocking coordination (allowed in workers, and in Node also on the main thread, though blocking the main thread is usually a bad idea).

```js
// main.js
import { Worker } from "node:worker_threads";

const shared = new SharedArrayBuffer(Int32Array.BYTES_PER_ELEMENT * 2);
const state = new Int32Array(shared); // [0] = jobs done, [1] = signal

const worker = new Worker(new URL("./worker.js", import.meta.url), {
  workerData: { shared },
  resourceLimits: { maxOldGenerationSizeMb: 256, maxYoungGenerationSizeMb: 32 },
});
worker.on("error", (err) => console.error("worker failed", err));
worker.on("exit", (code) => console.log("worker exit", code));

// worker.js
import { workerData } from "node:worker_threads";
const state = new Int32Array(workerData.shared);
while (true) {
  Atomics.wait(state, 1, 0); // sleep until signal changes from 0
  doJob();
  Atomics.add(state, 0, 1);
  Atomics.store(state, 1, 0);
}
```

`resourceLimits` caps the worker's heap so a runaway job kills only that worker (with an `ERR_WORKER_OUT_OF_MEMORY` error) instead of the whole process. Keep in mind that each worker has its own V8 heap and code cache, so ten workers use roughly ten times the base memory. For most workloads, transferring `ArrayBuffer`s through `postMessage` is simpler and almost as fast. Use shared memory for high-frequency coordination or large data that many threads read.

#### 352: How does the `cluster` module distribute connections, and what problems does that cause for WebSockets?

On Linux and macOS, the primary process accepts connections and hands them to workers in round-robin order (`SCHED_RR`, the default except on Windows). The alternative, `SCHED_NONE`, lets workers accept directly from the shared socket, which tends to send most connections to a few busy workers because of how the OS wakes them.

Problems with WebSockets and long-lived connections:

- Round-robin balances **connections**, not load. A worker with a few very busy sockets gets the same share of new connections as one with idle sockets.
- Protocols that need **stickiness**, like Socket.IO's HTTP long-polling fallback, break when a client's requests go to different workers. You need sticky routing by IP or session (for example `@socket.io/sticky`), or only allow the WebSocket transport.
- Broadcasting to all clients needs cross-worker messaging (an adapter backed by Redis or the cluster IPC).
- When a worker restarts, all its connections drop at once and reconnect to other workers.

In containerized deployments the same issues show up at the load balancer level, so it's simpler to run one process per container and handle stickiness and fan-out there.

#### 353: How do you read `--trace-gc` output, and when would you tune `--max-semi-space-size`?

```bash
node --trace-gc server.js
[12345:0x...]   1201 ms: Scavenge 38.1 (52.3) -> 31.0 (52.3) MB, 1.8 / 0.0 ms  (average mu = 0.991, current mu = 0.982) allocation failure;
[12345:0x...]   5320 ms: Mark-Compact 210.4 (240.1) -> 140.2 (238.0) MB, 95.2 / 0.0 ms  (average mu = 0.912, current mu = 0.873) allocation failure; GC in old space requested
```

- `Scavenge` is a young-generation collection, `Mark-Compact` is a full old-generation collection (`Mark-Compact (reduce)` happens under memory pressure).
- `38.1 (52.3) -> 31.0 (52.3) MB` is heap used (heap committed) before and after.
- `1.8 / 0.0 ms` is the main-thread pause time / time spent in external callbacks.
- `mu` (mutator utilization) is the share of time JavaScript ran instead of GC. Values falling well below 0.9 mean GC is eating a lot of time.

Signals:

- Scavenges every few milliseconds with lots of memory surviving: the young generation is too small for the allocation rate, and objects are being promoted early. Raising `--max-semi-space-size` (for example to 32 or 64 MB) can reduce the number of scavenges and promotions, and often improves throughput for allocation-heavy servers at the cost of more memory.
- Frequent Mark-Compact with little freed: you are near the heap limit, so you have a leak or need a larger `--max-old-space-size`.
- Long Mark-Compact pauses: the old generation is very large. Splitting into more processes or reducing retained data helps.

Always measure throughput and p99 latency before and after tuning, with production-like traffic.

#### 354: Why can RSS keep growing in a Node.js process when the V8 heap is stable?

Memory outside the V8 heap is still counted in RSS:

- **Buffers and ArrayBuffers**: allocated outside the JS heap. Large or many buffers (file uploads, response bodies, image processing) raise RSS. Watch `process.memoryUsage().arrayBuffers` and `external`.
- **Native addons** (image libraries, database drivers, compression) that allocate with `malloc` and may leak.
- **Allocator fragmentation**: glibc's `malloc` creates per-thread arenas and doesn't always return freed memory to the OS. With many threads (libuv pool, workers), RSS can grow and stay high even after objects are freed. Setting `MALLOC_ARENA_MAX=2` or using jemalloc (via `LD_PRELOAD`) often helps.
- **Code space and JIT memory** growing with lots of dynamically generated code (for example, `new Function` or many unique regexes).
- **Thread stacks** for many worker threads.
- **TLS and zlib contexts** created per connection or request and not freed quickly.

```bash
MALLOC_ARENA_MAX=2 node server.js
# or
LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libjemalloc.so.2 node server.js
```

To investigate, compare `heapUsed`, `external` and RSS over time, look at `/proc/<pid>/smaps_rollup` or `pmap -x`, and test with a different allocator. If heap snapshots look clean but RSS climbs, the problem is almost always native memory.

#### 355: When is it worth moving CPU-heavy work to WebAssembly or a native addon in Node.js?

Consider it when profiling shows a hot, self-contained computation (image processing, compression, parsing a binary format, crypto, numeric simulation) that is already well optimized in JavaScript and still too slow.

- **WebAssembly**: portable, sandboxed, no build per platform. Good for code you can compile from Rust, C or C++. Often gives 1.5x to several times speedup for numeric code, though sometimes V8's JIT is close. Copying data in and out of Wasm memory can eat the gains for small inputs.
- **Native addons (Node-API)**: full native speed and access to system libraries and SIMD, and they can run work on libuv threads without blocking the event loop. The downsides are platform-specific builds (prebuilt binaries for each OS and CPU), harder debugging, crash risk, and memory that's harder to track.
- **Existing native libraries**: often the best option, like `sharp` for images or using `zlib`/`crypto` built into Node instead of a JS implementation.

Before going native: check the algorithm, avoid repeated allocations, use typed arrays, cache results, and move the work to a worker thread. Often that is enough. Whatever you choose, run CPU-heavy native work off the main thread too, or it still blocks the event loop.

#### 356: Which Node.js HTTP server settings matter for performance and resilience?

```js
import http from "node:http";

const server = http.createServer(app);
server.keepAliveTimeout = 65_000; // longer than the load balancer's idle timeout
server.headersTimeout = 66_000; // must be longer than keepAliveTimeout
server.requestTimeout = 30_000; // max time to receive the whole request (default 300 s)
server.maxRequestsPerSocket = 1000; // recycle connections so load spreads after scaling
server.maxHeadersCount = 100;
server.maxConnections = 10_000; // refuse beyond this instead of degrading
server.timeout = 0; // inactivity timeout on sockets (0 = disabled)
server.listen(3000);
```

- `requestTimeout` and `headersTimeout` protect against slow clients holding sockets (slowloris-style attacks).
- `keepAliveTimeout` must be longer than the proxy's idle timeout to avoid 502s.
- `maxRequestsPerSocket` closes a keep-alive connection after N requests, which helps rebalance traffic when new instances join behind an L4 load balancer.
- `maxConnections` and `--max-http-header-size` limit resource use per instance.
- For HTTP/2 (`node:http2`), also look at `maxSessionMemory`, `peerMaxConcurrentStreams` and settings like `initialWindowSize`.

Also set `server.on('clientError', ...)` to close bad sockets cleanly, and use `server.closeIdleConnections()` during shutdown.

#### 357: How do you implement load shedding in a Node.js service?

When a service is overloaded, accepting more requests makes everything slower until requests time out anyway. Load shedding rejects some requests early (with 503 and `Retry-After`) so the rest succeed quickly.

```js
import { monitorEventLoopDelay } from "node:perf_hooks";

const lag = monitorEventLoopDelay({ resolution: 10 });
lag.enable();

let inFlight = 0;
const MAX_IN_FLIGHT = 200;
const MAX_LAG_MS = 150;

setInterval(() => lag.reset(), 1000).unref();

app.use((req, res, next) => {
  const lagMs = lag.percentile(99) / 1e6;
  if (inFlight >= MAX_IN_FLIGHT || lagMs > MAX_LAG_MS) {
    res.setHeader("Retry-After", "2");
    return res.status(503).json({ error: "overloaded" });
  }
  inFlight++;
  res.on("close", () => inFlight--);
  next();
});
```

Refinements:

- Exempt health checks and high-priority routes, and shed low-priority traffic first (for example, background sync before checkout).
- Use a concurrency limit per dependency too, like a DB pool with a short acquire timeout.
- Make clients retry with exponential backoff and jitter, and add a retry budget so retries can't double the load.
- Fastify's `@fastify/under-pressure` plugin implements this pattern with event loop delay, heap and RSS thresholds.

#### 358: How do Deno and Bun differ from Node.js in ways that affect performance?

- **Engine**: Deno uses V8 like Node, so JavaScript execution speed is similar. Bun uses JavaScriptCore, which tends to start faster and has different JIT and GC behavior. Some workloads are faster, some slower, and memory use can differ.
- **HTTP servers**: `Deno.serve()` runs on a Rust HTTP stack (hyper), and `Bun.serve()` is implemented in native code (Zig). Both have lower per-request overhead than Node's `http` module in micro-benchmarks. Node frameworks like Fastify close much of the gap.
- **Built-in tooling**: Bun's package installs, test runner and bundler are very fast, which shortens CI and dev loops even if production stays on Node. Deno includes formatting, linting, testing and compiling to a single binary.
- **TypeScript**: both run it directly. Node 22.18+ and 24 also strip types natively by default, so this gap is mostly closed for type-only TS syntax.
- **Compatibility**: both implement most `node:` modules and npm packages, but native addons, some edge APIs and APM agents may not work or may behave differently. Profiling tools also differ: Deno supports `--inspect` with Chrome DevTools, and Bun has its own inspector (web-based) that also uses the WebKit protocol.
- **Startup time**: matters for serverless and CLIs. Bun is usually fastest here. Deno and Node have improved with snapshots and compile caches.

For a long-running API dominated by database time, the runtime choice rarely changes p99 latency much. Measure with your real app before switching.

#### 359: How do you reduce Node.js startup time?

Startup matters for serverless cold starts, CLIs, autoscaling speed and deploys.

- **Load less code**: audit what gets required at startup with `node --cpu-prof` on boot, or `NODE_DEBUG=module`. Big SDKs and barrel files often pull in hundreds of modules.
- **Lazy load** rarely used modules inside the function that needs them (`await import('heavy-lib')`).
- **Bundle the server** with esbuild or Rolldown into one file. This avoids thousands of file system lookups for `node_modules` resolution.
- **Enable the compile cache**: `module.enableCompileCache()` (Node 22.1+) or the `NODE_COMPILE_CACHE` environment variable stores V8 code cache on disk, which speeds up later starts.
- **Startup snapshots**: `node --build-snapshot entry.js` creates a snapshot blob with your initialized heap, which you start with `--snapshot-blob`. Useful for CLIs with heavy initialization.
- **Avoid synchronous work at startup** like reading big files, compiling many regexes, or connecting to every dependency in sequence. Connect in parallel.
- **Keep TypeScript compilation out of production**: run built JS, or use Node's built-in type stripping, not `ts-node` with full type checking.

```js
// at the top of the entry file
import module from "node:module";
module.enableCompileCache?.();
```

#### 360: How do you handle CPU-bound requests in a Node.js API without hurting other users?

Options, from simplest to most involved:

1. **Make the work cheaper**: better algorithm, caching results, precomputing at write time instead of read time.
2. **Chunk and yield**: split the work and yield with `setImmediate` between chunks. Total time grows a little but other requests keep flowing. Good for moderate work.
3. **Worker thread pool** (Piscina): run the work on other cores. Set `maxThreads` to the cores you can use and a `maxQueue` so overload turns into quick 503s.
4. **Separate service or job queue**: send the work to a queue (BullMQ on Redis, SQS, Kafka) and let dedicated workers process it, with the API returning `202 Accepted` and a status URL or a webhook. This isolates heavy work completely and lets you scale it separately.
5. **Move it to a better-suited runtime or native code** if profiling shows the JavaScript is the real limit.

Also protect the API: limit request sizes, rate limit expensive endpoints per user, and set timeouts so a slow job can't hold a connection forever.

---

### Advanced: Networking and Web Protocols (361-375)

#### 361: How does request prioritization work in HTTP/2 and HTTP/3, and what is RFC 9218?

HTTP/2 originally used a priority tree where clients described dependencies and weights between streams. It was complex, browsers used it differently, and many servers and CDNs implemented it badly or ignored it. RFC 9113 deprecated that scheme.

RFC 9218 (Extensible Priorities) replaced it with a simple model used by HTTP/3 and newer HTTP/2 stacks:

- `u` (urgency): 0 (highest) to 7 (lowest), default 3.
- `i` (incremental): whether the response can be sent interleaved with others of the same urgency (good for images) or should be sent in full before the next (good for scripts and CSS).

```http
Priority: u=0
Priority: u=5, i
```

The client sends it as a header or a `PRIORITY_UPDATE` frame, and the server can override it in its response. Chrome maps its internal priorities (Highest to Lowest) to these values, so `fetchpriority` changes what goes over the wire.

Why it matters: on a single multiplexed connection, the server decides which stream's bytes go next. If the server or CDN ignores priority, a large low-priority image can fill the connection while the critical CSS waits. Test with WebPageTest to see whether your CDN honors priorities. Server-side buffering (large TCP send buffers) also reduces how well priorities work, because data already queued in the kernel can't be reordered.

#### 362: How does HTTP/2 flow control work, and how can it limit throughput?

HTTP/2 has flow control per stream and per connection. Each receiver advertises a window (how many bytes it is willing to receive), and the sender can't send more until the receiver sends `WINDOW_UPDATE` frames. The default initial window is 65,535 bytes, which is small.

On high-latency links, a small window limits throughput to roughly `window / RTT`. With a 64 KB window and 100 ms RTT, that's about 640 KB/s per stream, no matter how much bandwidth exists. Browsers set much larger windows (Chrome uses several MB for the connection), but server-to-server HTTP/2 clients, gRPC and proxies may keep defaults and see slow large transfers.

```js
// Node.js HTTP/2 server with larger windows
import http2 from "node:http2";
const server = http2.createSecureServer({
  key,
  cert,
  settings: { initialWindowSize: 4 * 1024 * 1024 },
});
server.on("session", (session) => session.setLocalWindowSize(16 * 1024 * 1024));
```

When tuning, also check the TCP layer (receive buffer sizes and window scaling), because HTTP/2 windows can't go beyond what TCP allows. If large downloads between data centers are slow over HTTP/2 but fast over HTTP/1.1, flow control windows are a likely cause.

#### 363: Why might HTTP/3 sometimes be slower than HTTP/2, and how does congestion control affect both?

HTTP/3 often helps on lossy mobile networks and for connection setup, but it can be slower in some cases:

- **UDP handling**: some networks rate-limit or block UDP, so the browser tries QUIC, fails or gets poor throughput, and falls back. Chrome races QUIC and TCP connections to limit the damage, but there can still be a penalty.
- **CPU cost**: QUIC runs in user space and encrypts every packet itself, while TCP benefits from decades of kernel and NIC offloads. At very high throughput, QUIC can use noticeably more CPU on both servers and phones. Features like UDP GSO/GRO reduce this.
- **Discovery**: the first visit uses HTTP/2 and only learns about HTTP/3 from `Alt-Svc`, unless an HTTPS DNS record advertises it.
- **Implementation maturity** and congestion control choices on the server.

Congestion control decides how fast to send:

- **CUBIC** (Linux TCP default) is loss-based: it grows the window until packets drop. On networks with deep buffers it fills them, adding latency (bufferbloat), and on lossy wireless links it backs off too much.
- **BBR** models bandwidth and RTT and sends at the estimated bottleneck rate. It often gives better throughput and lower latency on long or lossy paths. Google and many CDNs use BBR for both TCP and QUIC.

Since QUIC's congestion control is in user space, CDNs can update it independently of the OS kernel.

#### 364: How have newer TLS features changed handshake size and latency?

- **Post-quantum key exchange**: Chrome (since version 131) offers `X25519MLKEM768`, a hybrid of classic X25519 and the ML-KEM post-quantum algorithm. Its key share is over 1 KB, so the ClientHello no longer fits in one packet. That's usually fine, but some old middleboxes or servers mishandle large or split ClientHellos, and on lossy networks an extra packet slightly raises the chance of a retransmit during the handshake.
- **Certificate compression** (RFC 8879): Chrome supports Brotli-compressed certificates. Servers that enable it send much smaller certificate chains, which helps keep the server's first flight inside the initial congestion window.
- **Encrypted Client Hello (ECH)**: hides the hostname. It needs an HTTPS DNS record with ECH config, which the browser must fetch before connecting. That adds DNS dependency but not extra round trips if DNS is fast.
- **Session resumption and 0-RTT**: cut handshake round trips for returning visitors, with replay risk for 0-RTT.
- **Shorter certificate lifetimes** don't affect handshake speed directly but push teams toward automated renewal.

Practical steps: keep certificate chains small (ECDSA, no extra intermediates), enable certificate compression where your server or CDN supports it, and test with real clients after enabling new key exchanges.

#### 365: Which Linux TCP settings affect web server performance?

```bash
# Use BBR with the fq queueing discipline
sysctl -w net.core.default_qdisc=fq
sysctl -w net.ipv4.tcp_congestion_control=bbr

# Don't reset the congestion window after a connection is idle
sysctl -w net.ipv4.tcp_slow_start_after_idle=0

# Larger accept queue and SYN backlog for bursts
sysctl -w net.core.somaxconn=8192
sysctl -w net.ipv4.tcp_max_syn_backlog=8192

# Bigger buffers for high bandwidth-delay paths (min, default, max)
sysctl -w net.ipv4.tcp_rmem="4096 131072 16777216"
sysctl -w net.ipv4.tcp_wmem="4096 65536 16777216"

# More ephemeral ports and reuse of TIME_WAIT for outgoing connections
sysctl -w net.ipv4.ip_local_port_range="10000 65000"
sysctl -w net.ipv4.tcp_tw_reuse=1

# TCP Fast Open for clients and servers that support it
sysctl -w net.ipv4.tcp_fastopen=3
```

- `tcp_slow_start_after_idle=0` matters for keep-alive connections: by default the window shrinks after an idle period, making the next response slower.
- `tcp_notsent_lowat` (for example 16 KB) keeps less unsent data in the kernel, which helps HTTP/2 prioritization react faster.
- Change one thing at a time and measure. Many defaults are fine on modern kernels, and managed environments (load balancers, CDNs) often terminate client TCP for you, so tuning matters most on the edge-facing hosts.

#### 366: What is bufferbloat, and how does it show up in web performance?

Bufferbloat is when routers, modems or OS queues have very large buffers. Under load (for example during a big upload or download), packets sit in those buffers for hundreds of milliseconds or even seconds before being sent. Throughput looks fine, but latency for everything else explodes. A user uploading a video while browsing sees pages take seconds to start loading because every DNS lookup and handshake waits in the queue.

How it shows up: RTT under load is far higher than idle RTT. Tools like the Waveform or Cloudflare speed tests report "loaded latency". On servers, deep send buffers with loss-based congestion control can do the same thing on the server side.

Mitigations: active queue management (`fq_codel`, CAKE) on routers, BBR and `fq` pacing on servers, `tcp_notsent_lowat` to keep send queues short, and on the client side avoiding many parallel large transfers at the same time as critical requests. HTTP/3's per-stream delivery doesn't fix bufferbloat, since all packets share the same bottleneck queue.

#### 367: How do Happy Eyeballs and IPv6 affect connection latency, including in Node.js?

When a hostname has both IPv6 (AAAA) and IPv4 (A) records, a client that tries IPv6 first may wait for a long timeout if IPv6 is broken somewhere on the path. Happy Eyeballs (RFC 8305) starts the IPv6 attempt, and if it hasn't connected within a short delay (around 250 ms or less), starts an IPv4 attempt in parallel and uses whichever connects first. Browsers have done this for years.

Node.js 20 turned on `autoSelectFamily` by default for `net.connect` (and so for HTTP clients), which implements Happy Eyeballs. Before that, a server with broken IPv6 could see each outbound connection hang until a timeout. If you see odd connection delays to some hosts:

```js
import net from "node:net";
console.log(net.getDefaultAutoSelectFamily()); // true by default since Node 20
net.setDefaultAutoSelectFamilyAttemptTimeout(250); // ms before trying the next address
```

Also check `dns.setDefaultResultOrder()` (`verbatim` is the default since Node 17, `ipv4first` changes it). In containers and Kubernetes, IPv6 is often partly configured, which makes this a common source of "first request is slow" problems.

#### 368: How do you invalidate CDN caches efficiently at scale?

- **Versioned URLs** for static assets (content hash in the file name) so you never need to invalidate them. Deploys create new URLs.
- **Surrogate keys / cache tags**: tag responses with keys like `product-42 category-lamps` in a header (`Surrogate-Key` on Fastly, `Cache-Tag` on Cloudflare Enterprise and some other CDNs). Then purge every page that includes product 42 with one API call, without knowing their URLs.
- **Soft purge** (Fastly) or "mark stale": mark content stale instead of deleting it, so the CDN can still serve it with `stale-while-revalidate` or `stale-if-error` while it fetches a fresh copy. This avoids a burst of origin traffic.
- **Short TTL plus revalidation** for content that changes often: `s-maxage=60, stale-while-revalidate=600` with ETags means the CDN checks cheaply instead of being purged.
- **Event-driven purges**: purge from your write path or from a change data capture stream, not by hand. Batch purges to stay within CDN API rate limits.
- **Avoid wildcard or full purges** on busy sites. They send all traffic to the origin at once.

CloudFront supports path-based invalidations (with wildcards) and charges after a free monthly quota, so for CloudFront versioned URLs and short TTLs are usually the main tools.

#### 369: What is Compression Dictionary Transport, and when does it help?

It lets a browser use a previously downloaded resource as a compression dictionary for a new one. Chrome supports it since version 130, with Brotli (`dcb`) and Zstandard (`dcz`) encodings.

How it works:

1. The server sends a resource with a header saying it can be used as a dictionary for matching URLs:

```http
Use-As-Dictionary: match="/js/app.*.js"
```

2. Later, when requesting a matching URL, the browser sends the hash of the dictionary it has:

```http
Accept-Encoding: gzip, br, zstd, dcb, dcz
Available-Dictionary: :pZGm1Av0IEBKARczz7exkNYsZb8LzaMrV7J32a2fFG4=:
```

3. The server returns the new file compressed against the old one:

```http
Content-Encoding: dcb
Vary: Accept-Encoding, Available-Dictionary
```

Since most of a new app bundle is the same as the previous version, the delta can be 90% or more smaller than normal Brotli. It helps most for frequently deployed JavaScript bundles and for HTML pages that share lots of markup (using a separate dictionary file the page links with `<link rel="compression-dictionary">`). The cost is build or server complexity (generating and storing deltas for recent versions) and cache key handling at the CDN, which must vary on `Available-Dictionary`. Dictionaries are also partitioned like the HTTP cache and only work over HTTPS and same-origin (or CORS) responses.

#### 370: How does streaming HTML (early flush) improve performance, and what can break it?

Instead of waiting for all the data before sending anything, the server sends the `<head>` (with CSS, preloads and preconnects) immediately, then streams the body as data becomes available. The browser starts fetching critical resources and rendering while the server is still working, which improves FCP and LCP when the backend is slow.

```js
app.get("/product/:id", async (req, res) => {
  res.setHeader("Content-Type", "text/html; charset=utf-8");
  res.write(`<!doctype html><html><head>
    <link rel="stylesheet" href="/css/app.css">
    <link rel="preload" href="/js/app.js" as="script">
  </head><body><header>...</header>`);

  const product = await getProduct(req.params.id); // slow part
  res.write(renderProduct(product));
  res.end("</body></html>");
});
```

Frameworks do this with streaming SSR (`renderToPipeableStream` in React, streaming in Next.js, Nuxt, SvelteKit, Remix and others).

Things that break it:

- **Proxy buffering**: Nginx's `proxy_buffering on` collects the response first. Use `X-Accel-Buffering: no` for streamed pages, or `proxy_buffering off`.
- **Compression middleware** that buffers until a size threshold. Make sure it flushes per chunk (for example, `res.flush()` with the `compression` package).
- **CDNs or serverless platforms** that don't support streaming responses on your plan or configuration.
- **Status code and headers**: once you start streaming, you can't change the status code (for example, to 404 or a redirect) if something fails later. Handle errors in the stream, or fetch data needed for the status before flushing.
- **Very small first chunks** that don't reach the browser until more data arrives because of buffering in the network stack (Nagle's algorithm is disabled by default in Node, so this is mostly about proxies).

#### 371: What are WebSockets over HTTP/2 and WebTransport, and why might you use them?

- **WebSockets over HTTP/2** (RFC 8441): a WebSocket is opened as a stream on an existing HTTP/2 connection using an extended `CONNECT`, instead of a separate TCP connection with an HTTP/1.1 upgrade. Several WebSockets and normal requests share one connection, which saves handshakes and file descriptors. Chrome supports it, but servers and proxies must support it too. RFC 9220 does the same for HTTP/3.
- **WebTransport** (over HTTP/3): an API for low-latency, two-way communication with multiple independent streams (no head-of-line blocking between them), unreliable datagrams (like UDP, for game state or live media where old data is useless), and backpressure through the Streams API. It is supported in Chromium and Firefox and recently in Safari.

```js
const wt = new WebTransport("https://game.example.com:4433/session");
await wt.ready;
const writer = wt.datagrams.writable.getWriter();
setInterval(() => writer.write(encodePlayerPosition()), 50); // lost packets are fine

const stream = await wt.createBidirectionalStream(); // reliable channel for chat
```

Use WebSockets for typical chat and notifications since they work everywhere. Consider WebTransport for real-time games, live video or sensor data where old data should be dropped instead of delaying new data.

#### 372: How does head-of-line blocking show up at different layers, and how should it change your protocol choices?

- **HTTP/1.1 application layer**: one response at a time per connection, so a slow response blocks the next. Browsers work around it with 6 parallel connections.
- **HTTP/2**: fixes the application-level problem with multiplexing, but all streams share one TCP byte stream. A single lost packet holds back data for every stream until it is retransmitted. On networks with 1 to 2% loss, HTTP/2 can be slower than HTTP/1.1 with 6 connections, because 6 TCP connections lose and recover independently and each starts with its own congestion window.
- **TLS records**: data is decrypted per record (up to 16 KB). If part of a record is lost, the whole record waits. Dynamic record sizing (small records at the start of a connection) helps.
- **HTTP/3 / QUIC**: each stream is delivered independently, so loss only stalls the affected stream. Packets are encrypted individually.
- **Application protocols on top**: a single WebSocket, or a single gRPC stream carrying many logical messages, has its own head-of-line blocking regardless of transport.

Practical effects: enable HTTP/3 for mobile-heavy audiences, avoid funneling unrelated real-time messages through one ordered channel when ordering isn't needed, and keep critical resources small so they finish quickly even when the connection is shared.

#### 373: What are the pitfalls of ETags in multi-server and CDN setups?

- **Inconsistent ETags across servers**: some servers build ETags from file metadata such as inode, size and modification time. Behind a load balancer, each server may produce a different ETag for the same file, so revalidation alternates between 200 and 304 and caching barely works. Use content hashes or a version from your build or database instead.
- **Weak vs strong ETags**: `W/"abc"` means "semantically equal". Weak ETags are fine for `If-None-Match` on GET, but range requests need strong ETags. Some CDNs or proxies turn strong ETags into weak ones when they compress the response, or drop ETags entirely.
- **Compression variants**: the gzip and Brotli versions of a resource are different bytes. A strong ETag should differ per encoding, or the cache might mix them up.
- **CDN revalidation**: when the CDN copy expires, the CDN sends a conditional request to the origin. If ETags or `Last-Modified` are missing, every revalidation transfers the whole file.
- **Expensive ETag generation**: hashing a large dynamically generated body on every request means you do all the work even for 304s. Use version numbers or `updated_at` to decide before rendering.
- **Deploy timing**: if new and old app servers run side by side during a rolling deploy, they may produce different ETags for the same content.

#### 374: How do you cache HTML at the CDN while keeping browser caching safe?

You often want the CDN to cache HTML for a while (and purge it on changes) but want browsers to always revalidate, so users see updates quickly. Use separate directives for shared caches:

```http
Cache-Control: public, max-age=0, must-revalidate
CDN-Cache-Control: max-age=300, stale-while-revalidate=600
```

- `Cache-Control: max-age=0` (or `no-cache`) makes the browser revalidate each time, which is cheap with ETags.
- `s-maxage` in `Cache-Control` applies to all shared caches, including any proxies between the CDN and the user.
- `CDN-Cache-Control` (RFC 9213) applies only to CDNs that support it (Cloudflare and others), and many CDNs also support their own headers like `Surrogate-Control` (Fastly) or ignore it in favor of configured policies (CloudFront uses cache policies).

Rules to follow:

- Never cache personalized HTML in a shared cache. Strip or bypass on session cookies, or make the HTML generic and load user-specific parts with a separate request.
- Remove `Set-Cookie` from cacheable responses; most CDNs won't cache them anyway.
- Use surrogate keys or purge on publish, and `stale-if-error` to survive origin outages.

#### 375: Why do long-lived HTTP/2 or gRPC connections cause uneven load, and how do you fix it?

With HTTP/1.1, each request may open or reuse one of many connections, so an L4 load balancer spreads requests fairly well. With HTTP/2 and gRPC, a client opens one connection and sends all requests over it for hours. An L4 (TCP) load balancer balances connections, not requests, so:

- New instances added during scale-out get no traffic until clients reconnect.
- A client with heavy traffic pins all its load on one backend.
- After a deploy, the first instances to come up collect most connections.

Fixes:

- **Use an L7 load balancer** that understands HTTP/2 and balances individual requests (streams) across backends: AWS ALB with HTTP/2 or gRPC target groups, Envoy, Linkerd or Istio sidecars, Nginx with `grpc_pass`.
- **Client-side load balancing**: gRPC clients can resolve all backend addresses (for example via a headless Kubernetes Service) and use `round_robin` across them.
- **Connection max age**: servers close connections gracefully after some time (gRPC's `MAX_CONNECTION_AGE`, or `server.maxRequestsPerSocket` in Node for HTTP/1.1), forcing clients to reconnect and rebalance.
- **Headless services or service mesh** in Kubernetes, since a normal ClusterIP Service only balances at connection time.

---

### Advanced: Databases and Data Access (376-390)

#### 376: How does PostgreSQL choose between nested loop, hash and merge joins, and how does `work_mem` affect them?

- **Nested loop**: for each row from the outer side, look up matching rows on the inner side. Very fast when the outer side is small and the inner side has an index on the join key. Terrible when both sides are large and there's no index.
- **Hash join**: build a hash table from the smaller side, then scan the larger side and probe it. Good for large unsorted inputs with equality joins. The hash table must fit in `work_mem`, or it splits into batches written to disk (`Batches: 8` in the plan instead of `Batches: 1`).
- **Merge join**: both sides sorted on the join key (from an index or an explicit sort), then merged. Good for large inputs already sorted, and for some range conditions.

`work_mem` is the memory each sort or hash operation may use before spilling to disk. It applies per operation, per query, per parallel worker, so a complex query can use several times `work_mem`. Spills show up in `EXPLAIN ANALYZE` as `Sort Method: external merge  Disk: 120000kB` or `Batches > 1`.

```sql
SET work_mem = '64MB';   -- for this session only, for a heavy report
EXPLAIN (ANALYZE, BUFFERS) SELECT ...;
```

Raise `work_mem` per session or per role for reporting queries instead of globally, since a high global value multiplied by many connections can exhaust RAM. A bad join choice is usually caused by wrong row estimates, so fix statistics before forcing plans.

#### 377: Why does PostgreSQL misestimate rows for queries filtering on correlated columns, and how do extended statistics help?

By default, the planner assumes columns are independent. For `WHERE city = 'Tbilisi' AND country = 'GE'`, it multiplies the selectivity of each condition. But city fully determines country, so the real selectivity is just that of the city. The planner underestimates rows by a big factor, and may then pick a nested loop that runs millions of times.

Extended statistics teach it about relationships between columns:

```sql
CREATE STATISTICS addr_stats (dependencies, ndistinct, mcv)
  ON city, country FROM addresses;
ANALYZE addresses;
```

- `dependencies`: functional dependencies between columns.
- `ndistinct`: number of distinct combinations, which helps `GROUP BY` estimates.
- `mcv`: most common combinations of values, which helps with skewed data.

Other estimate fixes: raise the per-column statistics target for skewed columns (`ALTER TABLE ... ALTER COLUMN ... SET STATISTICS 1000`), run `ANALYZE` after bulk loads, and avoid hiding columns inside functions or casts that the planner can't estimate. Check by comparing estimated and actual rows in `EXPLAIN ANALYZE`.

#### 378: How do you diagnose and fix table bloat and autovacuum problems in PostgreSQL?

Signs: tables and indexes much larger than their live data, sequential scans getting slower over time, high `n_dead_tup`, and autovacuum running constantly on a few tables or never finishing.

```sql
SELECT relname, n_live_tup, n_dead_tup, last_autovacuum, autovacuum_count
FROM pg_stat_user_tables ORDER BY n_dead_tup DESC LIMIT 10;
```

The `pgstattuple` extension gives exact bloat figures. Common causes:

- **Long-running transactions** or idle-in-transaction sessions, abandoned replication slots, or old prepared transactions. VACUUM can't remove rows that any open snapshot might still see.
- **Autovacuum thresholds too high for big tables**: the default `autovacuum_vacuum_scale_factor = 0.2` means a 100-million-row table waits for 20 million dead rows.
- **Autovacuum throttled** by cost limits on fast storage.
- **Update-heavy tables** without HOT updates (an update that changes an indexed column can't use HOT and creates new index entries too).

Fixes:

```sql
ALTER TABLE orders SET (
  autovacuum_vacuum_scale_factor = 0.01,
  autovacuum_vacuum_cost_limit = 2000
);
ALTER TABLE orders SET (fillfactor = 85);  -- leave room for HOT updates
```

Kill idle-in-transaction sessions with `idle_in_transaction_session_timeout`. To reclaim space without long locks, use `pg_repack` instead of `VACUUM FULL`. Also watch transaction ID age (`age(datfrozenxid)`): if vacuum falls too far behind, PostgreSQL forces aggressive anti-wraparound vacuums and eventually stops accepting writes to protect data.

#### 379: How do you find and fix lock contention in PostgreSQL?

Find who is waiting on whom:

```sql
SELECT pid, wait_event_type, wait_event, state,
       pg_blocking_pids(pid) AS blocked_by,
       now() - query_start AS running_for,
       left(query, 80) AS query
FROM pg_stat_activity
WHERE wait_event_type = 'Lock' OR cardinality(pg_blocking_pids(pid)) > 0;
```

Common causes:

- **Hot rows**: many transactions updating the same row (counters, inventory, a "last updated" field on a parent row). Use atomic increments in short transactions, batch updates, or move counters to Redis and sync later.
- **Long transactions** holding row locks while doing slow work such as calling an external API. Do external calls outside the transaction.
- **DDL** like `ALTER TABLE` needing an `ACCESS EXCLUSIVE` lock. It waits behind running queries, and every new query then waits behind it, so the table freezes. Always set `lock_timeout` for migrations and retry.
- **Foreign key checks** that lock parent rows (`FOR KEY SHARE`), causing contention on popular parents.
- **`SELECT ... FOR UPDATE`** on more rows than needed. For queue tables, use `FOR UPDATE SKIP LOCKED`.

```sql
SET lock_timeout = '3s';
ALTER TABLE orders ADD COLUMN note text;

-- job queue
SELECT id FROM jobs WHERE status = 'ready'
ORDER BY id LIMIT 10 FOR UPDATE SKIP LOCKED;
```

Turn on `log_lock_waits = on` so waits longer than `deadlock_timeout` (1 s by default) are logged with details.

#### 380: How do prepared statements and plan caching work in PostgreSQL, and when do they hurt?

When a statement is prepared (explicitly, or by drivers that use the extended protocol with named statements), PostgreSQL can reuse its plan. For the first five executions it builds a **custom plan** using the actual parameter values. After that, it compares the average cost of the custom plans with a **generic plan** (built without knowing the values) and switches to the generic plan if it isn't much worse.

That's a problem with skewed data. For `WHERE status = $1`, `status = 'archived'` might match 95% of rows (sequential scan is best) and `status = 'failed'` matches 0.01% (index scan is best). A generic plan chosen during the first calls may be terrible for the other values. Symptoms: a query that is fast in `psql` with literal values but slow from the application.

Fixes:

```sql
SET plan_cache_mode = force_custom_plan;  -- per session or per role
```

Other options: use different queries for very different cases, use partial indexes, or avoid server-side prepared statements for that query. Check with `EXPLAIN (ANALYZE) EXECUTE stmt('failed')` and look for `$1` in the plan, which indicates a generic plan. With PgBouncer in transaction mode, make sure protocol-level prepared statements are handled (`max_prepared_statements` in PgBouncer 1.21+), or drivers will fail or re-prepare constantly.

#### 381: When would you use GIN, GiST, BRIN or hash indexes instead of B-tree?

- **B-tree** (default): equality, ranges, sorting, prefix `LIKE 'abc%'` (with the right collation or `text_pattern_ops`). Covers most cases.
- **GIN**: for values containing many elements, like `jsonb` (`@>`, `?`), arrays (`@>`, `&&`), full-text search (`tsvector`), and trigram search with `pg_trgm` (`LIKE '%term%'`, similarity). Fast reads, slower writes (it uses a pending list that `fastupdate` flushes later).
- **GiST**: geometric and range data, nearest-neighbor searches (`ORDER BY location <-> point`), PostGIS, exclusion constraints (no overlapping bookings), and also trigram search (smaller but slower than GIN).
- **BRIN**: very small index that stores min/max per block range. Great for huge append-only tables where the column is correlated with physical order, like `created_at` on an events table. Not useful if data is randomly ordered.
- **Hash**: equality only. Can be slightly smaller and faster than B-tree for long keys, but B-tree is usually good enough.

```sql
CREATE INDEX idx_products_attrs ON products USING gin (attributes jsonb_path_ops);
CREATE INDEX idx_users_name_trgm ON users USING gin (name gin_trgm_ops);
CREATE INDEX idx_events_created_brin ON events USING brin (created_at);
```

For vector similarity search, extensions like pgvector add HNSW and IVFFlat indexes.

#### 382: How does table partitioning help performance in PostgreSQL, and what are its traps?

Declarative partitioning splits a table into child tables by range, list or hash, for example monthly partitions of an events table.

Benefits:

- **Partition pruning**: queries filtering on the partition key only scan matching partitions, at planning and at execution time.
- **Cheap data retention**: `DROP TABLE events_2025_01` or `DETACH PARTITION` instead of a huge `DELETE` that creates bloat.
- **Smaller indexes per partition** and vacuum working on smaller tables.
- **Different storage** for hot and cold partitions.

```sql
CREATE TABLE events (id bigint, created_at timestamptz NOT NULL, payload jsonb)
  PARTITION BY RANGE (created_at);
CREATE TABLE events_2026_10 PARTITION OF events
  FOR VALUES FROM ('2026-10-01') TO ('2026-11-01');
```

Traps:

- Queries that don't filter on the partition key scan every partition, which can be slower than one table.
- Too many partitions (thousands) increase planning time and memory.
- Unique constraints and primary keys must include the partition key.
- You need automation to create future partitions (pg_partman or a scheduled job), or inserts fail.
- Partitioning doesn't replace indexes. It mainly helps with large time-based data and retention.

#### 383: How do read replicas help performance, and how do you handle replication lag?

Replicas take read traffic off the primary, so writes and important reads get more capacity. Replication is usually asynchronous, so replicas can lag behind the primary by milliseconds, or seconds to minutes under heavy writes or long queries on the replica.

Problems from lag: a user updates their profile, the next request reads from a replica and shows old data ("read-your-writes" violation), or a job reads a row that doesn't exist yet on the replica.

Strategies:

- **Route reads after writes to the primary**: for a few seconds after a user writes, send that user's reads to the primary (track with a cookie or session timestamp).
- **LSN-based consistency**: after a write, record the primary's WAL position (`pg_current_wal_lsn()`) and only read from replicas that have replayed past it (`pg_last_wal_replay_lsn()`).
- **Send critical reads to the primary** (checkout, payments) and only use replicas for lag-tolerant reads (listings, reports).
- **Monitor lag** (`pg_stat_replication` on the primary, `ReplicaLag` in CloudWatch for RDS) and remove lagging replicas from the read pool automatically.

Long queries on replicas can also conflict with replication (`canceling statement due to conflict with recovery`). `hot_standby_feedback` prevents that but can cause bloat on the primary.

#### 384: What determines MongoDB performance at scale, and how do you choose a shard key?

- **Working set in cache**: WiredTiger's cache defaults to 50% of (RAM − 1 GB) or 256 MB, whichever is larger. When frequently used indexes and documents don't fit, reads go to disk and latency jumps. Watch cache dirty and used ratios and pages read into cache in `db.serverStatus().wiredTiger.cache`.
- **Index selectivity and size**: every index must also fit in memory to be fast. Remove unused indexes (`$indexStats`).
- **Document size and growth**: large documents and unbounded arrays cost on every read and update.
- **Write concern and journaling**: `w: "majority"` waits for replication, adding latency but giving durability.

For sharding, a good shard key has:

- **High cardinality**: many distinct values so data can be split into many chunks.
- **Even write distribution**: avoid monotonically increasing keys like timestamps or ObjectIds alone, which send all inserts to the last chunk (a hot shard). Use hashed keys or compound keys.
- **Query isolation**: most queries should include the shard key so they go to one shard (targeted) instead of all shards (scatter-gather).

```js
sh.shardCollection("shop.orders", { customerId: 1, createdAt: 1 });
// or for even writes without range queries:
sh.shardCollection("logs.events", { deviceId: "hashed" });
```

Since MongoDB 5.0 you can reshard a collection, but it is expensive, so choose carefully up front.

#### 385: How do you investigate a MongoDB query that picks a bad plan?

MongoDB's planner runs candidate plans in a short trial, picks the one that produces results fastest, and caches that choice for the query shape. A plan that won for one set of values may be bad for another.

```js
const exp = db.orders
  .find({ status: "pending", customerId: 42 })
  .sort({ createdAt: -1 })
  .explain("allPlansExecution");

exp.queryPlanner.winningPlan; // which index was used
exp.queryPlanner.rejectedPlans; // alternatives
exp.executionStats; // totalKeysExamined, totalDocsExamined, nReturned, executionTimeMillis
```

Look for:

- `totalKeysExamined` and `totalDocsExamined` much larger than `nReturned`.
- An in-memory `SORT` stage.
- `FETCH` after `IXSCAN` with a filter that removes most documents, which means the index isn't selective enough for this query.

Fixes:

- Create a better index for the shape (following ESR).
- Remove redundant indexes that confuse the planner.
- Clear the plan cache for the collection (`db.orders.getPlanCache().clear()`) to check if a cached plan is the issue.
- As a last resort, `hint()` the index, or use an index filter / `setQuerySettings` (MongoDB 8.0) to pin it without changing app code.

Use the profiler (`db.setProfilingLevel(1, { slowms: 100 })`) or Atlas Query Insights to find slow shapes in the first place.

#### 386: Why can Redis latency spike, and how do you diagnose it?

Redis runs commands on a single main thread (I/O threads can help with network reads and writes, but commands still run one at a time). Anything slow blocks everyone.

Common causes:

- **O(N) commands on big keys**: `KEYS *`, `SMEMBERS` or `HGETALL` on huge sets and hashes, `LRANGE 0 -1` on long lists, `DEL` on a big key, `SORT`. Use `SCAN`, `HSCAN`, paging, and `UNLINK`.
- **Lua scripts or functions** that run long. Nothing else runs meanwhile.
- **Fork for persistence**: `BGSAVE` and AOF rewrite fork the process. With a large dataset, the fork itself can take hundreds of milliseconds, especially with transparent huge pages enabled. Check `latest_fork_usec` in `INFO`.
- **AOF `fsync`** with `appendfsync always`, or slow disks with `everysec`.
- **Swapping** or memory pressure on the host.
- **Many clients doing round trips** for single commands. Use pipelining or `MGET`/`MSET`.
- **Expiry storms**: many keys expiring at the same moment.

Tools:

```bash
redis-cli --latency -h host           # live latency samples
redis-cli SLOWLOG GET 20              # commands slower than slowlog-log-slower-than (default 10 ms)
redis-cli LATENCY DOCTOR              # needs latency-monitor-threshold set
redis-cli --bigkeys                   # find large keys
redis-cli INFO stats | grep -E 'instantaneous_ops|rejected|expired|evicted'
```

Also measure latency from the client side, since network problems and connection pool waits in your app look like Redis latency too.

#### 387: What race conditions can happen with cache invalidation, and how do you avoid serving stale data?

The classic cache-aside race:

1. Reader A misses the cache and reads value **v1** from the database.
2. Writer B updates the database to **v2** and deletes the cache key.
3. Reader A, delayed, writes **v1** into the cache.

Now the cache holds stale data until the TTL expires. Other issues: a delete that fails after the database write succeeds, and replicas returning old data to a reader right after the invalidation.

Ways to reduce the risk:

- **Always use a TTL**, so stale data has a maximum lifetime.
- **Versioned values**: store a version or `updated_at` with the cached value and only write if it is newer (a Lua script or `WATCH`/`MULTI` that compares versions).
- **Delayed double delete**: delete on write, then delete again after a short delay (longer than a typical read) to remove any stale value written in between.
- **Lease tokens** (as in Facebook's memcache paper): a miss gets a token, and a cache fill is only accepted if no invalidation happened since the token was issued.
- **Invalidate from the database's change stream** (CDC with Debezium, PostgreSQL logical replication or MongoDB change streams), so invalidations are tied to committed changes and retried if they fail.
- **Write-through** for some data: update the cache in the same code path as the database, with care around failures.
- **Read from the primary** when filling the cache right after writes, to avoid filling with replica-lagged data.

Decide per type of data how much staleness is acceptable. Prices and stock need tighter control than avatars.

#### 388: How do you find and fix ORM overhead in a production Node.js app?

1. **Look at the queries**: enable query logging in staging (`log: ['query']` in Prisma, `logging: true` in TypeORM/Sequelize), or look at database spans in APM. Count queries per request. A request making 300 queries is an N+1.
2. **Fix N+1 with eager loading or batching**: `include`/`relations` with a join or a second `IN` query. In Prisma, `relationLoadStrategy: 'join'` loads relations in one SQL query with joins, while `'query'` uses separate queries per relation. Choose based on data shape and measure.
3. **Select only needed fields**: `select: { id: true, name: true }` instead of full models, especially for wide tables or JSON columns.
4. **Avoid hydration for large reads**: for reports or exports, use raw queries or a lighter query builder and stream rows, instead of building thousands of full entity objects with change tracking.
5. **Batch writes**: `createMany`, bulk inserts or `INSERT ... ON CONFLICT` instead of saving entities one by one in a loop.
6. **Check generated SQL** with `EXPLAIN`: ORMs can generate `OFFSET` pagination, `IN` lists with thousands of values, or `LOWER()` wrappers that skip indexes.
7. **Watch connection usage**: ORM transactions that stay open across `await`s of external calls hold pool connections.

```js
// Prisma: one query with only the fields the page needs
const posts = await prisma.post.findMany({
  where: { published: true },
  select: { id: true, title: true, author: { select: { name: true } } },
  orderBy: { id: "desc" },
  take: 20,
  relationLoadStrategy: "join",
});
```

#### 389: How can a connection pool deadlock itself, and how do you detect pool exhaustion?

A pool deadlock happens when code holding a connection waits for another connection from the same pool. If enough requests do this at the same time, every connection is held by a request waiting for another one, and nothing moves.

```js
// Dangerous: holds one connection, then asks for another
await db.transaction(async (tx) => {
  await tx.query("UPDATE accounts SET ...");
  await auditLog.write(entry); // uses pool.query() internally, a second connection
});
```

With a pool of 10 and 10 concurrent requests, all 10 hold a transaction connection and wait forever for an audit connection.

Fixes: pass the transaction client to everything inside the transaction, keep transactions short, never do external calls or other pool requests inside them, and set an acquire timeout so the problem turns into errors instead of a hang.

Detecting exhaustion:

- Track pool metrics: total, idle and waiting clients (`pool.totalCount`, `pool.idleCount`, `pool.waitingCount` in `pg`), and time spent waiting to acquire.
- Alert when `waitingCount` stays above zero or acquire time rises.
- On the database, look at connections in `idle in transaction` state in `pg_stat_activity`, which often means app code is holding transactions open while doing something else.

```js
const pool = new pg.Pool({
  max: 10,
  connectionTimeoutMillis: 2000,
  idleTimeoutMillis: 30000,
});
setInterval(
  () => metrics.gauge("db_pool_waiting", pool.waitingCount),
  5000,
).unref();
```

#### 390: How do you implement keyset pagination with multiple sort columns, and how do you show total counts cheaply?

When sorting by a non-unique column, add a unique tie-breaker (like `id`) and compare both together. PostgreSQL supports row value comparison, which can use a composite index:

```sql
CREATE INDEX idx_posts_created_id ON posts (created_at DESC, id DESC);

-- first page
SELECT id, title, created_at FROM posts
ORDER BY created_at DESC, id DESC
LIMIT 20;

-- next page: pass the last row's (created_at, id)
SELECT id, title, created_at FROM posts
WHERE (created_at, id) < ($1, $2)
ORDER BY created_at DESC, id DESC
LIMIT 20;
```

Encode the cursor as an opaque string (base64 of the values) so clients don't depend on its format. For mixed sort directions (one column ascending, one descending), row comparison doesn't work directly. Write the expanded condition `(a > $1) OR (a = $1 AND b < $2)` and make sure the index matches.

For total counts, `SELECT count(*)` on a large filtered table can be slower than the page query itself. Options:

- Don't show exact totals. Show "more results" or "1,000+".
- Use the planner's estimate (`EXPLAIN` output's row count, or `reltuples` from `pg_class` for whole tables).
- Cache the count and refresh it periodically.
- Keep a counter table updated by triggers or events for common filters.

---

### Advanced: Operating Systems and Server Resources (391-405)

#### 391: A service has high latency but its CPU flame graph shows nothing unusual. What do you do next?

A normal (on-CPU) flame graph only shows time when threads are running. If requests are slow because threads are **waiting**, that time doesn't appear. Look at off-CPU time:

- **Off-CPU analysis**: tools like `offcputime` from BCC/bpftrace record stack traces when threads block and how long they were blocked. The result shows waits on locks, disk I/O, network reads, sleeps, and page faults.

```bash
sudo offcputime-bpfcc -df -p $(pgrep -f server.js) 30 > off.stacks
./flamegraph.pl --color=io --title="Off-CPU" < off.stacks > offcpu.svg
```

- **For Node specifically**: an idle event loop with slow requests means the time is in waits: DB queries, HTTP calls, the libuv thread pool queue, connection pool queues, or timers. Distributed traces and async spans show which.
- **Run queue latency**: threads may be ready but waiting for a CPU (`runqlat-bpfcc`), which happens with CPU throttling or noisy neighbors. The on-CPU flame graph doesn't show this either.
- **Check the system level**: PSI (`/proc/pressure/cpu`, `io`, `memory`), CFS throttling in `cpu.stat`, and steal time in `vmstat`.

The usual lesson: latency = time on CPU + time waiting. Profile both.

#### 392: Which eBPF tools are most useful for debugging server performance, and what do they show?

From the BCC tools (often named `*-bpfcc` on Ubuntu) and bpftrace:

- `runqlat`: histogram of how long runnable threads waited for a CPU. High values mean CPU saturation or throttling.
- `biolatency`: histogram of block I/O latency. Shows if the disk is slow, with outliers.
- `biosnoop`: each disk I/O with the process, size and latency.
- `tcpretrans`: TCP retransmits with addresses, pointing to packet loss on specific paths.
- `tcplife`: each TCP connection's duration and bytes, useful for finding short-lived connection churn.
- `tcpconnlat`: how long outbound TCP connects take.
- `execsnoop`: new processes started. Finds scripts or health checks forking constantly.
- `opensnoop`: files being opened, for example config files read on every request.
- `offcputime` and `profile`: off-CPU and on-CPU stack sampling.
- `cachestat`: page cache hit ratio.
- `gethostlatency`: DNS lookup latency from libc calls.

```bash
sudo runqlat-bpfcc 10 1
sudo tcpretrans-bpfcc
sudo bpftrace -e 'tracepoint:syscalls:sys_enter_openat /comm == "node"/ { @[str(args->filename)] = count(); }'
```

They have low overhead and are safe for short use in production. In containers, they usually need to run on the host or in a privileged debug container.

#### 393: How do you get accurate `perf` profiles of Node.js, including inside containers?

- Start Node with `--perf-basic-prof` (or `--perf-basic-prof-only-functions` for smaller maps) so V8 writes `/tmp/perf-<pid>.map` with names for JIT-compiled code.
- Add `--interpreted-frames-native-stack` so functions still in the interpreter show up by name instead of as generic interpreter frames.
- Make sure frame pointers or stack unwinding work. V8 keeps frame pointers for JS. For native code and libraries, `perf record -g` with frame pointers works if they were compiled with them; otherwise use `--call-graph dwarf`, which costs more.

```bash
node --perf-basic-prof --interpreted-frames-native-stack server.js &
sudo perf record -F 99 -g -p $! -- sleep 30
sudo perf script | ./stackcollapse-perf.pl | ./flamegraph.pl > node.svg
```

In containers:

- `perf` needs `CAP_PERFMON` or `CAP_SYS_ADMIN`, and the host's `kernel.perf_event_paranoid` setting must allow it.
- The process ID inside the container differs from the host PID. When running `perf` from the host, the map file must be visible at `/tmp/perf-<host-pid>.map`. Copy or symlink it from the container's filesystem (`/proc/<pid>/root/tmp/...`), or run `perf` inside the container with the right capabilities.
- Symbols for system libraries in the container image must be resolvable from where `perf report` runs.

Continuous profilers that use eBPF (Parca, Pyroscope's eBPF agent, Grafana Alloy) handle much of this automatically.

#### 394: What are page faults and transparent huge pages, and how can they affect Node.js, Redis or databases?

A **page fault** happens when a process touches memory that isn't mapped in its page tables yet. A **minor fault** is resolved without disk I/O (for example, the first touch of newly allocated memory). A **major fault** needs to read from disk (swap or a memory-mapped file) and is much slower. Many major faults mean memory pressure or swapping.

```bash
pidstat -r -p <pid> 1    # minflt/s and majflt/s
```

**Transparent huge pages (THP)** let the kernel use 2 MB pages instead of 4 KB pages automatically, which reduces TLB misses for large heaps. The downsides: background compaction (`khugepaged`) can cause latency spikes, memory use can grow because whole 2 MB pages are allocated, and copy-on-write after `fork()` copies 2 MB at a time.

- **Redis** recommends disabling THP because its `fork()` for persistence becomes slow with huge pages, and copy-on-write uses much more memory.
- **PostgreSQL** prefers explicit huge pages (`huge_pages = try` with configured `vm.nr_hugepages`) for shared buffers, and THP disabled or set to `madvise`.
- **MongoDB** changed its advice: from 8.0 it recommends enabling THP (with its updated TCMalloc), while older versions recommended disabling it. Follow the guidance for your version.
- **Node.js** usually works fine with the `madvise` setting, which is a sensible default on most systems.

```bash
cat /sys/kernel/mm/transparent_hugepage/enabled   # [always] madvise never
```

#### 395: How does cgroup v2 memory accounting work, and what is the difference between `memory.high` and `memory.max`?

In cgroup v2, a container's memory usage includes anonymous memory (heap, stacks), page cache from files it reads and writes, kernel memory like socket buffers, and tmpfs files. This surprises people: a container that writes large log files or reads big files can approach its limit because of page cache, even with a small heap. Reclaimable page cache is freed under pressure, but dirty pages must be written first.

- **`memory.max`**: the hard limit. If usage reaches it and the kernel can't reclaim enough, the OOM killer runs inside the cgroup.
- **`memory.high`**: a soft limit. Above it, the kernel throttles the cgroup and reclaims memory aggressively, making the process slower instead of killing it. It gives a warning zone before the hard limit.
- **`memory.low` / `memory.min`**: protection from reclaim by other cgroups.

```bash
cat /sys/fs/cgroup/memory.current
cat /sys/fs/cgroup/memory.stat | grep -E '^(anon|file|kernel|sock|shmem) '
cat /sys/fs/cgroup/memory.events   # high, max, oom, oom_kill counters
cat /sys/fs/cgroup/memory.pressure # PSI for this cgroup
```

A rising `high` counter in `memory.events` with latency spikes means the container is being throttled for memory, a sign to raise the limit or cut usage before OOM kills start.

#### 396: How do NUMA, hyperthreading and CPU steal affect server performance?

- **NUMA** (Non-Uniform Memory Access): on multi-socket servers, each CPU socket has local memory. Accessing the other socket's memory is slower. A process whose threads run on one socket while its memory lives on another gets less memory bandwidth and higher latency. Databases and caches on large servers benefit from NUMA-aware placement (`numactl --cpunodebind=0 --membind=0`), or from running one instance per socket. Kubernetes has a Topology Manager for this. Most cloud VMs smaller than a full host are single-NUMA-node, so this matters mainly on big instances or bare metal.
- **Hyperthreading (SMT)**: two logical CPUs share one physical core. Two busy threads on the same core each get less than a full core's throughput. So "8 vCPUs" in the cloud is often 4 physical cores. CPU-heavy benchmarks scale worse than the vCPU count suggests. Plan capacity in physical cores for CPU-bound work.
- **Steal time** (`st` in `top`/`vmstat`): time your VM wanted to run but the hypervisor gave the physical CPU to someone else. Steady steal above a few percent means noisy neighbors or a burstable instance that ran out of credits. The fix is a different instance type (non-burstable, dedicated) or moving hosts, since there's nothing to fix in your code.

#### 397: What does "nf_conntrack: table full, dropping packet" mean, and how do you fix it?

Linux connection tracking (conntrack) keeps state for every connection passing through netfilter, which is used by NAT, iptables stateful rules, Docker networking and Kubernetes `kube-proxy` in iptables mode. The table has a maximum size (`nf_conntrack_max`). When it fills, the kernel drops new packets, and clients see timeouts that look random. Busy proxies, NAT gateways and nodes with many short connections hit this.

```bash
dmesg -T | grep conntrack
cat /proc/sys/net/netfilter/nf_conntrack_count
cat /proc/sys/net/netfilter/nf_conntrack_max
conntrack -S   # stats including drops and insert failures (conntrack-tools)
```

Fixes:

- Raise `net.netfilter.nf_conntrack_max` (and the hash table size, `nf_conntrack_buckets`), keeping in mind each entry uses some memory.
- Lower timeouts for finished connections, like `nf_conntrack_tcp_timeout_time_wait`.
- Reduce connection churn with keep-alive and pooling, which is the real fix in most cases.
- For load balancers and proxies with very high connection counts, bypass conntrack for specific traffic using `NOTRACK` rules, or use an eBPF-based data path (for example Cilium) that doesn't use conntrack the same way.

A related issue in Kubernetes is conntrack race conditions for UDP DNS, which cause occasional 5-second DNS delays. NodeLocal DNSCache or TCP for DNS helps.

#### 398: How do you use `ss -ti` to understand TCP performance for a connection?

`ss -ti` shows internal TCP details for each connection, which helps explain slow transfers.

```bash
ss -ti dst 10.0.2.15
ESTAB 0 0 10.0.1.10:443 10.0.2.15:51234
  cubic wscale:7,7 rto:204 rtt:3.2/1.1 ato:40 mss:1448 cwnd:10 ssthresh:7
  bytes_sent:18234567 bytes_retrans:524288 bytes_acked:17700000
  segs_out:12650 segs_in:6120 send 36.2Mbps lastsnd:4 pacing_rate 43.4Mbps
  delivery_rate 30.1Mbps retrans:0/362 rcv_space:14480 notsent:0 minrtt:1.9
```

What to look at:

- `rtt` (smoothed RTT / variance) and `minrtt`: if `rtt` is much higher than `minrtt`, there is queueing on the path (bufferbloat) or a busy receiver.
- `cwnd` and `ssthresh`: a small `cwnd` with `ssthresh` set means the connection saw loss and backed off.
- `retrans` and `bytes_retrans`: a high retransmit ratio (here about 3%) means packet loss on the path, which hurts throughput a lot with loss-based congestion control.
- `rto`: retransmission timeout. Large values mean stalls when loss happens.
- `send` and `delivery_rate`: how fast data is actually moving.
- `rcv_space` and window scaling: a small receive window on the other side limits throughput.
- `notsent`: bytes queued in the kernel not yet sent. Large values mean the network can't keep up.

Combine with `nstat -az | grep -i retrans` for system-wide counts and `tcpretrans` to see which connections lose packets.

#### 399: Why might disk-heavy workloads on cloud VMs suddenly get slow?

- **Burst credits run out**: AWS `gp2` volumes give IOPS based on size with a burst bucket. When the `BurstBalance` metric hits zero, performance drops to the baseline, which can be very low for small volumes. `gp3` gives a fixed baseline (3,000 IOPS and 125 MB/s) that you can raise separately, which is more predictable. Burstable instance types also have network and EBS bandwidth bursts.
- **Instance EBS bandwidth limit**: each instance type has a maximum EBS throughput. Several volumes can't exceed it together.
- **Write amplification and `fsync` storms**: databases checkpointing, log rotation or many small synced writes create bursts of I/O. In PostgreSQL, spreading checkpoints with `checkpoint_completion_target` and a larger `max_wal_size` smooths this out.
- **Page cache writeback**: Linux holds dirty pages and writes them in bursts. With large `vm.dirty_ratio`, a burst can block writers for seconds. Lower `vm.dirty_background_bytes` and `vm.dirty_bytes` for smoother writeback.
- **Noisy neighbors** on shared storage, and first-read latency on volumes restored from snapshots (blocks load lazily from S3 until initialized).
- **Logging to disk** synchronously from the app at high volume.

Check `iostat -x` (await, queue size), CloudWatch `VolumeQueueLength`, `VolumeReadOps`/`VolumeWriteOps` and `BurstBalance`, and `biolatency` for real latency distribution.

#### 400: How do you find a file descriptor leak?

Symptoms: `EMFILE: too many open files`, rising "open files" in metrics, or new connections failing after the process has run for a while.

```bash
# How many FDs does the process have, and what's the limit?
ls /proc/<pid>/fd | wc -l
grep 'open files' /proc/<pid>/limits

# What are they?
ls -l /proc/<pid>/fd | awk '{print $NF}' | sed -E 's/[0-9]+/N/g' | sort | uniq -c | sort -rn | head
lsof -p <pid> | awk '{print $5}' | sort | uniq -c   # by type: REG, IPv4, sock, FIFO

# Sockets by state and destination
ss -tanp | grep "pid=<pid>" | awk '{print $1, $5}' | sort | uniq -c | sort -rn | head
```

Interpreting the result:

- Many sockets to one upstream in `ESTABLISHED`: a connection pool without a limit, or connections never released.
- Many `CLOSE_WAIT` sockets: the remote side closed the connection but your app never called `close()`. This is almost always a bug in your code or a library, such as not consuming or destroying an HTTP response body.
- Many regular files with the same path: files opened per request without closing, like `fs.createReadStream` on an error path that never gets destroyed.

In Node, a common cause is not consuming a `fetch` response body. With undici, unread bodies keep the connection busy, so always read or cancel them (`await res.body?.cancel()`). A diagnostic report (`process.report.getReport().libuv`) also lists open handles.

#### 401: How do you make Kubernetes rolling deploys drop zero requests?

When a pod is terminated, two things happen in parallel: the kubelet sends SIGTERM to the container, and the pod is removed from Service endpoints (which then has to reach kube-proxy, ingress controllers and load balancers on every node). If the app stops accepting connections before all of them have updated, some requests still go to it and fail.

Steps:

1. **Add a short delay before shutdown starts**, so routing updates finish first:

```yaml
lifecycle:
  preStop:
    sleep:
      seconds: 10 # built-in sleep action in newer Kubernetes; older versions use exec: ["sleep","10"]
terminationGracePeriodSeconds: 45
```

2. **Handle SIGTERM in the app**: fail readiness, stop accepting new connections, finish in-flight requests, close keep-alive connections (`server.closeIdleConnections()`, and send `Connection: close` on remaining responses), then exit.
3. **Make `terminationGracePeriodSeconds`** longer than preStop delay plus the longest request.
4. **Set a matching deregistration delay** on cloud load balancers that target pods directly (AWS Load Balancer Controller with IP targets), and make sure the readiness gate or target health is used during rollout.
5. **Use `maxUnavailable: 0` and `maxSurge`** in the rollout strategy, plus a readiness probe that only passes when the app has warmed up.
6. **Add a PodDisruptionBudget** so node drains don't take down too many pods at once.

Test it: run a load test during a rollout and confirm the error count stays at zero.

#### 402: Why does Kubernetes report higher memory use than the app's RSS, and why can a pod be evicted with "free" memory on the node?

Kubernetes and the kubelet look at the **working set** (`container_memory_working_set_bytes`), which is the cgroup's memory usage minus inactive file pages. It includes active page cache (files recently read or written by the container), kernel memory and tmpfs, not just your process's RSS. A Node app that writes large logs or temp files, or reads many files, can show a working set much bigger than its heap.

Eviction: the kubelet evicts pods when the **node** crosses eviction thresholds (for example `memory.available < 100Mi`), choosing pods whose usage is furthest above their memory **requests**. A pod using more than it requested is a likely victim even if it is under its limit. Pods in the Guaranteed QoS class (requests equal limits for all resources) are evicted last.

OOM kill vs eviction: going above your container's own limit triggers the kernel OOM killer (exit code 137, reason `OOMKilled`). Node pressure triggers kubelet eviction (status `Evicted`). They need different fixes.

Practical steps: set memory requests close to real working set usage, set the limit with headroom, use `emptyDir` with `medium: Memory` carefully since it counts as memory, keep logs on stdout instead of local files, and watch both RSS and working set metrics.

#### 403: How does the Linux scheduler decide which thread runs, and how does that affect latency?

For normal threads, Linux used the Completely Fair Scheduler (CFS) for many years. From kernel 6.6 it uses EEVDF (Earliest Eligible Virtual Deadline First), which keeps the same fairness goal but gives better latency for tasks that run briefly and often. Each thread gets CPU time in proportion to its weight (set by `nice` value or cgroup CPU weight).

Effects on latency:

- When more threads are runnable than there are CPUs, threads wait in the run queue. This shows up as run queue latency (`runqlat`) and as `r` greater than core count in `vmstat`.
- **Nice and cgroup weights** decide who gets CPU under contention. Background jobs (backups, log shippers, builds) can be given lower weight so they don't steal CPU from latency-sensitive services.
- **CFS bandwidth control** (CPU quotas) is separate from fair sharing and causes throttling pauses, as explained earlier.
- **CPU migrations** between cores lose cache warmth. Pinning (`taskset`, Kubernetes static CPU manager policy for Guaranteed pods) can help very latency-sensitive services.
- **Real-time classes** (`SCHED_FIFO`, `SCHED_RR`) exist but are dangerous for normal servers, since a busy real-time thread can starve everything else.

For most web services, the main lessons are: don't run more busy threads than cores, keep background work at lower priority, and avoid tight CPU quotas.

#### 404: When would you use `strace`, `ltrace`, `perf trace` or eBPF, given their overhead?

- **`strace`**: uses ptrace, which stops the process on every syscall. It can slow syscall-heavy programs by 10x or more. Great for quickly answering "what is this process doing/waiting on?" in development or very briefly in production with filters (`-e trace=`).
- **`ltrace`**: traces calls to shared library functions (like `malloc` or OpenSSL functions). Even more overhead than `strace`, and often doesn't work well with modern binaries. Use it rarely.
- **`perf trace`**: like `strace` but based on kernel tracing, with much lower overhead. It can also summarize syscalls (`perf trace -s`) and works across processes.
- **eBPF tools (bpftrace, BCC)**: run small programs in the kernel at chosen events (syscalls, kernel functions, user-space probes), aggregating data in the kernel and only sending summaries. Overhead is low enough for production use for minutes or longer. They need root or specific capabilities and a recent kernel.

```bash
sudo perf trace -s -p <pid> -- sleep 10           # syscall summary, low overhead
sudo bpftrace -e 'tracepoint:syscalls:sys_exit_read /pid == 1234/ { @bytes = hist(args->ret); }'
```

Rule of thumb: use `strace` for a quick look on a test box, `perf trace` or eBPF for anything in production.

#### 405: How do you capture and analyze a core dump from a crashed Node.js process?

A core dump is a full snapshot of process memory at the moment of the crash. It is useful for native crashes (segfaults in addons) and for analyzing the exact state at an uncaught exception.

```bash
ulimit -c unlimited
node --abort-on-uncaught-exception server.js   # abort() on uncaught exceptions, producing a core dump
```

Where the core file goes depends on `/proc/sys/kernel/core_pattern`. On systemd hosts, `coredumpctl` manages them. In containers, the pattern is set by the host, so you may need to configure it on the node, and the dump counts against disk space.

To analyze:

- **llnode** (an LLDB plugin) understands V8 structures: `v8 bt` shows the JavaScript stack, `v8 findjsobjects` lists objects by type and count, `v8 inspect` shows an object.
- **gdb or lldb** alone show native stacks, which is what you want for crashes inside addons.

```bash
lldb node -c core.12345
(lldb) plugin load /path/to/llnode.so
(lldb) v8 bt
(lldb) v8 findjsobjects
```

Core dumps contain everything in memory, including secrets and user data, so handle them like production data. For many cases, a diagnostic report (`--report-on-fatalerror`) or a heap snapshot near the heap limit gives enough information with less risk and size.

---

### Advanced: Cloud Infrastructure and Delivery (406-420)

#### 406: How do you use ALB access logs to find where request time is spent?

ALB access logs (written to S3) have three timing fields per request:

- `request_processing_time`: time from when the ALB received the request until it sent it to a target. Usually tiny. High values mean the ALB itself is busy or waiting for a target connection.
- `target_processing_time`: time from sending the request to the target until the target started responding. This is your application's time (plus network to the target).
- `response_processing_time`: time from receiving the response headers from the target until the ALB started sending the response to the client.

A value of `-1` means the step didn't complete (for example, the target closed the connection or timed out), usually together with a 502 or 504 in `elb_status_code`.

Query them with Athena:

```sql
SELECT target_ip,
       approx_percentile(target_processing_time, 0.99) AS p99,
       count(*) AS requests,
       sum(CASE WHEN elb_status_code = 502 THEN 1 ELSE 0 END) AS e502
FROM alb_logs
WHERE day = '2026/10/22' AND request_url LIKE '%/api/%'
GROUP BY target_ip
ORDER BY p99 DESC;
```

This can show that one target is slow (a bad instance or a noisy neighbor), that 502s come from a keep-alive timeout mismatch (`target_processing_time = -1` with tiny durations), or that the time is outside your app entirely. Remember that the client's experienced latency also includes the network between the client and the ALB, which these fields don't cover.

#### 407: How do you stop autoscaling from oscillating or reacting too late?

Oscillation (scale out, scale in, scale out again) and slow reaction both come from mismatched signals and timings.

- **Warm-up time**: set instance warm-up or `initialDelaySeconds` to how long a new instance needs before it carries full load (boot, JIT warm-up, cache fill). Otherwise the group sees high metrics from cold instances and scales out more than needed.
- **Scale-in protection**: scale in slowly (longer stabilization windows, smaller steps) and scale out quickly. HPA's `behavior.scaleDown.stabilizationWindowSeconds` and AWS's scale-in cooldown handle this.
- **Leading indicators**: CPU lags behind demand. Request rate or concurrency per target reacts sooner. For queues, scale on backlog per worker.
- **Target value with headroom**: target 50 to 60% CPU instead of 80%, leaving room for spikes while new capacity starts.
- **Predictive scaling**: AWS predictive scaling and scheduled scaling add capacity ahead of known daily peaks.
- **Faster boot**: smaller images, pre-baked AMIs, warm pools (pre-initialized stopped instances in AWS), and fast app startup.
- **Watch the dependencies**: scaling the app beyond what the database can handle just moves the bottleneck and adds connection pressure.

Track scaling events next to latency graphs to check that capacity arrives before latency rises.

#### 408: The CDN cache hit ratio is 40% on content that should be cacheable. How do you raise it?

1. **Find out why requests miss**: look at CDN logs for cache status (`Miss`, `Expired`, `Bypass`, `Dynamic`) per path, and the response headers from the origin.
2. **Check origin headers**: `Cache-Control: private`, `no-store`, `max-age=0`, missing cache headers, or `Set-Cookie` on responses all prevent or limit caching. Fix them at the origin.
3. **Normalize the cache key**: remove tracking parameters (`utm_*`, `fbclid`, `gclid`), sort query strings, ignore cookies that don't change the response, and lowercase paths if appropriate. One page with 500 URL variations has 500 separate cache entries.
4. **Remove harmful `Vary` headers** like `Vary: User-Agent` or `Vary: Cookie`. Replace them with a small set of normalized variants if needed (device class header from the CDN).
5. **Increase TTLs** with versioned URLs for assets, and use `stale-while-revalidate` so expiring content doesn't cause misses for users.
6. **Add a shield or tiered cache** so misses at edges are served from a regional or central cache instead of the origin.
7. **Look at long-tail content**: many rarely requested items naturally miss. Larger caches (Cloudflare Cache Reserve, for example) or accepting lower hit rates for that segment are the options.
8. **Measure byte hit ratio as well as request hit ratio**, since large files matter more for origin load and cost.

#### 409: When should you run code at the edge, and what are the trade-offs between edge platforms?

Edge compute runs code in CDN locations close to users. It is good for:

- Redirects, rewrites, header changes, A/B test bucketing, and auth token checks before cache.
- Personalizing cached pages lightly (geo-based content, feature flags).
- Serving responses built from data that is also at the edge (KV stores, cached API data).

It is a poor fit when every request needs your central database, because each request still travels to the origin region, and the edge just adds a hop. Moving code to the edge only helps if the data is close too.

Platforms:

- **CloudFront Functions**: lightweight JavaScript, sub-millisecond, runs only on viewer request and response, no network calls, tight memory and time limits. Good for header and URL work.
- **Lambda@Edge**: Node.js or Python, can make network calls, runs on origin request and response too. Higher latency and cold starts, runs in regional edge caches.
- **Cloudflare Workers** (and similar like Fastly Compute, Deno Deploy, Vercel's edge runtime): V8 isolates with very fast startup, Web-standard APIs, access to edge storage (KV, Durable Objects, D1, R2). CPU time limits per request apply.

Also consider observability and debugging, since edge logs and traces can be harder to work with, and vendor lock-in through platform-specific APIs.

#### 410: How do S3 request rate limits work, and how do you handle `503 SlowDown` errors?

S3 supports at least 3,500 PUT/COPY/POST/DELETE and 5,500 GET/HEAD requests per second **per partitioned prefix**. S3 scales by splitting prefixes into more partitions as load grows, but that takes time. A sudden spike on one prefix can return `503 Slow Down` until S3 catches up.

How to handle it:

- **Spread keys over multiple prefixes**, for example `uploads/<hash-prefix>/<id>` instead of `uploads/2026-10-23/<id>`, when you expect high request rates. Each prefix scales independently.
- **Retry with exponential backoff and jitter**. The AWS SDK does this by default; make sure your retry settings (adaptive retry mode) are on.
- **Ramp up gradually** for large batch jobs instead of starting at full speed.
- **Cache reads** with CloudFront so repeated GETs don't hit S3 at all.
- **Batch small objects**: millions of tiny objects mean millions of requests. Combining them (for example into Parquet files) cuts request count and cost.
- **Use S3 Express One Zone** for workloads needing very low latency and very high request rates in one Availability Zone.

Also note that S3 latency per request is in the tens of milliseconds for first byte, so throughput comes from parallelism: many concurrent requests or byte-range fetches.

#### 411: Which Nginx settings matter at high traffic?

```nginx
worker_processes auto;            # one per CPU core
worker_rlimit_nofile 200000;      # file descriptor limit per worker

events {
    worker_connections 20000;     # per worker; counts both client and upstream connections
    multi_accept on;
}

http {
    sendfile on;                  # kernel copies files directly to the socket
    tcp_nopush on;                # send headers and file start in full packets
    tcp_nodelay on;

    keepalive_timeout 65s;
    keepalive_requests 1000;

    open_file_cache max=10000 inactive=30s;  # cache file descriptors and metadata
    open_file_cache_valid 60s;

    client_body_buffer_size 16k;
    proxy_buffers 16 16k;
    proxy_buffer_size 16k;

    access_log /var/log/nginx/access.log main buffer=64k flush=5s;  # buffered logging

    server {
        listen 443 ssl reuseport;  # separate accept queue per worker, better spread across cores
        http2 on;
        ssl_session_cache shared:SSL:50m;
        ssl_session_timeout 1d;
    }
}
```

Points to remember:

- Each proxied request uses two connections (client and upstream), so `worker_connections` must account for both.
- Buffered access logs cut disk writes a lot, and turning off access logs for health checks and static assets reduces noise.
- `reuseport` spreads new connections more evenly across workers.
- Watch the `stub_status` page (active, reading, writing, waiting) and the error log for "worker_connections are not enough" or upstream errors.

#### 412: How can retries at proxies and clients make an outage worse, and how do you configure them safely?

If every layer retries, the load multiplies. A browser retries 2 times, the CDN retries 2 times, Nginx retries the next upstream 2 times, and the app retries its database call 3 times: one user action can become dozens of requests exactly when the system is already overloaded (a retry storm). Retries of non-idempotent requests like `POST /payments` can also cause duplicate side effects.

Safer configuration:

- **Retry at one layer**, usually closest to the failure, and disable or limit others.
- **Only retry idempotent requests**, or use idempotency keys for writes (`Idempotency-Key` header stored with the result).
- **Exponential backoff with jitter**, and a **retry budget** (for example, retries may add at most 10% to the request rate).
- **Respect `Retry-After`** and 429/503 responses.
- **Circuit breakers**: stop calling a failing dependency for a while and fail fast.
- **Timeouts that shrink across layers**: the outer layer's timeout must be larger than the inner layer's timeout times its retries, or retries keep running after the caller has given up.

```nginx
location /api/ {
    proxy_pass http://api;
    proxy_next_upstream error timeout http_502 http_503;
    proxy_next_upstream_tries 2;
    proxy_next_upstream_timeout 3s;
    # non-idempotent methods (POST, PATCH) are not retried by default; keep it that way
}
```

#### 413: How should you set CPU requests and limits for Node.js pods, and what are QoS classes?

Node runs JavaScript on one thread but also uses extra threads for GC, JIT compilation and libuv. With a tight CPU limit (say `500m`), these threads together can use the quota in a few milliseconds of each 100 ms period, leading to throttling pauses that show up as p99 latency spikes, often during GC.

Common approach:

- **Set CPU requests** based on measured usage at normal peak. Requests drive scheduling and fair sharing under contention.
- **Avoid CPU limits** (or set them well above requests) for latency-sensitive services, so pods can burst when the node has idle CPU. Some teams keep limits for noisy batch jobs only.
- **Set memory request equal to limit**, since memory overcommit leads to evictions and OOMs.
- **One Node process per pod**, sized for about 1 core of steady usage, and scale horizontally.

QoS classes:

- **Guaranteed**: every container has requests equal to limits for CPU and memory. Evicted last, can get exclusive CPUs with the static CPU manager policy.
- **Burstable**: requests set but lower than limits (or some missing). Most services.
- **BestEffort**: no requests or limits. Evicted first.

Check throttling with `container_cpu_cfs_throttled_periods_total` and compare with latency. Removing a CPU limit that caused heavy throttling often cuts p99 sharply without changing average CPU.

#### 414: What networking issues inside Kubernetes commonly add latency?

- **DNS `ndots:5`**: by default, pod DNS settings treat names with fewer than 5 dots as relative, so a lookup for `api.stripe.com` first tries `api.stripe.com.default.svc.cluster.local`, `api.stripe.com.svc.cluster.local`, `api.stripe.com.cluster.local` and so on, each a failed query, before the real one. That adds latency and load on CoreDNS. Fixes: use fully qualified names with a trailing dot (`api.stripe.com.`), lower `ndots` in the pod's `dnsConfig`, and run NodeLocal DNSCache.

```yaml
dnsConfig:
  options:
    - name: ndots
      value: "2"
```

- **No DNS caching in the app**: Node doesn't cache DNS results by itself, so every new connection does a lookup through the thread pool. Keep-alive connections reduce lookups.
- **kube-proxy in iptables mode**: with thousands of Services, iptables rule chains get long and updates slow down. IPVS mode or eBPF-based data paths (Cilium) scale better.
- **Cross-zone traffic**: Service traffic may go to pods in another Availability Zone, adding latency and cost. Topology-aware routing (`trafficDistribution: PreferClose` in newer versions) keeps traffic in the same zone when possible.
- **Extra hops**: Ingress → Service → pod, plus a service mesh sidecar on each side. Each sidecar adds some latency and CPU. Measure it.
- **conntrack issues** for UDP DNS (occasional 5-second delays).
- **MTU mismatches** in overlay networks causing fragmentation or dropped large packets.

#### 415: How do you deploy without dropping connections behind an AWS load balancer?

- **Deregistration delay (connection draining)**: when a target is removed, the ALB stops sending new requests but lets in-flight requests finish for up to this delay (300 seconds by default). Set it a bit above your longest normal request, for example 30 to 60 seconds, so deploys don't wait five minutes for no reason.
- **Health check timing**: new targets must pass health checks (threshold × interval) before getting traffic. Make the health endpoint reflect real readiness (DB pool connected, caches warmed).
- **Slow start mode**: the ALB can ramp traffic to new targets over a period, so cold instances aren't flooded right away.
- **App behavior on SIGTERM**: keep serving while draining, close idle keep-alive connections and send `Connection: close` on the last responses.
- **Rolling or blue/green**: with ECS or CodeDeploy, configure minimum healthy percent and maximum percent so capacity never drops. Blue/green switches the listener between target groups and lets you roll back quickly.
- **WebSockets and long requests**: drain them deliberately, ask clients to reconnect, and expect reconnect storms. Spread them with jitter.

Validate with a load test during a deploy and watch for 5xx and connection resets in ALB metrics.

#### 416: How do you make CI pipelines much faster for a large JavaScript monorepo?

- **Only build and test what changed**: Nx, Turborepo or similar tools compute the affected projects from the dependency graph (`nx affected`, `turbo run --filter=...[origin/main]`).
- **Remote caching**: share build, lint and test outputs between CI runs and developers, so unchanged packages are skipped entirely.
- **Fast package installs**: pnpm with a cached store, or `npm ci` with a cached `~/.npm`. Avoid reinstalling for every job by caching per lockfile hash.
- **Parallelism and sharding**: split tests across machines (`vitest --shard=1/4`, `playwright test --shard=1/4`), and run independent jobs in parallel.
- **Faster tools**: esbuild, SWC, Rolldown/Vite and Oxc-based linters are much faster than older Babel- and webpack-based setups. Type-check once in a separate job instead of in every build.
- **Docker layer caching**: use BuildKit with a registry cache (`--cache-from`/`--cache-to type=registry`) so CI doesn't rebuild unchanged layers.
- **Right-size runners**: more cores or memory often pays for itself if jobs are CPU-bound.
- **Measure**: track pipeline duration per step over time and fix the slowest step first.

#### 417: How do you detect frontend performance regressions in CI without false alarms from noise?

Performance measurements in CI are noisy because of shared machines, background processes and network variation. Comparing single runs to a fixed threshold produces flaky failures.

Better approaches:

- **Run many samples** of both the base branch and the pull request on the same machine in the same job, alternating runs, so environmental noise affects both equally.
- **Use statistics**: compare distributions (median and confidence intervals, or a Mann-Whitney U test) and only flag changes that are both statistically significant and larger than a minimum meaningful size, like 5%.
- **Prefer stable metrics**: bytes shipped, request counts and main-thread task duration under CPU throttling are much more stable than wall-clock load times over the network.
- **Control the environment**: lock CPU frequency if you own the machines, throttle the network consistently, disable unrelated background jobs, and use a local static server instead of the internet.
- **Tools**: Tachometer (for micro and page-level benchmarks with confidence intervals), Lighthouse CI with multiple runs and median assertions, and bundle size tools for byte-level budgets.
- **Track trends** on a dashboard so slow, gradual regressions that each pass the threshold still get noticed.

#### 418: How do you use Terraform to build repeatable performance test environments, and what are the pitfalls?

Approach:

- Build the test environment from the same modules as production, with variables for instance counts and sizes. Keep differences explicit and minimal.
- Create **ephemeral environments** per test run (`terraform apply` with a unique workspace or name prefix, run tests, then `terraform destroy`) so tests don't share state or interfere with each other.
- **Seed data** to production-like volume and distribution as part of the pipeline, for example by restoring an anonymized snapshot.
- **Tag everything** (test run ID, owner, expiry) and have an automated cleanup job for anything left behind.
- **Pin versions** of providers, AMIs and container images so two runs months apart are comparable.

Pitfalls:

- **Cold infrastructure**: newly created databases, volumes restored from snapshots and empty caches perform differently at first. Warm them up (for example, read all EBS blocks or run a warm-up phase) before measuring.
- **Account limits and quotas** that production has raised but test accounts haven't.
- **Shared services**: a "dedicated" environment that still uses a shared database or third-party sandbox is not isolated.
- **Drift**: manual changes to production that aren't in Terraform make the test environment differ. Run `terraform plan` against production regularly to detect drift.
- **Cost**: large environments left running are expensive. Automate teardown and schedule tests.

#### 419: How do you reduce cold start latency for Node.js on AWS Lambda?

A cold start happens when Lambda creates a new execution environment: it downloads your code, starts the runtime and runs your initialization code before handling the first request.

- **Make the package small**: bundle and minify with esbuild, exclude dev dependencies, and import only the AWS SDK v3 clients you use (`@aws-sdk/client-dynamodb`, not the whole SDK). Less code means faster load and parse.
- **Do expensive setup once, outside the handler**: create SDK clients and DB connections at module level so warm invocations reuse them. Use top-level `await` in ES modules for async init.
- **Lazy-load rarely used modules** inside the code paths that need them.
- **Choose memory carefully**: CPU scales with memory, so more memory often gives a faster cold start and faster execution for a similar cost.
- **Use arm64 (Graviton)** for better price-performance in most cases.
- **Provisioned concurrency** keeps environments initialized for predictable latency, at a cost. Use it for user-facing functions with steady traffic.
- **Keep connections efficient**: use RDS Proxy for relational databases to avoid connection storms when many environments start at once.
- **Avoid VPC-related overhead** where possible (modern Lambda VPC networking is much faster than before, but VPC access to the internet still needs NAT).

Measure with the `Init Duration` in the `REPORT` log lines and with X-Ray or OpenTelemetry traces.

#### 420: What are the trade-offs of running a web app in multiple regions for latency?

Benefits: users connect to a nearby region, so round trips for dynamic requests are shorter, and the app survives a regional outage.

The hard part is data:

- **Read-heavy apps** can use read replicas or global tables in each region, with writes going to one primary region. Reads are fast everywhere; writes from far regions are slow, and replication lag means users may not see their own writes immediately.
- **Multi-primary databases** (DynamoDB global tables, CockroachDB, Spanner, Aurora DSQL and others) allow writes everywhere, but bring conflict resolution or higher write latency from cross-region consensus.
- **Data residency rules** may require some users' data to stay in a specific region, which shapes the architecture.

Routing: use latency-based or geolocation routing (Route 53, global load balancers like AWS Global Accelerator or Cloudflare Load Balancing) with health checks so users fail over automatically.

Other costs: more infrastructure to run and monitor, cross-region data transfer fees, cache warmup in each region, and more complex deploys. A simpler first step is often to put a CDN in front of one region and cache as much as possible at the edge. Many apps get most of the latency benefit that way without multi-region data.

---

### Advanced: Observability, Profiling and Reliability (421-435)

#### 421: What is tail latency amplification in fan-out requests, and how do you reduce it?

If one user request calls N backend services in parallel and waits for all of them, the slowest call decides the response time. Even if each backend has only a 1% chance of being slow (its p99), the chance that at least one of 100 parallel calls is slow is `1 - 0.99^100 ≈ 63%`. So the backends' p99 becomes the frontend's typical latency.

Ways to reduce it:

- **Reduce fan-out**: batch calls, denormalize data, or cache aggregated results.
- **Hedged requests**: if a request hasn't returned by around the p95 latency, send a second copy to another replica and use whichever responds first. This adds only a few percent more load and cuts the tail a lot. Only do this for idempotent reads.
- **Timeouts with partial results**: return what you have after a deadline and show placeholders for missing parts, if the product allows it.
- **Fix tail causes at the source**: GC pauses, CPU throttling, cold caches, lock contention, noisy neighbors.
- **Load balancing that avoids slow replicas**, like least outstanding requests or latency-aware balancing.

```js
async function hedged(fn, hedgeAfterMs) {
  const ac = new AbortController();
  const first = fn(ac.signal);
  const timer = new Promise((r) => setTimeout(r, hedgeAfterMs, "hedge"));
  if (
    (await Promise.race([
      first.then(
        () => "done",
        () => "done",
      ),
      timer,
    ])) === "done"
  )
    return first;
  const second = fn(ac.signal);
  try {
    return await Promise.any([first, second]);
  } finally {
    ac.abort();
  }
}
```

#### 422: What is coordinated omission, and how do HDR histograms help?

Coordinated omission happens when a load generator waits for each response before sending the next request (a closed loop). When the server stalls for 2 seconds, the tool sends no requests during the stall, so only one slow sample is recorded instead of the many requests real users would have sent during that time. The reported p99 can look fine while real users suffered badly.

How to avoid it:

- Use **open-model** load generators that send requests at a fixed schedule regardless of responses (k6 arrival-rate executors, wrk2, Gatling's open injection, autocannon's `--overallRate` with care).
- Or correct the measurements: measure each request's latency from when it _should_ have been sent according to the schedule, not when it was actually sent.

**HDR Histogram** is a data structure that records latency values with a fixed relative precision (for example 3 significant digits) over a huge range, from microseconds to hours, using little memory. It makes percentiles accurate even at p99.99, can be merged across threads and machines, and some implementations include coordinated omission correction (`recordValueWithExpectedInterval`). Many load tools and latency libraries use it internally.

#### 423: How do you design an OpenTelemetry Collector pipeline for a high-traffic system?

The Collector receives telemetry, processes it and exports it. A common production setup has two tiers:

1. **Agent tier** (a DaemonSet or sidecar): receives OTLP from apps on the same node, adds resource attributes (Kubernetes pod, node, namespace), batches and forwards. Apps send to localhost, which is cheap and reliable.
2. **Gateway tier** (a scaled deployment): does tail sampling, filtering and export to backends.

```yaml
receivers:
  otlp:
    protocols: { grpc: {}, http: {} }
processors:
  memory_limiter: # first: refuse data before running out of memory
    check_interval: 1s
    limit_percentage: 80
    spike_limit_percentage: 20
  k8sattributes: {}
  tail_sampling:
    decision_wait: 10s
    policies:
      - {
          name: errors,
          type: status_code,
          status_code: { status_codes: [ERROR] },
        }
      - { name: slow, type: latency, latency: { threshold_ms: 1000 } }
      - {
          name: rest,
          type: probabilistic,
          probabilistic: { sampling_percentage: 5 },
        }
  batch: # last: send efficient batches
    send_batch_size: 8192
    timeout: 5s
exporters:
  otlp/backend:
    endpoint: tempo.observability:4317
    sending_queue: { enabled: true, queue_size: 5000 }
    retry_on_failure: { enabled: true }
service:
  pipelines:
    traces:
      receivers: [otlp]
      processors: [memory_limiter, k8sattributes, tail_sampling, batch]
      exporters: [otlp/backend]
```

Key points: tail sampling requires all spans of a trace on the same gateway instance, so put a `loadbalancing` exporter (routing by trace ID) in the agent tier. Monitor the Collector's own metrics (dropped spans, queue size, refused data). Keep SDK-side batching and timeouts reasonable so apps never block on telemetry.

#### 424: How do you find the critical path in a distributed trace?

The critical path is the chain of spans that actually determined the total duration. Optimizing anything off the critical path doesn't make the request faster.

How to find it:

- Start at the root span. Look at its children over time. Where children run in parallel, only the one that finished last is on the critical path. Where they run in sequence, all are.
- Repeat inside each critical child.
- **Gaps** in a parent span where no child is running are time spent in the parent itself: CPU work, waiting for a pool, event loop delay, or missing instrumentation.
- Many tracing UIs (Jaeger, Grafana Tempo, Honeycomb, Datadog) highlight the critical path automatically.

Common findings:

- **Sequential calls that could be parallel**: spans for `getUser`, `getCart`, `getRecommendations` one after another.
- **Waterfalls of small DB queries** (N+1), each short but adding up.
- **A long gap before the first DB span**, meaning connection pool wait or a slow middleware.
- **Fire-and-forget work** shown as spans continuing after the response was sent, which aren't on the user's critical path but may still use resources. Use span links instead of parent-child for async follow-up work like queue consumers.

#### 425: What are exemplars, and how do they connect metrics to traces?

An exemplar is a sample data point attached to a metric value: for example, a histogram bucket for "requests slower than 1 second" carries the trace ID of one actual request that fell into that bucket. In a dashboard, you see a latency spike on a graph, click the exemplar dot and jump straight to a trace of a slow request from that moment.

How it works:

- The metrics library records the active trace ID when it observes a value (OpenTelemetry SDKs do this automatically when a span is active and the trace is sampled).
- The metrics format must support exemplars (OpenMetrics/Prometheus with exemplar storage enabled, or OTLP).
- The dashboard (Grafana, for example) must have the trace data source linked.

Exemplars only help if the referenced trace was actually kept, so they work best combined with sampling that keeps slow and error traces. They are a cheap way to avoid the "the graph shows p99 went up, now what?" problem without high-cardinality labels.

#### 426: Why is high cardinality a problem in metrics, and how do you avoid it?

Each unique combination of metric name and label values is a separate time series that the metrics system stores and indexes. Adding a label like `user_id`, `request_id`, raw URL path or full error message can create millions of series. The result: high memory use, slow queries, expensive bills, and sometimes the metrics backend falls over.

How to avoid it:

- Use **bounded labels**: route templates (`/users/:id`), status code classes, region, service, method.
- **Never use IDs, emails, timestamps or raw URLs** as metric labels.
- Put high-cardinality detail in **traces and logs**, which are built for per-request data, and link to them from metrics with exemplars.
- **Drop or aggregate labels** at the Collector or with Prometheus relabeling before storage.
- Watch the series count per metric (for example `prometheus_tsdb_head_series` and per-metric counts) and alert when it jumps after a deploy.
- Be careful with automatic instrumentation that uses the raw path as a label. Make sure it uses route templates.

If you really need to analyze by many dimensions, use a tool designed for high-cardinality events (wide structured events in a columnar store) instead of a time-series metrics database.

#### 427: How do continuous profiling and differential flame graphs help find regressions?

Continuous profiling runs a low-overhead sampling profiler on every instance all the time (for example, Pyroscope, Parca, Grafana Cloud Profiles, Datadog Continuous Profiler, Google Cloud Profiler). You can then look at CPU, allocation and lock profiles for any time window, service, version or pod, without reproducing the problem.

A **differential flame graph** compares two profiles, for example "version 1.42 vs 1.43" or "yesterday 14:00 vs today 14:00". Functions that use more time are highlighted (often red) and functions that use less are highlighted in another color (often blue). Instead of reading two flame graphs and guessing, you see exactly which code paths got more expensive.

Typical uses:

- After a deploy CPU usage rose 20%: the diff shows a new JSON validation step in a hot middleware.
- Memory allocations increased: an allocation profile diff shows a library upgrade creating new buffers per request.
- Cost reduction: find the top functions across the whole fleet, since 5% saved in a function that runs everywhere is a lot of money.

Tag profiles with version, region and endpoint so you can slice them the same way as metrics.

#### 428: Show how allocation profiling can reduce GC pressure in a hot path.

Suppose a sampling heap profile shows that a request handler allocates a lot in a function that formats rows.

```js
// Before: creates many short-lived objects and strings per row
function formatRows(rows) {
  return rows
    .map((r) => ({ ...r, total: (r.price * r.qty).toFixed(2) }))
    .filter((r) => r.qty > 0)
    .map((r) => `${r.id},${r.name},${r.total}`)
    .join("\n");
}
```

Each row creates a spread copy of the object, a filtered array, a mapped array of strings, plus temporary strings. With 10,000 rows per request and hundreds of requests per second, the young generation fills quickly, scavenges run constantly, and some objects get promoted.

```js
// After: single pass, no intermediate arrays or object copies
function formatRows(rows) {
  let out = "";
  for (let i = 0; i < rows.length; i++) {
    const r = rows[i];
    if (r.qty <= 0) continue;
    if (out) out += "\n";
    out += r.id + "," + r.name + "," + (r.price * r.qty).toFixed(2);
  }
  return out;
}
```

How to verify:

1. Record an allocation sampling profile (DevTools Memory panel connected to Node, or `--heap-prof`) under load, before and after.
2. Compare `--trace-gc` output or GC metrics: fewer scavenges per second and less time in GC.
3. Check throughput and p99 latency with a load test.

Only optimize like this where profiles show it matters. For most code, readable chained array methods are fine.

#### 429: How do you find lock contention in a Node.js system, given JavaScript is single-threaded?

JavaScript itself doesn't use locks, but contention still happens in the system around it:

- **Database locks**: rows or tables locked by other transactions. Look at DB wait events (`pg_stat_activity.wait_event_type = 'Lock'`), lock wait logs, and long DB spans with low DB CPU.
- **Pool contention**: requests waiting for a DB connection, an HTTP agent socket, or a worker thread in a pool. Measure acquire wait time as a metric and as a span.
- **libuv thread pool**: tasks waiting for one of the pool threads. Instrument with trace events or measure `fs` and `dns.lookup` latency under load.
- **Application-level mutexes**: Redis locks (Redlock), advisory locks, or in-process async mutexes guarding shared resources (like token refresh). Add metrics for wait time and hold time.
- **`Atomics.wait`** in workers sharing memory.
- **Kernel-level contention**: `futex` waits in `strace`, or off-CPU analysis showing threads blocked in locks inside native addons or the allocator.

The pattern to look for: latency rises with concurrency while CPU stays low and the event loop isn't blocked. That means something is waiting. Off-CPU profiles and traces with spans around every acquire point tell you what.

#### 430: What goes wrong when running large load tests, and how do you avoid it?

- **The load generator is the bottleneck**: its CPU or network maxes out, and you measure the generator's limits instead of the system's. Watch generator CPU, use several machines (distributed k6, k6 Cloud or Kubernetes operator, JMeter in distributed mode), and confirm the target rate was actually reached.
- **All traffic from one IP**: load balancers, WAFs and rate limiters behave differently (or block you), and connection distribution is unrealistic. Use multiple generators and source IPs.
- **No connection reuse or too much of it**: real browsers open new connections and do TLS handshakes; many tools reuse a few keep-alive connections. Model both cases.
- **DNS caching**: generators cache DNS forever, so DNS-based load balancing or failover isn't exercised.
- **Testing through the CDN by accident**: you test the CDN's cache, not your origin. Or the reverse: you bypass the CDN that real users go through.
- **Unrealistic data**: same user, same product, so everything is cached.
- **Side effects on shared systems**: emails sent, payments created, third-party APIs hit with real requests. Use sandboxes and mocks.
- **Ramping too fast**: autoscaling and JIT warm-up never get a chance. Include realistic ramp-up.
- **Not watching the system during the test**: collect server metrics, traces and DB stats along with load tool results, or you won't know why it failed.

#### 431: How do you find a system's capacity limit, and what does the Universal Scalability Law say?

Run a stepped load test: increase load in steps (for example every 5 minutes), keeping each step long enough to stabilize. Plot throughput and latency against offered load. You typically see:

1. A linear region: throughput rises with load, latency stays flat.
2. A knee: latency starts rising faster as some resource saturates and queues form.
3. A plateau or decline: throughput stops rising or even drops while latency explodes.

The safe operating point is below the knee, with enough headroom for spikes and failures (for example, survive losing one zone).

The **Universal Scalability Law** (Neil Gunther) models throughput with N workers or nodes as:

```text
X(N) = λN / (1 + σ(N − 1) + κN(N − 1))
```

- `σ` (contention) models the part of the work that is serialized, like a shared lock or a single database. It makes throughput flatten (similar to Amdahl's law).
- `κ` (coherency) models the cost of keeping shared state in sync between workers, like cache invalidations or cross-node chatter. It makes throughput actually decrease after a point.

By fitting σ and κ to a few measured points, you can estimate where adding more instances stops helping, and whether the problem is serialization (find and remove the shared bottleneck) or coherency (reduce coordination).

#### 432: During a 12-hour soak test, memory grows slowly. How do you tell a leak from normal behavior, and pin it down?

Normal patterns:

- **Warm-up growth that levels off**: caches filling up to their size limit, JIT code, connection pools reaching max size.
- **Sawtooth heap** where the minimum after each major GC stays flat.
- **RSS that grows and stays high** but stabilizes, due to the allocator keeping freed memory.

Leak patterns:

- The **post-GC heap minimum keeps rising** over hours at a steady rate.
- Growth rate correlates with **request count** (a per-request leak) or with **time** (timers, intervals, polling).
- Eventually, more frequent major GCs, rising latency and finally an OOM.

How to pin it down:

1. Plot `heapUsed` right after GC (from `--trace-gc` or GC metrics via `PerformanceObserver` with `entryTypes: ['gc']`) together with request count.
2. Compute growth per request: if heap grows 50 MB per 1 million requests, it's about 50 bytes per request, so look for something small added to a collection on every request.
3. Take heap snapshots at, for example, 2 hours, 6 hours and 10 hours. Compare them and look for constructors whose count grows in proportion.
4. Check retainers for those objects.
5. If the heap is flat but RSS grows, look at native memory: `external` and `arrayBuffers`, allocator behavior, native addons.
6. Fix, then repeat the soak test to confirm the post-GC heap is flat.

#### 433: How do you design latency SLOs that actually reflect user experience?

- **Measure close to users**: at the edge or load balancer for server latency, and in RUM for page experience. App-internal timers miss queueing before the app and network time.
- **Use thresholds, not averages**: "99% of checkout API requests complete in under 500 ms" is easy to understand and to compute as good events / total events. Picking both the threshold and the percentage matters.
- **Separate by type of work**: interactive API calls, background jobs, file uploads and reports have different expectations. One SLO across all endpoints is dominated by the most common endpoint.
- **Focus on critical user journeys**: login, search, add to cart, checkout. An SLO per journey (possibly combining several calls) maps better to what the business cares about.
- **Include errors in latency SLOs carefully**: a fast error is not a good event. Count failed requests as bad for both availability and latency SLIs, or keep separate SLOs.
- **Pick windows**: 28 or 30 day rolling windows for SLOs, with burn rate alerts on shorter windows.
- **Write an error budget policy**: what happens when the budget runs out (pause risky releases, prioritize reliability work), agreed with product owners in advance.
- **Revisit regularly**: if the SLO is always met easily, it may be too loose to drive decisions. If it's always missed, it's not credible.

#### 434: How do you design alerts that catch real problems without causing alert fatigue?

- **Alert on symptoms users feel**: SLO burn rates, error rates, latency against thresholds. These page a human.
- **Use causes for diagnosis, not paging**: high CPU, a full disk on one replica, or one pod restarting are dashboard or ticket items unless they directly threaten the SLO.
- **Multi-window burn rate alerts** for SLOs, so short blips don't page but sustained problems do, and alerts clear quickly after recovery.
- **Every page must be actionable** and have a runbook link explaining what to check first.
- **Group related alerts**: one incident should produce one page, not 50 (Alertmanager grouping, inhibition rules so a "region down" alert silences per-service alerts).
- **Tune or delete noisy alerts**: track how many alerts led to action. Alerts that are routinely ignored should be fixed or removed.
- **Alert on saturation trends with lead time**: "disk will be full in 4 hours" (linear prediction) is more useful than "disk is 90% full".
- **Test alerts** with game days or synthetic failures so you know they fire.

#### 435: How do you use fault injection to verify that timeouts, retries and fallbacks actually work?

Code paths for failures are rarely exercised, so they often don't work when needed. Fault injection deliberately introduces failures in a controlled way.

Tools and methods:

- **Toxiproxy**: a TCP proxy between your app and a dependency that can add latency, limit bandwidth, drop connections or return resets on command. Good for integration tests and staging.

```bash
toxiproxy-cli create -l 0.0.0.0:6380 -u redis:6379 redis_proxy
toxiproxy-cli toxic add -t latency -a latency=2000 -a jitter=500 redis_proxy
# app connects to :6380, now every Redis call is 1.5 to 2.5 s slower
```

- **Service mesh fault injection** (Istio, Linkerd): add delays or HTTP errors to a percentage of requests between services without code changes.
- **Chaos tools** (AWS Fault Injection Service, Chaos Mesh, LitmusChaos, Gremlin): kill pods, stress CPU or memory, cut network between zones, or throttle disks.
- **Application-level flags** that make a client fail or delay on purpose in test environments.

What to verify:

- Timeouts actually fire at the configured values and don't stack up across layers.
- Retries back off and stop, and don't multiply load.
- Circuit breakers open and close as expected.
- Fallbacks (cached data, degraded mode) are used and look acceptable to users.
- Alerts fire and dashboards show the problem clearly.
- The system recovers fully when the fault is removed, without manual restarts.

Start in staging with small scope, define stop conditions, and only then run limited experiments in production.

---

### Advanced: Web Performance Standards and Metrics (436-450)

#### 436: How exactly is INP calculated for a page?

1. The browser records Event Timing entries for every discrete interaction: clicks, taps and key presses. Events from the same physical interaction (like `pointerdown`, `pointerup` and `click`) share an `interactionId`.
2. The latency of one interaction is the longest `duration` among its events. Duration runs from the hardware event timestamp until the next frame is presented after all handlers finished, rounded to 8 ms.
3. At the end of the page's life (or when reported), the browser picks a high percentile of all interaction latencies: it takes the worst interaction, but for every 50 interactions it ignores the single highest one. So a page with fewer than 50 interactions reports its worst; a page with 120 interactions reports roughly its third-worst.
4. Hovering, scrolling and pinch zooming aren't interactions. Keyboard interactions are grouped `keydown`/`keyup`.
5. Interactions in iframes count toward the top-level page's INP in CrUX, but JavaScript in the parent page can't see same-origin iframe interactions unless measured inside the iframe (and can't see cross-origin ones at all).
6. CrUX then reports the 75th percentile of page INP values across all page views. Page views with no interactions have no INP.

So INP is about your worst interactions on the slowest devices. One heavy handler that runs only on a rarely used button can still dominate if users click it.

#### 437: How does CLS session windowing work, and how do you measure CLS correctly in a single-page app?

Each layout shift gets a score: **impact fraction** (share of the viewport affected by unstable elements, combined before and after positions) × **distance fraction** (largest distance moved, divided by the viewport's largest dimension). Shifts within 500 ms of a discrete user input (`hadRecentInput: true`) are excluded, because users expect content to change when they click. Shifts caused by changes to `transform` don't count, since they don't change layout.

Shifts are grouped into **session windows**: a window continues while shifts happen less than 1 second apart, up to 5 seconds total. CLS is the score of the worst window, not the sum over the whole page life. This change (made in 2021) stopped long-lived pages from being punished just for staying open.

In single-page apps:

- Browsers measure CLS for the whole document lifetime, across client-side route changes, since a "soft navigation" isn't a new page load. A shift during one route change can be attributed to the initial landing page in CrUX.
- In your own RUM, you can reset the windowing on each route change to attribute CLS per route, but your numbers will then differ from CrUX.
- Route transitions that replace content right after a click are excluded only if they happen within 500 ms of the input. Slow data loading that changes the layout after that counts. Use skeletons with the right size, and keep layout stable while data loads.
- Chrome is experimenting with soft navigation measurement (see the next questions), which may change how SPAs are reported in the future.

#### 438: What are the less obvious rules about which element counts as LCP?

- LCP is reported for candidates as they render. The final LCP is the last candidate before the user's first interaction (click, tap, key press or scroll). After that, the browser stops reporting new candidates.
- Elements counted: `<img>`, `<image>` inside SVG, `<video>` (poster image or first frame), elements with a CSS `background-image` loaded via `url()`, and block-level elements containing text.
- **Size** is the visible area in the viewport, clipped by overflow and the viewport. For images, it's the smaller of the displayed size and the image's natural size (scaled-up small images don't get credit for the upscaled size).
- **Low-content images** are ignored: Chrome excludes images with very low bits per pixel (like solid color or blurred placeholders), so a tiny blurred placeholder can't become the LCP. When the real image loads, it becomes the candidate.
- Elements with `opacity: 0` aren't counted until they become visible, so a fade-in animation delays LCP until it starts showing.
- Elements removed from the DOM still count as the LCP if they were the largest when painted (this changed in the past; current Chrome keeps the reported candidate).
- **Full-viewport background images** may be treated as background and ignored in some cases.
- Cross-origin images without `Timing-Allow-Origin` report `renderTime` as 0 in some older implementations. Chrome now exposes a coarsened render time.
- For prerendered pages, LCP is measured from activation, and for bfcache restores, the web-vitals library reports time to the next frame after restoration.

#### 439: What are soft navigations, and how are they measured?

In single-page apps, a "navigation" usually doesn't load a new document. The app updates the URL with the History or Navigation API and re-renders content. Traditional metrics like LCP and TTFB only cover the first hard page load, so routes users reach through client-side navigation get no LCP of their own, and INP and CLS from many routes are mixed into the landing page's numbers.

Chrome has been working on a **Soft Navigations API**, available behind a flag and as an origin trial, which detects soft navigations when a user interaction leads to a URL change and a DOM change that paints. It then:

- Emits `soft-navigation` performance entries with a `navigationId` and start time.
- Reports LCP candidates for the new route (with the `navigationId`), and attributes interactions and layout shifts to the right navigation.

```js
new PerformanceObserver((list) => {
  for (const e of list.getEntries())
    console.log("soft nav", e.name, e.startTime);
}).observe({ type: "soft-navigation", buffered: true });
```

The `web-vitals` library has had experimental support (`reportSoftNavs`) for it. CrUX doesn't report soft navigations separately yet. Until it does, measure route changes yourself: mark the route change start, measure when the main content of the new route renders (with element timing or your own mark), and report it per route. Treat the API details as subject to change.

#### 440: How do prerendering and bfcache change how TTFB, FCP and LCP should be measured?

- **Prerendered pages**: the page may have been loaded long before the user clicked. Measuring from `navigationStart` would give negative or meaningless numbers. Use `activationStart` from the navigation entry and subtract it: `LCP_reported = max(0, lcp.startTime - activationStart)`. TTFB is `max(0, responseStart - activationStart)`, often 0, which is correct because the user waited for nothing.
- **bfcache restores**: there is no new navigation entry. The `pageshow` event with `persisted: true` marks the restore. Metrics like FCP and LCP are measured as the time from the `pageshow` event to the next frame. INP and CLS restart for the new "page view".
- **Navigation type**: report `nav.type` (`navigate`, `reload`, `back_forward`, `prerender`) and whether it was a bfcache restore, so you can segment. Mixing instant restores with cold loads hides problems in each group.
- **103 Early Hints**: `firstInterimResponseStart` marks when the 103 arrived and `responseStart` may refer to the final response in newer Chrome versions. Be clear which one your TTFB uses.
- **Service worker served pages**: `workerStart` and `fetchStart` show worker startup and handling time inside TTFB.

```js
const [nav] = performance.getEntriesByType("navigation");
const activation = nav.activationStart || 0;
const ttfb = Math.max(0, nav.responseStart - activation);
```

The `web-vitals` library handles all of these cases, which is a good reason to use it instead of writing your own.

#### 441: How do CSS and scripts interact to block rendering and parsing, and what does `blocking="render"` do?

- **Stylesheets in `<head>`** block rendering: the browser won't paint until they're loaded and parsed.
- **Classic synchronous scripts** block the HTML parser: parsing stops while the script downloads and runs.
- **Stylesheets also block scripts**: a synchronous script that comes after a stylesheet won't run until that stylesheet has loaded, because the script might read computed styles. So a slow CSS file can delay script execution, which in turn delays parsing of the rest of the page. This is why putting a stylesheet followed by a synchronous inline script in the head can be surprisingly slow.
- **`async` and `defer` scripts** don't block parsing. `defer` scripts still wait for preceding stylesheets before running.
- **Module scripts** are deferred by default; `async` modules run as soon as they and their dependencies are ready.
- **Fonts** don't block rendering in the same way, but they can hide text (`font-display: block`) or cause swaps.

`blocking="render"` (Chromium) lets you explicitly mark an element as render-blocking:

```html
<script src="/critical-theme.js" async blocking="render"></script>
<link rel="expect" href="#main-content" blocking="render" />
```

The first example makes the async script render-blocking without blocking the parser, for something like a theme that must apply before first paint. The second, used for cross-document View Transitions, delays first render until the `#main-content` element has been parsed, so the transition has the right content to animate. Use it sparingly, since it directly delays FCP.

#### 442: How would you design an image delivery pipeline for a large site?

- **Store originals once** in object storage, and generate variants on demand with an image CDN or service (Cloudinary, imgix, Cloudflare Images, CloudFront with a resize function, or a self-hosted service using `sharp`). Cache variants at the CDN.
- **Choose formats by content negotiation**: read the `Accept` header (`image/avif,image/webp,...`) and return AVIF, WebP or JPEG. The response needs `Vary: Accept`, and the CDN cache key must include a normalized format value (not the full `Accept` header) to keep hit ratios high.
- **Choose sizes**: generate a fixed set of widths (for example 320, 640, 960, 1280, 1920, 2560) instead of any arbitrary width, so cache entries are reused. Use `srcset`/`sizes` in markup. Client Hints (`Sec-CH-DPR`, `Sec-CH-Width`, `Sec-CH-Viewport-Width`, enabled by `Accept-CH`) let the server pick the size automatically in Chromium browsers, but they need `Vary` on those hints too.
- **Quality settings per format**: AVIF at lower quality numbers looks similar to JPEG at higher ones. Test visually, and consider perceptual quality metrics (like SSIMULACRA2 or Butteraugli) to automate it.
- **Markup rules**: width and height (or `aspect-ratio`) always, lazy loading below the fold, `fetchpriority="high"` for the LCP image, `decoding="async"` for others.
- **Placeholders**: dominant color or tiny blurred previews to improve perceived load, while knowing low-entropy placeholders won't count as LCP.
- **Monitoring**: track bytes per page, format share, cache hit ratio for image variants, and LCP for image-LCP pages in RUM.

#### 443: How do you ship less JavaScript to modern browsers without breaking older ones?

- **Set browser targets based on real usage**: use a Browserslist query such as `baseline widely available` or a list based on your analytics, instead of old defaults that include long-dead browsers. Transpiling modern syntax (classes, async/await, optional chaining) down to ES5 makes code larger and slower.
- **Remove unneeded polyfills**: check what `core-js` or `@babel/preset-env` with `useBuiltIns` adds for your targets. Many apps still ship polyfills for `Promise`, `fetch` or `Array.prototype.includes` that every target browser already has.
- **Drop the `module/nomodule` split** in most cases. Today, browsers without module support are a negligible share for most sites, so a single modern build is simpler and smaller.
- **Avoid heavy libraries for small features**: `date-fns` or the `Intl` APIs instead of Moment.js, native `structuredClone` instead of a deep-clone library, CSS for animations instead of JS libraries.
- **Analyze each dependency's cost** with bundle analyzers or bundlephobia-style tools before adding it.
- **Code split by route and interaction**, and preload what's needed next.
- **Compress well**: Brotli at high levels for static bundles, and consider Compression Dictionary Transport so returning users download only diffs after a deploy.
- **Check `sideEffects` and ESM builds** of dependencies so tree shaking works.

#### 444: What are the trade-offs of running third-party scripts in a Web Worker (for example with Partytown)?

Partytown and similar tools run third-party scripts like analytics and tag managers in a Web Worker so they don't compete with your code on the main thread. Since these scripts expect `window` and `document`, the library provides proxies that forward DOM access from the worker to the main thread. To make synchronous DOM reads work inside the worker, it uses synchronous XHR intercepted by a Service Worker, or `Atomics.wait` when the page is cross-origin isolated.

Benefits:

- Main thread work from third parties drops, which can improve TBT and INP.
- You can control which DOM APIs a script can access.

Costs and risks:

- **Every DOM access becomes slow**, since it crosses threads. Scripts that touch the DOM a lot (A/B testing tools, chat widgets, heatmaps) can become very slow or break.
- **Compatibility**: some scripts don't work, and vendors may not support this setup. Each script needs testing, and updates from the vendor can break it without warning.
- **Timing changes**: scripts may run later than intended, which can affect data accuracy (missed early events) or cause flicker for scripts that modify the page.
- **Complexity**: needs a Service Worker or cross-origin isolation headers, and makes debugging harder.

It is a reasonable option for simple, "fire and forget" scripts like analytics beacons. For scripts that change the visible page, it's usually better to delay, use a facade, or remove them. Often the simplest win is to remove or replace heavy tags altogether, or move tracking to the server side.

#### 445: How do SSR streaming, React Server Components and selective hydration affect Core Web Vitals?

- **Streaming SSR** sends the shell (`<head>`, layout, critical CSS) right away and streams slower parts later. TTFB and FCP improve because the browser starts working early, and LCP improves if the LCP element is in an early chunk. If the LCP element is inside a slow `Suspense` boundary, LCP waits for that data, so keep LCP content outside slow boundaries or make its data fast.
- **React Server Components** keep server-only components out of the client bundle. Less JavaScript means less parse, compile and hydration time, which helps INP and TBT, especially on low-end phones. The RSC payload (serialized component tree) is sent along with the HTML and also costs bytes and parse time, so very large server-rendered trees still have a cost.
- **Selective hydration** hydrates `Suspense` boundaries independently and prioritizes the one the user interacts with. A click on a not-yet-hydrated part makes React hydrate it first. This reduces the "page looks ready but doesn't respond" window, improving INP during load. Hydration is still main-thread work, though, so large boundaries still create long tasks.
- **CLS risks**: streamed content that replaces fallbacks with content of a different size causes layout shifts. Make Suspense fallbacks the same size as the final content.
- **Caching**: streamed, personalized responses are harder to cache at the CDN. Separating static shells (cacheable) from dynamic parts (streamed or fetched) keeps TTFB low.

Measure with RUM after rollout. Results depend heavily on how boundaries are placed and how much client-side JavaScript remains.

#### 446: How would you design a RUM pipeline that gives accurate percentiles without huge cost?

Collection in the browser:

- Use `web-vitals` (attribution build for debugging data) and report on `visibilitychange` to hidden (and `pagehide`) using `navigator.sendBeacon` or `fetch` with `keepalive`, since many page views end without an `unload`.
- Batch all metrics of a page view into one beacon where possible.
- Add context fields: route template, device class, effective connection type, country (from the server), navigation type, app version, and experiment variants.
- Sample at the page-view level (for example 10% of sessions), and record the sample rate so you can weight results. Never sample individual metrics differently within a page view, or correlations break.

Ingestion and storage:

- Accept beacons at an edge endpoint, validate and enrich them, and write to a queue or stream, then to a columnar store (ClickHouse, BigQuery, or a RUM vendor).
- Drop or bucket high-cardinality values (full URLs, raw user agents) at ingestion.

Analysis:

- Compute percentiles over raw values or with mergeable sketches (t-digest, DDSketch, HDR histograms) so you can aggregate across time and segments correctly. Never average percentiles.
- Report p75 to match CrUX and p95 for tails, with sample counts.
- Build regression detection per release and per route.

Privacy and cost: avoid personal data in beacons, respect consent rules, and keep raw data retention short with longer-lived aggregates.

#### 447: How do you run a performance budget program across several teams?

- **Define budgets per surface that teams own**: for example per route or per micro-frontend, covering JS bytes, LCP and INP targets in RUM, and Lighthouse lab thresholds for key pages.
- **Automate enforcement where signals are reliable**: bundle size checks and Lighthouse CI assertions in each team's pull requests. Block merges for clear regressions; warn for noisy metrics.
- **Attribute regressions**: tag RUM data with release versions and feature flags, and keep a dashboard per team. When a field metric worsens, check which deploys landed in that window and which routes are affected. Bundle analysis per pull request shows who added which bytes.
- **Make the cost visible**: show the impact of each new dependency or third-party tag in the pull request ("this adds 42 KB gzip to the checkout route").
- **Exception process**: allow temporary budget increases with an owner and an expiry date, so budgets don't just get raised silently.
- **Shared ownership for shared code**: design systems, frameworks and third-party tags need a clear owner too, since they affect everyone.
- **Review regularly**: a monthly review of trends, top offenders and wins, with product managers involved, keeps budgets tied to business goals.
- **Celebrate improvements**, not just failures, so teams see performance work as valued.

#### 448: How do you connect performance improvements to business metrics in a trustworthy way?

Correlation from dashboards ("fast sessions convert better") is misleading, because fast sessions also tend to be on better devices and networks, and those users may convert more anyway.

More reliable approaches:

- **A/B test the performance change itself**: ship the optimization to a random half of users (via a feature flag) and compare conversion, engagement and revenue. Make sure the test measures the performance difference too, so you know the treatment really was faster.
- **Slowdown experiments**: deliberately add small delays for a small share of users (some large companies have done this) to measure sensitivity. It needs careful ethics and product approval.
- **Natural experiments**: compare before and after a rollout across regions that were deployed at different times, using difference-in-differences to control for seasonality.
- **Segment carefully**: compare users on the same device class and network type, and look at the relationship within segments.
- **Use enough data and a pre-defined metric**: decide the primary metric and sample size before the test to avoid fishing for results.

Report results with confidence intervals, not single numbers, and connect them to the metric the business already tracks (conversion rate, bounce rate, ad revenue per session, task completion).

#### 449: How are accessibility and performance connected beyond reduced motion?

- **Large DOMs hurt assistive technology too**: browsers build an accessibility tree from the DOM, and screen readers query it. Huge DOMs and frequent large changes make the browser update that tree constantly, which can make screen readers lag. Virtualization reduces the work but needs correct ARIA (`aria-rowcount`, `aria-setsize`, `aria-posinset`) so screen readers still understand the list.
- **Live regions** (`aria-live`) that update very often (for example a ticker updating every 100 ms) flood screen readers and cost processing time. Throttle them and announce only meaningful changes.
- **Focus management**: moving focus with `focus()` can force layout and scroll. Do it once after rendering, and use `focus({ preventScroll: true })` when you handle scrolling yourself.
- **`content-visibility: auto`** keeps skipped content in the accessibility tree, which is good, but some headings or landmarks may report incorrect sizes. Test with a screen reader.
- **Keyboard and slow-device users** experience INP the same way: every key press is an interaction. Heavy keydown handlers in forms or editors hurt users who navigate entirely with the keyboard.
- **Native elements are faster and more accessible**: `<dialog>`, `<details>`, the Popover API and native form controls need less JavaScript than custom versions and come with correct semantics.
- **Zoom and reflow**: responsive layouts that work at 400% zoom without horizontal scroll often avoid fixed-size, expensive layout tricks.
- **Respect user preferences** like `prefers-reduced-motion`, `prefers-reduced-data` (where supported), and `prefers-contrast`, which can also reduce work.

#### 450: Users in one region report the site is slow, but your dashboards look fine. Walk through how you would debug it end to end.

1. **Confirm and scope it with field data**: filter RUM by country or region, device type and route. Compare LCP, INP and TTFB p75 against other regions. Check CrUX for that country if you have enough traffic. Find out when it started.
2. **Split by metric**: if **TTFB** is bad, the problem is network or backend. If TTFB is fine but **LCP** is bad, it's resource loading. If **INP** is bad, it's client-side work, which might come from a region-specific script (a local payment widget, a consent banner for that region's laws, or a different ad provider).
3. **Check the network path**: run WebPageTest from a location in that region. Look at DNS, connect and TLS times. Check which CDN edge served the request (response headers like `x-amz-cf-pop` or `cf-ray`). Users may be routed to a far edge because of DNS or anycast routing problems, or a local ISP may have poor peering with your CDN.
4. **Check CDN behavior per region**: cache hit ratio for that region's edges, origin fetch times from that edge, and whether a regional edge cache or shield is missing.
5. **Check the backend**: if dynamic requests are slow only from that region, look at ALB logs or traces filtered by client geography. Are those users served by a far-away region? Does their traffic hit a different backend (data residency, a regional database replica that's lagging or under-sized)?
6. **Check region-specific content**: localized pages may have bigger images, different fonts (for example, large CJK or Georgian font files without subsetting), extra third-party tags, or different A/B tests.
7. **Check devices and networks**: some regions have more low-end phones and slower mobile networks. Your global p75 may hide that. Test with matching throttling and a real low-end device.
8. **Form a hypothesis, fix one thing, and measure**: for example, add font subsetting, change CDN configuration, or add a regional replica. Watch the regional RUM p75 over the following days, and keep the regional breakdown on your dashboards so it doesn't go unnoticed again.
