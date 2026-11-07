# Debugging Interview Questions and Answers

_Last updated: November 6, 2026_

450 front-end debugging interview questions with answers, split into three levels: 150 easy, 150 moderate and 150 advanced.

The answers are written for current tools as of late 2026: Chrome DevTools (with notes on Firefox and Safari where they differ), React 19, Angular 21, Next.js 16, Vite, webpack 5, Vitest, Jest, Playwright and Cypress. They cover how to find bugs in the browser, in frameworks, in builds, in tests and in production. Tools change often, so some menu names may be a bit different in your version.

## Table of Contents

- [Easy Questions (1-150)](#easy-questions-1-150)
- [Moderate Questions (151-300)](#moderate-questions-151-300)
- [Advanced Questions (301-450)](#advanced-questions-301-450)

### Easy Questions (1-150)

- [1: What is debugging?](#1-what-is-debugging)
- [2: What steps do you follow when you debug a problem?](#2-what-steps-do-you-follow-when-you-debug-a-problem)
- [3: Why is reproducing a bug the first step?](#3-why-is-reproducing-a-bug-the-first-step)
- [4: What is a minimal reproduction?](#4-what-is-a-minimal-reproduction)
- [5: What is a stack trace?](#5-what-is-a-stack-trace)
- [6: How do you read a stack trace?](#6-how-do-you-read-a-stack-trace)
- [7: What is the difference between an error message and a stack trace?](#7-what-is-the-difference-between-an-error-message-and-a-stack-trace)
- [8: What is the console in browser DevTools?](#8-what-is-the-console-in-browser-devtools)
- [9: What console methods do you use besides console.log?](#9-what-console-methods-do-you-use-besides-consolelog)
- [10: How does console.table help with debugging?](#10-how-does-consoletable-help-with-debugging)
- [11: How do you measure how long some code takes with the console?](#11-how-do-you-measure-how-long-some-code-takes-with-the-console)
- [12: What does console.trace do?](#12-what-does-consoletrace-do)
- [13: What does console.assert do?](#13-what-does-consoleassert-do)
- [14: Why can console.log show a different value than the one at the time it was logged?](#14-why-can-consolelog-show-a-different-value-than-the-one-at-the-time-it-was-logged)
- [15: How do you log several variables so it is clear which value is which?](#15-how-do-you-log-several-variables-so-it-is-clear-which-value-is-which)
- [16: What is the $0 variable in the console?](#16-what-is-the-0-variable-in-the-console)
- [17: What are $ and $$ in the DevTools console?](#17-what-are--and--in-the-devtools-console)
- [18: What is a breakpoint?](#18-what-is-a-breakpoint)
- [19: What does the debugger statement do?](#19-what-does-the-debugger-statement-do)
- [20: Why use breakpoints instead of console.log?](#20-why-use-breakpoints-instead-of-consolelog)
- [21: What are the stepping controls in the debugger?](#21-what-are-the-stepping-controls-in-the-debugger)
- [22: What is the difference between step over and step into?](#22-what-is-the-difference-between-step-over-and-step-into)
- [23: What is the Sources panel in Chrome DevTools?](#23-what-is-the-sources-panel-in-chrome-devtools)
- [24: How do you find a file quickly in the Sources panel?](#24-how-do-you-find-a-file-quickly-in-the-sources-panel)
- [25: What is a conditional breakpoint?](#25-what-is-a-conditional-breakpoint)
- [26: What is a logpoint?](#26-what-is-a-logpoint)
- [27: What does the Scope section of the debugger show?](#27-what-does-the-scope-section-of-the-debugger-show)
- [28: What does the Call Stack section of the debugger show?](#28-what-does-the-call-stack-section-of-the-debugger-show)
- [29: What are watch expressions?](#29-what-are-watch-expressions)
- [30: How do you pause on exceptions?](#30-how-do-you-pause-on-exceptions)
- [31: What is a source map?](#31-what-is-a-source-map)
- [32: Why do you need source maps?](#32-why-do-you-need-source-maps)
- [33: What is minification and why does it make debugging harder?](#33-what-is-minification-and-why-does-it-make-debugging-harder)
- [34: What is the Elements panel used for?](#34-what-is-the-elements-panel-used-for)
- [35: What is the difference between the DOM in the Elements panel and View Source?](#35-what-is-the-difference-between-the-dom-in-the-elements-panel-and-view-source)
- [36: How do you inspect an element on the page?](#36-how-do-you-inspect-an-element-on-the-page)
- [37: How do you check which CSS rules apply to an element?](#37-how-do-you-check-which-css-rules-apply-to-an-element)
- [38: What does it mean when a CSS property is crossed out in the Styles pane?](#38-what-does-it-mean-when-a-css-property-is-crossed-out-in-the-styles-pane)
- [39: What is the Computed pane?](#39-what-is-the-computed-pane)
- [40: What is the box model view in DevTools?](#40-what-is-the-box-model-view-in-devtools)
- [41: What is CSS specificity?](#41-what-is-css-specificity)
- [42: How can you see the specificity of a selector in DevTools?](#42-how-can-you-see-the-specificity-of-a-selector-in-devtools)
- [43: How do you force a CSS state like hover or focus in DevTools?](#43-how-do-you-force-a-css-state-like-hover-or-focus-in-devtools)
- [44: What is the Network panel used for?](#44-what-is-the-network-panel-used-for)
- [45: How do you see only API calls in the Network panel?](#45-how-do-you-see-only-api-calls-in-the-network-panel)
- [46: What do HTTP status codes 4xx and 5xx mean?](#46-what-do-http-status-codes-4xx-and-5xx-mean)
- [47: What is the difference between 401 and 403?](#47-what-is-the-difference-between-401-and-403)
- [48: What does a red or failed request in the Network panel mean?](#48-what-does-a-red-or-failed-request-in-the-network-panel-mean)
- [49: What does "Preserve log" do in the Network and Console panels?](#49-what-does-preserve-log-do-in-the-network-and-console-panels)
- [50: What does "Disable cache" do in the Network panel?](#50-what-does-disable-cache-do-in-the-network-panel)
- [51: What is a hard reload?](#51-what-is-a-hard-reload)
- [52: What is CORS?](#52-what-is-cors)
- [53: How do you recognize a CORS error?](#53-how-do-you-recognize-a-cors-error)
- [54: What is the Application panel?](#54-what-is-the-application-panel)
- [55: How do you view and edit cookies in DevTools?](#55-how-do-you-view-and-edit-cookies-in-devtools)
- [56: What is the difference between localStorage and sessionStorage when debugging?](#56-what-is-the-difference-between-localstorage-and-sessionstorage-when-debugging)
- [57: How do you clear all site data while debugging?](#57-how-do-you-clear-all-site-data-while-debugging)
- [58: What is a TypeError in JavaScript?](#58-what-is-a-typeerror-in-javascript)
- [59: What is a ReferenceError?](#59-what-is-a-referenceerror)
- [60: What is a SyntaxError and when do you see it?](#60-what-is-a-syntaxerror-and-when-do-you-see-it)
- [61: What does "Cannot read properties of undefined" mean and how do you fix it?](#61-what-does-cannot-read-properties-of-undefined-mean-and-how-do-you-fix-it)
- [62: What does "x is not a function" mean?](#62-what-does-x-is-not-a-function-mean)
- [63: What is an unhandled promise rejection?](#63-what-is-an-unhandled-promise-rejection)
- [64: Why doesn't fetch throw an error for a 404 or 500 response?](#64-why-doesnt-fetch-throw-an-error-for-a-404-or-500-response)
- [65: What is the difference between null and undefined when debugging?](#65-what-is-the-difference-between-null-and-undefined-when-debugging)
- [66: Why does document.querySelector return null?](#66-why-does-documentqueryselector-return-null)
- [67: What is event bubbling?](#67-what-is-event-bubbling)
- [68: What is the difference between event.target and event.currentTarget?](#68-what-is-the-difference-between-eventtarget-and-eventcurrenttarget)
- [69: What is the difference between stopPropagation and preventDefault?](#69-what-is-the-difference-between-stoppropagation-and-preventdefault)
- [70: How do you see the event listeners on an element?](#70-how-do-you-see-the-event-listeners-on-an-element)
- [71: What is a closure and how can it cause bugs?](#71-what-is-a-closure-and-how-can-it-cause-bugs)
- [72: What is a memory leak in a web page?](#72-what-is-a-memory-leak-in-a-web-page)
- [73: How do you notice a memory leak?](#73-how-do-you-notice-a-memory-leak)
- [74: What is the Memory panel in Chrome DevTools?](#74-what-is-the-memory-panel-in-chrome-devtools)
- [75: What is the Performance panel used for?](#75-what-is-the-performance-panel-used-for)
- [76: What is a long task?](#76-what-is-a-long-task)
- [77: What is jank?](#77-what-is-jank)
- [78: What are Core Web Vitals?](#78-what-are-core-web-vitals)
- [79: What is Lighthouse?](#79-what-is-lighthouse)
- [80: What is React DevTools?](#80-what-is-react-devtools)
- [81: How do you find which React component renders a DOM element?](#81-how-do-you-find-which-react-component-renders-a-dom-element)
- [82: What is Angular DevTools?](#82-what-is-angular-devtools)
- [83: What is a hydration error?](#83-what-is-a-hydration-error)
- [84: What is Redux DevTools?](#84-what-is-redux-devtools)
- [85: How does TypeScript help prevent bugs?](#85-how-does-typescript-help-prevent-bugs)
- [86: How do you read a TypeScript error message?](#86-how-do-you-read-a-typescript-error-message)
- [87: What is a bundler?](#87-what-is-a-bundler)
- [88: What is the difference between a dev server and a production build?](#88-what-is-the-difference-between-a-dev-server-and-a-production-build)
- [89: What is hot module replacement (HMR)?](#89-what-is-hot-module-replacement-hmr)
- [90: What is cross-browser testing?](#90-what-is-cross-browser-testing)
- [91: How do you check if a browser supports a feature?](#91-how-do-you-check-if-a-browser-supports-a-feature)
- [92: What is device mode in Chrome DevTools?](#92-what-is-device-mode-in-chrome-devtools)
- [93: What is remote debugging?](#93-what-is-remote-debugging)
- [94: What is the accessibility tree?](#94-what-is-the-accessibility-tree)
- [95: How do you find accessibility problems quickly?](#95-how-do-you-find-accessibility-problems-quickly)
- [96: What is CSP and how does it show up while debugging?](#96-what-is-csp-and-how-does-it-show-up-while-debugging)
- [97: What is mixed content?](#97-what-is-mixed-content)
- [98: What is the SameSite cookie attribute?](#98-what-is-the-samesite-cookie-attribute)
- [99: What is a third-party script?](#99-what-is-a-third-party-script)
- [100: What is a service worker?](#100-what-is-a-service-worker)
- [101: How do you debug a service worker in Chrome?](#101-how-do-you-debug-a-service-worker-in-chrome)
- [102: What is a Web Worker?](#102-what-is-a-web-worker)
- [103: What is a flaky test?](#103-what-is-a-flaky-test)
- [104: What are Jest and Vitest?](#104-what-are-jest-and-vitest)
- [105: How do you run a single test while debugging?](#105-how-do-you-run-a-single-test-while-debugging)
- [106: What is Sentry?](#106-what-is-sentry)
- [107: What is window.onerror?](#107-what-is-windowonerror)
- [108: What is an error boundary in React?](#108-what-is-an-error-boundary-in-react)
- [109: What is session replay?](#109-what-is-session-replay)
- [110: What is RUM (Real User Monitoring)?](#110-what-is-rum-real-user-monitoring)
- [111: What is a feature flag?](#111-what-is-a-feature-flag)
- [112: How do you debug JavaScript in VS Code?](#112-how-do-you-debug-javascript-in-vs-code)
- [113: What is Puppeteer?](#113-what-is-puppeteer)
- [114: What is the Chrome DevTools Protocol (CDP)?](#114-what-is-the-chrome-devtools-protocol-cdp)
- [115: What AI features does Chrome DevTools have for debugging?](#115-what-ai-features-does-chrome-devtools-have-for-debugging)
- [116: What is rubber duck debugging?](#116-what-is-rubber-duck-debugging)
- [117: What does it mean to debug by bisecting?](#117-what-does-it-mean-to-debug-by-bisecting)
- [118: What is git bisect?](#118-what-is-git-bisect)
- [119: Why should you read the error message carefully before searching online?](#119-why-should-you-read-the-error-message-carefully-before-searching-online)
- [120: What is the difference between a bug and a regression?](#120-what-is-the-difference-between-a-bug-and-a-regression)
- [121: Why do you check the browser console first when a page breaks?](#121-why-do-you-check-the-browser-console-first-when-a-page-breaks)
- [122: How do you filter messages in the console?](#122-how-do-you-filter-messages-in-the-console)
- [123: What is the Snippets feature in the Sources panel?](#123-what-is-the-snippets-feature-in-the-sources-panel)
- [124: What is the Command Menu in Chrome DevTools?](#124-what-is-the-command-menu-in-chrome-devtools)
- [125: How do you take a screenshot of a whole page in Chrome DevTools?](#125-how-do-you-take-a-screenshot-of-a-whole-page-in-chrome-devtools)
- [126: How do you edit a page's JavaScript or CSS and keep the changes after reload?](#126-how-do-you-edit-a-pages-javascript-or-css-and-keep-the-changes-after-reload)
- [127: What is the difference between Local Overrides and Workspaces?](#127-what-is-the-difference-between-local-overrides-and-workspaces)
- [128: How do you simulate a slow network?](#128-how-do-you-simulate-a-slow-network)
- [129: How do you test what happens when the user goes offline?](#129-how-do-you-test-what-happens-when-the-user-goes-offline)
- [130: What is request blocking in DevTools?](#130-what-is-request-blocking-in-devtools)
- [131: What is a HAR file?](#131-what-is-a-har-file)
- [132: How do you copy a network request to run it outside the browser?](#132-how-do-you-copy-a-network-request-to-run-it-outside-the-browser)
- [133: How do you see a request's response body in DevTools?](#133-how-do-you-see-a-requests-response-body-in-devtools)
- [134: What is the Timing tab in the Network panel?](#134-what-is-the-timing-tab-in-the-network-panel)
- [135: What is the Initiator column in the Network panel?](#135-what-is-the-initiator-column-in-the-network-panel)
- [136: How do you debug a failing form submission?](#136-how-do-you-debug-a-failing-form-submission)
- [137: What are DOM breakpoints?](#137-what-are-dom-breakpoints)
- [138: What are event listener breakpoints?](#138-what-are-event-listener-breakpoints)
- [139: What are XHR/fetch breakpoints?](#139-what-are-xhrfetch-breakpoints)
- [140: What is the ignore list in DevTools?](#140-what-is-the-ignore-list-in-devtools)
- [141: How do you check which element is on top at a certain point on the page?](#141-how-do-you-check-which-element-is-on-top-at-a-certain-point-on-the-page)
- [142: What is z-index and why does it sometimes not work?](#142-what-is-z-index-and-why-does-it-sometimes-not-work)
- [143: How do you debug an element that is not visible on the page?](#143-how-do-you-debug-an-element-that-is-not-visible-on-the-page)
- [144: How do you debug a horizontal scrollbar appearing on a page?](#144-how-do-you-debug-a-horizontal-scrollbar-appearing-on-a-page)
- [145: What are the flexbox and grid overlays in DevTools?](#145-what-are-the-flexbox-and-grid-overlays-in-devtools)
- [146: How do you debug a CSS file that isn't applied at all?](#146-how-do-you-debug-a-css-file-that-isnt-applied-at-all)
- [147: What is the difference between display: none and visibility: hidden?](#147-what-is-the-difference-between-display-none-and-visibility-hidden)
- [148: Why should you test with browser extensions disabled?](#148-why-should-you-test-with-browser-extensions-disabled)
- [149: What is a race condition in front-end code?](#149-what-is-a-race-condition-in-front-end-code)
- [150: How are framework error messages different in development and production?](#150-how-are-framework-error-messages-different-in-development-and-production)

### Moderate Questions (151-300)

- [151: How do you debug an error from production that only has a minified stack trace?](#151-how-do-you-debug-an-error-from-production-that-only-has-a-minified-stack-trace)
- [152: What are hidden source maps and why use them in production?](#152-what-are-hidden-source-maps-and-why-use-them-in-production)
- [153: Why might DevTools not load your source maps?](#153-why-might-devtools-not-load-your-source-maps)
- [154: What are async stack traces?](#154-what-are-async-stack-traces)
- [155: How do you debug async/await code with breakpoints?](#155-how-do-you-debug-asyncawait-code-with-breakpoints)
- [156: What do debug(fn) and monitor(fn) do in the Chrome console?](#156-what-do-debugfn-and-monitorfn-do-in-the-chrome-console)
- [157: What does monitorEvents do?](#157-what-does-monitorevents-do)
- [158: What are some useful console utilities besides $ and $$?](#158-what-are-some-useful-console-utilities-besides--and-)
- [159: What are live expressions in the console?](#159-what-are-live-expressions-in-the-console)
- [160: Why doesn't a breakpoint get hit?](#160-why-doesnt-a-breakpoint-get-hit)
- [161: What do "Continue to here" and "Restart frame" do?](#161-what-do-continue-to-here-and-restart-frame-do)
- [162: Can you change code while the debugger is paused?](#162-can-you-change-code-while-the-debugger-is-paused)
- [163: How do you debug an event handler that doesn't fire?](#163-how-do-you-debug-an-event-handler-that-doesnt-fire)
- [164: How do you debug an event handler that runs twice?](#164-how-do-you-debug-an-event-handler-that-runs-twice)
- [165: What is a passive event listener and what bug can it cause?](#165-what-is-a-passive-event-listener-and-what-bug-can-it-cause)
- [166: What bugs are common with event delegation?](#166-what-bugs-are-common-with-event-delegation)
- [167: Why doesn't removeEventListener remove my listener?](#167-why-doesnt-removeeventlistener-remove-my-listener)
- [168: How do you debug a stale value inside setInterval?](#168-how-do-you-debug-a-stale-value-inside-setinterval)
- [169: How do you fix a race condition in a search box?](#169-how-do-you-fix-a-race-condition-in-a-search-box)
- [170: What bugs come from a missing await?](#170-what-bugs-come-from-a-missing-await)
- [171: Why doesn't async work inside forEach?](#171-why-doesnt-async-work-inside-foreach)
- [172: What is the difference between Promise.all and Promise.allSettled when debugging?](#172-what-is-the-difference-between-promiseall-and-promiseallsettled-when-debugging)
- [173: How do you debug code that runs in an unexpected order?](#173-how-do-you-debug-code-that-runs-in-an-unexpected-order)
- [174: How do you debug a CORS preflight failure?](#174-how-do-you-debug-a-cors-preflight-failure)
- [175: Why does CORS fail when you send cookies?](#175-why-does-cors-fail-when-you-send-cookies)
- [176: How do you tell if a response came from the cache?](#176-how-do-you-tell-if-a-response-came-from-the-cache)
- [177: How do you debug users seeing an old version of the app after a deploy?](#177-how-do-you-debug-users-seeing-an-old-version-of-the-app-after-a-deploy)
- [178: How do you debug a redirect loop?](#178-how-do-you-debug-a-redirect-loop)
- [179: How do you debug WebSocket connections?](#179-how-do-you-debug-websocket-connections)
- [180: How do you debug Server-Sent Events or streaming responses?](#180-how-do-you-debug-server-sent-events-or-streaming-responses)
- [181: How do you test the front end against an API response you can't easily change?](#181-how-do-you-test-the-front-end-against-an-api-response-you-cant-easily-change)
- [182: How do you debug a cookie that isn't being set?](#182-how-do-you-debug-a-cookie-that-isnt-being-set)
- [183: How do you debug a cookie that isn't sent with a request?](#183-how-do-you-debug-a-cookie-that-isnt-sent-with-a-request)
- [184: What localStorage bugs are common?](#184-what-localstorage-bugs-are-common)
- [185: How do you debug IndexedDB data?](#185-how-do-you-debug-indexeddb-data)
- [186: How do you inspect Cache Storage?](#186-how-do-you-inspect-cache-storage)
- [187: Why is a new service worker stuck in "waiting"?](#187-why-is-a-new-service-worker-stuck-in-waiting)
- [188: How do you debug a specificity conflict?](#188-how-do-you-debug-a-specificity-conflict)
- [189: How do cascade layers affect debugging?](#189-how-do-cascade-layers-affect-debugging)
- [190: What creates a stacking context, and how do you debug z-index issues with it?](#190-what-creates-a-stacking-context-and-how-do-you-debug-z-index-issues-with-it)
- [191: Why doesn't position: sticky work?](#191-why-doesnt-position-sticky-work)
- [192: Why does a flex item overflow or not shrink?](#192-why-does-a-flex-item-overflow-or-not-shrink)
- [193: What is margin collapsing and how does it cause layout bugs?](#193-what-is-margin-collapsing-and-how-does-it-cause-layout-bugs)
- [194: How do you debug a CSS grid layout?](#194-how-do-you-debug-a-css-grid-layout)
- [195: Why might a CSS custom property not work?](#195-why-might-a-css-custom-property-not-work)
- [196: How do you debug web font problems?](#196-how-do-you-debug-web-font-problems)
- [197: How do you check which image a responsive image actually loaded?](#197-how-do-you-check-which-image-a-responsive-image-actually-loaded)
- [198: How do you keep CSS changes you made in DevTools?](#198-how-do-you-keep-css-changes-you-made-in-devtools)
- [199: How do you debug layout shifts (CLS)?](#199-how-do-you-debug-layout-shifts-cls)
- [200: How do you debug a slow LCP?](#200-how-do-you-debug-a-slow-lcp)
- [201: How do you debug a slow INP?](#201-how-do-you-debug-a-slow-inp)
- [202: What is layout thrashing (forced reflow)?](#202-what-is-layout-thrashing-forced-reflow)
- [203: What can the Rendering tab do for debugging?](#203-what-can-the-rendering-tab-do-for-debugging)
- [204: What is paint flashing and what does it tell you?](#204-what-is-paint-flashing-and-what-does-it-tell-you)
- [205: What is the Coverage tab used for?](#205-what-is-the-coverage-tab-used-for)
- [206: How do you find a memory leak with heap snapshots?](#206-how-do-you-find-a-memory-leak-with-heap-snapshots)
- [207: What are detached DOM nodes?](#207-what-are-detached-dom-nodes)
- [208: What are the most common listener and timer leaks?](#208-what-are-the-most-common-listener-and-timer-leaks)
- [209: What do Shallow size and Retained size mean in a heap snapshot?](#209-what-do-shallow-size-and-retained-size-mean-in-a-heap-snapshot)
- [210: How do you find out why a React component re-rendered?](#210-how-do-you-find-out-why-a-react-component-re-rendered)
- [211: How do you debug a useEffect that runs too often or in a loop?](#211-how-do-you-debug-a-useeffect-that-runs-too-often-or-in-a-loop)
- [212: What is a stale closure in React and how do you fix it?](#212-what-is-a-stale-closure-in-react-and-how-do-you-fix-it)
- [213: Why do effects run twice in React development?](#213-why-do-effects-run-twice-in-react-development)
- [214: How do you fix a hydration mismatch in React?](#214-how-do-you-fix-a-hydration-mismatch-in-react)
- [215: What bugs come from wrong keys in React lists?](#215-what-bugs-come-from-wrong-keys-in-react-lists)
- [216: Why doesn't React state update immediately after setState?](#216-why-doesnt-react-state-update-immediately-after-setstate)
- [217: What does "Too many re-renders" mean in React?](#217-what-does-too-many-re-renders-mean-in-react)
- [218: How do you log React errors from all roots in one place?](#218-how-do-you-log-react-errors-from-all-roots-in-one-place)
- [219: How do you debug a component when the React Compiler is used?](#219-how-do-you-debug-a-component-when-the-react-compiler-is-used)
- [220: What is ExpressionChangedAfterItHasBeenCheckedError in Angular?](#220-what-is-expressionchangedafterithasbeencheckederror-in-angular)
- [221: Why doesn't an OnPush component update in Angular?](#221-why-doesnt-an-onpush-component-update-in-angular)
- [222: How do you debug signals in Angular?](#222-how-do-you-debug-signals-in-angular)
- [223: What changes when debugging a zoneless Angular app?](#223-what-changes-when-debugging-a-zoneless-angular-app)
- [224: What can you do with the ng global in the browser console?](#224-what-can-you-do-with-the-ng-global-in-the-browser-console)
- [225: How do you debug NullInjectorError in Angular?](#225-how-do-you-debug-nullinjectorerror-in-angular)
- [226: How do you debug Angular hydration errors?](#226-how-do-you-debug-angular-hydration-errors)
- [227: How do you tell if a Next.js error happened on the server or the client?](#227-how-do-you-tell-if-a-nextjs-error-happened-on-the-server-or-the-client)
- [228: What errors happen with "use client" boundaries in Next.js?](#228-what-errors-happen-with-use-client-boundaries-in-nextjs)
- [229: How do you debug stale data in a Next.js App Router app?](#229-how-do-you-debug-stale-data-in-a-nextjs-app-router-app)
- [230: Why is an environment variable undefined in the browser in Next.js or Vite?](#230-why-is-an-environment-variable-undefined-in-the-browser-in-nextjs-or-vite)
- [231: How do you debug Next.js server code with breakpoints?](#231-how-do-you-debug-nextjs-server-code-with-breakpoints)
- [232: How do you use Redux DevTools to find a bug in state?](#232-how-do-you-use-redux-devtools-to-find-a-bug-in-state)
- [233: How do you debug NgRx?](#233-how-do-you-debug-ngrx)
- [234: How do you debug a Zustand store?](#234-how-do-you-debug-a-zustand-store)
- [235: What does "Object is possibly undefined" mean in TypeScript and how should you fix it?](#235-what-does-object-is-possibly-undefined-mean-in-typescript-and-how-should-you-fix-it)
- [236: Why does TypeScript show no errors in the editor but fail in CI (or the other way)?](#236-why-does-typescript-show-no-errors-in-the-editor-but-fail-in-ci-or-the-other-way)
- [237: How do you fix "Cannot find module or its corresponding type declarations"?](#237-how-do-you-fix-cannot-find-module-or-its-corresponding-type-declarations)
- [238: What is the difference between @ts-ignore and @ts-expect-error?](#238-what-is-the-difference-between-ts-ignore-and-ts-expect-error)
- [239: How do you debug "Module not found" errors in a bundler?](#239-how-do-you-debug-module-not-found-errors-in-a-bundler)
- [240: How do you find what makes your JavaScript bundle so big?](#240-how-do-you-find-what-makes-your-javascript-bundle-so-big)
- [241: Why isn't tree shaking removing unused code?](#241-why-isnt-tree-shaking-removing-unused-code)
- [242: What does "Invalid hook call" mean in React, besides breaking the rules of hooks?](#242-what-does-invalid-hook-call-mean-in-react-besides-breaking-the-rules-of-hooks)
- [243: How do you debug dependency version conflicts?](#243-how-do-you-debug-dependency-version-conflicts)
- [244: How do you debug "it works on my machine" build problems?](#244-how-do-you-debug-it-works-on-my-machine-build-problems)
- [245: How do you fix problems caused by Vite's dependency pre-bundling cache?](#245-how-do-you-fix-problems-caused-by-vites-dependency-pre-bundling-cache)
- [246: Why might CSS look different in production than in development?](#246-why-might-css-look-different-in-production-than-in-development)
- [247: What date and time bugs are common in the front end?](#247-what-date-and-time-bugs-are-common-in-the-front-end)
- [248: How do you debug the 100vh problem on mobile browsers?](#248-how-do-you-debug-the-100vh-problem-on-mobile-browsers)
- [249: What touch and hover bugs happen on mobile devices?](#249-what-touch-and-hover-bugs-happen-on-mobile-devices)
- [250: How do you set up remote debugging for an Android device?](#250-how-do-you-set-up-remote-debugging-for-an-android-device)
- [251: How do you debug a page on an iPhone?](#251-how-do-you-debug-a-page-on-an-iphone)
- [252: How do you debug media query breakpoints?](#252-how-do-you-debug-media-query-breakpoints)
- [253: How do you debug container queries?](#253-how-do-you-debug-container-queries)
- [254: How do you debug a missing accessible name?](#254-how-do-you-debug-a-missing-accessible-name)
- [255: How do you debug focus problems?](#255-how-do-you-debug-focus-problems)
- [256: What ARIA mistakes cause accessibility bugs?](#256-what-aria-mistakes-cause-accessibility-bugs)
- [257: How do you check color contrast and vision issues in DevTools?](#257-how-do-you-check-color-contrast-and-vision-issues-in-devtools)
- [258: How do you test a CSP before enforcing it?](#258-how-do-you-test-a-csp-before-enforcing-it)
- [259: What is the Issues panel in Chrome DevTools?](#259-what-is-the-issues-panel-in-chrome-devtools)
- [260: How do you find which third-party scripts slow down a page?](#260-how-do-you-find-which-third-party-scripts-slow-down-a-page)
- [261: How do you debug code inside an iframe?](#261-how-do-you-debug-code-inside-an-iframe)
- [262: How do you debug a Web Worker?](#262-how-do-you-debug-a-web-worker)
- [263: How do you debug a failing Jest or Vitest test with breakpoints?](#263-how-do-you-debug-a-failing-jest-or-vitest-test-with-breakpoints)
- [264: How do you see what React Testing Library is rendering?](#264-how-do-you-see-what-react-testing-library-is-rendering)
- [265: Why does getByText fail even though the text appears later?](#265-why-does-getbytext-fail-even-though-the-text-appears-later)
- [266: Why does vi.mock or jest.mock not seem to work?](#266-why-does-vimock-or-jestmock-not-seem-to-work)
- [267: How do you debug tests that use fake timers?](#267-how-do-you-debug-tests-that-use-fake-timers)
- [268: How do you debug a Cypress test?](#268-how-do-you-debug-a-cypress-test)
- [269: How do you debug a Playwright test?](#269-how-do-you-debug-a-playwright-test)
- [270: How do you investigate a flaky end-to-end test?](#270-how-do-you-investigate-a-flaky-end-to-end-test)
- [271: How do you handle failing snapshot tests?](#271-how-do-you-handle-failing-snapshot-tests)
- [272: How do you set up Sentry so production errors are readable?](#272-how-do-you-set-up-sentry-so-production-errors-are-readable)
- [273: What extra context should you send with production errors?](#273-what-extra-context-should-you-send-with-production-errors)
- [274: How do you catch unhandled promise rejections globally?](#274-how-do-you-catch-unhandled-promise-rejections-globally)
- [275: Why do you see "Script error." with no details?](#275-why-do-you-see-script-error-with-no-details)
- [276: What should you log in the front end in production, and what should you avoid?](#276-what-should-you-log-in-the-front-end-in-production-and-what-should-you-avoid)
- [277: How do you reduce noise in production error reports?](#277-how-do-you-reduce-noise-in-production-error-reports)
- [278: How do you debug a bug that only some users see because of a feature flag?](#278-how-do-you-debug-a-bug-that-only-some-users-see-because-of-a-feature-flag)
- [279: How do you configure VS Code to debug a Vite or React app in Chrome?](#279-how-do-you-configure-vs-code-to-debug-a-vite-or-react-app-in-chrome)
- [280: How do you capture console errors and failed requests with Puppeteer?](#280-how-do-you-capture-console-errors-and-failed-requests-with-puppeteer)
- [281: How do you record reproduction steps for a bug without writing code?](#281-how-do-you-record-reproduction-steps-for-a-bug-without-writing-code)
- [282: How do you use AI assistance in DevTools to debug a style problem?](#282-how-do-you-use-ai-assistance-in-devtools-to-debug-a-style-problem)
- [283: What do you check when something works locally but breaks in production?](#283-what-do-you-check-when-something-works-locally-but-breaks-in-production)
- [284: How do you debug a blank white screen in a single page app?](#284-how-do-you-debug-a-blank-white-screen-in-a-single-page-app)
- [285: How do you debug a page that freezes completely?](#285-how-do-you-debug-a-page-that-freezes-completely)
- [286: How do you debug a slow initial page load?](#286-how-do-you-debug-a-slow-initial-page-load)
- [287: How do you debug "404 on refresh" in a single page app?](#287-how-do-you-debug-404-on-refresh-in-a-single-page-app)
- [288: How do you debug back/forward cache (bfcache) issues?](#288-how-do-you-debug-backforward-cache-bfcache-issues)
- [289: How do you debug CSS animations and transitions?](#289-how-do-you-debug-css-animations-and-transitions)
- [290: How do you debug a scroll position bug in a single page app?](#290-how-do-you-debug-a-scroll-position-bug-in-a-single-page-app)
- [291: How do you debug a "ChunkLoadError" or "Failed to fetch dynamically imported module"?](#291-how-do-you-debug-a-chunkloaderror-or-failed-to-fetch-dynamically-imported-module)
- [292: How do you debug an element that jumps or flickers on hover?](#292-how-do-you-debug-an-element-that-jumps-or-flickers-on-hover)
- [293: How do you debug wrong text encoding or broken characters?](#293-how-do-you-debug-wrong-text-encoding-or-broken-characters)
- [294: How do you debug a form that the browser autofills incorrectly?](#294-how-do-you-debug-a-form-that-the-browser-autofills-incorrectly)
- [295: How do you debug a bug that only happens in one browser?](#295-how-do-you-debug-a-bug-that-only-happens-in-one-browser)
- [296: How do you debug a dark mode bug?](#296-how-do-you-debug-a-dark-mode-bug)
- [297: How do you debug a print layout?](#297-how-do-you-debug-a-print-layout)
- [298: How do you debug a problem in a production site you can't change?](#298-how-do-you-debug-a-problem-in-a-production-site-you-cant-change)
- [299: How do you find which micro frontend owns a part of the page?](#299-how-do-you-find-which-micro-frontend-owns-a-part-of-the-page)
- [300: What should a good bug report contain?](#300-what-should-a-good-bug-report-contain)

### Advanced Questions (301-450)

- [301: How does a source map work internally?](#301-how-does-a-source-map-work-internally)
- [302: Why might source maps point to the wrong line?](#302-why-might-source-maps-point-to-the-wrong-line)
- [303: Why do stack traces still show minified function names even with source maps?](#303-why-do-stack-traces-still-show-minified-function-names-even-with-source-maps)
- [304: What are the security concerns of source maps in production?](#304-what-are-the-security-concerns-of-source-maps-in-production)
- [305: How does V8 build stack traces, and what limits them?](#305-how-does-v8-build-stack-traces-and-what-limits-them)
- [306: How do Error.cause and AggregateError help debugging?](#306-how-do-errorcause-and-aggregateerror-help-debugging)
- [307: Why does instanceof fail for errors or arrays from an iframe or a different realm?](#307-why-does-instanceof-fail-for-errors-or-arrays-from-an-iframe-or-a-different-realm)
- [308: Why does a bug disappear when DevTools is open or when you add a console.log?](#308-why-does-a-bug-disappear-when-devtools-is-open-or-when-you-add-a-consolelog)
- [309: How do you debug a production bug in minified code when you don't have source maps?](#309-how-do-you-debug-a-production-bug-in-minified-code-when-you-dont-have-source-maps)
- [310: Walk through finding a memory leak that grows with every route change in a single page app.](#310-walk-through-finding-a-memory-leak-that-grows-with-every-route-change-in-a-single-page-app)
- [311: How can closures keep more memory alive than you expect?](#311-how-can-closures-keep-more-memory-alive-than-you-expect)
- [312: How can WeakMap, WeakRef and FinalizationRegistry help with memory bugs?](#312-how-can-weakmap-weakref-and-finalizationregistry-help-with-memory-bugs)
- [313: How do RxJS subscriptions cause leaks in Angular, and how do you find them?](#313-how-do-rxjs-subscriptions-cause-leaks-in-angular-and-how-do-you-find-them)
- [314: How do memory leaks typically happen in React apps?](#314-how-do-memory-leaks-typically-happen-in-react-apps)
- [315: How can you measure memory usage in production?](#315-how-can-you-measure-memory-usage-in-production)
- [316: What is the Long Animation Frames API and why is it better than the Long Tasks API for debugging?](#316-what-is-the-long-animation-frames-api-and-why-is-it-better-than-the-long-tasks-api-for-debugging)
- [317: How do you debug a high INP caused by presentation delay?](#317-how-do-you-debug-a-high-inp-caused-by-presentation-delay)
- [318: How do you find expensive CSS selectors?](#318-how-do-you-find-expensive-css-selectors)
- [319: How do layers and compositing affect rendering bugs?](#319-how-do-layers-and-compositing-affect-rendering-bugs)
- [320: How do you debug scroll jank?](#320-how-do-you-debug-scroll-jank)
- [321: What bugs can content-visibility: auto cause?](#321-what-bugs-can-content-visibility-auto-cause)
- [322: Why can LCP look good in Lighthouse but bad in the field?](#322-why-can-lcp-look-good-in-lighthouse-but-bad-in-the-field)
- [323: How are Web Vitals measured differently in single page apps?](#323-how-are-web-vitals-measured-differently-in-single-page-apps)
- [324: How do you use React's Performance Tracks in Chrome DevTools?](#324-how-do-you-use-reacts-performance-tracks-in-chrome-devtools)
- [325: How do you add your own markers to a Performance trace?](#325-how-do-you-add-your-own-markers-to-a-performance-trace)
- [326: How does React recover from hydration errors, and why does it matter for debugging?](#326-how-does-react-recover-from-hydration-errors-and-why-does-it-matter-for-debugging)
- [327: How do you debug errors in React Server Components?](#327-how-do-you-debug-errors-in-react-server-components)
- [328: What is tearing in React and how do you debug it?](#328-what-is-tearing-in-react-and-how-do-you-debug-it)
- [329: Why does a component suspend forever or keep refetching with use() or Suspense?](#329-why-does-a-component-suspend-forever-or-keep-refetching-with-use-or-suspense)
- [330: How do you prevent and debug race conditions in useEffect data fetching?](#330-how-do-you-prevent-and-debug-race-conditions-in-useeffect-data-fetching)
- [331: How do you debug a re-render storm caused by React context?](#331-how-do-you-debug-a-re-render-storm-caused-by-react-context)
- [332: How do you find zone pollution in a zone.js Angular app?](#332-how-do-you-find-zone-pollution-in-a-zonejs-angular-app)
- [333: What causes NG0600 and infinite loops with Angular signals?](#333-what-causes-ng0600-and-infinite-loops-with-angular-signals)
- [334: How do you debug duplicate HTTP requests in Angular SSR?](#334-how-do-you-debug-duplicate-http-requests-in-angular-ssr)
- [335: How do you debug stale or wrong caching in Next.js at a deeper level?](#335-how-do-you-debug-stale-or-wrong-caching-in-nextjs-at-a-deeper-level)
- [336: How can SSR leak data between users, and how do you find it?](#336-how-can-ssr-leak-data-between-users-and-how-do-you-find-it)
- [337: How do Reselect's development checks help with selector bugs?](#337-how-do-reselects-development-checks-help-with-selector-bugs)
- [338: What do Redux Toolkit's serializability and immutability checks catch?](#338-what-do-redux-toolkits-serializability-and-immutability-checks-catch)
- [339: How do you debug state that is out of sync between browser tabs?](#339-how-do-you-debug-state-that-is-out-of-sync-between-browser-tabs)
- [340: How do you debug optimistic update bugs?](#340-how-do-you-debug-optimistic-update-bugs)
- [341: How do you debug slow TypeScript type checking?](#341-how-do-you-debug-slow-typescript-type-checking)
- [342: Why can TypeScript types give you false confidence about runtime data?](#342-why-can-typescript-types-give-you-false-confidence-about-runtime-data)
- [343: How do you debug a confusing generic type error?](#343-how-do-you-debug-a-confusing-generic-type-error)
- [344: Why doesn't a module augmentation or global type declaration apply?](#344-why-doesnt-a-module-augmentation-or-global-type-declaration-apply)
- [345: How do you debug a webpack build?](#345-how-do-you-debug-a-webpack-build)
- [346: How do you debug a Vite build or dev server problem?](#346-how-do-you-debug-a-vite-build-or-dev-server-problem)
- [347: What ESM and CommonJS interop bugs are common?](#347-what-esm-and-commonjs-interop-bugs-are-common)
- [348: What is the dual package hazard?](#348-what-is-the-dual-package-hazard)
- [349: How do package.json exports conditions cause wrong files to load?](#349-how-do-packagejson-exports-conditions-cause-wrong-files-to-load)
- [350: Why might sideEffects: false break your app?](#350-why-might-sideeffects-false-break-your-app)
- [351: How do you debug code that fails in older browsers?](#351-how-do-you-debug-code-that-fails-in-older-browsers)
- [352: How do you find duplicate packages in a bundle, and why do they matter?](#352-how-do-you-find-duplicate-packages-in-a-bundle-and-why-do-they-matter)
- [353: What problems are common in monorepos with package managers like pnpm?](#353-what-problems-are-common-in-monorepos-with-package-managers-like-pnpm)
- [354: How do you debug a Safari-only rendering bug?](#354-how-do-you-debug-a-safari-only-rendering-bug)
- [355: What JavaScript differences between engines can cause bugs?](#355-what-javascript-differences-between-engines-can-cause-bugs)
- [356: How do you reproduce performance problems that only happen on low-end devices?](#356-how-do-you-reproduce-performance-problems-that-only-happen-on-low-end-devices)
- [357: How do you debug a page inside an in-app browser or WebView?](#357-how-do-you-debug-a-page-inside-an-in-app-browser-or-webview)
- [358: What iOS Safari viewport bugs are common, and how do you debug them?](#358-what-ios-safari-viewport-bugs-are-common-and-how-do-you-debug-them)
- [359: Why do layout bugs appear at certain zoom levels or device pixel ratios?](#359-why-do-layout-bugs-appear-at-certain-zoom-levels-or-device-pixel-ratios)
- [360: How do you test that the layout survives large text sizes?](#360-how-do-you-test-that-the-layout-survives-large-text-sizes)
- [361: How do you debug screen reader announcements for dynamic content?](#361-how-do-you-debug-screen-reader-announcements-for-dynamic-content)
- [362: How do you debug focus and announcements on route changes in a single page app?](#362-how-do-you-debug-focus-and-announcements-on-route-changes-in-a-single-page-app)
- [363: How do you catch accessibility regressions automatically?](#363-how-do-you-catch-accessibility-regressions-automatically)
- [364: Why do ARIA references break across shadow DOM boundaries?](#364-why-do-aria-references-break-across-shadow-dom-boundaries)
- [365: How do you debug a CSP with nonces and strict-dynamic?](#365-how-do-you-debug-a-csp-with-nonces-and-strict-dynamic)
- [366: What are Trusted Types and how do you debug violations?](#366-what-are-trusted-types-and-how-do-you-debug-violations)
- [367: How do you debug features that depend on third-party cookies?](#367-how-do-you-debug-features-that-depend-on-third-party-cookies)
- [368: How do you debug cross-origin isolation errors (COOP and COEP)?](#368-how-do-you-debug-cross-origin-isolation-errors-coop-and-coep)
- [369: Why does fetch with mode "no-cors" seem to work but return nothing?](#369-why-does-fetch-with-mode-no-cors-seem-to-work-but-return-nothing)
- [370: How do you debug a race condition in token refresh?](#370-how-do-you-debug-a-race-condition-in-token-refresh)
- [371: How do you find where an XSS payload gets into the DOM?](#371-how-do-you-find-where-an-xss-payload-gets-into-the-dom)
- [372: How do you find out which script injected another script or element?](#372-how-do-you-find-out-which-script-injected-another-script-or-element)
- [373: How do you find which code changes a property or global variable?](#373-how-do-you-find-which-code-changes-a-property-or-global-variable)
- [374: How can third-party scripts break your code by changing globals or built-in prototypes?](#374-how-can-third-party-scripts-break-your-code-by-changing-globals-or-built-in-prototypes)
- [375: How do you debug shared dependency problems in Module Federation?](#375-how-do-you-debug-shared-dependency-problems-in-module-federation)
- [376: How do you debug CSS leaking between micro frontends?](#376-how-do-you-debug-css-leaking-between-micro-frontends)
- [377: How do you debug communication and routing conflicts between micro frontends?](#377-how-do-you-debug-communication-and-routing-conflicts-between-micro-frontends)
- [378: How do you send micro frontend errors to the right team?](#378-how-do-you-send-micro-frontend-errors-to-the-right-team)
- [379: How do you debug a service worker fetch handler?](#379-how-do-you-debug-a-service-worker-fetch-handler)
- [380: What bugs come from users running mixed versions of a service-worker-cached app?](#380-what-bugs-come-from-users-running-mixed-versions-of-a-service-worker-cached-app)
- [381: How do you remove a broken service worker that is already in production?](#381-how-do-you-remove-a-broken-service-worker-that-is-already-in-production)
- [382: What bugs appear with SharedArrayBuffer and Atomics in workers, and how do you debug them?](#382-what-bugs-appear-with-sharedarraybuffer-and-atomics-in-workers-and-how-do-you-debug-them)
- [383: Why can a worker fail to load after bundling?](#383-why-can-a-worker-fail-to-load-after-bundling)
- [384: How do you debug WebAssembly code in the browser?](#384-how-do-you-debug-webassembly-code-in-the-browser)
- [385: How do you investigate WebAssembly errors and performance?](#385-how-do-you-investigate-webassembly-errors-and-performance)
- [386: How do you find tests that depend on test order?](#386-how-do-you-find-tests-that-depend-on-test-order)
- [387: Why can tests in jsdom pass while the real browser is broken (or the other way)?](#387-why-can-tests-in-jsdom-pass-while-the-real-browser-is-broken-or-the-other-way)
- [388: How do you debug tests that leak async work into other tests?](#388-how-do-you-debug-tests-that-leak-async-work-into-other-tests)
- [389: How do you use a Playwright trace to find the cause of a CI-only failure?](#389-how-do-you-use-a-playwright-trace-to-find-the-cause-of-a-ci-only-failure)
- [390: How do you deal with flaky visual regression tests?](#390-how-do-you-deal-with-flaky-visual-regression-tests)
- [391: How can API mocks give you false confidence, and how do you catch it?](#391-how-can-api-mocks-give-you-false-confidence-and-how-do-you-catch-it)
- [392: Why do tests time out only in CI, and how do you fix it?](#392-why-do-tests-time-out-only-in-ci-and-how-do-you-fix-it)
- [393: How do you design error boundaries so failures stay small and recoverable?](#393-how-do-you-design-error-boundaries-so-failures-stay-small-and-recoverable)
- [394: How do you connect a front-end error to the back-end logs of the same request?](#394-how-do-you-connect-a-front-end-error-to-the-back-end-logs-of-the-same-request)
- [395: How do you choose sampling rates for errors, traces and replays?](#395-how-do-you-choose-sampling-rates-for-errors-traces-and-replays)
- [396: How do you debug a production bug that nobody can reproduce?](#396-how-do-you-debug-a-production-bug-that-nobody-can-reproduce)
- [397: How do you use RUM data to find the cause of bad Web Vitals?](#397-how-do-you-use-rum-data-to-find-the-cause-of-bad-web-vitals)
- [398: How do you send logs reliably when the user closes the page?](#398-how-do-you-send-logs-reliably-when-the-user-closes-the-page)
- [399: How can feature flags cause hydration mismatches, and how do you avoid it?](#399-how-can-feature-flags-cause-hydration-mismatches-and-how-do-you-avoid-it)
- [400: How do you find out if a new release caused a problem?](#400-how-do-you-find-out-if-a-new-release-caused-a-problem)
- [401: How do you debug a full stack app (like Next.js) in VS Code with one launch?](#401-how-do-you-debug-a-full-stack-app-like-nextjs-in-vs-code-with-one-launch)
- [402: What breakpoint features does VS Code's JavaScript debugger have?](#402-what-breakpoint-features-does-vs-codes-javascript-debugger-have)
- [403: How do you use the Chrome DevTools Protocol directly from Puppeteer?](#403-how-do-you-use-the-chrome-devtools-protocol-directly-from-puppeteer)
- [404: How would you write an automated check for memory leaks?](#404-how-would-you-write-an-automated-check-for-memory-leaks)
- [405: How do you capture a performance trace automatically?](#405-how-do-you-capture-a-performance-trace-automatically)
- [406: What is the Chrome DevTools MCP server and what are its risks?](#406-what-is-the-chrome-devtools-mcp-server-and-what-are-its-risks)
- [407: What are the limits of AI-assisted debugging, and how do you use it well?](#407-what-are-the-limits-of-ai-assisted-debugging-and-how-do-you-use-it-well)
- [408: What does Firefox DevTools offer that is useful for debugging?](#408-what-does-firefox-devtools-offer-that-is-useful-for-debugging)
- [409: What bugs are caused by timer throttling in background tabs?](#409-what-bugs-are-caused-by-timer-throttling-in-background-tabs)
- [410: How do page lifecycle events affect debugging on mobile?](#410-how-do-page-lifecycle-events-affect-debugging-on-mobile)
- [411: What bugs can prerendering with the Speculation Rules API cause?](#411-what-bugs-can-prerendering-with-the-speculation-rules-api-cause)
- [412: How do you debug view transitions?](#412-how-do-you-debug-view-transitions)
- [413: Why doesn't my CSS apply inside a web component?](#413-why-doesnt-my-css-apply-inside-a-web-component)
- [414: What bugs come from custom element upgrade timing?](#414-what-bugs-come-from-custom-element-upgrade-timing)
- [415: Why is event.target wrong for events from inside a shadow root?](#415-why-is-eventtarget-wrong-for-events-from-inside-a-shadow-root)
- [416: What number and money bugs are common in front-end code?](#416-what-number-and-money-bugs-are-common-in-front-end-code)
- [417: What bugs are common with virtualized lists?](#417-what-bugs-are-common-with-virtualized-lists)
- [418: How do you debug Apollo Client cache problems?](#418-how-do-you-debug-apollo-client-cache-problems)
- [419: How do you debug TanStack Query issues?](#419-how-do-you-debug-tanstack-query-issues)
- [420: What does "ResizeObserver loop completed with undelivered notifications" mean?](#420-what-does-resizeobserver-loop-completed-with-undelivered-notifications-mean)
- [421: How do you debug internationalization bugs?](#421-how-do-you-debug-internationalization-bugs)
- [422: Why do APIs like clipboard, geolocation or camera fail in some environments?](#422-why-do-apis-like-clipboard-geolocation-or-camera-fail-in-some-environments)
- [423: How do you debug "user activation" problems like blocked popups or autoplay?](#423-how-do-you-debug-user-activation-problems-like-blocked-popups-or-autoplay)
- [424: How do you debug canvas and WebGL problems?](#424-how-do-you-debug-canvas-and-webgl-problems)
- [425: How do you debug WebRTC calls?](#425-how-do-you-debug-webrtc-calls)
- [426: How do you debug audio and video playback issues?](#426-how-do-you-debug-audio-and-video-playback-issues)
- [427: How can promises freeze a page even without a long synchronous loop?](#427-how-can-promises-freeze-a-page-even-without-a-long-synchronous-loop)
- [428: How do you debug "Maximum call stack size exceeded"?](#428-how-do-you-debug-maximum-call-stack-size-exceeded)
- [429: How do circular imports cause bugs, and how do you find them?](#429-how-do-circular-imports-cause-bugs-and-how-do-you-find-them)
- [430: What do "preloaded but not used" warnings mean, and how do you debug resource priority?](#430-what-do-preloaded-but-not-used-warnings-mean-and-how-do-you-debug-resource-priority)
- [431: How do you debug a problem that only happens for users in some regions?](#431-how-do-you-debug-a-problem-that-only-happens-for-users-in-some-regions)
- [432: How do you test code that depends on the current time?](#432-how-do-you-test-code-that-depends-on-the-current-time)
- [433: How do you debug a login loop in an OAuth or OpenID Connect flow?](#433-how-do-you-debug-a-login-loop-in-an-oauth-or-openid-connect-flow)
- [434: Scenario: some users are randomly logged out. How do you investigate?](#434-scenario-some-users-are-randomly-logged-out-how-do-you-investigate)
- [435: Scenario: the checkout button does nothing for about 2% of users. How do you debug it?](#435-scenario-the-checkout-button-does-nothing-for-about-2-of-users-how-do-you-debug-it)
- [436: Scenario: a dashboard's memory grows for hours until the tab crashes. How do you find the cause?](#436-scenario-a-dashboards-memory-grows-for-hours-until-the-tab-crashes-how-do-you-find-the-cause)
- [437: Scenario: a page is fine on your laptop but slow on mid-range Android phones. What do you do?](#437-scenario-a-page-is-fine-on-your-laptop-but-slow-on-mid-range-android-phones-what-do-you-do)
- [438: Scenario: after a deploy, the layout is broken for some users until they refresh. Why?](#438-scenario-after-a-deploy-the-layout-is-broken-for-some-users-until-they-refresh-why)
- [439: Scenario: a hydration error happens only in production. How do you debug it?](#439-scenario-a-hydration-error-happens-only-in-production-how-do-you-debug-it)
- [440: Scenario: the API returns correct data, but the UI shows wrong values. Where do you look?](#440-scenario-the-api-returns-correct-data-but-the-ui-shows-wrong-values-where-do-you-look)
- [441: Scenario: a bug only happens for one specific customer account. How do you debug it?](#441-scenario-a-bug-only-happens-for-one-specific-customer-account-how-do-you-debug-it)
- [442: Scenario: errors spike right after a third-party script updates. How do you handle it?](#442-scenario-errors-spike-right-after-a-third-party-script-updates-how-do-you-handle-it)
- [443: Why might an animation run too fast on some screens, and how do you fix it?](#443-why-might-an-animation-run-too-fast-on-some-screens-and-how-do-you-fix-it)
- [444: How do you debug objects wrapped in a Proxy, like in reactive state libraries?](#444-how-do-you-debug-objects-wrapped-in-a-proxy-like-in-reactive-state-libraries)
- [445: How do you run a useful postmortem after a serious production bug?](#445-how-do-you-run-a-useful-postmortem-after-a-serious-production-bug)
- [446: How do you make a front-end app easier to debug from the start?](#446-how-do-you-make-a-front-end-app-easier-to-debug-from-the-start)
- [447: How do you decide between logging, breakpoints, tracing, profiling and session replay?](#447-how-do-you-decide-between-logging-breakpoints-tracing-profiling-and-session-replay)
- [448: How do you avoid wasting hours on the wrong lead while debugging?](#448-how-do-you-avoid-wasting-hours-on-the-wrong-lead-while-debugging)
- [449: How do you make sure a bug fix is correct and the bug doesn't come back?](#449-how-do-you-make-sure-a-bug-fix-is-correct-and-the-bug-doesnt-come-back)
- [450: Walk through how you would debug an unknown bug in a codebase you don't know yet.](#450-walk-through-how-you-would-debug-an-unknown-bug-in-a-codebase-you-dont-know-yet)

---

# Easy Questions (1-150)

## 1: What is debugging?

Debugging is the process of finding out why a program does something different from what you expect, and then fixing it. It is more than fixing: most of the time goes into understanding the problem, finding where it happens and why.

In front-end work, bugs can come from JavaScript, CSS, HTML, the network, the browser, the build, or the data coming from the server, so a good debugger knows how to check each of these.

## 2: What steps do you follow when you debug a problem?

A simple process that works for most bugs:

1. **Reproduce it.** Find exact steps that make the bug happen, ideally every time.
2. **Collect information.** Read the error message, the stack trace, the network requests, the console.
3. **Make a guess.** Based on what you saw, guess where the problem is.
4. **Test the guess.** Use breakpoints, logs or a small change to confirm or reject it.
5. **Fix the cause, not the symptom.**
6. **Verify.** Check the original steps again and, if possible, add a test so the bug does not come back.

## 3: Why is reproducing a bug the first step?

If you can't make the bug happen, you can't tell if your fix worked. A reliable reproduction also gives you a fast loop: change something, try again, see the result.

When a bug is hard to reproduce, collect more details first: browser and version, device, account, data, network speed, steps the user took, and the time it happened (so you can match it with logs).

## 4: What is a minimal reproduction?

A minimal reproduction is the smallest piece of code or the shortest set of steps that still shows the bug. You get it by removing parts of the app until the bug disappears, then putting back the last part you removed.

It helps in two ways: often you find the cause while making it, and it is what library maintainers ask for when you report a bug (for example a StackBlitz or CodeSandbox link, or a small GitHub repo).

## 5: What is a stack trace?

A stack trace is the list of function calls that were active when an error was thrown. The top line is the place where the error happened, and each line below is the function that called the one above it.

```
TypeError: Cannot read properties of undefined (reading 'name')
    at formatUser (user.js:12:18)
    at renderList (list.js:40:5)
    at main (app.js:8:3)
```

Here the error happened in `formatUser` at line 12, column 18 of `user.js`, which was called by `renderList`, which was called by `main`.

## 6: How do you read a stack trace?

Start with the error message on the first line: it tells you what went wrong. Then look at the first frame that is in your own code (not in a library or framework). That is usually the best place to start.

Then walk down the stack to understand how the code got there. If the top frames are all inside a library, the bug is often in how your code called that library, which you will find a few frames lower.

## 7: What is the difference between an error message and a stack trace?

The error message describes what went wrong, for example `Cannot read properties of undefined (reading 'name')`. The stack trace describes where it happened and the path of calls that led there.

You need both: the message tells you the kind of problem, and the stack tells you where to look.

## 8: What is the console in browser DevTools?

The Console panel shows messages logged by the page (`console.log`, warnings, errors), errors reported by the browser (failed requests, CSP violations, uncaught exceptions), and lets you run JavaScript in the context of the current page.

You can open it with `Ctrl+Shift+J` (`Cmd+Option+J` on Mac) in Chrome, and from any other panel by pressing `Esc` to open the Console drawer.

## 9: What console methods do you use besides console.log?

- `console.error` and `console.warn`: messages with error or warning level, so you can filter them.
- `console.info` and `console.debug`: lower levels. `debug` is hidden unless you enable the "Verbose" level.
- `console.table`: shows arrays or objects as a table.
- `console.dir`: shows an object as an expandable tree of properties (useful for DOM elements).
- `console.group` and `console.groupEnd`: group related messages.
- `console.time` and `console.timeEnd`: measure how long something takes.
- `console.count`: counts how many times a line runs.
- `console.trace`: prints the current stack trace.
- `console.assert`: logs an error only if a condition is false.

## 10: How does console.table help with debugging?

`console.table` prints an array of objects as a table, with one row per item and one column per property. It is much easier to read than a list of nested objects when you are checking data from an API.

```js
const users = [
  { id: 1, name: "Ana", active: true },
  { id: 2, name: "Ben", active: false },
];

console.table(users);
console.table(users, ["name"]); // only show the name column
```

## 11: How do you measure how long some code takes with the console?

Use `console.time` and `console.timeEnd` with the same label. The console prints the time in milliseconds between the two calls. `console.timeLog` prints the time so far without stopping the timer.

```js
console.time("load");
const data = await fetch("/api/items").then((r) => r.json());
console.timeLog("load", "fetched");
render(data);
console.timeEnd("load");
```

For real performance work use the Performance panel, but this is fine for a quick check.

## 12: What does console.trace do?

`console.trace()` prints a stack trace at the place where it is called, without throwing an error. It is useful when a function is called from many places and you want to know who called it this time.

```js
function saveUser(user) {
  console.trace("saveUser called");
  // ...
}
```

## 13: What does console.assert do?

`console.assert(condition, ...data)` logs an error with the given data only when the condition is false. When the condition is true, nothing happens. It does not throw and does not stop the code.

```js
console.assert(Array.isArray(items), "items should be an array", items);
```

## 14: Why can console.log show a different value than the one at the time it was logged?

When you log an object, Chrome shows a short preview at the moment of logging, but when you expand it, it reads the current values of the object. If the object changed after the log, the expanded view shows the new values. Chrome marks this with a small "i" icon saying the value was evaluated just now.

To log a snapshot, copy the object first:

```js
console.log(structuredClone(state));
// or
console.log(JSON.stringify(state, null, 2));
```

## 15: How do you log several variables so it is clear which value is which?

Wrap them in an object using shorthand properties. The console then shows the variable names as keys.

```js
const userId = 42;
const role = "admin";

console.log({ userId, role }); // { userId: 42, role: 'admin' }
```

## 16: What is the $0 variable in the console?

In Chrome, Firefox and Edge, `$0` refers to the element currently selected in the Elements panel. `$1` is the one selected before it, and so on up to `$4`. This lets you select an element visually and then work with it in the console.

```js
$0.getBoundingClientRect();
getComputedStyle($0).display;
```

## 17: What are $ and $$ in the DevTools console?

They are console helpers. `$(selector)` returns the first element that matches, like `document.querySelector`. `$$(selector)` returns an array of all matching elements, like `document.querySelectorAll` but as a real array.

If the page itself defines `$` (for example jQuery), the page's version is used instead.

```js
$$("img").filter((img) => !img.alt);
```

## 18: What is a breakpoint?

A breakpoint is a place in your code where the debugger pauses execution. While paused, you can see the values of variables, the call stack, and step through the code one line at a time.

In browser DevTools you set a breakpoint by clicking the line number in the Sources panel (Chrome) or the Debugger panel (Firefox).

## 19: What does the debugger statement do?

`debugger;` is a JavaScript statement that pauses execution at that line when DevTools is open, just like a breakpoint. If DevTools is closed, it does nothing.

```js
function calculateTotal(items) {
  debugger;
  return items.reduce((sum, item) => sum + item.price, 0);
}
```

It is handy when you can't easily find the file in DevTools. Remove it before committing; ESLint flags it with the `no-debugger` rule.

## 20: Why use breakpoints instead of console.log?

Breakpoints let you see every variable in scope, the full call stack and the state of the page at that moment, without deciding in advance what to print. You can also change values, step into functions and continue, all without editing and reloading the code.

`console.log` is still fine for quick checks or for seeing values over time, but for anything that needs more than one or two logs, a breakpoint is usually faster.

## 21: What are the stepping controls in the debugger?

- **Resume (F8):** continue running until the next breakpoint.
- **Step over (F10):** run the current line and stop at the next one, without going inside function calls.
- **Step into (F11):** if the current line calls a function, go inside it.
- **Step out (Shift+F11):** finish the current function and stop in the caller.
- **Step (F9):** step to the next statement, including into async callbacks.

## 22: What is the difference between step over and step into?

Step over runs the whole current line, including any function calls on it, and stops at the next line in the same function. Step into goes inside the function called on the current line, so you can follow its code.

Use step into when you suspect the called function. Use step over when you trust it and only care about its result.

## 23: What is the Sources panel in Chrome DevTools?

The Sources panel is where you debug JavaScript. It has:

- A file navigator on the left with all the scripts, styles and other files loaded by the page.
- A code editor in the middle where you set breakpoints.
- A debugger sidebar on the right with the call stack, scope variables, watch expressions and breakpoint lists.

It also has Snippets (small scripts you can run on any page), Overrides (local copies of network files) and Workspaces (edit files on disk).

## 24: How do you find a file quickly in the Sources panel?

Press `Ctrl+P` (`Cmd+P` on Mac) while DevTools is focused. It opens a quick search where you type part of the file name. To search text across all loaded files, press `Ctrl+Shift+F` (`Cmd+Option+F` on Mac).

## 25: What is a conditional breakpoint?

A conditional breakpoint pauses only when an expression you give is true. In Chrome, right-click a line number and choose "Add conditional breakpoint".

For example, in a loop over 1,000 items you can pause only on the broken one:

```js
item.id === 917;
```

It saves you from pressing resume hundreds of times.

## 26: What is a logpoint?

A logpoint is a breakpoint that logs a message to the console instead of pausing. In Chrome, right-click a line number and choose "Add logpoint", then type what to log, for example `"total is", total`.

It works like adding `console.log`, but you don't edit the source, don't need to rebuild, and can't forget to remove it from the code.

## 27: What does the Scope section of the debugger show?

When the debugger is paused, the Scope section shows the variables available at that point, grouped by scope:

- **Local:** variables of the current function, including `this`.
- **Closure:** variables captured from outer functions.
- **Script / Module:** top-level variables of the file.
- **Global:** the `window` object.

You can expand objects there and also double-click a value to change it.

## 28: What does the Call Stack section of the debugger show?

It shows the chain of function calls that led to the current paused line, with the current function at the top. Clicking a frame moves the editor and the Scope section to that function, so you can see the values of variables in the caller at the moment of the call.

## 29: What are watch expressions?

Watch expressions are expressions you add in the Watch section of the debugger. DevTools evaluates them every time the debugger pauses, so you can follow a value as you step through code.

For example you can watch `cart.items.length` or `user?.role` without expanding objects in the Scope section each time.

## 30: How do you pause on exceptions?

In the Breakpoints section of the Sources panel there are two checkboxes: "Pause on uncaught exceptions" and "Pause on caught exceptions". When an exception is thrown, the debugger pauses at the exact line that threw it, with all variables still available.

This is often faster than reading the stack trace, because you see the state that caused the error.

## 31: What is a source map?

A source map is a file (usually `.map`) that connects the code the browser runs (minified, bundled or compiled) back to your original source files. With a source map, DevTools shows your original TypeScript, JSX or SCSS, and stack traces point to the original lines.

The compiled file points to its map with a comment at the end:

```js
//# sourceMappingURL=main.js.map
```

## 32: Why do you need source maps?

Production code is usually minified and bundled, so an error might point to `main.3f9a1.js:1:48213`, which is useless. Source maps translate that position back to something like `src/cart/total.ts:27:10`.

They also let you set breakpoints in your original code during development, even though the browser runs transformed code.

## 33: What is minification and why does it make debugging harder?

Minification removes whitespace and comments, shortens variable names and rewrites code to make files smaller. After it, the code is usually one long line with names like `a`, `b`, `t`, so stack traces and breakpoints become very hard to read.

DevTools has a "pretty print" button (`{}`) that formats minified code, but variable names stay short. Source maps are the real fix.

## 34: What is the Elements panel used for?

The Elements panel shows the live DOM of the page (not the original HTML source) and the CSS applied to the selected element. You can:

- Edit HTML, attributes and text.
- Add, change or disable CSS rules in the Styles pane.
- See the final computed values in the Computed pane.
- See the box model (margin, border, padding, size).
- See event listeners and properties of the element.

## 35: What is the difference between the DOM in the Elements panel and View Source?

View Source (`Ctrl+U`) shows the HTML exactly as the server sent it. The Elements panel shows the current DOM, after the browser parsed the HTML, fixed invalid markup, and after JavaScript added, removed or changed elements.

If something is in Elements but not in View Source, it was added by JavaScript. This matters for single page apps and for SEO checks.

## 36: How do you inspect an element on the page?

Right-click the element and choose "Inspect", or open DevTools and use the element picker (the arrow icon or `Ctrl+Shift+C`), then click the element. DevTools selects it in the Elements panel and shows its styles.

## 37: How do you check which CSS rules apply to an element?

Select the element in the Elements panel and look at the Styles pane. It shows every rule that matches, with the winning rules at the top. Properties that are overridden by another rule are crossed out. Invalid properties or values have a warning icon.

The Computed pane shows the final value of each property and, when expanded, which rule it came from.

## 38: What does it mean when a CSS property is crossed out in the Styles pane?

It means the property is overridden: another rule with higher priority (a more specific selector, a later rule, `!important`, or an inline style) sets the same property, so this value is not used.

If it is grayed out with an info icon instead, the property has no effect in this situation, for example `justify-content` on an element that isn't a flex or grid container. Hovering over the icon explains why.

## 39: What is the Computed pane?

The Computed pane in the Elements panel shows the final value the browser uses for each CSS property of the selected element, after the cascade, inheritance and unit conversion. For example `width: 50%` becomes a value like `600px`.

Expanding a property shows which rule set it, which helps when you can't tell from the Styles pane where a value comes from.

## 40: What is the box model view in DevTools?

In the Computed pane (and at the bottom of the Styles pane in Chrome), DevTools shows a diagram with the element's content size, padding, border and margin. You can double-click values to edit them.

Hovering over an element in the Elements panel also highlights its margin, padding and content on the page in different colors.

## 41: What is CSS specificity?

Specificity is the rule browsers use to decide which CSS selector wins when several rules set the same property on the same element. It is counted as three numbers (A, B, C):

- **A:** ID selectors.
- **B:** classes, attributes and pseudo-classes.
- **C:** element types and pseudo-elements.

`#nav .link` (1,1,0) beats `.menu .link` (0,2,0). Inline styles beat all of these, and `!important` beats normal declarations. If specificity is equal, the rule that comes later wins.

## 42: How can you see the specificity of a selector in DevTools?

In Chrome, hover over a selector in the Styles pane. A tooltip shows its specificity, for example `Specificity: (0,2,1)`. This is the fastest way to see why one rule beats another.

## 43: How do you force a CSS state like hover or focus in DevTools?

Select the element, then click `:hov` in the Styles pane and check `:hover`, `:active`, `:focus`, `:focus-within`, `:focus-visible`, `:visited` or `:target`. The element then stays in that state so you can inspect its styles without keeping the mouse on it.

## 44: What is the Network panel used for?

The Network panel records every request the page makes: HTML, scripts, styles, images, fonts, `fetch` and XHR calls, WebSocket connections. For each request you can see the URL, method, status, size, timing, request and response headers, payload and response body.

It is the main tool when data doesn't load, an API returns an error, or the page loads slowly.

## 45: How do you see only API calls in the Network panel?

Click the "Fetch/XHR" filter in the Network panel toolbar. You can also type in the filter box, for example `/api/` to show only URLs that contain it, or use properties like `status-code:500` or `method:POST`.

## 46: What do HTTP status codes 4xx and 5xx mean?

- **4xx** are client errors: the request was wrong in some way. Common ones: `400` bad request, `401` not authenticated, `403` not allowed, `404` not found, `409` conflict, `422` validation failed, `429` too many requests.
- **5xx** are server errors: the request may be fine but the server failed. Common ones: `500` internal error, `502` bad gateway, `503` service unavailable, `504` gateway timeout.

A 4xx usually means fixing the front-end request. A 5xx usually means checking server logs.

## 47: What is the difference between 401 and 403?

`401 Unauthorized` means the server doesn't know who you are: no credentials, or expired or invalid ones. Logging in or refreshing the token should fix it.

`403 Forbidden` means the server knows who you are, but you are not allowed to do this. Logging in again won't help; it is a permissions issue.

## 48: What does a red or failed request in the Network panel mean?

A red request either got an error status (4xx or 5xx) or didn't get a normal HTTP response at all. In the second case the status shows "(failed)", "(blocked)" or "CORS error". Causes include: the server could not be reached, DNS failed, the connection was reset, the request was blocked by CORS, by an ad blocker or by CSP, it was cancelled (for example by navigating away or `AbortController`), or it was blocked as mixed content.

Hover over the status or check the Console; it usually tells you the exact reason, like `net::ERR_BLOCKED_BY_CLIENT` or a CORS error message.

## 49: What does "Preserve log" do in the Network and Console panels?

By default, DevTools clears the Network log and the Console when the page navigates or reloads. "Preserve log" keeps the entries across navigations.

You need it when debugging redirects, login flows, form submits that reload the page, or errors that happen right before a navigation.

## 50: What does "Disable cache" do in the Network panel?

When checked, the browser doesn't use its HTTP cache for requests while DevTools is open. Every reload fetches fresh files, so you see the latest version and the real first-visit load time.

It doesn't bypass service worker caches. For those, use "Bypass for network" in Application, then Service workers.

## 51: What is a hard reload?

A hard reload (`Ctrl+Shift+R` or `Shift+F5`, `Cmd+Shift+R` on Mac) reloads the page and asks the server for fresh copies instead of using the cache for the main resources. In Chrome, with DevTools open, you can also right-click the reload button and choose "Empty cache and hard reload".

Use it when you suspect you are seeing an old version of a file.

## 52: What is CORS?

CORS (Cross-Origin Resource Sharing) is a browser rule that controls whether JavaScript on one origin (scheme + host + port) can read responses from another origin. The server allows it by sending headers like `Access-Control-Allow-Origin`.

If the server doesn't send the right headers, the browser blocks your code from reading the response and shows a CORS error in the console. CORS is enforced by the browser, so the same request works fine from curl or Postman.

## 53: How do you recognize a CORS error?

The console shows a message like:

```
Access to fetch at 'https://api.example.com/data' from origin 'https://app.example.com'
has been blocked by CORS policy: No 'Access-Control-Allow-Origin' header is present
on the requested resource.
```

In JavaScript, `fetch` rejects with a generic `TypeError: Failed to fetch`, and you can't read the status code. In the Network panel the status shows "CORS error".

## 54: What is the Application panel?

The Application panel in Chrome DevTools shows storage and app features of the page:

- Cookies, Local storage, Session storage, IndexedDB, Cache storage.
- Service workers and the web app manifest.
- Storage usage and a "Clear site data" button.
- Back/forward cache status, background services and more.

You can view, edit and delete stored values there.

## 55: How do you view and edit cookies in DevTools?

Open the Application panel, expand "Cookies" and click the site. You see each cookie's name, value, domain, path, expiry, size and flags like `HttpOnly`, `Secure`, `SameSite` and `Partitioned`. You can double-click to edit a value or delete cookies.

The Network panel also shows which cookies a request sent and which ones the response set, in the request's Cookies tab.

## 56: What is the difference between localStorage and sessionStorage when debugging?

Both store string key/value pairs for an origin. `localStorage` stays until it is cleared. `sessionStorage` lives only for the current tab and is cleared when the tab is closed; each tab has its own copy.

A common bug: data saved in `sessionStorage` is missing when a user opens a link in a new tab. Another: objects saved without `JSON.stringify` are stored as `"[object Object]"`.

## 57: How do you clear all site data while debugging?

In Chrome, open Application, then "Storage", and click "Clear site data". It removes cookies, local and session storage, IndexedDB, cache storage and unregisters service workers for that origin. You can choose which types to clear.

You can also test a clean first visit with an Incognito window.

## 58: What is a TypeError in JavaScript?

A `TypeError` is thrown when a value is not of the type an operation needs. The most common cases:

```js
const user = undefined;
user.name; // TypeError: Cannot read properties of undefined (reading 'name')

const n = 5;
n(); // TypeError: n is not a function

const x = null;
x.push(1); // TypeError: Cannot read properties of null (reading 'push')
```

It also happens when you assign to a `const` variable or change a frozen object in strict mode.

## 59: What is a ReferenceError?

A `ReferenceError` happens when you use a variable that doesn't exist in the current scope, or use a `let`/`const` variable before its declaration (the temporal dead zone).

```js
console.log(totl); // ReferenceError: totl is not defined (typo)

console.log(count); // ReferenceError: Cannot access 'count' before initialization
let count = 1;
```

## 60: What is a SyntaxError and when do you see it?

A `SyntaxError` means the code (or data) can't be parsed. In your own code, the build or browser reports it before the code runs. At runtime the most common one comes from `JSON.parse` (or `res.json()`) on text that isn't valid JSON:

```js
JSON.parse("<!DOCTYPE html>...");
// SyntaxError: Unexpected token '<', "<!DOCTYPE "... is not valid JSON
```

That message usually means the API returned an HTML page (an error page or the app's index.html) instead of JSON.

## 61: What does "Cannot read properties of undefined" mean and how do you fix it?

It means you tried to read a property from a value that is `undefined`. The property name in the message tells you what you tried to read, so the value before that property is the one that is `undefined`.

To fix it, find out why the value is missing: data not loaded yet, wrong property name, an API response with a different shape, or an array index out of range. Guard where it is valid for the value to be missing:

```js
const city = user?.address?.city ?? "Unknown";
```

Don't add `?.` everywhere just to hide the error. If the value should always exist, fix the cause.

## 62: What does "x is not a function" mean?

It means you tried to call something that isn't a function. Common causes:

- A typo or wrong method name.
- Calling a method on the wrong type (`"abc".map(...)`).
- Wrong import: a default vs named import mismatch, so the imported value is `undefined` or an object.
- A variable that was overwritten with a non-function value.
- Calling a method from a library version that doesn't have it.

## 63: What is an unhandled promise rejection?

It happens when a promise rejects and no code handles the rejection with `.catch()`, `try/catch` around `await`, or a second argument to `.then()`. The browser logs `Uncaught (in promise)` with the error.

```js
async function load() {
  const res = await fetch("/api/data");
  if (!res.ok) throw new Error(`HTTP ${res.status}`);
  return res.json();
}

load(); // if it throws, nobody handles it -> unhandled rejection
load().catch((err) => showError(err)); // handled
```

## 64: Why doesn't fetch throw an error for a 404 or 500 response?

`fetch` only rejects when the request can't complete at all (network error, CORS block, abort). A response with status 404 or 500 is still a completed HTTP exchange, so the promise resolves. You have to check `res.ok` or `res.status` yourself.

```js
const res = await fetch("/api/user");
if (!res.ok) {
  throw new Error(`Request failed with ${res.status}`);
}
const user = await res.json();
```

Forgetting this is a very common source of confusing bugs later in the code.

## 65: What is the difference between null and undefined when debugging?

`undefined` usually means a value was never set: a missing property, a function with no `return`, a variable with no value. `null` is usually set on purpose to mean "no value".

The one you see in an error hints at the cause. `undefined` often points to a typo, wrong property name or data not loaded yet. `null` often comes from APIs like `document.querySelector` finding nothing, or a server sending `null`.

## 66: Why does document.querySelector return null?

It returns `null` when no element matches the selector at the moment it runs. Common causes:

- The script runs before the element exists (in `<head>` without `defer`).
- A typo in the selector, or a missing `.` or `#`.
- The element is rendered later by a framework or after data loads.
- The element is inside a shadow root or an iframe.

Use `defer` or `type="module"` on scripts, run code after the element is rendered, and test the selector in the console with `$()`.

## 67: What is event bubbling?

When an event happens on an element, it first runs handlers on that element, then on its parent, then on the grandparent and so on up to `document` and `window`. This is bubbling.

It is why a click on a button inside a card also triggers a click handler on the card. Most events bubble. Some, like `focus`, `blur`, `mouseenter` and `mouseleave`, do not (`focusin` and `focusout` are the bubbling versions of focus and blur).

## 68: What is the difference between event.target and event.currentTarget?

`event.target` is the element where the event started, for example the icon inside a button that you actually clicked. `event.currentTarget` is the element whose handler is running right now, the one you called `addEventListener` on.

A common bug is using `event.target` and getting a child element instead of the button you expected.

```js
button.addEventListener("click", (e) => {
  console.log(e.target); // could be the <svg> icon inside
  console.log(e.currentTarget); // always the button
});
```

## 69: What is the difference between stopPropagation and preventDefault?

- `event.stopPropagation()` stops the event from reaching other elements (parents when bubbling). It does not stop the browser's default action.
- `event.preventDefault()` stops the browser's default action, like following a link, submitting a form or checking a checkbox. It does not stop bubbling.

Mixing them up is a common bug, for example calling `stopPropagation` and wondering why a form still submits.

## 70: How do you see the event listeners on an element?

Select the element in the Elements panel and open the "Event Listeners" tab. It lists listeners grouped by event type, including listeners on ancestors (unless you uncheck "Ancestors"). Clicking the file link jumps to the handler's code.

In the console, Chrome also has `getEventListeners($0)`, which returns the listeners on the selected element.

## 71: What is a closure and how can it cause bugs?

A closure is a function that remembers variables from the scope where it was created. Bugs happen when the function keeps an old value while you expect the current one, or when variables are shared in a way you didn't expect.

The classic example with `var` in a loop:

```js
for (var i = 0; i < 3; i++) {
  setTimeout(() => console.log(i), 0);
}
// prints 3, 3, 3 because all callbacks share one i

for (let i = 0; i < 3; i++) {
  setTimeout(() => console.log(i), 0);
}
// prints 0, 1, 2 because let creates a new i for each iteration
```

## 72: What is a memory leak in a web page?

A memory leak is memory the page no longer needs but can't free, because something still holds a reference to it. Over time memory use grows, the page gets slower, and the tab may crash.

Common causes in front-end code: event listeners not removed, timers not cleared, DOM nodes removed from the page but still referenced by JavaScript, caches or arrays that only grow, and subscriptions that are never closed.

## 73: How do you notice a memory leak?

Signs include the page getting slower the longer it is open, the tab crashing after a while, or memory growing after repeating the same action (like opening and closing a modal).

To check, open Chrome's Task Manager (`Shift+Esc` on Windows/Linux, or the Chrome menu, then More tools, then Task manager), repeat the action several times, force garbage collection in the Memory panel, and see if memory goes back down. If it keeps climbing, take heap snapshots.

## 74: What is the Memory panel in Chrome DevTools?

The Memory panel helps you find memory problems. It has three main tools:

- **Heap snapshot:** a full picture of JavaScript objects and DOM nodes in memory at one moment.
- **Allocations on timeline:** records allocations over time, so you can see which ones were not freed.
- **Allocation sampling:** a low-overhead view of which functions allocate the most memory.

## 75: What is the Performance panel used for?

The Performance panel records what the browser does over time: JavaScript execution, style calculation, layout, paint, network, frames and user interactions. It shows a flame chart of the main thread so you can see which functions take time.

You use it for slow loading, janky scrolling or animations, and slow responses to clicks and typing. It also shows Core Web Vitals (LCP, INP, CLS) for the recording and live for your own interactions.

## 76: What is a long task?

A long task is any task on the main thread that takes more than 50 ms. While it runs, the browser can't respond to clicks, typing or scrolling, so the page feels frozen or laggy.

In the Performance panel, long tasks are marked with a red triangle and red stripes on the part after 50 ms.

## 77: What is jank?

Jank is visible stutter: scrolling, animations or typing that skip frames instead of moving smoothly. The browser aims to draw a new frame about every 16.7 ms on a 60 Hz screen. If the main thread is busy longer than that, frames are dropped.

Causes include long JavaScript tasks, expensive layout or paint, and animating properties that trigger layout.

## 78: What are Core Web Vitals?

Core Web Vitals are three metrics Google uses to measure user experience:

- **LCP (Largest Contentful Paint):** how fast the main content appears. Good: 2.5 s or less.
- **INP (Interaction to Next Paint):** how fast the page responds to user input. Good: 200 ms or less.
- **CLS (Cumulative Layout Shift):** how much the layout jumps around. Good: 0.1 or less.

They are measured at the 75th percentile of real user visits.

## 79: What is Lighthouse?

Lighthouse is an automated tool that audits a page for performance, accessibility, best practices and SEO, and gives a score with a list of problems and suggestions. It runs in Chrome DevTools (Lighthouse panel), from the command line, in CI, and powers PageSpeed Insights.

It is a lab test with simulated conditions, so its results can differ from what real users experience.

## 80: What is React DevTools?

React DevTools is a browser extension that adds two tabs to DevTools:

- **Components:** shows the React component tree, with props, state, hooks and context of the selected component. You can edit values live.
- **Profiler:** records renders so you can see which components rendered, how long they took, and why.

It works best with development builds. In production builds component names may be minified and profiling is off unless you use React's profiling build.

## 81: How do you find which React component renders a DOM element?

In the Components tab of React DevTools, click the element picker and click the element on the page, or select an element in the Elements panel and switch to the Components tab. The matching component is selected, with its props and state.

## 82: What is Angular DevTools?

Angular DevTools is a browser extension for debugging Angular apps. It has:

- **Components:** the component tree, with inputs, outputs, properties and signals of the selected component. You can edit values.
- **Profiler:** records change detection cycles and shows which components were checked and how long each took.
- **Injector tree:** shows the dependency injection hierarchy and providers.

It works with apps running in development mode.

## 83: What is a hydration error?

Hydration is when a framework attaches JavaScript to HTML that was rendered on the server. A hydration error happens when the HTML the client renders doesn't match the HTML the server sent.

Common causes are using `Date.now()`, `Math.random()`, `window` or `localStorage` during render, invalid HTML nesting (like a `<div>` inside a `<p>`), and browser extensions that change the DOM before hydration.

## 84: What is Redux DevTools?

Redux DevTools is a browser extension that shows every action dispatched to a store, the state before and after, and the difference between them. You can jump back to an earlier state (time travel), replay actions, and export or import state.

It works with Redux Toolkit out of the box, and also with NgRx (through `@ngrx/store-devtools`) and Zustand (through its `devtools` middleware).

## 85: How does TypeScript help prevent bugs?

TypeScript adds static types to JavaScript. The compiler checks that values are used correctly before the code runs, so many bugs, like calling a method that doesn't exist, passing the wrong argument type, or forgetting that a value can be `undefined`, show up in the editor or the build instead of in production.

Types are removed at build time, so TypeScript doesn't check data at runtime. Data from APIs still needs runtime validation (for example with Zod) if you can't trust it.

## 86: How do you read a TypeScript error message?

Start with the first line: it tells you what type was given and what type was expected, for example:

```
Type 'string | undefined' is not assignable to type 'string'.
  Type 'undefined' is not assignable to type 'string'.
```

For long messages, read the last indented line too; it is usually the most specific mismatch. Then hover over the variables in the editor to see their actual types.

## 87: What is a bundler?

A bundler takes your source files (JavaScript, TypeScript, CSS, images) and their imports, and produces optimized files the browser can load. Examples are webpack, Vite, Rollup, Rolldown, esbuild, Turbopack and Rspack.

Many front-end bugs come from the build: wrong module resolution, a missing polyfill, an environment variable that wasn't replaced, or code that was removed by tree shaking.

## 88: What is the difference between a dev server and a production build?

A dev server (like `vite` or `next dev`) serves your code with fast rebuilds, hot module replacement, readable code, source maps and extra framework warnings. A production build minifies code, removes dev-only checks, splits bundles and may run code differently (for example React StrictMode checks only run in development).

Some bugs only appear in production builds, so test a production build locally (`vite build` then `vite preview`, or `next build` then `next start`) before shipping.

## 89: What is hot module replacement (HMR)?

HMR updates changed modules in the running page without a full reload, keeping state like form inputs or the current route. It makes development faster.

It can also cause confusing bugs: old event listeners or timers from the previous version of a module may still run, or state gets out of sync. If something behaves strangely during development, do a full reload before you start debugging.

## 90: What is cross-browser testing?

Cross-browser testing means checking that your site works in the browsers your users use: Chrome, Edge, Firefox and Safari, on desktop and mobile. They use different engines (Blink, Gecko, WebKit), so CSS, JavaScript APIs, form controls and media can behave differently.

On iOS, browsers outside the EU all use WebKit, so iPhone bugs usually need testing in Safari.

## 91: How do you check if a browser supports a feature?

Look it up on caniuse.com or MDN's browser compatibility tables. Also check the Baseline status shown on MDN and web.dev, which says whether a feature works in all major browsers.

In code, use feature detection instead of checking the browser name:

```js
if ("IntersectionObserver" in window) {
  // use it
}

if (CSS.supports("container-type: inline-size")) {
  // container queries are supported
}
```

## 92: What is device mode in Chrome DevTools?

Device mode (the phone and tablet icon, or `Ctrl+Shift+M`) lets you see the page at different screen sizes, with device presets, touch emulation, device pixel ratio and user agent changes. It is good for checking responsive layouts quickly.

It does not emulate the real device's browser engine, CPU or memory. For real mobile bugs, test on an actual device.

## 93: What is remote debugging?

Remote debugging means using DevTools on your computer to debug a page running on another device, usually a phone.

- **Android Chrome:** enable USB debugging on the phone, connect it, then open `chrome://inspect` on your computer.
- **iOS Safari:** enable Web Inspector in the iPhone's Safari settings (Advanced), connect it to a Mac, and use the Develop menu in desktop Safari.

## 94: What is the accessibility tree?

The accessibility tree is a version of the DOM that browsers give to assistive technology like screen readers. Each node has a role (button, link, heading), a name (the label a screen reader reads), states (checked, expanded) and other properties.

You can see it in Chrome DevTools in the Elements panel's Accessibility pane, or switch on the full-page accessibility tree view.

## 95: How do you find accessibility problems quickly?

- Run Lighthouse's accessibility audit, or a tool like axe DevTools.
- Check color contrast in the Elements panel's color picker.
- Use the page with only the keyboard (`Tab`, `Shift+Tab`, `Enter`, `Space`, arrow keys).
- Look at the Accessibility pane for missing names or wrong roles.
- Try a screen reader (VoiceOver on Mac/iOS, NVDA on Windows, TalkBack on Android).

Automated tools catch only some problems, so keyboard and screen reader checks are still needed.

## 96: What is CSP and how does it show up while debugging?

CSP (Content Security Policy) is an HTTP header that tells the browser which sources of scripts, styles, images and other resources are allowed. When something breaks the policy, the browser blocks it and logs an error in the console like:

```
Refused to load the script 'https://cdn.example.com/x.js' because it violates
the following Content Security Policy directive: "script-src 'self'".
```

The message tells you what was blocked and which directive blocked it.

## 97: What is mixed content?

Mixed content is when an HTTPS page loads resources over plain HTTP. Browsers block scripts, iframes, styles and `fetch` calls over HTTP on HTTPS pages, and upgrade images, audio and video to HTTPS (blocking them if that fails). The console shows a "Mixed Content" warning or error.

The fix is to load everything over HTTPS.

## 98: What is the SameSite cookie attribute?

`SameSite` controls when the browser sends a cookie on requests coming from other sites:

- `Strict`: only sent on same-site requests.
- `Lax`: also sent on top-level navigations from other sites (clicking a link), but not on cross-site `fetch` or iframes. Chrome treats cookies without `SameSite` as `Lax`.
- `None`: sent on all requests, but only if the cookie is also `Secure`.

A cookie that "disappears" on cross-site requests is often a `SameSite` issue.

## 99: What is a third-party script?

A third-party script is JavaScript loaded from another company's server: analytics, ads, chat widgets, A/B testing, tag managers, payment forms. You don't control its code, it can change without notice, and it can slow your page, throw errors, or break your layout.

When debugging, use request blocking in DevTools to check if a problem goes away without a specific third-party script.

## 100: What is a service worker?

A service worker is a script that runs in the background, separate from the page, and can intercept network requests from pages in its scope. It is used for offline support, caching and push notifications.

It is also a common source of "I deployed but users still see the old version" bugs, because it can keep serving cached files.

## 101: How do you debug a service worker in Chrome?

Open Application, then "Service workers". There you can see the registered worker and its status, click "Update" or "Unregister", check "Update on reload" (always install the new version on reload), check "Bypass for network" (skip the worker for requests), and click the source link to debug its code.

`chrome://serviceworker-internals` shows all service workers across sites.

## 102: What is a Web Worker?

A Web Worker runs JavaScript on a background thread, separate from the main thread. It can't touch the DOM, and it talks to the page with `postMessage`. It is used for heavy work like parsing large files or calculations, so the page stays responsive.

In DevTools, workers appear as separate threads in the Sources panel and in the console's context dropdown.

## 103: What is a flaky test?

A flaky test is a test that sometimes passes and sometimes fails without any code change. Common causes are timing (waiting for fixed delays, animations, network), shared state between tests, test order dependency, random data, dates and time zones, and unstable selectors.

Flaky tests are dangerous because people start ignoring failures.

## 104: What are Jest and Vitest?

Jest and Vitest are JavaScript test runners. They find test files, run them, provide `describe`, `it`/`test` and `expect`, and support mocking. Vitest has an API mostly compatible with Jest, but it uses Vite's config and transform pipeline, so it fits Vite projects well and is usually faster.

Both usually run component tests in Node.js with a fake DOM (jsdom or happy-dom). Vitest also has a browser mode that runs tests in a real browser.

## 105: How do you run a single test while debugging?

Use `.only` on a test or describe block, or filter by name or file from the command line:

```js
it.only("adds an item to the cart", () => {
  // ...
});
```

```bash
npx vitest run cart.test.ts -t "adds an item"
npx jest cart.test.ts -t "adds an item"
```

Remember to remove `.only` before committing. Lint rules like `no-only-tests` help, and Vitest fails on `.only` in CI by default.

## 106: What is Sentry?

Sentry is an error monitoring service. Its SDK catches errors and unhandled promise rejections in your app and sends them to Sentry with the stack trace, browser, URL, user (if you set it), and breadcrumbs (clicks, navigation, network calls and console logs before the error). It groups similar errors and uses uploaded source maps to show original code.

It also has performance tracing and session replay. Alternatives include Datadog, New Relic, Bugsnag, Rollbar, and OpenTelemetry-based tools.

## 107: What is window.onerror?

`window.onerror` is a global handler called when a JavaScript error isn't caught anywhere. It receives the message, the source URL, line, column and the error object. `window.addEventListener("error", ...)` is the more flexible version.

```js
window.addEventListener("error", (event) => {
  reportError({
    message: event.message,
    source: event.filename,
    line: event.lineno,
    stack: event.error?.stack,
  });
});
```

It doesn't catch promise rejections. For those you need the `unhandledrejection` event.

## 108: What is an error boundary in React?

An error boundary is a component that catches errors thrown while rendering its children, shows a fallback UI, and lets the rest of the app keep working. Without one, an error during render unmounts the whole React tree and leaves a blank page.

Error boundaries are class components with `static getDerivedStateFromError` and/or `componentDidCatch`, or you can use the `react-error-boundary` package. They don't catch errors in event handlers or async code outside rendering.

## 109: What is session replay?

Session replay records what users do on your site (DOM changes, clicks, scrolling, inputs) so you can play it back like a video. It helps you see the steps that led to a bug a user reported, without having to guess.

Tools include Sentry Session Replay, LogRocket, FullStory, Microsoft Clarity and others. Sensitive data like passwords and personal details must be masked.

## 110: What is RUM (Real User Monitoring)?

RUM means collecting performance and error data from real users' browsers, instead of only lab tests. It shows how the site works on real devices and networks, for example Core Web Vitals at the 75th percentile, slow pages, errors by browser, and regions with bad performance.

You can build it with the `web-vitals` library and your own endpoint, or use tools like Sentry, Datadog RUM, New Relic, or Vercel Speed Insights. Google's CrUX dataset is public RUM data for popular sites.

## 111: What is a feature flag?

A feature flag is a switch that turns a feature on or off at runtime without a new deploy. It can be on for some users (by percentage, region, account) and off for others.

For debugging, flags let you turn off a broken feature quickly in production, and they also explain bugs that only some users see. Include the active flags in error reports.

## 112: How do you debug JavaScript in VS Code?

VS Code has a built-in JavaScript debugger. You can:

- Create a `launch.json` with a `chrome` or `msedge` configuration that opens your dev server URL, then set breakpoints in your source files in VS Code.
- Use the "JavaScript Debug Terminal" to debug any Node.js process started from it, like test runners or Next.js server code.
- Attach to a running browser or Node process.

You get breakpoints, watch expressions, the call stack and a debug console inside the editor.

## 113: What is Puppeteer?

Puppeteer is a Node.js library from the Chrome team that controls Chrome (and Firefox) through code. You can open pages, click, type, take screenshots, make PDFs, read console messages, record performance traces and intercept network requests.

It is useful for automating reproduction steps and for scraping or testing. Playwright is a similar tool that supports Chromium, Firefox and WebKit and is more common for end-to-end tests.

## 114: What is the Chrome DevTools Protocol (CDP)?

CDP is the protocol DevTools itself uses to talk to Chrome. It is split into domains like `Page`, `Network`, `Runtime`, `Debugger`, `DOM` and `Performance`, each with commands and events.

Tools like Puppeteer, Playwright (for Chromium), Lighthouse and the Chrome DevTools MCP server use CDP. You can use it directly to do things not available in higher-level APIs.

## 115: What AI features does Chrome DevTools have for debugging?

Recent Chrome versions include AI assistance in DevTools (when enabled and available in your region and account):

- **Console insights:** explains a console error or warning and suggests fixes.
- **AI assistance panel:** you can ask questions about a selected element and its styles, a network request, a source file, or a performance trace, and it can suggest and apply CSS changes.

There is also the Chrome DevTools MCP server, which lets AI coding agents open a page, read the console and network, and record traces. Always check AI suggestions yourself; they can be wrong.

## 116: What is rubber duck debugging?

Rubber duck debugging means explaining your code, line by line, to someone or something (even a rubber duck) that knows nothing about it. Saying out loud what each part should do often makes you notice where your assumption is wrong.

It works because it forces you to slow down and check details you would normally skip.

## 117: What does it mean to debug by bisecting?

Bisecting means cutting the search space in half again and again. You can do it with:

- **Code:** comment out half of the suspicious code, see if the bug remains, then narrow down.
- **History:** use `git bisect` to find the commit that introduced the bug.
- **Data:** remove half of the input data to find the record that breaks things.
- **Dependencies or extensions:** disable half of them at a time.

It finds the cause in a few steps, even in a large search space.

## 118: What is git bisect?

`git bisect` helps find the commit that introduced a bug using binary search. You mark a commit where the bug exists (bad) and one where it didn't (good). Git checks out a commit in the middle, you test and mark it, and it repeats until it finds the first bad commit.

```bash
git bisect start
git bisect bad            # current commit has the bug
git bisect good v2.3.0    # this release was fine
# test, then run: git bisect good  or  git bisect bad
git bisect reset          # when done
```

You can automate it with `git bisect run <test command>`.

## 119: Why should you read the error message carefully before searching online?

The error message often tells you exactly what's wrong: which value is undefined, which file is missing, which header is not allowed. Many developers skip it and start guessing or copying fixes from the internet that don't match their case.

Read the full message, note the file and line, and only then search for it if it's still unclear.

## 120: What is the difference between a bug and a regression?

A bug is any case where the software doesn't behave as intended. A regression is a bug in a feature that used to work and was broken by a later change.

Regressions are often easier to find, because you can compare the working and broken versions, for example with `git bisect` or by looking at recent changes and dependency updates.

## 121: Why do you check the browser console first when a page breaks?

The console shows uncaught JavaScript errors, failed resource loads, CORS and CSP blocks, framework warnings (like React or Angular dev warnings) and deprecation messages. Most page-breaking bugs leave a message there, often with a link to the exact line.

It takes a few seconds and often points you straight to the problem.

## 122: How do you filter messages in the console?

- Use the log levels dropdown (Verbose, Info, Warnings, Errors).
- Type text in the filter box. Prefix with `-` to hide matching messages, or use `/regex/`.
- Use the console sidebar to show messages by type or source.
- Right-click a message and choose "Hide messages from <file>" to hide a noisy script.
- Enable "Selected context only" to show messages from the current frame or worker.

## 123: What is the Snippets feature in the Sources panel?

Snippets are small scripts saved in DevTools that you can run on any page. Open Sources, then the Snippets tab, create one, and run it with `Ctrl+Enter`. You can also run a snippet from the Command Menu by typing `!` and the snippet name.

They are useful for repeated tasks like clearing specific storage, finding images without `alt`, or logging layout shifts.

## 124: What is the Command Menu in Chrome DevTools?

The Command Menu is opened with `Ctrl+Shift+P` (`Cmd+Shift+P` on Mac). You type the name of any DevTools action, like "Show Rendering", "Capture full size screenshot", "Disable JavaScript", or "Show Coverage", and run it. It is the quickest way to find features without knowing which menu they are in.

## 125: How do you take a screenshot of a whole page in Chrome DevTools?

Open the Command Menu (`Ctrl+Shift+P`) and run "Capture full size screenshot". You can also right-click a node in the Elements panel and choose "Capture node screenshot". In device mode, the three-dot menu has screenshot options too.

## 126: How do you edit a page's JavaScript or CSS and keep the changes after reload?

Use Local Overrides in the Sources panel. Choose a folder for overrides and allow access. Then edits you make to files in Sources or styles in Elements are saved locally, and DevTools serves your local copy instead of the network file on reload.

You can also override response headers. It is useful for testing a fix on a production site where you can't deploy.

## 127: What is the difference between Local Overrides and Workspaces?

Local Overrides save modified copies of files from any site into a local folder, and serve them instead of the real files. They don't change your project.

Workspaces connect DevTools to your actual project folder, so edits in DevTools are saved to your real source files. Overrides are for sites you don't control; Workspaces are for your own local project.

## 128: How do you simulate a slow network?

In the Network panel, open the throttling dropdown ("No throttling") and pick a preset like "Fast 4G", "Slow 4G" or "3G", or "Offline". You can also create custom profiles with your own download, upload and latency values.

The Performance panel has the same network setting plus CPU throttling, which matters because many users have slower phones than your laptop.

## 129: How do you test what happens when the user goes offline?

Choose "Offline" in the Network panel's throttling dropdown, or check "Offline" in Application, then Service workers. Then try actions that need the network to see how the app handles it: error messages, retry, cached data, or service worker offline pages.

You can also listen to the `online` and `offline` events in code, but note that `navigator.onLine` being `true` doesn't guarantee a working connection.

## 130: What is request blocking in DevTools?

Request blocking lets you stop specific URLs or patterns from loading. Right-click a request in the Network panel and choose "Block request URL" or "Block request domain", or open the "Request blocking" drawer tab and add patterns like `*analytics*`.

It is useful to check if a third-party script causes a bug, to test fallbacks when a CDN fails, and to see how much a resource affects load time.

## 131: What is a HAR file?

A HAR (HTTP Archive) file is a JSON file that contains the requests recorded in the Network panel: URLs, headers, bodies, timings and cookies. You export it from the Network panel with the download icon.

Support teams often ask users for a HAR file to see the network side of a bug. Be careful: HAR files can contain cookies, tokens and personal data. Chrome exports a sanitized version by default and has a separate option to export with sensitive data.

## 132: How do you copy a network request to run it outside the browser?

Right-click the request in the Network panel and choose "Copy", then "Copy as cURL" (or "Copy as fetch", "Copy as fetch (Node.js)", "Copy as PowerShell"). You get a command with the same URL, method, headers and body.

It is useful to check if the server behaves the same outside the browser, or to share an exact request with a back-end developer. Remember that it includes cookies and auth headers.

## 133: How do you see a request's response body in DevTools?

Click the request in the Network panel. The "Preview" tab shows a formatted version (JSON as a tree, images rendered), and the "Response" tab shows the raw text. The "Payload" tab shows what was sent: query parameters and the request body.

If the response is missing, the request may have failed, been a redirect, or the page navigated away (enable "Preserve log").

## 134: What is the Timing tab in the Network panel?

It shows how long each phase of a request took:

- **Queueing / Stalled:** waiting before the request could start.
- **DNS lookup, Initial connection, SSL:** connection setup.
- **Request sent.**
- **Waiting for server response:** time until the first byte arrived (TTFB).
- **Content download.**

A long wait points to a slow server. Long stalled or queueing time points to too many requests at once, low priority, or waiting for a connection.

## 135: What is the Initiator column in the Network panel?

The Initiator column shows what started a request: the HTML parser, a script with a line number, a CSS file, a redirect, or a preflight. Hovering over it shows the full call stack for requests started by JavaScript.

It answers the question "who is making this request?", which is useful for duplicate or unexpected requests.

## 136: How do you debug a failing form submission?

1. Open the Network panel with "Preserve log" checked, since forms often reload the page.
2. Submit the form and find the request.
3. Check the URL, method, and the Payload tab to see what data was actually sent.
4. Check the status and response for server validation errors.
5. If no request was sent, check the console for errors, and check for `preventDefault()` or HTML validation (`required`, `pattern`) blocking the submit.

## 137: What are DOM breakpoints?

DOM breakpoints pause the debugger when a specific element changes. Right-click an element in the Elements panel, choose "Break on", and pick:

- **Subtree modifications:** a child is added, removed or changed.
- **Attribute modifications:** an attribute (like `class` or `style`) changes.
- **Node removal:** the element is removed.

The debugger stops on the JavaScript line that made the change, which is great when you don't know which code is changing the DOM.

## 138: What are event listener breakpoints?

In the Sources panel, the "Event Listener Breakpoints" section lists event categories like Mouse, Keyboard, Timer, Animation and Control. Checking an event (for example `click`) makes the debugger pause in the first listener that runs for it.

Use it when you don't know which code handles an event. Combine it with the ignore list so you don't stop inside framework code.

## 139: What are XHR/fetch breakpoints?

In the Sources panel's "XHR/fetch Breakpoints" section, you can add a URL substring. The debugger pauses when any `fetch` or XHR request whose URL contains it is sent. Leave it empty to pause on every request.

The call stack then shows which code made the request, which helps with unexpected or duplicate API calls.

## 140: What is the ignore list in DevTools?

The ignore list tells the debugger to skip certain scripts, usually framework and library code. When you step through code or look at the call stack, ignored frames are skipped or collapsed, so you stay in your own code.

Chrome ignores `node_modules` and scripts marked in source maps with the `ignoreList` field by default. You can add more in Settings, then Ignore list, or by right-clicking a file and choosing "Add script to ignore list".

## 141: How do you check which element is on top at a certain point on the page?

Use the element picker and hover over that spot, or run in the console:

```js
document.elementFromPoint(200, 300);
```

If a click doesn't work, this often reveals an invisible overlay, a transparent element with a higher `z-index`, or a pseudo-element covering the target.

## 142: What is z-index and why does it sometimes not work?

`z-index` controls the stacking order of positioned elements (and flex or grid items). A higher value is drawn on top.

It often "doesn't work" because:

- The element has `position: static` and isn't a flex or grid item, so `z-index` is ignored.
- The elements are in different stacking contexts. A parent's stacking context limits how high a child can appear, no matter how big the child's `z-index` is.

## 143: How do you debug an element that is not visible on the page?

Check in this order:

1. Is it in the DOM? Search the Elements panel.
2. Does it have `display: none`, `visibility: hidden`, `opacity: 0`, or the `hidden` attribute? Check Computed.
3. Does it have zero size? Check the box model.
4. Is it outside the viewport or clipped by a parent with `overflow: hidden`?
5. Is it covered by another element (`z-index`, stacking context)?
6. Is its color the same as the background?

## 144: How do you debug a horizontal scrollbar appearing on a page?

Something is wider than the viewport. To find it:

- In the console, list elements that go past the right edge:

```js
[...document.querySelectorAll("*")].filter(
  (el) =>
    el.getBoundingClientRect().right > document.documentElement.clientWidth,
);
```

- Or temporarily add `* { outline: 1px solid red; }` in the Styles pane to see all boxes.

Common causes are fixed widths, `100vw` (which includes the scrollbar width on desktop), long words or URLs, large images, and negative margins.

## 145: What are the flexbox and grid overlays in DevTools?

In the Elements panel, flex and grid containers have a `flex` or `grid` badge. Clicking it shows an overlay on the page with the container's lines, gaps, item sizes and alignment. For grid it can also show line numbers, line names and area names.

The Layout pane lists all grid and flex containers on the page and lets you change overlay settings. Chrome also has flexbox and grid editors (the icon next to `display`) to try alignment values.

## 146: How do you debug a CSS file that isn't applied at all?

- Check the Network panel: did the file load (status 200) with a `text/css` content type?
- Check the console for CSP or MIME type errors.
- In the Elements panel, see if any rules from that file appear in the Styles pane.
- Check the selector: does it actually match the element? Look for typos, wrong class names, or CSS module names that were hashed.
- Check for a syntax error earlier in the file, like a missing `}`, that breaks the following rules.
- Check `@layer` order, and media or container queries that don't match.

## 147: What is the difference between display: none and visibility: hidden?

`display: none` removes the element from the layout completely, so it takes no space, and it is hidden from screen readers. `visibility: hidden` hides the element but it still takes up space in the layout. It is also hidden from screen readers and can't be clicked.

`opacity: 0` makes it invisible but it still takes space and can still be clicked and focused, which can cause "invisible element blocks clicks" bugs.

## 148: Why should you test with browser extensions disabled?

Extensions can inject scripts and styles, block requests (ad blockers), change the DOM (translators, password managers, grammar checkers), and cause hydration errors or console errors that aren't from your code.

Test in an Incognito or private window (extensions are usually off there) or a clean browser profile to see if the bug is caused by an extension.

## 149: What is a race condition in front-end code?

A race condition is a bug where the result depends on the order in which async operations finish. For example, a user types "ab" in a search box, two requests start, and the response for "a" arrives after the response for "ab", so the page shows results for "a".

The fix is to cancel old requests with `AbortController`, or ignore responses that are no longer the latest.

## 150: How are framework error messages different in development and production?

In development, React, Angular and Vue show long, helpful error messages and extra warnings. In production builds these are removed to keep bundles small, and errors are replaced by short codes or a link.

For example, React production errors say "Minified React error #418" with a link to react.dev that shows the full message. Angular shows codes like `NG0100` with a link to angular.dev's error reference.

# Moderate Questions (151-300)

## 151: How do you debug an error from production that only has a minified stack trace?

1. Find the exact build: the release version or commit, and the file name with its hash (for example `main.3f9a1.js`).
2. Get the source map for that build. Ideally your error tool (Sentry, Datadog and others) already has it uploaded and shows the original stack.
3. If not, load the source map locally. In Chrome you can right-click in the minified file in Sources and choose "Add source map", or use a tool like `source-map` in Node to map the line and column.
4. Open the original file and line, read the code around it, and check what data could make it fail.
5. Try to reproduce it with a production build locally, using the same data or feature flags.

## 152: What are hidden source maps and why use them in production?

A "hidden" source map is generated but the compiled file has no `//# sourceMappingURL` comment pointing to it. Browsers won't download it, so users can't see your original code easily, but you can still upload the map to your error tracking tool.

```js
// vite.config.js
export default {
  build: {
    sourcemap: "hidden",
  },
};
```

In webpack the same idea is `devtool: "hidden-source-map"`. After uploading the maps, many teams delete them from the deploy folder so they are not public.

## 153: Why might DevTools not load your source maps?

- Source maps are turned off in DevTools settings ("Enable JavaScript source maps").
- The build didn't generate them, or the `sourceMappingURL` comment is missing (hidden maps).
- The map URL returns 404, or needs authentication the browser doesn't have.
- The map is served with the wrong path, so the `sources` inside it don't match.
- The map belongs to a different build than the file (a stale map after a deploy).

Chrome shows source map load errors in the console and in the Developer Resources panel, which lists every map it tried to load and its status.

## 154: What are async stack traces?

Normally a stack trace only shows the synchronous calls. If an error happens inside a `setTimeout` callback, a promise `.then`, or after an `await`, the code that scheduled it is no longer on the stack.

Chrome DevTools records where async work was scheduled and shows those frames in the Call Stack, separated by labels like `setTimeout`, `Promise.then` or `await`. This lets you see the full path, for example from a button click, through an `await fetch(...)`, to the line that failed.

The `Error.stack` string in V8 also includes `async` frames for `await` chains, but not for callbacks like `setTimeout`.

## 155: How do you debug async/await code with breakpoints?

Set a breakpoint after the `await` line. When the promise resolves, the debugger pauses there with all local variables still available. You can step over an `await` line; DevTools waits for the promise and stops at the next line.

```js
async function loadOrder(id) {
  const res = await fetch(`/api/orders/${id}`); // step over waits for the response
  const order = await res.json(); // breakpoint here: res is in scope
  return order;
}
```

Turn on "Pause on caught exceptions" if the error is swallowed by a `try/catch` somewhere and you need to see where it first happened.

## 156: What do debug(fn) and monitor(fn) do in the Chrome console?

- `debug(fn)` sets a breakpoint at the start of the function, so the debugger pauses every time it is called. `undebug(fn)` removes it.
- `monitor(fn)` logs a message with the function name and arguments every time it is called. `unmonitor(fn)` stops it.

```js
debug(window.trackEvent); // pause whenever trackEvent runs
monitor(window.trackEvent); // log every call and its arguments
```

They are useful when you can find a function from the console but don't know where its code lives.

## 157: What does monitorEvents do?

`monitorEvents(element, types)` logs events fired on an element to the console. You can pass a single event name, an array, or a group like `"mouse"`, `"key"`, `"touch"` or `"control"`. `unmonitorEvents` stops it.

```js
monitorEvents($0, ["focus", "blur"]);
monitorEvents(window, "resize");
```

It is a quick way to check if an event is fired at all, and in what order.

## 158: What are some useful console utilities besides $ and $$?

- `copy(value)`: copies a value (objects are copied as JSON) to the clipboard.
- `queryObjects(Constructor)`: lists all live objects created by a constructor, for example `queryObjects(Promise)`.
- `getEventListeners(el)`: lists listeners on an element.
- `$_`: the result of the last expression.
- `$x(xpath)`: elements matching an XPath expression.
- `inspect(el)`: selects an element in the Elements panel or a function in Sources.
- `keys(obj)` and `values(obj)`.

These only work in the DevTools console, not in your page code.

## 159: What are live expressions in the console?

Live expressions are expressions pinned at the top of the console that DevTools re-evaluates about every 250 ms. Click the eye icon in the console toolbar to add one.

A good example is `document.activeElement`, to see which element has focus while you tab through the page, or `window.scrollY` while you scroll.

## 160: Why doesn't a breakpoint get hit?

- The code never runs: wrong branch, function not called, event not fired.
- The file you set the breakpoint in is not the file the browser runs, for example an old cached version, a different chunk, or the source map is wrong.
- The breakpoint was set in a file that was reloaded with different content (for example after HMR) and moved to another line.
- The code runs in a different context, like a worker, iframe or service worker.
- Breakpoints are disabled ("Deactivate breakpoints" is on).
- The script is on the ignore list.

Add a `debugger;` statement or a `console.log` to confirm whether the code runs at all.

## 161: What do "Continue to here" and "Restart frame" do?

While paused:

- **Continue to here:** right-click a line and choose it; execution runs until that line, like a one-time breakpoint.
- **Restart frame:** right-click a frame in the Call Stack and choose it; the debugger goes back to the start of that function and runs it again. Side effects that already happened (like network requests or changed globals) are not undone.

Restart frame is handy when you stepped past the interesting part and don't want to reproduce the bug again.

## 162: Can you change code while the debugger is paused?

Yes. In Chrome you can edit a JavaScript file in the Sources panel and save it with `Ctrl+S`. V8 replaces the function with the new version (live edit). If you edit the function you are paused in, DevTools restarts that frame.

There are limits: some changes, like editing top-level code or certain async functions, can't be applied. Changes are lost on reload unless you use Local Overrides or Workspaces.

## 163: How do you debug an event handler that doesn't fire?

1. Check the console for errors; an exception earlier may have stopped the code that adds the listener.
2. Select the element and check the Event Listeners tab: is the listener attached to this element or an ancestor?
3. Check if the element was replaced after the listener was added (common with `innerHTML` or framework re-renders).
4. Check for an overlay covering the element, or `pointer-events: none`.
5. Check if another handler calls `stopPropagation()` or `stopImmediatePropagation()` before yours.
6. Use `monitorEvents($0, "click")` to see if the event fires at all.

## 164: How do you debug an event handler that runs twice?

- The listener was added twice, for example in code that runs on every render or every route change. Check the Event Listeners tab for duplicates.
- The same handler is on the element and on a parent, and the event bubbles.
- A `<label>` wraps an input: a click on the label fires a click on the label and then a click on the input.
- In React development with StrictMode, effects run twice on mount, so manual `addEventListener` in an effect without cleanup adds two listeners.
- A form submit button with both a click handler and a submit handler that do the same thing.

## 165: What is a passive event listener and what bug can it cause?

A passive listener promises the browser it will not call `preventDefault()`, so the browser can scroll immediately without waiting for your JavaScript. It improves scroll performance.

```js
window.addEventListener("touchmove", onMove, { passive: true });
```

Chrome makes `touchstart`, `touchmove` and `wheel` listeners on `window`, `document` and `body` passive by default. If you call `preventDefault()` in a passive listener, it is ignored and the console shows "Unable to preventDefault inside passive event listener invocation". If you really need to block scrolling, add the listener with `{ passive: false }` or use the CSS `touch-action` property.

## 166: What bugs are common with event delegation?

Event delegation means putting one listener on a parent and checking `event.target` to see which child was clicked. Common bugs:

- `event.target` is a nested element (an icon or `<span>`) instead of the button. Use `closest()`:

```js
list.addEventListener("click", (e) => {
  const button = e.target.closest("button[data-id]");
  if (!button || !list.contains(button)) return;
  removeItem(button.dataset.id);
});
```

- Events that don't bubble (`focus`, `mouseenter`) never reach the parent; use `focusin` or `mouseover`.
- A child calls `stopPropagation()` so the parent never sees the event.

## 167: Why doesn't removeEventListener remove my listener?

`removeEventListener` needs the exact same function reference and the same `capture` value that were used with `addEventListener`. Anonymous functions or functions created with `.bind()` each time create a new reference, so nothing is removed.

```js
// Bug: two different functions
el.addEventListener("click", () => save());
el.removeEventListener("click", () => save());

// Fix: keep the reference, or use AbortController
const controller = new AbortController();
el.addEventListener("click", save, { signal: controller.signal });
controller.abort(); // removes it
```

## 168: How do you debug a stale value inside setInterval?

The callback is created once and keeps the variables from the moment it was created. If the code later expects a newer value, the interval still sees the old one. This is very common in React:

```jsx
function Counter() {
  const [count, setCount] = useState(0);

  useEffect(() => {
    const id = setInterval(() => {
      setCount(count + 1); // count is always 0 here, so it stays at 1
    }, 1000);
    return () => clearInterval(id);
  }, []);

  return <p>{count}</p>;
}
```

Fix it with a functional update, `setCount((c) => c + 1)`, or keep the latest value in a ref. A breakpoint inside the callback shows the captured value in the Closure scope.

## 169: How do you fix a race condition in a search box?

Cancel the previous request when a new one starts, so an old response can't overwrite a newer one:

```js
let controller;

async function search(query) {
  controller?.abort();
  controller = new AbortController();

  try {
    const res = await fetch(`/api/search?q=${encodeURIComponent(query)}`, {
      signal: controller.signal,
    });
    renderResults(await res.json());
  } catch (err) {
    if (err.name !== "AbortError") throw err;
  }
}
```

To confirm the bug first, throttle the network and type quickly; the Network panel will show responses finishing out of order. Data libraries like TanStack Query handle this for you.

## 170: What bugs come from a missing await?

Without `await`, you get a promise instead of the value, and code runs in the wrong order:

```js
async function save() {
  const user = getUser(); // forgot await: user is a Promise
  console.log(user.name); // undefined
  api.save(user); // sends "{}" or fails
}
```

Errors from the promise also become unhandled rejections instead of being caught by your `try/catch`. TypeScript and the `@typescript-eslint/no-floating-promises` and `no-misused-promises` lint rules catch many of these.

## 171: Why doesn't async work inside forEach?

`forEach` ignores the promises returned by an async callback. It doesn't wait for them, so code after the loop runs before the work is done, and errors are unhandled.

```js
// Bug: "done" logs before any item is saved
items.forEach(async (item) => {
  await saveItem(item);
});
console.log("done");

// In sequence
for (const item of items) {
  await saveItem(item);
}

// In parallel
await Promise.all(items.map((item) => saveItem(item)));
```

## 172: What is the difference between Promise.all and Promise.allSettled when debugging?

`Promise.all` rejects as soon as one promise rejects, and you only get that first error. The other promises keep running, but their results are lost. `Promise.allSettled` waits for all of them and gives you the status and value or reason of each.

When one failing request makes a whole page fail, `allSettled` is useful both for debugging (see which ones failed) and for showing partial data.

```js
const results = await Promise.allSettled([loadUser(), loadOrders(), loadAds()]);
results.forEach((r, i) => {
  if (r.status === "rejected") console.error(i, r.reason);
});
```

## 173: How do you debug code that runs in an unexpected order?

Remember the order: synchronous code first, then all microtasks (promise callbacks, `queueMicrotask`, `await` continuations), then the next task (`setTimeout`, events, messages). Rendering happens between tasks.

```js
console.log("1");
setTimeout(() => console.log("4"), 0);
Promise.resolve().then(() => console.log("3"));
console.log("2");
// 1, 2, 3, 4
```

To debug, add numbered logs or logpoints and read their order, or record a Performance trace to see which task each piece of code ran in.

## 174: How do you debug a CORS preflight failure?

A preflight is an `OPTIONS` request the browser sends before "non-simple" requests, for example with `Content-Type: application/json`, custom headers like `Authorization`, or methods like `PUT` and `DELETE`.

1. In the Network panel, find the `OPTIONS` request (it may be grouped with the real request; turn on "Preflight" in "Other" filters if needed).
2. Check its status: it must be 2xx. A 401 or 404 on `OPTIONS` means the server or a gateway doesn't handle it.
3. Check its response headers: `Access-Control-Allow-Origin`, `Access-Control-Allow-Methods` and `Access-Control-Allow-Headers` must include what your real request uses.
4. Fix it on the server or proxy, or use a same-origin proxy (like the dev server proxy) during development.

## 175: Why does CORS fail when you send cookies?

To send cookies on a cross-origin request you use `credentials: "include"` in `fetch` or `withCredentials` in XHR. Then the server must:

- Send `Access-Control-Allow-Origin` with the exact origin, not `*`.
- Send `Access-Control-Allow-Credentials: true`.

The cookie itself must also be allowed: `SameSite=None; Secure` for cross-site requests, and it must not be blocked by third-party cookie settings. The console message usually says which of these is missing.

## 176: How do you tell if a response came from the cache?

In the Network panel, the Size column shows `(memory cache)`, `(disk cache)`, `(ServiceWorker)` or `(prefetch cache)` instead of a byte size when the response came from a cache. A `304 Not Modified` status means the browser asked the server and the server said the cached copy is still fine.

Click the request and look at the response headers (`Cache-Control`, `ETag`, `Last-Modified`, `Age`) to see why it was cached and for how long.

## 177: How do you debug users seeing an old version of the app after a deploy?

- Check if `index.html` is cached. It should usually have `Cache-Control: no-cache` (or a short max-age) so the browser always checks for a new version.
- Check that JS and CSS files have content hashes in their names, so new builds get new URLs and can be cached for a long time.
- Check the CDN cache: was it purged, and what headers does it send?
- Check for a service worker that serves old files from Cache Storage.
- Check for users with an old tab open; they may load a lazy chunk that no longer exists after the deploy (a "ChunkLoadError" or failed dynamic import).

## 178: How do you debug a redirect loop?

The browser shows `ERR_TOO_MANY_REDIRECTS`. Enable "Preserve log" in the Network panel and load the page. You will see the chain of `301`, `302`, `307` or `308` responses and each `Location` header.

Common causes: HTTP to HTTPS redirects that fight with a proxy that already terminates TLS, `www` and non-`www` rules that point at each other, and auth redirects where the login page itself requires login. In SPAs, a client-side router guard that redirects back and forth can do the same without HTTP redirects; check the router logic and URL history.

## 179: How do you debug WebSocket connections?

In the Network panel, filter by "WS" and click the connection. The Headers tab shows the handshake (`101 Switching Protocols`), and the Messages tab shows every message sent (green arrow up) and received (red arrow down) with its time and content. You can filter messages by text.

If the connection closes, the close code helps: `1000` is normal, `1006` means it dropped without a close frame (often a proxy, timeout or network issue). Check that proxies and load balancers allow WebSocket upgrades and don't close idle connections.

## 180: How do you debug Server-Sent Events or streaming responses?

For `EventSource`, the Network panel shows an "EventStream" tab with each event's type, data and time. For streamed `fetch` responses (common with AI chat apps), the Response tab only fills in as data arrives, and you may need to log chunks from the reader in your code:

```js
const res = await fetch("/api/chat", { method: "POST", body });
const reader = res.body.pipeThrough(new TextDecoderStream()).getReader();
while (true) {
  const { value, done } = await reader.read();
  if (done) break;
  console.debug("chunk", value);
}
```

If chunks arrive all at once at the end, a proxy or compression is probably buffering the response.

## 181: How do you test the front end against an API response you can't easily change?

Use DevTools overrides: right-click the request in the Network panel and choose "Override content" (or "Override headers"). Edit the response, save, and reload; DevTools serves your version.

Other options are mocking in code with MSW (Mock Service Worker), `page.route()` in Playwright, `cy.intercept()` in Cypress, or a local proxy like Charles or mitmproxy. This lets you test empty lists, error responses and strange data without waiting for the back end.

## 182: How do you debug a cookie that isn't being set?

Click the response that sends `Set-Cookie` in the Network panel and open its Cookies tab. Blocked response cookies are shown with a warning and a reason when you hover, for example:

- `Secure` cookie set over HTTP.
- `SameSite=None` without `Secure`.
- `Domain` attribute doesn't match the current host.
- The cookie is set by a cross-site response and third-party cookies are blocked.
- Invalid syntax or too large.

Also remember that JavaScript can't read `HttpOnly` cookies, so `document.cookie` won't show them even when they are set.

## 183: How do you debug a cookie that isn't sent with a request?

Open the request in the Network panel, then the Cookies tab, and check "show filtered out request cookies". Chrome lists cookies that exist but were not sent, with the reason, for example:

- The path or domain doesn't match.
- `SameSite` blocked it on a cross-site request.
- It is `Secure` and the request is HTTP.
- It expired.
- The `fetch` call didn't use `credentials: "include"` for a cross-origin request.

## 184: What localStorage bugs are common?

- Storing objects without `JSON.stringify` (you get `"[object Object]"`) or forgetting `JSON.parse` when reading.
- `QuotaExceededError` when storage is full (usually around 5 MB per origin).
- Access throws in some sandboxed iframes or when storage is blocked by browser settings.
- Code that reads `localStorage` during server-side rendering, where `window` doesn't exist.
- Data from an old app version with a different shape, breaking the new code. Add a version key or validate what you read.

Wrap access in `try/catch` and check the Application panel to see the actual stored values.

## 185: How do you debug IndexedDB data?

In the Application panel, expand IndexedDB, then your database and object stores. You can browse records, search by key, refresh, delete records, or delete the whole database.

Common bugs are version upgrade problems (`onupgradeneeded` not creating a store, or a `blocked` event because another tab has the old version open), transactions that close because you awaited something unrelated in the middle, and storing objects that can't be cloned (functions, DOM nodes). Libraries like `idb` make the API easier and reduce these mistakes.

## 186: How do you inspect Cache Storage?

In the Application panel, expand "Cache storage" to see each named cache, the cached URLs, response headers and content. You can delete single entries or whole caches.

It is where service workers (for example built with Workbox) keep files. If the site serves old files, compare the cached entries with the current deploy, and check whether your service worker deletes old caches in its `activate` event.

## 187: Why is a new service worker stuck in "waiting"?

A new service worker installs but waits until all tabs using the old one are closed. A page reload is not enough if only one tab exists, because the old page is still in control during the reload.

In DevTools you can click "skipWaiting" in Application, then Service workers. In code, you can call `self.skipWaiting()` in the `install` event and `clients.claim()` in `activate`, or show users a "New version available, reload" message and call `skipWaiting` when they click it. Skipping waiting can mix old pages with new files, so be careful with lazy-loaded chunks.

## 188: How do you debug a specificity conflict?

Select the element, find the property in the Styles pane, and look at which rule wins and which are crossed out. Hover over the selectors to see their specificity. In the Computed pane, expand the property to see all rules that tried to set it, in order.

Fix it by making selectors simpler and more consistent (for example one class per component), using cascade layers, or `:where()` to lower specificity in base styles. Adding `!important` usually starts a war that makes the next bug harder.

## 189: How do cascade layers affect debugging?

With `@layer`, the order of layers matters more than specificity: a rule in a later layer wins over a rule in an earlier layer, even if the earlier rule has a more specific selector. Styles not in any layer win over all layered styles.

```css
@layer reset, base, components, utilities;

@layer components {
  #header .title {
    color: blue;
  } /* loses */
}
@layer utilities {
  .text-red {
    color: red;
  } /* wins, later layer */
}
```

Chrome's Styles pane shows the layer name above each rule, and the Elements panel can show the layer order. When a "more specific" rule loses, check the layers first. Note that `!important` reverses the layer order.

## 190: What creates a stacking context, and how do you debug z-index issues with it?

A stacking context is created by, among others: the root element, positioned elements with a `z-index` other than `auto`, `position: fixed` or `sticky`, `opacity` less than 1, `transform`, `filter`, `perspective`, `clip-path`, `mask`, `isolation: isolate`, `will-change` on those properties, `contain: paint`, and flex or grid items with a `z-index`.

A child can't appear above elements outside its parent's stacking context. To debug, walk up the ancestors of the element in the Elements panel and look for these properties. Chrome's Layers panel and the "Rendering" options can help visualize layers. Moving a modal to the end of `body` (a portal) or using the `<dialog>` element with `showModal()` (which puts it in the top layer) avoids most of these problems.

## 191: Why doesn't position: sticky work?

Common reasons:

- No `top`, `bottom`, `left` or `right` value is set.
- An ancestor has `overflow: hidden`, `auto` or `scroll`, so the element sticks inside that ancestor instead of the page (and if that ancestor doesn't scroll, it never sticks).
- The parent is not taller than the sticky element, so there's no room to stick.
- In a flex container with `align-items: stretch`, the sticky element is as tall as the container.

Check the ancestors in the Elements panel for `overflow` values first; that is the most common cause.

## 192: Why does a flex item overflow or not shrink?

Flex items have `min-width: auto` by default, which means they won't shrink below the size of their content. A long word, URL, `<pre>` block or wide table inside makes the item push out of the container.

```css
.item {
  min-width: 0; /* allow shrinking below content size */
}
.item .title {
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
}
```

The same applies to grid items: use `minmax(0, 1fr)` instead of `1fr` if content makes columns too wide. Chrome's flex overlay helps you see which item is too wide.

## 193: What is margin collapsing and how does it cause layout bugs?

Vertical margins of block elements can combine into one margin instead of adding up. For example, a `margin-top` on the first child can "leak" out of its parent and push the parent down, instead of creating space inside it.

It doesn't happen in flex or grid containers, or when the parent has padding, a border, or creates a new block formatting context (for example `display: flow-root`). The box model view in DevTools shows the margin, which helps you notice that the space belongs to the child, not the parent.

## 194: How do you debug a CSS grid layout?

- Click the `grid` badge in the Elements panel to show the overlay with line numbers, track sizes and area names.
- Check the Computed values of `grid-template-columns` to see the actual track sizes.
- Look for items placed in the wrong place because of a typo in `grid-area` names or line numbers; unnamed areas create implicit tracks.
- Check for implicit rows or columns created by items placed outside the defined grid (`grid-auto-rows`, `grid-auto-flow`).
- Use `minmax(0, 1fr)` when content makes `1fr` columns grow.

## 195: Why might a CSS custom property not work?

- The variable name has a typo or wrong case (custom properties are case sensitive).
- The variable is defined on an element that isn't an ancestor of the element using it.
- The value makes the property invalid, for example `--gap: 10` used in `margin: var(--gap)` without a unit. This is "invalid at computed-value time": the property falls back to its inherited or initial value, not to the previous valid declaration, so it looks like the rule is ignored.

Hover over `var(--gap)` in the Styles pane to see its current value. Chrome shows a warning if the variable is not defined. You can also give a fallback: `var(--gap, 16px)`, or register it with `@property` to give it a type.

## 196: How do you debug web font problems?

- In the Network panel, filter by "Font" to see if the files load, their status and size. A CORS error is common when fonts are on another domain.
- In the Elements panel, select text and scroll to the bottom of the Computed pane to see "Rendered Fonts": the font actually used and how many glyphs.
- Check the `font-family` name matches the `@font-face` declaration exactly.
- For invisible text during load, check `font-display` (use `swap` or `optional`).
- For layout shift when the font loads, use `size-adjust` and related descriptors on a fallback font, and preload important fonts.

## 197: How do you check which image a responsive image actually loaded?

Select the `<img>` in the Elements panel and, in the console, read `$0.currentSrc`. It shows the URL the browser picked from `srcset` or `<picture>`. Hovering over the `src` in the Elements panel also shows the rendered and intrinsic size.

If the browser picks a bigger image than you expect, check the `sizes` attribute (without it the browser assumes `100vw`), the device pixel ratio, and whether a larger image is already in the cache (browsers may reuse it).

## 198: How do you keep CSS changes you made in DevTools?

Chrome's Changes panel (open from the Command Menu, "Show Changes") lists every change you made in the Styles pane and Sources, as a diff, and lets you copy it. In the Styles pane you can also right-click a rule and copy it or all declarations.

If you use Workspaces with your project folder, changes are saved straight to your files.

## 199: How do you debug layout shifts (CLS)?

1. Open the Rendering tab and turn on "Layout shift regions"; shifted areas flash blue.
2. Record a Performance trace. Layout shifts appear in the "Layout shifts" track; click one to see which elements moved and its score. The CLS insight lists the "culprits" when Chrome can find them, for example images without size, injected content or web fonts.
3. In the field, use the `web-vitals` library with attribution to report the element that shifted:

```js
import { onCLS } from "web-vitals/attribution";

onCLS(({ value, attribution }) => {
  console.log(
    value,
    attribution.largestShiftTarget,
    attribution.largestShiftSource,
  );
});
```

Common fixes: set `width` and `height` or `aspect-ratio` on images and embeds, reserve space for ads and banners, and avoid inserting content above existing content.

## 200: How do you debug a slow LCP?

1. Record a Performance trace (or look at the live metrics view) to see which element is the LCP element.
2. Look at the LCP breakdown: time to first byte, resource load delay, resource load duration, and element render delay. Each part points to a different fix.
3. If TTFB is high, look at the server and caching. If load delay is high, the browser found the image late (for example it is set by JavaScript or CSS background), so preload it or put it in HTML with `fetchpriority="high"`. If load duration is high, make the image smaller. If render delay is high, something blocks rendering, like scripts, CSS or client-side rendering.
4. Never lazy-load the LCP image.

## 201: How do you debug a slow INP?

INP is the delay from a user interaction to the next frame being painted. It has three parts: input delay (main thread busy before the handler runs), processing time (your handlers), and presentation delay (style, layout and paint after).

1. In the Performance panel, the live metrics view shows INP and lists slow interactions as you use the page.
2. Record a trace while doing the slow interaction. The Interactions track shows it with its parts; the main thread below shows what ran.
3. Fix long handlers by doing less work, yielding with `scheduler.yield()` (with a fallback), moving work to a worker, or deferring non-urgent updates.
4. In the field, use `onINP` from `web-vitals/attribution` to get the target element and the long animation frame scripts.

## 202: What is layout thrashing (forced reflow)?

The browser normally calculates layout once per frame. If your code changes styles and then immediately reads a layout value (`offsetHeight`, `getBoundingClientRect()`, `scrollTop`), the browser has to calculate layout right away. Doing this in a loop forces layout many times in one frame.

```js
// Bad: read and write in the same loop
items.forEach((el) => {
  el.style.width = el.parentNode.offsetWidth / 2 + "px";
});

// Better: read all first, then write
const widths = items.map((el) => el.parentNode.offsetWidth);
items.forEach((el, i) => {
  el.style.width = widths[i] / 2 + "px";
});
```

In the Performance panel, forced layouts show as purple "Layout" blocks inside your JavaScript, with a warning "Forced reflow is a likely performance bottleneck", and the "Forced reflow" insight shows the line that caused it.

## 203: What can the Rendering tab do for debugging?

The Rendering tab (Command Menu, "Show Rendering") has:

- **Paint flashing:** green highlight on areas that repaint.
- **Layout shift regions:** blue highlight on areas that shift.
- **Layer borders:** shows composited layers and tiles.
- **Frame rendering stats:** FPS and GPU info overlay.
- **Scrolling performance issues:** highlights elements that slow down scrolling, like non-passive listeners.
- Emulation of `prefers-color-scheme`, `prefers-reduced-motion`, print media, vision deficiencies, focused page, and disabled local fonts or image formats.

## 204: What is paint flashing and what does it tell you?

With paint flashing on, Chrome flashes green over every area it repaints. If you scroll or hover and large parts of the page flash, the browser is doing more paint work than needed.

Common causes are animating properties like `top`, `left`, `width`, `box-shadow` or `background-color`, and fixed elements that cause the whole page to repaint. Animating `transform` and `opacity` usually avoids repaint because the compositor handles them.

## 205: What is the Coverage tab used for?

The Coverage tab (Command Menu, "Show Coverage") records which bytes of JavaScript and CSS were actually used while you interact with the page. Each file shows how much was unused, and in Sources unused lines are marked red.

It helps you find large libraries loaded up front but barely used, so you can split them into lazy chunks. Be careful: code unused on first load may still be needed later in another flow.

## 206: How do you find a memory leak with heap snapshots?

1. Load the page and do the action once (to warm up caches).
2. In the Memory panel, click the garbage collection icon, then take snapshot 1.
3. Repeat the action several times (for example open and close a modal 10 times).
4. Collect garbage again, then take snapshot 2.
5. In snapshot 2, switch the view to "Comparison" with snapshot 1 and sort by "# Delta" or "Size Delta".
6. Look for objects that grew by about the number of times you repeated the action, and check their "Retainers" to see what keeps them in memory.

## 207: What are detached DOM nodes?

A detached DOM node is an element that was removed from the document but is still referenced by JavaScript, so it can't be garbage collected. Often one reference keeps a whole removed subtree alive.

```js
let cache = [];
function showPopup() {
  const popup = document.createElement("div");
  document.body.append(popup);
  cache.push(popup); // still referenced after removal
  setTimeout(() => popup.remove(), 3000);
}
```

In the Memory panel, take a heap snapshot and type "Detached" in the class filter, or use the "Detached elements" profile type in recent Chrome versions. The Retainers section shows what holds on to them.

## 208: What are the most common listener and timer leaks?

- Listeners added to `window` or `document` in a component and never removed when it unmounts.
- `setInterval` that is never cleared, so its callback (and everything it closes over) stays alive.
- Observers (`ResizeObserver`, `IntersectionObserver`, `MutationObserver`) not disconnected.
- Subscriptions (RxJS, stores, WebSocket handlers) not unsubscribed.

In React, return a cleanup function from `useEffect`. In Angular, use `takeUntilDestroyed()`, `DestroyRef.onDestroy`, or the `async` pipe and signals. Using an `AbortController` signal lets you remove many listeners at once.

## 209: What do Shallow size and Retained size mean in a heap snapshot?

- **Shallow size:** memory used by the object itself.
- **Retained size:** memory that would be freed if this object were deleted, including everything only it keeps alive.

An object can be small but retain a lot, for example a closure that keeps a large array or a detached DOM tree alive. Sort by retained size to find the objects that matter most, and look at the Retainers path to see why they are still reachable.

## 210: How do you find out why a React component re-rendered?

- In React DevTools settings, enable "Highlight updates when components render" to see which parts of the page re-render as you interact.
- In the Profiler, enable "Record why each component rendered while profiling". After recording, select a component to see the reason: props changed (and which ones), state changed, hooks changed, context changed, or the parent rendered.
- Look at the flame chart for components that render often with no visible change.

Common causes are new object or function props created on every render, context values that change on every render, and state kept too high in the tree.

## 211: How do you debug a useEffect that runs too often or in a loop?

Check the dependency array. If a dependency is an object, array or function created during render, it is a new value every time, so the effect runs on every render. If the effect also sets state, you get an infinite loop.

```jsx
// Bug: options is new on every render
const options = { page, size: 20 };
useEffect(() => {
  fetchItems(options).then(setItems);
}, [options]);

// Fix: depend on primitives
useEffect(() => {
  fetchItems({ page, size: 20 }).then(setItems);
}, [page]);
```

Log the dependencies at the top of the effect, or use the Profiler's "why did this render" information. The `react-hooks/exhaustive-deps` lint rule helps keep the list correct; don't silence it without understanding why. Also ask if you need an effect at all; derived values can often be computed during render.

## 212: What is a stale closure in React and how do you fix it?

A stale closure is when a callback or effect uses state or props from an older render. Each render creates new functions that see the values of that render. If an old function is still used (in an effect with missing dependencies, a timer, a subscription, or a memoized callback), it sees old values.

Fixes:

- Add the missing dependencies to `useEffect`, `useCallback` or `useMemo`.
- Use a functional state update: `setCount((c) => c + 1)`.
- For event handlers used inside effects, use `useEffectEvent` (stable since React 19.2) so the effect doesn't need to re-run but the handler sees the latest values.
- Store the latest value in a ref when needed.

## 213: Why do effects run twice in React development?

In development, `<StrictMode>` mounts each component, unmounts it, and mounts it again. So effects run, clean up, and run again. React also calls component functions, initializers and state updaters twice. This happens only in development, to expose effects without proper cleanup and impure render code.

If running twice causes a bug (two subscriptions, two analytics events, duplicate data), the effect is missing cleanup or isn't safe to repeat. Fix the effect instead of removing StrictMode. React DevTools shows the second render's logs dimmed by default.

## 214: How do you fix a hydration mismatch in React?

Read the error: in React 19, the console shows a diff of the server and client HTML. Then find what renders differently:

- Values like `new Date()`, `Math.random()` or locale formatting that differ between server and client.
- Reading `window`, `localStorage` or media queries during render.
- Invalid HTML nesting that the browser "fixes" before hydration, like a `<div>` in a `<p>` or a missing `<tbody>`.
- Browser extensions changing the HTML.

Fix it by rendering the same output on both sides and updating client-only values after mount:

```jsx
function Clock() {
  const [now, setNow] = useState(null);
  useEffect(() => setNow(new Date()), []);
  return <span>{now ? now.toLocaleTimeString() : ""}</span>;
}
```

For unavoidable small differences like a timestamp, `suppressHydrationWarning` on that one element silences the warning.

## 215: What bugs come from wrong keys in React lists?

React uses `key` to match list items between renders. If keys are missing, duplicated, or use the array index while items are added, removed or reordered, React may reuse the wrong component, so state (like input values, checkboxes, or open/closed state) appears on the wrong row.

Use a stable unique id from the data as the key. Using a random value on every render is also wrong: it remounts every item every time, losing state and hurting performance. React warns in the console about missing and duplicate keys.

## 216: Why doesn't React state update immediately after setState?

Calling a state setter schedules a re-render; it doesn't change the variable in the current render. So reading the state right after setting it gives the old value.

```jsx
function handleClick() {
  setCount(count + 1);
  console.log(count); // still the old value
  setCount(count + 1); // uses the same old value, so +1 total, not +2
}
```

Use the new value you calculated, or functional updates (`setCount((c) => c + 1)`) when the update depends on the previous state. React batches several updates in one event into one render.

## 217: What does "Too many re-renders" mean in React?

React stops with "Too many re-renders. React limits the number of renders to prevent an infinite loop" when a component sets state during render in a way that causes another render, again and again. A common cause is calling a function instead of passing it:

```jsx
// Bug: runs setOpen on every render
<button onClick={setOpen(true)}>Open</button>

// Fix
<button onClick={() => setOpen(true)}>Open</button>
```

Other causes are setting state unconditionally in the component body, or an effect that sets state and depends on that same state.

## 218: How do you log React errors from all roots in one place?

In React 19, `createRoot` and `hydrateRoot` accept error callbacks:

```jsx
const root = createRoot(container, {
  onUncaughtError(error, errorInfo) {
    reportError(error, errorInfo.componentStack);
  },
  onCaughtError(error, errorInfo) {
    // errors caught by an error boundary
    reportError(error, errorInfo.componentStack);
  },
  onRecoverableError(error, errorInfo) {
    // for example hydration errors React recovered from
    console.warn(error, errorInfo.componentStack);
  },
});
root.render(<App />);
```

The `componentStack` shows which components were rendering, which is often more useful than the JavaScript stack.

## 219: How do you debug a component when the React Compiler is used?

The React Compiler memoizes components and hooks automatically at build time. In React DevTools, compiled components show a "Memo ✨" badge, so you can check whether a component was compiled.

If a component behaves differently after enabling the compiler, the code may break the Rules of React (for example mutating props or state, or reading refs during render). Check the compiler's ESLint rules (in `eslint-plugin-react-hooks`), and you can opt a single component out with the `"use no memo"` directive while you investigate.

## 220: What is ExpressionChangedAfterItHasBeenCheckedError in Angular?

It is error `NG0100`. In development, Angular runs an extra check after change detection to make sure bound values didn't change during the check. If a value changed, for example because a child component or a lifecycle hook like `ngAfterViewInit` updated a parent's value, Angular throws this error.

Fix it by not changing state during change detection: compute the value earlier (in `ngOnInit` or with a `computed` signal), move the update to an event, or restructure the data flow. Wrapping the change in `setTimeout` hides the error but usually just hides a design problem.

## 221: Why doesn't an OnPush component update in Angular?

An `OnPush` component is only checked when:

- One of its inputs gets a new reference.
- An event happens in its template or its children.
- A signal it reads in the template changes.
- An `async` pipe in its template emits.
- It is marked manually with `ChangeDetectorRef.markForCheck()`.

The common bug is mutating an object or array input (`this.items.push(x)`) instead of creating a new one, so the reference stays the same and the view doesn't update. Use immutable updates or signals.

## 222: How do you debug signals in Angular?

- In Angular DevTools, select a component to see its signal values, and use the signal graph view (in recent versions) to see which `computed` and `effect` nodes depend on which signals.
- A common bug is mutating the value inside a signal instead of setting a new one. `items().push(x)` doesn't notify anyone. Use `items.update((list) => [...list, x])`.
- A `computed` only tracks signals it actually reads during its last run; signals read only inside an `if` branch that didn't run aren't tracked.
- Reading signals inside `untracked()` or after an `await` in an effect doesn't create a dependency.
- Use `effect(() => console.log(mySignal()))` temporarily to log changes.

## 223: What changes when debugging a zoneless Angular app?

New Angular apps are zoneless by default since Angular 21, so `zone.js` doesn't patch `setTimeout`, promises and events to trigger change detection. Change detection runs when a signal read in a template changes, an input changes, a template event fires, an `async` pipe emits, or `markForCheck()` is called.

So the typical bug is: a plain class property is updated in a `setTimeout`, a `fetch().then()` or a third-party callback, and the view doesn't update. Fix it by storing that state in a signal. Stack traces are also shorter and cleaner without zone.js frames, which makes debugging easier.

## 224: What can you do with the ng global in the browser console?

In development mode, Angular adds an `ng` object to the console:

```js
const cmp = ng.getComponent($0); // component instance of the selected element
cmp.title = "Test";
ng.applyChanges(cmp); // run change detection for it

ng.getOwningComponent($0); // component whose template contains the element
ng.getContext($0); // context of @for or ngIf embedded views
ng.getDirectives($0);
ng.getInjector($0);
ng.getListeners($0);
```

It is useful for checking component state when DevTools extensions aren't available.

## 225: How do you debug NullInjectorError in Angular?

`NullInjectorError: No provider for X` means Angular looked for a dependency in the injector tree and didn't find a provider. Check:

- Is the service `providedIn: "root"`, or provided in `app.config.ts`, a route's `providers`, or the component's `providers`?
- For things like `HttpClient` or the router, did you add `provideHttpClient()` or `provideRouter()`?
- Are you injecting it in a place that can't see that provider, for example a provider in a lazy route that another part of the app tries to use?
- Is the token you inject the same as the one you provide (same import, not a copy from another package version)?

Angular DevTools' Injector tree shows which injector provides what.

## 226: How do you debug Angular hydration errors?

Angular hydration errors have codes in the `NG05xx` range, for example `NG0500` when the DOM structure doesn't match. The console message shows the expected node and the node it found.

Common causes are code that changes the DOM directly (for example with `document` or `ElementRef.nativeElement`), invalid HTML nesting, browser-only values used during render, and CDNs or extensions that change the HTML. Fix the template so server and client render the same output, use `afterNextRender` for browser-only code, and as a last resort add `ngSkipHydration` to one component while you fix it. Angular DevTools can show which components were hydrated.

## 227: How do you tell if a Next.js error happened on the server or the client?

- **Server errors** (Server Components, Server Actions, route handlers, `proxy.ts` or `middleware.ts`, server-side rendering) are printed in the terminal where `next dev` or the server runs. In development, Next.js also shows them in the error overlay in the browser.
- **Client errors** (Client Components after hydration, event handlers, effects) show in the browser console with a client stack trace.

In production, server error details are hidden from the browser; the client gets a generic message with a `digest`. Search the server logs for that digest to find the real error.

## 228: What errors happen with "use client" boundaries in Next.js?

In the App Router, components are Server Components by default. Common errors:

- Using `useState`, `useEffect`, event handlers or browser APIs in a Server Component. Add `"use client"` at the top of the file that needs them.
- Passing a function, class instance or other non-serializable value from a Server Component to a Client Component as a prop. Only serializable data can cross the boundary (Server Actions are the exception).
- Importing server-only code (database clients, secrets) into a Client Component. Use the `server-only` package to make this a build error.
- Making a big part of the tree client-side by putting `"use client"` too high.

## 229: How do you debug stale data in a Next.js App Router app?

First find out where the data is cached:

- **Route rendered at build time:** check the `next build` output; static routes are prerendered and don't fetch again until revalidated.
- **Data cache:** in Next.js 15 and later, `fetch` is not cached by default, but code using `"use cache"`, `unstable_cache`, or `fetch` with `cache: "force-cache"` or `next.revalidate` is.
- **Client router cache:** the browser keeps visited pages for back/forward navigation.
- **CDN or browser cache** in front of the app.

Then check that mutations call `revalidatePath`, `revalidateTag` or `updateTag`, or `router.refresh()` on the client. Logging inside the data function shows whether it actually runs on each request.

## 230: Why is an environment variable undefined in the browser in Next.js or Vite?

Build tools only put variables with a public prefix into client code, and they replace them at build time:

- Next.js: only `NEXT_PUBLIC_*` variables are available in the browser.
- Vite: only `VITE_*` variables, read with `import.meta.env.VITE_API_URL`.

Other common causes: you changed `.env` but didn't restart the dev server or rebuild, the variable is set only in your local `.env` and not in CI or the hosting provider, or you read it dynamically (`process.env[name]`), which can't be replaced at build time. Never put secrets in public variables.

## 231: How do you debug Next.js server code with breakpoints?

Start the dev server with the inspector on:

```bash
next dev --inspect
```

Then open `chrome://inspect` in Chrome and click "inspect" on the Next.js process, or attach the VS Code debugger. Breakpoints in Server Components, route handlers and Server Actions will pause there. The VS Code "JavaScript Debug Terminal" also works: run `npm run dev` inside it and set breakpoints in the editor.

## 232: How do you use Redux DevTools to find a bug in state?

1. Open the Redux tab and do the action that breaks things.
2. Find the action in the list. Check its payload in the "Action" tab: is it what you expected?
3. Check the "Diff" tab: did the state change the way you expected? If nothing changed, the reducer didn't handle the action (wrong type string, wrong slice).
4. Use the "Trace" tab (if enabled with `trace: true`) to see which code dispatched it.
5. Use the slider or "Jump" to go back to the state before the bug and step forward.

If the UI doesn't update even though state changed, a selector may return the same reference, or the state was mutated outside of Immer.

## 233: How do you debug NgRx?

- Add `provideStoreDevtools({ maxAge: 25, logOnly: !isDevMode() })` and use Redux DevTools to see actions and state.
- If an effect doesn't run, check it is registered (`provideEffects([...])`) and that `ofType` matches the action creator.
- If an effect stops working after the first error, it is because an error inside the main stream completed it. Catch errors inside the inner observable (`switchMap(() => api().pipe(catchError(...)))`).
- Turn on runtime checks like `strictStateImmutability` and `strictActionImmutability` (on by default in development) to catch mutations.
- For NgRx SignalStore, use `withDevtools` from `@angular-architects/ngrx-toolkit` to see its state in Redux DevTools.

## 234: How do you debug a Zustand store?

Wrap the store with the `devtools` middleware to see actions in Redux DevTools:

```js
import { create } from "zustand";
import { devtools } from "zustand/middleware";

const useCart = create(
  devtools(
    (set) => ({
      items: [],
      add: (item) =>
        set((s) => ({ items: [...s.items, item] }), false, "cart/add"),
    }),
    { name: "cart" },
  ),
);
```

The third argument to `set` names the action. A common bug is selecting a new object or array in a selector (`useCart((s) => ({ a: s.a, b: s.b }))`), which causes re-renders on every change or an infinite loop. Select single values or use `useShallow`.

## 235: What does "Object is possibly undefined" mean in TypeScript and how should you fix it?

With `strictNullChecks`, TypeScript knows a value may be `undefined` (for example from an optional property, `Array.find`, or a `Map.get`) and won't let you use it as if it always exists.

```ts
const user = users.find((u) => u.id === id);
user.name; // error: 'user' is possibly 'undefined'

if (!user) throw new Error(`User ${id} not found`);
user.name; // OK, narrowed
```

Prefer narrowing with checks, `?.` and `??`. The `!` non-null assertion turns off the check, so only use it when you are sure; if you are wrong you get a runtime error.

## 236: Why does TypeScript show no errors in the editor but fail in CI (or the other way)?

- The editor uses a different TypeScript version than the project (VS Code's bundled version vs the workspace version). Use "TypeScript: Select TypeScript Version" and choose the workspace one.
- The editor uses a different `tsconfig` than the build, for example in a monorepo or with `tsconfig.app.json` and `tsconfig.json`.
- The build tool (Vite, esbuild, SWC) only removes types and doesn't type check; the errors only show when running `tsc --noEmit`.
- Generated types (from GraphQL, Prisma, routes) are outdated locally or missing in CI.
- The editor's TS server needs a restart ("TypeScript: Restart TS Server").

## 237: How do you fix "Cannot find module or its corresponding type declarations"?

- Check the package is installed and the import path is correct (case matters on Linux CI but not on macOS or Windows).
- If the package has no types, install `@types/<name>`, or add a declaration file: `declare module "some-lib";`.
- For path aliases like `@/components`, make sure `paths` in `tsconfig.json` and the bundler config agree.
- For non-code imports (`.svg`, `.css`, `.png`), add the bundler's type declarations, like `/// <reference types="vite/client" />`.
- Check `moduleResolution` (`bundler` for most front-end projects) matches how the package defines its `exports`.

## 238: What is the difference between @ts-ignore and @ts-expect-error?

Both silence the TypeScript error on the next line. `@ts-expect-error` also reports an error if the next line has no error, so when the underlying problem is fixed, it reminds you to remove the comment. `@ts-ignore` stays silent forever.

Prefer `@ts-expect-error` with a comment explaining why. Both are a last resort; overusing them, or using `any`, hides real bugs.

## 239: How do you debug "Module not found" errors in a bundler?

- Read the full message: it shows the import path and the file that imports it.
- Check the path, extension and letter case. A file named `Button.tsx` imported as `./button` works on macOS but fails on Linux.
- For aliases, check the alias config in Vite (`resolve.alias`) or webpack (`resolve.alias`) and TypeScript `paths`.
- For packages, check they are in `dependencies`, installed, and that the import matches the package's `exports` field (deep imports like `pkg/dist/x` may be blocked).
- For Node built-ins (`fs`, `crypto`, `buffer`) imported in browser code, find which dependency pulls them in; webpack 5 and Vite don't polyfill them automatically.

## 240: How do you find what makes your JavaScript bundle so big?

Use a bundle analyzer:

- Vite or Rollup: `rollup-plugin-visualizer`, or `npx vite-bundle-visualizer`.
- webpack: `webpack-bundle-analyzer`, or `webpack --json > stats.json` and an online analyzer.
- Next.js: `@next/bundle-analyzer`, or the built-in bundle analyzer in recent versions.
- esbuild: `metafile: true` and the esbuild bundle analyzer website.

They show a treemap of every module and its size. Look for large libraries, duplicate copies of the same package, locales (like all `moment` or date library locales), and code that should be lazy-loaded. `source-map-explorer` works on any build with source maps.

## 241: Why isn't tree shaking removing unused code?

- The library is CommonJS (`require`/`module.exports`), which is hard to tree shake. Use its ES module build.
- You import the whole library (`import _ from "lodash"`) instead of named imports or per-function imports.
- The package doesn't declare `"sideEffects": false` in `package.json`, so the bundler keeps modules in case they have side effects.
- Your own code has top-level side effects, like registering things on import.
- Barrel files (`index.ts` re-exporting everything) can pull in more than needed, especially in development or with side effects.
- You are looking at a development build; tree shaking runs in production builds.

## 242: What does "Invalid hook call" mean in React, besides breaking the rules of hooks?

Besides calling hooks outside a component, this error often means there are two copies of React in the bundle, for example when a library brings its own `react`, or when using `npm link` with a local package that has its own `node_modules/react`.

Check with:

```bash
npm ls react
```

If you see more than one version, make the library list `react` as a peer dependency, deduplicate with `npm dedupe`, use `overrides` (npm) or `resolutions` (Yarn), or configure the bundler to resolve `react` to one path (`resolve.dedupe` in Vite).

## 243: How do you debug dependency version conflicts?

- `npm ls <package>` (or `pnpm why`, `yarn why`) shows which versions are installed and who requires them.
- Check peer dependency warnings during install; don't just add `--legacy-peer-deps` without understanding them.
- Look at the lockfile diff in the commit that broke things; a minor version bump in a sub-dependency can cause it.
- Force one version with `overrides` in `package.json` (npm), `pnpm.overrides`, or `resolutions` (Yarn).
- Check the library's changelog for breaking changes, even in minor versions.

```json
{
  "overrides": {
    "some-lib": "2.4.1"
  }
}
```

## 244: How do you debug "it works on my machine" build problems?

- Use the same Node.js version (`.nvmrc`, `engines`, or `packageManager` in `package.json`).
- Install with `npm ci` (or `pnpm install --frozen-lockfile`) so the lockfile is respected exactly.
- Delete `node_modules` and caches (bundler cache, `.next`, `node_modules/.vite`) and install again.
- Compare environment variables and `.env` files between machines.
- Check file name case sensitivity, since CI usually runs on Linux.
- Check the operating system and CPU for packages with native binaries (esbuild, sharp, SWC).

## 245: How do you fix problems caused by Vite's dependency pre-bundling cache?

Vite pre-bundles dependencies into `node_modules/.vite`. After installing, linking or patching a package, the cache can be stale and you may see old code, "Outdated Optimize Dep" errors (504), or duplicate module errors.

Restart with:

```bash
vite --force
```

or delete `node_modules/.vite`. For linked local packages or packages that cause trouble, add them to `optimizeDeps.include` or `optimizeDeps.exclude` in `vite.config`.

## 246: Why might CSS look different in production than in development?

- The order of CSS can change when the bundler splits CSS into chunks. Rules with the same specificity then win in a different order. Avoid relying on file order; use clearer selectors or cascade layers.
- CSS minifiers or PostCSS plugins can change or merge rules.
- Tailwind or other tools that scan files may remove classes built dynamically (like `"bg-" + color`) because they don't see the full class name.
- In development, styles are injected by JavaScript; in production they are `<link>` files that load at a different time.
- CSS modules generate different class names in production.

## 247: What date and time bugs are common in the front end?

- Parsing non-ISO strings like `"2024-01-15 10:00"` or `"01/15/2024"`: results differ between browsers, and older Safari returns `Invalid Date`. Use ISO format with `T` (`2024-01-15T10:00:00Z`) or a date library.
- `new Date("2024-01-15")` (date only) is parsed as UTC, but `new Date("2024-01-15T00:00")` is local time, so dates can show one day off.
- Time zone differences between server and browser, which also cause hydration mismatches.
- Months in `Date` are 0-based.
- Daylight saving time changes breaking "add one day" logic.

Use `Intl.DateTimeFormat` with an explicit `timeZone` when you format, and test with different time zones (DevTools Sensors panel can override the time zone).

## 248: How do you debug the 100vh problem on mobile browsers?

On mobile, the browser's address bar and toolbars appear and disappear while scrolling. `100vh` is the height with the bars hidden, so a `height: 100vh` element is taller than the visible area when the bars are shown, and bottom buttons can be hidden.

Use the dynamic viewport units:

```css
.full-screen {
  height: 100dvh; /* follows the current visible height */
  min-height: 100svh; /* smallest visible height */
}
```

DevTools device mode doesn't show this, so check on a real phone.

## 249: What touch and hover bugs happen on mobile devices?

- Hover styles stick after a tap on touch devices. Wrap hover styles in `@media (hover: hover) { ... }`.
- Menus that open only on hover can't be opened on touch screens.
- `click` events can be delayed or missing if `touchstart` handlers call `preventDefault()`.
- Elements too small to tap, or tap targets overlapping.
- `:active` styles not showing on iOS unless there is a touch listener.

Use pointer events (`pointerdown`, `pointerup`) for input that works with mouse, touch and pen.

## 250: How do you set up remote debugging for an Android device?

1. On the phone, enable Developer options and turn on USB debugging.
2. Connect the phone with USB and accept the debugging prompt.
3. On your computer, open `chrome://inspect#devices` in Chrome.
4. Your phone's open tabs appear; click "inspect" to open full DevTools for that tab.
5. To open your local dev server on the phone, use "Port forwarding" in the same page, for example forward port `5173` to `localhost:5173`.

WebViews in apps can be debugged too if the app enables `WebView.setWebContentsDebuggingEnabled(true)`.

## 251: How do you debug a page on an iPhone?

1. On the iPhone, open Settings, then Apps, then Safari, then Advanced, and turn on "Web Inspector".
2. Connect it to a Mac with a cable (or over the same network once paired).
3. In Safari on the Mac, enable the Develop menu (Settings, Advanced, "Show features for web developers").
4. Open the Develop menu, find your device, and click the page.

You get Safari's Web Inspector with Elements, Console, Sources, Network and more. The iOS Simulator in Xcode works the same way and is handy if you don't have a device.

## 252: How do you debug media query breakpoints?

- In device mode, the "Show media queries" option (in the three-dot menu) shows bars for every `min-width` and `max-width` breakpoint in your CSS; click a bar to resize to it.
- The Styles pane shows media queries above the rules they wrap, so you can see which ones match at the current size.
- Check the viewport meta tag. Without `<meta name="viewport" content="width=device-width, initial-scale=1">`, phones render at about 980px wide and your mobile media queries never match.
- Check for overlapping ranges, like `max-width: 768px` and `min-width: 768px` both matching at exactly 768px.

## 253: How do you debug container queries?

- The element with `container-type` shows a `container` badge in the Elements panel; clicking it highlights the container and its queried descendants.
- In the Styles pane, `@container` rules show which container they query; hover the container name to highlight it.
- Common bugs: forgetting `container-type: inline-size` on the parent, querying a container that is the element itself (an element can't query its own size), or a named container (`container-name`) with a typo.
- `container-type: size` needs the container to have an explicit height, or it collapses to zero.

## 254: How do you debug a missing accessible name?

An accessible name is what a screen reader reads for an element. Buttons with only an icon, inputs without labels, and links like "click here" are common problems.

Select the element and open the Accessibility pane. It shows the computed name and where it came from (`aria-labelledby`, `aria-label`, `<label>`, contents, `title`), in priority order. Fix it with visible text, a `<label for>`, or `aria-label` for icon buttons:

```html
<button type="button" aria-label="Close dialog">
  <svg aria-hidden="true">...</svg>
</button>
```

## 255: How do you debug focus problems?

- Add a live expression for `document.activeElement` and press `Tab` to see where focus goes.
- Check for missing focus styles (`outline: none` without a replacement); use `:focus-visible`.
- Check that modals move focus inside when opened, keep it inside while open, and return it when closed. The `<dialog>` element with `showModal()` does most of this.
- Check that removed elements don't leave focus on `body` (for example after deleting a list item).
- Check `tabindex` values: positive values change the tab order in confusing ways; use `0` or `-1`.

## 256: What ARIA mistakes cause accessibility bugs?

- Using ARIA instead of native elements, like `<div role="button">` without keyboard support. A real `<button>` gets focus, `Enter` and `Space` for free.
- `aria-hidden="true"` on an element that contains focusable elements, so keyboard users land on something screen readers can't see.
- Wrong or missing states, like `aria-expanded` not updated when a menu opens.
- `aria-labelledby` pointing to an id that doesn't exist.
- Roles that require child roles (like `listbox` needing `option` children) used without them.

The Accessibility pane and axe DevTools report most of these.

## 257: How do you check color contrast and vision issues in DevTools?

- In the Styles pane, click a color swatch. The color picker shows the contrast ratio against the background and whether it passes the AA and AAA levels, with a line showing which colors would pass.
- Lighthouse and the CSS Overview panel list low-contrast text.
- The Rendering tab can emulate vision deficiencies (blurred vision, reduced contrast, protanopia, deuteranopia, tritanopia, achromatopsia) to see the page like those users.
- Rendering can also emulate `prefers-contrast`, `prefers-color-scheme` and `forced-colors` to test high contrast and dark modes.

## 258: How do you test a CSP before enforcing it?

Use the `Content-Security-Policy-Report-Only` header. The browser reports violations in the console and to a reporting endpoint, but doesn't block anything:

```http
Content-Security-Policy-Report-Only: script-src 'self' 'nonce-abc123'; report-to csp
Reporting-Endpoints: csp="https://example.com/csp-reports"
```

In the page, you can also listen for violations:

```js
document.addEventListener("securitypolicyviolation", (e) => {
  console.log(e.violatedDirective, e.blockedURI, e.sourceFile, e.lineNumber);
});
```

Collect reports for a while, fix or allow what is legitimate, then switch to the enforcing header.

## 259: What is the Issues panel in Chrome DevTools?

The Issues panel collects problems Chrome found on the page that are not plain JavaScript errors: cookie problems (SameSite, third-party cookies), mixed content, CSP violations, CORS issues, deprecated features, accessibility and form problems (like inputs without labels or autocomplete), and more.

Each issue explains the problem and links to the affected requests or elements. When the console shows "N issues", click it to open this panel.

## 260: How do you find which third-party scripts slow down a page?

- In the Network panel, sort by domain, or use the "Group by frame" and "Big request rows" options. The "3rd-party requests" filter hides or shows third parties.
- In the Performance panel, the "3rd parties" insight lists each third party's main thread time and transfer size, and you can dim third-party entries in the flame chart.
- Lighthouse has a "Reduce the impact of third-party code" audit.
- Block a script with request blocking and measure again.

Load non-critical third parties with `async` or `defer`, after user interaction, or in a web worker with a tool like Partytown.

## 261: How do you debug code inside an iframe?

- In the Console, use the context dropdown (top left, usually "top") to switch to the iframe. Commands and `$0` then run in the iframe.
- In Sources, iframe files are listed under their own frame.
- In Elements, you can expand the iframe's `#document` to inspect its DOM (same-origin and cross-origin frames both show in Chrome).
- For `postMessage` bugs, log both sides and always check `event.origin`. A common bug is the wrong `targetOrigin` or the iframe not being loaded when the message is sent.

## 262: How do you debug a Web Worker?

- Workers appear in the Sources panel under "Threads"; set breakpoints in the worker file as usual.
- Pick the worker in the console's context dropdown to run code inside it.
- `console.log` from the worker shows in the main console.
- Errors in a worker fire an `error` event on the `Worker` object in the page; listen for it, since otherwise they are easy to miss.
- Data passed with `postMessage` is copied with the structured clone algorithm; functions, DOM nodes and class methods are lost, which causes "missing method" bugs.

```js
const worker = new Worker(new URL("./parser.js", import.meta.url), {
  type: "module",
});
worker.addEventListener("error", (e) =>
  console.error("worker error", e.message),
);
worker.addEventListener("messageerror", (e) =>
  console.error("could not deserialize", e),
);
```

## 263: How do you debug a failing Jest or Vitest test with breakpoints?

Run the test runner with the Node inspector and attach DevTools or VS Code:

```bash
# Vitest
npx vitest --inspect-brk --no-file-parallelism cart.test.ts

# Jest
node --inspect-brk node_modules/.bin/jest --runInBand cart.test.ts
```

Open `chrome://inspect` and click "inspect", then continue to your breakpoints or `debugger;` statements. In VS Code, the easier way is the "JavaScript Debug Terminal": run the same test command there and breakpoints in the editor work. The Vitest VS Code extension also has a debug button next to each test.

## 264: How do you see what React Testing Library is rendering?

- `screen.debug()` prints the current DOM (you can pass an element and a max length).
- `prettyDOM(element)` returns the same output as a string.
- `logRoles(container)` prints all elements by their ARIA role and name, which helps when `getByRole` doesn't find something.
- `screen.logTestingPlaygroundURL()` prints a link to Testing Playground with your DOM, where you can find the best query for an element.

When a `getBy` query fails, the error already prints the DOM. Read it to see what the user would see at that moment.

## 265: Why does getByText fail even though the text appears later?

`getBy` and `queryBy` queries check the DOM right now. If the text appears after a fetch, a timer or a state update, the query runs too early. Use `findBy`, which retries until the element appears (1000 ms by default), or `waitFor` for other assertions:

```js
render(<UserList />);
expect(await screen.findByText("Ana")).toBeInTheDocument();

await waitFor(() => expect(mockSave).toHaveBeenCalledTimes(1));
```

Warnings about updates not wrapped in `act(...)` usually mean the same thing: something updated after the test finished looking. Await the change instead of adding `act` manually.

## 266: Why does vi.mock or jest.mock not seem to work?

- The mock path must match the import path exactly as the module under test resolves it (aliases, extensions).
- `vi.mock` and `jest.mock` are hoisted to the top of the file, so variables you define above them aren't available inside the factory. Use `vi.hoisted()` in Vitest, or variables starting with `mock` in Jest.
- The code imports the module before the mock is set up, for example in a setup file.
- You mock a default export but the code uses a named export (or the other way).
- In ESM, you can't change an imported binding by assigning to it; mock the module instead.
- Mocks leak between tests if you don't reset them (`restoreMocks`, `clearMocks` config or `vi.restoreAllMocks()`).

## 267: How do you debug tests that use fake timers?

With fake timers (`vi.useFakeTimers()` or `jest.useFakeTimers()`), time only moves when you advance it. Common problems:

- The test hangs or times out because code waits for a timer you never advanced. Use `vi.advanceTimersByTime(ms)` or `vi.runAllTimers()`.
- Promises and timers mixed together: after advancing timers you also need to let promises resolve. Use the async versions like `await vi.advanceTimersByTimeAsync(ms)`.
- Testing Library's `findBy` and `waitFor` use timers internally; with fake timers they need the advance timers option or the runner's auto-advance setting.
- Forgetting `vi.useRealTimers()` in `afterEach`, so other tests break.

## 268: How do you debug a Cypress test?

- Use the Command Log in the Cypress app: click any command to see a snapshot of the page at that moment (time travel) and its details in the browser console.
- Add `cy.pause()` to stop the test and step through commands.
- Add `.debug()` after a command to open the debugger with the subject.
- Open the browser DevTools in the Cypress runner; `console.log` from the app and tests appear there.
- In CI, use screenshots on failure and video recording, and Cypress Cloud's Test Replay if you have it.

## 269: How do you debug a Playwright test?

- `npx playwright test --debug` opens the Playwright Inspector, pauses before each action, and highlights the locator on the page.
- `npx playwright test --ui` opens UI mode with a timeline, DOM snapshots for each step, the network log and console, and a watch mode.
- Add `await page.pause()` in a test to stop at that point.
- Record traces (`trace: "on-first-retry"` in the config) and open them with `npx playwright show-trace trace.zip` or trace.playwright.dev. A trace has every action, DOM snapshots before and after, network, console, and the source line.
- The VS Code Playwright extension lets you set breakpoints and run tests in debug mode.

## 270: How do you investigate a flaky end-to-end test?

1. Run it many times to see how often it fails: `npx playwright test my.spec.ts --repeat-each=50` (Playwright) or a loop in CI.
2. Collect traces, screenshots and videos for the failures, and compare them with passing runs.
3. Look for timing assumptions: fixed waits, checks that run before data loads, animations, or clicking an element that moves.
4. Look for shared state: tests using the same user or data, test order, leftover data from earlier tests.
5. Use web-first assertions that retry (`await expect(locator).toBeVisible()`) instead of manual checks, and wait for specific network responses when needed.
6. Fix the cause. Retries hide flakiness but don't fix it.

## 271: How do you handle failing snapshot tests?

First look at the diff. If the change is expected (you changed the component on purpose), update the snapshot (`vitest -u` or `jest -u`). If you didn't expect the change, it is a real regression or the snapshot includes unstable data.

Common causes of unstable snapshots are dates, random ids, generated class names and object key order. Mock time, use stable ids, and keep snapshots small (for example `toMatchInlineSnapshot` on a small part). Large snapshots that nobody reads tend to get updated without review, which makes them useless.

## 272: How do you set up Sentry so production errors are readable?

1. Install the SDK for your framework (`@sentry/react`, `@sentry/angular`, `@sentry/nextjs` and so on) and call `Sentry.init` early.
2. Set `release` (for example the git commit) and `environment`.
3. Upload source maps for each release with the Sentry build plugin (`@sentry/vite-plugin`, `@sentry/webpack-plugin`) or `sentry-cli`. Newer setups match maps with "debug IDs" injected into the files, so paths don't need to match exactly.
4. Delete or don't publish the `.map` files from your public server if you don't want them public.

```js
import * as Sentry from "@sentry/react";

Sentry.init({
  dsn: import.meta.env.VITE_SENTRY_DSN,
  release: import.meta.env.VITE_RELEASE,
  environment: import.meta.env.MODE,
  integrations: [
    Sentry.browserTracingIntegration(),
    Sentry.replayIntegration(),
  ],
  tracesSampleRate: 0.1,
  replaysOnErrorSampleRate: 1.0,
});
```

## 273: What extra context should you send with production errors?

- Release version and environment.
- User id (not personal data like email, unless your policy allows it) and account or tenant.
- Current route and relevant state, like the step of a checkout.
- Active feature flags and experiments.
- Breadcrumbs: recent clicks, navigations, network requests and console messages.
- Browser, OS and device (most tools add this automatically).

```js
Sentry.setUser({ id: user.id });
Sentry.setTag("plan", user.plan);
Sentry.setContext("cart", { items: cart.items.length });
```

## 274: How do you catch unhandled promise rejections globally?

Listen for the `unhandledrejection` event on `window`. `event.reason` is the rejection value (usually an `Error`).

```js
window.addEventListener("unhandledrejection", (event) => {
  reportError({
    message: event.reason?.message ?? String(event.reason),
    stack: event.reason?.stack,
  });
});
```

Error tracking SDKs do this automatically. If you see rejections with a reason that isn't an `Error` (like a string or a `Response` object), the stack is missing; reject with `Error` objects so you get a stack trace.

## 275: Why do you see "Script error." with no details?

When a script from another origin throws an error, the browser hides the details from `window.onerror` for security, and you only get the message "Script error." with no file, line or stack.

To get details, load the script with the `crossorigin` attribute and make the server send a CORS header:

```html
<script src="https://cdn.example.com/app.js" crossorigin="anonymous"></script>
```

```http
Access-Control-Allow-Origin: https://www.example.com
```

This matters when your own bundles are served from a CDN domain.

## 276: What should you log in the front end in production, and what should you avoid?

Log things that help you understand failures: errors with context, failed requests (URL, status, duration, request id), important user actions in a flow, and unexpected states. Use levels (`debug`, `info`, `warn`, `error`) and structured data, not free text.

Avoid logging passwords, tokens, full credit card numbers, personal data and full request bodies. Don't ship noisy `console.log` calls; remove them at build time or use a logger that can be turned on with a flag. Include a request or trace id so front-end logs can be matched with back-end logs.

## 277: How do you reduce noise in production error reports?

- Ignore errors from browser extensions (stack frames from `chrome-extension://` or `moz-extension://`).
- Filter known harmless errors like `ResizeObserver loop completed with undelivered notifications`, and errors from bots or very old browsers.
- Use the `allowUrls` option (in Sentry) to only report errors from your own scripts.
- Group errors correctly with release tracking and source maps, so the same bug isn't split into many issues.
- Set up alerts on new issues and on spikes, not on every single event.

## 278: How do you debug a bug that only some users see because of a feature flag?

- Make sure error reports and logs include the active flags and variants for that user.
- Check the flag tool's targeting rules and recent changes; a rule change is like a deploy.
- Reproduce by forcing the same flag values locally, using the flag SDK's override feature, a query parameter or a local override file.
- Turn the flag off for affected users to stop the damage while you fix it.
- Remove old flags; many combinations of old flags make bugs harder to reproduce.

## 279: How do you configure VS Code to debug a Vite or React app in Chrome?

Create `.vscode/launch.json`:

```json
{
  "version": "0.2.0",
  "configurations": [
    {
      "type": "chrome",
      "request": "launch",
      "name": "Debug app in Chrome",
      "url": "http://localhost:5173",
      "webRoot": "${workspaceFolder}"
    }
  ]
}
```

Start the dev server (`npm run dev`), then press `F5`. VS Code opens a Chrome window connected to the debugger, and breakpoints you set in your `.tsx` files work through source maps. If breakpoints show as "unbound", check that source maps are on and `webRoot` points to the folder the source paths are relative to.

## 280: How do you capture console errors and failed requests with Puppeteer?

```js
import puppeteer from "puppeteer";

const browser = await puppeteer.launch();
const page = await browser.newPage();

page.on("console", (msg) => {
  if (msg.type() === "error") console.log("console error:", msg.text());
});
page.on("pageerror", (err) => console.log("page error:", err.message));
page.on("requestfailed", (req) =>
  console.log("failed:", req.url(), req.failure()?.errorText),
);
page.on("response", (res) => {
  if (res.status() >= 400) console.log(res.status(), res.url());
});

await page.goto("https://example.com", { waitUntil: "networkidle0" });
await browser.close();
```

This is useful as a quick smoke check after a deploy, or to reproduce a bug automatically many times.

## 281: How do you record reproduction steps for a bug without writing code?

- Chrome's Recorder panel records clicks, typing and navigation as a user flow. You can replay it, slow it down, add assertions, measure its performance, and export it as a Puppeteer or Playwright script (with extensions) or JSON to share.
- Playwright's codegen records actions into test code: `npx playwright codegen https://example.com`.
- Session replay tools record real user sessions in production.

A recorded flow is a great attachment for a bug report.

## 282: How do you use AI assistance in DevTools to debug a style problem?

Select the element, right-click and choose "Debug with AI" (or open the AI assistance panel), then ask a question like "Why is this element not centered?". The assistant looks at the element, its styles and its parent's layout, explains what it found, and can run code on the page to check values. It can suggest CSS changes and apply them so you can see the result, and you can then copy them from the Changes panel.

Treat it like a colleague's guess: check the answer in the Styles and Computed panes before you trust it. Don't use it on pages with sensitive data unless your company allows it, since page data is sent to the model.

## 283: What do you check when something works locally but breaks in production?

- Different build: minification, tree shaking, dev-only code paths, `process.env.NODE_ENV` checks.
- Environment variables and API URLs.
- HTTPS vs HTTP: mixed content, `Secure` cookies, APIs that need a secure context.
- Different domain: CORS, cookie domains, `SameSite`.
- CSP headers that only exist in production.
- Caching layers: CDN, service worker.
- Real data that is bigger or has edge cases your test data doesn't.
- Third-party scripts only loaded in production.

## 284: How do you debug a blank white screen in a single page app?

1. Open the console: a white screen almost always has an uncaught error, a failed chunk load, or a CSP block.
2. Check the Network panel: did the main JS bundle load (200, not 404 or HTML instead of JS)? A wrong `base` path after deploying to a subfolder is common.
3. Check the Elements panel: is the root element empty, or is content rendered but hidden by CSS?
4. In React, an error during render without an error boundary unmounts the whole app; add error boundaries.
5. Check for old browser support: modern syntax in the bundle that an old browser can't parse.

## 285: How do you debug a page that freezes completely?

The main thread is stuck, usually in an infinite loop or a very long task.

1. Open DevTools (if possible before triggering the freeze), go to Sources, and click the pause button (or `F8`). The debugger stops wherever the code is running, which shows you the loop.
2. If DevTools also freezes, open Chrome's Task Manager to see the CPU use and kill the tab.
3. Record a Performance trace while reproducing a shorter version of the freeze to see which function takes the time.
4. Check for `while` loops with wrong exit conditions, recursion, or effects that keep triggering each other.

## 286: How do you debug a slow initial page load?

1. Record a Performance trace with "Reload" and CPU and network throttling on.
2. Look at the insights: LCP breakdown, render-blocking requests, network dependency tree, document request latency.
3. In the Network panel waterfall, look for chains: HTML, then JS, then API call, then image. Each step waits for the previous one.
4. Check bundle sizes and the Coverage tab for unused code.
5. Check caching and compression headers (`Content-Encoding: br` or `gzip`).
6. Compare with field data (CrUX, RUM) to make sure you are fixing what real users experience.

## 287: How do you debug "404 on refresh" in a single page app?

The app uses client-side routing (like `/dashboard/settings`), which works when you navigate inside the app. But on refresh, the browser asks the server for `/dashboard/settings`, and the server has no such file.

Configure the server or hosting to return `index.html` for unknown paths (a "fallback" or "rewrite" rule), while still returning real 404s for missing static files. If you deploy to a subfolder, also set the router's base path and the bundler's `base` option.

## 288: How do you debug back/forward cache (bfcache) issues?

The bfcache keeps a full copy of a page in memory when you navigate away, so going back is instant. Pages that can't use it reload instead, which is slower, and pages that do use it may show stale data.

- In Application, then "Back/forward cache", click "Test back/forward cache" to see if the page is eligible and the reasons if it is not (for example an `unload` listener, `Cache-Control: no-store`, or an open WebSocket or IndexedDB connection in some cases).
- Listen to `pageshow` with `event.persisted` to refresh data when a page is restored from bfcache.

```js
window.addEventListener("pageshow", (event) => {
  if (event.persisted) refreshCartCount();
});
```

## 289: How do you debug CSS animations and transitions?

Open the Animations panel (Command Menu, "Show Animations"). It records animations as they play, shows them on a timeline, and lets you replay, slow them down to 25% or 10%, scrub through them, and change their timing and delays.

Also check:

- Transitions don't run on `display: none` to `display: block` without newer features like `transition-behavior: allow-discrete` and `@starting-style`.
- `transition: all` can animate things you didn't expect.
- Animations of `width`, `height`, `top` or `left` cause layout on every frame; prefer `transform`.
- Users with `prefers-reduced-motion: reduce` should get less motion; you can emulate it in the Rendering tab.

## 290: How do you debug a scroll position bug in a single page app?

- When navigating between routes, the scroll position may stay where it was. Most routers have a scroll restoration option; check it is on.
- `history.scrollRestoration` can be `auto` or `manual`; libraries sometimes set it to `manual` and then don't restore.
- Content loaded after navigation changes the page height, so restored positions point to the wrong place. Restore after the content is ready, or reserve space.
- `scroll-behavior: smooth` on `html` makes programmatic jumps animate, which can look like a bug.
- Fixed headers covering anchor targets; use `scroll-margin-top`.

## 291: How do you debug a "ChunkLoadError" or "Failed to fetch dynamically imported module"?

These errors happen when the app tries to load a lazy chunk and the request fails. Common causes:

- A new deploy removed the old chunk files, and a user with an old tab open navigates to a lazy route.
- Wrong `base` or `publicPath`, so chunks are requested from the wrong URL.
- A network error, ad blocker or CSP blocking the file.

Check the failed URL in the Network panel. Keep old chunk files for some time after a deploy, and handle the error by reloading the page once (Vite fires a `vite:preloadError` event on `window` you can listen to).

## 292: How do you debug an element that jumps or flickers on hover?

- The hover style changes the element's size (border, padding, font weight), which changes layout and moves the mouse off the element, which removes the hover. Use `outline`, `box-shadow` or `transform` instead, or reserve the space.
- A tooltip or menu that appears under the cursor takes the hover away from the trigger.
- A transition on `all` animates properties you didn't mean to.

Force the `:hover` state in the Styles pane (`:hov`) to inspect it without moving the mouse.

## 293: How do you debug wrong text encoding or broken characters?

Broken characters like `Ã©` instead of `é` mean UTF-8 text was read as another encoding (or the other way).

- Check the `Content-Type` response header has `charset=utf-8`, and the HTML has `<meta charset="utf-8">` early in the `<head>`.
- Check the file itself is saved as UTF-8.
- For API data, check the server and database use UTF-8 end to end.
- For downloads or file reading in JavaScript, use `TextDecoder` with the right encoding.

## 294: How do you debug a form that the browser autofills incorrectly?

- Use the correct `autocomplete` values (`email`, `username`, `current-password`, `new-password`, `one-time-code`, `street-address`, `postal-code` and so on). Browsers rely on them.
- Make sure each input has a correct `name`, `type` and a `<label>`.
- Autofill may fill the field without firing the events your framework listens to in older setups; check that the form state matches what is shown.
- Chrome's Autofill panel in DevTools shows how fields were classified and which values were filled.
- The Issues panel reports form problems like duplicate ids or missing labels.

## 295: How do you debug a bug that only happens in one browser?

1. Confirm the exact browser and version, and reproduce it there.
2. Check the console in that browser; error messages differ between engines.
3. Check compatibility for every feature in the area (MDN, caniuse) and whether you need a polyfill or a fallback.
4. Reduce it to a minimal case (a small HTML file) and compare it across browsers.
5. Check vendor-specific behavior: Safari's date parsing, form control styling, flexbox gap in very old versions, `position: sticky` in tables.
6. If it is a browser bug, search the browser's bug tracker and look for a known workaround.

## 296: How do you debug a dark mode bug?

- Use the Rendering tab to emulate `prefers-color-scheme: dark` or `light` without changing your system settings.
- Check that all colors use your variables or tokens; hard-coded colors are the usual cause.
- Check images, icons and SVGs that assume a white background.
- Check `color-scheme` (on `:root` or with a meta tag) so form controls and scrollbars match the theme.
- For a theme toggle stored in `localStorage`, a "flash" of the wrong theme on load means the theme is applied too late; set it with a small inline script in the `<head>` before the page renders.

## 297: How do you debug a print layout?

In the Rendering tab, set "Emulate CSS media type" to `print`. The page then uses your `@media print` styles in the normal viewport, so you can inspect them with the Elements panel. Use the browser's print preview to see page breaks.

Common problems are hidden content that should print, navigation and ads that shouldn't, backgrounds missing (browsers skip them by default), and page breaks in the middle of elements; use `break-inside: avoid`.

## 298: How do you debug a problem in a production site you can't change?

- Use Local Overrides to change JS, CSS, HTML or response headers locally and test a fix.
- Use request blocking to remove a script and see if the problem goes away.
- Use the console and breakpoints on the pretty-printed code; load the source map manually if you have it.
- Use "Copy as cURL" to reproduce API calls outside the browser.
- Use the Recorder to save the reproduction steps for the team that owns the site.

## 299: How do you find which micro frontend owns a part of the page?

- Look at the Elements panel for markers: custom element tag names, `data-*` attributes or root containers that each micro frontend uses.
- In the Sources panel, check which bundle or remote entry the code comes from (different origins or paths per app).
- In React or Angular DevTools, check if there are several separate roots or apps on the page.
- Agree on a convention, like adding `data-mfe="checkout"` and the version to each app's root element, and including the app name in error reports.

## 300: What should a good bug report contain?

- A short title that describes the problem, not the guess about the cause.
- Steps to reproduce, starting from a clear state (logged in as which user, which page).
- Expected result and actual result.
- Environment: browser and version, OS, device, app version or release, feature flags.
- Evidence: screenshots or a video, console errors, failed requests (or a sanitized HAR file), and the error tracking link.
- How often it happens and how many users are affected.

A good report saves a lot of debugging time, and writing one is a good habit even for your own bugs.

# Advanced Questions (301-450)

## 301: How does a source map work internally?

A source map is a JSON file, standardized as ECMA-426. Its main fields are:

- `sources`: the original file paths.
- `sourcesContent`: optional copies of the original code, so DevTools can show it without fetching the files.
- `names`: original identifiers, like variable and function names.
- `mappings`: a long string that maps positions in the generated file to positions in the original files.
- `ignoreList`: indexes of sources that debuggers should skip (like library code).

`mappings` is split by `;` for each generated line and `,` for each segment. Each segment is encoded with Base64 VLQ and stores relative numbers: generated column, source index, original line, original column, and optionally a name index. Values are relative to the previous segment, which keeps the file small. DevTools decodes this into a lookup table to translate positions both ways.

## 302: Why might source maps point to the wrong line?

- The code goes through several tools (TypeScript, Babel, a bundler, a minifier), and one step doesn't pass on or combine the previous step's map, so the final map only maps to an intermediate file.
- A plugin changes code without producing a source map for its change (for example a custom string replace plugin), which shifts everything after it.
- The map is from a different build than the file that is running, for example after a deploy or because of caching.
- Cheap source map modes (like webpack's `cheap-*` options) only map lines, not columns, so the position inside a long line is wrong.

To check, use a source map visualizer (like `source-map-visualization`) on the generated file and its map, and test each build step separately.

## 303: Why do stack traces still show minified function names even with source maps?

Source maps map positions, and the `names` field maps identifiers at specific positions. But a stack trace frame names the function that contains the position, and the browser takes that name from the running (minified) code. Many tools only translate the file, line and column, not the function name.

Some tools (Sentry, newer DevTools versions) look at the original source around the mapped position to find the real function name. There is also a "scopes" proposal for source maps that would describe original functions and variables directly, so debuggers can show correct names and scopes in minified code.

## 304: What are the security concerns of source maps in production?

Public source maps with `sourcesContent` expose your full original code: comments, internal URLs, feature names, sometimes hard-coded keys that should not have been there. Front-end code is never secret, but source maps make it much easier to read.

Common approaches:

- Generate hidden source maps and upload them only to your error tracking tool.
- Serve maps only to internal users (for example behind VPN or authentication).
- Never put secrets in front-end code, maps or not.

Some teams decide public maps are fine for open debugging; it is a trade-off, but it should be a decision, not an accident.

## 305: How does V8 build stack traces, and what limits them?

When an `Error` is created, V8 captures the current stack and formats `error.stack` lazily the first time you read it. By default it keeps 10 frames, controlled by `Error.stackTraceLimit`. You can raise it while debugging:

```js
Error.stackTraceLimit = 50;
```

`Error.captureStackTrace(obj, fn)` (V8 only) adds a `stack` property to any object and can hide frames above `fn`, which is useful in custom error helpers. For `await` chains, V8 adds `async` frames to the stack string ("zero-cost async stack traces") by following the promise chain. For callbacks like `setTimeout` or event listeners, only DevTools (with async stack tagging) can show where they were scheduled, not `error.stack`.

## 306: How do Error.cause and AggregateError help debugging?

`Error.cause` lets you wrap a low-level error in a more meaningful one without losing the original:

```js
try {
  await saveOrder(order);
} catch (err) {
  throw new Error(`Could not save order ${order.id}`, { cause: err });
}
```

DevTools and error tracking tools show the cause chain, so you see both "Could not save order 42" and the original network or validation error.

`AggregateError` holds several errors at once. `Promise.any` rejects with one when all promises fail, and you can create your own when validating many items. Both are much better than `catch (e) { throw new Error("failed") }`, which throws away the real reason.

## 307: Why does instanceof fail for errors or arrays from an iframe or a different realm?

Each realm (a window, an iframe, a worker, a Node `vm` context) has its own copies of built-in constructors like `Array`, `Error` and `Object`. An array created in an iframe is an instance of the iframe's `Array`, not the main page's, so `value instanceof Array` is `false`.

This also happens with two copies of a library: `err instanceof ApiError` fails if the error was created by a different copy of the package. Use checks that work across realms, like `Array.isArray()`, a `name` or `code` property on errors, or symbol-based brand checks (`Symbol.for(...)`), and remove duplicate packages.

## 308: Why does a bug disappear when DevTools is open or when you add a console.log?

These are sometimes called "heisenbugs". Common reasons:

- **Timing:** DevTools, breakpoints and logging slow things down, which changes the order of async operations and hides a race condition.
- **Cache:** "Disable cache" is often on when DevTools is open, so the page loads fresh files.
- **Layout:** opening DevTools changes the viewport size, which changes media queries and layout.
- **Getters and lazy values:** expanding an object in the console calls getters, which can trigger side effects or load data.
- **Focus:** DevTools takes focus from the page, so `focus`/`blur` and `visibilitychange` behave differently.

Use logpoints or a ring buffer of logs (store events in an array and print later), undock DevTools into a separate window, and record a Performance trace instead of stepping through code.

## 309: How do you debug a production bug in minified code when you don't have source maps?

- Pretty print the file in Sources (`{}`), then search for nearby string literals from the error message, API URLs, or CSS class names; strings are not minified.
- Set a breakpoint on the minified line and column from the stack trace, reproduce, and read the values in Scope.
- Use XHR/fetch, DOM or event listener breakpoints to land in the right place without knowing the code.
- Compare with your own source: the structure (order of functions, string constants) usually matches closely.
- Rebuild the same commit locally with source maps on. If the build is deterministic, the maps will match the production files.

## 310: Walk through finding a memory leak that grows with every route change in a single page app.

1. Open the Performance panel with the Memory checkbox on, record while navigating between two routes 10 times, and click the garbage collection icon at the end. A JS heap or DOM node count that keeps rising in steps confirms the leak.
2. In the Memory panel, take a snapshot after the first navigation, then navigate back and forth 10 times, collect garbage, and take another snapshot.
3. Use the Comparison view and sort by "# Delta". Look for component instances, detached elements or arrays that grew by around 10.
4. Select one leaked object and read its Retainers path from the bottom up. It usually ends at a global: a store subscription, a `window` listener, a module-level cache, an interval, or a third-party library's registry.
5. Fix the cleanup (unsubscribe, remove the listener, clear the timer, limit the cache) and repeat the test to confirm the delta is gone.

## 311: How can closures keep more memory alive than you expect?

In V8, all closures created in the same function share one context object for the variables they capture. If one closure captures a large variable and another long-lived closure captures something small, the long-lived one can still keep the large variable alive, because they share the context.

```js
function setup() {
  const bigData = new Array(1e6).fill("x");
  const unused = () => bigData.length; // captures bigData
  return () => console.log("tick"); // shares the context, so bigData may stay alive
}
const tick = setup();
```

In a heap snapshot, this shows as a `(closure)` whose `context` retains the big object. Fix it by not capturing large values in closures near long-lived callbacks, setting them to `null` when done, or moving the long-lived function to a separate scope.

## 312: How can WeakMap, WeakRef and FinalizationRegistry help with memory bugs?

- `WeakMap` and `WeakSet` hold keys weakly, so attaching data to DOM nodes or objects doesn't keep them alive. Using a `Map` for this is a common leak.
- `WeakRef` lets you keep a reference that doesn't prevent garbage collection, for caches.
- `FinalizationRegistry` runs a callback after an object is collected. In debugging and tests, you can use it to check that objects you expect to be freed actually are:

```js
const registry = new FinalizationRegistry((name) =>
  console.log("collected", name),
);

function mountWidget() {
  const widget = createWidget();
  registry.register(widget, "widget");
  return widget;
}
```

If "collected" never appears after unmounting and forcing GC (in DevTools or with `node --expose-gc`), something still holds the widget. Don't rely on finalizers for app logic; their timing is not guaranteed.

## 313: How do RxJS subscriptions cause leaks in Angular, and how do you find them?

A subscription to a long-lived observable (a service `Subject`, `interval`, a store, a WebSocket stream, router events) keeps the callback and the component it closes over alive until you unsubscribe. Each time the component is created, a new subscription adds up.

To find them, take heap snapshots after creating and destroying the component several times, and look for component instances retained by `Subscriber` or `SafeSubscriber` objects. To fix them, prefer the `async` pipe or `toSignal()`, which clean up automatically, or use `takeUntilDestroyed()`:

```ts
export class PriceComponent {
  private prices = inject(PriceService);

  constructor() {
    this.prices.updates$
      .pipe(takeUntilDestroyed())
      .subscribe((p) => this.render(p));
  }
}
```

HTTP observables complete on their own, so they rarely leak.

## 314: How do memory leaks typically happen in React apps?

- Effects that subscribe or add listeners without returning a cleanup function.
- Storing DOM nodes, component instances or callbacks in global stores, module-level variables or caches that never shrink.
- Third-party libraries (charts, maps, editors) created in an effect and never destroyed.
- Large data kept in state of components that stay mounted (for example hidden tabs).

Note that React 18 removed the "Can't perform a React state update on an unmounted component" warning, because it was usually a false alarm; so you won't get a warning. Use heap snapshots and look for detached elements and fiber objects that grow after mounting and unmounting. React keeps two fiber trees (current and alternate), so you may see components retained for one extra render; that is normal, steady growth is not.

## 315: How can you measure memory usage in production?

`performance.measureUserAgentSpecificMemory()` returns an estimate of memory used by the page, broken down by frames and workers. It only works on cross-origin isolated pages (`COOP: same-origin` and `COEP: require-corp` or `credentialless`), and the result can take a while because it waits for garbage collection.

```js
if (crossOriginIsolated && performance.measureUserAgentSpecificMemory) {
  const result = await performance.measureUserAgentSpecificMemory();
  sendToAnalytics({ bytes: result.bytes });
}
```

Measure at random intervals in a sample of sessions and look at growth over session length. The older `performance.memory` (Chrome only) is not reliable for this. Crash reports (`Reporting API` with `crash` reports, including out-of-memory reasons) also help.

## 316: What is the Long Animation Frames API and why is it better than the Long Tasks API for debugging?

The Long Animation Frames API (LoAF) reports frames that took more than 50 ms from start to paint. Unlike Long Tasks, it covers the whole frame (several tasks, rendering, `requestAnimationFrame` callbacks) and gives details about which scripts ran:

```js
new PerformanceObserver((list) => {
  for (const entry of list.getEntries()) {
    for (const script of entry.scripts) {
      console.log(
        script.sourceURL,
        script.sourceFunctionName,
        script.invoker, // for example "BUTTON#buy.onclick"
        Math.round(script.duration),
        Math.round(script.forcedStyleAndLayoutDuration),
      );
    }
  }
}).observe({ type: "long-animation-frame", buffered: true });
```

In the field this tells you which script (yours or third party) causes slow interactions. The `web-vitals` attribution build includes LoAF entries for INP.

## 317: How do you debug a high INP caused by presentation delay?

Presentation delay is the time after your handlers finish until the next frame is painted: style recalculation, layout, paint and compositing for the changes you made.

1. In a Performance trace, find the interaction and look at the main thread after the handler: big purple (style/layout) or green (paint) blocks.
2. Check the DOM size: changing a class on `body` can force style recalculation for thousands of elements.
3. Enable "CSS selector stats" in the Performance panel settings to see which selectors are expensive during style recalculation.
4. Reduce the work: render fewer elements (virtualization, `content-visibility: auto`), change classes on smaller subtrees, avoid layout-triggering animations, and show quick visual feedback first, then do the heavy update after yielding.

## 318: How do you find expensive CSS selectors?

In the Performance panel settings, turn on "Enable CSS selector stats (slow)" and record. Click a "Recalculate style" event, then open the "Selector stats" tab. It lists selectors with time spent, match attempts and match count.

Selectors with many match attempts but few matches are the main cost, for example selectors ending in a universal or very common element (`.sidebar *`, `div span`), or complex `:has()` selectors on large DOMs. Fix them by using classes on the target elements, scoping rules, and reducing the number of elements affected by a change.

## 319: How do layers and compositing affect rendering bugs?

The browser may put some elements on their own compositor layers (for example with `transform: translateZ(0)`, `will-change: transform`, video, canvas, or animated `opacity`/`transform`). Layers can be moved and faded by the GPU without repaint, which makes animations smooth.

Too many layers use a lot of GPU memory and can make things slower, and layer changes can cause visual bugs like blurry text (subpixel positioning on layers), flicker, or elements drawn above things they shouldn't be. Use the Layers panel to see layers, why each was created ("compositing reasons") and their memory, and "Layer borders" in the Rendering tab. Use `will-change` only on elements that are about to animate, and remove it after.

## 320: How do you debug scroll jank?

1. Record a Performance trace while scrolling and look for long tasks and dropped frames in the Frames track.
2. Turn on "Scrolling performance issues" in the Rendering tab; it highlights elements with non-passive wheel or touch listeners that make scrolling wait for the main thread.
3. Look for scroll listeners that read layout and write styles on every event (sticky headers, parallax). Replace them with CSS (`position: sticky`, scroll-driven animations) or `IntersectionObserver`.
4. Check paint flashing: large repaints on each scroll frame point to fixed backgrounds, big shadows or elements that aren't on their own layer.
5. Check for images decoding on the main thread or huge DOM sections coming into view; use `content-visibility` and properly sized images.

## 321: What bugs can content-visibility: auto cause?

`content-visibility: auto` skips rendering of off-screen sections, which can make long pages much faster. Bugs it can cause:

- The scrollbar jumps, because skipped sections have no size. Set `contain-intrinsic-size: auto 500px` so the browser uses an estimated size and remembers the real one after rendering.
- Code that measures elements (`getBoundingClientRect`) in skipped sections gets estimated sizes.
- Anchor links and scroll restoration may land in the wrong place for the same reason.

Find-in-page and accessibility still work, since the content stays in the DOM. Chrome fires `contentvisibilityautostatechange` events when an element starts or stops being skipped, which helps when debugging.

## 322: Why can LCP look good in Lighthouse but bad in the field?

- Lighthouse runs on one simulated device and network; real users have slower phones and networks.
- Lighthouse loads the page with a cold cache from one location; users come from many regions, some far from your servers or CDN.
- Real users land on many pages, often with cookie banners, personalized content or A/B tests that Lighthouse doesn't see.
- Field LCP includes users who arrive from ads with redirect chains or slow `TTFB` on uncached pages.
- The LCP element can be different for real users, for example a banner image on mobile.

Segment field data by device, page type, country and connection, use the attribution build of `web-vitals` to collect the LCP element and its breakdown, and reproduce with matching throttling.

## 323: How are Web Vitals measured differently in single page apps?

Core Web Vitals are measured per page load. In a single page app, route changes are "soft navigations": the URL changes but there is no new page load, so LCP is not measured again, and CLS and INP keep adding up across all routes for the whole session (CLS uses the largest session window).

This makes it hard to know which route has the problem. Track the route in your RUM data with each metric, and break down INP and layout shifts by the route they happened on. Chrome has been working on a Soft Navigations API to measure LCP and other metrics per soft navigation; check its current status before relying on it.

## 324: How do you use React's Performance Tracks in Chrome DevTools?

Since React 19.2, React adds custom tracks to the Chrome Performance panel in development and profiling builds:

- **Scheduler:** shows what React is working on by priority (for example "Blocking" for user input and "Transition" for `startTransition` updates), including when work is waiting or blocked.
- **Components:** shows which components rendered or ran effects and how long each took, as a flame chart, next to the browser's own tracks.

Record a trace as usual and look at these tracks together with the main thread. This shows, for example, that a slow click is caused by a large transition render or by an effect, without switching to the React Profiler.

## 325: How do you add your own markers to a Performance trace?

Use the User Timing API. Marks and measures show in the "Timings" track:

```js
performance.mark("checkout:start");
await submitOrder();
performance.measure("checkout", "checkout:start");
```

Chrome also supports an extension to put entries in your own custom track, with colors and tooltips:

```js
const start = performance.now();
renderChart(data);
performance.measure("Render chart", {
  start,
  detail: {
    devtools: {
      dataType: "track-entry",
      track: "Charts",
      color: "tertiary",
      tooltipText: `${data.length} points`,
    },
  },
});
```

`console.timeStamp()` with extra arguments can also add entries to custom tracks with very little overhead. These markers make traces much easier to read for code you care about.

## 326: How does React recover from hydration errors, and why does it matter for debugging?

When hydration fails, React 18 and later don't keep the broken HTML. React throws away the server HTML up to the nearest `<Suspense>` boundary and renders that part again on the client. If there is no boundary, the whole root is client-rendered.

So the user may see the page "flash" and the app works, but you lose the benefit of SSR and pay double rendering cost. These errors go to `onRecoverableError` on the root, so they are easy to miss if you only watch uncaught errors. Report them to your monitoring, and use the diff in the development console message to find the mismatch.

## 327: How do you debug errors in React Server Components?

- In development, the error shows in the terminal and in the browser overlay with the server stack. Server logs replayed in the browser console are marked as coming from the server.
- In production, the client only gets a generic message and a `digest` string. Log the full error on the server (for example with `onRequestError` in Next.js's `instrumentation.ts`) and search by digest.
- "Only plain objects can be passed to Client Components" means you passed a class instance, `Date`-like object the serializer can't handle, a `Map` in older versions, or a function. Convert it to plain data first.
- Errors in async Server Components are caught by the nearest `error.js` boundary (in Next.js), which must be a Client Component.

## 328: What is tearing in React and how do you debug it?

Tearing is when different parts of the UI show different values of the same data during one render. It can happen with concurrent rendering when a component reads from an external mutable store (a global variable, a custom event emitter) that changes in the middle of a render that React paused and resumed.

Symptoms are short moments where two components show different values. Fix it by reading external stores with `useSyncExternalStore`, which React designed to keep all components consistent:

```jsx
const width = useSyncExternalStore(
  (callback) => {
    window.addEventListener("resize", callback);
    return () => window.removeEventListener("resize", callback);
  },
  () => window.innerWidth,
  () => 1024, // server snapshot
);
```

Store libraries like Redux and Zustand already use it.

## 329: Why does a component suspend forever or keep refetching with use() or Suspense?

`use(promise)` and Suspense expect the same promise across renders while it is pending. If you create the promise during render, every render creates a new one, so React suspends again and again, or fetches in a loop:

```jsx
// Bug: new promise on each render
function Profile({ id }) {
  const user = use(fetchUser(id));
  return <h1>{user.name}</h1>;
}
```

Create the promise outside render (in a parent Server Component, a loader, or an event), or cache it by key with a data library or a small cache. Also check for Suspense waterfalls, where nested components start fetching only after the parent finished; the Network panel shows these requests running one after another instead of in parallel.

## 330: How do you prevent and debug race conditions in useEffect data fetching?

When `id` changes quickly, older requests may finish after newer ones and set old data. Use an abort signal or an "ignore" flag in the cleanup:

```jsx
useEffect(() => {
  const controller = new AbortController();

  fetch(`/api/users/${id}`, { signal: controller.signal })
    .then((res) => res.json())
    .then(setUser)
    .catch((err) => {
      if (err.name !== "AbortError") setError(err);
    });

  return () => controller.abort();
}, [id]);
```

To reproduce the race, throttle the network and add a random delay on the mock server, then switch quickly between items. In development, StrictMode's double effect run also shows whether your cleanup works: you should see one request cancelled in the Network panel.

## 331: How do you debug a re-render storm caused by React context?

Every component that uses a context re-renders when the context value changes, even if it only uses one field. If a provider passes a new object on every render, all consumers render every time the provider renders.

```jsx
// Bug: new object each render
<AuthContext.Provider value={{ user, login, logout }}>

// Better: stable value (or let the React Compiler memoize it)
const value = useMemo(() => ({ user, login, logout }), [user, login, logout]);
<AuthContext.Provider value={value}>
```

In the Profiler with "why did this render", consumers show "Context changed". Split large contexts into smaller ones (state vs actions), keep fast-changing values out of global context, or use a store with selectors for data that changes often.

## 332: How do you find zone pollution in a zone.js Angular app?

In apps that still use zone.js, every `setTimeout`, `requestAnimationFrame`, event listener or promise inside the Angular zone triggers app-wide change detection. Third-party libraries (charts, maps, analytics) with frequent timers or `mousemove` listeners can cause hundreds of change detection cycles per second.

Use the Angular DevTools Profiler: many cycles with the "source" shown as a timer or event you didn't trigger point to pollution. Run that library outside Angular:

```ts
private ngZone = inject(NgZone);

ngAfterViewInit() {
  this.ngZone.runOutsideAngular(() => {
    this.chart = createChart(this.el.nativeElement);
  });
}
```

Re-enter with `ngZone.run()` only when you need to update the view. Moving to zoneless with signals removes this class of problem.

## 333: What causes NG0600 and infinite loops with Angular signals?

`NG0600` means you wrote to a signal where it isn't allowed, for example inside a `computed` or during template rendering. `computed` must be pure: it derives a value, it doesn't set other state.

Effects may write to signals (since Angular 19 the `allowSignalWrites` flag is no longer needed), but an effect that reads a signal and then writes to the same signal, or two effects that update each other, can loop or cause extra change detection. Usually the fix is to replace the effect with a `computed` or `linkedSignal`, or to read with `untracked()` when the value shouldn't be a dependency. Logging inside the effect and the Angular DevTools signal graph show which signal triggers it.

## 334: How do you debug duplicate HTTP requests in Angular SSR?

With SSR, a request made during server rendering and again during client bootstrap runs twice. Angular's HTTP transfer cache (enabled with `provideClientHydration()`) stores `GET` and `HEAD` responses made on the server in the page's HTML and reuses them on the client.

If you still see duplicates in the Network panel:

- The request is a `POST`, or has headers that are excluded by default (like `Authorization`); configure `withHttpTransferCacheOptions` if it is safe to cache.
- The URL differs between server and client (absolute vs relative, different host or query order).
- The request is made with `fetch` directly instead of `HttpClient`.
- The code runs in a way that isn't part of the hydration window (for example after a delay).

## 335: How do you debug stale or wrong caching in Next.js at a deeper level?

- Turn on fetch logging to see cache hits and misses in the terminal:

```js
// next.config.js
module.exports = {
  logging: {
    fetches: { fullUrl: true },
  },
};
```

- Run `next build` and read the route table: static routes, dynamic routes and partially prerendered routes are marked differently. A route you expected to be dynamic is often static because nothing in it reads request data (`cookies()`, `headers()`, `searchParams`).
- Check `"use cache"` functions and their `cacheLife` and `cacheTag` settings when Cache Components are enabled.
- Check response headers like `x-nextjs-cache` and `Cache-Control` on your host or CDN.
- Remember the client router cache: after a mutation, call `router.refresh()` or revalidate in the Server Action so the client gets fresh data.

## 336: How can SSR leak data between users, and how do you find it?

On the server, module-level variables live as long as the server process, and they are shared by all requests. Code that works in the browser (one user per page) becomes a bug on the server:

```js
// Bug on the server: shared between all requests
let currentUser = null;

export function setUser(user) {
  currentUser = user;
}
```

A user can then see another user's data under load, which is a serious security bug. It is hard to see in development, because you are the only user. Look for module-level state, singletons and stores created at import time. Create stores per request (for example inside a provider component or using request-scoped context), and add a test that renders two requests with different users in parallel and checks for mixed data.

## 337: How do Reselect's development checks help with selector bugs?

Reselect 5 (used by Redux Toolkit's `createSelector`) runs extra checks in development:

- **inputStabilityCheck:** runs input selectors twice and warns if they return different references for the same state. That means an input selector creates a new object or array each time, so memoization never works.
- **identityFunctionCheck:** warns if the result function just returns its input, which makes the selector useless.

When a component re-renders on every store update, check the console for these warnings, and make sure input selectors only pick values out of state. React-Redux's `useSelector` also warns in development when a selector returns a different result for the same state.

## 338: What do Redux Toolkit's serializability and immutability checks catch?

In development, `configureStore` adds two middlewares:

- **Immutability check:** detects state mutated outside a reducer or outside Immer, for example `state.items.push(x)` in a component. These mutations make the UI not update and time travel lie.
- **Serializability check:** warns when actions or state contain non-serializable values like `Date`, `Map`, class instances, promises or functions. These break DevTools, persistence and SSR.

They slow things down on large states, so they are off in production. If they are slow in development, you can raise the warning threshold or ignore specific paths instead of turning them off.

## 339: How do you debug state that is out of sync between browser tabs?

Each tab has its own JavaScript memory, so in-memory stores don't sync. Common bugs: logging out in one tab while another still shows the account, or a cart that differs between tabs.

- The `storage` event fires in other tabs when `localStorage` changes; use it to sync or react.
- `BroadcastChannel` sends messages between tabs of the same origin.
- For auth, check the session on focus (`visibilitychange`) and handle 401 responses everywhere.

To debug, open two tabs side by side, log events from both, and check what each tab stores in the Application panel.

## 340: How do you debug optimistic update bugs?

With optimistic updates, the UI changes before the server confirms, and rolls back on error. Common bugs:

- The rollback restores a snapshot that is out of date because another update happened meanwhile.
- A refetch after the mutation returns old data (cached or replicated with delay), so the item "jumps back".
- Two quick mutations finish in a different order than they started.
- Temporary ids aren't replaced with the real ids from the server, so later updates target the wrong item.

Test with throttled networks and forced server errors (overrides or MSW). In TanStack Query, cancel outgoing queries in `onMutate` and invalidate in `onSettled`. Log each step (optimistic apply, server response, rollback) with a mutation id.

## 341: How do you debug slow TypeScript type checking?

- Run `tsc --extendedDiagnostics` to see time spent in each phase, the number of types and memory used.
- Run `tsc --generateTrace ./trace` and open the trace in a performance trace viewer, or analyze it with `@typescript/analyze-trace`, to find the files and types that take the longest.
- Look for very large union types, deep recursive conditional types, heavy generic libraries, and big generated files.
- Use project references and `incremental` builds, and `skipLibCheck: true` to skip checking declaration files.

In the editor, slow IntelliSense often has the same cause. The TypeScript 7 native compiler (`tsgo`) is much faster, but complex types are still worth simplifying.

## 342: Why can TypeScript types give you false confidence about runtime data?

Types are only checked at compile time. When data comes from outside (APIs, `localStorage`, `JSON.parse`, URL params, `postMessage`), TypeScript trusts whatever type you give it:

```ts
const user = (await res.json()) as User; // no check happens here
user.address.city; // crashes if the API didn't send address
```

`as` casts and `any` silence the compiler without checking anything. Validate untrusted data at the boundary with a schema library (Zod, Valibot, ArkType) and derive the type from the schema, so the type and the runtime check can't drift apart. When debugging "impossible" errors in typed code, look for casts and `any` first.

## 343: How do you debug a confusing generic type error?

- Break the expression into steps with named intermediate variables, and hover over each to see where the type changes.
- Add explicit type arguments to the generic function to see if inference is the problem.
- Use `satisfies` to check that a value matches a type without changing its inferred type:

```ts
const routes = {
  home: "/",
  user: "/users/:id",
} satisfies Record<string, `/${string}`>;
```

- Create small test types to see what a helper type produces:

```ts
type Check = ReturnType<typeof makeStore>["getState"];
```

- In the TypeScript playground, reproduce it with the smallest code possible and try different TS versions.

## 344: Why doesn't a module augmentation or global type declaration apply?

- A `.d.ts` file with `declare module "lib" { ... }` replaces the module's types instead of augmenting them if the file is not itself a module. For augmentation, the file needs at least one `import` or `export` (for example `export {};`) and must import the original module.
- For globals, use `declare global { ... }` inside a module file.
- The file must be included by `tsconfig.json` (`include`, `files`), or be referenced with `/// <reference ...>`.
- The module name must match exactly how the package is imported, including subpaths.
- Different copies of the same package can make the augmentation apply to one copy but not the other.

## 345: How do you debug a webpack build?

- Get a full stats file with `webpack --json > stats.json` and look at module reasons ("why is this module included") with an analyzer.
- Set `stats: { reasons: true, optimizationBailout: true }` to see why modules couldn't be concatenated or tree shaken.
- Use `infrastructureLogging: { level: "verbose" }` and `--progress` to see what webpack is doing, and `--profile` for timing per plugin.
- For loader problems, check `module.rules` order (loaders run from right to left / bottom to top) and test the regex against the file path.
- For caching issues, delete the persistent cache folder (`node_modules/.cache/webpack`).

## 346: How do you debug a Vite build or dev server problem?

- Run `vite --debug` or set `DEBUG="vite:*"` to see detailed logs for resolving, transforming and pre-bundling. You can narrow it, for example `DEBUG="vite:resolve"`.
- Add `vite-plugin-inspect` and open `/__inspect/` to see each module's code after every plugin transform, so you can find which plugin changed something.
- Remember that dev and build use different pipelines: dev transforms files on request and pre-bundles dependencies, while build bundles everything. A bug in only one mode points to that difference.
- Use `vite build --mode development` with `build.minify: false` and `sourcemap: true` to debug build output more easily.
- Check plugin order with `enforce: "pre"` or `"post"`.

## 347: What ESM and CommonJS interop bugs are common?

- A CommonJS module's `module.exports` becomes the default export when imported from ESM, so `import { foo } from "cjs-lib"` may fail or `import lib from "lib"` gives `{ default: ... }`. You see errors like "lib.default is not a function" or "does not provide an export named".
- `__dirname`, `require` and `module` don't exist in ESM.
- Bundlers and Node.js handle interop differently, so code can work in Vite but fail in Node tests (or the other way).
- `"type": "module"` in `package.json` changes how `.js` files are treated.

Check how the package is published (`exports`, `main`, `module` fields) and what the importing environment expects. Testing the import in a tiny script in the same environment quickly shows the actual shape.

## 348: What is the dual package hazard?

When a package ships both CommonJS and ESM builds, an app can end up loading both copies: one through `require` and one through `import`. Then there are two separate module instances with their own state.

Symptoms: a singleton or registry exists twice, `instanceof` checks fail, a React context provider from one copy isn't seen by a consumer from the other, or "configuration" set in one copy is missing in the other. Find it with a bundle analyzer (two copies of the same package) or by logging a module-level id. Fix it by making all code use the same format, or by having the package keep its state in one shared file.

## 349: How do package.json exports conditions cause wrong files to load?

The `exports` field lets packages choose files based on conditions like `import`, `require`, `browser`, `node`, `development`, `production`, `types` and `default`. The bundler picks the first matching condition in the order they are written.

Bugs happen when the bundler or test runner uses different conditions than you expect: a Node build loads in the browser (and needs `fs`), a development build ships to production, or tests load a different file than the app. Check which file was resolved (Vite's `vite:resolve` debug logs, webpack stats, or `require.resolve`/`import.meta.resolve` in Node), and set conditions explicitly with `resolve.conditions` in Vite or `resolve.conditionNames` in webpack.

## 350: Why might sideEffects: false break your app?

`"sideEffects": false` in `package.json` tells the bundler that importing a module without using its exports does nothing, so it can drop it. If that's not true, the bundler removes code you need:

```js
import "./styles.css"; // removed
import "./polyfills"; // removed
import "./register-components"; // removed
```

The symptom is missing styles, missing polyfills or unregistered custom elements, but only in production builds. List files that do have side effects:

```json
{
  "sideEffects": ["*.css", "./src/polyfills.js", "./src/register-components.js"]
}
```

## 351: How do you debug code that fails in older browsers?

- Check the error: a `SyntaxError` on load usually means syntax the browser doesn't support (like optional chaining in very old engines, or class fields). A `TypeError` like "x is not a function" may be a missing API (like `Array.prototype.at` or `structuredClone`).
- Check the build target: Vite's `build.target`, the `browserslist` config used by Babel or SWC and Autoprefixer, and TypeScript's `target`.
- Remember that transpiling syntax doesn't add missing APIs; you need polyfills for those.
- Check dependencies: many packages ship modern code and are not transpiled by default.
- Test in that browser with BrowserStack, Sauce Labs, or Playwright's older browser builds when possible.

## 352: How do you find duplicate packages in a bundle, and why do they matter?

Run a bundle analyzer and look for the same package name appearing more than once, often in different versions under nested `node_modules` paths. `npm ls <pkg>` and `pnpm why <pkg>` show who requires each version.

Duplicates make the bundle bigger, and for packages with state they cause real bugs: two React copies (invalid hook call), two copies of a styling library (theme not applied), two copies of a router or state library (context not found). Fix with `npm dedupe`, aligned version ranges, `overrides`/`resolutions`, peer dependencies in your own packages, or bundler options like `resolve.dedupe` in Vite.

## 353: What problems are common in monorepos with package managers like pnpm?

- **Phantom dependencies:** code imports a package that isn't in its own `package.json` but works because it was hoisted from another package. pnpm's strict layout makes this fail, which is good; add the dependency explicitly.
- **Symlinked local packages:** the bundler may follow the symlink and not transpile or dedupe the package. Configure the bundler to treat workspace packages as source, and make sure peer dependencies like React resolve to one copy.
- **Stale builds:** an app uses an old build of a local library. Use the task runner (Turborepo, Nx) to build dependencies first, or point to source files.
- **Different versions** of the same tool in different packages.

## 354: How do you debug a Safari-only rendering bug?

1. Reproduce in Safari on macOS or iOS, and also in Playwright's WebKit build, which is close but not identical to Safari.
2. Use Safari's Web Inspector: the Elements tab has a Layout panel for grid and flex overlays, and the Layers tab shows compositing.
3. Make a minimal HTML file and remove CSS until the bug disappears.
4. Check known differences: flex and grid with percentage heights, `position: sticky` inside overflow containers, `backdrop-filter`, form control styling, `100vh`, SVG sizing, and newer features not yet supported.
5. Check Safari Technology Preview: if the bug is fixed there, it is an engine bug and a fix is coming; you may only need a temporary workaround.
6. Search the WebKit bug tracker for the behavior.

## 355: What JavaScript differences between engines can cause bugs?

- Date parsing of non-ISO strings.
- `Intl` output: number, date and list formatting can differ slightly between browsers and versions (spaces, symbols), so don't compare formatted strings in tests or logic.
- Error messages and `error.stack` format differ, so code that parses them breaks.
- Newer features available in one engine but not another (for example some regex flags, `Array` or `Set` methods, `Temporal`).
- Performance characteristics: code that is fast in V8 can be slow in another engine.

Feature-detect APIs, avoid parsing error messages, and use test runners in several engines (Playwright with Chromium, Firefox and WebKit, or Vitest browser mode).

## 356: How do you reproduce performance problems that only happen on low-end devices?

- Use CPU throttling in the Performance panel. Recent Chrome versions offer calibrated presets ("low-tier mobile", "mid-tier mobile") that measure your machine and set a slowdown to match those devices.
- Combine with network throttling and a cold cache.
- Test on a real mid-range Android phone with remote debugging; nothing replaces real hardware for things like thermal throttling, GPU limits and memory pressure.
- Look at RUM data split by device memory (`navigator.deviceMemory`) and CPU cores (`navigator.hardwareConcurrency`) to know which devices matter.

## 357: How do you debug a page inside an in-app browser or WebView?

Links opened from apps like social networks or email often open in a WebView, not the user's normal browser. These can have older engines, missing APIs, blocked popups, different cookie storage and injected scripts.

- **Android WebView:** if the app enables WebView debugging, it shows in `chrome://inspect`.
- **iOS WKWebView:** since iOS 16.4, the app must set `isInspectable = true`; then it shows in Safari's Develop menu. For apps you don't control, you usually can't inspect it.
- Detect WebViews from the user agent in your RUM data to see if errors cluster there, and log feature support at runtime.

## 358: What iOS Safari viewport bugs are common, and how do you debug them?

- The on-screen keyboard doesn't resize the layout viewport, only the visual viewport, so `position: fixed` footers can end up under the keyboard or move strangely.
- Inputs with a font size below 16px make Safari zoom in on focus.
- The address bar resizing makes `100vh` too tall (use `dvh`/`svh`).
- Rubber-band overscroll shows space above or below fixed elements.

Use the `visualViewport` API (`resize` and `scroll` events, `height`, `offsetTop`) to place elements relative to the visible area, and log these values on a real device with remote debugging, because simulators and device mode don't match exactly.

## 359: Why do layout bugs appear at certain zoom levels or device pixel ratios?

At zoom levels like 110% or 125% and on screens with a device pixel ratio like 1.5, CSS pixels don't map to whole device pixels. Browsers round sizes and positions, which can cause:

- 1px gaps or overlaps between elements that should touch.
- Blurry borders, text or images, especially on layers with transforms.
- Items wrapping to the next line because rounded widths add up to more than 100%.
- Scrollbars appearing because content is 0.5px too wide.

Test with browser zoom and device mode DPR settings. Avoid layouts that depend on exact pixel sums; use flex or grid with `gap`, and give a little room for rounding.

## 360: How do you test that the layout survives large text sizes?

Users increase text size in browser settings or OS settings (especially on mobile), and WCAG asks that text can be resized to 200% without losing content. Bugs include text cut off by fixed heights, overlapping elements and buttons that don't fit.

- Change the browser's default font size in its settings (not only zoom), and check that you use `rem` or `em` for font sizes so it applies.
- On iOS and Android, increase the system font size and test real devices (Safari applies Dynamic Type only to certain fonts and settings).
- Avoid fixed heights on text containers; use `min-height` and let content grow.
- Check with text spacing changes too (line height, letter spacing), which some users apply with extensions.

## 361: How do you debug screen reader announcements for dynamic content?

Content that changes without a page load (toasts, form errors, search result counts) is not announced unless it is in a live region.

- Use `role="status"` (polite) or `role="alert"` (assertive), or `aria-live="polite"`.
- The live region must exist in the DOM before the content changes. Adding an element that already contains the text often isn't announced; add the empty container on load and change its text later.
- Changing the text to the same value isn't announced again; clear it first or add something different.
- Too many assertive announcements interrupt users; use polite for most cases.

Test with a real screen reader (VoiceOver, NVDA), since behavior differs between screen readers and browsers. The Accessibility pane shows the live region properties, but not what was actually spoken.

## 362: How do you debug focus and announcements on route changes in a single page app?

In a normal page load, screen readers announce the new page and focus starts at the top. In a single page app nothing like that happens by default: focus stays on the link that was clicked (which may no longer exist), and screen reader users don't know the page changed.

Check what happens with a live expression on `document.activeElement` while navigating. A common fix is to move focus to the new page's main heading (with `tabindex="-1"`) or to a skip target after each route change, and update `document.title`. Some frameworks do part of this (for example Next.js has a route announcer, and Angular's router can be configured to restore focus); check what yours does and test it with a screen reader.

## 363: How do you catch accessibility regressions automatically?

Run axe-core in your tests:

```ts
import { test, expect } from "@playwright/test";
import AxeBuilder from "@axe-core/playwright";

test("checkout page has no detectable a11y violations", async ({ page }) => {
  await page.goto("/checkout");
  const results = await new AxeBuilder({ page })
    .withTags(["wcag2a", "wcag2aa"])
    .analyze();
  expect(results.violations).toEqual([]);
});
```

There are also `jest-axe` or `vitest-axe` for component tests, Storybook's accessibility addon, and Lighthouse CI. Also test keyboard flows in end-to-end tests with `page.keyboard.press("Tab")` and role-based locators (`getByRole`), which fail if elements lose their role or name. Automated checks find only part of the problems, so keep manual checks for important flows.

## 364: Why do ARIA references break across shadow DOM boundaries?

Attributes like `aria-labelledby`, `aria-describedby`, `aria-controls` and `<label for>` reference elements by id, and ids only work inside the same tree. An input inside a web component's shadow root can't be labelled by an id in the light DOM, and the other way around. The result is an element with no accessible name, even though it looks labelled.

The Accessibility pane shows the missing name. Fixes include keeping the label and input in the same shadow root, passing the label text in as a property and setting `aria-label` inside, using `ElementInternals` for form-associated custom elements, or the newer reference target proposal when browsers support it.

## 365: How do you debug a CSP with nonces and strict-dynamic?

A strict CSP looks like:

```http
Content-Security-Policy: script-src 'nonce-r4nd0m' 'strict-dynamic'; object-src 'none'; base-uri 'none'
```

Only scripts with the matching `nonce` attribute run, and scripts they add with `document.createElement("script")` are trusted too (because of `strict-dynamic`). Common bugs:

- The nonce is not regenerated per response, or cached HTML has an old nonce that doesn't match the new header.
- Scripts added with `innerHTML` or parser-inserted scripts (like `document.write`) are blocked even with `strict-dynamic`.
- Inline event handlers (`onclick="..."`) are blocked; they need `'unsafe-hashes'` or, better, moving to `addEventListener`.
- A framework or tag manager adds scripts in a way that doesn't pass on the nonce.

The console error says which directive blocked which script; compare the nonce in the header with the one in the HTML in the Network panel.

## 366: What are Trusted Types and how do you debug violations?

Trusted Types is a browser feature that blocks passing plain strings to dangerous DOM sinks like `innerHTML`, `outerHTML`, `document.write`, `eval` and `script.src`. You turn it on with CSP:

```http
Content-Security-Policy: require-trusted-types-for 'script'; trusted-types app-policy
```

Then code must create values through a policy:

```js
const policy = trustedTypes.createPolicy("app-policy", {
  createHTML: (input) => DOMPurify.sanitize(input),
});
element.innerHTML = policy.createHTML(userHtml);
```

When a violation happens, the console shows the sink and a stack trace pointing to the line, which is a great way to find every place that writes HTML. Start with `Content-Security-Policy-Report-Only` to collect violations without breaking the app.

## 367: How do you debug features that depend on third-party cookies?

Safari and Firefox block third-party cookies by default, and Chrome lets users block them (and blocks them in Incognito). Embedded widgets, single sign-on in iframes, and cross-site analytics break in those cases.

- The Issues panel and the request's Cookies tab show cookies blocked because of third-party cookie settings.
- Test with third-party cookies blocked in Chrome's settings, and in Safari and Firefox.
- For embedded content that needs its own state, use partitioned cookies (CHIPS) with the `Partitioned` attribute; they are stored per top-level site.
- For iframes that need access to their unpartitioned cookies after user action, look at the Storage Access API (`document.requestStorageAccess()`).

## 368: How do you debug cross-origin isolation errors (COOP and COEP)?

Features like `SharedArrayBuffer` and precise timers need the page to be cross-origin isolated, which requires:

```http
Cross-Origin-Opener-Policy: same-origin
Cross-Origin-Embedder-Policy: require-corp
```

After you add COEP, any cross-origin resource (images, scripts, iframes) without `Cross-Origin-Resource-Policy` or CORS headers is blocked. The Network panel shows these as blocked with a reason like `NotSameOriginAfterDefaultedToSameOriginByCoep`, and the Issues panel lists them. COOP `same-origin` also breaks popups that need `window.opener` (like some OAuth or payment flows).

Check `self.crossOriginIsolated` in the console. Use `COEP: credentialless` to load cross-origin resources without credentials when you can't change their headers, and `Cross-Origin-Embedder-Policy-Report-Only` to test first.

## 369: Why does fetch with mode "no-cors" seem to work but return nothing?

`mode: "no-cors"` lets you send a cross-origin request without CORS, but the response is "opaque": status `0`, no headers, and an empty body you can't read. The request was sent and may even have succeeded on the server, but your code can't see the result.

People often add `no-cors` to "fix" a CORS error, and then wonder why the data is empty. The real fix is CORS headers on the server or a same-origin proxy. Opaque responses can still be cached by service workers, but they take a lot of storage quota (padded size) and you can't check if they were errors, so caching them can store broken responses.

## 370: How do you debug a race condition in token refresh?

A typical bug: the access token expires, several requests fail with 401 at the same time, and each one starts its own refresh. If refresh tokens are rotated, the second refresh uses an old token and fails, logging the user out.

To confirm, look at the Network panel: several refresh requests in parallel, then a 401 or 400 on the later ones. Fix it by sharing one refresh promise:

```js
let refreshPromise = null;

async function getFreshToken() {
  refreshPromise ??= refreshToken().finally(() => {
    refreshPromise = null;
  });
  return refreshPromise;
}

async function apiFetch(url, options) {
  let res = await fetch(url, withToken(options));
  if (res.status === 401) {
    await getFreshToken();
    res = await fetch(url, withToken(options));
  }
  return res;
}
```

Also think about several tabs refreshing at the same time; a `BroadcastChannel` or the Web Locks API (`navigator.locks.request`) can coordinate them.

## 371: How do you find where an XSS payload gets into the DOM?

- Reproduce with a harmless payload like `<img src=x onerror="debugger">`. When it runs, the debugger pauses, and the call stack shows the code that inserted the HTML.
- Turn on Trusted Types in report-only mode; violations point to every sink that receives a string.
- Search the code for sinks: `innerHTML`, `outerHTML`, `insertAdjacentHTML`, `document.write`, `dangerouslySetInnerHTML`, `[innerHTML]` bindings with `bypassSecurityTrust...` in Angular, `v-html`, `href` with `javascript:` URLs, and `eval`/`new Function`.
- Follow the data back to its source: URL parameters, `postMessage`, `localStorage` or API data.

Fix by using text APIs (`textContent`), framework escaping, and sanitizing with DOMPurify when HTML is needed.

## 372: How do you find out which script injected another script or element?

- In the Network panel, the Initiator column of the injected script shows the call stack of the code that added it, which often goes through a tag manager.
- Set a DOM breakpoint ("Break on subtree modifications") on `<head>` or `<body>`; the debugger stops on the line that inserts the element.
- Use a `MutationObserver` in a snippet and log `new Error().stack` when the element appears, or patch `appendChild` temporarily:

```js
const original = Element.prototype.appendChild;
Element.prototype.appendChild = function (node) {
  if (node.tagName === "SCRIPT") console.trace("script added", node.src);
  return original.call(this, node);
};
```

Run the snippet early with Local Overrides or a breakpoint on the first script line, so it catches injections that happen during load.

## 373: How do you find which code changes a property or global variable?

Replace the property with a getter and setter that logs a stack trace or pauses:

```js
let value = window.appConfig;
Object.defineProperty(window, "appConfig", {
  configurable: true,
  get() {
    return value;
  },
  set(next) {
    console.trace("appConfig changed", next);
    debugger;
    value = next;
  },
});
```

The same trick works on any object property, for example `document.title` on an instance or a property of a store object. For whole objects, wrap them in a `Proxy` with a `set` trap. Run it before the suspect code (from a snippet at a breakpoint on the first script, or with Local Overrides).

## 374: How can third-party scripts break your code by changing globals or built-in prototypes?

Old or badly written scripts sometimes override globals (`window.$`, `window.define`), polyfill built-ins in a non-standard way (`Array.prototype.includes`), change `JSON.stringify` or `Promise`, or wrap `fetch` and `XMLHttpRequest` for tracking. Your code then sees strange behavior that doesn't happen without that script.

To debug, block the script with request blocking and compare. Check if a built-in was replaced: native functions print as `function fetch() { [native code] }` when you log `fetch.toString()`. Prefer loading third-party code in sandboxed iframes or workers when possible, and pin versions of scripts you load from CDNs (with Subresource Integrity, the `integrity` attribute) so they can't change without you knowing.

## 375: How do you debug shared dependency problems in Module Federation?

With Module Federation, micro frontends can share libraries like React. Common problems:

- Two versions of React load because one remote's version doesn't satisfy the host's `requiredVersion`. You get "Invalid hook call" or context not found. The console usually warns "Unsatisfied version".
- `singleton: true` is missing, so each app loads its own copy.
- A remote's `remoteEntry.js` is cached and points to old chunks.
- `eager: true` pulls shared modules into the initial chunk and changes load order.

```js
shared: {
  react: { singleton: true, requiredVersion: "^19.0.0" },
  "react-dom": { singleton: true, requiredVersion: "^19.0.0" },
}
```

Check which versions actually loaded with `__webpack_share_scopes__` (webpack) or the Module Federation devtools extension, and the Network panel for duplicate library chunks.

## 376: How do you debug CSS leaking between micro frontends?

Global selectors (`button`, `.title`, `h2`), resets and utility frameworks from one app affect the others. Symptoms are styles that change depending on which app loaded first, or after navigating between apps.

In the Styles pane, look at the file each winning rule comes from. Fixes:

- Prefix or scope styles per app (CSS modules, a root class per app, `@scope`).
- Use cascade layers so each app's styles have a clear order.
- Use Shadow DOM for strong isolation, but remember inherited properties (like `font` and `color`) still pass through.
- Avoid global resets in micro frontends; let the shell own them.

## 377: How do you debug communication and routing conflicts between micro frontends?

- **Events:** log every message on the shared event bus (custom events on `window`, a pub/sub module) with the sender name. Bugs are often events sent before the receiver has loaded, or name clashes.
- **Routing:** several apps listening to `popstate` or controlling the URL can fight. Make the shell own the top-level routes, and let each app handle only paths under its prefix.
- **Shared state:** two apps writing the same `localStorage` key or global variable. Namespace keys per app.
- **Lifecycle:** an app not cleaning up listeners and timers when it unmounts keeps reacting after it's gone.

## 378: How do you send micro frontend errors to the right team?

One error tracking project for the whole page mixes all teams' errors. Options:

- Tag errors with the app that owns the code, based on the file URL in the stack trace or on metadata.
- In Sentry, the `moduleMetadataIntegration` (with metadata added by the bundler plugin) attaches an app name or project to each module's frames, and `makeMultiplexedTransport` can send each error to a different project based on that.
- Include each app's version in the error, since each one deploys on its own schedule.
- Give each app its own error boundary so one crashing app doesn't take down the whole page, and report which boundary caught it.

## 379: How do you debug a service worker fetch handler?

- In Sources, open the service worker file (or click its link in Application, then Service workers) and set breakpoints in the `fetch` handler.
- In the Network panel, responses from the worker show `(ServiceWorker)` in the Size column, and requests the worker made itself appear with a gear icon.
- A common bug is calling `event.respondWith()` asynchronously (after an `await`); it must be called synchronously in the handler.
- Another is caching error responses (404, 500, opaque) and serving them forever. Check `response.ok` before caching.
- Navigation requests that are slow because the worker has to start first can use navigation preload (`registration.navigationPreload.enable()`).
- Check `chrome://serviceworker-internals` for worker start failures and logs.

## 380: What bugs come from users running mixed versions of a service-worker-cached app?

After a deploy, a user may have an old page open, served from the cache, while the new service worker has new files. If the new worker took control with `skipWaiting()`:

- The old page asks for a lazy chunk that no longer exists in the new cache.
- The old page calls an API that changed in a way it doesn't understand.
- Old JavaScript and new HTML or CSS mix.

To debug, check which cache and version each request came from (Application, then Cache storage), and log the app version in each request. Fixes are to keep old chunks available for a while, version the caches, avoid `skipWaiting` without reloading the page, or prompt users to reload when a new version is ready.

## 381: How do you remove a broken service worker that is already in production?

You can't uninstall it from the server directly, but the browser checks for updates to the service worker script on navigation (at most every 24 hours it bypasses the HTTP cache for it). Options:

- Deploy a new service worker at the same URL that does nothing harmful: it skips waiting, deletes all caches, and unregisters itself.

```js
self.addEventListener("install", () => self.skipWaiting());
self.addEventListener("activate", (event) => {
  event.waitUntil(
    (async () => {
      const keys = await caches.keys();
      await Promise.all(keys.map((key) => caches.delete(key)));
      await self.registration.unregister();
      const clients = await self.clients.matchAll();
      clients.forEach((client) => client.navigate(client.url));
    })(),
  );
});
```

- Send a `Clear-Site-Data: "storage"` header (which also removes service worker registrations) or `"cache"` from a response.

Always serve the service worker script with `Cache-Control: no-cache` so updates are picked up quickly.

## 382: What bugs appear with SharedArrayBuffer and Atomics in workers, and how do you debug them?

With `SharedArrayBuffer`, the main thread and workers read and write the same memory, which brings classic multithreading bugs: data races (two threads change the same value without `Atomics`), torn reads, and deadlocks (a thread waits with `Atomics.wait` for a signal that never comes).

`Atomics.wait` is not allowed on the main thread, which is a common error. To debug, log with thread ids, keep each piece of shared data owned by one writer, use `Atomics.load`/`Atomics.store` for every access to shared flags, and use timeouts on waits so a deadlock shows up as an error instead of a freeze. Remember these require cross-origin isolation. Often, plain `postMessage` with transferable `ArrayBuffer`s is simpler and safer.

## 383: Why can a worker fail to load after bundling?

- A plain string URL (`new Worker("./worker.js")`) points to a file the bundler didn't include. Use the pattern bundlers understand: `new Worker(new URL("./worker.js", import.meta.url), { type: "module" })`.
- The worker is a module but `type: "module"` is missing, so `import` statements throw a `SyntaxError`.
- CSP `worker-src` (or `script-src`) blocks it, or the worker comes from another origin (workers must be same-origin; a blob URL wrapper is a workaround).
- Dependencies use `window` or `document`, which don't exist in workers; use `self` or `globalThis`.

The worker's errors appear in its own context; listen for `error` on the `Worker` object, and check the Network panel for the worker file request.

## 384: How do you debug WebAssembly code in the browser?

- Chrome DevTools can step through WebAssembly in the Sources panel, showing the text format (WAT), with the Scope section showing locals, globals and the stack, and a Memory Inspector for the linear memory.
- For C, C++ or Rust compiled with debug info (DWARF), install the "C/C++ DevTools Support (DWARF)" extension. Then you can set breakpoints in the original source files and see original variable names and types.
- Build with debug info (for example `-g` with Emscripten, or a Rust debug profile), and keep the debug build separate from the optimized production build, since debug info makes files much larger.
- For Rust, `console_error_panic_hook` turns panics into readable console errors.

## 385: How do you investigate WebAssembly errors and performance?

- A WebAssembly "trap" (like `RuntimeError: unreachable`, out of bounds memory access, integer divide by zero) shows a stack with `wasm-function[...]` frames. With a names section or DWARF info, these show real function names.
- Memory problems show as growing `WebAssembly.Memory` that never shrinks; linear memory can only grow, so check for leaks in the original language's allocator.
- For performance, record a Performance trace; WebAssembly functions appear in the flame chart like JavaScript. Look at the cost of calls between JavaScript and WebAssembly and of copying data back and forth, which often costs more than the computation.
- Make sure the module is compiled with streaming (`WebAssembly.instantiateStreaming`) and served with `Content-Type: application/wasm`; otherwise you get an error or slower compilation.

## 386: How do you find tests that depend on test order?

A test that passes alone but fails in the suite (or the reverse) depends on state left by another test: a global variable, a module-level cache, a mock that wasn't reset, the DOM, `localStorage`, or fake timers left on.

- Run tests in random order: Vitest `--sequence.shuffle`, Jest `--randomize` (with `--seed` to repeat an order).
- Run the failing test alone, then with the file, then bisect the set of tests before it.
- Reset state in `afterEach`: `vi.restoreAllMocks()`, `localStorage.clear()`, `vi.useRealTimers()`, and Testing Library's `cleanup` (automatic in most setups).
- Use `vi.resetModules()` or isolated workers for modules with internal state.

## 387: Why can tests in jsdom pass while the real browser is broken (or the other way)?

jsdom implements the DOM but not layout or rendering. `getBoundingClientRect()` returns zeros, `offsetWidth` is 0, CSS isn't applied (so `display: none` from a stylesheet doesn't hide anything), `IntersectionObserver`, `ResizeObserver` and `matchMedia` are missing unless mocked, and focus and scrolling behave differently.

So tests can pass while the real component is hidden behind an overlay, or fail because code depends on sizes. For components that depend on layout, CSS or real browser APIs, use Vitest browser mode (with Playwright as the provider) or Playwright component tests, which run in a real browser. Keep jsdom for logic-heavy components where speed matters.

## 388: How do you debug tests that leak async work into other tests?

Symptoms: errors that appear in a different test than the one that caused them, "Cannot log after tests are done", the runner not exiting, or "act" warnings in unrelated tests.

- Await everything: user events (`await user.click(...)`), `findBy` queries and any promise the test starts.
- Clean up timers, intervals, subscriptions, servers and mocks in `afterEach`.
- Jest: `--detectOpenHandles` shows handles (timers, sockets) that keep the process alive.
- Vitest: the `hanging-process` reporter lists what keeps the process open.
- With MSW, set `onUnhandledRequest: "error"` and reset handlers after each test so one test's mock doesn't answer another test's request.

## 389: How do you use a Playwright trace to find the cause of a CI-only failure?

Open the trace (`npx playwright show-trace trace.zip`, or the HTML report) and go through:

1. **Actions list:** find the failed step and the steps right before it.
2. **DOM snapshots:** compare "before" and "after" for each action. Is the element there, visible, covered by something, or showing a loading state?
3. **Network tab:** did the API call needed for this step finish, fail, or return different data than locally?
4. **Console tab:** look for app errors that happened before the failure.
5. **Timing:** compare action durations with a passing run; slow CI machines expose missing waits.

Then fix the test to wait for the right condition (web-first assertions, `expect.poll`, waiting for a response) or fix the app bug the trace revealed. Use `test.step()` to group actions so traces are easier to read.

## 390: How do you deal with flaky visual regression tests?

Screenshot diffs fail because of things that aren't real changes:

- **Fonts and rendering:** different OS, font versions or GPU give slightly different pixels. Run screenshot tests in one fixed Docker image, the same locally and in CI.
- **Animations and carets:** disable them; Playwright's `toHaveScreenshot` does this with `animations: "disabled"` and hides the caret by default.
- **Dynamic content:** dates, avatars, ads and random data. Mock them, freeze time (`page.clock`), or mask regions with the `mask` option.
- **Loading timing:** wait for fonts (`document.fonts.ready`) and images before taking the screenshot.
- Allow small differences with `maxDiffPixels` or `threshold`, but not so much that real bugs pass.

## 391: How can API mocks give you false confidence, and how do you catch it?

Mocks (MSW handlers, fixtures, `cy.intercept` responses) are written once and then the real API changes. Tests keep passing while production breaks, for example when a field is renamed or becomes nullable.

Ways to catch it:

- Generate mock types or data from the API schema (OpenAPI, GraphQL) so a schema change breaks the build.
- Validate mock responses with the same runtime schema (Zod and so on) the app uses.
- Use contract testing (like Pact) between the front end and the API.
- Keep a small set of end-to-end tests against a real back end in a staging environment.

## 392: Why do tests time out only in CI, and how do you fix it?

- CI machines are slower and run many tests in parallel, so things that take 900 ms locally take 3 seconds in CI. Look at durations in the CI report; raise timeouts only for tests that really need it.
- Too many workers for the CPU count: Vitest and Jest default to a number based on CPUs, and containers can report the host's CPU count. Set `--maxWorkers` or `poolOptions` explicitly.
- Missing services: a test waiting for a server or database that isn't running in CI.
- First run costs: browsers not installed, caches empty, transforms not cached.
- Real network calls that are blocked or slow in CI; mock them or fail on unexpected requests.

Record traces or timings for the slow tests to see where the time goes.

## 393: How do you design error boundaries so failures stay small and recoverable?

- Put boundaries around independent parts of the page (widgets, sidebar, each route), not only at the root, so one broken widget doesn't blank the whole page.
- Give each boundary a useful fallback: a short message and a "Try again" button that resets it.
- Reset boundaries when the input changes, for example with `resetKeys` in `react-error-boundary`, or when the route changes.
- Report the error with the boundary's name, so you know where it happened.
- Remember boundaries don't catch errors in event handlers, timers or async code outside rendering; report those with try/catch and global handlers. In React 19, `onCaughtError` on the root reports all caught errors in one place.

```jsx
<ErrorBoundary
  FallbackComponent={WidgetError}
  resetKeys={[productId]}
  onError={(error, info) =>
    report(error, { boundary: "recommendations", ...info })
  }
>
  <Recommendations productId={productId} />
</ErrorBoundary>
```

## 394: How do you connect a front-end error to the back-end logs of the same request?

Use distributed tracing. The front end sends a trace header with each API request, the back end continues the same trace, and both sides log the trace id.

- The W3C Trace Context standard uses the `traceparent` header (OpenTelemetry uses it). Sentry uses `sentry-trace` and `baggage` headers, and can also work with OpenTelemetry.
- Configure which URLs get the headers (for example `tracePropagationTargets` in Sentry). Cross-origin APIs must allow these headers in CORS (`Access-Control-Allow-Headers`).
- Without tracing, at least send a request id header and show it in error messages ("Error id: abc123") so support can find the server logs.

Then an error in the browser links straight to the slow database query or exception on the server.

## 395: How do you choose sampling rates for errors, traces and replays?

Collecting everything is expensive and can hit quotas, but too little sampling hides rare bugs.

- **Errors:** usually 100%, since each one matters; filter noise instead of sampling.
- **Performance traces:** a small percentage (for example 5-20%) is usually enough for averages and percentiles on busy sites; use higher rates on low-traffic pages or new releases.
- **Session replays:** record a small sample of normal sessions, but 100% of sessions with an error (Sentry's `replaysOnErrorSampleRate`), since those are the ones you need.
- Use dynamic sampling: higher rates for important flows (checkout), new releases, or specific users when investigating.

Make sure sampling decisions are consistent across front end and back end so traces aren't cut in half.

## 396: How do you debug a production bug that nobody can reproduce?

1. Collect all the context you have: error reports with breadcrumbs, session replays, logs around the time, the user's browser, device, account, feature flags and release.
2. Look for patterns across occurrences: same browser, same route, same time of day, same data, same third-party script, same region.
3. Read the code path in the stack trace and list everything that could make it fail (null data, timing, permissions).
4. Add more logging or tracing around that path and ship it; next time it happens you will have the missing information.
5. Try to reproduce with the same conditions: same data copied to a test account, throttled network, same flags, same browser version.

Make sure session replays mask sensitive input and personal data, and that you are allowed to look at user sessions under your privacy policy.

## 397: How do you use RUM data to find the cause of bad Web Vitals?

Overall numbers rarely tell you what to fix. Break the data down by:

- **Page or route type:** a product page and a search page have different problems.
- **Device type and connection:** mobile on slow networks often drives the 75th percentile.
- **Country or region:** CDN and server distance.
- **Navigation type:** first visit, reload, back/forward, prerendered.
- **Attribution data:** for LCP the element and its phases, for INP the target element, interaction type and long animation frame scripts, for CLS the shifted element.

```js
import { onINP } from "web-vitals/attribution";

onINP(({ value, attribution }) => {
  sendToAnalytics({
    value,
    target: attribution.interactionTarget,
    type: attribution.interactionType,
    inputDelay: attribution.inputDelay,
    processing: attribution.processingDuration,
    presentation: attribution.presentationDelay,
  });
});
```

Then reproduce the worst segment in the lab with matching throttling.

## 398: How do you send logs reliably when the user closes the page?

Requests started during `unload` or `beforeunload` are often cancelled. Use `navigator.sendBeacon` or `fetch` with `keepalive: true`, and send on `visibilitychange` (when the page becomes hidden) or `pagehide`, which fire more reliably, especially on mobile:

```js
document.addEventListener("visibilitychange", () => {
  if (document.visibilityState === "hidden" && queue.length) {
    navigator.sendBeacon("/logs", JSON.stringify(queue.splice(0)));
  }
});
```

Batch logs instead of sending one request per event. Avoid `unload` handlers; they also prevent the page from using the back/forward cache.

## 399: How can feature flags cause hydration mismatches, and how do you avoid it?

If the server renders with one flag value and the client evaluates the flag again and gets a different value (because the flag SDK isn't ready yet, or uses different user data, or the flag changed in between), the HTML differs and hydration fails or the UI flickers.

Evaluate flags once on the server, send the values to the client with the page (for example in serialized props or a script tag), and initialize the client SDK with them. In the browser, render with those values first and only apply live updates after hydration. When debugging a mismatch, log the flag values used on each side.

## 400: How do you find out if a new release caused a problem?

- Tag every error and metric with the release version, so dashboards can compare error rates and Web Vitals between the old and new version.
- Use gradual rollouts (canary, percentage rollouts) so a bad release only affects a few users first, and you can compare both versions side by side.
- Watch "new issues in this release" in your error tracker after each deploy.
- Look at what changed: the code diff, dependency updates in the lockfile, config and environment changes, feature flag changes and third-party script changes, which also "deploy" without your release.
- Roll back or turn off the flag first if users are hurt, then debug.

## 401: How do you debug a full stack app (like Next.js) in VS Code with one launch?

Use separate configurations for the server and the browser and combine them, or use a single configuration that starts the server and attaches to the browser. The Next.js docs suggest something like:

```json
{
  "version": "0.2.0",
  "configurations": [
    {
      "name": "Next.js: debug full stack",
      "type": "node",
      "request": "launch",
      "program": "${workspaceFolder}/node_modules/next/dist/bin/next",
      "args": ["dev"],
      "serverReadyAction": {
        "action": "debugWithChrome",
        "pattern": "- Local:.+(https?://.+)",
        "uriFormat": "%s",
        "killOnServerStop": true
      },
      "skipFiles": ["<node_internals>/**"]
    }
  ]
}
```

Use `skipFiles` to step over Node internals and library code. If breakpoints don't bind, check source map paths; `sourceMapPathOverrides` can map paths like `webpack://_N_E/./*` to `${workspaceFolder}/*`. Compound configurations (`"compounds"`) can start several debug sessions together, for example an API server and the front end.

## 402: What breakpoint features does VS Code's JavaScript debugger have?

- **Conditional breakpoints:** pause only when an expression is true.
- **Hit count breakpoints:** pause after the line has run a number of times, for example `> 10`.
- **Logpoints:** log a message with expressions in `{}` without pausing, like `total is {total}`.
- **Exception breakpoints:** pause on caught or uncaught exceptions.
- **Triggered breakpoints:** only activate after another breakpoint has been hit.
- **Function breakpoints** by name.
- **Restart frame**, step into specific targets, and "Toggle skipping this file" from the call stack.

Logpoints and conditional breakpoints work the same way in Chrome DevTools, so the skills carry over.

## 403: How do you use the Chrome DevTools Protocol directly from Puppeteer?

When Puppeteer doesn't have an API for something, open a CDP session and send protocol commands:

```js
const client = await page.createCDPSession();

await client.send("Emulation.setCPUThrottlingRate", { rate: 4 });
await client.send("Network.enable");
client.on("Network.loadingFailed", (e) => console.log("failed", e.errorText));

await client.send("Performance.enable");
const { metrics } = await client.send("Performance.getMetrics");
console.log(metrics.find((m) => m.name === "JSHeapUsedSize"));
```

The protocol is documented at chromedevtools.github.io/devtools-protocol. Many CDP features also have Puppeteer helpers (`page.emulateCPUThrottling`, `page.coverage`, `page.tracing`), so check those first. CDP domains marked experimental can change between Chrome versions.

## 404: How would you write an automated check for memory leaks?

Repeat an action many times in a real browser and check that memory doesn't keep growing:

```js
import puppeteer from "puppeteer";

const browser = await puppeteer.launch();
const page = await browser.newPage();
await page.goto("http://localhost:5173");

async function heapAfterGC() {
  const client = await page.createCDPSession();
  await client.send("HeapProfiler.collectGarbage");
  const { JSHeapUsedSize } = await page.metrics();
  return JSHeapUsedSize;
}

const before = await heapAfterGC();
for (let i = 0; i < 20; i++) {
  await page.click("#open-modal");
  await page.click("#close-modal");
}
const after = await heapAfterGC();

console.log(`growth: ${((after - before) / 1024).toFixed(0)} KB`);
await browser.close();
```

You can also count objects of a specific class with `page.queryObjects(prototypeHandle)`. Tools like Meta's MemLab automate this pattern, take heap snapshots, and report leaked objects with retainer paths. Use a threshold, since memory always changes a little.

## 405: How do you capture a performance trace automatically?

With Puppeteer:

```js
await page.tracing.start({ path: "trace.json", screenshots: true });
await page.goto("http://localhost:3000/products");
await page.click("#filter-shoes");
await page.tracing.stop();
```

Open `trace.json` by dragging it into the Performance panel. You can also run Lighthouse user flows (navigation, timespan and snapshot modes) from a script to get scores and insights for a multi-step flow. In CI, compare key numbers between builds (like total blocking time or a custom `performance.measure`) and fail the build on big regressions, but expect some noise; run several times and use the median.

## 406: What is the Chrome DevTools MCP server and what are its risks?

The Chrome DevTools MCP server (`chrome-devtools-mcp`) lets AI coding agents control a real Chrome through the Model Context Protocol. The agent can open pages, click and fill forms, take screenshots, read console messages and network requests, run scripts, and record and analyze performance traces.

```json
{
  "mcpServers": {
    "chrome-devtools": {
      "command": "npx",
      "args": ["chrome-devtools-mcp@latest"]
    }
  }
}
```

It helps an agent check its own front-end changes instead of guessing. Risks: the agent can see everything in that browser profile, including cookies and logged-in sessions, and page content can contain instructions meant to mislead the agent (prompt injection). Use a separate browser profile or an isolated one, avoid pointing it at sensitive accounts, and review what it does.

## 407: What are the limits of AI-assisted debugging, and how do you use it well?

AI tools are good at explaining error messages, suggesting likely causes, reading long stack traces and writing quick test code. But they can be confidently wrong, invent APIs or settings, and suggest fixes that hide the symptom (like adding `?.` everywhere or catching and ignoring errors).

Use them well by giving real evidence (the exact error, code, network response, trace), asking for an explanation of the cause and not just a fix, and checking every claim with the actual tools (breakpoints, the Network panel, docs). Keep a reproduction and a test so you can prove the fix works. Don't paste secrets, tokens or customer data into tools your company hasn't approved.

## 408: What does Firefox DevTools offer that is useful for debugging?

- **Inactive CSS:** the Rules view greys out properties that have no effect and explains why (for example `align-items` on a non-flex element).
- **Flexbox and Grid inspectors** with detailed overlays, and a font editor.
- **Accessibility inspector** with checks for contrast, keyboard access and text labels, and a simulation of color vision deficiencies.
- **Firefox Profiler** (profiler.firefox.com), a detailed profiler you can share as a link.
- **Network panel features** like resending edited requests and blocking.
- Debugging Gecko-specific bugs, since Firefox uses a different engine.

Checking a bug in a second browser's tools often gives a clearer error message or a different view of the problem.

## 409: What bugs are caused by timer throttling in background tabs?

Browsers slow down timers in hidden tabs to save battery: in Chrome, timers in background tabs run at most once per second, and chained timers in tabs hidden for more than about 5 minutes may run only once per minute ("intensive throttling"). `requestAnimationFrame` stops completely in hidden tabs.

Bugs: countdowns that fall behind, polling that stops, session timeouts that fire late, animations that jump when the tab comes back, and WebSocket heartbeats that miss their deadline. Fix them by calculating from timestamps (`Date.now()` or `performance.now()`) instead of counting ticks, refreshing state on `visibilitychange`, and using server push or Web Push for important updates. To reproduce, switch to another tab for a few minutes while logging timestamps.

## 410: How do page lifecycle events affect debugging on mobile?

Mobile browsers freeze or discard background tabs to save memory. A frozen page stops running JavaScript; a discarded page is reloaded when the user comes back, losing in-memory state.

- Listen to `visibilitychange` and `pagehide` to save state and send logs; `unload` and `beforeunload` often don't fire on mobile.
- Chrome fires `freeze` and `resume` events, and `document.wasDiscarded` is `true` after a discarded tab is reloaded.
- Bugs look like "form data lost when switching apps" or "app shows stale data after coming back".

You can trigger discards in Chrome with `chrome://discards`, which lists tabs and lets you freeze or discard them to test.

## 411: What bugs can prerendering with the Speculation Rules API cause?

With speculation rules, the browser can prerender a page the user is likely to visit, running its JavaScript in the background before the user navigates. Bugs:

- Analytics count a page view that never happened, or count it twice.
- Code that starts timers, plays media or shows popups on load runs while the page is invisible.
- Pages that change server state on GET (like marking a notification as read) do it too early.

Check `document.prerendering` and wait for the `prerenderingchange` event before doing such work:

```js
if (document.prerendering) {
  document.addEventListener("prerenderingchange", trackPageView, {
    once: true,
  });
} else {
  trackPageView();
}
```

In Chrome DevTools, Application, then "Speculative loads" shows the rules, which URLs were prefetched or prerendered, and why some failed. You can also select the prerendered page in DevTools to debug it.

## 412: How do you debug view transitions?

During a view transition, the browser takes snapshots of the old and new states and animates them with pseudo-elements like `::view-transition-old(name)` and `::view-transition-new(name)`.

- Use the Animations panel to pause and slow down the transition; while paused, the pseudo-elements appear in the Elements panel and you can inspect their styles.
- If an element doesn't animate on its own, check that `view-transition-name` is set and unique on the page at the time of the snapshot. Duplicate names make the transition skip with an error in the console.
- If the transition doesn't start, check browser support and whether the update callback threw an error.
- Elements that look stretched usually need `object-fit` or size settings on the snapshot pseudo-elements.

## 413: Why doesn't my CSS apply inside a web component?

Shadow DOM isolates styles: page CSS selectors don't match elements inside a shadow root, and the component's styles don't leak out. Only these get through:

- Inherited properties like `color`, `font` and `line-height`.
- CSS custom properties (`--brand-color`), which are the main way to theme components.
- `::part()` for elements the component exposes with a `part` attribute.
- `::slotted()` inside the component for slotted light DOM children (top level only).

In the Elements panel, expand the `#shadow-root` to see the internal elements and which styles apply. If a page style "doesn't work", check whether the target is in the shadow tree; if a slotted element looks wrong, remember slotted content is styled by the page's CSS, not the component's (except `::slotted` rules).

## 414: What bugs come from custom element upgrade timing?

A custom element in HTML exists as a plain `HTMLElement` until `customElements.define()` runs; then it "upgrades". If code sets a property on the element before it upgrades, the value is stored as an own property and hides the class's getter and setter, so the component never sees it.

```js
class UserCard extends HTMLElement {
  connectedCallback() {
    // pick up values set before upgrade
    if (Object.hasOwn(this, "user")) {
      const value = this.user;
      delete this.user;
      this.user = value;
    }
  }
  set user(value) {
    this._user = value;
    this.render();
  }
  get user() {
    return this._user;
  }
}
customElements.define("user-card", UserCard);
```

Use `await customElements.whenDefined("user-card")` before talking to the element, and check `customElements.get("user-card")` in the console to see if it's defined. Unstyled content before definition can be hidden with `user-card:not(:defined) { visibility: hidden; }`.

## 415: Why is event.target wrong for events from inside a shadow root?

Events that cross a shadow boundary are retargeted: listeners outside the component see `event.target` as the host element, not the inner element that was clicked. This hides the component's internals but breaks delegation code that expects the inner element.

Use `event.composedPath()` to see the full path, including elements inside open shadow roots:

```js
document.addEventListener("click", (e) => {
  console.log(e.target); // <my-menu>
  console.log(e.composedPath()[0]); // the inner <button>
});
```

Also, custom events from inside a component only leave the shadow root if they are created with `composed: true` (and `bubbles: true` to bubble). Forgetting `composed` is a common reason a parent never receives a component's event.

## 416: What number and money bugs are common in front-end code?

- Floating point: `0.1 + 0.2` is `0.30000000000000004`, so totals and comparisons are slightly off. Store money as integer cents (or use a decimal library), and round only for display.
- Large ids: numbers above `Number.MAX_SAFE_INTEGER` (2^53 - 1) lose precision when parsed from JSON, so two ids can become the same. Send large ids as strings, or use `BigInt` with custom parsing.
- `parseInt("08")` works today, but `parseInt` on values like `"1e3"` or `0.0000005` gives surprising results; use `Number()` for full strings.
- Formatting: use `Intl.NumberFormat` with the right currency and locale instead of building strings by hand.
- `NaN` spreading silently through calculations; check with `Number.isNaN`.

## 417: What bugs are common with virtualized lists?

Virtualized lists only render the visible rows, which is great for performance but causes:

- Wrong scroll height or jumping scrollbar when row heights vary and the list uses estimates. Measure rows (most libraries support dynamic measurement) and give good estimates.
- Lost state in rows (input values, expanded state) when they scroll out and unmount. Keep that state outside the row.
- Browser find-in-page and screen readers can't see rows that aren't rendered.
- Scroll position resetting when data updates, because keys change or the list remounts.
- Tests failing because jsdom has no layout, so the list renders zero rows. Mock the size or test in a real browser.

## 418: How do you debug Apollo Client cache problems?

Apollo normalizes data by `__typename` and `id`. Common bugs:

- A list doesn't update after a mutation because the mutation result doesn't include the new item in the list query; update the cache with `cache.modify`, `refetchQueries`, or return the needed fields.
- Two objects with the same id but different fields overwrite each other, or objects without an `id` can't be normalized; set `keyFields` in `typePolicies`.
- Pagination merges data incorrectly without a `merge` function.
- `fetchPolicy` like `cache-first` returns old data.

Apollo Client Devtools shows the normalized cache, active queries and mutations, so you can see what is actually stored and which queries watch it.

## 419: How do you debug TanStack Query issues?

Use the TanStack Query Devtools component; it lists every query with its key, status, data, last update and observers, and lets you refetch, invalidate or reset queries.

Common bugs:

- **Query keys:** a key that doesn't include all variables (like a filter) returns cached data for another filter. Everything the query function uses should be in the key.
- **staleTime:** the default `0` refetches on every mount and window focus, which can look like "too many requests". Set `staleTime` to fit your data.
- **Invalidation:** `invalidateQueries` with a key prefix that doesn't match the real keys does nothing.
- **Objects in keys:** keys are compared by value (hashed), so this works, but class instances or functions in keys don't.
- **Errors:** retries (3 by default) delay error states; turn retries off in tests.

## 420: What does "ResizeObserver loop completed with undelivered notifications" mean?

It means a `ResizeObserver` callback changed the size of an observed element in the same frame, so the browser had to stop delivering notifications to avoid an infinite loop. The rest are delivered in the next frame. It is reported as an error on `window`, so it shows up in error trackers, but usually the page works fine.

It is often harmless and many teams filter it. If you see visible flicker or layout jumping, look at callbacks that change the size of what they observe; delay the change with `requestAnimationFrame` or change something that doesn't affect the observed element's size.

## 421: How do you debug internationalization bugs?

- **Missing translations:** use a pseudo-locale (like accented, longer strings: "[Ŝéttîñgš ____]") to spot hard-coded text and layouts that break with longer words.
- **RTL layouts:** switch `dir="rtl"` on `<html>` in the Elements panel. Use logical properties (`margin-inline-start` instead of `margin-left`) so the layout flips correctly; icons with direction (arrows) may need mirroring.
- **Plurals and formatting:** use `Intl.PluralRules`, `Intl.NumberFormat` and `Intl.DateTimeFormat`; building strings by hand fails in languages with several plural forms.
- **Locale mismatch between server and client** causes hydration errors; pass the locale explicitly.
- Test with a different browser language in the DevTools Sensors panel ("Location" and "Locale" overrides) or the browser settings.

## 422: Why do APIs like clipboard, geolocation or camera fail in some environments?

- They need a secure context: HTTPS or `localhost`. On plain HTTP (for example testing on a phone using your computer's LAN IP), `navigator.clipboard` or `navigator.mediaDevices` may be `undefined`. Check `window.isSecureContext`.
- They need permission, and the user may have denied it. Check with `navigator.permissions.query({ name: "geolocation" })`.
- In iframes, the parent must allow them with the `allow` attribute (`allow="clipboard-write; camera"`) or Permissions Policy headers.
- Some need a user gesture (clipboard write, fullscreen, payment).

DevTools lets you reset permissions from the site info icon in the address bar, and the Sensors panel can fake a geolocation.

## 423: How do you debug "user activation" problems like blocked popups or autoplay?

Some actions only work right after a user gesture (a click or key press): `window.open`, fullscreen, playing audio with sound, clipboard writes, and some permission prompts. If there is an `await` (like a network request) between the click and the action, the activation may have expired, and the browser blocks the action.

Check `navigator.userActivation.isActive` right before the call to see if the gesture is still valid. Fixes: open the popup first and set its URL after the request finishes, start media muted, or ask the user to click again once the data is ready. For autoplay, Chrome's Media panel and the `play()` promise rejection (`NotAllowedError`) tell you why playback was blocked.

## 424: How do you debug canvas and WebGL problems?

- For 2D canvas, a blurry drawing usually means the canvas size doesn't account for `devicePixelRatio`; set `canvas.width` to the CSS width times the ratio and scale the context.
- For WebGL, check `gl.getError()` after calls while debugging, and listen for `webglcontextlost` events; contexts can be lost on GPU resets or when too many are open.
- Spector.js (a browser extension) captures a WebGL frame and shows every draw call, its state, shaders and textures.
- Shader compile errors are only visible if you read `gl.getShaderInfoLog()`.
- Performance: record a trace and look at GPU activity, and keep draw calls and texture uploads low.
- For WebGPU, error scopes (`device.pushErrorScope`) and labels on resources make errors readable.

## 425: How do you debug WebRTC calls?

Open `chrome://webrtc-internals` in another tab during the call. It shows every peer connection, the ICE candidates gathered, the selected candidate pair, and live stats graphs (bitrate, packet loss, jitter, frame rate, resolution). You can download a dump to share.

Common problems: no connection because no ICE candidate pair works (missing or misconfigured TURN server behind strict firewalls), one-way audio or video (a track not added or a wrong `direction`), and quality drops (packet loss, CPU limits). Firefox has `about:webrtc` with similar information.

## 426: How do you debug audio and video playback issues?

Chrome's Media panel (Command Menu, "Show Media") lists every media player on the page with its properties, events and messages: the chosen decoder, buffering, resolution, errors like decode failures, and why autoplay was blocked.

Also check:

- The media file's format and codec support in that browser (`HTMLMediaElement.canPlayType`, `MediaSource.isTypeSupported`).
- The server supports range requests (`206 Partial Content`), which Safari needs for video.
- The `error` property of the media element (`video.error.code` and `message`).
- The `play()` promise rejecting with `NotAllowedError` for autoplay with sound.

## 427: How can promises freeze a page even without a long synchronous loop?

Microtasks (promise callbacks, `queueMicrotask`, `await` continuations) all run before the browser can render or handle the next event. If microtasks keep scheduling more microtasks, the queue never empties, and the page freezes like an infinite loop:

```js
function loop() {
  Promise.resolve().then(loop); // never yields to rendering or input
}
loop();
```

A more realistic version is a recursive async function that awaits values that are already resolved. In a Performance trace, this shows as one very long task with many tiny "Run microtasks" entries. To give the browser a chance to render, yield to a task: `await scheduler.yield()` (with a `setTimeout` fallback), or process work in chunks.

## 428: How do you debug "Maximum call stack size exceeded"?

This `RangeError` means a function called itself (directly or through others) too many times. Pause on the exception and look at the Call Stack: you'll see the same frames repeated.

Common causes:

- Recursion without a correct base case, often with unexpected data (a cycle in a tree, or a deeper structure than expected).
- A setter that sets itself (`set name(v) { this.name = v; }`).
- `JSON.stringify` or a deep clone on an object with a getter that creates new objects, or a custom `toJSON` that calls itself.
- Two event handlers or state updates triggering each other synchronously.
- A React component rendering itself by mistake.

For very deep data, switch from recursion to a loop with your own stack.

## 429: How do circular imports cause bugs, and how do you find them?

When module A imports B and B imports A, one of them runs first and sees the other's exports before they are initialized. You get `undefined` values or `ReferenceError: Cannot access 'X' before initialization`, often only in some build modes or after unrelated changes to import order.

Find cycles with `madge --circular src/` or the `import/no-cycle` ESLint rule. Webpack has `circular-dependency-plugin`, and Rollup prints circular dependency warnings in the build output. Fix them by moving shared code to a third module, avoiding top-level code that uses imports immediately, or importing directly from files instead of through barrel `index.ts` files, which create many hidden cycles.

## 430: What do "preloaded but not used" warnings mean, and how do you debug resource priority?

Chrome warns in the console when a resource was preloaded with `<link rel="preload">` but not used within a few seconds after load. Causes are preloading the wrong URL (a different query string or a different image size from `srcset`), missing `crossorigin` on font preloads (so the font is downloaded twice), or preloading things that aren't needed early. Wasted preloads compete with important resources.

To debug priority, right-click the Network panel header and turn on the "Priority" column. Check that the LCP image is `High` (use `fetchpriority="high"`), that below-the-fold images are lazy, and that non-critical scripts use `async` or `defer`. The Performance panel's network track shows the same priorities over time.

## 431: How do you debug a problem that only happens for users in some regions?

The most common cause is the CDN. Different edge locations can have different cached versions, or cache a response that should vary by something.

- Compare response headers from different regions (`Age`, `X-Cache`, `CF-Cache-Status`, `Via`, CDN-specific ids) using a VPN or online tools that fetch from many locations.
- Check the `Vary` header: if responses depend on `Accept-Language`, cookies or `Accept-Encoding` but the CDN doesn't vary on them, users get someone else's version.
- Check that personalized responses are not cached publicly (`Cache-Control: private`).
- Check geo-based features: redirects, consent banners, payment methods, blocked third-party domains in some countries.

## 432: How do you test code that depends on the current time?

Freeze or control time instead of waiting for it. In Playwright, the clock API controls `Date`, timers and `performance.now()` in the page:

```ts
test("shows session expired after 30 minutes", async ({ page }) => {
  await page.clock.install({ time: new Date("2026-03-10T09:00:00Z") });
  await page.goto("/dashboard");

  await page.clock.fastForward("30:00");
  await expect(page.getByText("Your session has expired")).toBeVisible();
});
```

In unit tests use `vi.useFakeTimers()` and `vi.setSystemTime()`. Also test daylight saving changes and different time zones (Playwright's `timezoneId` option, or the `TZ` environment variable in Node).

## 433: How do you debug a login loop in an OAuth or OpenID Connect flow?

The user logs in, gets sent back to the app, and is sent to login again. With "Preserve log" on, follow the redirects in the Network panel and check:

- Is the session cookie set on the callback response, and is it sent on the next request? It may be blocked by `SameSite`, `Secure` on HTTP, a wrong `Domain`, or third-party cookie blocking if the login runs in an iframe.
- Does the `state` or PKCE `code_verifier` stored before the redirect still exist after it? It may be in `sessionStorage` of another tab, or cleared.
- Does the token exchange fail (look at the callback's server logs or the token request)? A wrong redirect URI or clock difference can cause it.
- Does the app's auth check run before the token is saved, and redirect again?

## 434: Scenario: some users are randomly logged out. How do you investigate?

1. Collect data: which users, browsers, how often, after how long, and what they were doing. Check if it correlates with a release, a time window or a browser.
2. Check token and session lifetimes against the reports (for example logged out exactly after one hour means refresh doesn't work).
3. Look for refresh races: several tabs or parallel requests refreshing at once with rotating refresh tokens.
4. Check cookies: expiry, `SameSite`, domain changes, cookie size limits (too many or too big cookies get dropped), and browsers that limit cookie lifetime set by JavaScript (Safari caps some script-set cookies at 7 days).
5. Check server-side: session store evictions, load balancer sticky sessions, clock differences between servers.
6. Add logging for every forced logout with the reason, and ship it to get the missing information.

## 435: Scenario: the checkout button does nothing for about 2% of users. How do you debug it?

1. Check error tracking filtered to the checkout page: an error on click or on page load for those users.
2. Look at patterns: browser and version, device, country, ad blockers, extensions, feature flags or an A/B test variant. 2% often matches a specific browser or an experiment.
3. Watch session replays of affected users: is the button covered by something (a cookie banner, a chat widget)? Is it disabled because a form field failed validation silently?
4. Check if a third-party script (payment provider, fraud check, analytics) fails to load for them and your code waits for it; test with request blocking.
5. Check network logs: is the request sent and failing, or never sent?
6. Reproduce with the same conditions, fix, and add monitoring for "click without result" (for example log when the click handler starts and when the request is sent).

## 436: Scenario: a dashboard's memory grows for hours until the tab crashes. How do you find the cause?

1. Find out what runs repeatedly while the dashboard is open: polling, WebSocket updates, charts redrawing, timers.
2. Reproduce faster: speed up the polling interval or send many fake updates in a loop.
3. Record with the Performance panel's memory option, or take heap snapshots a few minutes apart and compare them.
4. Look at what grows: arrays of data points that are never trimmed, chart instances created on each update without destroying the old ones, listeners added on each message, detached DOM nodes from re-rendered widgets, or logs kept in memory by a logging library or console (logged objects are kept alive while DevTools is open).
5. Fix it (limit buffers, reuse or destroy chart instances, clean up listeners) and run the fast reproduction again to confirm memory stays flat.

## 437: Scenario: a page is fine on your laptop but slow on mid-range Android phones. What do you do?

1. Check field data split by device to confirm and see which metric is bad (LCP, INP).
2. Reproduce on a real mid-range phone with remote debugging, and record a Performance trace there. Use calibrated CPU throttling in desktop Chrome for faster iteration.
3. Look for main thread work: big JavaScript bundles (parse and compile time grows a lot on slow CPUs), hydration of a large page, heavy third-party scripts, and long tasks during interaction.
4. Check images and fonts: huge images decoded on a small screen, too many web fonts.
5. Fix the biggest items: code splitting, less JavaScript, lazy hydration, smaller images, deferring third parties, and breaking up long tasks.
6. Measure again on the same device and in the field after release.

## 438: Scenario: after a deploy, the layout is broken for some users until they refresh. Why?

Most likely those users have a mix of old and new files:

- The cached HTML references old CSS or JS, or new HTML loads with an old cached CSS file that has the same URL (no content hash).
- A CDN edge still serves old files.
- A service worker serves the old precached files.
- An open tab from before the deploy lazy-loads a chunk that now has different styles or no longer exists.

Check that all assets have content hashes in their file names, HTML is not cached for long, the CDN is purged for HTML on deploy, and the service worker update flow reloads the page. Keep old assets available for some time after a deploy.

## 439: Scenario: a hydration error happens only in production. How do you debug it?

Production React errors are minified and don't show the diff, so:

1. Use the error code link (like "Minified React error #418") to see the full message.
2. Reproduce with a production build locally (`next build` and `next start`). If you can, use a profiling or development build of React with production settings to get readable messages.
3. Compare the server HTML (View Source or `curl`) with the DOM after the client renders, for the area around the error.
4. Look for differences that only exist in production: CDN or proxy HTML changes (HTML minification, injected scripts, email obfuscation, automatic image changes), different time zones or locales on the server, A/B testing scripts that change the DOM before hydration, and real user data that includes edge cases.
5. Check `onRecoverableError` reports for the component stack.

## 440: Scenario: the API returns correct data, but the UI shows wrong values. Where do you look?

1. Confirm the response in the Network panel for the exact request (check it's the request you think; there may be several).
2. Follow the data through the app: set a breakpoint where the response is handled and step through transformations (mapping, normalization, sorting, formatting).
3. Check caching layers in between: a data library cache with a wrong key, a store not updated, or a stale response winning a race.
4. Check rendering: wrong React keys reusing the wrong row, a memoized component or selector not updating, or a stale closure.
5. Check formatting: time zones, number formatting and rounding, and locale differences.
6. Use React or Angular DevTools to see the props of the component that shows the wrong value, then move up the tree until you find where the data becomes wrong.

## 441: Scenario: a bug only happens for one specific customer account. How do you debug it?

The cause is almost always in the data or the settings of that account.

1. Get permission and look at what is special: amount of data (thousands of items instead of ten), unusual characters in names, missing optional fields, old records from an earlier schema, specific permissions or roles, enabled features or flags, locale and time zone.
2. Copy the relevant data (anonymized if needed) to a test account or local environment and try to reproduce.
3. If your system supports it, use a secure "view as user" tool with auditing, rather than asking for the customer's password.
4. Compare the API responses for this account with a working one; the difference often points straight at the problem.
5. Add a test with that data shape once you find it.

## 442: Scenario: errors spike right after a third-party script updates. How do you handle it?

1. Confirm the timing: compare the error spike with the third party's release or status page, and check that your own release didn't change at the same time.
2. Look at the stack traces: are the errors in the third-party script, or in your code calling its API (maybe its API changed)?
3. Block the script in DevTools and see if the problem goes away.
4. Short term: disable the integration with a feature flag, or pin to a known good version if the vendor allows versioned URLs.
5. Long term: load third parties with error isolation (try/catch around calls, checks that its API exists, timeouts for scripts that never load), use versioned URLs with Subresource Integrity where possible, and add monitoring that groups errors by script origin.

## 443: Why might an animation run too fast on some screens, and how do you fix it?

Code that moves something by a fixed amount per `requestAnimationFrame` call assumes 60 frames per second. On 120 Hz or 144 Hz screens, `requestAnimationFrame` runs twice as often, so the animation runs twice as fast. On slow devices or with dropped frames, it runs slower.

Use the timestamp passed to the callback and move by elapsed time:

```js
let last;
function frame(time) {
  const dt = last === undefined ? 0 : (time - last) / 1000;
  last = time;
  x += speedPixelsPerSecond * dt;
  draw(x);
  requestAnimationFrame(frame);
}
requestAnimationFrame(frame);
```

Better yet, use CSS animations or the Web Animations API, which are time based by default. You can test different refresh rates with the Frame rendering stats overlay and on real high refresh rate devices.

## 444: How do you debug objects wrapped in a Proxy, like in reactive state libraries?

Libraries like Vue, MobX, Immer drafts, Valtio and Solid stores wrap your data in `Proxy` objects. In the console you see `Proxy(Object)` with `[[Handler]]` and `[[Target]]`, which is harder to read, and logging a draft after it is finished may throw ("Cannot perform 'get' on a proxy that has been revoked" in Immer).

Convert to plain data before logging: `toRaw()` in Vue, `toJS()` in MobX, `current(draft)` in Immer, `snapshot()` in Valtio, or `structuredClone`/`JSON.parse(JSON.stringify(...))` as a last resort. Also remember that proxies can hide mutation bugs: changing the raw object directly instead of through the proxy doesn't trigger updates. Most of these libraries have their own DevTools extension, which shows state much more clearly.

## 445: How do you run a useful postmortem after a serious production bug?

- Write a timeline: when it started, when it was noticed, how, what was done, when it was fixed.
- Describe the impact: how many users, which features, how long.
- Find the root cause and the contributing factors (missing test, no alert, risky deploy process, unclear ownership), not just the line of code.
- Keep it blameless: focus on what in the system allowed the mistake, so people share information honestly.
- Agree on concrete action items with owners: a test, an alert, a lint rule, a safer rollout, better logging.
- Share it, so other teams learn from it.

The goal is that the same kind of bug is caught earlier, or can't happen again.

## 446: How do you make a front-end app easier to debug from the start?

- Ship source maps to your error tracker for every release, and tag everything with the release version.
- Use error boundaries and global handlers for errors and unhandled rejections.
- Add structured logging with request or trace ids that connect to the back end.
- Collect RUM with attribution for Web Vitals.
- Keep feature flags visible in error reports.
- Name things: named functions, readable `displayName`s, `performance.measure` for important operations.
- Write good error messages that include the values involved (`Order 42 has no items`, not `Invalid state`).
- Validate external data at the edges, so bad data fails early with a clear message instead of deep in the UI.
- Keep a way to turn on verbose logging for one user or session in production.

## 447: How do you decide between logging, breakpoints, tracing, profiling and session replay?

- **Breakpoints:** when you can reproduce locally and need to see the state at one moment.
- **Logging (or logpoints):** when you need to see values over time, in order, or across many events, or when pausing changes the behavior.
- **Performance profiling:** when the problem is speed or smoothness; it shows where time goes, which logs can't.
- **Memory snapshots:** for growth and leaks.
- **Distributed tracing:** when a request crosses services and you need to know which part is slow or failing.
- **Session replay:** when you can't reproduce a user's problem and need to see what they did.
- **Error tracking:** to know what fails in production, how often, and for whom.

Experienced debuggers switch between these quickly instead of trying to solve everything with one tool.

## 448: How do you avoid wasting hours on the wrong lead while debugging?

- Write down your current guess and what result would prove it wrong, then test that quickly.
- Check assumptions early: is the code you're reading the code that runs? Is the data what you think? Is it the right environment?
- Timebox: if a lead hasn't given new information in, say, 30 minutes, step back and gather more data instead of digging deeper.
- Change one thing at a time, so you know what made a difference.
- Use bisecting (code, commits, data) when you don't know where to look.
- Ask for help with a clear summary of what you tried; explaining it often shows the answer, and a fresh look catches what you missed.

## 449: How do you make sure a bug fix is correct and the bug doesn't come back?

- Confirm the fix with the original reproduction steps, not just "the error is gone".
- Make sure you understand why the fix works. If you don't, you may have hidden the symptom.
- Write a test that fails without the fix and passes with it: a unit test for logic, a component test for UI, an end-to-end test for flows across systems.
- Check related code for the same mistake (search for the same pattern).
- After release, watch the error tracker and metrics to confirm the errors stopped.
- If the bug was hard to find, improve the tooling: better error messages, logging, a lint rule or a type that makes it impossible.

## 450: Walk through how you would debug an unknown bug in a codebase you don't know yet.

1. **Reproduce it** and write down the exact steps, environment and expected result.
2. **Collect evidence** without reading much code: console errors, the Network panel, error tracker events, logs.
3. **Find the entry point** from the outside: the element in React or Angular DevTools to find the component, the Initiator of the failing request, a DOM breakpoint on the element that changes, or a search for a text string or API path.
4. **Follow the data** from that point with breakpoints, checking at each step where the value stops being what you expect.
5. **Narrow it down** with bisecting: `git bisect` if it used to work, or removing parts until the bug goes away.
6. **Understand the cause** before changing anything, and read the git history of the file to see why the code is the way it is.
7. **Fix it with a test**, keep the change small, and explain the cause in the pull request.
8. **Ask the owners** if the fix touches behavior you're unsure about; they may know about edge cases that aren't written down.
