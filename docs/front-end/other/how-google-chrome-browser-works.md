# How Google Chrome Browser Works Interview Questions and Answers

_Last updated: October 28, 2026_

450 interview questions with answers about how Google Chrome works under the hood, split into three levels: 150 easy, 150 moderate and 150 advanced.

The answers describe Chrome as of late 2026 (around Chrome 155), now on a two-week release cycle. They cover the multi-process architecture, navigation and networking, the rendering pipeline (RenderingNG, LayoutNG, the compositor and Viz), V8 (Ignition, Sparkplug, Maglev, TurboFan) and garbage collection, the page lifecycle, performance tooling, and security (the sandbox and Site Isolation). Older behavior is mentioned where you will still run into it.

## Table of Contents

- [Easy Questions (1-150)](#easy-questions-1-150)
- [Moderate Questions (151-300)](#moderate-questions-151-300)
- [Advanced Questions (301-450)](#advanced-questions-301-450)

### Easy Questions (1-150)

- [1: What is a web browser and what does it actually do?](#1-what-is-a-web-browser-and-what-does-it-actually-do)
- [2: What is the difference between Chromium and Google Chrome?](#2-what-is-the-difference-between-chromium-and-google-chrome)
- [3: What is Blink?](#3-what-is-blink)
- [4: What is V8?](#4-what-is-v8)
- [5: What are the main parts of a browser?](#5-what-are-the-main-parts-of-a-browser)
- [6: Which rendering engines exist besides Blink?](#6-which-rendering-engines-exist-besides-blink)
- [7: What happens at a high level when you type a URL and press Enter?](#7-what-happens-at-a-high-level-when-you-type-a-url-and-press-enter)
- [8: How does the address bar (Omnibox) decide whether you typed a URL or a search?](#8-how-does-the-address-bar-omnibox-decide-whether-you-typed-a-url-or-a-search)
- [9: What is the difference between a process and a thread?](#9-what-is-the-difference-between-a-process-and-a-thread)
- [10: Why does Chrome use multiple processes?](#10-why-does-chrome-use-multiple-processes)
- [11: What is the browser process?](#11-what-is-the-browser-process)
- [12: What is a renderer process?](#12-what-is-a-renderer-process)
- [13: What is the GPU process?](#13-what-is-the-gpu-process)
- [14: What is the network service in Chrome?](#14-what-is-the-network-service-in-chrome)
- [15: What are utility processes?](#15-what-are-utility-processes)
- [16: How do Chrome extensions run in terms of processes?](#16-how-do-chrome-extensions-run-in-terms-of-processes)
- [17: How do you see which processes Chrome is running?](#17-how-do-you-see-which-processes-chrome-is-running)
- [18: What does the "Aw, Snap!" page mean?](#18-what-does-the-aw-snap-page-mean)
- [19: What is the sandbox in Chrome?](#19-what-is-the-sandbox-in-chrome)
- [20: What is Site Isolation?](#20-what-is-site-isolation)
- [21: What is the difference between an origin and a site?](#21-what-is-the-difference-between-an-origin-and-a-site)
- [22: What happens during a DNS lookup?](#22-what-happens-during-a-dns-lookup)
- [23: How do you see or clear Chrome's DNS cache?](#23-how-do-you-see-or-clear-chromes-dns-cache)
- [24: What is the TCP handshake?](#24-what-is-the-tcp-handshake)
- [25: What happens during a TLS handshake?](#25-what-happens-during-a-tls-handshake)
- [26: How does Chrome check that an HTTPS certificate is valid?](#26-how-does-chrome-check-that-an-https-certificate-is-valid)
- [27: What does an HTTP request and response contain?](#27-what-does-an-http-request-and-response-contain)
- [28: What is the difference between HTTP/1.1, HTTP/2 and HTTP/3?](#28-what-is-the-difference-between-http11-http2-and-http3)
- [29: What is QUIC?](#29-what-is-quic)
- [30: What is the HTTP cache?](#30-what-is-the-http-cache)
- [31: What do common Cache-Control values mean?](#31-what-do-common-cache-control-values-mean)
- [32: What is the DOM?](#32-what-is-the-dom)
- [33: How does the browser parse HTML?](#33-how-does-the-browser-parse-html)
- [34: Why does a broken HTML file still display?](#34-why-does-a-broken-html-file-still-display)
- [35: What is the CSSOM?](#35-what-is-the-cssom)
- [36: What is style calculation?](#36-what-is-style-calculation)
- [37: What is the layout tree (render tree)?](#37-what-is-the-layout-tree-render-tree)
- [38: What is layout?](#38-what-is-layout)
- [39: What is paint?](#39-what-is-paint)
- [40: What is compositing?](#40-what-is-compositing)
- [41: What is the critical rendering path?](#41-what-is-the-critical-rendering-path)
- [42: What is a render-blocking resource?](#42-what-is-a-render-blocking-resource)
- [43: What is a parser-blocking script?](#43-what-is-a-parser-blocking-script)
- [44: What is the difference between async and defer on a script?](#44-what-is-the-difference-between-async-and-defer-on-a-script)
- [45: How do module scripts load by default?](#45-how-do-module-scripts-load-by-default)
- [46: What is the preload scanner?](#46-what-is-the-preload-scanner)
- [47: What is reflow and what triggers it?](#47-what-is-reflow-and-what-triggers-it)
- [48: What is repaint?](#48-what-is-repaint)
- [49: Which CSS properties are cheapest to animate and why?](#49-which-css-properties-are-cheapest-to-animate-and-why)
- [50: What is the main thread in a renderer process?](#50-what-is-the-main-thread-in-a-renderer-process)
- [51: What is the event loop in the browser?](#51-what-is-the-event-loop-in-the-browser)
- [52: What is the difference between tasks and microtasks?](#52-what-is-the-difference-between-tasks-and-microtasks)
- [53: What is requestAnimationFrame?](#53-what-is-requestanimationframe)
- [54: What is a frame and what does 60 fps mean for the browser?](#54-what-is-a-frame-and-what-does-60-fps-mean-for-the-browser)
- [55: What is jank?](#55-what-is-jank)
- [56: What is a long task?](#56-what-is-a-long-task)
- [57: What is a Web Worker and how does it relate to browser threads?](#57-what-is-a-web-worker-and-how-does-it-relate-to-browser-threads)
- [58: What is a Service Worker?](#58-what-is-a-service-worker)
- [59: What is the call stack?](#59-what-is-the-call-stack)
- [60: What is the heap in V8?](#60-what-is-the-heap-in-v8)
- [61: What is garbage collection?](#61-what-is-garbage-collection)
- [62: What are common causes of memory leaks on a web page?](#62-what-are-common-causes-of-memory-leaks-on-a-web-page)
- [63: What is JIT compilation?](#63-what-is-jit-compilation)
- [64: What is the difference between an interpreter and a compiler in V8?](#64-what-is-the-difference-between-an-interpreter-and-a-compiler-in-v8)
- [65: What is Ignition?](#65-what-is-ignition)
- [66: What does V8 do with JavaScript source code before running it?](#66-what-does-v8-do-with-javascript-source-code-before-running-it)
- [67: What are cookies and how does the browser handle them?](#67-what-are-cookies-and-how-does-the-browser-handle-them)
- [68: What is the difference between localStorage and sessionStorage?](#68-what-is-the-difference-between-localstorage-and-sessionstorage)
- [69: What is IndexedDB?](#69-what-is-indexeddb)
- [70: What is the Cache Storage API?](#70-what-is-the-cache-storage-api)
- [71: What is the same-origin policy?](#71-what-is-the-same-origin-policy)
- [72: What is CORS?](#72-what-is-cors)
- [73: What is Safe Browsing?](#73-what-is-safe-browsing)
- [74: What does Incognito mode actually do?](#74-what-does-incognito-mode-actually-do)
- [75: What is a Chrome profile?](#75-what-is-a-chrome-profile)
- [76: What is Manifest V3 for Chrome extensions?](#76-what-is-manifest-v3-for-chrome-extensions)
- [77: What are Chrome DevTools?](#77-what-are-chrome-devtools)
- [78: What are chrome:// pages and which ones are useful?](#78-what-are-chrome-pages-and-which-ones-are-useful)
- [79: What is chrome://flags and should you rely on it?](#79-what-is-chromeflags-and-should-you-rely-on-it)
- [80: What are Chrome's release channels?](#80-what-are-chromes-release-channels)
- [81: How often does Chrome release a new version?](#81-how-often-does-chrome-release-a-new-version)
- [82: How does Chrome update itself?](#82-how-does-chrome-update-itself)
- [83: What is the Chrome DevTools Protocol (CDP)?](#83-what-is-the-chrome-devtools-protocol-cdp)
- [84: What is headless Chrome?](#84-what-is-headless-chrome)
- [85: What is the User-Agent string and what is UA reduction?](#85-what-is-the-user-agent-string-and-what-is-ua-reduction)
- [86: What is the back/forward cache (bfcache)?](#86-what-is-the-backforward-cache-bfcache)
- [87: What are the page lifecycle states?](#87-what-are-the-page-lifecycle-states)
- [88: How do you detect when a user switches away from your tab?](#88-how-do-you-detect-when-a-user-switches-away-from-your-tab)
- [89: How does Chrome throttle background tabs?](#89-how-does-chrome-throttle-background-tabs)
- [90: What is Memory Saver?](#90-what-is-memory-saver)
- [91: What is Energy Saver?](#91-what-is-energy-saver)
- [92: What is hardware acceleration in Chrome?](#92-what-is-hardware-acceleration-in-chrome)
- [93: What is Skia?](#93-what-is-skia)
- [94: How does the browser load web fonts?](#94-how-does-the-browser-load-web-fonts)
- [95: How does native lazy loading work for images and iframes?](#95-how-does-native-lazy-loading-work-for-images-and-iframes)
- [96: What does the viewport meta tag do?](#96-what-does-the-viewport-meta-tag-do)
- [97: What is an iframe from the browser's point of view?](#97-what-is-an-iframe-from-the-browsers-point-of-view)
- [98: What are resource hints like preconnect, dns-prefetch, preload and prefetch?](#98-what-are-resource-hints-like-preconnect-dns-prefetch-preload-and-prefetch)
- [99: How does the browser handle redirects?](#99-how-does-the-browser-handle-redirects)
- [100: What is mixed content?](#100-what-is-mixed-content)
- [101: What is HSTS?](#101-what-is-hsts)
- [102: What is Content Security Policy?](#102-what-is-content-security-policy)
- [103: How does Chrome's popup blocker decide what to block?](#103-how-does-chromes-popup-blocker-decide-what-to-block)
- [104: How do site permissions work in Chrome?](#104-how-do-site-permissions-work-in-chrome)
- [105: How does Chrome autofill forms?](#105-how-does-chrome-autofill-forms)
- [106: What is WebAssembly and how does Chrome run it?](#106-what-is-webassembly-and-how-does-chrome-run-it)
- [107: What are WebGL and WebGPU?](#107-what-are-webgl-and-webgpu)
- [108: What is the difference between JavaScript and Web APIs?](#108-what-is-the-difference-between-javascript-and-web-apis)
- [109: What are Core Web Vitals?](#109-what-are-core-web-vitals)
- [110: What is LCP?](#110-what-is-lcp)
- [111: What is INP?](#111-what-is-inp)
- [112: What is CLS?](#112-what-is-cls)
- [113: What are TTFB and FCP?](#113-what-are-ttfb-and-fcp)
- [114: What is Lighthouse?](#114-what-is-lighthouse)
- [115: What does the DevTools Performance panel show?](#115-what-does-the-devtools-performance-panel-show)
- [116: How do you read the Network panel waterfall?](#116-how-do-you-read-the-network-panel-waterfall)
- [117: What is the difference between DOMContentLoaded and load?](#117-what-is-the-difference-between-domcontentloaded-and-load)
- [118: What is a same-document navigation?](#118-what-is-a-same-document-navigation)
- [119: What is the difference between standards mode and quirks mode?](#119-what-is-the-difference-between-standards-mode-and-quirks-mode)
- [120: What is the accessibility tree?](#120-what-is-the-accessibility-tree)
- [121: How does the browser handle Shadow DOM?](#121-how-does-the-browser-handle-shadow-dom)
- [122: How does Chrome show PDF files?](#122-how-does-chrome-show-pdf-files)
- [123: How does Chrome play video?](#123-how-does-chrome-play-video)
- [124: What are blob URLs and data URLs?](#124-what-are-blob-urls-and-data-urls)
- [125: What is FOUC?](#125-what-is-fouc)
- [126: What happens when you close a tab?](#126-what-happens-when-you-close-a-tab)
- [127: Does every tab get its own process?](#127-does-every-tab-get-its-own-process)
- [128: How does scrolling work at a basic level?](#128-how-does-scrolling-work-at-a-basic-level)
- [129: What image formats does Chrome support and why does it matter?](#129-what-image-formats-does-chrome-support-and-why-does-it-matter)
- [130: What is a browser-initiated vs a renderer-initiated navigation?](#130-what-is-a-browser-initiated-vs-a-renderer-initiated-navigation)
- [131: What does the beforeunload event do?](#131-what-does-the-beforeunload-event-do)
- [132: What is the user agent stylesheet?](#132-what-is-the-user-agent-stylesheet)
- [133: What is the difference between display: none, visibility: hidden and opacity: 0 for rendering?](#133-what-is-the-difference-between-display-none-visibility-hidden-and-opacity-0-for-rendering)
- [134: What is HTTP compression and which formats does Chrome support?](#134-what-is-http-compression-and-which-formats-does-chrome-support)
- [135: What is the difference between a normal reload, a hard reload and "Empty cache and hard reload"?](#135-what-is-the-difference-between-a-normal-reload-a-hard-reload-and-empty-cache-and-hard-reload)
- [136: What is HTTP keep-alive and connection reuse?](#136-what-is-http-keep-alive-and-connection-reuse)
- [137: What language is Chrome written in?](#137-what-language-is-chrome-written-in)
- [138: What is a Progressive Web App from the browser's point of view?](#138-what-is-a-progressive-web-app-from-the-browsers-point-of-view)
- [139: What is a stacking context?](#139-what-is-a-stacking-context)
- [140: What does Chrome do when a page uses too much memory?](#140-what-does-chrome-do-when-a-page-uses-too-much-memory)
- [141: How does Chrome handle a page that is not responding?](#141-how-does-chrome-handle-a-page-that-is-not-responding)
- [142: What is the difference between a tab, a window and a frame in Chrome?](#142-what-is-the-difference-between-a-tab-a-window-and-a-frame-in-chrome)
- [143: What is the difference between the window object and the document object?](#143-what-is-the-difference-between-the-window-object-and-the-document-object)
- [144: How much data can a site store in Chrome?](#144-how-much-data-can-a-site-store-in-chrome)
- [145: What is a secure context?](#145-what-is-a-secure-context)
- [146: What is the difference between the memory cache and the disk cache?](#146-what-is-the-difference-between-the-memory-cache-and-the-disk-cache)
- [147: How does Chrome decide the order in which to download resources?](#147-how-does-chrome-decide-the-order-in-which-to-download-resources)
- [148: Why is it bad to use document.write?](#148-why-is-it-bad-to-use-documentwrite)
- [149: What happens when JavaScript throws an uncaught error?](#149-what-happens-when-javascript-throws-an-uncaught-error)
- [150: What is the difference between innerHTML and textContent for the browser?](#150-what-is-the-difference-between-innerhtml-and-textcontent-for-the-browser)

### Moderate Questions (151-300)

- [151: Walk through a navigation in Chrome step by step, process by process.](#151-walk-through-a-navigation-in-chrome-step-by-step-process-by-process)
- [152: Why does Chrome start a renderer process before the network response arrives?](#152-why-does-chrome-start-a-renderer-process-before-the-network-response-arrives)
- [153: What is Mojo?](#153-what-is-mojo)
- [154: What is the network service's relation to the renderer when you call fetch()?](#154-what-is-the-network-services-relation-to-the-renderer-when-you-call-fetch)
- [155: How does Chrome decide which renderer process to use for a navigation?](#155-how-does-chrome-decide-which-renderer-process-to-use-for-a-navigation)
- [156: What is a browsing context group and why does it matter for processes?](#156-what-is-a-browsing-context-group-and-why-does-it-matter-for-processes)
- [157: What is an out-of-process iframe (OOPIF)?](#157-what-is-an-out-of-process-iframe-oopif)
- [158: What is a RenderFrameHost and a RenderFrame?](#158-what-is-a-renderframehost-and-a-renderframe)
- [159: What is MIME sniffing and how does Chrome use it?](#159-what-is-mime-sniffing-and-how-does-chrome-use-it)
- [160: How does speculative parsing interact with document.write?](#160-how-does-speculative-parsing-interact-with-documentwrite)
- [161: Why does CSS block JavaScript execution?](#161-why-does-css-block-javascript-execution)
- [162: How does selector matching work and why is it right to left?](#162-how-does-selector-matching-work-and-why-is-it-right-to-left)
- [163: What is style invalidation?](#163-what-is-style-invalidation)
- [164: What is layout thrashing (forced synchronous layout)?](#164-what-is-layout-thrashing-forced-synchronous-layout)
- [165: Which DOM properties and methods force layout?](#165-which-dom-properties-and-methods-force-layout)
- [166: What is LayoutNG?](#166-what-is-layoutng)
- [167: What is the fragment tree?](#167-what-is-the-fragment-tree)
- [168: What are paint records and display items?](#168-what-are-paint-records-and-display-items)
- [169: What is raster?](#169-what-is-raster)
- [170: What is the compositor thread?](#170-what-is-the-compositor-thread)
- [171: What makes an element get its own compositor layer?](#171-what-makes-an-element-get-its-own-compositor-layer)
- [172: What does will-change do and when should you use it?](#172-what-does-will-change-do-and-when-should-you-use-it)
- [173: What is layer explosion?](#173-what-is-layer-explosion)
- [174: Why are transform and opacity animations "compositor-only"?](#174-why-are-transform-and-opacity-animations-compositor-only)
- [175: What are passive event listeners and why do they help scrolling?](#175-what-are-passive-event-listeners-and-why-do-they-help-scrolling)
- [176: What is the non-fast scrollable region?](#176-what-is-the-non-fast-scrollable-region)
- [177: How does an input event travel from the OS to your JavaScript handler?](#177-how-does-an-input-event-travel-from-the-os-to-your-javascript-handler)
- [178: What is the touch-action CSS property?](#178-what-is-the-touch-action-css-property)
- [179: In what order does the browser do work within one frame?](#179-in-what-order-does-the-browser-do-work-within-one-frame)
- [180: What is VSync?](#180-what-is-vsync)
- [181: What is Viz?](#181-what-is-viz)
- [182: What is a compositor frame?](#182-what-is-a-compositor-frame)
- [183: What is content-visibility and how does it help rendering?](#183-what-is-content-visibility-and-how-does-it-help-rendering)
- [184: What is CSS containment?](#184-what-is-css-containment)
- [185: How does Chrome decode images and why can it be slow?](#185-how-does-chrome-decode-images-and-why-can-it-be-slow)
- [186: How many connections does Chrome open per host?](#186-how-many-connections-does-chrome-open-per-host)
- [187: What is HTTP/2 connection coalescing?](#187-what-is-http2-connection-coalescing)
- [188: How does Chrome find out a server supports HTTP/3?](#188-how-does-chrome-find-out-a-server-supports-http3)
- [189: What are 103 Early Hints?](#189-what-are-103-early-hints)
- [190: What is HTTP cache partitioning?](#190-what-is-http-cache-partitioning)
- [191: What is storage partitioning?](#191-what-is-storage-partitioning)
- [192: What is CHIPS?](#192-what-is-chips)
- [193: What is the current status of third-party cookies in Chrome?](#193-what-is-the-current-status-of-third-party-cookies-in-chrome)
- [194: How does the SameSite cookie attribute work?](#194-how-does-the-samesite-cookie-attribute-work)
- [195: What is the difference between same-site and cross-site requests for cookies?](#195-what-is-the-difference-between-same-site-and-cross-site-requests-for-cookies)
- [196: What is a CORS preflight request?](#196-what-is-a-cors-preflight-request)
- [197: What is Opaque Response Blocking (ORB)?](#197-what-is-opaque-response-blocking-orb)
- [198: What are COOP and COEP?](#198-what-are-coop-and-coep)
- [199: What does cross-origin isolation unlock?](#199-what-does-cross-origin-isolation-unlock)
- [200: Why was document.domain deprecated?](#200-why-was-documentdomain-deprecated)
- [201: What makes a page ineligible for the bfcache?](#201-what-makes-a-page-ineligible-for-the-bfcache)
- [202: How do you detect that a page was restored from the bfcache?](#202-how-do-you-detect-that-a-page-was-restored-from-the-bfcache)
- [203: Why is the unload event being deprecated in Chrome?](#203-why-is-the-unload-event-being-deprecated-in-chrome)
- [204: What happens to a page when Chrome freezes it?](#204-what-happens-to-a-page-when-chrome-freezes-it)
- [205: How does Chrome clamp timers?](#205-how-does-chrome-clamp-timers)
- [206: How can you yield to the browser in the middle of a long task?](#206-how-can-you-yield-to-the-browser-in-the-middle-of-a-long-task)
- [207: What is scheduler.postTask()?](#207-what-is-schedulerposttask)
- [208: What is the Long Animation Frames API?](#208-what-is-the-long-animation-frames-api)
- [209: How is INP broken down and what causes each part to be slow?](#209-how-is-inp-broken-down-and-what-causes-each-part-to-be-slow)
- [210: How do you measure Web Vitals in real users?](#210-how-do-you-measure-web-vitals-in-real-users)
- [211: What can be an LCP element?](#211-what-can-be-an-lcp-element)
- [212: How does CLS group layout shifts?](#212-how-does-cls-group-layout-shifts)
- [213: What are hidden classes (shapes or maps) in V8?](#213-what-are-hidden-classes-shapes-or-maps-in-v8)
- [214: What are inline caches in V8?](#214-what-are-inline-caches-in-v8)
- [215: What do monomorphic, polymorphic and megamorphic mean?](#215-what-do-monomorphic-polymorphic-and-megamorphic-mean)
- [216: What is Sparkplug?](#216-what-is-sparkplug)
- [217: What is Maglev?](#217-what-is-maglev)
- [218: What is TurboFan?](#218-what-is-turbofan)
- [219: What is deoptimization?](#219-what-is-deoptimization)
- [220: What is on-stack replacement (OSR)?](#220-what-is-on-stack-replacement-osr)
- [221: How does V8's code cache work in Chrome?](#221-how-does-v8s-code-cache-work-in-chrome)
- [222: What is lazy parsing in V8?](#222-what-is-lazy-parsing-in-v8)
- [223: How does V8's garbage collector work at a high level?](#223-how-does-v8s-garbage-collector-work-at-a-high-level)
- [224: What is Oilpan?](#224-what-is-oilpan)
- [225: How do you find a memory leak with DevTools?](#225-how-do-you-find-a-memory-leak-with-devtools)
- [226: What is the difference between shallow size and retained size in a heap snapshot?](#226-what-is-the-difference-between-shallow-size-and-retained-size-in-a-heap-snapshot)
- [227: What is a detached DOM node?](#227-what-is-a-detached-dom-node)
- [228: What are WeakRef and FinalizationRegistry, and should you use them?](#228-what-are-weakref-and-finalizationregistry-and-should-you-use-them)
- [229: What is a V8 isolate and a context?](#229-what-is-a-v8-isolate-and-a-context)
- [230: What is an isolated world?](#230-what-is-an-isolated-world)
- [231: What is the Service Worker lifecycle?](#231-what-is-the-service-worker-lifecycle)
- [232: How does Chrome check for Service Worker updates?](#232-how-does-chrome-check-for-service-worker-updates)
- [233: What is navigation preload?](#233-what-is-navigation-preload)
- [234: What are Speculation Rules?](#234-what-are-speculation-rules)
- [235: How do you write code that behaves correctly when a page is prerendered?](#235-how-do-you-write-code-that-behaves-correctly-when-a-page-is-prerendered)
- [236: What is the Navigation API?](#236-what-is-the-navigation-api)
- [237: What are View Transitions?](#237-what-are-view-transitions)
- [238: How do you record a trace with chrome://tracing or Perfetto?](#238-how-do-you-record-a-trace-with-chrometracing-or-perfetto)
- [239: How do you debug network problems with chrome://net-export?](#239-how-do-you-debug-network-problems-with-chromenet-export)
- [240: How do you debug Chrome on Android from a desktop?](#240-how-do-you-debug-chrome-on-android-from-a-desktop)
- [241: How do you automate Chrome with Puppeteer?](#241-how-do-you-automate-chrome-with-puppeteer)
- [242: What are worklets?](#242-what-are-worklets)
- [243: What is OffscreenCanvas?](#243-what-is-offscreencanvas)
- [244: What is Chrome's autoplay policy?](#244-what-is-chromes-autoplay-policy)
- [245: How does Chrome render text?](#245-how-does-chrome-render-text)
- [246: What are Trusted Types?](#246-what-are-trusted-types)
- [247: What is Permissions Policy?](#247-what-is-permissions-policy)
- [248: What is HTTPS-First mode?](#248-what-is-https-first-mode)
- [249: What is DNS over HTTPS in Chrome?](#249-what-is-dns-over-https-in-chrome)
- [250: What are Fetch Metadata headers?](#250-what-are-fetch-metadata-headers)
- [251: What does chrome://gpu tell you?](#251-what-does-chromegpu-tell-you)
- [252: What happens when the GPU is not available or blocklisted?](#252-what-happens-when-the-gpu-is-not-available-or-blocklisted)
- [253: What is ANGLE?](#253-what-is-angle)
- [254: What is Dawn?](#254-what-is-dawn)
- [255: How does Chrome connect when a host has both IPv4 and IPv6 addresses?](#255-how-does-chrome-connect-when-a-host-has-both-ipv4-and-ipv6-addresses)
- [256: How does TLS session resumption help performance?](#256-how-does-tls-session-resumption-help-performance)
- [257: What is the Chrome Root Store?](#257-what-is-the-chrome-root-store)
- [258: How long does a Manifest V3 extension service worker stay alive?](#258-how-long-does-a-manifest-v3-extension-service-worker-stay-alive)
- [259: What is declarativeNetRequest?](#259-what-is-declarativenetrequest)
- [260: When do content scripts run?](#260-when-do-content-scripts-run)
- [261: How do the parts of an extension talk to each other?](#261-how-do-the-parts-of-an-extension-talk-to-each-other)
- [262: How does Chrome choose which tab to discard?](#262-how-does-chrome-choose-which-tab-to-discard)
- [263: What is Media Source Extensions?](#263-what-is-media-source-extensions)
- [264: What is EME and Widevine?](#264-what-is-eme-and-widevine)
- [265: What is WebCodecs?](#265-what-is-webcodecs)
- [266: What is requestIdleCallback and when should you use it?](#266-what-is-requestidlecallback-and-when-should-you-use-it)
- [267: Why use IntersectionObserver instead of scroll events?](#267-why-use-intersectionobserver-instead-of-scroll-events)
- [268: When do ResizeObserver callbacks run?](#268-when-do-resizeobserver-callbacks-run)
- [269: When do MutationObserver callbacks run?](#269-when-do-mutationobserver-callbacks-run)
- [270: What are scroll-driven animations and why are they efficient?](#270-what-are-scroll-driven-animations-and-why-are-they-efficient)
- [271: What is the difference between CSS animations, the Web Animations API and JavaScript rAF animations?](#271-what-is-the-difference-between-css-animations-the-web-animations-api-and-javascript-raf-animations)
- [272: How does position: sticky work in the rendering pipeline?](#272-how-does-position-sticky-work-in-the-rendering-pipeline)
- [273: Why does a large DOM slow down rendering?](#273-why-does-a-large-dom-slow-down-rendering)
- [274: What does the DevTools Rendering tab offer?](#274-what-does-the-devtools-rendering-tab-offer)
- [275: What is the Coverage tab in DevTools?](#275-what-is-the-coverage-tab-in-devtools)
- [276: What is the difference between lab data and field data?](#276-what-is-the-difference-between-lab-data-and-field-data)
- [277: What is the Chrome UX Report (CrUX)?](#277-what-is-the-chrome-ux-report-crux)
- [278: Why is measuring performance in single-page apps tricky?](#278-why-is-measuring-performance-in-single-page-apps-tricky)
- [279: Why can a preload cause a double download?](#279-why-can-a-preload-cause-a-double-download)
- [280: How does Chrome pick an image from srcset and sizes?](#280-how-does-chrome-pick-an-image-from-srcset-and-sizes)
- [281: How can you adjust fallback fonts to reduce layout shift?](#281-how-can-you-adjust-fallback-fonts-to-reduce-layout-shift)
- [282: What are origin trials?](#282-what-are-origin-trials)
- [283: How does a new feature get added to Chrome?](#283-how-does-a-new-feature-get-added-to-chrome)
- [284: What are Web Platform Tests?](#284-what-are-web-platform-tests)
- [285: What is Local Network Access?](#285-what-is-local-network-access)
- [286: What is the difference between WebSockets and WebTransport?](#286-what-is-the-difference-between-websockets-and-webtransport)
- [287: What is the Service Worker Static Routing API?](#287-what-is-the-service-worker-static-routing-api)
- [288: How do tabs of the same origin talk to each other?](#288-how-do-tabs-of-the-same-origin-talk-to-each-other)
- [289: What is a SharedWorker?](#289-what-is-a-sharedworker)
- [290: How does Chrome evict site data when disk space is low?](#290-how-does-chrome-evict-site-data-when-disk-space-is-low)
- [291: What is the Storage Access API?](#291-what-is-the-storage-access-api)
- [292: What is FedCM?](#292-what-is-fedcm)
- [293: How do passkeys work in Chrome?](#293-how-do-passkeys-work-in-chrome)
- [294: What is the Web Locks API?](#294-what-is-the-web-locks-api)
- [295: How does the Async Clipboard API work in Chrome?](#295-how-does-the-async-clipboard-api-work-in-chrome)
- [296: How do you profile JavaScript CPU usage in Chrome?](#296-how-do-you-profile-javascript-cpu-usage-in-chrome)
- [297: What are DevTools local overrides?](#297-what-are-devtools-local-overrides)
- [298: What is the Save-Data header?](#298-what-is-the-save-data-header)
- [299: How does Chrome handle `<link rel="modulepreload">`?](#299-how-does-chrome-handle-link-relmodulepreload)
- [300: How does the browser handle a 304 Not Modified response?](#300-how-does-the-browser-handle-a-304-not-modified-response)

### Advanced Questions (301-450)

- [301: What is RenderingNG?](#301-what-is-renderingng)
- [302: List the stages of Chrome's rendering pipeline and the thread each runs on.](#302-list-the-stages-of-chromes-rendering-pipeline-and-the-thread-each-runs-on)
- [303: What are property trees?](#303-what-are-property-trees)
- [304: What is CompositeAfterPaint and why did it matter?](#304-what-is-compositeafterpaint-and-why-did-it-matter)
- [305: What are the pending tree and active tree in the compositor?](#305-what-are-the-pending-tree-and-active-tree-in-the-compositor)
- [306: What happens during commit?](#306-what-happens-during-commit)
- [307: What is BeginMainFrame?](#307-what-is-beginmainframe)
- [308: How does the compositor keep producing frames when the main thread is busy?](#308-how-does-the-compositor-keep-producing-frames-when-the-main-thread-is-busy)
- [309: What is a surface in Viz?](#309-what-is-a-surface-in-viz)
- [310: Why does a LocalSurfaceId need to be synchronized between processes?](#310-why-does-a-localsurfaceid-need-to-be-synchronized-between-processes)
- [311: What is out-of-process raster (OOP-R)?](#311-what-is-out-of-process-raster-oop-r)
- [312: What is the GPU command buffer?](#312-what-is-the-gpu-command-buffer)
- [313: Why is getImageData on a canvas slow?](#313-why-is-getimagedata-on-a-canvas-slow)
- [314: What is the difference between Skia Ganesh and Skia Graphite?](#314-what-is-the-difference-between-skia-ganesh-and-skia-graphite)
- [315: How does the compositor decide which tiles to rasterize first?](#315-how-does-the-compositor-decide-which-tiles-to-rasterize-first)
- [316: Why can text on an animated scaled layer look blurry?](#316-why-can-text-on-an-animated-scaled-layer-look-blurry)
- [317: What are hardware overlays?](#317-what-are-hardware-overlays)
- [318: How does Viz route input to the right process when there are OOPIFs?](#318-how-does-viz-route-input-to-the-right-process-when-there-are-oopifs)
- [319: How does Chrome throttle iframes?](#319-how-does-chrome-throttle-iframes)
- [320: What is the Blink scheduler?](#320-what-is-the-blink-scheduler)
- [321: How does Chrome prevent rendering from being starved by other tasks?](#321-how-does-chrome-prevent-rendering-from-being-starved-by-other-tasks)
- [322: What is the document lifecycle in Blink?](#322-what-is-the-document-lifecycle-in-blink)
- [323: How does LayoutNG cache layout results?](#323-how-does-layoutng-cache-layout-results)
- [324: How do container queries fit into the rendering pipeline?](#324-how-do-container-queries-fit-into-the-rendering-pipeline)
- [325: How does :has() work and why was it hard to implement?](#325-how-does-has-work-and-why-was-it-hard-to-implement)
- [326: What is the difference between paint invalidation and raster invalidation?](#326-what-is-the-difference-between-paint-invalidation-and-raster-invalidation)
- [327: Why can a small change cause a large repaint?](#327-why-can-a-small-change-cause-a-large-repaint)
- [328: What are layer squashing and overlap testing?](#328-what-are-layer-squashing-and-overlap-testing)
- [329: How does Chrome handle animations in the style engine?](#329-how-does-chrome-handle-animations-in-the-style-engine)
- [330: Why might a transform animation not run on the compositor?](#330-why-might-a-transform-animation-not-run-on-the-compositor)
- [331: What does "scroll unification" mean in Chrome?](#331-what-does-scroll-unification-mean-in-chrome)
- [332: How does Chrome decide whether a scroller can be composited?](#332-how-does-chrome-decide-whether-a-scroller-can-be-composited)
- [333: What is the image decode cache and discardable memory?](#333-what-is-the-image-decode-cache-and-discardable-memory)
- [334: How do you think about GPU memory as a front-end developer?](#334-how-do-you-think-about-gpu-memory-as-a-front-end-developer)
- [335: What is BlinkNG?](#335-what-is-blinkng)
- [336: What is pre-paint?](#336-what-is-pre-paint)
- [337: How does content-visibility work internally?](#337-how-does-content-visibility-work-internally)
- [338: Explain the cost difference between changing a CSS custom property on :root vs on a component.](#338-explain-the-cost-difference-between-changing-a-css-custom-property-on-root-vs-on-a-component)
- [339: How does font loading affect layout?](#339-how-does-font-loading-affect-layout)
- [340: What is the hit-test cache and why is hit testing sometimes slow?](#340-what-is-the-hit-test-cache-and-why-is-hit-testing-sometimes-slow)
- [341: Why does hover sometimes not update while scrolling?](#341-why-does-hover-sometimes-not-update-while-scrolling)
- [342: How does Chrome render a cross-origin iframe inside a page it composites?](#342-how-does-chrome-render-a-cross-origin-iframe-inside-a-page-it-composites)
- [343: What problems does rendering OOPIFs in a separate process cause?](#343-what-problems-does-rendering-oopifs-in-a-separate-process-cause)
- [344: How does the compositor handle a fixed-position element during scroll?](#344-how-does-the-compositor-handle-a-fixed-position-element-during-scroll)
- [345: What is the VideoNG project?](#345-what-is-the-videong-project)
- [346: How does Chrome measure frame quality internally?](#346-how-does-chrome-measure-frame-quality-internally)
- [347: What is a partially presented frame?](#347-what-is-a-partially-presented-frame)
- [348: What happens when you call element.getBoundingClientRect() during a compositor-driven scroll?](#348-what-happens-when-you-call-elementgetboundingclientrect-during-a-compositor-driven-scroll)
- [349: How do paint worklets run?](#349-how-do-paint-worklets-run)
- [350: What is the difference between raster on the CPU and GPU raster in terms of trade-offs?](#350-what-is-the-difference-between-raster-on-the-cpu-and-gpu-raster-in-terms-of-trade-offs)
- [351: How is the renderer sandbox implemented on each operating system?](#351-how-is-the-renderer-sandbox-implemented-on-each-operating-system)
- [352: Why does Chrome treat the renderer process as compromised?](#352-why-does-chrome-treat-the-renderer-process-as-compromised)
- [353: What is a process lock (site lock)?](#353-what-is-a-process-lock-site-lock)
- [354: What is the "Rule of Two" in Chromium security?](#354-what-is-the-rule-of-two-in-chromium-security)
- [355: What does a typical full Chrome exploit chain look like?](#355-what-does-a-typical-full-chrome-exploit-chain-look-like)
- [356: What is the V8 sandbox?](#356-what-is-the-v8-sandbox)
- [357: What is MiraclePtr?](#357-what-is-miracleptr)
- [358: What is PartitionAlloc?](#358-what-is-partitionalloc)
- [359: Why is Chromium adopting Rust?](#359-why-is-chromium-adopting-rust)
- [360: How does Chrome find security bugs before attackers?](#360-how-does-chrome-find-security-bugs-before-attackers)
- [361: Why are JIT compilers a common source of security bugs?](#361-why-are-jit-compilers-a-common-source-of-security-bugs)
- [362: What was Spectre and how did it change browsers?](#362-what-was-spectre-and-how-did-it-change-browsers)
- [363: How is Site Isolation different on Android?](#363-how-is-site-isolation-different-on-android)
- [364: Can two different origins of the same site share a process, and why does it matter?](#364-can-two-different-origins-of-the-same-site-share-a-process-and-why-does-it-matter)
- [365: Where does Chrome enforce CSP, CORS and cookie rules: in the renderer or outside it?](#365-where-does-chrome-enforce-csp-cors-and-cookie-rules-in-the-renderer-or-outside-it)
- [366: How does the browser process limit which Mojo interfaces a renderer can use?](#366-how-does-the-browser-process-limit-which-mojo-interfaces-a-renderer-can-use)
- [367: Why is the GPU process sandbox weaker than the renderer sandbox?](#367-why-is-the-gpu-process-sandbox-weaker-than-the-renderer-sandbox)
- [368: What is the difference between V8 jitless mode and turning off the optimizer?](#368-what-is-the-difference-between-v8-jitless-mode-and-turning-off-the-optimizer)
- [369: What is pointer compression in V8?](#369-what-is-pointer-compression-in-v8)
- [370: What is a Smi?](#370-what-is-a-smi)
- [371: What are elements kinds in V8?](#371-what-are-elements-kinds-in-v8)
- [372: What is dictionary mode for objects?](#372-what-is-dictionary-mode-for-objects)
- [373: How does V8 represent strings internally?](#373-how-does-v8-represent-strings-internally)
- [374: What is a write barrier in V8's GC?](#374-what-is-a-write-barrier-in-v8s-gc)
- [375: How does concurrent marking work?](#375-how-does-concurrent-marking-work)
- [376: What is idle-time garbage collection?](#376-what-is-idle-time-garbage-collection)
- [377: How does V8 compile WebAssembly?](#377-how-does-v8-compile-webassembly)
- [378: What is WasmGC and why does it matter?](#378-what-is-wasmgc-and-why-does-it-matter)
- [379: What is JSPI?](#379-what-is-jspi)
- [380: What are compile hints in V8?](#380-what-are-compile-hints-in-v8)
- [381: How does the network service organize requests per profile?](#381-how-does-the-network-service-organize-requests-per-profile)
- [382: How does the HTTP cache key work in Chrome today?](#382-how-does-the-http-cache-key-work-in-chrome-today)
- [383: How does Chrome delay low-priority requests while the page loads?](#383-how-does-chrome-delay-low-priority-requests-while-the-page-loads)
- [384: What is post-quantum key exchange in Chrome's TLS?](#384-what-is-post-quantum-key-exchange-in-chromes-tls)
- [385: What is Certificate Transparency and how does Chrome enforce it?](#385-what-is-certificate-transparency-and-how-does-chrome-enforce-it)
- [386: How does QUIC 0-RTT work and what are its risks?](#386-how-does-quic-0-rtt-work-and-what-are-its-risks)
- [387: What is the simple cache backend?](#387-what-is-the-simple-cache-backend)
- [388: What is "connection-level" privacy in Chrome, like network state partitioning?](#388-what-is-connection-level-privacy-in-chrome-like-network-state-partitioning)
- [389: How does Chrome decide whether to show a TLS interstitial or a connection error?](#389-how-does-chrome-decide-whether-to-show-a-tls-interstitial-or-a-connection-error)
- [390: How does Chrome handle a renderer that tries to navigate to a URL it isn't allowed to?](#390-how-does-chrome-handle-a-renderer-that-tries-to-navigate-to-a-url-it-isnt-allowed-to)
- [391: What is the browser-side CSP for frame embedding?](#391-what-is-the-browser-side-csp-for-frame-embedding)
- [392: How does Chrome isolate extensions from web pages and from each other?](#392-how-does-chrome-isolate-extensions-from-web-pages-and-from-each-other)
- [393: What is Origin-Agent-Cluster?](#393-what-is-origin-agent-cluster)
- [394: Why can't a page read pixels from a cross-origin image drawn on a canvas?](#394-why-cant-a-page-read-pixels-from-a-cross-origin-image-drawn-on-a-canvas)
- [395: What timing attacks do browsers still need to defend against?](#395-what-timing-attacks-do-browsers-still-need-to-defend-against)
- [396: How does Chrome stop pages from reading which links you visited?](#396-how-does-chrome-stop-pages-from-reading-which-links-you-visited)
- [397: What is a "renderer kill" and when does Chrome do it on purpose?](#397-what-is-a-renderer-kill-and-when-does-chrome-do-it-on-purpose)
- [398: Why are some memory-hungry features restricted to cross-origin isolated pages?](#398-why-are-some-memory-hungry-features-restricted-to-cross-origin-isolated-pages)
- [399: What is COEP credentialless and why was it added?](#399-what-is-coep-credentialless-and-why-was-it-added)
- [400: How does Chrome keep secrets in the browser process safe from a compromised renderer?](#400-how-does-chrome-keep-secrets-in-the-browser-process-safe-from-a-compromised-renderer)
- [401: How does Chrome decide how many renderer processes to create?](#401-how-does-chrome-decide-how-many-renderer-processes-to-create)
- [402: How does Android decide which Chrome renderer to kill when memory is low?](#402-how-does-android-decide-which-chrome-renderer-to-kill-when-memory-is-low)
- [403: How does the bfcache work internally?](#403-how-does-the-bfcache-work-internally)
- [404: How does prerendering work internally?](#404-how-does-prerendering-work-internally)
- [405: What limits does Chrome place on speculation rules?](#405-what-limits-does-chrome-place-on-speculation-rules)
- [406: How would you debug a page that feels slow on scroll?](#406-how-would-you-debug-a-page-that-feels-slow-on-scroll)
- [407: How would you investigate a high INP reported from real users?](#407-how-would-you-investigate-a-high-inp-reported-from-real-users)
- [408: A page's memory keeps growing in a long-running SPA. How do you approach it?](#408-a-pages-memory-keeps-growing-in-a-long-running-spa-how-do-you-approach-it)
- [409: Why might a site be fast in Lighthouse but slow for real users?](#409-why-might-a-site-be-fast-in-lighthouse-but-slow-for-real-users)
- [410: How would you diagnose a slow TTFB?](#410-how-would-you-diagnose-a-slow-ttfb)
- [411: How does streaming HTML help performance?](#411-how-does-streaming-html-help-performance)
- [412: Why do third-party scripts hurt performance so much?](#412-why-do-third-party-scripts-hurt-performance-so-much)
- [413: How does hydration affect the browser's main thread?](#413-how-does-hydration-affect-the-browsers-main-thread)
- [414: Why does Chrome sometimes show a white screen instead of the old page during navigation?](#414-why-does-chrome-sometimes-show-a-white-screen-instead-of-the-old-page-during-navigation)
- [415: How would you make a heavy data grid with 100,000 rows render fast?](#415-how-would-you-make-a-heavy-data-grid-with-100000-rows-render-fast)
- [416: How would you implement a smooth animated drawer that stays smooth during heavy JavaScript?](#416-how-would-you-implement-a-smooth-animated-drawer-that-stays-smooth-during-heavy-javascript)
- [417: Why might `position: fixed` elements jump on mobile Chrome?](#417-why-might-position-fixed-elements-jump-on-mobile-chrome)
- [418: How does Chrome handle the on-screen keyboard on Android for layout?](#418-how-does-chrome-handle-the-on-screen-keyboard-on-android-for-layout)
- [419: What would you check if a page is never restored from bfcache?](#419-what-would-you-check-if-a-page-is-never-restored-from-bfcache)
- [420: Why are cross-origin iframes expensive, and how would you reduce their cost?](#420-why-are-cross-origin-iframes-expensive-and-how-would-you-reduce-their-cost)
- [421: Why did Google fork WebKit to create Blink?](#421-why-did-google-fork-webkit-to-create-blink)
- [422: What are the trade-offs of Chrome's multi-process architecture?](#422-what-are-the-trade-offs-of-chromes-multi-process-architecture)
- [423: Why does Chrome run the network stack in a separate process?](#423-why-does-chrome-run-the-network-stack-in-a-separate-process)
- [424: What is the Chrome Servicification project?](#424-what-is-the-chrome-servicification-project)
- [425: How does Chrome share read-only data across processes to save memory?](#425-how-does-chrome-share-read-only-data-across-processes-to-save-memory)
- [426: How would you explain the difference between the main thread, the compositor thread and the GPU process in one sentence each?](#426-how-would-you-explain-the-difference-between-the-main-thread-the-compositor-thread-and-the-gpu-process-in-one-sentence-each)
- [427: A CSS animation is smooth on desktop but janky on a low-end Android phone. What do you check?](#427-a-css-animation-is-smooth-on-desktop-but-janky-on-a-low-end-android-phone-what-do-you-check)
- [428: Why is `box-shadow` or `filter: blur()` animation slow, and what is a better approach?](#428-why-is-box-shadow-or-filter-blur-animation-slow-and-what-is-a-better-approach)
- [429: How does Chrome handle very long JavaScript tasks inside iframes from other sites?](#429-how-does-chrome-handle-very-long-javascript-tasks-inside-iframes-from-other-sites)
- [430: What happens if two same-origin tabs share a renderer process and one runs an infinite loop?](#430-what-happens-if-two-same-origin-tabs-share-a-renderer-process-and-one-runs-an-infinite-loop)
- [431: Why does Chrome sometimes keep a process alive after you close a tab?](#431-why-does-chrome-sometimes-keep-a-process-alive-after-you-close-a-tab)
- [432: What is keepalive in fetch and why does it matter for unload?](#432-what-is-keepalive-in-fetch-and-why-does-it-matter-for-unload)
- [433: How does Chrome isolate Service Workers in terms of processes?](#433-how-does-chrome-isolate-service-workers-in-terms-of-processes)
- [434: How does Chrome reduce Service Worker startup cost?](#434-how-does-chrome-reduce-service-worker-startup-cost)
- [435: What role does Chrome play in web standards, and why does that matter in interviews?](#435-what-role-does-chrome-play-in-web-standards-and-why-does-that-matter-in-interviews)
- [436: How do you check if a feature is safe to use across browsers?](#436-how-do-you-check-if-a-feature-is-safe-to-use-across-browsers)
- [437: How would you design a page to load fast on a slow 3G connection in Chrome?](#437-how-would-you-design-a-page-to-load-fast-on-a-slow-3g-connection-in-chrome)
- [438: Why might `setTimeout` callbacks in a background tab fire much later than expected, and how do you design around it?](#438-why-might-settimeout-callbacks-in-a-background-tab-fire-much-later-than-expected-and-how-do-you-design-around-it)
- [439: How does the browser decide to show a page as "not secure" in the address bar?](#439-how-does-the-browser-decide-to-show-a-page-as-not-secure-in-the-address-bar)
- [440: How would you explain what happens between pressing a key in an input field and the character appearing on screen?](#440-how-would-you-explain-what-happens-between-pressing-a-key-in-an-input-field-and-the-character-appearing-on-screen)
- [441: What is the difference between how Chrome handles `<script type="module">` imports and a bundled script?](#441-what-is-the-difference-between-how-chrome-handles-script-typemodule-imports-and-a-bundled-script)
- [442: How does Chrome handle import maps?](#442-how-does-chrome-handle-import-maps)
- [443: Why is reading `localStorage` on page load a performance concern?](#443-why-is-reading-localstorage-on-page-load-a-performance-concern)
- [444: How does Chrome decide when to fire the `load` event on a page with lazy-loaded images?](#444-how-does-chrome-decide-when-to-fire-the-load-event-on-a-page-with-lazy-loaded-images)
- [445: What would you look for in a trace if users report the page "freezes for a second" after login?](#445-what-would-you-look-for-in-a-trace-if-users-report-the-page-freezes-for-a-second-after-login)
- [446: How does structured cloning affect performance with workers?](#446-how-does-structured-cloning-affect-performance-with-workers)
- [447: How does Chrome decide whether a page is "installable" as a PWA, and what changed recently?](#447-how-does-chrome-decide-whether-a-page-is-installable-as-a-pwa-and-what-changed-recently)
- [448: What happens in Chrome when you zoom a page with Ctrl/Cmd and +?](#448-what-happens-in-chrome-when-you-zoom-a-page-with-ctrlcmd-and-)
- [449: Why might `devicePixelRatio`-based canvas code look blurry or use too much memory?](#449-why-might-devicepixelratio-based-canvas-code-look-blurry-or-use-too-much-memory)
- [450: If you had to explain how Chrome works in two minutes in an interview, what would you say?](#450-if-you-had-to-explain-how-chrome-works-in-two-minutes-in-an-interview-what-would-you-say)

---

# Easy Questions (1-150)

## 1: What is a web browser and what does it actually do?

A browser is a program that downloads resources (HTML, CSS, JavaScript, images, fonts) from servers and turns them into a page you can see and use. To do that it has to talk to the network, parse the files, run JavaScript, work out where every element goes, draw pixels on the screen and react to clicks, typing and scrolling.

It also keeps you safe while doing this. A browser runs code from any site on the internet, so a big part of its job is to stop one site from reading data from another site or from your computer.

## 2: What is the difference between Chromium and Google Chrome?

Chromium is the open source project. It contains almost all of the browser code: the UI, Blink, V8, the network stack and so on. Anyone can build it and many companies do.

Google Chrome is Google's product built on top of Chromium. It adds a few closed-source or licensed parts, such as the automatic updater, some media codecs, Widevine DRM, crash reporting and Google account integration. Edge, Brave, Opera, Vivaldi and Samsung Internet are also built on Chromium.

## 3: What is Blink?

Blink is the rendering engine used by Chrome and other Chromium browsers. It takes HTML and CSS, builds the DOM, calculates styles, does layout and paint, and implements most Web APIs like `fetch`, the DOM API, Canvas and so on.

Blink started in 2013 as a fork of WebKit, the engine Safari uses. Google forked it because Chrome's multi-process design was different from Safari's, and keeping both in one codebase was slowing development.

## 4: What is V8?

V8 is Google's open source JavaScript and WebAssembly engine, written in C++. Chrome uses it to run all JavaScript on web pages, and Node.js, Deno and Electron use it too.

V8 parses your code, turns it into bytecode, runs it in an interpreter, and compiles the hot parts into fast machine code. It also manages memory for JavaScript objects with its own garbage collector.

## 5: What are the main parts of a browser?

A browser is usually described in these parts:

- **User interface**: address bar, tabs, back and forward buttons, bookmarks.
- **Browser engine**: connects the UI with the rendering engine.
- **Rendering engine**: parses HTML and CSS and draws the page (Blink in Chrome).
- **JavaScript engine**: runs scripts (V8 in Chrome).
- **Networking**: DNS, HTTP, TLS, caching.
- **Storage**: cookies, localStorage, IndexedDB, the HTTP cache.
- **Graphics backend**: talks to the GPU and the operating system to put pixels on screen.

In Chrome these parts are spread over several processes instead of living in one program.

## 6: Which rendering engines exist besides Blink?

- **WebKit**: used by Safari. On iOS, Apple required every browser to use WebKit for many years. Since iOS 17.4 browsers in the EU can ship their own engine.
- **Gecko**: used by Firefox.
- **Blink**: used by Chrome, Edge, Opera, Brave, Vivaldi and other Chromium browsers.

This is why you test in Chrome, Safari and Firefox. Testing in Chrome and Edge mostly tests the same engine.

## 7: What happens at a high level when you type a URL and press Enter?

1. The browser checks if the input is a URL or a search query.
2. It looks up the domain in DNS to get an IP address (unless it is already cached).
3. It opens a TCP connection (or a QUIC connection for HTTP/3) and does a TLS handshake for HTTPS.
4. It sends an HTTP request and gets a response.
5. Based on the response type, it picks a renderer process and hands the HTML to it.
6. The renderer parses HTML into the DOM, loads CSS and builds style info, runs scripts, and does layout and paint.
7. The compositor and GPU turn the result into pixels on screen.
8. The page fires events like `DOMContentLoaded` and `load`, and keeps reacting to user input.

## 8: How does the address bar (Omnibox) decide whether you typed a URL or a search?

The Omnibox checks the text as you type. If it looks like a URL (has a scheme like `https://`, a known top-level domain, an IP address, or matches a site in your history), it treats it as navigation. Otherwise it sends the text to your default search engine.

It also shows suggestions from history, bookmarks and the search engine, and it can start preconnecting or even prerendering a likely result before you press Enter.

## 9: What is the difference between a process and a thread?

A process is a running program with its own memory space. One process cannot read another process's memory directly; they have to talk through some form of inter-process communication (IPC).

A thread is a unit of work inside a process. Threads in the same process share memory, so they can talk easily but can also break each other. If a process crashes, all of its threads die with it, but other processes keep running.

## 10: Why does Chrome use multiple processes?

Chrome splits the browser into many processes for three main reasons:

- **Stability**: if one page crashes, only its renderer process dies. Other tabs keep working.
- **Security**: renderer processes run in a sandbox with very few rights. Even if an attacker takes over a renderer, they can't easily touch your files or other sites.
- **Performance**: work runs in parallel on different CPU cores, and a slow page doesn't freeze the whole browser.

The cost is more memory, because every process has its own copy of some data.

## 11: What is the browser process?

The browser process is the main process of Chrome. It draws the UI (tabs, address bar, menus), manages all the other processes, handles navigation decisions, permissions, the profile, and access to files and the operating system.

It has several threads, for example the UI thread and the IO thread. It is the most trusted process, so it treats messages from renderer processes as untrusted and checks them.

## 12: What is a renderer process?

A renderer process runs the web content. It contains Blink and V8, so it parses HTML and CSS, runs JavaScript, does layout and paint, and runs the compositor thread for that content.

Renderer processes run inside a sandbox. They can't open files or network sockets on their own; they ask the browser process or other services through IPC. Usually each site gets its own renderer process.

## 13: What is the GPU process?

The GPU process talks to the graphics card. Renderer processes and the browser process send it drawing commands, and it runs them using OpenGL, Direct3D, Metal or Vulkan.

It is a separate process because GPU drivers are often buggy. If a driver crashes, only the GPU process dies and Chrome restarts it, instead of the whole browser going down. Chrome's display compositor (Viz) also runs in this process.

## 14: What is the network service in Chrome?

The network service handles all network traffic: DNS, HTTP, HTTP/2, HTTP/3, TLS, cookies, the HTTP cache and proxies. On desktop it runs in its own utility process. On some low-memory Android devices it can run inside the browser process.

Renderers can't open sockets. When a page calls `fetch()`, the request goes over IPC to the network service, which makes the request and sends the response back.

## 15: What are utility processes?

Utility processes run small, separate services that Chrome doesn't want in the browser process. Examples are the network service, the storage service, the audio service, data decoders (for things like JSON from untrusted sources), and unzip or file parsing tasks.

Running them in their own sandboxed processes means a bug in, say, an image or archive parser can't take over the whole browser.

## 16: How do Chrome extensions run in terms of processes?

Extensions have their own processes. With Manifest V3 the background logic runs in an extension service worker, which Chrome starts when an event happens and stops when it is idle.

Content scripts are different. They run inside the renderer process of the page they are injected into, but in a separate "isolated world," so they see the same DOM as the page but have their own JavaScript globals.

## 17: How do you see which processes Chrome is running?

Open Chrome's Task Manager with `Shift + Esc` on Windows and Linux, or from the menu: More tools > Task manager. It lists the browser process, GPU process, network service, each tab, each extension and other utility processes, with their memory, CPU and network usage.

You can end a single process from there. For more detail, `chrome://process-internals` shows how frames are mapped to processes and which site each process is locked to.

## 18: What does the "Aw, Snap!" page mean?

It means the renderer process for that tab crashed or was killed. Common reasons are running out of memory, a bug in Chrome, a bad extension, or the operating system killing the process.

Because of the multi-process design, only that tab (and other tabs that shared the same process) is affected. Reloading starts a new renderer process.

## 19: What is the sandbox in Chrome?

The sandbox is a set of operating system restrictions placed on a process. Sandboxed processes can't read or write files, open network sockets, start programs, or call most system APIs. They can only compute and talk to the browser process over IPC.

Renderer processes are the most restricted, because they run untrusted code from the web. Even if an attacker finds a bug and runs code inside a renderer, they still need a second bug to escape the sandbox.

## 20: What is Site Isolation?

Site Isolation is a Chrome feature that puts pages from different sites into different renderer processes. This includes cross-site iframes: an iframe from `ads.com` inside `news.com` runs in a separate process from the parent page.

It protects against attacks like Spectre, where a page could read memory from the same process. If another site's data is never in your process, it can't be stolen that way. It has been on by default on desktop since Chrome 67.

## 21: What is the difference between an origin and a site?

An **origin** is scheme + host + port, for example `https://app.example.com:443`. Two URLs are same-origin only if all three match.

A **site** is scheme + registrable domain (eTLD+1), for example `https://example.com`. So `https://app.example.com` and `https://api.example.com` are different origins but the same site. The list of public suffixes like `.com` or `.co.uk` comes from the Public Suffix List.

Chrome's Site Isolation works at the site level, while the same-origin policy works at the origin level.

## 22: What happens during a DNS lookup?

DNS turns a domain name into an IP address. Chrome first checks its own host cache, then asks the operating system resolver (or uses its built-in resolver), which may check its cache and then ask a DNS server. That server may ask the root, TLD and authoritative servers until it gets the answer.

Each answer has a TTL that says how long it can be cached. Chrome also supports DNS over HTTPS, which encrypts these queries.

## 23: How do you see or clear Chrome's DNS cache?

Go to `chrome://net-internals/#dns`. There you can look up a host and press "Clear host cache." You may also need to flush idle sockets at `chrome://net-internals/#sockets`, because an open connection can keep using the old IP.

The operating system has its own DNS cache, which you clear with OS tools.

## 24: What is the TCP handshake?

Before sending data over TCP, the client and server do a three-step handshake: the client sends SYN, the server replies with SYN-ACK, and the client sends ACK. That costs one round trip before any HTTP data can be sent.

This is why connection setup matters for performance and why browsers reuse connections and support preconnect.

## 25: What happens during a TLS handshake?

For HTTPS, after TCP connects, the client and server do a TLS handshake. They agree on a TLS version and cipher, the server sends its certificate, the browser checks it, and both sides create shared encryption keys.

With TLS 1.3, the handshake takes one round trip, and resumed connections can send data with zero extra round trips (0-RTT) in some cases. Chrome uses BoringSSL, Google's fork of OpenSSL.

## 26: How does Chrome check that an HTTPS certificate is valid?

It checks that:

- The certificate is for the domain you are visiting.
- It is not expired.
- It chains up to a trusted root certificate in the Chrome Root Store.
- It has not been revoked (Chrome uses its own CRLSets list for this).
- It is logged in Certificate Transparency logs, which Chrome requires for public certificates.

If any check fails, you get a full-page warning like `NET::ERR_CERT_DATE_INVALID`.

## 27: What does an HTTP request and response contain?

A request has a method (`GET`, `POST`, etc.), a path, headers like `Host`, `Accept`, `Cookie` and `User-Agent`, and an optional body.

A response has a status code (`200`, `301`, `404`, `500`...), headers like `Content-Type`, `Cache-Control` and `Set-Cookie`, and a body with the actual content. The browser uses headers like `Content-Type` to decide what to do with the body.

## 28: What is the difference between HTTP/1.1, HTTP/2 and HTTP/3?

- **HTTP/1.1**: text-based, one request at a time per connection. Browsers open up to 6 connections per host to work around this.
- **HTTP/2**: binary, many requests at the same time over one TCP connection (multiplexing), header compression. But one lost TCP packet blocks every stream on that connection.
- **HTTP/3**: runs on QUIC over UDP. Streams are independent, so a lost packet only delays its own stream. Connection setup is faster and connections survive network changes.

Chrome supports all three and picks the best one the server offers.

## 29: What is QUIC?

QUIC is a transport protocol built on UDP, designed at Google and later standardized by the IETF. It combines what TCP and TLS do: reliable delivery, congestion control and encryption, in one layer.

Its benefits are faster connection setup (often one round trip, sometimes zero), no head-of-line blocking between streams, and connection migration, so a download can continue when your phone switches from Wi-Fi to mobile data. HTTP/3 runs on top of QUIC.

## 30: What is the HTTP cache?

The HTTP cache stores responses on disk (and some in memory) so the browser can reuse them without downloading again. Whether and how long a response is stored depends on headers like `Cache-Control`, `Expires`, `ETag` and `Last-Modified`.

When a cached response is still fresh, Chrome uses it directly. When it is stale, Chrome can send a conditional request, and the server can reply `304 Not Modified` with no body.

## 31: What do common Cache-Control values mean?

```http
Cache-Control: max-age=31536000, immutable   # cache for a year, never revalidate
Cache-Control: no-cache                       # store it, but always revalidate first
Cache-Control: no-store                       # never store it
Cache-Control: private                        # only the browser may cache, not CDNs
Cache-Control: public, max-age=600            # anyone may cache for 10 minutes
Cache-Control: max-age=60, stale-while-revalidate=300
```

A common setup is long `max-age` with `immutable` for files that have a hash in the name, and `no-cache` for HTML so users always get the latest version.

## 32: What is the DOM?

The DOM (Document Object Model) is the tree of objects the browser builds from HTML. Each element, text and comment becomes a node, and the nodes are linked as parents and children.

It is also an API: JavaScript can read and change the tree with methods like `querySelector`, `appendChild` and `setAttribute`, and the browser updates what you see. In Chrome, DOM nodes are C++ objects inside Blink, and JavaScript gets wrapper objects that point to them.

## 33: How does the browser parse HTML?

The HTML parser reads bytes from the network, decodes them into characters using the right encoding, and turns characters into tokens (start tag, end tag, text, comment). A tree builder then takes the tokens and creates DOM nodes.

Parsing happens step by step as data arrives, so the browser doesn't wait for the whole file. The HTML spec defines exactly how to handle every input, including broken HTML.

## 34: Why does a broken HTML file still display?

The HTML parsing spec defines what to do with every kind of error: missing closing tags, wrongly nested tags, a `<td>` outside a table, and so on. The parser fixes these up in a fixed, standard way.

For example, `<p>One<p>Two` creates two separate paragraphs, because a new `<p>` closes the open one. Since all browsers follow the same rules, broken HTML usually produces the same DOM everywhere.

## 35: What is the CSSOM?

The CSSOM (CSS Object Model) is the browser's representation of all the style sheets on the page: rules, selectors and declarations. It comes from `<link rel="stylesheet">`, `<style>` tags and inline styles, plus the browser's default styles.

JavaScript can access it with `document.styleSheets` and `CSSStyleSheet` objects. The browser uses it with the DOM to work out the final style of every element.

## 36: What is style calculation?

Style calculation (also called recalc style) is the step where the browser works out the final value of every CSS property for every element. It matches selectors against elements, applies the cascade and specificity, handles inheritance, and turns values like `2em` or `50%` into computed values.

The result is a computed style object per element. You can see it in the DevTools "Computed" tab or with `getComputedStyle(el)`.

## 37: What is the layout tree (render tree)?

The layout tree is built from the DOM and computed styles. It only has things that take up space or are drawn. Elements with `display: none` are not in it, while pseudo-elements like `::before` are added.

Each object in it knows how to lay itself out. Older articles call this the "render tree." In Blink, layout produces an immutable fragment tree that holds the final sizes and positions.

## 38: What is layout?

Layout (sometimes called reflow) is the step that works out the size and position of every box on the page. It uses the layout tree, the viewport size and the CSS rules for block, inline, flex, grid and so on.

Layout can be expensive on large pages, and changing one element can affect the layout of many others, for example making a sidebar wider makes the main content narrower.

## 39: What is paint?

Paint is the step where the browser decides what to draw and in which order: backgrounds, borders, text, images, shadows, outlines. In Chrome, paint does not draw pixels yet. It records drawing commands into a list (paint records, also called display items).

Later the raster step turns these commands into actual pixels.

## 40: What is compositing?

Compositing is splitting the page into separate layers, drawing each one, and then combining them into the final image on the GPU. Things like transformed elements, videos or scrolling areas can be on their own layers.

The big benefit is that when only a layer's position or opacity changes (for example a CSS transform animation or scrolling), the browser can just recombine existing layers instead of doing layout and paint again.

## 41: What is the critical rendering path?

It is the sequence of steps the browser must finish before it can show the first pixels: get the HTML, build the DOM, get the CSS, build the CSSOM, run any blocking scripts, compute style, do layout and paint.

To make first render faster you reduce what blocks it: inline critical CSS, defer non-critical JavaScript, reduce file sizes and round trips, and load fonts and images in a way that doesn't hold back the page.

## 42: What is a render-blocking resource?

A render-blocking resource is one the browser waits for before it paints anything. By default, stylesheets in `<head>` are render-blocking, because painting without them would show unstyled content and then jump.

Classic `<script>` tags in `<head>` without `async` or `defer` block too. You can reduce the cost with `media` attributes (`<link rel="stylesheet" media="print">` is not render-blocking for screen), inlining critical CSS and using `defer`.

## 43: What is a parser-blocking script?

A classic `<script src="...">` without `async` or `defer` stops the HTML parser. The browser must download it, wait for any earlier stylesheets, run it, and only then continue parsing.

It has to stop because the script could call `document.write()` or read the DOM up to that point. That is why such scripts were traditionally put at the end of `<body>`.

## 44: What is the difference between async and defer on a script?

```html
<script src="analytics.js" async></script>
<script src="app.js" defer></script>
```

Both download the script without blocking the parser.

- **async** runs the script as soon as it is downloaded, which can be in the middle of parsing. Order between async scripts is not guaranteed. Good for independent scripts like analytics.
- **defer** runs the script after the HTML is fully parsed, right before `DOMContentLoaded`, in the order they appear in the document. Good for app code that needs the DOM.

## 45: How do module scripts load by default?

`<script type="module">` is deferred by default. It doesn't block the parser and runs after the document is parsed, in order. You can add `async` to run it as soon as it and its imports are ready.

```html
<script type="module" src="/main.js"></script>
```

Modules also run in strict mode, have their own scope, and are fetched with CORS, so cross-origin module files need proper CORS headers.

## 46: What is the preload scanner?

The preload scanner is a lightweight second parser in Chrome. When the main parser is blocked by a script, the preload scanner keeps reading the rest of the HTML and starts downloading resources it finds, like scripts, stylesheets and images.

That's why resources should appear in the HTML markup. If you inject them with JavaScript or hide image URLs in `data-src` attributes, the preload scanner can't see them and they start loading later.

## 47: What is reflow and what triggers it?

Reflow is another name for layout: recalculating positions and sizes. It is triggered by things that change geometry, for example:

- Adding, removing or moving DOM nodes.
- Changing `width`, `height`, `padding`, `margin`, `font-size`, `display` and similar.
- Changing text content.
- Resizing the window.
- Reading layout values like `offsetHeight` or `getBoundingClientRect()` after a change, which forces the browser to do layout right away.

## 48: What is repaint?

A repaint happens when something visual changes but the geometry doesn't, for example `color`, `background-color`, `visibility` or `box-shadow`. The browser skips layout but has to paint and raster the affected area again.

A repaint is cheaper than a reflow but still costs time, especially for big areas or expensive effects like large blurs and shadows.

## 49: Which CSS properties are cheapest to animate and why?

`transform` and `opacity` are the cheapest. When an element is on its own compositor layer, changing these properties doesn't need layout or paint. The compositor thread just moves or fades the existing layer on the GPU.

```css
.box {
  transition:
    transform 300ms,
    opacity 300ms;
}
.box.open {
  transform: translateX(200px);
  opacity: 1;
}
```

Animating `left`, `top`, `width` or `height` causes layout on every frame, which is much slower. Some `filter` animations can also run on the compositor.

## 50: What is the main thread in a renderer process?

The main thread is the thread in the renderer where most work happens: running JavaScript, parsing HTML, style calculation, layout, paint, and handling most events.

Since it does all of that on one thread, a long JavaScript task blocks everything else. The page can't respond to clicks or update the screen until the task is done. Keeping the main thread free is the core of front-end performance.

## 51: What is the event loop in the browser?

The event loop is how the browser schedules work on the main thread. It repeatedly picks a task from a task queue (a click handler, a timer callback, a network response), runs it to completion, runs all pending microtasks, and then, when it is time for a new frame, updates the rendering.

Only one task runs at a time. That's why a long task makes the page freeze: nothing else, including rendering, can happen until it finishes.

## 52: What is the difference between tasks and microtasks?

**Tasks** (macrotasks) come from things like `setTimeout`, `setInterval`, user events, `postMessage` and network callbacks. The event loop runs one task per loop turn.

**Microtasks** come from resolved promises (`.then`, `await`), `queueMicrotask()` and `MutationObserver`. After each task, the browser runs every microtask in the queue, including new ones added while running, before doing anything else.

```js
setTimeout(() => console.log("task"), 0);
Promise.resolve().then(() => console.log("microtask"));
console.log("sync");
// sync, microtask, task
```

## 53: What is requestAnimationFrame?

`requestAnimationFrame(callback)` asks the browser to run your callback right before the next frame is rendered. It is the right place for visual updates in JavaScript animations, because the work lines up with the screen refresh.

```js
function step(time) {
  box.style.transform = `translateX(${(time / 10) % 300}px)`;
  requestAnimationFrame(step);
}
requestAnimationFrame(step);
```

In background tabs Chrome stops calling rAF callbacks, which saves CPU and battery.

## 54: What is a frame and what does 60 fps mean for the browser?

A frame is one image shown on screen. Most screens refresh 60 times per second, so to look smooth the browser needs a new frame about every 16.7 ms. On 120 Hz screens that drops to about 8.3 ms.

In that time the browser must run JavaScript, style, layout, paint and compositing. In practice you have roughly 10 ms for your own code, because the browser needs the rest for its own work.

## 55: What is jank?

Jank is visible stutter: scrolling that jumps, animations that skip, or a page that reacts late to clicks. It happens when the browser misses frames because the main thread (or sometimes the GPU) is too busy.

Common causes are long JavaScript tasks, layout thrashing, heavy paint work and too many layers or large images.

## 56: What is a long task?

A long task is any task that runs on the main thread for more than 50 ms. During that time the page can't respond to input, so the user feels lag.

You can find them in the DevTools Performance panel (marked with red corners) or with the Long Tasks API:

```js
new PerformanceObserver((list) => {
  for (const entry of list.getEntries()) {
    console.log("Long task", entry.duration);
  }
}).observe({ type: "longtask", buffered: true });
```

## 57: What is a Web Worker and how does it relate to browser threads?

A Web Worker runs JavaScript on a separate thread inside the renderer process. It has no access to the DOM, and it talks to the main thread with `postMessage`.

```js
// main.js
const worker = new Worker("worker.js");
worker.postMessage(bigArray);
worker.onmessage = (e) => console.log("result", e.data);

// worker.js
onmessage = (e) => postMessage(e.data.reduce((a, b) => a + b, 0));
```

Workers are useful for heavy computation like parsing, image processing or compression, so the main thread stays free for rendering and input.

## 58: What is a Service Worker?

A Service Worker is a script that sits between your page and the network. It runs on its own thread, separate from any page, and can intercept `fetch` requests, serve responses from a cache, and handle push notifications and background sync.

It only works on HTTPS (or localhost). It has a lifecycle (install, activate) and Chrome stops it when it is idle and starts it again when an event comes in.

## 59: What is the call stack?

The call stack keeps track of which function is running and where to return when it finishes. When a function is called, a frame is pushed on the stack. When it returns, the frame is popped.

JavaScript in one thread has one call stack. The event loop only picks the next task when the stack is empty. If you recurse too deep you get `RangeError: Maximum call stack size exceeded`.

## 60: What is the heap in V8?

The heap is the memory area where V8 stores objects, arrays, closures and strings. Unlike the call stack, which is cleaned up automatically when functions return, heap memory is freed by the garbage collector when objects are no longer reachable.

You can inspect it with a heap snapshot in the DevTools Memory panel.

## 61: What is garbage collection?

Garbage collection is the automatic freeing of memory that the program can no longer reach. V8 starts from roots (global object, the current stack, handles held by the browser) and marks every object it can reach. Everything else is garbage and is freed.

You don't free memory yourself in JavaScript, but you can still leak memory by keeping references to things you don't need, like global arrays or forgotten event listeners.

## 62: What are common causes of memory leaks on a web page?

- Event listeners on elements or `window` that are never removed.
- Timers (`setInterval`) that keep running and hold references.
- Global variables or caches (Maps, arrays) that only grow.
- Detached DOM nodes: elements removed from the page but still referenced from JavaScript.
- Closures that hold on to large objects.
- Subscriptions or observers (`ResizeObserver`, WebSocket handlers) that are never cleaned up.

The DevTools Memory panel can show detached nodes and what is keeping objects alive.

## 63: What is JIT compilation?

JIT (just-in-time) compilation means compiling code to machine code while the program runs, instead of before. V8 starts by interpreting bytecode, watches which functions run often and what types they use, and then compiles those hot functions into optimized machine code.

This gives fast startup (no long compile at the start) and fast speed for code that runs a lot.

## 64: What is the difference between an interpreter and a compiler in V8?

The interpreter (Ignition) runs bytecode instruction by instruction. It starts quickly and uses little memory, but is slower.

The compilers (Sparkplug, Maglev and TurboFan) turn bytecode into machine code. They take time to compile, but the result runs much faster. V8 only compiles functions that are used enough to make the compile time worth it.

## 65: What is Ignition?

Ignition is V8's interpreter. After V8 parses your JavaScript, Ignition generates compact bytecode and runs it. While running, it collects feedback, such as which object shapes and types each operation sees.

That feedback is later used by the optimizing compilers to make good guesses about how to generate fast code.

## 66: What does V8 do with JavaScript source code before running it?

1. **Parsing**: the source is turned into an abstract syntax tree (AST). To save time, functions that are not called right away are only pre-parsed (checked for syntax) and fully parsed later when needed.
2. **Bytecode generation**: Ignition turns the AST into bytecode.
3. **Execution**: Ignition runs the bytecode and collects type feedback.
4. **Optimization**: hot functions are compiled to machine code by Sparkplug, Maglev or TurboFan.

V8 can also cache compiled code, so the next visit to the page skips parsing and compiling for cached scripts.

## 67: What are cookies and how does the browser handle them?

Cookies are small pieces of data a server sets with the `Set-Cookie` header (or JavaScript sets with `document.cookie`). The browser stores them and sends them back in the `Cookie` header on matching requests.

```http
Set-Cookie: session=abc123; Path=/; Secure; HttpOnly; SameSite=Lax; Max-Age=3600
```

Attributes control where and when they are sent. `HttpOnly` hides the cookie from JavaScript, `Secure` sends it only over HTTPS, and `SameSite` controls whether it is sent on cross-site requests. In Chrome, cookies are stored and managed by the network service.

## 68: What is the difference between localStorage and sessionStorage?

Both store string key-value pairs per origin with a simple synchronous API.

- **localStorage** stays until it is cleared, even after the browser is closed. It is shared by all tabs of the same origin.
- **sessionStorage** is per tab and lasts only as long as that tab. Opening the same site in a new tab gives a new, empty sessionStorage.

Both are synchronous and run on the main thread, so they are not good for large amounts of data.

## 69: What is IndexedDB?

IndexedDB is a database built into the browser for storing large amounts of structured data, including files and blobs. It is asynchronous, supports transactions and indexes, and is available in workers too.

It is used for offline apps, caching API data and storing drafts. The raw API is verbose, so many people use a small wrapper library like `idb`.

## 70: What is the Cache Storage API?

Cache Storage (`caches`) stores pairs of `Request` and `Response` objects. It is mostly used with Service Workers to build offline support.

```js
const cache = await caches.open("v1");
await cache.addAll(["/", "/app.js", "/styles.css"]);
const res = await caches.match("/app.js");
```

It is separate from the HTTP cache. The HTTP cache is controlled by headers and by the browser; Cache Storage is fully controlled by your code.

## 71: What is the same-origin policy?

The same-origin policy is the base security rule of the web. A script from one origin can't read data from another origin. For example, a page on `evil.com` can't read the DOM of an iframe from `bank.com` or read the body of a `fetch` response from `bank.com`.

Some things are allowed across origins: loading images, scripts, styles, submitting forms, embedding iframes. But reading the content is blocked unless the other origin allows it, for example with CORS.

## 72: What is CORS?

CORS (Cross-Origin Resource Sharing) is a way for a server to say which other origins can read its responses. The browser sends an `Origin` header, and the server answers with `Access-Control-Allow-Origin`.

```http
Access-Control-Allow-Origin: https://app.example.com
Access-Control-Allow-Credentials: true
```

If the header doesn't allow your origin, the request may still reach the server, but the browser hides the response from your JavaScript. CORS is enforced by the browser, not by the server.

## 73: What is Safe Browsing?

Safe Browsing is a Google service that keeps lists of dangerous sites (phishing, malware, unwanted software). Chrome checks URLs against it and shows a red warning page if you try to open a known bad site. It also checks downloads.

By default Chrome uses privacy-friendly hash prefix checks. "Enhanced protection" sends more data to Google for real-time checks and better protection.

## 74: What does Incognito mode actually do?

Incognito opens a separate, temporary profile. Cookies, site data, history and form data from that session are deleted when you close all Incognito windows. It starts with no cookies, so you aren't logged in to sites. Third-party cookies are blocked there by default.

It does not hide you from websites, your employer, your internet provider or the network. Sites still see your IP address, and anything you download or bookmark stays.

## 75: What is a Chrome profile?

A profile is a separate set of browser data: history, bookmarks, cookies, passwords, extensions and settings. Each profile has its own folder on disk and its own storage.

Profiles are useful for keeping work and personal accounts apart. In the code, each profile has its own network context, so cookies and caches are not shared between profiles.

## 76: What is Manifest V3 for Chrome extensions?

Manifest V3 is the current extension platform. The main changes from V2:

- Background pages are replaced by service workers that start and stop as needed.
- Blocking `webRequest` is replaced by `declarativeNetRequest`, where the extension gives rules and the browser applies them.
- Remotely hosted code is not allowed; all code must be in the extension package.
- More promise-based APIs.

Chrome has turned off Manifest V2 extensions, so new and existing extensions must use V3.

## 77: What are Chrome DevTools?

DevTools are the developer tools built into Chrome. Main panels:

- **Elements**: inspect and edit the DOM and CSS.
- **Console**: run JavaScript and see logs and errors.
- **Sources**: debug JavaScript with breakpoints.
- **Network**: see every request, timing and headers.
- **Performance**: record and analyze runtime performance.
- **Memory**: heap snapshots and allocation tracking.
- **Application**: storage, cookies, Service Workers, cache, bfcache testing.
- **Lighthouse**: audits for performance, accessibility and SEO.

DevTools talks to the page through the Chrome DevTools Protocol.

## 78: What are chrome:// pages and which ones are useful?

They are internal pages built into the browser. Useful ones:

- `chrome://version`: Chrome version, V8 version, command line flags, profile path.
- `chrome://flags`: experimental features.
- `chrome://gpu`: GPU and hardware acceleration status.
- `chrome://net-internals` and `chrome://net-export`: network debugging.
- `chrome://inspect`: debug devices, workers and remote targets.
- `chrome://process-internals`: Site Isolation and process info.
- `chrome://discards`: tab discarding and lifecycle state.
- `chrome://serviceworker-internals`: registered Service Workers.
- `chrome://about`: list of all chrome:// pages.

## 79: What is chrome://flags and should you rely on it?

`chrome://flags` lets you turn experimental features on or off. Developers use it to test new APIs before they ship or to check if a problem is caused by a new feature.

You should not rely on flags in production or tell users to change them. Flags can be removed or change behavior in any release, and most users never touch them. For testing new APIs on real users, origin trials are the right tool.

## 80: What are Chrome's release channels?

- **Stable**: what most users run.
- **Beta**: the next version, a few weeks before Stable.
- **Dev**: updated weekly, less stable.
- **Canary**: built every day from the latest code, may break.

There is also **Extended Stable** for enterprises, which updates every eight weeks. Developers often test their sites in Beta or Canary to catch problems before a change reaches Stable.

## 81: How often does Chrome release a new version?

From 2021, Chrome shipped a new major version every four weeks. Starting with Chrome 153 in September 2026, Chrome moved to a two-week release cycle on desktop, Android and iOS. Each release is smaller, so it's easier to find what caused a problem.

Extended Stable for enterprises stays on an eight-week cycle. Security fixes can come out at any time between releases.

## 82: How does Chrome update itself?

Chrome checks for updates in the background with its updater (Google Update on Windows, Keystone on macOS, the system package manager on Linux). It downloads the update while you browse and applies it the next time you restart Chrome. You'll see the "Relaunch to update" button when one is ready.

Updates are rolled out in stages to a percentage of users first, so Google can stop a bad release early.

## 83: What is the Chrome DevTools Protocol (CDP)?

CDP is the protocol that DevTools uses to control and inspect Chrome. It sends JSON messages over a WebSocket and is split into domains like `Page`, `DOM`, `Network`, `Runtime` and `Performance`.

Tools like Puppeteer and Playwright use CDP to automate Chrome. You can start Chrome with `--remote-debugging-port=9222` and connect to it.

## 84: What is headless Chrome?

Headless Chrome is Chrome running without a visible window. It is used for automated tests, scraping, generating PDFs and screenshots, and server-side rendering.

```bash
chrome --headless --screenshot=page.png https://example.com
chrome --headless --print-to-pdf=page.pdf https://example.com
```

The current headless mode (the default for `--headless` since Chrome 132) runs the same code as normal Chrome, so pages behave the same as in a real browser. The old, lighter headless implementation now ships as a separate binary called `chrome-headless-shell`.

## 85: What is the User-Agent string and what is UA reduction?

The User-Agent header tells servers which browser and OS made the request. It used to contain detailed info like the exact Chrome version and OS version.

Chrome reduced it to lower fingerprinting: the minor version numbers and detailed OS info are now frozen to fixed values. Sites that need detailed info can ask for it with User-Agent Client Hints (`Sec-CH-UA-*` headers or `navigator.userAgentData`). Feature detection is still better than UA sniffing.

## 86: What is the back/forward cache (bfcache)?

The bfcache keeps a full snapshot of a page in memory, including the JavaScript heap, when you navigate away. If you press Back or Forward, Chrome restores the page instantly instead of loading it again.

Not every page can be cached. For example, pages with an `unload` handler or certain open connections may be excluded. You can test a page in DevTools under Application > Back/forward cache.

## 87: What are the page lifecycle states?

The Page Lifecycle API describes these states:

- **Active**: visible and has focus.
- **Passive**: visible but not focused.
- **Hidden**: not visible (background tab, minimized window).
- **Frozen**: Chrome has paused timers and tasks to save resources.
- **Terminated**: the page is being unloaded.
- **Discarded**: Chrome killed the page to save memory; it reloads when you return.

Events like `visibilitychange`, `freeze`, `resume`, `pagehide` and `pageshow` tell you when the state changes.

## 88: How do you detect when a user switches away from your tab?

Use the `visibilitychange` event and `document.visibilityState`:

```js
document.addEventListener("visibilitychange", () => {
  if (document.visibilityState === "hidden") {
    saveDraft();
    navigator.sendBeacon("/analytics", JSON.stringify(stats));
  }
});
```

This is the most reliable place to save state or send analytics, especially on mobile, where the page may be killed later without any other event.

## 89: How does Chrome throttle background tabs?

To save CPU and battery, Chrome limits what hidden tabs can do:

- `requestAnimationFrame` callbacks stop.
- Timers run at most about once per second.
- After a page is hidden for 5 minutes and meets some conditions, chained timers wake up at most once per minute (intensive throttling).
- Pages can be frozen and later discarded if memory is low.

Pages playing audio or using some real-time features (like WebRTC) are mostly excluded.

## 90: What is Memory Saver?

Memory Saver is a Chrome setting that discards inactive tabs to free memory for the tabs you are using. A discarded tab stays in the tab strip, but its process is gone. When you click it, the page reloads.

Users can add sites to a list that is never discarded. As a developer, you should save important state (for example in `visibilitychange`) so a reload after a discard doesn't lose the user's work. `document.wasDiscarded` tells you if the page was reloaded after a discard.

## 91: What is Energy Saver?

Energy Saver is a Chrome mode that turns on when your laptop is on battery (and can be set to turn on at low battery). It limits background activity and lowers the frame rate of some visual effects like animations and video to save power.

## 92: What is hardware acceleration in Chrome?

Hardware acceleration means using the GPU for work like compositing layers, rasterizing content, playing video, WebGL and WebGPU. The GPU does this work much faster and with less power than the CPU.

You can check its status at `chrome://gpu`. If the GPU or its driver is on Chrome's blocklist, Chrome falls back to software rendering, which is slower.

## 93: What is Skia?

Skia is the open source 2D graphics library Chrome uses to draw shapes, text, images and gradients. Android and Flutter use it too.

Paint commands recorded by Blink are eventually played back through Skia during raster. Skia can draw on the CPU or the GPU. Its newer GPU backend, Graphite, is built for modern graphics APIs like Metal, Vulkan and Direct3D 12 and is replacing the older Ganesh backend.

## 94: How does the browser load web fonts?

The browser only downloads a web font when it knows text on the page needs it, which means after CSS is loaded and style is calculated. While the font loads, the text is either hidden (FOIT, flash of invisible text) or shown with a fallback font (FOUT, flash of unstyled text).

You control this with `font-display`:

```css
@font-face {
  font-family: "Inter";
  src: url("/fonts/inter.woff2") format("woff2");
  font-display: swap;
}
```

Preloading key fonts with `<link rel="preload" as="font" crossorigin>` makes them start downloading earlier.

## 95: How does native lazy loading work for images and iframes?

```html
<img src="photo.jpg" loading="lazy" width="800" height="600" alt="" />
<iframe src="https://example.com/map" loading="lazy"></iframe>
```

With `loading="lazy"`, Chrome waits to fetch the resource until it is near the viewport. The distance depends on the connection type. This saves bandwidth and helps the page load faster.

Don't lazy load images that appear in the first screen, especially the LCP image. It delays them and makes LCP worse.

## 96: What does the viewport meta tag do?

```html
<meta name="viewport" content="width=device-width, initial-scale=1" />
```

On mobile, without it Chrome lays out the page as if the screen were about 980 px wide and then shrinks it. With `width=device-width`, the layout width matches the device width in CSS pixels, so responsive CSS works as expected.

It also removes the old 300 ms tap delay on mobile Chrome, because the page is marked as mobile-friendly.

## 97: What is an iframe from the browser's point of view?

An iframe is a separate document with its own DOM, JavaScript global object and history inside a parent page. In Chrome, if the iframe is from a different site than the parent, Site Isolation puts it in a different renderer process (an out-of-process iframe).

The parent and iframe can only talk through `postMessage` if they are cross-origin. Many iframes on a page can cost a lot of memory and slow down loading.

## 98: What are resource hints like preconnect, dns-prefetch, preload and prefetch?

```html
<link rel="preconnect" href="https://cdn.example.com" />
<link rel="dns-prefetch" href="https://api.example.com" />
<link rel="preload" href="/hero.webp" as="image" />
<link rel="prefetch" href="/next-page.js" />
```

- **dns-prefetch**: do the DNS lookup early.
- **preconnect**: do DNS, TCP and TLS early.
- **preload**: download a resource needed for this page with high priority.
- **prefetch**: download a resource that may be needed for a future navigation, with low priority.

Too many hints compete with each other, so use them only for things you know are important.

## 99: How does the browser handle redirects?

When a server replies with `301`, `302`, `303`, `307` or `308` and a `Location` header, the browser makes a new request to that URL. Each redirect adds at least one round trip, and redirects to a new domain also need new DNS, TCP and TLS.

`301` and `308` are permanent and can be cached. `307` and `308` keep the original method and body; `301` and `302` may change a `POST` into a `GET`, and `303` always does. Chrome stops after 20 redirects with `ERR_TOO_MANY_REDIRECTS`.

## 100: What is mixed content?

Mixed content is when an HTTPS page loads resources over plain HTTP. It weakens the page's security, because those resources can be read or changed by someone on the network.

Chrome blocks mixed scripts, stylesheets, iframes and fetch requests. For images, audio and video it tries to upgrade the URL to HTTPS automatically, and blocks the request if HTTPS doesn't work.

## 101: What is HSTS?

HSTS (HTTP Strict Transport Security) is a response header that tells the browser to only use HTTPS for a domain for a given time.

```http
Strict-Transport-Security: max-age=63072000; includeSubDomains; preload
```

After Chrome sees it, any `http://` link to that domain is changed to `https://` inside the browser before a request is sent. Sites can also be added to the HSTS preload list, which ships inside Chrome, so even the very first visit uses HTTPS.

## 102: What is Content Security Policy?

CSP is a response header that tells the browser which sources of scripts, styles, images, frames and other content are allowed on a page. It is a strong defense against cross-site scripting (XSS).

```http
Content-Security-Policy: default-src 'self'; script-src 'self' 'nonce-r4nd0m'; object-src 'none'; base-uri 'none'
```

If an attacker injects a `<script>` without the right nonce, Chrome refuses to run it and reports a violation in the console.

## 103: How does Chrome's popup blocker decide what to block?

Chrome allows `window.open()` only when it is called during a user activation, like a click or a key press. Popups opened from timers, page load or after an `await` that took too long are blocked, and Chrome shows an icon in the address bar.

This "user activation" idea is used for other APIs too, such as fullscreen, playing audio with sound, and opening the file picker.

## 104: How do site permissions work in Chrome?

Powerful features like camera, microphone, location, notifications and clipboard reading need the user's permission. When a site asks, Chrome shows a prompt and remembers the decision per origin.

Most of these features only work on secure origins (HTTPS or localhost). You can check the state from JavaScript:

```js
const status = await navigator.permissions.query({ name: "geolocation" });
console.log(status.state); // 'granted', 'denied' or 'prompt'
```

The page can also use Permissions Policy to control which iframes are allowed to ask.

## 105: How does Chrome autofill forms?

Chrome saves addresses, payment cards and passwords and fills them in when it recognizes a form. It uses the `autocomplete` attribute, field names, labels and server-side predictions to work out what each field is.

```html
<input name="email" type="email" autocomplete="email" />
<input name="password" type="password" autocomplete="current-password" />
<input name="new-password" type="password" autocomplete="new-password" />
```

Correct `autocomplete` values make autofill and the password manager work much better.

## 106: What is WebAssembly and how does Chrome run it?

WebAssembly (Wasm) is a compact binary format that runs at near-native speed in the browser. You usually compile it from languages like C, C++ or Rust.

In Chrome, V8 runs Wasm. It first compiles the module quickly with a baseline compiler called Liftoff so it can start fast, and then recompiles hot functions with TurboFan for better speed. Compiled modules can be cached, so the next load is faster.

## 107: What are WebGL and WebGPU?

Both let a page use the GPU for graphics.

- **WebGL** is based on OpenGL ES. It is older and supported everywhere. In Chrome, its calls go through ANGLE, which translates them into Direct3D, Metal, Vulkan or OpenGL.
- **WebGPU** is the newer API, built around modern APIs like Vulkan, Metal and Direct3D 12. It supports compute shaders and gives more control. Chrome shipped it in Chrome 113 and implements it with a library called Dawn.

Both run their GPU work in the GPU process, not in the renderer.

## 108: What is the difference between JavaScript and Web APIs?

JavaScript (ECMAScript) is the language: syntax, types, objects, promises, `Array`, `Map` and so on. V8 implements it.

Web APIs are features the browser gives to JavaScript: the DOM, `fetch`, `setTimeout`, `localStorage`, Canvas, `WebSocket` and many more. Blink implements these. That's why `document` exists in Chrome but not in plain Node.js, even though both use V8.

## 109: What are Core Web Vitals?

Core Web Vitals are three metrics Google uses to measure real user experience:

- **LCP** (Largest Contentful Paint): loading speed. Good is 2.5 s or less.
- **INP** (Interaction to Next Paint): responsiveness. Good is 200 ms or less.
- **CLS** (Cumulative Layout Shift): visual stability. Good is 0.1 or less.

They are measured at the 75th percentile of real page loads. Chrome collects real-world data from opted-in users in the Chrome UX Report (CrUX).

## 110: What is LCP?

LCP (Largest Contentful Paint) is the time from the start of the navigation until the largest image or text block in the viewport is painted. It usually corresponds to the hero image, a heading or a big paragraph.

To improve it: make the server respond faster, don't lazy load the LCP image, preload it or add `fetchpriority="high"`, reduce render-blocking CSS and JavaScript, and serve smaller images.

## 111: What is INP?

INP (Interaction to Next Paint) measures how long it takes from a user interaction (click, tap or key press) until the next frame is painted. It looks at all interactions during the page visit and reports one of the worst ones.

INP replaced First Input Delay (FID) as a Core Web Vital in March 2024. FID only measured the delay before the first handler started; INP covers the whole time, including your handler and the rendering after it.

## 112: What is CLS?

CLS (Cumulative Layout Shift) measures how much visible content moves around unexpectedly while the page is open. Content jumping because an image loaded without a size or an ad was inserted are typical causes.

To avoid it: set `width` and `height` (or `aspect-ratio`) on images and videos, reserve space for ads and embeds, avoid inserting content above existing content, and use `font-display` with fallback fonts that have similar size. Shifts within 500 ms after user input don't count.

## 113: What are TTFB and FCP?

- **TTFB** (Time to First Byte): time from the start of the navigation until the first byte of the response arrives. It includes redirects, DNS, connection setup and server time.
- **FCP** (First Contentful Paint): time until the browser first paints any content, like text or an image.

A slow TTFB pushes back every other metric, because nothing can render before the HTML starts arriving.

## 114: What is Lighthouse?

Lighthouse is an open source tool that audits a page for performance, accessibility, best practices and SEO. It loads the page in a controlled environment, usually with simulated slow network and CPU, and gives scores and suggestions.

It runs in DevTools, from the command line and in PageSpeed Insights. Its results are lab data. They are great for debugging but don't always match what real users see.

## 115: What does the DevTools Performance panel show?

It records what the browser does over time. You see:

- A timeline of frames and screenshots.
- The main thread flame chart: tasks, JavaScript functions, style, layout, paint.
- Other threads like the compositor, raster threads and GPU.
- Network requests.
- Web Vitals markers like LCP and layout shifts.

It is the main tool for finding long tasks, layout thrashing and slow rendering. You can also throttle the CPU to simulate a slower device.

## 116: How do you read the Network panel waterfall?

Each row is a request, and the bar shows its timing phases:

- **Queueing/Stalled**: waiting for a connection or behind higher-priority requests.
- **DNS Lookup**, **Initial connection**, **SSL**: connection setup.
- **Request sent**.
- **Waiting for server response**: server think time plus one round trip.
- **Content Download**.

Long chains of requests that each wait for the previous one are a sign that you should preload or flatten the dependency chain.

## 117: What is the difference between DOMContentLoaded and load?

- **DOMContentLoaded** fires when the HTML is fully parsed and all deferred and module scripts have run. Images, iframes and stylesheets may still be loading (although stylesheets that block scripts will have loaded).
- **load** fires when everything on the page has finished loading, including images, iframes and styles.

```js
document.addEventListener("DOMContentLoaded", init);
window.addEventListener("load", () => console.log("all done"));
```

`document.readyState` moves from `loading` to `interactive` to `complete` along the same steps.

## 118: What is a same-document navigation?

It is a navigation that changes the URL without loading a new document, for example clicking an `#anchor` link or calling `history.pushState()`. Single-page apps use it for routing.

```js
history.pushState({ page: 2 }, "", "/products?page=2");
window.addEventListener("popstate", (e) => render(e.state));
```

No network request is made for the page itself, and the JavaScript state stays. The newer Navigation API (`navigation.navigate()` and the `navigate` event) makes this easier to manage.

## 119: What is the difference between standards mode and quirks mode?

If a page has `<!DOCTYPE html>` at the top, Chrome renders it in standards mode, following the current CSS rules. Without a doctype (or with some old ones), it uses quirks mode, which copies the bugs of old browsers from the late 1990s for backward compatibility.

In quirks mode some things act differently, like the box model in some cases and how percentage heights work. Always start pages with `<!DOCTYPE html>`.

## 120: What is the accessibility tree?

The accessibility tree is a tree the browser builds from the DOM and styles for screen readers and other assistive tools. Each node has a role (button, heading, link), a name, a state (checked, expanded) and a value.

Chrome creates it only when an assistive technology is active (or DevTools asks for it). You can see it in DevTools under Elements > Accessibility. Using semantic HTML gives you a correct tree for free.

## 121: How does the browser handle Shadow DOM?

Shadow DOM lets an element have its own hidden DOM tree, the shadow tree, with its own scoped styles. Styles inside don't leak out, and page styles mostly don't leak in.

```js
const host = document.querySelector("#card");
const root = host.attachShadow({ mode: "open" });
root.innerHTML = `<style>p { color: red; }</style><p>Inside</p>`;
```

For rendering, Blink combines the light DOM and shadow DOM into a "flat tree" (slots are filled with the assigned children) and does style and layout on that. Built-in elements like `<video>` and `<input type="range">` use a shadow tree internally too.

## 122: How does Chrome show PDF files?

Chrome has a built-in PDF viewer. The PDF is parsed and drawn by PDFium, an open source PDF library, and the viewer UI is a small web app inside the browser. Newer versions run the viewer in an out-of-process iframe, so PDFs are isolated like other content.

PDFium is written in C++ and parses untrusted files, so it runs in a sandboxed process.

## 123: How does Chrome play video?

The `<video>` element downloads media (or gets it through Media Source Extensions for streaming). The data is demuxed into audio and video streams, decoded (using hardware decoders on the GPU when possible), and the decoded frames are handed to the compositor to draw.

Video usually gets its own compositor layer, so it can update every frame without repainting the page. Support for codecs like H.264, VP9 and AV1 depends on the platform and build.

## 124: What are blob URLs and data URLs?

- **Data URL**: the content is inside the URL itself, like `data:image/png;base64,iVBORw0...`. Good for tiny resources, but base64 is about 33% larger and can't be cached on its own.
- **Blob URL**: created with `URL.createObjectURL(blob)`, like `blob:https://site.com/uuid`. It points to data held in memory by the browser.

```js
const url = URL.createObjectURL(file);
img.src = url;
img.onload = () => URL.revokeObjectURL(url); // free the memory
```

If you don't revoke blob URLs, the data stays in memory until the page is closed.

## 125: What is FOUC?

FOUC (flash of unstyled content) is when the page shows raw unstyled HTML for a moment before CSS applies. It happens when CSS is loaded in a way that doesn't block rendering, for example injected with JavaScript or loaded late in the body.

Chrome avoids this for normal `<link rel="stylesheet">` in `<head>` because those block rendering. The trade-off is that a large or slow stylesheet delays the first paint.

## 126: What happens when you close a tab?

Chrome fires `beforeunload` (if a handler is registered), then `pagehide` and `visibilitychange`. The page may be stored in the bfcache when you navigate away, but closing the tab destroys it. If no other tab is using the renderer process, Chrome shuts the process down and the OS reclaims its memory.

Chrome tries to make closing feel fast, so it may hide the tab right away while the unload work finishes in the background. That's why you should not rely on `unload` for important work.

## 127: Does every tab get its own process?

Not always. Chrome usually gives each site its own process, so different sites are in different processes. But tabs of the same site can share a process (for example two tabs opened by links from the same page), and when there are many tabs, Chrome may reuse processes of the same site to save memory.

Cross-site pages are never put together in one process on desktop, because of Site Isolation. On Android with low memory, Chrome isolates only some sites (like ones you log in to), so other sites may share processes.

## 128: How does scrolling work at a basic level?

When you scroll, the input goes from the browser process to the renderer's compositor thread. If the page has no blocking scroll listeners, the compositor scrolls the already-rastered content on its own, without asking the main thread. That's why scrolling usually stays smooth even when JavaScript is busy.

The main thread is informed afterwards and fires `scroll` events. If the page has non-passive `touchstart` or `wheel` listeners, the compositor has to wait for the main thread first, which can make scrolling laggy.

## 129: What image formats does Chrome support and why does it matter?

Chrome supports JPEG, PNG, GIF, WebP, AVIF, SVG, ICO and BMP. WebP and AVIF usually give much smaller files than JPEG and PNG at similar quality. JPEG XL was removed in 2022, then came back in Chrome 155 with a new decoder written in Rust (jxl-rs).

Smaller images download faster and decode faster, which helps LCP. You can serve the best format with `<picture>`:

```html
<picture>
  <source srcset="hero.avif" type="image/avif" />
  <source srcset="hero.webp" type="image/webp" />
  <img src="hero.jpg" alt="Hero" width="1200" height="600" />
</picture>
```

## 130: What is a browser-initiated vs a renderer-initiated navigation?

A **browser-initiated** navigation starts from the browser UI: typing in the address bar, clicking a bookmark, pressing Back. The browser process starts it directly.

A **renderer-initiated** navigation starts from the page: clicking a link, submitting a form, or setting `location.href`. The renderer asks the browser process to navigate, and the browser process decides what happens. Some checks are different, for example renderer-initiated navigations need to pass more security checks.

## 131: What does the beforeunload event do?

`beforeunload` fires when the page is about to be left or closed. If the handler cancels it, Chrome shows a generic "Leave site?" dialog. You can't customize the text.

```js
window.addEventListener("beforeunload", (e) => {
  if (hasUnsavedChanges) e.preventDefault();
});
```

Chrome only shows the dialog if the user has interacted with the page. Add the listener only when there are unsaved changes and remove it afterwards.

## 132: What is the user agent stylesheet?

It is the browser's built-in default CSS. It's why `<h1>` is big and bold, `<body>` has an 8 px margin, links are blue and underlined, and `<div>` is `display: block`.

Your styles override it through the normal cascade. CSS resets and normalize files exist to make these defaults the same across browsers.

## 133: What is the difference between display: none, visibility: hidden and opacity: 0 for rendering?

- **display: none**: the element is not in the layout tree. It takes no space and isn't painted. Toggling it causes layout.
- **visibility: hidden**: the element keeps its space in layout but isn't painted. It can't be clicked.
- **opacity: 0**: the element is laid out and painted but fully transparent. It can still be clicked, and animating opacity can run on the compositor.

## 134: What is HTTP compression and which formats does Chrome support?

The browser lists the formats it understands in the `Accept-Encoding` header, and the server compresses text responses (HTML, CSS, JS, JSON) with one of them.

```http
Accept-Encoding: gzip, deflate, br, zstd
Content-Encoding: br
```

Chrome supports gzip, Brotli (`br`) and Zstandard (`zstd`). Brotli and zstd usually give smaller files than gzip. Images and videos are already compressed, so compressing them again doesn't help.

## 135: What is the difference between a normal reload, a hard reload and "Empty cache and hard reload"?

- **Normal reload** (`F5` / `Ctrl+R`): reloads the page and revalidates the main resource. Other resources may still come from the cache.
- **Hard reload** (`Ctrl+Shift+R` / `Cmd+Shift+R`): fetches resources again without using the cache.
- **Empty cache and hard reload** (right-click the reload button with DevTools open): clears the cache for the page and reloads, which also catches resources loaded later by JavaScript.

The "Disable cache" checkbox in the Network panel turns off the HTTP cache while DevTools is open.

## 136: What is HTTP keep-alive and connection reuse?

Opening a new connection costs DNS, TCP and TLS round trips. With keep-alive (the default in HTTP/1.1), the browser keeps connections open after a response and reuses them for later requests to the same origin.

HTTP/2 and HTTP/3 go further: many requests share one connection at the same time. Chrome keeps pools of idle connections and closes them after a timeout.

## 137: What language is Chrome written in?

Most of Chromium is written in C++. Parts of the UI on some platforms use Objective-C++ (macOS, iOS) and Java or Kotlin (Android). Internal pages like Settings are built with HTML, CSS and TypeScript.

Chromium also uses more and more Rust for new code that handles untrusted input, for example font parsing and some image decoders, because Rust prevents many memory bugs.

## 138: What is a Progressive Web App from the browser's point of view?

A PWA is a website that Chrome lets users install like an app. It needs HTTPS and a web app manifest with name, icons and `start_url`. A Service Worker adds offline support.

```html
<link rel="manifest" href="/manifest.webmanifest" />
```

After installing, the app opens in its own window without the address bar, appears in the OS app list, and can use features like badges, file handling and protocol handlers.

## 139: What is a stacking context?

A stacking context is a group of elements that are painted together and ordered by `z-index` inside the group. It is created by things like `position` with a `z-index`, `opacity` less than 1, `transform`, `filter`, `isolation: isolate` and `will-change` for some properties.

A child can never appear above an element outside its stacking context if the parent context is lower. This is the usual reason why `z-index: 9999` "doesn't work."

## 140: What does Chrome do when a page uses too much memory?

If a renderer process gets close to its memory limit, V8 runs garbage collection more aggressively. If memory still can't be found, the renderer crashes with an out-of-memory error and you see "Aw, Snap!" with error code `Out of Memory`.

At the system level, when the device is low on memory, Chrome can discard background tabs, and on Android the OS can kill background renderer processes.

## 141: How does Chrome handle a page that is not responding?

If the main thread of a renderer is stuck (for example an endless loop), the browser process notices the renderer doesn't answer input events in time. After a while it shows a "Page Unresponsive" dialog with "Wait" or "Exit page."

Other tabs keep working because they run in other processes. Inside the stuck tab, the compositor may still scroll content that was already rastered.

## 142: What is the difference between a tab, a window and a frame in Chrome?

- A **window** holds one or more tabs.
- A **tab** shows one page, which internally is a tree of frames (called a frame tree).
- A **frame** is a document: the main frame is the top page, and each iframe is a child frame.

Different frames in the same tab can be in different renderer processes if they are from different sites. The browser process keeps the full frame tree for each tab.

## 143: What is the difference between the window object and the document object?

`window` is the global object for a frame. It holds global variables and browser APIs like `setTimeout`, `location`, `history`, `localStorage` and `fetch`.

`document` is the DOM of the page loaded in that window, with methods like `querySelector` and `createElement`. When you navigate, a new document is loaded, and normally a new `window` is created too. Each iframe has its own `window` and `document`.

## 144: How much data can a site store in Chrome?

Chrome gives each origin a quota based on the free disk space. An origin can use up to about 60% of the total disk size. You can check the current usage:

```js
const { usage, quota } = await navigator.storage.estimate();
console.log(`${usage} of ${quota} bytes used`);
```

Data is "best effort" by default, so Chrome may delete it when disk space is low. Calling `navigator.storage.persist()` asks Chrome to keep it unless the user clears it.

## 145: What is a secure context?

A secure context is a page loaded over HTTPS, or from `localhost`, or a file URL. Many powerful APIs only work in secure contexts: Service Workers, geolocation, camera and microphone, the Clipboard API, Web Crypto's `subtle`, WebGPU and more.

You can check it with `window.isSecureContext`. An HTTPS iframe inside an HTTP page is not a secure context.

## 146: What is the difference between the memory cache and the disk cache?

Chrome keeps some resources in an in-memory cache inside the renderer for the current page. It's very fast and is used for things requested more than once during the same page load, like the same image used twice. It's cleared when the page goes away.

The disk cache is the HTTP cache managed by the network service. It stays between visits and browser restarts. In the Network panel, the Size column shows "(memory cache)" or "(disk cache)."

## 147: How does Chrome decide the order in which to download resources?

Chrome gives each request a priority based on its type and position: the main HTML, CSS in the head and fonts are highest; scripts are high or medium; images are low until they are found in the viewport; async scripts and prefetches are low.

You can change priority with `fetchpriority`:

```html
<img src="hero.jpg" fetchpriority="high" alt="" />
<script src="widget.js" async fetchpriority="low"></script>
```

You can see the priority of each request in the Network panel by enabling the "Priority" column.

## 148: Why is it bad to use document.write?

`document.write` inserts HTML into the parser at the current position. If it's used to add a script, the parser has to stop, download and run that script. On slow connections Chrome may even block `document.write` scripts from other origins.

If called after the page has loaded, it erases the whole document. Use DOM methods like `append` or `insertAdjacentHTML` instead.

## 149: What happens when JavaScript throws an uncaught error?

The current task stops at that point. The error is logged in the console and the `error` event fires on `window`. Other tasks, event handlers and timers keep running, so the page usually keeps working partly.

For promises, an unhandled rejection fires the `unhandledrejection` event. Error tracking tools listen to both events to report errors from real users.

## 150: What is the difference between innerHTML and textContent for the browser?

Setting `innerHTML` makes the browser run the HTML parser on the string, build new DOM nodes and replace the old ones. It is slower and can lead to XSS if the string contains user input.

Setting `textContent` just creates one text node. It doesn't parse anything, so it's faster and safe for user input.

```js
el.textContent = userInput; // safe
el.innerHTML = userInput; // dangerous with untrusted data
```

---

# Moderate Questions (151-300)

## 151: Walk through a navigation in Chrome step by step, process by process.

1. **Browser process, UI thread**: you press Enter. Chrome checks the input, runs `beforeunload` on the current page if needed, and starts a navigation.
2. **Network service**: does DNS, connects, sends the request, follows redirects. Safe Browsing checks run in parallel.
3. **Browser process**: when the response headers arrive, it looks at the `Content-Type`. If it's a download, it hands it to the download manager. If it's HTML, it picks or creates a renderer process for the site.
4. **Commit**: the browser process tells the renderer to commit the navigation and streams the body to it over a data pipe. The URL bar and history update.
5. **Renderer process**: parses, loads subresources, runs scripts, renders. When it's done it reports back so the browser can stop the loading spinner.

## 152: Why does Chrome start a renderer process before the network response arrives?

Starting a process takes time, tens of milliseconds or more. To hide that cost, Chrome often starts a renderer early, in parallel with the network request, as a guess. Chrome also keeps a "spare" renderer process ready on desktop so a new navigation can use it right away.

If the response turns out to be a redirect to another site or a download, Chrome drops or reuses the early process instead.

## 153: What is Mojo?

Mojo is Chromium's IPC system. It gives you message pipes between processes (or threads), and you define interfaces in `.mojom` files. A code generator creates C++, Java and JavaScript bindings.

```mojom
interface Calculator {
  Add(int32 a, int32 b) => (int32 sum);
};
```

One side holds a `Remote<Calculator>` and calls methods; the other side holds a `Receiver` and implements them. Almost all communication between the browser, renderers, the GPU process and services goes over Mojo.

## 154: What is the network service's relation to the renderer when you call fetch()?

The renderer can't open sockets because it's sandboxed. When JavaScript calls `fetch()`, Blink creates a request and sends it over Mojo to a `URLLoaderFactory` in the network service. The network service makes the request, applies CORS and cookie rules, reads the cache, and streams the response back through a Mojo data pipe.

The browser process gives each renderer a URLLoaderFactory that is bound to the right origin and settings, so a compromised renderer can't pretend to be another origin.

## 155: How does Chrome decide which renderer process to use for a navigation?

It uses the site of the destination URL. Chrome looks for a process locked to the same site that it can reuse (for example in the same browsing context group), and otherwise creates a new one or uses the spare process.

Each process is "locked" to one site after it commits a document. Pages that need a different site get a different process. Special pages like `chrome://` internal pages, extensions and error pages get their own process types.

## 156: What is a browsing context group and why does it matter for processes?

A browsing context group is a set of windows that can script each other, for example a page and a popup it opened with `window.open()`, which keeps a reference through `window.opener`.

Same-site pages in the same group must share a process, because they can access each other's objects directly. Setting `rel="noopener"` or the `Cross-Origin-Opener-Policy` header breaks this link, which lets Chrome put the new page in a separate group and process.

## 157: What is an out-of-process iframe (OOPIF)?

An OOPIF is an iframe that runs in a different renderer process from its parent page, because it's from a different site. The parent process only has a placeholder (a "proxy") for it. The two processes talk through the browser process, for example for `postMessage`.

Each process renders its own part, and Viz in the GPU process combines the outputs into one frame. This is the core of Site Isolation, and it means the parent page's process never has the iframe's memory.

## 158: What is a RenderFrameHost and a RenderFrame?

These are two halves of a frame in Chromium's code:

- **RenderFrameHost** lives in the browser process. It represents one document in one frame and talks to the renderer.
- **RenderFrame** (and Blink's `LocalFrame`) lives in the renderer process and actually holds the document.

When a frame is in another process, the renderer has a `RemoteFrame` proxy instead. Interview questions about this test if you understand how Chrome keeps a frame tree split across processes.

## 159: What is MIME sniffing and how does Chrome use it?

MIME sniffing is guessing a resource's type from its content when the `Content-Type` header is missing or wrong. Chrome does some sniffing to decide whether a response is HTML, a download or something else.

Sniffing can be a security problem, for example an uploaded image being run as script. The `X-Content-Type-Options: nosniff` header tells Chrome to trust `Content-Type` and block scripts and styles with the wrong type.

## 160: How does speculative parsing interact with document.write?

When the main parser is blocked on a script, the preload scanner keeps reading ahead and starts downloads. If the script then calls `document.write`, it can insert new HTML that changes what comes next, so the browser may have done some useless work.

This is one reason `document.write` is discouraged. Chrome also blocks `document.write` of cross-origin parser-blocking scripts on slow 2G connections.

## 161: Why does CSS block JavaScript execution?

A script might read styles, for example with `getComputedStyle()` or `offsetWidth`. If CSS hasn't loaded yet, those values would be wrong. So the browser waits for pending stylesheets before running a parser-blocking or deferred script that comes after them.

So a slow stylesheet can delay JavaScript, which then delays the parser. Putting `async` scripts before stylesheets, or inlining critical CSS, can reduce this chain.

## 162: How does selector matching work and why is it right to left?

The browser matches selectors from right to left. For `.nav li a`, it starts with each `a` element and then walks up the tree to check if there is an `li` ancestor and then a `.nav` ancestor.

Right to left is faster because most elements fail the rightmost part right away. Blink also uses bloom filters of ancestor info and buckets rules by their rightmost class, ID or tag, so it only tests rules that could possibly match.

## 163: What is style invalidation?

When something changes, like a class being added, Blink doesn't recalculate style for the whole page. It uses invalidation sets built from your selectors to work out which elements could be affected and marks only those for recalc.

Broad selectors make invalidation more expensive. For example, a rule like `.theme-dark *` means that changing the `theme-dark` class affects every descendant. `:has()` is powerful but can also cause wider invalidation.

## 164: What is layout thrashing (forced synchronous layout)?

Layout thrashing happens when JavaScript writes to the DOM and then reads a layout value in a loop. Each read forces Chrome to do layout right away, so you get many layouts in one frame instead of one.

```js
// Bad: layout on every iteration
for (const el of items) {
  el.style.width = box.offsetWidth + "px";
}

// Good: read once, then write
const width = box.offsetWidth;
for (const el of items) {
  el.style.width = width + "px";
}
```

DevTools marks these as "Forced reflow" warnings in the Performance panel.

## 165: Which DOM properties and methods force layout?

Reading anything that depends on current geometry forces layout if something has changed: `offsetTop/Left/Width/Height`, `clientWidth/Height`, `scrollTop`, `scrollHeight`, `getBoundingClientRect()`, `getClientRects()`, `getComputedStyle()` (for layout-dependent values), `innerText`, `focus()` and `scrollIntoView()`.

Group your reads before your writes, or move reads into `requestAnimationFrame` before you change anything.

## 166: What is LayoutNG?

LayoutNG is Blink's current layout engine, which replaced the old one fully around Chrome 108. Its main idea is that layout takes inputs (constraints like available width) and produces an immutable fragment tree as output, instead of changing objects in place.

This made layout more correct and easier to reason about, fixed many old bugs (especially with floats, fragmentation and writing modes), and makes caching of layout results more reliable.

## 167: What is the fragment tree?

The fragment tree is the output of LayoutNG. Each fragment holds the final size and position of a box (or a part of a box, like one line of text or one column of a multi-column layout).

Fragments are immutable, so later stages like paint can read them safely and reuse unchanged ones between frames. An element split across several lines or columns has several fragments.

## 168: What are paint records and display items?

When Blink paints, it doesn't draw pixels. It records a list of drawing operations, called display items, like "draw rect here with this color" or "draw this text." These are grouped in paint chunks with shared properties (transform, clip, effect).

The list can be cached. If only part of the page changed, Blink repaints only those items and reuses the rest. The list is later sent to the compositor and played back during raster.

## 169: What is raster?

Raster is turning paint commands into pixels. Chrome splits layers into tiles (often 256x256 or larger) and rasterizes the tiles near the viewport first, on raster worker threads or on the GPU.

Today most raster happens on the GPU, in the GPU process (out-of-process raster), using Skia. The results are stored as GPU textures, which the compositor then draws.

## 170: What is the compositor thread?

The compositor thread is a separate thread in the renderer process (called `cc`, the Chromium compositor). It takes the layer tree and paint output from the main thread, decides which tiles to rasterize, handles scrolling and compositor animations, and produces compositor frames.

Because it doesn't run JavaScript, it can keep scrolling and run transform or opacity animations smoothly even while the main thread is busy.

## 171: What makes an element get its own compositor layer?

Common reasons:

- 3D transforms or `will-change: transform` / `opacity`.
- An active CSS animation or transition on `transform`, `opacity` or some `filter`s.
- `<video>`, `<canvas>` with WebGL or accelerated 2D, and iframes from other processes.
- Scrolling containers that can be composited.
- `position: fixed` and `sticky` elements in some cases.
- Overlapping something that's already on a layer (an implicit reason).

The Layers panel in DevTools shows each layer and the reason it was created.

## 172: What does will-change do and when should you use it?

`will-change` tells the browser that a property is about to change, so it can prepare, usually by putting the element on its own layer ahead of time.

```css
.drawer {
  will-change: transform;
}
```

Use it only for elements that will animate soon, and remove it when done if you set it from JavaScript. Every layer uses GPU memory, and putting `will-change` on many elements can make performance worse. It also creates a stacking context and a containing block for fixed children.

## 173: What is layer explosion?

Layer explosion is when the page ends up with a huge number of compositor layers. It often happens because of overlap: if one element is on a layer, elements painted above it that overlap must also get layers to keep the correct order.

Too many layers use a lot of GPU memory and make compositing slow. You can find this in the Layers panel and fix it by changing `z-index` order, removing unneeded `will-change`, or reducing overlap.

## 174: Why are transform and opacity animations "compositor-only"?

When an element is on its own layer, `transform` and `opacity` only change how the layer is drawn, not what is inside it. The compositor thread can update them every frame using the existing textures on the GPU, without style, layout, paint or even the main thread.

So these animations keep running smoothly while JavaScript is busy. If you animate `width` or `top`, each frame needs the main thread for layout and paint.

## 175: What are passive event listeners and why do they help scrolling?

A passive listener promises not to call `preventDefault()`, so the browser doesn't have to wait for it before scrolling.

```js
window.addEventListener("touchstart", onTouch, { passive: true });
```

Without it, the compositor must send the event to the main thread and wait, because the handler might cancel the scroll. If the main thread is busy, scrolling stalls. Chrome treats `touchstart`, `touchmove` and `wheel` listeners on `window`, `document` and `body` as passive by default.

## 176: What is the non-fast scrollable region?

It's an area of the page the compositor knows has event handlers (like non-passive `touchstart` or `wheel` listeners) that could block scrolling. When input lands in that region, the compositor must ask the main thread before it scrolls.

Attaching non-passive listeners to large containers or `document` turns the whole page into such a region. Attaching them to small, specific elements keeps most scrolling on the fast path.

## 177: How does an input event travel from the OS to your JavaScript handler?

1. The OS sends the event to the browser process.
2. The browser process figures out which renderer is under the pointer (hit testing in Viz, important for OOPIFs) and sends the event to it.
3. The renderer's compositor thread gets it first. If it can handle it alone (like a scroll with no blocking handlers), it does.
4. Otherwise the event is forwarded to the main thread, where Blink does a hit test on the layout tree to find the target element and dispatches the DOM event.

Continuous events like `mousemove` and `touchmove` are lined up with frames (input alignment), so they are delivered at most once per frame.

## 178: What is the touch-action CSS property?

`touch-action` tells the browser which touch gestures it may handle itself, like panning or pinch-zoom, on an element.

```css
.map {
  touch-action: none;
} /* the app handles all touch */
.carousel {
  touch-action: pan-y;
} /* browser handles vertical scroll only */
```

Because the compositor can read it without running JavaScript, it can start scrolling right away in allowed directions. It is better than calling `preventDefault()` in touch handlers.

## 179: In what order does the browser do work within one frame?

Roughly, in the renderer's main thread:

1. Input events (aligned to the frame) are dispatched.
2. `requestAnimationFrame` callbacks run.
3. Style calculation.
4. Layout.
5. Paint (record display items).
6. Commit to the compositor thread.

Then the compositor rasterizes tiles if needed, builds a compositor frame and sends it to Viz, which draws it on screen at the next VSync. `ResizeObserver` and `IntersectionObserver` callbacks also run inside this update.

## 180: What is VSync?

VSync is the signal from the display that it is about to show a new frame, 60 times per second on a 60 Hz screen. Chrome uses it to time rendering: a BeginFrame message is sent to renderers on each VSync, telling them to start producing the next frame.

If a frame isn't ready in time, the screen shows the old one again and a frame is "dropped." This is what users see as jank.

## 181: What is Viz?

Viz is Chrome's display compositor service. It runs in the GPU process. Every renderer and the browser UI send compositor frames to Viz, and Viz combines them (surface aggregation) into one final frame and draws it to the screen.

Viz also sends BeginFrame signals, handles hit testing for input across processes, and manages GPU resources. Moving display compositing into the GPU process was part of the RenderingNG work.

## 182: What is a compositor frame?

A compositor frame is what a renderer sends to Viz for each new image. It contains render passes with "draw quads" (rectangles to draw with a texture, color or video frame) and references to resources like GPU textures.

It also can reference other "surfaces" by ID, for example a cross-process iframe. Viz replaces these references with the latest frame from that surface when building the final image.

## 183: What is content-visibility and how does it help rendering?

`content-visibility: auto` lets the browser skip style, layout and paint for an element's contents while it is off-screen.

```css
.article-section {
  content-visibility: auto;
  contain-intrinsic-size: auto 800px;
}
```

On long pages this can make the first render much faster. `contain-intrinsic-size` gives a placeholder size so the scrollbar doesn't jump. The content is still in the DOM, so find-in-page and accessibility still work.

## 184: What is CSS containment?

The `contain` property tells the browser that an element's subtree is independent from the rest of the page in some way:

- `layout`: inside layout doesn't affect outside.
- `paint`: children don't paint outside its box.
- `size`: its size doesn't depend on its children.
- `style`: counters and quotes don't leak.

```css
.widget {
  contain: layout paint;
}
```

This lets Blink limit how much work a change causes, for example a change inside the widget doesn't need layout of the whole page.

## 185: How does Chrome decode images and why can it be slow?

Downloaded images are compressed. Before drawing, they must be decoded into raw pixels, which for a big JPEG can take tens of milliseconds and a lot of memory (width x height x 4 bytes).

Chrome decodes images during raster, mostly off the main thread, and caches decoded results. Very large images still cause long raster times and memory pressure. Serve images at the size they're shown, and use `decoding="async"` or `img.decode()` when you need control.

```js
const img = new Image();
img.src = "/big.jpg";
await img.decode(); // decoded, safe to insert without a stutter
document.body.append(img);
```

## 186: How many connections does Chrome open per host?

For HTTP/1.1, Chrome opens at most 6 connections per host (and has an overall limit of around 256 sockets per profile). Extra requests wait in the queue, which you see as "Stalled" or "Queueing" in DevTools.

With HTTP/2 and HTTP/3, all requests to an origin usually go over one connection, so this limit doesn't matter as much. Old tricks like domain sharding are harmful with HTTP/2.

## 187: What is HTTP/2 connection coalescing?

If two hostnames resolve to the same IP and the TLS certificate covers both, Chrome can reuse one HTTP/2 connection for both, instead of opening a second one. For example, `www.example.com` and `static.example.com` may share a connection.

This saves the cost of a new DNS, TCP and TLS setup. HTTP/3 supports something similar.

## 188: How does Chrome find out a server supports HTTP/3?

Two common ways:

- **Alt-Svc header**: the server responds over HTTP/2 with `Alt-Svc: h3=":443"; ma=86400`. Chrome remembers it and tries HTTP/3 next time.
- **HTTPS DNS record**: the domain's DNS has an HTTPS record listing `h3` in its ALPN values, so Chrome can try HTTP/3 on the first connection.

Chrome races QUIC with a TCP connection in some cases, so if UDP is blocked the page still loads over HTTP/2.

## 189: What are 103 Early Hints?

`103 Early Hints` is an informational response a server can send before the final response. It usually contains `Link` headers with preload or preconnect hints.

```http
HTTP/1.1 103 Early Hints
Link: </styles.css>; rel=preload; as=style
Link: <https://cdn.example.com>; rel=preconnect

HTTP/1.1 200 OK
Content-Type: text/html
```

While the server is still generating the HTML, Chrome can already download CSS or connect to other origins. Chrome supports it for navigations over HTTP/2 and HTTP/3.

## 190: What is HTTP cache partitioning?

Since Chrome 86, the HTTP cache is partitioned (keyed) by the top-level site, and also the frame's site, as well as the resource URL. So if `site-a.com` and `site-b.com` both load `https://cdn.com/lib.js`, each site gets its own cached copy.

This stops one site from finding out what you visited on another site by timing cache hits. The downside is fewer cache hits for shared CDN files, which is why "use a public CDN so it's already cached" no longer works.

## 191: What is storage partitioning?

Storage partitioning (shipped around Chrome 115) means that storage used by third-party iframes is keyed by the top-level site too. An iframe from `widget.com` inside `a.com` gets different localStorage, IndexedDB, Cache Storage and Service Workers than the same iframe inside `b.com`.

This prevents cross-site tracking through storage. Cookies are handled separately; partitioned cookies need the `Partitioned` attribute (CHIPS).

## 192: What is CHIPS?

CHIPS (Cookies Having Independent Partitioned State) lets a third-party service set a cookie that is stored per top-level site.

```http
Set-Cookie: __Host-widget=abc; Secure; Path=/; SameSite=None; Partitioned
```

The cookie works inside `a.com` and inside `b.com`, but those are two different cookies, so they can't be used to track users across sites. It's useful for embedded chat widgets, maps or payment frames that need state.

## 193: What is the current status of third-party cookies in Chrome?

Chrome planned for years to remove third-party cookies, but in 2025 Google dropped that plan. Third-party cookies stay enabled by default in normal browsing, and users can block them in settings. They are blocked by default in Incognito.

Most of the Privacy Sandbox APIs built as replacements (Topics, Protected Audience, Attribution Reporting and others) were retired because few sites used them. CHIPS, FedCM and Private State Tokens are still supported.

## 194: How does the SameSite cookie attribute work?

- **Strict**: the cookie is sent only for same-site requests, not even when you click a link from another site.
- **Lax**: sent for same-site requests and for top-level navigations with safe methods (like clicking a link), but not for cross-site subresource requests or POSTs.
- **None**: sent on all requests, but must also be `Secure`.

Chrome treats cookies without a `SameSite` attribute as `Lax` by default. This protects against many CSRF attacks.

## 195: What is the difference between same-site and cross-site requests for cookies?

A request is same-site if the site (scheme + eTLD+1) of the page that made it matches the site of the URL. `https://app.example.com` requesting `https://api.example.com` is same-site; `https://example.com` requesting `https://other.com` is cross-site.

Since Chrome considers the scheme part of the site (schemeful same-site), `http://example.com` and `https://example.com` are cross-site.

## 196: What is a CORS preflight request?

For "non-simple" requests, the browser first sends an `OPTIONS` request to ask the server if the real request is allowed. Requests are non-simple when they use methods other than `GET`, `HEAD` or `POST`, custom headers like `Authorization`, or a `Content-Type` such as `application/json`.

```http
OPTIONS /api/items HTTP/1.1
Origin: https://app.example.com
Access-Control-Request-Method: PUT
Access-Control-Request-Headers: content-type
```

The server answers with `Access-Control-Allow-Methods` and `Access-Control-Allow-Headers`. `Access-Control-Max-Age` lets Chrome cache the answer (Chrome caps it at 2 hours).

## 197: What is Opaque Response Blocking (ORB)?

ORB (formerly CORB, Cross-Origin Read Blocking) stops cross-origin responses that look like data, such as HTML, JSON or XML, from reaching a renderer process when they are loaded with tags like `<img>` or `<script>`.

For example, `<img src="https://bank.com/account.json">` would bring JSON into the attacker's process, where a Spectre attack might read it. ORB lets Chrome's network service block such responses before they arrive, so they never enter the attacker's memory.

## 198: What are COOP and COEP?

- **COOP** (`Cross-Origin-Opener-Policy: same-origin`) puts your page in its own browsing context group, so cross-origin popups or openers can't keep a reference to your window.
- **COEP** (`Cross-Origin-Embedder-Policy: require-corp` or `credentialless`) makes the page load only cross-origin resources that agree to it (with CORS or `Cross-Origin-Resource-Policy`), or loads them without credentials.

Together they make a page "cross-origin isolated." That guarantees no other site's data is in your process.

## 199: What does cross-origin isolation unlock?

When `self.crossOriginIsolated` is `true`, the page can use features that are dangerous because they allow very precise timing:

- `SharedArrayBuffer` and `Atomics.wait` on the main thread.
- More precise `performance.now()` timers.
- `performance.measureUserAgentSpecificMemory()`.

```http
Cross-Origin-Opener-Policy: same-origin
Cross-Origin-Embedder-Policy: require-corp
```

These were restricted after Spectre, because high-resolution timers make it easier to read memory through side channels.

## 200: Why was document.domain deprecated?

`document.domain` let two pages on different subdomains, like `a.example.com` and `b.example.com`, set themselves to `example.com` and then script each other as if they were the same origin. That forced Chrome to keep them in the same process and weakened the same-origin policy.

Chrome now makes setting `document.domain` do nothing by default (origin-keyed agent clusters). Pages should use `postMessage` instead.

## 201: What makes a page ineligible for the bfcache?

Common reasons in Chrome:

- An `unload` event handler (on desktop it blocks bfcache).
- Open connections that can't be paused, like an active WebSocket or WebRTC connection, or an IndexedDB transaction in progress.
- The page was opened with `window.open()` and the opener still has a reference.
- `Cache-Control: no-store` on the main document (Chrome has been relaxing this rule in some cases).
- Using some APIs like WebUSB or holding certain locks.

DevTools > Application > Back/forward cache tests a page and lists the reasons. From JavaScript, `notRestoredReasons` on the navigation timing entry gives the reasons for real users.

## 202: How do you detect that a page was restored from the bfcache?

Use the `pageshow` event and check `event.persisted`:

```js
window.addEventListener("pageshow", (event) => {
  if (event.persisted) {
    // Restored from bfcache: refresh stale data, restart timers
    refreshCart();
  }
});

window.addEventListener("pagehide", (event) => {
  if (event.persisted) {
    // Going into bfcache: close connections
  }
});
```

Analytics tools need this too, because a bfcache restore is a page view that doesn't fire `load` again.

## 203: Why is the unload event being deprecated in Chrome?

`unload` is unreliable: on mobile it often doesn't fire at all, because the OS kills background pages. It also blocks the bfcache on desktop, which makes back and forward navigations slower.

Chrome is gradually turning off `unload` handlers by default. Use `pagehide` or `visibilitychange` instead. Sites can opt out temporarily, or opt in to the deprecation early, with the `Permissions-Policy: unload=()` header.

## 204: What happens to a page when Chrome freezes it?

When a page is frozen, Chrome stops running its tasks: timers, `fetch` callbacks and other task queues are paused. The page keeps its memory, and it fires a `freeze` event before and `resume` event after.

```js
document.addEventListener("freeze", () => saveState());
document.addEventListener("resume", () => reconnect());
```

Pages in the bfcache are frozen. Background tabs may also be frozen when Chrome needs to save resources, especially on mobile and with Energy Saver.

## 205: How does Chrome clamp timers?

- Nested `setTimeout` or `setInterval` calls (nested 5 or more levels deep) have a minimum delay of 4 ms, as the HTML spec says.
- In hidden tabs, timers run at most once per second.
- After 5 minutes hidden, with long chains of timers and no audio playing, timers are aligned to run at most once per minute.
- Frozen pages don't run timers at all.

So `setTimeout(fn, 0)` is never really zero, and you can't rely on exact timing in background tabs.

## 206: How can you yield to the browser in the middle of a long task?

Split the work into chunks and give control back between them so the browser can handle input and render. The modern way is `scheduler.yield()`, available in Chrome since version 129:

```js
async function processAll(items) {
  let deadline = performance.now() + 50;
  for (const item of items) {
    process(item);
    if (performance.now() > deadline) {
      await scheduler.yield();
      deadline = performance.now() + 50;
    }
  }
}
```

This gives the browser a chance to handle input and paint about every 50 ms. Unlike `setTimeout(0)`, `scheduler.yield()` puts the rest of your work near the front of the queue, so other scripts can't jump ahead of you.

## 207: What is scheduler.postTask()?

`scheduler.postTask()` lets you schedule a task with a priority: `user-blocking`, `user-visible` (default) or `background`.

```js
scheduler.postTask(() => renderSearchResults(), { priority: "user-blocking" });
scheduler.postTask(() => sendAnalytics(), { priority: "background" });

const controller = new TaskController({ priority: "background" });
scheduler.postTask(prefetchImages, { signal: controller.signal });
controller.abort(); // cancel it
```

Chrome runs higher-priority tasks first. It helps keep less important work out of the way of user interactions.

## 208: What is the Long Animation Frames API?

The Long Animation Frames API (LoAF), shipped in Chrome 123, reports frames that took more than 50 ms from start to finish. Unlike the Long Tasks API, it includes the rendering work and gives details about which scripts ran, where they came from and how long each took.

```js
new PerformanceObserver((list) => {
  for (const frame of list.getEntries()) {
    console.log(frame.duration, frame.blockingDuration);
    for (const script of frame.scripts) {
      console.log(script.sourceURL, script.invoker, script.duration);
    }
  }
}).observe({ type: "long-animation-frame", buffered: true });
```

It is the best tool for finding the cause of a bad INP in real users.

## 209: How is INP broken down and what causes each part to be slow?

INP has three parts:

1. **Input delay**: time from the interaction until your handler starts. Slow when the main thread is busy with other tasks.
2. **Processing time**: time your event handlers take. Slow when handlers do too much work.
3. **Presentation delay**: time from the end of handlers until the next frame is painted. Slow with heavy style, layout and paint, or a huge DOM.

Fixes: break up long tasks, do only the visual update in the handler and defer the rest, and keep the DOM small and rendering cheap.

## 210: How do you measure Web Vitals in real users?

Use the `web-vitals` library, which wraps the right performance APIs and handles edge cases like bfcache restores and background tabs:

```js
import { onLCP, onINP, onCLS } from "web-vitals";

function send(metric) {
  navigator.sendBeacon("/vitals", JSON.stringify(metric));
}
onLCP(send);
onINP(send);
onCLS(send);
```

The "attribution" build also tells you which element was the LCP, which interaction was slow and which element shifted.

## 211: What can be an LCP element?

LCP considers `<img>` elements, `<image>` inside SVG, the poster image of a `<video>` (and the first frame of a video), elements with a CSS `background-image` loaded with `url()`, and block-level elements containing text.

It ignores elements with zero opacity, elements that cover the whole viewport and are likely backgrounds, and low-entropy placeholder images. The LCP candidate can change while the page loads, and reporting stops at the first user input.

## 212: How does CLS group layout shifts?

CLS groups shifts into "session windows." A window ends when there is a 1 second gap with no shifts, or after 5 seconds total. The CLS value is the largest window's sum, not the sum of all shifts during the page life.

Each shift's score is the impact fraction (how much of the viewport moved content covers) times the distance fraction (how far it moved). Shifts within 500 ms of a user input are excluded because the user expected them.

## 213: What are hidden classes (shapes or maps) in V8?

V8 gives every object a hidden class, called a "Map" internally, that describes its layout: which properties it has and at which offset. Objects created the same way share the same hidden class.

```js
function Point(x, y) {
  this.x = x;
  this.y = y;
}
const a = new Point(1, 2);
const b = new Point(3, 4); // same hidden class as a
b.z = 5; // b now gets a new hidden class
```

Knowing the hidden class lets V8 read properties by a fixed offset instead of a dictionary lookup. Adding properties in different orders or deleting them creates different classes and slows things down.

## 214: What are inline caches in V8?

An inline cache (IC) remembers, at a specific place in the code, which hidden class it saw last time and where the property was. Next time, if the object has the same hidden class, V8 can go straight to the right offset.

The optimizing compilers use this IC feedback to generate fast machine code specialized for the shapes that were seen.

## 215: What do monomorphic, polymorphic and megamorphic mean?

They describe how many different hidden classes an operation sees:

- **Monomorphic**: always one shape. Fastest.
- **Polymorphic**: a few shapes (up to 4 in V8). Still fairly fast, V8 checks each.
- **Megamorphic**: many shapes. V8 gives up on specializing and uses a slower general lookup.

```js
function getX(p) {
  return p.x;
}
getX({ x: 1 }); // shape A
getX({ x: 1, y: 2 }); // shape B, now polymorphic
```

Hot code that always works with objects of the same shape runs faster.

## 216: What is Sparkplug?

Sparkplug is V8's baseline compiler, added in 2021. It turns bytecode into machine code very quickly, without any optimization: it basically writes out the machine code for each bytecode instruction.

It sits between Ignition and the optimizing compilers. It removes the overhead of the interpreter loop and speeds up code that runs a fair amount but isn't hot enough for full optimization.

## 217: What is Maglev?

Maglev is V8's mid-tier optimizing compiler, shipped in Chrome 117 (2023). It uses type feedback to generate optimized code, but compiles much faster than TurboFan, so code reaches good speed sooner.

The tiers are now: Ignition (interpreter), Sparkplug (baseline), Maglev (mid-tier) and TurboFan (top tier). Functions move up the tiers as they get hotter.

## 218: What is TurboFan?

TurboFan is V8's top-tier optimizing compiler. It uses the type feedback collected by lower tiers to make guesses (like "this is always a small integer"), and generates highly optimized machine code with inlining, escape analysis and other optimizations.

It's the slowest to compile, so V8 only uses it for the hottest functions. Its backend was rebuilt on a newer design called Turboshaft, which compiles faster.

## 219: What is deoptimization?

Optimized code is built on assumptions from past runs, like "`x` is always an integer" or "this object always has hidden class A." If an assumption breaks, V8 throws away the optimized code and goes back to running bytecode in the interpreter. This is called deoptimization (deopt).

```js
function add(a, b) {
  return a + b;
}
for (let i = 0; i < 1e6; i++) add(i, 1); // optimized for numbers
add("a", "b"); // deopt
```

An occasional deopt is fine, but code that deopts again and again is slow. Keeping types stable avoids it.

## 220: What is on-stack replacement (OSR)?

OSR lets V8 switch to optimized code in the middle of a running function, usually inside a long loop. Without it, a function that runs once but loops a million times would stay in the interpreter until it returns.

V8 compiles an optimized version and jumps into it at the current loop iteration. It can also do the reverse during a deopt.

## 221: How does V8's code cache work in Chrome?

When a script is run, V8 can save the compiled bytecode for it in Chrome's cache, next to the script in the HTTP cache. On later visits, Chrome loads the bytecode instead of parsing and compiling the script again.

Chrome caches scripts that are run a couple of times within a short period, and caches Service Worker scripts more eagerly when they are installed. Changing the script content (like a new build hash) means a new cache entry.

## 222: What is lazy parsing in V8?

Parsing all code fully at startup is slow, and much of it might never run. So V8 pre-parses most functions: it checks syntax and finds variables but doesn't build a full AST. A function is fully parsed only when it's first called.

If a function is called right away, it gets parsed twice. V8 uses hints like wrapping a function in parentheses (`(function () { ... })()`) to parse it eagerly. Chrome also supports compile hints magic comments for files whose functions are all needed at startup.

## 223: How does V8's garbage collector work at a high level?

V8 uses a generational GC because most objects die young:

- **Young generation**: new objects go here. It's small and collected often with a fast "scavenger" that copies live objects to another space.
- **Old generation**: objects that survive a couple of scavenges are moved here. It's collected less often with mark-sweep-compact.

The GC project is called Orinoco. It does much of its work in parallel on helper threads, concurrently while JavaScript runs, and in idle time between frames, so pauses stay short.

## 224: What is Oilpan?

Oilpan is the garbage collector for Blink's C++ objects, like DOM nodes and other Web API objects. Instead of manual `new` and `delete` or reference counting, these objects are traced and collected like JavaScript objects.

V8 and Oilpan work together as a unified heap: during a GC they trace references across both, from JavaScript wrappers to DOM nodes and back. This lets the browser find cycles between JavaScript and the DOM that reference counting would leak. Oilpan is now also available as `cppgc` inside V8.

## 225: How do you find a memory leak with DevTools?

1. Open the Memory panel and take a heap snapshot.
2. Do the action that you think leaks (open and close a modal, navigate in your SPA) several times.
3. Take another snapshot and use the "Comparison" view to see which objects grew.
4. Filter for "Detached" to find DOM nodes no longer in the page but still in memory.
5. Look at the Retainers section to see what keeps them alive.

The "Allocation instrumentation on timeline" option shows which allocations stay alive over time. The Performance panel with "Memory" checked shows if JS heap and DOM node count keep growing.

## 226: What is the difference between shallow size and retained size in a heap snapshot?

- **Shallow size**: memory used by the object itself.
- **Retained size**: memory that would be freed if this object were deleted, meaning the object plus everything only it keeps alive.

A small object, like a closure or a Map, can have a huge retained size if it holds the only reference to big data. When hunting leaks, sort by retained size.

## 227: What is a detached DOM node?

A detached DOM node is an element removed from the document but still referenced from JavaScript, so it can't be garbage collected. If it's the root of a big subtree, the whole subtree stays in memory.

```js
let cache = [];
function removeRow(row) {
  row.remove();
  cache.push(row); // leak: row is detached but still reachable
}
```

Common sources are arrays or Maps of elements, event listeners on removed elements that are referenced elsewhere, and framework components that don't clean up.

## 228: What are WeakRef and FinalizationRegistry, and should you use them?

`WeakRef` holds a reference to an object without stopping it from being collected. `FinalizationRegistry` lets you register a callback that may run after an object is collected.

```js
const ref = new WeakRef(bigObject);
const obj = ref.deref(); // the object, or undefined if collected
```

They are for special cases like caches. GC timing isn't predictable, finalizers may never run, and behavior differs between engines, so don't use them for important logic. `WeakMap` and `WeakSet` are better for most needs.

## 229: What is a V8 isolate and a context?

An **isolate** is a full, independent instance of the V8 engine with its own heap. Objects can't be shared between isolates. Each renderer main thread has one isolate, and each worker has its own.

A **context** is a global environment inside an isolate: its own global object and built-ins. Each frame has its own context, so `window` and `Array` in an iframe are different from those in the parent, even in the same process.

## 230: What is an isolated world?

An isolated world is a separate JavaScript context that shares the same DOM as the page but has its own global variables and JavaScript objects. Chrome extension content scripts run in isolated worlds.

So a content script and the page see the same `document.body`, but if the page changes `Array.prototype` or defines a global `foo`, the content script doesn't see it, and the other way around. DevTools also uses isolated worlds for some features.

## 231: What is the Service Worker lifecycle?

1. **Register**: `navigator.serviceWorker.register('/sw.js')`.
2. **Install**: the `install` event fires. You usually pre-cache files here.
3. **Waiting**: if an older worker controls open pages, the new one waits.
4. **Activate**: the `activate` event fires. You clean up old caches here.
5. **Controlling**: the worker handles `fetch` events for pages in its scope.

```js
self.addEventListener("install", (e) => {
  e.waitUntil(caches.open("v2").then((c) => c.addAll(["/", "/app.js"])));
  self.skipWaiting();
});
self.addEventListener("activate", (e) => e.waitUntil(clients.claim()));
```

`skipWaiting()` and `clients.claim()` let a new worker take over right away.

## 232: How does Chrome check for Service Worker updates?

Chrome checks for an updated `sw.js` on navigations to pages in scope, on some events, or when you call `registration.update()`, but at most once every 24 hours unless forced. By default it bypasses the HTTP cache for the worker script itself (`updateViaCache: 'imports'` is the default).

If the bytes differ, the new worker installs and waits. Imported scripts can also be checked depending on `updateViaCache`.

## 233: What is navigation preload?

When a Service Worker controls a page, it has to start up before it can handle a navigation request, which can take tens of milliseconds or more. Navigation preload lets the browser start the network request for the page in parallel with starting the worker.

```js
self.addEventListener("activate", (e) => {
  e.waitUntil(self.registration.navigationPreload.enable());
});

self.addEventListener("fetch", (e) => {
  if (e.request.mode === "navigate") {
    e.respondWith(
      (async () => (await e.preloadResponse) || fetch(e.request))(),
    );
  }
});
```

## 234: What are Speculation Rules?

Speculation Rules is a Chrome API that tells the browser which pages to prefetch or prerender for future navigations, using JSON in a script tag or an HTTP header.

```html
<script type="speculationrules">
  {
    "prerender": [
      {
        "where": { "href_matches": "/products/*" },
        "eagerness": "moderate"
      }
    ]
  }
</script>
```

`prefetch` downloads only the HTML of the next page. `prerender` loads and renders the whole page in a hidden tab, so the navigation can feel instant. `eagerness` controls when to start: `immediate`, `eager`, `moderate` (on hover) or `conservative` (on pointer down).

## 235: How do you write code that behaves correctly when a page is prerendered?

A prerendered page runs JavaScript before the user sees it. Check `document.prerendering` and wait for `prerenderingchange` before doing things that should only happen when the page is really viewed, like counting analytics.

```js
if (document.prerendering) {
  document.addEventListener("prerenderingchange", sendPageView, { once: true });
} else {
  sendPageView();
}
```

Chrome also delays some APIs, like permission prompts, until activation. Analytics vendors like Google Analytics already handle this.

## 236: What is the Navigation API?

The Navigation API (`window.navigation`) is a modern replacement for the History API in single-page apps. It gives one `navigate` event for all navigations, including link clicks, form submits and back/forward, which you can intercept.

```js
navigation.addEventListener("navigate", (event) => {
  if (!event.canIntercept || event.hashChange) return;
  const url = new URL(event.destination.url);
  event.intercept({
    async handler() {
      const html = await loadRoute(url.pathname);
      main.innerHTML = html;
    },
  });
});
```

It also gives a list of history entries and a promise when a navigation finishes. Chrome has supported it since version 102, and Safari and Firefox have added it more recently.

## 237: What are View Transitions?

View Transitions animate between two states of a page. The browser takes a snapshot of the old state, you update the DOM, and it animates from the old snapshot to the new one with CSS.

```js
document.startViewTransition(() => {
  updateTheDOM();
});
```

```css
@view-transition {
  navigation: auto;
} /* for multi-page sites */
.card {
  view-transition-name: card;
}
```

Same-document transitions work in single-page apps; cross-document transitions (Chrome 126+) work between pages of the same origin.

## 238: How do you record a trace with chrome://tracing or Perfetto?

For problems the DevTools Performance panel doesn't show (like GPU process work or browser process issues), record a full browser trace:

1. Open `https://ui.perfetto.dev` and record from Chrome, or use `chrome://tracing` (older UI).
2. Choose categories like `rendering`, `gpu`, `blink`, `v8`, `toplevel`.
3. Reproduce the problem and stop the recording.

You get every thread in every process on one timeline. It's how you see, for example, that a frame was late because the GPU process was busy.

## 239: How do you debug network problems with chrome://net-export?

1. Open `chrome://net-export`, choose what to include and start logging.
2. Reproduce the problem.
3. Stop and save the JSON file.
4. Open it in the NetLog viewer (`https://netlog-viewer.appspot.com`).

It shows DNS lookups, socket connections, proxy decisions, TLS handshakes, QUIC sessions and every URL request, with errors and timing. It's useful when the Network panel shows only a failed request without a clear reason.

## 240: How do you debug Chrome on Android from a desktop?

Enable USB debugging on the phone, connect it with a cable, and open `chrome://inspect#devices` on desktop Chrome. You'll see the open tabs on the phone and can click "inspect" to use the full DevTools on them.

You can also forward ports so the phone can reach a dev server on your computer at `localhost`.

## 241: How do you automate Chrome with Puppeteer?

```js
import puppeteer from "puppeteer";

const browser = await puppeteer.launch();
const page = await browser.newPage();
await page.goto("https://example.com", { waitUntil: "networkidle0" });
await page.screenshot({ path: "example.png" });
const title = await page.title();
console.log(title);
await browser.close();
```

Puppeteer starts Chrome (headless by default) and controls it over the Chrome DevTools Protocol. You can also call CDP directly with `page.createCDPSession()` for lower-level features like throttling or code coverage. Puppeteer also supports Firefox through WebDriver BiDi.

## 242: What are worklets?

Worklets are small, lightweight scripts that run in parts of the rendering pipeline, separate from the main JavaScript context. Examples:

- **AudioWorklet**: process audio on the audio rendering thread.
- **PaintWorklet** (CSS Paint API): draw a custom background with a canvas-like API.
- **Shared Storage worklets** and others for special APIs.

```js
CSS.paintWorklet.addModule("checkerboard.js");
```

```css
.box {
  background-image: paint(checkerboard);
}
```

They have limited APIs and the browser can run them on other threads.

## 243: What is OffscreenCanvas?

`OffscreenCanvas` is a canvas that isn't tied to the DOM, so you can draw to it in a Web Worker. This moves heavy drawing (charts, games, image processing) off the main thread.

```js
// main.js
const offscreen = canvas.transferControlToOffscreen();
worker.postMessage({ canvas: offscreen }, [offscreen]);

// worker.js
onmessage = ({ data }) => {
  const ctx = data.canvas.getContext("2d");
  ctx.fillRect(0, 0, 100, 100);
};
```

The frames drawn in the worker go straight to the compositor.

## 244: What is Chrome's autoplay policy?

Chrome allows video autoplay without sound (`muted`). Autoplay with sound is allowed only if the user has interacted with the site (click, tap), or the site has a high Media Engagement Index (the user often plays media there), or the site is installed as a PWA on mobile.

```html
<video src="intro.mp4" autoplay muted playsinline></video>
```

`video.play()` returns a promise that rejects if autoplay is blocked, so always handle it.

## 245: How does Chrome render text?

Text goes through several steps: Blink splits it into runs by font and script, HarfBuzz shapes each run (turns characters into positioned glyphs, handling ligatures, kerning and complex scripts like Arabic), LayoutNG breaks lines, and Skia draws the glyphs using the font data.

Font fallback chooses another font when the first one doesn't have a character, for example an emoji. Shaping results are cached because shaping is costly.

## 246: What are Trusted Types?

Trusted Types is a Chrome feature that blocks passing plain strings to dangerous DOM sinks like `innerHTML`, `eval` or `script.src`. With the policy on, only special typed objects created by your own policies are accepted.

```http
Content-Security-Policy: require-trusted-types-for 'script'; trusted-types app-policy
```

```js
const policy = trustedTypes.createPolicy("app-policy", {
  createHTML: (s) => DOMPurify.sanitize(s),
});
el.innerHTML = policy.createHTML(userInput);
```

This makes DOM XSS bugs much harder because all risky code goes through a few reviewed policies.

## 247: What is Permissions Policy?

Permissions Policy (formerly Feature Policy) lets a page control which browser features it and its iframes can use, like camera, geolocation, fullscreen or payment.

```http
Permissions-Policy: geolocation=(self), camera=(), fullscreen=(self "https://video.example.com")
```

```html
<iframe src="https://video.example.com" allow="fullscreen"></iframe>
```

It reduces what embedded third-party content can do and is also used to opt out of features like `unload`.

## 248: What is HTTPS-First mode?

HTTPS-First mode makes Chrome try HTTPS first for every navigation, even when you type or click an `http://` link. If the HTTPS version doesn't work, Chrome shows a warning before loading the HTTP page.

Chrome has been turning it on more widely, for example in Incognito and for users with Enhanced Safe Browsing, and has been moving toward using it by default for everyone.

## 249: What is DNS over HTTPS in Chrome?

DNS over HTTPS (DoH) sends DNS queries inside encrypted HTTPS connections, so people on the network can't see or change which domains you look up.

Chrome's default "secure DNS" mode upgrades to DoH automatically if your current DNS provider supports it, and falls back to normal DNS if not. Users can also pick a specific DoH provider in settings. Some enterprise and parental control setups turn it off.

## 250: What are Fetch Metadata headers?

Chrome adds `Sec-Fetch-*` headers to requests so the server knows the context:

```http
Sec-Fetch-Site: cross-site      # same-origin, same-site, cross-site, none
Sec-Fetch-Mode: no-cors         # navigate, cors, no-cors, same-origin, websocket
Sec-Fetch-Dest: image           # document, script, image, iframe, empty...
Sec-Fetch-User: ?1              # navigation triggered by the user
```

Pages can't change these headers. Servers use them to reject unexpected cross-site requests, for example blocking cross-site requests to an API endpoint, which helps against CSRF and cross-site leaks.

## 251: What does chrome://gpu tell you?

It shows the "Graphics Feature Status" for each feature (canvas, compositing, rasterization, video decode, WebGL, WebGPU and so on) and whether it is hardware accelerated, software only or disabled. It also lists the GPU, driver version, which driver bug workarounds are on and any problems Chrome detected.

When a user says "animations are slow only on my computer," this page often shows that hardware acceleration is off because of a blocklisted driver.

## 252: What happens when the GPU is not available or blocklisted?

Chrome falls back to software. Compositing can still happen through the GPU process using a software path, and raster happens on the CPU. For WebGL, Chrome used SwiftShader, a CPU implementation of the graphics API, but this fallback is being removed for WebGL because it was a security risk, so WebGL may just not be available.

Pages still work, but heavy animations, large canvases and video are slower and use more CPU.

## 253: What is ANGLE?

ANGLE (Almost Native Graphics Layer Engine) is a library that implements OpenGL ES on top of the native graphics API of each platform: Direct3D on Windows, Metal on macOS, Vulkan on Linux and Android, or desktop OpenGL.

Chrome uses it for WebGL and for parts of its own GPU work. It gives the same behavior on every platform and avoids many driver bugs, because Direct3D and Metal drivers are usually more stable than OpenGL ones.

## 254: What is Dawn?

Dawn is Chrome's open source implementation of WebGPU. It translates WebGPU calls into Vulkan, Metal or Direct3D 12, and checks every call for safety, because a web page must never be able to crash the GPU or read memory it shouldn't.

The renderer sends WebGPU commands through a "wire" to the GPU process, where Dawn runs them. Skia's Graphite backend also uses Dawn on some platforms.

## 255: How does Chrome connect when a host has both IPv4 and IPv6 addresses?

Chrome uses a Happy Eyeballs style approach. It usually tries the first address the resolver returns (often IPv6), and if that connection doesn't succeed within a short time (around 300 ms), it starts a connection to an IPv4 address in parallel. Whichever connects first wins.

This avoids long hangs on networks where IPv6 is broken.

## 256: How does TLS session resumption help performance?

After a full TLS handshake, the server can give the browser a session ticket (or pre-shared key in TLS 1.3). On the next connection, the browser presents it and both sides skip the certificate exchange and part of the key setup.

With TLS 1.3 resumption, the handshake still takes one round trip but uses less CPU. With 0-RTT, the browser can send the first request along with the handshake, but only for safe, repeatable requests because 0-RTT data can be replayed.

## 257: What is the Chrome Root Store?

Since Chrome 105, Chrome uses its own list of trusted root certificate authorities (the Chrome Root Store) and its own certificate verifier on most platforms, instead of relying on the operating system's list. This gives the same trust decisions on every OS.

Chrome can also remove trust from a CA that breaks the rules, which it has done for several CAs. Enterprise admins can still add their own roots.

## 258: How long does a Manifest V3 extension service worker stay alive?

Chrome stops an extension service worker after about 30 seconds without any events or extension API calls. A single request can't take more than 5 minutes. Each new event or API call resets the idle timer.

So you shouldn't keep state in global variables. Store it in `chrome.storage` and use `chrome.alarms` instead of `setInterval` for periodic work.

```js
chrome.alarms.create("sync", { periodInMinutes: 15 });
chrome.alarms.onAlarm.addListener((alarm) => {
  if (alarm.name === "sync") syncData();
});
```

## 259: What is declarativeNetRequest?

`declarativeNetRequest` lets an extension block, redirect or modify requests by giving Chrome a list of rules, instead of running code for every request. Chrome checks the rules itself in the network path.

```json
[
  {
    "id": 1,
    "priority": 1,
    "action": { "type": "block" },
    "condition": {
      "urlFilter": "||ads.example.com",
      "resourceTypes": ["script", "image"]
    }
  }
]
```

This is faster and more private, because the extension never sees your requests. It replaced blocking `webRequest` in Manifest V3, which is why ad blockers had to be rewritten.

## 260: When do content scripts run?

The `run_at` option controls it:

- `document_start`: after CSS files are injected, before any DOM is built or other scripts run.
- `document_end`: right after the DOM is complete, before images and frames finish loading.
- `document_idle` (default): sometime between `document_end` and right after `load`, when the browser is less busy.

```json
"content_scripts": [{
  "matches": ["https://*.example.com/*"],
  "js": ["content.js"],
  "run_at": "document_idle"
}]
```

By default content scripts run in an isolated world. With `"world": "MAIN"` they run in the page's own JavaScript context.

## 261: How do the parts of an extension talk to each other?

They use message passing:

```js
// content script
const reply = await chrome.runtime.sendMessage({ type: "getUser" });

// service worker
chrome.runtime.onMessage.addListener((msg, sender, sendResponse) => {
  if (msg.type === "getUser") {
    getUser().then(sendResponse);
    return true; // keep the channel open for the async reply
  }
});
```

For longer conversations, `chrome.runtime.connect()` opens a port. The messages go through the browser process, which checks the sender.

## 262: How does Chrome choose which tab to discard?

When memory is low, Chrome ranks background tabs and discards the least important first. It avoids tabs that are playing audio, using the camera or mic, doing screen sharing, have unsaved form input, are pinned in some cases, or are on the user's "always keep active" list. Recently used tabs are kept longer.

You can see the state and score of every tab at `chrome://discards`, and discard a tab manually there to test how your page behaves.

## 263: What is Media Source Extensions?

MSE lets JavaScript feed media data into a `<video>` element piece by piece, instead of giving it a single file URL. Players like YouTube, Netflix, hls.js and Shaka use it to do adaptive streaming: they fetch segments of video at different quality levels depending on the network.

```js
const ms = new MediaSource();
video.src = URL.createObjectURL(ms);
ms.addEventListener("sourceopen", async () => {
  const sb = ms.addSourceBuffer('video/mp4; codecs="avc1.42E01E"');
  sb.appendBuffer(await (await fetch("/seg1.mp4")).arrayBuffer());
});
```

## 264: What is EME and Widevine?

EME (Encrypted Media Extensions) is the standard API for playing DRM-protected video. The page uses EME to talk to a Content Decryption Module (CDM) that decrypts the media.

In Chrome the CDM is Widevine, made by Google. It runs in its own sandboxed process and, on some devices, uses hardware-protected paths so decrypted frames can't be copied. Widevine is one of the parts that is in Chrome but not in plain Chromium builds.

## 265: What is WebCodecs?

WebCodecs gives JavaScript low-level access to the browser's audio and video encoders and decoders, including hardware ones. You work with raw frames (`VideoFrame`) and encoded chunks.

It's used for video editors, game streaming and video conferencing, where `<video>` or MediaRecorder don't give enough control. It's more efficient than decoding with WebAssembly because it uses the same codecs (and hardware) that Chrome uses for `<video>`.

## 266: What is requestIdleCallback and when should you use it?

`requestIdleCallback` runs a callback when the main thread is idle, for example at the end of a frame with time left, or when nothing is happening.

```js
requestIdleCallback(
  (deadline) => {
    while (deadline.timeRemaining() > 0 && queue.length) {
      doWork(queue.shift());
    }
  },
  { timeout: 2000 },
);
```

It's good for low-priority work like sending analytics or warming caches. Don't change the DOM inside it, because that work happens after layout and would force another frame. In busy pages the callback can wait a long time, which is what `timeout` is for.

## 267: Why use IntersectionObserver instead of scroll events?

Scroll listeners run on the main thread for every scroll event, and checking element positions with `getBoundingClientRect()` forces layout. IntersectionObserver lets the browser compute visibility itself as part of the rendering update and call you only when something changes.

```js
const io = new IntersectionObserver(
  (entries) => {
    for (const e of entries) {
      if (e.isIntersecting) {
        loadImage(e.target);
        io.unobserve(e.target);
      }
    }
  },
  { rootMargin: "200px" },
);
document.querySelectorAll("img[data-src]").forEach((img) => io.observe(img));
```

## 268: When do ResizeObserver callbacks run?

ResizeObserver callbacks run during the rendering update, after layout and before paint. So you get the new sizes in the same frame and can react before anything is drawn.

If your callback changes sizes again, Chrome runs layout and calls observers again for deeper elements. If it loops too many times, Chrome stops and reports the error "ResizeObserver loop completed with undelivered notifications."

## 269: When do MutationObserver callbacks run?

MutationObserver callbacks run as microtasks, after the current script finishes and before the browser renders. Mutations are batched, so if you change the DOM 100 times in a loop you get one callback with 100 records.

```js
const mo = new MutationObserver((records) => {
  console.log(records.length, "changes");
});
mo.observe(list, { childList: true, subtree: true });
```

It replaced the old Mutation Events, which fired synchronously on every change and were very slow. Chrome removed Mutation Events in Chrome 127.

## 270: What are scroll-driven animations and why are they efficient?

Scroll-driven animations link a CSS animation's progress to scroll position instead of time.

```css
.progress {
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

When the animated properties are compositor-friendly (`transform`, `opacity`), Chrome runs them on the compositor thread together with scrolling. That's much smoother than updating styles from a JavaScript `scroll` listener.

## 271: What is the difference between CSS animations, the Web Animations API and JavaScript rAF animations?

- **CSS animations/transitions**: declared in CSS. Chrome can run `transform`/`opacity` ones on the compositor.
- **Web Animations API** (`el.animate()`): the same engine as CSS animations, controlled from JavaScript (pause, reverse, seek, promises). Can also run on the compositor.
- **rAF animations**: you update styles in each `requestAnimationFrame` callback. Full control, but always on the main thread, so a busy main thread makes them stutter.

```js
el.animate(
  [{ transform: "translateY(0)" }, { transform: "translateY(100px)" }],
  { duration: 300, easing: "ease-out", fill: "forwards" },
);
```

## 272: How does position: sticky work in the rendering pipeline?

Sticky elements are laid out in their normal place, and the compositor adjusts their offset while you scroll, based on the scroll position and the limits of their containing block. In Chrome this is often handled on the compositor thread, so sticky headers stay smooth during scrolling.

A sticky element sticks within its nearest scrolling ancestor. If a parent has `overflow: hidden` or `auto`, that parent becomes the scroll container, which is the usual reason sticky "doesn't work."

## 273: Why does a large DOM slow down rendering?

More nodes means more memory, slower style calculation (more elements to match), slower layout, bigger paint lists and slower hit testing. Changes that invalidate many nodes, like changing a class on `body`, get more expensive.

Lighthouse warns when a page has more than about 1,400 DOM nodes. Fixes include virtual lists for long lists, `content-visibility: auto` for off-screen sections and not rendering hidden UI until it's needed.

## 274: What does the DevTools Rendering tab offer?

Open it from the Command Menu (`Ctrl/Cmd+Shift+P`, "Show Rendering"). Useful options:

- **Paint flashing**: highlights areas that are repainted.
- **Layout shift regions**: highlights elements that shifted.
- **Layer borders**: shows compositor layers and tiles.
- **Frame rendering stats**: FPS and GPU memory.
- **Scrolling performance issues**: shows elements that slow down scrolling.
- Emulation of `prefers-color-scheme`, `prefers-reduced-motion`, vision problems and print media.

## 275: What is the Coverage tab in DevTools?

The Coverage tab records which bytes of your JavaScript and CSS were actually used while you used the page. It shows a red/green bar per file and highlights unused code in the Sources panel.

A large amount of unused code at load time suggests code splitting, lazy loading routes or removing dead CSS. Keep in mind that some code is used later, after interactions.

## 276: What is the difference between lab data and field data?

- **Lab data** comes from a controlled test, like Lighthouse or a DevTools recording. It's repeatable and good for debugging, but uses one device and network.
- **Field data** (RUM) comes from real users on real devices, like CrUX or your own `web-vitals` reporting. It shows what users really experience, including slow phones and bad networks.

Google Search uses field data from CrUX for Core Web Vitals. A good Lighthouse score doesn't guarantee good field data.

## 277: What is the Chrome UX Report (CrUX)?

CrUX is a public dataset of real-user performance data collected from Chrome users who opted in to sharing usage statistics. It contains LCP, INP, CLS, FCP, TTFB and more, per origin and per popular URL, split by device type.

You can see it in PageSpeed Insights, in the DevTools Performance panel (live metrics with field data), through the CrUX API and in BigQuery. Pages without enough traffic don't have data.

## 278: Why is measuring performance in single-page apps tricky?

Core Web Vitals are tied to page loads. In an SPA, route changes are same-document navigations, so LCP and CLS are only measured for the first load, and INP and CLS keep growing across all "pages" the user visits.

Chrome has been working on "soft navigation" detection, which treats a user interaction that changes the URL and paints new content as a new navigation with its own metrics. Until it's fully standard, SPAs often add their own timing with the User Timing API.

## 279: Why can a preload cause a double download?

Fonts are always fetched in CORS mode. If you preload a font without `crossorigin`, the preload is a non-CORS request and doesn't match the real font request, so Chrome downloads it twice.

```html
<!-- correct -->
<link
  rel="preload"
  href="/fonts/inter.woff2"
  as="font"
  type="font/woff2"
  crossorigin
/>
```

The same mismatch happens if `as` is wrong. Chrome logs a console warning when a preloaded resource isn't used within a few seconds of the load event.

## 280: How does Chrome pick an image from srcset and sizes?

With `srcset` width descriptors and `sizes`, Chrome calculates how wide the image will be shown (from `sizes` and the viewport), multiplies by the device pixel ratio, and picks the smallest candidate that's big enough.

```html
<img
  src="photo-800.jpg"
  srcset="photo-400.jpg 400w, photo-800.jpg 800w, photo-1600.jpg 1600w"
  sizes="(max-width: 600px) 100vw, 50vw"
  alt="Photo"
/>
```

If a larger version is already in the cache, Chrome may use it instead. Without `sizes`, Chrome assumes `100vw`, which often makes it download a bigger image than needed.

## 281: How can you adjust fallback fonts to reduce layout shift?

Use `@font-face` descriptors to make the fallback font take the same space as the web font:

```css
@font-face {
  font-family: "Inter Fallback";
  src: local("Arial");
  size-adjust: 107%;
  ascent-override: 90%;
  descent-override: 22%;
  line-gap-override: 0%;
}
body {
  font-family: "Inter", "Inter Fallback", sans-serif;
}
```

When the real font loads and swaps in, text barely moves, so there is less CLS. Frameworks like Next.js generate these values automatically.

## 282: What are origin trials?

Origin trials let developers try a new or experimental Chrome feature on their real site for a limited time. You register your origin, get a token and add it to your pages:

```html
<meta http-equiv="origin-trial" content="YOUR_TOKEN" />
```

The feature then works for all your users without them changing flags. Chrome uses feedback from trials to adjust the API before shipping. Trials have an end date, so you must not depend on them permanently.

## 283: How does a new feature get added to Chrome?

Blink has a public process. A feature goes through stages announced on the `blink-dev` mailing list: "Intent to Prototype," then often "Intent to Experiment" (origin trial), and finally "Intent to Ship," which needs approval from three Blink API owners. Status is tracked on chromestatus.com.

The process asks about standards status, other browsers' positions, security, privacy and tests. Deprecations and removals go through a similar "Intent to Deprecate and Remove."

## 284: What are Web Platform Tests?

Web Platform Tests (WPT) is a shared test suite used by all browser engines to check that they implement web standards the same way. Chrome imports and runs it continuously, and new Blink features are expected to add tests there.

Results for every browser are public on wpt.fyi. It's a good place to check if a bug is a Chrome bug or a spec issue.

## 285: What is Local Network Access?

Local Network Access is a Chrome security feature that stops public websites from silently sending requests to devices on your local network, like your router admin page or a printer. This kind of request has been used to attack home devices.

Chrome now asks the user for permission when a public site tries to reach a private IP address or `localhost`. It replaces an earlier approach called Private Network Access, which used special CORS preflights.

## 286: What is the difference between WebSockets and WebTransport?

- **WebSocket**: one bidirectional message stream over a TCP connection. Simple and supported everywhere, but a lost packet delays all messages.
- **WebTransport**: runs over HTTP/3 (QUIC). It supports many independent streams and also unreliable datagrams, which are good for games and live media where old data doesn't matter.

Chrome supports both. WebTransport has a more modern API based on streams.

## 287: What is the Service Worker Static Routing API?

It lets a Service Worker tell Chrome, during install, that some requests should go straight to the network or to the cache without starting the worker at all.

```js
self.addEventListener("install", (event) => {
  event.addRoutes([
    { condition: { urlPattern: "/api/*" }, source: "network" },
    { condition: { urlPattern: "/static/*" }, source: "cache" },
  ]);
});
```

This removes the cost of starting the worker for requests where it would just pass them through. Chrome shipped it in Chrome 123.

## 288: How do tabs of the same origin talk to each other?

- **BroadcastChannel**: send messages to all tabs and workers of the same origin.
- **localStorage `storage` event**: fires in other tabs when a key changes.
- **SharedWorker**: one worker shared by all tabs of the origin.
- **Service Worker** with `clients.matchAll()` and `postMessage`.
- **Web Locks API**: coordinate who does a task, like one tab keeping a WebSocket open.

```js
const ch = new BroadcastChannel("auth");
ch.postMessage({ type: "logout" });
ch.onmessage = (e) => {
  if (e.data.type === "logout") location.reload();
};
```

With storage partitioning, these only reach contexts in the same partition.

## 289: What is a SharedWorker?

A SharedWorker is a worker that several tabs, windows or iframes of the same origin can connect to at the same time. It's useful for sharing one WebSocket connection or one in-memory cache across tabs.

```js
const worker = new SharedWorker("shared.js");
worker.port.postMessage("hello");
worker.port.onmessage = (e) => console.log(e.data);
```

Chrome on Android added SharedWorker support later than desktop, so older versions may not support it.

## 290: How does Chrome evict site data when disk space is low?

Best-effort storage (IndexedDB, Cache Storage, localStorage, Service Workers and so on) can be cleared when the device runs low on space. Chrome deletes whole origins at once, choosing the least recently used origins first.

Origins with persistent storage (granted after `navigator.storage.persist()`) are not evicted automatically. Chrome grants persistence based on things like whether the site is bookmarked, installed or used a lot.

## 291: What is the Storage Access API?

When third-party cookies are blocked (for example in Incognito or by user settings), an embedded iframe can call `document.requestStorageAccess()` to ask for access to its unpartitioned cookies.

```js
button.addEventListener("click", async () => {
  try {
    await document.requestStorageAccess();
    loadUserComments();
  } catch {
    showLoginLink();
  }
});
```

It must be called after a user gesture, and Chrome may show a prompt. It is used for things like embedded comments or SSO widgets.

## 292: What is FedCM?

FedCM (Federated Credential Management) is a browser API for "Sign in with..." flows. Instead of the identity provider using third-party cookies, redirects or popups, the browser shows its own account chooser and handles the exchange between the site and the identity provider.

Google Identity Services uses FedCM in Chrome. It's one of the privacy APIs Chrome kept after retiring most of the Privacy Sandbox.

## 293: How do passkeys work in Chrome?

Passkeys use the WebAuthn API. The site asks the browser to create a key pair; the private key stays on the device or in a password manager (like Google Password Manager), and the site stores only the public key. To log in, the device signs a challenge after the user unlocks it with a fingerprint, face or PIN.

```js
const cred = await navigator.credentials.get({
  publicKey: { challenge, rpId: "example.com", userVerification: "preferred" },
  mediation: "conditional", // show passkeys in the autofill dropdown
});
```

Passkeys can't be phished, because the browser binds them to the site's domain.

## 294: What is the Web Locks API?

Web Locks lets scripts of the same origin, in different tabs or workers, take named locks so only one runs a piece of code at a time.

```js
await navigator.locks.request("token-refresh", async () => {
  const token = await refreshToken();
  localStorage.setItem("token", token);
});
```

It's useful when several tabs might do the same task, like refreshing an auth token or running a database migration. The lock is released when the callback's promise settles or the tab closes.

## 295: How does the Async Clipboard API work in Chrome?

```js
await navigator.clipboard.writeText("Copied!");
const text = await navigator.clipboard.readText();
```

Writing works when the page has focus and usually needs a user gesture. Reading requires the `clipboard-read` permission, so Chrome shows a prompt. Both only work in secure contexts. You can also read and write images and other types with `ClipboardItem`.

## 296: How do you profile JavaScript CPU usage in Chrome?

Use the Performance panel and look at the flame chart for the main thread. Wide bars are slow functions; use the "Bottom-Up" tab to see which functions take the most self time.

To simulate a slower device, set CPU throttling (4x or 6x slowdown). Make sure source maps are loaded so you see your original code. For Node.js or workers, you can attach DevTools to them and use the same profiler.

## 297: What are DevTools local overrides?

Local overrides let you change files or response headers in DevTools and keep those changes across reloads. Chrome serves your local copy instead of the network version.

This is useful for testing a fix on a production site, trying new caching or CSP headers, or mocking an API response, without deploying anything.

## 298: What is the Save-Data header?

When the user turns on a data-saving mode (common on Android in some regions), Chrome sends `Save-Data: on` with requests. JavaScript can check it too:

```js
if (navigator.connection?.saveData) {
  loadLowResImages();
}
```

Servers and pages can respond by sending smaller images, skipping autoplay video or not prefetching. The Network Information API also gives `effectiveType` like `4g` or `3g` in Chrome.

## 299: How does Chrome handle `<link rel="modulepreload">`?

`modulepreload` downloads a JavaScript module early and parses and compiles it ahead of time, so it's ready when the module graph needs it. Chrome only fetches the module you list, so list its important imports too to avoid a waterfall.

```html
<link rel="modulepreload" href="/js/app.js" />
<link rel="modulepreload" href="/js/router.js" />
```

Unlike `preload` with `as="script"`, it uses the correct CORS mode and credentials for modules and puts the result straight in the module map. Build tools like Vite add these tags automatically.

## 300: How does the browser handle a 304 Not Modified response?

When a cached response is stale, Chrome sends a conditional request with `If-None-Match` (the stored `ETag`) or `If-Modified-Since`. If the resource hasn't changed, the server replies `304 Not Modified` with no body.

```http
GET /app.css
If-None-Match: "abc123"

HTTP/1.1 304 Not Modified
ETag: "abc123"
Cache-Control: max-age=600
```

Chrome then uses the cached body and updates its freshness from the new headers. This saves bandwidth but still costs a round trip, which is why long `max-age` with hashed file names is better for static files.

---

# Advanced Questions (301-450)

## 301: What is RenderingNG?

RenderingNG is the name for Chrome's rendering architecture after a multi-year rewrite that finished around 2021-2022. It includes several projects:

- **LayoutNG**: new layout engine with immutable fragments.
- **BlinkNG**: cleaner separation of pipeline stages in Blink.
- **CompositeAfterPaint**: deciding layers after paint, not before.
- **Out-of-process raster (OOP-R)** and **out-of-process display compositor (OOP-D)**: raster and display work moved to the GPU process.
- **VideoNG** and **Non-blocking commit**, among others.

The goals were reliability, predictable performance and making it easier to add new features like container queries and View Transitions.

## 302: List the stages of Chrome's rendering pipeline and the thread each runs on.

1. **Animate**: update computed styles from animations (main thread, and compositor for compositor animations).
2. **Style**: compute styles (main).
3. **Layout**: produce the fragment tree (main).
4. **Pre-paint**: build property trees and invalidate paint (main).
5. **Scroll**: update scroll offsets (main and compositor).
6. **Paint**: record display lists (main).
7. **Commit**: copy property trees and display lists to the compositor (main to compositor).
8. **Layerize**: split display lists into composited layers (compositor).
9. **Raster, decode and paint worklets**: turn display lists into GPU textures (GPU process, raster threads).
10. **Activate**: make the new tree the one to draw (compositor).
11. **Aggregate**: Viz combines frames from all processes (GPU process).
12. **Draw**: Viz draws the final frame (GPU process).

## 303: What are property trees?

Property trees hold the visual properties that affect how content is drawn, separate from the content itself. There are four:

- **Transform tree**: transforms and scroll offsets.
- **Clip tree**: overflow and clip rects.
- **Effect tree**: opacity, filters, masks, blend modes.
- **Scroll tree**: scrolling info like which areas scroll and their size.

Every paint chunk points to a node in each tree. With this, the compositor can change a transform or scroll offset without touching the content, and Chrome avoids the problems the old layer tree had, where layer hierarchy and visual properties were tangled together.

## 304: What is CompositeAfterPaint and why did it matter?

In the old design, Blink decided which elements get compositor layers before painting, based on the layout tree. That logic was complex, buggy (layers didn't always match what was painted) and caused correctness issues with overlap.

With CompositeAfterPaint (shipped in Chrome 94), Blink first paints everything into one display list with property tree info, and only then decides how to split it into layers. Layering decisions are made from the paint output and property trees, which made them simpler, more correct and allowed better layer squashing.

## 305: What are the pending tree and active tree in the compositor?

The compositor keeps more than one copy of the layer tree:

- **Pending tree**: receives the latest commit from the main thread. Its tiles are rasterized here.
- **Active tree**: the one being drawn right now.

When enough of the pending tree's visible tiles are rasterized, the compositor "activates" it, and it becomes the new active tree. This way the screen never shows a half-rasterized new frame; the old frame keeps being drawn (and can still scroll and animate) until the new one is ready.

## 306: What happens during commit?

Commit is the step where the main thread hands its output to the compositor: the property trees, display lists and layer info. During commit the main thread and compositor thread are synchronized, so the data can be copied safely.

Historically the main thread was blocked during the whole commit. With "non-blocking commit," Chrome reduced how long the main thread waits, so it can start the next frame's work sooner.

## 307: What is BeginMainFrame?

BeginMainFrame is the message the compositor thread sends to the main thread to ask it to produce a new frame. It's triggered by a BeginFrame from Viz (based on VSync) when the compositor needs new main-thread content, for example because the DOM changed or a rAF callback is pending.

When the main thread gets it, it runs input handlers, rAF callbacks, style, layout, pre-paint and paint, and then commits. If the main thread doesn't answer in time, the compositor can still produce frames using the old content.

## 308: How does the compositor keep producing frames when the main thread is busy?

The compositor has its own copy of the layer tree, property trees and rastered tiles. On each BeginFrame it can:

- Apply scroll offsets from input it handled itself.
- Advance compositor animations (`transform`, `opacity`, some `filter`s, scroll-driven animations).
- Rasterize new tiles that come into view from existing display lists.

So scrolling and compositor animations stay at 60 fps even during a 500 ms JavaScript task. Anything that needs new main-thread work, like DOM changes or rAF animations, waits.

## 309: What is a surface in Viz?

A surface is a place that receives a stream of compositor frames from one client, such as a renderer's frame, the browser UI, a video, or an OOPIF. Each surface has a `SurfaceId` (a frame sink ID plus a local surface ID that changes when the size or device scale changes).

A compositor frame can embed another surface by its ID. Viz's surface aggregator walks these references and combines the latest frames from all surfaces into one frame to draw. This is how a page with cross-process iframes ends up as one image.

## 310: Why does a LocalSurfaceId need to be synchronized between processes?

When an embedded frame is resized (for example an OOPIF changes size), the parent and child must agree on which frame from the child fits the new size. Chrome gives the new size a new `LocalSurfaceId`. The parent embeds that ID, and Viz shows the child's frame only when the child submits a frame for that ID.

Until then Viz can show the older frame (stretched or with a fallback) instead of a frame with the wrong size. This avoids visible glitches during resizes and zoom changes.

## 311: What is out-of-process raster (OOP-R)?

Before OOP-R, the renderer process rasterized content itself (using the GPU through a command buffer, or the CPU). With OOP-R, the renderer serializes the display lists and sends them to the GPU process, where Skia rasterizes them directly into GPU textures.

Benefits: less work and memory in the renderer, raster code runs where the GPU context lives, better use of the GPU, and a single place for GPU resource management. It also helped prepare for Skia Graphite and Vulkan.

## 312: What is the GPU command buffer?

The command buffer is the mechanism renderers use to send GPU commands to the GPU process. The client writes commands into shared memory and the GPU process reads, validates and executes them on the real driver.

Validation matters because the renderer is untrusted. Bad commands must not crash the driver or read memory they shouldn't. This design is also why WebGL and canvas calls are asynchronous under the hood, and why reading pixels back (`getImageData`, `readPixels`) can be slow: it forces a round trip to the GPU process.

## 313: Why is getImageData on a canvas slow?

For an accelerated canvas, the pixels live in a GPU texture in the GPU process. `getImageData()` has to flush all pending drawing commands, wait for the GPU to finish, copy the pixels back to CPU memory and send them to the renderer. That stalls the main thread.

If you need to read pixels often, create the context with `willReadFrequently`, so Chrome keeps that canvas on the CPU:

```js
const ctx = canvas.getContext("2d", { willReadFrequently: true });
```

## 314: What is the difference between Skia Ganesh and Skia Graphite?

**Ganesh** is Skia's older GPU backend, designed around OpenGL. It mostly records and submits work on one thread and doesn't fit well with modern explicit APIs.

**Graphite** is the new backend built for Metal, Vulkan and Direct3D 12 (often through Dawn). It is designed to record work on several threads, compiles pipelines ahead of time to avoid shader compile stutter, and uses depth testing to reduce overdraw. Chrome launched it on Apple Silicon Macs in 2025, with results like about 15% better MotionMark scores, and is rolling it out to other platforms.

## 315: How does the compositor decide which tiles to rasterize first?

Each tile gets a priority based on its distance from the viewport and the direction and speed of scrolling. Tiles that are visible now come first, then tiles in the "soon" area just outside the viewport (more in the scroll direction), then everything else up to the memory budget.

The tile manager keeps rastered tiles within a GPU memory limit and drops far-away ones. If you scroll faster than raster can keep up, you see checkerboarding: empty or placeholder areas that fill in a moment later.

## 316: Why can text on an animated scaled layer look blurry?

When you animate `transform: scale()` on the compositor, the layer's existing tiles are scaled on the GPU instead of re-rasterized every frame. If the layer was rastered at a small scale, scaling it up makes it blurry until Chrome re-rasters it at the final scale.

Chrome tries to pick a good raster scale and re-rasters after the animation ends, but this trade-off (sharpness vs. raster cost) is why scale animations can look soft for a moment. Using `will-change: transform` for a long time can lock in a raster scale.

## 317: What are hardware overlays?

An overlay lets the display hardware place some content, like a video or the whole page, directly on screen without the GPU compositing it into a single image first. On Windows Chrome uses DirectComposition, on macOS Core Animation layers, on Android SurfaceControl.

Viz decides per frame which quads can be overlays. For full-screen or large videos this saves a lot of GPU work and power. That's one reason playing video in a normal `<video>` element is much cheaper than drawing it into a canvas.

## 318: How does Viz route input to the right process when there are OOPIFs?

The browser process gets the event and has to find which frame is under the pointer. Each renderer sends hit-test data with its compositor frames, describing regions and which surface (frame) they belong to. Viz uses this data, with the property trees, to find the target surface quickly without asking the renderers.

If the hit-test data isn't enough (for example complex clip paths or certain transforms), the browser asks the renderer for a precise slow-path hit test. Then the event is sent to the right renderer, with coordinates converted into that frame's space.

## 319: How does Chrome throttle iframes?

Chrome stops rendering updates for cross-origin iframes that are off-screen or hidden (`display: none` or `visibility: hidden`). They don't run rAF callbacks or produce frames, which saves CPU, GPU and battery.

Same-origin iframes are throttled when hidden or off-screen in some cases too. Timers in throttled frames keep running (subject to other limits). An iframe that is never visible, like a hidden ad tracker, still costs memory and network but much less rendering time.

## 320: What is the Blink scheduler?

The Blink scheduler decides which task runs next on the renderer's main thread. Instead of one FIFO queue, it has many task queues with types and priorities: input, rendering, loading, timers, idle, and so on, per frame.

It can raise the priority of input and rendering when the user is interacting, delay loading or timer tasks, throttle tasks in background frames, and pause queues for frozen pages. `scheduler.postTask()` maps onto these priorities.

## 321: How does Chrome prevent rendering from being starved by other tasks?

If the main thread always had another task to run, rendering might never happen. The Blink scheduler tracks how long it has been since the last frame. If too much time passes without a frame, rendering tasks get a higher priority than normal tasks, so a frame is produced even when lots of tasks are queued.

Input events are also prioritized, and continuous input is aligned to frames. The goal is to keep the page visually updating even under heavy load.

## 322: What is the document lifecycle in Blink?

Blink tracks which pipeline stage the document is in: for example `kVisualUpdatePending`, `kInStyleRecalc`, `kStyleClean`, `kInPerformLayout`, `kLayoutClean`, `kInPrePaint`, `kPrePaintClean`, `kInPaint`, `kPaintClean`.

Code checks these states with assertions. For example, paint code can't read layout data unless layout is clean, and code during paint can't change the DOM. This was a big part of BlinkNG and removed many bugs where one stage changed data another stage had already used.

## 323: How does LayoutNG cache layout results?

Each layout result is cached on the layout object together with the constraint space (the input: available size, percentage resolution size, and so on). On the next layout, if the node isn't dirty and the new constraint space matches (or is compatible), LayoutNG reuses the cached fragment instead of laying it out again.

There is also a cache for min/max content sizes, used by flex, grid and tables. Since fragments are immutable, reusing them is safe.

## 324: How do container queries fit into the rendering pipeline?

Container queries make styles depend on a container's size, which is only known after layout. That breaks the normal "style first, then layout" order.

Blink handles it by interleaving: it lays out the container first (requiring `container-type` so the container's size doesn't depend on its children), then calculates the style of the container's descendants with the size known, and continues layout inside. Size containment on the container is what prevents loops.

## 325: How does :has() work and why was it hard to implement?

`:has()` matches an element based on its descendants or following siblings, like `article:has(img)`. Normal selector matching walks up the tree, but `:has()` looks downward, and a change deep in the tree can change the style of an ancestor.

Blink made it fast enough by caching `:has()` results during style recalc and building invalidation sets that flag possible "has anchor" elements, so a DOM change only invalidates ancestors that could be affected. Still, very broad `:has()` selectors on large trees can be expensive.

## 326: What is the difference between paint invalidation and raster invalidation?

- **Paint invalidation**: deciding which display items must be re-recorded because their content or geometry changed. Blink compares new paint output with cached items and reuses the unchanged ones.
- **Raster invalidation**: deciding which areas of composited layers must be re-rasterized. The compositor then re-rasters only the tiles touching those rects.

A small change, like a color on a button, ideally causes a small paint invalidation and a tiny raster invalidation. Paint flashing in DevTools shows the raster invalidation areas.

## 327: Why can a small change cause a large repaint?

Some reasons:

- The changed element is on a large layer, and the change affects a big area (like a background or box shadow of a full-page element).
- The element isn't on its own layer, so the whole layer it's painted into must be re-rastered in that area.
- Effects like `filter: blur()` or large shadows expand the invalidated area.
- A change in one element shifts layout of many others.

Moving frequently changing elements onto their own layer (with care) or changing them in a way that doesn't affect layout limits the area.

## 328: What are layer squashing and overlap testing?

When an element needs a composited layer, everything painted after it that overlaps it also needs a layer, otherwise the paint order would be wrong. Overlap testing checks this.

To avoid creating hundreds of layers, Chrome "squashes" multiple overlapping elements that don't need their own layer into a single shared layer. With CompositeAfterPaint, this is done on paint chunks. It reduces GPU memory, but squashing can't happen in some cases, for example when elements have different transform or clip nodes.

## 329: How does Chrome handle animations in the style engine?

When style is calculated, CSS animations and transitions are created or updated. Each frame, the animation system computes the current animated values and applies them as a layer on top of the base computed style.

If an animation is "compositable" (supported property, no conflicting effects), Blink sends it to the compositor with its keyframes and timing. The compositor ticks it independently, and the main thread only syncs with it when something changes, like the animation being paused from JavaScript.

## 330: Why might a transform animation not run on the compositor?

Some causes:

- Another property in the same animation isn't compositable, like `width`.
- The element's transform depends on its size in a way that changes during the animation (percent values with changing size).
- The element has certain effects or the transform is set on an SVG element in some cases.
- Hardware acceleration is off.
- The animation uses keyframes Chrome can't send to the compositor.

DevTools' Performance panel shows "Animation" entries and notes when an animation isn't composited, along with the reason.

## 331: What does "scroll unification" mean in Chrome?

In older Chrome, some scrolls were handled on the compositor thread and some, like scrolls of elements that couldn't be composited, were handled on the main thread with a different code path. Behavior could differ between them.

Scroll unification moved all scrolling to the compositor thread's logic. When the compositor can't do it alone (for example blocking listeners), it still asks the main thread for help, but the scroll itself is always done by one code path. This fixed bugs and made scrolling more consistent.

## 332: How does Chrome decide whether a scroller can be composited?

Chrome wants to composite scrollers so scrolling is fast. A scroller needs a few things to be composited without visual problems, mainly being able to draw text correctly. In the past, scrollers with non-opaque backgrounds couldn't use LCD (subpixel) text antialiasing if composited, so Chrome sometimes didn't composite them.

Today Chrome composites most scrollers, especially on high-DPI screens where LCD text matters less. If a scroller isn't composited, scrolling it needs repaint on the main thread, which is slower.

## 333: What is the image decode cache and discardable memory?

Decoded images are large. Chrome keeps them in a decode cache so they can be reused across frames and tiles. The memory for this cache is often "discardable": Chrome can lock it while using it and unlock it after, and under memory pressure the OS or Chrome can free unlocked parts.

If a decoded image was discarded, it is decoded again the next time it's needed. Large or many images can make this cache churn, which shows up as repeated decode tasks in a trace.

## 334: How do you think about GPU memory as a front-end developer?

Every composited layer and rastered tile uses GPU memory: roughly width x height x 4 bytes, multiplied by the device pixel ratio squared. A full-screen layer on a 3x phone can be tens of megabytes.

Things that add up: many `will-change` elements, very large layers (for example a huge element with a transform), big canvases, many video elements. When Chrome hits its GPU memory budget, it drops tiles and you see checkerboarding or slow raster. The Layers panel shows each layer's memory estimate.

## 335: What is BlinkNG?

BlinkNG was a project to clean up Blink's rendering pipeline so each stage has clear inputs and outputs and runs in a fixed order. It added the strict document lifecycle checks, moved logic into the right stages (for example creating property trees in pre-paint), and removed cases where later stages reached back and changed earlier data.

It made features like container queries, `content-visibility` and CompositeAfterPaint possible, because the pipeline became predictable enough to interleave or skip stages safely.

## 336: What is pre-paint?

Pre-paint is the stage between layout and paint. It walks the layout tree and builds or updates the property trees (transform, clip, effect, scroll) and works out paint invalidations, for example which objects moved or changed visually.

Separating it from paint makes paint simpler: paint only records drawing commands using the property tree nodes that pre-paint already built.

## 337: How does content-visibility work internally?

`content-visibility: auto` uses a mechanism called display locking. When the element is off-screen, Blink "locks" its subtree, which means style, layout and paint for the subtree are skipped. The element is sized by `contain-intrinsic-size` (or the last remembered size with `auto`).

When the element nears the viewport, or something needs its contents (find-in-page, focus, accessibility, `scrollIntoView`), Blink unlocks it and runs the skipped work. Reading layout values inside a locked subtree from JavaScript also forces it to update.

## 338: Explain the cost difference between changing a CSS custom property on :root vs on a component.

Changing a custom property on `:root` can affect every element that inherits it, so Blink may need to recalculate style for the whole document. Blink has optimizations (like tracking which elements actually use the property and independent inheritance), but in the worst case it's a full-page style recalc.

Setting the property on a smaller container limits recalc to that subtree. Registered properties (`@property`) with `inherits: false` are even cheaper, because they don't propagate to children.

## 339: How does font loading affect layout?

When a web font finishes loading, every text node using that font family must be re-shaped and laid out again, because glyph widths change. On text-heavy pages, this can cause a noticeable layout and CLS.

Blink only invalidates text that uses the loaded font face. Using `font-display: optional` (no swap after a short timeout), matching fallback metrics and preloading critical fonts reduce the cost.

## 340: What is the hit-test cache and why is hit testing sometimes slow?

Hit testing walks the layout and paint information to find which element is under a point. Chrome does it for every pointer event, `elementFromPoint()`, hover state updates and more. On huge or deeply nested pages, or with many transforms and clip paths, it gets slow.

Blink caches the last hit-test result for repeated queries at the same point when nothing has changed. During scroll, Chrome delays hover updates to avoid hit testing on every frame.

## 341: Why does hover sometimes not update while scrolling?

To keep scrolling smooth, Chrome doesn't run a hit test and update `:hover` state on every scroll frame. It updates hover after scrolling settles (or at a lower rate). Otherwise each frame would need a main-thread hit test plus style recalc for elements entering and leaving hover.

This is a performance choice, not a bug. If a hover style must follow the pointer during scroll, you need different design, but usually users don't notice.

## 342: How does Chrome render a cross-origin iframe inside a page it composites?

The parent renderer lays out and paints the page, leaving a placeholder for the iframe that references the iframe's surface. The iframe's renderer process produces its own compositor frames for its surface.

Viz combines them: the parent's frame contains a surface draw quad pointing to the child's surface ID, and Viz draws the child's latest frame in that place with the right transform and clip. The parent never sees the child's pixels, which is important for security.

## 343: What problems does rendering OOPIFs in a separate process cause?

- **Synchronization**: the parent and child must agree on size, scale and visibility, which happen in different processes.
- **Input**: events must be routed to the right process, with coordinate transforms.
- **Effects and transforms**: CSS transforms, clips and filters on the iframe element must be applied to a surface rendered by another process.
- **Memory**: each process has overhead, so many cross-site iframes cost a lot.
- **Throttling and lifecycle**: each process needs to know if its frame is visible.

Chrome solved these with property tree info passed to the child, Viz hit-testing, and surface synchronization.

## 344: How does the compositor handle a fixed-position element during scroll?

`position: fixed` elements are attached to the viewport's transform node, not the scrolling content's. When the compositor scrolls the content, it updates only the scroll offset in the transform tree, and the fixed element stays in place.

If a fixed element is inside an element that creates a containing block (like a parent with `transform` or `will-change: transform`), it becomes fixed relative to that parent instead. That's a common surprise.

## 345: What is the VideoNG project?

VideoNG was a rework of Chrome's video playback pipeline as part of RenderingNG. It focused on smoother playback (better frame timing aligned with the display), using hardware overlays more, and lower power use.

Video frames are passed to Viz as resources that can go to an overlay directly, and the video's frame timing is handled closer to the display, so frames are shown at the right moment even when the renderer's main thread is busy.

## 346: How does Chrome measure frame quality internally?

Chrome tracks metrics like "dropped frames" and "percent dropped frames" in a sliding window, based on whether each frame that should have shown new content actually did. It cares more about frames that were expected to change (during scroll or animation) than idle frames.

DevTools shows similar info in the Frames track: green frames were presented on time, yellow are partially presented (some updates missed), and red are dropped.

## 347: What is a partially presented frame?

A partially presented frame is one where the compositor produced a new frame (for example the scroll updated) but some content from the main thread wasn't ready, so it shows old main-thread content with new compositor changes.

This happens when the main thread is busy but the compositor can still scroll. The user sees smooth scrolling, but something like a rAF-driven animation may lag. DevTools marks these frames in yellow.

## 348: What happens when you call element.getBoundingClientRect() during a compositor-driven scroll?

`getBoundingClientRect()` runs on the main thread. The main thread's scroll offset is updated from the compositor at the start of each main frame. So during a fast compositor scroll, the value you read can be slightly behind what's on screen.

That's why syncing elements to scroll position in JavaScript can look jittery. Using `position: sticky`, scroll-driven animations or IntersectionObserver lets the browser handle the sync correctly.

## 349: How do paint worklets run?

A paint worklet (CSS Paint API) is called during paint to draw an element's background or border image. Chrome can run paint worklets off the main thread for some cases, like when they only depend on registered custom properties being animated, so the compositor can animate them.

The worklet gets a limited canvas-like context, the element's size and the input properties. It can't access the DOM or network, and the browser may call it many times or keep several instances, so it must have no side effects.

## 350: What is the difference between raster on the CPU and GPU raster in terms of trade-offs?

- **CPU (software) raster**: works everywhere and has consistent results, but is slower for large areas and complex effects, and the result must be uploaded to the GPU.
- **GPU raster**: much faster for most content, especially paths, gradients and images, and avoids uploads. But it depends on drivers, may have small rendering differences and can hit GPU memory limits.

Chrome uses GPU raster almost everywhere today and falls back to CPU raster when the GPU is unavailable or the content is unsupported.

## 351: How is the renderer sandbox implemented on each operating system?

- **Windows**: the renderer runs with a restricted token, in a job object, at a low integrity level, on a separate desktop, with many Win32 calls blocked. Newer Windows versions also add process mitigation policies (for example no dynamic code in some processes, no loading of unsigned DLLs).
- **Linux and ChromeOS**: namespaces (user, PID, network) cut the process off from the system, and seccomp-bpf filters block most system calls.
- **macOS**: the Seatbelt sandbox, with a profile that denies file, network and most system access.
- **Android**: renderers run as isolated processes with their own UID and very limited permissions, plus seccomp.

In all cases, anything the renderer needs from the outside goes through IPC to a more trusted process.

## 352: Why does Chrome treat the renderer process as compromised?

Renderers run untrusted JavaScript, HTML, fonts, images and Wasm through huge, complex code like V8 and Blink. Bugs there are found often. So Chrome's security model assumes an attacker may fully control a renderer.

Because of that, the browser process and services never trust what a renderer says. If a renderer claims to be `bank.com`, asks for cookies of another site, or sends a malformed Mojo message, the browser checks it against what it knows about that process (its site lock) and kills the renderer if the request is not allowed.

## 353: What is a process lock (site lock)?

When a renderer process commits a document from a site, the browser process records that this process is locked to that site, for example `https://example.com`. From then on, the browser only gives that process data for that site.

If the process asks for cookies, localStorage, passwords or tries to commit a document from a different site, `ChildProcessSecurityPolicy` sees the mismatch and refuses, usually by terminating the process. This is what makes Site Isolation hold up even when a renderer is compromised.

## 354: What is the "Rule of Two" in Chromium security?

The Rule of Two says new code may have at most two of these three properties:

1. It processes untrustworthy input.
2. It is written in an unsafe language (C or C++).
3. It runs with no sandbox (high privilege).

For example, parsing a file format from the web in C++ is fine inside a sandboxed process, but not in the browser process. In the browser process, it has to be done in a memory-safe language like Rust, or moved to a sandboxed utility process.

## 355: What does a typical full Chrome exploit chain look like?

Usually two or more bugs:

1. **Renderer remote code execution**: often a V8 bug (like a type confusion in the JIT) that gives read/write access to memory, used to run code in the renderer.
2. **Sandbox escape**: a bug in the browser process, GPU process, a Mojo interface or the OS kernel that lets the attacker leave the sandbox.

Some chains also need a V8 sandbox bypass between those two steps. This layered design is why single bugs are worth much less to attackers and why Chrome pays high bug bounties for sandbox escapes.

## 356: What is the V8 sandbox?

The V8 sandbox (also called the heap sandbox) is a software isolation layer inside V8. The V8 heap is placed in a large reserved memory region, and pointers inside it are stored as offsets or indexes into tables, not raw addresses.

So even if an attacker corrupts V8 objects through a bug, they can only read and write inside that region, not the rest of the renderer's memory. Escaping it requires a second bug. It's been enabled in Chrome on 64-bit platforms and is part of the V8 bug bounty.

## 357: What is MiraclePtr?

MiraclePtr (`raw_ptr<T>` in Chromium code) is a smart pointer type that protects against use-after-free bugs. It works with PartitionAlloc's BackupRefPtr: each allocation keeps a count of `raw_ptr` references. If the object is freed while references still exist, the memory is "quarantined" and poisoned instead of reused.

That turns many use-after-free bugs, a top source of browser exploits, into non-exploitable crashes. Chromium rewrote large parts of its code to use `raw_ptr` for class fields.

## 358: What is PartitionAlloc?

PartitionAlloc is Chromium's memory allocator. It splits allocations into partitions by type and size, so objects of different kinds don't sit next to each other. This makes some memory corruption attacks harder, because an attacker can't easily place a controlled object where a freed one of another type was.

It's also tuned for performance and memory use, and it provides the base for security features like BackupRefPtr (MiraclePtr) and memory tagging on supported hardware.

## 359: Why is Chromium adopting Rust?

Around 70% of serious security bugs in Chromium are memory safety bugs, mostly in C++. Rust prevents most of them at compile time.

Chromium uses Rust for new code that handles untrusted input, for example font parsing (Skrifa, replacing FreeType for web fonts), the jxl-rs JPEG XL decoder, and work to move other image decoders and parsers to Rust. Because Rust code is memory safe, it can follow the Rule of Two even in more privileged processes.

## 360: How does Chrome find security bugs before attackers?

- **Fuzzing**: ClusterFuzz runs fuzzers (libFuzzer, AFL, custom ones for V8 and Mojo) on huge numbers of machines all the time and files bugs automatically.
- **Sanitizers**: AddressSanitizer, MemorySanitizer, UBSan and others in test builds.
- **Bug bounty**: the Chrome Vulnerability Reward Program pays outside researchers.
- **Internal teams**: Google Project Zero and Chrome security engineers.
- **AI tools**: Google has also used AI-based tools to find and review bugs.

Fixed security bugs stay hidden for a while after release so users can update first.

## 361: Why are JIT compilers a common source of security bugs?

The optimizing compiler makes assumptions about types and value ranges to remove checks, like bounds checks or type checks. If the compiler's reasoning is wrong in one edge case, the generated machine code can skip a check it needed. This often leads to type confusion or out-of-bounds memory access, which attackers turn into arbitrary read and write.

Because of this, V8 added the V8 sandbox, and Chrome lets users or admins turn off the V8 optimizers for sites they don't trust, which removes most of the JIT attack surface at the cost of speed.

## 362: What was Spectre and how did it change browsers?

Spectre (2018) showed that CPUs' speculative execution can leak memory contents through timing side channels. JavaScript in a page could read any memory in its own process, including data from other sites loaded into that process.

Browsers reacted by:

- Reducing timer precision and disabling `SharedArrayBuffer` at first.
- Chrome enabling Site Isolation so other sites' data isn't in the same process.
- Adding ORB (CORB) to keep cross-site data responses out of renderers.
- Bringing back precise timers and `SharedArrayBuffer` only for cross-origin isolated pages.

## 363: How is Site Isolation different on Android?

Android devices often have less memory, so full Site Isolation for every site would cost too much. Chrome on Android isolates only some sites: sites where users log in (detected by password entry or OAuth), sites that send headers like COOP, and some others.

Other sites can share renderer processes. It's only enabled on devices with enough memory (at least 2 GB of RAM in recent versions). So on Android, the protection is strongest for sites that hold sensitive data.

## 364: Can two different origins of the same site share a process, and why does it matter?

Yes. Site Isolation works at the site level, so `a.example.com` and `b.example.com` can share a process by default. Same-site origins can share cookies in some cases and used to use `document.domain` to script each other, so Chrome kept them together.

That means a compromised renderer of one subdomain could try to attack another subdomain in the same process. Sites can ask for origin-level isolation with `Origin-Agent-Cluster: ?1` or cross-origin isolation headers, and Chrome is moving toward origin-keyed agent clusters by default.

## 365: Where does Chrome enforce CSP, CORS and cookie rules: in the renderer or outside it?

Some checks happen in the renderer for speed and correct behavior, but the important ones are done (or repeated) in trusted processes:

- **CORS** is enforced in the network service.
- **Cookies** are attached in the network service, based on the request's origin, which comes from the browser-provided URLLoaderFactory, not from the renderer.
- **CSP for navigations** like `frame-ancestors` is checked in the browser process.
- **ORB** runs in the network service.

So even if a compromised renderer skips its own checks, it can't read other sites' cookies or CORS-protected data.

## 366: How does the browser process limit which Mojo interfaces a renderer can use?

Each renderer frame gets a `BrowserInterfaceBroker`, which only hands out interfaces that are allowed for that frame. Interface implementations in the browser are bound with the frame's context (like its origin and process), so they know who is calling and can check permissions.

Interfaces that only certain processes should use, for example interfaces for extensions or WebUI pages, aren't exposed to normal renderers at all. If a renderer sends a bad message on an interface, the browser can call `ReportBadMessage` and kill the renderer.

## 367: Why is the GPU process sandbox weaker than the renderer sandbox?

The GPU process has to talk to the graphics driver, which needs access to device files, driver libraries and more system calls than a renderer. On some platforms drivers also load extra code. So the GPU process can't be locked down as tightly.

That makes the GPU process an interesting target for sandbox escapes: attackers in a renderer can send crafted GPU commands. Chrome validates commands in the command buffer, and WebGPU validation in Dawn exists for the same reason.

## 368: What is the difference between V8 jitless mode and turning off the optimizer?

- **Jitless mode** (`--jitless`) disables generating any executable code at runtime. Everything runs in the Ignition interpreter, and Wasm doesn't work. It's used where executable memory isn't allowed, like some iOS contexts.
- **Turning off the optimizer** (Chrome's "V8 optimizer" setting per site) disables the optimizing JIT tiers, which carry most of the JIT security risk, but keeps the interpreter and may keep simpler tiers, and Wasm still works with reduced performance.

Both trade speed for a smaller attack surface.

## 369: What is pointer compression in V8?

On 64-bit systems, V8 stores pointers inside the heap as 32-bit offsets from a base address instead of full 64-bit addresses. Small integers (Smis) are also stored in 32 bits.

This cut V8 heap memory by up to around 40%, and made things like GC faster because there's less memory to scan. The trade-off is a heap size limit of 4 GB per pointer cage. It also lays the groundwork for the V8 sandbox.

## 370: What is a Smi?

A Smi (small integer) is how V8 stores small integers directly inside a tagged value, without allocating an object on the heap. The lowest bit of the value tells V8 whether it's a Smi or a pointer to a heap object.

With pointer compression, Smis are 31-bit signed integers. Numbers outside that range, or with fractions, are stored as heap numbers (boxed doubles) unless the compiler can keep them unboxed. Integer-only hot loops benefit from staying in the Smi range.

## 371: What are elements kinds in V8?

V8 tracks what kind of values an array holds, called its elements kind, for example `PACKED_SMI_ELEMENTS`, `PACKED_DOUBLE_ELEMENTS`, `PACKED_ELEMENTS` (any value), and `HOLEY_*` variants when the array has holes.

```js
const a = [1, 2, 3]; // PACKED_SMI_ELEMENTS
a.push(4.5); // PACKED_DOUBLE_ELEMENTS
a.push("x"); // PACKED_ELEMENTS
a[10] = 1; // HOLEY_ELEMENTS
```

Transitions only go toward more general kinds and never back. More specific kinds allow faster code, so avoid creating holes and mixing types in hot arrays.

## 372: What is dictionary mode for objects?

Normally objects use hidden classes with fast property access. If you add many properties dynamically, or `delete` properties, V8 may switch the object to dictionary mode, where properties are stored in a hash table.

```js
const obj = { a: 1, b: 2, c: 3 };
delete obj.a; // obj likely goes into dictionary mode
```

Dictionary mode is slower to read but faster to change. For objects used as maps with arbitrary keys, a `Map` is usually the better choice.

## 373: How does V8 represent strings internally?

V8 has several string representations: sequential strings (one or two bytes per character), cons strings (ropes: a pair of strings created by concatenation, flattened later), sliced strings (a view into a parent string), external strings (data owned by the embedder, like source code from Blink) and internalized strings (deduplicated, used for property names).

So `a + b` is cheap because it creates a rope, but a sliced string can keep a very large parent string alive in memory, which can surprise you in heap snapshots.

## 374: What is a write barrier in V8's GC?

A write barrier is a small piece of code that runs when a pointer is written into an object. It's needed for two reasons:

- **Generational GC**: if an old-generation object starts pointing to a young object, the GC must remember that, so the young object isn't freed during a scavenge.
- **Concurrent/incremental marking**: if JavaScript changes pointers while the GC is marking, the barrier tells the marker about the new reference so it isn't missed.

It's a cost on every pointer store, which the compiler tries to remove when it can prove it's not needed.

## 375: How does concurrent marking work?

During a major GC, V8 must find all live objects. Instead of stopping JavaScript for the whole mark phase, helper threads mark objects concurrently while the main thread keeps running JavaScript. Write barriers record changes made in the meantime.

At the end there's a short pause to finish marking and process remaining work, then sweeping is done concurrently too. Compaction (moving objects to reduce fragmentation) still needs parts of the work to pause the main thread, but it's done in parallel on several threads.

## 376: What is idle-time garbage collection?

Chrome tells V8 when the main thread is idle, for example when a frame finished early and there's time before the next one. V8 uses that time for GC work like incremental marking or scavenges, so the work doesn't happen in the middle of an animation or input handling.

That's one reason pages that keep the main thread busy all the time can have more noticeable GC pauses.

## 377: How does V8 compile WebAssembly?

V8 has two Wasm tiers:

- **Liftoff**: a fast baseline compiler that generates code in one pass, so the module can start running quickly.
- **TurboFan** (with the Turboshaft backend): the optimizing compiler.

With dynamic tiering, V8 compiles everything with Liftoff at first and only optimizes functions that turn out to be hot. Compilation can happen while the module is still downloading (`WebAssembly.compileStreaming` / `instantiateStreaming`), and results are cached.

```js
const { instance } = await WebAssembly.instantiateStreaming(
  fetch("/app.wasm"),
  imports,
);
```

## 378: What is WasmGC and why does it matter?

WasmGC adds garbage-collected structs and arrays to WebAssembly, managed by the browser's GC instead of by code shipped inside the Wasm module. Chrome shipped it in Chrome 119.

Languages with GC, like Kotlin, Dart, Java and OCaml, can now compile to Wasm without bringing their own garbage collector, which makes binaries smaller and allows proper GC across JavaScript and Wasm objects. Google Sheets used it to move its calculation engine to Wasm.

## 379: What is JSPI?

JSPI (JavaScript Promise Integration) lets WebAssembly code that was written in a synchronous style call asynchronous JavaScript APIs. When the Wasm code calls a JS function that returns a promise, JSPI suspends the Wasm stack and resumes it when the promise resolves.

This matters for porting C or C++ code that expects blocking calls (like file reads) to the web, without rewriting it with callbacks or using a costly transform like Asyncify.

## 380: What are compile hints in V8?

Compile hints let developers tell V8 which code is needed at startup, so V8 can compile it eagerly on a background thread instead of lazily on the main thread when it's first called.

Chrome supports a magic comment that marks a whole file for eager compilation:

```js
//# allFunctionsCalledOnLoad
```

Use it only for a small core file whose functions really are called during load. Eagerly compiling too much wastes time and memory.

## 381: How does the network service organize requests per profile?

Each profile (and things like Incognito, isolated apps or extensions with special storage) has its own `NetworkContext`. A NetworkContext owns the cookie store, HTTP cache, socket pools, proxy settings, HSTS state and so on.

So two profiles never share cookies or cached responses, and closing an Incognito window destroys its NetworkContext with all its state. Renderers get URLLoaderFactories created from the right NetworkContext.

## 382: How does the HTTP cache key work in Chrome today?

The key is no longer just the URL. Chrome uses the top-level site, the frame's site (in some cases a "is cross-site" bit instead), and the resource URL. Requests from opaque origins or with certain settings aren't cached at all.

A subtle effect: the same resource requested from a top-level page and from a cross-site iframe on that page may be cached separately.

## 383: How does Chrome delay low-priority requests while the page loads?

Chrome's resource loading scheduler holds back some low-priority requests (like images below the fold or async scripts) during the early "tight mode" phase of a page load, so high-priority resources (CSS, fonts, blocking scripts, the LCP image) get the bandwidth first.

On HTTP/2 and HTTP/3, Chrome also sends priority information to the server (using the Extensible Priorities scheme, the `priority` header or frames) so the server can send important responses first. How well this works depends on the server and CDN.

## 384: What is post-quantum key exchange in Chrome's TLS?

Chrome uses a hybrid key exchange for TLS 1.3 and QUIC that combines classic X25519 with ML-KEM (formerly Kyber), a post-quantum algorithm. Chrome switched to the standardized ML-KEM version in Chrome 131.

The idea is to protect today's traffic from "harvest now, decrypt later" attacks, where someone records encrypted traffic and decrypts it in the future with a quantum computer. The downside is larger handshake messages, which broke a few old middleboxes.

## 385: What is Certificate Transparency and how does Chrome enforce it?

Certificate Transparency (CT) means every publicly trusted TLS certificate must be logged in public, append-only logs. Anyone can watch the logs and spot certificates issued for their domains by mistake or by an attacker.

Chrome requires a certificate to come with Signed Certificate Timestamps (SCTs) from enough approved logs. If they're missing, Chrome treats the certificate as invalid with `NET::ERR_CERTIFICATE_TRANSPARENCY_REQUIRED`.

## 386: How does QUIC 0-RTT work and what are its risks?

If the browser connected to a server before, it can reuse cached keys to send the first HTTP request inside the very first packet, without waiting for the handshake. This saves a full round trip.

The risk is replay: an attacker can capture and resend 0-RTT data. So 0-RTT should only be used for idempotent requests like `GET`. Chrome only sends safe requests in 0-RTT, and servers should reject or handle replays for anything that changes state.

## 387: What is the simple cache backend?

The simple cache is Chrome's HTTP disk cache implementation on most platforms. It stores each entry in its own file (or small set of files), with an index kept in memory, instead of one big database file.

This design is simpler and holds up better against crashes and corruption, since one bad entry doesn't break the whole cache. The trade-off is many small files on disk.

## 388: What is "connection-level" privacy in Chrome, like network state partitioning?

Besides the HTTP cache, Chrome partitions other network state by top-level site: socket pools, DNS cache entries, TLS session tickets, HTTP/2 and QUIC sessions and Alt-Svc info. This is called network state partitioning.

Without it, a tracker embedded on two sites could tell they're the same user by checking whether a connection or TLS session is reused. The cost is fewer reused connections, so a third-party resource on a new site needs a fresh connection.

## 389: How does Chrome decide whether to show a TLS interstitial or a connection error?

If the TLS handshake works but the certificate fails verification (wrong name, expired, untrusted CA, missing CT), Chrome shows a full-page warning (interstitial) that sometimes lets the user proceed. If the site uses HSTS, there's no "proceed" button.

If the connection fails at the network or protocol level (DNS failure, refused connection, TLS protocol error), Chrome shows an error page like `ERR_NAME_NOT_RESOLVED` or `ERR_SSL_PROTOCOL_ERROR`, with no option to continue.

## 390: How does Chrome handle a renderer that tries to navigate to a URL it isn't allowed to?

Renderer-initiated navigations are requests the browser process checks. For example, a normal web page can't navigate to `file://` URLs or to `chrome://` pages, and can't navigate the top frame from a cross-origin iframe without user activation (unless sandbox rules allow it).

If the renderer asks for something its site lock or permissions don't allow, the browser blocks the navigation, and for clearly invalid requests, it kills the renderer as compromised.

## 391: What is the browser-side CSP for frame embedding?

`Content-Security-Policy: frame-ancestors` and the older `X-Frame-Options` header tell Chrome which parent pages may embed a document in a frame. They protect against clickjacking.

Chrome checks them in the browser process when the response for the frame arrives, before the document commits. If not allowed, the frame shows an error page and the content never reaches the embedding page's process.

```http
Content-Security-Policy: frame-ancestors 'self' https://partner.example.com
```

## 392: How does Chrome isolate extensions from web pages and from each other?

Each extension has its own origin (`chrome-extension://<id>`) and its pages run in their own process, separate from web content. Content scripts run in the web page's renderer, but in an isolated world, and Chrome treats messages from content scripts as less trusted than messages from the extension's own pages.

Extension APIs are only given to processes that host that extension. Permissions in the manifest and host permissions limit which sites an extension can touch.

## 393: What is Origin-Agent-Cluster?

`Origin-Agent-Cluster: ?1` is a response header that asks Chrome to put the page in an agent cluster keyed by its origin instead of its site. Then `document.domain` stops working for it, and Chrome can put it in its own process separate from other same-site origins.

Chrome has been moving toward origin-keyed agent clusters by default, so `document.domain` setting is ignored unless a site opts out with `Origin-Agent-Cluster: ?0`.

## 394: Why can't a page read pixels from a cross-origin image drawn on a canvas?

If you draw a cross-origin image without CORS approval on a canvas, the canvas becomes "tainted." After that, `getImageData()`, `toDataURL()` and `toBlob()` throw a security error.

Without this, a page could load a private image (like a profile picture on another site that uses your cookies) and read its pixels. To read pixels legally, load the image with `crossorigin` and have the server send CORS headers.

```html
<img src="https://cdn.example.com/photo.jpg" crossorigin="anonymous" />
```

## 395: What timing attacks do browsers still need to defend against?

Even with Site Isolation, pages can learn things about other sites through side channels: cache timing (fixed by cache partitioning), how long a cross-site response takes, frame counting via `window.length`, error events on resources, `:visited` link color, and more. These are called XS-Leaks.

Defenses include partitioning, Fetch Metadata checks on the server, `SameSite` cookies, COOP, and Chrome restricting what `:visited` styles can be read. Sites with sensitive data should use these headers.

## 396: How does Chrome stop pages from reading which links you visited?

`:visited` styles are limited to a few properties like `color` and `background-color`, and `getComputedStyle()` returns the unvisited values. Chrome also limits other ways to detect it.

In newer versions, Chrome partitions `:visited` history: a link is only shown as visited if you clicked it from the same top-level site (and frame origin). This blocks a whole class of history-sniffing attacks.

## 397: What is a "renderer kill" and when does Chrome do it on purpose?

When the browser process detects a renderer behaving in a way a correct renderer never would, like sending an invalid Mojo message, asking for data from a site it isn't locked to, or requesting a navigation it can't make, it terminates the renderer. In code this is triggered by `ReportBadMessage` or `bad_message::ReceivedBadMessage`.

From the user's point of view this looks like a crash ("Aw, Snap!"). It's a deliberate fail-safe: better to kill a possibly compromised process than to let it keep going.

## 398: Why are some memory-hungry features restricted to cross-origin isolated pages?

APIs like `SharedArrayBuffer` and high-precision timers make Spectre-style attacks much more practical. Cross-origin isolation (COOP + COEP) guarantees that no cross-origin data that didn't opt in can be loaded into the process, so these attacks have nothing to steal.

`performance.measureUserAgentSpecificMemory()` is also gated, because measuring memory precisely can leak information about other content in the process.

## 399: What is COEP credentialless and why was it added?

`Cross-Origin-Embedder-Policy: require-corp` requires every cross-origin resource to send `Cross-Origin-Resource-Policy` or use CORS, which is hard when you embed third-party resources you don't control.

`credentialless` is an easier option: cross-origin `no-cors` requests are sent without cookies or other credentials, so the response can't contain private user data, and it's allowed without CORP. This made cross-origin isolation possible for many more sites.

## 400: How does Chrome keep secrets in the browser process safe from a compromised renderer?

Sensitive data like saved passwords, cookies of other sites, autofill data and site permissions stays in the browser process or network service. A renderer only gets data for its own site, and only when needed: for example, a saved password is filled into the page only after the browser checks the frame's origin, and often after user interaction.

Cookies marked `HttpOnly` never go to the renderer at all. On Windows and macOS, Chrome encrypts stored passwords and cookies with OS-level keys, and newer versions use app-bound encryption to make it harder for other programs to steal them.

## 401: How does Chrome decide how many renderer processes to create?

On desktop, Chrome calculates a soft process limit from the amount of physical memory. Below the limit, it creates new processes freely. Above it, Chrome tries to reuse existing processes for the same site instead of creating new ones.

Site Isolation is never broken to save memory: cross-site documents always get different processes, even above the limit. So the limit mainly affects how many same-site tabs share a process.

## 402: How does Android decide which Chrome renderer to kill when memory is low?

Chrome tells Android how important each renderer is, using process priority bindings: the visible tab's renderer is foreground, recently used tabs are lower, and background tabs are lowest. When the system is low on memory, Android's low memory killer kills the lowest-priority processes first.

When you return to a killed tab, Chrome reloads it. That's why mobile web apps must save state on `visibilitychange`; the page may be killed without any other event.

## 403: How does the bfcache work internally?

When you navigate away from an eligible page, Chrome doesn't destroy the document. It keeps the RenderFrameHost and the renderer's document alive, freezes all its task queues, and marks it "in bfcache." The navigation to the new page happens normally, often in a new process.

On Back, Chrome finds the cached entry, swaps it back into the frame tree, resumes task queues and fires `pageshow` with `persisted: true`. Cached pages are evicted after a timeout (around 10 minutes), when memory is low, or if they try to do something not allowed while frozen, such as receiving a message that needs a response.

## 404: How does prerendering work internally?

Chrome creates a hidden frame tree (a separate page) in a renderer process and loads the target URL in it, running scripts and rendering as usual, but without showing it. Some APIs are deferred until activation, and things like popups or permission prompts cause the prerender to be cancelled.

When the user navigates to that URL, Chrome "activates" the prerendered page: it swaps it into the tab, fires `prerenderingchange`, and records it as a navigation. Since the page has already loaded and painted, it appears almost instantly.

## 405: What limits does Chrome place on speculation rules?

Chrome caps how many speculations run at once, with different limits per eagerness: for example up to 50 `immediate` or `eager` prefetches and 10 prerenders, and only 2 for `moderate` and `conservative` (oldest ones are dropped first). It also doesn't speculate when Data Saver or Energy Saver is on, when memory is low, or when the user turned off page preloading.

Cross-site prerendering isn't allowed, and cross-site prefetch only works when the user has no cookies for the target site (or through a private prefetch proxy in some cases). These limits protect privacy and resources.

## 406: How would you debug a page that feels slow on scroll?

1. Record a Performance profile while scrolling, with CPU throttling.
2. Check if frames are dropped and what's on the main thread during those frames.
3. Look for scroll or wheel/touch handlers that are non-passive or slow. Turn on "Scrolling performance issues" in the Rendering tab.
4. Check paint flashing: if content repaints during scroll, something isn't composited or there's a `background-attachment: fixed` or a scroll-linked style change.
5. Check the Layers panel for huge layers or too many layers.
6. Look for JavaScript that updates styles on scroll; replace it with `position: sticky`, IntersectionObserver or scroll-driven animations.

## 407: How would you investigate a high INP reported from real users?

1. Use the `web-vitals` attribution build or the LoAF API to collect which interaction, which element, and which part (input delay, processing, presentation) was slow.
2. Group by page and element to find the worst interactions.
3. Reproduce in DevTools with CPU throttling and record a profile while doing that interaction.
4. If input delay is high, find what long tasks were running (third-party scripts, hydration, timers).
5. If processing is high, optimize the handler, show visual feedback first and defer the rest with `scheduler.yield()`.
6. If presentation delay is high, reduce DOM size, style recalc and layout work after the interaction.

## 408: A page's memory keeps growing in a long-running SPA. How do you approach it?

1. Use the Performance panel with the memory checkbox to confirm that JS heap, DOM nodes and listeners grow steadily across repeated actions, even after forcing GC (the trash can icon).
2. Take heap snapshots before and after repeating an action several times and compare.
3. Look for detached DOM trees, growing arrays/Maps, listeners and closures.
4. Follow the retainer chain to your code: a global store, a cache without limits, an event bus subscription, a timer.
5. Fix by cleaning up on unmount (remove listeners, abort fetches with `AbortController`, clear intervals, disconnect observers) and by limiting cache sizes.

## 409: Why might a site be fast in Lighthouse but slow for real users?

- Lighthouse runs one cold load on a simulated device and network; real users have very different devices, many much slower.
- Real users interact; Lighthouse mostly measures the load, so INP problems don't show.
- Third-party scripts, A/B tests, ads and consent banners may behave differently in tests.
- Logged-in pages, personalized content and long sessions aren't covered.
- Users come back via bfcache or with warm caches, or arrive via slow redirects from ads.

Use field data (CrUX, RUM) to find real problems, and lab tools to debug them.

## 410: How would you diagnose a slow TTFB?

Break it down:

1. **Redirects**: check the navigation timing for redirect time (common with ad links and `http` to `https` redirects).
2. **Service Worker startup**: if a SW controls the page, check its startup and fetch handler time; use navigation preload.
3. **DNS, TCP, TLS**: check connection setup; consider a CDN closer to users and HTTP/3.
4. **Server time**: use `Server-Timing` headers to show backend phases in DevTools.

```http
Server-Timing: db;dur=53, render;dur=47, cache;desc="miss"
```

Then fix the biggest part: caching HTML at the edge, faster queries, streaming the response early, or `103 Early Hints`.

## 411: How does streaming HTML help performance?

Chrome parses HTML as it arrives. If the server sends the `<head>` with CSS and preload links right away, and the rest later as it's ready, the browser can start downloading resources and even paint the top of the page before the server finishes.

Frameworks like React (with `renderToPipeableStream` / `renderToReadableStream`), Next.js and Remix stream HTML. Buffering the whole response before sending it, for example in a proxy, removes this benefit.

## 412: Why do third-party scripts hurt performance so much?

- They compete for the main thread, causing long tasks and bad INP.
- They need new DNS, TCP and TLS connections to other origins, and with cache partitioning they aren't shared across sites.
- They can inject more scripts, iframes and layout shifts.
- You don't control their size or updates.

Load them with `async` or `defer`, lazy load ones that aren't needed right away (like chat widgets), use facades for heavy embeds like videos, and move some of them into a worker with tools like Partytown where possible.

## 413: How does hydration affect the browser's main thread?

With server-side rendering, the HTML appears quickly, but the page isn't interactive until the framework's JavaScript downloads, parses and runs "hydration": it walks the DOM, attaches event listeners and builds component state. On large pages this is one long task or several, which hurts INP and makes early clicks feel ignored.

Techniques like streaming SSR, selective or progressive hydration, islands (only hydrating interactive parts), React Server Components, and Angular's incremental hydration reduce this main-thread work.

## 414: Why does Chrome sometimes show a white screen instead of the old page during navigation?

When you navigate, Chrome keeps showing the old page until the new one has something worth painting. This is called "paint holding." For same-origin navigations it waits until the new page reaches first contentful paint or a timeout, to avoid a flash of white.

If the new page takes too long, or for some cross-origin cases, the old content is dropped and you may briefly see a blank page. A fast first paint on the new page is the real fix.

## 415: How would you make a heavy data grid with 100,000 rows render fast?

- Use virtualization: only render the rows in or near the viewport and reuse DOM nodes as the user scrolls.
- Keep row height fixed or predictable so you can calculate positions without layout.
- Use `transform: translateY()` for row positioning so it can be done without layout.
- Do sorting and filtering in a Web Worker for large data.
- Use `contain: strict` or `content-visibility` for cells or sections to limit layout scope.
- Avoid reading layout in scroll handlers; use rAF and cached measurements.

## 416: How would you implement a smooth animated drawer that stays smooth during heavy JavaScript?

Use a compositor-only animation: animate `transform` (and maybe `opacity`) with CSS transitions or the Web Animations API, not `left` or `width`.

```css
.drawer {
  transform: translateX(-100%);
  transition: transform 250ms ease-out;
}
.drawer.open {
  transform: translateX(0);
}
```

Start the animation before doing other work, and break heavy work into chunks with `scheduler.yield()`. Since the compositor runs the transform animation, it keeps going even if the main thread is busy for a while.

## 417: Why might `position: fixed` elements jump on mobile Chrome?

On mobile Chrome, the URL bar hides and shows as you scroll, which changes the visual viewport height. Elements sized with `100vh` use the largest viewport (as if the URL bar is hidden), so they can be cut off or jump when the bar appears.

Use the new viewport units: `svh` (small viewport), `lvh` (large) and `dvh` (dynamic, follows the current size). For bottom-fixed elements, also consider the `interactive-widget` setting in the viewport meta tag and the Visual Viewport API when the keyboard opens.

## 418: How does Chrome handle the on-screen keyboard on Android for layout?

By default, when the keyboard opens, Chrome resizes the visual viewport but not the layout viewport, so the page doesn't reflow, it just becomes scrollable over a smaller visible area. You can change this with the viewport meta tag:

```html
<meta
  name="viewport"
  content="width=device-width, initial-scale=1, interactive-widget=resizes-content"
/>
```

`resizes-content` shrinks the layout viewport (like older behavior), and `overlays-content` doesn't resize anything. The VirtualKeyboard API gives more control in Chrome.

## 419: What would you check if a page is never restored from bfcache?

1. Run the test in DevTools > Application > Back/forward cache to see the blocking reasons.
2. Collect `notRestoredReasons` from real users to see what happens in the field:

```js
const [nav] = performance.getEntriesByType("navigation");
if (nav.notRestoredReasons) console.log(nav.notRestoredReasons);
```

3. Remove `unload` handlers (including from third-party scripts), close WebSockets and IndexedDB connections in `pagehide`, and reopen them in `pageshow`.
4. Check `Cache-Control: no-store` on HTML and whether it's really needed.
5. Check whether the page was opened with `window.open` and has an opener.

## 420: Why are cross-origin iframes expensive, and how would you reduce their cost?

Each cross-site iframe needs its own renderer process on desktop (memory overhead, process start time), separate network connections, and its own JavaScript and rendering work. Ads, embeds and widgets add up fast.

Reduce the cost by lazy loading iframes (`loading="lazy"`), using facades (a static preview that loads the real embed on click), removing unneeded embeds, and setting `sandbox` and `allow` attributes to limit what they can do.

## 421: Why did Google fork WebKit to create Blink?

Chrome's multi-process architecture was very different from the WebKit project's own multi-process model (WebKit2). Supporting both in one codebase added complexity, and much of WebKit's code existed for ports Chrome didn't use.

Forking let the Chromium team remove a large amount of code, change architecture freely (for example for Site Isolation, the new compositor and LayoutNG) and move faster. The fork happened in 2013, and since then the engines have diverged a lot.

## 422: What are the trade-offs of Chrome's multi-process architecture?

**Benefits**: crash isolation, strong security boundaries with sandboxing and Site Isolation, parallelism across CPU cores, and a responsive UI even when a page hangs.

**Costs**: more memory (each process has its own copies of some data and overhead), the cost of IPC (latency and serialization), more complexity in code that must be split across processes, and process startup time.

Chrome reduces the costs with process reuse, spare processes, consolidating services on low-memory devices and sharing read-only data across processes.

## 423: Why does Chrome run the network stack in a separate process?

Historically the network code ran in the browser process. Moving it to its own utility process (the network service) means:

- A crash in the network stack doesn't take down the whole browser; Chrome restarts the service.
- The network code, which parses data from the internet (HTTP, QUIC, certificates), can be sandboxed more tightly.
- It gives a clean Mojo API, which made features like cookie and CORS enforcement in one trusted place simpler.

On low-memory Android devices it may still run in the browser process to save memory.

## 424: What is the Chrome Servicification project?

Servicification was the effort to split Chrome into separate services with clean Mojo interfaces, like the network service, storage service, device service, audio service and Viz. Before that, many features were deeply tangled inside the browser process.

With services, Chrome can run them in different processes depending on the platform and memory, sandbox them separately, restart them after crashes and reuse them in other products like ChromeOS.

## 425: How does Chrome share read-only data across processes to save memory?

Several techniques:

- **V8 snapshots**: the initial heap with built-in JavaScript objects is loaded from a snapshot that can be memory-mapped and shared.
- **Shared libraries and resource files**: code and resources like fonts and ICU data are memory-mapped, so the OS shares physical pages between processes.
- **Zygote** on Linux and Android: new processes are forked from a pre-initialized process, sharing pages copy-on-write.
- **Shared memory regions** for things like font data and cookie lists sent to renderers.

## 426: How would you explain the difference between the main thread, the compositor thread and the GPU process in one sentence each?

- **Main thread**: runs JavaScript and produces the content of the page (DOM, style, layout, paint records).
- **Compositor thread**: takes that content, splits it into layers and tiles, handles scrolling and compositor animations, and builds frames, without running JavaScript.
- **GPU process**: rasterizes tiles into textures, combines frames from all processes in Viz, and draws the final picture on screen.

## 427: A CSS animation is smooth on desktop but janky on a low-end Android phone. What do you check?

1. Is it animating compositor-friendly properties (`transform`, `opacity`)? If not, each frame needs layout or paint, which a slow CPU can't do in time.
2. Is the element on its own layer, and is the layer huge? Large layers on a high-DPR screen cost a lot of GPU memory and raster time.
3. Are there many layers or expensive effects (big blurs, shadows) being redrawn?
4. Is the main thread busy at the same time (hydration, third-party scripts)? Compositor animations survive this, main-thread ones don't.
5. Check `chrome://gpu` on the device through remote debugging to see if GPU raster is enabled.

## 428: Why is `box-shadow` or `filter: blur()` animation slow, and what is a better approach?

Animating `box-shadow` changes what is painted, so each frame needs paint and raster of the shadow area, and big blurs are expensive to raster. `filter: blur()` with a changing radius also costs a lot of GPU work.

A better approach is to put the final shadow on a pseudo-element and animate its `opacity`:

```css
.card {
  position: relative;
}
.card::after {
  content: "";
  position: absolute;
  inset: 0;
  box-shadow: 0 10px 30px rgb(0 0 0 / 0.3);
  opacity: 0;
  transition: opacity 200ms;
}
.card:hover::after {
  opacity: 1;
}
```

## 429: How does Chrome handle very long JavaScript tasks inside iframes from other sites?

Since a cross-site iframe runs in its own renderer process, its long tasks run on that process's main thread, not the parent's. The parent page stays responsive and can keep scrolling and handling input.

Same-site iframes, though, share the parent's process and main thread, so their long tasks block the parent too. This is one practical benefit of Site Isolation besides security.

## 430: What happens if two same-origin tabs share a renderer process and one runs an infinite loop?

They share the same main thread (in the same agent cluster), so the second tab also freezes. Chrome may show the "Page Unresponsive" dialog. Killing the process closes both, and both show "Aw, Snap!"

Chrome tries to avoid putting unrelated tabs of the same site in one process when it has room, but tabs connected through `window.opener` must share. Using `noopener` and COOP for links that open new tabs avoids this.

## 431: Why does Chrome sometimes keep a process alive after you close a tab?

Some reasons: another tab or frame from the same site still uses it, the page has a pending `unload` or a keepalive request (like `fetch(..., { keepalive: true })` or `sendBeacon`) that needs to finish, or a Service Worker or SharedWorker hosted in that process is still running.

Chrome also keeps a spare renderer around for future navigations. Process lifetime is controlled by reference counts of things that need it.

## 432: What is keepalive in fetch and why does it matter for unload?

A normal `fetch` started while a page is being closed may be cancelled. With `keepalive: true`, the request is allowed to finish even after the page is gone, as long as the body is small (limit 64 KB across keepalive requests).

```js
document.addEventListener("visibilitychange", () => {
  if (document.visibilityState === "hidden") {
    fetch("/log", {
      method: "POST",
      body: JSON.stringify(data),
      keepalive: true,
    });
  }
});
```

`navigator.sendBeacon()` works the same way. Chrome also has `fetchLater()`, which queues a request that the browser sends when the page is closed or after a timeout, so you don't have to guess when the page will go away.

## 433: How does Chrome isolate Service Workers in terms of processes?

A Service Worker runs in a renderer process that is locked to its site, like a page from that site. Chrome tries to start it in a process that already hosts the same site to save time, or in a new process. With storage partitioning, third-party Service Workers are keyed by top-level site, so one site's worker can't serve another top-level site.

Because Service Workers run without a page, Chrome limits their lifetime: they're stopped after about 30 seconds idle, and an event handler can't run for more than about 5 minutes.

## 434: How does Chrome reduce Service Worker startup cost?

Starting a SW means starting (or finding) a process, starting a worker thread, loading and running the script. Chrome reduces this with:

- Starting the worker early when it sees a likely navigation (for example on link hover or when typing in the Omnibox).
- Caching the compiled script code on install.
- Navigation preload, so the network request runs in parallel.
- The Static Routing API, so some requests skip the worker entirely.
- Skipping the worker when its fetch handler is empty (Chrome detects no-op fetch handlers).

## 435: What role does Chrome play in web standards, and why does that matter in interviews?

Chrome has a large market share and Google employs many engineers working on specs at W3C, WHATWG and IETF. Many APIs ship in Chrome first (sometimes years before other browsers), like WebGPU, View Transitions and Speculation Rules.

For developers this means a feature working in Chrome doesn't mean it works in Safari or Firefox. Check Baseline status (on MDN or web.dev) and use feature detection and progressive enhancement. Interviewers ask this to see if you understand that "Chrome" and "the web platform" are not the same thing.

## 436: How do you check if a feature is safe to use across browsers?

- Check MDN and "Baseline" status: "Newly available" means supported in all major browsers, "Widely available" means for 30 months or more.
- Use caniuse.com for details per version.
- Check chromestatus.com for Chrome's status and other browsers' positions.
- Use feature detection in code:

```js
if ("startViewTransition" in document) {
  document.startViewTransition(update);
} else {
  update();
}
```

```css
@supports (container-type: inline-size) {
  /* ... */
}
```

## 437: How would you design a page to load fast on a slow 3G connection in Chrome?

- Keep the HTML small and stream it; inline the critical CSS for the first screen.
- Avoid render-blocking JavaScript; use `defer` and code splitting.
- Use one origin where you can, to avoid extra connection setup; `preconnect` to required third parties.
- Compress text (Brotli or zstd) and serve images in AVIF or WebP at the right size with `srcset`.
- Preload the LCP image and critical font; lazy load the rest.
- Cache static files for a long time with hashed names, and add a Service Worker for repeat visits.
- Respect `Save-Data` to send lighter content.

## 438: Why might `setTimeout` callbacks in a background tab fire much later than expected, and how do you design around it?

Chrome throttles timers in hidden tabs (about once per second), applies intensive throttling after 5 minutes (once per minute for chained timers), and may freeze or discard the tab completely.

Don't rely on timers for timing-sensitive work in the background. Instead:

- Recalculate based on `Date.now()` when the tab becomes visible again.
- Use server push (WebSocket, Web Push) for updates, which aren't throttled the same way.
- Use the Notifications API or a Service Worker for reminders.
- Save state on `visibilitychange` so a discard doesn't lose data.

## 439: How does the browser decide to show a page as "not secure" in the address bar?

Chrome shows "Not secure" for pages loaded over plain HTTP. HTTPS pages show a neutral "tune" icon (Chrome replaced the lock icon in 2023, since HTTPS is now the normal case). If an HTTPS page has certificate errors that the user clicked through, it shows a red "Not secure" warning.

Mixed content that Chrome can't block or upgrade, or forms that submit to HTTP, also make Chrome warn the user.

## 440: How would you explain what happens between pressing a key in an input field and the character appearing on screen?

1. The OS sends the key event to the browser process.
2. The browser routes it to the focused frame's renderer; the compositor forwards it to the main thread because text input needs Blink.
3. Blink fires `keydown`, then `beforeinput`, inserts the character into the DOM (or the input's value), then fires `input` and `keyup`.
4. The change marks style and layout dirty; the next frame runs style, layout and paint for the input's text.
5. The compositor commits, raster updates the affected tile, Viz draws the frame.

If a long task is running in step 2, the character appears late, which is what INP measures.

## 441: What is the difference between how Chrome handles `<script type="module">` imports and a bundled script?

With native modules, Chrome downloads the entry module, parses it to find `import` statements, then downloads those, and so on. Deep import trees cause request waterfalls. Each module is a separate request and cache entry, though HTTP/2 or HTTP/3 makes many requests cheaper.

A bundled script is one or a few files, so there are fewer round trips and better compression. Bundlers with code splitting and `modulepreload` give a good middle ground: a few chunks, loaded in parallel.

## 442: How does Chrome handle import maps?

Import maps let you control how bare module specifiers like `import 'lodash'` resolve to URLs, without a bundler.

```html
<script type="importmap">
  {
    "imports": {
      "lodash": "/vendor/lodash-es/lodash.js",
      "app/": "/src/app/"
    }
  }
</script>
<script type="module">
  import { debounce } from "lodash";
</script>
```

Chrome reads the map before resolving module imports. Newer versions allow multiple import maps that are merged, and `integrity` metadata for modules.

## 443: Why is reading `localStorage` on page load a performance concern?

`localStorage` is synchronous. The first access in a renderer may need to load the origin's data from the storage service, and the main thread waits. Large values or many keys make it worse, and every `setItem` sends data across processes.

For small settings it's fine. For larger data, use IndexedDB (asynchronous) or keep data in memory and write to storage less often.

## 444: How does Chrome decide when to fire the `load` event on a page with lazy-loaded images?

Lazy-loaded images that are not near the viewport aren't fetched, so they don't delay `load`. Images that start loading (because they're near the viewport) do delay it.

This is one reason why native lazy loading makes the `load` event fire earlier. If an image near the top is lazy, it's still loaded, but it's discovered later (after layout), which can hurt LCP.

## 445: What would you look for in a trace if users report the page "freezes for a second" after login?

- A long task after the login response: often big JSON parsing, rendering a large initial state, or hydration of a heavy dashboard.
- Many synchronous `localStorage` writes or large `structuredClone` / `postMessage` copies.
- Forced synchronous layouts while building the UI.
- Garbage collection spikes from allocating lots of objects.
- Many third-party scripts that start running once the user is "known" (analytics, chat widgets).

Fixes: split work with `scheduler.yield()`, render above-the-fold first, move parsing to a worker, defer non-critical scripts.

## 446: How does structured cloning affect performance with workers?

`postMessage` copies data using the structured clone algorithm: it walks the object graph, serializes it on one thread and deserializes on the other. For big objects this takes time on both main and worker threads, and doubles memory for a moment.

For large binary data, transfer it instead of copying:

```js
const buffer = new ArrayBuffer(50_000_000);
worker.postMessage(buffer, [buffer]); // moved, not copied; buffer is now empty here
```

`SharedArrayBuffer` avoids copying entirely but requires cross-origin isolation and careful synchronization.

## 447: How does Chrome decide whether a page is "installable" as a PWA, and what changed recently?

In the past, Chrome required a web app manifest with name, icons and `start_url`, served over HTTPS, and a Service Worker with a fetch handler. Chrome dropped the Service Worker requirement, and now lets users install any site from the menu, with a manifest improving the result (icons, name, display mode).

When the page meets the criteria, Chrome fires `beforeinstallprompt`, which you can use to show your own install button.

## 448: What happens in Chrome when you zoom a page with Ctrl/Cmd and +?

Browser zoom changes the device scale factor used by the page: CSS pixels become larger, so `window.devicePixelRatio` changes and the layout viewport gets narrower in CSS pixels. The page is laid out again, which can trigger media queries and responsive layouts. Zoom is remembered per site.

Pinch-zoom on touch devices is different: it scales the visual viewport without changing layout, handled mostly on the compositor, so it's smooth and doesn't reflow the page.

## 449: Why might `devicePixelRatio`-based canvas code look blurry or use too much memory?

For a sharp canvas you size its backing store to CSS size times `devicePixelRatio` and scale the context:

```js
const dpr = window.devicePixelRatio;
canvas.width = canvas.clientWidth * dpr;
canvas.height = canvas.clientHeight * dpr;
ctx.scale(dpr, dpr);
```

If you forget this, the canvas is upscaled and looks blurry on high-DPI screens. If you do it on a large canvas on a 3x screen, memory grows 9x, which can hit GPU limits. DPR can change with zoom or moving the window to another screen, so listen for changes with a `matchMedia()` query on the current `resolution` and resize the canvas when it fires.

## 450: If you had to explain how Chrome works in two minutes in an interview, what would you say?

Chrome is a multi-process browser. The browser process runs the UI and coordinates everything; renderer processes, one per site, run Blink and V8 inside a sandbox; the GPU process draws pixels; the network service handles all traffic.

When you navigate, the browser process fetches the response through the network service, picks a renderer for the site and commits the page. The renderer parses HTML into the DOM, combines it with CSS to compute styles, runs layout to get geometry, and paints into display lists. The compositor thread splits them into layers and tiles, the GPU process rasterizes them, and Viz combines frames from all processes and puts them on screen, about 60 times a second.

JavaScript runs on the main thread through V8's tiers (Ignition, Sparkplug, Maglev, TurboFan) with a generational garbage collector. Security comes from layers: the sandbox, Site Isolation, and the rule that the browser never trusts a renderer.
