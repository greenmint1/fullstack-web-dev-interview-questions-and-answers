# Chrome DevTools Interview Questions and Answers

_Last updated: October 28, 2026_

450 Chrome DevTools interview questions with answers, split into three levels: 150 easy, 150 moderate and 150 advanced.

The answers are written for current Chrome (version 147 and later). They cover the main panels (Elements, Console, Sources, Network, Performance, Memory, Application, Lighthouse, Recorder), debugging and performance work, the Chrome DevTools Protocol, and newer features like the Performance panel insights, AI assistance and the DevTools MCP server. DevTools changes often, so some menu names and locations may be a bit different in your version.

## Table of Contents

- [Easy Questions (1-150)](#easy-questions-1-150)
- [Moderate Questions (151-300)](#moderate-questions-151-300)
- [Advanced Questions (301-450)](#advanced-questions-301-450)

### Easy Questions (1-150)

- [1: What is Chrome DevTools?](#1-what-is-chrome-devtools)
- [2: How do you open DevTools?](#2-how-do-you-open-devtools)
- [3: What are the main panels in DevTools?](#3-what-are-the-main-panels-in-devtools)
- [4: What is the Elements panel used for?](#4-what-is-the-elements-panel-used-for)
- [5: What is the difference between the HTML source and the DOM shown in the Elements panel?](#5-what-is-the-difference-between-the-html-source-and-the-dom-shown-in-the-elements-panel)
- [6: How do you inspect a specific element on the page?](#6-how-do-you-inspect-a-specific-element-on-the-page)
- [7: How do you edit the text or attributes of an element?](#7-how-do-you-edit-the-text-or-attributes-of-an-element)
- [8: How do you delete or hide an element in the Elements panel?](#8-how-do-you-delete-or-hide-an-element-in-the-elements-panel)
- [9: What is the Styles pane?](#9-what-is-the-styles-pane)
- [10: How do you add a new CSS rule in DevTools?](#10-how-do-you-add-a-new-css-rule-in-devtools)
- [11: What does the Computed tab show?](#11-what-does-the-computed-tab-show)
- [12: What is the box model view in DevTools?](#12-what-is-the-box-model-view-in-devtools)
- [13: How do you force an element into the `:hover` or `:focus` state?](#13-how-do-you-force-an-element-into-the-hover-or-focus-state)
- [14: How do you add or remove a class on an element quickly?](#14-how-do-you-add-or-remove-a-class-on-an-element-quickly)
- [15: What is the Console panel?](#15-what-is-the-console-panel)
- [16: How do you open the Console while working in another panel?](#16-how-do-you-open-the-console-while-working-in-another-panel)
- [17: What message levels can the Console show, and how do you filter them?](#17-what-message-levels-can-the-console-show-and-how-do-you-filter-them)
- [18: What is the difference between `console.log`, `console.warn` and `console.error`?](#18-what-is-the-difference-between-consolelog-consolewarn-and-consoleerror)
- [19: What does `console.table` do?](#19-what-does-consoletable-do)
- [20: How do you clear the Console?](#20-how-do-you-clear-the-console)
- [21: What does "Preserve log" do in the Console?](#21-what-does-preserve-log-do-in-the-console)
- [22: What is the Sources panel?](#22-what-is-the-sources-panel)
- [23: How do you open a file quickly in the Sources panel?](#23-how-do-you-open-a-file-quickly-in-the-sources-panel)
- [24: What is a breakpoint?](#24-what-is-a-breakpoint)
- [25: How is a breakpoint better than `console.log`?](#25-how-is-a-breakpoint-better-than-consolelog)
- [26: What does the `debugger` statement do?](#26-what-does-the-debugger-statement-do)
- [27: What do the step buttons in the debugger do?](#27-what-do-the-step-buttons-in-the-debugger-do)
- [28: What is the Scope pane?](#28-what-is-the-scope-pane)
- [29: What is the Call Stack pane?](#29-what-is-the-call-stack-pane)
- [30: What is the Watch pane?](#30-what-is-the-watch-pane)
- [31: What is the Network panel?](#31-what-is-the-network-panel)
- [32: How do you see the details of a single network request?](#32-how-do-you-see-the-details-of-a-single-network-request)
- [33: How do you filter requests in the Network panel?](#33-how-do-you-filter-requests-in-the-network-panel)
- [34: What does "Disable cache" do?](#34-what-does-disable-cache-do)
- [35: What does "Preserve log" do in the Network panel?](#35-what-does-preserve-log-do-in-the-network-panel)
- [36: What do the colors and numbers in the Status column mean?](#36-what-do-the-colors-and-numbers-in-the-status-column-mean)
- [37: How do you see the response body of an API call?](#37-how-do-you-see-the-response-body-of-an-api-call)
- [38: What is network throttling?](#38-what-is-network-throttling)
- [39: How do you test how a page works offline?](#39-how-do-you-test-how-a-page-works-offline)
- [40: What is Device Mode?](#40-what-is-device-mode)
- [41: Is Device Mode the same as testing on a real phone?](#41-is-device-mode-the-same-as-testing-on-a-real-phone)
- [42: What is the Application panel?](#42-what-is-the-application-panel)
- [43: How do you view and edit Local Storage?](#43-how-do-you-view-and-edit-local-storage)
- [44: How do you view the cookies of a site?](#44-how-do-you-view-the-cookies-of-a-site)
- [45: Can you see `HttpOnly` cookies in DevTools?](#45-can-you-see-httponly-cookies-in-devtools)
- [46: What is Lighthouse in DevTools?](#46-what-is-lighthouse-in-devtools)
- [47: How do you take a screenshot with DevTools?](#47-how-do-you-take-a-screenshot-with-devtools)
- [48: What is the Command Menu?](#48-what-is-the-command-menu)
- [49: How do you change where DevTools is docked?](#49-how-do-you-change-where-devtools-is-docked)
- [50: How do you switch DevTools to a dark theme?](#50-how-do-you-switch-devtools-to-a-dark-theme)
- [51: What is `$0` in the Console?](#51-what-is-0-in-the-console)
- [52: What do `$()` and `$$()` do in the Console?](#52-what-do--and--do-in-the-console)
- [53: What is `$_` in the Console?](#53-what-is-_-in-the-console)
- [54: What does `copy()` do in the Console?](#54-what-does-copy-do-in-the-console)
- [55: What does `console.dir` do and how is it different from `console.log`?](#55-what-does-consoledir-do-and-how-is-it-different-from-consolelog)
- [56: How do you show an object as JavaScript properties instead of HTML in the Console?](#56-how-do-you-show-an-object-as-javascript-properties-instead-of-html-in-the-console)
- [57: What does "Store as global variable" do?](#57-what-does-store-as-global-variable-do)
- [58: How do you use `console.group`?](#58-how-do-you-use-consolegroup)
- [59: How do you measure how long some code takes with the Console?](#59-how-do-you-measure-how-long-some-code-takes-with-the-console)
- [60: What does `console.count` do?](#60-what-does-consolecount-do)
- [61: What does `console.assert` do?](#61-what-does-consoleassert-do)
- [62: What does `console.trace` do?](#62-what-does-consoletrace-do)
- [63: How do you style text in `console.log`?](#63-how-do-you-style-text-in-consolelog)
- [64: Can you use `await` directly in the Console?](#64-can-you-use-await-directly-in-the-console)
- [65: What is a Live Expression?](#65-what-is-a-live-expression)
- [66: What is eager evaluation in the Console?](#66-what-is-eager-evaluation-in-the-console)
- [67: How do you run JavaScript in a specific iframe from the Console?](#67-how-do-you-run-javascript-in-a-specific-iframe-from-the-console)
- [68: How do you see JavaScript errors from a page?](#68-how-do-you-see-javascript-errors-from-a-page)
- [69: What does the link next to a Console message do?](#69-what-does-the-link-next-to-a-console-message-do)
- [70: What is pretty printing in the Sources panel?](#70-what-is-pretty-printing-in-the-sources-panel)
- [71: How do you search across all loaded files?](#71-how-do-you-search-across-all-loaded-files)
- [72: What are Snippets?](#72-what-are-snippets)
- [73: How do you disable JavaScript for a page?](#73-how-do-you-disable-javascript-for-a-page)
- [74: How do you reload the page while emptying the cache?](#74-how-do-you-reload-the-page-while-emptying-the-cache)
- [75: What is the drawer in DevTools?](#75-what-is-the-drawer-in-devtools)
- [76: How do you open a panel that is not visible in the main toolbar?](#76-how-do-you-open-a-panel-that-is-not-visible-in-the-main-toolbar)
- [77: How do you change DevTools settings?](#77-how-do-you-change-devtools-settings)
- [78: What is the size shown in the Network panel's Size column?](#78-what-is-the-size-shown-in-the-network-panels-size-column)
- [79: What does the summary bar at the bottom of the Network panel show?](#79-what-does-the-summary-bar-at-the-bottom-of-the-network-panel-show)
- [80: What are the blue and red lines in the Network waterfall?](#80-what-are-the-blue-and-red-lines-in-the-network-waterfall)
- [81: What is the Initiator column in the Network panel?](#81-what-is-the-initiator-column-in-the-network-panel)
- [82: How do you check the HTTP method and status code of a request?](#82-how-do-you-check-the-http-method-and-status-code-of-a-request)
- [83: How do you add or remove columns in the Network panel?](#83-how-do-you-add-or-remove-columns-in-the-network-panel)
- [84: How do you see the query string and the request body?](#84-how-do-you-see-the-query-string-and-the-request-body)
- [85: How do you copy a request so you can run it again outside the browser?](#85-how-do-you-copy-a-request-so-you-can-run-it-again-outside-the-browser)
- [86: How do you repeat a fetch or XHR request without reloading the page?](#86-how-do-you-repeat-a-fetch-or-xhr-request-without-reloading-the-page)
- [87: What is the Rendering tab?](#87-what-is-the-rendering-tab)
- [88: How do you test dark mode on a site without changing your OS setting?](#88-how-do-you-test-dark-mode-on-a-site-without-changing-your-os-setting)
- [89: How do you see the print version of a page?](#89-how-do-you-see-the-print-version-of-a-page)
- [90: What is the Sensors tool?](#90-what-is-the-sensors-tool)
- [91: How do you fake your geolocation in DevTools?](#91-how-do-you-fake-your-geolocation-in-devtools)
- [92: What is the Issues panel?](#92-what-is-the-issues-panel)
- [93: How do you check an element's color contrast in DevTools?](#93-how-do-you-check-an-elements-color-contrast-in-devtools)
- [94: How do you use the color picker in the Styles pane?](#94-how-do-you-use-the-color-picker-in-the-styles-pane)
- [95: What does a line through a CSS declaration in the Styles pane mean?](#95-what-does-a-line-through-a-css-declaration-in-the-styles-pane-mean)
- [96: What does a grayed-out CSS declaration with an info icon mean?](#96-what-does-a-grayed-out-css-declaration-with-an-info-icon-mean)
- [97: How do you find which file and line a CSS rule comes from?](#97-how-do-you-find-which-file-and-line-a-css-rule-comes-from)
- [98: What is the `user agent stylesheet`?](#98-what-is-the-user-agent-stylesheet)
- [99: How do you see the event listeners attached to an element?](#99-how-do-you-see-the-event-listeners-attached-to-an-element)
- [100: How do you find an element in the DOM tree by text or selector?](#100-how-do-you-find-an-element-in-the-dom-tree-by-text-or-selector)
- [101: How do you copy a CSS selector or XPath for an element?](#101-how-do-you-copy-a-css-selector-or-xpath-for-an-element)
- [102: How do you scroll the page to an element you selected in the DOM tree?](#102-how-do-you-scroll-the-page-to-an-element-you-selected-in-the-dom-tree)
- [103: How does DevTools show Shadow DOM?](#103-how-does-devtools-show-shadow-dom)
- [104: How do you see the `::before` and `::after` pseudo-elements of an element?](#104-how-do-you-see-the-before-and-after-pseudo-elements-of-an-element)
- [105: What is the Layout tab in the Elements panel?](#105-what-is-the-layout-tab-in-the-elements-panel)
- [106: What are the `grid` and `flex` badges in the DOM tree?](#106-what-are-the-grid-and-flex-badges-in-the-dom-tree)
- [107: What is the Accessibility pane in the Elements panel?](#107-what-is-the-accessibility-pane-in-the-elements-panel)
- [108: How do you see the full accessibility tree of a page?](#108-how-do-you-see-the-full-accessibility-tree-of-a-page)
- [109: What is the Memory panel?](#109-what-is-the-memory-panel)
- [110: What is a memory leak in a web page?](#110-what-is-a-memory-leak-in-a-web-page)
- [111: What is the Performance panel?](#111-what-is-the-performance-panel)
- [112: What does the Performance panel show before you record anything?](#112-what-does-the-performance-panel-show-before-you-record-anything)
- [113: What are Core Web Vitals?](#113-what-are-core-web-vitals)
- [114: How do you record a performance profile of page load?](#114-how-do-you-record-a-performance-profile-of-page-load)
- [115: How do you record a performance profile of an interaction, like clicking a button?](#115-how-do-you-record-a-performance-profile-of-an-interaction-like-clicking-a-button)
- [116: What is CPU throttling in the Performance panel?](#116-what-is-cpu-throttling-in-the-performance-panel)
- [117: What is a long task?](#117-what-is-a-long-task)
- [118: What is the Lighthouse Performance score based on?](#118-what-is-the-lighthouse-performance-score-based-on)
- [119: Why should you run Lighthouse in an Incognito window?](#119-why-should-you-run-lighthouse-in-an-incognito-window)
- [120: What is the Recorder panel?](#120-what-is-the-recorder-panel)
- [121: What is the Coverage tool?](#121-what-is-the-coverage-tool)
- [122: What is the Changes tool?](#122-what-is-the-changes-tool)
- [123: What is the Performance monitor?](#123-what-is-the-performance-monitor)
- [124: What is the Animations panel?](#124-what-is-the-animations-panel)
- [125: What are source maps?](#125-what-are-source-maps)
- [126: Where do you see original source files when source maps are loaded?](#126-where-do-you-see-original-source-files-when-source-maps-are-loaded)
- [127: What is a conditional breakpoint?](#127-what-is-a-conditional-breakpoint)
- [128: What is a logpoint?](#128-what-is-a-logpoint)
- [129: How do you remove or disable all breakpoints at once?](#129-how-do-you-remove-or-disable-all-breakpoints-at-once)
- [130: Do breakpoints stay after you reload the page?](#130-do-breakpoints-stay-after-you-reload-the-page)
- [131: How do you view Session Storage in DevTools?](#131-how-do-you-view-session-storage-in-devtools)
- [132: How do you view IndexedDB data?](#132-how-do-you-view-indexeddb-data)
- [133: What is Cache Storage in the Application panel?](#133-what-is-cache-storage-in-the-application-panel)
- [134: How do you clear all data for a site?](#134-how-do-you-clear-all-data-for-a-site)
- [135: What is a service worker and where do you see it in DevTools?](#135-what-is-a-service-worker-and-where-do-you-see-it-in-devtools)
- [136: What does the Manifest section in the Application panel show?](#136-what-does-the-manifest-section-in-the-application-panel-show)
- [137: How do you change the user agent string in DevTools?](#137-how-do-you-change-the-user-agent-string-in-devtools)
- [138: How do you see which media queries a page uses?](#138-how-do-you-see-which-media-queries-a-page-uses)
- [139: How do you change the device pixel ratio in Device Mode?](#139-how-do-you-change-the-device-pixel-ratio-in-device-mode)
- [140: Can you debug a website running on an Android phone with DevTools?](#140-can-you-debug-a-website-running-on-an-android-phone-with-devtools)
- [141: Can you debug Safari on iPhone with Chrome DevTools?](#141-can-you-debug-safari-on-iphone-with-chrome-devtools)
- [142: Can you use Chrome DevTools to debug Node.js?](#142-can-you-use-chrome-devtools-to-debug-nodejs)
- [143: What are DevTools extensions?](#143-what-are-devtools-extensions)
- [144: What does React Developer Tools add to DevTools?](#144-what-does-react-developer-tools-add-to-devtools)
- [145: What is AI assistance in Chrome DevTools?](#145-what-is-ai-assistance-in-chrome-devtools)
- [146: What does "Understand this error" do in the Console?](#146-what-does-understand-this-error-do-in-the-console)
- [147: How do you undo changes made in DevTools?](#147-how-do-you-undo-changes-made-in-devtools)
- [148: How do you open DevTools for a pop-up window or a new tab automatically?](#148-how-do-you-open-devtools-for-a-pop-up-window-or-a-new-tab-automatically)
- [149: How do you find the keyboard shortcuts for DevTools?](#149-how-do-you-find-the-keyboard-shortcuts-for-devtools)
- [150: Why do you sometimes see "Paused in debugger" on the page?](#150-why-do-you-sometimes-see-paused-in-debugger-on-the-page)

### Moderate Questions (151-300)

- [151: What types of breakpoints does DevTools support?](#151-what-types-of-breakpoints-does-devtools-support)
- [152: How do you find out which code changes a DOM element?](#152-how-do-you-find-out-which-code-changes-a-dom-element)
- [153: How do you pause when a specific fetch or XHR request is sent?](#153-how-do-you-pause-when-a-specific-fetch-or-xhr-request-is-sent)
- [154: What are event listener breakpoints?](#154-what-are-event-listener-breakpoints)
- [155: How do you pause on the very first line of any script that runs?](#155-how-do-you-pause-on-the-very-first-line-of-any-script-that-runs)
- [156: How do you pause when an exception is thrown?](#156-how-do-you-pause-when-an-exception-is-thrown)
- [157: How do you set a breakpoint on a function without knowing where it is defined?](#157-how-do-you-set-a-breakpoint-on-a-function-without-knowing-where-it-is-defined)
- [158: What does `monitor()` do in the Console?](#158-what-does-monitor-do-in-the-console)
- [159: What does `monitorEvents()` do?](#159-what-does-monitorevents-do)
- [160: What does `getEventListeners()` return?](#160-what-does-geteventlisteners-return)
- [161: What does `queryObjects()` do?](#161-what-does-queryobjects-do)
- [162: What does `inspect()` do in the Console?](#162-what-does-inspect-do-in-the-console)
- [163: What are async stack traces?](#163-what-are-async-stack-traces)
- [164: What does "Restart frame" do?](#164-what-does-restart-frame-do)
- [165: What does "Continue to here" do?](#165-what-does-continue-to-here-do)
- [166: What does "Never pause here" do?](#166-what-does-never-pause-here-do)
- [167: How do you change a variable's value while paused?](#167-how-do-you-change-a-variables-value-while-paused)
- [168: What is the ignore list in DevTools?](#168-what-is-the-ignore-list-in-devtools)
- [169: What does "Automatically add known third-party scripts to ignore list" mean?](#169-what-does-automatically-add-known-third-party-scripts-to-ignore-list-mean)
- [170: How do you edit JavaScript in DevTools and see the change without reloading?](#170-how-do-you-edit-javascript-in-devtools-and-see-the-change-without-reloading)
- [171: What are Workspaces in DevTools?](#171-what-are-workspaces-in-devtools)
- [172: What are automatic workspace folders?](#172-what-are-automatic-workspace-folders)
- [173: What are Local Overrides?](#173-what-are-local-overrides)
- [174: How can you override response headers in DevTools?](#174-how-can-you-override-response-headers-in-devtools)
- [175: How can you test a production bug fix without deploying?](#175-how-can-you-test-a-production-bug-fix-without-deploying)
- [176: How do you load a source map that is not linked from the file?](#176-how-do-you-load-a-source-map-that-is-not-linked-from-the-file)
- [177: Why might source maps not load, and how do you check?](#177-why-might-source-maps-not-load-and-how-do-you-check)
- [178: How do you block a request to see how the page behaves without it?](#178-how-do-you-block-a-request-to-see-how-the-page-behaves-without-it)
- [179: What do the phases in a request's Timing tab mean?](#179-what-do-the-phases-in-a-requests-timing-tab-mean)
- [180: What is TTFB and where do you see it in DevTools?](#180-what-is-ttfb-and-where-do-you-see-it-in-devtools)
- [181: How do you see Server-Timing values in DevTools?](#181-how-do-you-see-server-timing-values-in-devtools)
- [182: How do you find out why a resource was loaded?](#182-how-do-you-find-out-why-a-resource-was-loaded)
- [183: What do the Priority and Protocol columns tell you?](#183-what-do-the-priority-and-protocol-columns-tell-you)
- [184: How do you see the CORS preflight request in the Network panel?](#184-how-do-you-see-the-cors-preflight-request-in-the-network-panel)
- [185: How do you debug a CORS error with DevTools?](#185-how-do-you-debug-a-cors-error-with-devtools)
- [186: How do you find out why a cookie was not sent with a request?](#186-how-do-you-find-out-why-a-cookie-was-not-sent-with-a-request)
- [187: How do you inspect WebSocket messages?](#187-how-do-you-inspect-websocket-messages)
- [188: How do you inspect Server-Sent Events?](#188-how-do-you-inspect-server-sent-events)
- [189: What does a `304 Not Modified` response mean in the Network panel?](#189-what-does-a-304-not-modified-response-mean-in-the-network-panel)
- [190: What is the difference between `(memory cache)` and `(disk cache)` in the Size column?](#190-what-is-the-difference-between-memory-cache-and-disk-cache-in-the-size-column)
- [191: How do you check if a request was handled by a service worker?](#191-how-do-you-check-if-a-request-was-handled-by-a-service-worker)
- [192: What are some useful keyword filters in the Network panel?](#192-what-are-some-useful-keyword-filters-in-the-network-panel)
- [193: How do you create a custom network throttling profile?](#193-how-do-you-create-a-custom-network-throttling-profile)
- [194: What is a HAR file, and how do you export one?](#194-what-is-a-har-file-and-how-do-you-export-one)
- [195: Why should you be careful when sharing HAR files?](#195-why-should-you-be-careful-when-sharing-har-files)
- [196: How do you see all requests going to a third-party domain?](#196-how-do-you-see-all-requests-going-to-a-third-party-domain)
- [197: How do you find which requests block page rendering?](#197-how-do-you-find-which-requests-block-page-rendering)
- [198: What are the Fetch/XHR, Doc and Other filters useful for?](#198-what-are-the-fetchxhr-doc-and-other-filters-useful-for)
- [199: How do you see redirects in the Network panel?](#199-how-do-you-see-redirects-in-the-network-panel)
- [200: How do you check compression of responses?](#200-how-do-you-check-compression-of-responses)
- [201: How do you read the flame chart in the Performance panel?](#201-how-do-you-read-the-flame-chart-in-the-performance-panel)
- [202: What do the colors in the Performance panel mean?](#202-what-do-the-colors-in-the-performance-panel-mean)
- [203: What are the Summary, Bottom-up, Call tree and Event log tabs?](#203-what-are-the-summary-bottom-up-call-tree-and-event-log-tabs)
- [204: What is the difference between self time and total time?](#204-what-is-the-difference-between-self-time-and-total-time)
- [205: What tracks can you see in a Performance recording?](#205-what-tracks-can-you-see-in-a-performance-recording)
- [206: What does the Insights sidebar in the Performance panel do?](#206-what-does-the-insights-sidebar-in-the-performance-panel-do)
- [207: What is the LCP breakdown in the Performance panel?](#207-what-is-the-lcp-breakdown-in-the-performance-panel)
- [208: What is the INP breakdown in the Performance panel?](#208-what-is-the-inp-breakdown-in-the-performance-panel)
- [209: How do you find which interaction has the worst INP?](#209-how-do-you-find-which-interaction-has-the-worst-inp)
- [210: How do you find the cause of a layout shift?](#210-how-do-you-find-the-cause-of-a-layout-shift)
- [211: How do you compare your local metrics with real-user data in DevTools?](#211-how-do-you-compare-your-local-metrics-with-real-user-data-in-devtools)
- [212: What is the difference between lab data and field data?](#212-what-is-the-difference-between-lab-data-and-field-data)
- [213: How do you add notes to a performance trace?](#213-how-do-you-add-notes-to-a-performance-trace)
- [214: How do you save and share a Performance recording?](#214-how-do-you-save-and-share-a-performance-recording)
- [215: What does "Dim 3rd parties" do in the Performance panel?](#215-what-does-dim-3rd-parties-do-in-the-performance-panel)
- [216: How do you hide functions you don't care about in the flame chart?](#216-how-do-you-hide-functions-you-dont-care-about-in-the-flame-chart)
- [217: How do you zoom and move around in a Performance recording?](#217-how-do-you-zoom-and-move-around-in-a-performance-recording)
- [218: What does a red triangle on a Performance event mean?](#218-what-does-a-red-triangle-on-a-performance-event-mean)
- [219: How do you find forced reflows in a recording?](#219-how-do-you-find-forced-reflows-in-a-recording)
- [220: What is paint flashing and when would you use it?](#220-what-is-paint-flashing-and-when-would-you-use-it)
- [221: What does "Layer borders" in the Rendering tab show?](#221-what-does-layer-borders-in-the-rendering-tab-show)
- [222: What is the Layers panel?](#222-what-is-the-layers-panel)
- [223: What does "Frame rendering stats" show?](#223-what-does-frame-rendering-stats-show)
- [224: What does "Scrolling performance issues" in the Rendering tab do?](#224-what-does-scrolling-performance-issues-in-the-rendering-tab-do)
- [225: What CSS media features can you emulate in the Rendering tab?](#225-what-css-media-features-can-you-emulate-in-the-rendering-tab)
- [226: How do you simulate vision deficiencies?](#226-how-do-you-simulate-vision-deficiencies)
- [227: What does "Emulate a focused page" do?](#227-what-does-emulate-a-focused-page-do)
- [228: How do you inspect an element that disappears when you move the mouse?](#228-how-do-you-inspect-an-element-that-disappears-when-you-move-the-mouse)
- [229: How does the Performance panel's CPU throttling differ between presets?](#229-how-does-the-performance-panels-cpu-throttling-differ-between-presets)
- [230: What other capture settings does the Performance panel have?](#230-what-other-capture-settings-does-the-performance-panel-have)
- [231: How do you see which CSS selectors are slow?](#231-how-do-you-see-which-css-selectors-are-slow)
- [232: What does the Memory checkbox in the Performance panel show?](#232-what-does-the-memory-checkbox-in-the-performance-panel-show)
- [233: What are the Lighthouse modes?](#233-what-are-the-lighthouse-modes)
- [234: Why do Lighthouse scores differ between runs?](#234-why-do-lighthouse-scores-differ-between-runs)
- [235: What is the difference between simulated and DevTools throttling in Lighthouse?](#235-what-is-the-difference-between-simulated-and-devtools-throttling-in-lighthouse)
- [236: Which categories does Lighthouse audit today?](#236-which-categories-does-lighthouse-audit-today)
- [237: Should you aim for a Lighthouse performance score of 100?](#237-should-you-aim-for-a-lighthouse-performance-score-of-100)
- [238: How do you run a Lighthouse audit on a page behind a login?](#238-how-do-you-run-a-lighthouse-audit-on-a-page-behind-a-login)
- [239: How do you replay a recording in the Recorder at a slower speed?](#239-how-do-you-replay-a-recording-in-the-recorder-at-a-slower-speed)
- [240: How do you measure performance of a user flow with the Recorder?](#240-how-do-you-measure-performance-of-a-user-flow-with-the-recorder)
- [241: What selectors does the Recorder use for steps?](#241-what-selectors-does-the-recorder-use-for-steps)
- [242: What formats can you export a Recorder flow to?](#242-what-formats-can-you-export-a-recorder-flow-to)
- [243: How do you check unused CSS and JavaScript with the Coverage tool in a useful way?](#243-how-do-you-check-unused-css-and-javascript-with-the-coverage-tool-in-a-useful-way)
- [244: What is the difference between per function and per block coverage?](#244-what-is-the-difference-between-per-function-and-per-block-coverage)
- [245: How do you inspect and change a CSS animation's timing?](#245-how-do-you-inspect-and-change-a-css-animations-timing)
- [246: How do you debug Flexbox layout problems in DevTools?](#246-how-do-you-debug-flexbox-layout-problems-in-devtools)
- [247: How do you debug a CSS Grid layout in DevTools?](#247-how-do-you-debug-a-css-grid-layout-in-devtools)
- [248: How do you debug container queries in DevTools?](#248-how-do-you-debug-container-queries-in-devtools)
- [249: How does the Styles pane show cascade layers?](#249-how-does-the-styles-pane-show-cascade-layers)
- [250: How do you find where a CSS custom property is defined?](#250-how-do-you-find-where-a-css-custom-property-is-defined)
- [251: What views does a heap snapshot have?](#251-what-views-does-a-heap-snapshot-have)
- [252: What is the difference between shallow size and retained size?](#252-what-is-the-difference-between-shallow-size-and-retained-size)
- [253: What is the Retainers section in a heap snapshot?](#253-what-is-the-retainers-section-in-a-heap-snapshot)
- [254: What does the Distance column in a heap snapshot mean?](#254-what-does-the-distance-column-in-a-heap-snapshot-mean)
- [255: How do you find a memory leak with heap snapshots?](#255-how-do-you-find-a-memory-leak-with-heap-snapshots)
- [256: What is a detached DOM element?](#256-what-is-a-detached-dom-element)
- [257: How do you find detached DOM elements?](#257-how-do-you-find-detached-dom-elements)
- [258: What is "Allocations on timeline"?](#258-what-is-allocations-on-timeline)
- [259: What is "Allocation sampling"?](#259-what-is-allocation-sampling)
- [260: Why do objects stay in memory after you log them in the Console?](#260-why-do-objects-stay-in-memory-after-you-log-them-in-the-console)
- [261: How do you force garbage collection in DevTools?](#261-how-do-you-force-garbage-collection-in-devtools)
- [262: What does "Update on reload" do for service workers?](#262-what-does-update-on-reload-do-for-service-workers)
- [263: What does "Bypass for network" do?](#263-what-does-bypass-for-network-do)
- [264: How do you debug service worker code?](#264-how-do-you-debug-service-worker-code)
- [265: How do you test push notifications without a push server?](#265-how-do-you-test-push-notifications-without-a-push-server)
- [266: What is the back/forward cache, and how do you test it in DevTools?](#266-what-is-the-backforward-cache-and-how-do-you-test-it-in-devtools)
- [267: What does Application > Speculative loads show?](#267-what-does-application--speculative-loads-show)
- [268: How do you test what happens when storage is almost full?](#268-how-do-you-test-what-happens-when-storage-is-almost-full)
- [269: What does the Partition Key column in the Cookies view mean?](#269-what-does-the-partition-key-column-in-the-cookies-view-mean)
- [270: How do you see the frames on a page and their security details?](#270-how-do-you-see-the-frames-on-a-page-and-their-security-details)
- [271: How do you override the timezone and locale for a page?](#271-how-do-you-override-the-timezone-and-locale-for-a-page)
- [272: How do you emulate device orientation?](#272-how-do-you-emulate-device-orientation)
- [273: How do you add a custom device to Device Mode?](#273-how-do-you-add-a-custom-device-to-device-mode)
- [274: What is port forwarding in remote debugging?](#274-what-is-port-forwarding-in-remote-debugging)
- [275: Why is `node --inspect=0.0.0.0` risky?](#275-why-is-node---inspect0000-risky)
- [276: How do you debug a web worker in DevTools?](#276-how-do-you-debug-a-web-worker-in-devtools)
- [277: What do the Console settings "Selected context only" and "Group similar messages" do?](#277-what-do-the-console-settings-selected-context-only-and-group-similar-messages-do)
- [278: How do you see only messages from your own code in the Console?](#278-how-do-you-see-only-messages-from-your-own-code-in-the-console)
- [279: What does "Log XMLHttpRequests" do?](#279-what-does-log-xmlhttprequests-do)
- [280: What does the Privacy and security panel show?](#280-what-does-the-privacy-and-security-panel-show)
- [281: How do you find mixed content on a page?](#281-how-do-you-find-mixed-content-on-a-page)
- [282: What is the WebAuthn panel used for?](#282-what-is-the-webauthn-panel-used-for)
- [283: What is the Media panel?](#283-what-is-the-media-panel)
- [284: How do you move a DOM node to another place in the tree?](#284-how-do-you-move-a-dom-node-to-another-place-in-the-tree)
- [285: What is `inspector-stylesheet`?](#285-what-is-inspector-stylesheet)
- [286: How do you copy CSS from the Styles pane?](#286-how-do-you-copy-css-from-the-styles-pane)
- [287: How do you check which fonts an element actually uses?](#287-how-do-you-check-which-fonts-an-element-actually-uses)
- [288: How do you debug keyboard focus problems with DevTools?](#288-how-do-you-debug-keyboard-focus-problems-with-devtools)
- [289: How do you check accessibility issues of a page with DevTools?](#289-how-do-you-check-accessibility-issues-of-a-page-with-devtools)
- [290: What do the "Accessibility" checks in the inspect tooltip mean?](#290-what-do-the-accessibility-checks-in-the-inspect-tooltip-mean)
- [291: How can AI assistance help with CSS debugging?](#291-how-can-ai-assistance-help-with-css-debugging)
- [292: What kinds of context can you give AI assistance?](#292-what-kinds-of-context-can-you-give-ai-assistance)
- [293: What should you keep in mind about privacy when using AI assistance?](#293-what-should-you-keep-in-mind-about-privacy-when-using-ai-assistance)
- [294: What is code generation in the Console and Sources panels?](#294-what-is-code-generation-in-the-console-and-sources-panels)
- [295: How do you see the component tree of an Angular app in DevTools?](#295-how-do-you-see-the-component-tree-of-an-angular-app-in-devtools)
- [296: What does Redux DevTools add?](#296-what-does-redux-devtools-add)
- [297: How do you hide network messages and violations from the Console?](#297-how-do-you-hide-network-messages-and-violations-from-the-console)
- [298: What are "[Violation]" messages in the Console?](#298-what-are-violation-messages-in-the-console)
- [299: How do you debug code inside an iframe in the Sources panel?](#299-how-do-you-debug-code-inside-an-iframe-in-the-sources-panel)
- [300: How do you check that `preload` and `fetchpriority` hints work?](#300-how-do-you-check-that-preload-and-fetchpriority-hints-work)

### Advanced Questions (301-450)

- [301: How does DevTools talk to the page it inspects?](#301-how-does-devtools-talk-to-the-page-it-inspects)
- [302: What is the Chrome DevTools Protocol?](#302-what-is-the-chrome-devtools-protocol)
- [303: Is the DevTools frontend a native app?](#303-is-the-devtools-frontend-a-native-app)
- [304: How do you inspect DevTools itself?](#304-how-do-you-inspect-devtools-itself)
- [305: How do you connect to Chrome with CDP from your own script?](#305-how-do-you-connect-to-chrome-with-cdp-from-your-own-script)
- [306: Why does recent Chrome refuse `--remote-debugging-port` on the default profile?](#306-why-does-recent-chrome-refuse---remote-debugging-port-on-the-default-profile)
- [307: What is the Protocol monitor?](#307-what-is-the-protocol-monitor)
- [308: How does Puppeteer use CDP?](#308-how-does-puppeteer-use-cdp)
- [309: What is WebDriver BiDi and how is it related to CDP?](#309-what-is-webdriver-bidi-and-how-is-it-related-to-cdp)
- [310: How do you record a performance trace from a script?](#310-how-do-you-record-a-performance-trace-from-a-script)
- [311: What is the Chrome DevTools MCP server?](#311-what-is-the-chrome-devtools-mcp-server)
- [312: What are the risks of giving an AI agent access to the browser through the DevTools MCP server?](#312-what-are-the-risks-of-giving-an-ai-agent-access-to-the-browser-through-the-devtools-mcp-server)
- [313: How do you add your own data to the Performance panel?](#313-how-do-you-add-your-own-data-to-the-performance-panel)
- [314: What does `console.timeStamp()` do in newer versions of Chrome?](#314-what-does-consoletimestamp-do-in-newer-versions-of-chrome)
- [315: How does the JavaScript profiler in the Performance panel collect data?](#315-how-does-the-javascript-profiler-in-the-performance-panel-collect-data)
- [316: Why can a function show up as "(anonymous)" or with a strange name in a profile?](#316-why-can-a-function-show-up-as-anonymous-or-with-a-strange-name-in-a-profile)
- [317: How are source maps structured?](#317-how-are-source-maps-structured)
- [318: Is it safe to publish source maps in production?](#318-is-it-safe-to-publish-source-maps-in-production)
- [319: Why do breakpoints sometimes jump to a different line, or not hit, with source maps?](#319-why-do-breakpoints-sometimes-jump-to-a-different-line-or-not-hit-with-source-maps)
- [320: How does live editing JavaScript work under the hood?](#320-how-does-live-editing-javascript-work-under-the-hood)
- [321: How does a breakpoint actually work in V8?](#321-how-does-a-breakpoint-actually-work-in-v8)
- [322: Why can an open DevTools make the page slower?](#322-why-can-an-open-devtools-make-the-page-slower)
- [323: Why do variables sometimes show as "value unavailable" or "optimized out" in the debugger?](#323-why-do-variables-sometimes-show-as-value-unavailable-or-optimized-out-in-the-debugger)
- [324: What does the `(closure)`, `(system)` and `(compiled code)` grouping in a heap snapshot mean?](#324-what-does-the-closure-system-and-compiled-code-grouping-in-a-heap-snapshot-mean)
- [325: How can a closure cause a memory leak?](#325-how-can-a-closure-cause-a-memory-leak)
- [326: How do WeakMap and WeakRef affect what you see in heap snapshots?](#326-how-do-weakmap-and-weakref-affect-what-you-see-in-heap-snapshots)
- [327: What is a dominator in heap analysis?](#327-what-is-a-dominator-in-heap-analysis)
- [328: How do you find a leak caused by an event listener that is never removed?](#328-how-do-you-find-a-leak-caused-by-an-event-listener-that-is-never-removed)
- [329: How do you debug a memory leak in a single-page app when navigating between routes?](#329-how-do-you-debug-a-memory-leak-in-a-single-page-app-when-navigating-between-routes)
- [330: How do you analyze memory of a Node.js process with DevTools?](#330-how-do-you-analyze-memory-of-a-nodejs-process-with-devtools)
- [331: What is the Memory inspector?](#331-what-is-the-memory-inspector)
- [332: How do you debug WebAssembly in DevTools?](#332-how-do-you-debug-webassembly-in-devtools)
- [333: How does a DevTools extension work?](#333-how-does-a-devtools-extension-work)
- [334: How do framework DevTools extensions get component data from the page?](#334-how-do-framework-devtools-extensions-get-component-data-from-the-page)
- [335: What is the trace event format?](#335-what-is-the-trace-event-format)
- [336: How do Long Animation Frames relate to what you see in DevTools?](#336-how-do-long-animation-frames-relate-to-what-you-see-in-devtools)
- [337: How do you profile a web page on an Android phone?](#337-how-do-you-profile-a-web-page-on-an-android-phone)
- [338: What are the limits of Device Mode and throttling for performance testing?](#338-what-are-the-limits-of-device-mode-and-throttling-for-performance-testing)
- [339: Why might Lighthouse in DevTools and PageSpeed Insights give different results?](#339-why-might-lighthouse-in-devtools-and-pagespeed-insights-give-different-results)
- [340: How does Chrome decide what counts as third-party in the Performance panel?](#340-how-does-chrome-decide-what-counts-as-third-party-in-the-performance-panel)
- [341: How would you use CDP to emulate a slow device in automated tests?](#341-how-would-you-use-cdp-to-emulate-a-slow-device-in-automated-tests)
- [342: How can you intercept and modify requests with CDP?](#342-how-can-you-intercept-and-modify-requests-with-cdp)
- [343: How do you collect JavaScript coverage in automated tests?](#343-how-do-you-collect-javascript-coverage-in-automated-tests)
- [344: Why are DevTools features sometimes behind experiments, and how do you turn them on?](#344-why-are-devtools-features-sometimes-behind-experiments-and-how-do-you-turn-them-on)
- [345: What happens in a heap snapshot when you take it on a big app?](#345-what-happens-in-a-heap-snapshot-when-you-take-it-on-a-big-app)
- [346: Why does the JS heap size in DevTools differ from the memory shown in Chrome's Task Manager?](#346-why-does-the-js-heap-size-in-devtools-differ-from-the-memory-shown-in-chromes-task-manager)
- [347: How do you check what is keeping a `<canvas>` or image memory high?](#347-how-do-you-check-what-is-keeping-a-canvas-or-image-memory-high)
- [348: How do you use DevTools to verify Content Security Policy problems?](#348-how-do-you-use-devtools-to-verify-content-security-policy-problems)
- [349: What are Trusted Types violation breakpoints?](#349-what-are-trusted-types-violation-breakpoints)
- [350: How does the debugger handle code running in a cross-origin iframe with site isolation?](#350-how-does-the-debugger-handle-code-running-in-a-cross-origin-iframe-with-site-isolation)
- [351: A page has a slow LCP. How would you debug it with DevTools?](#351-a-page-has-a-slow-lcp-how-would-you-debug-it-with-devtools)
- [352: A button click feels slow. How would you find out why?](#352-a-button-click-feels-slow-how-would-you-find-out-why)
- [353: How do you break up a long task found in the Performance panel?](#353-how-do-you-break-up-a-long-task-found-in-the-performance-panel)
- [354: What is layout thrashing, and how does it look in a trace?](#354-what-is-layout-thrashing-and-how-does-it-look-in-a-trace)
- [355: An animation is janky. How would you investigate it?](#355-an-animation-is-janky-how-would-you-investigate-it)
- [356: How do you check that an animation runs on the compositor?](#356-how-do-you-check-that-an-animation-runs-on-the-compositor)
- [357: Why can too much `will-change` hurt performance?](#357-why-can-too-much-will-change-hurt-performance)
- [358: How do you find out what is causing slow scrolling on a page?](#358-how-do-you-find-out-what-is-causing-slow-scrolling-on-a-page)
- [359: How does DOM size affect performance, and how does DevTools show it?](#359-how-does-dom-size-affect-performance-and-how-does-devtools-show-it)
- [360: How do you check if `content-visibility: auto` is helping?](#360-how-do-you-check-if-content-visibility-auto-is-helping)
- [361: The TTFB of the main document is high. What can DevTools tell you?](#361-the-ttfb-of-the-main-document-is-high-what-can-devtools-tell-you)
- [362: How do you find request chains that delay loading?](#362-how-do-you-find-request-chains-that-delay-loading)
- [363: How do you check if a `preconnect` hint actually helps?](#363-how-do-you-check-if-a-preconnect-hint-actually-helps)
- [364: How can you tell if HTTP/2 or HTTP/3 connections are being reused?](#364-how-can-you-tell-if-http2-or-http3-connections-are-being-reused)
- [365: How would you debug a web font that makes text appear late?](#365-how-would-you-debug-a-web-font-that-makes-text-appear-late)
- [366: How do you check whether images are too large for how they are shown?](#366-how-do-you-check-whether-images-are-too-large-for-how-they-are-shown)
- [367: How do you verify that lazy loading works correctly?](#367-how-do-you-verify-that-lazy-loading-works-correctly)
- [368: How do you find duplicated or legacy JavaScript in your bundles?](#368-how-do-you-find-duplicated-or-legacy-javascript-in-your-bundles)
- [369: How do you measure the effect of a performance fix reliably?](#369-how-do-you-measure-the-effect-of-a-performance-fix-reliably)
- [370: How would you catch performance regressions in CI?](#370-how-would-you-catch-performance-regressions-in-ci)
- [371: How do you find out which React components make an interaction slow?](#371-how-do-you-find-out-which-react-components-make-an-interaction-slow)
- [372: How do you debug a hydration problem with DevTools?](#372-how-do-you-debug-a-hydration-problem-with-devtools)
- [373: A page fails the back/forward cache test. What are common reasons and fixes?](#373-a-page-fails-the-backforward-cache-test-what-are-common-reasons-and-fixes)
- [374: Prerendering with speculation rules is not working. How do you debug it?](#374-prerendering-with-speculation-rules-is-not-working-how-do-you-debug-it)
- [375: Users get old JavaScript after a deploy. How do you debug it with DevTools?](#375-users-get-old-javascript-after-a-deploy-how-do-you-debug-it-with-devtools)
- [376: How would you check a caching strategy for a site with DevTools?](#376-how-would-you-check-a-caching-strategy-for-a-site-with-devtools)
- [377: How do you reproduce a race condition between network requests?](#377-how-do-you-reproduce-a-race-condition-between-network-requests)
- [378: How do you debug a bug that only happens on page load and is too fast to catch?](#378-how-do-you-debug-a-bug-that-only-happens-on-page-load-and-is-too-fast-to-catch)
- [379: A bug only happens in production. How would you debug it?](#379-a-bug-only-happens-in-production-how-would-you-debug-it)
- [380: How do you test your app against a slow or failing API without changing the backend?](#380-how-do-you-test-your-app-against-a-slow-or-failing-api-without-changing-the-backend)
- [381: How do you debug an infinite loop that freezes the page?](#381-how-do-you-debug-an-infinite-loop-that-freezes-the-page)
- [382: How do you find which script added a global variable?](#382-how-do-you-find-which-script-added-a-global-variable)
- [383: How do you find out which code changes a property on an object?](#383-how-do-you-find-out-which-code-changes-a-property-on-an-object)
- [384: How would you investigate high CPU usage on an idle page?](#384-how-would-you-investigate-high-cpu-usage-on-an-idle-page)
- [385: How do you find out if a third-party script is slowing your page?](#385-how-do-you-find-out-if-a-third-party-script-is-slowing-your-page)
- [386: How do you check that work moved to a web worker actually left the main thread?](#386-how-do-you-check-that-work-moved-to-a-web-worker-actually-left-the-main-thread)
- [387: How do you measure the cost of style recalculation for a CSS change?](#387-how-do-you-measure-the-cost-of-style-recalculation-for-a-css-change)
- [388: How would you explain the rendering pipeline using what DevTools shows?](#388-how-would-you-explain-the-rendering-pipeline-using-what-devtools-shows)
- [389: Why can the Frames track show "partially presented" frames?](#389-why-can-the-frames-track-show-partially-presented-frames)
- [390: How do you profile a page with an emulated low-end device and get meaningful numbers?](#390-how-do-you-profile-a-page-with-an-emulated-low-end-device-and-get-meaningful-numbers)
- [391: What is the difference between the Network track in the Performance panel and the Network panel?](#391-what-is-the-difference-between-the-network-track-in-the-performance-panel-and-the-network-panel)
- [392: How do you find out why the LCP element changes between runs?](#392-how-do-you-find-out-why-the-lcp-element-changes-between-runs)
- [393: How do you investigate a CLS that only happens for real users?](#393-how-do-you-investigate-a-cls-that-only-happens-for-real-users)
- [394: How do you debug a memory leak that only appears after hours of use?](#394-how-do-you-debug-a-memory-leak-that-only-appears-after-hours-of-use)
- [395: How do you check that event listeners use `passive` correctly?](#395-how-do-you-check-that-event-listeners-use-passive-correctly)
- [396: How would you debug slow typing in a large text input or editor?](#396-how-would-you-debug-slow-typing-in-a-large-text-input-or-editor)
- [397: How do you analyze the JavaScript parse and compile cost of a bundle?](#397-how-do-you-analyze-the-javascript-parse-and-compile-cost-of-a-bundle)
- [398: What is V8's code cache, and can you see its effect in DevTools?](#398-what-is-v8s-code-cache-and-can-you-see-its-effect-in-devtools)
- [399: How would you debug a page that is slow only when DevTools is closed?](#399-how-would-you-debug-a-page-that-is-slow-only-when-devtools-is-closed)
- [400: How do you check Core Web Vitals for a single-page app's route changes?](#400-how-do-you-check-core-web-vitals-for-a-single-page-apps-route-changes)
- [401: Why can't you rely on hiding things from DevTools for security?](#401-why-cant-you-rely-on-hiding-things-from-devtools-for-security)
- [402: Can a website detect that DevTools is open or block it?](#402-can-a-website-detect-that-devtools-is-open-or-block-it)
- [403: How do you debug a login that works locally but loses the session in production?](#403-how-do-you-debug-a-login-that-works-locally-but-loses-the-session-in-production)
- [404: How do you debug an OAuth or SSO redirect flow?](#404-how-do-you-debug-an-oauth-or-sso-redirect-flow)
- [405: How do you debug cross-origin isolation problems?](#405-how-do-you-debug-cross-origin-isolation-problems)
- [406: How do you debug a Permissions Policy that blocks a feature?](#406-how-do-you-debug-a-permissions-policy-that-blocks-a-feature)
- [407: How do you debug third-party cookie and storage partitioning issues?](#407-how-do-you-debug-third-party-cookie-and-storage-partitioning-issues)
- [408: Why does a service worker not control a page you expect it to?](#408-why-does-a-service-worker-not-control-a-page-you-expect-it-to)
- [409: How do you debug why a PWA is not installable?](#409-how-do-you-debug-why-a-pwa-is-not-installable)
- [410: How do you debug `postMessage` communication between a page and an iframe?](#410-how-do-you-debug-postmessage-communication-between-a-page-and-an-iframe)
- [411: How do you profile CPU usage in Node.js?](#411-how-do-you-profile-cpu-usage-in-nodejs)
- [412: How do you debug Vitest or Jest tests with Chrome DevTools?](#412-how-do-you-debug-vitest-or-jest-tests-with-chrome-devtools)
- [413: How do you debug server-side code of a Next.js app with Chrome DevTools?](#413-how-do-you-debug-server-side-code-of-a-nextjs-app-with-chrome-devtools)
- [414: How do you debug a TypeScript Node app in DevTools with the original source?](#414-how-do-you-debug-a-typescript-node-app-in-devtools-with-the-original-source)
- [415: What would you check if breakpoints in a Node process never hit?](#415-what-would-you-check-if-breakpoints-in-a-node-process-never-hit)
- [416: How do you debug a z-index that doesn't work?](#416-how-do-you-debug-a-z-index-that-doesnt-work)
- [417: How do you find what causes a horizontal scrollbar on a mobile page?](#417-how-do-you-find-what-causes-a-horizontal-scrollbar-on-a-mobile-page)
- [418: Why doesn't `position: sticky` work, and how does DevTools help?](#418-why-doesnt-position-sticky-work-and-how-does-devtools-help)
- [419: How does DevTools help debug `<dialog>`, popovers and the top layer?](#419-how-does-devtools-help-debug-dialog-popovers-and-the-top-layer)
- [420: How do you debug CSS anchor positioning?](#420-how-do-you-debug-css-anchor-positioning)
- [421: How do you debug view transitions?](#421-how-do-you-debug-view-transitions)
- [422: How do you debug scroll-driven animations?](#422-how-do-you-debug-scroll-driven-animations)
- [423: How do you debug autofill problems on a form?](#423-how-do-you-debug-autofill-problems-on-a-form)
- [424: How do you test right-to-left layout with DevTools?](#424-how-do-you-test-right-to-left-layout-with-devtools)
- [425: How would you debug a GraphQL API in the Network panel?](#425-how-would-you-debug-a-graphql-api-in-the-network-panel)
- [426: How do you work with a very large JSON response in DevTools?](#426-how-do-you-work-with-a-very-large-json-response-in-devtools)
- [427: How can logging slow down your app or mislead you?](#427-how-can-logging-slow-down-your-app-or-mislead-you)
- [428: Why does an object in the Console sometimes show different values when you expand it?](#428-why-does-an-object-in-the-console-sometimes-show-different-values-when-you-expand-it)
- [429: How do you debug a CSS specificity conflict in a large codebase?](#429-how-do-you-debug-a-css-specificity-conflict-in-a-large-codebase)
- [430: How would you make DevTools part of your team's debugging workflow?](#430-how-would-you-make-devtools-part-of-your-teams-debugging-workflow)
- [431: How do Chrome DevTools compare with Firefox and Safari developer tools?](#431-how-do-chrome-devtools-compare-with-firefox-and-safari-developer-tools)
- [432: How do enterprise policies affect DevTools?](#432-how-do-enterprise-policies-affect-devtools)
- [433: How would you debug a memory leak caused by a detached iframe?](#433-how-would-you-debug-a-memory-leak-caused-by-a-detached-iframe)
- [434: How would you approach debugging a performance issue that a customer reports but you can't reproduce?](#434-how-would-you-approach-debugging-a-performance-issue-that-a-customer-reports-but-you-cant-reproduce)
- [435: What are the trade-offs of recording a trace with screenshots and JavaScript samples on?](#435-what-are-the-trade-offs-of-recording-a-trace-with-screenshots-and-javascript-samples-on)
- [436: How do you debug code that runs inside a browser extension's content script?](#436-how-do-you-debug-code-that-runs-inside-a-browser-extensions-content-script)
- [437: How do you find out if a browser extension is breaking your site?](#437-how-do-you-find-out-if-a-browser-extension-is-breaking-your-site)
- [438: How would you use the DevTools MCP server to verify a frontend fix an AI agent made?](#438-how-would-you-use-the-devtools-mcp-server-to-verify-a-frontend-fix-an-ai-agent-made)
- [439: How do you check that a website is ready for a CSP with `strict-dynamic` and nonces?](#439-how-do-you-check-that-a-website-is-ready-for-a-csp-with-strict-dynamic-and-nonces)
- [440: How do you debug a WebSocket connection that keeps disconnecting?](#440-how-do-you-debug-a-websocket-connection-that-keeps-disconnecting)
- [441: What can the Performance panel tell you about garbage collection pauses?](#441-what-can-the-performance-panel-tell-you-about-garbage-collection-pauses)
- [442: How do you use DevTools to check the cost of a framework's change detection or re-rendering?](#442-how-do-you-use-devtools-to-check-the-cost-of-a-frameworks-change-detection-or-re-rendering)
- [443: What is the best way to debug an error that has a minified stack trace from production?](#443-what-is-the-best-way-to-debug-an-error-that-has-a-minified-stack-trace-from-production)
- [444: How do you decide which DevTools tool to use for a vague "the site is slow" complaint?](#444-how-do-you-decide-which-devtools-tool-to-use-for-a-vague-the-site-is-slow-complaint)
- [445: What would you check if a page looks different in Device Mode compared to a real phone?](#445-what-would-you-check-if-a-page-looks-different-in-device-mode-compared-to-a-real-phone)
- [446: How do you check that your site works for users who prefer reduced motion?](#446-how-do-you-check-that-your-site-works-for-users-who-prefer-reduced-motion)
- [447: How do you debug an issue where clicks don't reach an element?](#447-how-do-you-debug-an-issue-where-clicks-dont-reach-an-element)
- [448: What happens, step by step, when you click "Inspect" on an element?](#448-what-happens-step-by-step-when-you-click-inspect-on-an-element)
- [449: What would you say are the strengths and weaknesses of Chrome DevTools?](#449-what-would-you-say-are-the-strengths-and-weaknesses-of-chrome-devtools)
- [450: Walk through how you would debug a page that freezes for a second after clicking "Add to cart".](#450-walk-through-how-you-would-debug-a-page-that-freezes-for-a-second-after-clicking-add-to-cart)

---

## Easy Questions (1-150)

### 1: What is Chrome DevTools?

Chrome DevTools is a set of tools for web developers that is built into Google Chrome. You use it to inspect and edit the HTML and CSS of a page, run JavaScript, debug code with breakpoints, look at network requests, check storage and measure performance. It ships with every Chrome install, so you don't need to add anything.

### 2: How do you open DevTools?

There are a few ways:

- Press `F12`, or `Ctrl+Shift+I` on Windows/Linux, or `Cmd+Option+I` on Mac.
- Right-click an element on the page and pick **Inspect**. DevTools opens with that element selected in the Elements panel.
- Open the Chrome menu and go to **More tools > Developer tools**.

`Ctrl+Shift+J` (`Cmd+Option+J` on Mac) opens DevTools straight on the Console panel.

### 3: What are the main panels in DevTools?

The panels you use most are:

- **Elements**: view and edit the DOM and CSS.
- **Console**: see logs and errors, and run JavaScript.
- **Sources**: view files, debug JavaScript and set breakpoints.
- **Network**: see every request the page makes.
- **Performance**: record and analyze runtime and loading performance.
- **Memory**: take heap snapshots and find memory leaks.
- **Application**: look at storage, cookies, service workers and the web app manifest.
- **Lighthouse**: run audits for performance, accessibility, best practices and SEO.

More panels, like Recorder, Coverage, Rendering and Animations, are under **More tools** or in the Command Menu.

### 4: What is the Elements panel used for?

It shows the live DOM of the page as a tree, with the CSS that applies to the selected element. You can edit tags, attributes and text, add or remove CSS rules, and see the box model. All changes are temporary. They are lost when you reload the page unless you save them through Workspaces or Local Overrides.

### 5: What is the difference between the HTML source and the DOM shown in the Elements panel?

The HTML source (what you see with **View page source**, `Ctrl+U`) is the original file the server sent. The Elements panel shows the current DOM, which is what the browser built from that HTML and then changed with JavaScript. If a script adds a list item or a framework renders a whole app into a `<div id="root">`, you will see those nodes in Elements but not in the page source.

### 6: How do you inspect a specific element on the page?

Right-click it and choose **Inspect**, or turn on the inspect mode with the arrow icon in the top-left of DevTools (`Ctrl+Shift+C`, `Cmd+Shift+C` on Mac) and click the element. While you hover in inspect mode, the page shows a tooltip with the element's size, color, font and accessibility info.

### 7: How do you edit the text or attributes of an element?

In the Elements panel, double-click the text, the tag name or an attribute to edit it in place. Press `Enter` to save. You can also right-click a node and choose **Edit attribute**, **Add attribute** or **Edit as HTML** to change a larger piece of markup at once.

### 8: How do you delete or hide an element in the Elements panel?

Select the node and press `Delete` to remove it from the DOM. Press `H` to hide it; this adds `visibility: hidden` through a special class, so the element still takes up space. Pressing `H` again shows it. `Ctrl+Z` undoes most changes made in the Elements panel.

### 9: What is the Styles pane?

The Styles pane sits next to the DOM tree in the Elements panel. It lists all CSS rules that match the selected element, in order of specificity, with the file and line where each rule comes from. Overridden declarations are shown with a line through them. You can click any value to change it, uncheck a declaration to turn it off, or add new declarations and rules.

### 10: How do you add a new CSS rule in DevTools?

Click the **+** (New Style Rule) button in the Styles pane. DevTools creates a rule with a selector for the selected element in a special stylesheet called `inspector-stylesheet`. You can change the selector and add declarations. You can also click inside an existing rule, after the last declaration, to add a property to that rule.

### 11: What does the Computed tab show?

It shows the final value of every CSS property for the selected element after the cascade, inheritance and default styles are applied. If you expand a property, you see which rules set it and which ones lost. Click the arrow next to a value to jump to the rule in the Styles pane. This is the fastest way to answer "why is this element red?".

### 12: What is the box model view in DevTools?

It is a diagram, shown at the bottom of the Styles pane and at the top of the Computed tab, that shows the content size, padding, border and margin of the selected element. Hovering over each area highlights it on the page. You can double-click a value in the diagram to change it.

### 13: How do you force an element into the `:hover` or `:focus` state?

Click **:hov** in the Styles pane and check the state you want: `:active`, `:hover`, `:focus`, `:visited`, `:focus-within`, `:focus-visible` or `:target`. You can also right-click the node in the DOM tree and pick **Force state**. This lets you inspect hover styles without keeping the mouse on the element.

### 14: How do you add or remove a class on an element quickly?

Click **.cls** in the Styles pane. A text field appears where you can type a class name, and every class on the element is listed with a checkbox. Unchecking a class removes it, so you can quickly see how the element looks with and without it.

### 15: What is the Console panel?

The Console shows messages logged by the page (`console.log`, warnings, errors) and errors from the browser itself, like failed requests or CSP violations. It is also a JavaScript REPL: you can type any expression and it runs in the context of the current page, with access to its variables, DOM and functions.

### 16: How do you open the Console while working in another panel?

Press `Esc`. This opens the drawer at the bottom of DevTools with the Console in it, so you can use it next to the Elements, Sources or Network panel. Press `Esc` again to close the drawer.

### 17: What message levels can the Console show, and how do you filter them?

The levels are **Verbose**, **Info**, **Warnings** and **Errors**. The **Default levels** dropdown in the Console toolbar lets you choose which ones to show. `console.debug()` messages are Verbose and are hidden by default. You can also filter by text, by regular expression (`/pattern/`), by URL with `url:`, or exclude text with `-text`.

### 18: What is the difference between `console.log`, `console.warn` and `console.error`?

All three print a message, but at different levels. `console.log` and `console.info` are Info level. `console.warn` shows a yellow warning. `console.error` shows a red error and includes a stack trace you can expand. The level matters because you can filter the Console by it, and some tools treat errors differently.

### 19: What does `console.table` do?

It prints an array or object as a table, which is much easier to read than a nested object when you have rows of data. You can pass a second argument to choose which columns to show.

```js
const users = [
  { id: 1, name: "Ana", role: "admin" },
  { id: 2, name: "Luka", role: "editor" },
];

console.table(users);
console.table(users, ["name"]);
```

### 20: How do you clear the Console?

Click the clear icon in the toolbar, press `Ctrl+L` (`Cmd+K` on Mac), or call `console.clear()` or `clear()`. If **Preserve log** is on, `console.clear()` from page code is ignored, but the button and shortcut still work.

### 21: What does "Preserve log" do in the Console?

Normally the Console is cleared every time the page navigates or reloads. With **Preserve log** turned on (in the Console settings), messages from the previous page are kept. This is useful when an error happens just before a redirect, for example after a form submit or a login.

### 22: What is the Sources panel?

The Sources panel shows all files the page loaded: HTML, JavaScript, CSS, images and source maps. Its main use is debugging JavaScript. You can set breakpoints, step through code, look at variables and the call stack, and edit files. It also has Snippets, Workspaces and Local Overrides.

### 23: How do you open a file quickly in the Sources panel?

Press `Ctrl+P` (`Cmd+P` on Mac) and start typing the file name. A fuzzy search list appears. You can add `:` and a line number, like `app.js:120`, to jump straight to that line.

### 24: What is a breakpoint?

A breakpoint is a place in the code where execution stops so you can look at what is going on. While paused, you can see the values of variables, the call stack, and step through the code line by line. In DevTools you set one by clicking the line number in the Sources panel.

### 25: How is a breakpoint better than `console.log`?

With `console.log` you only see the values you thought to print, and you have to change the code and reload each time. A breakpoint pauses the code and shows you every variable in scope, the full call stack and `this`. You can step forward, change values and run expressions while paused, without changing the source code.

### 26: What does the `debugger` statement do?

When DevTools is open, a `debugger;` statement in your code works like a breakpoint and pauses execution on that line. When DevTools is closed, it does nothing. It is handy when it is hard to find the line in Sources, for example in generated code, but remember to remove it before committing.

```js
function calculateTotal(items) {
  debugger;
  return items.reduce((sum, item) => sum + item.price, 0);
}
```

### 27: What do the step buttons in the debugger do?

- **Resume** (`F8`): run until the next breakpoint.
- **Step over** (`F10`): run the current line, without going into function calls on it.
- **Step into** (`F11`): go into the function called on the current line.
- **Step out** (`Shift+F11`): finish the current function and pause in the caller.
- **Step** (`F9`): go to the next statement, entering functions and async callbacks.

### 28: What is the Scope pane?

When execution is paused, the Scope pane shows the variables you can access at that point, grouped as **Local**, **Closure**, **Script**, **Module** and **Global**. You can expand objects and double-click a value to change it. This is how you see what a variable actually holds at a given moment.

### 29: What is the Call Stack pane?

It shows the chain of function calls that led to the current paused line, with the most recent call on top. Clicking a frame takes you to that function and updates the Scope pane, so you can see the variables in the caller. Async calls (after `await`, `setTimeout`, promise callbacks) are shown too, separated by a label.

### 30: What is the Watch pane?

The Watch pane lets you add expressions that DevTools evaluates every time execution pauses, like `user.id` or `items.length > 10`. It saves you from typing the same thing in the Console at every step. Expressions stay in the list until you remove them.

### 31: What is the Network panel?

The Network panel logs every request the page makes: HTML, CSS, JavaScript, images, fonts, fetch and XHR calls, WebSockets and more. For each request you can see the URL, status code, type, size, time, headers, payload and response. It records only while DevTools is open, so open it before you load the page.

### 32: How do you see the details of a single network request?

Click the request in the list. A side pane opens with tabs: **Headers** (URL, method, status, request and response headers), **Payload** (query string and request body), **Preview** (formatted response), **Response** (raw body), **Initiator** (what triggered it), **Timing** and **Cookies**. Fetch and WebSocket requests may have extra tabs like **Messages** or **EventStream**.

### 33: How do you filter requests in the Network panel?

Use the type buttons (All, Fetch/XHR, Doc, CSS, JS, Font, Img, Media, Manifest, WS, Wasm, Other) or type in the filter box. The filter box accepts plain text, a regular expression like `/api\/v\d/`, negative text with `-`, and keyword filters like `status-code:404`, `method:POST`, `domain:example.com` or `larger-than:100k`.

### 34: What does "Disable cache" do?

When checked, Chrome ignores the HTTP cache for requests made while DevTools is open, so every resource is downloaded again. This shows you what a first-time visitor experiences and makes sure you see your latest changes. It only works while DevTools is open. It does not bypass a service worker; use **Bypass for network** in the Application panel for that.

### 35: What does "Preserve log" do in the Network panel?

By default the request list is cleared on every navigation. With **Preserve log** on, requests from previous pages stay in the list. Use it when you need to see requests before a redirect, like a login form that posts and then redirects to a dashboard.

### 36: What do the colors and numbers in the Status column mean?

The column shows the HTTP status code. `2xx` means success, `3xx` is a redirect, `4xx` is a client error (like `404 Not Found` or `401 Unauthorized`) and `5xx` is a server error. Failed requests are shown in red. Other values you may see are `(failed)`, `(blocked:...)`, `(canceled)` and `(pending)`, which mean the request never got a normal response.

### 37: How do you see the response body of an API call?

Click the request and open the **Preview** tab to see JSON as an expandable tree, or the **Response** tab to see the raw text. For images, Preview shows the image. If the response tab is empty, the request may have failed, been canceled, or the body may not be available anymore after navigation.

### 38: What is network throttling?

Throttling makes Chrome simulate a slower connection, so you can see how your site behaves for users on mobile networks. In the Network panel, the throttling dropdown has presets like **Fast 4G**, **Slow 4G**, **3G** and **Offline**, and you can add custom profiles with your own download, upload and latency values.

### 39: How do you test how a page works offline?

Choose **Offline** in the Network panel's throttling dropdown, or check **Offline** in **Application > Service workers**. Then reload or use the page. This is how you check that a service worker serves cached files, or that your app shows a proper message when the network is down.

### 40: What is Device Mode?

Device Mode lets you see how a page looks and works on a phone or tablet. Turn it on with the device icon in the DevTools toolbar or `Ctrl+Shift+M` (`Cmd+Shift+M` on Mac). You can pick a device preset, set a custom width and height, change the device pixel ratio, rotate the screen and emulate touch.

### 41: Is Device Mode the same as testing on a real phone?

No. It is a close approximation. It changes the viewport, the user agent, the device pixel ratio and turns on touch events, but the page still runs on your desktop CPU, GPU and network. Mobile browser quirks, real touch behavior and real performance are not reproduced. Use it for layout work, and test on real devices before release.

### 42: What is the Application panel?

It shows the storage and app features of the page. You can view and edit Local Storage, Session Storage, IndexedDB, cookies and Cache Storage, inspect and control service workers, check the web app manifest, and clear all site data. It also has tools for back/forward cache, background services and speculative loads.

### 43: How do you view and edit Local Storage?

Go to **Application > Storage > Local storage** and pick the origin. You see a table of keys and values. Double-click a key or value to edit it, double-click an empty row to add one, and select a row and press `Delete` to remove it. You can also do it from the Console with `localStorage.setItem()` and `localStorage.getItem()`.

### 44: How do you view the cookies of a site?

Open **Application > Storage > Cookies** and select the origin. The table shows each cookie's name, value, domain, path, expiration, size and the flags `HttpOnly`, `Secure`, `SameSite` and `Partition Key`. You can edit values, delete one cookie, or clear all. To see which cookies were sent with a specific request, use the **Cookies** tab of that request in the Network panel.

### 45: Can you see `HttpOnly` cookies in DevTools?

Yes. JavaScript cannot read `HttpOnly` cookies through `document.cookie`, but DevTools can show them in **Application > Cookies** and in the Network panel. The flag protects the cookie from scripts running on the page, not from the person using the browser.

### 46: What is Lighthouse in DevTools?

Lighthouse is an automated audit tool built into DevTools. It loads the page and gives scores and suggestions for **Performance**, **Accessibility**, **Best Practices** and **SEO**. You open the Lighthouse panel, choose the device and categories, and click **Analyze page load**. The same engine is also available as a CLI and a Node module.

### 47: How do you take a screenshot with DevTools?

Open the Command Menu (`Ctrl+Shift+P`, `Cmd+Shift+P` on Mac) and type "screenshot". You can choose:

- **Capture screenshot**: the visible part of the page.
- **Capture full size screenshot**: the whole page, including the part you have to scroll to.
- **Capture area screenshot**: a region you select.
- **Capture node screenshot**: the element selected in the Elements panel.

### 48: What is the Command Menu?

It is a search box for almost every DevTools action, opened with `Ctrl+Shift+P` (`Cmd+Shift+P` on Mac). You can type things like "dark", "disable JavaScript", "coverage", "screenshot" or "show rendering" instead of looking for them in menus. If you delete the `>` at the start, it turns into the file search that `Ctrl+P` opens.

### 49: How do you change where DevTools is docked?

Click the three-dot menu in the top-right of DevTools and choose a **Dock side**: undocked (separate window), left, bottom or right. `Ctrl+Shift+D` (`Cmd+Shift+D` on Mac) switches back to the last dock position. An undocked window is useful on a second monitor or when you need the full page width.

### 50: How do you switch DevTools to a dark theme?

Open Settings (`F1` or the gear icon), go to **Preferences > Appearance**, and set **Theme** to **Dark**, **Light** or **System preference**. You can also type "dark" in the Command Menu and choose **Switch to dark theme**.

### 51: What is `$0` in the Console?

`$0` is a reference to the element currently selected in the Elements panel. `$1` is the one selected before it, and so on up to `$4`. So you can click an element in the DOM tree and then type `$0.textContent` or `$0.getBoundingClientRect()` in the Console without writing a selector.

### 52: What do `$()` and `$$()` do in the Console?

They are shortcuts that only work in the DevTools Console. `$(selector)` is the same as `document.querySelector(selector)` and returns the first match. `$$(selector)` returns all matches as a real array, not a `NodeList`, so you can call `map` and `filter` on it directly.

```js
$$("a").map((a) => a.href);
$("#login-form");
```

If the page itself defines a `$` (for example jQuery), the page's version wins.

### 53: What is `$_` in the Console?

`$_` holds the result of the last expression you ran in the Console. If you run `$$('img').length` and then want to use that number, type `$_`. It saves you from retyping or storing every result in a variable.

### 54: What does `copy()` do in the Console?

`copy(value)` puts a string version of the value on your clipboard. For objects and arrays it copies formatted JSON. It is handy for getting data out of a page, like an API response stored in a variable or the HTML of an element.

```js
copy($0.outerHTML);
copy(JSON.parse(localStorage.getItem("settings")));
```

### 55: What does `console.dir` do and how is it different from `console.log`?

For DOM elements, `console.log` prints the element as HTML that you can expand like in the Elements panel. `console.dir` prints it as a JavaScript object, showing its properties like `className`, `dataset` and `style`. For plain objects the two look almost the same.

### 56: How do you show an object as JavaScript properties instead of HTML in the Console?

Use `console.dir(element)` or the Console utility `dir(element)`. You can also right-click an element in the Console output or in the Elements panel and use **Store as global variable**, then expand it. The Properties tab in the Elements panel also shows the selected node's JavaScript properties.

### 57: What does "Store as global variable" do?

Right-click any object in the Console output, or a node in the Elements panel, and choose **Store as global variable**. DevTools saves it as `temp1`, `temp2` and so on. Then you can work with it in the Console. It is useful for big API responses or objects that you only see in a log message.

### 58: How do you use `console.group`?

`console.group(label)` starts an indented, collapsible group in the Console, and `console.groupEnd()` closes it. Every log between them goes inside the group. `console.groupCollapsed()` starts the group closed. Groups help when one action logs many lines.

```js
console.group("Checkout");
console.log("Items:", cart.items.length);
console.log("Total:", cart.total);
console.groupEnd();
```

### 59: How do you measure how long some code takes with the Console?

Use `console.time(label)` before the code and `console.timeEnd(label)` after it. The Console prints the elapsed time in milliseconds. `console.timeLog(label)` prints the time so far without stopping the timer.

```js
console.time("load users");
const users = await fetch("/api/users").then((r) => r.json());
console.timeEnd("load users"); // load users: 182.4 ms
```

### 60: What does `console.count` do?

`console.count(label)` prints how many times it has been called with that label, like `click: 3`. It is a quick way to check how often a function runs, for example to spot an effect running too many times. `console.countReset(label)` sets the counter back to zero.

### 61: What does `console.assert` do?

`console.assert(condition, ...data)` logs an error only when the condition is false. If the condition is true, nothing is printed. It does not throw and does not stop the code.

```js
console.assert(items.length > 0, "Cart is empty", items);
```

### 62: What does `console.trace` do?

It prints a stack trace at the point where it is called, so you can see which chain of calls reached that line. This is useful when a function is called from many places and you want to know who called it this time.

### 63: How do you style text in `console.log`?

Put `%c` in the message and pass a CSS string as the next argument. The styles apply to the text after `%c`.

```js
console.log(
  "%cWarning:%c check your input",
  "color: red; font-weight: bold",
  "",
);
```

Other format specifiers are `%s` (string), `%d` or `%i` (integer), `%f` (float), `%o` (expandable object) and `%O` (object shown as JavaScript object).

### 64: Can you use `await` directly in the Console?

Yes. The Console supports top-level `await`, so you can write `await fetch('/api/me').then(r => r.json())` and see the result without wrapping it in an async function. This only works in the Console, not in normal non-module scripts.

### 65: What is a Live Expression?

A Live Expression is an expression that the Console keeps evaluating and showing at the top, updating about every quarter of a second. Click the eye icon in the Console toolbar and type something like `document.activeElement` or `window.scrollY`. It is very useful for watching values that change while you interact with the page, like which element has focus.

### 66: What is eager evaluation in the Console?

While you type an expression, the Console shows its result in gray under the input before you press `Enter`. DevTools only does this for code with no side effects, so it will preview `[1, 2, 3].map(x => x * 2)` but not `localStorage.clear()`. You can turn it off in the Console settings.

### 67: How do you run JavaScript in a specific iframe from the Console?

Use the context dropdown in the Console toolbar, which usually says **top**. It lists every frame, worker and extension context on the page. Choose the iframe, and everything you type runs in that frame's `window`. This also works for service workers and web workers.

### 68: How do you see JavaScript errors from a page?

Open the Console. Uncaught errors and unhandled promise rejections appear in red with a message and a link to the file and line. Click the link to open the code in the Sources panel, and expand the error to see its stack trace. Network failures and some browser warnings also show up there.

### 69: What does the link next to a Console message do?

The link on the right side of each message (like `app.js:42`) shows where the message came from. Clicking it opens that file at that line in the Sources panel. If the page has source maps, the link points to your original source file instead of the bundled one.

### 70: What is pretty printing in the Sources panel?

Production JavaScript and CSS are often minified into one long line. Clicking the `{}` button at the bottom of the editor formats the file with line breaks and indentation, so you can read it and set breakpoints on separate statements. DevTools now usually offers to pretty print minified files automatically.

### 71: How do you search across all loaded files?

Open the Search panel with `Ctrl+Shift+F` (`Cmd+Option+F` on Mac). It searches the content of every file the page loaded, including scripts, stylesheets and HTML. You can turn on case sensitivity and regular expressions. Click a result to open the file at that line.

### 72: What are Snippets?

Snippets are small scripts you save in DevTools and can run on any page. Go to **Sources > Snippets**, click **New snippet**, write code and press `Ctrl+Enter` (`Cmd+Enter` on Mac) to run it. They are good for things you do often, like clearing app state or printing all images without `alt` text. You can also run a snippet from the Command Menu by typing `!` followed by its name.

### 73: How do you disable JavaScript for a page?

Open the Command Menu, type "disable JavaScript" and press `Enter`, then reload. The page loads without running scripts. This shows you what users or crawlers see without JavaScript, and helps check server-rendered content and progressive enhancement. The setting only lasts while DevTools is open.

### 74: How do you reload the page while emptying the cache?

With DevTools open, right-click (or long-press) the browser's reload button. A menu appears with **Normal reload**, **Hard reload** and **Empty cache and hard reload**. The last one clears the cache for the site and reloads, which is the most reliable way to make sure you get fresh files.

### 75: What is the drawer in DevTools?

The drawer is a second area at the bottom of DevTools, opened with `Esc` or from the three-dot menu > **More tools**. It can hold the Console, Rendering, Network conditions, Coverage, Animations, Sensors, Search, Changes and other tools. It lets you use two tools at once, like the Network panel on top and the Console below.

### 76: How do you open a panel that is not visible in the main toolbar?

Click the `>>` arrow at the end of the panel tabs, use the three-dot menu > **More tools**, or open the Command Menu and type "Show" followed by the panel name, for example "Show Coverage" or "Show Animations". You can drag panel tabs to reorder them, or move them between the main area and the drawer.

### 77: How do you change DevTools settings?

Press `F1` while DevTools is focused, or click the gear icon. Settings has sections like **Preferences**, **Workspace**, **AI innovations**, **Experiments**, **Ignore list**, **Devices**, **Throttling**, **Locations** and **Shortcuts**. To reset everything, use **Restore defaults and reload** at the bottom of Preferences.

### 78: What is the size shown in the Network panel's Size column?

The column has two numbers when you turn on **Big request rows**: the top one is the transfer size (bytes over the network, including headers, after compression), the bottom one is the resource size (the uncompressed body). If the resource came from a cache, the column shows something like `(memory cache)`, `(disk cache)` or `(ServiceWorker)` instead of a size.

### 79: What does the summary bar at the bottom of the Network panel show?

It shows the number of requests, the total transferred size, the total resource size, and timing: **Finish** (when the last request ended), **DOMContentLoaded** and **Load**. If you filter the list, the counts show the filtered numbers out of the total. It gives you a quick sense of how heavy a page is.

### 80: What are the blue and red lines in the Network waterfall?

The blue line marks the `DOMContentLoaded` event, when the HTML has been parsed and deferred scripts have run. The red line marks the `load` event, when all resources like images and stylesheets have finished loading. Requests that start after the red line were made later, for example by lazy loading or scripts.

### 81: What is the Initiator column in the Network panel?

It shows what caused the request: the parser (an HTML tag), a script (with a link to the file and line), a redirect, or something else. Clicking the link takes you to the code that started the request. The **Initiator** tab of a request shows the full chain, which helps when you need to find out why some file is being loaded.

### 82: How do you check the HTTP method and status code of a request?

Click the request and look at the **General** section at the top of the **Headers** tab. It shows the Request URL, Request Method, Status Code, Remote Address and Referrer Policy. You can also add a **Method** column to the request table by right-clicking the column headers.

### 83: How do you add or remove columns in the Network panel?

Right-click any column header in the request table. A menu lists all available columns, like Method, Protocol, Scheme, Domain, Remote Address, Priority, Cookies and Connection ID. You can also add any response header as a column with **Response Headers > Manage header columns**.

### 84: How do you see the query string and the request body?

Click the request and open the **Payload** tab. It shows **Query String Parameters** and the request body as **Form Data** or **Request Payload**. You can switch between a parsed view and **view source** to see the raw text. For GET requests, the body section is normally empty.

### 85: How do you copy a request so you can run it again outside the browser?

Right-click the request and choose **Copy**. Options include **Copy as fetch**, **Copy as fetch (Node.js)**, **Copy as cURL**, **Copy as PowerShell**, **Copy URL** and **Copy response**. You can paste the cURL command in a terminal or the fetch code in the Console to repeat the exact request with the same headers.

### 86: How do you repeat a fetch or XHR request without reloading the page?

Right-click the request in the Network panel and choose **Replay XHR**. It works for fetch and XHR requests and sends the same request again with the same headers and body. For other requests or to change something first, use **Copy as fetch**, edit the code and run it in the Console.

### 87: What is the Rendering tab?

It is a drawer tool with options that help you see and test rendering. You can turn on **Paint flashing** to highlight areas that are repainted, **Layout shift regions** to see shifts, **Layer borders**, and **Frame rendering stats**. It can also emulate CSS media features like `prefers-color-scheme: dark` or `prefers-reduced-motion`, emulate print styles, and emulate vision problems. Open it from **More tools > Rendering**.

### 88: How do you test dark mode on a site without changing your OS setting?

Open **Rendering** in the drawer and set **Emulate CSS media feature prefers-color-scheme** to `dark`. The page now matches `@media (prefers-color-scheme: dark)`. You can also open the Command Menu and type "Emulate CSS prefers-color-scheme: dark", or use the brush icon in the Styles pane toolbar.

### 89: How do you see the print version of a page?

In **Rendering**, set **Emulate CSS media type** to `print`. The page now applies your `@media print` styles, and you can inspect and edit them in the Elements panel like normal styles. This is much faster than opening print preview again and again.

### 90: What is the Sensors tool?

The Sensors drawer tool lets you fake device data. You can set a geolocation (with presets for cities, or custom latitude and longitude), the timezone and locale, device orientation, touch input, and the idle state. Open it with **More tools > Sensors** or by typing "sensors" in the Command Menu.

### 91: How do you fake your geolocation in DevTools?

Open **Sensors**, and under **Location** pick a preset like **London** or **Tokyo**, or choose **Other** and enter latitude and longitude. Pages that call `navigator.geolocation.getCurrentPosition()` will get those values. You can also pick **Location unavailable** to test how your app handles the error.

### 92: What is the Issues panel?

The Issues panel collects problems that Chrome finds on the page, grouped by type, with a short explanation and links to docs. Examples are cookie problems (like a missing `SameSite` or `Secure` flag), mixed content, CORS errors, Content Security Policy violations, deprecated features and some accessibility issues. Open it from the Console toolbar's issues counter or from **More tools > Issues**.

### 93: How do you check an element's color contrast in DevTools?

Hover over the element in inspect mode; the tooltip shows the contrast ratio with a check mark or warning icon. In the Styles pane, click the color swatch next to a `color` value to open the color picker, which shows the ratio and lines for the AA and AAA levels. Lighthouse's Accessibility audit also lists elements with low contrast.

### 94: How do you use the color picker in the Styles pane?

Click the small colored square next to any color value. The picker lets you choose a color, change the opacity, switch formats (hex, rgb, hsl, hwb, lch, oklch and others), pick colors from palettes, and use the eyedropper to grab a color from anywhere on the page. `Shift`-click on the swatch switches the value between formats without opening the picker.

### 95: What does a line through a CSS declaration in the Styles pane mean?

It means the declaration is overridden. Another rule with higher specificity, a later rule with the same specificity, an inline style or `!important` set a different value for the same property. If the line through is shown with a yellow warning icon instead, the declaration is invalid, for example a typo in the property name or a value that property doesn't accept.

### 96: What does a grayed-out CSS declaration with an info icon mean?

It means the declaration is valid but has no effect here because of other styles. For example, `justify-content` on an element that isn't a flex or grid container, or `width` on an inline element. Hovering the info icon explains why and often suggests a fix. This is called the inactive CSS hint.

### 97: How do you find which file and line a CSS rule comes from?

Each rule in the Styles pane has a link on the right with the file name and line, like `main.css:84`. Clicking it opens the file in the Sources panel. If the site uses CSS source maps, the link points to your original Sass or Less file. Rules from the browser are labeled `user agent stylesheet`.

### 98: What is the `user agent stylesheet`?

It is the browser's built-in default CSS, for example the margins on `body` and `h1`, or the styles for buttons and form fields. These rules show up in the Styles pane with that label so you know they are not from your code. Your styles override them, which is what CSS resets and normalize files do.

### 99: How do you see the event listeners attached to an element?

Select the element and open the **Event Listeners** tab in the Elements panel. It lists every event type with the handler function and the file it comes from. **Ancestors** shows listeners on parent elements too, since events bubble. You can also call `getEventListeners($0)` in the Console.

### 100: How do you find an element in the DOM tree by text or selector?

Click in the Elements panel and press `Ctrl+F` (`Cmd+F` on Mac). The search box accepts plain text, a CSS selector like `.card > h2`, or an XPath expression like `//button[@type="submit"]`. It highlights each match, and `Enter` moves to the next one.

### 101: How do you copy a CSS selector or XPath for an element?

Right-click the node in the Elements panel and go to **Copy**. You can choose **Copy selector**, **Copy JS path** (a `document.querySelector(...)` call), **Copy styles**, **Copy XPath**, **Copy full XPath**, **Copy element** or **Copy outerHTML**. The generated selectors are often long and fragile, so for tests it is better to write your own based on roles, labels or test IDs.

### 102: How do you scroll the page to an element you selected in the DOM tree?

Right-click the node and choose **Scroll into view**. The page scrolls until the element is visible. This helps when the element is far down the page or inside a scrolling container.

### 103: How does DevTools show Shadow DOM?

Elements with a shadow root show a `#shadow-root (open)` node in the DOM tree that you can expand like any other node. You can inspect and edit the styles of elements inside it. Built-in browser controls like `<input type="range">` or `<video>` also use shadow DOM, but it is hidden by default. Turn on **Show user agent shadow DOM** in Settings > Preferences > Elements to see it.

### 104: How do you see the `::before` and `::after` pseudo-elements of an element?

If an element has `::before` or `::after` with `content`, DevTools shows them as child nodes named `::before` and `::after` in the DOM tree. Select one to see and edit its styles in the Styles pane. Rules for pseudo-elements also appear in the Styles pane of the parent element under a **Pseudo ::before element** heading.

### 105: What is the Layout tab in the Elements panel?

The Layout tab lists every CSS Grid and Flexbox container on the page, with checkboxes to show an overlay for each one. Overlays draw the grid lines, track sizes, gaps and area names on the page. You can choose the overlay color and options like showing line numbers or line names.

### 106: What are the `grid` and `flex` badges in the DOM tree?

DevTools adds small badges next to elements in the DOM tree to show what they are. `grid` means a grid container, `flex` a flex container, `subgrid`, `container` (a container query container), `scroll-snap`, `slot`, `top-layer` and others. Clicking the `grid` or `flex` badge turns its overlay on or off.

### 107: What is the Accessibility pane in the Elements panel?

It shows accessibility information for the selected element: its position in the accessibility tree, its ARIA attributes, and its computed properties like role, name and description, plus where the name came from (`aria-label`, a `<label>`, text content, and so on). This shows you what a screen reader will announce for the element.

### 108: How do you see the full accessibility tree of a page?

In the Elements panel, open the Accessibility pane and turn on **Enable full-page accessibility tree**. After a reload, a button appears in the top-right of the Elements panel that switches the DOM tree to the accessibility tree. You see roles and names instead of tags, which helps find unlabeled buttons or wrong headings.

### 109: What is the Memory panel?

The Memory panel helps you understand how much memory a page uses and find memory leaks. It has profile types like **Heap snapshot**, **Allocations on timeline**, **Allocation sampling** and **Detached elements**. A heap snapshot shows every JavaScript object and DOM node in memory and what is keeping each one alive.

### 110: What is a memory leak in a web page?

A memory leak happens when the page keeps objects in memory that it no longer needs, so memory keeps growing the longer you use the page. Common causes in front-end code are event listeners that are never removed, timers that keep running, caches that only grow, and DOM nodes removed from the page but still referenced from JavaScript. Over time the page gets slow or crashes.

### 111: What is the Performance panel?

The Performance panel records what the browser does while a page loads or while you interact with it: JavaScript running, style calculation, layout, painting, network requests and more. After recording, it shows a timeline with tracks, a flame chart of function calls, and insights about slow parts. It also shows live Core Web Vitals when you first open it.

### 112: What does the Performance panel show before you record anything?

It shows a live metrics view with the Core Web Vitals for the current page on your machine: Largest Contentful Paint (LCP), Cumulative Layout Shift (CLS) and Interaction to Next Paint (INP). The values update as you use the page, and there is a list of recent interactions and layout shifts. If you turn on field data, it also shows real-user values from the Chrome UX Report next to your local values.

### 113: What are Core Web Vitals?

Core Web Vitals are three metrics Google uses to measure user experience:

- **LCP (Largest Contentful Paint)**: how long until the biggest image or text block is shown. Good is 2.5 seconds or less.
- **INP (Interaction to Next Paint)**: how quickly the page responds to clicks, taps and key presses. Good is 200 ms or less.
- **CLS (Cumulative Layout Shift)**: how much the content jumps around while loading. Good is 0.1 or less.

DevTools shows all three in the Performance panel.

### 114: How do you record a performance profile of page load?

Open the Performance panel and click **Record and reload** (the circular arrow, or `Ctrl+Shift+E` / `Cmd+Shift+E`). DevTools reloads the page, records until it finishes loading, then stops and shows the result. Throttling the CPU and network first gives results closer to a real mobile user.

### 115: How do you record a performance profile of an interaction, like clicking a button?

Open the Performance panel, click **Record** (`Ctrl+E` / `Cmd+E`), do the interaction on the page, and click **Stop**. Keep the recording short and focused on the thing you want to measure. A long recording is harder to read and takes more memory.

### 116: What is CPU throttling in the Performance panel?

CPU throttling makes Chrome run slower on purpose, like 4x or 6x slower, to simulate a cheaper phone. Developer laptops are much faster than most users' devices, so code that feels instant for you can be slow for them. You set it in the Performance panel's capture settings (the gear icon) or in the live metrics environment settings.

### 117: What is a long task?

A long task is any task on the main thread that takes more than 50 ms. While it runs, the browser can't respond to user input, so the page feels stuck. In the Performance panel, long tasks have a red triangle in the corner and the part over 50 ms is shaded with red stripes.

### 118: What is the Lighthouse Performance score based on?

It is a weighted score from 0 to 100 built from lab metrics measured during the test: First Contentful Paint, Largest Contentful Paint, Total Blocking Time, Cumulative Layout Shift and Speed Index. Under the score, Lighthouse lists insights and diagnostics with the estimated savings for each suggestion. The score can change between runs, so look at the trend over a few runs.

### 119: Why should you run Lighthouse in an Incognito window?

Browser extensions inject scripts and styles into pages, and they can slow down the page or change the results. Incognito windows run without most extensions by default, and they also start with an empty cache and no stored data. This gives cleaner and more repeatable results.

### 120: What is the Recorder panel?

The Recorder lets you record a user flow, like going to a page, filling a form and clicking submit, and then replay it. You can edit the steps, slow down the replay, measure performance of the flow, and export it as a Puppeteer script, a Lighthouse user flow script or JSON. Open it with **More tools > Recorder**.

### 121: What is the Coverage tool?

Coverage shows how much of each JavaScript and CSS file was actually used while you were on the page. Open it from **More tools > Coverage**, click record and reload, and you get a list of files with total bytes and unused bytes. Clicking a file opens it in Sources with a colored bar next to each line, where red means the code never ran. It helps you find code to remove or load later.

### 122: What is the Changes tool?

The Changes drawer tool shows a diff of the edits you made in DevTools to CSS and source files during the session. This helps when you tweak many styles in the Styles pane and then want to copy all changes into your real code. Open it from **More tools > Changes**. It has a button to copy all CSS changes.

### 123: What is the Performance monitor?

It is a drawer tool that shows live graphs of performance data while you use the page: CPU usage, JS heap size, DOM nodes, JS event listeners, documents, frames, layouts per second and style recalculations per second. Open it with **More tools > Performance monitor**. A number that only goes up, like DOM nodes or listeners, is a hint of a leak.

### 124: What is the Animations panel?

It records CSS animations, CSS transitions and Web Animations on the page and shows them on a timeline. You can replay them, slow them down to 25% or 10% speed, scrub through them, and change their delay and duration by dragging. Open it with **More tools > Animations**.

### 125: What are source maps?

Source maps are files that map bundled, minified code back to your original source files. If your app is written in TypeScript and bundled with Vite or webpack, the source map lets DevTools show the original `.ts` files in the Sources panel, set breakpoints in them, and show original file names and lines in stack traces. A built file points to its map with a comment like `//# sourceMappingURL=app.js.map`.

### 126: Where do you see original source files when source maps are loaded?

In the Sources panel's **Page** tab, original files appear in the file tree, usually grouped under the dev server's URL or a folder like `webpack://` or `src`. You can open them with `Ctrl+P` too. The bundled files are still there, but breakpoints, Console links and stack traces use the original files.

### 127: What is a conditional breakpoint?

A conditional breakpoint only pauses when an expression is true. Right-click a line number in Sources, pick **Add conditional breakpoint** and type a condition like `user.id === 42`. It is very useful in loops or functions called many times, when you only care about one specific case.

### 128: What is a logpoint?

A logpoint is a breakpoint that logs a message to the Console instead of pausing. Right-click a line number, choose **Add logpoint**, and type an expression like `'order', order.id, order.total`. You get the benefit of `console.log` without editing and reloading your code.

### 129: How do you remove or disable all breakpoints at once?

In the **Breakpoints** pane in Sources, right-click and choose **Remove all breakpoints** or **Deactivate breakpoints**. The **Deactivate breakpoints** button in the debugger toolbar (`Ctrl+F8` / `Cmd+F8`) turns off pausing without deleting them, so you can turn them back on later.

### 130: Do breakpoints stay after you reload the page?

Yes. DevTools saves breakpoints for each file and puts them back after a reload or when you come back later. If the file changes a lot, a breakpoint may end up on a different line than you expected. You can see all breakpoints in the **Breakpoints** pane.

### 131: How do you view Session Storage in DevTools?

Go to **Application > Storage > Session storage** and select the origin. It works like the Local Storage view: you can add, edit and delete keys. Remember that session storage is separate for each tab and is cleared when the tab is closed.

### 132: How do you view IndexedDB data?

Go to **Application > Storage > IndexedDB**, expand the database and click an object store. You see the records with their keys and values, and you can expand objects, filter by key, delete records or refresh the view. You can also delete the whole database from there.

### 133: What is Cache Storage in the Application panel?

Cache Storage is the storage used by the Cache API, mostly by service workers to keep files for offline use. In **Application > Storage > Cache storage** you can see each named cache, the requests stored in it, their response headers and the response body. You can delete entries or whole caches.

### 134: How do you clear all data for a site?

Go to **Application > Storage** (the **Storage** item at the top of that section). It shows how much space the site uses and has a **Clear site data** button. You can choose what to clear: cookies, storage (local, session, IndexedDB, cache storage), service workers and so on. This resets the site to a first-visit state.

### 135: What is a service worker and where do you see it in DevTools?

A service worker is a script that runs in the background, separate from the page. It can intercept network requests, cache files for offline use and receive push messages. In **Application > Service workers** you can see the registered worker, its status, its source file, and buttons to update, unregister, or send test push and sync events.

### 136: What does the Manifest section in the Application panel show?

It shows the parsed web app manifest: name, short name, start URL, theme and background colors, display mode, icons, shortcuts and more. It also lists errors and warnings, such as missing icons, and installability problems that stop the app from being installed as a PWA.

### 137: How do you change the user agent string in DevTools?

Open **More tools > Network conditions**. Under **User agent**, uncheck **Use browser default** and pick a preset or type a custom string. You can also set the user agent client hints values. Device Mode changes the user agent automatically when you pick a device preset.

### 138: How do you see which media queries a page uses?

In Device Mode, open the three-dot menu in the device toolbar and choose **Show media queries**. Colored bars appear above the viewport, one for each breakpoint in the CSS. Clicking a bar resizes the viewport to that width, and right-clicking lets you jump to the rule in the source.

### 139: How do you change the device pixel ratio in Device Mode?

In the device toolbar, choose a value in the **DPR** dropdown (it may be hidden; enable it from the toolbar's three-dot menu). This changes `window.devicePixelRatio` and which `srcset` image or `image-set()` the browser picks. It is useful for checking that your high-resolution images load correctly.

### 140: Can you debug a website running on an Android phone with DevTools?

Yes. Turn on Developer options and USB debugging on the phone, connect it to your computer with a USB cable, and open `chrome://inspect#devices` in desktop Chrome. Pages open in Chrome on the phone appear in the list, and clicking **inspect** opens full DevTools for that page, with a screencast of the phone screen.

### 141: Can you debug Safari on iPhone with Chrome DevTools?

No. Chrome DevTools works with Chromium-based browsers. To debug a page on an iPhone or iPad, you use Safari's Web Inspector on a Mac with the device connected (or a simulator). Chrome on iOS uses Apple's WebKit engine too, so its pages are also debugged with Safari Web Inspector.

### 142: Can you use Chrome DevTools to debug Node.js?

Yes. Start Node with the `--inspect` flag, then open `chrome://inspect` in Chrome and click **inspect** under your process, or click **Open dedicated DevTools for Node**. You get the Console, Sources with breakpoints, Memory and Performance tools for your Node code.

```bash
node --inspect server.js
# or pause on the first line:
node --inspect-brk server.js
```

### 143: What are DevTools extensions?

They are Chrome extensions that add new panels or features to DevTools. Common examples are React Developer Tools, Angular DevTools, Vue.js devtools and Redux DevTools. They show framework-specific information, like the component tree, props, state and store actions, which the built-in panels don't know about.

### 144: What does React Developer Tools add to DevTools?

It adds two panels: **Components** and **Profiler**. Components shows the React component tree with props, state and hooks for the selected component, and you can edit them live. Profiler records renders and shows which components rendered, how long they took and why they rendered.

### 145: What is AI assistance in Chrome DevTools?

It is a Gemini-based chat panel inside DevTools. You can ask questions about the selected element and its styles, a network request, a source file, or a performance trace, and it answers using data from the page. There are also related features like **Understand this error** in the Console and code generation in the Console and Sources panels. It must be turned on in **Settings > AI innovations** and needs a signed-in Google account in a supported region.

### 146: What does "Understand this error" do in the Console?

When you hover over an error or warning in the Console, a button appears that sends the message, its stack trace and related code to Gemini. You get a short explanation of what the error means and ideas for fixing it. It is a starting point; you still need to check the answer against your code.

### 147: How do you undo changes made in DevTools?

In the Elements panel and Styles pane, `Ctrl+Z` (`Cmd+Z` on Mac) undoes recent edits. Reloading the page throws away every DevTools change that was not saved to disk. If you edited many styles and want to keep some of them, check the Changes tool first to copy them.

### 148: How do you open DevTools for a pop-up window or a new tab automatically?

In Settings > Preferences, turn on **Auto-open DevTools for popups**. Then any window opened by the page with `window.open()` or a link with `target="_blank"` gets DevTools opened automatically. This helps when you need to catch requests or errors that happen right after the new window loads.

### 149: How do you find the keyboard shortcuts for DevTools?

Open Settings and go to **Shortcuts**. It lists every shortcut, and you can change them or switch the preset to match Visual Studio Code. You can also type "shortcuts" in the Command Menu. Pressing `?` while DevTools is focused also opens Settings.

### 150: Why do you sometimes see "Paused in debugger" on the page?

The page is stopped at a breakpoint, a `debugger` statement, or an exception (if **Pause on exceptions** is turned on). The page doesn't respond until you resume with `F8` or the play button in the overlay. If it keeps happening and you didn't set a breakpoint, check for `debugger` statements, event listener breakpoints or DOM breakpoints you forgot about, or deactivate breakpoints with `Ctrl+F8`.

## Moderate Questions (151-300)

### 151: What types of breakpoints does DevTools support?

- **Line-of-code** breakpoints, plus **conditional** breakpoints and **logpoints**.
- **DOM change** breakpoints: subtree modification, attribute modification, node removal.
- **XHR/fetch** breakpoints: pause when a request URL contains some text.
- **Event listener** breakpoints: pause when an event like `click` or `keydown` fires.
- **Exception** breakpoints: pause on uncaught or caught exceptions.
- **Function** breakpoints: pause when a function is called, using `debug(fn)`.
- **CSP violation** and **Trusted Type violation** breakpoints.

Knowing which one to use saves a lot of time compared to adding line breakpoints everywhere.

### 152: How do you find out which code changes a DOM element?

Right-click the element in the Elements panel and choose **Break on**, then **subtree modifications**, **attribute modifications** or **node removal**. The next time JavaScript makes that change, the debugger pauses on the line that did it, and the Call Stack shows how it got there. This is the fastest way to find out which script keeps adding a class or removing a node.

### 153: How do you pause when a specific fetch or XHR request is sent?

In the Sources panel, open the **XHR/fetch Breakpoints** pane, click **+** and type part of the URL, like `/api/orders`. The debugger pauses right before any request whose URL contains that text is sent, and the call stack shows which code started it. Leaving the text empty pauses on every fetch and XHR.

### 154: What are event listener breakpoints?

In the Sources panel, the **Event Listener Breakpoints** pane lists event categories like Mouse, Keyboard, Timer, Control, Animation and Script. Check one, like **Mouse > click** or **Timer > setTimeout fired**, and the debugger pauses as soon as a handler for that event runs. It is useful when you don't know which code handles an event.

### 155: How do you pause on the very first line of any script that runs?

In the **Event Listener Breakpoints** pane, expand **Script** and check **Script First Statement**. The debugger pauses at the first statement of every script that runs, including inline scripts and scripts added later. This helps when some code runs right at load time and finishes before you can set a normal breakpoint.

### 156: How do you pause when an exception is thrown?

In the Breakpoints pane of the Sources panel, check **Pause on uncaught exceptions**. Add **Pause on caught exceptions** if you also want to stop on errors that are caught by `try...catch` or a promise `.catch()`. The second option can be noisy, because many libraries throw and catch errors on purpose.

### 157: How do you set a breakpoint on a function without knowing where it is defined?

Call `debug(functionName)` in the Console. The next time that function runs, DevTools pauses on its first line. `undebug(functionName)` removes it. This works for any function you can reach from the Console, like `debug(window.myApp.saveForm)`.

### 158: What does `monitor()` do in the Console?

`monitor(fn)` logs a message to the Console each time the function is called, with the function name and the arguments it got. It does not pause. `unmonitor(fn)` stops it. It is a quick way to see how often something runs and with what values, without editing code.

### 159: What does `monitorEvents()` do?

`monitorEvents(element, types)` logs the events fired on an element to the Console. You can pass a single event, an array, or a group like `'mouse'` or `'key'`. `unmonitorEvents(element)` stops it.

```js
monitorEvents(window, "resize");
monitorEvents($0, ["focus", "blur"]);
monitorEvents(document.body, "key");
```

### 160: What does `getEventListeners()` return?

`getEventListeners(target)` returns an object where each key is an event type and the value is an array of listeners, with `listener`, `useCapture`, `passive`, `once` and `type`. It only works in the DevTools Console, not in page code.

```js
getEventListeners(window).scroll;
getEventListeners($0).click[0].listener;
```

### 161: What does `queryObjects()` do?

`queryObjects(Constructor)` prints all objects in memory that were created with that constructor, like `queryObjects(Promise)` or `queryObjects(MyComponent)`. It is useful for checking whether old instances are still around after they should have been cleaned up. DevTools runs a garbage collection first, so only live objects are listed.

### 162: What does `inspect()` do in the Console?

`inspect(value)` opens the right panel for the value. For a DOM element it selects the node in the Elements panel. For a function it opens the Sources panel at the function's definition. It saves time when you have a reference in the Console and want to see where it lives.

### 163: What are async stack traces?

When code runs in a callback after `await`, `setTimeout`, a promise or an event, the normal stack only shows the callback. DevTools records where the async work was scheduled and shows that part of the stack too, separated by labels like `await` or `setTimeout`. This is turned on by default and makes debugging async code much easier.

### 164: What does "Restart frame" do?

When paused, right-click a frame in the Call Stack and choose **Restart frame**. Execution goes back to the start of that function, so you can step through it again. Side effects that already happened, like changes to variables outside the function or network requests, are not undone, so use it with care.

### 165: What does "Continue to here" do?

While paused, right-click a line number and choose **Continue to here**. Execution runs until it reaches that line, then pauses, without you having to set and remove a breakpoint. It is quicker than stepping over many lines one by one.

### 166: What does "Never pause here" do?

Right-click a line number and choose **Never pause here**. DevTools adds a conditional breakpoint with the condition `false`, so a `debugger` statement or an exception on that line will not pause anymore. It helps when one line keeps stopping you and you can't change the code.

### 167: How do you change a variable's value while paused?

In the Scope pane, double-click the value and type a new one. You can also run an assignment in the Console, like `discount = 0.5`, because the Console runs in the paused frame's scope. When you resume, the code continues with the new value. This lets you test a fix without reloading.

### 168: What is the ignore list in DevTools?

The ignore list tells the debugger to skip certain scripts, like framework or `node_modules` code. When a script is ignored, stepping skips over it, the debugger doesn't pause in it on exceptions, and its frames are hidden from the Call Stack and Console stack traces. You can add a script by right-clicking it and choosing **Add script to ignore list**, or add patterns in **Settings > Ignore list**.

### 169: What does "Automatically add known third-party scripts to ignore list" mean?

Bundlers like Vite, webpack and Angular CLI can add an `x_google_ignoreList` field to their source maps that marks which original sources are third-party, usually everything from `node_modules`. When this setting is on, DevTools ignores those files automatically. The result is cleaner stack traces that only show your own code.

### 170: How do you edit JavaScript in DevTools and see the change without reloading?

Open the file in the Sources panel, edit it and press `Ctrl+S` (`Cmd+S` on Mac). V8 replaces the function code in the running page (live edit). New calls to the edited functions use the new code. There are limits: code that already ran is not run again, and some changes, like editing a function that is currently on the stack below the top frame, may not apply. The change is lost on reload unless you use Workspaces or Overrides.

### 171: What are Workspaces in DevTools?

Workspaces connect files served by your dev server to the matching files on your disk. After you set it up, edits you make in the Sources panel, and CSS changes made in the Styles pane, are saved to your real source files. You add a folder in **Sources > Workspace**, and DevTools maps network files to local files by matching names and paths.

### 172: What are automatic workspace folders?

It is a newer way to connect a workspace without picking a folder by hand. The dev server serves a JSON file at `/.well-known/appspecific/com.chrome.devtools.json` with the project's root path and a UUID. DevTools reads it and offers to connect the folder. Some tools, like a Vite plugin, can generate this file for you. It only works for pages on `localhost`.

```json
{
  "workspace": {
    "root": "/Users/me/projects/shop",
    "uuid": "53b029bb-c989-4dca-969b-835fecec3717"
  }
}
```

### 173: What are Local Overrides?

Local Overrides let you replace the response of any request with a file stored on your computer, and DevTools keeps using it across reloads. You can change the HTML, JS or CSS of a site you don't control, like a production page, and see the effect. You set them up in **Sources > Overrides** by choosing a folder, then right-click a request in the Network panel and choose **Override content**.

### 174: How can you override response headers in DevTools?

Right-click a request in the Network panel and choose **Override headers**, or click the pencil next to **Response Headers** in the Headers tab. You can add, change or remove headers, for example to test a new CORS or CSP header without changing the server. DevTools saves them in a `.headers` file in your overrides folder, and you can use wildcards there to apply them to many URLs.

### 175: How can you test a production bug fix without deploying?

Use Local Overrides. Turn on overrides, open the production JavaScript file in Sources (pretty print it if needed), make your change and save. DevTools serves your edited file on every reload, so you can check whether the fix works on real data. If the site uses source maps, you still have to override the built file, not the original source.

### 176: How do you load a source map that is not linked from the file?

Open the bundled file in the Sources panel, right-click inside the editor and choose **Add source map...**, then enter the URL of the `.map` file. This is useful when production builds don't include the `sourceMappingURL` comment but you have the maps stored privately, for example on an internal server.

### 177: Why might source maps not load, and how do you check?

Common reasons are a wrong `sourceMappingURL`, the map file returning `404` or being blocked by CORS, the map not being deployed, or source maps turned off in **Settings > Preferences > Sources**. Open **More tools > Developer resources** to see every source map DevTools tried to load, with its status and any error. The Console may also show a warning about a failed source map.

### 178: How do you block a request to see how the page behaves without it?

Right-click the request in the Network panel and choose **Block request URL** or **Block request domain**. This opens the **Network request blocking** drawer with the pattern added. Blocked requests fail with `(blocked:devtools)`. It is useful for checking what happens when a third-party script, a font or an API is unavailable.

### 179: What do the phases in a request's Timing tab mean?

- **Queueing**: the request waits because of priority or because there is no free connection.
- **Stalled**: time spent waiting before it can be sent, for any of the reasons above or others.
- **DNS Lookup**: resolving the host name.
- **Initial connection** and **SSL**: TCP and TLS handshakes.
- **Request sent**: sending the request.
- **Waiting for server response**: time to first byte (TTFB).
- **Content Download**: receiving the response body.

Long TTFB points to the server or backend; long download points to large files or slow network.

### 180: What is TTFB and where do you see it in DevTools?

TTFB (time to first byte) is the time from sending the request until the first byte of the response arrives. It includes network latency and the time the server needs to generate the response. In DevTools it's shown as **Waiting for server response** in the request's **Timing** tab. A high TTFB on the main document delays everything else.

### 181: How do you see Server-Timing values in DevTools?

If your server sends a `Server-Timing` header, the request's **Timing** tab shows a **Server Timing** section with each metric and its duration. This lets you see how much of the TTFB went to, for example, the database or cache, right in the browser.

```http
Server-Timing: db;dur=53.2, cache;desc="Cache read";dur=4.1
```

### 182: How do you find out why a resource was loaded?

Hold `Shift` and hover over a request in the Network panel. Its initiators are highlighted in green and the requests it started are highlighted in red. For the full chain, open the request's **Initiator** tab, which shows the request call stack and the initiator chain, like HTML loading a script that loads a module that calls `fetch`.

### 183: What do the Priority and Protocol columns tell you?

**Priority** shows the browser's priority for the request: Highest, High, Medium, Low or Lowest. It changes based on the type of resource, where it is in the page, and hints like `fetchpriority` and `<link rel="preload">`. **Protocol** shows the HTTP version, like `http/1.1`, `h2` (HTTP/2) or `h3` (HTTP/3). Both columns are hidden by default; right-click the header row to add them.

### 184: How do you see the CORS preflight request in the Network panel?

Preflight requests are `OPTIONS` requests sent before some cross-origin requests. In the Network panel they show up as a separate row with the type `preflight`, usually next to the main request, and the main request's Initiator mentions it. Check the response headers of the preflight (`Access-Control-Allow-Origin`, `-Methods`, `-Headers`) when the browser blocks a request.

### 185: How do you debug a CORS error with DevTools?

The Console shows the CORS error with the reason, like a missing `Access-Control-Allow-Origin` header or a credentials mismatch. The Issues panel explains the problem in more detail. In the Network panel, look at the failed request and its preflight: check the request's `Origin` header and the response's `Access-Control-*` headers. Fixing CORS is done on the server, not in the browser.

### 186: How do you find out why a cookie was not sent with a request?

Open the request in the Network panel and go to the **Cookies** tab. Turn on **show filtered out request cookies**. Cookies that were not sent are highlighted with a tooltip explaining why, for example a `SameSite` restriction, a missing `Secure` flag on HTTP, a domain or path mismatch, or the cookie being blocked by the user's settings. The **Set-Cookie** response cookies show similar warnings when the browser refuses to store them.

### 187: How do you inspect WebSocket messages?

Click the WebSocket request (filter with **WS**) and open the **Messages** tab. It lists every message sent (up arrow) and received (down arrow) with time and length. You can filter messages by text and click one to see its content, formatted if it's JSON. Binary frames are shown in hex or base64.

### 188: How do you inspect Server-Sent Events?

Select the `EventSource` request in the Network panel and open the **EventStream** tab. It shows each event with its ID, type, data and time as they arrive. For SSE implemented with plain `fetch` and a stream reader, there is no EventStream tab, so you have to look at the response or log the chunks yourself.

### 189: What does a `304 Not Modified` response mean in the Network panel?

The browser had a cached copy and sent a conditional request with `If-None-Match` (ETag) or `If-Modified-Since`. The server answered that the file hasn't changed, so the browser used the cached body. The transfer size is small because only headers were sent. If you see many 304s, consider longer `Cache-Control` max-age with hashed file names, so the browser doesn't need to ask at all.

### 190: What is the difference between `(memory cache)` and `(disk cache)` in the Size column?

`(memory cache)` means the resource came from the in-memory cache of the current tab, which is very fast and usually used for things already loaded on this page, like an image used twice or a reload. `(disk cache)` means it came from the HTTP cache on disk, which survives browser restarts. Neither makes a network request.

### 191: How do you check if a request was handled by a service worker?

The Size column shows `(ServiceWorker)` for responses served by the service worker. The service worker's own requests appear with a gear icon. You can filter with `is:service-worker-intercepted` and `is:service-worker-initiated`. The **Timing** tab also shows service worker phases like startup and `respondWith`.

### 192: What are some useful keyword filters in the Network panel?

- `status-code:500` and `-status-code:200`
- `method:POST`
- `domain:*.example.com`
- `mime-type:application/json`
- `larger-than:50k`
- `has-response-header:cache-control`
- `scheme:http` (find insecure requests)
- `is:running` (requests still in progress)
- `set-cookie-domain:example.com`

You can combine filters with spaces, and the text box autocompletes keywords and values.

### 193: How do you create a custom network throttling profile?

Open **Settings > Throttling** and click **Add profile** in the network section. Enter a name, download speed, upload speed and latency. The profile then appears in the throttling dropdown in the Network and Performance panels.

### 194: What is a HAR file, and how do you export one?

A HAR (HTTP Archive) file is a JSON file that contains the requests and responses from the Network panel, with headers, timings and often bodies. Click the download icon in the Network toolbar to export, and the upload icon (or drag and drop) to import one. By default DevTools exports a sanitized HAR without sensitive data like cookies and `Authorization` headers. Exporting with sensitive data has to be turned on in the Network settings.

### 195: Why should you be careful when sharing HAR files?

A HAR file can contain cookies, session tokens, `Authorization` headers, personal data in request and response bodies, and internal URLs. Anyone with the file could use a token to log in as you. Use the sanitized export when possible, check the file before sending it, and share it only with people who need it. Log out afterward if you shared a full one.

### 196: How do you see all requests going to a third-party domain?

Type `domain:` followed by the domain in the Network filter, like `domain:*.google-analytics.com`. To hide them, use `-domain:...`. Newer versions also have a filter option to show only third-party requests. You can add a **Domain** column and sort by it to group requests by origin.

### 197: How do you find which requests block page rendering?

In a Performance recording, the **Render blocking requests** insight lists them, and requests in the Network track that block rendering are marked. In the Network panel, look for stylesheets and synchronous scripts in the `<head>` that load before the first paint. Lighthouse also lists them with estimated savings. Fixes include inlining critical CSS, using `defer` or `async`, and preloading key resources.

### 198: What are the Fetch/XHR, Doc and Other filters useful for?

**Fetch/XHR** shows only API calls made with `fetch` or `XMLHttpRequest`, which is what you want most of the time when debugging data loading. **Doc** shows the HTML documents, including iframes and redirects. **Other** catches things like `ping` beacons, preflight requests and some manifest or prefetch requests that don't fit other types.

### 199: How do you see redirects in the Network panel?

Each redirect is its own row with a `3xx` status, like `301` or `302`, and a `Location` response header that points to the next URL. With **Preserve log** on, you can follow the whole chain. Too many redirects add a round trip each, which slows the page, so it is worth removing them for the main document and important resources.

### 200: How do you check compression of responses?

Look at the `Content-Encoding` response header in the Headers tab, which will be `gzip`, `br` (Brotli) or `zstd` if the response was compressed. With **Big request rows** on, compare the transfer size and resource size in the Size column. If they are almost the same for a large text file, the server may not be compressing it.

### 201: How do you read the flame chart in the Performance panel?

Time runs left to right. Each bar is a task or function call, and the bars under it are the functions it called, so the stack grows downward. A wide bar took a long time. To find the cause of a slow task, start at the top bar and follow the wide bars down until you reach the function that does the actual work. Click any bar to see details in the Summary tab.

### 202: What do the colors in the Performance panel mean?

- **Yellow**: scripting (JavaScript running, compiling, event handlers, timers).
- **Purple**: rendering (recalculate style, layout).
- **Green**: painting and compositing.
- **Blue**: loading (parsing HTML, network events).
- **Gray**: system and other browser work.

The Summary tab shows a breakdown of the selected range by these categories, which tells you quickly if a slowdown is mostly JavaScript or mostly layout.

### 203: What are the Summary, Bottom-up, Call tree and Event log tabs?

They are views at the bottom of the Performance panel for the selected time range.

- **Summary**: time spent by category, or details about the selected event.
- **Bottom-up**: activities sorted by self time, the time spent in that function itself. Good for finding the functions that do the most work.
- **Call tree**: root activities with their callees, sorted by total time. Good for seeing which top-level task was expensive.
- **Event log**: every event in time order.

You can group Bottom-up and Call tree by domain, URL or third party.

### 204: What is the difference between self time and total time?

Self time is the time spent in the function's own code, not counting the functions it calls. Total time includes everything it calls. A function with a big total time but small self time just calls slow things, so you look inside it. A function with a big self time is doing the expensive work itself and is the place to optimize.

### 205: What tracks can you see in a Performance recording?

Common tracks are **Network** (requests over time), **Frames** (each frame, with dropped or partially presented ones marked), **Timings** (FCP, LCP, DCL, load, and your `performance.mark` and `performance.measure` entries), **Interactions** (clicks and key presses with their duration), **Layout shifts**, **Main** (main thread activity), **Animations**, **GPU**, **Raster**, **Compositor**, **Thread pool** and any web workers. You can collapse, hide and reorder tracks.

### 206: What does the Insights sidebar in the Performance panel do?

After a recording, the sidebar on the left lists insights, which are automatic checks on the trace, many of them based on Lighthouse audits. Examples are LCP breakdown, INP breakdown, layout shift culprits, render blocking requests, document request latency, forced reflow, DOM size, third parties, image delivery and font display. Hovering or clicking an insight highlights the related parts of the timeline. The Performance Insights panel that existed earlier was removed, and its ideas moved here.

### 207: What is the LCP breakdown in the Performance panel?

It splits Largest Contentful Paint into four parts:

- **Time to first byte**: waiting for the HTML.
- **Resource load delay**: time from TTFB until the LCP image starts downloading.
- **Resource load duration**: time to download the image.
- **Element render delay**: time from the download finishing to the element being painted.

For text LCP there is no resource, so only TTFB and render delay apply. The biggest part tells you what to fix: server speed, discoverability (preload, `fetchpriority="high"`), image size, or main thread blocking.

### 208: What is the INP breakdown in the Performance panel?

When you select an interaction in the Interactions track, DevTools splits its duration into three parts:

- **Input delay**: time waiting for the main thread before handlers start, often because another task is running.
- **Processing duration**: time spent in the event handlers.
- **Presentation delay**: time from the handlers ending to the next frame being shown, which includes style, layout and paint.

Each part has different fixes, so this breakdown tells you where to look.

### 209: How do you find which interaction has the worst INP?

Use the live metrics view in the Performance panel: interact with the page and look at the **Interactions** list, which shows each interaction with its duration, and the INP card shows the slowest one. You can turn on detailed logging to see the phases. Then record a trace while doing that interaction again to see what runs during it.

### 210: How do you find the cause of a layout shift?

In the live metrics view, the **Layout shifts** list shows each shift with the elements that moved. In a recording, the **Layout shifts** track shows purple diamonds; select one to see the moved elements and possible culprits, like an image without dimensions, a web font swap or content injected above. The **Layout shift culprits** insight groups them. The Rendering tab's **Layout shift regions** option flashes the shifted areas on the page.

### 211: How do you compare your local metrics with real-user data in DevTools?

In the live metrics view of the Performance panel, open the field data settings and turn it on. DevTools fetches data from the Chrome UX Report (CrUX) for the URL or origin and shows the 75th percentile real-user LCP, CLS and INP next to your local values. It can also suggest throttling settings that match your users. CrUX only has data for sites with enough Chrome traffic.

### 212: What is the difference between lab data and field data?

Lab data is measured in a controlled setup, like a DevTools recording or a Lighthouse run, on one device and network. It's repeatable and good for debugging. Field data is collected from real users on many devices and networks, like CrUX or your own RUM tool. Field data is what users actually feel, and Google uses it for Core Web Vitals. Lab and field numbers often differ, and INP in particular needs real interactions, so lab tools can't fully measure it.

### 213: How do you add notes to a performance trace?

You can annotate a trace: double-click an entry to add a label, create a link between two entries (for example from an event handler to the layout it caused), or select a time range and label it. Annotations show in the **Annotations** tab of the sidebar and are saved with the trace file. This is useful when you share a trace with a teammate and want to point at the problem.

### 214: How do you save and share a Performance recording?

Click the download icon in the Performance panel toolbar to save the trace as a JSON file. You can choose to include the resource content and source maps so the other person can see your original code. Anyone can load the file with the upload icon or by dragging it into the panel. Remember that traces can include URLs, screenshots and code from your app.

### 215: What does "Dim 3rd parties" do in the Performance panel?

It grays out the events from third-party scripts in the flame chart, so your own code stands out. DevTools decides what is third-party based on the domain. It helps you see quickly how much of the main thread time goes to analytics, ads, chat widgets and other scripts you don't own.

### 216: How do you hide functions you don't care about in the flame chart?

Right-click an entry in the Main track and choose **Hide function**, **Hide children**, **Hide repeating children** or **Reset children**. You can also add a script to the ignore list from there, and then its frames are hidden in the flame chart. This makes deep framework call stacks much easier to read. The track shows a marker when some entries are hidden.

### 217: How do you zoom and move around in a Performance recording?

Drag in the overview at the top to select a range, or use the mouse wheel and `W`/`S` to zoom and `A`/`D` to move left and right. Selecting a range creates a breadcrumb at the top, so you can go back to a wider view. In the settings you can switch between **Classic** navigation (wheel zooms) and **Modern** navigation (wheel scrolls, `Ctrl` or `Cmd` plus wheel zooms).

### 218: What does a red triangle on a Performance event mean?

It marks a problem DevTools detected. On tasks it means a long task. On layout events it can mean a forced reflow, where JavaScript read a layout property right after changing styles. Click the event and the Summary tab explains the warning and links to the line of code involved.

### 219: How do you find forced reflows in a recording?

Look for purple **Layout** or **Recalculate Style** blocks inside a JavaScript task, often with a red triangle and a "Forced reflow" warning. The Summary tab shows the JavaScript line that caused it, and the **Forced reflow** insight in the sidebar lists the top functions. The usual fix is to batch all DOM reads before writes, or use `requestAnimationFrame` to move writes to a later frame.

### 220: What is paint flashing and when would you use it?

Paint flashing, in the Rendering tab, highlights areas of the page in green whenever they are repainted. When you scroll or interact, you can see if the browser repaints large areas that should not change. For example, a fixed header repainting on every scroll, or an animation of `top` instead of `transform`, shows up as constant green flashes.

### 221: What does "Layer borders" in the Rendering tab show?

It draws orange and olive borders around compositor layers and tiles. Layers are parts of the page that the GPU can move on their own, like elements with `will-change: transform` or a 3D transform. It helps you check whether an animated element got its own layer, or spot too many layers, which use a lot of GPU memory.

### 222: What is the Layers panel?

The Layers panel (**More tools > Layers**) shows all compositor layers of the page in a list and a 3D view you can rotate. For each layer you can see its size, the reasons it was created (like `will-change` or overlapping another layer), memory use and how many times it was painted. It helps with animation and scrolling performance work.

### 223: What does "Frame rendering stats" show?

It shows an overlay in the corner of the page with a frame chart and the share of frames that were dropped or partially presented, plus GPU memory use. It gives you a live view of how smooth scrolling or an animation is. For details about what happened in a slow frame, record a trace in the Performance panel.

### 224: What does "Scrolling performance issues" in the Rendering tab do?

It highlights elements that may slow down scrolling, like non-passive `touchstart` or `wheel` listeners and elements that cause the page to repaint on scroll. Non-passive listeners force the browser to wait for JavaScript before scrolling. Making them `{ passive: true }` when they don't call `preventDefault()` fixes the issue.

### 225: What CSS media features can you emulate in the Rendering tab?

You can emulate `prefers-color-scheme`, `prefers-reduced-motion`, `prefers-contrast`, `prefers-reduced-transparency`, `forced-colors`, `color-gamut` and the media type (`print` or `screen`). You can also turn on **automatic dark mode** to see how Chrome's forced dark theme affects your page. This lets you test accessibility and theme styles without changing system settings.

### 226: How do you simulate vision deficiencies?

In the Rendering tab, use **Emulate vision deficiencies** and pick blurred vision, reduced contrast, protanopia (no red), deuteranopia (no green), tritanopia (no blue) or achromatopsia (no color). The page is shown as someone with that condition might see it. It helps check that you don't rely only on color to show information, like red and green status labels.

### 227: What does "Emulate a focused page" do?

When you click in DevTools, the page loses focus, which closes dropdowns, hides `:focus` styles and fires `blur` events. **Emulate a focused page** (in the Rendering tab, or the Command Menu) makes the page behave as if it still has focus. This makes it possible to inspect autocomplete lists, custom selects and popups that close on blur.

### 228: How do you inspect an element that disappears when you move the mouse?

A few options:

- Use **:hov** to force `:hover` if the element shows on hover.
- Turn on **Emulate a focused page** if it closes on blur.
- Run `setTimeout(() => { debugger; }, 3000)` in the Console, open the element, and wait for the debugger to freeze the page.
- With the Sources panel open, press `F8` (or `Ctrl+\`) while the element is visible to pause script execution. DevTools needs keyboard focus for this.
- Set a DOM breakpoint on its parent to pause when it's removed.

### 229: How does the Performance panel's CPU throttling differ between presets?

There are fixed presets like 4x and 6x slowdown and a 20x preset for very low-end devices. Newer versions also offer calibrated presets, like low-tier and mid-tier mobile, which run a short benchmark on your machine to pick a slowdown factor that matches those devices. Calibrated presets give more consistent results across fast and slow developer machines.

### 230: What other capture settings does the Performance panel have?

In the gear menu you can turn off JavaScript samples (smaller trace, but no JS call stacks), turn on advanced paint instrumentation (more detail about paint and layers, but slower), turn on CSS selector stats (which selectors cost the most during style recalculation, also slower), set network throttling and CPU throttling, and change the reported hardware concurrency. The **Screenshots** and **Memory** checkboxes add filmstrip images and a memory graph.

### 231: How do you see which CSS selectors are slow?

Turn on **Enable CSS selector stats** in the Performance panel's capture settings and record. Select a **Recalculate Style** event and open the **Selector stats** tab. It lists selectors with the time spent matching them, number of match attempts and match count. Very broad or complex selectors that are tried against many elements show up at the top.

### 232: What does the Memory checkbox in the Performance panel show?

It adds a graph under the timeline with JS heap size, number of documents, DOM nodes, event listeners and GPU memory over the recording. A JS heap that goes up and comes back down is normal garbage collection. A sawtooth that keeps rising, or DOM nodes and listeners that keep growing after each repeat of an action, points to a leak.

### 233: What are the Lighthouse modes?

- **Navigation**: loads the page and measures it, the classic Lighthouse report.
- **Timespan**: records a period while you interact with the page, which can show INP-related issues and layout shifts after load.
- **Snapshot**: checks the page in its current state, useful for accessibility checks of a modal or a page after some steps.

Not every audit is available in every mode.

### 234: Why do Lighthouse scores differ between runs?

The score depends on things that change from run to run: network conditions, CPU load from other apps, server response time, ads and A/B tests, and browser extensions. Lighthouse in DevTools uses simulated throttling by default, which reduces but does not remove the variation. To get stable numbers, close other apps, use Incognito, run it several times and look at the median, or run the Lighthouse CLI in CI.

### 235: What is the difference between simulated and DevTools throttling in Lighthouse?

With simulated throttling (the default), Lighthouse loads the page without slowing it down and then calculates what the metrics would be on a slower network and CPU. It is faster and more consistent. With DevTools throttling (also called applied throttling), Chrome actually slows the network and CPU during the load. You can pick it in the Lighthouse settings by unchecking **Simulated throttling**.

### 236: Which categories does Lighthouse audit today?

Performance, Accessibility, Best Practices and SEO. The PWA category was removed in Lighthouse 12, so installability checks now live mainly in the Application panel's Manifest section. Each category gives a 0-100 score and a list of passed and failed audits with explanations.

### 237: Should you aim for a Lighthouse performance score of 100?

Not as a goal in itself. The score is a lab measurement on one simulated device, and it does not always match what real users see. It's better to track the actual metrics (LCP, INP, CLS) from field data and fix the issues Lighthouse points out that matter for your users. A score in the 90s on a heavy app can still feel slow if real users have slow phones.

### 238: How do you run a Lighthouse audit on a page behind a login?

In DevTools, log in first in the same tab, then run Lighthouse. Lighthouse uses the same browser session, so it sees the logged-in page. In navigation mode, uncheck **Clear storage** in the Lighthouse settings so your session cookies are not cleared before the run. For CI, you can use Puppeteer to log in first and then run Lighthouse, or use a user flow.

### 239: How do you replay a recording in the Recorder at a slower speed?

Click the dropdown next to **Replay** and choose **Slow**, **Very slow** or **Extremely slow**. Each step waits longer, so you can see what happens. You can also set breakpoints on steps and step through them one at a time, which helps when a replay fails at some step.

### 240: How do you measure performance of a user flow with the Recorder?

After recording a flow, click **Performance panel** in the Recorder toolbar. DevTools replays the flow while recording a performance trace, then opens it in the Performance panel. This gives you a repeatable way to profile a multi-step scenario, like adding to cart and checking out, instead of doing it by hand each time.

### 241: What selectors does the Recorder use for steps?

The Recorder can use CSS, ARIA, text, XPath and pierce (for shadow DOM) selectors, and it stores several of them for each step so replay can fall back if one fails. You can tell it to prefer a custom attribute like `data-testid` when you start a new recording. Stable selectors make the recording keep working after small UI changes.

### 242: What formats can you export a Recorder flow to?

Built-in options are JSON, a Puppeteer script, a Puppeteer script for Firefox, and a Puppeteer plus Lighthouse script (a Lighthouse user flow). Recorder extensions add more formats, like Cypress, Playwright and others. You can also import a JSON recording back into the Recorder, and replay JSON recordings in Node with the `@puppeteer/replay` library.

### 243: How do you check unused CSS and JavaScript with the Coverage tool in a useful way?

Record coverage while you use the main parts of the page, not just on load, because code for clicks and other routes only runs later. Look at the files with the most unused bytes and check the red lines in Sources. Unused code on the first page is a good sign that it can be split into a lazy-loaded chunk. Code that is never used anywhere can be removed.

### 244: What is the difference between per function and per block coverage?

The Coverage tool lets you choose the granularity. **Per function** marks a whole function as used if it ran at least once, and has lower overhead. **Per block** marks each block inside a function, like the branches of an `if`, so you can see code paths that never ran. Per block is more detailed but makes the page a bit slower while recording.

### 245: How do you inspect and change a CSS animation's timing?

Open the **Animations** panel and trigger the animation. It appears as a group with a bar for each animated element. You can drag the bar to change the delay, drag its ends to change the duration, and scrub the timeline to look at a specific moment. In the Styles pane, click the curve icon next to an easing value to open the cubic-bezier editor.

### 246: How do you debug Flexbox layout problems in DevTools?

Click the `flex` badge in the DOM tree to show the overlay, which marks the container, items, free space and gaps. In the Styles pane, click the icon next to `display: flex` to open the Flexbox editor, which lets you change `flex-direction`, `flex-wrap`, `align-*` and `justify-*` with buttons. The inactive CSS hints tell you when a flex property is set on the wrong element.

### 247: How do you debug a CSS Grid layout in DevTools?

Click the `grid` badge or turn on the overlay in the Layout tab. The overlay shows line numbers, line names, track sizes, gaps and named areas. In the Layout tab you can choose which labels to show and extend grid lines across the page. The Grid editor next to `display: grid` in the Styles pane changes alignment properties with buttons.

### 248: How do you debug container queries in DevTools?

Elements that are query containers get a `container` badge in the DOM tree. In the Styles pane, rules inside `@container` show the query, and you can click the container name to select the container element. Hovering it shows its size, so you can see why a query matches or doesn't. You can also edit the query condition right in the Styles pane.

### 249: How does the Styles pane show cascade layers?

Rules inside `@layer` show the layer name above the rule. Since layer order matters more than specificity, a rule with lower specificity in a later layer can win. DevTools sorts rules by the cascade, including layers, and you can click the layer name to see the full layer order. This helps explain why a selector you thought was stronger is crossed out.

### 250: How do you find where a CSS custom property is defined?

Hover over a `var(--name)` value in the Styles pane to see its computed value. Click the variable name to jump to the rule where it's declared. In the Computed tab you can see all custom properties for the element with **Show all**. If the variable is not defined, DevTools marks it, and a fallback value is shown when one is given.

### 251: What views does a heap snapshot have?

- **Summary**: objects grouped by constructor name, with counts, shallow size and retained size.
- **Comparison**: the difference between two snapshots, showing what was added and deleted.
- **Containment**: the heap structure starting from roots like `window` and GC roots.
- **Statistics**: a chart of memory by type (code, strings, arrays, typed arrays, system objects).

Summary and Comparison are the ones you use most for finding leaks.

### 252: What is the difference between shallow size and retained size?

Shallow size is the memory used by the object itself. Retained size is the memory that would be freed if this object were deleted, which includes all objects that are only reachable through it. A small object, like a closure or a `Map`, can have a huge retained size because it keeps a big tree of other objects alive. When hunting leaks, sort by retained size.

### 253: What is the Retainers section in a heap snapshot?

When you select an object, the **Retainers** section at the bottom shows the chain of references that keeps it alive, from the object back to a GC root. Reading it from top to bottom tells you which variable, property, closure or listener is holding the object. Finding the first retainer that belongs to your code usually shows you where the leak is.

### 254: What does the Distance column in a heap snapshot mean?

Distance is the number of references on the shortest path from a GC root (like the `window` object) to the object. Objects with a lower distance are closer to the root. It can help spot objects held by unexpected paths, but in practice the Retainers section is more useful for understanding why something is still alive.

### 255: How do you find a memory leak with heap snapshots?

A common method:

1. Load the page and do the action once to warm up caches.
2. Take a heap snapshot.
3. Repeat the action several times, like opening and closing a modal, and return to the start state.
4. Take a second snapshot.
5. Select the second snapshot and switch to **Comparison** against the first.

Look for constructors whose count grew by the number of repeats, then use Retainers to find what holds them. DevTools forces a garbage collection before each snapshot, so what you see is really retained.

### 256: What is a detached DOM element?

It is a DOM node that has been removed from the document but is still referenced from JavaScript, so it can't be garbage collected. A typical case is storing an element in an array or a closure and then removing it from the page. Detached nodes often keep their whole subtree and listeners in memory, which can be a lot.

### 257: How do you find detached DOM elements?

In the Memory panel, choose the **Detached elements** profile type and click **Obtain detached elements**. It lists the detached nodes that are still retained, grouped by tree. Click a node to see it in the Elements-like view and find where it's referenced. In a heap snapshot you can also type `Detached` in the class filter to find nodes with names like `Detached HTMLDivElement`.

### 258: What is "Allocations on timeline"?

It is a Memory panel profile type that records memory allocations over time while you use the page. Blue bars on the timeline show memory that was allocated and is still alive at the end; gray bars show memory that was freed. You can select a bar to see the objects allocated in that time and their stack traces, which helps find code that allocates objects that never go away.

### 259: What is "Allocation sampling"?

It records where memory is allocated, by function, using sampling, so it has very low overhead and can run for a long time. The result is shown like a CPU profile, but for memory, with the functions that allocated the most memory at the top. It's good for finding which code creates a lot of garbage, not for proving that a single object leaked.

### 260: Why do objects stay in memory after you log them in the Console?

When you log an object, the Console keeps a reference to it so you can expand it later. That reference stops it from being garbage collected, which can look like a leak in a heap snapshot. The same goes for `$0`, `$_`, `temp1` and other Console variables. Clear the Console and avoid logging the objects you are tracking before taking snapshots.

### 261: How do you force garbage collection in DevTools?

Click the trash can icon (**Collect garbage**) in the Memory panel or in the Performance panel toolbar. It runs a full garbage collection. It's useful before a measurement, so the numbers don't include garbage that is waiting to be collected. Heap snapshots already force a GC on their own.

### 262: What does "Update on reload" do for service workers?

In **Application > Service workers**, **Update on reload** makes Chrome install and activate a new version of the service worker on every page reload, skipping the waiting phase. Normally a new service worker waits until all tabs using the old one are closed. This option saves a lot of time during development, but it doesn't reflect how updates work for real users.

### 263: What does "Bypass for network" do?

When checked, the page ignores the service worker and sends all requests to the network, although the worker stays registered. It's useful when the worker's cache is serving old files and you want to see your latest code. It is different from the Network panel's **Disable cache**, which only bypasses the HTTP cache.

### 264: How do you debug service worker code?

Open **Application > Service workers** and click the link to the worker's source, or find it in the Sources panel under the worker's thread. You can set breakpoints in `install`, `activate` and `fetch` handlers. The Console context dropdown lets you run code in the worker's scope. `chrome://serviceworker-internals` shows all workers in the browser with more low-level details and logs.

### 265: How do you test push notifications without a push server?

In **Application > Service workers**, type a payload in the **Push** field and click **Push**. DevTools fires a `push` event on the service worker with that data, so you can test your notification code. There are similar buttons for **Sync** and **Periodic sync** to trigger those events.

### 266: What is the back/forward cache, and how do you test it in DevTools?

The back/forward cache (bfcache) keeps a full snapshot of a page in memory when you navigate away, so going back or forward is instant. Some things prevent it, like `unload` listeners or `Cache-Control: no-store` on the page. In **Application > Back/forward cache**, click **Test back/forward cache**. DevTools navigates away and back, and tells you if the page was restored from the cache and, if not, the reasons why.

### 267: What does Application > Speculative loads show?

It shows prefetch and prerender activity from the Speculation Rules API, and other preloading. You can see the rules the page defines, every speculation attempt with its status (like ready, failure or not triggered), and why an attempt failed. Newer versions let you filter attempts with keys like `url:`, `action:` and `status:`. It helps check that your speculation rules actually prerender the pages you expect.

### 268: How do you test what happens when storage is almost full?

Go to **Application > Storage** and turn on **Simulate custom storage quota**, then enter a small size in MB. The browser now reports and enforces that quota for the site, so you can test how your app handles `QuotaExceededError` when saving to IndexedDB or Cache Storage. It doesn't fill your disk; it only changes the limit.

### 269: What does the Partition Key column in the Cookies view mean?

It shows the partition of a cookie set with the `Partitioned` attribute (CHIPS). A partitioned cookie is stored separately for each top-level site where it was set. For example, a chat widget embedded on two different sites gets two separate cookies. The column shows the top-level site, which helps debug third-party cookie behavior.

### 270: How do you see the frames on a page and their security details?

Go to **Application > Frames** and expand **top**. Each frame shows its URL, origin, whether it's a secure context, whether it's cross-origin isolated, and the policies that apply, like permissions policy. This is useful for debugging iframes and features that need cross-origin isolation, like `SharedArrayBuffer`.

### 271: How do you override the timezone and locale for a page?

Open the **Sensors** tool. Under **Location**, you can choose a preset or **Other**, and set the **Timezone ID** (like `Asia/Tbilisi`) and the **Locale** (like `de-DE`). This changes what `Intl.DateTimeFormat` and `Date` return in the page, so you can test date and number formatting for users in other countries.

### 272: How do you emulate device orientation?

In **Sensors**, under **Orientation**, choose a preset like **Portrait upright** or **Landscape left**, or enter custom alpha, beta and gamma values. You can also drag the 3D phone model. Pages listening to `deviceorientation` events get these values. Rotating the screen in Device Mode is a different thing: it swaps width and height.

### 273: How do you add a custom device to Device Mode?

Go to **Settings > Devices** and click **Add custom device**. Enter a name, width, height, device pixel ratio, user agent string and type (mobile, desktop, tablet). The device then appears in the Device Mode dropdown. This is useful for testing a specific device your users have that isn't in the default list.

### 274: What is port forwarding in remote debugging?

When debugging an Android phone, the phone often can't reach `localhost` on your computer. In `chrome://inspect#devices`, open **Port forwarding** and add a rule like `8080` to `localhost:3000`. Then `localhost:8080` on the phone goes through the USB connection to your dev server. This lets you test your local site on a real phone without exposing it to the network.

### 275: Why is `node --inspect=0.0.0.0` risky?

The inspector protocol lets anyone who can connect run any code in your Node process. By default `--inspect` listens only on `127.0.0.1:9229`. Binding to `0.0.0.0` makes it open to the whole network, so someone on the same network, or the internet if the port is open, could take over the process and the machine. If you need remote debugging, use an SSH tunnel instead.

### 276: How do you debug a web worker in DevTools?

Workers appear in the Sources panel's **Threads** pane and in the file tree. You can set breakpoints in worker scripts like in normal scripts, and when a worker pauses, the Threads pane shows which thread is paused. In the Console, pick the worker from the context dropdown to run code in it. In the Performance panel, each worker gets its own track.

### 277: What do the Console settings "Selected context only" and "Group similar messages" do?

**Selected context only** shows only messages from the context chosen in the dropdown, like one iframe or worker, instead of everything. **Group similar messages** collapses repeated messages into one line with a counter, which keeps the Console readable when something logs in a loop. Turn it off when you need to see each message in order.

### 278: How do you see only messages from your own code in the Console?

Open the Console sidebar (the icon on the left of the Console toolbar). It groups messages by type and by source file, so you can click a file to show only its messages. You can also filter with `url:` or `-url:` in the filter box. Turning off **Show CORS errors** and **Log XMLHttpRequests**, or hiding network messages, also reduces noise.

### 279: What does "Log XMLHttpRequests" do?

It logs a line in the Console for every finished `fetch` and XHR request, with the method and URL. It shows API calls in the same place as your logs and errors, which helps you see the order of things, like "click handler ran, then the request finished, then the error happened".

### 280: What does the Privacy and security panel show?

It shows whether the page is served over a secure connection, details of the TLS connection and the certificate, and lists any mixed content (HTTP resources loaded on an HTTPS page). Newer versions also include privacy controls related to third-party cookies for testing. Clicking an origin shows details for its connection.

### 281: How do you find mixed content on a page?

Mixed content warnings and errors show in the Console and the Issues panel. In the Network panel you can filter with `mixed-content:displayed` or `mixed-content:all`, or `scheme:http`. The Privacy and security panel lists origins loaded over HTTP. Active mixed content, like scripts, is blocked by Chrome; images and media may be auto-upgraded to HTTPS.

### 282: What is the WebAuthn panel used for?

It lets you test passkeys and other WebAuthn logins without a real hardware key or biometric sensor. You enable a virtual authenticator environment and add virtual authenticators with options like protocol (CTAP2 or U2F), transport (USB, NFC, BLE, internal), resident keys and user verification. Your site can then register and sign in with them, and you can see the credentials created.

### 283: What is the Media panel?

It shows information about `<video>` and `<audio>` players on the page: properties like resolution, codec, buffering state and decoders used, plus events and errors from the media pipeline. It helps debug playback problems, like a video that doesn't start or stutters. Open it with **More tools > Media**.

### 284: How do you move a DOM node to another place in the tree?

Drag the node in the Elements panel and drop it where you want. You can also cut and paste with `Ctrl+X` and `Ctrl+V`. This is useful to test how a component looks in a different container. Like other Elements changes, it only affects the current page until reload.

### 285: What is `inspector-stylesheet`?

When you add a new style rule with the **+** button, DevTools puts it in a special stylesheet called `inspector-stylesheet`, shown as the rule's source. You can open it in the Sources panel and see all rules you added. It is a scratch area, not saved anywhere, so copy the rules to your real CSS before reloading.

### 286: How do you copy CSS from the Styles pane?

Right-click a rule or a declaration in the Styles pane. Options include **Copy declaration**, **Copy property**, **Copy value**, **Copy rule**, **Copy all declarations** and **Copy declaration as JS** or **Copy all declarations as JS**, which give you camelCase properties for inline styles in JavaScript. You can also copy all CSS changes from the Changes tool.

### 287: How do you check which fonts an element actually uses?

Select the element and scroll to the bottom of the **Computed** tab, where **Rendered Fonts** lists the font family that was really used and how many glyphs came from each font. The `font-family` value in CSS is only a list of choices; this section tells you if a fallback was used because a web font didn't load or doesn't have some characters.

### 288: How do you debug keyboard focus problems with DevTools?

Add a Live Expression with `document.activeElement` to see which element has focus as you press `Tab`. Use `:focus` and `:focus-visible` in **:hov** to check focus styles. In the Accessibility pane, check the role and name of the focused element. Use **Emulate a focused page** if focus keeps moving to DevTools when you click it.

### 289: How do you check accessibility issues of a page with DevTools?

Run the **Accessibility** category in Lighthouse for an automatic report with issues like missing labels, low contrast and wrong ARIA. Use the inspect tooltip and color picker for contrast, the Accessibility pane for each element's role and name, and the full-page accessibility tree to see the structure. Automated checks find only part of the problems, so you still need keyboard and screen reader testing.

### 290: What do the "Accessibility" checks in the inspect tooltip mean?

When you hover an element in inspect mode, the tooltip has an **Accessibility** section with the contrast ratio, the element's name and role, and whether it's keyboard-focusable. A warning icon next to contrast means the text doesn't meet the minimum ratio. A focusable element without a name is a hint that a screen reader user won't know what it does.

### 291: How can AI assistance help with CSS debugging?

Select an element and open AI assistance (or right-click and choose **Ask AI**). You can ask questions like "why is this element not centered?" or "why is there a gap below this image?". The agent can run scripts on the page to read computed styles and the DOM, and it can suggest and apply style changes. If your project is connected through Workspaces, some changes can be saved to your source files.

### 292: What kinds of context can you give AI assistance?

You can chat about a DOM element (styling and layout), a network request (headers, timing, status), a source file, or a performance trace and its insights. Newer versions can pick the context automatically when you ask an open-ended question, like "which requests are the slowest?". You can also start from the Console with **Understand this error**.

### 293: What should you keep in mind about privacy when using AI assistance?

The data you send, like the page's DOM, network headers, source code and trace data, goes to Google to generate answers. Depending on your account and settings, it may be reviewed and used to improve products. So don't use it on pages with personal, confidential or customer data unless your company allows it. Enterprise admins can turn the feature off with a policy, and it's not available in some regions or for users under 18.

### 294: What is code generation in the Console and Sources panels?

Newer versions of DevTools can write code for you with Gemini. You write a comment describing what you want, like `// get all links that open in a new tab`, and press `Ctrl+I` (`Cmd+I` on Mac) to generate the code. Earlier versions only offered inline code suggestions while you typed. You must turn on the feature in **Settings > AI innovations**, and you should read the code before running it.

### 295: How do you see the component tree of an Angular app in DevTools?

Install the Angular DevTools extension. It adds an **Angular** panel with a component explorer showing the tree of components and directives, their inputs, outputs and state (including signals), and a profiler that records change detection cycles. In the Console, the global `ng` object also has helpers in development builds, like `ng.getComponent($0)` to get the component instance of the selected element.

### 296: What does Redux DevTools add?

The Redux DevTools extension adds a panel that lists every dispatched action, the state after each action, and the difference between states. You can jump back to any previous state (time travel), skip actions, and export or import the action log. Redux Toolkit's `configureStore`, NgRx with `provideStoreDevtools`, and Zustand's `devtools` middleware can all connect to it.

### 297: How do you hide network messages and violations from the Console?

In the Console settings, check **Hide network** to hide messages about failed requests. Violation messages like "[Violation] 'click' handler took 250ms" are Verbose level, so they are hidden unless you turn on **Verbose**. You can also right-click a message and choose to hide messages from that source file.

### 298: What are "[Violation]" messages in the Console?

They are Verbose-level messages from Chrome that point out code that may hurt performance, like a long-running event handler, a forced reflow, or a non-passive touch listener. They don't break anything, but they tell you where the main thread was blocked. Turn on **Verbose** in the levels dropdown to see them.

### 299: How do you debug code inside an iframe in the Sources panel?

Each frame's files are grouped under the frame's name or URL in the **Page** tab. You can set breakpoints in iframe scripts like any others. When a breakpoint in an iframe hits, the Console context switches to that frame. Cross-origin iframes may run in a separate process, and they appear as their own targets in the file tree.

### 300: How do you check that `preload` and `fetchpriority` hints work?

In the Network panel, add the **Priority** column and check that the preloaded or `fetchpriority="high"` resource starts early in the waterfall with a high priority. The Initiator should show the `<link rel="preload">`. A Console warning appears if a preloaded resource is not used within a few seconds of the load event. In a Performance recording, the LCP breakdown shows if the LCP image still has a long load delay.

## Advanced Questions (301-450)

### 301: How does DevTools talk to the page it inspects?

DevTools uses the Chrome DevTools Protocol (CDP). The DevTools frontend sends JSON commands like `DOM.getDocument` or `Debugger.setBreakpointByUrl` and receives responses and events like `Network.requestWillBeSent`. Inside Chrome, these messages are handled by agents in the renderer and browser processes, including V8's inspector for JavaScript. When DevTools is built in, the messages go over Chrome's internal messaging; external clients connect over a WebSocket.

### 302: What is the Chrome DevTools Protocol?

CDP is the protocol for inspecting, debugging and controlling Chromium-based browsers. It is split into domains, like `Page`, `DOM`, `CSS`, `Network`, `Runtime`, `Debugger`, `Profiler`, `HeapProfiler`, `Tracing`, `Emulation`, `Input` and `Target`. Each domain has commands you send and events you receive. Tools like Puppeteer, Playwright (for Chromium), Lighthouse and many test runners are built on top of it.

### 303: Is the DevTools frontend a native app?

No. The DevTools UI is a web application written in TypeScript, mostly using web components and Lit. Chrome bundles it and loads it in a special window or docked view. The source is open in the `chrome-devtools-frontend` repository. Because it's a web page, you can even inspect DevTools with another DevTools.

### 304: How do you inspect DevTools itself?

Undock DevTools into a separate window, focus it, and press `Ctrl+Shift+I` (`Cmd+Option+I` on Mac). A second DevTools opens that inspects the first one. This is sometimes called "DevTools on DevTools". It's how DevTools developers work, and it's also a handy way to see what CDP messages the frontend sends, or to debug a DevTools extension panel.

### 305: How do you connect to Chrome with CDP from your own script?

Start Chrome with a remote debugging port and a separate profile, then get the WebSocket URL and send JSON messages.

```bash
chrome --remote-debugging-port=9222 --user-data-dir=/tmp/chrome-debug
curl http://localhost:9222/json/version
```

```js
// Node 22+ has a global WebSocket
const { webSocketDebuggerUrl } = await fetch(
  "http://localhost:9222/json/version",
).then((r) => r.json());
const ws = new WebSocket(webSocketDebuggerUrl);

ws.onopen = () => {
  ws.send(JSON.stringify({ id: 1, method: "Target.getTargets" }));
};
ws.onmessage = (event) => console.log(JSON.parse(event.data));
```

In practice you would use Puppeteer or a CDP client library instead of raw messages.

### 306: Why does recent Chrome refuse `--remote-debugging-port` on the default profile?

Starting with Chrome 136, the `--remote-debugging-port` and `--remote-debugging-pipe` flags are ignored when Chrome uses the default user data directory. Malware was using the debug port to steal cookies and sessions from users' real profiles. Now you must also pass `--user-data-dir` pointing to a separate folder, so the debugged browser can't reach your normal profile data.

### 307: What is the Protocol monitor?

The Protocol monitor is a DevTools panel that shows every CDP message the DevTools frontend sends and receives, with parameters, responses and timing. You can also send your own CDP commands from it, with an editor that helps fill in parameters. It's useful for learning CDP, or for finding which command does what before writing a Puppeteer script. You can find it via the Command Menu or **More tools**.

### 308: How does Puppeteer use CDP?

Puppeteer starts or connects to Chrome and opens a CDP session for each page. Its API calls turn into CDP commands; for example `page.goto()` uses `Page.navigate`, `page.click()` uses `Input.dispatchMouseEvent`, and `page.tracing.start()` uses the `Tracing` domain. You can also open a raw session with `page.createCDPSession()` to call any CDP method that Puppeteer doesn't wrap. Puppeteer also supports WebDriver BiDi, mainly for Firefox.

```js
const client = await page.createCDPSession();
await client.send("Network.enable");
await client.send("Network.emulateNetworkConditions", {
  offline: false,
  latency: 150,
  downloadThroughput: (1.6 * 1024 * 1024) / 8,
  uploadThroughput: (750 * 1024) / 8,
});
```

### 309: What is WebDriver BiDi and how is it related to CDP?

WebDriver BiDi is a W3C standard protocol for browser automation that works across Chrome, Firefox and others. Like CDP, it is two-way and event-based over WebSocket, unlike classic WebDriver which is request-response over HTTP. CDP is Chromium-specific, changes more often and exposes more internals. BiDi is for cross-browser automation, while CDP is still what DevTools itself uses.

### 310: How do you record a performance trace from a script?

With Puppeteer you can call `page.tracing.start()` and `page.tracing.stop()`. The result is the same trace JSON the Performance panel uses, so you can open it in DevTools.

```js
import puppeteer from "puppeteer";

const browser = await puppeteer.launch();
const page = await browser.newPage();

await page.tracing.start({ path: "trace.json", screenshots: true });
await page.goto("https://example.com", { waitUntil: "networkidle0" });
await page.tracing.stop();

await browser.close();
```

You can also use the `Tracing` CDP domain directly, or `chrome://tracing`-style categories for deeper browser internals.

### 311: What is the Chrome DevTools MCP server?

It is an official Model Context Protocol server, `chrome-devtools-mcp`, that lets AI coding agents control a Chrome instance and use DevTools features. Through it an agent can navigate pages, click and fill forms, read Console messages and network requests, take screenshots, record performance traces and read insights, take memory snapshots and run Lighthouse audits. It lets an agent check its own changes in a real browser.

```json
{
  "mcpServers": {
    "chrome-devtools": {
      "command": "npx",
      "args": ["-y", "chrome-devtools-mcp@latest"]
    }
  }
}
```

### 312: What are the risks of giving an AI agent access to the browser through the DevTools MCP server?

The agent can see everything in that browser instance: page content, cookies, network traffic and anything you are logged into. It can also be influenced by text on web pages it visits (prompt injection). To reduce the risk, use a separate, isolated profile without your real logins, avoid sensitive sites, review what the agent does, and don't let it use production accounts.

### 313: How do you add your own data to the Performance panel?

The simplest way is the User Timing API. `performance.mark()` and `performance.measure()` entries show up in the **Timings** track. With the extensibility API, you can put a `devtools` object in the `detail` field to create custom tracks with colors, tooltips and extra properties.

```js
const start = performance.now();
renderProductList(products);

performance.measure("Render product list", {
  start,
  end: performance.now(),
  detail: {
    devtools: {
      dataType: "track-entry",
      track: "Rendering",
      trackGroup: "My app",
      color: "tertiary-dark",
      properties: [["items", String(products.length)]],
      tooltipText: "Rendered product grid",
    },
  },
});
```

### 314: What does `console.timeStamp()` do in newer versions of Chrome?

Originally it just added a marker to the timeline. Chrome extended it so you can pass a label, a start time, an end time, a track name, a track group and a color, and it then draws an entry on a custom track like `performance.measure` does. The advantage is that it has almost no overhead and doesn't create entries in the performance timeline buffer, so it's good for frameworks that want to instrument many small operations.

### 315: How does the JavaScript profiler in the Performance panel collect data?

It's a sampling profiler. V8 stops the main thread at a regular short interval and records the current call stack. The flame chart is built from these samples, so time per function is an estimate. Very short functions can be missed entirely, and inlined functions may appear inside their caller. That's why you look for wide, repeated patterns, not single tiny bars.

### 316: Why can a function show up as "(anonymous)" or with a strange name in a profile?

Arrow functions and callbacks without names show as `(anonymous)` unless V8 can infer a name from the variable or property they are assigned to. In minified code, names are short like `t` or `e`. Source maps fix the file and line but not always the function name. Naming important functions and keeping source maps available makes profiles much easier to read.

### 317: How are source maps structured?

A source map is a JSON file with `version: 3`, `sources` (original file paths), optional `sourcesContent` (the original code itself), `names` (original identifiers) and `mappings`. `mappings` is a string of Base64 VLQ encoded segments that map each position in the generated file to a source file, line, column and optionally a name. Newer fields like `x_google_ignoreList` and the standard `ignoreList` mark third-party sources.

### 318: Is it safe to publish source maps in production?

It is a trade-off. Public source maps make debugging production errors easy, and minification was never a security barrier, since anyone can pretty print your code. But if `sourcesContent` includes comments, internal paths or secrets accidentally put in the code, they become very easy to read. A common middle ground is to generate maps but upload them only to your error tracker (like Sentry) or serve them from an internal server, and load them in DevTools with **Add source map** when needed.

### 319: Why do breakpoints sometimes jump to a different line, or not hit, with source maps?

The source map may be out of date, wrong, or only map at the start of statements, so a breakpoint on a line without a mapped position slides to the next mapped one. Transpilation can also merge or split code: a line in your TypeScript may become several pieces, or be removed as dead code. Making sure the map matches the running bundle and using a mapping mode that keeps column info (not `eval`-based maps) fixes most cases.

### 320: How does live editing JavaScript work under the hood?

When you save a script in Sources, DevTools sends `Debugger.setScriptSource` with the new code. V8 compiles it and replaces the code of the changed functions, keeping the script's state where it can. If a changed function is on the call stack, V8 can only replace it if it's the top frame, and then it restarts that frame. Changes that V8 can't apply safely are rejected with an error. Closures already created keep their captured variables.

### 321: How does a breakpoint actually work in V8?

When you set a breakpoint, DevTools sends a CDP command like `Debugger.setBreakpointByUrl`. V8 finds the matching code position and patches the function's bytecode with a debug break at that point. When execution reaches it, V8 stops the thread and sends a `Debugger.paused` event with the call frames and scope objects. While paused, DevTools evaluates expressions with `Debugger.evaluateOnCallFrame`. Optimized code is deoptimized where needed so the debugger can show accurate values.

### 322: Why can an open DevTools make the page slower?

Some features add overhead while DevTools is open: recording network requests with bodies, keeping Console messages and the objects they reference, async stack traces, source map processing, breakpoints that force deoptimization, and **Disable cache** if it's on. Heavy `console.log` calls with large objects can be slow too. For accurate measurements, use the Performance panel's recording (which is designed for it), close unneeded panels, and avoid logging inside hot loops.

### 323: Why do variables sometimes show as "value unavailable" or "optimized out" in the debugger?

V8 can drop variables that a function no longer needs, or keep them only in registers, to save memory and speed things up. Closures also only capture the variables they actually use, so a variable from an outer function that no inner function uses is not kept in the closure scope. When you pause, DevTools can't show a value that doesn't exist anymore. Referencing the variable in the code, or pausing earlier, makes it available.

### 324: What does the `(closure)`, `(system)` and `(compiled code)` grouping in a heap snapshot mean?

These are internal V8 categories. `(closure)` groups function objects with their captured scopes. `(compiled code)` is the bytecode and machine code V8 generated. `(system)` is internal V8 structures, like hidden classes (maps) and descriptor arrays. `(string)`, `(array)` and `(number)` group primitive storage. Most leak hunting focuses on your own constructors and `Detached` DOM nodes, but a big `(closure)` group can point to listeners or callbacks that pile up.

### 325: How can a closure cause a memory leak?

A closure keeps the variables it uses from outer scopes alive as long as the closure itself is reachable. If a long-lived function, like an event listener on `window` or a callback stored in a global, captures a variable that points to a big object or a DOM node, that object can't be freed. In V8, closures created in the same scope share one context object, so one leaked closure can keep variables used by other closures alive too.

```js
function setup(bigData) {
  const used = bigData.summary;
  const unused = () => bigData; // shares the context with the listener below
  window.addEventListener("resize", () => console.log(used));
}
```

### 326: How do WeakMap and WeakRef affect what you see in heap snapshots?

Keys of a `WeakMap` and targets of a `WeakRef` are held weakly, so they don't keep an object alive. In the Retainers view, weak references are shown but DevTools marks them, and they don't count when the GC decides what to keep. If an object is retained only through weak paths, the next garbage collection will free it. Using `WeakMap` for data attached to DOM nodes is a common way to avoid leaks.

### 327: What is a dominator in heap analysis?

Object A dominates object B if every path from the GC roots to B goes through A. The retained size of an object is the total size of all objects it dominates, plus its own size. This is why removing one object, like a cache or a component instance, can free a lot of memory. DevTools uses the dominator tree internally to calculate retained sizes.

### 328: How do you find a leak caused by an event listener that is never removed?

Use the Performance monitor to watch **JS event listeners** while repeating the action; if the number grows each time, listeners leak. In a heap snapshot comparison, look for growing `(closure)` counts or `EventListener` entries and follow Retainers to the target, often `window` or `document`. `getEventListeners(window)` in the Console lists them. Fix it by removing the listener on cleanup, or by using an `AbortController` signal.

```js
const controller = new AbortController();
window.addEventListener("resize", onResize, { signal: controller.signal });
// on cleanup
controller.abort();
```

### 329: How do you debug a memory leak in a single-page app when navigating between routes?

Go to route A, then B, then back to A to warm up. Take a snapshot. Do the A to B to A loop several times, take another snapshot, and compare. Look for component instances, detached DOM trees, stores or subscriptions whose count grows with each loop. Common causes are subscriptions not unsubscribed, intervals not cleared, global caches keyed by route data, and third-party widgets that aren't destroyed. Retainers usually lead to a module-level variable or a listener.

### 330: How do you analyze memory of a Node.js process with DevTools?

Start Node with `--inspect`, connect through `chrome://inspect`, and use the Memory tab to take heap snapshots or record allocation timelines, just like for a page. You can also write a snapshot from code with `v8.writeHeapSnapshot()` or start Node with `--heapsnapshot-signal=SIGUSR2`, then load the `.heapsnapshot` file into the Memory panel. For production servers, prefer taking snapshots on a copy of the traffic, because taking one pauses the process and uses a lot of memory.

### 331: What is the Memory inspector?

The Memory inspector (**More tools > Memory inspector**) shows the raw bytes of an `ArrayBuffer`, `TypedArray`, `DataView`, or WebAssembly memory. While paused, right-click a buffer in the Scope pane and choose to reveal it in the Memory inspector. You can see bytes in hex and ASCII, read values as integers or floats in different endianness, and jump to addresses. It's useful for binary protocols, canvas pixel data and Wasm.

### 332: How do you debug WebAssembly in DevTools?

Without extra tools, DevTools shows Wasm modules as disassembled text (WAT-like) where you can step and set breakpoints, and inspect locals and the stack. For C, C++ or Rust compiled with DWARF debug info, install the **C/C++ DevTools Support (DWARF)** extension. Then the Sources panel shows your original source files, and you can set breakpoints, step through and inspect variables with their original types.

### 333: How does a DevTools extension work?

A Chrome extension declares a `devtools_page` in its manifest. That page runs every time DevTools opens and can use the `chrome.devtools.*` APIs: `chrome.devtools.panels` to add panels or sidebars, `chrome.devtools.inspectedWindow` to run code in the inspected page, and `chrome.devtools.network` to read requests and HAR data. To talk to the page more deeply, extensions usually inject a content script and pass messages through the background service worker.

```json
{
  "manifest_version": 3,
  "name": "My DevTools Panel",
  "version": "1.0",
  "devtools_page": "devtools.html"
}
```

```js
// devtools.js, loaded from devtools.html
chrome.devtools.panels.create("My Panel", "", "panel.html");
```

### 334: How do framework DevTools extensions get component data from the page?

The framework includes a hook in development builds. React looks for `window.__REACT_DEVTOOLS_GLOBAL_HOOK__`, which the extension's content script installs before React loads. React registers its renderers with that hook and reports commits, so the extension can build the component tree. Data is sent through `window.postMessage` to the content script, then to the extension's DevTools panel. Production builds expose less data, which is why some features only work in development.

### 335: What is the trace event format?

It's the JSON format used by Chrome's tracing system and the Performance panel. A trace has a `traceEvents` array of events with fields like `name`, `cat` (category), `ph` (phase, like `X` for complete events or `B` and `E` for begin and end), `ts` (timestamp in microseconds), `dur`, `pid`, `tid` and `args`. DevTools parses these into tracks, the flame chart and insights. Other tools, like Perfetto, can open the same files.

### 336: How do Long Animation Frames relate to what you see in DevTools?

The Long Animation Frames API (LoAF) reports frames that took more than 50 ms from start to paint, with the scripts that ran in them, their source URLs and durations. It's the field version of what you see in a DevTools trace: you can send LoAF data from real users to your analytics to find which scripts cause slow interactions. Then you reproduce the problem locally and use the Performance panel to see the details.

### 337: How do you profile a web page on an Android phone?

Connect the phone with USB debugging, open `chrome://inspect#devices` and inspect the tab. Use the Performance panel from the remote DevTools to record a trace; it records on the phone itself, so CPU numbers are real. Turn off CPU throttling in DevTools for this, since the device is already slow. Traces from the phone show how your code runs on real mobile hardware, which is often 3 to 10 times slower than a laptop.

### 338: What are the limits of Device Mode and throttling for performance testing?

CPU throttling slows the main thread by a multiplier but doesn't model memory limits, thermal throttling, slower GPUs or slow storage. Network throttling adds latency and caps bandwidth at the browser level, but it doesn't model packet loss or real radio behavior. The results are useful for comparing before and after a change, but you should confirm important decisions on real devices and with field data.

### 339: Why might Lighthouse in DevTools and PageSpeed Insights give different results?

PageSpeed Insights runs Lighthouse on Google servers with fixed hardware and network settings, and also shows CrUX field data. DevTools Lighthouse runs on your machine, with your CPU, network, extensions and location. The server location, cache state, A/B tests and ads can differ too. Neither is wrong; use field data for the real picture and compare lab results only within the same setup.

### 340: How does Chrome decide what counts as third-party in the Performance panel?

DevTools groups URLs by entity. It uses a list of known third-party entities (from the third-party-web dataset) to group domains like `google-analytics.com` and `googletagmanager.com` under one company, and treats the main page's site as first-party. Unknown domains different from the page's site are also treated as separate entities. This is why some subdomains of your own CDN may show up as third-party unless they share the site.

### 341: How would you use CDP to emulate a slow device in automated tests?

Use the `Emulation` and `Network` domains through Puppeteer or Playwright: `Emulation.setCPUThrottlingRate` with a rate like 4, `Network.emulateNetworkConditions` for latency and bandwidth, and `Emulation.setDeviceMetricsOverride` for screen size and DPR. Puppeteer has helpers like `page.emulateCPUThrottling()` and `page.emulateNetworkConditions()`. Running performance tests this way in CI gives more stable comparisons between builds.

```js
import { PredefinedNetworkConditions } from "puppeteer";

await page.emulateCPUThrottling(4);
await page.emulateNetworkConditions(PredefinedNetworkConditions["Slow 4G"]);
```

### 342: How can you intercept and modify requests with CDP?

The `Fetch` domain lets you pause requests that match patterns and then continue, modify, fulfill with a fake response, or fail them. Puppeteer exposes this through `page.setRequestInterception(true)` and the `request` event. This is the same idea as DevTools Local Overrides, but scriptable, and it's used for mocking APIs in tests.

```js
await page.setRequestInterception(true);
page.on("request", (request) => {
  if (request.url().endsWith("/api/user")) {
    request.respond({
      status: 200,
      contentType: "application/json",
      body: JSON.stringify({ name: "Test user" }),
    });
  } else {
    request.continue();
  }
});
```

### 343: How do you collect JavaScript coverage in automated tests?

Use CDP's `Profiler.startPreciseCoverage` and `Profiler.takePreciseCoverage`, or Puppeteer's `page.coverage.startJSCoverage()` and `stopJSCoverage()`, which return ranges of used code for each script. This is the same data as the Coverage panel. You can use it to track unused bytes per route in CI, or convert it to Istanbul format for test coverage reports.

### 344: Why are DevTools features sometimes behind experiments, and how do you turn them on?

New features are shipped behind flags first so they can be tested and changed before becoming default. You can turn them on in **Settings > Experiments**. Some need a DevTools reload, and some need a browser restart. Chrome Canary gets features earlier than Stable. Experimental features can change or disappear, so don't rely on them for team workflows.

### 345: What happens in a heap snapshot when you take it on a big app?

V8 pauses JavaScript, runs a full garbage collection, then walks every object in the heap and writes a graph of nodes and edges. DevTools then parses this and builds indexes like retained sizes. On an app with a large heap this can take seconds and temporarily use a lot of extra memory, sometimes enough to crash the tab. For very large heaps, use allocation sampling first to find suspicious areas, and take snapshots on smaller scenarios.

### 346: Why does the JS heap size in DevTools differ from the memory shown in Chrome's Task Manager?

The JS heap size is only memory used by JavaScript objects in V8. The Task Manager's memory footprint for a tab includes the whole renderer process: the DOM, CSS data, decoded images, GPU-related buffers, compiled code, fonts and more. A page can have a small JS heap but use a lot of memory for images or canvas. `performance.measureUserAgentSpecificMemory()` and the Task Manager give a wider picture.

### 347: How do you check what is keeping a `<canvas>` or image memory high?

Heap snapshots show the DOM node and its JS wrapper, but the pixel data mostly lives outside the JS heap. Use the Performance panel's Memory graph with GPU memory, Chrome's Task Manager (with the GPU memory column), and the Layers panel for layer memory. Big canvases with high DPR, many large decoded images, and layers for every list item are common causes.

### 348: How do you use DevTools to verify Content Security Policy problems?

CSP violations appear as errors in the Console and as issues in the Issues panel, with the blocked URL and the directive that blocked it. You can turn on **CSP Violation Breakpoints** in Sources to pause on the code that triggered a violation, for example an inline `eval`. With header overrides you can try a new CSP header without deploying, and a `Content-Security-Policy-Report-Only` header lets you see what would break first.

### 349: What are Trusted Types violation breakpoints?

If a page enforces Trusted Types with a CSP like `require-trusted-types-for 'script'`, assigning a plain string to sinks like `innerHTML` throws. In the Sources panel's breakpoints, under **CSP Violation Breakpoints**, you can check **Trusted Type Violations** to pause on such assignments. This shows you every place that needs to be changed to use a Trusted Types policy, which is a strong defense against DOM XSS.

### 350: How does the debugger handle code running in a cross-origin iframe with site isolation?

With site isolation, a cross-origin iframe runs in a different renderer process. DevTools attaches to each process as a separate target using `Target.setAutoAttach`, so frames from other origins appear as their own targets in Sources, Console contexts and Performance tracks. You can debug them as usual, but each one has its own separate JavaScript heap, so a heap snapshot of the main page doesn't include the iframe's objects.

### 351: A page has a slow LCP. How would you debug it with DevTools?

1. Set CPU and network throttling to match your users (the field data panel can suggest settings).
2. **Record and reload** in the Performance panel.
3. Find the LCP marker in the Timings track and check which element it was in the **LCP breakdown** insight.
4. See which phase is biggest. Long TTFB: look at the server and the **Document request latency** insight. Long load delay: the image is found late, so preload it or add `fetchpriority="high"`, and don't lazy load it. Long load duration: compress or resize it (see **Image delivery**). Long render delay: render-blocking CSS or JS, or the main thread is busy.
5. Make one change at a time and record again to confirm.

### 352: A button click feels slow. How would you find out why?

Record a trace in the Performance panel while clicking it, with CPU throttling on. Select the interaction in the **Interactions** track and look at the INP breakdown. Long input delay means some other task was running when you clicked, so find that task in the Main track. Long processing means your handlers are slow, so look at the flame chart under the `click` event. Long presentation delay means a big style recalculation, layout or paint after the handler, often from changing a lot of DOM at once.

### 353: How do you break up a long task found in the Performance panel?

Split the work into smaller pieces and give the main thread back to the browser between them, so it can handle input and paint. `scheduler.yield()` is the modern way where supported, with `setTimeout` as a fallback. Do the visible update first, and push non-urgent work (analytics, saving to storage) to after the next paint. After the change, the trace should show several short tasks instead of one long one.

```js
async function processItems(items) {
  for (const item of items) {
    processItem(item);
    if ("scheduler" in window && "yield" in scheduler) {
      await scheduler.yield();
    } else {
      await new Promise((resolve) => setTimeout(resolve, 0));
    }
  }
}
```

In real code you would yield every few milliseconds of work, not after every item.

### 354: What is layout thrashing, and how does it look in a trace?

Layout thrashing happens when code reads a layout value (like `offsetHeight` or `getBoundingClientRect()`) right after changing styles, in a loop. Each read forces the browser to run layout again. In a trace, you see a JavaScript task with many small purple **Layout** blocks inside it, each marked as a forced reflow. The fix is to do all the reads first, then all the writes.

```js
// bad: read and write in the same loop
items.forEach((el) => {
  el.style.height = `${el.offsetWidth / 2}px`;
});

// better: read everything, then write
const widths = items.map((el) => el.offsetWidth);
items.forEach((el, i) => {
  el.style.height = `${widths[i] / 2}px`;
});
```

### 355: An animation is janky. How would you investigate it?

Record a trace during the animation and look at the **Frames** track for dropped or partially presented frames. Check the Main track: if each frame has style, layout and paint work, the animation probably changes properties like `top`, `left`, `width` or `height`. Turn on **Paint flashing** and **Layer borders** in Rendering to see repaints and layers. Animating only `transform` and `opacity` lets the compositor run the animation without the main thread, which usually fixes it.

### 356: How do you check that an animation runs on the compositor?

In a trace, a compositor-only animation shows little or no work on the Main track during the animation, and the frames are drawn on the Compositor and GPU tracks. The **Animations** track can also show if an animation was not composited, with the reason, like animating a property that needs layout or paint. Paint flashing should stay quiet during the animation.

### 357: Why can too much `will-change` hurt performance?

Each element with `will-change: transform` usually gets its own compositor layer. Layers take GPU memory and make compositing slower, and on phones too many layers can make things worse or even crash the tab. Use the Layers panel to see the number of layers, their memory and why they exist. Add `will-change` only to elements that actually animate, and only around the time they animate.

### 358: How do you find out what is causing slow scrolling on a page?

Record a trace while scrolling and look for long tasks and dropped frames. Turn on **Scrolling performance issues** to find non-passive wheel and touch listeners, and **Paint flashing** to see what repaints. Common causes are scroll handlers doing heavy work or reading layout on every event, large repaints from `position: fixed` elements without their own layer, heavy `box-shadow` or `filter`, and huge DOM trees. `IntersectionObserver` and passive listeners usually replace scroll handlers.

### 359: How does DOM size affect performance, and how does DevTools show it?

A large DOM makes style recalculation, layout and memory more expensive, and makes queries like `querySelectorAll` slower. The **DOM size** insight in the Performance panel reports the total element count, the maximum depth and the most children of one parent, and it links large style and layout events to it. The Performance monitor shows the DOM node count live. Virtualizing long lists and using `content-visibility: auto` for offscreen sections reduce the work.

### 360: How do you check if `content-visibility: auto` is helping?

Record a page load or a scroll before and after adding it. With it, the browser skips layout and paint for offscreen sections, so the **Layout** and **Paint** events on load should be shorter. Use **Enable advanced paint instrumentation** or the Summary tab to compare rendering time. Also check CLS, because without `contain-intrinsic-size` the skipped content has zero height and can cause the scrollbar to jump.

### 361: The TTFB of the main document is high. What can DevTools tell you?

The Timing tab splits the request into DNS, connection, TLS, waiting and download, so you can see if the time is in the network setup or in the server. `Server-Timing` headers show the time spent in the backend's parts. The **Document request latency** insight checks for redirects, a slow server response and missing compression. If waiting time is high, the fix is on the server: caching, CDN, faster database queries, or streaming the HTML.

### 362: How do you find request chains that delay loading?

The **Network dependency tree** insight in the Performance panel (Lighthouse calls it critical request chains) shows chains of requests where each one starts only after the previous one finishes, like HTML loads CSS which loads a font which is needed for text. The Initiator chain in the Network panel shows the same for a single request. Fixes include `preload` for late-discovered resources, `preconnect` for important origins and flattening import chains.

### 363: How do you check if a `preconnect` hint actually helps?

Add the **Connection ID** column in the Network panel. Without `preconnect`, the first request to that origin shows DNS, connection and TLS time in its Timing tab. With a working `preconnect`, the connection is set up early, so the first request reuses it and those phases are near zero. The Network dependency tree insight also lists preconnected origins and warns about unused preconnects or having too many.

### 364: How can you tell if HTTP/2 or HTTP/3 connections are being reused?

Show the **Protocol** and **Connection ID** columns in the Network panel. Requests to the same origin over `h2` or `h3` should share one connection ID. If you see many different IDs for one origin, something is preventing reuse, for example different credentials mode (CORS requests with and without credentials use separate connections) or the server closing connections. HTTP/1.1 uses up to six connections per origin and requests wait in **Stalled** when they're all busy.

### 365: How would you debug a web font that makes text appear late?

In the Network panel, check when the font request starts; if it starts late, the CSS is found late or the font isn't preloaded. In a trace, the **Font display** insight flags fonts that block text rendering, which happens with the default `font-display` behavior. The Computed tab's **Rendered Fonts** shows whether a fallback was used. Fixes are `font-display: swap` or `optional`, preloading the main font, self-hosting, and subsetting.

### 366: How do you check whether images are too large for how they are shown?

The **Image delivery** insight in the Performance panel and Lighthouse list images that are larger than their displayed size, not in a modern format, or poorly compressed, with estimated savings. In the Elements panel, hovering an `<img>` shows its rendered size and intrinsic size. Check `currentSrc` in the Console to see which `srcset` candidate the browser picked, and test different DPR values in Device Mode.

### 367: How do you verify that lazy loading works correctly?

Load the page with the Network panel open and filter by **Img**. Offscreen images with `loading="lazy"` should not load until you scroll near them. The LCP image must not be lazy loaded; Lighthouse and the LCP breakdown flag this because it increases load delay. For lazy-loaded JavaScript chunks, the Network panel should show them only when the route or feature is used, and Coverage should show less unused code on first load.

### 368: How do you find duplicated or legacy JavaScript in your bundles?

The **Duplicated JavaScript** insight lists modules included more than once across bundles, usually two versions of the same library or the same code in several chunks. The **Legacy JavaScript** insight lists polyfills and transforms that modern browsers don't need. Both work best with source maps, because then DevTools can see the original modules. Fixing them usually means deduping dependencies and targeting modern browsers in your build.

### 369: How do you measure the effect of a performance fix reliably?

Use the same conditions before and after: same machine, same throttling, Incognito or a clean profile, and the same scenario (ideally a Recorder flow or a script). Run it several times and compare medians, because single runs vary. Look at the specific metric you wanted to change, not only the overall score. Save the before and after traces with annotations so others can check. After deploy, confirm the change in field data.

### 370: How would you catch performance regressions in CI?

Run Lighthouse CI or a Puppeteer script against a production build on each pull request, with fixed throttling and several runs. Set budgets for metrics like LCP, TBT and CLS, and for bundle sizes, and fail the build when they're exceeded. Save traces and reports as build artifacts so a developer can open them in DevTools. Lab checks in CI catch big regressions, while RUM catches what really affects users.

### 371: How do you find out which React components make an interaction slow?

Use the React DevTools Profiler to record the interaction and see which components rendered, how long each took, and why (with **Record why each component rendered** turned on). Then record the same interaction in the Performance panel to see the full picture, including layout and paint. React 19.2 and later can add React-specific tracks, like Scheduler and Components, to the Performance panel in development and profiling builds, so you can see renders next to the browser work.

### 372: How do you debug a hydration problem with DevTools?

Hydration mismatch errors appear in the Console in development, with the expected and actual content. Compare the server HTML (View page source or the document's **Response** tab in Network) with the DOM in Elements after hydration. Disabling JavaScript shows only the server-rendered version. In a trace, a long task right after the scripts load is often hydration; if it delays interactions, consider partial or lazy hydration.

### 373: A page fails the back/forward cache test. What are common reasons and fixes?

The test in **Application > Back/forward cache** lists the reasons. Common ones are:

- An `unload` event listener, often from a third-party script. Use `pagehide` instead.
- `Cache-Control: no-store` on the main document.
- An open WebSocket, WebRTC connection or IndexedDB transaction when leaving.
- `window.opener` references between pages.

Some reasons are marked as actionable (you can fix them) and others as pending support or browser-specific. Fixing them makes back navigation instant.

### 374: Prerendering with speculation rules is not working. How do you debug it?

Open **Application > Speculative loads**. Check that the rules were parsed without errors, then look at the attempts for the target URL. Each failed attempt has a reason, like the eagerness setting not being triggered yet, too many prerenders, low memory, a cross-site URL, or the page using an API that isn't allowed during prerender. When you navigate, the panel shows whether the activation used the prerendered page. You can also inspect the prerendered page itself from the panel before activating it.

### 375: Users get old JavaScript after a deploy. How do you debug it with DevTools?

Check where the old file comes from. The Size column shows `(ServiceWorker)`, `(disk cache)` or a network size. If it's the service worker, check **Application > Service workers** for a waiting worker and **Cache storage** for old entries; the worker's update and cache cleanup logic is probably wrong. If it's the HTTP cache, look at `Cache-Control` and `ETag` headers of the HTML and JS. The usual fix is hashed file names with long caching, and `no-cache` on the HTML.

### 376: How would you check a caching strategy for a site with DevTools?

Load the page with **Disable cache** off, then reload and navigate between pages. For each resource, check the response headers (`Cache-Control`, `ETag`, `Last-Modified`, `Vary`) and the Size column on repeat views. Hashed assets should come from cache without any request; the HTML should be revalidated or short-lived. The **Use efficient cache lifetimes** insight lists resources with short cache times. Also check that the CDN headers (`Age`, `X-Cache` and similar) show cache hits.

### 377: How do you reproduce a race condition between network requests?

Throttle the network so requests take longer, and make the order random or reversed. You can add latency to only one request by overriding it and delaying the response in a service worker, or with request interception in Puppeteer. Breakpoints inside response handlers let you pause one request while another finishes. Logpoints that print timestamps and request IDs show you the real order without changing timing much.

### 378: How do you debug a bug that only happens on page load and is too fast to catch?

Some options:

- Use **Script First Statement** or an event listener breakpoint like `DOMContentLoaded` to pause early.
- Turn on **Pause on exceptions** before reloading.
- Turn on **Preserve log** so errors before a redirect stay in the Console.
- Record a trace with **Record and reload** and look at what ran.
- Add a `debugger` statement with Local Overrides in the production file.
- Slow the page with CPU and network throttling so timing issues show up more often.

### 379: A bug only happens in production. How would you debug it?

Load production source maps (or add them by hand with **Add source map**) so you can read the code. Use Local Overrides to add logging or a `debugger` statement to the production files without deploying. Override response headers or API responses to reproduce the user's data. Compare with local by checking feature flags, environment config and the exact build version. Error trackers with stack traces help you find the right line before you open DevTools.

### 380: How do you test your app against a slow or failing API without changing the backend?

In DevTools, you can throttle the network, block specific request URLs, or use Local Overrides to replace the response body and headers with an error or slow mock. For dynamic behavior, like returning a `500` every third time or adding a delay, use a service worker or a mocking tool like MSW in the browser. In automated tests, use CDP request interception in Puppeteer or Playwright.

### 381: How do you debug an infinite loop that freezes the page?

Open the Sources panel and press the pause button (`F8`); DevTools can usually interrupt a busy loop and show where it is, with the call stack. If DevTools itself is stuck, close the tab, reopen it with DevTools already open, turn on **Pause on exceptions** or set a breakpoint before the loop, then reload. In React, a loop of re-renders often shows as a "Maximum update depth exceeded" error; the call stack shows the effect or state update causing it.

### 382: How do you find which script added a global variable?

Before the page loads, define a setter on `window` for that property that stops in the debugger. With Local Overrides or a snippet run at the start (use **Script First Statement** to pause early and run it), the debugger pauses when the variable is assigned, and the call stack shows the script.

```js
let value;
Object.defineProperty(window, "someGlobal", {
  configurable: true,
  get() {
    return value;
  },
  set(v) {
    debugger;
    value = v;
  },
});
```

This only works if the variable is set as a property, not with a top-level `let` or `const` in a classic script.

### 383: How do you find out which code changes a property on an object?

Wrap the property with a getter and setter that hit `debugger` when it is set, as with a global variable. For many properties, use a `Proxy` around the object during debugging. For DOM attributes, use **Break on attribute modifications** instead. For style changes, the same attribute breakpoint works on the `style` attribute.

```js
function watch(obj, key) {
  let value = obj[key];
  Object.defineProperty(obj, key, {
    configurable: true,
    get: () => value,
    set(v) {
      debugger;
      value = v;
    },
  });
}

watch(store.state, "user");
```

### 384: How would you investigate high CPU usage on an idle page?

Open the Performance monitor and check CPU usage, layouts per second and style recalcs per second while you don't touch the page. Record a few seconds of trace with nothing happening. Look for timers (`setInterval`), `requestAnimationFrame` loops, animations running offscreen, polling requests, or third-party widgets. The Bottom-up tab grouped by domain shows who uses the time. Pausing animations and timers when the tab or element isn't visible usually fixes it.

### 385: How do you find out if a third-party script is slowing your page?

In a trace, use **Dim 3rd parties** and the **Third parties** insight, which lists main thread time and transfer size per third-party entity. Group Bottom-up by third parties to see their total. Block the script's domain with request blocking and record again to measure the difference directly. Then decide whether to remove it, load it later, use `async`/`defer`, or move it to a web worker with a tool like Partytown.

### 386: How do you check that work moved to a web worker actually left the main thread?

Record a trace and look at the worker's own track. The heavy functions should run there, not on the Main track. Check the cost of `postMessage`: serializing large objects shows up on the main thread as structured clone work. If that's big, transfer `ArrayBuffer`s instead of copying, or send less data. The main thread should only show short tasks to send and receive messages.

### 387: How do you measure the cost of style recalculation for a CSS change?

Record the interaction that triggers the change and select the **Recalculate Style** event. The Summary shows how many elements were affected and how long it took. With **CSS selector stats** turned on, you see which selectors were expensive. If a single class change on `<body>` causes a recalculation of thousands of elements, scope the change to a smaller subtree or simplify the selectors.

### 388: How would you explain the rendering pipeline using what DevTools shows?

A frame goes through JavaScript (yellow), **Recalculate Style** and **Layout** (purple), **Paint** (green) on the main thread, then **Commit**, raster and compositing on other threads. DevTools shows each step in the Main, Raster, GPU and Compositor tracks. Changing a layout property runs every step. Changing a paint-only property like `color` skips layout. Changing `transform` or `opacity` on a composited layer can skip both and only composite.

### 389: Why can the Frames track show "partially presented" frames?

A partially presented frame means the compositor showed a new frame, but some updates from the main thread didn't make it in time. For example, scrolling was smooth because the compositor handled it, but content that depends on JavaScript was late. It's better than a dropped frame, but it means the main thread is still too busy. Look at what the Main track was doing during those frames.

### 390: How do you profile a page with an emulated low-end device and get meaningful numbers?

Use a calibrated CPU throttling preset (like low-tier mobile) so the slowdown matches devices instead of an arbitrary multiplier, and pick a network preset that matches your field data. Use Device Mode for the viewport so layout matches mobile. Close other apps, record several runs and compare medians. Remember throttling doesn't model memory or GPU limits, so confirm big findings on a real phone with remote debugging.

### 391: What is the difference between the Network track in the Performance panel and the Network panel?

The Network panel is for request details: headers, bodies, cookies, timing phases, filters, and it records continuously. The Network track in a trace shows requests on the same timeline as main thread work, so you can see how requests relate to rendering, like a script that downloaded early but executed late because the main thread was busy. Each request in the track shows its priority and render-blocking status.

### 392: How do you find out why the LCP element changes between runs?

LCP is the largest element painted before the user interacts, so it can change with viewport size, fonts, A/B tests, cookie banners or images that load at different speeds. In the live metrics view, the LCP card shows the element; check it across several reloads. In a trace, the Timings track may show several LCP candidates, with the last one being final. Make the intended hero element fast and stable, and make sure banners don't become the LCP.

### 393: How do you investigate a CLS that only happens for real users?

Field CLS includes shifts during the whole visit, like after scrolling or late-loading ads, which a load-only lab test misses. In the live metrics view, use the page as a user would, including scrolling, and watch the **Layout shifts** list. Use a timespan Lighthouse run for interactions. Common causes are ads and embeds without reserved space, images without `width`/`height`, late web fonts, and content inserted above the viewport after a fetch.

### 394: How do you debug a memory leak that only appears after hours of use?

Use allocation sampling or a series of heap snapshots over a shorter but faster loop of the suspected action, so you can reproduce hours of usage in minutes with a Recorder replay or a script. Watch the JS heap and DOM node count in the Performance monitor. Compare snapshots taken after N and 2N repeats; objects that grow in proportion are the leak. In production, `performance.measureUserAgentSpecificMemory()` can report memory growth from real users to confirm the fix.

### 395: How do you check that event listeners use `passive` correctly?

`getEventListeners(target)` shows the `passive` flag for each listener. The **Scrolling performance issues** option highlights non-passive wheel and touch listeners. Console Violation messages also warn about non-passive listeners on scroll-blocking events. Chrome treats `touchstart`, `touchmove` and `wheel` listeners on `window`, `document` and `body` as passive by default, but listeners on other elements are not.

### 396: How would you debug slow typing in a large text input or editor?

Record a trace while typing and look at the `keydown`, `input` and `keyup` interactions. Long processing often comes from validating or re-rendering the whole form on every key press. Long presentation delay comes from big layouts, for example an auto-growing textarea that changes height and reflows the page. Debouncing expensive work, updating only the changed parts, and avoiding layout reads in input handlers usually help.

### 397: How do you analyze the JavaScript parse and compile cost of a bundle?

In a trace, look for **Compile Script**, **Compile Code** and **Evaluate Script** events after each script loads. Their duration on a throttled CPU shows the cost of shipping that much code. Bottom-up grouped by URL helps compare bundles. Coverage tells you how much of that code was even used. Code splitting, removing unused dependencies, and relying on V8's code cache for repeat visits reduce this cost.

### 398: What is V8's code cache, and can you see its effect in DevTools?

When a script is loaded a few times, V8 stores its compiled bytecode in the browser's cache, so later loads can skip compiling it. In a trace, the **Compile Script** event shows the cache status, and repeat loads should have much shorter compile time. Changing the script content (a new hash) invalidates the cache. This is one reason stable vendor chunks with long caching help repeat visits.

### 399: How would you debug a page that is slow only when DevTools is closed?

That usually means a timing issue, not a performance issue, since DevTools normally adds overhead. Some causes are code that relies on Console calls (for example a getter that runs when logged), different caching (DevTools **Disable cache** off), or code that behaves differently when it detects DevTools. Use the Performance panel's recording on load with DevTools in a separate window, or measure with `performance.mark` and send results to the Console after the fact.

### 400: How do you check Core Web Vitals for a single-page app's route changes?

Core Web Vitals are measured per page load, so soft navigations in an SPA are counted as part of the first page. INP and CLS keep growing over the whole visit. In DevTools, the live metrics view keeps running across route changes, so you can see how interactions and shifts after navigation affect the values. Chrome has worked on soft navigation measurement, but until it's standard, RUM tools have to split metrics by route themselves.

### 401: Why can't you rely on hiding things from DevTools for security?

Everything the browser receives can be seen and changed by the user: HTML, JavaScript, API responses, cookies (even `HttpOnly` ones in DevTools), and local storage. Users can edit requests, replay them, change variables in the debugger and override files. So secrets must never be shipped to the client, and every check, like permissions, prices or validation, must also happen on the server. Minifying or obfuscating code only slows people down.

### 402: Can a website detect that DevTools is open or block it?

Sites can try tricks, like timing `debugger` statements, checking window size differences, or using getters that only run when an object is logged. None of them are reliable, they break often, and they annoy legitimate users. Users can get around them with **Deactivate breakpoints**, **Never pause here**, Local Overrides or an undocked window. Companies that really need to block DevTools use the `DeveloperToolsAvailability` enterprise policy on managed devices instead.

### 403: How do you debug a login that works locally but loses the session in production?

Check the `Set-Cookie` response on the login request in the Network panel's **Cookies** tab; blocked cookies have a warning with the reason. Typical reasons are `SameSite=Lax` cookies not being sent on cross-site requests, a missing `Secure` flag, the wrong `Domain`, or the API being on a different site than the frontend. Check that `fetch` uses `credentials: 'include'` for cross-origin calls and that the server sends `Access-Control-Allow-Credentials: true` with a specific origin.

### 404: How do you debug an OAuth or SSO redirect flow?

Turn on **Preserve log** in both the Network panel and the Console, so requests and errors stay across the redirects to the identity provider and back. Follow the chain of `302` responses and check the `Location` headers, the `state` and `code` parameters, and the cookies set at each step. Errors like a mismatched redirect URI usually show in the provider's response. Be careful not to share HAR files from this flow, since they contain tokens.

### 405: How do you debug cross-origin isolation problems?

Features like `SharedArrayBuffer` and precise timers need `crossOriginIsolated` to be `true`, which requires `Cross-Origin-Opener-Policy: same-origin` and `Cross-Origin-Embedder-Policy: require-corp` (or `credentialless`). Check `self.crossOriginIsolated` in the Console. **Application > Frames** shows the isolation status and the COOP and COEP values. Resources blocked by COEP appear in the Network panel and the Issues panel, and they usually need a `Cross-Origin-Resource-Policy` header or CORS.

### 406: How do you debug a Permissions Policy that blocks a feature?

If a feature like the camera, geolocation or fullscreen is blocked, the Console shows a violation message. **Application > Frames** lists the allowed and disabled features for each frame and the reason, like the `Permissions-Policy` header or a missing `allow` attribute on an iframe. You can test a different header with response header overrides before changing the server.

### 407: How do you debug third-party cookie and storage partitioning issues?

Chrome partitions storage like `localStorage`, IndexedDB and service workers for iframes by top-level site, and third-party cookies may be blocked depending on user settings. In **Application**, storage is listed by origin, and the Cookies table has a **Partition Key** column. The Network panel's Cookies tab shows why a cookie was blocked. The Issues panel reports third-party cookie problems. Use `Partitioned` cookies (CHIPS) or the Storage Access API for embeds that need their own state.

### 408: Why does a service worker not control a page you expect it to?

Common reasons: the page is outside the worker's scope (a worker at `/js/sw.js` can only control `/js/` unless `Service-Worker-Allowed` allows more), the page was loaded before the worker activated and `clients.claim()` was not called, the page was loaded with a hard reload (which bypasses the worker), or **Bypass for network** is on. **Application > Service workers** shows the scope and status, and `navigator.serviceWorker.controller` in the Console shows if the page is controlled.

### 409: How do you debug why a PWA is not installable?

Open **Application > Manifest**. It shows the parsed manifest, warnings, and an **Installability** section with the reasons the app can't be installed, like missing icons of the right size, a missing `name`, a wrong `start_url`, or the page not being served over HTTPS. Check that the manifest link is in the HTML and the file loads without errors in the Network panel.

### 410: How do you debug `postMessage` communication between a page and an iframe?

Run `monitorEvents(window, 'message')` in the Console of the receiving frame (choose it in the context dropdown) to log every message event with its data and origin. Set a breakpoint or a logpoint in the `message` handler to see the data at that point. Check that the handler verifies `event.origin`, and that the sender uses the exact target origin instead of `'*'`.

### 411: How do you profile CPU usage in Node.js?

Connect DevTools with `--inspect` and record in the **Performance** or **Profiler** tab of the Node DevTools window. For scripts, start Node with `--cpu-prof`, which writes a `.cpuprofile` file when the process exits; load it in DevTools to see a flame chart. In production, short profiles from a single instance, taken while it's under real load, give the most useful data.

```bash
node --cpu-prof --cpu-prof-dir=./profiles app.js
```

### 412: How do you debug Vitest or Jest tests with Chrome DevTools?

Run the test runner under the inspector and open `chrome://inspect`. With `--inspect-brk`, Node pauses on the first line so you can set breakpoints. Running tests in a single thread or file makes debugging easier, because workers run in separate processes.

```bash
node --inspect-brk ./node_modules/vitest/vitest.mjs run --no-file-parallelism src/cart.test.ts
node --inspect-brk ./node_modules/.bin/jest --runInBand src/cart.test.ts
```

Vitest also has an `--inspect-brk` option of its own. Many editors can do the same with their built-in debugger.

### 413: How do you debug server-side code of a Next.js app with Chrome DevTools?

Start the dev server with the Node inspector turned on, then connect from `chrome://inspect`. Next.js supports this with `next dev --inspect` (or `NODE_OPTIONS='--inspect' next dev` in older versions). Server components, route handlers and server actions run in that Node process, so you can set breakpoints and see `console.log` output from the server in DevTools. Browser code is debugged as usual in the page's own DevTools.

### 414: How do you debug a TypeScript Node app in DevTools with the original source?

Build with source maps (`"sourceMap": true` in `tsconfig.json`, or use a runner like `tsx` that supports them), then start Node with `--inspect` and `--enable-source-maps` for readable stack traces. DevTools loads the maps and shows the `.ts` files in the Sources panel. Recent Node versions can also run TypeScript files directly by stripping types, and line numbers stay the same, so no map is needed in that case.

### 415: What would you check if breakpoints in a Node process never hit?

Check that DevTools is attached to the right process (child processes and worker threads need their own inspector), that the file in DevTools is the one actually running (not a different build output), that source maps match, and that the code runs after you attach (use `--inspect-brk` for startup code). Also check that the script isn't on the ignore list, and that breakpoints aren't deactivated.

### 416: How do you debug a z-index that doesn't work?

`z-index` only compares elements within the same stacking context. In the Elements panel, walk up the ancestors and look for properties that create a new stacking context: `position` with a `z-index`, `opacity` less than 1, `transform`, `filter`, `isolation: isolate`, `will-change`, `contain` and others. The Layers panel can show the actual layer order. Usually the fix is to move the element out of that ancestor (like with a portal) or remove the property that creates the context.

### 417: How do you find what causes a horizontal scrollbar on a mobile page?

In Device Mode, scroll right to see where the overflow is. In the Console, list elements wider than the viewport:

```js
$$("*").filter(
  (el) =>
    el.getBoundingClientRect().right > document.documentElement.clientWidth,
);
```

Then inspect those elements in the Elements panel. Common causes are fixed widths, `100vw` (which includes the scrollbar), long words or URLs without wrapping, images without `max-width: 100%`, and negative margins.

### 418: Why doesn't `position: sticky` work, and how does DevTools help?

Sticky elements stop sticking when an ancestor has `overflow: hidden`, `auto` or `scroll`, because they stick to the nearest scrolling ancestor. They also need a `top` (or other inset) value and enough room in their parent. In the Elements panel, check the ancestors' computed `overflow`, and DevTools shows a `scroll` badge on scroll containers. The inactive CSS hints may also explain why `top` has no effect.

### 419: How does DevTools help debug `<dialog>`, popovers and the top layer?

Elements shown in the top layer, like a modal `<dialog>` opened with `showModal()` or an element with the `popover` attribute, get a `top-layer` badge and are listed in a `#top-layer` section at the end of the DOM tree, with links back to the element. The `::backdrop` pseudo-element appears in the tree so you can style it. Forcing `:popover-open` or `:open` states and checking focus with Live Expressions help with these components.

### 420: How do you debug CSS anchor positioning?

When you select an element positioned with `position-anchor` or `anchor()`, DevTools shows which element it's anchored to, and the anchor gets a badge in the DOM tree. Clicking the badge or the anchor name in the Styles pane selects the other element. You can see which `position-try` fallback is used when there's not enough room, by resizing the viewport in Device Mode and watching the styles.

### 421: How do you debug view transitions?

The Animations panel captures view transitions, so you can pause, slow down and scrub them. During a transition, the pseudo-elements like `::view-transition`, `::view-transition-group(name)`, `::view-transition-old(name)` and `::view-transition-new(name)` appear in the DOM tree, and you can inspect their styles. Pausing in the Animations panel keeps them on screen so you can find wrong `view-transition-name` values or bad sizes.

### 422: How do you debug scroll-driven animations?

Scroll-driven animations (`animation-timeline: scroll()` or `view()`) show up in the Animations panel and in the Styles pane like other animations. You can scroll the page while watching the animation's progress, and edit the `animation-range` values live. Since the timeline is the scroll position, slowing down the animation speed doesn't apply; you control it by scrolling. Some versions of DevTools have extra visualizations for the scroll timeline.

### 423: How do you debug autofill problems on a form?

The **Autofill** panel (**More tools > Autofill**) shows what Chrome autofilled on the page: each field, the value filled, the autofill type Chrome inferred (like `email` or `postal-code`) and how it decided (the `autocomplete` attribute or heuristics). If a field gets the wrong data, check that it has a correct `autocomplete` attribute and a label. You can also see autofill-related issues in the Issues panel.

### 424: How do you test right-to-left layout with DevTools?

Edit the `<html>` element in the Elements panel and set `dir="rtl"` (and a `lang` like `ar`). Check that layout uses logical properties like `margin-inline-start` instead of `margin-left`, and that icons that point in a direction are mirrored. You can override the locale in **Sensors** to check date and number formats from `Intl`. Use Local Overrides if you need it to survive reloads.

### 425: How would you debug a GraphQL API in the Network panel?

GraphQL usually sends everything as `POST` to one URL, so filter by that path and look at the **Payload** tab to see the `operationName`, query and variables of each request. GraphQL often returns `200` even when there are errors, so check the response body for an `errors` array. Adding the operation name to the URL as a query parameter, or using a GraphQL DevTools extension, makes it easier to tell requests apart.

### 426: How do you work with a very large JSON response in DevTools?

The Preview tab can be slow with huge responses. Right-click the request and use **Copy response**, then paste it into the Console as `const data = <pasted JSON>`, or log the parsed object and use **Store as global variable**. Then use `console.table`, `Object.keys`, or array methods to look at the parts you need. For repeated analysis, export a HAR and process it with a script.

### 427: How can logging slow down your app or mislead you?

Logging large objects, or logging in hot paths like scroll handlers and render functions, makes the Console keep references and serialize data, which takes time and memory while DevTools is open. Objects are also logged by reference: when you expand them later, you see their current value, not the value at log time. Log a copy (`structuredClone(obj)` or `JSON.stringify`) when the value at that moment matters, and remove noisy logs from production builds.

### 428: Why does an object in the Console sometimes show different values when you expand it?

The preview line is taken at the time of logging, but when you expand the object, DevTools reads its properties at that moment. If the code changed the object in between, the expanded view shows the new values. DevTools shows a small info icon that says the value was evaluated just now. To keep a snapshot, log `structuredClone(obj)`, `{ ...obj }` for a shallow copy, or `JSON.stringify(obj)`.

### 429: How do you debug a CSS specificity conflict in a large codebase?

Select the element and look at the Styles pane, where rules are sorted by the cascade, including layers, origin and `!important`. Hover a selector to see its specificity. The Computed tab shows which rule won for a property and lists the losing ones. Click through to the source files to see which stylesheet each rule is from. The long-term fix is usually cascade layers or scoping (`@scope`, CSS modules) instead of more specific selectors or `!important`.

### 430: How would you make DevTools part of your team's debugging workflow?

Share Workspace setups (or the automatic workspace JSON) so CSS edits save to source. Use Snippets for common tasks and keep them in the repo for others to paste. Save Recorder flows for repeatable bug reproduction and performance tests. Share traces with annotations instead of screenshots when reporting performance issues. Agree on ignore list settings so stack traces show only your code, and use sanitized HAR files for network bugs.

### 431: How do Chrome DevTools compare with Firefox and Safari developer tools?

All three have elements, console, debugger, network, storage and performance tools, and the basics work the same. Chrome has the most advanced performance tooling, Lighthouse, Recorder and CDP-based automation. Firefox has strong CSS layout tools, like the Grid inspector, and good accessibility checks. Safari's Web Inspector is the only way to debug pages on iOS. Since layout and rendering differ between engines, you need each browser's tools for browser-specific bugs.

### 432: How do enterprise policies affect DevTools?

Admins can control DevTools with policies like `DeveloperToolsAvailability`, which can allow DevTools, block it everywhere, or block it only for extensions installed by policy. Other policies control AI features in DevTools and remote debugging. If DevTools doesn't open on a work machine, check `chrome://policy`. This is the only reliable way to restrict DevTools, since page-level tricks don't work.

### 433: How would you debug a memory leak caused by a detached iframe?

Removing an iframe from the DOM should free its document, but if the parent page keeps a reference to the iframe's `window`, `document` or any object created inside it, the whole frame's heap can stay alive. In a heap snapshot, look for extra `Window` or `HTMLDocument` objects and check their retainers. The Performance monitor's **Documents** and **Document frames** counters growing after closing iframes is a clear sign.

### 434: How would you approach debugging a performance issue that a customer reports but you can't reproduce?

Ask for details like device, browser version, network and the exact steps, and check RUM data for that segment. Try to match their conditions with calibrated CPU throttling, network throttling and their screen size. If you still can't reproduce it, ask them to record a trace in the Performance panel and send the file, with source maps excluded if needed. Annotated traces from users often show the problem, like a browser extension or a huge dataset in their account.

### 435: What are the trade-offs of recording a trace with screenshots and JavaScript samples on?

Screenshots give a filmstrip that makes it easy to match the timeline to what the user saw, and JS samples give the call stacks you need to find slow functions. Both make the trace bigger and add some overhead, which can slightly change timing. For long recordings, or when you only care about network and rendering, turning them off keeps the file small and the panel fast. For short focused recordings, keep both on.

### 436: How do you debug code that runs inside a browser extension's content script?

Content scripts run in an isolated world on the page. In the page's DevTools, choose the extension in the Console context dropdown to run code in that world. In the Sources panel, the **Content scripts** tab lists the extension's scripts, where you can set breakpoints. The extension's service worker and popup have their own DevTools, opened from `chrome://extensions` and by right-clicking the popup and choosing **Inspect**.

### 437: How do you find out if a browser extension is breaking your site?

Open the site in an Incognito window or a fresh Chrome profile without extensions and see if the bug disappears. In DevTools, look for scripts from `chrome-extension://` URLs in the Sources panel's **Content scripts** tab, and for DOM nodes the extension injected. In a performance trace, extension scripts appear in the flame chart with their own URLs. Error trackers often filter out these errors because they don't come from your code.

### 438: How would you use the DevTools MCP server to verify a frontend fix an AI agent made?

Give the agent access to a separate Chrome profile through the MCP server and ask it to open the page, reproduce the bug, and check the Console messages and network requests after its change. For performance work, ask it to record a trace and report insights like LCP breakdown before and after. You still review the code and the results, but it shortens the loop of "change, reload, check" and gives the agent real data instead of guesses.

### 439: How do you check that a website is ready for a CSP with `strict-dynamic` and nonces?

Deploy the policy as `Content-Security-Policy-Report-Only` first, or add it with header overrides in DevTools. Browse the main flows and watch the Console and Issues panel for violations, which list the blocked script or inline code. Turn on **CSP Violation Breakpoints** to find the code that injects scripts without a nonce. Once there are no violations, switch to the enforcing header.

### 440: How do you debug a WebSocket connection that keeps disconnecting?

In the Network panel, select the WebSocket and check the **Messages** tab for the last messages and close frames, and the **Headers** tab for the handshake status (`101 Switching Protocols`). Note the timing between disconnects; regular intervals often point to proxy or load balancer idle timeouts, which need ping/pong heartbeats. The Console shows close codes if your code logs them. Throttling to **Offline** and back tests your reconnect logic.

### 441: What can the Performance panel tell you about garbage collection pauses?

GC events like **Minor GC** and **Major GC** appear in the Main track inside tasks. Many minor GCs during an interaction mean the code creates a lot of short-lived objects, for example in an animation loop. Long major GCs add pauses that can drop frames. Allocation sampling in the Memory panel shows which functions allocate the most, and reusing objects or arrays in hot code reduces the pressure.

### 442: How do you use DevTools to check the cost of a framework's change detection or re-rendering?

Record the interaction and look at the flame chart under the event: framework internals (like React's commit work, or Angular's change detection) appear as repeated patterns. Bottom-up grouped by URL shows how much time is in framework code compared to your components. The framework's own DevTools profiler tells you which components ran. Comparing the two shows whether the cost is in rendering too many components or in the DOM work after it.

### 443: What is the best way to debug an error that has a minified stack trace from production?

Get the exact build's source maps, and map the stack with your error tracker or a tool that applies source maps. In DevTools, you can open the production page, load the source map with **Add source map**, and go to the line and column from the stack trace with `Ctrl+P` and `file.js:line:column`. Breakpoints and Local Overrides then let you reproduce the error with real code. Releasing with build IDs makes matching maps much easier.

### 444: How do you decide which DevTools tool to use for a vague "the site is slow" complaint?

Start with the Performance panel's live metrics and field data to see which metric is bad: LCP points to loading, INP to interactions, CLS to layout stability. Then record a trace for that scenario and read the insights. Use the Network panel for request details, Coverage for unused code, and the Memory panel if it gets slower over time. Lighthouse gives a quick overview but shouldn't be the only tool.

### 445: What would you check if a page looks different in Device Mode compared to a real phone?

Check the viewport meta tag, because Device Mode respects it but small differences in how mobile browsers handle it can appear. Real phones may have a different DPR, fonts, browser UI that changes the viewport height (`100vh` vs `100dvh`), safe areas, and text size settings. Touch behavior and hover media queries also differ. Remote debugging the real phone with `chrome://inspect` shows the actual computed styles.

### 446: How do you check that your site works for users who prefer reduced motion?

Set `prefers-reduced-motion: reduce` in the Rendering tab and use the site. Animations and transitions that move a lot should stop or be replaced with simpler ones. The Animations panel shows if any animations still run. Also check auto-playing carousels and parallax effects implemented in JavaScript, which need a `matchMedia('(prefers-reduced-motion: reduce)')` check.

### 447: How do you debug an issue where clicks don't reach an element?

Use inspect mode on the spot you are clicking; the element that gets selected is the one actually on top, often a transparent overlay or a pseudo-element. Check `pointer-events: none` on the target or `pointer-events` on overlays, and z-index and stacking contexts. `document.elementFromPoint(x, y)` in the Console tells you which element is at a point. An event listener breakpoint for **Mouse > click** shows if a handler calls `stopPropagation()` or `preventDefault()`.

### 448: What happens, step by step, when you click "Inspect" on an element?

1. Chrome opens DevTools (or focuses it) and attaches it to the tab's renderer through CDP.
2. DevTools enables domains like `DOM`, `CSS` and `Overlay`, and requests the document tree.
3. Chrome finds the node under the cursor and sends its node ID; DevTools expands the tree to it and selects it.
4. DevTools asks for matched styles, computed styles and the box model for that node with `CSS.getMatchedStylesForNode` and similar commands.
5. The Styles and Computed panes render, and `Overlay` commands draw the highlight on the page.
6. From then on, DOM change events keep the tree in sync as the page updates.

### 449: What would you say are the strengths and weaknesses of Chrome DevTools?

Strengths: built in and free, a very complete set of tools, strong performance tooling with insights and field data, deep integration with V8, source maps and Workspaces, automation through CDP, Puppeteer, Lighthouse and the MCP server, and a fast release cycle.

Weaknesses: it only covers Chromium browsers, emulation is not the same as real devices, the number of panels and options can be confusing, some features change or move often, and lab measurements can differ a lot from what real users see.

### 450: Walk through how you would debug a page that freezes for a second after clicking "Add to cart".

1. Open the Performance panel with CPU throttling and record while clicking the button.
2. Find the interaction in the Interactions track and read its INP breakdown.
3. If processing is long, follow the wide bars under the `click` handler in the flame chart to the slow function, with Bottom-up for self time.
4. If there are forced reflows, fix the read/write order. If it's a large re-render, check the framework profiler for components that didn't need to render.
5. If input delay is long, find the task that was running before the click, like a third-party script.
6. Check the Network track to see if the UI waits for a request that could be done after showing feedback.
7. Make the fix, show feedback first and yield before non-urgent work, then record again and compare the traces.
